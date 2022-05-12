label handjob_menu(character, action):
    menu:
        "Keep going. . ." if Speed:
            pass
        "Start moving? . ." if action in ["handjob", "footjob", "titjob"] and not Speed:
            $ Speed = 1
        "Speed up. . ." if action in ["handjob", "footjob", "titjob"] and Speed < 2:
            $ Speed = 2

            "You ask her to up the pace a bit."
        "Speed up. . . (locked)" if action in ["handjob", "footjob", "titjob"] and Speed >= 2:
            pass
        "Slow Down. . ." if action in ["handjob", "footjob", "titjob"] and Speed:
            $ Speed -= 1

            "You ask her to slow it down a bit."
        "Slow Down. . . (locked)" if action in ["handjob", "footjob", "titjob"] and not Speed:
            pass
        "Lick it. . ." if action == "blowjob" and Speed != 1:
            $ Speed = 1
        "Lick it. . . (locked)" if action == "blowjob" and Speed == 1:
            pass
        "Just the head. . ." if action == "blowjob" and Speed != 2:
            $ Speed = 2
        "Just the head. . . (locked)" iif action == "blowjob" and Speed == 2:
            pass
        "Suck on it." if action == "blowjob" and Speed != 3:
            $ Speed = 3

            if Trigger2 == "jackin":
                "She dips her head a bit lower, and you move your hand out of the way."
        "Suck on it. (locked)" if action == "blowjob" and Speed == 3:
            pass
        "Take it deeper." if action == "blowjob" and Speed != 4:
            if "pushed" not in character.RecentActions and character.Blow < 5:
                $ character.Statup("Love", 80, -(20 - 2*character.Blow))
                $ character.Statup("Obed", 80, 30 - 3*character.Blow)
                $ character.RecentActions.append("pushed")

            if Trigger2 == "jackin" and Speed != 3:
                "She takes it to the root, and you move your hand out of the way."

            $ Speed = 4
        "Take it deeper. (locked)" if action == "blowjob" and Speed == 4:
            pass
        "Set your own pace. . ." if action == "blowjob":
            "[character.Name] hums contentedly."

            if "setpace" not in character.RecentActions:
                $ character.Statup("Love", 80, 2)

            $ D20 = renpy.random.randint(1, 20)

            if character.Blow < 5:
                $ D20 -= 10
            elif character.Blow < 10:
                $ D20 -= 5

            if D20 > 15:
                $ Speed = 4

                if "setpace" not in character.RecentActions:
                    $ character.Statup("Inbt", 80, 3)
            elif D20 > 10:
                $ Speed = 3
            elif D20 > 5:
                $ Speed = 2
            else:
                $ Speed = 1

            $ character.RecentActions.append("setpace")
        "Slap her ass. . ." if action in ["dildo_pussy", "dildo_ass"]:
            call Slap_Ass(character)

            $ Cnt += 1
            $ Round -= 1

            call handjob_cycle(character, action)

            return
        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
            pass
        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
            "You concentrate on not burning out too quickly."

            $ Player.FocusX = 1
        "Release your focus." if Player.FocusX:
            "You release your concentration. . ."

            $ Player.FocusX = 0
        "Turn her around." if action == "footjob":
            $ character.Pose = "doggy" if character.Pose != "doggy" else "sex"

            "You turn her around. . ."

            call handjob_cycle(character, action)

            return
        "View" if action in ["dildo_pussy", "dildo_ass"]:
            call ViewShift(character, "menu")
            call handjob_cycle(character, action)

            return
        "Other options":
                menu:
                    "I also want to fondle her breasts." if Trigger2 != "fondle breasts":
                        if character.Action and MultiAction:
                            $ Trigger2 = "fondle breasts"

                            "You start to fondle her breasts."

                            $ character.Action -= 1
                        else:
                            call tired_lines(character)
                    "Offhand action" if action in ["footjob", "dildo_pussy", "dildo_ass"]:
                        if character.Action and MultiAction:
                            call Offhand_Set

                            if Trigger2:
                                $ character.Action -= 1
                        else:
                            call tired_lines(character)
                    "Shift primary action":
                        if character.Action and MultiAction:
                            menu:
                                "How about a handy?" if action in ["footjob", "titjob", "blowjob"]:
                                    if character.Action and MultiAction:
                                        $ Situation = "shift"

                                        call Rogue_TJ_After
                                        call Rogue_Handjob
                                    else:
                                        call tired_lines(character)
                                "How about a footjob?" if action in ["handjob", "titjob", "blowjob"]:
                                    if character.Action and MultiAction:
                                        $ Situation = "shift"

                                        call Rogue_TJ_After
                                        call Rogue_Footjob
                                    else:
                                        call tired_lines(character)
                                "How about a titjob?" if action in ["handjob", "footjob", "blowjob"]:
                                    if character.Action and MultiAction:
                                        $ Situation = "shift"

                                        call Rogue_HJ_After
                                        call Rogue_Titjob
                                    else:
                                        call tired_lines(character)
                                "How about a blowjob?" if action in ["handjob", "footjob", "titjob"]:
                                    if character.Action and MultiAction:
                                        $ Situation = "shift"

                                        call Rogue_HJ_After
                                        call Rogue_Blowjob
                                    else:
                                        call tired_lines(character)
                                "I want to stick a finger in her ass." if action == "dildo_pussy":
                                    if character.Action and MultiAction:
                                        $ Situation = "shift"

                                        call Rogue_DP_After
                                        call finger_ass(character)
                                    else:
                                        call tired_lines(character)
                                "Just stick a finger in her ass without asking." if action == "dildo_pussy":
                                    if character.Action and MultiAction:
                                        $ Situation = "auto"

                                        call Rogue_DP_After
                                        call finger_ass(character)
                                    else:
                                        call tired_lines(character)
                                "I want to shift the dildo to her ass." if action == "dildo_pussy":
                                    if character.Action and MultiAction:
                                        $ Situation = "shift"

                                        call Rogue_DP_After
                                        call Rogue_Dildo_Ass
                                    else:
                                        call tired_lines(character)
                                "I want to stick a finger in her pussy." if action == "dildo_ass":
                                    if character.Action and MultiAction:
                                        $ Situation = "shift"

                                        call Rogue_DA_After
                                        call finger_pussy(character)
                                    else:
                                        call tired_lines(character)
                                "Just stick a finger in her pussy without asking." if action == "dildo_ass":
                                    if character.Action and MultiAction:
                                        $ Situation = "auto"

                                        call Rogue_DA_After
                                        call finger_pussy(character)
                                    else:
                                        call tired_lines(character)
                                "I want to shift the dildo to her pussy." if action == "dildo_ass":
                                    if character.Action and MultiAction:
                                        $ Situation = "shift"

                                        call Rogue_DA_After
                                        call Rogue_Dildo_Pussy
                                    else:
                                        call tired_lines(character)
                                "Never Mind":
                                    call handjob_cycle(character, action)

                                    return
                        else:
                            call tired_lines(character)
                    "Shift your focus." if action in ["dildo_pussy", "dildo_ass"] and Trigger2:
                        $ Situation = "shift focus"

                        call after_handjob(character, action)
                        call Offhand_Set
                    "Shift your focus. (locked)" if action in ["dildo_pussy", "dildo_ass"] and not Trigger2:
                        pass
                    "Threesome actions (locked)" if not Partner:
                        pass
                    "Threesome actions" if Partner:
                        menu:
                            "Ask [character.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                call Les_Change(RogueX)
                            "Ask [character.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                pass
                            "Ask [Partner.Name] to do something else":
                                call Three_Change(RogueX)
                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                $ ThreeCount = 0
                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                $ ThreeCount = 0
                            "Swap to [Partner.Name]":
                                call Trigger_Swap(RogueX)
                            "Undress [Partner.Name]":
                                call Girl_Undress(Partner)
                                call handjob_cycle(character, action)

                                return
                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                pass
                            "Clean up [Partner.Name]" if Partner.Spunk:
                                call Girl_Cleanup(Partner,"ask")
                                call handjob_cycle(character, action)

                                return
                            "Never mind":
                                call handjob_cycle(character, action)

                                return
                    "Undress [character.Name]":
                        call Girl_Undress(RogueX)
                    "Clean up [character.Name] (locked)" if not character.Spunk:
                        pass
                    "Clean up [character.Name]" if character.Spunk:
                        call Girl_Cleanup(RogueX,"ask")
                    "Never mind":
                        call handjob_cycle(character, action)

                        return
        "Back to Sex Menu" if MultiAction:
            ch_p "Let's try something else."

            call handjob_reset(character)

            $ Situation = "shift"
            $ Line = 0

            call after_handjob(character, action)

            return
        "End Scene" if not MultiAction:
            ch_p "Let's stop for now."

            call handjob_reset(character)

            $ Line = 0

            call after_handjob(character, action)

            return

    return

label handjob_set_modifier(character, action):
    if action == "handjob":
        if character.Hand >= 7: # She loves it
            $ temp_modifier += 10
        elif character.Hand >= 3: #You've done it before several times
            $ temp_modifier += 7
        elif character.Hand: #You've done it before
            $ temp_modifier += 3

        if "exhibitionist" in character.Traits:
            $ temp_modifier += (3*Taboo)

        if character in Player.Harem or "sex friend" in character.Petnames:
            $ temp_modifier += 10
        elif "ex" in character.Traits:
            $ temp_modifier -= 40

        if character.Addict >= 75 and character.Swallow >= 3: #She's really strung out and has swallowed
            $ temp_modifier += 15
        if character.Addict >= 75:
            $ temp_modifier += 5

        if Situation == "shift":
            $ temp_modifier += 15
    elif action == "footjob":
        if character.Foot >= 7: # She loves it
            $ temp_modifier += 10
        elif character.Foot >= 3: #You've done it before several times
            $ temp_modifier += 7
        elif character.Foot: #You've done it before
            $ temp_modifier += 3

        if character.Addict >= 75 and character.Swallow >=3: #She's really strung out and has swallowed
            $ temp_modifier += 10
        if character.Addict >= 75:
            $ temp_modifier += 5

        if Situation == "shift":
            $ temp_modifier += 15
        if "exhibitionist" in character.Traits:
            $ temp_modifier += (3*Taboo)
        if character in Player.Harem or "sex friend" in character.Petnames:
            $ temp_modifier += 10
        elif "ex" in character.Traits:
            $ temp_modifier -= 40
    elif action == "titjob":
        if character.Tit >= 7: # She loves it
            $ temp_modifier += 10
        elif character.Tit >= 3: #You've done it before several times
            $ temp_modifier += 7
        elif character.Tit: #You've done it before
            $ temp_modifier += 5

        if character.SeenChest and ApprovalCheck(character, 500): # You've seen her tits.
            $ temp_modifier += 10
        if not character.Chest and not character.Over: #She's already topless
            $ temp_modifier += 10

        if "exhibitionist" in character.Traits:
            $ temp_modifier += (5*Taboo)

        if character in Player.Harem or "sex friend" in character.Petnames:
            $ temp_modifier += 10
        elif "ex" in character.Traits:
            $ temp_modifier -= 30

        if character.Lust > 75: #She's really horny
            $ temp_modifier += 10

        if character.Addict >= 75 and character.Swallow >= 3: #She's really strung out and has swallowed
            $ temp_modifier += 15
        if character.Addict >= 75:
            $ temp_modifier += 5

        if Situation == "shift":
            $ temp_modifier += 15
    elif action == "blowjob":
        if character.Blow >= 7: # She loves it
            $ temp_modifier += 15
        elif character.Blow >= 3: #You've done it before several times
            $ temp_modifier += 10
        elif character.Blow: #You've done it before
            $ temp_modifier += 7

        if character.Addict >= 75 and character.Swallow >=3: #She's really strung out and has swallowed
            $ temp_modifier += 25
        elif character.Addict >= 75: #She's really strung out
            $ temp_modifier += 15

        if "exhibitionist" in character.Traits:
            $ temp_modifier += (4*Taboo)
        if character in Player.Harem or "sex friend" in character.Petnames:
            $ temp_modifier += 10
        elif "ex" in character.Traits:
            $ temp_modifier -= 40

        if Situation == "shift":
            $ temp_modifier += 15
    elif action == "dildo_pussy":
        if character.DildoP: #You've done it before
            $ temp_modifier += 15
        if character.PantsNum() > 6: # she's got pants on.
            $ temp_modifier -= 20

        if character.Lust > 95:
            $ temp_modifier += 20
        elif character.Lust > 85: #She's really horny
            $ temp_modifier += 15

        if Situation == "shift":
            $ temp_modifier += 10
        if "exhibitionist" in character.Traits:
            $ temp_modifier += (5*Taboo)
        if character in Player.Harem or "sex friend" in character.Petnames:
            $ temp_modifier += 10
        elif "ex" in character.Traits:
            $ temp_modifier -= 40
    elif action == "dildo_ass":
        if character.Loose:
            $ temp_modifier += 30
        elif "anal" in character.RecentActions or "dildo anal" in character.RecentActions:
            $ temp_modifier -= 20
        elif "anal" in character.DailyActions or "dildo anal" in character.DailyActions:
            $ temp_modifier -= 10
        elif (character.Anal + character.DildoA + character.Plug) > 0: #You've done it before
            $ temp_modifier += 20

        if character.PantsNum() > 6: # she's got pants on.
            $ temp_modifier -= 20

        if character.Lust > 95:
            $ temp_modifier += 20
        elif character.Lust > 85: #She's really horny
            $ temp_modifier += 15

        if Situation == "shift":
            $ temp_modifier += 10
        if "exhibitionist" in character.Traits:
            $ temp_modifier += (5*Taboo)
        if character in Player.Harem or "sex friend" in character.Petnames:
            $ temp_modifier += 10
        elif "ex" in character.Traits:
            $ temp_modifier -= 40

    if character.ForcedCount and not character.Forced:
        $ temp_modifier -= 5*character.ForcedCount

    if Taboo and "tabno" in character.DailyActions:
        $ temp_modifier -= 10

    if "no_" + action in character.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no_" + action in character.RecentActions else 0

    return

label before_handjob(character, action):
    if Trigger2 == action:
        return

    if Taboo:
        $ character.Inbt += int(Taboo/10)
        $ character.Lust += int(Taboo/5)

    $ character.FaceChange("sexy")

    if action in ["handjob", "footjob", "titjob", "blowjob"]:
        if character.Forced:
            $ character.FaceChange("sad")
        elif not character.Hand:
            $ character.Brows = "confused"
            $ character.Eyes = "sexy"
            $ character.Mouth = "smile"
    elif action in ["dildo_pussy", "dildo_ass"]:
        if not character.Forced and Situation != "auto":
            if action == "dildo_pussy":
                $ temp_modifier = 15 if character.PantsNum() > 6 else 0
            elif action == "dildo_ass":
                $ temp_modifier = 20 if character.PantsNum() > 6 else 0

            call Bottoms_Off(character)

            if "angry" in character.RecentActions:
                return

        $ temp_modifier = 0

    call Seen_First_Peen(character, Partner, React = Situation)

    if action == "handjob":
        call handjob_launch(character, "L")
    elif action == "footjob":
        call sex_launch(character, "foot")
    elif action == "titjob":
        call titjob_launch(character, "L")
    elif action == "blowjob":
        call blowjob_launch(character, "L")
    elif action in ["dildo_pussy", "dildo_ass"]:
        call pussy_launch(character, action)

    if action in ["handjob", "titjob", "blowjob"]:
        if Situation == character:
            $ Situation = 0

            if action == "handjob":
                if Trigger2 == "jackin":
                    "[character.Name] brushes your hand aside and starts stroking your cock."
                else:
                    "[character.Name] gives you a mischevious smile, and starts to fondle your cock."
            elif action == "titjob":
                "[character.Name] slides down and sandwiches your dick between her tits."
            elif action == "blowjob":
                "[character.Name] slides down and gives your cock a little lick."

            if action == "handjob":
                $ action_line = "[character.Name] continues her actions."
                $ praise_line = "Oooh, that's good, [character.Pet]."
                $ reject_line = "Let's not do that for now, [character.Pet]."
                $ rejection_response_line = "[character.Name] puts it down."
            elif action == "titjob":
                $ action_line = "[character.Name] starts to slide them up and down."
                $ praise_line = "Oh, that sounds like a good idea, [character.Pet]."
                $ reject_line = "Let's not do that for now, [character.Pet]."
                $ rejection_response_line = "[character.Name] lets it drop out from between her breasts."
            elif action == "blowjob":
                $ action_line = "[character.Name] continues licking at it."
                $ praise_line = "Hmmm, keep doing that, [character.Pet]."
                $ reject_line = "Let's not do that for now, [character.Pet]."
                $ rejection_response_line = "[character.Name] puts it down."

            menu:
                "What do you do?"
                "Nothing.":
                    $ character.Statup("Inbt", 70, 3)
                    $ character.Statup("Inbt", 30, 2)

                    "[action_line]"
                "Praise her.":
                    $ character.FaceChange("sexy", 1)
                    $ character.Statup("Inbt", 70, 3)

                    ch_p "[praise_line]"

                    $ character.NameCheck() #checks reaction to petname

                    "[action_line]"

                    $ character.Statup("Love", 80, 1)
                    $ character.Statup("Obed", 90, 1)
                    $ character.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ character.FaceChange("surprised")
                    $ character.Statup("Inbt", 70, 1)

                    ch_p "[reject_line]"

                    $ character.NameCheck() #checks reaction to petname

                    "[rejection_response_line]"

                    $ character.Statup("Obed", 90, 1)
                    $ character.Statup("Obed", 50, 1)
                    $ character.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ character.AddWord(1,"refused","refused")

                    return

    if action == "handjob" and not character.Hand:
        if character.Forced:
            $ character.Statup("Love", 90, -20)
            $ character.Statup("Obed", 70, 25)
            $ character.Statup("Inbt", 80, 30)
        else:
            $ character.Statup("Love", 90, 5)
            $ character.Statup("Obed", 70, 20)
            $ character.Statup("Inbt", 80, 20)
    elif action == "footjob" and not character.Foot:
        if character.Forced:
            $ character.Statup("Love", 90, -20)
            $ character.Statup("Obed", 70, 25)
            $ character.Statup("Inbt", 80, 30)
        else:
            $ character.Statup("Love", 90, 5)
            $ character.Statup("Obed", 70, 20)
            $ character.Statup("Inbt", 80, 20)
    elif action == "titjob" and not character.Tit:
        if character.Forced:
            $ character.Statup("Love", 90, -25)
            $ character.Statup("Obed", 70, 30)
            $ character.Statup("Inbt", 80, 35)
        else:
            $ character.Statup("Love", 90, 5)
            $ character.Statup("Obed", 70, 25)
            $ character.Statup("Inbt", 80, 30)
    elif action == "blowjob" and not character.Blow:
        if character.Forced:
            $ character.Statup("Love", 90, -70)
            $ character.Statup("Obed", 70, 45)
            $ character.Statup("Inbt", 80, 60)
        else:
            $ character.Statup("Love", 90, 5)
            $ character.Statup("Obed", 70, 35)
            $ character.Statup("Inbt", 80, 40)
    if action == "dildo_pussy" and not character.DildoP:
        if character.Forced:
            $ character.Statup("Love", 90, -75)
            $ character.Statup("Obed", 70, 60)
            $ character.Statup("Inbt", 80, 35)
        else:
            $ character.Statup("Love", 90, 10)
            $ character.Statup("Obed", 70, 20)
            $ character.Statup("Inbt", 80, 45)
    if action == "dildo_ass" and not character.DildoA:
        if character.Forced:
            $ character.Statup("Love", 90, -75)
            $ character.Statup("Obed", 70, 60)
            $ character.Statup("Inbt", 80, 35)
        else:
            $ character.Statup("Love", 90, 10)
            $ character.Statup("Obed", 70, 20)
            $ character.Statup("Inbt", 80, 45)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0

    $ Line = 0
    $ Cnt = 0

    if Taboo:
        $ character.DrainWord("tabno")

    $ character.DrainWord("no_" + action)
    $ character.RecentActions.append(action)
    $ character.DailyActions.append(action)

    call handjob_cycle(character, action)

    return

label handjob_cycle(character, action):
    while Round > 0:
        call expression action + "launch('" + character.Tag "')"
        call Shift_Focus(character)

        $ character.LustFace()

        if Player.Focus < 100:
            call handjob_menu(character, action)

        if action in ["dildo_pussy", "dildo_ass"]:
            if character.Panties or RogueX.PantsNum() > 6 or character.HoseNum() >= 5:
                call Girl_Undress(character,"auto")

        call Shift_Focus(character)
        call Sex_Dialog(character,Partner)

        $ Cnt += 1
        $ Round -= 1

        if action in ["blowjob"] and Speed:
            $ Player.Wet = 1
            $ Player.Spunk = 0 if Player.Spunk else Player.Spunk

        $ end_cycle = end_of_handjob_round(character, action)

        if end_cycle:
            return

    $ character.FaceChange("bemused", 0)

    $ Line = 0

    call im_done_lines(character)
    call after_handjob(character, action)

    return

label end_of_handjob_round(character, action):
    $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up

    if Player.Focus >= 100 or character.Lust >= 100:
        if Player.Focus >= 100:
            call Player_Cumming(RogueX)

            if "angry" in character.RecentActions:
                call handjob_reset(character)

                return True

            $ character.Statup("Lust", 200, 5)

            if 100 > character.Lust >= 70 and character.OCount < 2 and character.SEXP >= 20:
                $ character.AddWord(0, "unsatisfied", "unsatisfied")

            if Player.Focus > 80:
                call after_handjob(character, action)

                return True

            $ Line = "came"

        if character.Lust >= 100:
            call Girl_Cumming(character)

            if Situation == "shift" or "angry" in character.RecentActions:
                call after_handjob(character, action)

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

    if action in ["handjob", "footjob", "titjob"]:
        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0
    elif action in ["blowjob", "dildo_pussy", "dildo_ass"]:
        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

    if action == "handjob":
        $ bonus = character.Hand
    elif action == "footjob":
        $ bonus = character.Footjob
    elif action == "titjob":
        $ bonus = character.Tit
    elif action == "blowjob":
        $ bonus = character.Blowjob
    elif action == "dildo_pussy":
        $ bonus = character.DildoP
    elif action == "dildo_ass":
        $ bonus = character.DildoA

    if character.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
        pass
    elif Cnt == (5 + bonus):
        $ character.Brows = "confused"

        call getting_close_lines(character)
        ch_r "Are you getting close here? I'm getting a little sore."
        ch_r "Are you getting close here? My jaw's getting pretty sore."
        ch_r "What are you even doing down there?"
    elif action in ["dildo_pussy", "dildo_ass"] and character.Lust >= 80:
        pass
    elif (action in ["handjob, footjob, titjob, blowjob"] and Cnt == (10 + bonus)) or (action in ["dildo_pussy", "dildo_ass"] and (Cnt == (15 + bonus) and character.SEXP <= 100 and not ApprovalCheck(character, 1200, "LO"))):
        $ character.Brows = "angry"

        call getting_rugburn_lines(character)
        ch_r "I'm getting rug-burn here [character.Petname]. Can we do something else?"
        ch_r "I'm getting a little tired, [character.Petname]. Can we do something else?"
        ch_r "[RogueX.Petname], this is getting uncomfortable, maybe we could try something else."
        ch_r "Ow, i'm not used to this. Mind if we take a break?"
        ch_r "Can we be done with this now? I'm getting sore."

        menu:
            extend ""
            "How about a handy?" if action in ["footjob", "titjob", "blowjob"] and character.Action and MultiAction:
                $ Situation = "shift"

                call handjob_after(character, action)
                call handjob(character)
            "How about a footjob?" if action in ["handjob", "titjob", "blowjob"] and character.Action and MultiAction:
                $ Situation = "shift"

                call handjob_after(character, action)
                call footjob(character)
            "How about a titjob?" if action in ["handjob", "footjob", "blowjob"] and character.Action and MultiAction:
                $ Situation = "shift"

                call handjob_after(character, action)
                call titjob(character)
            "How about a BJ?" if action in ["handjob", "footjob", "titjob"] and character.Action and MultiAction:
                $ Situation = "shift"

                call handjob_after(character, action)
                call blowjob(character)
            "Finish up." if action in ["handjob", "footjob", "titjob", "blowjob"] and Player.FocusX:
                "You release your concentration. . ."

                $ Player.FocusX = 0
                $ Player.Focus += 15

                call handjob_cycle(character, action)

                return
            "Finish up." if action in ["dildo_pussy", "dildo_ass"]:
                "You let go. . ."

                call after_handjob(character, action)

                return True
            "Let's try something else." if MultiAction:
                $ Line = 0
                $ Situation = "shift"

                call after_handjob(character, action)

                return True
            "No, get back down there." if action in ["handjob", "footjob", "titjob", "blowjob"]:
                if ApprovalCheck(character, 1200) or ApprovalCheck(character, 500, "O"):
                    $ character.Statup("Love", 200, -5)
                    $ character.Statup("Obed", 50, 3)
                    $ character.Statup("Obed", 80, 2)

                    "She grumbles but keeps going."
                else:
                    $ character.FaceChange("angry", 1)

                    call reset_position(character)

                    "She scowls at you, drops your cock and pulls back."

                    call this_is_boring_lines(character)

                    $ character.Statup("Love", 50, -3, 1)
                    $ character.Statup("Love", 80, -4, 1)
                    $ character.Statup("Obed", 30, -1, 1)
                    $ character.Statup("Obed", 50, -1, 1)
                    $ character.AddWord(1,"angry","angry")

                    call after_handjob(character, action)

                    return True
            "No, this is fun." if action in ["dildo_pussy", "dildo_ass"]
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

                    call after_handjob(character, action)

                    return True

    call Escalation(character)

    if Round == 10:
        call wrap_this_up_lines(character)
    elif Round == 5:
        call time_to_stop_soon_lines(character)

    return = False

label dildo_check(character):
    if "dildo" in Player.Inventory:
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in character.Inventory:
        "You ask [character.Name] to get out her favorite dildo."
    else:
        "You don't have one of those on you."

        return False

    return True

label vibrator_check(character):     
    if "vibrator" in Player.Inventory:
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in character.Inventory:
        "You ask [character.Name] to get out her vibrator."
    else:
        "You don't have one of those on you."

        return False

    return True
