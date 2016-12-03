

def store(sugarCount, bakerCount):
    print("You arrive at the store.")
    response = ""



    if bakerCount == 0:
        print("The store seems to be closed.")
        input()

    else:
        print("\"Welcome! Would you like to buy something?\"")
        input()
        print("\"We sell 4 pound bags of sugar and 5 pound bags of sugar.\"")
        input()


        if sugarCount > 0:
            print("\"You can also make returns.\"")
            input()


        while response != "d":
            print("\"What would you like to do?\"")


            print("Type the letter that matches what you want to do: ")
            print("a: Buy a 4 pound bag of sugar")
            print("b: Buy a 5 pound bag of sugar")
            print("c: Return your sugar")
            print("d: Exit the store")

            response = input().strip().lower()

            if response == "a":
                sugarCount += 4
                print("You bought a 4 pound bag of sugar. Now you have", sugarCount, "pounds of sugar.")
                input()
            elif response == "b":
                sugarCount += 5
                print("You bought a 5 pound bag of sugar. Now you have", sugarCount, "pounds of sugar.")
                input()
            elif response == "c":
                sugarCount = 0
                print("You returned all of the sugar. Now you have", sugarCount, "pounds of sugar.")
                input()

        if bakerCount <=4:
            if sugarCount == 0:
                bakerCount = 1

            elif sugarCount < 13:
                bakerCount = 2
            elif sugarCount > 13:
                bakerCount = 3

            else:
                bakerCount = 4


    return (sugarCount, bakerCount)