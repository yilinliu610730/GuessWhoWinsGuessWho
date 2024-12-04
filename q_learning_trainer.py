import random
import numpy as np
from data.characters import all_possible_characters, question_bank

class QLearningTrainer:
    def __init__(self, reward_func, epochs=10000, epsilon=0.5, learning_rate=0.1, discount_factor=0.8):
        self.epochs = epochs
        self.epsilon = epsilon
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.state_space = list(all_possible_characters.keys())
        self.action_space = list(range(len(question_bank)))
        self.q_table = np.zeros((len(self.state_space), len(self.action_space)))
        self.optimal_questions = {}
        self.current_best_reward = {}
        self.reward_function = reward_func
        random.seed(42)
        np.random.seed(42)

    def choose_action(self, state, asked_questions):
        available_actions = [a for a in self.action_space if a not in asked_questions]
        available_actions.sort()

        if random.uniform(0, 1) < self.epsilon:
            # Exploration
            return random.choice(available_actions)
        else:
            # Exploitation
            state_indices = [self.state_space.index(s) for s in state]
            available_q_values = self.q_table[np.array(state_indices)[:, None], np.array(available_actions)]

            max_index_flat = np.argmax(np.ravel(available_q_values))
            best_action = available_actions[np.unravel_index(max_index_flat, available_q_values.shape)[1]]
            return best_action

    def update_q_value(self, state, action, reward, next_state):
        state_index = [self.state_space.index(s) for s in state]
        action_index = action

        next_state_index = [self.state_space.index(s) for s in next_state]

        # Bellman equation update
        max_future_q = np.max(self.q_table[next_state_index])  # Maximum Q-value for next state
        current_q = self.q_table[state_index, action_index]
        
        # Q-value update
        new_q = current_q + self.learning_rate * (reward + self.discount_factor * max_future_q - current_q)
        self.q_table[state_index, action_index] = new_q

    def run_epoch(self, target_character):
        # print(f"Starting epoch to train agent for target character: {target_character}")

        possible_characters = list(all_possible_characters.keys())
        steps_taken = 0
        asked_questions = set()

        while len(possible_characters) > 1 and steps_taken < 20:
            state = tuple(possible_characters)
            sorted_state = tuple(sorted(state))

            # Initialize the current best reward for the state if not already set
            if sorted_state not in self.current_best_reward:
                self.current_best_reward[sorted_state] = -float('inf')

            # Choose the best question (action) to ask
            if steps_taken == 0:
                question_index = random.choice(self.action_space)
            else:
                question_index = self.choose_action(state, asked_questions)
            question_text = question_bank[question_index]

            # Mark this question as asked
            asked_questions.add(question_index)

            # Get the answer based on the target character
            answer = self.determine_answer(target_character, question_text)

            previous_count = len(possible_characters)
            possible_characters = self.eliminate_characters(possible_characters, question_index, answer)
            eliminated_count = previous_count - len(possible_characters)
            is_terminal = len(possible_characters) == 1
            reward = self.reward_function(eliminated_count, previous_count, is_terminal)
            # print(f"eliminated_count: {eliminated_count}, previous_count: {previous_count}, is_terminal: {is_terminal}, reward: {reward}")

            # Update the Q-value
            self.update_q_value(state, question_index, reward, tuple(sorted(possible_characters)))

            # Track the best question for this state based on reward
            if reward > self.current_best_reward[sorted_state]:
                self.current_best_reward[sorted_state] = reward
                self.optimal_questions[sorted_state] = question_bank[question_index]

            steps_taken += 1

        # self.evaluate_result(target_character, possible_characters)

    def determine_answer(self, target_character, question):
        question_index = question_bank.index(question)
        target_attributes = all_possible_characters[target_character]
        return "yes" if target_attributes[question_index] == 1 else "no"

    def eliminate_characters(self, possible_characters, q_index, answer):
        return [
            char_name for char_name in possible_characters
            if all_possible_characters[char_name][q_index] == (1 if answer == "yes" else 0)
        ]

    def evaluate_result(self, target_character, possible_characters):
        if len(possible_characters) == 1:
            guessed_character = possible_characters[0]
            if guessed_character == target_character:
                print(f"Epoch ended: The agent successfully identified the character: '{guessed_character}'!")
            else:
                print(f"Epoch ended: The agent guessed '{guessed_character}', but it was incorrect.")
        else:
            print("Epoch ended: The agent was unable to identify the character.")

    def train(self):
        print(f"Reward Function: {self.reward_function.__name__}")
        self.q_table = np.zeros((len(self.state_space), len(self.action_space)))  # Reset Q-table
        self.current_best_reward = {}  # Reset state tracking
        self.optimal_questions = {}  # Reset optimal questions
        for epoch in range(self.epochs):
            # print(f"\nEpoch {epoch + 1} of {self.epochs}...")
            target_character = random.choice(list(all_possible_characters.keys()))
            self.run_epoch(target_character)

        print(f"\nTraining finished after {self.epochs} epochs.")
        self.save_optimal_question_sequence()

    def save_optimal_question_sequence(self):
        with open(f"data/optimal_question_seq.py", "w") as f:
            f.write("optimal_question_sequence = {\n")
            for state, question in self.optimal_questions.items():
                sorted_state_tuple = tuple(sorted(state))
                f.write(f'    {sorted_state_tuple}: "{question}",\n')
            f.write("}\n")
        print("Optimal question sequence saved to optimal_question_seq.py")

# if __name__ == "__main__":
#     def reward_function(eliminated_count, previous_count, is_terminal=None):
#         if is_terminal:
#             print('terminal')
#         if eliminated_count > 0:
#             reward = (eliminated_count / previous_count) * 2
#         else:
#             reward = -1
#         return reward
#     QLearningTrainer(reward_function).train()
