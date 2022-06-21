label masturbate(Girl, context = None):
    while True:
        call set_approval_bonus(Girl, "masturbation", context)
        $ approval_bonus = _return

        call action_approval_checks(Girl, "masturbation")
        $ approval = _return

        $ Girl.drain_word("unseen", 1, 0)

        $ accepted = False

        if context == "join":
            if approval > 1 or (approval and Girl.lust >= 50):
                menu:
                    extend ""
                    "Would you like some help? I could lend some helping hands. . ." if Girl.remaining_actions:
                        $ Girl.change_stat("love", 90, 1)
                        $ Girl.change_stat("obedience", 50, 2)
                        $ Girl.change_face("_sexy")

                        call lend_some_helping_hands_lines(Girl, "masturbation")

                        $ Girl.change_stat("obedience", 70, 2)
                        $ Girl.change_stat("inhibition", 70, 1)

                        $ Girl.action_counter["masturbation"] += 1

                        call start_action(Girl, "fondle_breasts", "auto")

                        return _return
                    "Would you like some help? I could. . . up to you, I guess." if Player.semen and Girl.remaining_actions:
                        $ Girl.change_stat("love", 70, 2)
                        $ Girl.change_stat("love", 90, 1)
                        $ Girl.change_face("_sexy")

                        call lend_some_helping_hands_lines(Girl, "masturbation")

                        $ Girl.change_stat("obedience", 70, 2)
                        $ Girl.change_stat("inhibition", 70, 1)

                        $ D20 = renpy.random.randint(1, 20)

                        $ Girl.action_counter["masturbation"] += 1

                        if D20 > 10:
                            call start_action(Girl, "fondle_breasts", "auto")
                        else:
                            call start_action(Girl, "suck_breasts", "auto")

                        return _return
                    "Why don't we take care of each other?" if Player.semen and Girl.remaining_actions:
                        $ Girl.change_face("_sexy")

                        call why_dont_we_take_care_of_each_other_lines(Girl, "masturbation")
                        call enter_main_sex_menu(Girl)

                        return "switch"
                    "You look like you have things well in hand. . .":
                        if Girl.lust >= 50:
                            $ Girl.change_stat("love", 70, 2)
                            $ Girl.change_stat("love", 90, 1)
                            $ Girl.change_face("_sexy")

                            call well_in_hand_lust_lines(Girl, "masturbation")

                            $ Girl.change_stat("obedience", 80, 3)
                            $ Girl.change_stat("inhibition", 80, 5)

                            $ accepted = True
                        elif approval_check(Girl, 1000):
                            $ Girl.change_face("_sly")

                            call well_in_hand_approved_lines(Girl, "masturbation")
                        else:
                            $ Girl.change_face("_angry")

                            call well_in_hand_disapproved_lines(Girl, "masturbation")

            if not accepted:
                $ Girl.change_outfit()
                $ Girl.arm_pose = 1
                $ Girl.remaining_actions -= 1

                $ Player.change_stat("focus", 50, 30)

                call checkout(total = True)

                if approval:
                    $ Girl.change_face("_bemused", 2)

                    if bg_current == "bg_rogue":
                        call what_did_you_come_over_for_approval_lines(Girl, "masturbation")
                    else:
                        call fancy_bumping_into_you_approval_lines(Girl, "masturbation")

                    $ Girl.blushing = "_blush1"
                else:
                    $ Girl.change_stat("love", 200, -5)
                    $ Girl.change_face("_angry")
                    $ Girl.recent_history.append("_angry")
                    $ Girl.daily_history.append("_angry")

                    if bg_current == "bg_rogue":
                        call what_did_you_come_over_for_disapproval_lines(Girl, "masturbation")

                        jump reset_location
                    else:
                        call fancy_bumping_into_you_disapproval_lines(Girl, "masturbation")
                        call remove_girl(Girl)

                return "stop"

        if not accepted:
            if not Girl.action_counter["masturbation"] and "no_masturbation" not in Girl.recent_history:
                call first_time_asking_reactions(Girl, "masturbation")

            if not Girl.action_counter["masturbation"] and approval:
                call first_action_approval(Girl, "masturbation")
            elif approval:
                call action_approved(Girl, "masturbation")

            if approval >= 2:
                call action_accepted(Girl, "masturbation")

                $ accepted = True
            else:
                call action_disapproved(Girl, "masturbation")

                if _return == "rejected":
                    return "back"
                else:
                    $ action = _return

                    $ accepted = True

        if not accepted:
            call action_rejected(Girl, "masturbation")

            return "back"

        call before_masturbation(Girl)
        call masturbation_cycle(Girl)

        if _return == "interrupt":
            call after_masturbation(Girl, "interrupt")

            if _return == "switch":
                return "switch"
            elif _return == "stop":
                return "stop"
        elif _return == "switch":
            call after_masturbation(Girl, "switch")
            call stop_all_actions

            return "switch"
        elif _return == "stop":
            call after_masturbation(Girl, "stop")
            call stop_all_actions

            return "stop"

label before_masturbation(Girl):
    call expose_pussy(Girl)

    if "unseen" in Girl.recent_history:
        $ Girl.change_face("_sexy", eyes = "_closed")
        $ Girl.arm_pose = 2

        "You see [Girl.name] leaning back, masturbating. You don't think she's noticed you yet."
    else:
        $ Girl.change_face("_sexy")
        $ Girl.arm_pose = 2

        "[Girl.name] lays back and starts to toy with herself."

        if not Girl.action_counter["masturbation"]:
            if Girl.forced:
                $ Girl.change_stat("love", 90, -20)
                $ Girl.change_stat("obedience", 70, 45)
                $ Girl.change_stat("inhibition", 80, 35)
            else:
                $ Girl.change_stat("love", 90, 15)
                $ Girl.change_stat("obedience", 70, 35)
                $ Girl.change_stat("inhibition", 80, 40)

    if taboo:
        $ Girl.drain_word("no_taboo")

    $ Girl.drain_word("no_masturbation")
    $ Girl.recent_history.append("masturbation")
    $ Girl.daily_history.append("masturbation")

    $ Player.primary_action = "masturbation"
    $ girl_secondary_action = "fondle_pussy"

    return

label masturbation_cycle(Girl):
    while round > 0:
        $ stack_depth = renpy.call_stack_depth()

        call reset_position(Girl)

        $ Girl.lust_face()

        if "unseen" in Girl.recent_history:
            $ Girl.eyes = "_closed"

        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if Player.focus < 100:
            call masturbation_menu(Girl)

            if _return != "continue":
                $ context = _return

                return context

        call Sex_Dialog(Girl, Partner)

        $ counter += 1
        $ round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus

        if Player.focus >= 100 or Girl.lust >= 100:
            $ orgasmed = False

            if Player.focus >= 100:
                if "unseen" not in Girl.recent_history:
                    call Player_Cumming (Girl)

                    if "_angry" in Girl.recent_history:
                        call reset_position(Girl)

                        return "stop"

                    $ Girl.change_stat("lust", 200, 5)

                    if 100 > Girl.lust >= 70 and Girl.session_orgasms < 2:
                        $ Girl.recent_history.append("unsatisfied")
                        $ Girl.daily_history.append("unsatisfied")

                    $ orgasmed = True
                else:
                    "You grunt and try to hold it in."

                    $ Player.focus = 95

                    if Girl.location == bg_current or (bg_current == "bg_classroom" and Girl.location == "bg_teacher"):
                        return "interrupt"

            if Girl.lust >= 100:
                call Girl_Cumming (Girl)

                if Girl.location == bg_current or (bg_current == "bg_classroom" and Girl.location == "bg_teacher"):
                    return "interrupt"

            if orgasmed:
                if not Player.semen:
                    "You're emptied out, you should probably take a break."

                    $ Player.secondary_action = None if Player.secondary_action == "jerking_off" else Player.secondary_action

                if "unsatisfied" in Girl.recent_history:
                    call girl_unsatisfied_menu(Girl, "masturbation")

                    if _return == "stop":
                        return "stop"

        if Partner and Partner.lust >= 100:
            call Girl_Cumming (Partner)

        if "unseen" in Girl.recent_history:
            if round == 10:
                "It's getting a bit late, [Girl.name] will probably be wrapping up soon."
            elif round == 5:
                "She's definitely going to stop soon."
        else:
            if Girl.location == bg_current:
                call Escalation(Girl)

            if round == 10:
                call ten_rounds_left_lines(Girl, "masturbation")

                $ Girl.lust += 10
            elif round == 5:
                call five_rounds_left_lines(Girl, "masturbation")

                $ Girl.lust += 25

    $ Girl.change_face("_bemused", 0)

    if "unseen" not in Girl.recent_history:
        call end_of_action_lines(Girl, "masturbation")

    return "stop"

label after_masturbation(Girl, context):
    if context == "interrupt":
        $ Girl.change_face("_surprised", 1)

        $ girl_secondary_action = None

        "[Girl.name] stops what she's doing with a start, eyes wide."

        call expression Girl.tag + "_First_Bottomless" pass(1)

        $ Girl.change_face("_surprised", 1)

        if Player.secondary_action == "jerking_off":
            call caught_masturbating_lines(Girl, "masturbation")

            $ Girl.eyes = "_down"

            call notices_penis_is_out_lines(Girl, "masturbation")

            menu:
                "Long enough, it was an excellent show.":
                    $ Girl.change_face("_sexy")
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_stat("obedience", 70, 2)

                    call masturbation_excellent_show_cock_out_lines(Girl, "masturbation")

                    if Girl.love >= 800 or Girl.obedience >= 500 or Girl.inhibition >= 500:
                        $ approval_bonus += 10
                        $ Girl.change_stat("lust", 90, 5)

                        call masturbation_excellent_show_cock_out_happy_lines(Girl, "masturbation")
                "I. . . just got here?":
                    $ Girl.change_face("_angry")
                    $ Girl.change_stat("love", 70, 2)
                    $ Girl.change_stat("love", 90, 1)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("obedience", 70, 2)

                    "She looks pointedly at your cock."

                    call masturbation_just_got_here_cock_out_lines(Girl, "masturbation")

                    if Girl.love >= 800 or Girl.obedience >= 500 or Girl.inhibition >= 500:
                        $ approval_bonus += 10

                        $ Girl.change_stat("lust", 90, 5)
                        $ Girl.change_face("_bemused", 1)

                        call masturbation_just_got_here_cock_out_happy_lines(Girl, "masturbation")
                    else:
                        $ approval_bonus -= 10

                        $ Girl.change_stat("lust", 200, -5)

            call Seen_First_Peen(Girl, Partner)

            Girl.voice "Hmm. . ."
        else:
            call caught_masturbating_lines(Girl, "masturbation")

            menu:
                extend ""
                "Long enough.":
                    $ Girl.change_face("_sexy", 1)
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_stat("obedience", 70, 2)

                    call masturbation_watching_for_long_enough_lines(Girl, "masturbation")
                "I just got here.":
                    $ Girl.change_face("_bemused", 1)
                    $ Girl.change_stat("love", 70, 2)
                    $ Girl.change_stat("love", 90, 1)

                    call masturbation_just_got_here_lines(Girl, "masturbation")

                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("obedience", 70, 2)

        $ Girl.drain_word("unseen", 1, 0)
        $ Girl.action_counter["masturbation"] += 1

        if round <= 10:
            call too_late_to_masturbate_lines(Girl, "masturbation")

            return "stop"

        return "join"
    else:
        $ Girl.remaining_actions -= 1
        $ Girl.action_counter["masturbation"] += 1

        if Partner == EmmaX:
            call Partner_Like(Girl, 4)
        else:
            call Partner_Like(Girl, 3)

        call checkout

        if Girl.location != bg_current:
            return "stop"

        if round <= 10:
            call masturbation_worn_out_lines(Girl, "masturbation")

            return "stop"

        $ Girl.change_face("_sexy", 1)

        if Girl.lust < 20:
            call end_of_masturbation_satisfied_lines(Girl, "masturbation")
        else:
            call end_of_masturbation_lines(Girl, "masturbation")

        menu:
            extend ""
            "Well, I have something you could take care of. . ." if Player.semen and Girl.remaining_actions:
                return "switch"
            "You could just keep going. . ." if Player.semen:
                $ Girl.change_face("_sly")

                if Girl.remaining_actions and round >= 10:
                    call masturbation_keep_going_lines(Girl, "masturbation")

                    return "continue"
                else:
                    call masturbation_worn_out_lines(Girl, "masturbation")

                return "continue"
            "I'm good here. [[Stop]":
                if Girl.love < 800 and Girl.inhibition < 500 and Girl.obedience < 500:
                    $ Girl.change_outfit()

                $ Girl.change_face("_normal")
                $ Girl.brows = "_confused"

                call masturbation_good_here_lines(Girl, "masturbation")

                $ Girl.brows = "_normal"
            "You should probably stop for now." if Girl.lust > 30:
                $ Girl.change_face("_angry")

                call masturbation_stop_for_now_lines(Girl, "masturbation")

    return "stop"
