import sys
import time


MAX_EXPENSES = 500


def get_single_action_analysis(line: str):
    """Parses a single line from the CSV to extract action data."""
    try:
        action_name, action_cost, action_benefit_str = line.strip().split(",")
        
        cost = float(action_cost)
        benefit_percent = float(action_benefit_str.replace('%', ''))
        
        # We should not invest in actions that have a non-positive cost.
        if cost <= 0:
            return None
            
        money_earn = (cost * benefit_percent) / 100
        
        return {
            "name": action_name,
            "cost": cost,
            "benefit_money": money_earn,
            "benefit_percent": benefit_percent,
        }
    except (ValueError, IndexError):
        return None


def find_best_investment(actions):
    """
    Selects the best actions to invest in based on a greedy algorithm.
    It prioritizes actions with the highest benefit percentage.
    """
    # Sort actions by their benefit percentage in descending order
    sorted_actions = sorted(actions, key=lambda x: x['benefit_percent'], reverse=True)
    
    best_combination = []
    current_cost = 0
    
    for action in sorted_actions:
        if current_cost + action['cost'] <= MAX_EXPENSES:
            best_combination.append(action)
            current_cost += action['cost']
            
    return best_combination


if __name__ == "__main__":
    start_time = time.time()
    
    action_list_path = "actions_list.csv"
    actions_analysis = []
    
    if len(sys.argv) > 1:
        action_list_path = sys.argv[1]
    
    # 1. Read the action list and parse data
    try:
        with open(action_list_path, "r") as file:
            next(file)  # Skip header
            for line in file:
                if not line.strip():
                    continue
                
                analyzed_action = get_single_action_analysis(line)
                if analyzed_action:
                    actions_analysis.append(analyzed_action)
    except Exception as e:
        print(f"Error reading the file: {e}")
        sys.exit(1)
                
    # 2. Find the best investment using the optimized algorithm
    best_actions = find_best_investment(actions_analysis)
    
    end_time = time.time()
    
    # 3. Display the results
    print("Optimized algorithm results:")
    if best_actions:
        total_cost = sum(action['cost'] for action in best_actions)
        total_benefit = sum(action['benefit_money'] for action in best_actions)
        
        print("Best investment combination found:")
        for action in best_actions:
            print(f"- {action['name']} (Cost: {action['cost']}€, Benefit: {action['benefit_money']:.2f}€)")
        
        print(f"\nTotal cost: {total_cost:.2f}€")
        print(f"Total benefit (profit): {total_benefit:.2f}€")
    else:
        print("No suitable investment combination found within the budget.")
        
    print(f"\nExecution time: {end_time - start_time:.4f} seconds")