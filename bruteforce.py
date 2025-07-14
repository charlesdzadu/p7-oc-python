import itertools
import sys
import time


MAX_EXPENSES = 500


def get_single_action_analysis(line: str):
    """Parses a single line from the CSV to extract action data."""
    action_name, action_cost, action_benefit = line.strip().split(",")
    
    action_cost = float(action_cost)
    
    # Remove percentage sign from benefit
    action_benefit = action_benefit.replace("%", "")
    benefit_in_percentage = float(action_benefit)
    
    
    
    money_earn = (action_cost * benefit_in_percentage) / 100
    
    # Accept only 2 decimal places
    money_earn = round(money_earn, 2)
    
    # Check  if action_cost is not zero to avoid division by zero
    ratio = 0
    if action_cost != 0:
        ratio = money_earn / action_cost
        ratio = round(ratio, 4)
    
    return {
        "name": action_name,
        "cost": action_cost,
        "benefit": money_earn,
        "ratio": ratio,
    }


if __name__ == "__main__":
    start_time = time.time()
    action_list_path = "actions_list.csv"
    actions_analysis = []
    
    # Check args for action list path
    if len(sys.argv) > 1:
        action_list_path = sys.argv[1]
        

    
    # 1. Read the action list path line by line
    try:
        with open(action_list_path, "r") as file:
        # Skip header
            next(file)
            for line in file:
                if not line.strip():
                    continue
                actions_analysis.append(get_single_action_analysis(line))
    except Exception as e:
        print(f"Error reading the file: {e}")
        sys.exit(1)

    best_combination = None
    max_benefit = 0.0
    
    print(f"Number of actions: {len(actions_analysis)}")

    all_combinations = []
    for r in range(1, len(actions_analysis) + 1):
        combinations_object = itertools.combinations(actions_analysis, r)
        all_combinations.extend(list(combinations_object))
        
        
    print(f"Number of combinations: {len(all_combinations)}")

    for combo in all_combinations:
        total_cost = sum(action['cost'] for action in combo)
        total_benefit = sum(action['benefit'] for action in combo)

        if total_cost <= MAX_EXPENSES:
            if total_benefit > max_benefit:
                max_benefit = total_benefit
                best_combination = combo

    end_time = time.time()
    
    print("Brute-force algorithm results:")
    if best_combination:
        total_cost_of_best_combo = sum(action['cost'] for action in best_combination)
        print("Best investment combination found:")
        for action in best_combination:
            print(f"- {action['name']} (Cost: {action['cost']}€, Benefit: {action['benefit']:.2f}€)")
        print(f"\nTotal cost: {total_cost_of_best_combo:.2f}€")
        print(f"Total benefit (profit): {max_benefit:.2f}€")
    else:
        print("No suitable investment combination found within the budget.")
        
    print(f"\nExecution time: {end_time - start_time:.2f} seconds")









