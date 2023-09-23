# Testing Report

## Modules Tested
- MarkovModel Class
- Game Class

## Testing Overview:
- Various aspects including initialization, update, reset, focus limit, and order limit were tested.
- Tests were executed with string inputs representing different moves: 'rock', 'paper', and 'scissors'.
- The coverage report provides insights into areas covered and those requiring more testing.

## Testing Methodology
- **Initialization Testing:**
  - Objective: Validate correct initialization of classes with proper attributes and their default values.
  
- **Update and Score Testing:**
  - Objective: Validate score calculations and updates after every move.
  
- **Reset Testing:**
  - Objective: Ensure proper resetting of attributes to initial states.
  
- **Focus and Order Limit Testing:**
  - Objective: Ensure no exceedance of set limits in `score_history` and `user_moves`.

- **Play Method Testing:**
  - Objective: Validate method call sequencing and result accuracy.
  
- **AI Move, Round Evaluation, and Model Update Testing:**
  - Objective: Validate the correctness of AI moves, round evaluations, and model updates with user moves.


## Test Inputs
- Tests were performed using string inputs representing various moves: `'rock'`, `'paper'`, and `'scissors'`.

## Test Execution

- **Coverage Report Location:** [Coverage Report Site](https://app.codecov.io/gh/lina-ova/rockPaperScissors)

**Note**:
All the local testing and coverage command lines should be run at the root of the repository to ensure correct path resolution and access to all necessary files and modules.

- **Local Testing:**
  ```shell
  pip install pytest
  pytest
  ```

- For local coverage report generation:
    ```shell
      pip install coverage
      coverage run -m pytest main
      coverage report -m 
    ```

## Limitations and Future Work
- **UI Testing:** Currently, not implemented due to complexity.
- **Additional Testing:** Areas unreached by current tests, as identified by the coverage report, should have additional tests written for more thorough coverage.
