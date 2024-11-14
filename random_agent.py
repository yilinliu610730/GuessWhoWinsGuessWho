import random
from agent import Agent
from data.characters import question_bank, all_possible_characters

class RandomAgent(Agent):
    def __init__(self):
        super().__init__()
        self.possible_characters = list(all_possible_characters.keys())
        self.total_questions_asked = 0

    def ask_random_question(self):
        """
        Randomly selects an unused question from the question bank and asks it.
        """
        available_questions = [i for i in range(len(self.question_bank)) if i not in self.asked_questions]
        
        if not available_questions:
            return None, "No more questions available."  # Edge case handling

        q_index = random.choice(available_questions)
        self.asked_questions.add(q_index)
        question_text = self.question_bank[q_index]
        
        self.total_questions_asked += 1
        return q_index, question_text

    def eliminate_characters(self, q_index, answer):
        """
        Eliminates characters from possible choices based on the answer to the question.
        """
        new_possible_characters = [
            char_name for char_name in self.possible_characters
            if all_possible_characters[char_name][q_index] == (1 if answer == "yes" else 0)
        ]
        self.possible_characters = new_possible_characters
        print(f"Characters remaining: {self.possible_characters}")

    def play_game(self, target_character):
        """
        Simulates the game by repeatedly asking questions until the target character is identified.
        """
        print(f"Starting game to guess: {target_character}")
        
        target_attributes = all_possible_characters[target_character]
        
        while len(self.possible_characters) > 1 and self.total_questions_asked < 20:
            q_index, question_text = self.ask_random_question()
            if q_index is None:
                print("No more questions available. Game over.")
                break

            print(f"Question {self.total_questions_asked}: {question_text}")

            answer = "yes" if target_attributes[q_index] == 1 else "no"
            print(f"Answer: {answer}")

            self.eliminate_characters(q_index, answer)

        if len(self.possible_characters) == 1:
            guessed_character = self.possible_characters[0]
            if guessed_character == target_character:
                self.game_status = 1  # Success
                print(f"The agent successfully identified the character: '{guessed_character}' in {self.total_questions_asked} questions.")
            else:
                self.game_status = -1  # Incorrect guess
                print(f"The agent guessed '{guessed_character}', but it was incorrect. Game status: Lost.")
        else:
            self.game_status = -1  # Game over without a definite guess
            print("Could not determine the character with certainty.")