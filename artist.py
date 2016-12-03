

def artist(artistCount):
    print("You arrived at the artist's house.")

    if artistCount == 0:
        print("You open the door.")
        input()
        print("There's huge colorful pieces of paper everywhere.")
        input()
        print("From underneath a particularly large sheet, someone emerges.")
        input()
        print("\"Oh. Hello. Don't mind the mess, I'm just trying to get the float decorations ready.\"")
        input()
        print("\"Only problem is that I'm having some trouble figuring out the details.\"")
        input()
        print("\"You see I was told that I need to include certain shaped designs, but I don't remember how to make those shapes.\"")
        input()
        print("\"Do you think you could help me out?\"")
        input()
        artistCount += 1

    if artistCount == 1:
        artistCount = shapes(artistCount)

    if artistCount == 2:
        print("\"I'm really glad to have that figured out.\"")
        input()
        print("\"Now I only have to figure out if I have enough supplies for the next step.\"")
        input()
        print("\"I don't suppose you could help me out with that too?\"")
        artistCount += 1

    if artistCount == 3:
        print("\"I started off with 24 sheet of paper.\"")
        input()
        print("\"I've used 8 already.\"")
        input()
        print("\"I need 14 to make the next decoration.\"")
        input()
        print("\"Do I have enough left?\"")
        input()
        answer = ""

        while artistCount == 3 and answer != "quit":
            answer = input("Type yes or no to answer. Type quit to quit. ")
            if answer == "yes":
                artistCount += 1

    if artistCount == 4:
        print("\"Thanks a ton! Now my decorations are going to be amazing!\"")
        input()

    if artistCount == 5:
        print("You can't seem to find anyone in the mess of papers.")
        input()

    return artistCount

def shapes(artistCount):
    answerCount = 0
    answer = ""
    gotWrong = False
    while answerCount == 0 and answer != "quit":
        if gotWrong:
            print("Are you sure you're thinking of the right shape? Maybe you should try again.")
        print("\"Do you know how many sides a hexagon has?\"")
        print("a: 4")
        print("b: 5")
        print("c: 6")
        answer = input("Answer with a, b, or c. Type quit by typing quit. ").strip().lower()
        if answer == "c":
            answerCount += 1
        else:
            gotWrong = True

    gotWrong = False

    while answerCount == 1 and answer != "quit":
        if gotWrong:
            print("Are you sure you're thinking of the right shape? Maybe you should try again.").strip().lower()

        print("\"How many sides does an octagon have?\"")
        print("a: 5")
        print("b: 8")
        print("c: 12")
        answer = input("Answer with a, b, or c. Type quit by typing quit. ").strip().lower()
        if answer == "b":
            answerCount += 1
        gotWrong = True

    if answerCount == 2:
        artistCount += 1

    return artistCount