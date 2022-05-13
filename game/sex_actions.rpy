label sex_menu:
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
            call Slap_Ass(Player.focused_girl)

            $ Cnt += 1
            $ Round -= 1

            jump sex_cycle
        "Turn her around":
            $ Player.focused_girl.Pose = "doggy" if Player.focused_girl.Pose != "doggy" else "sex"

            "You turn her around. . ."

            jump sex_cycle
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
                    if Player.focused_girl.Action and MultiAction:
                        call Offhand_Set

                        if Trigger2:
                            $ Player.focused_girl.Action -= 1
                    else:
                        call Sex_Basic_Dialog(Player.focused_girl,"tired")
                "Shift primary action":
                    if Player.focused_girl.Action and MultiAction:
                        menu:
                            "How about sex?" if Player.primary_action != "sex":
                                $ Situation = "shift"

                                call after_sex(Player.focused_girl, Player.primary_action)
                                call sex(Player.focused_girl)
                            "Just stick it in her pussy [[without asking]." if Player.primary_action != "sex":
                                $ Situation = "auto"

                                call after_sex(Player.focused_girl, Player.primary_action)
                                call sex(Player.focused_girl)
                            "How about anal?" if Player.primary_action != "anal":
                                $ Situation = "shift"

                                call after_sex(Player.focused_girl, Player.primary_action)
                                call anal(Player.focused_girl)
                            "Just stick it in her ass [[without asking]." if Player.primary_action != "anal":
                                $ Situation = "auto"

                                call after_sex(Player.focused_girl, Player.primary_action)
                                call anal(Player.focused_girl)
                            "Pull back to hotdog her." if Player.primary_action != "hotdog":
                                $ Situation = "pullback"

                                call after_sex(Player.focused_girl, Player.primary_action)
                                call hotdog(Player.focused_girl)
                            "Never Mind":
                                jump sex_cycle
                    else:
                        call tired_lines(Player.focused_girl)
                "Threesome actions (locked)" if not Partner:
                    pass
                "Threesome actions" if Partner:
                    menu:
                        "Ask [Player.focused_girl.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                            call Les_Change(Player.focused_girl)
                        "Ask [Player.focused_girl.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                            pass
                        "Ask [Partner.Name] to do something else":
                            call Three_Change(Player.focused_girl)
                        "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                            $ ThreeCount = 0
                        "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                            $ ThreeCount = 0
                        "Swap to [Partner.Name]":
                            call Trigger_Swap(Player.focused_girl)
                        "Undress [Partner.Name]":
                            call Girl_Undress(Partner)
                            jump sex_cycle
                        "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                            pass
                        "Clean up [Partner.Name]" if Partner.Spunk:
                            call Girl_Cleanup(Partner,"ask")
                            jump sex_cycle
                        "Never mind":
                            jump sex_cycle
                "Just take a look at her.":
                    $ Player.Cock = 0

                    $ Speed = 0
                "Show her feet" if not ShowFeet and (Player.focused_girl.Pose == "doggy" or Player.focused_girl.Pose == "sex"):
                    $ ShowFeet = 1
                "Hide her feet" if ShowFeet and (Player.focused_girl.Pose == "doggy" or Player.focused_girl.Pose == "sex"):
                    $ ShowFeet = 0
                "Undress [Player.focused_girl.Name]":
                    call Girl_Undress(Player.focused_girl)
                "Clean up [Player.focused_girl.Name] (locked)" if not Player.focused_girl.Spunk:
                    pass
                "Clean up [Player.focused_girl.Name]" if Player.focused_girl.Spunk:
                    call Girl_Cleanup(Player.focused_girl,"ask")
                "Never mind":
                    jump sex_cycle
        "Back to Sex Menu" if MultiAction:
            ch_p "Let's try something else."

            call sex_reset(Player.focused_girl)

            $ Situation = "shift"
            $ Line = 0

            jump after_sex
        "End Scene" if not MultiAction:
            ch_p "Let's stop for now."

            call sex_reset(Player.focused_girl)

            $ Line = 0

            jump after_sex

    jump sex_menu_return

label before_sex:
    call Seen_First_Peen(Player.focused_girl, Partner, React = Situation)

    $ Player.focused_girl.Pose = "doggy"

    call sex_launch(Player.focused_girl, "hotdog")

    if Situation == Player.focused_girl:
        $ Situation = 0

        call Player.focused_girl_initiated_action(Player.focused_girl, Player.primary_action)

        if _return:
            return

        $ Player.focused_girl.PantiesDown = 1

        call first_bottomless(Player.focused_girl, 1)
    elif Situation != "auto":
        call AutoStrip(Player.focused_girl)

        call start_of_sex_narration(Player.focused_girl, Player.primary_action)
    else:
        if Player.primary_action in ["sex", "anal"]:
            if Player.primary_action == "sex":
                $ word = renpy.random.choice(["slit"])
            elif Player.primary_action == "anal":
                $ word = renpy.random.choice(["ass", "back door"])

            if (Player.focused_girl.PantsNum() > 6 and not Player.focused_girl.Upskirt) and (Player.focused_girl.Panties and not Player.focused_girl.PantiesDown):
                "You quickly pull down her pants and her [Player.focused_girl.Panties] and press against her [word]."
            elif (Player.focused_girl.Panties and not Player.focused_girl.PantiesDown):
                "You quickly pull down her [Player.focused_girl.Panties] and press against her [word]."

            $ Player.focused_girl.Upskirt = 1
            $ Player.focused_girl.PantiesDown = 1
            $ Player.focused_girl.SeenPanties = 1

            call first_bottomless(Player.focused_girl, 1)
        elif Player.primary_action == "hotdog":
            $ line = renpy.random.choice(["You press yourself against her ass.",
                "You press yourself against her mound.",
                "You roll back, pulling her on top of you and your rigid member.",
                "She lays back, pulling you against her with your rigid member.",
                "She turns around, pulling you against her with your rigid member."])
            "[line]"

    if Player.Focus >= 50:
        if Player.focused_girl == EmmaX:
            ch_e "My word [Player.focused_girl.Petname], your member is hard enough to crack diamond. . . and I should know."
        elif Player.focused_girl == LauraX:
            ch_l "Nice to see you're ready for business. . ."
        elif Player.focused_girl == JeanX:
            ch_j "I see you won't need any encouragement. . ."
        elif Player.focused_girl == StormX:
            ch_s "I must say [Player.focused_girl.Petname], you certainly do seem to be. . . excited."

    if Player.primary_action == "sex" and not Player.focused_girl.Sex:
        if Player.focused_girl.Forced:
            $ Player.focused_girl.Statup("Love", 90, -150)
            $ Player.focused_girl.Statup("Obed", 70, 60)
            $ Player.focused_girl.Statup("Inbt", 80, 50)
        else:
            $ Player.focused_girl.Statup("Love", 90, 30)
            $ Player.focused_girl.Statup("Obed", 70, 30)
            $ Player.focused_girl.Statup("Inbt", 80, 60)
    if Player.primary_action == "anal":
        if not Player.focused_girl.Anal:
            if Player.focused_girl.Forced:
                $ Player.focused_girl.Statup("Love", 90, -150)
                $ Player.focused_girl.Statup("Obed", 70, 70)
                $ Player.focused_girl.Statup("Inbt", 80, 40)
            else:
                $ Player.focused_girl.Statup("Love", 90, 10)
                $ Player.focused_girl.Statup("Obed", 70, 30)
                $ Player.focused_girl.Statup("Inbt", 80, 70)
        elif not Player.focused_girl.Loose:
            if Player.focused_girl.Forced:
                $ Player.focused_girl.Statup("Love", 90, -20)
                $ Player.focused_girl.Statup("Obed", 70, 10)
                $ Player.focused_girl.Statup("Inbt", 80, 5)
            else:
                $ Player.focused_girl.Statup("Obed", 70, 7)
                $ Player.focused_girl.Statup("Inbt", 80, 5)
    elif Player.primary_action == "hotdog" and not Player.focused_girl.Hotdog:
        if Player.focused_girl.Forced:
            $ Player.focused_girl.Statup("Love", 90, -5)
            $ Player.focused_girl.Statup("Obed", 70, 20)
            $ Player.focused_girl.Statup("Inbt", 80, 10)
        else:
            $ Player.focused_girl.Statup("Love", 90, 20)
            $ Player.focused_girl.Statup("Obed", 70, 20)
            $ Player.focused_girl.Statup("Inbt", 80, 20)

    if Situation:
        $ renpy.pop_call()

        $ Situation = 0

    $ Line = 0
    $ Cnt = 0

    if Player.primary_action == "sex":
        $ Player.Cock = "in"
    elif Player.primary_action == "anal":
        $ Player.Cock = action

    $ Trigger = action
    $ Speed = 1

    if Taboo:
        $ Player.focused_girl.DrainWord("tabno")

    $ Player.focused_girl.DrainWord("no_" + Player.primary_action)
    $ Player.focused_girl.RecentActions.append(action)
    $ Player.focused_girl.DailyActions.append(action)

label sex_cycle:
    while Round > 0:
        call Shift_Focus(Player.focused_girl)
        call sex_launch(Player.focused_girl, Player.primary_action)

        $ Player.focused_girl.LustFace()

        if Player.primary_action == "hotdog" and Speed:
            $ Player.Cock = "out"
        elif Player.primary_action == "sex":
            $ Player.Cock = "in"

        $ Trigger = action

        if Player.Focus < 100:
            jump sex_menu

            label sex_menu_return:

        call Shift_Focus(Player.focused_girl)
        call Sex_Dialog(Player.focused_girl,Partner)

        $ Cnt += 1
        $ Round -= 1

        $ Player.Wet = 1 #wets penis
        $ Player.Spunk = 0 if (Player.Spunk and "in" not in Player.focused_girl.Spunk) else Player.Spunk #cleans you off after one cycle

        call end_of_sex_round(Player.focused_girl, Player.primary_action)

        if _return:
            return

    $ Player.focused_girl.FaceChange("bemused", 0)

    $ Line = 0

    call im_done_lines(Player.focused_girl, 0)
    call after_sex(Player.focused_girl, Player.primary_action)

    return

label after_sex:
    if not Situation:
        $ Player.Sprite = 0
        $ Player.Cock = "out"

        call sex_reset(Player.focused_girl)

    $ Player.focused_girl.FaceChange("sexy")

    if Player.primary_action == "sex":
        $ Player.focused_girl.Sex += 1
    elif Player.primary_action == "anal":
        $ Player.focused_girl.Anal += 1
    elif Player.primary_action == "hotdog":
        $ Player.focused_girl.Hotdog += 1

    $ Player.focused_girl.Action -= 1
    $ Player.focused_girl.Addictionrate += 1

    if "addictive" in Player.Traits:
        $ Player.focused_girl.Addictionrate += 1

    if Player.primary_action == "sex":
        $ Player.focused_girl.Statup("Inbt", 30, 2)
        $ Player.focused_girl.Statup("Inbt", 70, 1)

        call Partner_Like(Player.focused_girl, 3, 2)
    elif Player.primary_action == "anal":
        $ Player.focused_girl.Statup("Inbt", 30, 3)
        $ Player.focused_girl.Statup("Inbt", 70, 1)

        if Partner == "Kitty":
            if Player.focused_girl == RogueX:
                call Partner_Like(Player.focused_girl, 3, 1)
            elif Player.focused_girl in [EmmaX, LauraX, JeanX, StormX, JubesX]:
                call Partner_Like(Player.focused_girl, 4, 2)
        else:
            if Player.focused_girl == RogueX:
                call Partner_Like(Player.focused_girl, 4, 2)
            elif Player.focused_girl in [EmmaX, LauraX, JeanX, StormX, JubesX]:
                call Partner_Like(Player.focused_girl, 3, 2)
    elif Player.primary_action == "hotdog":
        $ Player.focused_girl.Statup("Inbt", 30, 1)
        $ Player.focused_girl.Statup("Inbt", 70, 1)

        if Player.focused_girl == RogueX:
            call Partner_Like(Player.focused_girl, 1)
        elif Player.focused_girl in [KittyX, EmmaX, LauraX]:
            call Partner_Like(Player.focused_girl, 2)

    if Player.primary_action == "sex":
        if Player.focused_girl.Tag + " Sex Addict" in Achievements:
            pass
        elif Player.focused_girl.Sex >= 10:
            $ Player.focused_girl.SEXP += 5

            $ Achievements.append(Player.focused_girl.Tag + " Sex Addict")

            if not Situation:
                $ Player.focused_girl.FaceChange("smile", 1)

                if Player.focused_girl == RogueX:
                    ch_r "I think I'm getting addicted to this."
                elif Player.focused_girl == KittyX:
                    ch_k "I just can't seem to quit you."
                elif Player.focused_girl == EmmaX:
                    ch_e "I seem to fit you like a glove. . ."
                elif Player.focused_girl == LauraX:
                    ch_l "We're making this a regular thing, huh. . ."
                elif Player.focused_girl == JeanX:
                    ch_j "Hey, I just noticed we've been doing this a lot. . ."
                elif Player.focused_girl == StormX:
                    ch_s "We do go well together. . ."
                elif Player.focused_girl == JubesX:
                    ch_v "We're making this a regular thing, huh. . ."
        elif Player.focused_girl.Sex == 1:
            $ Player.focused_girl.SEXP += 20

            if not Situation:
                if Player.focused_girl.Love >= 500 and "unsatisfied" not in Player.focused_girl.RecentActions:
                    if Player.focused_girl == RogueX:
                        ch_r "That was really great, [Player.focused_girl.Petname], we'll have to do that again sometime."
                    elif Player.focused_girl == KittyX:
                        ch_k "I feel like I've been waiting[Player.focused_girl.like]a million years for that."
                    elif Player.focused_girl == EmmaX:
                        ch_e "I assume I rocked your entire world."
                    elif Player.focused_girl == LauraX:
                        ch_l "I can tell, I was the best you've had."
                    elif Player.focused_girl == JeanX:
                        ch_j "Blew your mind, uh?"
                    elif Player.focused_girl == StormX:
                        ch_s "I hope that was as enjoyable for you as it was for me."
                    elif Player.focused_girl == JubesX:
                        ch_v "I can tell, I was the best you've had."
                elif Player.focused_girl.Obed <= 500 and Player.Focus <= 20:
                    $ Player.focused_girl.Mouth = "sad"

                    if Player.focused_girl == RogueX:
                        ch_r "Did you get what you needed here?"
                    elif Player.focused_girl == KittyX:
                        ch_k "I hope that was worth the wait."
                    elif Player.focused_girl == EmmaX:
                        ch_e "I hope you enjoyed that."
                    elif Player.focused_girl == LauraX:
                        ch_l "Satisfied?"
                    elif Player.focused_girl == JeanX:
                        ch_j "Satisfied?"
                    elif Player.focused_girl == StormX:
                        ch_s "I hope you found that satisfactory."
                    elif Player.focused_girl == JubesX:
                        ch_v "Satisfied?"
        elif Player.focused_girl.Sex == 5:
            if Player.focused_girl == RogueX:
                ch_r "We're making a regular habit of this."
            elif Player.focused_girl == KittyX:
                ch_k "Why did we not do this sooner?!"
            elif Player.focused_girl == EmmaX:
                ch_e "We really should have done this sooner."
                ch_e "I can't imagine why I waited so long."
            elif Player.focused_girl == LauraX:
                ch_l "You know, this was a good idea."
            elif Player.focused_girl == JeanX:
                ch_j "You're pretty good at this. . ."
            elif Player.focused_girl == StormX:
                ch_s "You are quite skilled at this."
                ch_s "I am glad you \"bumped into\" me."
            elif Player.focused_girl == JubesX:
                ch_v "You know, this was a good idea."
        elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
            if "unsatisfied" in Player.focused_girl.RecentActions:
                $ Player.focused_girl.FaceChange("angry")

                if Player.focused_girl != JeanX:
                    $ Player.focused_girl.Eyes = "side"

                call didnt_get_off_lines(Player.focused_girl)

                if Player.focused_girl == RogueX:
                    ch_r "I didn't exactly get off there. . ."
                elif Player.focused_girl == KittyX:
                    ch_k "Could you have maybe paid more attention? . ."
                elif Player.focused_girl == EmmaX:
                    ch_e "Could you have perhaps been more attentive? . ."
                elif Player.focused_girl == LauraX:
                    ch_l "Forgetting someone? . ."
                elif Player.focused_girl == JeanX:
                    ch_j "I think you need to get back down there."
                elif Player.focused_girl == StormX:
                    ch_s "I could have used some more attention to my needs. . ."
                elif Player.focused_girl == JubesX:
                    ch_v "Forgetting someone? . ."
    elif Player.primary_action == "anal":
        if Player.focused_girl.Tag + " Anal Addict" in Achievements:
            pass
        elif Player.focused_girl.Anal >= 10:
            $ Player.focused_girl.SEXP += 7

            $ Achievements.append(Player.focused_girl.Tag + " Anal Addict")

            if not Situation:
                $ Player.focused_girl.FaceChange("bemused", 1)

                if Player.focused_girl == RogueX:
                    ch_r "I. . . really think I enjoy this. . ."
                elif Player.focused_girl == KittyX:
                    ch_k "I didn't think I'd love this so much!"
                elif Player.focused_girl == EmmaX:
                    ch_e "You're one of the better partners I've had at that."
                elif Player.focused_girl == LauraX:
                    ch_l "I think you've got a knack for that."
                elif Player.focused_girl == JeanX:
                    ch_j "This has been fun exercise."
                elif Player.focused_girl == StormX:
                    ch_s "I have certainly come to enjoy this."
                elif Player.focused_girl == JubesX:
                    ch_v "I think you've got a knack for that."
        elif Player.focused_girl.Anal == 1:
                $Player.focused_girl.SEXP += 25

                if not Situation:
                    if Player.focused_girl.Love >= 500 and "unsatisfied" not in Player.focused_girl.RecentActions:
                        if Player.focused_girl == RogueX:
                            ch_r "That was . . . interesting [Player.focused_girl.Petname]. We'll have to do that again sometime."
                        elif Player.focused_girl == KittyX:
                            ch_k "Anal. . . huh, who knew?"
                        elif Player.focused_girl == EmmaX:
                            ch_e "You really took to that well."
                        elif Player.focused_girl == LauraX:
                            ch_l "You seem to know your way around back there."
                        elif Player.focused_girl == JeanX:
                            ch_j "Hmmm, that was nice. . ."
                        elif Player.focused_girl == StormX:
                            ch_s "Well. . ."
                            ch_s "That was quite an experience. . ."
                        elif Player.focused_girl == JubesX:
                            ch_v "You seem to know your way around back there."
                    elif Player.focused_girl.Obed <= 500 and Player.Focus <= 20:
                        $ Player.focused_girl.Mouth = "sad"

                        if Player.focused_girl == RogueX:
                            ch_r "Ouch."
                            ch_r "Did you get what you needed here?"
                        elif Player.focused_girl == KittyX:
                            ch_k "Ouch."
                            ch_k "I guess you got what you needed?"
                        elif Player.focused_girl == EmmaX:
                            ch_e "Oooh."
                            ch_e "It's been a while."
                        elif Player.focused_girl == LauraX:
                            ch_l "That was pleasant."
                        elif Player.focused_girl == JeanX:
                            ch_j "That was great. . ."
                        elif Player.focused_girl == StormX:
                            ch_s "Well. . ."
                            ch_s "That was quite an experience. . ."
                        elif Player.focused_girl == JubesX:
                            ch_v "That was pleasant."
        elif Player.focused_girl.Anal == 5:
            if Player.focused_girl == RogueX:
                ch_r "We're making a regular habit of this."
            elif Player.focused_girl == KittyX:
                ch_k "I'm really starting to love this."
            elif Player.focused_girl == EmmaX:
                ch_e "You're pretty good at that."
            elif Player.focused_girl == LauraX:
                ch_l "I'm glad you're into this."
            elif Player.focused_girl == JeanX:
                ch_j "I'm glad we have similar interests. . ."
            elif Player.focused_girl == StormX:
                ch_s "You do certainly make the experience enjoyable."
            elif Player.focused_girl == JubesX:
                ch_v "I'm glad you're into this."
        elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
            if "unsatisfied" in Player.focused_girl.RecentActions:
                $ Player.focused_girl.FaceChange("angry")

                if Player.focused_girl != JeanX:
                    $ Player.focused_girl.Eyes = "side"

                call didnt_get_off_lines(Player.focused_girl)

                if Player.focused_girl == RogueX:
                    ch_r "I didn't exactly get off there. . ."
                elif Player.focused_girl == KittyX:
                    ch_k "Could you have maybe paid more attention? . ."
                elif Player.focused_girl == EmmaX:
                    ch_e "Could you have perhaps been more attentive? . ."
                elif Player.focused_girl == LauraX:
                    ch_l "Forgetting someone? . ."
                elif Player.focused_girl == JeanX:
                    ch_j "I think you need to get back down there."
                elif Player.focused_girl == StormX:
                    ch_s "I could have used some more attention to my needs. . ."
                elif Player.focused_girl == JubesX:
                    ch_v "Forgetting someone? . ."

                if Player.focused_girl == RogueX:
                    ch_r "That didn't really do it for me. . ."
                elif Player.focused_girl == KittyX:
                    ch_k "I didn't get much out of that. . ."
                elif Player.focused_girl == EmmaX:
                    ch_e "I'm afraid that didn't do much for me. . ."
                elif Player.focused_girl == LauraX:
                    ch_l "That didn't do much for me. . ."
                elif Player.focused_girl == JeanX:
                    ch_j "I think you need to get back down there."
                elif Player.focused_girl == StormX:
                    ch_s "I am afraid that did not do much for me. . ."
                elif Player.focused_girl == JubesX:
                    ch_v "That didn't do much for me. . ."

                if Player.focused_girl == RogueX:
                    ch_r "Hmm, you seemed to get more out of that than me. . ."
                elif Player.focused_girl == KittyX:
                    ch_k "Hmm, you seemed to get more out of that than me. . ."
                elif Player.focused_girl == EmmaX:
                    ch_e "Hmm, you seemed to get more out of that than I did. . ."
                elif Player.focused_girl == LauraX:
                    ch_l "Forgetting someone? . ."
                elif Player.focused_girl == JeanX:
                    ch_j "I think you need to get back down there."
                elif Player.focused_girl == StormX:
                    ch_s "I am afraid that you got more out of that than me. . ."
                elif Player.focused_girl == JubesX:
                    ch_v "Forgetting someone? . ."
    if Player.primary_action == "hotdog":
        if Player.focused_girl.Tag + " Full Buns" in Achievements:
            pass
        elif Player.focused_girl.Anal >= 10:
            $ Player.focused_girl.SEXP += 5

            $ Achievements.append(Player.focused_girl.Tag + " Full Buns")

            if Player.focused_girl == RogueX and not Situation:
                $ Player.focused_girl.FaceChange("smile", 1)

                ch_r "I think I'm getting addicted to this."
        elif Player.focused_girl.Hotdog == 1:
            $ Player.focused_girl.SEXP += 10

            if not Situation:
                if Player.focused_girl.Love >= 500 and "unsatisfied" not in Player.focused_girl.RecentActions:
                    if Player.focused_girl == RogueX:
                        ch_r "That was pretty hot, [Player.focused_girl.Petname], we'll have to do that again sometime."
                    elif Player.focused_girl == KittyX:
                        ch_k "I. . . liked that a lot."
                    elif Player.focused_girl == EmmaX:
                        ch_e "That was. . . pleasant."
                    elif Player.focused_girl == LauraX:
                        ch_l "That was. . . nice."
                    elif Player.focused_girl == JeanX:
                        ch_j "Ok, that was. . . fine."
                    elif Player.focused_girl == StormX:
                        ch_s "That was. . . enjoyable."
                    elif Player.focused_girl == JubesX:
                        ch_v "That was. . . nice."
                elif Player.focused_girl.Obed <= 500 and Player.Focus <= 20:
                    $ Player.focused_girl.Mouth = "sad"

                    if Player.focused_girl == RogueX:
                        ch_r "Did you get what you needed here?"
                    elif Player.focused_girl == KittyX:
                        ch_k "Well, did that work for you?"
                    elif Player.focused_girl == EmmaX:
                        ch_e "Was that enough for you?"
                    elif Player.focused_girl == LauraX:
                        ch_l "Enough for you?"
                    elif Player.focused_girl == JeanX:
                        ch_j "I guess that could have gone worse. . ."
                    elif Player.focused_girl == StormX:
                        ch_s "Was that satisfactory?"
                    elif Player.focused_girl == JubesX:
                        ch_v "Enough for you?"
        elif Player.focused_girl.Hotdog == 5:
            if Player.focused_girl == RogueX:
                ch_r "This is. . . interesting."
            elif Player.focused_girl == KittyX:
                ch_k "I'm surprised how much I enjoy this."
        elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
            if "unsatisfied" in Player.focused_girl.RecentActions:
                $ Player.focused_girl.FaceChange("angry")

                if Player.focused_girl != JeanX:
                    $ Player.focused_girl.Eyes = "side"

                call didnt_get_off_lines(Player.focused_girl)

                if Player.focused_girl == RogueX:
                    ch_r "That didn't really do it for me. . ."
                elif Player.focused_girl == KittyX:
                    ch_k "I didn't get much out of that. . ."
                elif Player.focused_girl == EmmaX:
                    ch_e "I'm afraid that didn't do much for me. . ."
                elif Player.focused_girl == LauraX:
                    ch_l "That didn't do much for me. . ."
                elif Player.focused_girl == JeanX:
                    ch_j "I think you need to get back down there."
                elif Player.focused_girl == StormX:
                    ch_s "I am afraid that did not do much for me. . ."
                elif Player.focused_girl == JubesX:
                    ch_v "That didn't do much for me. . ."

    $ temp_modifier = 0

    call Checkout

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

label sex(character):
    $ Player.primary_action = "sex"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(character)
    call sex_set_modifier(character, "sex")

    $ Approval = ApprovalCheck(character, 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)

    if Situation == "auto":
        $ character.Pose = "doggy"

        call sex_launch(character, "sex")

        if character.PantsNum() == 5:
            "You press up against [character.Name]'s backside, sliding her skirt up as you go."

            $ character.Upskirt = 1
        elif character.PantsNum() > 6:
            "You press up against [character.Name]'s backside, sliding her pants down as you do."

            $ character.Legs = 0
        else:
            "You press up against [character.Name]'s backside."

        $ character.SeenPanties = 1

        "You rub the tip of your cock against her moist slit."

        $ character.FaceChange("surprised", 1)

        if (character.Sex and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
            "[character.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."

            $ character.FaceChange("sexy")
            $ character.Statup("Obed", 70, 3)
            $ character.Statup("Inbt", 50, 3)
            $ character.Statup("Inbt", 70, 1)

            ch_r "Ok, [character.Petname], let's do this."

            jump before_sex
        else:                                                                                                            #she's questioning it
            $ character.Brows = "angry"

            menu:
                ch_r "Hey, what do you think you're doing back there?!"
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ character.FaceChange("sexy", 1)
                        $ character.Statup("Obed", 70, 3)
                        $ character.Statup("Inbt", 50, 3)
                        $ character.Statup("Inbt", 70, 1)

                        ch_r "Well, since you're be'in so nice about it, I guess we can give it a go. . ."

                        jump before_sex
                    "You pull back before you really get it in."

                    $ character.FaceChange("bemused", 1)

                    if character.Sex:
                        ch_r "Well ok, [character.Petname], no harm done. Just give me a little warning next time."
                    else:
                        ch_r "Well ok, [character.Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."
                "Just fucking.":
                    $ character.Statup("Love", 80, -10, 1)
                    $ character.Statup("Love", 200, -10)

                    "You press inside some more."

                    $ character.Statup("Obed", 70, 3)
                    $ character.Statup("Inbt", 50, 3)

                    if not ApprovalCheck(character, 700, "O", TabM=1):   #Checks if Obed is 700+
                        $ character.FaceChange("angry")

                        "[character.Name] shoves you away and slaps you in the face."
                        ch_r "Jackass!"
                        ch_r "If that's how you want to treat me, we're done here!"

                        $ character.Statup("Love", 50, -10, 1)
                        $ character.Statup("Obed", 50, 3)

                        $ renpy.pop_call()

                        if Situation:
                            $ renpy.pop_call()

                        call sex_reset(character)

                        $ character.RecentActions.append("angry")
                        $ character.DailyActions.append("angry")
                    else:
                        $ character.FaceChange("sad")

                        "[character.Name] doesn't seem to be into this, you're lucky she's so obedient."

                        jump before_sex
        return

    if not character.Sex and "no sex" not in character.RecentActions:                           #first time
        $ character.FaceChange("surprised", 1)
        $ character.Mouth = "kiss"

        ch_r "So, you'd like to take this to the next level? actionual sex? . . ."

        if character.Forced:
            $ character.FaceChange("sad")

            ch_r "You'd really take it that far?"

    if not character.Sex and Approval:                                                  #First time dialog
        call first_action_approval(character, "sex")
    elif Approval:
        call action_approved(character, "sex", character.Sex)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(character, "sex")

        return
    else:                                                                               #She's not into it, but maybe. . .
        call action_disapproved(character, "sex", character.Sex)

    $ character.ArmPose = 1

    call action_rejected(character, "sex", character.Sex)

    return

label anal(character):
    $ Player.primary_action = "anal"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(character)
    call sex_set_modifier(character, "anal")

    $ Approval = ApprovalCheck(character, 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)

    if Situation == "auto":
        $ character.Pose = "doggy"

        call sex_launch(character, "anal")

        if character.PantsNum() == 5:
            "You press up against [character.Name]'s backside, sliding her skirt up as you go."

            $ character.Upskirt = 1
        elif character.PantsNum() > 6:
            "You press up against [character.Name]'s backside, sliding her pants down as you do."

            $ character.Legs = 0
        else:
            "You press up against [character.Name]'s backside."

        $ character.SeenPanties = 1

        "You press the tip of your cock against her tight rim."

        $ character.FaceChange("surprised", 1)

        if (character.Anal and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
            "[character.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."

            $ character.FaceChange("sexy")
            $ character.Statup("Obed", 70, 3)
            $ character.Statup("Inbt", 50, 3)
            $ character.Statup("Inbt", 70, 1)

            ch_r "Hmm, stick it in. . ."

            jump before_sex
        else:                                                                                                            #she's questioning it
            $ character.Brows = "angry"

            menu:
                ch_r "Hey, what do you think you're doing back there?!"
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ character.FaceChange("sexy", 1)
                        $ character.Statup("Obed", 70, 3)
                        $ character.Statup("Inbt", 50, 3)
                        $ character.Statup("Inbt", 70, 1)

                        ch_r "I guess if you really want to try it. . ."

                        jump before_sex
                    "You pull back before you really get it in."

                    $ character.FaceChange("bemused", 1)

                    if character.Anal:
                        ch_r "Well ok, [character.Petname], no harm done. Just give me a little warning next time."
                    else:
                        ch_r "Well ok, [character.Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."
                "Just fucking.":
                    $ character.Statup("Love", 80, -10, 1)
                    $ character.Statup("Love", 200, -8)

                    "You press into her."

                    $ character.Statup("Obed", 70, 3)
                    $ character.Statup("Inbt", 50, 3)

                    if not ApprovalCheck(character, 700, "O", TabM=1):
                        $ character.FaceChange("angry")

                        "[character.Name] shoves you away and slaps you in the face."
                        ch_r "Jackass!"
                        ch_r "If that's how you want to treat me, we're done here!"

                        $ character.Statup("Love", 50, -10, 1)
                        $ character.Statup("Obed", 50, 3)

                        $ renpy.pop_call()

                        if Situation:
                            $ renpy.pop_call()

                        call sex_reset(character)

                        $ character.RecentActions.append("angry")
                        $ character.DailyActions.append("angry")
                    else:
                        $ character.FaceChange("sad")

                        "[character.Name] doesn't seem to be into this, you're lucky she's so obedient."

                        jump before_sex
        return

    if not character.Anal and "no anal" not in character.RecentActions:                                                               #first time
        $ character.FaceChange("surprised", 1)
        $ character.Mouth = "kiss"

        ch_r "Wait, so you want to stick it in my butt?!"

        if character.Forced:
            $ character.FaceChange("sad")

            ch_r "Seriously?"

    if not character.Loose and ("dildo anal" in character.DailyActions or "anal" in character.DailyActions):
        $ character.FaceChange("bemused", 1)

        ch_r "I'm still a little sore from earlier."
    elif "anal" in character.RecentActions:
        $ character.FaceChange("sexy", 1)

        ch_r "You want to go again? Ok."

        call before_sex

    if not character.Anal and Approval:                                                 #First time dialog
        call first_action_approval(character, "anal")
    elif Approval:
        call action_approved(character, "anal", character.Anal)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(character, "anal")

        return
    else:                                                                               #She's not into it, but maybe. . .
        call action_disapproved(character, "anal", character.Anal)

    $ character.ArmPose = 1

    call action_rejectd(character, "anal", character.Anal)

    return

label hotdog(character):
    $ Player.primary_action = "hotdog"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(character)
    call sex_set_modifier(character, "hotdog")

    $ Approval = ApprovalCheck(character, 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)

    if Situation == "auto":
        $ character.Pose = "doggy"

        call sex_launch("hotdog")

        "You press up against [character.Name]'s backside."

        $ character.FaceChange("surprised", 1)

        if (character.Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
            "[character.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."

            $ character.FaceChange("sexy")
            $ character.Statup("Obed", 70, 3)
            $ character.Statup("Inbt", 50, 3)
            $ character.Statup("Inbt", 70, 1)

            ch_r "Hmm, I've apparently got someone's attention. . ."

            jump before_sex
        else:                                                                                                            #she's questioning it
            $ character.Brows = "angry"

            menu:
                ch_r "Hmm, kinda rude, [character.Petname]."
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ character.FaceChange("sexy", 1)
                        $ character.Statup("Obed", 70, 3)
                        $ character.Statup("Inbt", 50, 3)
                        $ character.Statup("Inbt", 70, 1)

                        ch_r "I guess it doesn't feel so bad. . ."

                        jump before_sex

                    "You pull back before you really get it in."

                    $ character.FaceChange("bemused", 1)

                    if character.Hotdog:
                        ch_r "Well ok, [character.Petname], it has been kinda fun."
                    else:
                        ch_r "Well ok, [character.Petname], that's a bit dirty, maybe ask a girl?"
                "You'll see.":
                    $ character.Statup("Love", 80, -10, 1)
                    $ character.Statup("Love", 200, -8)

                    "You grind against her asscrack."

                    $ character.Statup("Obed", 70, 3)
                    $ character.Statup("Inbt", 50, 3)

                    if not ApprovalCheck(character, 500, "O", TabM=1): #Checks if Obed is 700+
                        $ character.FaceChange("angry")

                        "[character.Name] shoves you away."
                        ch_r "Dick!"
                        ch_r "If that's how you want want to act, I'm out of here!"

                        $ character.Statup("Love", 50, -10, 1)
                        $ character.Statup("Obed", 50, 3)

                        $ renpy.pop_call()

                        if Situation:
                            $ renpy.pop_call()

                        call sex_reset(character)

                        $ character.RecentActions.append("angry")
                        $ character.DailyActions.append("angry")
                    else:
                        $ character.FaceChange("sad")

                        "[character.Name] doesn't seem to be into this, but she knows her place."

                        jump before_sex
        return

    if not character.Hotdog and "no hotdog" not in character.RecentActions:                                                               #first time
        $ character.FaceChange("surprised", 1)
        $ character.Mouth = "kiss"

        ch_r "Wait, so you want to grind against my butt?!"

        if character.Forced:
            $ character.FaceChange("sad")

            ch_r ". . . That's all?"

    if not character.Hotdog and Approval:                                                 #First time dialog
        call first_action_approval(character, "hotdog")
    elif Approval:                                                                       #Second time+ dialog
        call action_approved(character, "hotdog", character.Hotdog)

    if Approval >= 2:                                                                   #She's into it. . .
        call action_accepted(character, "hotdog")

        return
    else:                                                                               #She's not into it, but maybe. . .
        call action_rejected(character, "hotdog", character.Hotdog)

    $ character.ArmPose = 1

    call action_rejected(character, "hotdog", character.Hotdog)

    return
