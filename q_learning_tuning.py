import random
import numpy as np
from data.characters import all_possible_characters, question_bank
from q_learning_trainer import QLearningTrainer
from q_learning_agent import QLearningAgent
import matplotlib.pyplot as plt

discount_factors = np.arange(0.5, 1.01, 0.1)
# learning_rates = np.arange(0.01, 0.11, 0.01)
learning_rates = [0.01, 0.05, 0.1, 0.5, 1]

def reward_func1(eliminated_count, previous_count, is_terminal=None):
    if eliminated_count > 0:
        reward = (eliminated_count / previous_count) * 2
    else:
        reward = -1
    return reward

def reward_func2(eliminated_count, previous_count, is_terminal=None):
    if eliminated_count > 0:
        reward = eliminated_count * 2
    else:
        reward = -1
    return reward

def reward_func3(eliminated_count, previous_count, is_terminal=None):
    if is_terminal:
        return 100
    if eliminated_count > 0:
        return (eliminated_count / previous_count) * 2
    return -1

def reward_func4(eliminated_count, previous_count, is_terminal=None):
    if is_terminal:
        return 100
    if eliminated_count > 0:
        return eliminated_count * 2
    return -1

reward_functions = [reward_func1, reward_func2, reward_func3, reward_func4]

# reward_results = {'reward_func1': 6.583, 'reward_func2': 6.917, 'reward_func3':6.125, 'reward_func4':6.917}
# characters = list(all_possible_characters.keys())
# for func in reward_functions:
#     # QLearningTrainer(func).train()
#     trainer = QLearningTrainer(func)
#     trainer.train()
#     num_questions = 0
#     for j in range(1000):
#         for i in range(24):
#             target_character = characters[i]
#             agent = QLearningAgent(optimal_question_sequence=trainer.optimal_questions)
#             total_questions_asked = agent.play_game(target_character)
#             num_questions += total_questions_asked
    
#     reward_results[str(func.__name__)] = num_questions / 24000

# print(f"Reward Results: {reward_results}")
# keys = list(reward_results.keys())
# values = list(reward_results.values())

# # Define custom labels for the bars
# labels = ["Reward1", "Reward2", "Reward3", "Reward4"]

# plt.figure(figsize=(12, 8))
# bars = plt.bar(labels, values,  color='skyblue')  # Use custom labels for the bars
# for bar in bars:
#     height = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width() / 2, height + 0.1, f'{round(height, 2)}', 
#              ha='center', va='bottom', fontsize=10)
# plt.xlabel("Reward Function", fontsize=16)
# plt.ylabel("Averaged Question Asked", fontsize=16)
# plt.title("Effect of Rewards on Questions Asked", fontsize=20)
# plt.tight_layout()
# plt.savefig('reward_function.png')


# step 2: learning rate
reward_function = reward_functions[0]

characters = list(all_possible_characters.keys())
lr_results = {}
for val in learning_rates:
    num_questions = 0
    trainer = QLearningTrainer(reward_function, learning_rate=val)
    trainer.train()
    for i in range(24):
        target_character = characters[i]
        agent = QLearningAgent(optimal_question_sequence=trainer.optimal_questions)
        total_questions_asked = agent.play_game(target_character)
        num_questions += total_questions_asked
    
    lr_results[str(val)] = num_questions / 24
print(lr_results)
# lr_keys = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]
lr_keys = [0.01, 0.05, 0.1, 0.5, 1]
lr_values = list(lr_results.values())
plt.figure(figsize=(12, 8))
bars = plt.bar([str(key) for key in lr_keys], lr_values, color='skyblue')

# Adding text labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 0.1, f'{round(height, 2)}', 
             ha='center', va='bottom', fontsize=10)

# Adding labels and title
plt.xlabel("Learning Rate", fontsize=14)
plt.ylabel("Averaged Questions Asked", fontsize=14)
plt.title("Effect of Learning Rates on Questions Asked", fontsize=16)
plt.tight_layout()
plt.savefig('lr.png')


# Step 3: discount factor
# func = reward_functions[0]
# lr = 0.04
# characters = list(all_possible_characters.keys())
# df_results = {}
# for val in discount_factors:
#     num_questions = 0
#     trainer = QLearningTrainer(func, learning_rate=lr, discount_factor=val)
#     trainer.train()
#     for i in range(24):
#         target_character = characters[i]
#         agent = QLearningAgent(optimal_question_sequence=trainer.optimal_questions)
#         total_questions_asked = agent.play_game(target_character)
#         num_questions += total_questions_asked
    
#     df_results[str(val)] = num_questions / 24
# print(df_results)
# df_keys = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
# df_values = list(df_results.values())
# plt.figure(figsize=(12, 8))
# bars = plt.bar([str(key) for key in df_keys], df_values, color = 'skyblue')
# for bar in bars:
#     height = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width() / 2, height + 0.1, f'{round(height, 2)}', 
#              ha='center', va='bottom', fontsize=10)
# plt.xlabel("Discount Factor")
# plt.ylabel("Averaged Question Asked")
# plt.title("Effect of Discount Factors on Questions Asked")
# plt.tight_layout()
# plt.savefig('Discount_factor.png')


