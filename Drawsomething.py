# coding=utf-8
def a4cdecision():
    q = int(raw_input("You want to do .... \n1. fight him \n2.keep pretending"))
    if q == 1:
        raw_input("you jump on him and punches him as hard as you can ")
        raw_input(" he knocks you back")
        raw_input("Uh...")
        raw_input("the alien is way stronger than you ")
        raw_input("you picked up your pocket knife and stabbed the alien's eyes")
        raw_input("the aliens screams wildly, he is mad now")
        raw_input("he chokes you ")
        raw_input("You stab him again on the side of his head")
        raw_input("the alien died. THE END")
    if q == 2:
        raw_input("he steps inside the room.")
        raw_input("he checks around if there is anything living")
        raw_input("he walks to you")
        raw_input("you thought he is gonna kill you")
        raw_input("he didn't see you")
        raw_input("he walks out of the room and leaves")
        raw_input("You open your eyes and gasp heavily")
        raw_input("you are temporarily safe. THE END")


def a4ddecision():
    p = int(raw_input("You want to... \n1. pinch yourself as hard as you can \n2. Find out what is wrong with this town"))
    if p == 1:
        raw_input("You pinched yourself as hard as you can")
        raw_input("You feel some one calling you ")
        raw_input('"Wake up! Wake up!! It is time to wake up!" It is your mom.')
        raw_input("You open your eyes, staring at the ceiling and sigh.")
        raw_input("you hugged your mom and was happy that this was only a dream. THE END")
    if p == 2:
        raw_input("you want to know what is going on")
        raw_input("you walk along time ")
        raw_input("you walked to the end of this town")
        raw_input("you realize there is a barrier that is covering this town")
        raw_input("You hit the barrier as hard as you can")
        raw_input("the barrier breaks in pieces")
        raw_input("You open your eyes and realize the shocking fact that this is the science experiment that the government had made, THE END")


def dd4():
    z = int(raw_input("You want to ... \n 1. you walk to the living room to check \n2. stay inside the room"))
    if z == 1:
        raw_input("you open your bedroom door to check if the alien is gone or not")
        raw_input("sounds like the alien is gone")
        raw_input("you sigh and look down")
        raw_input("dot dot dot ")
        raw_input("water drops from the ceiling ")
        raw_input("you lookup ")
        raw_input("alien is on the ceiling and he eats you alive. THE END")
        if z == 2:
            raw_input("you stay inside the room")
            raw_input("sounds like the alien is gone")
            raw_input("then peak your head to check")
            raw_input("ahh! ")
            raw_input("the alien eats your head. THE END ")


def a4adecision():
    x = int(raw_input("You want to ... \n1. suspect if there is anything wrong with Bob because usually he does not let you go into his house \n2. go inside the house "))
    if x == 1:

        raw_input("u step back")
        raw_input("asks if Bob is ok")
        raw_input("he didn't reply, but only smiles at you strangely")
        raw_input("Bob is already brainwashed by the aliens but you don't know")
        raw_input("Bob are you ok?")
        raw_input("he still didn't reply")
        raw_input("AH! ")
        raw_input("he shocks you with his weapon")
        raw_input("THE END")

    if x == 2:
        raw_input("He lead you to sit on his sofa ")
        raw_input("he hands you a cup of tea ")
        raw_input("you drink the tea")
        raw_input("you gradually feel very dizzy, and sees Bob transform into an alien")
        raw_input("You suddenly close your eyes. THE END")


def a3bdecision():
    j = int(raw_input("You want to... \n1. pretend sleeping \n2. stand up to see what is going on"))
    if j == 1:
        raw_input("you pretend to be sleeping")
        raw_input("the aliens walks around the house to see if there are anything else living. he opens your room door")
        a4cdecision()
    if j == 2:
        raw_input("You stand up")
        raw_input("suddenly the sound of the alien is gone")
        dd4()


def a3adecision():
    e = int(raw_input("You want to do .... \n1. go to take a look  \n2.ignore and keep searching for food"))
    if e == 1:
        raw_input("you walk to the house and knock on the door")
        raw_input("the lights are turned off inside the house ")
        raw_input("someone opens the door")
        raw_input("it is your friend Bob and he welcomes you to his house weirdly")
        a4adecision()

    if e == 2:
        raw_input("you ignore the house and keeps walking")
        raw_input("you realize everyone in the town is gone, something must be wrong. you think this must be a dream")
        a4ddecision()


def asecond_decision():
    d = int(raw_input("What would you want to do? \n1.go out to search for food \n2. scream for help"))
    if d == 1:
        raw_input("you stand up and go out of the house.")
        raw_input("you open the door and realize that your town has been bombed by aliens, however there is one house that stayed in good shape")
        a3adecision()
    elif d == 2:
        raw_input("You start yelling for help.")
        raw_input(" you heard something moving, so you strech your head to check what going on. An alien steps into your living room")
        a3bdecision()

def first_decision():
    c = int(raw_input("What do you want to do? \n1. Sit on the floor and cry \n2. Try to find if anyone else in the town is still alive"))
    if c == 1:
        raw_input("You sit down on your broken bed and start crying.")
        raw_input("After a while you got hungry ")
        raw_input("you look around your house to search for food")
        raw_input("you are very hungry now but you can't find anything to eat")
        asecond_decision()
    else:
        if c == 2:
            raw_input("You stand up and open you half-broken door")
            raw_input("You find out that every house was ruined ")
            raw_input("You start calling out your friend Bob and see if he is still alive")
            raw_input("you yelled his name in front of his house but no one responds, suddenly you heard a machine sound, you realize it might be from the alien's battleship")
            QQ_1()

def QQ_1():
    a = int(raw_input("you can… \n1 Hide under a bush \n2 continue searching for your friend "))
    if a == 1:
        raw_input("You look around, find our that there is a bush that you can hide")
        raw_input("you jump in that bush and watch what the aliens are doing")
        a_1()
    else:
        if a == 2:
            raw_input("you walk as if nothing happened ")
            raw_input("The aliens did not see you and they drove right past you")
            a_2()
        else:
            raw_input("Please type either 1 or 2, otherwise you will start from the top.")


def a_1():
    raw_input("They are in human shape and looks exactly like your town's people")
    b = int(raw_input("\n1.  you jump out of the bush and waved  \n2.keep hiding"))
    if b == 1:
        raw_input("you are yelling their names but they are not responding as they used to be")
        b_1()
    else:
        if b == 2:
            raw_input("You listen carefully to what they are talking about but you realize you cannot understand")
            b_2()
        else:
            raw_input("Please type either 1 or 2, otherwise you will start from the top.")


def b_1():
    raw_input(
        "they heard your voice and turned their head to you")
    j = int(raw_input(
        "now you have two decision: \n1. walk to them \n2. realize something is wrong and keep a safe distance between them ' "))
    if j == 1:
        raw_input(
            "they didn't say a single word and immediately beats you to the ground.")
        j_1()
    else:
        if j == 2:
            raw_input("you realize they are looking at you very strangely you begin to step back")
            j_2()
        else:
            raw_input("Please type either 1 or 2, otherwise you will start from the top.")


def j_1():
    p = raw_input("you can now decided \n1. you are all confused, you fought back and grabbed one of the alien's gun \n2. you don't know whats going on and starts yelling")
    if p == 1:
        p_1()
    else:
        if p == 2:
            p_2()
        else:
            raw_input("Please type either 1 or 2, otherwise you will start from the top.")


def p_1():
    raw_input(
        "you shot the two aliens and drove their space ship to furthur discover what happened to your town. THE END")


def p_2():
    raw_input("You are handcuffed and brought to the alien spaceship for human anatomy. THE END")


def j_2():
    raw_input("you backed up from them ")
    w = int(raw_input("you can decided \n1. run away \n2.Yelled: try to talk to them"))
    if w == 1:
        raw_input("they are very fast, they immediately catches you and kills you. THE END.")
    else:
        if w == 2:
            raw_input("they seem like they don't understand you. They stare at you calmly, and then suddenly you feel dizzy and lose your consciousness. THE END ")
        else:
            raw_input("Please type either 1 or 2, otherwise you will start from the top.")


def b_2():
    raw_input(
        "you listen to their conversation carefully ")
    qq = int(raw_input("you can decide \n1. keep listening   \n2. away "))
    if qq == 1:
        raw_input("they realize someone is nearby, they found you and kills you. THE END.")

    else:
        if qq == 2:
            raw_input("you ran away without making the aliens notice, but you got lost .THE END.")
        else:
            raw_input("Please type either 1 or 2, otherwise you will start from the top.")


def a_2():
    raw_input("you are very lucky, the aliens did not see you, but you feel very hungry  ")
    f = int(raw_input("you can decide \n1. go in your room  \n2. go to find something to eat "))
    if f == 1:
        raw_input("you fear that the alien might come back so you stay inside your room")
        f_1()
    else:
        if f == 2:
            raw_input("you are too hungry, you really want to eat something ")
            f_2()
        else:
            raw_input("Please type either 1 or 2, otherwise you will start from the top.")


def f_1():
    raw_input("suddenly you sea a bag of chips in your room")
    i = int(raw_input("you can choose to.. \n1. do not eat it \n2. eat "))
    if i == 1:
        i_1()
    else:
        if i == 2:
            i_2()
        else:
            raw_input("Please type either 1 or 2, otherwise you will start from the top.")


def i_1():
    raw_input("You choose not to eat it. You eventually starve to death. THE END.")


def i_2():
    raw_input("you choose to eat the bag of chips. But you didn't see the expiration date. It is already expired. You died. THE END ")


def f_2():
    raw_input(
        "you want to find food")
    u = int(raw_input("and now there are two choices: \n1. check if there is anthing left in the house \n2. go outside for food"))


    if u == 1:
        raw_input("you search around the house, but there weren't any food left. However, you encoutered an alien, you became the food.THE END.")

    else:
        if u == 2:
            raw_input("you go outside, and got lost. THE END.")
        else:
            raw_input("Please type either 1 or 2, otherwise you will start from the top.")



def main():
    raw_input("    TITLE : ALIEN  MAZE  123 ")
    raw_input('*** BEFORE YOU START *** Please hit "ok" if there is text only. Otherwise, enter a number when making your choices. ')
    raw_input("you wake up and found your house becomes destroyed, you call for your parents, but they are not answering, you realized that the aliens had bomb your city again ")
    first_decision()


main()