class Game:
    def setup_game(self):
        pass

    def play_game(self):
        pass

    def take_turn(self, player):
        pass

    def apply_card_effect(self, player, card):
        pass

    def check_winner(self):
        pass

    def end_round(self):
        pass


class Player:
    def add_points(self, amount):
        pass

    def bank_points(self):
        pass

    def reset_round(self):
        pass

    def lose_round_points(self):
        pass

    def is_capped(self, limit):
        pass

    def get_score(self):
        pass


class Deck:
    def load_cards(self, file):
        pass

    def shuffle(self):
        pass

    def draw_card(self):
        pass

    def reset_deck(self):
        pass


class Card:
    def get_card_value(self):
        pass

    def get_card_effect(self):
        pass

    def card_display(self):
        pass


class Scoreboard:
    def display_scores(self, players):
        pass

    def get_leader(self, players):
        pass

    def announce_winner(self, player):
        pass