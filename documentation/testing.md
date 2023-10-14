# **Testing Report**

## **Modules Tested**
- **MarkovModel Class**
- **Game Class**

## **Testing Overview:**
- For the `MarkovModel` class, various aspects including initialization, update, prediction, move evaluation, score retrieval, and reset were tested.
- For the `Game` class, areas such as the gameplay loop, user input handling, game outcomes, and player-AI interactions were covered.
- Tests were executed with string inputs representing different moves: 'rock', 'paper', and 'scissors'.
- The coverage report provides insights into areas covered and those requiring more testing.

## **Testing Methodology**

### **MarkovModel Class:**

- **Initialization Testing:**
  - *Objective:* Validate correct initialization with proper attributes and their default values.
  
- **Update and Score Testing:**
  - *Objective:* Validate score calculations and updates after every move.
  
- **Prediction Testing:**
  - *Objective:* Verify that predictions are made and cover the entire set of moves.
  
- **Move Evaluation Testing:**
  - *Objective:* Check if the moves are evaluated correctly considering the AI's move.
  
- **Score Retrieval Testing:**
  - *Objective:* Ensure that the score is accurately calculated from the score history.
  
- **Reset Testing:**
  - *Objective:* Ensure proper resetting of attributes to initial states.
  
- **Pattern Prediction Testing:**
  - *Objective:* Test the model's ability to recognize patterns and make accurate predictions based on those patterns.
  
- **Focus and Order Limit Testing:**
  - *Objective:* Ensure no exceedance of set limits in `score_history` and `user_moves`.

### **Game Class:**

- **Gameplay Loop Testing:**
  - *Objective:* Ensure that the game progresses in an expected manner, transitioning through various stages.
  
- **User Input Handling:**
  - *Objective:* Validate that user inputs for moves are correctly received and processed.
  
- **Determining Game Outcomes:**
  - *Objective:* Verify the correctness in determining round and overall game winners.
  
- **Player-AI Interaction:**
  - *Objective:* Test the interaction mechanics between the player and the AI, ensuring a balanced and competitive gameplay experience.

## **Test Inputs**
- Tests were performed using string inputs representing various moves: `'rock'`, `'paper'`, and `'scissors'`.

## **Test Execution**

- **Coverage Report Location:** [Coverage Report Site](https://app.codecov.io/gh/lina-ova/rockPaperScissors)

> **Note:** All the local testing and coverage command lines should be run at the root of the repository to ensure correct path resolution and access to all necessary files and modules.

```shell
pip install pytest
pytest
```

```shell
pip install coverage
coverage run -m pytest main
coverage report -m 
```

## **Limitations and Future Work**
- **UI Testing:** Currently, not implemented due to complexity.
- **Additional Testing:** Areas unreached by current tests, as identified by the coverage report, should have additional tests written for more thorough coverage.
