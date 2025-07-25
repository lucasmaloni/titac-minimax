# Minimax Algorithm applied to the Tic Tac Toe

## About the project

As part of my data structures and algorithms seminary, i'm developing a simple tic tac toe with the use of the Minimax algorithm as the second player. Not only that, the intention is to visualize and understand the decision making process by the AI. To do this, i'm using matplotlib, the python library that allows graphics ploting and interaction.

The visualization part of the project intends to ease the compreehension over binary trees and the decision making of AI, making it intuitive and acessible, even for non CompSci people.

## Current progress:

- ~~Tic tac toe working for 2 human players~~
- Tic tac toe working, it's possible to play against the AI, with the minimax algorithm determining the decisions
- After the AI makes its move, the decision tree is plotted to reflect and visualize its current state in the game ~~(the first plotted tree is extremely slow to render, so i will change the moment we start visualizing it, to only begin plotting it after the 3rd or 4th round)~~
- The decision tree graphic plotting is happening from the 5th round, i chose this due to performance and the graphic being actualy compreensible from this point in the game forward - currently, the plotted tree show the moves and scores used to calculate the best play

## Technologies used:

- Python
- Matplotlib
- Networkx
- Pydot
- Graphviz

## The Result: A Glimpse into the Machine's Mind
The most rewarding moment of the project was seeing the AI's "mind" in action. The GIF below shows the decision tree that the Minimax algorithm builds to find the perfect move.

![Decision Tree GIF](https://github.com/lucasmaloni/titac-minimax/blob/main/gif%20plot.gif)

To make it easier to understand, the visualization in the GIF focuses on the tree's structure and complexity. However, the project displays the scores and moves on each node.

The real challenge begins now: can you beat the machine?

Clone the project and play against the AI! See in real-time how the tree's complexity decreases with each round and how the algorithm always finds the right answer to your moves.

## Instalation:

To assure that the project works properly, you have to install all needed dependencies.

1. Clone this repo:
```bash
git clone https://github.com/lucasmaloni/titac-minimax.git
cd your-repo
```

2. Install all needed libraries with one command line:
```bash
pip install -r requirements.txt
```
**ATENTION: Graphviz must be installed folowing the instructions in this link -> https://graphviz.org/download/**

3. Run the game:
```bash
python main.py
```
