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

label first_action_reaction(character, action):
    if action == "fondle_thighs":
        $ character.SEXP += 3
    elif action in ["fondle_breasts", "suck_breasts", "fondle_ass"]:
        $ character.SEXP += 4
    elif action in ["fondle_pussy"]:
        $ character.SEXP += 7
    elif action in ["finger_pussy", "eat_pussy", "handjob", "footjob", "dildo_pussy", "hotdog"]:
        $ character.SEXP += 10
    elif action in ["finger_ass", "titjob"]:
        $ character.SEXP += 12
    elif action in ["eat_ass", "blowjob"]:
        $ character.SEXP += 15
    elif action in ["sex"]:
        $ character.SEXP += 20
    elif action in ["anal"]:
        $ character.SEXP += 25

    if not Situation:
        if character.Love >= 500 and "unsatisfied" not in character.RecentActions:
            $ character.Mouth = "smile"
            call that_was_nice_lines(character)
        elif action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass", "dildo_pussy", "dildo_ass"] and character.Obed <= 500 and Player.Focus <= 20:
            $ character.FaceChange("perplexed", 1)

            call was_that_enough_lines(character)
        elif action in ["handjob", "footjob", "titjob", "blowjob", "sex", "anal", "hotdog"] and  Player.Focus <= 20:
            $ character.Mouth = "sad"

            call was_that_enough_lines(character)

    return

label first_action_stats(character, action):
    if action == "fondle_thighs" and not character.FondleT:
        if character.Forced:
            $ character.Statup("Love", 90, -10)
            $ character.Statup("Obed", 70, 15)
            $ character.Statup("Inbt", 80, 10)
        else:
            $ character.Statup("Love", 90, 5)
            $ character.Statup("Obed", 70, 10)
            $ character.Statup("Inbt", 80, 15)
    elif action == "fondle_breasts" and not character.FondleB:
        if character.Forced:
            $ character.Statup("Love", 90, -20)
            $ character.Statup("Obed", 70, 25)
            $ character.Statup("Inbt", 80, 15)
        else:
            $ character.Statup("Love", 90, 10)
            $ character.Statup("Obed", 70, 5)
            $ character.Statup("Inbt", 80, 15)
    elif action == "suck_breasts" and not character.SuckB:
        if character.Forced:
            $ character.Statup("Love", 90, -25)
            $ character.Statup("Obed", 70, 25)
            $ character.Statup("Inbt", 80, 17)
        else:
            $ character.Statup("Love", 90, 10)
            $ character.Statup("Obed", 70, 10)
            $ character.Statup("Inbt", 80, 15)
    elif action == "fondle_pussy" and not character.FondleP:
        if character.Forced:
            $ character.Statup("Love", 90, -50)
            $ character.Statup("Obed", 70, 35)
            $ character.Statup("Inbt", 80, 25)
        else:
            $ character.Statup("Love", 90, 10)
            $ character.Statup("Obed", 70, 10)
            $ character.Statup("Inbt", 80, 15)
    elif action == "finger_pussy" and not character.InsertP:
        if character.Forced:
            $ character.Statup("Love", 90, -60)
            $ character.Statup("Obed", 70, 55)
            $ character.Statup("Inbt", 80, 35)
        else:
            $ character.Statup("Love", 90, 10)
            $ character.Statup("Obed", 70, 20)
            $ character.Statup("Inbt", 80, 25)
    if action == "eat_pussy" and not character.LickP:
        if character.Forced:
            $ character.Statup("Love", 90, -30)
            $ character.Statup("Obed", 70, 35)
            $ character.Statup("Inbt", 80, 75)
        else:
            $ character.Statup("Love", 90, 35)
            $ character.Statup("Obed", 70, 15)
            $ character.Statup("Inbt", 80, 35)
    elif action == "fondle_ass" and not character.FondleA:
        if character.Forced:
            $ character.Statup("Love", 90, -20)
            $ character.Statup("Obed", 70, 20)
            $ character.Statup("Inbt", 80, 15)
        else:
            $ character.Statup("Love", 90, 10)
            $ character.Statup("Obed", 70, 12)
            $ character.Statup("Inbt", 80, 20)
    elif action == "finger_ass" and not character.InsertA:
        if character.Forced:
            $ character.Statup("Love", 90, -50)
            $ character.Statup("Obed", 70, 60)
            $ character.Statup("Inbt", 80, 35)
        else:
            $ character.Statup("Love", 90, 10)
            $ character.Statup("Obed", 70, 20)
            $ character.Statup("Inbt", 80, 25)
    elif action == "eat_ass" and not character.LickA:
        if character.Forced:
            $ character.Statup("Love", 90, -30)
            $ character.Statup("Obed", 70, 40)
            $ character.Statup("Inbt", 80, 80)
        else:
            $ character.Statup("Love", 90, 35)
            $ character.Statup("Obed", 70, 25)
            $ character.Statup("Inbt", 80, 55)
    elif action == "handjob" and not character.Hand:
        if character.Forced:
            $ character.Statup("Love", 90, -20)
            $ character.Statup("Obed", 70, 25)
            $ character.Statup("Inbt", 80, 30)
        else:
            $ character.Statup("Love", 90, 5)
            $ character.Statup("Obed", 70, 20)
            $ character.Statup("Inbt", 80, 20)
    elif action == "footjob" and not character.Foot:
        if character.Forced:
            $ character.Statup("Love", 90, -20)
            $ character.Statup("Obed", 70, 25)
            $ character.Statup("Inbt", 80, 30)
        else:
            $ character.Statup("Love", 90, 5)
            $ character.Statup("Obed", 70, 20)
            $ character.Statup("Inbt", 80, 20)
    elif action == "titjob" and not character.Tit:
        if character.Forced:
            $ character.Statup("Love", 90, -25)
            $ character.Statup("Obed", 70, 30)
            $ character.Statup("Inbt", 80, 35)
        else:
            $ character.Statup("Love", 90, 5)
            $ character.Statup("Obed", 70, 25)
            $ character.Statup("Inbt", 80, 30)
    elif action == "blowjob" and not character.Blow:
        if character.Forced:
            $ character.Statup("Love", 90, -70)
            $ character.Statup("Obed", 70, 45)
            $ character.Statup("Inbt", 80, 60)
        else:
            $ character.Statup("Love", 90, 5)
            $ character.Statup("Obed", 70, 35)
            $ character.Statup("Inbt", 80, 40)
    elif action == "dildo_pussy" and not character.DildoP:
        if character.Forced:
            $ character.Statup("Love", 90, -75)
            $ character.Statup("Obed", 70, 60)
            $ character.Statup("Inbt", 80, 35)
        else:
            $ character.Statup("Love", 90, 10)
            $ character.Statup("Obed", 70, 20)
            $ character.Statup("Inbt", 80, 45)
    elif action == "dildo_ass" and not character.DildoA:
        if character.Forced:
            $ character.Statup("Love", 90, -75)
            $ character.Statup("Obed", 70, 60)
            $ character.Statup("Inbt", 80, 35)
        else:
            $ character.Statup("Love", 90, 10)
            $ character.Statup("Obed", 70, 20)
            $ character.Statup("Inbt", 80, 45)
    elif action == "sex" and not character.Sex:
        if character.Forced:
            $ character.Statup("Love", 90, -150)
            $ character.Statup("Obed", 70, 60)
            $ character.Statup("Inbt", 80, 50)
        else:
            $ character.Statup("Love", 90, 30)
            $ character.Statup("Obed", 70, 30)
            $ character.Statup("Inbt", 80, 60)
    elif action == "anal" and not character.Anal:
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

    return

label action_specific_consequences(character, action):
    $ achievement = None

    if action == "fondle_thighs":
        $ character.FondleT += 1

        $ counter = character.FondleT

        call Partner_Like(character, 1, 0)
    elif action == "fondle_breasts":
        $ character.FondleB += 1

        $ counter = character.FondleB

        call Partner_Like(character, 2)
    elif action == "suck_breasts":
        $ character.SuckB += 1

        $ counter = character.SuckB

        call Partner_Like(character, 2)
    elif action == "fondle_pussy":
        $ character.FondleP += 1

        $ counter = character.FondleP

        call Partner_Like(character, 2)
    elif action == "finger_pussy":
        $ character.InsertP += 1

        $ counter = character.InsertP

        call Partner_Like(character, 2)
    elif action == "eat_pussy":
        $ character.LickP += 1

        $ counter = character.LickP

        if character == RogueX and Partner == EmmaX:
            call Partner_Like(character,4,3)
        elif character not in [KittyX, StormX] and Partner == RogueX:
            call Partner_Like(character, 3, 3)
        elif character == RogueX:
            call Partner_Like(character,3,2)
        else:
            call Partner_Like(character, 2)
    elif action == "fondle_ass":
        $ character.FondleA += 1

        $ counter = character.FondleA

        call Partner_Like(character, 2)
    elif action == "finger_ass":
        $ character.InsertA += 1

        $ counter = character.InsertA

        call Partner_Like(character, 2)
    elif action == "eat_ass":
        $ character.LickA += 1

        $ counter = character.LickA

        call Partner_Like(character, 2)
    elif action == "handjob":
        $ character.Hand += 1

        $ achievement = character.Tag + " Handi-Queen"
        $ counter = character.Hand

        call Partner_Like(character, 2)
    elif action == "footjob":
        $ character.Foot += 1

        $ achievement = character.Tag + "pedi"
        $ counter = character.Foot

        call Partner_Like(character, 1)
    elif action == "titjob":
        $ character.Tit += 1

        $ counter = character.Tit

        call Partner_Like(character, 3)
    elif action == "blowjob":
        $ character.Blow += 1

        $ achievement = character.Tag + " Jobber"
        $ counter = character.Blow

        if character == RogueX and Partner == EmmaX:
            call Partner_Like(character, 3)
        else:
            call Partner_Like(character, 2)
    elif action == "dildo_pussy":
        $ character.DildoP += 1

        $ counter = character.DildoP

        call Partner_Like(character, 2)
    elif action == "dildo_ass":
        $ character.DildoA += 1

        $ counter = character.DildoA

        call Partner_Like(character, 2)
    elif action == "sex":
        $ character.Sex += 1

        $ achievement = character.Tag + " Sex Addict"
        $ counter = character.Sex

        call Partner_Like(character, 3, 2)

        $ character.Statup("Inbt", 30, 2)
        $ character.Statup("Inbt", 70, 1)
    elif action == "anal":
        $ character.Anal += 1

        $ achievement = character.Tag + " Anal Addict"
        $ counter = character.Anal

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

        $ character.Statup("Inbt", 30, 3)
        $ character.Statup("Inbt", 70, 1)
    elif action == "hotdog":
        $ character.Hotdog += 1

        $ achievement = character.Tag + " Full Buns"
        $ counter = character.Hotdog

        if character == RogueX:
            call Partner_Like(character, 1)
        elif character in [KittyX, EmmaX, LauraX]:
            call Partner_Like(character, 2)

        $ character.Statup("Inbt", 30, 1)
        $ character.Statup("Inbt", 70, 1)

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

        call recent_action_lines(character)

        if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
            call before_handjob
        elif action in ["sex", "anal", "hotdog"]:
            call before_action

        return
    elif action in character.DailyActions:
        $ character.FaceChange("sexy", 1)

        call daily_action_lines(character)

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

        call used_to_action_lines(character)

    $ Line = 0

    return

label action_disapproved(character, action, action_counter):
    if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
        $ character.FaceChange("angry", 1)
    elif action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "sex"]:
        $ character.FaceChange("angry")

    if "no_" + action in character.RecentActions:
        call just_told_you_no_lines(character)
    elif Taboo and "tabno" in character.DailyActions and "no_" + action in character.DailyActions:
        call had_enough_of_this_lines(character)
    elif "no_" + action in character.DailyActions:
        call already_said_no_lines(character)
    elif Taboo and "tabno" in character.DailyActions:
        call already_said_not_here_lines(character)
    elif not action_counter:
        $ character.FaceChange("bemused")

        if action not in ["finger_ass", "eat_ass"]:
            call not_ready_yet_lines(character)
        else:
            call not_into_ass_play(character)
    elif action in ["dildo_ass", "anal"] and not character.Loose and action not in character.DailyActions:
        $ character.FaceChange("perplexed")

        ch_r "You could have been a bit more gentle last time, [character.Petname]. . ."
    else:
        $ character.FaceChange("bemused")

        call rather_not_lines(character)

    call begging_menu(character, action)

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
            call before_action

    return

label action_rejected(character, action, action_counter):
    if "no_" + action in character.DailyActions:
        $ character.FaceChange("angry", 1)

        call learn_to_take_no_lines(character)

        $ character.AddWord(1,"angry","angry")
    elif character.Forced:
        call went_too_far_lines(character)

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

        if action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
            $ character.Statup("Lust", 200, 5)
            $ character.Statup("Obed", 50, -3)
    elif action in ["dildo_ass", "anal"] and not character.Loose and action in character.DailyActions:
        $ character.FaceChange("bemused")

        ch_r "Sorry, I just need a little break back there, [character.Petname]."
    elif action_counter:
        $ character.FaceChange("sad")

        call you_had_your_shot_lines(character)
    else:
        if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "fondle_ass", "handjob", "blowjob", "sex"]:
            $ character.FaceChange("sexy")
            $ character.Mouth = "sad"
        elif action in ["eat_pussy", "finger_ass", "eat_ass", "footjob", "titjob", "dildo_pussy", "dildo_ass", "anal", "hotdog"]:
            $ character.FaceChange("surprised")

        call not_happening_lines(character)

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
            jump before_fondle
        elif action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass"]:
            jump before_handjob
        elif action in ["sex", "anal", "hotdog"]:
            jump before_action
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

label before_action:
    if Player.primary_action not in ["sex", "anal", "hotdog"]:
        if Player.primary_action in ["fondle_thighs", "fondle_breasts", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
            if Trigger == "kiss_you":
                $ Trigger = Player.primary_action

                return

        if Trigger2 == Player.primary_action:
            return

        if Player.primary_action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass"]:
            if Taboo:
                $ Player.focused_girl.Inbt += int(Taboo/10)
                $ Player.focused_girl.Lust += int(Taboo/5)

            $ Player.focused_girl.FaceChange("sexy")

    # we have to fix the launch functions to accept Player.primary_action
    if Player.primary_action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
        if Player.primary_action in ["fondle_thighs", "fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
            if Player.focused_girl != EmmaX:
                call pussy_launch(Player.focused_girl, trigger = Player.primary_action)
            else:
                if Player.focused_girl.Pose in ["doggy", "sex"]:
                    call ViewShift(Player.focused_girl, Player.focused_girl.Pose, 0, Player.primary_action)
                else:
                    call ViewShift(Player.focused_girl, "pussy", 0, Player.primary_action)
        elif Player.primary_action in ["fondle_breasts", "suck_breasts"]:
            call breasts_launch(Player.focused_girl, trigger = Player.primary_action)

        if not Player.focused_girl.Forced and Situation != "auto":
            $ temp_modifier = 0

            if Player.primary_action in ["eat_pussy", "eat_ass"] and Player.focused_girl.PantsNum() >= 6:
                $ temp_modifier = 15

            if Player.primary_action in ["fondle_thighs", "fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
                call Bottoms_Off
            elif Player.primary_action in ["fondle_breasts", "suck_breasts"]:
                call Top_Off
            elif Player.primary_action == "finger_pussy":
                call Girl_Undress(Player.focused_girl, "bottom")

            if "angry" in Player.focused_girl.RecentActions:
                return

        $ temp_modifier = 0
    elif Player.primary_action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass"]:
        if Player.primary_action in ["handjob", "footjob", "titjob", "blowjob"]:
            if Player.focused_girl.Forced:
                $ Player.focused_girl.FaceChange("sad")
            elif not Player.focused_girl.Hand:
                $ Player.focused_girl.Brows = "confused"
                $ Player.focused_girl.Eyes = "sexy"
                $ Player.focused_girl.Mouth = "smile"
        elif Player.primary_action in ["dildo_pussy", "dildo_ass"]:
            if not Player.focused_girl.Forced and Situation != "auto":
                if Player.primary_action == "dildo_pussy":
                    $ temp_modifier = 15 if Player.focused_girl.PantsNum() > 6 else 0
                elif Player.primary_action == "dildo_ass":
                    $ temp_modifier = 20 if Player.focused_girl.PantsNum() > 6 else 0

                call Bottoms_Off(Player.focused_girl)

                if "angry" in Player.focused_girl.RecentActions:
                    return

            $ temp_modifier = 0

        call Seen_First_Peen(Player.focused_girl, Partner, React = Situation)

        if Player.primary_action == "handjob":
            call handjob_launch(Player.focused_girl, "L")
        elif Player.primary_action == "footjob":
            call sex_launch(Player.focused_girl, "foot")
        elif Player.primary_action == "titjob":
            call titjob_launch(Player.focused_girl, "L")
        elif Player.primary_action == "blowjob":
            call blowjob_launch(Player.focused_girl, "L")
        elif Player.primary_action in ["dildo_pussy", "dildo_ass"]:
            call pussy_launch
    elif Player.priamry_action in ["sex", "anal", "hotdog"]:
        call Seen_First_Peen(Player.focused_girl, Partner, React = Situation)

        $ Player.focused_girl.Pose = "doggy"

        call sex_launch(Player.focused_girl, "hotdog")

    if Player.primary_action not in ["sex", "anal", "hotdog"]:
        if Situation == Player.focused_girl:
            $ Situation = 0

            call character_initated_action(Player.focused_girl, Player.primary_action)

            if _return:
                return
    elif Player.primary_action in ["sex", "anal", "hotdog"]:
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

    call first_action_stats(Player.focused_girl, Player.primary_action)

    if Taboo:
        if Player.primary_action == "fondle_thighs":
            $ Player.focused_girl.Statup("Lust", 200, (int(Taboo/5)))
            $ Player.focused_girl.Statup("Inbt", 200, (2*(int(Taboo/5))))
        elif Player.primary_action in ["fondle_breasts", "suck_breasts", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass"]:
            $ Player.focused_girl.Inbt += int(Taboo/10)
            $ Player.focused_girl.Lust += int(Taboo/5)
        elif Player.primary_action in ["fondle_pussy", "eat_pussy", "finger_ass", "eat_ass"]:
            if Player.focused_girl == JeanX and Player.focused_girl.Taboo:
                $ Player.focused_girl.Statup("Inbt", 200, (int(Taboo/10)))
            elif Taboo:
                $ Player.focused_girl.Inbt += int(Taboo/10)

            $ Player.focused_girl.Lust += int(Taboo/5)

    if Situation:
        $ renpy.pop_call()

        $ Situation = 0

    if Player.primary_action in ["eat_pussy", "eat_ass"]:
        if Player.focused_girl.PantsNum() == 5:
            $ Player.focused_girl.Upskirt = 1
            $ Player.focused_girl.SeenPanties = 1

        if not Player.focused_girl.Panties:
            call first_bottomless(Player.focused_girl, 1)

    $ Line = 0
    $ Cnt = 0

    if Player.primary_action == "finger_pussy":
        $ Speed = 2
    elif Player.primary_action == "sex":
        $ Player.Cock = "in"

        $ Trigger = Player.primary_action
        $ Speed = 1
    elif Player.primary_action == "anal":
        $ Player.Cock = "anal"

        $ Trigger = Player.primary_action
        $ Speed = 1

    if Taboo:
        $ Player.focused_girl.DrainWord("tabno")

    # we have to fix DrainWord and AddWord to accept Player.primary_action
    $ Player.focused_girl.DrainWord("no_" + Player.primary_action)
    $ Player.focused_girl.AddWord(0, Player.primary_action, Player.primary_action)

    # we have to fix the launch functions to accept Player.primary_action
    if Player.primary_action in ["fondle_thighs", "fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
        if Player.focused_girl != EmmaX:
            call pussy_launch(Player.focused_girl, trigger = Player.primary_action)
        else:
            if Player.focused_girl.Pose in ["doggy", "sex"]:
                call ViewShift(Player.focused_girl, Player.focused_girl.Pose, 0, Player.primary_action)
            else:
                call ViewShift(Player.focused_girl, "pussy", 0, Player.primary_action)
    elif Player.primary_action in ["fondle_breasts", "suck_breasts"]:
        call breasts_launch(Player.focused_girl, trigger = Player.primary_action)

label action_cycle:
    if Player.primary_action in ["suck_breasts", "eat_pussy", "eat_ass"]:
        if Trigger2 == "kiss_you":
            $ Trigger2 = 0

    while Round > 0:
        call Shift_Focus(Player.focused_girl)

        if Player.primary_action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]
            # we have to fix ViewShift to accept Player.primary_action
            call ViewShift(Player.focused_girl, Player.focused_girl.Pose, 0, Player.primary_action)
        elif Player.primary_action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass"]:
            call handjob_launch(Player.focused_girl)
        elif Player.primary_action in ["sex", "anal", "hotdog"]:
            call sex_launch(Player.focused_girl, Player.primary_action)

        $ Player.focused_girl.LustFace()

        if Player.Focus < 100:
            if Player.primary_action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]
                jump fondle_menu

                label fondle_menu_return:
            elif Player.primary_action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass"]:
                jump handjob_menu

                label handjob_menu_return:
            elif Player.primary_action in ["sex", "anal", "hotdog"]:
                jump sex_menu

                label sex_menu_return:

        if Player.primary_action in ["eat_pussy", "fondle_ass", "finger_ass", "eat_ass", "dildo_pussy", "dildo_ass"]:
            if Player.focused_girl.Panties or Player.focused_girl.PantsNum() >= 6 or Player.focused_girl.HoseNum() >= 5: #This checks if Rogue wants to strip down.
                call Girl_Undress(Player.focused_girl, "auto")

        call Shift_Focus(Player.focused_girl)
        call Sex_Dialog(Player.focused_girl, Partner)

        $ Cnt += 1
        $ Round -= 1

        if (Player.primary_action in ["blowjob"] and Speed) or Player.primary_action in ["sex", "anal"[]]:
            $ Player.Wet = 1
            $ Player.Spunk = 0 if (Player.Spunk and "in" not in Player.focused_girl.Spunk) else Player.Spunk #cleans you off after one cycle

        if Player.primary_action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]
            call end_of_fondle_round(Player.focused_girl, Player.primary_action)
        elif Player.primary_action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass"]:
            end_of_handjob_round(Player.focused_girl, Player.primary_action)
        elif Player.primary_action in ["sex", "anal", "hotdog"]:
            call end_of_sex_round(Player.focused_girl, Player.primary_action)

        if _return:
            return

        if Player.primary_action in ["fondle_breasts", "suck_breasts"]:
            if Player.focused_girl.Lust >= 50 and not Player.focused_girl.Uptop and (Player.focused_girl.Chest or Player.focused_girl.Over):
                $ Player.focused_girl.Uptop = 1

                if Player.focused_girl == RogueX:
                    "[Player.focused_girl.Name] shrugs and pulls her top open."
                elif Player.focused_girl == KittyX:
                    "[KittyX.Name] laughs and pulls her top open."
                elif Player.focused_girl in [EmmaX, StormX]:
                    "[EmmaX.Name] sighs and tugs her breasts free of her clothes."
                elif Player.focused_girl in [LauraX, JeanX, JubesX]:
                    "[Player.focused_girl.Name] grunts and pulls her clothes aside."

                call first_topless

    $ Player.focused_girl.FaceChange("bemused", 0)

    $ Line = 0

    call im_done_lines(Player.focused_girl)

label after_action:
    if Player.primary_action in ["fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"] and not Situation:
        if Player.primary_action in ["sex", "anal", "hotdog"]:
            $ Player.Sprite = 0
            $ Player.Cock = "out"

        call reset_position(character)

    $ Player.focused_girl.FaceChange("sexy")
    $ Player.focused_girl.Action -= 1

    call action_specific_consequences(Player.focused_girl, Player.primary_action)

    if Player.primary_action not in ["dildo_pussy", "dildo_ass"]:
        $ Player.focused_girl.Addictionrate += 1

        if "addictive" in Player.Traits:
            $ Player.focused_girl.Addictionrate += 1

    if Player.primary_action in ["handjob", "footjob"]:
        $ Player.focused_girl.Statup("Lust", 90, 5)

    if achievement is not None and achievement in Achievements:
        pass
    elif Player.primary_action not in ["dildo_pussy", "dildo_ass"] and counter >= 10:
        if Player.primary_action not in ["anal"]:
            $ Player.focused_girl.SEXP += 5
        else:
            $ Player.focused_girl.SEXP += 7

        if achievement is not None:
            $ Achievements.append(achievement)

        if Player.primary_action not in ["anal"] and not Situation:
            $ Player.focused_girl.FaceChange("smile", 1)

            ch_r "I guess you can call me \"Handi-Queen.\""
            ch_r "I guess I've gotten used to this foot thing."
            ch_r "I'm really starting to enjoy this."

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

            ch_r "I think I'm getting addicted to this."
        elif Player.primary_action in ["anal"] and not Situation:
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
    elif counter == 1:
        call first_action_reaction(Player.focused_girl, Player.primary_action)
    elif Player.primary_action in ["handjob", "footjob", "titjob", "blowjob", "sex", "anal", "hotdog"] and counter == 5:
        ch_r "I think I've got this well in hand."
        ch_r "I kinda like this sensation.{p}}Never thought about touching people with my feet."
        ch_r "I think I've got the hang of this."

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

        if Player.focused_girl == RogueX:
            ch_r "This is. . . interesting."
        elif Player.focused_girl == KittyX:
            ch_k "I'm surprised how much I enjoy this."
    elif Player.primary_action in ["sex", "anal", "hotdog"] and Situation not in ["auto", "pullback"]:
        if "unsatisfied" in Player.focused_girl.RecentActions:
            $ Player.focused_girl.FaceChange("angry")

            if Player.focused_girl != JeanX:
                $ Player.focused_girl.Eyes = "side"

            call didnt_get_off_lines(Player.focused_girl)

    $ temp_modifier = 0

    call Checkout

    if Situation:
        call Sex_Basic_Dialog(Player.focused_girl, "switch")
        ch_r "Mmm, so what else did you have in mind?"
    else:
        if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
            call reset_position(character)
        elif Player.primary_action == "handjob":
            call handjob_reset(Player.focused_girl)
        elif Player.primary_action == "footjob":
            call doggy_reset(Player.focused_girl)
        elif Player.primary_action == "titjob":
            call titjob_reset(Player.focused_girl)
        elif Player.primary_action == "blowjob":
            call blowjob_reset(Player.focused_girl)

    return
