label set_approval_bonus(Girl, action, context):
    if action == "fondle_thighs":
        if Girl.action_counter["fondle_thighs"]:
            $ approval_bonus += 10

        if Girl.legs_covered:
            $ approval_bonus -= 5

        if Girl.lust > 75:
            $ approval_bonus += 10

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += taboo

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 25
    elif action == "fondle_breasts":
        if Girl.action_counter["fondle_breasts"]:
            $ approval_bonus += 15

        if Girl.lust > 75: #She's really horny
            $ approval_bonus += 20

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (3*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 20
    elif action == "suck_breasts":
        if Girl.action_counter["suck_breasts"]: #You've done it before
            $ approval_bonus += 15

        if not Girl.outfit["bra"] and not Girl.outfit["top"]:
            $ approval_bonus += 15

        if Girl.lust > 75: #She's really horny
            $ approval_bonus += 20

        if Girl.lust > 75 and context == "auto": #She's really horny
            $ approval_bonus += 10

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (4*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 25
    elif action == "fondle_pussy":
        if Girl.action_counter["fondle_pussy"]: #You've done it before
            $ approval_bonus += 20

        if Girl.legs_covered: # she's got pants on.
            $ approval_bonus -= 10

        if Girl.lust > 75: #She's really horny
            $ approval_bonus += 15

        if Girl.lust > 75 and context == "auto": #She's really horny
            $ approval_bonus += 10

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (2*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 25
    elif action == "eat_pussy":
        if Girl.action_counter["eat_pussy"]: #You've done it before
            $ approval_bonus += 15

        if Girl.legs_covered: # she's got pants on.
            $ approval_bonus -= 15

        if Girl.lust > 95:
            $ approval_bonus += 20
        elif Girl.lust > 85: #She's really horny
            $ approval_bonus += 15

        if Girl.lust > 85 and context == "auto": #She's really horny
            $ approval_bonus += 10

        if context == "shift":
            $ approval_bonus += 10

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (4*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 25
    elif action == "fondle_ass":
        if Girl.action_counter["fondle_ass"]: #You've done it before
            $ approval_bonus += 10

        if Girl.legs_covered: # she's got pants on.
            $ approval_bonus -= 5

        if Girl.lust > 75: #She's really horny
            $ approval_bonus += 15

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += taboo

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 25
    elif action == "finger_ass":
        if Girl.action_counter["finger_ass"]: #You've done it before
            $ approval_bonus += 25

        if Girl.legs_covered: # she's got pants on.
            $ approval_bonus -= 15

        if Girl.lust > 85 and Girl.used_to_anal: #She's really horny
            $ approval_bonus += 15

        if Girl.lust > 95 and Girl.used_to_anal:
            $ approval_bonus += 5

        if Girl.lust > 85 and context == "auto": #She's really horny
            $ approval_bonus += 10

        if context == "shift":
            $ approval_bonus += 10

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (4*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 25
    elif action == "eat_ass":
        if Girl.action_counter["eat_ass"]: #You've done it before
            $ approval_bonus += 20

        if Girl.legs_covered: # she's got pants on.
            $ approval_bonus -= 25

        if Girl.lust > 95:
            $ approval_bonus += 20
        elif Girl.lust > 85: #She's really horny
            $ approval_bonus += 15

        if Girl.lust > 85 and context == "auto": #auto
            $ approval_bonus += 10

        if context == "shift":
            $ approval_bonus += 10

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (4*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 25
    elif action == "handjob":
        if Girl.action_counter[action] >= 7: # She loves it
            $ approval_bonus += 10
        elif Girl.action_counter[action] >= 3: #You've done it before several times
            $ approval_bonus += 7
        elif Girl.action_counter[action]: #You've done it before
            $ approval_bonus += 3

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (3*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 40

        if Girl.addiction >= 75 and Girl.event_counter["swallowed"] >= 3: #She's really strung out and has swallowed
            $ approval_bonus += 15
        if Girl.addiction >= 75:
            $ approval_bonus += 5

        if context == "shift":
            $ approval_bonus += 15
    elif action == "footjob":
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

        if context == "shift":
            $ approval_bonus += 15
        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (3*taboo)
        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 40
    elif action == "titjob":
        if Girl.action_counter[action] >= 7: # She loves it
            $ approval_bonus += 10
        elif Girl.action_counter[action] >= 3: #You've done it before several times
            $ approval_bonus += 7
        elif Girl.action_counter[action]: #You've done it before
            $ approval_bonus += 5

        if Girl.seen_breasts and approval_check(Girl, 500): # You've seen her tits.
            $ approval_bonus += 10
        if not Girl.outfit["bra"] and not Girl.outfit["top"]: #She's already topless
            $ approval_bonus += 10

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (5*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 30

        if Girl.lust > 75: #She's really horny
            $ approval_bonus += 10

        if Girl.addiction >= 75 and Girl.event_counter["swallowed"] >= 3: #She's really strung out and has swallowed
            $ approval_bonus += 15
        if Girl.addiction >= 75:
            $ approval_bonus += 5

        if context == "shift":
            $ approval_bonus += 15
    elif action == "blowjob":
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

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (4*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 40

        if context == "shift":
            $ approval_bonus += 15
    elif action == "dildo_pussy":
        if Girl.action_counter[action]: #You've done it before
            $ approval_bonus += 15
        if Girl.legs_covered: # she's got pants on.
            $ approval_bonus -= 20

        if Girl.lust > 95:
            $ approval_bonus += 20
        elif Girl.lust > 85: #She's really horny
            $ approval_bonus += 15

        if context == "shift":
            $ approval_bonus += 10
        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (5*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 40
    elif action == "dildo_ass":
        if Girl.used_to_anal:
            $ approval_bonus += 30
        elif "anal" in Girl.recent_history or "dildo_ass" in Girl.recent_history:
            $ approval_bonus -= 20
        elif "anal" in Girl.daily_history or "dildo_ass" in Girl.daily_history:
            $ approval_bonus -= 10
        elif (Girl.action_counter["anal"] + Girl.action_counter["dildo_ass"]) > 0 or Girl.outfit["buttplug"]: #You've done it before
            $ approval_bonus += 20

        if Girl.legs_covered: # she's got pants on.
            $ approval_bonus -= 20

        if Girl.lust > 95:
            $ approval_bonus += 20
        elif Girl.lust > 85: #She's really horny
            $ approval_bonus += 15

        if context == "shift":
            $ approval_bonus += 10
        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (5*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 40
    elif action == "sex":
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

        if context == "shift":
            $ approval_bonus += 10
        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (4*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 40
    elif action == "anal":
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

        if context == "shift":
            $ approval_bonus += 10
        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (5*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 40
    elif action == "hotdog":
        if Girl.action_counter["hotdog"] >= 3: #You've done it before several times
            $ approval_bonus += 10
        elif Girl.action_counter["hotdog"]: #You've done it before
            $ approval_bonus += 5

        if Girl.lust > 85:
            $ approval_bonus += 10
        elif Girl.lust > 75: #She's really horny
            $ approval_bonus += 5
        if context == "shift":
            $ approval_bonus += 10
        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (3*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 40

    if Girl.event_counter["forced"] and not Girl.forced:
        $ approval_bonus -= 5*Girl.event_counter["forced"]

    if taboo and "no_taboo" in Girl.daily_history:
        $ approval_bonus -= 10

    if "no_" + action in Girl.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_" + action in Girl.recent_history else 0

    return approval_bonus

label end_of_action_round(Girl, action):
    $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus

    if Player.focus >= 100 or Girl.lust >= 100:
        $ orgasmed = False

        if Player.focus >= 100:
            call Player_Cumming(Girl)

            if "_angry" in Girl.recent_history:
                call reset_position(Girl)

                return [None, "stop"]

            $ Girl.change_stat("lust", 200, 5)

            if 100 > Girl.lust >= 70 and Girl.event_counter["orgasmed"] < 2 and Girl.SEXP >= 20:
                $ Girl.add_word(0, "unsatisfied", "unsatisfied")

            $ orgasmed = True

        if Girl.lust >= 100:
            call Girl_Cumming(Girl)

            if "_angry" in Girl.recent_history:
                return [None, "stop"]

        if orgasmed:
            if not Player.semen:
                if action in sex_actions:
                    $ line = renpy.random.choice(["She's emptied you out, you'll need to take a break."
                        "You're pretty wiped, better stop for now."])

                    "[line]"

                    return [None, "stop"]
                else:
                    "You're emptied out, you should probably take a break."

            if "unsatisfied" in Girl.recent_history:#And Rogue_sprite is unsatisfied,
                call girl_unsatisfied_menu(Girl, action)

                if _return == "stop":
                    return [None, "stop"]

    if Partner and Partner.lust >= 100:
        call Girl_Cumming(Partner)

    if action in ["kiss", "fondle_thighs", "fondle_breasts", "eat_pussy", "suck_breasts", "fondle_ass", "insert_ass", "handjob", "footjob", "titjob"]:
        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0
    elif action in ["blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

    if Girl.SEXP >= 100 or approval_check(Girl, 1200, "LO"):
        pass
    elif counter == (5 + Girl.action_counter[action]):
        call starting_to_get_bored_reactions(Girl, action)
    elif action in ["fondle_pussy", "finger_ass", "dildo_pussy", "dildo_ass"] and Girl.lust >= 80:
        pass
    elif action in ["fondle_breasts", "suck_breasts"] and Girl.lust >= 85:
        pass
    elif action in fondle_actions and counter == (15 + Girl.action_counter[action]) and Girl.SEXP >= 15 and not approval_check(Girl, 1500):
        call definitely_bored_now_reactions(Girl, action)

        if _return[1] != "continue":
            return _return
    elif action in ["handjob, footjob, titjob, blowjob", "sex", "anal", "hotdog"] and counter == (10 + Girl.action_counter[action]) and Girl.SEXP <= 100 and not approval_check(Girl, 1200, "LO"):
        call definitely_bored_now_reactions(Girl, action)

        if _return[1] != "continue":
            return _return
    elif action in ["kiss", "dildo_pussy", "dildo_ass"] and counter == (15 + Girl.action_counter[action]) and Girl.SEXP >= 15 and not approval_check(Girl, 1200, "LO"):
        call definitely_bored_now_reactions(Girl, action)

        if _return[1] != "continue":
            return _return
    elif action in ["footjob"] and counter == 20:
        call definitely_bored_now_reactions(Girl, action)

        if _return[1] != "continue":
            return _return

    call Escalation(Girl)

    if round == 10:
        call ten_rounds_left_lines(Girl, action)
    elif round == 5:
        call five_rounds_left_lines(Girl, action)

    return [None, "continue"]

label set_secondary_action(Girl):
    menu:
        "Also kiss her." if Player.primary_action not in mouth_actions and Player.secondary_action != "kiss":
            "You lean in and start kissing her."

            $ action = "kiss"
        "Also fondle her breasts." if "fondle_breasts" not in [Player.primary_action, Player.secondary_action]:
            $ action = "fondle_breasts"
        "Also suck her breasts." if Player.primary_action not in mouth_actions and Player.secondary_action != "suck_breasts":
            $ action = "suck_breasts"
        "Also fondle her pussy." if Player.primary_action not in ["fondle_pussy", "finger_pussy"] and Player.secondary_action not in ["fondle_pussy", "finger_pussy"]:
            $ action = "fondle_pussy"
        "Also finger her pussy." if Player.primary_action not in ["fondle_pussy", "finger_pussy"] and Player.secondary_action not in ["fondle_pussy", "finger_pussy"]:
            $ action = "finger_pussy"
        "Also fondle her ass." if "fondle_ass" not in [Player.primary_action, Player.secondary_action]:
            $ action = "fondle_ass"
        "Also finger her ass." if "finger_ass" not in [Player.primary_action, Player.secondary_action]:
            $ action = "finger_ass"
        "Also jack it." if Player.secondary_action != "jerking_off":
            call jerking_off(Girl)

            if _return == "stop":
                return "stop"
            else:
                return "continue"
        "Nevermind":
            return "continue"

    call set_approval_bonus(Girl, action, "offhand")
    $ approval_bonus = _return

    call action_approval_checks(Girl, action)
    $ approval = _return

    if Girl == EmmaX and action == "kiss" and not approval_check(Girl, 1000):
        $ Girl.change_face("_sadside")

        ch_e "Not when we barely know each other. . ."

        return "continue"

    call auto_action_narrations(Girl, action)

    if approval >= 2:
        call auto_approved_reactions(Girl, action)

        $ Player.secondary_action = action
    else:
        call auto_rejected_reactions(Girl, action)

        if _return == "accepted":
            $ Player.secondary_action = action
        else:
            $ Player.secondary_action = None

    return "continue"

label swap_actions(Girl):
    if Player.secondary_action in breast_actions:
        "You shift your attention to her breasts."
    elif Player.secondary_action in pussy_actions:
        "You shift your attention to her pussy."
    elif Player.secondary_action in ass_actions:
        "You shift your attention to her ass."
    elif Player.secondary_action == "kiss":
        "You go back to kissing her deeply."

    $ Player.primary_action, Player.secondary_action = Player.secondary_action, Player.primary_action

    return Player.primary_action

label jerking_off(Girl = None):
    if not Girl:
        python:
            for G in all_Girls:
                if G.location == bg_current:
                    Girl = G

                    break

    if "unseen" in Girl.recent_history:
        $ Player.recent_history.append("cockout")

        $ Player.secondary_action = "jerking_off"

        "You whip out your cock and start working it."
    else:
        if not Player.semen:
            "You don't think that would accomplish much, the poor thing is napping."

            return

        if "cockout" in Player.recent_history:
            "You start working your cock."
        else:
            "You whip out your cock and start working it."

            $ Player.recent_history.append("cockout")

            call Seen_First_Peen (Girl, Partner)

        $ Player.secondary_action = "jerking_off"

        if "jerking_off" in Girl.recent_history:
            return "continue"

        $ Girl.add_word(0,"jerking_off","jerking_off",0,0)

        if Girl == EmmaX and "classcaught" not in Girl.history:
            $ Girl.change_face("_surprised", 1)
            $ Girl.eyes = "_down"

            ch_e "Wait . ."

            $ Girl.change_face("_angry", 1)

            ch_e "That really isn't appropriate."

            $ Girl.change_stat("lust", 50, 7)

            if not approval_check(EmmaX, 1200, taboo_modifier = 3):
                $ Girl.add_word(0,"_angry","_angry",0,0)

                return "stop"

        if Girl.SEXP < 10 and Girl not in [JeanX, StormX]:
            $ Girl.change_face("_surprised", 2)
            $ Girl.eyes = "_down"

            if Girl == LauraX:
                $ Girl.brows = "_confused"

                "[Girl.name] seems perplexed that you would do something like that."
            else:
                "[Girl.name] blushes furiously, shocked at your behavior."

            $ Girl.change_face("_angry", 1)
            $ Girl.change_stat("lust", 50, 5)

            if not approval_check(Girl, 1200, taboo_modifier = 3):
                $ Girl.add_word(0,"_angry","_angry",0,0)

                return "stop"
        elif Girl.SEXP <= 15:
            $ Girl.change_face("_surprised", 2)
            $ Girl.eyes = "_down"

            if Girl == EmmaX:
                $ Girl.blushing = "_blush1"

                "[Girl.name] looks down at your cock with some surprise."

                $ Girl.change_stat("lust", 60, 2)
            else:
                "[Girl.name] looks down at your cock with surprise."

            $ Girl.change_face("_perplexed", 1)
            $ Girl.change_stat("lust", 60, 8)

            if not approval_check(Girl, 1200, taboo_modifier = 3) and Girl != JeanX:
                return "stop"
        elif approval_check(Girl, 1100, taboo_modifier = 3):
            $ Girl.change_face("_surprised", 1)
            $ Girl.eyes = "_down"

            "[Girl.name] looks down at your cock and smiles."

            $ Girl.change_face("_sly", 1)
            $ Girl.change_stat("lust", 70, 8,Alt=[[EmmaX],60,12])
        elif approval_check(Girl, 500, "I", taboo_modifier=2):
            $ Girl.change_face("_surprised", 1)
            $ Girl.eyes = "_down"

            "[Girl.name] glances at it, but just smiles in amusement."

            $ Girl.change_face("_sly", 1)
            $ Girl.change_stat("lust", 70, 10,Alt=[[EmmaX],60,15])
        else:
            $ Girl.change_face("_angry", 1)
            $ Girl.eyes = "_down"

            "[Girl.name] glances down at your cock with a scowl."

            $ Girl.eyes = "_sexy"
            $ Girl.add_word(0,"_angry","_angry",0,0)

            return "stop"

        if Girl.remaining_actions and Girl.location == bg_current:
            $ options = ["none"]

            $ counter = 0

            if Girl.action_counter["handjob"] >= 5 and approval_check(Girl, 1100, taboo_modifier = 3):
                $ counter = Girl.action_counter["handjob"] - 4
                $ counter = 10 if counter > 10 else counter

                while counter:
                    $ options.append("handjob")

                    $ counter -= 1

            if Girl.action_counter["blowjob"] >= 5 and approval_check(Girl, 1300, taboo_modifier = 3):
                $ counter = Girl.action_counter["blowjob"] - 4
                $ counter = 10 if counter > 10 else counter
                $ counter += 5 if "hungry" in Girl.traits else 0

                while counter:
                    $ options.append("blowjob")

                    $ counter -= 1

            if Girl.action_counter["titjob"] >= 5 and approval_check(Girl, 1200, taboo_modifier = 5):
                $ counter = Girl.action_counter["titjob"] - 4
                $ counter = 10 if counter > 10 else counter

                while counter:
                    $ options.append("titjob")

                    $ counter -= 1

            if Girl.action_counter["sex"] >= 5 and approval_check(Girl, 1400, taboo_modifier = 5):
                $ counter = Girl.action_counter["sex"] - 4
                $ counter = 10 if counter > 10 else counter
                $ counter += 5 if Girl.lust >= 70 else 0

                while counter:
                    $ options.append("sex")

                    $ counter -= 1

            if Girl.action_counter["anal"] >= 5 and approval_check(Girl, 1550, taboo_modifier = 5):
                $ counter = Girl.action_counter["anal"] - 4
                $ counter = 10 if counter > 10 else counter
                $ counter += 5 if Girl.lust >= 70 and Girl.used_to_anal else 0

                while counter:
                    $ options.append("anal")

                    $ counter -= 1

            $ renpy.random.shuffle(options)

            if options[0] == "handjob":
                if Girl == RogueX:
                    ch_r "Sure you don't want me to handle that for you?"
                elif Girl == KittyX:
                    ch_k "I could. . . lend you a hand?"
                elif Girl == EmmaX:
                    ch_e "Would you care for a hand with that?"
                elif Girl == LauraX:
                    ch_l "Did you want some help with that?"
                elif Girl == JeanX:
                    ch_j "Did you want a hand with that?"
                elif Girl == StormX:
                    ch_s "Did you want a hand?"
                elif Girl == JubesX:
                    ch_v "I could, uh, give you a hand there. . ."
            elif options[0] == "blowjob" or (Girl == JubesX and JubesX.action_counter["blowjob"]):
                if Girl == RogueX:
                    ch_r "Sure my mouth wouldn't do better?"
                elif Girl == KittyX:
                    ch_k "I could, get that wet for you. . ."
                elif Girl == EmmaX:
                    ch_e "I wouldn't mind a taste of that. . ."
                elif Girl == LauraX:
                    ch_l "Well that looks tasty. . ."
                elif Girl == JeanX:
                    ch_j "Well that looks delicious. . ."
                elif Girl == StormX:
                    ch_s "I could use a taste of that."
                elif Girl == JubesX:
                    $ Girl.change_face("_sly", 1, mouth = "_tongue")

                    ch_v "I uh, wouldn't mind giving that my full attention. . ."

                    $ Girl.mouth = "_smile"
            elif options[0] == "titjob":
                if Girl == RogueX:
                    ch_r "Sure you wouldn't prefer using these?"
                elif Girl == KittyX:
                    ch_k "My chest might keep that warm. . ."
                elif Girl == EmmaX:
                    ch_e "If you like, I could use my chest. . ."
                elif Girl == LauraX:
                    ch_l "I could use my tits. . ."
                elif Girl == JeanX:
                    ch_j "Did you want to use my tits with that?"
                elif Girl == StormX:
                    ch_s "Would you prefer these?"
                elif Girl == JubesX:
                    ch_v "I could use these. . ."
            elif options[0] == "sex":
                if Girl == RogueX:
                    ch_r "Oh, you're making me pretty wet here. . ."
                elif Girl == KittyX:
                    ch_k "I'm getting a little wet. . ."
                elif Girl == EmmaX:
                    ch_e "I'm positively dripping, you know. . ."
                elif Girl == LauraX:
                    ch_l "Well that's getting me wet. . ."
                elif Girl == JeanX:
                    ch_j "That's one way to get me wet. . ."
                elif Girl == StormX:
                    ch_s "Well that is one way to get me wet. . ."
                elif Girl == JubesX:
                    ch_v "I wouldn't mind sticking that in. . ."
            elif options[0] == "anal":
                if Girl == RogueX:
                    ch_r "You've really got my ass tingling. . ."
                elif Girl == KittyX:
                    ch_k "Why don't you bring that in through the back. . ."
                elif Girl == EmmaX:
                    ch_e "I wouldn't mind you using the back door. . ."
                elif Girl == LauraX:
                    ch_l "Why don't you stick that in me. . ."
                elif Girl == JeanX:
                    ch_j "I could use some attention around back. . ."
                elif Girl == StormX:
                    ch_s "I could use some help in back. . ."
                elif Girl == JubesX:
                    ch_v "I wouldn't mind taking that in the back. . ."
            else:
                if Girl == RogueX:
                    ch_r "I like what I'm seeing here. . ."
                elif Girl == KittyX:
                    ch_k "Prrrr. . ."
                elif Girl == EmmaX:
                    ch_e "Mmmmm. . ."
                elif Girl == LauraX:
                    ch_l "Prrrr. . ."
                elif Girl == JeanX:
                    ch_j "Oooh. . ."
                elif Girl == StormX:
                    ch_s "Hmmm. . ."
                elif Girl == JubesX:
                    ch_v "Ooohh. . ."
                return

            $ context = None

            menu:
                extend ""
                "No thanks, I've got this in hand.":
                    if Girl == RogueX:
                        ch_r "Your loss, [Girl.player_petname]."
                    elif Girl == KittyX:
                        ch_k "What ev, [Girl.player_petname]."
                    elif Girl == EmmaX:
                        $ Girl.change_face("_perplexed", 1)

                        ch_e "Oh. . ."
                        ch_e "Carry on then, [Girl.player_petname]."

                        $ Girl.change_face("_sly", 0,eyes="_down")
                    elif Girl == LauraX:
                        ch_l "Can't say I didn't offer."
                    elif Girl == JeanX:
                        ch_j "[[shrug]"
                    elif Girl == StormX:
                        ch_s "Your choice."
                    elif Girl == JubesX:
                        ch_v "Your call. . ."

                    return
                "Hmm, sounds like a plan.":
                    $ context = "shift"

                    $ Player.secondary_action = None

            if Player.primary_action == "striptease":
                call Group_Strip_End
            elif Player.primary_action == "masturbation":
                $ Girl.remaining_actions -= 1
                $ Girl.action_counter["masturbation"] += 1

                call checkout
            elif Player.primary_action:
                call after_action(Girl, Player.primary_action, "shift")

            call before_action(Girl, options[0], "shift")

    return "continue"

label girl_touches_you(Girl, forced = False):
    call shift_focus (Girl)

    $ gloves = Girl.outfit["gloves"]

    $ Girl.arm_pose = 2

    if not forced:
        $ Girl.eyes = "_closed"
        $ Girl.brows = "_sad"

    if forced and Player.level >= 5:
        if gloves == "_gloves":
            $ Girl.outfit["gloves"] = ""

            "She pulls off her gloves and reaches for your face."
        else:
            "She reaches out towards your face."

        menu:
            extend ""
            "Catch her arm [[refuse].":
                $ Girl.change_face("_surprised", 1)

                "As she reaches out, you bat her arm away. The brief contact isn't enough for her."

                $ Girl.change_face("_angry")
                $ Girl.change_stat("love", 80, -10)

                if Girl.addiction >= 80 and not approval_check(Girl, 400, "O",Alt=[[RogueX],600]):
                    $ Girl.eyes = "_manic"

                    "She lashes out and leaps at you, grabbing you by the chin."

                    $ Girl.eyes = "_sly"

                    if "no_tag" not in Girl.recent_history:
                        $ Girl.change_stat("obedience", 50, -5)
                        $ Girl.change_stat("inhibition", 30, 5)
                        $ Girl.change_stat("inhibition", 90, 1)

                    $ forced = True
                else:
                    if Girl == RogueX:
                        ch_r "Not cool, [Girl.player_petname]."
                    elif Girl == KittyX:
                        ch_k "[Girl.Like]so not cool, [Girl.player_petname]."
                    elif Girl == EmmaX:
                        ch_e "You don't want me as an enemy, [Player.name]."
                    elif Girl == LauraX:
                        ch_l "Don't push me, [Girl.player_petname]."
                    elif Girl == JeanX:
                        ch_j "You won't like me when I'm angry, [Girl.player_petname]."
                    elif Girl == StormX:
                        ch_s "Do not toy with me, [Girl.player_petname]."
                    elif Girl == JubesX:
                        ch_v "Please. . ."

                    if "no_tag" not in Girl.recent_history:
                        $ Girl.change_stat("obedience", 50, 5)
                        $ Girl.change_stat("obedience", 80, 5)

                    $ Girl.recent_history.append("no_tag")
                    $ Girl.daily_history.append("no_tag")
                    $ Girl.outfit["gloves"] = gloves
                    $ Girl.arm_pose = 1

                    return
            "Let her.":
                "She touches your face."
    else:
        $ Girl.addiction -= 10
        $ Girl.addiction_rate += 1 if Girl.addiction_rate < 5 else 0

        $ Girl.change_stat("lust", 90, 5)

        if gloves == "_gloves":
            $ Girl.outfit["gloves"] = ""

            $ line = "She pulls off her gloves and"
        else:
            $ line = "She reaches out and"

        if Girl == RogueX:
            "[line] touches your face for a moment."
        elif Girl == KittyX:
            "[line] grabs both sides of your face, looking intently into your eyes."
        elif Girl == EmmaX:
            "[line] rubs the back of her hand against your cheek."
        elif Girl == LauraX:
            "[line] grabs your face in one hand, firmly smooshing your cheeks together."
        elif Girl == JeanX:
            "[line] wraps her hand around the back of your neck."
        elif Girl == StormX:
            "[line] strokes her hand across your cheek."
        elif Girl == JubesX:
            "[line] strokes your neck and cups her hand under your jaw."

    $ Girl.blushing = "_blush2"

    if round <= 15:
        $ Girl.addiction -= 15 if Girl.addiction > 15 else Girl.addiction

    while Girl.addiction > 20 and round > 15:
        $ Girl.addiction_rate += 1 if Girl.addiction_rate < 5 else 0
        $ Girl.addiction -= 15

        $ round -= 5

        $ Girl.change_stat("lust", 90, 5)

        if Girl == RogueX:
            $ Girl.change_stat("lust", 90, 5)
        elif forced:
            $ Girl.change_stat("obedience", 50, 1)

        "She continues to touch you, and a slight shiver passes through her."

    if round <= 15:
        Girl.voice "I suppose we don't have time for any more than that."
    if gloves and not Girl.outfit["gloves"]:
        "Appearing sated, she puts her gloves back on."

    $ Girl.blushing = "_blush1"
    $ Girl.outfit["gloves"] = gloves
    $ Girl.arm_pose = 1
    $ Girl.change_face()

    if forced:
        $ Girl.recent_history.append("forced tag")
        $ Girl.daily_history.append("forced tag")

    $ Girl.recent_history.append("tag")
    $ Girl.daily_history.append("tag")

    return

label slap_ass(Girl):
    call shift_focus(Girl)
    call punch

    $ Girl.event_counter["ass_slapped"] += 1
    $ Girl.blushing = "_blush2" if taboo else 1

    if approval_check(Girl, 200, "O", taboo_modifier=1):
        $ Girl.change_face("_sexy", 1)
        $ Girl.mouth = "_surprised"
        $ Girl.change_stat("lust", 51, 3, 1)
        $ Girl.change_stat("lust", 80, 1)

        if Girl.recent_history.count("slap") < 4:
            $ Girl.change_stat("lust", 200, 1)

            if Girl.event_counter["ass_slapped"] <= 5:
                $ Girl.change_stat("obedience", 50, 2)

            if Girl.event_counter["ass_slapped"] <= 10:
                $ Girl.change_stat("obedience", 80, 1)

        "You slap her ass and she jumps with pleasure."
    else:
        $ Girl.change_face("_surprised", 1)

        if Girl.recent_history.count("slap") < 4:
            $ Girl.change_stat("obedience", 70, 2)
            $ Girl.change_stat("love", 50, -1)

        "You slap her ass and she looks back at you a bit startled."

    if Player.primary_action and Girl.lust >= 100:
        call Girl_Cumming (Girl)

    if taboo:
        if not approval_check(Girl, 800, taboo_modifier=2):
            if Girl.event_counter["ass_slapped"] <= 5:
                $ Girl.change_stat("obedience", 80, 2)
                $ Girl.change_stat("obedience", 50, 2)

            $ Girl.change_stat("love", 70, -2)
            $ Girl.change_stat("love", 50, -1)

            "She looks pretty mad though."
        elif not approval_check(Girl, 1500, taboo_modifier=2):
            if Girl.event_counter["ass_slapped"] <= 5:
                $ Girl.change_stat("obedience", 80, 2)

            $ Girl.change_stat("love", 70, -1)

            "She looks a bit embarrassed."
        else:
            $ Girl.change_face("_sexy")
            $ Girl.mouth = "_smile"

            if Girl.event_counter["ass_slapped"] <= 5:
                $ Girl.change_stat("obedience", 80, 1)

            "She gives you a naughty grin."

        $ Girl.blushing = "_blush1"

    if Girl.bottom_number() < 5 and Girl.underwear_number() < 5:
        if approval_check(Girl, 500, "O") and Girl.recent_history.count("slap") < 4:
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("lust", 200, 3)
        else:
            $ Girl.change_stat("lust", 80, 1)

        $ Girl.addiction -= 1

    $ Girl.recent_history.append("slap") if Girl.recent_history.count("slap") < 4 else Girl.recent_history
    $ Girl.daily_history.append("slap") if Girl.daily_history.count("slap") < 10 else Girl.daily_history

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
                call expose_bottom(Girl)

                $ line = 0

                if Girl.wearing_skirt:
                    $ line = Girl.name + " hikes up her skirt"
                elif Girl.outfit["bottom"]:
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
            if Player.secondary_action == "jerking_off":
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

            $ Girl.upskirt = True
        elif Girl.wearing_pants:
            "[Girl.name] grabs her dildo, pulling down her pants as she does."

            $ Girl.outfit["bottom"] = ""
        else:
            if action == "dildo_pussy":
                "[Girl.name] grabs her dildo, rubbing it suggestively against her crotch."
            elif action == "dildo_ass":
                "[Girl.name] grabs her dildo, rubbing is suggestively against her ass."

        $ Girl.seen_underwear = True

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

                $ Girl.upskirt = True
            elif Girl.wearing_pants:
                $ line = renpy.random.choice(["[Girl.name] turns and backs up against your cock, sliding her [Girl.outfit['bottom']] down as she does so.",
                    "[Girl.name] rolls back and pulls you against her, sliding her [Girl.outfit['bottom']] off as she does so.",
                    "[Girl.name] pushes you down and climbs on top of you, sliding her [Girl.outfit['bottom']] down as she does so.",
                    "[Girl.name] turns around, sliding her [Girl.outfit['bottom']] down as she does so.",
                    "[Girl.name] lays back, sliding her [Girl.outfit['bottom']] down as she does so."])

                "[line]"

                $ Girl.bottom_pulled_down
            elif Girl.wearing_shorts:
                $ line = renpy.random.choice(["[Girl.name] rolls onto her back and pulls you against her, sliding her shorts off as she does so."])

                "[line]"

                $ Girl.bottom_pulled_down
            else:
                $ line = renpy.random.choice(["[Girl.name] turns and backs up against your cock.",
                    "[Girl.name] rolls back and pulls you toward her.",
                    "[Girl.name] pushes you back and climbs on top of you.",
                    "[Girl.name] turns around and pulls you toward her."])
                "[line]"

            $ Girl.seen_underwear = True

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

                return "rejected"

    return "accepted"

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

label first_action_response(Girl, action, context):
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

    if not context:
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
    elif Girl.action_counter[action] < 3:
        $ Girl.change_face("_sexy", 1)
        $ Girl.brows = "_confused"
        $ Girl.mouth = "_kiss"

        call before_action_less_than_three_times_lines(Girl, action)
    else:
        $ Girl.change_face("_sexy", 1)
        $ Girl.arm_pose = 2

        call used_to_action_lines(Girl, action)

    return

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
    else:
        $ Girl.change_face("_bemused")

        call otherwise_not_interested_lines(Girl, action)

        if Girl in [RogueX, KittyX, EmmaX, StormX]:
            $ Girl.blushing = "_blush1"
        else:
            $ Girl.blushing = ""

    call begging_menu(Girl, action)

    if _return == "rejected":
        return "rejected"
    else:
        return _return

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

    return

label forced_action(Girl, action):
    call forced_approval_checks(Girl, action)
    $ approval = _return

    if approval > 1 or (approval and Girl.forced):
        call forced_but_not_unwelcome_reactions(Girl, action)

        if approval < 2:
            $ Girl.forced = True

        return "accepted"
    else:
        call forced_rejected_reactions(Girl, action)

        $ Girl.recent_history.append("no_" + action)
        $ Girl.daily_history.append("no_" + action)
        $ Girl.add_word(1, "_angry", "_angry")

        return "rejected"
