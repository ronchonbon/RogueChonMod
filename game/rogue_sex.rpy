label Rogue_SexAct(Act=0):
    if AloneCheck(Girl) and Girl.Taboo == 20:
        $ Girl.Taboo = 0
        $ Taboo = 0
    call shift_focus (Girl)
    if Act == "SkipTo":
        $ renpy.pop_call()
        $ renpy.pop_call()

        call SkipTo (Girl)
    elif Act == "switch":
        $ renpy.pop_call()


    elif Act == "masturbate":
        call before_masturbation
        if not action_context:
            return
    elif Act == "lesbian":
        call Les_Prep (Girl)
        if not action_context:
            return
    elif Act == "kiss":
        call KissPrep (Girl)
        if not action_context:
            return
    elif Act == "breasts":
        call Rogue_Fondle_Breasts
        if not action_context:
            return
    elif Act == "blowjob":
        call Rogue_BJ_Prep
        if not action_context:
            return
    elif Act == "handjob":
        call Rogue_HJ_Prep
        if not action_context:
            return
    elif Act == "sex":
        call Rogue_SexPrep
        if not action_context:
            return

label masturbate(Girl):
    $ round -= 5 if round > 5 else (round-1)
    call shift_focus(Girl)
    call set_approval_bonus(Girl, primary_action)
    call action_approval_checks(Girl, primary_action)

    $ Girl.drain_word("unseen",1,0)

    if action_context == "join":
        if approval > 1 or (approval and Girl.lust >= 50):
            $ Player.add_word(1,"join")
            menu:
                extend ""
                "Would you like some help? I could lend some helping hands. . ." if Player.semen and Girl.remaining_actions:
                    $ Girl.change_stat("love", 90, 1)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_face("_sexy")

                    call lend_some_helping_hands_lines(Girl, primary_action)

                    $ Girl.change_stat("obedience", 70, 2)
                    $ Girl.change_stat("inhibition", 70, 1)

                    $ offhand_action = "fondle_breasts"

                    $ Girl.action_counter["masturbation"] += 1

                    jump masturbation_cycle
                "Would you like some help? I could. . . up to you, I guess." if Player.semen and Girl.remaining_actions:
                    $ Girl.change_stat("love", 70, 2)
                    $ Girl.change_stat("love", 90, 1)
                    $ Girl.change_face("_sexy")

                    call lend_some_helping_hands_lines(Girl, primary_action)

                    $ Girl.change_stat("obedience", 70, 2)
                    $ Girl.change_stat("inhibition", 70, 1)

                    $ D20 = renpy.random.randint(1, 20)

                    if D20 > 10:
                        $ offhand_action = "fondle_breasts"
                    else:
                        $ offhand_action = "suck_breasts"

                    $ Girl.action_counter["masturbation"] += 1

                    jump masturbation_cycle
                "Why don't we take care of each other?" if Player.semen and Girl.remaining_actions:
                    $ Girl.change_face("_sexy")

                    call why_dont_we_take_care_of_each_other_lines(Girl, primary_action)

                    $ renpy.pop_call()

                    return
                "You look like you have things well in hand. . .":
                    if Girl.lust >= 50:
                        $ Girl.change_stat("love", 70, 2)
                        $ Girl.change_stat("love", 90, 1)
                        $ Girl.change_face("_sexy")

                        call well_in_hand_lust_lines(Girl, primary_action)

                        $ Girl.change_stat("obedience", 80, 3)
                        $ Girl.change_stat("inhibition", 80, 5)

                        jump masturbation_cycle
                    elif approval_check(Girl, 1000):
                        $ Girl.change_face("_sly")

                        call well_in_hand_approved_lines(Girl, primary_action)
                    else:
                        $ Girl.change_face("_angry")

                        call well_in_hand_disapproved_lines(Girl, primary_action)

        $ Girl.ArmPose = 1
        $ Girl.change_outfit(Changed=0)
        $ Girl.remaining_actions -= 1

        $ Player.change_stat("focus", 50, 30)
        call checkout (1)

        $ action_context = None

        $ renpy.pop_call()

        if approval:
            $ Girl.change_face("_bemused", 2)

            if bg_current == "bg_rogue":
                call what_did_you_come_over_for_approval_lines(Girl, primary_action)
            else:
                call fancy_bumping_into_you_approval_lines(Girl, primary_action)

            $ Girl.blushing = "_blush1"
        else:
            $ Girl.change_stat("love", 200, -5)
            $ Girl.change_face("_angry")
            $ Girl.recent_history.append("_angry")
            $ Girl.daily_history.append("_angry")

            if bg_current == "bg_rogue":
                call what_did_you_come_over_for_disapproval_lines(Girl, primary_action)

                $ renpy.pop_call()

                jump Campus_Map
            else:
                call fancy_bumping_into_you_disapproval_lines(Girl, primary_action)
                call remove_girl (Girl)
        return

    if action_context == Girl:
        if approval > 2:
            if Girl.PantsNum() == 5:
                "[Girl.name]'s hand snakes down her body, and hikes up her skirt."

                $ Girl.upskirt = 1
            elif Girl.PantsNum() > 6:
                "[Girl.name] slides her hand down her body and into her jeans."
            elif Girl.HoseNum() >= 5:
                "[Girl.name]'s hand slides down her body and under her [Girl.hose]."
            elif Girl.underwear:
                "[Girl.name]'s hand slides down her body and under her [Girl.underwear]."
            else:
                "[Girl.name]'s hand slides down her body and begins to caress her pussy."

            $ Girl.SeenPanties = 1

            "She starts to slowly rub herself."

            call expression Girl.Tag + "_First_Bottomless"

            menu:
                "What do you do?"
                "Nothing.":
                    $ Girl.change_stat("inhibition", 80, 3)
                    $ Girl.change_stat("inhibition", 60, 2)

                    "[Girl.name] begins to masturbate."
                "Go for it.":
                    $ Girl.change_face("sexy, 1")
                    $ Girl.change_stat("inhibition", 80, 3)

                    ch_p "That is so sexy, [Girl.petname]."

                    $ Girl.nameCheck()

                    "You lean back and enjoy the show."

                    $ Girl.change_stat("love", 80, 1)
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ Girl.change_face("_surprised")
                    $ Girl.change_stat("inhibition", 70, 1)

                    ch_p "Let's not do that right now, [Girl.petname]."

                    $ Girl.nameCheck()

                    "[Girl.name] pulls her hands away from herself."

                    $ Girl.change_outfit(Changed=0)
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Girl.change_stat("obedience", 30, 2)
                    return
            jump before_masturbation
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
        return

    if not Girl.action_counter["masturbation"]:
        call first_time_asking_reactions(Girl, primary_action)

        $ Girl.change_face("_surprised", 1)
        $ Girl.mouth = "_kiss"

        if Girl.forced:
            $ Girl.change_face("_sad")

            call action_forcefully_approved_lines(Girl, primary_action)

    if not Girl.action_counter["masturbation"] and approval:
        call first_action_approval(Girl, primary_action)
    elif approval:
        call action_approved(Girl, primary_action)

    if approval >= 2:
        call action_accepted(Girl, primary_action)
        label begging_approved:

        if Girl.forced:
            $ Girl.change_face("_sad")
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 60, 1)
        else:
            $ Girl.change_face("_sexy", 1)
            $ Girl.change_stat("love", 90, 1)
            $ Girl.change_stat("inhibition", 50, 3)

        $ Girl.change_stat("obedience", 20, 1)
        $ Girl.change_stat("obedience", 60, 1)
        $ Girl.change_stat("inhibition", 70, 2)

        jump before_masturbation
    else:
        call action_disapproved(Girl, primary_action)

    call action_rejected(Girl, primary_action)

    return

label before_masturbation:
    $ Girl.upskirt = 1
    $ Girl.underwear_pulled_down = 1
    call Rogue_First_Bottomless (1)
    call set_the_scene (Dress=0)


    if "unseen" in Girl.recent_history:
        $ Girl.change_face("_sexy")
        $ Girl.eyes = "_closed"
        $ Girl.ArmPose = 2
        "You see [Girl.name] leaning back, masturbating. You don't think she's noticed you yet."
    else:
        $ Girl.change_face("_sexy")
        $ Girl.ArmPose = 2
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


    $ primary_action = "masturbation"
    if not girl_offhand_action:
        $ girl_offhand_action = "fondle_pussy"

    if action_context:
        $ renpy.pop_call()
        $ action_context = None
    $ Line = 0
    if Taboo:
        $ Girl.drain_word("no_taboo")
    $ Girl.drain_word("no_masturbation")
    $ Girl.recent_history.append("masturbation")
    $ Girl.daily_history.append("masturbation")

label masturbation_cycle:
    if action_context == "join":

        $ renpy.pop_call()
        $ action_context = None

    while round > 0:
        call Rogue_Pos_Reset ("masturbation")
        call shift_focus (Girl)
        $ Girl.lust_face
        if "unseen" in Girl.recent_history:
            $ Girl.eyes = "_closed"

        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if Player.focus < 100:

            menu:
                "Keep Watching.":
                    pass

                "[Girl.name]. . .[[jump in]" if "unseen" not in Girl.recent_history and "join" not in Player.recent_history and Girl.location == bg_current:
                    "[Girl.name] slows what she's doing with a sly grin."

                    call masturbation_join_in_lines(Girl, primary_action)

                    $ action_context = "join"
                    call Rogue_Masturbate
                "\"Ahem. . .\"" if "unseen" in Girl.recent_history:
                    jump Rogue_M_Interupted

                "Start jack'in it." if offhand_action != "jerking_off":
                    call jerking_off (Girl)
                "Stop jack'in it." if offhand_action == "jerking_off":
                    $ offhand_action = 0

                "Slap her ass" if Girl.location == bg_current:
                    if "unseen" in Girl.recent_history:
                        "You smack [Girl.name] firmly on the ass!"
                        jump Rogue_M_Interupted
                    else:
                        call Slap_Ass (Girl)
                        $ counter += 1
                        $ round -= 1
                        jump masturbation_cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "Change what I'm doing":

                    menu:
                        "Offhand action" if Girl.location == bg_current:
                            if Girl.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ Girl.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (Girl, "tired")

                        "Threesome actions (locked)" if not Partner or "unseen" in Girl.recent_history or Girl.location == bg_current:
                            pass
                        "Threesome actions" if Girl.location == bg_current and Partner and "unseen" not in Girl.recent_history:
                            menu:
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (Girl)
                                "Swap to [Partner.name]":
                                    call primary_action_Swap (Girl)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump masturbation_cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump masturbation_cycle
                                "Never mind":
                                    jump masturbation_cycle

                        "Show her feet" if not ShowFeet and (Girl.pose == "doggy" or Girl.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (Girl.pose == "doggy" or Girl.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [Girl.name]":

                            if "unseen" in Girl.recent_history:
                                ch_p "Oh, yeah, take it off. . ."
                                jump Rogue_M_Interupted
                            else:
                                call Girl_Undress (Girl)
                        "Clean up [Girl.name] (locked)" if not Girl.spunk:
                            pass
                        "Clean up [Girl.name]" if Girl.spunk:
                            if "unseen" in Girl.recent_history:
                                ch_p "You've got a little something on you. . ."
                                jump Rogue_M_Interupted
                            else:
                                call Girl_Cleanup (Girl, "ask")
                        "Never mind":
                            jump masturbation_cycle

                "Back to Sex Menu" if multi_action and Girl.location == bg_current:
                    ch_p "Let's try something else."
                    call Rogue_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Rogue_M_Interupted
                "End Scene" if not multi_action or Girl.location != bg_current:
                    ch_p "Let's stop for now."
                    call Rogue_Pos_Reset
                    $ Line = 0
                    jump Rogue_M_Interupted


        call shift_focus (Girl)
        call Sex_Dialog (Girl, Partner)



        $ counter += 1
        $ round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus

        if Player.focus >= 100 or Girl.lust >= 100:

            if Player.focus >= 100:
                if "unseen" not in Girl.recent_history:

                    call Player_Cumming (Girl)
                    if "_angry" in Girl.recent_history:
                        call Rogue_Pos_Reset
                        return
                    $ Girl.change_stat("lust", 200, 5)
                    if 100 > Girl.lust >= 70 and Girl.session_orgasms < 2:
                        $ Girl.recent_history.append("unsatisfied")
                        $ Girl.daily_history.append("unsatisfied")
                    $ Line = "came"
                else:
                    "You grunt and try to hold it in."
                    $ Player.focus = 95
                    if Girl.location == bg_current:
                        jump Rogue_M_Interupted


            if Girl.lust >= 100:
                call Girl_Cumming (Girl)
                if Girl.location == bg_current:
                    jump Rogue_M_Interupted

            if Line == "came":
                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."
                    $ offhand_action = 0 if offhand_action == "jerking_off" else offhand_action


                if "unsatisfied" in Girl.recent_history:
                    "[Girl.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Let her keep going?"
                        "Yes, keep going for a bit.":
                            $ Line = "You let her get back into it"
                            jump masturbation_cycle
                        "No, I'm done.":
                            "You ask her to stop."
                            return
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        if "unseen" in Girl.recent_history:
            if round == 10:
                "It's getting a bit late, [Girl.name] will probably be wrapping up soon."
            elif round == 5:
                "She's definitely going to stop soon."
        else:
            if Girl.location == bg_current:
                call Escalation (Girl)

            if round == 10:
                ch_r "We might want to wrap this up, it's getting late."
                $ Girl.lust += 10
            elif round == 5:
                ch_r "Seriously, it'll be time to stop soon."
                $ Girl.lust += 25


    $ Girl.change_face("_bemused", 0)
    $ Line = 0
    if "unseen" not in Girl.recent_history:
        ch_r "Ok, [Girl.player_petname], that's enough of that for now."

label Rogue_M_Interupted:


    if "unseen" in Girl.recent_history:
        $ Girl.change_face("_surprised", 1)
        "[Girl.name] stops what she's doing with a start, eyes wide."
        call Rogue_First_Bottomless (1)
        $ Girl.change_face("_surprised", 1)


        if offhand_action == "jerking_off":
            call caught_masturbating_lines(Girl)
            $ Girl.eyes = "_down"
            call notices_penis_is_out_lines(Girl)
            menu:
                "Long enough, it was an excellent show.":
                    $ Girl.change_face("_sexy")
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_stat("obedience", 70, 2)

                    call masturbation_excellent_show_cock_out(Girl, primary_action)

                    if Girl.love >= 800 or Girl.obedience >= 500 or Girl.inhibition >= 500:
                        $ approval_bonus += 10
                        $ Girl.change_stat("lust", 90, 5)

                        call masturbation_excellent_show_cock_out_happy_lines(Girl, primary_action)
                "I. . . just got here?":

                    $ Girl.change_face("_angry")
                    $ Girl.change_stat("love", 70, 2)
                    $ Girl.change_stat("love", 90, 1)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("obedience", 70, 2)
                    "She looks pointedly at your cock,"

                    call masturbation_just_got_here_cock_out_lines(Girl, primary_action)

                    if Girl.love >= 800 or Girl.obedience >= 500 or Girl.inhibition >= 500:
                        $ approval_bonus += 10
                        $ Girl.change_stat("lust", 90, 5)
                        $ Girl.change_face("_bemused", 1)

                        call masturbation_just_got_here_cock_out_happy_lines(Girl, primary_action)
                    else:
                        $ approval_bonus -= 10
                        $ Girl.change_stat("lust", 200, -5)

            call Seen_First_Peen (Girl, Partner)

            Girl.voice "Hmm. . ."
        else:
            call caught_masturbating_lines(Girl)
            menu:
                extend ""
                "Long enough.":
                    $ Girl.change_face("_sexy", 1)
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_stat("obedience", 70, 2)

                    call masturbation_watching_for_long_enough_lines(Girl, primary_action)
                "I just got here.":
                    $ Girl.change_face("_bemused", 1)
                    $ Girl.change_stat("love", 70, 2)
                    $ Girl.change_stat("love", 90, 1)

                    call masturbation_just_got_here_lines(Girl, primary_action)

                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("obedience", 70, 2)

        $ Girl.drain_word("unseen",1,0)
        $ Girl.action_counter["masturbation"] += 1
        if round <= 10:
            call too_late_to_masturbate_lines(Girl)
            return
        $ action_context = "join"
        call Rogue_Masturbate
        "error: report this if you see it."
        return



    $ Girl.remaining_actions -= 1
    $ Girl.action_counter["masturbation"] += 1

    if Partner == EmmaX:
        call Partner_Like (Girl, 4)
    else:
        call Partner_Like (Girl, 3)
    call checkout
    if action_context == "shift":
        $ action_context = None
        return
    $ action_context = None

    if Girl.location != bg_current:
        return

    if round <= 10:
        call masturbation_worn_out_lines(Girl, primary_action)

        return
    $ Girl.change_face("_sexy", 1)
    if Girl.lust < 20:
        call end_of_masturbation_satisfied_lines(Girl, primary_action)
    else:
        call end_of_masturbation_lines(Girl, primary_action)

    menu:
        extend ""
        "Well, I have something you could take care of. . ." if Player.semen and Girl.remaining_actions:
            $ action_context = "shift"
            return
        "You could just keep going. . ." if Player.semen:
            $ Girl.change_face("_sly")
            if Girl.remaining_actions and round >= 10:
                call masturbation_keep_going_lines(Girl, primary_action)
                jump masturbation_cycle
            else:
                call masturbation_worn_out_lines(Girl, primary_action)
        "I'm good here. [[Stop]":
            if Girl.love < 800 and Girl.inhibition < 500 and Girl.obedience < 500:
                $ Girl.change_outfit(Changed=0)
            $ Girl.change_face("_normal")
            $ Girl.brows = "_confused"

            call masturbation_good_here_lines(Girl, primary_action)

            $ Girl.brows = "_normal"
        "You should probably stop for now." if Girl.lust > 30:
            $ Girl.change_face("_angry")

            call masturbation_stop_for_now_lines(Girl, primary_action)

    return
