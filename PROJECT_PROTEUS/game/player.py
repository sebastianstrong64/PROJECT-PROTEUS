class Player:
    def __init__(self, name, chips=1000):
        self.name = name
        self.hand = []
        self.chips = chips
        self.in_hand = True
        self.current_bet = 0

    def receive_hand(self, cards):
        self.hand = cards

    def show_hand(self):
        hand_str = " ".join([f"{rank}{suit}" for rank, suit in self.hand])
        return f"{self.name}'s hand: {hand_str}"

    def bet(self, amount):
        if amount <= self.chips:
            self.chips -= amount
            self.current_bet += amount
            return amount
        return 0

    def fold(self):
        self.in_hand = False

    def check(self):
        # Optional logic can be added here later
        pass

    def reset_for_new_hand(self):
        self.hand = []
        self.in_hand = True
        self.current_bet = 0

    def __str__(self):
        hand_str = " ".join([f"{rank}{suit}" for rank, suit in self.hand])
        return f"{self.name} | Hand: {hand_str} | Chips: {self.chips} | Bet: {self.current_bet} | In Hand: {self.in_hand}"
