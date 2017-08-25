start = '''
You have two weeks off of work so you decide to go on vacation. But you're having trouble deciding where to go.

'''

lame_end = '''
You have an amazing yet uneventful vacation.
'''

poor_end = '''
You have no money or any way of getting home. You are now homeless on the windy streets of Chicago.
'''

print(start)


print("Type 'Barcelona' to go to Barcelona, 'Chigaco' to go to Chigaco, or 'Fiji' to go to Fiji.")
location = input()
if location == "Barcelona":
    print("You're exploring the streets of Barcelona when a man approaches you. Should you talk to the man or walk away?")
    print ("Type 'talk'to talk to the man or 'walk' to walk away.")
    twa = input()

    if twa == "talk":
        print("The man offers you and interesting proposition. If you give him $500, you will get a superpower.")
        print("Type 'pay' to give him the $500 or type 'no thanks' to decline the offer.")

        offer = input()
        if offer == "pay":
            print("Type 'fly' to get the superpower of flying or type 'read minds' to read minds.")

            power1 = input()
            if power1 == "fly":
                print("You go to the top of a building to test your new superpower. You jump off the building but your power doesnt work! You safely land in a bullpen. You fend off against the bulls so well that you end up becoming a famous matador!")
                print ("THE END")

            elif power1 == "read minds":
                print("You sucessfully read else's mind but because you're in Spain. their thoughts are in Spanish. You don't speak Spanish so your superpower is useless.")
                print("THE END")

        elif offer == "no thanks":
            print(lame_end)
            print("THE END")

    elif twa == "walk":
        print(lame_end)
        print("THE END")






elif location == "Chicago":
    print("You're exploring the streets of Chigaco when a man approaches you Should you talk to the man or walk away?")
    print ("Type 'talk'to talk to the man or 'walk' to walk away.")

    twa2 = input()
    if twa2 == "talk":
        print("The man offers you and interesting proposition. If you give him $500, you will get a superpower.")
        print("Type 'pay' to give him the $500 or type 'no thanks' to decline the offer.")

        offer_two = input()
        if offer_two == "pay":
            print("Type 'telekinesis to get the superpower of telekinesis or type 'strength' to get super stength.")

            power2 = input()
            if power2 == "telekinesis":
                print("You walk to a public area and challenge someone to a bet. You bet that you can lift a deep dish pizza with your mind.")
                print("Type 'a lot' to bet all of your money or 'a little' to only bet a little.")

                bet = input()
                if bet == "a lot":
                    print("The man scammed you and you dont have a new superpower. Not only did you lose $500, you also lost the rest of your money.")
                    priny(poor_end)

                elif bet == " a little":
                    print("Your sucessfully lift the pizza. You decide to invest your money in a startup company and become super rich.")
                    print("THE END")

            elif power2 == "strength":
                print("You ecounter a robber and he steals your wallet!")
                print("Type 'fight' to get your wallet back or 'flee' to run away.")

                wallet = input()
                if wallet == "fight":
                    print("You get your wallet back and then you become a well known crime stopper on the streets of Chicago.")
                    print("THE END")

                elif wallet == "flee":
                    print(poor_end)

        elif offer_two == "no thanks":
            print(lame_end)
            print("THE END")

    elif twa2 == "walk":
        print(lame_end)
        print("THE END")

elif location == "Fiji":
    print("You arrive on the island of Fiji and decide to swim with dolphins. Suddenly a dolphin that talks swims up to you.")
    print("Type 'swim' to swim away from the dolphin or 'chat' to talk to the dolphin.")

    dolph = input()
    if dolph == "swim":
        print(lame_end)
        print("THE END")

    elif dolph == "chat":
        print("The dolphin asks for 10 fish in exchange for giving you a superpowerself.")
        print("Type 'fish' to feed the dolphin fish or 'leave' to swim away.")

        food = input()
        if food == "fish":
            print("Type 'animals' to get the power to talk to animals or 'shapeshift' to get the power of shapeshifting.")

            power3 = input()
            if power3 == "animals":
                print ("You are able to talk to animals, but all onlookers think you are insane so they leave you on a stranded island.")
                print("THE END")

            elif power3 == "shapeshift":
                print("Although you are able to shapeshift, you are only able to turn into a mongoose. Because of this, you live the remainder of your life as a mongoose.")
                print ("THE END")

        elif food == "leave":
            print(lame_end)



else:
    print("try again")
