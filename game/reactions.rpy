label forced_but_not_unwelcome_reactions(Girl, action):
    $ Girl.change_face("_sad")

    call forced_but_not_unwelcome_changes_A(Girl, action)
    call forced_but_not_unwelcome_lines(Girl, action)
    call forced_but_not_unwelcome_changes_B(Girl, action)

    return

label forced_action_rejected_reactions(Girl, action):
    if action == "masturbation":
        $ Girl.change_face("_angry", 1)

    call forced_action_rejected_lines(Girl, action)
    call forced_action_rejected_changes(Girl, action)

    return

label anal_insertion_not_loose_done_today_reactions(Girl, action):
    $ Girl.change_face("_bemused")

    call anal_insertion_not_loose_done_today_lines(Girl, action)

    return

label otherwise_rejected_reactions(Girl, action):
    if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "fondle_ass", "handjob", "blowjob", "sex"]:
        $ Girl.change_face("_sexy")
        $ Girl.mouth = "_sad"
    elif action in ["eat_pussy", "finger_ass", "eat_ass", "footjob", "titjob", "dildo_pussy", "dildo_ass", "anal", "hotdog"]:
        $ Girl.change_face("_surprised")
    elif action in ["masturbation"]:
        $ Girl.change_face("_normal", 1)

    call otherwise_not_interested_lines(Girl, action)

    $ Girl.change_face()

    return

label taboo_action_rejected_reactions(Girl, action):
    $ Girl.change_face("_angry", 1)

    call taboo_action_rejected_lines(Girl, action)
    call taboo_action_rejected_changes(Girl, action)

    return

label forced_rejected_reactions(Girl, action):
    call forced_rejected_changes(Girl, action)

    $ Girl.change_face("_angry", 1)

    if action in ["fondle_thighs", "fondle_breasts", "fondle_pussy", "fondle_ass", "finger_ass"]:
        "She slaps your hand away."
    elif action in ["suck_breasts"]:
        "She shoves your head back out."
    elif action in ["eat_pussy", "eat_ass"]:
        "She shoves your head back."

    return

label first_action_approval_forced_reactions(Girl, action):
    $ Girl.change_face("_sad")
    $ Girl.change_stat("love", 70, -3, 1)
    $ Girl.change_stat("love", 20, -2, 1)

    return

label first_action_approval_mostly_love_reactions(Girl, action):
    $ Girl.change_face("_sexy")
    $ Girl.brows = "_sad"
    $ Girl.mouth = "_smile"

    call first_action_approval_mostly_love_lines(Girl, action)

    return

label first_action_approval_mostly_obedience_reactions(Girl, action):
    if action in ["masturbation", "handjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
        $ Girl.change_face("_normal")
    elif action in ["footjob"]:
        $ Girl.change_face("_normal",1)

    call first_action_approval_mostly_obedience_lines(Girl, action)

    return

label first_action_approval_addicted_reactions(Girl, action):
    $ Girl.change_face("_manic", 1)

    call first_action_approval_addicted_lines(Girl, action)

    return

label first_action_approval_reactions(Girl, action):
    if action in ["masturbation", "handjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
        $ Girl.change_face("_sad")
        $ Girl.mouth = "_smile"
    elif action in ["footjob"]:
        $ Girl.change_face("_lipbite",1)

    call first_action_approval_lines(Girl, action)

    return

label auto_approved_reactions(Girl, action):
    if action in ["fondle_thighs", "fondle_breasts"]:
        $ Girl.change_face("_sexy")

        call auto_accepted_narrations(Girl, action)
    else:
        $ Girl.change_face("_surprised", 1)

        call auto_accepted_narrations(Girl, action)

        $ Girl.change_face("_sexy")

    call auto_accepted_lines(Girl, action)

    return

label auto_rejected_reactions(Girl, action):
    call auto_rejected_changes(Girl, action)

    if action in ["fondle_thighs", "suck_breasts", "fondle_pussy", "finger_ass", "eat_ass"]:
        $ Girl.change_face("_surprised")

        call auto_rejected_lines(Girl, action)
    elif action == "fondle_breasts":
        $ Girl.change_face("_surprised")
        $ Girl.brows = "_confused"

        call auto_rejected_lines(Girl, action)
    elif action == "finger_pussy":
        $ Girl.change_face("_surprised", 2)

        Girl.voice "Oooh!"
        "She slaps your hand back."

        $ Girl.change_face("_perplexed", 1)

        call auto_rejected_lines(Girl, action)
    elif action == "eat_pussy":
        $ Girl.change_face("_surprised")

        call auto_rejected_lines(Girl, action)

        $ Girl.change_face("_perplexed",1)

        "She pushes your head back away from her."
    elif action == "fondle_ass":
        $ Girl.change_face("_surprised")

        call auto_rejected_lines(Girl, action)

        $ Girl.change_face("_bemused")
    elif action in dildo_actions or action in sex_actions:
        $ Girl.brows = "_angry"

        call what_do_you_think_youre_doing_lines(Girl, action)
        call what_do_you_think_youre_doing_menu(Girl, action)

    return

label pullback_reactions(Girl, action):
    $ Girl.change_face("_surprised")
    $ Girl.brows = "_sad"

    call pullback_changes(Girl, action)

    $ lines = ["As you pull back, [Girl.name] looks a little sad."]

    if action in finger_actions:
        $ lines.append("As your finger slides out, [Girl.name] gasps and looks upset.")
        $ lines.append("As your hand pulls out, [Girl.name] gasps and looks upset.")

    $ line = renpy.random.choice(lines)

    "[line]"

    return

label recent_action_reactions(Girl, action):
    $ Girl.change_face("_sexy", 1)

    call recent_action_lines(Girl, action)

    return

label daily_action_reactions(Girl, action):
    $ Girl.change_face("_sexy", 1)

    call daily_action_lines(Girl, action)

    return

label first_time_asking_reactions(Girl, action):
    if primary_action != "footjob":
        $ Girl.change_face("_surprised", 1)
        $ Girl.mouth = "_kiss"

        call first_time_asking_lines(Girl, action)
    else:
        $ Girl.change_face("_confused", 2)

        call first_time_asking_lines(Girl, action)

        $ Girl.blushing = "_blush1"

    if action == "titjob":
        if Girl.action_counter["blowjob"]:
            $ Girl.mouth = "_smile"

            call mouth_not_enough(Girl, action)
        elif Girl.action_counter["handjob"]:
            $ Girl.mouth = "_smile"

            call hand_not_enough(Girl, action)
    elif action == "blowjob":
        if Girl.action_counter["handjob"]:
            $ Girl.mouth = "_smile"

            call hand_not_enough(Girl, action)

    if Girl.forced:
        $ Girl.change_face("_sad")

        call first_time_forcing_lines(Girl, action)

    return

label anal_insertion_reactions(Girl, action):
    $ Girl.change_face("_bemused", 1)

    call anal_insertion_not_loose_done_today_lines(Girl, action)

    return

label starting_to_get_bored_reactions(Girl, action):
    $ Girl.brows = "_confused"

    call starting_to_get_bored_lines(Girl, action)

    return

label definitely_bored_now_reactions(Girl, action):
    if action == "kiss":
        $ Girl.brows = "_confused"

        call try_something_else_lines(Girl, action)
    else:
        $ Girl.brows = "_angry"

        call definitely_bored_now_lines(Girl, action)

    call try_something_else_menu(Girl, action)

    return

label unsatisfied_reactions(Girl, action):
    $ Girl.change_face("_angry")

    if Girl != JeanX:
        $ Girl.eyes = "_side"

    call unsatisfied_lines(Girl, action)

    return

label would_you_like_more_reactions(Girl, action):
    $ Girl.change_face("_sexy", 1)
    $ Girl.brows = "_sad"

    call would_you_like_more_lines(Girl, action)

    return

label end_of_action_reactions(Girl, action):
    $ Girl.change_face("_bemused", 0)

    call end_of_action_lines(Girl, action)

label sex_acts(action = 0):
    if Alonecheck(focused_Girl) and focused_Girl.taboo == 20:
        $ focused_Girl.taboo = 0
        $ taboo = 0

    call shift_focus(focused_Girl)

    if action == "SkipTo":
        $ renpy.pop_call() #causes it to skip past the primary_action Swap
        $ renpy.pop_call()

        call SkipTo(focused_Girl)
    elif action == "switch":
        $ renpy.pop_call()
    elif action == "masturbation":
        call before_show

        if not action_context:
            return
    elif action == "lesbian":
        call Les_Prep(focused_Girl)

        if not action_context:
            return
    elif action:
        $ primary_action = action

        call before_action

        if not action_context:
            return

    return

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

        if (Girl.outfit["top"] or Girl.outfit["bra"]) and not Girl.top_pulled_up:
            if approval_check(Girl, 1250, taboo_modifier = 1) or (Girl.seen_breasts and approval_check(Girl, 500) and not taboo):
                $ Girl.top_pulled_up = 1

                $ line = Girl.outfit["top"] if Girl.outfit["top"] else Girl.outfit["bra"]

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


        if (Girl.outfit["bottom"] and not Girl.upskirt) or (Girl.outfit["underwear"] and not Girl.underwear_pulled_down):
            if approval_check(Girl, 1250, taboo_modifier = 1) or (Girl.seen_pussy and approval_check(Girl, 500) and not taboo):
                $ Girl.upskirt = 1
                $ Girl.underwear_pulled_down = 1

                $ line = 0

                if Girl.wearing_skirt:
                    $ line = Girl.name + " hikes up her skirt"
                elif Girl.bottom_number() > 6:
                    $ line = Girl.name + " pulls down her " + Girl.outfit["bottom"]
                else:
                    $ line = 0

                if Girl.outfit["underwear"]:
                    if line:
                        "[line] and pulls her [Girl.outfit['underwear']] out of the way."
                        "She then [phrase], clearly intending you to get to work."
                    else:
                        "She pulls her [Girl.outfit['underwear']] out of the way, and then [phrase]."
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
            if offhand_action == "jerking_off":
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

            $ Girl.upskirt = 1
        elif Girl.bottom_number() > 6:
            "[Girl.name] grabs her dildo, pulling down her pants as she does."

            $ Girl.outfit["bottom"] = 0
        else:
            if action == "dildo_pussy":
                "[Girl.name] grabs her dildo, rubbing it suggestively against her crotch."
            elif action == "dildo_ass":
                "[Girl.name] grabs her dildo, rubbing is suggestively against her ass."

        $ Girl.seen_underwear = 1

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

                $ Girl.upskirt = 1
            elif Girl.bottom_number() > 6:
                $ line = renpy.random.choice(["[Girl.name] turns and backs up against your cock, sliding her [Girl.outfit['legs']] down as she does so.",
                    "[Girl.name] rolls back and pulls you against her, sliding her [Girl.outfit['legs']] off as she does so.",
                    "[Girl.name] pushes you down and climbs on top of you, sliding her [Girl.outfit['legs']] down as she does so.",
                    "[Girl.name] turns around, sliding her [Girl.outfit['legs']] down as she does so.",
                    "[Girl.name] lays back, sliding her [Girl.outfit['legs']] down as she does so."])
                "[line]"

                $ Girl.upskirt = 1
            elif Girl.bottom_number() == 6:
                $ line = renpy.random.choice(["[Girl.name] rolls onto her back and pulls you against her, sliding her shorts off as she does so."])
                "[line]"

                $ Girl.upskirt = 1
            else:
                $ line = renpy.random.choice(["[Girl.name] turns and backs up against your cock.",
                    "[Girl.name] rolls back and pulls you toward her.",
                    "[Girl.name] pushes you back and climbs on top of you.",
                    "[Girl.name] turns around and pulls you toward her."])
                "[line]"

            $ Girl.seen_underwear = 1

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
        $ praise_line = "Mmm, this is a nice surprise, " + Girl.player_petname
        $ no_action_line = "You pull back."
        $ reject_line = "Let's not do that right now, " + Girl.player_petname
    elif action in ["fondle_breasts", "suck_breasts", "fondle_pussy", "eat_pussy", "finger_ass", "handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
        if action == "fondle_breasts":
            $ action_line = "You start to fondle them."
            $ praise_line = "I like the initiative, " + Girl.player_petname
            $ no_action_line = "You pull your hand back."
            $ reject_line = "Let's not do that right now, " + Girl.player_petname
            $ rejection_response_line = Girl.name + " pulls back."
        elif action == "suck_breasts":
            $ action_line = "You start to run your tongue along her nipple."
            $ praise_line = "Mmm, I like this, " + Girl.player_petname
            $ no_action_line = "You pull your head back."
            $ reject_line = "Let's not do that right now, " + Girl.player_petname
            $ rejection_response_line = Girl.name + " pulls away."
        elif action == "fondle_pussy":
            $ action_line = "You start to run your fingers along her pussy."
            $ praise_line = "I like the initiative, " + Girl.player_petname
            $ no_action_line = "You pull your hand back."
            $ reject_line = "Let's not do that right now, " + Girl.player_petname
            $ rejection_response_line = Girl.name + " pulls back."
        elif action == "eat_pussy":
            $ action_line = "You start licking her slit."
            $ praise_line = "Mmm, I like this idea, " + Girl.player_petname
            $ no_action_line = "You pull your head away."
            $ reject_line = "Let's not do that right now, " + Girl.player_petname
            $ rejection_response_line = Girl.name + " pulls back."
        elif action == "finger_ass":
            $ action_line = "You press your finger into her tight ass."
            $ praise_line = "Dirty girl, " + Girl.player_petname
            $ no_action_line = "You pull your hand back."
            $ reject_line = "Let's not do that right now, " + Girl.player_petname
            $ rejection_response_line = Girl.name + " pulls back."
        elif action == "handjob":
            $ action_line = "[Girl.name] continues her actions."
            $ praise_line = "Oooh, that's good, [Girl.player_petname]."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [Girl.player_petname]."
            $ rejection_response_line = "[Girl.name] puts it down."
        elif action == "footjob":
            $ action_line = "[Girl.name] continues her actions."
            $ praise_line = "Oooh, that's good, [Girl.player_petname]."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [Girl.player_petname]."
            $ rejection_response_line = "[Girl.name] puts it down."
        elif action == "titjob":
            $ action_line = "[Girl.name] starts to slide them up and down."
            $ praise_line = "Oh, that sounds like a good idea, [Girl.player_petname]."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [Girl.player_petname]."
            $ rejection_response_line = "[Girl.name] lets it drop out from between her breasts."
        elif action == "blowjob":
            $ action_line = "[Girl.name] continues licking at it."
            $ praise_line = "Hmmm, keep doing that, [Girl.player_petname]."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [Girl.player_petname]."
            $ rejection_response_line = "[Girl.name] puts it down."
        elif action == "dildo_pussy":
            $ action_line = "[Girl.name] slides it in."
            $ praise_line = "Oh yeah, [Girl.player_petname], let's do this."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [Girl.player_petname]."
            $ rejection_response_line = "[Girl.name] sets the dildo down."
        elif action == "dildo_ass":
            $ action_line = "[Girl.name] slides it in."
            $ praise_line = "Hmmm, keep doing that, [Girl.player_petname]."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [Girl.player_petname]."
            $ rejection_response_line = "[Girl.name] sets the dildo down."
        elif action == "sex":
            $ action_line = "[Girl.name] slides it in."
            $ praise_line = "Oh yeah, [Girl.player_petname], let's do this."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [Girl.player_petname]."
            $ rejection_response_line = "[Girl.name] pulls back."
        elif action == "anal":
            $ action_line = "[Girl.name] slides it in."
            $ praise_line = "Ooo, dirty girl, [Girl.player_petname], let's do this."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [Girl.player_petname]."
            $ rejection_response_line = "[Girl.name] pulls back."
        elif action == "hotdog":
            $ action_line = renpy.random.choice([Girl.name + " starts to grind against you",
                Girl.name + " keeps grinding",
                Girl.name + " continues to grind"])
            $ praise_line = "Hmmm, that's good, [Girl.player_petname]."
            $ no_action_line = None
            $ reject_line = "Let's not do that for now, [Girl.player_petname]."
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
                $ Girl.change_face("_sexy", 1)
                $ Girl.change_stat("inhibition", 80, 3)

                ch_p "[praise_line]"

                $ Girl.name_check() #checks reaction to petname

                "You grab the dildo and slide it in."

                $ Girl.change_stat("love", 85, 1)
                $ Girl.change_stat("obedience", 90, 1)
                $ Girl.change_stat("obedience", 50, 2)
            "Praise her." if action not in dildo_actions:
                $ Girl.change_face("_sexy", 1)

                if action in ["fondle_breasts", "suck_breasts", "fondle_pussy", "eat_pussy", "finger_ass", "dildo_pussy", "dildo_ass", "sex", "anal"]:
                    $ Girl.change_stat("inhibition", 80, 3)
                elif action in job_actions:
                    $ Girl.change_stat("inhibition", 70, 3)
                elif action in ["hotdog"]:
                    $ Girl.change_stat("inhibition", 80, 2)

                ch_p "[praise_line]"

                $ Girl.name_check() #checks reaction to petname

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

                $ Girl.change_face("_surprised")
                $ Girl.change_stat("inhibition", 70, 1)

                ch_p "[reject_line]"

                $ Girl.name_check() #checks reaction to petname

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

                $ Girl.add_word(1,"refused","refused")

                return True

    return False

label first_action_approval(Girl, action):
    if Girl.forced:
        call first_action_approval_forced_reactions(Girl, action)
    elif Girl.love >= (Girl.obedience + Girl.inhibition):
        call first_action_approval_mostly_love_reactions(Girl, action)
    elif Girl.obedience >= Girl.inhibition:
        call first_action_approval_mostly_obedience_reactions(Girl, action)
    elif action in cock_actions and Girl.addiction >= 50:
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
            $ Girl.mouth = "_smile"
            call satisfied_lines(Girl, action)
        elif action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass", "dildo_pussy", "dildo_ass"] and Girl.obedience <= 500 and Player.focus <= 20:
            $ Girl.change_face("_perplexed", 1)

            call was_that_enough_lines(Girl, action)
        elif action in cock_actions and Player.focus <= 20:
            $ Girl.mouth = "_sad"

            call was_that_enough_lines(Girl, action)

    return

label action_specific_consequences(Girl, action):
    $ achievement = None

    $ Girl.action_counter[action] += 1

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
        $ achievement = Girl.tag + " Handi-Queen"

        call Partner_Like(Girl, 2)
    elif action == "footjob":
        $ achievement = Girl.tag + "pedi"

        call Partner_Like(Girl, 1)
    elif action == "titjob":
        call Partner_Like(Girl, 3)
    elif action == "blowjob":
        $ achievement = Girl.tag + " Jobber"

        if Girl == RogueX and Partner == EmmaX:
            call Partner_Like(Girl, 3)
        else:
            call Partner_Like(Girl, 2)
    elif action in dildo_actions:
        call Partner_Like(Girl, 2)
    elif action == "sex":
        $ achievement = Girl.tag + " Sex Addict"

        call Partner_Like(Girl, 3, 2)
    elif action == "anal":
        $ achievement = Girl.tag + " Anal Addict"

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
    elif action == "hotdog":
        $ achievement = Girl.tag + " Full Buns"

        if Girl == RogueX:
            call Partner_Like(Girl, 1)
        elif Girl in [KittyX, EmmaX, LauraX]:
            call Partner_Like(Girl, 2)

    call action_specific_changes(Girl, action)

    return

label action_approved(Girl, action):
    $ Girl.change_face("_sexy", 1)

    if Girl.forced:
        $ Girl.change_face("_sad")
        $ Girl.change_stat("love", 70, -3, 1)
        $ Girl.change_stat("love", 20, -2, 1)

        call action_forcefully_approved_lines(Girl, action)
    elif not taboo and "no_taboo" in Girl.daily_history:
        call private_enough_lines(Girl, action)
    elif action == "anal" and "anal" in Girl.daily_history and not Girl.used_to_anal:
        pass
    elif action in Girl.recent_history:
        $ Girl.change_face("_sexy", 1)

        call recent_action_lines(Girl, action)

        return True
    elif action in Girl.daily_history:
        $ Girl.change_face("_sexy", 1)

        call daily_action_lines(Girl, action)

        return True
    elif Girl.action_counter[action] < 3:
        $ Girl.change_face("_sexy", 1)
        $ Girl.brows = "_confused"
        $ Girl.mouth = "_kiss"

        call before_action_less_than_three_times_lines(Girl, action)
    else:
        $ Girl.change_face("_sexy", 1)
        $ Girl.arm_pose = 2

        call used_to_action_lines(Girl, action)

    return False

label action_disapproved(Girl, action):
    if action in fondle_actions:
        $ Girl.change_face("_angry", 1)
    elif action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "sex"]:
        $ Girl.change_face("_angry")
    elif action in ["finger_pussy"]:
        $ Girl.change_face("_bemused", 2)

    if "no_" + action in Girl.recent_history:
        call said_no_recently_lines(Girl, action)
    elif taboo and "no_taboo" in Girl.daily_history and "no_" + action in Girl.daily_history:
        call taboo_and_said_no_today_lines(Girl, action)
    elif "no_" + action in Girl.daily_history:
        call said_no_today_lines(Girl, action)
    elif taboo and "no_taboo" in Girl.daily_history:
        call taboo_lines(Girl, action)
    elif not Girl.action_counter[action]:
        $ Girl.change_face("_bemused")

        call action_not_done_yet_lines(Girl, action)
    elif action in anal_insertion_actions and not Girl.used_to_anal and action not in Girl.daily_history:
        $ Girl.change_face("_perplexed")

        call anal_insertion_not_loose_lines(Girl, action)
    elif action != "masturbation":
        $ Girl.change_face("_bemused")

        call otherwise_not_interested_lines(Girl, action)

        if Girl in [RogueX, KittyX, EmmaX, StormX]:
            $ Girl.blushing = "_blush1"
        else:
            $ Girl.blushing = ""

    if action == "masturbation":
        ch_r "That's. . . a little intimate, [RogueX.player_petname]."
        ch_k "That's. . . private? You know?"
        ch_e "I don't know that I want to perform."
        ch_l "I don't know that I want to do that right now."
        ch_j "I don't know, it's kind of a bad time. . ."
        ch_s "I am unsure about this."
        ch_v "I don't know, I'm not really into it right now."

    call begging_menu(Girl, action)

    return

label action_accepted(Girl, action):
    $ Girl.change_face("_bemused", 1)

    if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy"]:
        if Girl.forced:
            $ Girl.change_face("_sad")

            call forced_action_accepted_changes(Girl, action)

        call action_accepted_enthusiastically_lines(Girl, action)
    else:
        if Girl.forced:
            $ Girl.change_face("_sad")

            call forced_action_accepted_changes(Girl, action)
            call action_forcefully_accepted_lines(Girl, action)
        elif "no_" + action in Girl.daily_history:
            call convinced_after_saying_no_lines(Girl, action)
        else:
            if action in ["fondle_ass"]:
                $ Girl.change_face("bemused", 1)
            else:
                $ Girl.change_face("_sexy", 1)

            call not_forced_action_accepted_changes(Girl, action)
            call accepted_without_question_lines(Girl, action)

    call action_accepted_changes(Girl, action)

    return

label action_rejected(Girl, action):
    $ Girl.arm_pose = 1

    if "no_" + action in Girl.daily_history:
        $ Girl.change_face("_angry", 1)

        call action_already_rejected_lines(Girl, action)

        $ Girl.add_word(1,"_angry","_angry")
    elif Girl.forced:
        call forced_action_rejected_reactions(Girl, action)

        $ Girl.add_word(1, "_angry", "_angry")
    elif taboo:
        call taboo_action_rejected_reactions(Girl, action)

        $ Girl.add_word(1, "no_taboo", "no_taboo")
    elif action in anal_insertion_actions and not Girl.used_to_anal and action in Girl.daily_history:
        call anal_insertion_not_loose_done_today_reactions(Girl, action)
    elif Girl.action_counter[action]:
        $ Girl.change_face("_sad")

        call previous_action_rejected_lines(Girl, action)
    else:
        call otherwise_rejected_reactions(Girl, action)

    $ Girl.recent_history.append("no_" + action)
    $ Girl.daily_history.append("no_" + action)

    $ approval_bonus = 0

    return

label forced_action(Girl, action):
    call forced_approval_checks(Girl, action)

    if approval > 1 or (approval and Girl.forced):
        call forced_but_not_unwelcome_reactions(Girl, action)

        if approval < 2:
            $ Girl.forced = 1

        if action == "masturbation":
            jump before_masturbation
        else:
            jump before_action
    else:
        call forced_rejected_reactions(Girl, action)

        $ Girl.add_word(1, "_angry", "_angry")

    return
