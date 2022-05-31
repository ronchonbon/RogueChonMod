label action:
    $ stack_depth = renpy.call_stack_depth()

    $ round -= 5 if round > 5 else (round-1)

    call set_approval_bonus
    call action_approval_checks(focused_Girl, primary_action)

    if primary_action == "kiss" and focused_Girl == EmmaX and not approval_check(focused_Girl, 1000):
        $ focused_Girl.change_face("_sadside")

        ch_e "Not when we barely know each other. . ."

        $ focused_Girl.recent_history.append("no_kiss")
        $ focused_Girl.daily_history.append("no_kiss")

        return

    if action_context in ["auto", "offhand"]:
        call auto_action_narrations(focused_Girl, primary_action)

        if approval:
            call auto_approved_reactions(focused_Girl, primary_action)

            if action_context == "auto":
                jump before_action
            else:
                return
        else:
            call auto_rejected_reactions(focused_Girl, primary_action)

            $ approval_bonus = 0
            $ offhand_action = None

            return
    elif action_context == "pullback":
        call pullback_reactions(focused_Girl, primary_action)
        jump before_action
    elif primary_action in anal_insertion_actions and not focused_Girl.used_to_anal and ("finger_ass" in focused_Girl.daily_history or "dildo_ass" in focused_Girl.daily_history or "anal" in focused_Girl.daily_history):
        call anal_insertion_reactions(focused_Girl, primary_action)
    elif primary_action in focused_Girl.recent_history:
        call recent_action_reactions(focused_Girl, primary_action)
        jump before_action
    elif primary_action in focused_Girl.daily_history:
        call daily_action_reactions(focused_Girl, primary_action)
        jump before_action

    if primary_action == "kiss":
        if approval > 1 and not focused_Girl.action_counter["kiss"] and not focused_Girl.forced:
            $ focused_Girl.change_face("_sexy")
            $ focused_Girl.eyes = "_side"

            call excited_for_first_kiss_lines(focused_Girl, primary_action)
            jump before_action
        elif approval and not focused_Girl.action_counter["kiss"]:
            $ focused_Girl.change_face("_sexy")
            $ focused_Girl.eyes = "_side"

            call less_excited_for_first_kiss_lines(focused_Girl, primary_action)
            jump before_action
        elif approval and "kiss" in focused_Girl.recent_history:
            $ focused_Girl.change_face("_sexy", 1)

            call recent_action_lines(focused_Girl, primary_action)
            jump before_action
        elif approval and "kiss" in focused_Girl.daily_history:
            $ focused_Girl.change_face("_sexy", 1)

            call daily_action_lines(focused_Girl, primary_action)
            jump before_action
        elif approval > 1 and focused_Girl.love > focused_Girl.obedience:
            $ focused_Girl.change_face("_sexy")

            call excited_for_kiss_love_lines(focused_Girl, primary_action)
            jump before_action
        elif approval_check(focused_Girl, 500, "O") and focused_Girl.obedience > focused_Girl.love:
            $ focused_Girl.change_face("_normal")

            call excited_for_kiss_obedience_lines(focused_Girl, primary_action)

            $ focused_Girl.change_stat("obedience", 60, 1)

            jump before_action
        elif approval_check(focused_Girl, 250, "O",Alt=[[KittyX,LauraX],300]) and approval_check(focused_Girl, 250, "L",Alt=[[KittyX,LauraX],200]):
            $ focused_Girl.change_face("_bemused")

            focused_Girl.voice "Ok, fine."

            $ focused_Girl.change_stat("obedience", 50, 3)

            jump before_action
        elif focused_Girl.addiction >= 50:
            $ focused_Girl.change_face("_sexy")
            $ focused_Girl.eyes = "_manic"

            call kiss_addicted_lines(focused_Girl, primary_action)
            jump before_action
        elif approval:
            $ focused_Girl.change_face("_bemused")

            call kiss_accepted_lines(focused_Girl, primary_action)
            jump before_action
        else:
            $ focused_Girl.change_face("_normal")
            $ focused_Girl.mouth = "_sad"

            call otherwise_not_interested_lines(focused_Girl, primary_action)

            $ focused_Girl.recent_history.append("no_kiss")
            $ focused_Girl.daily_history.append("no_kiss")
    else:
        if not focused_Girl.action_counter[primary_action] and "no_" + primary_action not in focused_Girl.recent_history:
            call first_time_asking_reactions(focused_Girl, primary_action)

        if not focused_Girl.action_counter[primary_action] and approval:
            call first_action_approval(focused_Girl, primary_action)
            jump before_action
        elif approval:
            call action_approved(focused_Girl, primary_action)

            if _return:
                jump before_action

        if approval >= 2:
            call action_accepted(focused_Girl, primary_action)
            jump before_action
        else:
            call action_disapproved(focused_Girl, primary_action)

        call action_rejected(focused_Girl, primary_action)

        label begging_rejected:

    return

label before_action:
    if taboo:
        $ focused_Girl.inhibition += int(taboo/10)
        $ focused_Girl.lust += int(taboo/5)

    $ focused_Girl.change_face("_sexy")

    if primary_action == "kiss":
        $ focused_Girl.change_stat("inhibition", 10, 1)
        $ focused_Girl.change_stat("inhibition", 20, 1)

        call kiss_launch(focused_Girl)

        if focused_Girl.action_counter["kiss"] >= 10 and focused_Girl.inhibition >= 300:
            $ focused_Girl.change_face("_sucking")
        elif focused_Girl.action_counter["kiss"] > 1 and focused_Girl.addiction >= 50:
            $ focused_Girl.change_face("_sucking")
        else:
            $ focused_Girl.change_face("_kiss",2)

        if focused_Girl == RogueX and not focused_Girl.action_counter["kiss"]:
            call Rogue_first_kiss

            return
        else:
            call kissing_narrations(focused_Girl)
    elif primary_action in fondle_actions:
        if not focused_Girl.forced and action_context != "auto":
            $ approval_bonus = 0

            if primary_action in ["eat_pussy", "eat_ass"]:
                $ approval_bonus = 15

            if primary_action in inside_panties_actions:
                call Bottoms_Off
            elif primary_action in breast_actions:
                call Top_Off

            if "_angry" in focused_Girl.recent_history:
                return

        $ approval_bonus = 0
    elif primary_action in job_actions:
        if primary_action not in dildo_actions:
            if focused_Girl.forced:
                $ focused_Girl.change_face("_sad")
            elif not focused_Girl.action_counter[primary_action]:
                $ focused_Girl.brows = "_confused"
                $ focused_Girl.eyes = "_sexy"
                $ focused_Girl.mouth = "_smile"
        else:
            if not focused_Girl.forced and action_context != "auto":
                call Bottoms_Off(focused_Girl)

                if "_angry" in focused_Girl.recent_history:
                    return

            $ approval_bonus = 0

        call Seen_First_Peen(focused_Girl, Partner, React = action_context)

        if primary_action == "handjob":
            call handjob_launch(focused_Girl)
        elif primary_action == "titjob":
            call titjob_launch(focused_Girl)
        elif primary_action == "blowjob":
            call blowjob_launch(focused_Girl)
        elif primary_action in dildo_actions:
            call pussy_launch(focused_Girl)
    elif primary_action in sex_actions:
        call Seen_First_Peen(focused_Girl, Partner, React = action_context)

        $ focused_Girl.pose = "doggy"

        call sex_launch(focused_Girl, primary_action)

    if primary_action not in sex_actions:
        if action_context == focused_Girl:
            $ action_context = None

            call girl_initiated_action(focused_Girl, primary_action)

            if _return:
                return
    elif primary_action in sex_actions:
        if action_context == focused_Girl:
            $ action_context = None

            call girl_initiated_action(focused_Girl, primary_action)

            if _return:
                return

            call expose_bottom(focused_Girl)
        elif action_context != "auto":
            if primary_action in ["sex", "anal"]:
                call AutoStrip(focused_Girl)
            elif primary_action == "hotdog":
                call Bottoms_Off(focused_Girl)

            call start_of_sex_narration(focused_Girl, primary_action)
        else:
            if primary_action in ["sex", "anal"]:
                if primary_action == "sex":
                    $ word = renpy.random.choice(["slit"])
                elif primary_action == "anal":
                    $ word = renpy.random.choice(["ass", "back door"])

                if (focused_Girl.wearing_pants and not focused_Girl.bottom_pulled_down) and (focused_Girl.outfit["underwear"] and not focused_Girl.underwear_pulled_down):
                    "You quickly pull down her pants and her [focused_Girl.outfit['underwear']] and press against her [word]."

                    $ focused_Girl.bottom_pulled_down = True
                    $ focused_Girl.underwear_pulled_down = True
                elif (focused_Girl.outfit["underwear"] and not focused_Girl.underwear_pulled_down):
                    "You quickly pull down her [focused_Girl.outfit['underwear']] and press against her [word]."

                    $ focused_Girl.underwear_pulled_down = True

                if focused_Girl.wearing_skirt:
                    $ focused_Girl.upskirt = True

                $ focused_Girl.seen_underwear = True

                call expression focused_Girl.tag + "_First_Bottomless" pass(1)
            elif primary_action == "hotdog":
                $ line = renpy.random.choice(["You press yourself against her ass.",
                    "You press yourself against her mound.",
                    "You roll back, pulling her on top of you and your rigid member.",
                    "She lays back, pulling you against her with your rigid member.",
                    "She turns around, pulling you against her with your rigid member."])
                "[line]"

        if Player.focus >= 50:
            call hard_cock_lines(focused_Girl, primary_action)

    call first_action_changes(focused_Girl, primary_action)

    if taboo:
        if primary_action == "fondle_thighs":
            $ focused_Girl.change_stat("lust", 200, (int(taboo/5)))
            $ focused_Girl.change_stat("inhibition", 200, (2*(int(taboo/5))))
        elif primary_action in ["fondle_breasts", "suck_breasts", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "dildo_pussy", "dildo_ass"]:
            $ focused_Girl.inhibition += int(taboo/10)
            $ focused_Girl.lust += int(taboo/5)
        elif primary_action in ["fondle_pussy", "eat_pussy", "finger_ass", "eat_ass"]:
            if focused_Girl == JeanX and focused_Girl.taboo:
                $ focused_Girl.change_stat("inhibition", 200, (int(taboo/10)))
            elif taboo:
                $ focused_Girl.inhibition += int(taboo/10)

            $ focused_Girl.lust += int(taboo/5)

    if action_context:
        $ action_context = None

    if primary_action in inside_panties_actions:
        if focused_Girl.wearing_skirt:
            $ focused_Girl.upskirt = 1
            $ focused_Girl.seen_underwear = 1

        call expression focused_Girl.tag + "_First_Bottomless" pass(1)

    $ line = 0
    $ counter = 0

    if primary_action == "fondle_pussy":
        $ action_speed = 1
    elif primary_action == "finger_pussy":
        $ action_speed = 2
    elif primary_action == "sex":
        $ Player.cock_position = "in"

        $ action_speed = 1
    elif primary_action == "anal":
        $ Player.cock_position = "anal"

        $ action_speed = 1
    elif primary_action == "hotdog":
        $ action_speed = 1

    if taboo:
        $ focused_Girl.drain_word("no_taboo")

    $ focused_Girl.drain_word("no_" + primary_action)
    $ focused_Girl.add_word(0, primary_action, primary_action)

    $ action_speed = 0

    if primary_action in fondle_actions:
        call shift_view(focused_Girl, focused_Girl.pose)
    elif primary_action in breast_actions:
        call breasts_launch(focused_Girl)
    elif primary_action == "footjob":
        call sex_launch(focused_Girl, primary_action)

label action_cycle:
    if primary_action in mouth_actions:
        if primary_action != "kiss" and offhand_action == "kiss":
            $ offhand_action = None

    $ action_speed = 0

    while round > 0:
        if primary_action == "kiss":
            call kiss_launch(focused_Girl)

            $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0
        if primary_action in fondle_actions:
            call shift_view(focused_Girl, focused_Girl.pose)
        elif primary_action in ["footjob", "sex", "anal", "hotdog"]:
            call sex_launch(focused_Girl, primary_action)

            if primary_action == "sex":
                $ Player.cock_position = "in"
            elif primary_action == "anal":
                $ Player.cock_position = "anal"
            elif primary_action == "hotdog":
                $ Player.cock_position = "out"
        elif primary_action in dildo_actions:
            call shift_view(focused_Girl, focused_Girl.pose)

        $ focused_Girl.lust_face()

        if Player.focus < 100:
            if primary_action == "kiss":
                jump kiss_menu
            elif primary_action in fondle_actions:
                jump fondle_menu
            elif primary_action in job_actions:
                jump handjob_menu
            elif primary_action in sex_actions:
                jump sex_menu

        label action_menu_return:

        if primary_action in inside_panties_actions:
            if focused_Girl.outfit["underwear"] or focused_Girl.legs_covered: #This checks if Rogue_sprite wants to strip down.
                call Girl_Undress(focused_Girl, "auto")

        call Sex_Dialog(focused_Girl, Partner)

        $ counter += 1
        $ round -= 1

        if (primary_action in ["blowjob"] and action_speed) or primary_action in ["sex", "anal"]:
            $ Player.cock_wet = 1
            $ Player.spunk = 0 if (Player.spunk and not focused_Girl.spunk["pussy"]) else Player.spunk #cleans you off after one cycle

        call end_of_action_round

        if _return:
            return

        if primary_action in breast_actions:
            if focused_Girl.lust >= 50 and not focused_Girl.top_pulled_up and (focused_Girl.outfit["bra"] or focused_Girl.outfit["top"]):
                call pull_off_top_narration(focused_Girl)

                $ focused_Girl.top_pulled_up = 1

                call expression focused_Girl.tag + "_First_Topless"

    call end_of_action_reactions(focused_Girl, action)

label after_action:
    if primary_action in sex_actions:
        $ Player.sprite = False
        $ Player.cock_position = "out"

    call reset_position(focused_Girl)

    $ focused_Girl.change_face("_sexy")
    $ focused_Girl.remaining_actions -= 1

    call action_specific_consequences(focused_Girl, primary_action)

    if primary_action == "kiss" and primary_action not in focused_Girl.recent_history:
        if focused_Girl.love > 300:
            $ focused_Girl.change_stat("love", 60, 4)
        $ focused_Girl.change_stat("love", 70, 1)

    if primary_action in ["fondle_thighs", "fondle_ass"]:
        if focused_Girl.legs_covered:
            $ focused_Girl.addiction_rate += 1

            if Player.addictive:
                $ focused_Girl.addiction_rate += 1
    elif primary_action not in dildo_actions:
        if primary_action == "kiss":
            $ focused_Girl.addiction_rate += 2 if focused_Girl.addiction_rate < 5 else 1
        else:
            $ focused_Girl.addiction_rate += 1

        if Player.addictive:
            $ focused_Girl.addiction_rate += 1

    if primary_action in ["handjob", "footjob"]:
        $ focused_Girl.change_stat("lust", 90, 5)

    if achievement is not None and achievement in achievements:
        pass
    elif primary_action == "titjob" and focused_Girl.action_counter[primary_action] > 5:
        pass
    elif primary_action == "kiss" and focused_Girl.action_counter[primary_action] > 10:
        pass
    elif primary_action not in dildo_actions and focused_Girl.action_counter[primary_action] >= 10:
        if primary_action not in ["anal"]:
            $ focused_Girl.SEXP += 5
        else:
            $ focused_Girl.SEXP += 7

        if achievement is not None:
            $ achievements.append(achievement)

        if primary_action not in ["anal"] and not action_context:
            $ focused_Girl.change_face("_smile", 1)
        elif primary_action in ["anal"] and not action_context:
            $ focused_Girl.change_face("_bemused", 1)

        call achievement_lines(focused_Girl, primary_action)
    elif primary_action == "blowjob" and action_context == "shift":
        pass
    elif focused_Girl.action_counter[primary_action] == 1:
        call first_action_response(focused_Girl, primary_action)
    elif (primary_action in cock_actions or primary_action == "kiss") and focused_Girl.action_counter[primary_action] == 5:
        call action_done_five_times_lines(focused_Girl, primary_action)
    elif primary_action in sex_actions and not action_context:
        if "unsatisfied" in focused_Girl.recent_history:
            call unsatisfied_reactions(focused_Girl, primary_action)

    if primary_action == "kiss" and not action_context and focused_Girl.action_counter["kiss"] > 5 and focused_Girl.lust > 50 and approval_check(focused_Girl, 950):
        call would_you_like_more_lines(focused_Girl, primary_action)

    $ approval_bonus = 0

    if action_context == "shift":
        call switching_action_lines(focused_Girl, primary_action)

        $ primary_action = None
        $ action_speed = 0
    else:
        call reset_position(focused_Girl)

    call checkout

    return

label set_approval_bonus:
    if primary_action == "fondle_thighs":
        if focused_Girl.action_counter["fondle_thighs"]:
            $ approval_bonus += 10

        if focused_Girl.legs_covered:
            $ approval_bonus -= 5

        if focused_Girl.lust > 75:
            $ approval_bonus += 10

        if "exhibitionist" in focused_Girl.traits:
            $ approval_bonus += taboo

        if focused_Girl in Player.Harem or "sex friend" in focused_Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in focused_Girl.traits:
            $ approval_bonus -= 25
    elif primary_action == "fondle_breasts":
        if focused_Girl.action_counter["fondle_breasts"]:
            $ approval_bonus += 15

        if focused_Girl.lust > 75: #She's really horny
            $ approval_bonus += 20

        if "exhibitionist" in focused_Girl.traits:
            $ approval_bonus += (3*taboo)

        if focused_Girl in Player.Harem or "sex friend" in focused_Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in focused_Girl.traits:
            $ approval_bonus -= 20
    elif primary_action == "suck_breasts":
        if focused_Girl.action_counter["suck_breasts"]: #You've done it before
            $ approval_bonus += 15

        if not focused_Girl.outfit["bra"] and not focused_Girl.outfit["top"]:
            $ approval_bonus += 15

        if focused_Girl.lust > 75: #She's really horny
            $ approval_bonus += 20

        if focused_Girl.lust > 75 and action_context == "auto": #She's really horny
            $ approval_bonus += 10

        if "exhibitionist" in focused_Girl.traits:
            $ approval_bonus += (4*taboo)

        if focused_Girl in Player.Harem or "sex friend" in focused_Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in focused_Girl.traits:
            $ approval_bonus -= 25
    elif primary_action == "fondle_pussy":
        if focused_Girl.action_counter["fondle_pussy"]: #You've done it before
            $ approval_bonus += 20

        if focused_Girl.legs_covered: # she's got pants on.
            $ approval_bonus -= 10

        if focused_Girl.lust > 75: #She's really horny
            $ approval_bonus += 15

        if focused_Girl.lust > 75 and action_context == "auto": #She's really horny
            $ approval_bonus += 10

        if "exhibitionist" in focused_Girl.traits:
            $ approval_bonus += (2*taboo)

        if focused_Girl in Player.Harem or "sex friend" in focused_Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in focused_Girl.traits:
            $ approval_bonus -= 25
    elif primary_action == "eat_pussy":
        if focused_Girl.action_counter["eat_pussy"]: #You've done it before
            $ approval_bonus += 15

        if focused_Girl.legs_covered: # she's got pants on.
            $ approval_bonus -= 15

        if focused_Girl.lust > 95:
            $ approval_bonus += 20
        elif focused_Girl.lust > 85: #She's really horny
            $ approval_bonus += 15

        if focused_Girl.lust > 85 and action_context == "auto": #She's really horny
            $ approval_bonus += 10

        if action_context == "shift":
            $ approval_bonus += 10

        if "exhibitionist" in focused_Girl.traits:
            $ approval_bonus += (4*taboo)

        if focused_Girl in Player.Harem or "sex friend" in focused_Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in focused_Girl.traits:
            $ approval_bonus -= 25
    elif primary_action == "fondle_ass":
        if focused_Girl.action_counter["fondle_ass"]: #You've done it before
            $ approval_bonus += 10

        if focused_Girl.legs_covered: # she's got pants on.
            $ approval_bonus -= 5

        if focused_Girl.lust > 75: #She's really horny
            $ approval_bonus += 15

        if "exhibitionist" in focused_Girl.traits:
            $ approval_bonus += taboo

        if focused_Girl in Player.Harem or "sex friend" in focused_Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in focused_Girl.traits:
            $ approval_bonus -= 25
    elif primary_action == "finger_ass":
        if focused_Girl.action_counter["finger_ass"]: #You've done it before
            $ approval_bonus += 25

        if focused_Girl.legs_covered: # she's got pants on.
            $ approval_bonus -= 15

        if focused_Girl.lust > 85 and focused_Girl.used_to_anal: #She's really horny
            $ approval_bonus += 15

        if focused_Girl.lust > 95 and focused_Girl.used_to_anal:
            $ approval_bonus += 5

        if focused_Girl.lust > 85 and action_context == "auto": #She's really horny
            $ approval_bonus += 10

        if action_context == "shift":
            $ approval_bonus += 10

        if "exhibitionist" in focused_Girl.traits:
            $ approval_bonus += (4*taboo)

        if focused_Girl in Player.Harem or "sex friend" in focused_Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in focused_Girl.traits:
            $ approval_bonus -= 25
    elif primary_action == "eat_ass":
        if focused_Girl.action_counter["eat_ass"]: #You've done it before
            $ approval_bonus += 20

        if focused_Girl.legs_covered: # she's got pants on.
            $ approval_bonus -= 25

        if focused_Girl.lust > 95:
            $ approval_bonus += 20
        elif focused_Girl.lust > 85: #She's really horny
            $ approval_bonus += 15

        if focused_Girl.lust > 85 and action_context == "auto": #auto
            $ approval_bonus += 10

        if action_context == "shift":
            $ approval_bonus += 10

        if "exhibitionist" in focused_Girl.traits:
            $ approval_bonus += (4*taboo)

        if focused_Girl in Player.Harem or "sex friend" in focused_Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in focused_Girl.traits:
            $ approval_bonus -= 25
    elif primary_action == "handjob":
        if focused_Girl.action_counter[primary_action] >= 7: # She loves it
            $ approval_bonus += 10
        elif focused_Girl.action_counter[primary_action] >= 3: #You've done it before several times
            $ approval_bonus += 7
        elif focused_Girl.action_counter[primary_action]: #You've done it before
            $ approval_bonus += 3

        if "exhibitionist" in focused_Girl.traits:
            $ approval_bonus += (3*taboo)

        if focused_Girl in Player.Harem or "sex friend" in focused_Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in focused_Girl.traits:
            $ approval_bonus -= 40

        if focused_Girl.addiction >= 75 and focused_Girl.event_counter["swallowed"] >= 3: #She's really strung out and has swallowed
            $ approval_bonus += 15
        if focused_Girl.addiction >= 75:
            $ approval_bonus += 5

        if action_context == "shift":
            $ approval_bonus += 15
    elif primary_action == "footjob":
        if focused_Girl.action_counter[primary_action] >= 7: # She loves it
            $ approval_bonus += 10
        elif focused_Girl.action_counter[primary_action] >= 3: #You've done it before several times
            $ approval_bonus += 7
        elif focused_Girl.action_counter[primary_action]: #You've done it before
            $ approval_bonus += 3

        if focused_Girl.addiction >= 75 and focused_Girl.event_counter["swallowed"] >=3: #She's really strung out and has swallowed
            $ approval_bonus += 10
        if focused_Girl.addiction >= 75:
            $ approval_bonus += 5

        if action_context == "shift":
            $ approval_bonus += 15
        if "exhibitionist" in focused_Girl.traits:
            $ approval_bonus += (3*taboo)
        if focused_Girl in Player.Harem or "sex friend" in focused_Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in focused_Girl.traits:
            $ approval_bonus -= 40
    elif primary_action == "titjob":
        if focused_Girl.action_counter[primary_action] >= 7: # She loves it
            $ approval_bonus += 10
        elif focused_Girl.action_counter[primary_action] >= 3: #You've done it before several times
            $ approval_bonus += 7
        elif focused_Girl.action_counter[primary_action]: #You've done it before
            $ approval_bonus += 5

        if focused_Girl.seen_breasts and approval_check(focused_Girl, 500): # You've seen her tits.
            $ approval_bonus += 10
        if not focused_Girl.outfit["bra"] and not focused_Girl.outfit["top"]: #She's already topless
            $ approval_bonus += 10

        if "exhibitionist" in focused_Girl.traits:
            $ approval_bonus += (5*taboo)

        if focused_Girl in Player.Harem or "sex friend" in focused_Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in focused_Girl.traits:
            $ approval_bonus -= 30

        if focused_Girl.lust > 75: #She's really horny
            $ approval_bonus += 10

        if focused_Girl.addiction >= 75 and focused_Girl.event_counter["swallowed"] >= 3: #She's really strung out and has swallowed
            $ approval_bonus += 15
        if focused_Girl.addiction >= 75:
            $ approval_bonus += 5

        if action_context == "shift":
            $ approval_bonus += 15
    elif primary_action == "blowjob":
        if focused_Girl.action_counter[primary_action] >= 7: # She loves it
            $ approval_bonus += 15
        elif focused_Girl.action_counter[primary_action] >= 3: #You've done it before several times
            $ approval_bonus += 10
        elif focused_Girl.action_counter[primary_action]: #You've done it before
            $ approval_bonus += 7

        if focused_Girl.addiction >= 75 and focused_Girl.event_counter["swallowed"] >=3: #She's really strung out and has swallowed
            $ approval_bonus += 25
        elif focused_Girl.addiction >= 75: #She's really strung out
            $ approval_bonus += 15

        if "exhibitionist" in focused_Girl.traits:
            $ approval_bonus += (4*taboo)

        if focused_Girl in Player.Harem or "sex friend" in focused_Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in focused_Girl.traits:
            $ approval_bonus -= 40

        if action_context == "shift":
            $ approval_bonus += 15
    elif primary_action == "dildo_pussy":
        if focused_Girl.action_counter[primary_action]: #You've done it before
            $ approval_bonus += 15
        if focused_Girl.legs_covered: # she's got pants on.
            $ approval_bonus -= 20

        if focused_Girl.lust > 95:
            $ approval_bonus += 20
        elif focused_Girl.lust > 85: #She's really horny
            $ approval_bonus += 15

        if action_context == "shift":
            $ approval_bonus += 10
        if "exhibitionist" in focused_Girl.traits:
            $ approval_bonus += (5*taboo)

        if focused_Girl in Player.Harem or "sex friend" in focused_Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in focused_Girl.traits:
            $ approval_bonus -= 40
    elif primary_action == "dildo_ass":
        if focused_Girl.used_to_anal:
            $ approval_bonus += 30
        elif "anal" in focused_Girl.recent_history or "dildo_ass" in focused_Girl.recent_history:
            $ approval_bonus -= 20
        elif "anal" in focused_Girl.daily_history or "dildo_ass" in focused_Girl.daily_history:
            $ approval_bonus -= 10
        elif (focused_Girl.action_counter["anal"] + focused_Girl.action_counter["dildo_ass"]) > 0 or focused_Girl.outfit["buttplug"]: #You've done it before
            $ approval_bonus += 20

        if focused_Girl.legs_covered: # she's got pants on.
            $ approval_bonus -= 20

        if focused_Girl.lust > 95:
            $ approval_bonus += 20
        elif focused_Girl.lust > 85: #She's really horny
            $ approval_bonus += 15

        if action_context == "shift":
            $ approval_bonus += 10
        if "exhibitionist" in focused_Girl.traits:
            $ approval_bonus += (5*taboo)

        if focused_Girl in Player.Harem or "sex friend" in focused_Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in focused_Girl.traits:
            $ approval_bonus -= 40
    elif primary_action == "sex":
        if focused_Girl.action_counter["sex"] >= 7: # She loves it
            $ approval_bonus += 15
        elif focused_Girl.action_counter["sex"] >= 3: #You've done it before several times
            $ approval_bonus += 12
        elif focused_Girl.action_counter["sex"]: #You've done it before
            $ approval_bonus += 10

        if focused_Girl.addiction >= 75 and (focused_Girl.event_counter["creampied"] + focused_Girl.event_counter["anal_creampied"]) >=3: #She's really strung out and has creampied
            $ approval_bonus += 20
        elif focused_Girl.addiction >= 75:
            $ approval_bonus += 15

        if focused_Girl.lust > 85:
            $ approval_bonus += 10
        elif focused_Girl.lust > 75: #She's really horny
            $ approval_bonus += 5

        if action_context == "shift":
            $ approval_bonus += 10
        if "exhibitionist" in focused_Girl.traits:
            $ approval_bonus += (4*taboo)

        if focused_Girl in Player.Harem or "sex friend" in focused_Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in focused_Girl.traits:
            $ approval_bonus -= 40
    elif primary_action == "anal":
        if focused_Girl.action_counter["anal"]  >= 7: # She loves it
            $ approval_bonus += 20
        elif focused_Girl.action_counter["anal"]  >= 3: #You've done it before several times
            $ approval_bonus += 17
        elif focused_Girl.action_counter["anal"] : #You've done it before
            $ approval_bonus += 15

        if focused_Girl.addiction >= 75 and (focused_Girl.event_counter["creampied"] + focused_Girl.event_counter["anal_creampied"]) >=3: #She's really strung out and has creampied
            $ approval_bonus += 25
        elif focused_Girl.addiction >= 75:
            $ approval_bonus += 15

        if focused_Girl.lust > 85:
            $ approval_bonus += 10
        elif focused_Girl.lust > 75: #She's really horny
            $ approval_bonus += 5

        if focused_Girl.used_to_anal:
            $ approval_bonus += 10
        elif "anal" in focused_Girl.recent_history:
            $ approval_bonus -= 20
        elif "anal" in focused_Girl.daily_history:
            $ approval_bonus -= 10

        if action_context == "shift":
            $ approval_bonus += 10
        if "exhibitionist" in focused_Girl.traits:
            $ approval_bonus += (5*taboo)

        if focused_Girl in Player.Harem or "sex friend" in focused_Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in focused_Girl.traits:
            $ approval_bonus -= 40
    elif primary_action == "hotdog":
        if focused_Girl.action_counter["hotdog"] >= 3: #You've done it before several times
            $ approval_bonus += 10
        elif focused_Girl.action_counter["hotdog"]: #You've done it before
            $ approval_bonus += 5

        if focused_Girl.lust > 85:
            $ approval_bonus += 10
        elif focused_Girl.lust > 75: #She's really horny
            $ approval_bonus += 5
        if action_context == "shift":
            $ approval_bonus += 10
        if "exhibitionist" in focused_Girl.traits:
            $ approval_bonus += (3*taboo)

        if focused_Girl in Player.Harem or "sex friend" in focused_Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in focused_Girl.traits:
            $ approval_bonus -= 40

    if focused_Girl.event_counter["forced"] and not focused_Girl.forced:
        $ approval_bonus -= 5*focused_Girl.event_counter["forced"]

    if taboo and "no_taboo" in focused_Girl.daily_history:
        $ approval_bonus -= 10

    if "no_" + primary_action in focused_Girl.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_" + primary_action in focused_Girl.recent_history else 0

    return

label end_of_action_round:
    $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus

    if Player.focus >= 100 or focused_Girl.lust >= 100:
        if Player.focus >= 100:
            call Player_Cumming(focused_Girl)

            if "_angry" in focused_Girl.recent_history:
                call reset_position(focused_Girl)

                return True

            $ focused_Girl.change_stat("lust", 200, 5)

            if 100 > focused_Girl.lust >= 70 and focused_Girl.event_counter["orgasmed"] < 2 and focused_Girl.SEXP >= 20:
                $ focused_Girl.add_word(0, "unsatisfied", "unsatisfied")

            if Player.focus > 80:
                jump after_action

            $ line = "came"

        if focused_Girl.lust >= 100:
            call Girl_Cumming(focused_Girl)

            if action_context == "shift" or "_angry" in focused_Girl.recent_history:
                jump after_action

        if line == "came": #ex Player.focus <= 20:
            $ line = 0

            if not Player.semen:
                if primary_action in sex_actions:
                    $ line = renpy.random.choice(["She's emptied you out, you'll need to take a break."
                        "You're pretty wiped, better stop for now."])

                    "[line]"

                    jump after_action
                else:
                    "You're emptied out, you should probably take a break."

            if "unsatisfied" in focused_Girl.recent_history:#And Rogue_sprite is unsatisfied,
                call girl_unsatisfied_menu(focused_Girl, primary_action)

    if Partner and Partner.lust >= 100:
        call Girl_Cumming(Partner)

    if primary_action in ["kiss", "fondle_thighs", "fondle_breasts", "eat_pussy", "suck_breasts", "fondle_ass", "insert_ass", "handjob", "footjob", "titjob"]:
        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0
    elif primary_action in ["blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

    if focused_Girl.SEXP >= 100 or approval_check(focused_Girl, 1200, "LO"):
        pass
    elif counter == (5 + focused_Girl.action_counter[primary_action]):
        call starting_to_get_bored_reactions(focused_Girl, primary_action)
    elif primary_action in ["fondle_pussy", "finger_ass", "dildo_pussy", "dildo_ass"] and focused_Girl.lust >= 80:
        pass
    elif primary_action in ["fondle_breasts", "suck_breasts"] and focused_Girl.lust >= 85:
        pass
    elif primary_action in fondle_actions and counter == (15 + focused_Girl.action_counter[primary_action]) and focused_Girl.SEXP >= 15 and not approval_check(focused_Girl, 1500):
        call definitely_bored_now_reactions(focused_Girl, primary_action)
    elif primary_action in ["handjob, footjob, titjob, blowjob", "sex", "anal", "hotdog"] and counter == (10 + focused_Girl.action_counter[primary_action]) and focused_Girl.SEXP <= 100 and not approval_check(focused_Girl, 1200, "LO"):
        call definitely_bored_now_reactions(focused_Girl, primary_action)
    elif primary_action in ["kiss", "dildo_pussy", "dildo_ass"] and counter == (15 + focused_Girl.action_counter[primary_action]) and focused_Girl.SEXP >= 15 and not approval_check(focused_Girl, 1200, "LO"):
        call definitely_bored_now_reactions(focused_Girl, primary_action)
    elif primary_action in ["footjob"] and counter == 20:
        call definitely_bored_now_reactions(focused_Girl, primary_action)

    call Escalation(focused_Girl)

    if round == 10:
        call ten_rounds_left_lines(focused_Girl, primary_action)
    elif round == 5:
        call five_rounds_left_lines(focused_Girl, primary_action)

    return False
