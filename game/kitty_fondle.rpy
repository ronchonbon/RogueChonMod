# KittyX.Fondle /////////////////////////////////////////////////////////////////////////////
label Kitty_Fondle:

    $ KittyX.Mouth = "smile"
    if not KittyX.Action:
        ch_k "I'm kinda tired right now, [KittyX.Petname], later?"
        return
    menu:
        ch_k "Um, what did you want to touch, [KittyX.Petname]?"
        "Your breasts?" if KittyX.Action:
                jump Kitty_Fondle_Breasts
        "Your thighs?" if KittyX.Action:
                jump Kitty_Fondle_Thighs
        "Your pussy?" if KittyX.Action:
                jump Kitty_Fondle_Pussy
        "Your Ass?" if KittyX.Action:
                jump Kitty_Fondle_Ass
        "Never mind.":
                return
    return


# ////////////////////////////////////////////////////////////////////////Start Fondle Pussy
label Kitty_Fondle_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(KittyX)
                                                                                        # Will she let you fondle? Modifiers
    if KittyX.FondleP: #You've done it before
        $ temp_modifier += 20
    if KittyX.PantsNum() > 6 or KittyX.HoseNum() >= 5: # she's got pants on.
        $ temp_modifier -= 10
    if KittyX.Lust > 75: #She's really horny
        $ temp_modifier += 15
    if KittyX.Lust > 75 and Situation == "auto": #She's really horny
        $ temp_modifier += 10
    if "exhibitionist" in KittyX.Traits:
        $ temp_modifier += (2*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.Petnames:
        $ temp_modifier += 10
    elif "ex" in KittyX.Traits:
        $ temp_modifier -= 25
    if KittyX.ForcedCount and not KittyX.Forced:
        $ temp_modifier -= 5 * KittyX.ForcedCount

    if Taboo and "tabno" in KittyX.DailyActions:
        $ temp_modifier -= 10

    if "no fondle pussy" in KittyX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no fondle pussy" in KittyX.RecentActions else 0

    $ Approval = ApprovalCheck(KittyX, 1050, TabM = 2) # 105, 120, 135, Taboo -80(185)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ KittyX.FaceChange("sexy")
            $ KittyX.Statup("Obed", 90, 1)
            $ KittyX.Statup("Obed", 70, 2)
            $ KittyX.Statup("Inbt", 70, 3)
            $ KittyX.Statup("Inbt", 30, 2)
            "As your hand creeps up her thigh, [KittyX.Name] seems a bit surprised, but then nods."
            jump Kitty_FP_Prep
        else:
            $ KittyX.FaceChange("surprised")
            $ KittyX.Statup("Obed", 50, -2)
            ch_k "Nuh-uh, [KittyX.Petname], get back to what you were doing."
            $ temp_modifier = 0
            $ Trigger2 = 0
            return

    if Situation == "pullback":
        $ KittyX.FaceChange("surprised")
        $ KittyX.Brows = "sad"
        if KittyX.Lust > 80:
            $ KittyX.Statup("Love", 70, -4)
        $ KittyX.Statup("Obed", 90, 1)
        $ KittyX.Statup("Obed", 70, 2)
        "As your hand pulls out, [KittyX.Name] gasps and looks upset."
        jump Kitty_FP_Prep
    elif "fondle pussy" in KittyX.RecentActions:
        $ KittyX.FaceChange("sexy", 1)
        ch_k "Mmm, again? Ok."
        jump Kitty_FP_Prep
    elif "fondle pussy" in KittyX.DailyActions:
        $ KittyX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Take it easy though.",
            "Take it a bit gently, I'm still shaking from earlier.",
            "Mmm. . ."])
        ch_k "[Line]"

    if Approval >= 2:                                                                   #She's into it. . .
        $ KittyX.FaceChange("bemused", 1)
        if KittyX.Forced:
            $ KittyX.FaceChange("sad")
            $ KittyX.Statup("Love", 70, -3, 1)
            $ KittyX.Statup("Love", 20, -2, 1)
            $ KittyX.Statup("Obed", 90, 1)
            $ KittyX.Statup("Inbt", 60, 1)
        ch_k "Ok, whatever."
        $ KittyX.Statup("Love", 90, 1)
        $ KittyX.Statup("Inbt", 50, 3)
        jump Kitty_FP_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ KittyX.FaceChange("angry", 1)
        if "no fondle pussy" in KittyX.RecentActions:
            ch_k "I[KittyX.like]{i}just{/i} told you \"no!\""
        elif Taboo and "tabno" in KittyX.DailyActions and "no fondle pussy" in KittyX.DailyActions:
            ch_k "I told you not to touch me like that in public!"
        elif "no fondle pussy" in KittyX.DailyActions:
            ch_k "[KittyX.Like]take a lesson, [KittyX.Petname]."
        elif Taboo and "tabno" in KittyX.DailyActions:
            ch_k "Not here!"
        elif not KittyX.FondleP:
            $ KittyX.FaceChange("bemused")
            ch_k "Um, not down there, [KittyX.Petname]. . ."
        else:
            $ KittyX.FaceChange("bemused")
            ch_k "Um, no."
        menu:
            extend ""
            "Sorry, never mind." if "no fondle pussy" in KittyX.DailyActions:
                $ KittyX.FaceChange("bemused")
                ch_k "Yeah, ok, [KittyX.Petname]."
                return
            "Maybe later?" if "no fondle pussy" not in KittyX.DailyActions:
                $ KittyX.FaceChange("sexy")
                ch_k "I'll give it some thought, [KittyX.Petname]."
                $ KittyX.Statup("Love", 80, 2)
                $ KittyX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ KittyX.RecentActions.append("tabno")
                    $ KittyX.DailyActions.append("tabno")
                $ KittyX.RecentActions.append("no fondle pussy")
                $ KittyX.DailyActions.append("no fondle pussy")
                return
            "Come on, Please?":
                if Approval:
                    $ KittyX.FaceChange("sexy")
                    $ KittyX.Statup("Obed", 90, 2)
                    $ KittyX.Statup("Obed", 50, 2)
                    $ KittyX.Statup("Inbt", 70, 3)
                    $ KittyX.Statup("Inbt", 40, 2)
                    ch_k "I like it when you beg. . ."
                    jump Kitty_FP_Prep
                else:
                    $ KittyX.FaceChange("sexy")
                    ch_k "Nuh uh."

            "[[Start fondling anyway]":                                               # Pressured into fondling.
                $ Approval = ApprovalCheck(KittyX, 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                if Approval > 1 or (Approval and KittyX.Forced):
                    $ KittyX.FaceChange("sad")
                    $ KittyX.Statup("Love", 70, -5, 1)
                    $ KittyX.Statup("Love", 200, -2)
                    ch_k "Well. . . I guess. . ."
                    $ KittyX.Statup("Obed", 50, 4)
                    $ KittyX.Statup("Inbt", 80, 1)
                    $ KittyX.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ KittyX.Forced = 1
                    jump Kitty_FP_Prep
                else:
                    $ KittyX.Statup("Love", 200, -15)
                    $ KittyX.FaceChange("angry", 1)
                    "She slaps your hand away."
                    $ KittyX.RecentActions.append("angry")
                    $ KittyX.DailyActions.append("angry")

    if "no fondle pussy" in KittyX.DailyActions:
        ch_k "How many times do I have to say \"no?\""
        $ KittyX.RecentActions.append("angry")
        $ KittyX.DailyActions.append("angry")
    elif KittyX.Forced:
        $ KittyX.FaceChange("angry", 1)
        ch_k "Keep away from my kitty, [KittyX.Petname]."
        $ KittyX.Statup("Lust", 70, 5)
        $ KittyX.Statup("Obed", 50, -2)
        $ KittyX.RecentActions.append("angry")
        $ KittyX.DailyActions.append("angry")
    elif Taboo:
        $ KittyX.FaceChange("angry", 1)
        $ KittyX.RecentActions.append("tabno")
        $ KittyX.DailyActions.append("tabno")
        ch_k "Time and place, [KittyX.Petname]!"
    elif KittyX.FondleP:
        $ KittyX.FaceChange("sad")
        ch_k "Sorry, keep your hands out of there."
    else:
        $ KittyX.FaceChange("sexy")
        $ KittyX.Mouth = "sad"
        ch_k "No luck [KittyX.Petname]."
    $ KittyX.RecentActions.append("no fondle pussy")
    $ KittyX.DailyActions.append("no fondle pussy")
    $ temp_modifier = 0
    return

label Kitty_FP_Prep: #Animation set-up
    if Trigger2 == "fondle pussy":
        return

    call Kitty_Pussy_Launch("fondle pussy")

    if Situation == KittyX:
            #Kitty auto-starts
            $ Situation = 0
            if (KittyX.Legs and not KittyX.Upskirt) or (KittyX.Panties and not KittyX.PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck(KittyX, 1250, TabM = 1) or (KittyX.SeenPussy and ApprovalCheck(KittyX, 500) and not Taboo):
                        $ KittyX.Upskirt = 1
                        $ KittyX.PantiesDown = 1
                        $ Line = 0
                        if KittyX.PantsNum() == 5:
                            $ Line = KittyX.Name + " hikes up her skirt"
                        elif KittyX.PantsNum() >= 5:
                            $ Line = KittyX.Name + " pulls down her " + KittyX.Legs
                        else:
                            $ Line = 0
                        if KittyX.Panties:
                            if Line:
                                #wearing pants
                                "[Line] and pulls her [KittyX.Panties] out of the way."
                                "She then grabs your arm and then presses your hand against her crotch, clearly intending you to get to work."
                            else:
                                #no pants
                                "She pulls her [KittyX.Panties] out of the way, and then presses your hand against her crotch."
                                "She clearly intends for you to get to work."
                        else:
                            #pants but no panties
                            "[Line], and then presses your hand against her crotch."
                            "She clearly intends for you to get to work."
                        call Kitty_First_Bottomless(1)
                else:
                        "[KittyX.Name] grabs your arm and presses your hand against her crotch, clearly intending you to get to work."
            else:
                        "[KittyX.Name] grabs your arm and presses your hand against her crotch, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":
                    $ KittyX.Statup("Inbt", 80, 3)
                    $ KittyX.Statup("Inbt", 50, 2)
                    "You start to run your fingers along her pussy."
                "Praise her.":
                    $ KittyX.FaceChange("sexy", 1)
                    $ KittyX.Statup("Inbt", 80, 3)
                    ch_p "I like the initiative, [KittyX.Pet]."
                    $ KittyX.NameCheck() #checks reaction to petname
                    "You start to run your fingers along her pussy."
                    $ KittyX.Statup("Love", 85, 1)
                    $ KittyX.Statup("Obed", 90, 1)
                    $ KittyX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your hand back."
                    $ KittyX.FaceChange("surprised")
                    $ KittyX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that right now, [KittyX.Pet]."
                    $ KittyX.NameCheck() #checks reaction to petname
                    "[KittyX.Name] pulls back."
                    $ KittyX.Statup("Obed", 90, 1)
                    $ KittyX.Statup("Obed", 50, 1)
                    $ KittyX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ KittyX.AddWord(1,"refused","refused")
                    return
            #end auto

    if not KittyX.Forced and Situation != "auto":
        $ temp_modifier = 0
        call Bottoms_Off(KittyX)
        if "angry" in KittyX.RecentActions:
            return
    $ temp_modifier = 0
    if not KittyX.FondleP:
        if KittyX.Forced:
            $ KittyX.Statup("Love", 90, -50)
            $ KittyX.Statup("Obed", 70, 35)
            $ KittyX.Statup("Inbt", 80, 25)
        else:
            $ KittyX.Statup("Love", 90, 10)
            $ KittyX.Statup("Obed", 70, 10)
            $ KittyX.Statup("Inbt", 80, 15)
    if Taboo:
        $ KittyX.Inbt += int(Taboo/10)
        $ KittyX.Lust += int(Taboo/5)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ KittyX.DrainWord("tabno")
    $ KittyX.DrainWord("no fondle pussy")
    $ KittyX.RecentActions.append("fondle pussy")
    $ KittyX.DailyActions.append("fondle pussy")

    $ Speed = 1
    call Kitty_Pussy_Launch("fondle pussy")

label Kitty_FP_Cycle: #Repeating strokes
    while Round > 0:
        call ViewShift(KittyX,KittyX.Pose,0,"fondle pussy")
        call Shift_Focus(KittyX)
        $ KittyX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "I want to stick a finger in. . ." if Speed != 2:
                                if KittyX.InsertP:
                                    $ Speed = 2
                                else:
                                    menu:
                                        "Ask her first":
                                            $ Situation = "shift"
                                        "Don't ask first [[just stick it in]":
                                            $ Situation = "auto"
                                    call Kitty_Insert_Pussy

                        "Pull back a bit. . ." if Speed == 2:
                                    $ Speed = 0

                        "Slap her ass":
                                    call Slap_Ass(KittyX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Kitty_FP_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0
                        "View":
                                    call ViewShift(KittyX,"menu")
                                    jump Kitty_FP_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if KittyX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ KittyX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")

                                    "Shift primary action":
                                            if KittyX.Action and MultiAction:
                                                    menu:
                                                        "I want to lick your pussy.":
                                                                $ Situation = "shift"
                                                                call Kitty_FP_After
                                                                call Kitty_Lick_Pussy
                                                        "Just start licking":
                                                                $ Situation = "auto"
                                                                call Kitty_FP_After
                                                                call Kitty_Lick_Pussy
                                                        "Pull back to the thighs":
                                                                $ Situation = "pullback"
                                                                call Kitty_FP_After
                                                                call Kitty_Fondle_Thighs
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Kitty_FP_After
                                                                call Kitty_Dildo_Pussy
                                                        "Never Mind":
                                                                jump Kitty_FP_Cycle
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Kitty_FP_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [KittyX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(KittyX)
                                            "Ask [KittyX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(KittyX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(KittyX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Kitty_FP_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Kitty_FP_Cycle
                                            "Never mind":
                                                        jump Kitty_FP_Cycle

                                    "Show her feet" if not ShowFeet and (KittyX.Pose == "doggy" or KittyX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (KittyX.Pose == "doggy" or KittyX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [KittyX.Name]":
                                            call Girl_Undress(KittyX)
                                    "Clean up [KittyX.Name] (locked)" if not KittyX.Spunk:
                                            pass
                                    "Clean up [KittyX.Name]" if KittyX.Spunk:
                                            call Girl_Cleanup(KittyX,"ask")
                                    "Never mind":
                                            jump Kitty_FP_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Kitty_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Kitty_FP_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Kitty_Pos_Reset
                                    $ Line = 0
                                    jump Kitty_FP_After
        #End menu (if Line)

        call Shift_Focus(KittyX)
        call Sex_Dialog(KittyX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or KittyX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(KittyX)
                            if "angry" in KittyX.RecentActions:
                                call Kitty_Pos_Reset
                                return
                            $ KittyX.Statup("Lust", 200, 5)
                            if 100 > KittyX.Lust >= 70 and KittyX.OCount < 2:
                                $ KittyX.RecentActions.append("unsatisfied")
                                $ KittyX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Kitty_FP_After
                            $ Line = "came"

                    if KittyX.Lust >= 100:
                            #If Kitty can cum
                            call Girl_Cumming(KittyX)
                            if Situation == "shift" or "angry" in KittyX.RecentActions:
                                jump Kitty_FP_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in KittyX.RecentActions:#And Kitty is unsatisfied,
                                "[KittyX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Kitty_FP_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if KittyX.SEXP >= 100 or ApprovalCheck(KittyX, 1200, "LO"):
            pass
        elif Cnt == (5 + KittyX.FondleP):
                    $ KittyX.Brows = "confused"
                    ch_k "You like how that feels, huh?"
        elif KittyX.Lust >= 80:
                    pass
        elif Cnt == (15 + KittyX.FondleP) and KittyX.SEXP >= 15 and not ApprovalCheck(KittyX, 1500):
                    $ KittyX.Brows = "confused"
                    menu:
                        ch_k "You look like you're having fun there, but maybe we could[KittyX.like]try something else?"
                        "Finish up.":
                                "You let go. . ."
                                jump Kitty_FP_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Kitty_FP_After
                        "No, this is fun.":
                                if ApprovalCheck(KittyX, 1200) or ApprovalCheck(KittyX, 500, "O"):
                                    $ KittyX.Statup("Love", 200, -5)
                                    $ KittyX.Statup("Obed", 50, 3)
                                    $ KittyX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ KittyX.FaceChange("angry", 1)
                                    call Kitty_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_k "Fun for you maybe, I'm tired of it."
                                    $ KittyX.Statup("Love", 50, -3, 1)
                                    $ KittyX.Statup("Love", 80, -4, 1)
                                    $ KittyX.Statup("Obed", 30, -1, 1)
                                    $ KittyX.Statup("Obed", 50, -1, 1)
                                    $ KittyX.RecentActions.append("angry")
                                    $ KittyX.DailyActions.append("angry")
                                    jump Kitty_FP_After
        #End Count check

        call Escalation(KittyX) #sees if she wants to escalate things

        if Round == 10:
            ch_k "It's[KittyX.like]getting kinda late."
        elif Round == 5:
            ch_k "We should wrap this up."

    #Round = 0 loop breaks
    $ KittyX.FaceChange("bemused", 0)
    $ Line = 0
    ch_k "Time to take a little break, for now."

label Kitty_FP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Kitty_Pos_Reset

    $ KittyX.FaceChange("sexy")

    $ KittyX.FondleP += 1
    $ KittyX.Action -=1
    if KittyX.PantsNum() < 6 or KittyX.Upskirt:
        $ KittyX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ KittyX.Addictionrate += 1

    call Partner_Like(KittyX,2)

    if KittyX.FondleP == 1:
            $ KittyX.SEXP += 7
            if not Situation:
                if KittyX.Love >= 500 and "unsatisfied" not in KittyX.RecentActions:
                    ch_k "Your hand is. . . bigger than mine."
                elif KittyX.Obed <= 500 and Player.Focus <= 20:
                    $ KittyX.FaceChange("perplexed", 1)
                    ch_k "Did you get what you needed?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_k "Ok, what else did you want to do?"
    call Checkout
    return

# end KittyX.Fondle Pussy /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy
label Kitty_Insert_Pussy:
    call Shift_Focus(KittyX)
    if Situation == "auto":                                                                  #You auto-start
        if ApprovalCheck(KittyX, 1100, TabM = 2):
            $ KittyX.FaceChange("surprised")
            $ KittyX.Statup("Obed", 90, 1)
            $ KittyX.Statup("Obed", 70, 2)
            $ KittyX.Statup("Inbt", 70, 3)
            $ KittyX.Statup("Inbt", 30, 2)
            "As you slide a finger in, [KittyX.Name] seems a bit surprised, but seems into it."
            jump Kitty_IP_Prep
        else:
            $ KittyX.FaceChange("surprised",2)
            $ KittyX.Statup("Love", 80, -2)
            $ KittyX.Statup("Obed", 50, -3)
            ch_k "Oooh!"
            "She slaps your hand back."
            $ KittyX.FaceChange("perplexed",1)
            ch_k "Um, no take that out."
            return

    if ApprovalCheck(KittyX, 1100, TabM = 2):                                                                   #She's into it. . .
        if KittyX.Forced:
            $ KittyX.FaceChange("sad")
            $ KittyX.Statup("Love", 70, -3, 1)
            $ KittyX.Statup("Love", 20, -2, 1)
            $ KittyX.Statup("Obed", 90, 1)
            $ KittyX.Statup("Inbt", 60, 1)
            ch_k "Ok, whatever."
        else:
            $ KittyX.FaceChange("sexy", 1)
            $ KittyX.Statup("Love", 90, 1)
            $ KittyX.Statup("Inbt", 50, 3)
            ch_k "Mmmmmm."
        $ KittyX.Statup("Obed", 20, 1)
        $ KittyX.Statup("Obed", 60, 1)
        $ KittyX.Statup("Inbt", 70, 2)
        jump Kitty_IP_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ KittyX.FaceChange("bemused", 2)
        ch_k "Um, no thanks, [KittyX.Petname]."
        $ KittyX.Blush = 1
    return


label Kitty_IP_Prep: #Animation set-up
    if not KittyX.InsertP:
        $ KittyX.InsertP = 1
        $ KittyX.SEXP += 10
        if KittyX.Forced:
            $ KittyX.Statup("Love", 90, -60)
            $ KittyX.Statup("Obed", 70, 55)
            $ KittyX.Statup("Inbt", 80, 35)
        else:
            $ KittyX.Statup("Love", 90, 10)
            $ KittyX.Statup("Obed", 70, 20)
            $ KittyX.Statup("Inbt", 80, 25)

    if not KittyX.Forced and Situation != "auto":
        call Girl_Undress(KittyX,"bottom")
        if "angry" in KittyX.RecentActions:
            return

#    call Kitty_Pussy_Launch("insert pussy")
    if Taboo:
        $ KittyX.Inbt += int(Taboo/10)
        $ KittyX.Lust += int(Taboo/5)

    $ Line = 0
    $ Speed = 2
    return

# end KittyX.Insert Pussy /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Pussy
label Kitty_Lick_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(KittyX)
                                                                                  # Will she let you fondle? Modifiers
    if KittyX.LickP: #You've done it before
        $ temp_modifier += 15
    if KittyX.PantsNum() > 6 or KittyX.HoseNum() >= 5: # she's got pants on.
        $ temp_modifier -= 15
    if KittyX.Lust > 95:
        $ temp_modifier += 20
    elif KittyX.Lust > 85: #She's really horny
        $ temp_modifier += 15
    if Situation == "shift":
        $ temp_modifier += 10
    if KittyX.Lust > 85 and Situation == "auto": #She's really horny
        $ temp_modifier += 10
    if "exhibitionist" in KittyX.Traits:
        $ temp_modifier += (4*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.Petnames:
        $ temp_modifier += 10
    elif "ex" in KittyX.Traits:
        $ temp_modifier -= 25
    if KittyX.ForcedCount and not KittyX.Forced:
        $ temp_modifier -= 5 * KittyX.ForcedCount

    if Taboo and "tabno" in KittyX.DailyActions:
        $ temp_modifier -= 10

    if "no lick pussy" in KittyX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no lick pussy" in KittyX.RecentActions else 0

    $ Approval = ApprovalCheck(KittyX, 1250, TabM = 4) # 125, 140, 155, Taboo -160(285)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ KittyX.FaceChange("surprised")
            $ KittyX.Statup("Obed", 90, 1)
            $ KittyX.Statup("Obed", 70, 2)
            $ KittyX.Statup("Inbt", 70, 3)
            $ KittyX.Statup("Inbt", 30, 2)
            "As you crouch down and start to lick her pussy, [KittyX.Name] jumps, but then softens."
            $ KittyX.FaceChange("sexy")
            jump Kitty_LP_Prep
        else:
            $ KittyX.FaceChange("surprised")
            $ KittyX.Statup("Love", 80, -2)
            $ KittyX.Statup("Obed", 50, -3)
            ch_k "Oooo! Um, no, no thanks. No. . ."
            $ KittyX.FaceChange("perplexed",1)
            "She pushes your head back away from her."
            $ temp_modifier = 0
            $ Trigger2 = 0
            return

    if "lick pussy" in KittyX.RecentActions:
        $ KittyX.FaceChange("sexy", 1)
        ch_k "Mmm, again? Ok."
        jump Kitty_LP_Prep
    elif "lick pussy" in KittyX.DailyActions:
        $ KittyX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Huh? Again?",
            "I must have done something right.",
            "What a girl wants. . .",
            "Mmm. . ."])
        ch_k "[Line]"

    if Approval >= 2:                                                                   #She's into it. . .
        if KittyX.Forced:
            $ KittyX.FaceChange("sad")
            $ KittyX.Statup("Love", 70, -3, 1)
            $ KittyX.Statup("Love", 20, -2, 1)
            $ KittyX.Statup("Obed", 90, 1)
            $ KittyX.Statup("Inbt", 60, 1)
            ch_k "Ok, whatever."
        else:
            $ KittyX.FaceChange("sexy", 1)
            $ KittyX.Eyes = "closed"
            $ KittyX.Statup("Love", 90, 1)
            $ KittyX.Statup("Inbt", 50, 3)
            $ KittyX.Statup("Lust", 200, 3)
            ch_k "Oooooooh. . ."
        $ KittyX.Statup("Obed", 20, 1)
        $ KittyX.Statup("Obed", 60, 1)
        $ KittyX.Statup("Inbt", 70, 2)
        jump Kitty_LP_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ KittyX.FaceChange("angry", 1)
        if "no lick pussy" in KittyX.RecentActions:
            ch_k "I[KittyX.like]{i}just{/i} told you \"no!\""
        elif Taboo and "tabno" in KittyX.DailyActions and "no lick pussy" in KittyX.DailyActions:
            ch_k "You already got your answer!"
        elif "no lick pussy" in KittyX.DailyActions:
            ch_k "[KittyX.Like]take a lesson, [KittyX.Petname]."
        elif Taboo and "tabno" in KittyX.DailyActions:
            ch_k "Not here!"
        elif not KittyX.LickP:
            $ KittyX.FaceChange("bemused")
            ch_k "That's pretty intimate, [KittyX.Petname]. . ."
        else:
            $ KittyX.FaceChange("bemused")
            ch_k "Oh, um, no, I'm not really comfortable with that. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no lick pussy" in KittyX.DailyActions:
                $ KittyX.FaceChange("bemused")
                ch_k "Yeah, ok, [KittyX.Petname]."
                return
            "I'm sure I can convince you later. . ." if "no lick pussy" not in KittyX.DailyActions:
                $ KittyX.FaceChange("sexy")
                ch_k "I'll be thinking about it, [KittyX.Petname]."
                $ KittyX.Statup("Love", 80, 2)
                $ KittyX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ KittyX.RecentActions.append("tabno")
                    $ KittyX.DailyActions.append("tabno")
                $ KittyX.RecentActions.append("no lick pussy")
                $ KittyX.DailyActions.append("no lick pussy")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ KittyX.FaceChange("sexy")
                    $ KittyX.Statup("Obed", 90, 2)
                    $ KittyX.Statup("Obed", 50, 2)
                    ch_k "Oh. . . you're probably right. . ."
                    $ KittyX.Statup("Inbt", 70, 3)
                    $ KittyX.Statup("Inbt", 40, 2)
                    jump Kitty_LP_Prep
                else:
                    $ KittyX.FaceChange("sexy")
                    ch_k "Um, not this time, [KittyX.Petname], that's too. . ."

            "[[Get in there anyway]":                                               # Pressured into being licked.
                $ Approval = ApprovalCheck(KittyX, 750, "OI", TabM = 4) # 75, 90, 105, -160(235)
                if Approval > 1 or (Approval and KittyX.Forced):
                    $ KittyX.FaceChange("sad")
                    $ KittyX.Statup("Love", 70, -5, 1)
                    $ KittyX.Statup("Love", 200, -2)
                    ch_k "Ok, get in there if you're so determined."
                    $ KittyX.Statup("Obed", 50, 4)
                    $ KittyX.Statup("Inbt", 80, 1)
                    $ KittyX.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ KittyX.Forced = 1
                    jump Kitty_LP_Prep
                else:
                    $ KittyX.Statup("Love", 200, -15)
                    $ KittyX.FaceChange("angry", 1)
                    "She shoves your head back."
                    $ KittyX.RecentActions.append("angry")
                    $ KittyX.DailyActions.append("angry")

    if "no lick pussy" in KittyX.DailyActions:
        ch_k "How many times do I have to say \"no?\""
        $ KittyX.RecentActions.append("angry")
        $ KittyX.DailyActions.append("angry")
    elif KittyX.Forced:
        $ KittyX.FaceChange("angry", 1)
        ch_k "Not even, [KittyX.Petname]."
        $ KittyX.Statup("Lust", 80, 5)
        $ KittyX.Statup("Obed", 50, -2)
        $ KittyX.RecentActions.append("angry")
        $ KittyX.DailyActions.append("angry")
    elif Taboo:
        $ KittyX.FaceChange("angry", 1)
        $ KittyX.RecentActions.append("tabno")
        $ KittyX.DailyActions.append("tabno")
        ch_k "This just really isn't the time or place, [KittyX.Petname]!"
    elif KittyX.LickP:
        $ KittyX.FaceChange("sad")
        ch_k "Keep your head out of there."
    else:
        $ KittyX.FaceChange("surprised")
        ch_k "Ugh!"
        $ KittyX.FaceChange()
    $ KittyX.RecentActions.append("no lick pussy")
    $ KittyX.DailyActions.append("no lick pussy")
    $ temp_modifier = 0
    return

label Kitty_LP_Prep: #Animation set-up
    if Trigger2 == "lick pussy": #fix pull down pants now an option, make it work
        return

    call Kitty_Pussy_Launch("lick pussy")

    if Situation == KittyX:
            #Kitty auto-starts
            $ Situation = 0
            if (KittyX.Legs and not KittyX.Upskirt) or (KittyX.Panties and not KittyX.PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck(KittyX, 1250, TabM = 1) or (KittyX.SeenPussy and ApprovalCheck(KittyX, 500) and not Taboo):
                        $ KittyX.Upskirt = 1
                        $ KittyX.PantiesDown = 1
                        $ Line = 0
                        if KittyX.PantsNum() == 5:
                            $ Line = KittyX.Name + " hikes up her skirt"
                        elif KittyX.PantsNum() >= 5:
                            $ Line = KittyX.Name + " pulls down her " + KittyX.Legs
                        else:
                            $ Line = 0
                        if KittyX.Panties:
                            if Line:
                                #wearing pants
                                "[Line] and pulls her [KittyX.Panties] out of the way."
                                "She then grabs your head and pulls it to her crotch, clearly intending you to get to work."
                            else:
                                #no pants
                                "She pulls her [KittyX.Panties] out of the way, and then shoves your face into her crotch."
                                "She clearly intends for you to get to work."
                        else:
                                #pants but no panties
                                "[Line], and then shoves your face into her crotch."
                                "She clearly intends for you to get to work."
                        call Kitty_First_Bottomless(1)
                else:
                        "[KittyX.Name] grabs your head and pulls it to her crotch, clearly intending you to get to work."
            else:
                        "[KittyX.Name] grabs your head and pulls it to her crotch, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":
                    $ KittyX.Statup("Inbt", 80, 3)
                    $ KittyX.Statup("Inbt", 50, 2)
                    "You start licking."
                "Praise her.":
                    $ KittyX.FaceChange("sexy", 1)
                    $ KittyX.Statup("Inbt", 80, 3)
                    ch_p "Mmm, I like this idea, [KittyX.Pet]."
                    $ KittyX.NameCheck() #checks reaction to petname
                    "You start licking."
                    $ KittyX.Statup("Love", 85, 1)
                    $ KittyX.Statup("Obed", 90, 1)
                    $ KittyX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your head away."
                    $ KittyX.FaceChange("surprised")
                    $ KittyX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that right now, [KittyX.Pet]."
                    $ KittyX.NameCheck() #checks reaction to petname
                    "[KittyX.Name] pulls back."
                    $ KittyX.Statup("Obed", 90, 1)
                    $ KittyX.Statup("Obed", 50, 1)
                    $ KittyX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ KittyX.AddWord(1,"refused","refused")
                    return
            #end auto

    if not KittyX.Forced and Situation != "auto":
        $ temp_modifier = 0
        if KittyX.PantsNum() > 6:
            $ temp_modifier = 15
        call Bottoms_Off(KittyX)
        if "angry" in KittyX.RecentActions:
            return

    $ temp_modifier = 0
    if not KittyX.LickP:
        if KittyX.Forced:
            $ KittyX.Statup("Love", 90, -30)
            $ KittyX.Statup("Obed", 70, 35)
            $ KittyX.Statup("Inbt", 80, 75)
        else:
            $ KittyX.Statup("Love", 90, 35)
            $ KittyX.Statup("Obed", 70, 15)
            $ KittyX.Statup("Inbt", 80, 35)
    if Taboo:
        $ KittyX.Inbt += int(Taboo/10)
        $ KittyX.Lust += int(Taboo/5)
    if Situation:
        $ renpy.pop_call()
        $ Situation = 0

    if KittyX.PantsNum() == 5:
        $ KittyX.Upskirt = 1
        $ KittyX.SeenPanties = 1
    if not KittyX.Panties:
        call Kitty_First_Bottomless(1)

    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ KittyX.DrainWord("tabno")
    $ KittyX.DrainWord("no lick pussy")
    $ KittyX.RecentActions.append("lick pussy")
    $ KittyX.DailyActions.append("lick pussy")
    call Kitty_Pussy_Launch("lick pussy")

label Kitty_LP_Cycle: #Repeating strokes
    if Trigger2 == "kiss you":
            $ Trigger2 = 0
    while Round > 0:
        call ViewShift(KittyX,KittyX.Pose,0,"lick pussy")
        call Shift_Focus(KittyX)
        $ KittyX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(KittyX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Kitty_LP_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0
                        "View":
                                    call ViewShift(KittyX,"menu")
                                    jump Kitty_LP_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if KittyX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ KittyX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")

                                    "Shift primary action":
                                            if KittyX.Action and MultiAction:
                                                    menu:
                                                        "Pull out and start rubbing again.":
                                                                if KittyX.Action and MultiAction:
                                                                    $ Situation = "pullback"
                                                                    call Kitty_LP_After
                                                                    call Kitty_Fondle_Pussy
                                                                else:
                                                                    call Sex_Basic_Dialog(KittyX,"tired")
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Kitty_LP_After
                                                                call Kitty_Dildo_Pussy
                                                        "Never Mind":
                                                                jump Kitty_LP_Cycle
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Kitty_LP_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [KittyX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(KittyX)
                                            "Ask [KittyX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(KittyX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(KittyX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Kitty_LP_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Kitty_LP_Cycle
                                            "Never mind":
                                                        jump Kitty_LP_Cycle

                                    "Show her feet" if not ShowFeet and (KittyX.Pose == "doggy" or KittyX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (KittyX.Pose == "doggy" or KittyX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [KittyX.Name]":
                                            call Girl_Undress(KittyX)
                                    "Clean up [KittyX.Name] (locked)" if not KittyX.Spunk:
                                            pass
                                    "Clean up [KittyX.Name]" if KittyX.Spunk:
                                            call Girl_Cleanup(KittyX,"ask")
                                    "Never mind":
                                            jump Kitty_LP_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Kitty_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Kitty_LP_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Kitty_Pos_Reset
                                    $ Line = 0
                                    jump Kitty_LP_After
        #End menu (if Line)

        if KittyX.Panties or KittyX.PantsNum() > 6 or KittyX.HoseNum() >= 5: #This checks if Kitty wants to strip down.
                call Girl_Undress(KittyX,"auto")

        call Shift_Focus(KittyX)
        call Sex_Dialog(KittyX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or KittyX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(KittyX)
                            if "angry" in KittyX.RecentActions:
                                call Kitty_Pos_Reset
                                return
                            $ KittyX.Statup("Lust", 200, 5)
                            if 100 > KittyX.Lust >= 70 and KittyX.OCount < 2:
                                $ KittyX.RecentActions.append("unsatisfied")
                                $ KittyX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Kitty_LP_After
                            $ Line = "came"

                    if KittyX.Lust >= 100:
                            #If Kitty can cum
                            call Girl_Cumming(KittyX)
                            if Situation == "shift" or "angry" in KittyX.RecentActions:
                                jump Kitty_LP_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in KittyX.RecentActions:#And Kitty is unsatisfied,
                                "[KittyX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Kitty_LP_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if KittyX.SEXP >= 100 or ApprovalCheck(KittyX, 1200, "LO"):
            pass
        elif Cnt == (5 + KittyX.LickP):
                    $ KittyX.Brows = "confused"
                    ch_k "You like it down there?"
        elif KittyX.Lust >= 80:
                    pass
        elif Cnt == (15 + KittyX.LickP) and KittyX.SEXP >= 15 and not ApprovalCheck(KittyX, 1500):
                    $ KittyX.Brows = "confused"
                    menu:
                        ch_k "[KittyX.Petname], I know you're having fun down there, but maybe we could try something else."
                        "Finish up.":
                                "You let go. . ."
                                jump Kitty_LP_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Kitty_LP_After
                        "No, this is fun.":
                                if ApprovalCheck(KittyX, 1200) or ApprovalCheck(KittyX, 500, "O"):
                                    $ KittyX.Statup("Love", 200, -5)
                                    $ KittyX.Statup("Obed", 50, 3)
                                    $ KittyX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ KittyX.FaceChange("angry", 1)
                                    call Kitty_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_k "Fun for you maybe, I'm tired of it."
                                    $ KittyX.Statup("Love", 50, -3, 1)
                                    $ KittyX.Statup("Love", 80, -4, 1)
                                    $ KittyX.Statup("Obed", 30, -1, 1)
                                    $ KittyX.Statup("Obed", 50, -1, 1)
                                    $ KittyX.RecentActions.append("angry")
                                    $ KittyX.DailyActions.append("angry")
                                    jump Kitty_LP_After
        #End Count check

        call Escalation(KittyX) #sees if she wants to escalate things

        if Round == 10:
            ch_k "It's[KittyX.like]getting kinda late."
        elif Round == 5:
            ch_k "We should wrap this up."

    #Round = 0 loop breaks
    $ KittyX.FaceChange("bemused", 0)
    $ Line = 0
    ch_k "Time to take a little break, for now."

label Kitty_LP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Kitty_Pos_Reset

    $ KittyX.FaceChange("sexy")

    $ KittyX.LickP += 1
    $ KittyX.Action -=1
    if KittyX.PantsNum() < 6 or KittyX.Upskirt:
        $ KittyX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ KittyX.Addictionrate += 1

    call Partner_Like(KittyX,3,2)

    if KittyX.LickP == 1:
            $ KittyX.SEXP += 10
            if not Situation:
                if KittyX.Love >= 500 and "unsatisfied" not in KittyX.RecentActions:
                    ch_k "Was it. . . good?"
                elif KittyX.Obed <= 500 and Player.Focus <= 20:
                    $ KittyX.FaceChange("perplexed", 1)
                    ch_k "Well, did you like the taste?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_k "Ok, what else did you want to do?"
    call Checkout
    return


# end KittyX.Lick Pussy /////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////Start Fondle Ass
label Kitty_Fondle_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(KittyX)
                                                                                     # Will she let you fondle? Modifiers
    if KittyX.FondleA: #You've done it before
        $ temp_modifier += 10
    if KittyX.PantsNum() > 6 or KittyX.HoseNum() >= 5: # she's got pants on.
        $ temp_modifier -= 5
    if KittyX.Lust > 75: #She's really horny
        $ temp_modifier += 15
    if "exhibitionist" in KittyX.Traits:
        $ temp_modifier += Taboo
    if KittyX in Player.Harem or "sex friend" in KittyX.Petnames:
        $ temp_modifier += 10
    elif "ex" in KittyX.Traits:
        $ temp_modifier -= 25
    if KittyX.ForcedCount and not KittyX.Forced:
        $ temp_modifier -= 5 * KittyX.ForcedCount

    if Taboo and "tabno" in KittyX.DailyActions:
        $ temp_modifier -= 10

    if "no fondle ass" in KittyX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no fondle ass" in KittyX.RecentActions else 0

    $ Approval = ApprovalCheck(KittyX, 850, TabM=1) # 85, 100, 115, Taboo -40(125)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ KittyX.FaceChange("surprised", 1)
            $ KittyX.Statup("Obed", 70, 2)
            $ KittyX.Statup("Inbt", 40, 2)
            "As your hand creeps down her backside, [KittyX.Name] jumps a bit, and then relaxes."
            $ KittyX.FaceChange("sexy")
            jump Kitty_FA_Prep
        else:
            $ KittyX.FaceChange("surprised")
            $ KittyX.Statup("Obed", 50, -3)
            ch_k "Hands off, [KittyX.Petname]."
            $ KittyX.FaceChange("bemused")
            $ temp_modifier = 0
            $ Trigger2 = 0
            return

    if Situation == "pullback":
        $ KittyX.FaceChange("surprised")
        $ KittyX.Brows = "sad"
        if KittyX.Lust > 80:
            $ KittyX.Statup("Love", 70, -4)
        $ KittyX.Statup("Obed", 90, 1)
        $ KittyX.Statup("Obed", 70, 2)
        "As your finger slides out, [KittyX.Name] gasps and looks upset."
        jump Kitty_FA_Prep
    elif "fondle ass" in KittyX.RecentActions:
        $ KittyX.FaceChange("sexy", 1)
        ch_k "Mmm, again? Ok."
        jump Kitty_FA_Prep
    elif "fondle ass" in KittyX.DailyActions:
        $ KittyX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Maybe not so rough this time though.",
            "Mmm. . ."])
        ch_k "[Line]"

    if Approval >= 2:                                                                   #She's into it. . .
        if KittyX.Forced:
            $ KittyX.FaceChange("sad")
            $ KittyX.Statup("Love", 70, -2, 1)
            $ KittyX.Statup("Obed", 90, 2)
            $ KittyX.Statup("Inbt", 60, 2)
            ch_k "Ok, geeze."
        else:
            $ KittyX.FaceChange("bemused, 1")
            ch_k "Ok, go for it."
        $ KittyX.Statup("Lust", 200, 3)
        $ KittyX.Statup("Obed", 60, 1)
        $ KittyX.Statup("Inbt", 70, 1)
        jump Kitty_FA_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ KittyX.FaceChange("angry", 1)
        if "no fondle ass" in KittyX.RecentActions:
            ch_k "I[KittyX.like]{i}just{/i} told you \"no!\""
        elif Taboo and "tabno" in KittyX.DailyActions and "no fondle ass" in KittyX.DailyActions:
            ch_k "I told you not to touch me like that in public!"
        elif "no fondle ass" in KittyX.DailyActions:
            ch_k "[KittyX.Like]take a lesson, [KittyX.Petname]."
        elif Taboo and "tabno" in KittyX.DailyActions:
            ch_k "Not here!"
        elif not KittyX.FondleA:
            $ KittyX.FaceChange("bemused")
            ch_k "Not yet, [KittyX.Petname]. . ."
        else:
            $ KittyX.FaceChange("bemused")
            ch_k "Let's not, ok [KittyX.Petname]?"
        menu:
            extend ""
            "Sorry, never mind." if "no fondle ass" in KittyX.DailyActions:
                $ KittyX.FaceChange("bemused")
                ch_k "Yeah, ok, [KittyX.Petname]."
                return
            "Maybe later?" if "no fondle ass" not in KittyX.DailyActions:
                $ KittyX.FaceChange("sexy")
                ch_k "Heh, maybe, [KittyX.Petname]."
                $ KittyX.Statup("Love", 80, 2)
                $ KittyX.Statup("Inbt", 50, 2)
                if Taboo:
                    $ KittyX.RecentActions.append("tabno")
                    $ KittyX.DailyActions.append("tabno")
                $ KittyX.RecentActions.append("no fondle ass")
                $ KittyX.DailyActions.append("no fondle ass")
                return
            "Just one good squeeze?":
                if Approval:
                    $ KittyX.FaceChange("sexy")
                    $ KittyX.Statup("Obed", 90, 1)
                    $ KittyX.Statup("Obed", 50, 2)
                    ch_k "I like it when you beg. . ."
                    $ KittyX.Statup("Inbt", 70, 1)
                    $ KittyX.Statup("Inbt", 40, 2)
                    jump Kitty_FA_Prep
                else:
                    $ KittyX.FaceChange("sexy")
                    ch_k "Nuh uh."

            "[[Start fondling anyway]":                                               # Pressured into fondling.
                $ Approval = ApprovalCheck(KittyX, 250, "OI", TabM = 3) # 25, 40, 55, -120(145)
                if Approval > 1 or (Approval and KittyX.Forced):
                    $ KittyX.FaceChange("sad")
                    $ KittyX.Statup("Love", 70, -3, 1)
                    $ KittyX.Statup("Love", 200, -1)
                    ch_k "Fine, I suppose."
                    $ KittyX.Statup("Obed", 50, 3)
                    $ KittyX.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ KittyX.Forced = 1
                    jump Kitty_FA_Prep
                else:
                    $ KittyX.Statup("Love", 200, -10)
                    $ KittyX.FaceChange("angry", 1)
                    "She slaps your hand away."
                    $ KittyX.RecentActions.append("angry")
                    $ KittyX.DailyActions.append("angry")

    if "no fondle ass" in KittyX.DailyActions:
        ch_k "How many times do I have to say \"no?\""
        $ KittyX.RecentActions.append("angry")
        $ KittyX.DailyActions.append("angry")
    elif KittyX.Forced:
        $ KittyX.FaceChange("angry", 1)
        ch_k "Back off!"
        $ KittyX.Statup("Lust", 60, 5)
        $ KittyX.Statup("Obed", 50, -2)
        $ KittyX.RecentActions.append("angry")
        $ KittyX.DailyActions.append("angry")
    elif Taboo:
        $ KittyX.FaceChange("angry", 1)
        $ KittyX.RecentActions.append("tabno")
        $ KittyX.DailyActions.append("tabno")
        ch_k "[KittyX.Petname]! Not here!"
    elif KittyX.FondleA:
        $ KittyX.FaceChange("sad")
        ch_k "Sorry, hands to yourself."
    else:
        $ KittyX.FaceChange("sexy")
        $ KittyX.Mouth = "sad"
        ch_k "Scram, [KittyX.Petname]."
    $ KittyX.RecentActions.append("no fondle ass")
    $ KittyX.DailyActions.append("no fondle ass")
    $ temp_modifier = 0
    return

ch_k "Sorry, I don't even know how I got here. . ."
return

label Kitty_FA_Prep: #Animation set-up
    if Trigger2 == "fondle ass":
        return
    if not KittyX.Forced and Situation != "auto":
        $ temp_modifier = 0
        call Bottoms_Off(KittyX)
        if "angry" in KittyX.RecentActions:
            return
    $ temp_modifier = 0
    call Kitty_Pussy_Launch("fondle ass")
    if not KittyX.FondleA:
        if KittyX.Forced:
            $ KittyX.Statup("Love", 90, -20)
            $ KittyX.Statup("Obed", 70, 20)
            $ KittyX.Statup("Inbt", 80, 15)
        else:
            $ KittyX.Statup("Love", 90, 10)
            $ KittyX.Statup("Obed", 70, 12)
            $ KittyX.Statup("Inbt", 80, 20)
    if Taboo:
        $ KittyX.Inbt += int(Taboo/10)
        $ KittyX.Lust += int(Taboo/5)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ KittyX.DrainWord("tabno")
    $ KittyX.DrainWord("no fondle ass")
    $ KittyX.RecentActions.append("fondle ass")
    $ KittyX.DailyActions.append("fondle ass")
    call Kitty_Pussy_Launch("fondle ass")

label Kitty_FA_Cycle: #Repeating strokes
    while Round > 0:
        call ViewShift(KittyX,KittyX.Pose,0,"fondle ass")
        call Shift_Focus(KittyX)
        $ KittyX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(KittyX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Kitty_FA_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0
                        "View":
                                    call ViewShift(KittyX,"menu")
                                    jump Kitty_FA_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if KittyX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ KittyX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")

                                    "Shift primary action":
                                            if KittyX.Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in.":
                                                                $ Situation = "shift"
                                                                call Kitty_FA_After
                                                                call Kitty_Insert_Ass
                                                        "Just stick a finger in without asking.":
                                                                $ Situation = "auto"
                                                                call Kitty_FA_After
                                                                call Kitty_Insert_Ass
                                                        "I want to lick your asshole.":
                                                                $ Situation = "shift"
                                                                call Kitty_FA_After
                                                                call Kitty_Lick_Ass
                                                        "Just start licking.":
                                                                $ Situation = "auto"
                                                                call Kitty_FA_After
                                                                call Kitty_Lick_Ass
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Kitty_FA_After
                                                                call Kitty_Dildo_Ass
                                                        "Never Mind":
                                                                jump Kitty_FA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Kitty_FA_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [KittyX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(KittyX)
                                            "Ask [KittyX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(KittyX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(KittyX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Kitty_FA_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Kitty_FA_Cycle
                                            "Never mind":
                                                        jump Kitty_FA_Cycle

                                    "Show her feet" if not ShowFeet and (KittyX.Pose == "doggy" or KittyX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (KittyX.Pose == "doggy" or KittyX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [KittyX.Name]":
                                            call Girl_Undress(KittyX)
                                    "Clean up [KittyX.Name] (locked)" if not KittyX.Spunk:
                                            pass
                                    "Clean up [KittyX.Name]" if KittyX.Spunk:
                                            call Girl_Cleanup(KittyX,"ask")
                                    "Never mind":
                                            jump Kitty_FA_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Kitty_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Kitty_FA_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Kitty_Pos_Reset
                                    $ Line = 0
                                    jump Kitty_FA_After
        #End menu (if Line)

        if KittyX.Panties or KittyX.PantsNum() > 6 or KittyX.HoseNum() >= 5: #This checks if Kitty wants to strip down.
                call Girl_Undress(KittyX,"auto")

        call Shift_Focus(KittyX)
        call Sex_Dialog(KittyX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or KittyX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(KittyX)
                            if "angry" in KittyX.RecentActions:
                                call Kitty_Pos_Reset
                                return
                            $ KittyX.Statup("Lust", 200, 5)
                            if 100 > KittyX.Lust >= 70 and KittyX.OCount < 2 and KittyX.SEXP >= 20:
                                $ KittyX.RecentActions.append("unsatisfied")
                                $ KittyX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Kitty_FA_After
                            $ Line = "came"

                    if KittyX.Lust >= 100:
                            #If Kitty can cum
                            call Girl_Cumming(KittyX)
                            if Situation == "shift" or "angry" in KittyX.RecentActions:
                                jump Kitty_FA_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in KittyX.RecentActions:#And Kitty is unsatisfied,
                                "[KittyX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Kitty_FA_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if KittyX.SEXP >= 100 or ApprovalCheck(KittyX, 1200, "LO"):
            pass
        elif Cnt == (5 + KittyX.FondleA):
                    $ KittyX.Brows = "confused"
                    ch_k "Uh, that's nice, but. . ."
        elif KittyX.Lust >= 80:
                    pass
        elif Cnt == (15 + KittyX.FondleA) and KittyX.SEXP >= 15 and not ApprovalCheck(KittyX, 1500):
                    $ KittyX.Brows = "confused"
                    menu:
                        ch_k "[KittyX.Petname], this is nice, but could we do something else?"
                        "Finish up.":
                                "You let go. . ."
                                jump Kitty_FA_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Kitty_FA_After
                        "No, this is fun.":
                                if ApprovalCheck(KittyX, 1200) or ApprovalCheck(KittyX, 500, "O"):
                                    $ KittyX.Statup("Love", 200, -5)
                                    $ KittyX.Statup("Obed", 50, 3)
                                    $ KittyX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ KittyX.FaceChange("angry", 1)
                                    call Kitty_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_k "Fun for you maybe, I'm tired of it."
                                    $ KittyX.Statup("Love", 50, -3, 1)
                                    $ KittyX.Statup("Love", 80, -4, 1)
                                    $ KittyX.Statup("Obed", 30, -1, 1)
                                    $ KittyX.Statup("Obed", 50, -1, 1)
                                    $ KittyX.RecentActions.append("angry")
                                    $ KittyX.DailyActions.append("angry")
                                    jump Kitty_FA_After
        #End Count check

        call Escalation(KittyX) #sees if she wants to escalate things

        if Round == 10:
            ch_k "It's[KittyX.like]getting kinda late."
        elif Round == 5:
            ch_k "We should wrap this up."

    #Round = 0 loop breaks
    $ KittyX.FaceChange("bemused", 0)
    $ Line = 0
    ch_k "Time to take a little break, for now."


label Kitty_FA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Kitty_Pos_Reset

    $ KittyX.FaceChange("sexy")

    $ KittyX.FondleA += 1
    $ KittyX.Action -=1
    if KittyX.PantsNum() < 6 or KittyX.Upskirt:
        $ KittyX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ KittyX.Addictionrate += 1

        call Partner_Like(KittyX,2)

    if KittyX.FondleA == 1:
            $ KittyX.SEXP += 4
            if not Situation:
                if KittyX.Love >= 500 and "unsatisfied" not in KittyX.RecentActions:
                    ch_k "Huh. . . um. . ."
                elif KittyX.Obed <= 500 and Player.Focus <= 20:
                    $ KittyX.FaceChange("perplexed", 1)
                    ch_k "Did you like that?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_k "Ok, what else did you want to do?"
    call Checkout
    return


# end KittyX.Fondle Ass /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Ass
label Kitty_Insert_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(KittyX)

    if KittyX.InsertA: #You've done it before
        $ temp_modifier += 25
    if KittyX.PantsNum() > 6 or KittyX.HoseNum() >= 5: # she's got pants on.
        $ temp_modifier -= 15
    if KittyX.Lust > 85 and KittyX.Loose: #She's really horny
        $ temp_modifier += 15
    if KittyX.Lust > 95 and KittyX.Loose:
        $ temp_modifier += 5
    if Situation == "shift":
        $ temp_modifier += 10
    if KittyX.Lust > 85 and Situation == "auto": #She's really horny
        $ temp_modifier += 10
    if "exhibitionist" in KittyX.Traits:
        $ temp_modifier += (4*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.Petnames:
        $ temp_modifier += 10
    elif "ex" in KittyX.Traits:
        $ temp_modifier -= 25
    if KittyX.ForcedCount and not KittyX.Forced:
        $ temp_modifier -= 5 * KittyX.ForcedCount

    if Taboo and "tabno" in KittyX.DailyActions:
        $ temp_modifier -= 10

    if "no insert ass" in KittyX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no insert ass" in KittyX.RecentActions else 0

    $ Approval = ApprovalCheck(KittyX, 1300, TabM = 3) # 130, 145, 160, Taboo -120(250)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ KittyX.FaceChange("surprised")
            $ KittyX.Statup("Obed", 90, 2)
            $ KittyX.Statup("Obed", 70, 2)
            $ KittyX.Statup("Inbt", 80, 2)
            $ KittyX.Statup("Inbt", 30, 2)
            "As you slide a finger in, [KittyX.Name] tightens around it in surprise, but seems into it."
            $ KittyX.FaceChange("sexy")
            jump Kitty_IA_Prep
        else:
            $ KittyX.FaceChange("surprised")
            $ KittyX.Statup("Love", 80, -2)
            $ KittyX.Statup("Obed", 50, -3)
            ch_k "Whoa, back off, [KittyX.Petname]."
            $ temp_modifier = 0
            $ Trigger2 = 0
            return

    if "insert ass" in KittyX.DailyActions and not KittyX.Loose:
        $ KittyX.FaceChange("bemused", 1)
        ch_k "I'm still a little sore from earlier, [KittyX.Petname]."
    elif "insert ass" in KittyX.DailyActions:
        $ KittyX.FaceChange("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Take it easy though.",
            "Mmm. . ."])
        ch_k "[Line]"

    if Approval >= 2:                                                                   #She's into it. . .
        if KittyX.Forced:
            $ KittyX.FaceChange("sad")
            $ KittyX.Statup("Love", 70, -3, 1)
            $ KittyX.Statup("Love", 20, -2, 1)
            $ KittyX.Statup("Obed", 90, 1)
            $ KittyX.Statup("Inbt", 60, 1)
            ch_k "Ok, whatever."
        else:
            $ KittyX.FaceChange("sexy", 1)
            $ KittyX.Eyes = "closed"
            $ KittyX.Statup("Love", 90, 1)
            $ KittyX.Statup("Inbt", 50, 3)
            $ KittyX.Statup("Lust", 200, 3)
            ch_k "Mmmmm. . ."
        $ KittyX.Statup("Obed", 20, 1)
        $ KittyX.Statup("Obed", 60, 1)
        $ KittyX.Statup("Inbt", 70, 2)
        jump Kitty_IA_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ KittyX.FaceChange("angry", 1)
        if "no insert ass" in KittyX.RecentActions:
            ch_k "I[KittyX.like]{i}just{/i} told you \"no!\""
        elif Taboo and "tabno" in KittyX.DailyActions and "no insert ass" in KittyX.DailyActions:
            ch_k "I told you that wasn't appropriate!"
        elif "no insert ass" in KittyX.DailyActions:
            ch_k "[KittyX.Like]take a lesson, [KittyX.Petname]."
        elif Taboo and "tabno" in KittyX.DailyActions:
            ch_k "Not here!"
        elif not KittyX.InsertA:
            $ KittyX.FaceChange("perplexed", 1)
            ch_k "I. . . don't think that's. . ."
        else:
            $ KittyX.FaceChange("bemused")
            ch_k "Oh, um, no, I'm not really comfortable with that. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no insert ass" in KittyX.DailyActions:
                $ KittyX.FaceChange("bemused")
                ch_k "Yeah, ok, [KittyX.Petname]."
                return
            "Maybe later?" if "no insert ass" not in KittyX.DailyActions:
                $ KittyX.FaceChange("sexy")
                ch_k "It's. . . possible, [KittyX.Petname]."
                $ KittyX.Statup("Love", 80, 2)
                $ KittyX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ KittyX.RecentActions.append("tabno")
                    $ KittyX.DailyActions.append("tabno")
                $ KittyX.RecentActions.append("no insert ass")
                $ KittyX.DailyActions.append("no insert ass")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ KittyX.FaceChange("sexy")
                    $ KittyX.Statup("Obed", 90, 2)
                    $ KittyX.Statup("Obed", 50, 2)
                    ch_k "Ok, you're probably right. . ."
                    $ KittyX.Statup("Inbt", 70, 3)
                    $ KittyX.Statup("Inbt", 40, 2)
                    jump Kitty_IA_Prep
                else:
                    $ KittyX.FaceChange("bemused")
                    ch_k "I really don't think that I would."

            "[[Slide a finger in anyway]":                                               # Pressured into being fingered.
                $ Approval = ApprovalCheck(KittyX, 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                if Approval > 1 or (Approval and KittyX.Forced):
                    $ KittyX.FaceChange("surprised", 1)
                    $ KittyX.Statup("Love", 70, -5, 1)
                    $ KittyX.Statup("Love", 200, -2)
                    ch_k "Oh. . . well, ok then. . ."
                    $ KittyX.FaceChange("sad")
                    $ KittyX.Statup("Obed", 50, 4)
                    $ KittyX.Statup("Inbt", 80, 1)
                    $ KittyX.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ KittyX.Forced = 1
                    jump Kitty_IA_Prep
                else:
                    $ KittyX.Statup("Love", 200, -15)
                    $ KittyX.FaceChange("angry", 1)
                    "She slaps your hand away."
                    $ KittyX.RecentActions.append("angry")
                    $ KittyX.DailyActions.append("angry")

    if "no insert ass" in KittyX.DailyActions:
        ch_k "How many times do I have to say \"no?\""
        $ KittyX.RecentActions.append("angry")
        $ KittyX.DailyActions.append("angry")
    elif KittyX.Forced:
        $ KittyX.FaceChange("angry", 1)
        ch_k "Um, no way."
        if ApprovalCheck(KittyX, 500, "I"):
                $ KittyX.Statup("Lust", 80, 10)
        else:
                $ KittyX.Statup("Lust", 50, 3)
        $ KittyX.Statup("Obed", 50, -2)
        $ KittyX.RecentActions.append("angry")
        $ KittyX.DailyActions.append("angry")
    elif Taboo:
        $ KittyX.FaceChange("angry", 1)
        $ KittyX.RecentActions.append("tabno")
        $ KittyX.DailyActions.append("tabno")
        ch_k "[KittyX.Petname]! Time and place!"
    elif KittyX.InsertA:
        $ KittyX.FaceChange("sad")
        ch_k "I don't feel like it."
    else:
        $ KittyX.FaceChange("surprised")
        ch_k "That's. . . not cool."
        $ KittyX.FaceChange()
    $ KittyX.RecentActions.append("no insert ass")
    $ KittyX.DailyActions.append("no insert ass")
    $ temp_modifier = 0
    return


label Kitty_IA_Prep: #Animation set-up
    if Trigger2 == "insert ass":
        return

    call Kitty_Pussy_Launch("insert ass")

    if Situation == KittyX:
            #Kitty auto-starts
            $ Situation = 0
            if (KittyX.Legs and not KittyX.Upskirt) or (KittyX.Panties and not KittyX.PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck(KittyX, 1250, TabM = 1) or (KittyX.SeenPussy and ApprovalCheck(KittyX, 500) and not Taboo):
                        $ KittyX.Upskirt = 1
                        $ KittyX.PantiesDown = 1
                        $ Line = 0
                        if KittyX.PantsNum() == 5:
                            $ Line = KittyX.Name + " hikes up her skirt"
                        elif KittyX.PantsNum() >= 5:
                            $ Line = KittyX.Name + " pulls down her " + KittyX.Legs
                        else:
                            $ Line = 0
                        if KittyX.Panties:
                            if Line:
                                #wearing pants
                                "[Line] and pulls her [KittyX.Panties] out of the way."
                                "She then grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
                            else:
                                #no pants
                                "She pulls her [KittyX.Panties] out of the way, and then presses your hand against her asshole."
                                "She clearly intends for you to get to work."
                        else:
                                #pants but no panties
                                "[Line], and then presses your hand against her asshole."
                                "She clearly intends for you to get to work."
                        call Kitty_First_Bottomless(1)
                else:
                        "[KittyX.Name] grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
            else:
                        "[KittyX.Name] grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
            menu:
                "What do you do?"
                "Get to work.":
                    $ KittyX.Statup("Inbt", 80, 3)
                    $ KittyX.Statup("Inbt", 50, 2)
                    "You press your finger into it."
                "Praise her.":
                    $ KittyX.FaceChange("sexy", 1)
                    $ KittyX.Statup("Inbt", 80, 3)
                    ch_p "Dirty girl, [KittyX.Pet]."
                    $ KittyX.NameCheck() #checks reaction to petname
                    "You press your finger into it."
                    $ KittyX.Statup("Love", 85, 1)
                    $ KittyX.Statup("Obed", 90, 1)
                    $ KittyX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    "You pull your hand back."
                    $ KittyX.FaceChange("surprised")
                    $ KittyX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that right now, [KittyX.Pet]."
                    $ KittyX.NameCheck() #checks reaction to petname
                    "[KittyX.Name] pulls back."
                    $ KittyX.Statup("Obed", 90, 1)
                    $ KittyX.Statup("Obed", 50, 1)
                    $ KittyX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ KittyX.AddWord(1,"refused","refused")
                    return
            #end auto

    if not KittyX.Forced and Situation != "auto":
        $ temp_modifier = 0
        call Bottoms_Off(KittyX)
        if "angry" in KittyX.RecentActions:
            return

    $ temp_modifier = 0
    if not KittyX.InsertA:
        if KittyX.Forced:
            $ KittyX.Statup("Love", 90, -50)
            $ KittyX.Statup("Obed", 70, 60)
            $ KittyX.Statup("Inbt", 80, 35)
        else:
            $ KittyX.Statup("Love", 90, 10)
            $ KittyX.Statup("Obed", 70, 20)
            $ KittyX.Statup("Inbt", 80, 25)

    if Taboo:
        $ KittyX.Inbt += int(Taboo/10)
        $ KittyX.Lust += int(Taboo/5)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ KittyX.DrainWord("tabno")
    $ KittyX.DrainWord("no insert ass")
    $ KittyX.RecentActions.append("insert ass")
    $ KittyX.DailyActions.append("insert ass")
    call Kitty_Pussy_Launch("insert ass")

label Kitty_IA_Cycle: #Repeating strokes
    while Round > 0:
        call ViewShift(KittyX,KittyX.Pose,0,"insert ass")
        call Shift_Focus(KittyX)
        $ KittyX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(KittyX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Kitty_IA_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0
                        "View":
                                    call ViewShift(KittyX,"menu")
                                    jump Kitty_IA_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if KittyX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ KittyX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")

                                    "Shift primary action":
                                            if KittyX.Action and MultiAction:
                                                    menu:
                                                        "Pull out and start rubbing again.":
                                                                $ Situation = "pullback"
                                                                call Kitty_IA_After
                                                                call Kitty_Fondle_Ass
                                                        "I want to lick your asshole.":
                                                                $ Situation = "shift"
                                                                call Kitty_IA_After
                                                                call Kitty_Lick_Ass
                                                        "Just start licking.":
                                                                $ Situation = "auto"
                                                                call Kitty_IA_After
                                                                call Kitty_Lick_Ass
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Kitty_IA_After
                                                                call Kitty_Dildo_Ass
                                                        "Never Mind":
                                                                jump Kitty_IA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Kitty_IA_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [KittyX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(KittyX)
                                            "Ask [KittyX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(KittyX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(KittyX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Kitty_IA_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Kitty_IA_Cycle
                                            "Never mind":
                                                        jump Kitty_IA_Cycle

                                    "Show her feet" if not ShowFeet and (KittyX.Pose == "doggy" or KittyX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (KittyX.Pose == "doggy" or KittyX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [KittyX.Name]":
                                            call Girl_Undress(KittyX)
                                    "Clean up [KittyX.Name] (locked)" if not KittyX.Spunk:
                                            pass
                                    "Clean up [KittyX.Name]" if KittyX.Spunk:
                                            call Girl_Cleanup(KittyX,"ask")
                                    "Never mind":
                                            jump Kitty_IA_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Kitty_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Kitty_IA_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Kitty_Pos_Reset
                                    $ Line = 0
                                    jump Kitty_IA_After
        #End menu (if Line)

        if KittyX.Panties or KittyX.PantsNum() > 6 or KittyX.HoseNum() >= 5: #This checks if Kitty wants to strip down.
                call Girl_Undress(KittyX,"auto")

        call Shift_Focus(KittyX)
        call Sex_Dialog(KittyX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or KittyX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(KittyX)
                            if "angry" in KittyX.RecentActions:
                                call Kitty_Pos_Reset
                                return
                            $ KittyX.Statup("Lust", 200, 5)
                            if 100 > KittyX.Lust >= 70 and KittyX.OCount < 2:
                                $ KittyX.RecentActions.append("unsatisfied")
                                $ KittyX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Kitty_IA_After
                            $ Line = "came"

                    if KittyX.Lust >= 100:
                            #If Kitty can cum
                            call Girl_Cumming(KittyX)
                            if Situation == "shift" or "angry" in KittyX.RecentActions:
                                jump Kitty_IA_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in KittyX.RecentActions:#And Kitty is unsatisfied,
                                "[KittyX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Kitty_IA_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if KittyX.SEXP >= 100 or ApprovalCheck(KittyX, 1200, "LO"):
            pass
        elif Cnt == (5 + KittyX.InsertA):
                    $ KittyX.Brows = "confused"
                    ch_k "What are you even?"
        elif KittyX.Lust >= 80:
                    pass
        elif Cnt == (15 + KittyX.InsertA) and KittyX.SEXP >= 15 and not ApprovalCheck(KittyX, 1500):
                    $ KittyX.Brows = "confused"
                    menu:
                        ch_k "[KittyX.Petname], this is getting kind sore, maybe we could try something else."
                        "Finish up.":
                                "You let go. . ."
                                jump Kitty_IA_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Kitty_IA_After
                        "No, this is fun.":
                                if ApprovalCheck(KittyX, 1200) or ApprovalCheck(KittyX, 500, "O"):
                                    $ KittyX.Statup("Love", 200, -5)
                                    $ KittyX.Statup("Obed", 50, 3)
                                    $ KittyX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ KittyX.FaceChange("angry", 1)
                                    call Kitty_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_k "Fun for you maybe, I'm tired of it."
                                    $ KittyX.Statup("Love", 50, -3, 1)
                                    $ KittyX.Statup("Love", 80, -4, 1)
                                    $ KittyX.Statup("Obed", 30, -1, 1)
                                    $ KittyX.Statup("Obed", 50, -1, 1)
                                    $ KittyX.RecentActions.append("angry")
                                    $ KittyX.DailyActions.append("angry")
                                    jump Kitty_IA_After
        #End Count check

        call Escalation(KittyX) #sees if she wants to escalate things

        if Round == 10:
            ch_k "It's[KittyX.like]getting kinda late."
        elif Round == 5:
            ch_k "We should wrap this up."

    #Round = 0 loop breaks
    $ KittyX.FaceChange("bemused", 0)
    $ Line = 0
    ch_k "Time to take a little break, for now."

label Kitty_IA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Kitty_Pos_Reset

    $ KittyX.FaceChange("sexy")

    $ KittyX.InsertA += 1
    $ KittyX.Action -=1
    $ KittyX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ KittyX.Addictionrate += 1

    call Partner_Like(KittyX,2)

    if KittyX.InsertA == 1:
            $ KittyX.SEXP += 12
            if not Situation:
                if KittyX.Love >= 500 and "unsatisfied" not in KittyX.RecentActions:
                    ch_k "That was odd. . ."
                elif KittyX.Obed <= 500 and Player.Focus <= 20:
                    $ KittyX.FaceChange("perplexed", 1)
                    ch_k "Well? Satisfied?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_k "Ok, what else did you want to do?"
    call Checkout
    return


# end KittyX.Insert Ass /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Ass
label Kitty_Lick_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(KittyX)
                                                                             # Will she let you lick? Modifiers
    if KittyX.LickA: #You've done it before
        $ temp_modifier += 20
    if KittyX.PantsNum() > 6 or KittyX.HoseNum() >= 5: # she's got pants on.
        $ temp_modifier -= 25
    if KittyX.Lust > 95:
        $ temp_modifier += 20
    elif KittyX.Lust > 85: #She's really horny
        $ temp_modifier += 15
    if KittyX.Lust > 85 and Situation == "auto": #auto
        $ temp_modifier += 10
    if Situation == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in KittyX.Traits:
        $ temp_modifier += (4*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.Petnames:
        $ temp_modifier += 10
    elif "ex" in KittyX.Traits:
        $ temp_modifier -= 25
    if KittyX.ForcedCount and not KittyX.Forced:
        $ temp_modifier -= 5 * KittyX.ForcedCount

    if Taboo and "tabno" in KittyX.DailyActions:
        $ temp_modifier -= 10

    if "no lick ass" in KittyX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no lick ass" in KittyX.RecentActions else 0

    $ Approval = ApprovalCheck(KittyX, 1550, TabM = 4) # 155, 170, 185, Taboo -160(315)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ KittyX.FaceChange("surprised")
            $ KittyX.Statup("Obed", 90, 1)
            $ KittyX.Statup("Inbt", 80, 3)
            $ KittyX.Statup("Inbt", 40, 2)
            "As you crouch down and start to lick her asshole, [KittyX.Name] startles briefly, but then begins to melt."
            $ KittyX.FaceChange("sexy")
            jump Kitty_LA_Prep
        else:
            $ KittyX.FaceChange("surprised")
            $ KittyX.Statup("Love", 80, -2)
            $ KittyX.Statup("Obed", 50, -3)
            ch_k "Um, don't do that. . ."
            $ temp_modifier = 0
            $ Trigger2 = 0
            return

    if "lick ass" in KittyX.RecentActions:
        $ KittyX.FaceChange("sexy", 1)
        ch_k "Mmm, again? Ok."
        jump Kitty_LA_Prep
    elif "lick ass" in KittyX.DailyActions:
        $ KittyX.FaceChange("sexy", 1)
        ch_k "Didn't get enough earlier?"


    if Approval >= 2:                                                                   #She's into it. . .
        if KittyX.Forced:
            $ KittyX.FaceChange("sad")
            $ KittyX.Statup("Love", 70, -3, 1)
            $ KittyX.Statup("Love", 20, -2, 1)
            $ KittyX.Statup("Obed", 90, 2)
            $ KittyX.Statup("Inbt", 60, 2)
            ch_k "Ok, whatever."
        else:
            $ KittyX.FaceChange("sexy", 1)
            $ KittyX.Eyes = "closed"
            $ KittyX.Statup("Love", 90, 1)
            $ KittyX.Statup("Inbt", 60, 2)
            $ KittyX.Statup("Lust", 200, 3)
            ch_k "Wha. . ."
        $ KittyX.Statup("Obed", 20, 1)
        $ KittyX.Statup("Obed", 60, 1)
        $ KittyX.Statup("Inbt", 80, 2)
        jump Kitty_LA_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ KittyX.FaceChange("angry", 1)
        if "no lick ass" in KittyX.RecentActions:
            ch_k "I[KittyX.like]{i}just{/i} told you \"no!\""
        elif Taboo and "tabno" in KittyX.DailyActions and "no lick ass" in KittyX.DailyActions:
            ch_k "I told you not to touch me like that in public!"
        elif "no lick ass" in KittyX.DailyActions:
            ch_k "[KittyX.Like]take a lesson, [KittyX.Petname]."
        elif Taboo and "tabno" in KittyX.DailyActions:
            ch_k "Not here!"
        elif not KittyX.LickA:                    #First time dialog
            $ KittyX.FaceChange("bemused", 1)
            if KittyX.Love >= KittyX.Obed and KittyX.Love >= KittyX.Inbt:
                ch_k "That's, I don't know. . ."
            elif KittyX.Obed >= KittyX.Inbt:
                ch_k "You don't have to do that."
            else:
                $ KittyX.Eyes = "sexy"
                ch_k "That's kinda gross. . ."
        else:
            $ KittyX.FaceChange("bemused")
            ch_k "Not now, [KittyX.Petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no lick ass" in KittyX.DailyActions:
                $ KittyX.FaceChange("bemused")
                ch_k "Yeah, ok, [KittyX.Petname]."
                return
            "I'm sure I can convince you later. . ." if "no lick ass" not in KittyX.DailyActions:
                $ KittyX.FaceChange("sexy")
                ch_k "Anything's possible, [KittyX.Petname]."
                $ KittyX.Statup("Love", 80, 2)
                $ KittyX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ KittyX.RecentActions.append("tabno")
                    $ KittyX.DailyActions.append("tabno")
                $ KittyX.RecentActions.append("no lick ass")
                $ KittyX.DailyActions.append("no lick ass")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ KittyX.FaceChange("sexy")
                    $ KittyX.Statup("Obed", 90, 2)
                    $ KittyX.Statup("Obed", 50, 2)
                    ch_k "Ok, you're probably right. . ."
                    $ KittyX.Statup("Inbt", 70, 3)
                    $ KittyX.Statup("Inbt", 40, 2)
                    jump Kitty_LA_Prep
                else:
                    $ KittyX.FaceChange("sexy")
                    ch_k "I really don't think so."

            "[[Start licking anyway]":                                               # Pressured into being licked.
                $ Approval = ApprovalCheck(KittyX, 1100, "OI", TabM = 4) # 110, 125, 140, -160(270)
                if Approval > 1 or (Approval and KittyX.Forced):
                    $ KittyX.FaceChange("sad")
                    $ KittyX.Statup("Love", 70, -5, 1)
                    $ KittyX.Statup("Love", 200, -2)
                    ch_k "Ok, {i}fine{/i}."
                    $ KittyX.Statup("Obed", 50, 4)
                    $ KittyX.Statup("Inbt", 80, 1)
                    $ KittyX.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ KittyX.Forced = 1
                    jump Kitty_LA_Prep
                else:
                    $ KittyX.Statup("Love", 200, -15)
                    $ KittyX.FaceChange("angry", 1)
                    "She shoves your head back."
                    $ KittyX.RecentActions.append("angry")
                    $ KittyX.DailyActions.append("angry")

    if "no lick ass" in KittyX.DailyActions:
        ch_k "How many times do I have to say \"no?\""
        $ KittyX.RecentActions.append("angry")
        $ KittyX.DailyActions.append("angry")
    elif KittyX.Forced:
        $ KittyX.FaceChange("angry", 1)
        ch_k "Ew, no way."
        if ApprovalCheck(KittyX, 500, "I"):
                $ KittyX.Statup("Lust", 80, 10)
        else:
                $ KittyX.Statup("Lust", 50, 3)
        $ KittyX.Statup("Obed", 50, -2)
        $ KittyX.RecentActions.append("angry")
        $ KittyX.DailyActions.append("angry")
    elif Taboo:
        $ KittyX.FaceChange("angry", 1)
        $ KittyX.RecentActions.append("tabno")
        $ KittyX.DailyActions.append("tabno")
        ch_k "This just really isn't the time or place, [KittyX.Petname]!"
    elif KittyX.LickA:
        $ KittyX.FaceChange("sad")
        ch_k "Sorry, no more of that."
    else:
        $ KittyX.FaceChange("surprised")
        ch_k "Ew."
        $ KittyX.FaceChange()
    $ KittyX.RecentActions.append("no lick ass")
    $ KittyX.DailyActions.append("no lick ass")
    $ temp_modifier = 0
    return

label Kitty_LA_Prep: #Animation set-up
    if Trigger2 == "lick ass":
        return
    if not KittyX.Forced and Situation != "auto":
        $ temp_modifier = 0
        if KittyX.PantsNum() > 6:
            $ temp_modifier = 15
        call Bottoms_Off(KittyX)
        if "angry" in KittyX.RecentActions:
            return
    $ temp_modifier = 0
    call Kitty_Pussy_Launch("lick ass")
    if not KittyX.LickA:
        if KittyX.Forced:
            $ KittyX.Statup("Love", 90, -30)
            $ KittyX.Statup("Obed", 70, 40)
            $ KittyX.Statup("Inbt", 80, 80)
        else:
            $ KittyX.Statup("Love", 90, 35)
            $ KittyX.Statup("Obed", 70, 25)
            $ KittyX.Statup("Inbt", 80, 55)
    if Taboo:
        $ KittyX.Inbt += int(Taboo/10)
        $ KittyX.Lust += int(Taboo/5)
    if Situation:
        $ renpy.pop_call()
        $ Situation = 0

    $ KittyX.Upskirt = 1
    if KittyX.PantsNum() == 5:
        $ KittyX.SeenPanties = 1
    if not KittyX.Panties:
        call Kitty_First_Bottomless(1)
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ KittyX.DrainWord("tabno")
    $ KittyX.DrainWord("no lick ass")

    $ KittyX.RecentActions.append("lick") if "lick" not in KittyX.RecentActions else KittyX.RecentActions
    $ KittyX.RecentActions.append("ass") if "ass" not in KittyX.RecentActions else KittyX.RecentActions
    $ KittyX.RecentActions.append("lick ass")

    $ KittyX.DailyActions.append("lick") if "lick" not in KittyX.DailyActions else KittyX.RecentActions
    $ KittyX.DailyActions.append("ass") if "ass" not in KittyX.DailyActions else KittyX.RecentActions
    $ KittyX.DailyActions.append("lick ass")
    call Kitty_Pussy_Launch("lick ass")
label Kitty_LA_Cycle: #Repeating strokes
    if Trigger2 == "kiss you":
            $ Trigger2 = 0
    while Round > 0:
        call ViewShift(KittyX,KittyX.Pose,0,"lick ass")
        call Shift_Focus(KittyX)
        $ KittyX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(KittyX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Kitty_LA_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0
                        "View":
                                    call ViewShift(KittyX,"menu")
                                    jump Kitty_LA_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if KittyX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ KittyX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")

                                    "Shift primary action":
                                            if KittyX.Action and MultiAction:
                                                    menu:
                                                        "Switch to fondling.":
                                                                $ Situation = "pullback"
                                                                call Kitty_LA_After
                                                                call Kitty_Fondle_Ass
                                                        "I want to stick a finger in.":
                                                                $ Situation = "shift"
                                                                call Kitty_LA_After
                                                                call Kitty_Insert_Ass
                                                        "Just stick a finger in [[without asking].":
                                                                $ Situation = "auto"
                                                                call Kitty_LA_After
                                                                call Kitty_Insert_Ass
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Kitty_LA_After
                                                                call Kitty_Dildo_Ass
                                                        "Never Mind":
                                                                jump Kitty_LA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Kitty_LA_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [KittyX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(KittyX)
                                            "Ask [KittyX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(KittyX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(KittyX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Kitty_LA_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Kitty_LA_Cycle
                                            "Never mind":
                                                        jump Kitty_LA_Cycle

                                    "Show her feet" if not ShowFeet and (KittyX.Pose == "doggy" or KittyX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (KittyX.Pose == "doggy" or KittyX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [KittyX.Name]":
                                            call Girl_Undress(KittyX)
                                    "Clean up [KittyX.Name] (locked)" if not KittyX.Spunk:
                                            pass
                                    "Clean up [KittyX.Name]" if KittyX.Spunk:
                                            call Girl_Cleanup(KittyX,"ask")
                                    "Never mind":
                                            jump Kitty_LA_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Kitty_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Kitty_LA_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Kitty_Pos_Reset
                                    $ Line = 0
                                    jump Kitty_LA_After
        #End menu (if Line)

        if KittyX.Panties or KittyX.PantsNum() > 6 or KittyX.HoseNum() >= 5: #This checks if Kitty wants to strip down.
                call Girl_Undress(KittyX,"auto")

        call Shift_Focus(KittyX)
        call Sex_Dialog(KittyX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or KittyX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(KittyX)
                            if "angry" in KittyX.RecentActions:
                                call Kitty_Pos_Reset
                                return
                            $ KittyX.Statup("Lust", 200, 5)
                            if 100 > KittyX.Lust >= 70 and KittyX.OCount < 2:
                                $ KittyX.RecentActions.append("unsatisfied")
                                $ KittyX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Kitty_LA_After
                            $ Line = "came"

                    if KittyX.Lust >= 100:
                            #If Kitty can cum
                            call Girl_Cumming(KittyX)
                            if Situation == "shift" or "angry" in KittyX.RecentActions:
                                jump Kitty_LA_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in KittyX.RecentActions:#And Kitty is unsatisfied,
                                "[KittyX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Kitty_LA_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if KittyX.SEXP >= 100 or ApprovalCheck(KittyX, 1200, "LO"):
            pass
        elif Cnt == (5 + KittyX.LickA):
                    $ KittyX.Brows = "confused"
                    ch_k "What are you even?"
        elif KittyX.Lust >= 80:
                    pass
        elif Cnt == (15 + KittyX.LickA) and KittyX.SEXP >= 15 and not ApprovalCheck(KittyX, 1500):
                    $ KittyX.Brows = "confused"
                    menu:
                        ch_k "[KittyX.Petname], this is getting weird, maybe we could try something else."
                        "Finish up.":
                                "You let go. . ."
                                jump Kitty_LA_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Kitty_LA_After
                        "No, this is fun.":
                                if ApprovalCheck(KittyX, 1200) or ApprovalCheck(KittyX, 500, "O"):
                                    $ KittyX.Statup("Love", 200, -5)
                                    $ KittyX.Statup("Obed", 50, 3)
                                    $ KittyX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ KittyX.FaceChange("angry", 1)
                                    call Kitty_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_k "Fun for you maybe, I'm tired of it."
                                    $ KittyX.Statup("Love", 50, -3, 1)
                                    $ KittyX.Statup("Love", 80, -4, 1)
                                    $ KittyX.Statup("Obed", 30, -1, 1)
                                    $ KittyX.Statup("Obed", 50, -1, 1)
                                    $ KittyX.RecentActions.append("angry")
                                    $ KittyX.DailyActions.append("angry")
                                    jump Kitty_LA_After
        #End Count check

        call Escalation(KittyX) #sees if she wants to escalate things

        if Round == 10:
            ch_k "It's[KittyX.like]getting kinda late."
        elif Round == 5:
            ch_k "We should wrap this up."

    #Round = 0 loop breaks
    $ KittyX.FaceChange("bemused", 0)
    $ Line = 0
    ch_k "Time to take a little break, for now."

label Kitty_LA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Kitty_Pos_Reset

    $ KittyX.FaceChange("sexy")

    $ KittyX.LickA += 1
    $ KittyX.Action -=1
    if KittyX.PantsNum() < 6 or KittyX.Upskirt:
        $ KittyX.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ KittyX.Addictionrate += 1

    call Partner_Like(KittyX,2)

    if KittyX.LickA == 1:
            $ KittyX.SEXP += 15
            if not Situation:
                if KittyX.Love >= 500 and "unsatisfied" not in KittyX.RecentActions:
                    ch_k "That was. . . good for you?"
                elif KittyX.Obed <= 500 and Player.Focus <= 20:
                    $ KittyX.FaceChange("perplexed", 1)
                    ch_k "Did that work for you?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_k "Ok, what else did you want to do?"
    call Checkout
    return

# end KittyX.Lick Ass /////////////////////////////////////////////////////////////////////////////
