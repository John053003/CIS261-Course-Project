#John Fernandez
#CIS261
#Project Phase 1 

def get_employee_name():
    # Get employee name from user
    name = input('Enter employee name (or "End" to terminate: ')
    return name

def get_hours_worked():
    while True:
        try:
            hours = float(input('Enter hours worked: '))
            if hours >= 0: #Making sure hours isn't negative 
                return hours 
            else: 
                print('Hours worked cannot be negative. Please try again.')
        except ValueError:
            print('Please enter a valid number.')
def calculate_pay(hours, rate, tax_rate):
    # Calculate gross pay, income tax, and net pay
    #Return these values 
    pass #You'll need to implement the calculations 

def main():
    # Initialize variables for totals 

    # Start the main loop
    while True:
        # Get employee information by calling your functions 
        employee_name = get_employee_name()

        # Check if user wants to end the program
        if employee_name.lower() == 'end': 
            break

        # Continue getting other information and perform calculations 

        # Display information for this employee




    pass

if __name__ == "__main__":
    main()
