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

    return

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

                if _return != "continue":
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

label set_offhand_action(Girl, shift = False):
    if shift:
        $ temp = offhand_action

        $ offhand_action = primary_action
        $ primary_action = temp

        if primary_action == "fondle_breasts":
            "You shift your attention to her breasts."
        elif primary_action == "suck_breasts":
            "You shift your attention to her breasts."
        elif primary_action == "fondle_pussy":
            "You shift your attention to her pussy."
        elif primary_action == "eat_pussy":
            "You shift your attention to her pussy."
        elif primary_action == "fondle_ass":
            "You shift your attention to her ass."
        elif primary_action == "finger_ass":
            "You shift your attention to her ass."
        elif primary_action == "kiss":
            "You go back to kissing her deeply."

        return [primary_action, "shift"]
    elif primary_action:
        menu:
            "Also kiss her." if primary_action not in mouth_actions:
                "You lean in and start kissing her."
                $ offhand_action = "kiss"

                return [offhand_action, "offhand"]
            "Also fondle her breasts." if primary_action != "fondle_breasts":
                $ offhand_action = "fondle_breasts"

                return [offhand_action, "offhand"]
            "Also suck her breasts." if primary_action not in mouth_actions:
                $ offhand_action = "suck_breasts"

                return [offhand_action, "offhand"]
            "Also fondle her pussy." if primary_action not in ["fondle_pussy", "finger_pussy"]:
                $ offhand_action = "fondle_pussy"

                return [offhand_action, "offhand"]
            "Also finger her pussy." if primary_action not in ["fondle_pussy", "finger_pussy"]:
                $ offhand_action = "finger_pussy"

                return [offhand_action, "offhand"]
            "Also fondle her ass." if primary_action != "fondle_ass":
                $ offhand_action = "fondle_ass"

                return [offhand_action, "offhand"]
            "Also finger her ass." if primary_action != "finger_ass":
                $ offhand_action = "finger_ass"

                return [offhand_action, "offhand"]
            "Also jack it." if offhand_action != "jerking_off":
                call jerking_off(Girl)

                if _return == "stop":
                    return "stop"
            "Nevermind":
                pass

    return "continue"

label jerking_off(Girl = None):
    if not Girl:
        python:
            for G in all_Girls:
                if G.location == bg_current:
                    Girl = G

                    break

    if "unseen" in Girl.recent_history:
        $ Player.recent_history.append("cockout")

        $ offhand_action = "jerking_off"

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

        $ offhand_action = "jerking_off"

        if "jerking_off" in Girl.recent_history:
            return

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

                    $ offhand_action = None

            if primary_action == "striptease":
                call Group_Strip_End
            elif primary_action == "masturbation":
                $ Girl.remaining_actions -= 1
                $ Girl.action_counter["masturbation"] += 1

                call checkout
            elif primary_action:
                call after_action(Girl, primary_action, "shift")

            call before_action(Girl, options[0], "shift")

    return

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

    if primary_action and Girl.lust >= 100:
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
