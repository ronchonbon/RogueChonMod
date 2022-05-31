label action(Girl, action, context = None):
    $ context = action_context

    while True:
        $ round -= 5 if round > 5 else (round-1)

        call set_approval_bonus(Girl, action, context)
        call action_approval_checks(Girl, action)

        if Girl == EmmaX and action == "kiss" and not approval_check(Girl, 1000):
            $ Girl.change_face("_sadside")

            ch_e "Not when we barely know each other. . ."

            $ Girl.recent_history.append("no_kiss")
            $ Girl.daily_history.append("no_kiss")

            return False

        $ accepted = False

        if context in ["auto", "offhand"]:
            call auto_action_narrations(Girl, action)

            if approval:
                call auto_approved_reactions(Girl, action)

                if context == "auto":
                    $ accepted = True
                elif context == "offhand":
                    $ offhand_action = action

                    return False
            else:
                call auto_rejected_reactions(Girl, action)

                if _return:
                    $ accepted = True
                else:
                    $ approval_bonus = 0
                    $ offhand_action = None

                    return False
        elif context == "pullback":
            call pullback_reactions(Girl, action)

            $ accepted = True
        elif action in anal_insertion_actions and not Girl.used_to_anal and ("finger_ass" in Girl.daily_history or "dildo_ass" in Girl.daily_history or "anal" in Girl.daily_history):
            call anal_insertion_reactions(Girl, action)
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

                    $ accepted = True
                elif approval and not Girl.action_counter["kiss"]:
                    $ Girl.change_face("_sexy")
                    $ Girl.eyes = "_side"

                    call less_excited_for_first_kiss_lines(Girl, action)

                    $ accepted = True
                elif approval > 1 and Girl.love > Girl.obedience:
                    $ Girl.change_face("_sexy")

                    call excited_for_kiss_love_lines(Girl, action)

                    $ accepted = True
                elif approval_check(Girl, 500, "O") and Girl.obedience > Girl.love:
                    $ Girl.change_face("_normal")

                    call excited_for_kiss_obedience_lines(Girl, action)

                    $ accepted = True

                    $ Girl.change_stat("obedience", 60, 1)
                elif approval_check(Girl, 250, "O",Alt=[[KittyX,LauraX],300]) and approval_check(Girl, 250, "L",Alt=[[KittyX,LauraX],200]):
                    $ Girl.change_face("_bemused")

                    Girl.voice "Ok, fine."

                    $ Girl.change_stat("obedience", 50, 3)

                    $ accepted = True
                elif Girl.addiction >= 50:
                    $ Girl.change_face("_sexy")
                    $ Girl.eyes = "_manic"

                    call kiss_addicted_lines(Girl, action)

                    $ accepted = True
                elif approval:
                    $ Girl.change_face("_bemused")

                    call kiss_accepted_lines(Girl, action)

                    $ accepted = True
                else:
                    $ Girl.change_face("_normal")
                    $ Girl.mouth = "_sad"

                    call otherwise_not_interested_lines(Girl, action)

                    $ Girl.recent_history.append("no_kiss")
                    $ Girl.daily_history.append("no_kiss")

                    return
            else:
                if not Girl.action_counter[action] and "no_" + action not in Girl.recent_history:
                    call first_time_asking_reactions(Girl, action)

                if not Girl.action_counter[action] and approval:
                    call first_action_approval(Girl, action)
                elif approval:
                    call action_approved(Girl, action)

                    if _return:
                        $ accepted = True

                if approval >= 2:
                    call action_accepted(Girl, action)

                    $ accepted = True
                else:
                    call action_disapproved(Girl, action)

                    if _return:
                        $ action = _return

                        $ accepted = True
                    else:
                        return False

        if not accepted:
            call action_rejected(Girl, action)

            return False

        $ primary_action = action

        call before_action(Girl, action, context)

        if not _return:
            call action_cycle(Girl, action, context)

            if _return[1] == "switch":
                call after_action(Girl, action, "shift")

                return False
            elif _return[1] == "stop":
                call after_action(Girl, action, context)

                return True
            elif _return[1]:
                $ temp_action = action
                $ temp_context = context

                $ action = _return[0]
                $ context = _return[1]

                call after_action(Girl, temp_action, temp_context)
        else:
            return True

label before_action(Girl, action, context):
    if taboo:
        $ Girl.inhibition += int(taboo/10)
        $ Girl.lust += int(taboo/5)

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

            return True
        else:
            call kissing_narrations(Girl)
    elif action in fondle_actions:
        if not Girl.forced and context != "auto":
            $ approval_bonus = 0

            if action in ["eat_pussy", "eat_ass"]:
                $ approval_bonus = 15

            if action in inside_panties_actions:
                call Bottoms_Off
            elif action in breast_actions:
                call Top_Off

            if "_angry" in Girl.recent_history:
                return True

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
                    return True

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

            if _return:
                return True
    elif action in sex_actions:
        if context == Girl:
            $ context = None

            call girl_initiated_action(Girl, action)

            if _return:
                return True

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
        if Girl.wearing_skirt:
            $ Girl.upskirt = True
            $ Girl.seen_underwear = True
        elif Girl.wearing_pants or Girl.wearing_shorts:
            $ Girl.bottom_pulled_down = True
            $ Girl.seen_underwear = True
        elif Girl.wearing_dress:
            $ Girl.dress_upskirt = True
            $ Girl.seen_underwear = True

        call expression Girl.tag + "_First_Bottomless" pass(1)

    if taboo:
        $ Girl.drain_word("no_taboo")

    $ Girl.drain_word("no_" + action)
    $ Girl.add_word(0, action, action)

    if action in mouth_actions:
        if action != "kiss" and offhand_action == "kiss":
            $ offhand_action = None

    $ action_speed = 0

    $ Player.sprite = True

    if action == "massage":
        $ Girl.pose = "doggy"

        $ Player.sprite = False
    elif action == "eat_pussy":
        $ Girl.pose = "sex"

        $ Player.sprite = False
    elif action == "eat_ass":
        $ Girl.pose = "doggy"

        $ Player.sprite = False
    elif action in ["handjob", "titjob", "blowjob"]:
        $ Girl.pose = action
    elif action == "footjob" and Girl == EmmaX:
        $ Girl.pose = "footjob"
    elif action == "footjob":
        $ Girl.pose = "doggy"
    elif action == "hotdog":
        $ Girl.pose = "doggy"
    elif action == "sex":
        $ Girl.pose = "sex"
    elif action == "anal":
        $ Girl.pose = "doggy"
    else:
        $ Girl.pose = "full"

    return False

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
                call kiss_menu(Girl, action)
            elif action in fondle_actions:
                call fondle_menu(Girl, action)
            elif action in job_actions:
                call handjob_menu(Girl, action)
            elif action in sex_actions:
                call sex_menu(Girl, action)

            if _return[1]:
                return _return

        if action in inside_panties_actions:
            if Girl.outfit["underwear"] or Girl.legs_covered: #This checks if Rogue_sprite wants to strip down.
                call Girl_Undress(Girl, "auto")

        call Sex_Dialog(Girl, Partner)

        $ counter += 1
        $ round -= 1

        if (action in ["blowjob"] and action_speed) or action in ["sex", "anal"]:
            $ Player.cock_wet = 1
            $ Player.spunk = 0 if (Player.spunk and not Girl.spunk["pussy"]) else Player.spunk #cleans you off after one cycle

        call end_of_action_round(Girl, action)

        if _return:
            return _return

        if action in breast_actions:
            if Girl.lust >= 50 and not Girl.top_pulled_up and (Girl.outfit["bra"] or Girl.outfit["top"]):
                call pull_off_top_narration(Girl)

                $ Girl.top_pulled_up = 1

                call expression Girl.tag + "_First_Topless"

    call end_of_action_reactions(Girl, action)

    return [None, "stop"]

label after_action(Girl, action, context):
    $ Player.sprite = False
    $ Player.cock_position = "out"

    call reset_position(Girl)

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

        if action not in ["anal"] and not context:
            $ Girl.change_face("_smile", 1)
        elif action in ["anal"] and not context:
            $ Girl.change_face("_bemused", 1)

        call achievement_lines(Girl, action)
    elif action == "blowjob" and context == "shift":
        pass
    elif Girl.action_counter[action] == 1:
        call first_action_response(Girl, action, context)
    elif (action in cock_actions or action == "kiss") and Girl.action_counter[action] == 5:
        call action_done_five_times_lines(Girl, action)
    elif action in sex_actions and not context:
        if "unsatisfied" in Girl.recent_history:
            call unsatisfied_reactions(Girl, action)

    if action == "kiss" and not context and Girl.action_counter["kiss"] > 5 and Girl.lust > 50 and approval_check(Girl, 950):
        call would_you_like_more_lines(Girl, action)

    $ approval_bonus = 0

    if context == "shift":
        call switching_action_lines(Girl, action)

        $ primary_action = None
        $ action_speed = 0
    else:
        call reset_position(Girl)

    call checkout

    return

label set_approval_bonus(Girl, action, context):
    if action == "fondle_thighs":
        if Girl.action_counter["fondle_thighs"]:
            $ approval_bonus += 10

        if Girl.legs_covered:
            $ approval_bonus -= 5

        if Girl.lust > 75:
            $ approval_bonus += 10

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += taboo

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 25
    elif action == "fondle_breasts":
        if Girl.action_counter["fondle_breasts"]:
            $ approval_bonus += 15

        if Girl.lust > 75: #She's really horny
            $ approval_bonus += 20

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (3*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 20
    elif action == "suck_breasts":
        if Girl.action_counter["suck_breasts"]: #You've done it before
            $ approval_bonus += 15

        if not Girl.outfit["bra"] and not Girl.outfit["top"]:
            $ approval_bonus += 15

        if Girl.lust > 75: #She's really horny
            $ approval_bonus += 20

        if Girl.lust > 75 and context == "auto": #She's really horny
            $ approval_bonus += 10

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (4*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 25
    elif action == "fondle_pussy":
        if Girl.action_counter["fondle_pussy"]: #You've done it before
            $ approval_bonus += 20

        if Girl.legs_covered: # she's got pants on.
            $ approval_bonus -= 10

        if Girl.lust > 75: #She's really horny
            $ approval_bonus += 15

        if Girl.lust > 75 and context == "auto": #She's really horny
            $ approval_bonus += 10

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (2*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 25
    elif action == "eat_pussy":
        if Girl.action_counter["eat_pussy"]: #You've done it before
            $ approval_bonus += 15

        if Girl.legs_covered: # she's got pants on.
            $ approval_bonus -= 15

        if Girl.lust > 95:
            $ approval_bonus += 20
        elif Girl.lust > 85: #She's really horny
            $ approval_bonus += 15

        if Girl.lust > 85 and context == "auto": #She's really horny
            $ approval_bonus += 10

        if context == "shift":
            $ approval_bonus += 10

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (4*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 25
    elif action == "fondle_ass":
        if Girl.action_counter["fondle_ass"]: #You've done it before
            $ approval_bonus += 10

        if Girl.legs_covered: # she's got pants on.
            $ approval_bonus -= 5

        if Girl.lust > 75: #She's really horny
            $ approval_bonus += 15

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += taboo

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 25
    elif action == "finger_ass":
        if Girl.action_counter["finger_ass"]: #You've done it before
            $ approval_bonus += 25

        if Girl.legs_covered: # she's got pants on.
            $ approval_bonus -= 15

        if Girl.lust > 85 and Girl.used_to_anal: #She's really horny
            $ approval_bonus += 15

        if Girl.lust > 95 and Girl.used_to_anal:
            $ approval_bonus += 5

        if Girl.lust > 85 and context == "auto": #She's really horny
            $ approval_bonus += 10

        if context == "shift":
            $ approval_bonus += 10

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (4*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 25
    elif action == "eat_ass":
        if Girl.action_counter["eat_ass"]: #You've done it before
            $ approval_bonus += 20

        if Girl.legs_covered: # she's got pants on.
            $ approval_bonus -= 25

        if Girl.lust > 95:
            $ approval_bonus += 20
        elif Girl.lust > 85: #She's really horny
            $ approval_bonus += 15

        if Girl.lust > 85 and context == "auto": #auto
            $ approval_bonus += 10

        if context == "shift":
            $ approval_bonus += 10

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (4*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 25
    elif action == "handjob":
        if Girl.action_counter[action] >= 7: # She loves it
            $ approval_bonus += 10
        elif Girl.action_counter[action] >= 3: #You've done it before several times
            $ approval_bonus += 7
        elif Girl.action_counter[action]: #You've done it before
            $ approval_bonus += 3

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (3*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 40

        if Girl.addiction >= 75 and Girl.event_counter["swallowed"] >= 3: #She's really strung out and has swallowed
            $ approval_bonus += 15
        if Girl.addiction >= 75:
            $ approval_bonus += 5

        if context == "shift":
            $ approval_bonus += 15
    elif action == "footjob":
        if Girl.action_counter[action] >= 7: # She loves it
            $ approval_bonus += 10
        elif Girl.action_counter[action] >= 3: #You've done it before several times
            $ approval_bonus += 7
        elif Girl.action_counter[action]: #You've done it before
            $ approval_bonus += 3

        if Girl.addiction >= 75 and Girl.event_counter["swallowed"] >=3: #She's really strung out and has swallowed
            $ approval_bonus += 10
        if Girl.addiction >= 75:
            $ approval_bonus += 5

        if context == "shift":
            $ approval_bonus += 15
        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (3*taboo)
        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 40
    elif action == "titjob":
        if Girl.action_counter[action] >= 7: # She loves it
            $ approval_bonus += 10
        elif Girl.action_counter[action] >= 3: #You've done it before several times
            $ approval_bonus += 7
        elif Girl.action_counter[action]: #You've done it before
            $ approval_bonus += 5

        if Girl.seen_breasts and approval_check(Girl, 500): # You've seen her tits.
            $ approval_bonus += 10
        if not Girl.outfit["bra"] and not Girl.outfit["top"]: #She's already topless
            $ approval_bonus += 10

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (5*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 30

        if Girl.lust > 75: #She's really horny
            $ approval_bonus += 10

        if Girl.addiction >= 75 and Girl.event_counter["swallowed"] >= 3: #She's really strung out and has swallowed
            $ approval_bonus += 15
        if Girl.addiction >= 75:
            $ approval_bonus += 5

        if context == "shift":
            $ approval_bonus += 15
    elif action == "blowjob":
        if Girl.action_counter[action] >= 7: # She loves it
            $ approval_bonus += 15
        elif Girl.action_counter[action] >= 3: #You've done it before several times
            $ approval_bonus += 10
        elif Girl.action_counter[action]: #You've done it before
            $ approval_bonus += 7

        if Girl.addiction >= 75 and Girl.event_counter["swallowed"] >=3: #She's really strung out and has swallowed
            $ approval_bonus += 25
        elif Girl.addiction >= 75: #She's really strung out
            $ approval_bonus += 15

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (4*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 40

        if context == "shift":
            $ approval_bonus += 15
    elif action == "dildo_pussy":
        if Girl.action_counter[action]: #You've done it before
            $ approval_bonus += 15
        if Girl.legs_covered: # she's got pants on.
            $ approval_bonus -= 20

        if Girl.lust > 95:
            $ approval_bonus += 20
        elif Girl.lust > 85: #She's really horny
            $ approval_bonus += 15

        if context == "shift":
            $ approval_bonus += 10
        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (5*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 40
    elif action == "dildo_ass":
        if Girl.used_to_anal:
            $ approval_bonus += 30
        elif "anal" in Girl.recent_history or "dildo_ass" in Girl.recent_history:
            $ approval_bonus -= 20
        elif "anal" in Girl.daily_history or "dildo_ass" in Girl.daily_history:
            $ approval_bonus -= 10
        elif (Girl.action_counter["anal"] + Girl.action_counter["dildo_ass"]) > 0 or Girl.outfit["buttplug"]: #You've done it before
            $ approval_bonus += 20

        if Girl.legs_covered: # she's got pants on.
            $ approval_bonus -= 20

        if Girl.lust > 95:
            $ approval_bonus += 20
        elif Girl.lust > 85: #She's really horny
            $ approval_bonus += 15

        if context == "shift":
            $ approval_bonus += 10
        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (5*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 40
    elif action == "sex":
        if Girl.action_counter["sex"] >= 7: # She loves it
            $ approval_bonus += 15
        elif Girl.action_counter["sex"] >= 3: #You've done it before several times
            $ approval_bonus += 12
        elif Girl.action_counter["sex"]: #You've done it before
            $ approval_bonus += 10

        if Girl.addiction >= 75 and (Girl.event_counter["creampied"] + Girl.event_counter["anal_creampied"]) >=3: #She's really strung out and has creampied
            $ approval_bonus += 20
        elif Girl.addiction >= 75:
            $ approval_bonus += 15

        if Girl.lust > 85:
            $ approval_bonus += 10
        elif Girl.lust > 75: #She's really horny
            $ approval_bonus += 5

        if context == "shift":
            $ approval_bonus += 10
        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (4*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 40
    elif action == "anal":
        if Girl.action_counter["anal"]  >= 7: # She loves it
            $ approval_bonus += 20
        elif Girl.action_counter["anal"]  >= 3: #You've done it before several times
            $ approval_bonus += 17
        elif Girl.action_counter["anal"] : #You've done it before
            $ approval_bonus += 15

        if Girl.addiction >= 75 and (Girl.event_counter["creampied"] + Girl.event_counter["anal_creampied"]) >=3: #She's really strung out and has creampied
            $ approval_bonus += 25
        elif Girl.addiction >= 75:
            $ approval_bonus += 15

        if Girl.lust > 85:
            $ approval_bonus += 10
        elif Girl.lust > 75: #She's really horny
            $ approval_bonus += 5

        if Girl.used_to_anal:
            $ approval_bonus += 10
        elif "anal" in Girl.recent_history:
            $ approval_bonus -= 20
        elif "anal" in Girl.daily_history:
            $ approval_bonus -= 10

        if context == "shift":
            $ approval_bonus += 10
        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (5*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 40
    elif action == "hotdog":
        if Girl.action_counter["hotdog"] >= 3: #You've done it before several times
            $ approval_bonus += 10
        elif Girl.action_counter["hotdog"]: #You've done it before
            $ approval_bonus += 5

        if Girl.lust > 85:
            $ approval_bonus += 10
        elif Girl.lust > 75: #She's really horny
            $ approval_bonus += 5
        if context == "shift":
            $ approval_bonus += 10
        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (3*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 40

    if Girl.event_counter["forced"] and not Girl.forced:
        $ approval_bonus -= 5*Girl.event_counter["forced"]

    if taboo and "no_taboo" in Girl.daily_history:
        $ approval_bonus -= 10

    if "no_" + action in Girl.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_" + action in Girl.recent_history else 0

    return

label end_of_action_round(Girl, action):
    $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus

    if Player.focus >= 100 or Girl.lust >= 100:
        if Player.focus >= 100:
            call Player_Cumming(Girl)

            if "_angry" in Girl.recent_history:
                call reset_position(Girl)

                return [None, "stop"]

            $ Girl.change_stat("lust", 200, 5)

            if 100 > Girl.lust >= 70 and Girl.event_counter["orgasmed"] < 2 and Girl.SEXP >= 20:
                $ Girl.add_word(0, "unsatisfied", "unsatisfied")

            $ line = "came"

        if Girl.lust >= 100:
            call Girl_Cumming(Girl)

            if "_angry" in Girl.recent_history:
                return [None, "stop"]

        if line == "came": #ex Player.focus <= 20:
            $ line = 0

            if not Player.semen:
                if action in sex_actions:
                    $ line = renpy.random.choice(["She's emptied you out, you'll need to take a break."
                        "You're pretty wiped, better stop for now."])

                    "[line]"

                    return [None, "stop"]
                else:
                    "You're emptied out, you should probably take a break."

            if "unsatisfied" in Girl.recent_history:#And Rogue_sprite is unsatisfied,
                call girl_unsatisfied_menu(Girl, action)

                if _return:
                    return [None, "stop"]

    if Partner and Partner.lust >= 100:
        call Girl_Cumming(Partner)

    if action in ["kiss", "fondle_thighs", "fondle_breasts", "eat_pussy", "suck_breasts", "fondle_ass", "insert_ass", "handjob", "footjob", "titjob"]:
        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0
    elif action in ["blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

    if Girl.SEXP >= 100 or approval_check(Girl, 1200, "LO"):
        pass
    elif counter == (5 + Girl.action_counter[action]):
        call starting_to_get_bored_reactions(Girl, action)
    elif action in ["fondle_pussy", "finger_ass", "dildo_pussy", "dildo_ass"] and Girl.lust >= 80:
        pass
    elif action in ["fondle_breasts", "suck_breasts"] and Girl.lust >= 85:
        pass
    elif action in fondle_actions and counter == (15 + Girl.action_counter[action]) and Girl.SEXP >= 15 and not approval_check(Girl, 1500):
        call definitely_bored_now_reactions(Girl, action)
    elif action in ["handjob, footjob, titjob, blowjob", "sex", "anal", "hotdog"] and counter == (10 + Girl.action_counter[action]) and Girl.SEXP <= 100 and not approval_check(Girl, 1200, "LO"):
        call definitely_bored_now_reactions(Girl, action)
    elif action in ["kiss", "dildo_pussy", "dildo_ass"] and counter == (15 + Girl.action_counter[action]) and Girl.SEXP >= 15 and not approval_check(Girl, 1200, "LO"):
        call definitely_bored_now_reactions(Girl, action)
    elif action in ["footjob"] and counter == 20:
        call definitely_bored_now_reactions(Girl, action)

    if _return:
        return _return

    call Escalation(Girl)

    if round == 10:
        call ten_rounds_left_lines(Girl, action)
    elif round == 5:
        call five_rounds_left_lines(Girl, action)

    return False

label set_offhand_action(Girl, shift_focus = False):
    if shift_focus:
        $ temp = offhand_action

        $ offhand_action = primary_action
        $ primary_action = temp

        if primary_action == "fondle_breasts":
            "You shift your attention to her breasts."
        elif primary_action == "suck_breasts":
            "You shift your attention to her breasts."
        elif primary_action == "fondle_pussy":
            "You shift your attention to her pussy."
        elif primary_action == "eat_pussy":
            "You shift your attention to her pussy."
        elif primary_action == "fondle_ass":
            "You shift your attention to her ass."
        elif primary_action == "finger_ass":
            "You shift your attention to her ass."
        elif primary_action == "kiss":
            "You go back to kissing her deeply."

        return [primary_action, "shift"]
    elif primary_action:
        menu:
            "Also kiss her." if primary_action in ("fondle_breasts","fondle_pussy", "fondle_thighs", "fondle_ass", "finger_ass", "sex", "anal", "hotdog", "dildo_pussy", "dildo_ass"):
                "You lean in and start kissing her."
                $ offhand_action = "kiss"

                return [offhand_action, "offhand"]
            "Also fondle her breasts." if primary_action in ("kiss","fondle_pussy", "fondle_thighs", "fondle_ass", "finger_ass", "suck_breasts", "eat_pussy", "eat_ass", "sex", "anal", "hotdog", "footjob", "dildo_pussy", "dildo_ass"):
                $ offhand_action = "fondle_breasts"

                return [offhand_action, "offhand"]
            "Also suck her breasts." if primary_action in ("fondle_breasts","fondle_pussy", "fondle_thighs", "fondle_ass", "finger_ass", "sex", "anal", "hotdog", "dildo_pussy", "dildo_ass"):
                $ offhand_action = "suck_breasts"

                return [offhand_action, "offhand"]
            "Also fondle her pussy." if primary_action in ("kiss","fondle_breasts","fondle_thighs", "fondle_ass", "finger_ass", "suck_breasts", "eat_pussy", "eat_ass", "sex", "anal", "hotdog", "footjob", "dildo_pussy", "dildo_ass"):
                $ offhand_action = "fondle_pussy"

                return [offhand_action, "offhand"]
            "Also fondle her ass." if primary_action in ("kiss","fondle_breasts","fondle_pussy", "fondle_thighs", "finger_ass", "suck_breasts", "eat_pussy", "eat_ass", "sex", "anal", "hotdog", "footjob", "dildo_pussy", "dildo_ass"):
                $ offhand_action = "fondle_ass"

                return [offhand_action, "offhand"]
            "Also finger her ass." if primary_action in ("fondle_breasts","fondle_pussy", "fondle_thighs", "fondle_ass", "suck_breasts", "eat_pussy", "eat_ass", "sex", "hotdog", "footjob", "dildo_pussy"):
                $ offhand_action = "finger_ass"

                return [offhand_action, "offhand"]
            "Also jack it." if primary_action in ("fondle_breasts","fondle_pussy", "fondle_thighs", "fondle_ass", "finger_ass", "suck_breasts", "eat_pussy", "eat_ass", "dildo_pussy", "dildo_ass"):
                call jerking_off(Girl)
            "Nevermind":
                pass

    return False
