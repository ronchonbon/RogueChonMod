label sex_prep(character):
    call Seen_First_Peen(character, Partner, React = Situation)

    $ character.Pose = "doggy"

    call expression character.Tag + "_Sex_Launch('hotdog')"

    if Situation == character:
        $ Situation = 0

        if character.PantsNum() == 5:
            if character == RogueX:
                "[character.Name] turns and backs up against your cock, sliding her skirt up as she does so."
            elif character == KittyX:
                "[character.Name] rolls back and pulls you toward her, sliding her skirt up as she does so."
            elif character == EmmaX:
                "[character.Name] pushes you back and climbs on top of you, sliding her skirt up as she does so."
            elif character == LauraX:
                "[character.Name] lays back, sliding her skirt up as she does so."
            elif character == JeanX:
                "[JeanX.Name] turns around, sliding her skirt up as she does so."
            elif character == StormX:
                "[StormX.Name] pushes you back and climbs on top of you, sliding her skirt up as she does so."
            elif character == JubesX:
                "[JubesX.Name] lays back, sliding her skirt up as she does so."

            $ character.Upskirt = 1
        elif character.PantsNum() > 6:
            if character == RogueX:
                "[character.Name] turns and backs up against your cock, sliding her pants down as she does so."
            elif character == KittyX:
                "[character.Name] rolls back and pulls you against her, sliding her pants off as she does so."
            elif character == EmmaX:
                "[character.Name] pushes you down and climbs on top of you, sliding her [character.Legs] down as she does so."
            elif character == LauraX:
                "[LauraX.Name] lays back, sliding her [LauraX.Legs] down as she does so."
            elif character == JeanX:
                "[JeanX.Name] turns around, sliding her [JeanX.Legs] down as she does so."
            elif character == StormX:
                "[StormX.Name] pushes you down and climbs on top of you, sliding her [StormX.Legs] down as she does so."
            elif character == JubesX:
                "[JubesX.Name] lays back, sliding her [JubesX.Legs] down as she does so."

            $ character.Upskirt = 1
        elif character.PantsNum() == 6:
            if character == KittyX:
                "[character.Name] rolls onto her back and pulls you against her, sliding her shorts off as she does so."

            $ character.Upskirt = 1
        else:
            if character == RogueX:
                "[character.Name] turns and backs up against your cock."
            elif character == KittyX:
                "[character.Name] rolls back and pulls you toward her."
            elif character == EmmaX:
                "[character.Name] pushes you back and climbs on top of you."
            elif character == LauraX:
                "[LauraX.Name] rolls back and pulls you toward her."
            elif character == JeanX:
                "[JeanX.Name] turns around and pulls you toward her."
            elif character == StormX:
                "[StormX.Name] pushes you back and climbs on top of you."
            elif character == JubesX:
                "[JubesX.Name] rolls back and pulls you toward her."

        $ character.SeenPanties = 1

        "She slides the tip along her pussy and seems to want you to insert it."

        menu:
            "What do you do?"
            "Go with it.":
                $ character.Statup("Inbt", 80, 3)
                $ character.Statup("Inbt", 50, 2)

                "[character.Name] slides it in."
            "Praise her.":
                $ character.FaceChange("sexy", 1)
                $ character.Statup("Inbt", 80, 3)

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

        call expression character.Tag + "_First_Bottomless(1)"
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
                    elif character in [LauraX, JubesX]:
                        "Then she lays back and slowly presses against your rigid member."
                    elif character == JeanX:
                        "Then she turns around and slowly presses against your rigid member."
                else:
                    if character in [EmmaX, StormX]:
                        "Then she pulls down your pants and climbs on top of you."
                    elif character in [LauraX, JubesX]:
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
            if character in [RogueX, KittyX]:
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
                    elif character in [LauraX, JubesX]:
                        "[character.Name] lays back and slowly presses against your rigid member."
                    elif character == JeanX:
                        "[JeanX.Name] turns around and slowly presses against your rigid member."
                else:
                    if character in [EmmaX, StormX]:
                        "[character.Name] pulls down your pants and climbs on top of you."
                    elif character in [LauraX, JubesX]:
                        "[character.Name] pulls down your pants and lays back."
                    elif character == JeanX:
                        "[JeanX.Name] pulls down your pants and turns around."

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

        call expression character.Tag + "_First_Bottomless(1)"

    if Player.Focus >= 50:
        if character == EmmaX:
            ch_e "My word [character.Petname], your member is hard enough to crack diamond. . . and I should know."
        elif character == LauraX:
            ch_l "Nice to see you're ready for business. . ."
        elif character == JeanX:
            ch_j "I see you won't need any encouragement. . ."
        elif character == StormX:
            ch_s "I must say [StormX.Petname], you certainly do seem to be. . . excited."

    if not character.Sex:
        if character.Forced:
            $ character.Statup("Love", 90, -150)
            $ character.Statup("Obed", 70, 60)
            $ character.Statup("Inbt", 80, 50)
        else:
            $ character.Statup("Love", 90, 30)
            $ character.Statup("Obed", 70, 30)
            $ character.Statup("Inbt", 80, 60)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0

    $ Line = 0
    $ Cnt = 0

    $ Player.Cock = "in"

    $ Trigger = "sex"
    $ Speed = 1

    if Taboo:
        $ character.DrainWord("tabno")

    $ character.DrainWord("no sex")
    $ character.RecentActions.append("sex")
    $ character.DailyActions.append("sex")

label sex_after(character):
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        $ Player.Sprite = 0
        $ Player.Cock = "out"

        call expression character.Tag + "_Sex_Reset"

    $ character.FaceChange("sexy")

    $ character.Sex += 1
    $ character.Action -=1
    $ character.Addictionrate += 1

    if "addictive" in Player.Traits:
        $ character.Addictionrate += 1

    $ character.Statup("Inbt", 30, 2)
    $ character.Statup("Inbt", 70, 1)

    call Partner_Like(character, 3, 2)

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
                    ch_k "I feel like I've been waiting[KittyX.like]a million years for that."
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

    $ temp_modifier = 0

    call Checkout

    return

label anal_prep(character):
    call Seen_First_Peen(character, Partner, React = Situation)

    if character in [RogueX]:
        $ character.Pose = "doggy"

    call expression character.Tag + "_Sex_Launch('hotdog')"

    if Situation == character:
        $ Situation = 0

        if character.PantsNum() == 5:
            if character == RogueX:
                "[character.Name] turns and backs up against your cock, sliding her skirt up as she does so."
            elif character == KittyX:
                "[character.Name] rolls back and pulls you toward her, sliding her skirt up as she does so."
            elif character == EmmaX:
                "[character.Name] pushes you back and climbs on top of you, sliding her skirt up as she does so."
            elif character == LauraX:
                "[character.Name] lays back, sliding her skirt up as she does so."
            elif character == JeanX:
                "[JeanX.Name] turns around, sliding her skirt up as she does so."
            elif character == StormX:
                "[StormX.Name] pushes you back and climbs on top of you, sliding her skirt up as she does so."
            elif character == JubesX:
                "[JubesX.Name] lays back, sliding her skirt up as she does so."

            $ character.Upskirt = 1
        elif character.PantsNum() > 6:
            if character == RogueX:
                "[character.Name] turns and backs up against your cock, sliding her pants down as she does so."
            elif character == KittyX:
                "[character.Name] rolls back and pulls you against her, sliding her pants off as she does so."
            elif character == EmmaX:
                "[character.Name] pushes you down and climbs on top of you, sliding her [character.Legs] down as she does so."
            elif character == LauraX:
                "[LauraX.Name] lays back, sliding her [LauraX.Legs] down as she does so."
            elif character == JeanX:
                "[JeanX.Name] turns around, sliding her [JeanX.Legs] down as she does so."
            elif character == StormX:
                "[StormX.Name] pushes you down and climbs on top of you, sliding her [StormX.Legs] down as she does so."
            elif character == JubesX:
                "[JubesX.Name] lays back, sliding her [JubesX.Legs] down as she does so."

            $ character.Upskirt = 1
        elif character.PantsNum() == 6:
            if character == KittyX:
                "[character.Name] rolls onto her back and pulls you against her, sliding her shorts off as she does so."

            $ character.Upskirt = 1
        else:
            if character == RogueX:
                "[character.Name] turns and backs up against your cock."
            elif character == KittyX:
                "[character.Name] rolls back and pulls you toward her."
            elif character == EmmaX:
                "[character.Name] pushes you back and climbs on top of you."
            elif character == LauraX:
                "[LauraX.Name] rolls back and pulls you toward her."
            elif character == JeanX:
                "[JeanX.Name] turns around and pulls you toward her."
            elif character == StormX:
                "[StormX.Name] pushes you back and climbs on top of you."
            elif character == JubesX:
                "[JubesX.Name] rolls back and pulls you toward her."

        $ character.SeenPanties = 1

        if character == RogueX:
            "She slides the tip up to her anus, and presses against it."
        elif character == KittyX:
            "She slides the tip along her ass and seems to want you to insert it."
        elif character in [EmmaX, StormX]:
            "She slides the tip against her ass and seems to want you to insert it."
        elif character in [LauraX, JeanX, JubesX]:
            "She slides the tip along her asshole, and seems to want you to insert it."

        menu:
            "What do you do?"
            "Go with it.":
                $ character.Statup("Inbt", 80, 3)
                $ character.Statup("Inbt", 50, 2)

                "[character.Name] slides it in."
            "Praise her.":
                $ character.FaceChange("sexy", 1)
                $ character.Statup("Inbt", 80, 3)

                if character == RogueX:
                    ch_p "Ooo, dirty girl, [character.Pet], let's do this."
                elif character in [KittyX, EmmaX, LauraX, JeanX, StormX, JubesX]:
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

        call expression character.Tag + "_First_Bottomless(1)"
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
                    elif character in [LauraX, JubesX]:
                        "Then she lays back and slowly presses against your rigid member."
                    elif character == JeanX:
                        "Then she turns around and slowly presses against your rigid member."
                else:
                    if character in [EmmaX, StormX]:
                        "Then she pulls down your pants and climbs on top of you."
                    elif character in [LauraX, JubesX]:
                        "Then she pulls down your pants and lays back."
                    elif character == JeanX:
                        "Then she pulls down your pants and turns around."

                    "She slowly presses against your rigid member."

                "She leans back a bit and your cock pops in."

            if character != JeanX:
                $ character.Inbt += int(Taboo/10)
                $ character.Lust += int(Taboo/5)
            else:
                $ JeanX.Statup("Inbt", 90, int(Taboo/10))
                $ JeanX.Statup("Lust", 50, int(Taboo/5))
        else:
            if character not in [EmmaX, LauraX, JeanX, StormX, JubesX]:
                if not character.Anal:
                    if character == RogueX:
                        "[character.Name] bends over and presses her backside against you suggestively."
                    elif character == KittyX:
                        "[KittyX.Name] leans back and presses against you suggestively."

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
                    elif character in [LauraX, JubesX]:
                        "[LauraX.Name] lays back and slowly presses against your rigid member."
                    elif character == JeanX:
                        "[JeanX.Name] turns around and slowly presses against your rigid member."
                else:
                    if character in [EmmaX, StormX]:
                        "[character.Name] pulls down your pants and climbs on top of you."
                    elif character in [LauraX, JubesX]:
                        "[LauraX.Name] pulls down your pants and lays back."
                    elif character == JeanX:
                        "[JeanX.Name] pulls down your pants and turns around."

                    "She slowly presses against your rigid member."

                "She leans back a bit and your cock pops in."
    else:
        if (character.PantsNum() > 6 and not character.Upskirt) and (character.Panties and not character.PantiesDown):
            if character == RogueX:
                "You quickly pull down her pants and her [character.Panties] and press against her ass."
            elif character in [KittyX, EmmaX, LauraX, JeanX, StormX, JubesX]:
                "You quickly pull down her pants and her [character.Panties] and press against her back door."
        elif (character.Panties and not character.PantiesDown):
            if character == RogueX:
                "You quickly pull down her [character.Panties] and press against her ass."
            elif character in [KittyX, EmmaX, LauraX, JeanX, StormX, JubesX]:
                "You quickly pull down her [character.Panties] and press against her back door."

        $ character.Upskirt = 1
        $ character.PantiesDown = 1
        $ character.SeenPanties = 1

        call expression character.Tag + "_First_Bottomless(1)"

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

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0

    $ Line = 0
    $ Cnt = 0

    $ Player.Cock = "anal"

    $ Trigger = "anal"
    $ Speed = 1

    if Taboo:
        $ character.DrainWord("tabno")

    $ character.DrainWord("no anal")
    $ character.RecentActions.append("anal")
    $ character.DailyActions.append("anal")

label anal_after(character):
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        $ Player.Sprite = 0
        $ Player.Cock = "out"

        call expression character.Tag + "_Sex_Reset"

    $ character.FaceChange("sexy")

    $ character.Anal += 1
    $ character.Action -=1
    $ character.Addictionrate += 1

    if "addictive" in Player.Traits:
        $ character.Addictionrate += 1

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
                ch_s "I am afraid that you got more out of that than I. . ."
            elif character == JubesX:
                ch_v  "Forgetting someone? . ."

    $ temp_modifier = 0

    call Checkout

    return

label hotdog_prep(character):
    call Seen_First_Peen(character, Partner, React = Situation)

    if character in [RogueX]:
        $ character.Pose = "doggy"

    call expression character.Tag + "_Sex_Launch('hotdog')"

    if Situation == character:
        $ Situation = 0

        if character == RogueX:
            "[character.Name] turns and backs up against your cock, rubbing it against her ass."
        elif character == KittyX:
            "[character.Name] rolls back and pulls you toward her, rubbing her pussy against your cock."
        elif character in [EmmaX, StormX]:
            "[character.Name] pushes you back and climbs on top of you, sliding back and forth along your shaft."
        elif character in [LauraX, JubesX]:
            "[LauraX.Name] rolls back and pulls you toward her, grinding against your cock."
        elif character == JeanX:
            "[JeanX.Name] turns around and pulls you toward her, grinding against your cock."

        menu:
            "What do you do?"
            "Go with it.":
                $ character.Statup("Inbt", 50, 3)

                if character in [RogueX, EmmaX, StormX]:
                    "[character.Name] starts to grind against you."
                elif character == KittyX:
                    "[KittyX.Name] keeps grinding."
                elif character in [LauraX, JeanX, JubesX]:
                    "[character.Name] continues to grind."
            "Praise her.":
                $ character.FaceChange("sexy", 1)
                $ character.Statup("Inbt", 80, 2)

                if character == RogueX:
                    ch_p "Hmmm, that's good, [character.Pet]."
                elif character in [KittyX, EmmaX, LauraX, JeanX, StormX, JubesX]:
                    ch_p "Oh yeah, [character.Pet], let's do this."

                $ character.NameCheck() #checks reaction to petname

                if character in [RogueX, EmmaX, StormX]:
                    "[character.Name] starts to grind against you."
                elif character == KittyX:
                    "[KittyX.Name] keeps grinding."
                elif character in [LauraX, JeanX, JubesX]:
                    "[character.Name] continues to grind."

                $ character.Statup("Love", 85, 1)
                $ character.Statup("Obed", 60, 2)
            "Ask her to stop.":
                $ character.FaceChange("surprised")
                $ character.Statup("Inbt", 70, 1)

                ch_p "Let's not do that right now, [character.Pet]."

                $ character.NameCheck() #checks reaction to petname

                "[character.Name] pulls back."

                $ character.Statup("Obed", 80, 1)
                $ character.Statup("Obed", 30, 2)

                $ Player.RecentActions.append("nope")

                $ character.AddWord(1,"refused","refused")

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
                    elif character in [LauraX, JubesX]:
                        "Then she lays back and slowly presses against your rigid member."
                    elif character == JeanX:
                        "Then she turns around and slowly presses against your rigid member."
                else:
                    if character in [EmmaX, StormX]:
                        "Then she pulls down your pants and climbs on top of you."
                    elif character in [LauraX, JubesX]:
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
                        "[KittyX.Name] leans back and presses against you suggestively."
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
                    elif character in [LauraX, JubesX]:
                        "[character.Name] lays back and slowly presses against your rigid member."
                    elif character == JeanX:
                        "[JeanX.Name] turns around and slowly presses against your rigid member."
                else:
                    if character in [EmmaX, StormX]:
                        "[character.Name] pulls down your pants and climbs on top of you."
                    elif character in [LauraX, JubesX]:
                        "[character.Name] pulls down your pants and lays back."
                    elif character == JeanX:
                        "[JeanX.Name] pulls down your pants and turns around."

                    "She slowly presses against your rigid member."
    else:
        if character == RogueX:
            "You press yourself against her ass."
        elif character == KittyX:
            "You press yourself against her mound."
        elif character in [EmmaX, StormX]:
            "You roll back, pulling her on top of you and your rigid member."
        elif character in [LauraX, JubesX]:
            "She lays back, pulling you against her with your rigid member."
        elif character == JeanX:
            "She turns around, pulling you against her with your rigid member."

    if not character.Hotdog:                                                      #First time stat buffs
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
    $ Trigger = "hotdog"
    $ Speed = 1

    if Taboo:
        $ character.DrainWord("tabno")

    $ character.DrainWord("no hotdog")
    $ character.RecentActions.append("hotdog")
    $ character.DailyActions.append("hotdog")

label hotdog_after(character):
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        $ Player.Sprite = 0
        $ Player.Cock = "out"

        call expression character.Tag + "_Sex_Reset"

    $ character.FaceChange("sexy")

    $ character.Hotdog += 1
    $ character.Action -=1
    $ character.Addictionrate += 1

    if "addictive" in Player.Traits:
        $ character.Addictionrate += 1

    $ character.Statup("Inbt", 30, 1)
    $ character.Statup("Inbt", 70, 1)

    if character == RogueX:
        call Partner_Like(character, 1)
    elif character in [KittyX, EmmaX, LauraX]:
        call Partner_Like(character, 2)

    elif character.Hotdog >= 10:
        $ character.SEXP += 5

        if character == RogueX:
            $ Achievements.append("Rogue Full Buns")

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
