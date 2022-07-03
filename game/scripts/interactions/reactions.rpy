label forced_but_not_unwelcome_reactions(Girl, action):
    $ Girl.change_face("sad")

    call forced_but_not_unwelcome_changes_A(Girl, action)
    call forced_but_not_unwelcome_lines(Girl, action)
    call forced_but_not_unwelcome_changes_B(Girl, action)

    return

label forced_action_rejected_reactions(Girl, action):
    if action == "masturbation":
        $ Girl.change_face("angry", 1)

    call forced_action_rejected_lines(Girl, action)
    call forced_action_rejected_changes(Girl, action)

    return

label otherwise_rejected_reactions(Girl, action):
    if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "fondle_ass", "handjob", "blowjob", "sex"]:
        $ Girl.change_face("sexy")
        $ Girl.mouth = "sad"
    elif action in ["eat_pussy", "finger_ass", "eat_ass", "footjob", "titjob", "dildo_pussy", "dildo_ass", "anal", "hotdog"]:
        $ Girl.change_face("surprised")
    elif action in ["masturbation"]:
        $ Girl.change_face("normal", 1)

    call otherwise_not_interested_lines(Girl, action)

    $ Girl.change_face()

    return

label taboo_action_rejected_reactions(Girl, action):
    $ Girl.change_face("angry", 1)

    call taboo_action_rejected_lines(Girl, action)
    call taboo_action_rejected_changes(Girl, action)

    return

label forced_rejected_reactions(Girl, action):
    call forced_rejected_changes(Girl, action)

    $ Girl.change_face("angry", 1)

    if action in ["fondle_thighs", "fondle_breasts", "fondle_pussy", "fondle_ass", "finger_ass"]:
        "She slaps your hand away."
    elif action in ["suck_breasts"]:
        "She shoves your head back out."
    elif action in ["eat_pussy", "eat_ass"]:
        "She shoves your head back."
    else:
        "She shoves you back."

    return

label first_action_approval_forced_reactions(Girl, action):
    $ Girl.change_face("sad")
    call change_Girl_stat(Girl, "love", 70, -3, 1)
    call change_Girl_stat(Girl, "love", 20, -2, 1)

    return

label first_action_approval_mostly_love_reactions(Girl, action):
    $ Girl.change_face("sexy")
    $ Girl.brows = "sad"
    $ Girl.mouth = "smile"

    call first_action_approval_mostly_love_lines(Girl, action)

    return

label first_action_approval_mostly_obedience_reactions(Girl, action):
    if action in ["masturbation", "handjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
        $ Girl.change_face("normal")
    elif action in ["footjob"]:
        $ Girl.change_face("normal", 1)

    call first_action_approval_mostly_obedience_lines(Girl, action)

    return

label first_action_approval_addicted_reactions(Girl, action):
    $ Girl.change_face("manic", 1)

    call first_action_approval_addicted_lines(Girl, action)

    return

label first_action_approval_reactions(Girl, action):
    if action in ["masturbation", "handjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
        $ Girl.change_face("sad")
        $ Girl.mouth = "smile"
    elif action in ["footjob"]:
        $ Girl.change_face("lipbite", 1)

    call first_action_approval_lines(Girl, action)

    return

label auto_approved_reactions(Girl, action):
    if action not in ["fondle_thighs", "fondle_breasts"]:
        $ Girl.change_face("surprised", 1)

    call auto_accepted_narrations(Girl, action)

    $ Girl.change_face("sexy")

    call auto_accepted_lines(Girl, action)

    return

label auto_rejected_reactions(Girl, action):
    call auto_rejected_changes(Girl, action)

    if action in ["fondle_thighs", "suck_breasts", "fondle_pussy", "finger_ass", "eat_ass"]:
        $ Girl.change_face("surprised")

        call auto_rejected_lines(Girl, action)
    elif action == "fondle_breasts":
        $ Girl.change_face("surprised")
        $ Girl.brows = "confused"

        call auto_rejected_lines(Girl, action)
    elif action == "finger_pussy":
        $ Girl.change_face("surprised", 2)

        Girl.voice "Oooh!"
        "She slaps your hand back."

        $ Girl.change_face("perplexed", 1)

        call auto_rejected_lines(Girl, action)
    elif action == "eat_pussy":
        $ Girl.change_face("surprised")

        call auto_rejected_lines(Girl, action)

        $ Girl.change_face("perplexed", 1)

        "She pushes your head back away from her."
    elif action == "fondle_ass":
        $ Girl.change_face("surprised")

        call auto_rejected_lines(Girl, action)

        $ Girl.change_face("bemused")
    elif action in dildo_actions or action in sex_actions:
        $ Girl.brows = "angry"

        call what_do_you_think_youre_doing_lines(Girl, action)
        call what_do_you_think_youre_doing_menu(Girl, action)

        if _return == "accepted":
            return "accepted"

    $ Girl.recent_history.append("no_" + action)
    $ Girl.daily_history.append("no_" + action)

    return "rejected"

label pullback_reactions(Girl, action):
    $ Girl.change_face("surprised")
    $ Girl.brows = "sad"

    call pullback_changes(Girl, action)

    $ lines = ["As you pull back, " + Girl.name + " looks a little sad."]

    if action in finger_actions:
        $ lines.append("As your finger slides out, " + Girl.name + " gasps and looks upset.")
        $ lines.append("As your hand pulls out, " + Girl.name + " gasps and looks upset.")

    $ line = renpy.random.choice(lines)

    "[line]"

    return

label recent_action_reactions(Girl, action):
    $ Girl.change_face("sexy", 1)

    call recent_action_lines(Girl, action)

    return

label daily_action_reactions(Girl, action):
    $ Girl.change_face("sexy", 1)

    call daily_action_lines(Girl, action)

    return

label first_time_asking_reactions(Girl, action):
    if action in ["footjob", "masturbation"]:
        $ Girl.change_face("surprised", 1)
        $ Girl.mouth = "kiss"

        call first_time_asking_lines(Girl, action)
    else:
        $ Girl.change_face("confused", 2)

        call first_time_asking_lines(Girl, action)

        $ Girl.blushing = "_blush1"

    if action == "titjob":
        if Girl.Action_counter["blowjob"]:
            $ Girl.mouth = "smile"

            call mouth_not_enough(Girl, action)
        elif Girl.Action_counter["handjob"]:
            $ Girl.mouth = "smile"

            call hand_not_enough(Girl, action)
    elif action == "blowjob":
        if Girl.Action_counter["handjob"]:
            $ Girl.mouth = "smile"

            call hand_not_enough(Girl, action)

    if Girl.forced:
        $ Girl.change_face("sad")

        if action == "masturbation":
            call action_forcefully_approved_lines(Girl, "masturbation")
        else:
            call first_time_forcing_lines(Girl, action)

    return

label anal_insertion_not_loose_done_today_reactions(Girl, action):
    $ Girl.change_face("bemused", 1)

    call anal_insertion_not_loose_done_today_lines(Girl, action)

    return

label starting_to_get_bored_reactions(Girl, action):
    $ Girl.brows = "confused"

    call starting_to_get_bored_lines(Girl, action)

    return

label definitely_bored_now_reactions(Girl, action):
    if action == "kiss":
        $ Girl.brows = "confused"

        call try_something_else_lines(Girl, action)
    else:
        $ Girl.brows = "angry"

        call definitely_bored_now_lines(Girl, action)

    call try_something_else_menu(Girl, action)

    return _return

label unsatisfied_reactions(Girl, action):
    $ Girl.change_face("angry")

    if Girl != JeanX:
        $ Girl.eyes = "side"

    call unsatisfied_lines(Girl, action)

    return

label would_you_like_more_reactions(Girl, action):
    $ Girl.change_face("sexy", 1)
    $ Girl.brows = "sad"

    call would_you_like_more_lines(Girl, action)

    return

label end_of_action_reactions(Girl, action):
    $ Girl.change_face("bemused", 0)

    call end_of_action_lines(Girl, action)
