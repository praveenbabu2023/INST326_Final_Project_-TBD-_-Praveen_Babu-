import random

class Game:
    def __init__(self):
        """
        Purpose: Creates the game.
        Arguments: None
        Returns: None
        Author: TBD
        """
        self.players = []
        self.deck = Deck()
        self.scoreboard = Scoreboard()
    
    def setup_game(self):
        """
        Purpose: setup_game() will create players and loads/shuffles the deck
        Arguments: None
        Returns: None
        Author: TBD
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
        Author: TBD
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
        Author: TBD
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
            choice = input("Choice: ")

            if choice == "Draw Card":
                card = self.deck.draw_card()

                if card == None:
                    self.deck.reset_deck()
                    self.deck.shuffle()
                    card = self.deck.draw_card()

                self.apply_card_effect(player, card)

                print("You drew:", card.card_display())
                print("Card value:", card.get_card_value())
                print("Effect:", card.get_card_effect())
                print("Turn score:", player.round_score)
                print("Total score:", player.get_score())

                if player.is_capped(50):
                    print("Bust! You went over 50.")
                    print("You lost all points from this turn.")
                    player.lose_round_points()
                    turn_over = True

            elif choice == "End":
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
        Author: TBD
        """
        if card.get_card_effect() == "double_plus_seven":
            player.round_score = player.round_score * 2 + 7
        else:
            player.add_points(card.get_card_value())

    def check_winner(self):
        """
        Purpose: check_winner() will check if any player reached 100 points
        Arguments: None
        Returns: Player or None
        Author: TBD
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
        Author: TBD
        """
        print()
        print("Round over.")
        self.scoreboard.display_scores(self.players)


class Player:
    def __init__(self, name):
        """
        Purpose: Creates a player with a name, total score, and round score.
        Arguments: name
        Returns: None
        Author: TBD
        """
        self.name = name
        self.total_score = 0
        self.round_score = 0
        
    def add_points(self, amount):
        """
        Purpose: add_points(amount) will add points to the player’s round total
        Arguments: amount
        Returns: None
        Author: TBD
        """
        self.round_score = self.round_score + amount

    def bank_points(self):
        """
        Purpose: bank_points() will adds round points to total score
        Arguments: None
        Returns: None
        Author: TBD
        """
        self.total_score = self.total_score + self.round_score
        self.round_score = 0

    def reset_round(self):
        """
        Purpose: reset_round() resets round points to 0 at start of turn
        Arguments: None
        Returns: None
        Author: TBD
        """
        self.round_score = 0

    def lose_round_points(self):
        """
        Purpose: lose_round_points() will clears the points if player busts
        Arguments: None
        Returns: None
        Author: TBD
        """
        self.round_score = 0

    def is_capped(self, limit):
        """
        Purpose: is_capped(limit) checks if round total exceeds 50
        Arguments: limit
        Returns: bool
        Author: TBD
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
        Author: TBD
        """
        return self.total_score

class Deck:
    def __init__(self):
        """
        Purpose: Creates an empty deck.
        Arguments: None
        Returns: None
        Author: Samantha Koppe
        """
        self.cards = []
        self.used_cards = []
        
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
     
if __name__ == "__main__":
    game = Game()
    game.setup_game()
    game.play_game()    