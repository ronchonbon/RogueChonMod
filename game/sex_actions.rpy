label sex_menu(character, action):
    menu:
        "Keep going. . ." if Speed:
            pass
        "Keep going. . . (locked)" if not Speed:
            pass
        "Start moving? . ." if not Speed:
            $ Speed = 1
        "Speed up. . ." if 0 < Speed < 3:
            $ Speed += 1

            "You ask her to up the pace a bit."
        "Speed up. . . (locked)" if Speed >= 3:
            pass
        "Slow Down. . ." if Speed:
            $ Speed -= 1

            "You ask her to slow it down a bit."
        "Slow Down. . . (locked)" if not Speed:
            pass
        "Slap her ass":
            call Slap_Ass(character)

            $ Cnt += 1
            $ Round -= 1

            call sex_cycle(character, action)

            return
        "Turn her around":
            $ character.Pose = "doggy" if character.Pose != "doggy" else "sex"

            "You turn her around. . ."

            call sex_cycle(character, action)

            return
        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
            pass
        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
            "You concentrate on not burning out too quickly."

            $ Player.FocusX = 1
        "Release your focus." if Player.FocusX:
            "You release your concentration. . ."

            $ Player.FocusX = 0
        "Other options":
            menu:
                "Offhand action":
                    if character.Action and MultiAction:
                        call Offhand_Set

                        if Trigger2:
                            $ character.Action -= 1
                    else:
                        call Sex_Basic_Dialog(character,"tired")
                "Shift primary action":
                    if character.Action and MultiAction:
                        menu:
                            "How about sex?" if action != "sex":
                                $ Situation = "shift"

                                call after_sex(character, action)
                                call Rogue_Sex_P
                            "Just stick it in her pussy [[without asking]." if action != "sex":
                                $ Situation = "auto"

                                call after_sex(character, action)
                                call Rogue_Sex_P
                            "How about anal?" if action != "anal":
                                $ Situation = "shift"

                                call after_sex(character, action)
                                call Rogue_Sex_A
                            "Just stick it in her ass [[without asking]." if action != "anal":
                                $ Situation = "auto"

                                call after_sex(character, action)
                                call Rogue_Sex_A
                            "Pull back to hotdog her." if action != "hotdog":
                                $ Situation = "pullback"

                                call after_sex(character, action)
                                call Rogue_Sex_H
                            "Never Mind":
                                pass

                        call sex_cycle(character, action)

                        return
                    else:
                        call tired_lines(character)
                "Threesome actions (locked)" if not Partner:
                    pass
                "Threesome actions" if Partner:
                    menu:
                        "Ask [character.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                            call Les_Change(character)
                        "Ask [character.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                            pass
                        "Ask [Partner.Name] to do something else":
                            call Three_Change(character)
                        "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                            $ ThreeCount = 0
                        "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                            $ ThreeCount = 0
                        "Swap to [Partner.Name]":
                            call Trigger_Swap(character)
                        "Undress [Partner.Name]":
                            call Girl_Undress(Partner)
                            call sex_cycle(character, action)

                            return
                        "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                            pass
                        "Clean up [Partner.Name]" if Partner.Spunk:
                            call Girl_Cleanup(Partner,"ask")
                            call sex_cycle(character, action)

                            return
                        "Never mind":
                            call sex_cycle(character, action)

                            return
                "Just take a look at her.":
                    $ Player.Cock = 0

                    $ Speed = 0
                "Show her feet" if not ShowFeet and (character.Pose == "doggy" or character.Pose == "sex"):
                    $ ShowFeet = 1
                "Hide her feet" if ShowFeet and (character.Pose == "doggy" or character.Pose == "sex"):
                    $ ShowFeet = 0
                "Undress [character.Name]":
                    call Girl_Undress(character)
                "Clean up [character.Name] (locked)" if not character.Spunk:
                    pass
                "Clean up [character.Name]" if character.Spunk:
                    call Girl_Cleanup(character,"ask")
                "Never mind":
                    call sex_cycle(character, action)

                    return
        "Back to Sex Menu" if MultiAction:
            ch_p "Let's try something else."

            call sex_reset(character)

            $ Situation = "shift"
            $ Line = 0

            call after_sex(character, action)

            return
        "End Scene" if not MultiAction:
            ch_p "Let's stop for now."

            call sex_reset(character)

            $ Line = 0

            call after_sex(character, action)

            return

    return

label sex_set_modifier(character, action):
    if action == "sex":
        if character.Sex >= 7: # She loves it
            $ temp_modifier += 15
        elif character.Sex >= 3: #You've done it before several times
            $ temp_modifier += 12
        elif character.Sex: #You've done it before
            $ temp_modifier += 10

        if character.Addict >= 75 and (character.CreamP + character.CreamA) >=3: #She's really strung out and has creampied
            $ temp_modifier += 20
        elif character.Addict >= 75:
            $ temp_modifier += 15

        if character.Lust > 85:
            $ temp_modifier += 10
        elif character.Lust > 75: #She's really horny
            $ temp_modifier += 5

        if Situation == "shift":
            $ temp_modifier += 10
        if "exhibitionist" in character.Traits:
            $ temp_modifier += (4*Taboo)
    elif action == "anal":
        if character.Anal >= 7: # She loves it
            $ temp_modifier += 20
        elif character.Anal >= 3: #You've done it before several times
            $ temp_modifier += 17
        elif character.Anal: #You've done it before
            $ temp_modifier += 15

        if character.Addict >= 75 and (character.CreamP + character.CreamA) >=3: #She's really strung out and has creampied
            $ temp_modifier += 25
        elif character.Addict >= 75:
            $ temp_modifier += 15

        if character.Lust > 85:
            $ temp_modifier += 10
        elif character.Lust > 75: #She's really horny
            $ temp_modifier += 5

        if character.Loose:
            $ temp_modifier += 10
        elif "anal" in character.RecentActions:
            $ temp_modifier -= 20
        elif "anal" in character.DailyActions:
            $ temp_modifier -= 10

        if Situation == "shift":
            $ temp_modifier += 10
        if "exhibitionist" in character.Traits:
            $ temp_modifier += (5*Taboo)
    elif action == "hotdog":
        if character.Hotdog >= 3: #You've done it before several times
            $ temp_modifier += 10
        elif character.Hotdog: #You've done it before
            $ temp_modifier += 5

        if character.Lust > 85:
            $ temp_modifier += 10
        elif character.Lust > 75: #She's really horny
            $ temp_modifier += 5
        if Situation == "shift":
            $ temp_modifier += 10
        if "exhibitionist" in character.Traits:
            $ temp_modifier += (3*Taboo)

    if character in Player.Harem or "sex friend" in character.Petnames:
        $ temp_modifier += 10
    elif "ex" in character.Traits:
        $ temp_modifier -= 40

    if character.ForcedCount and not character.Forced:
        $ temp_modifier -= 5*character.ForcedCount

    if Taboo and "tabno" in character.DailyActions:
        $ temp_modifier -= 10

    if "no_" + action in character.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no_" + action in character.RecentActions else 0

    return

label before_sex(character, action):
    call Seen_First_Peen(character, Partner, React = Situation)

    $ character.Pose = "doggy"

    call sex_launch(character, "hotdog")

    if Situation == character:
        $ Situation = 0

        if action in ["sex", "anal"]:
            if character.PantsNum() == 5:
                call before_sex_skirt_lines(character)

                $ character.Upskirt = 1
            elif character.PantsNum() > 6:
                call before_sex_leg_lines(character)

                $ character.Upskirt = 1
            elif character.PantsNum() == 6:
                call before_sex_shorts_lines(character)

                $ character.Upskirt = 1
            else:
                call before_sex_commando_lines(character)

            $ character.SeenPanties = 1

            if action == "sex":
                "She slides the tip along her pussy and seems to want you to insert it."
            elif action == "anal":
                call anal_wants_to_insert_lines(character)
        else:
            call before_hotdog_lines(character)

        menu:
            "What do you do?"
            "Go with it.":
                $ character.Statup("Inbt", 80, 3)
                $ character.Statup("Inbt", 50, 2)

                "[character.Name] slides it in."
            "Praise her.":
                $ character.FaceChange("sexy", 1)
                $ character.Statup("Inbt", 80, 3)

                if action == "anal" and character == RogueX:
                    ch_p "Ooo, dirty girl, [character.Pet], let's do this."
                elif action == "hotdog" and character == RogueX:
                    ch_p "Hmmm, that's good, [character.Pet]."
                else:
                    ch_p "Oh yeah, [character.Pet], let's do this."

                $ character.NameCheck() #checks reaction to petname

                "[character.Name] slides it in."

                $ character.Statup("Love", 85, 1)
                $ character.Statup("Obed", 90, 1)
                $ character.Statup("Obed", 50, 2)
            "Ask her to stop.":
                $ character.FaceChange("surprised")
                $ character.Statup("Inbt", 70, 1)

                ch_p "Let's not do that right now, [character.Pet]."

                $ character.NameCheck() #checks reaction to petname

                "[character.Name] pulls back."

                $ character.Statup("Obed", 90, 1)
                $ character.Statup("Obed", 50, 1)
                $ character.Statup("Obed", 30, 2)

                $ Player.RecentActions.append("nope")

                $ character.AddWord(1,"refused","refused")

                return

        $ character.PantiesDown = 1

        call first_bottomless(character, 1)
    elif Situation != "auto":
        call AutoStrip(character)

        if Taboo:
            if character in [RogueX, KittyX]:
                if not character.Sex:
                    "[character.Name] glances around for voyeurs. . ."

                    if "cockout" in Player.RecentActions:
                        "[character.Name] slowly presses against your rigid member."
                    else:
                        "She hesitantly pulls down your pants and slowly backs up against your rigid member."

                    "You guide it into place and slide it in."
                else:
                    "[character.Name] glances around to see if anyone notices what she's doing, then backs her ass up against your cock."
                    "You guide your cock into place and ram it home."
            elif character in [EmmaX, LauraX, JeanX, StormX, JubesX]:
                "[character.Name] glances around to see if anyone notices what she's doing."

                if "cockout" in Player.RecentActions:
                    if character in [EmmaX, StormX]:
                        "Then she pushes you back and slowly presses against your rigid member."
                    elif character in [character, JubesX]:
                        "Then she lays back and slowly presses against your rigid member."
                    elif character == JeanX:
                        "Then she turns around and slowly presses against your rigid member."
                else:
                    if character in [EmmaX, StormX]:
                        "Then she pulls down your pants and climbs on top of you."
                    elif character in [character, JubesX]:
                        "Then she pulls down your pants and lays back."
                    elif character == JeanX:
                        "Then she pulls down your pants and turns around."

                    "She slowly presses against your rigid member."

                "She leans back a bit and your cock slides in."

            if character != JeanX:
                $ character.Inbt += int(Taboo/10)
                $ character.Lust += int(Taboo/5)
            else:
                $ JeanX.Statup("Inbt", 90, int(Taboo/10))
                $ JeanX.Statup("Lust", 50, int(Taboo/5))
        else:
            if character in [character, KittyX]:
                if not character.Sex:
                    if "cockout" in Player.RecentActions:
                        "[character.Name] slowly presses against your rigid member."
                    else:
                        "[character.Name] hesitantly pulls down your pants and slowly backs up against your rigid member."

                    "You press her folds aside and nudge your cock in."
                else:
                    "[character.Name] bends over and presses her backside against you suggestively."
                    "You take careful aim and then ram your cock in."
            elif character in [EmmaX, LauraX, JeanX, StormX, JubesX]:
                if "cockout" in Player.RecentActions:
                    if character in [EmmaX, StormX]:
                        "[character.Name] pushes you back and slowly presses against your rigid member."
                    elif character in [character, JubesX]:
                        "[character.Name] lays back and slowly presses against your rigid member."
                    elif character == JeanX:
                        "[character.Name] turns around and slowly presses against your rigid member."
                else:
                    if character in [EmmaX, StormX]:
                        "[character.Name] pulls down your pants and climbs on top of you."
                    elif character in [character, JubesX]:
                        "[character.Name] pulls down your pants and lays back."
                    elif character == JeanX:
                        "[character.Name] pulls down your pants and turns around."

                    "She slowly presses against your rigid member."

                "She leans back a bit and your cock slides in."
    else:
        if (character.PantsNum() > 6 and not character.Upskirt) and (character.Panties and not character.PantiesDown):
            "You quickly pull down her pants and her [character.Panties] and press against her slit."
        elif (character.Panties and not character.PantiesDown):
            "You quickly pull down her [character.Panties] and press against her slit."

        $ character.Upskirt = 1
        $ character.PantiesDown = 1
        $ character.SeenPanties = 1

        call first_bottomless(character, 1)

    if Player.Focus >= 50:
        if character == EmmaX:
            ch_e "My word [character.Petname], your member is hard enough to crack diamond. . . and I should know."
        elif character == LauraX:
            ch_l "Nice to see you're ready for business. . ."
        elif character == JeanX:
            ch_j "I see you won't need any encouragement. . ."
        elif character == StormX:
            ch_s "I must say [character.Petname], you certainly do seem to be. . . excited."

    if action == "sex" and not character.Sex:
        if character.Forced:
            $ character.Statup("Love", 90, -150)
            $ character.Statup("Obed", 70, 60)
            $ character.Statup("Inbt", 80, 50)
        else:
            $ character.Statup("Love", 90, 30)
            $ character.Statup("Obed", 70, 30)
            $ character.Statup("Inbt", 80, 60)
    if action == "anal":
        if not character.Anal:
            if character.Forced:
                $ character.Statup("Love", 90, -150)
                $ character.Statup("Obed", 70, 70)
                $ character.Statup("Inbt", 80, 40)
            else:
                $ character.Statup("Love", 90, 10)
                $ character.Statup("Obed", 70, 30)
                $ character.Statup("Inbt", 80, 70)
        elif not character.Loose:
            if character.Forced:
                $ character.Statup("Love", 90, -20)
                $ character.Statup("Obed", 70, 10)
                $ character.Statup("Inbt", 80, 5)
            else:
                $ character.Statup("Obed", 70, 7)
                $ character.Statup("Inbt", 80, 5)
    elif action == "hotdog" and not character.Hotdog:
        if character.Forced:
            $ character.Statup("Love", 90, -5)
            $ character.Statup("Obed", 70, 20)
            $ character.Statup("Inbt", 80, 10)
        else:
            $ character.Statup("Love", 90, 20)
            $ character.Statup("Obed", 70, 20)
            $ character.Statup("Inbt", 80, 20)

    if Situation:
        $ renpy.pop_call()

        $ Situation = 0

    $ Line = 0
    $ Cnt = 0

    if action == "sex":
        $ Player.Cock = "in"
    elif action == "anal":
        $ Player.Cock = action

    $ Trigger = action
    $ Speed = 1

    if Taboo:
        $ character.DrainWord("tabno")

    $ character.DrainWord("no_" + action)
    $ character.RecentActions.append(action)
    $ character.DailyActions.append(action)

label sex_cycle(character, action):
    while Round > 0:
        call sex_launch(character, action)
        call Shift_Focus(character)

        $ character.LustFace()

        if action == "hotdog" and Speed:
            $ Player.Cock = "out"
        elif action == "sex":
            $ Player.Cock = "in"

        $ Trigger = action

        if Player.Focus < 100:
            call sex_menu(character, action)

        call Shift_Focus(character)
        call Sex_Dialog(character,Partner)

        $ Cnt += 1
        $ Round -= 1

        $ Player.Wet = 1 #wets penis
        $ Player.Spunk = 0 if (Player.Spunk and "in" not in character.Spunk) else Player.Spunk #cleans you off after one cycle

        $ end_cycle = end_of_sex_round(character, action)

        if end_cycle:
            return

    $ character.FaceChange("bemused", 0)

    $ Line = 0

    call im_done_lines(character, 0)
    call after_sex(character, action)

    return

label after_sex(character, action):
    if not Situation:
        $ Player.Sprite = 0
        $ Player.Cock = "out"

        call sex_reset(character)

    $ character.FaceChange("sexy")

    if action == "sex":
        $ character.Sex += 1
    elif action == "anal":
        $ character.Anal += 1
    elif action == "hotdog":
        $ character.Hotdog += 1

    $ character.Action -= 1
    $ character.Addictionrate += 1

    if "addictive" in Player.Traits:
        $ character.Addictionrate += 1

    if action == "sex":
        $ character.Statup("Inbt", 30, 2)
        $ character.Statup("Inbt", 70, 1)

        call Partner_Like(character, 3, 2)
    elif action == "anal":
        $ character.Statup("Inbt", 30, 3)
        $ character.Statup("Inbt", 70, 1)

        if Partner == "Kitty":
            if character == RogueX:
                call Partner_Like(character, 3, 1)
            elif character in [EmmaX, LauraX, JeanX, StormX, JubesX]:
                call Partner_Like(character, 4, 2)
        else:
            if character == RogueX:
                call Partner_Like(character, 4, 2)
            elif character in [EmmaX, LauraX, JeanX, StormX, JubesX]:
                call Partner_Like(character, 3, 2)
    elif action == "hotdog":
        $ character.Statup("Inbt", 30, 1)
        $ character.Statup("Inbt", 70, 1)

        if character == RogueX:
            call Partner_Like(character, 1)
        elif character in [KittyX, EmmaX, LauraX]:
            call Partner_Like(character, 2)

    if action == "sex":
        if expression character.Tag + " Sex Addict" in Achievements:
            pass
        elif character.Sex >= 10:
            $ character.SEXP += 5

            if character == RogueX:
                $ Achievements.append("Rogue Sex Addict")
            elif character == KittyX:
                $ Achievements.append("Kitty Sex Addict")
            elif character == EmmaX:
                $ Achievements.append("Emma Sex Addict")
            elif character == LauraX:
                $ Achievements.append("Laura Sex Addict")
            elif character == JeanX:
                $ Achievements.append("Jean Sex Addict")
            elif character == StormX:
                $ Achievements.append("Storm Sex Addict")
            elif character == JubesX:
                $ Achievements.append("Jubes Sex Addict")

            if not Situation:
                $ character.FaceChange("smile", 1)

                if character == RogueX:
                    ch_r "I think I'm getting addicted to this."
                elif character == KittyX:
                    ch_k "I just can't seem to quit you."
                elif character == EmmaX:
                    ch_e "I seem to fit you like a glove. . ."
                elif character == LauraX:
                    ch_l "We're making this a regular thing, huh. . ."
                elif character == JeanX:
                    ch_j "Hey, I just noticed we've been doing this a lot. . ."
                elif character == StormX:
                    ch_s "We do go well together. . ."
                elif character == JubesX:
                    ch_v "We're making this a regular thing, huh. . ."
        elif character.Sex == 1:
            $ character.SEXP += 20

            if not Situation:
                if character.Love >= 500 and "unsatisfied" not in character.RecentActions:
                    if character == RogueX:
                        ch_r "That was really great, [character.Petname], we'll have to do that again sometime."
                    elif character == KittyX:
                        ch_k "I feel like I've been waiting[character.like]a million years for that."
                    elif character == EmmaX:
                        ch_e "I assume I rocked your entire world."
                    elif character == LauraX:
                        ch_l "I can tell, I was the best you've had."
                    elif character == JeanX:
                        ch_j "Blew your mind, uh?"
                    elif character == StormX:
                        ch_s "I hope that was as enjoyable for you as it was for me."
                    elif character == JubesX:
                        ch_v "I can tell, I was the best you've had."
                elif character.Obed <= 500 and Player.Focus <= 20:
                    $ character.Mouth = "sad"

                    if character == RogueX:
                        ch_r "Did you get what you needed here?"
                    elif character == KittyX:
                        ch_k "I hope that was worth the wait."
                    elif character == EmmaX:
                        ch_e "I hope you enjoyed that."
                    elif character == LauraX:
                        ch_l "Satisfied?"
                    elif character == JeanX:
                        ch_j "Satisfied?"
                    elif character == StormX:
                        ch_s "I hope you found that satisfactory."
                    elif character == JubesX:
                        ch_v "Satisfied?"
        elif character.Sex == 5:
            if character == RogueX:
                ch_r "We're making a regular habit of this."
            elif character == KittyX:
                ch_k "Why did we not do this sooner?!"
            elif character == EmmaX:
                ch_e "We really should have done this sooner."
                ch_e "I can't imagine why I waited so long."
            elif character == LauraX:
                ch_l "You know, this was a good idea."
            elif character == JeanX:
                ch_j "You're pretty good at this. . ."
            elif character == StormX:
                ch_s "You are quite skilled at this."
                ch_s "I am glad you \"bumped into\" me."
            elif character == JubesX:
                ch_v "You know, this was a good idea."
        elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
            if "unsatisfied" in character.RecentActions:
                $ character.FaceChange("angry")

                if character != JeanX:
                    $ character.Eyes = "side"

                call didnt_get_off_lines(character)

                if character == RogueX:
                    ch_r "I didn't exactly get off there. . ."
                elif character == KittyX:
                    ch_k "Could you have maybe paid more attention? . ."
                elif character == EmmaX:
                    ch_e "Could you have perhaps been more attentive? . ."
                elif character == LauraX:
                    ch_l "Forgetting someone? . ."
                elif character == JeanX:
                    ch_j "I think you need to get back down there."
                elif character == StormX:
                    ch_s "I could have used some more attention to my needs. . ."
                elif character == JubesX:
                    ch_v "Forgetting someone? . ."
    elif action == "anal":
        if expression character.Tag + " Anal Addict" in Achievements:
            pass
        elif character.Anal >= 10:
            $ character.SEXP += 7

            if character == RogueX:
                $ Achievements.append("Rogue Anal Addict")
            elif character == KittyX:
                $ Achievements.append("Kitty Anal Addict")
            elif character == EmmaX:
                $ Achievements.append("Emma Anal Addict")
            elif character == LauraX:
                $ Achievements.append("Laura Anal Addict")
            elif character == JeanX:
                $ Achievements.append("Jean Anal Addict")
            elif character == StormX:
                $ Achievements.append("Storm Anal Addict")
            elif character == JubesX:
                $ Achievements.append("Jubes Anal Addict")

            if not Situation:
                $ character.FaceChange("bemused", 1)

                if character == RogueX:
                    ch_r "I. . . really think I enjoy this. . ."
                elif character == KittyX:
                    ch_k "I didn't think I'd love this so much!"
                elif character == EmmaX:
                    ch_e "You're one of the better partners I've had at that."
                elif character == LauraX:
                    ch_l "I think you've got a knack for that."
                elif character == JeanX:
                    ch_j "This has been fun exercise."
                elif character == StormX:
                    ch_s "I have certainly come to enjoy this."
                elif character == JubesX:
                    ch_v "I think you've got a knack for that."
        elif character.Anal == 1:
                $character.SEXP += 25

                if not Situation:
                    if character.Love >= 500 and "unsatisfied" not in character.RecentActions:
                        if character == RogueX:
                            ch_r "That was . . . interesting [character.Petname]. We'll have to do that again sometime."
                        elif character == KittyX:
                            ch_k "Anal. . . huh, who knew?"
                        elif character == EmmaX:
                            ch_e "You really took to that well."
                        elif character == LauraX:
                            ch_l "You seem to know your way around back there."
                        elif character == JeanX:
                            ch_j "Hmmm, that was nice. . ."
                        elif character == StormX:
                            ch_s "Well. . ."
                            ch_s "That was quite an experience. . ."
                        elif character == JubesX:
                            ch_v "You seem to know your way around back there."
                    elif character.Obed <= 500 and Player.Focus <= 20:
                        $ character.Mouth = "sad"

                        if character == RogueX:
                            ch_r "Ouch."
                            ch_r "Did you get what you needed here?"
                        elif character == KittyX:
                            ch_k "Ouch."
                            ch_k "I guess you got what you needed?"
                        elif character == EmmaX:
                            ch_e "Oooh."
                            ch_e "It's been a while."
                        elif character == LauraX:
                            ch_l "That was pleasant."
                        elif character == JeanX:
                            ch_j "That was great. . ."
                        elif character == StormX:
                            ch_s "Well. . ."
                            ch_s "That was quite an experience. . ."
                        elif character == JubesX:
                            ch_v "That was pleasant."
        elif character.Anal == 5:
            if character == RogueX:
                ch_r "We're making a regular habit of this."
            elif character == KittyX:
                ch_k "I'm really starting to love this."
            elif character == EmmaX:
                ch_e "You're pretty good at that."
            elif character == LauraX:
                ch_l "I'm glad you're into this."
            elif character == JeanX:
                ch_j "I'm glad we have similar interests. . ."
            elif character == StormX:
                ch_s "You do certainly make the experience enjoyable."
            elif character == JubesX:
                ch_v "I'm glad you're into this."
        elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
            if "unsatisfied" in character.RecentActions:
                $ character.FaceChange("angry")

                if character != JeanX:
                    $ character.Eyes = "side"

                call didnt_get_off_lines(character)

                if character == RogueX:
                    ch_r "I didn't exactly get off there. . ."
                elif character == KittyX:
                    ch_k "Could you have maybe paid more attention? . ."
                elif character == EmmaX:
                    ch_e "Could you have perhaps been more attentive? . ."
                elif character == LauraX:
                    ch_l "Forgetting someone? . ."
                elif character == JeanX:
                    ch_j "I think you need to get back down there."
                elif character == StormX:
                    ch_s "I could have used some more attention to my needs. . ."
                elif character == JubesX:
                    ch_v "Forgetting someone? . ."

                if character == RogueX:
                    ch_r "That didn't really do it for me. . ."
                elif character == KittyX:
                    ch_k "I didn't get much out of that. . ."
                elif character == EmmaX:
                    ch_e "I'm afraid that didn't do much for me. . ."
                elif character == LauraX:
                    ch_l "That didn't do much for me. . ."
                elif character == JeanX:
                    ch_j "I think you need to get back down there."
                elif character == StormX:
                    ch_s "I am afraid that did not do much for me. . ."
                elif character == JubesX:
                    ch_v "That didn't do much for me. . ."

                if character == RogueX:
                    ch_r "Hmm, you seemed to get more out of that than me. . ."
                elif character == KittyX:
                    ch_k "Hmm, you seemed to get more out of that than me. . ."
                elif character == EmmaX:
                    ch_e "Hmm, you seemed to get more out of that than I did. . ."
                elif character == LauraX:
                    ch_l "Forgetting someone? . ."
                elif character == JeanX:
                    ch_j "I think you need to get back down there."
                elif character == StormX:
                    ch_s "I am afraid that you got more out of that than me. . ."
                elif character == JubesX:
                    ch_v "Forgetting someone? . ."
    if action == "hotdog":
        if expression character.Tag + " Full Buns" in Achievements:
            pass
        elif character.Anal >= 10:
            $ character.SEXP += 5

            if character == RogueX:
                $ Achievements.append("Rogue Full Buns")
            elif character == KittyX:
                $ Achievements.append("Kitty Full Buns")
            elif character == EmmaX:
                $ Achievements.append("Emma Full Buns")
            elif character == LauraX:
                $ Achievements.append("Laura Full Buns")
            elif character == JeanX:
                $ Achievements.append("Jean Full Buns")
            elif character == StormX:
                $ Achievements.append("Storm Full Buns")
            elif character == JubesX:
                $ Achievements.append("Jubes Full Buns")

            if character == RogueX and not Situation:
                $ character.FaceChange("smile", 1)

                ch_r "I think I'm getting addicted to this."
        elif character.Hotdog == 1:
            $ character.SEXP += 10

            if not Situation:
                if character.Love >= 500 and "unsatisfied" not in character.RecentActions:
                    if character == RogueX:
                        ch_r "That was pretty hot, [character.Petname], we'll have to do that again sometime."
                    elif character == KittyX:
                        ch_k "I. . . liked that a lot."
                    elif character == EmmaX:
                        ch_e "That was. . . pleasant."
                    elif character == LauraX:
                        ch_l "That was. . . nice."
                    elif character == JeanX:
                        ch_j "Ok, that was. . . fine."
                    elif character == StormX:
                        ch_s "That was. . . enjoyable."
                    elif character == JubesX:
                        ch_v "That was. . . nice."
                elif character.Obed <= 500 and Player.Focus <= 20:
                    $ character.Mouth = "sad"

                    if character == RogueX:
                        ch_r "Did you get what you needed here?"
                    elif character == KittyX:
                        ch_k "Well, did that work for you?"
                    elif character == EmmaX:
                        ch_e "Was that enough for you?"
                    elif character == LauraX:
                        ch_l "Enough for you?"
                    elif character == JeanX:
                        ch_j "I guess that could have gone worse. . ."
                    elif character == StormX:
                        ch_s "Was that satisfactory?"
                    elif character == JubesX:
                        ch_v "Enough for you?"
        elif character.Hotdog == 5:
            if character == RogueX:
                ch_r "This is. . . interesting."
            elif character == KittyX:
                ch_k "I'm surprised how much I enjoy this."
        elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
            if "unsatisfied" in character.RecentActions:
                $ character.FaceChange("angry")

                if character != JeanX:
                    $ character.Eyes = "side"

                call didnt_get_off_lines(character)

                if character == RogueX:
                    ch_r "That didn't really do it for me. . ."
                elif character == KittyX:
                    ch_k "I didn't get much out of that. . ."
                elif character == EmmaX:
                    ch_e "I'm afraid that didn't do much for me. . ."
                elif character == LauraX:
                    ch_l "That didn't do much for me. . ."
                elif character == JeanX:
                    ch_j "I think you need to get back down there."
                elif character == StormX:
                    ch_s "I am afraid that did not do much for me. . ."
                elif character == JubesX:
                    ch_v "That didn't do much for me. . ."

    $ temp_modifier = 0

    call Checkout

    return

label end_of_sex_round(character, action):
    $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus

    if Player.Focus >= 100 or character.Lust >= 100:
        if Player.Focus >= 100:
            call Player_Cumming(character)

            if "angry" in character.RecentActions:
                call sex_reset(character)

                return True

            $ character.Statup("Lust", 200, 5)

            if 100 > character.Lust >= 70 and character.OCount < 2:
                $ character.AddWord(0, "unsatisfied", "unsatisfied")

            if Player.Focus > 80:
                call after_sex(character, action)

                return True

            $ Line = "came"

        if character.Lust >= 100:
            call Girl_Cumming(character)

            if Situation == "shift" or "angry" in character.RecentActions:
                call after_sex(character, action)

                return True

        if Line == "came": #ex Player.Focus <= 20:
            $ Line = 0

            if not Player.Semen:
                "She's emptied you out, you'll need to take a break."

                call after_sex(character, action)

                return True
            elif "unsatisfied" in character.RecentActions:#And Rogue is unsatisfied,
                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.",
                    "She is breathing heavily as your cock rubs inside her.",
                    "She slowly turns back towards you and smiles.",
                    "She doesn't seem ready to stop."])
                "[Line]"
                "Keep going?"

                menu:
                    extend ""
                    "Yes, keep going for a bit." if Player.Semen:
                        $ Line = "You get back into it"
                    "No, I'm done." if Player.Semen:
                        "You pull back."

                        call after_sex(character, action)

                        return True
                    "No, I'm spent." if not Player.Semen:
                        "You pull back."

                        call after_sex(character, action)

                        return True

    if Partner and Partner.Lust >= 100:
        call Girl_Cumming(Partner)

    $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

    if action == "sex":
        $ bonus = character.Sex
    elif action == "anal":
        $ bonus = character.Anal
    elif action == "hotdog":
        $ bonus = character.Hotdog

    if character.SEXP >= 100 or ApprovalCheck(character, 1200, "LO"):
        pass
    elif Cnt == (5 + bonus):
        $ character.Brows = "confused"

        call getting_close_lines(character)
        ch_r "Are you getting close here? I'm getting a little sore."
        ch_r "Are you getting close here?"
    elif Cnt == (10 + bonus):
        $ character.Brows = "angry"

        call done_with_this_lines(character)
        ch_r "I'm . . .getting . . .worn out. . . here, . . [character.Petname]."
        ch_r "I'm kinda done with this, [character.Petname]."

        call can_we_do_something_else(character)
        ch_r "Can we. . . do something. . . else?"

        menu:
            extend ""
            "How about a BJ?" if character.Action and MultiAction:
                if action != "anal":
                    $ Situation = "shift"

                    call after_sex(character, action)
                    call blowjob(character)
                else:
                    if character.Anal >= 5 and character.Blow >= 10 and character.SEXP >= 50:
                        $ Situation = "shift"

                        call after_sex(character, action)
                        call blowjob(character)
                    else:
                        call no_ass_to_mouth_lines(character)
                        ch_r "No thanks, [character.Petname]. Maybe a Handy instead?"

                        $ Situation = "shift"

                        call after_sex(character, action)
                        call before_handjob(character, "handjob")
            "How about a Handy?" if character.Action and MultiAction:
                $ Situation = "shift"

                call after_sex(character, action)
                call handjob(character)
            "Finish up.":
                "You release your concentration. . ."

                $ Player.FocusX = 0
                $ Player.Focus += 15

                call after_sex(character, action)

                return True
            "Let's try something else." if MultiAction:
                $ Line = 0
                $ Situation = "shift"

                call after_sex(character, action)

                return True
            "No, get back down there.":
                if ApprovalCheck(character, 1200) or ApprovalCheck(character, 500, "O"):
                    $ character.Statup("Love", 200, -5)
                    $ character.Statup("Obed", 50, 3)
                    $ character.Statup("Obed", 80, 2)

                    "She grumbles but lets you keep going."
                else:
                    $ character.FaceChange("angry", 1)

                    call reset_position(character)

                    "She scowls at you and pulls back."

                    call this_is_boring_lines(character)

                    $ character.Statup("Love", 50, -3, 1)
                    $ character.Statup("Love", 80, -4, 1)
                    $ character.Statup("Obed", 30, -1, 1)
                    $ character.Statup("Obed", 50, -1, 1)
                    $ character.AddWord(1,"angry","angry")

                    call after_sex(character, action)

                    return True

    call Escalation(character)

    if Round == 10:
        call wrap_this_up_lines(character)
    elif Round == 5:
        call time_to_stop_soon_lines(character)

    return False





label before_anal(character):


    elif Situation != "auto":
        call AutoStrip(character)

        if Taboo:
            if character not in [EmmaX, LauraX, JeanX, StormX, JubesX]:
                if character.Anal:
                    "[character.Name] glances around to see if anyone notices what she's doing, then backs her ass up against your cock."
                    "You guide your cock into place and ram it home."
                else:
                    "[character.Name] glances around for voyeurs. . ."

                    if "cockout" in Player.RecentActions:
                        "[character.Name] slowly presses against your rigid member."
                    else:
                        if character == RogueX:
                            "[character.Name] hesitantly pulls down your pants and slowly backs up against your rigid member."
                        elif character == KittyX:
                            "[character.Name] hesitantly pulls down your pants and slowly presses against your rigid member."

                    "You guide it into place and slide it in."
            else:
                "[character.Name] glances around to see if anyone notices what she's doing."

                if "cockout" in Player.RecentActions:
                    if character in [EmmaX, StormX]:
                        "Then she pushes you back and slowly presses against your rigid member."
                    elif character in [character, JubesX]:
                        "Then she lays back and slowly presses against your rigid member."
                    elif character == JeanX:
                        "Then she turns around and slowly presses against your rigid member."
                else:
                    if character in [EmmaX, StormX]:
                        "Then she pulls down your pants and climbs on top of you."
                    elif character in [character, JubesX]:
                        "Then she pulls down your pants and lays back."
                    elif character == JeanX:
                        "Then she pulls down your pants and turns around."

                    "She slowly presses against your rigid member."

                "She leans back a bit and your cock pops in."


        else:
            if character not in [EmmaX, LauraX, JeanX, StormX, JubesX]:
                if not character.Anal:
                    if character == RogueX:
                        "[character.Name] bends over and presses her backside against you suggestively."
                    elif character == KittyX:
                        "[character.Name] leans back and presses against you suggestively."

                    "You take careful aim and then push your cock in."
                else:
                    if "cockout" in Player.RecentActions:
                        "[character.Name] slowly presses against your rigid member."
                    else:
                        if character == RogueX:
                            "[character.Name] hesitantly pulls down your pants and slowly backs up against your rigid member."
                        elif character == KittyX:
                            "[character.Name] hesitantly pulls down your pants and slowly presses against your rigid member."

                    "You press against her rim and nudge your cock in."
            else:
                if "cockout" in Player.RecentActions:
                    if character in [EmmaX, StormX]:
                        "[character.Name] pushes you back and slowly presses against your rigid member."
                    elif character in [character, JubesX]:
                        "[character.Name] lays back and slowly presses against your rigid member."
                    elif character == JeanX:
                        "[character.Name] turns around and slowly presses against your rigid member."
                else:
                    if character in [EmmaX, StormX]:
                        "[character.Name] pulls down your pants and climbs on top of you."
                    elif character in [character, JubesX]:
                        "[character.Name] pulls down your pants and lays back."
                    elif character == JeanX:
                        "[character.Name] pulls down your pants and turns around."

                    "She slowly presses against your rigid member."

                "She leans back a bit and your cock pops in."
    else:
        if (character.PantsNum() > 6 and not character.Upskirt) and (character.Panties and not character.PantiesDown):
            if character == RogueX:
                "You quickly pull down her pants and her [character.Panties] and press against her ass."
            elif character in [character, EmmaX, LauraX, JeanX, StormX, JubesX]:
                "You quickly pull down her pants and her [character.Panties] and press against her back door."
        elif (character.Panties and not character.PantiesDown):
            if character == RogueX:
                "You quickly pull down her [character.Panties] and press against her ass."
            elif character in [character, EmmaX, LauraX, JeanX, StormX, JubesX]:
                "You quickly pull down her [character.Panties] and press against her back door."





label before_hotdog(character):

        menu:
            "What do you do?"
            "Go with it.":
                $ character.Statup("Inbt", 50, 3)

                if character in [character, EmmaX, StormX]:
                    "[character.Name] starts to grind against you."
                elif character == KittyX:
                    "[character.Name] keeps grinding."
                elif character in [character, JeanX, JubesX]:
                    "[character.Name] continues to grind."
            "Praise her.":
                $ character.FaceChange("sexy", 1)
                $ character.Statup("Inbt", 80, 2)

                if character in [character, EmmaX, StormX]:
                    "[character.Name] starts to grind against you."
                elif character == KittyX:
                    "[character.Name] keeps grinding."
                elif character in [character, JeanX, JubesX]:
                    "[character.Name] continues to grind."

                $ character.Statup("Love", 85, 1)
                $ character.Statup("Obed", 60, 2)
            "Ask her to stop.":

                $ character.Statup("Obed", 80, 1)
                $ character.Statup("Obed", 30, 2)

                return
    elif Situation != "auto":
        call Bottoms_Off(character)

        if Taboo:
            if character not in [EmmaX, LauraX, JeanX, StormX, JubesX]:
                if character.Hotdog:
                    "[character.Name] glances around to see if anyone notices what she's doing, then backs her ass up against your cock."
                else:
                    "[character.Name] glances around for voyeurs. . ."

                    if "cockout" in Player.RecentActions:
                        "[character.Name] slowly presses against your rigid member."
                    else:
                        if character == RogueX:
                            "[character.Name] hesitantly pulls down your pants and slowly backs up against your rigid member."
                        elif character == KittyX:
                            "[character.Name] hesitantly pulls down your pants and slowly presses against your rigid member."
            else:
                "[character.Name] glances around to see if anyone notices what she's doing."

                if "cockout" in Player.RecentActions:
                    if character in [EmmaX, StormX]:
                        "Then she pushes you back and slowly presses against your rigid member."
                    elif character in [character, JubesX]:
                        "Then she lays back and slowly presses against your rigid member."
                    elif character == JeanX:
                        "Then she turns around and slowly presses against your rigid member."
                else:
                    if character in [EmmaX, StormX]:
                        "Then she pulls down your pants and climbs on top of you."
                    elif character in [character, JubesX]:
                        "Then she pulls down your pants and lays back."
                    elif character == JeanX:
                        "Then she pulls down your pants and turns around."

                    "She slowly presses against your rigid member."

            if character != JeanX:
                $ character.Inbt += int(Taboo/10)
                $ character.Lust += int(Taboo/5)
            else:
                $ JeanX.Statup("Inbt", 90, int(Taboo/10))
                $ JeanX.Statup("Lust", 50, int(Taboo/5))
        else:
            if character not in [EmmaX, LauraX, JeanX, StormX, JubesX]:
                if not character.Hotdog:
                    if character == RogueX:
                        "[character.Name] bends over and presses her backside against you suggestively."
                    elif character == KittyX:
                        "[character.Name] leans back and presses against you suggestively."
                else:
                    if "cockout" in Player.RecentActions:
                        "[character.Name] slowly presses against your rigid member."
                    else:
                        if character == RogueX:
                            "[character.Name] hesitantly pulls down your pants and slowly backs up against your rigid member."
                        elif character == KittyX:
                            "[character.Name] hesitantly pulls down your pants and slowly presses against your rigid member."
            else:
                if "cockout" in Player.RecentActions:
                    if character in [EmmaX, StormX]:
                        "[character.Name] pushes you back and slowly presses against your rigid member."
                    elif character in [character, JubesX]:
                        "[character.Name] lays back and slowly presses against your rigid member."
                    elif character == JeanX:
                        "[character.Name] turns around and slowly presses against your rigid member."
                else:
                    if character in [EmmaX, StormX]:
                        "[character.Name] pulls down your pants and climbs on top of you."
                    elif character in [character, JubesX]:
                        "[character.Name] pulls down your pants and lays back."
                    elif character == JeanX:
                        "[character.Name] pulls down your pants and turns around."

                    "She slowly presses against your rigid member."
    else:
        if character == RogueX:
            "You press yourself against her ass."
        elif character == KittyX:
            "You press yourself against her mound."
        elif character in [EmmaX, StormX]:
            "You roll back, pulling her on top of you and your rigid member."
        elif character in [character, JubesX]:
            "She lays back, pulling you against her with your rigid member."
        elif character == JeanX:
            "She turns around, pulling you against her with your rigid member."
