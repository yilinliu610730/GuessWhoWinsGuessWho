from data.characters import all_possible_characters
from random_agent import RandomAgent
from oracle_agent import OracleAgent
from greedy_agent import GreedyAgent
from q_learning_agent import QLearningAgent
from q_learning_trainer import QLearningTrainer
import numpy as np


def run_experiments(game_mode, trials_per_character=1000):
    results = {}
    all_characters = list(all_possible_characters.keys())[:24]  # Limit to 24 characters

    # Initialize the agent based on the selected game mode
    if game_mode == 1:
        agent_class = RandomAgent
    elif game_mode == 2:
        agent_class = QLearningAgent
    elif game_mode == 3:
        agent_class = OracleAgent
    elif game_mode == 4:
        agent_class = GreedyAgent
    else:
        raise ValueError("Invalid game mode selected.")

    all_character_questions = 0
    for character in all_characters:
        print(f"Starting experiments for character: {character}")
        success_count = 0
        total_questions = []

        for trial in range(trials_per_character):
            agent = agent_class()  # Initialize a new agent for each trial
            steps_taken = agent.play_game(character)
            print(f"steps_taken: {steps_taken}")

            # Track success and number of questions
            if agent.game_status == 1:
                success_count += 1
            total_questions.append(steps_taken)
            print(f"total_questions: {total_questions}")

        # Store results for the character
        print(f"Starting experiments for character: {character}")
        avg_questions = np.mean(total_questions)
        results[character] = {
            "success_rate": success_count / trials_per_character,
            "avg_questions": avg_questions,
        }

        print(f"Results for {character}: Success Rate = {results[character]['success_rate']:.2f}, "
              f"Average Questions = {results[character]['avg_questions']:.2f}\n")

        all_character_questions += np.sum(total_questions)
    
    return results, all_character_questions


def main():
    # Prompt the user to select a game mode
    print("Select game mode:")
    print("1: Random Agent")
    print("2: Q-Learning Agent")
    print("3: Oracle Agent")
    print("4: Greedy Agent")
    game_mode = input("Enter the number corresponding to your chosen game mode: ")

    while game_mode not in {"1", "2", "3", "4"}:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
        game_mode = input("Enter the number corresponding to your chosen game mode: ")
    
    game_mode = int(game_mode)
    print(f"Game mode selected: {game_mode}\n")

    # Run experiments
    results, total_questions = run_experiments(game_mode, trials_per_character=1000)

    # Save results to a file
    with open("experiment_results/"+str(game_mode)+".txt", "w") as file:
        for character, stats in results.items():
            file.write(f"{character}: Success Rate = {stats['success_rate']:.2f}, "
                       f"Average Questions = {stats['avg_questions']:.2f}\n")
        file.write(f"Average questions asked = {total_questions/24000}\n")

    print("Experiment completed. Results saved to 'experiment_results.txt'.")


if __name__ == "__main__":
    main()
