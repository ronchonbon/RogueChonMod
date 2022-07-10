

label Kitty_boyfriend:
    if KittyX.location != Player.location:
        if KittyX not in Player.Party:
            "[KittyX.name] approaches you and asks if the two of you can talk."
        else:
            "[KittyX.name] turns towards you and asks if the two of you can talk."

    call clear_the_room(KittyX)

    "A little blush on her cheeks, you can tell she's a bit anxious about whatever she has to say."

    $ KittyX.change_face("bemused", blushing = 1)

    ch_k "So, [KittyX.player_petname], we've[KittyX.like]been hanging for a while, right?"
    ch_k ". . ."

    $ KittyX.eyes = "sexy"

    menu:
        ch_k "Right?"
        "Yeah. And it's been amazing.":
            call change_Girl_stat(KittyX, "love", 20)
        "Yeah, I guess":
            call change_Girl_stat(KittyX, "love", 10)
        "Uhm. . .maybe?":
            call change_Girl_stat(KittyX, "love", -10)
            call change_Girl_stat(KittyX, "obedience", 30)

    if KittyX.SEXP >= 10:
        ch_k "I mean, I've gone further with you than I've ever been with anybody before. . ."

    if KittyX.SEXP >= 15:
        ch_k "You know[KittyX.like]. . .in the {i}bedroom{/i}. . ."

    if len(Player.Harem) > 1:
        ch_k "I know you[KittyX.like]really get around and all. . ."
    elif RogueX in Player.Harem:
        ch_k "I know you're kinda[KittyX.like][RogueX.name]'s boyfriend and all. . ."
    elif Player.Harem:
        ch_k "I know you're kinda[KittyX.like]dating [Player.Harem[0].name] and all. . ."

    if not Player.Harem and approval_check(KittyX, 750, "L"):
        ch_k "So, uhm. . ."
        ch_k "It’s not like I[KittyX.like]haven’t gone out with guys before."
        ch_k "I just[KittyX.like]wow, this is so awkward. I really like you a lot and. . ."
        ch_k "I mean. . . do you wanna[KittyX.like]be my boyfriend?"
        ch_k "[KittyX.Like]maybe we could make it official?"
    elif Player.Harem:
        ch_k "If you were okay with it. . . I’d still like to be your girlfriend, too."
    else:
        ch_k "I wish you weren’t[KittyX.like]such a jerk sometimes, but still. . . I’m totally serious about this."
        ch_k "I wanna be your girlfriend[KittyX.like]officially."

    menu:
        extend ""
        "Are you kidding? I'd love to!":
            call change_Girl_stat(KittyX, "love", 30)

            "[KittyX.name] wraps her arms around you and starts kissing you passionately."

            call kiss_launch(KittyX)

            $ KittyX.permanent_History["kiss"] += 1
        "Uhm[KittyX.like]okay.":
            $ KittyX.brows = "confused"

            "[KittyX.name] seems a little put off by how casually you’re taking all this."
            "Still, she must think it’s a good first step, at least, because she leans into you and gives you a hug."
        "I'm with someone else now." if Player.Harem:
            $ KittyX.change_face("sad", blushing = 1)

            menu:
                ch_k "I know. I just[KittyX.like]. . . I thought maybe you could go out with me, too, maybe?"
                "Yes. Absolutely.":
                    call change_Girl_stat(KittyX, "love", 30)

                    "[KittyX.name] wraps her arms around you and starts kissing you passionately."

                    call kiss_launch(KittyX)

                    $ KittyX.permanent_History["kiss"] += 1
                "She wouldn't understand." if len(Player.Harem) == 1:
                    $ line = "no"
                "They wouldn't be cool with that." if len(Player.Harem) > 1:
                    $ line = "no"
                "I'm sorry, but. . . no.":
                    $ line = "no"
                "No way.":
                    jump Kitty_boyfriend_bad_ending

            if line == "no":
                call change_Girl_stat(KittyX, "love", -10)

                ch_k "Well. . . okay. I get it."

                call remove_Girl(KittyX)

                return

        "Not really.":
            jump Kitty_boyfriend_bad_ending

    $ Player.Harem.append(KittyX)

    $ KittyX.change_face("sexy")
    $ KittyX.player_petnames.append("boyfriend")

    ch_k "Now. . . boyfriend. . . how about you and I[KittyX.like]celebrate, huh?"

    call enter_main_sex_menu(KittyX)

    return

label Kitty_boyfriend_bad_ending:
    $ KittyX.change_face("angry", blushing = 1)

    ch_k "Fine![KittyX.Like]. . .be that way!"

    call change_Girl_stat(KittyX, "love", -50)
    call change_Girl_stat(KittyX, "obedience", 40)

    if Player.location == RogueX.home:
        ch_k "Get out, you big jerk!"

        $ Player.traveling = True

        jump player_room
    else:
        call remove_Girl(KittyX)

        "[KittyX.name] storms off."

        $ KittyX.location = "bg_rogue"

    return

label Kitty_key:
    $ shift_focus(KittyX)
    call set_the_scene

    $ KittyX.change_face("bemused")
    $ KittyX.arm_pose = 2

    ch_k "So you've[KittyX.like]been dropping by a lot lately, I figured you might want a key. . ."
    ch_p "Thanks."

    $ KittyX.arm_pose = 1
    $ Player.Keys.append(KittyX)

    return





label Kitty_Love:


    $ shift_focus (KittyX)
    $ KittyX.drain_word("asked_to_meet")
    if KittyX.event_happened[6]:

        "[KittyX.name] seems kind of shy and shuffles up to you, as if working up her nerve."
    elif Player.location != "bg_kitty":
        if KittyX.location == Player.location or KittyX in Player.Party:
            "Suddenly, [KittyX.name] says she wants to talk to you in her room and drags you over there."
        else:
            "[KittyX.name] shows up, hurriedly says she wants to talk to you in her room and drags you over there."
        $ Player.location = "bg_kitty"
    else:
        "[KittyX.name] suddenly stares at you very intently."


    call set_the_scene
    call show_Girl (KittyX)
    call clear_the_room (KittyX)
    call set_Character_taboos
    $ KittyX.daily_history.append("relationship")
    $ KittyX.change_face("bemused", 1)
    $ KittyX.eyes = "side"
    $ line = 0
    $ KittyX.event_happened[6] += 1
    if KittyX.event_happened[6] == 1:
        if KittyX in Player.Harem:
            ch_k "We've[KittyX.like]been together for a while now, and I've been thinking. . ."
        else:
            ch_k "We've[KittyX.like]know each other for a while now, and I've been thinking. . ."
        ch_k "It's been[KittyX.like]kinda hard for me to really get invested in anyone. . ."
        $ KittyX.eyes = "down"
        ch_k ". . . to[KittyX.like]be comfortable with who they are and be myself. . ."
        $ KittyX.eyes = "squint"
        ch_k "I just feel like sometimes you. . ."
        $ KittyX.eyes = "side"
        ch_k "and me[KittyX.like] . ."
        $ KittyX.change_face("perplexed", 2)
        $ KittyX.eyes = "surprised"
        ch_k "Never mind!"
        "Kitty dashes off and phases through the nearest wall."

        call remove_Girl(KittyX)
        return
    if KittyX.event_happened[6] == 2:
        ch_k "Sorry about before, I don't think I was ready maybe. . ."
        ch_k ". . . but I was kind of thinking-"
    elif KittyX.event_happened[6] >= 5:
        ch_k "Um. . ."
        $ KittyX.eyes = "squint"
        ch_k "You know, it's time to stop running. I think I love you."
        $ KittyX.eyes = "side"
        ch_k "You don't have to say it back, but I do."
        $ KittyX.player_petnames.append("lover")
        ch_k "Um, that's all."
    else:
        ch_k "Um. . ."
    if "lover" not in KittyX.player_petnames:
        menu:
            "She turns and makes a break for the nearest wall."
            "Catch her":
                $ KittyX.change_face("perplexed", 2)
                $ KittyX.eyes = "surprised"
                call change_Girl_stat(KittyX, "love", 10)
                call change_Girl_stat(KittyX, "obedience", 15)
                "As she spins, you grab on to her wrist. She's slightly startled to have been caught."
            "Let her go":
                "She dashes through the nearest wall and vanishes from view."
                jump Kitty_Love_End
        $ KittyX.blushing = "_blush1"
        menu:
            extend ""
            "Pull her close":
                $ KittyX.change_face("smile", 1)
                call change_Girl_stat(KittyX, "love", 20)
                "You draw her into an embrace, arms wrapped tightly around her waist."
                $ line = "hug"
            "Stay like this":
                $ KittyX.eyes = "down"
                call change_Girl_stat(KittyX, "obedience", 10)
                "You keep hold of her wrist."
                $ line = "wrist"
            "Let her go":
                if 1 < KittyX.event_happened[6] < 4:
                    "You immediately release her wrist."
                    $ KittyX.eyes = "down"
                    "She dashes through the nearest wall and vanishes from view."
                    jump Kitty_Love_End
                else:
                    call change_Girl_stat(KittyX, "love", 10)
                    call change_Girl_stat(KittyX, "obedience", 20)
                    call change_Girl_stat(KittyX, "inhibition", 20)
                    "You release her wrist and she takes a step back."

        ch_k "I'm. . . I'm sorry, I just kind of panicked."
    if "lover" not in KittyX.player_petnames:

        ch_k "I thought maybe if I let myself get too close. . ."
        ch_k "I'd fall. . ."
        menu:
            extend ""
            "I'll never let go." if line:
                call change_Girl_stat(KittyX, "love", 20)
                call change_Girl_stat(KittyX, "inhibition", 10)
                "She melts into your arms."
            "I'd always catch you.":
                $ KittyX.change_face("smile")
                call change_Girl_stat(KittyX, "love", 20)
                call change_Girl_stat(KittyX, "obedience", 15)
                "She smiles and shifts a bit uncomfortably."
            "Yeah, you should watch out for that.":
                $ KittyX.change_face("angry", 1)
                $ KittyX.recent_history.append("angry")
                call change_Girl_stat(KittyX, "love", -20)
                call change_Girl_stat(KittyX, "obedience", 10)
                call change_Girl_stat(KittyX, "inhibition", 10)
                "She shoves you away and then stomps through the nearest wall."
                jump Kitty_Love_End
            "So get going. [[Give her a shove]":

                $ KittyX.change_face("surprised", 1)
                call change_Girl_stat(KittyX, "love", -50)
                call change_Girl_stat(KittyX, "obedience", 10)
                call change_Girl_stat(KittyX, "inhibition", 10)
                "You shove her through the nearest wall and then continue on you way."
                $ KittyX.recent_history.append("angry")
                call remove_Girl(KittyX)
                jump Kitty_Love_End

    if "lover" in KittyX.player_petnames:

        menu:
            extend ""
            "I love you too.":
                call change_Girl_stat(KittyX, "love", 40)
                call change_Girl_stat(KittyX, "inhibition", 50)
                $ KittyX.change_face("smile")
            "You love me?":
                $ KittyX.change_face("confused", 2)
                menu:
                    ch_k "But you don't love me?"
                    "Yeah, of course I do!":
                        call change_Girl_stat(KittyX, "love", 30)
                        call change_Girl_stat(KittyX, "inhibition", 60)
                        $ KittyX.change_face("smile")
                    "I mean, a little?":
                        call change_Girl_stat(KittyX, "obedience", 20)
                        call change_Girl_stat(KittyX, "inhibition", -10)
                        ch_k "That's not a \"yes.\" . ."
                        $ line = "awkward"
                    "Not really.":
                        call change_Girl_stat(KittyX, "love", -30)
                        call change_Girl_stat(KittyX, "obedience", 30)
                        call change_Girl_stat(KittyX, "inhibition", -30)
                        $ KittyX.change_face("angry", 2)
                        ch_k "Huh?!"
                        $ line = "awkward"
            "Huh.":
                call change_Girl_stat(KittyX, "love", -10)
                call change_Girl_stat(KittyX, "obedience", 10)
                call change_Girl_stat(KittyX, "inhibition", -20)
                menu:
                    ch_k "Huh?!"
                    "I mean, I love you too!":
                        call change_Girl_stat(KittyX, "love", 30)
                        call change_Girl_stat(KittyX, "inhibition", 10)
                        $ KittyX.change_face("smile")
                        ch_k "Way to pull out a last minute save there. . ."
                    "Well that's awkward.":
                        call change_Girl_stat(KittyX, "love", -20)
                        call change_Girl_stat(KittyX, "obedience", 30)
                        call change_Girl_stat(KittyX, "inhibition", -20)
                        $ KittyX.change_face("angry", 2)
                        $ line = "awkward"
            "Well that's awkward.":
                call change_Girl_stat(KittyX, "love", -30)
                call change_Girl_stat(KittyX, "obedience", 40)
                call change_Girl_stat(KittyX, "inhibition", -20)
                $ KittyX.change_face("perplexed", 2)
                $ line = "awkward"
    else:
        menu:
            extend ""
            "I love you, [KittyX.name].":
                call change_Girl_stat(KittyX, "love", 50)
                call change_Girl_stat(KittyX, "inhibition", 30)
                $ KittyX.change_face("smile")
                $ line = "love"
            "I think you're pretty great.":
                $ KittyX.change_face("confused")
                menu:
                    ch_k "But you don't love me?"
                    "Yeah, of course I do!":
                        call change_Girl_stat(KittyX, "love", 30)
                        call change_Girl_stat(KittyX, "obedience", 10)
                        call change_Girl_stat(KittyX, "inhibition", 20)
                        $ KittyX.change_face("smile")
                    "I mean, a little?":
                        if approval_check(KittyX, 1200, "OI"):
                            $ KittyX.change_face("sad")
                            call change_Girl_stat(KittyX, "love", -30)
                            call change_Girl_stat(KittyX, "obedience", 20)
                            call change_Girl_stat(KittyX, "inhibition", 10)
                            ch_k "But[KittyX.like]not \"nothing\". . ."
                        else:
                            $ line = "awkward"
                    "Not really.":
                        $ KittyX.change_face("sad")
                        if approval_check(KittyX, 1500, "OI"):
                            call change_Girl_stat(KittyX, "love", -30)
                            call change_Girl_stat(KittyX, "obedience", 30)
                            ch_k "Ouch. . ."
                        else:
                            $ line = "awkward"
            "I was thinking something more casual. . .":
                $ KittyX.change_face("sad")
                if approval_check(KittyX, 1200, "OI") or approval_check(KittyX, 700, "I"):
                    call change_Girl_stat(KittyX, "love", -30)
                    call change_Girl_stat(KittyX, "obedience", 20)
                    call change_Girl_stat(KittyX, "inhibition", 30)
                    ch_k "Close enough."
                else:
                    $ line = "awkward"

    if line == "awkward":
        if approval_check(KittyX, 700, "O"):
            ch_k "Fine, this doesn't have to be love."
        elif approval_check(KittyX, 700, "I"):
            ch_k "Fine, just sex it is."
        elif approval_check(KittyX, 1200, "OI"):
            ch_k "Fine, I can work with that."
        else:
            call change_Girl_stat(KittyX, "love", -50)
            call change_Girl_stat(KittyX, "obedience", 50)
            call change_Girl_stat(KittyX, "inhibition", -50)
            ch_k "Oh, well I mean if you don't love me-"
            ch_k "You don't have to love me, that's ok."
            ch_k "I'll, um. . . never mind."
            if not simulation:
                $ KittyX.recent_history.append("angry")
        $ KittyX.event_happened[6] = 20
    else:
        if line:

            "She squeezes you even tighter and makes a little whimper."
        else:
            "She dives into your arms with a little squeak."
        if "lover" not in KittyX.player_petnames:
            ch_k "I love you too. . ."
            ch_k "I think I have for a while now."
            $ KittyX.player_petnames.append("lover")

label Kitty_Love_End:
    if line == "awkward" or "lover" not in KittyX.player_petnames:

        call remove_Girl(KittyX)
        return
    ch_k "So I was thinking. . . did you want to . . ."
    if Player.location != "bg_player" and Player.location != "bg_kitty":
        ch_k "Wait, let's take this someplace more private. . ."
        $ Player.location = "bg_kitty"

        call set_the_scene
        call clear_the_room (KittyX)
        call set_Character_taboos
        ch_k "Ok, so like I was saying. . ."
    call change_Girl_stat(KittyX, "obedience", 10)
    $ Player.add_word(1, "interruption")
    menu:
        extend ""
        "Yeah, let's do this. . . [[have sex]":
            call change_Girl_stat(KittyX, "inhibition", 30)
            ch_k "Hmm. . ."
            if simulation:
                return True
            call start_Action(KittyX, "sex")
        "I have something else in mind. . .[[choose another activity]":
            $ KittyX.brows = "confused"
            call change_Girl_stat(KittyX, "obedience", 20)
            ch_k "Something like. . ."
            if simulation:
                return True
            $ approval_bonus = 20
            call enter_main_sex_menu(KittyX)
    return

label Kitty_Love_Redux:

    $ line = 0
    $ KittyX.daily_history.append("relationship")
    if KittyX.event_happened[6] >= 25:

        ch_p "I hope you've forgiven me, I still love you."
        call change_Girl_stat(KittyX, "love", 10)
        if approval_check(KittyX, 950, "L"):
            $ line = "love"
        else:
            $ KittyX.change_face("sad")
            ch_k "You've dug too deep a hole, [KittyX.player_petname]."
            ch_k "Keep trying though."
    else:
        ch_p "Remember when I told you that I didn't love you?"
        $ KittyX.change_face("perplexed", 1)
        ch_k "Um, YEAH?!"
        menu:
            "I'm sorry, I didn't mean it.":
                $ KittyX.eyes = "surprised"
                ch_k "Well, if you. . . so wait, you {i}do{/i} love me?"
                ch_p "Yeah. I mean, yes, I love you, Kitty."
                call change_Girl_stat(KittyX, "love", 10)
                if approval_check(KittyX, 950, "L"):
                    $ line = "love"
                else:
                    $ KittyX.change_face("sadside")
                    ch_k "Well, I don't know how I feel at this point. . ."
            "I've changed my mind, so. . .":
                if approval_check(KittyX, 950, "L"):
                    $ line = "love"
                    $ KittyX.eyes = "surprised"
                    ch_k "Really?!"
                else:
                    $ KittyX.mouth = "sad"
                    ch_k "Oh, you've changed your mind. Wonderful."
                    call change_Girl_stat(KittyX, "inhibition", 10)
                    $ KittyX.change_face("sadside")
                    ch_k "Maybe I have too. . ."
            "Um, never mind.":
                call change_Girl_stat(KittyX, "love", -30)
                call change_Girl_stat(KittyX, "obedience", 10)
                $ KittyX.change_face("angry")
                ch_k "Seriously?"
                $ KittyX.recent_history.append("angry")
    if line == "love":
        call change_Girl_stat(KittyX, "love", 40)
        call change_Girl_stat(KittyX, "obedience", 10)
        call change_Girl_stat(KittyX, "inhibition", 10)
        $ KittyX.change_face("smile")
        ch_k "I[KittyX.like]love you too!"
        if KittyX.event_happened[6] < 25:
            $ KittyX.change_face("sly")
            "She slugs you in the arm"
            ch_k "Took you long enough."
        $ KittyX.player_petnames.append("lover")
    $ KittyX.event_happened[6] = 25
    return





label Kitty_Sub:
    $ shift_focus (KittyX)
    $ KittyX.drain_word("asked_to_meet")
    if KittyX.location != Player.location and KittyX not in Player.Party:
        "Suddenly, [KittyX.name] shows up and says she needs to talk to you."


    call set_the_scene
    call show_Girl (KittyX)
    call clear_the_room (KittyX)
    call set_Character_taboos
    $ KittyX.daily_history.append("relationship")
    $ KittyX.change_face("bemused", 1)

    $ line = 0
    ch_k "So, uhm. . .you've really kinda[KittyX.like]taken control in our relationship lately."
    menu:
        extend ""
        "I guess. That's just kind of what comes naturally for me.":
            call change_Girl_stat(KittyX, "obedience", 10)
            call change_Girl_stat(KittyX, "inhibition", 5)
        "Sorry. I didn't mean to come off like that.":
            $ KittyX.change_face("startled", 2)
            call change_Girl_stat(KittyX, "love", 5)
            call change_Girl_stat(KittyX, "obedience", -5)
            call change_Girl_stat(KittyX, "inhibition", -5)
            ch_k "No! Don't get the wrong idea! I just. . ."
        "Yup. Deal with it.":
            if approval_check(KittyX, 1000, "LO"):
                call change_Girl_stat(KittyX, "obedience", 20)
                call change_Girl_stat(KittyX, "inhibition", 10)
                ch_k "Um, yeah. . ."
            else:
                call change_Girl_stat(KittyX, "love", -10)
                call change_Girl_stat(KittyX, "obedience", 10)
                call change_Girl_stat(KittyX, "inhibition", 5)
                $ KittyX.change_face("angry")
                ch_k "I {i}was{/i} going to tell you I kinda liked it. But I didn't think you'd be[KittyX.like]a {i}jerk{/i} about it!"
                menu:
                    extend ""
                    "Guess you don't know me so well, huh?":
                        ch_k "I guess not."
                        $ line = "rude"
                    "Sorry. I kind of thought you were getting into me being like that.":
                        $ KittyX.change_face("sexy", 2)
                        $ KittyX.eyes = "side"
                        call change_Girl_stat(KittyX, "love", 5)
                        call change_Girl_stat(KittyX, "obedience", 5)
                        call change_Girl_stat(KittyX, "inhibition", 5)
                        ch_k ". . ."

    $ KittyX.blushing = "_blush1"
    if not line:

        ch_k "Well, I've, uhm. . . never had a guy be like that with me before. . ."
        $ KittyX.change_face("sly", 2)
        ch_k "I think I kinda like it."
        $ KittyX.change_face("smile", 1)
        menu:
            extend ""
            "Good. If you wanna be with me, that's how it'll be.":
                if approval_check(KittyX, 1000, "LO"):
                    call change_Girl_stat(KittyX, "obedience", 15)
                    call change_Girl_stat(KittyX, "inhibition", 10)
                    ch_k "I guess I walked into that one. . ."
                else:
                    $ KittyX.change_face("sadside", 1)
                    call change_Girl_stat(KittyX, "love", -5)
                    call change_Girl_stat(KittyX, "obedience", 10)
                    ch_k "You don't have to do it[KittyX.like]{i}all{/i} the time. You could still be nice once in a while."
                    menu:
                        extend ""
                        "Whatever. That's how it is. Take it or leave it.":
                            $ KittyX.change_face("angry")
                            call change_Girl_stat(KittyX, "love", -10)
                            call change_Girl_stat(KittyX, "obedience", 5)
                            ch_k "Y'know, you're such a jerk, [Player.name]!"
                            $ line = "rude"
                        "I think I could maybe do that.":
                            $ KittyX.change_face("bemused", 2)
                            $ KittyX.eyes = "side"
                            call change_Girl_stat(KittyX, "love", 5)
                            call change_Girl_stat(KittyX, "obedience", 3)
                            call change_Girl_stat(KittyX, "inhibition", 5)
                            ch_k "Uhm. . .yeah. It's[KittyX.like]. . kinda hot."
            "Yeah? You think it's sexy?":

                $ KittyX.change_face("bemused", 2)
                $ KittyX.eyes = "side"
                call change_Girl_stat(KittyX, "obedience", 5)
                call change_Girl_stat(KittyX, "inhibition", 10)
                ch_k "Uhm. . .yeah. It's[KittyX.like]. . kinda hot."
            "You sure you don't want me to back off a little?":

                $ KittyX.change_face("startled", 1)
                call change_Girl_stat(KittyX, "obedience", -5)
                menu:
                    ch_k "Only if you think it might be[KittyX.like]weird. But I think it's kinda hot."
                    "Only if you're okay with it.":
                        $ KittyX.change_face("bemused", 2)
                        call change_Girl_stat(KittyX, "love", 10)
                        call change_Girl_stat(KittyX, "inhibition", 10)
                        $ line = 0
                    "Uhm. . .yeah. I {i}do{/i} think it's weird. Sorry.":
                        call change_Girl_stat(KittyX, "love", -15)
                        call change_Girl_stat(KittyX, "obedience", -5)
                        call change_Girl_stat(KittyX, "inhibition", -10)
                        $ line = "embarrassed"
            "I don't really care what you like. I do what I want.":

                call change_Girl_stat(KittyX, "love", -10)
                call change_Girl_stat(KittyX, "obedience", 15)
                $ KittyX.change_face("angry")
                ch_k "Y'know, you're such a jerk, [Player.name]!"
                $ line = "rude"

    if not line:
        $ KittyX.change_face("bemused", 1)
        $ KittyX.eyes = "down"
        ch_k "Cool. So. . .just so you know. . .I don't mind[KittyX.like]you being in control."
        if "256 Shades of Grey" in KittyX.inventory:
            ch_k "Like in that '256 Shades of Grey' book."
        menu Kitty_Sub_Choice:
            extend ""
            "Don't you think that relationship's kinda. . .weird?":
                call change_Girl_stat(KittyX, "love", -5)
                call change_Girl_stat(KittyX, "inhibition", -15)
                $ line = "embarrassed"
            "I think I could get used to that kinda thing.":
                call change_Girl_stat(KittyX, "obedience", 5)
                call change_Girl_stat(KittyX, "inhibition", 5)
                $ KittyX.change_face("smile", 1)
                $ line = 0
            "You actually {i}read{/i} that?" if "256 Shades of Grey" in KittyX.inventory and line != "grey":
                call change_Girl_stat(KittyX, "love", 5)
                $ KittyX.change_face("sly", 1)
                ch_k "You think I wouldn't read something you bought me? I think you {i}maybe{/i} don't realize how much I like you."
                call change_Girl_stat(KittyX, "inhibition", 5)
                ch_k "Well, I {i}did{/i} read it. And. . .it turns out it kinda[KittyX.like]. . {i}really{/i} turned me on."
                ch_k "So. . .what d'you think? Think[KittyX.like]maybe you'd like that?"
                $ line = "grey"
                jump Kitty_Sub_Choice

    if not line:
        $ KittyX.change_face("smile", 1)
        ch_k "Awesome. So. . .if you wanted me to, I could[KittyX.like]call you {i}sir{/i} or something."
        $ KittyX.change_face("sly", 2)
        ch_k "Think you'd like that?"
        $ KittyX.blushing = "_blush1"
        menu:
            extend ""
            "That has a nice ring to it.":
                call change_Girl_stat(KittyX, "love", 5)
                call change_Girl_stat(KittyX, "obedience", 15)
                call change_Girl_stat(KittyX, "inhibition", 5)
                ch_k "Okay, then. . .{i}sir{/i}."
                $ KittyX.player_petname = "sir"
            "I think I'd rather stick with what we've got going.":
                $ KittyX.change_face("startled", 2)
                ch_k "Oh!"
                call change_Girl_stat(KittyX, "inhibition", -5)
                $ KittyX.change_face("sadside", 1)
                menu:
                    ch_k ". . . Well. . . maybe you can still kinda[KittyX.like]be in control, anyway?"
                    "I like that idea.":
                        call change_Girl_stat(KittyX, "obedience", 10)
                        $ KittyX.change_face("smile", 1)
                        ch_k "You're so awesome, [KittyX.player_petname]."
                    "This is getting really weird.":
                        call change_Girl_stat(KittyX, "love", -10)
                        call change_Girl_stat(KittyX, "obedience", -50)
                        call change_Girl_stat(KittyX, "inhibition", -15)
                        $ line = "embarrassed"


    $ KittyX.history.append("sir")
    if not line:
        $ KittyX.blushing = "_blush1"
        $ KittyX.player_petnames.append("sir")

    elif line == "rude":

        call remove_Girl(KittyX)
        if not simulation:
            $ renpy.pop_call()
        "[KittyX.name] phases through the floor in a huff, leaving you alone."
    elif line == "embarrassed":
        $ KittyX.change_face("sadside", 2)
        ch_k "Oh! Uhm, yeah! [KittyX.Like]I mean. . ."
        $ KittyX.mouth = "smile"
        ch_k "I was just kidding. I[KittyX.like]. . yeah. That's kinda weird."
        ch_k "I should go. I think I hear Professor Xavier calling me."
        $ KittyX.blushing = "_blush1"

        call remove_Girl(KittyX)
        if not simulation:
            $ renpy.pop_call()
        "[KittyX.name] phases through the floor, leaving you alone. It didn't look like she could get away fast enough."
    return

label Kitty_Sub_Asked:
    $ line = 0
    $ KittyX.change_face("sadside", 1)
    ch_k "Yeah. And I also[KittyX.like]remember what a {i}jerk{/i} you were to me about it."
    menu:
        extend ""
        "Well, I wanted to say I was sorry. And I was hoping maybe we could give it another shot.":
            if "sir" in KittyX.player_petnames and approval_check(KittyX, 850, "O"):

                pass
            elif approval_check(KittyX, 550, "O"):

                pass
            else:
                ch_k "Well maybe {i}I'm{/i}[KittyX.like]over that. . ."
                $ line = "rude"

            if line != "rude":
                call change_Girl_stat(KittyX, "love", 10)
                $ KittyX.change_face("sly", 1)
                ch_k "Well. . .okay. I {i}did{/i} think that was pretty hot. Also, you're super-cute when you apologize."
                call Kitty_Kissing_Smooch
                ch_k "Okay. We can[KittyX.like]try again."
        "Listen. . . I know it's what you want. Do you want to try again, or not?":

            $ KittyX.change_face("bemused", 1)
            if "sir" in KittyX.player_petnames:
                if approval_check(KittyX, 850, "O"):
                    ch_k "Ok, fine."
                else:
                    ch_k "Um, not really."
                    $ line = "rude"
            elif approval_check(KittyX, 600, "O"):

                $ KittyX.change_face("sadside", 1)
                ch_k "You're[KittyX.like]totally impossible."
                $ KittyX.eyes = "squint"
                ch_k "Maybe you're right."
                ch_k "But I still think you should[KittyX.like] apologize for being a jerk to me."
                menu:
                    extend ""
                    "Okay, I'm sorry I was mean about it.":
                        call change_Girl_stat(KittyX, "love", 15)
                        call change_Girl_stat(KittyX, "inhibition", 10)
                        $ KittyX.change_face("bemused", 1)
                        $ KittyX.eyes = "side"
                        ch_k "That's all you had to say."
                    "Not gonna happen.":
                        if "sir" in KittyX.player_petnames and approval_check(KittyX, 900, "O"):
                            call change_Girl_stat(KittyX, "love", -5)
                            call change_Girl_stat(KittyX, "obedience", 10)
                            ch_k ". . ."
                        elif approval_check(KittyX, 650, "O"):
                            call change_Girl_stat(KittyX, "love", -5)
                            call change_Girl_stat(KittyX, "obedience", 10)
                            ch_k "I, um. . ."
                        else:
                            call change_Girl_stat(KittyX, "love", -10)
                            call change_Girl_stat(KittyX, "obedience", -10)
                            call change_Girl_stat(KittyX, "obedience", -10)
                            call change_Girl_stat(KittyX, "inhibition", -15)
                            "Kitty sighs and rolls her eyes."
                            $ KittyX.change_face("angry", 1)
                            $ KittyX.eyes = "side"
                            ch_k "You really don't learn, do you?"
                            $ line = "rude"
                    "Ok, never mind then.":
                        $ KittyX.change_face("angry", 1)
                        call change_Girl_stat(KittyX, "love", -10)
                        call change_Girl_stat(KittyX, "obedience", -10)
                        call change_Girl_stat(KittyX, "obedience", -10)
                        call change_Girl_stat(KittyX, "inhibition", -15)
                        ch_k "Y'know, if you're gonna throw that in my face, forget it."
                        ch_k "I should've[KittyX.like]expected you'd be like that."
                        $ line = "rude"

    $ KittyX.recent_history.append("asked sub")
    $ KittyX.daily_history.append("asked sub")
    if line == "rude":


        call remove_Girl(KittyX)
        $ KittyX.recent_history.append("angry")
        if not simulation:
            $ renpy.pop_call()
        "[KittyX.name] phases through the floor, leaving you alone. She looked pretty upset."
    elif "sir" in KittyX.player_petnames:

        call change_Girl_stat(KittyX, "obedience", 50)
        $ KittyX.player_petnames.append("master")
        $ KittyX.player_petname = "master"
        $ KittyX.eyes = "squint"
        ch_k ". . . master. . ."
    else:

        call change_Girl_stat(KittyX, "obedience", 30)
        $ KittyX.player_petnames.append("sir")
        $ KittyX.player_petname = "sir"
        $ KittyX.eyes = "squint"
        ch_k ". . . sir."
    return






label Kitty_Master:
    $ shift_focus (KittyX)
    $ KittyX.drain_word("asked_to_meet")
    if KittyX.location != Player.location and KittyX not in Player.Party:
        "Suddenly, [KittyX.name] shows up and says she needs to talk to you."


    call set_the_scene
    call show_Girl (KittyX)
    call clear_the_room (KittyX)
    $ KittyX.daily_history.append("relationship")
    call set_Character_taboos
    $ line = 0
    $ KittyX.change_face("bemused", 1)
    ch_k "[KittyX.player_petname], if you don't mind me saying so. . ."
    ch_k "I think having you be[KittyX.like]in control of our relationship is working out pretty awesome."
    menu:
        extend ""
        "I like it too.":
            $ KittyX.change_face("sly", 1)
            ch_k "Cool. Maybe we could[KittyX.like]kick it up a notch?"
            menu:
                extend ""
                "Nah. This is just about perfect.":
                    $ KittyX.change_face("sad", 1)
                    call change_Girl_stat(KittyX, "obedience", -15)
                    call change_Girl_stat(KittyX, "inhibition", 10)
                    ch_k "Oh. Well, okay, I guess."
                    $ line = "fail"
                "What'd you have in mind?":
                    $ KittyX.eyes = "side"
                    ch_k "I dunno. I was thinking[KittyX.like]maybe I could start calling you. . . {i}master{/i}?"
                    $ KittyX.eyes = "squint"
                    ch_k "Would you like that? I think that'd be kinda[KittyX.like]hot."
                    menu:
                        extend ""
                        "Oh, yeah. I'd like that.":
                            ch_k "Cool. . ."
                        "Uhm. . .nah. That's too much.":
                            $ KittyX.change_face("sad", 1)
                            call change_Girl_stat(KittyX, "obedience", -15)
                            call change_Girl_stat(KittyX, "inhibition", 5)
                            ch_k "Oh. Well, okay, I guess."
                            $ line = "fail"
                "Actually, I'd prefer we stopped doing it. I don't want to be too controlling.":

                    $ KittyX.change_face("sly", 1)
                    call change_Girl_stat(KittyX, "love", 15)
                    call change_Girl_stat(KittyX, "obedience", -10)
                    call change_Girl_stat(KittyX, "inhibition", 10)
                    ch_k "Aw, I guess I can't get mad about that. . ."
                    $ line = "fail"
                "Actually, let's stop that. It's creeping me out.":

                    $ KittyX.change_face("perplexed", 2)
                    call change_Girl_stat(KittyX, "love", -10)
                    call change_Girl_stat(KittyX, "obedience", -50)
                    call change_Girl_stat(KittyX, "inhibition", -15)
                    ch_k "Oh. Sorry. I guess I got[KittyX.like]carried away with it."
                    $ KittyX.blushing = "_blush1"
                    $ line = "embarrassed"
        "As if I care what you think, slut.":

            $ KittyX.change_face("sad", 1)
            call change_Girl_stat(KittyX, "love", -20)
            call change_Girl_stat(KittyX, "obedience", 10)
            call change_Girl_stat(KittyX, "inhibition", -10)
            menu:
                ch_k "Excuse me?"
                "Sorry. I just don't care what you want.":
                    if approval_check(KittyX, 1400, "LO"):
                        call change_Girl_stat(KittyX, "obedience", 10)
                        ch_k "That's so. . ."
                        $ KittyX.change_face("sly", 1)
                        call change_Girl_stat(KittyX, "love", 20)
                        call change_Girl_stat(KittyX, "inhibition", 15)
                        ch_k ". . .{i}mean!{/i}"
                    else:
                        call change_Girl_stat(KittyX, "love", -15)
                        call change_Girl_stat(KittyX, "obedience", -10)
                        call change_Girl_stat(KittyX, "inhibition", 5)
                        $ KittyX.change_face("angry", 1)
                        ch_k "!!!"
                        $ line = "rude"
                "Sorry. I'm just trying to do the \"control\" thing. I thought you'd like it. Too much?":

                    call change_Girl_stat(KittyX, "love", 10)
                    call change_Girl_stat(KittyX, "obedience", 10)
                    call change_Girl_stat(KittyX, "inhibition", 5)
                    ch_k "Oh, okay. Just. . .try not to be so[KittyX.like]mean about it, 'kay?"
        "Not me. It's kind of creepy.":

            $ KittyX.change_face("sad", 2)
            call change_Girl_stat(KittyX, "love", -10)
            call change_Girl_stat(KittyX, "obedience", -20)
            call change_Girl_stat(KittyX, "inhibition", -25)
            ch_k "Oh. Uhm. . .never mind, then."
            $ line = "embarrassed"

    $ KittyX.history.append("master")
    if line == "rude":
        $ KittyX.recent_history.append("angry")

        call remove_Girl(KittyX)
        if not simulation:
            $ renpy.pop_call()
        "[KittyX.name] phases through the floor in a huff. She might have been crying."
    elif line == "embarrassed":

        call remove_Girl(KittyX)
        if not simulation:
            $ renpy.pop_call()
        "[KittyX.name] phases through the floor, leaving you alone. She looked really embarrassed."
    elif line != "fail":
        call change_Girl_stat(KittyX, "obedience", 50)
        $ KittyX.player_petnames.append("master")
        $ KittyX.player_petname = "master"
        ch_k ". . .master."
    return






label Kitty_Sexfriend:

    call set_the_scene
    call show_Girl (KittyX)
    call clear_the_room (KittyX)
    $ KittyX.daily_history.append("relationship")
    call set_Character_taboos
    $ line = 0
    $ KittyX.change_face("bemused", 1)
    ch_k "So, [KittyX.player_petname]. . .you[KittyX.like]got a second?"
    menu:
        extend ""
        "Not really.":
            $ KittyX.change_face("angry", 1)
            ch_k "You're such a jerk, [Player.name]!"
            call change_Girl_stat(KittyX, "love", -20)
            call change_Girl_stat(KittyX, "obedience", 3)
            $ line = "rude"
        "This doesn't sound good.":

            $ KittyX.change_face("perplexed", 1)
            ch_k "I promise. It's nothing[KittyX.like]bad."
        "Yeah. What's up?":

            pass

    if not line:
        if approval_check(KittyX, 850, "L"):
            $ KittyX.change_face("bemused", 1)
            ch_k "Well. . . I really like you. You know that, right?"
            menu:
                extend ""
                "I was kinda hoping.":
                    $ KittyX.change_face("sexy", 1)
                    call change_Girl_stat(KittyX, "love", 10)
                    call change_Girl_stat(KittyX, "inhibition", 5)
                    ch_k "I was {i}really{/i} hoping you'd say that [KittyX.player_petname]."
                "Really?":

                    ch_k "Uhm. . . [KittyX.like]yeah. I really do."
                "Ugh. Gross":

                    $ KittyX.change_face("angry", 1)
                    call change_Girl_stat(KittyX, "love", -10)
                    call change_Girl_stat(KittyX, "obedience", 5)
                    call change_Girl_stat(KittyX, "inhibition", -5)
                    ch_k "Y'know, you're such an ass, [Player.name]!"
                    $ line = "rude"

        elif approval_check(KittyX, 1000, "LI"):
            $ KittyX.change_face("sexy", 1)
            ch_k "I just wanted to tell you. . .I think you're[KittyX.like]kinda cute."
            menu:
                extend ""
                "That's really nice of you to say.":
                    call change_Girl_stat(KittyX, "love", 5)
                    call change_Girl_stat(KittyX, "inhibition", 5)
                    ch_k "Well, I really mean it."
                "Me? You really think so?":

                    ch_k "Yeah. I {i}really{/i} do."
                "Are you going somewhere with this?":

                    $ KittyX.change_face("angry")
                    ch_k "Well not anymore, I'm not!"
                    $ line = "rude"
        else:

            $ KittyX.mouth = "smile"
            $ KittyX.brows = "sad"
            $ KittyX.eyes = "side"
            ch_k "This is gonna sound[KittyX.like]really weird."
            menu:
                extend ""
                "Well, you've got me intrigued. Now you {i}have{/i} to tell me.":
                    ch_k "Promise you won't think[KittyX.like]{i}badly{/i}of me?"
                    menu:
                        extend ""
                        "[KittyX.name]. . . I really like you. I promise.":
                            $ KittyX.change_face("smile")
                            call change_Girl_stat(KittyX, "love", 10)
                            call change_Girl_stat(KittyX, "inhibition", 5)
                            ch_k "Well. . . okay."
                        "Uhm. . . okay?":

                            ch_k "Well. . ."
                        "No promises.":

                            $ KittyX.change_face("perplexed", 2)
                            call change_Girl_stat(KittyX, "inhibition", -5)
                            ch_k "Uhm. . . never mind, then."
                            $ line = "embarrassed"
                "Uhm, I think I've had my fill of {i}weird{/i}, thanks":

                    $ KittyX.change_face("angry", 1)
                    ch_k "Fine. [KittyX.like]whatever."
                    $ line = "rude"
    if KittyX in Player.Harem:
        $ line = "harem"
    if not line:
        ch_k "Anyway. . . I was[KittyX.like]kinda thinking. . . we get along pretty well, right?"
        menu:
            extend ""
            "Right. . . ":
                pass
            "Okay. Just stop. You're creeping me out.":
                $ KittyX.change_face("perplexed", 2)
                call change_Girl_stat(KittyX, "love", -10)
                call change_Girl_stat(KittyX, "inhibition", -10)
                ch_k "Sorry. I knew this was a mistake."
                $ line = "embarrassed"

    if not line:
        ch_k "And we've[KittyX.like]known each other for a little while, right?"
        menu:
            extend ""
            "Right. . . ":
                pass
            "Okay. Just stop. You're creeping me out.":
                $ KittyX.change_face("perplexed", 2)
                call change_Girl_stat(KittyX, "love", -10)
                call change_Girl_stat(KittyX, "inhibition", -10)
                ch_k "Sorry. I knew this was a mistake."
                $ line = "embarrassed"
    if not line:
        ch_k "Well. . . I was just kinda thinking. . . "
        ch_k "[KittyX.like]we could take our relationship a little further, if you wanted to."
        menu:
            extend ""
            "You mean. . . like, being {i}friends with benefits{/i}?":
                ch_k "Kinda, yeah. Whaddya think?"
                menu:
                    extend ""
                    "Sounds amazing! Count me in.":
                        $ KittyX.change_face("smile", 1)
                        call change_Girl_stat(KittyX, "love", 10)
                        call change_Girl_stat(KittyX, "obedience", 10)
                        call change_Girl_stat(KittyX, "inhibition", 50)
                        call change_Girl_stat(KittyX, "lust", 5)
                        "Kitty leans in and gives you a gentle kiss on the cheek."
                        ch_k "I can't wait to get started, [KittyX.player_petname]."
                    "That may be the sluttiest thing I've ever heard in my life.":

                        $ KittyX.change_face("angry", 1)
                        call change_Girl_stat(KittyX, "love", -30)
                        call change_Girl_stat(KittyX, "obedience", 10)
                        call change_Girl_stat(KittyX, "inhibition", -40)
                        ch_k "You're the biggest asshole[KittyX.like]ever, [KittyX.player_petname]!"
                        $ line = "rude"
            "Uhm, to be honest, I'd rather not.":

                $ KittyX.change_face("sadside", 2)
                call change_Girl_stat(KittyX, "obedience", 15)
                call change_Girl_stat(KittyX, "inhibition", -15)
                ch_k "Oh. Okay."
                ch_k "I[KittyX.like]think I should go now. I've got[KittyX.like]stuff to do."
                $ line = "sad"
    if line == "harem":
        ch_k "I am -totally- addicted to this dick. . ."
        $ line = 0
    if line == "rude":
        $ KittyX.change_face("angry", 1)
        $ KittyX.recent_history.append("angry")
        call change_Girl_stat(KittyX, "love", -20)
        call change_Girl_stat(KittyX, "obedience", 5)
        call change_Girl_stat(KittyX, "inhibition", -10)
        call remove_Girl(KittyX)
        $ KittyX.recent_history.append("angry")
        "[KittyX.name] storms off in a huff. She seemed pretty mad at you."
    elif line == "embarrassed":
        $ KittyX.change_face("perplexed", 1)
        call change_Girl_stat(KittyX, "love", -10)
        call change_Girl_stat(KittyX, "obedience", 5)
        call change_Girl_stat(KittyX, "inhibition", -20)
        call remove_Girl(KittyX, transition = easeoutbottom)
        "[KittyX.name] phases through the floor leaving you alone. That was very strange."
    elif line == "sad":
        call remove_Girl(KittyX, transition = easeoutbottom)
        "[KittyX.name] phases through the floor leaving you alone. You think you may have hurt her feelings."
    else:
        $ KittyX.player_petnames.append("sex friend")
        $ KittyX.change_face("sly", 2)
        call change_Girl_stat(KittyX, "inhibition", 10)
        call change_Girl_stat(KittyX, "lust", 10)
        "[KittyX.name] leans in and passes her hand across your body."
        "As she does so, she phases her hand through your jeans, so her fingers slide along your bare skin."
        $ KittyX.blushing = "_blush1"
        ch_k "I'll definitely be seeing {i}you{/i} later, [KittyX.player_petname]."
        call remove_Girl(KittyX)
        "She passes through a nearby wall. "
    call remove_Girl(KittyX)
    return








label Kitty_Fuckbuddy:
    $ KittyX.daily_history.append("relationship")
    $ KittyX.drain_word("asked_to_meet")
    "Out of nowhere, you feel a hand stroking across your cock."
    "Even though you're fully dressed, it definitely feels like soft skin touching your own."
    "You glance down and see a slender arm snaked around your waist, before vanishing into your pants."
    "As you try to control your rising erection, a voice whispers into your ear, "
    ch_k "Any time, just let me know. . ."
    "-and suddenly the pressure is gone."
    "Looking around, you don't see anyone nearby, and it doesn't look like anyone else noticed what happened."
    "Maybe you'll check up on [KittyX.name] later. . ."
    $ KittyX.player_petnames.append("fuck buddy")
    $ KittyX.event_happened[10] += 1
    return






label Kitty_Daddy:
    $ KittyX.daily_history.append("relationship")
    $ KittyX.drain_word("asked_to_meet")
    $ shift_focus (KittyX)
    call set_the_scene
    ch_k ". . ."
    if KittyX in Player.Harem:
        ch_k "Hey, so[KittyX.like]we've been dating, "
    else:
        ch_k "Hey, so[KittyX.like]we've been hanging out, "
    if KittyX.love > KittyX.obedience and KittyX.love > KittyX.inhibition:
        ch_k "and you're so sweet. . ."
    elif KittyX.obedience > KittyX.inhibition:
        ch_k "and you give me what I need. . ."
    else:
        ch_k "and I've been trying out new things. . ."
    ch_k "So[KittyX.like]I was thinking, could I call you. . . \"daddy?\""
    menu:
        extend ""
        "Ok, go right ahead?":
            $ KittyX.change_face("smile")
            call change_Girl_stat(KittyX, "love", 25)
            call change_Girl_stat(KittyX, "obedience", 10)
            call change_Girl_stat(KittyX, "inhibition", 30)
            ch_k "Great!"
        "What do you mean by that?":
            $ KittyX.change_face("bemused")
            ch_k "I don't know, it'd kinda be hot, being your baby girl. . ."
            ch_k "Could'ya call me that?"
            menu:
                extend ""
                "Sounds interesting, fine by me.":
                    $ KittyX.change_face("smile")
                    call change_Girl_stat(KittyX, "love", 17)
                    call change_Girl_stat(KittyX, "obedience", 20)
                    call change_Girl_stat(KittyX, "inhibition", 25)
                    ch_k "Nice! . . daddy."
                    $ KittyX.player_petname = "daddy"
                "Could you not, please?":
                    call change_Girl_stat(KittyX, "obedience", 40)
                    call change_Girl_stat(KittyX, "inhibition", 20)
                    $ KittyX.change_face("sad")
                    ch_k " . . . "
                    ch_k "Huh. K."
                "No, that creeps me out.":
                    call change_Girl_stat(KittyX, "love", -15)
                    call change_Girl_stat(KittyX, "obedience", 45)
                    call change_Girl_stat(KittyX, "inhibition", 5)
                    $ KittyX.change_face("angry")
                    ch_k "Booo."
        "No, that creeps me out.":
            call change_Girl_stat(KittyX, "love", -10)
            call change_Girl_stat(KittyX, "obedience", 40)
            call change_Girl_stat(KittyX, "inhibition", 10)
            $ KittyX.change_face("angry")
            ch_k "Hrmph."
    $ KittyX.player_petnames.append("daddy")
    return




label Kitty_Yoink(Girl=0, TempBonus=0, Shy=0):






    if "yoink" in KittyX.daily_history:
        ch_k "We've had enough fun with that."
        return

    if RogueX.location == Player.location:
        $ Girl = RogueX
    elif EmmaX.location == Player.location:
        $ Girl = EmmaX
    elif LauraX.location == Player.location:
        $ Girl = LauraX
    elif JeanX.location == Player.location:
        $ Girl = JeanX
    elif StormX.location == Player.location:
        $ Girl = StormX
    elif JubesX.location == Player.location:
        $ Girl = JubesX

    if (EmmaX.teaching or StormX.teaching) and Player.location == "bg_classroom":

        menu:
            "About who?"
            "[Girl.name]?" if Girl:
                pass
            "[EmmaX.name]" if EmmaX.teaching:
                $ Girl = EmmaX
            "[StormX.name]" if StormX.teaching:
                $ Girl = StormX
            "Never mind":
                return
    elif not Girl:
        "I don't know who you think you could yoink from."
        return


    if KittyX.likes[Girl.tag] <= 200:
        $ TempBonus = 400
    elif KittyX.likes[Girl.tag] <= 400:
        $ TempBonus = 200
    elif KittyX.likes[Girl.tag] >= 800 or approval_check(Girl, 500, "I", taboo_modifier = 3):

        $ TempBonus = 0
    else:

        $ TempBonus = -400

    menu:
        "Hey [KittyX.name], why don't you snag [Girl.name]'s. . ."
        ". . . [Girl.Clothes[top].name]?" if Girl.Clothes["top"]:
            if Girl.Clothes["bra"]:

                $ Shy = 2
                if approval_check(KittyX, 800, taboo_modifier=2, Bonus=TempBonus):


                    $ line = "over"
                elif approval_check(KittyX, 600, taboo_modifier=2, Bonus=TempBonus):

                    $ line = "no"
                else:

                    $ line = "noway"
            else:

                $ Shy = 3
                if approval_check(KittyX, 800, taboo_modifier=2.5, Bonus=(TempBonus*1.5)):
                    $ line = "over"
                elif approval_check(KittyX, 600, taboo_modifier = 1.5, Bonus=TempBonus):
                    $ line = "no"
                else:
                    $ line = "noway"

        ". . . [Girl.Clothes[bra].name]?" if Girl.Clothes["bra"]:
            if Girl.Clothes["top"]:

                $ Shy = 1
                if approval_check(KittyX, 1200, taboo_modifier = 1, Bonus=TempBonus):


                    $ line = "chest"
                elif approval_check(KittyX, 600, taboo_modifier=0.5, Bonus=TempBonus):

                    $ line = "no"
                else:

                    $ line = "noway"
            else:

                $ Shy = 3
                if approval_check(KittyX, 800, taboo_modifier=2.5, Bonus=(TempBonus*1.5)):
                    $ line = "chest"
                elif approval_check(KittyX, 600, taboo_modifier = 1.5, Bonus=TempBonus):
                    $ line = "no"
                else:
                    $ line = "noway"

        ". . . [Girl.Clothes[bottom].name]?" if Girl.Clothes["bottom"]:
            if Girl.Clothes["underwear"] or Girl.Clothes["hose"] == "tights":

                $ Shy = 2
                if approval_check(KittyX, 1000, taboo_modifier=2, Bonus=TempBonus):


                    $ line = "legs"
                elif approval_check(KittyX, 800, taboo_modifier=2, Bonus=TempBonus):

                    $ line = "no"
                else:

                    $ line = "noway"
            else:

                $ Shy = 3
                if approval_check(KittyX, 1000, taboo_modifier=2.5, Bonus=(TempBonus*1.5)):
                    $ line = "legs"
                elif approval_check(KittyX, 800, taboo_modifier = 1.5, Bonus=TempBonus):
                    $ line = "no"
                else:
                    $ line = "noway"

        ". . . [Girl.Clothes[underwear].name]?" if Girl.Clothes["underwear"]:
            if Girl.Clothes["bottom"] or Girl.Clothes["hose"] == "tights":

                $ Shy = 1
                if approval_check(KittyX, 1000, taboo_modifier = 1, Bonus=TempBonus):


                    $ line = "panties"
                elif approval_check(KittyX, 800, taboo_modifier=0.5, Bonus=TempBonus):

                    $ line = "no"
                else:

                    $ line = "noway"
            else:

                $ Shy = 3
                if approval_check(KittyX, 1000, taboo_modifier=2.5, Bonus=(TempBonus*1.5)):
                    $ line = "panties"
                elif approval_check(KittyX, 800, taboo_modifier = 1.5, Bonus=TempBonus):
                    $ line = "no"
                else:
                    $ line = "noway"

        ". . . [Girl.Clothes[hose].name]?" if Girl.Clothes["hose"]:
            if Girl.Clothes["bottom"]:

                $ Shy = 1
                if approval_check(KittyX, 800, taboo_modifier = 1, Bonus=TempBonus):


                    $ line = "hose"
                elif approval_check(KittyX, 800, taboo_modifier=0.5, Bonus=TempBonus):

                    $ line = "no"
                else:

                    $ line = "noway"
            elif Girl.Clothes["underwear"] or Girl.Clothes["hose"] != "pantyhose":

                $ Shy = 2
                if approval_check(KittyX, 1000, taboo_modifier=2, Bonus=TempBonus):


                    $ line = "hose"
                elif approval_check(KittyX, 800, taboo_modifier=2, Bonus=TempBonus):

                    $ line = "no"
                else:

                    $ line = "noway"
            else:

                $ Shy = 3
                if approval_check(KittyX, 1000, taboo_modifier=2.5, Bonus=(TempBonus*1.5)):
                    $ line = "hose"
                elif approval_check(KittyX, 800, taboo_modifier = 1.5, Bonus=TempBonus):
                    $ line = "no"
                else:
                    $ line = "noway"
        "Never mind.":

            return

    if line == "no":
        $ KittyX.change_face("sadside", 1)
        call change_Girl_stat(KittyX, "love", -(Shy))
        ch_k "I really couldn't do that to her."
        return
    if line == "noway":
        $ KittyX.change_face("angry", 1)
        call change_Girl_stat(KittyX, "love", -(2*Shy))
        call change_Girl_stat(KittyX, "obedience", -(Shy))
        ch_k "How could you[KittyX.like]even {i}consider{/i} something like that?"
        return


    call change_Girl_stat(KittyX, "obedience", Shy)
    call change_Girl_stat(KittyX, "inhibition", Shy)
    "[KittyX.name] sneaks up behind [Girl.name]. . ."

    $ Girl.change_face("surprised", 2)
    if line == "over":
        $ line = Girl.Clothes["top"]
        $ Girl.take_off("top")
        call expression Girl.tag + "_First_Topless" pass (1)
        "She reaches out and snags [Girl.name]'s [line], tugging it through her body."

    elif line == "chest":
        $ line = Girl.Clothes["bra"]
        $ Girl.take_off("bra")
        call expression Girl.tag + "_First_Topless" pass (1)
        if Girl.Clothes["top"]:
            "She reaches through [Girl.name]'s [Girl.Clothes[top].name] and snags her [line]."
        else:
            "She reaches out and snags [Girl.name]'s [line], tugging it free."

    elif line == "legs":
        $ line = Girl.Clothes["bottom"]
        $ Girl.Outfit.remove_Clothing(["pants", "skirt"])
        call expression Girl.tag + "_First_Bottomless" pass (1)
        "She reaches down and snags [Girl.name]'s [line], tugging them through her body."

    elif line == "panties":
        $ line = Girl.Clothes["underwear"]
        $ Girl.take_off("underwear")
        call expression Girl.tag + "_First_Bottomless" pass (1)
        if Girl.Clothes["bottom"]:
            "She reaches down through [Girl.name]'s [Girl.Clothes[bottom].name] and snags her [line]."
        elif Girl.Clothes["hose"]:
            "She reaches down through [Girl.name]'s [Girl.Clothes[hose].name] and snags her [line]."
        else:
            "She reaches out and snags [Girl.name]'s [line], tugging them free."
    elif line == "hose":
        $ line = Girl.Clothes["hose"]
        $ Girl.take_off("hose")
        call expression Girl.tag + "_First_Bottomless" pass (1)
        if Girl.Clothes["bottom"]:
            "She reaches down through [Girl.name]'s [Girl.Clothes[bottom].name] and snags her [line]."
        else:
            "She reaches out and snags [Girl.name]'s [line], tugging them free."

    "She then dashes back a few steps, slipping the [line] behind her back."

    call Activity_Check (Girl, KittyX, 1, 0, 2)
    $ approval = _return

    $ KittyX.daily_history.append("yoink")
    if "yoink" not in KittyX.history:
        $ KittyX.history.append("yoink")

    if "exhibitionist" in Girl.traits:
        $ approval = 2
    $ Girl.daily_history.append("yoink")

    if Shy <= 1:

        if approval >= 2:

            $ Girl.change_face("sly")
            call change_Girl_stat(Girl, "inhibition", Shy)
            call change_Girl_stat(Girl, "lust", 2)
            "[Girl.name] glances back in surprise, but then breaks into a quick smile."
        elif approval:

            $ Girl.change_face("angry", 1)
            call change_Girl_stat(Girl, "love", -(Shy))
            "[Girl.name] glances back in surprise, and then glances over at you with a glare."
        else:
            $ Girl.change_face("angry", 2)
            call change_Girl_stat(Girl, "love", -(Shy))
            "[Girl.name] glances back in surprise, and then glances over at you with a glare."
            "She storms away in disgust."

    elif Shy <= 2:

        if approval >= 2:

            $ Girl.change_face("sly")
            call change_Girl_stat(Girl, "inhibition", Shy)
            call change_Girl_stat(Girl, "lust", Shy)
            "[Girl.name] glances back in surprise, but then breaks into a quick smile."
            "She then just leans back, unconcerned."
        elif approval or Girl == JeanX:

            $ Girl.change_face("angry", 1)
            call change_Girl_stat(Girl, "love", -(Shy))
            call change_Girl_stat(Girl, "inhibition", -(Shy))
            call change_Girl_stat(Girl, "lust", Shy)
            "[Girl.name] glances back in surprise, and then glances over at you with a glare."
            if Girl != JeanX:
                $ Girl.change_face("sadside", 2)
                "She settles back down with a little embarassment."
        else:
            $ Girl.change_face("angry", 2)
            call change_Girl_stat(Girl, "love", -(Shy))
            call change_Girl_stat(Girl, "inhibition", -(Shy))
            "[Girl.name] glances back in surprise, and then glances over at you with a glare."
            "She dashes away in embarassment."
    else:

        if approval >= 2:

            $ Girl.change_face("sly")
            call change_Girl_stat(Girl, "love", 1)
            call change_Girl_stat(Girl, "inhibition", Shy)
            call change_Girl_stat(Girl, "lust", 2*Shy)
            "[Girl.name] glances back in surprise, but then breaks into a quick smile."
            "She looks around, daring anyone to comment."
        elif approval or Girl == JeanX:

            $ Girl.change_face("angry", 2)
            call change_Girl_stat(Girl, "love", -(Shy))
            call change_Girl_stat(Girl, "inhibition", -(Shy))
            "[Girl.name] glances back in surprise, and then glances over at you with a glare."
            if Girl != JeanX:
                "She seems really mortified, but stands her ground."
        else:
            $ Girl.change_face("angry", 2)
            call change_Girl_stat(Girl, "love", -(Shy))
            call change_Girl_stat(Girl, "inhibition", -(Shy))
            "[Girl.name] glances back in surprise, and then glances over at you with a glare."
            "She dashes away in embarassment."



    if approval:
        $ Girl.check_if_likes(KittyX, 900, (2*Shy), 1)
        $ KittyX.check_if_likes(Girl, 900, (2*Shy), 1)
        $ Girl.add_word(1, "yoinked")
    else:
        call remove_Girl(Girl)
        $ Girl.check_if_likes(KittyX, 900, -(2*Shy), 1)

    if Girl == JeanX and approval < 2:
        "With a quick nod, her clothes come flying back to her."
        $ Girl.drain_word("yoinked")
        $ Girl.change_Outfit()
        "[KittyX.name]'s left a little dazed."
    elif TempBonus > 0:
        if approval < 2:

            $ KittyX.change_face("sly")
            call change_Girl_stat(KittyX, "love", 1)
            "[KittyX.name] smiles triumphantly."
        else:

            $ KittyX.change_face("angry", eyes = "side")
            "[KittyX.name] seems a bit annoyed at [Girl.name]'s attitude."

    elif not approval:

        $ KittyX.change_face("sly")
        call change_Girl_stat(KittyX, "lust", Shy)
        "[KittyX.name] seems a bit uncertain about the whole thing."
    else:

        $ KittyX.change_face("sly")
        call change_Girl_stat(KittyX, "love", 1)
        call change_Girl_stat(KittyX, "lust", Shy)
        "[KittyX.name] laughs under her breath and waggles the [line] at you."
    return




label Kitty_Kate:
    $ KittyX.location = Player.location
    call set_the_scene
    call show_Girl (KittyX)
    call set_Character_taboos
    $ line = 0
    $ KittyX.change_face("bemused", 1)
    ch_k "Hey, [KittyX.player_petname]. . .you[KittyX.like]got a second?"
    menu:
        extend ""
        "Not really.":
            $ KittyX.change_face("angry", 1)
            ch_k "You're such a jerk, [Player.name]!"
            call change_Girl_stat(KittyX, "love", -10)
            call change_Girl_stat(KittyX, "obedience", 3)
        "Yeah. What's up?":

            pass
    $ KittyX.names.append("Kate")
    ch_k "I just wanted to let you know, I'm going by \"Kate\" now!"
    $ KittyX.name = "Kate"
    menu:
        extend ""
        "Oh no you aren't.":
            call change_Girl_stat(KittyX, "love", -10)
            call change_Girl_stat(KittyX, "obedience", 10)
            call change_Girl_stat(KittyX, "inhibition", -10)
            $ KittyX.change_face("angry", 2)
            ch_k "!!!"
            if approval_check(KittyX, 1200, "LO") or approval_check(KittyX, 500, "O"):
                $ KittyX.name = "Kitty"
                $ KittyX.change_face("sadside", 1)
                call change_Girl_stat(KittyX, "obedience", 10)
                call change_Girl_stat(KittyX, "inhibition", -5)
                ch_k "Well. . . ok. . ."
            else:
                ch_k "You're not my supervisor!"
        "That's a good fit for you.":
            $ KittyX.change_face("smile", 1)
            call change_Girl_stat(KittyX, "love", 5)
            call change_Girl_stat(KittyX, "love", 5)
            call change_Girl_stat(KittyX, "inhibition", 5)
            ch_k "Thanks!"
        "I always thought \"Kitty\" sounded pretty.":
            $ KittyX.name = "Kitty"
            call change_Girl_stat(KittyX, "love", 5)
            call change_Girl_stat(KittyX, "obedience", 5)
            call change_Girl_stat(KittyX, "inhibition", 5)
            ch_k "Oh, well I guess if you really like \"Kitty,\" I can understand that. . ."
        "Why?":
            $ KittyX.names.append("Katherine")
            ch_k "Well, my full name is \"Katherine Pryde\", and I thought \"Kate\" sounded more grown-up."
            menu:
                extend ""
                "Oh, ok then.":
                    $ KittyX.change_face("smile", 1)
                    call change_Girl_stat(KittyX, "love", 5)
                    call change_Girl_stat(KittyX, "love", 5)
                    call change_Girl_stat(KittyX, "inhibition", 5)
                    ch_k ". . ."
                "No, it sounds silly.":
                    call change_Girl_stat(KittyX, "love", -10)
                    call change_Girl_stat(KittyX, "obedience", 10)
                    call change_Girl_stat(KittyX, "inhibition", -10)
                    $ KittyX.change_face("angry", 2)
                    ch_k "!!!"
                    if approval_check(KittyX, 1200, "LO") or approval_check(KittyX, 500, "O"):
                        $ KittyX.name = "Kitty"
                        $ KittyX.change_face("sadside", 1)
                        call change_Girl_stat(KittyX, "obedience", 10)
                        call change_Girl_stat(KittyX, "inhibition", -5)
                        ch_k "Well. . . ok. . ."
                    else:
                        ch_k "You're not my supervisor!"
                "I suppose, but \"Kitty\" is such a pretty name.":
                    call change_Girl_stat(KittyX, "love", 5)
                    call change_Girl_stat(KittyX, "inhibition", 5)
                    if approval_check(KittyX, 800, "LO"):
                        $ KittyX.name = "Kitty"
                        call change_Girl_stat(KittyX, "obedience", 5)
                        ch_k "Well, I guess if you prefer it. . ."
                    else:
                        ch_k "Well. . . too bad."
                "Why not \"Katherine\" then?":
                    call change_Girl_stat(KittyX, "obedience", 5)
                    if approval_check(KittyX, 1200, "LO") or approval_check(KittyX, 500, "0"):
                        $ KittyX.name = "Katherine"
                        call change_Girl_stat(KittyX, "obedience", 5)
                        ch_k "I suppose I could. . ."
                    else:
                        ch_k "I don't really like it that much. . ."
                        menu:
                            extend ""
                            "Ok, \"Kate\" it is then.":
                                $ KittyX.name = "Kate"
                                $ KittyX.change_face("smile", 1)
                                call change_Girl_stat(KittyX, "love", 5)
                                call change_Girl_stat(KittyX, "love", 5)
                                call change_Girl_stat(KittyX, "inhibition", 5)
                                ch_k ". . ."
                            "Ok, then back to \"Kitty?\"":
                                call change_Girl_stat(KittyX, "love", 5)
                                call change_Girl_stat(KittyX, "inhibition", 5)
                                if approval_check(KittyX, 800, "LO"):
                                    $ KittyX.name = "Kitty"
                                    call change_Girl_stat(KittyX, "obedience", 5)
                                    ch_k "I suppose, if you prefer it that way. . ."
                                else:
                                    ch_k "Well. . . too bad."



    return
