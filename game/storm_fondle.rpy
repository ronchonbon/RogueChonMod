# StormX.Fondle /////////////////////////////////////////////////////////////////////////////
label Storm_Fondle:

    $ StormX.Mouth = "smile"
    if not StormX.Action:
        call Sex_Basic_Dialog(StormX,"tired")
        return
    menu:
        ch_s "Where did you want to touch, [StormX.Petname]?"
        "Your breasts?" if StormX.Action:
                jump Storm_Fondle_Breasts
        "Your thighs?" if StormX.Action:
                jump Storm_Fondle_Thighs
        "Your pussy?" if StormX.Action:
                jump Storm_Fondle_Pussy
        "Your Ass?" if StormX.Action:
                jump Storm_Fondle_Ass
        "Never mind.":
                return
    return

# ////////////////////////////////////////////////////////////////////////Start Fondle Pussy
label Storm_Fondle_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(StormX)
                                                                                        # Will she let you fondle? Modifiers
    if StormX.FondleP: #You've done it before
        $ temp_modifier += 20
    if StormX.PantsNum() > 6 or StormX.HoseNum() >= 5: # she's got pants on.
        $ temp_modifier -= 10
    if StormX.Lust > 75: #She's really horny
        $ temp_modifier += 15
    if StormX.Lust > 75 and Situation == "auto": #She's really horny
        $ temp_modifier += 10
    if "exhibitionist" in StormX.Traits:
        $ temp_modifier += (2*Taboo)
    if StormX in Player.Harem or "sex friend" in StormX.Petnames:
        $ temp_modifier += 10
    elif "ex" in StormX.Traits:
        $ temp_modifier -= 25
    if StormX.ForcedCount and not StormX.Forced:
        $ temp_modifier -= 5 * StormX.ForcedCount

    if Taboo and "tabno" in StormX.DailyActions:
        $ temp_modifier -= 10
    if Taboo and "public" not in StormX.History:
        $ temp_modifier -= 20

    if "no fondle pussy" in StormX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no fondle pussy" in StormX.RecentActions else 0

    $ Approval = ApprovalCheck(StormX, 1050, TabM = 2) # 105, 120, 135, Taboo -80(185)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ StormX.FaceChange("sexy")
            $ StormX.Statup("Obed", 90, 1)
            $ StormX.Statup("Obed", 70, 2)
            $ StormX.Statup("Inbt", 70, 3)
            $ StormX.Statup("Inbt", 30, 2)
            "As your hand creeps up her thigh, [StormX.Name] seems a bit surprised, but then nods."
            jump Storm_FP_Prep
        else:
            $ StormX.FaceChange("surprised")
            $ StormX.Statup("Obed", 50, -2)
            ch_s "Perhaps show some control. . ."
            $ temp_modifier = 0
            $ Trigger2 = 0
            return

    if Situation == "pullback":
        $ StormX.FaceChange("surprised")
        $ StormX.Brows = "sad"
        if StormX.Lust > 80:
            $ StormX.Statup("Love", 70, -4)
        $ StormX.Statup("Obed", 90, 1)
        $ StormX.Statup("Obed", 70, 2)
        "As your hand pulls out, [StormX.Name] gasps and looks upset."
        jump Storm_FP_Prep
    elif "fondle pussy" in StormX.RecentActions:
        $ StormX.FaceChange("sexy", 1)
        ch_s "Mmmm, again? I suppose. . ."
        jump Storm_FP_Prep
    elif "fondle pussy" in StormX.DailyActions:
        $ StormX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["You did not get enough earlier?",
            "Relax, gently. . .",
            "Take it a bit gently, I am still glowing from earlier.",
            "Mmm. . ."])
        ch_s "[Line]"

    if Approval >= 2:                                                                   #She's into it. . .
        $ StormX.FaceChange("bemused", 1)
        if StormX.Forced:
            $ StormX.FaceChange("sad")
            $ StormX.Statup("Love", 70, -3, 1)
            $ StormX.Statup("Love", 20, -2, 1)
            $ StormX.Statup("Obed", 90, 1)
            $ StormX.Statup("Inbt", 60, 1)
        ch_s "Mmmm, I could not refuse. . ."
        $ StormX.Statup("Love", 90, 1)
        $ StormX.Statup("Inbt", 50, 3)
        jump Storm_FP_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ StormX.FaceChange("angry", 1)
        if "no fondle pussy" in StormX.RecentActions:
            ch_s "Your persistance is doing you no favors, [StormX.Petname]."
        elif "no fondle pussy" in StormX.DailyActions:
            ch_s "I have already told you my answer."
        elif Taboo and "tabno" in StormX.DailyActions:
            ch_s "This area is too public, [StormX.Petname]."
        elif not StormX.FondleP:
            $ StormX.FaceChange("bemused")
            ch_s "Perhaps go slower, [StormX.Petname]. . ."
        else:
            $ StormX.FaceChange("bemused")
            ch_s "Hmm, no."
        menu:
            extend ""
            "Sorry, never mind." if "no fondle pussy" in StormX.DailyActions:
                $ StormX.FaceChange("bemused")
                ch_s "I appreciate your restraint, [StormX.Petname]."
                return
            "Maybe later?" if "no fondle pussy" not in StormX.DailyActions:
                $ StormX.FaceChange("sexy")
                ch_s "I will give it some thought, [StormX.Petname]."
                $ StormX.Statup("Love", 80, 2)
                $ StormX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ StormX.RecentActions.append("tabno")
                    $ StormX.DailyActions.append("tabno")
                $ StormX.RecentActions.append("no fondle pussy")
                $ StormX.DailyActions.append("no fondle pussy")
                return
            "Come on, Please?":
                if Approval:
                    $ StormX.FaceChange("sexy")
                    $ StormX.Statup("Obed", 90, 2)
                    $ StormX.Statup("Obed", 50, 2)
                    $ StormX.Statup("Inbt", 70, 3)
                    $ StormX.Statup("Inbt", 40, 2)
                    ch_s "I suppose it could not hurt. . ."
                    jump Storm_FP_Prep
                else:
                    $ StormX.FaceChange("sexy")
                    ch_s "No."

            "[[Start fondling anyway]":                                               # Pressured into fondling.
                $ Approval = ApprovalCheck(StormX, 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                if Approval > 1 or (Approval and StormX.Forced):
                    $ StormX.FaceChange("sad")
                    $ StormX.Statup("Love", 70, -5, 1)
                    $ StormX.Statup("Love", 200, -2)
                    ch_s "Oh, if you insist. . ."
                    $ StormX.Statup("Obed", 50, 4)
                    $ StormX.Statup("Inbt", 80, 1)
                    $ StormX.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ StormX.Forced = 1
                    jump Storm_FP_Prep
                else:
                    $ StormX.Statup("Love", 200, -15)
                    $ StormX.FaceChange("angry", 1)
                    "She slaps your hand away."
                    $ StormX.RecentActions.append("angry")
                    $ StormX.DailyActions.append("angry")

    if "no fondle pussy" in StormX.DailyActions:
        ch_s "I have been clear on this."
        $ StormX.RecentActions.append("angry")
        $ StormX.DailyActions.append("angry")
    elif StormX.Forced:
        $ StormX.FaceChange("angry", 1)
        ch_s "You go too far."
        $ StormX.Statup("Lust", 70, 5)
        $ StormX.Statup("Obed", 50, -2)
        $ StormX.RecentActions.append("angry")
        $ StormX.DailyActions.append("angry")
    elif Taboo:
        $ StormX.FaceChange("angry", 1)
        $ StormX.RecentActions.append("tabno")
        $ StormX.DailyActions.append("tabno")
        ch_s "I should not be seen doing that."
    elif StormX.FondleP:
        $ StormX.FaceChange("sad")
        ch_s "No, I do not think so."
    else:
        $ StormX.FaceChange("sexy")
        $ StormX.Mouth = "sad"
        ch_s "No, I do not think so."
    $ StormX.RecentActions.append("no fondle pussy")
    $ StormX.DailyActions.append("no fondle pussy")
    $ temp_modifier = 0
    return

label Storm_FP_Prep: #Animation set-up
    if Trigger2 == "fondle pussy":
        return

    call Storm_Pussy_Launch("fondle pussy")

    if Situation == StormX:
            #Storm auto-starts
            $ Situation = 0
            if (StormX.Legs and not StormX.Upskirt) or (StormX.Panties and not StormX.PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck(StormX, 1250, TabM = 1) or (StormX.SeenPussy and ApprovalCheck(StormX, 500) and not Taboo):
                        $ StormX.Upskirt = 1
                        $ StormX.PantiesDown = 1
                        $ Line = 0
                        if StormX.PantsNum() == 5:
                            $ Line = StormX.Name + " hikes up her skirt"
                        elif StormX.PantsNum() >= 6:
                            $ Line = StormX.Name + " pulls down her " + StormX.Legs
                        else:
                            $ Line = 0
                        if StormX.Panties:
                            if Line:
                                #wearing pants
                                "[Line] and pulls her [StormX.Panties] out of the way."
                                "She then grabs your arm and then strokes your hand across her crotch, clearly intending you to get to work."
                            else:
                                #no pants
                                "She pulls her [StormX.Panties] out of the way, and then strokes your hand across her crotch."
                                "She clearly intends for you to get to work."
                        else:
                                #pants but no panties
                                "[Line], and then strokes your hand across her crotch."
                                "She clearly intends for you to get to work."
                        call Storm_First_Bottomless(1)
                else:
                        "[StormX.Name] grabs your arm and strokes your hand across her crotch, clearly intending you to get to work."
            else:
                        "[StormX.Name] grabs your arm and strokes your hand across her crotch, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":
                    $ StormX.Statup("Inbt", 80, 3)
                    $ StormX.Statup("Inbt", 50, 2)
                    "You start to run your fingers along her pussy."
                "Praise her.":
                    $ StormX.FaceChange("sexy", 1)
                    $ StormX.Statup("Inbt", 80, 3)
                    ch_p "I like the initiative, [StormX.Pet]."
                    $ StormX.NameCheck() #checks reaction to petname
                    "You start to run your fingers along her pussy."
                    $ StormX.Statup("Love", 85, 1)
                    $ StormX.Statup("Obed", 90, 1)
                    $ StormX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your hand back."
                    $ StormX.FaceChange("surprised")
                    $ StormX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that right now, [StormX.Pet]."
                    $ StormX.NameCheck() #checks reaction to petname
                    "[StormX.Name] pulls back."
                    $ StormX.Statup("Obed", 90, 1)
                    $ StormX.Statup("Obed", 50, 1)
                    $ StormX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ StormX.AddWord(1,"refused","refused")
                    return
            #end auto

    if not StormX.Forced and Situation != "auto":
        $ temp_modifier = 0
        call Bottoms_Off(StormX)
        if "angry" in StormX.RecentActions:
            return
    $ temp_modifier = 0

    if not StormX.FondleP:
        if StormX.Forced:
            $ StormX.Statup("Love", 90, -50)
            $ StormX.Statup("Obed", 70, 35)
            $ StormX.Statup("Inbt", 80, 25)
        else:
            $ StormX.Statup("Love", 90, 10)
            $ StormX.Statup("Obed", 70, 10)
            $ StormX.Statup("Inbt", 80, 15)
    if Taboo:
        $ StormX.Inbt += int(Taboo/10)
        $ StormX.Lust += int(Taboo/5)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ StormX.DrainWord("tabno")
    $ StormX.DrainWord("no fondle pussy")
    $ StormX.RecentActions.append("fondle pussy")
    $ StormX.DailyActions.append("fondle pussy")
    call Storm_Pussy_Launch("fondle pussy")

    $ Speed = 1

label Storm_FP_Cycle: #Repeating strokes
    while Round > 0:
        call ViewShift(StormX,StormX.Pose,0,"fondle pussy")
        call Shift_Focus(StormX)
        $ StormX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "I want to stick a finger in. . ." if Speed != 2:
                                if StormX.InsertP:
                                    $ Speed = 2
                                else:
                                    menu:
                                        "Ask her first":
                                            $ Situation = "shift"
                                        "Don't ask first [[just stick it in]":
                                            $ Situation = "auto"
                                    call Storm_Insert_Pussy

                        "Pull back a bit. . ." if Speed == 2:
                                    $ Speed = 0

                        "Slap her ass":
                                    call Slap_Ass(StormX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Storm_FP_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0
                        "View":
                                    call ViewShift(StormX,"menu")
                                    jump Storm_FP_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if StormX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ StormX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(StormX,"tired")

                                    "Shift primary action":
                                            if StormX.Action and MultiAction:
                                                    menu:
                                                        "I want to lick your pussy.":
                                                                $ Situation = "shift"
                                                                call Storm_FP_After
                                                                call Storm_Lick_Pussy
                                                        "Just start licking":
                                                                $ Situation = "auto"
                                                                call Storm_FP_After
                                                                call Storm_Lick_Pussy
                                                        "Pull back to the thighs":
                                                                $ Situation = "pullback"
                                                                call Storm_FP_After
                                                                call Storm_Fondle_Thighs
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Storm_FP_After
                                                                call Storm_Dildo_Pussy
                                                        "Never Mind":
                                                                jump Storm_FP_Cycle
                                            else:
                                                call Sex_Basic_Dialog(StormX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Storm_FP_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [StormX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(StormX)
                                            "Asks [StormX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(StormX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(StormX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Storm_FP_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Storm_FP_Cycle
                                            "Never mind":
                                                        jump Storm_FP_Cycle

                                    "Show her feet" if not ShowFeet and (StormX.Pose == "doggy" or StormX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (StormX.Pose == "doggy" or StormX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [StormX.Name]":
                                            call Girl_Undress(StormX)
                                    "Clean up [StormX.Name] (locked)" if not StormX.Spunk:
                                            pass
                                    "Clean up [StormX.Name]" if StormX.Spunk:
                                            call Girl_Cleanup(StormX,"ask")
                                    "Never mind":
                                            jump Storm_FP_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Storm_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Storm_FP_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Storm_Pos_Reset
                                    $ Line = 0
                                    jump Storm_FP_After
        #End menu (if Line)

        call Shift_Focus(StormX)
        call Sex_Dialog(StormX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or StormX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(StormX)
                            if "angry" in StormX.RecentActions:
                                call Storm_Pos_Reset
                                return
                            $ StormX.Statup("Lust", 200, 5)
                            if 100 > StormX.Lust >= 70 and StormX.OCount < 2:
                                $ StormX.RecentActions.append("unsatisfied")
                                $ StormX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Storm_FP_After
                            $ Line = "came"

                    if StormX.Lust >= 100:
                            #If [StormX.Name] can cum
                            call Girl_Cumming(StormX)
                            if Situation == "shift" or "angry" in StormX.RecentActions:
                                jump Storm_FP_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in StormX.RecentActions:#And [StormX.Name] is unsatisfied,
                                    "[StormX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Storm_FP_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if StormX.SEXP >= 100 or ApprovalCheck(StormX, 1200, "LO"):
            pass
        elif Cnt == (5 + StormX.FondleP):
                    $ StormX.Brows = "confused"
                    ch_s "Mmmm, yes. . . deeper. . ."
        elif StormX.Lust >= 80:
                    pass
        elif Cnt == (15 + StormX.FondleP) and StormX.SEXP >= 15 and not ApprovalCheck(StormX, 1500):
                    $ StormX.Brows = "confused"
                    menu:
                        ch_s "I am sure that is fun, but could we try something different?"
                        "Finish up.":
                                "You let go. . ."
                                jump Storm_FP_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Storm_FP_After
                        "No, this is fun.":
                                if ApprovalCheck(StormX, 1200) or ApprovalCheck(StormX, 500, "O"):
                                    $ StormX.Statup("Love", 200, -5)
                                    $ StormX.Statup("Obed", 50, 3)
                                    $ StormX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ StormX.FaceChange("angry", 1)
                                    call Storm_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_s "Well however much you are enjoying yourself, I need to take a break."
                                    $ StormX.Statup("Love", 50, -3, 1)
                                    $ StormX.Statup("Love", 80, -4, 1)
                                    $ StormX.Statup("Obed", 30, -1, 1)
                                    $ StormX.Statup("Obed", 50, -1, 1)
                                    $ StormX.RecentActions.append("angry")
                                    $ StormX.DailyActions.append("angry")
                                    jump Storm_FP_After
        #End Count check

        if Round == 10:
                call Sex_Basic_Dialog(StormX,10) #"It is getting late, [Girl.Petname]. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(StormX,5)   #"We should take a break soon."

    #Round = 0 loop breaks
    $ StormX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(StormX,"done") # ch_s "I need to take a moment to collect myself."

label Storm_FP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Storm_Pos_Reset

    $ StormX.FaceChange("sexy")

    $ StormX.FondleP += 1
    $ StormX.Action -=1
    if StormX.PantsNum() <= 6 or StormX.Upskirt:
        $ StormX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ StormX.Addictionrate += 1

    call Partner_Like(StormX,2)

    if StormX.FondleP == 1:
            $ StormX.SEXP += 7
            if not Situation:
                if StormX.Love >= 500 and "unsatisfied" not in StormX.RecentActions:
                    ch_s "You certainly. . . reached some interesting places there. . ."
                elif StormX.Obed <= 500 and Player.Focus <= 20:
                    $ StormX.FaceChange("perplexed", 1)
                    ch_s "Did you enjoy that?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_s "Oh? What did you have in mind?"
    call Checkout
    return

# end StormX.Fondle Pussy /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy
label Storm_Insert_Pussy:
    call Shift_Focus(StormX)
    if Situation == "auto":                                                                  #You auto-start
        if ApprovalCheck(StormX, 1100, TabM = 2):
            $ StormX.FaceChange("surprised")
            $ StormX.Statup("Obed", 90, 1)
            $ StormX.Statup("Obed", 70, 2)
            $ StormX.Statup("Inbt", 70, 3)
            $ StormX.Statup("Inbt", 30, 2)
            "As you slide a finger in, [StormX.Name] seems a bit surprised, but seems into it."
            jump Storm_IP_Prep
        else:
            $ StormX.FaceChange("surprised",2)
            $ StormX.Statup("Love", 80, -2)
            $ StormX.Statup("Obed", 50, -3)
            ch_s "Oooh!"
            "She slaps your hand back."
            $ StormX.FaceChange("perplexed",1)
            ch_s "Careful what you put in there, you may not get it back."
            return

    if ApprovalCheck(StormX, 1100, TabM = 2):                                                                   #She's into it. . .
        if StormX.Forced:
            $ StormX.FaceChange("sad")
            $ StormX.Statup("Love", 70, -3, 1)
            $ StormX.Statup("Love", 20, -2, 1)
            $ StormX.Statup("Obed", 90, 1)
            $ StormX.Statup("Inbt", 60, 1)
            ch_s "If you must. . ."
        else:
            $ StormX.FaceChange("sexy", 1)
            $ StormX.Statup("Love", 90, 1)
            $ StormX.Statup("Inbt", 50, 3)
            ch_s "Mmmmmm. . ."
        $ StormX.Statup("Obed", 20, 1)
        $ StormX.Statup("Obed", 60, 1)
        $ StormX.Statup("Inbt", 70, 2)
        jump Storm_IP_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ StormX.FaceChange("bemused", 2)
        ch_s "No. Thank you."
        $ StormX.Blush = 1
    return


label Storm_IP_Prep: #Animation set-up
    if not StormX.InsertP:
        $ StormX.InsertP = 1
        $ StormX.SEXP += 10
        if StormX.Forced:
            $ StormX.Statup("Love", 90, -60)
            $ StormX.Statup("Obed", 70, 55)
            $ StormX.Statup("Inbt", 80, 35)
        else:
            $ StormX.Statup("Love", 90, 10)
            $ StormX.Statup("Obed", 70, 20)
            $ StormX.Statup("Inbt", 80, 25)

    if not StormX.Forced and Situation != "auto":
        call Girl_Undress(StormX,"bottom")
        if "angry" in StormX.RecentActions:
            return

#    call Storm_Pussy_Launch("insert pussy")
    if Taboo:
        $ StormX.Inbt += int(Taboo/10)
        $ StormX.Lust += int(Taboo/5)

    $ Line = 0
    $ Speed = 2
    return

# end StormX.Insert Pussy /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Pussy
label Storm_Lick_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(StormX)
                                                                                  # Will she let you fondle? Modifiers
    if StormX.LickP: #You've done it before
        $ temp_modifier += 15
    if StormX.PantsNum() > 6 or StormX.HoseNum() >= 5: # she's got pants on.
        $ temp_modifier -= 15
    if StormX.Lust > 95:
        $ temp_modifier += 20
    elif StormX.Lust > 85: #She's really horny
        $ temp_modifier += 15
    if Situation == "shift":
        $ temp_modifier += 10
    if StormX.Lust > 85 and Situation == "auto": #She's really horny
        $ temp_modifier += 10
    if "exhibitionist" in StormX.Traits:
        $ temp_modifier += (4*Taboo)
    if StormX in Player.Harem or "sex friend" in StormX.Petnames:
        $ temp_modifier += 10
    elif "ex" in StormX.Traits:
        $ temp_modifier -= 25
    if StormX.ForcedCount and not StormX.Forced:
        $ temp_modifier -= 5 * StormX.ForcedCount

    if Taboo and "tabno" in StormX.DailyActions:
        $ temp_modifier -= 10
    if Taboo and "public" not in StormX.History:
        $ temp_modifier -= 20

    if "no lick pussy" in StormX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no lick pussy" in StormX.RecentActions else 0

    $ Approval = ApprovalCheck(StormX, 1250, TabM = 4) # 125, 140, 155, Taboo -160(285)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ StormX.FaceChange("surprised")
            $ StormX.Statup("Obed", 90, 1)
            $ StormX.Statup("Obed", 70, 2)
            $ StormX.Statup("Inbt", 70, 3)
            $ StormX.Statup("Inbt", 30, 2)
            "As you crouch down and start to lick her pussy, [StormX.Name] jumps, but then softens."
            $ StormX.FaceChange("sexy")
            jump Storm_LP_Prep
        else:
            $ StormX.FaceChange("surprised")
            $ StormX.Statup("Love", 80, -2)
            $ StormX.Statup("Obed", 50, -3)
            ch_s "I appreciate the intent, but this is not the time for it."
            $ StormX.FaceChange("perplexed",1)
            "She pushes your head back away from her."
            $ temp_modifier = 0
            $ Trigger2 = 0
            return

    if "lick pussy" in StormX.RecentActions:
        $ StormX.FaceChange("sexy", 1)
        ch_s "Mmmm, again? I suppose. . ."
        jump Storm_LP_Prep
    elif "lick pussy" in StormX.DailyActions:
        $ StormX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Huh? Again?",
            "I must have done something right.",
            "What a queen deserves. . .",
            "Mmm. . ."])
        ch_s "[Line]"

    if Approval >= 2:                                                                   #She's into it. . .
        if StormX.Forced:
            $ StormX.FaceChange("sad")
            $ StormX.Statup("Love", 70, -3, 1)
            $ StormX.Statup("Love", 20, -2, 1)
            $ StormX.Statup("Obed", 90, 1)
            $ StormX.Statup("Inbt", 60, 1)
            ch_s "If you must. . ."
        else:
            $ StormX.FaceChange("sexy", 1)
            $ StormX.Eyes = "closed"
            $ StormX.Statup("Love", 90, 1)
            $ StormX.Statup("Inbt", 50, 3)
            $ StormX.Statup("Lust", 200, 3)
            ch_s "Mmmmmm. . ."
        $ StormX.Statup("Obed", 20, 1)
        $ StormX.Statup("Obed", 60, 1)
        $ StormX.Statup("Inbt", 70, 2)
        jump Storm_LP_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ StormX.FaceChange("angry", 1)
        if "no lick pussy" in StormX.RecentActions:
            ch_s "Do not persist in this, [StormX.Petname]."
        elif Taboo and "tabno" in StormX.DailyActions and "no lick pussy" in StormX.DailyActions:
            ch_s "You already got your answer!"
        elif "no lick pussy" in StormX.DailyActions:
            ch_s "I believe you know my answer on this matter."
        elif Taboo and "tabno" in StormX.DailyActions:
            ch_s "This area is too public, [StormX.Petname]."
        elif not StormX.LickP:
            $ StormX.FaceChange("bemused")
            ch_s "Oh, that would. . .perhaps not, [StormX.Petname]. . ."
        else:
            $ StormX.FaceChange("bemused")
            ch_s "I would be uncomfortable with that. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no lick pussy" in StormX.DailyActions:
                $ StormX.FaceChange("bemused")
                ch_s "I appreciate your restraint, [StormX.Petname]."
                return
            "I'm sure I can convince you later. . ." if "no lick pussy" not in StormX.DailyActions:
                $ StormX.FaceChange("sexy")
                ch_s "I will give it some thought, [StormX.Petname]."
                $ StormX.Statup("Love", 80, 2)
                $ StormX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ StormX.RecentActions.append("tabno")
                    $ StormX.DailyActions.append("tabno")
                $ StormX.RecentActions.append("no lick pussy")
                $ StormX.DailyActions.append("no lick pussy")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ StormX.FaceChange("sexy")
                    $ StormX.Statup("Obed", 90, 2)
                    $ StormX.Statup("Obed", 50, 2)
                    ch_s "I. . . would. . ."
                    $ StormX.Statup("Inbt", 70, 3)
                    $ StormX.Statup("Inbt", 40, 2)
                    jump Storm_LP_Prep
                else:
                    $ StormX.FaceChange("sexy")
                    ch_s "I would, but still no, [StormX.Petname]."

            "[[Get in there anyway]":                                               # Pressured into being licked.
                $ Approval = ApprovalCheck(StormX, 750, "OI", TabM = 4) # 75, 90, 105, -160(235)
                if Approval > 1 or (Approval and StormX.Forced):
                    $ StormX.FaceChange("sad")
                    $ StormX.Statup("Love", 70, -5, 1)
                    $ StormX.Statup("Love", 200, -2)
                    ch_s "If you insist. . ."
                    $ StormX.Statup("Obed", 50, 4)
                    $ StormX.Statup("Inbt", 80, 1)
                    $ StormX.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ StormX.Forced = 1
                    jump Storm_LP_Prep
                else:
                    $ StormX.Statup("Love", 200, -15)
                    $ StormX.FaceChange("angry", 1)
                    "She shoves your head back."
                    $ StormX.RecentActions.append("angry")
                    $ StormX.DailyActions.append("angry")

    if "no lick pussy" in StormX.DailyActions:
        ch_s "I have been clear on this."
        $ StormX.RecentActions.append("angry")
        $ StormX.DailyActions.append("angry")
    elif StormX.Forced:
        $ StormX.FaceChange("angry", 1)
        ch_s "You go too far."
        $ StormX.Statup("Lust", 80, 5)
        $ StormX.Statup("Obed", 50, -2)
        $ StormX.RecentActions.append("angry")
        $ StormX.DailyActions.append("angry")
    elif Taboo:
        $ StormX.FaceChange("angry", 1)
        $ StormX.RecentActions.append("tabno")
        $ StormX.DailyActions.append("tabno")
        ch_s "I should not be seen doing that."
    elif StormX.LickP:
        $ StormX.FaceChange("sad")
        ch_s "No, I do not think so."
    else:
        $ StormX.FaceChange("surprised")
        ch_s "No, I do not think so."
        $ StormX.FaceChange()
    $ StormX.RecentActions.append("no lick pussy")
    $ StormX.DailyActions.append("no lick pussy")
    $ temp_modifier = 0
    return

label Storm_LP_Prep: #Animation set-up
    if Trigger2 == "lick pussy": #fix pull down pants now an option, make it work
        return

    call Storm_Pussy_Launch("lick pussy")

    if Situation == StormX:
            #Storm auto-starts
            $ Situation = 0
            if (StormX.Legs and not StormX.Upskirt) or (StormX.Panties and not StormX.PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck(StormX, 1250, TabM = 1) or (StormX.SeenPussy and ApprovalCheck(StormX, 500) and not Taboo):
                        $ StormX.Upskirt = 1
                        $ StormX.PantiesDown = 1
                        $ Line = 0
                        if StormX.PantsNum() == 5:
                            $ Line = StormX.Name + " hikes up her skirt"
                        elif StormX.PantsNum() >= 6:
                            $ Line = StormX.Name + " pulls down her " + StormX.Legs
                        else:
                            $ Line = 0
                        if StormX.Panties:
                            if Line:
                                #wearing pants
                                "[Line] and pulls her [StormX.Panties] out of the way."
                                "She then grabs your head and pulls it to her crotch, clearly intending you to get to work."
                            else:
                                #no pants
                                "She pulls her [StormX.Panties] out of the way, and then shoves your face into her crotch."
                                "She clearly intends for you to get to work."
                        else:
                                #pants but no panties
                                "[Line], and then shoves your face into her crotch."
                                "She clearly intends for you to get to work."
                        call Storm_First_Bottomless(1)
                else:
                        "[StormX.Name] grabs your head and pulls it to her crotch, clearly intending you to get to work."
            else:
                        "[StormX.Name] grabs your head and pulls it to her crotch, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":
                    $ StormX.Statup("Inbt", 80, 3)
                    $ StormX.Statup("Inbt", 50, 2)
                    "You start licking."
                "Praise her.":
                    $ StormX.FaceChange("sexy", 1)
                    $ StormX.Statup("Inbt", 80, 3)
                    ch_p "Mmm, I like this idea, [StormX.Pet]."
                    $ StormX.NameCheck() #checks reaction to petname
                    "You start licking."
                    $ StormX.Statup("Love", 85, 1)
                    $ StormX.Statup("Obed", 90, 1)
                    $ StormX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your head away."
                    $ StormX.FaceChange("surprised")
                    $ StormX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that right now, [StormX.Pet]."
                    $ StormX.NameCheck() #checks reaction to petname
                    "[StormX.Name] pulls back."
                    $ StormX.Statup("Obed", 90, 1)
                    $ StormX.Statup("Obed", 50, 1)
                    $ StormX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ StormX.AddWord(1,"refused","refused")
                    return
            #end auto

    if not StormX.Forced and Situation != "auto":
        $ temp_modifier = 0
        if StormX.PantsNum() > 6:
            $ temp_modifier = 15
        call Bottoms_Off(StormX)
        if "angry" in StormX.RecentActions:
            return

    $ temp_modifier = 0
    if not StormX.LickP:
        if StormX.Forced:
            $ StormX.Statup("Love", 90, -30)
            $ StormX.Statup("Obed", 70, 35)
            $ StormX.Statup("Inbt", 80, 75)
        else:
            $ StormX.Statup("Love", 90, 35)
            $ StormX.Statup("Obed", 70, 15)
            $ StormX.Statup("Inbt", 80, 35)
    if Taboo:
        $ StormX.Inbt += int(Taboo/10)
        $ StormX.Lust += int(Taboo/5)
    if Situation:
        $ renpy.pop_call()
        $ Situation = 0

    if StormX.PantsNum() == 5:
        $ StormX.Upskirt = 1
        $ StormX.SeenPanties = 1
    call Storm_First_Bottomless(1)

    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ StormX.DrainWord("tabno")
    $ StormX.DrainWord("no lick pussy")
    $ StormX.RecentActions.append("lick pussy")
    $ StormX.DailyActions.append("lick pussy")
    call Storm_Pussy_Launch("lick pussy")

label Storm_LP_Cycle: #Repeating strokes
    if Trigger2 == "kiss you":
            $ Trigger2 = 0
    while Round > 0:
        call ViewShift(StormX,StormX.Pose,0,"lick pussy")
        call Shift_Focus(StormX)
        $ StormX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(StormX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Storm_LP_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0
                        "View":
                                    call ViewShift(StormX,"menu")
                                    jump Storm_LP_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if StormX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ StormX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(StormX,"tired")

                                    "Shift primary action":
                                            if StormX.Action and MultiAction:
                                                    menu:
                                                        "Pull out and start rubbing again.":
                                                                if StormX.Action and MultiAction:
                                                                    $ Situation = "pullback"
                                                                    call Storm_LP_After
                                                                    call Storm_Fondle_Pussy
                                                                else:
                                                                    call Sex_Basic_Dialog(StormX,"tired")
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Storm_LP_After
                                                                call Storm_Dildo_Pussy
                                                        "Never Mind":
                                                                jump Storm_LP_Cycle
                                            else:
                                                call Sex_Basic_Dialog(StormX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Storm_LP_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [StormX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(StormX)
                                            "Asks [StormX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(StormX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(StormX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Storm_LP_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Storm_LP_Cycle
                                            "Never mind":
                                                        jump Storm_LP_Cycle

                                    "Show her feet" if not ShowFeet and (StormX.Pose == "doggy" or StormX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (StormX.Pose == "doggy" or StormX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [StormX.Name]":
                                            call Girl_Undress(StormX)
                                    "Clean up [StormX.Name] (locked)" if not StormX.Spunk:
                                            pass
                                    "Clean up [StormX.Name]" if StormX.Spunk:
                                            call Girl_Cleanup(StormX,"ask")
                                    "Never mind":
                                            jump Storm_LP_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Storm_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Storm_LP_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Storm_Pos_Reset
                                    $ Line = 0
                                    jump Storm_LP_After
        #End menu (if Line)

        if StormX.Panties or StormX.PantsNum() > 6 or StormX.HoseNum() >= 5: #This checks if [StormX.Name] wants to strip down.
                call Girl_Undress(StormX,"auto")

        call Shift_Focus(StormX)
        call Sex_Dialog(StormX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or StormX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(StormX)
                            if "angry" in StormX.RecentActions:
                                call Storm_Pos_Reset
                                return
                            $ StormX.Statup("Lust", 200, 5)
                            if 100 > StormX.Lust >= 70 and StormX.OCount < 2:
                                $ StormX.RecentActions.append("unsatisfied")
                                $ StormX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Storm_LP_After
                            $ Line = "came"

                    if StormX.Lust >= 100:
                            #If [StormX.Name] can cum
                            call Girl_Cumming(StormX)
                            if Situation == "shift" or "angry" in StormX.RecentActions:
                                jump Storm_LP_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in StormX.RecentActions:#And [StormX.Name] is unsatisfied,
                                    "[StormX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Storm_LP_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if StormX.SEXP >= 100 or ApprovalCheck(StormX, 1200, "LO"):
            pass
        elif Cnt == (5 + StormX.LickP):
                    $ StormX.Brows = "confused"
                    ch_s "Oh, that is delightful. . ."
        elif StormX.Lust >= 80:
                    pass
        elif Cnt == (15 + StormX.LickP) and StormX.SEXP >= 15 and not ApprovalCheck(StormX, 1500):
                    $ StormX.Brows = "confused"
                    menu:
                        ch_s "I am sure that is fun, but could we try something different?"
                        "Finish up.":
                                "You let go. . ."
                                jump Storm_LP_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Storm_LP_After
                        "No, this is fun.":
                                if ApprovalCheck(StormX, 1200) or ApprovalCheck(StormX, 500, "O"):
                                    $ StormX.Statup("Love", 200, -5)
                                    $ StormX.Statup("Obed", 50, 3)
                                    $ StormX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ StormX.FaceChange("angry", 1)
                                    call Storm_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_s "Well however much you are enjoying yourself, I need to take a break."
                                    $ StormX.Statup("Love", 50, -3, 1)
                                    $ StormX.Statup("Love", 80, -4, 1)
                                    $ StormX.Statup("Obed", 30, -1, 1)
                                    $ StormX.Statup("Obed", 50, -1, 1)
                                    $ StormX.RecentActions.append("angry")
                                    $ StormX.DailyActions.append("angry")
                                    jump Storm_LP_After
        #End Count check

        call Escalation(StormX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(StormX,10) #"It is getting late, [Girl.Petname]. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(StormX,5)   #"We should take a break soon."

    #Round = 0 loop breaks
    $ StormX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(StormX,"done") # ch_s "I need to take a moment to collect myself."

label Storm_LP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Storm_Pos_Reset

    $ StormX.FaceChange("sexy")

    $ StormX.LickP += 1
    $ StormX.Action -=1
    if StormX.PantsNum() <= 6 or StormX.Upskirt:
        $ StormX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ StormX.Addictionrate += 1

    call Partner_Like(StormX,3,2)

    if StormX.LickP == 1:
            $ StormX.SEXP += 10
            if not Situation:
                if StormX.Love >= 500 and "unsatisfied" not in StormX.RecentActions:
                    ch_s "You really do have  atalent for that. . ."
                elif StormX.Obed <= 500 and Player.Focus <= 20:
                    $ StormX.FaceChange("perplexed", 1)
                    ch_s "That was not so bad. . ."

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_s "Oh? What did you have in mind?"
    call Checkout
    return


# end StormX.Lick Pussy /////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////Start Fondle Ass
label Storm_Fondle_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(StormX)
                                                                                     # Will she let you fondle? Modifiers
    if StormX.FondleA: #You've done it before
        $ temp_modifier += 10
    if StormX.PantsNum() > 6 or StormX.HoseNum() >= 5: # she's got pants on.
        $ temp_modifier -= 5
    if StormX.Lust > 75: #She's really horny
        $ temp_modifier += 15
    if "exhibitionist" in StormX.Traits:
        $ temp_modifier += Taboo
    if StormX in Player.Harem or "sex friend" in StormX.Petnames:
        $ temp_modifier += 10
    elif "ex" in StormX.Traits:
        $ temp_modifier -= 25
    if StormX.ForcedCount and not StormX.Forced:
        $ temp_modifier -= 5 * StormX.ForcedCount

    if Taboo and "tabno" in StormX.DailyActions:
        $ temp_modifier -= 10
    if Taboo and "public" not in StormX.History:
        $ temp_modifier -= 20

    if "no fondle ass" in StormX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no fondle ass" in StormX.RecentActions else 0

    $ Approval = ApprovalCheck(StormX, 750, TabM=1) # 85, 100, 115, Taboo -40(125)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ StormX.FaceChange("surprised", 1)
            $ StormX.Statup("Obed", 70, 2)
            $ StormX.Statup("Inbt", 40, 2)
            "As your hand creeps down her backside, [StormX.Name] jumps a bit, and then relaxes."
            $ StormX.FaceChange("sexy")
            jump Storm_FA_Prep
        else:
            $ StormX.FaceChange("surprised")
            $ StormX.Statup("Obed", 50, -3)
            ch_s "Release me, [StormX.Petname]."
            $ StormX.FaceChange("bemused")
            $ temp_modifier = 0
            $ Trigger2 = 0
            return

    if Situation == "pullback":
        $ StormX.FaceChange("surprised")
        $ StormX.Brows = "sad"
        if StormX.Lust > 80:
            $ StormX.Statup("Love", 70, -4)
        $ StormX.Statup("Obed", 90, 1)
        $ StormX.Statup("Obed", 70, 2)
        "As your finger slides out, [StormX.Name] gasps and looks upset."
        jump Storm_FA_Prep
    elif "fondle ass" in StormX.RecentActions:
        $ StormX.FaceChange("sexy", 1)
        ch_s "Mmmm, again? I suppose. . ."
        jump Storm_FA_Prep
    elif "fondle ass" in StormX.DailyActions:
        $ StormX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Perhaps not so rough this time?",
            "Mmm. . ."])
        ch_s "[Line]"

    if Approval >= 2:                                                                   #She's into it. . .
        if StormX.Forced:
            $ StormX.FaceChange("sad")
            $ StormX.Statup("Love", 70, -2, 1)
            $ StormX.Statup("Obed", 90, 2)
            $ StormX.Statup("Inbt", 60, 2)
            ch_s "If you insist. . ."
        else:
            $ StormX.FaceChange("bemused, 1")
            ch_s "I suppose that is reasonable. . ."
        $ StormX.Statup("Lust", 200, 3)
        $ StormX.Statup("Obed", 60, 1)
        $ StormX.Statup("Inbt", 70, 1)
        jump Storm_FA_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ StormX.FaceChange("angry", 1)
        if "no fondle ass" in StormX.RecentActions:
            ch_s "Your persistance is doing you no favors, [StormX.Petname]."
        elif "no fondle ass" in StormX.DailyActions:
            ch_s "I have already told you my answer."
        elif Taboo and "tabno" in StormX.DailyActions:
            ch_s "This area is too public, [StormX.Petname]."
        elif not StormX.FondleA:
            $ StormX.FaceChange("bemused")
            ch_s "I would rather not, [StormX.Petname]. . ."
        else:
            $ StormX.FaceChange("bemused")
            ch_s "Not now, [StormX.Petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no fondle ass" in StormX.DailyActions:
                $ StormX.FaceChange("bemused")
                ch_s "I appreciate your restraint, [StormX.Petname]."
                return
            "Maybe later?" if "no fondle ass" not in StormX.DailyActions:
                $ StormX.FaceChange("sexy")
                ch_s "I will give it some thought, [StormX.Petname]."
                $ StormX.Statup("Love", 80, 2)
                $ StormX.Statup("Inbt", 50, 2)
                if Taboo:
                    $ StormX.RecentActions.append("tabno")
                    $ StormX.DailyActions.append("tabno")
                $ StormX.RecentActions.append("no fondle ass")
                $ StormX.DailyActions.append("no fondle ass")
                return
            "Just one good squeeze?":
                if Approval:
                    $ StormX.FaceChange("sexy")
                    $ StormX.Statup("Obed", 90, 1)
                    $ StormX.Statup("Obed", 50, 2)
                    ch_s "Well, one could not hurt. . ."
                    $ StormX.Statup("Inbt", 70, 1)
                    $ StormX.Statup("Inbt", 40, 2)
                    jump Storm_FA_Prep
                else:
                    $ StormX.FaceChange("sexy")
                    ch_s "No."

            "[[Start fondling anyway]":                                               # Pressured into fondling.
                $ Approval = ApprovalCheck(StormX, 250, "OI", TabM = 3) # 25, 40, 55, -120(145)
                if Approval > 1 or (Approval and StormX.Forced):
                    $ StormX.FaceChange("sad")
                    $ StormX.Statup("Love", 70, -3, 1)
                    $ StormX.Statup("Love", 200, -1)
                    ch_s ". . . I suppose."
                    $ StormX.Statup("Obed", 50, 3)
                    $ StormX.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ StormX.Forced = 1
                    jump Storm_FA_Prep
                else:
                    $ StormX.Statup("Love", 200, -10)
                    $ StormX.FaceChange("angry", 1)
                    "She slaps your hand away."
                    $ StormX.RecentActions.append("angry")
                    $ StormX.DailyActions.append("angry")

    if "no fondle ass" in StormX.DailyActions:
        ch_s "I have been clear on this."
        $ StormX.RecentActions.append("angry")
        $ StormX.DailyActions.append("angry")
    elif StormX.Forced:
        $ StormX.FaceChange("angry", 1)
        ch_s "You go too far."
        $ StormX.Statup("Lust", 60, 5)
        $ StormX.Statup("Obed", 50, -2)
        $ StormX.RecentActions.append("angry")
        $ StormX.DailyActions.append("angry")
    elif Taboo:
        $ StormX.FaceChange("angry", 1)
        $ StormX.RecentActions.append("tabno")
        $ StormX.DailyActions.append("tabno")
        ch_s "I should not be seen doing that."
    elif StormX.FondleA:
        $ StormX.FaceChange("sad")
        ch_s "No, I do not think so."
    else:
        $ StormX.FaceChange("sexy")
        $ StormX.Mouth = "sad"
        ch_s "No, I do not think so."
    $ StormX.RecentActions.append("no fondle ass")
    $ StormX.DailyActions.append("no fondle ass")
    $ temp_modifier = 0
    return

ch_s "Sorry, I don't even know how I got here. . ."
return

label Storm_FA_Prep: #Animation set-up
    if Trigger2 == "fondle ass":
        return
    if not StormX.Forced and Situation != "auto":
        $ temp_modifier = 0
        call Bottoms_Off(StormX)
        if "angry" in StormX.RecentActions:
            return
    $ temp_modifier = 0
    call Storm_Pussy_Launch("fondle ass")
    if not StormX.FondleA:
        if StormX.Forced:
            $ StormX.Statup("Love", 90, -20)
            $ StormX.Statup("Obed", 70, 20)
            $ StormX.Statup("Inbt", 80, 15)
        else:
            $ StormX.Statup("Love", 90, 10)
            $ StormX.Statup("Obed", 70, 12)
            $ StormX.Statup("Inbt", 80, 20)
    if Taboo:
        $ StormX.Inbt += int(Taboo/10)
        $ StormX.Lust += int(Taboo/5)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ StormX.DrainWord("tabno")
    $ StormX.DrainWord("no fondle ass")
    $ StormX.RecentActions.append("fondle ass")
    $ StormX.DailyActions.append("fondle ass")
    call Storm_Pussy_Launch("fondle ass")

label Storm_FA_Cycle: #Repeating strokes
    while Round > 0:
        call ViewShift(StormX,StormX.Pose,0,"fondle ass")
        call Shift_Focus(StormX)
        $ StormX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(StormX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Storm_FA_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0
                        "View":
                                    call ViewShift(StormX,"menu")
                                    jump Storm_FA_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if StormX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ StormX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(StormX,"tired")

                                    "Shift primary action":
                                            if StormX.Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in.":
                                                                $ Situation = "shift"
                                                                call Storm_FA_After
                                                                call Storm_Insert_Ass
                                                        "Just stick a finger in without asking.":
                                                                $ Situation = "auto"
                                                                call Storm_FA_After
                                                                call Storm_Insert_Ass
                                                        "I want to lick your asshole.":
                                                                $ Situation = "shift"
                                                                call Storm_FA_After
                                                                call Storm_Lick_Ass
                                                        "Just start licking.":
                                                                $ Situation = "auto"
                                                                call Storm_FA_After
                                                                call Storm_Lick_Ass
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Storm_FA_After
                                                                call Storm_Dildo_Ass
                                                        "Never Mind":
                                                                jump Storm_FA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(StormX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Storm_FA_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [StormX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(StormX)
                                            "Asks [StormX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(StormX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(StormX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Storm_FA_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Storm_FA_Cycle
                                            "Never mind":
                                                        jump Storm_FA_Cycle

                                    "Show her feet" if not ShowFeet and (StormX.Pose == "doggy" or StormX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (StormX.Pose == "doggy" or StormX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [StormX.Name]":
                                            call Girl_Undress(StormX)
                                    "Clean up [StormX.Name] (locked)" if not StormX.Spunk:
                                            pass
                                    "Clean up [StormX.Name]" if StormX.Spunk:
                                            call Girl_Cleanup(StormX,"ask")
                                    "Never mind":
                                            jump Storm_FA_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Storm_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Storm_FA_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Storm_Pos_Reset
                                    $ Line = 0
                                    jump Storm_FA_After
        #End menu (if Line)

        if StormX.Panties or StormX.PantsNum() > 6 or StormX.HoseNum() >= 5: #This checks if [StormX.Name] wants to strip down.
                call Girl_Undress(StormX,"auto")

        call Shift_Focus(StormX)
        call Sex_Dialog(StormX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or StormX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(StormX)
                            if "angry" in StormX.RecentActions:
                                call Storm_Pos_Reset
                                return
                            $ StormX.Statup("Lust", 200, 5)
                            if 100 > StormX.Lust >= 70 and StormX.OCount < 2 and StormX.SEXP >= 20:
                                $ StormX.RecentActions.append("unsatisfied")
                                $ StormX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Storm_FA_After
                            $ Line = "came"

                    if StormX.Lust >= 100:
                            #If [StormX.Name] can cum
                            call Girl_Cumming(StormX)
                            if Situation == "shift" or "angry" in StormX.RecentActions:
                                jump Storm_FA_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in StormX.RecentActions:#And [StormX.Name] is unsatisfied,
                                    "[StormX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Storm_FA_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if StormX.SEXP >= 100 or ApprovalCheck(StormX, 1200, "LO"):
            pass
        elif Cnt == (5 + StormX.FondleA):
                    $ StormX.Brows = "confused"
                    ch_s "Mmmm. . ."
        elif StormX.Lust >= 80:
                    pass
        elif Cnt == (15 + StormX.FondleA) and StormX.SEXP >= 15 and not ApprovalCheck(StormX, 1500):
                    $ StormX.Brows = "confused"
                    menu:
                        ch_s "I am sure that is fun, but could we try something different?"
                        "Finish up.":
                                "You let go. . ."
                                jump Storm_FA_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Storm_FA_After
                        "No, this is fun.":
                                if ApprovalCheck(StormX, 1200) or ApprovalCheck(StormX, 500, "O"):
                                    $ StormX.Statup("Love", 200, -5)
                                    $ StormX.Statup("Obed", 50, 3)
                                    $ StormX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ StormX.FaceChange("angry", 1)
                                    call Storm_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_s "Well however much you are enjoying yourself, I need to take a break."
                                    $ StormX.Statup("Love", 50, -3, 1)
                                    $ StormX.Statup("Love", 80, -4, 1)
                                    $ StormX.Statup("Obed", 30, -1, 1)
                                    $ StormX.Statup("Obed", 50, -1, 1)
                                    $ StormX.RecentActions.append("angry")
                                    $ StormX.DailyActions.append("angry")
                                    jump Storm_FA_After
        #End Count check

        call Escalation(StormX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(StormX,10) #"It is getting late, [Girl.Petname]. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(StormX,5)   #"We should take a break soon."

    #Round = 0 loop breaks
    $ StormX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(StormX,"done") # ch_s "I need to take a moment to collect myself."

label Storm_FA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Storm_Pos_Reset

    $ StormX.FaceChange("sexy")

    $ StormX.FondleA += 1
    $ StormX.Action -=1
    if StormX.PantsNum() <= 6 or StormX.Upskirt:
        $ StormX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ StormX.Addictionrate += 1

        call Partner_Like(StormX,2)

    if StormX.FondleA == 1:
            $ StormX.SEXP += 4
            if not Situation:
                if StormX.Love >= 500 and "unsatisfied" not in StormX.RecentActions:
                    ch_s "That was. . . nice. . ."
                elif StormX.Obed <= 500 and Player.Focus <= 20:
                    $ StormX.FaceChange("perplexed", 1)
                    ch_s "Did you enjoy that?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_s "Oh? What did you have in mind?"
    call Checkout
    return


# end StormX.Fondle Ass /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Ass
label Storm_Insert_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(StormX)

    if StormX.InsertA: #You've done it before
        $ temp_modifier += 25
    if StormX.PantsNum() > 6 or StormX.HoseNum() >= 5: # she's got pants on.
        $ temp_modifier -= 15
    if StormX.Lust > 85: #She's really horny
        $ temp_modifier += 15
    if StormX.Lust > 95:
        $ temp_modifier += 5
    if Situation == "shift":
        $ temp_modifier += 10
    if StormX.Lust > 85 and Situation == "auto": #She's really horny
        $ temp_modifier += 10
    if "exhibitionist" in StormX.Traits:
        $ temp_modifier += (4*Taboo)
    if StormX in Player.Harem or "sex friend" in StormX.Petnames:
        $ temp_modifier += 10
    elif "ex" in StormX.Traits:
        $ temp_modifier -= 25
    if StormX.ForcedCount and not StormX.Forced:
        $ temp_modifier -= 5 * StormX.ForcedCount

    if Taboo and "tabno" in StormX.DailyActions:
        $ temp_modifier -= 10
    if Taboo and "public" not in StormX.History:
        $ temp_modifier -= 20

    if "no insert ass" in StormX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no insert ass" in StormX.RecentActions else 0

    $ Approval = ApprovalCheck(StormX, 1300, TabM = 3) # 130, 145, 160, Taboo -120(250)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ StormX.FaceChange("surprised")
            $ StormX.Statup("Obed", 90, 2)
            $ StormX.Statup("Obed", 70, 2)
            $ StormX.Statup("Inbt", 80, 2)
            $ StormX.Statup("Inbt", 30, 2)
            "As you slide a finger in, [StormX.Name] tightens around it in surprise, but seems into it."
            $ StormX.FaceChange("sexy")
            jump Storm_IA_Prep
        else:
            $ StormX.FaceChange("surprised")
            $ StormX.Statup("Love", 80, -2)
            $ StormX.Statup("Obed", 50, -3)
            ch_s "You go too far, [StormX.Petname]."
            $ temp_modifier = 0
            $ Trigger2 = 0
            return

    if "insert ass" in StormX.DailyActions:
        $ StormX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax, gently. . .",
            "Mmm. . ."])
        ch_s "[Line]"

    if Approval >= 2:                                                                   #She's into it. . .
        if StormX.Forced:
            $ StormX.FaceChange("sad")
            $ StormX.Statup("Love", 70, -3, 1)
            $ StormX.Statup("Love", 20, -2, 1)
            $ StormX.Statup("Obed", 90, 1)
            $ StormX.Statup("Inbt", 60, 1)
            ch_s "If you must. . ."
        else:
            $ StormX.FaceChange("sexy", 1)
            $ StormX.Eyes = "closed"
            $ StormX.Statup("Love", 90, 1)
            $ StormX.Statup("Inbt", 50, 3)
            $ StormX.Statup("Lust", 200, 3)
            ch_s "Mmmmm. . ."
        $ StormX.Statup("Obed", 20, 1)
        $ StormX.Statup("Obed", 60, 1)
        $ StormX.Statup("Inbt", 70, 2)
        jump Storm_IA_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ StormX.FaceChange("angry", 1)
        if "no insert ass" in StormX.RecentActions:
            ch_s "Do not persist in this, [StormX.Petname]."
        elif "no insert ass" in StormX.DailyActions:
            ch_s "I have already told you my answer."
        elif Taboo and "tabno" in StormX.DailyActions:
            ch_s "This area is too public, [StormX.Petname]."
        elif not StormX.InsertA:
            $ StormX.FaceChange("perplexed", 1)
            ch_s "I am unsure about that. . ."
        else:
            $ StormX.FaceChange("bemused")
            ch_s "I would rather not. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no insert ass" in StormX.DailyActions:
                $ StormX.FaceChange("bemused")
                ch_s "I appreciate your restraint, [StormX.Petname]."
                return
            "Maybe later?" if "no insert ass" not in StormX.DailyActions:
                $ StormX.FaceChange("sexy")
                ch_s "I will give it some thought, [StormX.Petname]."
                $ StormX.Statup("Love", 80, 2)
                $ StormX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ StormX.RecentActions.append("tabno")
                    $ StormX.DailyActions.append("tabno")
                $ StormX.RecentActions.append("no insert ass")
                $ StormX.DailyActions.append("no insert ass")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ StormX.FaceChange("sexy")
                    $ StormX.Statup("Obed", 90, 2)
                    $ StormX.Statup("Obed", 50, 2)
                    ch_s "You may be correct. . ."
                    $ StormX.Statup("Inbt", 70, 3)
                    $ StormX.Statup("Inbt", 40, 2)
                    jump Storm_IA_Prep
                else:
                    $ StormX.FaceChange("bemused")
                    ch_s "I do not think that I would."

            "[[Slide a finger in anyway]":                                               # Pressured into being fingered.
                $ Approval = ApprovalCheck(StormX, 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                if Approval > 1 or (Approval and StormX.Forced):
                    $ StormX.FaceChange("surprised", 1)
                    $ StormX.Statup("Love", 70, -5, 1)
                    $ StormX.Statup("Love", 200, -2)
                    ch_s "That was unexpected. . ."
                    $ StormX.FaceChange("sad")
                    $ StormX.Statup("Obed", 50, 4)
                    $ StormX.Statup("Inbt", 80, 1)
                    $ StormX.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ StormX.Forced = 1
                    jump Storm_IA_Prep
                else:
                    $ StormX.Statup("Love", 200, -15)
                    $ StormX.FaceChange("angry", 1)
                    "She slaps your hand away."
                    $ StormX.RecentActions.append("angry")
                    $ StormX.DailyActions.append("angry")

    if "no insert ass" in StormX.DailyActions:
        ch_s "I have been clear on this."
        $ StormX.RecentActions.append("angry")
        $ StormX.DailyActions.append("angry")
    elif StormX.Forced:
        $ StormX.FaceChange("angry", 1)
        ch_s "You go too far."
        if ApprovalCheck(StormX, 500, "I"):
                $ StormX.Statup("Lust", 80, 10)
        else:
                $ StormX.Statup("Lust", 50, 3)
        $ StormX.Statup("Obed", 50, -2)
        $ StormX.RecentActions.append("angry")
        $ StormX.DailyActions.append("angry")
    elif Taboo:
        $ StormX.FaceChange("angry", 1)
        $ StormX.RecentActions.append("tabno")
        $ StormX.DailyActions.append("tabno")
        ch_s "I should not be seen doing that."
    elif StormX.InsertA:
        $ StormX.FaceChange("sad")
        ch_s "No, I do not think so."
    else:
        $ StormX.FaceChange("surprised")
        ch_s "No, I do not think so."
        $ StormX.FaceChange()
    $ StormX.RecentActions.append("no insert ass")
    $ StormX.DailyActions.append("no insert ass")
    $ temp_modifier = 0
    return


label Storm_IA_Prep: #Animation set-up
    if Trigger2 == "insert ass":
        return

    call Storm_Pussy_Launch("insert ass")

    if Situation == StormX:
            #Storm auto-starts
            $ Situation = 0
            if (StormX.Legs and not StormX.Upskirt) or (StormX.Panties and not StormX.PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck(StormX, 1250, TabM = 1) or (StormX.SeenPussy and ApprovalCheck(StormX, 500) and not Taboo):
                        $ StormX.Upskirt = 1
                        $ StormX.PantiesDown = 1
                        $ Line = 0
                        if StormX.PantsNum() == 5:
                            $ Line = StormX.Name + " hikes up her skirt"
                        elif StormX.PantsNum() >= 6:
                            $ Line = StormX.Name + " pulls down her " + StormX.Legs
                        else:
                            $ Line = 0
                        if StormX.Panties:
                            if Line:
                                #wearing pants
                                "[Line] and pulls her [StormX.Panties] out of the way."
                                "She then grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
                            else:
                                #no pants
                                "She pulls her [StormX.Panties] out of the way, and then presses your hand against her asshole."
                                "She clearly intends for you to get to work."
                        else:
                                #pants but no panties
                                "[Line], and then presses your hand against her asshole."
                                "She clearly intends for you to get to work."
                        call Storm_First_Bottomless(1)
                else:
                        "[StormX.Name] grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
            else:
                        "[StormX.Name] grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":
                    $ StormX.Statup("Inbt", 80, 3)
                    $ StormX.Statup("Inbt", 50, 2)
                    "You press your finger into it."
                "Praise her.":
                    $ StormX.FaceChange("sexy", 1)
                    $ StormX.Statup("Inbt", 80, 3)
                    ch_p "Dirty girl, [StormX.Pet]."
                    $ StormX.NameCheck() #checks reaction to petname
                    "You press your finger into it."
                    $ StormX.Statup("Love", 85, 1)
                    $ StormX.Statup("Obed", 90, 1)
                    $ StormX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your hand back."
                    $ StormX.FaceChange("surprised")
                    $ StormX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that right now, [StormX.Pet]."
                    $ StormX.NameCheck() #checks reaction to petname
                    "[StormX.Name] pulls back."
                    $ StormX.Statup("Obed", 90, 1)
                    $ StormX.Statup("Obed", 50, 1)
                    $ StormX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ StormX.AddWord(1,"refused","refused")
                    return
            #end auto

    if not StormX.Forced and Situation != "auto":
        $ temp_modifier = 0
        call Bottoms_Off(StormX)
        if "angry" in StormX.RecentActions:
            return

    $ temp_modifier = 0
    if not StormX.InsertA:
        if StormX.Forced:
            $ StormX.Statup("Love", 90, -50)
            $ StormX.Statup("Obed", 70, 60)
            $ StormX.Statup("Inbt", 80, 35)
        else:
            $ StormX.Statup("Love", 90, 10)
            $ StormX.Statup("Obed", 70, 20)
            $ StormX.Statup("Inbt", 80, 25)

    if Taboo:
        $ StormX.Inbt += int(Taboo/10)
        $ StormX.Lust += int(Taboo/5)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ StormX.DrainWord("tabno")
    $ StormX.DrainWord("no insert ass")
    $ StormX.RecentActions.append("insert ass")
    $ StormX.DailyActions.append("insert ass")
    call Storm_Pussy_Launch("insert ass")

label Storm_IA_Cycle: #Repeating strokes
    while Round > 0:
        call ViewShift(StormX,StormX.Pose,0,"insert ass")
        call Shift_Focus(StormX)
        $ StormX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(StormX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Storm_IA_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0
                        "View":
                                    call ViewShift(StormX,"menu")
                                    jump Storm_IA_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if StormX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ StormX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(StormX,"tired")

                                    "Shift primary action":
                                            if StormX.Action and MultiAction:
                                                    menu:
                                                        "Pull out and start rubbing again.":
                                                                $ Situation = "pullback"
                                                                call Storm_IA_After
                                                                call Storm_Fondle_Ass
                                                        "I want to lick your asshole.":
                                                                $ Situation = "shift"
                                                                call Storm_IA_After
                                                                call Storm_Lick_Ass
                                                        "Just start licking.":
                                                                $ Situation = "auto"
                                                                call Storm_IA_After
                                                                call Storm_Lick_Ass
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Storm_IA_After
                                                                call Storm_Dildo_Ass
                                                        "Never Mind":
                                                                jump Storm_IA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(StormX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Storm_IA_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [StormX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(StormX)
                                            "Asks [StormX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(StormX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(StormX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Storm_IA_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Storm_IA_Cycle
                                            "Never mind":
                                                        jump Storm_IA_Cycle

                                    "Show her feet" if not ShowFeet and (StormX.Pose == "doggy" or StormX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (StormX.Pose == "doggy" or StormX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [StormX.Name]":
                                            call Girl_Undress(StormX)
                                    "Clean up [StormX.Name] (locked)" if not StormX.Spunk:
                                            pass
                                    "Clean up [StormX.Name]" if StormX.Spunk:
                                            call Girl_Cleanup(StormX,"ask")
                                    "Never mind":
                                            jump Storm_IA_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Storm_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Storm_IA_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Storm_Pos_Reset
                                    $ Line = 0
                                    jump Storm_IA_After
        #End menu (if Line)

        if StormX.Panties or StormX.PantsNum() > 6 or StormX.HoseNum() >= 5: #This checks if [StormX.Name] wants to strip down.
                call Girl_Undress(StormX,"auto")

        call Shift_Focus(StormX)
        call Sex_Dialog(StormX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or StormX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(StormX)
                            if "angry" in StormX.RecentActions:
                                call Storm_Pos_Reset
                                return
                            $ StormX.Statup("Lust", 200, 5)
                            if 100 > StormX.Lust >= 70 and StormX.OCount < 2:
                                $ StormX.RecentActions.append("unsatisfied")
                                $ StormX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Storm_IA_After
                            $ Line = "came"

                    if StormX.Lust >= 100:
                            #If [StormX.Name] can cum
                            call Girl_Cumming(StormX)
                            if Situation == "shift" or "angry" in StormX.RecentActions:
                                jump Storm_IA_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in StormX.RecentActions:#And [StormX.Name] is unsatisfied,
                                    "[StormX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Storm_IA_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if StormX.SEXP >= 100 or ApprovalCheck(StormX, 1200, "LO"):
            pass
        elif Cnt == (5 + StormX.InsertA):
                    $ StormX.Brows = "confused"
                    ch_s "Ooh, watch it, watch it. . ."
        elif StormX.Lust >= 80:
                    pass
        elif Cnt == (15 + StormX.InsertA) and StormX.SEXP >= 15 and not ApprovalCheck(StormX, 1500):
                    $ StormX.Brows = "confused"
                    menu:
                        ch_s "I am sure that is fun, but could we try something different?"
                        "Finish up.":
                                "You let go. . ."
                                jump Storm_IA_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Storm_IA_After
                        "No, this is fun.":
                                if ApprovalCheck(StormX, 1200) or ApprovalCheck(StormX, 500, "O"):
                                    $ StormX.Statup("Love", 200, -5)
                                    $ StormX.Statup("Obed", 50, 3)
                                    $ StormX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ StormX.FaceChange("angry", 1)
                                    call Storm_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_s "Well however much you are enjoying yourself, I need to take a break."
                                    $ StormX.Statup("Love", 50, -3, 1)
                                    $ StormX.Statup("Love", 80, -4, 1)
                                    $ StormX.Statup("Obed", 30, -1, 1)
                                    $ StormX.Statup("Obed", 50, -1, 1)
                                    $ StormX.RecentActions.append("angry")
                                    $ StormX.DailyActions.append("angry")
                                    jump Storm_IA_After
        #End Count check

        call Escalation(StormX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(StormX,10) #"It is getting late, [Girl.Petname]. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(StormX,5)   #"We should take a break soon."

    #Round = 0 loop breaks
    $ StormX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(StormX,"done") # ch_s "I need to take a moment to collect myself."

label Storm_IA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Storm_Pos_Reset

    $ StormX.FaceChange("sexy")

    $ StormX.InsertA += 1
    $ StormX.Action -=1
    $ StormX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ StormX.Addictionrate += 1

    call Partner_Like(StormX,2)

    if StormX.InsertA == 1:
            $ StormX.SEXP += 12
            if not Situation:
                if StormX.Love >= 500 and "unsatisfied" not in StormX.RecentActions:
                    ch_s "That one caught me by surprise. . ."
                elif StormX.Obed <= 500 and Player.Focus <= 20:
                    $ StormX.FaceChange("perplexed", 1)
                    ch_s "did that work for you?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_s "Oh? What did you have in mind?"
    call Checkout
    return


# end StormX.Insert Ass /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Ass
label Storm_Lick_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(StormX)
                                                                             # Will she let you lick? Modifiers
    if StormX.LickA: #You've done it before
        $ temp_modifier += 20
    if StormX.PantsNum() > 6 or StormX.HoseNum() >= 5: # she's got pants on.
        $ temp_modifier -= 25
    if StormX.Lust > 95:
        $ temp_modifier += 20
    elif StormX.Lust > 85: #She's really horny
        $ temp_modifier += 15
    if StormX.Lust > 85 and Situation == "auto": #auto
        $ temp_modifier += 10
    if Situation == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in StormX.Traits:
        $ temp_modifier += (4*Taboo)
    if StormX in Player.Harem or "sex friend" in StormX.Petnames:
        $ temp_modifier += 10
    elif "ex" in StormX.Traits:
        $ temp_modifier -= 25
    if StormX.ForcedCount and not StormX.Forced:
        $ temp_modifier -= 5 * StormX.ForcedCount

    if Taboo and "tabno" in StormX.DailyActions:
        $ temp_modifier -= 10
    if Taboo and "public" not in StormX.History:
        $ temp_modifier -= 20

    if "no lick ass" in StormX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no lick ass" in StormX.RecentActions else 0

    $ Approval = ApprovalCheck(StormX, 1550, TabM = 4) # 155, 170, 185, Taboo -160(315)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ StormX.FaceChange("surprised")
            $ StormX.Statup("Obed", 90, 1)
            $ StormX.Statup("Inbt", 80, 3)
            $ StormX.Statup("Inbt", 40, 2)
            "As you crouch down and start to lick her asshole, [StormX.Name] startles briefly, but then begins to melt."
            $ StormX.FaceChange("sexy")
            jump Storm_LA_Prep
        else:
            $ StormX.FaceChange("surprised")
            $ StormX.Statup("Love", 80, -2)
            $ StormX.Statup("Obed", 50, -3)
            ch_s "[StormX.Petname]! Not now. . ."
            $ temp_modifier = 0
            $ Trigger2 = 0
            return

    if "lick ass" in StormX.RecentActions:
        $ StormX.FaceChange("sexy", 1)
        ch_s "Mmmm, again? I suppose. . ."
        jump Storm_LA_Prep
    elif "lick ass" in StormX.DailyActions:
        $ StormX.FaceChange("sexy", 1)
        ch_s "You didn't get enough earlier?"


    if Approval >= 2:                                                                   #She's into it. . .
        if StormX.Forced:
            $ StormX.FaceChange("sad")
            $ StormX.Statup("Love", 70, -3, 1)
            $ StormX.Statup("Love", 20, -2, 1)
            $ StormX.Statup("Obed", 90, 2)
            $ StormX.Statup("Inbt", 60, 2)
            ch_s "If you must. . ."
        else:
            $ StormX.FaceChange("sexy", 1)
            $ StormX.Eyes = "closed"
            $ StormX.Statup("Love", 90, 1)
            $ StormX.Statup("Inbt", 60, 2)
            $ StormX.Statup("Lust", 200, 3)
            ch_s "Mmm. . . naughty."
        $ StormX.Statup("Obed", 20, 1)
        $ StormX.Statup("Obed", 60, 1)
        $ StormX.Statup("Inbt", 80, 2)
        jump Storm_LA_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ StormX.FaceChange("angry", 1)
        if "no lick ass" in StormX.RecentActions:
            ch_s "Do not persist in this, [StormX.Petname]."
        elif "no lick ass" in StormX.DailyActions:
            ch_s "I have already told you my answer."
        elif Taboo and "tabno" in StormX.DailyActions:
            ch_s "This area is too public, [StormX.Petname]."
        elif not StormX.LickA:                    #First time dialog
            $ StormX.FaceChange("bemused", 1)
            if StormX.Love >= StormX.Obed and StormX.Love >= StormX.Inbt:
                ch_s "Oh, that is a bit forward!"
            elif StormX.Obed >= StormX.Inbt:
                ch_s "That is what you want?"
            else:
                $ StormX.Eyes = "sexy"
                ch_s "Hmmm, an interesting proposal. . ."
        else:
            $ StormX.FaceChange("bemused")
            ch_s "Not now, [StormX.Petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no lick ass" in StormX.DailyActions:
                $ StormX.FaceChange("bemused")
                ch_s "I appreciate your restraint, [StormX.Petname]."
                return
            "I'm sure I can convince you later. . ." if "no lick ass" not in StormX.DailyActions:
                $ StormX.FaceChange("sexy")
                ch_s "I will give it some thought, [StormX.Petname]."
                $ StormX.Statup("Love", 80, 2)
                $ StormX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ StormX.RecentActions.append("tabno")
                    $ StormX.DailyActions.append("tabno")
                $ StormX.RecentActions.append("no lick ass")
                $ StormX.DailyActions.append("no lick ass")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ StormX.FaceChange("sexy")
                    $ StormX.Statup("Obed", 90, 2)
                    $ StormX.Statup("Obed", 50, 2)
                    ch_s "Well. . . I might at that. . ."
                    $ StormX.Statup("Inbt", 70, 3)
                    $ StormX.Statup("Inbt", 40, 2)
                    jump Storm_LA_Prep
                else:
                    $ StormX.FaceChange("sexy")
                    ch_s "I really do not think so."

            "[[Start licking anyway]":                                               # Pressured into being licked.
                $ Approval = ApprovalCheck(StormX, 1100, "OI", TabM = 4) # 110, 125, 140, -160(270)
                if Approval > 1 or (Approval and StormX.Forced):
                    $ StormX.FaceChange("sad")
                    $ StormX.Statup("Love", 70, -5, 1)
                    $ StormX.Statup("Love", 200, -2)
                    ch_s "If you must. . ."
                    $ StormX.Statup("Obed", 50, 4)
                    $ StormX.Statup("Inbt", 80, 1)
                    $ StormX.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ StormX.Forced = 1
                    jump Storm_LA_Prep
                else:
                    $ StormX.Statup("Love", 200, -15)
                    $ StormX.FaceChange("angry", 1)
                    "She shoves your head back."
                    $ StormX.RecentActions.append("angry")
                    $ StormX.DailyActions.append("angry")

    if "no lick ass" in StormX.DailyActions:
        ch_s "I have been clear on this."
        $ StormX.RecentActions.append("angry")
        $ StormX.DailyActions.append("angry")
    elif StormX.Forced:
        $ StormX.FaceChange("angry", 1)
        ch_s "You go too far."
        if ApprovalCheck(StormX, 500, "I"):
                $ StormX.Statup("Lust", 80, 10)
        else:
                $ StormX.Statup("Lust", 50, 3)
        $ StormX.Statup("Obed", 50, -2)
        $ StormX.RecentActions.append("angry")
        $ StormX.DailyActions.append("angry")
    elif Taboo:
        $ StormX.FaceChange("angry", 1)
        $ StormX.RecentActions.append("tabno")
        $ StormX.DailyActions.append("tabno")
        ch_s "I should not be seen doing that."
    elif StormX.LickA:
        $ StormX.FaceChange("sad")
        ch_s "No, I do not think so."
    else:
        $ StormX.FaceChange("surprised")
        ch_s "No, I do not think so."
        $ StormX.FaceChange()
    $ StormX.RecentActions.append("no lick ass")
    $ StormX.DailyActions.append("no lick ass")
    $ temp_modifier = 0
    return

label Storm_LA_Prep: #Animation set-up
    if Trigger2 == "lick ass":
        return
    if not StormX.Forced and Situation != "auto":
        $ temp_modifier = 0
        if StormX.PantsNum() > 6:
            $ temp_modifier = 15
        call Bottoms_Off(StormX)
        if "angry" in StormX.RecentActions:
            return
    $ temp_modifier = 0
    call Storm_Pussy_Launch("lick ass")
    if not StormX.LickA:
        if StormX.Forced:
            $ StormX.Statup("Love", 90, -30)
            $ StormX.Statup("Obed", 70, 40)
            $ StormX.Statup("Inbt", 80, 80)
        else:
            $ StormX.Statup("Love", 90, 35)
            $ StormX.Statup("Obed", 70, 25)
            $ StormX.Statup("Inbt", 80, 55)
    if Taboo:
        $ StormX.Inbt += int(Taboo/10)
        $ StormX.Lust += int(Taboo/5)
    if Situation:
        $ renpy.pop_call()
        $ Situation = 0

    $ StormX.Upskirt = 1
    if StormX.PantsNum() == 5:
        $ StormX.SeenPanties = 1
    call Storm_First_Bottomless(1)
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ StormX.DrainWord("tabno")
    $ StormX.DrainWord("no lick ass")

    $ StormX.RecentActions.append("lick") if "lick" not in StormX.RecentActions else StormX.RecentActions
    $ StormX.RecentActions.append("ass") if "ass" not in StormX.RecentActions else StormX.RecentActions
    $ StormX.RecentActions.append("lick ass")

    $ StormX.DailyActions.append("lick") if "lick" not in StormX.DailyActions else StormX.RecentActions
    $ StormX.DailyActions.append("ass") if "ass" not in StormX.DailyActions else StormX.RecentActions
    $ StormX.DailyActions.append("lick ass")
    call Storm_Pussy_Launch("lick ass")

label Storm_LA_Cycle: #Repeating strokes
    if Trigger2 == "kiss you":
            $ Trigger2 = 0
    while Round > 0:
        call ViewShift(StormX,StormX.Pose,0,"lick ass")
        call Shift_Focus(StormX)
        $ StormX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(StormX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Storm_LA_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0
                        "View":
                                    call ViewShift(StormX,"menu")
                                    jump Storm_LA_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if StormX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ StormX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(StormX,"tired")

                                    "Shift primary action":
                                            if StormX.Action and MultiAction:
                                                    menu:
                                                        "Switch to fondling.":
                                                                $ Situation = "pullback"
                                                                call Storm_LA_After
                                                                call Storm_Fondle_Ass
                                                        "I want to stick a finger in.":
                                                                $ Situation = "shift"
                                                                call Storm_LA_After
                                                                call Storm_Insert_Ass
                                                        "Just stick a finger in [[without asking].":
                                                                $ Situation = "auto"
                                                                call Storm_LA_After
                                                                call Storm_Insert_Ass
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Storm_LA_After
                                                                call Storm_Dildo_Ass
                                                        "Never Mind":
                                                                jump Storm_LA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(StormX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Storm_LA_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [StormX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(StormX)
                                            "Asks [StormX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(StormX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(StormX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Storm_LA_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Storm_LA_Cycle
                                            "Never mind":
                                                        jump Storm_LA_Cycle

                                    "Show her feet" if not ShowFeet and (StormX.Pose == "doggy" or StormX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (StormX.Pose == "doggy" or StormX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [StormX.Name]":
                                            call Girl_Undress(StormX)
                                    "Clean up [StormX.Name] (locked)" if not StormX.Spunk:
                                            pass
                                    "Clean up [StormX.Name]" if StormX.Spunk:
                                            call Girl_Cleanup(StormX,"ask")
                                    "Never mind":
                                            jump Storm_LA_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Storm_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Storm_LA_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Storm_Pos_Reset
                                    $ Line = 0
                                    jump Storm_LA_After
        #End menu (if Line)

        if StormX.Panties or StormX.PantsNum() > 6 or StormX.HoseNum() >= 5: #This checks if [StormX.Name] wants to strip down.
                call Girl_Undress(StormX,"auto")

        call Shift_Focus(StormX)
        call Sex_Dialog(StormX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or StormX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(StormX)
                            if "angry" in StormX.RecentActions:
                                call Storm_Pos_Reset
                                return
                            $ StormX.Statup("Lust", 200, 5)
                            if 100 > StormX.Lust >= 70 and StormX.OCount < 2:
                                $ StormX.RecentActions.append("unsatisfied")
                                $ StormX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Storm_LA_After
                            $ Line = "came"

                    if StormX.Lust >= 100:
                            #If [StormX.Name] can cum
                            call Girl_Cumming(StormX)
                            if Situation == "shift" or "angry" in StormX.RecentActions:
                                jump Storm_LA_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in StormX.RecentActions:#And [StormX.Name] is unsatisfied,
                                    "[StormX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Storm_LA_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if StormX.SEXP >= 100 or ApprovalCheck(StormX, 1200, "LO"):
            pass
        elif Cnt == (5 + StormX.LickA):
                    $ StormX.Brows = "confused"
                    ch_s "You are quite enthusiastic. . ."
        elif StormX.Lust >= 80:
                    pass
        elif Cnt == (15 + StormX.LickA) and StormX.SEXP >= 15 and not ApprovalCheck(StormX, 1500):
                    $ StormX.Brows = "confused"
                    menu:
                        ch_s "I am sure that is fun, but could we try something different?"
                        "Finish up.":
                                "You let go. . ."
                                jump Storm_LA_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Storm_LA_After
                        "No, this is fun.":
                                if ApprovalCheck(StormX, 1200) or ApprovalCheck(StormX, 500, "O"):
                                    $ StormX.Statup("Love", 200, -5)
                                    $ StormX.Statup("Obed", 50, 3)
                                    $ StormX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ StormX.FaceChange("angry", 1)
                                    call Storm_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_s "Well however much you are enjoying yourself, I need to take a break."
                                    $ StormX.Statup("Love", 50, -3, 1)
                                    $ StormX.Statup("Love", 80, -4, 1)
                                    $ StormX.Statup("Obed", 30, -1, 1)
                                    $ StormX.Statup("Obed", 50, -1, 1)
                                    $ StormX.RecentActions.append("angry")
                                    $ StormX.DailyActions.append("angry")
                                    jump Storm_LA_After
        #End Count check

        call Escalation(StormX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(StormX,10) #"It is getting late, [Girl.Petname]. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(StormX,5)   #"We should take a break soon."

    #Round = 0 loop breaks
    $ StormX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(StormX,"done") # ch_s "I need to take a moment to collect myself."

label Storm_LA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Storm_Pos_Reset

    $ StormX.FaceChange("sexy")

    $ StormX.LickA += 1
    $ StormX.Action -=1
    if StormX.PantsNum() <= 6 or StormX.Upskirt:
        $ StormX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ StormX.Addictionrate += 1

    call Partner_Like(StormX,2)

    if StormX.LickA == 1:
            $ StormX.SEXP += 15
            if not Situation:
                if StormX.Love >= 500 and "unsatisfied" not in StormX.RecentActions:
                    ch_s "That was. . . certainly interesting. . ."
                elif StormX.Obed <= 500 and Player.Focus <= 20:
                    $ StormX.FaceChange("perplexed", 1)
                    ch_s "Did you enjoy that?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_s "Oh? What did you have in mind?"
    call Checkout
    return

# end StormX.Lick Ass /////////////////////////////////////////////////////////////////////////////
