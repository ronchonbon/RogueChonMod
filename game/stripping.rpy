label Group_Strip(Girl=0, approval_bonus=approval_bonus, approval_bonusP=[0,0], temp_Girls=[]):

    $ Present = []
    $ temp_Girls = all_Girls[:]
    while temp_Girls:
        if temp_Girls[0].location == bg_current:
            $ Present.append(temp_Girls[0])
        $ temp_Girls.remove(temp_Girls[0])

    if not Present:
        "Nobody's here."
        "You dance alone."
        return

    while len(Present) > 2:

        call remove_girl (Present[2])


    if len(Present) == 2:
        $ renpy.random.shuffle(Present)
        if Girl and Present[0] != Girl:
            $ Party.reverse()
        elif approval_check(Present[0],Check=1) <= approval_check(Present[1],Check=1):

            $ Present.reverse()

    call shift_focus (Present[0])

    $ round -= 5 if round > 5 else (round-1)
    call set_the_scene (1, 0, 0, 0)

    $ Present[0].change_face("_sexy",1)
    if len(Present) >= 2:
        if Present[1] in all_Girls:
            $ Present[1].change_face("_sexy",1)
        else:
            $ Present.remove(Present[1])

    $ counter = len(Present)
    while counter:
        $ counter -= 1
        if Girl == EmmaX and "classcaught" in EmmaX.recent_history and AloneCheck(EmmaX):

            pass
        elif not approval_check(Present[counter], 600, taboo_modifier = 1,Alt=[[EmmaX],(650+taboo*10)]) or (Present[counter] == EmmaX and taboo and "taboo" not in EmmaX.history):
            if not approval_check(Present[counter], 400):
                if Present[counter] == RogueX:
                    ch_r "I'm just some sort'a gogo dancer now?"
                elif Present[counter] == KittyX:
                    ch_k "Like I would just dance for you?"
                elif Present[counter] == EmmaX:
                    ch_e "Oh, you think I'll dance to your tune?"
                elif Present[counter] == LauraX:
                    ch_l "I don't dance."
                elif Present[counter] == JeanX:
                    ch_j "I'm not in the mood."
                elif Present[counter] == StormX:
                    ch_s "I do not dance."
                elif Present[counter] == JubesX:
                    ch_v "I don't wanna dance, weirdo. . ."
            elif Present[counter].taboo:
                if Present[counter] == RogueX:
                    ch_r "I don't think this is the best place for dance'n."
                elif Present[counter] == KittyX:
                    ch_k "I don't know, this really isn't a good place for it?"
                elif Present[counter] == EmmaX:
                    ch_e "You must be joking. Here?"
                elif Present[counter] == LauraX:
                    if approval_check(LauraX, 600, taboo_modifier = 0):
                        $ Present.append(LauraX)
                    else:
                        ch_l "I don't feel like it."
                elif Present[counter] == JeanX:
                    ch_j "I don't want to just randomly dance in public."
                elif Present[counter] == StormX:
                    ch_s "I would not want to make a scene."
                elif Present[counter] == JubesX:
                    ch_v "This isn't really the place for it. . ."
            else:
                if Present[counter] == RogueX:
                    ch_r "I dont feel it right now."
                elif Present[counter] == KittyX:
                    ch_k "I don't know, I don't really feel like dancing right now."
                elif Present[counter] == EmmaX:
                    ch_e "I don't really feel like dancing at the moment."
                elif Present[counter] == LauraX:
                    ch_l "I don't feel like it."
                elif Present[counter] == JeanX:
                    ch_j "I'm not in the mood."
                elif Present[counter] == StormX:
                    ch_s "I do not wish to dance right now."
                elif Present[counter] == JubesX:
                    ch_v "Yeah, I don't feel like dancing right now. . ."
            $ Present.remove(Present[counter])

    if not Present:
        return

    if EmmaX.location == bg_current and EmmaX not in Present:

        if "classcaught" not in EmmaX.history:
            if EmmaX.location == EmmaX.home:

                ch_e "If the two of you would like to dance, please do it elsewhere."
                $ Present = []
                return
            else:
                ch_e "I should really be going."
                call remove_girl (EmmaX)

    if "stripping" in Present[0].daily_history and approval_check(Present[0], 500, taboo_modifier = 3):
        $ line = renpy.random.choice(["You liked the show earlier?",
                    "Didn't get enough earlier?",
                    "You're going to wear me out."])
    else:
        $ line = renpy.random.choice(["Ok, that sounds fun.",
                    "I could get into that.",
                    "Yeah, ok."])

    Present[0].voice "[line]"
    $ line = 0

    $ temp_Girls = all_Girls[:]

    while temp_Girls:
        call reset_position(temp_Girls[0])

        $ temp_Girls.remove(temp_Girls[0])

    $ counter = len(Present)
    while counter:
        $ counter -= 1
        if Present[counter] == RogueX:
            show Rogue_sprite standing at Girl_Dance1(RogueX)
        elif Present[counter] == KittyX:
            show Kitty_sprite standing at Girl_Dance1(KittyX)
        elif Present[counter] == EmmaX:
            show Emma_sprite standing at Girl_Dance1(EmmaX)
        elif Present[counter] == LauraX:
            show Laura_sprite standing at Girl_Dance1(LauraX)
        elif Present[counter] == JeanX:
            show Jean_sprite standing at Girl_Dance1(JeanX)
        elif Present[counter] == StormX:
            show Storm_sprite standing at Girl_Dance1(StormX)
        elif Present[counter] == JubesX:
            show Jubes_sprite standing at Girl_Dance1(JubesX)
        $ Present[counter].recent_history.append("stripping")
        $ Present[counter].daily_history.append("stripping")
        $ Present[counter].action_counter["striptease"] += 1
        $ Present[counter].remaining_actions -= 1
        $ approval_bonusP[counter] = approval_bonus
        if Present[counter].seen_breasts or Present[counter].seen_pussy:

            $ approval_bonusP[counter] += 20
        if Present[counter].seen_underwear:

            $ approval_bonusP[counter] += 5
        if "exhibitionist" in Present[counter].traits:
            $ approval_bonusP[counter] += (4*taboo)
        if ("sex friend" in Present[counter].player_petnames or Present[counter] in Player.Harem) and not taboo:
            $ approval_bonusP[counter] += 15
        elif "ex" in Present[counter].traits:
            $ approval_bonusP[counter] -= 40
        elif Present[counter].event_counter["forced"] and not Present[counter].forced:
            $ approval_bonusP[counter] -= 5*Present[counter].event_counter["forced"]

    if len(Present) >= 2:
        "They start to dance."
        $ Partner = Present[1]
        $ between_event_count = 1
    else:
        "She starts to dance."
        $ between_event_count = 0
        $ Partner = 0


    if Girl == EmmaX and "classcaught" in EmmaX.recent_history and AloneCheck(EmmaX):

        $ Count = 0
        jump Group_Stripping


    $ temp_Girls = all_Girls[:]
    while temp_Girls:
        if temp_Girls[0].location == bg_current and temp_Girls[0] not in Present:
            $ Present.append(temp_Girls[0])
            if "stopdancing" not in temp_Girls[0].recent_history:
                $ temp_Girls[0].recent_history.append("stopdancing")
        $ temp_Girls.remove(temp_Girls[0])

    $ approval_bonus = approval_bonusP[0]
    $ primary_action = "striptease"
    $ Count = 1

    while Count and round >=10:

        $ round -= 2 if round > 2 else round
        if len(Present) >= 2:
            $ Present[0].check_if_likes(Present[1],600,1,1)
            $ Present[1].check_if_likes(Present[0],600,1,1)
        menu:
            "Continue":
                pass
            "Would you kindly take off some clothes?":

                Present[0].voice "Hmm?"
                $ Count = 0
            "Stop":
                jump Group_Strip_End


    if EmmaX.location == bg_current and len(Present) >= 2:

        if "classcaught" not in EmmaX.history or "threesome" not in EmmaX.history or (taboo and "taboo" not in EmmaX.history):
            if EmmaX.location == "bg_emma":

                ch_e "If the two of you would like to get indecent, please do it elsewhere."
                $ Present = []
                return
            else:
                ch_e "I should really be going."
                call remove_girl (EmmaX)

label Group_Stripping:
    while round >= 10 and Present:
        $ round -= 2 if round > 2 else round

        if Present[Count] != focused_Girl:
            call shift_focus (Present[Count])

        call Girl_Stripping (Present[Count])

        if len(Present) < 2 and Count != 0:
            $ Count = 0
        if not Present or not Present[Count]:
            jump Group_Strip_End
        if "stopdancing" in Present[Count].recent_history:

            if len(Present) >= 2 and "stopdancing" in Present[0].recent_history and "stopdancing" in Present[1].recent_history:
                jump Group_Strip_End

        $ primary_action = "striptease"

        if not Present:

            jump Group_Strip_End

        if len(Present) >= 2 and Count != between_event_count:
            $ Present[Count].check_if_likes(Present[between_event_count],800,2,1)
            $ Present[between_event_count].check_if_likes(Present[Count],800,2,1)

        if len(Present) >= 2:


            if Count == 0 and "stopdancing" not in Present[1].recent_history:
                $ Count = 1
                $ between_event_count = 0
                $ approval_bonusP[1] = approval_bonus
                $ approval_bonus = approval_bonusP[0]
            elif Count == 1 and "stopdancing" not in Present[0].recent_history:
                $ Count = 0
                $ between_event_count = 1
                $ approval_bonusP[0] = approval_bonus
                $ approval_bonus = approval_bonusP[1]
            call shift_focus (Present[Count])


            call Activity_Check (focused_Girl, Partner)

        if len(Present) < 2 or "stopdancing" in Present[1].recent_history:

            $ approval_bonus = approval_bonusP[Count]
            $ Count = 0
            $ between_event_count = 0
            $ Partner = 0

            call Activity_Check (focused_Girl, Partner)

            if not Present or "stopdancing" in Present[0].recent_history:
                jump Group_Strip_End

    if Present and round <=15:
        Present[0].voice "It's getting late, we should probably take a break."

label Group_Strip_End:

    if Present:
        $ Present[0].drain_word("stopdancing",1,0,0)
        $ Present[0].drain_word("keepdancing",1,0,0)
    if len(Present) >= 2:
        $ Present[1].drain_word("stopdancing",1,0,0)
        $ Present[1].drain_word("keepdancing",1,0,0)

    call set_the_scene (1, 0, 0, 0)
    $ Count = 0
    $ between_event_count = 0

    return




label Girl_Stripping(Girl=0, Nudist=0):

    if "stopdancing" in Girl.recent_history:

        return

    $ Girl.arm_pose = 2
    $ Girl.lust_face(1)

    if Girl == StormX and (StormX in Rules or Girl.taboo <= 20):

        if Girl.forced:
            $ Nudist = -40
        else:
            $ Nudist = Girl.taboo
    if "keepdancing" not in Girl.recent_history:

        if Girl == JubesX and Girl.outfit["front_outer_accessory"] and (Girl.outfit["top"] or Girl.outfit["bra"]) and (Girl.outfit["underwear"] or Girl.outfit["bottom"] or Girl.hose_number() >= 10):

            if approval_check(Girl, 750, taboo_modifier = 3):
                $ Girl.change_stat("obedience", 50, 1)
                $ Girl.change_stat("inhibition", 25, 1)
                $ Player.change_stat("focus", 60, 3)
                $ line = Girl.outfit["front_outer_accessory"]
                $ Girl.outfit["front_outer_accessory"] = ""
                "She shrugs off her [line] and throws it behind her."
            else:
                jump Strip_Ultimatum
        elif Girl == JubesX and Girl.outfit["front_outer_accessory"] and Girl.outfit["top"] and (Girl.outfit["underwear"] or Girl.outfit["bottom"] or Girl.hose_number() >= 10):

            if approval_check(Girl, 750, taboo_modifier = 3):
                $ Girl.change_stat("obedience", 50, 1)
                $ Girl.change_stat("inhibition", 25, 1)
                $ Player.change_stat("focus", 60, 3)
                $ line = Girl.outfit["front_outer_accessory"]
                $ Girl.outfit["front_outer_accessory"] = ""
                "She shrugs off her [line] and throws it behind her."
            else:
                jump Strip_Ultimatum
        elif Girl.outfit["top"] and Girl.outfit["bra"] and (Girl.outfit["underwear"] or Girl.outfit["bottom"] or Girl.hose_number() >= 10):

            if approval_check(Girl, 750, taboo_modifier = 3,Alt=[[StormX],(300-Nudist*3)]):
                $ Girl.change_stat("obedience", 50, 1)
                $ Girl.change_stat("inhibition", 25, 1)
                $ Player.change_stat("focus", 60, 3)
                $ line = Girl.outfit["top"]
                $ Girl.outfit["top"] = ""
                if Girl == KittyX:
                    "She drops her shoulders and her [line] falls to the floor."
                else:
                    "She pulls her [line] over her head and throws it behind her."
            else:
                jump Strip_Ultimatum

        elif Girl.outfit["bottom"] and (Girl.outfit["underwear"] or Girl.hose_number() >= 10):

            if approval_check(Girl, 1200, taboo_modifier = 3,Alt=[[StormX],(600-Nudist*3)]) or (Girl.seen_underwear and approval_check(Girl, 900, taboo_modifier = 3) and not Girl.taboo):
                $ Girl.change_stat("lust", 50, 5)
                $ Girl.change_stat("obedience", 50, 1)
                $ Girl.change_stat("inhibition", 30, 1)
                $ Player.change_stat("focus", 60, 5)
                $ line = Girl.outfit["bottom"]
                $ Girl.outfit["bottom"] = ""
                if Girl == KittyX:
                    "Her [line] slide through her legs until they're only on her toes, before she kicks them to the floor."
                else:
                    "She unzips and pulls down her [line], dropping them to the floor."
                if not Girl.seen_underwear:
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("obedience", 200, 3)
                    $ Girl.change_stat("inhibition", 50, 3)
                    $ Girl.change_stat("inhibition", 200, 2)
                    $ Girl.seen_underwear = 1
            else:
                jump Strip_Ultimatum

        elif Girl.outfit["hose"]:

            if Girl.hose_number() >= 10:
                if approval_check(Girl, 1200, taboo_modifier = 3):
                    $ Girl.change_stat("lust", 50, 6)
                    $ Player.change_stat("focus", 60, 6)
                else:
                    jump Strip_Ultimatum

            elif Girl.hose_number() >= 6 and approval_check(Girl, 1200, taboo_modifier = 3):
                if approval_check(Girl, 1200, taboo_modifier = 3,Alt=[[StormX],(600-Nudist*3)]):
                    $ Girl.change_stat("lust", 50, 4)
                    $ Player.change_stat("focus", 60, 4)
                else:
                    jump Strip_Ultimatum
            else:
                $ Player.change_stat("focus", 60, 3)
            $ line = Girl.outfit["hose"]
            $ Girl.outfit["hose"] = ""
            if Girl == KittyX:
                "Her [line] slide down off her legs, leaving them in a small pile."
            else:
                "She rolls the [line] down off her legs, leaving them in a small pile."
            call expression Girl.tag + "_First_Bottomless" pass (1)

        elif Girl == JubesX and Girl.outfit["front_outer_accessory"] and (Girl.outfit["underwear"] or Girl.outfit["bottom"] or Girl.hose_number() >= 10):

            if approval_check(Girl, 1250, taboo_modifier = 3) or (Girl.seen_breasts and approval_check(Girl, 1000, taboo_modifier = 3) and not Girl.taboo):
                $ Girl.change_stat("lust", 60, 5)
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("inhibition", 50, 10)
                $ Player.change_stat("focus", 80, 15)
                $ line = Girl.outfit["front_outer_accessory"]
                $ Girl.outfit["front_outer_accessory"] = ""
                "She shrugs off her [line] and throws it behind her."
                if not Girl.seen_breasts:
                    $ Girl.change_face("_bemused", 1)
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_stat("obedience", 200, 4)
                    $ Girl.change_stat("inhibition", 50, 3)
                    $ Girl.change_stat("inhibition", 200, 3)
                    "She hesitantly glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                    call expression Girl.tag + "_First_Topless" pass (1)
            else:
                jump Strip_Ultimatum
        elif Girl.outfit["top"] and not Girl.outfit["bra"] and (Girl.outfit["underwear"] or Girl.hose_number() >= 10):

            if approval_check(Girl, 1250, taboo_modifier = 3,Alt=[[StormX],(650-Nudist*3)]) or (Girl.seen_breasts and approval_check(Girl, 1000, taboo_modifier = 3) and not Girl.taboo):
                $ Girl.change_stat("lust", 60, 5)
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("inhibition", 50, 10)
                $ Player.change_stat("focus", 80, 15)
                $ line = Girl.outfit["top"]
                $ Girl.outfit["top"] = ""
                if not Girl.seen_breasts:
                    $ Girl.change_face("_bemused", 1)
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_stat("obedience", 200, 4)
                    $ Girl.change_stat("inhibition", 50, 3)
                    $ Girl.change_stat("inhibition", 200, 3)
                    if Girl == KittyX:
                        "She hesitantly glances your way, and then with tug her [line] passes through her, tossing it to the ground."
                    elif Girl in (EmmaX,LauraX,StormX):
                        "She glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                    else:
                        "She hesitantly glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                    call expression Girl.tag + "_First_Topless" pass (1)
                else:
                    if Girl == KittyX:
                        "She drops her shoulders and her [line] falls to the floor."
                    else:
                        "She pulls her [line] over her head, tossing it to the ground."
            else:
                jump Strip_Ultimatum

        elif Girl.outfit["bra"] and not Girl.outfit["top"]:

            if approval_check(Girl, 1250, taboo_modifier = 3,Alt=[[StormX],(650-Nudist*3)]) or (Girl.seen_breasts and approval_check(Girl, 1000, taboo_modifier = 3) and not Girl.taboo):
                $ Girl.change_stat("lust", 60, 5)
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("inhibition", 50, 1)
                $ Player.change_stat("focus", 80, 15)
                $ line = Girl.outfit["bra"]
                $ Girl.outfit["bra"] = ""
                if not Girl.seen_breasts:
                    $ Girl.change_face("_bemused", 1)
                    if Girl == KittyX:
                        "She hesitantly glances your way, and then with a shrug pulls her [line] through herself, tossing it to the ground."
                    elif Girl in (EmmaX,LauraX,StormX):
                        "She glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                    else:
                        "She hesitantly glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_stat("obedience", 200, 4)
                    $ Girl.change_stat("inhibition", 50, 3)
                    $ Girl.change_stat("inhibition", 200, 3)
                    call expression Girl.tag + "_First_Topless" pass (1)
                else:
                    $ Girl.change_face("_sexy")
                    if Girl == KittyX:
                        "She pulls her [line] through herself, tossing it to the ground."
                    else:
                        "She pulls her [line] over her head, tossing it to the ground."
            else:
                jump Strip_Ultimatum

        elif Girl.outfit["bottom"]:

            if approval_check(Girl, 1350, taboo_modifier = 3,Alt=[[StormX],(800-Nudist*3)]) or (Girl.seen_pussy and approval_check(Girl, 1100, taboo_modifier = 3) and not Girl.taboo):
                $ Girl.change_stat("lust", 75, 10)
                $ line = Girl.outfit["bottom"]
                $ Girl.outfit["bottom"] = ""
                if not Girl.seen_pussy:
                    $ Girl.change_stat("obedience", 60, 3)
                    $ Girl.change_stat("obedience", 200, 5)
                    $ Girl.change_stat("inhibition", 50, 4)
                    $ Girl.change_stat("inhibition", 200, 4)
                    if Girl == KittyX:
                        "She shyly looks up at you, and then slowly lets her [line] slide to the floor."
                    elif Girl in (EmmaX,LauraX,JeanX):
                        "She hesitantly looks up at you, and then slowly unzips and pulls down her [line], dropping them to the floor."
                    else:
                        "She shyly looks up at you, and then slowly unzips and pulls down her [line], dropping them to the floor."
                    call expression Girl.tag + "_First_Bottomless" pass (1)
                else:
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Girl.change_stat("obedience", 75, 1)
                    if Girl == KittyX:
                        "She lets her [line] pass through her legs, dropping them to the floor."
                    else:
                        "She unzips and pulls down her [line], dropping them to the floor."
                    $ Girl.change_stat("inhibition", 70, 2)
                $ Player.change_stat("focus", 85, 15)
            else:
                jump Strip_Ultimatum

        elif Girl == JubesX and Girl.outfit["front_outer_accessory"]:

            if approval_check(Girl, 1350, taboo_modifier = 3) or (Girl.seen_pussy and approval_check(Girl, 1100, taboo_modifier = 3) and not Girl.taboo):
                $ line = Girl.outfit["front_outer_accessory"]
                $ Girl.outfit["front_outer_accessory"] = ""
                if not Girl.seen_pussy:
                    $ Girl.change_stat("obedience", 60, 3)
                    $ Girl.change_stat("obedience", 200, 5)
                    $ Girl.change_stat("inhibition", 50, 4)
                    $ Girl.change_stat("inhibition", 200, 4)
                    "She hesitantly glances your way, and then with a shrug pulls her [line] off, tossing it to the ground."
                    call expression Girl.tag + "_First_Bottomless" pass (1)
                else:
                    "She shrugs her [line] off, tossing it to the ground."

                if not Girl.outfit["bra"] or Girl.top_pulled_up:
                    if not Girl.seen_breasts:
                        $ Girl.change_stat("obedience", 50, 3)
                        $ Girl.change_stat("inhibition", 50, 3)
                        call expression Girl.tag + "_First_Topless" pass (1)
                    else:
                        $ Girl.change_stat("lust", 60, 15)
                        $ Girl.change_stat("obedience", 50, 3)
                        $ Girl.change_stat("obedience", 75, 1)
                        $ Girl.change_stat("inhibition", 50, 3)
                else:
                    $ Girl.change_stat("lust", 75, 10)
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Girl.change_stat("obedience", 75, 1)
                    $ Girl.change_stat("inhibition", 70, 2)
                $ Player.change_stat("focus", 85, 15)
            else:
                jump Strip_Ultimatum
        elif Girl.outfit["top"] and not Girl.outfit["underwear"]:

            if approval_check(Girl, 1350, taboo_modifier = 3,Alt=[[StormX],(800-Nudist*3)]) or (Girl.seen_pussy and approval_check(Girl, 1100, taboo_modifier = 3) and not Girl.taboo):
                $ line = Girl.outfit["top"]
                $ Girl.outfit["top"] = ""
                if not Girl.seen_pussy:
                    $ Girl.change_stat("obedience", 60, 3)
                    $ Girl.change_stat("obedience", 200, 5)
                    $ Girl.change_stat("inhibition", 50, 4)
                    $ Girl.change_stat("inhibition", 200, 4)
                    if Girl == KittyX:
                        "She hesitantly glances your way, and then with a tug pulls her [line] through herself, tossing it to the ground."
                    elif Girl in (EmmaX,LauraX,StormX):
                        "She glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                    else:
                        "She hesitantly glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                    call expression Girl.tag + "_First_Bottomless" pass (1)
                else:
                    if Girl == KittyX:
                        "She drops her shoulders and her [line] falls to the floor."
                    else:
                        "She pulls her [line] over her head, tossing it to the ground."

                if not Girl.outfit["bra"] or Girl.top_pulled_up:
                    if not Girl.seen_breasts:
                        $ Girl.change_stat("obedience", 50, 3)
                        $ Girl.change_stat("inhibition", 50, 3)
                        call expression Girl.tag + "_First_Topless" pass (1)
                    else:
                        $ Girl.change_stat("lust", 60, 15)
                        $ Girl.change_stat("obedience", 50, 3)
                        $ Girl.change_stat("obedience", 75, 1)
                        $ Girl.change_stat("inhibition", 50, 3)
                else:
                    $ Girl.change_stat("lust", 75, 10)
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Girl.change_stat("obedience", 75, 1)
                    $ Girl.change_stat("inhibition", 70, 2)
                $ Player.change_stat("focus", 85, 15)
            else:
                jump Strip_Ultimatum

        elif Girl.outfit["bra"]:

            if approval_check(Girl, 1250, taboo_modifier = 3,Alt=[[StormX],(750-Nudist*3)]) or (Girl.seen_breasts and approval_check(Girl, 1100, taboo_modifier = 3) and not Girl.taboo):
                $ Girl.change_stat("lust", 60, 5)
                $ line = Girl.outfit["bra"]
                $ Girl.outfit["bra"] = ""
                if not Girl.seen_breasts:
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_stat("obedience", 200, 4)
                    $ Girl.change_stat("inhibition", 50, 3)
                    $ Girl.change_stat("inhibition", 200, 3)
                    if Girl == KittyX:
                        "She hesitantly glances your way, and then with a tug pulls her [line] through herself, tossing it to the ground."
                    elif Girl in (EmmaX,LauraX,StormX):
                        "She glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                    else:
                        "She hesitantly glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                    call expression Girl.tag + "_First_Topless" pass (1)
                else:
                    $ Girl.change_stat("obedience", 50, 2)
                    if Girl == KittyX:
                        "She drops her shoulders and her [line] falls to the floor."
                    else:
                        "She pulls her [line] over her head, tossing it to the ground."
                    $ Girl.change_stat("inhibition", 50, 1)
                $ Player.change_stat("focus", 80, 15)
            else:
                jump Strip_Ultimatum

        elif Girl.outfit["underwear"]:

            if approval_check(Girl, 1350, taboo_modifier = 3,Alt=[[StormX],(800-Nudist*3)]) or (Girl.seen_pussy and approval_check(Girl, 1100, taboo_modifier = 3) and not Girl.taboo):
                $ Girl.change_stat("lust", 75, 10)
                $ line = Girl.outfit["underwear"]
                $ Girl.outfit["underwear"] = ""
                if not Girl.seen_pussy:
                    $ Girl.change_stat("obedience", 60, 3)
                    $ Girl.change_stat("obedience", 200, 5)
                    $ Girl.change_stat("inhibition", 50, 4)
                    $ Girl.change_stat("inhibition", 200, 4)
                    if Girl == KittyX:
                        "She shyly looks up at you, and then slowly tugs her [line] off, flinging them to the side."
                    elif Girl in (EmmaX,LauraX):
                        "She looks up at you, and then slowly pulls her [line] down, kicking them off to the side."
                    else:
                        "She shyly looks up at you, and then slowly pulls her [line] down, kicking them off to the side."
                    call expression Girl.tag + "_First_Bottomless" pass (1)
                else:
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Girl.change_stat("obedience", 75, 1)
                    if Girl == KittyX:
                        "She looks up at you, and then gently pulls her [line] off, flicking them to the side."
                    else:
                        "She looks up at you, and then gently pulls her [line] down, kicking them off to the side."
                    $ Girl.change_stat("inhibition", 70, 2)
                $ Player.change_stat("focus", 85, 15)
            else:
                jump Strip_Ultimatum
        else:

            $ Girl.change_face("_sexy")
            if Girl == RogueX:
                ch_r "I'm afraid that's all I have on, [Girl.player_petname]. . ."
            elif Girl == KittyX:
                ch_k "It looks like I've run out of clothes. . ."
            elif Girl == EmmaX:
                ch_e "Well, it appears I've run out of clothes, [Girl.player_petname]. . ."
            elif Girl == LauraX:
                ch_l "Well, that's all I've got, [Girl.player_petname]. . ."
            elif Girl == JeanX:
                ch_j "I'm all out of clothes. . ."
            elif Girl == StormX:
                ch_s "I appear to have lost my clothing. . ."
            elif Girl == JubesX:
                ch_v "Well, it looks like I'm done here. . ."
            menu:
                extend ""
                "Ok, you can stop":
                    $ Girl.recent_history.append("stopdancing")
                    call reset_position(Girl)
                "Keep on dancing":
                    $ Girl.recent_history.append("keepdancing")


    $ Girl.change_stat("lust", 70, 2)
    if "exhibitionist" in Girl.traits:
        $ Girl.change_stat("lust", 200, 2)
    $ Player.change_stat("focus", 60, 3)
    if offhand_action == "jerking_off":
        $ Girl.change_stat("lust", 200, 2)
        $ Player.change_stat("focus", 200, 5)

    if not Player.semen and Player.focus >= 50:
        $ Player.focus = 50

    if Player.focus >= 100 or Girl.lust >= 100:


        if Player.focus >= 100:

            call Player_Cumming (Girl)
            if "_angry" in Girl.recent_history:
                return
            $ Girl.change_stat("lust", 200, 5)
            if not Player.semen and offhand_action == "jerking_off":
                "You're spitting dust here, maybe just watch quietly for a while."
                $ offhand_action = None
            if Player.focus > 80:
                jump Group_Strip_End

        if Girl.lust >= 100:

            call Girl_Cumming (Girl)
            if action_context == "shift" or "_angry" in Girl.recent_history:
                $ Count = 0
                jump Group_Strip_End

        call reset_position(Girl)

        if Girl == RogueX:
            show Rogue_sprite standing at Girl_Dance1(Girl)
        elif Girl == KittyX:
            show Kitty_sprite standing at Girl_Dance1(Girl)
        elif Girl == EmmaX:
            show Emma_sprite standing at Girl_Dance1(Girl)
        elif Girl == LauraX:
            show Laura_sprite standing at Girl_Dance1(Girl)
        elif Girl == JeanX:
            show Jean_sprite standing at Girl_Dance1(Girl)
        elif Girl == StormX:
            show Storm_sprite standing at Girl_Dance1(Girl)
        elif Girl == JubesX:
            show Jubes_sprite standing at Girl_Dance1(Girl)

        "[Girl.name] begins to dance again."

    if Partner and Partner.lust >= 100:

        call Girl_Cumming (Partner)

    menu:
        "[Girl.name] should. . ."
        "Keep Going. . ." if "keepdancing" not in Girl.recent_history:
            $ Girl.eyes = "_sexy"
            if Girl.love >= 700 or Girl.obedience >= 500:
                if not approval_bonus:
                    $ approval_bonus = 10
                elif approval_bonus <= 20:
                    $ approval_bonus += 1
            if taboo and Girl.action_counter["striptease"] <= 10:
                $ Girl.change_stat("obedience", 50, 7)
            elif taboo or Girl.action_counter["striptease"] <= 10:
                $ Girl.change_stat("obedience", 50, 5)
            elif Girl.action_counter["striptease"] <= 50:
                $ Girl.change_stat("obedience", 50, 3)
        "Keep Dancing. . ." if "keepdancing" in Girl.recent_history:
            $ Girl.eyes = "_sexy"

        "Stop stripping, keep dancing" if "keepdancing" not in Girl.recent_history:
            if Girl == RogueX:
                ch_r "Ok. . ."
            elif Girl == KittyX:
                ch_k "K. . ."
            elif Girl == EmmaX:
                ch_e "Oh? Very well."
            elif Girl == LauraX:
                ch_l "Huh? I guess. . ."
            elif Girl == JeanX:
                ch_j "Ok, sure."
            elif Girl == StormX:
                ch_s "Fine. . ."
            elif Girl == JubesX:
                ch_v "Oh, well ok. . ."
            $ Girl.recent_history.append("keepdancing")

        "Start stripping again" if "keepdancing" in Girl.recent_history:
            $ Girl.recent_history.remove("keepdancing")
            if "stripforced" in Girl.recent_history:
                Girl.voice ". . ."
            else:
                if Girl == RogueX:
                    ch_r "Hmm. . ."
                elif Girl == KittyX:
                    ch_k "Huh?"
                else:
                    Girl.voice "Hmm. . ."
        "Just watch silently":

            if "watching" not in Girl.recent_history:
                if "keepdancing" not in Girl.recent_history:
                    if taboo and Girl.action_counter["striptease"] <= 10:
                        $ Girl.change_stat("inhibition", 50, 3)
                    elif taboo or Girl.action_counter["striptease"] <= 10:
                        $ Girl.change_stat("inhibition", 50, 1)
                elif Girl.action_counter["striptease"] <= 50:
                    $ Girl.change_stat("inhibition", 50, 2)
                    $ Girl.change_stat("lust", 70, 2)
                $ Girl.recent_history.append("watching")

        "Start jack'in it." if offhand_action != "jerking_off":
            call jerking_off (Girl)
        "Stop jack'in it." if offhand_action == "jerking_off":
            $ offhand_action = None

        "Lose the [Girl.outfit[gloves]]. . ." if Girl.outfit["gloves"]:
            $ Girl.change_face("_surprised")
            $ Girl.mouth = "_kiss"
            Girl.voice "All right, [Girl.player_petname]."
            $ Girl.change_face("_sexy")
            $ Girl.outfit["gloves"] = ""
        "Ok, that's enough.":

            if Girl == RogueX:
                ch_r "Ok, [Girl.player_petname]. . . "
            elif Girl == KittyX:
                ch_k "Ok. . ."
            else:
                Girl.voice "Alright, [Girl.player_petname]."
            $ renpy.pop_call()
            jump Group_Strip_End

    return


label Strip_Ultimatum:
    if "keepdancing" in Girl.recent_history:
        return

    call reset_position(Girl)

    $ Girl.change_face("_bemused", 1)
    if "stripforced" in Girl.recent_history:
        $ Girl.change_face("_sad", 1)
        if Girl == RogueX:
            ch_r "That's as far as I care to go, [Girl.player_petname]."
        elif Girl == KittyX:
            ch_k "That's all you get."
        elif Girl == EmmaX:
            ch_e "I think that's plenty, [Girl.player_petname]."
        elif Girl == LauraX:
            ch_l "Last call, [Girl.player_petname]."
        elif Girl == JeanX:
            ch_j "Ok, that's my limit."
        elif Girl == StormX:
            ch_s "I will go no further. . ."
        elif Girl == JubesX:
            ch_v "Ok, that's all you get. . ."
    else:
        if Girl == RogueX:
            ch_r "I'm sorry, [Girl.player_petname], I'm not ready to show you more. . . Yet."
        elif Girl == KittyX:
            ch_k "I don't know, [Girl.player_petname], that's as far as I'll go for now."
        elif Girl == EmmaX:
            ch_e "I'm afraid that's as far as I'm ready to go, [Girl.player_petname]. . . for now."
        elif Girl == LauraX:
            ch_l "Ok, that's enough, [Girl.player_petname]. . . for now."
        elif Girl == JeanX:
            ch_j "Ok, I think you've seen enough. . ."
        elif Girl == StormX:
            ch_s "That's enough for now. . ."
        elif Girl == JubesX:
            ch_v "I'm kinda done here. . ."
    menu:
        extend ""
        "That's ok, you can stop.":
            if "ultimatum" not in Girl.daily_history:
                $ Girl.change_stat("love", 50, 2)
                $ Girl.change_stat("love", 90, 2)
                $ Girl.change_stat("inhibition", 50, 2)
                $ Girl.daily_history.append("ultimatum")
            $ Girl.recent_history.append("stopdancing")
            return
        "That's ok, but keep dancing for a bit. . .":
            if "ultimatum" not in Girl.daily_history:
                $ Girl.change_stat("love", 50, 2)
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("inhibition", 50, 2)
                $ Girl.daily_history.append("ultimatum")
            $ Girl.recent_history.append("keepdancing")
            if "stripforced" in Girl.recent_history:
                Girl.voice ". . ."
            else:
                if Girl == RogueX:
                    ch_r "Heh, ok [Girl.player_petname]."
                elif Girl == KittyX:
                    ch_k "Heh, alright."
                elif Girl == EmmaX:
                    ch_e "Oh, if I must, [Girl.player_petname]."
                elif Girl == LauraX:
                    ch_l "Eh? Fine."
                elif Girl == JeanX:
                    ch_j "Ok, sure."
                elif Girl == StormX:
                    ch_s "Very well. . ."
                elif Girl == JubesX:
                    ch_v "Ok, sure. . ."
        "You'd better." if Girl.forced:
            if not approval_check(Girl, 500, "O", taboo_modifier=5) and not approval_check(Girl, 800, "L", taboo_modifier=5):
                $ Girl.change_face("_angry")
                if Girl == RogueX:
                    ch_r "I don't know who you think I am, but I ain't gonna just jump when you say \"toad\"."
                    ch_r "I think we're done here for now."
                elif Girl == KittyX:
                    ch_k "I'm not just going to do \"whatever\"!"
                    ch_k "I'm done with this."
                elif Girl == EmmaX:
                    ch_e "I think you're overstepping your bounds here, [Girl.player_petname]."
                    ch_e "Remember your place."
                elif Girl == LauraX:
                    ch_l "I don't like that tone, [Girl.player_petname]."
                elif Girl == JeanX:
                    ch_j "Don't talk to me like that. -I- talk to -you- like that."
                elif Girl == StormX:
                    ch_s "I do not appreciate that tone."
                elif Girl == JubesX:
                    ch_v "I'd better not break your face either. . ."
                $ Girl.recent_history.append("_angry")
                $ Girl.daily_history.append("_angry")
                call remove_girl (Girl)
                return
            $ approval_bonus += 20
            $ Girl.forced += 1
            $ Girl.change_face("_sad")
            if "stripforced" in Girl.recent_history:
                $ Girl.change_face("_angry")
                Girl.voice ". . ."
            else:
                if Girl == RogueX:
                    ch_r "I. . . guess I could. . ."
                elif Girl == KittyX:
                    ch_k "I. . . could show a bit more. . ."
                elif Girl == EmmaX:
                    ch_e "Hmm, forceful. . ."
                elif Girl == LauraX:
                    ch_l "Grrrr. . ."
                elif Girl == JeanX:
                    ch_j ". . . fine."
                elif Girl == StormX:
                    ch_s ". . ."
                elif Girl == JubesX:
                    ch_v "Well. . . ok. . ."
                $ Girl.recent_history.append("stripforced")
            $ Girl.change_stat("love", 200, -40)
        "You can do better than that. Keep going." if not Girl.forced:
            if not approval_check(Girl, 300, "O", taboo_modifier=5) and not approval_check(Girl, 700, "L", taboo_modifier=5):
                $ Girl.change_face("_angry")
                if Girl == RogueX:
                    ch_r "I don't know who you think I am, but I ain't gonna just jump when you say \"toad\"."
                    ch_r "I think we're done here for now."
                elif Girl == KittyX:
                    ch_k "I'm not just going to do \"whatever\"!"
                    ch_k "I'm done with this."
                elif Girl == EmmaX:
                    ch_e "I think you're overstepping your bounds here, [Girl.player_petname]."
                    ch_e "Remember your place."
                elif Girl == LauraX:
                    ch_l "I don't like that tone, [Girl.player_petname]."
                elif Girl == JeanX:
                    ch_j "Don't talk to me like that. -I- talk to -you- like that."
                elif Girl == StormX:
                    ch_s "No, I do not think so."
                elif Girl == JubesX:
                    ch_v "Oh, I can, but you're not goinna see it. . ."
                $ Girl.recent_history.append("_angry")
                $ Girl.daily_history.append("_angry")
                call remove_girl (Girl)
                return
            $ Girl.change_stat("love", 200, -10)
            $ Girl.change_stat("obedience", 50, 3)
            $ Girl.change_stat("obedience", 75, 5)
            $ approval_bonus += 20
            $ Girl.forced += 1
            $ Girl.change_face("_sad")
            if Girl == RogueX:
                ch_r "Well, if you insist. . ."
            elif Girl == KittyX:
                ch_k "I mean, maybe. . ."
            elif Girl == EmmaX:
                ch_e "I can't imagine doing better than \"perfection\". . ."
            elif Girl == LauraX:
                ch_l ". . . Right. . ."
            elif Girl == JeanX:
                ch_j "I don't see how anyone could. . ."
            elif Girl == StormX:
                ch_s "We shall see. . ."
            elif Girl == JubesX:
                ch_v "Ok, how about this. . ."
    if "ultimatum" not in Girl.daily_history:
        $ Girl.daily_history.append("ultimatum")

    if Girl == RogueX:
        show Rogue_sprite standing at Girl_Dance1(Girl)
    elif Girl == KittyX:
        show Kitty_sprite standing at Girl_Dance1(Girl)
    elif Girl == EmmaX:
        show Emma_sprite standing at Girl_Dance1(Girl)
    elif Girl == LauraX:
        show Laura_sprite standing at Girl_Dance1(Girl)
    elif Girl == JeanX:
        show Jean_sprite standing at Girl_Dance1(Girl)
    elif Girl == StormX:
        show Storm_sprite standing at Girl_Dance1(Girl)
    elif Girl == JubesX:
        show Jubes_sprite standing at Girl_Dance1(Girl)
    "[Girl.name] begins to dance again."
    return

transform Girl_Dance1(Chr=focused_Girl):
    subpixel True
    pos (Chr.sprite_location, 50)
    xoffset 0
    yoffset 0
    choice:
        parallel:
            ease 2.5 xoffset -40
            ease 2.5 xoffset 0
        parallel:
            easeout 1.0 yoffset 30
            linear 0.5 yoffset 40
            easein 1.0 yoffset 0
            easeout 1.0 yoffset 40
            linear 0.5 yoffset 50
            easein 1.0 yoffset 0
    choice:
        parallel:
            ease 2.5 xoffset 40
            ease 2.5 xoffset 0
        parallel:
            easeout 1.0 yoffset 30
            linear 0.5 yoffset 40
            easein 1.0 yoffset 0
            easeout 1.0 yoffset 40
            linear 0.5 yoffset 50
            easein 1.0 yoffset 0
    choice (0.3):
        parallel:
            ease 2.5 xoffset -30
            ease 2.5 xoffset 0
        parallel:
            ease 1.5 yoffset 150
            ease 3.5 yoffset 0
    repeat

label AutoStrip(Girl=0):

    $ Girl = check_girl(Girl)
    if (Girl.outfit["underwear"] and not Girl.underwear_pulled_down) or Girl.bottom_number() >= 6 or Girl.hose_number() >= 6:
        if Girl == RogueX:
            ch_r "Well, I guess some things are necessary, [RogueX.player_petname]."
        elif Girl == KittyX:
            ch_k "We can't exactly do much like this, huh."
        elif Girl == EmmaX:
            ch_e "I suppose we can't do much with all this on."
        elif Girl == LauraX:
            ch_l "Huh. . ."
        elif Girl == JeanX:
            ch_j "Huh. . ."
        elif Girl == StormX:
            ch_s "I suppose our options are limited with these on."
        elif Girl == JubesX:
            ch_v "Let's get these out of the way. . ."

        if (Girl.outfit["underwear"] and not Girl.underwear_pulled_down) and (Girl.bottom_number() > 6 and not Girl.upskirt):
            "She quickly drops her pants and her [Girl.outfit[underwear]]."
        elif (Girl.outfit["underwear"] and not Girl.underwear_pulled_down) and (Girl.bottom_number() == 6 and not Girl.upskirt):
            "She quickly drops her shorts and her [Girl.outfit[underwear]]."
        elif Girl.bottom_number() > 6 and not Girl.upskirt:
            "She tugs her pants down, exposing her bare pussy."
        elif Girl.bottom_number() == 6 and not Girl.upskirt:
            "She tugs her shorts down, exposing her bare pussy."
        elif Girl.hose_number() >= 6 and (Girl.outfit["underwear"] and not Girl.underwear_pulled_down):
            "She tugs her [Girl.outfit[hose]] and [Girl.outfit[underwear]] off."

        elif Girl.hose_number() >= 6:
            "She tugs her [Girl.outfit[hose]] off and drops them to the ground."

        elif (Girl.outfit["underwear"] and not Girl.underwear_pulled_down):
            "She tugs her [Girl.outfit[underwear]] off and drops them to the ground."

    $ Girl.upskirt = 1 if Girl.outfit["bottom"] else 0
    $ Girl.underwear_pulled_down = 1 if Girl.outfit["underwear"] else 0
    $ Girl.outfit["hose"] = "" if Girl.hose_number() >= 6 else Girl.outfit["hose"]

    $ Girl.seen_underwear = 1
    call expression Girl.tag + "_First_Bottomless"
    return

label Girl_Undress(Girl=0, Region="ask", stored_count=0):

    $ Girl = check_girl(Girl)
    call shift_focus (Girl)

    $ stored_count = approval_bonus
    if Partner == Girl:
        $ approval_bonus = 0
    call shift_focus (Girl)

    if Region == "auto":
        if Girl.upskirt and Girl.underwear_pulled_down:
            return
        if Girl.bottom_number() > 5 and approval_bonus < 20:
            $ approval_bonus = 20
        if Girl.lust >= 90:
            $ approval_bonus += 10
        elif Girl.lust >= 80:
            $ approval_bonus += 5
        $ action_context = "auto"
        call Bottoms_Off (Girl, 0)

    if Region == "ask":
        menu:
            "Which parts?"
            "Her top" if Girl.outfit["top"] or Girl.outfit["bra"] or Girl.outfit["gloves"] or Girl.outfit["front_outer_accessory"]:
                $ Region = "top"
            "Her bottoms" if Girl.outfit["bottom"] or Girl.outfit["underwear"] or Girl.outfit["hose"] or Girl.outfit["front_outer_accessory"]:
                $ Region = "bottom"
            "A little of both. . ." if Girl.outfit["top"] or Girl.outfit["bra"] or Girl.outfit["bottom"] or Girl.outfit["underwear"] or Girl.outfit["hose"] or Girl.outfit["front_outer_accessory"]:
                $ Region = "both"
            "Never mind":
                pass

    if Region == "top":
        if Girl.outfit["top"] or Girl.outfit["bra"]:
            call Top_Off (Girl, 0)
    elif Region == "bottom":
        if Girl.outfit["bottom"] or Girl.outfit["underwear"] or Girl.outfit["hose"]:
            call Bottoms_Off (Girl, 0)
    elif Region == "both":
        if Girl.outfit["top"] or Girl.outfit["bra"]:
            call Top_Off (Girl, 0)

        if Partner == Girl:
            $ approval_bonus = 0
        else:
            $ approval_bonus = stored_count

        if "_angry" in Girl.recent_history:
            pass
        elif not Girl.outfit["bottom"] and not Girl.outfit["underwear"] and not Girl.outfit["hose"]:
            pass
        elif "no_topless" in Girl.recent_history:
            if Girl == RogueX:
                ch_r "You might want to rethink your next question."
            elif Girl == KittyX:
                ch_k "Don't push it. . ."
            elif Girl == EmmaX:
                ch_e "Care to push your luck?"
            elif Girl == LauraX:
                ch_l "Know when to fold'em, [Girl.player_petname]."
            elif Girl == JeanX:
                ch_j "Ha! Keep trying, [Girl.player_petname]."
            elif Girl == StormX:
                ch_s "I do not see this going your way. . ."
            elif Girl == JubesX:
                ch_v "Well now you're pushing it. . ."
            menu:
                extend ""
                "And now the bottoms?":
                    call Bottoms_Off (Girl, 0)
                "You're probably right, sorry.":
                    pass
        else:
            ch_p "And now the bottoms?"
            call Bottoms_Off (Girl, 0)

    $ approval_bonus = stored_count
    return



label Top_Off(Girl=0, Intro=1, line=0, counter=0):

    $ Girl = check_girl(Girl)
    call shift_focus (Girl)

    if not Girl.outfit["top"] and not Girl.outfit["bra"]:

        $ approval_bonus = 0
        return

    if "_angry" in Girl.recent_history:
        if Girl == RogueX:
            ch_r "I'm just too annoyed to deal with this right now."
        elif Girl == KittyX:
            ch_k "No titties for you."
        elif Girl == EmmaX:
            ch_e "I'm in no mood, [Girl.player_petname]."
        elif Girl == LauraX:
            ch_l "Don't push it, [Girl.player_petname]."
        elif Girl == JeanX:
            ch_j "No way, [Girl.player_petname]."
        elif Girl == StormX:
            ch_s "These are not for your enjoyment."
        elif Girl == JubesX:
            ch_v "The top stays on. . ."
        return

    if Girl.seen_breasts and approval_check(Girl, 500) and not taboo:

        $ approval_bonus += 20
    if "exhibitionist" in Girl.traits:
        $ approval_bonus += (4*taboo)
    if Girl in Player.Harem or "sex friend" in Girl.player_petnames and not taboo:
        $ approval_bonus += 10
    elif "ex" in Girl.traits:
        $ approval_bonus -= 40
    if "no_topless" in Girl.recent_history:
        $ approval_bonus -= 10
    elif Girl == StormX and (not taboo or Girl in Rules):

        $ approval_bonus += 20


    if Intro and not Girl.top_pulled_up:
        if Intro == 2:

            if Girl == RogueX:
                ch_r "I don't know, you'd have to touch them. . ."
            elif Girl == KittyX:
                ch_k "So, you'd have to be able to[KittyX.like]touch them, I guess. . ."
            elif Girl == EmmaX:
                ch_e "I would probably need to be bare-chested to get anything out of that. . ."
            elif Girl == LauraX:
                ch_l "I'd need to be topless to get anything from that. . ."
            elif Girl == JeanX:
                ch_j "I guess I'd have to go topless. . ."
            elif Girl == StormX:
                ch_s "If direct contact is necessary. . ."
            elif Girl == JubesX:
                ch_v "Well, I'd need to be topless for that to. . ."
        else:
            if Girl.outfit["top"]:
                ch_p "This might be easier without your [Girl.outfit[top]] on."
            elif Girl.outfit["bra"]:
                ch_p "This might be easier without your [Girl.outfit[bra]] on."


    $ approval = approval_check(Girl, 1100, taboo_modifier = 4)

    if action_context == "auto" and  (Girl.outfit["top"] or Girl.outfit["bra"] or (Girl == JubesX and Girl.outfit["front_outer_accessory"])) and not Girl.top_pulled_up:
        $ line = 0
        if approval_check(Girl, 1250, taboo_modifier = 1) or (Girl.seen_breasts and approval_check(Girl, 500) and not taboo):

            $ Girl.change_stat("inhibition", 70, 1)
            $ Girl.top_pulled_up = 1
            $ line = Girl.outfit["top"] if Girl.outfit["top"] else Girl.outfit["bra"]
            "[Girl.name] sighs in frustration, and pulls her [line] up over her breasts."
            if Girl == RogueX:
                ch_r "I just wasn't getting much out of it that way."
            elif Girl == KittyX:
                ch_k "I[Girl.like]wasn't feeling it that way."
            elif Girl == EmmaX:
                ch_e "Sometimes only direct contact will do."
            elif Girl == LauraX:
                ch_l "That wasn't working out."
            elif Girl == JeanX:
                ch_j "Ok, try that now, [Girl.player_petname]."
            elif Girl == StormX:
                ch_s "Does that work better?"
            elif Girl == JubesX:
                ch_v "Ok, that's more comfortable. . ."
            if taboo:
                $ Girl.change_stat("inhibition", 90, (int(taboo/20)))
            call expression Girl.tag + "_First_Topless" pass (1)
        elif Girl.outfit["top"] and Girl.outfit["bra"] and approval_check(Girl, 800, taboo_modifier = 1):

            $ Girl.change_stat("inhibition", 40, 1)
            $ line = Girl.outfit["top"]
            $ Girl.outfit["top"] = ""
            if Girl == KittyX:
                "[Girl.name] sighs in frustration, and her [line] drops to the ground."
            elif Girl == JubesX:
                if Girl.outfit["front_outer_accessory"]:
                    $ Girl.outfit["front_outer_accessory"] = ""
                    "[Girl.name] sighs in frustration, and shrugs off her Jacket, before pulling her [line] over her head."
                else:
                    "[Girl.name] sighs in frustration, and pulls her [line] over her head, throwing it aside."
            else:
                "[Girl.name] sighs in frustration, and pulls her [line] over her head, throwing it aside."
            if Girl == RogueX:
                ch_r "I just wasn't getting much out of it that way."
            elif Girl == KittyX:
                ch_k "I[Girl.like]wasn't feeling it that way."
            elif Girl == EmmaX:
                ch_e "I just wasn't getting much out of it that way."
            elif Girl == LauraX:
                ch_l "That wasn't working out."
            elif Girl == JeanX:
                ch_j "Ok, try that now, [Girl.player_petname]."
            elif Girl == StormX:
                ch_s "Does that work better?"
            elif Girl == JubesX:
                ch_v "Ok, that's a bit better. . ."


        $ line = 0
        return

    if approval >= 2:

        if "no_topless" in Girl.daily_history:
            if Girl == RogueX:
                ch_r "Ok, fine, top off."
            elif Girl == KittyX:
                ch_k "Okay, okay!"
            elif Girl == EmmaX:
                ch_e "{i}Fine,{/i} if that will shut you up."
            elif Girl == LauraX:
                ch_l "{i}Fine,{/i} but don't think I'm getting soft on you."
            elif Girl == JeanX:
                ch_j "Oh, fine. . ."
            elif Girl == StormX:
                ch_s "Oh, if you insist. . ."
            elif Girl == JubesX:
                ch_v "Well if you insist. . ."
        $ Girl.change_face("_sexy", 1)
        if Girl.forced:
            $ Girl.change_face("_sad", 1)
            $ Girl.change_stat("love", 20, -2, 1)
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 60, 1)
        $ Girl.change_stat("inhibition", 50, 3)
        $ counter = 1
        while (Girl.outfit["bra"] or Girl.outfit["top"] or (Girl == JubesX and Girl.outfit["front_outer_accessory"])) and counter:
            if Girl == RogueX:
                ch_r "So, [Girl.player_petname]. Did you want me to take my top off?"
            elif Girl == KittyX:
                ch_k "So[Girl.like]how much did you want me to take off?"
            elif Girl == EmmaX:
                ch_e "What was it you were interested in, [Girl.player_petname]?"
            elif Girl == LauraX:
                ch_l "What did you want to see, [Girl.player_petname]?"
            elif Girl == JeanX:
                ch_j "Oh, what were you looking to see, [Girl.player_petname]."
            elif Girl == StormX:
                ch_s "What should I remove?"
            elif Girl == JubesX:
                ch_v "Ok then, so what did you want off?"
            menu:
                extend ""


                "Why don't you lose the jacket?" if Girl == JubesX and Girl.outfit["front_outer_accessory"]:
                    $ Girl.outfit["front_outer_accessory"] = ""
                    "[Girl.name] shrugs her jacket off."

                "Lose the [Girl.outfit[top]]." if Girl.outfit["top"]:
                    $ Girl.change_face("_bemused", 1)
                    $ line = Girl.outfit["top"]
                    $ Girl.outfit["top"] = ""
                    if Girl == KittyX:
                        "[Girl.name] shrugs and her [line] falls through to the ground."
                    else:
                        "[Girl.name] pulls her [line] off and tosses it aside."

                "Why don't you lose the [Girl.outfit[neck]]?" if Girl.outfit["neck"]:
                    $ line = Girl.outfit["neck"]
                    $ Girl.outfit["neck"] = ""
                    "[Girl.name] pulls her [line] off."

                "Just lose the [Girl.outfit[bra]]." if Girl.outfit["top"] and Girl.outfit["bra"]:
                    $ Girl.change_face("_bemused", 1)
                    $ line = Girl.outfit["bra"]
                    $ Girl.outfit["bra"] = ""
                    if Girl == KittyX:
                        "[Girl.name] reaches through her top and pulls her [line] free, dropping it to the ground."
                    else:
                        "[Girl.name] slowly removes her [line] from under the [Girl.outfit[top]]."
                "Lose the [Girl.outfit[bra]]." if not Girl.outfit["top"] and Girl.outfit["bra"]:
                    $ Girl.change_face("_bemused", 1)
                    $ line = Girl.outfit["bra"]
                    $ Girl.outfit["bra"] = ""
                    if Girl == KittyX:
                        "[Girl.name] shrugs and her [line] falls through to the ground."
                    else:
                        "[Girl.name] throws off her [line]."
                "Just pull it up." if (Girl.outfit["top"] or Girl.outfit["bra"]) and not Girl.top_pulled_up:
                    $ Girl.change_face("_bemused", 1)
                    $ Girl.top_pulled_up = 1
                    if Girl == EmmaX:
                        "[Girl.name] smiles and pulls out her tits. . ."
                    elif Girl.outfit["top"] and Girl.outfit["bra"]:
                        "[Girl.name] smiles and lifts up her tops. . ."
                    else:
                        "[Girl.name] smiles and lifts up her top. . ."
                "Lose both tops." if Girl.outfit["top"] and Girl.outfit["bra"]:
                    $ Girl.change_face("_bemused", 1)
                    if Girl == KittyX:
                        $ Girl.outfit["top"] = ""
                        $ Girl.outfit["bra"] = ""
                        "[Girl.name] shrugs and her tops fall through her body to the ground."
                    else:
                        if Girl == JubesX and Girl.outfit["front_outer_accessory"]:
                            $ Girl.outfit["front_outer_accessory"] = ""
                            "[Girl.name] pulls off her jacket. . ."
                        $ line = Girl.outfit["top"]
                        $ Girl.outfit["top"] = ""
                        "[Girl.name] tosses the [line] over her head. . ."
                        $ line = Girl.outfit["bra"]
                        $ Girl.outfit["bra"] = ""
                        ". . .and then the [line] as well."
                "Lose the [Girl.outfit[gloves]]. . ." if Girl.outfit["gloves"]:
                    $ Girl.change_face("_sexy")
                    $ line = Girl.outfit["gloves"]
                    $ Girl.outfit["gloves"] = ""
                    "She pulls off her [line]."

                "Why don't you lose the suspenders?" if Girl.outfit["front_outer_accessory"] == "_suspenders" or Girl.outfit["front_outer_accessory"] == "_suspenders2":
                    $ Girl.outfit["front_outer_accessory"] = ""
                    "[Girl.name] pulls her suspenders off."

                "Why don't you lose the hoops?" if Girl.outfit["front_outer_accessory"] == "_rings" or Girl.outfit["front_outer_accessory"] == "_rings":
                    $ Girl.outfit["front_outer_accessory"] = ""
                    "[Girl.name] pulls her hoops off."

                "Why don't you lose the hat?" if Girl.outfit["hair"] == "_hat" or Girl.outfit["hair"] == "_wet_hat":
                    $ Girl.outfit["hair"] == "_wet" if Girl.outfit["hair"] == "_wet_hat" else "_wavy"
                    "[Girl.name] tosses her hat aside."
                "That's enough. [[exit]":

                    $ Girl.change_face("_bemused", 1)
                    Girl.voice "All right, [Girl.player_petname]."
                    $ counter = 0
        if Girl.bra_number() < 3 and Girl.top_number() < 3:

            $ Girl.change_stat("obedience", 50, 1)
            $ Girl.change_stat("obedience", 90, 1)
            call expression Girl.tag + "_First_Topless"
        $ Girl.change_stat("lust", 80, 3)
        $ Girl.recent_history.append("ask topless")
        $ Girl.daily_history.append("ask topless")
        $ approval_bonus = 0
        return



    $ Girl.change_face("_bemused", 1)
    if Girl == RogueX:
        if Intro == "massage" and not approval:
            ch_r "I'm ok with a massage, but my top stays on."
        elif "no_topless" in Girl.recent_history:
            $ Girl.change_face("_angry")
            ch_r "I just told you no, [Girl.player_petname]."
        elif approval and not Girl.seen_breasts:
            ch_r "I'd like to leave something to the imagination. . ."
        elif not Girl.seen_breasts:
            ch_r "I'm not ready to show you those yet. . ."
        elif "no_topless" in Girl.daily_history:
            ch_r "I wasn't into it earlier, [Girl.player_petname], what's changed?"
        elif "ask topless" in Girl.recent_history:
            ch_r "outfit_changed your mind, [Girl.player_petname]?"
        elif taboo:
            ch_r "It's a bit exposed here. . ."
        elif approval:
            ch_r "Well, you've seen them before, but. . ."
        else:
            ch_r "Not right now."
    elif Girl == KittyX:
        if Intro == "massage" and not approval:
            ch_k "A massage is fine, but I'm keeping my top on, ok?"
        elif "no_topless" in Girl.recent_history:
            $ Girl.change_face("_angry")
            ch_k "I[Girl.like]already told you, no way!"
        elif approval and not Girl.seen_breasts:
            ch_k "I'm[Girl.like]not really comfortable with that."
        elif not Girl.seen_breasts:
            ch_k "I'd[Girl.like]really rather not, ok?"
        elif "no_topless" in Girl.daily_history:
            ch_k "Do you[Girl.like]think something's changed since earlier?"
        elif "ask topless" in Girl.recent_history:
            ch_k "Did you[Girl.like]want something else off?"
        elif taboo:
            ch_k "I'm[Girl.like]not that comfortable out here. . ."
        elif approval:
            ch_k "Maybe not?"
        else:
            ch_k "Nu-uh."
    elif Girl == EmmaX:
        if Intro == "massage" and not approval:
            ch_e "I welcome a massage, but I'm staying fully dressed."
        elif "no_topless" in Girl.recent_history:
            $ Girl.change_face("_angry")
            ch_e "Learn from previous mistakes, [Girl.player_petname]."
        elif approval and not Girl.seen_breasts:
            ch_e "I don't know if that would be appropriate."
        elif not Girl.seen_breasts:
            ch_e "I don't think you're ready for that."
        elif "no_topless" in Girl.daily_history:
            ch_e "Are you still that obsessed?"
        elif "ask topless" in Girl.recent_history:
            ch_e "You want more?"
        elif taboo:
            ch_e "[Girl.player_petname], not around prying eyes."
        elif approval:
            ch_e "Are you sure you're prepared?"
        else:
            ch_e "No."
    elif Girl == LauraX:
        if Intro == "massage" and not approval:
            ch_l "I could use a massage, but I'm keeping my clothes on."
        elif "no_topless" in Girl.recent_history:
            $ Girl.change_face("_angry")
            ch_l "Don't push it, [Girl.player_petname]."
        elif approval and not Girl.seen_breasts:
            ch_l "I don't know, man."
        elif not Girl.seen_breasts:
            ch_l "I really don't think so."
        elif "no_topless" in Girl.daily_history:
            ch_l "Dude, relax."
        elif "ask topless" in Girl.recent_history:
            ch_l "Again?"
        elif taboo:
            ch_l "[Girl.player_petname], not around here, alright?"
        elif approval:
            ch_l "Are you sure?"
        else:
            ch_l "No."
    elif Girl == JeanX:
        if Intro == "massage" and not approval:
            ch_j "Massage, yes, but top on."
        elif "no_topless" in Girl.recent_history:
            $ JeanX.change_face("_angry")
            ch_j "Relax, [Girl.player_petname]."




        elif "no_topless" in Girl.daily_history:
            ch_j "Not happening."
        elif "ask topless" in Girl.recent_history:
            ch_j "So soon?"
        elif taboo:
            ch_j "Hmm. . . not around here"
        elif approval:
            ch_j "Hmm. . ."
        else:
            ch_j "No way."
    elif Girl == StormX:
        if Intro == "massage" and not approval:
            ch_s "I would enjoy a massage, but I'm staying fully clothed."
        elif "no_topless" in Girl.recent_history:
            $ Girl.change_face("_angry")
            ch_s "I am not so pliable as that, [Girl.player_petname]."
        elif approval and not Girl.seen_breasts:
            ch_s "I don't know if that would be appropriate."
        elif "no_topless" in Girl.daily_history:
            ch_s "Do not ask again."
        elif "ask topless" in Girl.recent_history:
            ch_s "Oh, you'd like to see them again?"
        elif taboo and Girl not in Rules:
            ch_s "I'm afraid not in public, [Girl.player_petname]."
        elif approval:
            ch_s "Are you Certain?"
        else:
            ch_s "No."
    elif Girl == JubesX:
        if Intro == "massage" and not approval:
            ch_v "I could use a massage, but I'm keeping my clothes on."
        elif "no_topless" in Girl.recent_history:
            $ Girl.change_face("_angry")
            ch_v "Don't push it, [Girl.player_petname]."
        elif approval and not Girl.seen_breasts:
            ch_v "I don't know, man."
        elif not Girl.seen_breasts:
            ch_v "I'm not cool with that."
        elif "no_topless" in Girl.daily_history:
            ch_v "Dude, relax."
        elif "ask topless" in Girl.recent_history:
            ch_v "Again?"
        elif taboo:
            ch_v "[Girl.player_petname], it's just public here?"
        elif approval:
            ch_v "I dunno, really?"
        else:
            ch_v "Nah."
    menu:
        extend ""
        "Sorry, sorry." if "no_topless" in Girl.recent_history:
            $ Girl.change_face("_bemused", 1)
            if Girl == RogueX:
                ch_r "Ok, just. . . give it a rest, huh?"
            elif Girl == KittyX:
                ch_k "It's cool, I get it, but[Girl.like]chill out, huh?"
            elif Girl == EmmaX:
                ch_e "I can't blame you for your persistance, but learn from your errors."
            elif Girl == LauraX:
                ch_l "Right, I get it, stay thirsty."
            elif Girl == JeanX:
                ch_j "It's not like I can blame you, [Girl.player_petname]."
            elif Girl == StormX:
                ch_s "I cannot blame you."
            elif Girl == JubesX:
                ch_v "Well, you can't win if the don't play, right?"

        "Ok, that's fine." if "no_topless" not in Girl.recent_history:
            if "ask topless" not in Girl.daily_history:
                $ Girl.change_stat("lust", 80, 3)
                $ Girl.change_stat("love", 70, 1)
                $ Girl.change_stat("love", 90, 1)
                $ Girl.change_stat("inhibition", 50, 3)
            if Girl.forced:
                $ Girl.mouth = "_smile"
                if Girl == RogueX:
                    ch_r "I really appreciate that."
                elif Girl == KittyX:
                    ch_k "That's[Girl.like]really cool of you."
                elif Girl == EmmaX:
                    ch_e "How. . . generous of you."
                elif Girl == LauraX:
                    ch_l "Ok."
                elif Girl == JeanX:
                    ch_j ". . ."
                elif Girl == StormX:
                    ch_s "Good."
                elif Girl == JubesX:
                    ch_v "Yeah, thanks. . ."
                if "ask topless" not in Girl.daily_history:
                    $ Girl.change_stat("love", 20, 2)
                    $ Girl.change_stat("love", 70, 2)
                    $ Girl.change_stat("inhibition", 60, 1)

        "How about just the jacket?" if Girl == JubesX and Girl.outfit["front_outer_accessory"]:

            if Girl.outfit["top"] or Girl.outfit["front_outer_accessory"] == "_open_jacket":

                ch_v "Sure, I guess. . ."
                $ Girl.outfit["front_outer_accessory"] = ""
                "[Girl.name] shrugs off her Jacket."
            elif approval_check(Girl, 800, taboo_modifier = 2) and Girl.outfit["bra"]:
                $ Girl.change_face("_sexy")
                ch_v "Well, I guess. . ."
                $ Girl.change_face("_bemused", 1)
                $ Girl.outfit["front_outer_accessory"] = ""
                "[Girl.name] shrugs off her Jacket."
                $ Girl.change_stat("obedience", 50, 1)
                $ Girl.change_stat("inhibition", 30, 2)
            elif not Girl.outfit["bra"]:
                $ Girl.eyes = "_surprised"
                $ Girl.blushing = "_blush2"
                ch_v "I kinda don't have anything under this. . ."
                $ Girl.change_stat("inhibition", 30, 1)
                menu:
                    extend ""
                    "Ok, you can leave it on.":
                        $ Girl.mouth = "_smile"
                        $ Girl.change_stat("love", 70, 2)
                        ch_v "Whew, thanks. . ."
                    "That doesn't bother me any.":

                        if approval_check(Girl, 500, "I", taboo_modifier=3) or approval_check(Girl, 1000, "LI", taboo_modifier=3):
                            $ Girl.change_face("_bemused", 1)
                            ch_v "Whoa, spicy. . ."
                            $ Girl.change_stat("obedience", 20, 2)
                            $ Girl.change_stat("obedience", 60, 1)
                            $ Girl.change_face("_sexy")
                            $ Girl.outfit["front_outer_accessory"] = ""
                            "[Girl.name] shrugs off her Jacket."
                            $ Girl.outfit["top"] = ""
                            $ Girl.change_stat("inhibition", 30, 2)
                            $ Girl.change_stat("inhibition", 60, 1)
                            call expression Girl.tag + "_First_Topless"
                        else:
                            $ Girl.change_face("_bemused")
                            call Top_Off_Refused (Girl)
                    "I know, take it off.":

                        call ToplessorNothing (Girl)
                $ Girl.blushing = "_blush1"
            else:
                $ Girl.change_face("_sexy")
                call Top_Off_Refused (Girl)

        "How about just the [Girl.outfit[top]]?" if Girl.outfit["top"]:

            if approval_check(Girl, 800, taboo_modifier = 2) and Girl.outfit["bra"]:
                $ Girl.change_face("_sexy")
                if Girl == RogueX:
                    ch_r "Well, that's no big deal I guess. . ."
                elif Girl == KittyX:
                    ch_k "Um, I guess I could. . ."
                elif Girl == EmmaX:
                    ch_e "Well, I suppose that would be fine. . ."
                elif Girl == LauraX:
                    ch_l "I mean. . . I guess. . ."
                elif Girl == JeanX:
                    ch_j "Sure, whatever."
                elif Girl == StormX:
                    ch_s "I suppose so."
                elif Girl == JubesX:
                    ch_v "Well, I guess. . ."
                $ Girl.change_face("_bemused", 1)
                $ line = Girl.outfit["top"]
                $ Girl.outfit["top"] = ""
                if Girl == KittyX:
                    "[Girl.name] shrugs and her [line] falls through to the ground."
                elif Girl == JubesX:
                    if Girl.outfit["front_outer_accessory"]:
                        $ Girl.outfit["front_outer_accessory"] = ""
                        "[Girl.name] shrugs off her Jacket, before pulling her [line] over her head."
                    else:
                        "[Girl.name] pulls her [line] over her head, throwing it aside."
                else:
                    "[Girl.name] tosses the [line] over her head."
                $ Girl.change_stat("obedience", 50, 1)
                $ Girl.change_stat("inhibition", 30, 2)
            elif not Girl.outfit["bra"]:
                $ Girl.eyes = "_surprised"
                $ Girl.blushing = "_blush2"
                if Girl == RogueX:
                    ch_r "I'm not exactly decent under this, you know."
                elif Girl == KittyX:
                    ch_k "I'd[Girl.like]be {i}totally{/i} exposed here."
                elif Girl == EmmaX:
                    ch_e "I don't think you're prepared for what's under there."
                elif Girl == LauraX:
                    ch_l "I don't really have anything on under here."
                elif Girl == JeanX:
                    ch_j "I'm not wearing a bra at the moment."
                elif Girl == StormX:
                    ch_s "I am naked under this, you know. . ."
                elif Girl == JubesX:
                    ch_v "I kinda don't have anything under this. . ."
                $ Girl.change_stat("inhibition", 30, 1)
                menu:
                    extend ""
                    "Ok, you can leave it on.":
                        $ Girl.mouth = "_smile"
                        $ Girl.change_stat("love", 70, 2)
                        if Girl == RogueX:
                            ch_r "Great!"
                        elif Girl == KittyX:
                            ch_k "Thanks!"
                        elif Girl == EmmaX:
                            ch_e "Good."
                        elif Girl == LauraX:
                            ch_l "Right."
                        elif Girl == JeanX:
                            ch_j "That's what I said."
                        elif Girl == StormX:
                            ch_s "Very well then."
                        elif Girl == JubesX:
                            ch_v "Whew, thanks. . ."
                    "That doesn't bother me any.":

                        if approval_check(Girl, 500, "I", taboo_modifier=3) or approval_check(Girl, 1000, "LI", taboo_modifier=3):
                            $ Girl.change_face("_bemused", 1)
                            if Girl == RogueX:
                                ch_r "Ooh, at least you know what you like"
                            elif Girl == KittyX:
                                ch_k "Why am I not surprised?"
                            elif Girl == EmmaX:
                                ch_e "Well, I suppose it couldn't hurt to try."
                            elif Girl == LauraX:
                                ch_l "Maybe it should. . ."
                            elif Girl == JeanX:
                                ch_j ". . ."
                            elif Girl == StormX:
                                ch_s "It doesn't bother me much either."
                            elif Girl == JubesX:
                                ch_v "Whoa, spicy. . ."
                            $ Girl.change_stat("obedience", 20, 2)
                            $ Girl.change_stat("obedience", 60, 1)
                            $ Girl.change_face("_sexy")
                            $ line = Girl.outfit["top"]
                            $ Girl.outfit["top"] = ""
                            if Girl == KittyX:
                                "[Girl.name] shrugs and her [line] falls through to the ground."
                            elif Girl == JubesX:
                                if Girl.outfit["front_outer_accessory"]:
                                    $ Girl.outfit["front_outer_accessory"] = ""
                                    "[Girl.name] shrugs off her Jacket, before pulling her [line] over her head."
                                else:
                                    "[Girl.name] and pulls her [line] over her head, throwing it aside."
                            else:
                                "[Girl.name] tosses the [line] over her head."
                            $ Girl.outfit["top"] = ""
                            $ Girl.change_stat("inhibition", 30, 2)
                            $ Girl.change_stat("inhibition", 60, 1)
                            call expression Girl.tag + "_First_Topless"
                        else:
                            $ Girl.change_face("_bemused")
                            call Top_Off_Refused (Girl)
                    "I know, take it off.":

                        call ToplessorNothing (Girl)
                $ Girl.blushing = "_blush1"
            else:
                $ Girl.change_face("_sexy")
                call Top_Off_Refused (Girl)
        "Come on, please? [[take it all off]":



            if approval and approval_check(Girl, 600, "L", taboo_modifier=1):
                $ Girl.change_stat("obedience", 40, 2)
                $ Girl.change_face("_sexy")
                if Girl == RogueX:
                    if "no_topless" in Girl.recent_history:
                        ch_r "You're pretty persistent, [Girl.player_petname]. I guess this time it'll be rewarded. . ."
                    else:
                        ch_r "Heh, I suppose I can hardly refuse ya when you use the magic words . . ."
                elif Girl == KittyX:
                    if "no_topless" in Girl.recent_history:
                        ch_k "You just don't know when to quit. . . but you got lucky this time. . ."
                    else:
                        ch_k "You[Girl.like]know how to ask nicely . . ."
                elif Girl == EmmaX:
                    if "no_topless" in Girl.recent_history:
                        ch_e "Fine, I can't take your constant begging."
                    else:
                        ch_e "Well, I suppose if you ask nicely . . ."
                elif Girl == LauraX:
                    ch_l "Fine, you thirsty weirdo."
                elif Girl == JeanX:
                    if "no_topless" in Girl.recent_history:
                        ch_j "Oh, whatever."
                    else:
                        ch_j "I guess. . ."
                elif Girl == StormX:
                    ch_s "Oh, very well."
                elif Girl == JubesX:
                    ch_v "Ok, fine, geeze."
                $ Girl.top_pulled_up = 1
                "[Girl.name] just pulls her top up over her tits."
                $ Girl.outfit["gloves"] = ""
                $ Girl.change_stat("inhibition", 30, 2)
                $ Girl.change_stat("inhibition", 60, 1)
                call expression Girl.tag + "_First_Topless"
            elif "no_topless" in Girl.recent_history:
                $ Girl.change_face("_angry")
                if Girl == RogueX:
                    ch_r "Nuh uh, [Girl.player_petname]."
                elif Girl == KittyX:
                    ch_k "Noooope!"
                elif Girl == EmmaX:
                    ch_e "Again, no."
                elif Girl == LauraX:
                    ch_l "Still no."
                elif Girl == JeanX:
                    ch_j "Still a \"no\" on that, [Girl.player_petname]."
                elif Girl == StormX:
                    ch_s "Not today, no."
                elif Girl == JubesX:
                    ch_v "Nah. . ."
                $ Girl.change_stat("love", 80, -5)
                $ Girl.recent_history.append("_angry")
                $ Girl.daily_history.append("_angry")
            else:
                $ Girl.change_face("_sexy")
                call Top_Off_Refused (Girl)


        "Lose the [Girl.outfit[gloves]], at least. . ." if Girl.outfit["gloves"]:
            $ Girl.change_face("_sexy")
            Girl.voice "Oh, all right."
            $ line = Girl.outfit["gloves"]
            $ Girl.outfit["gloves"] = ""
            "She pulls off her [line]."
        "No, topless or nothing.":

            call ToplessorNothing (Girl)
        "Never mind.":

            pass

    $ Girl.recent_history.append("ask topless")
    $ Girl.daily_history.append("ask topless")
    $ approval_bonus = 0
    return


label Top_Off_Refused(Girl=0):

    $ Girl = check_girl(Girl)
    call shift_focus (Girl)

    $ Girl.change_face("_angry")
    if Girl == RogueX:
        if "no_topless" in Girl.recent_history:
            ch_r "Get a clue, [Girl.player_petname]."
        elif "no_topless" in Girl.daily_history:
            ch_r "Give it a rest, [Girl.player_petname]."
        else:
            $ Girl.change_face("_sad")
            ch_r "I'm afraid not this time, [Girl.player_petname]. Sure we can't have some fun anyway?"
    elif Girl == KittyX:
        if "no_topless" in Girl.recent_history:
            ch_k "[Girl.Like]back off."
        elif "no_topless" in Girl.daily_history:
            ch_k "Not today, maybe not ever, [Girl.player_petname]."
        else:
            $ KittyX.change_face("_sad")
            ch_k "[Girl.Like], no way, but I don't want to go. . ."
    elif Girl == EmmaX:
        if "no_topless" in Girl.recent_history:
            ch_e "You should probably back off now."
        elif "no_topless" in Girl.daily_history:
            ch_e "I'm tired of this, [Girl.player_petname]."
        else:
            ch_e "Is this a dealbreaker for you?"
    elif Girl == LauraX:
        if "no_topless" in Girl.recent_history:
            ch_l "You're getting real close to the line, [Girl.player_petname]."
        elif "no_topless" in Girl.daily_history:
            ch_l "You keep coming back with this, [Girl.player_petname]."
        else:
            ch_l "Let it go?"
    elif Girl == JeanX:
        if "no_topless" in Girl.recent_history:
            ch_j "Step carefully, [Girl.player_petname]."
        elif "no_topless" in Girl.daily_history:
            ch_j "Still on about that?"
        else:
            ch_j "Careful. . ."
    elif Girl == StormX:
        if "no_topless" in Girl.recent_history:
            ch_s "I will not move on this."
        elif "no_topless" in Girl.daily_history:
            ch_s "Find your joy elsewhere, [Girl.player_petname]."
        else:
            ch_s "Do you insist on this path?"
    elif Girl == JubesX:
        if "no_topless" in Girl.recent_history:
            ch_v "I thought I was clear. . ."
        elif "no_topless" in Girl.daily_history:
            ch_v "Look, cut it out, [Girl.player_petname]."
        else:
            ch_v "Whoa, slow your roll there. . ."
    menu:
        extend ""
        "Sure, never mind." if "no_topless" not in Girl.recent_history:
            $ Girl.change_face("_sexy")
            $ Girl.change_stat("love", 70, 2)
            if Girl == RogueX or Girl == KittyX:
                Girl.voice "Great!"
            else:
                Girl.voice "Good."
        "Sorry, I'll drop it." if "no_topless" in Girl.recent_history:
            if Girl == RogueX:
                ch_r "Fine. . ."
            elif Girl == KittyX:
                ch_k "Good!"
            else:
                Girl.voice "Good."
        "No, I insist. . .":
            $ Girl.brows = "_angry"
            if Girl == RogueX:
                $ Girl.brows = "_confused"
                ch_r "Ok [Girl.player_petname], your loss."
            elif Girl == KittyX:
                ch_k "Fine then!"
            elif Girl == EmmaX:
                ch_e "Very well."
            elif Girl == LauraX:
                ch_l "Your funeral."
            elif Girl == JeanX:
                $ Girl.change_face("_smile")
                ch_j "Well that was at least good for a laugh."
            elif Girl == StormX:
                ch_s "So be it."
            elif Girl == JubesX:
                ch_v "Too bad then. . ."
            $ Girl.change_stat("lust", 50, 5)
            $ Girl.change_stat("love", 70, -2, 1)
            if "no_topless" not in Girl.recent_history:
                $ Girl.change_stat("obedience", 60, 4)
            $ Girl.recent_history.append("_angry")
            $ Girl.daily_history.append("_angry")
    $ Girl.recent_history.append("no_topless")
    $ Girl.daily_history.append("no_topless")
    return


label ToplessorNothing(Girl=0):

    $ Girl = check_girl(Girl)
    call shift_focus (Girl)

    $ Girl.change_face("_angry")
    if approval_check(Girl, 800, "OI", taboo_modifier = 4) and approval_check(Girl, 400, "O", taboo_modifier = 3):
        $ Girl.change_stat("love", 20, -2, 1)
        $ Girl.change_stat("love", 70, -5, 1)
        $ Girl.change_stat("inhibition", 60, 3)
        $ Girl.change_face("_sad")
        if Girl == RogueX:
            if "no_topless" in Girl.recent_history:
                ch_r "Ok, ok, whatever."
            else:
                ch_r "Fine, if that's what you want."
        elif Girl == KittyX:
            if "no_topless" in Girl.recent_history:
                ch_k "Ok, fine. This time."
            else:
                $ Girl.change_face("_sad")
                ch_k "Whatever."
        elif Girl == EmmaX:
            if "no_topless" in Girl.recent_history:
                ch_e "Oh, very well. . ."
            else:
                $ Girl.change_face("_sad")
                ch_e "Fine."
        elif Girl == LauraX:
            if "no_topless" in Girl.recent_history:
                ch_l "Hrmph, whatever. . ."
            else:
                $ Girl.change_face("_sad")
                ch_l "Ugh, whatever."
        elif Girl == JeanX:
            if "no_topless" in Girl.recent_history:
                ch_j "Ok, fine. . ."
            else:
                $ Girl.change_face("_sad")
                ch_j "Fine! . . whatever."
        elif Girl == StormX:
            $ Girl.change_face("_sad")
            if "no_topless" in Girl.recent_history:
                ch_s "I suppose sometimes I must. . ."
            else:
                ch_s "Fine."
        elif Girl == JubesX:
            if "no_topless" in Girl.recent_history:
                ch_v "Ok, fine, just quit asking."
            else:
                ch_v "Ok, fine, whatever."
        $ Girl.change_stat("obedience", 60, 4)
        $ Girl.change_stat("obedience", 90, 2)
        $ Girl.top_pulled_up = 1
        "[Girl.name] slowly pulls her top up over her tits."
        call expression Girl.tag + "_First_Topless"
    else:
        $ Girl.change_stat("love", 200, -10)
        $ Girl.change_stat("obedience", 40, -1, 1)
        if Girl == RogueX:
            if "no_topless" in Girl.recent_history:
                ch_r "Seriously, cut this shit out."
            else:
                $ Girl.brows = "_confused"
                ch_r "\"Nothing\" it is then."
        elif Girl == KittyX:
            if "no_topless" in Girl.recent_history:
                ch_k "It[Girl.like]wasn't cute the first time."
            else:
                $ Girl.brows = "_angry"
                ch_k "[Girl.Like]no way!"
        elif Girl == EmmaX:
            if "no_topless" in Girl.recent_history:
                $ Girl.brows = "_angry"
                ch_e "Learn to take \"no\" for an answer."
            else:
                ch_e "I'm afraid not."
        elif Girl == LauraX:
            if "no_topless" in Girl.recent_history:
                $ Girl.brows = "_angry"
                ch_l "You have got to chill."
            else:
                ch_l "Nope."
        elif Girl == JeanX:
            if "no_topless" in Girl.recent_history:
                $ Girl.brows = "_angry"
                ch_j "Keep it under control."
            else:
                ch_j "Oh, no."
        elif Girl == StormX:
            if "no_topless" in Girl.recent_history:
                $ Girl.brows = "_angry"
                ch_s "I say again, \"no.\"."
            else:
                ch_s "Then that would be a \"no.\"."
        elif Girl == JubesX:
            if "no_topless" in Girl.recent_history:
                $ Girl.brows = "_angry"
                ch_v "Look, I told you, \"no.\"."
            else:
                ch_v "Sorry, no go."
        $ Girl.recent_history.append("no_topless")
        $ Girl.daily_history.append("no_topless")
        $ Girl.recent_history.append("_angry")
        $ Girl.daily_history.append("_angry")
    return


label Bottoms_Off(Girl=0, Intro=1, line=0, counter=0):
    $ Girl = check_girl(Girl)
    call shift_focus (Girl)

    if not Girl.outfit["bottom"] and not Girl.outfit["underwear"] and not Girl.outfit["hose"]:

        $ approval_bonus = 0
        return

    if "_angry" in Girl.recent_history:
        if Girl == RogueX:
            ch_r "I'm just too annoyed to deal with this right now."
        elif Girl == KittyX:
            ch_k "The only \"kitty\" you're getting is up here."
        elif Girl == EmmaX:
            ch_e "I would give up on that."
        elif Girl == LauraX:
            ch_l "You're barking up the wrong tree."
        elif Girl == JeanX:
            ch_j "Definitely not, [Girl.player_petname]."
        elif Girl == StormX:
            ch_s "That is certainly optimistic."
            ch_s "No."
        elif Girl == JubesX:
            ch_v "Definitely not."
        return


    if Girl.seen_pussy and approval_check(Girl, 700):
        $ approval_bonus += 20
    elif not Girl.outfit["underwear"]:
        $ approval_bonus -= 20
    elif Girl.seen_underwear and approval_check(Girl, 500):
        $ approval_bonus += 5
    if Intro == "_dildo":
        $ approval_bonus += 20
    if "exhibitionist" in Girl.traits:
        $ approval_bonus += (taboo*5)
    if (Girl in Player.Harem or "sex friend" in Girl.player_petnames) and not taboo:
        $ approval_bonus += 10
    elif "ex" in Girl.traits:
        $ approval_bonus -= 40
    if "no_bottomless" in Girl.recent_history:
        $ approval_bonus -= 20
    elif Girl == StormX and (not taboo or Girl in Rules):

        $ approval_bonus += 20

    if Intro:
        if Intro == 2 and Girl.bottom_number() > 5:

            if Girl == RogueX:
                ch_r "I don't know, I might need my knickers off for that. . ."
            elif Girl == KittyX:
                ch_k "So, you'd have to be able to[KittyX.like]touch down there, I guess. . ."
            elif Girl == EmmaX:
                ch_e "I would probably need to lose these to get anything out of that. . ."
            elif Girl == LauraX:
                ch_l "I'd need to be pantsless to get anything from that. . ."
            elif Girl == JeanX:
                ch_j "I guess I'd have to go bottomless. . ."
            elif Girl == StormX:
                ch_s "I will remove these then. . ."
            elif Girl == JubesX:
                ch_v "I guess these would get in the way. . ."
        else:
            if Girl.outfit["bottom"] and not Girl.upskirt:
                ch_p "This might be easier without your [Girl.outfit[bottom]] on."
            elif Girl.outfit["underwear"] and not Girl.underwear_pulled_down:
                ch_p "This might be easier without your [Girl.outfit[underwear]] on."

    $ approval = approval_check(Girl, 1200, taboo_modifier = 5)

    if action_context == "auto":
        $ counter = 0

        if not Girl.upskirt and not Girl.underwear_pulled_down:
            if Girl.bottom_number() == 5:

                if approval >= 2 or (Girl.seen_pussy and not taboo):
                    $ Girl.change_stat("inhibition", 60, 1)
                    if taboo:
                        $ Girl.change_stat("inhibition", 90, (int(taboo/20)))
                    $ Girl.upskirt = 1
                    "She slides her skirt up."
                    $ counter = 1

            if Girl.bottom_number() >= 6 or Girl.hose_number() >= 6:
                if Girl.outfit["underwear"]:

                    if not approval or (not Girl.seen_underwear and taboo):
                        return
                elif approval < 2 or (not Girl.seen_pussy and taboo):
                    return
                elif Girl.upskirt:
                    return
                $ Girl.change_stat("inhibition", 60, 1)
                if Girl.hose_number() >= 6:
                    $ line = Girl.outfit["hose"]
                    $ Girl.outfit["hose"] = ""
                $ Girl.upskirt = 1

                if Girl == KittyX:
                    if Girl.bottom_number(0) >= 6:
                        "[Girl.name] grumbles to herself, and then allows her [Girl.outfit[bottom]] to drop down her legs."
                    else:
                        "[Girl.name] grumbles to herself, and then allows her [line] to drop down her legs."
                    if Girl.outfit["underwear"]:
                        $ Girl.seen_underwear = 1
                elif Girl.outfit["underwear"]:
                    if Girl.bottom_number(0) >= 6:
                        "[Girl.name] grumbles to herself, and then unzips her [Girl.outfit[bottom]], sliding them down her legs."
                    else:
                        "[Girl.name] grumbles to herself, and then pulls her [line] down her legs."
                    $ Girl.seen_underwear = 1
                else:
                    if Girl.bottom_number(0) >= 6:
                        "[Girl.name] grumbles to herself, and then unzips her [Girl.outfit[bottom]], sliding them off her bare ass."
                    else:
                        "[Girl.name] grumbles to herself, and then pulls her [line] down her bare ass."
                call expression Girl.tag + "_First_Bottomless" pass (1)
                if taboo:
                    $ Girl.change_stat("inhibition", 90, (int(taboo/10)))
                $ counter = 1

        if Girl.outfit["underwear"] and not Girl.underwear_pulled_down:

            if approval >= 2 or (Girl.seen_pussy and not taboo):
                $ Girl.change_stat("inhibition", 70, 2)
                if taboo:
                    $ Girl.change_stat("inhibition", 90, (int(taboo/10)))
                $ Girl.underwear_pulled_down = 1
                if Girl.bottom_number() >= 6 or Girl.hose_number() >= 6:
                    $ Girl.upskirt = 1
                if Girl == KittyX:
                    if counter:
                        "With a second thought, [Girl.name] lets her [Girl.outfit[underwear]] drop too."
                    else:
                        "[Girl.name] tsks in irritation, and her [Girl.outfit[underwear]] slide off to the ground."
                else:
                    if counter:
                        "[Girl.name] tsks in irritation, and pulls down her [Girl.outfit[underwear]] too."
                    else:
                        "[Girl.name] tsks in irritation, and pulls down her [Girl.outfit[underwear]]."
                call expression Girl.tag + "_First_Bottomless" pass (1)
                if Girl == RogueX:
                    ch_r "I wasn't getting anything out of it with those on. Give it another go."
                elif Girl == KittyX:
                    ch_k "It's super annoying not being able to phase you through these."
                elif Girl == EmmaX:
                    ch_e "That was just in the way."
                elif Girl == LauraX:
                    ch_l "I guess all that was in the way."
                elif Girl == JeanX:
                    ch_j "Ok, see if you can make that work, [Girl.player_petname]."
                elif Girl == StormX:
                    ch_s "That should simplify things. . ."
                elif Girl == JubesX:
                    ch_v "Ok, that's a bit more comfortable. . ."
        return


    if approval >= 2:

        $ Girl.change_face("_sexy", 1)
        if Girl.forced:
            $ Girl.change_face("_sad", 1)
            $ Girl.change_stat("love", 20, -2, 1)
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 60, 1)
        if Girl == RogueX:
            if approval >= 3:
                $ line = "Hmmm, what do you want to see? . ."
            else:
                $ line = "Well, ok. I'd kinda like to keep {i}some{/i} modesty though. . ."
        elif Girl == KittyX:
            if approval >= 3:
                $ line = "Heh, what would you like to see? . ."
            else:
                $ line = "Ok, maybe, but don't push it. . ."
        elif Girl == EmmaX:
            if approval >= 3:
                $ line = "Mmmm, what would you like?"
            else:
                $ line = "What would you have me take off?"
        elif Girl == LauraX:
            if approval >= 3:
                $ line = "What did you want off?"
            else:
                $ line = "Hm, what did you want me to lose?"
        elif Girl == JeanX:
            if approval >= 3:
                $ line = "What did you want off?"
            else:
                $ line = "Like. . . what? . ."
        elif Girl == StormX:
            $ line = "What would you have me remove?"
        elif Girl == JubesX:
            $ line =  "Well like what did you have in mind here?"
        call Bottoms_Off_Legs (Girl)

        if not Girl.outfit["underwear"] and Girl.recent_history.count("bottomless") < 2:
            $ Girl.change_stat("obedience", 50, 1)
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 50, 3)
            $ Girl.change_stat("lust", 80, 3)

    elif Girl.outfit["bottom"] or Girl.outfit["underwear"] or Girl.outfit["hose"]:

        $ Girl.change_face("_bemused", 1)
        if Girl == RogueX:
            if "no_bottomless" in Girl.recent_history:
                $ Girl.change_face("_angry")
                ch_r "What did I just tell you, [Girl.player_petname]?"
            elif "no_topless" in Girl.recent_history:
                $ Girl.change_face("_angry")
                ch_r "I doubt your odds will be better here, [Girl.player_petname]. . ."
            elif approval and not Girl.seen_pussy:
                ch_r "Not everything, right?"
            elif not Girl.seen_pussy and "ask topless" in Girl.recent_history:
                ch_r "I'm not ready to show you that either."
            elif "no_bottomless" in Girl.daily_history:
                ch_r "Have you forgot what I said earlier, [Girl.player_petname]?"
            elif taboo:
                ch_r "I don't know about doing it here. . ."
            elif approval:
                ch_r "I don't know if I want to take my bottoms off. . ."
            elif Girl.seen_pussy:
                ch_r "Well, you've seen it before, but. . ."
            else:
                ch_r "I'm not taking my bottoms off."
        elif Girl == KittyX:
            if "no_bottomless" in Girl.recent_history:
                $ KittyX.change_face("_angry")
                ch_k "Last warning, [Girl.player_petname]. No."
            elif "no_topless" in Girl.recent_history:
                $ KittyX.change_face("_angry")
                ch_k "Not learning from your mistakes here, [Girl.player_petname]. . ."
            elif approval and not Girl.seen_pussy:
                ch_k "I'm not sure about that. . ."
            elif not Girl.seen_pussy and "ask topless" in Girl.recent_history:
                ch_k "That's a bit too far."
            elif "no_bottomless" in Girl.daily_history:
                ch_k "Short memory, [Girl.player_petname]?"
            elif taboo:
                ch_k "This is[Girl.like]kinda public. . ."
            elif approval:
                ch_k "I'm[Girl.like]not sure about this. . ."
            elif Girl.seen_pussy:
                ch_k "Well, you've seen[Girl.like]it before . . ."
            elif Girl.bottom_number(0) > 6:
                ch_k "I'm keeping my pants on."
            elif Girl.bottom_number(0) > 5:
                ch_k "I'm keeping my shorts on."
            else:
                ch_k "I'm keeping my panties on."
        elif Girl == EmmaX:
            if "no_bottomless" in Girl.recent_history:
                $ EmmaX.change_face("_angry")
                ch_e "Stop asking, you're embarrassing yourself."
            elif "no_topless" in Girl.recent_history:
                $ EmmaX.change_face("_angry")
                ch_e "Do you really think that's likely?"
            elif approval and not Girl.seen_pussy:
                ch_e "I don't know if you're ready for that."
            elif not Girl.seen_pussy and "ask topless" in Girl.recent_history:
                ch_e "Be careful how far you push it. . ."
            elif "no_bottomless" in Girl.daily_history:
                ch_e "Don't you learn anything, [Girl.player_petname]?"
            elif taboo:
                ch_e "Not with so many eyes around, [Girl.player_petname]. . ."
            elif approval:
                ch_e "Probably not. . ."
            elif Girl.seen_pussy:
                ch_e "I think you've seen enough . . ."
            elif Girl.bottom_number(0) > 6:
                ch_e "I'm keeping my pants on."
            elif Girl.bottom_number(0) == 5:
                ch_e "I'm keeping my skirt on."
            elif Girl.bottom_number(0) == 6:
                ch_e "I'm keeping my shorts on."
            else:
                ch_e "I'm keeping my panties on."
        elif Girl == LauraX:
            if "no_bottomless" in Girl.recent_history:
                $ LauraX.change_face("_angry")
                ch_l "Now you're just embarrassing yourself."
            elif "no_topless" in Girl.recent_history:
                $ LauraX.change_face("_angry")
                ch_l "This is really pushing it."
            elif approval and not Girl.seen_pussy:
                ch_l "I don't know if you're earned that yet."
            elif not Girl.seen_pussy and "ask topless" in Girl.recent_history:
                ch_l "Kinda pushing it, [Girl.player_petname]. . ."
            elif "no_bottomless" in Girl.daily_history:
                ch_l "So thirsty. . ."
            elif taboo:
                ch_l "This is pretty exposed, [Girl.player_petname]. . ."
            elif approval:
                ch_l "Probably not. . ."
            elif Girl.seen_pussy:
                ch_l "You've probably seen enough . . ."
            elif Girl.bottom_number(0) > 6:
                ch_l "Well, I'm keeping my pants on."
            elif Girl.bottom_number(0) == 5:
                ch_l "Well, I'm keeping my skirt on."
            elif Girl.bottom_number(0) == 6:
                ch_l "Well, I'm keeping my shorts on."
            else:
                ch_l "Well, I'm keeping my panties on."
        elif Girl == JeanX:
            if "no_bottomless" in Girl.recent_history:
                $ JeanX.change_face("_angry")
                ch_j "Look, it's just not happening."
            elif "no_topless" in Girl.recent_history:
                $ JeanX.change_face("_angry")
                ch_j "Why did you think that would be different?"
            elif approval and not Girl.seen_pussy:
                ch_j "Hmm. . . have your earned that. . ."
            elif "no_bottomless" in Girl.daily_history:
                ch_j "Again with this?"
            elif taboo:
                ch_j "Not here, [Girl.player_petname]. . ."
            elif approval:
                ch_j "Hmm. . ."
            elif Girl.seen_pussy:
                ch_j "Hmm. . ."
            elif Girl.bottom_number(0) > 6:
                ch_j "I'm keeping my pants on though."
            elif Girl.bottom_number(0) == 5:
                ch_j "I'm keeping my skirt on though."
            elif Girl.bottom_number(0) == 6:
                ch_j "I'm keeping my shorts on though."
            else:
                ch_j "I'm keeping my panties on though."
        elif Girl == StormX:
            if "no_bottomless" in Girl.recent_history:
                $ StormX.change_face("_angry")
                ch_s "You need to stop asking about that."
            elif taboo and Girl not in Rules:
                ch_s "I cannot in public, [Girl.player_petname]. . ."
            elif approval:
                ch_s "I am unsure. . ."
            elif Girl.bottom_number(0) > 6:
                ch_s "I will be keeping my pants on."
            elif Girl.bottom_number(0) == 5:
                ch_s "I will be keeping my skirt on."
            elif Girl.bottom_number(0) == 6:
                ch_s "I will be keeping my shorts on."
            else:
                ch_s "I will be keeping my panties on."
        elif Girl == JubesX:
            if "no_bottomless" in Girl.recent_history:
                $ JubesX.change_face("_angry")
                ch_v "Don't have a cow, dude."
            elif "no_topless" in Girl.recent_history:
                $ JubesX.change_face("_angry")
                ch_v "Don't push it, [Girl.player_petname]."
            elif approval and not Girl.seen_pussy:
                ch_v "I don't know, man."
            elif not Girl.seen_pussy and "ask topless" in Girl.recent_history:
                ch_v "Kinda pushing it, [Girl.player_petname]. . ."
            elif "no_bottomless" in Girl.daily_history:
                ch_v "So thirsty. . ."
            elif taboo:
                ch_v "[Girl.player_petname], it's just public here?"
            elif approval:
                ch_v "Doubtful. . ."
            elif Girl.seen_pussy:
                ch_v "Need another look?"
            elif Girl.bottom_number(0) > 6:
                ch_v "Well, I'm keeping my pants on."


            elif Girl.bottom_number(0) == 6:
                ch_v "Well, I'm keeping my shorts on."
            else:
                ch_v "Well, I'm keeping my panties on."
        menu:
            extend ""
            "Ok, never mind." if "no_bottomless" not in Girl.recent_history:
                if "ask bottomless" not in Girl.daily_history:
                    $ Girl.change_stat("lust", 80, 2)
                    $ Girl.change_stat("love", 70, 1)
                    $ Girl.change_stat("love", 90, 1)
                    $ Girl.change_stat("inhibition", 50, 3)
                if Girl.forced:
                    $ Girl.mouth = "_smile"
                    if Girl == RogueX:
                        ch_r "I really appreciate that."
                    elif Girl == KittyX:
                        ch_k ". . . thank you."
                    elif Girl == EmmaX:
                        ch_e "Very. . . generous."
                    elif Girl == LauraX:
                        ch_l "Right."
                    elif Girl == JeanX:
                        ch_j ". . ."
                    elif Girl == StormX:
                        ch_s "Thank you. . ."
                    elif Girl == JubesX:
                        ch_v "Thanks. . ."
                    if "ask bottomless" not in Girl.daily_history:
                        $ Girl.change_stat("love", 20, 3)
                        $ Girl.change_stat("love", 70, 4)
                        $ Girl.change_stat("inhibition", 60, 2)

            "Sorry, sorry." if "no_bottomless" in Girl.recent_history:
                if Girl == RogueX:
                    ch_r "Ok, fine, just chill out about it."
                elif Girl == KittyX:
                    ch_k "[Girl.Like], fine, whatever."
                else:
                    Girl.voice "Good."
            "Come on, please?":

                if "no_bottomless" in Girl.daily_history:
                    $ Girl.change_face("_angry", 1)
                    if Girl == RogueX:
                        ch_r "Listen up when I tell you \"no.\""
                    elif Girl == KittyX:
                        ch_k "I already told you \"no.\""
                    elif Girl == EmmaX:
                        ch_e "I believe you've heard my answer on that."
                    elif Girl == LauraX:
                        ch_l "You heard me."
                    elif Girl == JeanX:
                        ch_j "Are you deaf, or stupid?"
                    elif Girl == StormX:
                        ch_s "I have spoken on the matter."
                    elif Girl == JubesX:
                        ch_v "No."
                else:
                    if approval and approval_check(Girl, 600, "L", taboo_modifier=1):
                        $ Girl.change_face("_sexy", 1)
                        $ D20 = renpy.random.randint(1, 3)
                        $ approval += 1 if D20 == 3 else 0
                        if Girl == RogueX:
                            $ line = "Well, what were you thinking then. . ."
                        elif Girl == KittyX:
                            $ line = "I guess. . ."
                        elif Girl == EmmaX:
                            $ line = "Perhaps. . ."
                        elif Girl == LauraX:
                            $ line = "Maybe. . ."
                        elif Girl == JeanX:
                            $ line = "-sigh-. . . like what?"
                        elif Girl == StormX:
                            ch_s ". . ."
                            $ line = "What did you want? . ."
                        elif Girl == JubesX:
                            $ line =  "I mean, maaaybe. . ."
                        call Bottoms_Off_Legs (Girl)
                    else:
                        $ Girl.change_face("_sexy")
                        call Bottoms_Off_Refused (Girl)

            "It doesn't have to be everything. . ." if Girl.outfit["bottom"] or Girl.hose_number() >= 10 or Girl.outfit["underwear"] == "_shorts":
                if approval and "no_bottomless" not in Girl.daily_history:
                    $ Girl.change_face("_bemused", 1)
                    $ line = "Well what did you have in mind then?"
                    call Bottoms_Off_Legs (Girl)
                else:

                    $ Girl.change_face("_sexy")
                    call Bottoms_Off_Refused (Girl)
            "It doesn't have to be everything. . . (locked)" if not Girl.outfit["bottom"] and Girl.hose_number() < 10 and Girl.outfit["underwear"] != "_shorts":
                pass
            "No, lose 'em.":

                if (approval and Girl.obedience >= 250) or (approval_check(Girl, 850, "OI", taboo_modifier = 5) and approval_check(Girl, 400, "O")):
                    $ Girl.change_stat("love", 20, -1, 1)
                    $ Girl.change_stat("love", 70, -5, 1)
                    $ Girl.change_stat("obedience", 50, 4)
                    $ Girl.change_stat("inhibition", 60, 3)
                    if Girl == RogueX:
                        $ line =  "Fine, if that's what you want. What do you want to see?"
                    elif Girl == KittyX:
                        $ line =  "Like geez, you're serious. . ."
                    elif Girl == EmmaX:
                        $ line =  "Don't test me. . ."
                    elif Girl == LauraX:
                        $ line =  "Don't push me. . ."
                    elif Girl == JeanX:
                        $ line = "Think very carefully. . ."
                    elif Girl == StormX:
                        ch_s ". . ."
                        $ line = "What did you want? . ."
                    elif Girl == JubesX:
                        $ line =  "Tone. . ."
                    $ approval = 1 if approval < 1 else approval
                    $ Girl.forced = 1
                    call Bottoms_Off_Legs (Girl)
                else:
                    $ Girl.change_stat("love", 200, -10)
                    if approval_check(Girl, 400, "O"):
                        if Girl == RogueX:
                            ch_r "I. . . I really can't."
                        elif Girl == KittyX:
                            ch_k "Sorry[Girl.like]no way."
                        elif Girl == EmmaX:
                            ch_e "Definitely not."
                        elif Girl == LauraX:
                            ch_l "No way."
                        elif Girl == JeanX:
                            ch_j "Ha! No."
                        elif Girl == StormX:
                            ch_s "I am sorry, no."
                        elif Girl == JubesX:
                            ch_v "Definitely not."
                    else:
                        $ Girl.change_face("_angry")
                        if Girl == RogueX:
                            ch_r "Well fuck off then!"
                        elif Girl == KittyX:
                            ch_k "GTFO."
                        elif Girl == EmmaX:
                            ch_e "Out of my sight, [Girl.player_petname]."
                        elif Girl == LauraX:
                            ch_l "Fuck off."
                        elif Girl == JeanX:
                            ch_j "Not even."
                        elif Girl == StormX:
                            ch_s "No."
                        elif Girl == JubesX:
                            ch_v "Nah. . ."
                        $ Girl.recent_history.append("_angry")
                        $ Girl.daily_history.append("_angry")
                    $ Girl.recent_history.append("no_bottomless")
                    $ Girl.daily_history.append("no_bottomless")

    $ approval_bonus = 0
    $ Girl.recent_history.append("ask bottomless")
    $ Girl.daily_history.append("ask bottomless")
    return

label Bottoms_Off_Legs(Girl=0):
    $ Girl = check_girl(Girl)
    call shift_focus (Girl)

    if Girl.forced:
        $ Girl.change_face("_sad", 1)
    elif approval_check(Girl, 1100, "OI", taboo_modifier = 3):
        $ Girl.change_face("_sly")
    elif approval_check(Girl, 1400, taboo_modifier = 3):
        $ Girl.change_face("_sexy", 1)
    else:
        $ Girl.change_face("_bemused", 1)

    $ line = "Well what did you want off?" if not line else line
    $ counter = 1
    while counter and (Girl.outfit["bottom"] or Girl.outfit["underwear"] or Girl.outfit["hose"]):
        Girl.voice "[line]"
        menu:
            extend ""

            "Take it all off" if line != "Well what did you have in mind then?":

                if not Girl.outfit["underwear"] and Girl.hose_number() < 10:
                    call NoPantiesOn (Girl)

                if Girl.outfit["bottom"]:
                    $ line = Girl.outfit["bottom"]
                    $ Girl.outfit["bottom"] = ""
                    if not Girl.seen_underwear:
                        if Girl == RogueX:
                            "[Girl.name] shyly removes her [line]."
                        elif Girl == KittyX:
                            "[Girl.name] shyly tugs her [line] off of her legs."
                        else:
                            "[Girl.name] pulls off her [line]."
                        $ Girl.seen_underwear = 1
                    else:
                        "[Girl.name] pulls her [line] off."

                if approval < 2 and not Girl.outfit["underwear"] and Girl.hose_number() >= 10:
                    call NoPantiesOn (Girl)

                if Girl == JubesX and JubesX.outfit["front_outer_accessory"] != "_shut_jacket":

                    pass
                elif Girl == JubesX and JubesX.outfit["front_outer_accessory"] == "_shut_jacket":
                    $ Girl.outfit["front_outer_accessory"] = ""
                    "She pulls her [Girl.outfit[front_outer_accessory]] off."
                    call expression Girl.tag + "_First_Bottomless"
                elif Girl.outfit["front_outer_accessory"]:
                    $ Girl.outfit["front_outer_accessory"] = ""
                    "She pulls her [Girl.outfit[front_outer_accessory]] off."

                if Girl.outfit["hose"]:
                    $ line = Girl.outfit["hose"]
                    $ Girl.outfit["hose"] = ""
                    if Girl == KittyX:
                        "Her [line] drop to the ground in a heap."
                    else:
                        "She pulls her [line] down."

                if approval < 2:
                    call NoPantiesOn (Girl)

                if Girl.outfit["underwear"]:
                    $ line = Girl.outfit["underwear"]
                    $ Girl.outfit["underwear"] = ""
                    if Girl == KittyX:
                        "She glances up at you as her [line] fall clear of her."
                    else:
                        "She glances up at you as she removes her [line]."
                call expression Girl.tag + "_First_Bottomless"


            "Lose the [Girl.outfit[bottom]]." if Girl.outfit["bottom"]:
                if Girl.outfit["underwear"] and approval >= 2:
                    $ Girl.change_face("_sexy")
                    if Girl == RogueX:
                        ch_r "I guess I could do that. . ."
                    elif Girl == KittyX:
                        ch_k "That's. . . doable. . ."
                    elif Girl == EmmaX:
                        ch_e "I can manage that. . ."
                    elif Girl == LauraX:
                        ch_l "I guess I could. . ."
                    elif Girl == JeanX:
                        ch_j ". . .I guess. . ."
                    elif Girl == StormX:
                        ch_s "I could do that. . ."
                    elif Girl == JubesX:
                        ch_v "Well, I could do that. . ."
                elif approval:
                    $ Girl.change_face("_sexy", 1)
                    if approval < 2 and not Girl.outfit["underwear"] and Girl.hose_number() < 10:
                        call NoPantiesOn (Girl)
                else:
                    $ Girl.change_face("_sexy")
                    call Bottoms_Off_Refused (Girl)
                    return

                $ line = Girl.outfit["bottom"]
                $ Girl.outfit["bottom"] = ""
                if not Girl.outfit["underwear"] and Girl.hose_number() < 10:
                    $ Girl.change_face("_sly", 2)
                    if Girl == KittyX:
                        "She blushes and looks at you as her [line] drops at her feet."
                    elif Girl == RogueX:
                        "She blushes and looks at you slyly before removing her [line]."
                    else:
                        "She glaces at you slyly before removing her [line]."
                    call expression Girl.tag + "_First_Bottomless"
                elif not Girl.seen_underwear:
                    if Girl == KittyX:
                        "She blushes and looks at you as her [line] drops at her feet."
                    elif Girl == RogueX:
                        "She blushes and looks at you slyly before removing her [line]."
                    else:
                        "She glaces at you slyly before removing her [line]."
                    $ Girl.seen_underwear = 1
                else:
                    "[Girl.name] pulls her [line] off."
                $ Girl.change_face("_bemused", 1)

            "Lose the [Girl.outfit[underwear]]." if Girl.outfit["underwear"]:
                if approval < 2:
                    if Girl == RogueX:
                        ch_r "No thanks, [Girl.player_petname]."
                    elif Girl == KittyX:
                        ch_k "Sorry, no."
                    elif Girl == EmmaX:
                        ch_e "I'm afraid not."
                    elif Girl == LauraX:
                        ch_l "No way."
                    elif Girl == JeanX:
                        ch_j "Ha! No way."
                    elif Girl == StormX:
                        ch_s "I would rather not."
                    elif Girl == JubesX:
                        ch_v "Um, no thanks. . ."
                    $ Girl.recent_history.append("no_bottomless")
                    $ Girl.daily_history.append("no_bottomless")
                    return
                elif Girl.bottom_number() >= 6 or Girl.hose_number() >= 6:
                    if Girl == RogueX:
                        ch_r "A little backwards, but sure. . ."
                    elif Girl == KittyX:
                        ch_k "[Girl.Like]I guess. . ."
                    elif Girl == EmmaX:
                        ch_e "I suppose that I could. . ."
                    elif Girl == LauraX:
                        ch_l "Huh, ok. . ."
                    elif Girl == JeanX:
                        ch_j "Hmm. . . I guess. . ."
                    elif Girl == StormX:
                        ch_s "I could do that. . ."
                    elif Girl == JubesX:
                        ch_v "Well, I could do that. . ."
                else:
                    if Girl == EmmaX:
                        ch_e "Of course."
                    elif Girl == LauraX:
                        ch_l "Huh, ok. . ."
                    elif Girl == StormX:
                        ch_s "Fine."
                    else:
                        Girl.voice "Ok, sure, [Girl.player_petname]."
                $ line = Girl.outfit["underwear"]
                $ Girl.outfit["underwear"] = ""
                if Girl == KittyX:
                    if Girl.bottom_number() >= 5:
                        "She reaches a hand into her [Girl.outfit[bottom]] and pulls her [line] out through the pocket."
                        "She gives a little wink as she drops them to the ground."
                    elif Girl.hose_number() >= 5:
                        "She reaches a hand into her [Girl.outfit[hose]] and pulls her [line] out through the pocket."
                        "She gives a little wink as she drops them to the ground."
                    else:
                        "With a little shimmy, her [line] drop to the ground."
                elif Girl.bottom_number() >= 6:
                    "She pulls her [Girl.outfit[bottom]] off, then removes her [line], before putting them back on."
                elif Girl.hose_number() >= 6:
                    "She pulls her [Girl.outfit[hose]] off, then removes her [line], before putting them back on."
                elif Girl == JubesX and JubesX.outfit["front_outer_accessory"] == "_shut_jacket":
                    "She reaches under her jacket and pulls her [line] down."
                elif Girl.outfit["bottom"]:
                    "She reaches under her [Girl.outfit[bottom]] and pulls her [line] down."
                else:
                    "She glances up at you as she removes her [line]."
                call expression Girl.tag + "_First_Bottomless"

            "Just give me a clear view. . ." if (Girl.outfit["underwear"] and not Girl.underwear_pulled_down) or (Girl.outfit["bottom"] and not Girl.upskirt):
                if approval >= 2:
                    if Girl == LauraX:
                        ch_l "Whatever."
                    else:
                        Girl.voice "Fine."
                    $ Girl.underwear_pulled_down = 1 if Girl.outfit["underwear"] else 0
                    $ Girl.upskirt = 1 if Girl.outfit["bottom"] else 0
                    if Girl.outfit["bottom"]:
                        "She shifts her [Girl.outfit[bottom]] out of the way."
                    else:
                        "She shifts her [Girl.outfit[underwear]] out of the way."
                elif approval >= 1 and Girl.outfit["bottom"] and Girl.outfit["underwear"] and not Girl.underwear_pulled_down:
                    if Girl == RogueX:
                        ch_r "I'll show you a little bit. . ."
                    elif Girl == KittyX:
                        ch_k "I guess I could show you something. . ."
                    elif Girl == EmmaX:
                        ch_e "I'll give at least give a little view. . ."
                    elif Girl == LauraX:
                        ch_l "Make do with this. . ."
                    elif Girl == JeanX:
                        ch_j "This should be plenty, [Girl.player_petname]."
                    elif Girl == StormX:
                        ch_s "I have taken off enough. . ."
                    elif Girl == JubesX:
                        ch_v "I guess. . . how 'bout this. . ."
                    $ Girl.upskirt = 1
                else:
                    Girl.voice "No."
                    $ Girl.recent_history.append("no_bottomless")
                    $ Girl.daily_history.append("no_bottomless")
                    return
                call expression Girl.tag + "_First_Bottomless"

            "Lose the [Girl.outfit[hose]]." if Girl.outfit["hose"]:
                $ Girl.change_face("_bemused", 1)
                if Girl.outfit["bottom"]:
                    Girl.voice "All right, fine."
                elif approval < 2 and not Girl.outfit["underwear"] and Girl.hose_number() >= 10:
                    call NoPantiesOn (Girl)
                elif not approval and Girl.hose_number() >= 6:
                    if Girl == RogueX:
                        ch_r "No thanks, [Girl.player_petname]."
                    else:
                        Girl.voice "Sorry, no, [Girl.player_petname]."
                    return
                else:
                    if Girl == RogueX:
                        ch_r "Ok, sure, [Girl.player_petname]."
                    else:
                        Girl.voice "Fine, [Girl.player_petname]."
                $ line = Girl.outfit["hose"]
                $ Girl.outfit["hose"] = ""
                if Girl == KittyX:
                    if Girl.bottom_number() >= 5:
                        "She reaches a hand into her [Girl.outfit[bottom]] and pulls her [line] right through her legs."
                        "She makes a little flourish and drops them to the ground."
                    else:
                        "She gives a little shake and her [line] drop to the ground."
                elif Girl.bottom_number() >= 6:
                    "She pulls off her [Girl.outfit[bottom]] and pulls her [line] off, then puts them back on."
                elif Girl.outfit["bottom"]:
                    "She reaches under her [Girl.outfit[bottom]] and pulls her [line] down."
                elif Girl.hose_number() < 10:
                    "[Girl.name] pulls her [line] off."
                elif not Girl.outfit["underwear"]:
                    $ Girl.change_face("_sly", 2)
                    "She blushes and looks at you slyly before removing her [line]."
                    $ Girl.blushing = "_blush1"
                    call expression Girl.tag + "_First_Bottomless"
                elif not Girl.seen_underwear:
                    "[Girl.name] shyly removes her [line]."
                    $ Girl.seen_underwear = 1
                else:
                    "[Girl.name] pulls her [line] off."

            "Rip the [Girl.outfit[hose]]." if Girl.outfit["hose"] == "_pantyhose" or Girl.outfit["hose"] == "_tights":
                $ Girl.change_face("_bemused", 1)
                if Girl.outfit["bottom"]:
                    Girl.voice "All right, fine."
                elif approval < 2 and not Girl.outfit["underwear"] and Girl.hose_number() >= 10:
                    call NoPantiesOn (Girl)
                elif not approval and Girl.hose_number() >= 6:
                    if Girl == RogueX:
                        ch_r "I'd rather you didn't, [Girl.player_petname]."
                    else:
                        Girl.voice "Sorry, no, [Girl.player_petname]."
                    return

                $ line = Girl.outfit["hose"]
                if Girl.outfit["hose"] == "_tights":
                    $ Girl.outfit["hose"] = "_ripped_tights"
                elif Girl.outfit["hose"] == "_pantyhose":
                    $ Girl.outfit["hose"] = "_ripped_pantyhose"
                if Girl.outfit["hose"] not in Girl.inventory:
                    $ Girl.inventory.append(Girl.outfit["hose"])
                $ Girl.add_word(1,"ripped", "ripped")
                "You tear holes in her [line]."
                if not approval_check(Girl, 1200, taboo_modifier=0):
                    $ Girl.change_face("_angry", 1,eyes="_down")
                    if Girl == RogueX:
                        ch_r "Dammit, [Girl.player_petname], those are gettin expensive!"
                    elif Girl == KittyX:
                        ch_k "Hey, I was using those!"
                    elif Girl == EmmaX:
                        ch_e "I hope you're paying for those."
                    elif Girl == LauraX:
                        ch_l "Hey. Not cool."
                    elif Girl == JeanX:
                        ch_j "Oh, whatever."
                    elif Girl == StormX:
                        ch_s "Those do not grow on trees. . ."
                    elif Girl == JubesX:
                        ch_v "Hey! You'd better replace those. . ."
                    $ Girl.change_face("_bemused", 1)

            "Why don't you lose the sweater?" if Girl.outfit["front_outer_accessory"] == "_sweater":
                $ Girl.outfit["front_outer_accessory"] = ""
                "[Girl.name] tosses her sweater off."

            "Keep it all on for now." if counter == 1:
                $ counter = 0

            "Ok, that's enough for now." if counter == 2:
                $ counter = 0

        $ counter = 2 if counter else counter
        $ line = "Anything else?"
    return


label NoPantiesOn(Girl=0):

    $ Girl = check_girl(Girl)
    call shift_focus (Girl)

    if not Girl.outfit["underwear"]:
        return

    if Girl == RogueX:
        if Girl.outfit["bottom"] or Girl.hose_number() >= 10:
            ch_r "Well, I'm not exactly decent under here, you know. . ."
        else:
            ch_r "This is the last bit. . ."
    elif Girl == KittyX:
        if Girl.outfit["bottom"] or Girl.hose_number() >= 10:
            ch_k "[Girl.Like]I'm not wearing any panties. . ."
        else:
            ch_k "Not much else on. . ."
    elif Girl == EmmaX:
        if Girl.outfit["bottom"] or Girl.hose_number() >= 10:
            ch_e "I don't have anything on under this. . ."
        else:
            ch_e "This is all I have on. . ."
    elif Girl == LauraX:
        if Girl.outfit["bottom"] or Girl.hose_number() >= 10:
            ch_l "I don't have anything on under this. . ."
        else:
            ch_l "These are all I have on. . ."
    elif Girl == JeanX:
        if Girl.outfit["bottom"] or Girl.hose_number() >= 10:
            ch_j "I don't have panties on right now. . ."
        else:
            ch_j ". . ."
    elif Girl == StormX:
        if Girl.outfit["bottom"] or Girl.hose_number() >= 10:
            ch_s "I am naked under this. . ."
        else:
            ch_s "This is all I have on. . ."
    elif Girl == JubesX:
        if Girl.bottom_number() >= 5 or Girl.hose_number() >= 10:
            ch_v "I don't have anything on under this. . ."
        else:
            ch_v "This is all I've got on. . ."
    menu:
        extend ""
        "Could you do it anyway?":
            if approval_check(Girl, 1000, "LI", taboo_modifier=1):
                if Girl == RogueX:
                    ch_r "Well, if you're gonna ask so nicely. . . "
                elif Girl == KittyX:
                    ch_k "I[Girl.like]guess so. . . "
                elif Girl == EmmaX:
                    ch_e "I suppose. . . "
                elif Girl == LauraX:
                    ch_l "I guess. . . "
                elif Girl == JeanX:
                    ch_j "Oh, why not. . ."
                elif Girl == StormX:
                    ch_s "I suppose I could. . ."
                elif Girl == JubesX:
                    ch_v "Well, guess. . ."
            else:
                if Girl == RogueX:
                    ch_r "Sorry, I don't think so."
                elif Girl == KittyX:
                    ch_k "No thanks."
                elif Girl == EmmaX:
                    ch_e "I'm afraid not."
                elif Girl == LauraX:
                    ch_l "Nah, not right now."
                elif Girl == JeanX:
                    ch_j "Ha! Keep trying, [Girl.player_petname]."
                elif Girl == StormX:
                    ch_s "I do not think so, right now."
                elif Girl == JubesX:
                    ch_v "Nah. . ."
                call Bottoms_Off_Refused (Girl)
                $ renpy.pop_call()
        "Don't care, lose'em.":
            if approval_check(Girl, 800, "OI", taboo_modifier=1):
                if Girl == RogueX:
                    ch_r "Fine, whatever."
                elif Girl == KittyX:
                    ch_k "Whatev."
                elif Girl == EmmaX:
                    ch_e "If you insist."
                elif Girl == LauraX:
                    ch_l "Fine."
                elif Girl == JeanX:
                    ch_j ". . ."
                elif Girl == StormX:
                    ch_s ". . ."
                elif Girl == JubesX:
                    ch_v "Fine. . ."
            else:
                call Bottoms_Off_Refused (Girl)
                $ renpy.pop_call()
        "Ok, you can leave it on.":

            $ renpy.pop_call()
    return

label Bottoms_Off_Refused(Girl=0):
    $ Girl = check_girl(Girl)
    call shift_focus (Girl)

    if Girl == RogueX:
        if "no_bottomless" in Girl.recent_history:
            ch_r "What part of \"no\" escapes you, [Girl.player_petname]?"
        elif "no_bottomless" in Girl.daily_history:
            ch_r "If you keep this up, not ever, [Girl.player_petname]."
        else:
            $ Girl.change_face("_sad")
            if counter == 2:
                ch_r "That's enough, [Girl.player_petname]. Sure we can't have some fun anyway?"
            else:
                ch_r "I'm afraid not this time, [Girl.player_petname]. Sure we can't have some fun anyway?"
    elif Girl == KittyX:
        if "no_bottomless" in Girl.recent_history:
            ch_k "You're[Girl.like]on my last nerve here."
        elif "no_bottomless" in Girl.daily_history:
            ch_k "Give it a rest."
        else:
            $ Girl.change_face("_sad")
            if counter == 2:
                ch_k "What you see is what you get, but[Girl.like]can't we still have some fun?"
            else:
                ch_k "The answer's \"no,\" but[Girl.like]can't we still have some fun?"
    elif Girl == EmmaX:
        if "no_bottomless" in Girl.recent_history:
            ch_e "Try to control your impulses."
        elif "no_bottomless" in Girl.daily_history:
            ch_e "Not today."
        else:
            $ Girl.change_face("_sad")
            if counter == 2:
                ch_e "That's all I'm willing to do, is that a deal-breaker?"
            else:
                ch_e "I'm afraid not, is that a deal-breaker?"
    elif Girl == LauraX:
        if "no_bottomless" in Girl.recent_history:
            ch_l "Reign it in."
        elif "no_bottomless" in Girl.daily_history:
            ch_l "No, not today."
        else:
            $ Girl.change_face("_sad")
            if counter == 2:
                ch_l "No more, is that going to be a problem?"
            else:
                ch_l "Nope, is that going to be a problem?"
    elif Girl == JeanX:
        if "no_bottomless" in Girl.recent_history:
            ch_j "Take a breath, [Girl.player_petname]."
        elif "no_bottomless" in Girl.daily_history:
            ch_j "I made myself clear."
        else:
            $ Girl.change_face("_sad")



            ch_j "Do we have a problem?"
    elif Girl == StormX:
        if "no_bottomless" in Girl.recent_history:
            ch_s "Show some restraint."
        else:
            $ Girl.change_face("_sad")
            if counter == 2:
                ch_s "This is all, can we continue without it?"
            else:
                ch_s "I would rather not, can we continue without it?"
    elif Girl == JubesX:
        if "no_bottomless" in Girl.daily_history:
            ch_v "Like I said, nope."
        else:
            $ Girl.change_face("_sad")
            ch_v "This is it, ok?"
    menu:
        extend ""
        "Sure, never mind." if "no_bottomless" not in Girl.recent_history:
            $ Girl.mouth = "_smile"
            $ Girl.change_stat("love", 70, 2)
            $ Girl.change_stat("obedience", 60, 2)
            if Girl == RogueX:
                ch_r "Great."
            elif Girl == KittyX:
                ch_k "Great!"
            elif Girl == EmmaX:
                ch_e "Excellent."
            elif Girl == LauraX:
                ch_l "Right."
            elif Girl == JeanX:
                ch_j "Good. . ."
            elif Girl == StormX:
                ch_s "Good. . ."
            elif Girl == JubesX:
                ch_v "Cool."

        "Sorry, I'll drop it." if "no_bottomless" in Girl.recent_history:
            if Girl == EmmaX:
                ch_e "Good."
            elif Girl == LauraX:
                ch_l "Cool."
            else:
                Girl.voice "Fine. . ."
        "No, let's do something else.":

            $ Girl.brows = "_confused"
            if Girl == RogueX:
                ch_r "Ok [Girl.player_petname], your loss."
            elif Girl == KittyX:
                ch_k "Ok[Girl.like]whatever."
            elif Girl == StormX:
                ch_s "So be it. . ."
            elif Girl == JubesX:
                ch_v "Whatever. . ."
            else:
                Girl.voice "Your loss."
            $ Girl.change_stat("lust", 50, 5)
            $ Girl.change_stat("love", 70, -2, 1)
            if "no_bottomless" not in Girl.recent_history:
                $ Girl.change_stat("obedience", 60, 4)
            $ Girl.recent_history.append("_angry")
            $ Girl.daily_history.append("_angry")

    $ Girl.recent_history.append("no_bottomless")
    $ Girl.daily_history.append("no_bottomless")
    $ approval_bonus = 0
    return
