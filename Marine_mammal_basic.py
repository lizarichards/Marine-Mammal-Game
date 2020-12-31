count = 0

def hello():
    mammals = ["walrus", "polar bear", "dolphin", "whale", "sea otter", "manatee", "sea lion"]
    print("Instructions: You will be given some facts about a marine mammal")
    print("Based on the facts, you have to guess which marine mammal I am talking about")
    print("When entering your guess, make sure that it is either all lower case, or that you capitalize the first letter")
    print("\n")
    print("Here are the options: ")
    for item in mammals:
        print(item)
    print("\n")
    print("I will be keeping score so do your best!")
    print("Let's begin!")
    print("\n")


def dolphin():
    print("Fact 1: This marine mammal is known to be social, as they travel, play, and hunt in groups")
    print("Fact 2: This marine mammal is very smart, as they have evolved to have large brains")
    print("\n")
    global count
    val = input("Based on these facts, what marine mammal do you think it is?: ")
    if (val == "dolphin") or (val == "Dolphin"):
        print("Correct! The animal is a dolphin!")
        count += 1
        print("\n")
    else:
        print("That is incorrect, I will give you another fact and you can try again.")
        print("Fact 3: This marine mammal has conical shaped teeth")
        val = input("Based on these facts, what marine mammal do you think it is?: ")
        if (val == "dolphin") or (val == "Dolphin"):
            print("Correct! The animal is a dolphin!")
            count += 1
            print("\n")
        else:
            print("That is incorrect, here is one more fact")
            print("Fact 4: ")
            val = input("Based on these facts, what marine mammal do you think it is?: ")
            if (val == "dolphin") or (val == "Dolphin"):
                print("Correct! The animal is a dolphin!")
                count += 1
                print("\n")
            else:
                print("That is incorrect, The animal is a dolphin!")
                print("\n")

def walrus():
    print("Fact 1: This marine mammals has very large tusks used to break through ice and to defend itself")
    print("Fact 2: This marine mammal is one of the largest pinnipeds")
    print("\n")
    global count
    val = input("Based on these facts, what marine mammal do you think it is?: ")
    if (val == "walrus") or (val == "Walrus"):
        print("Correct! The animal is a walrus!")
        count += 1
        print("\n")

    else:
        print("That is incorrect, I will give you another fact and you can try again.")
        print("Fact 3: This marine mammal can lower its heartbeat to live in very cold temperatures like the Artic Circle")
        val = input("Based on these facts, what marine mammal do you think it is?: ")
        if (val == "walrus") or (val is "Walrus"):
            print("Correct! The animal is a walrus!")
            count += 1
            print("\n")

        else:
            print("That is incorrect, here is one more fact")
            print("Fact 4: This animal uses their whiskers to find clams and crustaceans along the bottom of Ocean")
            val = input("Based on these facts, what marine mammal do you think it is?: ")
            if (val == "walrus") or (val == "Walrus"):
                print("Correct! The animal is a walrus!")
                count += 1
                print("\n")

            else:
                print("That is incorrect, The animal is a walrus!")
                print("\n")


def polar_bear():
    print("Fact 1: This marine mammal can move quickly on land and in the water")
    print("Fact 2: This marine mammal is the largest land carnivore")
    global count
    print("\n")

    val = input("Based on these facts, what marine mammal do you think it is?: ")
    if (val == "polar bear") or (val == "Polar bear") or (val == "Polar Bear"):
        print("Correct! The animal is a polar bear!")
        count += 1
        print("\n")

    else:
        print("That is incorrect, I will give you another fact and you can try again.")
        print("Fact 3: Their paws are designed for traversing across snow and ice")
        val = input("Based on these facts, what marine mammal do you think it is?: ")
        if (val == "polar bear") or (val == "Polar bear") or (val == "Polar Bear"):
            print("Correct! The animal is a polar bear!")
            count += 1
            print("\n")

        else:
            print("That is incorrect, here is one more fact")
            print("Fact 4: This marine mammal can have up to 5 litters of cubs in their lifetime")
            val = input("Based on these facts, what marine mammal do you think it is?: ")
            if (val == "polar bear") or (val == "Polar bear") or (val == "Polar Bear"):
                print("Correct! The animal is a polar bear!")
                count += 1
                print("\n")

            else:
                print("That is incorrect, The animal is a polar bear!")
                print("\n")


def whale():
    print("Fact 1: This marine mammal 'sings' songs that can be heard up to 20 minutes away")
    print("Fact 2: This marine mammal breathes through a blowhole")
    global count
    print("\n")

    val = input("Based on these facts, what marine mammal do you think it is?: ")
    if (val == "whale") or (val == "Whale"):
        print("Correct! The animal is a whale!")
        count += 1
        print("\n")

    else:
        print("That is incorrect, I will give you another fact and you can try again.")
        print("Fact 3: This marine mammal is the largest animal in the world")
        val = input("Based on these facts, what marine mammal do you think it is?: ")
        if (val == "whale") or (val == "Whale"):
            print("Correct! The animal is a whale!")
            count += 1
            print("\n")

        else:
            print("That is incorrect, here is one more fact")
            print("Fact 4: They eat using hundreds of baleen plates that overlap each other and strain out sea water and keep prey")
            val = input("Based on these facts, what marine mammal do you think it is?: ")
            if (val == "whale") or (val == "Whale"):
                print("Correct! The animal is a whale!")
                count += 1
                print("\n")

            else:
                print("That is incorrect, The animal is a whale!")
                print("\n")


def sea_otter():
    print("Fact 1: This marine mammal has the thickest fur of any animal")
    print("Fact 2: This marine mammal uses rocks to consume thier diet which consists of sea urchins, crabs, mussels, and clams ")
    global count
    print("\n")

    val = input("Based on these facts, what marine mammal do you think it is?: ")
    if (val == "sea otter") or (val == "Sea otter") or (val == "Sea Otter"):
        print("Correct! The animal is a sea otter!")
        count += 1
        print("\n")

    else:
        print("That is incorrect, I will give you another fact and you can try again.")
        print("Fact 3: This marine mammal is a keystone species in its environment")
        val = input("Based on these facts, what marine mammal do you think it is?: ")
        if (val == "sea otter") or (val == "Sea otter") or (val == "Sea Otter"):
            print("Correct! The animal is a sea otter!")
            count += 1
            print("\n")

        else:
            print("That is incorrect, here is one more fact")
            print("Fact 4: These marine mammals often sleep holding hands as to not drift away from each other")
            val = input("Based on these facts, what marine mammal do you think it is?: ")
            if (val == "sea otter") or (val == "Sea otter") or (val == "Sea Otter"):
                print("Correct! The animal is a sea otter!")
                count += 1
                print("\n")

            else:
                print("That is incorrect, The animal is a sea otter!")
                print("\n")


def manatee():
    print("Fact 1: These marine mammals are bottom grazers and eat sea grass and algae")
    print("Fact 2: These marine mammals live in warmer water because they have a low metabolism")
    global count
    print("\n")

    val = input("Based on these facts, what marine mammal do you think it is?: ")
    if (val == "manatee") or (val == "Manatee"):
        print("Correct! The animal is a manatee!")
        count += 1
        print("\n")

    else:
        print("That is incorrect, I will give you another fact and you can try again.")
        print("Fact 3: This animal has been nicknamed the 'sea cow'")
        val = input("Based on these facts, what marine mammal do you think it is?: ")
        if (val == "manatee") or (val == "Manatee"):
            print("Correct! The animal is a manatee!")
            count += 1
            print("\n")

        else:
            print("That is incorrect, here is one more fact")
            print("Fact 4: This marine mammal has a tail shaped like a paddle")
            val = input("Based on these facts, what marine mammal do you think it is?: ")
            if (val == "manatee") or (val == "Manatee"):
                print("Correct! The animal is a manatee!")
                count += 1
                print("\n")

            else:
                print("That is incorrect, The animal is a manatee!")
                print("\n")


def sea_lion():
    print("Fact 1: Their streamlined bodies help them chase fish and squid")
    print("Fact 2: Some species of this marine mammal have external ear flaps")
    global count
    print("\n")

    val = input("Based on these facts, what marine mammal do you think it is?: ")
    if (val == "sea lion") or (val == "Sea lion") or (val == "Sea Lion"):
        print("Correct! The animal is a sea lion!")
        count += 1
        print("\n")

    else:
        print("That is incorrect, I will give you another fact and you can try again.")
        print("Fact 3: They get their name for their loud and distinct 'roar")
        val = input("Based on these facts, what marine mammal do you think it is?: ")
        if (val == "sea lion") or (val == "Sea lion") or (val == "Sea Lion"):
            print("Correct! The animal is a sea lion!")
            count += 1
            print("\n")

        else:
            print("That is incorrect, here is one more fact")
            print("Fact 4: The females give birth to one pup per year")
            val = input("Based on these facts, what marine mammal do you think it is?: ")
            if (val == "sea lion") or (val == "Sea lion") or (val == "Sea Lion"):
                print("Correct! The animal is a sea lion!")
                count += 1
                print("\n")

            else:
                print("That is incorrect, The animal is a sea lion!")
                print("\n")


def main():
    global count
    hello()
    walrus()
    print("New Animal!")
    dolphin()
    print("New Animal!")
    sea_otter()
    print("New Animal!")
    sea_lion()
    print("New Animal!")
    manatee()
    print("New Animal!")
    whale()
    print("New Animal!")
    polar_bear()
    print("You have completed the game. You had ", count, " correct answers. Thanks for playing!")
    if count == 7:
        print("You got all of them correct! Congrats!")

if __name__ == '__main__':
    main()