print("Welcome to Python Pizza Deliveries!")

# Input collection with validation
size = input("What size pizza do you want? S, M, L: ").upper()
while size not in ["S", "M", "L"]:
    print("Invalid input. Please enter S, M, or L.")
    size = input("What size pizza do you want? S, M, L: ").upper()

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
while pepperoni not in ["Y", "N"]:
    print("Invalid input. Please enter Y or N.")
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()

extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
while extra_cheese not in ["Y", "N"]:
    print("Invalid input. Please enter Y or N.")
    extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

# Bill calculation
bill = 0

# Base price based on size
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

# Add-ons
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")



