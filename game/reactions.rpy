label forced_but_not_unwelcome_reactions(Girl, action):
    $ Girl.change_face("sad")

    if action in ["fondle_thighs", "fondle_breasts", "fondle_ass"]:
        $ Girl.change_stat("love", 70, -3, 1)
        $ Girl.change_stat("love", 20, -1, 1)
    elif action in ["suck_breasts", "fondle_pussy", "eat_pussy", "finger_ass", "eat_ass"]:
        $ Girl.change_stat("love", 70, -5, 1)
        $ Girl.change_stat("love", 20, -2, 1)
    elif action in job_actions:
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
    elif action in breast_actions:
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

    return

label went_too_far_reactions(Girl, action):
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
            if Approvalcheck(Girl, 500, "I"):
                $ Girl.change_stat("lust", 80, 10)
            else:
                $ Girl.change_stat("lust", 50, 3)
        elif action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal"]:
            $ Girl.change_stat("lust", 200, 5)

            if Girl.love > 300:
                $ Girl.change_stat("love", 70, -2)

        $ Girl.change_stat("obedience", 50, -2)

    return

label anal_insertion_not_loose_done_today_reactions(Girl, action):
    $ Girl.change_face("bemused")

    call anal_insertion_not_loose_done_today_lines(Girl)

    return

label not_happening_reactions(Girl, action):
    if action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "fondle_ass", "handjob", "blowjob", "sex"]:
        $ Girl.change_face("sexy")
        $ Girl.Mouth = "sad"
    elif action in ["eat_pussy", "finger_ass", "eat_ass", "footjob", "titjob", "dildo_pussy", "dildo_ass", "anal", "hotdog"]:
        $ Girl.change_face("surprised")

    call not_happening_lines(Girl)

    $ Girl.change_face()

    return

label action_rejected_taboo_reactions(Girl, action):
    $ Girl.change_face("angry", 1)

    call not_in_public_lines(Girl)

    if action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
        $ Girl.change_stat("lust", 200, 5)
        $ Girl.change_stat("obedience", 50, -3)

    return

label forced_rejected_reactions(Girl, action):
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

    return

label first_action_reactions(Girl, action):
    if not Girl.action_counter[action]:
        if action == "fondle_thighs":
            if Girl.Forced:
                $ Girl.change_stat("love", 90, -10)
                $ Girl.change_stat("obedience", 70, 15)
                $ Girl.change_stat("inhibition", 80, 10)
            else:
                $ Girl.change_stat("love", 90, 5)
                $ Girl.change_stat("obedience", 70, 10)
                $ Girl.change_stat("inhibition", 80, 15)
        elif action == "fondle_breasts":
            if Girl.Forced:
                $ Girl.change_stat("love", 90, -20)
                $ Girl.change_stat("obedience", 70, 25)
                $ Girl.change_stat("inhibition", 80, 15)
            else:
                $ Girl.change_stat("love", 90, 10)
                $ Girl.change_stat("obedience", 70, 5)
                $ Girl.change_stat("inhibition", 80, 15)
        elif action == "suck_breasts":
            if Girl.Forced:
                $ Girl.change_stat("love", 90, -25)
                $ Girl.change_stat("obedience", 70, 25)
                $ Girl.change_stat("inhibition", 80, 17)
            else:
                $ Girl.change_stat("love", 90, 10)
                $ Girl.change_stat("obedience", 70, 10)
                $ Girl.change_stat("inhibition", 80, 15)
        elif action == "fondle_pussy":
            if Girl.Forced:
                $ Girl.change_stat("love", 90, -50)
                $ Girl.change_stat("obedience", 70, 35)
                $ Girl.change_stat("inhibition", 80, 25)
            else:
                $ Girl.change_stat("love", 90, 10)
                $ Girl.change_stat("obedience", 70, 10)
                $ Girl.change_stat("inhibition", 80, 15)
        elif action == "finger_pussy":
            if Girl.Forced:
                $ Girl.change_stat("love", 90, -60)
                $ Girl.change_stat("obedience", 70, 55)
                $ Girl.change_stat("inhibition", 80, 35)
            else:
                $ Girl.change_stat("love", 90, 10)
                $ Girl.change_stat("obedience", 70, 20)
                $ Girl.change_stat("inhibition", 80, 25)
        if action == "eat_pussy":
            if Girl.Forced:
                $ Girl.change_stat("love", 90, -30)
                $ Girl.change_stat("obedience", 70, 35)
                $ Girl.change_stat("inhibition", 80, 75)
            else:
                $ Girl.change_stat("love", 90, 35)
                $ Girl.change_stat("obedience", 70, 15)
                $ Girl.change_stat("inhibition", 80, 35)
        elif action == "fondle_ass":
            if Girl.Forced:
                $ Girl.change_stat("love", 90, -20)
                $ Girl.change_stat("obedience", 70, 20)
                $ Girl.change_stat("inhibition", 80, 15)
            else:
                $ Girl.change_stat("love", 90, 10)
                $ Girl.change_stat("obedience", 70, 12)
                $ Girl.change_stat("inhibition", 80, 20)
        elif action == "finger_ass":
            if Girl.Forced:
                $ Girl.change_stat("love", 90, -50)
                $ Girl.change_stat("obedience", 70, 60)
                $ Girl.change_stat("inhibition", 80, 35)
            else:
                $ Girl.change_stat("love", 90, 10)
                $ Girl.change_stat("obedience", 70, 20)
                $ Girl.change_stat("inhibition", 80, 25)
        elif action == "eat_ass":
            if Girl.Forced:
                $ Girl.change_stat("love", 90, -30)
                $ Girl.change_stat("obedience", 70, 40)
                $ Girl.change_stat("inhibition", 80, 80)
            else:
                $ Girl.change_stat("love", 90, 35)
                $ Girl.change_stat("obedience", 70, 25)
                $ Girl.change_stat("inhibition", 80, 55)
        elif action == "handjob":
            if Girl.Forced:
                $ Girl.change_stat("love", 90, -20)
                $ Girl.change_stat("obedience", 70, 25)
                $ Girl.change_stat("inhibition", 80, 30)
            else:
                $ Girl.change_stat("love", 90, 5)
                $ Girl.change_stat("obedience", 70, 20)
                $ Girl.change_stat("inhibition", 80, 20)
        elif action == "footjob":
            if Girl.Forced:
                $ Girl.change_stat("love", 90, -20)
                $ Girl.change_stat("obedience", 70, 25)
                $ Girl.change_stat("inhibition", 80, 30)
            else:
                $ Girl.change_stat("love", 90, 5)
                $ Girl.change_stat("obedience", 70, 20)
                $ Girl.change_stat("inhibition", 80, 20)
        elif action == "titjob":
            if Girl.Forced:
                $ Girl.change_stat("love", 90, -25)
                $ Girl.change_stat("obedience", 70, 30)
                $ Girl.change_stat("inhibition", 80, 35)
            else:
                $ Girl.change_stat("love", 90, 5)
                $ Girl.change_stat("obedience", 70, 25)
                $ Girl.change_stat("inhibition", 80, 30)
        elif action == "blowjob":
            if Girl.Forced:
                $ Girl.change_stat("love", 90, -70)
                $ Girl.change_stat("obedience", 70, 45)
                $ Girl.change_stat("inhibition", 80, 60)
            else:
                $ Girl.change_stat("love", 90, 5)
                $ Girl.change_stat("obedience", 70, 35)
                $ Girl.change_stat("inhibition", 80, 40)
        elif action == "dildo_pussy":
            if Girl.Forced:
                $ Girl.change_stat("love", 90, -75)
                $ Girl.change_stat("obedience", 70, 60)
                $ Girl.change_stat("inhibition", 80, 35)
            else:
                $ Girl.change_stat("love", 90, 10)
                $ Girl.change_stat("obedience", 70, 20)
                $ Girl.change_stat("inhibition", 80, 45)
        elif action == "dildo_ass":
            if Girl.Forced:
                $ Girl.change_stat("love", 90, -75)
                $ Girl.change_stat("obedience", 70, 60)
                $ Girl.change_stat("inhibition", 80, 35)
            else:
                $ Girl.change_stat("love", 90, 10)
                $ Girl.change_stat("obedience", 70, 20)
                $ Girl.change_stat("inhibition", 80, 45)
        elif action == "sex":
            if Girl.Forced:
                $ Girl.change_stat("love", 90, -150)
                $ Girl.change_stat("obedience", 70, 60)
                $ Girl.change_stat("inhibition", 80, 50)
            else:
                $ Girl.change_stat("love", 90, 30)
                $ Girl.change_stat("obedience", 70, 30)
                $ Girl.change_stat("inhibition", 80, 60)
        elif action == "anal":
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
        elif action == "hotdog":
            if Girl.Forced:
                $ Girl.change_stat("love", 90, -5)
                $ Girl.change_stat("obedience", 70, 20)
                $ Girl.change_stat("inhibition", 80, 10)
            else:
                $ Girl.change_stat("love", 90, 20)
                $ Girl.change_stat("obedience", 70, 20)
                $ Girl.change_stat("inhibition", 80, 20)

    return

label first_action_approval_forced_reactions(Girl, action):
    $ Girl.change_face("sad")

    if action in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "anal", "hotdog"]:
        $ Girl.change_stat("love", 70, -3, 1)
        $ Girl.change_stat("love", 20, -2, 1)
    elif action in ["sex"]:
        $ Girl.change_stat("love", 70, -30, 1)
        $ Girl.change_stat("love", 20, -20, 1)

    return

label first_action_approval_mostly_love_reactions(Girl, action):
    $ Girl.change_face("sexy")
    $ Girl.Brows = "sad"
    $ Girl.Mouth = "smile"

    call first_action_approval_mostly_love_lines(Girl)

    return

label first_action_approval_mostly_obedience_reactions(Girl, action):
    if action in ["handjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
        $ Girl.change_face("normal")
    elif action in ["footjob"]:
        $ Girl.change_face("normal",1)

    call first_action_approval_mostly_obedience_lines(Girl)

    return

label first_action_approval_addicted_reactions(Girl, action):
    $ Girl.change_face("manic", 1)

    call first_action_approval_addicted_lines(Girl)

    return

label first_action_approval_reactions(Girl, action):
    if action in ["handjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
        $ Girl.change_face("sad")
        $ Girl.Mouth = "smile"
    elif action in ["footjob"]:
        $ Girl.change_face("lipbite",1)

    call first_action_approval_lines(Girl)

    return

label auto_approved_reactions(Girl, action):
    if action == "fondle_thighs":
        $ Girl.change_face("sexy")
        $ Girl.change_stat("obedience", 50, 1)
        $ Girl.change_stat("inhibition", 30, 2)

        "As you caress her thigh, [Girl.name] glances at you, and smiles."
    elif action == "fondle_breasts":
        $ Girl.change_face("sexy")
        $ Girl.change_stat("obedience", 90, 1)
        $ Girl.change_stat("obedience", 70, 2)
        $ Girl.change_stat("inhibition", 70, 3)
        $ Girl.change_stat("inhibition", 30, 2)

        "As you cup her breast, [Girl.name] gently nods."
    elif action == "suck_breasts":
        $ Girl.change_face("sexy")
        $ Girl.change_stat("obedience", 90, 1)
        $ Girl.change_stat("obedience", 70, 2)
        $ Girl.change_stat("inhibition", 70, 3)
        $ Girl.change_stat("inhibition", 30, 2)

        "As you dive in, [Girl.name] seems a bit surprised, but just makes a little \"coo.\""
    elif action == "fondle_pussy":
        $ Girl.change_face("sexy")
        $ Girl.change_stat("obedience", 90, 1)
        $ Girl.change_stat("obedience", 70, 2)
        $ Girl.change_stat("inhibition", 70, 3)
        $ Girl.change_stat("inhibition", 30, 2)

        "As your hand creeps up her thigh, [Girl.name] seems a bit surprised, but then nods."
    elif action == "finger_pussy":
        $ Girl.change_face("surprised")
        $ Girl.change_stat("obedience", 90, 1)
        $ Girl.change_stat("obedience", 70, 2)
        $ Girl.change_stat("inhibition", 70, 3)
        $ Girl.change_stat("inhibition", 30, 2)

        "As you slide a finger in, [Girl.name] seems a bit surprised, but seems into it."
    elif action == "eat_pussy":
        $ Girl.change_face("surprised")
        $ Girl.change_stat("obedience", 90, 1)
        $ Girl.change_stat("obedience", 70, 2)
        $ Girl.change_stat("inhibition", 70, 3)
        $ Girl.change_stat("inhibition", 30, 2)

        $ line = renpy.random.choice(["As you crouch down and start to lick her pussy, [Girl.name] startles, but then sinks into the sensation.",
            "As you crouch down and start to lick her pussy, [Girl.name] jumps, but then softens.",
            "As you crouch down and start to lick her pussy, [Girl.name] starts, but then softens."])
        "[line]"

        $ Girl.change_face("sexy")
    elif action == "fondle_ass":
        $ Girl.change_face("surprised", 1)
        $ Girl.change_stat("obedience", 70, 2)
        $ Girl.change_stat("inhibition", 40, 2)

        $ line = renpy.random.choice(["As your hand creeps down her backside, [Girl.name] seems a bit surprised, but then nods.",
            "As your hand creeps down her backside, [Girl.name] jumps a bit, and then relaxes.",
            "As your hand creeps down her backside, [Girl.name] shivers a bit, and then relaxes."])
        "[line]"

        $ Girl.change_face("sexy")
    elif action == "finger_ass":
        $ Girl.change_face("surprised")
        $ Girl.change_stat("obedience", 90, 2)
        $ Girl.change_stat("obedience", 70, 2)
        $ Girl.change_stat("inhibition", 80, 2)
        $ Girl.change_stat("inhibition", 30, 2)

        "As you slide a finger in, [Girl.name] tightens around it in surprise, but seems into it."

        $ Girl.change_face("sexy")
    elif action == "eat_ass":
        $ Girl.change_face("surprised")
        $ Girl.change_stat("obedience", 90, 1)
        $ Girl.change_stat("inhibition", 80, 3)
        $ Girl.change_stat("inhibition", 40, 2)

        "As you crouch down and start to lick her asshole, [Girl.name] startles briefly, but then begins to melt."

        $ Girl.change_face("sexy")
    elif action in dildo_actions or action in sex_actions:
        "[Girl.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."

        $ Girl.change_face("sexy")
        $ Girl.change_stat("obedience", 70, 3)
        $ Girl.change_stat("inhibition", 50, 3)
        $ Girl.change_stat("inhibition", 70, 1)

        call lets_do_this_lines(Girl)

    return

label auto_rejected_reactions(Girl, action):
    if action in ["fondle_thighs", "suck_breasts", "fondle_pussy"]:
        $ Girl.change_face("surprised")
        $ Girl.change_stat("obedience", 50, -2)

        call go_back_lines(Girl)
    elif action == "fondle_breasts":
        $ Girl.change_face("surprised")
        $ Girl.Brows = "confused"
        $ Girl.change_stat("obedience", 50, -2)

        call go_back_lines(Girl)
    elif action == "finger_pussy":
        $ Girl.change_face("surprised", 2)
        $ Girl.change_stat("love", 80, -2)
        $ Girl.change_stat("obedience", 50, -3)

        Girl.voice "Oooh!"
        "She slaps your hand back."

        $ Girl.change_face("perplexed", 1)

        call go_back_lines(Girl)
    elif action == "eat_pussy":
        $ Girl.change_face("surprised")
        $ Girl.change_stat("love", 80, -2)
        $ Girl.change_stat("obedience", 50, -3)

        call go_back_lines(Girl)

        $ Girl.change_face("perplexed",1)

        "She pushes your head back away from her."
    elif action == "fondle_ass":
        $ Girl.change_face("surprised")
        $ Girl.change_stat("obedience", 50, -3)

        call go_back_lines(Girl)

        $ Girl.change_face("bemused")
    elif action in ["finger_ass", "eat_ass"]:
        $ Girl.change_face("surprised")
        $ Girl.change_stat("love", 80, -2)
        $ Girl.change_stat("obedience", 50, -3)

        call go_back_lines(Girl)
    elif action in dildo_actions or action in sex_actions:
        $ Girl.Brows = "angry"

        call what_do_you_think_youre_doing_lines(Girl)
        call what_do_you_think_youre_doing_menu(Girl, action)

    return

label pullback_reactions(Girl, action):
    $ Girl.change_face("surprised")
    $ Girl.Brows = "sad"

    if action in ["fondle_pussy", "fondle_ass"]:
        if Girl.lust > 80:
            $ Girl.change_stat("love", 70, -4)
    elif action in ["fondle_thighs", "finger_ass", "eat_ass"]:
        if Girl.lust > 60:
            $ Girl.change_stat("love", 70, -3)

    $ Girl.change_stat("obedience", 90, 1)
    $ Girl.change_stat("obedience", 70, 2)

    "As you pull back, [Girl.name] looks a little sad."
    "As your finger slides out, [Girl.name] gasps and looks upset."
    "As your hand pulls out, [Girl.name] gasps and looks upset."

    return

label recent_action_reactions(Girl):
    $ Girl.change_face("sexy", 1)

    call recent_action_lines(Girl)

    return

label done_action_today_reactions(Girl):
    $ Girl.change_face("sexy", 1)

    call gently_lines(Girl)

    return

label first_time_asking_reactions(Girl, action):
    if primary_action != "footjob":
        $ Girl.change_face("surprised", 1)
        $ Girl.Mouth = "kiss"

        call first_time_asking_lines(Girl)
    else:
        $ Girl.change_face("confused", 2)

        call first_time_asking_lines(Girl)

        $ Girl.Blush = 1

    if action == "titjob":
        if Girl.blowjob:
            $ Girl.Mouth = "smile"

            call mouth_not_enough(Girl)
        elif Girl.handjob:
            $ Girl.Mouth = "smile"

            call hand_not_enough(Girl)
    elif action == "blowjob":
        if Girl.handjob:
            $ Girl.Mouth = "smile"

            call hand_not_enough(Girl)

    if Girl.Forced:
        $ Girl.change_face("sad")

        call first_time_forcing_lines(Girl)

    return

label ass_sore_reactions(Girl):
    $ Girl.change_face("bemused", 1)

    call ass_sore_lines(Girl)

    return

label starting_to_get_bored_reactions(Girl, action):
    $ Girl.Brows = "confused"

    call warm_hands_lines(Girl)
    call getting_close_lines(Girl)

    return

label definitely_bored_now_reactions(Girl, action):
    if action == "kiss":
        $ Girl.Brows = "confused"

        call try_something_else_lines(Girl)
    else:
        $ Girl.Brows = "angry"

        call getting_rugburn_lines(Girl)
        call done_with_this_lines(Girl)
        call can_we_do_something_else_lines(Girl)

    call try_something_else_menu(Girl, action)

    return

label unsatisfied_reactions(Girl, action):
    $ Girl.change_face("angry")

    if Girl != JeanX:
        $ Girl.Eyes = "side"

    call didnt_get_off_lines(Girl)

    return

label would_you_like_more_reactions(Girl, action):
    $ Girl.change_face("sexy", 1)
    $ Girl.Brows = "sad"

    call would_you_like_more_lines(Girl)

    return

label done_with_action_reactions(Girl, action):
    $ Girl.change_face("bemused", 0)

    call im_done_lines(Girl)
