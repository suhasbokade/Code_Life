num1 = input("Please enter a number")
try:
    num2 = int(num1)
    print(num2)
except Exception:
    print("You are enter the correct input")
print("Outside of try-except clauses. This statement is always executed.")


#while True:
 #   try:
  #      name = input("Please enter an string: ")
   #     n = char(name)
    #    print(n)
     #   break
    #except Exception:
     #   print("No valid integer! Please try again ...")

#print("Great, you successfully entered an integer!")