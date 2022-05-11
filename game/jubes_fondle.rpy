# JubesX.Fondle /////////////////////////////////////////////////////////////////////////////
label Jubes_Fondle: #rkeljsv

    $ JubesX.Mouth = "smile"
    if not JubesX.Action:
        ch_v "Maybe later, [JubesX.Petname]"
        return
    menu:
        ch_v "Well? Where did you want to touch, [JubesX.Petname]?"
        "Your breasts?" if JubesX.Action:
                jump Jubes_Fondle_Breasts
        "Your thighs?" if JubesX.Action:
                jump Jubes_Fondle_Thighs
        "Your pussy?" if JubesX.Action:
                jump Jubes_Fondle_Pussy
        "Your Ass?" if JubesX.Action:
                jump Jubes_Fondle_Ass
        "Never mind.":
                return
    return

# ////////////////////////////////////////////////////////////////////////Start Fondle Pussy
label Jubes_Fondle_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JubesX)
                                                                                        # Will she let you fondle? Modifiers
    if JubesX.FondleP: #You've done it before
        $ temp_modifier += 20
    if JubesX.PantsNum() >= 6 or JubesX.HoseNum() >= 5: # she's got pants on.
        $ temp_modifier -= 10
    if JubesX.Lust > 75: #She's really horny
        $ temp_modifier += 15
    if JubesX.Lust > 75 and Situation == "auto": #She's really horny
        $ temp_modifier += 10
    if "exhibitionist" in JubesX.Traits:
        $ temp_modifier += (2*Taboo)
    if JubesX in Player.Harem or "sex friend" in JubesX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JubesX.Traits:
        $ temp_modifier -= 25
    if JubesX.ForcedCount and not JubesX.Forced:
        $ temp_modifier -= 5 * JubesX.ForcedCount

    if Taboo and "tabno" in JubesX.DailyActions:
        $ temp_modifier -= 10
    if Taboo and "public" not in JubesX.History:
        $ temp_modifier -= 20

    if "no fondle pussy" in JubesX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no fondle pussy" in JubesX.RecentActions else 0

    $ Approval = ApprovalCheck(JubesX, 1050, TabM = 2) # 105, 120, 135, Taboo -80(185)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ JubesX.FaceChange("sexy")
            $ JubesX.Statup("Obed", 90, 1)
            $ JubesX.Statup("Obed", 70, 2)
            $ JubesX.Statup("Inbt", 70, 3)
            $ JubesX.Statup("Inbt", 30, 2)
            "As your hand creeps up her thigh, [JubesX.Name] seems a bit surprised, but then nods."
            jump Jubes_FP_Prep
        else:
            $ JubesX.FaceChange("surprised")
            $ JubesX.Statup("Obed", 50, -2)
            ch_v "Cool your jets, [JubesX.Petname]. . ."
            $ temp_modifier = 0
            $ Trigger2 = 0
            return

    if Situation == "pullback":
        $ JubesX.FaceChange("surprised")
        $ JubesX.Brows = "sad"
        if JubesX.Lust > 80:
            $ JubesX.Statup("Love", 70, -4)
        $ JubesX.Statup("Obed", 90, 1)
        $ JubesX.Statup("Obed", 70, 2)
        "As your hand pulls out, [JubesX.Name] gasps and looks upset."
        jump Jubes_FP_Prep
    elif "fondle pussy" in JubesX.RecentActions:
        $ JubesX.FaceChange("sexy", 1)
        ch_v "Mmmm, again? I guess. . ."
        jump Jubes_FP_Prep
    elif "fondle pussy" in JubesX.DailyActions:
        $ JubesX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax. . .",
            "Take it slow, I'm still shaking from earlier.",
            "Mmm. . ."])
        ch_v "[Line]"

    if Approval >= 2:                                                                   #She's into it. . .
        $ JubesX.FaceChange("bemused", 1)
        if JubesX.Forced:
            $ JubesX.FaceChange("sad")
            $ JubesX.Statup("Love", 70, -3, 1)
            $ JubesX.Statup("Love", 20, -2, 1)
            $ JubesX.Statup("Obed", 90, 1)
            $ JubesX.Statup("Inbt", 60, 1)
        ch_v "Mmmm, I couldn't refuse. . ."
        $ JubesX.Statup("Love", 90, 1)
        $ JubesX.Statup("Inbt", 50, 3)
        jump Jubes_FP_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ JubesX.FaceChange("angry", 1)
        if "no fondle pussy" in JubesX.RecentActions:
            ch_v "I already told you, \"no\"."
        elif Taboo and "tabno" in JubesX.DailyActions and "no fondle pussy" in JubesX.DailyActions:
            ch_v "I told you not to touch me like that in public!"
        elif "no fondle pussy" in JubesX.DailyActions:
            ch_v "Don't make me tell you again today."
        elif Taboo and "tabno" in JubesX.DailyActions:
            ch_v "I told you, not here, [JubesX.Petname]."
        elif not JubesX.FondleP:
            $ JubesX.FaceChange("bemused")
            ch_v "I don't think we're there yet, [JubesX.Petname]. . ."
        else:
            $ JubesX.FaceChange("bemused")
            ch_v "You wish."
        menu:
            extend ""
            "Sorry, never mind." if "no fondle pussy" in JubesX.DailyActions:
                $ JubesX.FaceChange("bemused")
                ch_v "Yeah, whatever."
                return
            "Maybe later?" if "no fondle pussy" not in JubesX.DailyActions:
                $ JubesX.FaceChange("sexy")
                ch_v "Maybe, [JubesX.Petname]."
                $ JubesX.Statup("Love", 80, 2)
                $ JubesX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ JubesX.RecentActions.append("tabno")
                    $ JubesX.DailyActions.append("tabno")
                $ JubesX.RecentActions.append("no fondle pussy")
                $ JubesX.DailyActions.append("no fondle pussy")
                return
            "Come on, Please?":
                if Approval:
                    $ JubesX.FaceChange("sexy")
                    $ JubesX.Statup("Obed", 90, 2)
                    $ JubesX.Statup("Obed", 50, 2)
                    $ JubesX.Statup("Inbt", 70, 3)
                    $ JubesX.Statup("Inbt", 40, 2)
                    ch_v "Oooh, beg for me. . ."
                    jump Jubes_FP_Prep
                else:
                    $ JubesX.FaceChange("sexy")
                    ch_v "No."

            "[[Start fondling anyway]":                                               # Pressured into fondling.
                $ Approval = ApprovalCheck(JubesX, 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                if Approval > 1 or (Approval and JubesX.Forced):
                    $ JubesX.FaceChange("sad")
                    $ JubesX.Statup("Love", 70, -5, 1)
                    $ JubesX.Statup("Love", 200, -2)
                    ch_v "Ok, fine. . ."
                    $ JubesX.Statup("Obed", 50, 4)
                    $ JubesX.Statup("Inbt", 80, 1)
                    $ JubesX.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ JubesX.Forced = 1
                    jump Jubes_FP_Prep
                else:
                    $ JubesX.Statup("Love", 200, -15)
                    $ JubesX.FaceChange("angry", 1)
                    "She slaps your hand away."
                    $ JubesX.RecentActions.append("angry")
                    $ JubesX.DailyActions.append("angry")

    if "no fondle pussy" in JubesX.DailyActions:
        ch_v "I'm pretty clear on this, NO."
        $ JubesX.RecentActions.append("angry")
        $ JubesX.DailyActions.append("angry")
    elif JubesX.Forced:
        $ JubesX.FaceChange("angry", 1)
        ch_v "I don't think so, [JubesX.Petname]."
        $ JubesX.Statup("Lust", 70, 5)
        $ JubesX.Statup("Obed", 50, -2)
        $ JubesX.RecentActions.append("angry")
        $ JubesX.DailyActions.append("angry")
    elif Taboo:
        $ JubesX.FaceChange("angry", 1)
        $ JubesX.RecentActions.append("tabno")
        $ JubesX.DailyActions.append("tabno")
        ch_v "I don't wanna make a scene."
    elif JubesX.FondleP:
        $ JubesX.FaceChange("sad")
        ch_v "Sorry, keep your fingers outside."
    else:
        $ JubesX.FaceChange("sexy")
        $ JubesX.Mouth = "sad"
        ch_v "No thank you, [JubesX.Petname]."
    $ JubesX.RecentActions.append("no fondle pussy")
    $ JubesX.DailyActions.append("no fondle pussy")
    $ temp_modifier = 0
    return

label Jubes_FP_Prep: #Animation set-up
    if Trigger2 == "fondle pussy":
        return

    call Jubes_Pussy_Launch("fondle pussy")

    if Situation == JubesX:
            #Jubes auto-starts
            $ Situation = 0
            if (JubesX.Legs and not JubesX.Upskirt) or (JubesX.Panties and not JubesX.PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck(JubesX, 1250, TabM = 1) or (JubesX.SeenPussy and ApprovalCheck(JubesX, 500) and not Taboo):
                        $ JubesX.Upskirt = 1
                        $ JubesX.PantiesDown = 1
                        $ Line = 0
                        if JubesX.PantsNum() == 5:
                            $ Line = JubesX.Name + " hikes up her skirt"
                        elif JubesX.PantsNum() >= 6:
                            $ Line = JubesX.Name + " pulls down her " + JubesX.Legs
                        else:
                            $ Line = 0
                        if JubesX.Panties:
                            if Line:
                                #wearing pants
                                "[Line] and pulls her [JubesX.Panties] out of the way."
                                "She then grabs your arm and then presses your hand against her crotch, clearly intending you to get to work."
                            else:
                                #no pants
                                "She pulls her [JubesX.Panties] out of the way, and then presses your hand against her crotch."
                                "She clearly intends for you to get to work."
                        else:
                            #pants but no panties
                            "[Line], and then presses your hand against her crotch."
                            "She clearly intends for you to get to work."
                        call Jubes_First_Bottomless(1)
                else:
                        "[JubesX.Name] grabs your arm and presses your hand against her crotch, clearly intending you to get to work."
            else:
                        "[JubesX.Name] grabs your arm and presses your hand against her crotch, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":
                    $ JubesX.Statup("Inbt", 80, 3)
                    $ JubesX.Statup("Inbt", 50, 2)
                    "You start to run your fingers along her pussy."
                "Praise her.":
                    $ JubesX.FaceChange("sexy", 1)
                    $ JubesX.Statup("Inbt", 80, 3)
                    ch_p "I like the initiative, [JubesX.Pet]."
                    $ JubesX.NameCheck() #checks reaction to petname
                    "You start to run your fingers along her pussy."
                    $ JubesX.Statup("Love", 85, 1)
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your hand back."
                    $ JubesX.FaceChange("surprised")
                    $ JubesX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that right now, [JubesX.Pet]."
                    $ JubesX.NameCheck() #checks reaction to petname
                    "[JubesX.Name] pulls back."
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Obed", 50, 1)
                    $ JubesX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ JubesX.AddWord(1,"refused","refused")
                    return
            #end auto

    if not JubesX.Forced and Situation != "auto":
        $ temp_modifier = 0
        call Bottoms_Off(JubesX)
        if "angry" in JubesX.RecentActions:
            return
    $ temp_modifier = 0

    if not JubesX.FondleP:
        if JubesX.Forced:
            $ JubesX.Statup("Love", 90, -50)
            $ JubesX.Statup("Obed", 70, 35)
            $ JubesX.Statup("Inbt", 80, 25)
        else:
            $ JubesX.Statup("Love", 90, 10)
            $ JubesX.Statup("Obed", 70, 10)
            $ JubesX.Statup("Inbt", 80, 15)
    if Taboo:
        $ JubesX.Inbt += int(Taboo/10)
        $ JubesX.Lust += int(Taboo/5)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ JubesX.DrainWord("tabno")
    $ JubesX.DrainWord("no fondle pussy")
    $ JubesX.RecentActions.append("fondle pussy")
    $ JubesX.DailyActions.append("fondle pussy")
    call Jubes_Pussy_Launch("fondle pussy")
    $ Speed = 1

label Jubes_FP_Cycle: #Repeating strokes
    while Round > 0:
        call ViewShift(JubesX,JubesX.Pose,0,"fondle pussy")
        call Shift_Focus(JubesX)
        $ JubesX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "I want to stick a finger in. . ." if Speed != 2:
                                if JubesX.InsertP:
                                    $ Speed = 2
                                else:
                                    menu:
                                        "Ask her first":
                                            $ Situation = "shift"
                                        "Don't ask first [[just stick it in]":
                                            $ Situation = "auto"
                                    call Jubes_Insert_Pussy

                        "Pull back a bit. . ." if Speed == 2:
                                    $ Speed = 0

                        "Slap her ass":
                                    call Slap_Ass(JubesX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Jubes_FP_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0
                        "View":
                                    call ViewShift(JubesX,"menu")
                                    jump Jubes_FP_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if JubesX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ JubesX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")

                                    "Shift primary action":
                                            if JubesX.Action and MultiAction:
                                                    menu:
                                                        "I want to lick your pussy.":
                                                                $ Situation = "shift"
                                                                call Jubes_FP_After
                                                                call Jubes_Lick_Pussy
                                                        "Just start licking":
                                                                $ Situation = "auto"
                                                                call Jubes_FP_After
                                                                call Jubes_Lick_Pussy
                                                        "Pull back to the thighs":
                                                                $ Situation = "pullback"
                                                                call Jubes_FP_After
                                                                call Jubes_Fondle_Thighs
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Jubes_FP_After
                                                                call Jubes_Dildo_Pussy
                                                        "Never Mind":
                                                                jump Jubes_FP_Cycle
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Jubes_FP_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [JubesX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(JubesX)
                                            "Ask [JubesX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(JubesX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(JubesX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jubes_FP_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jubes_FP_Cycle
                                            "Never mind":
                                                        jump Jubes_FP_Cycle

                                    "Show her feet" if not ShowFeet and (JubesX.Pose == "doggy" or JubesX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (JubesX.Pose == "doggy" or JubesX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [JubesX.Name]":
                                            call Girl_Undress(JubesX)
                                    "Clean up [JubesX.Name] (locked)" if not JubesX.Spunk:
                                            pass
                                    "Clean up [JubesX.Name]" if JubesX.Spunk:
                                            call Girl_Cleanup(JubesX,"ask")
                                    "Never mind":
                                            jump Jubes_FP_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Jubes_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Jubes_FP_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Jubes_Pos_Reset
                                    $ Line = 0
                                    jump Jubes_FP_After
        #End menu (if Line)

        call Shift_Focus(JubesX)
        call Sex_Dialog(JubesX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JubesX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JubesX)
                            if "angry" in JubesX.RecentActions:
                                call Jubes_Pos_Reset
                                return
                            $ JubesX.Statup("Lust", 200, 5)
                            if 100 > JubesX.Lust >= 70 and JubesX.OCount < 2:
                                $ JubesX.RecentActions.append("unsatisfied")
                                $ JubesX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jubes_FP_After
                            $ Line = "came"

                    if JubesX.Lust >= 100:
                            #If Jubes can cum
                            call Girl_Cumming(JubesX)
                            if Situation == "shift" or "angry" in JubesX.RecentActions:
                                jump Jubes_FP_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in JubesX.RecentActions:#And Jubes is unsatisfied,
                                    "[JubesX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Jubes_FP_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if JubesX.SEXP >= 100 or ApprovalCheck(JubesX, 1200, "LO"):
            pass
        elif Cnt == (5 + JubesX.FondleP):
                    $ JubesX.Brows = "confused"
                    ch_v "Having fun?"
        elif JubesX.Lust >= 80:
                    pass
        elif Cnt == (15 + JubesX.FondleP) and JubesX.SEXP >= 15 and not ApprovalCheck(JubesX, 1500):
                    $ JubesX.Brows = "confused"
                    menu:
                        ch_v "Could we maybe try. . . something else?"
                        "Finish up.":
                                "You let go. . ."
                                jump Jubes_FP_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Jubes_FP_After
                        "No, this is fun.":
                                if ApprovalCheck(JubesX, 1200) or ApprovalCheck(JubesX, 500, "O"):
                                    $ JubesX.Statup("Love", 200, -5)
                                    $ JubesX.Statup("Obed", 50, 3)
                                    $ JubesX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ JubesX.FaceChange("angry", 1)
                                    call Jubes_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_v "This is kinda boring. . .."
                                    $ JubesX.Statup("Love", 50, -3, 1)
                                    $ JubesX.Statup("Love", 80, -4, 1)
                                    $ JubesX.Statup("Obed", 30, -1, 1)
                                    $ JubesX.Statup("Obed", 50, -1, 1)
                                    $ JubesX.RecentActions.append("angry")
                                    $ JubesX.DailyActions.append("angry")
                                    jump Jubes_FP_After
        #End Count check

        call Escalation(JubesX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(JubesX,10) #"I could use a break soon. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(JubesX,5)   #". . . I could really use a break here. . ."

    #Round = 0 loop breaks
    $ JubesX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(JubesX,"done") # ch_s "Ok, that's it, I need a break."


label Jubes_FP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Jubes_Pos_Reset

    $ JubesX.FaceChange("sexy")

    $ JubesX.FondleP += 1
    $ JubesX.Action -=1
    if JubesX.PantsNum() < 6 or JubesX.Upskirt:
        $ JubesX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ JubesX.Addictionrate += 1

    call Partner_Like(JubesX,2)

    if JubesX.FondleP == 1:
            $ JubesX.SEXP += 7
            if not Situation:
                if JubesX.Love >= 500 and "unsatisfied" not in JubesX.RecentActions:
                    ch_v "Wow. . . that was nice. . ."
                elif JubesX.Obed <= 500 and Player.Focus <= 20:
                    $ JubesX.FaceChange("perplexed", 1)
                    ch_v "Did you find anything in there?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_v "Oh? What did you have in mind?"
    call Checkout
    return

# end JubesX.Fondle Pussy /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy
label Jubes_Insert_Pussy:
    call Shift_Focus(JubesX)
    if Situation == "auto":                                                                  #You auto-start
        if ApprovalCheck(JubesX, 1100, TabM = 2):
            $ JubesX.FaceChange("surprised")
            $ JubesX.Statup("Obed", 90, 1)
            $ JubesX.Statup("Obed", 70, 2)
            $ JubesX.Statup("Inbt", 70, 3)
            $ JubesX.Statup("Inbt", 30, 2)
            "As you slide a finger in, [JubesX.Name] seems a bit surprised, but seems into it."
            jump Jubes_IP_Prep
        else:
            $ JubesX.FaceChange("surprised",2)
            $ JubesX.Statup("Love", 80, -2)
            $ JubesX.Statup("Obed", 50, -3)
            ch_v "Oooh!"
            "She slaps your hand back."
            $ JubesX.FaceChange("perplexed",1)
            ch_v "Watch your hands, or lose them."
            return

    if ApprovalCheck(JubesX, 1100, TabM = 2):                                                                   #She's into it. . .
        if JubesX.Forced:
            $ JubesX.FaceChange("sad")
            $ JubesX.Statup("Love", 70, -3, 1)
            $ JubesX.Statup("Love", 20, -2, 1)
            $ JubesX.Statup("Obed", 90, 1)
            $ JubesX.Statup("Inbt", 60, 1)
            ch_v "Going there, huh. . ."
        else:
            $ JubesX.FaceChange("sexy", 1)
            $ JubesX.Statup("Love", 90, 1)
            $ JubesX.Statup("Inbt", 50, 3)
            ch_v "Mmmmmm. . ."
        $ JubesX.Statup("Obed", 20, 1)
        $ JubesX.Statup("Obed", 60, 1)
        $ JubesX.Statup("Inbt", 70, 2)
        jump Jubes_IP_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ JubesX.FaceChange("bemused", 1)
        ch_v "Nope."
        $ JubesX.Blush = 0
    return


label Jubes_IP_Prep: #Animation set-up
    if not JubesX.InsertP:
        $ JubesX.InsertP = 1
        $ JubesX.SEXP += 10
        if JubesX.Forced:
            $ JubesX.Statup("Love", 90, -60)
            $ JubesX.Statup("Obed", 70, 55)
            $ JubesX.Statup("Inbt", 80, 35)
        else:
            $ JubesX.Statup("Love", 90, 10)
            $ JubesX.Statup("Obed", 70, 20)
            $ JubesX.Statup("Inbt", 80, 25)

    if not JubesX.Forced and Situation != "auto":
        call Girl_Undress(JubesX,"bottom")
        if "angry" in JubesX.RecentActions:
            return

#    call Jubes_Pussy_Launch("insert pussy")
    if Taboo:
        $ JubesX.Inbt += int(Taboo/10)
        $ JubesX.Lust += int(Taboo/5)

    $ Line = 0
    $ Speed = 2
    return

# end JubesX.Insert Pussy /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Pussy
label Jubes_Lick_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JubesX)
                                                                                  # Will she let you fondle? Modifiers
    if JubesX.LickP: #You've done it before
        $ temp_modifier += 15
    if JubesX.PantsNum() >= 6 or JubesX.HoseNum() >= 5: # she's got pants on.
        $ temp_modifier -= 15
    if JubesX.Lust > 95:
        $ temp_modifier += 20
    elif JubesX.Lust > 85: #She's really horny
        $ temp_modifier += 15
    if Situation == "shift":
        $ temp_modifier += 10
    if JubesX.Lust > 85 and Situation == "auto": #She's really horny
        $ temp_modifier += 10
    if "exhibitionist" in JubesX.Traits:
        $ temp_modifier += (4*Taboo)
    if JubesX in Player.Harem or "sex friend" in JubesX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JubesX.Traits:
        $ temp_modifier -= 25
    if JubesX.ForcedCount and not JubesX.Forced:
        $ temp_modifier -= 5 * JubesX.ForcedCount

    if Taboo and "tabno" in JubesX.DailyActions:
        $ temp_modifier -= 10
    if Taboo and "public" not in JubesX.History:
        $ temp_modifier -= 20

    if "no lick pussy" in JubesX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no lick pussy" in JubesX.RecentActions else 0

    $ Approval = ApprovalCheck(JubesX, 1250, TabM = 4) # 125, 140, 155, Taboo -160(285)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ JubesX.FaceChange("surprised")
            $ JubesX.Statup("Obed", 90, 1)
            $ JubesX.Statup("Obed", 70, 2)
            $ JubesX.Statup("Inbt", 70, 3)
            $ JubesX.Statup("Inbt", 30, 2)
            "As you crouch down and start to lick her pussy, [JubesX.Name] starts, but then softens."
            $ JubesX.FaceChange("sexy")
            jump Jubes_LP_Prep
        else:
            $ JubesX.FaceChange("surprised")
            $ JubesX.Statup("Love", 80, -2)
            $ JubesX.Statup("Obed", 50, -3)
            ch_v "Hey, good instincts, but maybe hold off?"
            $ JubesX.FaceChange("perplexed",1)
            "She pushes your head back away from her."
            $ temp_modifier = 0
            $ Trigger2 = 0
            return

    if "lick pussy" in JubesX.RecentActions:
        $ JubesX.FaceChange("sexy", 1)
        ch_v "Mmmm, again? I guess. . ."
        jump Jubes_LP_Prep
    elif "lick pussy" in JubesX.DailyActions:
        $ JubesX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Huh? Again?",
            "I must have done something right.",
            "I guess fair's fair. . .",
            "Mmm. . ."])
        ch_v "[Line]"

    if Approval >= 2:                                                                   #She's into it. . .
        if JubesX.Forced:
            $ JubesX.FaceChange("sad")
            $ JubesX.Statup("Love", 70, -3, 1)
            $ JubesX.Statup("Love", 20, -2, 1)
            $ JubesX.Statup("Obed", 90, 1)
            $ JubesX.Statup("Inbt", 60, 1)
            ch_v "If you haveta. . ."
        else:
            $ JubesX.FaceChange("sexy", 1)
            $ JubesX.Eyes = "closed"
            $ JubesX.Statup("Love", 90, 1)
            $ JubesX.Statup("Inbt", 50, 3)
            $ JubesX.Statup("Lust", 200, 3)
            ch_v "Mmmmmm. . ."
        $ JubesX.Statup("Obed", 20, 1)
        $ JubesX.Statup("Obed", 60, 1)
        $ JubesX.Statup("Inbt", 70, 2)
        jump Jubes_LP_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ JubesX.FaceChange("angry", 1)
        if "no lick pussy" in JubesX.RecentActions:
            ch_v "I already told you, \"no\"."
        elif Taboo and "tabno" in JubesX.DailyActions and "no lick pussy" in JubesX.DailyActions:
            ch_v "You already got your answer!"
        elif "no lick pussy" in JubesX.DailyActions:
            ch_v "Don't make me tell you again today."
        elif Taboo and "tabno" in JubesX.DailyActions:
            ch_v "I told you, not here, [JubesX.Petname]."
        elif not JubesX.LickP:
            $ JubesX.FaceChange("bemused")
            ch_v "I'm not sure we're there yet, [JubesX.Petname]. . ."
        else:
            $ JubesX.FaceChange("bemused")
            ch_v "I'm really not cool with that. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no lick pussy" in JubesX.DailyActions:
                $ JubesX.FaceChange("bemused")
                ch_v "Yeah, whatever."
                return
            "I'm sure I can convince you later. . ." if "no lick pussy" not in JubesX.DailyActions:
                $ JubesX.FaceChange("sexy")
                ch_v "I'll be thinking about it, [JubesX.Petname]."
                $ JubesX.Statup("Love", 80, 2)
                $ JubesX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ JubesX.RecentActions.append("tabno")
                    $ JubesX.DailyActions.append("tabno")
                $ JubesX.RecentActions.append("no lick pussy")
                $ JubesX.DailyActions.append("no lick pussy")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ JubesX.FaceChange("sexy")
                    $ JubesX.Statup("Obed", 90, 2)
                    $ JubesX.Statup("Obed", 50, 2)
                    ch_v "You make a good point. . ."
                    $ JubesX.Statup("Inbt", 70, 3)
                    $ JubesX.Statup("Inbt", 40, 2)
                    jump Jubes_LP_Prep
                else:
                    $ JubesX.FaceChange("sexy")
                    ch_v "I would, but still no, [JubesX.Petname]."

            "[[Get in there anyway]":                                               # Pressured into being licked.
                $ Approval = ApprovalCheck(JubesX, 750, "OI", TabM = 4) # 75, 90, 105, -160(235)
                if Approval > 1 or (Approval and JubesX.Forced):
                    $ JubesX.FaceChange("sad")
                    $ JubesX.Statup("Love", 70, -5, 1)
                    $ JubesX.Statup("Love", 200, -2)
                    ch_v "Well I don't want to get in your way. . ."
                    $ JubesX.Statup("Obed", 50, 4)
                    $ JubesX.Statup("Inbt", 80, 1)
                    $ JubesX.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ JubesX.Forced = 1
                    jump Jubes_LP_Prep
                else:
                    $ JubesX.Statup("Love", 200, -15)
                    $ JubesX.FaceChange("angry", 1)
                    "She shoves your head back."
                    $ JubesX.RecentActions.append("angry")
                    $ JubesX.DailyActions.append("angry")

    if "no lick pussy" in JubesX.DailyActions:
        ch_v "I'm pretty clear on this, NO."
        $ JubesX.RecentActions.append("angry")
        $ JubesX.DailyActions.append("angry")
    elif JubesX.Forced:
        $ JubesX.FaceChange("angry", 1)
        ch_v "I really can't, [JubesX.Petname]."
        $ JubesX.Statup("Lust", 80, 5)
        $ JubesX.Statup("Obed", 50, -2)
        $ JubesX.RecentActions.append("angry")
        $ JubesX.DailyActions.append("angry")
    elif Taboo:
        $ JubesX.FaceChange("angry", 1)
        $ JubesX.RecentActions.append("tabno")
        $ JubesX.DailyActions.append("tabno")
        ch_v "I don't wanna make a scene."
    elif JubesX.LickP:
        $ JubesX.FaceChange("sad")
        ch_v "Keep your head out of there."
    else:
        $ JubesX.FaceChange("surprised")
        ch_v "Yeah, sorry."
        $ JubesX.FaceChange()
    $ JubesX.RecentActions.append("no lick pussy")
    $ JubesX.DailyActions.append("no lick pussy")
    $ temp_modifier = 0
    return

label Jubes_LP_Prep: #Animation set-up
    if Trigger2 == "lick pussy": #fix pull down pants now an option, make it work
        return

    $ temp_modifier = 0
    call Jubes_Pussy_Launch("lick pussy")

    if Situation == JubesX:
            #Jubes auto-starts
            $ Situation = 0
            if (JubesX.Legs and not JubesX.Upskirt) or (JubesX.Panties and not JubesX.PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck(JubesX, 1250, TabM = 1) or (JubesX.SeenPussy and ApprovalCheck(JubesX, 500) and not Taboo):
                        $ JubesX.Upskirt = 1
                        $ JubesX.PantiesDown = 1
                        $ Line = 0
                        if JubesX.PantsNum() == 5:
                            $ Line = JubesX.Name + " hikes up her skirt"
                        elif JubesX.PantsNum() >= 6:
                            $ Line = JubesX.Name + " pulls down her " + JubesX.Legs
                        else:
                            $ Line = 0
                        if JubesX.Panties:
                            if Line:
                                #wearing pants
                                "[Line] and pulls her [JubesX.Panties] out of the way."
                                "She then grabs your head and wraps her thighs around it, clearly intending you to get to work."
                            else:
                                #no pants
                                "She pulls her [JubesX.Panties] out of the way, and then wraps her thighs around your head."
                                "She clearly intends for you to get to work."
                        else:
                            #pants but no panties
                            "[Line], and then wraps her thighs around your head."
                            "She clearly intends for you to get to work."
                        call Jubes_First_Bottomless(1)
                else:
                        "[JubesX.Name] grabs your head and wraps her thighs around it, clearly intending you to get to work."
            else:
                        "[JubesX.Name] grabs your head and wraps her thighs around it, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":
                    $ JubesX.Statup("Inbt", 80, 3)
                    $ JubesX.Statup("Inbt", 50, 2)
                    "You start licking."
                "Praise her.":
                    $ JubesX.FaceChange("sexy", 1)
                    $ JubesX.Statup("Inbt", 80, 3)
                    ch_p "Mmm, I like this idea, [JubesX.Pet]."
                    $ JubesX.NameCheck() #checks reaction to petname
                    "You start licking."
                    $ JubesX.Statup("Love", 85, 1)
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your head away."
                    $ JubesX.FaceChange("surprised")
                    $ JubesX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that right now, [JubesX.Pet]."
                    $ JubesX.NameCheck() #checks reaction to petname
                    "[JubesX.Name] pulls back."
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Obed", 50, 1)
                    $ JubesX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ JubesX.AddWord(1,"refused","refused")
                    return
            #end auto

    if not JubesX.Forced and Situation != "auto":
        $ temp_modifier = 0
        if JubesX.PantsNum() >= 6 and not JubesX.Upskirt:
            $ temp_modifier = 15
        call Bottoms_Off(JubesX)
        if "angry" in JubesX.RecentActions:
            return

    if not JubesX.LickP:
        if JubesX.Forced:
            $ JubesX.Statup("Love", 90, -30)
            $ JubesX.Statup("Obed", 70, 35)
            $ JubesX.Statup("Inbt", 80, 75)
        else:
            $ JubesX.Statup("Love", 90, 35)
            $ JubesX.Statup("Obed", 70, 15)
            $ JubesX.Statup("Inbt", 80, 35)
    if Taboo:
        $ JubesX.Inbt += int(Taboo/10)
        $ JubesX.Lust += int(Taboo/5)
    if Situation:
        $ renpy.pop_call()
        $ Situation = 0

    if JubesX.PantsNum() == 5:
        $ JubesX.Upskirt = 1
        $ JubesX.SeenPanties = 1
    call Jubes_First_Bottomless(1)

    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ JubesX.DrainWord("tabno")
    $ JubesX.DrainWord("no lick pussy")
    $ JubesX.RecentActions.append("lick pussy")
    $ JubesX.DailyActions.append("lick pussy")
    call Jubes_Pussy_Launch("lick pussy")

label Jubes_LP_Cycle: #Repeating strokes
    if Trigger2 == "kiss you":
            $ Trigger2 = 0
    while Round > 0:
        call ViewShift(JubesX,JubesX.Pose,0,"lick pussy")
        call Shift_Focus(JubesX)
        $ JubesX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(JubesX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Jubes_LP_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0
                        "View":
                                    call ViewShift(JubesX,"menu")
                                    jump Jubes_LP_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if JubesX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ JubesX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")

                                    "Shift primary action":
                                            if JubesX.Action and MultiAction:
                                                    menu:
                                                        "Pull out and start rubbing again.":
                                                                if JubesX.Action and MultiAction:
                                                                    $ Situation = "pullback"
                                                                    call Jubes_LP_After
                                                                    call Jubes_Fondle_Pussy
                                                                else:
                                                                    call Sex_Basic_Dialog(JubesX,"tired")
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Jubes_LP_After
                                                                call Jubes_Dildo_Pussy
                                                        "Never Mind":
                                                                jump Jubes_LP_Cycle
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Jubes_LP_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [JubesX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(JubesX)
                                            "Ask [JubesX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(JubesX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(JubesX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jubes_LP_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jubes_LP_Cycle
                                            "Never mind":
                                                        jump Jubes_LP_Cycle

                                    "Show her feet" if not ShowFeet and (JubesX.Pose == "doggy" or JubesX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (JubesX.Pose == "doggy" or JubesX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [JubesX.Name]":
                                            call Girl_Undress(JubesX)
                                    "Clean up [JubesX.Name] (locked)" if not JubesX.Spunk:
                                            pass
                                    "Clean up [JubesX.Name]" if JubesX.Spunk:
                                            call Girl_Cleanup(JubesX,"ask")
                                    "Never mind":
                                            jump Jubes_LP_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Jubes_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Jubes_LP_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Jubes_Pos_Reset
                                    $ Line = 0
                                    jump Jubes_LP_After
        #End menu (if Line)

        if JubesX.Panties or JubesX.PantsNum() >= 6 or JubesX.HoseNum() >= 5: #This checks if Jubes wants to strip down.
                call Girl_Undress(JubesX,"auto")

        call Shift_Focus(JubesX)
        call Sex_Dialog(JubesX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JubesX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JubesX)
                            if "angry" in JubesX.RecentActions:
                                call Jubes_Pos_Reset
                                return
                            $ JubesX.Statup("Lust", 200, 5)
                            if 100 > JubesX.Lust >= 70 and JubesX.OCount < 2:
                                $ JubesX.RecentActions.append("unsatisfied")
                                $ JubesX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jubes_LP_After
                            $ Line = "came"

                    if JubesX.Lust >= 100:
                            #If Jubes can cum
                            call Girl_Cumming(JubesX)
                            if Situation == "shift" or "angry" in JubesX.RecentActions:
                                jump Jubes_LP_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in JubesX.RecentActions:#And Jubes is unsatisfied,
                                    "[JubesX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Jubes_LP_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if JubesX.SEXP >= 100 or ApprovalCheck(JubesX, 1200, "LO"):
            pass
        elif Cnt == (5 + JubesX.LickP):
                    $ JubesX.Brows = "confused"
                    ch_v "Yeah, I like that too. . ."
        elif JubesX.Lust >= 80:
                    pass
        elif Cnt == (15 + JubesX.LickP) and JubesX.SEXP >= 15 and not ApprovalCheck(JubesX, 1500):
                    $ JubesX.Brows = "confused"
                    menu:
                        ch_v "Could we maybe try. . . something else?"
                        "Finish up.":
                                "You let go. . ."
                                jump Jubes_LP_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Jubes_LP_After
                        "No, this is fun.":
                                if ApprovalCheck(JubesX, 1200) or ApprovalCheck(JubesX, 500, "O"):
                                    $ JubesX.Statup("Love", 200, -5)
                                    $ JubesX.Statup("Obed", 50, 3)
                                    $ JubesX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ JubesX.FaceChange("angry", 1)
                                    call Jubes_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_v "This is kinda boring. . .."
                                    $ JubesX.Statup("Love", 50, -3, 1)
                                    $ JubesX.Statup("Love", 80, -4, 1)
                                    $ JubesX.Statup("Obed", 30, -1, 1)
                                    $ JubesX.Statup("Obed", 50, -1, 1)
                                    $ JubesX.RecentActions.append("angry")
                                    $ JubesX.DailyActions.append("angry")
                                    jump Jubes_LP_After
        #End Count check

        call Escalation(JubesX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(JubesX,10) #"I could use a break soon. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(JubesX,5)   #". . . I could really use a break here. . ."

    #Round = 0 loop breaks
    $ JubesX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(JubesX,"done") # ch_s "Ok, that's it, I need a break."


label Jubes_LP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Jubes_Pos_Reset

    $ JubesX.FaceChange("sexy")

    $ JubesX.LickP += 1
    $ JubesX.Action -=1
    if JubesX.PantsNum() < 6 or JubesX.Upskirt:
        $ JubesX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ JubesX.Addictionrate += 1

    if Partner == "Rogue":
        call Partner_Like(JubesX,3,2)
    else:
        call Partner_Like(JubesX,2)

    if JubesX.LickP == 1:
            $ JubesX.SEXP += 10
            if not Situation:
                if JubesX.Love >= 500 and "unsatisfied" not in JubesX.RecentActions:
                    ch_v "You really give me a run for my money. . ."
                elif JubesX.Obed <= 500 and Player.Focus <= 20:
                    $ JubesX.FaceChange("perplexed", 1)
                    ch_v "Well, that wasn't so bad. . ."

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_v "Oh? What did you have in mind?"
    call Checkout
    return


# end JubesX.Lick Pussy /////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////Start Fondle Ass
label Jubes_Fondle_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JubesX)
                                                                                     # Will she let you fondle? Modifiers
    if JubesX.FondleA: #You've done it before
        $ temp_modifier += 10
    if JubesX.PantsNum() >= 6 or JubesX.HoseNum() >= 5: # she's got pants on.
        $ temp_modifier -= 5
    if JubesX.Lust > 75: #She's really horny
        $ temp_modifier += 15
    if "exhibitionist" in JubesX.Traits:
        $ temp_modifier += Taboo
    if JubesX in Player.Harem or "sex friend" in JubesX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JubesX.Traits:
        $ temp_modifier -= 25
    if JubesX.ForcedCount and not JubesX.Forced:
        $ temp_modifier -= 5 * JubesX.ForcedCount

    if Taboo and "tabno" in JubesX.DailyActions:
        $ temp_modifier -= 10
    if Taboo and "public" not in JubesX.History:
        $ temp_modifier -= 20

    if "no fondle ass" in JubesX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no fondle ass" in JubesX.RecentActions else 0

    $ Approval = ApprovalCheck(JubesX, 850, TabM=1) # 85, 100, 115, Taboo -40(125)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ JubesX.FaceChange("surprised", 1)
            $ JubesX.Statup("Obed", 70, 2)
            $ JubesX.Statup("Inbt", 40, 2)
            "As your hand creeps down her backside, [JubesX.Name] shivers a bit, and then relaxes."
            $ JubesX.FaceChange("sexy")
            jump Jubes_FA_Prep
        else:
            $ JubesX.FaceChange("surprised")
            $ JubesX.Statup("Obed", 50, -3)
            ch_v "Hands off, [JubesX.Petname]."
            $ JubesX.FaceChange("bemused")
            $ temp_modifier = 0
            $ Trigger2 = 0
            return

    if Situation == "pullback":
        $ JubesX.FaceChange("surprised")
        $ JubesX.Brows = "sad"
        if JubesX.Lust > 80:
            $ JubesX.Statup("Love", 70, -4)
        $ JubesX.Statup("Obed", 90, 1)
        $ JubesX.Statup("Obed", 70, 2)
        "As your finger slides out, [JubesX.Name] gasps and looks upset."
        jump Jubes_FA_Prep
    elif "fondle ass" in JubesX.RecentActions:
        $ JubesX.FaceChange("sexy", 1)
        ch_v "Mmmm, again? I guess. . ."
        jump Jubes_FA_Prep
    elif "fondle ass" in JubesX.DailyActions:
        $ JubesX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Mmm, you like that? . .",
            "Mmm. . ."])
        ch_v "[Line]"

    if Approval >= 2:                                                                   #She's into it. . .
        if JubesX.Forced:
            $ JubesX.FaceChange("sad")
            $ JubesX.Statup("Love", 70, -2, 1)
            $ JubesX.Statup("Obed", 90, 2)
            $ JubesX.Statup("Inbt", 60, 2)
            ch_v "If you insist. . ."
        else:
            $ JubesX.FaceChange("bemused, 1")
            ch_v "Yeah, ok. . ."
        $ JubesX.Statup("Lust", 200, 3)
        $ JubesX.Statup("Obed", 60, 1)
        $ JubesX.Statup("Inbt", 70, 1)
        jump Jubes_FA_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ JubesX.FaceChange("angry", 1)
        if "no fondle ass" in JubesX.RecentActions:
            ch_v "I already told you, \"no\"."
        elif Taboo and "tabno" in JubesX.DailyActions and "no fondle ass" in JubesX.DailyActions:
            ch_v "I told you not to touch me like that in public!"
        elif "no fondle ass" in JubesX.DailyActions:
            ch_v "Don't make me tell you again today."
        elif Taboo and "tabno" in JubesX.DailyActions:
            ch_v "I told you, not here, [JubesX.Petname]."
        elif not JubesX.FondleA:
            $ JubesX.FaceChange("bemused")
            ch_v "Not yet, [JubesX.Petname]. . ."
        else:
            $ JubesX.FaceChange("bemused")
            ch_v "Let's not, ok [JubesX.Petname]?"
        menu:
            extend ""
            "Sorry, never mind." if "no fondle ass" in JubesX.DailyActions:
                $ JubesX.FaceChange("bemused")
                ch_v "Yeah, whatever."
                return
            "Maybe later?" if "no fondle ass" not in JubesX.DailyActions:
                $ JubesX.FaceChange("sexy")
                ch_v "Maybe?"
                $ JubesX.Statup("Love", 80, 2)
                $ JubesX.Statup("Inbt", 50, 2)
                if Taboo:
                    $ JubesX.RecentActions.append("tabno")
                    $ JubesX.DailyActions.append("tabno")
                $ JubesX.RecentActions.append("no fondle ass")
                $ JubesX.DailyActions.append("no fondle ass")
                return
            "Just one good squeeze?":
                if Approval:
                    $ JubesX.FaceChange("sexy")
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Obed", 50, 2)
                    ch_v "Oooh, beg for me. . ."
                    $ JubesX.Statup("Inbt", 70, 1)
                    $ JubesX.Statup("Inbt", 40, 2)
                    jump Jubes_FA_Prep
                else:
                    $ JubesX.FaceChange("sexy")
                    ch_v "No."

            "[[Start fondling anyway]":                                               # Pressured into fondling.
                $ Approval = ApprovalCheck(JubesX, 250, "OI", TabM = 3) # 25, 40, 55, -120(145)
                if Approval > 1 or (Approval and JubesX.Forced):
                    $ JubesX.FaceChange("sad")
                    $ JubesX.Statup("Love", 70, -3, 1)
                    $ JubesX.Statup("Love", 200, -1)
                    ch_v "Fine, I guess."
                    $ JubesX.Statup("Obed", 50, 3)
                    $ JubesX.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ JubesX.Forced = 1
                    jump Jubes_FA_Prep
                else:
                    $ JubesX.Statup("Love", 200, -10)
                    $ JubesX.FaceChange("angry", 1)
                    "She slaps your hand away."
                    $ JubesX.RecentActions.append("angry")
                    $ JubesX.DailyActions.append("angry")

    if "no fondle ass" in JubesX.DailyActions:
        ch_v "I'm pretty clear on this, NO."
        $ JubesX.RecentActions.append("angry")
        $ JubesX.DailyActions.append("angry")
    elif JubesX.Forced:
        $ JubesX.FaceChange("angry", 1)
        ch_v "Do you want to keep those fingers?"
        $ JubesX.Statup("Lust", 60, 5)
        $ JubesX.Statup("Obed", 50, -2)
        $ JubesX.RecentActions.append("angry")
        $ JubesX.DailyActions.append("angry")
    elif Taboo:
        $ JubesX.FaceChange("angry", 1)
        $ JubesX.RecentActions.append("tabno")
        $ JubesX.DailyActions.append("tabno")
        ch_v "I don't wanna make a scene."
    elif JubesX.FondleA:
        $ JubesX.FaceChange("sad")
        ch_v "Sorry, keep your hands to yourself."
    else:
        $ JubesX.FaceChange("sexy")
        $ JubesX.Mouth = "sad"
        ch_v "No."
    $ JubesX.RecentActions.append("no fondle ass")
    $ JubesX.DailyActions.append("no fondle ass")
    $ temp_modifier = 0
    return

ch_v "Sorry, I don't even know how I got here. . ."
return

label Jubes_FA_Prep: #Animation set-up
    if Trigger2 == "fondle ass":
        return
    if not JubesX.Forced and Situation != "auto":
        $ temp_modifier = 0
        call Bottoms_Off(JubesX)
        if "angry" in JubesX.RecentActions:
            return
    $ temp_modifier = 0
    call Jubes_Pussy_Launch("fondle ass")
    if not JubesX.FondleA:
        if JubesX.Forced:
            $ JubesX.Statup("Love", 90, -20)
            $ JubesX.Statup("Obed", 70, 20)
            $ JubesX.Statup("Inbt", 80, 15)
        else:
            $ JubesX.Statup("Love", 90, 10)
            $ JubesX.Statup("Obed", 70, 12)
            $ JubesX.Statup("Inbt", 80, 20)
    if Taboo:
        $ JubesX.Inbt += int(Taboo/10)
        $ JubesX.Lust += int(Taboo/5)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ JubesX.DrainWord("tabno")
    $ JubesX.DrainWord("no fondle ass")
    $ JubesX.RecentActions.append("fondle ass")
    $ JubesX.DailyActions.append("fondle ass")
    call Jubes_Pussy_Launch("fondle ass")

label Jubes_FA_Cycle: #Repeating strokes
    while Round > 0:
        call ViewShift(JubesX,JubesX.Pose,0,"fondle ass")
        call Shift_Focus(JubesX)
        $ JubesX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(JubesX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Jubes_FA_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0
                        "View":
                                    call ViewShift(JubesX,"menu")
                                    jump Jubes_FA_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if JubesX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ JubesX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")

                                    "Shift primary action":
                                            if JubesX.Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in.":
                                                                $ Situation = "shift"
                                                                call Jubes_FA_After
                                                                call Jubes_Insert_Ass
                                                        "Just stick a finger in without asking.":
                                                                $ Situation = "auto"
                                                                call Jubes_FA_After
                                                                call Jubes_Insert_Ass
                                                        "I want to lick your asshole.":
                                                                $ Situation = "shift"
                                                                call Jubes_FA_After
                                                                call Jubes_Lick_Ass
                                                        "Just start licking.":
                                                                $ Situation = "auto"
                                                                call Jubes_FA_After
                                                                call Jubes_Lick_Ass
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Jubes_FA_After
                                                                call Jubes_Dildo_Ass
                                                        "Never Mind":
                                                                jump Jubes_FA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Jubes_FA_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [JubesX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(JubesX)
                                            "Ask [JubesX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(JubesX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(JubesX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jubes_FA_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jubes_FA_Cycle
                                            "Never mind":
                                                        jump Jubes_FA_Cycle

                                    "Show her feet" if not ShowFeet and (JubesX.Pose == "doggy" or JubesX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (JubesX.Pose == "doggy" or JubesX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [JubesX.Name]":
                                            call Girl_Undress(JubesX)
                                    "Clean up [JubesX.Name] (locked)" if not JubesX.Spunk:
                                            pass
                                    "Clean up [JubesX.Name]" if JubesX.Spunk:
                                            call Girl_Cleanup(JubesX,"ask")
                                    "Never mind":
                                            jump Jubes_FA_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Jubes_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Jubes_FA_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Jubes_Pos_Reset
                                    $ Line = 0
                                    jump Jubes_FA_After
        #End menu (if Line)

        if JubesX.Panties or JubesX.PantsNum() >= 6 or JubesX.HoseNum() >= 5: #This checks if Jubes wants to strip down.
                call Girl_Undress(JubesX,"auto")

        call Shift_Focus(JubesX)
        call Sex_Dialog(JubesX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JubesX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JubesX)
                            if "angry" in JubesX.RecentActions:
                                call Jubes_Pos_Reset
                                return
                            $ JubesX.Statup("Lust", 200, 5)
                            if 100 > JubesX.Lust >= 70 and JubesX.OCount < 2 and JubesX.SEXP >= 20:
                                $ JubesX.RecentActions.append("unsatisfied")
                                $ JubesX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jubes_FA_After
                            $ Line = "came"

                    if JubesX.Lust >= 100:
                            #If Jubes can cum
                            call Girl_Cumming(JubesX)
                            if Situation == "shift" or "angry" in JubesX.RecentActions:
                                jump Jubes_FA_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in JubesX.RecentActions:#And Jubes is unsatisfied,
                                    "[JubesX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Jubes_FA_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if JubesX.SEXP >= 100 or ApprovalCheck(JubesX, 1200, "LO"):
            pass
        elif Cnt == (5 + JubesX.FondleA):
                    $ JubesX.Brows = "confused"
                    ch_v "Mmmm. . ."
        elif JubesX.Lust >= 80:
                    pass
        elif Cnt == (15 + JubesX.FondleA) and JubesX.SEXP >= 15 and not ApprovalCheck(JubesX, 1500):
                    $ JubesX.Brows = "confused"
                    menu:
                        ch_v "Could we maybe try. . . something else?"
                        "Finish up.":
                                "You let go. . ."
                                jump Jubes_FA_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Jubes_FA_After
                        "No, this is fun.":
                                if ApprovalCheck(JubesX, 1200) or ApprovalCheck(JubesX, 500, "O"):
                                    $ JubesX.Statup("Love", 200, -5)
                                    $ JubesX.Statup("Obed", 50, 3)
                                    $ JubesX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ JubesX.FaceChange("angry", 1)
                                    call Jubes_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_v "This is kinda boring. . .."
                                    $ JubesX.Statup("Love", 50, -3, 1)
                                    $ JubesX.Statup("Love", 80, -4, 1)
                                    $ JubesX.Statup("Obed", 30, -1, 1)
                                    $ JubesX.Statup("Obed", 50, -1, 1)
                                    $ JubesX.RecentActions.append("angry")
                                    $ JubesX.DailyActions.append("angry")
                                    jump Jubes_FA_After
        #End Count check

        call Escalation(JubesX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(JubesX,10) #"I could use a break soon. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(JubesX,5)   #". . . I could really use a break here. . ."

    #Round = 0 loop breaks
    $ JubesX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(JubesX,"done") # ch_s "Ok, that's it, I need a break."


label Jubes_FA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Jubes_Pos_Reset

    $ JubesX.FaceChange("sexy")

    $ JubesX.FondleA += 1
    $ JubesX.Action -=1
    if JubesX.PantsNum() < 6 or JubesX.Upskirt:
        $ JubesX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ JubesX.Addictionrate += 1

        call Partner_Like(JubesX,2)

    if JubesX.FondleA == 1:
            $ JubesX.SEXP += 4
            if not Situation:
                if JubesX.Love >= 500 and "unsatisfied" not in JubesX.RecentActions:
                    ch_v "That was. . . nice. . ."
                elif JubesX.Obed <= 500 and Player.Focus <= 20:
                    $ JubesX.FaceChange("perplexed", 1)
                    ch_v "Did you like that?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_v "Oh? What did you have in mind?"
    call Checkout
    return


# end JubesX.Fondle Ass /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Ass
label Jubes_Insert_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JubesX)

    if JubesX.InsertA: #You've done it before
        $ temp_modifier += 25
    if JubesX.PantsNum() >= 6 or JubesX.HoseNum() >= 5: # she's got pants on.
        $ temp_modifier -= 15
    if JubesX.Lust > 85 and JubesX.Loose: #She's really horny
        $ temp_modifier += 15
    if JubesX.Lust > 95 and JubesX.Loose:
        $ temp_modifier += 5
    if Situation == "shift":
        $ temp_modifier += 10
    if JubesX.Lust > 85 and Situation == "auto": #She's really horny
        $ temp_modifier += 10
    if "exhibitionist" in JubesX.Traits:
        $ temp_modifier += (4*Taboo)
    if JubesX in Player.Harem or "sex friend" in JubesX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JubesX.Traits:
        $ temp_modifier -= 25
    if JubesX.ForcedCount and not JubesX.Forced:
        $ temp_modifier -= 5 * JubesX.ForcedCount

    if Taboo and "tabno" in JubesX.DailyActions:
        $ temp_modifier -= 10
    if Taboo and "public" not in JubesX.History:
        $ temp_modifier -= 20

    if "no insert ass" in JubesX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no insert ass" in JubesX.RecentActions else 0

    $ Approval = ApprovalCheck(JubesX, 1300, TabM = 3) # 130, 145, 160, Taboo -120(250)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ JubesX.FaceChange("surprised")
            $ JubesX.Statup("Obed", 90, 2)
            $ JubesX.Statup("Obed", 70, 2)
            $ JubesX.Statup("Inbt", 80, 2)
            $ JubesX.Statup("Inbt", 30, 2)
            "As you slide a finger in, [JubesX.Name] tightens around it in surprise, but seems into it."
            $ JubesX.FaceChange("sexy")
            jump Jubes_IA_Prep
        else:
            $ JubesX.FaceChange("surprised")
            $ JubesX.Statup("Love", 80, -2)
            $ JubesX.Statup("Obed", 50, -3)
            ch_v "Whoa, back off, [JubesX.Petname]."
            $ temp_modifier = 0
            $ Trigger2 = 0
            return

    if "insert ass" in JubesX.DailyActions and not JubesX.Loose:
        $ JubesX.FaceChange("bemused", 1)
        ch_v "I'm still a little sore from earlier, [JubesX.Petname]."
    elif "insert ass" in JubesX.DailyActions:
        $ JubesX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax. . .",
            "Mmm. . ."])
        ch_v "[Line]"

    if Approval >= 2:                                                                   #She's into it. . .
        if JubesX.Forced:
            $ JubesX.FaceChange("sad")
            $ JubesX.Statup("Love", 70, -3, 1)
            $ JubesX.Statup("Love", 20, -2, 1)
            $ JubesX.Statup("Obed", 90, 1)
            $ JubesX.Statup("Inbt", 60, 1)
            ch_v "If you haveta. . ."
        else:
            $ JubesX.FaceChange("sexy", 1)
            $ JubesX.Eyes = "closed"
            $ JubesX.Statup("Love", 90, 1)
            $ JubesX.Statup("Inbt", 50, 3)
            $ JubesX.Statup("Lust", 200, 3)
            ch_v "Mmmmm. . ."
        $ JubesX.Statup("Obed", 20, 1)
        $ JubesX.Statup("Obed", 60, 1)
        $ JubesX.Statup("Inbt", 70, 2)
        jump Jubes_IA_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ JubesX.FaceChange("angry", 1)
        if "no insert ass" in JubesX.RecentActions:
            ch_v "I already told you, \"no\"."
        elif Taboo and "tabno" in JubesX.DailyActions and "no insert ass" in JubesX.DailyActions:
            ch_v "I told you that wasn't appropriate!"
        elif "no insert ass" in JubesX.DailyActions:
            ch_v "Don't make me tell you again today."
        elif Taboo and "tabno" in JubesX.DailyActions:
            ch_v "I told you, not here, [JubesX.Petname]."
        elif not JubesX.InsertA:
            $ JubesX.FaceChange("perplexed", 1)
            ch_v "That's really not my style. . ."
        else:
            $ JubesX.FaceChange("bemused")
            ch_v "I'd rather not today. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no insert ass" in JubesX.DailyActions:
                $ JubesX.FaceChange("bemused")
                ch_v "Yeah, whatever."
                return
            "Maybe later?" if "no insert ass" not in JubesX.DailyActions:
                $ JubesX.FaceChange("sexy")
                ch_v "It's. . . possible, [JubesX.Petname]."
                $ JubesX.Statup("Love", 80, 2)
                $ JubesX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ JubesX.RecentActions.append("tabno")
                    $ JubesX.DailyActions.append("tabno")
                $ JubesX.RecentActions.append("no insert ass")
                $ JubesX.DailyActions.append("no insert ass")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ JubesX.FaceChange("sexy")
                    $ JubesX.Statup("Obed", 90, 2)
                    $ JubesX.Statup("Obed", 50, 2)
                    ch_v "Um. . . maybe. . ."
                    $ JubesX.Statup("Inbt", 70, 3)
                    $ JubesX.Statup("Inbt", 40, 2)
                    jump Jubes_IA_Prep
                else:
                    $ JubesX.FaceChange("bemused")
                    ch_v "I really doubt that. . ."

            "[[Slide a finger in anyway]":                                               # Pressured into being fingered.
                $ Approval = ApprovalCheck(JubesX, 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                if Approval > 1 or (Approval and JubesX.Forced):
                    $ JubesX.FaceChange("surprised", 1)
                    $ JubesX.Statup("Love", 70, -5, 1)
                    $ JubesX.Statup("Love", 200, -2)
                    ch_v "Um, hello? . ."
                    $ JubesX.FaceChange("sad")
                    $ JubesX.Statup("Obed", 50, 4)
                    $ JubesX.Statup("Inbt", 80, 1)
                    $ JubesX.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ JubesX.Forced = 1
                    jump Jubes_IA_Prep
                else:
                    $ JubesX.Statup("Love", 200, -15)
                    $ JubesX.FaceChange("angry", 1)
                    "She slaps your hand away."
                    $ JubesX.RecentActions.append("angry")
                    $ JubesX.DailyActions.append("angry")

    if "no insert ass" in JubesX.DailyActions:
        ch_v "I'm pretty clear on this, NO."
        $ JubesX.RecentActions.append("angry")
        $ JubesX.DailyActions.append("angry")
    elif JubesX.Forced:
        $ JubesX.FaceChange("angry", 1)
        ch_v "I'm not going there today."
        if ApprovalCheck(JubesX, 500, "I"):
                $ JubesX.Statup("Lust", 80, 10)
        else:
                $ JubesX.Statup("Lust", 50, 3)
        $ JubesX.Statup("Obed", 50, -2)
        $ JubesX.RecentActions.append("angry")
        $ JubesX.DailyActions.append("angry")
    elif Taboo:
        $ JubesX.FaceChange("angry", 1)
        $ JubesX.RecentActions.append("tabno")
        $ JubesX.DailyActions.append("tabno")
        ch_v "I don't wanna make a scene."
    elif JubesX.InsertA:
        $ JubesX.FaceChange("sad")
        ch_v "I'm not into it."
    else:
        $ JubesX.FaceChange("surprised")
        ch_v "Not today, [JubesX.Petname]."
        $ JubesX.FaceChange()
    $ JubesX.RecentActions.append("no insert ass")
    $ JubesX.DailyActions.append("no insert ass")
    $ temp_modifier = 0
    return


label Jubes_IA_Prep: #Animation set-up
    if Trigger2 == "insert ass":
        return

    call Jubes_Pussy_Launch("insert ass")

    if Situation == JubesX:
            #Jubes auto-starts
            $ Situation = 0
            if (JubesX.Legs and not JubesX.Upskirt) or (JubesX.Panties and not JubesX.PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck(JubesX, 1250, TabM = 1) or (JubesX.SeenPussy and ApprovalCheck(JubesX, 500) and not Taboo):
                        $ JubesX.Upskirt = 1
                        $ JubesX.PantiesDown = 1
                        $ Line = 0
                        if JubesX.PantsNum() == 5:
                            $ Line = JubesX.Name + " hikes up her skirt"
                        elif JubesX.PantsNum() >= 6:
                            $ Line = JubesX.Name + " pulls down her " + JubesX.Legs
                        else:
                            $ Line = 0
                        if JubesX.Panties:
                            if Line:
                                #wearing pants
                                "[Line] and pulls her [JubesX.Panties] out of the way."
                                "She then grabs your arm and rubs your hand against her asshole, clearly intending you to get to work."
                            else:
                                #no pants
                                "She pulls her [JubesX.Panties] out of the way, and then rubs your hand against her asshole."
                                "She clearly intends for you to get to work."
                        else:
                            #pants but no panties
                            "[Line], and then rubs your hand against her asshole."
                            "She clearly intends for you to get to work."
                        call Jubes_First_Bottomless(1)
                else:
                        "[JubesX.Name] grabs your arm and rubs your hand against her asshole, clearly intending you to get to work."
            else:
                        "[JubesX.Name] grabs your arm and rubs your hand against her asshole, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":
                    $ JubesX.Statup("Inbt", 80, 3)
                    $ JubesX.Statup("Inbt", 50, 2)
                    "You press your finger into it."
                "Praise her.":
                    $ JubesX.FaceChange("sexy", 1)
                    $ JubesX.Statup("Inbt", 80, 3)
                    ch_p "Dirty girl, [JubesX.Pet]."
                    $ JubesX.NameCheck() #checks reaction to petname
                    "You press your finger into it."
                    $ JubesX.Statup("Love", 85, 1)
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your hand back."
                    $ JubesX.FaceChange("surprised")
                    $ JubesX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that right now, [JubesX.Pet]."
                    $ JubesX.NameCheck() #checks reaction to petname
                    "[JubesX.Name] pulls back."
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Obed", 50, 1)
                    $ JubesX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ JubesX.AddWord(1,"refused","refused")
                    return
            #end auto

    if not JubesX.Forced and Situation != "auto":
        $ temp_modifier = 0
        call Bottoms_Off(JubesX)
        if "angry" in JubesX.RecentActions:
            return

    $ temp_modifier = 0
    if not JubesX.InsertA:
        if JubesX.Forced:
            $ JubesX.Statup("Love", 90, -50)
            $ JubesX.Statup("Obed", 70, 60)
            $ JubesX.Statup("Inbt", 80, 35)
        else:
            $ JubesX.Statup("Love", 90, 10)
            $ JubesX.Statup("Obed", 70, 20)
            $ JubesX.Statup("Inbt", 80, 25)

    if Taboo:
        $ JubesX.Inbt += int(Taboo/10)
        $ JubesX.Lust += int(Taboo/5)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ JubesX.DrainWord("tabno")
    $ JubesX.DrainWord("no insert ass")
    $ JubesX.RecentActions.append("insert ass")
    $ JubesX.DailyActions.append("insert ass")
    call Jubes_Pussy_Launch("insert ass")

label Jubes_IA_Cycle: #Repeating strokes
    while Round > 0:
        call ViewShift(JubesX,JubesX.Pose,0,"insert ass")
        call Shift_Focus(JubesX)
        $ JubesX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(JubesX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Jubes_IA_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0
                        "View":
                                    call ViewShift(JubesX,"menu")
                                    jump Jubes_IA_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if JubesX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ JubesX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")

                                    "Shift primary action":
                                            if JubesX.Action and MultiAction:
                                                    menu:
                                                        "Pull out and start rubbing again.":
                                                                $ Situation = "pullback"
                                                                call Jubes_IA_After
                                                                call Jubes_Fondle_Ass
                                                        "I want to lick your asshole.":
                                                                $ Situation = "shift"
                                                                call Jubes_IA_After
                                                                call Jubes_Lick_Ass
                                                        "Just start licking.":
                                                                $ Situation = "auto"
                                                                call Jubes_IA_After
                                                                call Jubes_Lick_Ass
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Jubes_IA_After
                                                                call Jubes_Dildo_Ass
                                                        "Never Mind":
                                                                jump Jubes_IA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Jubes_IA_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [JubesX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(JubesX)
                                            "Ask [JubesX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(JubesX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(JubesX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jubes_IA_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jubes_IA_Cycle
                                            "Never mind":
                                                        jump Jubes_IA_Cycle

                                    "Show her feet" if not ShowFeet and (JubesX.Pose == "doggy" or JubesX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (JubesX.Pose == "doggy" or JubesX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [JubesX.Name]":
                                            call Girl_Undress(JubesX)
                                    "Clean up [JubesX.Name] (locked)" if not JubesX.Spunk:
                                            pass
                                    "Clean up [JubesX.Name]" if JubesX.Spunk:
                                            call Girl_Cleanup(JubesX,"ask")
                                    "Never mind":
                                            jump Jubes_IA_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Jubes_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Jubes_IA_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Jubes_Pos_Reset
                                    $ Line = 0
                                    jump Jubes_IA_After
        #End menu (if Line)

        if JubesX.Panties or JubesX.PantsNum() >= 6 or JubesX.HoseNum() >= 5: #This checks if Jubes wants to strip down.
                call Girl_Undress(JubesX,"auto")

        call Shift_Focus(JubesX)
        call Sex_Dialog(JubesX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JubesX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JubesX)
                            if "angry" in JubesX.RecentActions:
                                call Jubes_Pos_Reset
                                return
                            $ JubesX.Statup("Lust", 200, 5)
                            if 100 > JubesX.Lust >= 70 and JubesX.OCount < 2:
                                $ JubesX.RecentActions.append("unsatisfied")
                                $ JubesX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jubes_IA_After
                            $ Line = "came"

                    if JubesX.Lust >= 100:
                            #If Jubes can cum
                            call Girl_Cumming(JubesX)
                            if Situation == "shift" or "angry" in JubesX.RecentActions:
                                jump Jubes_IA_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in JubesX.RecentActions:#And Jubes is unsatisfied,
                                    "[JubesX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Jubes_IA_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if JubesX.SEXP >= 100 or ApprovalCheck(JubesX, 1200, "LO"):
            pass
        elif Cnt == (5 + JubesX.InsertA):
                    $ JubesX.Brows = "confused"
                    ch_v "Having fun?"
        elif JubesX.Lust >= 80:
                    pass
        elif Cnt == (15 + JubesX.InsertA) and JubesX.SEXP >= 15 and not ApprovalCheck(JubesX, 1500):
                    $ JubesX.Brows = "confused"
                    menu:
                        ch_v "Could we maybe try. . . something else?"
                        "Finish up.":
                                "You let go. . ."
                                jump Jubes_IA_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Jubes_IA_After
                        "No, this is fun.":
                                if ApprovalCheck(JubesX, 1200) or ApprovalCheck(JubesX, 500, "O"):
                                    $ JubesX.Statup("Love", 200, -5)
                                    $ JubesX.Statup("Obed", 50, 3)
                                    $ JubesX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ JubesX.FaceChange("angry", 1)
                                    call Jubes_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_v "This is kinda boring. . .."
                                    $ JubesX.Statup("Love", 50, -3, 1)
                                    $ JubesX.Statup("Love", 80, -4, 1)
                                    $ JubesX.Statup("Obed", 30, -1, 1)
                                    $ JubesX.Statup("Obed", 50, -1, 1)
                                    $ JubesX.RecentActions.append("angry")
                                    $ JubesX.DailyActions.append("angry")
                                    jump Jubes_IA_After
        #End Count check

        call Escalation(JubesX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(JubesX,10) #"I could use a break soon. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(JubesX,5)   #". . . I could really use a break here. . ."

    #Round = 0 loop breaks
    $ JubesX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(JubesX,"done") # ch_s "Ok, that's it, I need a break."

label Jubes_IA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Jubes_Pos_Reset

    $ JubesX.FaceChange("sexy")

    $ JubesX.InsertA += 1
    $ JubesX.Action -=1
    $ JubesX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ JubesX.Addictionrate += 1

    call Partner_Like(JubesX,2)

    if JubesX.InsertA == 1:
            $ JubesX.SEXP += 12
            if not Situation:
                if JubesX.Love >= 500 and "unsatisfied" not in JubesX.RecentActions:
                    ch_v "That was kinda weird. . ."
                elif JubesX.Obed <= 500 and Player.Focus <= 20:
                    $ JubesX.FaceChange("perplexed", 1)
                    ch_v "Did you like that?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_v "Oh? What did you have in mind?"
    call Checkout
    return


# end JubesX.Insert Ass /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Ass
label Jubes_Lick_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JubesX)
                                                                             # Will she let you lick? Modifiers
    if JubesX.LickA: #You've done it before
        $ temp_modifier += 20
    if JubesX.PantsNum() >= 6 or JubesX.HoseNum() >= 5: # she's got pants on.
        $ temp_modifier -= 25
    if JubesX.Lust > 95:
        $ temp_modifier += 20
    elif JubesX.Lust > 85: #She's really horny
        $ temp_modifier += 15
    if JubesX.Lust > 85 and Situation == "auto": #auto
        $ temp_modifier += 10
    if Situation == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in JubesX.Traits:
        $ temp_modifier += (4*Taboo)
    if JubesX in Player.Harem or "sex friend" in JubesX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JubesX.Traits:
        $ temp_modifier -= 25
    if JubesX.ForcedCount and not JubesX.Forced:
        $ temp_modifier -= 5 * JubesX.ForcedCount

    if Taboo and "tabno" in JubesX.DailyActions:
        $ temp_modifier -= 10
    if Taboo and "public" not in JubesX.History:
        $ temp_modifier -= 20

    if "no lick ass" in JubesX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no lick ass" in JubesX.RecentActions else 0

    $ Approval = ApprovalCheck(JubesX, 1550, TabM = 4) # 155, 170, 185, Taboo -160(315)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ JubesX.FaceChange("surprised")
            $ JubesX.Statup("Obed", 90, 1)
            $ JubesX.Statup("Inbt", 80, 3)
            $ JubesX.Statup("Inbt", 40, 2)
            "As you crouch down and start to lick her asshole, [JubesX.Name] startles briefly, but then begins to melt."
            $ JubesX.FaceChange("sexy")
            jump Jubes_LA_Prep
        else:
            $ JubesX.FaceChange("surprised")
            $ JubesX.Statup("Love", 80, -2)
            $ JubesX.Statup("Obed", 50, -3)
            ch_v "[JubesX.Petname]! No. . ."
            $ temp_modifier = 0
            $ Trigger2 = 0
            return

    if "lick ass" in JubesX.RecentActions:
        $ JubesX.FaceChange("sexy", 1)
        ch_v "Mmmm, again? I guess. . ."
        jump Jubes_LA_Prep
    elif "lick ass" in JubesX.DailyActions:
        $ JubesX.FaceChange("sexy", 1)
        ch_v "You didn't get enough earlier?"


    if Approval >= 2:                                                                   #She's into it. . .
        if JubesX.Forced:
            $ JubesX.FaceChange("sad")
            $ JubesX.Statup("Love", 70, -3, 1)
            $ JubesX.Statup("Love", 20, -2, 1)
            $ JubesX.Statup("Obed", 90, 2)
            $ JubesX.Statup("Inbt", 60, 2)
            ch_v "Meh. . ."
        else:
            $ JubesX.FaceChange("sexy", 1)
            $ JubesX.Eyes = "closed"
            $ JubesX.Statup("Love", 90, 1)
            $ JubesX.Statup("Inbt", 60, 2)
            $ JubesX.Statup("Lust", 200, 3)
            ch_v "Mmm. . . naughty."
        $ JubesX.Statup("Obed", 20, 1)
        $ JubesX.Statup("Obed", 60, 1)
        $ JubesX.Statup("Inbt", 80, 2)
        jump Jubes_LA_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ JubesX.FaceChange("angry", 1)
        if "no lick ass" in JubesX.RecentActions:
            ch_v "I already told you, \"no\"."
        elif Taboo and "tabno" in JubesX.DailyActions and "no lick ass" in JubesX.DailyActions:
            ch_v "I told you not to touch me like that in public!"
        elif "no lick ass" in JubesX.DailyActions:
            ch_v "Don't make me tell you again today."
        elif Taboo and "tabno" in JubesX.DailyActions:
            ch_v "I told you, not here, [JubesX.Petname]."
        elif not JubesX.LickA:                    #First time dialog
            $ JubesX.FaceChange("bemused", 1)
            if JubesX.Love >= JubesX.Obed and JubesX.Love >= JubesX.Inbt:
                ch_v "What? What're you talking about?"
            elif JubesX.Obed >= JubesX.Inbt:
                ch_v "Is that what gets you off?"
            else:
                $ JubesX.Eyes = "sexy"
                ch_v "Hm, I hadn't thought. . ."
        else:
            $ JubesX.FaceChange("bemused")
            ch_v "Not now, [JubesX.Petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no lick ass" in JubesX.DailyActions:
                $ JubesX.FaceChange("bemused")
                ch_v "Yeah, whatever."
                return
            "I'm sure I can convince you later. . ." if "no lick ass" not in JubesX.DailyActions:
                $ JubesX.FaceChange("sexy")
                ch_v "Anything's possible, [JubesX.Petname]."
                $ JubesX.Statup("Love", 80, 2)
                $ JubesX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ JubesX.RecentActions.append("tabno")
                    $ JubesX.DailyActions.append("tabno")
                $ JubesX.RecentActions.append("no lick ass")
                $ JubesX.DailyActions.append("no lick ass")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ JubesX.FaceChange("sexy")
                    $ JubesX.Statup("Obed", 90, 2)
                    $ JubesX.Statup("Obed", 50, 2)
                    ch_v "Um. . . maybe? . ."
                    $ JubesX.Statup("Inbt", 70, 3)
                    $ JubesX.Statup("Inbt", 40, 2)
                    jump Jubes_LA_Prep
                else:
                    $ JubesX.FaceChange("sexy")
                    ch_v "Doubt."

            "[[Start licking anyway]":                                               # Pressured into being licked.
                $ Approval = ApprovalCheck(JubesX, 1100, "OI", TabM = 4) # 110, 125, 140, -160(270)
                if Approval > 1 or (Approval and JubesX.Forced):
                    $ JubesX.FaceChange("sad")
                    $ JubesX.Statup("Love", 70, -5, 1)
                    $ JubesX.Statup("Love", 200, -2)
                    ch_v "Suit yourself."
                    $ JubesX.Statup("Obed", 50, 4)
                    $ JubesX.Statup("Inbt", 80, 1)
                    $ JubesX.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ JubesX.Forced = 1
                    jump Jubes_LA_Prep
                else:
                    $ JubesX.Statup("Love", 200, -15)
                    $ JubesX.FaceChange("angry", 1)
                    "She shoves your head back."
                    $ JubesX.RecentActions.append("angry")
                    $ JubesX.DailyActions.append("angry")

    if "no lick ass" in JubesX.DailyActions:
        ch_v "I'm pretty clear on this, NO."
        $ JubesX.RecentActions.append("angry")
        $ JubesX.DailyActions.append("angry")
    elif JubesX.Forced:
        $ JubesX.FaceChange("angry", 1)
        ch_v "I don't think so."
        if ApprovalCheck(JubesX, 500, "I"):
                $ JubesX.Statup("Lust", 80, 10)
        else:
                $ JubesX.Statup("Lust", 50, 3)
        $ JubesX.Statup("Obed", 50, -2)
        $ JubesX.RecentActions.append("angry")
        $ JubesX.DailyActions.append("angry")
    elif Taboo:
        $ JubesX.FaceChange("angry", 1)
        $ JubesX.RecentActions.append("tabno")
        $ JubesX.DailyActions.append("tabno")
        ch_v "I don't wanna make a scene."
    elif JubesX.LickA:
        $ JubesX.FaceChange("sad")
        ch_v "Sorry, no more of that."
    else:
        $ JubesX.FaceChange("surprised")
        ch_v "I'm sorry, not now."
        $ JubesX.FaceChange()
    $ JubesX.RecentActions.append("no lick ass")
    $ JubesX.DailyActions.append("no lick ass")
    $ temp_modifier = 0
    return

label Jubes_LA_Prep: #Animation set-up
    if Trigger2 == "lick ass":
        return
    if not JubesX.Forced and Situation != "auto":
        $ temp_modifier = 0
        if JubesX.PantsNum() >= 6:
            $ temp_modifier = 15
        call Bottoms_Off(JubesX)
        if "angry" in JubesX.RecentActions:
            return
    $ temp_modifier = 0
    call Jubes_Pussy_Launch("lick ass")
    if not JubesX.LickA:
        if JubesX.Forced:
            $ JubesX.Statup("Love", 90, -30)
            $ JubesX.Statup("Obed", 70, 40)
            $ JubesX.Statup("Inbt", 80, 80)
        else:
            $ JubesX.Statup("Love", 90, 35)
            $ JubesX.Statup("Obed", 70, 25)
            $ JubesX.Statup("Inbt", 80, 55)
    if Taboo:
        $ JubesX.Inbt += int(Taboo/10)
        $ JubesX.Lust += int(Taboo/5)
    if Situation:
        $ renpy.pop_call()
        $ Situation = 0

    $ JubesX.Upskirt = 1
    if JubesX.PantsNum() == 5:
        $ JubesX.SeenPanties = 1
    if not JubesX.Panties:
        call Jubes_First_Bottomless(1)
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ JubesX.DrainWord("tabno")
    $ JubesX.DrainWord("no lick ass")

    $ JubesX.RecentActions.append("lick") if "lick" not in JubesX.RecentActions else JubesX.RecentActions
    $ JubesX.RecentActions.append("ass") if "ass" not in JubesX.RecentActions else JubesX.RecentActions
    $ JubesX.RecentActions.append("lick ass")

    $ JubesX.DailyActions.append("lick") if "lick" not in JubesX.DailyActions else JubesX.RecentActions
    $ JubesX.DailyActions.append("ass") if "ass" not in JubesX.DailyActions else JubesX.RecentActions
    $ JubesX.DailyActions.append("lick ass")
    call Jubes_Pussy_Launch("lick ass")
label Jubes_LA_Cycle: #Repeating strokes
    if Trigger2 == "kiss you":
            $ Trigger2 = 0
    while Round > 0:
        call ViewShift(JubesX,JubesX.Pose,0,"lick ass")
        call Shift_Focus(JubesX)
        $ JubesX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(JubesX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Jubes_LA_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0
                        "View":
                                    call ViewShift(JubesX,"menu")
                                    jump Jubes_LA_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if JubesX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ JubesX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")

                                    "Shift primary action":
                                            if JubesX.Action and MultiAction:
                                                    menu:
                                                        "Switch to fondling.":
                                                                $ Situation = "pullback"
                                                                call Jubes_LA_After
                                                                call Jubes_Fondle_Ass
                                                        "I want to stick a finger in.":
                                                                $ Situation = "shift"
                                                                call Jubes_LA_After
                                                                call Jubes_Insert_Ass
                                                        "Just stick a finger in [[without asking].":
                                                                $ Situation = "auto"
                                                                call Jubes_LA_After
                                                                call Jubes_Insert_Ass
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Jubes_LA_After
                                                                call Jubes_Dildo_Ass
                                                        "Never Mind":
                                                                jump Jubes_LA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Jubes_LA_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [JubesX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(JubesX)
                                            "Ask [JubesX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(JubesX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(JubesX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jubes_LA_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jubes_LA_Cycle
                                            "Never mind":
                                                        jump Jubes_LA_Cycle

                                    "Show her feet" if not ShowFeet and (JubesX.Pose == "doggy" or JubesX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (JubesX.Pose == "doggy" or JubesX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [JubesX.Name]":
                                            call Girl_Undress(JubesX)
                                    "Clean up [JubesX.Name] (locked)" if not JubesX.Spunk:
                                            pass
                                    "Clean up [JubesX.Name]" if JubesX.Spunk:
                                            call Girl_Cleanup(JubesX,"ask")
                                    "Never mind":
                                            jump Jubes_LA_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Jubes_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Jubes_LA_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Jubes_Pos_Reset
                                    $ Line = 0
                                    jump Jubes_LA_After
        #End menu (if Line)

        if JubesX.Panties or JubesX.PantsNum() >= 6 or JubesX.HoseNum() >= 5: #This checks if Jubes wants to strip down.
                call Girl_Undress(JubesX,"auto")

        call Shift_Focus(JubesX)
        call Sex_Dialog(JubesX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JubesX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JubesX)
                            if "angry" in JubesX.RecentActions:
                                call Jubes_Pos_Reset
                                return
                            $ JubesX.Statup("Lust", 200, 5)
                            if 100 > JubesX.Lust >= 70 and JubesX.OCount < 2:
                                $ JubesX.RecentActions.append("unsatisfied")
                                $ JubesX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jubes_LA_After
                            $ Line = "came"

                    if JubesX.Lust >= 100:
                            #If Jubes can cum
                            call Girl_Cumming(JubesX)
                            if Situation == "shift" or "angry" in JubesX.RecentActions:
                                jump Jubes_LA_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in JubesX.RecentActions:#And Jubes is unsatisfied,
                                    "[JubesX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Jubes_LA_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if JubesX.SEXP >= 100 or ApprovalCheck(JubesX, 1200, "LO"):
            pass
        elif Cnt == (5 + JubesX.LickA):
                    $ JubesX.Brows = "confused"
                    ch_v "Having fun?"
        elif JubesX.Lust >= 80:
                    pass
        elif Cnt == (15 + JubesX.LickA) and JubesX.SEXP >= 15 and not ApprovalCheck(JubesX, 1500):
                    $ JubesX.Brows = "confused"
                    menu:
                        ch_v "Could we maybe try. . . something else?"
                        "Finish up.":
                                "You let go. . ."
                                jump Jubes_LA_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Jubes_LA_After
                        "No, this is fun.":
                                if ApprovalCheck(JubesX, 1200) or ApprovalCheck(JubesX, 500, "O"):
                                    $ JubesX.Statup("Love", 200, -5)
                                    $ JubesX.Statup("Obed", 50, 3)
                                    $ JubesX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ JubesX.FaceChange("angry", 1)
                                    call Jubes_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_v "This is kinda boring. . .."
                                    $ JubesX.Statup("Love", 50, -3, 1)
                                    $ JubesX.Statup("Love", 80, -4, 1)
                                    $ JubesX.Statup("Obed", 30, -1, 1)
                                    $ JubesX.Statup("Obed", 50, -1, 1)
                                    $ JubesX.RecentActions.append("angry")
                                    $ JubesX.DailyActions.append("angry")
                                    jump Jubes_LA_After
        #End Count check

        call Escalation(JubesX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(JubesX,10) #"I could use a break soon. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(JubesX,5)   #". . . I could really use a break here. . ."

    #Round = 0 loop breaks
    $ JubesX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(JubesX,"done") # ch_s "Ok, that's it, I need a break."

label Jubes_LA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Jubes_Pos_Reset

    $ JubesX.FaceChange("sexy")

    $ JubesX.LickA += 1
    $ JubesX.Action -=1
    if JubesX.PantsNum() < 6 or JubesX.Upskirt:
        $ JubesX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ JubesX.Addictionrate += 1

    call Partner_Like(JubesX,2)

    if JubesX.LickA == 1:
            $ JubesX.SEXP += 15
            if not Situation:
                if JubesX.Love >= 500 and "unsatisfied" not in JubesX.RecentActions:
                    ch_v "That was. . . interesting."
                elif JubesX.Obed <= 500 and Player.Focus <= 20:
                    $ JubesX.FaceChange("perplexed", 1)
                    ch_v "Was that good for you?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_v "Oh? What did you have in mind?"
    call Checkout
    return

# end JubesX.Lick Ass /////////////////////////////////////////////////////////////////////////////
