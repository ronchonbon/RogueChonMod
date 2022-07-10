label meet_Jubes:
    show black_screen onlayer black

    pause 3.0

    $ Player.climax = 30

    $ JubesX.name = "???"
    $ JubesX.names = []
    $ JubesX.location = Player.location
    $ JubesX.arm_pose = 2
    $ JubesX.change_face("sucking", 1)
    $ JubesX.change_Outfit()

    ch_u "\"Slurp, slurp, slurp.\""

    call get_color_transform
    $ color_transform = _return

    call show_Girl(JubesX, x_position = stage_right, color_transform = color_transform, animation_transform = vampire)
    call change_Player_stat("focus", 80, 5)
    call change_Girl_stat(JubesX, "lust", 5)

    "You feel a pleasant sensation. . ."
    ch_u "\"Slurp, slurp, slurp.\""

    call change_Player_stat("focus", 80, 5)

    call change_Girl_stat(JubesX, "lust", 5)
    $ JubesX.addiction_rate += 1

    "It's somewhere below your waist. . ."
    ch_u "\"Slurp, slurp, slurp.\""

    call change_Player_stat("focus", 80, 10)
    call change_Girl_stat(JubesX, "lust", 5)

    "Wait . . no it's not. . ."

    "You open your eyes. . ."

    hide black_screen onlayer black

    $ shift_focus(JubesX)

    $ counter = 3

    "Someone seems to be giving you a hickey on your neck. . ."

    while counter > 0:
        call change_Player_stat("focus", 80, 10)
        call change_Girl_stat(JubesX, "lust", 5)

        menu:
            extend ""
            "Stay quiet.":
                call change_Girl_stat(JubesX, "inhibition", 2)
                call change_Girl_stat(JubesX, "lust", 5)
                $ JubesX.addiction_rate += 1

                if counter > 2:
                    "You just let her do her thing and pretend to still be asleep."
                    ch_v "\"Slurp, slurp, slurp.\""
                    ". . ."
                elif counter > 1:
                    "It does feel nice. . ."
                    ch_v "\"Slurp, slurp, slurp.\""
                    ". . ."
                else:
                    "You wouldn't want to disturb her. . ."
                    ch_v "\"Slurp, slurp, slurp.\""

                    show black_screen onlayer black

                    ". . ."

                    call change_Girl_stat(JubesX, "love", 2)
                    $ JubesX.change_face("surprised", 2)

                    ch_v "Whoa! Um. . . this is bad. . ."
                    ch_v "Wake up! Wake up! Sorry!!!!"
                    "You slowly pull yourself back. . ."

                    hide black_screen onlayer black

                    ch_v "Sorry!"

                    call show_Girl(JubesX)

                    ch_v "I think I maybe drained a bit too much!"

                    $ JubesX.change_face("sadside", 1)

                    ch_v "I was just. . . thirsty. . ."
            "Um. . . lady? What're you doing?":
                call change_Girl_stat(JubesX, "obedience", 5)
                call change_Girl_stat(JubesX, "inhibition", -1)
                $ JubesX.change_face("surprised", 2)

                call show_Girl(JubesX)

                ch_v "Ah!"

                $ JubesX.change_face("sadside", 1, mouth = "normal")

                ch_v "Oh, I guess I was. . ."

                $ counter = 1
            "That feels great, keep going. . .":
                call change_Girl_stat(JubesX, "love", 2)
                call change_Girl_stat(JubesX, "inhibition", 2)
                $ JubesX.change_face("surprised", 2)

                call show_Girl(JubesX)

                ch_v "Oh!"

                $ JubesX.change_face("sadside", 1, mouth = "smile")

                ch_v "I, um. . . I wasn't expecting that reaction. . ."

                $ JubesX.change_face("sad", 1, mouth = "smile")

                $ counter = 1
            "Hey, quit that!":
                call change_Girl_stat(JubesX, "obedience", 10)
                call change_Girl_stat(JubesX, "inhibition", -3)
                $ JubesX.change_face("surprised", 2)

                call show_Girl(JubesX)

                ch_v "Ah!"

                $ JubesX.change_face("sadside", 1, mouth = "normal")

                ch_v "Sorry!"

                $ counter = 1

        $ counter -= 1

    $ JubesX.blushing = "_blush1"

    call show_full_body(JubesX)

    $ counter = 3

    while counter > 0:
        menu:
            extend ""
            "Who are you?" if "Jubilee" not in JubesX.names:
                call change_Girl_stat(JubesX, "love", 2)
                call change_Girl_stat(JubesX, "obedience", 1)
                $ JubesX.change_face("smile", 1)

                ch_v "Oh, I guess I should introduce myself."
                ch_v "The name's \"Jubilee.\""

                $ JubesX.names.append("Jubilee")
                $ JubesX.name = "Jubilee"

                ch_v "Nice to ea- meet you."

                menu:
                    extend ""
                    "Ok. . .":
                        $ JubesX.change_face("confused", 1)
                        call change_Girl_stat(JubesX, "obedience", 3)

                        ch_v ". . ."
                    "My name's [Player.name]":
                        call change_Girl_stat(JubesX, "love", 3)
                        call change_Girl_stat(JubesX, "obedience", 2)

                        ch_v "Oh, yeah, I know that."

                        call change_Girl_stat(JubesX, "inhibition", 2)

                        ch_v "I've. . . heard about you."
                    "Huh.":
                        $ JubesX.change_face("confused", 1)

                        ch_v ". . ."
            "That's an interesting name." if "Jubilee" in JubesX.names and "Jubilation" not in JubesX.names:
                $ JubesX.change_face("smile", 1)

                ch_v "Oh, yeah. Weird parents."
                ch_v "It's actually \"Jubilation Lee,\" but you know. . ."
                ch_v "Guess I leaned into it?"

                $ JubesX.names.append("Jubilation")
                $ JubesX.names.append("Miss Lee")
                $ JubesX.petnames.append("Miss Lee")

                menu:
                    extend ""
                    "Yeah, sure.":
                        call change_Girl_stat(JubesX, "love", 1)
                        call change_Girl_stat(JubesX, "obedience", 3)

                        ch_v ". . ."
                    "It suits you.":
                        call change_Girl_stat(JubesX, "love", 5)
                        call change_Girl_stat(JubesX, "inhibition", 2)

                        ch_v ". . ."
                    "Weird.":
                        $ JubesX.change_face("angry", 1)
                        call change_Girl_stat(JubesX, "love", -3)
                        call change_Girl_stat(JubesX, "obedience", 3)
                        call change_Girl_stat(JubesX, "inhibition", 1)

                        ch_v ". . ."

                        $ JubesX.change_face("normal", 1)
            "What are you doing in my room?!" if "thirst" not in JubesX.recent_history:
                call change_Girl_stat(JubesX, "love", -1)
                call change_Girl_stat(JubesX, "obedience", 7)
                call change_Girl_stat(JubesX, "inhibition", -2)
                $ JubesX.change_face("startled", 2)
                ch_v "Oh, I was just. . . thirsty?"
                $ JubesX.change_face("smile", 1)
                $ JubesX.add_word(1, "thirst", 0, 0, 0)


            "What were you doing?" if "thirst" not in JubesX.recent_history:
                call change_Girl_stat(JubesX, "inhibition", 1)
                $ JubesX.change_face("startled", 2)
                ch_v "I was just. . . getting a drink?"
                $ JubesX.change_face("smile", 1)
                $ JubesX.add_word(1, "thirst", 0, 0, 0)




            "So you drink blood?" if "vamp" in JubesX.recent_history and "blood" not in JubesX.recent_history:
                call change_Girl_stat(JubesX, "love", 1)
                $ JubesX.change_face("sadside", 2)
                ch_v "Yeah, I kinda have to. . ."
                $ JubesX.change_face("sad", 1)
                ch_v "Sorry again. . ."
                $ JubesX.add_word(1, "blood", 0, 0, 0)
            "Can you turn into a bat?" if "vamp" in JubesX.recent_history and "bat" not in JubesX.recent_history:
                call change_Girl_stat(JubesX, "love", 1)
                $ JubesX.change_face("confused", 1)
                ch_v "Well, no. . ."
                $ JubesX.change_face("sly", 1)
                ch_v "But I am strong and can turn into mist."
                ch_v "Sometimes."
                $ JubesX.add_word(1, "bat", 0, 0, 0)
            "Is it contagious?" if "vamp" in JubesX.recent_history and "contagious" not in JubesX.history:
                $ JubesX.change_face("sadside", 2)
                ch_v "Infectious. . ."
                $ JubesX.change_face("surprised", 1, mouth = "sucking")
                ch_v "- and no!"
                $ JubesX.change_face("sadside", 1)
                ch_v "It was, but Dr. Strange was able to cast a spell or something."
                ch_v "So you don't need to worry about it spreading to you or anything."
                $ JubesX.change_face("sad", 1)
                $ JubesX.add_word(1, 0, 0, 0, "contagious")
            "Why me?" if "vamp" in JubesX.recent_history and "devamp" not in JubesX.recent_history:
                call change_Girl_stat(JubesX, "love", 1)
                $ JubesX.change_face("sly", 1, eyes = "side")
                ch_v "Well. . ."
                ch_v "I had a theory. . ."
                ch_v "I sorta figured that if you could negate powers, then maybe. . ."
                $ JubesX.change_face("smile", 1)
                ch_v "Maybe you could \"de-vampire\" me?"
                $ JubesX.add_word(1, "devamp", 0, 0, 0)
                menu:
                    extend ""
                    "You don't want to be a vampire":
                        call change_Girl_stat(JubesX, "love", 2)
                        call change_Girl_stat(JubesX, "obedience", 1)
                        ch_v "Well, no. . ."
                    "I guess.":
                        $ JubesX.change_face("confused", 1)
                        call change_Girl_stat(JubesX, "love", -1)
                        ch_v ". . ."
                ch_v "The powers are cool and all, but I can't even go out during the daytime!"
                ch_v "and the blood drinking, of course."
                $ JubesX.change_face("normal", 1)

                menu:
                    extend ""
                    "Of course.":
                        call change_Girl_stat(JubesX, "love", 2)
                        call change_Girl_stat(JubesX, "inhibition", 1)
                        ch_v ". . ."
                    "Yeah. . .":
                        call change_Girl_stat(JubesX, "obedience", 1)
                        call change_Girl_stat(JubesX, "inhibition", 1)
                        ch_v ". . ."


            "Are you a mutant?" if "mutant" not in JubesX.recent_history:
                call change_Girl_stat(JubesX, "love", 2)
                $ JubesX.change_face("smile", 1)
                ch_v "Yeah! Of course I am!"
                $ JubesX.change_face("smile", 1, eyes = "side")
                if "vamp" in JubesX.recent_history:
                    ch_v "You know, among other things. . ."
                else:
                    ch_v ". . . among other things. . ."
                $ JubesX.add_word(1, "mutant", 0, 0, 0)
                menu:
                    extend ""
                    "So what's your power?":
                        call change_Girl_stat(JubesX, "love", 3)
                        call change_Girl_stat(JubesX, "inhibition", 1)
                        ch_v ". . ."
                    "Oh, ok.":
                        call change_Girl_stat(JubesX, "love", -1)
                        call change_Girl_stat(JubesX, "obedience", 3)
                        $ JubesX.change_face("confused", 1)
                        ch_v "Not even curious about what I can do?"
                $ JubesX.change_face("smile", 1)
                ch_v "I can shoot fireworks."
                $ JubesX.arm_pose = 1
                show Fireworks as Fire1 onlayer black:
                    pos (JubesX.sprite_location+300,350)
                show Fireworks as Fire2 onlayer black:
                    pos (JubesX.sprite_location+300,350)
                ch_v "Pew pew!"
                menu:
                    extend ""
                    "Neat!":
                        call change_Girl_stat(JubesX, "love", 3)
                        call change_Girl_stat(JubesX, "inhibition", 5)
                        ch_v "Thanks!"
                    "K.":
                        call change_Girl_stat(JubesX, "obedience", 2)
                        call change_Girl_stat(JubesX, "inhibition", -1)
                        $ JubesX.change_face("angry", 1, eyes = "side")
                        ch_v "Ok, so it's not \"negating mutant powers\" cool or anything. . ."
                        ch_v "I can do other stuff. . ."
                        $ JubesX.change_face("normal", 1)
                    ". . .":
                        call change_Girl_stat(JubesX, "obedience", 2)
                        ch_v ". . ."
            "Well, I guess I'm out of questions.":


                $ JubesX.add_word(1, "thirst", 0, 0, 0)
                $ counter = 0

        if "thirst" in JubesX.recent_history and "vamp" not in JubesX.recent_history:
            "You feel a tickle on your neck and rub it, coming back with a trickle of blood on your fingers."
            menu:
                extend ""
                "Oh. Blood. . .":
                    call change_Girl_stat(JubesX, "love", 2)
                    call change_Girl_stat(JubesX, "obedience", 3)
                    call change_Girl_stat(JubesX, "inhibition", -2)
                    $ JubesX.change_face("angry", 1, eyes = "squint", mouth = "kiss")
                    ch_v "You are -remarkably- chill about this."
                    $ JubesX.change_face("smile", 1, eyes = "surprised", brows = "sad")
                    ch_v "Maybe I took too much? . ."
                "Why is my neck bleeding?":
                    call change_Girl_stat(JubesX, "love", 4)
                    call change_Girl_stat(JubesX, "obedience", 2)
                    $ JubesX.change_face("sadside", 1)
                    ch_v "Yeah. . . about that. . ."
                    ch_v "Sorry."
                "What the fuck?!":
                    call change_Girl_stat(JubesX, "love", -2)
                    call change_Girl_stat(JubesX, "obedience", 10)
                    call change_Girl_stat(JubesX, "inhibition", -2)
                    $ JubesX.change_face("startled", 2)
                    ch_v "Sorry! Sorry!"
                    $ JubesX.change_face("startled", 1)
                    ch_v "Let me explain!"
            $ JubesX.change_face("sadside", 1)
            ch_v "So. . . I'm. . . a vampire?"
            $ JubesX.add_word(1, "vamp", 0, 0, 0)
            menu:
                extend ""
                "This isn't a refreshment stand!":
                    call change_Girl_stat(JubesX, "love", 1)
                    call change_Girl_stat(JubesX, "obedience", 3)
                    call change_Girl_stat(JubesX, "inhibition", 1)
                    $ JubesX.change_face("sly", 1)
                    ch_v "Says you."
                "A vampire. . .":
                    ch_v ". . . Yeah. . ."
                "Oh. Gotcha.":
                    call change_Girl_stat(JubesX, "love", 2)
                    call change_Girl_stat(JubesX, "obedience", 2)
                    call change_Girl_stat(JubesX, "inhibition", -1)
                    $ JubesX.change_face("perplexed", 1)
                    ch_v "Maybe we should take you to the medbay. . ."
            $ counter += 1





    if "Jubilee" not in JubesX.names:
        call change_Girl_stat(JubesX, "love", -5)
        call change_Girl_stat(JubesX, "obedience", 10)
        $ JubesX.change_face("angry", 1)
        ch_v "Seriously? You don't even want to know my fucking name?"
        $ JubesX.change_face("sadside", 1, brows = "angry")
        ch_v "How many girls do you have going through this place?"
        ch_v ". . ."
        $ JubesX.change_face("angry", 1)
        ch_v "It's \"Jubilee,\" b-t-dubs."
        menu:
            extend ""
            "Where's a jubliee?":
                call change_Girl_stat(JubesX, "obedience", 1)
                call change_Girl_stat(JubesX, "inhibition", 1)
                ch_v "My -name- is Jubilee, dumbass."
            "Your name? Ok.":
                call change_Girl_stat(JubesX, "love", 3)
                call change_Girl_stat(JubesX, "obedience", 5)
                call change_Girl_stat(JubesX, "inhibition", 15)
                $ JubesX.change_face("smile", 1)
                ch_v "You catch on quick. . ."
            "Most nights are, yeah.":
                $ JubesX.change_face("confused", 1)
                ch_v "Wha. . . oh."
                call change_Girl_stat(JubesX, "love", 10)
                call change_Girl_stat(JubesX, "obedience", 5)
                call change_Girl_stat(JubesX, "inhibition", 15)
                $ JubesX.change_face("smile", 1)
                ch_v "Heh."
                ch_v "Ok, that's cool. No, I meant my -name- is Jubilee."
                ch_v "It's actually \"Jubilation Lee,\" but you know. . ."
        $ JubesX.name = "Jubilee"
        $ JubesX.names.append("Jubilation")
        $ JubesX.names.append("Miss Lee")
        $ JubesX.petnames.append("Miss Lee")
        ch_v "And I know your name's [Player.name], obviously."
    if "devamp" not in JubesX.recent_history:
        $ JubesX.change_face("sadside", 1)
        ch_v "Anyway, I just figured that maybe your blood could reverse this \"vampire\" thing."
    menu:
        extend ""
        "So do you feel any different?":
            call change_Girl_stat(JubesX, "love", 5)
            call change_Girl_stat(JubesX, "inhibition", 2)
            $ JubesX.change_face("smile", 1)
        ". . .":
            call change_Girl_stat(JubesX, "love", -2)
            call change_Girl_stat(JubesX, "obedience", 2)
            $ JubesX.change_face("perplexed", 1)
            ch_v "You don't even want to ask about the \"vampire\" thing?"
            menu:
                extend ""
                "Oh, yeah, how are you doing?":
                    call change_Girl_stat(JubesX, "love", 1)
                    call change_Girl_stat(JubesX, "inhibition", 1)
                    $ JubesX.change_face("smile", 1)
                "Not really.":
                    call change_Girl_stat(JubesX, "love", -3)
                    call change_Girl_stat(JubesX, "obedience", 3)
                    $ JubesX.change_face("angry", 1)
                    ch_v "Well that's a bad start!"
                "Oh, ok.":
                    $ JubesX.change_face("confused", 1)
                    ch_v ". . ."

    ch_v "I guess. . . not that much different."
    ch_v "Still have the teeth, the. . . thirst."
    $ JubesX.change_face("sadside", 1)
    ch_v "I guess I'm still a vampire."
    $ JubesX.change_face("normal", 1)
    ch_v "But I do feel a bit better. . ."
    $ JubesX.change_face("sad", 1)
    ch_v "I am sorry, I shouldn't have attacked you like that."
    ch_v "Not cool, I know."
    menu:
        extend ""
        "It's ok, I get it.":
            call change_Girl_stat(JubesX, "love", 5)
            call change_Girl_stat(JubesX, "obedience", -1)
            call change_Girl_stat(JubesX, "inhibition", 2)
            $ JubesX.change_face("smile", 1)
            ch_v "Thanks."
            ch_v "Is there any way I could make it up to you?"
        "Why not make it up to me?":
            call change_Girl_stat(JubesX, "obedience", 2)
            $ JubesX.change_face("sexy", 1)
            ch_v "Oh?"
        "How dare you!":
            call change_Girl_stat(JubesX, "obedience", 3)
            call change_Girl_stat(JubesX, "inhibition", -1)
            $ JubesX.change_face("surprised", 1)
            ch_v "I know! I know!"
            $ JubesX.change_face("smile", 1)
            ch_v "I can make it up to you!"
        ". . .":
            call change_Girl_stat(JubesX, "inhibition", 3)
            $ JubesX.change_face("sly", 1)
            ch_v "So. . . I guess I could make it up to you?"
    menu:
        extend ""
        "That's not necessary.":
            call change_Girl_stat(JubesX, "love", 5)
            call change_Girl_stat(JubesX, "inhibition", 1)
            $ JubesX.change_face("smile", 1)
            ch_v "That's sweet of you."
            ch_v "Seriously though, I'll think of something. . ."
        "A kiss, maybe?":
            call change_Girl_stat(JubesX, "love", 3)
            call change_Girl_stat(JubesX, "obedience", 3)
            call change_Girl_stat(JubesX, "inhibition", 2)
            $ JubesX.change_face("sly", 1)
            ch_v "I heard you're a charmer."
            ch_v "Well, I guess. . . one. . ."
            $ JubesX.change_face("kiss")
            show Jubes_sprite standing:
                ease 0.5 offset (0, 0) zoom 2
            pause 1
            show Jubes_sprite standing:
                ease 0.5 offset (100, 0) zoom 1.5
            $ JubesX.change_face("sly", 1)
            ch_v ". . ."
        "You could flash me?":
            call change_Girl_stat(JubesX, "obedience", 3)
            if approval_check(JubesX, 620):
                call change_Girl_stat(JubesX, "love", 2)
                call change_Girl_stat(JubesX, "inhibition", 1)
                $ JubesX.change_face("sly", 1)
                ch_v "I guess I could. . ."
                $ JubesX.change_face("smile", 1, mouth = "sucking")
            else:
                call change_Girl_stat(JubesX, "love", -2)
                call change_Girl_stat(JubesX, "obedience", 1)
                $ JubesX.change_face("angry", 1, mouth = "sucking")
            $ JubesX.arm_pose = 1
            show Fireworks as Fire1 onlayer black:
                pos (JubesX.sprite_location+250,350)
            show Fireworks as Fire2 onlayer black:
                pos (JubesX.sprite_location+250,350)
            ch_v "As if."
            $ JubesX.change_face("smile", 1)
        "A blowjob?":

            if approval_check(JubesX, 620):
                call change_Girl_stat(JubesX, "love", 1)
                call change_Girl_stat(JubesX, "obedience", 5)
                call change_Girl_stat(JubesX, "inhibition", 1)
                $ JubesX.change_face("smile", 1, mouth = "sucking")
            else:
                call change_Girl_stat(JubesX, "love", -5)
                call change_Girl_stat(JubesX, "obedience", 2)
                $ JubesX.change_face("angry", 1, mouth = "sucking")

            ch_v "Hey, I may suck more than most, but even I'm not that easy!"
            $ JubesX.change_face("smile", 1)
    ch_v "Anyway, I should get going before dawn."
    ch_v "I might see you around sometime."
    ch_v "In the moonlight. . ."

    $ JubesX.add_word(1, 0, 0, 0, "met")
    $ active_Girls.append(JubesX) if JubesX not in active_Girls else active_Girls

    call remove_Girl(JubesX)

    "[JubesX.name] leaves the room, you might as well get some sleep. . ."

    show black_screen onlayer black

    pause 2.0

    $ JubesX.history.append("met")

    $ active_Girls.append(JubesX)

    return
