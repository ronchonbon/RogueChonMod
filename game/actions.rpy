label start_action(Girl, action, context = None):
    while True:
        call set_approval_bonus(Girl, action, context)
        $ approval_bonus = _return

        call action_approval_checks(Girl, action)
        $ approval = _return

        if Girl == EmmaX and action == "kiss" and not approval_check(Girl, 1000):
            $ Girl.change_face("_sadside")

            ch_e "Not when we barely know each other. . ."

            return "back"

        $ accepted = False

        if context == "auto":
            call auto_action_narrations(Girl, action)

            if approval >= 2:
                call auto_approved_reactions(Girl, action)

                $ accepted = True
            else:
                call auto_rejected_reactions(Girl, action)

                if _return == "accepted":
                    $ accepted = True
                elif _return == "rejected":
                    return "back"
        elif context == "pullback":
            call pullback_reactions(Girl, action)

            $ accepted = True
        elif action in anal_insertion_actions and not Girl.used_to_anal and ("finger_ass" in Girl.daily_history or "dildo_ass" in Girl.daily_history or "anal" in Girl.daily_history):
            call anal_insertion_not_loose_done_today_reactions(Girl, action)

            $ Girl.recent_history.append("no_" + action)
            $ Girl.daily_history.append("no_" + action)

            return "back"
        elif action in Girl.recent_history:
            call recent_action_reactions(Girl, action)

            $ accepted = True
        elif action in Girl.daily_history:
            call daily_action_reactions(Girl, action)

            $ accepted = True

        if not accepted:
            if action == "kiss":
                if approval > 1 and not Girl.action_counter["kiss"] and not Girl.forced:
                    $ Girl.change_face("_sexy")
                    $ Girl.eyes = "_side"

                    call excited_for_first_kiss_lines(Girl, action)
                elif approval and not Girl.action_counter["kiss"]:
                    $ Girl.change_face("_sexy")
                    $ Girl.eyes = "_side"

                    call less_excited_for_first_kiss_lines(Girl, action)
                elif approval > 1 and Girl.love > Girl.obedience:
                    $ Girl.change_face("_sexy")

                    call excited_for_kiss_love_lines(Girl, action)
                elif approval_check(Girl, 500, "O") and Girl.obedience > Girl.love:
                    $ Girl.change_face("_normal")

                    call excited_for_kiss_obedience_lines(Girl, action)

                    $ Girl.change_stat("obedience", 60, 1)
                elif approval_check(Girl, 250, "O",Alt=[[KittyX,LauraX],300]) and approval_check(Girl, 250, "L",Alt=[[KittyX,LauraX],200]):
                    $ Girl.change_face("_bemused")

                    Girl.voice "Ok, fine."

                    $ Girl.change_stat("obedience", 50, 3)
                elif Girl.addiction >= 50:
                    $ Girl.change_face("_sexy")
                    $ Girl.eyes = "_manic"

                    call kiss_addicted_lines(Girl, action)
                elif approval:
                    $ Girl.change_face("_bemused")

                    call kiss_accepted_lines(Girl, action)
                else:
                    $ Girl.change_face("_normal")
                    $ Girl.mouth = "_sad"

                    call otherwise_not_interested_lines(Girl, action)

                    $ Girl.recent_history.append("no_" + action)
                    $ Girl.daily_history.append("no_" + action)

                    return "back"

                $ accepted = True
            else:
                if not Girl.action_counter[action] and "no_" + action not in Girl.recent_history:
                    call first_time_asking_reactions(Girl, action)

                if not Girl.action_counter[action] and approval:
                    call first_action_approval(Girl, action)
                elif approval:
                    call action_approved(Girl, action)

                if approval >= 2:
                    call action_accepted(Girl, action)

                    $ accepted = True
                else:
                    call action_disapproved(Girl, action)

                    if _return == "rejected":
                        return "back"
                    else:
                        $ action = _return

                        $ accepted = True

        if not accepted:
            call action_rejected(Girl, action)

            return "back"

        call before_action(Girl, action, context)

        if _return == "continue":
            call action_cycle(Girl, action, context)

            if _return[1] == "switch":
                call after_action(Girl, action, "switch")
                call stop_all_actions

                return "switch"
            elif _return[1] == "stop":
                call after_action(Girl, action, "stop")
                call stop_all_actions

                return "stop"
            else:
                $ action = _return[0]
                $ context = _return[1]
        elif _return == "stop":
            call stop_all_actions

            return "stop"

label before_action(Girl, action, context):
    $ Girl.change_face("_sexy")

    if action == "kiss":
        $ Girl.change_stat("inhibition", 10, 1)
        $ Girl.change_stat("inhibition", 20, 1)

        call kiss_launch(Girl)

        if Girl.action_counter["kiss"] >= 10 and Girl.inhibition >= 300:
            $ Girl.change_face("_sucking")
        elif Girl.action_counter["kiss"] > 1 and Girl.addiction >= 50:
            $ Girl.change_face("_sucking")
        else:
            $ Girl.change_face("_kiss",2)

        if Girl == RogueX and not Girl.action_counter["kiss"]:
            call Rogue_first_kiss

            return "stop"
        else:
            call kissing_narrations(Girl)
    elif action in fondle_actions:
        if not Girl.forced and context != "auto":
            $ approval_bonus = 0

            if action in ["eat_pussy", "eat_ass"]:
                $ approval_bonus = 15

            if action in inside_panties_actions:
                call Bottoms_Off(Girl)
            elif action in breast_actions:
                call Top_Off(Girl)

            if "_angry" in Girl.recent_history:
                return "stop"

        $ approval_bonus = 0
    elif action in job_actions:
        if action not in dildo_actions:
            if Girl.forced:
                $ Girl.change_face("_sad")
            elif not Girl.action_counter[action]:
                $ Girl.brows = "_confused"
                $ Girl.eyes = "_sexy"
                $ Girl.mouth = "_smile"
        else:
            if not Girl.forced and context != "auto":
                call Bottoms_Off(Girl)

                if "_angry" in Girl.recent_history:
                    return "stop"

            $ approval_bonus = 0

        call Seen_First_Peen(Girl, Partner, React = context)

        if action == "handjob":
            call show_handjob(Girl)
        elif action == "titjob":
            call show_titjob(Girl)
        elif action == "blowjob":
            call show_blowjob(Girl)
        elif action in dildo_actions:
            call pussy_launch(Girl)
    elif action in sex_actions:
        call Seen_First_Peen(Girl, Partner, React = context)

        $ Girl.pose = "doggy"

        call show_sex(Girl, action)

    if action not in sex_actions:
        if context == Girl:
            $ context = None

            call girl_initiated_action(Girl, action)

            if _return == "rejected":
                return "stop"
    elif action in sex_actions:
        if context == Girl:
            $ context = None

            call girl_initiated_action(Girl, action)

            if _return == "rejected":
                return "stop"

            call expose_bottom(Girl)
        elif context != "auto":
            if action in ["sex", "anal"]:
                call AutoStrip(Girl)
            elif action == "hotdog":
                call Bottoms_Off(Girl)

            call start_of_sex_narration(Girl, action)
        else:
            if action in ["sex", "anal"]:
                if action == "sex":
                    $ word = renpy.random.choice(["slit"])
                elif action == "anal":
                    $ word = renpy.random.choice(["ass", "back door"])

                if (Girl.wearing_pants and not Girl.bottom_pulled_down) and (Girl.outfit["underwear"] and not Girl.underwear_pulled_down):
                    "You quickly pull down her pants and her [Girl.outfit['underwear']] and press against her [word]."

                    $ Girl.bottom_pulled_down = True
                    $ Girl.underwear_pulled_down = True
                elif (Girl.outfit["underwear"] and not Girl.underwear_pulled_down):
                    "You quickly pull down her [Girl.outfit['underwear']] and press against her [word]."

                    $ Girl.underwear_pulled_down = True

                if Girl.wearing_skirt:
                    $ Girl.upskirt = True

                $ Girl.seen_underwear = True

                call expression Girl.tag + "_First_Bottomless" pass(1)
            elif action == "hotdog":
                $ line = renpy.random.choice(["You press yourself against her ass.",
                    "You press yourself against her mound.",
                    "You roll back, pulling her on top of you and your rigid member.",
                    "She lays back, pulling you against her with your rigid member.",
                    "She turns around, pulling you against her with your rigid member."])
                "[line]"

        if Player.focus >= 50:
            call hard_cock_lines(Girl, action)

    call first_action_changes(Girl, action)

    if taboo:
        if action == "fondle_thighs":
            $ Girl.change_stat("lust", 200, (int(taboo/5)))
            $ Girl.change_stat("inhibition", 200, (2*(int(taboo/5))))
        elif action in ["fondle_breasts", "suck_breasts", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "dildo_pussy", "dildo_ass"]:
            $ Girl.inhibition += int(taboo/10)
            $ Girl.lust += int(taboo/5)
        elif action in ["fondle_pussy", "eat_pussy", "finger_ass", "eat_ass"]:
            if Girl == JeanX and Girl.taboo:
                $ Girl.change_stat("inhibition", 200, (int(taboo/10)))
            elif taboo:
                $ Girl.inhibition += int(taboo/10)

            $ Girl.lust += int(taboo/5)

    if action in inside_panties_actions:
        call expose_bottom(Girl)

    if taboo:
        $ Girl.drain_word("no_taboo")

    $ Girl.drain_word("no_" + action)
    $ Girl.add_word(0, action, action)

    $ Player.primary_action = action

    if action in mouth_actions and Player.secondary_action in mouth_actions:
        $ Player.secondary_action = None
    elif action in cock_actions and Player.secondary_action in cock_actions:
        $ Player.secondary_action = None

    $ Player.sprite = True

    if action == "massage":
        $ Girl.pose = "doggy"

        $ Player.sprite = False
    elif action == "eat_pussy":
        if Girl.pose != "doggy":
            $ Girl.pose = "sex"

        $ Player.sprite = False
    elif action == "eat_ass":
        if Girl.pose != "sex":
            $ Girl.pose = "doggy"

        $ Player.sprite = False
    elif action in ["handjob", "titjob", "blowjob"]:
        $ Girl.pose = action
    elif action == "footjob" and Girl == EmmaX:
        $ Girl.pose = "footjob"
    elif action == "footjob":
        if Girl.pose != "sex":
            $ Girl.pose = "doggy"
    elif action == "hotdog":
        if Girl.pose != "sex":
            $ Girl.pose = "doggy"
    elif action == "sex":
        if Girl.pose != "doggy":
            $ Girl.pose = "sex"
    elif action == "anal":
        if Girl.pose != "sex":
            $ Girl.pose = "doggy"
    else:
        $ Girl.pose = "full"

    return "continue"

label action_cycle(Girl, action, context):
    while round > 0:
        $ stack_depth = renpy.call_stack_depth()

        if action == "kiss":
            call kiss_launch(Girl)

            $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0
        if action in fondle_actions:
            call shift_view(Girl, Girl.pose)
        elif action in ["massage", "footjob", "hotdog", "sex", "anal"]:
            call show_sex(Girl, action)
        elif action in dildo_actions:
            call shift_view(Girl, Girl.pose)

        $ Girl.lust_face()

        if Player.focus < 100:
            if action == "kiss":
                call kiss_menu(Girl)
            elif action in fondle_actions:
                call fondle_menu(Girl, action)
            elif action in job_actions:
                call handjob_menu(Girl, action)
            elif action in sex_actions:
                call sex_menu(Girl, action)

            if _return[1] == "switch":
                return [None, "switch"]
            elif _return[1] == "stop":
                return [None, "stop"]
            elif _return[1] != "continue":
                $ action = _return[0]
                $ context = _return[1]

                return [action, context]

        if action in inside_panties_actions:
            if Girl.outfit["underwear"] or Girl.legs_covered: #This checks if Rogue wants to strip down.
                call Girl_Undress(Girl, "auto")

        call Sex_Dialog(Girl, Partner)

        $ counter += 1
        $ round -= 1

        if (action in ["blowjob"] and action_speed) or action in ["sex", "anal"]:
            $ Player.cock_wet = True
            $ Player.spunk = False if (Player.spunk and not Girl.spunk["pussy"]) else Player.spunk #cleans you off after one cycle

        call end_of_action_round(Girl, action)

        if _return[1] == "switch":
            return [None, "switch"]
        elif _return[1] == "stop":
            return [None, "stop"]
        elif _return[1] != "continue":
            $ action = _return[0]
            $ context = _return[1]

            return [action, context]

        if action in breast_actions:
            if Girl.lust >= 50 and not Girl.top_pulled_up and (Girl.outfit["bra"] or Girl.outfit["top"]):
                call pulls_off_top_narration(Girl)

                $ Girl.top_pulled_up = 1

                call expression Girl.tag + "_First_Topless"

    call end_of_action_reactions(Girl, action)

    return [None, "stop"]

label after_action(Girl, action, context):
    $ Girl.change_face("_sexy")
    $ Girl.remaining_actions -= 1

    call action_specific_consequences(Girl, action)

    if action == "kiss" and action not in Girl.recent_history:
        if Girl.love > 300:
            $ Girl.change_stat("love", 60, 4)

        $ Girl.change_stat("love", 70, 1)

    if action in ["fondle_thighs", "fondle_ass"]:
        if not Girl.legs_covered:
            $ Girl.addiction_rate += 1

            if Player.addictive:
                $ Girl.addiction_rate += 1
    elif action not in dildo_actions:
        if action == "kiss":
            $ Girl.addiction_rate += 2 if Girl.addiction_rate < 5 else 1
        else:
            $ Girl.addiction_rate += 1

        if Player.addictive:
            $ Girl.addiction_rate += 1

    if action in ["handjob", "footjob"]:
        $ Girl.change_stat("lust", 90, 5)

    if achievement is not None and achievement in achievements:
        pass
    elif action == "titjob" and Girl.action_counter[action] > 5:
        pass
    elif action == "kiss" and Girl.action_counter[action] > 10:
        pass
    elif action not in dildo_actions and Girl.action_counter[action] >= 10:
        if action not in ["anal"]:
            $ Girl.SEXP += 5
        else:
            $ Girl.SEXP += 7

        if achievement is not None:
            $ achievements.append(achievement)

        if action not in ["anal"]:
            $ Girl.change_face("_smile", 1)
        elif action in ["anal"]:
            $ Girl.change_face("_bemused", 1)

        call achievement_lines(Girl, action)
    elif Girl.action_counter[action] == 1:
        call first_action_response(Girl, action, context)
    elif (action in cock_actions or action == "kiss") and Girl.action_counter[action] == 5:
        call action_done_five_times_lines(Girl, action)
    elif action in sex_actions and context == "stop":
        if "unsatisfied" in Girl.recent_history:
            call unsatisfied_reactions(Girl, action)

    if action == "kiss" and context == "stop" and Girl.action_counter["kiss"] > 5 and Girl.lust > 50 and approval_check(Girl, 950):
        call would_you_like_more_lines(Girl, action)

    if context == "switch":
        call switching_action_lines(Girl, action)

    $ Player.sprite = False
    $ Player.cock_position = "out"

    call checkout

    return
