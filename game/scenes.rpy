



label Study_Session(BO=[]):

    $ Party = []

    $ BO = all_Girls[:]
    while BO:
        if BO[0].location == bg_current:
            $ Party.append(BO[0])
        $ BO.remove(BO[0])

    if not Party:
        "There's nobody here to study with."
        menu:
            "Study anyway?"
            "Yes":
                $ Player.XP += 5
                $ Round -= 30 if Round >= 30 else Round
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

    if Round <= 30:
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
        $ Round = 10
        return
    call Wait
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













label Pool_Sunbathe(Girl=0, Type=0, Mod=0):




    menu:
        "With who?"
        "[RogueX.name]" if bg_current == RogueX.location:
            $ Girl = RogueX
        "[KittyX.name]" if bg_current == KittyX.location:
            $ Girl = KittyX
        "[EmmaX.name]" if bg_current == EmmaX.location:
            $ Girl = EmmaX
        "[LauraX.name]" if bg_current == LauraX.location:
            $ Girl = LauraX
        "[JeanX.name]" if bg_current == JeanX.location:
            $ Girl = JeanX
        "[StormX.name]" if bg_current == StormX.location:
            $ Girl = StormX
        "[JubesX.name]" if bg_current == JubesX.location:
            $ Girl = JubesX
        "Never mind.":
            return

    if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
        ch_p "Hey, [Girl.name], why don't you just relax over here?"
        ch_p "You don't want to get tanlines, why don't you. . ."
        ch_p ". . . take off a few layers?"
    else:
        ch_p "Are you sure you don't want to. . ."

    if time_index >= 2:
        $ Girl.change_face("_confused")
        Girl.voice "A bit late in the day for that. . ."
        $ Girl.change_face("_normal")
        return
    if not Girl.ClothingCheck():

        $ Girl.change_face("_sly")
        Girl.voice "Little late for that."
        return
    if "no_tan" in Girl.recent_history:
        $ Girl.change_face("_angry")
        Girl.voice "I just told you \"no.\""
        $ Girl.add_word(1,"_angry","_angry")
        return
    elif "no_tan" in Girl.daily_history:
        $ Girl.change_face("_angry")
        Girl.voice "Not today."
        $ Girl.add_word(1,"_angry","_angry")
        return

    if Girl == EmmaX:
        if "classcaught" not in EmmaX.history:
            $ Girl.change_face("_angry",2)
            ch_e "That would be entirely inappropriate."
            return
        if "taboo" not in EmmaX.history:
            $ Girl.change_face("_bemused",2)
            ch_e "[EmmaX.player_petname], we can't be seen like that in public. . ."
            return
        if "three" not in EmmaX.history:
            if not AloneCheck(EmmaX):
                $ Girl.change_face("_bemused",2)
                ch_e "Not with this sort of company. . ."
                return

    if not Girl.top and not Girl.bra and not Girl.legs and not Girl.underwear and (not Girl.accessory or Girl != JubesX):

        $ Girl.change_face("_sly")
        if Girl == RogueX:
            ch_r "I don't think that'll be a problem, [RogueX.player_petname]."
        elif Girl == KittyX:
            ch_k "Beat you to it."
        elif Girl == EmmaX:
            ch_e "I plan ahead."
        elif Girl == LauraX:
            ch_l "Yup."
        elif Girl == JeanX:
            ch_j "Seems that's taken care of. . ."
        elif Girl == StormX:
            ch_s "I cannot get much more naked. . ."
        elif Girl == JubesX:
            ch_v "I'm already pretty naked here. . ."
        $ Girl.add_word(1,"tan","tan")
        return

    $ Line = 0
    while True:

        if not Line:

            menu:
                extend ""
                "take it all off?" if (Girl.top or Girl.bra) and (Girl.legs or Girl.underwear or Girl.hose):
                    if Girl.top == "_towel" and not Girl.legs and not Girl.hose and not Girl.underwear:
                        $ Type = "no_panties"
                    elif (Girl.legs or Girl.hose) and not Girl.underwear:
                        $ Type = "no_panties"
                    elif Girl.top and not Girl.bra:
                        $ Type = "no_bra"
                    else:
                        $ Type = "both"
                    $ Mod = 200

                "lose the top?" if Girl.bra and not Girl.top:
                    $ Type = "_bra"

                "maybe just lose the jacket?" if Girl.accessory and Girl == JubesX:
                    if Girl.accessory == "shut_jacket" and not Girl.legs and not Girl.hose and not Girl.underwear:
                        $ Type = "no_panties"
                    elif Girl.accessory == "shut_jacket" and not Girl.top and not Girl.bra:
                        $ Type = "no_bra"
                    else:
                        $ Type = "_jacket"

                "maybe just lose the [Girl.top]?" if Girl.top:
                    if Girl.top == "_towel" and not Girl.legs and not Girl.hose and not Girl.underwear:
                        $ Type = "no_panties"
                    elif not Girl.bra:
                        $ Type = "no_bra"
                    else:
                        $ Type = "over"

                "maybe just lose the [Girl.legs]?" if Girl.legs:
                    if not Girl.underwear:
                        $ Type = "no_panties"
                    else:
                        $ Type = "legs"

                "maybe just lose the [Girl.hose]?" if Girl.hose and not Girl.legs:
                    if not Girl.underwear:
                        $ Type = "no_panties"
                    else:
                        $ Type = "legs"

                "maybe just lose the [Girl.underwear]?" if Girl.underwear:
                    $ Type = "_panties"
                    $ Mod = 200
                "never mind.":

                    return


        if Type == "no_panties":
            $ Mod = 200
            $ Girl.change_face("_bemused",1)
            Girl.voice "I don't have bottoms on under this. . ."
        elif Type == "no_bra":
            $ Girl.change_face("_bemused",1)
            Girl.voice "I don't have a top on under this. . ."

        if (Girl.SeenPussy and Girl.SeenChest) and AloneCheck():
            $ Mod -= 100


        if "exhibitionist" in Girl.traits:

            $ Line = "sure"
        elif approval_check(Girl, 700+Mod, "I"):

            $ Line = "sure"
        elif approval_check(Girl, 1400+Mod) or (Girl == StormX and StormX in Rules):

            $ Line = "sure"
        elif approval_check(Girl, 900):

            $ Line = "sorry"
        else:

            $ Line = "no"

        if Type == "no_bra" or Type == "no_panties":

            menu:
                extend ""
                "And?":
                    if Line == "sure":
                        if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                            $ Girl.change_stat("inhibition", 70, 1)

                        $ Girl.change_face("_sly",1)
                        if Girl == RogueX:
                            ch_r "Hmm, good point. . ."
                        elif Girl == KittyX:
                            ch_k "\"And\". . . I don't know. . ."
                        elif Girl == EmmaX:
                            ch_e "\"And\". . . you're lucky you're so cute. . ."
                        elif Girl == LauraX:
                            ch_l "I don't know. . ."
                        elif Girl == JeanX:
                            ch_j "Good point."
                        elif Girl == StormX:
                            ch_s "Just giving you fair warning. . ."
                        elif Girl == JubesX:
                            ch_v "Well. . . ok. . ."
                    else:
                        if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                            $ Girl.change_stat("love", 70, -1)
                            $ Girl.change_stat("obedience", 80, 1)

                        $ Girl.change_face("_angry",2)
                        if Girl == RogueX:
                            ch_r "\"And\" that's all you're getting. . . for now. . ."
                        elif Girl == KittyX:
                            ch_k "\"And\". . . AND!"
                        elif Girl == EmmaX:
                            ch_e "\"And\". . . you shouldn't push your luck. . ."
                        elif Girl == LauraX:
                            ch_l "\"And\" that's all you get."
                        elif Girl == JeanX:
                            $ Girl.change_face("_bemused",1)
                            ch_j "\"And\" I'd rather not."
                        elif Girl == StormX:
                            ch_s "\"And\" I would prefer to keep it on."
                        elif Girl == JubesX:
                            ch_v "Well, I'm keeping it on."
                "Take it off anyway.":
                    if Line == "sure" or (Line == "sorry" and Girl != StormX and approval_check(Girl, 600+Mod, "O")):
                        if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                            $ Girl.change_stat("obedience", 50, 1)
                            $ Girl.change_stat("obedience", 80, 2)
                        if Line != "sure":
                            $ Girl.change_face("_sad",2)
                        else:
                            $ Girl.change_face("_normal",1)
                        if Girl == RogueX:
                            ch_r "Oh, ok. . ."
                        elif Girl == KittyX:
                            ch_k "Yeah, ok. . ."
                        elif Girl == EmmaX:
                            ch_e "If you insist. . ."
                        elif Girl == LauraX:
                            ch_l "Affirmative."
                        elif Girl == JeanX:
                            ch_j ". . . ok."
                        elif Girl == StormX:
                            $ Girl.change_stat("love", 80, -2)
                            ch_s ". . . fine. . ."
                        elif Girl == JubesX:
                            ch_v "Whatever. . ."

                        $ Line = "sure"
                    else:
                        if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                            $ Girl.change_stat("love", 80, -2)
                            $ Girl.change_stat("obedience", 80, -1)
                            $ Girl.change_stat("inhibition", 60, 1)

                        $ Girl.change_face("_angry",1)
                        if Girl == RogueX:
                            ch_r "I don't like that tone on you. . ."
                        elif Girl == KittyX:
                            ch_k "How about \"no\". . ."
                        elif Girl == EmmaX:
                            ch_e "Not with that tone. . ."
                        elif Girl == LauraX:
                            ch_l "Don't push me."
                        elif Girl == JeanX:
                            $ Girl.change_face("_bemused",1)
                            ch_j "Ha! no."
                        elif Girl == StormX:
                            $ Girl.change_stat("love", 80, -2)
                            ch_s "You presume too much."
                        elif Girl == JubesX:
                            ch_v "Nope."

                        $ Girl.add_word(1,"no_tan","no_tan")
                        return
                "Hot.":
                    if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                        $ Girl.change_stat("love", 80, 1)
                        $ Girl.change_stat("obedience", 70, 2)
                        $ Girl.change_stat("inhibition", 60, 1)
                        $ Girl.change_stat("inhibition", 80, 1)

                    $ Girl.change_face("_sly",1)
                    if Girl == RogueX:
                        ch_r "Heh, you're a sweetie. . ."
                    elif Girl == KittyX:
                        ch_k "Hehe. . ."
                    elif Girl == EmmaX:
                        ch_e "How sweet. . ."
                    elif Girl == LauraX:
                        ch_l "True."
                    elif Girl == JeanX:
                        ch_j "You know it."
                    elif Girl == StormX:
                        ch_s ". . . I suppose so."
                    elif Girl == JubesX:
                        ch_v "Hehe. . ."
                "Ok, that's fine.":

                    if Line == "sure":
                        if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                            $ Girl.change_stat("love", 80, 2)
                            $ Girl.change_stat("obedience", 80, 1)
                            $ Girl.change_stat("inhibition", 60, 1)
                            $ Girl.change_stat("inhibition", 80, 1)

                        $ Girl.change_face("_sly",1)
                        if Girl == RogueX:
                            ch_r "Ready for a nice surprise? . ."
                        elif Girl == KittyX:
                            ch_k "Oh, you bet it is. . ."
                        elif Girl == EmmaX:
                            ch_e "More than you know. . ."
                        elif Girl == LauraX:
                            ch_l "But I can be generous. . ."
                        elif Girl == JeanX:
                            ch_j "But. . . I guess I can make an exception. . ."
                        elif Girl == StormX:
                            ch_s "But you are right about the value in an even tan. . ."
                        elif Girl == JubesX:
                            ch_v "You bet. . ."
                    else:
                        if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                            $ Girl.change_stat("love", 50, 1)
                            $ Girl.change_stat("love", 80, 1)
                            $ Girl.change_stat("inhibition", 60, 1)

                        $ Girl.change_face("_smile")
                        if Girl == RogueX:
                            ch_r "Thanks, [RogueX.player_petname]. . ."
                        elif Girl == KittyX:
                            ch_k "Thanks. . ."
                        elif Girl == EmmaX:
                            ch_e "Good. . ."
                        elif Girl == LauraX:
                            ch_l "Right."
                        elif Girl == JeanX:
                            ch_j "Good. . ."
                        elif Girl == StormX:
                            ch_s "I am sorry to disappoint."
                        elif Girl == JubesX:
                            ch_v "Thanks. . ."

            if Line == "sure":

                $ Girl.top = ""
                call expression Girl.tag + "_First_Topless"
                if Type == "no_panties":
                    $ Girl.legs = ""
                    $ Girl.hose = ""
                    call expression Girl.tag + "_First_Bottomless"
                $ Girl.add_word(1,"tan","tan")
            else:
                $ Girl.add_word(1,"no_tan","no_tan")

            $ Line = 0


        if Line == "sure":

            if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                $ Girl.change_stat("obedience", 70, 2)
                $ Girl.change_stat("obedience", 90, 1)
                $ Girl.change_stat("inhibition", 70, 2)
                $ Girl.change_stat("inhibition", 90, 1)
            $ Girl.change_face("_sly",1)
            if Girl == RogueX:
                ch_r "I suppose I could. . ."
            elif Girl == KittyX:
                ch_k "I guess. . ."
            elif Girl == EmmaX:
                ch_e "Hmmm. . ."
            elif Girl == LauraX:
                ch_l "Sure."
            elif Girl == JeanX:
                ch_j "Yeah, ok."
            elif Girl == StormX:
                ch_s "I suppose I could."
            elif Girl == JubesX:
                ch_v "Sure. . ."

            if Type == "_jacket" or Type == "both":
                if Girl == JubesX:
                    $ Girl.accessory = ""
            if Type == "over" or Type == "both":
                $ Girl.top = ""
            if Type == "_bra" or Type == "both":
                $ Girl.bra = ""
            call expression Girl.tag + "_First_Topless"

            if Type == "legs" or Type == "both":
                $ Girl.legs = ""
                $ Girl.hose = ""
            if Type == "_panties" or Type == "both":
                $ Girl.underwear = ""
            call expression Girl.tag + "_First_Bottomless"

            $ Girl.add_word(1,"tan","tan")

        elif Line == "sorry" and (Type == "over" or Type == "legs" or Type == "_jacket"):

            if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                $ Girl.change_stat("obedience", 50, 1)
                $ Girl.change_stat("obedience", 80, 1)
                $ Girl.change_stat("inhibition", 60, 1)
                $ Girl.change_stat("inhibition", 80, 1)
            $ Girl.change_face("_bemused",1)
            if Girl == RogueX:
                ch_r "I suppose I could. . ."
            elif Girl == KittyX:
                ch_k "I guess. . ."
            elif Girl == EmmaX:
                ch_e "Hmmm. . ."
            elif Girl == LauraX:
                ch_l "Sure."
            elif Girl == JeanX:
                ch_j "Sure, I guess."
            elif Girl == StormX:
                ch_s "I suppose I could."
            elif Girl == JubesX:
                ch_v "Sure. . ."

            if Type == "_jacket":
                $ Girl.accessory = ""
            if Type == "over":
                $ Girl.top = ""
            if Type == "legs":
                $ Girl.legs = ""
                $ Girl.hose = ""
            $ Girl.add_word(1,"tan","tan")

        elif Line == "sorry":

            if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("obedience", 80, 2)
                $ Girl.change_stat("inhibition", 60, 1)
                $ Girl.change_stat("inhibition", 90, 2)
            $ Girl.change_face("_sadside",1)
            if Girl == RogueX:
                ch_r "Sorry, I think I can live with the tan lines. . ."
            elif Girl == KittyX:
                ch_k "I just can't. . ."
            elif Girl == EmmaX:
                ch_e "That just wouldn't be appropriate. . ."
            elif Girl == LauraX:
                ch_l "Nah. . ."
            elif Girl == JeanX:
                ch_j "I. . . wouldn't be comfortable with that. . ."
            elif Girl == StormX:
                ch_s "I am sorry to disappoint you."
            elif Girl == JubesX:
                ch_v "Sorry. . ."
            $ Girl.add_word(1,"no_tan","no_tan")

        elif Line == "no":

            $ Girl.change_stat("love", 50, -5)
            $ Girl.change_stat("obedience", 50, 2)
            $ Girl.change_stat("inhibition", 60, 1)
            $ Girl.change_face("_angry",1)
            if Girl == RogueX:
                ch_r "Not interested, [RogueX.player_petname]. . ."
            elif Girl == KittyX:
                ch_k "Not even."
            elif Girl == EmmaX:
                ch_e "You must be dreaming. . ."
            elif Girl == LauraX:
                ch_l "Nope. . ."
            elif Girl == JeanX:
                ch_j "Ha!"
            elif Girl == StormX:
                ch_s "I am afraid not, [Girl.player_petname]."
            elif Girl == JubesX:
                ch_v "Sure. . ."

            $ Girl.add_word(1,"no_tan","no_tan")
            return
        if not Girl.bra and not Girl.top and not Girl.underwear and not Girl.legs and Girl.HoseNum() < 10:
            $ Girl.change_outfit("nude")
        $ Mod = 0
        $ Line = 0
        if Girl.ClothingCheck():
            "Anything else?"
        else:
            return
    return






label Pool_Skinnydip(Girl=0, Line=0, Type=0, Mod=0):




    menu:
        "With who?"
        "[RogueX.name]" if bg_current == RogueX.location:
            $ Girl = RogueX
        "[KittyX.name]" if bg_current == KittyX.location:
            $ Girl = KittyX
        "[EmmaX.name]" if bg_current == EmmaX.location:
            $ Girl = EmmaX
        "[LauraX.name]" if bg_current == LauraX.location:
            $ Girl = LauraX
        "[JeanX.name]" if bg_current == JeanX.location:
            $ Girl = JeanX
        "[StormX.name]" if bg_current == StormX.location:
            $ Girl = StormX
        "[JubesX.name]" if bg_current == JubesX.location:
            $ Girl = JubesX
        "Never mind.":
            return

    ch_p "Hey, [Girl.name], why don't we skinny dip?"

    if Round <= 10:
        $ Girl.change_face("_sad")
        Girl.voice "No time for that."
        return
    elif "no_dip" in Girl.recent_history:
        $ Girl.change_face("_angry")
        Girl.voice "I just told you \"no.\""
        $ Girl.add_word(1,"_angry","_angry")
        return
    elif "no_dip" in Girl.daily_history:
        $ Girl.change_face("_angry")
        Girl.voice "Not today."
        $ Girl.add_word(1,"_angry","_angry")
        return
    elif "dip" in Girl.recent_history:
        $ Girl.change_face("_confused")
        Girl.voice "We already did that."
        return

    if Girl == EmmaX:
        if "classcaught" not in EmmaX.history:
            $ Girl.change_face("_angry",2)
            ch_e "That would be entirely inappropriate."
            return
        if "taboo" not in EmmaX.history:
            $ Girl.change_face("_bemused",2)
            ch_e "[EmmaX.player_petname], I couldn't risk us getting caught. . ."
            return
        if "three" not in EmmaX.history:
            if not AloneCheck(EmmaX):
                $ Girl.change_face("_bemused",2)
                ch_e "Not with this sort of company. . ."
                return

    if not Girl.ClothingCheck():

        $ Girl.change_face("_sly")
        if Girl == RogueX:
            ch_r "Sure, let's get wet."
        elif Girl == KittyX:
            ch_k "Cannonball!"
        elif Girl == EmmaX:
            ch_e "Lovely."
        elif Girl == LauraX:
            ch_l "I'm in."
        elif Girl == JeanX:
            ch_j "Heh, sure."
        elif Girl == StormX:
            ch_s "I would love to."
        elif Girl == JubesX:
            ch_v "Sure!"

        $ Girl.add_word(1,"dip","dip")
    else:

        if Girl.SeenPussy and Girl.SeenChest:
            $ Mod += 100

        if "exhibitionist" in Girl.traits:

            $ Line = "sure"
        elif approval_check(Girl, 700-Mod, "I"):

            $ Line = "sure"
        elif approval_check(Girl, 1200-Mod) or (Girl == StormX and StormX in Rules):

            $ Line = "sure"
        elif approval_check(Girl, 800):

            $ Line = "sorry"
        else:

            $ Line = "no"

        if Line == "sure":

            if "dip" not in Girl.recent_history and "no_dip" not in Girl.recent_history:
                $ Girl.change_stat("obedience", 70, 2)
                $ Girl.change_stat("obedience", 90, 1)
                $ Girl.change_stat("inhibition", 70, 2)
                $ Girl.change_stat("inhibition", 90, 1)
            $ Girl.change_face("_sly",1)
            if Girl == RogueX:
                ch_r "Sounds fun. . ."
            elif Girl == KittyX:
                ch_k "Oooh, naughty. . ."
            elif Girl == EmmaX:
                ch_e "How daring. . ."
            elif Girl == LauraX:
                ch_l "Sure."
            elif Girl == JeanX:
                ch_j "Yeah, ok."
            elif Girl == StormX:
                ch_s "I would love to."
            elif Girl == JubesX:
                ch_v "Sure!"


            $ Girl.top = ""
            $ Girl.bra = ""
            call expression Girl.tag + "_First_Topless"

            $ Girl.legs = ""
            $ Girl.hose = ""
            $ Girl.underwear = ""
            call expression Girl.tag + "_First_Bottomless"
            $ Girl.change_outfit("nude")
            $ Girl.add_word(1,"dip","dip")

        elif Line == "sorry":

            if "dip" not in Girl.recent_history and "no_dip" not in Girl.recent_history:
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("obedience", 80, 2)
                $ Girl.change_stat("inhibition", 60, 1)
                $ Girl.change_stat("inhibition", 90, 2)
            $ Girl.change_face("_sadside",1)
            if Girl == RogueX:
                ch_r "Couldn't we just take a normal swim?"
            elif Girl == KittyX:
                ch_k "I don't think so. . ."
            elif Girl == EmmaX:
                ch_e "Perhaps in a tub. . ."
            elif Girl == LauraX:
                ch_l "Nah. . ."
            elif Girl == JeanX:
                ch_j "Um, no, not right now."
            elif Girl == StormX:
                ch_s "I am afraid not, [Girl.player_petname]."
            elif Girl == JubesX:
                ch_v "Yeah, not right now."
            menu:
                extend ""
                "Ok, we can just use swimsuits.":
                    if Girl.Swim[0]:

                        if "dip" not in Girl.recent_history and "no_dip" not in Girl.recent_history:
                            $ Girl.change_stat("love", 80, 2)
                            $ Girl.change_stat("obedience", 50, 1)
                            $ Girl.change_stat("inhibition", 60, 2)
                        $ Girl.change_face("_smile")
                        if Girl == RogueX:
                            ch_r "Thanks, [RogueX.player_petname]."
                        elif Girl == KittyX:
                            ch_k "Cool."
                        elif Girl == EmmaX:
                            ch_e "That would be nice."
                        elif Girl == LauraX:
                            ch_l "Whatever."
                        elif Girl == JeanX:
                            ch_j "Yeah, ok."
                        elif Girl == StormX:
                            ch_s "Yes, that would be fine."
                        elif Girl == JubesX:
                            ch_v "Sure!"

                        show blackscreen onlayer black
                        "She goes and changes into her suit. . ."
                        $ Girl.change_outfit("swimwear")
                        hide blackscreen onlayer black
                        $ Girl.add_word(1,"no_dip","no_dip")
                        $ Count = 1
                    else:
                        if not Girl.change_outfit("swimwear"):
                            $ Count = 0
                    if not Count:

                        menu:
                            extend ""
                            "Then what about your undies?":
                                if Girl.ChestNum() > 2 and Girl.PantiesNum() > 2 and approval_check(Girl, 1000):

                                    pass
                                elif Girl.ChestNum() > 1 and Girl.PantiesNum() > 1 and approval_check(Girl, 1200):

                                    pass
                                else:
                                    $ Girl.change_face("_sly",1)
                                    Girl.voice "That's not going to work either."
                                    $ Girl.add_word(1,"no_dip","no_dip")
                                    return
                                $ Girl.change_face("_smile",1)
                                if Girl == RogueX:
                                    ch_r "Ok, fine. . ."
                                elif Girl == KittyX:
                                    ch_k "Fine, geez."
                                elif Girl == EmmaX:
                                    ch_e "I suppose. . ."
                                elif Girl == LauraX:
                                    ch_l "Sure, whatever. . ."
                                elif Girl == JeanX:
                                    ch_j ". . . I guess."
                                elif Girl == StormX:
                                    ch_s "Oh, I suppose so. . ."
                                elif Girl == JubesX:
                                    ch_v "I guess so. . ."
                            "Ok then, never mind.":
                                Girl.voice "Thanks."
                                $ Girl.add_word(1,"no_dip","no_dip")
                                return
                        $ Girl.top = ""
                        "She starts to strip down."
                        $ Girl.legs = ""
                        $ Girl.hose = ""
                        "And ends up in her underwear."
                        $ Girl.SeenPanties = 1
                "Never mind then.":


                    $ Girl.change_stat("love", 80, -1)
                    if "dip" not in Girl.recent_history and "no_dip" not in Girl.recent_history:
                        $ Girl.change_stat("obedience", 50, 2)
                        $ Girl.change_stat("inhibition", 60, 1)
                    if Girl == RogueX:
                        ch_r "Hmph."
                    elif Girl == KittyX:
                        ch_k "Bummer."
                    elif Girl == EmmaX:
                        ch_e "Disappointing."
                    elif Girl == LauraX:
                        ch_l "K."
                    elif Girl == StormX:
                        ch_s "Thank you, [Girl.player_petname]."
                    elif Girl == JubesX:
                        ch_v "Ok."
                    $ Girl.add_word(1,"no_dip","no_dip")
                    return

        elif Line == "no":

            $ Girl.change_stat("love", 50, -5)
            if "dip" not in Girl.recent_history and "no_dip" not in Girl.recent_history:
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("inhibition", 60, 1)
            $ Girl.change_face("_angry",1)
            if Girl == RogueX:
                ch_r "Not interested, [RogueX.player_petname]. . ."
            elif Girl == KittyX:
                ch_k "Not even."
            elif Girl == EmmaX:
                ch_e "You must be dreaming. . ."
            elif Girl == LauraX:
                ch_l "Nope. . ."
            elif Girl == JeanX:
                $ Girl.change_face("_bemused",1)
                ch_j "Ha!"
            elif Girl == StormX:
                ch_s "I am afraid not, [Girl.player_petname]."
            elif Girl == JubesX:
                ch_v "Sorry. . ."

            $ Girl.add_word(1,"no_dip","no_dip")
            return

    call ShowPool ([Girl])
    $ Girl.Water = 1
    $ Round -= 20 if Round >= 20 else Round
    "You both swim around for a bit."
    hide FullPool
    call set_the_scene (1, 0, 0)

    return





label Pool_Topless(Girl=focused_Girl, BO=[]):

    if Girl.location != bg_current:

        $ BO = all_Girls[:]
        $ renpy.random.shuffle(BO)
        while BO:
            if BO[0].location == bg_current:
                call shift_focus (BO[0])
                $ BO = [1]
            $ BO.remove(BO[0])

    $ focused_Girl = Girl
    if (Girl.ChestNum() <= 1 and Girl.OverNum() <= 1) or Girl.location != bg_current:

        $ D20 = renpy.random.randint(1, 14)
        return
    $ Girl.top_pulled_up = 1
    "[Girl.name] dives into the pool"
    menu:
        "It appears she's had a wardrobe malfunction."
        "Hey, [Girl.name]. . .":
            ch_p "Looks like you might be missing something there. . ."
            $ Girl.change_face("_confused")
            if Girl != StormX:
                $ Girl.change_stat("obedience", 60, 2)
                $ Girl.change_stat("inhibition", 50, -2)
                Girl.voice ". . ."
                $ Girl.change_face("_surprised",2,Eyes="_down")
            $ Girl.change_stat("love", 80, 3)
            $ Girl.change_stat("love", 90, 1)
            $ Girl.change_stat("lust", 50, 2)
            $ Count = 100
        "Say nothing":
            $ Girl.change_face("_surprised",2,Eyes="_down")
            "After a few moments, [Girl.name] seems to notice that her top rode up."
            if approval_check(Girl, 1200):
                $ Count = 0
            else:
                $ Count = -100

    if approval_check(Girl, 800-Count,"I") or approval_check(Girl, 1600-Count) or (Girl == StormX and StormX in Rules):
        $ Girl.change_face("_sly")
        $ Girl.bra = ""
        $ Girl.top = ""
        $ Girl.change_stat("obedience", 60, 2)
        $ Girl.change_stat("inhibition", 50, 4)
        $ Girl.change_stat("inhibition", 90, 2)
        $ Girl.change_stat("lust", 50, 5)
        "She smiles and tosses her top over her head."
        call expression Girl.tag + "_First_Topless"
    elif approval_check(Girl, 500-Count,"I") or approval_check(Girl, 1200-Count):
        $ Girl.change_face("_sly",1)
        $ Girl.change_stat("obedience", 60, 2)
        $ Girl.change_stat("inhibition", 50, 3)
        $ Girl.change_stat("inhibition", 80, 2)
        $ Girl.change_stat("lust", 50, 3)
        "She smiles, and leaves the top how it is."
        call expression Girl.tag + "_First_Topless"
    else:
        if approval_check(Girl, 800-Count) or (Girl == StormX):

            $ Girl.change_stat("obedience", 60, 2)
            $ Girl.change_stat("inhibition", 70, 2)
            $ Girl.change_stat("lust", 50, 1)
            $ Girl.change_face("_bemused",2)
        else:

            $ Girl.change_stat("love", 70, -2)
            $ Girl.change_stat("inhibition", 50, 1)
            $ Girl.change_face("_angry",2)
        call expression Girl.tag + "_First_Topless" pass (1)
        $ Girl.top_pulled_up = 0
        "She tugs her top back into place."
        if Count <= 0:
            $ Girl.change_stat("love", 70, -5)
            $ Girl.change_stat("obedience", 60, -2)
            $ Girl.change_stat("inhibition", 60, 2)
            Girl.voice "You could have told me."

    $ Count = 0
    return





label Breakup(Girl=0, Other=0, Anger=0, BO=[]):



    $ Girl.add_word(1,"breakup talk","breakup talk",0,0)

    if Girl.Break[1] > 3:
        $ Girl.change_face("_angry")
        $ Girl.change_stat("love", 50, -5, 1)
        $ Girl.change_stat("love", 80, -10, 1)
        $ Girl.change_stat("obedience", 30, -5, 1)
        $ Girl.change_stat("obedience", 50, -10, 1)
        $ Girl.change_stat("inhibition", 50, 3)
        $ Girl.change_stat("inhibition", 80, 1)
        Girl.voice "This is getting old."
        $ Anger -= 1
    elif Girl.Break[1]:
        $ Girl.change_face("_surprised")
        $ Girl.change_stat("love", 50, -5, 1)
        $ Girl.change_stat("obedience", 30, -5, 1)
        $ Girl.change_stat("inhibition", 80, 1)
        Girl.voice "What, again?"
        $ Girl.change_face("_angry")
        $ Anger += 1
    else:
        $ Girl.change_face("_surprised")
        Girl.voice "What?! Why?"

    $ Line = 0
    menu:
        "It's not you, it's me.":
            $ Girl.change_stat("love", 200, -5)
            $ Girl.change_stat("obedience", 80, -5)
            $ Girl.change_stat("inhibition", 50, 3)
            $ Girl.change_stat("inhibition", 70, 1)
            $ Girl.change_face("_confused")
        "I just think we need a break.":

            $ Girl.change_stat("love", 200, -5)
            $ Girl.change_face("_sad")
        "I've found someone else.":

            $ Anger += 1
            $ Girl.change_stat("love", 200, -10)
            $ Girl.change_stat("obedience", 50, 3)
            $ Girl.change_stat("obedience", 80, 3)
            $ Girl.change_stat("inhibition", 50, -5)
            $ Girl.change_face("_angry")
            Girl.voice "Who is it?"
            menu:
                extend ""
                "[RogueX.name]" if Girl != RogueX:
                    $ Other = RogueX
                "[KittyX.name]" if Girl != KittyX and "met" in KittyX.history:
                    $ Other = KittyX
                "[EmmaX.name]" if Girl != EmmaX and "met" in EmmaX.history:
                    $ Other = EmmaX
                "[LauraX.name]" if Girl != LauraX and "met" in LauraX.history:
                    $ Other = LauraX
                "[JeanX.name]" if Girl != JeanX and "met" in JeanX.history:
                    $ Other = JeanX
                "[StormX.name]" if Girl != StormX and "met" in StormX.history:
                    $ Other = StormX
                "[JubesX.name]" if Girl != JubesX and "met" in JubesX.history:
                    $ Other = JubesX
                "I won't say.":
                    $ Girl.change_stat("love", 200, -5)
                    $ BO = active_Girls[:]
                    $ BO.remove(Girl)
                    $ Count = 0
                    while BO:
                        if BO[0].SEXP > Count:

                            $ Other = BO[0]
                            $ Count = BO[0].SEXP
                        $ BO.remove(BO[0])
                    $ Count = 0
                    if not Other:
                        Girl.voice "Well it's got to be someone. . ."
                    else:
                        Girl.voice "It's [Other.name], isn't it."
                "I was kidding.":
                    $ Girl.change_stat("love", 200, -5)
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_face("_angry")
                    if Girl == RogueX:
                        ch_r "That was a pretty rude way to deflect there."
                    elif Girl == KittyX:
                        ch_k "I'll[KittyX.like]kid you!"
                    elif Girl == EmmaX:
                        ch_e "Oh, you do *not* want to \"kid\" me about that."
                    elif Girl == LauraX:
                        ch_l ". . ."
                    elif Girl == JeanX:
                        ch_j "The last time I heard a joke like that, someone lost a 7th birthday."
                    elif Girl == StormX:
                        ch_s "You should not \"kid\" about such things, [Girl.player_petname]."
                    elif Girl == JubesX:
                        ch_v "Right. . ."
                    $ Girl.change_face("_normal")
                    $ Anger += 1
        "I'm just done with you.":

            $ Girl.change_face("_angry")
            $ Girl.change_stat("love", 50, 3)
            $ Girl.change_stat("love", 200, -15)
            $ Girl.change_stat("obedience", 50, 5)
            $ Girl.change_stat("obedience", 80, 5)
            $ Girl.change_stat("obedience", 200,5)
            $ Girl.change_stat("inhibition", 50, -5)
            $ Anger += 1


    if not Other:

        $ Girl.change_face("_sad")
        if approval_check(Girl, 900, "O"):

            Girl.voice "If that's really what you want. . ."
        elif approval_check(Girl, 900, "L"):

            Girl.voice "But I love you so much!"
        elif approval_check(Girl, 900, "I") or Girl == JeanX:

            Girl.voice "If that's how you feel. . ."
        elif approval_check(Girl, 1500):

            Girl.voice "But we mean so much to each other!"
        else:

            Girl.voice "Are you sure this is what you want?"
        $ Line = "bargaining"
    else:



        $ counter = int((Girl.GirlLikeCheck(Other) - 500)/2)

        if Girl.GirlLikeCheck(Other) >= 800:
            $ Girl.change_stat("lust", 70, 5)
            $ Girl.change_stat("obedience", 50, 5)
            $ Girl.change_stat("obedience", 200, 5)
            $ Girl.change_stat("inhibition", 50, 1)
            $ Girl.change_stat("inhibition", 200, 5)
            $ Girl.change_face(5,2)
            Girl.voice "Well, you have good tastes, at least."
            $ Girl.change_face(5,1)
        elif Girl.GirlLikeCheck(Other) >= 600:
            $ Girl.change_stat("love", 50, -5, 1)
            $ Girl.change_stat("love", 80, -10, 1)
            $ Girl.change_stat("obedience", 50, 5)
            $ Girl.change_stat("obedience", 200, 3)
            if Other == EmmaX and Girl != StormX:
                Girl.voice "With our teacher?!"
            if Other == StormX and Girl != EmmaX:
                Girl.voice "With our teacher?!"
            elif Girl == EmmaX and Other != StormX:
                ch_e "And I always did like her in class. . ."
            elif Girl == StormX and Other == EmmaX:
                ch_s "And she seemed so respectable. . ."
            elif Girl in (EmmaX,StormX) and Other in (EmmaX,StormX):
                Girl.voice "You have a thing for teachers?"
            elif Girl == LauraX:
                ch_l "I do kinda like her."
            elif Girl == JeanX:
                ch_j "Well, she's not a complete bitch."
            else:
                Girl.voice "With one of my friends?!"
            $ Girl.change_face("_normal")
            $ Anger += 1
        elif Girl.GirlLikeCheck(Other) >= 400:
            $ Girl.change_stat("love", 50, -3, 1)
            $ Girl.change_stat("love", 80, -5, 1)
            $ Girl.change_stat("obedience", 80, 5)
            $ Girl.change_stat("inhibition", 50, 1)
            $ Girl.change_stat("inhibition", 80, 3)
            Girl.voice "You know you can do better."
        else:
            $ Girl.change_stat("love", 50, -5, 1)
            $ Girl.change_stat("obedience", 80, 3)
            $ Girl.change_stat("inhibition", 50, 2)
            $ Girl.change_stat("inhibition", 80, 5)
            $ Girl.change_face("_angry")
            Girl.voice "With that skank?!"
            $ Anger += 2

        if approval_check(Girl, 2000, Bonus = counter):
            $ Girl.change_stat("lust", 70, 5)
            $ Girl.change_face("_sexy")
            Girl.voice "Why not both of us?"
            $ Line = "threeway"
        else:
            $ Girl.change_face("_sad")
            Girl.voice "You would rather be with her than with me?"
            menu:
                extend ""
                "Yes, I would.":
                    $ Girl.change_stat("love", 50, -3, 1)
                    $ Girl.change_stat("love", 80, -5, 1)
                    $ Girl.change_stat("obedience", 30, 1)
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Anger += 1
                    $ Line = "bargaining"
                    if Girl == RogueX:
                        ch_r "Well then I don't think I can help you."
                    elif Girl == KittyX:
                        ch_k "!!!"
                    elif Girl == EmmaX:
                        ch_e "I suppose you've made your choice then."
                    elif Girl == LauraX:
                        ch_l "Your loss."
                    elif Girl == JeanX:
                        ch_j "Nonsense."
                    elif Girl == StormX:
                        ch_s "Then I understand."
                        $ Line = "threeway"
                    elif Girl == JubesX:
                        ch_v "Rough. . ."
                "I'd rather be with both of you.":

                    $ Line = "threeway"
                "No, I'm sorry, never mind that.":

                    $ Girl.change_stat("love", 50, -3, 1)
                    $ Girl.change_stat("obedience", 80, -5)
                    Girl.voice "Not doing yourself any favors there. . ."
                    $ Line = "bargaining"


    if Line == "threeway" and Anger < 4:
        if Girl == StormX:
            ch_s "So would she be fine with you dating us both?"
        else:
            Girl.voice "Date us both at once? What does she think about that?"
        menu Breakup_Threeway_Offer:
            extend ""
            "She said it would be ok with her." if "poly "+ Girl.tag in Other.traits or Girl.tag+"Yes" in Player.traits:

                if approval_check(Girl, 1800, Bonus = counter):
                    $ Girl.change_face("_smile", 1)
                    $ Girl.change_stat("lust", 70, 5)
                    $ Girl.change_stat("obedience", 50, 5)
                    $ Girl.change_stat("obedience", 80, 3)
                    $ Girl.change_stat("inhibition", 50, 3)
                    $ Girl.change_stat("inhibition", 80, 1)
                    if Girl.GirlLikeCheck(Other) < 400:
                        $ Girl.change_face("_angry")
                        if Girl == RogueX:
                            ch_r "I can't stand that bitch, but for you I'll put up with her."
                        elif Girl == KittyX:
                            ch_k "That bitch! Fine, I'll put up with her."
                        elif Girl == EmmaX:
                            ch_e "I suppose I can be the better woman here. . ."
                            ch_e "Not that it's hard to accomplish."
                        elif Girl == LauraX:
                            ch_l "I can keep my claws in. . . for you."
                        elif Girl == JeanX:
                            ch_j "Well. . I guess I can find -some- use for her."
                        elif Girl == StormX:
                            ch_s "I dislike her, but I will put up with her."
                        elif Girl == JubesX:
                            ch_v "Well, this is not cool. . . but I can deal. . ."
                    elif Girl == StormX:
                        ch_s "Then that is all I need to know."
                    elif Girl.GirlLikeCheck(Other) >= 700 or Girl == JeanX:
                        $ Girl.change_face("_sexy")
                        Girl.voice "I have to say I've kind of been thinking about it myself."
                    elif Girl.love >= Girl.obedience:
                        $ Girl.change_face("_sad")
                        Girl.voice "Just so long as we can be together, I can share."
                    else:

                        Girl.voice "If she's in, I am."

                    $ Girl.add_word(1,0,0,"poly "+Other.tag,0)
                else:
                    $ Anger += 2
                    $ Girl.change_stat("love", 50, -10, 1)
                    $ Girl.change_stat("love", 80, -15, 1)
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_stat("obedience", 80, 3)
                    $ Girl.change_stat("inhibition", 50, 5)
                    $ Girl.change_stat("inhibition", 80, 3)
                    $ Girl.change_face("_angry", 1)
                    Girl.voice "Well maybe she did, but I don't want to share."
                    $ Line = "bargaining"
                    if Girl == StormX:
                        $ Line = "breakup"
            "I have no idea.":


                $ Line = "ask " + Other.tag
            "She's not into it.":

                if Girl.GirlLikeCheck(Other) >= 700:
                    $ Girl.change_stat("love", 200, -5)
                elif Girl.GirlLikeCheck(Other) <= 400:
                    $ Girl.change_stat("love", 90, 5)
                Girl.voice "Well then why even bring it up?"
            "Well, even if she doesn't agree. . .":


                $ Line = "ask " + Other.tag
                if Girl.GirlLikeCheck(Other) >= 700:
                    $ Girl.change_face("_angry")
                    $ Girl.change_stat("love", 200, -5)
                elif Girl.GirlLikeCheck(Other) <= 400:
                    $ Girl.change_stat("love", 90, 5)

        if Line == "ask " + Other.tag and Girl.GirlLikeCheck(Other) >= 700:

            Girl.voice "You want me to ask her for you?"
            menu:
                extend ""
                "Yes, that'd be a good idea.":
                    $ Girl.change_stat("love", 90, 5)
                    $ Girl.change_stat("obedience", 70, 1)
                    $ Girl.change_stat("inhibition", 80, 5)
                    $ Girl.change_face("_sexy")
                    Girl.voice "I guess I could."
                    $ Girl.add_word(1,0,0,"ask "+Other.tag,0)
                    $ Girl.add_word(1,0,0,"poly "+Other.tag,0)
                "No, let's just keep it under cover.":
                    $ Girl.change_stat("love", 50, -5, 1)
                    $ Girl.change_stat("love", 80, -5, 1)
                    $ Girl.change_stat("obedience", 80, 5)
                    $ Girl.change_stat("inhibition", 50, 3)
                    Girl.voice "I don't know. . ."

        if Line == "breakup":
            pass
        elif Line != "bargaining" and "poly "+ Other.tag not in Girl.traits:


            if "ask "+ Other.tag not in Girl.traits and not approval_check(Girl, 1800, Bonus = -(int((Girl.GirlLikeCheck(Other) - 600)/2))):


                $ Girl.change_stat("love", 50, -5, 1)
                $ Girl.change_stat("obedience", 80, -10, 1)
                $ Girl.change_stat("inhibition", 50, 5)
                $ Girl.change_face("_angry", 1)
                if not approval_check(Girl, 1800):
                    Girl.voice "Maybe I don't like you that much either."
                else:
                    $ Girl.change_stat("love", 80, -10, 1)
                    $ Girl.change_stat("obedience", 50, -5, 1)
                    if Girl == EmmaX and Other != StormX:
                        ch_e "I'd rather not be dallying with another teacher's boyfriend. . ."
                    elif Girl == EmmaX:
                        ch_e "I'd rather not be dallying with a student's boyfriend. . ."
                    elif Girl == StormX:
                        ch_s "I would rather not creep around like that."
                    elif Girl == JeanX:
                        ch_j "I don't know, shes a little boring. . ."
                    elif Other == EmmaX:
                        Girl.voice "I don't want to get caught with the teacher's boyfriend!"
                    else:
                        Girl.voice "I'm not really cool with that, [Other.name]'s a friend of mine."
                $ Anger += 1
                if Girl != StormX:
                    $ Line = "bargaining"
            else:

                $ Girl.change_stat("obedience", 30, 5)
                $ Girl.change_stat("obedience", 50, 3)
                $ Girl.change_stat("inhibition", 50, 5)
                $ Girl.change_stat("inhibition", 80, 1)
                $ Girl.change_face("_sad")
                if Girl.GirlLikeCheck(Other) < 400:
                    $ Girl.change_face("_angry")
                    if Girl == RogueX:
                        ch_r "I can't stand that bitch, but for you I'll put up with her."
                    elif Girl == KittyX:
                        ch_k "That bitch! Fine, I'll put up with her."
                    elif Girl == EmmaX:
                        ch_e "I suppose I can be the better woman here. . ."
                        ch_e "Not that it's hard to accomplish."
                    elif Girl == LauraX:
                        ch_l "I can keep my claws in. . . for you."
                    elif Girl == JeanX:
                        ch_j "Well. . I guess I can find -some- use for her."
                    elif Girl == StormX:
                        ch_s "I dislike her, but I will put up with her."
                    elif Girl == JubesX:
                        ch_v "Well, this is not cool. . . but I can deal. . ."
                elif Girl.GirlLikeCheck(Other) >= 700:
                    $ Girl.change_face("_sexy")
                    Girl.voice "I have to say I've kind of been thinking about it myself."
                elif Girl.love >= Girl.obedience:

                    $ Girl.change_face("_sad")
                    Girl.voice "Just so long as we can be together, I can share."
                else:

                    Girl.voice "If she's in, I am."
                $ Girl.add_word(1,0,0,"poly "+Other.tag,0)
                if "ask "+ Other.tag in Girl.traits:

                    Girl.voice "I'll talk to [Other.name] about it."
                else:
                    $ Girl.change_face("_sad")
                    $ Girl.add_word(1,0,0,"downlow",0)
                    if Girl == RogueX:
                        ch_r "I guess we can keep this on the downlow, for now at least."
                    elif Girl == KittyX:
                        ch_k "Oooh, our little secret. . ."
                    elif Girl == EmmaX:
                        ch_e "I suppose I can be discreet."
                    elif Girl == LauraX:
                        ch_l "I can keep a secret."
                    elif Girl == JeanX:
                        ch_j "Sure, that works."
                    elif Girl == StormX:
                        ch_s "I can keep my secrets."
                    elif Girl == JubesX:
                        ch_v "I can keep to myself. . ."

                    if Girl.GirlLikeCheck(Other) >= 800 and Girl != JeanX:
                        Girl.voice "Please talk to [Other.name] about sharing you openly though."
                    elif Girl.GirlLikeCheck(Other) >= 500 and Girl != JeanX:
                        Girl.voice "I really don't like going behind [Other.name]'s back though."
                    else:
                        Girl.voice "Might be fun, sneaking around behind her back."


    if Line == "bargaining" and Anger < 4:
        $ Girl.change_face("_sad")
        Girl.voice "You're sure there's no way I could convince you to stay?"
        menu Breakup_Bargaining:
            extend ""
            "Sorry, I've changed my mind.":
                $ Girl.change_stat("obedience", 80, 5)
                if approval_check(Girl, 1500):
                    $ Line = "makeup"
                    $ Girl.change_stat("love", 80, 5)
                    if Girl == RogueX:
                        ch_r "That's wonderful!"
                    elif Girl == KittyX:
                        ch_k "Ok!"
                    elif Girl == EmmaX:
                        ch_e "I can accept that as an apology. . ."
                    elif Girl == LauraX:
                        ch_l "Huh? Ok. . ."
                    elif Girl == JeanX:
                        ch_j "Finally, you've come to your senses."
                    elif Girl == StormX:
                        ch_s "Then you can stay."
                    elif Girl == JubesX:
                        ch_v "Cool. . ."
                else:
                    $ Line = "breakup"
                    $ Girl.change_stat("love", 90, -5)
                    $ Girl.change_stat("obedience", 80, -5)
                    $ Girl.change_stat("inhibition", 80, 10)
                    if Girl == RogueX:
                        ch_r "You know what? Save it. We're done."
                    elif Girl == KittyX:
                        ch_k "Too little, too late. . ."
                    elif Girl == EmmaX:
                        ch_e "I'm afraid it's too late for apologies."
                    elif Girl == LauraX:
                        ch_l "Uh-huh. Too late for that."
                    elif Girl == JeanX:
                        ch_j "You know what? Too late."
                    elif Girl == StormX:
                        ch_s "I am not interested in your games."
                    elif Girl == JubesX:
                        ch_v "Too late. . ."
            "My mind's made up.":
                $ Girl.change_stat("obedience", 80, 5)
                $ Line = "breakup"
            "Well, you could do something for me. . .[[sex menu]":
                $ Girl.add_word(1,"bargainsex",0,0,0)
                $ Girl.change_stat("obedience", 80, 3)
                $ approval_bonus = 50
                $ multi_action = 0
                call expression Girl.tag + "_SMenu"
                $ multi_action = 1
                menu:
                    "Ok, I guess we can give it another shot.":
                        $ Girl.change_stat("love", 80, 3)
                        $ Girl.change_stat("obedience", 80, 5)
                        $ Line = "makeup"
                        $ Girl.change_face("_smile")
                    "That was nice, but we're still over.":

                        $ Girl.change_face("_angry")
                        $ Girl.change_stat("love", 50, -5, 1)
                        $ Girl.change_stat("love", 80, -10, 1)
                        $ Girl.change_stat("obedience", 50, 15)
                        $ Girl.change_stat("obedience", 80, 10)
                        $ Line = "breakup"
                        $ Anger += 4

            "Maybe if we brought someone else into this relationship?" if not Other and "bargainthreeway" not in Girl.recent_history:

                $ Girl.add_word(1,"bargainthreeway",0,0,0)
                Girl.voice "Who?"
                menu:
                    extend ""
                    "[RogueX.name]?" if Girl != RogueX:
                        $ Other = RogueX
                    "[KittyX.name]?" if Girl != KittyX and "met" in KittyX.history:
                        $ Other = KittyX
                    "[EmmaX.name]?" if Girl != EmmaX and "met" in EmmaX.history:
                        $ Other = EmmaX
                    "[LauraX.name]?" if Girl != LauraX and "met" in LauraX.history:
                        $ Other = LauraX
                    "[JeanX.name]?" if Girl != JeanX and "met" in JeanX.history:
                        $ Other = JeanX
                    "[StormX.name]?" if Girl != StormX and "met" in StormX.history:
                        $ Other = StormX
                    "[JubesX.name]?" if Girl != JubesX and "met" in JubesX.history:
                        $ Other = JubesX
                    "Up to you?":

                        $ Girl.change_face("_confused")

                        $ BO = active_Girls[:]
                        $ BO.remove(Girl)
                        $ Count = 0
                        while BO:
                            if Girl.GirlLikeCheck(BO[0]) > Count:

                                $ Other = BO[0]
                                $ Count = Girl.GirlLikeCheck(BO[0])
                            $ BO.remove(BO[0])
                        $ Count = 0
                        Girl.voice "[Other.name]?"
                    "Never mind, silly question.":

                        $ Girl.change_stat("love", 200, -10)
                        $ Girl.change_stat("obedience", 50, -10, 1)
                        $ Anger += 1
                        $ Girl.change_face("_angry")
                        jump Breakup_Bargaining

                if Other:
                    $ Girl.change_face("_confused")
                    jump Breakup_Threeway_Offer

        if Anger < 3 and Line != "breakup" and Line != "makeup":

            if Girl == StormX:
                $ Line = "breakup"
            else:
                jump Breakup_Bargaining




    if Line == "breakup" or Anger >= 4:
        if Anger >= 4:

            $ Girl.change_face("_angry")
            $ Girl.change_stat("love", 60, -10, 1)
            $ Girl.change_stat("obedience", 50, -5)
            $ Girl.change_stat("inhibition", 70, 5)
            if Girl == RogueX:
                ch_r "Well fuck you then!"
            elif Girl == KittyX:
                ch_k "Jerk!!"
            elif Girl == EmmaX:
                ch_e "Scum."
            elif Girl == LauraX:
                ch_l "You're gonna want to back up a few steps."
            elif Girl == JeanX:
                ch_j "Ok, that's it, I'm pulling the plug on this one!"
            elif Girl == StormX:
                ch_s "I am afraid that you have overstayed your welcome."
            elif Girl == JubesX:
                ch_v "Fuck off then!"
        else:

            $ Girl.change_stat("inhibition", 70, 5)
            $ Girl.change_face("_sad")

            if Girl.love >= Girl.obedience:

                if Girl == RogueX:
                    ch_r "I'll really miss you."
                elif Girl == KittyX:
                    ch_k "I was[KittyX.like]totally all-in on this!"
                elif Girl == EmmaX:
                    ch_e "I'll be devastated."
                    ch_e "For at least five minutes."
                elif Girl == LauraX:
                    ch_l ". . ."
                elif Girl == JeanX:
                    ch_j "You know what. . . forget it."
                elif Girl == StormX:
                    ch_s "I will miss you."
                elif Girl == JubesX:
                    ch_v "I'll miss you. . ."
                $ Girl.add_word(1,0,0,"ex",0)
            elif Girl.obedience >= Girl.inhibition:

                $ Girl.change_stat("obedience", 200, -10)
                if Girl == RogueX:
                    ch_r "You're abandoning me."
                elif Girl == KittyX:
                    ch_k "I'm[KittyX.like]not sure what to do next."
                elif Girl == EmmaX:
                    ch_e "I suppose I'll have to make do."
                elif Girl == LauraX:
                    ch_l "I'll need some new options."
                elif Girl == JeanX:
                    ch_j "Ok, never mind then."
                elif Girl == StormX:
                    ch_s "I am sorry it has come to this."
                elif Girl == JubesX:
                    ch_v "I needed this. . ."
                $ Girl.add_word(1,0,0,"ex",0)
            else:

                if Girl == RogueX:
                    ch_r "Now who'll I fuck?"
                elif Girl == KittyX:
                    ch_k "I guess I'll[KittyX.like]have to find someone else to bang?"
                elif Girl == EmmaX:
                    ch_e "I suppose I'll have other options."
                elif Girl == LauraX:
                    ch_l "Ok, later."
                elif Girl == JeanX:
                    ch_j "Ok, that's cool."
                elif Girl == StormX:
                    ch_s "Well, I will find a way to move on."
                elif Girl == JubesX:
                    ch_v "This was fun. . ."


        if Girl in Player.Harem:
            $ Player.Harem.remove(Girl)

        $ Girl.Break[0] = 5 + Girl.Break[1] + Girl.Cheated
        $ Girl.Break[1] += 1
    else:



        $ Girl.change_face("_smile")
        Girl.voice "I'm glad we could work things out. . ."
        if Girl.love >= Girl.obedience:

            $ Girl.change_stat("love", 200, 3)
            if Girl == RogueX:
                ch_r "I'd really miss you."
            elif Girl == KittyX:
                ch_k "I'd[KittyX.like]totes miss you!"
            elif Girl == EmmaX:
                ch_e "I'm in too deep, [EmmaX.player_petname]."
            elif Girl == LauraX:
                ch_l "I. . . care about you."
            elif Girl == JeanX:
                ch_j "You've really grown on me."
                $ Girl.change_face("_sly")
                ch_j "Like a one of those teacup pigs. . ."
            elif Girl == StormX:
                ch_s "I would miss you very much."
            elif Girl == JubesX:
                ch_v "I woulda missed you. . ."
        elif Girl.obedience >= Girl.inhibition:

            if Girl == RogueX:
                ch_r "I need you with me."
            elif Girl == KittyX:
                ch_k "I'm[KittyX.like]totally all-in on this."
            elif Girl == EmmaX:
                ch_e "I don't think I could do without you."
            elif Girl == LauraX:
                ch_l "I need you too much."
            elif Girl == JeanX:
                ch_j "I was really starting to enjoy this. . ."
            elif Girl == StormX:
                ch_s "I would miss you very much."
            elif Girl == JubesX:
                ch_v "I need this. . ."
        else:

            if Girl == RogueX:
                ch_r "We have fun together. Let's keep it at that."
            elif Girl == KittyX:
                ch_k "You[KittyX.like]really dodged a bullet on that one."
            elif Girl == EmmaX:
                ch_e "It's too much trouble finding another toy."
            elif Girl == LauraX:
                ch_l "Ok, fine."
            elif Girl == JeanX:
                ch_j "Yeah. . . ok."
            elif Girl == StormX:
                ch_s "I suppose so."
            elif Girl == JubesX:
                ch_v "This is fun, right?"
    $ Line = 0
    return






label Cheated(Girl=0, Other=0, Resolution=0, B=0):


    $ Girl.add_word(1,0,"relationship",0,0)
    call shift_focus (Girl)

    $ Girl.change_face("_angry")
    if Girl.location != bg_current and Girl not in Party:
        "Suddenly, [Girl.name] shows up and says she needs to talk to you."
    $ Girl.location = bg_current

    $ Girl.drain_word("asked meet",0,1)
    if "meet girl" in Player.daily_history:
        $ Player.daily_history.remove("meet girl")

    call set_the_scene
    call clear_the_room (Girl)
    call Taboo_Level (1)

    if Girl.GirlLikeCheck(Other) >= 900:
        $ Resolution += 2
    elif Girl.GirlLikeCheck(Other) >= 800:
        $ Resolution += 1
    $ B = int((Girl.GirlLikeCheck(Other) - 500)/2)

    $ Resolution -= Girl.Cheated if Girl.Cheated <= 3 else 3

    if Girl.Cheated:
        $ Girl.change_stat("love", 200, -50)
        $ Girl.change_stat("obedience", 80, -20)
        $ Girl.change_stat("inhibition", 50, -50)
        if Girl == RogueX:
            ch_r "Why're you screw'in around on me again?"
        elif Girl == KittyX:
            ch_k "Again with this?!"
        elif Girl == EmmaX:
            ch_e "I noticed you're back to jumping anything that moves. . ."
        elif Girl == LauraX:
            ch_l "You were screwing someone else again."
        elif Girl == JeanX:
            ch_j "You were sneaking around with. . . someone again!"
        elif Girl == StormX:
            ch_s "You are straying again. . ."
        elif Girl == JubesX:
            ch_v "You're sleeping around on me again. . ."
    else:
        $ Girl.change_stat("love", 200, -100)
        $ Girl.change_stat("obedience", 80, -30)
        $ Girl.change_stat("inhibition", 50, -20)
        if Girl == RogueX:
            ch_r "What the hell was that about earlier?"
        elif Girl == KittyX:
            ch_k "Hello?! What was that?"
        elif Girl == EmmaX:
            ch_e "Do you mind explaining what I saw earlier?"
        elif Girl == LauraX:
            ch_l "You were with someone else earlier."
        elif Girl == JeanX:
            ch_j "Hey! I saw you with. . . "
            ch_j ". . . I can't remember her name, but I saw you!"
        elif Girl == StormX:
            ch_s "I see that you've found someone else to occupy your time. . ."
        elif Girl == JubesX:
            ch_v "I think you've been cheating. . ."

    menu:
        extend ""
        "I'm sorry.":
            $ Girl.change_stat("love", 90, 30)
            $ Girl.change_stat("obedience", 80, -10)
            $ Line = "sorry"
            $ Resolution += 1
        "What do you mean?":

            $ Girl.change_stat("love", 200, -10)
            $ Girl.change_stat("obedience", 80, 15)
            $ Girl.change_stat("inhibition", 80, 5)
            if Girl == StormX:
                ch_s "I am talking about you and [Other.name]. . ."
            else:
                Girl.voice "I mean you screwing around with [Other.name]!"
            menu:
                extend ""
                "Oh! I'm sorry!":
                    $ Girl.change_stat("love", 90, 20)
                    $ Girl.change_stat("obedience", 80, -10)
                    $ Line = "sorry"
                "Oh, that. Yeah.":
                    $ Girl.change_stat("love", 200, -20)
                    $ Girl.change_stat("obedience", 80, 10)
                    $ Line = "yeah"
                    $ Resolution -= 1
        "You mean with [Other.name]?":

            $ Girl.change_stat("love", 200, -15)
            $ Girl.change_stat("obedience", 80, 20)
            $ Girl.change_stat("inhibition", 80, 10)
            Girl.voice "Yes, \"I mean with [Other.name].\""

            if Girl == RogueX:
                $ Line = "Y'all were screwing around behind my back!"
            elif Girl == KittyX:
                $ Line = "Why were you all over her like that?!"
            elif Girl == EmmaX:
                $ Line = "Or didn't you notice who you were fucking?"
            elif Girl == LauraX:
                $ Line = "I can smell her on you."
            elif Girl == JeanX:
                $ Line = "I played back her memories of it!"
            elif Girl == StormX:
                $ Line = "I know that the two of your were together."
            elif Girl == JubesX:
                ch_v "I have a sensitive nose. . ."

            if Girl.Cheated:
                $ Line = Line+" Again!"
            Girl.voice "[Line]"
            menu:
                extend ""
                "Oh! I'm sorry!":
                    $ Girl.change_stat("love", 90, 15)
                    $ Girl.change_stat("obedience", 80, -10)
                    $ Line = "sorry"
                "Oh, yeah.":
                    $ Girl.change_stat("love", 200, -20)
                    $ Girl.change_stat("obedience", 80, 10)
                    $ Line = "yeah"
                    $ Resolution -= 2

    if Line == "sorry":
        $ Girl.change_face("_sadside")
        if Girl == RogueX:
            ch_r "Well 'course you are, but that don't make it right."
            ch_r "Screwing around with [Other.name] like that. . ."
        elif Girl == KittyX:
            ch_k "Don't you tell me you're sorry, I'll tell you when you're sorry!"
        elif Girl == EmmaX:
            ch_e "Very sorry indeed. . ."
        elif Girl == LauraX:
            ch_l "You will be."
        elif Girl == JeanX:
            ch_j "Of course you are!"
        elif Girl == StormX:
            ch_s "I am certain that you are."
        elif Girl == JubesX:
            ch_v "Oh, I bet you are."
        $ Girl.change_face("_sad")
    else:
        $ Girl.change_face("_confused")
        if Girl == RogueX:
            ch_r "Oh? So what do you have to say for yourself?"
        elif Girl == KittyX:
            ch_k "Yeah? Yeah?! What does that even mean?!"
        elif Girl == EmmaX:
            ch_e "I'm not sure you understand what trouble you're in here. . ."
        elif Girl == LauraX:
            ch_l "So did you have an explanation, or. . ."
        elif Girl == JeanX:
            ch_j "So do you have a story to tell me?!"
        elif Girl == StormX:
            ch_s "Did you have some explanation?"
        elif Girl == JubesX:
            ch_v "Well, did you have some excuse?"
        $ Girl.change_face("_angry")

    menu:
        extend ""
        "I really hurt you, and I'm sorry.":
            $ Girl.change_stat("love", 90, 25)
            if Girl == JeanX:
                $ Girl.change_stat("obedience", 80, 10)
                $ Resolution += 1
                ch_j "Yes, we've established that, what else?"
            else:
                $ Girl.change_stat("obedience", 80, -5)
                Girl.voice "Well at least you're owning up to it."
            $ Resolution += 2
        "We were just messing around, nothing serious.":

            $ Girl.change_stat("obedience", 80, 30)
            $ Girl.change_stat("inhibition", 80, 10)
            if Girl == RogueX:
                ch_r "\"Nothing serious?\" You did {i}not{/i} just tell me that."
            elif Girl == KittyX:
                ch_k "I'll \"nothing serious\" you!"
            elif Girl == EmmaX:
                ch_e "I'll be the judge of what is or is not \"serious.\""
            elif Girl == LauraX:
                if approval_check(Girl, 1500):
                    ch_l "Ok, that's fair."
                else:
                    ch_l "Do you want to try that one again?"
            elif Girl == JeanX:
                $ Girl.eyes = "_side"
                $ Girl.change_stat("love", 80, 10)
                $ Resolution += 1
                ch_j "Oh. . . well. . ."
                $ Girl.change_face("_angry",2)
                ch_j "That's not the point!"
                $ Girl.blushing = "_blush1"
            elif Girl == StormX:
                ch_s "Nothing serious to you, but what of me?"
            elif Girl == JubesX:
                ch_v "Oh, is that supposed to be an excuse?"
            $ Girl.change_stat("love", 200, -25)

            if not approval_check(Girl, 700, "O", Bonus = (B/3)):
                $ Resolution -= 2
        "I think she's really hot.":

            if B >= 100 or approval_check(Girl, 500, "I", Bonus = (B/3)):

                $ Girl.change_face("_confused",Eyes="_side")
                if Girl == StormX:
                    ch_s "She is certainly beautiful, but I do not see why that would be an excuse."
                elif Other == KittyX:
                    Girl.voice "Well. . . yeah, she is cute, but so what?"
                else:
                    Girl.voice "Well. . . yeah, she is hot, but so what?"
                $ Girl.change_stat("lust", 90, 5)
                $ Line = "threeway"
            else:
                $ Girl.change_stat("love", 200, -20)
                $ Girl.change_stat("obedience", 80, 30)
                if Girl == RogueX:
                    ch_r "Well that don't mean shit, [Player.name], you're with me!"
                elif Girl == KittyX:
                    ch_k "What does that have to do with anything?!"
                elif Girl == EmmaX:
                    ch_e "But I am here. [[gestures to encompass her body]"
                elif Girl == LauraX:
                    ch_l "That doesn't make her fair game."
                elif Girl == JeanX:
                    ch_j "That doesn't mean you're allowed to fuck her!"
                elif Girl == StormX:
                    ch_s "I do not see how that makes it better."
                elif Girl == JubesX:
                    ch_v "I don't care how hot she is!"
                $ Resolution -= 2
        "Don't you like her?":

            $ Girl.change_stat("obedience", 80, 30)
            if B >= 100 or approval_check(Girl,500,"I"):

                $ Girl.change_face("_confused",Eyes="_side")
                $ Girl.change_stat("inhibition", 90, 25)
                $ Girl.change_stat("lust", 90, 5)
                if Girl == RogueX:
                    ch_r "I mean, sorta. Not like that really though. . ."
                elif Girl == KittyX:
                    ch_k "What, like. . . \"like\" like? Um. . ."
                elif Girl == EmmaX:
                    ch_e "She is attractive, yes, but I don't think that's relevant."
                elif Girl == LauraX:
                    ch_l "Yeah, but I like you too."
                elif Girl == JeanX:
                    ch_j "I mean. . . kinda. . ."
                elif Girl == StormX:
                    ch_s "I do, though perhaps not as much as you do. . ."
                elif Girl == JubesX:
                    ch_v "Well, yeah, but. . . don't distract me!"
                $ Line = "threeway"
            elif B >= 50 and Girl != JeanX:

                $ Girl.change_face("_confused")
                $ Girl.change_stat("love", 200, -10)
                if Girl == EmmaX and Other != StormX:
                    ch_e "She's a good student, but that doesn't mean I'm interested in sharing."
                elif Girl == StormX:
                    ch_s "I like her well enough, but what difference does that make?"
                else:
                    Girl.voice "We're friends, but so what?"
            else:
                $ Girl.change_stat("love", 200, -20)
                if Girl == RogueX:
                    ch_r "Whether I like her or not, don't give you rights to hook up with her."
                elif Girl == KittyX:
                    ch_k "What does that have to do with anything?!"
                elif Girl == EmmaX:
                    ch_e "That's entirely irrelevant!"
                elif Girl == LauraX:
                    ch_l "Not enough to share."
                elif Girl == JeanX:
                    ch_j "Not enough."
                elif Girl == StormX:
                    ch_s "I am afraid not enough."
                elif Girl == JubesX:
                    ch_v "I don't care how hot she is!"
                $ Resolution -= 1

    menu:
        "I won't do it again.":
            if Girl.Cheated:
                $ Girl.change_stat("love", 90, 5)
                Girl.voice "Like the last time you told me that, you mean?"
                $ Resolution -= 1
            else:
                $ Girl.change_stat("love", 90, 20)
                $ Girl.change_face("_angry")
                $ Resolution += 2 if Resolution < 3 else 0
                Girl.voice "I'll hold you to that."
            $ Line = 0
        "I can't make any promises, she's pretty hot.":

            $ Girl.change_face("_angry")
            $ Girl.change_stat("love", 200, -40)
            $ Girl.change_stat("obedience", 90, 40)
            $ Girl.change_stat("inhibition", 90, 10)
            Girl.voice "Then I don't know what you tell you, I think we're through."
            $ Resolution -= 2
            $ Line = 0
        "Have you considered maybe letting her join us?":

            $ Girl.change_face("_confused",Mouth="_smile")
            if approval_check(Girl, 2200, Bonus = B) or approval_check(Girl, 950, "L", Bonus = (B/3)):
                $ Girl.change_stat("inhibition", 90, 30)
                $ Girl.change_stat("lust", 89, 10)
                $ Resolution += 2
            elif approval_check(Girl, 1500, Bonus = B) or Girl.GirlLikeCheck(Other) >= 700:
                $ Girl.change_stat("inhibition", 90, 10)
                $ Girl.change_stat("lust", 90, 5)
            else:
                $ Resolution -= 3
                $ Girl.change_stat("love", 200, -25)
                $ Girl.change_stat("inhibition", 90, 10)

            $ Girl.change_stat("obedience", 90, 40)
            if Girl == RogueX:
                ch_r "I don't know what to do with that, you talk'in a three-way?"
            elif Girl == KittyX:
                ch_k "What, like a threeway?"
            elif Girl == EmmaX:
                ch_e "I'm not sure how to process that."
                ch_e "Are you suggesting a threeway?"
            elif Girl == LauraX:
                ch_l "You wanna fuck both of us?"
            elif Girl == JeanX:
                ch_j "Yeah, maybe. But not like you just randomly fucking around."
            elif Girl == StormX:
                ch_s "An interesting proposition. . ."
            elif Girl == JubesX:
                ch_v "What? . . I mean. . . "
                ch_v ". . . what?"
            $ Line = "threeway"

    if Resolution >= 5 and Line == "threeway":
        if Girl.Cheated:
            $ Girl.change_stat("love", 90, 25)
            $ Girl.change_stat("obedience", 90, 30)
            $ Girl.change_stat("inhibition", 90, 60)
        else:
            $ Girl.change_stat("love", 90, 50)
            $ Girl.change_stat("obedience", 90, 40)
            $ Girl.change_stat("inhibition", 90, 40)
        if Girl == RogueX:
            ch_r "So I catch you fool'in around on me, and you want to make it official?"
        elif Girl == KittyX:
            ch_k "So you cheat on me, and then ask for a threeway?"
        elif Girl == EmmaX:
            ch_e "Bold move. Boldness should be rewarded. . ."
        elif Girl == LauraX:
            ch_l "Cheat on me, and then Ask for a threeway?"
            ch_l "Risky gamble there."
        elif Girl == JeanX:
            ch_j "I was thinking that -I- would be bringing other people in. . ."
        elif Girl == StormX:
            ch_s "I suppose it could be. . . mutually beneficial."
        elif Girl == JubesX:
            ch_v "I mean, I guess we could. . ."
        Girl.voice "Maybe I could live with that, I'll talk to [Other.name]."

        $ Line = "poly"

    elif Resolution >= 5:
        if Girl.Cheated:
            $ Girl.change_stat("love", 90, 20)
            $ Girl.change_stat("obedience", 90, 10)
            $ Girl.change_stat("inhibition", 90, 100)
        else:
            $ Girl.change_stat("love", 90, 40)
            $ Girl.change_stat("obedience", 90, 10)
            $ Girl.change_stat("inhibition", 90, 60)
        if Girl == RogueX:
            ch_r "You're just a regular polecat in heat. I guess I can't tame you."
            ch_r "Not alone, at least."
        elif Girl == KittyX:
            ch_k "What a mess. I guess maybe I could share though. . ."
        elif Girl == EmmaX:
            ch_e "Bold move. Boldness should be rewarded. . ."
        elif Girl == LauraX:
            ch_l "You're a piece of work, but maybe I could share . . ."
        elif Girl == JeanX:
            ch_j "I was thinking that -I- would be bringing other people in. . ."
        elif Girl == StormX:
            ch_s "Perhaps there is a way we could both benefit from this."
        elif Girl == JubesX:
            ch_v "Maybe we could work together. . ."

        if Girl in (EmmaX,StormX):
            Girl.voice "Perhaps [Other.name] and I could work something out."
        else:
            Girl.voice "Maybe me and [Other.name] can work something out."
        $ Line = "poly"

    elif Resolution >= 2:
        if Line == "threeway":

            $ Girl.change_stat("obedience", 80, 10)
            if Girl == RogueX:
                ch_r "Don't try to play cards ya just don't have."
            elif Girl == KittyX:
                ch_k "Way to read the room. . ."
            elif Girl == EmmaX:
                ch_e "I appreciate the initiative, if not the common sense. . ."
            elif Girl == LauraX:
                ch_l "Like that'll happen . . ."
            elif Girl == JeanX:
                ch_j "Nah, you haven't earned it."
            elif Girl == StormX:
                ch_s "I do not think you're prepared for such a relationship."
            elif Girl == JubesX:
                ch_v "I'm not interested in that right now!"
        $ Girl.change_face("_sadside")
        if Girl.Cheated:
            $ Girl.change_stat("obedience", 80, 15)
            if Girl == RogueX:
                ch_r "I've given you a chance to do right by me, and you keep screwing it up."
                ch_r "I don't know how many more chances I can give you here."
            elif Girl == KittyX:
                ch_k "Too many times, [KittyX.player_petname]. . ."
            elif Girl == EmmaX:
                ch_e "At some point I'll have to stop putting up with you. . ."
            elif Girl == LauraX:
                ch_l "This is getting tired . . ."
            elif Girl == JeanX:
                ch_j "I'm not giving you more chances to fuck this up."
            elif Girl == StormX:
                ch_s "You have betrayed my trust too many times."
            elif Girl == JubesX:
                ch_v "You've just played me too many times. . ."
        else:
            $ Girl.change_stat("obedience", 80, 30)
            if Girl == RogueX:
                ch_r "You betrayed my trust, [RogueX.player_petname]."
                ch_r "Don't let it happen again."
            elif Girl == KittyX:
                ch_k "You hurt me here, [KittyX.player_petname]. . ."
                ch_k "Don't hurt me like this again."
            elif Girl == EmmaX:
                ch_e "I'll let you off with a warning this time, but don't let it happen again."
            elif Girl == LauraX:
                ch_l "You're on thin ice, bub."
            elif Girl == JeanX:
                ch_j "I'll let you off this time, but don't push it."
            elif Girl == StormX:
                ch_s "You have betrayed my trust, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "I don't like these games. . ."
    else:


        $ Girl.change_face("_angry")
        if Line == "threeway":
            $ Girl.change_stat("obedience", 80, 10)
            if Girl == RogueX:
                ch_r "I can't even believe you would suggest a fucking {i}threeway!{/i}"
            elif Girl == KittyX:
                ch_k "Seriously? A threeway?!"
            elif Girl == EmmaX:
                ch_e "Bold move. Sometimes boldness will get you hurt. . ."
            elif Girl == LauraX:
                ch_l "A threeway?"
            elif Girl == JeanX:
                ch_j "You're seriously looking for a prize here?"
            elif Girl == StormX:
                ch_s "I do not think you're prepared for such a relationship."
            elif Girl == JubesX:
                ch_v "You're pushing it."
        if Girl.Cheated:
            $ Girl.change_stat("obedience", 90, -50)
            $ Girl.change_stat("inhibition", 90, 20)
            if Girl == RogueX:
                ch_r "You done this too many times for me to keep let'in you back."
                ch_r "Sorry, [RogueX.player_petname], this is the end."
            elif Girl == KittyX:
                ch_k "You aren't even that cute. . ."
                ch_k "We're over."
            elif Girl == EmmaX:
                ch_e "I don't think I'm in the mode for these games."
                ch_e "We're done."
            elif Girl == LauraX:
                ch_l "I hoped I could trust you, but you blew it again. . ."
            elif Girl == JeanX:
                ch_j "I gave you a shot, but you blew it."
            elif Girl == StormX:
                ch_s "You have betrayed my trust too many times."
            elif Girl == JubesX:
                ch_v "You've just played me too many times!"
        else:
            $ Girl.change_stat("obedience", 90, -50)
            $ Girl.change_stat("inhibition", 90, 10)
            if Girl == RogueX:
                ch_r "I just don't think I can trust you anymore, [RogueX.player_petname]."
                ch_r "This is it for us."
            elif Girl == KittyX:
                ch_k "You hurt me. I just can't even."
            elif Girl == EmmaX:
                ch_e "You've lost my trust. We're done here."
            elif Girl == LauraX:
                ch_l "I can't trust you. I'm through."
            elif Girl == JeanX:
                ch_j "I gave you a shot, but you blew it."
            elif Girl == StormX:
                ch_s "You have betrayed my trust, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "I don't like these games!"

        $ Girl.add_word(1,0,0,"ex",0)
        if Girl in Player.Harem:
            $ Player.Harem.remove(Girl)
        $ Girl.add_word(1,0,"_angry",0,0)



    $ BO = all_Girls[:]
    while BO:

        $ Girl.drain_word("saw with "+BO[0].tag,0,0,1)
        $ BO.remove(BO[0])

    if Line == "poly":
        $ Girl.add_word(1,0,0,"poly "+Other.tag,0)
        $ Girl.add_word(1,0,0,"ask "+Other.tag,0)
    else:
        $ Girl.GLG(Other,1000,-50,1)

    if "ex" in Girl.traits:
        $ Girl.Break[0] = 5 + Girl.Break[1] + Girl.Cheated
    $ Girl.Cheated += 1


    menu:
        "I'm glad we could work this out." if Girl in Player.Harem:
            $ Girl.change_face("_sad")
            if Resolution >= 3:
                $ Girl.change_stat("love", 90, 10)
                $ Girl.change_stat("obedience", 90, 5)
                if Girl == RogueX:
                    ch_r "I am too, [RogueX.player_petname]."
                elif Girl == KittyX:
                    ch_k "Me too, [KittyX.player_petname]. . ."
            else:
                $ Girl.change_stat("love", 90, 5)
                if Girl == RogueX:
                    ch_r "Yeah, we'll see, [RogueX.player_petname]."
                elif Girl == KittyX:
                    ch_k "Sure, [KittyX.player_petname]. . ."
            if Girl == EmmaX:
                ch_e "Yes, delightful."
            elif Girl == LauraX:
                ch_l "Yeah, sure."
            elif Girl == JeanX:
                ch_j "Right, sure."
            elif Girl == StormX:
                ch_s "We shall see if I made the correct decision, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "Yeah, maybe. . ."

        "Want to fool around a bit?" if Girl in Player.Harem and not Taboo:
            if Girl.obedience + Girl.inhibition >= (1.5*Girl.love) or Girl.lust >= 70:

                $ Girl.change_face("_sly",Eyes="_side")
                $ Girl.change_stat("love", 90, 20)
                $ Girl.change_stat("obedience", 90, 10)
                $ Girl.change_stat("inhibition", 90, 10)
                if Girl == StormX:
                    ch_s "You are incorrigible, [StormX.player_petname]."
                else:
                    Girl.voice "Sure, whatever."
                call expression Girl.tag + "_SMenu"
            else:
                $ Girl.change_face("_sad")
                $ Girl.change_stat("love", 90, -10)
                $ Girl.change_stat("obedience", 90, -10)
                if Girl == RogueX:
                    ch_r "It's still too raw, [RogueX.player_petname]."
                elif Girl == KittyX:
                    ch_k "Don't even, [KittyX.player_petname]. . ."
                elif Girl == EmmaX:
                    ch_e "Oh, this is rich."
                elif Girl == LauraX:
                    ch_l "Yeah, not now."
                elif Girl == JeanX:
                    ch_j "Maybe later."
                elif Girl == StormX:
                    ch_s "Take some time to reflect on your actions, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Don't even with me right now. . ."

        "I'm sorry it didn't work out." if Girl not in Player.Harem:
            $ Girl.change_face("_sad")
            $ Girl.change_stat("love", 90, 10)
            if Girl == RogueX:
                ch_r "I am too, [RogueX.player_petname]."
            elif Girl == KittyX:
                ch_k "Yeah, me too, [KittyX.player_petname]. . ."
            elif Girl == EmmaX:
                ch_e "Yes, you'll get over it. . . eventually."
            elif Girl == LauraX:
                ch_l "Yeah."
            elif Girl == JeanX:
                ch_j "Sure, whatever."
            elif Girl == StormX:
                ch_s "Yes, it is unfortunate. . ."
            elif Girl == JubesX:
                ch_v "Yeah, maybe. . ."

        "Want to have some break-up sex?" if Girl not in Player.Harem and not Taboo:
            if Girl.obedience + Girl.inhibition >= (1.5*Girl.love) or Girl.lust >= 70:

                $ Girl.change_face("_angry",Eyes="_side")
                $ Girl.change_stat("obedience", 90, 10)
                $ Girl.change_stat("inhibition", 90, 10)
                if Girl == StormX:
                    ch_s "You are incorrigible, [StormX.player_petname]."
                else:
                    Girl.voice "Sure, whatever."
                $ Girl.drain_word("_angry",0,1)
                call expression Girl.tag + "_SMenu"
                $ Girl.add_word(1,0,"_angry",0,0)
            else:
                $ Girl.change_face("_angry")
                $ Girl.change_stat("love", 90, -20)
                $ Girl.change_stat("obedience", 90, -10)
                if Girl == RogueX:
                    ch_r "You have got to be kidding me."
                elif Girl == KittyX:
                    ch_k "Don't even, [KittyX.player_petname]. . ."
                elif Girl == EmmaX:
                    ch_e "Oh, this is rich."
                elif Girl == LauraX:
                    ch_l "Yeah, not now."
                elif Girl == JeanX:
                    ch_j "Maybe later."
                elif Girl == StormX:
                    ch_s "Take some time to reflect on your actions, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Don't even with me right now. . ."

        "Let me know if you change your mind." if Girl not in Player.Harem:
            $ Girl.change_face("_angry",Eyes="_side")
            $ Girl.change_stat("love", 90, -5)
            $ Girl.change_stat("obedience", 90, 10)
            if Girl == RogueX:
                ch_r "Yeah, I'll get right on that."
            elif Girl == KittyX:
                ch_k "Oh, sure, right."
            elif Girl == EmmaX:
                ch_e "Oh, I'm sure you'll be the first I tell."
            elif Girl == LauraX:
                ch_l "Uh-huh."
            elif Girl == JeanX:
                ch_j "Oh, sure."
            elif Girl == StormX:
                ch_s "I am sure that I will, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "Sure, whatever. . ."
        "Ok, see you later then.":

            $ Girl.change_face("_confused")

    if Girl == RogueX:
        ch_r "I need some time alone, [RogueX.player_petname]. I'll see you later."
    elif Girl == KittyX:
        ch_k "I need some \"me\" time, I'll see you around."
    elif Girl == EmmaX:
        ch_e "Now, I need to be alone for a bit."
    elif Girl == LauraX:
        ch_l "Ok, well, bye."
    elif Girl == StormX:
        ch_s "I'm sure that I will see you later, [StormX.player_petname]."
    elif Girl == JubesX:
        ch_v "I'm gonna. . . get out of here. . ."

    $ Round -= 10 if Round > 10 else Round

    if bg_current == Girl.home:

        $ bg_current = "bg_player"
        jump Misplaced
    else:
        call Remove_Girl (Girl)
    return







label NoFap(Girl=0, TabStore=Taboo, counter=0):



    $ Taboo = 0
    ch_p "About when you masturbate on your own time. . ."

    if "askedfap" in Girl.daily_history:

        if "nofap" in Girl.traits:
            Girl.voice "I understand already."
        else:
            Girl.voice "Stop bothering me with this."

    elif "askedfap" in Girl.history:

        if not approval_check(Girl, 800):

            $ Girl.change_face("_angry",2,Eyes="_surprised")
            $ Girl.change_stat("love", 80, -1)
            $ Girl.change_stat("obedience", 50, 1)
            $ Girl.change_stat("obedience", 80, 1)
            $ Girl.change_stat("inhibition", 30, -1)
            $ Girl.change_stat("inhibition", 30, 3, 1)
            if Girl == RogueX:
                ch_r "I really don't want to go over this again. . ."
            elif Girl == KittyX:
                ch_k "This isn't really appropriate. . . "
            elif Girl == EmmaX:
                ch_e "I'd rather not discuss this again. . ."
            elif Girl == LauraX:
                ch_l "Hmm, I don't want to have this conversation again."
            elif Girl == JeanX:
                ch_j "We've been over this, and you were insane."
            elif Girl == StormX:
                ch_s "This really is none of your business, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "You, um, need to stop asking. . ."
            $ Girl.change_face("_angry",1)
        else:

            $ Girl.change_stat("obedience", 60, 2)
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 60, 1)
            $ Girl.change_stat("lust", 50, 1)
            $ Girl.change_face("_confused",1)
            if Girl == EmmaX:
                ch_e "Oh? This again?"
            elif Girl == LauraX:
                ch_l "Yeah?"
            elif Girl == StormX:
                ch_s "Oh, what is it, [StormX.player_petname]?"
            else:
                $ Girl.change_face("_confused",2)
                Girl.voice "Um, yeah, what about it?"
    else:


        if not approval_check(Girl, 800):

            $ Girl.change_face("_angry",2,Eyes="_surprised")
            $ Girl.change_stat("love", 90, -5)
            $ Girl.change_stat("obedience", 50, 3)
            $ Girl.change_stat("obedience", 80, 1)
            $ Girl.change_stat("inhibition", 30, -1)
            $ Girl.change_stat("inhibition", 30, 3, 1)
            if Girl == RogueX:
                ch_r "Don't go talk'in about a girl's personal time like that."
            elif Girl == KittyX:
                ch_k "I, um. . . "
                extend "hey! That's not any of your business!"
            elif Girl == EmmaX:
                ch_e "What I do in the privacy of my own class-"
                ch_e "Never mind."
            elif Girl == LauraX:
                ch_l "Hmm, I don't want to have this conversation."
            elif Girl == JeanX:
                ch_j ". . ."
                ch_j "Why are you talking about my personal habits?"
            elif Girl == StormX:
                ch_s ". . ."
                ch_s "I am not really sure what business that is of yours, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "Do I. . ."
                ch_v "What? What business is that of yours?!"
            $ Girl.change_face("_angry",1)
        elif not approval_check(Girl, 500, "I"):

            $ Girl.change_stat("love", 90, -5)
            $ Girl.change_stat("obedience", 50, 3)
            $ Girl.change_stat("obedience", 80, 1)
            $ Girl.change_stat("inhibition", 30, -1)
            $ Girl.change_stat("inhibition", 30, 3, 1)
            $ Girl.change_stat("lust", 50, 3)
            if Girl == RogueX:
                $ Girl.change_face("_surprised",2)
                ch_r "I. . um. . I don't really do that. . ."
            elif Girl == KittyX:
                $ Girl.change_face("_surprised",2)
                ch_k "Oh, um, that's not really something I. . ."
            elif Girl == EmmaX:
                $ Girl.change_face("_confused",1)
                ch_e "I'm not sure why what I do in private is your business. . ."
            elif Girl == LauraX:
                $ Girl.change_face("_surprised",2)
                ch_l "Um. . . yeah?"
            elif Girl == JeanX:
                ch_j "Well, look. . . that's none of your business."
            elif Girl == StormX:
                ch_s ". . ."
                ch_s "I am not really sure what business that is of yours, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "Do I. . ."
                ch_v "What? Um. . . I don't wanna talk about it."
        elif approval_check(Girl, 500, "O"):

            $ Girl.change_stat("obedience", 90, 5)
            $ Girl.change_stat("inhibition", 50, 2)
            $ Girl.change_stat("inhibition", 80, 1)
            $ Girl.change_stat("lust", 50, 5)
            $ Girl.change_face("_confused",1)
            if Girl == EmmaX:
                ch_e "What of it?"
            else:
                Girl.voice "What about it?"
        else:

            $ Girl.change_stat("obedience", 90, 4)
            $ Girl.change_stat("inhibition", 90, 3)
            $ Girl.change_stat("lust", 50, 3)
            $ Girl.change_face("_confused",1)
            if Girl == EmmaX:
                ch_e "Oh? What about it?"
            elif Girl in (LauraX,JeanX):
                Girl.voice "Yeah?"
            elif Girl == StormX:
                ch_s ". . ."
                ch_s "What did you want to know?"
            else:
                $ Girl.change_face("_confused",2)
                Girl.voice "Um, yeah, what about it?"


    menu:
        extend ""
        "I'd rather you not do that." if "nofap" not in Girl.traits:
            if "askedfap" not in Girl.daily_history:
                $ Girl.change_stat("obedience", 200, 2)
                $ Girl.change_stat("inhibition", 90, 1)
            if approval_check(Girl, 1400, "LO"):

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("love", 90, 4)
                    $ Girl.change_stat("obedience", 200, 5)
                    $ Girl.change_stat("inhibition", 90, 3)
                $ Girl.change_face("_bemused",2)
                if Girl == RogueX:
                    ch_r "Well, only because it seems to matter to you. . ."
                elif Girl == KittyX:
                    ch_k "You really care about something like that?"
                    ch_k "Ok, fine."
                elif Girl == EmmaX:
                    ch_e "[EmmaX.player_petname], the idea of it really bothers you?"
                    ch_e "Fine, I can make do. . ."
                elif Girl == LauraX:
                    ch_l "So, that'd really bother you? . ."
                    ch_l "I guess I could stop. . ."
                elif Girl == JeanX:
                    ch_j "Hmm. . ."
                    ch_j "I guess we could give that a try. . ."
                    ch_j "But you'd better make it up to me."
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "If you truly believe you can take over my needs, [StormX.player_petname]. . ."
                elif Girl == JubesX:
                    ch_v "Well, I mean. . ."
                    ch_v "I do have needs. . ."
                    ch_v "You would need to make sure they get. . . taken care of."
                $ Girl.change_face("_bemused",1)
            elif approval_check(Girl, 1600) and not approval_check(Girl, 500, "I") and Girl != JeanX:

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("obedience", 200, 5)
                    $ Girl.change_stat("inhibition", 90, 5)
                    $ Girl.change_stat("lust", 50, 5)
                $ Girl.change_face("_bemused",2,Eyes="_side")
                if Girl == RogueX:
                    ch_r "Not that I was, but. . . sure."
                elif Girl == KittyX:
                    ch_k "I don't. . . right, I don't."
                elif Girl == EmmaX:
                    ch_e "I suppose if it matters to you. . ."
                elif Girl == LauraX:
                    ch_l "I guess if it matters to you. . ."
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "I am not really sure what business that is of yours, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "I don't really. . ."
                    ch_v "Ok, we'll see. . ."
                $ Girl.change_face("_bemused",1)
            elif approval_check(Girl, 700, "O",Alt=[[JeanX],800]):

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("love", 90, 3)
                    $ Girl.change_stat("obedience", 200, 4)
                    $ Girl.change_stat("inhibition", 90, 5)
                    $ Girl.change_stat("lust", 70, 5)
                $ Girl.change_face("_sly",1)
                Girl.voice "Yes,[Girl.player_petname]."
            elif not approval_check(Girl, 800):

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("love", 90, -5)
                    $ Girl.change_stat("obedience", 90, -3)
                    $ Girl.change_stat("inhibition", 90, 3)
                $ Girl.change_face("_angry",2)
                if Girl == KittyX:
                    ch_k "I- this whole conversation is inappropriate!"
                elif Girl in (EmmaX,JeanX):
                    Girl.voice "I really don't care what \"you'd rather.\""
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "I am uninterested in your opinions on this, [StormX.player_petname]."
                else:
                    Girl.voice "I'd rather you stay out my business."
                $ Girl.change_face("_angry",1)
                $ counter = 1
            else:

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("love", 90, -1)
                    $ Girl.change_stat("obedience", 70, 2)
                    $ Girl.change_stat("inhibition", 60, 2)
                $ Girl.change_face("_sly",1)
                if Girl == RogueX:
                    ch_r "'Fraid not, [RogueX.player_petname]."
                elif Girl == KittyX:
                    ch_k "Sorry, no. I try to keep busy."
                elif Girl == EmmaX:
                    ch_e "No, I think I shall. . . often."
                elif Girl == LauraX:
                    ch_l "Sorry, [LauraX.player_petname], I've got needs."
                elif Girl == JeanX:
                    $ Girl.change_face("_confused",1)
                    ch_j "Um. . . no?"
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "I would rather we not discuss this, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Um, that would be very inconvenient for me, so. . ."
                    ch_v "No."
                $ counter = 1
            if not counter:
                $ Girl.add_word(1,0,0,"nofap")


        "Don't do that without permission." if "nofap" not in Girl.traits:
            if "askedfap" not in Girl.daily_history:
                $ Girl.change_stat("obedience", 200, 3)
            if approval_check(Girl, 600, "O"):

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("love", 90, 3)
                    $ Girl.change_stat("obedience", 80, 3)
                    $ Girl.change_stat("obedience", 200, 4)
                    $ Girl.change_stat("inhibition", 90, 5)
                    $ Girl.change_stat("lust", 50, 5)
                    $ Girl.change_stat("lust", 70, 5)
                $ Girl.change_face("_sly")
                Girl.voice "Yes,[Girl.player_petname]."
            elif approval_check(Girl, 1200, "LO"):

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("love", 90, 4)
                    $ Girl.change_stat("obedience", 80, 3)
                    $ Girl.change_stat("obedience", 200, 5)
                    $ Girl.change_stat("inhibition", 90, 3)
                    $ Girl.change_stat("lust", 50, 5)
                $ Girl.change_face("_bemused",1)
                if Girl == RogueX:
                    ch_r "I guess if it means so much to you. . ."
                elif Girl == KittyX:
                    ch_k "I guess I could do \"no_fap no-\" what month even is this? . ."
                elif Girl == EmmaX:
                    ch_e "Well, aren't you being dominant. . ."
                    ch_e "I suppose I could restrain myself. . ."
                elif Girl == LauraX:
                    ch_l "I guess I could."
                elif Girl == JeanX:
                    ch_j "Hmm. . ."
                    ch_j "I guess we could give that a try. . ."
                    ch_j "But you'd better make it up to me."
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "Well, I could give that a try, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Well, I mean. . ."
                    ch_v "I do have needs. . ."
                    ch_v "You would need to make sure they get. . . taken care of."
            elif not approval_check(Girl, 500, "I"):

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("obedience", 200, 5)
                    $ Girl.change_stat("inhibition", 90, 5)
                    $ Girl.change_stat("lust", 50, 5)
                $ Girl.change_face("_bemused",2,Eyes="_side")
                if Girl == RogueX:
                    ch_r "It's not like I even do. . ."
                elif Girl == KittyX:
                    ch_k "Girls don't do that. But even if I did, you're being rude."
                elif Girl == EmmaX:
                    ch_e "I really don't think it's any of your business."
                elif Girl == LauraX:
                    ch_l "Not interested."
                elif Girl == JeanX:
                    ch_j "I don't like your tone. . ."
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "Do not take this tone with me, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Um, I don't know about that. . ."
                $ Girl.change_face("_normal",1)
                $ counter = 1
            elif not approval_check(Girl, 800):

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("love", 70, -5)
                    $ Girl.change_stat("love", 90, -5)
                    $ Girl.change_stat("obedience", 60, -3)
                    $ Girl.change_stat("obedience", 90, -3)
                    $ Girl.change_stat("inhibition", 90, 3)
                $ Girl.change_face("_angry",2)
                if Girl == RogueX:
                    ch_r "Fuck you I won't."
                elif Girl == KittyX:
                    ch_k "I- this whole conversation is inappropriate!"
                elif Girl == EmmaX:
                    ch_e "I really don't think it's any of your business."
                elif Girl == LauraX:
                    ch_l "Don't tell me what to do."
                elif Girl == JeanX:
                    ch_j "Buzz off."
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "I would rather we not discuss this, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Rude. . ."
                $ Girl.change_face("_angry",1)
                $ counter = 1
            else:

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("love", 90, -2)
                    $ Girl.change_stat("obedience", 70, -2)
                    $ Girl.change_stat("inhibition", 60, 2)
                $ Girl.change_face("_bemused",2)
                if Girl == RogueX:
                    ch_r "'Fraid not, [RogueX.player_petname]."
                elif Girl == KittyX:
                    ch_k "Sorry, no. I try to keep busy."
                elif Girl == EmmaX:
                    ch_e "No, I think I shall. . . often."
                elif Girl == LauraX:
                    ch_l "Sorry, [LauraX.player_petname], I've got needs."
                elif Girl == JeanX:
                    $ Girl.change_face("_confused",1)
                    ch_j "Um. . . no?"
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "I would rather we not discuss this, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "I'm gonna do. . . whatever."
                $ Girl.change_face("_bemused",1)
                $ counter = 1
            if not counter:
                $ Girl.add_word(1,0,0,"nofap")


        "You can do that if you need to." if "nofap" in Girl.traits:
            if "askedfap" not in Girl.daily_history:
                $ Girl.change_stat("love", 90, 1)
                $ Girl.change_stat("obedience", 90, 1)
                $ Girl.change_stat("inhibition", 90, 1)
            if not approval_check(Girl, 500, "I"):

                if "okfap" not in Girl.history:
                    $ Girl.change_stat("love", 60, 1)
                    $ Girl.change_stat("love", 90, 5)
                    $ Girl.change_stat("obedience", 60, 3)
                    $ Girl.change_stat("inhibition", 70, 5)
                    $ Girl.change_stat("lust", 90, 10)
                $ Girl.change_face("_confused",2)
                if Girl == RogueX:
                    ch_r "Right! Not that I ever do that anyway, of course. . ."
                elif Girl == KittyX:
                    ch_k "Oh? Um, thanks?"
                elif Girl == EmmaX:
                    ch_e "I'm glad that I have your permission. . ."
                elif Girl == LauraX:
                    ch_l "Good to know."
                elif Girl == JeanX:
                    ch_j "Well. . . good?"
                elif Girl == StormX:
                    ch_s "Oh?"
                    ch_s "Good."
                elif Girl == JubesX:
                    ch_v "Huh? Ok then. . ."
                $ Girl.change_face("_smile",1)
            elif approval_check(Girl, 750, "O"):

                if "okfap" not in Girl.history:
                    $ Girl.change_stat("love", 90, 20)
                    $ Girl.change_stat("obedience", 200, 5)
                    $ Girl.change_stat("obedience", 90, 10)
                    $ Girl.change_stat("inhibition", 90, 10)
                    $ Girl.change_stat("lust", 90, 10)
                $ Girl.change_face("_sly",1)
                Girl.voice "Yes,[Girl.player_petname]."
            else:

                if "okfap" not in Girl.history:
                    $ Girl.change_stat("love", 90, 5)
                    $ Girl.change_stat("obedience", 60, 3)
                    $ Girl.change_stat("inhibition", 70, 3)
                    $ Girl.change_stat("lust", 50, 5)
                $ Girl.change_face("_surprised",2)
                if Girl == RogueX:
                    ch_r "Great! I mean, that's cool."
                elif Girl == KittyX:
                    ch_k "Nice! I'll, um, yeah."
                elif Girl == EmmaX:
                    ch_e "Oh, what a relief. . ."
                elif Girl == LauraX:
                    ch_l "Finally."
                elif Girl == JeanX:
                    ch_j "Oh! That'll be nice. . ."
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "That would be fantastic, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Oh. . . oh! Nice!"
                $ Girl.change_face("_smile",1)
            $ Girl.drain_word("nofap",0,0,1)
            $ Girl.add_word(1,0,0,0,"okfap")
        "Nevermind":




            if not approval_check(Girl, 500, "I"):

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("love", 80, 10)
                    $ Girl.change_stat("inhibition", 50, 5)
                $ Girl.change_face("_bemused",1)
                if Girl == EmmaX:
                    ch_e "Back to more appropriate topics, I hope?"
                elif Girl == LauraX:
                    ch_l "Glad we're off this one. . ."
                elif Girl == JeanX:
                    $ Girl.change_face("_confused",1)
                    ch_j "Um. . .ok?"
                elif Girl == StormX:
                    ch_s ". . . Fine."
                else:
                    $ Girl.change_face("_surprised",2)
                    Girl.voice "Right! What were we even talking about?"
                    $ Girl.change_face("_smile",1)
            elif approval_check(Girl, 500, "O"):

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("obedience", 60, 5)
                    $ Girl.change_stat("inhibition", 80, 5)
                    $ Girl.change_stat("lust", 50, 5)
                $ Girl.change_face("_sly",1)
                if Girl in (EmmaX, StormX):
                    Girl.voice "Very Well. . ."
                else:
                    Girl.voice "Ok."
            elif not approval_check(Girl, 800):

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("love", 80, 5)
                    $ Girl.change_stat("obedience", 50, 5)
                $ Girl.change_face("_angry",2,Eyes="_side")
                if Girl == RogueX:
                    ch_r "Damned straight, \"never mind.\""
                elif Girl == EmmaX:
                    ch_e "I should hope so . . ."
                elif Girl == StormX:
                    ch_s "Of course."
                else:
                    Girl.voice "Damned right, \"never mind.\""
                $ Girl.change_face("_angry",1)
            else:

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_stat("inhibition", 50, 2)
                $ Girl.change_face("_sly",1)
                if Girl in (EmmaX,StormX):
                    Girl.voice "Very Well. . ."
                else:
                    Girl.voice "Ok."


    $ Girl.add_word(1,0,"askedfap",0,"askedfap")
    $ Taboo = TabStore
    return






label CalltoFap(Girl=0, Fap=0):



    if "nofap" not in Girl.traits:

        $ Girl.drain_word("wannafap",0,1)
        $ Girl.add_word(1,0,"gonnafap",0,0)
        return

    if Girl.location == bg_current:

        return


    $ EGirls.remove(EGirls[0])
    while EGirls:

        if "wannafap" in EGirls[0].daily_history and "nofap" not in EGirls[0].daily_history:

            $ EGirls[0].add_word(1,0,"gonnafap",0,0)
        $ EGirls.remove(EGirls[0])


    $ Player.daily_history.append("fapcall")


    show Cellphone at sprite_location(stage_left)

    "[Girl.name] calls you up. . ."
    if Girl == RogueX:
        ch_r "So. . . I was wondering. . ."
        ch_r "I know you didn't want me to. . . um. . . "
        ch_r "take care of my needs?"
        ch_r ". . ."
        ch_r ". . .but would you mind if I were to do that?"
        ch_r "Right now?"
    elif Girl == KittyX:
        ch_k "Hey, so[KittyX.like]I know you were all like. . ."
        ch_k "\"don't touch yourself, Kitty,\" and[KittyX.like],"
        ch_k "I know I agreed and all, but. . ."
        ch_k "Would you mind if[KittyX.like]maybe I did anyway?"
    elif Girl == EmmaX:
        ch_e "I'm aware that we had something of an arrangement going on. . ."
        ch_e "One relating to me. . . gratifying myself. . ."
        ch_e "or the lack thereof. . ."
        ch_e "And I was just curious, would you mind if we perhaps suspended that rule. . ."
        ch_e "Just for tonight, perhaps?"
    elif Girl == LauraX:
        ch_l "Hey, remember when you told me I couldn't schlick off?"
        ch_l "I want to schlick off."
        ch_l ". . ."
        ch_l "That cool? or. . ."
    elif Girl == JeanX:
        ch_j "Hey [JeanX.player_petname]. . ."
        ch_j "Remember how we agreed that I would hold off on. . ."
        ch_j ". . . on schlicking?"
        ch_j "Well I was just thinking. . ."
        ch_j "Maybe I could anyway?"
    elif Girl == StormX:
        ch_s "[StormX.player_petname]. . ."
        ch_s "I find myself in need of some. . . relief."
        ch_s "Would you mind if I were to satisfy myself?"
    elif Girl == JubesX:
        ch_v "Hey, remember how you told me I couldn't. . ."
        ch_v ". . . \"take care of my own needs?\""
        ch_v "Well. . . I have needs."
        ch_v "A whole lotta needs. . ."
        ch_v "So I was kinda hoping. . ."

    menu:
        "Sure, no problem.":
            $ Girl.change_stat("love", 90, 5)
            $ Girl.change_stat("love", 80, 5)
            $ Girl.change_stat("love", 200, 1)
            $ Girl.change_stat("obedience", 80, 2)
            $ Girl.change_stat("inhibition", 80, 3)
            $ Girl.change_stat("lust", 50, 5)
            if Girl == RogueX:
                ch_r "Thanks, I really appreciate that."
            elif Girl == KittyX:
                ch_k "Cool!"
            elif Girl == EmmaX:
                ch_e "Oh, thank you, [EmmaX.player_petname]."
            elif Girl == LauraX:
                ch_l "Nice."
            elif Girl == JeanX:
                ch_j "Whew!"
            elif Girl == StormX:
                ch_s ". . . Thank you, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "Nice. . ."
            $ Fap = 1
        "If you really have to. . .":
            if (Girl.love + Girl.obedience) >= 2*Girl.inhibition:

                $ Girl.change_stat("love", 80, 2)
                $ Girl.change_stat("obedience", 60, 3)
                $ Girl.change_stat("obedience", 80, 1)
                $ Girl.change_stat("lust", 80, 5)
                if Girl == RogueX:
                    ch_r "Oh, well. . ."
                    ch_r "I suppose I could restrain myself. . ."
                elif Girl == KittyX:
                    ch_k "Well, if it really bothers you. . ."
                elif Girl == EmmaX:
                    ch_e "I imagine I can find other distractions, [EmmaX.player_petname]."
                elif Girl == LauraX:
                    ch_l "Hmm. Yeah, whatever. Nevermind."
                elif Girl == JeanX:
                    ch_j "Well, I guess I could hold off. . ."
                    ch_j "I do have -exceptional- self control. . ."
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "I suppose I can contain myself, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Well, I mean. . ."
                    ch_v "I don't want to disappoint you. . ."
                $ Girl.Thirst += 10
            else:


                $ Girl.change_stat("love", 80, 3)
                $ Girl.change_stat("love", 200, 1)
                $ Girl.change_stat("obedience", 50, -4)
                $ Girl.change_stat("obedience", 90, -1)
                $ Girl.change_stat("inhibition", 50, 2)
                $ Girl.change_stat("inhibition", 80, 5)
                $ Girl.change_stat("lust", 50, 5)
                if Girl == RogueX:
                    ch_r "I would REALLY appreciate that."
                    ch_r "Thank you."
                elif Girl == KittyX:
                    ch_k "I kinda. . . yeah."
                elif Girl == EmmaX:
                    ch_e "It would really just take the edge off of a long day."
                elif Girl == LauraX:
                    ch_l "Yeah, I probably do."
                elif Girl == JeanX:
                    ch_j "K', thanks!"
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "That is appreciated, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Nice. . ."
                $ Fap = 1
        "No, you may not.":
            if approval_check(Girl,600,"O") and (Girl.obedience >= Girl.inhibition):

                $ Girl.change_stat("love", 50, -5)
                $ Girl.change_stat("obedience", 60, 5)
                $ Girl.change_stat("obedience", 200, 2)
                $ Girl.change_stat("lust", 80, 5)
                if approval_check(Girl,800,"O"):
                    $ Girl.change_stat("lust", 200, 5)
                if Girl == RogueX:
                    ch_r "Oh, well. . ."
                    ch_r "I suppose I could restrain myself. . ."
                elif Girl == KittyX:
                    ch_k "Well, if it really bothers you. . ."
                elif Girl == EmmaX:
                    ch_e "I imagine I can find other distractions, [EmmaX.player_petname]."
                elif Girl == LauraX:
                    ch_l "Hmm. Yeah, whatever. Nevermind."
                elif Girl == JeanX:
                    ch_j ". . ."
                    ch_j ". . . . . ."
                    ch_j "Ok."
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "Fine."
                elif Girl == JubesX:
                    ch_v "Well. . . Ok. . ."
                $ Girl.Thirst += 10
            elif approval_check(Girl,1000,"LO"):

                $ Girl.change_stat("love", 70, -5)
                $ Girl.change_stat("obedience", 50, -3)
                $ Girl.change_stat("obedience", 80, -2)
                $ Girl.change_stat("inhibition", 50, 3)
                $ Girl.change_stat("inhibition", 80, 2)
                $ Girl.change_stat("lust", 80, 5)
                if Girl == RogueX:
                    ch_r "Well, I mean, I kind of started. . ."
                elif Girl == KittyX:
                    ch_k "Um, sorry, but I[KittyX.like]have to?"
                elif Girl == EmmaX:
                    ch_e "I think I'll just have to do it anyway. . ."
                elif Girl == LauraX:
                    ch_l "Um, sure, I will -NOT- be doing just that. . ."
                elif Girl == JeanX:
                    ch_j "Well. . . as it turns out. . ."
                    ch_j "\"Ask for forgiveness,\" you know?"
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "I am afraid that I have my limits, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "I'm a little wired right now. . ."
                $ Girl.Thirst += 10
                $ Fap = 1
            else:

                $ Girl.change_stat("love", 70, -5)
                $ Girl.change_stat("love", 90, -5)
                $ Girl.change_stat("obedience", 80, -5)
                $ Girl.change_stat("inhibition", 50, 4)
                $ Girl.change_stat("inhibition", 80, 3)
                if Girl == RogueX:
                    ch_r "You know what? Screw it, and screw you!"
                elif Girl == KittyX:
                    ch_k "Well. . . I'm doing it anyway!"
                elif Girl == EmmaX:
                    ch_e "I think I can be the judge of that."
                elif Girl == LauraX:
                    ch_l "Sure, keep thinking I care."
                elif Girl == JeanX:
                    ch_j "Fine!"
                    ch_j "You can just imagine what I'm *not* doing right now."
                    $ Girl.change_face("_angry",Mouth="_smirk")
                    call PsychicFlash (0)
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "Well, that is unfortunate, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "I kinda need some release here though. . ."
                $ Girl.Thirst += 10
                $ Fap = 1
        "I could come over and take care of that. . .":
            $ Girl.change_stat("love", 80, 4)
            $ Girl.change_stat("love", 200, 1)
            $ Girl.change_stat("obedience", 80, 2)
            $ Girl.change_stat("inhibition", 80, 2)
            $ Girl.change_stat("lust", 80, 5)
            if Girl == EmmaX:
                ch_e "I think you could at that, [EmmaX.player_petname]."
            elif Girl == LauraX:
                ch_l "Cool."
            elif Girl == StormX:
                ch_s "I imagine that you could, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "That might be nice."
            else:
                Girl.voice "Oh, you would, would you. . ."
            $ Fap = 3
        "Only if I can watch." if AloneCheck():
            if approval_check(Girl, 1200):

                $ Girl.change_stat("love", 80, 4)
                $ Girl.change_stat("obedience", 60, 2)
                $ Girl.change_stat("obedience", 80, 2)
                $ Girl.change_stat("inhibition", 50, 2)
                $ Girl.change_stat("inhibition", 80, 3)
                $ Girl.change_stat("lust", 80, 5)
                if Girl == RogueX:
                    ch_r "Hmm. . . that sounds like fun. . ."
                elif Girl == KittyX:
                    ch_k "Heh, you looking for a show? . ."
                elif Girl == EmmaX:
                    ch_e "I think we could arrange that. . ."
                elif Girl == LauraX:
                    ch_l "Yeah, I could do that, gimme a sec. . ."
                elif Girl == JeanX:
                    ch_j "Ok, fair. . ."
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "I would not mind that, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Oh, well, I guess that'd be fine. . ."
                $ Fap = 2
            else:

                $ Girl.change_stat("love", 60, -3)
                $ Girl.change_stat("obedience", 60, -2)
                $ Girl.change_stat("inhibition", 80, 3)
                $ Girl.change_stat("lust", 50, 5)
                if Girl == RogueX:
                    ch_r "I, um, I don't know about that. . ."
                elif Girl == KittyX:
                    ch_k "Heh, heh, um, I don't think I could. . ."
                elif Girl == EmmaX:
                    ch_e "I'd rather avoid putting on a show like that. . ."
                elif Girl == LauraX:
                    ch_l "Nah, had enough of surveillance . . ."
                elif Girl == JeanX:
                    ch_j "Um, no?"
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "I am uncomfortable with that, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "I'd uh, prefer you didn't. . ."
                $ Girl.Thirst += 15

    $ Girl.drain_word("wannafap",0,1)
    hide Cellphone

    if Fap == 3:

        $ del Options[:]

        $ Girl.location = Girl.home
        $ bg_current = Girl.home
        call Taboo_Level (1)

        jump Misplaced

    elif Fap == 2:

        $ del Options[:]
        if Girl in (EmmaX,StormX) and Girl.location == "bg_classroom" and time_index >= 2:
            pass
        else:
            $ Girl.location = Girl.home
        call Taboo_Level (0)
        call PhoneSex (Girl)
        $ renpy.pop_call()
    elif Fap:

        $ Girl.add_word(1,0,"gonnafap",0,0)

    $ Options = ["empty"]
    return







label PhoneSex(Girl=0):


    if bg_current != "bg_player":
        "You rush back to your room."
        $ bg_current = "bg_player"
        call Taboo_Level
        call set_the_scene
    if Girl in (EmmaX,JeanX):

        call MindFuck

    $ Player.add_word(1,"phonesex","phonesex",0,"phonesex")


    call shift_focus (Girl)
    show PhoneSex zorder 150

    $ Girl.add_word(1,"phonesex","phonesex",0,"phonesex")
    $ primary_action = 1
    if Girl == RogueX:
        ch_r "Ok, I think that should get the video running, right?"
        call Rogue_M_Prep
        ch_r "Hmm, that was a satisfying phone call. . ."
        ch_r "I gotta go."
    elif Girl == KittyX:
        ch_k "Ok, that's got it up."
        ch_k "[KittyX.Like]how do I look?"
        call Kitty_M_Prep
        ch_k "Mmmmm. . . call any time, [KittyX.player_petname]."
        ch_k "[KittyX.Like]ANY time."
    elif Girl == EmmaX:
        ch_e "Now, set it up like so. . ."
        ch_e "There, you should have video up."
        call Emma_M_Prep
        ch_e "I do enjoy these little chats. . ."
        ch_e "I need to be going though."
    elif Girl == LauraX:
        ch_l "Ok, video up. . ."
        call Laura_M_Prep
        ch_l "That was fun. Call you later?"
    elif Girl == JeanX:
        ch_j "Ooookay. . . There, video on. . ."
        call Jean_M_Prep
        ch_j "Ok, later."
    elif Girl == StormX:
        ch_s ". . ."
        ch_s "I believe I've got the camera set up, [StormX.player_petname]. . ."
        call Storm_M_Prep
        ch_s "I enjoyed that, thank you. . ."
    elif Girl == JubesX:
        ch_v "Ok, loaded up. . ."
        ch_v "Looking good?"
        call Jubes_M_Prep
        ch_v "Mmmmm. . . call again, [JubesX.player_petname]."
        ch_v "I'll be waiting. . ."


    hide PhoneSex

    call Get_Dressed
    $ Girl.change_outfit(5)
    call checkout (1)
    $ Player.recent_history.remove("phonesex")
    return




label MindFuck_Screen:

    if bg_current in PersonalRooms:
        call RoomMask




















    elif bg_current == "bg_classroom":
        show bg_classmask onlayer black:
            alpha .2
    elif bg_current == "bg_dangerroom":
        show bg_danger onlayer black:
            alpha .2
    elif bg_current == "bg_showerroom":
        show bg_shower onlayer black:
            alpha .2
    elif bg_current == "bg_study":
        show bg_study onlayer black:
            alpha .2
    elif bg_current == "bg_movies":
        show bg_movies onlayer black:
            alpha .2
    elif bg_current == "bg_restaurant":
        show bg_rest onlayer black:
            alpha .2
    elif bg_current == "bg_pool":
        show bg_pool onlayer black:
            alpha .2
    else:
        show bg_campus onlayer black:
            alpha .2
    return

label PsychicFlash(Face="_sly", TempLoc=0):
    call MindFuck_Screen
    $ Line = Girl.location
    $ Girl.location = bg_current
    call set_the_scene (1, 0, 0, 0, 1)
    if Face:
        $ Girl.change_face(Face)
    $ Girl.ArmPose = 2
    $ Girl.top_pulled_up = 1
    $ Girl.upskirt = 1
    $ Girl.underwear_pulled_down = 1
    ". . . {w=0.3}{nw}"
    if Girl == EmmaX:
        hide Emma_Sprite with fade
    elif Girl == JeanX:
        hide Jean_Sprite with fade
    $ Girl.change_outfit(6,Changed=1)
    scene onlayer black
    $ Girl.ArmPose = 1
    $ Line = 0
    Girl.voice ". . ."


label MindFuck(TempLoc=0):

    if Girl == EmmaX:
        ch_e "Would you prefer to have some telepathic sex?"
    elif Girl == JeanX:
        ch_j "Wouldn't telepathic sex be more fun?"
    menu MindFuck_Menu:
        "Sure":
            if Girl == EmmaX:
                ch_e "Lovely. . ."
                ch_e "Just let me prepare us. . ."
            elif Girl == JeanX:
                ch_j "Great!"
                ch_j "Ok, looping you in. . ."

            call MindFuck_Screen
            $ TempLoc = Girl.location
            $ Girl.location = bg_current
            $ Girl.change_face("_sly")

            call set_the_scene (1, 0, 0, 0, 1)
            Girl.voice "There. . ."

            $ Player.add_word(1,"MindFuck","MindFuck",0,"MindFuck")
            call shift_focus(Girl)
            jump enter_main_sex_menu

            $ Girl.location = TempLoc
            if Girl == EmmaX:
                ch_e "That'll be all for now. . ."
                ch_e "I'll see you in your dreams. . ."
            elif Girl == JeanX:
                ch_j "Ok, that'll do it. . ."
                ch_j "Be thinking about me. . ."

            $ Girl.change_outfit(6,Changed=1)
            $ Girl.spunk = []
            if Girl == EmmaX:
                hide Emma_Sprite with fade
            elif Girl == JeanX:
                hide Jean_Sprite with fade
            scene onlayer black
            jump Misplaced
        "What is that?" if "mfuck?" not in Player.recent_history and "MindFuck" not in Player.history:
            if Girl == EmmaX:
                ch_e "Well, if you open your mind a bit, I could project into it."
                ch_e "Then we could have. . . all sorts of fun. . ."
            elif Girl == JeanX:
                ch_j "You know, like if you let your guards down a little. . ."
                ch_j "I could work my way in there and we could have some fun. . ."
            $ Player.add_word(1,"mfuck?")
            jump MindFuck_Menu
        "Nah, over the phone is fine.":
            if Girl == EmmaX:
                ch_e "Fine, be boring. . ."
            elif Girl == JeanX:
                ch_j "Lame. . ."
            return
    return



label Frisky_Class(Girl=0, Teacher=0, LineB=0, BO=[]):
    if Girl not in all_Girls:
        return
    $ Partner = 0
    $ Line = 0

    if len(Present) >= 2:
        $ Present[1].sprite_location = stage_left
        $ Present[1].eyes = "_side"
    $ Present[0].sprite_location = stage_right

    $ BO = active_Girls[:]

    while BO:

        if renpy.showing(BO[0].tag+"_Sprite"):
            if BO[0] == RogueX:
                show Rogue_sprite at sprite_location(RogueX.sprite_location,50):
                    ease .5 ypos 250
            elif BO[0] == KittyX:
                show Kitty_sprite at sprite_location(KittyX.sprite_location,50):
                    ease .5 ypos 250
            elif BO[0] == LauraX:
                show Laura_Sprite at sprite_location(LauraX.sprite_location,50):
                    ease .5 ypos 250
            elif BO[0] == JeanX:
                show Jean_Sprite at sprite_location(JeanX.sprite_location,50):
                    ease .5 ypos 250
            elif BO[0] == JubesX:
                show Jubes_Sprite at sprite_location(JubesX.sprite_location,50):
                    ease .5 ypos 250
        $ BO.remove(BO[0])

    call shift_focus (Girl)
    if EmmaX.location == "bg_teacher":
        "[EmmaX.name] is giving a lecture on mutant relations. Sitting next to you, you notice [Girl.name] shifting uncomfortably in her seat."
        $ Teacher = EmmaX
    elif StormX.location == "bg_teacher":
        "[StormX.name] is giving a lecture on geography and politics. Sitting next to you, you notice [Girl.name] shifting uncomfortably in her seat."
        $ Teacher = StormX
    else:
        "Professor McCoy is giving a lecture on the X-Gene. Sitting next to you, you notice [Girl.name] shifting uncomfortably in her seat."
    "Occasionally, you catch her glancing over your way."

    "[Girl.name] opens her notebook and begins scratching out a note."
    "She detaches the slip of paper from the binder, carefully folding it before sliding it in front of you."
    "She watches you as you unfold the note."
    if "friskyclass" in Girl.history:
        "It reads \"Did you want to fool around again? Y[[] N[[]\""
        menu:
            "Y":
                $ Girl.change_face("_sly",1)
                $ Girl.change_stat("love", 80, 3)
                $ Girl.change_stat("inhibition", 60, 3)
                "She smiles suggestively."
                $ D20 = renpy.random.randint(1, 15)
                jump Frisky_Class_Loop
            "N":
                $ Girl.change_stat("love", 80, -10)
                $ Girl.change_stat("love", 70, -5)
                $ Girl.change_stat("obedience", 70, 5)
                $ Girl.change_stat("inhibition", 60, -3)
                $ Line = "rejected"
                $ Girl.change_face("_angry")
                $ Girl.daily_history.append("_angry")
                jump Frisky_Class_End
    if Girl == RogueX:
        "In looping penstrokes, it reads: \"You like biology?\""
    elif Girl == KittyX:
        "In girly penstrokes, it reads: \"biology?\""
    elif Girl == LauraX:
        "In roughly formed penstrokes, it reads: \"Boring, right?\""
    elif Girl == JeanX:
        "In sloppy penstrokes, it reads: \"kinda dull\"."
    elif Girl == JubesX:
        "In flashy penstrokes, it reads: \"Totally boring?\""
    if Girl in (RogueX,KittyX):
        $ Girl.change_face("_smile",2)
        "You look back and see that she's blushing slightly."
        "She slides her pen over to you so you can reply."
        $ Girl.change_face("_smile",1)
    else:
        $ Girl.change_face("_sly",1)
        "You look back and see that she's staring at you suggestively."
        "She slides her pen over to you so you can reply."

    menu:
        "You reply. . ."
        "What are you talking about?":
            jump Frisky_Class_End
        "Naah. Not so much.":

            $ Girl.change_stat("love", 80, -3)
            $ Girl.change_stat("inhibition", 60, -3)
            $ Girl.change_face("_confused")
            jump Frisky_Class_End

        "It's my favorite subject." if Girl in (RogueX,KittyX):
            $ Girl.change_stat("love", 80, 5)
            $ Girl.change_face("_smile")
            "[Girl.name] reads your note and starts to smile. She quickly dashes off another note, sliding it in front of you again."
            "You unfold the note, trying not to let the teacher see you. \"Then maybe we could study together tonight?\"."
            $ Line = "continue"

        "Yeah, pretty lame." if Girl not in (RogueX,KittyX):
            $ Girl.change_stat("love", 80, 5)
            $ Girl.change_face("_smile")
            "[Girl.name] reads your note and starts to smile. She quickly dashes off another note, sliding it in front of you again."
            "You unfold the note, trying not to let the teacher see you. \"Then maybe we could 'study' together tonight?\"."
            $ Line = "continue"

        "I do when it's about you." if Girl in (RogueX,KittyX):
            $ Line = "her"

        "I was too busy thinking about you." if Girl not in (RogueX,KittyX):
            $ Line = "her"



    if Line == "her":
        if approval_check(Girl, 500, "I") or Girl.SEXP >= 30:
            $ Girl.change_face("_sly")
            "[Girl.name] reads your note and smiles at you suggestively."
            $ Line = "flirt"
        elif approval_check(Girl, 900):
            if Girl in (RogueX,KittyX):
                $ Girl.change_face("_confused",2)
                "[Girl.name] reads your note and blushes furiously, looking down at her notes."
            else:
                $ Girl.change_face("_sly",1)
                "[Girl.name] reads your note and gets a sly smile, looking down at her notes."
            $ Girl.change_face("_bemused",1)
            $ Line = "flirt"
        else:

            if Girl in (RogueX,KittyX):
                $ Girl.change_face("_perplexed",2)
                "[Girl.name] reads your note and blushes furiously. She quickly dashes off another note, sliding it in front of you again."
                "You unfold the note, trying not to let the teacher see you. \"I meant the class! Maybe we could study tonight?\"."
            else:
                $ Girl.change_face("_sly",1)
                "[Girl.name] reads your note and gets a sly smile. She quickly dashes off another note, sliding it in front of you again."
                "You unfold the note, trying not to let the teacher see you. \"I meant the class! Maybe we could 'study' tonight?\"."
            $ Girl.change_face("_bemused",1)
            $ Line = "continue"


    if Line == "continue":
        "She's trying to act like she's paying attention to the lecture, but she can't hide the big smile on her face."
        menu:
            "You respond. . ."
            "Maybe later.":
                $ Girl.change_stat("love", 80, -3)
                $ Girl.change_stat("obedience", 70, 5)
                $ Girl.change_stat("inhibition", 60, -3)
                $ Girl.change_face("_confused")
                $ Line = 0
                jump Frisky_Class_End
            "Naah. I've got better things to do.":
                $ Girl.change_stat("love", 80, -10)
                $ Girl.change_stat("love", 70, -5)
                $ Girl.change_stat("obedience", 70, 5)
                $ Girl.change_stat("inhibition", 60, -3)
                $ Line = "rejected"
                $ Girl.change_face("_angry")
                $ Girl.daily_history.append("_angry")
                jump Frisky_Class_End
            "Count on it.":
                $ Girl.change_face("_smile")
                "She smiles when she reads your reply, and throws you a wink."
                $ Girl.daily_history.append("studydate")
                "The rest of class is uneventful."
                return
            "We could get some \"studying\" done right now.":
                if approval_check(Girl, 1000):
                    $ Girl.change_face("_sly",1)
                    $ Girl.change_stat("love", 80, 3)
                    $ Girl.change_stat("inhibition", 60, 3)
                    "[Girl.name] gets a mischevious grin on her face and leans towards you."
                    $ Line = "flirt"
                elif approval_check(Girl, 700):
                    $ Girl.change_face("_smile",1)
                    $ Girl.change_stat("inhibition", 60, 2)
                    if Girl in (RogueX,KittyX):
                        "[Girl.name] blushes and smiles your way."
                    else:
                        "[Girl.name] startles a bit and smiles your way."
                    $ Line = "flirt"
                else:
                    $ Girl.change_face("_confused",1)
                    "[Girl.name] looks a bit surprised, then scowls at you."
                    jump Frisky_Class_End




    if Line == "flirt":
        $ Round -= 20
        $ D20 = renpy.random.randint(1, 15)
        $ Girl.change_face("_sly")
        "You notice one of [Girl.name]'s shoes slip from her foot beneath the desk. She tosses you a sly grin."
        if Girl.hose:
            "You feel the smooth texture of her stockinged foot begin to slowly slide back and forth along the length of your calf."
        else:
            "You feel the smooth skin of her bare foot begin to slowly slide back and forth along the length of your calf."

        while D20 <= 21 or "go on" in Player.recent_history:
            menu Frisky_Class_Loop:
                "Pull away from her.":
                    if Line == "fondle_pussy":
                        "You slowly slide your hand from her lap and start taking notes again."
                        $ Line = "tease"
                    elif Line == "fondle_breast":
                        "With a final squeeze, you move your hand back to the desktop."
                        $ Line = "tease"
                    elif Girl.session_orgasms and Girl.lust < 90:
                        "That'll probably do for now. . ."
                        $ Line = "tease"
                    else:
                        $ Line = "rejected"
                        $ Girl.change_stat("love", 200, -15)
                        $ Girl.change_stat("obedience", 70, 2)
                        $ Girl.change_stat("inhibition", 60, -2)
                    jump Frisky_Class_End

                "Look into her eyes and smile slightly." if Line == "flirt":
                    $ Girl.change_face("_smile")
                    $ Girl.change_stat("love", 200, 5)
                    "[Girl.name] smiles back."
                    "She looks back towards the front of the class, but her hand drifts across the top of the desk until she's holding yours."
                    $ Line = "handholding"
                    jump Frisky_Class_Loop
                "Grasp her hand gently, stroking the top of it." if Line == "handholding":
                    $ Girl.change_stat("love", 200, 5)
                    $ Girl.change_stat("lust", 50, 5)
                    $ Girl.change_face("_smile")
                    "[Girl.name] sighs contentedly and holds your hand for the remainder of class."
                    jump Frisky_Class_End


                "Try and slip your hand to her lap." if Line != "fondle_pussy":
                    $ Line = "fondle_pussy"
                    if approval_check(Girl, 1200) and Girl.action_counter["fondle_pussy"] and Girl.SEXP >= 40:
                        $ Girl.change_face("_sly")
                        $ Girl.change_stat("love", 90, 5)
                        $ Girl.change_stat("obedience", 70, 5)
                        $ Girl.change_stat("inhibition", 60, 5)
                        "[Girl.name] gets a mischievous grin and places her hand on your arm."
                    elif approval_check(Girl, 1400) and Girl.action_counter["fondle_pussy"]:
                        $ Girl.change_face("_smile")
                        $ Girl.change_stat("love", 80, 3)
                        $ Girl.change_stat("obedience", 70, 7)
                        $ Girl.change_stat("inhibition", 60, 3)
                        "[Girl.name] starts slightly as your hand travels up her thigh, but then she lets out a slight grin."
                    elif approval_check(Girl, 1500):
                        $ Girl.change_face("_perplexed",2)
                        $ Girl.change_stat("obedience", 70, 10)
                        $ Girl.change_stat("inhibition", 60, 3)
                        "[Girl.name] glances at you in alarm, but then slowly calms down."
                        $ Girl.change_face("_smile",1)
                        $ D20 += 2
                    else:
                        $ Line = "too far"

                    if Line == "fondle_pussy":
                        $ Girl.change_face("_sly")
                        $ Girl.change_stat("lust", 94, 5)
                        if Girl.PantsNum() == 5:
                            "[Girl.name]'s sly smile turns sultry as she feels your fingers sneak under the hem of her skirt, slowly tracing the soft contours of her mound."
                        elif Girl.PantsNum() >= 7:
                            "[Girl.name]'s sly smile turns sultry as she feels your fingers sneak down her pants, slowly tracing the soft contours of her mound."
                        else:
                            "[Girl.name]'s sly smile turns sultry as she feels your fingers sneak between her legs, slowly tracing the soft contours of her mound."

                        $ Girl.change_stat("lust", 94, 5)
                        if Girl.underwear == "_shorts":
                            "You think her shorts are becoming damp as you stroke the thin material. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                        elif Girl.underwear:
                            "You think her panties are becoming damp as you stroke the thin material. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                        elif Girl.pubes:
                            "You feel her soft fur moisten as you stroke the soft flesh below. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                        else:
                            "You feel her lips moisten as you stroke the soft flesh. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                        $ primary_action = "fondle_pussy"
                        $ D20 += 5

                "Keep fondling her pussy." if Line == "fondle_pussy":
                    $ Girl.change_stat("obedience", 70, 5)
                    $ Girl.change_stat("inhibition", 60, 3)
                    $ Girl.change_stat("lust", 89, 5)
                    $ Girl.change_stat("lust", 94, 5)
                    $ LineB = renpy.random.choice(["As the class drones on, you continue to slowly massage her warm delta.",
                                        "As the class continues, you continue to slowly massage her moist pussy.",
                                        "As the lecture drones on, you continue to slowly stroke her clit.",
                                        "As the class continues, you continue to slowly caress her labia."])
                    "[LineB]"

                    $ D20 += 5


                "Start fondling her tits." if Line != "fondle_breasts":
                    $ Line = "fondle_breasts"
                    if approval_check(Girl, 1100) and Girl.action_counter["fondle_breasts"]and Girl.SEXP >= 40:
                        $ Girl.change_stat("love", 80, 5)
                        $ Girl.change_stat("obedience", 70, 5)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.change_face("_sly")
                        "[Girl.name] closes her eyes and caresses your arm."
                    elif approval_check(Girl, 1300) and Girl.action_counter["fondle_breasts"]:
                        $ Girl.change_stat("love", 80, 3)
                        $ Girl.change_stat("obedience", 70, 7)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.change_face("_smile",1)
                        "[Girl.name] flinches as your hand travels up her ribcage, but she grins as you reach her breast."
                    elif approval_check(Girl, 1400):
                        $ Girl.change_stat("obedience", 70, 10)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.change_face("_perplexed",2)
                        "[Girl.name] glances at you in alarm, but then slowly calms down."
                        $ Girl.change_face("_smile",2)
                        $ D20 += 5
                    else:
                        $ Line = "too far"

                    if Line == "fondle_breasts":
                        $ Girl.change_face("_sly")
                        $ Girl.change_stat("lust", 94, 5)
                        "[Girl.name]'s sly eyes spakle as your hand cups her breast, giving it a casual caress."
                        "her nipples begin to firm up and she lets out a small moan of pleasure."
                        $ D20 += 7
                        $ primary_action = "fondle_breasts"
                "Keep fondling her tits." if Line == "fondle_breasts":
                    $ Girl.change_stat("obedience", 70, 5)
                    $ Girl.change_stat("inhibition", 60, 2)
                    $ Girl.change_stat("lust", 95, 3)
                    "Barely paying attention to the lecture, you continue to pulse her breast in your palm."
                    $ D20 += 7


                "Try and pull her hand toward your lap." if not offhand_action and Player.semen:
                    if "handjob" in Girl.recent_history:
                        "[Girl.name] grins and her hand grasps your cock again."
                    elif approval_check(Girl, 1200) and Girl.action_counter["handjob"] and Girl.SEXP >= 40:
                        $ Girl.change_face("_sly")
                        $ Girl.change_stat("love", 90, 5)
                        $ Girl.change_stat("obedience", 70, 5)
                        $ Girl.change_stat("inhibition", 60, 5)
                        "[Girl.name] gets a mischievous grin and her hand starts to caress your crotch."
                    elif approval_check(Girl, 1400) and Girl.action_counter["fondle_pussy"]:
                        $ Girl.change_face("_smile")
                        $ Girl.change_stat("love", 80, 3)
                        $ Girl.change_stat("obedience", 70, 7)
                        $ Girl.change_stat("inhibition", 60, 3)
                        "[Girl.name] starts slightly as your move her hand up your thigh, but then she lets out a slight grin."
                    elif approval_check(Girl, 1500):
                        $ Girl.change_face("_perplexed",2)
                        $ Girl.change_stat("obedience", 70, 10)
                        $ Girl.change_stat("inhibition", 60, 3)
                        "[Girl.name] glances at you in alarm, but then slowly calms down."
                        $ Girl.change_face("_smile",1)
                        $ D20 += 2
                    else:
                        $ Line = "too far"

                    if Line != "too far":

                        $ Girl.change_face("_sly")
                        $ Girl.change_stat("lust", 94, 5)
                        if "cockout" not in Player.recent_history:
                            "[Girl.name]'s hand slowly unzips your pants and pulls your cock free."
                            $ Player.add_word(1,"cockout")
                            call Seen_First_Peen (Girl, Partner)
                            $ Girl.change_stat("lust", 94, 5)
                        $ offhand_action = "handjob"
                        $ Girl.recent_history.append("handjob")
                        $ Girl.daily_history.append("handjob")
                        "She begins to gently stroke it. . ."
                        if "handjob" not in Girl.recent_history:
                            $ Girl.action_counter["handjob"] += 1
                        $ D20 += 5


                "Stop her handjob." if offhand_action:
                    "You put a hand on her wrist and nudge her hand away."
                    if approval_check(Girl, 1800) or approval_check(Girl, 700, "O") or (Girl.love+Girl.obedience) >= (2*Girl.inhibition):

                        $ Girl.change_face("_sad")
                        $ Girl.change_stat("love", 90, -1)
                        $ Girl.change_stat("obedience", 60, 2)
                        $ Girl.change_stat("obedience", 80, 3)
                        "[Girl.name] allows her hand to be pulled away and goes back to what she'd been doing with it."
                        $ Girl.change_face("_sly")
                        $ offhand_action = 0
                    else:
                        $ Girl.change_face("_angry")
                        $ Girl.change_stat("love", 80, -3)
                        $ Girl.change_stat("love", 90, -1)
                        $ Girl.change_stat("obedience", 70, -2)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.change_stat("inhibition", 80, 2)
                        "[Girl.name] grasps your cock tightly, then continues to stroke it when you let go."
                        $ Girl.change_face("_sly")
                        $ D20 += 2





            if not offhand_action and Player.semen and "stophand" not in Girl.recent_history:
                if approval_check(Girl, 1200) and approval_check(Girl, 400, "I") and Girl.action_counter["handjob"] and Girl.SEXP >= 40:
                    $ Girl.change_face("_sly")
                    "[Girl.name] gets a mischievous grin and her hand starts to caress your crotch."
                    menu:
                        "What do you do?"
                        "Let her":
                            "You smile and nod a little."
                            $ Girl.change_face("_sly")
                            $ Girl.change_stat("love", 80, 1)
                            $ Girl.change_stat("inhibition", 70, 3)
                            $ Girl.change_stat("inhibition", 90, 2)
                            $ Girl.change_stat("lust", 94, 5)
                            if "cockout" not in Player.recent_history:
                                "[Girl.name]'s hand slowly unzips your pants and pulls your cock free."
                                $ Player.add_word(1,"cockout")
                                call Seen_First_Peen (Girl, Partner)
                                $ Girl.change_stat("lust", 94, 5)
                            $ offhand_action = "handjob"
                            $ Girl.recent_history.append("handjob")
                            $ Girl.daily_history.append("handjob")
                            "She begins to gently stroke it. . ."
                            if "handjob" not in Girl.recent_history:
                                $ Girl.action_counter["handjob"] += 1
                            $ D20 += 10
                        "Stop her":
                            "You put a hand on her wrist and nudge her hand away."
                            $ Girl.recent_history.append("stophand")
                            if approval_check(Girl, 1800) or approval_check(Girl, 700, "O") or (Girl.love+Girl.obedience) >= (2*Girl.inhibition):

                                $ Girl.change_face("_sad")
                                $ Girl.change_stat("love", 90, -1)
                                $ Girl.change_stat("obedience", 60, 2)
                                $ Girl.change_stat("obedience", 80, 3)
                                "[Girl.name] allows her hand to be pulled away and goes back to what she'd been doing with it."
                                $ Girl.change_face("_sly")
                                $ offhand_action = 0
                            else:
                                $ Girl.change_face("_angry")
                                $ Girl.change_stat("love", 80, -3)
                                $ Girl.change_stat("love", 90, -1)
                                $ Girl.change_stat("obedience", 70, -2)
                                $ Girl.change_stat("inhibition", 60, 3)
                                $ Girl.change_stat("inhibition", 80, 2)
                                "[Girl.name] stops, but looks really annoyed."
                                $ D20 += 10


            if offhand_action:

                "[Girl.name]'s hand continues to caress your cock. . ."
                $ Player.focus += 15 if Player.focus < 60 else 10
                if Player.focus >= 100:

                    "As you start to reach your limits, [Girl.name] places a hand over your cock."
                    "You jiz all over her hand."
                    $ Player.semen -= 1
                    if (Girl.action_counter["blowjob"] and approval_check(Girl, 1200)) or Girl == JubesX:
                        "She quickly licks it all up."
                        $ Girl.addiction -= 20
                        $ Girl.event_counter["swallowed"] += 1
                        $ Girl.recent_history.append("swallow")
                        $ Girl.daily_history.append("swallow")
                    else:
                        "She quickly wipes her hand off under the desk."
                    $ Girl.change_stat("lust", 200, 5)
                    $ D20 += 10
                    if not Player.semen:
                        "She continues to lightly stroke you, but you don't seem up to it for now. . ."
                        $ offhand_action = 0
                $ D20 += 5



            if Girl.lust >= 95:
                $ LineB = Line
                call Girl_Cumming (Girl, 1)
                $ Line = LineB
                $ LineB = renpy.random.choice([Girl.name+" collapses over her desk.",
                                    Girl.name+" mumbles something unintelligible.",
                                    Girl.name+" bites her lip as she struggles to stay upright.",
                                    Girl.name+" seems a bit flushed."])
                "[LineB]"
                $ D20 += 15



            $ Round -= 7
            if Round <= 15:
                "Unfortunately it seems like class is wrapping up. You'll have to save this for later. . ."
                $ Line = "tease"
                jump Frisky_Class_End
            if Line == "too far":

                $ Girl.change_face("_surprised",2)
                $ Girl.change_stat("love", 80, -5)
                $ Girl.change_stat("obedience", 70, 7)
                $ Girl.change_stat("inhibition", 50, -3)
                "[Girl.name] sits up straight in her seat and makes a little yelping noise."
                $ Girl.change_face("_angry",1)
                "Between that and the icy glare she shoots you, it's enough to draw the attention of your fellow students in your direction."
                $ D20 += 20
                if "go on" in Player.recent_history:
                    jump Frisky_Class_End
                    $ Line = "caught"
            else:
                if len(Present) >= 2 and D20 >= 15:

                    if Partner:

                        $ Partner.GirlLikeUp(Girl,2)
                        $ Girl.GirlLikeUp(Partner,2)
                        $ Partner.change_stat("lust", 95, 3)
                        $ LineB = renpy.random.choice([0,
                                            0,
                                            0,
                                            Partner.name+" seems into it. . .",
                                            Partner.name+"'s hand moves a bit faster.",
                                            Partner.name+" bites her lip as her hand continues to move.",
                                            Partner.name+"'s hand slows down a bit."])
                        if LineB:
                            "[LineB]"
                        if Partner.lust >= 95:
                            $ LineB = Line
                            call Girl_Cumming (Partner, 1)
                            $ Line = LineB
                            $ LineB = renpy.random.choice([Partner.name+" collapses over her desk.",
                                                    Partner.name+" mumbles something unintelligible.",
                                                    Partner.name+" bites her lip as she struggles to stay upright.",
                                                    Partner.name+" seems a bit flushed."])
                            "[LineB]"
                            $ D20 += 15

                    elif "saw with "+ Girl.tag in Present[1].traits:
                        Present[1].voice "Well!"
                        $ Present[1].GirlLikeUp(Girl,-4)
                        $ Girl.GirlLikeUp(Present[1],-2)
                        call Remove_Girl (Present[1])
                    elif approval_check(Present[1], 1500) and Present[1].GirlLikeCheck(Girl) >= 600:

                        $ Present[1].eyes = "leftside"
                        "[Present[1].name] seems to notice what you and [Girl.name] are doing."
                        $ Present[1].change_face("_sly",1)
                        "She seems to be kinda into it. . ."
                        if approval_check(Present[1], 800, "I") or "exhibitionist" in Present[1].traits:
                            $ Girl.change_stat("inhibition", 90, 3)
                            $ Present[1].GirlLikeUp(Girl,3)
                            $ Girl.GirlLikeUp(Present[1],5)
                            $ Present[1].change_stat("lust", 89, 7)
                            "You notice that [Present[1].name]'s begun feeling herself up as well."
                            $ Present[1].add_word(1,"frisky","frisky",0,0)
                            $ Partner = Present[1]
                    else:


                        $ Present[1].eyes = "leftside"
                        "[Present[1].name] seems to notice what you and [Girl.name] are doing."
                        $ Present[1].add_word(1,0,0,"saw with " + Girl.tag)
                        $ Present[1].change_face("_angry",1)
                        if Present[1] == RogueX:
                            ch_r "How dare you! Hussy."
                        elif Present[1] == KittyX:
                            ch_k "Hey! . . . HEY!"
                        elif Present[1] == LauraX:
                            ch_l "Cool off, you two."
                        elif Present[1] == JeanX:
                            ch_j "Hey, cut it out."
                        $ Present[1].GirlLikeUp(Girl,-2)
                        $ Girl.GirlLikeUp(Present[1],-3)
                        $ D20 += 15
                        if "go on" in Player.recent_history:
                            $ Line = "caught"
                            jump Frisky_Class_End


                if Teacher and "frisky" in Teacher.recent_history:

                    $ Teacher.GirlLikeUp(Girl,2)
                    $ Girl.GirlLikeUp(Teacher,2)
                    $ Teacher.change_stat("lust", 95, 3)
                    $ LineB = renpy.random.choice([0,
                                    0,
                                    0,
                                    Teacher.name+" stumbles a bit over the delivery of the next portion of her lecture.",
                                    Teacher.name+"'s hand moves a bit faster.",
                                    Teacher.name+" bites her lip as her hand continues to move.",
                                    Teacher.name+"'s hand slows down a bit."])
                    if LineB:
                        "[LineB]"
                    if Teacherlust >= 95:
                        $ LineB = Line
                        call Girl_Cumming (Teacher, 1)
                        $ Line = LineB
                        $ LineB = renpy.random.choice([Teacher.name+" stumbles a bit over the delivery of the next portion of her lecture.",
                                            Teacher.name+" mumbles something unintelligible but continues the lecture.",
                                            Teacher.name+" bites her lip as she struggles to continue talking.",
                                            Teacher.name+" seems a bit under the weather.",
                                            Teacher.name+" seems a bit flushed."])
                        "[LineB]"
                        $ D20 += 15

                if D20 > 30:

                    if D20 >= 50:
                        $ LineB = renpy.random.choice([0,
                                        0,
                                        0,
                                        "The class isn't paying attention to the lecture anymore.",
                                        "The class definitely seems into the show she's putting on.",
                                        "The class is hooting and hollering.",
                                        "The students seem to be watching you intently."])
                    else:
                        $ LineB = renpy.random.choice([0,
                                        0,
                                        0,
                                        "The class seems a little confused as to what she's talking about.",
                                        "The class seems a little confused as to what she's doing back there.",
                                        "The class is shifting strange looks your way.",
                                        "A bunch of students seem to be watching you intently."])
                    if LineB:
                        "[LineB]"



        if "exhibitionist" not in Girl.traits and not approval_check(Girl, 700,"I"):

            $ Line = "too far"
        if Line not in ("rejected", "handholding", "tease"):
            $ Girl.change_face("_surprised")
            if Teacher:
                $ Teacher.change_face("_surprised",1)
                "[Teacher.name] stops her lecture in mid-sentence when she notices what you and [Girl.name] are up to."
                if approval_check(Teacher, 1500) and Teacher.GirlLikeCheck(Girl) >= 600:

                    $ Teacher.change_face("_sly",1)
                    if Line == "too far":

                        $ Girl.mouth = "_sad"
                        if Teacher == EmmaX:
                            "She looks over at you and shrugs as she continues her lecture, but the moment has past."
                        elif Teacher == StormX:
                            "She looks over at you and smiles consolingly as she continues her lecture, but the moment has past."
                        jump Frisky_Class_End
                    "She gets a sly smile on her face and continues her lecture."
                    $ Girl.change_face("_sly",1)
                    if approval_check(Teacher, 800, "I") or "exhibitionist" in Teacher.traits:
                        $ Teacher.change_stat("inhibition", 90, 3)
                        $ Teacher.GirlLikeUp(Girl,3)
                        $ Girl.GirlLikeUp(Teacher,5)
                        $ Teacher.change_stat("lust", 89, 7)
                        "You notice that [Teacher.name]'s hand has snaked down beneath the podium and begun to move."
                        $ Teacher.add_word(1,"frisky","frisky",0,0)
                        $ Player.add_word(1,"go on","go on",0,0)
                    "[Girl.name] looks around and shrugs. . ."
                    jump Frisky_Class_Loop
                else:
                    $ Teacher.change_face("_angry",1)
                    $ Girl.mouth = "_sad"
                    if Teacher == EmmaX:
                        ch_e "[EmmaX.player_petname], [Girl.tag], if you could perhaps pay more attention to the lecture, and less to each other's bodies?"
                        ch_e "Perhaps it would be best if you visited the headmaster's office and cool off?"
                    elif Teacher == StormX:
                        ch_s "[StormX.player_petname], [Girl.tag], I can appreciate your enthusaism, but perhaps not on my time?"
                        ch_s "I think perhaps you should visit Charles and cool off?"
            else:
                "Dr. McCoy stops his lecture in mid-sentence when he notices that the whole class is looking at you and [Girl.name]."
                ch_b "Oh, my stars and garters!"
                ch_b "[Player.name]!?! {b}WHAT ARE YOU DOING? BOTH OF YOU, TO THE PROFESSOR'S OFFICE, IMMEDIATELY!{/b}"
            $ Girl.add_word(1,0,0,0,"friskyclass")
            $ Line = 0
            $ Girl.change_stat("love", 80, -10)
            $ Girl.change_stat("obedience", 70, -5)
            $ Girl.change_stat("inhibition", 50, -10)
            $ primary_action = 0
            if Girl not in Rules:
                call Girls_Caught (Girl)
            else:
                "Since Xavier isn't concerned with your activities, you both head back to your room instead."
                $ Girl.location = "bg_player"
                call clear_the_room (Girl, 0, 1)
                jump player_room



label Frisky_Class_End:
    $ primary_action = 0
    $ Partner = 0
    if Teacher:
        $ Teacher.drain_word("frisky",1,0)
    if not Line:

        $ Girl.change_face("_confused")
        "She unfolds the note and quickly reads it over."
        $ Girl.change_face("_sad")
        "As she does, you immediately see disappointment come over her features."
        "She scratches out a reply and slides it back in front of you."
        "When you open it up, it reads: {i}Never mind.{/i}"
    elif Line == "tease":

        if Girl.lust >= 80:
            $ Girl.change_face("_surprised",2)
            "[Girl.name] startles briefly."
            $ Girl.change_face("_sad",2)
            "[Girl.name] she looks over at you a bit upset that you ended things so abruptly."
        $ Girl.add_word(1,0,0,0,"friskyclass")
        $ Girl.change_face("_sly",1)
        "[Girl.name] takes in a deep breath and exhales it in a sigh, leaning in to whisper."
        if Girl == RogueX:
            ch_r "Tonight's \"study session\" just got a whole lot more interesting."
        elif Girl == KittyX:
            ch_k "I think we'll have[KittyX.like]a -lot- more fun tonight. . ."
        elif Girl == LauraX:
            ch_l "Tonight we can. . . finish this."
        elif Girl == JeanX:
            ch_j "I guess it can wait until later. . ."
        elif Girl == JubesX:
            ch_v "I'm looking forward to picking this up later. . ."
    elif Line == "rejected":

        if Girl in (RogueX,KittyX):
            $ Girl.change_face("_sadside")
            "[Girl.name] looks surprised and hurt. For the rest of the class, she says nothing."
        else:
            $ Girl.change_face("_angry")
            "[Girl.name] looks surprised and hurt. For the rest of the class, she stares daggers at you."
        "It seems like she has a hard time looking you in the eye."
    elif Line == "caught":
        "You quickly separate and go back to trying to study. . ."

    "Eventually, [Girl.name] seems to settle down and pay attention to the course material. You manage to do the same without falling asleep."
    $ Line = 0
    return




label Rogue_First_Topless(Silent=0, TempLine=0):
    if RogueX.ChestNum() > 1 or RogueX.OverNum() > 2:

        return
    if RogueX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ RogueX.recent_history.append("topless")
    $ RogueX.daily_history.append("topless")
    $ RogueX.drain_word("no_topless")
    $ RogueX.SeenChest += 1
    if RogueX.SeenChest > 1:
        return

    $ RogueX.change_stat("inhibition", 70, 20)
    if not Silent:
        $ RogueX.change_face("_bemused", 1)
        "[RogueX.name] looks a bit shy, and slowly lowers her hands from her chest."
        ch_r "Well, [RogueX.player_petname]? Like what you see?"
        menu Rogue_First_TMenu:
            extend ""
            "Nod":
                $ RogueX.change_stat("love", 90, 20)
                $ RogueX.change_stat("inhibition", 70, 20)
                $ RogueX.change_face("_smile")
                ch_r ". . ."
                $ RogueX.change_stat("love", 40, 20)
            "Whatever.":
                $ RogueX.change_stat("love", 90, -30)
                $ RogueX.change_stat("obedience", 50, 20)
                $ RogueX.change_stat("inhibition", 70, -10)
                $ RogueX.change_face("_angry")
                ch_r "Hmph!"
                $ RogueX.change_stat("obedience", 70, 20)
            "Well, they aren't that bad. . .":
                $ RogueX.change_stat("love", 90, -30)
                $ RogueX.change_stat("obedience", 60, 25)
                $ RogueX.change_stat("inhibition", 70, -15)
                $ RogueX.change_face("_confused",2)
                ch_r "Say what now?"
                menu:
                    "I, um, no, they're great!":
                        $ RogueX.change_face("_angry",2, Mouth="_smile")
                        $ RogueX.change_stat("inhibition", 70, 10)
                        ch_r "Of couse they are!"
                    "[EmmaX.name]'s were bigger, that's all." if EmmaX.SeenChest:
                        $ TempLine = EmmaX
                    "[StormX.name]'s were bigger, that's all." if StormX.SeenChest:
                        $ TempLine = StormX
                    "[KittyX.name]'s were tighter, that's all." if KittyX.SeenChest:
                        $ TempLine = KittyX

                if TempLine:
                    $ RogueX.change_face("_angry")
                    $ RogueX.mouth = "_surprised"
                    $ RogueX.change_stat("love", 90, -10)
                    $ RogueX.change_stat("obedience", 80, 30)
                    $ RogueX.change_stat("inhibition", 70, -25)
                    ch_r ". . ."
                    $ RogueX.mouth = "_sad"
                    if TempLine in (EmmaX,StormX):
                        if RogueX.GirlLikeCheck(TempLine) >= 800:
                            $ RogueX.change_face("_sly",2,Eyes="_side")
                            $ RogueX.change_stat("obedience", 80, 5)
                            ch_r "Well, I mean they would be quite the handful. . ."
                            $ RogueX.GirlLikeUp(TempLine,20)
                        elif RogueX.GirlLikeCheck(TempLine) >= 700:
                            $ RogueX.eyes = "_side"
                            $ RogueX.change_stat("obedience", 80, 5)
                            ch_r "I mean, I guess, if you like that kind of thing. . ."
                        else:
                            $ RogueX.GirlLikeUp(TempLine,-50)
                            $ TempLine = "bad"
                    elif TempLine == KittyX:
                        if RogueX.LikeKitty >= 800:
                            $ RogueX.change_face("_sly",2,Eyes="_side")
                            $ RogueX.change_stat("obedience", 80, 5)
                            ch_r "They are kind of adorable. . ."
                            $ RogueX.LikeKitty += 20
                        elif RogueX.LikeKitty >= 700:
                            $ RogueX.eyes = "_side"
                            $ RogueX.change_stat("obedience", 80, 5)
                            ch_r "I mean, yeah, I guess. . ."
                        else:
                            $ RogueX.LikeKitty -= 50
                            $ TempLine = "bad"

                    if TempLine == "bad":
                        $ RogueX.change_stat("love", 90, -20)
                        ch_r "Yeah, that's enough outta you, [RogueX.player_petname]."
                        $ RogueX.change_outfit()
                        $ RogueX.recent_history.append("no_topless")
                        $ RogueX.daily_history.append("no_topless")
                        $ RogueX.recent_history.append("_angry")
                        $ RogueX.daily_history.append("_angry")
    else:
        $ RogueX.add_word(1,0, "", "", "topless")
        if approval_check(RogueX, 800) and not RogueX.Forced:
            $ RogueX.change_stat("inhibition", 70, 5)
            $ RogueX.change_stat("obedience", 70, 5)
        else:
            $ RogueX.change_stat("love", 90, -5)
            $ RogueX.change_stat("inhibition", 70, -5)
            $ RogueX.change_face("_angry")
            $ RogueX.change_stat("obedience", 70, 15)
    return


label Rogue_First_Bottomless(Silent=0):
    if RogueX.PantiesNum() > 1 or RogueX.PantsNum() > 2 or RogueX.HoseNum() > 9:

        return
    if RogueX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ RogueX.recent_history.append("bottomless")
    $ RogueX.daily_history.append("bottomless")
    $ RogueX.drain_word("no_bottomless")
    $ RogueX.SeenPussy += 1
    if RogueX.SeenPussy > 1:

        return

    $ RogueX.change_stat("inhibition", 80, 40)
    if not Silent:
        $ RogueX.change_face("_bemused", 1)
        "[RogueX.name] shyly moves her hands aside, revealing her pussy."
        menu Rogue_First_BMenu:
            ch_r "Well, [RogueX.player_petname]? Was it worth the wait?"
            "Lovely. . .":
                $ RogueX.change_stat("love", 90, 20)
                $ RogueX.change_stat("inhibition", 60, 30)
                $ RogueX.change_face("_smile")
                ch_r ". . ."
                $ RogueX.change_stat("love", 40, 20)
            "I suppose.":
                $ RogueX.change_stat("love", 90, -30)
                $ RogueX.change_stat("obedience", 50, 20)
                $ RogueX.change_stat("inhibition", 70, -20)
                $ RogueX.change_face("_angry")
                ch_r ". . ."
                $ RogueX.change_stat("obedience", 70, 30)
    else:
        $ RogueX.add_word(1,0, "", "", "bottomless")
        if approval_check(RogueX, 500):
            $ RogueX.change_stat("inhibition", 60, 30)
        else:
            $ RogueX.change_stat("love", 90, -5)
            $ RogueX.change_stat("inhibition", 70, -5)
            $ RogueX.change_face("_angry")
            $ RogueX.change_stat("obedience", 70, 15)
    return


label Kitty_First_Topless(Silent=0, TempLine=0):
    if KittyX.ChestNum() > 1 or KittyX.OverNum() > 2:

        return
    if KittyX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ KittyX.recent_history.append("topless")
    $ KittyX.daily_history.append("topless")
    $ KittyX.drain_word("no_topless")
    $ KittyX.SeenChest += 1
    if KittyX.SeenChest > 1:
        return


    $ KittyX.change_stat("inhibition", 70, 15)
    if not Silent:
        $ KittyX.change_face("_bemused", 2)
        "Kitty looks a bit shy, and slowly lowers her hands from her chest."
        ch_k "[KittyX.Like]what do you think?"
        $ KittyX.blushing = "_blush1"
        menu Kitty_First_TMenu:
            extend ""
            "Lovely.":
                $ KittyX.change_stat("love", 90, 20)
                $ KittyX.change_stat("inhibition", 70, 20)
                $ KittyX.change_face("_smile",2)
                ch_k ". . ."
                $ KittyX.change_stat("love", 40, 20)
                $ KittyX.blushing = "_blush1"
            "That's it?":

                $ KittyX.change_stat("love", 90, -30)
                $ KittyX.change_stat("obedience", 60, 25)
                $ KittyX.change_stat("inhibition", 70, -15)
                $ KittyX.change_face("_confused",2)
                ch_k "What?"
                menu:
                    "I, um, no, they're great!":
                        $ KittyX.change_face("_angry",2, Mouth="_smile")
                        $ KittyX.change_stat("inhibition", 70, 10)
                        ch_k "Obviously!"
                    "[EmmaX.name]'s were bigger, that's all." if EmmaX.SeenChest:
                        $ TempLine = EmmaX
                    "[RogueX.name]'s were bigger, that's all." if RogueX.SeenChest:
                        $ TempLine = RogueX
                    "[LauraX.name]'s were bigger, that's all." if LauraX.SeenChest:
                        $ TempLine = LauraX
                    "[JeanX.name]'s were bigger, that's all." if JeanX.SeenChest:
                        $ TempLine = JeanX
                    "[StormX.name]'s were bigger, that's all." if StormX.SeenChest:
                        $ TempLine = StormX

                if TempLine:
                    $ KittyX.change_face("_angry")
                    $ KittyX.mouth = "_surprised"
                    $ KittyX.change_stat("love", 90, -10)
                    $ KittyX.change_stat("obedience", 80, 30)
                    $ KittyX.change_stat("inhibition", 70, -25)
                    ch_k ". . ."
                    $ KittyX.mouth = "_sad"
                    if TempLine in (EmmaX,StormX):
                        if KittyX.GirlLikeCheck(TempLine) >= 800:
                            $ KittyX.change_face("_sly",2,Eyes="_side")
                            $ KittyX.change_stat("obedience", 80, 5)
                            ch_k "Yeah, like you just wanna shove your head into there. . ."
                            $ KittyX.GirlLikeUp(TempLine,20)
                        elif KittyX.GirlLikeCheck(TempLine) >= 700:
                            $ KittyX.eyes = "_side"
                            $ KittyX.change_stat("obedience", 80, 5)
                            ch_k "I mean, I guess, if you like that kind of thing. . ."
                        else:
                            $ KittyX.GirlLikeUp(TempLine,-50)
                            $ TempLine = "bad"
                    elif TempLine:
                        if KittyX.GirlLikeCheck(TempLine) >= 800:
                            $ KittyX.change_face("_sly",2,Eyes="_side")
                            $ KittyX.change_stat("obedience", 80, 5)
                            ch_k "Yeah, like two ripe apples. . . I mean-"
                            $ KittyX.GirlLikeUp(TempLine,20)
                        elif KittyX.GirlLikeCheck(TempLine) >= 700:
                            $ KittyX.eyes = "_side"
                            $ KittyX.change_stat("obedience", 80, 5)
                            ch_k "[KittyX.Like]I guess. . ."
                        else:
                            $ KittyX.GirlLikeUp(TempLine,-50)
                            $ TempLine = "bad"

                    if TempLine == "bad":
                        $ KittyX.change_stat("love", 90, -20)
                        ch_k "Well you sure know how to ruin a mood."
                        $ KittyX.change_outfit()
                        $ KittyX.recent_history.append("no_topless")
                        $ KittyX.daily_history.append("no_topless")
                        $ KittyX.recent_history.append("_angry")
                        $ KittyX.daily_history.append("_angry")
    else:


        $ KittyX.add_word(1,0, "", "", "topless")
        if approval_check(KittyX, 800) and not KittyX.Forced:
            $ KittyX.change_stat("inhibition", 70, 5)
            $ KittyX.change_stat("obedience", 70, 10)
        else:
            $ KittyX.change_stat("love", 90, -5)
            $ KittyX.change_stat("inhibition", 70, -5)
            $ KittyX.change_face("_angry")
            $ KittyX.change_stat("obedience", 70, 20)
    return

label Kitty_First_Bottomless(Silent=0):
    if KittyX.PantiesNum() > 1 or KittyX.PantsNum() > 2 or KittyX.HoseNum() > 9:

        return
    if KittyX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ KittyX.recent_history.append("bottomless")
    $ KittyX.daily_history.append("bottomless")
    $ KittyX.drain_word("no_bottomless")
    $ KittyX.SeenPussy += 1
    if KittyX.SeenPussy > 1:
        return

    $ KittyX.change_stat("inhibition", 80, 30)
    $ KittyX.change_stat("obedience", 70, 10)
    if not Silent:
        $ KittyX.change_face("_bemused", 1)
        "[KittyX.name] shyly moves her hands aside, revealing her pussy."
        menu Kitty_First_BMenu:
            extend ""
            "Lovely. . .":
                $ KittyX.change_stat("love", 90, 20)
                $ KittyX.change_stat("inhibition", 60, 25)
                $ KittyX.change_face("_smile")
                ch_k ". . ."
                $ KittyX.change_stat("love", 40, 20)
            "Now {i}that's{/i} the \"Kitty\" I wanted to see.":
                $ KittyX.change_stat("love", 40, 25)
                $ KittyX.change_stat("inhibition", 60, 30)
                $ KittyX.change_face("_perplexed", 2)
                ch_k "[[snort]"
                $ KittyX.change_stat("love", 90, 25)
                $ KittyX.blushing = "_blush1"
            "Pretty messy down there." if KittyX.pubes:
                $ KittyX.change_face("_surprised",2)
                ch_k "!"
                if approval_check(KittyX, 800, "LO"):
                    $ KittyX.change_face("_bemused",1)
                    $ KittyX.change_stat("obedience", 50, 30)
                    $ KittyX.change_stat("inhibition", 60, 25)
                    ch_k "I guess I could trim it up a bit. . ."
                    $ KittyX.Todo.append("shave")
                else:
                    $ KittyX.change_face("_angry",1)
                    $ KittyX.change_stat("love", 40, -20)
                    $ KittyX.change_stat("obedience", 50, 25)
                    $ KittyX.change_stat("inhibition", 60, -5)
                    ch_k "Well[KittyX.like]sorry I don't keep it baby soft!"
            "I've seen better.":
                $ KittyX.change_stat("love", 90, -30)
                $ KittyX.change_stat("obedience", 50, 25)
                $ KittyX.change_stat("inhibition", 70, -30)
                $ KittyX.change_face("_angry")
                ch_k ". . ."
                $ KittyX.change_stat("obedience", 70, 35)
    else:
        $ KittyX.add_word(1,0, "", "", "bottomless")
        if approval_check(KittyX, 800) and not KittyX.Forced:
            $ KittyX.change_stat("inhibition", 60, 15)
            $ KittyX.change_stat("obedience", 70, 10)
        else:
            $ KittyX.change_stat("love", 90, -10)
            $ KittyX.change_stat("inhibition", 70, -5)
            $ KittyX.change_face("_angry")
            $ KittyX.change_stat("obedience", 70, 20)
    return



label Emma_First_Topless(Silent=0, TempLine=0):
    if EmmaX.ChestNum() > 1 or EmmaX.OverNum() > 2:

        return
    if EmmaX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ EmmaX.recent_history.append("topless")
    $ EmmaX.daily_history.append("topless")
    $ EmmaX.drain_word("no_topless")
    $ EmmaX.SeenChest += 1
    if EmmaX.SeenChest > 1:
        return


    $ EmmaX.change_stat("inhibition", 70, 15)
    if not Silent:
        $ EmmaX.change_face("_sly")
        "You get your first look at [EmmaX.name]'s bare chest."
        ch_e "Well, [EmmaX.player_petname]? Is it everything you dreamed?"
        $ EmmaX.blushing = "_blush1"
        menu Emma_First_TMenu:
            extend ""
            "Definitely, and more.":
                $ EmmaX.change_stat("love", 90, 20)
                $ EmmaX.change_stat("inhibition", 70, 20)
                $ EmmaX.change_face("_smile",1)
                ch_e "I do aim to impress."
                $ EmmaX.change_stat("love", 40, 20)
                $ EmmaX.blushing = ""
            ". . . [[stunned]":
                $ EmmaX.change_stat("love", 90, 20)
                $ EmmaX.change_stat("inhibition", 70, 30)
                ch_e "Yes, that would be the usual reaction."
                $ EmmaX.change_stat("love", 40, 10)
            "Huh, not what I was expecting. . .":
                $ EmmaX.change_stat("love", 90, -30)
                $ EmmaX.change_stat("obedience", 60, 25)
                $ EmmaX.change_stat("inhibition", 70, -15)
                $ EmmaX.change_face("_confused",2)
                ch_e "What?"
                menu:
                    "They're even better than I imagined!":
                        $ EmmaX.change_stat("love", 90, 20)
                        $ EmmaX.change_stat("obedience", 60, -20)
                        $ EmmaX.change_stat("inhibition", 70, 20)
                        $ EmmaX.change_face("_perplexed",1)
                        ch_e "Well, I suppose you managed to salvage that one. . ."
                    "I, um, no, they're great!":
                        $ EmmaX.change_face("_angry",2, Mouth="_smile")
                        $ EmmaX.change_stat("inhibition", 70, 10)
                        ch_e "Of couse they are!"
                    "[RogueX.name]'s were tighter, that's all." if RogueX.SeenChest:
                        $ TempLine = RogueX
                    "[KittyX.name]'s were tighter, that's all." if KittyX.SeenChest:
                        $ TempLine = KittyX
                    "[LauraX.name]'s were tighter, that's all." if LauraX.SeenChest:
                        $ TempLine = LauraX
                    "[JeanX.name]'s were tighter, that's all." if JeanX.SeenChest:
                        $ TempLine = JeanX
                    "[StormX.name]'s were larger, that's all." if StormX.SeenChest:
                        $ TempLine = StormX

                if TempLine:
                    $ EmmaX.change_face("_angry")
                    $ EmmaX.mouth = "_surprised"
                    $ EmmaX.change_stat("love", 90, -10)
                    $ EmmaX.change_stat("obedience", 80, 30)
                    $ EmmaX.change_stat("inhibition", 70, -25)
                    ch_e ". . ."
                    $ EmmaX.mouth = "_sad"
                    if TempLine == KittyX:
                        if EmmaX.LikeKitty >= 800:
                            $ EmmaX.change_face("_sly",2,Eyes="_side")
                            $ EmmaX.change_stat("obedience", 80, 5)
                            ch_e "They are rather . . . pert. . ."
                            $ EmmaX.LikeKitty += 20
                        elif EmmaX.LikeKitty >= 700:
                            $ EmmaX.eyes = "_side"
                            $ EmmaX.change_stat("obedience", 80, 5)
                            ch_e "Well, for a child. . ."
                        else:
                            $ EmmaX.LikeKitty -= 50
                            $ TempLine = "bad"

                    elif TempLine == StormX:
                        if EmmaX.GirlLikeCheck(TempLine) >= 800:
                            $ EmmaX.change_face("_sly",2,Eyes="_side")
                            $ EmmaX.change_stat("obedience", 80, 5)
                            ch_e "They are lovely, but. . ."
                            $ EmmaX.GirlLikeUp(TempLine,20)
                        elif EmmaX.GirlLikeCheck(TempLine) >= 700:
                            $ EmmaX.eyes = "_side"
                            $ EmmaX.change_stat("obedience", 80, 5)
                            ch_e "I don't know about that. . ."
                        else:
                            $ EmmaX.GirlLikeUp(TempLine,-50)
                            $ TempLine = "bad"
                    elif TempLine:
                        if EmmaX.GirlLikeCheck(TempLine) >= 800:
                            $ EmmaX.change_face("_sly",2,Eyes="_side")
                            $ EmmaX.change_stat("obedience", 80, 5)
                            ch_e "They are rather . . . ripe. . ."
                            $ EmmaX.GirlLikeUp(TempLine,20)
                        elif EmmaX.GirlLikeCheck(TempLine) >= 700:
                            $ EmmaX.eyes = "_side"
                            $ EmmaX.change_stat("obedience", 80, 5)
                            ch_e "I suppose if you prefer that. . ."
                        else:
                            $ EmmaX.GirlLikeUp(TempLine,-50)
                            $ TempLine = "bad"


                    if TempLine == "bad":
                        $ EmmaX.change_stat("love", 90, -20)
                        ch_e "I think you've seen enough for now, [EmmaX.player_petname]."
                        $ EmmaX.change_outfit()
                        $ EmmaX.recent_history.append("no_topless")
                        $ EmmaX.daily_history.append("no_topless")
                        $ EmmaX.recent_history.append("_angry")
                        $ EmmaX.daily_history.append("_angry")
    else:


        $ EmmaX.add_word(1,0, "", "", "topless")
        if approval_check(EmmaX, 800) and not EmmaX.Forced:
            $ EmmaX.change_stat("inhibition", 70, 5)
            $ EmmaX.change_stat("obedience", 70, 5)
        else:
            $ EmmaX.change_stat("love", 90, -10)
            $ EmmaX.change_stat("inhibition", 70, -5)
            $ EmmaX.change_face("_angry")
            $ EmmaX.change_stat("obedience", 70, 15)
    return


label Emma_First_Bottomless(Silent=0):
    if EmmaX.PantiesNum() > 1 or EmmaX.PantsNum() > 2 or EmmaX.HoseNum() > 9:

        return
    if EmmaX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ EmmaX.recent_history.append("bottomless")
    $ EmmaX.daily_history.append("bottomless")
    $ EmmaX.drain_word("no_bottomless")
    $ EmmaX.SeenPussy += 1
    if EmmaX.SeenPussy > 1:
        return


    $ EmmaX.change_stat("inhibition", 80, 30)
    $ EmmaX.change_stat("obedience", 70, 10)
    if not Silent:
        $ EmmaX.change_face("_sly")
        "You find yourself staring at [EmmaX.name]'s bare pussy."
        menu Emma_First_BMenu:
            extend ""
            "Niiice. . .":
                $ EmmaX.change_stat("love", 90, 20)
                $ EmmaX.change_stat("inhibition", 60, 25)
                $ EmmaX.change_face("_smile")
                ch_e "I'm aware. . . "
                $ EmmaX.change_stat("love", 40, 20)
            "I see you keep it smooth down there." if not EmmaX.pubes:
                $ EmmaX.change_face("_confused",1)
                ch_e "Yes?"
                if approval_check(EmmaX, 700, "LO"):
                    $ EmmaX.change_face("_bemused")
                    menu:
                        ch_e "Do you prefer more fuzz?"
                        "Yes":
                            if approval_check(EmmaX, 900, "LO"):
                                $ EmmaX.change_stat("obedience", 50, 30)
                                $ EmmaX.change_stat("inhibition", 60, 25)
                                ch_e "I suppose I could let it go. . ."
                                $ EmmaX.Todo.append("pubes")
                            else:
                                $ EmmaX.change_face("_normal")
                                ch_e "Well that's a pity."
                        "Up to you, I guess.":
                            $ EmmaX.change_stat("love", 80, 10)
                            ch_e "I'm glad you agree."
                        "No, leave it that way.":
                            if approval_check(EmmaX, 900, "LO"):
                                $ EmmaX.change_face("_sly")
                                $ EmmaX.change_stat("love", 80, 10)
                            else:
                                $ EmmaX.change_face("_angry",Mouth="_normal")
                            $ EmmaX.change_stat("inhibition", 60, 25)
                            ch_e "I'm glad I have your. . . permission."
                            $ EmmaX.brows = "_normal"
                else:
                    $ EmmaX.change_face("_angry",1)
                    $ EmmaX.change_stat("love", 40, -20)
                    $ EmmaX.change_stat("obedience", 50, 25)
                    $ EmmaX.change_stat("inhibition", 60, -5)
                    ch_e "Yes, I'm afraid I don't like an unkept garden."
            "Not bad for someone your age.":
                $ EmmaX.change_stat("love", 90, -30)
                $ EmmaX.change_stat("obedience", 50, 25)
                $ EmmaX.change_stat("inhibition", 70, -30)
                $ EmmaX.change_face("_angry",2)
                if not EmmaX.Forced and not approval_check(EmmaX, 900, "LO"):
                    $ EmmaX.recent_history.append("_angry")
                    $ EmmaX.daily_history.append("_angry")
                    $ EmmaX.change_stat("obedience", 70, 25)
                ch_e "You will regret that remark. . ."
    else:

        $ EmmaX.add_word(1,0, "", "", "bottomless")
        if approval_check(EmmaX, 800) and not EmmaX.Forced:
            $ EmmaX.change_stat("inhibition", 60, 5)
            $ EmmaX.change_stat("obedience", 70, 10)
        else:
            $ EmmaX.change_stat("love", 90, -10)
            $ EmmaX.change_stat("inhibition", 70, -5)
            $ EmmaX.change_face("_angry")
            $ EmmaX.change_stat("obedience", 70, 15)
    return


label Laura_First_Topless(Silent=0, TempLine=0):
    if LauraX.ChestNum() > 1 or LauraX.OverNum() > 2:

        return
    if LauraX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ LauraX.recent_history.append("topless")
    $ LauraX.daily_history.append("topless")
    $ LauraX.drain_word("no_topless")
    $ LauraX.SeenChest += 1
    if LauraX.SeenChest > 1:
        return

    $ LauraX.change_stat("inhibition", 70, 15)
    if not Silent:
        $ LauraX.change_face("_sly")
        "You get your first look at Laura's bare chest."
        ch_l "So? What are you looking at?"
        $ LauraX.blushing = "_blush1"
        menu Laura_First_TMenu:
            extend ""
            "Your tits? They look great.":
                $ LauraX.change_stat("love", 90, 20)
                $ LauraX.change_stat("inhibition", 70, 20)
                $ LauraX.change_face("_sexy",1,Eyes="_down")
                ch_l "Huh. I mean I guess so. . ."
                $ LauraX.change_face("_smile", 0)
                $ LauraX.change_stat("love", 40, 20)
            ". . . [[stunned]":
                $ LauraX.change_stat("love", 90, 10)
                $ LauraX.change_stat("inhibition", 70, 10)
                ch_l "Cat got your tongue?"
                $ LauraX.change_stat("love", 40, 10)
            "Huh, not what I was expecting. . .":
                $ LauraX.change_stat("love", 90, -30)
                $ LauraX.change_stat("obedience", 60, 25)
                $ LauraX.change_stat("inhibition", 70, -15)
                $ LauraX.change_face("_confused",2)
                ch_l "Huh?"
                menu:
                    "They're really perky!":
                        $ LauraX.change_stat("love", 90, 20)
                        $ LauraX.change_stat("obedience", 60, -20)
                        $ LauraX.change_stat("inhibition", 70, 20)
                        $ LauraX.change_face("_perplexed",1)
                        ch_l "Oh. Right. . ."
                    "I, um, no, they're great!":
                        $ LauraX.change_face("_angry",2, Mouth="_smile")
                        $ LauraX.change_stat("inhibition", 70, 10)
                        ch_l "Why wouldn't they be?"
                    "[KittyX.name]'s were tighter, that's all." if KittyX.SeenChest:
                        $ TempLine = KittyX
                    "[EmmaX.name]'s were a lot bigger, that's all." if EmmaX.SeenChest:
                        $ TempLine = EmmaX
                    "[StormX.name]'s were a lot bigger, that's all." if StormX.SeenChest:
                        $ TempLine = StormX

                if TempLine:
                    $ LauraX.change_face("_angry")
                    $ LauraX.mouth = "_surprised"
                    $ LauraX.change_stat("love", 90, -10)
                    $ LauraX.change_stat("obedience", 80, 30)
                    $ LauraX.change_stat("inhibition", 70, -25)
                    ch_l ". . ."
                    $ LauraX.mouth = "_sad"
                    if TempLine in (EmmaX,StormX):
                        if LauraX.GirlLikeCheck(TempLine) >= 800:
                            $ LauraX.change_face("_sly",2,Eyes="_side")
                            $ LauraX.change_stat("obedience", 80, 5)
                            ch_l "They are kinda huge. . ."
                            $ LauraX.GirlLikeUp(TempLine,20)
                        elif LauraX.GirlLikeCheck(TempLine) >= 700:
                            $ LauraX.eyes = "_side"
                            $ LauraX.change_stat("obedience", 80, 5)
                            ch_l "I guess that's true. . ."
                        else:
                            $ LauraX.GirlLikeUp(TempLine,-50)
                            $ TempLine = "bad"

                    elif TempLine == KittyX:
                        if LauraX.LikeKitty >= 800:
                            $ LauraX.change_face("_sly",2,Eyes="_side")
                            $ LauraX.change_stat("obedience", 80, 5)
                            ch_l "She is very. . . streamlined. . ."
                            $ LauraX.LikeKitty += 20
                        elif LauraX.LikeKitty >= 700:
                            $ LauraX.eyes = "_side"
                            $ LauraX.change_stat("obedience", 80, 5)
                            ch_l "they are kinda. . . pointy. . ."
                        else:
                            $ LauraX.LikeKitty -= 50
                            $ TempLine = "bad"


                    if TempLine == "bad":
                        $ LauraX.change_stat("love", 90, -20)
                        ch_l "Still kinda rude though."
                        $ LauraX.change_outfit()
                        $ LauraX.recent_history.append("no_topless")
                        $ LauraX.daily_history.append("no_topless")
                        $ LauraX.recent_history.append("_angry")
                        $ LauraX.daily_history.append("_angry")
    else:


        $ LauraX.add_word(1,0, "", "", "topless")
        if approval_check(LauraX, 800) and not LauraX.Forced:
            $ LauraX.change_stat("inhibition", 70, 5)
            $ LauraX.change_stat("obedience", 70, 10)
        else:
            $ LauraX.change_stat("love", 90, -5)
            $ LauraX.change_stat("inhibition", 70, -5)
            $ LauraX.change_face("_angry")
            $ LauraX.change_stat("obedience", 70, 10)
    return


label Laura_First_Bottomless(Silent=0):
    if LauraX.PantiesNum() > 1 or LauraX.PantsNum() > 2 or LauraX.HoseNum() > 9:

        return
    if LauraX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ LauraX.recent_history.append("bottomless")
    $ LauraX.daily_history.append("bottomless")
    $ LauraX.drain_word("no_bottomless")
    $ LauraX.SeenPussy += 1
    if LauraX.SeenPussy > 1:
        return


    $ LauraX.change_stat("inhibition", 80, 30)
    $ LauraX.change_stat("obedience", 70, 10)
    if not Silent:
        $ LauraX.change_face("_sly")
        if LauraX.pubes:
            "You find yourself staring at [LauraX.name]'s furry pussy."
        else:
            "You find yourself staring at [LauraX.name]'s bare pussy."
        menu Laura_First_BMenu:
            extend ""
            "Niiice. . .":
                $ LauraX.change_stat("love", 90, 20)
                $ LauraX.change_stat("inhibition", 60, 25)
                $ LauraX.change_face("_smile")
                ch_l "You think?"
                ch_l "Yeah, I like it too. . . "
                $ LauraX.change_stat("love", 40, 20)
            "I see you keep it natural down there." if LauraX.pubes:
                $ LauraX.change_face("_confused",1)
                ch_l "Well. . . yeah."
                if approval_check(LauraX, 700, "LO"):
                    $ LauraX.change_face("_bemused")
                    menu:
                        ch_l "What, am I supposed to shave it?"
                        "Yes":
                            if approval_check(LauraX, 900, "LO"):
                                $ LauraX.change_stat("obedience", 50, 30)
                                $ LauraX.change_stat("inhibition", 60, 25)
                                ch_l "I guess I could. . ."
                                $ LauraX.Todo.append("pubes")
                            else:
                                $ LauraX.change_face("_normal")
                                ch_l "Seems like a waste of time."
                                ch_l "Do you know how fast my hair grows?"
                        "Up to you, I guess.":
                            $ LauraX.change_stat("love", 80, 10)
                            ch_l "Yeah, I mean, shaving would be a lot of work."
                        "No, leave it that way.":
                            if approval_check(LauraX, 900, "LO"):
                                $ LauraX.change_face("_sly")
                                $ LauraX.change_stat("love", 80, 10)
                            else:
                                $ LauraX.change_face("_angry",Mouth="_normal")
                            $ LauraX.change_stat("inhibition", 60, 25)
                            ch_l "Right."
                            $ LauraX.brows = "_normal"
                else:
                    $ LauraX.change_face("_angry",1)
                    $ LauraX.change_stat("love", 40, -20)
                    $ LauraX.change_stat("obedience", 50, 25)
                    $ LauraX.change_stat("inhibition", 60, -5)
                    ch_l "I mean, what else would I do?"
            "What a mess.":
                $ LauraX.change_stat("love", 90, -30)
                $ LauraX.change_stat("obedience", 50, 25)
                $ LauraX.change_stat("inhibition", 70, -30)
                $ LauraX.change_face("_angry",2)
                if not LauraX.Forced and not approval_check(LauraX, 900, "LO"):
                    $ LauraX.recent_history.append("_angry")
                    $ LauraX.daily_history.append("_angry")
                    $ LauraX.change_stat("obedience", 70, 25)
                ch_l "I'll make you a mess. . ."
    else:
        $ LauraX.add_word(1,0, "", "", "bottomless")
        if approval_check(LauraX, 800) and not LauraX.Forced:
            $ LauraX.change_stat("inhibition", 60, 5)
            $ LauraX.change_stat("obedience", 70, 10)
        else:
            $ LauraX.change_stat("love", 90, -5)
            $ LauraX.change_stat("inhibition", 70, -5)
            $ LauraX.change_face("_angry")
            $ LauraX.change_stat("obedience", 70, 15)
    return



label Jean_First_Topless(Silent=0, TempLine=0):
    if (JeanX.ChestNum() > 1 or JeanX.OverNum() > 2) and not TempLine:


        return
    if JeanX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ JeanX.recent_history.append("topless")
    $ JeanX.daily_history.append("topless")
    $ JeanX.drain_word("no_topless")
    $ JeanX.SeenChest += 1
    if JeanX.SeenChest > 1:
        return

    $ JeanX.change_stat("inhibition", 70, 15)
    if not Silent:
        $ JeanX.change_face("_sly")
        "You get your first look at Jean's bare chest."
        ch_j "So, pretty spectacular, right?"
        $ JeanX.blushing = "_blush1"
        menu Jean_First_TMenu:
            extend ""
            "Yeah, they look amazing.":
                $ JeanX.change_stat("love", 90, 10)
                $ JeanX.change_stat("inhibition", 200, 20)
                $ JeanX.change_face("_sexy",1,Eyes="_down")
                ch_j "Yeah, they are pretty tight. . ."
                $ JeanX.change_face("_smile", 0)
                $ JeanX.change_stat("obedience", 40, 20)
            ". . . [[stunned]":
                $ JeanX.change_stat("love", 90, 20)
                $ JeanX.change_stat("inhibition", 200, 10)
                ch_j "Stunning, I know."
                $ JeanX.change_stat("obedience", 40, 10)
            "Huh, not what I was expecting. . .":
                $ JeanX.change_stat("love", 90, 10)
                $ JeanX.change_stat("obedience", 40, 20)
                $ JeanX.change_stat("inhibition", 200, 20)
                $ JeanX.change_face("_smile", 0)
                ch_j "Exactl-{w=0.3}{nw}"
                $ JeanX.change_stat("love", 90, -40)
                $ JeanX.change_stat("obedience", 60, 10)
                $ JeanX.change_stat("inhibition", 200, -15)
                $ JeanX.change_face("_confused",2)
                ch_j "Exactl- wait, what?"
                $ TempLine = 0
                menu:
                    "They're really perky!":
                        $ JeanX.change_stat("love", 90, 10)
                        $ JeanX.change_stat("obedience", 60, 10)
                        $ JeanX.change_stat("inhibition", 200, 20)
                        $ JeanX.change_face("_perplexed",1)
                        ch_j "Oh. Of course. . ."
                    "I, um, no, they're great!":
                        $ JeanX.change_face("_angry",2, Mouth="_smile")
                        $ JeanX.change_stat("obedience", 80, 20)
                        ch_j "Of course they are!"
                    "[RogueX.name]'s were nicer, that's all." if RogueX.SeenChest:
                        $ TempLine = RogueX
                    "[KittyX.name]'s were tighter, that's all." if KittyX.SeenChest:
                        $ TempLine = KittyX
                    "[EmmaX.name]'s were a lot bigger, that's all." if EmmaX.SeenChest:
                        $ TempLine = EmmaX
                    "[LauraX.name]'s were nicer, that's all." if LauraX.SeenChest:
                        $ TempLine = LauraX
                    "[StormX.name]'s were a lot bigger, that's all." if StormX.SeenChest:
                        $ TempLine = StormX

                if TempLine:
                    $ JeanX.change_face("_angry")
                    $ JeanX.mouth = "_surprised"
                    $ JeanX.change_stat("love", 50, -10)
                    $ JeanX.change_stat("love", 90, -10)
                    $ JeanX.change_stat("obedience", 50, 10)
                    $ JeanX.change_stat("obedience", 80, 30)
                    $ JeanX.change_stat("inhibition", 200, -15)
                    ch_j ". . ."
                    $ JeanX.mouth = "_sad"
                    if TempLine in (EmmaX,StormX):
                        if JeanX.GirlLikeCheck(TempLine) >= 700:
                            $ JeanX.change_face("_sly",2,Eyes="_side")
                            ch_j "Well, they are. . . heavy. . ."
                            $ JeanX.GirlLikeUp(TempLine,20)
                        else:
                            $ JeanX.eyes = "_side"
                            ch_j "If you have a thing for udders. . ."
                            $ JeanX.LikeEmma -= 50
                            $ JeanX.GirlLikeUp(TempLine,-50)
                            $ TempLine = "bad"

                    elif TempLine == KittyX:
                        if JeanX.LikeKitty >= 700:
                            $ JeanX.change_face("_sly",2,Eyes="_side")
                            ch_j "She is very. . . cute. . ."
                            $ JeanX.LikeKitty += 20
                        else:
                            $ JeanX.eyes = "_side"
                            ch_j "If you have a thing for surf boards. . ."
                            $ JeanX.LikeKitty -= 50
                            $ TempLine = "bad"
                    else:
                        if JeanX.GirlLikeCheck(TempLine) >= 700:
                            $ JeanX.change_face("_sly",2,Eyes="_side")
                            ch_j "She is very. . . petite. . ."
                            $ JeanX.GirlLikeUp(TempLine,20)
                        else:
                            $ JeanX.eyes = "_side"
                            ch_j "they are kinda. . . pointy. . ."
                            $ JeanX.GirlLikeUp(TempLine,-50)
                            $ TempLine = "bad"


                    if TempLine == "bad":
                        $ JeanX.change_stat("love", 90, -20)
                        ch_j "Still, inappropriate on your part!"
                        $ JeanX.change_outfit()
                        $ JeanX.recent_history.append("no_topless")
                        $ JeanX.daily_history.append("no_topless")
                        $ JeanX.recent_history.append("_angry")
                        $ JeanX.daily_history.append("_angry")
    else:


        if approval_check(JeanX, 800) and not JeanX.Forced:
            $ JeanX.change_stat("love", 70, 10)
            $ JeanX.change_stat("obedience", 70, 25)
            $ JeanX.change_stat("inhibition", 70, 15)
        else:
            $ JeanX.change_stat("love", 90, -40)
            $ JeanX.change_stat("inhibition", 200, -20)
            $ JeanX.change_face("_angry")
            $ JeanX.change_stat("obedience", 70, 40)
    return


label Jean_First_Bottomless(Silent=0):
    if JeanX.PantiesNum() > 1 or JeanX.PantsNum() > 2 or JeanX.HoseNum() > 9:

        return
    if JeanX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ JeanX.recent_history.append("bottomless")
    $ JeanX.daily_history.append("bottomless")
    $ JeanX.drain_word("no_bottomless")
    $ JeanX.SeenPussy += 1
    if JeanX.SeenPussy > 1:
        return

    $ JeanX.change_stat("inhibition", 200, 30)
    $ JeanX.change_stat("obedience", 90, 10)
    if not Silent:
        $ JeanX.change_face("_sly")
        if JeanX.pubes:
            "You find yourself staring at [JeanX.name]'s fuzzy pussy."
        else:
            "You find yourself staring at [JeanX.name]'s bare pussy."
        menu Jean_First_BMenu:
            extend ""
            "Niiice. . .":
                $ JeanX.change_stat("love", 90, 20)
                $ JeanX.change_stat("inhibition", 200, 25)
                $ JeanX.change_face("_smile")
                ch_j "Right?"
                $ JeanX.change_stat("love", 40, 20)
            "I see you got a fire crotch down there." if JeanX.pubes:
                $ JeanX.change_face("_confused",1)
                ch_j "Well. . . yeah."
                if approval_check(JeanX, 700, "LO"):
                    $ JeanX.change_face("_bemused")
                    menu:
                        ch_j "Do you prefer it smooth?"
                        "Yes":
                            if approval_check(JeanX, 900, "LO"):
                                $ JeanX.change_stat("obedience", 90, 30)
                                $ JeanX.change_stat("inhibition", 200, 25)
                                ch_j "Hmm, I guess. . ."
                                $ JeanX.Todo.append("pubes")
                            else:
                                $ JeanX.change_face("_normal")
                                ch_j "Not worth the hassle."
                        "Up to you, I guess.":
                            $ JeanX.change_stat("love", 80, 10)
                            ch_j "Of course it is."
                        "No, leave it that way.":
                            if approval_check(JeanX, 900, "LO"):
                                $ JeanX.change_face("_sly")
                                $ JeanX.change_stat("love", 80, 10)
                            else:
                                $ JeanX.change_face("_angry",Mouth="_normal")
                            $ JeanX.change_stat("inhibition", 200, 25)
                            ch_j "Of course."
                            $ JeanX.brows = "_normal"
                else:
                    $ JeanX.change_face("_angry",1)
                    $ JeanX.change_stat("love", 40, -20)
                    $ JeanX.change_stat("obedience", 90, 25)
                    $ JeanX.change_stat("inhibition", 200, -5)
                    ch_j "I didn't really feel like waxing it."
            "What a mess." if JeanX.pubes:
                $ JeanX.change_stat("love", 90, -30)
                $ JeanX.change_stat("obedience", 90, 25)
                $ JeanX.change_stat("inhibition", 200, -30)
                $ JeanX.change_face("_angry",2)
                if not JeanX.Forced and not approval_check(JeanX, 900, "LO"):
                    $ JeanX.recent_history.append("_angry")
                    $ JeanX.daily_history.append("_angry")
                    $ JeanX.change_stat("obedience", 90, 25)
                ch_j "Oh, so it's not baby-smooth like [EmmaX.name]'s?"
            "Eh, I've seen better" if not JeanX.pubes:
                $ JeanX.change_stat("love", 90, -30)
                $ JeanX.change_stat("obedience", 90, 25)
                $ JeanX.change_stat("inhibition", 200, -30)
                $ JeanX.change_face("_angry",2)
                if not JeanX.Forced and not approval_check(JeanX, 900, "LO"):
                    $ JeanX.recent_history.append("_angry")
                    $ JeanX.daily_history.append("_angry")
                    $ JeanX.change_stat("obedience", 90, 25)
                ch_j "Oh, so it's not saggy like [EmmaX.name]'s?"
    else:
        $ JeanX.add_word(1,0, "", "", "bottomless")
        if approval_check(JeanX, 800) and not JeanX.Forced:
            $ JeanX.change_stat("inhibition", 60, 5)
            $ JeanX.change_stat("obedience", 90, 10)
        else:
            $ JeanX.change_stat("love", 90, -5)
            $ JeanX.change_stat("inhibition", 200, -5)
            $ JeanX.change_face("_angry")
            $ JeanX.change_stat("obedience", 90, 15)
    return



label Storm_First_Topless(Silent=0, TempLine=0):

    if StormX.ChestNum() > 1 or StormX.OverNum() > 2:

        return
    if StormX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ StormX.recent_history.append("topless")
    $ StormX.daily_history.append("topless")
    $ StormX.drain_word("no_topless")
    $ StormX.SeenChest += 1
    return


label Storm_First_Bottomless(Silent=0):
    if StormX.PantiesNum() > 1 or StormX.PantsNum() > 2 or StormX.HoseNum() > 9:

        return
    if StormX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ StormX.recent_history.append("bottomless")
    $ StormX.daily_history.append("bottomless")
    $ StormX.drain_word("no_bottomless")
    $ StormX.SeenPussy += 1
    return



label Jubes_First_Topless(Silent=0, TempLine=0):
    if JubesX.ChestNum() > 1 or JubesX.OverNum() > 2:

        return
    if JubesX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ JubesX.recent_history.append("topless")
    $ JubesX.daily_history.append("topless")
    $ JubesX.drain_word("no_topless")
    $ JubesX.SeenChest += 1
    if JubesX.SeenChest > 1:
        return

    $ JubesX.change_stat("inhibition", 70, 15)
    if not Silent:
        $ JubesX.change_face("_sly")
        "You get your first look at Jubes's bare chest."
        ch_v "So. . . um. . . like what you see?"
        $ JubesX.blushing = "_blush1"
        menu Jubes_First_TMenu:
            extend ""
            "Your tits? They look great.":
                $ JubesX.change_stat("love", 90, 20)
                $ JubesX.change_stat("inhibition", 70, 20)
                $ JubesX.change_face("_smile",2)
                pause 0.5
                $ JubesX.change_face("_sexy",1,Eyes="_down")
                ch_v "Ah! Um. . . yeah, I guess. . ."
                $ JubesX.change_face("_smile")
                $ JubesX.change_stat("love", 40, 20)
            ". . . [[stunned]":
                $ JubesX.change_stat("love", 90, 10)
                $ JubesX.change_stat("inhibition", 70, 10)
                ch_v "Oh, that's a \"hit.\""
                $ JubesX.change_stat("love", 40, 10)
            "Huh, not what I was expecting. . .":
                $ JubesX.change_stat("love", 90, -30)
                $ JubesX.change_stat("obedience", 60, 25)
                $ JubesX.change_stat("inhibition", 70, -15)
                $ JubesX.change_face("_confused",2)
                ch_v "Wha?"
                menu:
                    "They're really perky!":
                        $ JubesX.change_stat("love", 90, 20)
                        $ JubesX.change_stat("obedience", 60, -20)
                        $ JubesX.change_stat("inhibition", 70, 20)
                        $ JubesX.change_face("_perplexed",1)
                        ch_v "Oh. Right. . ."
                    "I, um, no, they're great!":
                        $ JubesX.change_face("_angry",2, Mouth="_smile")
                        $ JubesX.change_stat("inhibition", 70, 10)
                        ch_v ". . ."
                        ch_v "I -know- that, that's why I was confused?"
                    "[KittyX.name]'s were tighter, that's all." if KittyX.SeenChest:
                        $ TempLine = KittyX
                    "[EmmaX.name]'s were a lot bigger, that's all." if EmmaX.SeenChest:
                        $ TempLine = EmmaX
                    "[StormX.name]'s were a lot bigger, that's all." if StormX.SeenChest:
                        $ TempLine = StormX

                if TempLine:
                    $ JubesX.change_face("_angry")
                    $ JubesX.mouth = "_surprised"
                    $ JubesX.change_stat("love", 90, -10)
                    $ JubesX.change_stat("obedience", 80, 30)
                    $ JubesX.change_stat("inhibition", 70, -25)
                    ch_v ". . ."
                    $ JubesX.mouth = "_sad"
                    if TempLine in (EmmaX,StormX):
                        if JubesX.GirlLikeCheck(TempLine) >= 800:
                            $ JubesX.change_face("_sly",2,Eyes="_side")
                            $ JubesX.change_stat("obedience", 80, 5)
                            ch_v "Well they are really ginormous. . ."
                            $ JubesX.GirlLikeUp(TempLine,20)
                        elif JubesX.GirlLikeCheck(TempLine) >= 700:
                            $ JubesX.eyes = "_side"
                            $ JubesX.change_stat("obedience", 80, 5)
                            ch_v "Oh. Well I can't compete there. . ."
                        else:
                            $ JubesX.GirlLikeUp(TempLine,-50)
                            $ TempLine = "bad"

                    elif TempLine == KittyX:
                        if JubesX.LikeKitty >= 800:
                            $ JubesX.change_face("_sly",2,Eyes="_side")
                            $ JubesX.change_stat("obedience", 80, 5)
                            ch_v ". . . I guess they are really cute. . ."
                            $ JubesX.LikeKitty += 20
                        elif JubesX.LikeKitty >= 700:
                            $ JubesX.eyes = "_side"
                            $ JubesX.change_stat("obedience", 80, 5)
                            ch_v "Ok, into that, uh? . ."
                        else:
                            $ JubesX.LikeKitty -= 50
                            $ TempLine = "bad"


                    if TempLine == "bad":
                        $ JubesX.change_stat("love", 90, -20)
                        ch_v "Still, you don't just -say- something like that!"
                        $ JubesX.change_outfit()
                        $ JubesX.recent_history.append("no_topless")
                        $ JubesX.daily_history.append("no_topless")
                        $ JubesX.recent_history.append("_angry")
                        $ JubesX.daily_history.append("_angry")
    else:


        $ JubesX.add_word(1,0, "", "", "topless")
        if approval_check(JubesX, 800) and not JubesX.Forced:
            $ JubesX.change_stat("inhibition", 70, 5)
            $ JubesX.change_stat("obedience", 70, 10)
        else:
            $ JubesX.change_stat("love", 90, -5)
            $ JubesX.change_stat("inhibition", 70, -5)
            $ JubesX.change_face("_angry")
            $ JubesX.change_stat("obedience", 70, 10)
    return


label Jubes_First_Bottomless(Silent=0):
    if JubesX.PantiesNum() > 1 or JubesX.PantsNum() > 2 or JubesX.HoseNum() > 9:

        return
    if JubesX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ JubesX.recent_history.append("bottomless")
    $ JubesX.daily_history.append("bottomless")
    $ JubesX.drain_word("no_bottomless")
    $ JubesX.SeenPussy += 1
    if JubesX.SeenPussy > 1:
        return


    $ JubesX.change_stat("inhibition", 80, 30)
    $ JubesX.change_stat("obedience", 70, 10)
    if not Silent:
        $ JubesX.change_face("_sly")
        if JubesX.pubes:
            "You find yourself staring at [JubesX.name]'s furry pussy."
        else:
            "You find yourself staring at [JubesX.name]'s bare pussy."
        menu Jubes_First_BMenu:
            extend ""
            "Niiice. . .":
                $ JubesX.change_stat("love", 90, 20)
                $ JubesX.change_stat("inhibition", 60, 25)
                $ JubesX.change_face("_surprised",2)
                ch_v "!!"
                $ JubesX.change_face("_smile",1)
                ch_v "Oh, um, yeah, I. . . also. . . "
                $ JubesX.change_stat("love", 40, 20)
            "I see you keep it natural down there." if JubesX.pubes:
                $ JubesX.change_face("_confused",2)
                ch_v "Well. . . yeah."
                if approval_check(JubesX, 700, "LO"):
                    $ JubesX.change_face("_bemused",1)
                    menu:
                        ch_v "Did you. . . prefer it shaved?"
                        "Yes":
                            if approval_check(JubesX, 900, "LO"):
                                $ JubesX.change_stat("obedience", 50, 30)
                                $ JubesX.change_stat("inhibition", 60, 25)
                                ch_v "I guess I could. . ."
                                $ JubesX.Todo.append("pubes")
                            else:
                                $ JubesX.change_face("_normal")
                                ch_v "I dunno, seems like a lot of hassle."
                        "Up to you, I guess.":
                            $ JubesX.change_stat("love", 80, 10)
                            ch_v "Well, yeah, right? Of course."
                            if approval_check(JubesX, 900, "LO"):
                                $ JubesX.change_stat("inhibition", 60, 10)
                                $ JubesX.Todo.append("pubes")
                        "No, leave it that way.":
                            if approval_check(JubesX, 900, "LO"):
                                $ JubesX.change_face("_sly")
                                $ JubesX.change_stat("love", 80, 10)
                            else:
                                $ JubesX.change_face("_angry",Mouth="_normal")
                            $ JubesX.change_stat("inhibition", 60, 25)
                            ch_v "Oh, I guess that's your call?"
                            $ JubesX.brows = "_normal"
                else:
                    $ JubesX.change_face("_angry",1)
                    $ JubesX.change_stat("love", 40, -20)
                    $ JubesX.change_stat("obedience", 50, 25)
                    $ JubesX.change_stat("inhibition", 60, -5)
                    ch_v "Well, of course!"
            "What a mess.":
                $ JubesX.change_stat("love", 90, -30)
                $ JubesX.change_stat("obedience", 50, 25)
                $ JubesX.change_stat("inhibition", 70, -30)
                $ JubesX.change_face("_angry",2)
                if not JubesX.Forced and not approval_check(JubesX, 900, "LO"):
                    $ JubesX.recent_history.append("_angry")
                    $ JubesX.daily_history.append("_angry")
                    $ JubesX.change_stat("obedience", 70, 25)
                ch_v "Oh, them's fighting words. . ."
    else:
        $ JubesX.add_word(1,0, "", "", "bottomless")
        if approval_check(JubesX, 800) and not JubesX.Forced:
            $ JubesX.change_stat("inhibition", 60, 5)
            $ JubesX.change_stat("obedience", 70, 10)
        else:
            $ JubesX.change_stat("love", 90, -5)
            $ JubesX.change_stat("inhibition", 70, -5)
            $ JubesX.change_face("_angry")
            $ JubesX.change_stat("obedience", 70, 15)
    return


label Showering(Occupants=[], StayCount=[] , Showered=0, Line=0, BO=[]):


    $ BO = all_Girls[:]
    while BO:

        if BO[0] not in active_Girls:
            $ BO[0].location = "hold"
        if BO[0].location == "bg_showerroom" and BO[0] not in Occupants:
            $ Occupants.append(BO[0])
        $ BO.remove(BO[0])
    if Occupants:
        ch_p "I'm taking a shower, care to join me?"
        if Occupants[0] == RogueX and "showered" in RogueX.recent_history:
            if len(Occupants) > 1:

                ch_r "We actually just finished up, so we'll head out."
            else:
                ch_r "I actually just finished up, so I'll head out."
            $ Showered = 1
        elif Occupants[0] == KittyX and "showered" in KittyX.recent_history:
            if len(Occupants) > 1:

                ch_k "We actually just showered, so we're heading out."
            else:
                ch_k "I actually just showered, so I'm heading out."
            $ Showered = 1
        elif Occupants[0] == EmmaX and "showered" in EmmaX.recent_history:
            if len(Occupants) > 1:

                ch_e "We were actually finishing up, so we're heading out."
            else:
                ch_e "I was actually finishing up, so I'm heading out."
            $ Showered = 1
        elif Occupants[0] == LauraX and "showered" in LauraX.recent_history:
            if len(Occupants) > 1:

                ch_l "We were done, actually."
            else:
                ch_l "I'm heading out now."
            $ Showered = 1
        elif Occupants[0] == JeanX and "showered" in JeanX.recent_history:
            if len(Occupants) > 1:

                ch_j "We were done."
            else:
                ch_j "I'm heading out."
            $ Showered = 1
        elif Occupants[0] == StormX and "showered" in StormX.recent_history:
            if len(Occupants) > 1:

                ch_s "I think we're about finished and heading out now."
            else:
                ch_s "I was about finished and heading out now."
            $ Showered = 1
        elif Occupants[0] == JubesX and "showered" in JubesX.recent_history:
            if len(Occupants) > 1:

                ch_v "We finished getting showered, so we're taking off."
            else:
                ch_v "I finished getting showered, so I'm taking off."
            $ Showered = 1
        else:

            if Occupants[0] == RogueX:
                if approval_check(RogueX, 1200) or (approval_check(RogueX, 600) and RogueX.SeenChest and RogueX.SeenPussy):

                    ch_r "I suppose I could stick around. . ."
                    $ StayCount.append(RogueX)
                else:

                    ch_r "Nah, I should probably get going."
            elif Occupants[0] == KittyX:
                if approval_check(KittyX, 1400) or (approval_check(KittyX, 700) and KittyX.SeenChest and KittyX.SeenPussy):
                    ch_k "Yeah, I could stick around."
                    $ StayCount.append(KittyX)
                else:
                    ch_k "I've got to get going."
            elif Occupants[0] == EmmaX:
                if not "classcaught" in EmmaX.history or "three" not in EmmaX.history:
                    ch_e "I really should be going. . ."
                elif approval_check(EmmaX, 1400) or (approval_check(EmmaX, 700) and EmmaX.SeenChest and EmmaX.SeenPussy):
                    ch_e "I suppose I could stay, for a bit."
                    $ StayCount.append(EmmaX)
                else:
                    ch_e "I'm afraid I really must be going."
            elif Occupants[0] == LauraX:
                if approval_check(LauraX, 1400) or (approval_check(LauraX, 700) and LauraX.SeenChest and LauraX.SeenPussy):
                    ch_l "I got nothing better to do."
                    $ StayCount.append(LauraX)
                else:
                    ch_l "I gotta get going."
            elif Occupants[0] == JeanX:
                if approval_check(JeanX, 1400) or (approval_check(JeanX, 700) and JeanX.SeenChest and JeanX.SeenPussy):
                    ch_j "Sure, why not."
                    $ StayCount.append(JeanX)
                else:
                    ch_j "Nah, lol."
            elif Occupants[0] == StormX:
                if approval_check(StormX, 700):
                    ch_s "I could stay, I suppose."
                    $ StayCount.append(StormX)
                else:
                    ch_s "I really do have things to do, [StormX.player_petname]."
            elif Occupants[0] == JubesX:
                if approval_check(JubesX, 1400) or (approval_check(JubesX, 700) and JubesX.SeenChest and JubesX.SeenPussy):
                    ch_v "I guess I could stay a minute. . ."
                    $ StayCount.append(JubesX)
                else:
                    ch_v "I'm kinda busy, [JubesX.player_petname]."


            if len(Occupants) >= 2:

                if Occupants[1] == RogueX:
                    if approval_check(RogueX, 1200) or (approval_check(RogueX, 600) and RogueX.SeenChest and RogueX.SeenPussy):
                        if StayCount:

                            ch_r "I could stick around too. . ."
                        else:

                            ch_r "Well, I could probably stay."
                        $ StayCount.append(RogueX)
                    else:
                        if StayCount:

                            ch_r "I can't though . ."
                        else:

                            ch_r "I should get going too."

                elif Occupants[1] == KittyX:
                    if approval_check(KittyX, 1400) or (approval_check(KittyX, 700) and KittyX.SeenChest and KittyX.SeenPussy):
                        if StayCount:

                            ch_k "I guess I could stay too. . ."
                        else:

                            ch_k "Well, I could stay though."
                        $ StayCount.append(KittyX)
                    else:
                        if StayCount:

                            ch_k "I've really got to go though. . ."
                        else:

                            ch_k "Yeah, I should head out too."

                elif Occupants[1] == EmmaX:
                    if not "classcaught" in EmmaX.history or "three" not in EmmaX.history:
                        ch_e "I really should be going. . ."
                    elif approval_check(EmmaX, 1400) or (approval_check(EmmaX, 700) and EmmaX.SeenChest and EmmaX.SeenPussy):
                        if StayCount:

                            ch_e "I suppose I could also stay. . ."
                        else:

                            ch_e "But {i}I{/i} could stick around. . ."
                        $ StayCount.append(EmmaX)
                    else:
                        if StayCount:

                            ch_e "But I really must be going. . ."
                        else:

                            ch_e "Yes, let's go."

                elif Occupants[1] == LauraX:
                    if approval_check(LauraX, 1400) or (approval_check(LauraX, 700) and LauraX.SeenChest and LauraX.SeenPussy):
                        if StayCount:

                            ch_l "I could stay too. . ."
                        else:

                            ch_l "I could stick around."
                        $ StayCount.append(LauraX)
                    else:
                        if StayCount:

                            ch_l "I gotta get going though. . ."
                        else:

                            ch_l "Yeah, me too."

                elif Occupants[1] == JeanX:
                    if approval_check(JeanX, 1000) or (approval_check(JeanX, 600) and JeanX.SeenChest and JeanX.SeenPussy):
                        if StayCount:

                            ch_j "I guess I could stay too. . ."
                        else:

                            ch_j "I could stick around."
                        $ StayCount.append(JeanX)
                    else:
                        if StayCount:

                            ch_j "I'm heading out though. . ."
                        else:

                            ch_j "Yeah."

                elif Occupants[1] == StormX:
                    if approval_check(StormX, 700):
                        if StayCount:

                            ch_s "I could also stay. . ."
                        else:

                            ch_s "I could stay for a moment though. . ."
                        $ StayCount.append(StormX)
                    else:
                        if StayCount:

                            ch_s "Well I'm afraid I must be going. . ."
                        else:

                            ch_s "Yes, let's."

                elif Occupants[1] == JubesX:
                    if approval_check(JubesX, 1400) or (approval_check(JubesX, 700) and JubesX.SeenChest and JubesX.SeenPussy):
                        if StayCount:

                            ch_k "I could kinda stay too. . ."
                        else:

                            ch_k "Well, -I'm- not that busy. . ."
                        $ StayCount.append(JubesX)
                    else:
                        if StayCount:

                            ch_k "I'm really busy right now though. . ."
                        else:

                            ch_k "Oh, yeah, I gotta go too. . ."


        if len(Occupants) > len(StayCount):

            menu:
                extend ""
                "Ok, see you later then.":
                    if RogueX.location == bg_current and RogueX not in StayCount:
                        ch_r "Yeah, later."
                    if KittyX.location == bg_current and KittyX not in StayCount:
                        ch_k "Bye!"
                    if EmmaX.location == bg_current and EmmaX not in StayCount:
                        ch_e "Yes, later."
                    if LauraX.location == bg_current and LauraX not in StayCount:
                        ch_l "Yup."
                    if JeanX.location == bg_current and JeanX not in StayCount:
                        ch_j "Ok."
                    if StormX.location == bg_current and StormX not in StayCount:
                        ch_s "Yes, I'll see you."
                    if JubesX.location == bg_current and JubesX not in StayCount:
                        ch_v "Laters!"

                "Sure you got every spot?" if Showered:
                    $ Line = "spot"
                "Maybe you could stay and watch?":



                    $ Line = "watch me"

                "But I didn't get to watch." if Showered:
                    $ Line = "watch you"
            if Line:
                $ BO = Occupants[:]
                while BO:

                    if BO[0].location == bg_current and BO[0] not in StayCount:
                        if BO[0] == EmmaX and (not "classcaught" in EmmaX.history or (StayCount and "three" not in EmmaX.history)):

                            pass
                        elif BO[0] == JeanX and approval_check(BO[0], 600):
                            $ StayCount.append(BO[0])
                        elif BO[0] == StormX:
                            if approval_check(BO[0], 700, "LO"):
                                $ StayCount.append(BO[0])
                        elif approval_check(BO[0], 1200,Alt=[[KittyX],1400]) or (approval_check(BO[0], 600,Alt=[[KittyX],700]) and BO[0].SeenChest and BO[0].SeenPussy):
                            $ StayCount.append(BO[0])
                        elif Line == "spot" and approval_check(BO[0], 1000, "LI",Alt=[[KittyX],1200]):
                            $ StayCount.append(BO[0])
                        elif Line == "watch you" and approval_check(BO[0], 600, "O",Alt=[[EmmaX],500]):
                            $ StayCount.append(BO[0])

                    $ BO.remove(BO[0])

                if Line == "spot":

                    if StayCount:

                        if StayCount[0] == RogueX:

                            ch_r "Fine, I could use another scrub."
                        elif StayCount[0] == KittyX:

                            ch_k "Oh, I guess I could take another pass at it."
                        elif StayCount[0] == EmmaX:

                            ch_e "I suppose we could take a look. . ."
                        elif StayCount[0] == LauraX:

                            ch_l "Well, maybe. . ."
                        elif StayCount[0] == JeanX:

                            ch_j "Well. . ."
                        elif StayCount[0] == StormX:

                            ch_s "Well, another pass couldn't hurt. . ."
                        elif StayCount[0] == JubesX:

                            ch_v "I mean, you can never be -too- clean. . ."
                    if RogueX.location == bg_current and RogueX not in StayCount:

                        if StayCount:
                            ch_r "Well, [RogueX.player_petname], I think I'm fine."
                        else:
                            ch_r "No, [RogueX.player_petname], I think I'm covered."
                    if KittyX.location == bg_current and KittyX not in StayCount:

                        if StayCount:
                            ch_k "Oh, well I think I[KittyX.like]got it?"
                            ch_k "See you later, [KittyX.player_petname]."
                        else:
                            ch_k "Ha, I'm squeaky clean, [KittyX.player_petname], see you later."
                    if EmmaX.location == bg_current and EmmaX not in StayCount:

                        if StayCount:
                            ch_e "Well it appears you'll be taken care of."
                            ch_e "I'll be going, [EmmaX.player_petname]."
                        else:
                            ch_e "I'm afraid not, [EmmaX.player_petname], I'll be going."
                    if LauraX.location == bg_current and LauraX not in StayCount:

                        if StayCount:
                            ch_l "Looks like you got this handled."
                            ch_l "I'm out, [LauraX.player_petname]."
                        else:
                            ch_l "I'm out."
                    if JeanX.location == bg_current and JeanX not in StayCount:

                        if StayCount:
                            ch_j "Well, looks like you guys are going to have fun."
                            ch_j "I'll head out, [JeanX.player_petname]."
                        else:
                            ch_j "I'll head out."
                    if StormX.location == bg_current and StormX not in StayCount:

                        if StayCount:
                            ch_s "It looks like you'll be occupied."
                            ch_s "I'll be going, [StormX.player_petname]."
                        else:
                            ch_s "I really doubt that I could have, [StormX.player_petname], I'll be going."
                    if JubesX.location == bg_current and JubesX not in StayCount:

                        if StayCount:
                            ch_v "Nah, I think you'll be fine."
                            ch_v "Later, guys."
                        else:
                            ch_v "Nah, I'm good. Later, [JubesX.player_petname]."


                elif Line == "watch me":

                    if StayCount:
                        if StayCount[0] == RogueX:

                            ch_r "Yeah, I guess I do enjoy the view."
                        elif StayCount[0] == KittyX:

                            ch_k "I. . . guess I wouldn't mind that. . ."
                        elif StayCount[0] == LauraX:

                            ch_l "Ok, let's see what you got."
                        elif StayCount[0] == JeanX:

                            ch_j "Ohh, this should be good. . ."
                        elif StayCount[0] == StormX:

                            ch_s "I suppose that I could. . ."
                        elif StayCount[0] == JubesX:

                            ch_v ". . . Yeah, ok."

                    if RogueX.location == bg_current and RogueX not in StayCount:

                        if StayCount:
                            ch_r "Oh, well, I'm gonna pass on that, [RogueX.player_petname]."
                        else:
                            ch_r "Yeah, I'm gonna pass on that, [RogueX.player_petname]."
                    if KittyX.location == bg_current and KittyX not in StayCount:

                        if StayCount:
                            ch_k "Well, [KittyX.like]I don't need to see that."
                            ch_k "See you later, [KittyX.player_petname]."
                        else:
                            ch_k "[KittyX.Like]I don't need to see that."
                    if EmmaX.location == bg_current and EmmaX not in StayCount:

                        if StayCount:
                            ch_e "You appear to have enough of an audience."
                            ch_e "I'll be going, [EmmaX.player_petname]."
                        else:
                            ch_e "I think I'll be fine, [EmmaX.player_petname], I'll be going."
                    if LauraX.location == bg_current and LauraX not in StayCount:

                        if StayCount:
                            ch_l "She's got you covered."
                            ch_l "I'm out, [LauraX.player_petname]."
                        else:
                            ch_l "I'm out."
                    if JeanX.location == bg_current and JeanX not in StayCount:

                        if StayCount:
                            ch_j "Well, looks like you guys are going to have fun."
                            ch_j "I'll head out, [JeanX.player_petname]."
                        else:
                            ch_j "I'll head out."
                    if StormX.location == bg_current and StormX not in StayCount:

                        if StayCount:
                            ch_s "Oh, I think someone else wants the show."
                            ch_s "I'll be going, [StormX.player_petname]."
                        else:
                            ch_s "I don't see why I would, [StormX.player_petname]. I'll be going."
                    if JubesX.location == bg_current and JubesX not in StayCount:

                        if StayCount:
                            ch_v "Um, no thanks. . ."
                            ch_v "See you later, [JubesX.player_petname]."
                        else:
                            ch_v "Um, no thanks."


                elif Line == "watch you":

                    if StayCount:
                        if StayCount[0] == RogueX:

                            ch_r "Well, I don't mind putting on a show."
                        elif StayCount[0] == KittyX:

                            ch_k "You want to watch me. . ."
                            ch_k "Ok."
                        elif StayCount[0] == EmmaX:

                            ch_e "I suppose I can't blame you for that. . ."
                        elif StayCount[0] == LauraX:

                            ch_l "Huh. Suit yourself."
                        elif StayCount[0] == JeanX:

                            ch_j "Well, we can't have that. . ."
                        elif StayCount[0] == StormX:

                            ch_s ". . ."
                        elif StayCount[0] == JubesX:

                            ch_v "Well. . . I guess we should make up for that. . ."

                    if RogueX.location == bg_current and RogueX not in StayCount:

                        if StayCount:
                            ch_r "Really? Well not me."
                            ch_r "Have fun, [RogueX.player_petname]."
                        else:
                            ch_r "Keep dreaming, [RogueX.player_petname]."
                    if KittyX.location == bg_current and KittyX not in StayCount:

                        if StayCount:
                            ch_k "Seriously?! Well I'm not into that."
                            ch_k "Later, [KittyX.player_petname]."
                        else:
                            ch_k "[KittyX.Like]no way!"
                    if EmmaX.location == bg_current and EmmaX not in StayCount:

                        if StayCount:
                            ch_e "I wouldn't want to intrude."
                            ch_e "I'll be going."
                        else:
                            ch_e "Hmm, I doubt you could handle it."
                            ch_e "I'll be going."
                    if LauraX.location == bg_current and LauraX not in StayCount:

                        if StayCount:
                            ch_l "She's got you covered."
                            ch_l "I'm out, [LauraX.player_petname]."
                        else:
                            ch_l "I'm out."
                    if JeanX.location == bg_current and JeanX not in StayCount:

                        if StayCount:
                            ch_j "Well, looks like you guys are going to have fun."
                            ch_j "I'll head out, [JeanX.player_petname]."
                        else:
                            ch_j "I'll head out."
                    if StormX.location == bg_current and StormX not in StayCount:

                        if StayCount:
                            ch_s "Well, you two enjoy yourselves."
                            ch_s "I'll be going."
                        else:
                            ch_s "I'm flattered, but no."
                            ch_s "I'll be going."
                    if JubesX.location == bg_current and JubesX not in StayCount:

                        if StayCount:
                            ch_v "Ok, looks like you two can have fun with that."
                            ch_v "Later, [JubesX.player_petname]."
                        else:
                            ch_v "Yeah, no way."


            if len(StayCount) > 1:

                if StayCount[1].GirlLikeCheck(StayCount[0]) > 500:

                    if StayCount[1] == RogueX:
                        ch_r "I guess I could too."
                    elif StayCount[1] == EmmaX:
                        ch_e "I suppose I don't want to be left out of this. . ."
                    elif StayCount[1] == JeanX:
                        ch_j "Well, it does look like fun. . ."
                else:
                    if StayCount[1] == RogueX:
                        ch_r "Well I guess if she's in, I am too!"
                    elif StayCount[1] == EmmaX:
                        ch_e "I wouldn't want to leave you alone with. . . this."
                    elif StayCount[1] == JeanX:
                        ch_j "Hmm, maybe I should stick around. . ."
                if StayCount[1] == KittyX:
                    ch_k "I- yeah, me neither!"
                elif StayCount[1] == LauraX:
                    ch_l "Fine."
                elif StayCount[1] == StormX:
                    ch_s "Well I suppose I should join you. . ."
                elif StayCount[1] == JubesX:
                    ch_v "Um, yeah, let's do this."

        $ BO = Occupants[:]
        while BO:

            if BO[0].location == bg_current:
                if BO[0] in StayCount:

                    $ BO[0].change_outfit("nude")
                    $ BO[0].Water = 1
                    $ BO[0].spunk = []
                    $ BO[0].recent_history.append("showered")
                    $ BO[0].daily_history.append("showered")
                    call expression BO[0].tag + "_First_Bottomless" pass (1)
                    call expression BO[0].tag + "_First_Topless" pass (1)
                else:

                    call Remove_Girl (BO[0])
                while BO[0] in Nearby:
                    $ Nearby.remove(BO[0])
            $ BO.remove(BO[0])





    call Seen_First_Peen (0, 0, 0, 1)

    while len(StayCount) >= 2 and StayCount[1] in Nearby:

        $ Nearby.remove(StayCount[1])
    while StayCount and StayCount[0] in Nearby:

        $ Nearby.remove(StayCount[0])

    if Nearby and len(StayCount) < 2:

        $ renpy.random.shuffle(Nearby)

        while Nearby and (len(Nearby) + len(StayCount)) > 2:

            $ Nearby.remove(Nearby[0])

        if len(Nearby) >= 2:
            "As you finish getting undressed, [Nearby[0].name] and [Nearby[1].name] enter the room."
            $ Nearby[1].location = bg_current
        else:
            "As you finish getting undressed, [Nearby[0].name] enters the room."
        $ Nearby[0].location = bg_current

        $ BO = Nearby[:]


        call set_the_scene (Dress=0)

        call Seen_First_Peen (0, 0, 1, 1)

        if RogueX in BO:
            if RogueX.SeenPeen == 1:
                $ RogueX.change_face("_surprised",2,Eyes="_down")
                ch_r "Oh!"
                $ RogueX.change_face("_bemused",1,Eyes="_side")
                ch_r "I am so sorry, I should {i}not{/i} have just barged in like that."
            else:
                $ RogueX.change_face("_bemused",1,Eyes="_side")
                ch_r "I simply {i}must{/i} be more careful. . ."
        if KittyX in BO:
            $ KittyX.change_face("_bemused",2,Eyes="_side")
            if KittyX.SeenPeen == 1:
                ch_k "Sorry! Sorry! I need to stop just casually phasing into places!"
            else:
                ch_k "I have {i}got{/i} to knock more. . ."
        if EmmaX in BO:
            if EmmaX.SeenPeen == 1:
                $ EmmaX.change_face("_surprised")
                ch_e "Oh! Dreadfully sorry."
                $ EmmaX.change_face("_sexy",Eyes="_down")
                ch_e "I hope we can meet again under. . . different circumstances."
            else:
                $ EmmaX.change_face("_sexy",Eyes="_down")
                ch_e "I really should pay closer attention. . ."
            if "classcaught" not in EmmaX.history or ((StayCount or len(Nearby) >= 2) and "three" not in EmmaX.history):

                "[EmmaX.name] decides to leave immediately."
                call Remove_Girl (EmmaX)
                $ BO.remove(EmmaX)
                $ EmmaX.change_outfit()
        if LauraX in BO:
            if LauraX.SeenPeen == 1:
                $ LauraX.change_face("_surprised",Eyes="_down")
                ch_l "Hey. That's interesting. . ."
            else:
                $ LauraX.change_face("_normal",Eyes="_down")
                ch_l ". . ."
                $ LauraX.change_face("_normal")
                ch_l "I'm supposed to knock, aren't I."
        if JeanX in BO:
            if JeanX.SeenPeen == 1:
                $ JeanX.change_face("_surprised",Eyes="_down")
                ch_j "Well what do we have here? . ."
            else:
                $ JeanX.change_face("_normal",Eyes="_down")
                ch_j ". . ."
                $ JeanX.change_face("_normal")
                ch_j "Oh, nice to catch you. . . like this. . ."
        if StormX in BO:
            if StormX.SeenPeen == 1:
                $ StormX.change_face("_surprised")
                ch_s "Oh! Hello there."
                $ StormX.change_face("_sexy",Eyes="_down")
                ch_s "And hello to you as well. . ."
            else:
                $ StormX.change_face("_sexy",Eyes="_down")
                ch_s "I'm sorry to intrude. . ."
            $ StormX.change_face("_sexy")
        if JubesX in BO:
            $ JubesX.change_face("_bemused",2,Eyes="_side")
            if JubesX.SeenPeen == 1:
                ch_v "Oh, sorry! I wasn't paying attention."
                $ JubesX.eyes = "_down"
                pause 1
                $ JubesX.eyes = "_side"
                ch_v "um. . . hey. . ."
            else:
                ch_v "Oh, sorry! I wasn't paying attention."

        if EmmaX in StayCount and "three" not in EmmaX.history:

            if len(BO) >= 2:
                "Seeing the other girls arrive, [EmmaX.name] quickly excuses herself."
            else:
                "Seeing [BO[0].name] arrive, [EmmaX.name] quickly excuses herself."
            $ StayCount.remove(EmmaX)
            call Remove_Girl (EmmaX)
            $ EmmaX.change_outfit()

        if BO:

            if approval_check(BO[0], 1200):
                $ StayCount.append(BO[0])
            if len(BO) >=2 and approval_check(BO[1], 1200) and len(StayCount) < 2:
                $ StayCount.append(BO[1])

            if len(BO) >=2:
                if BO[0] not in StayCount and BO[1] not in StayCount:
                    "They both turn right back around."
                    call Remove_Girl (BO[0])
                    call Remove_Girl (BO[1])
                    $ BO = []
                elif BO[0] not in StayCount:
                    "[BO[0].name] turns right back around, but [BO[1].name] stays."
                    call Remove_Girl (BO[0])
                    $ BO.remove(BO[0])
                elif BO[1] not in StayCount:
                    "[BO[1].name] turns right back around, but [BO[0].name] stays."
                    call Remove_Girl (BO[1])
                    $ BO.remove(BO[1])
            elif BO[0] not in StayCount:
                "She turns right back around."
                call Remove_Girl (BO[0])
                $ BO.remove(BO[0])

            while BO:


                $ BO[0].change_outfit("nude")
                $ BO[0].Water = 1
                $ BO[0].spunk = []
                $ BO[0].recent_history.append("showered")
                $ BO[0].daily_history.append("showered")
                call expression BO[0].tag + "_First_Bottomless" pass (1)
                call expression BO[0].tag + "_First_Topless" pass (1)
                if BO[0] == RogueX:
                    ch_r "I wouldn't mind stick'in around though."
                elif BO[0] == KittyX:
                    ch_k "I {i}could{/i} get in on this."
                elif BO[0] == EmmaX:
                    ch_e "But, I could use some face time."
                elif BO[0] == LauraX:
                    ch_l "Scoot over."
                elif BO[0] == JeanX:
                    ch_j "You're hogging the water."
                elif BO[0] == StormX:
                    ch_s "Oh, goodbye then. . ."
                elif BO[0] == JubesX:
                    ch_v "Well, I could always join ya."
                $ BO.remove(BO[0])



    $ Round -= 30 if Round >= 30 else Round
    $ primary_action = 0

    if StayCount:

        if len(StayCount) > 1 and StayCount[0] == StayCount[1]:
            $ StayCount.remove(StayCount[0])
        if len(StayCount) > 1:

            call shift_focus (StayCount[0], StayCount[1])
            "You take a quick shower with [StayCount[0].name] and [StayCount[1].name]."
        else:
            call shift_focus (StayCount[0])
            "You take a quick shower with [StayCount[0].name]."

        call Shower_Sex

        if StayCount[0] == RogueX:

            ch_r "That was real nice, [RogueX.player_petname]."
        elif StayCount[0] == KittyX:

            ch_k "That was. . . nice."
        elif StayCount[0] == EmmaX:

            ch_e "That was. . . distracting."
        elif StayCount[0] == LauraX:

            ch_l "Well that was fun."
        elif StayCount[0] == JeanX:

            ch_j "That was fun."
        elif StayCount[0] == StormX:

            ch_s "Ah, that was relaxing."
        elif StayCount[0] == JubesX:

            ch_v "That was fun, [JubesX.player_petname]."

        if len(StayCount) > 1:

            if StayCount[1] == RogueX:

                ch_r "Yeah."
            elif StayCount[1] == KittyX:

                ch_k "Yeah, I had fun."
            elif StayCount[1] == EmmaX:

                ch_e "Indeed."
            elif StayCount[1] == LauraX:

                ch_l "Yup."
            elif StayCount[1] == JeanX:

                ch_j "Yeah, it was."
            elif StayCount[1] == StormX:

                ch_s "Certainly."
            elif StayCount[1] == JubesX:

                ch_v "Yeah, totally."
    else:


        $ Line = "You take a quick shower" + renpy.random.choice([". It was fairly uneventful.",
                        ". A few people came and went as you did so.",
                        ". That was refreshing."])
        "[Line]"

    $ Player.recent_history.append("showered")
    $ Player.daily_history.append("showered")
    if "scent" in Player.daily_history:
        $ Player.daily_history.remove("scent")

    call Get_Dressed
    if RogueX.location == bg_current:
        $ RogueX.change_outfit("_towel")
    if KittyX.location == bg_current:
        $ KittyX.change_outfit("_towel")
    if EmmaX.location == bg_current:
        $ EmmaX.change_outfit("_towel")
    if LauraX.location == bg_current:
        $ LauraX.change_outfit("_towel")
    if JeanX.location == bg_current:
        $ JeanX.change_outfit("_towel")


    if JubesX.location == bg_current:
        $ JubesX.change_outfit("_towel")

    $ Options = []









    return




label Shower_Sex(Options=0, Line=0):

    if len(StayCount) > 1 and (approval_check(StayCount[1], 1800,Check=1) > approval_check(StayCount[0], 1800,Check=1)):
        $ renpy.random.shuffle(StayCount)
    call shift_focus (StayCount[0])

    $ D20 = renpy.random.randint(1,20)
    $ D20 += 5 if approval_check(StayCount[0], 1800) else 0

    if "showered" in Player.recent_history:
        $ D20 = 0

    $ StayCount[0].change_face("_sly")

    if len(StayCount) > 1 and D20 >= 10:
        "As you do so, both girls press their bodies body up against yours."
        $ Line = StayCount[0].name
        call Close_Launch (StayCount[0], StayCount[1])
    elif D20 >= 5:
        "As you do so, [StayCount[0].name] presses her body up against you."
        $ Line = "She"
        call Close_Launch (StayCount[0])
    else:
        $ Line = renpy.random.choice(["It was fairly uneventful.",
                    "A few people came and went as you did so.",
                    "That was refreshing."])
        "[Line]"
        if len(StayCount) > 1:
            $ StayCount[0].change_stat("lust", 50, 15)
            $ StayCount[1].change_stat("lust", 50, 15)
            $ StayCount[0].change_stat("lust", 90, 10)
            $ StayCount[1].change_stat("lust", 90, 10)
            "You got a good look at them washing off, and they didn't seem to mind the view either."
            $ StayCount[0].GLG(StayCount[1],600,4,1)
            $ StayCount[1].GLG(StayCount[0],600,4,1)
            $ StayCount[0].GLG(StayCount[1],800,2,1)
            $ StayCount[1].GLG(StayCount[0],800,2,1)
        else:
            $ StayCount[0].change_stat("lust", 50, 15)
            $ StayCount[0].change_stat("lust", 90, 10)
            "You got a good look at her washing off, and she didn't seem to mind the view either."
        return

    if Line:
        if len(StayCount) > 1:
            $ StayCount[0].change_stat("lust", 50, 5)
            $ StayCount[0].change_stat("lust", 70, 3)
            $ StayCount[1].change_stat("lust", 50, 5)
            $ StayCount[1].change_stat("lust", 70, 3)
        else:
            $ StayCount[0].change_stat("lust", 50, 6)
            $ StayCount[0].change_stat("lust", 70, 3)
        $ Player.change_stat("focus", 50, 5)
        $ Player.change_stat("focus", 80, 2)
        menu:
            extend ""
            "Continue?":
                pass
            "Stop her." if len(StayCount) < 2:
                $ Line = 0
                call expression StayCount[0].tag + "_Pos_Reset"
                "You take a step back, pulling away from her."
                $ StayCount[0].change_stat("love", 80, -1)
                $ StayCount[0].change_stat("obedience", 80, 5)
                $ StayCount[0].change_stat("inhibition", 80, -1)
                $ StayCount[0].change_face("_sad")
                "She seems a bit disappointed."
            "Stop them." if len(StayCount) > 1:
                $ Line = 0
                call expression StayCount[1].tag + "_Pos_Reset"
                call expression StayCount[0].tag + "_Pos_Reset"
                "You take a step back, pulling away from them."
                $ StayCount[0].change_stat("love", 80, -1)
                $ StayCount[0].change_stat("obedience", 80, 5)
                $ StayCount[0].change_stat("inhibition", 80, -1)
                $ StayCount[1].change_stat("obedience", 80, 5)
                $ StayCount[1].change_stat("inhibition", 80, -1)
                $ StayCount[0].change_face("_sad")
                $ StayCount[1].change_face("_sad")
                "They seem a bit disappointed."
    if Line:

        $ Options = [1]
        if len(StayCount) > 1:
            if approval_check(StayCount[0], 1300) and StayCount[0].GirlLikeCheck(StayCount[1]) >= 800:
                $ Options.append(2)
            if approval_check(StayCount[0], 1200) and StayCount[0].GirlLikeCheck(StayCount[1]) >= 700:
                $ Options.append(3)

        if approval_check(StayCount[0], 1300):
            $ Options.append(4)
        if approval_check(StayCount[0], 1400):
            $ Options.append(5)

        if approval_check(StayCount[0], 1300):
            $ Options.append(6)
        if approval_check(StayCount[0], 1200):
            $ Options.append(7)

        if not approval_check(StayCount[0], 1400):

            if approval_check(StayCount[0], 1000):
                $ Options.append(8)
            if approval_check(StayCount[0], 1100):
                $ Options.append(9)
            if approval_check(StayCount[0], 1000):
                $ Options.append(10)
            if approval_check(StayCount[0], 1100):
                $ Options.append(11)

        $ renpy.random.shuffle(Options)



        if Options[0] == 2:
            $ StayCount[0].change_stat("lust", 50, 5)
            $ StayCount[0].change_stat("lust", 70, 2)
            $ StayCount[1].change_stat("lust", 50, 7)
            $ StayCount[1].change_stat("lust", 70, 3)
            $ Player.change_stat("focus", 50, 8)
            $ Player.change_stat("focus", 80, 4)
            "[Line] reaches over to [StayCount[1].name] and begins soaping up her chest."
        elif Options[0] == 3:
            $ StayCount[0].change_stat("lust", 50, 7)
            $ StayCount[0].change_stat("lust", 70, 3)
            $ StayCount[1].change_stat("lust", 50, 8)
            $ StayCount[1].change_stat("lust", 70, 4)
            $ Player.change_stat("focus", 50, 8)
            $ Player.change_stat("focus", 80, 5)
            "[Line] reaches over to [StayCount[1].name] and begins soaping up her pussy."


        elif Options[0] == 4:
            if len(StayCount) > 1:
                $ StayCount[0].change_stat("lust", 50, 10)
                $ StayCount[0].change_stat("lust", 70, 7)
            else:
                $ StayCount[0].change_stat("lust", 50, 8)
                $ StayCount[0].change_stat("lust", 70, 5)
            $ Player.change_stat("focus", 50, 10)
            $ Player.change_stat("focus", 80, 6)
            "[Line] reaches down and takes your cock in her hand, soaping it up."
        elif Options[0] == 5:
            if len(StayCount) > 1:
                $ StayCount[0].change_stat("lust", 50, 12)
                $ StayCount[0].change_stat("lust", 70, 8)
            else:
                $ StayCount[0].change_stat("lust", 50, 9)
                $ StayCount[0].change_stat("lust", 70, 6)
            $ Player.change_stat("focus", 50, 10)
            $ Player.change_stat("focus", 80, 4)
            "[Line] kneels down and wraps her breasts around your cock, soaping it up."


        elif Options[0] == 6:
            if len(StayCount) > 1:
                $ StayCount[0].change_stat("lust", 50, 11)
                $ StayCount[0].change_stat("lust", 70, 6)
            else:
                $ StayCount[0].change_stat("lust", 50, 9)
                $ StayCount[0].change_stat("lust", 70, 5)
            $ Player.change_stat("focus", 50, 9)
            $ Player.change_stat("focus", 80, 4)
            "[Line] reaches down and begins fondling her own pussy, building a nice lather."
        elif Options[0] == 7:
            if len(StayCount) > 1:
                $ StayCount[0].change_stat("lust", 50, 10)
                $ StayCount[0].change_stat("lust", 70, 5)
            else:
                $ StayCount[0].change_stat("lust", 50, 9)
                $ StayCount[0].change_stat("lust", 70, 4)
            $ Player.change_stat("focus", 50, 8)
            $ Player.change_stat("focus", 80, 3)
            "[Line] begins rubbing her own breasts in circles, building a nice lather."


        elif Options[0] == 8:
            $ StayCount[0].change_stat("lust", 50, 6)
            $ StayCount[0].change_stat("lust", 70, 3)
            $ Player.change_stat("focus", 50, 7)
            $ Player.change_stat("focus", 80, 3)
            "[Line] draws her breasts up and down your arm, the soap bubbles squirting out."
        elif Options[0] == 9:
            $ StayCount[0].change_stat("lust", 50, 8)
            $ StayCount[0].change_stat("lust", 70, 3)
            $ Player.change_stat("focus", 50, 8)
            $ Player.change_stat("focus", 80, 3)
            "[Line] kneels down and rubs her breasts against your leg, soaping it up."
        elif Options[0] == 10:
            $ StayCount[0].change_stat("lust", 50, 7)
            $ StayCount[0].change_stat("lust", 70, 3)
            $ Player.change_stat("focus", 50, 6)
            $ Player.change_stat("focus", 80, 3)
            "[Line] presses against your back, her soapy breasts rubbing back and forth against it."
        elif Options[0] == 11:
            $ StayCount[0].change_stat("lust", 50, 7)
            $ StayCount[0].change_stat("lust", 70, 3)
            $ Player.change_stat("focus", 50, 8)
            $ Player.change_stat("focus", 80, 4)
            "[Line] presses against your chest, her soapy breasts rubbing back and forth against it."
        elif Options[0] == 1:
            $ StayCount[0].change_stat("lust", 50, 5)
            $ StayCount[0].change_stat("lust", 70, 2)
            $ Player.change_stat("focus", 50, 6)
            $ Player.change_stat("focus", 80, 3)
            "[Line] stares silently at you as she moves her hands along her soapy body. . ."
            $ Line = 0

    if Line and len(StayCount) > 1:

        $ D20 += 5 if approval_check(StayCount[1], 1800) else 0
        if StayCount[1].GirlLikeCheck(StayCount[0]) <= 800 and 2 <= Options[0] <=3:
            $ D20 -= 5
        if StayCount[1].GirlLikeCheck(StayCount[0]) <= 600:
            $ D20 -= 5

        if 2 <= Options[0] <= 3:

            if approval_check(StayCount[1], 1300) and StayCount[1].GirlLikeCheck(StayCount[0]) >= 800:
                $ StayCount[1].change_face("_sexy",1)
                $ StayCount[0].change_stat("lust", 50, 5)
                $ StayCount[0].change_stat("lust", 70, 5)
                $ StayCount[1].change_stat("lust", 50, 12)
                $ StayCount[1].change_stat("lust", 70, 12)
                call Close_Launch (StayCount[0], StayCount[1])
                "[StayCount[1].name] seems really into this, and returns the favor."
                $ Player.change_stat("focus", 50, 7)
                $ Player.change_stat("focus", 80, 3)
                $ Line = 4
            elif approval_check(StayCount[1], 1200) and StayCount[1].GirlLikeCheck(StayCount[0]) >= 700:
                $ StayCount[1].change_face("_sexy",2,Eyes="_closed")
                $ StayCount[1].change_stat("lust", 50, 10)
                $ StayCount[1].change_stat("lust", 70, 10)
                $ Player.change_stat("focus", 50, 5)
                $ Player.change_stat("focus", 80, 3)
                call Close_Launch (StayCount[0], StayCount[1])
                "[StayCount[1].name] seems really into this, and leans into it."
            else:
                $ StayCount[1].change_stat("lust", 50, 10)
                $ StayCount[1].change_face("_sadside",Brows="_confused")
                "[StayCount[1].name] doesn't really seem to appreciate this."
                "She pulls away."
                $ Line = 3
        else:

            if (approval_check(StayCount[1], 1300) and StayCount[1].GirlLikeCheck(StayCount[0]) >= 700) or approval_check(StayCount[1], 2000):
                if Options[0] == 5:
                    $ StayCount[1].change_stat("lust", 50, 10)
                    $ StayCount[1].change_stat("lust", 70, 5)
                    $ Player.change_stat("focus", 50, 6)
                    $ Player.change_stat("focus", 80, 3)
                    call Close_Launch (StayCount[0], StayCount[1])
                    "[StayCount[1].name] seems really into this, slowly rubbing against you as she watches."
                else:
                    $ StayCount[1].change_stat("lust", 50, 10)
                    $ StayCount[1].change_stat("lust", 70, 5)
                    $ Player.change_stat("focus", 50, 5)
                    $ Player.change_stat("focus", 80, 3)
                    call Close_Launch (StayCount[0], StayCount[1])
                    "[StayCount[1].name] seems really into this, and joins her on the other side."
                $ Line = 4
            elif ((approval_check(StayCount[1], 1200) and StayCount[1].GirlLikeCheck(StayCount[0]) >= 600)) or approval_check(StayCount[1], 1600):
                $ StayCount[1].change_face("_sexy",2,Eyes="_down")
                $ StayCount[1].change_stat("lust", 50, 10)
                $ StayCount[1].change_stat("lust", 70, 5)
                "[StayCount[1].name] seems really into this, and watches her do it."
            else:
                $ StayCount[1].change_face("_sadside",Brows="_confused")
                $ StayCount[1].change_stat("lust", 50, 5)
                "[StayCount[1].name] doesn't really seem to appreciate this."
                $ Line = 3
    if Line:
        menu:
            extend ""
            "Continue?":
                pass
            "Stop her." if len(StayCount) < 2:
                $ Line = 0
                call expression StayCount[0].tag + "_Pos_Reset"
                "You take a step back, pulling away from her."
                $ StayCount[0].change_stat("love", 80, -2)
                $ StayCount[0].change_stat("obedience", 80, 5)
                $ StayCount[0].change_stat("inhibition", 80, -2)
                $ StayCount[0].change_face("_sad")
                "She seems a bit disappointed."
            "Stop them." if len(StayCount) > 1:
                $ Line = 0
                call expression StayCount[1].tag + "_Pos_Reset"
                call expression StayCount[0].tag + "_Pos_Reset"
                "You take a step back, pulling away from them."
                $ StayCount[0].change_face("_sad")
                $ StayCount[0].change_stat("love", 80, -2)
                $ StayCount[0].change_stat("obedience", 80, 5)
                $ StayCount[0].change_stat("inhibition", 80, -2)
                if Line == 3:
                    $ StayCount[1].change_stat("love", 80, 4)
                    $ StayCount[1].change_stat("obedience", 80, 5)
                    $ StayCount[1].change_face("_bemused")
                    "[StayCount[0].name] seems a bit disappointed, but [StayCount[1].name] seems pleased."
                else:
                    $ StayCount[1].change_stat("love", 80, -1)
                    $ StayCount[1].change_stat("obedience", 80, 5)
                    $ StayCount[1].change_stat("inhibition", 80, -1)
                    $ StayCount[1].change_face("_sad")
                    "They seem a bit disappointed."

    if Line:

        if len(StayCount) > 1 and Line != 3:
            $ StayCount[0].GLG(StayCount[1],600,4,1)
            $ StayCount[1].GLG(StayCount[0],600,4,1)
            $ StayCount[0].GLG(StayCount[1],800,3,1)
            $ StayCount[1].GLG(StayCount[0],800,3,1)
            $ StayCount[0].GLG(StayCount[1],900,1,1)
            $ StayCount[1].GLG(StayCount[0],900,1,1)
        if 2 <= Options[0] <= 3 and D20 >= 15:

            $ StayCount[1].GLG(StayCount[0],900,4,1)
            $ Player.change_stat("focus", 50, 10)
            $ Player.change_stat("focus", 80, 5)
            "After a few minutes of this, it looks like [StayCount[1].name] gets off."
            call Girl_Cumming (StayCount[1], 1)
            if Line == 4:
                $ StayCount[0].GLG(StayCount[1],900,3,1)
                "It looks like [StayCount[0].name] is reacting positively to it as well. . ."
                call Girl_Cumming (StayCount[0], 1)
            if len(StayCount) > 1:
                "The girls take a step back."
                call expression StayCount[1].tag + "_Pos_Reset"
            else:
                "[StayCount[0].name] takes a step back."
            call expression StayCount[0].tag + "_Pos_Reset"

        elif 4 <= Options[0] <= 5 and D20 >= 10:

            $ Player.focus = 15
            if Options[0] == 5:
                $ StayCount[0].spunk.append("tits")

            if Line == 4:
                $ StayCount[0].change_stat("inhibition", 90, 7)
                $ StayCount[1].change_stat("inhibition", 90, 4)
                $ StayCount[0].GLG(StayCount[1],900,3,1)
                $ StayCount[1].GLG(StayCount[0],900,3,1)
                "After a few minutes of this, the two of them manage to get you off."
            else:
                $ StayCount[0].change_stat("inhibition", 90, 5)
                "After a few minutes of this, she manages to get you off."
            "A little more work is needed to clean up the mess."
            if Options[0] == 5:
                $ StayCount[0].spunk = []
            if len(StayCount) > 1:
                "The girls take a step back."
                call expression StayCount[1].tag + "_Pos_Reset"
            else:
                "[StayCount[0].name] takes a step back."
            call expression StayCount[0].tag + "_Pos_Reset"

        elif 6 <= Options[0] <= 7 and D20 >= 15:

            $ StayCount[0].change_stat("inhibition", 90, 7)
            $ Player.change_stat("focus", 50, 15)
            $ Player.change_stat("focus", 80, 5)
            "After a few minutes of this, it looks like [StayCount[0].name] gets off."
            call Girl_Cumming (StayCount[0], 1)
            if Line == 4:
                $ StayCount[1].change_stat("inhibition", 90, 6)
                $ StayCount[0].GLG(StayCount[1],900,3,1)
                "It looks like [StayCount[1].name] is enjoying herself as well. . ."
                call Girl_Cumming (StayCount[1], 1)
            if len(StayCount) > 1:
                $ StayCount[1].GLG(StayCount[0],900,3,1)
                "The girls take a step back."
                call expression StayCount[1].tag + "_Pos_Reset"
            else:
                "[StayCount[0].name] takes a step back."
            call expression StayCount[0].tag + "_Pos_Reset"
        else:

            if len(StayCount) > 1:
                call expression StayCount[1].tag + "_Pos_Reset"
            call expression StayCount[0].tag + "_Pos_Reset"
            $ Player.change_stat("focus", 50, 15)
            $ Player.change_stat("focus", 80, 5)
            if D20 >= 15:
                "After a minute or two, it sounds like someone is coming, so you scramble apart."
                "Disappointing. . ."
            elif D20 >= 10:
                "After a minute or two, she seems satisfied with her efforts, and pulls back."
                if 4 <= Options[0] <= 5:
                    "You're left pretty hard."
            else:
                "After a minute or so of this, she draws back and finshes washing herself off."
                if 4 <= Options[0] <= 5:
                    "You're left pretty hard."
    call shift_focus (StayCount[0])
    return
