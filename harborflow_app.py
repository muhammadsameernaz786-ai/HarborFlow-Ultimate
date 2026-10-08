# Task1 Menu building
# Task2: Validate booking reference and handle
def validate_reference(reference):
    normalized = reference.strip().upper()

    # Rule 1: must be exactly 12 characters
    if len(normalized) != 12:
        return ""

    # Rule 2: hyphens must be in the right spots
    if normalized[3] != "-" or normalized[7] != "-":
        return ""

    prefix = normalized[0:3]
    customer_code = normalized[4:7]
    shipment_number = normalized[8:12]

    # Rule 3: prefix must be HFL
    if prefix != "HFL":
        return ""

    # Rule 4: customer code must be 3 letters
    if not customer_code.isalpha():
        return ""

    # Rule 5: shipment number must be 4 digits
    if not shipment_number.isdigit():
        return ""

    return normalized

def handle_validate_reference():
    reference = input("Booking reference: ")
    result = validate_reference(reference)

    if result != "":
        print("Valid reference:", result)
    else:
        print("Invalid booking reference.")

# Task 3: Calculate delivery quote
def calculate_quote(distance, weight, service_code):
    #Basic components for the quote and subtotal
    base_charge = 45.00
    
    # Conditions for the service code
    if service_code == "S":
        service_multiplier = 1.0
    elif service_code == "X":
        service_multiplier = 1.25
    elif service_code == "P":
        service_multiplier = 1.6
    
    # Calculation for subtotal and delivery quote
    subtotal = base_charge + (distance * 6.5) + (weight * 4)
    quote = subtotal * service_multiplier
    return quote

def get_valid_service_code():
    """
    Validates service codes (must be S, X, or P).
    """
    while True:
        code = input("Service code: ").strip().upper()
        if code in ["S", "X", "P"]:
            return code
        print("Error - Service code must be S, X or P.")

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
                print("Error - Value must be greater than zero.")
        except ValueError:
            print("Error - Value must be greater than zero.")

def handle_delivery_quote():
    distance = get_valid_positive_float("Distance (km): ")
    weight = get_valid_positive_float("Weight (kg): ")
    service_code = get_valid_service_code()
    quote = calculate_quote(distance, weight, service_code)
    print(f"Delivery quote: {quote:.2f} SEK")
    
#Task 4 - Consolidate parcel labels
# list, distinct label once, preserving the order, 
# splitting, loops, normalization, memberships checks, ordered output

def consolidate_parcel_labels():
    scanned_labels = input("Scanned labels: ")
    scanned_labels = scanned_labels.split(",")

    unique_labels = []

    for label in scanned_labels:
        label = label.upper()
        label = label.strip()
        if label not in unique_labels:
            unique_labels.append(label)

    print(f"Unique load list:")

    for number, label in enumerate(unique_labels, start = 1):
        print(f"{number}. {label}")

    print(f"Total unique parcels: {len(unique_labels)}")


def get_valid_capacity_weights():
    """Validates parcel weight lists for capacity checking (all values > 0)."""
    while True:
        raw_input = input("Parcel weights (kg): ")
        parts = raw_input.split(",")
        weights = []
        valid = True
        
        for part in parts:
            try:
                weight = float(part.strip())
            except ValueError:
                valid = False
                break
            if weight <= 0:
                valid = False
                break
            weights.append(weight)
                
        if valid:
            return weights
        else:
            print("Error - Value must be greater than zero.")


# Task 5:  Check Van Capacity function
def check_van_capacity():
    capacity = get_valid_positive_float("Van capacity (kg): ")
    weights = get_valid_capacity_weights()
    remaining_capacity = capacity
    accepted_count = 0
    loaded_weight = 0.0

    # Used For Loop and If-Else statement
    for i in range(len(weights)):
        weight = weights[i]

        if weight <= remaining_capacity:
            print(f"Parcel {i + 1}: ACCEPTED")
            accepted_count += 1
            loaded_weight += weight
            remaining_capacity -= weight
        else:
            print(f"Parcel {i + 1}: REJECTED")

    print(f"Accepted parcels: {accepted_count}")
    print(f"Loaded weight: {loaded_weight:.2f} kg")
    print(f"Remaining capacity: {remaining_capacity:.2f} kg")

# Task 6:  Classify Performance and Service performance function
def classify_performance(promised, actual, damaged):
    delay = actual - promised

# Using If-Else Statements 

    if damaged > 0:
        status = "SERVICE FAILURE"
    elif delay <= 0:
        status = "ON TIME"
    elif delay <= 15:
        status = "MINOR DELAY"
    else:
        status = "MAJOR DELAY"

    return delay, status

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
                print("Error - Value must be non-negative.")
        except ValueError:
            print("Error - Value must be non-negative.")
            
# Created another function named Service Performance 
def service_performance():
    promised = get_valid_non_negative_int("Promised minutes: ")
    actual = get_valid_non_negative_int("Actual minutes: ")
    damaged = get_valid_non_negative_int("Damaged parcels: ")

    delay, status = classify_performance(promised, actual, damaged)

    print(f"Delay: {delay} minutes")
    print(f"Service status: {status}")


# ==============================================================================
# TASK 7: Produce the weekly dispatch report
# ==============================================================================
def produce_weekly_report(deliveries, target):
    """
    Processes 7 daily delivery counts and a target value to print the weekly report.
    For ties, reports the LAST day with the highest/lowest value.
    """
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
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

def handle_weekly_report():
    deliveries = get_valid_weekly_deliveries()
    target = get_valid_non_negative_int("Daily target: ")

    produce_weekly_report(deliveries, target)    
    
# ==============================================================================
# TASK 8: Make the console resilient (Input Validation Functions)
# ==============================================================================

def get_valid_menu_option(max_option=8):
    """
    Validates main menu selections (1 to max_option).
    """
    while True:
        try:
            choice = int(input("Select service: "))
            if 1 <= choice <= max_option:
                return choice
            else:
                print("Error - Select a service from 1 to 8.")
        except ValueError:
            print("Error - Select a service from 1 to 8.")


def get_valid_weekly_deliveries():
    """
    Validates weekly delivery inputs: exactly 7 non-negative integers.
    """
    while True:
        raw_deliveries = input("Completed deliveries: ")
        parts = raw_deliveries.split(",")
        
        if len(parts) != 7:
            print("Error - Weekly report requires 7 delivery counts.")
            continue
        
        deliveries = []    
        valid = True
        
        for part in parts:
            text = part.strip()
            if not text.isdigit():
                valid = False
                break
            deliveries.append(int(text))
                
        if valid:
            return deliveries
        else:
            print("Error - Weekly report requires 7 delivery counts.")


# Task 9 (depending on Task 3)
def compare_service_scenarios():
    distance = get_valid_positive_float("Distance (km): ")
    weight = get_valid_positive_float("Weight (kg): ")
    
    # Reusage of Task 3 function to calculate quotes for each service type
    standard_quote = calculate_quote(distance, weight, "S")
    express_quote = calculate_quote(distance, weight, "X")
    priority_quote = calculate_quote(distance, weight, "P")
    
    # Cheapest and most expensive service comparison
    cheapest_quote = standard_quote
    cheapest_service = "Standard"
    
    if express_quote < cheapest_quote:
        cheapest_quote = express_quote
        cheapest_service = "Express"
    if priority_quote < cheapest_quote:
        cheapest_quote = priority_quote
        cheapest_service = "Priority"

    most_expensive_quote = standard_quote
    most_expensive_service = "Standard"
    
    if express_quote > most_expensive_quote:
        most_expensive_quote = express_quote
        most_expensive_service = "Express"
    if priority_quote > most_expensive_quote:
        most_expensive_quote = priority_quote
        most_expensive_service = "Priority"
    
    print(f"Service comparison")
    print(f"Standard: {standard_quote:.2f} SEK")
    print(f"Express: {express_quote:.2f} SEK")
    print(f"Priority: {priority_quote:.2f} SEK")
    print(f"Cheapest service: {cheapest_service}")
    print(f"Most expensive service: {most_expensive_service}")    


"""HarborFlow Assignment 1 starter file.

Replace the TODO sections with your team's implementation. Keep the program
entry point so the file can be run with: python harborflow_app.py
"""


def main():
    # Task 1: Build the dispatch menu
    while True:
        print("\nHARBORFLOW DISPATCH CONSOLE")
        print("1. Close console")
        print("2. Validate booking reference")
        print("3. Calculate delivery quote")
        print("4. Consolidate parcel labels")
        print("5. Check van capacity")
        print("6. Classify service performance")
        print("7. Produce weekly dispatch report")
        print("8. Compare service scenarios")
        choice = get_valid_menu_option(8)

        if choice == 1:
            print("Console closed. Dispatch data remains safe.")
            break  # Ends the while loop, which ends the program
        elif choice == 2:
            handle_validate_reference()
        elif choice == 3:
            # Printing values for the quote and subtotal
            handle_delivery_quote()
        elif choice == 4:
            consolidate_parcel_labels()
        elif choice == 5:
            check_van_capacity()
        elif choice == 6:
            service_performance()
        elif choice == 7:
            handle_weekly_report()
        elif choice == 8:
            compare_service_scenarios()
        else:
            print("Error - Select a service from 1 to 8.")


if __name__ == "__main__":
    main()
