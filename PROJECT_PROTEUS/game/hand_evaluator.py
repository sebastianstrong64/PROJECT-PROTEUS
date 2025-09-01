# game/hand_evaluator.py
from treys import Card, Evaluator

# Map your symbols to treys one-letter suits and "10" -> "T"
SUIT_MAP = {"♠": "s", "♥": "h", "♦": "d", "♣": "c"}
RANK_MAP = {
    "2": "2", "3": "3", "4": "4", "5": "5", "6": "6",
    "7": "7", "8": "8", "9": "9", "10": "T", "J": "J",
    "Q": "Q", "K": "K", "A": "A",
}

evaluator = Evaluator()

def _to_treys_str(rank: str, suit: str) -> str:
    try:
        return f"{RANK_MAP[rank]}{SUIT_MAP[suit]}"
    except KeyError as e:
        raise ValueError(f"Bad card input: {(rank, suit)}") from e

def convert_to_treys(cards):
    """cards: list[tuple[str,str]] like [("A","♠"), ("K","♥")]"""
    return [Card.new(_to_treys_str(rank, suit)) for rank, suit in cards]

def evaluate_raw_score(hole_cards, community_cards) -> int:
    """Lower is better. Uses Treys total ordering (1..7462)."""
    board = convert_to_treys(community_cards)
    hole = convert_to_treys(hole_cards)
    return evaluator.evaluate(board, hole)

def evaluate_hand_strength_0_1(hole_cards, community_cards) -> float:
    """Optional: normalized strength for bots (higher is better)."""
    score = evaluate_raw_score(hole_cards, community_cards)
    return round(1.0 - (score / 7462.0), 4)

def hand_class_string(score: int) -> str:
    """Human-readable class: 'High Card', 'Pair', ... 'Straight Flush'."""
    return evaluator.class_to_string(evaluator.get_rank_class(score))

def pick_winners(players, community_cards):
    """
    players: list of Player (must have .hand and .in_hand == True if not folded)
    Returns: dict with keys:
        - 'scores': {player: score}
        - 'best': list[Player]  # all winners (ties possible)
        - 'class': {player: class_string}
        - 'min_score': int
    """
    live_players = [p for p in players if p.in_hand and len(p.hand) == 2]
    if not live_players:
        return {"scores": {}, "best": [], "class": {}, "min_score": None}

    scores = {}
    classes = {}
    min_score = None

    for p in live_players:
        s = evaluate_raw_score(p.hand, community_cards)
        scores[p] = s
        classes[p] = hand_class_string(s)
        min_score = s if (min_score is None or s < min_score) else min_score

    winners = [p for p, s in scores.items() if s == min_score]
    return {"scores": scores, "best": winners, "class": classes, "min_score": min_score}
