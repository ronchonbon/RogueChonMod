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
        "Just the head. . . (locked)" if action == "blowjob" and Speed == 2:
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

                                        call after_handjob(character, action)
                                        call handjob(character)
                                    else:
                                        call tired_lines(character)
                                "How about a footjob?" if action in ["handjob", "titjob", "blowjob"]:
                                    if character.Action and MultiAction:
                                        $ Situation = "shift"

                                        call after_handjob(character, action)
                                        call footjob(character)
                                    else:
                                        call tired_lines(character)
                                "How about a titjob?" if action in ["handjob", "footjob", "blowjob"]:
                                    if character.Action and MultiAction:
                                        $ Situation = "shift"

                                        call after_handjob(character, action)
                                        call titjob(character)
                                    else:
                                        call tired_lines(character)
                                "How about a blowjob?" if action in ["handjob", "footjob", "titjob"]:
                                    if character.Action and MultiAction:
                                        $ Situation = "shift"

                                        call after_handjob(character, action)
                                        call blowjob(character)
                                    else:
                                        call tired_lines(character)
                                "I want to stick a finger in her ass." if action == "dildo_pussy":
                                    if character.Action and MultiAction:
                                        $ Situation = "shift"

                                        call after_handjob(character, action)
                                        call finger_ass(character)
                                    else:
                                        call tired_lines(character)
                                "Just stick a finger in her ass without asking." if action == "dildo_pussy":
                                    if character.Action and MultiAction:
                                        $ Situation = "auto"

                                        call after_handjob(character, action)
                                        call finger_ass(character)
                                    else:
                                        call tired_lines(character)
                                "I want to shift the dildo to her ass." if action == "dildo_pussy":
                                    if character.Action and MultiAction:
                                        $ Situation = "shift"

                                        call after_handjob(character, action)
                                        call dildo_ass(character)
                                    else:
                                        call tired_lines(character)
                                "I want to stick a finger in her pussy." if action == "dildo_ass":
                                    if character.Action and MultiAction:
                                        $ Situation = "shift"

                                        call after_handjob(character, action)
                                        call finger_pussy(character)
                                    else:
                                        call tired_lines(character)
                                "Just stick a finger in her pussy without asking." if action == "dildo_ass":
                                    if character.Action and MultiAction:
                                        $ Situation = "auto"

                                        call after_handjob(character, action)
                                        call finger_pussy(character)
                                    else:
                                        call tired_lines(character)
                                "I want to shift the dildo to her pussy." if action == "dildo_ass":
                                    if character.Action and MultiAction:
                                        $ Situation = "shift"

                                        call after_handjob(character, action)
                                        call dildo_pussy(character)
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

    if Situation == character:
        $ Situation = 0

        $ stop_character = False

        call character_initiated_action(character, action)

        if _return:
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
        #$ renpy.pop_call()

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
        call handjob_launch(character)
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

        call end_of_handjob_round(character, action)

        if _return:
            return

    $ character.FaceChange("bemused", 0)

    $ Line = 0

    call im_done_lines(character)
    call after_handjob(character, action)

    return

label after_handjob(character, action):
    if action in ["dildo_pussy", "dildo_ass"] and not Situation:
        call reset_position(character)

    $ character.FaceChange("sexy")

    if action == "handjob":
        $ character.Hand += 1

        $ achievement = character.Tag + " Handi-Queen"
        $ counter = character.Hand

        call Partner_Like(character, 2)
    elif action == "footjob":
        $ character.Foot += 1

        $ achievement = character.Tag + "pedi"
        $ counter = character.Foot

        call Partner_Like(character, 1)
    elif action == "titjob":
        $ character.Tit += 1

        $ achievement = None
        $ counter = character.Tit

        call Partner_Like(character, 3)
    elif action == "blowjob":
        $ character.Blow += 1

        $ achievement = character.Tag + " Jobber"
        $ counter = character.Blow

        if character == RogueX and Partner == EmmaX:
            call Partner_Like(character, 3)
        else:
            call Partner_Like(character, 2)
    elif action == "dildo_pussy":
        $ character.DildoP += 1

        $ achievement = None
        $ counter = character.DildoP

        call Partner_Like(character, 2)
    elif action == "dildo_ass":
        $ character.DildoA += 1

        $ achievement = None
        $ counter = character.DildoA

        call Partner_Like(character, 2)

    $ character.Action -= 1

    if action not in ["dildo_pussy", "dildo_ass"]:
        $ character.Addictionrate += 1

        if "addictive" in Player.Traits:
            $ character.Addictionrate += 1

    if action in ["handjob", "footjob"]:
        $ character.Statup("Lust", 90, 5)

    if achievement is not None and achievement in Achievements:
        pass
    elif action not in ["dildo_pussy", "dildo_ass"] and counter >= 10:
        $ character.FaceChange("smile", 1)

        ch_r "I guess you can call me \"Handi-Queen.\""
        ch_r "I guess I've gotten used to this foot thing."
        ch_r "I'm really starting to enjoy this."

        if achievement is not None:
            $ Achievements.append(achievement)

        $ character.SEXP += 5
    elif counter == 1:
        if action in ["handjob", "footjob", "dildo_pussy"]:
            $ character.SEXP += 10
        elif action in ["titjob"]:
            $ character.SEXP += 12
        elif action in ["blowjob"]:
            $ character.SEXP += 15

        if character.Love >= 500 and "unsatisfied" not in character.RecentActions:
            $ character.Mouth = "smile"

            ch_r "Well, it's really nice to finally be able to reach out and touch someone."
            ch_r "That was a real interesting experience. . ."
            ch_r "Well, that was certainly interesting."
            ch_r "That really wasn't half bad."
            ch_r "Well I liked that. . ."
            ch_r "Well that was a bit rough. . ."
        elif action not in ["dildo_pussy", "dildo_ass"] and  Player.Focus <= 20:
            $ character.Mouth = "sad"

            ch_r "Well, I hope that got your rocks off."
            ch_r "Did that work for you?"
            ch_r "Well, I hope that was enough for you."
        elif action in ["dildo_pussy", "dildo_ass"] and character.Obed <= 500 and Player.Focus <= 20:
            $ character.FaceChange("perplexed", 1)

            ch_r "Did you like that?"
    elif action not in ["dildo_pussy", "dildo_ass"] and counter == 5:
        ch_r "I think I've got this well in hand."
        ch_r "I kinda like this sensation.{p}}Never thought about touching people with my feet."
        ch_r "I think I've got the hang of this."

    $ temp_modifier = 0

    if Situation == "shift":
        ch_r "Mmm, so what else did you have in mind?"
    else:
        if action == "handjob":
            call handjob_reset(character)
        elif action == "footjob":
            call doggy_reset(character)
        elif action == "titjob":
            call titjob_reset(character)
        elif action == "blowjob":
            call blowjob_reset(character)

    call Checkout

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
        $ bonus = character.Foot
    elif action == "titjob":
        $ bonus = character.Tit
    elif action == "blowjob":
        $ bonus = character.Blow
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
            "No, this is fun." if action in ["dildo_pussy", "dildo_ass"]:
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

    return False

label handjob(character):
    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(character)
    call handjob_set_modifier(character, "handjob")

    $ Approval = ApprovalCheck(character, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if not character.Hand and "no hand" not in character.RecentActions:
        $ character.FaceChange("surprised", 1)
        $ character.Mouth = "kiss"

        ch_r "You want me to rub your cock, with my hand?"

    if not character.Hand and Approval:                                                 #First time dialog
        call first_action_approval(character, "handjob")
    elif Approval:
        call action_approved(character, "handjob", character.Hand)

    if Approval >= 2:
        call action_accepted(character, "handjob")

        return
    else:                                                                               #She's not into it, but maybe. . .
        call action_disapproved(character, "handjob", character.Hand)

    $ character.ArmPose = 1

    call action_rejected(character, "handjob", character.Hand)

    return

label footjob(character):
    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(character)
    call handjob_set_modifier(character, "footjob")

    $ Approval = ApprovalCheck(character, 1250, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if Situation == character:                                                                  #Rogue auto-starts
        if Approval > 2:                                                      # fix, add rogue auto stuff here
            call character_initiated_action(character, "footjob")

            if _return:
                return

            if Trigger:
                $ Trigger3 = "foot"
                return

            call before_handjob(character, "footjob")
        else:
            $ temp_modifier = 0                               # fix, add rogue auto stuff here
            $ Trigger2 = 0

            return

    if not character.Foot and "no foot" not in character.RecentActions:
        $ character.FaceChange("confused", 2)

        ch_r "Huh, so like a handy, but with my feet?"

        $ character.Blush = 1

    if not character.Foot and Approval:                                                 #First time dialog
        call first_action_approval(character, "footjob")
    elif Approval:
        call action_approved(character, "footjob", character.Foot)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(character, "footjob")

        return
    else:                                                                               #She's not into it, but maybe. . .
        call action_disapproved(character, "footjob", character.Foot)

    $ character.ArmPose = 1

    call action_rejected(character, "footjob", character.Foot)

    return

label titjob(character):
    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(character)
    call handjob_set_modifier(character, "titjob")

    $ Approval = ApprovalCheck(character, 1200, TabM = 5) # 120, 135, 150, Taboo -200(320)

    if not character.Tit and "no titjob" not in character.RecentActions:
        $ character.FaceChange("surprised", 1)
        $ character.Mouth = "kiss"

        ch_r "You want me to rub your cock with my breasts?"

        if character.Blow:
            $ character.Mouth = "smile"

            ch_r "My mouth wasn't enough?"
        elif character.Hand:
            $ character.Mouth = "smile"

            ch_r "My hand wasn't enough?"

    if not character.Tit and Approval:                                                 #First time dialog
        call first_action_approval(character)
    elif Approval:
        call action_approved(character, "titjob", character.Tit)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(character, "titjob")
    else:                                                                               #She's not into it, but maybe. . .
        call action_disapproved(character, "titjob", character.Tit)

    call action_rejected(character, "titjob", character.Tit)

    return

label blowjob(character):
    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(character)
    call handjob_set_modifier(character, "blowjob")

    $ Approval = ApprovalCheck(character, 1300, TabM = 4) # 130, 145, 160, Taboo -160(290)

    if not character.Blow and "no blow" not in character.RecentActions:
        $ character.FaceChange("surprised", 1)
        $ character.Mouth = "kiss"

        ch_r "You want me to put your dick. . . in my mouth?"
        if character.Hand:
            $ character.Mouth = "smile"

            ch_r "My hand wasn't enough?"

    if not character.Blow and Approval:                                                 #First time dialog
        call first_action_approval(character)
    elif Approval:
        call action_approved(character, "blowjob", character.Blow)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(character, "blowjob")

        return
    else:                                                                               #She's not into it, but maybe. . .
        call action_disapproved(character, "blowjob", character.Blow)

    call action_rejected(character, "blowjob", character.Blow)

    return

label dildo_pussy(character):
    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(character)
    call Rogue_Dildo_Check

    if not _return:
        return

    call handjob_set_modifier(character, "dildo_pussy")

    $ Approval = ApprovalCheck(character, 1250, TabM = 4) # 125, 140, 155, Taboo -160(335)

    if Situation == character:                                                                  #Rogue auto-starts
        if Approval > 2:                                                      # fix, add rogue auto stuff here

            call character_initiated_action(character, "dildo_pussy")

            if _return:
                return

            call before_handjob(character, "dildo_pussy")
        else:
            $ temp_modifier = 0                               # fix, add rogue auto stuff here
            $ Trigger2 = 0
        return

    if Situation == "auto":
        "You rub the dildo across her body, and along her moist slit."

        $ character.FaceChange("surprised", 1)

        if (character.DildoP and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
            "[character.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."

            $ character.FaceChange("sexy")
            $ character.Statup("Obed", 70, 3)
            $ character.Statup("Inbt", 50, 3)
            $ character.Statup("Inbt", 70, 1)

            ch_r "Ok, [character.Petname], let's do this."

            call before_handjob(character, "dildo_pussy")

            return
        else:                                                                                                            #she's questioning it
            $ character.Brows = "angry"

            menu:
                ch_r "Hey, what do you think you're doing back there?!"
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ character.FaceChange("sexy", 1)
                        $ character.Statup("Obed", 70, 3)
                        $ character.Statup("Inbt", 50, 3)
                        $ character.Statup("Inbt", 70, 1)

                        ch_r "Well, since you're be'in so nice about it, I guess we can give it a go. . ."

                        call before_handjob(character, "dildo_pussy")

                        return
                    "You pull back before you really get it in."

                    $ character.FaceChange("bemused", 1)

                    if character.DildoP:
                        ch_r "Well ok, [character.Petname], no harm done. Just give me a little warning next time."
                    else:
                        ch_r "Well ok, [character.Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."
                "Just playing with my favorite toys.":
                    $ character.Statup("Love", 80, -10, 1)
                    $ character.Statup("Love", 200, -10)

                    "You press it inside some more."

                    $ character.Statup("Obed", 70, 3)
                    $ character.Statup("Inbt", 50, 3)

                    if not ApprovalCheck(character, 700, "O", TabM=1): #Checks if Obed is 700+
                        $ character.FaceChange("angry")

                        "[character.Name] shoves you away and slaps you in the face."
                        ch_r "Jackass!"
                        ch_r "If that's how you want to treat me, we're done here!"

                        $ character.Statup("Love", 50, -10, 1)
                        $ character.Statup("Obed", 50, 3)

                        $ renpy.pop_call()

                        if Situation:
                            $ renpy.pop_call()

                        if renpy.showing("Rogue_Doggy"):
                            call doggy_reset(character)

                        $ character.RecentActions.append("angry")
                        $ character.DailyActions.append("angry")
                    else:
                        $ character.FaceChange("sad")

                        "[character.Name] doesn't seem to be into this, you're lucky she's so obedient."

                        call before_handjob(character, "dildo_pussy")

                        return
        return

    if not character.DildoP:
        $ character.FaceChange("surprised", 1)
        $ character.Mouth = "kiss"

        ch_r "Hmmm, so you'd like to try out some toys?"

        if character.Forced:
            $ character.FaceChange("sad")

            ch_r "I suppose there are worst things you could ask for."

    if not character.DildoP and Approval:
        call first_action_approval(character, "dildo_pussy")
    elif Approval:
        call action_approved(character, "dildo_pussy", character.DildoP)

    if Approval >= 2:
        call action_accepted(character, "dildo_pussy")
    else:
        call action_disapproved(character, "dildo_pussy", character.DildoP)

    $ character.ArmPose = 1

    call action_rejected(character, "dildo_pussy", character.DildoP)

    return

label dildo_ass(character):
    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(character)
    call Rogue_Dildo_Check

    if not _return:
        return

    call handjob_set_modifier(character, "dildo_ass")

    $ Approval = ApprovalCheck(character, 1450, TabM = 4) # 145, 160, 175, Taboo -160(355)

    if Situation == character:
        if Approval > 2:                                                      # fix, add rogue auto stuff here
            call character_initiated_action(character, "dildo_ass")

            if _return:
                return

            call before_handjob(character, "dildo_ass")

            return
        else:
            $ temp_modifier = 0                               # fix, add rogue auto stuff here
            $ Trigger2 = 0
        return

    if Situation == "auto":
        "You rub the dildo across her body, and against her tight anus."
        $ character.FaceChange("surprised", 1)

        if (character.DildoA and Approval) or (Approval > 1):
            "[character.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."

            $ character.FaceChange("sexy")
            $ character.Statup("Obed", 70, 3)
            $ character.Statup("Inbt", 50, 3)
            $ character.Statup("Inbt", 70, 1)

            ch_r "Ok, [character.Petname], let's do this."

            call before_handjob(character, "dildo_ass")

            return
        else:
            $ character.Brows = "angry"

            menu:
                ch_r "Hey, what do you think you're doing back there?!"
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ character.FaceChange("sexy", 1)
                        $ character.Statup("Obed", 70, 3)
                        $ character.Statup("Inbt", 50, 3)
                        $ character.Statup("Inbt", 70, 1)

                        ch_r "Well, since you're be'in so nice about it, I guess we can give it a go. . ."

                        call before_handjob(character, "dildo_ass")

                        return

                    "You pull back before you really get it in."

                    $ character.FaceChange("bemused", 1)

                    if character.DildoA:
                        ch_r "Well ok, [character.Petname], no harm done. Just give me a little warning next time."
                    else:
                        ch_r "Well ok, [character.Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."
                "Just playing with my favorite toys.":
                    $ character.Statup("Love", 80, -10, 1)
                    $ character.Statup("Love", 200, -10)

                    "You press it inside some more."
                    $ character.Statup("Obed", 70, 3)
                    $ character.Statup("Inbt", 50, 3)

                    if not ApprovalCheck(character, 700, "O", TabM=1): #Checks if Obed is 700+
                        $ character.FaceChange("angry")

                        "[character.Name] shoves you away and slaps you in the face."
                        ch_r "Jackass!"
                        ch_r "If that's how you want to treat me, we're done here!"

                        $ character.Statup("Love", 50, -10, 1)
                        $ character.Statup("Obed", 50, 3)

                        $ renpy.pop_call()

                        if Situation:
                            $ renpy.pop_call()

                        if renpy.showing("Rogue_Doggy"):
                            call doggy_reset(character)

                        $ character.RecentActions.append("angry")
                        $ character.DailyActions.append("angry")
                    else:
                        $ character.FaceChange("sad")

                        "[character.Name] doesn't seem to be into this, you're lucky she's so obedient."

                        call before_handjob(character, "dildo_ass")

                        return
        return

    if not character.DildoA:
        $ character.FaceChange("surprised", 1)
        $ character.Mouth = "kiss"

        ch_r "Hmmm, so you'd like to try out some toys?"

        if character.Forced:
            $ character.FaceChange("sad")

            ch_r "You had to go for the butt, uh?"

    if not character.Loose and ("dildo anal" in character.RecentActions or "anal" in character.RecentActions or "dildo anal" in character.DailyActions or "anal" in character.DailyActions):
        $ character.FaceChange("bemused", 1)

        ch_r "I'm still a bit sore from earlier. . ."

    if not character.DildoA and Approval:
        call first_action_approval(character, "dildo_ass")
    elif Approval:
        call action_approved(character, "dildo_ass")

    if Approval >= 2:
        call action_accepted(character, "dildo_ass")
    else:
        call action_disapproved(character, "dildo_ass", character.DildoA)

    $ character.ArmPose = 1

    call action_rejected(character, "dildo_ass", character.DildoA)

    return

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
