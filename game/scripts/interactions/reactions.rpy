label forced_but_not_unwelcome_reactions(Girl, Action_type):
    $ Girl.change_face("sad")

    call forced_but_not_unwelcome_changes_A(Girl, Action_type)
    call forced_but_not_unwelcome_lines(Girl, Action_type)
    call forced_but_not_unwelcome_changes_B(Girl, Action_type)

    return

label forced_action_rejected_reactions(Girl, Action_type):
    if Action_type == "masturbation":
        $ Girl.change_face("angry", blushing = 1)

    call forced_action_rejected_lines(Girl, Action_type)
    call forced_action_rejected_changes(Girl, Action_type)

    return

label otherwise_rejected_reactions(Girl, Action_type):
    if Action_type in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "fondle_ass", "handjob", "blowjob", "sex"]:
        $ Girl.change_face("sexy")
        $ Girl.mouth = "sad"
    elif Action_type in ["eat_pussy", "finger_ass", "eat_ass", "footjob", "titjob", "dildo_pussy", "dildo_ass", "anal", "hotdog"]:
        $ Girl.change_face("surprised")
    elif Action_type in ["masturbation"]:
        $ Girl.change_face("normal", blushing = 1)

    call otherwise_not_interested_lines(Girl, Action_type)

    $ Girl.change_face()

    return

label taboo_action_rejected_reactions(Girl, Action_type):
    $ Girl.change_face("angry", blushing = 1)

    call taboo_action_rejected_lines(Girl, Action_type)
    call taboo_action_rejected_changes(Girl, Action_type)

    return

label forced_rejected_reactions(Girl, Action_type):
    call forced_rejected_changes(Girl, Action_type)

    $ Girl.change_face("angry", blushing = 1)

    if Action_type in ["fondle_thighs", "fondle_breasts", "fondle_pussy", "fondle_ass", "finger_ass"]:
        "She slaps your hand away."
    elif Action_type in ["suck_breasts"]:
        "She shoves your head back out."
    elif Action_type in ["eat_pussy", "eat_ass"]:
        "She shoves your head back."
    else:
        "She shoves you back."

    return

label first_action_approval_forced_reactions(Girl, Action_type):
    $ Girl.change_face("sad")
    call change_Girl_stat(Girl, "love", 1)
    call change_Girl_stat(Girl, "love", 1)

    return

label first_action_approval_mostly_love_reactions(Girl, Action_type):
    $ Girl.change_face("sexy", brows = "sad", mouth = "smile")

    call first_action_approval_mostly_love_lines(Girl, Action_type)

    return

label first_action_approval_mostly_obedience_reactions(Girl, Action_type):
    if Action_type in ["masturbation", "handjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
        $ Girl.change_face("normal")
    elif Action_type in ["footjob"]:
        $ Girl.change_face("normal", blushing = 1)

    call first_action_approval_mostly_obedience_lines(Girl, Action_type)

    return

label first_action_approval_addicted_reactions(Girl, Action_type):
    $ Girl.change_face("manic", blushing = 1)

    call first_action_approval_addicted_lines(Girl, Action_type)

    return

label first_action_approval_reactions(Girl, Action_type):
    if Action_type in ["masturbation", "handjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
        $ Girl.change_face("sad", mouth = "smile")
    elif Action_type in ["footjob"]:
        $ Girl.change_face("lipbite", blushing = 1)

    call first_action_approval_lines(Girl, Action_type)

    return

label auto_approved_reactions(Girl, Action_type):
    if Action_type not in ["fondle_thighs", "fondle_breasts"]:
        $ Girl.change_face("surprised", blushing = 1)

    call auto_accepted_narrations(Girl, Action_type)

    $ Girl.change_face("sexy")

    call auto_accepted_lines(Girl, Action_type)

    return

label auto_rejected_reactions(Girl, Action_type):
    call auto_rejected_changes(Girl, Action_type)

    if Action_type in ["fondle_thighs", "suck_breasts", "fondle_pussy", "finger_ass", "eat_ass"]:
        $ Girl.change_face("surprised")

        call auto_rejected_lines(Girl, Action_type)
    elif Action_type == "fondle_breasts":
        $ Girl.change_face("surprised")
        $ Girl.brows = "confused"

        call auto_rejected_lines(Girl, Action_type)
    elif Action_type == "finger_pussy":
        $ Girl.change_face("surprised", blushing = 2)

        Girl.voice "Oooh!"
        "She slaps your hand back."

        $ Girl.change_face("perplexed", blushing = 1)

        call auto_rejected_lines(Girl, Action_type)
    elif Action_type == "eat_pussy":
        $ Girl.change_face("surprised")

        call auto_rejected_lines(Girl, Action_type)

        $ Girl.change_face("perplexed", blushing = 1)

        "She pushes your head back away from her."
    elif Action_type == "fondle_ass":
        $ Girl.change_face("surprised")

        call auto_rejected_lines(Girl, Action_type)

        $ Girl.change_face("bemused")
    elif Action_type in dildo_actions or Action_type in sex_actions:
        $ Girl.brows = "angry"

        call what_do_you_think_youre_doing_lines(Girl, Action_type)
        call what_do_you_think_youre_doing_menu(Girl, Action_type)

        if _return == "accepted":
            return "accepted"

    $ Girl.recent_history.append("no_" + Action_type)
    $ Girl.daily_history.append("no_" + Action_type)

    return "rejected"

label pullback_reactions(Girl, Action_type):
    $ Girl.change_face("surprised")
    $ Girl.brows = "sad"

    call pullback_changes(Girl, Action_type)

    $ lines = ["As you pull back, " + Girl.name + " looks a little sad."]

    if Action_type in finger_actions:
        $ lines.append("As your finger slides out, " + Girl.name + " gasps and looks upset.")
        $ lines.append("As your hand pulls out, " + Girl.name + " gasps and looks upset.")

    $ line = renpy.random.choice(lines)

    "[line]"

    return

label recent_action_reactions(Girl, Action_type):
    $ Girl.change_face("sexy", blushing = 1)

    call recent_action_lines(Girl, Action_type)

    return

label daily_action_reactions(Girl, Action_type):
    $ Girl.change_face("sexy", blushing = 1)

    call daily_action_lines(Girl, Action_type)

    return

label first_time_asking_reactions(Girl, Action_type):
    if Action_type in ["footjob", "masturbation"]:
        $ Girl.change_face("surprised", blushing = 1, mouth = "kiss")

        call first_time_asking_lines(Girl, Action_type)
    else:
        $ Girl.change_face("confused", blushing = 2)

        call first_time_asking_lines(Girl, Action_type)

        $ Girl.blushing = "_blush1"

    if Action_type == "titjob":
        if Girl.permanent_History["blowjob"]:
            $ Girl.mouth = "smile"

            call mouth_not_enough(Girl, Action_type)
        elif Girl.permanent_History["handjob"]:
            $ Girl.mouth = "smile"

            call hand_not_enough(Girl, Action_type)
    elif Action_type == "blowjob":
        if Girl.permanent_History["handjob"]:
            $ Girl.mouth = "smile"

            call hand_not_enough(Girl, Action_type)

    if Girl.forced:
        $ Girl.change_face("sad")

        if Action_type == "masturbation":
            call action_forcefully_approved_lines(Girl, "masturbation")
        else:
            call first_time_forcing_lines(Girl, Action_type)

    return

label anal_insertion_not_loose_done_today_reactions(Girl, Action_type):
    $ Girl.change_face("bemused", blushing = 1)

    call anal_insertion_not_loose_done_today_lines(Girl, Action_type)

    return

label starting_to_get_bored_reactions(Girl, Action_type):
    $ Girl.brows = "confused"

    call starting_to_get_bored_lines(Girl, Action_type)

    return

label definitely_bored_now_reactions(Girl, Action_type):
    if Action_type == "kiss":
        $ Girl.brows = "confused"

        call try_something_else_lines(Girl, Action_type)
    else:
        $ Girl.brows = "angry"

        call definitely_bored_now_lines(Girl, Action_type)

    call try_something_else_menu(Girl, Action_type)

    return _return

label unsatisfied_reactions(Girl, Action_type):
    $ Girl.change_face("angry", eyes = "side")

    call unsatisfied_lines(Girl, Action_type)

    return

label would_you_like_more_reactions(Girl, Action_type):
    $ Girl.change_face("sexy", blushing = 1, brows = "sad")

    call would_you_like_more_lines(Girl, Action_type)

    return

label end_of_action_reactions(Girl, Action_type):
    $ Girl.change_face("bemused", blushing = 0)

    call end_of_action_lines(Girl, Action_type)
