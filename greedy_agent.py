import random
from agent import Agent
from data.characters import question_bank, all_possible_characters

class GreedyAgent(Agent):
    def __init__(self):
        super().__init__()
        self.possible_characters = list(all_possible_characters.keys())
        self.total_questions_asked = 0

    def compute_information_gain(self, q_index):
        """
        Computes the expected number of characters remaining if we ask question q_index.
        """
        yes_count = sum(
            1 for char in self.possible_characters if all_possible_characters[char][q_index] == 1
        )
        no_count = len(self.possible_characters) - yes_count

        p_yes = yes_count / len(self.possible_characters)
        p_no = no_count / len(self.possible_characters)
        
        expected_remaining = p_yes * yes_count + p_no * no_count
        return expected_remaining

    def choose_best_question(self):
        """
        Selects the question with the minimum expected number of characters remaining.
        """
        available_questions = [i for i in range(len(self.question_bank)) if i not in self.asked_questions]
        
        if not available_questions:
            return None, "No more questions available."

        # Compute expected remaining characters for each available question
        best_question = min(available_questions, key=self.compute_information_gain)
        question_text = self.question_bank[best_question]
        
        self.asked_questions.add(best_question)
        self.total_questions_asked += 1

        return best_question, question_text

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
        
        # Get the target character's attributes
        target_attributes = all_possible_characters[target_character]
        
        while len(self.possible_characters) > 1 and self.total_questions_asked < 20:
            # Choose the best question
            q_index, question_text = self.choose_best_question()
            if q_index is None:
                print("No more questions available. Game over.")
                break

            print(f"Question {self.total_questions_asked}: {question_text}")

            # Automatically determine the answer based on the target character's attributes
            answer = "yes" if target_attributes[q_index] == 1 else "no"
            print(f"Answer: {answer}")

            # Process the answer to eliminate impossible characters
            self.eliminate_characters(q_index, answer)

        # Check if a single character remains
        if len(self.possible_characters) == 1:
            guessed_character = self.possible_characters[0]
            if guessed_character == target_character:
                self.game_status = 1 
                print(f"The agent successfully identified the character: '{guessed_character}' in {self.total_questions_asked} questions.")
            else:
                self.game_status = -1 
                print(f"The agent guessed '{guessed_character}', but it was incorrect. Game status: Lost.")
        else:
            self.game_status = -1
            print("Could not determine the character with certainty.")
