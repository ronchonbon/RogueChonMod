init python:

    def meet_Kitty():
        label = meet_Kitty

        conditions = [
            "'met' not in KittyX.permanent_History.keys()",
            "Player.destination == 'bg_classroom'",
            "Player.traveling"]

        priority = True
        repeatable = False

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label meet_Kitty:
    call set_the_scene(location = "bg_campus", fade = True)

    "As you rush to class, you see another student running straight at you."
    "You try to move aside, but aren't fast enough to get out of her way, "

    $ KittyX.name = "???"
    $ KittyX.change_face("surprised")
    $ KittyX.location = Player.location
    $ KittyX.change_Outfit(instant = True)

    call get_color_transform
    $ color_transform = _return

    call show_Girl(KittyX, x_position = stage_center, color_transform = color_transform, transition = vpunch)
    $ shift_focus(KittyX)

    "She crashes into you at a full jog, and you both fall to the ground."
    "You scramble to your feet and offer the girl a hand up."
    ch_k "Hey!"

    $ KittyX.brows = "angry"
    call change_Girl_stat(KittyX, "love", -25)

    ch_k "What the hell was that?"

    menu:
        extend ""
        "You crashed into me!":
            $ KittyX.change_face("confused", blushing = 2)
            call change_Girl_stat(KittyX, "love", 5)
            call change_Girl_stat(KittyX, "obedience", 20)

            ch_k "Wha! Well, yeah. . ."

            $ KittyX.blushing = "_blush1"
            $ KittyX.mood += 1
        "Sorry about that.":
            $ KittyX.change_face("bemused", blushing = 1, eyes = "side")
            call change_Girl_stat(KittyX, "love", 25)

            ch_k "Well, I guess it[KittyX.like]wasn't entirely your fault. . ."
        "A meet-cute?":
            $ KittyX.change_face("surprised", blushing = 2)
            call change_Girl_stat(KittyX, "love", 15)
            call change_Girl_stat(KittyX, "inhibition", 10)

            ch_k " ! "

            $ KittyX.change_face("bemused", blushing = 1)

            ch_k "Hmm. . . maybe. . ."

    ch_p "My name's [Player.name], by the way."

    if not KittyX.mood:
        $ KittyX.change_face("smile", blushing = 1)

        ch_k "Mine's Kitty! Kitty Pryde. Nice to meet you!"
    else:
        $ KittyX.change_face("sadside", blushing = 1)

        ch_k "Um, mine's Kitty."

    $ KittyX.name = "Kitty"
    $ KittyX.change_face("normal", blushing = 1, mouth = "sad")

    menu:
        ch_k "I just[KittyX.like]didn't expect to bounce off you like that. Normally I can phase through things."
        "Losing your touch?":
            $ KittyX.change_face("confused", blushing = 0)
            call change_Girl_stat(KittyX, "obedience", 5)

            ch_k "I don't {i}think{/i} that's it. . ."
            ch_p "Just kidding. . ."

            call change_Girl_stat(KittyX, "love", 5)
        "Was I too distracting?":
            $ KittyX.change_face("angry", blushing = 1, brows = "normal")
            call change_Girl_stat(KittyX, "love", -2)
            call change_Girl_stat(KittyX, "obedience", 8)
            call change_Girl_stat(KittyX, "inhibition", 4)

            ch_k "Like, no."
            ch_p "Heh, I guess not."
        "It must be my powers.":
            $ KittyX.change_face("confused", blushing = 0)
            call change_Girl_stat(KittyX, "love", 5)

            ch_k "Oh?"

    ch_p "I have the ability to negate mutant powers, so you can't phase through me."

    $ KittyX.change_face("perplexed", blushing = 0)

    menu:
        ch_k "Oh! Wow, that's an interesting power. So if you grab me, I can't get away?"
        "Want to give it a try?":
            $ KittyX.change_face("perplexed")
            call change_Girl_stat(KittyX, "love", 5)
            call change_Girl_stat(KittyX, "inhibition", 5)

            ch_k "I'm definitely curious."
        "I guess so.":
            $ KittyX.change_face("sadside", mouth = "lipbite")
            call change_Girl_stat(KittyX, "obedience", 3)
            call change_Girl_stat(KittyX, "inhibition", 7)

            ch_k "I'd like to give it a try."
        "Does that turn you on?":
            $ KittyX.change_face("surprised", blushing = 2)
            call change_Girl_stat(KittyX, "obedience", 5)

            ch_k "What?! No! . ."

            $ KittyX.change_face("bemused", blushing = 1, eyes = "side")
            call change_Girl_stat(KittyX, "inhibition", 5)

            ch_k ". . . no."

            $ KittyX.eyes = "sexy"

            ch_k "But it is[KittyX.like]worth testing."

    ch_p "Ok, let's give it a shot."
    "You reach out and grab her wrist."

    $ KittyX.change_face("angry", blushing = 1, eyes = "down")

    "She struggles for a few moments to shake you free, but you hold firm."

    $ holding = True
    $ hugged = False
    $ counter = 0

    while holding:
        menu:
            extend ""
            "Let her go.":
                if not counter:
                    call change_Girl_stat(KittyX, "love", 7)
                    call change_Girl_stat(KittyX, "inhibition", -2)
                elif counter == 1:
                    call change_Girl_stat(KittyX, "love", 10)
                else:
                    call change_Girl_stat(KittyX, "love", 5)

                "You release her arm and step back."

                $ holding = False
            "Hold on.":
                "You continue to hold onto her arm and she fidgets uncomfortably."

                if not counter:
                    $ KittyX.eyes = "sexy"

                    ch_k "Are you[KittyX.like]going to let go of my arm any time soon?"
                elif counter == 1:
                    call change_Girl_stat(KittyX, "love", -1)
                    call change_Girl_stat(KittyX, "obedience", 2)
                else:
                    ch_k "Ok, that's enough!"

                    $ KittyX.eyes = "sexy"
                    call change_Girl_stat(KittyX, "love", -10)
                    call change_Girl_stat(KittyX, "obedience", -5)
                    call change_Girl_stat(KittyX, "inhibition", 10)
                    $ KittyX.mood += 1

                    "She reaches over and pries your hand loose."

                    $ holding = False

                    "Um. . ."

                $ counter += 1
            "Pull her in for a hug.":
                $ KittyX.change_face("surprised", blushing = 2)
                call change_Girl_stat(KittyX, "love", -5)

                ch_k "Hey! Like, not cool!"

                $ KittyX.change_face("angry", blushing = 1)
                $ KittyX.mood += 2

                call show_Girl(KittyX, transition = vpunch)

                "She elbows you in the ribs and shoves herself back a few steps."

                call change_Girl_stat(KittyX, "inhibition", 10)

                ch_k "My powers may not work on you, but I have[KittyX.like]a few years of combat experience on you."
                ch_k "And don't you forget it!"

                $ holding = False
                $ hugged = True

    if counter or hugged:
        $ KittyX.eyes = "side"

        ch_k "Still though, that was an interesting experience. . ."
    else:
        $ KittyX.change_face("bemused", blushing = 1, eyes = "side")

        ch_k "That was an interesting experience. . ."

    $ KittyX.eyes = "sexy"
    $ KittyX.mouth = "lipbite"

    ch_k "Kinda tingly. . ."

    $ KittyX.change_face("surprised")

    ch_k "Oh! I[KittyX.like]totally forgot, I have to get to a briefing!"

    if not KittyX.mood:
        $ KittyX.change_face("smile")

        ch_k "I'll see you later though! Like, bye!"
    else:
        $ KittyX.change_face("normal")

        ch_k "I'll see you around I guess. Like, bye!"

    call remove_Girl(KittyX)

    "She jogs off down the path, and you continue on to class."

    $ active_Girls.append(KittyX)

    $ KittyX.History.update("met")

    $ round -= 10

    return
