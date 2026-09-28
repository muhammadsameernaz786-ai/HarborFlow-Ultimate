# ==============================================================================
# TASK 7: Produce the weekly dispatch report
# ==============================================================================

def produce_weekly_report(deliveries_str, target):
    """
    Processes 7 daily delivery counts and a target value to print the weekly report.
    For ties, reports the LAST day with the highest/lowest value.
    """
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Split comma-separated string into integer list
    raw_parts = deliveries_str.split(",")
    deliveries = []
    for part in raw_parts:
        deliveries.append(int(part.strip()))
        
    # Manual manual traversal using accumulators
    total_deliveries = 0
    days_meeting_target = 0
    
    highest_val = deliveries[0]
    highest_day_idx = 0
    
    lowest_val = deliveries[0]
    lowest_day_idx = 0
    
    for i in range(len(deliveries)):
        val = deliveries[i]
        total_deliveries += val
        
        if val >= target:
            days_meeting_target += 1
            
        # >= and <= ensure that in case of ties, the LAST occurrence is kept
        if val >= highest_val:
            highest_val = val
            highest_day_idx = i
            
        if val <= lowest_val:
            lowest_val = val
            lowest_day_idx = i
            
    avg_per_day = total_deliveries / len(deliveries)
    
    # Print formatted summary report
    print("Weekly dispatch report")
    print(f"Total deliveries: {total_deliveries}")
    print(f"Average per day: {avg_per_day:.2f}")
    print(f"Highest day: {days[highest_day_idx]} ({highest_val})")
    print(f"Lowest day: {days[lowest_day_idx]} ({lowest_val})")
    print(f"Days meeting target: {days_meeting_target}")
    
    
# ==============================================================================
# TASK 8: Make the console resilient (Input Validation Functions)
# ==============================================================================

def get_valid_menu_option(max_option=7):
    """
    Validates main menu selections (1 to max_option).
    """
    while True:
        try:
            choice = int(input("Select service: "))
            if 1 <= choice <= max_option:
                return choice
            else:
                print("Error: Select a service from 1 to 8.")
        except ValueError:
            print("Error: Select a service from 1 to 8.")


def get_valid_positive_float(prompt):
    """
    Validates numeric inputs that must be > 0 (distance, weight, capacity).
    """
    while True:
        try:
            val = float(input(prompt))
            if val > 0:
                return val
            else:
                print("Error: Value must be greater than zero.")
        except ValueError:
            print("Error: Value must be greater than zero.")


def get_valid_service_code():
    """
    Validates service codes (must be S, X, or P).
    """
    while True:
        code = input("Service code: ").strip().upper()
        if code in ["S", "X", "P"]:
            return code
        print("Error: Service code must be S, X or P.")


def get_valid_non_negative_int(prompt):
    """
    Validates integers that must be >= 0 (minutes, damaged parcels).
    """
    while True:
        try:
            val = int(input(prompt))
            if val >= 0:
                return val
            else:
                print("Error: Value must be non-negative.")
        except ValueError:
            print("Error: Value must be non-negative.")


def get_valid_weekly_deliveries():
    """
    Validates weekly delivery inputs: exactly 7 non-negative integers.
    """
    while True:
        raw_input = input("Completed deliveries: ")
        parts = raw_input.split(",")
        
        if len(parts) != 7:
            print("Error: Weekly report requires 7 delivery counts.")
            continue
            
        valid = True
        for p in parts:
            p_str = p.strip()
            if not p_str.isdigit():
                valid = False
                break
                
        if valid:
            return raw_input
        else:
            print("Error: Weekly report requires 7 delivery counts.")


def get_valid_capacity_weights():
    """
    Validates parcel weight lists for capacity checking (all values > 0).
    """
    while True:
        raw_input = input("Parcel weights (kg): ")
        parts = raw_input.split(",")
        valid = True
        
        for p in parts:
            try:
                w = float(p.strip())
                if w <= 0:
                    valid = False
                    break
            except ValueError:
                valid = False
                break
                
        if valid:
            return raw_input
        else:
            print("Error: Value must be greater than zero.")





















"""HarborFlow Assignment 1 starter file.

Replace the TODO sections with your team's implementation. Keep the program
entry point so the file can be run with: python harborflow_app.py
"""


def main():
    """Run the HarborFlow Dispatch Console."""
    # TODO: implement the persistent menu and dispatch to task functions.
    pass


if __name__ == "__main__":
    main()
