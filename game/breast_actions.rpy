label fondle_breasts(character):
    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(character)

    if character.FondleB:
        $ temp_modifier += 15

    if character.Lust > 75: #She's really horny
        $ temp_modifier += 20

    if "exhibitionist" in character.Traits:
        $ temp_modifier += (3*Taboo)

    if character in Player.Harem or "sex friend" in character.Petnames:
        $ temp_modifier += 10
    elif "ex" in character.Traits:
        $ temp_modifier -= 20

    if character.ForcedCount and not character.Forced:
        $ temp_modifier -= 5*character.ForcedCount

    if Taboo and "tabno" in character.DailyActions:
        $ temp_modifier -= 10

    if "no fondle breasts" in character.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no fondle breasts" in character.RecentActions else 0

    $ Approval = ApprovalCheck(character, 950, TabM = 3)

    if Situation == "auto":
        if Approval:
            $ character.FaceChange("sexy")
            $ character.Statup("Obed", 90, 1)
            $ character.Statup("Obed", 70, 2)
            $ character.Statup("Inbt", 70, 3)
            $ character.Statup("Inbt", 30, 2)

            "As you cup her breast, [character.Name] gently nods."

            call fondle_breasts_prep(character)

            return
        else:
            $ character.FaceChange("surprised")
            $ character.Brows = "confused"
            $ character.Statup("Obed", 50, -2)

            call go_back_dialog(character)

            $ temp_modifier = 0
            $ Trigger2 = 0

            return

    if Approval:                                                                       #Second time+ dialog
        $ character.FaceChange("sexy", 1)

        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Love", 20, -2, 1)

        elif not Taboo and "tabno" in character.DailyActions:
            call private_enough_dialog(character)

    if "fondle breasts" in character.RecentActions:
        $ character.FaceChange("sexy", 1)

        call repeat_action_dialog(character)
        call fondle_breasts_prep(character)

        return
    elif "fondle breasts" in character.DailyActions:
        $ character.FaceChange("sexy", 1)

        call gently_dialog(character)

    if Approval >= 2:
        $ character.FaceChange("bemused", 1)

        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Love", 20, -2, 1)
            $ character.Statup("Obed", 90, 1)
            $ character.Statup("Inbt", 60, 1)

        call come_and_get_em_dialog(character)

        $ character.Statup("Love", 90, 1)
        $ character.Statup("Inbt", 50, 3)

        call fondle_breasts_prep(character)

        return
    else:
        $ character.FaceChange("angry", 1)

        if "no fondle breasts" in character.RecentActions:
            call just_told_you_no_dialog(character)
        elif Taboo and "tabno" in character.DailyActions and "no fondle breasts" in character.DailyActions:
            call had_enough_of_this_dialog(character)
        elif "no fondle breasts" in character.DailyActions:
            call already_said_no_dialog(character)
        elif Taboo and "tabno" in character.DailyActions:
            call already_said_not_here_dialog(character)
        elif not character.FondleB:
            $ character.FaceChange("bemused")

            call not_ready_yet_dialog(character)
        else:
            $ character.FaceChange("bemused")

            call rather_not_dialog(character)
        menu:
            extend ""
            "Sorry, never mind." if "no fondle breasts" in character.DailyActions:
                $ character.FaceChange("bemused")

                call no_problem_dialog(character)

                return
            "Maybe later?" if "no fondle breasts" not in character.DailyActions:
                $ character.FaceChange("sexy")

                if character not in [LauraX, JubesX]:
                    "She re-adjusts her cleavage."

                call maybe_later_dialog(character)

                $ character.Statup("Love", 80, 1)
                $ character.Statup("Love", 50, 1)
                $ character.Statup("Inbt", 30, 2)

                if Taboo:
                    $ character.AddWord(1,"tabno","tabno")

                $ character.RecentActions.append("no fondle breasts")
                $ character.DailyActions.append("no fondle breasts")

                return
            "Come on, Please?":
                if Approval:
                    $ character.FaceChange("sexy")

                    if character != LauraX:
                        $ character.Statup("Obed", 90, 1)

                    $ character.Statup("Obed", 50, 2)
                    $ character.Statup("Inbt", 60, 3)
                    $ character.Statup("Inbt", 30, 2)

                    call reward_politeness_dialog(character)
                    call fondle_breasts_prep(character)

                    return
                else:
                    $ character.FaceChange("sexy")

                    call please_not_good_enough_dialog(character)
            "[[Grab her chest anyway]":
                $ Approval = ApprovalCheck(character, 350, "OI", TabM = 3)

                if Approval > 1 or (Approval and character.Forced):
                    $ character.FaceChange("sad")
                    $ character.Statup("Love", 70, -5, 1)
                    $ character.Statup("Love", 20, -2, 1)

                    call forced_but_not_unwelcome_dialog(character)

                    $ character.Statup("Obed", 90, 2)
                    $ character.Statup("Obed", 50, 4)
                    $ character.Statup("Inbt", 60, 3)

                    if Approval < 2:
                        $ character.Forced = 1

                    call fondle_breasts_prep(character)

                    return
                else:
                    $ character.Statup("Love", 200, -10)
                    $ character.FaceChange("angry", 1)

                    "She slaps your hand away."

                    $ character.AddWord(1,"angry","angry")

    if "no fondle breasts" in character.DailyActions:
        call learn_to_take_no_dialog(character)

        $ character.AddWord(1,"angry","angry")
    elif character.Forced:
        $ character.FaceChange("angry", 1)

        call went_too_far_dialog(character)

        $ character.Statup("Lust", 60, 5)
        $ character.Statup("Obed", 50, -2)
        $ character.AddWord(1,"angry","angry")
    elif Taboo:
        $ character.FaceChange("angry", 1)
        $ character.AddWord(1,"tabno","tabno")

        call not_in_public_dialog(character)
    elif character.FondleB:
        $ character.FaceChange("sad")

        call you_had_your_shot_dialog(character)
    else:
        $ character.FaceChange("sexy")
        $ character.Mouth = "sad"

        call not_happening_dialog(character)

    $ character.RecentActions.append("no fondle breasts")
    $ character.DailyActions.append("no fondle breasts")

    $ temp_modifier = 0

    return

label fondle_breasts_prep(character): #Animation set-up
    if Trigger == "kiss you":
        $ Trigger = "fondle breasts"

        return

    if Trigger2 == "fondle breasts":
        return

    call breasts_launch(character, "fondle breasts")

    if Situation == character:
        $ Situation = 0

        if (character.Over or character.Chest) and not character.Uptop:
            if ApprovalCheck(character, 1250, TabM = 1) or (character.SeenChest and ApprovalCheck(character, 500) and not Taboo):
                $ character.Uptop = 1

                $ Line = character.Over if character.Over else character.Chest

                "With a mischievous grin, [character.Name] pulls her [Line] up over her breasts."

                call first_topless(character, silent = True)

                $ Line = 0

                "She then grabs your arm and shoves your hand against her breast, clearly intending you to get to work."
            else:
                "[character.Name] grabs your arm and shoves your hand against her covered breast, clearly intending you to get to work."
        else:
            "[character.Name] grabs your arm and shoves your hand against her breast, clearly intending you to get to work."

        menu:
            "What do you do?"
            "Get to work.":
                $ character.Statup("Inbt", 80, 3)
                $ character.Statup("Inbt", 50, 2)

                "You start to fondle them."
            "Praise her.":
                $ character.FaceChange("sexy", 1)
                $ character.Statup("Inbt", 80, 3)

                ch_p "I like the initiative, [character.Pet]."

                $ character.NameCheck() #checks reaction to petname

                "You start to fondle them."

                $ character.Statup("Love", 85, 1)
                $ character.Statup("Obed", 90, 1)
                $ character.Statup("Obed", 50, 2)
            "Ask her to stop.":
                "You pull your hand back."

                $ character.FaceChange("surprised")
                $ character.Statup("Inbt", 70, 1)

                ch_p "Let's not do that right now, [character.Pet]."

                $ character.NameCheck() #checks reaction to petname

                "[character.Name] pulls back."

                $ character.Statup("Obed", 90, 1)
                $ character.Statup("Obed", 50, 1)
                $ character.Statup("Obed", 30, 2)

                $ Player.RecentActions.append("nope")

                $ character.AddWord(1,"refused","refused")

                return

    if not character.Forced and Situation != "auto":
        $ temp_modifier = 0

        call Top_Off(character)

        if "angry" in character.RecentActions:
            return

    $ temp_modifier = 0

    if not character.FondleB:
        if character.Forced:
            $ character.Statup("Love", 90, -20)
            $ character.Statup("Obed", 70, 25)
            $ character.Statup("Inbt", 80, 15)
        else:
            $ character.Statup("Love", 90, 10)
            $ character.Statup("Obed", 70, 5)
            $ character.Statup("Inbt", 80, 15)

    if Taboo:
        $ character.Inbt += int(Taboo/10)
        $ character.Lust += int(Taboo/5)

    if Situation:
        $ Situation = 0

    $ Line = 0
    $ Cnt = 0

    if Taboo:
        $ character.DrainWord("tabno")

    $ character.DrainWord("no fondle breasts")
    $ character.AddWord(0,"fondle breasts","fondle breasts")

    call breasts_launch(character, "fondle breasts")
    call fondle_breasts_cycle(character)

    return

label fondle_breasts_cycle(character): #Repeating strokes
    while Round > 0:
        call ViewShift(character,character.Pose,0,"fondle breasts")
        call Shift_Focus(character)

        $ character.LustFace()

        if Player.Focus < 100:
            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":
                    call Slap_Ass(character)

                    $ Cnt += 1
                    $ Round -= 1

                    call fondle_breasts_cycle(character)

                    return
                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."

                    $ Player.FocusX = 1
                "Release your focus." if Player.FocusX:
                    "You release your concentration. . ."

                    $ Player.FocusX = 0
                "View":
                    call ViewShift(character,"menu")
                    call fondle_breasts_cycle(character)

                    return
                "Other options":
                    menu:
                        "Offhand action":
                            if character.Action and MultiAction:
                                call Offhand_Set

                                if Trigger2:
                                     $ character.Action -= 1
                            else:
                                call tired_dialog(character)
                        "Shift primary action":
                            if character.Action and MultiAction:
                                menu:
                                    "Ask to suck on them.":
                                        if character.Action and MultiAction:
                                            $ Situation = "shift"

                                            call fondle_breasts_after(character)
                                            call suck_breasts(character)

                                            return
                                        else:
                                            call tired_dialog(character)
                                    "Just suck on them without asking.":
                                        if character.Action and MultiAction:
                                            $ Situation = "auto"

                                            call fondle_breasts_after(character)
                                            call suck_breasts(character)

                                            return
                                        else:
                                            "As you lean in to suck on her breast, she grabs your head and pushes back."

                                            call tired_dialog(character)
                                    "Never Mind":
                                        pass

                                call fondle_breasts_cycle(character)

                                return
                            else:
                                call tired_dialog(character)
                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [character.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                    call Les_Change(character)
                                "Ask [character.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                    pass
                                "Ask [Partner.Name] to do something else":
                                    call Three_Change(character)
                                "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                    $ ThreeCount = 0
                                "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                    $ ThreeCount = 0
                                "Swap to [Partner.Name]":
                                    call Trigger_Swap(character)
                                "Undress [Partner.Name]":
                                    call Girl_Undress(Partner)
                                    call fondle_breasts_cycle(character)

                                    return
                                "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.Name]" if Partner.Spunk:
                                    call Girl_Cleanup(Partner,"ask")
                                    call fondle_breasts_cycle(character)

                                    return
                                "Never mind":
                                    call fondle_breasts_cycle(character)

                                    return
                        "Show her feet" if not ShowFeet and (character.Pose == "doggy" or character.Pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (character.Pose == "doggy" or character.Pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [character.Name]":
                            call Girl_Undress(character)
                        "Clean up [character.Name] (locked)" if not character.Spunk:
                            pass
                        "Clean up [character.Name]" if character.Spunk:
                            call Girl_Cleanup(character,"ask")
                        "Never mind":
                            call fondle_breasts_cycle(character)

                            return
                "Back to Sex Menu" if MultiAction:
                    ch_p "Let's try something else."

                    call reset_position(character)

                    $ Situation = "shift"

                    $ Line = 0

                    call fondle_breasts_after(character)

                    return
                "End Scene" if not MultiAction:
                    ch_p "Let's stop for now."

                    call reset_position(character)

                    $ Line = 0

                    call fondle_breasts_after(character)

                    return

        call Shift_Focus(character)
        call Sex_Dialog(character,Partner)

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus

        if Player.Focus >= 100 or character.Lust >= 100:
            if Player.Focus >= 100:
                call Player_Cumming(character)

                if "angry" in character.RecentActions:
                    call reset_position(character)

                    return

                $ character.Statup("Lust", 200, 5)

                if 100 > character.Lust >= 70 and character.OCount < 2 and character.SEXP >= 20:
                    $ character.AddWord(0,"unsatisfied","unsatisfied")

                if Player.Focus > 80:
                    call fondle_breasts_after(character)

                    return

                $ Line = "came"

            if character.Lust >= 100:
                call Girl_Cumming(character)

                if Situation == "shift" or "angry" in character.RecentActions:
                    call fondle_breasts_after(character)

                    return

            if Line == "came": #ex Player.Focus <= 20:
                $ Line = 0

                if not Player.Semen:
                    "You're emptied out, you should probably take a break."

                if "unsatisfied" in character.RecentActions:#And Rogue is unsatisfied,
                    "[character.Name] still seems a bit unsatisfied with the experience."

                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."

                            call fondle_breasts_after(character)

                            return

        if Partner and Partner.Lust >= 100:
            call Girl_Cumming(Partner)

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if character.SEXP >= 100 or ApprovalCheck(character, 1200, "LO"):
            pass
        elif Cnt == (5 + character.FondleB):
            $ character.Brows = "confused"

            call warm_hands_dialog(character)
        elif character.Lust >= 85:
            pass
        elif Cnt == (15 + character.FondleB) and character.SEXP >= 15 and not ApprovalCheck(character, 1500):
            $ character.Brows = "confused"

            call try_something_else_dialog(character)

            menu:
                extend ""
                "Finish up.":
                    "You let go. . ."

                    call fondle_breasts_after(character)

                    return
                "Let's try something else." if MultiAction:
                    $ Line = 0
                    $ Situation = "shift"

                    call fondle_breasts_after(character)

                    return
                "No, this is fun.":
                    if ApprovalCheck(character, 1200) or ApprovalCheck(character, 500, "O"):
                        $ character.Statup("Love", 200, -5)
                        $ character.Statup("Obed", 50, 3)
                        $ character.Statup("Obed", 80, 2)

                        "She grumbles but lets you keep going."
                    else:
                        $ character.FaceChange("angry", 1)

                        call reset_position(character)

                        "She scowls at you and pulls back."

                        call this_is_boring_dialog(character)

                        $ character.Statup("Love", 50, -3, 1)
                        $ character.Statup("Love", 80, -4, 1)
                        $ character.Statup("Obed", 30, -1, 1)
                        $ character.Statup("Obed", 50, -1, 1)
                        $ character.AddWord(1,"angry","angry")

                        call fondle_breasts_after(character)

                        return

        call Escalation(character)

        if Round == 10:
            call wrap_this_up_dialog(character)
        elif Round == 5:
            call time_to_stop_soon_dialog(character)

        if character.Lust >= 50 and not character.Uptop and (character.Chest or character.Over):
            $ character.Uptop = 1

            if character == RogueX:
                "[character.Name] shrugs and pulls her top open."
            elif character == KittyX:
                "[KittyX.Name] laughs and pulls her top open."
            elif character in [EmmaX, StormX]:
                "[EmmaX.Name] sighs and tugs her breasts free of her clothes."
            elif character in [LauraX, JeanX, JubesX]:
                "[character.Name] grunts and pulls her clothes aside."

            call first_topless(character)

    $ character.FaceChange("bemused", 0)

    $ Line = 0

    call im_done_dialog(character)
    call fondle_breasts_after(character)

    return

label fondle_breasts_after(character):
    $ character.FaceChange("sexy")
    $ character.FondleB += 1
    $ character.Action -=1
    $ character.Addictionrate += 1

    if "addictive" in Player.Traits:
        $ character.Addictionrate += 1

    call Partner_Like(character,2)

    if character.FondleB == 1:
        $ character.SEXP += 4

        if not Situation:
            if character.Love >= 500 and "unsatisfied" not in character.RecentActions:
                call that_was_nice_dialog(character)
            elif character.Obed <= 500 and Player.Focus <= 20:
                $ character.FaceChange("perplexed", 1)

                call was_that_enough_dialog(character)

    $ temp_modifier = 0

    call Checkout

    if Situation:
        call Sex_Basic_Dialog(character, "switch")
    else:
        call reset_position(character)

    return

label suck_breasts(character):
    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(character)
                                                                                        # Will she let you suck? Modifiers
    if character.SuckB: #You've done it before
        $ temp_modifier += 15

    if not character.Chest and not character.Over:
        $ temp_modifier += 15

    if character.Lust > 75: #She's really horny
        $ temp_modifier += 20

    if character.Lust > 75 and Situation == "auto": #She's really horny
        $ temp_modifier += 10

    if "exhibitionist" in character.Traits:
        $ temp_modifier += (4*Taboo)

    if character in Player.Harem or "sex friend" in character.Petnames:
        $ temp_modifier += 10
    elif "ex" in character.Traits:
        $ temp_modifier -= 25

    if character.ForcedCount and not character.Forced:
        $ temp_modifier -= 5 * character.ForcedCount

    if Taboo and "tabno" in character.DailyActions:
        $ temp_modifier -= 10

    if "no suck breasts" in character.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no suck breasts" in character.RecentActions else 0

    $ Approval = ApprovalCheck(character, 1050, TabM = 4) # 105, 120, 135, Taboo -160(265)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ character.FaceChange("sexy")
            $ character.Statup("Obed", 90, 1)
            $ character.Statup("Obed", 70, 2)
            $ character.Statup("Inbt", 70, 3)
            $ character.Statup("Inbt", 30, 2)

            "As you dive in, [character.Name] seems a bit surprised, but just makes a little \"coo.\""

            call suck_breasts_prep(character)

            return
        else:
            $ character.FaceChange("surprised")
            $ character.Statup("Obed", 50, -2)

            call go_back_dialog(character)

            $ temp_modifier = 0
            $ Trigger2 = 0

            return

    if "suck breasts" in character.RecentActions:
        $ character.FaceChange("sexy", 1)

        call repeat_action_dialog(character)
        call suck_breasts_prep(character)

        return
    elif "suck breasts" in character.DailyActions:
        $ character.FaceChange("sexy", 1)

        call gently_dialog(character)

    if Approval >= 2:                                                                   #She's into it. . .
        $ character.FaceChange("bemused", 1)

        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Love", 20, -2, 1)
            $ character.Statup("Obed", 90, 1)
            $ character.Statup("Inbt", 60, 1)

        call come_and_get_em_dialog(character)

        $ character.Statup("Love", 90, 1)
        $ character.Statup("Inbt", 50, 3)

        call suck_breasts_prep(character)

        return
    else:                                                                               #She's not into it, but maybe. . .
        $ character.FaceChange("angry", 1)

        if "no suck breasts" in character.RecentActions:
            call just_told_you_no_dialog(character)
        elif Taboo and "tabno" in character.DailyActions and "no suck breasts" in character.DailyActions:
            call had_enough_of_this_dialog(character)
        elif "no suck breasts" in character.DailyActions:
            call already_said_no_dialog(character)
        elif Taboo and "tabno" in character.DailyActions:
            call already_said_not_here_dialog(character)
        elif not character.SuckB:
            $ character.FaceChange("bemused")

            call not_ready_yet_dialog(character)
        else:
            $ character.FaceChange("bemused")

            call rather_not_dialog(character)
        menu:
            extend ""
            "Sorry, never mind." if "no suck breasts" in character.DailyActions:
                $ character.FaceChange("bemused")

                call no_problem_dialog(character)

                return
            "Maybe later?" if "no suck breasts" not in character.DailyActions:
                $ character.FaceChange("sexy")

                call maybe_later_dialog(character)

                $ character.Statup("Love", 80, 1)
                $ character.Statup("Love", 50, 1)
                $ character.Statup("Inbt", 30, 2)

                if Taboo:
                    $ character.AddWord(1,"tabno","tabno")

                $ character.RecentActions.append("no suck breasts")
                $ character.DailyActions.append("no suck breasts")

                return
            "Come on, Please?":
                if Approval:
                    $ character.FaceChange("sexy")
                    $ character.Statup("Obed", 90, 1)
                    $ character.Statup("Obed", 50, 2)
                    $ character.Statup("Inbt", 60, 3)
                    $ character.Statup("Inbt", 30, 2)

                    call reward_politeness_dialog(character)
                    call suck_breasts_prep(character)

                    return
                else:
                    $ character.FaceChange("sexy")

                    call please_not_good_enough_dialog(character)
            "[[Start sucking anyway]":                                               # Pressured into licking.
                $ Approval = ApprovalCheck(character, 450, "OI", TabM = 3) # 45, 60, 75, -120(165)

                if Approval > 1 or (Approval and character.Forced):
                    $ character.FaceChange("sad")
                    $ character.Statup("Love", 70, -5, 1)
                    $ character.Statup("Love", 20, -2, 1)

                    call forced_but_not_unwelcome_dialog(character)

                    $ character.Statup("Obed", 90, 2)
                    $ character.Statup("Obed", 50, 4)
                    $ character.Statup("Inbt", 60, 3)

                    if Approval < 2:
                        $ character.Forced = 1

                    call suck_breasts_prep(character)

                    return
                else:
                    $ character.Statup("Love", 200, -10)
                    $ character.FaceChange("angry", 1)

                    "She shoves your head back out."

                    $ character.AddWord(1,"angry","angry")

    if "no suck breasts" in character.DailyActions:
        call learn_to_take_no_dialog(character)

        $ character.AddWord(1,"angry","angry")
    elif character.Forced:
        $ character.FaceChange("angry", 1)

        call went_too_far_dialog(character)

        $ character.Statup("Lust", 60, 5)
        $ character.Statup("Obed", 50, -2)
        $ character.AddWord(1,"angry","angry")
    elif Taboo:
        $ character.FaceChange("angry", 1)
        $ character.AddWord(1,"tabno","tabno")

        call not_in_public_dialog(character)
    elif character.SuckB:
        $ character.FaceChange("sad")

        call you_had_your_shot_dialog(character)
    else:
        $ character.FaceChange("sexy")
        $ character.Mouth = "sad"

        call not_happening_dialog(character)

    $ character.RecentActions.append("no suck breasts")
    $ character.DailyActions.append("no suck breasts")

    $ temp_modifier = 0

    return

label suck_breasts_prep(character):
    if Trigger2 == "suck breasts":
        return

    call breasts_launch(character, "suck breasts")

    if Situation == character:
        $ Situation = 0

        if (character.Over or character.Chest) and not character.Uptop:
            if ApprovalCheck(character, 1250, TabM = 1) or (character.SeenChest and ApprovalCheck(character, 500) and not Taboo):
                $ character.Uptop = 1

                $ Line = character.Over if character.Over else character.Chest

                "With a mischievous grin, [character.Name] pulls her [Line] up over her breasts."

                call first_topless(character, silent = True)

                $ Line = 0

                "She then grabs your head and shoves your face into her chest, clearly intending you to get to work."
            else:
                "[character.Name] grabs your head and shoves your face into her chest, clearly intending you to get to work."
        else:
            "[character.Name] grabs your head and shoves your face into her chest, clearly intending you to get to work."

        menu:
            "What do you do?"
            "Get to work.":
                $ character.Statup("Inbt", 80, 3)
                $ character.Statup("Inbt", 50, 2)

                "You start to run your tongue along her nipple."
            "Praise her.":
                $ character.FaceChange("sexy", 1)
                $ character.Statup("Inbt", 80, 3)

                ch_p "Mmm, I like this, [character.Pet]."

                $ character.NameCheck() #checks reaction to petname

                "You start to run your tongue along her nipple."

                $ character.Statup("Love", 85, 1)
                $ character.Statup("Obed", 90, 1)
                $ character.Statup("Obed", 50, 2)
            "Ask her to stop.":
                "You pull your head back."

                $ character.FaceChange("surprised")
                $ character.Statup("Inbt", 70, 1)

                ch_p "Let's not do that right now, [character.Pet]."

                $ character.NameCheck() #checks reaction to petname

                "[character.Name] pulls away."

                $ character.Statup("Obed", 90, 1)
                $ character.Statup("Obed", 50, 1)
                $ character.Statup("Obed", 30, 2)

                $ Player.RecentActions.append("nope")

                $ character.AddWord(1,"refused","refused")

                return

    if not character.Forced and Situation != "auto":
        $ temp_modifier = 0

        call Top_Off(character)

        if "angry" in character.RecentActions:
            return

    $ temp_modifier = 0

    if not character.SuckB:
        if character.Forced:
            $ character.Statup("Love", 90, -25)
            $ character.Statup("Obed", 70, 25)
            $ character.Statup("Inbt", 80, 17)
        else:
            $ character.Statup("Love", 90, 10)
            $ character.Statup("Obed", 70, 10)
            $ character.Statup("Inbt", 80, 15)

    if Taboo:
        $ character.Inbt += int(Taboo/10)
        $ character.Lust += int(Taboo/5)

    if Situation:
        $ Situation = 0

    $ Line = 0
    $ Cnt = 0

    if Taboo:
        $ character.DrainWord("tabno")

    $ character.DrainWord("no suck breasts")
    $ character.AddWord(0,"suck breasts","suck breasts")

    call breasts_launch(character, "suck breasts")
    call suck_breasts_cycle(character)

    return

label suck_breasts_cycle(character): #Repeating strokes
    if Trigger2 == "kiss you":
        $ Trigger2 = 0

    while Round > 0:
        call ViewShift(character,character.Pose,0,"suck breasts")
        call Shift_Focus(character)

        $ character.LustFace()

        if Player.Focus < 100:
            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":
                    call Slap_Ass(character)

                    $ Cnt += 1
                    $ Round -= 1

                    call suck_breasts_cycle(character)

                    return
                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."

                    $ Player.FocusX = 1
                "Release your focus." if Player.FocusX:
                    "You release your concentration. . ."

                    $ Player.FocusX = 0
                "View":
                    call ViewShift(character,"menu")
                    call suck_breasts_cycle(character)

                    return
                "Other options":
                    menu:
                        "Offhand action":
                                if character.Action and MultiAction:
                                    call Offhand_Set

                                    if Trigger2:
                                        $ character.Action -= 1
                                else:
                                    call tired_dialog(character)
                        "Shift primary action":
                            if character.Action and MultiAction:
                                menu:
                                    "Pull back to fondling.":
                                        if character.Action and MultiAction:
                                            $ Situation = "pullback"

                                            call suck_breasts_after(character)
                                            call expression character.Tag + "_Fondle_Breasts"
                                        else:
                                            "As you pull back, [character.Name] pushes you back in close."

                                            call tired_dialog(character)
                                    "Never Mind":
                                        pass

                                call suck_breasts_cycle(character)

                                return
                            else:
                                call tired_dialog(character)
                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [character.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                    call Les_Change(character)
                                "Ask [character.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                    pass
                                "Ask [Partner.Name] to do something else":
                                    call Three_Change(character)
                                "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                    $ ThreeCount = 0
                                "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                    $ ThreeCount = 0
                                "Swap to [Partner.Name]":
                                    call Trigger_Swap(character)
                                "Undress [Partner.Name]":
                                    call Girl_Undress(Partner)
                                    call suck_breasts_cycle(character)

                                    return
                                "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.Name]" if Partner.Spunk:
                                    call Girl_Cleanup(Partner,"ask")
                                    call suck_breasts_cycle(character)

                                    return
                                "Never mind":
                                    call suck_breasts_cycle(character)

                                    return
                        "Show her feet" if not ShowFeet and (character.Pose == "doggy" or character.Pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (character.Pose == "doggy" or character.Pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [character.Name]":
                            call Girl_Undress(character)
                        "Clean up [character.Name] (locked)" if not character.Spunk:
                            pass
                        "Clean up [character.Name]" if character.Spunk:
                            call Girl_Cleanup(character,"ask")
                        "Never mind":
                            call suck_breasts_cycle(character)

                            return
                "Back to Sex Menu" if MultiAction:
                    ch_p "Let's try something else."

                    call reset_position(character)

                    $ Situation = "shift"
                    $ Line = 0

                    call suck_breasts_after(character)

                    return
                "End Scene" if not MultiAction:
                    ch_p "Let's stop for now."

                    call reset_position(character)

                    $ Line = 0

                    call suck_breasts_after(character)

                    return

        call Shift_Focus(character)
        call Sex_Dialog(character,Partner)

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus

        if Player.Focus >= 100 or character.Lust >= 100:
            if Player.Focus >= 100:
                call Player_Cumming(character)

                if "angry" in character.RecentActions:
                    call reset_position(character)

                    return

                $ character.Statup("Lust", 200, 5)

                if 100 > character.Lust >= 70 and character.OCount < 2:
                    $ character.AddWord(0,"unsatisfied","unsatisfied")

                if Player.Focus > 80:
                    call suck_breasts_after(character)

                    return

                $ Line = "came"

            if character.Lust >= 100:
                call Girl_Cumming(character)

                if Situation == "shift" or "angry" in character.RecentActions:
                    call suck_breasts_after(character)

                    return

            if Line == "came": #ex Player.Focus <= 20:
                $ Line = 0

                if not Player.Semen:
                    "You're emptied out, you should probably take a break."

                if "unsatisfied" in character.RecentActions:#And Rogue is unsatisfied,
                    "[character.Name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."

                            call suck_breasts_after(character)

                            return

        if Partner and Partner.Lust >= 100:
            call Girl_Cumming(Partner)

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if character.SEXP >= 100 or ApprovalCheck(character, 1200, "LO"):
            pass
        elif Cnt == (5 + character.SuckB):
            if character not in [RogueX, KittyX]:
                $ character.Brows = "confused"
            else:
                $ character.Brows = "sly"

            call warm_hands_dialog(character)
        elif character.Lust >= 85:
            pass
        elif Cnt == (15 + character.SuckB) and character.SEXP >= 15 and not ApprovalCheck(character, 1500):
            $ character.Brows = "confused"

            call try_something_else_dialog(character)

            menu:
                extend ""
                "Finish up.":
                    "You let go. . ."

                    call suck_breasts_after(character)

                    return
                "Let's try something else." if MultiAction:
                    $ Line = 0
                    $ Situation = "shift"

                    call suck_breasts_after(character)

                    return
                "No, this is fun.":
                    if ApprovalCheck(character, 1200) or ApprovalCheck(character, 500, "O"):
                        $ character.Statup("Love", 200, -5)
                        $ character.Statup("Obed", 50, 3)
                        $ character.Statup("Obed", 80, 2)

                        "She grumbles but lets you keep going."
                    else:
                        $ character.FaceChange("angry", 1)

                        call reset_position(character)

                        "She scowls at you and pulls back."

                        call this_is_boring_dialog(character)

                        $ character.Statup("Love", 50, -3, 1)
                        $ character.Statup("Love", 80, -4, 1)
                        $ character.Statup("Obed", 30, -1, 1)
                        $ character.Statup("Obed", 50, -1, 1)
                        $ character.AddWord(1,"angry","angry")

                        call suck_breasts_after(character)

                        return

        call Escalation(character) #sees if she wants to escalate things

        if Round == 10:
            call wrap_this_up_dialog(character)
        elif Round == 5:
            call time_to_stop_soon_dialog(character)

        if character.Lust >= 50 and not character.Uptop and (character.Chest or character.Over):
            $ character.Uptop = 1

            if character == RogueX:
                "[character.Name] shrugs and pulls her top open."
            elif character == KittyX:
                "[KittyX.Name] laughs and pulls her top open."
            elif character in [EmmaX, StormX]:
                "[EmmaX.Name] sighs and tugs her breasts free of her clothes."
            elif character in [LauraX, JeanX, JubesX]:
                "[character.Name] grunts and pulls her clothes aside."

            call first_topless(character)

    $ character.FaceChange("bemused", 0)

    $ Line = 0

    call im_done_dialog(character)
    call suck_breasts_after(character)

    return

label suck_breasts_after(character):
    $ character.FaceChange("sexy")
    $ character.SuckB += 1
    $ character.Action -=1
    $ character.Addictionrate += 1

    if "addictive" in Player.Traits:
        $ character.Addictionrate += 1

    call Partner_Like(character,2)

    if character.SuckB == 1:
        $ character.SEXP += 4

        if not Situation:
            if character.Love >= 500 and "unsatisfied" not in character.RecentActions:
                call that_was_nice_dialog(character)
            elif character.Obed <= 500 and Player.Focus <= 20:
                $ character.FaceChange("perplexed", 1)

                call was_that_enough_dialog(character)

    $ temp_modifier = 0

    call Checkout

    if Situation:
        call Sex_Basic_Dialog(character, "switch")
    else:
        call reset_position(character)

    return
