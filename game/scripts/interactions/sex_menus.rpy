label enter_main_sex_menu(Girl):
    call stop_all_actions
    call shift_focus(Girl)

    if Girl == EmmaX:
        if "classcaught" not in Girl.history:
            ch_e "I can't imagine being a part of something so. . . tawdry."

            return

        if "threesome" not in Girl.history and not AloneCheck(Girl):
            call expression Girl.tag + "_ThreeCheck"

        if taboo > 20 and "taboo" not in Girl.history:
            call expression Girl.tag + "_taboo_Talk"

            if Player.location == "bg_classroom" or Player.location in bedrooms and AloneCheck(Girl):
                ch_p "We could just lock the door, right?"
                ch_e "We certainly could. . ."
                "[Girl.name] walks to the door and locks it behind her."

                $ Player.traits.append("locked")

                call set_Character_taboos
            else:
                return

    $ Girl.arm_pose = 1

    call set_the_scene

    if Girl in [EmmaX, StormX]:
        if "detention" in Girl.recent_history:
            $ temp_modifier = 20 if temp_modifier <= 20 else temp_modifier

    if not Player.semen:
        "You're a little out of juice at the moment, you might want to wait a bit."

    if Player.focus >= 95:
        "You're practically buzzing, the slightest breeze could set you off."

    if not Girl.remaining_actions:
        "[Girl.name]'s looking a bit tired out, maybe let her rest a bit."

    if "caught" in Girl.recent_history or "angry" in Girl.recent_history:
        if Girl.location == Player.location:
            call sex_menu_caught_or_angry_lines(Girl)

        $ Girl.change_Outfit()
        $ Girl.drain_word("caught", 1, 0)

        return

    if round < 5:
        call sex_menu_less_than_five_rounds_lines(Girl)

        return

    call girl_sex_menu(Girl)

    if Girl.location != Player.location:
        call set_the_scene
        call stop_all_actions

        return

    if not multi_action:
        $ Girl.session_orgasms = 0

        call end_of_sex_menu_not_multiaction_lines(Girl)
        call set_the_scene
        call stop_all_actions

        return

    call are_girls_angry

    return

label girl_sex_menu(Girl):
    call shift_focus(Girl)

    $ having_sex = True

    while having_sex:
        if Player.focused_Girl == RogueX:
            $ main_line = "So what would you like to do?"
            $ fondle_line = "Well where exactly were you interested in touching, " + Player.focused_Girl.player_petname + "_?"
            $ handjob_line = "What did you have in mind, " + Player.focused_Girl.player_petname + "_?"
            $ show_line = "What sort of show were you expecting?"
        elif Player.focused_Girl == KittyX:
            $ main_line = "So what would you like to do?"
            $ fondle_line = "Um, what did you want to touch, " + Player.focused_Girl.player_petname + "_?"
            $ handjob_line = Player.focused_Girl.Like + "_what did you want me to do?"
            $ show_line = Player.focused_Girl.Like + "_what did you want to see?"
        elif Player.focused_Girl == EmmaX:
            $ main_line = "So, what was it you hoped to do?"
            $ fondle_line = "Well? Where did you want to touch, " + Player.focused_Girl.player_petname + "_?"
            $ handjob_line = "What did you want me to do?"
            $ show_line = "What did you want to see?"
        elif Player.focused_Girl == LauraX:
            $ main_line = "What did you want to do?"
            $ fondle_line = "Yeah? Like where?"
            $ handjob_line = "Oh? Like what?"
            $ show_line = "What kind of show are you thinking?"
        elif Player.focused_Girl == JeanX:
            $ main_line = "What did you want to do?"
            $ fondle_line = "Yeah? Like where?"
            $ handjob_line = "Oh? Like what?"
            $ show_line = "What kind of show are you thinking?"
        elif Player.focused_Girl == StormX:
            $ main_line = "So, what was it you hoped to do?"
            $ fondle_line = "What did you wish to touch, " + Player.focused_Girl.player_petname + "_?"
            $ handjob_line = "What did you want me to do?"
            $ show_line = "What did you want to see?"
        elif Player.focused_Girl == JubesX:
            $ main_line = "So what did you wanna do?"
            $ fondle_line = "Where were you thinking?"
            $ handjob_line = "What were you thinking?"
            $ show_line = "What kind of show?"

        menu:
            Player.focused_Girl.voice "[main_line]"
            "Do you want to make out?":
                if Player.focused_Girl.remaining_actions:
                    call start_action(Player.focused_Girl, "kiss")
                else:
                    call out_of_action_lines(Player.focused_Girl)

                    $ having_sex = False
            "Could I touch you?":
                if Player.focused_Girl.remaining_actions:
                    if Player.focused_Girl in [EmmaX, StormX]:
                        $ Player.focused_Girl.change_face("sly")
                    else:
                        $ Player.focused_Girl.mouth = "smile"

                    menu:
                        Player.focused_Girl.voice "[fondle_line]"
                        "Could I give you a massage?":
                            call Massage (Player.focused_Girl)
                        "Your thighs?" if Player.focused_Girl.remaining_actions:
                            call start_action(Player.focused_Girl, "fondle_thighs")
                        "Your breasts?":
                            call start_action(Player.focused_Girl, "fondle_breasts")
                        "Suck your nipples?" if Player.focused_Girl.remaining_actions and Player.focused_Girl.action_counter["suck_breasts"]:
                            call start_action(Player.focused_Girl, "suck_breasts")
                        "Your pussy?" if Player.focused_Girl.remaining_actions:
                            call start_action(Player.focused_Girl, "fondle_pussy")
                        "Eat your pussy?" if Player.focused_Girl.remaining_actions and Player.focused_Girl.action_counter["eat_pussy"]:
                            call start_action(Player.focused_Girl, "eat_pussy")
                        "Your ass?":
                            call start_action(Player.focused_Girl, "fondle_ass")
                        "Eat your ass?" if Player.focused_Girl.remaining_actions and Player.focused_Girl.action_counter["eat_ass"]:
                            call start_action(Player.focused_Girl, "eat_ass")
                        "Never mind [[something else]":
                            pass
                else:
                    call out_of_action_lines(Player.focused_Girl)

                    $ having_sex = False
            "Could you take care of something for me?" if Player.semen:
                if Player.semen and Player.focused_Girl.remaining_actions:
                    menu:
                        Player.focused_Girl.voice "[handjob_line]"
                        "Could you give me a handjob?":
                            call start_action(Player.focused_Girl, "handjob")
                        "Could use your feet?":
                            call start_action(Player.focused_Girl, "footjob")
                        "Could you give me a titjob?":
                            call start_action(Player.focused_Girl, "titjob")
                        "Could you suck my cock?":
                            call start_action(Player.focused_Girl, "blowjob")
                        "Never mind [[something else]":
                            pass
                elif Player.semen and not Player.focused_Girl.remaining_actions:
                    call out_of_action_lines(Player.focused_Girl)

                    $ having_sex = False
                else:
                    "You really don't have it in you, maybe take a break."

                    $ having_sex = False
            "Could you put on a show for me?":
                menu:
                    Player.focused_Girl.voice "[show_line]"
                    "Dance for me?":
                        if Player.focused_Girl.remaining_actions:
                            call Group_Strip(Player.focused_Girl)
                        else:
                            call out_of_action_lines(Player.focused_Girl)

                            $ having_sex = False
                    "Could you undress for me?":
                        call undress_Girl(Player.focused_Girl)
                    "You've got a little something. . . " if Player.focused_Girl.spunk:
                        call sex_menu_cleanup_lines(Player.focused_Girl)
                        call Girl_Cleanup(Player.focused_Girl,"ask")
                    "Could I watch you get yourself off?":
                        if Player.focused_Girl.remaining_actions:
                            call masturbate(Player.focused_Girl)
                        else:
                            call out_of_action_lines(Player.focused_Girl)

                            $ having_sex = False
                    "Maybe make out with [RogueX.name]?" if Player.focused_Girl != RogueX and RogueX.location == Player.location:
                        call LesScene(RogueX)
                    "Maybe make out with [KittyX.name]?" if Player.focused_Girl != KittyX and  KittyX.location == Player.location:
                        call LesScene(KittyX)
                    "Maybe make out with [LauraX.name]?" if Player.focused_Girl != LauraX and LauraX.location == Player.location:
                        call LesScene(LauraX)
                    "Maybe make out with [JeanX.name]?" if Player.focused_Girl != JeanX and JeanX.location == Player.location:
                        call LesScene(JeanX)
                    "Maybe make out with [StormX.name]?" if Player.focused_Girl != StormX and StormX.location == Player.location:
                        call LesScene(StormX)
                    "Maybe make out with [JubesX.name]?" if Player.focused_Girl != JubesX and JubesX.location == Player.location:
                        call LesScene(JubesX)
                    "Never mind [[something else]":
                        pass
            "Could we maybe. . . ?":
                if Player.focused_Girl.remaining_actions:
                    menu:
                        Player.focused_Girl.voice "[main_line]"
                        "Come over here, I've got something in mind. . .":
                            if Player.semen:
                                call start_action(Player.focused_Girl, "hotdog")
                            else:
                                "The spirit is apparently willing, but the flesh is spongy and bruised."

                                $ having_sex = False
                        "Fuck your pussy.":
                            if Player.semen:
                                call start_action(Player.focused_Girl, "sex")
                            else:
                                "The spirit is apparently willing, but the flesh is spongy and bruised."

                                $ having_sex = False
                        "Fuck your ass.":
                            if Player.semen:
                                call start_action(Player.focused_Girl, "anal")
                            else:
                                "The spirit is apparently willing, but the flesh is spongy and bruised."

                                $ having_sex = False
                        "How about some toys? [[Pussy]":
                            call dildo_check(Player.focused_Girl)

                            if _return == "found":
                                call start_action(Player.focused_Girl, "dildo_pussy")
                        "How about some toys? [[Anal]":
                            call dildo_check(Player.focused_Girl)

                            if _return == "found":
                                call start_action(Player.focused_Girl, "dildo_ass")
                        "Never mind [[something else]":
                            pass
                else:
                    call out_of_action_lines(Player.focused_Girl)

                    $ having_sex = False
            "Hey, do you want in on this? [[Threesome]" if len(Present) > 1 and not Partner:
                call Sex_Menu_Threesome(Player.focused_Girl)
            "Hey, [Partner.name]? [[Switch lead]" if Partner:
                call shift_focus(Partner)
            "Cheat Menu" if config.developer:
                call cheat_menu(Player.focused_Girl)
            "Never mind. [[exit]":
                if Player.focused_Girl.lust >= 50 or Player.focused_Girl.addiction >= 50:
                    $ Player.focused_Girl.change_face("sad")

                    if Player.focused_Girl.remaining_actions and Player.focused_Girl.SEXP >= 15 and round > 20:
                        if "round2" not in Player.focused_Girl.recent_history:
                            call exit_sex_menu_experienced_first_round_lines(Player.focused_Girl)

                            call change_Girl_stat(Player.focused_Girl, "inhibition", 30, 2)
                            call change_Girl_stat(Player.focused_Girl, "inhibition", 50, 1)
                        elif Player.focused_Girl.addiction >= 50:
                            call exit_sex_menu_experienced_addicted_lines(Player.focused_Girl)
                        else:
                            call exit_sex_menu_experienced_lines(Player.focused_Girl)

                        menu:
                            extend ""
                            "Yeah, I'm done for now." if Player.semen and "round2" not in Player.focused_Girl.recent_history:
                                if "unsatisfied" in Player.focused_Girl.recent_history and not Player.focused_Girl.session_orgasms:
                                    $ Player.focused_Girl.change_face("angry")
                                    $ Player.focused_Girl.eyes = "side"
                                    call change_Girl_stat(Player.focused_Girl, "love", 70, -2)
                                    call change_Girl_stat(Player.focused_Girl, "love", 90, -4)
                                    call change_Girl_stat(Player.focused_Girl, "obedience", 30, 2)
                                    call change_Girl_stat(Player.focused_Girl, "obedience", 70, 1)

                                    call exit_sex_menu_done_for_now_unsatisfied_lines(Player.focused_Girl)

                                    $ having_sex = False
                                else:
                                    $ Player.focused_Girl.change_face("bemused", 1)
                                    call change_Girl_stat(Player.focused_Girl, "obedience", 50, 2)

                                    call exit_sex_menu_done_for_now_satisfied_lines(Player.focused_Girl)

                                    $ having_sex = False
                            "I gave it a shot." if "round2" in Player.focused_Girl.recent_history:
                                if "unsatisfied" in Player.focused_Girl.recent_history and not Player.focused_Girl.session_orgasms:
                                    $ Player.focused_Girl.change_face("angry")
                                    $ Player.focused_Girl.eyes = "side"

                                    call exit_sex_menu_gave_it_a_shot_unsatisfied_lines(Player.focused_Girl)

                                    $ having_sex = False
                                else:
                                    $ Player.focused_Girl.change_face("bemused", 1)

                                    call exit_sex_menu_gave_it_a_shot_satisfied_lines(Player.focused_Girl)

                                    $ having_sex = False
                            "Hey, I did my part." if Player.focused_Girl.session_orgasms > 2:
                                $ Player.focused_Girl.change_face("sly", 1)

                                call exit_sex_menu_did_my_part_lines(Player.focused_Girl)

                                $ having_sex = False
                            "I'm tapped out for the moment, let's try again later." if not Player.semen:
                                $ Player.focused_Girl.change_face("normal")

                                call exit_sex_menu_out_of_semen_lines(Player.focused_Girl)

                                $ having_sex = False
                            "Ok, we can try something else." if multi_action and "round2" not in Player.focused_Girl.recent_history:
                                $ Player.focused_Girl.change_face("smile")
                                call change_Girl_stat(Player.focused_Girl, "love", 70, 2)
                                call change_Girl_stat(Player.focused_Girl, "love", 90, 1)

                                call exit_sex_menu_less_than_two_rounds_lines(Player.focused_Girl)

                                $ Player.focused_Girl.recent_history.append("round2")
                                $ Player.focused_Girl.daily_history.append("round2")
                            "Again? Ok, fine." if multi_action and "round2" in Player.focused_Girl.recent_history:
                                $ Player.focused_Girl.change_face("sly")

                                call exit_sex_menu_more_than_two_rounds_lines(Player.focused_Girl)
                    else:
                        $ Player.focused_Girl.change_face("bemused", 1)

                        call exit_sex_menu_girl_also_tired_lines(Player.focused_Girl)

                        call change_Girl_stat(Player.focused_Girl, "inhibition", 30, 2)
                        call change_Girl_stat(Player.focused_Girl, "inhibition", 50, 1)

                        $ having_sex = False
                else:
                    call generic_exit_sex_menu_lines(Player.focused_Girl)

                    $ having_sex = False

        if _return == "stop" or "angry" in Girl.recent_history:
            $ having_sex = False

    $ Girl.change_face()

    call sex_over

    return

label kiss_menu(Girl):
    menu:
        "Keep going. . .":
            pass
        "Slap her ass":
            call slap_ass(Girl)

            $ counter += 1
            $ round -= 1
        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
            pass
        "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
            "You concentrate on not burning out too quickly."

            $ Player.focusing = 1
        "Release your focus." if Player.focusing:
            "You release your concentration. . ."

            $ Player.focusing = 0
        "Start jack'in it." if multi_action and Player.secondary_action != "jerking_off":
            call jerking_off(Girl)

            if _return == "stop":
                return [None, "stop"]
        "Stop jack'in it." if multi_action and Player.secondary_action == "jerking_off":
            "You stop jack'in it."

            $ Player.secondary_action = None
        "Other options":
            menu:
                "Offhand action":
                    if Girl.remaining_actions and multi_action:
                        call set_secondary_action(Girl)

                        if _return == "stop":
                            return [None, "stop"]

                        if Player.secondary_action:
                             $ Girl.remaining_actions -= 1
                    else:
                        call tired_lines(Girl, "kiss")
                "Shift primary action":
                    if Girl.remaining_actions and multi_action:
                        menu:
                            "Move a hand to her thighs. . ." if Girl.action_counter["kiss"] >= 1:
                                return ["fondle_thighs", "auto"]
                            "Move a hand to her breasts. . ." if Girl.action_counter["kiss"] >= 1:
                                return ["fondle_breasts", "auto"]
                            "Never mind":
                                pass
                    else:
                        call tired_lines(Girl, "kiss")
                "Threesome actions" if Partner:
                    menu:
                        "Ask [Girl.name] to do something else with [Partner.name]" if action == "lesbian":
                            call Les_Change(Girl)
                        "Ask [Girl.name] to do something else with [Partner.name] (locked)" if action != "lesbian":
                            pass
                        "Ask [Partner.name] to do something else":
                            call Three_Change(Girl)
                        "Don't stop what you're doing. . ." if position_timer and second_girl_main_action:
                            $ position_timer = 0
                        "Swap to [Partner.name]":
                            call shift_focus(Partner)
                        "Undress [Partner.name]":
                            call undress_Girl(Partner)
                        "Clean up Partner" if any(Partner.spunk):
                            call Girl_Cleanup(Partner, "ask")
                        "Never mind":
                            pass
                "Undress [Girl.name]":
                    call undress_Girl(Girl)
                "Clean up [Girl.name]" if any(Girl.spunk):
                    call Girl_Cleanup(Girl, "ask")
                "Never mind":
                    pass
        "Back to Sex Menu" if multi_action and Girl.action_counter["kiss"] >= 5:
            ch_p "Let's try something else."

            return [None, "switch"]
        "End scene":
            ch_p "Let's stop for now."

            return [None, "stop"]

    return [None, "continue"]

label masturbation_menu(Girl):
    menu:
        "Keep watching.":
            pass
        "[Girl.name]. . .[[jump in]" if "unseen" not in Girl.recent_history and Girl.location == Player.location:
            "[Girl.name] slows what she's doing with a sly grin."

            call masturbation_join_in_lines(Girl, "masturbation")

            return "join"
        "\"Ahem. . .\"" if "unseen" in Girl.recent_history:
            return "interrupt"
        "Start jack'in it." if Player.secondary_action != "jerking_off":
            call jerking_off(Girl)

            if _return == "stop":
                return "stop"
        "Stop jack'in it." if Player.secondary_action == "jerking_off":
            $ Player.secondary_action = None
        "Slap her ass" if Girl.location == Player.location:
            if "unseen" in Girl.recent_history:
                "You smack [Girl.name] firmly on the ass!"

                return "interrupt"
            else:
                call slap_ass (Girl)

                $ counter += 1
                $ round -= 1
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
                "Threesome actions" if Girl.location == Player.location and Partner and "unseen" not in Girl.recent_history:
                    menu:
                        "Ask [Partner.name] to do something else":
                            call Three_Change(Girl)
                        "Swap to [Partner.name]":
                            call shift_focus(Partner)
                        "Undress [Partner.name]":
                            call undress_Girl(Partner)
                        "Clean up [Partner.name]" if any(Partner.spunk):
                            call Girl_Cleanup (Partner, "ask")
                        "Never mind":
                            pass
                "Show her feet" if not show_feet and Girl.pose in ["sex", "doggy"]:
                    $ show_feet = True
                "Hide her feet" if show_feet and Girl.pose in ["sex", "doggy"]:
                    $ show_feet = False
                "Undress [Girl.name]":
                    if "unseen" in Girl.recent_history:
                        ch_p "Oh, yeah, take it off. . ."

                        return "interrupt"
                    else:
                        call undress_Girl(Girl)
                "Clean up [Girl.name]" if any(Girl.spunk):
                    if "unseen" in Girl.recent_history:
                        ch_p "You've got a little something on you. . ."

                        return "interrupt"
                    else:
                        call Girl_Cleanup(Girl, "ask")
                "Never mind":
                    pass
        "Back to Sex Menu" if multi_action and Girl.location == Player.location:
            ch_p "Let's try something else."

            return "switch"
        "End Scene" if not multi_action or Girl.location != Player.location:
            ch_p "Let's stop for now."

            return "stop"

    return "continue"

label fondle_menu(Girl, action):
    menu:
        "Keep going. . .":
            pass
        "I want to stick a finger in. . ." if action == "fondle_pussy":
            if Girl.action_counter["finger_pussy"]:
                return ["finger_pussy", "auto"]
            else:
                menu:
                    "Ask her first":
                        return ["finger_pussy", "shift"]
                    "Don't ask first [[just stick it in]":
                        return ["finger_pussy", "auto"]
        "Pull back a bit. . ." if action == "fondle_pussy":
            return ["fondle_thighs", "pullback"]
        "Pull out. . ." if action == "finger_pussy":
            return ["fondle_pussy", "pullback"]
        "Slap her ass":
            call slap_ass(Girl)

            $ counter += 1
            $ round -= 1
        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
            pass
        "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
            "You concentrate on not burning out too quickly."

            $ Player.focusing = 1
        "Release your focus." if Player.focusing:
            "You release your concentration. . ."

            $ Player.focusing = 0
        "View":
            call shift_view(Girl, "menu")
        "Other options":
            menu:
                "Offhand action":
                    if Girl.remaining_actions and multi_action:
                        call set_secondary_action(Girl)

                        if _return == "stop":
                            return [None, "stop"]

                        if Player.secondary_action:
                            $ Girl.remaining_actions -= 1
                    else:
                        call tired_lines(Girl, action)
                "Shift primary action":
                    if Girl.remaining_actions and multi_action:
                        menu:
                            "Can I go a little deeper?" if action == "fondle_thighs":
                                return ["fondle_pussy", "shift"]
                            "Shift your hands a bit higher without asking" if action == "fondle_thighs":
                                return ["fondle_pussy", "auto"]
                            "I want to finger you." if action == "fondle_pussy":
                                return ["finger_pussy", "shift"]
                            "Just slip a finger in." if action == "fondle_pussy":
                                return ["finger_pussy", "auto"]
                            "Ask to suck on them." if action == "fondle_breasts":
                                return ["suck_breasts", "shift"]
                            "Just suck on them without asking." if action == "fondle_breasts":
                                return ["suck_breasts", "auto"]
                            "Pull back to fondling." if action = = "suck_breasts":
                                return ["fondle_breasts", "pullback"]
                            "I want to lick your pussy." if action in ["fondle_pussy", "finger_pussy"]:
                                return ["eat_pussy", "shift"]
                            "Just start licking." if action in ["fondle_pussy", "finger_pussy"]:
                                return ["eat_pussy", "auto"]
                            "Pull back to the thighs." if action in ["fondle_pussy"]:
                                return ["fondle_thighs", "auto"]
                            "I want to stick a dildo in." if action in ["fondle_pussy", "finger_pussy", "eat_pussy"]:
                                call dildo_check(Girl)

                                if _return == "found":
                                    return ["dildo_pussy", "shift"]
                            "Pull out and start rubbing again." if action in ["finger_pussy"]:
                                return ["fondle_pussy", "pullback"]
                            "I want to stick a finger in." if action in ["fondle_ass", "eat_ass"]:
                                return ["finger_ass", "shift"]
                            "Just stick a finger in without asking." if action in ["fondle_ass", "eat_ass"]:
                                return ["finger_ass", "auto"]
                            "I want to lick your asshole." if action in ["fondle_ass", "finger_ass"]:
                                return ["eat_ass", "shift"]
                            "Just start licking." if action in ["fondle_ass", "finger_ass"]:
                                return ["eat_ass", "auto"]
                            "I want to stick a dildo in." if action in ["fondle_ass", "finger_ass", "eat_ass"]:
                                call dildo_check(Girl)

                                if _return == "found":
                                    return ["dildo_ass", "shift"]
                            "Pull out and start rubbing again." if action in ["finger_ass"]:
                                return ["fondle_ass", "pullback"]
                            "Switch to fondling." if action = = "eat_ass":
                                return ["fondle_ass", "pullback"]
                            "Never mind":
                                pass
                    else:
                        call tired_lines(Girl, action)
                "Shift your focus" if Player.primary_action and Player.secondary_action:
                    call swap_actions(Girl)

                    $ action = _return

                    return [action, "auto"]
                "Threesome actions" if Partner:
                    menu:
                        "Ask [Girl.name] to do something else with [Partner.name]" if action == "lesbian":
                            call Les_Change(Girl)
                        "Ask [Girl.name] to do something else with [Partner.name] (locked)" if action != "lesbian":
                            pass
                        "Ask [Partner.name] to do something else":
                            call Three_Change
                        "Don't stop what you're doing. . ." if position_timer and second_girl_main_action:
                            $ position_timer = 0
                        "Swap to [Partner.name]":
                            call shift_focus(Partner)
                        "Undress [Partner.name]":
                            call undress_Girl(Partner)
                        "Clean up [Partner.name]" if any(Partner.spunk):
                            call Girl_Cleanup(Partner,"ask")
                        "Never mind":
                            pass
                "Show her feet" if not show_feet and Girl.pose in ["sex", "doggy"]:
                    $ show_feet = True
                "Hide her feet" if show_feet and Girl.pose in ["sex", "doggy"]:
                    $ show_feet = False
                "Undress [Girl.name]":
                    call undress_Girl(Girl)
                "Clean up [Girl.name]" if any(Girl.spunk):
                    call Girl_Cleanup(Girl,"ask")
                "Never mind":
                    pass
        "Back to Sex Menu" if multi_action:
            ch_p "Let's try something else."

            return [None, "switch"]
        "End Scene" if not multi_action:
            ch_p "Let's stop for now."

            return [None, "stop"]

    return [None, "continue"]

label handjob_menu(Girl, action):
    menu:
        "Keep going. . ." if action_speed:
            pass
        "Start moving? . ." if action in ["handjob", "footjob", "titjob"] and not action_speed:
            $ action_speed = 1
        "Speed up. . ." if action in ["handjob", "footjob", "titjob"] and action_speed < 2:
            $ action_speed = 2

            "You ask her to up the pace a bit."
        "Speed up. . . (locked)" if action in ["handjob", "footjob", "titjob"] and action_speed >= 2:
            pass
        "Slow Down. . ." if action in ["handjob", "footjob", "titjob"] and action_speed:
            $ action_speed -= 1

            "You ask her to slow it down a bit."
        "Slow Down. . . (locked)" if action in ["handjob", "footjob", "titjob"] and not action_speed:
            pass
        "Lick it. . ." if action == "blowjob" and action_speed != 1:
            $ action_speed = 1
        "Lick it. . . (locked)" if action == "blowjob" and action_speed == 1:
            pass
        "Just the head. . ." if action == "blowjob" and action_speed != 2:
            $ action_speed = 2
        "Just the head. . . (locked)" if action == "blowjob" and action_speed == 2:
            pass
        "Suck on it." if action == "blowjob" and action_speed != 3:
            $ action_speed = 3

            if Player.secondary_action == "jerking_off":
                "She dips her head a bit lower, and you move your hand out of the way."
        "Suck on it. (locked)" if action == "blowjob" and action_speed == 3:
            pass
        "Take it deeper." if action == "blowjob" and action_speed != 4:
            if "pushed" not in Girl.recent_history and Girl.action_counter["blowjob"] < 5:
                call change_Girl_stat(Girl, "love", 80, -(20 - 2*Girl.action_counter["blowjob"]))
                call change_Girl_stat(Girl, "obedience", 80, 30 - 3*Girl.action_counter["blowjob"])
                $ Girl.recent_history.append("pushed")

            if Player.secondary_action == "jerking_off" and action_speed != 3:
                "She takes it to the root, and you move your hand out of the way."

            $ action_speed = 4
        "Take it deeper. (locked)" if action == "blowjob" and action_speed == 4:
            pass
        "Set your own pace. . ." if action == "blowjob":
            "[Girl.name] hums contentedly."

            if "setpace" not in Girl.recent_history:
                call change_Girl_stat(Girl, "love", 80, 2)

            $ D20 = renpy.random.randint(1, 20)

            if Girl.action_counter["blowjob"] < 5:
                $ D20 -= 10
            elif Girl.action_counter["blowjob"] < 10:
                $ D20 -= 5

            if D20 > 15:
                $ action_speed = 4

                if "setpace" not in Girl.recent_history:
                    call change_Girl_stat(Girl, "inhibition", 80, 3)
            elif D20 > 10:
                $ action_speed = 3
            elif D20 > 5:
                $ action_speed = 2
            else:
                $ action_speed = 1

            $ Girl.recent_history.append("setpace")
        "Slap her ass. . ." if action in ["dildo_pussy", "dildo_ass"]:
            call slap_ass(Girl)

            $ counter += 1
            $ round -= 1
        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
            pass
        "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
            "You concentrate on not burning out too quickly."

            $ Player.focusing = 1
        "Release your focus." if Player.focusing:
            "You release your concentration. . ."

            $ Player.focusing = 0
        "Turn her around." if action == "footjob":
            $ Girl.pose = "doggy" if Girl.pose != "doggy" else "sex"

            call show_sex(Girl, action)

            "You turn her around. . ."
        "View" if action in ["dildo_pussy", "dildo_ass"]:
            call shift_view(Girl, "menu")
        "Other options":
                menu:
                    "I also want to fondle her breasts." if Player.secondary_action != "fondle_breasts":
                        if Girl.remaining_actions and multi_action:
                            $ Player.secondary_action = "fondle_breasts"

                            "You start to fondle her breasts."

                            $ Girl.remaining_actions -= 1
                        else:
                            call tired_lines(Girl, action)
                    "Offhand action":
                        if Girl.remaining_actions and multi_action:
                            call set_secondary_action(Girl)

                            if _return == "stop":
                                return [None, "stop"]

                            if Player.secondary_action:
                                $ Girl.remaining_actions -= 1
                        else:
                            call tired_lines(Girl, action)
                    "Shift primary action":
                        if Girl.remaining_actions and multi_action:
                            menu:
                                "How about a handy?" if action in ["footjob", "titjob", "blowjob"]:
                                    if Girl.remaining_actions and multi_action:
                                        return ["handjob", "shift"]
                                    else:
                                        call tired_lines(Girl, action)
                                "How about a footjob?" if action in ["handjob", "titjob", "blowjob"]:
                                    if Girl.remaining_actions and multi_action:
                                        return ["footjob", "shift"]
                                    else:
                                        call tired_lines(Girl, action)
                                "How about a titjob?" if action in ["handjob", "footjob", "blowjob"]:
                                    if Girl.remaining_actions and multi_action:
                                        return ["titjob", "shift"]
                                    else:
                                        call tired_lines(Girl, action)
                                "How about a blowjob?" if action in ["handjob", "footjob", "titjob"]:
                                    if Girl.remaining_actions and multi_action:
                                        return ["blowjob", "shift"]
                                    else:
                                        call tired_lines(Girl, action)
                                "I want to stick a finger in her ass." if action == "dildo_pussy":
                                    if Girl.remaining_actions and multi_action:
                                        return ["finger_ass", "shift"]
                                    else:
                                        call tired_lines(Girl, action)
                                "Just stick a finger in her ass without asking." if action == "dildo_pussy":
                                    if Girl.remaining_actions and multi_action:
                                        return ["finger_ass", "auto"]
                                    else:
                                        call tired_lines(Girl, action)
                                "I want to shift the dildo to her ass." if action == "dildo_pussy":
                                    if Girl.remaining_actions and multi_action:
                                        return ["dildo_ass", "shift"]
                                    else:
                                        call tired_lines(Girl, action)
                                "I want to stick a finger in her pussy." if action == "dildo_ass":
                                    if Girl.remaining_actions and multi_action:
                                        return ["finger_pussy", "shift"]
                                    else:
                                        call tired_lines(Girl, action)
                                "Just stick a finger in her pussy without asking." if action == "dildo_ass":
                                    if Girl.remaining_actions and multi_action:
                                        return ["finger_pussy", "auto"]
                                    else:
                                        call tired_lines(Girl, action)
                                "I want to shift the dildo to her pussy." if action == "dildo_ass":
                                    if Girl.remaining_actions and multi_action:
                                        return ["dildo_pussy", "shift"]
                                    else:
                                        call tired_lines(Girl, action)
                                "Never mind":
                                    pass
                        else:
                            call tired_lines(Girl, action)
                    "Shift your focus" if Player.primary_action and Player.secondary_action:
                        call swap_actions(Girl)

                        $ action = _return

                        return [action, "auto"]
                    "Shift your focus. (locked)" if action in ["dildo_pussy", "dildo_ass"] and not Player.secondary_action:
                        pass
                    "Threesome actions" if Partner:
                        menu:
                            "Ask [Girl.name] to do something else with [Partner.name]" if action == "lesbian":
                                call Les_Change(Girl)
                            "Ask [Girl.name] to do something else with [Partner.name] (locked)" if action != "lesbian":
                                pass
                            "Ask [Partner.name] to do something else":
                                call Three_Change(Girl)
                            "Don't stop what you're doing. . ." if position_timer and second_girl_main_action:
                                $ position_timer = 0
                            "Swap to [Partner.name]":
                                call shift_focus(Partner)
                            "Undress [Partner.name]":
                                call undress_Girl(Partner)
                            "Clean up [Partner.name]" if any(Partner.spunk):
                                call Girl_Cleanup(Partner,"ask")
                            "Never mind":
                                pass
                    "Undress [Girl.name]":
                        call undress_Girl(Girl)
                    "Clean up [Girl.name]" if any(Girl.spunk):
                        call Girl_Cleanup(Girl, "ask")
                    "Never mind":
                        pass
        "Back to Sex Menu" if multi_action:
            ch_p "Let's try something else."

            return [None, "switch"]
        "End Scene" if not multi_action:
            ch_p "Let's stop for now."

            return [None, "stop"]

    return [None, "continue"]

label sex_menu(Girl, action):
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
            call slap_ass(Girl)

            $ counter += 1
            $ round -= 1
        "Turn her around":
            $ Girl.pose = "doggy" if Girl.pose != "doggy" else "sex"

            call show_sex(Girl, action)

            "You turn her around. . ."
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
                    if Girl.remaining_actions and multi_action:
                        call set_secondary_action(Girl)

                        if _return == "stop":
                            return [None, "stop"]

                        if Player.secondary_action:
                            $ Girl.remaining_actions -= 1
                    else:
                        call Sex_Basic_Dialog(Girl,"tired")
                "Shift primary action":
                    if Girl.remaining_actions and multi_action:
                        menu:
                            "How about sex?" if action != "sex":
                                return ["sex", "shift"]
                            "Just stick it in her pussy [[without asking]." if action != "sex":
                                return ["sex", "auto"]
                            "How about anal?" if action != "anal":
                                return ["anal", "shift"]
                            "Just stick it in her ass [[without asking]." if action != "anal":
                                return ["anal", "auto"]
                            "Pull back to hotdog her." if action != "hotdog":
                                return ["hotdog", "pullback"]
                            "Never mind":
                                pass
                    else:
                        call tired_lines(Girl, action)
                "Threesome actions (locked)" if not Partner:
                    pass
                "Threesome actions" if Partner:
                    menu:
                        "Ask [Girl.name] to do something else with [Partner.name]" if action == "lesbian":
                            call Les_Change(Girl)
                        "Ask [Girl.name] to do something else with [Partner.name] (locked)" if action != "lesbian":
                            pass
                        "Ask [Partner.name] to do something else":
                            call Three_Change(Girl)
                        "Don't stop what you're doing. . ." if position_timer and second_girl_main_action:
                            $ position_timer = 0
                        "Swap to [Partner.name]":
                            call shift_focus(Partner)
                        "Undress [Partner.name]":
                            call undress_Girl(Partner)
                        "Clean up [Partner.name]" if any(Partner.spunk):
                            call Girl_Cleanup(Partner,"ask")
                        "Never mind":
                            pass
                "Just take a look at her.":
                    $ action_speed = 0
                "Show her feet" if not show_feet and Girl.pose in ["sex", "doggy"]:
                    $ show_feet = True
                "Hide her feet" if show_feet and Girl.pose in ["sex", "doggy"]:
                    $ show_feet = False
                "Undress [Girl.name]":
                    call undress_Girl(Girl)
                "Clean up [Girl.name]" if any(Girl.spunk):
                    call Girl_Cleanup(Girl,"ask")
                "Never mind":
                    pass
        "Back to Sex Menu" if multi_action:
            ch_p "Let's try something else."

            return [None, "switch"]
        "End Scene" if not multi_action:
            ch_p "Let's stop for now."

            return [None, "stop"]

    return [None, "continue"]

label begging_menu(Girl, action):
    menu:
        extend ""
        "Sorry, never mind.":
            if "no_" + action not in Girl.daily_history:
                $ Girl.change_face("bemused")

                call sorry_never_mind_lines(Girl, action)

                $ Girl.recent_history.append("no_" + action)
                $ Girl.daily_history.append("no_" + action)
        "Maybe later?" if "no_" + action not in Girl.daily_history:
            if action == "masturbation":
                $ Girl.change_face("sexy", 1)
            else:
                $ Girl.change_face("sexy")

            if action == "fondle_breasts" and Girl not in [LauraX, JubesX]:
                "She re-adjusts her cleavage."

            call maybe_later_lines(Girl, action)

            if action in ["fondle_thighs", "fondle_breasts", "suck_breasts"]:
                call change_Girl_stat(Girl, "love", 80, 1)
                call change_Girl_stat(Girl, "inhibition", 30, 2)

                if action in breast_actions:
                    call change_Girl_stat(Girl, "love", 50, 1)
            elif action in ["masturbation", "fondle_pussy"]:
                call change_Girl_stat(Girl, "love", 80, 2)
                call change_Girl_stat(Girl, "inhibition", 70, 2)
            elif action in ["fondle_ass"]:
                call change_Girl_stat(Girl, "love", 80, 2)
                call change_Girl_stat(Girl, "inhibition", 50, 2)
            elif action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal"]:
                call change_Girl_stat(Girl, "love", 80, 2)
                call change_Girl_stat(Girl, "inhibition", 70, 2)
            elif action in ["hotdog"]:
                call change_Girl_stat(Girl, "love", 80, 1)
                call change_Girl_stat(Girl, "inhibition", 50, 1)

            $ Girl.recent_history.append("no_" + action)
            $ Girl.daily_history.append("no_" + action)
        "You look like you could use it. . ." if action == "masturbation":
            if approval:
                $ Girl.change_face("sexy")
                call change_Girl_stat(Girl, "obedience", 90, 2)
                call change_Girl_stat(Girl, "obedience", 50, 2)
                call change_Girl_stat(Girl, "inhibition", 70, 3)
                call change_Girl_stat(Girl, "inhibition", 40, 2)

                call begging_lines(Girl, action)

                return action
            else:
                call action_rejected(Girl, action)
        "Come on, please?" if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "blowjob"]:
            if approval:
                $ Girl.change_face("sexy")

                if action == "fondle_thighs":
                    call change_Girl_stat(Girl, "obedience", 60, 1)
                    call change_Girl_stat(Girl, "obedience", 30, 2)
                    call change_Girl_stat(Girl, "inhibition", 50, 1)
                    call change_Girl_stat(Girl, "inhibition", 30, 2)
                elif action in ["fondle_breasts", "suck_breasts"]:
                    if Girl != LauraX:
                        call change_Girl_stat(Girl, "obedience", 90, 1)

                    call change_Girl_stat(Girl, "obedience", 50, 2)
                    call change_Girl_stat(Girl, "inhibition", 60, 3)
                    call change_Girl_stat(Girl, "inhibition", 30, 2)
                elif action in ["fondle_pussy", "blowjob"]:
                    call change_Girl_stat(Girl, "obedience", 90, 2)
                    call change_Girl_stat(Girl, "obedience", 50, 2)
                    call change_Girl_stat(Girl, "inhibition", 70, 3)
                    call change_Girl_stat(Girl, "inhibition", 40, 2)

                call begging_lines(Girl, action)

                return action
            else:
                if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy"]:
                    $ Girl.change_face("sexy")

                    call please_not_good_enough_lines(Girl, action)
                elif action in ["blowjob"]:
                    if approval_check(Girl, 1100, taboo_modifier = 3): # 110, 125, 140, taboo -120(230)             Handy instead?
                        call change_Girl_stat(Girl, "inhibition", 80, 1)
                        call change_Girl_stat(Girl, "inhibition", 60, 3)
                        $ Girl.change_face("confused", 1)

                        call maybe_handjob_instead_lines(Girl)

                        menu:
                            extend ""
                            "Sure, that's fine.":
                                call change_Girl_stat(Girl, "love", 80, 2)
                                call change_Girl_stat(Girl, "inhibition", 60, 1)
                                call change_Girl_stat(Girl, "obedience", 50, 1)

                                return "handjob"
                            "Nah, if it's not a BJ, forget it.":
                                call change_Girl_stat(Girl, "love", 200, -2)

                                call alternative_rejected_lines(Girl)

                                call change_Girl_stat(Girl, "obedience", 70, 2)

                $ Girl.recent_history.append("no_" + action)
                $ Girl.daily_history.append("no_" + action)
        "I'm sure I can convince you later. . ." if action in ["eat_pussy", "eat_ass"] and "no_" + action not in Girl.daily_history:
            $ Girl.change_face("sexy")

            call maybe_later_lines(Girl, action)

            call change_Girl_stat(Girl, "love", 80, 2)
            call change_Girl_stat(Girl, "inhibition", 70, 2)

            $ Girl.recent_history.append("no_" + action)
            $ Girl.daily_history.append("no_" + action)
        "I think you'd really enjoy it. . ." if action in ["eat_pussy", "eat_ass"]:
            if approval:
                $ Girl.change_face("sexy")
                call change_Girl_stat(Girl, "obedience", 90, 2)
                call change_Girl_stat(Girl, "obedience", 50, 2)

                call trying_to_convince_lines(Girl, action)

                call change_Girl_stat(Girl, "inhibition", 70, 3)
                call change_Girl_stat(Girl, "inhibition", 40, 2)

                return action
            else:
                $ Girl.change_face("sexy")

                call unconvinced_lines(Girl, action)

                $ Girl.recent_history.append("no_" + action)
                $ Girl.daily_history.append("no_" + action)
        "Just one good squeeze?" if action == "fondle_ass":
            if approval:
                $ Girl.change_face("sexy")
                call change_Girl_stat(Girl, "obedience", 90, 1)
                call change_Girl_stat(Girl, "obedience", 50, 2)

                call begging_lines(Girl, action)

                call change_Girl_stat(Girl, "inhibition", 70, 1)
                call change_Girl_stat(Girl, "inhibition", 40, 2)

                return action
            else:
                $ Girl.change_face("sexy")

                call unconvinced_lines(Girl, action)

                $ Girl.recent_history.append("no_" + action)
                $ Girl.daily_history.append("no_" + action)
        "I'd really appreciate it. . ." if action in ["handjob"]:
            if approval:
                $ Girl.change_face("sexy")
                call change_Girl_stat(Girl, "obedience", 90, 2)
                call change_Girl_stat(Girl, "obedience", 50, 2)
                call change_Girl_stat(Girl, "inhibition", 70, 3)
                call change_Girl_stat(Girl, "inhibition", 40, 2)

                call begging_lines(Girl, action)

                return action
            else:
                call action_rejected(Girl, action)
        "I think this could be fun for both of us. . ." if action in ["titjob"]:
            if approval:
                $ Girl.change_face("sexy")
                call change_Girl_stat(Girl, "obedience", 80, 2)
                call change_Girl_stat(Girl, "obedience", 40, 2)
                call change_Girl_stat(Girl, "inhibition", 70, 3)
                call change_Girl_stat(Girl, "inhibition", 40, 2)

                call trying_to_convince_lines(Girl, action)

                return action
            else:
                $ approval = approval_check(Girl, 1100, taboo_modifier = 3) # 110, 125, 140, taboo -120(230)             Handy instead?

                $ blowjob_rejected = False

                if approval >= 2:
                    call change_Girl_stat(Girl, "inhibition", 80, 1)
                    call change_Girl_stat(Girl, "inhibition", 60, 3)
                    $ Girl.change_face("confused", 1)

                    call maybe_blowjob_instead_lines(Girl)

                    menu:
                        extend ""
                        "Ok, get down there.":
                            call change_Girl_stat(Girl, "love", 80, 2)
                            call change_Girl_stat(Girl, "inhibition", 60, 1)
                            call change_Girl_stat(Girl, "obedience", 50, 1)

                            return "blowjob"
                        "Nah, it's all about dem titties.":
                            $ blowjob_rejected = True

                    call change_Girl_stat(Girl, "love", 200, -2)

                    call alternative_rejected_lines(Girl)

                    call change_Girl_stat(Girl, "obedience", 70, 2)
                elif approval:
                    call change_Girl_stat(Girl, "inhibition", 80, 1)
                    call change_Girl_stat(Girl, "inhibition", 60, 3)
                    $ Girl.change_face("confused", 1)

                    call maybe_handjob_instead_lines(Girl)

                    menu:
                        extend ""
                        "Sure, that's fine.":
                            call change_Girl_stat(Girl, "love", 80, 2)
                            call change_Girl_stat(Girl, "inhibition", 60, 1)
                            call change_Girl_stat(Girl, "obedience", 50, 1)

                            return "handjob"
                        "Seriously, titties." if blowjob_rejected:
                            pass
                        "Nah, it's all about dem titties." if not blowjob_rejected:
                            pass

                    call change_Girl_stat(Girl, "love", 200, -2)

                    call alternative_rejected_lines(Girl)

                    call change_Girl_stat(Girl, "obedience", 70, 2)

                $ Girl.recent_history.append("no_" + action)
                $ Girl.daily_history.append("no_" + action)
        "I think you'd like it. . ." if action in ["dildo_pussy", "dildo_ass"]:
            if approval:
                $ Girl.change_face("sexy")
                call change_Girl_stat(Girl, "obedience", 90, 2)
                call change_Girl_stat(Girl, "obedience", 50, 2)
                call change_Girl_stat(Girl, "inhibition", 70, 3)
                call change_Girl_stat(Girl, "inhibition", 40, 2)

                call trying_to_convince_lines(Girl, action)

                return action
            else:
                call action_rejected(Girl, action)
        "I think you'd enjoy it as much as I would. . ." if action in ["sex"]:
            if approval:
                $ Girl.change_face("sexy")
                call change_Girl_stat(Girl, "obedience", 90, 2)
                call change_Girl_stat(Girl, "obedience", 50, 2)
                call change_Girl_stat(Girl, "inhibition", 70, 3)
                call change_Girl_stat(Girl, "inhibition", 40, 2)

                call trying_to_convince_lines(Girl, action)

                return action
            else:
                call action_rejected(Girl, action)
        "I bet it would feel really good. . ." if action in ["anal"]:
            if approval:
                $ Girl.change_face("sexy")
                call change_Girl_stat(Girl, "obedience", 90, 2)
                call change_Girl_stat(Girl, "obedience", 50, 2)
                call change_Girl_stat(Girl, "inhibition", 70, 3)
                call change_Girl_stat(Girl, "inhibition", 40, 2)

                call trying_to_convince_lines(Girl, action)

                return action
            else:
                call action_rejected(Girl, action)
        "You might like it. . ." if action in ["hotdog"]:
            if approval:
                $ Girl.change_face("sexy")
                call change_Girl_stat(Girl, "obedience", 60, 2)
                call change_Girl_stat(Girl, "inhibition", 50, 2)

                call trying_to_convince_lines(Girl, action)

                return action
            else:
                call action_rejected(Girl, action)
        "Just get at it already." if action == "masturbation":
            call forced_action(Girl, action)

            if _return == "accepted":
                return action
        "[[Start caressing her thigh anyway]" if action == "fondle_thighs":
            call forced_action(Girl, action)

            if _return == "accepted":
                return action
        "[[Grab her chest anyway]" if action == "fondle_breasts":
            call forced_action(Girl, action)

            if _return == "accepted":
                return action
        "[[Start sucking anyway]" if action == "suck_breasts":
            call forced_action(Girl, action)

            if _return == "accepted":
                return action
        "[[Start fondling anyway]" if action in ["fondle_pussy", "fondle_ass"]:
            call forced_action(Girl, action)

            if _return == "accepted":
                return action
        "[[Get in there anyway]" if action == "eat_pussy":
            call forced_action(Girl, action)

            if _return == "accepted":
                return action
        "[[Slide a finger in anyway]" if action == "finger_ass":
            call forced_action(Girl, action)

            if _return == "accepted":
                return action
        "[[Start licking anyway]" if action in ["eat_pussy", "eat_ass"]:
            call forced_action(Girl, action)

            if _return == "accepted":
                return action
        "Come on, get to work." if action in ["handjob", "footjob"]:                                               # Pressured into it
            call forced_action(Girl, action)

            if _return == "accepted":
                return action
        "Come on, let me fuck those titties, [Girl.petname]" if action in ["titjob"]:
            $ Girl.name_check() #checks reaction to petname

            call forced_action(Girl, action)

            if _return == "accepted":
                return action
        "Suck it, [Girl.petname]" if action in ["blowjob"]:                                               # Pressured into it
            $ Girl.name_check() #checks reaction to petname

            call forced_action(Girl, action)

            if _return == "accepted":
                return action
        "[[Press it against her.]]" if action in ["dildo_pussy", "dildo_ass"]:
            call forced_action(Girl, action)

            if _return == "accepted":
                return action
        "Bend over." if action in ["sex", "anal", "hotdog"]:
            call forced_action(Girl, action)

            if _return == "accepted":
                return action

    return "rejected"

label try_something_else_menu(Girl, action):
    menu:
        extend ""
        "How about a handy?" if action in ["footjob", "titjob", "blowjob", "sex", "anal", "hotdog"] and Girl.remaining_actions and multi_action:
            return ["handjob", "shift"]
        "How about a footjob?" if action in ["handjob", "titjob", "blowjob", "sex", "anal", "hotdog"] and Girl.remaining_actions and multi_action:
            return ["footjob", "shift"]
        "How about a titjob?" if action in ["handjob", "footjob", "blowjob", "sex", "anal", "hotdog"] and Girl.remaining_actions and multi_action:
            return ["titjob", "shift"]
        "How about a blowjob?" if action in ["handjob", "footjob", "titjob", "sex", "anal", "hotdog"] and Girl.remaining_actions and multi_action:
            if action != "anal":
                return ["blowjob", "shift"]
            else:
                if Girl.action_counter["anal"] >= 5 and Girl.action_counter["blowjob"] >= 10 and Girl.SEXP >= 50:
                    return ["blowjob", "shift"]
                else:
                    call no_ass_to_mouth_lines(Girl, action)

                    return ["handjob", "shift"]
        "Finish up." if action in ["handjob", "footjob", "titjob", "blowjob", "sex", "anal", "hotdog"] and Player.focusing:
            "You release your concentration. . ."

            $ Player.focusing = 0
            $ Player.focus += 15
        "No, get back down there." if action in ["handjob", "footjob", "titjob", "blowjob"]:
            if approval_check(Girl, 1200) or approval_check(Girl, 500, "O"):
                call change_Girl_stat(Girl, "love", 200, -5)
                call change_Girl_stat(Girl, "obedience", 50, 3)
                call change_Girl_stat(Girl, "obedience", 80, 2)

                "She grumbles but keeps going."
            else:
                $ Girl.change_face("angry", 1)

                call show_full_body(Girl)

                "She scowls at you, drops your cock and pulls back."

                call this_is_boring_lines(Girl, action)

                call change_Girl_stat(Girl, "love", 50, -3, 1)
                call change_Girl_stat(Girl, "love", 80, -4, 1)
                call change_Girl_stat(Girl, "obedience", 30, -1, 1)
                call change_Girl_stat(Girl, "obedience", 50, -1, 1)
                $ Girl.add_word(1,"angry", "angry")

                return [None, "stop"]
        "Finish up.":
            "You let go. . ."

            return [None, "switch"]
        "Let's try something else." if multi_action:
            return [None, "switch"]
        "No, this is fun.":
            if approval_check(Girl, 1200) or approval_check(Girl, 500, "O"):
                call change_Girl_stat(Girl, "love", 200, -5)
                call change_Girl_stat(Girl, "obedience", 50, 3)
                call change_Girl_stat(Girl, "obedience", 80, 2)

                "She grumbles but lets you keep going."
            else:
                $ Girl.change_face("angry", 1)

                call show_full_body(Girl)

                "She scowls at you and pulls back."

                call this_is_boring_lines(Girl, action)

                call change_Girl_stat(Girl, "love", 50, -3, 1)
                call change_Girl_stat(Girl, "love", 80, -4, 1)
                call change_Girl_stat(Girl, "obedience", 30, -1, 1)
                call change_Girl_stat(Girl, "obedience", 50, -1, 1)
                $ Girl.add_word(1,"angry", "angry")

                return [None, "stop"]

    return [None, "continue"]

label girl_unsatisfied_menu(Girl, action):
    if action in sex_actions:
        call not_ready_to_stop_narrations(Girl, action)

        menu:
            "Keep going?"
            "Yes, keep going for a bit." if Player.semen:
                $ line = "You get back into it."
            "No, I'm done." if Player.semen:
                "You pull back."

                return "stop"
            "No, I'm spent." if not Player.semen:
                "You pull back."

                return "stop"
    else:
        "[Girl.name] still seems a bit unsatisfied with the experience."

        if action == "masturbation":
            menu:
                "Let her keep going?"
                "Yes, keep going for a bit.":
                    $ line = "You let her get back into it"
                "No, I'm done.":
                    "You ask her to stop."

                    return "stop"
        else:
            menu:
                "Finish her?"
                "Yes, keep going for a bit.":
                    $ line = "You get back into it."
                "No, I'm done.":
                    "You pull back."

                    return "stop"

    return "continue"

label what_do_you_think_youre_doing_menu(Girl, action):
    menu:
        extend ""
        "Sorry, sorry! Never mind.":
            if approval:
                $ Girl.change_face("sexy", 1)
                call change_Girl_stat(Girl, "obedience", 70, 3)
                call change_Girl_stat(Girl, "inhibition", 50, 3)
                call change_Girl_stat(Girl, "inhibition", 70, 1)

                call since_you_are_so_nice_lines(Girl, action)

                return "accepted"

            "You pull back before you really get it in."

            $ Girl.change_face("bemused", 1)

            call pull_back_before_get_in_lines(Girl, action)
        "Just playing with my favorite toys." if action in dildo_actions:
            call change_Girl_stat(Girl, "love", 80, -10, 1)
            call change_Girl_stat(Girl, "love", 200, -10)

            "You press it inside some more."

            call change_Girl_stat(Girl, "obedience", 70, 3)
            call change_Girl_stat(Girl, "inhibition", 50, 3)

            if not approval_check(Girl, 700, "O", taboo_modifier = 1): #checks if obedience is 700+
                $ Girl.change_face("angry")

                call were_done_here_lines(Girl, action)

                call change_Girl_stat(Girl, "love", 50, -10, 1)
                call change_Girl_stat(Girl, "obedience", 50, 3)

                call show_full_body(Girl)

                $ Girl.recent_history.append("angry")
                $ Girl.daily_history.append("angry")
            else:
                $ Girl.change_face("sad")

                call knows_her_place_lines(Girl, action)

                return "accepted"
        "Just fucking." if action in ["sex", "anal"]:
            call change_Girl_stat(Girl, "love", 80, -10, 1)
            call change_Girl_stat(Girl, "love", 200, -10)

            if action == "sex":
                "You press inside some more."
            elif action == "anal":
                "You press into her."

            call change_Girl_stat(Girl, "obedience", 70, 3)
            call change_Girl_stat(Girl, "inhibition", 50, 3)

            if not approval_check(Girl, 700, "O", taboo_modifier = 1):   #checks if obedience is 700+
                $ Girl.change_face("angry")

                call were_done_here_lines(Girl, action)

                call change_Girl_stat(Girl, "love", 50, -10, 1)
                call change_Girl_stat(Girl, "obedience", 50, 3)

                call show_full_body(Girl)

                $ Girl.recent_history.append("angry")
                $ Girl.daily_history.append("angry")
            else:
                $ Girl.change_face("sad")

                call knows_her_place_lines(Girl, action)

                return "accepted"
        "You'll see." if action == "hotdog":
            call change_Girl_stat(Girl, "love", 80, -10, 1)
            call change_Girl_stat(Girl, "love", 200, -8)

            "You grind against her asscrack."

            call change_Girl_stat(Girl, "obedience", 70, 3)
            call change_Girl_stat(Girl, "inhibition", 50, 3)

            if not approval_check(Girl, 500, "O", taboo_modifier = 1): #checks if obedience is 700+
                $ Girl.change_face("angry")

                call were_done_here_lines(Girl, action)

                call change_Girl_stat(Girl, "love", 50, -10, 1)
                call change_Girl_stat(Girl, "obedience", 50, 3)

                call show_full_body(Girl)

                $ Girl.recent_history.append("angry")
                $ Girl.daily_history.append("angry")
            else:
                $ Girl.change_face("sad")

                call knows_her_place_lines(Girl, action)

                return "accepted"

    return "rejected"
