label enter_main_sex_menu:
    if focused_Girl == EmmaX:
        if "classcaught" not in focused_Girl.history:
            ch_e "I can't imagine being a part of something so. . . tawdry."

            return

        if "three" not in focused_Girl.history and not AloneCheck(focused_Girl):
            call expression focused_Girl.Tag + "_ThreeCheck

        if Taboo > 20 and "taboo" not in focused_Girl.history:
            call expression focused_Girl.Tag + "_Taboo_Talk

            if bg_current == "bg_classroom" or bg_current in PersonalRooms and AloneCheck(focused_Girl):
                ch_p "We could just lock the door, right?"
                ch_e "We certainly could. . ."
                "[focused_Girl.name] walks to the door and locks it behind her."

                $ Player.Traits.append("locked")

                call Taboo_Level
            else:
                return

    $ action_context = 0
    $ primary_action = 0
    $ offhand_action = 0
    $ girl_offhand_action = 0

    call expression focused_Girl.Tag + "_Hide" pass(1)

    $ focused_Girl.ArmPose = 1

    call set_the_scene(1,0,0,0,1)

    if focused_Girl in [EmmaX, StormX]:
        if "detention" in focused_Girl.recent_history:
            $ temp_modifier = 20 if temp_modifier <= 20 else temp_modifier

    if not Player.semen:
        "You're a little out of juice at the moment, you might want to wait a bit."
    if Player.Focus >= 95:
        "You're practically buzzing, the slightest breeze could set you off."
    if not focused_Girl.remaining_actions:
        "[focused_Girl.name]'s looking a bit tired out, maybe let her rest a bit."

    if "caught" in focused_Girl.recent_history or "angry" in focused_Girl.recent_history:
        if focused_Girl.location == bg_current:
            call sex_menu_caught_or_angry_lines(focused_Girl)

        $ focused_Girl.OutfitChange()
        $ focused_Girl.DrainWord("caught",1,0)

        return

    if Round < 5:
        call sex_menu_less_than_five_rounds(focused_Girl)

        return

    $ main_line = None
    $ fondle_line = None
    $ handjob_line = None
    $ show_line = None

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

    call GirlsAngry
    jump enter_main_sex_menu

label girl_sex_menu(Girl):
    if Girl == RogueX:
        $ main_line = "So what would you like to do?"
        $ fondle_line = "Well where exactly were you interested in touching, " + Girl.Petname + "?"
        $ handjob_line = "What did you have in mind, " + Girl.Petname + "?"
        $ show_line = "What sort of show were you expecting?"
    elif Girl == KittyX:
        $ main_line = "So what would you like to do?"
        $ fondle_line = "Um, what did you want to touch, " + Girl.Petname + "?"
        $ handjob_line = Girl.Like + "what did you want me to do?"
        $ show_line = Girl.Like + "what did you want to see?"
    elif Girl == EmmaX:
        $ main_line = "So, what was it you hoped to do?"
        $ fondle_line = "Well? Where did you want to touch, " + Girl.Petname + "?"
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
        $ fondle_line = "What did you wish to touch, " + Girl.Petname + "?"
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
                call Makeout (Girl)
            else:
                call out_of_action_lines(Girl)
        "Could I touch you?":
            if Girl.remaining_actions:
                if Girl in [EmmaX, StormX]:
                    $ Girl.change_face("sly")
                else:
                    $ Girl.mouth = "smile"

                menu:
                    Girl.voice "[fondle_line]"
                    "Could I give you a massage?":
                        call Massage (Girl)
                    "Your thighs?" if Girl.remaining_actions:
                        call expression Girl.Tag + "_Fondle_Thighs"
                    "Your breasts?":
                        call expression Girl.Tag + "_Fondle_Breasts"
                    "Suck your breasts?" if Girl.remaining_actions and Girl.action_counter["suck_breasts"]:
                        call expression Girl.Tag + "_Suck_Breasts"
                    "Your pussy?" if Girl.remaining_actions:
                        call expression Girl.Tag + "_Fondle_Pussy"
                    "Lick your pussy?" if Girl.remaining_actions and Girl.action_counter["eat_pussy"]:
                        call expression Girl.Tag + "_Lick_Pussy"
                    "Your ass?":
                        call expression Girl.Tag + "_Fondle_Ass"
                    "Never mind [[something else]":
                        jump main_sex_menu
            else:
                call out_of_action_lines(Girl)
        "Could you take care of something for me? [[Your dick, you mean your dick]" if Player.semen:
            if Girl.remaining_actions:
                menu:
                    Girl.voice "[handjob_line]"
                    "Could you give me a handjob?":
                        call expression Girl.Tag + "_Handjob"
                    "Could you give me a titjob?":
                        call expression Girl.Tag + "_Titjob"
                    "Could you suck my cock?":
                        call expression Girl.Tag + "_Blowjob"
                    "Could use your feet?":
                        call expression Girl.Tag + "_Footjob"
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
                "You've got a little something. . . [[clean-up]" if Girl.Spunk:
                    call sex_menu_cleanup_lines(Girl)
                    call Girl_Cleanup(Girl,"ask")
                "Could I watch you get yourself off? [[masturbate]":
                    if Girl.remaining_actions:
                        call expression Girl.Tag "_Masturbate"
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
                            call expression character.Tag "_Sex_H"
                        else:
                            "The spirit is apparently willing, but the flesh is spongy and bruised."
                    "Fuck your pussy.":
                        if Player.semen:
                            call expression character.Tag "_Sex_P"
                        else:
                            "The spirit is apparently willing, but the flesh is spongy and bruised."
                    "Fuck your ass.":
                        if Player.semen:
                            call expression character.Tag "_Sex_A"
                        else:
                            "The spirit is apparently willing, but the flesh is spongy and bruised."
                    "How about some toys? [[Pussy]":
                        call expression character.Tag "_Dildo_Pussy"
                    "How about some toys? [[Anal]":
                        call expression character.Tag "_Dildo_Ass"
                    "Never mind [[something else]":
                        jump main_sex_menu
            else:
                call out_of_action_lines(Girl)
        "Hey, do you want in on this? [[Threesome]" if not Partner:
            call Sex_Menu_Threesome(Girl)
            jump main_sex_menu
        "Hey, [Partner.name]? [[Switch lead]" if Partner:
            call expression Partner.Tag + "_SexAct" pass ("switch")

            return True
        "Cheat Menu" if config.developer:
            call Cheat_Menu(Girl)
        "Never mind. [[exit]":
            if Girl.lust >= 50 or Girl.addiction >= 50:
                $ Girl.change_face("sad")

                if Girl.remaining_actions and Girl.SEXP >= 15 and Round > 20:
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
                                $ Girl.change_face("angry")
                                $ Girl.Eyes = "side"
                                $ Girl.change_stat("love", 70, -2)
                                $ Girl.change_stat("love", 90, -4)
                                $ Girl.change_stat("obedience", 30, 2)
                                $ Girl.change_stat("obedience", 70, 1)

                                call exit_sex_menu_done_for_now_unsatisfied_lines(Girl)
                            else:
                                $ Girl.change_face("bemused", 1)
                                $ Girl.change_stat("obedience", 50, 2)

                                call exit_sex_menu_done_for_now_satisfied_lines(Girl)
                        "I gave it a shot." if "round2" in Girl.recent_history:
                            if "unsatisfied" in Girl.recent_history and not Girl.session_orgasms:
                                $ Girl.change_face("angry")
                                $ Girl.Eyes = "side"

                                call exit_sex_menu_gave_it_a_shot_unsatisfied_lines(Girl)
                            else:
                                $ Girl.change_face("bemused", 1)

                                call exit_sex_menu_gave_it_a_shot_satisfied_lines(Girl)
                        "Hey, I did my part." if Girl.session_orgasms > 2:
                            $ Girl.change_face("sly", 1)

                            call exit_sex_menu_did_my_part_lines(Girl)
                        "I'm tapped out for the moment, let's try again later." if not Player.semen:
                            $ Girl.change_face("normal")

                            call exit_sex_menu_out_of_semen_lines(Girl)
                        "Ok, we can try something else." if multi_action and "round2" not in Girl.recent_history:
                            $ Girl.change_face("smile")
                            $ Girl.change_stat("love", 70, 2)
                            $ Girl.change_stat("love", 90, 1)

                            call exit_sex_menu_less_than_two_rounds_lines(Girl)

                            $ Girl.recent_history.append("round2")
                            $ Girl.daily_history.append("round2")

                            jump main_sex_menu
                        "Again? Ok, fine." if multi_action and "round2" in Girl.recent_history:
                            $ Girl.change_face("sly")

                            call exit_sex_menu_more_than_two_rounds_lines(Girl)
                            jump main_sex_menu
                else:
                    $ Girl.change_face("bemused", 1)

                    call exit_sex_menu_girl_also_tired_lines(Girl)

                    $ Girl.change_stat("inhibition", 30, 2)
                    $ Girl.change_stat("inhibition", 50, 1)
            else:
                call generic_exit_sex_menu_lines(Girl)

            $ Girl.change_face()

            call Sex_Over

            return True

    return False
