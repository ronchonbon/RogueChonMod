label enter_main_sex_menu(character):
    if character == EmmaX:
        if "classcaught" not in character.History:
            ch_e "I can't imagine being a part of something so. . . tawdry."

            return
        if "three" not in character.History and not AloneCheck(character):
            call expression character.Tag + "_ThreeCheck"
        if Taboo > 20 and "taboo" not in character.History:
            call expression character.Tag + "_Taboo_Talk"

            if bg_current == "bg classroom" or bg_current in PersonalRooms and AloneCheck(character):
                ch_p "We could just lock the door, right?"
                ch_e "We certainly could. . ."
                "[character.Name] walks to the door and locks it behind her."

                $ Player.Traits.append("locked")

                call Taboo_Level
            else:
                return

    call Shift_Focus(character)

    $ Trigger = 0
    $ Trigger2 = 0
    $ Trigger3 = 0
    $ Situation = 0

    call hide_girl(character, sprite = True)

    $ character.ArmPose = 1

    call Set_The_Scene(1,0,0,0,1)

    if character in [EmmaX, StormX]:
        if "detention" in character.RecentActions:
            $ temp_modifier = 20 if temp_modifier <= 20 else temp_modifier

    if not Player.Semen:
        "You're a little out of juice at the moment, you might want to wait a bit."
    if Player.Focus >= 95:
        "You're practically buzzing, the slightest breeze could set you off."
    if not character.Action:
        "[character.Name]'s looking a bit tired out, maybe let her rest a bit."

    if "caught" in character.RecentActions or "angry" in character.RecentActions:
        if character.Loc == bg_current:
            call angry_dialog(character)

        $ character.OutfitChange()
        $ character.DrainWord("caught",1,0)

        return

    if Round < 5:
        call take_a_breather_dialog(character)

        return

    $ main_line = None
    $ fondle_line = None
    $ handjob_line = None
    $ show_line = None

    call character_sex_menu(character)

    if character.Loc != bg_current:
        call Set_The_Scene
        call Trig_Reset

        return

    if not MultiAction:
        call Set_The_Scene

        call thats_it_for_now_dialog(character)

        $ character.OCount = 0

        call Trig_Reset

        return

    call GirlsAngry
    call enter_main_sex_menu(character)

    return

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
                call Makeout(character)
            else:
                call out_of_action_dialog(character)
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
                call out_of_action_dialog(character)
        "Could you take care of something for me? [[Your dick, you mean your dick]":
            if Player.Semen and character.Action:
                menu:
                    character.voice "[handjob_line]"
                    "Could you give me a handjob?":
                        call expression character.Tag + "_Handjob"
                    "Could you give me a titjob?":
                        call expression character.Tag + "_Titjob"
                    "Could you suck my cock?":
                        call expression character.Tag + "_Blowjob"
                    "Could use your feet?":
                        call expression character.Tag + "_Footjob"
                    "Never mind [[something else]":
                        jump main_sex_menu
            elif not character.Action:
                call out_of_action_dialog(character)
            else:
                "You really don't have it in you, maybe take a break."
        "Could you put on a show for me?":
            menu:
                character.voice "[show_line]"
                "Dance for me?":
                    if character.Action:
                        call Group_Strip(character)
                    else:
                        call out_of_action_dialog(character)
                "Could you undress for me?":
                    call Girl_Undress(character)
                "You've got a little something. . . [[clean-up]" if character.Spunk:
                    call got_some_spunk_dialog(character)

                    call Girl_Cleanup(character,"ask")
                "Could I watch you get yourself off? [[masturbate]":
                    if character.Action:
                        call expression character.Tag + "_Masturbate"
                    else:
                        call out_of_action_dialog(character)
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
                            call expression character.Tag + "_Sex_H"
                        else:
                            "The spirit is apparently willing, but the flesh is spongy and bruised."
                    "Fuck your pussy.":
                        if Player.Semen:
                            call expression character.Tag + "_Sex_P"
                        else:
                            "The spirit is apparently willing, but the flesh is spongy and bruised."
                    "Fuck your ass.":
                        if Player.Semen:
                            call expression character.Tag + "_Sex_A"
                        else:
                            "The spirit is apparently willing, but the flesh is spongy and bruised."
                    "How about some toys? [[Pussy]":
                        call expression character.Tag + "_Dildo_Pussy"
                    "How about some toys? [[Anal]":
                        call expression character.Tag + "_Dildo_Ass"
                    "Never mind [[something else]":
                        jump main_sex_menu
            else:
                call out_of_action_dialog(character)
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

            return

    return
