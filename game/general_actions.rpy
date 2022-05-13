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

label character_initiated_action(character, action):
    if action in ["fondle_breasts", "suck_breasts"]:
        if action == "fondle_breasts":
            $ covered_phrase = "arm and shoves your hand against her covered breast"
            $ topless_phrase = "arm and shoves your hand against her breast"
        elif action == "suck_breasts":
            $ covered_phrase = "head and shoves your face into her chest"
            $ topless_phrase = covered_phrase

        if (character.Over or character.Chest) and not character.Uptop:
            if ApprovalCheck(character, 1250, TabM = 1) or (character.SeenChest and ApprovalCheck(character, 500) and not Taboo):
                $ character.Uptop = 1

                $ Line = character.Over if character.Over else character.Chest

                "With a mischievous grin, [character.Name] pulls her [Line] up over her breasts."

                call first_topless(character, silent = True)

                $ Line = 0

                "She then grabs your [topless_phrase], clearly intending you to get to work."
            else:
                "[character.Name] grabs your [covered_phrase], clearly intending you to get to work."
        else:
            "[character.Name] grabs your [topless_phrase], clearly intending you to get to work."
    elif action in ["fondle_pussy", "eat_pussy", "finger_ass"]:
        if action == "fondle_pussy":
            if character in [Jeanx, JubesX]:
                $ phrase = "grabs your arm and presses your hand into her crotch"
            elif character == StormX:
                $ phrase = "grabs your arm and strokes your hand across her crotch"
            else:
                $ phrase = "grabs your arm and shoves your hand into her crotch"
        elif action == "eat_pussy":
            $ phrase = renpy.random.choice(["grabs your head and shoves your face into her crotch",
                "grabs your head and pulls it to her crotch",
                "grabs your head and wraps her thighs around it"])
        elif action == "finger_ass":
            $ phrase = renpy.random.choice(["grabs your arm and presses your hand against her asshole",
                "grabs your arm and rubs your hand against her asshole"])


        if (character.Legs and not character.Upskirt) or (character.Panties and not character.PantiesDown):
            if ApprovalCheck(character, 1250, TabM = 1) or (character.SeenPussy and ApprovalCheck(character, 500) and not Taboo):
                $ character.Upskirt = 1
                $ character.PantiesDown = 1

                $ Line = 0

                if character.PantsNum() == 5:
                    $ Line = character.Name + " hikes up her skirt"
                elif character.PantsNum() > 6:
                    $ Line = character.Name + " pulls down her " + character.Legs
                else:
                    $ Line = 0

                if character.Panties:
                    if Line:
                        "[Line] and pulls her [character.Panties] out of the way."
                        "She then [phrase], clearly intending you to get to work."
                    else:
                        "She pulls her [character.Panties] out of the way, and then [phrase]."
                        "She clearly intends for you to get to work."
                else:
                    "[Line], and then [phrase]."
                    "She clearly intends for you to get to work."

                call first_bottomless(character, 1)
            else:
                "[character.Name] [phrase], clearly intending you to get to work."
        else:
            "[character.Name] [phrase], clearly intending you to get to work."
    elif action in ["handjob", "footjob", "titjob", "blowjob"]:
        if action == "handjob":
            if Trigger2 == "jackin":
                "[character.Name] brushes your hand aside and starts stroking your cock."
            else:
                "[character.Name] gives you a mischevious smile, and starts to fondle your cock."
        elif action == "footjob":
            "[character.Name] leans forward and starts rubbing your cock between her feet."
        elif action == "titjob":
            "[character.Name] slides down and sandwiches your dick between her tits."
        elif action == "blowjob":
            "[character.Name] slides down and gives your cock a little lick."
    elif action in ["dildo_pussy", "dildo_ass"]:
        if character.PantsNum() == 5:
            "[character.Name] grabs her dildo, hiking up her skirt as she does."

            $ character.Upskirt = 1
        elif character.PantsNum() > 6:
            "[character.Name] grabs her dildo, pulling down her pants as she does."

            $ character.Legs = 0
        else:
            if action == "dildo_pussy":
                "[character.Name] grabs her dildo, rubbing it suggestively against her crotch."
            elif action == "dildo_ass":
                "[character.Name] grabs her dildo, rubbing is suggestively against her ass."

        $ character.SeenPanties = 1

        if action == "dildo_pussy":
            "She slides the tip along her pussy and seems to want you to insert it."
        elif action == "dildo_ass":
            "She slides the tip against her asshole, and seems to want you to insert it."
    elif action in ["sex", "anal", "hotdog"]:
        if action in ["sex", "anal"]:
            if character.PantsNum() == 5:
                $ line = renpy.random.choice(["[character.Name] turns and backs up against your cock, sliding her skirt up as she does so.",
                    "[character.Name] rolls back and pulls you toward her, sliding her skirt up as she does so.",
                    "[character.Name] turns around, sliding her skirt up as she does so.",
                    "[character.Name] pushes you back and climbs on top of you, sliding her skirt up as she does so.",
                    "[character.Name] lays back, sliding her skirt up as she does so."])
                "[line]"

                $ character.Upskirt = 1
            elif character.PantsNum() > 6:
                $ line = renpy.random.choice(["[character.Name] turns and backs up against your cock, sliding her [character.Legs] down as she does so.",
                    "[character.Name] rolls back and pulls you against her, sliding her [character.Legs] off as she does so.",
                    "[character.Name] pushes you down and climbs on top of you, sliding her [character.Legs] down as she does so.",
                    "[character.Name] turns around, sliding her [character.Legs] down as she does so.",
                    "[character.Name] lays back, sliding her [character.Legs] down as she does so."])
                "[line]"

                $ character.Upskirt = 1
            elif character.PantsNum() == 6:
                $ line = renpy.random.choice(["[character.Name] rolls onto her back and pulls you against her, sliding her shorts off as she does so."])
                "[line]"

                $ character.Upskirt = 1
            else:
                $ line = renpy.random.choice(["[character.Name] turns and backs up against your cock.",
                    "[character.Name] rolls back and pulls you toward her.",
                    "[character.Name] pushes you back and climbs on top of you.",
                    "[character.Name] turns around and pulls you toward her."])
                "[line]"

            $ character.SeenPanties = 1

            if action == "sex":
                $ line = renpy.random.choice(["She slides the tip along her pussy and seems to want you to insert it."])
                "[line]"
            elif action == "anal":
                $ line = renpy.random.choice(["She slides the tip up to her anus, and presses against it.",
                    "She slides the tip along her ass and seems to want you to insert it.",
                    "She slides the tip against her ass and seems to want you to insert it.",
                    "She slides the tip along her asshole, and seems to want you to insert it."])
                "[line]"
        else:
            $ line = renpy.random.choice(["[character.Name] turns and backs up against your cock, rubbing it against her ass.",
                "[character.Name] rolls back and pulls you toward her, rubbing her pussy against your cock.",
                "[character.Name] pushes you back and climbs on top of you, sliding back and forth along your shaft.",
                "[character.Name] rolls back and pulls you toward her, grinding against your cock.",
                "[character.Name] turns around and pulls you toward her, grinding against your cock."])
            "[line]"

    if action in ["fondle_breasts", "suck_breasts", "fondle_pussy", "eat_pussy", "finger_ass", "handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
        if action == "fondle_breasts":
            $ action_line = "You start to fondle them."
            $ praise_line = "I like the initiative, " + character.Pet
            $ no_action_line = "You pull your hand back."
            $ reject_line = "Let's not do that right now, " + character.Pet
            $ rejection_response_line = character.Name + " pulls back."
        elif action == "suck_breasts":
            $ action_line = "You start to run your tongue along her nipple."
            $ praise_line = "Mmm, I like this, " + character.Pet
            $ no_action_line = "You pull your head back."
            $ reject_line = "Let's not do that right now, " + character.Pet
            $ rejection_response_line = character.Name + " pulls away."
        elif action == "fondle_pussy":
            $ action_line = "You start to run your fingers along her pussy."
            $ praise_line = "I like the initiative, " + character.Pet
            $ no_action_line = "You pull your hand back."
            $ reject_line = "Let's not do that right now, " + character.Pet
            $ rejection_response_line = character.Name + " pulls back."
        elif action == "eat_pussy":
            $ action_line = "You start licking her slit."
            $ praise_line = "Mmm, I like this idea, " + character.Pet
            $ no_action_line = "You pull your head away."
            $ reject_line = "Let's not do that right now, " + character.Pet
            $ rejection_response_line = character.Name + " pulls back."
        elif action == "finger_ass":
            $ action_line = "You press your finger into her tight ass."
            $ praise_line = "Dirty girl, " + character.Pet
            $ no_action_line = "You pull your hand back."
            $ reject_line = "Let's not do that right now, " + character.Pet
            $ rejection_response_line = character.Name + " pulls back."
        elif action == "handjob":
            $ action_line = "[character.Name] continues her actions."
            $ praise_line = "Oooh, that's good, [character.Pet]."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [character.Pet]."
            $ rejection_response_line = "[character.Name] puts it down."
        elif action == "footjob":
            $ action_line = "[character.Name] continues her actions."
            $ praise_line = "Oooh, that's good, [character.Pet]."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [character.Pet]."
            $ rejection_response_line = "[character.Name] puts it down."
        elif action == "titjob":
            $ action_line = "[character.Name] starts to slide them up and down."
            $ praise_line = "Oh, that sounds like a good idea, [character.Pet]."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [character.Pet]."
            $ rejection_response_line = "[character.Name] lets it drop out from between her breasts."
        elif action == "blowjob":
            $ action_line = "[character.Name] continues licking at it."
            $ praise_line = "Hmmm, keep doing that, [character.Pet]."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [character.Pet]."
            $ rejection_response_line = "[character.Name] puts it down."
        elif action == "dildo_pussy":
            $ action_line = "[character.Name] slides it in."
            $ praise_line = "Oh yeah, [character.Pet], let's do this."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [character.Pet]."
            $ rejection_response_line = "[character.Name] sets the dildo down."
        elif action == "dildo_ass":
            $ action_line = "[character.Name] slides it in."
            $ praise_line = "Hmmm, keep doing that, [character.Pet]."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [character.Pet]."
            $ rejection_response_line = "[character.Name] sets the dildo down."
        elif action == "sex":
            $ action_line = "[character.Name] slides it in."
            $ praise_line = "Oh yeah, [character.Pet], let's do this."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [character.Pet]."
            $ rejection_response_line = "[character.Name] pulls back."
        elif action == "anal":
            $ action_line = "[character.Name] slides it in."
            $ praise_line = "Ooo, dirty girl, [character.Pet], let's do this."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [character.Pet]."
            $ rejection_response_line = "[character.Name] pulls back."
        elif action == "hotdog":
            $ action_line = renpy.random.choice([character.Name + " starts to grind against you",
                character.Name + " keeps grinding",
                character.Name + " continues to grind"])
            $ praise_line = "Hmmm, that's good, [character.Pet]."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [character.Pet]."
            $ rejection_response_line = "[character.Name] pulls back."

        menu:
            "What do you do?"
            "Get to work." if action in ["fondle_breasts", "suck_breasts", "fondle_pussy", "eat_pussy", "finger_ass"]:
                $ character.Statup("Inbt", 80, 3)
                $ character.Statup("Inbt", 50, 2)

                "[action_line]"
            "Nothing." if action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass"]:
                $ character.Statup("Inbt", 70, 3)
                $ character.Statup("Inbt", 30, 2)

                "[action_line]"
            "Go with it." if action in ["sex", "anal", "hotdog"]:
                if action in ["sex", "anal"]:
                    $ character.Statup("Inbt", 80, 3)
                    $ character.Statup("Inbt", 50, 2)
                elif action in ["hotdog"]:
                    $ character.Statup("Inbt", 50, 3)

                "[action_line]"
            "Go for it." if action in ["dildo_pussy", "dildo_ass"]:
                $ character.FaceChange("sexy", 1)
                $ character.Statup("Inbt", 80, 3)

                ch_p "[praise_line]"

                $ character.NameCheck() #checks reaction to petname

                "You grab the dildo and slide it in."

                $ character.Statup("Love", 85, 1)
                $ character.Statup("Obed", 90, 1)
                $ character.Statup("Obed", 50, 2)
            "Praise her." if action not in ["dildo_pussy", "dildo_ass"]:
                $ character.FaceChange("sexy", 1)

                if action in ["fondle_breasts", "suck_breasts", "fondle_pussy", "eat_pussy", "finger_ass", "dildo_pussy", "dildo_ass", "sex", "anal"]:
                    $ character.Statup("Inbt", 80, 3)
                elif action in ["handjob", "footjob", "titjob", "blowjob"]:
                    $ character.Statup("Inbt", 70, 3)
                elif action in ["hotdog"]:
                    $ character.Statup("Inbt", 80, 2)

                ch_p "[praise_line]"

                $ character.NameCheck() #checks reaction to petname

                "[action_line]"

                if action in ["fondle_breasts", "suck_breasts", "fondle_pussy", "eat_pussy", "finger_ass", "dildo_pussy", "dildo_ass", "sex", "anal"]:
                    $ character.Statup("Love", 85, 1)
                elif action in ["handjob", "footjob", "titjob", "blowjob", "hotdog"]:
                    $ character.Statup("Love", 80, 1)

                $ character.Statup("Obed", 90, 1)
                $ character.Statup("Obed", 50, 2)
            "Ask her to stop.":
                if no_action_line is not None:
                    "[no_action_line]"

                $ character.FaceChange("surprised")
                $ character.Statup("Inbt", 70, 1)

                ch_p "[reject_line]"

                $ character.NameCheck() #checks reaction to petname

                if character == JeanX:
                    $ character.Statup("Love", 70, -4)

                "[rejection_response_line]"

                if action not in ["hotdog"]:
                    $ character.Statup("Obed", 90, 1)
                    $ character.Statup("Obed", 50, 1)
                    $ character.Statup("Obed", 30, 2)
                else:
                    $ character.Statup("Obed", 80, 1)
                    $ character.Statup("Obed", 30, 2)

                $ Player.RecentActions.append("nope")

                $ character.AddWord(1,"refused","refused")

                return True

    return False

label first_action_approval(character, action):
    if character.Forced:
        $ character.FaceChange("sad")

        if action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "anal", "hotdog"]:
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Love", 20, -2, 1)
        elif action in ["sex"]:
            $ character.Statup("Love", 70, -30, 1)
            $ character.Statup("Love", 20, -20, 1)
    elif character.Love >= (character.Obed + character.Inbt):
        $ character.FaceChange("sexy")
        $ character.Brows = "sad"
        $ character.Mouth = "smile"

        ch_r "Well, I've never really been able to touch people without draining them, this could be an interesting experience. . ."
        ch_r "If that's what you like. . ."
        ch_r "Huh, well that's certainly one way to get off."
        ch_r "I've never really put something like that in my mouth. . . might be interesting."
        ch_r "I've had a reasonable amount of experience with these, you know. . ."
        ch_r "I haven't actually used one of these, back there before. . ."
        ch_r "Well, I've never been able to do this before now, so this might be fun."
        ch_r "I guess if you really want to try it. . ."
        ch_r "It looks like you need some relief. . ."
    elif character.Obed >= character.Inbt:
        if action in ["handjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
            $ character.FaceChange("normal")
        elif action in ["footjob"]:
            $ character.FaceChange("normal",1)

        ch_r "If that's what you want, [character.Petname]. . ."
        ch_r "If that's what you want. . ."
        ch_r "I suppose, if that's what you want. . ."
        ch_r "Ok, [character.Petname], I'm ready."
    elif action in ["handjob", "footjob", "titjob", "blowjob", "sex", "anal", "hotdog"] and character.Addict >= 50:
        $ character.FaceChange("manic", 1)

        ch_r "I think, if I could just touch that. . ."
        ch_r "I guess. . ."
        ch_r "I think. . . for some reason I really do want that in my mouth. . ."
        ch_r "Hmmmm. . . ."
        ch_r "Well. . . I bet it would feel really good down there."
    else:
        if action in ["handjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
            $ character.FaceChange("sad")
            $ character.Mouth = "smile"
        elif action in ["footjob"]:
            $ character.FaceChange("lipbite",1)

        ch_r "Hmm, could be fun. . ."
        ch_r "Sure. . ."
        ch_r "Heh, might be fun."
        ch_r "I guess. . ."
        ch_r "I guess it could be fun with a partner. . ."
        ch_r "Hmm, I've always wanted to try it. . ."
        ch_r "Hmm, it has been on my list. . ."
        ch_r "Hmm, you look ready for it, at least. . ."

    return

label action_accepted(character, action):
    $ character.FaceChange("bemused", 1)

    if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy"]:
        if character.Forced:
            $ character.FaceChange("sad")

            if action in ["fondle_thighs"]:
                $ character.Statup("Love", 70, -3, 1)
                $ character.Statup("Obed", 90, 1)
                $ character.Statup("Inbt", 60, 1)
            elif action in ["fondle_breasts", "suck_breasts", "fondle_pussy"]:
                $ character.Statup("Love", 70, -3, 1)
                $ character.Statup("Love", 20, -2, 1)
                $ character.Statup("Obed", 90, 1)
                $ character.Statup("Inbt", 60, 1)

        call come_and_get_em_lines(character)

        $ character.Statup("Love", 90, 1)
        $ character.Statup("Inbt", 50, 3)

        call before_fondle
    elif action in ["finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
        if character.Forced:
            $ character.FaceChange("sad")

            if action in ["finger_pussy", "eat_pussy", "finger_ass"]:
                $ character.Statup("Love", 70, -3, 1)
                $ character.Statup("Love", 20, -2, 1)
                $ character.Statup("Obed", 90, 1)
                $ character.Statup("Inbt", 60, 1)
            elif action in ["fondle_ass"]:
                $ character.Statup("Love", 70, -2, 1)
                $ character.Statup("Obed", 90, 2)
                $ character.Statup("Inbt", 60, 2)
            elif action in ["eat_ass"]:
                $ character.Statup("Love", 70, -3, 1)
                $ character.Statup("Love", 20, -2, 1)
                $ character.Statup("Obed", 90, 2)
                $ character.Statup("Inbt", 60, 2)

            call forced_but_welcome_lines(character)
        else:
            if action in ["finger_pussy", "eat_pussy"]:
                $ character.FaceChange("sexy", 1)

                if action in ["finger_pussy"]:
                    $ character.Statup("Love", 90, 1)
                    $ character.Statup("Inbt", 50, 3)
                elif action in ["eat_pussy", "finger_ass"]:
                    $ character.Eyes = "closed"
                    $ character.Statup("Love", 90, 1)
                    $ character.Statup("Inbt", 50, 3)
                    $ character.Statup("Lust", 200, 3)
                elif action in ["eat_ass"]:
                    $ character.Eyes = "closed"
                    $ character.Statup("Love", 90, 1)
                    $ character.Statup("Inbt", 60, 2)
                    $ character.Statup("Lust", 200, 3)
            elif action in ["fondle_ass"]:
                $ character.FaceChange("bemused, 1")

            call come_and_get_em_lines(character)

        if action in ["finger_pussy", "eat_pussy", "finger_ass"]:
            $ character.Statup("Obed", 20, 1)
            $ character.Statup("Obed", 60, 1)
            $ character.Statup("Inbt", 70, 2)
        elif action in ["fondle_ass"]:
            $ character.Statup("Lust", 200, 3)
            $ character.Statup("Obed", 60, 1)
            $ character.Statup("Inbt", 70, 1)
        elif action in ["eat_ass"]:
            $ character.Statup("Obed", 20, 1)
            $ character.Statup("Obed", 60, 1)
            $ character.Statup("Inbt", 80, 2)

        call before_fondle
    elif action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:                                                                   #She's into it. . .
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Inbt", 60, 1)

            if action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal"]:
                $ character.Statup("Obed", 90, 1)
            elif action in ["hotdog"]:
                $ character.Statup("Obed", 80, 1)

            ch_r "Ok, fine."
            ch_r ". . . Ok, if that's what you want."
            ch_r "Well, there are worst ways to get you off. . ."
            ch_r "Whatever."
        elif "no_" + action in character.DailyActions:
            ch_r "I guess if it'll get you off. . ."
            ch_r "Fine!"
            ch_r "Hmm, I suppose. . ."
            ch_r "Oh, I suppose it isn't so bad. . ."
            ch_r "Ok, you've won me over on this one. . ."
            ch_r "Ok, ok, I have been itching for this. . ."
            ch_r "Well, I guess it's not so bad. . ."
        else:
            $ character.FaceChange("sexy", 1)

            if action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal"]:
                $ character.Statup("Love", 90, 1)
                $ character.Statup("Inbt", 50, 3)
            elif action in ["hotdog"]:
                $ character.Statup("Love", 80, 1)
                $ character.Statup("Inbt", 50, 2)

            $ Line = renpy.random.choice(["Well, sure, put'im here.",
                "Well. . . ok.",
                "Well, sure, give it a rub.",
                "I suppose, drop trou.",
                "Sure, I guess.",
                "Well, sure, stick it in.",
                "Yum.",
                "Well, sure, stick it in.",
                "Sure!",
                "Sure, whip it out.",
                "Fine. . . [She drools a bit into her cleavage].",
                "Heh, ok, alright.",
                "Well, sure, ahhhhhh.",
                "Okay.",
                "I guess I could. . . stick it in.",
                "Hells yeah.",
                "Ok, lemme see it.",
                "Fine. . . [She licks her lips].",
                "I guess. . .",
                "I guess I could. . . whip it out.",
                "Fine. . . [She gestures for you to come over].",
                "Heh, ok, ok."])
            ch_r "[Line]"

            $ Line = 0

        $ character.Statup("Obed", 20, 1)

        if action in ["handjob", "footjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
            $ character.Statup("Obed", 60, 1)
            $ character.Statup("Inbt", 70, 2)
        elif action in ["titjob", "blowjob"]:
            $ character.Statup("Obed", 70, 1)
            $ character.Statup("Inbt", 80, 2)

        if action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass"]:
            call before_handjob
        elif action in ["sex", "anal", "hotdog"]:
            call before_sex

    return

label action_approved(character, action, action_counter):                                                                      #Second time+ dialog
    if character.Forced:
        $ character.FaceChange("sad")
        $ character.Statup("Love", 70, -3, 1)
        $ character.Statup("Love", 20, -2, 1)

        ch_r "That's really what you want?"
        ch_r "That's it?"
        ch_r "This isn't going to become a habit, will it?"
        ch_r "You want me to do that again?"
        ch_r "The toys again?"
        ch_r "That's all you want?"
    elif not Taboo and "tabno" in character.DailyActions:
        ch_r "Ok, I guess this is private enough. . ."
        ch_r "I guess here would be ok. . ."
        ch_r "Well, at least you got us some privacy this time. . ."
    elif action == "anal" and "anal" in character.DailyActions and not character.Loose:
        pass
    elif action in character.RecentActions:
        $ character.FaceChange("sexy", 1)

        ch_r "Mmm, again? Let me flex my hand a bit. . ."
        ch_r "I don't want to wear them out. . ."
        ch_r "Mmm, again? Ok, let me get the girls ready."
        ch_r "Mmm, again? [[stretches her jaw]"
        ch_r "Mmm, again? Ok, let's get to it."
        ch_r "You want to go again? Ok."
        ch_r "I think I'm warmed up. . ."

        if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
            call before_handjob
        elif action in ["sex", "anal", "hotdog"]:
            call before_sex

        return
    elif action in character.DailyActions:
        $ character.FaceChange("sexy", 1)

        $ Line = renpy.random.choice(["Back again so soon?",
            "You're going to give me calluses.",
            "Another one?",
            "Breaking out the toys again?",
            "So you'd like another go?",
            "You can't stay away from this booty. . .",
            "Are you sure that's all you want?"
            "You can't stay away from this. . .",
            "Didn't get enough earlier?",
            "You're going to wear me out.",
            "I'm still a bit sore from earlier.",
            "My arm's still a bit sore from earlier.",
            "My arm's still a bit sore from earlier.",
            "My feet are a bit sore from earlier.",
            "My feet are kinda sore from earlier.",
            "My tits are still a bit sore from earlier.",
            "You're going to give me lockjaw.",
            "Let me get some saliva going.",
            "Didn't get enough earlier?",
            "My jaw's still a bit sore from earlier.",
            "My jaw's still a bit sore from earlier."])
        ch_r "[Line]"
    elif action_counter < 3:
        $ character.FaceChange("sexy", 1)
        $ character.Brows = "confused"
        $ character.Mouth = "kiss"

        ch_r "So you'd like another handy?"
        ch_r "Again?"
        ch_r "So you'd like another titjob?"
        ch_r "So you'd like another blowjob?"
        ch_r "You want to stick it in my pussy again?"
        ch_r "You want to stick it in my ass again?"
        ch_r "So you'd like another go?"
    else:
        $ character.FaceChange("sexy", 1)
        $ character.ArmPose = 2

        $ Line = renpy.random.choice(["You want some of this action?",
            "So you'd like another go?",
            "You want to stick it in my pussy again?",
            "You want to stick it in my ass again?",
            "You want me ta lube up your toy?",
            "You can't stay away from this. . .",
            "You want me to slick your pole?"
            "You can't stay away from this booty.",
            "You want me to ride your pole?",
            "You wanna dip your wick?",
            "So you'd like another handy?",
            "A little. . . [fist pumping hand gestures]?",
            "You want me to grease your skids?",
            "A little tender loving care?",
            "You want me to use my feet?",
            "So you'd like another foot rub?",
            "So you'd like me to. . . [she rubs her foot along your leg]?",
            "So you'd like another foot rub?",
            "You want some of this action [jiggles her tits]?",
            "So you'd like another titjob?",
            "A little. . . bounce?",
            "You want me to pillow your crank?",
            "A little soft embrace?",
            "You want some of this action [mimes blowing]?",
            "So you'd like another blowjob?",
            "A little. . . lick?",
            "You want me to wet your willy?",
            "A little tender loving care?"])
        ch_r "[Line]"

    $ Line = 0

    return

label action_disapproved(character, action, action_counter):
    if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
        $ character.FaceChange("angry", 1)
    elif action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "sex"]:
        $ character.FaceChange("angry")

    if "no_" + action in character.RecentActions:
        call just_told_you_no_lines(character)
        ch_r "I {i}just{/i} told you \"no,\" [character.Petname]."
        ch_r "What part of \"no,\" did you not get, [character.Petname]?"
    elif Taboo and "tabno" in character.DailyActions and "no_" + action in character.DailyActions:
        call had_enough_of_this_lines(character)
        ch_r "I already told you that I wouldn't jerk you off in public!"
        ch_r "This is just way too exposed!"
        ch_r "I already told you that I wouldn't suck you off in public!"
        ch_r "Not in public!"
        ch_r "Stop swinging that thing around in public!"
        ch_r "I already told you that I wouldn't bang you in public!"
        ch_r "I already told you that I wouldn't do that out here!"
        ch_r "I told you that I didn't want you rubb'in up on me in public!"
    elif "no_" + action in character.DailyActions:
        call already_said_no_lines(character)
        ch_r "I already told you \"no,\" [character.Petname]."
        ch_r "I told you \"no\" earlier [character.Petname]."
    elif Taboo and "tabno" in character.DailyActions:
        call already_said_not_here_lines(character)
        ch_r "I already told you this is too public!"
        ch_r "This is just way too exposed!"
        ch_r "I said not in public!"
        ch_r "Stop swinging that thing around in public!"
        ch_r "I already told you that I wouldn't do that out here!"
        ch_r "I told you that I didn't want you rubb'in up on me in public!"
    elif not action_counter:
        $ character.FaceChange("bemused")

        if action not in ["finger_ass", "eat_ass"]:
            call not_ready_yet_lines(character)
            ch_r "I don't really want to touch it, [character.Petname]. . ."
            ch_r "I'm not really up for that, [character.Petname]. . ."
            ch_r "I don't think I'd like the taste, [character.Petname]. . ."
            ch_r ". . . well I don't know about that, [character.Petname]. . ."
            ch_r "I'm just not into toys, [character.Petname]. . ."
            ch_r "I just don't think I'm ready yet, [character.Petname]. . ."
            ch_r "I'm just not into that, [character.Petname]. . ."
            ch_r "That's kinda naughty, [character.Petname]. . ."
        else:
            call not_into_ass_play(character)
    elif action in ["dildo_ass", "anal"] and not character.Loose and action not in character.DailyActions:
        $ character.FaceChange("perplexed")

        ch_r "You could have been a bit more gentle last time, [character.Petname]. . ."
    else:
        $ character.FaceChange("bemused")

        call rather_not_lines(character)
        ch_r "Not right now, [character.Petname]. . ."
        ch_r "Maybe not right now, ok?"
        ch_r "I don't think we need any toys, [character.Petname]."

    call begging_menu(character, action)

    return

label action_rejected(character, action, action_counter):
    if "no_" + action in character.DailyActions:
        $ character.FaceChange("angry", 1)

        call learn_to_take_no_lines(character)
        ch_r "I just don't want to, [character.Petname]."
        ch_r "I'aint tellin you again."
        ch_r "Look, I already told you no thanks, [character.Petname]."
        ch_r "Read my lips, no."
        ch_r "Learn to take \"no\" for an answer, [character.Petname]."

        $ character.AddWord(1,"angry","angry")
    elif character.Forced:
        call went_too_far_lines(character)
        ch_r "I'm not that kind of girl!"
        ch_r "Not even with my feet."
        ch_r "That isn't something I'd want!"
        ch_r "I'm not going to let you use that on me."
        ch_r "I'm not doing that just because you have me over a barrel."
        ch_r "That's a bit much, even for you."
        ch_r "Even that's not worth it."

        if action in ["fondle_thighs"]:
            $ character.Statup("Lust", 50, 2)
            $ character.Statup("Obed", 50, -1)
        elif action in ["hotdog"]:
            $ character.Statup("Lust", 200, 5)

            if character.Love > 300:
                $ character.Statup("Love", 70, -1)

            $ character.Statup("Obed", 50, -1)
        else:
            if action in ["fondle_pussy"]:
                $ character.Statup("Lust", 70, 5)
            elif action in ["eat_pussy"]:
                $ character.Statup("Lust", 80, 5)
            elif action in ["fondle_breasts", "suck_breasts", "fondle_ass"]:
                $ character.Statup("Lust", 60, 5)
            elif action in ["finger_ass", "eat_ass"]:
                if ApprovalCheck(character, 500, "I"):
                    $ character.Statup("Lust", 80, 10)
                else:
                    $ character.Statup("Lust", 50, 3)
            elif action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal"]:
                $ character.Statup("Lust", 200, 5)

                if character.Love > 300:
                    $ character.Statup("Love", 70, -2)

            $ character.Statup("Obed", 50, -2)

        $ character.AddWord(1, "angry", "angry")
    elif Taboo:
        $ character.FaceChange("angry", 1)
        $ character.AddWord(1, "tabno", "tabno")

        call not_in_public_lines(character)
        ch_r "I really don't think this is the right place for that!"
        ch_r "Not in such an exposed place, [character.Petname]."
        ch_r "You really expect me to do that here? You realize how. . . exposed that would be?"
        ch_r "You really expect me to do that here?"
        ch_r "Not here!"
        ch_r "Even if I wanted to, it certainly wouldn't be here!"
        ch_r "That you would even suggest such a thing in a place like this. . ."
        ch_r "I'd be a bit embarassed doing that here."

        if action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
            $ character.Statup("Lust", 200, 5)
            $ character.Statup("Obed", 50, -3)
    elif action in ["dildo_ass", "anal"] and not character.Loose and action in character.DailyActions:
        $ character.FaceChange("bemused")

        ch_r "Sorry, I just need a little break back there, [character.Petname]."
    elif action_counter:
        $ character.FaceChange("sad")

        call you_had_your_shot_lines(character)
        ch_r "I think you can manage it yourself this time. . ."
        ch_r "Not right now, [character.Petname]. . ."
        ch_r "I think I'll let you know when I want you touching these again."
        ch_r "I think I've got the taste out of my mouth, thanks."
        ch_r "Sorry, you can keep your toys to yourself."
        ch_r "Sorry, you can keep your toys out of there."
        ch_r "Maybe you could go fuck yourself instead."
        ch_r "Eh-eh, not anymore, [character.Petname]."
        ch_r "The only thing you can do with my ass is kiss it, [character.Petname].{p}. . .Don't get any ideas."
    else:
        if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "fondle_ass", "handjob", "blowjob", "sex"]:
            $ character.FaceChange("sexy")
            $ character.Mouth = "sad"
        elif action in ["eat_pussy", "finger_ass", "eat_ass", "footjob", "titjob", "dildo_pussy", "dildo_ass", "anal", "hotdog"]:
            $ character.FaceChange("surprised")

        call not_happening_lines(character)
        ch_r "I'd really rather not."
        ch_r "That isn't really how I planned to use my feet today"
        ch_r "How about let's not, [character.Petname]."
        ch_r "Not interested."
        ch_r "No way."
        ch_r "Not happening."

        $ character.FaceChange()

    $ character.RecentActions.append("no_" + action)
    $ character.DailyActions.append("no_" + action)

    $ temp_modifier = 0

    return

label forced_action(character, action):
    if action in ["fondle_thighs", "fondle_breasts"]:
        $ Approval = ApprovalCheck(character, 350, "OI", TabM = 2)
    elif action in ["suck_breasts", "fondle_pussy"]:
        $ Approval = ApprovalCheck(character, 450, "OI", TabM = 3)
    elif action in ["suck_breasts", "blowjob"]:
        $ Approval = ApprovalCheck(character, 750, "OI", TabM = 3)
    elif action in ["eat_pussy"]:
        $ Approval = ApprovalCheck(character, 750, "OI", TabM = 4)
    elif action in ["fondle_ass"]:
        $ Approval = ApprovalCheck(character, 250, "OI", TabM = 3)
    elif action in ["finger_ass", "dildo_pussy"]:
        $ Approval = ApprovalCheck(character, 950, "OI", TabM = 3)
    elif action in ["eat_ass"]:
        $ Approval = ApprovalCheck(character, 1100, "OI", TabM = 4)
    elif action in ["handjob"]:
        $ Approval = ApprovalCheck(character, 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
    elif action in ["footjob", "hotdog"]:
        $ Approval = ApprovalCheck(character, 400, "OI", TabM = 3) # 35, 50, 65, -120(155)
    elif action in ["titjob"]:
        $ Approval = ApprovalCheck(character, 700, "OI", TabM = 4) # 70, 85, 100, -160(230)
    elif action in ["dildo_ass"]:
        $ Approval = ApprovalCheck(character, 1050, "OI", TabM = 3) # 105, 120, 135, -120(225)
    elif action in ["sex"]:
        $ Approval = ApprovalCheck(character, 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
    elif action in ["anal"]:
        $ Approval = ApprovalCheck(character, 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)

    if Approval > 1 or (Approval and character.Forced):
        $ character.FaceChange("sad")

        if action in ["fondle_thighs", "fondle_breasts", "fondle_ass"]:
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Love", 20, -1, 1)
        elif action in ["suck_breasts", "fondle_pussy", "eat_pussy", "finger_ass", "eat_ass"]:
            $ character.Statup("Love", 70, -5, 1)
            $ character.Statup("Love", 20, -2, 1)
        elif action in ["handjob", "footjob", "titjob", "blowjob"]:
            $ character.Statup("Love", 70, -5, 1)
            $ character.Statup("Love", 200, -2)
        elif action in ["dildo_pussy", "dildo_ass", "sex", "anal"]:
            $ character.Statup("Love", 70, -5, 1)
            $ character.Statup("Love", 200, -5)
        elif action in ["hotdog"]:
            $ character.Statup("Love", 70, -2, 1)
            $ character.Statup("Love", 200, -5)

        call forced_but_not_unwelcome_lines(character)
        ch_r "Ok, fine, whip it out."
        ch_r "Ok, fine"
        ch_r "Ok, fine. If we're going to do this, stick it in already."
        ch_r "Ok, fine. Whatever."

        if action == "fondle_thighs":
            $ character.Statup("Obed", 50, 3)
            $ character.Statup("Inbt", 60, 2)
        elif action in ["fondle_breasts", "suck_breasts"]:
            $ character.Statup("Obed", 90, 2)
            $ character.Statup("Obed", 50, 4)
            $ character.Statup("Inbt", 60, 3)
        elif action in ["fondle_pussy", "eat_pussy", "finger_ass", "eat_ass", "handjob", "footjob", "titjob", "blowjob"]:
            $ character.Statup("Obed", 50, 4)
            $ character.Statup("Inbt", 80, 1)
            $ character.Statup("Inbt", 60, 3)
        elif action in ["fondle_ass"]:
            $ character.Statup("Obed", 50, 3)
            $ character.Statup("Inbt", 60, 3)
        elif action in ["dildo_pussy", "dildo_ass", "sex", "anal"]:
            $ character.Statup("Obed", 80, 4)
            $ character.Statup("Inbt", 80, 1)
            $ character.Statup("Inbt", 60, 3)
        elif action in ["hotdog"]:
            $ character.Statup("Obed", 80, 4)
            $ character.Statup("Inbt", 60, 2)

        if Approval < 2:
            $ character.Forced = 1

        if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
            call before_fondle
        elif action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass"]:
            call before_handjob
        elif action in ["sex", "anal", "hotdog"]:
            call before_sex

        return
    else:
        if action in ["fondle_thighs"]:
            $ character.Statup("Love", 200, -8)
        elif action in ["fondle_breasts", "suck_breasts", "fondle_ass", "hotdog"]:
            $ character.Statup("Love", 200, -10)
        elif action in ["fondle_pussy", "eat_pussy", "finger_ass", "eat_ass", "handjob", "footjob", "titjob", "blowjob"]:
            $ character.Statup("Love", 200, -15)
        elif action in ["dildo_pussy", "dildo_ass", "sex", "anal"]:
            $ character.Statup("Love", 200, -20)

        $ character.FaceChange("angry", 1)

        if action in ["fondle_thighs", "fondle_breasts", "fondle_pussy", "fondle_ass", "finger_ass"]:
            "She slaps your hand away."
        elif action in ["suck_breasts"]:
            "She shoves your head back out."
        elif action in ["eat_pussy", "eat_ass"]:
            "She shoves your head back."

        $ character.AddWord(1, "angry", "angry")

    return

label begging_menu(character, action):
    menu:
        extend ""
        "Sorry, never mind." if "no_" + action in character.DailyActions:
            $ character.FaceChange("bemused")

            call no_problem_lines(character)
            ch_r "Yeah, ok, [character.Petname]."
            ch_r "Fine."
            ch_r "No problem."

            return
        "Maybe later?" if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "fondle_ass", "handjob", "footjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"] and "no_" + action not in character.DailyActions:
            $ character.FaceChange("sexy")

            if action == "fondle_breasts" and character not in [LauraX, JubesX]:
                "She re-adjusts her cleavage."

            call maybe_later_lines(character)
            ch_r "I'll give it some thought, [character.Petname]."
            ch_r ". . .{p}I guess?"
            ch_r "We'll have to see."
            ch_r "I might get hungry, [character.Petname]."
            ch_r "Maybe I'll practice on my own time, [character.Petname]."
            ch_r "Yeah, maybe, [character.Petname]."

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
                    call before_fondle
                elif action in ["blowjob"]:
                    $ Line = renpy.random.choice(["Well, sure, ahhhhhh.",
                        "Well. . . ok.",
                        "I guess a taste couldn't hurt.",
                        "I guess I could. . . whip it out.",
                        "Fine. . . [She licks her lips].",
                        "Heh, ok, alright."])
                    ch_r "[Line]"

                    $ Line = 0

                    call before_handjob

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

                                call before_handjob(character, "handjob")
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

                call before_fondle

                return
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

                call before_fondle

                return
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

                call before_handjob

                return
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

                call before_handjob

                return
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

                            call before_handjob(character, "blowjob")

                            return
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

                            call before_handjob(character, "handjob")

                            return
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

                call before_sex
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

                call before_sex
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

                call before_sex
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
