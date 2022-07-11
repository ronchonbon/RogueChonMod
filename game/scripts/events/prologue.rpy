label prologue:
    $ time_index = 2
    $ current_time = time_options[time_index]

    $ Player.location = "bg_entrance"

    scene background onlayer background
    scene

    show midground zorder 2
    show foreground zorder 4
    show cover zorder 7
    show Chibi_cock onlayer screens

    if config.developer:
        menu:
            "Skip prologue?"
            "Yes":
                jump prologue_end
            "No":
                pass

    "You recently discovered that you were a mutant when a Sentinel attacked your home.\nYou were rescued by a squad of X-Men and given this address."
    "You've arrived in the early evening at the Xavier Institute, where you've been promised a new home."
    "Things have been tough for mutants in the years since Apocalypse's fall, but this sounds like it might be a good deal."

    call get_color_transform
    $ color_transform = _return

    show Xavier_sprite at sprite_location(stage_left), color_transform with easeinleft

    ch_x "Welcome to the Xavier Institute for Higher Learning. This is a home for all mutants to learn and grow."
    ch_x "My name is Charles Xavier, and I have dedicated my life to helping other mutants such as yourself."
    ch_x "I know that you've had a difficult time, but you will be safe here."
    ch_x "You'll have classes in the day to teach you the skills you'll need, and training in the Danger Room for self defense."
    ch_x "Since you're on your own, we'll provide a small stipend for your day-to-day needs."
    ch_x "Did you have any questions for me young man?"
    ch_p "Why did you even bring me here, I don't have any \"super powers.\""
    ch_x "Nonsense, my boy. You have an incredibly useful ability. . ."
    ch_x "the power to negate other powers, even including my own."

    $ RogueX.name = "???"
    $ RogueX.change_face("surprised")
    $ RogueX.location = Player.location

    call show_Girl(RogueX, x_position = stage_far_far_right, color_transform = color_transform, transition = easeinright)

    ch_r "What's that Prof? This new kid can negate mutant powers?"

    $ RogueX.mouth = "normal"

    call show_Girl(RogueX, x_position = stage_right, transition = ease)

    ch_r "Maybe even my own?"
    ch_x "That is correct, Rogue, though currently, his powers are weak and uncontrolled."

    $ RogueX.name = "Rogue"

    ch_x "One day, however, he may even be able to help you turn your powers off permanently."
    ch_r "! . . ."

    $ RogueX.change_face("smile")

    ch_x "Since you're here, why don't you show our new guest around the mansion?"
    ch_x "This young lady is named [RogueX.name], one of our veteran students."
    ch_x "And [RogueX.name], this young man goes by the name \"[Player.name]\"."

    hide Xavier_sprite with easeoutright

    call show_Girl(RogueX, x_position = stage_center, transition = ease)

    menu:
        ch_r "A pleasure ta meet ya, [RogueX.player_petname]. Let me give ya the lay of the place."
        "It's nice to meet you too.":
            $ RogueX.change_face("smile", blushing = 1)
            call change_Girl_stat(RogueX, "love", 20)

            ch_r "Oh, a gentleman. I think we'll really get along."

            $ RogueX.blushing = ""

            ch_r "Ok, so let me show ya around. . ."
        "The \"lay\" of the place, eh?":
            $ RogueX.brows = "normal"
            $ RogueX.eyes = "surprised"
            $ RogueX.mouth = "smile"
            $ RogueX.blushing = "_blush1"
            call change_Girl_stat(RogueX, "love", 10)

            ch_r "Wha- what? N, no, that's not what I meant! I'm just giving you the campus tour!"

            $ RogueX.change_face("bemused")
            call change_Girl_stat(RogueX, "inhibition", 20)
            call change_Girl_stat(RogueX, "obedience", 20)

            ch_r "Hmm. . ."

            call change_Girl_stat(RogueX, "lust", 3)
            $ RogueX.change_face("normal", eyes = "surprised")

            ch_r "Anyways, let's get this back on track. . ."

            $ RogueX.blushing = ""
        "Whatever.":
            call change_Girl_stat(RogueX, "obedience", 20)
            $ RogueX.change_face("sad", brows = "normal")
            $ RogueX.mood += 1

            ch_r "Tsk, well ok, let's get started."
        "Screw off.":
            $ RogueX.change_face("angry")
            call change_Girl_stat(RogueX, "love", -30)
            call change_Girl_stat(RogueX, "obedience", 30)
            $ RogueX.mood += 4

            call show_Girl(RogueX, transition = vpunch)

            ch_r "Well I never!"
            ch_r "Hmph, I have to give the tour anyways, so get mov'in. . ."

    call hide_Girl(RogueX)

label tour_start:
    call set_the_scene(location = "bg_campus", fade = True)
    call add_Girls(RogueX)

    ch_r "This is the campus square. It links up to all the major locations on campus and you'll probably pass through here a lot."

    call hide_Girl(RogueX)
    call set_the_scene(location = "bg_player", fade = True)
    call add_Girls(RogueX)

    ch_r "This will be your room, we each get private rooms now that the campus has been expanded."

    menu:
        ch_r "Pretty nice, right?"
        "It is with you in it.":
            $ RogueX.blushing = "_blush1"
            call change_Girl_stat(RogueX, "love", 20)
            call change_Girl_stat(RogueX, "lust", 5)
        "It'll do.":
            call change_Girl_stat(RogueX, "obedience", 10)

    ch_p "And where do you live?"

    $ RogueX.blushing = ""

    ch_r "Oh, right down the hall, all the doors are labeled."

    if not approval_check(RogueX, 500, "L") or RogueX.mood > 5:
        ch_r "I wouldn't recommend bothering me though."
    else:
        ch_r "You can stop by sometime, but not after curfew."

    call hide_Girl(RogueX)
    call set_the_scene(location = "bg_classroom", fade = True)
    call add_Girls(RogueX)

    ch_r "And this is one of our state-of-the-art classrooms."
    ch_r "They're multi-purpose so they can teach almost anything in them."
    ch_r "This used to just be an after school training facility, but over the past few years it's grown into a full service university."

    call hide_Girl(RogueX)
    call set_the_scene(location = "bg_dangerroom", fade = True)
    call add_Girls(RogueX)

    ch_r "This is the Danger Room. It's been upgraded to a fully holographic experience, allowing realistic battlefield simulations."

    $ counter = 0

    while counter < 3:
        menu:
            extend ""
            "Why would you need battlefield simulations?" if counter != 1:
                ch_r "The world is a dangerous place, [RogueX.player_petname], especially for us mutants."
                ch_r "This place helps us train to use our powers. Coming here can help you to get a grasp on yours as well."

                $ counter = 3 if counter == 2 else 1
            "So can this place make some more. . . erotic simulations?" if counter != 2:
                $ RogueX.eyes = "side"
                $ RogueX.mouth = "lipbite"
                $ RogueX.blushing = "_blush1"
                call change_Girl_stat(RogueX, "inhibition", 30)
                call change_Girl_stat(RogueX, "lust", 5)

                ch_r "Well. . . I suppose it could. . . if one were into such things."

                $ RogueX.blushing = ""

                $ counter = 3 if counter == 1 else 2
            "Ok, let's move on.":
                $ counter = 3

    ch_r "Moving on then. . ."

    call hide_Girl(RogueX)

label tour_end:
    call set_the_scene(location = "bg_campus", fade = True)
    call add_Girls(RogueX)

    ch_r "Well, that's the nickel tour, now you know where everything is. . ."

    $ RogueX.mouth = "normal"
    $ RogueX.eyes = "normal"
    $ RogueX.brows = "confused"

    menu:
        ch_r "I was curious about your ability. Is it true that other mutant powers don't work on you?"
        "Sure.":
            ch_p "That's what they tell me, but to be honest, I don't know much about it."
        "What's it to you?":
            ch_p "What do you care?"

            $ RogueX.eyes = "sexy"

            ch_r ". . ."

            call change_Girl_stat(RogueX, "love", -30)

    ch_r "Well, you see, my power is the ability to absorb the mutant powers and memories of those I touch."
    ch_r "Only, I still can't really control it. I can't touch people without hurting them, and I might even put them into a coma if I'm not careful."
    ch_r "So I was hoping that maybe with your power. . ."

    $ RogueX.change_face("sexy", brows = "sad")

    ch_r "I could. . . touch you?"

    menu:
        ch_r "So I was hoping that maybe with your power. . . I could. . . touch you?"
        "Like, a kiss?":
            if approval_check(RogueX, 500, "L"):
                $ RogueX.change_face("surprised", blushing = 1)
                call change_Girl_stat(RogueX, "love", 20)
                call change_Girl_stat(RogueX, "obedience", 30)
                call change_Girl_stat(RogueX, "inhibition", 20)

                ch_r "Well, aren't you fresh."

                $ RogueX.change_face("sexy", mouth = "smile")

                ch_r "Just this once."

                call smooch(RogueX)

                "She gives you a little peck on the cheek."

                $ RogueX.change_face("smile")
            else:
                $ RogueX.change_face("bemused")
                call change_Girl_stat(RogueX, "love", 30)

                ch_r "Heh, You'll have to earn that [RogueX.player_petname]."

                $ RogueX.change_face("sexy", brows = "sad")
                $ RogueX.arm_pose = 2
                $ RogueX.change_out_of("gloves")

                "She pulls off her glove and touches your face."
        "Ok, be my guest.":
            call change_Girl_stat(RogueX, "love", 30)
            $ RogueX.change_face("sexy", brows = "sad")
            $ RogueX.arm_pose = 2
            $ RogueX.change_out_of("gloves")

            "She pulls off her glove and touches your face."
        "No, that's weird.":
            $ RogueX.change_face("sad", brows = "normal")
            call change_Girl_stat(RogueX, "love", -30)
            call change_Girl_stat(RogueX, "inhibition", 30)

            ch_r "Well I'm just too damned curious, sorry."

            $ RogueX.arm_pose = 2
            $ RogueX.change_out_of("gloves")

            "She pulls off her glove and touches your face."

    $ RogueX.change_face("surprised")

    ch_r "Wow."
    ch_r "This is amazing! With anyone else I would have drained their powers and they'd be out by now."

    $ RogueX.change_face("sexy")

    menu:
        ch_r "Do you know how long it's been since I've felt human contact without hurting them?"
        "Glad I could help.":
            call change_Girl_stat(RogueX, "love", 10)
        "I'm guessing it's been quite a while.":
            $ RogueX.change_face("bemused", blushing = 1)
            call change_Girl_stat(RogueX, "lust", 5)

            ch_r ". . ."

    $ RogueX.change_face("smile")

    ch_r "What a rush. I guess that's it then, I'm heading back to my room, you can head to yours."

    $ RogueX.blushing = ""

    if approval_check(RogueX, 500, "L"):
        ch_r "Maybe I'll see you around though. Here's my number, you can give me a call."

        $ Player.Phonebook.append(RogueX)

    $ RogueX.arm_pose = 1
    $ RogueX.change_into("black gloves")

label tour_parting:
    $ RogueX.emotion = "normal"
    $ RogueX.blushing = ""

    $ line = "Want to make out a little?"

    menu:
        extend ""
        "Ok, see you later.":
            call remove_Girl(RogueX)

            "You head back to your room."
        "[line]":
            if approval_check(RogueX, 560, "L"):
                $ RogueX.change_face("bemused", 1)
                call change_Girl_stat(RogueX, "inhibition", 20)
                call change_Girl_stat(RogueX, "inhibition", 10)

                call start_Action(RogueX, "kiss")

                if RogueX.mood > 4:
                    call change_Girl_stat(RogueX, "love", -10)
                    call change_Girl_stat(RogueX, "obedience", 30)

                    ch_r "What the hell, [Player.name]?!"
                    ch_r "Way to take advantage of a girl's feelings there!"

                    call remove_Girl(RogueX)

                    "[RogueX.name] tears off and you head back to your room."
                else:
                    $ RogueX.change_face("bemused", blushing = 1)

                    ch_r "That was real nice, [RogueX.player_petname]. I'll definitely be seeing you later."

                    call remove_Girl(RogueX)

                    "You head back to your room."
            else:
                $ RogueX.change_face("bemused")

                ch_r "Nah, I think you've had enough for today, [RogueX.player_petname]."

                call remove_Girl(RogueX)

                "You head back to your room."

label prologue_end:
    $ RogueX.location = "bg_rogue"

    $ active_Girls.append(RogueX)

    $ RogueX.History.update("met")

    $ round = 10

    $ shift_focus(RogueX)

    show screen status()

    jump player_room
