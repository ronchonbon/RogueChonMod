label enter_main_sex_menu:
    if Player.focused_girl == EmmaX:
        if "classcaught" not in Player.focused_girl.History:
            ch_e "I can't imagine being a part of something so. . . tawdry."

            return
        if "three" not in Player.focused_girl.History and not AloneCheck(Player.focused_girl):
            call expression Player.focused_girl.Tag + "_ThreeCheck"
        if Taboo > 20 and "taboo" not in Player.focused_girl.History:
            call expression Player.focused_girl.Tag + "_Taboo_Talk"

            if bg_current == "bg classroom" or bg_current in PersonalRooms and AloneCheck(Player.focused_girl):
                ch_p "We could just lock the door, right?"
                ch_e "We certainly could. . ."
                "[Player.focused_girl.Name] walks to the door and locks it behind her."

                $ Player.Traits.append("locked")

                call Taboo_Level
            else:
                return

    call Shift_Focus(Player.focused_girl)

    $ Trigger = 0
    $ Trigger2 = 0
    $ Trigger3 = 0
    $ Situation = 0

    call hide_girl(Player.focused_girl, sprite = True)

    $ Player.focused_girl.ArmPose = 1

    call Set_The_Scene(1,0,0,0,1)

    if Player.focused_girl in [EmmaX, StormX]:
        if "detention" in Player.focused_girl.RecentActions:
            $ temp_modifier = 20 if temp_modifier <= 20 else temp_modifier

    if not Player.Semen:
        "You're a little out of juice at the moment, you might want to wait a bit."
    if Player.Focus >= 95:
        "You're practically buzzing, the slightest breeze could set you off."
    if not Player.focused_girl.Action:
        "[Player.focused_girl.Name]'s looking a bit tired out, maybe let her rest a bit."

    if "caught" in Player.focused_girl.RecentActions or "angry" in Player.focused_girl.RecentActions:
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

    call character_sex_menu(Player.focused_girl)

    if _return:
        return

    if Player.focused_girl.Loc != bg_current:
        call Set_The_Scene
        call Trig_Reset

        return

    if not MultiAction:
        call Set_The_Scene

        call thats_it_for_now_lines(Player.focused_girl)

        $ Player.focused_girl.OCount = 0

        call Trig_Reset

        return

    call GirlsAngry
    jump enter_main_sex_menu

label character_sex_menu(character):
    if character == RogueX:
        $ main_line = "So what would you like to do?"
        $ fondle_line = "Well where exactly were you interested in touching, " + character.Petname + "?"
        $ handjob_line = "What did you have in mind, " + character.Petname + "?"
        $ show_line = "What sort of show were you expecting?"
    elif character == KittyX:
        $ main_line = "So what would you like to do?"
        $ fondle_line = "Um, what did you want to touch, " + character.Petname + "?"
        $ handjob_line = character.Like + "what did you want me to do?"
        $ show_line = character.Like + "what did you want to see?"
    elif character == EmmaX:
        $ main_line = "So, what was it you hoped to do?"
        $ fondle_line = "Well? Where did you want to touch, " + character.Petname + "?"
        $ handjob_line = "What did you want me to do?"
        $ show_line = "What did you want to see?"
    elif character == LauraX:
        $ main_line = "What did you want to do?"
        $ fondle_line = "Yeah? Like where?"
        $ handjob_line = "Oh? Like what?"
        $ show_line = "What kind of show are you thinking?"
    elif character == JeanX:
        $ main_line = "What did you want to do?"
        $ fondle_line = "Yeah? Like where?"
        $ handjob_line = "Oh? Like what?"
        $ show_line = "What kind of show are you thinking?"
    elif character == StormX:
        $ main_line = "So, what was it you hoped to do?"
        $ fondle_line = "What did you wish to touch, " + character.Petname + "?"
        $ handjob_line = "What did you want me to do?"
        $ show_line = "What did you want to see?"
    elif character == JubesX:
        $ main_line = "So what did you wanna do?"
        $ fondle_line = "Where were you thinking?"
        $ handjob_line = "What were you thinking?"
        $ show_line = "What kind of show?"

    menu main_sex_menu:
        character.voice "[main_line]"
        "Do you want to make out?":
            if character.Action:
                call kiss(character)
            else:
                call out_of_action_lines(character)
        "Could I touch you?":
            if character.Action:
                if character in [EmmaX, StormX]:
                    $ character.FaceChange("sly")
                else:
                    $ character.Mouth = "smile"

                menu:
                    character.voice "[fondle_line]"
                    "Could I give you a massage?":
                        call Massage(character)
                    "Your breasts?":
                        call fondle_breasts(character)
                    "Suck your breasts?" if character.Action and character.SuckB:
                        call suck_breasts(character)
                    "Your thighs?" if character.Action:
                        call fondle_thighs(character)
                    "Your pussy?" if character.Action:
                        call fondle_pussy(character)
                    "Lick your pussy?" if character.Action and character.LickP:
                        call lick_pussy(character)
                    "Your Ass?":
                        call fondle_ass(character)
                    "Eat your ass?" if character.Action and character.LickA:
                        call lick_ass(character)
                    "Never mind [[something else]":
                        jump main_sex_menu
            else:
                call out_of_action_lines(character)
        "Could you take care of something for me? [[Your dick, you mean your dick]":
            if Player.Semen and character.Action:
                menu:
                    character.voice "[handjob_line]"
                    "Could you give me a handjob?":
                        call handjob(character)
                    "Could you give me a titjob?":
                        call titjob(character)
                    "Could you suck my cock?":
                        call blowjob(character)
                    "Could use your feet?":
                        call footjob(character)
                    "Never mind [[something else]":
                        jump main_sex_menu
            elif not character.Action:
                call out_of_action_lines(character)
            else:
                "You really don't have it in you, maybe take a break."
        "Could you put on a show for me?":
            menu:
                character.voice "[show_line]"
                "Dance for me?":
                    if character.Action:
                        call Group_Strip(character)
                    else:
                        call out_of_action_lines(character)
                "Could you undress for me?":
                    call Girl_Undress(character)
                "You've got a little something. . . [[clean-up]" if character.Spunk:
                    call got_some_spunk_lines(character)

                    call Girl_Cleanup(character,"ask")
                "Could I watch you get yourself off? [[masturbate]":
                    if character.Action:
                        call masturbate(character)
                    else:
                        call out_of_action_lines(character)
                "Maybe make out with [RogueX.Name]?" if character != RogueX and RogueX.Loc == bg_current:
                    call LesScene(RogueX)
                "Maybe make out with [KittyX.Name]?" if character != KittyX and  KittyX.Loc == bg_current:
                    call LesScene(KittyX)
                "Maybe make out with [LauraX.Name]?" if character != LauraX and LauraX.Loc == bg_current:
                    call LesScene(LauraX)
                "Maybe make out with [JeanX.Name]?" if character != JeanX and JeanX.Loc == bg_current:
                    call LesScene(JeanX)
                "Maybe make out with [StormX.Name]?" if character != StormX and StormX.Loc == bg_current:
                    call LesScene(StormX)
                "Maybe make out with [JubesX.Name]?" if character != JubesX and JubesX.Loc == bg_current:
                    call LesScene(JubesX)
                "Never mind [[something else]":
                    jump main_sex_menu
        "Could we maybe?. . . [[fuck]":
            if character.Action:
                menu:
                    "What did you want to do?"
                    "Come over here, I've got something in mind. . .":
                        if Player.Semen:
                            call hotdog(character)
                        else:
                            "The spirit is apparently willing, but the flesh is spongy and bruised."
                    "Fuck your pussy.":
                        if Player.Semen:
                            call sex(character)
                        else:
                            "The spirit is apparently willing, but the flesh is spongy and bruised."
                    "Fuck your ass.":
                        if Player.Semen:
                            call anal(character)
                        else:
                            "The spirit is apparently willing, but the flesh is spongy and bruised."
                    "How about some toys? [[Pussy]":
                        call dildo_pussy(character)
                    "How about some toys? [[Anal]":
                        call dildo_ass(character)
                    "Never mind [[something else]":
                        jump main_sex_menu
            else:
                call out_of_action_lines(character)
        "Hey, do you want in on this? [[Threesome]" if not Partner:
            call main_sex_menu_Threesome(character)

            jump main_sex_menu
        "Hey, [Partner.Name]? [[Switch lead]" if Partner:
            call expression Partner.Tag + "_SexAct" pass ("switch")
        "Cheat Menu" if config.developer:
            call Cheat_Menu(character)
        "Never mind. [[exit]":
            if character.Lust >= 50 or character.Addict >= 50:
                $ character.FaceChange("sad")

                if character.Action and character.SEXP >= 15 and Round > 20:
                    if "round2" not in character.RecentActions:
                        if character == RogueX:
                            ch_r "Are you sure, [character.Petname]? I could really use some company."
                        elif character == KittyX:
                            ch_k "Are you sure, [character.Petname]? I wasn't exactly. . . finished."
                        elif character == EmmaX:
                            ch_e "Are you certain, [character.Petname]? Are you perhaps forgetting something?"
                        elif character == LauraX:
                            ch_l "Are you sure, [character.Petname]?"
                            ch_l "I could go another round. . . or two. . ."
                        elif character == JeanX:
                            ch_j "Are you sure, [character.Petname]?"
                            ch_j "I could go another round. . . or two. . ."
                        elif character == StormX:
                            ch_s "Are you certain, [character.Petname]? Are you perhaps forgetting something?"
                        elif character == JubesX:
                            ch_v "Are you sure, [character.Petname]?"
                            ch_v "I could keep going. . ."

                        $ character.Statup("Inbt", 30, 2)
                        $ character.Statup("Inbt", 50, 1)
                    elif character.Addict >= 50:
                        if character == RogueX:
                            ch_r "I still need a little. . . contact."
                        elif character == KittyX:
                            ch_k "I need more touching."
                        elif character == EmmaX:
                            ch_e "I need more contact."
                        elif character == LauraX:
                            ch_l "I need more contact."
                        elif character == JeanX:
                            ch_j "I need some more skin contact."
                            ch_j "You gonna leave me hanging?"
                        elif character == StormX:
                            ch_s "I need your touch."
                        elif character == JubesX:
                            ch_v "I'm a little drained, I need more contact."
                    else:
                        if character == RogueX:
                            ch_r "Don't leave my hang'in, [character.Petname]."
                        elif character == KittyX:
                            ch_k "I still need some more attention."
                        elif character == EmmaX:
                            ch_e "I'm afraid that still wasn't enough."
                        elif character == LauraX:
                            ch_l "Aren't you forgetting something?"
                        elif character == JeanX:
                            ch_j "Hey, you'd better get me off here."
                            ch_j "You gonna leave me hanging?"
                        elif character == StormX:
                            ch_s "That was not enough to satisfy me."
                        elif character == JubesX:
                            ch_v "Hey! Don't leave me hanging here."
                    menu:
                        extend ""
                        "Yeah, I'm done for now." if Player.Semen and "round2" not in character.RecentActions:
                            if "unsatisfied" in character.RecentActions and not character.OCount:
                                $ character.FaceChange("angry")
                                $ character.Eyes = "side"
                                $ character.Statup("Love", 70, -2)
                                $ character.Statup("Love", 90, -4)
                                $ character.Statup("Obed", 30, 2)
                                $ character.Statup("Obed", 70, 1)

                                if character == RogueX:
                                    ch_r "Way to leave a girl in the lurch. . ."
                                elif character == KittyX:
                                    ch_k "Rude!"
                                elif character == EmmaX:
                                    ch_e "Well! This might count against you next time."
                                elif character == LauraX:
                                    ch_l "You'll regret that one."
                                elif character == JeanX:
                                    ch_j "The die has been cast."
                                elif character == StormX:
                                    ch_s "Perhaps I need to teach you to be more generous."
                                elif character == JubesX:
                                    ch_v "Well, that sucks."
                            else:
                                $ character.FaceChange("bemused", 1)
                                $ character.Statup("Obed", 50, 2)

                                if character == RogueX:
                                    ch_r "Well, you did at least do your part. . ."
                                elif character == KittyX:
                                    ch_k "I guess I'll take what I can get. . ."
                                elif character == EmmaX:
                                    ch_e "I suppose I'll have to blame myself as an educator."
                                elif character == LauraX:
                                    ch_l "Selfish. . ."
                                elif character == JeanX:
                                    ch_j "Booo. . ."
                                elif character == StormX:
                                    ch_s "Perhaps I need to teach you to be more generous."
                                elif character == JubesX:
                                    ch_v "So selfish. . ."
                        "I gave it a shot." if "round2" in character.RecentActions:
                            if "unsatisfied" in character.RecentActions and not character.OCount:
                                $ character.FaceChange("angry")
                                $ character.Eyes = "side"

                                if character == RogueX:
                                    ch_r "Way to leave a girl in the lurch. . ."
                                elif character == KittyX:
                                    ch_k "Rude!"
                                elif character == EmmaX:
                                    ch_e "Yes, disappointingly so. . ."
                                elif character == LauraX:
                                    ch_l "Not a very good one."
                                elif character == JeanX:
                                    ch_j "If that's what you want to call it. . ."
                                elif character == StormX:
                                    ch_s "So that was the best you could achieve. . ."
                                elif character == JubesX:
                                    ch_v "Well try again."
                            else:
                                $ character.FaceChange("bemused", 1)

                                if character == RogueX:
                                    ch_r "Well, fair enough. . ."
                                elif character == KittyX:
                                    ch_k "I guess I'll take what I can get. . ."
                                elif character == EmmaX:
                                    ch_e "I suppose you did. . . shame you couldn't do better. . ."
                                elif character == LauraX:
                                    ch_l "Selfish. . ."
                                elif character == JeanX:
                                    ch_j "Booo. . ."
                                elif character == StormX:
                                    ch_s "So that was the best you could achieve. . ."
                                elif character == JubesX:
                                    ch_v "So selfish. . ."
                        "Hey, I did my part." if character.OCount > 2:
                                $ character.FaceChange("sly", 1)

                                if character == RogueX:
                                    ch_r "I guess you did at that. . ."
                                elif character == KittyX:
                                    ch_k "Well. . . yeah, but. . ."
                                elif character == EmmaX:
                                    ch_e "Take it as a compliment that I expected more."
                                elif character == LauraX:
                                    ch_l "Well. . . yeah, but. . ."
                                elif character == JeanX:
                                    ch_j "Stingy. . ."
                                elif character == StormX:
                                    ch_s "I had hoped for better.  . ."
                                elif character == JubesX:
                                    ch_v "Yeah, but. . . keep doing that. . ."
                        "I'm tapped out for the moment, let's try again later." if not Player.Semen:
                            $ character.FaceChange("normal")

                            if character == RogueX:
                                ch_r "Huh, can't be helped, I s'pose."
                            elif character == KittyX:
                                ch_k "Yeah, but [character.like]. . ."
                            elif character == EmmaX:
                                ch_e "I suppose that can't be helped. . ."
                            elif character == LauraX:
                                ch_l "Well, you could always try something else. . ."
                            elif character == JeanX:
                                ch_j "Your hands don't seem to be broken."
                            elif character == StormX:
                                ch_s "Well, I cannot push you to breaking. . ."
                            elif character == JubesX:
                                ch_l "Well, you could always try something else. . ."
                        "Ok, we can try something else." if MultiAction and "round2" not in character.RecentActions:
                            $ character.FaceChange("smile")
                            $ character.Statup("Love", 70, 2)
                            $ character.Statup("Love", 90, 1)

                            if character == RogueX:
                                ch_r "Mmmm. . ."
                            elif character == KittyX:
                                ch_k "Hehe. . ."
                            elif character == EmmaX:
                                ch_e "Excellent. . ."
                            elif character == LauraX:
                                ch_l "Good. . ."
                            elif character == JeanX:
                                ch_j "Good. . ."
                            elif character == StormX:
                                ch_s "Thank you."
                            elif character == JubesX:
                                ch_v "Cool. . ."

                            $ character.RecentActions.append("round2")
                            $ character.DailyActions.append("round2")

                            call main_sex_menu(character)

                            return
                        "Again? Ok, fine." if MultiAction and "round2" in character.RecentActions:
                            $ character.FaceChange("sly")

                            if character == RogueX:
                                ch_r "Yeah, again. . ."
                            elif character == KittyX:
                                ch_k "You know it. . ."
                            elif character == EmmaX:
                                ch_e "Always. . ."
                            elif character == LauraX:
                                ch_l "Always. . ."
                            elif character == JeanX:
                                ch_j "Always. . ."
                            elif character == StormX:
                                ch_s "Always. . ."
                            elif character == JubesX:
                                ch_v "Yup. . ."

                            call main_sex_menu(character)

                            return
                else:
                    $ character.FaceChange("bemused", 1)

                    if character == RogueX:
                        ch_r "I guess I'm a bit tuckered out too, [character.Petname]. I guess we can take a breather."
                    elif character == KittyX:
                        ch_k "I guess I'm kinda tired too, [character.Petname]. We can take a break. . ."
                        ch_k ". . .for now."
                    elif character == EmmaX:
                        ch_e "I suppose I'm tired as well, [character.Petname]. We can take a breather. . ."
                    elif character == LauraX:
                        ch_l "Yeah, you look like you've had enough. We can take a break. . ."
                        ch_l ". . .for now."
                    elif character == JeanX:
                        ch_j "Ok, sounds good. . ."
                    elif character == StormX:
                        ch_s "I could use some rest as well, [character.Petname]."
                    elif character == JubesX:
                        ch_v "Sure, I guess we can take a little break. . ."

                    $ character.Statup("Inbt", 30, 2)
                    $ character.Statup("Inbt", 50, 1)
            else:
                if character == RogueX:
                    ch_r "Huh? Ok."
                elif character == KittyX:
                    ch_k "Ok, fine."
                elif character == EmmaX:
                    ch_e "Fine."
                elif character == LauraX:
                    ch_l "Ok, fine."
                elif character == JeanX:
                    ch_j "Ok, fine."
                elif character == StormX:
                    ch_s "That is fine."
                elif character == JubesX:
                    ch_v "Sure, fine."

            $ character.FaceChange()
            call Sex_Over

            return True

    return False

label begging_menu(character, action):
    menu:
        extend ""
        "Sorry, never mind." if "no_" + action in character.DailyActions:
            $ character.FaceChange("bemused")

            call no_problem_lines(character)

            return
        "Maybe later?" if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "fondle_ass", "handjob", "footjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"] and "no_" + action not in character.DailyActions:
            $ character.FaceChange("sexy")

            if action == "fondle_breasts" and character not in [LauraX, JubesX]:
                "She re-adjusts her cleavage."

            call maybe_later_lines(character)

            if action in ["fondle_thighs", "fondle_breasts", "suck_breasts"]:
                $ character.Statup("Love", 80, 1)
                $ character.Statup("Inbt", 30, 2)

                if action in ["fondle_breasts", "suck_breasts"]:
                    $ character.Statup("Love", 50, 1)
            elif action in ["fondle_pussy"]:
                $ character.Statup("Love", 80, 2)
                $ character.Statup("Inbt", 70, 2)
            elif action in ["fondle_ass"]:
                $ character.Statup("Love", 80, 2)
                $ character.Statup("Inbt", 50, 2)
            elif action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal"]:
                $ character.Statup("Love", 80, 2)
                $ character.Statup("Inbt", 70, 2)
            elif action in ["hotdog"]:
                $ character.Statup("Love", 80, 1)
                $ character.Statup("Inbt", 50, 1)

            if Taboo:
                $ character.AddWord(1, "tabno", "tabno")

            $ character.RecentActions.append("no_" + action)
            $ character.DailyActions.append("no_" + action)

            return
        "Come on, please?" if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "blowjob"]:
            if Approval:
                $ character.FaceChange("sexy")

                if action == "fondle_thighs":
                    $ character.Statup("Obed", 60, 1)
                    $ character.Statup("Obed", 30, 2)
                    $ character.Statup("Inbt", 50, 1)
                    $ character.Statup("Inbt", 30, 2)
                elif action in ["fondle_breasts", "suck_breasts"]:
                    if character != LauraX:
                        $ character.Statup("Obed", 90, 1)

                    $ character.Statup("Obed", 50, 2)
                    $ character.Statup("Inbt", 60, 3)
                    $ character.Statup("Inbt", 30, 2)
                elif action in ["fondle_pussy", "blowjob"]:
                    $ character.Statup("Obed", 90, 2)
                    $ character.Statup("Obed", 50, 2)
                    $ character.Statup("Inbt", 70, 3)
                    $ character.Statup("Inbt", 40, 2)

                call reward_politeness_lines(character)

                if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy"]:
                    jump before_fondle
                elif action in ["blowjob"]:
                    $ Line = renpy.random.choice(["Well, sure, ahhhhhh.",
                        "Well. . . ok.",
                        "I guess a taste couldn't hurt.",
                        "I guess I could. . . whip it out.",
                        "Fine. . . [She licks her lips].",
                        "Heh, ok, alright."])
                    ch_r "[Line]"

                    $ Line = 0

                    jump before_handjob

                return
            else:
                if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy"]:
                    $ character.FaceChange("sexy")

                    call please_not_good_enough_lines(character)
                elif action in ["blowjob"]:
                    if ApprovalCheck(character, 1100, TabM = 3): # 110, 125, 140, Taboo -120(230)             Handy instead?
                        $ character.Statup("Inbt", 80, 1)
                        $ character.Statup("Inbt", 60, 3)
                        $ character.FaceChange("confused", 1)

                        if character.Hand:
                            ch_r "Maybe you'd settle for a handy?"
                        else:
                            ch_r "I could maybe. . . [[she makes a jerking motion with her hand]?"

                        menu:
                            ch_r "What do you say?"
                            "Sure, that's fine.":
                                $ character.Statup("Love", 80, 2)
                                $ character.Statup("Inbt", 60, 1)
                                $ character.Statup("Obed", 50, 1)

                                $ Player.primary_action = "handjob"

                                jump before_handjob
                            "Nah, if it's not a BJ, forget it.":
                                $ character.Statup("Love", 200, -2)

                                ch_r "Ok, whatever."

                                $ character.Statup("Obed", 70, 2)
        "I'm sure I can convince you later. . ." if action in ["eat_pussy", "eat_ass"] and "no_" + action not in character.DailyActions:
            $ character.FaceChange("sexy")

            call maybe_later_lines(character)

            $ character.Statup("Love", 80, 2)
            $ character.Statup("Inbt", 70, 2)

            if Taboo:
                $ character.AddWord(1, "tabno", "tabno")

            $ character.RecentActions.append("no_" + action)
            $ character.DailyActions.append("no_" + action)

            return
        "I think you'd really enjoy it. . ." if action in ["eat_pussy", "eat_ass"]:
            if Approval:
                $ character.FaceChange("sexy")
                $ character.Statup("Obed", 90, 2)
                $ character.Statup("Obed", 50, 2)

                call think_would_enjoy_lines(character)

                $ character.Statup("Inbt", 70, 3)
                $ character.Statup("Inbt", 40, 2)

                jump before_fondle
            else:
                $ character.FaceChange("sexy")

                call unconvinced_lines(character)
        "Just one good squeeze?" if action == "fondle_ass":
            if Approval:
                $ character.FaceChange("sexy")
                $ character.Statup("Obed", 90, 1)
                $ character.Statup("Obed", 50, 2)

                call reward_politeness_lines(character)

                $ character.Statup("Inbt", 70, 1)
                $ character.Statup("Inbt", 40, 2)

                jump before_fondle
            else:
                $ character.FaceChange("sexy")

                call unconvinced_lines(character)
        "I'd really appreciate it. . ." if action in ["handjob"]:
            if Approval:
                $ character.FaceChange("sexy")
                $ character.Statup("Obed", 90, 2)
                $ character.Statup("Obed", 50, 2)
                $ character.Statup("Inbt", 70, 3)
                $ character.Statup("Inbt", 40, 2)

                $ Line = renpy.random.choice(["Sure, put'im here.",
                    "No Problem.",
                    "Sure. Drop trou.",
                    "Sure, I guess.",
                    "Okay.",
                    "Ok, lemme see it.",
                    "I guess. . .",
                    "I suppose, whip it out.",
                    "Ok, [She gestures for you to come over].",
                    "Heh, ok."])
                ch_r "[Line]"

                $ Line = 0

                jump before_handjob
            else:
                pass
        "I think this could be fun for both of us. . ." if action in ["titjob"]:
            if Approval:
                $ character.FaceChange("sexy")
                $ character.Statup("Obed", 80, 2)
                $ character.Statup("Obed", 40, 2)
                $ character.Statup("Inbt", 70, 3)
                $ character.Statup("Inbt", 40, 2)

                $ Line = renpy.random.choice(["Well, ok, put it here.",
                    "Well. . . ok.",
                    "I guess.",
                    "I guess, whip it out.",
                    "Fine. . . [She drools a bit into her cleavage].",
                    "Heh, ok, alright."])
                ch_r "[Line]"

                $ Line = 0

                jump before_handjob
            else:
                $ Approval = ApprovalCheck(character, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)             Handy instead?

                if Approval >= 2:
                    $ character.Statup("Inbt", 80, 1)
                    $ character.Statup("Inbt", 60, 3)
                    $ character.FaceChange("confused", 1)

                    if character.Blow:
                        ch_r "I could just. . . blow you instead?"
                    else:
                        ch_r "I could maybe. . . you know, [[she pushes her tongue against the side of her cheek]?"

                    menu:
                        extend ""
                        "Ok, get down there.":
                            $ character.Statup("Love", 80, 2)
                            $ character.Statup("Inbt", 60, 1)
                            $ character.Statup("Obed", 50, 1)

                            $ Player.primary_action = "blowjob"

                            jump before_handjob
                        "Nah, it's all about dem titties.":
                            $ Line = "no BJ"
                if Approval:
                    $ character.Statup("Inbt", 80, 1)
                    $ character.Statup("Inbt", 60, 3)
                    $ character.FaceChange("confused", 1)

                    if character.Hand:
                        ch_r "Maybe you'd settle for a handy?"
                    else:
                        ch_r "I could maybe. . . [[she makes a jerking motion with her hand]?"

                    menu:
                        extend ""
                        "Sure, that's fine.":
                            $ character.Statup("Love", 80, 2)
                            $ character.Statup("Inbt", 60, 1)
                            $ character.Statup("Obed", 50, 1)

                            $ Player.primary_action = "handjob"

                            jump before_handjob
                        "Seriously, titties." if Line == "no BJ":
                            $ Line = 0
                        "Nah, it's all about dem titties." if Line != "no BJ":
                            pass

                $ character.Statup("Love", 200, -2)

                ch_r "Ok, whatever."

                $ character.Statup("Obed", 70, 2)
        "I think you'd like it. . ." if action in ["dildo_pussy", "dildo_ass"]:
            if Approval:
                $ character.FaceChange("sexy")
                $ character.Statup("Obed", 90, 2)
                $ character.Statup("Obed", 50, 2)
                $ character.Statup("Inbt", 70, 3)
                $ character.Statup("Inbt", 40, 2)

                $ Line = renpy.random.choice(["Well, sure, stick it in.",
                    "I suppose. . .",
                    "You've got me there."])
                ch_r "[Line]"

                $ Line = 0

                call before_handjob
            else:
                pass
        "I think you'd enjoy it as much as I would. . ." if action in ["sex"]:
            if Approval:
                $ character.FaceChange("sexy")
                $ character.Statup("Obed", 90, 2)
                $ character.Statup("Obed", 50, 2)
                $ character.Statup("Inbt", 70, 3)
                $ character.Statup("Inbt", 40, 2)

                $ Line = renpy.random.choice(["Well, sure, stick it in.",
                    "I suppose. . .",
                    "You've got me there."])
                ch_r "[Line]"

                $ Line = 0

                call before_action
        "I bet it would feel really good. . ." if action in ["anal"]:
            if Approval:
                $ character.FaceChange("sexy")
                $ character.Statup("Obed", 90, 2)
                $ character.Statup("Obed", 50, 2)
                $ character.Statup("Inbt", 70, 3)
                $ character.Statup("Inbt", 40, 2)

                $ Line = renpy.random.choice(["Well, sure, stick it in.",
                    "I suppose. . .",
                    "You've got me there."])
                ch_r "[Line]"

                $ Line = 0

                call before_action
            else:
                pass
        "You might like it. . ." if action in ["hotdog"]:
            if Approval:
                $ character.FaceChange("sexy")
                $ character.Statup("Obed", 60, 2)
                $ character.Statup("Inbt", 50, 2)

                $ Line = renpy.random.choice(["Well, sure, give it a rub.",
                    "I suppose. . .",
                    "You've got me there."])
                ch_r "[Line]"

                $ Line = 0

                call before_action
            else:
                pass
        "[[Start caressing her thigh anyway]" if action == "fondle_thighs":
            call forced_action(character, action)
        "[[Grab her chest anyway]" if action == "fondle_breasts":
            call forced_action(character, action)
        "[[Start sucking anyway]" if action == "suck_breasts":
            call forced_action(character, action)
        "[[Start fondling anyway]" if action in ["fondle_pussy", "fondle_ass"]:
            call forced_action(character, action)
        "[[Get in there anyway]" if action == "eat_pussy":
            call forced_action(character, action)
        "[[Slide a finger in anyway]" if action == "finger_ass":
            call forced_action(character, action)
        "[[Start licking anyway]" if action == "eat_ass":
            call forced_action(character, action)
        "Come on, get to work." if action in ["handjob", "footjob"]:                                               # Pressured into it
            call forced_action(character, action)
        "Come on, let me fuck those titties, [character.Pet]" if action in ["titjob"]:
            $ character.NameCheck() #checks reaction to petname

            call forced_action(character, action)
        "Suck it, [character.Pet]" if action in ["blowjob"]:                                               # Pressured into it
            $ character.NameCheck() #checks reaction to petname

            call forced_action(character, action)
        "[[Press it against her.]]" if action in ["dildo_pussy", "dildo_ass"]:
            call forced_action(character, action)
        "Bend over." if action in ["sex", "anal", "hotdog"]:
            call forced_action(character, action)

    return
