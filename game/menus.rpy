label enter_main_sex_menu:
    if Player.focused_girl == EmmaX:
        if "classcaught" not in Player.focused_girl.History:
            ch_e "I can't imagine being a part of something so. . . tawdry."

            return
        if "three" not in Player.focused_girl.History and not AloneCheck(Player.focused_girl):
            call expression Player.focused_girl.Tag + "_ThreeCheck"
        if Taboo > 20 and "taboo" not in Player.focused_girl.History:
            call expression Player.focused_girl.Tag + "_Taboo_Talk"

            if bg_current == "bg_classroom" or bg_current in PersonalRooms and AloneCheck(Player.focused_girl):
                ch_p "We could just lock the door, right?"
                ch_e "We certainly could. . ."
                "[Player.focused_girl.name] walks to the door and locks it behind her."

                $ Player.Traits.append("locked")

                call Taboo_Level
            else:
                return

    call Shift_Focus(Player.focused_girl)

    $ primary_action = 0
    $ offhand_action = 0
    $ girl_offhand_action = 0
    $ action_context = 0

    call hide_girl(Player.focused_girl, sprite = True)

    $ Player.focused_girl.ArmPose = 1

    call set_the_scene(1,0,0,0,1)

    if Player.focused_girl in [EmmaX, StormX]:
        if "detention" in Player.focused_girl.recent_history:
            $ temp_modifier = 20 if temp_modifier <= 20 else temp_modifier

    if not Player.Semen:
        "You're a little out of juice at the moment, you might want to wait a bit."
    if Player.Focus >= 95:
        "You're practically buzzing, the slightest breeze could set you off."
    if not Player.focused_girl.Action:
        "[Player.focused_girl.name]'s looking a bit tired out, maybe let her rest a bit."

    if "caught" in Player.focused_girl.recent_history or "angry" in Player.focused_girl.recent_history:
        if Player.focused_girl.Loc == bg_current:
            call angry_lines(Player.focused_girl)

        $ Player.focused_girl.OutfitChange()
        $ Player.focused_girl.DrainWord("caught",1,0)

        return

    if Round < 5:
        call take_a_breather_lines(Player.focused_girl)

        return

    $ main_line = None
    $ fondle_line = None
    $ handjob_line = None
    $ show_line = None

    call Girl_sex_menu(Player.focused_girl)

    if _return:
        return

    if Player.focused_girl.Loc != bg_current:
        call set_the_scene
        call Trig_Reset

        return

    if not multi_action:
        call set_the_scene

        call thats_it_for_now_lines(Player.focused_girl)

        $ Player.focused_girl.OCount = 0

        call Trig_Reset

        return

    call GirlsAngry
    jump enter_main_sex_menu

label Girl_sex_menu(Girl):
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
            if Girl.Action:
                call kiss(Girl)
            else:
                call out_of_action_lines(Girl)
        "Could I touch you?":
            if Girl.Action:
                if Girl in [EmmaX, StormX]:
                    $ Girl.change_face("sly")
                else:
                    $ Girl.Mouth = "smile"

                menu:
                    Girl.voice "[fondle_line]"
                    "Could I give you a massage?":
                        call Massage(Girl)
                    "Your breasts?":
                        call fondle_breasts(Girl)
                    "Suck your breasts?" if Girl.Action and Girl.SuckB:
                        call suck_breasts(Girl)
                    "Your thighs?" if Girl.Action:
                        call fondle_thighs(Girl)
                    "Your pussy?" if Girl.Action:
                        call fondle_pussy(Girl)
                    "Lick your pussy?" if Girl.Action and Girl.LickP:
                        call lick_pussy(Girl)
                    "Your Ass?":
                        call fondle_ass(Girl)
                    "Eat your ass?" if Girl.Action and Girl.LickA:
                        call lick_ass(Girl)
                    "Never mind [[something else]":
                        jump main_sex_menu
            else:
                call out_of_action_lines(Girl)
        "Could you take care of something for me? [[Your dick, you mean your dick]":
            if Player.Semen and Girl.Action:
                menu:
                    Girl.voice "[handjob_line]"
                    "Could you give me a handjob?":
                        call handjob(Girl)
                    "Could you give me a titjob?":
                        call titjob(Girl)
                    "Could you suck my cock?":
                        call blowjob(Girl)
                    "Could use your feet?":
                        call footjob(Girl)
                    "Never mind [[something else]":
                        jump main_sex_menu
            elif not Girl.Action:
                call out_of_action_lines(Girl)
            else:
                "You really don't have it in you, maybe take a break."
        "Could you put on a show for me?":
            menu:
                Girl.voice "[show_line]"
                "Dance for me?":
                    if Girl.Action:
                        call Group_Strip(Girl)
                    else:
                        call out_of_action_lines(Girl)
                "Could you undress for me?":
                    call Girl_Undress(Girl)
                "You've got a little something. . . [[clean-up]" if Girl.Spunk:
                    call got_some_spunk_lines(Girl)

                    call Girl_Cleanup(Girl,"ask")
                "Could I watch you get yourself off? [[masturbate]":
                    if Girl.Action:
                        call masturbate(Girl)
                    else:
                        call out_of_action_lines(Girl)
                "Maybe make out with [RogueX.name]?" if Girl != RogueX and RogueX.Loc == bg_current:
                    call LesScene(RogueX)
                "Maybe make out with [KittyX.name]?" if Girl != KittyX and  KittyX.Loc == bg_current:
                    call LesScene(KittyX)
                "Maybe make out with [LauraX.name]?" if Girl != LauraX and LauraX.Loc == bg_current:
                    call LesScene(LauraX)
                "Maybe make out with [JeanX.name]?" if Girl != JeanX and JeanX.Loc == bg_current:
                    call LesScene(JeanX)
                "Maybe make out with [StormX.name]?" if Girl != StormX and StormX.Loc == bg_current:
                    call LesScene(StormX)
                "Maybe make out with [JubesX.name]?" if Girl != JubesX and JubesX.Loc == bg_current:
                    call LesScene(JubesX)
                "Never mind [[something else]":
                    jump main_sex_menu
        "Could we maybe?. . . [[fuck]":
            if Girl.Action:
                menu:
                    "What did you want to do?"
                    "Come over here, I've got something in mind. . .":
                        if Player.Semen:
                            call hotdog(Girl)
                        else:
                            "The spirit is apparently willing, but the flesh is spongy and bruised."
                    "Fuck your pussy.":
                        if Player.Semen:
                            call sex(Girl)
                        else:
                            "The spirit is apparently willing, but the flesh is spongy and bruised."
                    "Fuck your ass.":
                        if Player.Semen:
                            call anal(Girl)
                        else:
                            "The spirit is apparently willing, but the flesh is spongy and bruised."
                    "How about some toys? [[Pussy]":
                        call dildo_pussy(Girl)
                    "How about some toys? [[Anal]":
                        call dildo_ass(Girl)
                    "Never mind [[something else]":
                        jump main_sex_menu
            else:
                call out_of_action_lines(Girl)
        "Hey, do you want in on this? [[Threesome]" if not Partner:
            call main_sex_menu_Threesome(Girl)

            jump main_sex_menu
        "Hey, [Partner.name]? [[Switch lead]" if Partner:
            call expression Partner.Tag + "_SexAct" pass ("switch")
        "Cheat Menu" if config.developer:
            call Cheat_Menu(Girl)
        "Never mind. [[exit]":
            if Girl.lust >= 50 or Girl.Addict >= 50:
                $ Girl.change_face("sad")

                if Girl.Action and Girl.SEXP >= 15 and Round > 20:
                    if "round2" not in Girl.recent_history:
                        if Girl == RogueX:
                            ch_r "Are you sure, [Girl.Petname]? I could really use some company."
                        elif Girl == KittyX:
                            ch_k "Are you sure, [Girl.Petname]? I wasn't exactly. . . finished."
                        elif Girl == EmmaX:
                            ch_e "Are you certain, [Girl.Petname]? Are you perhaps forgetting something?"
                        elif Girl == LauraX:
                            ch_l "Are you sure, [Girl.Petname]?"
                            ch_l "I could go another round. . . or two. . ."
                        elif Girl == JeanX:
                            ch_j "Are you sure, [Girl.Petname]?"
                            ch_j "I could go another round. . . or two. . ."
                        elif Girl == StormX:
                            ch_s "Are you certain, [Girl.Petname]? Are you perhaps forgetting something?"
                        elif Girl == JubesX:
                            ch_v "Are you sure, [Girl.Petname]?"
                            ch_v "I could keep going. . ."

                        $ Girl.change_stat("inhibition", 30, 2)
                        $ Girl.change_stat("inhibition", 50, 1)
                    elif Girl.Addict >= 50:
                        if Girl == RogueX:
                            ch_r "I still need a little. . . contact."
                        elif Girl == KittyX:
                            ch_k "I need more touching."
                        elif Girl == EmmaX:
                            ch_e "I need more contact."
                        elif Girl == LauraX:
                            ch_l "I need more contact."
                        elif Girl == JeanX:
                            ch_j "I need some more skin contact."
                            ch_j "You gonna leave me hanging?"
                        elif Girl == StormX:
                            ch_s "I need your touch."
                        elif Girl == JubesX:
                            ch_v "I'm a little drained, I need more contact."
                    else:
                        if Girl == RogueX:
                            ch_r "Don't leave my hang'in, [Girl.Petname]."
                        elif Girl == KittyX:
                            ch_k "I still need some more attention."
                        elif Girl == EmmaX:
                            ch_e "I'm afraid that still wasn't enough."
                        elif Girl == LauraX:
                            ch_l "Aren't you forgetting something?"
                        elif Girl == JeanX:
                            ch_j "Hey, you'd better get me off here."
                            ch_j "You gonna leave me hanging?"
                        elif Girl == StormX:
                            ch_s "That was not enough to satisfy me."
                        elif Girl == JubesX:
                            ch_v "Hey! Don't leave me hanging here."
                    menu:
                        extend ""
                        "Yeah, I'm done for now." if Player.Semen and "round2" not in Girl.recent_history:
                            if "unsatisfied" in Girl.recent_history and not Girl.OCount:
                                $ Girl.change_face("angry")
                                $ Girl.Eyes = "side"
                                $ Girl.change_stat("love", 70, -2)
                                $ Girl.change_stat("love", 90, -4)
                                $ Girl.change_stat("obedience", 30, 2)
                                $ Girl.change_stat("obedience", 70, 1)

                                if Girl == RogueX:
                                    ch_r "Way to leave a girl in the lurch. . ."
                                elif Girl == KittyX:
                                    ch_k "Rude!"
                                elif Girl == EmmaX:
                                    ch_e "Well! This might count against you next time."
                                elif Girl == LauraX:
                                    ch_l "You'll regret that one."
                                elif Girl == JeanX:
                                    ch_j "The die has been cast."
                                elif Girl == StormX:
                                    ch_s "Perhaps I need to teach you to be more generous."
                                elif Girl == JubesX:
                                    ch_v "Well, that sucks."
                            else:
                                $ Girl.change_face("bemused", 1)
                                $ Girl.change_stat("obedience", 50, 2)

                                if Girl == RogueX:
                                    ch_r "Well, you did at least do your part. . ."
                                elif Girl == KittyX:
                                    ch_k "I guess I'll take what I can get. . ."
                                elif Girl == EmmaX:
                                    ch_e "I suppose I'll have to blame myself as an educator."
                                elif Girl == LauraX:
                                    ch_l "Selfish. . ."
                                elif Girl == JeanX:
                                    ch_j "Booo. . ."
                                elif Girl == StormX:
                                    ch_s "Perhaps I need to teach you to be more generous."
                                elif Girl == JubesX:
                                    ch_v "So selfish. . ."
                        "I gave it a shot." if "round2" in Girl.recent_history:
                            if "unsatisfied" in Girl.recent_history and not Girl.OCount:
                                $ Girl.change_face("angry")
                                $ Girl.Eyes = "side"

                                if Girl == RogueX:
                                    ch_r "Way to leave a girl in the lurch. . ."
                                elif Girl == KittyX:
                                    ch_k "Rude!"
                                elif Girl == EmmaX:
                                    ch_e "Yes, disappointingly so. . ."
                                elif Girl == LauraX:
                                    ch_l "Not a very good one."
                                elif Girl == JeanX:
                                    ch_j "If that's what you want to call it. . ."
                                elif Girl == StormX:
                                    ch_s "So that was the best you could achieve. . ."
                                elif Girl == JubesX:
                                    ch_v "Well try again."
                            else:
                                $ Girl.change_face("bemused", 1)

                                if Girl == RogueX:
                                    ch_r "Well, fair enough. . ."
                                elif Girl == KittyX:
                                    ch_k "I guess I'll take what I can get. . ."
                                elif Girl == EmmaX:
                                    ch_e "I suppose you did. . . shame you couldn't do better. . ."
                                elif Girl == LauraX:
                                    ch_l "Selfish. . ."
                                elif Girl == JeanX:
                                    ch_j "Booo. . ."
                                elif Girl == StormX:
                                    ch_s "So that was the best you could achieve. . ."
                                elif Girl == JubesX:
                                    ch_v "So selfish. . ."
                        "Hey, I did my part." if Girl.OCount > 2:
                                $ Girl.change_face("sly", 1)

                                if Girl == RogueX:
                                    ch_r "I guess you did at that. . ."
                                elif Girl == KittyX:
                                    ch_k "Well. . . yeah, but. . ."
                                elif Girl == EmmaX:
                                    ch_e "Take it as a compliment that I expected more."
                                elif Girl == LauraX:
                                    ch_l "Well. . . yeah, but. . ."
                                elif Girl == JeanX:
                                    ch_j "Stingy. . ."
                                elif Girl == StormX:
                                    ch_s "I had hoped for better.  . ."
                                elif Girl == JubesX:
                                    ch_v "Yeah, but. . . keep doing that. . ."
                        "I'm tapped out for the moment, let's try again later." if not Player.Semen:
                            $ Girl.change_face("normal")

                            if Girl == RogueX:
                                ch_r "Huh, can't be helped, I s'pose."
                            elif Girl == KittyX:
                                ch_k "Yeah, but [Girl.like]. . ."
                            elif Girl == EmmaX:
                                ch_e "I suppose that can't be helped. . ."
                            elif Girl == LauraX:
                                ch_l "Well, you could always try something else. . ."
                            elif Girl == JeanX:
                                ch_j "Your hands don't seem to be broken."
                            elif Girl == StormX:
                                ch_s "Well, I cannot push you to breaking. . ."
                            elif Girl == JubesX:
                                ch_l "Well, you could always try something else. . ."
                        "Ok, we can try something else." if multi_action and "round2" not in Girl.recent_history:
                            $ Girl.change_face("smile")
                            $ Girl.change_stat("love", 70, 2)
                            $ Girl.change_stat("love", 90, 1)

                            if Girl == RogueX:
                                ch_r "Mmmm. . ."
                            elif Girl == KittyX:
                                ch_k "Hehe. . ."
                            elif Girl == EmmaX:
                                ch_e "Excellent. . ."
                            elif Girl == LauraX:
                                ch_l "Good. . ."
                            elif Girl == JeanX:
                                ch_j "Good. . ."
                            elif Girl == StormX:
                                ch_s "Thank you."
                            elif Girl == JubesX:
                                ch_v "Cool. . ."

                            $ Girl.recent_history.append("round2")
                            $ Girl.daily_history.append("round2")

                            call main_sex_menu(Girl)

                            return
                        "Again? Ok, fine." if multi_action and "round2" in Girl.recent_history:
                            $ Girl.change_face("sly")

                            if Girl == RogueX:
                                ch_r "Yeah, again. . ."
                            elif Girl == KittyX:
                                ch_k "You know it. . ."
                            elif Girl == EmmaX:
                                ch_e "Always. . ."
                            elif Girl == LauraX:
                                ch_l "Always. . ."
                            elif Girl == JeanX:
                                ch_j "Always. . ."
                            elif Girl == StormX:
                                ch_s "Always. . ."
                            elif Girl == JubesX:
                                ch_v "Yup. . ."

                            call main_sex_menu(Girl)

                            return
                else:
                    $ Girl.change_face("bemused", 1)

                    if Girl == RogueX:
                        ch_r "I guess I'm a bit tuckered out too, [Girl.Petname]. I guess we can take a breather."
                    elif Girl == KittyX:
                        ch_k "I guess I'm kinda tired too, [Girl.Petname]. We can take a break. . ."
                        ch_k ". . .for now."
                    elif Girl == EmmaX:
                        ch_e "I suppose I'm tired as well, [Girl.Petname]. We can take a breather. . ."
                    elif Girl == LauraX:
                        ch_l "Yeah, you look like you've had enough. We can take a break. . ."
                        ch_l ". . .for now."
                    elif Girl == JeanX:
                        ch_j "Ok, sounds good. . ."
                    elif Girl == StormX:
                        ch_s "I could use some rest as well, [Girl.Petname]."
                    elif Girl == JubesX:
                        ch_v "Sure, I guess we can take a little break. . ."

                    $ Girl.change_stat("inhibition", 30, 2)
                    $ Girl.change_stat("inhibition", 50, 1)
            else:
                if Girl == RogueX:
                    ch_r "Huh? Ok."
                elif Girl == KittyX:
                    ch_k "Ok, fine."
                elif Girl == EmmaX:
                    ch_e "Fine."
                elif Girl == LauraX:
                    ch_l "Ok, fine."
                elif Girl == JeanX:
                    ch_j "Ok, fine."
                elif Girl == StormX:
                    ch_s "That is fine."
                elif Girl == JubesX:
                    ch_v "Sure, fine."

            $ Girl.change_face()
            call Sex_Over

            return True

    return False

label begging_menu(Girl, action):
    menu:
        extend ""
        "Sorry, never mind." if "no_" + action in Girl.daily_history:
            $ Girl.change_face("bemused")

            call no_problem_lines(Girl)

            return
        "Maybe later?" if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "fondle_ass", "handjob", "footjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"] and "no_" + action not in Girl.daily_history:
            $ Girl.change_face("sexy")

            if action == "fondle_breasts" and Girl not in [LauraX, JubesX]:
                "She re-adjusts her cleavage."

            call maybe_later_lines(Girl)

            if action in ["fondle_thighs", "fondle_breasts", "suck_breasts"]:
                $ Girl.change_stat("love", 80, 1)
                $ Girl.change_stat("inhibition", 30, 2)

                if action in ["fondle_breasts", "suck_breasts"]:
                    $ Girl.change_stat("love", 50, 1)
            elif action in ["fondle_pussy"]:
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

            if Taboo:
                $ Girl.AddWord(1, "tabno", "tabno")

            $ Girl.recent_history.append("no_" + action)
            $ Girl.daily_history.append("no_" + action)

            return
        "Come on, please?" if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "blowjob"]:
            if Approval:
                $ Girl.change_face("sexy")

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

                call reward_politeness_lines(Girl)

                if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy"]:
                    jump before_fondle
                elif action in ["blowjob"]:
                    $ line = renpy.random.choice(["Well, sure, ahhhhhh.",
                        "Well. . . ok.",
                        "I guess a taste couldn't hurt.",
                        "I guess I could. . . whip it out.",
                        "Fine. . . [She licks her lips].",
                        "Heh, ok, alright."])
                    ch_r "[line]"

                    $ line = 0

                    jump before_handjob

                return
            else:
                if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy"]:
                    $ Girl.change_face("sexy")

                    call please_not_good_enough_lines(Girl)
                elif action in ["blowjob"]:
                    if ApprovalCheck(Girl, 1100, TabM = 3): # 110, 125, 140, Taboo -120(230)             Handy instead?
                        $ Girl.change_stat("inhibition", 80, 1)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.change_face("confused", 1)

                        if Girl.Hand:
                            ch_r "Maybe you'd settle for a handy?"
                        else:
                            ch_r "I could maybe. . . [[she makes a jerking motion with her hand]?"

                        menu:
                            ch_r "What do you say?"
                            "Sure, that's fine.":
                                $ Girl.change_stat("love", 80, 2)
                                $ Girl.change_stat("inhibition", 60, 1)
                                $ Girl.change_stat("obedience", 50, 1)

                                $ Player.primary_action = "handjob"

                                jump before_handjob
                            "Nah, if it's not a BJ, forget it.":
                                $ Girl.change_stat("love", 200, -2)

                                ch_r "Ok, whatever."

                                $ Girl.change_stat("obedience", 70, 2)
        "I'm sure I can convince you later. . ." if action in ["eat_pussy", "eat_ass"] and "no_" + action not in Girl.daily_history:
            $ Girl.change_face("sexy")

            call maybe_later_lines(Girl)

            $ Girl.change_stat("love", 80, 2)
            $ Girl.change_stat("inhibition", 70, 2)

            if Taboo:
                $ Girl.AddWord(1, "tabno", "tabno")

            $ Girl.recent_history.append("no_" + action)
            $ Girl.daily_history.append("no_" + action)

            return
        "I think you'd really enjoy it. . ." if action in ["eat_pussy", "eat_ass"]:
            if Approval:
                $ Girl.change_face("sexy")
                $ Girl.change_stat("obedience", 90, 2)
                $ Girl.change_stat("obedience", 50, 2)

                call think_would_enjoy_lines(Girl)

                $ Girl.change_stat("inhibition", 70, 3)
                $ Girl.change_stat("inhibition", 40, 2)

                jump before_fondle
            else:
                $ Girl.change_face("sexy")

                call unconvinced_lines(Girl)
        "Just one good squeeze?" if action == "fondle_ass":
            if Approval:
                $ Girl.change_face("sexy")
                $ Girl.change_stat("obedience", 90, 1)
                $ Girl.change_stat("obedience", 50, 2)

                call reward_politeness_lines(Girl)

                $ Girl.change_stat("inhibition", 70, 1)
                $ Girl.change_stat("inhibition", 40, 2)

                jump before_fondle
            else:
                $ Girl.change_face("sexy")

                call unconvinced_lines(Girl)
        "I'd really appreciate it. . ." if action in ["handjob"]:
            if Approval:
                $ Girl.change_face("sexy")
                $ Girl.change_stat("obedience", 90, 2)
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("inhibition", 70, 3)
                $ Girl.change_stat("inhibition", 40, 2)

                $ line = renpy.random.choice(["Sure, put'im here.",
                    "No Problem.",
                    "Sure. Drop trou.",
                    "Sure, I guess.",
                    "Okay.",
                    "Ok, lemme see it.",
                    "I guess. . .",
                    "I suppose, whip it out.",
                    "Ok, [She gestures for you to come over].",
                    "Heh, ok."])
                ch_r "[line]"

                $ line = 0

                jump before_handjob
            else:
                pass
        "I think this could be fun for both of us. . ." if action in ["titjob"]:
            if Approval:
                $ Girl.change_face("sexy")
                $ Girl.change_stat("obedience", 80, 2)
                $ Girl.change_stat("obedience", 40, 2)
                $ Girl.change_stat("inhibition", 70, 3)
                $ Girl.change_stat("inhibition", 40, 2)

                $ line = renpy.random.choice(["Well, ok, put it here.",
                    "Well. . . ok.",
                    "I guess.",
                    "I guess, whip it out.",
                    "Fine. . . [She drools a bit into her cleavage].",
                    "Heh, ok, alright."])
                ch_r "[line]"

                $ line = 0

                jump before_handjob
            else:
                $ Approval = ApprovalCheck(Girl, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)             Handy instead?

                if Approval >= 2:
                    $ Girl.change_stat("inhibition", 80, 1)
                    $ Girl.change_stat("inhibition", 60, 3)
                    $ Girl.change_face("confused", 1)

                    if Girl.Blow:
                        ch_r "I could just. . . blow you instead?"
                    else:
                        ch_r "I could maybe. . . you know, [[she pushes her tongue against the side of her cheek]?"

                    menu:
                        extend ""
                        "Ok, get down there.":
                            $ Girl.change_stat("love", 80, 2)
                            $ Girl.change_stat("inhibition", 60, 1)
                            $ Girl.change_stat("obedience", 50, 1)

                            $ Player.primary_action = "blowjob"

                            jump before_handjob
                        "Nah, it's all about dem titties.":
                            $ line = "no BJ"
                if Approval:
                    $ Girl.change_stat("inhibition", 80, 1)
                    $ Girl.change_stat("inhibition", 60, 3)
                    $ Girl.change_face("confused", 1)

                    if Girl.Hand:
                        ch_r "Maybe you'd settle for a handy?"
                    else:
                        ch_r "I could maybe. . . [[she makes a jerking motion with her hand]?"

                    menu:
                        extend ""
                        "Sure, that's fine.":
                            $ Girl.change_stat("love", 80, 2)
                            $ Girl.change_stat("inhibition", 60, 1)
                            $ Girl.change_stat("obedience", 50, 1)

                            $ Player.primary_action = "handjob"

                            jump before_handjob
                        "Seriously, titties." if line == "no BJ":
                            $ line = 0
                        "Nah, it's all about dem titties." if line != "no BJ":
                            pass

                $ Girl.change_stat("love", 200, -2)

                ch_r "Ok, whatever."

                $ Girl.change_stat("obedience", 70, 2)
        "I think you'd like it. . ." if action in ["dildo_pussy", "dildo_ass"]:
            if Approval:
                $ Girl.change_face("sexy")
                $ Girl.change_stat("obedience", 90, 2)
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("inhibition", 70, 3)
                $ Girl.change_stat("inhibition", 40, 2)

                $ line = renpy.random.choice(["Well, sure, stick it in.",
                    "I suppose. . .",
                    "You've got me there."])
                ch_r "[line]"

                $ line = 0

                call before_handjob
            else:
                pass
        "I think you'd enjoy it as much as I would. . ." if action in ["sex"]:
            if Approval:
                $ Girl.change_face("sexy")
                $ Girl.change_stat("obedience", 90, 2)
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("inhibition", 70, 3)
                $ Girl.change_stat("inhibition", 40, 2)

                $ line = renpy.random.choice(["Well, sure, stick it in.",
                    "I suppose. . .",
                    "You've got me there."])
                ch_r "[line]"

                $ line = 0

                call before_action
        "I bet it would feel really good. . ." if action in ["anal"]:
            if Approval:
                $ Girl.change_face("sexy")
                $ Girl.change_stat("obedience", 90, 2)
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("inhibition", 70, 3)
                $ Girl.change_stat("inhibition", 40, 2)

                $ line = renpy.random.choice(["Well, sure, stick it in.",
                    "I suppose. . .",
                    "You've got me there."])
                ch_r "[line]"

                $ line = 0

                call before_action
            else:
                pass
        "You might like it. . ." if action in ["hotdog"]:
            if Approval:
                $ Girl.change_face("sexy")
                $ Girl.change_stat("obedience", 60, 2)
                $ Girl.change_stat("inhibition", 50, 2)

                $ line = renpy.random.choice(["Well, sure, give it a rub.",
                    "I suppose. . .",
                    "You've got me there."])
                ch_r "[line]"

                $ line = 0

                call before_action
            else:
                pass
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
        "[[Start licking anyway]" if action == "eat_ass":
            call forced_action(Girl, action)
        "Come on, get to work." if action in ["handjob", "footjob"]:                                               # Pressured into it
            call forced_action(Girl, action)
        "Come on, let me fuck those titties, [Girl.Pet]" if action in ["titjob"]:
            $ Girl.nameCheck() #checks reaction to petname

            call forced_action(Girl, action)
        "Suck it, [Girl.Pet]" if action in ["blowjob"]:                                               # Pressured into it
            $ Girl.nameCheck() #checks reaction to petname

            call forced_action(Girl, action)
        "[[Press it against her.]]" if action in ["dildo_pussy", "dildo_ass"]:
            call forced_action(Girl, action)
        "Bend over." if action in ["sex", "anal", "hotdog"]:
            call forced_action(Girl, action)

    return
