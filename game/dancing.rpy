
# start Strip Tease / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#start Dancing/Stripping / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Group_Strip(Girl=0,temp_modifier = temp_modifier,temp_modifierP=[0,0],BO=[]): #rkeljsv
        #Note, this event would break during a date, since it manipulates Adjacent. Perhaps use unique list?
        $ Present = []
        $ BO = TotalGirls[:]
        while BO:
                if BO[0].Loc == bg_current:
                        $ Present.append(BO[0])
                $ BO.remove(BO[0])

        if not Present:
                "Nobody's here."
                "You dance alone."
                return

        while len(Present) > 2:
                #culls out extra members
                call Remove_Girl(Present[2])
    #            $ Present.remove(Present[2])

        if len(Present) == 2:
            $ renpy.random.shuffle(Present)
            if Girl and Present[0] != Girl:
                    $ Party.reverse()
            elif ApprovalCheck(Present[0],Check=1) <= ApprovalCheck(Present[1],Check=1):
                    # If second one likes you more, pick her
                    $ Present.reverse()

        call Shift_Focus(Present[0])

        $ Round -= 5 if Round > 5 else (Round-1)
        call Set_The_Scene(1,0,0,0)

        $ Present[0].FaceChange("sexy",1)
        if len(Present) >= 2:
                if Present[1] in TotalGirls:
                        $ Present[1].FaceChange("sexy",1)
                else:
                        $ Present.remove(Present[1])

        $ Cnt = len(Present) #max 2
        while Cnt:
            $ Cnt -= 1 #max 1
            if Girl == EmmaX and "classcaught" in EmmaX.RecentActions and AloneCheck(EmmaX):
                        #skip this step if during classcaught sequence
                        pass
            elif not ApprovalCheck(Present[Cnt], 600, TabM = 1,Alt=[[EmmaX],(650+Taboo*10)]) or (Present[Cnt] == EmmaX and Taboo and "taboo" not in EmmaX.History):
                    if not ApprovalCheck(Present[Cnt], 400):
                        if Present[Cnt] == RogueX:
                                ch_r "I'm just some sort'a gogo dancer now?"
                        elif Present[Cnt] == KittyX:
                                ch_k "Like I would just dance for you?"
                        elif Present[Cnt] == EmmaX:
                                ch_e "Oh, you think I'll dance to your tune?"
                        elif Present[Cnt] == LauraX:
                                ch_l "I don't dance."
                        elif Present[Cnt] == JeanX:
                                ch_j "I'm not in the mood."
                        elif Present[Cnt] == StormX:
                                ch_s "I do not dance."
                        elif Present[Cnt] == JubesX:
                                ch_v "I don't wanna dance, weirdo. . ."
                    elif Present[Cnt].Taboo:
                        if Present[Cnt] == RogueX:
                                ch_r "I don't think this is the best place for dance'n."
                        elif Present[Cnt] == KittyX:
                                ch_k "I don't know, this really isn't a good place for it?"
                        elif Present[Cnt] == EmmaX:
                                ch_e "You must be joking. Here?"
                        elif Present[Cnt] == LauraX:
                                if ApprovalCheck(LauraX, 600, TabM = 0):    #should add a second Laura, then the first gets removed.
                                        $ Present.append(LauraX)            #This restores the "taboo is irrelevant to her" state
                                else:
                                        ch_l "I don't feel like it."
                        elif Present[Cnt] == JeanX:
                                ch_j "I don't want to just randomly dance in public."
                        elif Present[Cnt] == StormX:
                                ch_s "I would not want to make a scene."
                        elif Present[Cnt] == JubesX:
                                ch_v "This isn't really the place for it. . ."
                    else:
                        if Present[Cnt] == RogueX:
                                ch_r "I dont feel it right now."
                        elif Present[Cnt] == KittyX:
                                ch_k "I don't know, I don't really feel like dancing right now."
                        elif Present[Cnt] == EmmaX:
                                ch_e "I don't really feel like dancing at the moment."
                        elif Present[Cnt] == LauraX:
                                ch_l "I don't feel like it."
                        elif Present[Cnt] == JeanX:
                                ch_j "I'm not in the mood."
                        elif Present[Cnt] == StormX:
                                ch_s "I do not wish to dance right now."
                        elif Present[Cnt] == JubesX:
                                ch_v "Yeah, I don't feel like dancing right now. . ."
                    $ Present.remove(Present[Cnt])

        if not Present:
                return

        if EmmaX.Loc == bg_current and EmmaX not in Present:
                #If Emma is here, but does not agree to this,
                if "classcaught" not in EmmaX.History:
                        if EmmaX.Loc == EmmaX.Home:
                                #if it's her room. . .
                                ch_e "If the two of you would like to dance, please do it elsewhere."
                                $ Present = []
                                return
                        else:
                                ch_e "I should really be going."
                                call Remove_Girl(EmmaX)

        if "stripping" in Present[0].DailyActions and ApprovalCheck(Present[0], 500, TabM = 3):
                $ Line = renpy.random.choice(["You liked the show earlier?",
                    "Didn't get enough earlier?",
                    "You're going to wear me out."])
        else:
                $ Line = renpy.random.choice(["Ok, that sounds fun.",
                    "I could get into that.",
                    "Yeah, ok."])

        call AnyLine(Present[0],Line)
        $ Line = 0

        call AllReset("All")


        $ Cnt = len(Present) #max 2
        while Cnt:
                $ Cnt -= 1 #max 1
                if Present[Cnt] == RogueX:
                            show Rogue_Sprite at Girl_Dance1(RogueX)
                elif Present[Cnt] == KittyX:
                            show Kitty_Sprite at Girl_Dance1(KittyX)
                elif Present[Cnt] == EmmaX:
                            show Emma_Sprite at Girl_Dance1(EmmaX)
                elif Present[Cnt] == LauraX:
                            show Laura_Sprite at Girl_Dance1(LauraX)
                elif Present[Cnt] == JeanX:
                            show Jean_Sprite at Girl_Dance1(JeanX)
                elif Present[Cnt] == StormX:
                            show Storm_Sprite at Girl_Dance1(StormX)
                elif Present[Cnt] == JubesX:
                            show Jubes_Sprite at Girl_Dance1(JubesX)
                $ Present[Cnt].RecentActions.append("stripping")
                $ Present[Cnt].DailyActions.append("stripping")
                $ Present[Cnt].Strip += 1
                $ Present[Cnt].Action -= 1
                $ temp_modifierP[Cnt] = temp_modifier
                if Present[Cnt].SeenChest or Present[Cnt].SeenPussy:
                        #You've seen her tits.
                        $ temp_modifierP[Cnt] += 20
                if Present[Cnt].SeenPanties:
                        #You've seen her panties.
                        $ temp_modifierP[Cnt] += 5
                if "exhibitionist" in Present[Cnt].Traits:
                        $ temp_modifierP[Cnt] += (4*Taboo)
                if ("sex friend" in Present[Cnt].Petnames or Present[Cnt] in Player.Harem) and not Taboo:
                        $ temp_modifierP[Cnt] += 15
                elif "ex" in Present[Cnt].Traits:
                        $ temp_modifierP[Cnt] -= 40
                elif Present[Cnt].ForcedCount and not Present[Cnt].Forced:
                        $ temp_modifierP[Cnt] -= 5 * Present[Cnt].ForcedCount

        if len(Present) >= 2:
                "They start to dance."
                $ Partner = Present[1]
                $ Count2 = 1
        else:
                "She starts to dance."
                $ Count2 = 0
                $ Partner = 0


        if Girl == EmmaX and "classcaught" in EmmaX.RecentActions and AloneCheck(EmmaX):
                #skip this step if during classcaught sequence
                $ Count = 0
                jump Group_Stripping

        #this portion adds back in girls who dropped out, but sets their "stop" flag.
        $ BO = TotalGirls[:]
        while BO:
                if BO[0].Loc == bg_current and BO[0] not in Present:
                        $ Present.append(BO[0])
                        if "stopdancing" not in BO[0].RecentActions:
                                $ BO[0].RecentActions.append("stopdancing")
                $ BO.remove(BO[0])

        $ temp_modifier = temp_modifierP[0]
        $ Trigger = "strip"
        $ Count = 1

        while Count and Round >=10:
                #Loops endlessly until you do something.
                $ Round -= 2 if Round > 2 else Round
                if len(Present) >= 2:
                    $ Present[0].GLG(Present[1],600,1,1)
                    $ Present[1].GLG(Present[0],600,1,1)
                menu:
                    "Continue":
                            pass
                    "Would you kindly take off some clothes?":
                            #add checks here
                            call AnyLine(Present[0],"Hmm?")
                            $ Count = 0
                    "Stop":
                            jump Group_Strip_End


        if EmmaX.Loc == bg_current and len(Present) >= 2:
                #If Emma is here, but does not agree to this,
                if "classcaught" not in EmmaX.History or "three" not in EmmaX.History or (Taboo and "taboo" not in EmmaX.History):
                    if EmmaX.Loc == "bg emma":
                            #if it's her room. . .
                            ch_e "If the two of you would like to get indecent, please do it elsewhere."
                            $ Present = []
                            return
                    else:
                            ch_e "I should really be going."
                            call Remove_Girl(EmmaX)

label Group_Stripping:
        while Round >= 10 and Present:
            $ Round -= 2 if Round > 2 else Round

            if Present[Count] != Ch_Focus:
                    call Shift_Focus(Present[Count])

            call Girl_Stripping(Present[Count])

            if len(Present) < 2 and Count != 0:
                    $ Count = 0
            if not Present or not Present[Count]: #threw "list index" errors?
                    jump Group_Strip_End
            if "stopdancing" in Present[Count].RecentActions:
                    #if she's just standing around, cut back to the other girl
                    if len(Present) >= 2 and "stopdancing" in Present[0].RecentActions and "stopdancing" in Present[1].RecentActions:
                            jump Group_Strip_End

            $ Trigger = "strip"

            if not Present:
                    #If everyone leaves, quit out
                    jump Group_Strip_End

            if len(Present) >= 2 and Count != Count2:
                $ Present[Count].GLG(Present[Count2],800,2,1)
                $ Present[Count2].GLG(Present[Count],800,2,1)

            if len(Present) >= 2:
                    # Flips the numbers if in a group
                    # Count starts at 0
                    if Count == 0 and "stopdancing" not in Present[1].RecentActions:
                            $ Count = 1
                            $ Count2 = 0
                            $ temp_modifierP[1] = temp_modifier
                            $ temp_modifier = temp_modifierP[0]
                    elif Count == 1 and "stopdancing" not in Present[0].RecentActions:
                            $ Count = 0
                            $ Count2 = 1
                            $ temp_modifierP[0] = temp_modifier
                            $ temp_modifier = temp_modifierP[1]
                    call Shift_Focus(Present[Count])
    #                $ Partner = Present[Count2]

                    call Activity_Check(Ch_Focus,Partner)

            if len(Present) < 2 or "stopdancing" in Present[1].RecentActions:
                    #Plays if only one girl is dancing
                    $ temp_modifier = temp_modifierP[Count]
                    $ Count = 0
                    $ Count2 = 0
                    $ Partner = 0

                    call Activity_Check(Ch_Focus,Partner)

                    if not Present or "stopdancing" in Present[0].RecentActions:
                            jump Group_Strip_End
            #ends loop
        if Present and Round <=15:
                call AnyLine(Present[0],"It's getting late, we should probably take a break.")

label Group_Strip_End:
        #add like-ups here. . .
        if Present:
                $ Present[0].DrainWord("stopdancing",1,0,0)
                $ Present[0].DrainWord("keepdancing",1,0,0)
        if len(Present) >= 2:
                $ Present[1].DrainWord("stopdancing",1,0,0)
                $ Present[1].DrainWord("keepdancing",1,0,0)

        call Set_The_Scene(1,0,0,0)
        $ Count = 0
        $ Count2 = 0
    #    $ renpy.pop_call()
        return

#end Dancing/Stripping / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Girl_Stripping(Girl=0,Nudist=0): #rkeljsv
        #This gets called by Group_Stripping, and returns there at the end.
        if "stopdancing" in Girl.RecentActions:
                #if she's just standing around, cut back to the other girl
                return

        $ Girl.ArmPose = 2
        $ Girl.LustFace(1) #sets her lusty face

        if Girl == StormX and (StormX in Rules or Girl.Taboo <= 20):
                #if it's Storm and either you're in private or have broken Xavier, she doesn't fight you
                if Girl.Forced:
                        $ Nudist = -40
                else:
                        $ Nudist = Girl.Taboo
        if "keepdancing" not in Girl.RecentActions:
                # if Count isn't 2, it loops.
                if Girl == JubesX and Girl.Acc and (Girl.Over or Girl.Chest) and (Girl.Panties or Girl.Legs or Girl.HoseNum() >= 10):
                    #will she lose the jacket when she's dressed under?
                    if ApprovalCheck(Girl, 750, TabM = 3):
                            $ Girl.Statup("Obed", 50, 1)
                            $ Girl.Statup("Inbt", 25, 1)
                            $ Player.Statup("Focus", 60, 3)
                            $ Line = Girl.Acc
                            $ Girl.Acc = 0
                            "She shrugs off her [Line] and throws it behind her."
                    else:
                            jump Strip_Ultimatum
                elif Girl == JubesX and Girl.Acc and Girl.Over and (Girl.Panties or Girl.Legs or Girl.HoseNum() >= 10):
                    #will she lose the jacket when she's dressed under?
                    if ApprovalCheck(Girl, 750, TabM = 3):
                            $ Girl.Statup("Obed", 50, 1)
                            $ Girl.Statup("Inbt", 25, 1)
                            $ Player.Statup("Focus", 60, 3)
                            $ Line = Girl.Acc
                            $ Girl.Acc = 0
                            "She shrugs off her [Line] and throws it behind her."
                    else:
                            jump Strip_Ultimatum
                elif Girl.Over and Girl.Chest and (Girl.Panties or Girl.Legs or Girl.HoseNum() >= 10):
                    #will she lose the overshirt when she's dressed under?
                    if ApprovalCheck(Girl, 750, TabM = 3,Alt=[[StormX],(300-Nudist*3)]):
                            $ Girl.Statup("Obed", 50, 1)
                            $ Girl.Statup("Inbt", 25, 1)
                            $ Player.Statup("Focus", 60, 3)
                            $ Line = Girl.Over
                            $ Girl.Over = 0
                            if Girl == KittyX:
                                    "She drops her shoulders and her [Line] falls to the floor."
                            else:
                                    "She pulls her [Line] over her head and throws it behind her."
                    else:
                            jump Strip_Ultimatum

                elif Girl.Legs and (Girl.Panties or Girl.HoseNum() >= 10):
                    #will she lose the pants/skirt if she has panties on?
                    if ApprovalCheck(Girl, 1200, TabM = 3,Alt=[[StormX],(600-Nudist*3)]) or (Girl.SeenPanties and ApprovalCheck(Girl, 900, TabM = 3) and not Girl.Taboo):
                            $ Girl.Statup("Lust", 50, 5)
                            $ Girl.Statup("Obed", 50, 1)
                            $ Girl.Statup("Inbt", 30, 1)
                            $ Player.Statup("Focus", 60, 5)
                            $ Line = Girl.Legs
                            $ Girl.Legs = 0
                            if Girl == KittyX:
                                    "Her [Line] slide through her legs until they're only on her toes, before she kicks them to the floor."
                            else:
                                    "She unzips and pulls down her [Line], dropping them to the floor."
                            if not Girl.SeenPanties:
                                    $ Girl.Statup("Obed", 50, 2)
                                    $ Girl.Statup("Obed", 200, 3)
                                    $ Girl.Statup("Inbt", 50, 3)
                                    $ Girl.Statup("Inbt", 200, 2)
                                    $ Girl.SeenPanties = 1
                    else:
                            jump Strip_Ultimatum

                elif Girl.Hose:
                    # Will she lose the hose?
                    if Girl.HoseNum() >= 10:
                            if ApprovalCheck(Girl, 1200, TabM = 3):
                                    $ Girl.Statup("Lust", 50, 6)
                                    $ Player.Statup("Focus", 60, 6)
                            else:
                                    jump Strip_Ultimatum

                    elif Girl.HoseNum() >= 6 and ApprovalCheck(Girl, 1200, TabM = 3):
                            if ApprovalCheck(Girl, 1200, TabM = 3,Alt=[[StormX],(600-Nudist*3)]):
                                $ Girl.Statup("Lust", 50, 4)
                                $ Player.Statup("Focus", 60, 4)
                            else:
                                jump Strip_Ultimatum
                    else:
                            $ Player.Statup("Focus", 60, 3)
                    $ Line = Girl.Hose
                    $ Girl.Hose = 0
                    if Girl == KittyX:
                            "Her [Line] slide down off her legs, leaving them in a small pile."
                    else:
                            "She rolls the [Line] down off her legs, leaving them in a small pile."
                    call expression Girl.Tag + "_First_Bottomless" pass (1)

                elif Girl == JubesX and Girl.Acc and (Girl.Panties or Girl.Legs or Girl.HoseNum() >= 10):
                    #will she lose the jacket when she's topless under?
                    if ApprovalCheck(Girl, 1250, TabM = 3) or (Girl.SeenChest and ApprovalCheck(Girl, 1000, TabM = 3) and not Girl.Taboo):
                            $ Girl.Statup("Lust", 60, 5)
                            $ Girl.Statup("Obed", 50, 2)
                            $ Girl.Statup("Inbt", 50, 10)
                            $ Player.Statup("Focus", 80, 15)
                            $ Line = Girl.Acc
                            $ Girl.Acc = 0
                            "She shrugs off her [Line] and throws it behind her."
                            if not Girl.SeenChest:
                                    $ Girl.FaceChange("bemused", 1)
                                    $ Girl.Statup("Obed", 50, 3)
                                    $ Girl.Statup("Obed", 200, 4)
                                    $ Girl.Statup("Inbt", 50, 3)
                                    $ Girl.Statup("Inbt", 200, 3)
                                    "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                                    call first_topless(Girl, silent = True)
                    else:
                            jump Strip_Ultimatum
                elif Girl.Over and not Girl.Chest and (Girl.Panties or Girl.HoseNum() >= 10):
                    #will she lose the top when she's topless with panties?
                    if ApprovalCheck(Girl, 1250, TabM = 3,Alt=[[StormX],(650-Nudist*3)]) or (Girl.SeenChest and ApprovalCheck(Girl, 1000, TabM = 3) and not Girl.Taboo):
                            $ Girl.Statup("Lust", 60, 5)
                            $ Girl.Statup("Obed", 50, 2)
                            $ Girl.Statup("Inbt", 50, 10)
                            $ Player.Statup("Focus", 80, 15)
                            $ Line = Girl.Over
                            $ Girl.Over = 0
                            if not Girl.SeenChest:
                                    $ Girl.FaceChange("bemused", 1)
                                    $ Girl.Statup("Obed", 50, 3)
                                    $ Girl.Statup("Obed", 200, 4)
                                    $ Girl.Statup("Inbt", 50, 3)
                                    $ Girl.Statup("Inbt", 200, 3)
                                    if Girl == KittyX:
                                            "She hesitantly glances your way, and then with tug her [Line] passes through her, tossing it to the ground."
                                    elif Girl in (EmmaX,LauraX,StormX):
                                            "She glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                                    else:
                                            "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                                    call first_topless(Girl, silent = True)
                            else:
                                if Girl == KittyX:
                                        "She drops her shoulders and her [Line] falls to the floor."
                                else:
                                        "She pulls her [Line] over her head, tossing it to the ground."
                    else:
                            jump Strip_Ultimatum

                elif Girl.Chest and not Girl.Over:
                    # Will she lose the bra?
                    if ApprovalCheck(Girl, 1250, TabM = 3,Alt=[[StormX],(650-Nudist*3)]) or (Girl.SeenChest and ApprovalCheck(Girl, 1000, TabM = 3) and not Girl.Taboo):
                            $ Girl.Statup("Lust", 60, 5)
                            $ Girl.Statup("Obed", 50, 2)
                            $ Girl.Statup("Inbt", 50, 1)
                            $ Player.Statup("Focus", 80, 15)
                            $ Line = Girl.Chest
                            $ Girl.Chest = 0
                            if not Girl.SeenChest:
                                    $ Girl.FaceChange("bemused", 1)
                                    if Girl == KittyX:
                                            "She hesitantly glances your way, and then with a shrug pulls her [Line] through herself, tossing it to the ground."
                                    elif Girl in (EmmaX,LauraX,StormX):
                                            "She glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                                    else:
                                            "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                                    $ Girl.Statup("Obed", 50, 3)
                                    $ Girl.Statup("Obed", 200, 4)
                                    $ Girl.Statup("Inbt", 50, 3)
                                    $ Girl.Statup("Inbt", 200, 3)
                                    call first_topless(Girl, silent = True)
                            else:
                                    $ Girl.FaceChange("sexy")
                                    if Girl == KittyX:
                                            "She pulls her [Line] through herself, tossing it to the ground."
                                    else:
                                            "She pulls her [Line] over her head, tossing it to the ground."
                    else:
                            jump Strip_Ultimatum

                elif Girl.Legs:
                    #will she lose the pants/skirt if she has no panties on?
                    if ApprovalCheck(Girl, 1350, TabM = 3,Alt=[[StormX],(800-Nudist*3)]) or (Girl.SeenPussy and ApprovalCheck(Girl, 1100, TabM = 3) and not Girl.Taboo):
                            $ Girl.Statup("Lust", 75, 10)
                            $ Line = Girl.Legs
                            $ Girl.Legs = 0
                            if not Girl.SeenPussy:
                                    $ Girl.Statup("Obed", 60, 3)
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Inbt", 50, 4)
                                    $ Girl.Statup("Inbt", 200, 4)
                                    if Girl == KittyX:
                                            "She shyly looks up at you, and then slowly lets her [Line] slide to the floor."
                                    elif Girl in (EmmaX,LauraX,JeanX):
                                            "She hesitantly looks up at you, and then slowly unzips and pulls down her [Line], dropping them to the floor."
                                    else:
                                            "She shyly looks up at you, and then slowly unzips and pulls down her [Line], dropping them to the floor."
                                    call expression Girl.Tag + "_First_Bottomless" pass (1)
                            else:
                                    $ Girl.Statup("Obed", 50, 1)
                                    $ Girl.Statup("Obed", 75, 1)
                                    if Girl == KittyX:
                                            "She lets her [Line] pass through her legs, dropping them to the floor."
                                    else:
                                            "She unzips and pulls down her [Line], dropping them to the floor."
                                    $ Girl.Statup("Inbt", 70, 2)
                            $ Player.Statup("Focus", 85, 15)
                    else:
                            jump Strip_Ultimatum

                elif Girl == JubesX and Girl.Acc:
                    #will she lose the jacket when she's naked under?
                    if ApprovalCheck(Girl, 1350, TabM = 3) or (Girl.SeenPussy and ApprovalCheck(Girl, 1100, TabM = 3) and not Girl.Taboo):
                            $ Line = Girl.Acc
                            $ Girl.Acc = 0
                            if not Girl.SeenPussy:
                                    $ Girl.Statup("Obed", 60, 3)
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Inbt", 50, 4)
                                    $ Girl.Statup("Inbt", 200, 4)
                                    "She hesitantly glances your way, and then with a shrug pulls her [Line] off, tossing it to the ground."
                                    call expression Girl.Tag + "_First_Bottomless" pass (1)
                            else:
                                    "She shrugs her [Line] off, tossing it to the ground."

                            if not Girl.Chest or Girl.Uptop:
                                if not Girl.SeenChest:
                                        $ Girl.Statup("Obed", 50, 3)
                                        $ Girl.Statup("Inbt", 50, 3)
                                        call first_topless(Girl, silent = True)
                                else:
                                        $ Girl.Statup("Lust", 60, 15)
                                        $ Girl.Statup("Obed", 50, 3)
                                        $ Girl.Statup("Obed", 75, 1)
                                        $ Girl.Statup("Inbt", 50, 3)
                            else:
                                    $ Girl.Statup("Lust", 75, 10)
                                    $ Girl.Statup("Obed", 50, 1)
                                    $ Girl.Statup("Obed", 75, 1)
                                    $ Girl.Statup("Inbt", 70, 2)
                            $ Player.Statup("Focus", 85, 15)
                    else:
                            jump Strip_Ultimatum
                elif Girl.Over and not Girl.Panties:
                    #will she lose the overshirt when she's bottomless under?
                    if ApprovalCheck(Girl, 1350, TabM = 3,Alt=[[StormX],(800-Nudist*3)]) or (Girl.SeenPussy and ApprovalCheck(Girl, 1100, TabM = 3) and not Girl.Taboo):
                            $ Line = Girl.Over
                            $ Girl.Over = 0
                            if not Girl.SeenPussy:
                                    $ Girl.Statup("Obed", 60, 3)
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Inbt", 50, 4)
                                    $ Girl.Statup("Inbt", 200, 4)
                                    if Girl == KittyX:
                                            "She hesitantly glances your way, and then with a tug pulls her [Line] through herself, tossing it to the ground."
                                    elif Girl in (EmmaX,LauraX,StormX):
                                            "She glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                                    else:
                                            "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                                    call expression Girl.Tag + "_First_Bottomless" pass (1)
                            else:
                                if Girl == KittyX:
                                        "She drops her shoulders and her [Line] falls to the floor."
                                else:
                                        "She pulls her [Line] over her head, tossing it to the ground."

                            if not Girl.Chest or Girl.Uptop:
                                if not Girl.SeenChest:
                                        $ Girl.Statup("Obed", 50, 3)
                                        $ Girl.Statup("Inbt", 50, 3)
                                        call first_topless(Girl, silent = True)
                                else:
                                        $ Girl.Statup("Lust", 60, 15)
                                        $ Girl.Statup("Obed", 50, 3)
                                        $ Girl.Statup("Obed", 75, 1)
                                        $ Girl.Statup("Inbt", 50, 3)
                            else:
                                    $ Girl.Statup("Lust", 75, 10)
                                    $ Girl.Statup("Obed", 50, 1)
                                    $ Girl.Statup("Obed", 75, 1)
                                    $ Girl.Statup("Inbt", 70, 2)
                            $ Player.Statup("Focus", 85, 15)
                    else:
                            jump Strip_Ultimatum

                elif Girl.Chest:
                    # Will she go topless?
                    if ApprovalCheck(Girl, 1250, TabM = 3,Alt=[[StormX],(750-Nudist*3)]) or (Girl.SeenChest and ApprovalCheck(Girl, 1100, TabM = 3) and not Girl.Taboo):
                            $ Girl.Statup("Lust", 60, 5)
                            $ Line = Girl.Chest
                            $ Girl.Chest = 0
                            if not Girl.SeenChest:
                                    $ Girl.Statup("Obed", 50, 3)
                                    $ Girl.Statup("Obed", 200, 4)
                                    $ Girl.Statup("Inbt", 50, 3)
                                    $ Girl.Statup("Inbt", 200, 3)
                                    if Girl == KittyX:
                                            "She hesitantly glances your way, and then with a tug pulls her [Line] through herself, tossing it to the ground."
                                    elif Girl in (EmmaX,LauraX,StormX):
                                            "She glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                                    else:
                                            "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                                    call first_topless(Girl, silent = True)
                            else:
                                    $ Girl.Statup("Obed", 50, 2)
                                    if Girl == KittyX:
                                            "She drops her shoulders and her [Line] falls to the floor."
                                    else:
                                            "She pulls her [Line] over her head, tossing it to the ground."
                                    $ Girl.Statup("Inbt", 50, 1)
                            $ Player.Statup("Focus", 80, 15)
                    else:
                            jump Strip_Ultimatum

                elif Girl.Panties:
                    # Will she go bottomless?
                    if ApprovalCheck(Girl, 1350, TabM = 3,Alt=[[StormX],(800-Nudist*3)]) or (Girl.SeenPussy and ApprovalCheck(Girl, 1100, TabM = 3) and not Girl.Taboo):
                            $ Girl.Statup("Lust", 75, 10)
                            $ Line = Girl.Panties
                            $ Girl.Panties = 0
                            if not Girl.SeenPussy:
                                    $ Girl.Statup("Obed", 60, 3)
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Inbt", 50, 4)
                                    $ Girl.Statup("Inbt", 200, 4)
                                    if Girl == KittyX:
                                            "She shyly looks up at you, and then slowly tugs her [Line] off, flinging them to the side."
                                    elif Girl in (EmmaX,LauraX):
                                            "She looks up at you, and then slowly pulls her [Line] down, kicking them off to the side."
                                    else:
                                            "She shyly looks up at you, and then slowly pulls her [Line] down, kicking them off to the side."
                                    call expression Girl.Tag + "_First_Bottomless" pass (1)
                            else:
                                    $ Girl.Statup("Obed", 50, 1)
                                    $ Girl.Statup("Obed", 75, 1)
                                    if Girl == KittyX:
                                            "She  looks up at you, and then gently pulls her [Line] off, flicking them to the side."
                                    else:
                                            "She  looks up at you, and then gently pulls her [Line] down, kicking them off to the side."
                                    $ Girl.Statup("Inbt", 70, 2)
                            $ Player.Statup("Focus", 85, 15)
                    else:
                            jump Strip_Ultimatum

                else:
                    $ Girl.FaceChange("sexy")
                    if Girl == RogueX:
                            ch_r "I'm afraid that's all I have on, [Girl.Petname]. . ."
                    elif Girl == KittyX:
                            ch_k "It looks like I've run out of clothes. . ."
                    elif Girl == EmmaX:
                            ch_e "Well, it appears I've run out of clothes, [Girl.Petname]. . ."
                    elif Girl == LauraX:
                            ch_l "Well, that's all I've got, [Girl.Petname]. . ."
                    elif Girl == JeanX:
                            ch_j "I'm all out of clothes. . ."
                    elif Girl == StormX:
                            ch_s "I appear to have lost my clothing. . ."
                    elif Girl == JubesX:
                            ch_v "Well, it looks like I'm done here. . ."
                    menu:
                            extend ""
                            "Ok, you can stop":
                                    $ Girl.RecentActions.append("stopdancing")
                                    call reset_position(Girl)

                                    return
                            "Keep on dancing":
                                    $ Girl.RecentActions.append("keepdancing")
        # end "nude" not in Girl.RecentActions loop

        $ Girl.Statup("Lust", 70, 2)               #lust/Focus
        if "exhibitionist" in Girl.Traits:
                $ Girl.Statup("Lust", 200, 2)
        $ Player.Statup("Focus", 60, 3)
        if Trigger2 == "jackin":
                $ Girl.Statup("Lust", 200, 2)
                $ Player.Statup("Focus", 200, 5)

        if not Player.Semen and Player.Focus >= 50:
                $ Player.Focus = 50

        if Player.Focus >= 100 or Girl.Lust >= 100:
                #If either of you could cum

                if Player.Focus >= 100:
                    #You cum
                    call Player_Cumming(Girl)
                    if "angry" in Girl.RecentActions:
                            return
                    $ Girl.Statup("Lust", 200, 5)
                    if not Player.Semen and Trigger2 == "jackin":
                            "You're spitting dust here, maybe just watch quietly for a while."
                            $ Trigger2 = 0
                    if Player.Focus > 80:
                            jump Group_Strip_End

                if Girl.Lust >= 100:
                    #and girl cums
                    call Girl_Cumming(Girl)
                    if Situation == "shift" or "angry" in Girl.RecentActions:
                            $ Count = 0
                            jump Group_Strip_End

                call AllReset(Girl)

                if Girl == RogueX:
                            show Rogue_Sprite at Girl_Dance1(Girl)
                elif Girl == KittyX:
                            show Kitty_Sprite at Girl_Dance1(Girl)
                elif Girl == EmmaX:
                            show Emma_Sprite at Girl_Dance1(Girl)
                elif Girl == LauraX:
                            show Laura_Sprite at Girl_Dance1(Girl)
                elif Girl == JeanX:
                            show Jean_Sprite at Girl_Dance1(Girl)
                elif Girl == StormX:
                            show Storm_Sprite at Girl_Dance1(Girl)
                elif Girl == JubesX:
                            show Jubes_Sprite at Girl_Dance1(Girl)

                "[Girl.Name] begins to dance again."

        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)

        menu:
            "[Girl.Name] should. . ."
            "Keep Going. . ." if "keepdancing" not in Girl.RecentActions:
                    $ Girl.Eyes = "sexy"
                    if Girl.Love >= 700 or Girl.Obed >= 500:
                        if not temp_modifier:
                            $ temp_modifier = 10
                        elif temp_modifier <= 20:
                            $ temp_modifier += 1
                    if Taboo and Girl.Strip <= 10:
                        $ Girl.Statup("Obed", 50, 7)
                    elif Taboo or Girl.Strip <= 10:
                        $ Girl.Statup("Obed", 50, 5)
                    elif Girl.Strip <= 50:
                        $ Girl.Statup("Obed", 50, 3)
            "Keep Dancing. . ." if "keepdancing" in Girl.RecentActions:
                    $ Girl.Eyes = "sexy"

            "Stop stripping, keep dancing" if "keepdancing" not in Girl.RecentActions:
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
                    $ Girl.RecentActions.append("keepdancing")

            "Start stripping again" if "keepdancing" in Girl.RecentActions:
                    $ Girl.RecentActions.remove("keepdancing")
                    if "stripforced" in Girl.RecentActions:
                            call AnyLine(Girl,". . .")
                    else:
                            if Girl == RogueX:
                                    ch_r "Hmm. . ."
                            elif Girl == KittyX:
                                    ch_k "Huh?"
                            else:
                                    call AnyLine(Girl,"Hmm. . .")

            "Just watch silently":
                if "watching" not in Girl.RecentActions:
                    if "keepdancing" not in Girl.RecentActions:
                        if Taboo and Girl.Strip <= 10:
                            $ Girl.Statup("Inbt", 50, 3)
                        elif Taboo or Girl.Strip <= 10:
                            $ Girl.Statup("Inbt", 50, 1)
                    elif Girl.Strip <= 50:
                            $ Girl.Statup("Inbt", 50, 2)
                            $ Girl.Statup("Lust", 70, 2)
                    $ Girl.RecentActions.append("watching")

            "Start jack'in it." if Trigger2 != "jackin":
                    call Jackin(Girl)
            "Stop jack'in it." if Trigger2 == "jackin":
                    $ Trigger2 = 0

            "Lose the [Girl.Arms]. . ." if Girl.Arms:
                    $ Girl.FaceChange("surprised")
                    $ Girl.Mouth = "kiss"
                    call AnyLine(Girl,"All right, "+Girl.Petname+".")
                    $ Girl.FaceChange("sexy")
                    $ Girl.Arms = 0

            "Ok, that's enough.":
                    if Girl == RogueX:
                            ch_r "Ok, [Girl.Petname]. . . "
                    elif Girl == KittyX:
                            ch_k "Ok. . ."
                    else:
                            call AnyLine(Girl,"Alright, "+Girl.Petname+".")
                    $ renpy.pop_call()
                    jump Group_Strip_End

        return


label Strip_Ultimatum: #rkeljsv
        if "keepdancing" in Girl.RecentActions:
            return

        call reset_position(Girl)

        $ Girl.FaceChange("bemused", 1)
        if "stripforced" in Girl.RecentActions:
                    $ Girl.FaceChange("sad", 1)
                    if Girl == RogueX:
                            ch_r "That's as far as I care to go, [Girl.Petname]."
                    elif Girl == KittyX:
                            ch_k "That's all you get."
                    elif Girl == EmmaX:
                            ch_e "I think that's plenty, [Girl.Petname]."
                    elif Girl == LauraX:
                            ch_l "Last call, [Girl.Petname]."
                    elif Girl == JeanX:
                            ch_j "Ok, that's my limit."
                    elif Girl == StormX:
                            ch_s "I will go no further. . ."
                    elif Girl == JubesX:
                            ch_v "Ok, that's all you get. . ."
        else:
                    if Girl == RogueX:
                            ch_r "I'm sorry, [Girl.Petname], I'm not ready to show you more. . . Yet."
                    elif Girl == KittyX:
                            ch_k "I don't know, [Girl.Petname], that's as far as I'll go for now."
                    elif Girl == EmmaX:
                            ch_e "I'm afraid that's as far as I'm ready to go, [Girl.Petname]. . . for now."
                    elif Girl == LauraX:
                            ch_l "Ok, that's enough, [Girl.Petname]. . . for now."
                    elif Girl == JeanX:
                            ch_j "Ok, I think you've seen enough. . ."
                    elif Girl == StormX:
                            ch_s "That's enough for now. . ."
                    elif Girl == JubesX:
                            ch_v "I'm kinda done here. . ."
        menu:
            extend ""
            "That's ok, you can stop.":
                    if "ultimatum" not in Girl.DailyActions:
                            $ Girl.Statup("Love", 50, 2)
                            $ Girl.Statup("Love", 90, 2)
                            $ Girl.Statup("Inbt", 50, 2)
                            $ Girl.DailyActions.append("ultimatum")
                    $ Girl.RecentActions.append("stopdancing")
                    return
            "That's ok, but keep dancing for a bit. . .":
                    if "ultimatum" not in Girl.DailyActions:
                            $ Girl.Statup("Love", 50, 2)
                            $ Girl.Statup("Obed", 50, 2)
                            $ Girl.Statup("Inbt", 50, 2)
                            $ Girl.DailyActions.append("ultimatum")
                    $ Girl.RecentActions.append("keepdancing")
                    if "stripforced" in Girl.RecentActions:
                            call AnyLine(Girl,". . .")
                    else:
                            if Girl == RogueX:
                                    ch_r "Heh, ok [Girl.Petname]."
                            elif Girl == KittyX:
                                    ch_k "Heh, alright."
                            elif Girl == EmmaX:
                                    ch_e "Oh, if I must, [Girl.Petname]."
                            elif Girl == LauraX:
                                    ch_l "Eh? Fine."
                            elif Girl == JeanX:
                                    ch_j "Ok, sure."
                            elif Girl == StormX:
                                    ch_s "Very well. . ."
                            elif Girl == JubesX:
                                    ch_v "Ok, sure. . ."
            "You'd better." if Girl.Forced:
                    if not ApprovalCheck(Girl, 500, "O", TabM=5) and not ApprovalCheck(Girl, 800, "L", TabM=5):
                            $ Girl.FaceChange("angry")
                            if Girl == RogueX:
                                    ch_r "I don't know who you think I am, but I ain't gonna just jump when you say \"toad\"."
                                    ch_r "I think we're done here for now."
                            elif Girl == KittyX:
                                    ch_k "I'm not just going to do \"whatever\"!"
                                    ch_k "I'm done with this."
                            elif Girl == EmmaX:
                                    ch_e "I think you're overstepping your bounds here, [Girl.Petname]."
                                    ch_e "Remember your place."
                            elif Girl == LauraX:
                                    ch_l "I don't like that tone, [Girl.Petname]."
                            elif Girl == JeanX:
                                    ch_j "Don't talk to me like that. -I- talk to -you- like that."
                            elif Girl == StormX:
                                    ch_s "I do not appreciate that tone."
                            elif Girl == JubesX:
                                    ch_v "I'd better not break your face either. . ."
                            $ Girl.RecentActions.append("angry")
                            $ Girl.DailyActions.append("angry")
                            call Remove_Girl(Girl)
                            return
                    $ temp_modifier += 20
                    $ Girl.Forced += 1
                    $ Girl.FaceChange("sad")
                    if "stripforced" in Girl.RecentActions:
                            $ Girl.FaceChange("angry")
                            call AnyLine(Girl,". . .")
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
                            $ Girl.RecentActions.append("stripforced")
                    $ Girl.Statup("Love", 200, -40)
            "You can do better than that. Keep going." if not Girl.Forced:
                    if not ApprovalCheck(Girl, 300, "O", TabM=5) and not ApprovalCheck(Girl, 700, "L", TabM=5):
                            $ Girl.FaceChange("angry")
                            if Girl == RogueX:
                                    ch_r "I don't know who you think I am, but I ain't gonna just jump when you say \"toad\"."
                                    ch_r "I think we're done here for now."
                            elif Girl == KittyX:
                                    ch_k "I'm not just going to do \"whatever\"!"
                                    ch_k "I'm done with this."
                            elif Girl == EmmaX:
                                    ch_e "I think you're overstepping your bounds here, [Girl.Petname]."
                                    ch_e "Remember your place."
                            elif Girl == LauraX:
                                    ch_l "I don't like that tone, [Girl.Petname]."
                            elif Girl == JeanX:
                                    ch_j "Don't talk to me like that. -I- talk to -you- like that."
                            elif Girl == StormX:
                                    ch_s "No, I do not think so."
                            elif Girl == JubesX:
                                    ch_v "Oh, I can, but you're not goinna see it. . ."
                            $ Girl.RecentActions.append("angry")
                            $ Girl.DailyActions.append("angry")
                            call Remove_Girl(Girl)
                            return
                    $ Girl.Statup("Love", 200, -10)
                    $ Girl.Statup("Obed", 50, 3)
                    $ Girl.Statup("Obed", 75, 5)
                    $ temp_modifier += 20
                    $ Girl.Forced += 1
                    $ Girl.FaceChange("sad")
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
        if "ultimatum" not in Girl.DailyActions:
                    $ Girl.DailyActions.append("ultimatum")

        if Girl == RogueX:
                    show Rogue_Sprite at Girl_Dance1(Girl)
        elif Girl == KittyX:
                    show Kitty_Sprite at Girl_Dance1(Girl)
        elif Girl == EmmaX:
                    show Emma_Sprite at Girl_Dance1(Girl)
        elif Girl == LauraX:
                    show Laura_Sprite at Girl_Dance1(Girl)
        elif Girl == JeanX:
                    show Jean_Sprite at Girl_Dance1(Girl)
        elif Girl == StormX:
                    show Storm_Sprite at Girl_Dance1(Girl)
        elif Girl == JubesX:
                    show Jubes_Sprite at Girl_Dance1(Girl)
        "[Girl.Name] begins to dance again."
        return

transform Girl_Dance1(Chr=Ch_Focus):
        subpixel True
        pos (Chr.sprite_location, 50)
        xoffset 0
        yoffset 0
        choice:
            parallel:
                ease 2.5 xoffset -40
                ease 2.5 xoffset 0
            parallel:
                easeout 1.0 yoffset 30 # 70 and 80
                linear 0.5 yoffset 40
                easein 1.0 yoffset 0
                easeout 1.0 yoffset 40
                linear 0.5 yoffset 50 #1.35
                easein 1.0 yoffset 0
        choice:
            parallel:
                ease 2.5 xoffset 40
                ease 2.5 xoffset 0
            parallel:
                easeout 1.0 yoffset 30 #1.3
                linear 0.5 yoffset 40
                easein 1.0 yoffset 0
                easeout 1.0 yoffset 40
                linear 0.5 yoffset 50 #1.35
                easein 1.0 yoffset 0
        choice(0.3):
            parallel:
                ease 2.5 xoffset -30
                ease 2.5 xoffset 0
            parallel:
                ease 1.5 yoffset 150
                ease 3.5 yoffset 0
        repeat
# End Strip Dancing / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
