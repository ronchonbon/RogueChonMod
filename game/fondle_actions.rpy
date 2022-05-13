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

            jump fondle_cycle
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
            jump fondle_cycle
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

                                        call after_fondle
                                        call fondle_pussy(Player.focused_girl)
                                    else:
                                        call tired_lines(Player.focused_girl)
                                "Shift your hands a bit higher without asking":
                                    if Player.focused_girl.Action:
                                        $ Situation = "auto"

                                        call after_fondle
                                        call fondle_pussy(Player.focused_girl)
                                    else:
                                        "As your hands creep upwards, she grabs your wrists."

                                        call tired_lines(Player.focused_girl)
                                "Never Mind":
                                    jump fondle_cycle
                        else:
                            call tired_lines(Player.focused_girl)
                    elif Player.primary_action == "fondle_breasts":
                        if Player.focused_girl.Action and MultiAction:
                            menu:
                                "Ask to suck on them.":
                                    if Player.focused_girl.Action and MultiAction:
                                        $ Situation = "shift"

                                        call after_fondle
                                        call suck_breasts(Player.focused_girl)
                                    else:
                                        call tired_lines(Player.focused_girl)
                                "Just suck on them without asking.":
                                    if Player.focused_girl.Action and MultiAction:
                                        $ Situation = "auto"

                                        call after_fondle
                                        call suck_breasts(Player.focused_girl)
                                    else:
                                        "As you lean in to suck on her breast, she grabs your head and pushes back."

                                        call tired_lines(Player.focused_girl)
                                "Never Mind":
                                    jump fondle_cycle
                        else:
                            call tired_lines(Player.focused_girl)
                    elif Player.primary_action == "suck_breasts":
                        if MultiAction:
                            menu:
                                "Pull back to fondling.":
                                    if Player.focused_girl.Action and MultiAction:
                                        $ Situation = "pullback"

                                        call after_fondle
                                        call fondle_breasts
                                    else:
                                        "As you pull back, [Player.focused_girl.Name] pushes you back in close."

                                        call tired_lines(Player.focused_girl)
                                "Never Mind":
                                    jump fondle_cycle
                        else:
                            call tired_lines(Player.focused_girl)
                    elif Player.primary_action == "fondle_pussy":
                        if MultiAction:
                            menu:
                                "I want to lick your pussy.":
                                    if Player.focused_girl.Action:
                                        $ Situation = "shift"

                                        call after_fondle
                                        call eat_pussy(Player.focused_girl)

                                        return False
                                    else:
                                        call tired_lines(Player.focused_girl)
                                "Just start licking":
                                    if Player.focused_girl.Action:
                                        $ Situation = "auto"

                                        call after_fondle
                                        call eat_pussy(Player.focused_girl)

                                        return False
                                    else:
                                        "As you lean in to lick her pussy, she grabs your head and pushes back."

                                        call tired_lines(Player.focused_girl)
                                "Pull back to the thighs":
                                    if Player.focused_girl.Action:
                                        $ Situation = "pullback"

                                        call after_fondle
                                        call fondle_thighs(Player.focused_girl)

                                        return False
                                    else:
                                        "As you pull your hand back, [Player.focused_girl.Name] pulls it back in close."

                                        call tired_lines(Player.focused_girl)
                                "I want to stick a dildo in.":
                                    if Player.focused_girl.Action:
                                        $ Situation = "shift"

                                        call after_fondle
                                        call dildo_pussy(Player.focused_girl)

                                        return False
                                    else:
                                        call tired_lines(Player.focused_girl)
                                "Never Mind":
                                    jump fondle_cycle
                        else:
                            call tired_lines(Player.focused_girl)
                    elif Player.primary_action == "eat_pussy":
                        if Player.focused_girl.Action and MultiAction:
                            menu:
                                "Pull out and start rubbing again.":
                                    $ Situation = "pullback"

                                    call after_fondle
                                    call fondle_pussy(Player.focused_girl)
                                "I want to stick a dildo in.":
                                    $ Situation = "shift"

                                    call after_fondle
                                    call dildo_pussy(Player.focused_girl)
                                "Never Mind":
                                    jump fondle_cycle
                        else:
                            call tired_lines(Player.focused_girl)
                    elif Player.primary_action == "fondle_ass":
                        if Player.focused_girl.Action and MultiAction:
                            menu:
                                "I want to stick a finger in.":
                                    $ Situation = "shift"

                                    call after_fondle
                                    call finger_ass(Player.focused_girl)
                                "Just stick a finger in without asking.":
                                    $ Situation = "auto"

                                    call after_fondle
                                    call finger_ass(Player.focused_girl)
                                "I want to lick your asshole.":
                                    $ Situation = "shift"

                                    call after_fondle
                                    call eat_ass(Player.focused_girl)
                                "Just start licking.":
                                    $ Situation = "auto"

                                    call after_fondle
                                    call eat_ass(Player.focused_girl)
                                "I want to stick a dildo in.":
                                    $ Situation = "shift"

                                    call after_fondle
                                    call dildo_ass(Player.focused_girl)
                                "Never Mind":
                                    jump fondle_cycle
                    elif Player.primary_action == "finger_ass":
                        if Player.focused_girl.Action and MultiAction:
                            menu:
                                "Pull out and start rubbing again.":
                                    $ Situation = "pullback"

                                    call after_fondle
                                    call fondle_ass(Player.focused_girl)
                                "I want to lick your asshole.":
                                    $ Situation = "shift"

                                    call after_fondle
                                    call eat_ass(Player.focused_girl)
                                "Just start licking.":
                                    $ Situation = "auto"

                                    call after_fondle
                                    call eat_ass(Player.focused_girl)
                                "I want to stick a dildo in.":
                                    $ Situation = "shift"

                                    call after_fondle
                                    call dildo_ass(Player.focused_girl)
                                "Never Mind":
                                    jump fondle_cycle
                        else:
                            call tired_lines(Player.focused_girl)
                    elif Player.primary_action == "eat_ass":
                        if Player.focused_girl.Action and MultiAction:
                            menu:
                                "Switch to fondling.":
                                    $ Situation = "pullback"

                                    call after_fondle
                                    call fondle_ass(Player.focused_girl)
                                "I want to stick a finger in.":
                                    $ Situation = "shift"

                                    call after_fondle
                                    call finger_ass(Player.focused_girl)
                                "Just stick a finger in [[without asking].":
                                    $ Situation = "auto"

                                    call after_fondle
                                    call finger_ass(Player.focused_girl)
                                "I want to stick a dildo in.":
                                    $ Situation = "shift"

                                    call after_fondle
                                    call dildo_ass(Player.focused_girl)
                                "Never Mind":
                                    jump fondle_cycle
                        else:
                            call tired_lines(Player.focused_girl)
                "Shift your focus" if Trigger2:
                    $ Situation = "shift focus"

                    call after_fondle
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
                            jump fondle_cycle
                        "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                            pass
                        "Clean up [Partner.Name]" if Partner.Spunk:
                            call Girl_Cleanup(Partner,"ask")
                            jump fondle_cycle
                        "Never mind":
                            jump fondle_cycle
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
                    jump fondle_cycle
        "Back to Sex Menu" if MultiAction:
            ch_p "Let's try something else."

            call reset_position(character)

            $ Situation = "shift"
            $ Line = 0

            jump after_fondle
        "End Scene" if not MultiAction:
            ch_p "Let's stop for now."

            call reset_position(character)

            $ Line = 0

            jump after_fondle

    jump fondle_menu_return

label before_fondle:
    if Player.primary_action not in ["suck_breasts", "fondle_pussy"]:
        if Trigger == "kiss_you":
            $ Trigger = Player.primary_action

            return

    if Player.primary_action != "finger_pussy" and Trigger2 == Player.primary_action:
        return

    # we have to fix the launch functions to accept Player.primary_action
    if Player.primary_action in ["fondle_thighs", "fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
        if Player.focused_girl != EmmaX:
            call pussy_launch(Player.focused_girl, trigger = Player.primary_action)
        else:
            if Player.focused_girl.Pose in ["doggy", "sex"]:
                call ViewShift(Player.focused_girl, Player.focused_girl.Pose, 0, Player.primary_action)
            else:
                call ViewShift(Player.focused_girl, "pussy", 0, Player.primary_action)
    elif Player.primary_action in ["fondle_breasts", "suck_breasts"]:
        call breasts_launch(Player.focused_girl, trigger = Player.primary_action)

    if Situation == Player.focused_girl:
        $ Situation = 0

        call character_initated_action(Player.focused_girl, Player.primary_action)

        if _return:
            return

    if not Player.focused_girl.Forced and Situation != "auto":
        $ temp_modifier = 0

        if Player.primary_action in ["eat_pussy", "eat_ass"] and Player.focused_girl.PantsNum() >= 6:
            $ temp_modifier = 15

        if Player.primary_action in ["fondle_thighs", "fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
            call Bottoms_Off
        elif Player.primary_action in ["fondle_breasts", "suck_breasts"]:
            call Top_Off
        elif Player.primary_action == "finger_pussy":
            call Girl_Undress(Player.focused_girl, "bottom")

        if "angry" in Player.focused_girl.RecentActions:
            return

    $ temp_modifier = 0

    if Player.primary_action == "fondle_thighs" and not Player.focused_girl.FondleT:
        if Player.focused_girl.Forced:
            $ Player.focused_girl.Statup("Love", 90, -10)
            $ Player.focused_girl.Statup("Obed", 70, 15)
            $ Player.focused_girl.Statup("Inbt", 80, 10)
        else:
            $ Player.focused_girl.Statup("Love", 90, 5)
            $ Player.focused_girl.Statup("Obed", 70, 10)
            $ Player.focused_girl.Statup("Inbt", 80, 15)
    elif Player.primary_action == "fondle_breasts" and not Player.focused_girl.FondleB:
        if Player.focused_girl.Forced:
            $ Player.focused_girl.Statup("Love", 90, -20)
            $ Player.focused_girl.Statup("Obed", 70, 25)
            $ Player.focused_girl.Statup("Inbt", 80, 15)
        else:
            $ Player.focused_girl.Statup("Love", 90, 10)
            $ Player.focused_girl.Statup("Obed", 70, 5)
            $ Player.focused_girl.Statup("Inbt", 80, 15)
    elif Player.primary_action == "suck_breasts" and not Player.focused_girl.SuckB:
        if Player.focused_girl.Forced:
            $ Player.focused_girl.Statup("Love", 90, -25)
            $ Player.focused_girl.Statup("Obed", 70, 25)
            $ Player.focused_girl.Statup("Inbt", 80, 17)
        else:
            $ Player.focused_girl.Statup("Love", 90, 10)
            $ Player.focused_girl.Statup("Obed", 70, 10)
            $ Player.focused_girl.Statup("Inbt", 80, 15)
    elif Player.primary_action == "fondle_pussy" and not Player.focused_girl.FondleP:
        if Player.focused_girl.Forced:
            $ Player.focused_girl.Statup("Love", 90, -50)
            $ Player.focused_girl.Statup("Obed", 70, 35)
            $ Player.focused_girl.Statup("Inbt", 80, 25)
        else:
            $ Player.focused_girl.Statup("Love", 90, 10)
            $ Player.focused_girl.Statup("Obed", 70, 10)
            $ Player.focused_girl.Statup("Inbt", 80, 15)
    elif Player.primary_action == "finger_pussy" and not Player.focused_girl.InsertP:
        if Player.focused_girl.Forced:
            $ Player.focused_girl.Statup("Love", 90, -60)
            $ Player.focused_girl.Statup("Obed", 70, 55)
            $ Player.focused_girl.Statup("Inbt", 80, 35)
        else:
            $ Player.focused_girl.Statup("Love", 90, 10)
            $ Player.focused_girl.Statup("Obed", 70, 20)
            $ Player.focused_girl.Statup("Inbt", 80, 25)
    if Player.primary_action == "eat_pussy" and not Player.focused_girl.LickP:
        if Player.focused_girl.Forced:
            $ Player.focused_girl.Statup("Love", 90, -30)
            $ Player.focused_girl.Statup("Obed", 70, 35)
            $ Player.focused_girl.Statup("Inbt", 80, 75)
        else:
            $ Player.focused_girl.Statup("Love", 90, 35)
            $ Player.focused_girl.Statup("Obed", 70, 15)
            $ Player.focused_girl.Statup("Inbt", 80, 35)
    elif Player.primary_action == "fondle_ass" and not Player.focused_girl.FondleA:
        if Player.focused_girl.Forced:
            $ Player.focused_girl.Statup("Love", 90, -20)
            $ Player.focused_girl.Statup("Obed", 70, 20)
            $ Player.focused_girl.Statup("Inbt", 80, 15)
        else:
            $ Player.focused_girl.Statup("Love", 90, 10)
            $ Player.focused_girl.Statup("Obed", 70, 12)
            $ Player.focused_girl.Statup("Inbt", 80, 20)
    elif Player.primary_action == "finger_ass" and not Player.focused_girl.InsertA:
        if Player.focused_girl.Forced:
            $ Player.focused_girl.Statup("Love", 90, -50)
            $ Player.focused_girl.Statup("Obed", 70, 60)
            $ Player.focused_girl.Statup("Inbt", 80, 35)
        else:
            $ Player.focused_girl.Statup("Love", 90, 10)
            $ Player.focused_girl.Statup("Obed", 70, 20)
            $ Player.focused_girl.Statup("Inbt", 80, 25)
    elif Player.primary_action == "eat_ass" and not Player.focused_girl.LickA:
        if Player.focused_girl.Forced:
            $ Player.focused_girl.Statup("Love", 90, -30)
            $ Player.focused_girl.Statup("Obed", 70, 40)
            $ Player.focused_girl.Statup("Inbt", 80, 80)
        else:
            $ Player.focused_girl.Statup("Love", 90, 35)
            $ Player.focused_girl.Statup("Obed", 70, 25)
            $ Player.focused_girl.Statup("Inbt", 80, 55)

    if Taboo:
        if Player.primary_action == "fondle_thighs":
            $ Player.focused_girl.Statup("Lust", 200, (int(Taboo/5)))
            $ Player.focused_girl.Statup("Inbt", 200, (2*(int(Taboo/5))))
        elif Player.primary_action in ["fondle_breasts", "suck_breasts", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass"]:
            $ Player.focused_girl.Inbt += int(Taboo/10)
            $ Player.focused_girl.Lust += int(Taboo/5)
        elif Player.primary_action in ["fondle_pussy", "eat_pussy", "finger_ass", "eat_ass"]:
            if Player.focused_girl == JeanX and Player.focused_girl.Taboo:
                $ Player.focused_girl.Statup("Inbt", 200, (int(Taboo/10)))
            elif Taboo:
                $ Player.focused_girl.Inbt += int(Taboo/10)

            $ Player.focused_girl.Lust += int(Taboo/5)

    if Situation:
        $ renpy.pop_call()

        $ Situation = 0

    if Player.primary_action in ["eat_pussy", "eat_ass"]:
        if Player.focused_girl.PantsNum() == 5:
            $ Player.focused_girl.Upskirt = 1
            $ Player.focused_girl.SeenPanties = 1

        if not Player.focused_girl.Panties:
            call first_bottomless(Player.focused_girl, 1)

    $ Line = 0
    $ Cnt = 0

    if Player.primary_action == "finger_pussy":
        $ Speed = 2

    if Taboo:
        $ Player.focused_girl.DrainWord("tabno")

    # we have to fix DrainWord and AddWord to accept Player.primary_action
    $ Player.focused_girl.DrainWord("no_" + Player.primary_action)
    $ Player.focused_girl.AddWord(0, Player.primary_action, Player.primary_action)

    # we have to fix the launch functions to accept Player.primary_action
    if Player.primary_action in ["fondle_thighs", "fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
        if Player.focused_girl != EmmaX:
            call pussy_launch(Player.focused_girl, trigger = Player.primary_action)
        else:
            if Player.focused_girl.Pose in ["doggy", "sex"]:
                call ViewShift(Player.focused_girl, Player.focused_girl.Pose, 0, Player.primary_action)
            else:
                call ViewShift(Player.focused_girl, "pussy", 0, Player.primary_action)
    elif Player.primary_action in ["fondle_breasts", "suck_breasts"]:
        call breasts_launch(Player.focused_girl, trigger = Player.primary_action)

label fondle_cycle:
    if Player.primary_action in ["suck_breasts", "eat_pussy", "eat_ass"]:
        if Trigger2 == "kiss_you":
            $ Trigger2 = 0

    while Round > 0:

        # we have to fix ViewShift to accept Player.primary_action
        call Shift_Focus(RogueX)
        call ViewShift(Player.focused_girl, Player.focused_girl.Pose, 0, Player.primary_action)

        $ Player.focused_girl.LustFace()

        if Player.Focus < 100:
            jump fondle_menu

            label fondle_menu_return:

        if Player.primary_action in ["eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
            if Player.focused_girl.Panties or Player.focused_girl.PantsNum() >= 6 or Player.focused_girl.HoseNum() >= 5: #This checks if Rogue wants to strip down.
                call Girl_Undress(Player.focused_girl, "auto")

        call Shift_Focus(character)
        call Sex_Dialog(Player.focused_girl, Partner)

        $ Cnt += 1
        $ Round -= 1

        call end_of_fondle_round(Player.focused_girl, Player.primary_action)

        if _return:
            return

        if Player.primary_action in ["fondle_breasts", "suck_breasts"]:
            if Player.focused_girl.Lust >= 50 and not Player.focused_girl.Uptop and (Player.focused_girl.Chest or Player.focused_girl.Over):
                $ Player.focused_girl.Uptop = 1

                if Player.focused_girl == RogueX:
                    "[Player.focused_girl.Name] shrugs and pulls her top open."
                elif Player.focused_girl == KittyX:
                    "[KittyX.Name] laughs and pulls her top open."
                elif Player.focused_girl in [EmmaX, StormX]:
                    "[EmmaX.Name] sighs and tugs her breasts free of her clothes."
                elif Player.focused_girl in [LauraX, JeanX, JubesX]:
                    "[Player.focused_girl.Name] grunts and pulls her clothes aside."

                call first_topless

    $ Player.focused_girl.FaceChange("bemused", 0)

    $ Line = 0

    call im_done_lines

label after_fondle:
    if Player.primary_action in ["fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
        if not Situation:
            call reset_position(character)

    $ Player.focused_girl.FaceChange("sexy")
    $ Player.focused_girl.Action -= 1

    if Player.primary_action == "fondle_thighs":
        $ Player.focused_girl.FondleT += 1
    elif Player.primary_action == "fondle_breasts":
        $ Player.focused_girl.FondleB += 1
    elif Player.primary_action == "suck_breasts":
        $ Player.focused_girl.SuckB += 1
    elif Player.primary_action == "fondle_pussy":
        $ Player.focused_girl.FondleP += 1
    elif Player.primary_action == "finger_pussy":
        $ Player.focused_girl.InsertP += 1
    elif Player.primary_action == "eat_pussy":
        $ Player.focused_girl.LickP += 1
    elif Player.primary_action == "fondle_ass":
        $ Player.focused_girl.FondleA += 1
    elif Player.primary_action == "finger_ass":
        $ Player.focused_girl.InsertA += 1
    elif Player.primary_action == "eat_ass":
        $ Player.focused_girl.LickA += 1

    if Player.primary_action in ["fondle_thighs", "fondle_pussy", "eat_pussy", "fondle_ass"] and Player.focused_girl.PantsNum() < 6 or Player.focused_girl.Upskirt:
        $ Player.focused_girl.Addictionrate += 1

        if "addictive" in Player.Traits:
            $ Player.focused_girl.Addictionrate += 1

        if Player.primary_action == "fondle_thighs":
            call Partner_Like(Player.focused_girl, 1, 0)
        elif Player.primary_action == ["fondle_pussy", "fondle_ass"]:
            call Partner_Like(Player.focused_girl, 2)
        elif Player.primary_action == "eat_pussy":
            if Player.focused_girl == RogueX and Partner == EmmaX:
                call Partner_Like(Player.focused_girl,4,3)
            elif Player.focused_girl not in [KittyX, StormX] and Partner == RogueX:
                call Partner_Like(Player.focused_girl, 3, 3)
            elif Player.focused_girl == RogueX:
                call Partner_Like(Player.focused_girl,3,2)
            else:
                call Partner_Like(Player.focused_girl, 2)
    else:
        $ Player.focused_girl.Addictionrate += 1

        if "addictive" in Player.Traits:
            $ Player.focused_girl.Addictionrate += 1

        call Partner_Like(Player.focused_girl, 2)

    $ first_time_fondling_thighs = (Player.primary_action == "fondle_thighs" and Player.focused_girl.FondleT == 1)
    $ first_time_fondling_breasts = (Player.primary_action == "fondle_breasts" and Player.focused_girl.FondleB == 1)
    $ first_time_sucking_breasts = (Player.primary_action == "suck_breasts" and Player.focused_girl.SuckB == 1)
    $ first_time_fondling_pussy = (Player.primary_action == "fondle_pussy" and Player.focused_girl.FondleP == 1)
    $ first_time_fingering_pussy = (Player.primary_action == "finger_pussy" and Player.focused_girl.InsertP == 1)
    $ first_time_licking_pussy = (Player.primary_action == "eat_pussy" and Player.focused_girl.LickP == 1)
    $ first_time_fondling_ass = (Player.primary_action == "fondle_ass" and Player.focused_girl.FondleA == 1)
    $ first_time_fingering_ass = (Player.primary_action == "finger_ass" and Player.focused_girl.InsertA == 1)
    $ first_time_licking_ass = (Player.primary_action == "eat_ass" and Player.focused_girl.LickA == 1)

    if first_time_fondling_thighs or first_time_fondling_breasts or first_time_sucking_breasts or first_time_fondling_pussy or first_time_fingering_pussy or first_time_licking_pussy or first_time_fondling_ass or first_time_fingering_ass or first_time_licking_ass:
        if Player.primary_action == "fondle_thighs":
            $ Player.focused_girl.SEXP += 3
        elif Player.primary_action in ["fondle_breasts", "suck_breasts", "fondle_ass"]:
            $ Player.focused_girl.SEXP += 4
        elif Player.primary_action in ["fondle_pussy"]:
            $ Player.focused_girl.SEXP += 7
        elif Player.primary_action in ["finger_pussy", "eat_pussy"]:
            $ Player.focused_girl.SEXP += 10
        elif Player.primary_action in ["finger_ass"]:
            $ Player.focused_girl.SEXP += 12
        elif Player.primary_action in ["eat_ass"]:
            $ Player.focused_girl.SEXP += 15

        if not Situation:
            if Player.focused_girl.Love >= 500 and "unsatisfied" not in Player.focused_girl.RecentActions:
                call that_was_nice_lines(character)
            elif Player.focused_girl.Obed <= 500 and Player.Focus <= 20:
                $ Player.focused_girl.FaceChange("perplexed", 1)

                call was_that_enough_lines(character)

    $ temp_modifier = 0

    call Checkout

    if Situation:
        call Sex_Basic_Dialog(Player.focused_girl, "switch")
    else:
        call reset_position(character)

    return

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
                jump after_fondle

            $ Line = "came"

        if character.Lust >= 100:
            call Girl_Cumming

            if Situation == "shift" or "angry" in character.RecentActions:
                jump after_fondle

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

                        jump after_fondle

    if Partner and Partner.Lust >= 100:
        call Girl_Cumming(Partner)

    $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

    if character == "fondle_thighs":
        $ bonus = character.FondleT
    elif character == "fondle_breasts":
        $ bonus = character.FondleB
    elif character == "suck_breasts":
        $ bonus = character.SuckB
    elif character == "fondle_pussy":
        $ bonus = character.FondleP
    elif character == "finger_pussy":
        $ bonus = character.InsertP
    elif character == "eat_pussy":
        $ bonus = character.LickP
    elif character == "fondle_ass":
        $ bonus = character.FondleA
    elif character == "finger_ass":
        $ bonus = character.InsertA
    elif character == "eat_ass":
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

                jump after_fondle
            "Let's try something else." if MultiAction:
                $ Line = 0
                $ Situation = "shift"

                jump after_fondle
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

                    jump after_fondle

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

            jump before_fondle
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

        jump before_fondle
    elif "fondle_thighs" in character.RecentActions:
        $ character.FaceChange("sexy", 1)

        call repeat_action_lines(character)
        jump before_fondle
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

            jump before_fondle
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
        jump before_fondle
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

            jump before_fondle
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
        jump before_fondle
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

            jump before_fondle
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

        jump before_fondle
    elif "fondle_pussy" in character.RecentActions:
        $ character.FaceChange("sexy", 1)

        call repeat_action_lines(character)
        jump before_fondle
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

            jump before_fondle
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

            jump before_fondle
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

        jump before_fondle
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

            jump before_fondle
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

        jump before_fondle
    elif "fondle_ass" in character.RecentActions:
        $ character.FaceChange("sexy", 1)

        call repeat_action_lines(character)

        jump before_fondle
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

            jump before_fondle
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

            jump before_fondle
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
        jump before_fondle
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
