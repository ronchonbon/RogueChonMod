label enter_main_sex_menu:
    if focused_Girl == EmmaX:
        if "classcaught" not in focused_Girl.history:
            ch_e "I can't imagine being a part of something so. . . tawdry."

            return

        if "threesome" not in focused_Girl.history and not AloneCheck(focused_Girl):
            call expression focused_Girl.tag + "_ThreeCheck"

        if taboo > 20 and "taboo" not in focused_Girl.history:
            call expression focused_Girl.tag + "_taboo_Talk"

            if bg_current == "bg_classroom" or bg_current in personal_rooms and AloneCheck(focused_Girl):
                ch_p "We could just lock the door, right?"
                ch_e "We certainly could. . ."
                "[focused_Girl.name] walks to the door and locks it behind her."

                $ Player.traits.append("locked")

                call taboo_level
            else:
                return

    $ action_context = None
    $ primary_action = None
    $ offhand_action = None
    $ girl_offhand_action = None

    call hide_girl(focused_Girl, hide_sprite = True)

    $ focused_Girl.arm_pose = 1

    call set_the_scene(1,0,0,0,1)

    if focused_Girl in [EmmaX, StormX]:
        if "detention" in focused_Girl.recent_history:
            $ temp_modifier = 20 if temp_modifier <= 20 else temp_modifier

    if not Player.semen:
        "You're a little out of juice at the moment, you might want to wait a bit."
    if Player.focus >= 95:
        "You're practically buzzing, the slightest breeze could set you off."
    if not focused_Girl.remaining_actions:
        "[focused_Girl.name]'s looking a bit tired out, maybe let her rest a bit."

    if "caught" in focused_Girl.recent_history or "_angry" in focused_Girl.recent_history:
        if focused_Girl.location == bg_current:
            call sex_menu_caught_or_angry_lines(focused_Girl)

        $ focused_Girl.change_outfit()
        $ focused_Girl.drain_word("caught",1,0)

        return

    if round < 5:
        call sex_menu_less_than_five_rounds_lines(focused_Girl)

        return

    call girl_sex_menu(focused_Girl)

    if _return:
        return

    if focused_Girl.location != bg_current:
        call set_the_scene
        call Trig_Reset

        return

    if not multi_action:
        $ focused_Girl.session_orgasms = 0

        call end_of_sex_menu_not_multiaction_lines(focused_Girl)
        call set_the_scene
        call Trig_Reset

        return

    call are_girls_angry

    return

label girl_sex_menu(Girl):
    if Girl == RogueX:
        $ main_line = "So what would you like to do?"
        $ fondle_line = "Well where exactly were you interested in touching, " + Girl.player_petname + "?"
        $ handjob_line = "What did you have in mind, " + Girl.player_petname + "?"
        $ show_line = "What sort of show were you expecting?"
    elif Girl == KittyX:
        $ main_line = "So what would you like to do?"
        $ fondle_line = "Um, what did you want to touch, " + Girl.player_petname + "?"
        $ handjob_line = Girl.Like + "what did you want me to do?"
        $ show_line = Girl.Like + "what did you want to see?"
    elif Girl == EmmaX:
        $ main_line = "So, what was it you hoped to do?"
        $ fondle_line = "Well? Where did you want to touch, " + Girl.player_petname + "?"
        $ handjob_line = "What did you want me to do?"
        $ show_line = "What did you want to see?"
    elif Girl == LauraX:
        $ main_line = "What did you want to do?"
        $ fondle_line = "Yeah? Like where?"
        $ handjob_line = "Oh? Like what?"
        $ show_line = "What kind of show are you thinking?"
    elif Girl == JeanX:
        $ main_line = "What did you want to do?"
        $ fondle_line = "Yeah? Like where?"
        $ handjob_line = "Oh? Like what?"
        $ show_line = "What kind of show are you thinking?"
    elif Girl == StormX:
        $ main_line = "So, what was it you hoped to do?"
        $ fondle_line = "What did you wish to touch, " + Girl.player_petname + "?"
        $ handjob_line = "What did you want me to do?"
        $ show_line = "What did you want to see?"
    elif Girl == JubesX:
        $ main_line = "So what did you wanna do?"
        $ fondle_line = "Where were you thinking?"
        $ handjob_line = "What were you thinking?"
        $ show_line = "What kind of show?"

    menu main_sex_menu:
        Girl.voice "[main_line]"
        "Do you want to make out?":
            if Girl.remaining_actions:
                $ primary_action = "kiss"

                jump action
            else:
                call out_of_action_lines(Girl)
        "Could I touch you?":
            if Girl.remaining_actions:
                if Girl in [EmmaX, StormX]:
                    $ Girl.change_face("_sly")
                else:
                    $ Girl.mouth = "_smile"

                menu:
                    Girl.voice "[fondle_line]"
                    "Could I give you a massage?":
                        call Massage (Girl)
                    "Your thighs?" if Girl.remaining_actions:
                        $ primary_action = "fondle_thighs"
                        jump action
                    "Your breasts?":
                        $ primary_action = "fondle_breasts"
                        jump action
                    "Suck your breasts?" if Girl.remaining_actions and Girl.action_counter["suck_breasts"]:
                        $ primary_action = "suck_breasts"
                        jump action
                    "Your pussy?" if Girl.remaining_actions:
                        $ primary_action = "fondle_pussy"
                        jump action
                    "Lick your pussy?" if Girl.remaining_actions and Girl.action_counter["eat_pussy"]:
                        $ primary_action = "lick_pussy"
                        jump action
                    "Your ass?":
                        $ primary_action = "fondle_ass"
                        jump action
                    "Never mind [[something else]":
                        jump main_sex_menu
            else:
                call out_of_action_lines(Girl)
        "Could you take care of something for me? [[Your dick, you mean your dick]" if Player.semen:
            if Girl.remaining_actions:
                menu:
                    Girl.voice "[handjob_line]"
                    "Could you give me a handjob?":
                        $ primary_action = "handjob"
                        jump action
                    "Could use your feet?":
                        $ primary_action = "footjob"
                        jump action
                    "Could you give me a titjob?":
                        $ primary_action = "titjob"
                        jump action
                    "Could you suck my cock?":
                        $ primary_action = "blowjob"
                        jump action
                    "Never mind [[something else]":
                        jump main_sex_menu
            elif not Girl.remaining_actions:
                call out_of_action_lines(Girl)
            else:
                "You really don't have it in you, maybe take a break."
        "Could you put on a show for me?":
            menu:
                Girl.voice "[show_line]"
                "Dance for me?":
                    if Girl.remaining_actions:
                        call Group_Strip(Girl)
                    else:
                        call out_of_action_lines(Girl)
                "Could you undress for me?":
                    call Girl_Undress(Girl)
                "You've got a little something. . . [[clean-up]" if Girl.spunk:
                    call sex_menu_cleanup_lines(Girl)
                    call Girl_Cleanup(Girl,"ask")
                "Could I watch you get yourself off? [[masturbate]":
                    if Girl.remaining_actions:
                        call expression Girl.tag + "_Masturbate"
                    else:
                        call out_of_action_lines(Girl)
                "Maybe make out with [RogueX.name]?" if Girl != RogueX and RogueX.location == bg_current:
                    call LesScene(RogueX)
                "Maybe make out with [KittyX.name]?" if Girl != KittyX and  KittyX.location == bg_current:
                    call LesScene(KittyX)
                "Maybe make out with [LauraX.name]?" if Girl != LauraX and LauraX.location == bg_current:
                    call LesScene(LauraX)
                "Maybe make out with [JeanX.name]?" if Girl != JeanX and JeanX.location == bg_current:
                    call LesScene(JeanX)
                "Maybe make out with [StormX.name]?" if Girl != StormX and StormX.location == bg_current:
                    call LesScene(StormX)
                "Maybe make out with [JubesX.name]?" if Girl != JubesX and JubesX.location == bg_current:
                    call LesScene(JubesX)
                "Never mind [[something else]":
                    jump main_sex_menu
        "Could we maybe?. . . [[fuck]":
            if Girl.remaining_actions:
                menu:
                    Girl.voice "[main_line]"
                    "Come over here, I've got something in mind. . .":
                        if Player.semen:
                            $ primary_action = "hotdog"
                            jump action
                        else:
                            "The spirit is apparently willing, but the flesh is spongy and bruised."
                    "Fuck your pussy.":
                        if Player.semen:
                            $ primary_action = "sex"
                            jump action
                        else:
                            "The spirit is apparently willing, but the flesh is spongy and bruised."
                    "Fuck your ass.":
                        if Player.semen:
                            $ primary_action = "anal"
                            jump action
                        else:
                            "The spirit is apparently willing, but the flesh is spongy and bruised."
                    "How about some toys? [[Pussy]":
                        $ primary_action = "dildo_pussy"
                        jump action
                    "How about some toys? [[Anal]":
                        $ primary_action = "dildo_ass"
                        jump action
                    "Never mind [[something else]":
                        jump main_sex_menu
            else:
                call out_of_action_lines(Girl)
        "Hey, do you want in on this? [[Threesome]" if not Partner:
            call Sex_Menu_Threesome(Girl)
        "Hey, [Partner.name]? [[Switch lead]" if Partner:
            call expression Partner.tag + "_SexAct" pass ("switch")
        "Cheat Menu" if config.developer:
            call cheat_menu(Girl)
            jump main_sex_menu
        "Never mind. [[exit]":
            if Girl.lust >= 50 or Girl.addiction >= 50:
                $ Girl.change_face("_sad")

                if Girl.remaining_actions and Girl.SEXP >= 15 and round > 20:
                    if "round2" not in Girl.recent_history:
                        call exit_sex_menu_experienced_first_round_lines(Girl)

                        $ Girl.change_stat("inhibition", 30, 2)
                        $ Girl.change_stat("inhibition", 50, 1)
                    elif Girl.addiction >= 50:
                        call exit_sex_menu_experienced_addicted_lines(Girl)
                    else:
                        call exit_sex_menu_experienced_lines(Girl)

                    menu:
                        extend ""
                        "Yeah, I'm done for now." if Player.semen and "round2" not in Girl.recent_history:
                            if "unsatisfied" in Girl.recent_history and not Girl.session_orgasms:
                                $ Girl.change_face("_angry")
                                $ Girl.eyes = "_side"
                                $ Girl.change_stat("love", 70, -2)
                                $ Girl.change_stat("love", 90, -4)
                                $ Girl.change_stat("obedience", 30, 2)
                                $ Girl.change_stat("obedience", 70, 1)

                                call exit_sex_menu_done_for_now_unsatisfied_lines(Girl)
                            else:
                                $ Girl.change_face("_bemused", 1)
                                $ Girl.change_stat("obedience", 50, 2)

                                call exit_sex_menu_done_for_now_satisfied_lines(Girl)
                        "I gave it a shot." if "round2" in Girl.recent_history:
                            if "unsatisfied" in Girl.recent_history and not Girl.session_orgasms:
                                $ Girl.change_face("_angry")
                                $ Girl.eyes = "_side"

                                call exit_sex_menu_gave_it_a_shot_unsatisfied_lines(Girl)
                            else:
                                $ Girl.change_face("_bemused", 1)

                                call exit_sex_menu_gave_it_a_shot_satisfied_lines(Girl)
                        "Hey, I did my part." if Girl.session_orgasms > 2:
                            $ Girl.change_face("_sly", 1)

                            call exit_sex_menu_did_my_part_lines(Girl)
                        "I'm tapped out for the moment, let's try again later." if not Player.semen:
                            $ Girl.change_face("_normal")

                            call exit_sex_menu_out_of_semen_lines(Girl)
                        "Ok, we can try something else." if multi_action and "round2" not in Girl.recent_history:
                            $ Girl.change_face("_smile")
                            $ Girl.change_stat("love", 70, 2)
                            $ Girl.change_stat("love", 90, 1)

                            call exit_sex_menu_less_than_two_rounds_lines(Girl)

                            $ Girl.recent_history.append("round2")
                            $ Girl.daily_history.append("round2")

                            jump main_sex_menu
                        "Again? Ok, fine." if multi_action and "round2" in Girl.recent_history:
                            $ Girl.change_face("_sly")

                            call exit_sex_menu_more_than_two_rounds_lines(Girl)
                            jump main_sex_menu
                else:
                    $ Girl.change_face("_bemused", 1)

                    call exit_sex_menu_girl_also_tired_lines(Girl)

                    $ Girl.change_stat("inhibition", 30, 2)
                    $ Girl.change_stat("inhibition", 50, 1)
            else:
                call generic_exit_sex_menu_lines(Girl)

            $ Girl.change_face()

            call Sex_Over

            return True

    $ Girl.change_face()

    call Sex_Over

    return False

label begging_menu(Girl, action):
    menu:
        extend ""
        "Sorry, never mind." if "no_" + action in Girl.daily_history:
            $ Girl.change_face("_bemused")

            call sorry_never_mind_lines(Girl)

            return
        "Maybe later?" if action in ["masturbation", "fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "fondle_ass", "handjob", "footjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"] and "no_" + action not in Girl.daily_history:
            if action == "masturbation":
                $ Girl.change_face("_sexy", 1)
            else:
                $ Girl.change_face("_sexy")

            if action == "fondle_breasts" and Girl not in [LauraX, JubesX]:
                "She re-adjusts her cleavage."

            call maybe_later_lines(Girl, action)

            if action in ["fondle_thighs", "fondle_breasts", "suck_breasts"]:
                $ Girl.change_stat("love", 80, 1)
                $ Girl.change_stat("inhibition", 30, 2)

                if action in ["fondle_breasts", "suck_breasts"]:
                    $ Girl.change_stat("love", 50, 1)
            elif action in ["masturbation", "fondle_pussy"]:
                $ Girl.change_stat("love", 80, 2)
                $ Girl.change_stat("inhibition", 70, 2)
            elif action in ["fondle_ass"]:
                $ Girl.change_stat("love", 80, 2)
                $ Girl.change_stat("inhibition", 50, 2)
            elif action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal"]:
                $ Girl.change_stat("love", 80, 2)
                $ Girl.change_stat("inhibition", 70, 2)
            elif action in ["hotdog"]:
                $ Girl.change_stat("love", 80, 1)
                $ Girl.change_stat("inhibition", 50, 1)

            if taboo:
                $ Girl.add_word(1, "no_taboo", "no_taboo")

            $ Girl.recent_history.append("no_" + action)
            $ Girl.daily_history.append("no_" + action)

            jump begging_rejected
        "You look like you could use it. . ." if action == "masturbation":
            if approval:
                $ Girl.change_face("_sexy")
                $ Girl.change_stat("obedience", 90, 2)
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("inhibition", 70, 3)
                $ Girl.change_stat("inhibition", 40, 2)

                call begging_lines(Girl, action)
                jump before_masturbation
        "Come on, please?" if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "blowjob"]:
            if approval:
                $ Girl.change_face("_sexy")

                if action == "fondle_thighs":
                    $ Girl.change_stat("obedience", 60, 1)
                    $ Girl.change_stat("obedience", 30, 2)
                    $ Girl.change_stat("inhibition", 50, 1)
                    $ Girl.change_stat("inhibition", 30, 2)
                elif action in ["fondle_breasts", "suck_breasts"]:
                    if Girl != LauraX:
                        $ Girl.change_stat("obedience", 90, 1)

                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("inhibition", 60, 3)
                    $ Girl.change_stat("inhibition", 30, 2)
                elif action in ["fondle_pussy", "blowjob"]:
                    $ Girl.change_stat("obedience", 90, 2)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("inhibition", 70, 3)
                    $ Girl.change_stat("inhibition", 40, 2)

                call begging_lines(Girl)
                jump before_action
            else:
                if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy"]:
                    $ Girl.change_face("_sexy")

                    call please_not_good_enough_lines(Girl)
                elif action in ["blowjob"]:
                    if approval_check(Girl, 1100, taboo_modifier = 3): # 110, 125, 140, taboo -120(230)             Handy instead?
                        $ Girl.change_stat("inhibition", 80, 1)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.change_face("_confused", 1)

                        if Girl.action_counter["handjob"]:
                            ch_r "Maybe you'd settle for a handy?"
                            ch_k "Maybe I could just use my hand?"
                            ch_e "I could just stroke you off, perhaps?"
                            ch_l "Couldn't I just use my hand again?{p}You seemed to like that."
                            ch_s "I could just stroke you off, perhaps?"
                        else:
                            ch_r "I could maybe. . . [[she makes a jerking motion with her hand]?"
                            ch_k "I could maybe. . . [[she makes a jerking motion with her hand]?"
                            ch_e "Would my hand be an adequate substitute?"
                            ch_l "I could maybe use my hand instead, how's that sound?"
                            ch_s "Would my hand be an adequate substitute?"

                        menu:
                            ch_r ""
                            "Sure, that's fine.":
                                $ Girl.change_stat("love", 80, 2)
                                $ Girl.change_stat("inhibition", 60, 1)
                                $ Girl.change_stat("obedience", 50, 1)

                                $ primary_action = "handjob"

                                jump before_action
                            "Nah, if it's not a BJ, forget it.":
                                $ Girl.change_stat("love", 200, -2)

                                ch_r "Ok, whatever."
                                ch_k "Ok, your loss."
                                ch_e "Pity."
                                ch_l "Fine, be that way."
                                $ JeanX.outfit["gloves"] = ""
                                ch_j "Too bad then."
                                ch_s "That is unfortunate."

                                $ Girl.change_stat("obedience", 70, 2)
        "I'm sure I can convince you later. . ." if action in ["eat_pussy", "eat_ass"] and "no_" + action not in Girl.daily_history:
            $ Girl.change_face("_sexy")

            call maybe_later_lines(Girl, action)

            $ Girl.change_stat("love", 80, 2)
            $ Girl.change_stat("inhibition", 70, 2)

            if taboo:
                $ Girl.add_word(1, "no_taboo", "no_taboo")

            $ Girl.recent_history.append("no_" + action)
            $ Girl.daily_history.append("no_" + action)

            jump begging_rejected
        "I think you'd really enjoy it. . ." if action in ["eat_pussy", "eat_ass"]:
            if approval:
                $ Girl.change_face("_sexy")
                $ Girl.change_stat("obedience", 90, 2)
                $ Girl.change_stat("obedience", 50, 2)

                call trying_to_convince_lines(Girl)

                $ Girl.change_stat("inhibition", 70, 3)
                $ Girl.change_stat("inhibition", 40, 2)

                jump before_action
            else:
                $ Girl.change_face("_sexy")

                call unconvinced_lines(Girl)
        "Just one good squeeze?" if action == "fondle_ass":
            if approval:
                $ Girl.change_face("_sexy")
                $ Girl.change_stat("obedience", 90, 1)
                $ Girl.change_stat("obedience", 50, 2)

                call begging_lines(Girl)

                $ Girl.change_stat("inhibition", 70, 1)
                $ Girl.change_stat("inhibition", 40, 2)

                jump before_action
            else:
                $ Girl.change_face("_sexy")

                call unconvinced_lines(Girl)
        "I'd really appreciate it. . ." if action in ["handjob"]:
            if approval:
                $ Girl.change_face("_sexy")
                $ Girl.change_stat("obedience", 90, 2)
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("inhibition", 70, 3)
                $ Girl.change_stat("inhibition", 40, 2)

                call begging_lines(Girl)
                jump before_action
        "I think this could be fun for both of us. . ." if action in ["titjob"]:
            if approval:
                $ Girl.change_face("_sexy")
                $ Girl.change_stat("obedience", 80, 2)
                $ Girl.change_stat("obedience", 40, 2)
                $ Girl.change_stat("inhibition", 70, 3)
                $ Girl.change_stat("inhibition", 40, 2)

                call trying_to_convince_lines(Girl, action)
                jump before_action
            else:
                $ approval = approval_check(Girl, 1100, taboo_modifier = 3) # 110, 125, 140, taboo -120(230)             Handy instead?

                if approval >= 2:
                    $ Girl.change_stat("inhibition", 80, 1)
                    $ Girl.change_stat("inhibition", 60, 3)
                    $ Girl.change_face("_confused", 1)

                    call maybe_blowjob_instead_lines(Girl, action)

                    if Girl.action_counter["blowjob"]:
                        ch_r "I could just. . . blow you instead?"
                        ch_e "You seemed to enjoy blowjobs, would that work instead?"
                        ch_s "You seemed to enjoy blowjobs, would that work instead?"
                    else:
                        ch_r "I could maybe. . . you know, [[she pushes her tongue against the side of her cheek]?"
                        ch_k "Could I[Girl.like]. . . blow you instead?"
                        ch_e "Would you perhaps prefer a blowjob?"
                        ch_l "I could maybe blow you?"
                        ch_j "What about a blowjob then?"
                        ch_s "Would you perhaps prefer a blowjob?"

                    menu:
                        extend ""
                        "Ok, get down there.":
                            $ Girl.change_stat("love", 80, 2)
                            $ Girl.change_stat("inhibition", 60, 1)
                            $ Girl.change_stat("obedience", 50, 1)

                            $ primary_action = "blowjob"

                            jump before_action
                        "Nah, it's all about dem titties.":
                            $ line = "no_BJ"
                if approval:
                    $ Girl.change_stat("inhibition", 80, 1)
                    $ Girl.change_stat("inhibition", 60, 3)
                    $ Girl.change_face("_confused", 1)

                    call maybe_handjob_instead_lines(Girl, action)

                    ch_r "Maybe you'd settle for a handy?"
                    ch_r "I could maybe. . . [[she makes a jerking motion with her hand]?"
                    ch_k "Maybe you'd[Girl.like]settle for a handy?"
                    ch_e "Perhaps a handjob?"
                    ch_l "I could give you a handy?"
                    ch_j "I could give you a hand job?"
                    ch_s "Perhaps a handjob?"

                    menu:
                        extend ""
                        "Sure, that's fine.":
                            $ Girl.change_stat("love", 80, 2)
                            $ Girl.change_stat("inhibition", 60, 1)
                            $ Girl.change_stat("obedience", 50, 1)

                            $ primary_action = "handjob"

                            jump before_action
                        "Seriously, titties." if line == "no_BJ":
                            $ line = 0
                        "Nah, it's all about dem titties." if line != "no_BJ":
                            pass

                $ Girl.change_stat("love", 200, -2)

                call alternative_rejected_lines(Girl, action)
                ch_r "Ok, whatever."
                ch_k "Nah."
                ch_e "Well, that's too bad."
                ch_l "Nah."
                ch_j "Well then too bad, I guess."
                ch_s "Well. That is unfortunate. . ."

                $ Girl.change_stat("obedience", 70, 2)
        "I think you'd like it. . ." if action in ["dildo_pussy", "dildo_ass"]:
            if approval:
                $ Girl.change_face("_sexy")
                $ Girl.change_stat("obedience", 90, 2)
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("inhibition", 70, 3)
                $ Girl.change_stat("inhibition", 40, 2)

                call trying_to_convince_lines(Girl, action)
                jump before_action
        "I think you'd enjoy it as much as I would. . ." if action in ["sex"]:
            if approval:
                $ Girl.change_face("_sexy")
                $ Girl.change_stat("obedience", 90, 2)
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("inhibition", 70, 3)
                $ Girl.change_stat("inhibition", 40, 2)

                call trying_to_convince_lines(Girl, action)
                jump before_action
        "I bet it would feel really good. . ." if action in ["anal"]:
            if approval:
                $ Girl.change_face("_sexy")
                $ Girl.change_stat("obedience", 90, 2)
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("inhibition", 70, 3)
                $ Girl.change_stat("inhibition", 40, 2)

                call trying_to_convince_lines(Girl, action)
                jump before_action
        "You might like it. . ." if action in ["hotdog"]:
            if approval:
                $ Girl.change_face("_sexy")
                $ Girl.change_stat("obedience", 60, 2)
                $ Girl.change_stat("inhibition", 50, 2)

                call trying_to_convince_lines(Girl, action)
                jump before_action
        "Just get at it already." if action == "masturbation":
            call forced_action(Girl, action)
        "[[Start caressing her thigh anyway]" if action == "fondle_thighs":
            call forced_action(Girl, action)
        "[[Grab her chest anyway]" if action == "fondle_breasts":
            call forced_action(Girl, action)
        "[[Start sucking anyway]" if action == "suck_breasts":
            call forced_action(Girl, action)
        "[[Start fondling anyway]" if action in ["fondle_pussy", "fondle_ass"]:
            call forced_action(Girl, action)
        "[[Get in there anyway]" if action == "eat_pussy":
            call forced_action(Girl, action)
        "[[Slide a finger in anyway]" if action == "finger_ass":
            call forced_action(Girl, action)
        "[[Start licking anyway]" if action in ["eat_pussy", "eat_ass"]:
            call forced_action(Girl, action)
        "Come on, get to work." if action in ["handjob", "footjob"]:                                               # Pressured into it
            call forced_action(Girl, action)
        "Come on, let me fuck those titties, [Girl.player_petname]" if action in ["titjob"]:
            $ Girl.name_check() #checks reaction to petname

            call forced_action(Girl, action)
        "Suck it, [Girl.player_petname]" if action in ["blowjob"]:                                               # Pressured into it
            $ Girl.name_check() #checks reaction to petname

            call forced_action(Girl, action)
        "[[Press it against her.]]" if action in ["dildo_pussy", "dildo_ass"]:
            call forced_action(Girl, action)
        "Bend over." if action in ["sex", "anal", "hotdog"]:
            call forced_action(Girl, action)

    return

label try_something_else_menu(Girl, action):
    menu:
        extend ""
        "How about a handy?" if action in ["footjob", "titjob", "blowjob", "sex", "anal", "hotdog"] and Girl.remaining_actions and multi_action:
            $ action_context = "shift"

            call after_action

            $ primary_action = "handjob"

            jump action
        "How about a footjob?" if action in ["handjob", "titjob", "blowjob", "sex", "anal", "hotdog"] and Girl.remaining_actions and multi_action:
            $ action_context = "shift"

            call after_action

            $ primary_action = "footjob"

            jump action
        "How about a titjob?" if action in ["handjob", "footjob", "blowjob", "sex", "anal", "hotdog"] and Girl.remaining_actions and multi_action:
            $ action_context = "shift"

            call after_action

            $ primary_action = "tiitjob"

            jump action
        "How about a BJ?" if action in ["handjob", "footjob", "titjob", "sex", "anal", "hotdog"] and Girl.remaining_actions and multi_action:
            if action != "anal":
                $ action_context = "shift"

                call after_action

                $ primary_action = "blowjob"

                jump action
            else:
                if Girl.action_counter["anal"] >= 5 and Girl.action_counter["blowjob"] >= 10 and Girl.SEXP >= 50:
                    $ action_context = "shift"

                    call after_action

                    $ primary_action = "blowjob"

                    jump action
                else:
                    call no_ass_to_mouth_lines(Girl)

                    $ action_context = "shift"

                    call after_action

                    $ primary_action = "handjob"

                    jump before_action
        "Finish up." if action in ["handjob", "footjob", "titjob", "blowjob", "sex", "anal", "hotdog"] and Player.focusing:
            "You release your concentration. . ."

            $ Player.focusing = 0
            $ Player.focus += 15

            jump action_cycle
        "No, get back down there." if action in ["handjob", "footjob", "titjob", "blowjob"]:
            if approval_check(Girl, 1200) or approval_check(Girl, 500, "O"):
                $ Girl.change_stat("love", 200, -5)
                $ Girl.change_stat("obedience", 50, 3)
                $ Girl.change_stat("obedience", 80, 2)

                "She grumbles but keeps going."
            else:
                $ Girl.change_face("_angry", 1)

                $ focused_Girl = Girl

                call reset_position

                "She scowls at you, drops your cock and pulls back."

                call this_is_boring_lines(Girl)

                $ Girl.change_stat("love", 50, -3, 1)
                $ Girl.change_stat("love", 80, -4, 1)
                $ Girl.change_stat("obedience", 30, -1, 1)
                $ Girl.change_stat("obedience", 50, -1, 1)
                $ Girl.add_word(1,"_angry","_angry")

                jump after_action
        "Finish up.":
            "You let go. . ."

            jump after_action
        "Let's try something else." if multi_action:
            $ action_context = "shift"

            jump after_action
        "No, this is fun.":
            if approval_check(Girl, 1200) or approval_check(Girl, 500, "O"):
                $ Girl.change_stat("love", 200, -5)
                $ Girl.change_stat("obedience", 50, 3)
                $ Girl.change_stat("obedience", 80, 2)

                "She grumbles but lets you keep going."
            else:
                $ Girl.change_face("_angry", 1)

                $ focused_Girl = Girl

                call reset_position

                "She scowls at you and pulls back."

                call this_is_boring_lines(Girl)

                $ Girl.change_stat("love", 50, -3, 1)
                $ Girl.change_stat("love", 80, -4, 1)
                $ Girl.change_stat("obedience", 30, -1, 1)
                $ Girl.change_stat("obedience", 50, -1, 1)
                $ Girl.add_word(1,"_angry","_angry")

                jump after_action

    return

label girl_unsatisfied_menu(Girl, action):
    if action in sex_actions:
        call not_ready_to_stop_narrations(Girl, action)

        menu:
            "Keep going?"
            "Yes, keep going for a bit." if Player.semen:
                $ line = "You get back into it"
            "No, I'm done." if Player.semen:
                "You pull back."

                jump after_action
            "No, I'm spent." if not Player.semen:
                "You pull back."

                jump after_action
    else:
        "[Girl.name] still seems a bit unsatisfied with the experience."

        "Finish her?"
        menu:
            extend ""
            "Yes, keep going for a bit.":
                $ line = "You get back into it"
            "No, I'm done.":
                "You pull back."

                jump after_action

    return

label kiss_menu:
    menu:
        "Keep going. . .":
            pass
        "Slap her ass":
            call Slap_Ass(focused_Girl)

            $ counter += 1
            $ round -= 1

            jump action_cycle
        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
            pass
        "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
            "You concentrate on not burning out too quickly."

            $ Player.focusing = 1
        "Release your focus." if Player.focusing:
            "You release your concentration. . ."

            $ Player.focusing = 0
        "Start jack'in it." if multi_action and offhand_action != "jerking_off":
            call jerking_off(focused_Girl)
        "Stop jack'in it." if multi_action and offhand_action == "jerking_off":
            "You stop jack'in it."

            $ offhand_action = None
        "Other options":
            menu:
                "Offhand action":
                    if focused_Girl.remaining_actions and multi_action:
                        call Offhand_Set

                        if offhand_action:
                             $ focused_Girl.remaining_actions -= 1
                    else:
                        call tired_lines(focused_Girl, primary_action)
                "Shift primary action":
                    if focused_Girl.remaining_actions and multi_action:
                        menu:
                            "Move a hand to her breasts. . ." if focused_Girl.action_counter["kiss"] >= 1:
                                $ action_context = "auto"

                                call after_action

                                $ primary_action = "fondle_breasts"
                            "Move a hand to her thighs. . ." if focused_Girl.action_counter["kiss"] >= 1:
                                $ action_context = "auto"

                                call after_action

                                $ primary_action = "fondle_thighs"
                            "Never Mind":
                                jump action_cycle

                        $ Girl = focused_Girl

                        jump action
                    else:
                        call tired_lines(focused_Girl, primary_action)
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
                            call shift_focus(Partner)

                            jump action_cycle
                        "Clean up Partner":
                            call Girl_Cleanup(Partner,"ask")

                            jump action_cycle
                        "Never mind":
                            jump action_cycle
                "Undress [focused_Girl.name]":
                    call Girl_Undress(focused_Girl)
                "Clean up [Girl.name] (locked)" if not focused_Girl.spunk:
                    pass
                "Clean up [focused_Girl.name]" if focused_Girl.spunk:
                    call Girl_Cleanup(focused_Girl,"ask")
                "Never mind":
                    jump action_cycle
        "Back to Sex Menu" if multi_action and focused_Girl.action_counter["kiss"] >= 5:
            ch_p "Let's try something else."

            $ action_context = "shift"

            call after_action
            jump main_sex_menu
        "End scene":
            ch_p "Let's stop for now."

            jump after_action

    jump action_menu_return

label fondle_menu:
    menu:
        "Keep going. . .":
            pass
        "I want to stick a finger in. . ." if primary_action == "fondle_pussy" and action_speed != 2:
            if focused_Girl.action_counter["finger_pussy"]:
                $ action_speed = 2
            else:
                menu:
                    "Ask her first":
                        $ action_context = "shift"
                    "Don't ask first [[just stick it in]":
                        $ action_context = "auto"

                $ Girl = focused_Girl
                $ primary_action = "finger_pussy"

                jump action
        "Pull back a bit. . ." if primary_action == "fondle_pussy" and action_speed != 2:
            $ action_speed = 0
        "Slap her ass":
            call Slap_Ass(focused_Girl)

            $ counter += 1
            $ round -= 1

            jump action_cycle
        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
            pass
        "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
            "You concentrate on not burning out too quickly."

            $ Player.focusing = 1
        "Release your focus." if Player.focusing:
            "You release your concentration. . ."

            $ Player.focusing = 0
        "View":
            call shift_view(focused_Girl, "menu")
            jump action_cycle
        "Other options":
            menu:
                "Offhand action":
                    if focused_Girl.remaining_actions and multi_action:
                        call Offhand_Set

                        if offhand_action:
                            $ focused_Girl.remaining_actions -= 1
                    else:
                        call tired_lines(focused_Girl, primary_action)
                "Shift primary action":
                    if focused_Girl.remaining_actions and multi_action:
                        menu:
                            "Can I go a little deeper?" if primary_action == "fondle_thighs":
                                $ action_context = "shift"
                                $ primary_action = "fondle_pussy"
                            "Shift your hands a bit higher without asking" if primary_action == "fondle_thighs":
                                $ action_context = "auto"
                                $ primary_action = "fondle_pussy"
                            "Ask to suck on them." if primary_action == "fondle_breasts":
                                $ action_context = "shift"
                                $ primary_action = "suck_breasts"
                            "Just suck on them without asking." if primary_action == "fondle_breasts":
                                $ action_context = "auto"
                                $ primary_action = "suck_breasts"
                            "Pull back to fondling." if primary_action =="suck_breasts":
                                $ action_context = "pullback"
                                $ primary_action = "fondle_breasts"
                            "I want to lick your pussy." if primary_action in ["fondle_pussy", "finger_pussy"]:
                                $ action_context = "shift"
                                $ primary_action = "eat_pussy"
                            "Just start licking" if primary_action in ["fondle_pussy", "finger_pussy"]:
                                $ action_context = "auto"
                                $ primary_action = "eat_pussy"
                            "Pull back to the thighs" if primary_action in ["fondle_pussy"]:
                                $ action_context = "pullback"
                                $ primary_action = "fondle_thighs"
                            "I want to stick a dildo in." if primary_action in ["fondle_pussy", "finger_pussy", "eat_pussy"]:
                                $ action_context = "shift"
                                $ primary_action = "dildo_pussy"
                            "Pull out and start rubbing again." if primary_action in ["finger_pussy"]:
                                $ action_context = "pullback"
                                $ primary_action = "fondle_pussy"
                            "I want to stick a finger in." if primary_action in ["fondle_ass", "eat_ass"]:
                                $ action_context = "shift"
                                $ primary_action = "finger_ass"
                            "Just stick a finger in without asking." if primary_action in ["fondle_ass", "eat_ass"]:
                                $ action_context = "auto"
                                $ primary_action = "finger_ass"
                            "I want to lick your asshole." if primary_action in ["fondle_ass", "finger_ass"]:
                                $ action_context = "shift"
                                $ primary_action = "eat_ass"
                            "Just start licking." if primary_action in ["fondle_ass", "finger_ass"]:
                                $ action_context = "auto"
                                $ primary_action = "eat_ass"
                            "I want to stick a dildo in." if primary_action in ["fondle_ass", "finger_ass", "eat_ass"]:
                                $ action_context = "shift"
                                $ primary_action = "dildo_ass"
                            "Pull out and start rubbing again." if primary_action in ["fondle_ass"]:
                                $ action_context = "pullback"
                                $ primary_action = "fondle_ass"
                            "Switch to fondling." if primary_action =="eat_ass":
                                $ action_context = "pullback"
                                $ primary_action = "fondle_ass"
                            "Never Mind":
                                jump action_cycle

                        $ Girl = focused_Girl

                        jump action
                    else:
                        call tired_lines(focused_Girl, primary_action)
                "Shift your focus" if offhand_action:
                    $ action_context = "shift_focus"

                    call after_action
                    call Offhand_Set
                "Shift your focus (locked)" if not offhand_action:
                    pass
                "Threesome actions (locked)" if not Partner:
                    pass
                "Threesome actions" if Partner:
                    menu:
                        "Ask [focused_Girl.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                            call Les_Change
                        "Ask [focused_Girl.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                            pass
                        "Ask [Partner.name] to do something else":
                            call Three_Change
                        "Don't stop what you're doing. . . (locked)" if not position_change_timer or not second_girl_primary_action:
                            $ position_change_timer = 0
                        "Don't stop what you're doing. . ." if position_change_timer and second_girl_primary_action:
                            $ position_change_timer = 0
                        "Swap to [Partner.name]":
                            call primary_action_Swap
                        "Undress [Partner.name]":
                            call Girl_Undress(Partner)
                            jump action_cycle
                        "Clean up [Partner.name] (locked)" if not Partner.spunk:
                            pass
                        "Clean up [Partner.name]" if Partner.spunk:
                            call Girl_Cleanup(Partner,"ask")
                            jump action_cycle
                        "Never mind":
                            jump action_cycle
                "Show her feet" if not show_feet and focused_Girl.pose in ["doggy", "sex"]:
                    $ show_feet = 1
                "Hide her feet" if show_feet and focused_Girl.pose in ["doggy", "sex"]:
                    $ show_feet = 0
                "Undress [focused_Girl.name]":
                    call Girl_Undress
                "Clean up [focused_Girl.name] (locked)" if not focused_Girl.spunk:
                    pass
                "Clean up [focused_Girl.name]" if focused_Girl.spunk:
                    call Girl_Cleanup(focused_Girl,"ask")
                "Never mind":
                    jump action_cycle
        "Back to Sex Menu" if multi_action:
            ch_p "Let's try something else."

            $ focused_Girl = Girl

            call reset_position

            $ action_context = "shift"

            call after_action
            jump main_sex_menu
        "End Scene" if not multi_action:
            ch_p "Let's stop for now."

            $ focused_Girl = Girl

            call reset_position
            jump after_action

    jump action_menu_return

label handjob_menu:
    menu:
        "Keep going. . ." if action_speed:
            pass
        "Start moving? . ." if primary_action in ["handjob", "footjob", "titjob"] and not action_speed:
            $ action_speed = 1
        "Speed up. . ." if primary_action in ["handjob", "footjob", "titjob"] and action_speed < 2:
            $ action_speed = 2

            "You ask her to up the pace a bit."
        "Speed up. . . (locked)" if primary_action in ["handjob", "footjob", "titjob"] and action_speed >= 2:
            pass
        "Slow Down. . ." if primary_action in ["handjob", "footjob", "titjob"] and action_speed:
            $ action_speed -= 1

            "You ask her to slow it down a bit."
        "Slow Down. . . (locked)" if primary_action in ["handjob", "footjob", "titjob"] and not action_speed:
            pass
        "Lick it. . ." if primary_action == "blowjob" and action_speed != 1:
            $ action_speed = 1
        "Lick it. . . (locked)" if primary_action == "blowjob" and action_speed == 1:
            pass
        "Just the head. . ." if primary_action == "blowjob" and action_speed != 2:
            $ action_speed = 2
        "Just the head. . . (locked)" if primary_action == "blowjob" and action_speed == 2:
            pass
        "Suck on it." if primary_action == "blowjob" and action_speed != 3:
            $ action_speed = 3

            if offhand_action == "jerking_off":
                "She dips her head a bit lower, and you move your hand out of the way."
        "Suck on it. (locked)" if primary_action == "blowjob" and action_speed == 3:
            pass
        "Take it deeper." if primary_action == "blowjob" and action_speed != 4:
            if "pushed" not in focused_Girl.recent_history and focused_Girl.action_counter["blowjob"] < 5:
                $ focused_Girl.change_stat("love", 80, -(20 - 2*focused_Girl.action_counter["blowjob"]))
                $ focused_Girl.change_stat("obedience", 80, 30 - 3*focused_Girl.action_counter["blowjob"])
                $ focused_Girl.recent_history.append("pushed")

            if offhand_action == "jerking_off" and action_speed != 3:
                "She takes it to the root, and you move your hand out of the way."

            $ action_speed = 4
        "Take it deeper. (locked)" if primary_action == "blowjob" and action_speed == 4:
            pass
        "Set your own pace. . ." if primary_action == "blowjob":
            "[focused_Girl.name] hums contentedly."

            if "setpace" not in focused_Girl.recent_history:
                $ focused_Girl.change_stat("love", 80, 2)

            $ D20 = renpy.random.randint(1, 20)

            if focused_Girl.action_counter["blowjob"] < 5:
                $ D20 -= 10
            elif focused_Girl.action_counter["blowjob"] < 10:
                $ D20 -= 5

            if D20 > 15:
                $ action_speed = 4

                if "setpace" not in focused_Girl.recent_history:
                    $ focused_Girl.change_stat("inhibition", 80, 3)
            elif D20 > 10:
                $ action_speed = 3
            elif D20 > 5:
                $ action_speed = 2
            else:
                $ action_speed = 1

            $ focused_Girl.recent_history.append("setpace")
        "Slap her ass. . ." if primary_action in ["dildo_pussy", "dildo_ass"]:
            call Slap_Ass(focused_Girl)

            $ counter += 1
            $ round -= 1

            jump action_cycle
        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
            pass
        "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
            "You concentrate on not burning out too quickly."

            $ Player.focusing = 1
        "Release your focus." if Player.focusing:
            "You release your concentration. . ."

            $ Player.focusing = 0
        "Turn her around." if primary_action == "footjob":
            $ focused_Girl.pose = "doggy" if focused_Girl.pose != "doggy" else "sex"

            "You turn her around. . ."

            jump action_cycle
        "View" if primary_action in ["dildo_pussy", "dildo_ass"]:
            call shift_view(focused_Girl, "menu")
            jump action_cycle
        "Other options":
                menu:
                    "I also want to fondle her breasts." if offhand_action != "fondle_breasts":
                        if focused_Girl.remaining_actions and multi_action:
                            $ offhand_action = "fondle_breasts"

                            "You start to fondle her breasts."

                            $ focused_Girl.remaining_actions -= 1
                        else:
                            call tired_lines(focused_Girl, primary_action)
                    "Offhand action" if primary_action in ["footjob", "dildo_pussy", "dildo_ass"]:
                        if focused_Girl.remaining_actions and multi_action:
                            call Offhand_Set

                            if offhand_action:
                                $ focused_Girl.remaining_actions -= 1
                        else:
                            call tired_lines(focused_Girl, primary_action)
                    "Shift primary action":
                        if focused_Girl.remaining_actions and multi_action:
                            menu:
                                "How about a handy?" if primary_action in ["footjob", "titjob", "blowjob"]:
                                    if focused_Girl.remaining_actions and multi_action:
                                        $ action_context = "shift"

                                        call after_action

                                        $ primary_action = "handjob"
                                    else:
                                        call tired_lines(focused_Girl, primary_action)
                                "How about a footjob?" if primary_action in ["handjob", "titjob", "blowjob"]:
                                    if focused_Girl.remaining_actions and multi_action:
                                        $ action_context = "shift"

                                        call after_action

                                        $ primary_action = "footjob"
                                    else:
                                        call tired_lines(focused_Girl, primary_action)
                                "How about a titjob?" if primary_action in ["handjob", "footjob", "blowjob"]:
                                    if focused_Girl.remaining_actions and multi_action:
                                        $ action_context = "shift"

                                        call after_action

                                        $ primary_action = "titjob"
                                    else:
                                        call tired_lines(focused_Girl, primary_action)
                                "How about a blowjob?" if primary_action in ["handjob", "footjob", "titjob"]:
                                    if focused_Girl.remaining_actions and multi_action:
                                        $ action_context = "shift"

                                        call after_action

                                        $ primary_action = "blowjob"
                                    else:
                                        call tired_lines(focused_Girl, primary_action)
                                "I want to stick a finger in her ass." if primary_action == "dildo_pussy":
                                    if focused_Girl.remaining_actions and multi_action:
                                        $ action_context = "shift"

                                        call after_action

                                        $ primary_action = "finger_ass"
                                    else:
                                        call tired_lines(focused_Girl, primary_action)
                                "Just stick a finger in her ass without asking." if primary_action == "dildo_pussy":
                                    if focused_Girl.remaining_actions and multi_action:
                                        $ action_context = "auto"

                                        call after_action

                                        $ primary_action = "finger_ass"
                                    else:
                                        call tired_lines(focused_Girl, primary_action)
                                "I want to shift the dildo to her ass." if primary_action == "dildo_pussy":
                                    if focused_Girl.remaining_actions and multi_action:
                                        $ action_context = "shift"

                                        call after_action

                                        $ primary_action = "dildo_ass"
                                    else:
                                        call tired_lines(focused_Girl, primary_action)
                                "I want to stick a finger in her pussy." if primary_action == "dildo_ass":
                                    if focused_Girl.remaining_actions and multi_action:
                                        $ action_context = "shift"

                                        call after_action

                                        $ primary_action = "finger_pussy"
                                    else:
                                        call tired_lines(focused_Girl, primary_action)
                                "Just stick a finger in her pussy without asking." if primary_action == "dildo_ass":
                                    if focused_Girl.remaining_actions and multi_action:
                                        $ action_context = "auto"

                                        call after_action

                                        $ primary_action = "finger_pussy"
                                    else:
                                        call tired_lines(focused_Girl, primary_action)
                                "I want to shift the dildo to her pussy." if primary_action == "dildo_ass":
                                    if focused_Girl.remaining_actions and multi_action:
                                        $ action_context = "shift"

                                        call after_action

                                        $ primary_action = "dildo_pussy"
                                    else:
                                        call tired_lines(focused_Girl, primary_action)
                                "Never Mind":
                                    jump action_cycle

                            $ Girl = focused_Girl

                            jump action
                        else:
                            call tired_lines(focused_Girl, primary_action)
                    "Shift your focus." if primary_action in ["dildo_pussy", "dildo_ass"] and offhand_action:
                        $ action_context = "shift_focus"

                        call after_action
                        call Offhand_Set
                    "Shift your focus. (locked)" if primary_action in ["dildo_pussy", "dildo_ass"] and not offhand_action:
                        pass
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
                            "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                pass
                            "Clean up [Partner.name]" if Partner.spunk:
                                call Girl_Cleanup(Partner,"ask")
                                jump action_cycle
                            "Never mind":
                                jump action_cycle
                    "Undress [focused_Girl.name]":
                        call Girl_Undress(focused_Girl)
                    "Clean up [focused_Girl.name] (locked)" if not focused_Girl.spunk:
                        pass
                    "Clean up [focused_Girl.name]" if focused_Girl.spunk:
                        call Girl_Cleanup(RogueX,"ask")
                    "Never mind":
                        jump action_cycle
        "Back to Sex Menu" if multi_action:
            ch_p "Let's try something else."

            $ focused_Girl = Girl

            call reset_position

            $ action_context = "shift"

            call after_action
            jump main_sex_menu
        "End Scene" if not multi_action:
            ch_p "Let's stop for now."

            $ focused_Girl = Girl

            call reset_position
            jump after_action

    jump action_menu_return

label sex_menu:
    menu:
        "Keep going. . ." if action_speed:
            pass
        "Keep going. . . (locked)" if not action_speed:
            pass
        "Start moving? . ." if not action_speed:
            $ action_speed = 1
        "Speed up. . ." if 0 < action_speed < 3:
            $ action_speed += 1

            "You ask her to up the pace a bit."
        "Speed up. . . (locked)" if action_speed >= 3:
            pass
        "Slow Down. . ." if action_speed:
            $ action_speed -= 1

            "You ask her to slow it down a bit."
        "Slow Down. . . (locked)" if not action_speed:
            pass
        "Slap her ass":
            call Slap_Ass(focused_Girl)

            $ counter += 1
            $ round -= 1

            jump action_cycle
        "Turn her around":
            $ focused_Girl.pose = "doggy" if focused_Girl.pose != "doggy" else "sex"

            "You turn her around. . ."

            jump action_cycle
        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
            pass
        "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
            "You concentrate on not burning out too quickly."

            $ Player.focusing = 1
        "Release your focus." if Player.focusing:
            "You release your concentration. . ."

            $ Player.focusing = 0
        "Other options":
            menu:
                "Offhand action":
                    if focused_Girl.remaining_actions and multi_action:
                        call Offhand_Set

                        if offhand_action:
                            $ focused_Girl.remaining_actions -= 1
                    else:
                        call Sex_Basic_Dialog(focused_Girl,"tired")
                "Shift primary action":
                    if focused_Girl.remaining_actions and multi_action:
                        menu:
                            "How about sex?" if primary_action != "sex":
                                $ action_context = "shift"

                                call after_action

                                $ primary_action = "sex"
                            "Just stick it in her pussy [[without asking]." if primary_action != "sex":
                                $ action_context = "auto"

                                call after_action

                                $ primary_action = "sex"
                            "How about anal?" if primary_action != "anal":
                                $ action_context = "shift"

                                call after_action

                                $ primary_action = "anal"
                            "Just stick it in her ass [[without asking]." if primary_action != "anal":
                                $ action_context = "auto"

                                call after_action

                                $ primary_action = "anal"
                            "Pull back to hotdog her." if primary_action != "hotdog":
                                $ action_context = "pullback"

                                call after_action

                                $ primary_action = "hotdog"
                            "Never Mind":
                                jump action_cycle

                        $ Girl = focused_Girl

                        jump action
                    else:
                        call tired_lines(focused_Girl, primary_action)
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
                        "Clean up [Partner.name] (locked)" if not Partner.spunk:
                            pass
                        "Clean up [Partner.name]" if Partner.spunk:
                            call Girl_Cleanup(Partner,"ask")
                            jump action_cycle
                        "Never mind":
                            jump action_cycle
                "Just take a look at her.":
                    $ Player.cock_position = 0

                    $ action_speed = 0
                "Show her feet" if not show_feet and focused_Girl.pose in ["doggy", "sex"]:
                    $ show_feet = 1
                "Hide her feet" if show_feet and focused_Girl.pose in ["doggy", "sex"]:
                    $ show_feet = 0
                "Undress [focused_Girl.name]":
                    call Girl_Undress(focused_Girl)
                "Clean up [focused_Girl.name] (locked)" if not focused_Girl.spunk:
                    pass
                "Clean up [focused_Girl.name]" if focused_Girl.spunk:
                    call Girl_Cleanup(focused_Girl,"ask")
                "Never mind":
                    jump action_cycle
        "Back to Sex Menu" if multi_action:
            ch_p "Let's try something else."

            $ focused_Girl = Girl

            call reset_position

            $ action_context = "shift"

            call after_action
            jump main_sex_menu
        "End Scene" if not multi_action:
            ch_p "Let's stop for now."

            $ focused_Girl = Girl

            call reset_position
            jump after_action

    jump action_menu_return

label what_do_you_think_youre_doing_menu(Girl, action):
    menu:
        extend ""
        "Sorry, sorry! Never mind.":
            if approval:
                $ Girl.change_face("_sexy", 1)
                $ Girl.change_stat("obedience", 70, 3)
                $ Girl.change_stat("inhibition", 50, 3)
                $ Girl.change_stat("inhibition", 70, 1)

                call since_you_are_so_nice_lines(Girl)

                jump before_action

            "You pull back before you really get it in."

            $ Girl.change_face("_bemused", 1)

            call pull_back_before_get_in_lines(Girl)
        "Just playing with my favorite toys." if action in dildo_actions:
            $ Girl.change_stat("love", 80, -10, 1)
            $ Girl.change_stat("love", 200, -10)

            "You press it inside some more."

            $ Girl.change_stat("obedience", 70, 3)
            $ Girl.change_stat("inhibition", 50, 3)

            if not approval_check(Girl, 700, "O", taboo_modifier=1): #checks if obedience is 700+
                $ Girl.change_face("_angry")

                call were_done_here_lines(Girl)

                $ Girl.change_stat("love", 50, -10, 1)
                $ Girl.change_stat("obedience", 50, 3)

                $ renpy.pop_call()

                if action_context:
                    $ renpy.pop_call()

                $ focused_Girl = Girl

                call reset_position

                $ Girl.recent_history.append("_angry")
                $ Girl.daily_history.append("_angry")
            else:
                $ Girl.change_face("_sad")

                call knows_her_place_lines(Girl)
                jump before_action
        "Just fucking." if action in ["sex", "anal"]:
            $ Girl.change_stat("love", 80, -10, 1)
            $ Girl.change_stat("love", 200, -10)

            if action == "sex":
                "You press inside some more."
            elif action == "anal":
                "You press into her."

            $ Girl.change_stat("obedience", 70, 3)
            $ Girl.change_stat("inhibition", 50, 3)

            if not approval_check(Girl, 700, "O", taboo_modifier=1):   #checks if obedience is 700+
                $ Girl.change_face("_angry")

                call were_done_here_lines(Girl)

                $ Girl.change_stat("love", 50, -10, 1)
                $ Girl.change_stat("obedience", 50, 3)

                $ renpy.pop_call()

                if action_context:
                    $ renpy.pop_call()

                $ focused_Girl = Girl

                call reset_position

                $ Girl.recent_history.append("_angry")
                $ Girl.daily_history.append("_angry")
            else:
                $ Girl.change_face("_sad")

                call knows_her_place_lines(Girl)
                jump before_action
        "You'll see." if action == "hotdog":
            $ Girl.change_stat("love", 80, -10, 1)
            $ Girl.change_stat("love", 200, -8)

            "You grind against her asscrack."

            $ Girl.change_stat("obedience", 70, 3)
            $ Girl.change_stat("inhibition", 50, 3)

            if not approval_check(Girl, 500, "O", taboo_modifier=1): #checks if obedience is 700+
                $ Girl.change_face("_angry")

                call were_done_here_lines(Girl)

                $ Girl.change_stat("love", 50, -10, 1)
                $ Girl.change_stat("obedience", 50, 3)

                $ renpy.pop_call()

                if action_context:
                    $ renpy.pop_call()

                $ focused_Girl = Girl

                call reset_position

                $ Girl.recent_history.append("_angry")
                $ Girl.daily_history.append("_angry")
            else:
                $ Girl.change_face("_sad")

                call knows_her_place_lines(Girl)

                jump before_action
