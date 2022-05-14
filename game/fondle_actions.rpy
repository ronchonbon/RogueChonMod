label fondle_menu:
    menu:
        "Keep going. . .":
            pass
        "I want to stick a finger in. . ." if primary_action == "fondle_pussy" and action_speed != 2:
            if focused_Girl.InsertP:
                $ action_speed = 2
            else:
                menu:
                    "Ask her first":
                        $ action_context = "shift"
                    "Don't ask first [[just stick it in]":
                        $ action_context = "auto"

                call finger_pussy(focused_Girl)
        "Pull back a bit. . ." if primary_action == "fondle_pussy" and action_speed != 2:
            $ action_speed = 0
        "Slap her ass":
            call Slap_Ass(focused_Girl)

            $ counter += 1
            $ Round -= 1

            jump action_cycle
        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
            pass
        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
            "You concentrate on not burning out too quickly."

            $ Player.FocusX = 1
        "Release your focus." if Player.FocusX:
            "You release your concentration. . ."

            $ Player.FocusX = 0
        "View":
            call ViewShift(focused_Girl, "menu")
            jump action_cycle
        "Other options":
            menu:
                "Offhand action":
                    if focused_Girl.Action and MultiAction:
                        call Offhand_Set

                        if offhand_action:
                            $ focused_Girl.Action -= 1
                    else:
                        call tired_lines(focused_Girl)
                "Shift primary action":
                    if primary_action == "fondle_thighs":
                        if MultiAction:
                            menu:
                                "Can I go a little deeper?":
                                    if focused_Girl.Action:
                                        $ action_context = "shift"

                                        call after_action
                                        call fondle_pussy(focused_Girl)
                                    else:
                                        call tired_lines(focused_Girl)
                                "Shift your hands a bit higher without asking":
                                    if focused_Girl.Action:
                                        $ action_context = "auto"

                                        call after_action
                                        call fondle_pussy(focused_Girl)
                                    else:
                                        "As your hands creep upwards, she grabs your wrists."

                                        call tired_lines(focused_Girl)
                                "Never Mind":
                                    jump action_cycle
                        else:
                            call tired_lines(focused_Girl)
                    elif primary_action == "fondle_breasts":
                        if focused_Girl.Action and MultiAction:
                            menu:
                                "Ask to suck on them.":
                                    if focused_Girl.Action and MultiAction:
                                        $ action_context = "shift"

                                        call after_action
                                        call suck_breasts(focused_Girl)
                                    else:
                                        call tired_lines(focused_Girl)
                                "Just suck on them without asking.":
                                    if focused_Girl.Action and MultiAction:
                                        $ action_context = "auto"

                                        call after_action
                                        call suck_breasts(focused_Girl)
                                    else:
                                        "As you lean in to suck on her breast, she grabs your head and pushes back."

                                        call tired_lines(focused_Girl)
                                "Never Mind":
                                    jump action_cycle
                        else:
                            call tired_lines(focused_Girl)
                    elif primary_action == "suck_breasts":
                        if MultiAction:
                            menu:
                                "Pull back to fondling.":
                                    if focused_Girl.Action and MultiAction:
                                        $ action_context = "pullback"

                                        call after_action
                                        call fondle_breasts
                                    else:
                                        "As you pull back, [focused_Girl.name] pushes you back in close."

                                        call tired_lines(focused_Girl)
                                "Never Mind":
                                    jump action_cycle
                        else:
                            call tired_lines(focused_Girl)
                    elif primary_action == "fondle_pussy":
                        if MultiAction:
                            menu:
                                "I want to lick your pussy.":
                                    if focused_Girl.Action:
                                        $ action_context = "shift"

                                        call after_action
                                        call eat_pussy(focused_Girl)

                                        return False
                                    else:
                                        call tired_lines(focused_Girl)
                                "Just start licking":
                                    if focused_Girl.Action:
                                        $ action_context = "auto"

                                        call after_action
                                        call eat_pussy(focused_Girl)

                                        return False
                                    else:
                                        "As you lean in to lick her pussy, she grabs your head and pushes back."

                                        call tired_lines(focused_Girl)
                                "Pull back to the thighs":
                                    if focused_Girl.Action:
                                        $ action_context = "pullback"

                                        call after_action
                                        call fondle_thighs(focused_Girl)

                                        return False
                                    else:
                                        "As you pull your hand back, [focused_Girl.name] pulls it back in close."

                                        call tired_lines(focused_Girl)
                                "I want to stick a dildo in.":
                                    if focused_Girl.Action:
                                        $ action_context = "shift"

                                        call after_action
                                        call dildo_pussy(focused_Girl)

                                        return False
                                    else:
                                        call tired_lines(focused_Girl)
                                "Never Mind":
                                    jump action_cycle
                        else:
                            call tired_lines(focused_Girl)
                    elif primary_action == "eat_pussy":
                        if focused_Girl.Action and MultiAction:
                            menu:
                                "Pull out and start rubbing again.":
                                    $ action_context = "pullback"

                                    call after_action
                                    call fondle_pussy(focused_Girl)
                                "I want to stick a dildo in.":
                                    $ action_context = "shift"

                                    call after_action
                                    call dildo_pussy(focused_Girl)
                                "Never Mind":
                                    jump action_cycle
                        else:
                            call tired_lines(focused_Girl)
                    elif primary_action == "fondle_ass":
                        if focused_Girl.Action and MultiAction:
                            menu:
                                "I want to stick a finger in.":
                                    $ action_context = "shift"

                                    call after_action
                                    call finger_ass(focused_Girl)
                                "Just stick a finger in without asking.":
                                    $ action_context = "auto"

                                    call after_action
                                    call finger_ass(focused_Girl)
                                "I want to lick your asshole.":
                                    $ action_context = "shift"

                                    call after_action
                                    call eat_ass(focused_Girl)
                                "Just start licking.":
                                    $ action_context = "auto"

                                    call after_action
                                    call eat_ass(focused_Girl)
                                "I want to stick a dildo in.":
                                    $ action_context = "shift"

                                    call after_action
                                    call dildo_ass(focused_Girl)
                                "Never Mind":
                                    jump action_cycle
                    elif primary_action == "finger_ass":
                        if focused_Girl.Action and MultiAction:
                            menu:
                                "Pull out and start rubbing again.":
                                    $ action_context = "pullback"

                                    call after_action
                                    call fondle_ass(focused_Girl)
                                "I want to lick your asshole.":
                                    $ action_context = "shift"

                                    call after_action
                                    call eat_ass(focused_Girl)
                                "Just start licking.":
                                    $ action_context = "auto"

                                    call after_action
                                    call eat_ass(focused_Girl)
                                "I want to stick a dildo in.":
                                    $ action_context = "shift"

                                    call after_action
                                    call dildo_ass(focused_Girl)
                                "Never Mind":
                                    jump action_cycle
                        else:
                            call tired_lines(focused_Girl)
                    elif primary_action == "eat_ass":
                        if focused_Girl.Action and MultiAction:
                            menu:
                                "Switch to fondling.":
                                    $ action_context = "pullback"

                                    call after_action
                                    call fondle_ass(focused_Girl)
                                "I want to stick a finger in.":
                                    $ action_context = "shift"

                                    call after_action
                                    call finger_ass(focused_Girl)
                                "Just stick a finger in [[without asking].":
                                    $ action_context = "auto"

                                    call after_action
                                    call finger_ass(focused_Girl)
                                "I want to stick a dildo in.":
                                    $ action_context = "shift"

                                    call after_action
                                    call dildo_ass(focused_Girl)
                                "Never Mind":
                                    jump action_cycle
                        else:
                            call tired_lines(focused_Girl)
                "Shift your focus" if offhand_action:
                    $ action_context = "shift focus"

                    call after_action
                    call Offhand_Set
                "Shift your focus (locked)" if not offhand_action:
                    pass
                "Threesome actions (locked)" if not Partner:
                    pass
                "Threesome actions" if Partner:
                    menu:
                        "Ask [focused_Girl.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                            call Les_Change
                        "Ask [focused_Girl.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                            pass
                        "Ask [Partner.name] to do something else":
                            call Three_Change
                        "Don't stop what you're doing. . . (locked)" if not position_change_timer or not Partner_primary_action:
                            $ position_change_timer = 0
                        "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                            $ position_change_timer = 0
                        "Swap to [Partner.name]":
                            call primary_action_Swap
                        "Undress [Partner.name]":
                            call Girl_Undress(Partner)
                            jump action_cycle
                        "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                            pass
                        "Clean up [Partner.name]" if Partner.Spunk:
                            call Girl_Cleanup(Partner,"ask")
                            jump action_cycle
                        "Never mind":
                            jump action_cycle
                "Show her feet" if not ShowFeet and (focused_Girl.Pose == "doggy" or focused_Girl.Pose == "sex"):
                    $ ShowFeet = 1
                "Hide her feet" if ShowFeet and (focused_Girl.Pose == "doggy" or focused_Girl.Pose == "sex"):
                    $ ShowFeet = 0
                "Undress [focused_Girl.name]":
                    call Girl_Undress
                "Clean up [focused_Girl.name] (locked)" if not focused_Girl.Spunk:
                    pass
                "Clean up [focused_Girl.name]" if focused_Girl.Spunk:
                    call Girl_Cleanup(focused_Girl,"ask")
                "Never mind":
                    jump action_cycle
        "Back to Sex Menu" if MultiAction:
            ch_p "Let's try something else."

            call reset_position(Girl)

            $ action_context = "shift"
            $ line = 0

            jump after_action
        "End Scene" if not MultiAction:
            ch_p "Let's stop for now."

            call reset_position(Girl)

            $ line = 0

            jump after_action

    jump fondle_menu_return

label fondle_set_modifier(Girl, action):
    if action == "fondle_thighs":
        if Girl.FondleT:
            $ temp_modifier += 10

        if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 5:
            $ temp_modifier -= 5

        if Girl.lust > 75:
            $ temp_modifier += 10

        if "exhibitionist" in Girl.Traits:
            $ temp_modifier += Taboo

        if Girl in Player.Harem or "sex friend" in Girl.Petnames:
            $ temp_modifier += 10
        elif "ex" in Girl.Traits:
            $ temp_modifier -= 25
    elif action == "fondle_breasts":
        if Girl.FondleB:
            $ temp_modifier += 15

        if Girl.lust > 75: #She's really horny
            $ temp_modifier += 20

        if "exhibitionist" in Girl.Traits:
            $ temp_modifier += (3*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.Petnames:
            $ temp_modifier += 10
        elif "ex" in Girl.Traits:
            $ temp_modifier -= 20
    elif action == "suck_breasts":
        if Girl.SuckB: #You've done it before
            $ temp_modifier += 15

        if not Girl.Chest and not Girl.Over:
            $ temp_modifier += 15

        if Girl.lust > 75: #She's really horny
            $ temp_modifier += 20

        if Girl.lust > 75 and action_context == "auto": #She's really horny
            $ temp_modifier += 10

        if "exhibitionist" in Girl.Traits:
            $ temp_modifier += (4*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.Petnames:
            $ temp_modifier += 10
        elif "ex" in Girl.Traits:
            $ temp_modifier -= 25
    elif action == "fondle_pussy":
        if Girl.FondleP: #You've done it before
            $ temp_modifier += 20

        if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 5: # she's got pants on.
            $ temp_modifier -= 10

        if Girl.lust > 75: #She's really horny
            $ temp_modifier += 15

        if Girl.lust > 75 and action_context == "auto": #She's really horny
            $ temp_modifier += 10

        if "exhibitionist" in Girl.Traits:
            $ temp_modifier += (2*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.Petnames:
            $ temp_modifier += 10
        elif "ex" in Girl.Traits:
            $ temp_modifier -= 25
    elif action == "eat_pussy":
        if Girl.LickP: #You've done it before
            $ temp_modifier += 15

        if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 5: # she's got pants on.
            $ temp_modifier -= 15

        if Girl.lust > 95:
            $ temp_modifier += 20
        elif Girl.lust > 85: #She's really horny
            $ temp_modifier += 15

        if Girl.lust > 85 and action_context == "auto": #She's really horny
            $ temp_modifier += 10

        if action_context == "shift":
            $ temp_modifier += 10

        if "exhibitionist" in Girl.Traits:
            $ temp_modifier += (4*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.Petnames:
            $ temp_modifier += 10
        elif "ex" in Girl.Traits:
            $ temp_modifier -= 25
    elif action == "fondle_ass":
        if Girl.FondleA: #You've done it before
            $ temp_modifier += 10

        if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 5: # she's got pants on.
            $ temp_modifier -= 5

        if Girl.lust > 75: #She's really horny
            $ temp_modifier += 15

        if "exhibitionist" in Girl.Traits:
            $ temp_modifier += Taboo

        if Girl in Player.Harem or "sex friend" in Girl.Petnames:
            $ temp_modifier += 10
        elif "ex" in Girl.Traits:
            $ temp_modifier -= 25
    elif action == "finger_ass":
        if Girl.InsertA: #You've done it before
            $ temp_modifier += 25

        if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 5: # she's got pants on.
            $ temp_modifier -= 15

        if Girl.lust > 85 and Girl.Loose: #She's really horny
            $ temp_modifier += 15

        if Girl.lust > 95 and Girl.Loose:
            $ temp_modifier += 5

        if Girl.lust > 85 and action_context == "auto": #She's really horny
            $ temp_modifier += 10

        if action_context == "shift":
            $ temp_modifier += 10

        if "exhibitionist" in Girl.Traits:
            $ temp_modifier += (4*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.Petnames:
            $ temp_modifier += 10
        elif "ex" in Girl.Traits:
            $ temp_modifier -= 25
    elif action == "eat_ass":
        if Girl.LickA: #You've done it before
            $ temp_modifier += 20

        if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 5: # she's got pants on.
            $ temp_modifier -= 25

        if Girl.lust > 95:
            $ temp_modifier += 20
        elif Girl.lust > 85: #She's really horny
            $ temp_modifier += 15

        if Girl.lust > 85 and action_context == "auto": #auto
            $ temp_modifier += 10

        if action_context == "shift":
            $ temp_modifier += 10

        if "exhibitionist" in Girl.Traits:
            $ temp_modifier += (4*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.Petnames:
            $ temp_modifier += 10
        elif "ex" in Girl.Traits:
            $ temp_modifier -= 25

    if Girl.ForcedCount and not Girl.Forced:
        $ temp_modifier -= 5*Girl.ForcedCount

    if Taboo and "tabno" in Girl.daily_history:
        $ temp_modifier -= 10

    if "no_" + action in Girl.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no_" + action in Girl.recent_history else 0

    return

label end_of_fondle_round(Girl, action):
    $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus

    if Player.Focus >= 100 or Girl.lust >= 100:
        if Player.Focus >= 100:
            call Player_Cumming

            if "angry" in Girl.recent_history:
                call reset_position(Girl)

                return True

            $ Girl.change_stat("lust", 200, 5)

            if 100 > Girl.lust >= 70 and Girl.OCount < 2 and Girl.SEXP >= 20:
                $ Girl.AddWord(0, "unsatisfied", "unsatisfied")

            if Player.Focus > 80:
                jump after_action

            $ line = "came"

        if Girl.lust >= 100:
            call Girl_Cumming

            if action_context == "shift" or "angry" in Girl.recent_history:
                jump after_action

        if line == "came": #ex Player.Focus <= 20:
            $ line = 0

            if not Player.Semen:
                "You're emptied out, you should probably take a break."

            if "unsatisfied" in Girl.recent_history:#And Rogue is unsatisfied,
                "[Girl.name] still seems a bit unsatisfied with the experience."
                menu:
                    "Finish her?"
                    "Yes, keep going for a bit.":
                        $ line = "You get back into it"
                    "No, I'm done.":
                        "You pull back."

                        jump after_action

    if Partner and Partner.lust >= 100:
        call Girl_Cumming(Partner)

    $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

    if action == "fondle_thighs":
        $ bonus = Girl.FondleT
    elif action == "fondle_breasts":
        $ bonus = Girl.FondleB
    elif action == "suck_breasts":
        $ bonus = Girl.SuckB
    elif action == "fondle_pussy":
        $ bonus = Girl.FondleP
    elif action == "finger_pussy":
        $ bonus = Girl.InsertP
    elif action == "eat_pussy":
        $ bonus = Girl.LickP
    elif action == "fondle_ass":
        $ bonus = Girl.FondleA
    elif action == "finger_ass":
        $ bonus = Girl.InsertA
    elif action == "eat_ass":
        $ bonus = Girl.LickA

    if Girl.SEXP >= 100 or ApprovalCheck(Girl, 1200, "LO"):
        pass
    elif counter == (5 + bonus):
        $ Girl.Brows = "confused"

        call warm_hands_lines(Girl)
    elif counter == (15 + bonus) and Girl.SEXP >= 15 and not ApprovalCheck(Girl, 1500):
        $ Girl.Brows = "confused"

        call try_something_else_lines(Girl)

        menu:
            extend ""
            "Finish up.":
                "You let go. . ."

                jump after_action
            "Let's try something else." if MultiAction:
                $ line = 0
                $ action_context = "shift"

                jump after_action
            "No, this is fun.":
                if ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "O"):
                    $ Girl.change_stat("love", 200, -5)
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_stat("obedience", 80, 2)

                    "She grumbles but lets you keep going."
                else:
                    $ Girl.change_face("angry", 1)

                    call reset_position(Girl)

                    "She scowls at you and pulls back."

                    call this_is_boring_lines(Girl)

                    $ Girl.change_stat("love", 50, -3, 1)
                    $ Girl.change_stat("love", 80, -4, 1)
                    $ Girl.change_stat("obedience", 30, -1, 1)
                    $ Girl.change_stat("obedience", 50, -1, 1)
                    $ Girl.AddWord(1,"angry","angry")

                    jump after_action

    call Escalation(Girl)

    if Round == 10:
        call wrap_this_up_lines(Girl)
    elif Round == 5:
        call time_to_stop_soon_lines(Girl)

    return False

label fondle_thighs(Girl):
    $ primary_action = "fondle_thighs"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(Girl)
    call fondle_set_modifier(Girl, "fondle_thighs")

    $ Approval = ApprovalCheck(Girl, 750, TabM=1)

    if action_context == "auto":
        if Approval:
            $ Girl.change_face("sexy")
            $ Girl.change_stat("obedience", 50, 1)
            $ Girl.change_stat("inhibition", 30, 2)

            "As you caress her thigh, [Girl.name] glances at you, and smiles."

            jump before_action
        else:
            $ Girl.change_face("surprised")
            $ Girl.change_stat("obedience", 50, -2)

            call go_back_lines(Girl)

            $ temp_modifier = 0
            $ offhand_action = 0

            return

    if action_context == "pullback":
        $ Girl.change_face("surprised")
        $ Girl.Brows = "sad"

        if Girl.lust > 60:
            $ Girl.change_stat("love", 70, -3)

        $ Girl.change_stat("obedience", 90, 1)
        $ Girl.change_stat("obedience", 70, 2)

        "As you pull back, [Girl.name] looks a little sad."

        jump before_action
    elif "fondle_thighs" in Girl.recent_history:
        $ Girl.change_face("sexy", 1)

        call repeat_action_lines(Girl)
        jump before_action
    elif "fondle_thighs" in Girl.daily_history:
        $ Girl.change_face("sexy", 1)

        call gently_lines(Girl)

    if Approval >= 2:
        call action_accepted(Girl, "fondle_thighs")

        return
    else:
        call action_disapproved(Girl, "fondle_thighs", Girl.FondleT)

    call action_rejected(Girl, "fondle_thighs", Girl.FondleT)

    return

label fondle_breasts(Girl):
    $ primary_action = "fondle_breasts"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(Girl)
    call fondle_set_modifier(Girl, "fondle_breasts")

    $ Approval = ApprovalCheck(Girl, 950, TabM = 3)

    if action_context == "auto":
        if Approval:
            $ Girl.change_face("sexy")
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("obedience", 70, 2)
            $ Girl.change_stat("inhibition", 70, 3)
            $ Girl.change_stat("inhibition", 30, 2)

            "As you cup her breast, [Girl.name] gently nods."

            jump before_action
        else:
            $ Girl.change_face("surprised")
            $ Girl.Brows = "confused"
            $ Girl.change_stat("obedience", 50, -2)

            call go_back_lines(Girl)

            $ temp_modifier = 0
            $ offhand_action = 0

            return

    if Approval:                                                                       #Second time+ dialog
        $ Girl.change_face("sexy", 1)

        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)

        elif not Taboo and "tabno" in Girl.daily_history:
            call private_enough_lines(Girl)

    if "fondle_breasts" in Girl.recent_history:
        $ Girl.change_face("sexy", 1)

        call repeat_action_lines(Girl)
        jump before_action
    elif "fondle_breasts" in Girl.daily_history:
        $ Girl.change_face("sexy", 1)

        call gently_lines(Girl)

    if Approval >= 2:
        call action_accepted(Girl, "fondle_breasts")

        return
    else:
        call action_disapproved(Girl, "fondle_breasts", Girl.FondleB)

    call action_rejected(Girl, "fondle_breasts", Girl.FondleB)

    return

label suck_breasts(Girl):
    $ primary_action = "suck_breasts"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(Girl)
    call fondle_set_modifier(Girl, "suck_breasts")

    $ Approval = ApprovalCheck(Girl, 1050, TabM = 4) # 105, 120, 135, Taboo -160(265)

    if action_context == "auto":                                                                  #You auto-start
        if Approval:
            $ Girl.change_face("sexy")
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("obedience", 70, 2)
            $ Girl.change_stat("inhibition", 70, 3)
            $ Girl.change_stat("inhibition", 30, 2)

            "As you dive in, [Girl.name] seems a bit surprised, but just makes a little \"coo.\""

            jump before_action
        else:
            $ Girl.change_face("surprised")
            $ Girl.change_stat("obedience", 50, -2)

            call go_back_lines(Girl)

            $ temp_modifier = 0
            $ offhand_action = 0

            return

    if "suck_breasts" in Girl.recent_history:
        $ Girl.change_face("sexy", 1)

        call repeat_action_lines(Girl)
        jump before_action
    elif "suck_breasts" in Girl.daily_history:
        $ Girl.change_face("sexy", 1)

        call gently_lines(Girl)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(Girl, "suck_breasts")

        return
    else:
        call action_disapproved(Girl, "suck_breasts", Girl.SuckB)

    call action_rejected(Girl, "suck_breasts", Girl.SuckB)

    return

label fondle_pussy(Girl):
    $ primary_action = "fondle_pussy"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(Girl)
    call fondle_set_modifier(Girl, "fondle_pussy")

    if Girl in [EmmaX, LauraX, JeanX, StormX, JubesX] and Taboo and "public" not in Girl.History:
        $ temp_modifier -= 20

    if "no_fondle_pussy" in Girl.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no_fondle_pussy" in Girl.recent_history else 0

    $ Approval = ApprovalCheck(Girl, 1050, TabM = 2) # 105, 120, 135, Taboo -80(185)

    if action_context == "auto":                                                                  #You auto-start
        if Approval:
            $ Girl.change_face("sexy")
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("obedience", 70, 2)
            $ Girl.change_stat("inhibition", 70, 3)
            $ Girl.change_stat("inhibition", 30, 2)

            "As your hand creeps up her thigh, [Girl.name] seems a bit surprised, but then nods."

            jump before_action
        else:
            $ Girl.change_face("surprised")
            $ Girl.change_stat("obedience", 50, -2)

            call go_back_lines(Girl)

            $ temp_modifier = 0
            $ offhand_action = 0

            return

    if action_context == "pullback":
        $ Girl.change_face("surprised")
        $ Girl.Brows = "sad"

        if Girl.lust > 80:
            $ Girl.change_stat("love", 70, -4)

        $ Girl.change_stat("obedience", 90, 1)
        $ Girl.change_stat("obedience", 70, 2)

        "As your hand pulls out, [Girl.name] gasps and looks upset."

        jump before_action
    elif "fondle_pussy" in Girl.recent_history:
        $ Girl.change_face("sexy", 1)

        call repeat_action_lines(Girl)
        jump before_action
    elif "fondle_pussy" in Girl.daily_history:
        $ Girl.change_face("sexy", 1)

        call gently_lines(Girl)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(Girl, "fondle_pussy")

        return
    else:
        call action_disapproved(Girl, primary_action, Girl.FondleP)

    call action_rejected(Girl, "fondle_pussy", Girl.FondleP)

    return

label finger_pussy(Girl):
    $ primary_action = "finger_pussy"

    call Shift_Focus(Girl)

    if action_context == "auto":                                                                  #You auto-start
        if ApprovalCheck(Girl, 1100, TabM = 2):
            $ Girl.change_face("surprised")
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("obedience", 70, 2)
            $ Girl.change_stat("inhibition", 70, 3)
            $ Girl.change_stat("inhibition", 30, 2)

            "As you slide a finger in, [Girl.name] seems a bit surprised, but seems into it."

            jump before_action
        else:
            $ Girl.change_face("surprised", 2)
            $ Girl.change_stat("love", 80, -2)
            $ Girl.change_stat("obedience", 50, -3)

            Girl.voice "Oooh!"
            "She slaps your hand back."

            $ Girl.change_face("perplexed", 1)

            call go_back_lines(Girl)

            return

    if ApprovalCheck(Girl, 1100, TabM = 2):                           #She's into it. . .
        call action_accepted(Girl, "finger_pussy")

        return
    else:                                                                               #She's not into it, but maybe. . .
        $ Girl.change_face("bemused", 2)

        call not_happening_lines(Girl)

        if Girl in [RogueX, KittyX, EmmaX, StormX]:
            $ Girl.Blush = 1
        else:
            $ Girl.Blush = 0

    return

label eat_pussy(Girl):
    $ primary_action = "eat_pussy"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(Girl)
    call fondle_set_modifier(Girl, "eat_pussy")

    $ Approval = ApprovalCheck(Girl, 1250, TabM = 4) # 125, 140, 155, Taboo -160(285)

    if action_context == "auto":                                                                  #You auto-start
        if Approval:
            $ Girl.change_face("surprised")
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("obedience", 70, 2)
            $ Girl.change_stat("inhibition", 70, 3)
            $ Girl.change_stat("inhibition", 30, 2)

            $ line = renpy.random.choice(["As you crouch down and start to lick her pussy, [Girl.name] startles, but then sinks into the sensation.",
                "As you crouch down and start to lick her pussy, [Girl.name] jumps, but then softens.",
                "As you crouch down and start to lick her pussy, [Girl.name] starts, but then softens."])
            "[line]"

            $ Girl.change_face("sexy")

            jump before_action
        else:
            $ Girl.change_face("surprised")
            $ Girl.change_stat("love", 80, -2)
            $ Girl.change_stat("obedience", 50, -3)

            call go_back_lines(Girl)

            $ Girl.change_face("perplexed",1)

            "She pushes your head back away from her."

            $ temp_modifier = 0
            $ offhand_action = 0

            return

    if "eat_pussy" in Girl.recent_history:
        $ Girl.change_face("sexy", 1)

        call repeat_action_lines(Girl)

        jump before_action
    elif "eat_pussy" in Girl.daily_history:
        $ Girl.change_face("sexy", 1)

        call gently_lines(Girl)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(Girl, "eat_pussy")

        return
    else:
        call action_disapproved(Girl, primary_action, Girl.LickP)

    call action_rejected(Girl, "eat_pussy", Girl.LickP)

label fondle_ass(Girl):
    $ primary_action = "fondle_ass"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(Girl)
    call fondle_set_modifier(Girl, "fondle_ass")

    $ Approval = ApprovalCheck(Girl, 850, TabM=1, Alt = [[StormX], 750]) # 85, 100, 115, Taboo -40(125)

    if action_context == "auto":                                                                  #You auto-start
        if Approval:
            $ Girl.change_face("surprised", 1)
            $ Girl.change_stat("obedience", 70, 2)
            $ Girl.change_stat("inhibition", 40, 2)

            $ line = renpy.random.choice(["As your hand creeps down her backside, [Girl.name] seems a bit surprised, but then nods.",
                "As your hand creeps down her backside, [Girl.name] jumps a bit, and then relaxes.",
                "As your hand creeps down her backside, [Girl.name] shivers a bit, and then relaxes."])
            "[line]"

            $ Girl.change_face("sexy")

            jump before_action
        else:
            $ Girl.change_face("surprised")
            $ Girl.change_stat("obedience", 50, -3)

            call go_back_lines(Girl)

            $ Girl.change_face("bemused")

            $ temp_modifier = 0
            $ offhand_action = 0

            return

    if action_context == "pullback":
        $ Girl.change_face("surprised")
        $ Girl.Brows = "sad"

        if Girl.lust > 80:
            $ Girl.change_stat("love", 70, -4)

        $ Girl.change_stat("obedience", 90, 1)
        $ Girl.change_stat("obedience", 70, 2)

        "As your finger slides out, [Girl.name] gasps and looks upset."

        jump before_action
    elif "fondle_ass" in Girl.recent_history:
        $ Girl.change_face("sexy", 1)

        call repeat_action_lines(Girl)

        jump before_action
    elif "fondle_ass" in Girl.daily_history:
        $ Girl.change_face("sexy", 1)

        call gently_lines(Girl)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(Girl, "fondle_ass")

        return
    else:
        call action_disapproved(Girl, primary_action, Girl.FondleA)

    call action_rejected(Girl, "fondle_ass", Girl.FondleA)

    return

label finger_ass(Girl):
    $ primary_action = "finger_ass"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(Girl)
    call fondle_set_modifier(Girl, "finger_ass")

    $ Approval = ApprovalCheck(Girl, 1300, TabM = 3) # 130, 145, 160, Taboo -120(250)

    if action_context == "auto":                                                                  #You auto-start
        if Approval:
            $ Girl.change_face("surprised")
            $ Girl.change_stat("obedience", 90, 2)
            $ Girl.change_stat("obedience", 70, 2)
            $ Girl.change_stat("inhibition", 80, 2)
            $ Girl.change_stat("inhibition", 30, 2)

            "As you slide a finger in, [Girl.name] tightens around it in surprise, but seems into it."

            $ Girl.change_face("sexy")

            jump before_action
        else:
            $ Girl.change_face("surprised")
            $ Girl.change_stat("love", 80, -2)
            $ Girl.change_stat("obedience", 50, -3)

            call go_back_lines(Girl)

            $ temp_modifier = 0
            $ offhand_action = 0

            return

    if "finger_ass" in Girl.daily_history and not Girl.Loose:
        $ Girl.change_face("bemused", 1)

        call ass_sore_lines(Girl)
    elif "finger_ass" in Girl.daily_history:
        $ Girl.change_face("sexy", 1)

        call gently_lines(Girl)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(Girl, "finger_ass")

        return

    else:
        call action_disapproved(Girl, "finger_ass", Girl.InsertA)

    call action_rejected(Girl, "finger_ass", Girl.InsertA)

    return

label eat_ass(Girl):
    $ primary_action = "eat_ass"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(Girl)
    call fondle_set_modifier(Girl, "eat_ass")

    $ Approval = ApprovalCheck(Girl, 1550, TabM = 4) # 155, 170, 185, Taboo -160(315)

    if action_context == "auto":                                                                  #You auto-start
        if Approval:
            $ Girl.change_face("surprised")
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 80, 3)
            $ Girl.change_stat("inhibition", 40, 2)

            "As you crouch down and start to lick her asshole, [Girl.name] startles briefly, but then begins to melt."

            $ Girl.change_face("sexy")

            jump before_action
        else:
            $ Girl.change_face("surprised")
            $ Girl.change_stat("love", 80, -2)
            $ Girl.change_stat("obedience", 50, -3)

            call go_back_lines(Girl)

            $ temp_modifier = 0
            $ offhand_action = 0

            return

    if "eat_ass" in Girl.recent_history:
        $ Girl.change_face("sexy", 1)

        call repeat_action_lines(Girl)
        jump before_action
    elif "eat_ass" in Girl.daily_history:
        $ Girl.change_face("sexy", 1)

        call gently_lines(Girl)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(Girl, "eat_ass")

        return

    else:                                                                               #She's not into it, but maybe. . .
        call action_disapproved(Girl, "eat_ass", Girl.LickA)

    call action_rejected(Girl, "eat_ass", Girl.LickA)

    return
