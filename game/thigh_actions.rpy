label fondle_thighs(character):
    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(character)

    if character.FondleT:
        $ temp_modifier += 10

    if character.PantsNum() >= 6 or character.HoseNum() >= 5: # she's got pants on.
        $ temp_modifier -= 5

    if character.Lust > 75:
        $ temp_modifier += 10

    if "exhibitionist" in character.Traits:
        $ temp_modifier += Taboo

    if character in Player.Harem or "sex friend" in character.Petnames:
        $ temp_modifier += 10
    elif "ex" in character.Traits:
        $ temp_modifier -= 25

    if character.ForcedCount and not character.Forced:
        $ temp_modifier -= 5*character.ForcedCount

    if Taboo and "tabno" in character.DailyActions:
        $ temp_modifier -= 10

    if "no fondle thighs" in character.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no fondle thighs" in character.RecentActions else 0

    $ Approval = ApprovalCheck(character, 750, TabM=1)

    if Situation == "auto":
        if Approval:
            $ character.FaceChange("sexy")
            $ character.Statup("Obed", 50, 1)
            $ character.Statup("Inbt", 30, 2)

            "As you caress her thigh, [character.Name] glances at you, and smiles."

            call fondle_thighs_prep(character)

            return
        else:
            $ character.FaceChange("surprised")
            $ character.Statup("Obed", 50, -2)

            call go_back_dialog(character)

            $ temp_modifier = 0
            $ Trigger2 = 0

            return

    if Situation == "pullback":
        $ character.FaceChange("surprised")
        $ character.Brows = "sad"

        if character.Lust > 60:
            $ character.Statup("Love", 70, -3)

        $ character.Statup("Obed", 90, 1)
        $ character.Statup("Obed", 70, 2)

        "As you pull back, [character.Name] looks a little sad."

        call fondle_thighs_prep(character)

        return
    elif "fondle thighs" in character.RecentActions:
        $ character.FaceChange("sexy", 1)

        call repeat_action_dialog(character)
        call fondle_thighs_prep(character)

        return
    elif "fondle thighs" in character.DailyActions:
        $ character.FaceChange("sexy", 1)

        call gently_dialog(character)

    if Approval >= 2:
        $ character.FaceChange("bemused", 1)

        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Obed", 90, 1)
            $ character.Statup("Inbt", 60, 1)

        call come_and_get_em_dialog(character)

        $ character.Statup("Love", 90, 1)
        $ character.Statup("Inbt", 50, 3)

        call fondle_thighs_prep(character)

        return
    else:
        $ character.FaceChange("angry", 1)

        if "no fondle thighs" in character.RecentActions:
            call just_told_you_no_dialog(character)
        elif Taboo and "tabno" in character.DailyActions and "no fondle thighs" in character.DailyActions:
            call had_enough_of_this_dialog(character)
        elif "no fondle thighs" in character.DailyActions:
            call already_said_no_dialog(character)
        elif Taboo and "tabno" in character.DailyActions:
            call already_said_not_here_dialog(character)
        elif not character.FondleT:
            $ character.FaceChange("bemused")

            call not_ready_yet_dialog(character)
        else:
            $ character.FaceChange("bemused")

            call rather_not_dialog(character)
        menu:
            extend ""
            "Sorry, never mind." if "no fondle thighs" in character.DailyActions:
                $ character.FaceChange("bemused")

                call no_problem_dialog(character)

                return
            "Maybe later?" if "no fondle thighs" not in character.DailyActions:
                $ character.FaceChange("sexy")

                call maybe_later_dialog(character)

                $ character.Statup("Love", 80, 1)
                $ character.Statup("Inbt", 30, 2)

                if Taboo:
                    $ character.AddWord(1,"tabno","tabno")

                $ character.RecentActions.append("no fondle thighs")
                $ character.DailyActions.append("no fondle thighs")

                return
            "Come on, Please?":
                if Approval:
                    $ character.FaceChange("sexy")
                    $ character.Statup("Obed", 60, 1)
                    $ character.Statup("Obed", 30, 2)
                    $ character.Statup("Inbt", 50, 1)
                    $ character.Statup("Inbt", 30, 2)

                    call reward_politeness_dialog(character)
                    call fondle_thighs_prep(character)

                    return
                else:
                    $ character.FaceChange("sexy")

                    call please_not_good_enough_dialog(character)
            "[[Start caressing her thigh anyway]":
                $ Approval = ApprovalCheck(character, 350, "OI", TabM = 2)

                if Approval > 1 or (Approval and character.Forced):
                    $ character.FaceChange("sad")
                    $ character.Statup("Love", 70, -5, 1)
                    $ character.Statup("Love", 20, -2, 1)

                    call forced_but_not_unwelcome_dialog(character)

                    $ character.Statup("Obed", 50, 3)
                    $ character.Statup("Inbt", 60, 2)

                    if Approval < 2:
                        $ character.Forced = 1

                    call fondle_thighs_prep(character)

                    return
                else:
                    $ character.Statup("Love", 200, -8)
                    $ character.FaceChange("angry", 1)

                    "She slaps your hand away."

                    $ character.AddWord(1,"angry","angry")

    if "no fondle thighs" in character.DailyActions:
        call learn_to_take_no_dialog(character)

        $ character.AddWord(1,"angry","angry")
    elif character.Forced:
        $ character.FaceChange("angry", 1)

        call went_too_far_dialog(character)

        $ character.Statup("Lust", 50, 2)
        $ character.Statup("Obed", 50, -1)
        $ character.AddWord(1,"angry","angry")
    elif Taboo:
        $ character.FaceChange("angry", 1)
        $ character.AddWord(1,"tabno","tabno")

        call not_in_public_dialog(character)
    elif character.FondleT:
        $ character.FaceChange("sad")

        call you_had_your_shot_dialog(character)
    else:
        $ character.FaceChange("sexy")
        $ character.Mouth = "sad"

        call not_happening_dialog(character)

    $ character.RecentActions.append("no fondle thighs")
    $ character.DailyActions.append("no fondle thighs")

    $ temp_modifier = 0

    return

label fondle_thighs_prep(character):
    if Trigger == "kiss you":
        $ Trigger = "fondle thighs"

        return

    if Trigger2 == "fondle thighs":
        return

    call pussy_launch(character, trigger = "fondle thighs")

    if not character.Forced and Situation != "auto":
        $ temp_modifier = 0

        call Bottoms_Off(character)

        if "angry" in character.RecentActions:
            return

    $ temp_modifier = 0

    if not character.FondleT:
        if character.Forced:
            $ character.Statup("Love", 90, -10)
            $ character.Statup("Obed", 70, 15)
            $ character.Statup("Inbt", 80, 10)
        else:
            $ character.Statup("Love", 90, 5)
            $ character.Statup("Obed", 70, 10)
            $ character.Statup("Inbt", 80, 15)

    if Taboo:
        $ character.Statup("Lust", 200, (int(Taboo/5)))
        $ character.Statup("Inbt", 200, (2*(int(Taboo/5))))

    if Situation:
        $ Situation = 0

    $ Line = 0
    $ Cnt = 0

    if Taboo:
        $ character.DrainWord("tabno")

    $ character.DrainWord("no fondle thighs")
    $ character.AddWord(0,"fondle thighs","fondle thighs")

    call pussy_launch(character, trigger = "fondle thighs")
    call fondle_thighs_cycle(character)

    return

label fondle_thighs_cycle(character):
    while Round > 0:
        call ViewShift(character,character.Pose,0,"fondle thighs")
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

                    call fondle_thighs_cycle(character)

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
                    call fondle_thighs_cycle(character)

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
                                        "Can I go a little deeper?":
                                            if character.Action and MultiAction:
                                                $ Situation = "shift"

                                                call fondle_thighs_after(character)
                                                call expression character.Tag + "_Fondle_Pussy"
                                            else:
                                                call tired_dialog(character)
                                        "Shift your hands a bit higher without asking":
                                            if character.Action and MultiAction:
                                                $ Situation = "auto"

                                                call fondle_thighs_after(character)
                                                call expression character.Tag + "_Fondle_Pussy"
                                            else:
                                                "As your hands creep upwards, she grabs your wrists."

                                                call tired_dialog(character)
                                        "Never Mind":
                                            pass

                                    call fondle_thighs_cycle(character)

                                    return
                                else:
                                    call tired_dialog(character)
                        "Shift your focus" if Trigger2:
                            $ Situation = "shift focus"

                            call fondle_thighs_after(character)
                            call Offhand_Set

                            return
                        "Shift your focus (locked)" if not Trigger2:
                            pass
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
                                    call fondle_thighs_cycle(character)

                                    return
                                "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.Name]" if Partner.Spunk:
                                    call Girl_Cleanup(Partner,"ask")
                                    call fondle_thighs_cycle(character)

                                    return
                                "Never mind":
                                    call fondle_thighs_cycle(character)

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
                            call fondle_thighs_cycle(character)

                            return
                "Back to Sex Menu" if MultiAction:
                    ch_p "Let's try something else."

                    call reset_position(character)

                    $ Situation = "shift"
                    $ Line = 0

                    call fondle_thighs_after(character)

                    return
                "End Scene" if not MultiAction:
                    ch_p "Let's stop for now."

                    call reset_position(character)

                    $ Line = 0

                    call fondle_thighs_after(character)

                    return

        call Shift_Focus(character)
        call Sex_Dialog(character, Partner)

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up

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
                    call fondle_thighs_after(character)

                    return

                $ Line = "came"

            if character.Lust >= 100:
                call Girl_Cumming(character)

                if Situation == "shift" or "angry" in character.RecentActions:
                    call fondle_thighs_after(character)

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

                            call fondle_thighs_after(character)

                            return

        if Partner and Partner.Lust >= 100:
            call Girl_Cumming(Partner)

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if character.SEXP >= 100 or ApprovalCheck(character, 1200, "LO"):
            pass
        elif Cnt == (5 + character.FondleT):
            $ character.Brows = "confused"

            call warm_hands_dialog(character)
        elif Cnt == (15 + character.FondleT) and character.SEXP >= 15 and not ApprovalCheck(character, 1500):
            $ character.Brows = "confused"

            call try_something_else_dialog(character)

            menu:
                extend ""
                "Finish up.":
                    "You let go. . ."

                    call fondle_thighs_after(character)

                    return
                "Let's try something else." if MultiAction:
                    $ Line = 0
                    $ Situation = "shift"

                    call fondle_thighs_after(character)

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

                        call fondle_thighs_after(character)

                        return

        call Escalation(character)

        if Round == 10:
            call wrap_this_up_dialog(character)
        elif Round == 5:
            call time_to_stop_soon_dialog(character)

    $ character.FaceChange("bemused", 0)

    $ Line = 0

    call im_done_dialog(character)
    call fondle_thighs_after(character)

    return

label fondle_thighs_after(character):
    $ character.FaceChange("sexy")
    $ character.FondleT += 1
    $ character.Action -=1

    if character.PantsNum() < 6 or character.Upskirt:
        $ character.Addictionrate += 1

        if "addictive" in Player.Traits:
            $ character.Addictionrate += 1

        call Partner_Like(character,1,0)

    if character.FondleT == 1:
        $ character.SEXP += 3

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
