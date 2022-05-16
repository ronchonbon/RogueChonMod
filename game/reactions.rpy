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
            if approvalcheck(Girl, 500, "I"):
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
            if not Girl.action_counter["anal"]:
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

label sex_acts(action = 0):
    if Alonecheck(focused_Girl) and focused_Girl.Taboo == 20:
        $ focused_Girl.Taboo = 0
        $ Taboo = 0

    call shift_focus(focused_Girl)

    if action == "SkipTo":
        $ renpy.pop_call() #causes it to skip past the Trigger Swap
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

        if (Girl.Over or Girl.Chest) and not Girl.top_pulled_up:
            if approvalcheck(Girl, 1250, TabM = 1) or (Girl.SeenChest and approvalcheck(Girl, 500) and not Taboo):
                $ Girl.top_pulled_up = 1

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


        if (Girl.Legs and not Girl.upskirt) or (Girl.Panties and not Girl.underwear_pulled_down):
            if approvalcheck(Girl, 1250, TabM = 1) or (Girl.SeenPussy and approvalcheck(Girl, 500) and not Taboo):
                $ Girl.upskirt = 1
                $ Girl.underwear_pulled_down = 1

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

            $ Girl.upskirt = 1
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

                $ Girl.upskirt = 1
            elif Girl.PantsNum() > 6:
                $ line = renpy.random.choice(["[Girl.name] turns and backs up against your cock, sliding her [Girl.Legs] down as she does so.",
                    "[Girl.name] rolls back and pulls you against her, sliding her [Girl.Legs] off as she does so.",
                    "[Girl.name] pushes you down and climbs on top of you, sliding her [Girl.Legs] down as she does so.",
                    "[Girl.name] turns around, sliding her [Girl.Legs] down as she does so.",
                    "[Girl.name] lays back, sliding her [Girl.Legs] down as she does so."])
                "[line]"

                $ Girl.upskirt = 1
            elif Girl.PantsNum() == 6:
                $ line = renpy.random.choice(["[Girl.name] rolls onto her back and pulls you against her, sliding her shorts off as she does so."])
                "[line]"

                $ Girl.upskirt = 1
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

                $ Girl.add_word(1,"refused","refused")

                return True

    return False

label first_action_approval(Girl, action):
    if Girl.Forced:
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
            $ Girl.Mouth = "smile"
            call that_was_nice_lines(Girl)
        elif action in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass", "dildo_pussy", "dildo_ass"] and Girl.obedience <= 500 and Player.focus <= 20:
            $ Girl.change_face("perplexed", 1)

            call was_that_enough_lines(Girl)
        elif action in cock_actions and  Player.focus <= 20:
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

        $ Girl.change_stat("inhibition", 30, 2)
        $ Girl.change_stat("inhibition", 70, 1)
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

        $ Girl.change_stat("inhibition", 30, 3)
        $ Girl.change_stat("inhibition", 70, 1)
    elif action == "hotdog":
        $ achievement = Girl.tag + " Full Buns"

        if Girl == RogueX:
            call Partner_Like(Girl, 1)
        elif Girl in [KittyX, EmmaX, LauraX]:
            call Partner_Like(Girl, 2)

        $ Girl.change_stat("inhibition", 30, 1)
        $ Girl.change_stat("inhibition", 70, 1)

    return

label action_approved(Girl, action):
    $ Girl.change_face("sexy", 1)

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
    elif action in ["finger_pussy"]:
        $ Girl.change_face("bemused", 2)

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
        call not_happening_lines(Girl)

        if Girl in [RogueX, KittyX, EmmaX, StormX]:
            $ Girl.Blush = 1
        else:
            $ Girl.Blush = 0

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
    $ Girl.ArmPose = 1

    if "no_" + action in Girl.daily_history:
        $ Girl.change_face("angry", 1)

        call learn_to_take_no_lines(Girl)

        $ Girl.add_word(1,"angry","angry")
    elif Girl.Forced:
        call went_too_far_reactions(Girl, action)

        $ Girl.add_word(1, "angry", "angry")
    elif Taboo:
        call action_rejected_taboo_reactions(Girl, action)

        $ Girl.add_word(1, "tabno", "tabno")
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

    if approval > 1 or (approval and Girl.Forced):
        call forced_but_not_unwelcome_reactions(Girl, action)

        if approval < 2:
            $ Girl.Forced = 1

        jump before_action
    else:
        call forced_rejected_reactions(Girl, action)

        $ Girl.add_word(1, "angry", "angry")

    return
