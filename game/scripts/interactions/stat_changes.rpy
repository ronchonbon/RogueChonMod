label forced_but_not_unwelcome_changes_A(Girl, Action_type):
    if Action_type in ["fondle_thighs", "fondle_breasts", "fondle_ass"]:
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "love", 1)
    elif Action_type in ["suck_breasts", "fondle_pussy", "eat_pussy", "finger_ass", "eat_ass"]:
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "love", 1)
    elif Action_type in job_actions:
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "love", -2)
    elif Action_type in ["masturbation", "dildo_pussy", "dildo_ass", "sex", "anal"]:
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "love", -5)
    elif Action_type in ["hotdog"]:
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "love", -5)

    return

label forced_but_not_unwelcome_changes_B(Girl, Action_type):
    if Action_type == "fondle_thighs":
        call change_Girl_stat(Girl, "obedience", 3)
        call change_Girl_stat(Girl, "inhibition", 2)
    elif Action_type in breast_actions:
        call change_Girl_stat(Girl, "obedience", 2)
        call change_Girl_stat(Girl, "obedience", 4)
        call change_Girl_stat(Girl, "inhibition", 3)
    elif Action_type in ["fondle_pussy", "eat_pussy", "finger_ass", "eat_ass", "handjob", "footjob", "titjob", "blowjob"]:
        call change_Girl_stat(Girl, "obedience", 4)
        call change_Girl_stat(Girl, "inhibition", 1)
        call change_Girl_stat(Girl, "inhibition", 3)
    elif Action_type in ["fondle_ass"]:
        call change_Girl_stat(Girl, "obedience", 3)
        call change_Girl_stat(Girl, "inhibition", 3)
    elif Action_type in ["masturbation", "dildo_pussy", "dildo_ass", "sex", "anal"]:
        call change_Girl_stat(Girl, "obedience", 4)
        call change_Girl_stat(Girl, "inhibition", 1)
        call change_Girl_stat(Girl, "inhibition", 3)
    elif Action_type in ["hotdog"]:
        call change_Girl_stat(Girl, "obedience", 4)
        call change_Girl_stat(Girl, "inhibition", 2)

    return

label forced_action_rejected_changes(Girl, Action_type):
    if Action_type == "masturbation":
        call change_Girl_stat(Girl, "lust", 5)

        if Girl.love > 300:
            call change_Girl_stat(Girl, "love", -2)
    elif Action_type in ["fondle_thighs"]:
        call change_Girl_stat(Girl, "lust", 2)
        call change_Girl_stat(Girl, "obedience", -1)
    elif Action_type in ["hotdog"]:
        call change_Girl_stat(Girl, "lust", 5)

        if Girl.love > 300:
            call change_Girl_stat(Girl, "love", -1)

        call change_Girl_stat(Girl, "obedience", -1)
    else:
        if Action_type in ["fondle_pussy"]:
            call change_Girl_stat(Girl, "lust", 5)
        elif Action_type in ["eat_pussy"]:
            call change_Girl_stat(Girl, "lust", 5)
        elif Action_type in ["fondle_breasts", "suck_breasts", "fondle_ass"]:
            call change_Girl_stat(Girl, "lust", 5)
        elif Action_type in ["finger_ass", "eat_ass"]:
            if approval_check(Girl, 500, "I"):
                call change_Girl_stat(Girl, "lust", 10)
            else:
                call change_Girl_stat(Girl, "lust", 3)
        elif Action_type in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal"]:
            call change_Girl_stat(Girl, "lust", 5)

            if Girl.love > 300:
                call change_Girl_stat(Girl, "love", -2)

        call change_Girl_stat(Girl, "obedience", -2)

    return

label taboo_action_rejected_changes(Girl, Action_type):
    if Action_type == "masturbation":
        call change_Girl_stat(Girl, "lust", 5)
        call change_Girl_stat(Girl, "obedience", -3)
    if Action_type in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
        call change_Girl_stat(Girl, "lust", 5)
        call change_Girl_stat(Girl, "obedience", -3)

    return

label forced_rejected_changes(Girl, Action_type):
    if Action_type in ["fondle_thighs"]:
        call change_Girl_stat(Girl, "love", -8)
    elif Action_type in ["fondle_breasts", "suck_breasts", "fondle_ass", "hotdog"]:
        call change_Girl_stat(Girl, "love", -10)
    elif Action_type in ["fondle_pussy", "eat_pussy", "finger_ass", "eat_ass", "handjob", "footjob", "titjob", "blowjob"]:
        call change_Girl_stat(Girl, "love", -15)
    elif Action_type in ["masturbation", "dildo_pussy", "dildo_ass", "sex", "anal"]:
        call change_Girl_stat(Girl, "love", -20)

    return

label first_action_changes(Girl, Action_type):
    if not Girl.permanent_History[action]:
        if Action_type == "fondle_thighs":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", -10)
                call change_Girl_stat(Girl, "obedience", 15)
                call change_Girl_stat(Girl, "inhibition", 10)
            else:
                call change_Girl_stat(Girl, "love", 5)
                call change_Girl_stat(Girl, "obedience", 10)
                call change_Girl_stat(Girl, "inhibition", 15)
        elif Action_type == "fondle_breasts":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", -20)
                call change_Girl_stat(Girl, "obedience", 25)
                call change_Girl_stat(Girl, "inhibition", 15)
            else:
                call change_Girl_stat(Girl, "love", 10)
                call change_Girl_stat(Girl, "obedience", 5)
                call change_Girl_stat(Girl, "inhibition", 15)
        elif Action_type == "suck_breasts":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", -25)
                call change_Girl_stat(Girl, "obedience", 25)
                call change_Girl_stat(Girl, "inhibition", 17)
            else:
                call change_Girl_stat(Girl, "love", 10)
                call change_Girl_stat(Girl, "obedience", 10)
                call change_Girl_stat(Girl, "inhibition", 15)
        elif Action_type == "fondle_pussy":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", -50)
                call change_Girl_stat(Girl, "obedience", 35)
                call change_Girl_stat(Girl, "inhibition", 25)
            else:
                call change_Girl_stat(Girl, "love", 10)
                call change_Girl_stat(Girl, "obedience", 10)
                call change_Girl_stat(Girl, "inhibition", 15)
        elif Action_type == "finger_pussy":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", -60)
                call change_Girl_stat(Girl, "obedience", 55)
                call change_Girl_stat(Girl, "inhibition", 35)
            else:
                call change_Girl_stat(Girl, "love", 10)
                call change_Girl_stat(Girl, "obedience", 20)
                call change_Girl_stat(Girl, "inhibition", 25)
        if Action_type == "eat_pussy":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", -30)
                call change_Girl_stat(Girl, "obedience", 35)
                call change_Girl_stat(Girl, "inhibition", 75)
            else:
                call change_Girl_stat(Girl, "love", 35)
                call change_Girl_stat(Girl, "obedience", 15)
                call change_Girl_stat(Girl, "inhibition", 35)
        elif Action_type == "fondle_ass":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", -20)
                call change_Girl_stat(Girl, "obedience", 20)
                call change_Girl_stat(Girl, "inhibition", 15)
            else:
                call change_Girl_stat(Girl, "love", 10)
                call change_Girl_stat(Girl, "obedience", 12)
                call change_Girl_stat(Girl, "inhibition", 20)
        elif Action_type == "finger_ass":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", -50)
                call change_Girl_stat(Girl, "obedience", 60)
                call change_Girl_stat(Girl, "inhibition", 35)
            else:
                call change_Girl_stat(Girl, "love", 10)
                call change_Girl_stat(Girl, "obedience", 20)
                call change_Girl_stat(Girl, "inhibition", 25)
        elif Action_type == "eat_ass":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", -30)
                call change_Girl_stat(Girl, "obedience", 40)
                call change_Girl_stat(Girl, "inhibition", 80)
            else:
                call change_Girl_stat(Girl, "love", 35)
                call change_Girl_stat(Girl, "obedience", 25)
                call change_Girl_stat(Girl, "inhibition", 55)
        elif Action_type == "handjob":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", -20)
                call change_Girl_stat(Girl, "obedience", 25)
                call change_Girl_stat(Girl, "inhibition", 30)
            else:
                call change_Girl_stat(Girl, "love", 5)
                call change_Girl_stat(Girl, "obedience", 20)
                call change_Girl_stat(Girl, "inhibition", 20)
        elif Action_type == "footjob":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", -20)
                call change_Girl_stat(Girl, "obedience", 25)
                call change_Girl_stat(Girl, "inhibition", 30)
            else:
                call change_Girl_stat(Girl, "love", 5)
                call change_Girl_stat(Girl, "obedience", 20)
                call change_Girl_stat(Girl, "inhibition", 20)
        elif Action_type == "titjob":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", -25)
                call change_Girl_stat(Girl, "obedience", 30)
                call change_Girl_stat(Girl, "inhibition", 35)
            else:
                call change_Girl_stat(Girl, "love", 5)
                call change_Girl_stat(Girl, "obedience", 25)
                call change_Girl_stat(Girl, "inhibition", 30)
        elif Action_type == "blowjob":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", -70)
                call change_Girl_stat(Girl, "obedience", 45)
                call change_Girl_stat(Girl, "inhibition", 60)
            else:
                call change_Girl_stat(Girl, "love", 5)
                call change_Girl_stat(Girl, "obedience", 35)
                call change_Girl_stat(Girl, "inhibition", 40)
        elif Action_type == "dildo_pussy":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", -75)
                call change_Girl_stat(Girl, "obedience", 60)
                call change_Girl_stat(Girl, "inhibition", 35)
            else:
                call change_Girl_stat(Girl, "love", 10)
                call change_Girl_stat(Girl, "obedience", 20)
                call change_Girl_stat(Girl, "inhibition", 45)
        elif Action_type == "dildo_ass":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", -75)
                call change_Girl_stat(Girl, "obedience", 60)
                call change_Girl_stat(Girl, "inhibition", 35)
            else:
                call change_Girl_stat(Girl, "love", 10)
                call change_Girl_stat(Girl, "obedience", 20)
                call change_Girl_stat(Girl, "inhibition", 45)
        elif Action_type == "sex":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", -150)
                call change_Girl_stat(Girl, "obedience", 60)
                call change_Girl_stat(Girl, "inhibition", 50)
            else:
                call change_Girl_stat(Girl, "love", 30)
                call change_Girl_stat(Girl, "obedience", 30)
                call change_Girl_stat(Girl, "inhibition", 60)
        elif Action_type == "anal":
            if not Girl.permanent_History["anal"]:
                if Girl.forced:
                    call change_Girl_stat(Girl, "love", -150)
                    call change_Girl_stat(Girl, "obedience", 70)
                    call change_Girl_stat(Girl, "inhibition", 40)
                else:
                    call change_Girl_stat(Girl, "love", 10)
                    call change_Girl_stat(Girl, "obedience", 30)
                    call change_Girl_stat(Girl, "inhibition", 70)
            elif not Girl.used_to_anal:
                if Girl.forced:
                    call change_Girl_stat(Girl, "love", -20)
                    call change_Girl_stat(Girl, "obedience", 10)
                    call change_Girl_stat(Girl, "inhibition", 5)
                else:
                    call change_Girl_stat(Girl, "obedience", 7)
                    call change_Girl_stat(Girl, "inhibition", 5)
        elif Action_type == "hotdog":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", -5)
                call change_Girl_stat(Girl, "obedience", 20)
                call change_Girl_stat(Girl, "inhibition", 10)
            else:
                call change_Girl_stat(Girl, "love", 20)
                call change_Girl_stat(Girl, "obedience", 20)
                call change_Girl_stat(Girl, "inhibition", 20)

    return

label first_action_approval_forced_changes(Girl, Action_type):
    if Action_type in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "anal", "hotdog"]:
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "love", 1)
    elif Action_type in ["sex"]:
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "love", 1)

    return

label auto_approved_changes(Girl, Action_type):
    if Action_type == "fondle_thighs":
        call change_Girl_stat(Girl, "obedience", 1)
        call change_Girl_stat(Girl, "inhibition", 2)
    elif Action_type == "fondle_breasts":
        call change_Girl_stat(Girl, "obedience", 1)
        call change_Girl_stat(Girl, "obedience", 2)
        call change_Girl_stat(Girl, "inhibition", 3)
        call change_Girl_stat(Girl, "inhibition", 2)
    elif Action_type == "suck_breasts":
        call change_Girl_stat(Girl, "obedience", 1)
        call change_Girl_stat(Girl, "obedience", 2)
        call change_Girl_stat(Girl, "inhibition", 3)
        call change_Girl_stat(Girl, "inhibition", 2)
    elif Action_type == "fondle_pussy":
        call change_Girl_stat(Girl, "obedience", 1)
        call change_Girl_stat(Girl, "obedience", 2)
        call change_Girl_stat(Girl, "inhibition", 3)
        call change_Girl_stat(Girl, "inhibition", 2)
    elif Action_type == "finger_pussy":
        call change_Girl_stat(Girl, "obedience", 1)
        call change_Girl_stat(Girl, "obedience", 2)
        call change_Girl_stat(Girl, "inhibition", 3)
        call change_Girl_stat(Girl, "inhibition", 2)
    elif Action_type == "eat_pussy":
        call change_Girl_stat(Girl, "obedience", 1)
        call change_Girl_stat(Girl, "obedience", 2)
        call change_Girl_stat(Girl, "inhibition", 3)
        call change_Girl_stat(Girl, "inhibition", 2)
    elif Action_type == "fondle_ass":
        call change_Girl_stat(Girl, "obedience", 2)
        call change_Girl_stat(Girl, "inhibition", 2)
    elif Action_type == "finger_ass":
        call change_Girl_stat(Girl, "obedience", 2)
        call change_Girl_stat(Girl, "obedience", 2)
        call change_Girl_stat(Girl, "inhibition", 2)
        call change_Girl_stat(Girl, "inhibition", 2)
    elif Action_type == "eat_ass":
        call change_Girl_stat(Girl, "obedience", 1)
        call change_Girl_stat(Girl, "inhibition", 3)
        call change_Girl_stat(Girl, "inhibition", 2)
    elif Action_type in dildo_actions or Action_type in sex_actions:
        call change_Girl_stat(Girl, "obedience", 3)
        call change_Girl_stat(Girl, "inhibition", 3)
        call change_Girl_stat(Girl, "inhibition", 1)

    return

label auto_rejected_changes(Girl, Action_type):
    if Action_type in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy"]:
        call change_Girl_stat(Girl, "obedience", -2)
    elif Action_type in ["finger_pussy", "eat_pussy", "finger_ass", "eat_ass"]:
        call change_Girl_stat(Girl, "love", -2)
        call change_Girl_stat(Girl, "obedience", -3)
    elif Action_type == "fondle_ass":
        call change_Girl_stat(Girl, "obedience", -3)

    return

label pullback_changes(Girl, Action_type):
    if Action_type in ["fondle_pussy", "fondle_ass"]:
        if Girl.lust > 80:
            call change_Girl_stat(Girl, "love", -4)
    elif Action_type in ["fondle_thighs", "finger_ass", "eat_ass"]:
        if Girl.lust > 60:
            call change_Girl_stat(Girl, "love", -3)

    call change_Girl_stat(Girl, "obedience", 1)
    call change_Girl_stat(Girl, "obedience", 2)

    return

label action_specific_changes(Girl, Action_type):
    if Action_type == "sex":
        call change_Girl_stat(Girl, "inhibition", 2)
        call change_Girl_stat(Girl, "inhibition", 1)
    elif Action_type == "anal":
        call change_Girl_stat(Girl, "inhibition", 3)
        call change_Girl_stat(Girl, "inhibition", 1)
    elif Action_type == "hotdog":
        call change_Girl_stat(Girl, "inhibition", 1)
        call change_Girl_stat(Girl, "inhibition", 1)

    return

label forced_action_accepted_changes(Girl, Action_type):
    if Action_type in ["fondle_thighs"]:
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "obedience", 1)
        call change_Girl_stat(Girl, "inhibition", 1)
    elif Action_type in ["fondle_breasts", "suck_breasts", "fondle_pussy"]:
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "obedience", 1)
        call change_Girl_stat(Girl, "inhibition", 1)
    elif Action_type in ["finger_pussy", "eat_pussy", "finger_ass"]:
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "obedience", 1)
        call change_Girl_stat(Girl, "inhibition", 1)
    elif Action_type in ["fondle_ass"]:
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "obedience", 2)
        call change_Girl_stat(Girl, "inhibition", 2)
    elif Action_type in ["eat_ass"]:
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "obedience", 2)
        call change_Girl_stat(Girl, "inhibition", 2)
    elif Action_type in ["masturbation", "handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal"]:
        call change_Girl_stat(Girl, "inhibition", 1)
        call change_Girl_stat(Girl, "obedience", 1)
    elif Action_type in ["hotdog"]:
        call change_Girl_stat(Girl, "inhibition", 1)
        call change_Girl_stat(Girl, "obedience", 1)

    return

label not_forced_action_accepted_changes(Girl, Action_type):
    if Action_type in ["finger_pussy", "masturbation"]:
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "inhibition", 3)
    elif Action_type in ["eat_pussy", "finger_ass"]:
        $ Girl.eyes = "closed"
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "inhibition", 3)
        call change_Girl_stat(Girl, "lust", 3)
    elif Action_type in ["eat_ass"]:
        $ Girl.eyes = "closed"
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "inhibition", 2)
        call change_Girl_stat(Girl, "lust", 3)
    elif Action_type in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal"]:
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "inhibition", 3)
    elif Action_type in ["hotdog"]:
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "inhibition", 2)

    return

label action_accepted_changes(Girl, Action_type):
    if Action_type in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy"]:
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "inhibition", 3)
    elif Action_type in ["masturbation", "finger_pussy", "eat_pussy", "finger_ass"]:
        call change_Girl_stat(Girl, "obedience", 1)
        call change_Girl_stat(Girl, "obedience", 1)
        call change_Girl_stat(Girl, "inhibition", 2)
    elif Action_type in ["fondle_ass"]:
        call change_Girl_stat(Girl, "lust", 3)
        call change_Girl_stat(Girl, "obedience", 1)
        call change_Girl_stat(Girl, "inhibition", 1)
    elif Action_type in ["eat_ass"]:
        call change_Girl_stat(Girl, "obedience", 1)
        call change_Girl_stat(Girl, "obedience", 1)
        call change_Girl_stat(Girl, "inhibition", 2)
    elif Action_type in ["handjob", "footjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
        call change_Girl_stat(Girl, "obedience", 1)
        call change_Girl_stat(Girl, "obedience", 1)
        call change_Girl_stat(Girl, "inhibition", 2)
    elif Action_type in ["titjob", "blowjob"]:
        call change_Girl_stat(Girl, "obedience", 1)
        call change_Girl_stat(Girl, "obedience", 1)
        call change_Girl_stat(Girl, "inhibition", 2)
