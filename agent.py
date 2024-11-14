import random
from data.characters import all_possible_characters, question_bank

class Agent:
    def __init__(self, char_name=None):
        """
        Initializes the agent with a given character or assigns one randomly.
        """
        self.given_char_name = self.assign_char(char_name)
        self.character_attributes = all_possible_characters.get(self.given_char_name, [])
        self.question_bank = question_bank
        self.asked_questions = set()
        self.possible_characters = list(all_possible_characters.keys())
        self.total_questions_asked = 0
        self.game_status = 0  # 0: ongoing, 1: win, -1: lost

    def assign_char(self, char_name=None):
        """
        Assigns a character to the agent, either the one provided or chosen randomly.
        """
        if char_name:
            self.given_char_name = char_name
        else:
            self.given_char_name = random.choice(list(all_possible_characters.keys()))
            print(f"Assigned character: {self.given_char_name}")

        return self.given_char_name

    def reset(self):
        """
        Resets the agent's state for a new game.
        """
        self.asked_questions.clear()
        self.possible_characters = list(all_possible_characters.keys())
        self.total_questions_asked = 0
        self.game_status = 0
        self.assign_char()
        print("Agent has been reset for a new game.")

    def ask_question(self):
        """
        Placeholder method to ask a question. Should be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses should implement this method to ask a question.")

    def eliminate_characters(self, q_index, answer):
        """
        Placeholder for eliminating characters. Should be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses should implement this method for the full game loop.")

    def play_game(self, target_character):
        """
        Placeholder for playing a complete game. The full game loop should be implemented in subclasses.
        """
        raise NotImplementedError("Subclasses should implement this method for the full game loop.")