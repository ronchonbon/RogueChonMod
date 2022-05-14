label sex_menu:
    menu:
        "Keep going. . ." if Speed:
            pass
        "Keep going. . . (locked)" if not Speed:
            pass
        "Start moving? . ." if not Speed:
            $ Speed = 1
        "Speed up. . ." if 0 < Speed < 3:
            $ Speed += 1

            "You ask her to up the pace a bit."
        "Speed up. . . (locked)" if Speed >= 3:
            pass
        "Slow Down. . ." if Speed:
            $ Speed -= 1

            "You ask her to slow it down a bit."
        "Slow Down. . . (locked)" if not Speed:
            pass
        "Slap her ass":
            call Slap_Ass(Player.focused_girl)

            $ Cnt += 1
            $ Round -= 1

            jump sex_cycle
        "Turn her around":
            $ Player.focused_girl.Pose = "doggy" if Player.focused_girl.Pose != "doggy" else "sex"

            "You turn her around. . ."

            jump sex_cycle
        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
            pass
        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
            "You concentrate on not burning out too quickly."

            $ Player.FocusX = 1
        "Release your focus." if Player.FocusX:
            "You release your concentration. . ."

            $ Player.FocusX = 0
        "Other options":
            menu:
                "Offhand action":
                    if Player.focused_girl.Action and MultiAction:
                        call Offhand_Set

                        if Trigger2:
                            $ Player.focused_girl.Action -= 1
                    else:
                        call Sex_Basic_Dialog(Player.focused_girl,"tired")
                "Shift primary action":
                    if Player.focused_girl.Action and MultiAction:
                        menu:
                            "How about sex?" if Player.primary_action != "sex":
                                $ Situation = "shift"

                                call after_action(Player.focused_girl, Player.primary_action)
                                call sex(Player.focused_girl)
                            "Just stick it in her pussy [[without asking]." if Player.primary_action != "sex":
                                $ Situation = "auto"

                                call after_action(Player.focused_girl, Player.primary_action)
                                call sex(Player.focused_girl)
                            "How about anal?" if Player.primary_action != "anal":
                                $ Situation = "shift"

                                call after_action(Player.focused_girl, Player.primary_action)
                                call anal(Player.focused_girl)
                            "Just stick it in her ass [[without asking]." if Player.primary_action != "anal":
                                $ Situation = "auto"

                                call after_action(Player.focused_girl, Player.primary_action)
                                call anal(Player.focused_girl)
                            "Pull back to hotdog her." if Player.primary_action != "hotdog":
                                $ Situation = "pullback"

                                call after_action(Player.focused_girl, Player.primary_action)
                                call hotdog(Player.focused_girl)
                            "Never Mind":
                                jump sex_cycle
                    else:
                        call tired_lines(Player.focused_girl)
                "Threesome actions (locked)" if not Partner:
                    pass
                "Threesome actions" if Partner:
                    menu:
                        "Ask [Player.focused_girl.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                            call Les_Change(Player.focused_girl)
                        "Ask [Player.focused_girl.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                            pass
                        "Ask [Partner.Name] to do something else":
                            call Three_Change(Player.focused_girl)
                        "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                            $ ThreeCount = 0
                        "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                            $ ThreeCount = 0
                        "Swap to [Partner.Name]":
                            call Trigger_Swap(Player.focused_girl)
                        "Undress [Partner.Name]":
                            call Girl_Undress(Partner)
                            jump sex_cycle
                        "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                            pass
                        "Clean up [Partner.Name]" if Partner.Spunk:
                            call Girl_Cleanup(Partner,"ask")
                            jump sex_cycle
                        "Never mind":
                            jump sex_cycle
                "Just take a look at her.":
                    $ Player.Cock = 0

                    $ Speed = 0
                "Show her feet" if not ShowFeet and (Player.focused_girl.Pose == "doggy" or Player.focused_girl.Pose == "sex"):
                    $ ShowFeet = 1
                "Hide her feet" if ShowFeet and (Player.focused_girl.Pose == "doggy" or Player.focused_girl.Pose == "sex"):
                    $ ShowFeet = 0
                "Undress [Player.focused_girl.Name]":
                    call Girl_Undress(Player.focused_girl)
                "Clean up [Player.focused_girl.Name] (locked)" if not Player.focused_girl.Spunk:
                    pass
                "Clean up [Player.focused_girl.Name]" if Player.focused_girl.Spunk:
                    call Girl_Cleanup(Player.focused_girl,"ask")
                "Never mind":
                    jump sex_cycle
        "Back to Sex Menu" if MultiAction:
            ch_p "Let's try something else."

            call sex_reset(Player.focused_girl)

            $ Situation = "shift"
            $ Line = 0

            jump after_action
        "End Scene" if not MultiAction:
            ch_p "Let's stop for now."

            call sex_reset(Player.focused_girl)

            $ Line = 0

            jump after_action

    jump sex_menu_return

label sex_set_modifier(character, action):
    if action == "sex":
        if character.Sex >= 7: # She loves it
            $ temp_modifier += 15
        elif character.Sex >= 3: #You've done it before several times
            $ temp_modifier += 12
        elif character.Sex: #You've done it before
            $ temp_modifier += 10

        if character.Addict >= 75 and (character.CreamP + character.CreamA) >=3: #She's really strung out and has creampied
            $ temp_modifier += 20
        elif character.Addict >= 75:
            $ temp_modifier += 15

        if character.Lust > 85:
            $ temp_modifier += 10
        elif character.Lust > 75: #She's really horny
            $ temp_modifier += 5

        if Situation == "shift":
            $ temp_modifier += 10
        if "exhibitionist" in character.Traits:
            $ temp_modifier += (4*Taboo)
    elif action == "anal":
        if character.Anal >= 7: # She loves it
            $ temp_modifier += 20
        elif character.Anal >= 3: #You've done it before several times
            $ temp_modifier += 17
        elif character.Anal: #You've done it before
            $ temp_modifier += 15

        if character.Addict >= 75 and (character.CreamP + character.CreamA) >=3: #She's really strung out and has creampied
            $ temp_modifier += 25
        elif character.Addict >= 75:
            $ temp_modifier += 15

        if character.Lust > 85:
            $ temp_modifier += 10
        elif character.Lust > 75: #She's really horny
            $ temp_modifier += 5

        if character.Loose:
            $ temp_modifier += 10
        elif "anal" in character.RecentActions:
            $ temp_modifier -= 20
        elif "anal" in character.DailyActions:
            $ temp_modifier -= 10

        if Situation == "shift":
            $ temp_modifier += 10
        if "exhibitionist" in character.Traits:
            $ temp_modifier += (5*Taboo)
    elif action == "hotdog":
        if character.Hotdog >= 3: #You've done it before several times
            $ temp_modifier += 10
        elif character.Hotdog: #You've done it before
            $ temp_modifier += 5

        if character.Lust > 85:
            $ temp_modifier += 10
        elif character.Lust > 75: #She's really horny
            $ temp_modifier += 5
        if Situation == "shift":
            $ temp_modifier += 10
        if "exhibitionist" in character.Traits:
            $ temp_modifier += (3*Taboo)

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

label end_of_sex_round(character, action):
    $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus

    if Player.Focus >= 100 or character.Lust >= 100:
        if Player.Focus >= 100:
            call Player_Cumming(character)

            if "angry" in character.RecentActions:
                call sex_reset(character)

                return True

            $ character.Statup("Lust", 200, 5)

            if 100 > character.Lust >= 70 and character.OCount < 2:
                $ character.AddWord(0, "unsatisfied", "unsatisfied")

            if Player.Focus > 80:
                call after_action(character, action)

                return True

            $ Line = "came"

        if character.Lust >= 100:
            call Girl_Cumming(character)

            if Situation == "shift" or "angry" in character.RecentActions:
                call after_action(character, action)

                return True

        if Line == "came": #ex Player.Focus <= 20:
            $ Line = 0

            if not Player.Semen:
                "She's emptied you out, you'll need to take a break."

                call after_action(character, action)

                return True
            elif "unsatisfied" in character.RecentActions:#And Rogue is unsatisfied,
                call not_ready_to_stop_lines(character)

                menu:
                    extend "Keep going?"
                    "Yes, keep going for a bit." if Player.Semen:
                        $ Line = "You get back into it"
                    "No, I'm done." if Player.Semen:
                        "You pull back."

                        call after_action(character, action)

                        return True
                    "No, I'm spent." if not Player.Semen:
                        "You pull back."

                        call after_action(character, action)

                        return True

    if Partner and Partner.Lust >= 100:
        call Girl_Cumming(Partner)

    $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

    if action == "sex":
        $ bonus = character.Sex
    elif action == "anal":
        $ bonus = character.Anal
    elif action == "hotdog":
        $ bonus = character.Hotdog

    if character.SEXP >= 100 or ApprovalCheck(character, 1200, "LO"):
        pass
    elif Cnt == (5 + bonus):
        $ character.Brows = "confused"

        call getting_close_lines(character)
    elif Cnt == (10 + bonus):
        $ character.Brows = "angry"

        call done_with_this_lines(character)
        call can_we_do_something_else_lines(character)

        menu:
            extend ""
            "How about a BJ?" if character.Action and MultiAction:
                if action != "anal":
                    $ Situation = "shift"

                    call after_action(character, action)
                    call blowjob(character)
                else:
                    if character.Anal >= 5 and character.Blow >= 10 and character.SEXP >= 50:
                        $ Situation = "shift"

                        call after_action(character, action)
                        call blowjob(character)
                    else:
                        call no_ass_to_mouth_lines(character)

                        $ Situation = "shift"

                        call after_action(character, action)
                        call before_handjob(character, "handjob")
            "How about a Handy?" if character.Action and MultiAction:
                $ Situation = "shift"

                call after_action(character, action)
                call handjob(character)
            "Finish up.":
                "You release your concentration. . ."

                $ Player.FocusX = 0
                $ Player.Focus += 15

                call after_action(character, action)

                return True
            "Let's try something else." if MultiAction:
                $ Line = 0
                $ Situation = "shift"

                call after_action(character, action)

                return True
            "No, get back down there.":
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

                    call after_action(character, action)

                    return True

    call Escalation(character)

    if Round == 10:
        call wrap_this_up_lines(character)
    elif Round == 5:
        call time_to_stop_soon_lines(character)

    return False

label sex(character):
    $ Player.primary_action = "sex"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(character)
    call sex_set_modifier(character, "sex")

    $ Approval = ApprovalCheck(character, 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)

    if Situation == "auto":
        $ character.Pose = "doggy"

        call sex_launch(character, "sex")

        if character.PantsNum() == 5:
            "You press up against [character.Name]'s backside, sliding her skirt up as you go."

            $ character.Upskirt = 1
        elif character.PantsNum() > 6:
            "You press up against [character.Name]'s backside, sliding her pants down as you do."

            $ character.Legs = 0
        else:
            "You press up against [character.Name]'s backside."

        $ character.SeenPanties = 1

        "You rub the tip of your cock against her moist slit."

        $ character.FaceChange("surprised", 1)

        if (character.Sex and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
            "[character.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."

            $ character.FaceChange("sexy")
            $ character.Statup("Obed", 70, 3)
            $ character.Statup("Inbt", 50, 3)
            $ character.Statup("Inbt", 70, 1)

            call lets_do_this_lines(character)

            jump before_action
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

                        call since_you_are_so_nice_lines(character)

                        jump before_action

                    "You pull back before you really get it in."

                    $ character.FaceChange("bemused", 1)

                    if character.Sex:
                        ch_r "Well ok, [character.Petname], no harm done. Just give me a little warning next time."
                    else:
                        ch_r "Well ok, [character.Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."
                "Just fucking.":
                    $ character.Statup("Love", 80, -10, 1)
                    $ character.Statup("Love", 200, -10)

                    "You press inside some more."

                    $ character.Statup("Obed", 70, 3)
                    $ character.Statup("Inbt", 50, 3)

                    if not ApprovalCheck(character, 700, "O", TabM=1):   #Checks if Obed is 700+
                        $ character.FaceChange("angry")

                        call were_done_here_lines(character)

                        $ character.Statup("Love", 50, -10, 1)
                        $ character.Statup("Obed", 50, 3)

                        $ renpy.pop_call()

                        if Situation:
                            $ renpy.pop_call()

                        call sex_reset(character)

                        $ character.RecentActions.append("angry")
                        $ character.DailyActions.append("angry")
                    else:
                        $ character.FaceChange("sad")

                        call knows_her_place_lines(character)

                        jump before_action
        return

    if not character.Sex and "no sex" not in character.RecentActions:                           #first time
        $ character.FaceChange("surprised", 1)
        $ character.Mouth = "kiss"

        ch_r "So, you'd like to take this to the next level? Actual sex? . . ."

        if character.Forced:
            $ character.FaceChange("sad")

            ch_r "You'd really take it that far?"

    if not character.Sex and Approval:                                                  #First time dialog
        call first_action_approval(character, "sex")
    elif Approval:
        call action_approved(character, "sex", character.Sex)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(character, "sex")

        return
    else:                                                                               #She's not into it, but maybe. . .
        call action_disapproved(character, "sex", character.Sex)

    $ character.ArmPose = 1

    call action_rejected(character, "sex", character.Sex)

    return

label anal(character):
    $ Player.primary_action = "anal"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(character)
    call sex_set_modifier(character, "anal")

    $ Approval = ApprovalCheck(character, 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)

    if Situation == "auto":
        $ character.Pose = "doggy"

        call sex_launch(character, "anal")

        if character.PantsNum() == 5:
            "You press up against [character.Name]'s backside, sliding her skirt up as you go."

            $ character.Upskirt = 1
        elif character.PantsNum() > 6:
            "You press up against [character.Name]'s backside, sliding her pants down as you do."

            $ character.Legs = 0
        else:
            "You press up against [character.Name]'s backside."

        $ character.SeenPanties = 1

        "You press the tip of your cock against her tight rim."

        $ character.FaceChange("surprised", 1)

        if (character.Anal and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
            "[character.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."

            $ character.FaceChange("sexy")
            $ character.Statup("Obed", 70, 3)
            $ character.Statup("Inbt", 50, 3)
            $ character.Statup("Inbt", 70, 1)

            ch_r "Hmm, stick it in. . ."

            jump before_action
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

                        call since_you_are_so_nice_lines(character)

                        jump before_action

                    "You pull back before you really get it in."

                    $ character.FaceChange("bemused", 1)

                    if character.Anal:
                        ch_r "Well ok, [character.Petname], no harm done. Just give me a little warning next time."
                    else:
                        ch_r "Well ok, [character.Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."
                "Just fucking.":
                    $ character.Statup("Love", 80, -10, 1)
                    $ character.Statup("Love", 200, -8)

                    "You press into her."

                    $ character.Statup("Obed", 70, 3)
                    $ character.Statup("Inbt", 50, 3)

                    if not ApprovalCheck(character, 700, "O", TabM=1):
                        $ character.FaceChange("angry")

                        call were_done_here_lines(character)

                        $ character.Statup("Love", 50, -10, 1)
                        $ character.Statup("Obed", 50, 3)

                        $ renpy.pop_call()

                        if Situation:
                            $ renpy.pop_call()

                        call sex_reset(character)

                        $ character.RecentActions.append("angry")
                        $ character.DailyActions.append("angry")
                    else:
                        $ character.FaceChange("sad")

                        call knows_her_place_lines(character)

                        jump before_action
        return

    if not character.Anal and "no anal" not in character.RecentActions:                                                               #first time
        $ character.FaceChange("surprised", 1)
        $ character.Mouth = "kiss"

        ch_r "Wait, so you want to stick it in my butt?!"

        if character.Forced:
            $ character.FaceChange("sad")

            ch_r "Seriously?"

    if not character.Loose and ("dildo anal" in character.DailyActions or "anal" in character.DailyActions):
        $ character.FaceChange("bemused", 1)

        call ass_sore_lines(character)
    elif "anal" in character.RecentActions:
        $ character.FaceChange("sexy", 1)

        call recent_action_lines(character)
        call before_action

    if not character.Anal and Approval:                                                 #First time dialog
        call first_action_approval(character, "anal")
    elif Approval:
        call action_approved(character, "anal", character.Anal)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(character, "anal")

        return
    else:                                                                               #She's not into it, but maybe. . .
        call action_disapproved(character, "anal", character.Anal)

    $ character.ArmPose = 1

    call action_rejectd(character, "anal", character.Anal)

    return

label hotdog(character):
    $ Player.primary_action = "hotdog"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(character)
    call sex_set_modifier(character, "hotdog")

    $ Approval = ApprovalCheck(character, 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)

    if Situation == "auto":
        $ character.Pose = "doggy"

        call sex_launch("hotdog")

        "You press up against [character.Name]'s backside."

        $ character.FaceChange("surprised", 1)

        if (character.Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
            "[character.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."

            $ character.FaceChange("sexy")
            $ character.Statup("Obed", 70, 3)
            $ character.Statup("Inbt", 50, 3)
            $ character.Statup("Inbt", 70, 1)

            ch_r "Hmm, I've apparently got someone's attention. . ."

            jump before_action
        else:                                                                                                            #she's questioning it
            $ character.Brows = "angry"

            menu:
                ch_r "Hmm, kinda rude, [character.Petname]."
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ character.FaceChange("sexy", 1)
                        $ character.Statup("Obed", 70, 3)
                        $ character.Statup("Inbt", 50, 3)
                        $ character.Statup("Inbt", 70, 1)

                        call since_you_are_so_nice_lines(character)

                        jump before_action

                    "You pull back before you really get it in."

                    $ character.FaceChange("bemused", 1)

                    if character.Hotdog:
                        ch_r "Well ok, [character.Petname], it has been kinda fun."
                    else:
                        ch_r "Well ok, [character.Petname], that's a bit dirty, maybe ask a girl?"
                "You'll see.":
                    $ character.Statup("Love", 80, -10, 1)
                    $ character.Statup("Love", 200, -8)

                    "You grind against her asscrack."

                    $ character.Statup("Obed", 70, 3)
                    $ character.Statup("Inbt", 50, 3)

                    if not ApprovalCheck(character, 500, "O", TabM=1): #Checks if Obed is 700+
                        $ character.FaceChange("angry")

                        call were_done_here_lines(character)

                        $ character.Statup("Love", 50, -10, 1)
                        $ character.Statup("Obed", 50, 3)

                        $ renpy.pop_call()

                        if Situation:
                            $ renpy.pop_call()

                        call sex_reset(character)

                        $ character.RecentActions.append("angry")
                        $ character.DailyActions.append("angry")
                    else:
                        $ character.FaceChange("sad")

                        call knows_her_place_lines(character)

                        jump before_action
        return

    if not character.Hotdog and "no hotdog" not in character.RecentActions:                                                               #first time
        $ character.FaceChange("surprised", 1)
        $ character.Mouth = "kiss"

        ch_r "Wait, so you want to grind against my butt?!"

        if character.Forced:
            $ character.FaceChange("sad")

            ch_r ". . . That's all?"

    if not character.Hotdog and Approval:                                                 #First time dialog
        call first_action_approval(character, "hotdog")
    elif Approval:                                                                       #Second time+ dialog
        call action_approved(character, "hotdog", character.Hotdog)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(character, "hotdog")

        return
    else:                                                                               #She's not into it, but maybe. . .
        call action_rejected(character, "hotdog", character.Hotdog)

    $ character.ArmPose = 1

    call action_rejected(character, "hotdog", character.Hotdog)

    return
