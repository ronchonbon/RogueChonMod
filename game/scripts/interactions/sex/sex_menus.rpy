label enter_main_sex_menu(Girl):
    if not Player.semen:
        "You're a little out of juice at the moment, you might want to wait a bit."

        return

    if Player.climax >= 95:
        "You're practically buzzing, the slightest breeze could set you off."

    if not Girl.remaining_Actions:
        "[Girl.name]'s looking a bit tired out, maybe let her rest a bit."

        return

    if round < 5:
        call sex_menu_less_than_five_rounds_lines(Girl)

        return

    call girl_sex_menu(Girl)

    return

label girl_sex_menu(Girl):
    $ shift_focus(Girl)
    call set_the_scene

    $ having_sex = True

    while having_sex:
        if Girl == RogueX:
            $ main_line = "So what would you like to do?"
            $ fondle_line = "Well where exactly were you interested in touching, " + Girl.player_petname + "_?"
            $ handjob_line = "What did you have in mind, " + Girl.player_petname + "_?"
            $ show_line = "What sort of show were you expecting?"
        elif Girl == KittyX:
            $ main_line = "So what would you like to do?"
            $ fondle_line = "Um, what did you want to touch, " + Girl.player_petname + "_?"
            $ handjob_line = Girl.Like + "_what did you want me to do?"
            $ show_line = Girl.Like + "_what did you want to see?"
        elif Girl == EmmaX:
            $ main_line = "So, what was it you hoped to do?"
            $ fondle_line = "Well? Where did you want to touch, " + Girl.player_petname + "_?"
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
            $ fondle_line = "What did you wish to touch, " + Girl.player_petname + "_?"
            $ handjob_line = "What did you want me to do?"
            $ show_line = "What did you want to see?"
        elif Girl == JubesX:
            $ main_line = "So what did you wanna do?"
            $ fondle_line = "Where were you thinking?"
            $ handjob_line = "What were you thinking?"
            $ show_line = "What kind of show?"

        menu:
            Girl.voice "[main_line]"
            "Do you want to make out?":
                if Girl.remaining_Actions:
                    call start_Action(Girl, "kiss")
                else:
                    call out_of_Actions_lines(Girl)

                    $ having_sex = False
            "Could I touch you?":
                if Girl.remaining_Actions:
                    if Girl in [EmmaX, StormX]:
                        $ Girl.change_face("sly")
                    else:
                        $ Girl.mouth = "smile"

                    menu:
                        Girl.voice "[fondle_line]"
                        "Your thighs?" if Girl.remaining_Actions:
                            call start_Action(Girl, "fondle_thighs")
                        "Your breasts?":
                            call start_Action(Girl, "fondle_breasts")
                        "Suck your nipples?" if Girl.remaining_Actions and Girl.permanent_History["suck_breasts"]:
                            call start_Action(Girl, "suck_breasts")
                        "Your pussy?" if Girl.remaining_Actions:
                            call start_Action(Girl, "fondle_pussy")
                        "Eat your pussy?" if Girl.remaining_Actions and Girl.permanent_History["eat_pussy"]:
                            call start_Action(Girl, "eat_pussy")
                        "Your ass?":
                            call start_Action(Girl, "fondle_ass")
                        "Eat your ass?" if Girl.remaining_Actions and Girl.permanent_History["eat_ass"]:
                            call start_Action(Girl, "eat_ass")
                        "Maybe something else.":
                            pass
                else:
                    call out_of_Actions_lines(Girl)

                    $ having_sex = False
            "Could you take care of something for me?" if Player.semen:
                if Player.semen and Girl.remaining_Actions:
                    menu:
                        Girl.voice "[handjob_line]"
                        "Could you give me a handjob?":
                            call start_Action(Girl, "handjob")
                        "Could use your feet?":
                            call start_Action(Girl, "footjob")
                        "Could you give me a titjob?":
                            call start_Action(Girl, "titjob")
                        "Could you suck my cock?":
                            call start_Action(Girl, "blowjob")
                        "Never mind [[something else]":
                            pass
                elif Player.semen and not Girl.remaining_Actions:
                    call out_of_Actions_lines(Girl)

                    $ having_sex = False
                else:
                    "You really don't have it in you, maybe take a break."

                    $ having_sex = False
            "Could we maybe. . . ?":
                if Girl.remaining_Actions:
                    menu:
                        Girl.voice "[main_line]"
                        "Come over here, I've got something in mind. . .":
                            if Player.semen:
                                call start_Action(Girl, "hotdog")
                            else:
                                "The spirit is apparently willing, but the flesh is spongy and bruised."

                                $ having_sex = False
                        "Fuck your pussy.":
                            if Player.semen:
                                call start_Action(Girl, "sex")
                            else:
                                "The spirit is apparently willing, but the flesh is spongy and bruised."

                                $ having_sex = False
                        "Fuck your ass.":
                            if Player.semen:
                                call start_Action(Girl, "anal")
                            else:
                                "The spirit is apparently willing, but the flesh is spongy and bruised."

                                $ having_sex = False
                        "How about some toys? [[Pussy]":
                            call dildo_check(Girl)

                            if _return == "found":
                                call start_Action(Girl, "dildo_pussy")
                        "How about some toys? [[Anal]":
                            call dildo_check(Girl)

                            if _return == "found":
                                call start_Action(Girl, "dildo_ass")
                        "Maybe something else.":
                            pass
                else:
                    call out_of_Actions_lines(Girl)

                    $ having_sex = False
            "Cheat menu" if config.developer:
                call sex_cheats(Girl)
            "I'm done.":
                call generic_exit_sex_menu_lines(Girl)

                $ having_sex = False

        if _return == "stop":
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
        "Other options":
            menu:
                # "Offhand action":
                #     if Girl.remaining_Actions:
                #         call set_secondary_Action(Girl)
                #
                #         if _return == "stop":
                #             return [None, "stop"]
                #
                #         if Player.secondary_Action:
                #              $ Girl.remaining_Actions -= 1
                #     else:
                #         call tired_lines(Girl, "kiss")
                "Shift primary action":
                    if Girl.remaining_Actions:
                        menu:
                            "Move a hand to her thighs. . .":
                                return ["fondle_thighs", "auto"]
                            "Move a hand to her breasts. . .":
                                return ["fondle_breasts", "auto"]
                            "Continue":
                                pass
                    else:
                        call tired_lines(Girl, "kiss")
                "Continue":
                    pass
        "Back to Sex Menu":
            ch_p "Let's try something else."

            return [None, "switch"]
        "End scene":
            ch_p "Let's stop for now."

            return [None, "stop"]

    return [None, "continue"]

label masturbation_menu(Girl):
    menu:
        "Keep watching":
            pass
        "Jump in":
            return "join"
        "Slap her ass":
            call slap_ass (Girl)

            $ counter += 1
            $ round -= 1
        "Back to Sex Menu":
            ch_p "Let's try something else."

            return "switch"
        "End scene":
            ch_p "Let's stop for now."

            return "stop"

    return "continue"

label fondle_menu(Girl, Action_type):
    menu:
        "Keep going. . .":
            pass
        "I want to stick a finger in. . ." if Action_type == "fondle_pussy":
            if Girl.permanent_History["finger_pussy"]:
                return ["finger_pussy", "auto"]
            else:
                menu:
                    "Ask her first":
                        return ["finger_pussy", "shift"]
                    "Don't ask first [[just stick it in]":
                        return ["finger_pussy", "auto"]
        "Pull back a bit. . ." if Action_type == "fondle_pussy":
            return ["fondle_thighs", "pullback"]
        "Pull out. . ." if Action_type == "finger_pussy":
            return ["fondle_pussy", "pullback"]
        "Slap her ass":
            call slap_ass(Girl)

            $ counter += 1
            $ round -= 1
        "Change view":
            call shift_view(Girl, "menu")
        "Other options":
            menu:
                # "Offhand action":
                #     if Girl.remaining_Actions:
                #         call set_secondary_Action(Girl)
                #
                #         if _return == "stop":
                #             return [None, "stop"]
                #
                #         if Player.secondary_Action:
                #             $ Girl.remaining_Actions -= 1
                #     else:
                #         call tired_lines(Girl, Action_type)
                "Shift primary action":
                    if Girl.remaining_Actions:
                        menu:
                            "Can I go a little deeper?" if Action_type == "fondle_thighs":
                                return ["fondle_pussy", "shift"]
                            "Shift your hands a bit higher without asking" if Action_type == "fondle_thighs":
                                return ["fondle_pussy", "auto"]
                            "I want to finger you." if Action_type == "fondle_pussy":
                                return ["finger_pussy", "shift"]
                            "Just slip a finger in." if Action_type == "fondle_pussy":
                                return ["finger_pussy", "auto"]
                            "Ask to suck on them." if Action_type == "fondle_breasts":
                                return ["suck_breasts", "shift"]
                            "Just suck on them without asking." if Action_type == "fondle_breasts":
                                return ["suck_breasts", "auto"]
                            "Pull back to fondling." if Action_type = = "suck_breasts":
                                return ["fondle_breasts", "pullback"]
                            "I want to lick your pussy." if Action_type in ["fondle_pussy", "finger_pussy"]:
                                return ["eat_pussy", "shift"]
                            "Just start licking." if Action_type in ["fondle_pussy", "finger_pussy"]:
                                return ["eat_pussy", "auto"]
                            "Pull back to the thighs." if Action_type in ["fondle_pussy"]:
                                return ["fondle_thighs", "auto"]
                            "I want to stick a dildo in." if Action_type in ["fondle_pussy", "finger_pussy", "eat_pussy"]:
                                call dildo_check(Girl)

                                if _return == "found":
                                    return ["dildo_pussy", "shift"]
                            "Pull out and start rubbing again." if Action_type in ["finger_pussy"]:
                                return ["fondle_pussy", "pullback"]
                            "I want to stick a finger in." if Action_type in ["fondle_ass", "eat_ass"]:
                                return ["finger_ass", "shift"]
                            "Just stick a finger in without asking." if Action_type in ["fondle_ass", "eat_ass"]:
                                return ["finger_ass", "auto"]
                            "I want to lick your asshole." if Action_type in ["fondle_ass", "finger_ass"]:
                                return ["eat_ass", "shift"]
                            "Just start licking." if Action_type in ["fondle_ass", "finger_ass"]:
                                return ["eat_ass", "auto"]
                            "I want to stick a dildo in." if Action_type in ["fondle_ass", "finger_ass", "eat_ass"]:
                                call dildo_check(Girl)

                                if _return == "found":
                                    return ["dildo_ass", "shift"]
                            "Pull out and start rubbing again." if Action_type in ["finger_ass"]:
                                return ["fondle_ass", "pullback"]
                            "Switch to fondling." if Action_type = = "eat_ass":
                                return ["fondle_ass", "pullback"]
                            "Continue":
                                pass
                    else:
                        call tired_lines(Girl, Action_type)
                "Show her feet" if not show_feet:
                    $ show_feet = True
                "Hide her feet" if show_feet:
                    $ show_feet = False
                "Continue":
                    pass
        "Back to Sex Menu":
            ch_p "Let's try something else."

            return [None, "switch"]
        "End scene":
            ch_p "Let's stop for now."

            return [None, "stop"]

    return [None, "continue"]

label handjob_menu(Girl, Action_type):
    menu:
        "Keep going. . ." if Girl.primary_Action.speed:
            pass
        "Start moving? . ." if Action_type in ["handjob", "footjob", "titjob"] and not Girl.primary_Action.speed:
            $ Girl.primary_Action.speed = 1
        "Speed up. . ." if Action_type in ["handjob", "footjob", "titjob"] and Girl.primary_Action.speed < 2:
            $ Girl.primary_Action.speed = 2
        "Speed up. . . (locked)" if Action_type in ["handjob", "footjob", "titjob"] and Girl.primary_Action.speed > 1:
            pass
        "Slow Down. . ." if Action_type in ["handjob", "footjob", "titjob"] and Girl.primary_Action.speed:
            $ Girl.primary_Action.speed -= 1

            "You ask her to slow it down a bit."
        "Slow Down. . . (locked)" if Action_type in ["handjob", "footjob", "titjob"] and not Girl.primary_Action.speed:
            pass
        "Lick it. . ." if Action_type == "blowjob" and Girl.primary_Action.speed != 1:
            $ Girl.primary_Action.speed = 1
        "Lick it. . . (locked)" if Action_type == "blowjob" and Girl.primary_Action.speed == 1:
            pass
        "Just the head. . ." if Action_type == "blowjob" and Girl.primary_Action.speed != 2:
            $ Girl.primary_Action.speed = 2
        "Just the head. . . (locked)" if Action_type == "blowjob" and Girl.primary_Action.speed == 2:
            pass
        "Suck on it." if Action_type == "blowjob" and Girl.primary_Action.speed != 3:
            $ Girl.primary_Action.speed = 3
        "Suck on it. (locked)" if Action_type == "blowjob" and Girl.primary_Action.speed == 3:
            pass
        "Take it deeper." if Action_type == "blowjob" and Girl.primary_Action.speed != 4:
            $ Girl.primary_Action.speed = 4
        "Take it deeper. (locked)" if Action_type == "blowjob" and Girl.primary_Action.speed == 4:
            pass
        "Set your own pace. . ." if Action_type == "blowjob":
            "[Girl.name] hums contentedly."

            $ D20 = renpy.random.randint(1, 20)

            if Girl.permanent_History["blowjob"] < 5:
                $ D20 -= 10
            elif Girl.permanent_History["blowjob"] < 10:
                $ D20 -= 5

            if D20 > 15:
                $ Girl.primary_Action.speed = 4
            elif D20 > 10:
                $ Girl.primary_Action.speed = 3
            elif D20 > 5:
                $ Girl.primary_Action.speed = 2
            else:
                $ Girl.primary_Action.speed = 1
        "Slap her ass. . ." if Action_type in dildo_Action_types:
            call slap_ass(Girl)

            $ counter += 1
            $ round -= 1
        "Turn her around." if Action_type == "footjob":
            if renpy.showing(Girl.tag + "_sprite sex"):
                call show_doggy(Girl)
            elif renpy.showing(Girl.tag + "_sprite doggy"):
                call show_sex(Girl)
        "Change view" if Action_type in dildo_Action_types:
            call shift_view(Girl, "menu")
        "Other options":
                menu:
                    # "Offhand action":
                    #     if Girl.remaining_Actions:
                    #         call set_secondary_Action(Girl)
                    #
                    #         if _return == "stop":
                    #             return [None, "stop"]
                    #
                    #         if Player.secondary_Action:
                    #             $ Girl.remaining_Actions -= 1
                    #     else:
                    #         call tired_lines(Girl, Action_type)
                    "Shift primary action":
                        if Girl.remaining_Actions:
                            menu:
                                "How about a handy?" if Action_type in ["footjob", "titjob", "blowjob"]:
                                    if Girl.remaining_Actions:
                                        return ["handjob", "shift"]
                                    else:
                                        call tired_lines(Girl, Action_type)
                                "How about a footjob?" if Action_type in ["handjob", "titjob", "blowjob"]:
                                    if Girl.remaining_Actions:
                                        return ["footjob", "shift"]
                                    else:
                                        call tired_lines(Girl, Action_type)
                                "How about a titjob?" if Action_type in ["handjob", "footjob", "blowjob"]:
                                    if Girl.remaining_Actions:
                                        return ["titjob", "shift"]
                                    else:
                                        call tired_lines(Girl, Action_type)
                                "How about a blowjob?" if Action_type in ["handjob", "footjob", "titjob"]:
                                    if Girl.remaining_Actions:
                                        return ["blowjob", "shift"]
                                    else:
                                        call tired_lines(Girl, Action_type)
                                "I want to stick a finger in her ass." if Action_type == "dildo_pussy":
                                    if Girl.remaining_Actions:
                                        return ["finger_ass", "shift"]
                                    else:
                                        call tired_lines(Girl, Action_type)
                                "Just stick a finger in her ass without asking." if Action_type == "dildo_pussy":
                                    if Girl.remaining_Actions:
                                        return ["finger_ass", "auto"]
                                    else:
                                        call tired_lines(Girl, Action_type)
                                "I want to shift the dildo to her ass." if Action_type == "dildo_pussy":
                                    if Girl.remaining_Actions:
                                        return ["dildo_ass", "shift"]
                                    else:
                                        call tired_lines(Girl, Action_type)
                                "I want to stick a finger in her pussy." if Action_type == "dildo_ass":
                                    if Girl.remaining_Actions:
                                        return ["finger_pussy", "shift"]
                                    else:
                                        call tired_lines(Girl, Action_type)
                                "Just stick a finger in her pussy without asking." if Action_type == "dildo_ass":
                                    if Girl.remaining_Actions:
                                        return ["finger_pussy", "auto"]
                                    else:
                                        call tired_lines(Girl, Action_type)
                                "I want to shift the dildo to her pussy." if Action_type == "dildo_ass":
                                    if Girl.remaining_Actions:
                                        return ["dildo_pussy", "shift"]
                                    else:
                                        call tired_lines(Girl, Action_type)
                                "Never mind":
                                    pass
                        else:
                            call tired_lines(Girl, Action_type)
                    "Never mind":
                        pass
        "Back to Sex Menu":
            ch_p "Let's try something else."

            return [None, "switch"]
        "End scene":
            ch_p "Let's stop for now."

            return [None, "stop"]

    return [None, "continue"]

label sex_menu(Girl, Action_type):
    menu:
        "Keep going. . ." if Player.primary_Action.speed:
            pass
        "Keep going. . . (locked)" if not Player.primary_Action.speed:
            pass
        "Start moving? . ." if not Player.primary_Action.speed:
            $ Player.primary_Action.speed = 1
        "Speed up. . ." if 0 < Player.primary_Action.speed < 3:
            $ Player.primary_Action.speed += 1
        "Speed up. . . (locked)" if Player.primary_Action.speed > 2:
            pass
        "Slow down. . ." if Player.primary_Action.speed:
            $ Player.primary_Action.speed -= 1
        "Slow down. . . (locked)" if not Player.primary_Action.speed:
            pass
        "Slap her ass":
            call slap_ass(Girl)

            $ counter += 1
            $ round -= 1
        "Turn her around":
            if renpy.showing(Girl.tag + "_sprite sex"):
                call show_doggy(Girl)
            elif renpy.showing(Girl.tag + "_sprite doggy"):
                call show_sex(Girl)
        "Other options":
            menu:
                # "Offhand action":
                #     if Girl.remaining_Actions:
                #         call set_secondary_Action(Girl)
                #
                #         if _return == "stop":
                #             return [None, "stop"]
                #
                #         if Player.secondary_Action:
                #             $ Girl.remaining_Actions -= 1
                #     else:
                #         call tired_lines(Girl, Action_type)
                "Shift primary action":
                    if Girl.remaining_Actions:
                        menu:
                            "How about sex?" if Action_type != "sex":
                                return ["sex", "shift"]
                            "Just stick it in her pussy" if Action_type != "sex":
                                return ["sex", "auto"]
                            "How about anal?" if Action_type != "anal":
                                return ["anal", "shift"]
                            "Just stick it in her ass" if Action_type != "anal":
                                return ["anal", "auto"]
                            "Pull back to hotdog her" if Action_type != "hotdog":
                                return ["hotdog", "pullback"]
                            "Continue":
                                pass
                    else:
                        call tired_lines(Girl, Action_type)
                "Show her feet" if not show_feet:
                    $ show_feet = True
                "Hide her feet" if show_feet:
                    $ show_feet = False
                "Continued":
                    pass
        "Back to Sex Menu":
            ch_p "Let's try something else."

            return [None, "switch"]
        "End scene":
            ch_p "Let's stop for now."

            return [None, "stop"]

    return [None, "continue"]



















label begging_menu(Girl, Action_type):
    menu:
        extend ""
        "Sorry, never mind.":
            if "no_" + Action_type not in Girl.daily_history:
                $ Girl.change_face("bemused")

                call sorry_never_mind_lines(Girl, Action_type)

                $ Girl.recent_history.append("no_" + Action_type)
                $ Girl.daily_history.append("no_" + Action_type)
        "Maybe later?" if "no_" + Action_type not in Girl.daily_history:
            if Action_type == "masturbation":
                $ Girl.change_face("sexy", 1)
            else:
                $ Girl.change_face("sexy")

            if Action_type == "fondle_breasts" and Girl not in [LauraX, JubesX]:
                "She re-adjusts her cleavage."

            call maybe_later_lines(Girl, Action_type)

            if Action_type in ["fondle_thighs", "fondle_breasts", "suck_breasts"]:
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "inhibition", 2)

                if Action_type in breast_Action_types:
                    call change_Girl_stat(Girl, "love", 1)
            elif Action_type in ["masturbation", "fondle_pussy"]:
                call change_Girl_stat(Girl, "love", 2)
                call change_Girl_stat(Girl, "inhibition", 2)
            elif Action_type in ["fondle_ass"]:
                call change_Girl_stat(Girl, "love", 2)
                call change_Girl_stat(Girl, "inhibition", 2)
            elif Action_type in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal"]:
                call change_Girl_stat(Girl, "love", 2)
                call change_Girl_stat(Girl, "inhibition", 2)
            elif Action_type in ["hotdog"]:
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "inhibition", 1)

            $ Girl.recent_history.append("no_" + Action_type)
            $ Girl.daily_history.append("no_" + Action_type)
        "You look like you could use it. . ." if Action_type == "masturbation":
            if approval:
                $ Girl.change_face("sexy")
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "inhibition", 3)
                call change_Girl_stat(Girl, "inhibition", 2)

                call begging_lines(Girl, Action_type)

                return Action_type
            else:
                call action_rejected(Girl, Action_type)
        "Come on, please?" if Action_type in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "blowjob"]:
            if approval:
                $ Girl.change_face("sexy")

                if Action_type == "fondle_thighs":
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "inhibition", 1)
                    call change_Girl_stat(Girl, "inhibition", 2)
                elif Action_type in ["fondle_breasts", "suck_breasts"]:
                    if Girl != LauraX:
                        call change_Girl_stat(Girl, "obedience", 1)

                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "inhibition", 3)
                    call change_Girl_stat(Girl, "inhibition", 2)
                elif Action_type in ["fondle_pussy", "blowjob"]:
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "inhibition", 3)
                    call change_Girl_stat(Girl, "inhibition", 2)

                call begging_lines(Girl, Action_type)

                return Action_type
            else:
                if Action_type in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy"]:
                    $ Girl.change_face("sexy")

                    call please_not_good_enough_lines(Girl, Action_type)
                elif Action_type in ["blowjob"]:
                    if approval_check(Girl, 1100, taboo_modifier = 3): # 110, 125, 140, taboo -120(230)             Handy instead?
                        call change_Girl_stat(Girl, "inhibition", 1)
                        call change_Girl_stat(Girl, "inhibition", 3)
                        $ Girl.change_face("confused", 1)

                        call maybe_handjob_instead_lines(Girl)

                        menu:
                            extend ""
                            "Sure, that's fine.":
                                call change_Girl_stat(Girl, "love", 2)
                                call change_Girl_stat(Girl, "inhibition", 1)
                                call change_Girl_stat(Girl, "obedience", 1)

                                return "handjob"
                            "Nah, if it's not a BJ, forget it.":
                                call change_Girl_stat(Girl, "love", -2)

                                call alternative_rejected_lines(Girl)

                                call change_Girl_stat(Girl, "obedience", 2)

                $ Girl.recent_history.append("no_" + Action_type)
                $ Girl.daily_history.append("no_" + Action_type)
        "I'm sure I can convince you later. . ." if Action_type in ["eat_pussy", "eat_ass"] and "no_" + Action_type not in Girl.daily_history:
            $ Girl.change_face("sexy")

            call maybe_later_lines(Girl, Action_type)

            call change_Girl_stat(Girl, "love", 2)
            call change_Girl_stat(Girl, "inhibition", 2)

            $ Girl.recent_history.append("no_" + Action_type)
            $ Girl.daily_history.append("no_" + Action_type)
        "I think you'd really enjoy it. . ." if Action_type in ["eat_pussy", "eat_ass"]:
            if approval:
                $ Girl.change_face("sexy")
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "obedience", 2)

                call trying_to_convince_lines(Girl, Action_type)

                call change_Girl_stat(Girl, "inhibition", 3)
                call change_Girl_stat(Girl, "inhibition", 2)

                return Action_type
            else:
                $ Girl.change_face("sexy")

                call unconvinced_lines(Girl, Action_type)

                $ Girl.recent_history.append("no_" + Action_type)
                $ Girl.daily_history.append("no_" + Action_type)
        "Just one good squeeze?" if Action_type == "fondle_ass":
            if approval:
                $ Girl.change_face("sexy")
                call change_Girl_stat(Girl, "obedience", 1)
                call change_Girl_stat(Girl, "obedience", 2)

                call begging_lines(Girl, Action_type)

                call change_Girl_stat(Girl, "inhibition", 1)
                call change_Girl_stat(Girl, "inhibition", 2)

                return Action_type
            else:
                $ Girl.change_face("sexy")

                call unconvinced_lines(Girl, Action_type)

                $ Girl.recent_history.append("no_" + Action_type)
                $ Girl.daily_history.append("no_" + Action_type)
        "I'd really appreciate it. . ." if Action_type in ["handjob"]:
            if approval:
                $ Girl.change_face("sexy")
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "inhibition", 3)
                call change_Girl_stat(Girl, "inhibition", 2)

                call begging_lines(Girl, Action_type)

                return Action_type
            else:
                call action_rejected(Girl, Action_type)
        "I think this could be fun for both of us. . ." if Action_type in ["titjob"]:
            if approval:
                $ Girl.change_face("sexy")
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "inhibition", 3)
                call change_Girl_stat(Girl, "inhibition", 2)

                call trying_to_convince_lines(Girl, Action_type)

                return Action_type
            else:
                $ approval = approval_check(Girl, 1100, taboo_modifier = 3) # 110, 125, 140, taboo -120(230)             Handy instead?

                $ blowjob_rejected = False

                if approval >= 2:
                    call change_Girl_stat(Girl, "inhibition", 1)
                    call change_Girl_stat(Girl, "inhibition", 3)
                    $ Girl.change_face("confused", 1)

                    call maybe_blowjob_instead_lines(Girl)

                    menu:
                        extend ""
                        "Ok, get down there.":
                            call change_Girl_stat(Girl, "love", 2)
                            call change_Girl_stat(Girl, "inhibition", 1)
                            call change_Girl_stat(Girl, "obedience", 1)

                            return "blowjob"
                        "Nah, it's all about dem titties.":
                            $ blowjob_rejected = True

                    call change_Girl_stat(Girl, "love", -2)

                    call alternative_rejected_lines(Girl)

                    call change_Girl_stat(Girl, "obedience", 2)
                elif approval:
                    call change_Girl_stat(Girl, "inhibition", 1)
                    call change_Girl_stat(Girl, "inhibition", 3)
                    $ Girl.change_face("confused", 1)

                    call maybe_handjob_instead_lines(Girl)

                    menu:
                        extend ""
                        "Sure, that's fine.":
                            call change_Girl_stat(Girl, "love", 2)
                            call change_Girl_stat(Girl, "inhibition", 1)
                            call change_Girl_stat(Girl, "obedience", 1)

                            return "handjob"
                        "Seriously, titties." if blowjob_rejected:
                            pass
                        "Nah, it's all about dem titties." if not blowjob_rejected:
                            pass

                    call change_Girl_stat(Girl, "love", -2)

                    call alternative_rejected_lines(Girl)

                    call change_Girl_stat(Girl, "obedience", 2)

                $ Girl.recent_history.append("no_" + Action_type)
                $ Girl.daily_history.append("no_" + Action_type)
        "I think you'd like it. . ." if Action_type in dildo_Action_types:
            if approval:
                $ Girl.change_face("sexy")
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "inhibition", 3)
                call change_Girl_stat(Girl, "inhibition", 2)

                call trying_to_convince_lines(Girl, Action_type)

                return Action_type
            else:
                call action_rejected(Girl, Action_type)
        "I think you'd enjoy it as much as I would. . ." if Action_type in ["sex"]:
            if approval:
                $ Girl.change_face("sexy")
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "inhibition", 3)
                call change_Girl_stat(Girl, "inhibition", 2)

                call trying_to_convince_lines(Girl, Action_type)

                return Action_type
            else:
                call action_rejected(Girl, Action_type)
        "I bet it would feel really good. . ." if Action_type in ["anal"]:
            if approval:
                $ Girl.change_face("sexy")
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "inhibition", 3)
                call change_Girl_stat(Girl, "inhibition", 2)

                call trying_to_convince_lines(Girl, Action_type)

                return Action_type
            else:
                call action_rejected(Girl, Action_type)
        "You might like it. . ." if Action_type in ["hotdog"]:
            if approval:
                $ Girl.change_face("sexy")
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "inhibition", 2)

                call trying_to_convince_lines(Girl, Action_type)

                return Action_type
            else:
                call action_rejected(Girl, Action_type)
        "Just get at it already." if Action_type == "masturbation":
            call forced_Action(Girl, Action_type)

            if _return == "accepted":
                return Action_type
        "[[Start caressing her thigh anyway]" if Action_type == "fondle_thighs":
            call forced_Action(Girl, Action_type)

            if _return == "accepted":
                return Action_type
        "[[Grab her chest anyway]" if Action_type == "fondle_breasts":
            call forced_Action(Girl, Action_type)

            if _return == "accepted":
                return Action_type
        "[[Start sucking anyway]" if Action_type == "suck_breasts":
            call forced_Action(Girl, Action_type)

            if _return == "accepted":
                return Action_type
        "[[Start fondling anyway]" if Action_type in ["fondle_pussy", "fondle_ass"]:
            call forced_Action(Girl, Action_type)

            if _return == "accepted":
                return Action_type
        "[[Get in there anyway]" if Action_type == "eat_pussy":
            call forced_Action(Girl, Action_type)

            if _return == "accepted":
                return Action_type
        "[[Slide a finger in anyway]" if Action_type == "finger_ass":
            call forced_Action(Girl, Action_type)

            if _return == "accepted":
                return Action_type
        "[[Start licking anyway]" if Action_type in ["eat_pussy", "eat_ass"]:
            call forced_Action(Girl, Action_type)

            if _return == "accepted":
                return Action_type
        "Come on, get to work." if Action_type in ["handjob", "footjob"]:                                               # Pressured into it
            call forced_Action(Girl, Action_type)

            if _return == "accepted":
                return Action_type
        "Come on, let me fuck those titties, [Girl.petname]" if Action_type in ["titjob"]:
            $ Girl.name_check() #checks reaction to petname

            call forced_Action(Girl, Action_type)

            if _return == "accepted":
                return Action_type
        "Suck it, [Girl.petname]" if Action_type in ["blowjob"]:                                               # Pressured into it
            $ Girl.name_check() #checks reaction to petname

            call forced_Action(Girl, Action_type)

            if _return == "accepted":
                return Action_type
        "[[Press it against her.]]" if Action_type in dildo_Action_types:
            call forced_Action(Girl, Action_type)

            if _return == "accepted":
                return Action_type
        "Bend over." if Action_type in ["sex", "anal", "hotdog"]:
            call forced_Action(Girl, Action_type)

            if _return == "accepted":
                return Action_type

    return "rejected"

label try_something_else_menu(Girl, Action_type):
    menu:
        extend ""
        "How about a handy?" if Action_type in ["footjob", "titjob", "blowjob", "sex", "anal", "hotdog"] and Girl.remaining_Actions:
            return ["handjob", "shift"]
        "How about a footjob?" if Action_type in ["handjob", "titjob", "blowjob", "sex", "anal", "hotdog"] and Girl.remaining_Actions:
            return ["footjob", "shift"]
        "How about a titjob?" if Action_type in ["handjob", "footjob", "blowjob", "sex", "anal", "hotdog"] and Girl.remaining_Actions:
            return ["titjob", "shift"]
        "How about a blowjob?" if Action_type in ["handjob", "footjob", "titjob", "sex", "anal", "hotdog"] and Girl.remaining_Actions:
            if Action_type != "anal":
                return ["blowjob", "shift"]
            else:
                if Girl.permanent_History["anal"] >= 5 and Girl.permanent_History["blowjob"] >= 10 and Girl.SEXP >= 50:
                    return ["blowjob", "shift"]
                else:
                    call no_ass_to_mouth_lines(Girl, Action_type)

                    return ["handjob", "shift"]
        "Finish up." if Action_type in ["handjob", "footjob", "titjob", "blowjob", "sex", "anal", "hotdog"] and Player.focusing:
            "You release your concentration. . ."

            $ Player.focusing = 0
            $ Player.climax += 15
        "No, get back down there." if Action_type in ["handjob", "footjob", "titjob", "blowjob"]:
            if approval_check(Girl, 1200) or approval_check(Girl, 500, "O"):
                call change_Girl_stat(Girl, "love", -5)
                call change_Girl_stat(Girl, "obedience", 3)
                call change_Girl_stat(Girl, "obedience", 2)

                "She grumbles but keeps going."
            else:
                $ Girl.change_face("angry", 1)

                call show_full_body(Girl)

                "She scowls at you, drops your cock and pulls back."

                call this_is_boring_lines(Girl, Action_type)

                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "obedience", 1)
                call change_Girl_stat(Girl, "obedience", 1)
                $ Girl.add_word(1, "angry", "angry")

                return [None, "stop"]
        "Finish up.":
            "You let go. . ."

            return [None, "switch"]
        "Let's try something else.":
            return [None, "switch"]
        "No, this is fun.":
            if approval_check(Girl, 1200) or approval_check(Girl, 500, "O"):
                call change_Girl_stat(Girl, "love", -5)
                call change_Girl_stat(Girl, "obedience", 3)
                call change_Girl_stat(Girl, "obedience", 2)

                "She grumbles but lets you keep going."
            else:
                $ Girl.change_face("angry", 1)

                call show_full_body(Girl)

                "She scowls at you and pulls back."

                call this_is_boring_lines(Girl, Action_type)

                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "obedience", 1)
                call change_Girl_stat(Girl, "obedience", 1)
                $ Girl.add_word(1, "angry", "angry")

                return [None, "stop"]

    return [None, "continue"]

label girl_unsatisfied_menu(Girl, Action_type):
    if Action_type in sex_actions:
        call not_ready_to_stop_narrations(Girl, Action_type)

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

        if Action_type == "masturbation":
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

label what_do_you_think_youre_doing_menu(Girl, Action_type):
    menu:
        extend ""
        "Sorry, sorry! Never mind.":
            if approval:
                $ Girl.change_face("sexy", 1)
                call change_Girl_stat(Girl, "obedience", 3)
                call change_Girl_stat(Girl, "inhibition", 3)
                call change_Girl_stat(Girl, "inhibition", 1)

                call since_you_are_so_nice_lines(Girl, Action_type)

                return "accepted"

            "You pull back before you really get it in."

            $ Girl.change_face("bemused", 1)

            call pull_back_before_get_in_lines(Girl, Action_type)
        "Just playing with my favorite toys." if Action_type in dildo_actions:
            call change_Girl_stat(Girl, "love", 1)
            call change_Girl_stat(Girl, "love", -10)

            "You press it inside some more."

            call change_Girl_stat(Girl, "obedience", 3)
            call change_Girl_stat(Girl, "inhibition", 3)

            if not approval_check(Girl, 700, "O", taboo_modifier = 1): #checks if obedience is 700+
                $ Girl.change_face("angry")

                call were_done_here_lines(Girl, Action_type)

                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "obedience", 3)

                call show_full_body(Girl)

                $ Girl.recent_history.append("angry")
                $ Girl.daily_history.append("angry")
            else:
                $ Girl.change_face("sad")

                call knows_her_place_lines(Girl, Action_type)

                return "accepted"
        "Just fucking." if Action_type in ["sex", "anal"]:
            call change_Girl_stat(Girl, "love", 1)
            call change_Girl_stat(Girl, "love", -10)

            if Action_type == "sex":
                "You press inside some more."
            elif Action_type == "anal":
                "You press into her."

            call change_Girl_stat(Girl, "obedience", 3)
            call change_Girl_stat(Girl, "inhibition", 3)

            if not approval_check(Girl, 700, "O", taboo_modifier = 1):   #checks if obedience is 700+
                $ Girl.change_face("angry")

                call were_done_here_lines(Girl, Action_type)

                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "obedience", 3)

                call show_full_body(Girl)

                $ Girl.recent_history.append("angry")
                $ Girl.daily_history.append("angry")
            else:
                $ Girl.change_face("sad")

                call knows_her_place_lines(Girl, Action_type)

                return "accepted"
        "You'll see." if Action_type == "hotdog":
            call change_Girl_stat(Girl, "love", 1)
            call change_Girl_stat(Girl, "love", -8)

            "You grind against her asscrack."

            call change_Girl_stat(Girl, "obedience", 3)
            call change_Girl_stat(Girl, "inhibition", 3)

            if not approval_check(Girl, 500, "O", taboo_modifier = 1): #checks if obedience is 700+
                $ Girl.change_face("angry")

                call were_done_here_lines(Girl, Action_type)

                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "obedience", 3)

                call show_full_body(Girl)

                $ Girl.recent_history.append("angry")
                $ Girl.daily_history.append("angry")
            else:
                $ Girl.change_face("sad")

                call knows_her_place_lines(Girl, Action_type)

                return "accepted"

    return "rejected"
