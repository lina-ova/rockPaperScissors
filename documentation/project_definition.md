### Rock-paper-scissors Using Markov Chains with Multi-AI Approach: Specification Document

#### **1. Programming Language and Expertise**
- **Programming language used**: **Python**
- Other languages I'm proficient in for peer review: Java, JavaScript

#### **2. Algorithms, Data Structures, and Techniques Employed**
- **Markov Chains**: Utilized for predicting and optimizing strategies in the rock-paper-scissors game.

- **Multi-AI Approach**: Combining various orders of Markov Chains (1st to 5th) to effectively counter varying human strategies by rapidly adapting to recent human play patterns.

- **List structures in Python**: Used for storing inputs, statistics, and the recent performance of each Markov Chain model.

- **Dynamic AI Selection**: Based on the recent performance (tracked through a parameter named "focus length") of each Markov Chain model, the AI selects the most suitable model for the upcoming move.

#### **3. Problem to Solve and Rationale for Choices**
- Aim is to enhance the artificial intelligence performance in the rock-paper-scissors game, allowing it to outperform various human strategies.
- Markov Chains were chosen because they are well-suited for analyzing sequences where the next event depends only on the previous one.
- The Multi-AI approach is employed to cater to the variability and unpredictability of human strategy.

#### **4. Inputs and Their Utilization**
- The program takes the player's moves: rock, paper, or scissors as input.
- These inputs are utilized for updating the state matrix of each Markov Chain model and predicting the next move.

#### **5. Time and Space Complexity**
- **Time Complexity**: O(n) where n is the number of AI models.
- **Space Complexity**: O(n) for storing the performance history and state of each model.

#### **6. References**
- [Markov chains, wikipedia](https://en.wikipedia.org/wiki/Markov_chain)
- [Multi‑AI competing and winning
against humans in iterated
Rock‑Paper‑Scissors game](https://arxiv.org/ftp/arxiv/papers/2003/2003.06769.pdf)

#### **7. Academic Program**
- Tietojenkäsittelytieteen kandidaatti (TKT)

#### **8. Documentation Language**
- Language for project code, comments, and documentation: **English**
