# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label home:

    scene anime bedroom

    "you decide to go home, but there's nothing to do at home."
    "you finish your homework and go to sleep."
    "you are bored, sad, and above all, alone. maybe you should've gone somewhere..."

    scene black
    "slowly, you start to drift off."

    scene anime bedroom
    play sound "audio/crash.mp3"
    "you wake up with a startle."
    pov "ah! who's there!?"
    play music "audio/"
    show echo dizzy
    e "calm down calm down! it's just me!"
    pov "why are you here?!?!"
    pov "get out of my house!"
    show echo happy
    e "i'm god! i can go wherever i want!"
    pov "arghh!"
    pov "what was that sound??"
    e "ehe"
    pov "..."
    e "ok fine. i accidentally crashed into your desk. all of your textbooks fell down."
    pov "hey!"
    e "what do you need that many textbooks for anyway? nerd"
    pov "shut up."
    e "no."
    pov "..."
    e "..."
    menu:
        "what do you want to ask?"

        "how did you even crash into my desk in the first place?":
            $howcrash = True
            jump howcrash

        "can you leave i just want to sleep":
            jump plsleave

    return

label howcrash:
    pov "how did you even crash into my desk in the first place?"

    jump unfinished

label plsleave:
    e "i'd rather not."
    e "sleep is for the weak."
    menu:
        "what do you want to ask?"
        "how did you even crash into my desk in the first place?" if howcrash == False:
            jump howcrash
    return

return
