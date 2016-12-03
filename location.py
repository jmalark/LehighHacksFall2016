import turtle
import map

def locationfinder(p,location):
    place=0
    if location=="baker":
        place=7
    elif location=="farmer":
        place=4
    elif location=="artist":
        place=2
    elif location=="mayor":
        place=8
    elif location=="store":
        place=1
    elif location=="river":
        place=3
    elif location=="musician":
        place=5
    elif location=="scientist":
        place=6

    else:
        print("Sorry, but that is not in this town. Please try visiting one of the areas in the town")
    return place
def chooseLocation(myTurtle):
    p = myTurtle
    print("Legend: ")
    print("store = yellow")
    print("artist = pink")
    print("river = blue")
    print("farmer = green")
    print("musician = orange")
    print("scientist = purple")
    print("baker = brown")
    print("mayor = red")


    location=input("Where would you like to go?: ").strip().lower()
    place=locationfinder(p,location)
    steps = map.move(p, place)

    return (location,steps)
