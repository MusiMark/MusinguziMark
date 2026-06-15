print("="*6 + " BILL SPLIT CALCULATOR " + "="*6)

while True:
    try:
        total_bill = int(input("Enter total bill: "))
    except ValueError:
        total_bill = 0

    if total_bill > 0:
        break
    elif total_bill == 0:
        print("Invalid input, please enter a numeric value")
    else:
        print("Bill cannot be negative, please enter a value greater than 0")

while True:
    try:
        no_of_people = int(input("Enter number of people: "))
    except ValueError:
        no_of_people = 0

    if no_of_people > 0:
        break
    elif no_of_people == 0:
        print("Invalid input, please enter a numeric value")
    else:
        print("Number of people cannot be negative, please enter a value greater than 0")

while True:
    try:
        choice = int(input("Choose tip percentage: \n1) 10% \n2) 15% \n3) 20% \n4) custom\n"))
    except ValueError:
        choice = 0

    match choice:
        case 1:
            tip_percentage = 0.1
            break
        case 2:
            tip_percentage = 0.15
            break
        case 3:
            tip_percentage = 0.20
            break
        case 4:
            try:
                value = int(input("Enter a custom tip percentage(between 0 and 100): "))
            except ValueError:
                value = 0
                print("Invalid tip, please enter a value greater than 0")

            if 0<value<=100:
                tip_percentage = (value/100)
                break
        case _:
            print("Invalid choose, please enter either '1','2','3' or '4'")

# Calculations
tip_amount = tip_percentage * total_bill
total_amount = total_bill + tip_amount
amount_per_person = total_amount / no_of_people

#Output
print("="*6 + " RECEIPT " + "="*6)
print(f"Total bill: Ugx {total_bill}")
print(f"Tip: {tip_percentage * 100}%")
print(f"Total tip: Ugx {tip_amount}")
print(f"Total amount: Ugx {total_amount}")
print(f"Amount per person({no_of_people}): Ugx {amount_per_person}")