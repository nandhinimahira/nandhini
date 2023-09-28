print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
bill="X"
c_bill="Y"
p_bill="Z"
if(size=="S"):
    X=15
    
if(size=="M"):
    X=20
if(size=="L"):
    X=25
   
add_pepperoni = input("Do you want pepperoni? Y or N ")
if(add_pepperoni=="Y"):
    
    if(size=="S"):
        Y=2
    else:
        Y=3

extra_cheese = input("Do you want extra cheese? Y or N ")
if(extra_cheese=="Y"):
    Z=1

total=X+Y+Z
print("Your final bill is:" + " "+ str(total))

