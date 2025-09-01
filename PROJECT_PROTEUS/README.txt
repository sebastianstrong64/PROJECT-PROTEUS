Project Overview: PROTEUS Poker Simulation


PROTEUS is a high-concept simulation of 6-max No Limit Texas Hold’em designed to explore strategic evolution, psychological modeling, and adaptive AI. It creates a realistic poker ecosystem where bots interact, learn, and evolve across many games — producing rich insights into strategy, psychology, and dynamic decision-making.

🎯
Ultimate Goals
Simulate a dynamic poker world where each bot represents a unique player with distinct traits.

Test hypotheses about adaptability, memory, emotional control (tilt), and strategy evolution.

Model realistic game mechanics, including blinds, chip stacks, betting rounds, and positional advantage.

Track long-term performance and strategic shifts over hundreds of hands or “time units.”

Identify which types of players thrive in dynamic environments: rigid optimizers vs adaptive strategists, emotionally stable vs impulsive, etc.

🔩
Core Simulation Components


🔹 PokerTable (Game Environment)
Central controller for each hand.

Manages:

Dealing (hole cards, flop, turn, river)

Pot size

Posting blinds

Betting rounds

Community cards

Turn order and position logic

Interfaces with Player and Deck objects.

🔹 Player Object (Bot)


Each bot has:

Name/ID

Hole cards

Chip count

Current bet in round

Folded status

Position (dealer, SB, BB, etc.)

Personality traits:

Aggression (how often they raise)

Tightness (how selective they are with hands)

Bluff frequency

Tilt sensitivity

Adaptability

Strategic disorder (willingness to deviate from GTO)

Memory score (how reliably they recall past scenarios)

Game IQ (how well they detect opponent strategies)



These values form the bot’s behavioral profile and influence all decisions.

🔹 Blinds and Betting
Each hand starts with small blind and big blind automatically posted.

Turn order rotates each hand, respecting positional flow.

Betting rounds:

Pre-flop, Flop, Turn, River

Bots can fold, check, call, bet, or raise

Pot updates based on chip contributions

Chip counts reduce accordingly

Players with 0 chips are eliminated

🧠
AI & Evolution Layer


🔹 Memory System
Bots store past strategies that worked against certain types of opponents.

Each stored “memory” includes:

Opponent type (based on observed stats)

Strategy used

Result (success/failure)

Memory score governs:

How quickly memories decay

How easily successful memories are recalled and reused

Frequently used memories become cheaper to access, simulating reinforced learning.

🔹 Tilt Model (Emotional Reactivity)
Tilt is a numerical variable that increases when:

Bot folds pre-flop and would’ve won

Bot loses several hands in a row

Bot gets bluffed or beaten badly

High tilt causes:

Over-aggressive plays

Poor hand selection

More calling or bluffing

Tilt decays exponentially after a win or rest period

🔹 Strategic Adaptation Engine
Bots analyze opponent tendencies over time:

Fold-to-3-bet %

Bluff frequency

Trap frequency

Continuation bet %

Based on IQ and adaptability, bots adjust their strategy mid-game.

Some bots play static GTO, others exploit, others evolve rapidly

High-IQ bots are better at:

Identifying targetable weaknesses

Recognizing when they are being exploited

Switching strategy profiles to counter adaptations

🔹 Strategic Disorder Variable
Represents how chaotic a bot is willing to be when facing superior opponents

High disorder bots may:

Make intentionally weird plays

Randomize actions

Force suboptimal but unpredictable lines

Useful in non-static environments, where predictability is a weakness

🧪
Simulation Flow
Generate a large pool of bots (50–200), each with randomized but structured traits

Simulate hundreds of games across time units

After a set number of hands:

Rank players by total earnings

Log tilt trends, adaptations, memory usage

Select top 6 bots (highest earners) for a final battle:

Play 10+ cash games

Let them adapt and exploit each other

Export data on:

Strategic success

Emotional volatility

Memory effectiveness

Adaptation quality

📊
Analysis & Outcome Goals
Determine which personality profiles perform best long-term

Test whether adaptive chaos can beat fixed GTO

Observe how bots counter-exploit each other in layered strategy battles

Identify emergent behaviors like:

Bots selectively showing bluffs to induce tilt

Bots recognizing repetition in strategy cycles

Bots exploiting others’ memory patterns