# AlgoInvest & Trade

This project analyzes and compares two algorithms for selecting a portfolio of shares to maximize returns within a fixed budget. It includes a brute-force method that explores all possible combinations and an optimized dynamic programming approach for efficiency.

## Algorithms

- `bruteforce.py`: A script that implements the brute-force algorithm to find the best combination of shares. It has an exponential time complexity, making it suitable only for small datasets.
- `optimized.py`: A script using dynamic programming (knapsack problem approach) to find the optimal portfolio. This approach is much more efficient and can handle larger datasets.

## Dataset

The `actions_list.csv` file contains the list of available shares with their cost and profit after 2 years. The `backtest` directory contains other datasets for testing purposes.

## Usage

To run the algorithms, you can execute the Python scripts from your terminal.

```bash
# Run the brute-force algorithm
python bruteforce.py

# Run the optimized algorithm
python optimized.py
```

## Dependencies

This project requires Python 3. It is recommended to use a virtual environment to manage dependencies.
