import numpy as np
from game.player import Player
from bots.archetypes import ARCHETYPE_PROFILES
from random import random


class Bot(Player):
    def __init__(self, name, chips=1000, archetype=None):
        super().__init__(name, chips)

        # 🎭 Assign archetype
        self.archetype = archetype or self.assign_archetype()

        # 🎯 Generate traits
        self.traits = self.generate_traits()

        # 🧠 Internal states
        self.tilt = 0.0
        self.memory = {}
        self.model = None  # Placeholder for future NN logic

    def assign_archetype(self):
        return np.random.choice(list(ARCHETYPE_PROFILES.keys()))

    def generate_traits(self):
        ALL_RANDOM_TRAITS = [
            "tilt_sensitivity",
            "adaptability",
            "strategic_disorder",
            "memory_score",
            "game_iq"
        ]

        traits = {}

        # Archetype-driven traits
        profile = ARCHETYPE_PROFILES[self.archetype]
        for trait, (mean, std) in profile.items():
            traits[trait] = float(np.clip(np.random.normal(mean, std), 0, 1))

        # Fully randomized traits
        for trait in ALL_RANDOM_TRAITS:
            traits[trait] = float(np.clip(np.random.normal(0.5, 0.15), 0, 1))

        return traits

    def decide_action(self, game_state):
        """
        Simple decision logic using hand strength and traits.
        game_state should include:
            - 'hand_strength': float between 0 and 1
        """
        hand_strength = game_state.get("hand_strength", 0.5)

        aggression = self.traits["aggression"]
        bluff_freq = self.traits["bluff_freq"]
        tightness = self.traits["tightness"]

        # Strong hand: bet or check
        if hand_strength > (1 - tightness):
            if random() < aggression:
                amount = int(self.chips * 0.1)
                self.bet(amount)
                return "bet", amount
            else:
                self.check()
                return "check", 0

        # Medium-strength hand
        elif hand_strength > 0.4:
            if random() < 0.5:
                self.check()
                return "check", 0
            else:
                amount = min(self.chips, 10)
                self.bet(amount)
                return "bet", amount

        # Weak hand
        else:
            if random() < bluff_freq:
                amount = min(self.chips, 15)
                self.bet(amount)
                return "bluff", amount
            else:
                self.fold()
                return "fold", 0

    def __str__(self):
        trait_summary = ", ".join([f"{k}: {v:.2f}" for k, v in self.traits.items()])
        return f"{self.name} ({self.archetype}) | Traits: {trait_summary}"
