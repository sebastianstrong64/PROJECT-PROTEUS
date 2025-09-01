from .deck import Deck
from .player import Player
from bots.bot import Bot
from game.hand_evaluator import pick_winners, evaluate_hand_strength_0_1, hand_class_string


class PokerTable:
    def __init__(self, num_players=6):
        self.deck = Deck()
        self.players = [Bot(f"Bot {i+1}") for i in range(num_players)]
        self.community_cards = []
        self.pot = 0
        self.small_blind = 10
        self.big_blind = 20
        self.dealer_position = 0

    def deal_hole_cards(self):
        for player in self.players:
            player.receive_hand(self.deck.deal(2))

    def deal_flop(self):
        self.community_cards.extend(self.deck.deal(3))

    def deal_turn(self):
        self.community_cards.append(self.deck.deal(1)[0])

    def deal_river(self):
        self.community_cards.append(self.deck.deal(1)[0])

    def show_table(self):
        print("Community Cards:", self.community_cards)
        for p in self.players:
            print(p.show_hand())

    def post_blinds(self):
        sb = (self.dealer_position + 1) % len(self.players)
        bb = (self.dealer_position + 2) % len(self.players)

        self.players[sb].chips -= self.small_blind
        self.players[sb].current_bet = self.small_blind
        self.pot += self.small_blind

        self.players[bb].chips -= self.big_blind
        self.players[bb].current_bet = self.big_blind
        self.pot += self.big_blind

    def betting_round(self):
        for player in self.players:
            if not player.in_hand:
                continue

            # Only bots supported for now
            if isinstance(player, Bot):
                hand_strength = evaluate_hand(player.hand, self.community_cards)

                game_state = {
                    "hand_strength": hand_strength,
                    "community_cards": self.community_cards,
                    "pot_size": self.pot,
                    "player_chips": player.chips,
                    "num_players": len([p for p in self.players if p.in_hand]),
                    "position": self.players.index(player),
                }

                action, amount = player.decide_action(game_state)
                print(f"{player.name} -> {action.upper()} (${amount})")
                self.pot += amount
            else:
                print("Non-bot player detected (unsupported).")

    def rotate_dealer(self):
        self.dealer_position = (self.dealer_position + 1) % len(self.players)

    def reset_round(self):
        self.community_cards = []
        self.pot = 0
        self.deck = Deck()
        for p in self.players:
            p.reset_for_new_hand()

    def resolve_showdown(self):
        """Evaluate all live hands, announce winners, and split the pot (no side pots)."""
        result = pick_winners(self.players, self.community_cards)
        winners = result["best"]

        if not winners:
            print("No players eligible at showdown.")
            return

        # Print everyone’s final hand class
        print("\n--- SHOWDOWN ---")
        for p, score in result["scores"].items():
            hand_cls = result["class"][p]
            hand_str = " ".join([f"{r}{s}" for r, s in p.hand])
            print(f"{p.name}: {hand_str} -> {hand_cls} (score {score})")

        # Split pot equally among tied winners (rounding down), handle remainders
        share = self.pot // len(winners)
        remainder = self.pot - share * len(winners)

        for w in winners:
            w.chips += share

        # simple rule: give leftover chips (if any) to the earliest-position winner
        if remainder > 0:
            winners_sorted = sorted(
                winners, key=lambda pl: self.players.index(pl)
            )
            winners_sorted[0].chips += remainder

        names = ", ".join(w.name for w in winners)
        print(f"Winners: {names} — each gets {share}" + (
            f", +{remainder} extra to {winners[0].name}" if remainder else ""))
        self.pot = 0