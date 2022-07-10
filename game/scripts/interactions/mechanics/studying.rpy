label study:
    $ Player.Party = []

    python:
        for G in all_Girls:
            if G.location == Player.location:
                Player.Party.append(G)

    if not Player.Party:
        "There's nobody here to study with."
        menu:
            "Study anyway?"
            "Yes":
                $ Player.XP += 5

                $ round -= 30 if round >= 30 else round
            "Never mind.":
                return

        call wait
        call set_Girls_locations

        return

    $ renpy.random.shuffle(Player.Party)

    if time_index > 2:
        if Player.Party[0] == JubesX and len(Player.Party) < 2:
            pass
        else:
            if EmmaX in Player.Party:
                ch_e "It's a little late for a study session, maybe tomorrow."
            elif Player.Party[0] == RogueX:
                ch_r "It's a little late for studying, maybe tomorrow."
            elif Player.Party[0] == KittyX:
                ch_k "It's kinda late for studying. . . Tomorrow?"
            elif Player.Party[0] == LauraX:
                ch_l "It's late. Maybe tomorrow."
            elif Player.Party[0] == JeanX:
                ch_j "-Yawn- Maybe tomorrow. . ."
            elif Player.Party[0] == StormX:
                ch_s "It is getting a bit late for study."
            elif Player.Party[0] == JubesX:
                ch_v "Well, it is getting kinda late. . ."
                ch_v "I don't think it'd be good for you guys. . ."

            $ Player.Party = []

            return

    if round <= 30:
        if EmmaX in Player.Party:
            ch_e "I'm afraid I was just about to take a break, perhaps another time. . ."
        elif Player.Party[0] == RogueX:
            ch_r "I don't know that there's time for that, maybe if we wait a bit. . ."
        elif Player.Party[0] == KittyX:
            ch_k "I don't know that there's time for that, maybe if we wait a bit. . ."
        elif Player.Party[0] == LauraX:
            ch_l "I was about to take a break, maybe wait a bit."
        elif Player.Party[0] == JeanX:
            ch_j "I need a break, gimme a minute. . ."
        elif Player.Party[0] == StormX:
            ch_s "I need a quick break, perhaps in a few minutes."
        elif Player.Party[0] == JubesX:
            ch_v "We could maybe get some snacks first. . ."

        $ Player.Party = []

        return

    if Player.Party[0] == RogueX:
        ch_r "Sure."
    elif Player.Party[0] == KittyX:
        ch_k "Sure."
    elif Player.Party[0] == EmmaX:
        ch_e "Very well."
    elif Player.Party[0] == LauraX:
        ch_l "Fine."
    elif Player.Party[0] == JeanX:
        ch_j "I guess."
    elif Player.Party[0] == StormX:
        ch_s "I suppose we could go over a few things. . ."
    elif Player.Party[0] == JubesX:
        ch_v "I guess we could study. . ."

    $ Player.XP += 5

    $ line = renpy.random.choice(["you run you through some basic routines, it's fairly uneventful.",
        "You study up for the mutant biology test.",
        "You study for the math quiz.",
        "You get bored and discuss student gossip instead.",
        "You study for a few hours, that was fun.",
        "You spend the next few hours studying the lit test.",
        "You study for the game design course."])
    "[line]"

    $ temp_Girls = Player.Party[:]

    while temp_Girls:
        call change_Girl_stat(temp_Girls[0], "love", 2)
        $ temp_Girls[0].XP += 5

        $ temp_Girls.remove(temp_Girls[0])

    if Player.Party[0] == RogueX:
        ch_r "It's getting a bit late, we should wrap this up. . ."
    elif Player.Party[0] == KittyX:
        ch_k "It's kinda late, we should probably stop. . ."
    elif Player.Party[0] == EmmaX:
        ch_e "I'm afraid it's getting a bit late, we should wrap this up. . ."
    elif Player.Party[0] == LauraX:
        ch_l "I'm bored now."
    elif Player.Party[0] == JeanX:
        ch_j "Ok, that's enough of that. . ."
    elif Player.Party[0] == StormX:
        ch_s "I think that will be enough for now."
    elif Player.Party[0] == JubesX:
        ch_v "Ugh, my head hurts!"

    $ Player.XP += 5

    $ Player.Party = []

    if time_index > 2:
        $ round = 10

        return

    call wait

    return















label frisky_study(Prime_Bonus=0, Second_Bonus=0):
    $ shift_focus(Player.Party[0])

    if len(Player.Party) >= 2:
        $ Second = Player.Party[1]

    if Player.Party[0] == EmmaX and "classcaught" not in EmmaX.history:
        "[EmmaX.name] leans close to you for a moment, but then catches herself and pulls back."
    elif Player.Party[0] == EmmaX and Second and ("threesome" not in EmmaX.history or "taboo" not in EmmaX.history):
        "[EmmaX.name] starts to lean close to you, but then notices [Second.name]."

        $ Player.Party[0].change_face("sly", 1, eyes = "side")

        "She stops immediately and looks a bit embarrassed."
    elif D20 > 17 and approval_check(Player.Party[0], 1000) and Player.Party[0].permanent_History["blowjob"] > 5:
        $ action = "blowjob"
    elif D20 > 14 and Player.Party[0] == JubesX and approval_check(Player.Party[0], 1000) and Player.Party[0].permanent_History["blowjob"] > 5:
        $ action = "blowjob"
    elif D20 > 14 and approval_check(Player.Party[0], 1000) and Player.Party[0].permanent_History["handjob"] >= 5:
        $ action = "handjob"
    elif D20 > 10 and (approval_check(Player.Party[0], 1300) or (Player.Party[0].permanent_History["masturbation"] and approval_check(Player.Party[0], 1000))) and Player.Party[0].lust >= 70:
        $ action = "masturbation"
    elif D20 > 10 and approval_check(Player.Party[0], 1200) and Player.Party[0].lust >= 30:
        $ action = "striptease"
    elif approval_check(Player.Party[0], 700) and Player.Party[0].permanent_History["kiss"] > 1:
        $ action = "kiss"
    elif approval_check(Player.Party[0], 500):
        $ action = "snuggle"

        if Player.Party[0] == JeanX and not approval_check(Player.Party[0], 700, "L"):
            "[Player.Party[0].name] briefly rests against your shoulder, but then shakes herself and pulls back."

            $ action = None

    if not action and len(Player.Party) >= 2 and not Prime_Bonus:
        $ Player.Party.reverse()

        call frisky_study (1)

        return
    elif not action or action == "striptease":
        pass
    elif action == "blowjob":
        $ Player.Party[0].change_face("sly")

        if Player.Party[0] == KittyX:
            "[KittyX.name] reaches her hand through your textbook and you can feel it in your lap."
            "She unzips you pants and pulls your dick out, stroking it slowly."
            "She then dives her head under the book, and starts to lick it."
        else:
            "[Player.Party[0].name] gets a predatory grin, and begins to unzip your pants."
            "She pulls your dick out and pops it into her mouth."
    elif action == "handjob":
        $ Player.Party[0].change_face("sly")

        if Player.Party[0] == KittyX:
            "[KittyX.name] reaches her hand through your textbook and you can feel it in your lap."
            "She runs her finger along your erection, her hand passing through the jeans to touch your bare skin."
            "She unzips you pants and pulls your dick out, stroking it slowly."
        elif Player.Party[0] == JeanX and D20 > 15:
            "As you study, you feel something stirring along your cock, a slight hint of pressure."

            menu:
                "Go with it":
                    "After a moment, you can feel a tugging on your zipper as it releases."
                    "You cock floats free of your pants, lifted half under its own power and half due to. . ."

                    $ Player.Party[0].change_face("sly", eyes = "leftside")

                    "You glance over at [JeanX.name] and she smiles mischieviously as the pressure builds."
                    "You can feel a strong rubbing sensation along the length of the shaft, up and down."
                    "It feels similar to a hand or mouth wrapped around itpassing from root to tip and back."
                    "[JeanX.name] throws an arm over your shoulders and leans against you as this pressure continues. . ."
                "Flex your power to shut it down":
                    $ Player.Party[0].change_face("sad")
                    call change_Girl_stat(Player.Party[0], "love", -2)
                    call change_Girl_stat(Player.Party[0], "obedience", 3)
                    call change_Girl_stat(Player.Party[0], "obedience", 5)
                    call change_Girl_stat(Player.Party[0], "inhibition", -2)

                    ch_j "Aw. . ."

                    $ action = None
        else:
            "[Player.Party[0].name] gets a predatory grin, and begins to unzip your pants."
            "She pulls your dick out and begins to slowly stroke it."

    elif action == "masturbation":
        $ Player.Party[0].change_face("sly", eyes = "side")

        "[Player.Party[0].name] leans back a bit and starts to rub herself."
    elif action == "kiss":
        "[Player.Party[0].name] leans close to you, and leans in for a kiss."
    elif action == "snuggle":
        "[Player.Party[0].name] leans close to you and you spend the rest of the study session nuzzled close."

    if action == "striptease":
        if Player.Party[0] != EmmaX and EmmaX in Player.Party and approval_check(EmmaX, 1200) and EmmaX.lust >= 30:
            $ Player.Party.reverse()

        if StormX in Player.Party and renpy.random.randint(1, 2) > 1:
            $ Player.Party.reverse()

        call Group_Strip_Study
    elif action in all_actions and len(Player.Party) == 1:
        if check_if_alone(Player.Party[0]) and Player.Party[0].taboo == 20:
            $ Player.Party[0].taboo = 0
            $ taboo = 0

        call before_action(Player.Party[0], action)
    elif action:
        if action == "snuggle" and len(Player.Party) == 2:
            call check_if_second_minds(Player.Party[0], Player.Party[1])

            if _return == 3:
                $ Player.Party[1].change_face("angry")

                "[Player.Party[1].name] glowers at you a bit."

                $ Player.Party[0].check_if_likes(Second, 700, 5, 1)

                $ Player.Party[1].check_if_likes(Player.Party[0], 700, 5, 1)
        elif len(Player.Party) == 2:
            call check_if_second_minds(Player.Party[0], Player.Party[1])

        if _return == 4:
            if action == "blowjob":
                "[Player.Party[0].name] lets your dick fall out of her mouth."
                "You zip your pants back up."
            elif action == "handjob":
                "[Player.Party[0].name] lets your dick drop into your lap."
                "You zip your pants back up."
            else:
                "[Player.Party[0].name] stops what she's doing."

            $ Player.Party[0].change_face("sad")

            if Player.Party[0] == RogueX:
                ch_r "Buzzkill."
            elif Player.Party[0] == KittyX:
                ch_k "Booo."
            elif Player.Party[0] == EmmaX:
                ch_e "Oh, very well."
            elif Player.Party[0] == LauraX:
                ch_l "Be that way."
            elif Player.Party[0] == JeanX:
                ch_j "Aw. . ."
            elif Player.Party[0] == StormX:
                ch_s "How unfortunate."
            elif Player.Party[0] == JubesX:
                ch_v "Jerk!"
        elif action != "snuggle":
            if _return == 3:
                if Player.Party[0] == RogueX:
                    ch_r "Mind if I continue?"
                elif Player.Party[0] == KittyX:
                    ch_k "I can keep going?"
                elif Player.Party[0] == EmmaX:
                    ch_e "You don't mind if I continue?"
                elif Player.Party[0] == LauraX:
                    ch_l "Keep going?"
                elif Player.Party[0] == JeanX:
                    ch_j "Ok, back to it. . ."
                elif Player.Party[0] == StormX:
                    ch_s "Well, would you like me to stop?"
                elif Player.Party[0] == JubesX:
                    ch_v "Not interested?"

                menu:
                    extend ""
                    "Go ahead.":
                        $ Player.Party[0].change_face("sly")

                        if Player.Party[0] == RogueX:
                            ch_r "Nice."
                        elif Player.Party[0] == KittyX:
                            ch_k "Cool."
                        elif Player.Party[0] == EmmaX:
                            ch_e "Lovely."
                        elif Player.Party[0] == LauraX:
                            ch_l "Un."
                        elif Player.Party[0] == JeanX:
                            ch_j "Mmm. . ."
                        elif Player.Party[0] == StormX:
                            ch_s "That is what I'd hoped. . ."
                        elif Player.Party[0] == JubesX:
                            ch_v "Sweet!"
                    "We should stop.":
                        $ Player.Party[0].change_face("sad")

                        if Player.Party[0] == RogueX:
                            ch_r "Hmph."
                        elif Player.Party[0] == KittyX:
                            ch_k "Lame."
                        elif Player.Party[0] == EmmaX:
                            ch_e "Spoil sport."
                        elif Player.Party[0] == LauraX:
                            ch_l "Grr."
                        elif Player.Party[0] == JeanX:
                            ch_j "Aw. . ."
                        elif Player.Party[0] == StormX:
                            ch_s "Pity."
                        elif Player.Party[0] == JubesX:
                            ch_v "Aw!"

                        $ Player.Party[0].change_face("normal")

                        return

            if check_if_alone(Player.Party[0]) and Player.Party[0].taboo == 20:
                $ Player.Party[0].taboo = 0
                $ taboo = 0

            call before_action(Player.Party[0], action)
        if len(Player.Party) >= 2:
            $ Player.Party[0].check_if_likes(Player.Party[1], 900, 10, 1)
            $ Player.Party[1].check_if_likes(Player.Party[0], 900, 10, 1)
    else:
        return

    if Player.Party:
        $ Player.Party[0].add_word(1, 0, 0, 0, "frisky")
    if len(Player.Party) >= 2:
        $ Player.Party[1].add_word(1, 0, 0, 0, "frisky")

    "Well that was certainly a productive use of your study time. . ."

    return
