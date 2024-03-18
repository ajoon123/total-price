sum = 0
while(True):
    userInput = input("Enter the item price or press q to quit: \54n")
    if (userInput!='q'):
        sum = sum + int(userInput)
        print(f"order total so far: {sum}")

    else:
         print(f"your bill total is {sum}. thanks")
         break

