label meet_Laura:
    call set_the_scene(location = "bg_dangerroom", show_Characters = False, fade = True)
    call remove_all

    "As you approach the Danger Room, you hear a ferocious clanging of metal."
    "Just as you pass through the door, a robotic arm smashes into your face."

    show black_screen onlayer black with vpunch

    ". . ."

    $ LauraX.name = "???"
    $ LauraX.names = []
    $ LauraX.location = Player.location
    $ LauraX.change_Outfit(instant = True)

    call get_color_transform
    $ color_transform = _return

    call show_Girl(LauraX, x_position = stage_center, color_transform = color_transform, animation_transform = kiss_launch_animation, transition = False)

    pause 1.0

    hide black_screen onlayer black with dissolve

    "When you come to, a girl pulls you up by your arm."

    call show_Girl(LauraX, animation_transform = reset_zoom)
    $ shift_focus(LauraX)

    $ LauraX.change_face("surprised", eyes = "squint", brows = "sad")

    ch_l "Oh, good, you don't look too damaged."

    $ LauraX.change_face("smile", brows = "sad")

    ch_l "Sorry about that, I was getting a work-out in, and must have forgotten to lock the door."

    $ LauraX.change_face("smile")

    $ loop = True
    $ topics = []

    while loop:
        menu:
            extend ""
            "Who are you?" if LauraX.name == "???":
                $ LauraX.change_face("normal")

                ch_l "I go by \"X-23\" in the field."

                $ LauraX.name = "X-23"
                $ LauraX.names.append("X-23")
            "X-23? Is that your real name?" if LauraX.name == "X-23" and "X23" not in topics:
                $ topics.append("X23")

                $ LauraX.change_face("confused")

                ch_l "It's the one I was born with."
            "Is there anything else I could call you?" if "X23" in topics and "Laura" not in topics:
                $ topics.append("Laura")

                $ LauraX.change_face("normal")
                call change_Girl_stat(LauraX, "love", 5)

                ch_l "I also go by Laura. Laura Kinney."

                $ LauraX.change_face("confused", mouth = "normal")

                $ LauraX.name = "Laura"
                $ LauraX.names.append("Laura")

                menu:
                    extend ""
                    "Nice to meet you Laura.":
                        $ LauraX.change_face("normal")
                        call change_Girl_stat(LauraX, "love", 5)

                        ch_l "Yeah, ok."
                    "Hello Laura Laura Kinney.":
                        $ LauraX.change_face("confused", mouth = "sucking")

                        ch_l "It's just-"

                        $ LauraX.change_face("smile", brows = "surprised")
                        call change_Girl_stat(LauraX, "love", 3)
                        call change_Girl_stat(LauraX, "inhibition", 2)

                        ch_l "Oh, I get it."
                    "Ok, how did you get that name?":
                        $ LauraX.change_face("angry", blushing = 1, eyes = "side")
                        call change_Girl_stat(LauraX, "love", -2)
                        call change_Girl_stat(LauraX, "obedience", 2)

                        ch_l "You're getting too personal."

                        $ LauraX.blushing = ""
            "I think I'd prefer calling you X-23." if LauraX.name == "Laura":
                $ LauraX.change_face("sadside", brows = "normal")
                call change_Girl_stat(LauraX, "love", -2)
                call change_Girl_stat(LauraX, "obedience", 5)

                ch_l "Suit yourself."

                $ LauraX.name = "X-23"
            "My name is [Player.name]" if LauraX.name != "???" and "player" not in topics:
                $ topics.append("player")

                $ LauraX.change_face("normal")

                ch_l "Ok."

                menu:
                    extend ""
                    ". . .and it's nice to meet you?":
                        $ LauraX.change_face("confused", mouth = "normal")
                        call change_Girl_stat(LauraX, "love", 1)

                        ch_l "Yeah, you too."
                    "So. . .":
                        call change_Girl_stat(LauraX, "love", 3)
                        call change_Girl_stat(LauraX, "obedience", 1)
                        call change_Girl_stat(LauraX, "inhibition", 1)
            "What are you doing here?" if "training" not in topics:
                $ topics.append("training")

                $ LauraX.change_face("confused")
                call change_Girl_stat(LauraX, "obedience", -2)

                ch_l "Training. That's the point of this place."

                menu:
                    extend ""
                    "I meant in the school, I haven't seen you around before.":
                        call change_Girl_stat(LauraX, "obedience", 2)
                    "Ok, that's fair.":
                        $ LauraX.change_face("normal")

                        ch_p "But are you new to this school?"

                        call change_Girl_stat(LauraX, "love", 3)
                        call change_Girl_stat(LauraX, "obedience", 4)

                ch_l "I've been here since before your time."
                ch_l "Mostly out in the field though."
            "So you don't stay here long?" if "training" in topics and "stay" not in topics:
                $ topics.append("stay")

                $ LauraX.change_face("normal", eyes = "side")
                call change_Girl_stat(LauraX, "love", 2)

                ch_l "I'll be heading out again soon."

                $ LauraX.change_face("normal")

                ch_l "But I am planning to stick around after I get back from this mission."
            "What the hell was that?" if len(topics) < 2 and "wtf" not in topics:
                $ topics.append("wtf")

                $ LauraX.change_face("confused")
                call change_Girl_stat(LauraX, "love", -2)
                call change_Girl_stat(LauraX, "obedience", 8)

                ch_l "It was a robot arm."

                $ LauraX.change_face("sad", blushing = 1, eyes = "leftside")

                ch_l "Like I said, sorry."

                $ LauraX.change_face("smile", blushing = 0, brows = "confused")
                call change_Girl_stat(LauraX, "obedience", -3)
                call change_Girl_stat(LauraX, "inhibition", 3)

                ch_l "You probably should have ducked though."
            "So what's your mutant power?" if LauraX.name != "???" and "claws" not in topics:
                $ topics.append("claws")

                $ LauraX.change_face("normal")
                call change_Girl_stat(LauraX, "love", 1)
                call change_Girl_stat(LauraX, "obedience", 1)

                ch_l "I can heal fast."

                $ LauraX.arm_pose = 2

                ch_l "Also I have claws."

                $ LauraX.claws = True
                $ LauraX.change_face("smile", brows = "confused")

                "snikt"

                menu:
                    "Those claws look pretty sharp.":
                        call change_Girl_stat(LauraX, "inhibition", 3)

                        ch_l "Yeah, indestructible too."
                    "Cool.":
                        $ LauraX.change_face("smile", brows = "surprised")
                        call change_Girl_stat(LauraX, "love", 3)
                        call change_Girl_stat(LauraX, "obedience", 2)
                        call change_Girl_stat(LauraX, "inhibition", 1)

                        ch_l "Yeah, indestructible too."
                    "Ouch.":
                        $ LauraX.claws = False
                        $ LauraX.change_face("confused")
                        call change_Girl_stat(LauraX, "love", -2)
                        call change_Girl_stat(LauraX, "obedience", -5)

                        ch_l "Don't worry, I won't stab you."

                        $ LauraX.change_face("confused", mouth = "normal")
                        call change_Girl_stat(LauraX, "inhibition", 7)

                        ch_l "Probably."

                $ LauraX.claws = False
                $ LauraX.arm_pose = 1
            "Don't you want to know my power?" if "claws" in topics and "powers" not in topics:
                $ topics.append("powers")

                if approval_check(LauraX, 405, "L"):
                    $ LauraX.change_face("smile", brows = "confused")

                    ch_l "Yeah, I guess."
                else:
                    $ LauraX.change_face("normal")

                    ch_l "Not really."

                call change_Girl_stat(LauraX, "inhibition", 3)

                ch_p "I'm immune to mutant powers and can shut them off."

                $ LauraX.change_face("smile", brows = "confused")
                call change_Girl_stat(LauraX, "love", 3)
                call change_Girl_stat(LauraX, "obedience", 3)

                ch_l "Huh. Interesting. So you can stop me from healing?"
                ch_p "Yeah. If I touch you, temporarily."

                call change_Girl_stat(LauraX, "obedience", 2)
                call change_Girl_stat(LauraX, "lust", 3)

                ch_l "Give it a try."
                "She holds out her arm, and you grab it."

                $ LauraX.change_face("confused")
                call change_Girl_stat(LauraX, "love", 1)
                call change_Girl_stat(LauraX, "obedience", 2)
                call change_Girl_stat(LauraX, "lust", 5)

                ch_l "Huh."

                $ LauraX.addiction_rate += 1
                $ LauraX.change_face("sexy", blushing = 1, eyes = "closed")

                "You can feel her shudder a little."

                $ LauraX.addiction_rate += 1
                $ LauraX.change_face("sexy", blushing = 1)
                call change_Girl_stat(LauraX, "love", 1)
                call change_Girl_stat(LauraX, "obedience", 3)
                call change_Girl_stat(LauraX, "lust", 5)

                ch_l "That feels weird."

                $ LauraX.addiction_rate += 1
                $ LauraX.eyes = "leftside"
                call change_Girl_stat(LauraX, "obedience", 1)
                call change_Girl_stat(LauraX, "lust", 3)

                ch_l "-a little more \"alive\" than usual."

                $ LauraX.addiction_rate += 1
                $ LauraX.change_face("sexy", blushing = 1, brows = "confused")
                call change_Girl_stat(LauraX, "inhibition", 5)
                call change_Girl_stat(LauraX, "lust", 5)

                ch_l "Almost. . . dangerous."

                $ LauraX.blushing = ""
            "Anyways. . ." if LauraX.name != "???":
                $ loop = False

        if len(topics) > 2 and LauraX.name == "???":
            call change_Girl_stat(LauraX, "love", -2)
            call change_Girl_stat(LauraX, "obedience", 5)
            call change_Girl_stat(LauraX, "inhibition", 5)

            ch_l "Oh, by the way, you can call me \"X-23\"."

            $ LauraX.name = "X-23"
            $ LauraX.names.append("X-23")

        if len(topics) > 7:
            $ loop = False

    ch_l "Ok, I've got a plane to catch."

    if "player" in topics:
        $ LauraX.change_face("smile")
        call change_Girl_stat(LauraX, "love", 2)
        call change_Girl_stat(LauraX, "lust", 1)

        ch_l "Maybe I'll see you when I get back, [Player.name]."
    else:
        $ LauraX.change_face("normal")

        ch_l "Maybe I'll see you when I get back, stranger."

    if "powers" in topics:
        $ LauraX.change_face("smile", blushing = 1, brows = "confused")
        call change_Girl_stat(LauraX, "obedience", 2)
        call change_Girl_stat(LauraX, "inhibition", 2)
        call change_Girl_stat(LauraX, "lust", 3)

        ch_l "We should. . . spar."

    call remove_Girl(LauraX)

    "She dashes out of the room, headed for the hangar."

    $ Nearby = []

    $ LauraX.location = "hold"
    $ LauraX.History.update("met")

    $ shift_focus(RogueX)

    $ round -= 20

    return
