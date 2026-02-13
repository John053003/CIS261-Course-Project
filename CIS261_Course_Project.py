#John Fernandez
#CIS261
#Project Phase 1 

def get_employee_name():
    # Get employee name from user
    name = input("Enter employee name (or 'End' to terminate: ")
    return name

def get_hours_worked():
    while True:
        try:
            hours = float(input("Enter hours worked: "))
            if hours >= 0: #Making sure hours isn't negative 
                return hours 
            else: 
                print("Hours worked cannot be negative. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
def get_hourly_rate():
    while True: 
        try:
            rate = float(input("Enter hourly rate: "))
            if rate >= 0:
                return rate 
            else:
                print("Hourly rate cannot be negative. Please try again.")
        except ValueError: 
            print("Please enter a valid number.") 

def get_tax_rate(): 
    while True:
        try: 
            tax_rate = float(input("Enter income tax rate (example 0.15 for 15%): "))
            if 0 <= tax_rate <= 1:
                return tax_rate 
            else:
                print("Tax rate must be between 0 and 1. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def calculate_pay(hours, rate, tax_rate):
    gross_pay = hours * rate 
    income_tax = gross_pay * tax_rate 
    net_pay = gross_pay - income_tax 
    return gross_pay, income_tax, net_pay 

def display_employee_summary(name, hours, rate, tax_rate, gross, tax, net):
    print("\n--- Employee Summary ---")
    print(f"Name: {name}") 
    print(f"Hours Worked: {hours:.2f}")
    print(f"Hourly Rate: ${rate:.2f}")
    print(f"Tax Rate: {tax_rate:.2f}")
    print(f"Gross Pay: ${gross:.2f}")
    print(f"Income Tax: ${tax:.2f}")
    print(f"Net Pay: ${net:.2f}")

def display_totals(total_employees, total_hours, total_gross, total_tax, total_net):
    print("\n===== FINAL TOTALS =====")
    print(f"Employees: {total_employees}")
    print(f"Total Hours: {total_hours:.2f}")
    print(f"Total Gross Pay: ${total_gross:.2f}")
    print(f"Total Income Tax: ${total_tax:.2f}")
    print(f"Total Net Pay: ${total_net:.2f}")

    
def main():
    total_employees = 0 
    total_hours = 0 
    total_gross = 0 
    total_tax = 0 
    total_net = 0 

    # Start the main loop
    while True:
        # Get employee information by calling your functions 
        employee_name = get_employee_name()

        # Check if user wants to end the program
        if employee_name.lower() == 'end': 
            break

        hours = get_hours_worked()
        rate = get_hourly_rate()
        tax_rate = get_tax_rate()

        gross, tax, net = calculate_pay(hours, rate, tax_rate)

        display_employee_summary(employee_name, hours, rate, tax_rate, gross, tax, net)

        total_employees += 1
        total_hours += hours
        total_gross += gross
        total_tax += tax
        total_net += net

        display_totals(total_employees, total_hours, total_gross, total_tax, total_net)


        # Display information for this employee

if __name__ == "__main__":
    main()
