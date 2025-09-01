from game.table import PokerTable



def main():
    table = PokerTable(num_players=6)
    table.post_blinds()

    table.deal_hole_cards()
    table.betting_round()

    table.deal_flop()
    table.betting_round()

    table.deal_turn()
    table.betting_round()

    table.deal_river()
    table.betting_round()

    table.show_table()
    table.resolve_showdown()


if __name__ == "__main__":
    main()
