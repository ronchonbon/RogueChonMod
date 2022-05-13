label fondle_action(character):
    $ character.Mouth = "smile"

    if not character.Action:
        call out_of_action_lines(character)

        return

    if character == RogueX:
        character.voice "Well where exactly were you interested in touching, [character.Petname]?"
    elif character == KittyX:
        character.voice "Um, what did you want to touch, [character.Petname]?"
    elif character == EmmaX:
        character.voice "Well? Where did you want to touch, [character.Petname]?"
    elif character == LauraX:
        character.voice "Yeah? Like where?"
    elif character == JeanX:
        character.voice "Yeah? Like where?"
    elif character == StormX:
        character.voice "What did you wish to touch, [character.Petname]?"
    elif character == JubesX:
        character.voice "Where were you thinking?"

    menu:
        extend ""
        "Your breasts?" if character.Action:
            call fondle_breasts(character)
        "Suck on your breasts?" if character.Action and character.SuckB:
            call suck_breasts(character)
        "Your thighs?" if character.Action:
            call fondle_thighs(character)
        "Your pussy?" if character.Action:
            call fondle_pussy(character)
        "Lick your pussy?" if character.Action and character.LickP:
            call eat_pussy(character)
        "Your Ass?" if character.Action:
            call fondles_ass(character)
        "Eat your ass?" if character.Action and character.LickA:
            call eat_ass(character)
        "Never mind.":
            return

    return

label fondle_menu(character, action):
    menu:
        "Keep going. . .":
            pass
        "I want to stick a finger in. . ." if action == "fondle_pussy" and Speed != 2:
            if character.InsertP:
                $ Speed = 2
            else:
                menu:
                    "Ask her first":
                        $ Situation = "shift"
                    "Don't ask first [[just stick it in]":
                        $ Situation = "auto"

                call finger_pussy(character)
        "Pull back a bit. . ." if action == "fondle_pussy" and Speed != 2:
            $ Speed = 0
        "Slap her ass":
            call Slap_Ass(character)

            $ Cnt += 1
            $ Round -= 1

            call fondle_cycle(character, action)

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
            call ViewShift(character, "menu")
            call fondle_cycle(character, action)

            return
        "Other options":
            menu:
                "Offhand action":
                    if character.Action and MultiAction:
                        call Offhand_Set

                        if Trigger2:
                            $ character.Action -= 1
                    else:
                        call tired_lines(character)
                "Shift primary action":
                    if action == "fondle_thighs":
                        if MultiAction:
                            menu:
                                "Can I go a little deeper?":
                                    if character.Action:
                                        $ Situation = "shift"

                                        call after_fondle(character, action)
                                        call fondle_pussy(character)

                                        return
                                    else:
                                        call tired_lines(character)
                                "Shift your hands a bit higher without asking":
                                    if character.Action:
                                        $ Situation = "auto"

                                        call after_fondle(character, action)
                                        call fondle_pussy(character)

                                        return
                                    else:
                                        "As your hands creep upwards, she grabs your wrists."

                                        call tired_lines(character)
                                "Never Mind":
                                    pass

                            call fondle_cycle(character, action)

                            return
                        else:
                            call tired_lines(character)
                    elif action == "fondle_breasts":
                        if character.Action and MultiAction:
                            menu:
                                "Ask to suck on them.":
                                    if character.Action and MultiAction:
                                        $ Situation = "shift"

                                        call after_fondle(character, action)
                                        call suck_breasts(character)
                                    else:
                                        call tired_lines(character)
                                "Just suck on them without asking.":
                                    if character.Action and MultiAction:
                                        $ Situation = "auto"

                                        call after_fondle(character, action)
                                        call suck_breasts(character)
                                    else:
                                        "As you lean in to suck on her breast, she grabs your head and pushes back."

                                        call tired_lines(character)
                                "Never Mind":
                                    pass

                            call fondle_cycle(character, action)

                            return
                        else:
                            call tired_lines(character)
                    elif action == "suck_breasts":
                        if MultiAction:
                            menu:
                                "Pull back to fondling.":
                                    if character.Action and MultiAction:
                                        $ Situation = "pullback"

                                        call after_fondle(character, action)
                                        call fondle_breasts(character)
                                    else:
                                        "As you pull back, [character.Name] pushes you back in close."

                                        call tired_lines(character)
                                "Never Mind":
                                    pass

                            call fondle_cycle(character, action)

                            return
                        else:
                            call tired_lines(character)
                    elif action == "fondle_pussy":
                        if MultiAction:
                            menu:
                                "I want to lick your pussy.":
                                    if character.Action:
                                        $ Situation = "shift"

                                        call fondle_pussy_after(character)
                                        call eat_pussy(character)

                                        return
                                    else:
                                        call tired_lines(character)
                                "Just start licking":
                                    if character.Action:
                                        $ Situation = "auto"

                                        call fondle_pussy_after(character)
                                        call eat_pussy(character)

                                        return
                                    else:
                                        "As you lean in to lick her pussy, she grabs your head and pushes back."

                                        call tired_lines(character)
                                "Pull back to the thighs":
                                    if character.Action:
                                        $ Situation = "pullback"

                                        call fondle_pussy_after(character)
                                        call fondle_thighs(character)

                                        return
                                    else:
                                        "As you pull your hand back, [character.Name] pulls it back in close."

                                        call tired_lines(character)
                                "I want to stick a dildo in.":
                                    if character.Action:
                                        $ Situation = "shift"

                                        call fondle_pussy_after(character)
                                        call dildo_pussy(character)

                                        return
                                    else:
                                        call tired_lines(character)
                                "Never Mind":
                                    pass

                            call fondle_cycle(character, action)

                            return
                        else:
                            call tired_lines(character)
                    elif action == "eat_pussy":
                        if character.Action and MultiAction:
                            menu:
                                "Pull out and start rubbing again.":
                                    $ Situation = "pullback"

                                    call after_fondle(character, action)
                                    call fondle_pussy(character)
                                "I want to stick a dildo in.":
                                    $ Situation = "shift"

                                    call after_fondle(character, action)
                                    call dildo_pussy(character)
                                "Never Mind":
                                    pass

                            call fondle_cycle(character, action)

                            return
                        else:
                            call tired_lines(character)
                    elif action == "fondle_ass":
                        if character.Action and MultiAction:
                            menu:
                                "I want to stick a finger in.":
                                    $ Situation = "shift"

                                    call after_fondle(character, action)
                                    call finger_ass(character)
                                "Just stick a finger in without asking.":
                                    $ Situation = "auto"

                                    call after_fondle(character, action)
                                    call finger_ass(character)
                                "I want to lick your asshole.":
                                    $ Situation = "shift"

                                    call after_fondle(character, action)
                                    call eat_ass(character)
                                "Just start licking.":
                                    $ Situation = "auto"

                                    call after_fondle(character, action)
                                    call eat_ass(character)
                                "I want to stick a dildo in.":
                                    $ Situation = "shift"

                                    call after_fondle(character, action)
                                    call dildo_ass(character)
                                "Never Mind":
                                    pass

                            call fondle_cycle(character, action)

                            return
                    elif action == "finger_ass":
                        if character.Action and MultiAction:
                            menu:
                                "Pull out and start rubbing again.":
                                    $ Situation = "pullback"

                                    call after_fondle(character, action)
                                    call fondle_ass(character)
                                "I want to lick your asshole.":
                                    $ Situation = "shift"

                                    call after_fondle(character, action)
                                    call eat_ass(character)
                                "Just start licking.":
                                    $ Situation = "auto"

                                    call after_fondle(character, action)
                                    call eat_ass(character)
                                "I want to stick a dildo in.":
                                    $ Situation = "shift"

                                    call after_fondle(character, action)
                                    call dildo_ass(character)
                                "Never Mind":
                                    pass

                            call fondle_cycle(character, action)

                            return
                        else:
                            call tired_lines(character)
                    elif action == "eat_ass":
                        if character.Action and MultiAction:
                            menu:
                                "Switch to fondling.":
                                    $ Situation = "pullback"

                                    call after_fondle(character, action)
                                    call fondle_ass(character)
                                "I want to stick a finger in.":
                                    $ Situation = "shift"

                                    call after_fondle(character, action)
                                    call finger_ass(character)
                                "Just stick a finger in [[without asking].":
                                    $ Situation = "auto"

                                    call after_fondle(character, action)
                                    call finger_ass(character)
                                "I want to stick a dildo in.":
                                    $ Situation = "shift"

                                    call after_fondle(character, action)
                                    call dildo_ass(character)
                                "Never Mind":
                                    pass

                            call fondle_cycle(character, action)

                            return
                        else:
                            call tired_lines(character)
                "Shift your focus" if Trigger2:
                    $ Situation = "shift focus"

                    call after_fondle(character, action)
                    call Offhand_Set
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
                        "Don't stop what you're doing. . . (locked)" if not ThreeCount or not Trigger4:
                            $ ThreeCount = 0
                        "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                            $ ThreeCount = 0
                        "Swap to [Partner.Name]":
                            call Trigger_Swap(character)
                        "Undress [Partner.Name]":
                            call Girl_Undress(Partner)
                            call fondle_cycle(character, action)

                            return
                        "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                            pass
                        "Clean up [Partner.Name]" if Partner.Spunk:
                            call Girl_Cleanup(Partner,"ask")
                            call fondle_cycle(character, action)

                            return
                        "Never mind":
                            call fondle_cycle(character, action)

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
                    call fondle_cycle(character, action)

                    return
        "Back to Sex Menu" if MultiAction:
            ch_p "Let's try something else."

            call reset_position(character)

            $ Situation = "shift"
            $ Line = 0

            call after_fondle(character, action)

            return
        "End Scene" if not MultiAction:
            ch_p "Let's stop for now."

            call reset_position(character)

            $ Line = 0

            call after_fondle(character, action)

            return

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

label before_fondle(character, action):
    if action not in ["suck_breasts", "fondle_pussy"]:
        if Trigger == "kiss_you":
            $ Trigger = action

            return

    if action != "finger_pussy" and Trigger2 == action:
        return

    # we have to fix the launch functions to accept action
    if action in ["fondle_thighs", "fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
        if character != EmmaX:
            call pussy_launch(character, trigger = action)
        else:
            if character.Pose in ["doggy", "sex"]:
                call ViewShift(character, character.Pose, 0, action)
            else:
                call ViewShift(character, "pussy", 0, action)
    elif action in ["fondle_breasts", "suck_breasts"]:
        call breasts_launch(character, trigger = action)

    if Situation == character:
        $ Situation = 0

        call character_initiated_action(character, action)

        if _return:
            return

    if not character.Forced and Situation != "auto":
        $ temp_modifier = 0

        if action in ["eat_pussy", "eat_ass"] and character.PantsNum() >= 6:
            $ temp_modifier = 15

        if action in ["fondle_thighs", "fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
            call Bottoms_Off(character)
        elif action in ["fondle_breasts", "suck_breasts"]:
            call Top_Off(character)
        elif action == "finger_pussy":
            call Girl_Undress(character, "bottom")

        if "angry" in character.RecentActions:
            return

    $ temp_modifier = 0

    if action == "fondle_thighs" and not character.FondleT:
        if character.Forced:
            $ character.Statup("Love", 90, -10)
            $ character.Statup("Obed", 70, 15)
            $ character.Statup("Inbt", 80, 10)
        else:
            $ character.Statup("Love", 90, 5)
            $ character.Statup("Obed", 70, 10)
            $ character.Statup("Inbt", 80, 15)
    elif action == "fondle_breasts" and not character.FondleB:
        if character.Forced:
            $ character.Statup("Love", 90, -20)
            $ character.Statup("Obed", 70, 25)
            $ character.Statup("Inbt", 80, 15)
        else:
            $ character.Statup("Love", 90, 10)
            $ character.Statup("Obed", 70, 5)
            $ character.Statup("Inbt", 80, 15)
    elif action == "suck_breasts" and not character.SuckB:
        if character.Forced:
            $ character.Statup("Love", 90, -25)
            $ character.Statup("Obed", 70, 25)
            $ character.Statup("Inbt", 80, 17)
        else:
            $ character.Statup("Love", 90, 10)
            $ character.Statup("Obed", 70, 10)
            $ character.Statup("Inbt", 80, 15)
    elif action == "fondle_pussy" and not character.FondleP:
        if character.Forced:
            $ character.Statup("Love", 90, -50)
            $ character.Statup("Obed", 70, 35)
            $ character.Statup("Inbt", 80, 25)
        else:
            $ character.Statup("Love", 90, 10)
            $ character.Statup("Obed", 70, 10)
            $ character.Statup("Inbt", 80, 15)
    elif action == "finger_pussy" and not character.InsertP:
        if character.Forced:
            $ character.Statup("Love", 90, -60)
            $ character.Statup("Obed", 70, 55)
            $ character.Statup("Inbt", 80, 35)
        else:
            $ character.Statup("Love", 90, 10)
            $ character.Statup("Obed", 70, 20)
            $ character.Statup("Inbt", 80, 25)
    if action == "eat_pussy" and not character.LickP:
        if character.Forced:
            $ character.Statup("Love", 90, -30)
            $ character.Statup("Obed", 70, 35)
            $ character.Statup("Inbt", 80, 75)
        else:
            $ character.Statup("Love", 90, 35)
            $ character.Statup("Obed", 70, 15)
            $ character.Statup("Inbt", 80, 35)
    elif action == "fondle_ass" and not character.FondleA:
        if character.Forced:
            $ character.Statup("Love", 90, -20)
            $ character.Statup("Obed", 70, 20)
            $ character.Statup("Inbt", 80, 15)
        else:
            $ character.Statup("Love", 90, 10)
            $ character.Statup("Obed", 70, 12)
            $ character.Statup("Inbt", 80, 20)
    elif action == "finger_ass" and not character.InsertA:
        if character.Forced:
            $ character.Statup("Love", 90, -50)
            $ character.Statup("Obed", 70, 60)
            $ character.Statup("Inbt", 80, 35)
        else:
            $ character.Statup("Love", 90, 10)
            $ character.Statup("Obed", 70, 20)
            $ character.Statup("Inbt", 80, 25)
    elif action == "eat_ass" and not character.LickA:
        if character.Forced:
            $ character.Statup("Love", 90, -30)
            $ character.Statup("Obed", 70, 40)
            $ character.Statup("Inbt", 80, 80)
        else:
            $ character.Statup("Love", 90, 35)
            $ character.Statup("Obed", 70, 25)
            $ character.Statup("Inbt", 80, 55)

    if Taboo:
        if action == "fondle_thighs":
            $ character.Statup("Lust", 200, (int(Taboo/5)))
            $ character.Statup("Inbt", 200, (2*(int(Taboo/5))))
        elif action in ["fondle_breasts", "suck_breasts", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass"]:
            $ character.Inbt += int(Taboo/10)
            $ character.Lust += int(Taboo/5)
        elif action in ["fondle_pussy", "eat_pussy", "finger_ass", "eat_ass"]:
            if character == JeanX and character.Taboo:
                $ character.Statup("Inbt", 200, (int(Taboo/10)))
            elif Taboo:
                $ character.Inbt += int(Taboo/10)

            $ character.Lust += int(Taboo/5)

    if Situation:
        #$ renpy.pop_call()

        $ Situation = 0

    if action in ["eat_pussy", "eat_ass"]:
        if character.PantsNum() == 5:
            $ character.Upskirt = 1
            $ character.SeenPanties = 1

        if not character.Panties:
            call first_bottomless(character, 1)

    $ Line = 0
    $ Cnt = 0

    if action == "finger_pussy":
        $ Speed = 2

    if Taboo:
        $ character.DrainWord("tabno")

    # we have to fix DrainWord and AddWord to accept action
    $ character.DrainWord("no_" + action)
    $ character.AddWord(0, action, action)

    # we have to fix the launch functions to accept action
    if action in ["fondle_thighs", "fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
        if character != EmmaX:
            call pussy_launch(character, trigger = action)
        else:
            if character.Pose in ["doggy", "sex"]:
                call ViewShift(character, character.Pose, 0, action)
            else:
                call ViewShift(character, "pussy", 0, action)
    elif action in ["fondle_breasts", "suck_breasts"]:
        call breasts_launch(character, trigger = action)

    call fondle_cycle(character, action)

    return

label fondle_cycle(character, action):
    if action in ["suck_breasts", "eat_pussy", "eat_ass"]:
        if Trigger2 == "kiss_you":
            $ Trigger2 = 0

    while Round > 0:

        # we have to fix ViewShift to accept action
        call ViewShift(character, character.Pose, 0, action)
        call Shift_Focus(character)

        $ character.LustFace()

        if Player.Focus < 100:
            call fondle_menu(character, action)

        if action in ["eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
            if character.Panties or character.PantsNum() >= 6 or character.HoseNum() >= 5: #This checks if Rogue wants to strip down.
                call Girl_Undress(character, "auto")

        call Shift_Focus(character)
        call Sex_Dialog(character, Partner)

        $ Cnt += 1
        $ Round -= 1

        call end_of_fondle_round(character, action)

        if _return:
            return

        if action in ["fondle_breasts", "suck_breasts"]:
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

    call im_done_lines(character)
    call after_fondle(character, action)

    return

label after_fondle(character, action):
    if action in ["fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
        if not Situation:
            call reset_position(character)

    $ character.FaceChange("sexy")
    $ character.Action -= 1

    if action == "fondle_thighs":
        $ character.FondleT += 1
    elif action == "fondle_breasts":
        $ character.FondleB += 1
    elif action == "suck_breasts":
        $ character.SuckB += 1
    elif action == "fondle_pussy":
        $ character.FondleP += 1
    elif action == "finger_pussy":
        $ character.InsertP += 1
    elif action == "eat_pussy":
        $ character.LickP += 1
    elif action == "fondle_ass":
        $ character.FondleA += 1
    elif action == "finger_ass":
        $ character.InsertA += 1
    elif action == "eat_ass":
        $ character.LickA += 1

    if action in ["fondle_thighs", "fondle_pussy", "eat_pussy", "fondle_ass"] and character.PantsNum() < 6 or character.Upskirt:
        $ character.Addictionrate += 1

        if "addictive" in Player.Traits:
            $ character.Addictionrate += 1

        if action == "fondle_thighs":
            call Partner_Like(character, 1, 0)
        elif action == ["fondle_pussy", "fondle_ass"]:
            call Partner_Like(character, 2)
        elif action == "eat_pussy":
            if character == RogueX and Partner == EmmaX:
                call Partner_Like(character,4,3)
            elif character not in [KittyX, StormX] and Partner == RogueX:
                call Partner_Like(character, 3, 3)
            elif character == RogueX:
                call Partner_Like(character,3,2)
            else:
                call Partner_Like(character, 2)
    else:
        $ character.Addictionrate += 1

        if "addictive" in Player.Traits:
            $ character.Addictionrate += 1

        call Partner_Like(character, 2)

    $ first_time_fondling_thighs = (action == "fondle_thighs" and character.FondleT == 1)
    $ first_time_fondling_breasts = (action == "fondle_breasts" and character.FondleB == 1)
    $ first_time_sucking_breasts = (action == "suck_breasts" and character.SuckB == 1)
    $ first_time_fondling_pussy = (action == "fondle_pussy" and character.FondleP == 1)
    $ first_time_fingering_pussy = (action == "finger_pussy" and character.InsertP == 1)
    $ first_time_licking_pussy = (action == "eat_pussy" and character.LickP == 1)
    $ first_time_fondling_ass = (action == "fondle_ass" and character.FondleA == 1)
    $ first_time_fingering_ass = (action == "finger_ass" and character.InsertA == 1)
    $ first_time_licking_ass = (action == "eat_ass" and character.LickA == 1)

    if first_time_fondling_thighs or first_time_fondling_breasts or first_time_sucking_breasts or first_time_fondling_pussy or first_time_fingering_pussy or first_time_licking_pussy or first_time_fondling_ass or first_time_fingering_ass or first_time_licking_ass:
        if action == "fondle_thighs":
            $ character.SEXP += 3
        elif action in ["fondle_breasts", "suck_breasts", "fondle_ass"]:
            $ character.SEXP += 4
        elif action in ["fondle_pussy"]:
            $ character.SEXP += 7
        elif action in ["finger_pussy", "eat_pussy"]:
            $ character.SEXP += 10
        elif action in ["finger_ass"]:
            $ character.SEXP += 12
        elif action in ["eat_ass"]:
            $ character.SEXP += 15

        if not Situation:
            if character.Love >= 500 and "unsatisfied" not in character.RecentActions:
                call that_was_nice_lines(character)
            elif character.Obed <= 500 and Player.Focus <= 20:
                $ character.FaceChange("perplexed", 1)

                call was_that_enough_lines(character)

    $ temp_modifier = 0

    call Checkout

    if Situation:
        call Sex_Basic_Dialog(character, "switch")
    else:
        call reset_position(character)

    return

label end_of_fondle_round(character, action):
    $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus

    if Player.Focus >= 100 or character.Lust >= 100:
        if Player.Focus >= 100:
            call Player_Cumming(character)

            if "angry" in character.RecentActions:
                call reset_position(character)

                return True

            $ character.Statup("Lust", 200, 5)

            if 100 > character.Lust >= 70 and character.OCount < 2 and character.SEXP >= 20:
                $ character.AddWord(0, "unsatisfied", "unsatisfied")

            if Player.Focus > 80:
                call after_fondle(character, action)

                return True

            $ Line = "came"

        if character.Lust >= 100:
            call Girl_Cumming(character)

            if Situation == "shift" or "angry" in character.RecentActions:
                call after_fondle(character, action)

                return True

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

                        call after_fondle(character, action)

                        return True

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

                call after_fondle(character, action)

                return True
            "Let's try something else." if MultiAction:
                $ Line = 0
                $ Situation = "shift"

                call after_fondle(character, action)

                return True
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

                    call after_fondle(character, action)

                    return True

    call Escalation(character)

    if Round == 10:
        call wrap_this_up_lines(character)
    elif Round == 5:
        call time_to_stop_soon_lines(character)

    return False

label fondle_thighs(character):
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

            call before_fondle(character, "fondle_thighs")

            return
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

        call before_fondle(character, "fondle_thighs")

        return
    elif "fondle_thighs" in character.RecentActions:
        $ character.FaceChange("sexy", 1)

        call repeat_action_lines(character)
        call before_fondle(character, "fondle_thighs")

        return
    elif "fondle_thighs" in character.DailyActions:
        $ character.FaceChange("sexy", 1)

        call gently_lines(character)

    if Approval >= 2:
        call action_accepted(character)

        return
    else:
        call action_disapproved(character, "fondle_thighs", character.FondleT)

    call action_rejected(character, "fondle_thighs", character.FondleT)

    return

label fondle_breasts(character):
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

            call before_fondle(character, "fondle_breasts")

            return
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
        call before_fondle(character, "fondle_breasts")

        return
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

            call before_fondle(character, "suck_breasts")

            return
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
        call before_fondle(character, "suck_breasts")

        return
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

            call before_fondle(character, "fondle_pussy")

            return
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

        call before_fondle(character, "fondle_pussy")

        return
    elif "fondle_pussy" in character.RecentActions:
        $ character.FaceChange("sexy", 1)

        call repeat_action_lines(character)
        call before_fondle(character, "fondle_pussy")

        return
    elif "fondle_pussy" in character.DailyActions:
        $ character.FaceChange("sexy", 1)

        call gently_lines(character)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(character, "fondle_pussy")

        return
    else:
        call action_disapproved(character, action, character.FondleP)

    call action_rejected(character, "fondle_pussy", character.FondleP)

    return

label finger_pussy(character):
    call Shift_Focus(character)

    if Situation == "auto":                                                                  #You auto-start
        if ApprovalCheck(character, 1100, TabM = 2):
            $ character.FaceChange("surprised")
            $ character.Statup("Obed", 90, 1)
            $ character.Statup("Obed", 70, 2)
            $ character.Statup("Inbt", 70, 3)
            $ character.Statup("Inbt", 30, 2)

            "As you slide a finger in, [character.Name] seems a bit surprised, but seems into it."

            call before_fondle(character, "finger_pussy")

            return
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

            call before_fondle(character, "eat_pussy")

            return
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

        call before_fondle(character, "eat_pussy")

        return
    elif "eat_pussy" in character.DailyActions:
        $ character.FaceChange("sexy", 1)

        call gently_lines(character)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(character, "eat_pussy")

        return
    else:
        call action_disapproved(character, action, character.LickP)

    call action_rejected(character, "eat_pussy", character.LickP)

label fondle_ass(character):
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

            call before_fondle(character, "fondle_ass")

            return
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

        call before_fondle(character, "fondle_ass")

        return
    elif "fondle_ass" in character.RecentActions:
        $ character.FaceChange("sexy", 1)

        call repeat_action_lines(character)

        call before_fondle(character, "fondle_ass")

        return
    elif "fondle_ass" in character.DailyActions:
        $ character.FaceChange("sexy", 1)

        call gently_lines(character)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(character, "fondle_ass")

        return
    else:
        call action_disapproved(character, action, character.FondleA)

    call action_rejected(character, "fondle_ass", character.FondleA)

    return

label finger_ass(character):
    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(character)
    call fondle_set_modifier(character, action)

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

            call before_fondle(character, "finger_ass")

            return
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

            call before_fondle(character, "eat_ass")

            return
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
        call before_fondle(character, "eat_ass")

        return
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
