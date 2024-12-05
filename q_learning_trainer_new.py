import random
import numpy as np
from data.characters import all_possible_characters, question_bank

class QLearningTrainer:
    def __init__(self, reward_func, epochs=20000, epsilon=0.3, learning_rate=0.5, discount_factor=0.6):
        self.epochs = epochs
        self.epsilon = epsilon
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.action_space = list(range(len(question_bank)))
        self.q_table = {}  # Dynamic Q-table for state-action pairs
        self.reward_function = reward_func
        random.seed(42)

    def choose_action(self, state, asked_questions):
        """
        Selects an action (question) based on epsilon-greedy policy.
        """
        available_actions = [a for a in self.action_space if a not in asked_questions]

        if random.uniform(0, 1) < self.epsilon:
            # Exploration
            return random.choice(available_actions)
        else:
            # Exploitation
            q_values = [self.q_table.get((state, action), 0) for action in available_actions]
            max_q_index = np.argmax(q_values)
            return available_actions[max_q_index]

    def update_q_value(self, state, action, reward, next_state):
        """
        Updates the Q-value using the Bellman equation.
        """
        current_q = self.q_table.get((state, action), 0)
        max_future_q = max([self.q_table.get((next_state, a), 0) for a in self.action_space], default=0)
        new_q = current_q + self.learning_rate * (reward + self.discount_factor * max_future_q - current_q)
        self.q_table[(state, action)] = new_q

    def determine_answer(self, target_character, question):
        """
        Determines the answer ('yes' or 'no') for a given question based on the target character's attributes.
        """
        question_index = question_bank.index(question)
        target_attributes = all_possible_characters[target_character]
        return "yes" if target_attributes[question_index] == 1 else "no"

    def eliminate_characters(self, possible_characters, q_index, answer):
        """
        Eliminates characters based on the answer ('yes' or 'no') for the current question.
        """
        return [
            char_name for char_name in possible_characters
            if all_possible_characters[char_name][q_index] == (1 if answer == "yes" else 0)
        ]

    def run_epoch(self, target_character):
        """
        Runs a single training epoch for the target character.
        """
        possible_characters = list(all_possible_characters.keys())
        steps_taken = 0
        asked_questions = set()
        last_answer = None

        while len(possible_characters) > 1 and steps_taken < 20:
            remaining_count = len(possible_characters)
            state = (remaining_count, last_answer, tuple(sorted(asked_questions)))

            # Choose the best question (action) to ask
            question_index = self.choose_action(state, asked_questions)
            question_text = question_bank[question_index]

            # Mark this question as asked
            asked_questions.add(question_index)

            # Get the answer based on the target character
            answer = self.determine_answer(target_character, question_text)
            last_answer = answer

            # Eliminate characters based on the answer
            previous_count = len(possible_characters)
            possible_characters = self.eliminate_characters(possible_characters, question_index, answer)
            eliminated_count = previous_count - len(possible_characters)

            # Calculate reward
            is_terminal = len(possible_characters) == 1
            reward = self.reward_function(eliminated_count, previous_count, is_terminal)

            # Update Q-value
            next_state = (len(possible_characters), last_answer, tuple(sorted(asked_questions)))
            self.update_q_value(state, question_index, reward, next_state)

            steps_taken += 1

    def train(self):
        """
        Trains the Q-learning agent over multiple epochs.
        """
        for epoch in range(self.epochs):
            target_character = random.choice(list(all_possible_characters.keys()))
            self.run_epoch(target_character)
        print(f"Training finished after {self.epochs} epochs.")
        optimal_policy  = self.save_optimal_question_sequence()
        return optimal_policy

    def save_optimal_question_sequence(self):
        optimal_question_sequence = {}

        # Extract optimal question for each state from Q-table
        for (state, action), q_value in self.q_table.items():
            if state not in optimal_question_sequence:
                optimal_question_sequence[state] = action
            else:
                current_best_action = optimal_question_sequence[state]
                if self.q_table[(state, current_best_action)] < q_value:
                    optimal_question_sequence[state] = action
        with open(f"data/optimal_question_seq_new.py", "w") as f:
            f.write("optimal_question_sequence = {\n")
            for state, action in optimal_question_sequence.items():
                question_text = question_bank[action]
                optimal_question_sequence[state] = question_bank[action]
                f.write(f'    {tuple(state)}: "{question_text}",\n')
            f.write("}\n")
        print("Optimal question sequence saved to optimal_question_seq.py")
        return optimal_question_sequence

# Define a reward function
def reward_func1(eliminated_count, previous_count, is_terminal=None):
    if eliminated_count > 0:
        reward = (eliminated_count / previous_count) * 2
    else:
        reward = -1
    return reward


if __name__ == "__main__":
    QLearningTrainer(reward_func1).train()
