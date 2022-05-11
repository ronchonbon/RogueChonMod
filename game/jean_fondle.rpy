# JeanX.Fondle /////////////////////////////////////////////////////////////////////////////
label Jean_Fondle:

    $ JeanX.Mouth = "smile"
    if not JeanX.Action:
        ch_j "Gimme a minute, k?"
        return
    menu:
        ch_j "Well? Where did you want to touch, [JeanX.Petname]?"
        "Your breasts?" if JeanX.Action:
                jump Jean_Fondle_Breasts
        "Your thighs?" if JeanX.Action:
                jump Jean_Fondle_Thighs
        "Your pussy?" if JeanX.Action:
                jump Jean_Fondle_Pussy
        "Your Ass?" if JeanX.Action:
                jump Jean_Fondle_Ass
        "Never mind.":
                return
    return


# ////////////////////////////////////////////////////////////////////////Start Fondle Pussy
label Jean_Fondle_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JeanX)
                                                                                        # Will she let you fondle? Modifiers
    if JeanX.FondleP: #You've done it before
        $ temp_modifier += 20
    if JeanX.PantsNum() >= 6 or JeanX.HoseNum() >= 5: # she's got pants on.
        $ temp_modifier -= 10
    if JeanX.Lust > 75: #She's really horny
        $ temp_modifier += 15
    if JeanX.Lust > 75 and Situation == "auto": #She's really horny
        $ temp_modifier += 10
    if "exhibitionist" in JeanX.Traits:
        $ temp_modifier += (2*JeanX.Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JeanX.Traits:
        $ temp_modifier -= 25
    if JeanX.ForcedCount and not JeanX.Forced:
        $ temp_modifier -= 5 * JeanX.ForcedCount

    if JeanX.Taboo and "tabno" in JeanX.DailyActions:
        $ temp_modifier -= 10
    if JeanX.Taboo and "public" not in JeanX.History:
        $ temp_modifier -= 20

    if "no fondle pussy" in JeanX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no fondle pussy" in JeanX.RecentActions else 0

    $ Approval = ApprovalCheck(JeanX, 1050, TabM = 2) # 105, 120, 135, Taboo -80(185)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ JeanX.FaceChange("sexy")
            $ JeanX.Statup("Obed", 90, 1)
            $ JeanX.Statup("Obed", 70, 2)
            $ JeanX.Statup("Inbt", 70, 3)
            $ JeanX.Statup("Inbt", 30, 2)
            "As your hand creeps up her thigh, [JeanX.Name] seems a bit surprised, but then nods."
            jump Jean_FP_Prep
        else:
            $ JeanX.FaceChange("surprised")
            $ JeanX.Statup("Obed", 50, -2)
            ch_j "Not so fast, [JeanX.Petname]. . ."
            $ temp_modifier = 0
            $ Trigger2 = 0
            return

    if Situation == "pullback":
        $ JeanX.FaceChange("surprised")
        $ JeanX.Brows = "sad"
        if JeanX.Lust > 80:
            $ JeanX.Statup("Love", 70, -4)
        $ JeanX.Statup("Obed", 90, 1)
        $ JeanX.Statup("Obed", 70, 2)
        "As your hand pulls out, [JeanX.Name] gasps and looks upset."
        jump Jean_FP_Prep
    elif "fondle pussy" in JeanX.RecentActions:
        $ JeanX.FaceChange("sexy", 1)
        ch_j "Mmmm, again? I guess. . ."
        jump Jean_FP_Prep
    elif "fondle pussy" in JeanX.DailyActions:
        $ JeanX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Chill. . .",
            "Take it slow, I'm still shaking from earlier.",
            "Mmm. . ."])
        ch_j "[Line]"

    if Approval >= 2:                                                                   #She's into it. . .
        $ JeanX.FaceChange("bemused", 1)
        if JeanX.Forced:
            $ JeanX.FaceChange("sad")
            $ JeanX.Statup("Love", 70, -3, 1)
            $ JeanX.Statup("Love", 20, -2, 1)
            $ JeanX.Statup("Obed", 90, 1)
            $ JeanX.Statup("Inbt", 60, 1)
        ch_j "Mmmm, I couldn't refuse. . ."
        $ JeanX.Statup("Love", 90, 1)
        $ JeanX.Statup("Inbt", 50, 3)
        jump Jean_FP_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ JeanX.FaceChange("angry", 1)
        if "no fondle pussy" in JeanX.RecentActions:
            ch_j "I'm not used to repeating myself."
        elif JeanX.Taboo and "tabno" in JeanX.DailyActions and "no fondle pussy" in JeanX.DailyActions:
            ch_j "I told you not to touch me like that in public!"
        elif "no fondle pussy" in JeanX.DailyActions:
            ch_j "Don't ask me again today."
        elif JeanX.Taboo and "tabno" in JeanX.DailyActions:
            ch_j "I told you. . . not here, [JeanX.Petname]."
        elif not JeanX.FondleP:
            $ JeanX.FaceChange("bemused")
            ch_j "I don't think we're there yet, [JeanX.Petname]. . ."
        else:
            $ JeanX.FaceChange("bemused")
            ch_j "You wish."
        menu:
            extend ""
            "Sorry, never mind." if "no fondle pussy" in JeanX.DailyActions:
                $ JeanX.FaceChange("bemused")
                ch_j "It's fine, I get it."
                return
            "Maybe later?" if "no fondle pussy" not in JeanX.DailyActions:
                $ JeanX.FaceChange("sexy")
                ch_j ". . . I guess? Maybe."
                $ JeanX.Statup("Love", 80, 2)
                $ JeanX.Statup("Inbt", 70, 2)
                if JeanX.Taboo:
                    $ JeanX.RecentActions.append("tabno")
                    $ JeanX.DailyActions.append("tabno")
                $ JeanX.RecentActions.append("no fondle pussy")
                $ JeanX.DailyActions.append("no fondle pussy")
                return
            "Come on, Please?":
                if Approval:
                    $ JeanX.FaceChange("sexy")
                    $ JeanX.Statup("Obed", 90, 2)
                    $ JeanX.Statup("Obed", 50, 2)
                    $ JeanX.Statup("Inbt", 70, 3)
                    $ JeanX.Statup("Inbt", 40, 2)
                    ch_j "Oooh, beg for me. . ."
                    jump Jean_FP_Prep
                else:
                    $ JeanX.FaceChange("sexy")
                    ch_j "No."

            "[[Start fondling anyway]":                                               # Pressured into fondling.
                $ Approval = ApprovalCheck(JeanX, 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                if Approval > 1 or (Approval and JeanX.Forced):
                    $ JeanX.FaceChange("sad")
                    $ JeanX.Statup("Love", 70, -5, 1)
                    $ JeanX.Statup("Love", 200, -2)
                    ch_j ". . .whatever. . ."
                    $ JeanX.Statup("Obed", 50, 4)
                    $ JeanX.Statup("Inbt", 80, 1)
                    $ JeanX.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ JeanX.Forced = 1
                    jump Jean_FP_Prep
                else:
                    $ JeanX.Statup("Love", 200, -15)
                    $ JeanX.FaceChange("angry", 1)
                    "She slaps your hand away."
                    $ JeanX.RecentActions.append("angry")
                    $ JeanX.DailyActions.append("angry")

    if "no fondle pussy" in JeanX.DailyActions:
        ch_j "I don't want to have to go through this again."
        $ JeanX.RecentActions.append("angry")
        $ JeanX.DailyActions.append("angry")
    elif JeanX.Forced:
        $ JeanX.FaceChange("angry", 1)
        ch_j "I don't think so, [JeanX.Petname]."
        $ JeanX.Statup("Lust", 70, 5)
        $ JeanX.Statup("Obed", 50, -2)
        $ JeanX.RecentActions.append("angry")
        $ JeanX.DailyActions.append("angry")
    elif JeanX.Taboo:
        $ JeanX.FaceChange("angry", 1)
        $ JeanX.RecentActions.append("tabno")
        $ JeanX.DailyActions.append("tabno")
        ch_j "I'm. . . not comfortable. . . in public. . ."
    elif JeanX.FondleP:
        $ JeanX.FaceChange("sad")
        ch_j "You can keep those to yourself."
    else:
        $ JeanX.FaceChange("sexy")
        $ JeanX.Mouth = "sad"
        ch_j "No thanks, [JeanX.Petname]."
    $ JeanX.RecentActions.append("no fondle pussy")
    $ JeanX.DailyActions.append("no fondle pussy")
    $ temp_modifier = 0
    return

label Jean_FP_Prep: #Animation set-up
    if Trigger2 == "fondle pussy":
        return

    call Jean_Pussy_Launch("fondle pussy")

    if Situation == JeanX:
            #Jean auto-starts
            $ Situation = 0
            if (JeanX.Legs and not JeanX.Upskirt) or (JeanX.Panties and not JeanX.PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck(JeanX, 1250, TabM = 1) or (JeanX.SeenPussy and ApprovalCheck(JeanX, 500) and not JeanX.Taboo):
                        $ JeanX.Upskirt = 1
                        $ JeanX.PantiesDown = 1
                        $ Line = 0
                        if JeanX.PantsNum() == 5:
                            $ Line = JeanX.Name + " hikes up her skirt"
                        elif JeanX.PantsNum() >= 6:
                            $ Line = JeanX.Name + " pulls down her " + JeanX.Legs
                        else:
                            $ Line = 0
                        if JeanX.Panties:
                            if Line:
                                #wearing pants
                                "[Line] and pulls her [JeanX.Panties] out of the way."
                                "She then grabs your arm and then presses your hand against her crotch, clearly intending you to get to work."
                            else:
                                #no pants
                                "She pulls her [JeanX.Panties] out of the way, and then presses your hand against her crotch."
                                "She clearly intends for you to get to work."
                        else:
                            #pants but no panties
                            "[Line], and then presses your hand against her crotch."
                            "She clearly intends for you to get to work."
                        call Jean_First_Bottomless(1)
                else:
                        "[JeanX.Name] grabs your arm and presses your hand against her crotch, clearly intending you to get to work."
            else:
                        "[JeanX.Name] grabs your arm and presses your hand against her crotch, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":
                    $ JeanX.Statup("Inbt", 80, 3)
                    $ JeanX.Statup("Inbt", 50, 2)
                    "You start to run your fingers along her pussy."
                "Praise her.":
                    $ JeanX.FaceChange("sexy", 1)
                    $ JeanX.Statup("Inbt", 80, 3)
                    ch_p "I like the initiative, [JeanX.Pet]."
                    $ JeanX.NameCheck() #checks reaction to petname
                    "You start to run your fingers along her pussy."
                    $ JeanX.Statup("Love", 85, 1)
                    $ JeanX.Statup("Obed", 90, 1)
                    $ JeanX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your hand back."
                    $ JeanX.FaceChange("surprised")
                    $ JeanX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that right now, [JeanX.Pet]."
                    $ JeanX.NameCheck() #checks reaction to petname
                    $ JeanX.Statup("Love", 70, -4)
                    "[JeanX.Name] pulls back."
                    $ JeanX.Statup("Obed", 90, 1)
                    $ JeanX.Statup("Obed", 50, 1)
                    $ JeanX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ JeanX.AddWord(1,"refused","refused")
                    return
            #end auto

    if not JeanX.Forced and Situation != "auto":
        $ temp_modifier = 0
        call Bottoms_Off(JeanX)
        if "angry" in JeanX.RecentActions:
            return
    $ temp_modifier = 0

    if not JeanX.FondleP:
        if JeanX.Forced:
            $ JeanX.Statup("Love", 90, -50)
            $ JeanX.Statup("Obed", 70, 35)
            $ JeanX.Statup("Inbt", 80, 25)
        else:
            $ JeanX.Statup("Love", 90, 10)
            $ JeanX.Statup("Obed", 70, 10)
            $ JeanX.Statup("Inbt", 80, 15)
    if JeanX.Taboo:
        $ JeanX.Statup("Inbt", 200, (int(Taboo/10)))
        $ JeanX.Lust += int(Taboo/5)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if JeanX.Taboo:
        $ JeanX.DrainWord("tabno")
    $ JeanX.DrainWord("no fondle pussy")
    $ JeanX.RecentActions.append("fondle pussy")
    $ JeanX.DailyActions.append("fondle pussy")
    call Jean_Pussy_Launch("fondle pussy")

    $ Speed = 1

label Jean_FP_Cycle: #Repeating strokes
    while Round > 0:
        call ViewShift(JeanX,JeanX.Pose,0,"fondle pussy")
        call Shift_Focus(JeanX)
        $ JeanX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "I want to stick a finger in. . ." if Speed != 2:
                                if JeanX.InsertP:
                                    $ Speed = 2
                                else:
                                    menu:
                                        "Ask her first":
                                            $ Situation = "shift"
                                        "Don't ask first [[just stick it in]":
                                            $ Situation = "auto"
                                    call Jean_Insert_Pussy

                        "Pull back a bit. . ." if Speed == 2:
                                    $ Speed = 0

                        "Slap her ass":
                                    call Slap_Ass(JeanX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Jean_FP_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0
                        "View":
                                    call ViewShift(JeanX,"menu")
                                    jump Jean_FP_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if JeanX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ JeanX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Shift primary action":
                                            if JeanX.Action and MultiAction:
                                                    menu:
                                                        "I want to lick your pussy.":
                                                                $ Situation = "shift"
                                                                call Jean_FP_After
                                                                call Jean_Lick_Pussy
                                                        "Just start licking":
                                                                $ Situation = "auto"
                                                                call Jean_FP_After
                                                                call Jean_Lick_Pussy
                                                        "Pull back to the thighs":
                                                                $ Situation = "pullback"
                                                                call Jean_FP_After
                                                                call Jean_Fondle_Thighs
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Jean_FP_After
                                                                call Jean_Dildo_Pussy
                                                        "Never Mind":
                                                                jump Jean_FP_Cycle
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Jean_FP_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [JeanX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(JeanX)
                                            "Ask [JeanX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(JeanX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(JeanX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jean_FP_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jean_FP_Cycle
                                            "Never mind":
                                                        jump Jean_FP_Cycle

                                    "Show her feet" if not ShowFeet and (JeanX.Pose == "doggy" or JeanX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (JeanX.Pose == "doggy" or JeanX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [JeanX.Name]":
                                            call Girl_Undress(JeanX)
                                    "Clean up [JeanX.Name] (locked)" if not JeanX.Spunk:
                                            pass
                                    "Clean up [JeanX.Name]" if JeanX.Spunk:
                                            call Girl_Cleanup(JeanX,"ask")
                                    "Never mind":
                                            jump Jean_FP_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Jean_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Jean_FP_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Jean_Pos_Reset
                                    $ Line = 0
                                    jump Jean_FP_After
        #End menu (if Line)

        call Shift_Focus(JeanX)
        call Sex_Dialog(JeanX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JeanX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JeanX)
                            if "angry" in JeanX.RecentActions:
                                call Jean_Pos_Reset
                                return
                            $ JeanX.Statup("Lust", 200, 5)
                            if 100 > JeanX.Lust >= 70 and JeanX.OCount < 2:
                                $ JeanX.RecentActions.append("unsatisfied")
                                $ JeanX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jean_FP_After
                            $ Line = "came"

                    if JeanX.Lust >= 100:
                            #If Jean can cum
                            call Girl_Cumming(JeanX)
                            if Situation == "shift" or "angry" in JeanX.RecentActions:
                                jump Jean_FP_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in JeanX.RecentActions:#And Jean is unsatisfied,
                                    "[JeanX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Jean_FP_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if JeanX.SEXP >= 100 or ApprovalCheck(JeanX, 1200, "LO"):
            pass
        elif Cnt == (5 + JeanX.FondleP):
                    $ JeanX.Brows = "confused"
                    ch_j "Mmmm, you're enjoying that, huh?"
        elif JeanX.Lust >= 80:
                    pass
        elif Cnt == (15 + JeanX.FondleP) and JeanX.SEXP >= 15 and not ApprovalCheck(JeanX, 1500):
                    $ JeanX.Brows = "confused"
                    menu:
                        ch_j "Maybe try something else?"
                        "Finish up.":
                                "You let go. . ."
                                jump Jean_FP_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Jean_FP_After
                        "No, this is fun.":
                                if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                                    $ JeanX.Statup("Love", 200, -5)
                                    $ JeanX.Statup("Obed", 50, 3)
                                    $ JeanX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ JeanX.FaceChange("angry", 1)
                                    call Jean_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_j "Well -I'm- bored."
                                    $ JeanX.Statup("Love", 50, -3, 1)
                                    $ JeanX.Statup("Love", 80, -4, 1)
                                    $ JeanX.Statup("Obed", 30, -1, 1)
                                    $ JeanX.Statup("Obed", 50, -1, 1)
                                    $ JeanX.RecentActions.append("angry")
                                    $ JeanX.DailyActions.append("angry")
                                    jump Jean_FP_After
        #End Count check

        call Escalation(JeanX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(JeanX,10) #"You might want to wrap this up, it's getting late."
        elif Round == 5:
                call Sex_Basic_Dialog(JeanX,5)   #"Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ JeanX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(JeanX,"done")   #"Ok, [Girl.Petname], that's enough of that for now."

label Jean_FP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Jean_Pos_Reset

    $ JeanX.FaceChange("sexy")

    $ JeanX.FondleP += 1
    $ JeanX.Action -=1
    if JeanX.PantsNum() < 6 or JeanX.Upskirt:
        $ JeanX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ JeanX.Addictionrate += 1

    call Partner_Like(JeanX,2)

    if JeanX.FondleP == 1:
            $ JeanX.SEXP += 7
            if not Situation:
                if JeanX.Love >= 500 and "unsatisfied" not in JeanX.RecentActions:
                    ch_j "Well, that was a nice surprise. . ."
                elif JeanX.Obed <= 500 and Player.Focus <= 20:
                    $ JeanX.FaceChange("perplexed", 1)
                    ch_j "Did you find what you were looking for?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_j "Oh? What did you have in mind?"
    call Checkout
    return

# end JeanX.Fondle Pussy /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy
label Jean_Insert_Pussy:
    call Shift_Focus(JeanX)
    if Situation == "auto":                                                                  #You auto-start
        if ApprovalCheck(JeanX, 1100, TabM = 2):
            $ JeanX.FaceChange("surprised")
            $ JeanX.Statup("Obed", 90, 1)
            $ JeanX.Statup("Obed", 70, 2)
            $ JeanX.Statup("Inbt", 70, 3)
            $ JeanX.Statup("Inbt", 30, 2)
            "As you slide a finger in, [JeanX.Name] seems a bit surprised, but seems into it."
            jump Jean_IP_Prep
        else:
            $ JeanX.FaceChange("surprised",2)
            $ JeanX.Statup("Love", 80, -2)
            $ JeanX.Statup("Obed", 50, -3)
            ch_j "Oooh!"
            "She slaps your hand back."
            $ JeanX.FaceChange("perplexed",1)
            ch_j "Not so fast, [JeanX.Petname]. . ."
            return

    if ApprovalCheck(JeanX, 1100, TabM = 2):                                                                   #She's into it. . .
        if JeanX.Forced:
            $ JeanX.FaceChange("sad")
            $ JeanX.Statup("Love", 70, -3, 1)
            $ JeanX.Statup("Love", 20, -2, 1)
            $ JeanX.Statup("Obed", 90, 1)
            $ JeanX.Statup("Inbt", 60, 1)
            ch_j "Going there, huh. . ."
        else:
            $ JeanX.FaceChange("sexy", 1)
            $ JeanX.Statup("Love", 90, 1)
            $ JeanX.Statup("Inbt", 50, 3)
            ch_j "Mmmmmm. . ."
        $ JeanX.Statup("Obed", 20, 1)
        $ JeanX.Statup("Obed", 60, 1)
        $ JeanX.Statup("Inbt", 70, 2)
        jump Jean_IP_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ JeanX.FaceChange("bemused", 1)
        ch_j "Nope."
        $ JeanX.Blush = 0
    return


label Jean_IP_Prep: #Animation set-up
    if not JeanX.InsertP:
        $ JeanX.InsertP = 1
        $ JeanX.SEXP += 10
        if JeanX.Forced:
            $ JeanX.Statup("Love", 90, -60)
            $ JeanX.Statup("Obed", 70, 55)
            $ JeanX.Statup("Inbt", 80, 35)
        else:
            $ JeanX.Statup("Love", 90, 10)
            $ JeanX.Statup("Obed", 70, 20)
            $ JeanX.Statup("Inbt", 80, 25)

    if not JeanX.Forced and Situation != "auto":
        call Girl_Undress(JeanX,"bottom")
        if "angry" in JeanX.RecentActions:
            return

#    call Jean_Pussy_Launch("insert pussy")
    if JeanX.Taboo:
        $ JeanX.Statup("Inbt", 200, (int(Taboo/10)))
        $ JeanX.Lust += int(Taboo/5)

    $ Line = 0
    $ Speed = 2
    return

# end JeanX.Insert Pussy /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Pussy
label Jean_Lick_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JeanX)
                                                                                  # Will she let you fondle? Modifiers
    if JeanX.LickP: #You've done it before
        $ temp_modifier += 15
    if JeanX.PantsNum() >= 6 or JeanX.HoseNum() >= 5: # she's got pants on.
        $ temp_modifier -= 15
    if JeanX.Lust > 95:
        $ temp_modifier += 20
    elif JeanX.Lust > 85: #She's really horny
        $ temp_modifier += 15
    if Situation == "shift":
        $ temp_modifier += 10
    if JeanX.Lust > 85 and Situation == "auto": #She's really horny
        $ temp_modifier += 10
    if "exhibitionist" in JeanX.Traits:
        $ temp_modifier += (4*JeanX.Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JeanX.Traits:
        $ temp_modifier -= 25
    if JeanX.ForcedCount and not JeanX.Forced:
        $ temp_modifier -= 5 * JeanX.ForcedCount

    if JeanX.Taboo and "tabno" in JeanX.DailyActions:
        $ temp_modifier -= 10
    if JeanX.Taboo and "public" not in JeanX.History:
        $ temp_modifier -= 20

    if "no lick pussy" in JeanX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no lick pussy" in JeanX.RecentActions else 0

    $ Approval = ApprovalCheck(JeanX, 1250, TabM = 4) # 125, 140, 155, Taboo -160(285)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ JeanX.FaceChange("surprised")
            $ JeanX.Statup("Obed", 90, 1)
            $ JeanX.Statup("Obed", 70, 2)
            $ JeanX.Statup("Inbt", 70, 3)
            $ JeanX.Statup("Inbt", 30, 2)
            "As you crouch down and start to lick her pussy, [JeanX.Name] starts, but then softens."
            $ JeanX.FaceChange("sexy")
            jump Jean_LP_Prep
        else:
            $ JeanX.FaceChange("surprised")
            $ JeanX.Statup("Love", 80, -2)
            $ JeanX.Statup("Obed", 50, -3)
            ch_j "Hmmm, not yet, [JeanX.Petname]."
            $ JeanX.FaceChange("perplexed",1)
            "She pushes your head back away from her."
            $ temp_modifier = 0
            $ Trigger2 = 0
            return

    if "lick pussy" in JeanX.RecentActions:
        $ JeanX.FaceChange("sexy", 1)
        ch_j "Mmmm, again? I guess. . ."
        jump Jean_LP_Prep
    elif "lick pussy" in JeanX.DailyActions:
        $ JeanX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Huh? Again?",
            "I must have done something right.",
            "I do like this. . .",
            "Mmm. . ."])
        ch_j "[Line]"

    if Approval >= 2:                                                                   #She's into it. . .
        if JeanX.Forced:
            $ JeanX.FaceChange("sad")
            $ JeanX.Statup("Love", 70, -3, 1)
            $ JeanX.Statup("Love", 20, -2, 1)
            $ JeanX.Statup("Obed", 90, 1)
            $ JeanX.Statup("Inbt", 60, 1)
            ch_j "If you must. . ."
        else:
            $ JeanX.FaceChange("sexy", 1)
            $ JeanX.Eyes = "closed"
            $ JeanX.Statup("Love", 90, 1)
            $ JeanX.Statup("Inbt", 50, 3)
            $ JeanX.Statup("Lust", 200, 3)
            ch_j "Mmmmmm. . ."
        $ JeanX.Statup("Obed", 20, 1)
        $ JeanX.Statup("Obed", 60, 1)
        $ JeanX.Statup("Inbt", 70, 2)
        jump Jean_LP_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ JeanX.FaceChange("angry", 1)
        if "no lick pussy" in JeanX.RecentActions:
            ch_j "I'm not used to repeating myself."
        elif JeanX.Taboo and "tabno" in JeanX.DailyActions and "no lick pussy" in JeanX.DailyActions:
            ch_j "You already got your answer!"
        elif "no lick pussy" in JeanX.DailyActions:
            ch_j "Don't ask me again today."
        elif JeanX.Taboo and "tabno" in JeanX.DailyActions:
            ch_j "I told you. . . not here, [JeanX.Petname]."
        elif not JeanX.LickP:
            $ JeanX.FaceChange("bemused")
            ch_j "Mmmm, not right now, [JeanX.Petname]. . ."
        else:
            $ JeanX.FaceChange("bemused")
            ch_j "I'd rather not."
        menu:
            extend ""
            "Sorry, never mind." if "no lick pussy" in JeanX.DailyActions:
                $ JeanX.FaceChange("bemused")
                ch_j "It's fine, I get it."
                return
            "I'm sure I can convince you later. . ." if "no lick pussy" not in JeanX.DailyActions:
                $ JeanX.FaceChange("sexy")
                ch_j "Well, I'll give it some thought, [JeanX.Petname]."
                $ JeanX.Statup("Love", 80, 2)
                $ JeanX.Statup("Inbt", 70, 2)
                if JeanX.Taboo:
                    $ JeanX.RecentActions.append("tabno")
                    $ JeanX.DailyActions.append("tabno")
                $ JeanX.RecentActions.append("no lick pussy")
                $ JeanX.DailyActions.append("no lick pussy")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ JeanX.FaceChange("sexy")
                    $ JeanX.Statup("Obed", 90, 2)
                    $ JeanX.Statup("Obed", 50, 2)
                    ch_j "You make a good point. . ."
                    $ JeanX.Statup("Inbt", 70, 3)
                    $ JeanX.Statup("Inbt", 40, 2)
                    jump Jean_LP_Prep
                else:
                    $ JeanX.FaceChange("sexy")
                    ch_j "I would, but still no, [JeanX.Petname]."

            "[[Get in there anyway]":                                               # Pressured into being licked.
                $ Approval = ApprovalCheck(JeanX, 750, "OI", TabM = 4) # 75, 90, 105, -160(235)
                if Approval > 1 or (Approval and JeanX.Forced):
                    $ JeanX.FaceChange("sad")
                    $ JeanX.Statup("Love", 70, -5, 1)
                    $ JeanX.Statup("Love", 200, -2)
                    ch_j "I guess you won't take \"no\" for an answer. . ."
                    $ JeanX.Statup("Obed", 50, 4)
                    $ JeanX.Statup("Inbt", 80, 1)
                    $ JeanX.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ JeanX.Forced = 1
                    jump Jean_LP_Prep
                else:
                    $ JeanX.Statup("Love", 200, -15)
                    $ JeanX.FaceChange("angry", 1)
                    "She shoves your head back."
                    $ JeanX.RecentActions.append("angry")
                    $ JeanX.DailyActions.append("angry")

    if "no lick pussy" in JeanX.DailyActions:
        ch_j "I don't want to have to go through this again."
        $ JeanX.RecentActions.append("angry")
        $ JeanX.DailyActions.append("angry")
    elif JeanX.Forced:
        $ JeanX.FaceChange("angry", 1)
        ch_j "I really can't, [JeanX.Petname]."
        $ JeanX.Statup("Lust", 80, 5)
        $ JeanX.Statup("Obed", 50, -2)
        $ JeanX.RecentActions.append("angry")
        $ JeanX.DailyActions.append("angry")
    elif JeanX.Taboo:
        $ JeanX.FaceChange("angry", 1)
        $ JeanX.RecentActions.append("tabno")
        $ JeanX.DailyActions.append("tabno")
        ch_j "I'm. . . not comfortable. . . in public. . ."
    elif JeanX.LickP:
        $ JeanX.FaceChange("sad")
        ch_j "Keep your tongue to yourself."
    else:
        $ JeanX.FaceChange("surprised")
        ch_j "Yeah, sorry."
        $ JeanX.FaceChange()
    $ JeanX.RecentActions.append("no lick pussy")
    $ JeanX.DailyActions.append("no lick pussy")
    $ temp_modifier = 0
    return

label Jean_LP_Prep: #Animation set-up
    if Trigger2 == "lick pussy": #fix pull down pants now an option, make it work
        return

    $ temp_modifier = 0
    call Jean_Pussy_Launch("lick pussy")

    if Situation == JeanX:
            #Jean auto-starts
            $ Situation = 0
            if (JeanX.Legs and not JeanX.Upskirt) or (JeanX.Panties and not JeanX.PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck(JeanX, 1250, TabM = 1) or (JeanX.SeenPussy and ApprovalCheck(JeanX, 500) and not JeanX.Taboo):
                        $ JeanX.Upskirt = 1
                        $ JeanX.PantiesDown = 1
                        $ Line = 0
                        if JeanX.PantsNum() == 5:
                            $ Line = JeanX.Name + " hikes up her skirt"
                        elif JeanX.PantsNum() >= 6:
                            $ Line = JeanX.Name + " pulls down her " + JeanX.Legs
                        else:
                            $ Line = 0
                        if JeanX.Panties:
                            if Line:
                                #wearing pants
                                "[Line] and pulls her [JeanX.Panties] out of the way."
                                "She then grabs your head and wraps her thighs around it, clearly intending you to get to work."
                            else:
                                #no pants
                                "She pulls her [JeanX.Panties] out of the way, and then wraps her thighs around your head."
                                "She clearly intends for you to get to work."
                        else:
                            #pants but no panties
                            "[Line], and then wraps her thighs around your head."
                            "She clearly intends for you to get to work."
                        call Jean_First_Bottomless(1)
                else:
                        "[JeanX.Name] grabs your head and wraps her thighs around it, clearly intending you to get to work."
            else:
                        "[JeanX.Name] grabs your head and wraps her thighs around it, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":
                    $ JeanX.Statup("Inbt", 80, 3)
                    $ JeanX.Statup("Inbt", 50, 2)
                    "You start licking."
                "Praise her.":
                    $ JeanX.FaceChange("sexy", 1)
                    $ JeanX.Statup("Inbt", 80, 3)
                    ch_p "Mmm, I like this idea, [JeanX.Pet]."
                    $ JeanX.NameCheck() #checks reaction to petname
                    "You start licking."
                    $ JeanX.Statup("Love", 85, 1)
                    $ JeanX.Statup("Obed", 90, 1)
                    $ JeanX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your head away."
                    $ JeanX.FaceChange("surprised")
                    $ JeanX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that right now, [JeanX.Pet]."
                    $ JeanX.NameCheck() #checks reaction to petname
                    $ JeanX.Statup("Love", 70, -5)
                    "[JeanX.Name] pulls back."
                    $ JeanX.Statup("Obed", 90, 1)
                    $ JeanX.Statup("Obed", 50, 1)
                    $ JeanX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ JeanX.AddWord(1,"refused","refused")
                    return
            #end auto

    if not JeanX.Forced and Situation != "auto":
        $ temp_modifier = 0
        if JeanX.PantsNum() >= 6 and not JeanX.Upskirt:
            $ temp_modifier = 15
        call Bottoms_Off(JeanX)
        if "angry" in JeanX.RecentActions:
            return

    if not JeanX.LickP:
        if JeanX.Forced:
            $ JeanX.Statup("Love", 90, -30)
            $ JeanX.Statup("Obed", 70, 35)
            $ JeanX.Statup("Inbt", 80, 75)
        else:
            $ JeanX.Statup("Love", 90, 35)
            $ JeanX.Statup("Obed", 70, 15)
            $ JeanX.Statup("Inbt", 80, 35)
    if JeanX.Taboo:
        $ JeanX.Statup("Inbt", 200, (int(Taboo/10)))
        $ JeanX.Lust += int(Taboo/5)
    if Situation:
        $ renpy.pop_call()
        $ Situation = 0

    if JeanX.PantsNum() == 5:
        $ JeanX.Upskirt = 1
        $ JeanX.SeenPanties = 1
    call Jean_First_Bottomless(1)

    $ Line = 0
    $ Cnt = 0
    if JeanX.Taboo:
        $ JeanX.DrainWord("tabno")
    $ JeanX.DrainWord("no lick pussy")
    $ JeanX.RecentActions.append("lick pussy")
    $ JeanX.DailyActions.append("lick pussy")
    call Jean_Pussy_Launch("lick pussy")

label Jean_LP_Cycle: #Repeating strokes
    if Trigger2 == "kiss you":
            $ Trigger2 = 0
    while Round > 0:
        call ViewShift(JeanX,JeanX.Pose,0,"lick pussy")
        call Shift_Focus(JeanX)
        $ JeanX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(JeanX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Jean_LP_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0
                        "View":
                                    call ViewShift(JeanX,"menu")
                                    jump Jean_LP_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if JeanX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ JeanX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Shift primary action":
                                            if JeanX.Action and MultiAction:
                                                    menu:
                                                        "Pull out and start rubbing again.":
                                                                if JeanX.Action and MultiAction:
                                                                    $ Situation = "pullback"
                                                                    call Jean_LP_After
                                                                    call Jean_Fondle_Pussy
                                                                else:
                                                                    call Sex_Basic_Dialog(JeanX,"tired")
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Jean_LP_After
                                                                call Jean_Dildo_Pussy
                                                        "Never Mind":
                                                                jump Jean_LP_Cycle
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Jean_LP_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [JeanX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(JeanX)
                                            "Ask [JeanX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(JeanX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(JeanX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jean_LP_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jean_LP_Cycle
                                            "Never mind":
                                                        jump Jean_LP_Cycle

                                    "Show her feet" if not ShowFeet and (JeanX.Pose == "doggy" or JeanX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (JeanX.Pose == "doggy" or JeanX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [JeanX.Name]":
                                            call Girl_Undress(JeanX)
                                    "Clean up [JeanX.Name] (locked)" if not JeanX.Spunk:
                                            pass
                                    "Clean up [JeanX.Name]" if JeanX.Spunk:
                                            call Girl_Cleanup(JeanX,"ask")
                                    "Never mind":
                                            jump Jean_LP_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Jean_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Jean_LP_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Jean_Pos_Reset
                                    $ Line = 0
                                    jump Jean_LP_After
        #End menu (if Line)

        if JeanX.Panties or JeanX.PantsNum() >= 6 or JeanX.HoseNum() >= 5: #This checks if Jean wants to strip down.
                call Girl_Undress(JeanX,"auto")

        call Shift_Focus(JeanX)
        call Sex_Dialog(JeanX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JeanX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JeanX)
                            if "angry" in JeanX.RecentActions:
                                call Jean_Pos_Reset
                                return
                            $ JeanX.Statup("Lust", 200, 5)
                            if 100 > JeanX.Lust >= 70 and JeanX.OCount < 2:
                                $ JeanX.RecentActions.append("unsatisfied")
                                $ JeanX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jean_LP_After
                            $ Line = "came"

                    if JeanX.Lust >= 100:
                            #If Jean can cum
                            call Girl_Cumming(JeanX)
                            if Situation == "shift" or "angry" in JeanX.RecentActions:
                                jump Jean_LP_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in JeanX.RecentActions:#And Jean is unsatisfied,
                                    "[JeanX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Jean_LP_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if JeanX.SEXP >= 100 or ApprovalCheck(JeanX, 1200, "LO"):
            pass
        elif Cnt == (5 + JeanX.LickP):
                    $ JeanX.Brows = "confused"
                    ch_j "Isn't it just delicious?"
        elif JeanX.Lust >= 80:
                    pass
        elif Cnt == (15 + JeanX.LickP) and JeanX.SEXP >= 15 and not ApprovalCheck(JeanX, 1500):
                    $ JeanX.Brows = "confused"
                    menu:
                        ch_j "Maybe try something else?"
                        "Finish up.":
                                "You let go. . ."
                                jump Jean_LP_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Jean_LP_After
                        "No, this is fun.":
                                if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                                    $ JeanX.Statup("Love", 200, -5)
                                    $ JeanX.Statup("Obed", 50, 3)
                                    $ JeanX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ JeanX.FaceChange("angry", 1)
                                    call Jean_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_j "Well -I'm- bored."
                                    $ JeanX.Statup("Love", 50, -3, 1)
                                    $ JeanX.Statup("Love", 80, -4, 1)
                                    $ JeanX.Statup("Obed", 30, -1, 1)
                                    $ JeanX.Statup("Obed", 50, -1, 1)
                                    $ JeanX.RecentActions.append("angry")
                                    $ JeanX.DailyActions.append("angry")
                                    jump Jean_LP_After
        #End Count check

        call Escalation(JeanX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(JeanX,10) #"You might want to wrap this up, it's getting late."
        elif Round == 5:
                call Sex_Basic_Dialog(JeanX,5)   #"Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ JeanX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(JeanX,"done")   #"Ok, [Girl.Petname], that's enough of that for now."

label Jean_LP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Jean_Pos_Reset

    $ JeanX.FaceChange("sexy")

    $ JeanX.LickP += 1
    $ JeanX.Action -=1
    if JeanX.PantsNum() < 6 or JeanX.Upskirt:
        $ JeanX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ JeanX.Addictionrate += 1

    if Partner == "Rogue":
        call Partner_Like(JeanX,3,2)
    else:
        call Partner_Like(JeanX,2)

    if JeanX.LickP == 1:
            $ JeanX.SEXP += 10
            if not Situation:
                if JeanX.Love >= 500 and "unsatisfied" not in JeanX.RecentActions:
                    ch_j "You really put that tongue to work. . ."
                elif JeanX.Obed <= 500 and Player.Focus <= 20:
                    $ JeanX.FaceChange("perplexed", 1)
                    ch_j "I guess that wasn't so bad. . ."

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_j "Oh? What did you have in mind?"
    call Checkout
    return


# end JeanX.Lick Pussy /////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////Start Fondle Ass
label Jean_Fondle_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JeanX)
                                                                                     # Will she let you fondle? Modifiers
    if JeanX.FondleA: #You've done it before
        $ temp_modifier += 10
    if JeanX.PantsNum() >= 6 or JeanX.HoseNum() >= 5: # she's got pants on.
        $ temp_modifier -= 5
    if JeanX.Lust > 75: #She's really horny
        $ temp_modifier += 15
    if "exhibitionist" in JeanX.Traits:
        $ temp_modifier += Taboo
    if JeanX in Player.Harem or "sex friend" in JeanX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JeanX.Traits:
        $ temp_modifier -= 25
    if JeanX.ForcedCount and not JeanX.Forced:
        $ temp_modifier -= 5 * JeanX.ForcedCount

    if JeanX.Taboo and "tabno" in JeanX.DailyActions:
        $ temp_modifier -= 10
    if JeanX.Taboo and "public" not in JeanX.History:
        $ temp_modifier -= 20

    if "no fondle ass" in JeanX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no fondle ass" in JeanX.RecentActions else 0

    $ Approval = ApprovalCheck(JeanX, 850, TabM=1) # 85, 100, 115, Taboo -40(125)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ JeanX.FaceChange("surprised", 1)
            $ JeanX.Statup("Obed", 70, 2)
            $ JeanX.Statup("Inbt", 40, 2)
            "As your hand creeps down her backside, [JeanX.Name] shivers a bit, and then relaxes."
            $ JeanX.FaceChange("sexy")
            jump Jean_FA_Prep
        else:
            $ JeanX.FaceChange("surprised")
            $ JeanX.Statup("Obed", 50, -3)
            ch_j "Not so fast, [JeanX.Petname]. . ."
            $ JeanX.FaceChange("bemused")
            $ temp_modifier = 0
            $ Trigger2 = 0
            return

    if Situation == "pullback":
        $ JeanX.FaceChange("surprised")
        $ JeanX.Brows = "sad"
        if JeanX.Lust > 80:
            $ JeanX.Statup("Love", 70, -4)
        $ JeanX.Statup("Obed", 90, 1)
        $ JeanX.Statup("Obed", 70, 2)
        "As your finger slides out, [JeanX.Name] gasps and looks upset."
        jump Jean_FA_Prep
    elif "fondle ass" in JeanX.RecentActions:
        $ JeanX.FaceChange("sexy", 1)
        ch_j "Mmmm, again? I guess. . ."
        jump Jean_FA_Prep
    elif "fondle ass" in JeanX.DailyActions:
        $ JeanX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Mmm, you like that? . .",
            "Mmm. . ."])
        ch_j "[Line]"

    if Approval >= 2:                                                                   #She's into it. . .
        if JeanX.Forced:
            $ JeanX.FaceChange("sad")
            $ JeanX.Statup("Love", 70, -2, 1)
            $ JeanX.Statup("Obed", 90, 2)
            $ JeanX.Statup("Inbt", 60, 2)
            ch_j "If you insist. . ."
        else:
            $ JeanX.FaceChange("bemused, 1")
            ch_j "Yeah, ok. . ."
        $ JeanX.Statup("Lust", 200, 3)
        $ JeanX.Statup("Obed", 60, 1)
        $ JeanX.Statup("Inbt", 70, 1)
        jump Jean_FA_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ JeanX.FaceChange("angry", 1)
        if "no fondle ass" in JeanX.RecentActions:
            ch_j "I'm not used to repeating myself."
        elif JeanX.Taboo and "tabno" in JeanX.DailyActions and "no fondle ass" in JeanX.DailyActions:
            ch_j "I told you not to touch me like that in public!"
        elif "no fondle ass" in JeanX.DailyActions:
            ch_j "Don't ask me again today."
        elif JeanX.Taboo and "tabno" in JeanX.DailyActions:
            ch_j "I told you. . . not here, [JeanX.Petname]."
        elif not JeanX.FondleA:
            $ JeanX.FaceChange("bemused")
            ch_j "Not yet, [JeanX.Petname]. . ."
        else:
            $ JeanX.FaceChange("bemused")
            ch_j "Let's not, ok [JeanX.Petname]?"
        menu:
            extend ""
            "Sorry, never mind." if "no fondle ass" in JeanX.DailyActions:
                $ JeanX.FaceChange("bemused")
                ch_j "It's fine, I get it."
                return
            "Maybe later?" if "no fondle ass" not in JeanX.DailyActions:
                $ JeanX.FaceChange("sexy")
                ch_j ". . . I guess? Maybe."
                $ JeanX.Statup("Love", 80, 2)
                $ JeanX.Statup("Inbt", 50, 2)
                if JeanX.Taboo:
                    $ JeanX.RecentActions.append("tabno")
                    $ JeanX.DailyActions.append("tabno")
                $ JeanX.RecentActions.append("no fondle ass")
                $ JeanX.DailyActions.append("no fondle ass")
                return
            "Just one good squeeze?":
                if Approval:
                    $ JeanX.FaceChange("sexy")
                    $ JeanX.Statup("Obed", 90, 1)
                    $ JeanX.Statup("Obed", 50, 2)
                    ch_j "Oooh, beg for me. . ."
                    $ JeanX.Statup("Inbt", 70, 1)
                    $ JeanX.Statup("Inbt", 40, 2)
                    jump Jean_FA_Prep
                else:
                    $ JeanX.FaceChange("sexy")
                    ch_j "No."

            "[[Start fondling anyway]":                                               # Pressured into fondling.
                $ Approval = ApprovalCheck(JeanX, 250, "OI", TabM = 3) # 25, 40, 55, -120(145)
                if Approval > 1 or (Approval and JeanX.Forced):
                    $ JeanX.FaceChange("sad")
                    $ JeanX.Statup("Love", 70, -3, 1)
                    $ JeanX.Statup("Love", 200, -1)
                    ch_j ". . .whatever. . ."
                    $ JeanX.Statup("Obed", 50, 3)
                    $ JeanX.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ JeanX.Forced = 1
                    jump Jean_FA_Prep
                else:
                    $ JeanX.Statup("Love", 200, -10)
                    $ JeanX.FaceChange("angry", 1)
                    "She slaps your hand away."
                    $ JeanX.RecentActions.append("angry")
                    $ JeanX.DailyActions.append("angry")

    if "no fondle ass" in JeanX.DailyActions:
        ch_j "I don't want to have to go through this again."
        $ JeanX.RecentActions.append("angry")
        $ JeanX.DailyActions.append("angry")
    elif JeanX.Forced:
        $ JeanX.FaceChange("angry", 1)
        ch_j "Mmmm, no."
        $ JeanX.Statup("Lust", 60, 5)
        $ JeanX.Statup("Obed", 50, -2)
        $ JeanX.RecentActions.append("angry")
        $ JeanX.DailyActions.append("angry")
    elif JeanX.Taboo:
        $ JeanX.FaceChange("angry", 1)
        $ JeanX.RecentActions.append("tabno")
        $ JeanX.DailyActions.append("tabno")
        ch_j "I'm. . . not comfortable. . . in public. . ."
    elif JeanX.FondleA:
        $ JeanX.FaceChange("sad")
        ch_j "Sorry, keep your hands to yourself."
    else:
        $ JeanX.FaceChange("sexy")
        $ JeanX.Mouth = "sad"
        ch_j "No."
    $ JeanX.RecentActions.append("no fondle ass")
    $ JeanX.DailyActions.append("no fondle ass")
    $ temp_modifier = 0
    return

ch_j "Sorry, I don't even know how I got here. . ."
return

label Jean_FA_Prep: #Animation set-up
    if Trigger2 == "fondle ass":
        return
    if not JeanX.Forced and Situation != "auto":
        $ temp_modifier = 0
        call Bottoms_Off(JeanX)
        if "angry" in JeanX.RecentActions:
            return
    $ temp_modifier = 0
    call Jean_Pussy_Launch("fondle ass")
    if not JeanX.FondleA:
        if JeanX.Forced:
            $ JeanX.Statup("Love", 90, -20)
            $ JeanX.Statup("Obed", 70, 20)
            $ JeanX.Statup("Inbt", 80, 15)
        else:
            $ JeanX.Statup("Love", 90, 10)
            $ JeanX.Statup("Obed", 70, 12)
            $ JeanX.Statup("Inbt", 80, 20)
    if JeanX.Taboo:
        $ JeanX.Statup("Inbt", 200, (int(Taboo/10)))
        $ JeanX.Lust += int(Taboo/5)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if JeanX.Taboo:
        $ JeanX.DrainWord("tabno")
    $ JeanX.DrainWord("no fondle ass")
    $ JeanX.RecentActions.append("fondle ass")
    $ JeanX.DailyActions.append("fondle ass")
    call Jean_Pussy_Launch("fondle ass")

label Jean_FA_Cycle: #Repeating strokes
    while Round > 0:
        call ViewShift(JeanX,JeanX.Pose,0,"fondle ass")
        call Shift_Focus(JeanX)
        $ JeanX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(JeanX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Jean_FA_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0
                        "View":
                                    call ViewShift(JeanX,"menu")
                                    jump Jean_FA_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if JeanX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ JeanX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Shift primary action":
                                            if JeanX.Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in.":
                                                                $ Situation = "shift"
                                                                call Jean_FA_After
                                                                call Jean_Insert_Ass
                                                        "Just stick a finger in without asking.":
                                                                $ Situation = "auto"
                                                                call Jean_FA_After
                                                                call Jean_Insert_Ass
                                                        "I want to lick your asshole.":
                                                                $ Situation = "shift"
                                                                call Jean_FA_After
                                                                call Jean_Lick_Ass
                                                        "Just start licking.":
                                                                $ Situation = "auto"
                                                                call Jean_FA_After
                                                                call Jean_Lick_Ass
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Jean_FA_After
                                                                call Jean_Dildo_Ass
                                                        "Never Mind":
                                                                jump Jean_FA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Jean_FA_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [JeanX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(JeanX)
                                            "Ask [JeanX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(JeanX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(JeanX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jean_FA_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jean_FA_Cycle
                                            "Never mind":
                                                        jump Jean_FA_Cycle

                                    "Show her feet" if not ShowFeet and (JeanX.Pose == "doggy" or JeanX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (JeanX.Pose == "doggy" or JeanX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [JeanX.Name]":
                                            call Girl_Undress(JeanX)
                                    "Clean up [JeanX.Name] (locked)" if not JeanX.Spunk:
                                            pass
                                    "Clean up [JeanX.Name]" if JeanX.Spunk:
                                            call Girl_Cleanup(JeanX,"ask")
                                    "Never mind":
                                            jump Jean_FA_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Jean_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Jean_FA_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Jean_Pos_Reset
                                    $ Line = 0
                                    jump Jean_FA_After
        #End menu (if Line)

        if JeanX.Panties or JeanX.PantsNum() >= 6 or JeanX.HoseNum() >= 5: #This checks if Jean wants to strip down.
                call Girl_Undress(JeanX,"auto")

        call Shift_Focus(JeanX)
        call Sex_Dialog(JeanX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JeanX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JeanX)
                            if "angry" in JeanX.RecentActions:
                                call Jean_Pos_Reset
                                return
                            $ JeanX.Statup("Lust", 200, 5)
                            if 100 > JeanX.Lust >= 70 and JeanX.OCount < 2 and JeanX.SEXP >= 20:
                                $ JeanX.RecentActions.append("unsatisfied")
                                $ JeanX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jean_FA_After
                            $ Line = "came"

                    if JeanX.Lust >= 100:
                            #If Jean can cum
                            call Girl_Cumming(JeanX)
                            if Situation == "shift" or "angry" in JeanX.RecentActions:
                                jump Jean_FA_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in JeanX.RecentActions:#And Jean is unsatisfied,
                                    "[JeanX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Jean_FA_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if JeanX.SEXP >= 100 or ApprovalCheck(JeanX, 1200, "LO"):
            pass
        elif Cnt == (5 + JeanX.FondleA):
                    $ JeanX.Brows = "confused"
                    ch_j "Mmmm. . ."
        elif JeanX.Lust >= 80:
                    pass
        elif Cnt == (15 + JeanX.FondleA) and JeanX.SEXP >= 15 and not ApprovalCheck(JeanX, 1500):
                    $ JeanX.Brows = "confused"
                    menu:
                        ch_j "Maybe try something else?"
                        "Finish up.":
                                "You let go. . ."
                                jump Jean_FA_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Jean_FA_After
                        "No, this is fun.":
                                if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                                    $ JeanX.Statup("Love", 200, -5)
                                    $ JeanX.Statup("Obed", 50, 3)
                                    $ JeanX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ JeanX.FaceChange("angry", 1)
                                    call Jean_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_j "Well -I'm- bored."
                                    $ JeanX.Statup("Love", 50, -3, 1)
                                    $ JeanX.Statup("Love", 80, -4, 1)
                                    $ JeanX.Statup("Obed", 30, -1, 1)
                                    $ JeanX.Statup("Obed", 50, -1, 1)
                                    $ JeanX.RecentActions.append("angry")
                                    $ JeanX.DailyActions.append("angry")
                                    jump Jean_FA_After
        #End Count check

        call Escalation(JeanX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(JeanX,10) #"You might want to wrap this up, it's getting late."
        elif Round == 5:
                call Sex_Basic_Dialog(JeanX,5)   #"Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ JeanX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(JeanX,"done")   #"Ok, [Girl.Petname], that's enough of that for now."

label Jean_FA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Jean_Pos_Reset

    $ JeanX.FaceChange("sexy")

    $ JeanX.FondleA += 1
    $ JeanX.Action -=1
    if JeanX.PantsNum() < 6 or JeanX.Upskirt:
        $ JeanX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ JeanX.Addictionrate += 1

        call Partner_Like(JeanX,2)

    if JeanX.FondleA == 1:
            $ JeanX.SEXP += 4
            if not Situation:
                if JeanX.Love >= 500 and "unsatisfied" not in JeanX.RecentActions:
                    ch_j "That was. . . nice. . ."
                elif JeanX.Obed <= 500 and Player.Focus <= 20:
                    $ JeanX.FaceChange("perplexed", 1)
                    ch_j "I bet you enjoyed that."

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_j "Oh? What did you have in mind?"
    call Checkout
    return


# end JeanX.Fondle Ass /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Ass
label Jean_Insert_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JeanX)

    if JeanX.InsertA: #You've done it before
        $ temp_modifier += 25
    if JeanX.PantsNum() >= 6 or JeanX.HoseNum() >= 5: # she's got pants on.
        $ temp_modifier -= 15
    if JeanX.Lust > 85: #She's really horny
        $ temp_modifier += 15
    if JeanX.Lust > 95:
        $ temp_modifier += 5
    if Situation == "shift":
        $ temp_modifier += 10
    if JeanX.Lust > 85 and Situation == "auto": #She's really horny
        $ temp_modifier += 10
    if "exhibitionist" in JeanX.Traits:
        $ temp_modifier += (4*JeanX.Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JeanX.Traits:
        $ temp_modifier -= 25
    if JeanX.ForcedCount and not JeanX.Forced:
        $ temp_modifier -= 5 * JeanX.ForcedCount

    if JeanX.Taboo and "tabno" in JeanX.DailyActions:
        $ temp_modifier -= 10
    if JeanX.Taboo and "public" not in JeanX.History:
        $ temp_modifier -= 20

    if "no insert ass" in JeanX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no insert ass" in JeanX.RecentActions else 0

    $ Approval = ApprovalCheck(JeanX, 1300, TabM = 3) # 130, 145, 160, Taboo -120(250)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ JeanX.FaceChange("surprised")
            $ JeanX.Statup("Obed", 90, 2)
            $ JeanX.Statup("Obed", 70, 2)
            $ JeanX.Statup("Inbt", 80, 2)
            $ JeanX.Statup("Inbt", 30, 2)
            "As you slide a finger in, [JeanX.Name] tightens around it in surprise, but seems into it."
            $ JeanX.FaceChange("sexy")
            jump Jean_IA_Prep
        else:
            $ JeanX.FaceChange("surprised")
            $ JeanX.Statup("Love", 80, -2)
            $ JeanX.Statup("Obed", 50, -3)
            ch_j "Ooo! Not right now, [JeanX.Petname]."
            $ temp_modifier = 0
            $ Trigger2 = 0
            return

    if "insert ass" in JeanX.DailyActions:
        $ JeanX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Chill. . .",
            "Mmm. . ."])
        ch_j "[Line]"

    if Approval >= 2:                                                                   #She's into it. . .
        if JeanX.Forced:
            $ JeanX.FaceChange("sad")
            $ JeanX.Statup("Love", 70, -3, 1)
            $ JeanX.Statup("Love", 20, -2, 1)
            $ JeanX.Statup("Obed", 90, 1)
            $ JeanX.Statup("Inbt", 60, 1)
            ch_j "If you must. . ."
        else:
            $ JeanX.FaceChange("sexy", 1)
            $ JeanX.Eyes = "closed"
            $ JeanX.Statup("Love", 90, 1)
            $ JeanX.Statup("Inbt", 50, 3)
            $ JeanX.Statup("Lust", 200, 3)
            ch_j "Mmmmm. . ."
        $ JeanX.Statup("Obed", 20, 1)
        $ JeanX.Statup("Obed", 60, 1)
        $ JeanX.Statup("Inbt", 70, 2)
        jump Jean_IA_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ JeanX.FaceChange("angry", 1)
        if "no insert ass" in JeanX.RecentActions:
            ch_j "I'm not used to repeating myself."
        elif JeanX.Taboo and "tabno" in JeanX.DailyActions and "no insert ass" in JeanX.DailyActions:
            ch_j "I told you that wasn't appropriate!"
        elif "no insert ass" in JeanX.DailyActions:
            ch_j "Don't ask me again today."
        elif JeanX.Taboo and "tabno" in JeanX.DailyActions:
            ch_j "I told you. . . not here, [JeanX.Petname]."
        elif not JeanX.InsertA:
            $ JeanX.FaceChange("perplexed", 1)
            ch_j "That's really not my style. . ."
        else:
            $ JeanX.FaceChange("bemused")
            ch_j "I'd rather not today. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no insert ass" in JeanX.DailyActions:
                $ JeanX.FaceChange("bemused")
                ch_j "It's fine, I get it."
                return
            "Maybe later?" if "no insert ass" not in JeanX.DailyActions:
                $ JeanX.FaceChange("sexy")
                ch_j ". . . I guess? Maybe."
                $ JeanX.Statup("Love", 80, 2)
                $ JeanX.Statup("Inbt", 70, 2)
                if JeanX.Taboo:
                    $ JeanX.RecentActions.append("tabno")
                    $ JeanX.DailyActions.append("tabno")
                $ JeanX.RecentActions.append("no insert ass")
                $ JeanX.DailyActions.append("no insert ass")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ JeanX.FaceChange("sexy")
                    $ JeanX.Statup("Obed", 90, 2)
                    $ JeanX.Statup("Obed", 50, 2)
                    ch_j "You're probably right. . ."
                    $ JeanX.Statup("Inbt", 70, 3)
                    $ JeanX.Statup("Inbt", 40, 2)
                    jump Jean_IA_Prep
                else:
                    $ JeanX.FaceChange("bemused")
                    ch_j "I don't think that I would."

            "[[Slide a finger in anyway]":                                               # Pressured into being fingered.
                $ Approval = ApprovalCheck(JeanX, 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                if Approval > 1 or (Approval and JeanX.Forced):
                    $ JeanX.FaceChange("surprised", 1)
                    $ JeanX.Statup("Love", 70, -5, 1)
                    $ JeanX.Statup("Love", 200, -2)
                    ch_j "Ooo! Well ok then. . ."
                    $ JeanX.FaceChange("sad")
                    $ JeanX.Statup("Obed", 50, 4)
                    $ JeanX.Statup("Inbt", 80, 1)
                    $ JeanX.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ JeanX.Forced = 1
                    jump Jean_IA_Prep
                else:
                    $ JeanX.Statup("Love", 200, -15)
                    $ JeanX.FaceChange("angry", 1)
                    "She slaps your hand away."
                    $ JeanX.RecentActions.append("angry")
                    $ JeanX.DailyActions.append("angry")

    if "no insert ass" in JeanX.DailyActions:
        ch_j "I don't want to have to go through this again."
        $ JeanX.RecentActions.append("angry")
        $ JeanX.DailyActions.append("angry")
    elif JeanX.Forced:
        $ JeanX.FaceChange("angry", 1)
        ch_j "I'm not going there today."
        if ApprovalCheck(JeanX, 500, "I"):
                $ JeanX.Statup("Lust", 80, 10)
        else:
                $ JeanX.Statup("Lust", 50, 3)
        $ JeanX.Statup("Obed", 50, -2)
        $ JeanX.RecentActions.append("angry")
        $ JeanX.DailyActions.append("angry")
    elif JeanX.Taboo:
        $ JeanX.FaceChange("angry", 1)
        $ JeanX.RecentActions.append("tabno")
        $ JeanX.DailyActions.append("tabno")
        ch_j "I'm. . . not comfortable. . . in public. . ."
    elif JeanX.InsertA:
        $ JeanX.FaceChange("sad")
        ch_j "I don't feel like it."
    else:
        $ JeanX.FaceChange("surprised")
        ch_j "Not today, [JeanX.Petname]."
        $ JeanX.FaceChange()
    $ JeanX.RecentActions.append("no insert ass")
    $ JeanX.DailyActions.append("no insert ass")
    $ temp_modifier = 0
    return


label Jean_IA_Prep: #Animation set-up
    if Trigger2 == "insert ass":
        return

    call Jean_Pussy_Launch("insert ass")

    if Situation == JeanX:
            #Jean auto-starts
            $ Situation = 0
            if (JeanX.Legs and not JeanX.Upskirt) or (JeanX.Panties and not JeanX.PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck(JeanX, 1250, TabM = 1) or (JeanX.SeenPussy and ApprovalCheck(JeanX, 500) and not JeanX.Taboo):
                        $ JeanX.Upskirt = 1
                        $ JeanX.PantiesDown = 1
                        $ Line = 0
                        if JeanX.PantsNum() == 5:
                            $ Line = JeanX.Name + " hikes up her skirt"
                        elif JeanX.PantsNum() >= 6:
                            $ Line = JeanX.Name + " pulls down her " + JeanX.Legs
                        else:
                            $ Line = 0
                        if JeanX.Panties:
                            if Line:
                                #wearing pants
                                "[Line] and pulls her [JeanX.Panties] out of the way."
                                "She then grabs your arm and rubs your hand against her asshole, clearly intending you to get to work."
                            else:
                                #no pants
                                "She pulls her [JeanX.Panties] out of the way, and then rubs your hand against her asshole."
                                "She clearly intends for you to get to work."
                        else:
                            #pants but no panties
                            "[Line], and then rubs your hand against her asshole."
                            "She clearly intends for you to get to work."
                        call Jean_First_Bottomless(1)
                else:
                        "[JeanX.Name] grabs your arm and rubs your hand against her asshole, clearly intending you to get to work."
            else:
                        "[JeanX.Name] grabs your arm and rubs your hand against her asshole, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":
                    $ JeanX.Statup("Inbt", 80, 3)
                    $ JeanX.Statup("Inbt", 50, 2)
                    "You press your finger into it."
                "Praise her.":
                    $ JeanX.FaceChange("sexy", 1)
                    $ JeanX.Statup("Inbt", 80, 3)
                    ch_p "Dirty girl, [JeanX.Pet]."
                    $ JeanX.NameCheck() #checks reaction to petname
                    "You press your finger into it."
                    $ JeanX.Statup("Love", 85, 1)
                    $ JeanX.Statup("Obed", 90, 1)
                    $ JeanX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your hand back."
                    $ JeanX.FaceChange("surprised")
                    $ JeanX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that right now, [JeanX.Pet]."
                    $ JeanX.NameCheck() #checks reaction to petname
                    $ JeanX.Statup("Love", 70, -2)
                    "[JeanX.Name] pulls back."
                    $ JeanX.Statup("Obed", 90, 1)
                    $ JeanX.Statup("Obed", 50, 1)
                    $ JeanX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ JeanX.AddWord(1,"refused","refused")
                    return
            #end auto

    if not JeanX.Forced and Situation != "auto":
        $ temp_modifier = 0
        call Bottoms_Off(JeanX)
        if "angry" in JeanX.RecentActions:
            return

    $ temp_modifier = 0
    if not JeanX.InsertA:
        if JeanX.Forced:
            $ JeanX.Statup("Love", 90, -50)
            $ JeanX.Statup("Obed", 70, 60)
            $ JeanX.Statup("Inbt", 80, 35)
        else:
            $ JeanX.Statup("Love", 90, 10)
            $ JeanX.Statup("Obed", 70, 20)
            $ JeanX.Statup("Inbt", 80, 25)

    if JeanX.Taboo:
        $ JeanX.Statup("Inbt", 200, (int(Taboo/10)))
        $ JeanX.Lust += int(Taboo/5)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if JeanX.Taboo:
        $ JeanX.DrainWord("tabno")
    $ JeanX.DrainWord("no insert ass")
    $ JeanX.RecentActions.append("insert ass")
    $ JeanX.DailyActions.append("insert ass")
    call Jean_Pussy_Launch("insert ass")

label Jean_IA_Cycle: #Repeating strokes
    while Round > 0:
        call ViewShift(JeanX,JeanX.Pose,0,"insert ass")
        call Shift_Focus(JeanX)
        $ JeanX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(JeanX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Jean_IA_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0
                        "View":
                                    call ViewShift(JeanX,"menu")
                                    jump Jean_IA_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if JeanX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ JeanX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Shift primary action":
                                            if JeanX.Action and MultiAction:
                                                    menu:
                                                        "Pull out and start rubbing again.":
                                                                $ Situation = "pullback"
                                                                call Jean_IA_After
                                                                call Jean_Fondle_Ass
                                                        "I want to lick your asshole.":
                                                                $ Situation = "shift"
                                                                call Jean_IA_After
                                                                call Jean_Lick_Ass
                                                        "Just start licking.":
                                                                $ Situation = "auto"
                                                                call Jean_IA_After
                                                                call Jean_Lick_Ass
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Jean_IA_After
                                                                call Jean_Dildo_Ass
                                                        "Never Mind":
                                                                jump Jean_IA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Jean_IA_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [JeanX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(JeanX)
                                            "Ask [JeanX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(JeanX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(JeanX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jean_IA_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jean_IA_Cycle
                                            "Never mind":
                                                        jump Jean_IA_Cycle

                                    "Show her feet" if not ShowFeet and (JeanX.Pose == "doggy" or JeanX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (JeanX.Pose == "doggy" or JeanX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [JeanX.Name]":
                                            call Girl_Undress(JeanX)
                                    "Clean up [JeanX.Name] (locked)" if not JeanX.Spunk:
                                            pass
                                    "Clean up [JeanX.Name]" if JeanX.Spunk:
                                            call Girl_Cleanup(JeanX,"ask")
                                    "Never mind":
                                            jump Jean_IA_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Jean_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Jean_IA_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Jean_Pos_Reset
                                    $ Line = 0
                                    jump Jean_IA_After
        #End menu (if Line)

        if JeanX.Panties or JeanX.PantsNum() >= 6 or JeanX.HoseNum() >= 5: #This checks if Jean wants to strip down.
                call Girl_Undress(JeanX,"auto")

        call Shift_Focus(JeanX)
        call Sex_Dialog(JeanX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JeanX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JeanX)
                            if "angry" in JeanX.RecentActions:
                                call Jean_Pos_Reset
                                return
                            $ JeanX.Statup("Lust", 200, 5)
                            if 100 > JeanX.Lust >= 70 and JeanX.OCount < 2:
                                $ JeanX.RecentActions.append("unsatisfied")
                                $ JeanX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jean_IA_After
                            $ Line = "came"

                    if JeanX.Lust >= 100:
                            #If Jean can cum
                            call Girl_Cumming(JeanX)
                            if Situation == "shift" or "angry" in JeanX.RecentActions:
                                jump Jean_IA_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in JeanX.RecentActions:#And Jean is unsatisfied,
                                    "[JeanX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Jean_IA_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if JeanX.SEXP >= 100 or ApprovalCheck(JeanX, 1200, "LO"):
            pass
        elif Cnt == (5 + JeanX.InsertA):
                    $ JeanX.Brows = "confused"
                    ch_j "Ungh, you're really getting in there. . ."
        elif JeanX.Lust >= 80:
                    pass
        elif Cnt == (15 + JeanX.InsertA) and JeanX.SEXP >= 15 and not ApprovalCheck(JeanX, 1500):
                    $ JeanX.Brows = "confused"
                    menu:
                        ch_j "Maybe try something else?"
                        "Finish up.":
                                "You let go. . ."
                                jump Jean_IA_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Jean_IA_After
                        "No, this is fun.":
                                if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                                    $ JeanX.Statup("Love", 200, -5)
                                    $ JeanX.Statup("Obed", 50, 3)
                                    $ JeanX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ JeanX.FaceChange("angry", 1)
                                    call Jean_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_j "Well -I'm- bored."
                                    $ JeanX.Statup("Love", 50, -3, 1)
                                    $ JeanX.Statup("Love", 80, -4, 1)
                                    $ JeanX.Statup("Obed", 30, -1, 1)
                                    $ JeanX.Statup("Obed", 50, -1, 1)
                                    $ JeanX.RecentActions.append("angry")
                                    $ JeanX.DailyActions.append("angry")
                                    jump Jean_IA_After
        #End Count check

        call Escalation(JeanX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(JeanX,10) #"You might want to wrap this up, it's getting late."
        elif Round == 5:
                call Sex_Basic_Dialog(JeanX,5)   #"Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ JeanX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(JeanX,"done")   #"Ok, [Girl.Petname], that's enough of that for now."

label Jean_IA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Jean_Pos_Reset

    $ JeanX.FaceChange("sexy")

    $ JeanX.InsertA += 1
    $ JeanX.Action -=1
    $ JeanX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ JeanX.Addictionrate += 1

    call Partner_Like(JeanX,2)

    if JeanX.InsertA == 1:
            $ JeanX.SEXP += 12
            if not Situation:
                if JeanX.Love >= 500 and "unsatisfied" not in JeanX.RecentActions:
                    ch_j "That was. . . interesting. . ."
                elif JeanX.Obed <= 500 and Player.Focus <= 20:
                    $ JeanX.FaceChange("perplexed", 1)
                    ch_j "I bet you enjoyed that."

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_j "Oh? What did you have in mind?"
    call Checkout
    return


# end JeanX.Insert Ass /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Ass
label Jean_Lick_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JeanX)
                                                                             # Will she let you lick? Modifiers
    if JeanX.LickA: #You've done it before
        $ temp_modifier += 20
    if JeanX.PantsNum() >= 6 or JeanX.HoseNum() >= 5: # she's got pants on.
        $ temp_modifier -= 25
    if JeanX.Lust > 95:
        $ temp_modifier += 20
    elif JeanX.Lust > 85: #She's really horny
        $ temp_modifier += 15
    if JeanX.Lust > 85 and Situation == "auto": #auto
        $ temp_modifier += 10
    if Situation == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in JeanX.Traits:
        $ temp_modifier += (4*JeanX.Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JeanX.Traits:
        $ temp_modifier -= 25
    if JeanX.ForcedCount and not JeanX.Forced:
        $ temp_modifier -= 5 * JeanX.ForcedCount

    if JeanX.Taboo and "tabno" in JeanX.DailyActions:
        $ temp_modifier -= 10
    if JeanX.Taboo and "public" not in JeanX.History:
        $ temp_modifier -= 20

    if "no lick ass" in JeanX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no lick ass" in JeanX.RecentActions else 0

    $ Approval = ApprovalCheck(JeanX, 1550, TabM = 4) # 155, 170, 185, Taboo -160(315)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ JeanX.FaceChange("surprised")
            $ JeanX.Statup("Obed", 90, 1)
            $ JeanX.Statup("Inbt", 80, 3)
            $ JeanX.Statup("Inbt", 40, 2)
            "As you crouch down and start to lick her asshole, [JeanX.Name] startles briefly, but then begins to melt."
            $ JeanX.FaceChange("sexy")
            jump Jean_LA_Prep
        else:
            $ JeanX.FaceChange("surprised")
            $ JeanX.Statup("Love", 80, -2)
            $ JeanX.Statup("Obed", 50, -3)
            ch_j "Whoa there, [JeanX.Petname]!"
            $ temp_modifier = 0
            $ Trigger2 = 0
            return

    if "lick ass" in JeanX.RecentActions:
        $ JeanX.FaceChange("sexy", 1)
        ch_j "Mmmm, again? I guess. . ."
        jump Jean_LA_Prep
    elif "lick ass" in JeanX.DailyActions:
        $ JeanX.FaceChange("sexy", 1)
        ch_j "You didn't get enough earlier?"


    if Approval >= 2:                                                                   #She's into it. . .
        if JeanX.Forced:
            $ JeanX.FaceChange("sad")
            $ JeanX.Statup("Love", 70, -3, 1)
            $ JeanX.Statup("Love", 20, -2, 1)
            $ JeanX.Statup("Obed", 90, 2)
            $ JeanX.Statup("Inbt", 60, 2)
            ch_j "Whatever. . ."
        else:
            $ JeanX.FaceChange("sexy", 1)
            $ JeanX.Eyes = "closed"
            $ JeanX.Statup("Love", 90, 1)
            $ JeanX.Statup("Inbt", 60, 2)
            $ JeanX.Statup("Lust", 200, 3)
            ch_j "Mmm. . . naughty."
        $ JeanX.Statup("Obed", 20, 1)
        $ JeanX.Statup("Obed", 60, 1)
        $ JeanX.Statup("Inbt", 80, 2)
        jump Jean_LA_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ JeanX.FaceChange("angry", 1)
        if "no lick ass" in JeanX.RecentActions:
            ch_j "I'm not used to repeating myself."
        elif JeanX.Taboo and "tabno" in JeanX.DailyActions and "no lick ass" in JeanX.DailyActions:
            ch_j "I told you not to touch me like that in public!"
        elif "no lick ass" in JeanX.DailyActions:
            ch_j "Don't ask me again today."
        elif JeanX.Taboo and "tabno" in JeanX.DailyActions:
            ch_j "I told you. . . not here, [JeanX.Petname]."
        elif not JeanX.LickA:                    #First time dialog
            $ JeanX.FaceChange("bemused", 1)
            if JeanX.Love >= JeanX.Obed and JeanX.Love >= (JeanX.Inbt - JeanX.IX):
                ch_j "Oh, we're there now?"
            elif JeanX.Obed >= (JeanX.Inbt - JeanX.IX):
                ch_j "Is that what gets you off?"
            else:
                $ JeanX.Eyes = "sexy"
                ch_j "Mmmm, you're into that?"
        else:
            $ JeanX.FaceChange("bemused")
            ch_j "Not now, [JeanX.Petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no lick ass" in JeanX.DailyActions:
                $ JeanX.FaceChange("bemused")
                ch_j "It's fine, I get it."
                return
            "I'm sure I can convince you later. . ." if "no lick ass" not in JeanX.DailyActions:
                $ JeanX.FaceChange("sexy")
                ch_j ". . . I guess? Maybe."
                $ JeanX.Statup("Love", 80, 2)
                $ JeanX.Statup("Inbt", 70, 2)
                if JeanX.Taboo:
                    $ JeanX.RecentActions.append("tabno")
                    $ JeanX.DailyActions.append("tabno")
                $ JeanX.RecentActions.append("no lick ass")
                $ JeanX.DailyActions.append("no lick ass")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ JeanX.FaceChange("sexy")
                    $ JeanX.Statup("Obed", 90, 2)
                    $ JeanX.Statup("Obed", 50, 2)
                    ch_j "Ok, you're probably right. . ."
                    $ JeanX.Statup("Inbt", 70, 3)
                    $ JeanX.Statup("Inbt", 40, 2)
                    jump Jean_LA_Prep
                else:
                    $ JeanX.FaceChange("sexy")
                    ch_j "I really don't think so."

            "[[Start licking anyway]":                                               # Pressured into being licked.
                $ Approval = ApprovalCheck(JeanX, 1100, "OI", TabM = 4) # 110, 125, 140, -160(270)
                if Approval > 1 or (Approval and JeanX.Forced):
                    $ JeanX.FaceChange("sad")
                    $ JeanX.Statup("Love", 70, -5, 1)
                    $ JeanX.Statup("Love", 200, -2)
                    ch_j ". . .whatever. . ."
                    $ JeanX.Statup("Obed", 50, 4)
                    $ JeanX.Statup("Inbt", 80, 1)
                    $ JeanX.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ JeanX.Forced = 1
                    jump Jean_LA_Prep
                else:
                    $ JeanX.Statup("Love", 200, -15)
                    $ JeanX.FaceChange("angry", 1)
                    "She shoves your head back."
                    $ JeanX.RecentActions.append("angry")
                    $ JeanX.DailyActions.append("angry")

    if "no lick ass" in JeanX.DailyActions:
        ch_j "I don't want to have to go through this again."
        $ JeanX.RecentActions.append("angry")
        $ JeanX.DailyActions.append("angry")
    elif JeanX.Forced:
        $ JeanX.FaceChange("angry", 1)
        ch_j "I don't think so."
        if ApprovalCheck(JeanX, 500, "I"):
                $ JeanX.Statup("Lust", 80, 10)
        else:
                $ JeanX.Statup("Lust", 50, 3)
        $ JeanX.Statup("Obed", 50, -2)
        $ JeanX.RecentActions.append("angry")
        $ JeanX.DailyActions.append("angry")
    elif JeanX.Taboo:
        $ JeanX.FaceChange("angry", 1)
        $ JeanX.RecentActions.append("tabno")
        $ JeanX.DailyActions.append("tabno")
        ch_j "I'm. . . not comfortable. . . in public. . ."
    elif JeanX.LickA:
        $ JeanX.FaceChange("sad")
        ch_j "We've had enough of that."
    else:
        $ JeanX.FaceChange("surprised")
        ch_j "I'm sorry, not now."
        $ JeanX.FaceChange()
    $ JeanX.RecentActions.append("no lick ass")
    $ JeanX.DailyActions.append("no lick ass")
    $ temp_modifier = 0
    return

label Jean_LA_Prep: #Animation set-up
    if Trigger2 == "lick ass":
        return
    if not JeanX.Forced and Situation != "auto":
        $ temp_modifier = 0
        if JeanX.PantsNum() >= 6:
            $ temp_modifier = 15
        call Bottoms_Off(JeanX)
        if "angry" in JeanX.RecentActions:
            return
    $ temp_modifier = 0
    call Jean_Pussy_Launch("lick ass")
    if not JeanX.LickA:
        if JeanX.Forced:
            $ JeanX.Statup("Love", 90, -30)
            $ JeanX.Statup("Obed", 70, 40)
            $ JeanX.Statup("Inbt", 80, 80)
        else:
            $ JeanX.Statup("Love", 90, 35)
            $ JeanX.Statup("Obed", 70, 25)
            $ JeanX.Statup("Inbt", 80, 55)
    if JeanX.Taboo:
        $ JeanX.Statup("Inbt", 200, (int(Taboo/10)))
        $ JeanX.Lust += int(Taboo/5)
    if Situation:
        $ renpy.pop_call()
        $ Situation = 0

    $ JeanX.Upskirt = 1
    if JeanX.PantsNum() == 5:
        $ JeanX.SeenPanties = 1
    if not JeanX.Panties:
        call Jean_First_Bottomless(1)
    $ Line = 0
    $ Cnt = 0
    if JeanX.Taboo:
        $ JeanX.DrainWord("tabno")
    $ JeanX.DrainWord("no lick ass")

    $ JeanX.RecentActions.append("lick") if "lick" not in JeanX.RecentActions else JeanX.RecentActions
    $ JeanX.RecentActions.append("ass") if "ass" not in JeanX.RecentActions else JeanX.RecentActions
    $ JeanX.RecentActions.append("lick ass")

    $ JeanX.DailyActions.append("lick") if "lick" not in JeanX.DailyActions else JeanX.RecentActions
    $ JeanX.DailyActions.append("ass") if "ass" not in JeanX.DailyActions else JeanX.RecentActions
    $ JeanX.DailyActions.append("lick ass")
    call Jean_Pussy_Launch("lick ass")

label Jean_LA_Cycle: #Repeating strokes
    if Trigger2 == "kiss you":
            $ Trigger2 = 0
    while Round > 0:
        call ViewShift(JeanX,JeanX.Pose,0,"lick ass")
        call Shift_Focus(JeanX)
        $ JeanX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(JeanX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Jean_LA_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0
                        "View":
                                    call ViewShift(JeanX,"menu")
                                    jump Jean_LA_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if JeanX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ JeanX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Shift primary action":
                                            if JeanX.Action and MultiAction:
                                                    menu:
                                                        "Switch to fondling.":
                                                                $ Situation = "pullback"
                                                                call Jean_LA_After
                                                                call Jean_Fondle_Ass
                                                        "I want to stick a finger in.":
                                                                $ Situation = "shift"
                                                                call Jean_LA_After
                                                                call Jean_Insert_Ass
                                                        "Just stick a finger in [[without asking].":
                                                                $ Situation = "auto"
                                                                call Jean_LA_After
                                                                call Jean_Insert_Ass
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Jean_LA_After
                                                                call Jean_Dildo_Ass
                                                        "Never Mind":
                                                                jump Jean_LA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Jean_LA_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [JeanX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(JeanX)
                                            "Ask [JeanX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(JeanX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(JeanX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jean_LA_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jean_LA_Cycle
                                            "Never mind":
                                                        jump Jean_LA_Cycle

                                    "Show her feet" if not ShowFeet and (JeanX.Pose == "doggy" or JeanX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (JeanX.Pose == "doggy" or JeanX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [JeanX.Name]":
                                            call Girl_Undress(JeanX)
                                    "Clean up [JeanX.Name] (locked)" if not JeanX.Spunk:
                                            pass
                                    "Clean up [JeanX.Name]" if JeanX.Spunk:
                                            call Girl_Cleanup(JeanX,"ask")
                                    "Never mind":
                                            jump Jean_LA_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Jean_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Jean_LA_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Jean_Pos_Reset
                                    $ Line = 0
                                    jump Jean_LA_After
        #End menu (if Line)

        if JeanX.Panties or JeanX.PantsNum() >= 6 or JeanX.HoseNum() >= 5: #This checks if Jean wants to strip down.
                call Girl_Undress(JeanX,"auto")

        call Shift_Focus(JeanX)
        call Sex_Dialog(JeanX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JeanX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JeanX)
                            if "angry" in JeanX.RecentActions:
                                call Jean_Pos_Reset
                                return
                            $ JeanX.Statup("Lust", 200, 5)
                            if 100 > JeanX.Lust >= 70 and JeanX.OCount < 2:
                                $ JeanX.RecentActions.append("unsatisfied")
                                $ JeanX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jean_LA_After
                            $ Line = "came"

                    if JeanX.Lust >= 100:
                            #If Jean can cum
                            call Girl_Cumming(JeanX)
                            if Situation == "shift" or "angry" in JeanX.RecentActions:
                                jump Jean_LA_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in JeanX.RecentActions:#And Jean is unsatisfied,
                                    "[JeanX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Jean_LA_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if JeanX.SEXP >= 100 or ApprovalCheck(JeanX, 1200, "LO"):
            pass
        elif Cnt == (5 + JeanX.LickA):
                    $ JeanX.Brows = "confused"
                    ch_j "You seem to be enjoying yourself. . ."
        elif JeanX.Lust >= 80:
                    pass
        elif Cnt == (15 + JeanX.LickA) and JeanX.SEXP >= 15 and not ApprovalCheck(JeanX, 1500):
                    $ JeanX.Brows = "confused"
                    menu:
                        ch_j "[JeanX.Petname], could we try something different?"
                        "Finish up.":
                                "You let go. . ."
                                jump Jean_LA_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Jean_LA_After
                        "No, this is fun.":
                                if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                                    $ JeanX.Statup("Love", 200, -5)
                                    $ JeanX.Statup("Obed", 50, 3)
                                    $ JeanX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ JeanX.FaceChange("angry", 1)
                                    call Jean_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_j "Well -I'm- bored."
                                    $ JeanX.Statup("Love", 50, -3, 1)
                                    $ JeanX.Statup("Love", 80, -4, 1)
                                    $ JeanX.Statup("Obed", 30, -1, 1)
                                    $ JeanX.Statup("Obed", 50, -1, 1)
                                    $ JeanX.RecentActions.append("angry")
                                    $ JeanX.DailyActions.append("angry")
                                    jump Jean_LA_After
        #End Count check

        call Escalation(JeanX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(JeanX,10) #"You might want to wrap this up, it's getting late."
        elif Round == 5:
                call Sex_Basic_Dialog(JeanX,5)   #"Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ JeanX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(JeanX,"done")   #"Ok, [Girl.Petname], that's enough of that for now."

label Jean_LA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Jean_Pos_Reset

    $ JeanX.FaceChange("sexy")

    $ JeanX.LickA += 1
    $ JeanX.Action -=1
    if JeanX.PantsNum() < 6 or JeanX.Upskirt:
        $ JeanX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ JeanX.Addictionrate += 1

    call Partner_Like(JeanX,2)

    if JeanX.LickA == 1:
            $ JeanX.SEXP += 15
            if not Situation:
                if JeanX.Love >= 500 and "unsatisfied" not in JeanX.RecentActions:
                    ch_j "That was. . . interesting."
                elif JeanX.Obed <= 500 and Player.Focus <= 20:
                    $ JeanX.FaceChange("perplexed", 1)
                    ch_j "Was that good for you?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_j "Oh? What did you have in mind?"
    call Checkout
    return

# end JeanX.Lick Ass /////////////////////////////////////////////////////////////////////////////
