import random
from .constants import RANKS, SUITS

class Deck:
    def __init__(self):
        """Initialize and shuffle a standard 52-card deck with tuple-style cards."""
        self.cards = [(rank, suit) for rank in RANKS for suit in SUITS]
        self.shuffle()

    def shuffle(self):
        """Randomly shuffle the deck."""
        random.shuffle(self.cards)

    def deal(self, n):
        """Deal n cards from the top of the deck.

        Raises:
            ValueError: If not enough cards remain to deal.
        """
        if n > len(self.cards):
            raise ValueError(f"Cannot deal {n} cards — only {len(self.cards)} left.")
        return [self.cards.pop() for _ in range(n)]

    def reset(self):
        """Reset the deck to a full 52-card set and shuffle."""
        self.cards = [(rank, suit) for rank in RANKS for suit in SUITS]
        self.shuffle()
