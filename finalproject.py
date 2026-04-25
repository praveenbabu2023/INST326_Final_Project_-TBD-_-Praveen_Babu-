class Game:
    def setup_game(self):
        """
        Purpose: setup_game() will create players and loads/shuffles the deck
        Arguments: None
        Returns: None
        Author: TBD
        """
        pass

    def play_game(self):
        """
        Purpose: play_game() will run the full game loop until someone wins
        Arguments: None
        Returns: None
        Author: TBD
        """
        pass

    def take_turn(self, player):
        """
        Purpose: take_turn(player) will control one player’s turn if its a draw or stop
        Arguments: player
        Returns: None
        Author: TBD
        """
        pass

    def apply_card_effect(self, player, card):
        """
        Purpose: apply_card_effect(player, card) applies the effect of a drawn card
        Arguments: player, card
        Returns: None
        Author: TBD
        """
        pass

    def check_winner(self):
        """
        Purpose: check_winner() will check if any player reached 100 points
        Arguments: None
        Returns: Player or None
        Author: TBD
        """
        pass

    def end_round(self):
        """
        Purpose: end_round() will handle round transitions/reset if needed
        Arguments: None
        Returns: None
        Author: TBD
        """
        pass


class Player:
    def add_points(self, amount):
        """
        Purpose: add_points(amount) will add points to the player’s round total
        Arguments: amount
        Returns: None
        Author: TBD
        """
        pass

    def bank_points(self):
        """
        Purpose: bank_points() will adds round points to total score
        Arguments: None
        Returns: None
        Author: TBD
        """
        pass

    def reset_round(self):
        """
        Purpose: reset_round() resets round points to 0 at start of turn
        Arguments: None
        Returns: None
        Author: TBD
        """
        pass

    def lose_round_points(self):
        """
        Purpose: lose_round_points() will clears the points if player busts
        Arguments: None
        Returns: None
        Author: TBD
        """
        pass

    def is_capped(self, limit):
        """
        Purpose: is_capped(limit) checks if round total exceeds 50
        Arguments: limit
        Returns: bool
        Author: TBD
        """
        pass

    def get_score(self):
        """
        Purpose: get_score() will return total score
        Arguments: None
        Returns: int
        Author: TBD
        """
        pass

class Deck:
    def __init__(self):
        """
        Purpose: Creates an empty deck.
        Arguments: None
        Returns: None
        Author: Samantha Koppe
        """
        self.cards = []
        
    def load_cards(self, file):
        """
        Purpose: load_cards(file) will load the card data from external file (Txt Value for cards)
        Arguments: file
        Returns: None
        Author: Samantha Koppe
        """
        suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        
        ranks = (
        ("2", 2), ("3", 3), ("4", 4), ("5", 5),
        ("6", 6), ("7", 7), ("8", 8), ("9", 9),
        ("10", 10), ("Jack", 10), ("Queen", 10),
        ("King", 10), ("Ace", 11)
        )
        
        for suit in suits:
            for rank, value in ranks:
                card = Card(rank, suit, value, "none")
                self.cards.append(card)

    def shuffle(self):
        """
        Purpose: shuffle() shuffles the deck
        Arguments: None
        Returns: None
        Author: Amira Thompson
        """
        #Count how many cards are in the deck
        n = len(self.cards)
        
        #Get Permission for random library before we do this part
        # Step 1: Count how many cards are in the deck
        # Step 2: Rearrange the cards
        # Step 3: Replace the deck with new order

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
        Author: TBD
        """
        self.cards = []
        self.load_cards(None)

class Card:
    def __init__(self, rank, suit, value, effect):
        """
        Purpose: Creates a card with rank, suit, value, and effect.
        Arguments: rank, suit, value, effect
        Returns: None
        Author: Praveen Babu
        """
        
        self.rank = rank
        self.suit = suit
        self.value = value
        self.effect = effect
        
    def get_card_value(self):
        """
        Purpose: get_card_value() will return the card’s point value
        Arguments: None
        Returns: int
        Author: Praveen Babu
        """
        return self.value

    def get_card_effect(self):
        """
        Purpose: get_card_effect() will return the card’s effect
        Arguments: None
        Returns: str
        Author: Praveen Babu
        """
        return self.effect

    def card_display(self):
        """
        Purpose: card_display() will show card details to the player
        Arguments: None
        Returns: str
        Author: Praveen Babu
        """
        return self.rank + " of " + self.suit


class Scoreboard:
    def display_scores(self, players):
        """
        Purpose: display_scores(players) prints all player scores
        Arguments: players
        Returns: None
        Author: TBD
        """
        pass

    def get_leader(self, players):
        """
        Purpose: get_leader(players) will return player with highest score
        Arguments: players
        Returns: Player
        Author: TBD
        """
        pass

    def announce_winner(self, player):
        """
        Purpose: announce_winner(player) will display the winner
        Arguments: player
        Returns: None
        Author: TBD
        """
        pass