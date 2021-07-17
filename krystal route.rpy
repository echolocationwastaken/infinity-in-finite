# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label artstore:

    scene street

    "you decide to go to the art store!"

    "you're not exactly sure what you want to do there, but the ~unique~ name caught your eye."

    "figured that you might as well check it out..."

    scene art store
    play sound "audio/door_chime.mp3"

    "you enter the shop, the chime of a bell welcoming you inside."

    "the shop is small, but it's cozy and welcoming."

    "light pours in from the windows, basking everything in a surreal warm yellow glow."

    "the light happens to fall on a girl emerging from the shelves of art supplies."

    show krystal happy
    play music "audio/will_he.mp3" fadeout 1.0 fadein 1.0
    unknown "hi! i haven't seen you around here before!"

    pov "{i}woah...{/i}"

    menu:
        "introduce yourself":
            jump intro

        "omg it's a pretty girl i have to make a dick joke":
            $ krystal_a += 1
            jump joke

    return

label intro:
    pov "hi! my name's [povname]."
    pov "i'm new here and decided to check out the art store."

    jump introkrsy

label joke:
    pov "u havent seen me before but i can show you my (dick) blick"

    "to your suprise, she starts bursting in laughter."

    "her smile is so bright that you can't help but laugh as well."

    unknown "pfffFT"

    unknown "ALKDJFSLKDF PLS-"

    "she manages to finally catch her breath."

    unknown "you're funny! what's your name?"

    pov "my name's [povname]! i'm new here and decided to check out the art store."

    "she smiles again, and your heart melts."

    jump introkrsy

label introkrsy:
    unknown "my name's krystal. it's nice to meet you!"

    k "here, let me show you around the art store."

    "before you can object, she disappears back into the shelves."
    "you are compelled to follow."

    k "ok so here's the thing:"
    k "everything here is damn expensive."
    k "but i still go here cos everything is also damn cool."

    "she continues down the aisle, fingertips brushing against the shelves."

    "lol i havent finished this"

label shopclose:

    "the hours fly by."

    "the shop is closing for the night, and a twinge of disapointment brushes against your heart."

    pov "ah, it looks like it's time to leave."

    pov "will i be able to see you again?"

    k "sure! i'm always at the art shop, so you can find me here."

    k "but before you go, i want to know"

    k "what did you draw?"

    menu:
        "rabbit":
            $drawing = "rabbit"
            jump showdrawing

        "deer":
            $drawing = "deer"
            jump showdrawing

        "you":
            $drawing = "you"
            jump showdrawing

    return

label showdrawing:
    k "can you show me it?"
    menu:
        "yes":
            $krystal_a += 2
            jump doesshow

        "no":
            $krystal_a -= 1
            jump doesntshow

    return

label doesshow:
    pov "sure"

    "your hand trembles as you hand her the paper."

    pov "{i}what if she thinks it's ugly?{/i}"

    pov "{i}what if she doesn't like it? what if she hates it?{/i}"

    pov "{i}and by extension- {b}me{/b}?{/i}"

    "your breath is caught in your ribcage."

    "your heart shivers. your drawing in her hand trembles with the breeze."

label doesntshow:

label akldsf:

    return
