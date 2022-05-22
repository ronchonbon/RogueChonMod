label action(Girl):
    if primary_action in dildo_actions:
        call dildo_check(Girl)

        if not _return:
            return

    $ round -= 5 if round > 5 else (round-1)

    call shift_focus(Girl)
    call set_approval_bonus(Girl, primary_action)
    call action_approval_checks(Girl, primary_action)

    if primary_action == "kiss" and Girl == EmmaX and not approval_check(Girl, 1000):
        $ Girl.change_face("_sadside")

        ch_e "Not when we barely know each other. . ."

        $ Girl.recent_history.append("no_kiss")
        $ Girl.daily_history.append("no_kiss")

        return

    if action_context in ["auto", "offhand"]:
        call auto_action_narrations(Girl, primary_action)

        if approval:
            call auto_approved_reactions(Girl, primary_action)

            if action_context == "auto":
                jump before_action
            else:
                return
        else:
            call auto_rejected_reactions(Girl, primary_action)

            $ approval_bonus = 0
            $ offhand_action = 0

            return
    elif action_context == "pullback":
        call pullback_reactions(Girl, primary_action)
        jump before_action
    elif primary_action in anal_insertion_actions and not Girl.used_to_anal and ("finger_ass" in Girl.daily_history or "dildo_anal" in Girl.daily_history or "anal" in Girl.daily_history):
        call anal_insertion_reactions(Girl)
    elif primary_action in Girl.recent_history:
        call recent_action_reactions(Girl)
        jump before_action
    elif primary_action in Girl.daily_history:
        call daily_action_reactions(Girl)
        jump before_action

    if primary_action == "kiss":
        if approval > 1 and not Girl.action_counter["kiss"] and not Girl.forced:
            $ Girl.change_face("_sexy")
            $ Girl.eyes = "_side"

            call excited_for_first_kiss_lines(Girl, primary_action)
            jump before_action
        elif approval and not Girl.action_counter["kiss"]:
            $ Girl.change_face("_sexy")
            $ Girl.eyes = "_side"

            call less_excited_for_first_kiss_lines(Girl, primary_action)
            jump before_action
        elif approval and "kiss" in Girl.recent_history:
            $ Girl.change_face("_sexy", 1)

            call recent_action_lines(Girl, primary_action)
            jump before_action
        elif approval and "kiss" in Girl.daily_history:
            $ Girl.change_face("_sexy", 1)

            call daily_action_lines(Girl, primary_action)
            jump before_action
        elif approval > 1 and Girl.love > Girl.obedience:
            $ Girl.change_face("_sexy")

            call excited_for_kiss_love_lines(Girl, primary_action)
            jump before_action
        elif approval_check(Girl, 500, "O") and Girl.obedience > Girl.love:
            $ Girl.change_face("_normal")

            call excited_for_kiss_obedience_lines(Girl, primary_action)

            $ Girl.change_stat("obedience", 60, 1)

            jump before_action
        elif approval_check(Girl, 250, "O",Alt=[[KittyX,LauraX],300]) and approval_check(Girl, 250, "L",Alt=[[KittyX,LauraX],200]):
            $ Girl.change_face("_bemused")

            Girl.voice "Ok, fine."

            $ Girl.change_stat("obedience", 50, 3)

            jump before_action
        elif Girl.addiction >= 50:
            $ Girl.change_face("_sexy")
            $ Girl.eyes = "_manic"

            call kiss_addicted_lines(Girl, primary_action)
            jump before_action
        elif approval:
            $ Girl.change_face("_bemused")

            call kiss_accepted_lines(Girl, primary_action)
            jump before_action
        else:
            $ Girl.change_face("_normal")
            $ Girl.mouth = "_sad"

            call otherwise_not_interested_lines(Girl, primary_action)

            $ Girl.recent_history.append("no_kiss")
            $ Girl.daily_history.append("no_kiss")
    else:
        if not Girl.action_counter[primary_action] and "no_" + primary_action not in Girl.recent_history:
            call first_time_asking_reactions(Girl, primary_action)

        if not Girl.action_counter[primary_action] and approval:
            call first_action_approval(Girl, primary_action)
        elif approval:
            call action_approved(Girl, primary_action)

        if approval >= 2:
            call action_accepted(Girl, primary_action)
            label begging_approved:
            jump before_action
        else:
            call action_disapproved(Girl, primary_action)

        call action_rejected(Girl, primary_action)
        label begging_rejected:

    return

label before_action:
    if Taboo:
        $ focused_Girl.inhibition += int(Taboo/10)
        $ focused_Girl.lust += int(Taboo/5)

    $ focused_Girl.change_face("_sexy")

    if primary_action == "kiss":
        $ focused_Girl.change_stat("inhibition", 10, 1)
        $ focused_Girl.change_stat("inhibition", 20, 1)

        call expression focused_Girl.tag + "_Kissing_Launch" pass("kiss")

        if focused_Girl.action_counter["kiss"] >= 10 and focused_Girl.inhibition >= 300:
            $ focused_Girl.change_face("_sucking")
        elif focused_Girl.action_counter["kiss"] > 1 and focused_Girl.addiction >= 50:
            $ focused_Girl.change_face("_sucking")
        else:
            $ focused_Girl.change_face("_kiss",2)

        if focused_Girl == RogueX and not Girl.action_counter["kiss"]:
            jump Rogue_first_kiss
        else:
            call kissing_narrations(focused_Girl)
    elif primary_action in fondle_actions:
        if not focused_Girl.forced and action_context != "auto":
            $ approval_bonus = 0

            if primary_action in ["eat_pussy", "eat_ass"] and focused_Girl.PantsNum() >= 6:
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
                $ focused_Girl.Brows = "_confused"
                $ focused_Girl.Eyes = "_sexy"
                $ focused_Girl.Mouth = "_smile"
        else:
            if not focused_Girl.forced and action_context != "auto":
                if primary_action == "dildo_pussy":
                    $ approval_bonus = 15 if focused_Girl.PantsNum() > 6 else 0
                elif primary_action == "dildo_ass":
                    $ approval_bonus = 20 if focused_Girl.PantsNum() > 6 else 0

                call Bottoms_Off(focused_Girl)

                if "_angry" in focused_Girl.recent_history:
                    return

            $ approval_bonus = 0

        call Seen_First_Peen(focused_Girl, Partner, React = action_context)

        if primary_action == "handjob":
            call expression focused_Girl.tag + "_HJ_Launch" pass("L")
        elif primary_action == "titjob":
            call expression focused_Girl.tag + "_TJ_Launch" pass("L")
        elif primary_action == "blowjob":
            call expression focused_Girl.tag + "_BJ_Launch" pass("L")
        elif primary_action in dildo_actions:
            call expression focused_Girl.tag + "_Pussy_Launch" pass(primary_action)
    elif primary_action in sex_actions:
        call Seen_First_Peen(focused_Girl, Partner, React = action_context)

        $ focused_Girl.pose = "doggy"

        call expression focused_Girl.tag + "_Sex_Launch" pass(primary_action)

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

            $ focused_Girl.underwear_pulled_down = 1

            call expression focused_Girl.tag + "_First_Bottomless" pass(1)
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

                if (focused_Girl.PantsNum() > 6 and not focused_Girl.upskirt) and (focused_Girl.underwear and not focused_Girl.underwear_pulled_down):
                    "You quickly pull down her pants and her [focused_Girl.Panties] and press against her [word]."
                elif (focused_Girl.underwear and not focused_Girl.underwear_pulled_down):
                    "You quickly pull down her [focused_Girl.Panties] and press against her [word]."

                $ focused_Girl.upskirt = 1
                $ focused_Girl.underwear_pulled_down = 1
                $ focused_Girl.SeenPanties = 1

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

    if Taboo:
        if primary_action == "fondle_thighs":
            $ focused_Girl.change_stat("lust", 200, (int(Taboo/5)))
            $ focused_Girl.change_stat("inhibition", 200, (2*(int(Taboo/5))))
        elif primary_action in ["fondle_breasts", "suck_breasts", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "dildo_pussy", "dildo_ass"]:
            $ focused_Girl.inhibition += int(Taboo/10)
            $ focused_Girl.lust += int(Taboo/5)
        elif primary_action in ["fondle_pussy", "eat_pussy", "finger_ass", "eat_ass"]:
            if focused_Girl == JeanX and focused_Girl.Taboo:
                $ focused_Girl.change_stat("inhibition", 200, (int(Taboo/10)))
            elif Taboo:
                $ focused_Girl.inhibition += int(Taboo/10)

            $ focused_Girl.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()

        $ action_context = None

    if primary_action in inside_panties_actions:
        if focused_Girl.wearing_skirt:
            $ focused_Girl.upskirt = 1
            $ focused_Girl.SeenPanties = 1

        call expression focused_Girl.tag + "_First_Bottomless" pass(1)

    $ line = 0
    $ counter = 0

    if primary_action == "fondle_pussy":
        $ action_speed = 1
    elif primary_action == "finger_pussy":
        $ action_speed = 2
    elif primary_action == "sex":
        $ Player.cock_position = "sex"

        $ action_speed = 1
    elif primary_action == "anal":
        $ Player.cock_position = "anal"

        $ action_speed = 1
    elif primary_action == "hotdog":
        $ action_speed = 1

    if Taboo:
        $ focused_Girl.drain_word("no_taboo")

    $ focused_Girl.drain_word("no_" + primary_action)
    $ focused_Girl.add_word(0, primary_action, primary_action)

    if primary_action in fondle_actions:
        if focused_Girl != EmmaX:
            call expression focused_Girl.tag + "_Pussy_Launch" pass(primary_action)
        else:
            if focused_Girl.pose in ["doggy", "sex"]:
                call ViewShift(focused_Girl, focused_Girl.pose, 0, primary_action)
            else:
                call ViewShift(focused_Girl, "pussy", 0, primary_action)
    elif primary_action in breast_actions:
        call expression focused_Girl.tag + "_Breasts_Launch" pass(primary_action)
    elif primary_action == "footjob":
        call expression focused_Girl.tag + "_Sex_Launch" pass(primary_action)

label action_cycle:
    if primary_action in mouth_actions:
        if primary_action != "kiss" and offhand_action == "kiss":
            $ offhand_action = 0

    while round > 0:
        if primary_action == "kiss":
            call expression focused_Girl.tag + "_Kissing_Launch" pass("kiss")

            $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0
        if primary_action in fondle_actions:
            call ViewShift(focused_Girl, Girl.pose, 0, primary_actions)
        elif primary_action in ["footjob", "sex", "anal", "hotdog"]:
            call expression focused_Girl.tag + "_Sex_Launch" pass(primary_action)

            if primary_action == "sex":
                $ Player.cock_position = "sex"
            elif primary_action == "anal":
                $ Player.cock_position = "anal"
            elif primary_action == "hotdog":
                $ Player.cock_position = "out"
        elif primary_action in dildo_actions:
            call ViewShift(focused_Girl, Girl.pose, 0)

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
            if focused_Girl.underwear or focused_Girl.PantsNum() >= 6 or focused_Girl.HoseNum() >= 5: #This checks if Rogue wants to strip down.
                call Girl_Undress(focused_Girl, "auto")

        call Sex_Dialog(focused_Girl, Partner)

        $ counter += 1
        $ round -= 1

        if (primary_action in ["blowjob"] and action_speed) or primary_action in ["sex", "anal"]:
            $ Player.cock_wet = 1
            $ Player.spunk = 0 if (Player.spunk and "in" not in focused_Girl.spunk) else Player.spunk #cleans you off after one cycle

        call end_of_action_round(focused_Girl, primary_action)

        if _return:
            return

        if primary_action in breast_actions:
            if focused_Girl.lust >= 50 and not focused_Girl.top_pulled_up and (focused_Girl.Chest or focused_Girl.Over):
                call pull_off_top_narration(focused_Girl)

                $ focused_Girl.top_pulled_up = 1

                call expression focused_Girl.tag + "_First_Topless"

    call end_of_action_reactions(focused_Girl, action)

label after_action:
    if primary_action in sex_actions:
        $ Player.sprite = 0
        $ Player.cock_position = "out"

        call expression focused_Girl.tag + "_Sex_Reset"
    elif primary_action in [fondle_actions, dildo_actions]:
        call expression focused_Girl.tag + "_Pos_Reset"

    $ focused_Girl.change_face("_sexy")
    $ focused_Girl.remaining_actions -= 1

    call action_specific_consequences(focused_Girl, primary_action)

    if primary_action == "kiss" and primary_action not in focused_Girl.recent_history:
        if Girl.love > 300:
            $ Girl.change_stat("love", 60, 4)
        $ Girl.change_stat("love", 70, 1)

    if primary_action in ["fondle_thighs", "fondle_ass"]:
        if RogueX.PantsNum() < 6 or RogueX.upskirt:
            $ RogueX.addiction_rate += 1

            if Player.addictive:
                $ RogueX.addiction_rate += 1
    elif primary_action not in dildo_actions:
        if primary_action == "kiss":
            $ focused_Girl.addiction_rate += 2 if focused_Girl.addiction_rate < 5 else 1
        else:
            $ focused_Girl.addiction_rate += 1

        if Player.addictive:
            $ focused_Girl.addiction_rate += 1

    if primary_action in ["handjob", "footjob"]:
        $ focused_Girl.change_stat("lust", 90, 5)

    if achievement is not None and achievement in Achievements:
        pass
    elif primary_action == "titjob" and Girl.action_counter[primary_action] > 5:
        pass
    elif primary_action == "kiss" and Girl.action_counter[primary_action] > 10:
        pass
    elif primary_action not in dildo_actions and Girl.action_counter[primary_action] >= 10:
        if primary_action not in ["anal"]:
            $ focused_Girl.SEXP += 5
        else:
            $ focused_Girl.SEXP += 7

        if achievement is not None:
            $ Achievements.append(achievement)

        if primary_action not in ["anal"] and not action_context:
            $ focused_Girl.change_face("_smile", 1)
        elif primary_action in ["anal"] and not action_context:
            $ focused_Girl.change_face("_bemused", 1)

        call achievement_lines(focused_Girl, primary_action)
    elif primary_action == "blowjob" and action_context == "shift":
        pass
    elif Girl.action_counter[primary_action] == 1:
        call first_action_response(focused_Girl, primary_action)
    elif (primary_action in cock_actions or primary_action == "kiss") and Girl.action_counter[primary_action] == 5:
        call action_done_five_times_lines(focused_Girl)
    elif primary_action in sex_actions and not action_context:
        if "unsatisfied" in focused_Girl.recent_history:
            call unsatisfied_reactions(Girl, primary_action)

    if primary_action == "kiss" and not action_context and focused_Girl.action_counter["kiss"] > 5 and focused_Girl.lust > 50 and approvalcheck(focused_Girl, 950):
        call would_you_like_more_lines(Girl, primary_action)

    $ approval_bonus = 0

    if action_context == "shift":
        call switching_action_lines(focused_Girl, primary_action)
    elif primary_action == "kiss":
        call expression focused_Girl.Tah + "_Pos_Reset"
    elif primary_action == "handjob":
        call expression focused_Girl.tag + "_HJ_Reset"
    elif primary_action == "footjob":
        call expression focused_Girl.tag + "_Doggy_Reset"
    elif primary_action == "titjob":
        call expression focused_Girl.tag + "_TJ_Reset"
    elif primary_action == "blowjob":
        call expression focused_Girl.tag + "_BJ_Reset"

    call checkout

    return

label set_approval_bonus(Girl, action):
    if primary_action == "fondle_thighs":
        if Girl.action_counter["fondle_thighs"]:
            $ approval_bonus += 10

        if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 5:
            $ approval_bonus -= 5

        if Girl.lust > 75:
            $ approval_bonus += 10

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += Taboo

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 25
    elif primary_action == "fondle_breasts":
        if Girl.action_counter["fondle_breasts"]:
            $ approval_bonus += 15

        if Girl.lust > 75: #She's really horny
            $ approval_bonus += 20

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (3*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 20
    elif primary_action == "suck_breasts":
        if Girl.action_counter["suck_breasts"]: #You've done it before
            $ approval_bonus += 15

        if not Girl.Chest and not Girl.Over:
            $ approval_bonus += 15

        if Girl.lust > 75: #She's really horny
            $ approval_bonus += 20

        if Girl.lust > 75 and action_context == "auto": #She's really horny
            $ approval_bonus += 10

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (4*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 25
    elif primary_action == "fondle_pussy":
        if Girl.action_counter["fondle_pussy"]: #You've done it before
            $ approval_bonus += 20

        if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 5: # she's got pants on.
            $ approval_bonus -= 10

        if Girl.lust > 75: #She's really horny
            $ approval_bonus += 15

        if Girl.lust > 75 and action_context == "auto": #She's really horny
            $ approval_bonus += 10

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (2*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 25
    elif primary_action == "eat_pussy":
        if Girl.action_counter["eat_pussy"]: #You've done it before
            $ approval_bonus += 15

        if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 5: # she's got pants on.
            $ approval_bonus -= 15

        if Girl.lust > 95:
            $ approval_bonus += 20
        elif Girl.lust > 85: #She's really horny
            $ approval_bonus += 15

        if Girl.lust > 85 and action_context == "auto": #She's really horny
            $ approval_bonus += 10

        if action_context == "shift":
            $ approval_bonus += 10

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (4*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 25
    elif primary_action == "fondle_ass":
        if Girl.action_counter["fondle_ass"]: #You've done it before
            $ approval_bonus += 10

        if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 5: # she's got pants on.
            $ approval_bonus -= 5

        if Girl.lust > 75: #She's really horny
            $ approval_bonus += 15

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += Taboo

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 25
    elif primary_action == "finger_ass":
        if Girl.action_counter["finger_ass"]: #You've done it before
            $ approval_bonus += 25

        if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 5: # she's got pants on.
            $ approval_bonus -= 15

        if Girl.lust > 85 and Girl.used_to_anal: #She's really horny
            $ approval_bonus += 15

        if Girl.lust > 95 and Girl.used_to_anal:
            $ approval_bonus += 5

        if Girl.lust > 85 and action_context == "auto": #She's really horny
            $ approval_bonus += 10

        if action_context == "shift":
            $ approval_bonus += 10

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (4*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 25
    elif primary_action == "eat_ass":
        if Girl.action_counter["eat_ass"]: #You've done it before
            $ approval_bonus += 20

        if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 5: # she's got pants on.
            $ approval_bonus -= 25

        if Girl.lust > 95:
            $ approval_bonus += 20
        elif Girl.lust > 85: #She's really horny
            $ approval_bonus += 15

        if Girl.lust > 85 and action_context == "auto": #auto
            $ approval_bonus += 10

        if action_context == "shift":
            $ approval_bonus += 10

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (4*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 25
    elif primary_action == "handjob":
        if Girl.action_counter[primary_action] >= 7: # She loves it
            $ approval_bonus += 10
        elif Girl.action_counter[primary_action] >= 3: #You've done it before several times
            $ approval_bonus += 7
        elif Girl.action_counter[primary_action]: #You've done it before
            $ approval_bonus += 3

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (3*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 40

        if Girl.addiction >= 75 and Girl.event_counter["swallowed"] >= 3: #She's really strung out and has swallowed
            $ approval_bonus += 15
        if Girl.addiction >= 75:
            $ approval_bonus += 5

        if action_context == "shift":
            $ approval_bonus += 15
    elif primary_action == "footjob":
        if Girl.action_counter[primary_action] >= 7: # She loves it
            $ approval_bonus += 10
        elif Girl.action_counter[primary_action] >= 3: #You've done it before several times
            $ approval_bonus += 7
        elif Girl.action_counter[primary_action]: #You've done it before
            $ approval_bonus += 3

        if Girl.addiction >= 75 and Girl.event_counter["swallowed"] >=3: #She's really strung out and has swallowed
            $ approval_bonus += 10
        if Girl.addiction >= 75:
            $ approval_bonus += 5

        if action_context == "shift":
            $ approval_bonus += 15
        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (3*Taboo)
        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 40
    elif primary_action == "titjob":
        if Girl.action_counter[primary_action] >= 7: # She loves it
            $ approval_bonus += 10
        elif Girl.action_counter[primary_action] >= 3: #You've done it before several times
            $ approval_bonus += 7
        elif Girl.action_counter[primary_action]: #You've done it before
            $ approval_bonus += 5

        if Girl.SeenChest and approval_check(Girl, 500): # You've seen her tits.
            $ approval_bonus += 10
        if not Girl.Chest and not Girl.Over: #She's already topless
            $ approval_bonus += 10

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (5*Taboo)

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

        if action_context == "shift":
            $ approval_bonus += 15
    elif primary_action == "blowjob":
        if Girl.action_counter[primary_action] >= 7: # She loves it
            $ approval_bonus += 15
        elif Girl.action_counter[primary_action] >= 3: #You've done it before several times
            $ approval_bonus += 10
        elif Girl.action_counter[primary_action]: #You've done it before
            $ approval_bonus += 7

        if Girl.addiction >= 75 and Girl.event_counter["swallowed"] >=3: #She's really strung out and has swallowed
            $ approval_bonus += 25
        elif Girl.addiction >= 75: #She's really strung out
            $ approval_bonus += 15

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (4*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 40

        if action_context == "shift":
            $ approval_bonus += 15
    elif primary_action == "dildo_pussy":
        if Girl.action_counter[primary_action]: #You've done it before
            $ approval_bonus += 15
        if Girl.PantsNum() > 6: # she's got pants on.
            $ approval_bonus -= 20

        if Girl.lust > 95:
            $ approval_bonus += 20
        elif Girl.lust > 85: #She's really horny
            $ approval_bonus += 15

        if action_context == "shift":
            $ approval_bonus += 10
        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (5*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 40
    elif primary_action == "dildo_ass":
        if Girl.used_to_anal:
            $ approval_bonus += 30
        elif "anal" in Girl.recent_history or "dildo_anal" in Girl.recent_history:
            $ approval_bonus -= 20
        elif "anal" in Girl.daily_history or "dildo_anal" in Girl.daily_history:
            $ approval_bonus -= 10
        elif (Girl.action_counter["anal"] + Girl.action_counter["dildo_ass"] + Girl.Plug) > 0: #You've done it before
            $ approval_bonus += 20

        if Girl.PantsNum() > 6: # she's got pants on.
            $ approval_bonus -= 20

        if Girl.lust > 95:
            $ approval_bonus += 20
        elif Girl.lust > 85: #She's really horny
            $ approval_bonus += 15

        if action_context == "shift":
            $ approval_bonus += 10
        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (5*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 40
    elif primary_action == "sex":
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

        if action_context == "shift":
            $ approval_bonus += 10
        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (4*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 40
    elif primary_action == "anal":
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

        if action_context == "shift":
            $ approval_bonus += 10
        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (5*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 40
    elif primary_action == "hotdog":
        if Girl.action_counter["hotdog"] >= 3: #You've done it before several times
            $ approval_bonus += 10
        elif Girl.action_counter["hotdog"]: #You've done it before
            $ approval_bonus += 5

        if Girl.lust > 85:
            $ approval_bonus += 10
        elif Girl.lust > 75: #She's really horny
            $ approval_bonus += 5
        if action_context == "shift":
            $ approval_bonus += 10
        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (3*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 40

    if Girl.event_counter["forced"] and not Girl.forced:
        $ approval_bonus -= 5*Girl.event_counter["forced"]

    if Taboo and "no_taboo" in Girl.daily_history:
        $ approval_bonus -= 10

    if "no_" + primary_action in Girl.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_" + primary_action in Girl.recent_history else 0

    return

label end_of_action_round(Girl, action):
    $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus

    if Player.focus >= 100 or Girl.lust >= 100:
        if Player.focus >= 100:
            call Player_Cumming(Girl)

            if "_angry" in Girl.recent_history:
                if primary_action in sex_actions:
                    call expression Girl.tag + "_Sex_Reset"
                else:
                    call expression Girl.tag + "_Pos_Reset"

                return True

            $ Girl.change_stat("lust", 200, 5)

            if 100 > Girl.lust >= 70 and Girl.event_counter["orgasmed"] < 2 and Girl.SEXP >= 20:
                $ Girl.add_word(0, "unsatisfied", "unsatisfied")

            if Player.focus > 80:
                jump after_action

            $ line = "came"

        if Girl.lust >= 100:
            call Girl_Cumming(Girl)

            if action_context == "shift" or "_angry" in Girl.recent_history:
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

            if "unsatisfied" in Girl.recent_history:#And Rogue is unsatisfied,
                call girl_unsatisfied_menu(Girl, action)

    if Partner and Partner.lust >= 100:
        call Girl_Cumming(Partner)

    if primary_action in ["kiss", "fondle_thighs", "fondle_breasts", "eat_pussy", "suck_breasts", "fondle_ass", "insert_ass", "handjob", "footjob", "titjob"]:
        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0
    elif primary_action in ["blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

    if Girl.SEXP >= 100 or approval_check(Girl, 1200, "LO"):
        pass
    elif counter == (5 + Girl.action_counter[primary_action]):
        call starting_to_get_bored_reactions(Girl, action)
    elif primary_action in ["fondle_pussy", "finger_ass", "dildo_pussy", "dildo_ass"] and Girl.lust >= 80:
        pass
    elif primary_action in ["fondle_breasts", "suck_breasts"] and Girl.lust >= 85:
        pass
    elif primary_action in fondle_actions and counter == (15 + Girl.action_counter[primary_action]) and Girl.SEXP >= 15 and not approval_check(Girl, 1500):
        call definitely_bored_now_reactions(Girl, primary_action)
    elif primary_action in ["handjob, footjob, titjob, blowjob", "sex", "anal", "hotdog"] and counter == (10 + Girl.action_counter[primary_action]) and Girl.SEXP <= 100 and not approval_check(Girl, 1200, "LO"):
        call definitely_bored_now_reactions(Girl, primary_action)
    elif primary_action in ["kiss", "dildo_pussy", "dildo_ass"] and counter == (15 + Girl.action_counter[primary_action]) and Girl.SEXP >= 15 and not approval_check(Girl, 1200, "LO"):
        call definitely_bored_now_reactions(Girl, primary_action)
    elif primary_action in ["footjob"] and counter == 20:
        call definitely_bored_now_reactions(Girl, primary_action)

    call Escalation(Girl)

    if round == 10:
        call ten_rounds_left_lines(Girl, primary_action)
    elif round == 5:
        call five_rounds_left_lines(Girl, primary_action)

    return False
