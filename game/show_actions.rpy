
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


label Rogue_Masturbate: #(Situation = Situation):
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(character)
    if character.Mast:
        $ temp_modifier += 10
    if character.SEXP >= 50:
        $ temp_modifier += 25
    elif character.SEXP >= 30:
        $ temp_modifier += 15
    elif character.SEXP >= 15:
        $ temp_modifier += 5
    if character.Lust >= 90:
        $ temp_modifier += 20
    elif character.Lust >= 75:
        $ temp_modifier += 5
    if "exhibitionist" in character.Traits:
        $ temp_modifier += (3*Taboo)
    if character in Player.Harem or "sex friend" in character.Petnames:
        $ temp_modifier += 10
    elif "ex" in character.Traits:
        $ temp_modifier -= 40
    if character.ForcedCount and not character.Forced:
        $ temp_modifier -= 5 * character.ForcedCount

    $ Approval = ApprovalCheck(character, 1200, TabM = 2) # 120, 135, 150, Taboo -80(200)

    $ character.DrainWord("unseen",1,0) #She sees you, so remove unseens

    if Situation == "join":       # This triggers if you ask to join in
                if Approval > 1 or (Approval and character.Lust >= 50):
                    $ Player.AddWord(1,"join")
                    menu:
                        extend ""
                        "Would you like some help? I could lend some helping hands. . ."  if Player.Semen and character.Action:
                                $ character.Statup("Love", 90, 1)
                                $ character.Statup("Obed", 50, 2)
                                $ character.FaceChange("sexy")
                                ch_r "Well, [character.Petname], I suppose I could use some help with these. . ."
                                $ character.Statup("Obed", 70, 2)
                                $ character.Statup("Inbt", 70, 1)
                                $ Trigger2 = "fondle breasts"
                                $ character.Mast += 1
                                jump Rogue_M_Cycle
                        "Would you like some help? I could. . . up to you, I guess." if Player.Semen and character.Action:
                                $ character.Statup("Love", 70, 2)
                                $ character.Statup("Love", 90, 1)
                                $ character.FaceChange("sexy")
                                ch_r "Well, [character.Petname], I suppose you could help me with these. . ."
                                $ character.Statup("Obed", 70, 2)
                                $ character.Statup("Inbt", 70, 1)
                                $ D20 = renpy.random.randint(1, 20)
                                if D20 > 10:
                                    $ Trigger2 = "fondle breasts"
                                else:
                                    $ Trigger2 = "suck breasts"
                                $ character.Mast += 1
                                jump Rogue_M_Cycle
                        "Why don't we take care of each other?" if Player.Semen and character.Action:
                                $ character.FaceChange("sexy")
                                ch_r "Well what did you have in mind?"
                                $ renpy.pop_call()          #removes the call to this label
                                return                      #returns to sexmenu=
                        "You look like you have things well in hand. . .":
                                if character.Lust >= 50:
                                    $ character.Statup("Love", 70, 2)
                                    $ character.Statup("Love", 90, 1)
                                    $ character.FaceChange("sexy")
                                    ch_r "Well, [character.Petname], I suppose I do at that . ."
                                    $ character.Statup("Obed", 80, 3)
                                    $ character.Statup("Inbt", 80, 5)
                                    jump Rogue_M_Cycle
                                elif ApprovalCheck(character, 1000):
                                    $ character.FaceChange("sly")
                                    ch_r "Well I did, but I think I've got it taken care of for now. . ."
                                else:
                                    $ character.FaceChange("angry")
                                    ch_r "Well I did, but now you've blown the mood."

                #else: You've failed all checks so she kicks you out.
                $ character.ArmPose = 1
                $ character.OutfitChange(Changed=0)
                $ character.Action -= 1
                $ Player.Statup("Focus", 50, 30)
                call Checkout(1)
                $ Line = 0
                $ Situation = 0
                $ renpy.pop_call()          #removes the call to this label
                if Approval:
                        $ character.FaceChange("bemused", 2)
                        if bg_current == "bg rogue":
                            ch_r "So what did you come over for anyway, [character.Petname]?"
                        else:
                            ch_r "So . . . fancy bumping into you here, [character.Petname]. . ."
                        $ character.Blush = 1
                else:
                        $ character.Statup("Love", 200, -5)
                        $ character.FaceChange("angry")
                        $ character.RecentActions.append("angry")
                        $ character.DailyActions.append("angry")
                        if bg_current == "bg rogue":
                            ch_r "Well if you don't mind, I'd kind of appreciate you getting out of here. Maybe knock next time?"
                            "[character.Name] kicks you out of her room."
                            $ renpy.pop_call()
                            jump Campus_Map
                        else:
                            ch_r "Well if you don't mind, I'm getting out of here. Maybe knock next time?"
                            call Remove_Girl(character)
                return                      #returns to sexmenu, which returns to original
    #End of "Join" option



    if Situation == character:                                                                  #Rogue auto-starts
                if Approval > 2:                                                      # fix, add rogue auto stuff here
                        if character.PantsNum() == 5:
                            "[character.Name]'s hand snakes down her body, and hikes up her skirt."
                            $ character.Upskirt = 1
                        elif character.PantsNum() > 6:
                            "[character.Name] slides her hand down her body and into her jeans."
                        elif character.HoseNum() >= 5:
                            "[character.Name]'s hand slides down her body and under her [character.Hose]."
                        elif character.Panties:
                            "[character.Name]'s hand slides down her body and under her [character.Panties]."
                        else:
                            "[character.Name]'s hand slides down her body and begins to caress her pussy."
                        $ character.SeenPanties = 1
                        "She starts to slowly rub herself."
                        call Rogue_First_Bottomless
                        menu:
                            "What do you do?"
                            "Nothing.":
                                    $ character.Statup("Inbt", 80, 3)
                                    $ character.Statup("Inbt", 60, 2)
                                    "[character.Name] begins to masturbate."
                            "Go for it.":
                                    $ character.FaceChange("sexy, 1")
                                    $ character.Statup("Inbt", 80, 3)
                                    ch_p "That is so sexy, [character.Pet]."
                                    $ character.NameCheck() #checks reaction to petname
                                    "You lean back and enjoy the show."
                                    $ character.Statup("Love", 80, 1)
                                    $ character.Statup("Obed", 90, 1)
                                    $ character.Statup("Obed", 50, 2)
                            "Ask her to stop.":
                                    $ character.FaceChange("surprised")
                                    $ character.Statup("Inbt", 70, 1)
                                    ch_p "Let's not do that right now, [character.Pet]."
                                    $ character.NameCheck() #checks reaction to petname
                                    "[character.Name] pulls her hands away from herself."
                                    $ character.OutfitChange(Changed=0)
                                    $ character.Statup("Obed", 90, 1)
                                    $ character.Statup("Obed", 50, 1)
                                    $ character.Statup("Obed", 30, 2)
                                    return
                        jump Rogue_M_Prep
                else:
                        $ temp_modifier = 0                               # fix, add rogue auto stuff here
                        $ Trigger2 = 0
                return
    #End if Rogue intitiates this action

    #first time
    if not character.Mast:
            $ character.FaceChange("surprised", 1)
            $ character.Mouth = "kiss"
            ch_r "You want me to get myself off, while you watch?"
            if character.Forced:
                $ character.FaceChange("sad")
                ch_r "So you just want to watch then?"


    #First time dialog
    if not character.Mast and Approval:
            if character.Forced:
                $ character.FaceChange("sad")
                $ character.Statup("Love", 70, -3, 1)
                $ character.Statup("Love", 20, -2, 1)
            elif character.Love >= (character.Obed + character.Inbt):
                $ character.FaceChange("sexy")
                $ character.Brows = "sad"
                $ character.Mouth = "smile"
                ch_r "Since my love life's been a bit. . . limited, I've gotten pretty good at this."
            elif character.Obed >= character.Inbt:
                $ character.FaceChange("normal")
                ch_r "If that's what you want, [character.Petname]. . ."
            else: # Uninhibited
                $ character.FaceChange("sad")
                $ character.Mouth = "smile"
                ch_r "I guess it could be fun with you watching. . ."


    #Second time+ initial dialog
    elif Approval:
            if character.Forced:
                $ character.FaceChange("sad")
                $ character.Statup("Love", 70, -3, 1)
                $ character.Statup("Love", 20, -2, 1)
                ch_r "You want to watch me again?"
            elif Approval and "masturbation" in character.RecentActions:
                $ character.FaceChange("sexy", 1)
                ch_r "I guess I have a bit more in me. . ."
                jump Rogue_M_Prep
            elif Approval and "masturbation" in character.DailyActions:
                $ character.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["You enjoyed the show?",
                    "Didn't get enough earlier?",
                    "It is nice to have an audience. . ."])
                ch_r "[Line]"
            elif character.Mast < 3:
                $ character.FaceChange("sexy", 1)
                $ character.Brows = "confused"
                ch_r "You like to watch, huh?"
            else:
                $ character.FaceChange("sexy", 1)
                $ character.ArmPose = 2
                $ Line = renpy.random.choice(["You sure do like to watch.",
                    "So you'd like me to go again?",
                    "You want to watch some more?",
                    "You want me ta diddle myself?"])
                ch_r "[Line]"
                $ Line = 0
    #End second time+ initial dialog

    #If she's into it. . .
    if Approval >= 2:
            if character.Forced:
                $ character.FaceChange("sad")
                $ character.Statup("Obed", 90, 1)
                $ character.Statup("Inbt", 60, 1)
                ch_r "I suppose, let me get comfortable. . ."
            else:
                $ character.FaceChange("sexy", 1)
                $ character.Statup("Love", 90, 1)
                $ character.Statup("Inbt", 50, 3)
                $ Line = renpy.random.choice(["Well. . . ok.",
                    "I suppose it would help to have something nice to look at. . .",
                    "I've kind of needed this anyways. . .",
                    "Sure!",
                    "I guess I could. . . give it a go.",
                    "Heh, ok, ok."])
                ch_r "[Line]"
                $ Line = 0
            $ character.Statup("Obed", 20, 1)
            $ character.Statup("Obed", 60, 1)
            $ character.Statup("Inbt", 70, 2)
            jump Rogue_M_Prep

    #If she's not into it, but maybe. . .
    else:
        menu:
            ch_r "That's. . . a little intimate, [character.Petname]."
            "Maybe later?":
                    $ character.FaceChange("sexy", 1)
                    if character.Lust > 50:
                        ch_r "Well, definitely later. . . but I'll have to think about inviting you."
                    else:
                        ch_r "Hmm, maybe. . . I'll let you know."
                    $ character.Statup("Love", 80, 2)
                    $ character.Statup("Inbt", 70, 2)
                    return
            "You look like you could use it. . .":
                    if Approval:
                        $ character.FaceChange("sexy")
                        $ character.Statup("Obed", 90, 2)
                        $ character.Statup("Obed", 50, 2)
                        $ character.Statup("Inbt", 70, 3)
                        $ character.Statup("Inbt", 40, 2)
                        $ Line = renpy.random.choice(["Well. . . ok.",
                            "I suppose it would help to have something nice to look at. . .",
                            "I've kind of needed this anyways. . .",
                            "Sure!",
                            "I guess I could. . . give it a go.",
                            "Heh, ok, ok."])
                        ch_r "[Line]"
                        $ Line = 0
                        jump Rogue_M_Prep

            "Just get at it already.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(character, 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                    if Approval > 1 or (Approval and character.Forced):
                        $ character.FaceChange("sad")
                        $ character.Statup("Love", 70, -5, 1)
                        $ character.Statup("Love", 200, -5)
                        ch_r "Ok, fine. I'll give it a try."
                        $ character.Statup("Obed", 80, 4)
                        $ character.Statup("Inbt", 80, 1)
                        $ character.Statup("Inbt", 60, 3)
                        $ character.Forced = 1
                        jump Rogue_M_Prep
                    else:
                        $ character.Statup("Love", 200, -20)
                        $ character.RecentActions.append("angry")
                        $ character.DailyActions.append("angry")
    # end of asking her to do it

    #She refused all offers.
    $ character.ArmPose = 1
    if character.Forced:
            $ character.FaceChange("angry", 1)
            ch_r "I'm not doing something so. . . intimate with you watching."
            $ character.Statup("Lust", 90, 5)
            if character.Love > 300:
                $ character.Statup("Love", 70, -2)
            $ character.Statup("Obed", 50, -2)
            $ character.RecentActions.append("angry")
            $ character.DailyActions.append("angry")
            $ character.RecentActions.append("no masturbation")
            $ character.DailyActions.append("no masturbation")
            return
    elif Taboo:                             # she refuses and this is too public a place for her
            $ character.FaceChange("angry", 1)
            $ character.DailyActions.append("tabno")
            ch_r "I can't do that here!"
            $ character.Statup("Lust", 90, 5)
            $ character.Statup("Obed", 50, -3)
            return
    elif character.Mast:
            $ character.FaceChange("sad")
            ch_r "Nope, not anymore, you'll have to go back to Internet porn."
    else:
            $ character.FaceChange("normal", 1)
            ch_r "Heh, no, I'm not doing that."
    $ character.RecentActions.append("no masturbation")
    $ character.DailyActions.append("no masturbation")
    $ temp_modifier = 0
    return

label Rogue_M_Prep:
    $ character.Upskirt = 1
    $ character.PantiesDown = 1
    call Rogue_First_Bottomless(1)
    call Set_The_Scene(Dress=0)

    #if she hasn't seen you yet. . .
    if "unseen" in character.RecentActions:
            $ character.FaceChange("sexy")
            $ character.Eyes = "closed"
            $ character.ArmPose = 2
            "You see [character.Name] leaning back, masturbating. You don't think she's noticed you yet."
    else:
            $ character.FaceChange("sexy")
            $ character.ArmPose = 2
            "[character.Name] lays back and starts to toy with herself."
            if not character.Mast:#First time
                    if character.Forced:
                        $ character.Statup("Love", 90, -20)
                        $ character.Statup("Obed", 70, 45)
                        $ character.Statup("Inbt", 80, 35)
                    else:
                        $ character.Statup("Love", 90, 15)
                        $ character.Statup("Obed", 70, 35)
                        $ character.Statup("Inbt", 80, 40)


    $ Trigger = "masturbation"
    if not Trigger3:
        $ Trigger3 = "fondle pussy"

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    if Taboo:
        $ character.DrainWord("tabno")
    $ character.DrainWord("no masturbation")
    $ character.RecentActions.append("masturbation")
    $ character.DailyActions.append("masturbation")

label Rogue_M_Cycle:
    if Situation == "join":
        # resets the call made to this option
        $ renpy.pop_call()
        $ Situation = 0

    while Round > 0:
        call reset_position(character, trigger = "masturbation")
        call Shift_Focus(character)
        $ character.LustFace
        if "unseen" in character.RecentActions:
                $ character.Eyes = "closed"

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep Watching.":
                                pass

                        "[character.Name]. . .[[jump in]" if "unseen" not in character.RecentActions and "join" not in Player.RecentActions and character.Loc == bg_current:
                                "[character.Name] slows what she's doing with a sly grin."
                                ch_r "Yeah, did you want something, [character.Petname]?"
                                $ Situation = "join"
                                call Rogue_Masturbate
                        "\"Ahem. . .\"" if "unseen" in character.RecentActions:
                                jump Rogue_M_Interupted

                        "Start jack'in it." if Trigger2 != "jackin":
                                call Jackin(character)
                        "Stop jack'in it." if Trigger2 == "jackin":
                                $ Trigger2 = 0

                        "Slap her ass" if character.Loc == bg_current:
                                if "unseen" in character.RecentActions:
                                        "You smack [character.Name] firmly on the ass!"
                                        jump Rogue_M_Interupted
                                else:
                                        call Slap_Ass(character)
                                        $ Cnt += 1
                                        $ Round -= 1
                                        jump Rogue_M_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0

                        "Change what I'm doing":
                                menu:
                                    "Offhand action" if character.Loc == bg_current:
                                            if character.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ character.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(character,"tired")

                                    "Threesome actions (locked)" if not Partner or "unseen" in character.RecentActions or character.Loc == bg_current:
                                        pass
                                    "Threesome actions" if character.Loc == bg_current and Partner and "unseen" not in character.RecentActions:
                                        menu:
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(character)
                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(character)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Rogue_M_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Rogue_M_Cycle
                                            "Never mind":
                                                        jump Rogue_M_Cycle

                                    "Show her feet" if not ShowFeet and (character.Pose == "doggy" or character.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (character.Pose == "doggy" or character.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [character.Name]":
                                            if "unseen" in character.RecentActions:
                                                    ch_p "Oh, yeah, take it off. . ."
                                                    jump Rogue_M_Interupted
                                            else:
                                                    call Girl_Undress(character)
                                    "Clean up [character.Name] (locked)" if not character.Spunk:
                                            pass
                                    "Clean up [character.Name]" if character.Spunk:
                                            if "unseen" in character.RecentActions:
                                                    ch_p "You've got a little something on you. . ."
                                                    jump Rogue_M_Interupted
                                            else:
                                                    call Girl_Cleanup(character,"ask")
                                    "Never mind":
                                            jump Rogue_M_Cycle

                        "Back to Sex Menu" if MultiAction and character.Loc == bg_current:
                                    ch_p "Let's try something else."
                                    call reset_position(character)
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Rogue_M_Interupted
                        "End Scene" if not MultiAction or character.Loc != bg_current:
                                    ch_p "Let's stop for now."
                                    call reset_position(character)
                                    $ Line = 0
                                    jump Rogue_M_Interupted
        #End menu (if Line)

        call Shift_Focus(character)
        call Sex_Dialog(character,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up

        if Player.Focus >= 100 or character.Lust >= 100:
                    #If you can cum:
                    if Player.Focus >= 100:
                        if "unseen" not in character.RecentActions:
                            #if she knows you're there
                            call Player_Cumming(character)
                            if "angry" in character.RecentActions:
                                call reset_position(character)
                                return
                            $ character.Statup("Lust", 200, 5)
                            if 100 > character.Lust >= 70 and character.OCount < 2:
                                $ character.RecentActions.append("unsatisfied")
                                $ character.DailyActions.append("unsatisfied")
                            $ Line = "came"
                        else: #If she wasn't aware you were there
                            "You grunt and try to hold it in."
                            $ Player.Focus = 95
                            if character.Loc == bg_current:
                                    jump Rogue_M_Interupted

                    #If Rogue can cum
                    if character.Lust >= 100:
                        call Girl_Cumming(character)
                        if character.Loc == bg_current:
                                jump Rogue_M_Interupted

                    if Line == "came":
                        $ Line = 0
                        if not Player.Semen:
                            "You're emptied out, you should probably take a break."
                            $ Trigger2 = 0 if Trigger2 == "jackin" else Trigger2


                        if "unsatisfied" in character.RecentActions:#And Rogue is unsatisfied,
                            "[character.Name] still seems a bit unsatisfied with the experience."
                            menu:
                                "Let her keep going?"
                                "Yes, keep going for a bit.":
                                    $ Line = "You let her get back into it"
                                    jump Rogue_M_Cycle
                                "No, I'm done.":
                                    "You ask her to stop."
                                    return
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        if "unseen" in character.RecentActions:
                if Round == 10:
                    "It's getting a bit late, [character.Name] will probably be wrapping up soon."
                elif Round == 5:
                    "She's definitely going to stop soon."
        else:
                if character.Loc == bg_current:
                        call Escalation(character) #sees if she wants to escalate things

                if Round == 10:
                    ch_r "We might want to wrap this up, it's getting late."
                    $ character.Lust += 10
                elif Round == 5:
                    ch_r "Seriously, it'll be time to stop soon."
                    $ character.Lust += 25

    #Round = 0 loop breaks
    $ character.FaceChange("bemused", 0)
    $ Line = 0
    if "unseen" not in character.RecentActions:
        ch_r "Ok, [character.Petname], that's enough of that for now."

label Rogue_M_Interupted:

    # If she hasn't noticed you're there before cumming
    if "unseen" in character.RecentActions:
                $ character.FaceChange("surprised", 1)
                "[character.Name] stops what she's doing with a start, eyes wide."
                call Rogue_First_Bottomless(1)
                $ character.FaceChange("surprised", 1)

                #If you've been jacking it
                if Trigger2 == "jackin":
                        ch_r "H- how long you been stand'in there, [character.Petname]?"
                        $ character.Eyes = "down"
                        menu:
                            ch_r "And why is your cock out like that?!"
                            "Long enough, it was an excellent show.":
                                    $ character.FaceChange("sexy")
                                    $ character.Statup("Obed", 50, 3)
                                    $ character.Statup("Obed", 70, 2)
                                    ch_r "Well, I imagine it was. . ."
                                    if character.Love >= 800 or character.Obed >= 500 or character.Inbt >= 500:
                                        $ temp_modifier += 10
                                        $ character.Statup("Lust", 90, 5)
                                        ch_r "And the view from this angle ain't so bad either. . ."

                            "I. . . just got here?":
                                    $ character.FaceChange("angry")
                                    $ character.Statup("Love", 70, 2)
                                    $ character.Statup("Love", 90, 1)
                                    $ character.Statup("Obed", 50, 2)
                                    $ character.Statup("Obed", 70, 2)
                                    "She looks pointedly at your cock,"
                                    ch_r "A likely story . . ."
                                    if character.Love >= 800 or character.Obed >= 500 or character.Inbt >= 500:
                                            $ temp_modifier += 10
                                            $ character.Statup("Lust", 90, 5)
                                            $ character.FaceChange("bemused", 1)
                                            ch_r "Still, can't blame a fella for take'in inspirations."
                                    else:
                                            $ temp_modifier -= 10
                                            $ character.Statup("Lust", 200, -5)
                        call Seen_First_Peen(character,Partner)
                        ch_r "Hmm. . ."

                #you haven't been jacking it
                else:
                        ch_r "H- how long you been stand'in there, [character.Petname]?"
                        menu:
                            extend ""
                            "Long enough.":
                                    $ character.FaceChange("sexy", 1)
                                    $ character.Statup("Obed", 50, 3)
                                    $ character.Statup("Obed", 70, 2)
                                    ch_r "Well I hope you got a good show out of it. . ."
                            "I just got here.":
                                    $ character.FaceChange("bemused", 1)
                                    $ character.Statup("Love", 70, 2)
                                    $ character.Statup("Love", 90, 1)
                                    ch_r "A likely story . . ."
                                    $ character.Statup("Obed", 50, 2)
                                    $ character.Statup("Obed", 70, 2)

                $ character.DrainWord("unseen",1,0) #She sees you, so remove unseens
                $ character.Mast += 1
                if Round <= 10:
                    ch_r "It's getting too late to do much about it right now though."
                    return
                $ Situation = "join"
                call Rogue_Masturbate
                "error: report this if you see it."
                return #should be redundant
    #End Unseen

    #else, if She's seen you already
    $ character.Action -= 1
    $ character.Mast += 1

    if Partner == EmmaX:
        call Partner_Like(character,4)
    else:
        call Partner_Like(character,3)
    call Checkout
    if Situation == "shift":
        $ Situation = 0
        return
    $ Situation = 0

    if character.Loc != bg_current:
        return

    if Round <= 10:
            ch_r "I need to take a little break here, [character.Petname]."
            return
    $ character.FaceChange("sexy", 1)
    if character.Lust < 20:
        ch_r "That really worked for me, [character.Petname]. How about you?"
    else:
        ch_r "Yeah, what did you want?"
    menu:
        extend ""
        "Well, I have something you could take care of. . ." if Player.Semen and character.Action:
                $ Situation = "shift"
                return
        "You could just keep going. . ." if Player.Semen:
                $ character.FaceChange("sly")
                if character.Action and Round >= 10:
                    ch_r "Well, alright. . ."
                    jump Rogue_M_Cycle
                else:
                    ch_r "I'm kinda worn out, maybe time for a break. . ."
        "I'm good here. [[Stop]":
                if character.Love < 800 and character.Inbt < 500 and character.Obed < 500:
                    $ character.OutfitChange(Changed=0)
                $ character.FaceChange("normal")
                $ character.Brows = "confused"
                ch_r "Well. . . ok then. . ."
                $ character.Brows = "normal"
        "You should probably stop for now." if character.Lust > 30:
                $ character.FaceChange("angry")
                ch_r "Well if you say so."
    return
