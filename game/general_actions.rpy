label Girl_initiated_action(Girl, action):
    if action in ["fondle_breasts", "suck_breasts"]:
        if action == "fondle_breasts":
            $ covered_phrase = "arm and shoves your hand against her covered breast"
            $ topless_phrase = "arm and shoves your hand against her breast"
        elif action == "suck_breasts":
            $ covered_phrase = "head and shoves your face into her chest"
            $ topless_phrase = covered_phrase

        if (Girl.Over or Girl.Chest) and not Girl.Uptop:
            if ApprovalCheck(Girl, 1250, TabM = 1) or (Girl.SeenChest and ApprovalCheck(Girl, 500) and not Taboo):
                $ Girl.Uptop = 1

                $ line = Girl.Over if Girl.Over else Girl.Chest

                "With a mischievous grin, [Girl.name] pulls her [line] up over her breasts."

                call first_topless(Girl, silent = True)

                $ line = 0

                "She then grabs your [topless_phrase], clearly intending you to get to work."
            else:
                "[Girl.name] grabs your [covered_phrase], clearly intending you to get to work."
        else:
            "[Girl.name] grabs your [topless_phrase], clearly intending you to get to work."
    elif action in ["fondle_pussy", "eat_pussy", "finger_ass"]:
        if action == "fondle_pussy":
            if Girl in [Jeanx, JubesX]:
                $ phrase = "grabs your arm and presses your hand into her crotch"
            elif Girl == StormX:
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


        if (Girl.Legs and not Girl.Upskirt) or (Girl.Panties and not Girl.PantiesDown):
            if ApprovalCheck(Girl, 1250, TabM = 1) or (Girl.SeenPussy and ApprovalCheck(Girl, 500) and not Taboo):
                $ Girl.Upskirt = 1
                $ Girl.PantiesDown = 1

                $ line = 0

                if Girl.wearing_skirt:
                    $ line = Girl.name + " hikes up her skirt"
                elif Girl.PantsNum() > 6:
                    $ line = Girl.name + " pulls down her " + Girl.Legs
                else:
                    $ line = 0

                if Girl.Panties:
                    if line:
                        "[line] and pulls her [Girl.Panties] out of the way."
                        "She then [phrase], clearly intending you to get to work."
                    else:
                        "She pulls her [Girl.Panties] out of the way, and then [phrase]."
                        "She clearly intends for you to get to work."
                else:
                    "[line], and then [phrase]."
                    "She clearly intends for you to get to work."

                call first_bottomless(Girl, 1)
            else:
                "[Girl.name] [phrase], clearly intending you to get to work."
        else:
            "[Girl.name] [phrase], clearly intending you to get to work."
    elif action in ["handjob", "footjob", "titjob", "blowjob"]:
        if action == "handjob":
            if offhand_action == "jackin":
                "[Girl.name] brushes your hand aside and starts stroking your cock."
            else:
                "[Girl.name] gives you a mischevious smile, and starts to fondle your cock."
        elif action == "footjob":
            "[Girl.name] leans forward and starts rubbing your cock between her feet."
        elif action == "titjob":
            "[Girl.name] slides down and sandwiches your dick between her tits."
        elif action == "blowjob":
            "[Girl.name] slides down and gives your cock a little lick."
    elif action in ["dildo_pussy", "dildo_ass"]:
        if Girl.wearing_skirt:
            "[Girl.name] grabs her dildo, hiking up her skirt as she does."

            $ Girl.Upskirt = 1
        elif Girl.PantsNum() > 6:
            "[Girl.name] grabs her dildo, pulling down her pants as she does."

            $ Girl.Legs = 0
        else:
            if action == "dildo_pussy":
                "[Girl.name] grabs her dildo, rubbing it suggestively against her crotch."
            elif action == "dildo_ass":
                "[Girl.name] grabs her dildo, rubbing is suggestively against her ass."

        $ Girl.SeenPanties = 1

        if action == "dildo_pussy":
            "She slides the tip along her pussy and seems to want you to insert it."
        elif action == "dildo_ass":
            "She slides the tip against her asshole, and seems to want you to insert it."
    elif action in ["sex", "anal", "hotdog"]:
        if action in ["sex", "anal"]:
            if Girl.wearing_skirt:
                $ line = renpy.random.choice(["[Girl.name] turns and backs up against your cock, sliding her skirt up as she does so.",
                    "[Girl.name] rolls back and pulls you toward her, sliding her skirt up as she does so.",
                    "[Girl.name] turns around, sliding her skirt up as she does so.",
                    "[Girl.name] pushes you back and climbs on top of you, sliding her skirt up as she does so.",
                    "[Girl.name] lays back, sliding her skirt up as she does so."])
                "[line]"

                $ Girl.Upskirt = 1
            elif Girl.PantsNum() > 6:
                $ line = renpy.random.choice(["[Girl.name] turns and backs up against your cock, sliding her [Girl.Legs] down as she does so.",
                    "[Girl.name] rolls back and pulls you against her, sliding her [Girl.Legs] off as she does so.",
                    "[Girl.name] pushes you down and climbs on top of you, sliding her [Girl.Legs] down as she does so.",
                    "[Girl.name] turns around, sliding her [Girl.Legs] down as she does so.",
                    "[Girl.name] lays back, sliding her [Girl.Legs] down as she does so."])
                "[line]"

                $ Girl.Upskirt = 1
            elif Girl.PantsNum() == 6:
                $ line = renpy.random.choice(["[Girl.name] rolls onto her back and pulls you against her, sliding her shorts off as she does so."])
                "[line]"

                $ Girl.Upskirt = 1
            else:
                $ line = renpy.random.choice(["[Girl.name] turns and backs up against your cock.",
                    "[Girl.name] rolls back and pulls you toward her.",
                    "[Girl.name] pushes you back and climbs on top of you.",
                    "[Girl.name] turns around and pulls you toward her."])
                "[line]"

            $ Girl.SeenPanties = 1

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
            $ line = renpy.random.choice(["[Girl.name] turns and backs up against your cock, rubbing it against her ass.",
                "[Girl.name] rolls back and pulls you toward her, rubbing her pussy against your cock.",
                "[Girl.name] pushes you back and climbs on top of you, sliding back and forth along your shaft.",
                "[Girl.name] rolls back and pulls you toward her, grinding against your cock.",
                "[Girl.name] turns around and pulls you toward her, grinding against your cock."])
            "[line]"

    if action in ["fondle_breasts", "suck_breasts", "fondle_pussy", "eat_pussy", "finger_ass", "handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
        if action == "fondle_breasts":
            $ action_line = "You start to fondle them."
            $ praise_line = "I like the initiative, " + Girl.Pet
            $ no_action_line = "You pull your hand back."
            $ reject_line = "Let's not do that right now, " + Girl.Pet
            $ rejection_response_line = Girl.name + " pulls back."
        elif action == "suck_breasts":
            $ action_line = "You start to run your tongue along her nipple."
            $ praise_line = "Mmm, I like this, " + Girl.Pet
            $ no_action_line = "You pull your head back."
            $ reject_line = "Let's not do that right now, " + Girl.Pet
            $ rejection_response_line = Girl.name + " pulls away."
        elif action == "fondle_pussy":
            $ action_line = "You start to run your fingers along her pussy."
            $ praise_line = "I like the initiative, " + Girl.Pet
            $ no_action_line = "You pull your hand back."
            $ reject_line = "Let's not do that right now, " + Girl.Pet
            $ rejection_response_line = Girl.name + " pulls back."
        elif action == "eat_pussy":
            $ action_line = "You start licking her slit."
            $ praise_line = "Mmm, I like this idea, " + Girl.Pet
            $ no_action_line = "You pull your head away."
            $ reject_line = "Let's not do that right now, " + Girl.Pet
            $ rejection_response_line = Girl.name + " pulls back."
        elif action == "finger_ass":
            $ action_line = "You press your finger into her tight ass."
            $ praise_line = "Dirty girl, " + Girl.Pet
            $ no_action_line = "You pull your hand back."
            $ reject_line = "Let's not do that right now, " + Girl.Pet
            $ rejection_response_line = Girl.name + " pulls back."
        elif action == "handjob":
            $ action_line = "[Girl.name] continues her actions."
            $ praise_line = "Oooh, that's good, [Girl.Pet]."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [Girl.Pet]."
            $ rejection_response_line = "[Girl.name] puts it down."
        elif action == "footjob":
            $ action_line = "[Girl.name] continues her actions."
            $ praise_line = "Oooh, that's good, [Girl.Pet]."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [Girl.Pet]."
            $ rejection_response_line = "[Girl.name] puts it down."
        elif action == "titjob":
            $ action_line = "[Girl.name] starts to slide them up and down."
            $ praise_line = "Oh, that sounds like a good idea, [Girl.Pet]."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [Girl.Pet]."
            $ rejection_response_line = "[Girl.name] lets it drop out from between her breasts."
        elif action == "blowjob":
            $ action_line = "[Girl.name] continues licking at it."
            $ praise_line = "Hmmm, keep doing that, [Girl.Pet]."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [Girl.Pet]."
            $ rejection_response_line = "[Girl.name] puts it down."
        elif action == "dildo_pussy":
            $ action_line = "[Girl.name] slides it in."
            $ praise_line = "Oh yeah, [Girl.Pet], let's do this."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [Girl.Pet]."
            $ rejection_response_line = "[Girl.name] sets the dildo down."
        elif action == "dildo_ass":
            $ action_line = "[Girl.name] slides it in."
            $ praise_line = "Hmmm, keep doing that, [Girl.Pet]."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [Girl.Pet]."
            $ rejection_response_line = "[Girl.name] sets the dildo down."
        elif action == "sex":
            $ action_line = "[Girl.name] slides it in."
            $ praise_line = "Oh yeah, [Girl.Pet], let's do this."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [Girl.Pet]."
            $ rejection_response_line = "[Girl.name] pulls back."
        elif action == "anal":
            $ action_line = "[Girl.name] slides it in."
            $ praise_line = "Ooo, dirty girl, [Girl.Pet], let's do this."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [Girl.Pet]."
            $ rejection_response_line = "[Girl.name] pulls back."
        elif action == "hotdog":
            $ action_line = renpy.random.choice([Girl.name + " starts to grind against you",
                Girl.name + " keeps grinding",
                Girl.name + " continues to grind"])
            $ praise_line = "Hmmm, that's good, [Girl.Pet]."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [Girl.Pet]."
            $ rejection_response_line = "[Girl.name] pulls back."

        menu:
            "What do you do?"
            "Get to work." if action in ["fondle_breasts", "suck_breasts", "fondle_pussy", "eat_pussy", "finger_ass"]:
                $ Girl.change_stat("inhibition", 80, 3)
                $ Girl.change_stat("inhibition", 50, 2)

                "[action_line]"
            "Nothing." if action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass"]:
                $ Girl.change_stat("inhibition", 70, 3)
                $ Girl.change_stat("inhibition", 30, 2)

                "[action_line]"
            "Go with it." if action in ["sex", "anal", "hotdog"]:
                if action in ["sex", "anal"]:
                    $ Girl.change_stat("inhibition", 80, 3)
                    $ Girl.change_stat("inhibition", 50, 2)
                elif action in ["hotdog"]:
                    $ Girl.change_stat("inhibition", 50, 3)

                "[action_line]"
            "Go for it." if action in ["dildo_pussy", "dildo_ass"]:
                $ Girl.change_face("sexy", 1)
                $ Girl.change_stat("inhibition", 80, 3)

                ch_p "[praise_line]"

                $ Girl.nameCheck() #checks reaction to petname

                "You grab the dildo and slide it in."

                $ Girl.change_stat("love", 85, 1)
                $ Girl.change_stat("obedience", 90, 1)
                $ Girl.change_stat("obedience", 50, 2)
            "Praise her." if action not in ["dildo_pussy", "dildo_ass"]:
                $ Girl.change_face("sexy", 1)

                if action in ["fondle_breasts", "suck_breasts", "fondle_pussy", "eat_pussy", "finger_ass", "dildo_pussy", "dildo_ass", "sex", "anal"]:
                    $ Girl.change_stat("inhibition", 80, 3)
                elif action in ["handjob", "footjob", "titjob", "blowjob"]:
                    $ Girl.change_stat("inhibition", 70, 3)
                elif action in ["hotdog"]:
                    $ Girl.change_stat("inhibition", 80, 2)

                ch_p "[praise_line]"

                $ Girl.nameCheck() #checks reaction to petname

                "[action_line]"

                if action in ["fondle_breasts", "suck_breasts", "fondle_pussy", "eat_pussy", "finger_ass", "dildo_pussy", "dildo_ass", "sex", "anal"]:
                    $ Girl.change_stat("love", 85, 1)
                elif action in ["handjob", "footjob", "titjob", "blowjob", "hotdog"]:
                    $ Girl.change_stat("love", 80, 1)

                $ Girl.change_stat("obedience", 90, 1)
                $ Girl.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                if no_action_line is not None:
                    "[no_action_line]"

                $ Girl.change_face("surprised")
                $ Girl.change_stat("inhibition", 70, 1)

                ch_p "[reject_line]"

                $ Girl.nameCheck() #checks reaction to petname

                if Girl == JeanX:
                    $ Girl.change_stat("love", 70, -4)

                "[rejection_response_line]"

                if action not in ["hotdog"]:
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Girl.change_stat("obedience", 30, 2)
                else:
                    $ Girl.change_stat("obedience", 80, 1)
                    $ Girl.change_stat("obedience", 30, 2)

                $ Player.recent_history.append("nope")

                $ Girl.AddWord(1,"refused","refused")

                return True

    return False

label first_action_approval(Girl, action):
    if Girl.Forced:
        $ Girl.change_face("sad")

        if action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "anal", "hotdog"]:
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
        elif action in ["sex"]:
            $ Girl.change_stat("love", 70, -30, 1)
            $ Girl.change_stat("love", 20, -20, 1)
    elif Girl.love >= (Girl.obedience + Girl.inhibition):
        $ Girl.change_face("sexy")
        $ Girl.Brows = "sad"
        $ Girl.Mouth = "smile"

        ch_r "Well, I've never really been able to touch people without draining them, this could be an interesting experience. . ."
        ch_r "If that's what you like. . ."
        ch_r "Huh, well that's certainly one way to get off."
        ch_r "I've never really put something like that in my mouth. . . might be interesting."
        ch_r "I've had a reasonable amount of experience with these, you know. . ."
        ch_r "I haven't actually used one of these, back there before. . ."
        ch_r "Well, I've never been able to do this before now, so this might be fun."
        ch_r "I guess if you really want to try it. . ."
        ch_r "It looks like you need some relief. . ."
    elif Girl.obedience >= Girl.inhibition:
        if action in ["handjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
            $ Girl.change_face("normal")
        elif action in ["footjob"]:
            $ Girl.change_face("normal",1)

        ch_r "If that's what you want, [Girl.Petname]. . ."
        ch_r "If that's what you want. . ."
        ch_r "I suppose, if that's what you want. . ."
        ch_r "Ok, [Girl.Petname], I'm ready."
    elif action in ["handjob", "footjob", "titjob", "blowjob", "sex", "anal", "hotdog"] and Girl.Addict >= 50:
        $ Girl.change_face("manic", 1)

        ch_r "I think, if I could just touch that. . ."
        ch_r "I guess. . ."
        ch_r "I think. . . for some reason I really do want that in my mouth. . ."
        ch_r "Hmmmm. . . ."
        ch_r "Well. . . I bet it would feel really good down there."
    else:
        if action in ["handjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
            $ Girl.change_face("sad")
            $ Girl.Mouth = "smile"
        elif action in ["footjob"]:
            $ Girl.change_face("lipbite",1)

        ch_r "Hmm, could be fun. . ."
        ch_r "Sure. . ."
        ch_r "Heh, might be fun."
        ch_r "I guess. . ."
        ch_r "I guess it could be fun with a partner. . ."
        ch_r "Hmm, I've always wanted to try it. . ."
        ch_r "Hmm, it has been on my list. . ."
        ch_r "Hmm, you look ready for it, at least. . ."

    return

label first_action_reaction(Girl, action):
    if action == "fondle_thighs":
        $ Girl.SEXP += 3
    elif action in ["fondle_breasts", "suck_breasts", "fondle_ass"]:
        $ Girl.SEXP += 4
    elif action in ["fondle_pussy"]:
        $ Girl.SEXP += 7
    elif action in ["finger_pussy", "eat_pussy", "handjob", "footjob", "dildo_pussy", "hotdog"]:
        $ Girl.SEXP += 10
    elif action in ["finger_ass", "titjob"]:
        $ Girl.SEXP += 12
    elif action in ["eat_ass", "blowjob"]:
        $ Girl.SEXP += 15
    elif action in ["sex"]:
        $ Girl.SEXP += 20
    elif action in ["anal"]:
        $ Girl.SEXP += 25

    if not action_context:
        if Girl.love >= 500 and "unsatisfied" not in Girl.recent_history:
            $ Girl.Mouth = "smile"
            call that_was_nice_lines(Girl)
        elif action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass", "dildo_pussy", "dildo_ass"] and Girl.obedience <= 500 and Player.Focus <= 20:
            $ Girl.change_face("perplexed", 1)

            call was_that_enough_lines(Girl)
        elif action in ["handjob", "footjob", "titjob", "blowjob", "sex", "anal", "hotdog"] and  Player.Focus <= 20:
            $ Girl.Mouth = "sad"

            call was_that_enough_lines(Girl)

    return

label first_action_stats(Girl, action):
    if action == "fondle_thighs" and not Girl.FondleT:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -10)
            $ Girl.change_stat("obedience", 70, 15)
            $ Girl.change_stat("inhibition", 80, 10)
        else:
            $ Girl.change_stat("love", 90, 5)
            $ Girl.change_stat("obedience", 70, 10)
            $ Girl.change_stat("inhibition", 80, 15)
    elif action == "fondle_breasts" and not Girl.FondleB:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -20)
            $ Girl.change_stat("obedience", 70, 25)
            $ Girl.change_stat("inhibition", 80, 15)
        else:
            $ Girl.change_stat("love", 90, 10)
            $ Girl.change_stat("obedience", 70, 5)
            $ Girl.change_stat("inhibition", 80, 15)
    elif action == "suck_breasts" and not Girl.SuckB:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -25)
            $ Girl.change_stat("obedience", 70, 25)
            $ Girl.change_stat("inhibition", 80, 17)
        else:
            $ Girl.change_stat("love", 90, 10)
            $ Girl.change_stat("obedience", 70, 10)
            $ Girl.change_stat("inhibition", 80, 15)
    elif action == "fondle_pussy" and not Girl.FondleP:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -50)
            $ Girl.change_stat("obedience", 70, 35)
            $ Girl.change_stat("inhibition", 80, 25)
        else:
            $ Girl.change_stat("love", 90, 10)
            $ Girl.change_stat("obedience", 70, 10)
            $ Girl.change_stat("inhibition", 80, 15)
    elif action == "finger_pussy" and not Girl.InsertP:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -60)
            $ Girl.change_stat("obedience", 70, 55)
            $ Girl.change_stat("inhibition", 80, 35)
        else:
            $ Girl.change_stat("love", 90, 10)
            $ Girl.change_stat("obedience", 70, 20)
            $ Girl.change_stat("inhibition", 80, 25)
    if action == "eat_pussy" and not Girl.LickP:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -30)
            $ Girl.change_stat("obedience", 70, 35)
            $ Girl.change_stat("inhibition", 80, 75)
        else:
            $ Girl.change_stat("love", 90, 35)
            $ Girl.change_stat("obedience", 70, 15)
            $ Girl.change_stat("inhibition", 80, 35)
    elif action == "fondle_ass" and not Girl.FondleA:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -20)
            $ Girl.change_stat("obedience", 70, 20)
            $ Girl.change_stat("inhibition", 80, 15)
        else:
            $ Girl.change_stat("love", 90, 10)
            $ Girl.change_stat("obedience", 70, 12)
            $ Girl.change_stat("inhibition", 80, 20)
    elif action == "finger_ass" and not Girl.InsertA:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -50)
            $ Girl.change_stat("obedience", 70, 60)
            $ Girl.change_stat("inhibition", 80, 35)
        else:
            $ Girl.change_stat("love", 90, 10)
            $ Girl.change_stat("obedience", 70, 20)
            $ Girl.change_stat("inhibition", 80, 25)
    elif action == "eat_ass" and not Girl.LickA:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -30)
            $ Girl.change_stat("obedience", 70, 40)
            $ Girl.change_stat("inhibition", 80, 80)
        else:
            $ Girl.change_stat("love", 90, 35)
            $ Girl.change_stat("obedience", 70, 25)
            $ Girl.change_stat("inhibition", 80, 55)
    elif action == "handjob" and not Girl.Hand:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -20)
            $ Girl.change_stat("obedience", 70, 25)
            $ Girl.change_stat("inhibition", 80, 30)
        else:
            $ Girl.change_stat("love", 90, 5)
            $ Girl.change_stat("obedience", 70, 20)
            $ Girl.change_stat("inhibition", 80, 20)
    elif action == "footjob" and not Girl.Foot:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -20)
            $ Girl.change_stat("obedience", 70, 25)
            $ Girl.change_stat("inhibition", 80, 30)
        else:
            $ Girl.change_stat("love", 90, 5)
            $ Girl.change_stat("obedience", 70, 20)
            $ Girl.change_stat("inhibition", 80, 20)
    elif action == "titjob" and not Girl.Tit:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -25)
            $ Girl.change_stat("obedience", 70, 30)
            $ Girl.change_stat("inhibition", 80, 35)
        else:
            $ Girl.change_stat("love", 90, 5)
            $ Girl.change_stat("obedience", 70, 25)
            $ Girl.change_stat("inhibition", 80, 30)
    elif action == "blowjob" and not Girl.Blow:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -70)
            $ Girl.change_stat("obedience", 70, 45)
            $ Girl.change_stat("inhibition", 80, 60)
        else:
            $ Girl.change_stat("love", 90, 5)
            $ Girl.change_stat("obedience", 70, 35)
            $ Girl.change_stat("inhibition", 80, 40)
    elif action == "dildo_pussy" and not Girl.DildoP:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -75)
            $ Girl.change_stat("obedience", 70, 60)
            $ Girl.change_stat("inhibition", 80, 35)
        else:
            $ Girl.change_stat("love", 90, 10)
            $ Girl.change_stat("obedience", 70, 20)
            $ Girl.change_stat("inhibition", 80, 45)
    elif action == "dildo_ass" and not Girl.DildoA:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -75)
            $ Girl.change_stat("obedience", 70, 60)
            $ Girl.change_stat("inhibition", 80, 35)
        else:
            $ Girl.change_stat("love", 90, 10)
            $ Girl.change_stat("obedience", 70, 20)
            $ Girl.change_stat("inhibition", 80, 45)
    elif action == "sex" and not Girl.Sex:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -150)
            $ Girl.change_stat("obedience", 70, 60)
            $ Girl.change_stat("inhibition", 80, 50)
        else:
            $ Girl.change_stat("love", 90, 30)
            $ Girl.change_stat("obedience", 70, 30)
            $ Girl.change_stat("inhibition", 80, 60)
    elif action == "anal" and not Girl.Anal:
        if not Girl.Anal:
            if Girl.Forced:
                $ Girl.change_stat("love", 90, -150)
                $ Girl.change_stat("obedience", 70, 70)
                $ Girl.change_stat("inhibition", 80, 40)
            else:
                $ Girl.change_stat("love", 90, 10)
                $ Girl.change_stat("obedience", 70, 30)
                $ Girl.change_stat("inhibition", 80, 70)
        elif not Girl.Loose:
            if Girl.Forced:
                $ Girl.change_stat("love", 90, -20)
                $ Girl.change_stat("obedience", 70, 10)
                $ Girl.change_stat("inhibition", 80, 5)
            else:
                $ Girl.change_stat("obedience", 70, 7)
                $ Girl.change_stat("inhibition", 80, 5)
    elif action == "hotdog" and not Girl.Hotdog:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -5)
            $ Girl.change_stat("obedience", 70, 20)
            $ Girl.change_stat("inhibition", 80, 10)
        else:
            $ Girl.change_stat("love", 90, 20)
            $ Girl.change_stat("obedience", 70, 20)
            $ Girl.change_stat("inhibition", 80, 20)

    return

label action_specific_consequences(Girl, action):
    $ achievement = None

    if action == "fondle_thighs":
        $ Girl.FondleT += 1

        $ counter = Girl.FondleT

        call Partner_Like(Girl, 1, 0)
    elif action == "fondle_breasts":
        $ Girl.FondleB += 1

        $ counter = Girl.FondleB

        call Partner_Like(Girl, 2)
    elif action == "suck_breasts":
        $ Girl.SuckB += 1

        $ counter = Girl.SuckB

        call Partner_Like(Girl, 2)
    elif action == "fondle_pussy":
        $ Girl.FondleP += 1

        $ counter = Girl.FondleP

        call Partner_Like(Girl, 2)
    elif action == "finger_pussy":
        $ Girl.InsertP += 1

        $ counter = Girl.InsertP

        call Partner_Like(Girl, 2)
    elif action == "eat_pussy":
        $ Girl.LickP += 1

        $ counter = Girl.LickP

        if Girl == RogueX and Partner == EmmaX:
            call Partner_Like(Girl,4,3)
        elif Girl not in [KittyX, StormX] and Partner == RogueX:
            call Partner_Like(Girl, 3, 3)
        elif Girl == RogueX:
            call Partner_Like(Girl,3,2)
        else:
            call Partner_Like(Girl, 2)
    elif action == "fondle_ass":
        $ Girl.FondleA += 1

        $ counter = Girl.FondleA

        call Partner_Like(Girl, 2)
    elif action == "finger_ass":
        $ Girl.InsertA += 1

        $ counter = Girl.InsertA

        call Partner_Like(Girl, 2)
    elif action == "eat_ass":
        $ Girl.LickA += 1

        $ counter = Girl.LickA

        call Partner_Like(Girl, 2)
    elif action == "handjob":
        $ Girl.Hand += 1

        $ achievement = Girl.Tag + " Handi-Queen"
        $ counter = Girl.Hand

        call Partner_Like(Girl, 2)
    elif action == "footjob":
        $ Girl.Foot += 1

        $ achievement = Girl.Tag + "pedi"
        $ counter = Girl.Foot

        call Partner_Like(Girl, 1)
    elif action == "titjob":
        $ Girl.Tit += 1

        $ counter = Girl.Tit

        call Partner_Like(Girl, 3)
    elif action == "blowjob":
        $ Girl.Blow += 1

        $ achievement = Girl.Tag + " Jobber"
        $ counter = Girl.Blow

        if Girl == RogueX and Partner == EmmaX:
            call Partner_Like(Girl, 3)
        else:
            call Partner_Like(Girl, 2)
    elif action == "dildo_pussy":
        $ Girl.DildoP += 1

        $ counter = Girl.DildoP

        call Partner_Like(Girl, 2)
    elif action == "dildo_ass":
        $ Girl.DildoA += 1

        $ counter = Girl.DildoA

        call Partner_Like(Girl, 2)
    elif action == "sex":
        $ Girl.Sex += 1

        $ achievement = Girl.Tag + " Sex Addict"
        $ counter = Girl.Sex

        call Partner_Like(Girl, 3, 2)

        $ Girl.change_stat("inhibition", 30, 2)
        $ Girl.change_stat("inhibition", 70, 1)
    elif action == "anal":
        $ Girl.Anal += 1

        $ achievement = Girl.Tag + " Anal Addict"
        $ counter = Girl.Anal

        if Partner == "Kitty":
            if Girl == RogueX:
                call Partner_Like(Girl, 3, 1)
            elif Girl in [EmmaX, LauraX, JeanX, StormX, JubesX]:
                call Partner_Like(Girl, 4, 2)
        else:
            if Girl == RogueX:
                call Partner_Like(Girl, 4, 2)
            elif Girl in [EmmaX, LauraX, JeanX, StormX, JubesX]:
                call Partner_Like(Girl, 3, 2)

        $ Girl.change_stat("inhibition", 30, 3)
        $ Girl.change_stat("inhibition", 70, 1)
    elif action == "hotdog":
        $ Girl.Hotdog += 1

        $ achievement = Girl.Tag + " Full Buns"
        $ counter = Girl.Hotdog

        if Girl == RogueX:
            call Partner_Like(Girl, 1)
        elif Girl in [KittyX, EmmaX, LauraX]:
            call Partner_Like(Girl, 2)

        $ Girl.change_stat("inhibition", 30, 1)
        $ Girl.change_stat("inhibition", 70, 1)

    return

label action_approved(Girl, action, action_counter):                                                                      #Second time+ dialog
    if Girl.Forced:
        $ Girl.change_face("sad")
        $ Girl.change_stat("love", 70, -3, 1)
        $ Girl.change_stat("love", 20, -2, 1)

        ch_r "That's really what you want?"
        ch_r "That's it?"
        ch_r "This isn't going to become a habit, will it?"
        ch_r "You want me to do that again?"
        ch_r "The toys again?"
        ch_r "That's all you want?"
    elif not Taboo and "tabno" in Girl.daily_history:
        ch_r "Ok, I guess this is private enough. . ."
        ch_r "I guess here would be ok. . ."
        ch_r "Well, at least you got us some privacy this time. . ."
    elif action == "anal" and "anal" in Girl.daily_history and not Girl.Loose:
        pass
    elif action in Girl.recent_history:
        $ Girl.change_face("sexy", 1)

        call recent_action_lines(Girl)

        if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
            call before_handjob
        elif action in ["sex", "anal", "hotdog"]:
            call before_action

        return
    elif action in Girl.daily_history:
        $ Girl.change_face("sexy", 1)

        call daily_action_lines(Girl)

    elif action_counter < 3:
        $ Girl.change_face("sexy", 1)
        $ Girl.Brows = "confused"
        $ Girl.Mouth = "kiss"

        ch_r "So you'd like another handy?"
        ch_r "Again?"
        ch_r "So you'd like another titjob?"
        ch_r "So you'd like another blowjob?"
        ch_r "You want to stick it in my pussy again?"
        ch_r "You want to stick it in my ass again?"
        ch_r "So you'd like another go?"
    else:
        $ Girl.change_face("sexy", 1)
        $ Girl.ArmPose = 2

        call used_to_action_lines(Girl)

    $ line = 0

    return

label action_disapproved(Girl, action, action_counter):
    if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
        $ Girl.change_face("angry", 1)
    elif action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "sex"]:
        $ Girl.change_face("angry")

    if "no_" + action in Girl.recent_history:
        call just_told_you_no_lines(Girl)
    elif Taboo and "tabno" in Girl.daily_history and "no_" + action in Girl.daily_history:
        call had_enough_of_this_lines(Girl)
    elif "no_" + action in Girl.daily_history:
        call already_said_no_lines(Girl)
    elif Taboo and "tabno" in Girl.daily_history:
        call already_said_not_here_lines(Girl)
    elif not action_counter:
        $ Girl.change_face("bemused")

        if action not in ["finger_ass", "eat_ass"]:
            call not_ready_yet_lines(Girl)
        else:
            call not_into_ass_play(Girl)
    elif action in ["dildo_ass", "anal"] and not Girl.Loose and action not in Girl.daily_history:
        $ Girl.change_face("perplexed")

        ch_r "You could have been a bit more gentle last time, [Girl.Petname]. . ."
    else:
        $ Girl.change_face("bemused")

        call rather_not_lines(Girl)

    call begging_menu(Girl, action)

    return

label action_accepted(Girl, action):
    $ Girl.change_face("bemused", 1)

    if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy"]:
        if Girl.Forced:
            $ Girl.change_face("sad")

            if action in ["fondle_thighs"]:
                $ Girl.change_stat("love", 70, -3, 1)
                $ Girl.change_stat("obedience", 90, 1)
                $ Girl.change_stat("inhibition", 60, 1)
            elif action in ["fondle_breasts", "suck_breasts", "fondle_pussy"]:
                $ Girl.change_stat("love", 70, -3, 1)
                $ Girl.change_stat("love", 20, -2, 1)
                $ Girl.change_stat("obedience", 90, 1)
                $ Girl.change_stat("inhibition", 60, 1)

        call come_and_get_em_lines(Girl)

        $ Girl.change_stat("love", 90, 1)
        $ Girl.change_stat("inhibition", 50, 3)

        call before_fondle
    elif action in ["finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
        if Girl.Forced:
            $ Girl.change_face("sad")

            if action in ["finger_pussy", "eat_pussy", "finger_ass"]:
                $ Girl.change_stat("love", 70, -3, 1)
                $ Girl.change_stat("love", 20, -2, 1)
                $ Girl.change_stat("obedience", 90, 1)
                $ Girl.change_stat("inhibition", 60, 1)
            elif action in ["fondle_ass"]:
                $ Girl.change_stat("love", 70, -2, 1)
                $ Girl.change_stat("obedience", 90, 2)
                $ Girl.change_stat("inhibition", 60, 2)
            elif action in ["eat_ass"]:
                $ Girl.change_stat("love", 70, -3, 1)
                $ Girl.change_stat("love", 20, -2, 1)
                $ Girl.change_stat("obedience", 90, 2)
                $ Girl.change_stat("inhibition", 60, 2)

            call forced_but_welcome_lines(Girl)
        else:
            if action in ["finger_pussy", "eat_pussy"]:
                $ Girl.change_face("sexy", 1)

                if action in ["finger_pussy"]:
                    $ Girl.change_stat("love", 90, 1)
                    $ Girl.change_stat("inhibition", 50, 3)
                elif action in ["eat_pussy", "finger_ass"]:
                    $ Girl.Eyes = "closed"
                    $ Girl.change_stat("love", 90, 1)
                    $ Girl.change_stat("inhibition", 50, 3)
                    $ Girl.change_stat("lust", 200, 3)
                elif action in ["eat_ass"]:
                    $ Girl.Eyes = "closed"
                    $ Girl.change_stat("love", 90, 1)
                    $ Girl.change_stat("inhibition", 60, 2)
                    $ Girl.change_stat("lust", 200, 3)
            elif action in ["fondle_ass"]:
                $ Girl.change_face("bemused, 1")

            call come_and_get_em_lines(Girl)

        if action in ["finger_pussy", "eat_pussy", "finger_ass"]:
            $ Girl.change_stat("obedience", 20, 1)
            $ Girl.change_stat("obedience", 60, 1)
            $ Girl.change_stat("inhibition", 70, 2)
        elif action in ["fondle_ass"]:
            $ Girl.change_stat("lust", 200, 3)
            $ Girl.change_stat("obedience", 60, 1)
            $ Girl.change_stat("inhibition", 70, 1)
        elif action in ["eat_ass"]:
            $ Girl.change_stat("obedience", 20, 1)
            $ Girl.change_stat("obedience", 60, 1)
            $ Girl.change_stat("inhibition", 80, 2)

        call before_fondle
    elif action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:                                                                   #She's into it. . .
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("inhibition", 60, 1)

            if action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal"]:
                $ Girl.change_stat("obedience", 90, 1)
            elif action in ["hotdog"]:
                $ Girl.change_stat("obedience", 80, 1)

            ch_r "Ok, fine."
            ch_r ". . . Ok, if that's what you want."
            ch_r "Well, there are worst ways to get you off. . ."
            ch_r "Whatever."
        elif "no_" + action in Girl.daily_history:
            ch_r "I guess if it'll get you off. . ."
            ch_r "Fine!"
            ch_r "Hmm, I suppose. . ."
            ch_r "Oh, I suppose it isn't so bad. . ."
            ch_r "Ok, you've won me over on this one. . ."
            ch_r "Ok, ok, I have been itching for this. . ."
            ch_r "Well, I guess it's not so bad. . ."
        else:
            $ Girl.change_face("sexy", 1)

            if action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal"]:
                $ Girl.change_stat("love", 90, 1)
                $ Girl.change_stat("inhibition", 50, 3)
            elif action in ["hotdog"]:
                $ Girl.change_stat("love", 80, 1)
                $ Girl.change_stat("inhibition", 50, 2)

            $ line = renpy.random.choice(["Well, sure, put'im here.",
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
            ch_r "[line]"

            $ line = 0

        $ Girl.change_stat("obedience", 20, 1)

        if action in ["handjob", "footjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
            $ Girl.change_stat("obedience", 60, 1)
            $ Girl.change_stat("inhibition", 70, 2)
        elif action in ["titjob", "blowjob"]:
            $ Girl.change_stat("obedience", 70, 1)
            $ Girl.change_stat("inhibition", 80, 2)

        if action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass"]:
            call before_handjob
        elif action in ["sex", "anal", "hotdog"]:
            call before_action

    return

label action_rejected(Girl, action, action_counter):
    if "no_" + action in Girl.daily_history:
        $ Girl.change_face("angry", 1)

        call learn_to_take_no_lines(Girl)

        $ Girl.AddWord(1,"angry","angry")
    elif Girl.Forced:
        call went_too_far_lines(Girl)

        if action in ["fondle_thighs"]:
            $ Girl.change_stat("lust", 50, 2)
            $ Girl.change_stat("obedience", 50, -1)
        elif action in ["hotdog"]:
            $ Girl.change_stat("lust", 200, 5)

            if Girl.love > 300:
                $ Girl.change_stat("love", 70, -1)

            $ Girl.change_stat("obedience", 50, -1)
        else:
            if action in ["fondle_pussy"]:
                $ Girl.change_stat("lust", 70, 5)
            elif action in ["eat_pussy"]:
                $ Girl.change_stat("lust", 80, 5)
            elif action in ["fondle_breasts", "suck_breasts", "fondle_ass"]:
                $ Girl.change_stat("lust", 60, 5)
            elif action in ["finger_ass", "eat_ass"]:
                if ApprovalCheck(Girl, 500, "I"):
                    $ Girl.change_stat("lust", 80, 10)
                else:
                    $ Girl.change_stat("lust", 50, 3)
            elif action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal"]:
                $ Girl.change_stat("lust", 200, 5)

                if Girl.love > 300:
                    $ Girl.change_stat("love", 70, -2)

            $ Girl.change_stat("obedience", 50, -2)

        $ Girl.AddWord(1, "angry", "angry")
    elif Taboo:
        $ Girl.change_face("angry", 1)
        $ Girl.AddWord(1, "tabno", "tabno")

        call not_in_public_lines(Girl)

        if action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
            $ Girl.change_stat("lust", 200, 5)
            $ Girl.change_stat("obedience", 50, -3)
    elif action in ["dildo_ass", "anal"] and not Girl.Loose and action in Girl.daily_history:
        $ Girl.change_face("bemused")

        ch_r "Sorry, I just need a little break back there, [Girl.Petname]."
    elif action_counter:
        $ Girl.change_face("sad")

        call you_had_your_shot_lines(Girl)
    else:
        if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "fondle_ass", "handjob", "blowjob", "sex"]:
            $ Girl.change_face("sexy")
            $ Girl.Mouth = "sad"
        elif action in ["eat_pussy", "finger_ass", "eat_ass", "footjob", "titjob", "dildo_pussy", "dildo_ass", "anal", "hotdog"]:
            $ Girl.change_face("surprised")

        call not_happening_lines(Girl)

        $ Girl.change_face()

    $ Girl.recent_history.append("no_" + action)
    $ Girl.daily_history.append("no_" + action)

    $ temp_modifier = 0

    return

label forced_action(Girl, action):
    if action in ["fondle_thighs", "fondle_breasts"]:
        $ Approval = ApprovalCheck(Girl, 350, "OI", TabM = 2)
    elif action in ["suck_breasts", "fondle_pussy"]:
        $ Approval = ApprovalCheck(Girl, 450, "OI", TabM = 3)
    elif action in ["suck_breasts", "blowjob"]:
        $ Approval = ApprovalCheck(Girl, 750, "OI", TabM = 3)
    elif action in ["eat_pussy"]:
        $ Approval = ApprovalCheck(Girl, 750, "OI", TabM = 4)
    elif action in ["fondle_ass"]:
        $ Approval = ApprovalCheck(Girl, 250, "OI", TabM = 3)
    elif action in ["finger_ass", "dildo_pussy"]:
        $ Approval = ApprovalCheck(Girl, 950, "OI", TabM = 3)
    elif action in ["eat_ass"]:
        $ Approval = ApprovalCheck(Girl, 1100, "OI", TabM = 4)
    elif action in ["handjob"]:
        $ Approval = ApprovalCheck(Girl, 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
    elif action in ["footjob", "hotdog"]:
        $ Approval = ApprovalCheck(Girl, 400, "OI", TabM = 3) # 35, 50, 65, -120(155)
    elif action in ["titjob"]:
        $ Approval = ApprovalCheck(Girl, 700, "OI", TabM = 4) # 70, 85, 100, -160(230)
    elif action in ["dildo_ass"]:
        $ Approval = ApprovalCheck(Girl, 1050, "OI", TabM = 3) # 105, 120, 135, -120(225)
    elif action in ["sex"]:
        $ Approval = ApprovalCheck(Girl, 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
    elif action in ["anal"]:
        $ Approval = ApprovalCheck(Girl, 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)

    if Approval > 1 or (Approval and Girl.Forced):
        $ Girl.change_face("sad")

        if action in ["fondle_thighs", "fondle_breasts", "fondle_ass"]:
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -1, 1)
        elif action in ["suck_breasts", "fondle_pussy", "eat_pussy", "finger_ass", "eat_ass"]:
            $ Girl.change_stat("love", 70, -5, 1)
            $ Girl.change_stat("love", 20, -2, 1)
        elif action in ["handjob", "footjob", "titjob", "blowjob"]:
            $ Girl.change_stat("love", 70, -5, 1)
            $ Girl.change_stat("love", 200, -2)
        elif action in ["dildo_pussy", "dildo_ass", "sex", "anal"]:
            $ Girl.change_stat("love", 70, -5, 1)
            $ Girl.change_stat("love", 200, -5)
        elif action in ["hotdog"]:
            $ Girl.change_stat("love", 70, -2, 1)
            $ Girl.change_stat("love", 200, -5)

        call forced_but_not_unwelcome_lines(Girl)

        if action == "fondle_thighs":
            $ Girl.change_stat("obedience", 50, 3)
            $ Girl.change_stat("inhibition", 60, 2)
        elif action in ["fondle_breasts", "suck_breasts"]:
            $ Girl.change_stat("obedience", 90, 2)
            $ Girl.change_stat("obedience", 50, 4)
            $ Girl.change_stat("inhibition", 60, 3)
        elif action in ["fondle_pussy", "eat_pussy", "finger_ass", "eat_ass", "handjob", "footjob", "titjob", "blowjob"]:
            $ Girl.change_stat("obedience", 50, 4)
            $ Girl.change_stat("inhibition", 80, 1)
            $ Girl.change_stat("inhibition", 60, 3)
        elif action in ["fondle_ass"]:
            $ Girl.change_stat("obedience", 50, 3)
            $ Girl.change_stat("inhibition", 60, 3)
        elif action in ["dildo_pussy", "dildo_ass", "sex", "anal"]:
            $ Girl.change_stat("obedience", 80, 4)
            $ Girl.change_stat("inhibition", 80, 1)
            $ Girl.change_stat("inhibition", 60, 3)
        elif action in ["hotdog"]:
            $ Girl.change_stat("obedience", 80, 4)
            $ Girl.change_stat("inhibition", 60, 2)

        if Approval < 2:
            $ Girl.Forced = 1

        if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
            jump before_fondle
        elif action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass"]:
            jump before_handjob
        elif action in ["sex", "anal", "hotdog"]:
            jump before_action
    else:
        if action in ["fondle_thighs"]:
            $ Girl.change_stat("love", 200, -8)
        elif action in ["fondle_breasts", "suck_breasts", "fondle_ass", "hotdog"]:
            $ Girl.change_stat("love", 200, -10)
        elif action in ["fondle_pussy", "eat_pussy", "finger_ass", "eat_ass", "handjob", "footjob", "titjob", "blowjob"]:
            $ Girl.change_stat("love", 200, -15)
        elif action in ["dildo_pussy", "dildo_ass", "sex", "anal"]:
            $ Girl.change_stat("love", 200, -20)

        $ Girl.change_face("angry", 1)

        if action in ["fondle_thighs", "fondle_breasts", "fondle_pussy", "fondle_ass", "finger_ass"]:
            "She slaps your hand away."
        elif action in ["suck_breasts"]:
            "She shoves your head back out."
        elif action in ["eat_pussy", "eat_ass"]:
            "She shoves your head back."

        $ Girl.AddWord(1, "angry", "angry")

    return

label before_action:
    if primary_action not in ["sex", "anal", "hotdog"]:
        if primary_action in ["fondle_thighs", "fondle_breasts", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
            if primary_action == "kiss_you":
                $ primary_action = primary_action

                return

        if offhand_action == primary_action:
            return

        if primary_action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass"]:
            if Taboo:
                $ focused_Girl.inhibition += int(Taboo/10)
                $ focused_Girl.lust += int(Taboo/5)

            $ focused_Girl.change_face("sexy")

    # we have to fix the launch functions to accept primary_action
    if primary_action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
        if primary_action in ["fondle_thighs", "fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
            if focused_Girl != EmmaX:
                call pussy_launch(focused_Girl, trigger = primary_action)
            else:
                if focused_Girl.Pose in ["doggy", "sex"]:
                    call ViewShift(focused_Girl, focused_Girl.Pose, 0, primary_action)
                else:
                    call ViewShift(focused_Girl, "pussy", 0, primary_action)
        elif primary_action in ["fondle_breasts", "suck_breasts"]:
            call breasts_launch(focused_Girl, trigger = primary_action)

        if not focused_Girl.Forced and action_context != "auto":
            $ temp_modifier = 0

            if primary_action in ["eat_pussy", "eat_ass"] and focused_Girl.PantsNum() >= 6:
                $ temp_modifier = 15

            if primary_action in ["fondle_thighs", "fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
                call Bottoms_Off
            elif primary_action in ["fondle_breasts", "suck_breasts"]:
                call Top_Off
            elif primary_action == "finger_pussy":
                call Girl_Undress(focused_Girl, "bottom")

            if "angry" in focused_Girl.recent_history:
                return

        $ temp_modifier = 0
    elif primary_action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass"]:
        if primary_action in ["handjob", "footjob", "titjob", "blowjob"]:
            if focused_Girl.Forced:
                $ focused_Girl.change_face("sad")
            elif not focused_Girl.Hand:
                $ focused_Girl.Brows = "confused"
                $ focused_Girl.Eyes = "sexy"
                $ focused_Girl.Mouth = "smile"
        elif primary_action in ["dildo_pussy", "dildo_ass"]:
            if not focused_Girl.Forced and action_context != "auto":
                if primary_action == "dildo_pussy":
                    $ temp_modifier = 15 if focused_Girl.PantsNum() > 6 else 0
                elif primary_action == "dildo_ass":
                    $ temp_modifier = 20 if focused_Girl.PantsNum() > 6 else 0

                call Bottoms_Off(focused_Girl)

                if "angry" in focused_Girl.recent_history:
                    return

            $ temp_modifier = 0

        call Seen_First_Peen(focused_Girl, Partner, React = action_context)

        if primary_action == "handjob":
            call handjob_launch(focused_Girl, "L")
        elif primary_action == "footjob":
            call sex_launch(focused_Girl, "foot")
        elif primary_action == "titjob":
            call titjob_launch(focused_Girl, "L")
        elif primary_action == "blowjob":
            call blowjob_launch(focused_Girl, "L")
        elif primary_action in ["dildo_pussy", "dildo_ass"]:
            call pussy_launch
    elif Player.priamry_action in ["sex", "anal", "hotdog"]:
        call Seen_First_Peen(focused_Girl, Partner, React = action_context)

        $ focused_Girl.Pose = "doggy"

        call sex_launch(focused_Girl, "hotdog")

    if primary_action not in ["sex", "anal", "hotdog"]:
        if action_context == focused_Girl:
            $ action_context = 0

            call Girl_initated_action(focused_Girl, primary_action)

            if _return:
                return
    elif primary_action in ["sex", "anal", "hotdog"]:
        if action_context == focused_Girl:
            $ action_context = 0

            call focused_Girl_initiated_action(focused_Girl, primary_action)

            if _return:
                return

            $ focused_Girl.PantiesDown = 1

            call first_bottomless(focused_Girl, 1)
        elif action_context != "auto":
            call AutoStrip(focused_Girl)

            call start_of_sex_narration(focused_Girl, primary_action)
        else:
            if primary_action in ["sex", "anal"]:
                if primary_action == "sex":
                    $ word = renpy.random.choice(["slit"])
                elif primary_action == "anal":
                    $ word = renpy.random.choice(["ass", "back door"])

                if (focused_Girl.PantsNum() > 6 and not focused_Girl.Upskirt) and (focused_Girl.Panties and not focused_Girl.PantiesDown):
                    "You quickly pull down her pants and her [focused_Girl.Panties] and press against her [word]."
                elif (focused_Girl.Panties and not focused_Girl.PantiesDown):
                    "You quickly pull down her [focused_Girl.Panties] and press against her [word]."

                $ focused_Girl.Upskirt = 1
                $ focused_Girl.PantiesDown = 1
                $ focused_Girl.SeenPanties = 1

                call first_bottomless(focused_Girl, 1)
            elif primary_action == "hotdog":
                $ line = renpy.random.choice(["You press yourself against her ass.",
                    "You press yourself against her mound.",
                    "You roll back, pulling her on top of you and your rigid member.",
                    "She lays back, pulling you against her with your rigid member.",
                    "She turns around, pulling you against her with your rigid member."])
                "[line]"

        if Player.Focus >= 50:
            if focused_Girl == EmmaX:
                ch_e "My word [focused_Girl.Petname], your member is hard enough to crack diamond. . . and I should know."
            elif focused_Girl == LauraX:
                ch_l "Nice to see you're ready for business. . ."
            elif focused_Girl == JeanX:
                ch_j "I see you won't need any encouragement. . ."
            elif focused_Girl == StormX:
                ch_s "I must say [focused_Girl.Petname], you certainly do seem to be. . . excited."

    call first_action_stats(focused_Girl, primary_action)

    if Taboo:
        if primary_action == "fondle_thighs":
            $ focused_Girl.change_stat("lust", 200, (int(Taboo/5)))
            $ focused_Girl.change_stat("inhibition", 200, (2*(int(Taboo/5))))
        elif primary_action in ["fondle_breasts", "suck_breasts", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass"]:
            $ focused_Girl.inhibition += int(Taboo/10)
            $ focused_Girl.lust += int(Taboo/5)
        elif primary_action in ["fondle_pussy", "eat_pussy", "finger_ass", "eat_ass"]:
            if focused_Girl == JeanX and focused_Girl.Taboo:
                $ focused_Girl.change_stat("inhibition", 200, (int(Taboo/10)))
            elif Taboo:
                $ focused_Girl.inhibition += int(Taboo/10)

            $ focused_Girl.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()

        $ action_context = 0

    if primary_action in ["eat_pussy", "eat_ass"]:
        if focused_Girl.wearing_skirt:
            $ focused_Girl.Upskirt = 1
            $ focused_Girl.SeenPanties = 1

        if not focused_Girl.Panties:
            call first_bottomless(focused_Girl, 1)

    $ line = 0
    $ counter = 0

    if primary_action == "finger_pussy":
        $ action_speed = 2
    elif primary_action == "sex":
        $ Player.Cock = "in"

        $ primary_action = primary_action
        $ action_speed = 1
    elif primary_action == "anal":
        $ Player.Cock = "anal"

        $ primary_action = primary_action
        $ action_speed = 1

    if Taboo:
        $ focused_Girl.DrainWord("tabno")

    # we have to fix DrainWord and AddWord to accept primary_action
    $ focused_Girl.DrainWord("no_" + primary_action)
    $ focused_Girl.AddWord(0, primary_action, primary_action)

    # we have to fix the launch functions to accept primary_action
    if primary_action in ["fondle_thighs", "fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
        if focused_Girl != EmmaX:
            call pussy_launch(focused_Girl, trigger = primary_action)
        else:
            if focused_Girl.Pose in ["doggy", "sex"]:
                call ViewShift(focused_Girl, focused_Girl.Pose, 0, primary_action)
            else:
                call ViewShift(focused_Girl, "pussy", 0, primary_action)
    elif primary_action in ["fondle_breasts", "suck_breasts"]:
        call breasts_launch(focused_Girl, trigger = primary_action)

label action_cycle:
    if primary_action in ["suck_breasts", "eat_pussy", "eat_ass"]:
        if offhand_action == "kiss_you":
            $ offhand_action = 0

    while Round > 0:
        call Shift_Focus(focused_Girl)

        if primary_action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]
            # we have to fix ViewShift to accept primary_action
            call ViewShift(focused_Girl, focused_Girl.Pose, 0, primary_action)
        elif primary_action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass"]:
            call handjob_launch(focused_Girl)
        elif primary_action in ["sex", "anal", "hotdog"]:
            call sex_launch(focused_Girl, primary_action)

        $ focused_Girl.lustFace()

        if Player.Focus < 100:
            if primary_action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]
                jump fondle_menu

                label fondle_menu_return:
            elif primary_action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass"]:
                jump handjob_menu

                label handjob_menu_return:
            elif primary_action in ["sex", "anal", "hotdog"]:
                jump sex_menu

                label sex_menu_return:

        if primary_action in ["eat_pussy", "fondle_ass", "finger_ass", "eat_ass", "dildo_pussy", "dildo_ass"]:
            if focused_Girl.Panties or focused_Girl.PantsNum() >= 6 or focused_Girl.HoseNum() >= 5: #This checks if Rogue wants to strip down.
                call Girl_Undress(focused_Girl, "auto")

        call Shift_Focus(focused_Girl)
        call Sex_Dialog(focused_Girl, Partner)

        $ counter += 1
        $ Round -= 1

        if (primary_action in ["blowjob"] and action_speed) or primary_action in ["sex", "anal"[]]:
            $ Player.Wet = 1
            $ Player.Spunk = 0 if (Player.Spunk and "in" not in focused_Girl.Spunk) else Player.Spunk #cleans you off after one cycle

        if primary_action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]
            call end_of_fondle_round(focused_Girl, primary_action)
        elif primary_action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass"]:
            end_of_handjob_round(focused_Girl, primary_action)
        elif primary_action in ["sex", "anal", "hotdog"]:
            call end_of_sex_round(focused_Girl, primary_action)

        if _return:
            return

        if primary_action in ["fondle_breasts", "suck_breasts"]:
            if focused_Girl.lust >= 50 and not focused_Girl.Uptop and (focused_Girl.Chest or focused_Girl.Over):
                $ focused_Girl.Uptop = 1

                if focused_Girl == RogueX:
                    "[focused_Girl.name] shrugs and pulls her top open."
                elif focused_Girl == KittyX:
                    "[KittyX.name] laughs and pulls her top open."
                elif focused_Girl in [EmmaX, StormX]:
                    "[EmmaX.name] sighs and tugs her breasts free of her clothes."
                elif focused_Girl in [LauraX, JeanX, JubesX]:
                    "[focused_Girl.name] grunts and pulls her clothes aside."

                call first_topless

    $ focused_Girl.change_face("bemused", 0)

    $ line = 0

    call im_done_lines(focused_Girl)

label after_action:
    if primary_action in ["fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"] and not action_context:
        if primary_action in ["sex", "anal", "hotdog"]:
            $ Player.Sprite = 0
            $ Player.Cock = "out"

        call reset_position(Girl)

    $ focused_Girl.change_face("sexy")
    $ focused_Girl.Action -= 1

    call action_specific_consequences(focused_Girl, primary_action)

    if primary_action not in ["dildo_pussy", "dildo_ass"]:
        $ focused_Girl.Addictionrate += 1

        if "addictive" in Player.Traits:
            $ focused_Girl.Addictionrate += 1

    if primary_action in ["handjob", "footjob"]:
        $ focused_Girl.change_stat("lust", 90, 5)

    if achievement is not None and achievement in Achievements:
        pass
    elif primary_action not in ["dildo_pussy", "dildo_ass"] and counter >= 10:
        if primary_action not in ["anal"]:
            $ focused_Girl.SEXP += 5
        else:
            $ focused_Girl.SEXP += 7

        if achievement is not None:
            $ Achievements.append(achievement)

        if primary_action not in ["anal"] and not action_context:
            $ focused_Girl.change_face("smile", 1)

            ch_r "I guess you can call me \"Handi-Queen.\""
            ch_r "I guess I've gotten used to this foot thing."
            ch_r "I'm really starting to enjoy this."

            if focused_Girl == RogueX:
                ch_r "I think I'm getting addicted to this."
            elif focused_Girl == KittyX:
                ch_k "I just can't seem to quit you."
            elif focused_Girl == EmmaX:
                ch_e "I seem to fit you like a glove. . ."
            elif focused_Girl == LauraX:
                ch_l "We're making this a regular thing, huh. . ."
            elif focused_Girl == JeanX:
                ch_j "Hey, I just noticed we've been doing this a lot. . ."
            elif focused_Girl == StormX:
                ch_s "We do go well together. . ."
            elif focused_Girl == JubesX:
                ch_v "We're making this a regular thing, huh. . ."

            ch_r "I think I'm getting addicted to this."
        elif primary_action in ["anal"] and not action_context:
            $ focused_Girl.change_face("bemused", 1)

            if focused_Girl == RogueX:
                ch_r "I. . . really think I enjoy this. . ."
            elif focused_Girl == KittyX:
                ch_k "I didn't think I'd love this so much!"
            elif focused_Girl == EmmaX:
                ch_e "You're one of the better partners I've had at that."
            elif focused_Girl == LauraX:
                ch_l "I think you've got a knack for that."
            elif focused_Girl == JeanX:
                ch_j "This has been fun exercise."
            elif focused_Girl == StormX:
                ch_s "I have certainly come to enjoy this."
            elif focused_Girl == JubesX:
                ch_v "I think you've got a knack for that."
    elif counter == 1:
        call first_action_reaction(focused_Girl, primary_action)
    elif primary_action in ["handjob", "footjob", "titjob", "blowjob", "sex", "anal", "hotdog"] and counter == 5:
        ch_r "I think I've got this well in hand."
        ch_r "I kinda like this sensation.{p}}Never thought about touching people with my feet."
        ch_r "I think I've got the hang of this."

        if focused_Girl == RogueX:
            ch_r "We're making a regular habit of this."
        elif focused_Girl == KittyX:
            ch_k "Why did we not do this sooner?!"
        elif focused_Girl == EmmaX:
            ch_e "We really should have done this sooner."
            ch_e "I can't imagine why I waited so long."
        elif focused_Girl == LauraX:
            ch_l "You know, this was a good idea."
        elif focused_Girl == JeanX:
            ch_j "You're pretty good at this. . ."
        elif focused_Girl == StormX:
            ch_s "You are quite skilled at this."
            ch_s "I am glad you \"bumped into\" me."
        elif focused_Girl == JubesX:
            ch_v "You know, this was a good idea."

        if focused_Girl == RogueX:
            ch_r "We're making a regular habit of this."
        elif focused_Girl == KittyX:
            ch_k "I'm really starting to love this."
        elif focused_Girl == EmmaX:
            ch_e "You're pretty good at that."
        elif focused_Girl == LauraX:
            ch_l "I'm glad you're into this."
        elif focused_Girl == JeanX:
            ch_j "I'm glad we have similar interests. . ."
        elif focused_Girl == StormX:
            ch_s "You do certainly make the experience enjoyable."
        elif focused_Girl == JubesX:
            ch_v "I'm glad you're into this."

        if focused_Girl == RogueX:
            ch_r "This is. . . interesting."
        elif focused_Girl == KittyX:
            ch_k "I'm surprised how much I enjoy this."
    elif primary_action in ["sex", "anal", "hotdog"] and action_context not in ["auto", "pullback"]:
        if "unsatisfied" in focused_Girl.recent_history:
            $ focused_Girl.change_face("angry")

            if focused_Girl != JeanX:
                $ focused_Girl.Eyes = "side"

            call didnt_get_off_lines(focused_Girl)

    $ temp_modifier = 0

    call Checkout

    if action_context:
        call Sex_Basic_Dialog(focused_Girl, "switch")
        ch_r "Mmm, so what else did you have in mind?"
    else:
        if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
            call reset_position(Girl)
        elif primary_action == "handjob":
            call handjob_reset(focused_Girl)
        elif primary_action == "footjob":
            call doggy_reset(focused_Girl)
        elif primary_action == "titjob":
            call titjob_reset(focused_Girl)
        elif primary_action == "blowjob":
            call blowjob_reset(focused_Girl)

    return
