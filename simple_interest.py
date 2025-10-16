# simple_interest.py
# Program to calculate Simple Interest

def calculate_simple_interest(principal, rate, time):
    """Calculate simple interest given principal, rate, and time."""
    return (principal * rate * time) / 100


if __name__ == "__main__":
    print("=== Simple Interest Calculator ===")
    try:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the rate of interest (%): "))
        time = float(input("Enter the time (in years): "))

        interest = calculate_simple_interest(principal, rate, time)
        print(f"\nSimple Interest = {interest:.2f}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")
