label sex_acts(action = 0):
    if Alonecheck(focused_Girl) and focused_Girl.Taboo == 20:
        $ focused_Girl.Taboo = 0
        $ Taboo = 0

    call shift_focus(focused_Girl)

    if action == "SkipTo":
        $ renpy.pop_call() #causes it to skip past the Trigger Swap
        $ renpy.pop_call()

        call SkipTo(focused_Girl)
    elif action == "switch":
        $ renpy.pop_call()
    elif action == "masturbation":
        call before_show

        if not action_context:
            return
    elif action == "lesbian":
        call Les_Prep(focused_Girl)

        if not action_context:
            return
    elif action == "kiss":
        call before_action

        if not action_context:
            return
    elif action == "fondle_breasts":
        call fondle_breasts(focused_Girl)

        if not action_context:
            return
    elif action in ["handjob", "blowjob"]:
        call before_action

        if not action_context:
            return
    elif action == "sex":
        call before_action

        if not action_context:
            return

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

            jump action_cycle
        "Turn her around":
            $ focused_Girl.Pose = "doggy" if focused_Girl.Pose != "doggy" else "sex"

            "You turn her around. . ."

            jump action_cycle
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
                    if focused_Girl.action and multi_action:
                        call Offhand_Set

                        if offhand_action:
                            $ focused_Girl.action -= 1
                    else:
                        call Sex_Basic_Dialog(focused_Girl,"tired")
                "Shift primary action":
                    if focused_Girl.action and multi_action:
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
                                jump action_cycle
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
                        "Don't stop what you're doing. . .(locked)" if not position_change_timer or not second_girl_primary_action:
                            $ position_change_timer = 0
                        "Don't stop what you're doing. . ." if position_change_timer and second_girl_primary_action:
                            $ position_change_timer = 0
                        "Swap to [Partner.name]":
                            call primary_action_Swap(focused_Girl)
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
                    jump action_cycle
        "Back to Sex Menu" if multi_action:
            ch_p "Let's try something else."

            call sex_reset(focused_Girl)

            $ action_context = "shift"
            $ line = 0

            jump after_action
        "End Scene" if not multi_action:
            ch_p "Let's stop for now."

            call sex_reset(focused_Girl)

            $ line = 0

            jump after_action

    jump sex_menu_return

label sex_set_modifier(Girl, action):
    if action == "sex":
        if Girl.action_counter["sex"] >= 7: # She loves it
            $ temp_modifier += 15
        elif Girl.action_counter["sex"] >= 3: #You've done it before several times
            $ temp_modifier += 12
        elif Girl.action_counter["sex"]: #You've done it before
            $ temp_modifier += 10

        if Girl.Addict >= 75 and (Girl.event_counter["creampied"] + Girl.event_counter["anal_creampied"]) >=3: #She's really strung out and has creampied
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
        if Girl.action_counter["anal"]  >= 7: # She loves it
            $ temp_modifier += 20
        elif Girl.action_counter["anal"]  >= 3: #You've done it before several times
            $ temp_modifier += 17
        elif Girl.action_counter["anal"] : #You've done it before
            $ temp_modifier += 15

        if Girl.Addict >= 75 and (Girl.event_counter["creampied"] + Girl.event_counter["anal_creampied"]) >=3: #She's really strung out and has creampied
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
        if Girl.action_counter["hotdog"] >= 3: #You've done it before several times
            $ temp_modifier += 10
        elif Girl.action_counter["hotdog"]: #You've done it before
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

label sex(Girl):
    $ primary_action = "sex"

    $ Round -= 5 if Round > 5 else (Round-1)

    call shift_focus(Girl)
    call sex_set_modifier(Girl, "sex")

    $ Approval = Approvalcheck(Girl, 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)

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

        if (Girl.action_counter["sex"] and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
            "[Girl.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."

            $ Girl.change_face("sexy")
            $ Girl.change_stat("obedience", 70, 3)
            $ Girl.change_stat("inhibition", 50, 3)
            $ Girl.change_stat("inhibition", 70, 1)

            call lets_do_this_lines(Girl)

            jump before_action
        else:                                                                                                            #she's questioning it
            $ Girl.Brows = "angry"

            call what_do_you_think_youre_doing_lines(Girl)

            menu:
                extend ""
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

                    call pull_back_before_get_in_lines(Girl)
                "Just fucking.":
                    $ Girl.change_stat("love", 80, -10, 1)
                    $ Girl.change_stat("love", 200, -10)

                    "You press inside some more."

                    $ Girl.change_stat("obedience", 70, 3)
                    $ Girl.change_stat("inhibition", 50, 3)

                    if not Approvalcheck(Girl, 700, "O", TabM=1):   #checks if obedience is 700+
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

    if not Girl.action_counter["sex"] and "no_sex" not in Girl.recent_history:                           #first time
        $ Girl.change_face("surprised", 1)
        $ Girl.Mouth = "kiss"

        call first_time_asking_lines(Girl)

        if Girl.Forced:
            $ Girl.change_face("sad")

            call first_time_forcing_lines(Girl)

    if not Girl.action_counter["sex"] and Approval:                                                  #First time dialog
        call first_action_approval(Girl, "sex")
    elif Approval:
        call action_approved(Girl, "sex", Girl.action_counter["sex"])

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(Girl, "sex")

        return
    else:                                                                               #She's not into it, but maybe. . .
        call action_disapproved(Girl, "sex", Girl.action_counter["sex"])

    $ Girl.ArmPose = 1

    call action_rejected(Girl, "sex", Girl.action_counter["sex"])

    return

label anal(Girl):
    $ primary_action = "anal"

    $ Round -= 5 if Round > 5 else (Round-1)

    call shift_focus(Girl)
    call sex_set_modifier(Girl, "anal")

    $ Approval = Approvalcheck(Girl, 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)

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

        if (Girl.action_counter["anal"]  and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
            "[Girl.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."

            $ Girl.change_face("sexy")
            $ Girl.change_stat("obedience", 70, 3)
            $ Girl.change_stat("inhibition", 50, 3)
            $ Girl.change_stat("inhibition", 70, 1)

            call lets_do_this_lines(Girl)

            jump before_action
        else:                                                                                                            #she's questioning it
            $ Girl.Brows = "angry"

            call what_do_you_think_youre_doing_lines(Girl)

            menu:
                extend ""
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

                    call pull_back_before_get_in_lines(Girl)
                "Just fucking.":
                    $ Girl.change_stat("love", 80, -10, 1)
                    $ Girl.change_stat("love", 200, -8)

                    "You press into her."

                    $ Girl.change_stat("obedience", 70, 3)
                    $ Girl.change_stat("inhibition", 50, 3)

                    if not Approvalcheck(Girl, 700, "O", TabM=1):
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

    if not Girl.action_counter["anal"]  and "no_anal" not in Girl.recent_history:                                                               #first time
        $ Girl.change_face("surprised", 1)
        $ Girl.Mouth = "kiss"

        call first_time_asking_lines(Girl)

        if Girl.Forced:
            $ Girl.change_face("sad")

            call first_time_forcing_lines(Girl)

    if not Girl.Loose and ("dildo_anal" in Girl.daily_history or "anal" in Girl.daily_history):
        $ Girl.change_face("bemused", 1)

        call ass_sore_lines(Girl)
    elif "anal" in Girl.recent_history:
        $ Girl.change_face("sexy", 1)

        call recent_action_lines(Girl)
        call before_action

    if not Girl.action_counter["anal"]  and Approval:                                                 #First time dialog
        call first_action_approval(Girl, "anal")
    elif Approval:
        call action_approved(Girl, "anal", Girl.action_counter["anal"] )

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(Girl, "anal")

        return
    else:                                                                               #She's not into it, but maybe. . .
        call action_disapproved(Girl, "anal", Girl.action_counter["anal"] )

    $ Girl.ArmPose = 1

    call action_rejectd(Girl, "anal", Girl.action_counter["anal"] )

    return

label hotdog(Girl):
    $ primary_action = "hotdog"

    $ Round -= 5 if Round > 5 else (Round-1)

    call shift_focus(Girl)
    call sex_set_modifier(Girl, "hotdog")

    $ Approval = Approvalcheck(Girl, 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)

    if action_context == "auto":
        $ Girl.Pose = "doggy"

        call sex_launch("hotdog")

        "You press up against [Girl.name]'s backside."

        $ Girl.change_face("surprised", 1)

        if (Girl.action_counter["hotdog"] and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
            "[Girl.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."

            $ Girl.change_face("sexy")
            $ Girl.change_stat("obedience", 70, 3)
            $ Girl.change_stat("inhibition", 50, 3)
            $ Girl.change_stat("inhibition", 70, 1)

            call lets_do_this_lines(Girl)

            jump before_action
        else:                                                                                                            #she's questioning it
            $ Girl.Brows = "angry"

            call what_do_you_think_youre_doing_lines(Girl)

            menu:
                extend ""
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

                    call pull_back_before_get_in_lines(Girl)
                "You'll see.":
                    $ Girl.change_stat("love", 80, -10, 1)
                    $ Girl.change_stat("love", 200, -8)

                    "You grind against her asscrack."

                    $ Girl.change_stat("obedience", 70, 3)
                    $ Girl.change_stat("inhibition", 50, 3)

                    if not Approvalcheck(Girl, 500, "O", TabM=1): #checks if obedience is 700+
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

    if not Girl.action_counter["hotdog"] and "no_hotdog" not in Girl.recent_history:                                                               #first time
        $ Girl.change_face("surprised", 1)
        $ Girl.Mouth = "kiss"

        call first_time_asking_lines(Girl)

        if Girl.Forced:
            $ Girl.change_face("sad")

            call first_time_forcing_lines(Girl)

    if not Girl.action_counter["hotdog"] and Approval:                                                 #First time dialog
        call first_action_approval(Girl, "hotdog")
    elif Approval:                                                                       #Second time+ dialog
        call action_approved(Girl, "hotdog", Girl.action_counter["hotdog"])

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(Girl, "hotdog")

        return
    else:                                                                               #She's not into it, but maybe. . .
        call action_rejected(Girl, "hotdog", Girl.action_counter["hotdog"])

    $ Girl.ArmPose = 1

    call action_rejected(Girl, "hotdog", Girl.action_counter["hotdog"])

    return
