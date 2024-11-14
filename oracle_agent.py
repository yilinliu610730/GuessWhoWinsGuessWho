from agent import Agent
from data.characters import question_bank, all_possible_characters, oracle_question_sequence

class OracleAgent(Agent):
    def __init__(self):
        super().__init__()
        self.current_question = "Do they have a big mouth?"  # Start with the initial question
        self.steps_taken = 0  # Counter for the number of steps/questions asked

    def ask_question(self):
        """
        Asks the current question in the oracle sequence.
        """
        question = self.current_question
        print(f"Question: {question}")
        return question

    def determine_answer(self, target_character, question):
        """
        Determines the answer ('yes' or 'no') for a given question based on the target character's attributes.
        """
        question_index = self.question_bank.index(question)

        target_attributes = all_possible_characters[target_character]
        return "yes" if target_attributes[question_index] == 1 else "no"

    def eliminate_characters(self, q_index, answer):
        """
        Eliminates characters based on the answer ('yes' or 'no') for the current question.
        """
        previous_count = len(self.possible_characters)
        self.possible_characters = [
            char_name for char_name in self.possible_characters
            if all_possible_characters[char_name][q_index] == (1 if answer == "yes" else 0)
        ]
        eliminated_count = previous_count - len(self.possible_characters)
        print(f"Eliminated {eliminated_count} characters based on answer '{answer}'. Remaining possible characters: {self.possible_characters}")

    def next_question(self, answer):
        """
        Updates the current question based on the answer ('yes' or 'no') using the oracle question sequence.
        """
        if self.current_question in oracle_question_sequence:
            self.current_question = oracle_question_sequence[self.current_question].get(answer)
            return self.current_question

    def play_game(self, target_character):
        """
        Plays the game by asking questions until the sequence is exhausted or the target character is identified.
        """
        print(f"Starting game to guess: {target_character}\n")
        
        while self.current_question:
            self.steps_taken += 1

            question = self.ask_question()
            
            answer = self.determine_answer(target_character, question)
            print(f"Answer: {answer}")

            q_index = self.question_bank.index(question)
            self.eliminate_characters(q_index, answer)  # Eliminate characters based on the answer

            self.next_question(answer)

            if len(self.possible_characters) == 1:
                guessed_character = self.possible_characters[0]
                if guessed_character == target_character:
                    self.game_status = 1  # Game status indicates a win
                    print(f"The agent successfully identified the character: '{guessed_character}' in {self.steps_taken} steps!")
                else:
                    self.game_status = -1  # Game status indicates a loss
                    print(f"The agent guessed '{guessed_character}', but it was incorrect. Game status: Lost.")
                return
            elif not self.current_question:
                self.game_status = -1  # Game status indicates a loss
                print(f"End of question sequence. Unable to identify the character with certainty after {self.steps_taken} steps.")
                break

        print(f"Oracle Agent has finished the question sequence for character '{target_character}'.")