label handjob_menu:
    menu:
        "Keep going. . ." if action_speed:
            pass
        "Start moving? . ." if primary_action in ["handjob", "footjob", "titjob"] and not action_speed:
            $ action_speed = 1
        "action_speed up. . ." if primary_action in ["handjob", "footjob", "titjob"] and action_speed < 2:
            $ action_speed = 2

            "You ask her to up the pace a bit."
        "action_speed up. . . (locked)" if primary_action in ["handjob", "footjob", "titjob"] and action_speed >= 2:
            pass
        "Slow Down. . ." if primary_action in ["handjob", "footjob", "titjob"] and action_speed:
            $ action_speed -= 1

            "You ask her to slow it down a bit."
        "Slow Down. . . (locked)" if primary_action in ["handjob", "footjob", "titjob"] and not action_speed:
            pass
        "Lick it. . ." if primary_action == "blowjob" and action_speed != 1:
            $ action_speed = 1
        "Lick it. . . (locked)" if primary_action == "blowjob" and action_speed == 1:
            pass
        "Just the head. . ." if primary_action == "blowjob" and action_speed != 2:
            $ action_speed = 2
        "Just the head. . . (locked)" if primary_action == "blowjob" and action_speed == 2:
            pass
        "Suck on it." if primary_action == "blowjob" and action_speed != 3:
            $ action_speed = 3

            if offhand_action == "jackin":
                "She dips her head a bit lower, and you move your hand out of the way."
        "Suck on it. (locked)" if primary_action == "blowjob" and action_speed == 3:
            pass
        "Take it deeper." if primary_action == "blowjob" and action_speed != 4:
            if "pushed" not in focused_Girl.recent_history and focused_Girl.Blow < 5:
                $ focused_Girl.change_stat("love", 80, -(20 - 2*focused_Girl.Blow))
                $ focused_Girl.change_stat("obedience", 80, 30 - 3*focused_Girl.Blow)
                $ focused_Girl.recent_history.append("pushed")

            if offhand_action == "jackin" and action_speed != 3:
                "She takes it to the root, and you move your hand out of the way."

            $ action_speed = 4
        "Take it deeper. (locked)" if primary_action == "blowjob" and action_speed == 4:
            pass
        "Set your own pace. . ." if primary_action == "blowjob":
            "[focused_Girl.name] hums contentedly."

            if "setpace" not in focused_Girl.recent_history:
                $ focused_Girl.change_stat("love", 80, 2)

            $ D20 = renpy.random.randint(1, 20)

            if focused_Girl.Blow < 5:
                $ D20 -= 10
            elif focused_Girl.Blow < 10:
                $ D20 -= 5

            if D20 > 15:
                $ action_speed = 4

                if "setpace" not in focused_Girl.recent_history:
                    $ focused_Girl.change_stat("inhibition", 80, 3)
            elif D20 > 10:
                $ action_speed = 3
            elif D20 > 5:
                $ action_speed = 2
            else:
                $ action_speed = 1

            $ focused_Girl.recent_history.append("setpace")
        "Slap her ass. . ." if primary_action in ["dildo_pussy", "dildo_ass"]:
            call Slap_Ass(focused_Girl)

            $ counter += 1
            $ Round -= 1

            jump handjob_cycle
        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
            pass
        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
            "You concentrate on not burning out too quickly."

            $ Player.FocusX = 1
        "Release your focus." if Player.FocusX:
            "You release your concentration. . ."

            $ Player.FocusX = 0
        "Turn her around." if primary_action == "footjob":
            $ focused_Girl.Pose = "doggy" if focused_Girl.Pose != "doggy" else "sex"

            "You turn her around. . ."

            jump handjob_cycle
        "View" if primary_action in ["dildo_pussy", "dildo_ass"]:
            call ViewShift(focused_Girl, "menu")
            jump handjob_cycle
        "Other options":
                menu:
                    "I also want to fondle her breasts." if offhand_action != "fondle breasts":
                        if focused_Girl.Action and multi_action:
                            $ offhand_action = "fondle breasts"

                            "You start to fondle her breasts."

                            $ focused_Girl.Action -= 1
                        else:
                            call tired_lines(focused_Girl)
                    "Offhand action" if primary_action in ["footjob", "dildo_pussy", "dildo_ass"]:
                        if focused_Girl.Action and multi_action:
                            call Offhand_Set

                            if offhand_action:
                                $ focused_Girl.Action -= 1
                        else:
                            call tired_lines(focused_Girl)
                    "Shift primary action":
                        if focused_Girl.Action and multi_action:
                            menu:
                                "How about a handy?" if primary_action in ["footjob", "titjob", "blowjob"]:
                                    if focused_Girl.Action and multi_action:
                                        $ action_context = "shift"

                                        call after_action
                                        call handjob(focused_Girl)
                                    else:
                                        call tired_lines(focused_Girl)
                                "How about a footjob?" if primary_action in ["handjob", "titjob", "blowjob"]:
                                    if focused_Girl.Action and multi_action:
                                        $ action_context = "shift"

                                        call after_action
                                        call footjob(focused_Girl)
                                    else:
                                        call tired_lines(focused_Girl)
                                "How about a titjob?" if primary_action in ["handjob", "footjob", "blowjob"]:
                                    if focused_Girl.Action and multi_action:
                                        $ action_context = "shift"

                                        call after_action
                                        call titjob(focused_Girl)
                                    else:
                                        call tired_lines(focused_Girl)
                                "How about a blowjob?" if primary_action in ["handjob", "footjob", "titjob"]:
                                    if focused_Girl.Action and multi_action:
                                        $ action_context = "shift"

                                        call after_action
                                        call blowjob(focused_Girl)
                                    else:
                                        call tired_lines(focused_Girl)
                                "I want to stick a finger in her ass." if primary_action == "dildo_pussy":
                                    if focused_Girl.Action and multi_action:
                                        $ action_context = "shift"

                                        call after_action
                                        call finger_ass(focused_Girl)
                                    else:
                                        call tired_lines(focused_Girl)
                                "Just stick a finger in her ass without asking." if primary_action == "dildo_pussy":
                                    if focused_Girl.Action and multi_action:
                                        $ action_context = "auto"

                                        call after_action
                                        call finger_ass(focused_Girl)
                                    else:
                                        call tired_lines(focused_Girl)
                                "I want to shift the dildo to her ass." if primary_action == "dildo_pussy":
                                    if focused_Girl.Action and multi_action:
                                        $ action_context = "shift"

                                        call after_action
                                        call dildo_ass(focused_Girl)
                                    else:
                                        call tired_lines(focused_Girl)
                                "I want to stick a finger in her pussy." if primary_action == "dildo_ass":
                                    if focused_Girl.Action and multi_action:
                                        $ action_context = "shift"

                                        call after_action
                                        call finger_pussy(focused_Girl)
                                    else:
                                        call tired_lines(focused_Girl)
                                "Just stick a finger in her pussy without asking." if primary_action == "dildo_ass":
                                    if focused_Girl.Action and multi_action:
                                        $ action_context = "auto"

                                        call after_action
                                        call finger_pussy(focused_Girl)
                                    else:
                                        call tired_lines(focused_Girl)
                                "I want to shift the dildo to her pussy." if primary_action == "dildo_ass":
                                    if focused_Girl.Action and multi_action:
                                        $ action_context = "shift"

                                        call after_action
                                        call dildo_pussy(focused_Girl)
                                    else:
                                        call tired_lines(focused_Girl)
                                "Never Mind":
                                    jump handjob_cycle
                        else:
                            call tired_lines(focused_Girl)
                    "Shift your focus." if primary_action in ["dildo_pussy", "dildo_ass"] and offhand_action:
                        $ action_context = "shift focus"

                        call after_action
                        call Offhand_Set
                    "Shift your focus. (locked)" if primary_action in ["dildo_pussy", "dildo_ass"] and not offhand_action:
                        pass
                    "Threesome actions (locked)" if not Partner:
                        pass
                    "Threesome actions" if Partner:
                        menu:
                            "Ask [focused_Girl.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                call Les_Change(focused_Girl)
                            "Ask [focused_Girl.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                pass
                            "Ask [Partner.name] to do something else":
                                call Three_Change(focused_Girl)
                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                $ position_change_timer = 0
                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                $ position_change_timer = 0
                            "Swap to [Partner.name]":
                                call primary_action_Swap(focused_Girl)
                            "Undress [Partner.name]":
                                call Girl_Undress(Partner)
                                jump handjob_cycle
                            "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                pass
                            "Clean up [Partner.name]" if Partner.Spunk:
                                call Girl_Cleanup(Partner,"ask")
                                jump handjob_cycle
                            "Never mind":
                                jump handjob_cycle
                    "Undress [focused_Girl.name]":
                        call Girl_Undress(focused_Girl)
                    "Clean up [focused_Girl.name] (locked)" if not focused_Girl.Spunk:
                        pass
                    "Clean up [focused_Girl.name]" if focused_Girl.Spunk:
                        call Girl_Cleanup(RogueX,"ask")
                    "Never mind":
                        jump handjob_cycle
        "Back to Sex Menu" if multi_action:
            ch_p "Let's try something else."

            call handjob_reset(focused_Girl)

            $ action_context = "shift"
            $ line = 0

            jump after_action
        "End Scene" if not multi_action:
            ch_p "Let's stop for now."

            call handjob_reset(focused_Girl)

            $ line = 0

            jump after_action

    jump handjob_menu_return

label handjob_set_modifier(Girl, action):
    if action == "handjob":
        if Girl.Hand >= 7: # She loves it
            $ temp_modifier += 10
        elif Girl.Hand >= 3: #You've done it before several times
            $ temp_modifier += 7
        elif Girl.Hand: #You've done it before
            $ temp_modifier += 3

        if "exhibitionist" in Girl.Traits:
            $ temp_modifier += (3*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.Petnames:
            $ temp_modifier += 10
        elif "ex" in Girl.Traits:
            $ temp_modifier -= 40

        if Girl.Addict >= 75 and Girl.Swallow >= 3: #She's really strung out and has swallowed
            $ temp_modifier += 15
        if Girl.Addict >= 75:
            $ temp_modifier += 5

        if action_context == "shift":
            $ temp_modifier += 15
    elif action == "footjob":
        if Girl.Foot >= 7: # She loves it
            $ temp_modifier += 10
        elif Girl.Foot >= 3: #You've done it before several times
            $ temp_modifier += 7
        elif Girl.Foot: #You've done it before
            $ temp_modifier += 3

        if Girl.Addict >= 75 and Girl.Swallow >=3: #She's really strung out and has swallowed
            $ temp_modifier += 10
        if Girl.Addict >= 75:
            $ temp_modifier += 5

        if action_context == "shift":
            $ temp_modifier += 15
        if "exhibitionist" in Girl.Traits:
            $ temp_modifier += (3*Taboo)
        if Girl in Player.Harem or "sex friend" in Girl.Petnames:
            $ temp_modifier += 10
        elif "ex" in Girl.Traits:
            $ temp_modifier -= 40
    elif action == "titjob":
        if Girl.Tit >= 7: # She loves it
            $ temp_modifier += 10
        elif Girl.Tit >= 3: #You've done it before several times
            $ temp_modifier += 7
        elif Girl.Tit: #You've done it before
            $ temp_modifier += 5

        if Girl.SeenChest and ApprovalCheck(Girl, 500): # You've seen her tits.
            $ temp_modifier += 10
        if not Girl.Chest and not Girl.Over: #She's already topless
            $ temp_modifier += 10

        if "exhibitionist" in Girl.Traits:
            $ temp_modifier += (5*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.Petnames:
            $ temp_modifier += 10
        elif "ex" in Girl.Traits:
            $ temp_modifier -= 30

        if Girl.lust > 75: #She's really horny
            $ temp_modifier += 10

        if Girl.Addict >= 75 and Girl.Swallow >= 3: #She's really strung out and has swallowed
            $ temp_modifier += 15
        if Girl.Addict >= 75:
            $ temp_modifier += 5

        if action_context == "shift":
            $ temp_modifier += 15
    elif action == "blowjob":
        if Girl.Blow >= 7: # She loves it
            $ temp_modifier += 15
        elif Girl.Blow >= 3: #You've done it before several times
            $ temp_modifier += 10
        elif Girl.Blow: #You've done it before
            $ temp_modifier += 7

        if Girl.Addict >= 75 and Girl.Swallow >=3: #She's really strung out and has swallowed
            $ temp_modifier += 25
        elif Girl.Addict >= 75: #She's really strung out
            $ temp_modifier += 15

        if "exhibitionist" in Girl.Traits:
            $ temp_modifier += (4*Taboo)
        if Girl in Player.Harem or "sex friend" in Girl.Petnames:
            $ temp_modifier += 10
        elif "ex" in Girl.Traits:
            $ temp_modifier -= 40

        if action_context == "shift":
            $ temp_modifier += 15
    elif action == "dildo_pussy":
        if Girl.DildoP: #You've done it before
            $ temp_modifier += 15
        if Girl.PantsNum() > 6: # she's got pants on.
            $ temp_modifier -= 20

        if Girl.lust > 95:
            $ temp_modifier += 20
        elif Girl.lust > 85: #She's really horny
            $ temp_modifier += 15

        if action_context == "shift":
            $ temp_modifier += 10
        if "exhibitionist" in Girl.Traits:
            $ temp_modifier += (5*Taboo)
        if Girl in Player.Harem or "sex friend" in Girl.Petnames:
            $ temp_modifier += 10
        elif "ex" in Girl.Traits:
            $ temp_modifier -= 40
    elif action == "dildo_ass":
        if Girl.Loose:
            $ temp_modifier += 30
        elif "anal" in Girl.recent_history or "dildo anal" in Girl.recent_history:
            $ temp_modifier -= 20
        elif "anal" in Girl.daily_history or "dildo anal" in Girl.daily_history:
            $ temp_modifier -= 10
        elif (Girl.Anal + Girl.DildoA + Girl.Plug) > 0: #You've done it before
            $ temp_modifier += 20

        if Girl.PantsNum() > 6: # she's got pants on.
            $ temp_modifier -= 20

        if Girl.lust > 95:
            $ temp_modifier += 20
        elif Girl.lust > 85: #She's really horny
            $ temp_modifier += 15

        if action_context == "shift":
            $ temp_modifier += 10
        if "exhibitionist" in Girl.Traits:
            $ temp_modifier += (5*Taboo)
        if Girl in Player.Harem or "sex friend" in Girl.Petnames:
            $ temp_modifier += 10
        elif "ex" in Girl.Traits:
            $ temp_modifier -= 40

    if Girl.ForcedCount and not Girl.Forced:
        $ temp_modifier -= 5*Girl.ForcedCount

    if Taboo and "tabno" in Girl.daily_history:
        $ temp_modifier -= 10

    if "no_" + action in Girl.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no_" + action in Girl.recent_history else 0

    return

label end_of_handjob_round(Girl, action):
    $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up

    if Player.Focus >= 100 or Girl.lust >= 100:
        if Player.Focus >= 100:
            call Player_Cumming(focused_Girl)

            if "angry" in Girl.recent_history:
                call handjob_reset(Girl)

                return True

            $ Girl.change_stat("lust", 200, 5)

            if 100 > Girl.lust >= 70 and Girl.OCount < 2 and Girl.SEXP >= 20:
                $ Girl.AddWord(0, "unsatisfied", "unsatisfied")

            if Player.Focus > 80:
                jump after_action

            $ line = "came"

        if Girl.lust >= 100:
            call Girl_Cumming(Girl)

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

    if action in ["handjob", "footjob", "titjob"]:
        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0
    elif action in ["blowjob", "dildo_pussy", "dildo_ass"]:
        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

    if action == "handjob":
        $ bonus = Girl.Hand
    elif action == "footjob":
        $ bonus = Girl.Foot
    elif action == "titjob":
        $ bonus = Girl.Tit
    elif action == "blowjob":
        $ bonus = Girl.Blow
    elif action == "dildo_pussy":
        $ bonus = Girl.DildoP
    elif action == "dildo_ass":
        $ bonus = Girl.DildoA

    if Girl.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
        pass
    elif counter == (5 + bonus):
        $ Girl.Brows = "confused"

        call getting_close_lines(Girl)
    elif action in ["dildo_pussy", "dildo_ass"] and Girl.lust >= 80:
        pass
    elif (action in ["handjob, footjob, titjob, blowjob"] and counter == (10 + bonus)) or (action in ["dildo_pussy", "dildo_ass"] and (counter == (15 + bonus) and Girl.SEXP <= 100 and not ApprovalCheck(Girl, 1200, "LO"))):
        $ Girl.Brows = "angry"

        call getting_rugburn_lines(Girl)

        menu:
            extend ""
            "How about a handy?" if action in ["footjob", "titjob", "blowjob"] and Girl.Action and multi_action:
                $ action_context = "shift"

                call handjob_after
                call handjob(Girl)
            "How about a footjob?" if action in ["handjob", "titjob", "blowjob"] and Girl.Action and multi_action:
                $ action_context = "shift"

                call handjob_after
                call footjob(Girl)
            "How about a titjob?" if action in ["handjob", "footjob", "blowjob"] and Girl.Action and multi_action:
                $ action_context = "shift"

                call handjob_after
                call titjob(Girl)
            "How about a BJ?" if action in ["handjob", "footjob", "titjob"] and Girl.Action and multi_action:
                $ action_context = "shift"

                call handjob_after
                call blowjob(Girl)
            "Finish up." if action in ["handjob", "footjob", "titjob", "blowjob"] and Player.FocusX:
                "You release your concentration. . ."

                $ Player.FocusX = 0
                $ Player.Focus += 15

                jump handjob_cycle
            "Finish up." if action in ["dildo_pussy", "dildo_ass"]:
                "You let go. . ."

                jump after_action
            "Let's try something else." if multi_action:
                $ line = 0
                $ action_context = "shift"

                jump after_action
            "No, get back down there." if action in ["handjob", "footjob", "titjob", "blowjob"]:
                if ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "O"):
                    $ Girl.change_stat("love", 200, -5)
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_stat("obedience", 80, 2)

                    "She grumbles but keeps going."
                else:
                    $ Girl.change_face("angry", 1)

                    call reset_position(Girl)

                    "She scowls at you, drops your cock and pulls back."

                    call this_is_boring_lines(Girl)

                    $ Girl.change_stat("love", 50, -3, 1)
                    $ Girl.change_stat("love", 80, -4, 1)
                    $ Girl.change_stat("obedience", 30, -1, 1)
                    $ Girl.change_stat("obedience", 50, -1, 1)
                    $ Girl.AddWord(1,"angry","angry")

                    jump after_action
            "No, this is fun." if action in ["dildo_pussy", "dildo_ass"]:
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

label handjob(Girl):
    $ primary_action = "handjob"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(Girl)
    call handjob_set_modifier(Girl, "handjob")

    $ Approval = ApprovalCheck(Girl, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if not Girl.Hand and "no hand" not in Girl.recent_history:
        $ Girl.change_face("surprised", 1)
        $ Girl.Mouth = "kiss"

        ch_r "You want me to rub your cock, with my hand?"

    if not Girl.Hand and Approval:                                                 #First time dialog
        call first_action_approval(Girl, "handjob")
    elif Approval:
        call action_approved(Girl, "handjob", Girl.Hand)

    if Approval >= 2:
        call action_accepted(Girl, "handjob")

        return
    else:                                                                               #She's not into it, but maybe. . .
        call action_disapproved(Girl, "handjob", Girl.Hand)

    $ Girl.ArmPose = 1

    call action_rejected(Girl, "handjob", Girl.Hand)

    return

label footjob(Girl):
    $ primary_action = "footjob"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(Girl)
    call handjob_set_modifier(Girl, "footjob")

    $ Approval = ApprovalCheck(Girl, 1250, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if action_context == Girl:                                                                  #Rogue auto-starts
        if Approval > 2:                                                      # fix, add rogue auto stuff here
            call Girl_initiated_action(Girl, "footjob")

            if _return:
                return

            if primary_action:
                $ girl_offhand_action = "foot"
                return

            call before_action(Girl, "footjob")
        else:
            $ temp_modifier = 0                               # fix, add rogue auto stuff here
            $ offhand_action = 0

            return

    if not Girl.Foot and "no foot" not in Girl.recent_history:
        $ Girl.change_face("confused", 2)

        ch_r "Huh, so like a handy, but with my feet?"

        $ Girl.Blush = 1

    if not Girl.Foot and Approval:                                                 #First time dialog
        call first_action_approval(Girl, "footjob")
    elif Approval:
        call action_approved(Girl, "footjob", Girl.Foot)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(Girl, "footjob")

        return
    else:                                                                               #She's not into it, but maybe. . .
        call action_disapproved(Girl, "footjob", Girl.Foot)

    $ Girl.ArmPose = 1

    call action_rejected(Girl, "footjob", Girl.Foot)

    return

label titjob(Girl):
    $ primary_action = "titjob"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(Girl)
    call handjob_set_modifier(Girl, "titjob")

    $ Approval = ApprovalCheck(Girl, 1200, TabM = 5) # 120, 135, 150, Taboo -200(320)

    if not Girl.Tit and "no titjob" not in Girl.recent_history:
        $ Girl.change_face("surprised", 1)
        $ Girl.Mouth = "kiss"

        ch_r "You want me to rub your cock with my breasts?"

        if Girl.Blow:
            $ Girl.Mouth = "smile"

            ch_r "My mouth wasn't enough?"
        elif Girl.Hand:
            $ Girl.Mouth = "smile"

            ch_r "My hand wasn't enough?"

    if not Girl.Tit and Approval:                                                 #First time dialog
        call first_action_approval(Girl)
    elif Approval:
        call action_approved(Girl, "titjob", Girl.Tit)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(Girl, "titjob")
    else:                                                                               #She's not into it, but maybe. . .
        call action_disapproved(Girl, "titjob", Girl.Tit)

    call action_rejected(Girl, "titjob", Girl.Tit)

    return

label blowjob(Girl):
    $ primary_action = "blowjob"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(Girl)
    call handjob_set_modifier(Girl, "blowjob")

    $ Approval = ApprovalCheck(Girl, 1300, TabM = 4) # 130, 145, 160, Taboo -160(290)

    if not Girl.Blow and "no blow" not in Girl.recent_history:
        $ Girl.change_face("surprised", 1)
        $ Girl.Mouth = "kiss"

        ch_r "You want me to put your dick. . . in my mouth?"

        if Girl.Hand:
            $ Girl.Mouth = "smile"

            ch_r "My hand wasn't enough?"

    if not Girl.Blow and Approval:                                                 #First time dialog
        call first_action_approval(Girl)
    elif Approval:
        call action_approved(Girl, "blowjob", Girl.Blow)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(Girl, "blowjob")

        return
    else:                                                                               #She's not into it, but maybe. . .
        call action_disapproved(Girl, "blowjob", Girl.Blow)

    call action_rejected(Girl, "blowjob", Girl.Blow)

    return

label dildo_pussy(Girl):
    $ primary_action = "dildo_pussy"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(Girl)
    call Rogue_Dildo_Check

    if not _return:
        return

    call handjob_set_modifier(Girl, "dildo_pussy")

    $ Approval = ApprovalCheck(Girl, 1250, TabM = 4) # 125, 140, 155, Taboo -160(335)

    if action_context == Girl:                                                                  #Rogue auto-starts
        if Approval > 2:                                                      # fix, add rogue auto stuff here

            call Girl_initiated_action(Girl, "dildo_pussy")

            if _return:
                return

            call before_action(Girl, "dildo_pussy")
        else:
            $ temp_modifier = 0                               # fix, add rogue auto stuff here
            $ offhand_action = 0
        return

    if action_context == "auto":
        "You rub the dildo across her body, and along her moist slit."

        $ Girl.change_face("surprised", 1)

        if (Girl.DildoP and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
            "[Girl.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."

            $ Girl.change_face("sexy")
            $ Girl.change_stat("obedience", 70, 3)
            $ Girl.change_stat("inhibition", 50, 3)
            $ Girl.change_stat("inhibition", 70, 1)

            ch_r "Ok, [Girl.Petname], let's do this."

            jump before_action
        else:                                                                                                            #she's questioning it
            $ Girl.Brows = "angry"

            menu:
                ch_r "Hey, what do you think you're doing back there?!"
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ Girl.change_face("sexy", 1)
                        $ Girl.change_stat("obedience", 70, 3)
                        $ Girl.change_stat("inhibition", 50, 3)
                        $ Girl.change_stat("inhibition", 70, 1)

                        call since_you_are_so_nice_lines(Girl)

                        jump before_action

                    "You pull back before you really get it in."

                    $ Girl.change_face("bemused", 1)

                    if Girl.DildoP:
                        ch_r "Well ok, [Girl.Petname], no harm done. Just give me a little warning next time."
                    else:
                        ch_r "Well ok, [Girl.Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."
                "Just playing with my favorite toys.":
                    $ Girl.change_stat("love", 80, -10, 1)
                    $ Girl.change_stat("love", 200, -10)

                    "You press it inside some more."

                    $ Girl.change_stat("obedience", 70, 3)
                    $ Girl.change_stat("inhibition", 50, 3)

                    if not ApprovalCheck(Girl, 700, "O", TabM=1): #Checks if obedience is 700+
                        $ Girl.change_face("angry")

                        "[Girl.name] shoves you away and slaps you in the face."
                        ch_r "Jackass!"
                        ch_r "If that's how you want to treat me, we're done here!"

                        $ Girl.change_stat("love", 50, -10, 1)
                        $ Girl.change_stat("obedience", 50, 3)

                        $ renpy.pop_call()

                        if action_context:
                            $ renpy.pop_call()

                        if renpy.showing("Rogue_Doggy"):
                            call doggy_reset(Girl)

                        $ Girl.recent_history.append("angry")
                        $ Girl.daily_history.append("angry")
                    else:
                        $ Girl.change_face("sad")

                        "[Girl.name] doesn't seem to be into this, you're lucky she's so obedient."

                        jump before_action
        return

    if not Girl.DildoP:
        $ Girl.change_face("surprised", 1)
        $ Girl.Mouth = "kiss"

        ch_r "Hmmm, so you'd like to try out some toys?"

        if Girl.Forced:
            $ Girl.change_face("sad")

            ch_r "I suppose there are worst things you could ask for."

    if not Girl.DildoP and Approval:
        call first_action_approval(Girl, "dildo_pussy")
    elif Approval:
        call action_approved(Girl, "dildo_pussy", Girl.DildoP)

    if Approval >= 2:
        call action_accepted(Girl, "dildo_pussy")
    else:
        call action_disapproved(Girl, "dildo_pussy", Girl.DildoP)

    $ Girl.ArmPose = 1

    call action_rejected(Girl, "dildo_pussy", Girl.DildoP)

    return

label dildo_ass(Girl):
    $ primary_action = "dildo_ass"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(Girl)
    call Rogue_Dildo_Check

    if not _return:
        return

    call handjob_set_modifier(Girl, "dildo_ass")

    $ Approval = ApprovalCheck(Girl, 1450, TabM = 4) # 145, 160, 175, Taboo -160(355)

    if action_context == Girl:
        if Approval > 2:                                                      # fix, add rogue auto stuff here
            call Girl_initiated_action(Girl, "dildo_ass")

            if _return:
                return

            jump before_action
        else:
            $ temp_modifier = 0                               # fix, add rogue auto stuff here
            $ offhand_action = 0
        return

    if action_context == "auto":
        "You rub the dildo across her body, and against her tight anus."
        $ Girl.change_face("surprised", 1)

        if (Girl.DildoA and Approval) or (Approval > 1):
            "[Girl.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."

            $ Girl.change_face("sexy")
            $ Girl.change_stat("obedience", 70, 3)
            $ Girl.change_stat("inhibition", 50, 3)
            $ Girl.change_stat("inhibition", 70, 1)

            ch_r "Ok, [Girl.Petname], let's do this."

            jump before_action
        else:
            $ Girl.Brows = "angry"

            menu:
                ch_r "Hey, what do you think you're doing back there?!"
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ Girl.change_face("sexy", 1)
                        $ Girl.change_stat("obedience", 70, 3)
                        $ Girl.change_stat("inhibition", 50, 3)
                        $ Girl.change_stat("inhibition", 70, 1)

                        call since_you_are_so_nice_lines(Girl)

                        jump before_action

                    "You pull back before you really get it in."

                    $ Girl.change_face("bemused", 1)

                    if Girl.DildoA:
                        ch_r "Well ok, [Girl.Petname], no harm done. Just give me a little warning next time."
                    else:
                        ch_r "Well ok, [Girl.Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."
                "Just playing with my favorite toys.":
                    $ Girl.change_stat("love", 80, -10, 1)
                    $ Girl.change_stat("love", 200, -10)

                    "You press it inside some more."
                    $ Girl.change_stat("obedience", 70, 3)
                    $ Girl.change_stat("inhibition", 50, 3)

                    if not ApprovalCheck(Girl, 700, "O", TabM=1): #Checks if obedience is 700+
                        $ Girl.change_face("angry")

                        "[Girl.name] shoves you away and slaps you in the face."
                        ch_r "Jackass!"
                        ch_r "If that's how you want to treat me, we're done here!"

                        $ Girl.change_stat("love", 50, -10, 1)
                        $ Girl.change_stat("obedience", 50, 3)

                        $ renpy.pop_call()

                        if action_context:
                            $ renpy.pop_call()

                        if renpy.showing("Rogue_Doggy"):
                            call doggy_reset(Girl)

                        $ Girl.recent_history.append("angry")
                        $ Girl.daily_history.append("angry")
                    else:
                        $ Girl.change_face("sad")

                        "[Girl.name] doesn't seem to be into this, you're lucky she's so obedient."

                        jump before_action
        return

    if not Girl.DildoA:
        $ Girl.change_face("surprised", 1)
        $ Girl.Mouth = "kiss"

        ch_r "Hmmm, so you'd like to try out some toys?"

        if Girl.Forced:
            $ Girl.change_face("sad")

            ch_r "You had to go for the butt, uh?"

    if not Girl.Loose and ("dildo anal" in Girl.recent_history or "anal" in Girl.recent_history or "dildo anal" in Girl.daily_history or "anal" in Girl.daily_history):
        $ Girl.change_face("bemused", 1)

        ch_r "I'm still a bit sore from earlier. . ."

    if not Girl.DildoA and Approval:
        call first_action_approval(Girl, "dildo_ass")
    elif Approval:
        call action_approved(Girl, "dildo_ass")

    if Approval >= 2:
        call action_accepted(Girl, "dildo_ass")
    else:
        call action_disapproved(Girl, "dildo_ass", Girl.DildoA)

    $ Girl.ArmPose = 1

    call action_rejected(Girl, "dildo_ass", Girl.DildoA)

    return

label dildo_check(Girl):
    if "dildo" in Player.Inventory:
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in Girl.Inventory:
        "You ask [Girl.name] to get out her favorite dildo."
    else:
        "You don't have one of those on you."

        return False

    return True

label vibrator_check(Girl):
    if "vibrator" in Player.Inventory:
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in Girl.Inventory:
        "You ask [Girl.name] to get out her vibrator."
    else:
        "You don't have one of those on you."

        return False

    return True
