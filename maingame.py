from baker import *
from mayor import *
from scientist import *
from store import *
from musician import *
from farmer import *
from river import *
from artist import *
from location import *
import turtle

def main():


    bakerCount = 0
    scientistCount = 0
    mayorCount = 0
    musicianCount = 0
    artistCount = 0
    sugarCount = 0
    location = "mayor"
    #(sugarCount, bakerCount)
    storeTuple = (0, bakerCount)


    townName = input("Name the town: ")
    townName = townName.strip()

    mayorCount = mayor(mayorCount,townName)
    p = turtle.Turtle()
    map.map(p)
    steps = 0

    while mayorCount != 6 and location != "quit":

        if steps > 0:
            map.back(p, steps)

        locationTuple = chooseLocation(p)
        location = locationTuple[0]
        steps = locationTuple[1]


        if location == "mayor":
            mayorCount = mayor(mayorCount, townName)


        elif location == "baker":

            if bakerCount == 4:
                mayorCount += 1

            bakerCount = baker(townName, bakerCount)


        elif location == "scientist":
            if scientistCount == 3:
                mayorCount += 1

            scientistCount = scientist(scientistCount)

        elif location == "store":
            storeTuple = store(sugarCount, bakerCount)
            sugarCount = storeTuple[0]
            bakerCount = storeTuple[1]

        elif location == "farmer":
            scientistCount = farmer(scientistCount)

        elif location == "river":
            scientistCount = river(scientistCount)

        elif location == "musician":
            musicianCount = musician(musicianCount, townName)
            if musicianCount == 4:
                mayorCount += 1
                musicianCount += 1

        elif location == "artist":
            if artistCount == 4:
                mayorCount += 1
                artistCount += 1
            artistCount = artist(artistCount)

        elif location == "quit":
            print("Thanks for playing!")


main()


