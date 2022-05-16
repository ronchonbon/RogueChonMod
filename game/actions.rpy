label action(Girl):
    if primary_action in dildo_actions:
        call Rogue_Dildo_check

        if not _return:
            return

    $ Round -= 5 if Round > 5 else (Round-1)

    call shift_focus(Girl)
    call set_approval_bonus(Girl, primary_action)
    call action_approval_checks(Girl, primary_action)

    if primary_action == "kiss" and Girl == EmmaX and not approval_check(Girl, 1000):
        $ Girl.change_face("sadside")

        ch_e "Not when we barely know each other. . ."

        $ Girl.recent_history.append("no_kissing")
        $ Girl.daily_history.append("no_kissing")

        return

    if action_context in ["auto", "offhand"]:
        call auto_action_narrations(Girl, primary_action)

        if Approval:
            call auto_approved_reactions(Girl, primary_action)

            if action_context == "auto":
                jump before_action
            else:
                return
        else:
            call auto_rejected_reactions(Girl, primary_action)

            $ approval_bonus = 0
            $ offhand_action = 0

            return

    if action_context == "pullback":
        call pullback_reactions(Girl)
        jump before_action
    elif primary_action in anal_insertion_actions and not Girl.used_to_anal and ("finger_ass" in Girl.daily_history or "dildo_anal" in Girl.daily_history or "anal" in Girl.daily_history):
        call ass_sore_reactions(Girl)
    elif primary_action in Girl.recent_history:
        call recent_action_reactions(Girl)
        jump before_action
    elif primary_action in Girl.daily_history:
        call done_action_today_reactions(Girl)
        jump before_action

    if primary_action != "kiss":
        if not Girl.action_counter[primary_action] and "no_" + primary_action not in Girl.recent_history:
            call first_time_asking_reactions(Girl, primary_action)

        if not Girl.action_counter[primary_action] and Approval:
            call first_action_approval(Girl, primary_action)
        elif Approval:
            call action_approved(Girl, primary_action)

        if Approval >= 2:
            call action_accepted(Girl, primary_action)
            label begging_approved:

            return
        else:
            call action_disapproved(Girl, primary_action)

        call action_rejected(Girl, primary_action)
        label begging_rejected:
    elif primary_action == "kiss":
        if Approval > 1 and not Girl.action_counter["kiss"] and not Girl.Forced:
            $ Girl.change_face("sexy")
            $ Girl.eyes = "side"

            if Girl == RogueX:
                ch_r "I've never really been able to do this, so I'm a bit excited to try. . ."
            elif Girl == KittyX:
                ch_k "You are kinda cute. . ."
            elif Girl == EmmaX:
                ch_e "Well, I suppose it couldn't hurt. . ."
            elif Girl == LauraX:
                ch_l "Worth a shot. . ."
            elif Girl == JeanX:
                ch_j "Why not?"
            elif Girl == StormX:
                ch_s "I would like that."
            elif Girl == JubesX:
                ch_v "I guess we did get off to a poor start. . ."
        elif Approval and not Girl.action_counter["kiss"]:
            $ Girl.change_face("sexy")
            $ Girl.eyes = "side"

            if Girl == RogueX:
                ch_r "I guess it's worth a shot. . ."
            elif Girl == KittyX:
                ch_k "I'll give it a go. . ."
            elif Girl == EmmaX:
                ch_e "We could. . ."
            elif Girl == LauraX:
                ch_l "If you insist. . ."
            elif Girl == JeanX:
                ch_j "I mean, whatever. . ."
            elif Girl == StormX:
                ch_s "I suppose."
            elif Girl == JubesX:
                ch_v "I suppose we could. . ."
        elif Approval and "kissing" in Girl.recent_history:
            $ Girl.change_face("sexy", 1)

            if Girl == KittyX:
                ch_k "Prrr. . ."
            else:
                Girl.voice "Mmmm. . ."

            jump before_action
        elif Approval and "kissing" in Girl.daily_history:
            $ Girl.change_face("sexy", 1)

            $ Line = renpy.random.choice(["A","B","C"])

            if Line == "A":
                Girl.voice "Didn't get enough earlier?"
            elif Girl == RogueX:
                if Line == "B":
                    ch_r "{i}I'm{/i} used to being the one sucking people dry. . ."
                else:
                    ch_r "Gimme some sugar, sugar."
            elif Girl == KittyX:
                if Line == "B":
                    ch_k "Meow."
                else:
                    ch_k "Come'ere tasty."
            elif Girl == EmmaX:
                if Line == "B":
                    ch_e "Mmmm. . ."
                else:
                    ch_e "Come and get it."
            elif Girl == LauraX:
                if Line == "B":
                    ch_l "Mmmmmm."
                else:
                    ch_l "Get over here."
            elif Girl == JeanX:
                if Line == "B":
                    ch_j "MmMmmm. . ."
                else:
                    ch_j "Oh, get over here."
            elif Girl == StormX:
                if Line == "B":
                    ch_s "Mmmm. . ."
                else:
                    ch_s "Yes, let's."
            elif Girl == JubesX:
                if Line == "B":
                    ch_v "Mmmm. . ."
                else:
                    ch_v "Sure, come to me."

            $ Line = 0
        elif Approval > 1 and Girl.love > Girl.obedience:
            $ Girl.change_face("sexy")

            if Girl == RogueX:
                ch_r "Sure, why not?"
            elif Girl == KittyX:
                ch_k "Smooches!"
            elif Girl == EmmaX:
                ch_e "Mwa."
            elif Girl == LauraX:
                ch_l "Mmmmm. . ."
            elif Girl == JeanX:
                ch_j "MmMmmmm. . ."
            elif Girl == StormX:
                ch_s "Hrm. . ."
            elif Girl == JubesX:
                ch_v "Mmmm. . ."
        elif approval_check(Girl, 500, "O") and Girl.obedience > Girl.love:
            $ Girl.change_face("normal")

            if Girl == RogueX:
                ch_r "If you wish."
            elif Girl == KittyX:
                ch_k "Sure, ok."
            elif Girl == EmmaX:
                ch_e "Of course."
            elif Girl == LauraX:
                ch_l "If you want."
            elif Girl == JeanX:
                ch_j "Ok. . ."
            elif Girl == StormX:
                ch_s "Very well. . ."
            elif Girl == JubesX:
                ch_v "sure. . ."

            $ Girl.change_stat("obedience", 60, 1)
        elif approval_check(Girl, 250, "O",Alt=[[KittyX,LauraX],300]) and approval_check(Girl, 250, "L",Alt=[[KittyX,LauraX],200]):
            $ Girl.change_face("bemused")

            Girl.voice "Ok, fine."

            $ Girl.change_stat("obedience", 50, 3)
        elif Girl.addiction >= 50:
            $ Girl.change_face("sexy")
            $ Girl.eyes = "manic"

            if Girl == RogueX:
                ch_r "Hm. . . ok, let's do this."
            elif Girl == KittyX:
                ch_k "I kinda have to."
            elif Girl == EmmaX:
                ch_e ". . . yes."
            elif Girl == LauraX:
                ch_l "I have to."
            elif Girl == JeanX:
                ch_j "Um. . . yeah. . ."
            elif Girl == StormX:
                ch_s ". . . yes. . ."
            elif Girl == JubesX:
                ch_v "Oh yes. . ."
        elif Approval:
            $ Girl.change_face("bemused")

            if Girl == RogueX:
                ch_r "hmm, ok."
            elif Girl == KittyX:
                ch_k "Yeah, whatever."
            elif Girl == EmmaX:
                ch_e "Very well."
            elif Girl == LauraX:
                ch_l "Sure."
            elif Girl == JeanX:
                ch_j "Whatever. . ."
            elif Girl == StormX:
                ch_s "Fine."
            elif Girl == JubesX:
                ch_v "Sure, ok. . ."
        else:
            $ Girl.change_face("normal")
            $ Girl.mouth = "sad"

            if Girl == RogueX:
                ch_r "Nah, I don't think I'm interested."
            elif Girl == KittyX:
                ch_k "Nope."
            elif Girl == EmmaX:
                ch_e "Hmmm, no."
            elif Girl == LauraX:
                ch_l "No."
            elif Girl == JeanX:
                ch_j "You wish. . ."
            elif Girl == StormX:
                ch_s "I do not think so."
            elif Girl == JubesX:
                ch_v "No thanks. . ."

            $ Girl.recent_history.append("no_kissing")
            $ Girl.daily_history.append("no_kissing")

    return

label before_action:
    if Taboo:
        $ focused_Girl.inhibition += int(Taboo/10)
        $ focused_Girl.lust += int(Taboo/5)

    $ focused_Girl.change_face("sexy")

    if primary_action == "kiss":
        $ focused_Girl.change_stat("inhibition", 10, 1)
        $ focused_Girl.change_stat("inhibition", 20, 1)

        call expression focused_Girl.Tag + "_Kissing_Launch" pass("kiss")

        if focused_Girl.action_counter["kiss"] >= 10 and focused_Girl.inhibition >= 300:
            $ focused_Girl.change_face("sucking")
        elif focused_Girl.action_counter["kiss"] > 1 and focused_Girl.addiction >= 50:
            $ focused_Girl.change_face("sucking")
        else:
            $ focused_Girl.change_face("kiss",2)

        if focused_Girl == RogueX and not Girl.action_counter["kiss"]:
            jump Rogue_first_kiss
        else:
            call kissing_narrations(focused_Girl)
    elif primary_action in fondle_actions:
        if not focused_Girl.Forced and action_context != "auto":
            $ approval_bonus = 0

            if primary_action in ["eat_pussy", "eat_ass"] and focused_Girl.PantsNum() >= 6:
                $ approval_bonus = 15

            if primary_action in inside_panties_actions:
                call Bottoms_Off
            elif primary_action in breast_actions:
                call Top_Off

            if "angry" in focused_Girl.recent_history:
                return

        $ approval_bonus = 0
    elif primary_action in job_actions:
        if primary_action not in dildo_actions:
            if focused_Girl.Forced:
                $ focused_Girl.change_face("sad")
            elif not focused_Girl.action_counter[action]:
                $ focused_Girl.Brows = "confused"
                $ focused_Girl.Eyes = "sexy"
                $ focused_Girl.Mouth = "smile"
        else:
            if not focused_Girl.Forced and action_context != "auto":
                if primary_action == "dildo_pussy":
                    $ approval_bonus = 15 if focused_Girl.PantsNum() > 6 else 0
                elif primary_action == "dildo_ass":
                    $ approval_bonus = 20 if focused_Girl.PantsNum() > 6 else 0

                call Bottoms_Off(focused_Girl)

                if "angry" in focused_Girl.recent_history:
                    return

            $ approval_bonus = 0

        call Seen_First_Peen(focused_Girl, Partner, React = action_context)

        if primary_action == "handjob":
            call expression focused_Girl.Tag + "_HJ_Launch" pass("L")
        elif primary_action == "titjob":
            call expression focused_Girl.Tag + "_TJ_Launch" pass("L")
        elif primary_action == "blowjob":
            call expression focused_Girl.Tag + "_BJ_Launch" pass("L")
        elif primary_action in dildo_actions:
            call expression focused_Girl.Tag + "_Pussy_Launch" pass(primary_action)
    elif primary_action in sex_actions:
        call Seen_First_Peen(focused_Girl, Partner, React = action_context)

        $ focused_Girl.pose = "doggy"

        call expression focused_Girl.Tag + "_Sex_Launch" pass(primary_action)

    if primary_action not in sex_actions:
        if action_context == focused_Girl:
            $ action_context = 0

            call girl_initiated_action(focused_Girl, primary_action)

            if _return:
                return
    elif primary_action in sex_actions:
        if action_context == focused_Girl:
            $ action_context = 0

            call girl_initiated_action(focused_Girl, primary_action)

            if _return:
                return

            $ focused_Girl.underwearDown = 1

            call expression focused_Girl.Tag + "_First_Bottomless" pass(1)
        elif action_context != "auto":
            if primary_action in ["sex", "anal"]:
                call AutoStrip(focused_Girl)
            elif primary_action == "hotdog":
                call Bottoms_Off(focused_Girl)

            call start_of_sex_narration(focused_Girl, primary_action)
        else:
            if primary_action in ["sex", "anal"]:
                if primary_action == "sex":
                    $ word = renpy.random.choice(["slit"])
                elif primary_action == "anal":
                    $ word = renpy.random.choice(["ass", "back door"])

                if (focused_Girl.PantsNum() > 6 and not focused_Girl.Upskirt) and (focused_Girl.underwear and not focused_Girl.underwearDown):
                    "You quickly pull down her pants and her [focused_Girl.Panties] and press against her [word]."
                elif (focused_Girl.underwear and not focused_Girl.underwearDown):
                    "You quickly pull down her [focused_Girl.Panties] and press against her [word]."

                $ focused_Girl.Upskirt = 1
                $ focused_Girl.underwearDown = 1
                $ focused_Girl.SeenPanties = 1

                call expression focused_Girl.Tag + "_First_Bottomless" pass(1)
            elif primary_action == "hotdog":
                $ line = renpy.random.choice(["You press yourself against her ass.",
                    "You press yourself against her mound.",
                    "You roll back, pulling her on top of you and your rigid member.",
                    "She lays back, pulling you against her with your rigid member.",
                    "She turns around, pulling you against her with your rigid member."])
                "[line]"

        if Player.focus >= 50:
            call hard_cock_lines(focused_Girl)

    call first_action_reactions(focused_Girl, primary_action)

    if Taboo:
        if primary_action == "fondle_thighs":
            $ focused_Girl.change_stat("lust", 200, (int(Taboo/5)))
            $ focused_Girl.change_stat("inhibition", 200, (2*(int(Taboo/5))))
        elif primary_action in ["fondle_breasts", "suck_breasts", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "dildo_pussy", "dildo_ass"]:
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

        call expression focused_Girl.Tag + "_First_Bottomless" pass(1)

    $ line = 0
    $ counter = 0

    if primary_action == "fondle_pussy":
        $ action_speed = 1
    elif primary_action == "finger_pussy":
        $ action_speed = 2
    elif primary_action == "sex":
        $ Player.Cock = "in"

        $ action_speed = 1
    elif primary_action == "anal":
        $ Player.Cock = "anal"

        $ action_speed = 1
    elif primary_action == "hotdog":
        $ action_speed = 1

    if Taboo:
        $ focused_Girl.DrainWord("tabno")

    $ focused_Girl.DrainWord("no_" + primary_action)
    $ focused_Girl.AddWord(0, primary_action, primary_action)

    if primary_action in fondle_actions:
        if focused_Girl != EmmaX:
            call expression focused_Girl.Tag + "_Pussy_Launch" pass(primary_action)
        else:
            if focused_Girl.pose in ["doggy", "sex"]:
                call ViewShift(focused_Girl, focused_Girl.pose, 0, primary_action)
            else:
                call ViewShift(focused_Girl, "pussy", 0, primary_action)
    elif primary_action in breast_actions:
        call expression focused_Girl.Tag + "_Breasts_Launch" pass(primary_action)
    elif primary_action == "footjob":
        call expression focused_Girl.Tag + "_Sex_Launch" pass(footjob)

label action_cycle:
    if primary_action in mouth_actions:
        if primary_action != "kiss" and offhand_action == "kiss":
            $ offhand_action = 0

    while Round > 0:
        if primary_action == "kiss":
            call expression focused_Girl.Tag + "_Kissing_Launch" pass("kiss")

            $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0
        if primary_action in fondle_actions:
            call ViewShift(focused_Girl, Girl.pose, 0, primary_actions)
        elif primary_action in ["footjob", "sex", "anal", "hotdog"]:
            call expression focused_Girl.Tag + "_Sex_Launch" pass(primary_action)

            if primary_action == "sex":
                $ Player.Cock = "in"
            elif primary_action == "anal":
                $ Player.Cock = "anal"
            elif primary_action == "hotdog":
                $ Player.Cock = "out"
        elif primary_action in dildo_actions:
            call ViewShift(focused_Girl, Girl.pose, 0)

        $ focused_Girl.lust_face()

        if Player.focus < 100:
            if primary_action == "kiss":
                jump kiss_menu
            elif primary_action in fondle_actions:
                jump fondle_menu
            elif primary_action in job_actions:
                jump handjob_menu
            elif primary_action in sex_actions:
                jump sex_menu

        label action_menu_return:

        if primary_action in inside_panties_actions:
            if focused_Girl.underwear or focused_Girl.PantsNum() >= 6 or focused_Girl.HoseNum() >= 5: #This checks if Rogue wants to strip down.
                call Girl_Undress(focused_Girl, "auto")

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
                call pull_off_top_narration(focused_Girl)

                $ focused_Girl.Uptop = 1

                call expression focused_Girl.Tag + "_First_Topless"

    call end_of_action_reactions(focused_Girl, action)

label after_action:
    if primary_action in sex_actions:
        $ Player.Sprite = 0
        $ Player.Cock = "out"

        call expression focused_Girl.Tag + "_Sex_Reset"
    elif primary_action in fondle_actions:
        call expression focused_Girl.Tag + "_Pos_Reset"
    elif primary_action in dildo_actions:
        call expression focused_Girl.Tag + "_Pos_Reset"

    $ focused_Girl.change_face("sexy")
    $ focused_Girl.remaining_actions -= 1

    call action_specific_consequences(focused_Girl, primary_action)

    if primary_action == "kiss" and primary_action not in focused_Girl.recent_history:
        if Girl.love > 300:
            $ Girl.change_stat("love", 60, 4)
        $ Girl.change_stat("love", 70, 1)

    if primary_action in ["fondle_thighs", "fondle_ass"]:
        if RogueX.PantsNum() < 6 or RogueX.Upskirt:
            $ RogueX.addiction_rate += 1

            if Player.addictive:
                $ RogueX.addiction_rate += 1
    if primary_action not in dildo_actions:
        if primary_action == "kiss":
            $ focused_Girl.addiction_rate += 2 if focused_Girl.addiction_rate < 5 else 1
        else:
            $ focused_Girl.addiction_rate += 1

        if Player.addictive:
            $ focused_Girl.addiction_rate += 1

    if primary_action in ["handjob", "footjob"]:
        $ focused_Girl.change_stat("lust", 90, 5)

    if achievement is not None and achievement in Achievements:
        pass
    elif primary_action == "titjob" and Girl.action_counter[action] > 5:
        pass
    elif primary_action == "kiss" and Girl.action_counter[action] > 10:
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
    elif primary_action == "blowjob" and action_context == "shift":
        pass
    elif Girl.action_counter[action] == 1:
        call first_action_response(focused_Girl, primary_action)
    elif (primary_action in cock_actions or primary_action == "kiss") and Girl.action_counter[action] == 5:
        call after_action_five_times_lines(focused_Girl)
    elif primary_action in sex_actions and not action_context:
        if "unsatisfied" in focused_Girl.recent_history:
            call unsatisfied_reactions(Girl, action)

    if primary_action == "kiss" and not action_context and focused_Girl.action_counter["kiss"] > 5 and focused_Girl.lust > 50 and Approvalcheck(focused_Girl, 950):
        call would_you_like_more_lines(Girl, action)

    $ approval_bonus = 0

    if action_context == "shift":
        call switching_action_lines(focused_Girl)
    elif primary_action == "kiss":
        call expression focused_Girl.Tah + "_Pos_Reset"
    elif primary_action == "handjob":
        call expression focused_Girl.tag + "_HJ_Reset"
    elif primary_action == "footjob":
        call expression focused_Girl.tag + "_Doggy_Reset"
    elif primary_action == "titjob":
        call expression focused_Girl.tag + "_TJ_Reset"
    elif primary_action == "blowjob":
        call expression focused_Girl.tag + "_BJ_Reset"

    call checkout

    return

label set_approval_bonus(Girl, action):
    if primary_action == "fondle_thighs":
        if Girl.action_counter["fondle_thighs"]:
            $ approval_bonus += 10

        if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 5:
            $ approval_bonus -= 5

        if Girl.lust > 75:
            $ approval_bonus += 10

        if "exhibitionist" in Girl.Traits:
            $ approval_bonus += Taboo

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.Traits:
            $ approval_bonus -= 25
    elif primary_action == "fondle_breasts":
        if Girl.action_counter["fondle_breasts"]:
            $ approval_bonus += 15

        if Girl.lust > 75: #She's really horny
            $ approval_bonus += 20

        if "exhibitionist" in Girl.Traits:
            $ approval_bonus += (3*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.Traits:
            $ approval_bonus -= 20
    elif primary_action == "suck_breasts":
        if Girl.action_counter["suck_breasts"]: #You've done it before
            $ approval_bonus += 15

        if not Girl.Chest and not Girl.Over:
            $ approval_bonus += 15

        if Girl.lust > 75: #She's really horny
            $ approval_bonus += 20

        if Girl.lust > 75 and action_context == "auto": #She's really horny
            $ approval_bonus += 10

        if "exhibitionist" in Girl.Traits:
            $ approval_bonus += (4*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.Traits:
            $ approval_bonus -= 25
    elif primary_action == "fondle_pussy":
        if Girl.action_counter["fondle_pussy"]: #You've done it before
            $ approval_bonus += 20

        if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 5: # she's got pants on.
            $ approval_bonus -= 10

        if Girl.lust > 75: #She's really horny
            $ approval_bonus += 15

        if Girl.lust > 75 and action_context == "auto": #She's really horny
            $ approval_bonus += 10

        if "exhibitionist" in Girl.Traits:
            $ approval_bonus += (2*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.Traits:
            $ approval_bonus -= 25
    elif primary_action == "eat_pussy":
        if Girl.action_counter["eat_pussy"]: #You've done it before
            $ approval_bonus += 15

        if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 5: # she's got pants on.
            $ approval_bonus -= 15

        if Girl.lust > 95:
            $ approval_bonus += 20
        elif Girl.lust > 85: #She's really horny
            $ approval_bonus += 15

        if Girl.lust > 85 and action_context == "auto": #She's really horny
            $ approval_bonus += 10

        if action_context == "shift":
            $ approval_bonus += 10

        if "exhibitionist" in Girl.Traits:
            $ approval_bonus += (4*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.Traits:
            $ approval_bonus -= 25
    elif primary_action == "fondle_ass":
        if Girl.action_counter["fondle_ass"]: #You've done it before
            $ approval_bonus += 10

        if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 5: # she's got pants on.
            $ approval_bonus -= 5

        if Girl.lust > 75: #She's really horny
            $ approval_bonus += 15

        if "exhibitionist" in Girl.Traits:
            $ approval_bonus += Taboo

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.Traits:
            $ approval_bonus -= 25
    elif primary_action == "finger_ass":
        if Girl.action_counter["finger_ass"]: #You've done it before
            $ approval_bonus += 25

        if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 5: # she's got pants on.
            $ approval_bonus -= 15

        if Girl.lust > 85 and Girl.used_to_anal: #She's really horny
            $ approval_bonus += 15

        if Girl.lust > 95 and Girl.used_to_anal:
            $ approval_bonus += 5

        if Girl.lust > 85 and action_context == "auto": #She's really horny
            $ approval_bonus += 10

        if action_context == "shift":
            $ approval_bonus += 10

        if "exhibitionist" in Girl.Traits:
            $ approval_bonus += (4*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.Traits:
            $ approval_bonus -= 25
    elif primary_action == "eat_ass":
        if Girl.action_counter["eat_ass"]: #You've done it before
            $ approval_bonus += 20

        if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 5: # she's got pants on.
            $ approval_bonus -= 25

        if Girl.lust > 95:
            $ approval_bonus += 20
        elif Girl.lust > 85: #She's really horny
            $ approval_bonus += 15

        if Girl.lust > 85 and action_context == "auto": #auto
            $ approval_bonus += 10

        if action_context == "shift":
            $ approval_bonus += 10

        if "exhibitionist" in Girl.Traits:
            $ approval_bonus += (4*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.Traits:
            $ approval_bonus -= 25
    elif primary_action == "handjob":
        if Girl.action_counter[action] >= 7: # She loves it
            $ approval_bonus += 10
        elif Girl.action_counter[action] >= 3: #You've done it before several times
            $ approval_bonus += 7
        elif Girl.action_counter[action]: #You've done it before
            $ approval_bonus += 3

        if "exhibitionist" in Girl.Traits:
            $ approval_bonus += (3*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.Traits:
            $ approval_bonus -= 40

        if Girl.addiction >= 75 and Girl.event_counter["swallowed"] >= 3: #She's really strung out and has swallowed
            $ approval_bonus += 15
        if Girl.addiction >= 75:
            $ approval_bonus += 5

        if action_context == "shift":
            $ approval_bonus += 15
    elif primary_action == "footjob":
        if Girl.action_counter[action] >= 7: # She loves it
            $ approval_bonus += 10
        elif Girl.action_counter[action] >= 3: #You've done it before several times
            $ approval_bonus += 7
        elif Girl.action_counter[action]: #You've done it before
            $ approval_bonus += 3

        if Girl.addiction >= 75 and Girl.event_counter["swallowed"] >=3: #She's really strung out and has swallowed
            $ approval_bonus += 10
        if Girl.addiction >= 75:
            $ approval_bonus += 5

        if action_context == "shift":
            $ approval_bonus += 15
        if "exhibitionist" in Girl.Traits:
            $ approval_bonus += (3*Taboo)
        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.Traits:
            $ approval_bonus -= 40
    elif primary_action == "titjob":
        if Girl.action_counter[action] >= 7: # She loves it
            $ approval_bonus += 10
        elif Girl.action_counter[action] >= 3: #You've done it before several times
            $ approval_bonus += 7
        elif Girl.action_counter[action]: #You've done it before
            $ approval_bonus += 5

        if Girl.SeenChest and approval_check(Girl, 500): # You've seen her tits.
            $ approval_bonus += 10
        if not Girl.Chest and not Girl.Over: #She's already topless
            $ approval_bonus += 10

        if "exhibitionist" in Girl.Traits:
            $ approval_bonus += (5*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.Traits:
            $ approval_bonus -= 30

        if Girl.lust > 75: #She's really horny
            $ approval_bonus += 10

        if Girl.addiction >= 75 and Girl.event_counter["swallowed"] >= 3: #She's really strung out and has swallowed
            $ approval_bonus += 15
        if Girl.addiction >= 75:
            $ approval_bonus += 5

        if action_context == "shift":
            $ approval_bonus += 15
    elif primary_action == "blowjob":
        if Girl.action_counter[action] >= 7: # She loves it
            $ approval_bonus += 15
        elif Girl.action_counter[action] >= 3: #You've done it before several times
            $ approval_bonus += 10
        elif Girl.action_counter[action]: #You've done it before
            $ approval_bonus += 7

        if Girl.addiction >= 75 and Girl.event_counter["swallowed"] >=3: #She's really strung out and has swallowed
            $ approval_bonus += 25
        elif Girl.addiction >= 75: #She's really strung out
            $ approval_bonus += 15

        if "exhibitionist" in Girl.Traits:
            $ approval_bonus += (4*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.Traits:
            $ approval_bonus -= 40

        if action_context == "shift":
            $ approval_bonus += 15
    elif primary_action == "dildo_pussy":
        if Girl.action_counter[action]: #You've done it before
            $ approval_bonus += 15
        if Girl.PantsNum() > 6: # she's got pants on.
            $ approval_bonus -= 20

        if Girl.lust > 95:
            $ approval_bonus += 20
        elif Girl.lust > 85: #She's really horny
            $ approval_bonus += 15

        if action_context == "shift":
            $ approval_bonus += 10
        if "exhibitionist" in Girl.Traits:
            $ approval_bonus += (5*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.Traits:
            $ approval_bonus -= 40
    elif primary_action == "dildo_ass":
        if Girl.used_to_anal:
            $ approval_bonus += 30
        elif "anal" in Girl.recent_history or "dildo_anal" in Girl.recent_history:
            $ approval_bonus -= 20
        elif "anal" in Girl.daily_history or "dildo_anal" in Girl.daily_history:
            $ approval_bonus -= 10
        elif (Girl.action_counter["anal"] + Girl.action_counter["dildo_ass"] + Girl.Plug) > 0: #You've done it before
            $ approval_bonus += 20

        if Girl.PantsNum() > 6: # she's got pants on.
            $ approval_bonus -= 20

        if Girl.lust > 95:
            $ approval_bonus += 20
        elif Girl.lust > 85: #She's really horny
            $ approval_bonus += 15

        if action_context == "shift":
            $ approval_bonus += 10
        if "exhibitionist" in Girl.Traits:
            $ approval_bonus += (5*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.Traits:
            $ approval_bonus -= 40
    elif primary_action == "sex":
        if Girl.action_counter["sex"] >= 7: # She loves it
            $ approval_bonus += 15
        elif Girl.action_counter["sex"] >= 3: #You've done it before several times
            $ approval_bonus += 12
        elif Girl.action_counter["sex"]: #You've done it before
            $ approval_bonus += 10

        if Girl.addiction >= 75 and (Girl.event_counter["creampied"] + Girl.event_counter["anal_creampied"]) >=3: #She's really strung out and has creampied
            $ approval_bonus += 20
        elif Girl.addiction >= 75:
            $ approval_bonus += 15

        if Girl.lust > 85:
            $ approval_bonus += 10
        elif Girl.lust > 75: #She's really horny
            $ approval_bonus += 5

        if action_context == "shift":
            $ approval_bonus += 10
        if "exhibitionist" in Girl.Traits:
            $ approval_bonus += (4*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.Traits:
            $ approval_bonus -= 40
    elif primary_action == "anal":
        if Girl.action_counter["anal"]  >= 7: # She loves it
            $ approval_bonus += 20
        elif Girl.action_counter["anal"]  >= 3: #You've done it before several times
            $ approval_bonus += 17
        elif Girl.action_counter["anal"] : #You've done it before
            $ approval_bonus += 15

        if Girl.addiction >= 75 and (Girl.event_counter["creampied"] + Girl.event_counter["anal_creampied"]) >=3: #She's really strung out and has creampied
            $ approval_bonus += 25
        elif Girl.addiction >= 75:
            $ approval_bonus += 15

        if Girl.lust > 85:
            $ approval_bonus += 10
        elif Girl.lust > 75: #She's really horny
            $ approval_bonus += 5

        if Girl.used_to_anal:
            $ approval_bonus += 10
        elif "anal" in Girl.recent_history:
            $ approval_bonus -= 20
        elif "anal" in Girl.daily_history:
            $ approval_bonus -= 10

        if action_context == "shift":
            $ approval_bonus += 10
        if "exhibitionist" in Girl.Traits:
            $ approval_bonus += (5*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.Traits:
            $ approval_bonus -= 40
    elif primary_action == "hotdog":
        if Girl.action_counter["hotdog"] >= 3: #You've done it before several times
            $ approval_bonus += 10
        elif Girl.action_counter["hotdog"]: #You've done it before
            $ approval_bonus += 5

        if Girl.lust > 85:
            $ approval_bonus += 10
        elif Girl.lust > 75: #She's really horny
            $ approval_bonus += 5
        if action_context == "shift":
            $ approval_bonus += 10
        if "exhibitionist" in Girl.Traits:
            $ approval_bonus += (3*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.Traits:
            $ approval_bonus -= 40

    if Girl.event_counter["forced"] and not Girl.Forced:
        $ approval_bonus -= 5*Girl.event_counter["forced"]

    if Taboo and "tabno" in Girl.daily_history:
        $ approval_bonus -= 10

    if "no_" + primary_action in Girl.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_" + primary_action in Girl.recent_history else 0

    return

label end_of_action_round(Girl, action):
    $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus

    if Player.focus >= 100 or Girl.lust >= 100:
        if Player.focus >= 100:
            call Player_Cumming(Girl)

            if "angry" in Girl.recent_history:
                if primary_action in sex_actions:
                    call expression Girl.Tag + "_Sex_Reset"
                else:
                    call expression Girl.Tag + "_Pos_Reset"

                return True

            $ Girl.change_stat("lust", 200, 5)

            if 100 > Girl.lust >= 70 and Girl.OCount < 2 and Girl.SEXP >= 20:
                $ Girl.AddWord(0, "unsatisfied", "unsatisfied")

            if Player.focus > 80:
                jump after_action

            $ line = "came"

        if Girl.lust >= 100:
            call Girl_Cumming(Girl)

            if action_context == "shift" or "angry" in Girl.recent_history:
                jump after_action

        if line == "came": #ex Player.focus <= 20:
            $ line = 0

            if not Player.semen:
                if primary_action in sex_actions:
                    "She's emptied you out, you'll need to take a break."
                    "You're pretty wiped, better stop for now."

                    jump after_action
                else:
                    "You're emptied out, you should probably take a break."

            if "unsatisfied" in Girl.recent_history:#And Rogue is unsatisfied,
                call girl_unsatisfied_menu(Girl, action)

    if Partner and Partner.lust >= 100:
        call Girl_Cumming(Partner)

    if primary_action in ["kiss", "fondle_thighs", "fondle_breasts", "eat_pussy", "suck_breasts", "fondle_ass", "insert_ass", "handjob", "footjob", "titjob"]:
        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0
    elif primary_action in ["blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

    if Girl.SEXP >= 100 or approval_check(Girl, 1200, "LO"):
        pass
    elif counter == (5 + Girl.action_counter[action]):
        call starting_to_get_bored_reactions(Girl, action)
    elif primary_action in ["fondle_pussy", "finger_ass", "dildo_pussy", "dildo_ass"] and Girl.lust >= 80:
        pass
    elif primary_action in ["fondle_breasts", "suck_breasts"] and Girl.lust >= 85:
        pass
    elif primary_action in fondle_actions and counter == (15 + Girl.action_counter[primary_action]) and Girl.SEXP >= 15 and not approval_check(Girl, 1500):
        call definitely_bored_now_reactions(Girl, primary_action)
    elif primary_action in ["handjob, footjob, titjob, blowjob", "sex", "anal", "hotdog"] and counter == (10 + Girl.action_counter[action]) and Girl.SEXP <= 100 and not approval_check(Girl, 1200, "LO"):
        call definitely_bored_now_reactions(Girl, primary_action)
    elif primary_action in ["kiss", "dildo_pussy", "dildo_ass"] and counter == (15 + Girl.action_counter[action]) and Girl.SEXP >= 15 and not approval_check(Girl, 1200, "LO"):
        call definitely_bored_now_reactions(Girl, primary_action)
    elif primary_action in ["footjob"] and counter == 20:
        call definitely_bored_now_reactions(Girl, primary_action)

    call Escalation(Girl)

    if Round == 10:
        call ten_rounds_left_lines(Girl)
    elif Round == 5:
        call five_rounds_left_lines(Girl)

    return False
