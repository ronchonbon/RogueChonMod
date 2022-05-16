label girl_initiated_action(Girl, action):
    if action == "kiss":
        "[focused_Girl.name] presses her body against yours, and kisses you deeply."
    elif action in breast_actions:
        if action == "fondle_breasts":
            $ covered_phrase = "arm and shoves your hand against her covered breast"
            $ topless_phrase = "arm and shoves your hand against her breast"
        elif action == "suck_breasts":
            $ covered_phrase = "head and shoves your face into her chest"
            $ topless_phrase = covered_phrase

        if (Girl.Over or Girl.Chest) and not Girl.Uptop:
            if Approvalcheck(Girl, 1250, TabM = 1) or (Girl.SeenChest and Approvalcheck(Girl, 500) and not Taboo):
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
            if Approvalcheck(Girl, 1250, TabM = 1) or (Girl.SeenPussy and Approvalcheck(Girl, 500) and not Taboo):
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
    elif action in job_actions:
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
    elif action in dildo_actions:
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
    elif action in sex_actions:
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

    if action in == "kiss":
        $ action_line = "You lean in to the kiss"
        $ praise_line = "Mmm, this is a nice surprise, " + Girl.Pet
        $ no_action_line = "You pull back."
        $ reject_line = "Let's not do that right now, " + Girl.Pet
    elif action in ["fondle_breasts", "suck_breasts", "fondle_pussy", "eat_pussy", "finger_ass", "handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
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
            "Nothing." if action in job_actions:
                $ Girl.change_stat("inhibition", 70, 3)
                $ Girl.change_stat("inhibition", 30, 2)

                "[action_line]"
            "Go with it." if action in sex_actions:
                if action in ["sex", "anal"]:
                    $ Girl.change_stat("inhibition", 80, 3)
                    $ Girl.change_stat("inhibition", 50, 2)
                elif action in ["hotdog"]:
                    $ Girl.change_stat("inhibition", 50, 3)

                "[action_line]"
            "Go for it." if action in dildo_actions:
                $ Girl.change_face("sexy", 1)
                $ Girl.change_stat("inhibition", 80, 3)

                ch_p "[praise_line]"

                $ Girl.namecheck() #checks reaction to petname

                "You grab the dildo and slide it in."

                $ Girl.change_stat("love", 85, 1)
                $ Girl.change_stat("obedience", 90, 1)
                $ Girl.change_stat("obedience", 50, 2)
            "Praise her." if action not in dildo_actions:
                $ Girl.change_face("sexy", 1)

                if action in ["fondle_breasts", "suck_breasts", "fondle_pussy", "eat_pussy", "finger_ass", "dildo_pussy", "dildo_ass", "sex", "anal"]:
                    $ Girl.change_stat("inhibition", 80, 3)
                elif action in job_actions:
                    $ Girl.change_stat("inhibition", 70, 3)
                elif action in ["hotdog"]:
                    $ Girl.change_stat("inhibition", 80, 2)

                ch_p "[praise_line]"

                $ Girl.namecheck() #checks reaction to petname

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

                $ Girl.namecheck() #checks reaction to petname

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
        call first_action_approval_forced_reactions(Girl, action)
    elif Girl.love >= (Girl.obedience + Girl.inhibition):
        call first_action_approval_mostly_love_reactions(Girl, action)
    elif Girl.obedience >= Girl.inhibition:
        call first_action_approval_mostly_obedience_reactions(Girl, action)
    elif action in cock_actions and Girl.Addict >= 50:
        call first_action_approval_addicted_reactions(Girl, action)
    else:
        call first_action_approval_reactions(Girl, action)

    return

label first_action_response(Girl, action):
    if action == "kiss":
        $ Girl.SEXP += 1

        if Girl == JubesX:
            "[focused_Girl.name] bites your lip as she pulls back, and licks some blood off her lips."

            ch_v "Sorry about that. . ."
            ch_v "Won't happen again."
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
        elif action in cock_actions and  Player.Focus <= 20:
            $ Girl.Mouth = "sad"

            call was_that_enough_lines(Girl)

    return

label action_specific_consequences(Girl, action):
    $ achievement = None

    $ Girl.action_counter[action] += 1
    $ setattr(Girl, action, Girl.action_counter[action])

    if action == "kiss":
        call Partner_Like(Girl, 1)
    if action == "fondle_thighs":
        call Partner_Like(Girl, 1, 0)
    elif action in ["fondle_breasts", "suck_breasts", "fondle_pussy", "finger_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
        call Partner_Like(Girl, 2)
    elif action == "eat_pussy":
        if Girl == RogueX and Partner == EmmaX:
            call Partner_Like(Girl,4,3)
        elif Girl not in [KittyX, StormX] and Partner == RogueX:
            call Partner_Like(Girl, 3, 3)
        elif Girl == RogueX:
            call Partner_Like(Girl,3,2)
        else:
            call Partner_Like(Girl, 2)
    elif action == "handjob":
        $ achievement = Girl.Tag + " Handi-Queen"

        call Partner_Like(Girl, 2)
    elif action == "footjob":
        $ achievement = Girl.Tag + "pedi"

        call Partner_Like(Girl, 1)
    elif action == "titjob":
        call Partner_Like(Girl, 3)
    elif action == "blowjob":
        $ achievement = Girl.Tag + " Jobber"

        if Girl == RogueX and Partner == EmmaX:
            call Partner_Like(Girl, 3)
        else:
            call Partner_Like(Girl, 2)
    elif action in dildo_actions:
        call Partner_Like(Girl, 2)
    elif action == "sex":
        $ achievement = Girl.Tag + " Sex Addict"

        call Partner_Like(Girl, 3, 2)

        $ Girl.change_stat("inhibition", 30, 2)
        $ Girl.change_stat("inhibition", 70, 1)
    elif action == "anal":
        $ achievement = Girl.Tag + " Anal Addict"

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
        $ achievement = Girl.Tag + " Full Buns"

        if Girl == RogueX:
            call Partner_Like(Girl, 1)
        elif Girl in [KittyX, EmmaX, LauraX]:
            call Partner_Like(Girl, 2)

        $ Girl.change_stat("inhibition", 30, 1)
        $ Girl.change_stat("inhibition", 70, 1)

    return

label action_approved(Girl, action):
    if Girl.Forced:
        $ Girl.change_face("sad")
        $ Girl.change_stat("love", 70, -3, 1)
        $ Girl.change_stat("love", 20, -2, 1)

        call action_forcefully_approved_lines(Girl)
    elif not Taboo and "tabno" in Girl.daily_history:
        call private_enough_lines(Girl)
    elif action == "anal" and "anal" in Girl.daily_history and not Girl.Loose:
        pass
    elif action in Girl.recent_history:
        $ Girl.change_face("sexy", 1)

        call recent_action_lines(Girl)

        jump before_action
    elif action in Girl.daily_history:
        $ Girl.change_face("sexy", 1)

        call daily_action_lines(Girl)

    elif Girl.action_counter[action] < 3:
        $ Girl.change_face("sexy", 1)
        $ Girl.Brows = "confused"
        $ Girl.Mouth = "kiss"

        call before_action_less_than_three_times_lines(Girl)
    else:
        $ Girl.change_face("sexy", 1)
        $ Girl.ArmPose = 2

        call used_to_action_lines(Girl)

    $ line = 0

    return

label action_disapproved(Girl, action):
    if action in fondle_actions:
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
    elif not Girl.action_counter[action]:
        $ Girl.change_face("bemused")

        if action not in ["finger_ass", "eat_ass"]:
            call not_ready_yet_lines(Girl)
        else:
            call not_into_ass_play(Girl)
    elif action in anal_insertion_actions and not Girl.Loose and action not in Girl.daily_history:
        $ Girl.change_face("perplexed")

        call anal_insertion_not_loose_lines(Girl)
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

        call before_action
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
            if action in ["finger_pussy", "eat_pussy", "finger_ass", "eat_ass"]:
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

        call before_action
    elif action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:                                                                   #She's into it. . .
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("inhibition", 60, 1)

            if action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal"]:
                $ Girl.change_stat("obedience", 90, 1)
            elif action in ["hotdog"]:
                $ Girl.change_stat("obedience", 80, 1)

            call action_forcefully_accepted_lines(Girl)
        elif "no_" + action in Girl.daily_history:
            call convinced_after_saying_no_lines(Girl)
        else:
            $ Girl.change_face("sexy", 1)

            if action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal"]:
                $ Girl.change_stat("love", 90, 1)
                $ Girl.change_stat("inhibition", 50, 3)
            elif action in ["hotdog"]:
                $ Girl.change_stat("love", 80, 1)
                $ Girl.change_stat("inhibition", 50, 2)

            call accepted_without_question_lines(Girl)

            $ line = 0

        $ Girl.change_stat("obedience", 20, 1)

        if action in ["handjob", "footjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
            $ Girl.change_stat("obedience", 60, 1)
            $ Girl.change_stat("inhibition", 70, 2)
        elif action in ["titjob", "blowjob"]:
            $ Girl.change_stat("obedience", 70, 1)
            $ Girl.change_stat("inhibition", 80, 2)

        jump before_action

    return

label action_rejected(Girl, action):
    if "no_" + action in Girl.daily_history:
        $ Girl.change_face("angry", 1)

        call learn_to_take_no_lines(Girl)

        $ Girl.AddWord(1,"angry","angry")
    elif Girl.Forced:
        call went_too_far_reactions(Girl, action)
    elif Taboo:
        call action_rejected_taboo_reactions(Girl, action)
    elif action in anal_insertion_actions and not Girl.Loose and action in Girl.daily_history:
        call anal_insertion_not_loose_done_today_reactions(Girl)
    elif Girl.action_counter[action]:
        $ Girl.change_face("sad")

        call you_had_your_shot_lines(Girl)
    else:
        call not_happening_reactions(Girl, action)

    $ Girl.recent_history.append("no_" + action)
    $ Girl.daily_history.append("no_" + action)

    $ temp_modifier = 0

    return

label forced_action(Girl, action):
    call forced_approval_checks(Girl, action)

    if Approval > 1 or (Approval and Girl.Forced):
        call forced_but_not_unwelcome_reactions(Girl, action)

        if Approval < 2:
            $ Girl.Forced = 1

        jump before_action
    else:
        call forced_rejected_reactions(Girl, action)

    return

label before_action:
    if offhand_action == primary_action:
        return

    if Taboo:
        $ focused_Girl.inhibition += int(Taboo/10)
        $ focused_Girl.lust += int(Taboo/5)

    $ focused_Girl.change_face("sexy")

    if primary_action == "kiss":
        $ focused_Girl.change_stat("inhibition", 10, 1)
        $ focused_Girl.change_stat("inhibition", 20, 1)

        call kissing_launch(focused_Girl, "kiss")

        if focused_Girl.action_counter["kiss"] >= 10 and focused_Girl.inhibition >= 300:
            $ focused_Girl.change_face("sucking")
        elif focused_Girl.action_counter["kiss"] > 1 and focused_Girl.Addict >= 50:
            $ focused_Girl.change_face("sucking")
        else:
            $ focused_Girl.change_face("kiss",2)

        if focused_Girl == RogueX and not focused_Girl.action_counter["kiss"]:
            jump Rogue_first_kisss
            jump after_action

        if focused_Girl.action_counter["kiss"] >= 10 and focused_Girl.lust >= 80:
            $ line = renpy.random.choice(["She's all over you, running her hands along your body.",
                "She's all over you, licking all over your face and neck.",
                "She's all over you, kissing all over your face and grinding against you."])
        elif focused_Girl.action_counter["kiss"] > 7:
            $ line = renpy.random.choice(["She's really sucking face.",
                "You kiss deeply and passionately.",
                "You kiss deeply and passionately.",
                "You kiss deeply and passionately."])
        elif focused_Girl.action_counter["kiss"] > 3:
            $ line = renpy.random.choice(["She's really getting into it.",
                "She's really getting into it, her tongue's going at it.",
                "She's really getting into it, there's some heavy tongue action."])
        else:
            $ line = "You and "+ focused_Girl.name +" make out for a while."
    elif primary_action in fondle_actions:
        if primary_action in ["fondle_thighs", "fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
            if focused_Girl != EmmaX:
                call pussy_launch(focused_Girl, trigger = primary_action)
            else:
                if focused_Girl.Pose in ["doggy", "sex"]:
                    call ViewShift(focused_Girl, focused_Girl.Pose, 0, primary_action)
                else:
                    call ViewShift(focused_Girl, "pussy", 0, primary_action)
        elif primary_action in breast_actions:
            call breasts_launch(focused_Girl, trigger = primary_action)

        if not focused_Girl.Forced and action_context != "auto":
            $ temp_modifier = 0

            if primary_action in ["eat_pussy", "eat_ass"] and focused_Girl.PantsNum() >= 6:
                $ temp_modifier = 15

            if primary_action in ["fondle_thighs", "fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
                call Bottoms_Off
            elif primary_action in breast_actions:
                call Top_Off
            elif primary_action == "finger_pussy":
                call Girl_Undress(focused_Girl, "bottom")

            if "angry" in focused_Girl.recent_history:
                return

        $ temp_modifier = 0
    elif primary_action in job_actions:
        if primary_action not in dildo_actions:
            if focused_Girl.Forced:
                $ focused_Girl.change_face("sad")
            elif not focused_Girl.Hand:
                $ focused_Girl.Brows = "confused"
                $ focused_Girl.Eyes = "sexy"
                $ focused_Girl.Mouth = "smile"
        else:
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
            call sex_launch(focused_Girl, "footjob")
        elif primary_action == "titjob":
            call titjob_launch(focused_Girl, "L")
        elif primary_action == "blowjob":
            call blowjob_launch(focused_Girl, "L")
        elif primary_action in dildo_actions:
            call pussy_launch
    elif primary_action in sex_actions:
        call Seen_First_Peen(focused_Girl, Partner, React = action_context)

        $ focused_Girl.Pose = "doggy"

        call sex_launch(focused_Girl, "hotdog")

    if primary_action not in sex_actions:
        if action_context == focused_Girl:
            $ action_context = 0

            call girl_initated_action(focused_Girl, primary_action)

            if _return:
                return
    elif primary_action in sex_actions:
        if action_context == focused_Girl:
            $ action_context = 0

            call girl_initiated_action(focused_Girl, primary_action)

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
            call hard_cock_lines(focused_Girl)

    call first_action_reactions(focused_Girl, primary_action)

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

    if primary_action in inside_panties_actions:
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

        $ action_speed = 1
    elif primary_action == "anal":
        $ Player.Cock = "anal"

        $ action_speed = 1

    if Taboo:
        $ focused_Girl.DrainWord("tabno")

    $ focused_Girl.DrainWord("no_" + primary_action)
    $ focused_Girl.AddWord(0, primary_action, primary_action)

    if primary_action in ["fondle_thighs", "fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
        if focused_Girl != EmmaX:
            call pussy_launch(focused_Girl, trigger = primary_action)
        else:
            if focused_Girl.Pose in ["doggy", "sex"]:
                call ViewShift(focused_Girl, focused_Girl.Pose, 0, primary_action)
            else:
                call ViewShift(focused_Girl, "pussy", 0, primary_action)
    elif primary_action in breast_actions:
        call breasts_launch(focused_Girl, trigger = primary_action)

label action_cycle:
    if primary_action in mouth_actions:
        if primary_action != "kiss" and offhand_action == "kiss":
            $ offhand_action = 0

    while Round > 0:
        call shift_focus(focused_Girl)

        if primary_action == "kiss":
            call kissing_launch(focused_Girl, "kiss")

            $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0
        elif primary_action in fondle_actions:
            call ViewShift(focused_Girl, focused_Girl.Pose, 0, primary_action)
        elif primary_action in job_actions:
            call handjob_launch(focused_Girl)
        elif primary_action in sex_actions:
            call sex_launch(focused_Girl, primary_action)

        $ focused_Girl.lustFace()

        if Player.Focus < 100:
            if primary_action == "kiss":
                menu:
                    "Keep going. . .":
                        pass
                    "Slap her ass":
                        call Slap_Ass(focused_Girl)

                        $ counter += 1
                        $ Round -= 1

                        jump action_cycle
                    "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                        pass
                    "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                        "You concentrate on not burning out too quickly."

                        $ Player.FocusX = 1
                    "Release your focus." if Player.FocusX:
                        "You release your concentration. . ."

                        $ Player.FocusX = 0
                    "Start jack'in it." if multi_action and offhand_action != "jackin":
                        call Jackin(focused_Girl)
                    "Stop jack'in it." if multi_action and offhand_action == "jackin":
                        "You stop jack'in it."

                        $ offhand_action = 0
                    "Other options":
                        menu:
                            "Offhand action":
                                if focused_Girl.Action and multi_action:
                                    call Offhand_Set

                                    if offhand_action:
                                         $ focused_Girl.Action -= 1
                                else:
                                    call tired_lines(focused_Girl)
                            "Shift primary action":
                                if focused_Girl.Action and multi_action:
                                    menu:
                                        "Move a hand to her breasts. . ." if focused_Girl.action_counter["kiss"] >= 1 and multi_action:
                                            if focused_Girl.Action and multi_action:
                                                $ action_context = "auto"

                                                call after_action
                                                call fondle_breasts(focused_Girl)

                                                if primary_action == "fondle_breasts":
                                                    $ offhand_action = "kiss"

                                                    $ primary_action = "fondle_breasts"

                                                    call before_action
                                                else:
                                                    $ primary_action = "kiss"
                                            else:
                                                "As your hands creep upwards, she grabs your wrists."

                                                call tired_lines(focused_Girl)
                                        "Move a hand to her thighs. . ." if focused_Girl.action_counter["kiss"] >= 1 and multi_action:
                                            if focused_Girl.Action and multi_action:
                                                $ action_context = "auto"

                                                call after_action
                                                call fondle_thighs(focused_Girl)

                                                if primary_action == "fondle_thighs":
                                                        $ offhand_action = "kiss"

                                                        $ primary_action = "fondle_thighs"

                                                        call before_action
                                                else:
                                                    $ primary_action = "kiss"
                                            else:
                                                "As your hands creep downwards, she grabs your wrists."

                                                call tired_lines(focused_Girl)
                                        "Never Mind":
                                            jump action_cycle
                                else:
                                    call tired_lines(focused_Girl)
                            "Threesome actions (locked)" if not Partner:
                                pass
                            "Threesome actions" if Partner:
                                menu:
                                    "Ask [focused_Girl.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                        call Les_Change(focused_Girl)
                                    "Ask [focused_Girl.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                        pass
                                    "Ask [Partner.name] to do something else":
                                        call Three_Change(focused_Girl)
                                    "Don't stop what you're doing. . .(locked)" if not position_change_timer or not second_girl_primary_action:
                                        $ position_change_timer = 0
                                    "Don't stop what you're doing. . ." if position_change_timer and second_girl_primary_action:
                                        $ position_change_timer = 0
                                    "Swap to [Partner.name]":
                                        call primary_action_Swap(focused_Girl)
                                    "Undress [Partner.name]":
                                        call Girl_Undress(Partner)
                                        call shift_focus(Partner)

                                        jump action_cycle
                                    "Clean up Partner":
                                        call Girl_Cleanup(Partner,"ask")

                                        jump action_cycle
                                    "Never mind":
                                        jump action_cycle
                            "Undress [focused_Girl.name]":
                                call Girl_Undress(focused_Girl)
                            "Clean up [Girl.name] (locked)" if not focused_Girl.Spunk:
                                pass
                            "Clean up [focused_Girl.name]" if focused_Girl.Spunk:
                                call Girl_Cleanup(focused_Girl,"ask")
                            "Never mind":
                                jump action_cycle
                    "Back to Sex Menu" if multi_action and focused_Girl.action_counter["kiss"] >= 5:
                        ch_p "Let's try something else."

                        $ action_context = "shift"
                        $ line = 0

                        jump after_action
                    "End Scene":
                        ch_p "Let's stop for now."

                        $ line = 0

                        jump after_action
            elif primary_action in fondle_actions:
                jump fondle_menu

                label fondle_menu_return:
            elif primary_action in job_actions:
                jump handjob_menu

                label handjob_menu_return:
            elif primary_action in sex_actions:
                jump sex_menu

                label sex_menu_return:

        if primary_action in inside_panties_actions:
            if focused_Girl.Panties or focused_Girl.PantsNum() >= 6 or focused_Girl.HoseNum() >= 5: #This checks if Rogue wants to strip down.
                call Girl_Undress(focused_Girl, "auto")

        call shift_focus(focused_Girl)
        call Sex_Dialog(focused_Girl, Partner)

        $ counter += 1
        $ Round -= 1

        if (primary_action in ["blowjob"] and action_speed) or primary_action in ["sex", "anal"]:
            $ Player.Wet = 1
            $ Player.Spunk = 0 if (Player.Spunk and "in" not in focused_Girl.Spunk) else Player.Spunk #cleans you off after one cycle

        call end_of_action_round(focused_Girl, primary_action)

        if _return:
            return

        if primary_action in breast_actions:
            if focused_Girl.lust >= 50 and not focused_Girl.Uptop and (focused_Girl.Chest or focused_Girl.Over):
                $ focused_Girl.Uptop = 1

                call pulls_off_top_narration(focused_Girl)
                call first_topless

    $ focused_Girl.change_face("bemused", 0)

    $ line = 0

    call im_done_lines(focused_Girl)

label after_action:
    if primary_action in ["fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"] and not action_context:
        if primary_action in sex_actions:
            $ Player.Sprite = 0
            $ Player.Cock = "out"

        call reset_position(focused_Girl)

    $ focused_Girl.change_face("sexy")
    $ focused_Girl.Action -= 1

    call action_specific_consequences(focused_Girl, primary_action)

    if primary_action not in dildo_actions:
        if primary_action == "kiss":
            $ focused_Girl.Addictionrate += 2 if focused_Girl.Addictionrate < 5 else 1
        else:
            $ focused_Girl.Addictionrate += 1

        if Player.addictive:
            $ focused_Girl.Addictionrate += 1

    if primary_action in ["handjob", "footjob"]:
        $ focused_Girl.change_stat("lust", 90, 5)

    if achievement is not None and achievement in Achievements:
        pass
    elif primary_action not in dildo_actions and Girl.action_counter[action] >= 10:
        if primary_action not in ["anal"]:
            $ focused_Girl.SEXP += 5
        else:
            $ focused_Girl.SEXP += 7

        if achievement is not None:
            $ Achievements.append(achievement)

        if primary_action not in ["anal"] and not action_context:
            $ focused_Girl.change_face("smile", 1)
        elif primary_action in ["anal"] and not action_context:
            $ focused_Girl.change_face("bemused", 1)

        call achievement_lines(focused_Girl)
    elif Girl.action_counter[action] == 1:
        call first_action_response(focused_Girl, primary_action)
    elif (primary_action in cock_actions or primary_action == "kiss") and Girl.action_counter[action] == 5:
        call after_action_five_times_lines(focused_Girl)
    elif primary_action in sex_actions and action_context not in ["auto", "pullback"]:
        if "unsatisfied" in focused_Girl.recent_history:
            $ focused_Girl.change_face("angry")

            if focused_Girl != JeanX:
                $ focused_Girl.Eyes = "side"

            call didnt_get_off_lines(focused_Girl)

    if primary_action == "kiss" and not action_context and focused_Girl.action_counter["kiss"] > 5 and focused_Girl.lust > 50 and Approvalcheck(focused_Girl, 950):
        $ focused_Girl.change_face("sexy", 1)
        $ focused_Girl.Brows = "sad"

        call would_you_like_more_lines(focused_Girl)

    $ temp_modifier = 0

    call checkout

    if action_context:
        call switching_action_lines(focused_Girl)
    else:
        if primary_action == "kiss":
            call reset_position(focused_Girl)
        if primary_action in fondle_actions:
            call reset_position(focused_Girl)
        elif primary_action == "handjob":
            call handjob_reset(focused_Girl)
        elif primary_action == "footjob":
            call doggy_reset(focused_Girl)
        elif primary_action == "titjob":
            call titjob_reset(focused_Girl)
        elif primary_action == "blowjob":
            call blowjob_reset(focused_Girl)

    return

label end_of_action_round(Girl, action):
    $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus

    if Player.Focus >= 100 or Girl.lust >= 100:
        if Player.Focus >= 100:
            call Player_Cumming(focused_Girl)

            if "angry" in Girl.recent_history:
                if action in sex_actions:
                    call sex_reset(Girl)
                else:
                    call reset_position(Girl)

                return True

            $ Girl.change_stat("lust", 200, 5)

            if 100 > Girl.lust >= 70 and Girl.OCount < 2 and Girl.SEXP >= 20:
                $ Girl.AddWord(0, "unsatisfied", "unsatisfied")

            if Player.Focus > 80:
                jump after_action

            $ line = "came"

        if Girl.lust >= 100:
            call Girl_Cumming(Girl)

            if action_context == "shift" or "angry" in Girl.recent_history:
                jump after_action

        if line == "came": #ex Player.Focus <= 20:
            $ line = 0

            if not Player.Semen:
                if action in sex_actions:
                    "She's emptied you out, you'll need to take a break."
                    "You're pretty wiped, better stop for now."

                    jump after_action
                else:
                    "You're emptied out, you should probably take a break."

            if "unsatisfied" in Girl.recent_history:#And Rogue is unsatisfied,
                call girl_unsatisfied_menu(Girl, action)

    if Partner and Partner.lust >= 100:
        call Girl_Cumming(Partner)

    if action in ["kiss", "handjob", "footjob", "titjob"]:
        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0
    elif action in ["blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

    if Girl.SEXP >= 100 or Approvalcheck(Girl, 1200, "LO"):
        pass
    elif counter == (5 + Girl.action_counter[action]):
        $ Girl.Brows = "confused"

        call warm_hands_lines(Girl)
        call getting_close_lines(Girl)
    elif action in ["dildo_pussy", "dildo_ass"] and Girl.lust >= 80:
        pass
    elif (action in ["handjob, footjob, titjob, blowjob", "sex", "anal", "hotdog"] and counter == (10 + Girl.action_counter[action])) or (action in ["kiss", "dildo_pussy", "dildo_ass"] and (counter == (15 + Girl.action_counter[action]) and Girl.SEXP <= 100 and not Approvalcheck(Girl, 1200, "LO"))):
        if action == "kiss":
            $ Girl.Brows = "confused"

            call try_something_else_lines(Girl)
        else:
            $ Girl.Brows = "angry"

            call getting_rugburn_lines(Girl)
            call done_with_this_lines(Girl)
            call can_we_do_something_else_lines(Girl)

        call try_something_else_menu(Girl, action)

    call Escalation(Girl)

    if Round == 10:
        call wrap_this_up_lines(Girl)
    elif Round == 5:
        call time_to_stop_soon_lines(Girl)

    return False
