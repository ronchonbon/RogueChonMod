# LauraX.Fondle /////////////////////////////////////////////////////////////////////////////
label Laura_Fondle: #rkel

    $ LauraX.Mouth = "smile"
    if not LauraX.Action:
        ch_l "Maybe later, [LauraX.Petname]"
        return
    menu:
        ch_l "Well? Where did you want to touch, [LauraX.Petname]?"
        "Your breasts?" if LauraX.Action:
                jump Laura_Fondle_Breasts
        "Your thighs?" if LauraX.Action:
                jump Laura_Fondle_Thighs
        "Your pussy?" if LauraX.Action:
                jump Laura_Fondle_Pussy
        "Your Ass?" if LauraX.Action:
                jump Laura_Fondle_Ass
        "Never mind.":
                return
    return

# ////////////////////////////////////////////////////////////////////////Start Fondle Pussy
label Laura_Fondle_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(LauraX)
                                                                                        # Will she let you fondle? Modifiers
    if LauraX.FondleP: #You've done it before
        $ temp_modifier += 20
    if LauraX.PantsNum() >= 6 or LauraX.HoseNum() >= 5: # she's got pants on.
        $ temp_modifier -= 10
    if LauraX.Lust > 75: #She's really horny
        $ temp_modifier += 15
    if LauraX.Lust > 75 and Situation == "auto": #She's really horny
        $ temp_modifier += 10
    if "exhibitionist" in LauraX.Traits:
        $ temp_modifier += (2*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.Petnames:
        $ temp_modifier += 10
    elif "ex" in LauraX.Traits:
        $ temp_modifier -= 25
    if LauraX.ForcedCount and not LauraX.Forced:
        $ temp_modifier -= 5 * LauraX.ForcedCount

    if Taboo and "tabno" in LauraX.DailyActions:
        $ temp_modifier -= 10
    if Taboo and "public" not in LauraX.History:
        $ temp_modifier -= 20

    if "no fondle pussy" in LauraX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no fondle pussy" in LauraX.RecentActions else 0

    $ Approval = ApprovalCheck(LauraX, 1050, TabM = 2) # 105, 120, 135, Taboo -80(185)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ LauraX.FaceChange("sexy")
            $ LauraX.Statup("Obed", 90, 1)
            $ LauraX.Statup("Obed", 70, 2)
            $ LauraX.Statup("Inbt", 70, 3)
            $ LauraX.Statup("Inbt", 30, 2)
            "As your hand creeps up her thigh, [LauraX.Name] seems a bit surprised, but then nods."
            jump Laura_FP_Prep
        else:
            $ LauraX.FaceChange("surprised")
            $ LauraX.Statup("Obed", 50, -2)
            ch_l "Roll it back, [LauraX.Petname]. . ."
            $ temp_modifier = 0
            $ Trigger2 = 0
            return

    if Situation == "pullback":
        $ LauraX.FaceChange("surprised")
        $ LauraX.Brows = "sad"
        if LauraX.Lust > 80:
            $ LauraX.Statup("Love", 70, -4)
        $ LauraX.Statup("Obed", 90, 1)
        $ LauraX.Statup("Obed", 70, 2)
        "As your hand pulls out, [LauraX.Name] gasps and looks upset."
        jump Laura_FP_Prep
    elif "fondle pussy" in LauraX.RecentActions:
        $ LauraX.FaceChange("sexy", 1)
        ch_l "Mmmm, again? I guess. . ."
        jump Laura_FP_Prep
    elif "fondle pussy" in LauraX.DailyActions:
        $ LauraX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Chill. . .",
            "Take it slow, I'm still shaking from earlier.",
            "Mmm. . ."])
        ch_l "[Line]"

    if Approval >= 2:                                                                   #She's into it. . .
        $ LauraX.FaceChange("bemused", 1)
        if LauraX.Forced:
            $ LauraX.FaceChange("sad")
            $ LauraX.Statup("Love", 70, -3, 1)
            $ LauraX.Statup("Love", 20, -2, 1)
            $ LauraX.Statup("Obed", 90, 1)
            $ LauraX.Statup("Inbt", 60, 1)
        ch_l "Mmmm, I couldn't refuse. . ."
        $ LauraX.Statup("Love", 90, 1)
        $ LauraX.Statup("Inbt", 50, 3)
        jump Laura_FP_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ LauraX.FaceChange("angry", 1)
        if "no fondle pussy" in LauraX.RecentActions:
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "tabno" in LauraX.DailyActions and "no fondle pussy" in LauraX.DailyActions:
            ch_l "I told you not to touch me like that in public!"
        elif "no fondle pussy" in LauraX.DailyActions:
            ch_l "Don't make me tell you again today."
        elif Taboo and "tabno" in LauraX.DailyActions:
            ch_l "I told you, not here, [LauraX.Petname]."
        elif not LauraX.FondleP:
            $ LauraX.FaceChange("bemused")
            ch_l "I don't think we're there yet, [LauraX.Petname]. . ."
        else:
            $ LauraX.FaceChange("bemused")
            ch_l "You wish."
        menu:
            extend ""
            "Sorry, never mind." if "no fondle pussy" in LauraX.DailyActions:
                $ LauraX.FaceChange("bemused")
                ch_l "It's cool, [LauraX.Petname]."
                return
            "Maybe later?" if "no fondle pussy" not in LauraX.DailyActions:
                $ LauraX.FaceChange("sexy")
                ch_l "Maybe, [LauraX.Petname]."
                $ LauraX.Statup("Love", 80, 2)
                $ LauraX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ LauraX.RecentActions.append("tabno")
                    $ LauraX.DailyActions.append("tabno")
                $ LauraX.RecentActions.append("no fondle pussy")
                $ LauraX.DailyActions.append("no fondle pussy")
                return
            "Come on, Please?":
                if Approval:
                    $ LauraX.FaceChange("sexy")
                    $ LauraX.Statup("Obed", 90, 2)
                    $ LauraX.Statup("Obed", 50, 2)
                    $ LauraX.Statup("Inbt", 70, 3)
                    $ LauraX.Statup("Inbt", 40, 2)
                    ch_l "Oooh, beg for me. . ."
                    jump Laura_FP_Prep
                else:
                    $ LauraX.FaceChange("sexy")
                    ch_l "No."

            "[[Start fondling anyway]":                                               # Pressured into fondling.
                $ Approval = ApprovalCheck(LauraX, 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                if Approval > 1 or (Approval and LauraX.Forced):
                    $ LauraX.FaceChange("sad")
                    $ LauraX.Statup("Love", 70, -5, 1)
                    $ LauraX.Statup("Love", 200, -2)
                    ch_l "Ok, fine. . ."
                    $ LauraX.Statup("Obed", 50, 4)
                    $ LauraX.Statup("Inbt", 80, 1)
                    $ LauraX.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ LauraX.Forced = 1
                    jump Laura_FP_Prep
                else:
                    $ LauraX.Statup("Love", 200, -15)
                    $ LauraX.FaceChange("angry", 1)
                    "She slaps your hand away."
                    $ LauraX.RecentActions.append("angry")
                    $ LauraX.DailyActions.append("angry")

    if "no fondle pussy" in LauraX.DailyActions:
        ch_l "I don't like to repeat myself, [LauraX.Petname]."
        $ LauraX.RecentActions.append("angry")
        $ LauraX.DailyActions.append("angry")
    elif LauraX.Forced:
        $ LauraX.FaceChange("angry", 1)
        ch_l "I don't think so, [LauraX.Petname]."
        $ LauraX.Statup("Lust", 70, 5)
        $ LauraX.Statup("Obed", 50, -2)
        $ LauraX.RecentActions.append("angry")
        $ LauraX.DailyActions.append("angry")
    elif Taboo:
        $ LauraX.FaceChange("angry", 1)
        $ LauraX.RecentActions.append("tabno")
        $ LauraX.DailyActions.append("tabno")
        ch_l "I try to stay off the radar."
    elif LauraX.FondleP:
        $ LauraX.FaceChange("sad")
        ch_l "Sorry, fingers outside."
    else:
        $ LauraX.FaceChange("sexy")
        $ LauraX.Mouth = "sad"
        ch_l "No thank you, [LauraX.Petname]."
    $ LauraX.RecentActions.append("no fondle pussy")
    $ LauraX.DailyActions.append("no fondle pussy")
    $ temp_modifier = 0
    return

label Laura_FP_Prep: #Animation set-up
    if Trigger2 == "fondle pussy":
        return

    call Laura_Pussy_Launch("fondle pussy")

    if Situation == LauraX:
            #Laura auto-starts
            $ Situation = 0
            if (LauraX.Legs and not LauraX.Upskirt) or (LauraX.Panties and not LauraX.PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck(LauraX, 1250, TabM = 1) or (LauraX.SeenPussy and ApprovalCheck(LauraX, 500) and not Taboo):
                        $ LauraX.Upskirt = 1
                        $ LauraX.PantiesDown = 1
                        $ Line = 0
                        if LauraX.PantsNum() == 5:
                            $ Line = LauraX.Name + " hikes up her skirt"
                        elif LauraX.PantsNum() >= 6:
                            $ Line = LauraX.Name + " pulls down her " + LauraX.Legs
                        else:
                            $ Line = 0
                        if LauraX.Panties:
                            if Line:
                                #wearing pants
                                "[Line] and pulls her [LauraX.Panties] out of the way."
                                "She then grabs your arm and then presses your hand against her crotch, clearly intending you to get to work."
                            else:
                                #no pants
                                "She pulls her [LauraX.Panties] out of the way, and then presses your hand against her crotch."
                                "She clearly intends for you to get to work."
                        else:
                            #pants but no panties
                            "[Line], and then presses your hand against her crotch."
                            "She clearly intends for you to get to work."
                        call Laura_First_Bottomless(1)
                else:
                        "[LauraX.Name] grabs your arm and presses your hand against her crotch, clearly intending you to get to work."
            else:
                        "[LauraX.Name] grabs your arm and presses your hand against her crotch, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":
                    $ LauraX.Statup("Inbt", 80, 3)
                    $ LauraX.Statup("Inbt", 50, 2)
                    "You start to run your fingers along her pussy."
                "Praise her.":
                    $ LauraX.FaceChange("sexy", 1)
                    $ LauraX.Statup("Inbt", 80, 3)
                    ch_p "I like the initiative, [LauraX.Pet]."
                    $ LauraX.NameCheck() #checks reaction to petname
                    "You start to run your fingers along her pussy."
                    $ LauraX.Statup("Love", 85, 1)
                    $ LauraX.Statup("Obed", 90, 1)
                    $ LauraX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your hand back."
                    $ LauraX.FaceChange("surprised")
                    $ LauraX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that right now, [LauraX.Pet]."
                    $ LauraX.NameCheck() #checks reaction to petname
                    "[LauraX.Name] pulls back."
                    $ LauraX.Statup("Obed", 90, 1)
                    $ LauraX.Statup("Obed", 50, 1)
                    $ LauraX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ LauraX.AddWord(1,"refused","refused")
                    return
            #end auto

    if not LauraX.Forced and Situation != "auto":
        $ temp_modifier = 0
        call Bottoms_Off(LauraX)
        if "angry" in LauraX.RecentActions:
            return
    $ temp_modifier = 0

    if not LauraX.FondleP:
        if LauraX.Forced:
            $ LauraX.Statup("Love", 90, -50)
            $ LauraX.Statup("Obed", 70, 35)
            $ LauraX.Statup("Inbt", 80, 25)
        else:
            $ LauraX.Statup("Love", 90, 10)
            $ LauraX.Statup("Obed", 70, 10)
            $ LauraX.Statup("Inbt", 80, 15)
    if Taboo:
        $ LauraX.Inbt += int(Taboo/10)
        $ LauraX.Lust += int(Taboo/5)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ LauraX.DrainWord("tabno")
    $ LauraX.DrainWord("no fondle pussy")
    $ LauraX.RecentActions.append("fondle pussy")
    $ LauraX.DailyActions.append("fondle pussy")
    call Laura_Pussy_Launch("fondle pussy")
    $ Speed = 1

label Laura_FP_Cycle: #Repeating strokes
    while Round > 0:
        call ViewShift(LauraX,LauraX.Pose,0,"fondle pussy")
        call Shift_Focus(LauraX)
        $ LauraX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "I want to stick a finger in. . ." if Speed != 2:
                                if LauraX.InsertP:
                                    $ Speed = 2
                                else:
                                    menu:
                                        "Ask her first":
                                            $ Situation = "shift"
                                        "Don't ask first [[just stick it in]":
                                            $ Situation = "auto"
                                    call Laura_Insert_Pussy

                        "Pull back a bit. . ." if Speed == 2:
                                    $ Speed = 0

                        "Slap her ass":
                                    call Slap_Ass(LauraX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Laura_FP_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0
                        "View":
                                    call ViewShift(LauraX,"menu")
                                    jump Laura_FP_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if LauraX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ LauraX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")

                                    "Shift primary action":
                                            if LauraX.Action and MultiAction:
                                                    menu:
                                                        "I want to lick your pussy.":
                                                                $ Situation = "shift"
                                                                call Laura_FP_After
                                                                call Laura_Lick_Pussy
                                                        "Just start licking":
                                                                $ Situation = "auto"
                                                                call Laura_FP_After
                                                                call Laura_Lick_Pussy
                                                        "Pull back to the thighs":
                                                                $ Situation = "pullback"
                                                                call Laura_FP_After
                                                                call Laura_Fondle_Thighs
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Laura_FP_After
                                                                call Laura_Dildo_Pussy
                                                        "Never Mind":
                                                                jump Laura_FP_Cycle
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Laura_FP_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [LauraX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(LauraX)
                                            "Ask [LauraX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(LauraX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(LauraX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Laura_FP_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Laura_FP_Cycle
                                            "Never mind":
                                                        jump Laura_FP_Cycle

                                    "Show her feet" if not ShowFeet and (LauraX.Pose == "doggy" or LauraX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (LauraX.Pose == "doggy" or LauraX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [LauraX.Name]":
                                            call Girl_Undress(LauraX)
                                    "Clean up [LauraX.Name] (locked)" if not LauraX.Spunk:
                                            pass
                                    "Clean up [LauraX.Name]" if LauraX.Spunk:
                                            call Girl_Cleanup(LauraX,"ask")
                                    "Never mind":
                                            jump Laura_FP_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Laura_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Laura_FP_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Laura_Pos_Reset
                                    $ Line = 0
                                    jump Laura_FP_After
        #End menu (if Line)

        call Shift_Focus(LauraX)
        call Sex_Dialog(LauraX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or LauraX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(LauraX)
                            if "angry" in LauraX.RecentActions:
                                call Laura_Pos_Reset
                                return
                            $ LauraX.Statup("Lust", 200, 5)
                            if 100 > LauraX.Lust >= 70 and LauraX.OCount < 2:
                                $ LauraX.RecentActions.append("unsatisfied")
                                $ LauraX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Laura_FP_After
                            $ Line = "came"

                    if LauraX.Lust >= 100:
                            #If Laura can cum
                            call Girl_Cumming(LauraX)
                            if Situation == "shift" or "angry" in LauraX.RecentActions:
                                jump Laura_FP_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in LauraX.RecentActions:#And Laura is unsatisfied,
                                    "[LauraX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Laura_FP_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if LauraX.SEXP >= 100 or ApprovalCheck(LauraX, 1200, "LO"):
            pass
        elif Cnt == (5 + LauraX.FondleP):
                    $ LauraX.Brows = "confused"
                    ch_l "Mmmm, you're enjoying that, huh?"
        elif LauraX.Lust >= 80:
                    pass
        elif Cnt == (15 + LauraX.FondleP) and LauraX.SEXP >= 15 and not ApprovalCheck(LauraX, 1500):
                    $ LauraX.Brows = "confused"
                    menu:
                        ch_l "Maybe change things up a little?"
                        "Finish up.":
                                "You let go. . ."
                                jump Laura_FP_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Laura_FP_After
                        "No, this is fun.":
                                if ApprovalCheck(LauraX, 1200) or ApprovalCheck(LauraX, 500, "O"):
                                    $ LauraX.Statup("Love", 200, -5)
                                    $ LauraX.Statup("Obed", 50, 3)
                                    $ LauraX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ LauraX.FaceChange("angry", 1)
                                    call Laura_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_l "I'm kinda bored here."
                                    $ LauraX.Statup("Love", 50, -3, 1)
                                    $ LauraX.Statup("Love", 80, -4, 1)
                                    $ LauraX.Statup("Obed", 30, -1, 1)
                                    $ LauraX.Statup("Obed", 50, -1, 1)
                                    $ LauraX.RecentActions.append("angry")
                                    $ LauraX.DailyActions.append("angry")
                                    jump Laura_FP_After
        #End Count check

        call Escalation(LauraX) #sees if she wants to escalate things

        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [LauraX.Petname]."

    #Round = 0 loop breaks
    $ LauraX.FaceChange("bemused", 0)
    $ Line = 0
    ch_l "Ok, [LauraX.Petname], breaktime."


label Laura_FP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Laura_Pos_Reset

    $ LauraX.FaceChange("sexy")

    $ LauraX.FondleP += 1
    $ LauraX.Action -=1
    if LauraX.PantsNum() < 6 or LauraX.Upskirt:
        $ LauraX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ LauraX.Addictionrate += 1

    call Partner_Like(LauraX,2)

    if LauraX.FondleP == 1:
            $ LauraX.SEXP += 7
            if not Situation:
                if LauraX.Love >= 500 and "unsatisfied" not in LauraX.RecentActions:
                    ch_l "You're really getting into the good stuff."
                elif LauraX.Obed <= 500 and Player.Focus <= 20:
                    $ LauraX.FaceChange("perplexed", 1)
                    ch_l "Did you find what you were looking for?"

    $ temp_modifier = 0

    call Checkout
    return

# end LauraX.Fondle Pussy /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy
label Laura_Insert_Pussy:
    call Shift_Focus(LauraX)
    if Situation == "auto":                                                                  #You auto-start
        if ApprovalCheck(LauraX, 1100, TabM = 2):
            $ LauraX.FaceChange("surprised")
            $ LauraX.Statup("Obed", 90, 1)
            $ LauraX.Statup("Obed", 70, 2)
            $ LauraX.Statup("Inbt", 70, 3)
            $ LauraX.Statup("Inbt", 30, 2)
            "As you slide a finger in, [LauraX.Name] seems a bit surprised, but seems into it."
            jump Laura_IP_Prep
        else:
            $ LauraX.FaceChange("surprised",2)
            $ LauraX.Statup("Love", 80, -2)
            $ LauraX.Statup("Obed", 50, -3)
            ch_l "Oooh!"
            "She slaps your hand back."
            $ LauraX.FaceChange("perplexed",1)
            ch_l "Watch your hands, or lose them."
            return

    if ApprovalCheck(LauraX, 1100, TabM = 2):                                                                   #She's into it. . .
        if LauraX.Forced:
            $ LauraX.FaceChange("sad")
            $ LauraX.Statup("Love", 70, -3, 1)
            $ LauraX.Statup("Love", 20, -2, 1)
            $ LauraX.Statup("Obed", 90, 1)
            $ LauraX.Statup("Inbt", 60, 1)
            ch_l "Going there, huh. . ."
        else:
            $ LauraX.FaceChange("sexy", 1)
            $ LauraX.Statup("Love", 90, 1)
            $ LauraX.Statup("Inbt", 50, 3)
            ch_l "Mmmmmm. . ."
        $ LauraX.Statup("Obed", 20, 1)
        $ LauraX.Statup("Obed", 60, 1)
        $ LauraX.Statup("Inbt", 70, 2)
        jump Laura_IP_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ LauraX.FaceChange("bemused", 1)
        ch_l "Nope."
        $ LauraX.Blush = 0
    return


label Laura_IP_Prep: #Animation set-up
    if not LauraX.InsertP:
        $ LauraX.InsertP = 1
        $ LauraX.SEXP += 10
        if LauraX.Forced:
            $ LauraX.Statup("Love", 90, -60)
            $ LauraX.Statup("Obed", 70, 55)
            $ LauraX.Statup("Inbt", 80, 35)
        else:
            $ LauraX.Statup("Love", 90, 10)
            $ LauraX.Statup("Obed", 70, 20)
            $ LauraX.Statup("Inbt", 80, 25)

    if not LauraX.Forced and Situation != "auto":
        call Girl_Undress(LauraX,"bottom")
        if "angry" in LauraX.RecentActions:
            return

    if Taboo:
        $ LauraX.Inbt += int(Taboo/10)
        $ LauraX.Lust += int(Taboo/5)

    $ Line = 0
    $ Speed = 2
    return

label Laura_Lick_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(LauraX)
                                                                                  # Will she let you fondle? Modifiers
    if LauraX.LickP: #You've done it before
        $ temp_modifier += 15
    if LauraX.PantsNum() >= 6 or LauraX.HoseNum() >= 5: # she's got pants on.
        $ temp_modifier -= 15
    if LauraX.Lust > 95:
        $ temp_modifier += 20
    elif LauraX.Lust > 85: #She's really horny
        $ temp_modifier += 15
    if Situation == "shift":
        $ temp_modifier += 10
    if LauraX.Lust > 85 and Situation == "auto": #She's really horny
        $ temp_modifier += 10
    if "exhibitionist" in LauraX.Traits:
        $ temp_modifier += (4*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.Petnames:
        $ temp_modifier += 10
    elif "ex" in LauraX.Traits:
        $ temp_modifier -= 25
    if LauraX.ForcedCount and not LauraX.Forced:
        $ temp_modifier -= 5 * LauraX.ForcedCount

    if Taboo and "tabno" in LauraX.DailyActions:
        $ temp_modifier -= 10
    if Taboo and "public" not in LauraX.History:
        $ temp_modifier -= 20

    if "no lick pussy" in LauraX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no lick pussy" in LauraX.RecentActions else 0

    $ Approval = ApprovalCheck(LauraX, 1250, TabM = 4) # 125, 140, 155, Taboo -160(285)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ LauraX.FaceChange("surprised")
            $ LauraX.Statup("Obed", 90, 1)
            $ LauraX.Statup("Obed", 70, 2)
            $ LauraX.Statup("Inbt", 70, 3)
            $ LauraX.Statup("Inbt", 30, 2)
            "As you crouch down and start to lick her pussy, [LauraX.Name] starts, but then softens."
            $ LauraX.FaceChange("sexy")
            jump Laura_LP_Prep
        else:
            $ LauraX.FaceChange("surprised")
            $ LauraX.Statup("Love", 80, -2)
            $ LauraX.Statup("Obed", 50, -3)
            ch_l "Hey, good instincts, but maybe hold off?"
            $ LauraX.FaceChange("perplexed",1)
            "She pushes your head back away from her."
            $ temp_modifier = 0
            $ Trigger2 = 0
            return

    if "lick pussy" in LauraX.RecentActions:
        $ LauraX.FaceChange("sexy", 1)
        ch_l "Mmmm, again? I guess. . ."
        jump Laura_LP_Prep
    elif "lick pussy" in LauraX.DailyActions:
        $ LauraX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Huh? Again?",
            "I must have done something right.",
            "I do like this treatment. . .",
            "Mmm. . ."])
        ch_l "[Line]"

    if Approval >= 2:                                                                   #She's into it. . .
        if LauraX.Forced:
            $ LauraX.FaceChange("sad")
            $ LauraX.Statup("Love", 70, -3, 1)
            $ LauraX.Statup("Love", 20, -2, 1)
            $ LauraX.Statup("Obed", 90, 1)
            $ LauraX.Statup("Inbt", 60, 1)
            ch_l "If you must. . ."
        else:
            $ LauraX.FaceChange("sexy", 1)
            $ LauraX.Eyes = "closed"
            $ LauraX.Statup("Love", 90, 1)
            $ LauraX.Statup("Inbt", 50, 3)
            $ LauraX.Statup("Lust", 200, 3)
            ch_l "Mmmmmm. . ."
        $ LauraX.Statup("Obed", 20, 1)
        $ LauraX.Statup("Obed", 60, 1)
        $ LauraX.Statup("Inbt", 70, 2)
        jump Laura_LP_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ LauraX.FaceChange("angry", 1)
        if "no lick pussy" in LauraX.RecentActions:
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "tabno" in LauraX.DailyActions and "no lick pussy" in LauraX.DailyActions:
            ch_l "You already got your answer!"
        elif "no lick pussy" in LauraX.DailyActions:
            ch_l "Don't make me tell you again today."
        elif Taboo and "tabno" in LauraX.DailyActions:
            ch_l "I told you, not here, [LauraX.Petname]."
        elif not LauraX.LickP:
            $ LauraX.FaceChange("bemused")
            ch_l "I'm not sure we're there yet, [LauraX.Petname]. . ."
        else:
            $ LauraX.FaceChange("bemused")
            ch_l "I'm really not cool with that. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no lick pussy" in LauraX.DailyActions:
                $ LauraX.FaceChange("bemused")
                ch_l "It's cool, [LauraX.Petname]."
                return
            "I'm sure I can convince you later. . ." if "no lick pussy" not in LauraX.DailyActions:
                $ LauraX.FaceChange("sexy")
                ch_l "I'll be thinking about it, [LauraX.Petname]."
                $ LauraX.Statup("Love", 80, 2)
                $ LauraX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ LauraX.RecentActions.append("tabno")
                    $ LauraX.DailyActions.append("tabno")
                $ LauraX.RecentActions.append("no lick pussy")
                $ LauraX.DailyActions.append("no lick pussy")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ LauraX.FaceChange("sexy")
                    $ LauraX.Statup("Obed", 90, 2)
                    $ LauraX.Statup("Obed", 50, 2)
                    ch_l "You make a good point. . ."
                    $ LauraX.Statup("Inbt", 70, 3)
                    $ LauraX.Statup("Inbt", 40, 2)
                    jump Laura_LP_Prep
                else:
                    $ LauraX.FaceChange("sexy")
                    ch_l "I would, but still no, [LauraX.Petname]."

            "[[Get in there anyway]":                                               # Pressured into being licked.
                $ Approval = ApprovalCheck(LauraX, 750, "OI", TabM = 4) # 75, 90, 105, -160(235)
                if Approval > 1 or (Approval and LauraX.Forced):
                    $ LauraX.FaceChange("sad")
                    $ LauraX.Statup("Love", 70, -5, 1)
                    $ LauraX.Statup("Love", 200, -2)
                    ch_l "If you insist. . ."
                    $ LauraX.Statup("Obed", 50, 4)
                    $ LauraX.Statup("Inbt", 80, 1)
                    $ LauraX.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ LauraX.Forced = 1
                    jump Laura_LP_Prep
                else:
                    $ LauraX.Statup("Love", 200, -15)
                    $ LauraX.FaceChange("angry", 1)
                    "She shoves your head back."
                    $ LauraX.RecentActions.append("angry")
                    $ LauraX.DailyActions.append("angry")

    if "no lick pussy" in LauraX.DailyActions:
        ch_l "I don't like to repeat myself, [LauraX.Petname]."
        $ LauraX.RecentActions.append("angry")
        $ LauraX.DailyActions.append("angry")
    elif LauraX.Forced:
        $ LauraX.FaceChange("angry", 1)
        ch_l "I really can't, [LauraX.Petname]."
        $ LauraX.Statup("Lust", 80, 5)
        $ LauraX.Statup("Obed", 50, -2)
        $ LauraX.RecentActions.append("angry")
        $ LauraX.DailyActions.append("angry")
    elif Taboo:
        $ LauraX.FaceChange("angry", 1)
        $ LauraX.RecentActions.append("tabno")
        $ LauraX.DailyActions.append("tabno")
        ch_l "I try to stay off the radar."
    elif LauraX.LickP:
        $ LauraX.FaceChange("sad")
        ch_l "Keep your head out of there."
    else:
        $ LauraX.FaceChange("surprised")
        ch_l "Yeah, sorry."
        $ LauraX.FaceChange()
    $ LauraX.RecentActions.append("no lick pussy")
    $ LauraX.DailyActions.append("no lick pussy")
    $ temp_modifier = 0
    return

label Laura_LP_Prep: #Animation set-up
    if Trigger2 == "lick pussy": #fix pull down pants now an option, make it work
        return

    $ temp_modifier = 0
    call Laura_Pussy_Launch("lick pussy")

    if Situation == LauraX:
            #Laura auto-starts
            $ Situation = 0
            if (LauraX.Legs and not LauraX.Upskirt) or (LauraX.Panties and not LauraX.PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck(LauraX, 1250, TabM = 1) or (LauraX.SeenPussy and ApprovalCheck(LauraX, 500) and not Taboo):
                        $ LauraX.Upskirt = 1
                        $ LauraX.PantiesDown = 1
                        $ Line = 0
                        if LauraX.PantsNum() == 5:
                            $ Line = LauraX.Name + " hikes up her skirt"
                        elif LauraX.PantsNum() >= 6:
                            $ Line = LauraX.Name + " pulls down her " + LauraX.Legs
                        else:
                            $ Line = 0
                        if LauraX.Panties:
                            if Line:
                                #wearing pants
                                "[Line] and pulls her [LauraX.Panties] out of the way."
                                "She then grabs your head and wraps her thighs around it, clearly intending you to get to work."
                            else:
                                #no pants
                                "She pulls her [LauraX.Panties] out of the way, and then wraps her thighs around your head."
                                "She clearly intends for you to get to work."
                        else:
                            #pants but no panties
                            "[Line], and then wraps her thighs around your head."
                            "She clearly intends for you to get to work."
                        call Laura_First_Bottomless(1)
                else:
                        "[LauraX.Name] grabs your head and wraps her thighs around it, clearly intending you to get to work."
            else:
                        "[LauraX.Name] grabs your head and wraps her thighs around it, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":
                    $ LauraX.Statup("Inbt", 80, 3)
                    $ LauraX.Statup("Inbt", 50, 2)
                    "You start licking."
                "Praise her.":
                    $ LauraX.FaceChange("sexy", 1)
                    $ LauraX.Statup("Inbt", 80, 3)
                    ch_p "Mmm, I like this idea, [LauraX.Pet]."
                    $ LauraX.NameCheck() #checks reaction to petname
                    "You start licking."
                    $ LauraX.Statup("Love", 85, 1)
                    $ LauraX.Statup("Obed", 90, 1)
                    $ LauraX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your head away."
                    $ LauraX.FaceChange("surprised")
                    $ LauraX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that right now, [LauraX.Pet]."
                    $ LauraX.NameCheck() #checks reaction to petname
                    "[LauraX.Name] pulls back."
                    $ LauraX.Statup("Obed", 90, 1)
                    $ LauraX.Statup("Obed", 50, 1)
                    $ LauraX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ LauraX.AddWord(1,"refused","refused")
                    return
            #end auto

    if not LauraX.Forced and Situation != "auto":
        $ temp_modifier = 0
        if LauraX.PantsNum() >= 6 and not LauraX.Upskirt:
            $ temp_modifier = 15
        call Bottoms_Off(LauraX)
        if "angry" in LauraX.RecentActions:
            return

    if not LauraX.LickP:
        if LauraX.Forced:
            $ LauraX.Statup("Love", 90, -30)
            $ LauraX.Statup("Obed", 70, 35)
            $ LauraX.Statup("Inbt", 80, 75)
        else:
            $ LauraX.Statup("Love", 90, 35)
            $ LauraX.Statup("Obed", 70, 15)
            $ LauraX.Statup("Inbt", 80, 35)
    if Taboo:
        $ LauraX.Inbt += int(Taboo/10)
        $ LauraX.Lust += int(Taboo/5)
    if Situation:
        $ renpy.pop_call()
        $ Situation = 0

    if LauraX.PantsNum() == 5:
        $ LauraX.Upskirt = 1
        $ LauraX.SeenPanties = 1
    call Laura_First_Bottomless(1)

    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ LauraX.DrainWord("tabno")
    $ LauraX.DrainWord("no lick pussy")
    $ LauraX.RecentActions.append("lick pussy")
    $ LauraX.DailyActions.append("lick pussy")
    call Laura_Pussy_Launch("lick pussy")

label Laura_LP_Cycle: #Repeating strokes
    if Trigger2 == "kiss you":
            $ Trigger2 = 0
    while Round > 0:
        call ViewShift(LauraX,LauraX.Pose,0,"lick pussy")
        call Shift_Focus(LauraX)
        $ LauraX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(LauraX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Laura_LP_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0
                        "View":
                                    call ViewShift(LauraX,"menu")
                                    jump Laura_LP_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if LauraX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ LauraX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")

                                    "Shift primary action":
                                            if LauraX.Action and MultiAction:
                                                    menu:
                                                        "Pull out and start rubbing again.":
                                                                if LauraX.Action and MultiAction:
                                                                    $ Situation = "pullback"
                                                                    call Laura_LP_After
                                                                    call Laura_Fondle_Pussy
                                                                else:
                                                                    call Sex_Basic_Dialog(LauraX,"tired")
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Laura_LP_After
                                                                call Laura_Dildo_Pussy
                                                        "Never Mind":
                                                                jump Laura_LP_Cycle
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Laura_LP_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [LauraX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(LauraX)
                                            "Ask [LauraX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(LauraX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(LauraX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Laura_LP_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Laura_LP_Cycle
                                            "Never mind":
                                                        jump Laura_LP_Cycle

                                    "Show her feet" if not ShowFeet and (LauraX.Pose == "doggy" or LauraX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (LauraX.Pose == "doggy" or LauraX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [LauraX.Name]":
                                            call Girl_Undress(LauraX)
                                    "Clean up [LauraX.Name] (locked)" if not LauraX.Spunk:
                                            pass
                                    "Clean up [LauraX.Name]" if LauraX.Spunk:
                                            call Girl_Cleanup(LauraX,"ask")
                                    "Never mind":
                                            jump Laura_LP_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Laura_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Laura_LP_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Laura_Pos_Reset
                                    $ Line = 0
                                    jump Laura_LP_After
        #End menu (if Line)

        if LauraX.Panties or LauraX.PantsNum() >= 6 or LauraX.HoseNum() >= 5: #This checks if Laura wants to strip down.
                call Girl_Undress(LauraX,"auto")

        call Shift_Focus(LauraX)
        call Sex_Dialog(LauraX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or LauraX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(LauraX)
                            if "angry" in LauraX.RecentActions:
                                call Laura_Pos_Reset
                                return
                            $ LauraX.Statup("Lust", 200, 5)
                            if 100 > LauraX.Lust >= 70 and LauraX.OCount < 2:
                                $ LauraX.RecentActions.append("unsatisfied")
                                $ LauraX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Laura_LP_After
                            $ Line = "came"

                    if LauraX.Lust >= 100:
                            #If Laura can cum
                            call Girl_Cumming(LauraX)
                            if Situation == "shift" or "angry" in LauraX.RecentActions:
                                jump Laura_LP_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in LauraX.RecentActions:#And Laura is unsatisfied,
                                    "[LauraX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Laura_LP_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if LauraX.SEXP >= 100 or ApprovalCheck(LauraX, 1200, "LO"):
            pass
        elif Cnt == (5 + LauraX.LickP):
                    $ LauraX.Brows = "confused"
                    ch_l "Isn't it just delicious?"
        elif LauraX.Lust >= 80:
                    pass
        elif Cnt == (15 + LauraX.LickP) and LauraX.SEXP >= 15 and not ApprovalCheck(LauraX, 1500):
                    $ LauraX.Brows = "confused"
                    menu:
                        ch_l "Maybe change things up a little?"
                        "Finish up.":
                                "You let go. . ."
                                jump Laura_LP_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Laura_LP_After
                        "No, this is fun.":
                                if ApprovalCheck(LauraX, 1200) or ApprovalCheck(LauraX, 500, "O"):
                                    $ LauraX.Statup("Love", 200, -5)
                                    $ LauraX.Statup("Obed", 50, 3)
                                    $ LauraX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ LauraX.FaceChange("angry", 1)
                                    call Laura_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_l "I'm kinda bored here."
                                    $ LauraX.Statup("Love", 50, -3, 1)
                                    $ LauraX.Statup("Love", 80, -4, 1)
                                    $ LauraX.Statup("Obed", 30, -1, 1)
                                    $ LauraX.Statup("Obed", 50, -1, 1)
                                    $ LauraX.RecentActions.append("angry")
                                    $ LauraX.DailyActions.append("angry")
                                    jump Laura_LP_After
        #End Count check

        call Escalation(LauraX) #sees if she wants to escalate things

        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [LauraX.Petname]."

    #Round = 0 loop breaks
    $ LauraX.FaceChange("bemused", 0)
    $ Line = 0
    ch_l "Ok, [LauraX.Petname], breaktime."


label Laura_LP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Laura_Pos_Reset

    $ LauraX.FaceChange("sexy")

    $ LauraX.LickP += 1
    $ LauraX.Action -=1
    if LauraX.PantsNum() < 6 or LauraX.Upskirt:
        $ LauraX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ LauraX.Addictionrate += 1

    if Partner == "Rogue":
        call Partner_Like(LauraX,3,2)
    else:
        call Partner_Like(LauraX,2)

    if LauraX.LickP == 1:
            $ LauraX.SEXP += 10
            if not Situation:
                if LauraX.Love >= 500 and "unsatisfied" not in LauraX.RecentActions:
                    ch_l "That was a really good use of that tongue of yours."
                elif LauraX.Obed <= 500 and Player.Focus <= 20:
                    $ LauraX.FaceChange("perplexed", 1)
                    ch_l "I suppose we both got something out of that. . ."

    $ temp_modifier = 0

    call Checkout
    return


# end LauraX.Lick Pussy /////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////Start Fondle Ass
label Laura_Fondle_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(LauraX)
                                                                                     # Will she let you fondle? Modifiers
    if LauraX.FondleA: #You've done it before
        $ temp_modifier += 10
    if LauraX.PantsNum() >= 6 or LauraX.HoseNum() >= 5: # she's got pants on.
        $ temp_modifier -= 5
    if LauraX.Lust > 75: #She's really horny
        $ temp_modifier += 15
    if "exhibitionist" in LauraX.Traits:
        $ temp_modifier += Taboo
    if LauraX in Player.Harem or "sex friend" in LauraX.Petnames:
        $ temp_modifier += 10
    elif "ex" in LauraX.Traits:
        $ temp_modifier -= 25
    if LauraX.ForcedCount and not LauraX.Forced:
        $ temp_modifier -= 5 * LauraX.ForcedCount

    if Taboo and "tabno" in LauraX.DailyActions:
        $ temp_modifier -= 10
    if Taboo and "public" not in LauraX.History:
        $ temp_modifier -= 20

    if "no fondle ass" in LauraX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no fondle ass" in LauraX.RecentActions else 0

    $ Approval = ApprovalCheck(LauraX, 850, TabM=1) # 85, 100, 115, Taboo -40(125)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ LauraX.FaceChange("surprised", 1)
            $ LauraX.Statup("Obed", 70, 2)
            $ LauraX.Statup("Inbt", 40, 2)
            "As your hand creeps down her backside, [LauraX.Name] shivers a bit, and then relaxes."
            $ LauraX.FaceChange("sexy")
            jump Laura_FA_Prep
        else:
            $ LauraX.FaceChange("surprised")
            $ LauraX.Statup("Obed", 50, -3)
            ch_l "Hands off, [LauraX.Petname]."
            $ LauraX.FaceChange("bemused")
            $ temp_modifier = 0
            $ Trigger2 = 0
            return

    if Situation == "pullback":
        $ LauraX.FaceChange("surprised")
        $ LauraX.Brows = "sad"
        if LauraX.Lust > 80:
            $ LauraX.Statup("Love", 70, -4)
        $ LauraX.Statup("Obed", 90, 1)
        $ LauraX.Statup("Obed", 70, 2)
        "As your finger slides out, [LauraX.Name] gasps and looks upset."
        jump Laura_FA_Prep
    elif "fondle ass" in LauraX.RecentActions:
        $ LauraX.FaceChange("sexy", 1)
        ch_l "Mmmm, again? I guess. . ."
        jump Laura_FA_Prep
    elif "fondle ass" in LauraX.DailyActions:
        $ LauraX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Mmm, you like that? . .",
            "Mmm. . ."])
        ch_l "[Line]"

    if Approval >= 2:                                                                   #She's into it. . .
        if LauraX.Forced:
            $ LauraX.FaceChange("sad")
            $ LauraX.Statup("Love", 70, -2, 1)
            $ LauraX.Statup("Obed", 90, 2)
            $ LauraX.Statup("Inbt", 60, 2)
            ch_l "If you insist. . ."
        else:
            $ LauraX.FaceChange("bemused, 1")
            ch_l "Yeah, ok. . ."
        $ LauraX.Statup("Lust", 200, 3)
        $ LauraX.Statup("Obed", 60, 1)
        $ LauraX.Statup("Inbt", 70, 1)
        jump Laura_FA_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ LauraX.FaceChange("angry", 1)
        if "no fondle ass" in LauraX.RecentActions:
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "tabno" in LauraX.DailyActions and "no fondle ass" in LauraX.DailyActions:
            ch_l "I told you not to touch me like that in public!"
        elif "no fondle ass" in LauraX.DailyActions:
            ch_l "Don't make me tell you again today."
        elif Taboo and "tabno" in LauraX.DailyActions:
            ch_l "I told you, not here, [LauraX.Petname]."
        elif not LauraX.FondleA:
            $ LauraX.FaceChange("bemused")
            ch_l "Not yet, [LauraX.Petname]. . ."
        else:
            $ LauraX.FaceChange("bemused")
            ch_l "Let's not, ok [LauraX.Petname]?"
        menu:
            extend ""
            "Sorry, never mind." if "no fondle ass" in LauraX.DailyActions:
                $ LauraX.FaceChange("bemused")
                ch_l "It's cool, [LauraX.Petname]."
                return
            "Maybe later?" if "no fondle ass" not in LauraX.DailyActions:
                $ LauraX.FaceChange("sexy")
                ch_l "Maybe?"
                $ LauraX.Statup("Love", 80, 2)
                $ LauraX.Statup("Inbt", 50, 2)
                if Taboo:
                    $ LauraX.RecentActions.append("tabno")
                    $ LauraX.DailyActions.append("tabno")
                $ LauraX.RecentActions.append("no fondle ass")
                $ LauraX.DailyActions.append("no fondle ass")
                return
            "Just one good squeeze?":
                if Approval:
                    $ LauraX.FaceChange("sexy")
                    $ LauraX.Statup("Obed", 90, 1)
                    $ LauraX.Statup("Obed", 50, 2)
                    ch_l "Oooh, beg for me. . ."
                    $ LauraX.Statup("Inbt", 70, 1)
                    $ LauraX.Statup("Inbt", 40, 2)
                    jump Laura_FA_Prep
                else:
                    $ LauraX.FaceChange("sexy")
                    ch_l "No."

            "[[Start fondling anyway]":                                               # Pressured into fondling.
                $ Approval = ApprovalCheck(LauraX, 250, "OI", TabM = 3) # 25, 40, 55, -120(145)
                if Approval > 1 or (Approval and LauraX.Forced):
                    $ LauraX.FaceChange("sad")
                    $ LauraX.Statup("Love", 70, -3, 1)
                    $ LauraX.Statup("Love", 200, -1)
                    ch_l "Fine, I guess."
                    $ LauraX.Statup("Obed", 50, 3)
                    $ LauraX.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ LauraX.Forced = 1
                    jump Laura_FA_Prep
                else:
                    $ LauraX.Statup("Love", 200, -10)
                    $ LauraX.FaceChange("angry", 1)
                    "She slaps your hand away."
                    $ LauraX.RecentActions.append("angry")
                    $ LauraX.DailyActions.append("angry")

    if "no fondle ass" in LauraX.DailyActions:
        ch_l "I don't like to repeat myself, [LauraX.Petname]."
        $ LauraX.RecentActions.append("angry")
        $ LauraX.DailyActions.append("angry")
    elif LauraX.Forced:
        $ LauraX.FaceChange("angry", 1)
        ch_l "Do you want to keep those fingers?"
        $ LauraX.Statup("Lust", 60, 5)
        $ LauraX.Statup("Obed", 50, -2)
        $ LauraX.RecentActions.append("angry")
        $ LauraX.DailyActions.append("angry")
    elif Taboo:
        $ LauraX.FaceChange("angry", 1)
        $ LauraX.RecentActions.append("tabno")
        $ LauraX.DailyActions.append("tabno")
        ch_l "I try to stay off the radar."
    elif LauraX.FondleA:
        $ LauraX.FaceChange("sad")
        ch_l "Sorry, keep your hands to yourself."
    else:
        $ LauraX.FaceChange("sexy")
        $ LauraX.Mouth = "sad"
        ch_l "No."
    $ LauraX.RecentActions.append("no fondle ass")
    $ LauraX.DailyActions.append("no fondle ass")
    $ temp_modifier = 0
    return

    ch_l "Sorry, I don't even know how I got here. . ."
    return

label Laura_FA_Prep: #Animation set-up
    if Trigger2 == "fondle ass":
        return
    if not LauraX.Forced and Situation != "auto":
        $ temp_modifier = 0
        call Bottoms_Off(LauraX)
        if "angry" in LauraX.RecentActions:
            return
    $ temp_modifier = 0
    call Laura_Pussy_Launch("fondle ass")
    if not LauraX.FondleA:
        if LauraX.Forced:
            $ LauraX.Statup("Love", 90, -20)
            $ LauraX.Statup("Obed", 70, 20)
            $ LauraX.Statup("Inbt", 80, 15)
        else:
            $ LauraX.Statup("Love", 90, 10)
            $ LauraX.Statup("Obed", 70, 12)
            $ LauraX.Statup("Inbt", 80, 20)
    if Taboo:
        $ LauraX.Inbt += int(Taboo/10)
        $ LauraX.Lust += int(Taboo/5)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ LauraX.DrainWord("tabno")
    $ LauraX.DrainWord("no fondle ass")
    $ LauraX.RecentActions.append("fondle ass")
    $ LauraX.DailyActions.append("fondle ass")
    call Laura_Pussy_Launch("fondle ass")

label Laura_FA_Cycle: #Repeating strokes
    while Round > 0:
        call ViewShift(LauraX,LauraX.Pose,0,"fondle ass")
        call Shift_Focus(LauraX)
        $ LauraX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(LauraX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Laura_FA_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0
                        "View":
                                    call ViewShift(LauraX,"menu")
                                    jump Laura_FA_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if LauraX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ LauraX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")

                                    "Shift primary action":
                                            if LauraX.Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in.":
                                                                $ Situation = "shift"
                                                                call Laura_FA_After
                                                                call Laura_Insert_Ass
                                                        "Just stick a finger in without asking.":
                                                                $ Situation = "auto"
                                                                call Laura_FA_After
                                                                call Laura_Insert_Ass
                                                        "I want to lick your asshole.":
                                                                $ Situation = "shift"
                                                                call Laura_FA_After
                                                                call Laura_Lick_Ass
                                                        "Just start licking.":
                                                                $ Situation = "auto"
                                                                call Laura_FA_After
                                                                call Laura_Lick_Ass
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Laura_FA_After
                                                                call Laura_Dildo_Ass
                                                        "Never Mind":
                                                                jump Laura_FA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Laura_FA_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [LauraX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(LauraX)
                                            "Ask [LauraX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(LauraX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(LauraX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Laura_FA_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Laura_FA_Cycle
                                            "Never mind":
                                                        jump Laura_FA_Cycle

                                    "Show her feet" if not ShowFeet and (LauraX.Pose == "doggy" or LauraX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (LauraX.Pose == "doggy" or LauraX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [LauraX.Name]":
                                            call Girl_Undress(LauraX)
                                    "Clean up [LauraX.Name] (locked)" if not LauraX.Spunk:
                                            pass
                                    "Clean up [LauraX.Name]" if LauraX.Spunk:
                                            call Girl_Cleanup(LauraX,"ask")
                                    "Never mind":
                                            jump Laura_FA_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Laura_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Laura_FA_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Laura_Pos_Reset
                                    $ Line = 0
                                    jump Laura_FA_After
        #End menu (if Line)

        if LauraX.Panties or LauraX.PantsNum() >= 6 or LauraX.HoseNum() >= 5: #This checks if Laura wants to strip down.
                call Girl_Undress(LauraX,"auto")

        call Shift_Focus(LauraX)
        call Sex_Dialog(LauraX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or LauraX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(LauraX)
                            if "angry" in LauraX.RecentActions:
                                call Laura_Pos_Reset
                                return
                            $ LauraX.Statup("Lust", 200, 5)
                            if 100 > LauraX.Lust >= 70 and LauraX.OCount < 2 and LauraX.SEXP >= 20:
                                $ LauraX.RecentActions.append("unsatisfied")
                                $ LauraX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Laura_FA_After
                            $ Line = "came"

                    if LauraX.Lust >= 100:
                            #If Laura can cum
                            call Girl_Cumming(LauraX)
                            if Situation == "shift" or "angry" in LauraX.RecentActions:
                                jump Laura_FA_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in LauraX.RecentActions:#And Laura is unsatisfied,
                                    "[LauraX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Laura_FA_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if LauraX.SEXP >= 100 or ApprovalCheck(LauraX, 1200, "LO"):
            pass
        elif Cnt == (5 + LauraX.FondleA):
                    $ LauraX.Brows = "confused"
                    ch_l "Mmmm. . ."
        elif LauraX.Lust >= 80:
                    pass
        elif Cnt == (15 + LauraX.FondleA) and LauraX.SEXP >= 15 and not ApprovalCheck(LauraX, 1500):
                    $ LauraX.Brows = "confused"
                    menu:
                        ch_l "Maybe change things up a little?"
                        "Finish up.":
                                "You let go. . ."
                                jump Laura_FA_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Laura_FA_After
                        "No, this is fun.":
                                if ApprovalCheck(LauraX, 1200) or ApprovalCheck(LauraX, 500, "O"):
                                    $ LauraX.Statup("Love", 200, -5)
                                    $ LauraX.Statup("Obed", 50, 3)
                                    $ LauraX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ LauraX.FaceChange("angry", 1)
                                    call Laura_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_l "I'm kinda bored here."
                                    $ LauraX.Statup("Love", 50, -3, 1)
                                    $ LauraX.Statup("Love", 80, -4, 1)
                                    $ LauraX.Statup("Obed", 30, -1, 1)
                                    $ LauraX.Statup("Obed", 50, -1, 1)
                                    $ LauraX.RecentActions.append("angry")
                                    $ LauraX.DailyActions.append("angry")
                                    jump Laura_FA_After
        #End Count check

        call Escalation(LauraX) #sees if she wants to escalate things

        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [LauraX.Petname]."

    #Round = 0 loop breaks
    $ LauraX.FaceChange("bemused", 0)
    $ Line = 0
    ch_l "Ok, [LauraX.Petname], breaktime."


label Laura_FA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Laura_Pos_Reset

    $ LauraX.FaceChange("sexy")

    $ LauraX.FondleA += 1
    $ LauraX.Action -=1
    if LauraX.PantsNum() < 6 or LauraX.Upskirt:
        $ LauraX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ LauraX.Addictionrate += 1

        call Partner_Like(LauraX,2)

    if LauraX.FondleA == 1:
            $ LauraX.SEXP += 4
            if not Situation:
                if LauraX.Love >= 500 and "unsatisfied" not in LauraX.RecentActions:
                    ch_l "That was. . . nice. . ."
                elif LauraX.Obed <= 500 and Player.Focus <= 20:
                    $ LauraX.FaceChange("perplexed", 1)
                    ch_l "Did you enjoy that?"

    $ temp_modifier = 0
    call Checkout
    return


# end LauraX.Fondle Ass /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Ass
label Laura_Insert_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(LauraX)

    if LauraX.InsertA: #You've done it before
        $ temp_modifier += 25
    if LauraX.PantsNum() >= 6 or LauraX.HoseNum() >= 5: # she's got pants on.
        $ temp_modifier -= 15
    if LauraX.Lust > 85: #She's really horny
        $ temp_modifier += 15
    if LauraX.Lust > 95:
        $ temp_modifier += 5
    if Situation == "shift":
        $ temp_modifier += 10
    if LauraX.Lust > 85 and Situation == "auto": #She's really horny
        $ temp_modifier += 10
    if "exhibitionist" in LauraX.Traits:
        $ temp_modifier += (4*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.Petnames:
        $ temp_modifier += 10
    elif "ex" in LauraX.Traits:
        $ temp_modifier -= 25
    if LauraX.ForcedCount and not LauraX.Forced:
        $ temp_modifier -= 5 * LauraX.ForcedCount

    if Taboo and "tabno" in LauraX.DailyActions:
        $ temp_modifier -= 10
    if Taboo and "public" not in LauraX.History:
        $ temp_modifier -= 20

    if "no insert ass" in LauraX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no insert ass" in LauraX.RecentActions else 0

    $ Approval = ApprovalCheck(LauraX, 1300, TabM = 3) # 130, 145, 160, Taboo -120(250)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ LauraX.FaceChange("surprised")
            $ LauraX.Statup("Obed", 90, 2)
            $ LauraX.Statup("Obed", 70, 2)
            $ LauraX.Statup("Inbt", 80, 2)
            $ LauraX.Statup("Inbt", 30, 2)
            "As you slide a finger in, [LauraX.Name] tightens around it in surprise, but seems into it."
            $ LauraX.FaceChange("sexy")
            jump Laura_IA_Prep
        else:
            $ LauraX.FaceChange("surprised")
            $ LauraX.Statup("Love", 80, -2)
            $ LauraX.Statup("Obed", 50, -3)
            ch_l "Whoa, back off, [LauraX.Petname]."
            $ temp_modifier = 0
            $ Trigger2 = 0
            return

    if "insert ass" in LauraX.DailyActions:
        $ LauraX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Chill. . .",
            "Mmm. . ."])
        ch_l "[Line]"

    if Approval >= 2:                                                                   #She's into it. . .
        if LauraX.Forced:
            $ LauraX.FaceChange("sad")
            $ LauraX.Statup("Love", 70, -3, 1)
            $ LauraX.Statup("Love", 20, -2, 1)
            $ LauraX.Statup("Obed", 90, 1)
            $ LauraX.Statup("Inbt", 60, 1)
            ch_l "If you must. . ."
        else:
            $ LauraX.FaceChange("sexy", 1)
            $ LauraX.Eyes = "closed"
            $ LauraX.Statup("Love", 90, 1)
            $ LauraX.Statup("Inbt", 50, 3)
            $ LauraX.Statup("Lust", 200, 3)
            ch_l "Mmmmm. . ."
        $ LauraX.Statup("Obed", 20, 1)
        $ LauraX.Statup("Obed", 60, 1)
        $ LauraX.Statup("Inbt", 70, 2)
        jump Laura_IA_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ LauraX.FaceChange("angry", 1)
        if "no insert ass" in LauraX.RecentActions:
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "tabno" in LauraX.DailyActions and "no insert ass" in LauraX.DailyActions:
            ch_l "I told you that wasn't appropriate!"
        elif "no insert ass" in LauraX.DailyActions:
            ch_l "Don't make me tell you again today."
        elif Taboo and "tabno" in LauraX.DailyActions:
            ch_l "I told you, not here, [LauraX.Petname]."
        elif not LauraX.InsertA:
            $ LauraX.FaceChange("perplexed", 1)
            ch_l "That's really not my style. . ."
        else:
            $ LauraX.FaceChange("bemused")
            ch_l "I'd rather not today. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no insert ass" in LauraX.DailyActions:
                $ LauraX.FaceChange("bemused")
                ch_l "It's cool, [LauraX.Petname]."
                return
            "Maybe later?" if "no insert ass" not in LauraX.DailyActions:
                $ LauraX.FaceChange("sexy")
                ch_l "It's. . . possible, [LauraX.Petname]."
                $ LauraX.Statup("Love", 80, 2)
                $ LauraX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ LauraX.RecentActions.append("tabno")
                    $ LauraX.DailyActions.append("tabno")
                $ LauraX.RecentActions.append("no insert ass")
                $ LauraX.DailyActions.append("no insert ass")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ LauraX.FaceChange("sexy")
                    $ LauraX.Statup("Obed", 90, 2)
                    $ LauraX.Statup("Obed", 50, 2)
                    ch_l "You're probably right. . ."
                    $ LauraX.Statup("Inbt", 70, 3)
                    $ LauraX.Statup("Inbt", 40, 2)
                    jump Laura_IA_Prep
                else:
                    $ LauraX.FaceChange("bemused")
                    ch_l "I don't think that I would."

            "[[Slide a finger in anyway]":                                               # Pressured into being fingered.
                $ Approval = ApprovalCheck(LauraX, 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                if Approval > 1 or (Approval and LauraX.Forced):
                    $ LauraX.FaceChange("surprised", 1)
                    $ LauraX.Statup("Love", 70, -5, 1)
                    $ LauraX.Statup("Love", 200, -2)
                    ch_l "Well hello there. . ."
                    $ LauraX.FaceChange("sad")
                    $ LauraX.Statup("Obed", 50, 4)
                    $ LauraX.Statup("Inbt", 80, 1)
                    $ LauraX.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ LauraX.Forced = 1
                    jump Laura_IA_Prep
                else:
                    $ LauraX.Statup("Love", 200, -15)
                    $ LauraX.FaceChange("angry", 1)
                    "She slaps your hand away."
                    $ LauraX.RecentActions.append("angry")
                    $ LauraX.DailyActions.append("angry")

    if "no insert ass" in LauraX.DailyActions:
        ch_l "I don't like to repeat myself, [LauraX.Petname]."
        $ LauraX.RecentActions.append("angry")
        $ LauraX.DailyActions.append("angry")
    elif LauraX.Forced:
        $ LauraX.FaceChange("angry", 1)
        ch_l "I'm not going there today."
        if ApprovalCheck(LauraX, 500, "I"):
                $ LauraX.Statup("Lust", 80, 10)
        else:
                $ LauraX.Statup("Lust", 50, 3)
        $ LauraX.Statup("Obed", 50, -2)
        $ LauraX.RecentActions.append("angry")
        $ LauraX.DailyActions.append("angry")
    elif Taboo:
        $ LauraX.FaceChange("angry", 1)
        $ LauraX.RecentActions.append("tabno")
        $ LauraX.DailyActions.append("tabno")
        ch_l "I try to stay off the radar."
    elif LauraX.InsertA:
        $ LauraX.FaceChange("sad")
        ch_l "I don't feel like it."
    else:
        $ LauraX.FaceChange("surprised")
        ch_l "Not today, [LauraX.Petname]."
        $ LauraX.FaceChange()
    $ LauraX.RecentActions.append("no insert ass")
    $ LauraX.DailyActions.append("no insert ass")
    $ temp_modifier = 0
    return


label Laura_IA_Prep: #Animation set-up
    if Trigger2 == "insert ass":
        return

    call Laura_Pussy_Launch("insert ass")

    if Situation == LauraX:
            #Laura auto-starts
            $ Situation = 0
            if (LauraX.Legs and not LauraX.Upskirt) or (LauraX.Panties and not LauraX.PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck(LauraX, 1250, TabM = 1) or (LauraX.SeenPussy and ApprovalCheck(LauraX, 500) and not Taboo):
                        $ LauraX.Upskirt = 1
                        $ LauraX.PantiesDown = 1
                        $ Line = 0
                        if LauraX.PantsNum() == 5:
                            $ Line = LauraX.Name + " hikes up her skirt"
                        elif LauraX.PantsNum() >= 6:
                            $ Line = LauraX.Name + " pulls down her " + LauraX.Legs
                        else:
                            $ Line = 0
                        if LauraX.Panties:
                            if Line:
                                #wearing pants
                                "[Line] and pulls her [LauraX.Panties] out of the way."
                                "She then grabs your arm and rubs your hand against her asshole, clearly intending you to get to work."
                            else:
                                #no pants
                                "She pulls her [LauraX.Panties] out of the way, and then rubs your hand against her asshole."
                                "She clearly intends for you to get to work."
                        else:
                            #pants but no panties
                            "[Line], and then rubs your hand against her asshole."
                            "She clearly intends for you to get to work."
                        call Laura_First_Bottomless(1)
                else:
                        "[LauraX.Name] grabs your arm and rubs your hand against her asshole, clearly intending you to get to work."
            else:
                        "[LauraX.Name] grabs your arm and rubs your hand against her asshole, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":
                    $ LauraX.Statup("Inbt", 80, 3)
                    $ LauraX.Statup("Inbt", 50, 2)
                    "You press your finger into it."
                "Praise her.":
                    $ LauraX.FaceChange("sexy", 1)
                    $ LauraX.Statup("Inbt", 80, 3)
                    ch_p "Dirty girl, [LauraX.Pet]."
                    $ LauraX.NameCheck() #checks reaction to petname
                    "You press your finger into it."
                    $ LauraX.Statup("Love", 85, 1)
                    $ LauraX.Statup("Obed", 90, 1)
                    $ LauraX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your hand back."
                    $ LauraX.FaceChange("surprised")
                    $ LauraX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that right now, [LauraX.Pet]."
                    $ LauraX.NameCheck() #checks reaction to petname
                    "[LauraX.Name] pulls back."
                    $ LauraX.Statup("Obed", 90, 1)
                    $ LauraX.Statup("Obed", 50, 1)
                    $ LauraX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ LauraX.AddWord(1,"refused","refused")
                    return
            #end auto

    if not LauraX.Forced and Situation != "auto":
        $ temp_modifier = 0
        call Bottoms_Off(LauraX)
        if "angry" in LauraX.RecentActions:
            return

    $ temp_modifier = 0
    if not LauraX.InsertA:
        if LauraX.Forced:
            $ LauraX.Statup("Love", 90, -50)
            $ LauraX.Statup("Obed", 70, 60)
            $ LauraX.Statup("Inbt", 80, 35)
        else:
            $ LauraX.Statup("Love", 90, 10)
            $ LauraX.Statup("Obed", 70, 20)
            $ LauraX.Statup("Inbt", 80, 25)

    if Taboo:
        $ LauraX.Inbt += int(Taboo/10)
        $ LauraX.Lust += int(Taboo/5)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ LauraX.DrainWord("tabno")
    $ LauraX.DrainWord("no insert ass")
    $ LauraX.RecentActions.append("insert ass")
    $ LauraX.DailyActions.append("insert ass")
    call Laura_Pussy_Launch("insert ass")

label Laura_IA_Cycle: #Repeating strokes
    while Round > 0:
        call ViewShift(LauraX,LauraX.Pose,0,"insert ass")
        call Shift_Focus(LauraX)
        $ LauraX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(LauraX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Laura_IA_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0
                        "View":
                                    call ViewShift(LauraX,"menu")
                                    jump Laura_IA_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if LauraX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ LauraX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")

                                    "Shift primary action":
                                            if LauraX.Action and MultiAction:
                                                    menu:
                                                        "Pull out and start rubbing again.":
                                                                $ Situation = "pullback"
                                                                call Laura_IA_After
                                                                call Laura_Fondle_Ass
                                                        "I want to lick your asshole.":
                                                                $ Situation = "shift"
                                                                call Laura_IA_After
                                                                call Laura_Lick_Ass
                                                        "Just start licking.":
                                                                $ Situation = "auto"
                                                                call Laura_IA_After
                                                                call Laura_Lick_Ass
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Laura_IA_After
                                                                call Laura_Dildo_Ass
                                                        "Never Mind":
                                                                jump Laura_IA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Laura_IA_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [LauraX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(LauraX)
                                            "Ask [LauraX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(LauraX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(LauraX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Laura_IA_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Laura_IA_Cycle
                                            "Never mind":
                                                        jump Laura_IA_Cycle

                                    "Show her feet" if not ShowFeet and (LauraX.Pose == "doggy" or LauraX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (LauraX.Pose == "doggy" or LauraX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [LauraX.Name]":
                                            call Girl_Undress(LauraX)
                                    "Clean up [LauraX.Name] (locked)" if not LauraX.Spunk:
                                            pass
                                    "Clean up [LauraX.Name]" if LauraX.Spunk:
                                            call Girl_Cleanup(LauraX,"ask")
                                    "Never mind":
                                            jump Laura_IA_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Laura_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Laura_IA_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Laura_Pos_Reset
                                    $ Line = 0
                                    jump Laura_IA_After
        #End menu (if Line)

        if LauraX.Panties or LauraX.PantsNum() >= 6 or LauraX.HoseNum() >= 5: #This checks if Laura wants to strip down.
                call Girl_Undress(LauraX,"auto")

        call Shift_Focus(LauraX)
        call Sex_Dialog(LauraX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or LauraX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(LauraX)
                            if "angry" in LauraX.RecentActions:
                                call Laura_Pos_Reset
                                return
                            $ LauraX.Statup("Lust", 200, 5)
                            if 100 > LauraX.Lust >= 70 and LauraX.OCount < 2:
                                $ LauraX.RecentActions.append("unsatisfied")
                                $ LauraX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Laura_IA_After
                            $ Line = "came"

                    if LauraX.Lust >= 100:
                            #If Laura can cum
                            call Girl_Cumming(LauraX)
                            if Situation == "shift" or "angry" in LauraX.RecentActions:
                                jump Laura_IA_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in LauraX.RecentActions:#And Laura is unsatisfied,
                                    "[LauraX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Laura_IA_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if LauraX.SEXP >= 100 or ApprovalCheck(LauraX, 1200, "LO"):
            pass
        elif Cnt == (5 + LauraX.InsertA):
                    $ LauraX.Brows = "confused"
                    ch_l "Ungh, you're really getting in there. . ."
        elif LauraX.Lust >= 80:
                    pass
        elif Cnt == (15 + LauraX.InsertA) and LauraX.SEXP >= 15 and not ApprovalCheck(LauraX, 1500):
                    $ LauraX.Brows = "confused"
                    menu:
                        ch_l "Maybe change things up a little?"
                        "Finish up.":
                                "You let go. . ."
                                jump Laura_IA_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Laura_IA_After
                        "No, this is fun.":
                                if ApprovalCheck(LauraX, 1200) or ApprovalCheck(LauraX, 500, "O"):
                                    $ LauraX.Statup("Love", 200, -5)
                                    $ LauraX.Statup("Obed", 50, 3)
                                    $ LauraX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ LauraX.FaceChange("angry", 1)
                                    call Laura_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_l "I'm kinda bored here."
                                    $ LauraX.Statup("Love", 50, -3, 1)
                                    $ LauraX.Statup("Love", 80, -4, 1)
                                    $ LauraX.Statup("Obed", 30, -1, 1)
                                    $ LauraX.Statup("Obed", 50, -1, 1)
                                    $ LauraX.RecentActions.append("angry")
                                    $ LauraX.DailyActions.append("angry")
                                    jump Laura_IA_After
        #End Count check

        call Escalation(LauraX) #sees if she wants to escalate things

        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [LauraX.Petname]."

    #Round = 0 loop breaks
    $ LauraX.FaceChange("bemused", 0)
    $ Line = 0
    ch_l "Ok, [LauraX.Petname], breaktime."

label Laura_IA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Laura_Pos_Reset

    $ LauraX.FaceChange("sexy")

    $ LauraX.InsertA += 1
    $ LauraX.Action -=1
    $ LauraX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ LauraX.Addictionrate += 1

    call Partner_Like(LauraX,2)

    if LauraX.InsertA == 1:
            $ LauraX.SEXP += 12
            if not Situation:
                if LauraX.Love >= 500 and "unsatisfied" not in LauraX.RecentActions:
                    ch_l "That was kinda wild. . ."
                elif LauraX.Obed <= 500 and Player.Focus <= 20:
                    $ LauraX.FaceChange("perplexed", 1)
                    ch_l "Did you enjoy that?"

    $ temp_modifier = 0
    call Checkout
    return


# end LauraX.Insert Ass /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Ass
label Laura_Lick_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(LauraX)
                                                                             # Will she let you lick? Modifiers
    if LauraX.LickA: #You've done it before
        $ temp_modifier += 20
    if LauraX.PantsNum() >= 6 or LauraX.HoseNum() >= 5: # she's got pants on.
        $ temp_modifier -= 25
    if LauraX.Lust > 95:
        $ temp_modifier += 20
    elif LauraX.Lust > 85: #She's really horny
        $ temp_modifier += 15
    if LauraX.Lust > 85 and Situation == "auto": #auto
        $ temp_modifier += 10
    if Situation == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in LauraX.Traits:
        $ temp_modifier += (4*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.Petnames:
        $ temp_modifier += 10
    elif "ex" in LauraX.Traits:
        $ temp_modifier -= 25
    if LauraX.ForcedCount and not LauraX.Forced:
        $ temp_modifier -= 5 * LauraX.ForcedCount

    if Taboo and "tabno" in LauraX.DailyActions:
        $ temp_modifier -= 10
    if Taboo and "public" not in LauraX.History:
        $ temp_modifier -= 20

    if "no lick ass" in LauraX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no lick ass" in LauraX.RecentActions else 0

    $ Approval = ApprovalCheck(LauraX, 1550, TabM = 4) # 155, 170, 185, Taboo -160(315)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ LauraX.FaceChange("surprised")
            $ LauraX.Statup("Obed", 90, 1)
            $ LauraX.Statup("Inbt", 80, 3)
            $ LauraX.Statup("Inbt", 40, 2)
            "As you crouch down and start to lick her asshole, [LauraX.Name] startles briefly, but then begins to melt."
            $ LauraX.FaceChange("sexy")
            jump Laura_LA_Prep
        else:
            $ LauraX.FaceChange("surprised")
            $ LauraX.Statup("Love", 80, -2)
            $ LauraX.Statup("Obed", 50, -3)
            ch_l "[LauraX.Petname]! No. . ."
            $ temp_modifier = 0
            $ Trigger2 = 0
            return

    if "lick ass" in LauraX.RecentActions:
        $ LauraX.FaceChange("sexy", 1)
        ch_l "Mmmm, again? I guess. . ."
        jump Laura_LA_Prep
    elif "lick ass" in LauraX.DailyActions:
        $ LauraX.FaceChange("sexy", 1)
        ch_l "You didn't get enough earlier?"


    if Approval >= 2:                                                                   #She's into it. . .
        if LauraX.Forced:
            $ LauraX.FaceChange("sad")
            $ LauraX.Statup("Love", 70, -3, 1)
            $ LauraX.Statup("Love", 20, -2, 1)
            $ LauraX.Statup("Obed", 90, 2)
            $ LauraX.Statup("Inbt", 60, 2)
            ch_l "Meh. . ."
        else:
            $ LauraX.FaceChange("sexy", 1)
            $ LauraX.Eyes = "closed"
            $ LauraX.Statup("Love", 90, 1)
            $ LauraX.Statup("Inbt", 60, 2)
            $ LauraX.Statup("Lust", 200, 3)
            ch_l "Mmm. . . naughty."
        $ LauraX.Statup("Obed", 20, 1)
        $ LauraX.Statup("Obed", 60, 1)
        $ LauraX.Statup("Inbt", 80, 2)
        jump Laura_LA_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ LauraX.FaceChange("angry", 1)
        if "no lick ass" in LauraX.RecentActions:
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "tabno" in LauraX.DailyActions and "no lick ass" in LauraX.DailyActions:
            ch_l "I told you not to touch me like that in public!"
        elif "no lick ass" in LauraX.DailyActions:
            ch_l "Don't make me tell you again today."
        elif Taboo and "tabno" in LauraX.DailyActions:
            ch_l "I told you, not here, [LauraX.Petname]."
        elif not LauraX.LickA:                    #First time dialog
            $ LauraX.FaceChange("bemused", 1)
            if LauraX.Love >= LauraX.Obed and LauraX.Love >= LauraX.Inbt:
                ch_l "Oh, we're there now?"
            elif LauraX.Obed >= LauraX.Inbt:
                ch_l "Is that what gets you off?"
            else:
                $ LauraX.Eyes = "sexy"
                ch_l "Hm, I didn't know that's what you were into."
        else:
            $ LauraX.FaceChange("bemused")
            ch_l "Not now, [LauraX.Petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no lick ass" in LauraX.DailyActions:
                $ LauraX.FaceChange("bemused")
                ch_l "It's cool, [LauraX.Petname]."
                return
            "I'm sure I can convince you later. . ." if "no lick ass" not in LauraX.DailyActions:
                $ LauraX.FaceChange("sexy")
                ch_l "Anything's possible, [LauraX.Petname]."
                $ LauraX.Statup("Love", 80, 2)
                $ LauraX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ LauraX.RecentActions.append("tabno")
                    $ LauraX.DailyActions.append("tabno")
                $ LauraX.RecentActions.append("no lick ass")
                $ LauraX.DailyActions.append("no lick ass")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ LauraX.FaceChange("sexy")
                    $ LauraX.Statup("Obed", 90, 2)
                    $ LauraX.Statup("Obed", 50, 2)
                    ch_l "Ok, you're probably right. . ."
                    $ LauraX.Statup("Inbt", 70, 3)
                    $ LauraX.Statup("Inbt", 40, 2)
                    jump Laura_LA_Prep
                else:
                    $ LauraX.FaceChange("sexy")
                    ch_l "I really don't think so."

            "[[Start licking anyway]":                                               # Pressured into being licked.
                $ Approval = ApprovalCheck(LauraX, 1100, "OI", TabM = 4) # 110, 125, 140, -160(270)
                if Approval > 1 or (Approval and LauraX.Forced):
                    $ LauraX.FaceChange("sad")
                    $ LauraX.Statup("Love", 70, -5, 1)
                    $ LauraX.Statup("Love", 200, -2)
                    ch_l "Suit yourself."
                    $ LauraX.Statup("Obed", 50, 4)
                    $ LauraX.Statup("Inbt", 80, 1)
                    $ LauraX.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ LauraX.Forced = 1
                    jump Laura_LA_Prep
                else:
                    $ LauraX.Statup("Love", 200, -15)
                    $ LauraX.FaceChange("angry", 1)
                    "She shoves your head back."
                    $ LauraX.RecentActions.append("angry")
                    $ LauraX.DailyActions.append("angry")

    if "no lick ass" in LauraX.DailyActions:
        ch_l "I don't like to repeat myself, [LauraX.Petname]."
        $ LauraX.RecentActions.append("angry")
        $ LauraX.DailyActions.append("angry")
    elif LauraX.Forced:
        $ LauraX.FaceChange("angry", 1)
        ch_l "I don't think so."
        if ApprovalCheck(LauraX, 500, "I"):
                $ LauraX.Statup("Lust", 80, 10)
        else:
                $ LauraX.Statup("Lust", 50, 3)
        $ LauraX.Statup("Obed", 50, -2)
        $ LauraX.RecentActions.append("angry")
        $ LauraX.DailyActions.append("angry")
    elif Taboo:
        $ LauraX.FaceChange("angry", 1)
        $ LauraX.RecentActions.append("tabno")
        $ LauraX.DailyActions.append("tabno")
        ch_l "I try to stay off the radar."
    elif LauraX.LickA:
        $ LauraX.FaceChange("sad")
        ch_l "Sorry, no more of that."
    else:
        $ LauraX.FaceChange("surprised")
        ch_l "I'm sorry, not now."
        $ LauraX.FaceChange()
    $ LauraX.RecentActions.append("no lick ass")
    $ LauraX.DailyActions.append("no lick ass")
    $ temp_modifier = 0
    return

label Laura_LA_Prep: #Animation set-up
    if Trigger2 == "lick ass":
        return
    if not LauraX.Forced and Situation != "auto":
        $ temp_modifier = 0
        if LauraX.PantsNum() >= 6:
            $ temp_modifier = 15
        call Bottoms_Off(LauraX)
        if "angry" in LauraX.RecentActions:
            return
    $ temp_modifier = 0
    call Laura_Pussy_Launch("lick ass")
    if not LauraX.LickA:
        if LauraX.Forced:
            $ LauraX.Statup("Love", 90, -30)
            $ LauraX.Statup("Obed", 70, 40)
            $ LauraX.Statup("Inbt", 80, 80)
        else:
            $ LauraX.Statup("Love", 90, 35)
            $ LauraX.Statup("Obed", 70, 25)
            $ LauraX.Statup("Inbt", 80, 55)
    if Taboo:
        $ LauraX.Inbt += int(Taboo/10)
        $ LauraX.Lust += int(Taboo/5)
    if Situation:
        $ renpy.pop_call()
        $ Situation = 0

    $ LauraX.Upskirt = 1
    if LauraX.PantsNum() == 5:
        $ LauraX.SeenPanties = 1
    if not LauraX.Panties:
        call Laura_First_Bottomless(1)
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ LauraX.DrainWord("tabno")
    $ LauraX.DrainWord("no lick ass")

    $ LauraX.RecentActions.append("lick") if "lick" not in LauraX.RecentActions else LauraX.RecentActions
    $ LauraX.RecentActions.append("ass") if "ass" not in LauraX.RecentActions else LauraX.RecentActions
    $ LauraX.RecentActions.append("lick ass")

    $ LauraX.DailyActions.append("lick") if "lick" not in LauraX.DailyActions else LauraX.RecentActions
    $ LauraX.DailyActions.append("ass") if "ass" not in LauraX.DailyActions else LauraX.RecentActions
    $ LauraX.DailyActions.append("lick ass")
    call Laura_Pussy_Launch("lick ass")

label Laura_LA_Cycle: #Repeating strokes
    if Trigger2 == "kiss you":
            $ Trigger2 = 0
    while Round > 0:
        call ViewShift(LauraX,LauraX.Pose,0,"lick ass")
        call Shift_Focus(LauraX)
        $ LauraX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(LauraX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Laura_LA_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0
                        "View":
                                    call ViewShift(LauraX,"menu")
                                    jump Laura_LA_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if LauraX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ LauraX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")

                                    "Shift primary action":
                                            if LauraX.Action and MultiAction:
                                                    menu:
                                                        "Switch to fondling.":
                                                                $ Situation = "pullback"
                                                                call Laura_LA_After
                                                                call Laura_Fondle_Ass
                                                        "I want to stick a finger in.":
                                                                $ Situation = "shift"
                                                                call Laura_LA_After
                                                                call Laura_Insert_Ass
                                                        "Just stick a finger in [[without asking].":
                                                                $ Situation = "auto"
                                                                call Laura_LA_After
                                                                call Laura_Insert_Ass
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Laura_LA_After
                                                                call Laura_Dildo_Ass
                                                        "Never Mind":
                                                                jump Laura_LA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Laura_LA_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [LauraX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(LauraX)
                                            "Ask [LauraX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(LauraX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(LauraX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Laura_LA_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Laura_LA_Cycle
                                            "Never mind":
                                                        jump Laura_LA_Cycle

                                    "Show her feet" if not ShowFeet and (LauraX.Pose == "doggy" or LauraX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (LauraX.Pose == "doggy" or LauraX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [LauraX.Name]":
                                            call Girl_Undress(LauraX)
                                    "Clean up [LauraX.Name] (locked)" if not LauraX.Spunk:
                                            pass
                                    "Clean up [LauraX.Name]" if LauraX.Spunk:
                                            call Girl_Cleanup(LauraX,"ask")
                                    "Never mind":
                                            jump Laura_LA_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Laura_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Laura_LA_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Laura_Pos_Reset
                                    $ Line = 0
                                    jump Laura_LA_After
        #End menu (if Line)

        if LauraX.Panties or LauraX.PantsNum() >= 6 or LauraX.HoseNum() >= 5: #This checks if Laura wants to strip down.
                call Girl_Undress(LauraX,"auto")

        call Shift_Focus(LauraX)
        call Sex_Dialog(LauraX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or LauraX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(LauraX)
                            if "angry" in LauraX.RecentActions:
                                call Laura_Pos_Reset
                                return
                            $ LauraX.Statup("Lust", 200, 5)
                            if 100 > LauraX.Lust >= 70 and LauraX.OCount < 2:
                                $ LauraX.RecentActions.append("unsatisfied")
                                $ LauraX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Laura_LA_After
                            $ Line = "came"

                    if LauraX.Lust >= 100:
                            #If Laura can cum
                            call Girl_Cumming(LauraX)
                            if Situation == "shift" or "angry" in LauraX.RecentActions:
                                jump Laura_LA_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in LauraX.RecentActions:#And Laura is unsatisfied,
                                    "[LauraX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Laura_LA_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if LauraX.SEXP >= 100 or ApprovalCheck(LauraX, 1200, "LO"):
            pass
        elif Cnt == (5 + LauraX.LickA):
                    $ LauraX.Brows = "confused"
                    ch_l "You seem to be enjoying yourself. . ."
        elif LauraX.Lust >= 80:
                    pass
        elif Cnt == (15 + LauraX.LickA) and LauraX.SEXP >= 15 and not ApprovalCheck(LauraX, 1500):
                    $ LauraX.Brows = "confused"
                    menu:
                        ch_l "[LauraX.Petname], could we try something different?"
                        "Finish up.":
                                "You let go. . ."
                                jump Laura_LA_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Laura_LA_After
                        "No, this is fun.":
                                if ApprovalCheck(LauraX, 1200) or ApprovalCheck(LauraX, 500, "O"):
                                    $ LauraX.Statup("Love", 200, -5)
                                    $ LauraX.Statup("Obed", 50, 3)
                                    $ LauraX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ LauraX.FaceChange("angry", 1)
                                    call Laura_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_l "I'm kinda bored here."
                                    $ LauraX.Statup("Love", 50, -3, 1)
                                    $ LauraX.Statup("Love", 80, -4, 1)
                                    $ LauraX.Statup("Obed", 30, -1, 1)
                                    $ LauraX.Statup("Obed", 50, -1, 1)
                                    $ LauraX.RecentActions.append("angry")
                                    $ LauraX.DailyActions.append("angry")
                                    jump Laura_LA_After
        #End Count check

        call Escalation(LauraX) #sees if she wants to escalate things

        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [LauraX.Petname]."

    #Round = 0 loop breaks
    $ LauraX.FaceChange("bemused", 0)
    $ Line = 0
    ch_l "Ok, [LauraX.Petname], breaktime."

label Laura_LA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Laura_Pos_Reset

    $ LauraX.FaceChange("sexy")

    $ LauraX.LickA += 1
    $ LauraX.Action -=1
    if LauraX.PantsNum() < 6 or LauraX.Upskirt:
        $ LauraX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ LauraX.Addictionrate += 1

    call Partner_Like(LauraX,2)

    if LauraX.LickA == 1:
            $ LauraX.SEXP += 15
            if not Situation:
                if LauraX.Love >= 500 and "unsatisfied" not in LauraX.RecentActions:
                    ch_l "That was. . . interesting."
                elif LauraX.Obed <= 500 and Player.Focus <= 20:
                    $ LauraX.FaceChange("perplexed", 1)
                    ch_l "Was that good for you?"

    $ temp_modifier = 0
    call Checkout
    return

# end LauraX.Lick Ass /////////////////////////////////////////////////////////////////////////////
