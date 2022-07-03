label forced_but_not_unwelcome_changes_A(Girl, action):
    if action in ["fondle_thighs", "fondle_breasts", "fondle_ass"]:
        call change_Girl_stat(Girl, "love", 70, -3, 1)
        call change_Girl_stat(Girl, "love", 20, -1, 1)
    elif action in ["suck_breasts", "fondle_pussy", "eat_pussy", "finger_ass", "eat_ass"]:
        call change_Girl_stat(Girl, "love", 70, -5, 1)
        call change_Girl_stat(Girl, "love", 20, -2, 1)
    elif action in job_actions:
        call change_Girl_stat(Girl, "love", 70, -5, 1)
        call change_Girl_stat(Girl, "love", 200, -2)
    elif action in ["masturbation", "dildo_pussy", "dildo_ass", "sex", "anal"]:
        call change_Girl_stat(Girl, "love", 70, -5, 1)
        call change_Girl_stat(Girl, "love", 200, -5)
    elif action in ["hotdog"]:
        call change_Girl_stat(Girl, "love", 70, -2, 1)
        call change_Girl_stat(Girl, "love", 200, -5)

    return

label forced_but_not_unwelcome_changes_B(Girl, action):
    if action == "fondle_thighs":
        call change_Girl_stat(Girl, "obedience", 50, 3)
        call change_Girl_stat(Girl, "inhibition", 60, 2)
    elif action in breast_actions:
        call change_Girl_stat(Girl, "obedience", 90, 2)
        call change_Girl_stat(Girl, "obedience", 50, 4)
        call change_Girl_stat(Girl, "inhibition", 60, 3)
    elif action in ["fondle_pussy", "eat_pussy", "finger_ass", "eat_ass", "handjob", "footjob", "titjob", "blowjob"]:
        call change_Girl_stat(Girl, "obedience", 50, 4)
        call change_Girl_stat(Girl, "inhibition", 80, 1)
        call change_Girl_stat(Girl, "inhibition", 60, 3)
    elif action in ["fondle_ass"]:
        call change_Girl_stat(Girl, "obedience", 50, 3)
        call change_Girl_stat(Girl, "inhibition", 60, 3)
    elif action in ["masturbation", "dildo_pussy", "dildo_ass", "sex", "anal"]:
        call change_Girl_stat(Girl, "obedience", 80, 4)
        call change_Girl_stat(Girl, "inhibition", 80, 1)
        call change_Girl_stat(Girl, "inhibition", 60, 3)
    elif action in ["hotdog"]:
        call change_Girl_stat(Girl, "obedience", 80, 4)
        call change_Girl_stat(Girl, "inhibition", 60, 2)

    return

label forced_action_rejected_changes(Girl, action):
    if action == "masturbation":
        call change_Girl_stat(Girl, "lust", 90, 5)

        if Girl.love > 300:
            call change_Girl_stat(Girl, "love", 70, -2)
    elif action in ["fondle_thighs"]:
        call change_Girl_stat(Girl, "lust", 50, 2)
        call change_Girl_stat(Girl, "obedience", 50, -1)
    elif action in ["hotdog"]:
        call change_Girl_stat(Girl, "lust", 200, 5)

        if Girl.love > 300:
            call change_Girl_stat(Girl, "love", 70, -1)

        call change_Girl_stat(Girl, "obedience", 50, -1)
    else:
        if action in ["fondle_pussy"]:
            call change_Girl_stat(Girl, "lust", 70, 5)
        elif action in ["eat_pussy"]:
            call change_Girl_stat(Girl, "lust", 80, 5)
        elif action in ["fondle_breasts", "suck_breasts", "fondle_ass"]:
            call change_Girl_stat(Girl, "lust", 60, 5)
        elif action in ["finger_ass", "eat_ass"]:
            if approval_check(Girl, 500, "I"):
                call change_Girl_stat(Girl, "lust", 80, 10)
            else:
                call change_Girl_stat(Girl, "lust", 50, 3)
        elif action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal"]:
            call change_Girl_stat(Girl, "lust", 200, 5)

            if Girl.love > 300:
                call change_Girl_stat(Girl, "love", 70, -2)

        call change_Girl_stat(Girl, "obedience", 50, -2)

    return

label taboo_action_rejected_changes(Girl, action):
    if action == "masturbation":
        call change_Girl_stat(Girl, "lust", 90, 5)
        call change_Girl_stat(Girl, "obedience", 50, -3)
    if action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
        call change_Girl_stat(Girl, "lust", 200, 5)
        call change_Girl_stat(Girl, "obedience", 50, -3)

    return

label forced_rejected_changes(Girl, action):
    if action in ["fondle_thighs"]:
        call change_Girl_stat(Girl, "love", 200, -8)
    elif action in ["fondle_breasts", "suck_breasts", "fondle_ass", "hotdog"]:
        call change_Girl_stat(Girl, "love", 200, -10)
    elif action in ["fondle_pussy", "eat_pussy", "finger_ass", "eat_ass", "handjob", "footjob", "titjob", "blowjob"]:
        call change_Girl_stat(Girl, "love", 200, -15)
    elif action in ["masturbation", "dildo_pussy", "dildo_ass", "sex", "anal"]:
        call change_Girl_stat(Girl, "love", 200, -20)

    return

label first_action_changes(Girl, action):
    if not Girl.Action_counter[action]:
        if action == "fondle_thighs":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", 90, -10)
                call change_Girl_stat(Girl, "obedience", 70, 15)
                call change_Girl_stat(Girl, "inhibition", 80, 10)
            else:
                call change_Girl_stat(Girl, "love", 90, 5)
                call change_Girl_stat(Girl, "obedience", 70, 10)
                call change_Girl_stat(Girl, "inhibition", 80, 15)
        elif action == "fondle_breasts":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", 90, -20)
                call change_Girl_stat(Girl, "obedience", 70, 25)
                call change_Girl_stat(Girl, "inhibition", 80, 15)
            else:
                call change_Girl_stat(Girl, "love", 90, 10)
                call change_Girl_stat(Girl, "obedience", 70, 5)
                call change_Girl_stat(Girl, "inhibition", 80, 15)
        elif action == "suck_breasts":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", 90, -25)
                call change_Girl_stat(Girl, "obedience", 70, 25)
                call change_Girl_stat(Girl, "inhibition", 80, 17)
            else:
                call change_Girl_stat(Girl, "love", 90, 10)
                call change_Girl_stat(Girl, "obedience", 70, 10)
                call change_Girl_stat(Girl, "inhibition", 80, 15)
        elif action == "fondle_pussy":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", 90, -50)
                call change_Girl_stat(Girl, "obedience", 70, 35)
                call change_Girl_stat(Girl, "inhibition", 80, 25)
            else:
                call change_Girl_stat(Girl, "love", 90, 10)
                call change_Girl_stat(Girl, "obedience", 70, 10)
                call change_Girl_stat(Girl, "inhibition", 80, 15)
        elif action == "finger_pussy":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", 90, -60)
                call change_Girl_stat(Girl, "obedience", 70, 55)
                call change_Girl_stat(Girl, "inhibition", 80, 35)
            else:
                call change_Girl_stat(Girl, "love", 90, 10)
                call change_Girl_stat(Girl, "obedience", 70, 20)
                call change_Girl_stat(Girl, "inhibition", 80, 25)
        if action == "eat_pussy":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", 90, -30)
                call change_Girl_stat(Girl, "obedience", 70, 35)
                call change_Girl_stat(Girl, "inhibition", 80, 75)
            else:
                call change_Girl_stat(Girl, "love", 90, 35)
                call change_Girl_stat(Girl, "obedience", 70, 15)
                call change_Girl_stat(Girl, "inhibition", 80, 35)
        elif action == "fondle_ass":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", 90, -20)
                call change_Girl_stat(Girl, "obedience", 70, 20)
                call change_Girl_stat(Girl, "inhibition", 80, 15)
            else:
                call change_Girl_stat(Girl, "love", 90, 10)
                call change_Girl_stat(Girl, "obedience", 70, 12)
                call change_Girl_stat(Girl, "inhibition", 80, 20)
        elif action == "finger_ass":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", 90, -50)
                call change_Girl_stat(Girl, "obedience", 70, 60)
                call change_Girl_stat(Girl, "inhibition", 80, 35)
            else:
                call change_Girl_stat(Girl, "love", 90, 10)
                call change_Girl_stat(Girl, "obedience", 70, 20)
                call change_Girl_stat(Girl, "inhibition", 80, 25)
        elif action == "eat_ass":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", 90, -30)
                call change_Girl_stat(Girl, "obedience", 70, 40)
                call change_Girl_stat(Girl, "inhibition", 80, 80)
            else:
                call change_Girl_stat(Girl, "love", 90, 35)
                call change_Girl_stat(Girl, "obedience", 70, 25)
                call change_Girl_stat(Girl, "inhibition", 80, 55)
        elif action == "handjob":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", 90, -20)
                call change_Girl_stat(Girl, "obedience", 70, 25)
                call change_Girl_stat(Girl, "inhibition", 80, 30)
            else:
                call change_Girl_stat(Girl, "love", 90, 5)
                call change_Girl_stat(Girl, "obedience", 70, 20)
                call change_Girl_stat(Girl, "inhibition", 80, 20)
        elif action == "footjob":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", 90, -20)
                call change_Girl_stat(Girl, "obedience", 70, 25)
                call change_Girl_stat(Girl, "inhibition", 80, 30)
            else:
                call change_Girl_stat(Girl, "love", 90, 5)
                call change_Girl_stat(Girl, "obedience", 70, 20)
                call change_Girl_stat(Girl, "inhibition", 80, 20)
        elif action == "titjob":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", 90, -25)
                call change_Girl_stat(Girl, "obedience", 70, 30)
                call change_Girl_stat(Girl, "inhibition", 80, 35)
            else:
                call change_Girl_stat(Girl, "love", 90, 5)
                call change_Girl_stat(Girl, "obedience", 70, 25)
                call change_Girl_stat(Girl, "inhibition", 80, 30)
        elif action == "blowjob":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", 90, -70)
                call change_Girl_stat(Girl, "obedience", 70, 45)
                call change_Girl_stat(Girl, "inhibition", 80, 60)
            else:
                call change_Girl_stat(Girl, "love", 90, 5)
                call change_Girl_stat(Girl, "obedience", 70, 35)
                call change_Girl_stat(Girl, "inhibition", 80, 40)
        elif action == "dildo_pussy":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", 90, -75)
                call change_Girl_stat(Girl, "obedience", 70, 60)
                call change_Girl_stat(Girl, "inhibition", 80, 35)
            else:
                call change_Girl_stat(Girl, "love", 90, 10)
                call change_Girl_stat(Girl, "obedience", 70, 20)
                call change_Girl_stat(Girl, "inhibition", 80, 45)
        elif action == "dildo_ass":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", 90, -75)
                call change_Girl_stat(Girl, "obedience", 70, 60)
                call change_Girl_stat(Girl, "inhibition", 80, 35)
            else:
                call change_Girl_stat(Girl, "love", 90, 10)
                call change_Girl_stat(Girl, "obedience", 70, 20)
                call change_Girl_stat(Girl, "inhibition", 80, 45)
        elif action == "sex":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", 90, -150)
                call change_Girl_stat(Girl, "obedience", 70, 60)
                call change_Girl_stat(Girl, "inhibition", 80, 50)
            else:
                call change_Girl_stat(Girl, "love", 90, 30)
                call change_Girl_stat(Girl, "obedience", 70, 30)
                call change_Girl_stat(Girl, "inhibition", 80, 60)
        elif action == "anal":
            if not Girl.Action_counter["anal"]:
                if Girl.forced:
                    call change_Girl_stat(Girl, "love", 90, -150)
                    call change_Girl_stat(Girl, "obedience", 70, 70)
                    call change_Girl_stat(Girl, "inhibition", 80, 40)
                else:
                    call change_Girl_stat(Girl, "love", 90, 10)
                    call change_Girl_stat(Girl, "obedience", 70, 30)
                    call change_Girl_stat(Girl, "inhibition", 80, 70)
            elif not Girl.used_to_anal:
                if Girl.forced:
                    call change_Girl_stat(Girl, "love", 90, -20)
                    call change_Girl_stat(Girl, "obedience", 70, 10)
                    call change_Girl_stat(Girl, "inhibition", 80, 5)
                else:
                    call change_Girl_stat(Girl, "obedience", 70, 7)
                    call change_Girl_stat(Girl, "inhibition", 80, 5)
        elif action == "hotdog":
            if Girl.forced:
                call change_Girl_stat(Girl, "love", 90, -5)
                call change_Girl_stat(Girl, "obedience", 70, 20)
                call change_Girl_stat(Girl, "inhibition", 80, 10)
            else:
                call change_Girl_stat(Girl, "love", 90, 20)
                call change_Girl_stat(Girl, "obedience", 70, 20)
                call change_Girl_stat(Girl, "inhibition", 80, 20)

    return

label first_action_approval_forced_changes(Girl, action):
    if action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "anal", "hotdog"]:
        call change_Girl_stat(Girl, "love", 70, -3, 1)
        call change_Girl_stat(Girl, "love", 20, -2, 1)
    elif action in ["sex"]:
        call change_Girl_stat(Girl, "love", 70, -30, 1)
        call change_Girl_stat(Girl, "love", 20, -20, 1)

    return

label auto_approved_changes(Girl, action):
    if action == "fondle_thighs":
        call change_Girl_stat(Girl, "obedience", 50, 1)
        call change_Girl_stat(Girl, "inhibition", 30, 2)
    elif action == "fondle_breasts":
        call change_Girl_stat(Girl, "obedience", 90, 1)
        call change_Girl_stat(Girl, "obedience", 70, 2)
        call change_Girl_stat(Girl, "inhibition", 70, 3)
        call change_Girl_stat(Girl, "inhibition", 30, 2)
    elif action == "suck_breasts":
        call change_Girl_stat(Girl, "obedience", 90, 1)
        call change_Girl_stat(Girl, "obedience", 70, 2)
        call change_Girl_stat(Girl, "inhibition", 70, 3)
        call change_Girl_stat(Girl, "inhibition", 30, 2)
    elif action == "fondle_pussy":
        call change_Girl_stat(Girl, "obedience", 90, 1)
        call change_Girl_stat(Girl, "obedience", 70, 2)
        call change_Girl_stat(Girl, "inhibition", 70, 3)
        call change_Girl_stat(Girl, "inhibition", 30, 2)
    elif action == "finger_pussy":
        call change_Girl_stat(Girl, "obedience", 90, 1)
        call change_Girl_stat(Girl, "obedience", 70, 2)
        call change_Girl_stat(Girl, "inhibition", 70, 3)
        call change_Girl_stat(Girl, "inhibition", 30, 2)
    elif action == "eat_pussy":
        call change_Girl_stat(Girl, "obedience", 90, 1)
        call change_Girl_stat(Girl, "obedience", 70, 2)
        call change_Girl_stat(Girl, "inhibition", 70, 3)
        call change_Girl_stat(Girl, "inhibition", 30, 2)
    elif action == "fondle_ass":
        call change_Girl_stat(Girl, "obedience", 70, 2)
        call change_Girl_stat(Girl, "inhibition", 40, 2)
    elif action == "finger_ass":
        call change_Girl_stat(Girl, "obedience", 90, 2)
        call change_Girl_stat(Girl, "obedience", 70, 2)
        call change_Girl_stat(Girl, "inhibition", 80, 2)
        call change_Girl_stat(Girl, "inhibition", 30, 2)
    elif action == "eat_ass":
        call change_Girl_stat(Girl, "obedience", 90, 1)
        call change_Girl_stat(Girl, "inhibition", 80, 3)
        call change_Girl_stat(Girl, "inhibition", 40, 2)
    elif action in dildo_actions or action in sex_actions:
        call change_Girl_stat(Girl, "obedience", 70, 3)
        call change_Girl_stat(Girl, "inhibition", 50, 3)
        call change_Girl_stat(Girl, "inhibition", 70, 1)

    return

label auto_rejected_changes(Girl, action):
    if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy"]:
        call change_Girl_stat(Girl, "obedience", 50, -2)
    elif action in ["finger_pussy", "eat_pussy", "finger_ass", "eat_ass"]:
        call change_Girl_stat(Girl, "love", 80, -2)
        call change_Girl_stat(Girl, "obedience", 50, -3)
    elif action == "fondle_ass":
        call change_Girl_stat(Girl, "obedience", 50, -3)

    return

label pullback_changes(Girl, action):
    if action in ["fondle_pussy", "fondle_ass"]:
        if Girl.lust > 80:
            call change_Girl_stat(Girl, "love", 70, -4)
    elif action in ["fondle_thighs", "finger_ass", "eat_ass"]:
        if Girl.lust > 60:
            call change_Girl_stat(Girl, "love", 70, -3)

    call change_Girl_stat(Girl, "obedience", 90, 1)
    call change_Girl_stat(Girl, "obedience", 70, 2)

    return

label action_specific_changes(Girl, action):
    if action == "sex":
        call change_Girl_stat(Girl, "inhibition", 30, 2)
        call change_Girl_stat(Girl, "inhibition", 70, 1)
    elif action == "anal":
        call change_Girl_stat(Girl, "inhibition", 30, 3)
        call change_Girl_stat(Girl, "inhibition", 70, 1)
    elif action == "hotdog":
        call change_Girl_stat(Girl, "inhibition", 30, 1)
        call change_Girl_stat(Girl, "inhibition", 70, 1)

    return

label forced_action_accepted_changes(Girl, action):
    if action in ["fondle_thighs"]:
        call change_Girl_stat(Girl, "love", 70, -3, 1)
        call change_Girl_stat(Girl, "obedience", 90, 1)
        call change_Girl_stat(Girl, "inhibition", 60, 1)
    elif action in ["fondle_breasts", "suck_breasts", "fondle_pussy"]:
        call change_Girl_stat(Girl, "love", 70, -3, 1)
        call change_Girl_stat(Girl, "love", 20, -2, 1)
        call change_Girl_stat(Girl, "obedience", 90, 1)
        call change_Girl_stat(Girl, "inhibition", 60, 1)
    elif action in ["finger_pussy", "eat_pussy", "finger_ass"]:
        call change_Girl_stat(Girl, "love", 70, -3, 1)
        call change_Girl_stat(Girl, "love", 20, -2, 1)
        call change_Girl_stat(Girl, "obedience", 90, 1)
        call change_Girl_stat(Girl, "inhibition", 60, 1)
    elif action in ["fondle_ass"]:
        call change_Girl_stat(Girl, "love", 70, -2, 1)
        call change_Girl_stat(Girl, "obedience", 90, 2)
        call change_Girl_stat(Girl, "inhibition", 60, 2)
    elif action in ["eat_ass"]:
        call change_Girl_stat(Girl, "love", 70, -3, 1)
        call change_Girl_stat(Girl, "love", 20, -2, 1)
        call change_Girl_stat(Girl, "obedience", 90, 2)
        call change_Girl_stat(Girl, "inhibition", 60, 2)
    elif action in ["masturbation", "handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal"]:
        call change_Girl_stat(Girl, "inhibition", 60, 1)
        call change_Girl_stat(Girl, "obedience", 90, 1)
    elif action in ["hotdog"]:
        call change_Girl_stat(Girl, "inhibition", 60, 1)
        call change_Girl_stat(Girl, "obedience", 80, 1)

    return

label not_forced_action_accepted_changes(Girl, action):
    if action in ["finger_pussy", "masturbation"]:
        call change_Girl_stat(Girl, "love", 90, 1)
        call change_Girl_stat(Girl, "inhibition", 50, 3)
    elif action in ["eat_pussy", "finger_ass"]:
        $ Girl.eyes = "closed"
        call change_Girl_stat(Girl, "love", 90, 1)
        call change_Girl_stat(Girl, "inhibition", 50, 3)
        call change_Girl_stat(Girl, "lust", 200, 3)
    elif action in ["eat_ass"]:
        $ Girl.eyes = "closed"
        call change_Girl_stat(Girl, "love", 90, 1)
        call change_Girl_stat(Girl, "inhibition", 60, 2)
        call change_Girl_stat(Girl, "lust", 200, 3)
    elif action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal"]:
        call change_Girl_stat(Girl, "love", 90, 1)
        call change_Girl_stat(Girl, "inhibition", 50, 3)
    elif action in ["hotdog"]:
        call change_Girl_stat(Girl, "love", 80, 1)
        call change_Girl_stat(Girl, "inhibition", 50, 2)

    return

label action_accepted_changes(Girl, action):
    if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy"]:
        call change_Girl_stat(Girl, "love", 90, 1)
        call change_Girl_stat(Girl, "inhibition", 50, 3)
    elif action in ["masturbation", "finger_pussy", "eat_pussy", "finger_ass"]:
        call change_Girl_stat(Girl, "obedience", 20, 1)
        call change_Girl_stat(Girl, "obedience", 60, 1)
        call change_Girl_stat(Girl, "inhibition", 70, 2)
    elif action in ["fondle_ass"]:
        call change_Girl_stat(Girl, "lust", 200, 3)
        call change_Girl_stat(Girl, "obedience", 60, 1)
        call change_Girl_stat(Girl, "inhibition", 70, 1)
    elif action in ["eat_ass"]:
        call change_Girl_stat(Girl, "obedience", 20, 1)
        call change_Girl_stat(Girl, "obedience", 60, 1)
        call change_Girl_stat(Girl, "inhibition", 80, 2)
    elif action in ["handjob", "footjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
        call change_Girl_stat(Girl, "obedience", 20, 1)
        call change_Girl_stat(Girl, "obedience", 60, 1)
        call change_Girl_stat(Girl, "inhibition", 70, 2)
    elif action in ["titjob", "blowjob"]:
        call change_Girl_stat(Girl, "obedience", 20, 1)
        call change_Girl_stat(Girl, "obedience", 70, 1)
        call change_Girl_stat(Girl, "inhibition", 80, 2)
