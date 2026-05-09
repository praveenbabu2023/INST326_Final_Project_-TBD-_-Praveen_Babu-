import random

class Game:
    """
    Purpose: Controls the main game setup, game loop, player turns, and win checking.
    Author: Praveen Babu
    """
    def __init__(self):
        """
        Purpose: Creates the game.
        Arguments: None
        Returns: None
        Author: Praveen Babu
        """
        self.players = []
        self.deck = Deck()
        self.scoreboard = Scoreboard()
    
    def setup_game(self):
        """
        Purpose: setup_game() will create players and loads/shuffles the deck
        Arguments: None
        Returns: None
        Author: Praveen Babu
        """
        print("Welcome to All or Nothing!")

        player_count = int(input("How many players? "))

        for number in range(player_count):
            name = input("Enter player name: ")
            player = Player(name)
            self.players.append(player)

        self.deck.load_cards("cards.txt")
        self.deck.shuffle()

    def play_game(self):
        """
        Purpose: play_game() will run the full game loop until someone wins
        Arguments: None
        Returns: None
        Author: Praveen Babu
        """
        winner = None

        while winner == None:
            for player in self.players:
                self.take_turn(player)
                winner = self.check_winner()

                if winner != None:
                    self.scoreboard.announce_winner(winner)
                    return

    def take_turn(self, player):
        """
        Purpose: take_turn(player) will control one player’s turn if its a draw or stop
        Arguments: player
        Returns: None
        Author: Praveen Babu
        """
        player.reset_round()
        turn_over = False

        print()
        print(player.name + "'s turn")
        print("Total score:", player.get_score())
        print("Turn score:", player.round_score)
        print("Type Draw Card to draw a card.")
        print("Type End to end your turn.")

        while turn_over == False:
            choice = input("Choice: ").strip().lower()

            if choice == "draw card":
                card = self.deck.draw_card()

                if card == None:
                    self.deck.reset_deck()
                    self.deck.shuffle()
                    card = self.deck.draw_card()

                self.apply_card_effect(player, card)
                player.add_drawn_card(card)
                
                if self.check_same_suit_bonus(player) and player.same_suit_bonus_used == False:
                    player.add_points(15)
                    player.same_suit_bonus_used = True
                    print("Same suit bonus! You gained 15 points.")
            
            
                print("You drew:", card)
                print("Card value:", card.get_card_value())
                print("Effect:", card.get_card_effect())
                print("Turn score:", player.round_score)
                print("Total score:", player.get_score())

                if player.is_capped():
                    print("Bust! You went over 50.")
                    print("You lost all points from this turn.")
                    player.lose_round_points()
                    turn_over = True

            elif choice == "end":
                saved_points = player.round_score
                player.bank_points()

                print(player.name + " ended their turn.")
                print(saved_points, "points were saved.")
                print(player.name + "'s total score is now", player.get_score())

                turn_over = True

            else:
                print("Please type Draw Card or End.")

    def apply_card_effect(self, player, card):
        """
        Purpose: apply_card_effect(player, card) applies the effect of a drawn card
        Arguments: player, card
        Returns: None
        Author: Praveen Babu
        """
        if card.get_card_effect() == "double_plus_seven":
            player.round_score = player.round_score * 2 + 7
        else:
            player.add_points(card.get_card_value())
            
    def check_same_suit_bonus(self, player):
        """
        Purpose: Checks if a player drew more than 3 cards of the same suit in one turn.
        Arguments: player
        Returns: bool
        Author: Praveen Babu
        """
        suits = []

        for card in player.drawn_cards:
            suits.append(card.suit)

        for suit in suits:
            count = 0

            for card_suit in suits:
                if card_suit == suit:
                    count = count + 1

            if count > 3:
                return True

        return False

    def check_winner(self):
        """
        Purpose: check_winner() will check if any player reached 100 points
        Arguments: None
        Returns: Player or None
        Author: Praveen Babu
        """
        for player in self.players:
            if player.get_score() >= 100:
                return player

        return None

    def end_round(self):
        """
        Purpose: end_round() will handle round transitions/reset if needed
        Arguments: None
        Returns: None
        Author: Praveen Babu
        """
        print()
        print("Round over.")
        self.scoreboard.display_scores(self.players)


class Player:
    """
    Purpose: Stores each player's name, total score, round score, drawn cards, and bonus status.
    Author: Samantha Koppe
    """
    
    def __init__(self, name):
        """
        Purpose: Creates a player with a name, total score, round score, drawn cards list, and bonus tracker.
        Arguments: name
        Returns: None
        Author: Samantha Koppe
        """
        self.name = name
        self.total_score = 0
        self.round_score = 0
        self.drawn_cards = []
        self.same_suit_bonus_used = False
        
    def add_points(self, amount):
        """
        Purpose: add_points(amount) will add points to the player’s round total
        Arguments: amount
        Returns: None
        Author: Samantha Koppe
        """
        self.round_score = self.round_score + amount
        
    def add_drawn_card(self, card):
        """
        Purpose: Adds a drawn card to the player's drawn card list.
        Arguments: card
        Returns: None
        Author: Samantha Koppe
        """
        self.drawn_cards.append(card)

    def bank_points(self):
        """
        Purpose: bank_points() will adds round points to total score
        Arguments: None
        Returns: None
        Author: Samantha Koppe
        """
        self.total_score = self.total_score + self.round_score
        self.round_score = 0

    def reset_round(self):
        """
        Purpose: Resets the player's round score, drawn cards list, and same-suit bonus tracker at the start of a turn.
        Arguments: None
        Returns: None
        Author: Samantha Koppe
        """
        self.round_score = 0
        self.drawn_cards = []
        self.same_suit_bonus_used = False

    def lose_round_points(self):
        """
        Purpose: lose_round_points() will clears the points if player busts
        Arguments: None
        Returns: None
        Author: Samantha Koppe
        """
        self.round_score = 0

    def is_capped(self, limit=50):
        """
        Purpose: is_capped(limit) checks if round total exceeds 50
        Arguments: limit
        Returns: bool
        Author: Samantha Koppe
        """
        if self.round_score > limit:
            return True
        else:
            return False

    def get_score(self):
        """
        Purpose: get_score() will return total score
        Arguments: None
        Returns: int
        Author: Samantha Koppe
        """
        return self.total_score

class Deck:
    """
    Purpose: Handles loading, shuffling, drawing, and resetting cards.
    Author: Amira Thompson
    """
    def __init__(self):
        """
        Purpose: Creates an empty deck.
        Arguments: None
        Returns: None
        Author: Amira Thompson
        """
        self.cards = []
    
    def load_cards(self, file):
        """
        Purpose: load_cards(file) will load the card data from external file (Txt Value for cards)
        Arguments: file
        Returns: None
        Author: Amira Thompson
        """
        with open(file, "r") as card_file:
            for line in card_file:
                rank, suit, value, effect = line.strip().split(",")

                value = int(value)
                card = Card(rank, suit, value, effect)
                self.cards.append(card)

    def shuffle(self):
        """
        Purpose: shuffle() shuffles the deck
        Arguments: None
        Returns: None
        Author: Praveen Babu
        """
        
        random.shuffle(self.cards)

    def draw_card(self):
        """
        Purpose: draw_card() removes and returns the top card
        Arguments: None
        Returns: Card
        Author: Amira Thompson
        """
        
        if self.cards:
            return self.cards.pop(0)
        return None

    def reset_deck(self):
        """
        Purpose: reset_deck() reloads or reshuffles when empty
        Arguments: None
        Returns: None
        Author: Amira Thompson
        """
        self.cards = []
        self.load_cards("cards.txt")
        self.shuffle()

class Card:
    """
    Purpose: Stores one card's rank, suit, value, and effect.
    Author: Mekiyas Seleshi
    """
    def __init__(self, rank, suit, value, effect):
        """
        Purpose: Creates a card with rank, suit, value, and effect.
        Arguments: rank, suit, value, effect
        Returns: None
        Author: Mekiyas Seleshi
        """
        
        self.rank = rank
        self.suit = suit
        self.value = value
        self.effect = effect
        
    def __str__(self):
        """
        Purpose: Returns the card as a readable string.
        Arguments: None
        Returns: str
        Author: Mekiyas Seleshi
        """
        return self.rank + " of " + self.suit
        
    def get_card_value(self):
        """
        Purpose: get_card_value() will return the card’s point value
        Arguments: None
        Returns: int
        Author: Mekiyas Seleshi
        """
        return self.value

    def get_card_effect(self):
        """
        Purpose: get_card_effect() will return the card’s effect
        Arguments: None
        Returns: str
        Author: Mekiyas Seleshi
        """
        return self.effect

    def card_display(self):
        """
        Purpose: card_display() will show card details to the player
        Arguments: None
        Returns: str
        Author: Mekiyas Seleshi
        """
        return self.rank + " of " + self.suit


class Scoreboard:
    """
    Purpose: Displays scores, finds the leader, and announces the winner.
    Author: Praveen Babu
    """
    def display_scores(self, players):
        """
        Purpose: display_scores(players) prints all player scores
        Arguments: players
        Returns: None
        Author: Praveen Babu
        """
        print("Current Scores:")

        for player in players:
            print(f"{player.name}: {player.get_score()} points")

    def get_leader(self, players):
        """
        Purpose: get_leader(players) will return player with highest score
        Arguments: players
        Returns: Player
        Author: Praveen Babu
        """
        leader = max(players, key=Player.get_score)
        return leader

    def announce_winner(self, player):
        """
        Purpose: announce_winner(player) will display the winner
        Arguments: player
        Returns: None
        Author: Praveen Babu
        """
        print()
        print("Game over!")
        print(f"{player.name} wins All or Nothing with {player.get_score()} points!")
     
if __name__ == "__main__":
    game = Game()
    game.setup_game()
    game.play_game()    