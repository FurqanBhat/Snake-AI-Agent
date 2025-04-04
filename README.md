# Snake Game AI – Deep Q-Learning with PyTorch

## Description

This project implements an AI agent that learns to play the classic Snake game using Deep Q-Learning (DQL). The agent is built with PyGame for the game environment and visualization, and PyTorch for creating and training the neural network-based Q-learning model. Through interaction with the game environment, the AI learns optimal movement strategies to maximize its score.

This project is ideal for anyone looking to understand the practical application of Deep Reinforcement Learning concepts, specifically DQN, in game AI development.

## Features

-   **Game Environment:** Snake game built from scratch using Python and PyGame.
-   **AI Agent:** Deep Q-Network (DQN) agent implementation.
-   **Learning Algorithm:** Q-learning with experience replay and an epsilon-greedy strategy for balancing exploration and exploitation.
-   **State Representation:** Custom state space designed to capture relevant information about the snake's surroundings.
-   **Reward System:** Engineered rewards to encourage seeking food and heavily penalize collisions.
-   **Training:** Real-time training process with performance monitoring capabilities.
-   **Technology:** Core implementation uses Python, PyTorch, and PyGame.

## Tech Stack

-   **Language:** Python
-   **Libraries:**
    -   PyTorch (for Neural Network and DQL)
    -   PyGame (for Game Environment and Visualization)
    -   NumPy (for numerical operations)

## Project Structure

* `snake_game.py`: Implementation of the core Snake game environment using PyGame.
* `model.py`: Contains the PyTorch neural network definition (`Linear_QNet`) and the `QTrainer` class responsible for the Q-learning update steps.
* `agent.py`: Defines the `Agent` class, encapsulating the DQN logic, including state definition, action selection (epsilon-greedy), memory (experience replay), and                    interaction with the model and trainer.
* `train.py`: Orchestrates the entire process – initializes the game, agent, model, and runs the main training loop, handling episode management and progress tracking.

## Inspiration

This project draws inspiration from Deep Q-Network (DQN) concepts commonly found in reinforcement learning tutorials and resources. It serves as a practical example for anyone interested in understanding how AI agents can learn to master game environments through trial and error.
