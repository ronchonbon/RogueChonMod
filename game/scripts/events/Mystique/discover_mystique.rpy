label discover_Mystique:
    $ MystiqueX.location = "bg_dangerroom"

    call set_the_scene(location = "bg_dangerroom", fade = True)

    "You enter the danger room. [MystiqueX.name]'s in the middle of an intense training simulation."

    $ MystiqueX.change_face("surprised")

    "You lock eyes with her just as she attempts a difficult maneuver."

    show black_screen onlayer black with vpunch

    "The distraction lasts less than a second, but it's enough to knock her to the ground."

    hide black_screen onlayer black

    "You reach out to help her up, but as you touch her, her body begins to. . . ripple?"

    $ MystiqueX.disguise = None
    $ MystiqueX.Outfit.undress()

    call show_Girl(MystiqueX, transition = Mystique_dissolve)

    ch_p "Wha. . . what's going on?"
    ch_m "Idiot! Unhand me!"
    ch_p "You're Mystique!!!"

    $ MystiqueX.name = "Mystique"
    $ MystiqueX.names.append("Mystique")
    $ MystiqueX.change_face("angry")

    ch_m "You will be quiet, or you will die."
    "You try to make a run for it but she quickly jumps between you and the door."
    ch_m "I'd rather you didn't."

    menu:
        ch_m "I'm sure we can make a deal for your silence."
        "How can I trust you?":
            ch_m "You can't."
        "What are you talking about? No!":
            ch_m "There must be something you want."

    ". . ."

    menu:
        "Your eyes can't help but drift down her naked body."
        "Huh. You make some great points.":
            ch_m "Or, I could just kill you. . ."

    ch_p "Wait! If you do that, everyone on campus will be looking for you. That would be bad, right?"

    $ MystiqueX.change_face("confused")

    ch_m "You may be right. . ."

    $ MystiqueX.eyes = "closed"

    pause 0.5

    ch_m "Fine."

    $ MystiqueX.disguise = "Raven"
    $ MystiqueX.change_face("sly")

    call show_Girl(MystiqueX, transition = Mystique_dissolve)

    ch_m "Meet me in my room."

    $ MystiqueX.History.update("discovered")

    call hide_all

    $ Girl = MystiqueX

    jump girls_room
