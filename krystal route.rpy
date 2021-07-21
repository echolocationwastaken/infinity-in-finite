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
            $ krystal_a += 2
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

    hide krystal happy

    "before you can object, she disappears back into the shelves."
    "you are compelled to follow."

    scene art store shelves

    show krystal happy

    k "ok so here's the thing:"
    k "everything here is damn expensive."
    k "but i still go here cos everything is also damn cool."

    "she continues down the aisle, fingertips brushing against the shelves."

    "she suddenly stops and you almost bump into her."

    "her eyes are lit up and a steady grin spreads across her face."

    "she reaches for a box of watercolor paint. she holds it up for you to see."

    pov "winsor & newton water colors...?"

    "her grin turns into a wide smile."

    k "these watercolors? IMMACULATE"

    k "they are literally SO PRETTY"

    k "the high pigment transparency is sooo hot ughhhhhh"

    k "it's the best consistency. if you want watercolors, you should totally get these."

    menu:
        "buy the watercolors":
            $ krystal_a += 1
            jump buywatercolors

        "don't buy the watercolors":
            jump dontbuywatercolors

    return

label buywatercolors:
    pov "i think i'll get these."
    k "omg yay! thanks for taking my reccomendation."
    jump oilpaints

label dontbuywatercolors:
    pov "hmmm these are nice but i think i'll pass."
    k "awww alright"
    jump oilpaints

label oilpaints:
    pov "what else would you recommend?"
    k "uhhh...lemme think"

    hide krystal happy

    "she begins to drift through the shelves again."
    "as you follow her, you inhale the scent of the art store. it smells like a combination of wood, glue, paint, and more."
    "you can't quite place the name of the scent, but it smells good."

    scene art store shelves 2

    "suddenly, she stops. she gestures to a set of paints on the shelf."

    show krystal happy
    k "ok, so these are winsor newton oil paints. they are sexy too!"
    k "unfortunately they're hella expensive, so i never go to try them."
    k "right now i'm using blick brand oil paints, which are for beginners"
    k "cuz I still haven't used it up ahaha (it’s super hard to waste oil paint it just never dries lmfao so you can just keep using it)"

    "you can see the longing in her eyes as she stares at the expensive oil paints."

    menu:
        "buy the expensive oil paints for krystal":
            $ krystal_a += 5
            jump buyforkrsy

        "buy the expensive oil paints for yourself":
            $ krystal_a += 1
            jump buyforself

        "don't buy the expensive oil paints":
            jump dontbuyoilpaints
    return

label buyforkrsy:
    pov "i'll buy them for you."
    k "WHAT"
    "she starts shaking"
    k "t-this isn't some sort of twisted joke right?"
    pov "of course not."
    pov "i want you to try them out."
    pov "i wouldn't mind buying them for you."
    show krystal blush
    k "OMG THANK YOU"
    "she wraps you in a bear hug."
    k "THANK YOU THANK YOU THANK YOU"
    pov "ah, i-it's getting hard breathe--"
    k "LSKDJF SORRY SORRY i got too excited"
    pov "nono don't worry i liked it"
    "she pulls away, and you notice that her eyes are wet."
    pov "are you crying???"
    k "ahaha sorry, i'm getting emotional over LITERALLY nothing."
    k "thank you so much again"
    pov "of course"
    show krystal happy

    jump cafeornah

label buyforself:
    pov "i think i'm going to buy these"
    k "ayeee! nice!"
    k "lemme know how you like them."
    "she hands you the oil paints, but she hesitates before giving them to you."
    "the longing lingers in her eyes."

    jump cafeornah

label dontbuyoilpaints:
    pov "hmm, they look nice but i don't think i'll buy them."
    k "aaah, yeayea i understand"
    k "sorry for fangirling so much over paints ahaha. i get too excited over these things."
    pov "nono you don't have to worry about it. especially not with me."
    "she beams at you."
    $ krystal_a += 1
    k "thanks!"

    jump cafeornah

label cafeornah:
    k "oops, we already spent an hour in here ahaha"
    k "we should probably go."
    pov "w-wait. i still wanna hang out with you more."
    "she smiles"
    k "alright, there's a cafe next door called \"eating paint.\" wanna check it out with me? we can even do art together!!"
    menu:
        "go to the cafe":
            $ krystal_a += 5
            jump cafe

        "head home for the day":
            jump gohome
    return

label cafe:
    scene street
    hide krystal happy
    "both of you head next door to the cafe."
    play sound "audio/cafe_bgm.mp3" volume 0.3
    scene cafe seat
    show krystal sit
    "she picks a table, and you settle into the seat across from her."
    "she takes out her sketchbook and you follow suit."
    pov "oh no, i just realized. i didn't bring any paper or pencil."
    k "ahh, it's alright. i'll lend you some of my supplies."
    "she hands you a piece of paper and a few pencils."
    pov "thanks!"
    k "you're welcome!"
    show krystal sit smile
    "she smiles, and begins sketching. so do you."

    show krystal sit
    "the hours fly by. you lose track of time as you immerse yourself in your work."

    "before you know it, the cafe is closing for the night, and a twinge of disapointment brushes against your heart."

    pov "ah, it looks like it's time to leave."

    pov "will i be able to see you again?"

    k "sure! i'm always at the art shop, so you can find me here."

    k "but before you go, i want to know"

    k "what did you draw?"

    menu:
        "rabbit":
            jump showdrawing

        "deer":
            jump showdrawing

        "you":
            $drawing = "you"
            $krystal_a += 5
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

    "you feel as if you can't breathe."

    "your heart shivers. your drawing in her hand trembles with the breeze."

    if drawing == "you":
        jump drawingyou
    else:
        jump drawingelse

label drawingyou:
    k "oh..."
    k "wow"
    k "[povname], i don't even know what to say"
    pov "do you like it?"
    show krystal sit smile
    k "i love it!!!!"
    "{i}relief{/i}"
    k "i  literally love how you used like the colors. it's beautiful."
    k "and the cross hatching and shading omg <3"
    k "you drew me so well!!"
    k "thnak :)"
    jump krystaldrawing

label drawingelse:
    k "oh..."
    k "wow"
    pov "do you like it?"
    show krystal sit smile
    k "of course!!!!"
    "{i}relief{/i}"
    k "it looks really good!"
    jump krystaldrawing

label doesntshow:
    pov "i'd rather not"
    k "oh...alright! that's fine"
    "you notice she looks disappointed."
    jump krystaldrawing

label krystaldrawing:
    show krystal sit
    pov "krystal, what did you draw?"
    "she hands you her sketchbook..."
    "it's a sketch of a boy."
    k "ok so heres the thing:"
    k "can i vent to you about something real quick?"
    menu:
        "yes":
            $krystal_a += 2
            jump vent

        "no":
            jump novent

    return

label vent:
    k "aaaah thank you so much!"
    k "so"
    k "this little shit head is stupid but i still like him for some reason."
    k "i dont even know why i drew him god ew"
    k "he only wears fckin highlighter colors!!!"
    k "he's boring and lame and it's just so {i}tiring{/i} to talk to him."
    k "it's just so stressful."
    "..."
    pov "krystal, i'm so sorry that you have to go through this."
    pov "from what i can tell, this relationship you have with him is toxic."
    pov "and you probably would be better without him."
    pov "give yourself some space."
    "she sighs."
    k "you're right."
    "she sniffles, then laughs."
    show krystal sit smile
    k "you're right!"
    "she takes the drawing she had been working on, and rips it into little shreds."
    k "there! wow, i feel a lot better now"
    pov "you don't need to talk to this guy anymore."
    pov "not even if you feel lonely."
    pov "because i'll always be here for you."
    k "thank you,"
    k "so much"
    k "aha plsss, i think imma get all emotional again"
    pov "ahaha let's pick up these paper shreds first."
    k "ah! i forgor"
    "both of you work together to clean up all the scraps"
    "when you're finally done, she wraps you in a hug."
    k "thanks"
    pov "of course"
    scene street
    stop sound
    play music "audio/kyoto_bgm.mp3"
    "you say goodbye, and you head home."
    "as you head back, her name swirls in your head: krystal."
    return


label novent:
    pov "sorry, but i don't think i'm comfortable with that"
    k "ahhh, it's alright. sorry, i'm not sure how to explain who he is without getting mad."
    pov "that's fine. i guess i'll head home for the day. see you tomorrow?"
    k "see ya!"
    scene street
    stop sound
    play music "audio/kyoto_bgm.mp3"
    "you head home, her name swirling in your head: krystal."
    return

label gohome:
    pov "nah,,,i think i'll call it a day."
    pov "will i be able to see you again?"
    k "sure! i'm always at the art shop, so you can find me here."
    k "cya!"
    pov "bye!"
    scene street
    stop sound
    play music "audio/kyoto_bgm.mp3"
    "you head home, her name swirling in your head: krystal."
    return
