# The script of the game goes in this file.

# The game starts here.

label total_visits:
    #to count total visits
    #use this to call total visits
        #call total_visits

    $ totalv = echov + markv + krystalv + jackv + wilsonv + conniev
    return


label start:
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("echo (aka god)")
define pov = Character("[povname]")
define ml = Character(_("Mark Leschinsky"), color="#ff1100")
define k = Character("krystal")
define j = Character("jack pada")
define c = Character("connie")
define unknown = Character("???")

#number of visits defined

default echov = 0
default markv = 0
default krystalv = 0
default jackv = 0
default wilsonv = 0
default conniev = 0
default totalv = 0

#find total visits at the top of this file

#affection levels defined

default echo_a = 0
default mark_a = 0
default krystal_a = 0
default jack_a = 0
default wilson_a = 0
default connie_a = 0

#creating the weekdays
#weekdays = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]
#index = 0
#while index < 7:
#    call total visits from "_call_total_visits" + str(index+8)
#    if totalv%7 == index:
#        "8" + weekdays[index] = true
#    index+=1

default monday = False
default tuesday = False
default wednesday = False
default thursday = False
default friday = False
default saturday = False
default sunday = False

call total_visits from _call_total_visits_8
if totalv % 7 == 0:
    $monday = True

call total_visits from _call_total_visits_9
if totalv % 7 == 1:
    $tuesday = True

call total_visits from _call_total_visits_10
if totalv % 7 == 2:
    $wednesday = True

call total_visits from _call_total_visits_11
if totalv % 7 == 3:
    $thursday = True

call total_visits from _call_total_visits_12
if totalv % 7 == 4:
    $friday = True

call total_visits from _call_total_visits_13
if totalv % 7 == 5:
    $saturday = True

call total_visits from _call_total_visits_14
if totalv % 7 == 6:
    $sunday = True

label naming:

    #choosing a name

    python:
        povname = renpy.input("what's your name?", length=32)
        povname = povname.strip()

        if not povname:
            povname = "xXX_pl4y3r_XXx"

    pov "your name has been set to [povname]!"

label wake:

    play music "audio/morning_flower.mp3" fadeout 1.0 fadein 1.0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene anime bedroom

    # These display lines of dialogue.

    "it's daylight outside. you should prolly wake up."

    pov "hmlkajsdfpppphrmhmmmm,,,don't wanna"

    pov "who even are you"

    show echo happy

    e "my name's echo, aka god. i'm telling you to wake up directly from the
    pixelated heavens."

    e "today's also the first day at your new school, BCA, so wake up."

    pov "bbbbbrrrrmkaaffnnllll die pls"

    $ goddead = False
    $ dead = False


    menu:
        "what do you do"

        "god is dead":

            jump godisdead

        "death":

            jump death

        "wake up and go to school":

            jump endofthebeginning

label godisdead:
    $ goddead = True
    e "mothersucker you can't kill me"

    menu:
        "what do you do"

        "death" if dead == False:
            jump death

        "wake up and go to school":

            jump endofthebeginning

label death:
    $ dead = True
    show echo sad
    e "..."
    e "suicide isn't poggers yknow"
    show echo happy
    menu:
        e "try again :)"

        "god is dead" if goddead == False:
            jump godisdead

        "wake up and go to school":

            jump endofthebeginning


label endofthebeginning:
    pov "fine i'll wake up."

    e "yay!"

    hide echo happy

    "bedgrudgingly, you start getting ready."

    "..."

    "your infinity begins now!"

    play music "audio/kyoto_bgm.mp3" fadeout 1.0 fadein 1.0

    jump weekday

    # This ends the game.

    return
