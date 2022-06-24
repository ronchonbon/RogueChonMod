label meet_Kitty:
    $ Player.location = "bg_campus"

    "As you rush to class, you see another student running straight at you."
    "You try to move aside, but aren't fast enough to get out of her way,"

    $ KittyX.name = "???"
    $ KittyX.location = Player.location
    $ KittyX.arm_pose = 1
    $ KittyX.change_face("_surprised")

    call show_Girl(KittyX, x_position = stage_center, transition = vpunch)
    call shift_focus(KittyX)

    "She crashes into you at a full jog, and you both fall to the ground."
    "You scramble to your feet and offer the girl a hand up."
    ch_k "Hey!"

    $ KittyX.brows = "_angry"
    $ KittyX.change_stat("love", 90, -25)

    ch_k "What the hell was that?"

    $ flag = True

    menu:
        extend ""
        "You crashed into me!":
            $ KittyX.change_face("_confused", 2)
            $ KittyX.change_stat("love", 90, 5)
            $ KittyX.change_stat("obedience", 80, 20)

            ch_k "Wha! Well, yeah. . ."

            $ KittyX.blushing = "_blush1"

            $ flag = False
        "Sorry about that.":
            $ KittyX.change_face("_bemused", 1)
            $ KittyX.eyes = "_side"
            $ KittyX.change_stat("love", 90, 25)

            ch_k "Well, I guess it[KittyX.like]wasn't entirely your fault. . ."
        "A meet-cute?":
            $ KittyX.change_face("_surprised", 2)
            $ KittyX.change_stat("love", 90, 15)
            $ KittyX.change_stat("inhibition", 70, 10)

            ch_k " ! "

            $ KittyX.change_face("_bemused", 1)

            ch_k "Hmm. . . maybe. . ."

    ch_p "My name's [Player.name], by the way."

    if flag:
        $ KittyX.change_face("_smile", 1)

        ch_k "Mine's Kitty! Kitty Pryde. Nice to meet you!"
    else:
        $ KittyX.change_face("_sadside", 1)

        ch_k "Um, mine's Kitty."

    $ KittyX.name = "Kitty"
    $ KittyX.change_face("_normal", blushing = 1, mouth = "_sad")

    ch_k "I just[KittyX.like]didn't expect to bounce off you like that. Normally I can phase through things."

    menu:
        extend ""
        "Losing your touch?":
            $ KittyX.change_face("_confused", 0)
            $ KittyX.change_stat("obedience", 80, 5)

            ch_k "I don't {i}think{/i} that's it. . ."
            ch_p "Just kidding. . ."

            $ KittyX.change_stat("love", 90, 5)
        "Was I too distracting?":
            $ KittyX.change_face("_angry", 1, brows = "_normal")
            $ KittyX.change_stat("love", 90, -2)
            $ KittyX.change_stat("obedience", 80, 8)
            $ KittyX.change_stat("inhibition", 70, 4)

            ch_k "Like, no."
            ch_p "Heh, I guess not."
        "It must be my powers.":
            $ KittyX.change_face("_confused", 0)
            $ KittyX.change_stat("love", 90, 5)

            ch_k "Oh?"

    ch_p "I have the ability to negate mutant powers, so you can't phase through me."

    $ KittyX.change_face("_perplexed", 0)

    ch_k "Oh! Wow, that's an interesting power. So if you grab me, I can't get away?"

    menu:
        extend ""
        "Want to give it a try?":
            $ KittyX.change_face("_perplexed", 0)
            $ KittyX.change_stat("love", 90, 5)
            $ KittyX.change_stat("inhibition", 70, 5)

            ch_k "I'm definitely curious."
        "I guess so.":
            $ KittyX.change_face("_sadside", 0, mouth = "_lipbite")
            $ KittyX.change_stat("obedience", 80, 3)
            $ KittyX.change_stat("inhibition", 70, 7)

            ch_k "I'd like to give it a try."
        "Does that turn you on?":
            $ KittyX.change_face("_surprised", 2)
            $ KittyX.change_stat("obedience", 80, 5)

            ch_k "What?! No! . ."

            $ KittyX.change_face("_bemused", 1)
            $ KittyX.change_stat("inhibition", 70, 5)
            $ KittyX.eyes = "_side"

            ch_k ". . . no."

            $ KittyX.eyes = "_sexy"

            ch_k "But it is[KittyX.like]worth testing."

    ch_p "Ok, let's give it a shot."
    "You reach out and grab her wrist."

    $ KittyX.addiction_rate += 2
    $ KittyX.change_face("_angry", 1, eyes = "_down")

    "She struggles for a few moments to shake you free, but you hold firm."

    $ holding = True
    $ hugged = False
    $ counter = 0

    while holding:
        menu:
            extend ""
            "Let her go.":
                if not counter:
                    $ KittyX.change_stat("love", 90, 7)
                    $ KittyX.change_stat("inhibition", 70, -2)
                elif counter == 1:
                    $ KittyX.change_stat("love", 90, 10)
                else:
                    $ KittyX.change_stat("love", 90, 5)

                "You release her arm and step back."

                $ holding = False
            "Hold on.":
                "You continue to hold onto her arm and she fidgets uncomfortably."

                if not counter:
                    $ KittyX.eyes = "_sexy"

                    ch_k "Are you[KittyX.like]going to let go of my arm any time soon?"
                elif counter == 1:
                    $ KittyX.change_stat("love", 90, -1)
                    $ KittyX.change_stat("obedience", 80, 2)
                else:
                    ch_k "Ok, that's enough!"

                    $ KittyX.eyes = "_sexy"
                    $ KittyX.change_stat("love", 90, -10)
                    $ KittyX.change_stat("obedience", 80, -5)
                    $ KittyX.change_stat("inhibition", 70, 10)

                    "She reaches over and pries your hand loose."

                    $ holding = False

                    "Um. . ."

                $ counter += 1

                $ KittyX.addiction_rate += 1
            "Pull her in for a hug.":
                $ KittyX.change_stat("love", 90, -5)
                $ KittyX.change_face("_surprised", 2)

                ch_k "Hey! Like, not cool!"

                $ KittyX.change_face("_angry", 1)

                call show_Girl(KittyX, transition = vpunch)

                "She elbows you in the ribs and shoves herself back a few steps."

                $ KittyX.change_stat("inhibition", 70, 10)

                ch_k "My powers may not work on you, but I have[KittyX.like]a few years of combat experience on you."
                ch_k "And don't you forget it!"

                $ holding = False
                $ hugged = True

    if counter or hugged:
        $ KittyX.eyes = "_side"

        ch_k "Still though, that was an interesting experience. . ."
    else:
        $ KittyX.change_face("_bemused", 1, eyes = "_side")

        ch_k "That was an interesting experience. . ."

    $ KittyX.eyes = "_sexy"
    $ KittyX.mouth = "_lipbite"

    ch_k "Kinda tingly. . ."

    $ KittyX.change_face("_surprised", mouth = "_kiss")

    ch_k "Oh! I[KittyX.like]totally forgot, I have to get to a briefing!"

    if not hugged:
        $ KittyX.change_face("_smile")

        ch_k "I'll see you later though! Like, bye!"
    else:
        $ KittyX.change_face("_normal")

        ch_k "I'll see you around I guess. Like, bye!"

    call remove_Girl(KittyX)

    "She jogs off down the path, and you continue on to class."

    $ KittyX.history.append("met")

    $ active_Girls.append(KittyX)

    $ Player.location = "bg_classroom"

    return















label Kitty_Key:
    call shift_focus (KittyX)
    call set_the_scene
    $ KittyX.change_face("_bemused")
    $ KittyX.arm_pose = 2
    ch_k "So you've[KittyX.like]been dropping by a lot lately, I figured you might want a key. . ."
    ch_p "Thanks."
    $ KittyX.arm_pose = 1
    $ Player.Keys.append(KittyX)
    $ KittyX.event_happened[0] = 1
    return





label Kitty_BF:
    call shift_focus (KittyX)

    $ KittyX.drain_word("asked_to_meet")

    if KittyX.location != Player.location:
        if KittyX not in Player.Party:
            "[KittyX.name] approaches you and asks if the two of you can talk."
        else:
            "[KittyX.name] turns towards you and asks if the two of you can talk."

    call clear_the_room(KittyX)
    call set_Character_taboos

    "A little blush on her cheeks, you can tell she's a bit anxious about whatever she has to say."

    $ KittyX.daily_history.append("relationship")
    $ KittyX.change_face("_bemused", 1)

    ch_k "So, [KittyX.player_petname], we've[KittyX.like]been hanging for a while, right?"
    ch_k ". . ."
    $ KittyX.eyes = "_sexy"
    menu:
        ch_k "Right?"
        "Yeah. And it's been amazing.":
            $ KittyX.change_stat("love", 200, 20)
        "Yeah, I guess":
            $ KittyX.change_stat("love", 200, 10)
        "Uhm. . .maybe?":
            $ KittyX.change_stat("love", 200, -10)
            $ KittyX.change_stat("obedience", 200, 30)
    if KittyX.SEXP >= 10:
        ch_k "I mean, I've gone further with you than I've ever been with anybody before. . ."
    if KittyX.SEXP >= 15:
        ch_k "You know[KittyX.like]. . .in the {i}bedroom{/i}. . ."
    if len(Player.Harem) >= 2:
        ch_k "I know you[KittyX.like]really get around and all. . ."
    elif RogueX in Player.Harem:
        if "dating?" in KittyX.traits:
            ch_k "I know you're kinda[KittyX.like][RogueX.name]'s boyfriend and all. . . but she and I were talking and[KittyX.like]. . ."
        else:
            ch_k "I know you're kinda[KittyX.like][RogueX.name]'s boyfriend and all. . ."
    elif Player.Harem:
        ch_k "I know you're kinda[KittyX.like]dating [Player.Harem[0].name] and all. . ."

    if not KittyX.event_happened[5]:
        ch_k "So, uhm. . ."
        ch_k "It’s not like I[KittyX.like]haven’t gone out with guys before."
        ch_k "I just[KittyX.like].wow, this is so awkward. I really like you a lot and. . ."
        ch_k "I mean. . . do you wanna[KittyX.like]be my boyfriend?"
        ch_k "[KittyX.Like]maybe we could make it official?"
    elif "dating?" in KittyX.traits:
        ch_k "[RogueX.name] said it’d totally be cool if we were[KittyX.like]dating, too."
    elif Player.Harem:
        ch_k "If you were okay with it. . . I’d still like to be your girlfriend, too."
    else:
        ch_k "I wish you weren’t[KittyX.like]such a jerk sometimes, but still. . . I’m totally serious about this."
        ch_k "I wanna be your girlfriend[KittyX.like]officially."
    $ KittyX.event_happened[5] += 1
    menu:
        extend ""
        "Are you kidding? I'd love to!":
            $ KittyX.change_stat("love", 200, 30)
            "[KittyX.name] wraps her arms around you and starts kissing you passionately."
            call kiss_launch(KittyX)
            $ KittyX.action_counter["kiss"] += 1
        "Uhm[KittyX.like]okay.":
            $ KittyX.brows = "_confused"
            "[KittyX.name] seems a little put off by how casually you’re taking all this."
            "Still, she must think it’s a good first step, at least, because she leans into you and gives you a hug."
        "I'm with someone else now." if Player.Harem:
            $ KittyX.change_face("_sad", 1)
            ch_k "I know. I just[KittyX.like]. . . I thought maybe you could go out with me, too, maybe?"
            menu:
                extend ""
                "Yes. Absolutely." if "KittyYes" in Player.traits:
                    $ KittyX.change_stat("love", 200, 30)
                    "[KittyX.name] wraps her arms around you and starts kissing you passionately."
                    call kiss_launch(KittyX)
                    $ KittyX.action_counter["kiss"] += 1
                "She wouldn't understand." if len(Player.Harem) == 1:
                    $ line = "no"
                "They wouldn't be cool with that." if len(Player.Harem) > 1:
                    $ line = "no"
                "I'm sorry, but. . . no." if KittyX.event_happened[5] != 20:
                    $ line = "no"
                "No way.":
                    jump Kitty_BF_Jerk
            if line == "no":
                $ KittyX.change_stat("love", 200, -10)
                ch_k "Well. . . okay. I get it."
                $ KittyX.event_happened[5] = 20
                call remove_Girl(KittyX)
                $ line = 0
                return
        "Not really.":
            jump Kitty_BF_Jerk

    if not simulation:
        $ Player.Harem.append(KittyX)
        if "KittyYes" in Player.traits:
            $ Player.traits.remove("KittyYes")
    $ KittyX.player_petnames.append("boyfriend")
    $ KittyX.change_face("_sexy")
    ch_k "Now. . . boyfriend. . . how about you and I[KittyX.like]celebrate, huh?"
    if simulation:
        return True
    $ approval_bonus = 10
    $ Player.add_word(1,"interruption")
    call enter_main_sex_menu(KittyX)
    $ approval_bonus = 0
    return

label Kitty_BF_Jerk:
    $ KittyX.change_face("_angry", 1)
    ch_k "Fine![KittyX.Like]. . .be that way!"
    $ KittyX.change_stat("obedience", 50, 40)
    if KittyX.event_happened[5] != 20:
        $ KittyX.change_stat("obedience", 200, (20* KittyX.event_happened[5]))
    if 20 > KittyX.event_happened[5] >= 3:
        $ KittyX.change_face("_sad")
        ch_k "Yeah? Well. . .[KittyX.like]I don’t care what you want! We’re dating! Deal."
        ch_k "I. . .uhm. . .think I need to[KittyX.like]be alone for a little while."
        if simulation:
            return True
        $ KittyX.player_petnames.append("boyfriend")
        $ achievements.append("I am not your Boyfriend!")
        $ Player.location = "bg_player"
        call remove_Girl(KittyX)
        call set_the_scene
        $ renpy.pop_call()
        jump player_room
    if KittyX.event_happened[5] > 1:
        ch_k "It was such a mistake asking you again. You’re[KittyX.like]still such a jerk!"
    if KittyX.event_happened[5] != 20:
        $ KittyX.change_stat("love", 200, -(50* KittyX.event_happened[5]))
    else:
        $ KittyX.change_stat("love", 200, -50)
    ch_k "Get out, you big jerk!"
    if simulation:
        return
    $ Player.location = "bg_player"
    call remove_Girl(KittyX)
    $ renpy.pop_call()
    jump player_room




label Kitty_Love:


    call shift_focus (KittyX)
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

    $ KittyX.location = Player.location
    call set_the_scene (0)
    call show_Girl (KittyX)
    call clear_the_room (KittyX)
    call set_Character_taboos
    $ KittyX.daily_history.append("relationship")
    $ KittyX.change_face("_bemused", 1)
    $ KittyX.eyes = "_side"
    $ line = 0
    $ KittyX.event_happened[6] += 1
    if KittyX.event_happened[6] == 1:
        if KittyX in Player.Harem:
            ch_k "We've[KittyX.like]been together for a while now, and I've been thinking. . ."
        else:
            ch_k "We've[KittyX.like]know each other for a while now, and I've been thinking. . ."
        ch_k "It's been[KittyX.like]kinda hard for me to really get invested in anyone. . ."
        $ KittyX.eyes = "_down"
        ch_k ". . . to[KittyX.like]be comfortable with who they are and be myself. . ."
        $ KittyX.eyes = "_squint"
        ch_k "I just feel like sometimes you. . ."
        $ KittyX.eyes = "_side"
        ch_k "and me[KittyX.like] . ."
        $ KittyX.change_face("_perplexed", 2)
        $ KittyX.eyes = "_surprised"
        ch_k "Never mind!"
        "Kitty dashes off and phases through the nearest wall."

        call remove_Girl(KittyX)
        return
    if KittyX.event_happened[6] == 2:
        ch_k "Sorry about before, I don't think I was ready maybe. . ."
        ch_k ". . . but I was kind of thinking-"
    elif KittyX.event_happened[6] >= 5:
        ch_k "Um. . ."
        $ KittyX.eyes = "_squint"
        ch_k "You know, it's time to stop running. I think I love you."
        $ KittyX.eyes = "_side"
        ch_k "You don't have to say it back, but I do."
        $ KittyX.player_petnames.append("lover")
        ch_k "Um, that's all."
    else:
        ch_k "Um. . ."
    if "lover" not in KittyX.player_petnames:
        menu:
            "She turns and makes a break for the nearest wall."
            "Catch her":
                $ KittyX.change_face("_perplexed", 2)
                $ KittyX.eyes = "_surprised"
                $ KittyX.change_stat("love", 95, 10)
                $ KittyX.change_stat("obedience", 95, 15)
                "As she spins, you grab on to her wrist. She's slightly startled to have been caught."
            "Let her go":
                "She dashes through the nearest wall and vanishes from view."
                jump Kitty_Love_End
        $ KittyX.blushing = "_blush1"
        menu:
            extend ""
            "Pull her close":
                $ KittyX.change_face("_smile", 1)
                $ KittyX.change_stat("love", 95, 20)
                "You draw her into an embrace, arms wrapped tightly around her waist."
                $ line = "hug"
            "Stay like this":
                $ KittyX.eyes = "_down"
                $ KittyX.change_stat("obedience", 95, 10)
                "You keep hold of her wrist."
                $ line = "wrist"
            "Let her go":
                if 1 < KittyX.event_happened[6] < 4:
                    "You immediately release her wrist."
                    $ KittyX.eyes = "_down"
                    "She dashes through the nearest wall and vanishes from view."
                    jump Kitty_Love_End
                else:
                    $ KittyX.change_stat("love", 95, 10)
                    $ KittyX.change_stat("obedience", 95, 20)
                    $ KittyX.change_stat("inhibition", 80, 20)
                    "You release her wrist and she takes a step back."

        ch_k "I'm. . . I'm sorry, I just kind of panicked."
    if "lover" not in KittyX.player_petnames:

        ch_k "I thought maybe if I let myself get too close. . ."
        ch_k "I'd fall. . ."
        menu:
            extend ""
            "I'll never let go." if line:
                $ KittyX.change_stat("love", 95, 20)
                $ KittyX.change_stat("inhibition", 80, 10)
                "She melts into your arms."
            "I'd always catch you.":
                $ KittyX.change_face("_smile")
                $ KittyX.change_stat("love", 95, 20)
                $ KittyX.change_stat("obedience", 80, 15)
                "She smiles and shifts a bit uncomfortably."
            "Yeah, you should watch out for that.":
                $ KittyX.change_face("_angry", 1)
                $ KittyX.recent_history.append("_angry")
                $ KittyX.change_stat("love", 200, -20)
                $ KittyX.change_stat("obedience", 80, 10)
                $ KittyX.change_stat("inhibition", 80, 10)
                "She shoves you away and then stomps through the nearest wall."
                jump Kitty_Love_End
            "So get going. [[Give her a shove]":

                $ KittyX.change_face("_surprised", 1)
                $ KittyX.change_stat("love", 200, -50)
                $ KittyX.change_stat("obedience", 80, 10)
                $ KittyX.change_stat("inhibition", 80, 10)
                "You shove her through the nearest wall and then continue on you way."
                $ KittyX.recent_history.append("_angry")
                call remove_Girl(KittyX)
                jump Kitty_Love_End

    if "lover" in KittyX.player_petnames:

        menu:
            extend ""
            "I love you too.":
                $ KittyX.change_stat("love", 200, 40)
                $ KittyX.change_stat("inhibition", 200, 50)
                $ KittyX.change_face("_smile")
            "You love me?":
                $ KittyX.change_face("_confused", 2)
                menu:
                    ch_k "But you don't love me?"
                    "Yeah, of course I do!":
                        $ KittyX.change_stat("love", 200, 30)
                        $ KittyX.change_stat("inhibition", 200, 60)
                        $ KittyX.change_face("_smile")
                    "I mean, a little?":
                        $ KittyX.change_stat("obedience", 80, 20)
                        $ KittyX.change_stat("inhibition", 80, -10)
                        ch_k "That's not a \"yes.\" . ."
                        $ line = "awkward"
                    "Not really.":
                        $ KittyX.change_stat("love", 200, -30)
                        $ KittyX.change_stat("obedience", 80, 30)
                        $ KittyX.change_stat("inhibition", 80, -30)
                        $ KittyX.change_face("_angry", 2)
                        ch_k "Huh?!"
                        $ line = "awkward"
            "Huh.":
                $ KittyX.change_stat("love", 200, -10)
                $ KittyX.change_stat("obedience", 80, 10)
                $ KittyX.change_stat("inhibition", 80, -20)
                menu:
                    ch_k "Huh?!"
                    "I mean, I love you too!":
                        $ KittyX.change_stat("love", 200, 30)
                        $ KittyX.change_stat("inhibition", 80, 10)
                        $ KittyX.change_face("_smile")
                        ch_k "Way to pull out a last minute save there. . ."
                    "Well that's awkward.":
                        $ KittyX.change_stat("love", 200, -20)
                        $ KittyX.change_stat("obedience", 80, 30)
                        $ KittyX.change_stat("inhibition", 80, -20)
                        $ KittyX.change_face("_angry", 2)
                        $ line = "awkward"
            "Well that's awkward.":
                $ KittyX.change_stat("love", 200, -30)
                $ KittyX.change_stat("obedience", 80, 40)
                $ KittyX.change_stat("inhibition", 80, -20)
                $ KittyX.change_face("_perplexed", 2)
                $ line = "awkward"
    else:
        menu:
            extend ""
            "I love you, [KittyX.name].":
                $ KittyX.change_stat("love", 200, 50)
                $ KittyX.change_stat("inhibition", 80, 30)
                $ KittyX.change_face("_smile")
                $ line = "love"
            "I think you're pretty great.":
                $ KittyX.change_face("_confused")
                menu:
                    ch_k "But you don't love me?"
                    "Yeah, of course I do!":
                        $ KittyX.change_stat("love", 200, 30)
                        $ KittyX.change_stat("obedience", 50, 10)
                        $ KittyX.change_stat("inhibition", 80, 20)
                        $ KittyX.change_face("_smile")
                    "I mean, a little?":
                        if approval_check(KittyX, 1200, "OI"):
                            $ KittyX.change_face("_sad")
                            $ KittyX.change_stat("love", 200, -30)
                            $ KittyX.change_stat("obedience", 90, 20)
                            $ KittyX.change_stat("inhibition", 80, 10)
                            ch_k "But[KittyX.like]not \"nothing\". . ."
                        else:
                            $ line = "awkward"
                    "Not really.":
                        $ KittyX.change_face("_sad")
                        if approval_check(KittyX, 1500, "OI"):
                            $ KittyX.change_stat("love", 200, -30)
                            $ KittyX.change_stat("obedience", 50, 30)
                            ch_k "Ouch. . ."
                        else:
                            $ line = "awkward"
            "I was thinking something more casual. . .":
                $ KittyX.change_face("_sad")
                if approval_check(KittyX, 1200, "OI") or approval_check(KittyX, 700, "I"):
                    $ KittyX.change_stat("love", 200, -30)
                    $ KittyX.change_stat("obedience", 90, 20)
                    $ KittyX.change_stat("inhibition", 90, 30)
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
            $ KittyX.change_stat("love", 200, -50)
            $ KittyX.change_stat("obedience", 95, 50)
            $ KittyX.change_stat("inhibition", 80, -50)
            ch_k "Oh, well I mean if you don't love me-"
            ch_k "You don't have to love me, that's ok."
            ch_k "I'll, um. . . never mind."
            if not simulation:
                $ KittyX.recent_history.append("_angry")
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
        $ KittyX.location = Player.location
        call set_the_scene
        call clear_the_room (KittyX)
        call set_Character_taboos
        ch_k "Ok, so like I was saying. . ."
    $ KittyX.change_stat("obedience", 70, 10)
    $ Player.add_word(1,"interruption")
    menu:
        extend ""
        "Yeah, let's do this. . . [[have sex]":
            $ KittyX.change_stat("inhibition", 30, 30)
            ch_k "Hmm. . ."
            if simulation:
                return True
            call start_action(KittyX, "sex")
        "I have something else in mind. . .[[choose another activity]":
            $ KittyX.brows = "_confused"
            $ KittyX.change_stat("obedience", 70, 20)
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
        $ KittyX.change_stat("love", 95, 10)
        if approval_check(KittyX, 950, "L"):
            $ line = "love"
        else:
            $ KittyX.change_face("_sad")
            ch_k "You've dug too deep a hole, [KittyX.player_petname]."
            ch_k "Keep trying though."
    else:
        ch_p "Remember when I told you that I didn't love you?"
        $ KittyX.change_face("_perplexed", 1)
        ch_k "Um, YEAH?!"
        menu:
            "I'm sorry, I didn't mean it.":
                $ KittyX.eyes = "_surprised"
                ch_k "Well, if you. . . so wait, you {i}do{/i} love me?"
                ch_p "Yeah. I mean, yes, I love you, Kitty."
                $ KittyX.change_stat("love", 200, 10)
                if approval_check(KittyX, 950, "L"):
                    $ line = "love"
                else:
                    $ KittyX.change_face("_sadside")
                    ch_k "Well, I don't know how I feel at this point. . ."
            "I've changed my mind, so. . .":
                if approval_check(KittyX, 950, "L"):
                    $ line = "love"
                    $ KittyX.eyes = "_surprised"
                    ch_k "Really?!"
                else:
                    $ KittyX.mouth = "_sad"
                    ch_k "Oh, you've changed your mind. Wonderful."
                    $ KittyX.change_stat("inhibition", 90, 10)
                    $ KittyX.change_face("_sadside")
                    ch_k "Maybe I have too. . ."
            "Um, never mind.":
                $ KittyX.change_stat("love", 200, -30)
                $ KittyX.change_stat("obedience", 50, 10)
                $ KittyX.change_face("_angry")
                ch_k "Seriously?"
                $ KittyX.recent_history.append("_angry")
    if line == "love":
        $ KittyX.change_stat("love", 200, 40)
        $ KittyX.change_stat("obedience", 90, 10)
        $ KittyX.change_stat("inhibition", 90, 10)
        $ KittyX.change_face("_smile")
        ch_k "I[KittyX.like]love you too!"
        if KittyX.event_happened[6] < 25:
            $ KittyX.change_face("_sly")
            "She slugs you in the arm"
            ch_k "Took you long enough."
        $ KittyX.player_petnames.append("lover")
    $ KittyX.event_happened[6] = 25
    return





label Kitty_Sub:
    call shift_focus (KittyX)
    $ KittyX.drain_word("asked_to_meet")
    if KittyX.location != Player.location and KittyX not in Player.Party:
        "Suddenly, [KittyX.name] shows up and says she needs to talk to you."

    $ KittyX.location = Player.location
    call set_the_scene (0)
    call show_Girl (KittyX)
    call clear_the_room (KittyX)
    call set_Character_taboos
    $ KittyX.daily_history.append("relationship")
    $ KittyX.change_face("_bemused", 1)

    $ line = 0
    ch_k "So, uhm. . .you've really kinda[KittyX.like]taken control in our relationship lately."
    menu:
        extend ""
        "I guess. That's just kind of what comes naturally for me.":
            $ KittyX.change_stat("obedience", 200, 10)
            $ KittyX.change_stat("inhibition", 50, 5)
        "Sorry. I didn't mean to come off like that.":
            $ KittyX.change_face("startled", 2)
            $ KittyX.change_stat("love", 80, 5)
            $ KittyX.change_stat("obedience", 200, -5)
            $ KittyX.change_stat("inhibition", 50, -5)
            ch_k "No! Don't get the wrong idea! I just. . ."
        "Yup. Deal with it.":
            if approval_check(KittyX, 1000, "LO"):
                $ KittyX.change_stat("obedience", 200, 20)
                $ KittyX.change_stat("inhibition", 50, 10)
                ch_k "Um, yeah. . ."
            else:
                $ KittyX.change_stat("love", 200, -10)
                $ KittyX.change_stat("obedience", 200, 10)
                $ KittyX.change_stat("inhibition", 50, 5)
                $ KittyX.change_face("_angry")
                ch_k "I {i}was{/i} going to tell you I kinda liked it. But I didn't think you'd be[KittyX.like]a {i}jerk{/i} about it!"
                menu:
                    extend ""
                    "Guess you don't know me so well, huh?":
                        ch_k "I guess not."
                        $ line = "rude"
                    "Sorry. I kind of thought you were getting into me being like that.":
                        $ KittyX.change_face("_sexy", 2)
                        $ KittyX.eyes = "_side"
                        $ KittyX.change_stat("love", 95, 5)
                        $ KittyX.change_stat("obedience", 200, 5)
                        $ KittyX.change_stat("inhibition", 50, 5)
                        ch_k ". . ."

    $ KittyX.blushing = "_blush1"
    if not line:

        ch_k "Well, I've, uhm. . . never had a guy be like that with me before. . ."
        $ KittyX.change_face("_sly", 2)
        ch_k "I think I kinda like it."
        $ KittyX.change_face("_smile", 1)
        menu:
            extend ""
            "Good. If you wanna be with me, that's how it'll be.":
                if approval_check(KittyX, 1000, "LO"):
                    $ KittyX.change_stat("obedience", 200, 15)
                    $ KittyX.change_stat("inhibition", 50, 10)
                    ch_k "I guess I walked into that one. . ."
                else:
                    $ KittyX.change_face("_sadside", 1)
                    $ KittyX.change_stat("love", 200, -5)
                    $ KittyX.change_stat("obedience", 200, 10)
                    ch_k "You don't have to do it[KittyX.like]{i}all{/i} the time. You could still be nice once in a while."
                    menu:
                        extend ""
                        "Whatever. That's how it is. Take it or leave it.":
                            $ KittyX.change_face("_angry")
                            $ KittyX.change_stat("love", 200, -10)
                            $ KittyX.change_stat("obedience", 200, 5)
                            ch_k "Y'know, you're such a jerk, [Player.name]!"
                            $ line = "rude"
                        "I think I could maybe do that.":
                            $ KittyX.change_face("_bemused", 2)
                            $ KittyX.eyes = "_side"
                            $ KittyX.change_stat("love", 95, 5)
                            $ KittyX.change_stat("obedience", 200, 3)
                            $ KittyX.change_stat("inhibition", 50, 5)
                            ch_k "Uhm. . .yeah. It's[KittyX.like]. . kinda hot."
            "Yeah? You think it's sexy?":

                $ KittyX.change_face("_bemused", 2)
                $ KittyX.eyes = "_side"
                $ KittyX.change_stat("obedience", 200, 5)
                $ KittyX.change_stat("inhibition", 50, 10)
                ch_k "Uhm. . .yeah. It's[KittyX.like]. . kinda hot."
            "You sure you don't want me to back off a little?":

                $ KittyX.change_face("startled", 1)
                $ KittyX.change_stat("obedience", 200, -5)
                menu:
                    ch_k "Only if you think it might be[KittyX.like]weird. But I think it's kinda hot."
                    "Only if you're okay with it.":
                        $ KittyX.change_face("_bemused", 2)
                        $ KittyX.change_stat("love", 95, 10)
                        $ KittyX.change_stat("inhibition", 50, 10)
                        $ line = 0
                    "Uhm. . .yeah. I {i}do{/i} think it's weird. Sorry.":
                        $ KittyX.change_stat("love", 200, -15)
                        $ KittyX.change_stat("obedience", 200, -5)
                        $ KittyX.change_stat("inhibition", 50, -10)
                        $ line = "embarrassed"
            "I don't really care what you like. I do what I want.":

                $ KittyX.change_stat("love", 200, -10)
                $ KittyX.change_stat("obedience", 200, 15)
                $ KittyX.change_face("_angry")
                ch_k "Y'know, you're such a jerk, [Player.name]!"
                $ line = "rude"

    if not line:
        $ KittyX.change_face("_bemused", 1)
        $ KittyX.eyes = "_down"
        ch_k "Cool. So. . .just so you know. . .I don't mind[KittyX.like]you being in control."
        if "256 Shades of Grey" in KittyX.inventory:
            ch_k "Like in that '256 Shades of Grey' book."
        menu Kitty_Sub_Choice:
            extend ""
            "Don't you think that relationship's kinda. . .weird?":
                $ KittyX.change_stat("love", 200, -5)
                $ KittyX.change_stat("inhibition", 50, -15)
                $ line = "embarrassed"
            "I think I could get used to that kinda thing.":
                $ KittyX.change_stat("obedience", 200, 5)
                $ KittyX.change_stat("inhibition", 50, 5)
                $ KittyX.change_face("_smile", 1)
                $ line = 0
            "You actually {i}read{/i} that?" if "256 Shades of Grey" in KittyX.inventory and line != "grey":
                $ KittyX.change_stat("love", 95, 5)
                $ KittyX.change_face("_sly", 1)
                ch_k "You think I wouldn't read something you bought me? I think you {i}maybe{/i} don't realize how much I like you."
                $ KittyX.change_stat("inhibition", 50, 5)
                ch_k "Well, I {i}did{/i} read it. And. . .it turns out it kinda[KittyX.like]. . {i}really{/i} turned me on."
                ch_k "So. . .what d'you think? Think[KittyX.like]maybe you'd like that?"
                $ line = "grey"
                jump Kitty_Sub_Choice

    if not line:
        $ KittyX.change_face("_smile", 1)
        ch_k "Awesome. So. . .if you wanted me to, I could[KittyX.like]call you {i}sir{/i} or something."
        $ KittyX.change_face("_sly", 2)
        ch_k "Think you'd like that?"
        $ KittyX.blushing = "_blush1"
        menu:
            extend ""
            "That has a nice ring to it.":
                $ KittyX.change_stat("love", 95, 5)
                $ KittyX.change_stat("obedience", 200, 15)
                $ KittyX.change_stat("inhibition", 50, 5)
                ch_k "Okay, then. . .{i}sir{/i}."
                $ KittyX.player_petname = "sir"
            "I think I'd rather stick with what we've got going.":
                $ KittyX.change_face("startled", 2)
                ch_k "Oh!"
                $ KittyX.change_stat("inhibition", 50, -5)
                $ KittyX.change_face("_sadside", 1)
                menu:
                    ch_k ". . . Well. . . maybe you can still kinda[KittyX.like]be in control, anyway?"
                    "I like that idea.":
                        $ KittyX.change_stat("obedience", 200, 10)
                        $ KittyX.change_face("_smile", 1)
                        ch_k "You're so awesome, [KittyX.player_petname]."
                    "This is getting really weird.":
                        $ KittyX.change_stat("love", 200, -10)
                        $ KittyX.change_stat("obedience", 200, -50)
                        $ KittyX.change_stat("inhibition", 50, -15)
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
        $ KittyX.change_face("_sadside", 2)
        ch_k "Oh! Uhm, yeah! [KittyX.Like]I mean. . ."
        $ KittyX.mouth = "_smile"
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
    $ KittyX.change_face("_sadside", 1)
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
                $ KittyX.change_stat("love", 90, 10)
                $ KittyX.change_face("_sly", 1)
                ch_k "Well. . .okay. I {i}did{/i} think that was pretty hot. Also, you're super-cute when you apologize."
                call Kitty_Kissing_Smooch
                ch_k "Okay. We can[KittyX.like]try again."
        "Listen. . . I know it's what you want. Do you want to try again, or not?":

            $ KittyX.change_face("_bemused", 1)
            if "sir" in KittyX.player_petnames:
                if approval_check(KittyX, 850, "O"):
                    ch_k "Ok, fine."
                else:
                    ch_k "Um, not really."
                    $ line = "rude"
            elif approval_check(KittyX, 600, "O"):

                $ KittyX.change_face("_sadside", 1)
                ch_k "You're[KittyX.like]totally impossible."
                $ KittyX.eyes = "_squint"
                ch_k "Maybe you're right."
                ch_k "But I still think you should[KittyX.like] apologize for being a jerk to me."
                menu:
                    extend ""
                    "Okay, I'm sorry I was mean about it.":
                        $ KittyX.change_stat("love", 90, 15)
                        $ KittyX.change_stat("inhibition", 50, 10)
                        $ KittyX.change_face("_bemused", 1)
                        $ KittyX.eyes = "_side"
                        ch_k "That's all you had to say."
                    "Not gonna happen.":
                        if "sir" in KittyX.player_petnames and approval_check(KittyX, 900, "O"):
                            $ KittyX.change_stat("love", 200, -5)
                            $ KittyX.change_stat("obedience", 200, 10)
                            ch_k ". . ."
                        elif approval_check(KittyX,650, "O"):
                            $ KittyX.change_stat("love", 200, -5)
                            $ KittyX.change_stat("obedience", 200, 10)
                            ch_k "I, um. . ."
                        else:
                            $ KittyX.change_stat("love", 200, -10)
                            $ KittyX.change_stat("obedience", 90, -10)
                            $ KittyX.change_stat("obedience", 200, -10)
                            $ KittyX.change_stat("inhibition", 50, -15)
                            "Kitty sighs and rolls her eyes."
                            $ KittyX.change_face("_angry", 1)
                            $ KittyX.eyes = "_side"
                            ch_k "You really don't learn, do you?"
                            $ line = "rude"
                    "Ok, never mind then.":
                        $ KittyX.change_face("_angry", 1)
                        $ KittyX.change_stat("love", 200, -10)
                        $ KittyX.change_stat("obedience", 90, -10)
                        $ KittyX.change_stat("obedience", 200, -10)
                        $ KittyX.change_stat("inhibition", 50, -15)
                        ch_k "Y'know, if you're gonna throw that in my face, forget it."
                        ch_k "I should've[KittyX.like]expected you'd be like that."
                        $ line = "rude"

    $ KittyX.recent_history.append("asked sub")
    $ KittyX.daily_history.append("asked sub")
    if line == "rude":


        call remove_Girl(KittyX)
        $ KittyX.recent_history.append("_angry")
        if not simulation:
            $ renpy.pop_call()
        "[KittyX.name] phases through the floor, leaving you alone. She looked pretty upset."
    elif "sir" in KittyX.player_petnames:

        $ KittyX.change_stat("obedience", 200, 50)
        $ KittyX.player_petnames.append("master")
        $ KittyX.player_petname = "master"
        $ KittyX.eyes = "_squint"
        ch_k ". . . master. . ."
    else:

        $ KittyX.change_stat("obedience", 200, 30)
        $ KittyX.player_petnames.append("sir")
        $ KittyX.player_petname = "sir"
        $ KittyX.eyes = "_squint"
        ch_k ". . . sir."
    return






label Kitty_Master:
    call shift_focus (KittyX)
    $ KittyX.drain_word("asked_to_meet")
    if KittyX.location != Player.location and KittyX not in Player.Party:
        "Suddenly, [KittyX.name] shows up and says she needs to talk to you."

    $ KittyX.location = Player.location
    call set_the_scene (0)
    call show_Girl (KittyX)
    call clear_the_room (KittyX)
    $ KittyX.daily_history.append("relationship")
    call set_Character_taboos
    $ line = 0
    $ KittyX.change_face("_bemused", 1)
    ch_k "[KittyX.player_petname], if you don't mind me saying so. . ."
    ch_k "I think having you be[KittyX.like]in control of our relationship is working out pretty awesome."
    menu:
        extend ""
        "I like it too.":
            $ KittyX.change_face("_sly", 1)
            ch_k "Cool. Maybe we could[KittyX.like]kick it up a notch?"
            menu:
                extend ""
                "Nah. This is just about perfect.":
                    $ KittyX.change_face("_sad", 1)
                    $ KittyX.change_stat("obedience", 200, -15)
                    $ KittyX.change_stat("inhibition", 50, 10)
                    ch_k "Oh. Well, okay, I guess."
                    $ line = "fail"
                "What'd you have in mind?":
                    $ KittyX.eyes = "_side"
                    ch_k "I dunno. I was thinking[KittyX.like]maybe I could start calling you. . . {i}master{/i}?"
                    $ KittyX.eyes = "_squint"
                    ch_k "Would you like that? I think that'd be kinda[KittyX.like]hot."
                    menu:
                        extend ""
                        "Oh, yeah. I'd like that.":
                            ch_k "Cool. . ."
                        "Uhm. . .nah. That's too much.":
                            $ KittyX.change_face("_sad", 1)
                            $ KittyX.change_stat("obedience", 200, -15)
                            $ KittyX.change_stat("inhibition", 50, 5)
                            ch_k "Oh. Well, okay, I guess."
                            $ line = "fail"
                "Actually, I'd prefer we stopped doing it. I don't want to be too controlling.":

                    $ KittyX.change_face("_sly", 1)
                    $ KittyX.change_stat("love", 200, 15)
                    $ KittyX.change_stat("obedience", 200, -10)
                    $ KittyX.change_stat("inhibition", 50, 10)
                    ch_k "Aw, I guess I can't get mad about that. . ."
                    $ line = "fail"
                "Actually, let's stop that. It's creeping me out.":

                    $ KittyX.change_face("_perplexed", 2)
                    $ KittyX.change_stat("love", 200, -10)
                    $ KittyX.change_stat("obedience", 200, -50)
                    $ KittyX.change_stat("inhibition", 50, -15)
                    ch_k "Oh. Sorry. I guess I got[KittyX.like]carried away with it."
                    $ KittyX.blushing = "_blush1"
                    $ line = "embarrassed"
        "As if I care what you think, slut.":

            $ KittyX.change_face("_sad", 1)
            $ KittyX.change_stat("love", 200, -20)
            $ KittyX.change_stat("obedience", 200, 10)
            $ KittyX.change_stat("inhibition", 50, -10)
            menu:
                ch_k "Excuse me?"
                "Sorry. I just don't care what you want.":
                    if approval_check(KittyX, 1400, "LO"):
                        $ KittyX.change_stat("obedience", 200, 10)
                        ch_k "That's so. . ."
                        $ KittyX.change_face("_sly", 1)
                        $ KittyX.change_stat("love", 200, 20)
                        $ KittyX.change_stat("inhibition", 50, 15)
                        ch_k ". . .{i}mean!{/i}"
                    else:
                        $ KittyX.change_stat("love", 200, -15)
                        $ KittyX.change_stat("obedience", 200, -10)
                        $ KittyX.change_stat("inhibition", 50, 5)
                        $ KittyX.change_face("_angry", 1)
                        ch_k "!!!"
                        $ line = "rude"
                "Sorry. I'm just trying to do the \"control\" thing. I thought you'd like it. Too much?":

                    $ KittyX.change_stat("love", 200, 10)
                    $ KittyX.change_stat("obedience", 200, 10)
                    $ KittyX.change_stat("inhibition", 50, 5)
                    ch_k "Oh, okay. Just. . .try not to be so[KittyX.like]mean about it, 'kay?"
        "Not me. It's kind of creepy.":

            $ KittyX.change_face("_sad", 2)
            $ KittyX.change_stat("love", 200, -10)
            $ KittyX.change_stat("obedience", 200, -20)
            $ KittyX.change_stat("inhibition", 50, -25)
            ch_k "Oh. Uhm. . .never mind, then."
            $ line = "embarrassed"

    $ KittyX.history.append("master")
    if line == "rude":
        $ KittyX.recent_history.append("_angry")

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
        $ KittyX.change_stat("obedience", 200, 50)
        $ KittyX.player_petnames.append("master")
        $ KittyX.player_petname = "master"
        ch_k ". . .master."
    return






label Kitty_Sexfriend:
    $ KittyX.location = Player.location
    call set_the_scene (0)
    call show_Girl (KittyX)
    call clear_the_room (KittyX)
    $ KittyX.daily_history.append("relationship")
    call set_Character_taboos
    $ line = 0
    $ KittyX.change_face("_bemused", 1)
    ch_k "So, [KittyX.player_petname]. . .you[KittyX.like]got a second?"
    menu:
        extend ""
        "Not really.":
            $ KittyX.change_face("_angry", 1)
            ch_k "You're such a jerk, [Player.name]!"
            $ KittyX.change_stat("love", 200, -20)
            $ KittyX.change_stat("obedience", 50, 3)
            $ line = "rude"
        "This doesn't sound good.":

            $ KittyX.change_face("_perplexed", 1)
            ch_k "I promise. It's nothing[KittyX.like]bad."
        "Yeah. What's up?":

            pass

    if not line:
        if approval_check(KittyX, 850, "L"):
            $ KittyX.change_face("_bemused", 1)
            ch_k "Well. . . I really like you. You know that, right?"
            menu:
                extend ""
                "I was kinda hoping.":
                    $ KittyX.change_face("_sexy", 1)
                    $ KittyX.change_stat("love", 90, 10)
                    $ KittyX.change_stat("inhibition", 80, 5)
                    ch_k "I was {i}really{/i} hoping you'd say that [KittyX.player_petname]."
                "Really?":

                    ch_k "Uhm. . . [KittyX.like]yeah. I really do."
                "Ugh. Gross":

                    $ KittyX.change_face("_angry", 1)
                    $ KittyX.change_stat("love", 200, -10)
                    $ KittyX.change_stat("obedience", 50, 5)
                    $ KittyX.change_stat("inhibition", 80, -5)
                    ch_k "Y'know, you're such an ass, [Player.name]!"
                    $ line = "rude"

        elif approval_check(KittyX, 1000, "LI"):
            $ KittyX.change_face("_sexy", 1)
            ch_k "I just wanted to tell you. . .I think you're[KittyX.like]kinda cute."
            menu:
                extend ""
                "That's really nice of you to say.":
                    $ KittyX.change_stat("love", 80, 5)
                    $ KittyX.change_stat("inhibition", 80, 5)
                    ch_k "Well, I really mean it."
                "Me? You really think so?":

                    ch_k "Yeah. I {i}really{/i} do."
                "Are you going somewhere with this?":

                    $ KittyX.change_face("_angry")
                    ch_k "Well not anymore, I'm not!"
                    $ line = "rude"
        else:

            $ KittyX.mouth = "_smile"
            $ KittyX.brows = "_sad"
            $ KittyX.eyes = "_side"
            ch_k "This is gonna sound[KittyX.like]really weird."
            menu:
                extend ""
                "Well, you've got me intrigued. Now you {i}have{/i} to tell me.":
                    ch_k "Promise you won't think[KittyX.like]{i}badly{/i}of me?"
                    menu:
                        extend ""
                        "[KittyX.name]. . . I really like you. I promise.":
                            $ KittyX.change_face("_smile")
                            $ KittyX.change_stat("love", 80, 10)
                            $ KittyX.change_stat("inhibition", 80, 5)
                            ch_k "Well. . . okay."
                        "Uhm. . . okay?":

                            ch_k "Well. . ."
                        "No promises.":

                            $ KittyX.change_face("_perplexed",2)
                            $ KittyX.change_stat("inhibition", 80, -5)
                            ch_k "Uhm. . . never mind, then."
                            $ line = "embarrassed"
                "Uhm, I think I've had my fill of {i}weird{/i}, thanks":

                    $ KittyX.change_face("_angry", 1)
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
                $ KittyX.change_face("_perplexed",2)
                $ KittyX.change_stat("love", 200, -10)
                $ KittyX.change_stat("inhibition", 80, -10)
                ch_k "Sorry. I knew this was a mistake."
                $ line = "embarrassed"

    if not line:
        ch_k "And we've[KittyX.like]known each other for a little while, right?"
        menu:
            extend ""
            "Right. . . ":
                pass
            "Okay. Just stop. You're creeping me out.":
                $ KittyX.change_face("_perplexed",2)
                $ KittyX.change_stat("love", 200, -10)
                $ KittyX.change_stat("inhibition", 80, -10)
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
                        $ KittyX.change_face("_smile", 1)
                        $ KittyX.change_stat("love", 80, 10)
                        $ KittyX.change_stat("obedience", 50, 10)
                        $ KittyX.change_stat("inhibition", 200, 50)
                        $ KittyX.change_stat("lust", 200, 5)
                        "Kitty leans in and gives you a gentle kiss on the cheek."
                        ch_k "I can't wait to get started, [KittyX.player_petname]."
                    "That may be the sluttiest thing I've ever heard in my life.":

                        $ KittyX.change_face("_angry", 1)
                        $ KittyX.change_stat("love", 200, -30)
                        $ KittyX.change_stat("obedience", 50, 10)
                        $ KittyX.change_stat("inhibition", 80, -40)
                        ch_k "You're the biggest asshole[KittyX.like]ever, [KittyX.player_petname]!"
                        $ line = "rude"
            "Uhm, to be honest, I'd rather not.":

                $ KittyX.change_face("_sadside",2)
                $ KittyX.change_stat("obedience", 50, 15)
                $ KittyX.change_stat("inhibition", 80, -15)
                ch_k "Oh. Okay."
                ch_k "I[KittyX.like]think I should go now. I've got[KittyX.like]stuff to do."
                $ line = "_sad"
    if line == "harem":
        ch_k "I am -totally- addicted to this dick. . ."
        $ line = 0
    if line == "rude":
        $ KittyX.change_face("_angry", 1)
        $ KittyX.recent_history.append("_angry")
        $ KittyX.change_stat("love", 200, -20)
        $ KittyX.change_stat("obedience", 50, 5)
        $ KittyX.change_stat("inhibition", 80, -10)
        call remove_Girl(KittyX)
        $ KittyX.recent_history.append("_angry")
        "[KittyX.name] storms off in a huff. She seemed pretty mad at you."
    elif line == "embarrassed":
        $ KittyX.change_face("_perplexed", 1)
        $ KittyX.change_stat("love", 200, -10)
        $ KittyX.change_stat("obedience", 50, 5)
        $ KittyX.change_stat("inhibition", 80, -20)
        call remove_Girl(KittyX, transition = easeoutbottom)
        "[KittyX.name] phases through the floor leaving you alone. That was very strange."
    elif line == "_sad":
        call remove_Girl(KittyX, transition = easeoutbottom)
        "[KittyX.name] phases through the floor leaving you alone. You think you may have hurt her feelings."
    else:
        $ KittyX.player_petnames.append("sex friend")
        $ KittyX.change_face("_sly",2)
        $ KittyX.change_stat("inhibition", 80, 10)
        $ KittyX.change_stat("lust", 80, 10)
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
    "As you try to control your rising erection, a voice whispers into your ear,"
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
    call shift_focus (KittyX)
    call set_the_scene
    ch_k ". . ."
    if KittyX in Player.Harem:
        ch_k "Hey, so[KittyX.like]we've been dating,"
    else:
        ch_k "Hey, so[KittyX.like]we've been hanging out,"
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
            $ KittyX.change_face("_smile")
            $ KittyX.change_stat("love", 90, 25)
            $ KittyX.change_stat("obedience", 60, 10)
            $ KittyX.change_stat("inhibition", 80, 30)
            ch_k "Great!"
        "What do you mean by that?":
            $ KittyX.change_face("_bemused")
            ch_k "I don't know, it'd kinda be hot, being your baby girl. . ."
            ch_k "Could'ya call me that?"
            menu:
                extend ""
                "Sounds interesting, fine by me.":
                    $ KittyX.change_face("_smile")
                    $ KittyX.change_stat("love", 90, 17)
                    $ KittyX.change_stat("obedience", 60, 20)
                    $ KittyX.change_stat("inhibition", 80, 25)
                    ch_k "Nice! . . daddy."
                    $ KittyX.player_petname = "daddy"
                "Could you not, please?":
                    $ KittyX.change_stat("obedience", 80, 40)
                    $ KittyX.change_stat("inhibition", 80, 20)
                    $ KittyX.change_face("_sad")
                    ch_k " . . . "
                    ch_k "Huh. K."
                "No, that creeps me out.":
                    $ KittyX.change_stat("love", 90, -15)
                    $ KittyX.change_stat("obedience", 80, 45)
                    $ KittyX.change_stat("inhibition", 70, 5)
                    $ KittyX.change_face("_angry")
                    ch_k "Booo."
        "No, that creeps me out.":
            $ KittyX.change_stat("love", 90, -10)
            $ KittyX.change_stat("obedience", 80, 40)
            $ KittyX.change_stat("inhibition", 70, 10)
            $ KittyX.change_face("_angry")
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
    elif KittyX.likes[Girl.tag] >= 800 or approval_check(Girl, 500, "I", taboo_modifier=3):

        $ TempBonus = 0
    else:

        $ TempBonus = -400

    menu:
        "Hey [KittyX.name], why don't you snag [Girl.name]'s. . ."
        ". . . [Girl.outfit[top]]?" if Girl.outfit["top"]:
            if Girl.outfit["bra"]:

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
                elif approval_check(KittyX, 600, taboo_modifier=1.5, Bonus=TempBonus):
                    $ line = "no"
                else:
                    $ line = "noway"

        ". . . [Girl.outfit[bra]]?" if Girl.outfit["bra"]:
            if Girl.outfit["top"]:

                $ Shy = 1
                if approval_check(KittyX, 1200, taboo_modifier=1, Bonus=TempBonus):


                    $ line = "chest"
                elif approval_check(KittyX, 600, taboo_modifier=0.5, Bonus=TempBonus):

                    $ line = "no"
                else:

                    $ line = "noway"
            else:

                $ Shy = 3
                if approval_check(KittyX, 800, taboo_modifier=2.5, Bonus=(TempBonus*1.5)):
                    $ line = "chest"
                elif approval_check(KittyX, 600, taboo_modifier=1.5, Bonus=TempBonus):
                    $ line = "no"
                else:
                    $ line = "noway"

        ". . . [Girl.outfit[bottom]]?" if Girl.outfit["bottom"]:
            if Girl.outfit["underwear"] or Girl.outfit["hose"] == "_tights":

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
                elif approval_check(KittyX, 800, taboo_modifier=1.5, Bonus=TempBonus):
                    $ line = "no"
                else:
                    $ line = "noway"

        ". . . [Girl.outfit[underwear]]?" if Girl.outfit["underwear"]:
            if Girl.outfit["bottom"] or Girl.outfit["hose"] == "_tights":

                $ Shy = 1
                if approval_check(KittyX, 1000, taboo_modifier=1, Bonus=TempBonus):


                    $ line = "_panties"
                elif approval_check(KittyX, 800, taboo_modifier=0.5, Bonus=TempBonus):

                    $ line = "no"
                else:

                    $ line = "noway"
            else:

                $ Shy = 3
                if approval_check(KittyX, 1000, taboo_modifier=2.5, Bonus=(TempBonus*1.5)):
                    $ line = "_panties"
                elif approval_check(KittyX, 800, taboo_modifier=1.5, Bonus=TempBonus):
                    $ line = "no"
                else:
                    $ line = "noway"

        ". . . [Girl.outfit[hose]]?" if Girl.outfit["hose"]:
            if Girl.outfit["bottom"]:

                $ Shy = 1
                if approval_check(KittyX, 800, taboo_modifier=1, Bonus=TempBonus):


                    $ line = "hose"
                elif approval_check(KittyX, 800, taboo_modifier=0.5, Bonus=TempBonus):

                    $ line = "no"
                else:

                    $ line = "noway"
            elif Girl.outfit["underwear"] or Girl.outfit["hose"] != "_pantyhose":

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
                elif approval_check(KittyX, 800, taboo_modifier=1.5, Bonus=TempBonus):
                    $ line = "no"
                else:
                    $ line = "noway"
        "Never mind.":

            return

    if line == "no":
        $ KittyX.change_face("_sadside", 1)
        $ KittyX.change_stat("love", 90, -(Shy))
        ch_k "I really couldn't do that to her."
        return
    if line == "noway":
        $ KittyX.change_face("_angry", 1)
        $ KittyX.change_stat("love", 90, -(2*Shy))
        $ KittyX.change_stat("obedience", 60, -(Shy))
        ch_k "How could you[KittyX.like]even {i}consider{/i} something like that?"
        return


    $ KittyX.change_stat("obedience", 70, Shy)
    $ KittyX.change_stat("inhibition", 80, Shy)
    "[KittyX.name] sneaks up behind [Girl.name]. . ."

    $ Girl.change_face("_surprised",2)
    if line == "over":
        $ line = Girl.outfit["top"]
        $ Girl.outfit["top"] = ""
        call expression Girl.tag + "_First_Topless" pass (1)
        "She reaches out and snags [Girl.name]'s [line], tugging it through her body."

    elif line == "chest":
        $ line = Girl.outfit["bra"]
        $ Girl.outfit["bra"] = ""
        call expression Girl.tag + "_First_Topless" pass (1)
        if Girl.outfit["top"]:
            "She reaches through [Girl.name]'s [Girl.outfit[top]] and snags her [line]."
        else:
            "She reaches out and snags [Girl.name]'s [line], tugging it free."

    elif line == "legs":
        $ line = Girl.outfit["bottom"]
        $ Girl.outfit["bottom"] = ""
        call expression Girl.tag + "_First_Bottomless" pass (1)
        "She reaches down and snags [Girl.name]'s [line], tugging them through her body."

    elif line == "_panties":
        $ line = Girl.outfit["underwear"]
        $ Girl.outfit["underwear"] = ""
        call expression Girl.tag + "_First_Bottomless" pass (1)
        if Girl.outfit["bottom"]:
            "She reaches down through [Girl.name]'s [Girl.outfit[bottom]] and snags her [line]."
        elif Girl.outfit["hose"]:
            "She reaches down through [Girl.name]'s [Girl.outfit[hose]] and snags her [line]."
        else:
            "She reaches out and snags [Girl.name]'s [line], tugging them free."
    elif line == "hose":
        $ line = Girl.outfit["hose"]
        $ Girl.outfit["hose"] = ""
        call expression Girl.tag + "_First_Bottomless" pass (1)
        if Girl.outfit["bottom"]:
            "She reaches down through [Girl.name]'s [Girl.outfit[bottom]] and snags her [line]."
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

            $ Girl.change_face("_sly")
            $ Girl.change_stat("inhibition", 80, Shy)
            $ Girl.change_stat("lust", 80, 2)
            "[Girl.name] glances back in surprise, but then breaks into a quick smile."
        elif approval:

            $ Girl.change_face("_angry", 1)
            $ Girl.change_stat("love", 90, -(Shy))
            "[Girl.name] glances back in surprise, and then glances over at you with a glare."
        else:
            $ Girl.change_face("_angry",2)
            $ Girl.change_stat("love", 90, -(Shy))
            "[Girl.name] glances back in surprise, and then glances over at you with a glare."
            "She storms away in disgust."

    elif Shy <= 2:

        if approval >= 2:

            $ Girl.change_face("_sly")
            $ Girl.change_stat("inhibition", 80, Shy)
            $ Girl.change_stat("lust", 80, Shy)
            "[Girl.name] glances back in surprise, but then breaks into a quick smile."
            "She then just leans back, unconcerned."
        elif approval or Girl == JeanX:

            $ Girl.change_face("_angry", 1)
            $ Girl.change_stat("love", 90, -(Shy))
            $ Girl.change_stat("inhibition", 80, -(Shy))
            $ Girl.change_stat("lust", 80, Shy)
            "[Girl.name] glances back in surprise, and then glances over at you with a glare."
            if Girl != JeanX:
                $ Girl.change_face("_sadside",2)
                "She settles back down with a little embarassment."
        else:
            $ Girl.change_face("_angry",2)
            $ Girl.change_stat("love", 90, -(Shy))
            $ Girl.change_stat("inhibition", 80, -(Shy))
            "[Girl.name] glances back in surprise, and then glances over at you with a glare."
            "She dashes away in embarassment."
    else:

        if approval >= 2:

            $ Girl.change_face("_sly")
            $ Girl.change_stat("love", 90, 1)
            $ Girl.change_stat("inhibition", 80, Shy)
            $ Girl.change_stat("lust", 80, 2*Shy)
            "[Girl.name] glances back in surprise, but then breaks into a quick smile."
            "She looks around, daring anyone to comment."
        elif approval or Girl == JeanX:

            $ Girl.change_face("_angry",2)
            $ Girl.change_stat("love", 90, -(Shy))
            $ Girl.change_stat("inhibition", 80, -(Shy))
            "[Girl.name] glances back in surprise, and then glances over at you with a glare."
            if Girl != JeanX:
                "She seems really mortified, but stands her ground."
        else:
            $ Girl.change_face("_angry",2)
            $ Girl.change_stat("love", 90, -(Shy))
            $ Girl.change_stat("inhibition", 80, -(Shy))
            "[Girl.name] glances back in surprise, and then glances over at you with a glare."
            "She dashes away in embarassment."



    if approval:
        $ Girl.check_if_likes(KittyX,900,(2*Shy), 1)
        $ KittyX.check_if_likes(Girl,900,(2*Shy), 1)
        $ Girl.add_word(1,"yoinked")
    else:
        call remove_Girl(Girl)
        $ Girl.check_if_likes(KittyX,900,-(2*Shy), 1)

    if Girl == JeanX and approval < 2:
        "With a quick nod, her clothes come flying back to her."
        $ Girl.drain_word("yoinked")
        $ Girl.change_outfit()
        "[KittyX.name]'s left a little dazed."
    elif TempBonus > 0:
        if approval < 2:

            $ KittyX.change_face("_sly")
            $ KittyX.change_stat("love", 80, 1)
            "[KittyX.name] smiles triumphantly."
        else:

            $ KittyX.change_face("_angry", eyes = "_side")
            "[KittyX.name] seems a bit annoyed at [Girl.name]'s attitude."

    elif not approval:

        $ KittyX.change_face("_sly")
        $ KittyX.change_stat("lust", 80, Shy)
        "[KittyX.name] seems a bit uncertain about the whole thing."
    else:

        $ KittyX.change_face("_sly")
        $ KittyX.change_stat("love", 80, 1)
        $ KittyX.change_stat("lust", 80, Shy)
        "[KittyX.name] laughs under her breath and waggles the [line] at you."
    return




label Kitty_Kate:
    $ KittyX.location = Player.location
    call set_the_scene (0)
    call show_Girl (KittyX)
    call set_Character_taboos
    $ line = 0
    $ KittyX.change_face("_bemused", 1)
    ch_k "Hey, [KittyX.player_petname]. . .you[KittyX.like]got a second?"
    menu:
        extend ""
        "Not really.":
            $ KittyX.change_face("_angry", 1)
            ch_k "You're such a jerk, [Player.name]!"
            $ KittyX.change_stat("love", 200, -10)
            $ KittyX.change_stat("obedience", 50, 3)
        "Yeah. What's up?":

            pass
    $ KittyX.names.append("Kate")
    ch_k "I just wanted to let you know, I'm going by \"Kate\" now!"
    $ KittyX.name = "Kate"
    menu:
        extend ""
        "Oh no you aren't.":
            $ KittyX.change_stat("love", 90, -10)
            $ KittyX.change_stat("obedience", 50, 10)
            $ KittyX.change_stat("inhibition", 80, -10)
            $ KittyX.change_face("_angry", 2)
            ch_k "!!!"
            if approval_check(KittyX, 1200, "LO") or approval_check(KittyX, 500, "O"):
                $ KittyX.name = "Kitty"
                $ KittyX.change_face("_sadside", 1)
                $ KittyX.change_stat("obedience", 90, 10)
                $ KittyX.change_stat("inhibition", 80, -5)
                ch_k "Well. . . ok. . ."
            else:
                ch_k "You're not my supervisor!"
        "That's a good fit for you.":
            $ KittyX.change_face("_smile", 1)
            $ KittyX.change_stat("love", 60, 5)
            $ KittyX.change_stat("love", 90, 5)
            $ KittyX.change_stat("inhibition", 60, 5)
            ch_k "Thanks!"
        "I always thought \"Kitty\" sounded pretty.":
            $ KittyX.name = "Kitty"
            $ KittyX.change_stat("love", 90, 5)
            $ KittyX.change_stat("obedience", 70, 5)
            $ KittyX.change_stat("inhibition", 50, 5)
            ch_k "Oh, well I guess if you really like \"Kitty,\" I can understand that. . ."
        "Why?":
            $ KittyX.names.append("Katherine")
            ch_k "Well, my full name is \"Katherine Pryde\", and I thought \"Kate\" sounded more grown-up."
            menu:
                extend ""
                "Oh, ok then.":
                    $ KittyX.change_face("_smile", 1)
                    $ KittyX.change_stat("love", 60, 5)
                    $ KittyX.change_stat("love", 90, 5)
                    $ KittyX.change_stat("inhibition", 60, 5)
                    ch_k ". . ."
                "No, it sounds silly.":
                    $ KittyX.change_stat("love", 90, -10)
                    $ KittyX.change_stat("obedience", 50, 10)
                    $ KittyX.change_stat("inhibition", 80, -10)
                    $ KittyX.change_face("_angry", 2)
                    ch_k "!!!"
                    if approval_check(KittyX, 1200, "LO") or approval_check(KittyX, 500, "O"):
                        $ KittyX.name = "Kitty"
                        $ KittyX.change_face("_sadside", 1)
                        $ KittyX.change_stat("obedience", 90, 10)
                        $ KittyX.change_stat("inhibition", 80, -5)
                        ch_k "Well. . . ok. . ."
                    else:
                        ch_k "You're not my supervisor!"
                "I suppose, but \"Kitty\" is such a pretty name.":
                    $ KittyX.change_stat("love", 90, 5)
                    $ KittyX.change_stat("inhibition", 50, 5)
                    if approval_check(KittyX, 800, "LO"):
                        $ KittyX.name = "Kitty"
                        $ KittyX.change_stat("obedience", 70, 5)
                        ch_k "Well, I guess if you prefer it. . ."
                    else:
                        ch_k "Well. . . too bad."
                "Why not \"Katherine\" then?":
                    $ KittyX.change_stat("obedience", 70, 5)
                    if approval_check(KittyX, 1200, "LO") or approval_check(KittyX, 500, "0"):
                        $ KittyX.name = "Katherine"
                        $ KittyX.change_stat("obedience", 90, 5)
                        ch_k "I suppose I could. . ."
                    else:
                        ch_k "I don't really like it that much. . ."
                        menu:
                            extend ""
                            "Ok, \"Kate\" it is then.":
                                $ KittyX.name = "Kate"
                                $ KittyX.change_face("_smile", 1)
                                $ KittyX.change_stat("love", 60, 5)
                                $ KittyX.change_stat("love", 90, 5)
                                $ KittyX.change_stat("inhibition", 60, 5)
                                ch_k ". . ."
                            "Ok, then back to \"Kitty?\"":
                                $ KittyX.change_stat("love", 90, 5)
                                $ KittyX.change_stat("inhibition", 50, 5)
                                if approval_check(KittyX, 800, "LO"):
                                    $ KittyX.name = "Kitty"
                                    $ KittyX.change_stat("obedience", 70, 5)
                                    ch_k "I suppose, if you prefer it that way. . ."
                                else:
                                    ch_k "Well. . . too bad."



    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
