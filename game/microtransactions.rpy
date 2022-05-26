
label Microtransactions_Intro:
    "You are getting a pulse that feels like Xavier calling."
    ch_x "Could you come to my office please?"
    menu:
        extend ""
        "Ok" if not Party and not Present:
            $ Party = []
            "You head over."
        "I should go for this." if Party or Present:
            $ Party = []
            "You excuse yourself and head out."
        "Nah.":

            ch_x "-Now,- [Player.name]!"
            if Party or Present:
                $ Party = []
                "You excuse yourself and head out."
            else:
                "You head over."
    show black_screen onlayer black
    pause 0.1
    $ round -= 5
    $ bg_current = "bg_study"
    call change_Xavier_face ("_happy")
    call set_the_scene
    hide black_screen onlayer black
    ch_x "[Player.name], I'm glad you came to see me."
    ch_x "I have a problem that I believe you could take off my plate."
    ch_x " I've heard that you have been having. . . financial problems of late."
    ch_x "I may be able to help those problems go away."
    ch_x "I've come up with a fantstic new method of acquiring money."
    ch_x "I call it \"micro transactions!\""
    menu:
        extend ""
        "What, like -I- give -you- cash?":
            call change_Xavier_face ("_shocked")
            ch_x "What? How would that make sense? You give me cash so I give you cash?"
        "What a rip-off!":
            call change_Xavier_face ("_shocked")
            ch_x "I haven't even explained the system yet!"
        "Shill!":
            call change_Xavier_face ("_shocked")
            ch_x "what are you even talking about?"
    ch_x "I don't understand what the problem is, it's just a form of surprise mechanic!"
    call change_Xavier_face ("_happy")
    ch_x "You open a small box and receive an item!"
    ch_x "It really is a remarkable system!"
    ch_x "It involves using a certain invention developed by a friend of mine."
    ch_x "They are called \"Pym particles.\""
    menu:
        extend ""
        "What?!":
            pass
        "Oh. I see where this is going. . .":
            pass
    ch_x "Yes, what it allows me to do is take large. . ."
    ch_x ". . . cumbersome. . . "
    ch_x ". . . objects, and shrink them down to a more manageable size."
    ch_x "Then those items can be conveniently delivered all over town."
    ch_x "All I need from you is to pick up these packages and deliver them to their destinations."
    ch_x "Microtransactions!"
    menu:
        "Yes, I get it.":
            pass
        "Huh?":
            call change_Xavier_face ("_shocked")
            ch_x ". . . I don't think I could dumb it down further."
    call change_Xavier_face ("_happy")
    ch_x "Here, a nice starter package, just bring this to Henry in the lab."
    menu:
        extend ""
        "Ok.":
            pass
        "No thank you.":
            ch_x "If this isn't something you want to do, I understand."
            ch_x "But this is actually a rather urgent delivery, so I'm afraid that just this once. . ."
            ch_x "I must insist."
    show black_screen onlayer black
    scene
    pause 0.1
    scene empty_class onlayer backdrop
    hide black_screen onlayer black
    $ round -= 5
    "You take a small metal box from the Professor, and head to Professor McCoy's lab."
    "You drop it off in the corner, and it rapidly expands into a large device labeled \"Pym\""
    ch_b "Oh, my shirnk ray!"
    $ bg_current = "bg_study"
    show black_screen onlayer black
    pause 0.1
    call set_the_scene
    hide black_screen onlayer black
    $ round -= 5
    "You return to Xavier's office."
    $ Player.cash += 5
    ch_x "See? Simple!"
    $ Player.history.append("micro")
    ch_x "If you wish to make further microtransactions, just access it from McCoy's lab."
    ch_x "I'm sure there will be plenty of business."
    "You return to your room."
    $ bg_current = "bg_player"
    show black_screen onlayer black
    pause 0.1
    call set_the_scene
    hide black_screen onlayer black
    return

label Microtransactions:



    if round < 20:
        "You don't have time for that now, maybe later."
        return
    if Player.daily_history.count("micro") >= 3:
        "There are no more Microtransactions for today."
        return
    menu:
        "What do you want to do?"
        "Deliver a nearby MT":
            $ line = renpy.random.choice(["the danger room",
                        "the classroom",
                        "the pool",
                        "Scott's room",
                        "Kurt's room",
                        "Bobby's room",
                        "Logan's room",
                        "-|A|-'s room",
                        "an unmarked room with a single flickering bulb and odd staining patterns",
                        "the library",
                        "Xavier's study",
                        "the caffeteria"])
            $ round -= 10
            show black_screen onlayer black
            pause 0.1
            hide black_screen onlayer black
            "You grab a package from McCoy and deliver it to [line]."
            $ line = renpy.random.choice(["a refridgerator",
                        "a microwave",
                        "a sex doll. That's awkward",
                        "a sex doll. That makes sense",
                        "a car. Maybe you should have opened this outside?",
                        "a desk",
                        "a large bed",
                        "a crate full of wrapped white powder. Flour, probably",
                        "a giant pile of wrapped clothing",
                        "a giant crate of booze"])
            "It quickly grows into [line]."
            $ round -= 5
            $ Player.cash += 1
            show black_screen onlayer black
            pause 0.1
            hide black_screen onlayer black
            "You head back home."
        "Deliver a distant MT [[locked] (locked)" if round < 50:
            pass
        "Deliver a distant MT" if round >= 50:
            $ line = renpy.random.choice(["the restaurant",
                        "the theater",
                        "a local boutique",
                        "mayor's house",
                        "the mall",
                        "the fire station",
                        "the other restaurant, the one you don't go to",
                        "the dance club",
                        "a broken down shack",
                        "the local highschool"])
            $ round -= 20
            show black_screen onlayer black
            pause 0.1
            hide black_screen onlayer black
            "You grab a package from McCoy and deliver it to [line]."
            $ line = renpy.random.choice(["a refridgerator",
                        "a microwave",
                        "a sex doll. That's awkward",
                        "a sex doll. That makes sense",
                        "a car. Maybe you should have opened this outside?",
                        "a sofa",
                        "a large bed",
                        "a crate full of wrapped white powder. Flour, probably",
                        "a giant pile of wrapped clothing",
                        "a giant crate of popcorn"])
            "It quickly grows into [line]."
            $ round -= 10
            $ Player.cash += 3
            show black_screen onlayer black
            pause 0.1
            hide black_screen onlayer black
            "You head back home."
        "Exit":
            return
    $ Player.daily_history.append("micro")
    return
