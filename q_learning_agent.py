from agent import Agent
from data.characters import all_possible_characters
from data.optimal_question_seq import optimal_question_sequence

class QLearningAgent(Agent):
    def __init__(self):
        super().__init__()
        self.possible_characters = list(all_possible_characters.keys())
        self.steps_taken = 0
        self.game_status = 0
        self.current_question = None
        self.state = tuple(sorted(self.possible_characters))
        self.asked_questions = set()  # Track questions that have been asked

    def ask_question(self):
        """
        Asks the current question based on the optimal question sequence for the current state.
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
        return eliminated_count

    def find_new_question(self, sorted_state):
        """
        Finds a new question dynamically that has not been asked yet and could help eliminate characters.
        """
        # Try to find a question from the most similar state
        most_similar_state = self.find_most_similar_state(sorted_state)
        if most_similar_state:
            question = optimal_question_sequence.get(most_similar_state)
            if question and question not in self.asked_questions:
                return question

        # Fallback: Choose an unexplored question from the question bank
        for question in self.question_bank:
            if question not in self.asked_questions:
                return question

        return None  # If no valid questions remain

    def find_most_similar_state(self, current_state):
        """
        Finds the most similar state to the current state based on the intersection of possible characters.
        """
        max_overlap = -1
        most_similar_state = None

        # Loop through all possible states to find the most similar one
        for state in optimal_question_sequence.keys():
            overlap = len(set(current_state).intersection(set(state)))

            # Update the most similar state if this one has more overlap
            if overlap > max_overlap:
                max_overlap = overlap
                most_similar_state = state

        return most_similar_state

    def next_question(self, sorted_state, eliminated_count):
        """
        Updates the current question based on the remaining characters and optimal question sequence.
        """
        if eliminated_count == 0:
            # If no characters were eliminated, dynamically find a new question
            new_question = self.find_new_question(sorted_state)
            if new_question:
                self.current_question = new_question
                return

        # Use the optimal sequence for the current sorted state
        if sorted_state in optimal_question_sequence:
            self.current_question = optimal_question_sequence[sorted_state]

    def play_game(self, target_character):
        """
        Plays the game by asking questions until the sequence is exhausted or the target character is identified.
        """
        print(f"Starting game to guess: {target_character}\n")

        if self.current_question is None:
            sorted_state = tuple(sorted(self.state))
            if sorted_state in optimal_question_sequence:
                self.current_question = optimal_question_sequence[sorted_state]

        while len(self.possible_characters) > 1 and self.steps_taken < 20:
            self.steps_taken += 1

            question = self.ask_question()
            self.asked_questions.add(question)  # Mark the question as asked

            answer = self.determine_answer(target_character, question)
            print(f"Answer: {answer}")

            q_index = self.question_bank.index(question)
            eliminated_count = self.eliminate_characters(q_index, answer)

            # Update the current question based on whether any characters were eliminated
            sorted_state = tuple(sorted(self.possible_characters))
            self.next_question(sorted_state, eliminated_count)

        if len(self.possible_characters) == 1:
            guessed_character = self.possible_characters[0]
            if guessed_character == target_character:
                self.game_status = 1
                print(f"The agent successfully identified the character: '{guessed_character}' in {self.steps_taken} steps!")
            else:
                self.game_status = -1
                print(f"The agent guessed '{guessed_character}', but it was incorrect. Game status: Lost.")
            return
        else:
            self.game_status = -1
            print("Could not determine the character with certainty.")
