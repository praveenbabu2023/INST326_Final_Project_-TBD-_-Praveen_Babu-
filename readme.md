# All or Nothing
By: Praveen Babu, Samantha Koppe, Amira Thompson and Mekiyas Seleshi

## Game Description
All or Nothing is a card game where players take turns drawing cards to build points each round. 
Each card can add or subtract points. After each draw, the player decides to keep going or stop 
and save their points. If a player goes over 50 points in one turn, they lose all points from 
that round. The goal is to be the first player to reach 100 total points by balancing risk and 
safe choices. Also, any 7 has a special effect. It doubles the player’s current turn score and then adds 7 more points. If a player draws more than three cards of the same suit in one turn, 15 points is added to their turn score.

## Each File's Purpose
| File | Purpose |
|---|---|
| finalproject.py | This is the main Python file. It contains the game classes, player turns, card effects, scoring, and text-based user interface. |
|cards.txt| This file stores the card data. Each line has the card rank, suit, value, and effect. |
| README.md| This file explains the project, how to run it, how to use it, the sources used, the rules and who contributed to what portion of the project.|
 
## How to Run All or Nothing
To run the program, make sure finalproject.py and cards.txt are saved in the same folder. Then open the terminal in the project folder and run python finalproject.py. The program should start in the terminal.

## Rules/How to Play All or Nothing
When the game starts, enter the number of players. Then enter each player name.

On each turn, type Draw Card to draw a card. Type End to save your points and end your turn.

After each draw, the program shows the card drawn, the card value, the card effect, the turn score, and the total score.

The turn score is the points from the current turn. These points are not safe until the player types End. The total score is the points the player has already saved.

If the turn score goes over 50, the player busts and loses the points from that turn. A score of exactly 50 is safe. The first player to reach 100 or more total points wins.

Any 7 card doubles the current turn score and then adds 7 points. If a player draws more than three cards of the same suit in one turn, 15 points are added to their turn score.

## Annotated Bibliography

Blackjack  
https://sites.math.duke.edu/~rtd/MEC/prob/blackjack.html  
This source was used as background information for how card games handle drawing and stopping. It helped us design the main idea of players choosing whether to keep drawing cards or stop to save their points.

Poker  
https://bicyclecards.com/how-to-play/basics-of-poker  
This source was used to understand strategy in card games. It helped us think about how players make decisions based on risk and possible outcomes.

Random Library
https://www.w3schools.com/python/module_random.asp  
This source was used to understand the Python random module. It helped us understand how random functions can be used to shuffle or randomize items. We used random.shuffle() in the Deck class to shuffle the cards after getting permission to use the random module.

GitHub: Organizing Information with Tables  
https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-tables  
This source was used to format tables in the README.md file.

GitHub: Basic Writing and Formatting Syntax  
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax  
This source was used for Markdown formatting in the README.md file.

## Attribution Table

| Method/Function | Primary Author | Technique Claimed |
|---|---|---|
| Game.take_turn() | Praveen Babu | N/A |
| Game.check_same_suit_bonus() | Praveen Babu | Significant original algorithm |
| Scoreboard.display_scores() | Praveen Babu | 3. f-strings containing expressions |
| Scoreboard.get_leader() | Praveen Babu | 9. use of a key function with max() |
| Player.__init__() | Samantha Koppe | N/A |
| Player.add_drawn_card() | Samantha Koppe | N/A |
| Player.is_capped() | Samantha Koppe | 2. optional parameters and/or keyword arguments |
| Deck.load_cards() | Amira Thompson | 4. with statements; 6. sequence unpacking; 11. composition of two custom classes |
| Deck.shuffle() | Amira Thompson | N/A |
| Deck.draw_card() | Amira Thompson | N/A |
| Card.__str__() | Mekiyas Seleshi | 14. magic methods other than __init__() |
| Card.get_card_value() | Mekiyas Seleshi | N/A |
| Card.get_card_effect() | Mekiyas Seleshi | N/A |

## Thank You for Checking Out All or Nothing!!!