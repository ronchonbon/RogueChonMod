label fondle_menu:
    menu:
        "Keep going. . .":
            pass
        "I want to stick a finger in. . ." if Player.primary_action == "fondle_pussy" and Speed != 2:
            if Player.focused_girl.InsertP:
                $ Speed = 2
            else:
                menu:
                    "Ask her first":
                        $ Situation = "shift"
                    "Don't ask first [[just stick it in]":
                        $ Situation = "auto"

                call finger_pussy(Player.focused_girl)
        "Pull back a bit. . ." if Player.primary_action == "fondle_pussy" and Speed != 2:
            $ Speed = 0
        "Slap her ass":
            call Slap_Ass(Player.focused_girl)

            $ Cnt += 1
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
            call ViewShift(Player.focused_girl, "menu")
            jump action_cycle
        "Other options":
            menu:
                "Offhand action":
                    if Player.focused_girl.Action and MultiAction:
                        call Offhand_Set

                        if Trigger2:
                            $ Player.focused_girl.Action -= 1
                    else:
                        call tired_lines(Player.focused_girl)
                "Shift primary action":
                    if Player.primary_action == "fondle_thighs":
                        if MultiAction:
                            menu:
                                "Can I go a little deeper?":
                                    if Player.focused_girl.Action:
                                        $ Situation = "shift"

                                        call after_action
                                        call fondle_pussy(Player.focused_girl)
                                    else:
                                        call tired_lines(Player.focused_girl)
                                "Shift your hands a bit higher without asking":
                                    if Player.focused_girl.Action:
                                        $ Situation = "auto"

                                        call after_action
                                        call fondle_pussy(Player.focused_girl)
                                    else:
                                        "As your hands creep upwards, she grabs your wrists."

                                        call tired_lines(Player.focused_girl)
                                "Never Mind":
                                    jump action_cycle
                        else:
                            call tired_lines(Player.focused_girl)
                    elif Player.primary_action == "fondle_breasts":
                        if Player.focused_girl.Action and MultiAction:
                            menu:
                                "Ask to suck on them.":
                                    if Player.focused_girl.Action and MultiAction:
                                        $ Situation = "shift"

                                        call after_action
                                        call suck_breasts(Player.focused_girl)
                                    else:
                                        call tired_lines(Player.focused_girl)
                                "Just suck on them without asking.":
                                    if Player.focused_girl.Action and MultiAction:
                                        $ Situation = "auto"

                                        call after_action
                                        call suck_breasts(Player.focused_girl)
                                    else:
                                        "As you lean in to suck on her breast, she grabs your head and pushes back."

                                        call tired_lines(Player.focused_girl)
                                "Never Mind":
                                    jump action_cycle
                        else:
                            call tired_lines(Player.focused_girl)
                    elif Player.primary_action == "suck_breasts":
                        if MultiAction:
                            menu:
                                "Pull back to fondling.":
                                    if Player.focused_girl.Action and MultiAction:
                                        $ Situation = "pullback"

                                        call after_action
                                        call fondle_breasts
                                    else:
                                        "As you pull back, [Player.focused_girl.Name] pushes you back in close."

                                        call tired_lines(Player.focused_girl)
                                "Never Mind":
                                    jump action_cycle
                        else:
                            call tired_lines(Player.focused_girl)
                    elif Player.primary_action == "fondle_pussy":
                        if MultiAction:
                            menu:
                                "I want to lick your pussy.":
                                    if Player.focused_girl.Action:
                                        $ Situation = "shift"

                                        call after_action
                                        call eat_pussy(Player.focused_girl)

                                        return False
                                    else:
                                        call tired_lines(Player.focused_girl)
                                "Just start licking":
                                    if Player.focused_girl.Action:
                                        $ Situation = "auto"

                                        call after_action
                                        call eat_pussy(Player.focused_girl)

                                        return False
                                    else:
                                        "As you lean in to lick her pussy, she grabs your head and pushes back."

                                        call tired_lines(Player.focused_girl)
                                "Pull back to the thighs":
                                    if Player.focused_girl.Action:
                                        $ Situation = "pullback"

                                        call after_action
                                        call fondle_thighs(Player.focused_girl)

                                        return False
                                    else:
                                        "As you pull your hand back, [Player.focused_girl.Name] pulls it back in close."

                                        call tired_lines(Player.focused_girl)
                                "I want to stick a dildo in.":
                                    if Player.focused_girl.Action:
                                        $ Situation = "shift"

                                        call after_action
                                        call dildo_pussy(Player.focused_girl)

                                        return False
                                    else:
                                        call tired_lines(Player.focused_girl)
                                "Never Mind":
                                    jump action_cycle
                        else:
                            call tired_lines(Player.focused_girl)
                    elif Player.primary_action == "eat_pussy":
                        if Player.focused_girl.Action and MultiAction:
                            menu:
                                "Pull out and start rubbing again.":
                                    $ Situation = "pullback"

                                    call after_action
                                    call fondle_pussy(Player.focused_girl)
                                "I want to stick a dildo in.":
                                    $ Situation = "shift"

                                    call after_action
                                    call dildo_pussy(Player.focused_girl)
                                "Never Mind":
                                    jump action_cycle
                        else:
                            call tired_lines(Player.focused_girl)
                    elif Player.primary_action == "fondle_ass":
                        if Player.focused_girl.Action and MultiAction:
                            menu:
                                "I want to stick a finger in.":
                                    $ Situation = "shift"

                                    call after_action
                                    call finger_ass(Player.focused_girl)
                                "Just stick a finger in without asking.":
                                    $ Situation = "auto"

                                    call after_action
                                    call finger_ass(Player.focused_girl)
                                "I want to lick your asshole.":
                                    $ Situation = "shift"

                                    call after_action
                                    call eat_ass(Player.focused_girl)
                                "Just start licking.":
                                    $ Situation = "auto"

                                    call after_action
                                    call eat_ass(Player.focused_girl)
                                "I want to stick a dildo in.":
                                    $ Situation = "shift"

                                    call after_action
                                    call dildo_ass(Player.focused_girl)
                                "Never Mind":
                                    jump action_cycle
                    elif Player.primary_action == "finger_ass":
                        if Player.focused_girl.Action and MultiAction:
                            menu:
                                "Pull out and start rubbing again.":
                                    $ Situation = "pullback"

                                    call after_action
                                    call fondle_ass(Player.focused_girl)
                                "I want to lick your asshole.":
                                    $ Situation = "shift"

                                    call after_action
                                    call eat_ass(Player.focused_girl)
                                "Just start licking.":
                                    $ Situation = "auto"

                                    call after_action
                                    call eat_ass(Player.focused_girl)
                                "I want to stick a dildo in.":
                                    $ Situation = "shift"

                                    call after_action
                                    call dildo_ass(Player.focused_girl)
                                "Never Mind":
                                    jump action_cycle
                        else:
                            call tired_lines(Player.focused_girl)
                    elif Player.primary_action == "eat_ass":
                        if Player.focused_girl.Action and MultiAction:
                            menu:
                                "Switch to fondling.":
                                    $ Situation = "pullback"

                                    call after_action
                                    call fondle_ass(Player.focused_girl)
                                "I want to stick a finger in.":
                                    $ Situation = "shift"

                                    call after_action
                                    call finger_ass(Player.focused_girl)
                                "Just stick a finger in [[without asking].":
                                    $ Situation = "auto"

                                    call after_action
                                    call finger_ass(Player.focused_girl)
                                "I want to stick a dildo in.":
                                    $ Situation = "shift"

                                    call after_action
                                    call dildo_ass(Player.focused_girl)
                                "Never Mind":
                                    jump action_cycle
                        else:
                            call tired_lines(Player.focused_girl)
                "Shift your focus" if Trigger2:
                    $ Situation = "shift focus"

                    call after_action
                    call Offhand_Set
                "Shift your focus (locked)" if not Trigger2:
                    pass
                "Threesome actions (locked)" if not Partner:
                    pass
                "Threesome actions" if Partner:
                    menu:
                        "Ask [Player.focused_girl.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                            call Les_Change
                        "Ask [Player.focused_girl.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                            pass
                        "Ask [Partner.Name] to do something else":
                            call Three_Change
                        "Don't stop what you're doing. . . (locked)" if not ThreeCount or not Trigger4:
                            $ ThreeCount = 0
                        "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                            $ ThreeCount = 0
                        "Swap to [Partner.Name]":
                            call Trigger_Swap
                        "Undress [Partner.Name]":
                            call Girl_Undress(Partner)
                            jump action_cycle
                        "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                            pass
                        "Clean up [Partner.Name]" if Partner.Spunk:
                            call Girl_Cleanup(Partner,"ask")
                            jump action_cycle
                        "Never mind":
                            jump action_cycle
                "Show her feet" if not ShowFeet and (Player.focused_girl.Pose == "doggy" or Player.focused_girl.Pose == "sex"):
                    $ ShowFeet = 1
                "Hide her feet" if ShowFeet and (Player.focused_girl.Pose == "doggy" or Player.focused_girl.Pose == "sex"):
                    $ ShowFeet = 0
                "Undress [Player.focused_girl.Name]":
                    call Girl_Undress
                "Clean up [Player.focused_girl.Name] (locked)" if not Player.focused_girl.Spunk:
                    pass
                "Clean up [Player.focused_girl.Name]" if Player.focused_girl.Spunk:
                    call Girl_Cleanup(Player.focused_girl,"ask")
                "Never mind":
                    jump action_cycle
        "Back to Sex Menu" if MultiAction:
            ch_p "Let's try something else."

            call reset_position(character)

            $ Situation = "shift"
            $ Line = 0

            jump after_action
        "End Scene" if not MultiAction:
            ch_p "Let's stop for now."

            call reset_position(character)

            $ Line = 0

            jump after_action

    jump fondle_menu_return

label fondle_set_modifier(character, action):
    if action == "fondle_thighs":
        if character.FondleT:
            $ temp_modifier += 10

        if character.PantsNum() >= 6 or character.HoseNum() >= 5:
            $ temp_modifier -= 5

        if character.Lust > 75:
            $ temp_modifier += 10

        if "exhibitionist" in character.Traits:
            $ temp_modifier += Taboo

        if character in Player.Harem or "sex friend" in character.Petnames:
            $ temp_modifier += 10
        elif "ex" in character.Traits:
            $ temp_modifier -= 25
    elif action == "fondle_breasts":
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
    elif action == "suck_breasts":
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
    elif action == "fondle_pussy":
        if character.FondleP: #You've done it before
            $ temp_modifier += 20

        if character.PantsNum() >= 6 or character.HoseNum() >= 5: # she's got pants on.
            $ temp_modifier -= 10

        if character.Lust > 75: #She's really horny
            $ temp_modifier += 15

        if character.Lust > 75 and Situation == "auto": #She's really horny
            $ temp_modifier += 10

        if "exhibitionist" in character.Traits:
            $ temp_modifier += (2*Taboo)

        if character in Player.Harem or "sex friend" in character.Petnames:
            $ temp_modifier += 10
        elif "ex" in character.Traits:
            $ temp_modifier -= 25
    elif action == "eat_pussy":
        if character.LickP: #You've done it before
            $ temp_modifier += 15

        if character.PantsNum() >= 6 or character.HoseNum() >= 5: # she's got pants on.
            $ temp_modifier -= 15

        if character.Lust > 95:
            $ temp_modifier += 20
        elif character.Lust > 85: #She's really horny
            $ temp_modifier += 15

        if character.Lust > 85 and Situation == "auto": #She's really horny
            $ temp_modifier += 10

        if Situation == "shift":
            $ temp_modifier += 10

        if "exhibitionist" in character.Traits:
            $ temp_modifier += (4*Taboo)

        if character in Player.Harem or "sex friend" in character.Petnames:
            $ temp_modifier += 10
        elif "ex" in character.Traits:
            $ temp_modifier -= 25
    elif action == "fondle_ass":
        if character.FondleA: #You've done it before
            $ temp_modifier += 10

        if character.PantsNum() >= 6 or character.HoseNum() >= 5: # she's got pants on.
            $ temp_modifier -= 5

        if character.Lust > 75: #She's really horny
            $ temp_modifier += 15

        if "exhibitionist" in character.Traits:
            $ temp_modifier += Taboo

        if character in Player.Harem or "sex friend" in character.Petnames:
            $ temp_modifier += 10
        elif "ex" in character.Traits:
            $ temp_modifier -= 25
    elif action == "finger_ass":
        if character.InsertA: #You've done it before
            $ temp_modifier += 25

        if character.PantsNum() >= 6 or character.HoseNum() >= 5: # she's got pants on.
            $ temp_modifier -= 15

        if character.Lust > 85 and character.Loose: #She's really horny
            $ temp_modifier += 15

        if character.Lust > 95 and character.Loose:
            $ temp_modifier += 5

        if character.Lust > 85 and Situation == "auto": #She's really horny
            $ temp_modifier += 10

        if Situation == "shift":
            $ temp_modifier += 10

        if "exhibitionist" in character.Traits:
            $ temp_modifier += (4*Taboo)

        if character in Player.Harem or "sex friend" in character.Petnames:
            $ temp_modifier += 10
        elif "ex" in character.Traits:
            $ temp_modifier -= 25
    elif action == "eat_ass":
        if character.LickA: #You've done it before
            $ temp_modifier += 20

        if character.PantsNum() >= 6 or character.HoseNum() >= 5: # she's got pants on.
            $ temp_modifier -= 25

        if character.Lust > 95:
            $ temp_modifier += 20
        elif character.Lust > 85: #She's really horny
            $ temp_modifier += 15

        if character.Lust > 85 and Situation == "auto": #auto
            $ temp_modifier += 10

        if Situation == "shift":
            $ temp_modifier += 10

        if "exhibitionist" in character.Traits:
            $ temp_modifier += (4*Taboo)

        if character in Player.Harem or "sex friend" in character.Petnames:
            $ temp_modifier += 10
        elif "ex" in character.Traits:
            $ temp_modifier -= 25

    if character.ForcedCount and not character.Forced:
        $ temp_modifier -= 5*character.ForcedCount

    if Taboo and "tabno" in character.DailyActions:
        $ temp_modifier -= 10

    if "no_" + action in character.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no_" + action in character.RecentActions else 0

    return

label end_of_fondle_round(character, action):
    $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus

    if Player.Focus >= 100 or character.Lust >= 100:
        if Player.Focus >= 100:
            call Player_Cumming

            if "angry" in character.RecentActions:
                call reset_position(character)

                return True

            $ character.Statup("Lust", 200, 5)

            if 100 > character.Lust >= 70 and character.OCount < 2 and character.SEXP >= 20:
                $ character.AddWord(0, "unsatisfied", "unsatisfied")

            if Player.Focus > 80:
                jump after_action

            $ Line = "came"

        if character.Lust >= 100:
            call Girl_Cumming

            if Situation == "shift" or "angry" in character.RecentActions:
                jump after_action

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

                        jump after_action

    if Partner and Partner.Lust >= 100:
        call Girl_Cumming(Partner)

    $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

    if action == "fondle_thighs":
        $ bonus = character.FondleT
    elif action == "fondle_breasts":
        $ bonus = character.FondleB
    elif action == "suck_breasts":
        $ bonus = character.SuckB
    elif action == "fondle_pussy":
        $ bonus = character.FondleP
    elif action == "finger_pussy":
        $ bonus = character.InsertP
    elif action == "eat_pussy":
        $ bonus = character.LickP
    elif action == "fondle_ass":
        $ bonus = character.FondleA
    elif action == "finger_ass":
        $ bonus = character.InsertA
    elif action == "eat_ass":
        $ bonus = character.LickA

    if character.SEXP >= 100 or ApprovalCheck(character, 1200, "LO"):
        pass
    elif Cnt == (5 + bonus):
        $ character.Brows = "confused"

        call warm_hands_lines(character)
    elif Cnt == (15 + bonus) and character.SEXP >= 15 and not ApprovalCheck(character, 1500):
        $ character.Brows = "confused"

        call try_something_else_lines(character)

        menu:
            extend ""
            "Finish up.":
                "You let go. . ."

                jump after_action
            "Let's try something else." if MultiAction:
                $ Line = 0
                $ Situation = "shift"

                jump after_action
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

                    call this_is_boring_lines(character)

                    $ character.Statup("Love", 50, -3, 1)
                    $ character.Statup("Love", 80, -4, 1)
                    $ character.Statup("Obed", 30, -1, 1)
                    $ character.Statup("Obed", 50, -1, 1)
                    $ character.AddWord(1,"angry","angry")

                    jump after_action

    call Escalation(character)

    if Round == 10:
        call wrap_this_up_lines(character)
    elif Round == 5:
        call time_to_stop_soon_lines(character)

    return False

label fondle_thighs(character):
    $ Player.primary_action = "fondle_thighs"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(character)
    call fondle_set_modifier(character, "fondle_thighs")

    $ Approval = ApprovalCheck(character, 750, TabM=1)

    if Situation == "auto":
        if Approval:
            $ character.FaceChange("sexy")
            $ character.Statup("Obed", 50, 1)
            $ character.Statup("Inbt", 30, 2)

            "As you caress her thigh, [character.Name] glances at you, and smiles."

            jump before_action
        else:
            $ character.FaceChange("surprised")
            $ character.Statup("Obed", 50, -2)

            call go_back_lines(character)

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

        jump before_action
    elif "fondle_thighs" in character.RecentActions:
        $ character.FaceChange("sexy", 1)

        call repeat_action_lines(character)
        jump before_action
    elif "fondle_thighs" in character.DailyActions:
        $ character.FaceChange("sexy", 1)

        call gently_lines(character)

    if Approval >= 2:
        call action_accepted(character, "fondle_thighs")

        return
    else:
        call action_disapproved(character, "fondle_thighs", character.FondleT)

    call action_rejected(character, "fondle_thighs", character.FondleT)

    return

label fondle_breasts(character):
    $ Player.primary_action = "fondle_breasts"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(character)
    call fondle_set_modifier(character, "fondle_breasts")

    $ Approval = ApprovalCheck(character, 950, TabM = 3)

    if Situation == "auto":
        if Approval:
            $ character.FaceChange("sexy")
            $ character.Statup("Obed", 90, 1)
            $ character.Statup("Obed", 70, 2)
            $ character.Statup("Inbt", 70, 3)
            $ character.Statup("Inbt", 30, 2)

            "As you cup her breast, [character.Name] gently nods."

            jump before_action
        else:
            $ character.FaceChange("surprised")
            $ character.Brows = "confused"
            $ character.Statup("Obed", 50, -2)

            call go_back_lines(character)

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
            call private_enough_lines(character)

    if "fondle_breasts" in character.RecentActions:
        $ character.FaceChange("sexy", 1)

        call repeat_action_lines(character)
        jump before_action
    elif "fondle_breasts" in character.DailyActions:
        $ character.FaceChange("sexy", 1)

        call gently_lines(character)

    if Approval >= 2:
        call action_accepted(character, "fondle_breasts")

        return
    else:
        call action_disapproved(character, "fondle_breasts", character.FondleB)

    call action_rejected(character, "fondle_breasts", character.FondleB)

    return

label suck_breasts(character):
    $ Player.primary_action = "suck_breasts"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(character)
    call fondle_set_modifier(character, "suck_breasts")

    $ Approval = ApprovalCheck(character, 1050, TabM = 4) # 105, 120, 135, Taboo -160(265)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ character.FaceChange("sexy")
            $ character.Statup("Obed", 90, 1)
            $ character.Statup("Obed", 70, 2)
            $ character.Statup("Inbt", 70, 3)
            $ character.Statup("Inbt", 30, 2)

            "As you dive in, [character.Name] seems a bit surprised, but just makes a little \"coo.\""

            jump before_action
        else:
            $ character.FaceChange("surprised")
            $ character.Statup("Obed", 50, -2)

            call go_back_lines(character)

            $ temp_modifier = 0
            $ Trigger2 = 0

            return

    if "suck_breasts" in character.RecentActions:
        $ character.FaceChange("sexy", 1)

        call repeat_action_lines(character)
        jump before_action
    elif "suck_breasts" in character.DailyActions:
        $ character.FaceChange("sexy", 1)

        call gently_lines(character)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(character, "suck_breasts")

        return
    else:
        call action_disapproved(character, "suck_breasts", character.SuckB)

    call action_rejected(character, "suck_breasts", character.SuckB)

    return

label fondle_pussy(character):
    $ Player.primary_action = "fondle_pussy"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(character)
    call fondle_set_modifier(character, "fondle_pussy")

    if character in [EmmaX, LauraX, JeanX, StormX, JubesX] and Taboo and "public" not in character.History:
        $ temp_modifier -= 20

    if "no_fondle_pussy" in character.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no_fondle_pussy" in character.RecentActions else 0

    $ Approval = ApprovalCheck(character, 1050, TabM = 2) # 105, 120, 135, Taboo -80(185)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ character.FaceChange("sexy")
            $ character.Statup("Obed", 90, 1)
            $ character.Statup("Obed", 70, 2)
            $ character.Statup("Inbt", 70, 3)
            $ character.Statup("Inbt", 30, 2)

            "As your hand creeps up her thigh, [character.Name] seems a bit surprised, but then nods."

            jump before_action
        else:
            $ character.FaceChange("surprised")
            $ character.Statup("Obed", 50, -2)

            call go_back_lines(character)

            $ temp_modifier = 0
            $ Trigger2 = 0

            return

    if Situation == "pullback":
        $ character.FaceChange("surprised")
        $ character.Brows = "sad"

        if character.Lust > 80:
            $ character.Statup("Love", 70, -4)

        $ character.Statup("Obed", 90, 1)
        $ character.Statup("Obed", 70, 2)

        "As your hand pulls out, [character.Name] gasps and looks upset."

        jump before_action
    elif "fondle_pussy" in character.RecentActions:
        $ character.FaceChange("sexy", 1)

        call repeat_action_lines(character)
        jump before_action
    elif "fondle_pussy" in character.DailyActions:
        $ character.FaceChange("sexy", 1)

        call gently_lines(character)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(character, "fondle_pussy")

        return
    else:
        call action_disapproved(character, Player.primary_action, character.FondleP)

    call action_rejected(character, "fondle_pussy", character.FondleP)

    return

label finger_pussy(character):
    $ Player.primary_action = "finger_pussy"

    call Shift_Focus(character)

    if Situation == "auto":                                                                  #You auto-start
        if ApprovalCheck(character, 1100, TabM = 2):
            $ character.FaceChange("surprised")
            $ character.Statup("Obed", 90, 1)
            $ character.Statup("Obed", 70, 2)
            $ character.Statup("Inbt", 70, 3)
            $ character.Statup("Inbt", 30, 2)

            "As you slide a finger in, [character.Name] seems a bit surprised, but seems into it."

            jump before_action
        else:
            $ character.FaceChange("surprised", 2)
            $ character.Statup("Love", 80, -2)
            $ character.Statup("Obed", 50, -3)

            character.voice "Oooh!"
            "She slaps your hand back."

            $ character.FaceChange("perplexed", 1)

            call go_back_lines(character)

            return

    if ApprovalCheck(character, 1100, TabM = 2):                           #She's into it. . .
        call action_accepted(character, "finger_pussy")

        return
    else:                                                                               #She's not into it, but maybe. . .
        $ character.FaceChange("bemused", 2)

        call not_happening_lines(character)

        if character in [RogueX, KittyX, EmmaX, StormX]:
            $ character.Blush = 1
        else:
            $ character.Blush = 0

    return

label eat_pussy(character):
    $ Player.primary_action = "eat_pussy"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(character)
    call fondle_set_modifier(character, "eat_pussy")

    $ Approval = ApprovalCheck(character, 1250, TabM = 4) # 125, 140, 155, Taboo -160(285)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ character.FaceChange("surprised")
            $ character.Statup("Obed", 90, 1)
            $ character.Statup("Obed", 70, 2)
            $ character.Statup("Inbt", 70, 3)
            $ character.Statup("Inbt", 30, 2)

            $ line = renpy.random.choice(["As you crouch down and start to lick her pussy, [character.Name] startles, but then sinks into the sensation.",
                "As you crouch down and start to lick her pussy, [character.Name] jumps, but then softens.",
                "As you crouch down and start to lick her pussy, [character.Name] starts, but then softens."])
            "[line]"

            $ character.FaceChange("sexy")

            jump before_action
        else:
            $ character.FaceChange("surprised")
            $ character.Statup("Love", 80, -2)
            $ character.Statup("Obed", 50, -3)

            call go_back_lines(character)

            $ character.FaceChange("perplexed",1)

            "She pushes your head back away from her."

            $ temp_modifier = 0
            $ Trigger2 = 0

            return

    if "eat_pussy" in character.RecentActions:
        $ character.FaceChange("sexy", 1)

        call repeat_action_lines(character)

        jump before_action
    elif "eat_pussy" in character.DailyActions:
        $ character.FaceChange("sexy", 1)

        call gently_lines(character)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(character, "eat_pussy")

        return
    else:
        call action_disapproved(character, Player.primary_action, character.LickP)

    call action_rejected(character, "eat_pussy", character.LickP)

label fondle_ass(character):
    $ Player.primary_action = "fondle_ass"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(character)
    call fondle_set_modifier(character, "fondle_ass")

    $ Approval = ApprovalCheck(character, 850, TabM=1, Alt = [[StormX], 750]) # 85, 100, 115, Taboo -40(125)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ character.FaceChange("surprised", 1)
            $ character.Statup("Obed", 70, 2)
            $ character.Statup("Inbt", 40, 2)

            $ line = renpy.random.choice(["As your hand creeps down her backside, [character.Name] seems a bit surprised, but then nods.",
                "As your hand creeps down her backside, [character.Name] jumps a bit, and then relaxes.",
                "As your hand creeps down her backside, [character.Name] shivers a bit, and then relaxes."])
            "[line]"

            $ character.FaceChange("sexy")

            jump before_action
        else:
            $ character.FaceChange("surprised")
            $ character.Statup("Obed", 50, -3)

            call go_back_lines(character)

            $ character.FaceChange("bemused")

            $ temp_modifier = 0
            $ Trigger2 = 0

            return

    if Situation == "pullback":
        $ character.FaceChange("surprised")
        $ character.Brows = "sad"

        if character.Lust > 80:
            $ character.Statup("Love", 70, -4)

        $ character.Statup("Obed", 90, 1)
        $ character.Statup("Obed", 70, 2)

        "As your finger slides out, [character.Name] gasps and looks upset."

        jump before_action
    elif "fondle_ass" in character.RecentActions:
        $ character.FaceChange("sexy", 1)

        call repeat_action_lines(character)

        jump before_action
    elif "fondle_ass" in character.DailyActions:
        $ character.FaceChange("sexy", 1)

        call gently_lines(character)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(character, "fondle_ass")

        return
    else:
        call action_disapproved(character, Player.primary_action, character.FondleA)

    call action_rejected(character, "fondle_ass", character.FondleA)

    return

label finger_ass(character):
    $ Player.primary_action = "finger_ass"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(character)
    call fondle_set_modifier(character, "finger_ass")

    $ Approval = ApprovalCheck(character, 1300, TabM = 3) # 130, 145, 160, Taboo -120(250)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ character.FaceChange("surprised")
            $ character.Statup("Obed", 90, 2)
            $ character.Statup("Obed", 70, 2)
            $ character.Statup("Inbt", 80, 2)
            $ character.Statup("Inbt", 30, 2)

            "As you slide a finger in, [character.Name] tightens around it in surprise, but seems into it."

            $ character.FaceChange("sexy")

            jump before_action
        else:
            $ character.FaceChange("surprised")
            $ character.Statup("Love", 80, -2)
            $ character.Statup("Obed", 50, -3)

            call go_back_lines(character)

            $ temp_modifier = 0
            $ Trigger2 = 0

            return

    if "finger_ass" in character.DailyActions and not character.Loose:
        $ character.FaceChange("bemused", 1)

        call ass_sore_lines(character)
    elif "finger_ass" in character.DailyActions:
        $ character.FaceChange("sexy", 1)

        call gently_lines(character)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(character, "finger_ass")

        return

    else:
        call action_disapproved(character, "finger_ass", character.InsertA)

    call action_rejected(character, "finger_ass", character.InsertA)

    return

label eat_ass(character):
    $ Player.primary_action = "eat_ass"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(character)
    call fondle_set_modifier(character, "eat_ass")

    $ Approval = ApprovalCheck(character, 1550, TabM = 4) # 155, 170, 185, Taboo -160(315)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ character.FaceChange("surprised")
            $ character.Statup("Obed", 90, 1)
            $ character.Statup("Inbt", 80, 3)
            $ character.Statup("Inbt", 40, 2)

            "As you crouch down and start to lick her asshole, [character.Name] startles briefly, but then begins to melt."

            $ character.FaceChange("sexy")

            jump before_action
        else:
            $ character.FaceChange("surprised")
            $ character.Statup("Love", 80, -2)
            $ character.Statup("Obed", 50, -3)

            call go_back_lines(character)

            $ temp_modifier = 0
            $ Trigger2 = 0

            return

    if "eat_ass" in character.RecentActions:
        $ character.FaceChange("sexy", 1)

        call repeat_action_lines(character)
        jump before_action
    elif "eat_ass" in character.DailyActions:
        $ character.FaceChange("sexy", 1)

        call gently_lines(character)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(character, "eat_ass")

        return

    else:                                                                               #She's not into it, but maybe. . .
        call action_disapproved(character, "eat_ass", character.LickA)

    call action_rejected(character, "eat_ass", character.LickA)

    return
