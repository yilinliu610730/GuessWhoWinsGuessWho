# main.py
from data.characters import all_possible_characters
from random_agent import RandomAgent
# from q_learning_agent import QLearningAgent
from oracle_agent import OracleAgent
from greedy_agent import GreedyAgent

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
    print("Available characters:", ", ".join(all_possible_characters.keys()))

    target_character = input("Please enter the name of the target character for the agent to guess: ")

    while target_character not in all_possible_characters:
        print("Invalid character name. Please choose a valid character from the list.")
        target_character = input("Enter the target character name again: ")

    print(f"\nTarget character for this game is: {target_character}\n")

    # Initialize the appropriate agent based on the selected game mode
    if game_mode == 1:
        agent = RandomAgent()
    elif game_mode == 2:
        # Initialize QLearningAgent if available
        # agent = QLearningAgent()
        return
    elif game_mode == 3:
        agent = OracleAgent()
    elif game_mode == 4:
        agent = GreedyAgent()

    # Start the game
    agent.play_game(target_character)

    # Check the game status
    if agent.game_status == 1:
        print(f"The agent successfully guessed the character '{target_character}' in {agent.total_questions_asked} questions.")
    elif agent.game_status == -1:
        print("The agent failed to guess the character.")
    else:
        print("The game is still ongoing.")

if __name__ == "__main__":
    main()