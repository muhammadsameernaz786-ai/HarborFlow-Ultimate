"""HarborFlow Assignment 1 starter file.

Replace the TODO sections with your team's implementation. Keep the program
entry point so the file can be run with: python harborflow_app.py
"""
#Task 3
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

# Task 9 (depending on Task 3)
def compare_service_scenarios():
    distance = float(input("Distance (km): "))
    weight = float(input("Weight (kg): "))
    
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



def main():
    """Run the HarborFlow Dispatch Console."""
    # TODO: implement the persistent menu and dispatch to task functions.
    compare_service_scenarios()


if __name__ == "__main__":
    main()
