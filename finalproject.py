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
    def load_cards(self, file):
        """
        Purpose: load_cards(file) will load the card data from external file (Txt Value for cards)
        Arguments: file
        Returns: None
        Author: TBD
        """
        pass

    def shuffle(self):
        """
        Purpose: shuffle() shuffles the deck
        Arguments: None
        Returns: None
        Author: TBD
        """
        pass

    def draw_card(self):
        """
        Purpose: draw_card() removes and returns the top card
        Arguments: None
        Returns: Card
        Author: TBD
        """
        pass

    def reset_deck(self):
        """
        Purpose: reset_deck() reloads or reshuffles when empty
        Arguments: None
        Returns: None
        Author: TBD
        """
        pass


class Card:
    def get_card_value(self):
        """
        Purpose: get_card_value() will return the card’s point value
        Arguments: None
        Returns: int
        Author: TBD
        """
        pass

    def get_card_effect(self):
        """
        Purpose: get_card_effect() will return the card’s effect
        Arguments: None
        Returns: str
        Author: TBD
        """
        pass

    def card_display(self):
        """
        Purpose: card_display() will show card details to the player
        Arguments: None
        Returns: str
        Author: TBD
        """
        pass


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