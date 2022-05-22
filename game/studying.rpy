label Study_Session(temp_Girls=[]):

    $ Party = []

    $ temp_Girls = all_Girls[:]
    while temp_Girls:
        if temp_Girls[0].location == bg_current:
            $ Party.append(temp_Girls[0])
        $ temp_Girls.remove(temp_Girls[0])

    if not Party:
        "There's nobody here to study with."
        menu:
            "Study anyway?"
            "Yes":
                $ Player.XP += 5
                $ round -= 30 if round >= 30 else round
            "Never mind.":
                pass
        return

    $ renpy.random.shuffle(Party)

    if time_index >= 3:
        if Party[0] == JubesX and len(Party) < 2:

            pass
        else:
            if EmmaX in Party:
                ch_e "It's a little late for a study session, maybe tomorrow."
            elif Party[0] == RogueX:
                ch_r "It's a little late for studying, maybe tomorrow."
            elif Party[0] == KittyX:
                ch_k "It's kinda late for studying. . . Tomorrow?"
            elif Party[0] == LauraX:
                ch_l "It's late. Maybe tomorrow."
            elif Party[0] == JeanX:
                ch_j "-Yawn- Maybe tomorrow. . ."
            elif Party[0] == StormX:
                ch_s "It is getting a bit late for study."
            elif Party[0] == JubesX:
                ch_v "Well, it is getting kinda late. . ."
                ch_v "I don't think it'd be good for you guys. . ."
            $ Party = []
            return

    if round <= 30:
        if EmmaX in Party:
            ch_e "I'm afraid I was just about to take a break, perhaps another time. . ."
        elif Party[0] == RogueX:
            ch_r "I don't know that there's time for that, maybe if we wait a bit. . ."
        elif Party[0] == KittyX:
            ch_k "I don't know that there's time for that, maybe if we wait a bit. . ."
        elif Party[0] == LauraX:
            ch_l "I was about to take a break, maybe wait a bit."
        elif Party[0] == JeanX:
            ch_j "I need a break, gimme a minute. . ."
        elif Party[0] == StormX:
            ch_s "I need a quick break, perhaps in a few minutes."
        elif Party[0] == JubesX:
            ch_v "We could maybe get some snacks first. . ."
        $ Party = []
        return

    elif EmmaX in Party and len(Party) >= 2:
        ch_e "I suppose you could both use some work."
    else:
        if EmmaX in Party:
            ch_e "Very well."
        elif Party[0] == RogueX:
            ch_r "Sure."
        elif Party[0] == KittyX:
            ch_k "Sure."
        elif Party[0] == LauraX:
            ch_l "Fine."
        elif Party[0] == JeanX:
            ch_j "I guess."
        elif Party[0] == StormX:
            ch_s "I suppose we could go over a few things. . ."
        elif Party[0] == JubesX:
            ch_v "I guess we could study. . ."


    $ Player.recent_history.append("study")
    $ Player.XP += 5
    $ primary_action = 0
    $ Line = renpy.random.choice(["you run you through some basic routines, it's fairly uneventful.",
                    "You study up for the mutant biology test.",
                    "You study for the math quiz.",
                    "You get bored and discuss student gossip instead.",
                    "You study for a few hours, that was fun.",
                    "You spend the next few hours studying the lit test.",
                    "You study for the game design course."])
    "[Line]"
    $ Line = 0

    $ Party[0].change_stat("love", 80, 2)
    $ Party[0].XP += 5
    if len(Party) >= 2:
        $ Party[1].change_stat("love", 80, 2)
        $ Party[0].GLG(Party[1],700,5,1)
        $ Party[1].GLG(Party[0],700,5,1)
        $ Party[1].XP += 5


    $ D20 = renpy.random.randint(1, 20)


    if len(Party) >= 2 and EmmaX in Party and "three" not in EmmaX.history:
        $ Line = "no"

    if Line != "no" and D20 >= 10:
        call Frisky_Study
    else:

        if EmmaX in Party:
            ch_e "I'm afraid it's getting a bit late, we should wrap this up. . ."
        elif Party[0] == RogueX:
            ch_r "It's getting a bit late, we should wrap this up. . ."
        elif Party[0] == KittyX:
            ch_k "It's kinda late, we should probably stop. . ."
        elif Party[0] == LauraX:
            ch_l "I'm bored now."
        elif Party[0] == JeanX:
            ch_j "Ok, that's enough of that. . ."
        elif Party[0] == StormX:
            ch_s "I think that will be enough for now."
        elif Party[0] == JubesX:
            ch_v "Ugh, my head hurts!"
        $ Player.XP += 5
    $ Line = 0
    $ Party = []
    if time_index >= 3:
        $ round = 10
        return
    call wait
    call girls_location
    return




label Frisky_Study(Prime_Bonus=0, Second=0, Line=0, Second_Bonus=0):




    call shift_focus (Party[0])

    if len(Party) >= 2:
        $ Second = Party[1]

    if Party[0] == EmmaX and "classcaught" not in EmmaX.history:

        "[EmmaX.name] leans close to you for a moment, but then catches herself and pulls back."
    elif Party[0] == EmmaX and Second and ("three" not in EmmaX.history or "taboo" not in EmmaX.history):

        "[EmmaX.name] starts to lean close to you, but then notices [Second.name]."
        $ Party[0].change_face("_sly",1,Eyes="_side")
        "She stops immediately and looks a bit embarrassed."
    elif D20 > 17 and approval_check(Party[0], 1000) and Party[0].action_counter["blowjob"] > 5:
        $ Line = "blowjob"
    elif D20 > 14 and Party[0] == JubesX and approval_check(Party[0], 1000) and Party[0].action_counter["blowjob"] > 5:
        $ Line = "blowjob"
    elif D20 > 14 and approval_check(Party[0], 1000) and Party[0].action_counter["handjob"] >= 5:
        $ Line = "handjob"
    elif D20 > 10 and (approval_check(Party[0], 1300) or (Party[0].action_counter["masturbation"] and approval_check(Party[0], 1000))) and Party[0].lust >= 70:
        $ Line = "masturbate"
    elif D20 > 10 and approval_check(Party[0], 1200) and Party[0].lust >= 30:
        $ Line = "strip"
    elif approval_check(Party[0], 700) and Party[0].action_counter["kiss"] > 1:
        $ Line = "kiss"
    elif approval_check(Party[0], 500):
        $ Line = "snuggle"
        if Party[0] != JeanX or approval_check(Party[0], 700,"L"):
            $ Line = "snuggle"
        else:
            "[Party[0].name] briefly rests against your shoulder, but then shakes herself and pulls back."
            $ Line = 0


    if not Line and len(Party) >= 2 and not Prime_Bonus:


        $ Party.reverse()
        call Frisky_Study (1)
        return
    elif not Line or Line == "strip":
        pass
    elif Line == "blowjob":
        $ Party[0].change_face("_sly")
        if Party[0] == KittyX:
            "[KittyX.name] reaches her hand through your textbook and you can feel it in your lap."
            "She unzips you pants and pulls your dick out, stroking it slowly."
            "She then dives her head under the book, and starts to lick it."
        else:
            "[Party[0].name] get predatory grin, and begins to unzip your pants."
            "She pulls your dick out and pops it into her mouth."
    elif Line == "handjob":
        $ Party[0].change_face("_sly")
        if Party[0] == KittyX:
            "[KittyX.name] reaches her hand through your textbook and you can feel it in your lap."
            "She runs her finger along your erection, her hand passing through the jeans to touch your bare skin."
            "She unzips you pants and pulls your dick out, stroking it slowly."
        elif Party[0] == JeanX and D20 > 15:
            "As you study, you feel something stirring along your cock, a slight hint of pressure."
            menu:
                "Go with it":
                    "After a moment, you can feel a tugging on your zipper as it releases."
                    "You cock floats free of your pants, lifted half under its own power and half due to. . ."
                    $ Party[0].change_face("_sly",Eyes="leftside")
                    "You glance over at [JeanX.name] and she smiles mischieviously as the pressure builds."
                    "You can feel a strong rubbing sensation along the length of the shaft, up and down."
                    "It feels similar to a hand or mouth wrapped around itpassing from root to tip and back."
                    "[JeanX.name] throws an arm over your shoulders and leans against you as this pressure continues. . ."
                "Flex your power to shut it down":
                    $ Party[0].change_face("_sad")
                    $ Party[0].change_stat("love", 80, -2)
                    $ Party[0].change_stat("obedience", 50, 3)
                    $ Party[0].change_stat("obedience", 80, 5)
                    $ Party[0].change_stat("inhibition", 90, -2)
                    ch_j "Aw. . ."
                    $ Line = 0
        else:
            "[Party[0].name] get predatory grin, and begins to unzip your pants."
            "She pulls your dick out and begins to slowly stroke it."
    elif Line == "masturbate":
        $ Party[0].change_face("_sly", Eyes="_side")
        "[Party[0].name] leans back a bit and starts to rub herself."
        $ primary_action = "masturbation"
    elif Line == "kiss":
        "[Party[0].name] leans close to you, and leans in for a kiss."
    elif Line == "snuggle":
        "[Party[0].name] leans close to you and you spend the rest of the study session nuzzled close."


    if Line == "strip":
        if Party[0] != EmmaX and EmmaX in Party and approval_check(EmmaX, 1200) and EmmaX.lust >= 30:
            $ Party.reverse()

        if StormX in Party and renpy.random.randint(1,2) > 1:
            $ Party.reverse()


        call Group_Strip_Study
    elif Line and len(Party) < 2:

        call expression Party[0].tag + "_SexAct" pass (Line)
    elif Line:

        if Line == "snuggle":
            call Date_Sex_Break (Party[0], Second, 2)
            if _return == 3:
                $ Second.change_face("_angry")
                "[Second.name] glowers at you a bit."
                $ Party[0].GLG(Second,700,5,1)
                $ Second.GLG(Party[0],700,5,1)
        else:
            call Date_Sex_Break (Party[0], Second)

        if _return == 4:
            if Line == "blowjob":
                "[Party[0].name] lets your dick fall out of her mouth."
                "You zip your pants back up."
            elif Line == "handjob":
                "[Party[0].name] lets your dick drop into your lap."
                "You zip your pants back up."
            else:
                "[Party[0].name] stops what she's doing."

            $ Party[0].change_face("_sad")
            if Party[0] == RogueX:
                ch_r "Buzzkill."
            elif Party[0] == KittyX:
                ch_k "Booo."
            elif Party[0] == EmmaX:
                ch_e "Oh, very well."
            elif Party[0] == LauraX:
                ch_l "Be that way."
            elif Party[0] == JeanX:
                ch_j "Aw. . ."
            elif Party[0] == StormX:
                ch_s "How unfortunate."
            elif Party[0] == JubesX:
                ch_v "Jerk!"
        elif Line != "snuggle":


            if _return == 3:

                if Party[0] == RogueX:
                    ch_r "Mind if I continue?"
                elif Party[0] == KittyX:
                    ch_k "I can keep going?"
                elif Party[0] == EmmaX:
                    ch_e "You don't mind if I continue?"
                elif Party[0] == LauraX:
                    ch_l "Keep going?"
                elif Party[0] == JeanX:
                    ch_j "Ok, back to it. . ."
                elif Party[0] == StormX:
                    ch_s "Well, would you like me to stop?"
                elif Party[0] == JubesX:
                    ch_v "Not interested?"
                menu:
                    extend ""
                    "Go ahead.":
                        $ Party[0].change_face("_sly")
                        if Party[0] == RogueX:
                            ch_r "Nice."
                        elif Party[0] == KittyX:
                            ch_k "Cool."
                        elif Party[0] == EmmaX:
                            ch_e "Lovely."
                        elif Party[0] == LauraX:
                            ch_l "Un."
                        elif Party[0] == JeanX:
                            ch_j "Mmm. . ."
                        elif Party[0] == StormX:
                            ch_s "That is what I'd hoped. . ."
                        elif Party[0] == JubesX:
                            ch_v "Sweet!"
                    "We should stop.":
                        $ Party[0].change_face("_sad")
                        if Party[0] == RogueX:
                            ch_r "Hmph."
                        elif Party[0] == KittyX:
                            ch_k "Lame."
                        elif Party[0] == EmmaX:
                            ch_e "Spoil sport."
                        elif Party[0] == LauraX:
                            ch_l "Grr."
                        elif Party[0] == JeanX:
                            ch_j "Aw. . ."
                        elif Party[0] == StormX:
                            ch_s "Pity."
                        elif Party[0] == JubesX:
                            ch_v "Aw!"
                        $ Party[0].change_face("_normal")
                        return

            call expression Party[0].tag + "_SexAct" pass (Line)
        if len(Party) >= 2:
            $ Party[0].GLG(Party[1],900,10,1)
            $ Party[1].GLG(Party[0],900,10,1)
    else:


        return
    if Party:
        $ Party[0].add_word(1,0,0,0,"frisky")
    if len(Party) >= 2:
        $ Party[1].add_word(1,0,0,0,"frisky")

    "Well that was certainly a productive use of your study time. . ."
    return
