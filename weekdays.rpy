# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label weekday:

    scene black

#    index = 0
#    while index < 7:
#        label weekdays[index]:
#            "today is" + weekdays[index] + "remember to save your game! :) <3"
#        jump school
#        index += 1

    call total_visits from _call_total_visits
    if monday == True:
        jump monday

    call total_visits from _call_total_visits_1
    if tuesday == True:
        jump tuesday

    call total_visits from _call_total_visits_2
    if wednesday == True:
        jump wednesday

    call total_visits from _call_total_visits_3
    if thursday == True:
        jump thursday

    call total_visits from _call_total_visits_4
    if friday == True:
        jump friday

    call total_visits from _call_total_visits_5
    if saturday == True:
        jump saturday

    call total_visits from _call_total_visits_6
    if sunday == True:
        jump sunday

label monday:
    "today is monday. remember to save your game! :) <3"
    jump school

label tuesday:
    "today is tuesday. remember to save your game! :D <3"
    jump school

label wednesday:
    "today is wednesday. remember to save your game! :) <3"
    jump school

label thursday:
    "today is thursday. remember to save your game! :) <3"
    jump school

label friday:
    "today is friday. remember to save your game! :D <3"
    jump school

label saturday:
    "today is saturday. remember to save your game! :) <3"
    jump dates

label sunday:
    "today is sunday. remember to save your game! :) <3"
    jump dates

label school:
    scene school hallway

    "you go to school. it's horribly uneventful. all your classes are boring
     and you spend the entire time taking notes."

    "finally, school is over. free at last"

    call total_visits from _call_total_visits_7

    if totalv == 0:
        jump firstday
    else:
        jump where

label firstday:
    "you feel proud for making it through the first day. then you realize you
    haven't made a single friend."

    show echo happy

    e "heyo! didja know u can meet new people by going to different places? and maybe u
    can make a friend or two!"

    pov "how did know what i was thinking"

    e "shut"

    hide echo

    jump where

label where:
    menu:
        e "where do you wanna go?"

        "{color=#f00}The Business Room{/color}":
            $ markv += 1
            jump unfinished

        "soccer field":
            $ jackv += 1
            jump unfinished

        "dick blick art store":
            $ krystalv += 1
            jump artstore

        "ymca (or was it the ywca...)":
            $ wilsonv += 1
            jump unfinished

        "gym":
            $ conniev += 1
            jump unfinished

        "go home":
            $ echov += 1
            jump home

label dates:
    jump unfinished

label unfinished:
    show echo happy
    e "sorry, but i havent finished this yet!"
return
