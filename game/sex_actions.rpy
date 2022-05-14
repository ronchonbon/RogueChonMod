label sex_menu:
    menu:
        "Keep going. . ." if action_speed:
            pass
        "Keep going. . . (locked)" if not action_speed:
            pass
        "Start moving? . ." if not action_speed:
            $ action_speed = 1
        "action_speed up. . ." if 0 < action_speed < 3:
            $ action_speed += 1

            "You ask her to up the pace a bit."
        "action_speed up. . . (locked)" if action_speed >= 3:
            pass
        "Slow Down. . ." if action_speed:
            $ action_speed -= 1

            "You ask her to slow it down a bit."
        "Slow Down. . . (locked)" if not action_speed:
            pass
        "Slap her ass":
            call Slap_Ass(focused_Girl)

            $ counter += 1
            $ Round -= 1

            jump sex_cycle
        "Turn her around":
            $ focused_Girl.Pose = "doggy" if focused_Girl.Pose != "doggy" else "sex"

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
                    if focused_Girl.Action and MultiAction:
                        call Offhand_Set

                        if offhand_action:
                            $ focused_Girl.Action -= 1
                    else:
                        call Sex_Basic_Dialog(focused_Girl,"tired")
                "Shift primary action":
                    if focused_Girl.Action and MultiAction:
                        menu:
                            "How about sex?" if primary_action != "sex":
                                $ action_context = "shift"

                                call after_action(focused_Girl, primary_action)
                                call sex(focused_Girl)
                            "Just stick it in her pussy [[without asking]." if primary_action != "sex":
                                $ action_context = "auto"

                                call after_action(focused_Girl, primary_action)
                                call sex(focused_Girl)
                            "How about anal?" if primary_action != "anal":
                                $ action_context = "shift"

                                call after_action(focused_Girl, primary_action)
                                call anal(focused_Girl)
                            "Just stick it in her ass [[without asking]." if primary_action != "anal":
                                $ action_context = "auto"

                                call after_action(focused_Girl, primary_action)
                                call anal(focused_Girl)
                            "Pull back to hotdog her." if primary_action != "hotdog":
                                $ action_context = "pullback"

                                call after_action(focused_Girl, primary_action)
                                call hotdog(focused_Girl)
                            "Never Mind":
                                jump sex_cycle
                    else:
                        call tired_lines(focused_Girl)
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
                            jump sex_cycle
                        "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                            pass
                        "Clean up [Partner.name]" if Partner.Spunk:
                            call Girl_Cleanup(Partner,"ask")
                            jump sex_cycle
                        "Never mind":
                            jump sex_cycle
                "Just take a look at her.":
                    $ Player.Cock = 0

                    $ action_speed = 0
                "Show her feet" if not ShowFeet and (focused_Girl.Pose == "doggy" or focused_Girl.Pose == "sex"):
                    $ ShowFeet = 1
                "Hide her feet" if ShowFeet and (focused_Girl.Pose == "doggy" or focused_Girl.Pose == "sex"):
                    $ ShowFeet = 0
                "Undress [focused_Girl.name]":
                    call Girl_Undress(focused_Girl)
                "Clean up [focused_Girl.name] (locked)" if not focused_Girl.Spunk:
                    pass
                "Clean up [focused_Girl.name]" if focused_Girl.Spunk:
                    call Girl_Cleanup(focused_Girl,"ask")
                "Never mind":
                    jump sex_cycle
        "Back to Sex Menu" if MultiAction:
            ch_p "Let's try something else."

            call sex_reset(focused_Girl)

            $ action_context = "shift"
            $ line = 0

            jump after_action
        "End Scene" if not MultiAction:
            ch_p "Let's stop for now."

            call sex_reset(focused_Girl)

            $ line = 0

            jump after_action

    jump sex_menu_return

label sex_set_modifier(Girl, action):
    if action == "sex":
        if Girl.Sex >= 7: # She loves it
            $ temp_modifier += 15
        elif Girl.Sex >= 3: #You've done it before several times
            $ temp_modifier += 12
        elif Girl.Sex: #You've done it before
            $ temp_modifier += 10

        if Girl.Addict >= 75 and (Girl.CreamP + Girl.CreamA) >=3: #She's really strung out and has creampied
            $ temp_modifier += 20
        elif Girl.Addict >= 75:
            $ temp_modifier += 15

        if Girl.lust > 85:
            $ temp_modifier += 10
        elif Girl.lust > 75: #She's really horny
            $ temp_modifier += 5

        if action_context == "shift":
            $ temp_modifier += 10
        if "exhibitionist" in Girl.Traits:
            $ temp_modifier += (4*Taboo)
    elif action == "anal":
        if Girl.Anal >= 7: # She loves it
            $ temp_modifier += 20
        elif Girl.Anal >= 3: #You've done it before several times
            $ temp_modifier += 17
        elif Girl.Anal: #You've done it before
            $ temp_modifier += 15

        if Girl.Addict >= 75 and (Girl.CreamP + Girl.CreamA) >=3: #She's really strung out and has creampied
            $ temp_modifier += 25
        elif Girl.Addict >= 75:
            $ temp_modifier += 15

        if Girl.lust > 85:
            $ temp_modifier += 10
        elif Girl.lust > 75: #She's really horny
            $ temp_modifier += 5

        if Girl.Loose:
            $ temp_modifier += 10
        elif "anal" in Girl.recent_history:
            $ temp_modifier -= 20
        elif "anal" in Girl.daily_history:
            $ temp_modifier -= 10

        if action_context == "shift":
            $ temp_modifier += 10
        if "exhibitionist" in Girl.Traits:
            $ temp_modifier += (5*Taboo)
    elif action == "hotdog":
        if Girl.Hotdog >= 3: #You've done it before several times
            $ temp_modifier += 10
        elif Girl.Hotdog: #You've done it before
            $ temp_modifier += 5

        if Girl.lust > 85:
            $ temp_modifier += 10
        elif Girl.lust > 75: #She's really horny
            $ temp_modifier += 5
        if action_context == "shift":
            $ temp_modifier += 10
        if "exhibitionist" in Girl.Traits:
            $ temp_modifier += (3*Taboo)

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

label end_of_sex_round(Girl, action):
    $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus

    if Player.Focus >= 100 or Girl.lust >= 100:
        if Player.Focus >= 100:
            call Player_Cumming(Girl)

            if "angry" in Girl.recent_history:
                call sex_reset(Girl)

                return True

            $ Girl.change_stat("lust", 200, 5)

            if 100 > Girl.lust >= 70 and Girl.OCount < 2:
                $ Girl.AddWord(0, "unsatisfied", "unsatisfied")

            if Player.Focus > 80:
                call after_action(Girl, action)

                return True

            $ line = "came"

        if Girl.lust >= 100:
            call Girl_Cumming(Girl)

            if action_context == "shift" or "angry" in Girl.recent_history:
                call after_action(Girl, action)

                return True

        if line == "came": #ex Player.Focus <= 20:
            $ line = 0

            if not Player.Semen:
                "She's emptied you out, you'll need to take a break."

                call after_action(Girl, action)

                return True
            elif "unsatisfied" in Girl.recent_history:#And Rogue is unsatisfied,
                call not_ready_to_stop_lines(Girl)

                menu:
                    extend "Keep going?"
                    "Yes, keep going for a bit." if Player.Semen:
                        $ line = "You get back into it"
                    "No, I'm done." if Player.Semen:
                        "You pull back."

                        call after_action(Girl, action)

                        return True
                    "No, I'm spent." if not Player.Semen:
                        "You pull back."

                        call after_action(Girl, action)

                        return True

    if Partner and Partner.lust >= 100:
        call Girl_Cumming(Partner)

    $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

    if action == "sex":
        $ bonus = Girl.Sex
    elif action == "anal":
        $ bonus = Girl.Anal
    elif action == "hotdog":
        $ bonus = Girl.Hotdog

    if Girl.SEXP >= 100 or ApprovalCheck(Girl, 1200, "LO"):
        pass
    elif counter == (5 + bonus):
        $ Girl.Brows = "confused"

        call getting_close_lines(Girl)
    elif counter == (10 + bonus):
        $ Girl.Brows = "angry"

        call done_with_this_lines(Girl)
        call can_we_do_something_else_lines(Girl)

        menu:
            extend ""
            "How about a BJ?" if Girl.Action and MultiAction:
                if action != "anal":
                    $ action_context = "shift"

                    call after_action(Girl, action)
                    call blowjob(Girl)
                else:
                    if Girl.Anal >= 5 and Girl.Blow >= 10 and Girl.SEXP >= 50:
                        $ action_context = "shift"

                        call after_action(Girl, action)
                        call blowjob(Girl)
                    else:
                        call no_ass_to_mouth_lines(Girl)

                        $ action_context = "shift"

                        call after_action(Girl, action)
                        call before_handjob(Girl, "handjob")
            "How about a Handy?" if Girl.Action and MultiAction:
                $ action_context = "shift"

                call after_action(Girl, action)
                call handjob(Girl)
            "Finish up.":
                "You release your concentration. . ."

                $ Player.FocusX = 0
                $ Player.Focus += 15

                call after_action(Girl, action)

                return True
            "Let's try something else." if MultiAction:
                $ line = 0
                $ action_context = "shift"

                call after_action(Girl, action)

                return True
            "No, get back down there.":
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

                    call after_action(Girl, action)

                    return True

    call Escalation(Girl)

    if Round == 10:
        call wrap_this_up_lines(Girl)
    elif Round == 5:
        call time_to_stop_soon_lines(Girl)

    return False

label sex(Girl):
    $ primary_action = "sex"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(Girl)
    call sex_set_modifier(Girl, "sex")

    $ Approval = ApprovalCheck(Girl, 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)

    if action_context == "auto":
        $ Girl.Pose = "doggy"

        call sex_launch(Girl, "sex")

        if Girl.wearing_skirt:
            "You press up against [Girl.name]'s backside, sliding her skirt up as you go."

            $ Girl.Upskirt = 1
        elif Girl.PantsNum() > 6:
            "You press up against [Girl.name]'s backside, sliding her pants down as you do."

            $ Girl.Legs = 0
        else:
            "You press up against [Girl.name]'s backside."

        $ Girl.SeenPanties = 1

        "You rub the tip of your cock against her moist slit."

        $ Girl.change_face("surprised", 1)

        if (Girl.Sex and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
            "[Girl.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."

            $ Girl.change_face("sexy")
            $ Girl.change_stat("obedience", 70, 3)
            $ Girl.change_stat("inhibition", 50, 3)
            $ Girl.change_stat("inhibition", 70, 1)

            call lets_do_this_lines(Girl)

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

                    if Girl.Sex:
                        ch_r "Well ok, [Girl.Petname], no harm done. Just give me a little warning next time."
                    else:
                        ch_r "Well ok, [Girl.Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."
                "Just fucking.":
                    $ Girl.change_stat("love", 80, -10, 1)
                    $ Girl.change_stat("love", 200, -10)

                    "You press inside some more."

                    $ Girl.change_stat("obedience", 70, 3)
                    $ Girl.change_stat("inhibition", 50, 3)

                    if not ApprovalCheck(Girl, 700, "O", TabM=1):   #Checks if obedience is 700+
                        $ Girl.change_face("angry")

                        call were_done_here_lines(Girl)

                        $ Girl.change_stat("love", 50, -10, 1)
                        $ Girl.change_stat("obedience", 50, 3)

                        $ renpy.pop_call()

                        if action_context:
                            $ renpy.pop_call()

                        call sex_reset(Girl)

                        $ Girl.recent_history.append("angry")
                        $ Girl.daily_history.append("angry")
                    else:
                        $ Girl.change_face("sad")

                        call knows_her_place_lines(Girl)

                        jump before_action
        return

    if not Girl.Sex and "no sex" not in Girl.recent_history:                           #first time
        $ Girl.change_face("surprised", 1)
        $ Girl.Mouth = "kiss"

        ch_r "So, you'd like to take this to the next level? Actual sex? . . ."

        if Girl.Forced:
            $ Girl.change_face("sad")

            ch_r "You'd really take it that far?"

    if not Girl.Sex and Approval:                                                  #First time dialog
        call first_action_approval(Girl, "sex")
    elif Approval:
        call action_approved(Girl, "sex", Girl.Sex)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(Girl, "sex")

        return
    else:                                                                               #She's not into it, but maybe. . .
        call action_disapproved(Girl, "sex", Girl.Sex)

    $ Girl.ArmPose = 1

    call action_rejected(Girl, "sex", Girl.Sex)

    return

label anal(Girl):
    $ primary_action = "anal"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(Girl)
    call sex_set_modifier(Girl, "anal")

    $ Approval = ApprovalCheck(Girl, 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)

    if action_context == "auto":
        $ Girl.Pose = "doggy"

        call sex_launch(Girl, "anal")

        if Girl.wearing_skirt:
            "You press up against [Girl.name]'s backside, sliding her skirt up as you go."

            $ Girl.Upskirt = 1
        elif Girl.PantsNum() > 6:
            "You press up against [Girl.name]'s backside, sliding her pants down as you do."

            $ Girl.Legs = 0
        else:
            "You press up against [Girl.name]'s backside."

        $ Girl.SeenPanties = 1

        "You press the tip of your cock against her tight rim."

        $ Girl.change_face("surprised", 1)

        if (Girl.Anal and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
            "[Girl.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."

            $ Girl.change_face("sexy")
            $ Girl.change_stat("obedience", 70, 3)
            $ Girl.change_stat("inhibition", 50, 3)
            $ Girl.change_stat("inhibition", 70, 1)

            ch_r "Hmm, stick it in. . ."

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

                    if Girl.Anal:
                        ch_r "Well ok, [Girl.Petname], no harm done. Just give me a little warning next time."
                    else:
                        ch_r "Well ok, [Girl.Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."
                "Just fucking.":
                    $ Girl.change_stat("love", 80, -10, 1)
                    $ Girl.change_stat("love", 200, -8)

                    "You press into her."

                    $ Girl.change_stat("obedience", 70, 3)
                    $ Girl.change_stat("inhibition", 50, 3)

                    if not ApprovalCheck(Girl, 700, "O", TabM=1):
                        $ Girl.change_face("angry")

                        call were_done_here_lines(Girl)

                        $ Girl.change_stat("love", 50, -10, 1)
                        $ Girl.change_stat("obedience", 50, 3)

                        $ renpy.pop_call()

                        if action_context:
                            $ renpy.pop_call()

                        call sex_reset(Girl)

                        $ Girl.recent_history.append("angry")
                        $ Girl.daily_history.append("angry")
                    else:
                        $ Girl.change_face("sad")

                        call knows_her_place_lines(Girl)

                        jump before_action
        return

    if not Girl.Anal and "no anal" not in Girl.recent_history:                                                               #first time
        $ Girl.change_face("surprised", 1)
        $ Girl.Mouth = "kiss"

        ch_r "Wait, so you want to stick it in my butt?!"

        if Girl.Forced:
            $ Girl.change_face("sad")

            ch_r "Seriously?"

    if not Girl.Loose and ("dildo anal" in Girl.daily_history or "anal" in Girl.daily_history):
        $ Girl.change_face("bemused", 1)

        call ass_sore_lines(Girl)
    elif "anal" in Girl.recent_history:
        $ Girl.change_face("sexy", 1)

        call recent_action_lines(Girl)
        call before_action

    if not Girl.Anal and Approval:                                                 #First time dialog
        call first_action_approval(Girl, "anal")
    elif Approval:
        call action_approved(Girl, "anal", Girl.Anal)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(Girl, "anal")

        return
    else:                                                                               #She's not into it, but maybe. . .
        call action_disapproved(Girl, "anal", Girl.Anal)

    $ Girl.ArmPose = 1

    call action_rejectd(Girl, "anal", Girl.Anal)

    return

label hotdog(Girl):
    $ primary_action = "hotdog"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(Girl)
    call sex_set_modifier(Girl, "hotdog")

    $ Approval = ApprovalCheck(Girl, 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)

    if action_context == "auto":
        $ Girl.Pose = "doggy"

        call sex_launch("hotdog")

        "You press up against [Girl.name]'s backside."

        $ Girl.change_face("surprised", 1)

        if (Girl.Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
            "[Girl.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."

            $ Girl.change_face("sexy")
            $ Girl.change_stat("obedience", 70, 3)
            $ Girl.change_stat("inhibition", 50, 3)
            $ Girl.change_stat("inhibition", 70, 1)

            ch_r "Hmm, I've apparently got someone's attention. . ."

            jump before_action
        else:                                                                                                            #she's questioning it
            $ Girl.Brows = "angry"

            menu:
                ch_r "Hmm, kinda rude, [Girl.Petname]."
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

                    if Girl.Hotdog:
                        ch_r "Well ok, [Girl.Petname], it has been kinda fun."
                    else:
                        ch_r "Well ok, [Girl.Petname], that's a bit dirty, maybe ask a girl?"
                "You'll see.":
                    $ Girl.change_stat("love", 80, -10, 1)
                    $ Girl.change_stat("love", 200, -8)

                    "You grind against her asscrack."

                    $ Girl.change_stat("obedience", 70, 3)
                    $ Girl.change_stat("inhibition", 50, 3)

                    if not ApprovalCheck(Girl, 500, "O", TabM=1): #Checks if obedience is 700+
                        $ Girl.change_face("angry")

                        call were_done_here_lines(Girl)

                        $ Girl.change_stat("love", 50, -10, 1)
                        $ Girl.change_stat("obedience", 50, 3)

                        $ renpy.pop_call()

                        if action_context:
                            $ renpy.pop_call()

                        call sex_reset(Girl)

                        $ Girl.recent_history.append("angry")
                        $ Girl.daily_history.append("angry")
                    else:
                        $ Girl.change_face("sad")

                        call knows_her_place_lines(Girl)

                        jump before_action
        return

    if not Girl.Hotdog and "no hotdog" not in Girl.recent_history:                                                               #first time
        $ Girl.change_face("surprised", 1)
        $ Girl.Mouth = "kiss"

        ch_r "Wait, so you want to grind against my butt?!"

        if Girl.Forced:
            $ Girl.change_face("sad")

            ch_r ". . . That's all?"

    if not Girl.Hotdog and Approval:                                                 #First time dialog
        call first_action_approval(Girl, "hotdog")
    elif Approval:                                                                       #Second time+ dialog
        call action_approved(Girl, "hotdog", Girl.Hotdog)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(Girl, "hotdog")

        return
    else:                                                                               #She's not into it, but maybe. . .
        call action_rejected(Girl, "hotdog", Girl.Hotdog)

    $ Girl.ArmPose = 1

    call action_rejected(Girl, "hotdog", Girl.Hotdog)

    return
