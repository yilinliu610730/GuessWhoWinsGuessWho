from agent import Agent
from data.characters import all_possible_characters, question_bank
from data.optimal_question_seq_new import optimal_question_sequence


class QLearningAgent(Agent):
    def __init__(self):
        self.possible_characters = list(all_possible_characters.keys())
        self.steps_taken = 0
        self.asked_questions = set()
        self.last_answer = None

    def ask_question(self, state):
        """
        Determines the question to ask based on the optimal policy.
        """
        if state in optimal_question_sequence:
            question_text = optimal_question_sequence[state]
            question_index = question_bank.index(question_text)
            print(f"Question: {question_text}")
            return question_index, question_text
        else:
            return None, None  # No valid question for this state

    def determine_answer(self, target_character, question_index):
        """
        Determines the answer ('yes' or 'no') for a given question based on the target character's attributes.
        """
        target_attributes = all_possible_characters[target_character]
        return "yes" if target_attributes[question_index] == 1 else "no"

    def eliminate_characters(self, question_index, answer):
        """
        Eliminates characters based on the answer ('yes' or 'no') for the current question.
        """
        previous_count = len(self.possible_characters)
        eliminated_count = previous_count - len(self.possible_characters)
        self.possible_characters = [
            char_name for char_name in self.possible_characters
            if all_possible_characters[char_name][question_index] == (1 if answer == "yes" else 0)
        ]
        eliminated_count = previous_count - len(self.possible_characters)
        print(f"Eliminated {eliminated_count} characters based on answer '{answer}'. Remaining possible characters: {self.possible_characters}")

    def play_game(self, target_character):
        """
        Plays the game using the loaded optimal question sequence.
        """
        self.possible_characters = list(all_possible_characters.keys())
        self.steps_taken = 0
        self.asked_questions = set()
        self.last_answer = None

        while len(self.possible_characters) > 1 and self.steps_taken < 20:
            self.steps_taken += 1

            # Construct the current state
            state = (len(self.possible_characters), self.last_answer, tuple(sorted(self.asked_questions)))

            # Ask the next question based on the optimal policy
            question_index, question_text = self.ask_question(state)
            if question_index is None:
                print("No more valid questions in the policy.")
                break

            self.asked_questions.add(question_index)

            # Get the answer based on the target character
            self.last_answer = self.determine_answer(target_character, question_index)
            print(f"Answer: {self.last_answer}")

            # Eliminate characters based on the answer
            self.eliminate_characters(question_index, self.last_answer)

        if len(self.possible_characters) == 1:
            guessed_character = self.possible_characters[0]
            if guessed_character == target_character:
                self.game_status = 1
                print(f"The agent successfully identified the character: '{guessed_character}' in {self.steps_taken} steps!")
                return self.steps_taken
            else:
                self.game_status = -1
                print(f"The agent guessed '{guessed_character}', but it was incorrect. Game status: Lost.")
            return
        else:
            self.game_status = -1
            print("Could not determine the character with certainty.")
