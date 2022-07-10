label set_approval_bonus(Girl, Action_type, context):
    if Action_type == "fondle_thighs":
        if Girl.permanent_History["fondle_thighs"]:
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
    elif Action_type == "fondle_breasts":
        if Girl.permanent_History["fondle_breasts"]:
            $ approval_bonus += 15

        if Girl.lust > 75: #She's really horny
            $ approval_bonus += 20

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (3*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 20
    elif Action_type == "suck_breasts":
        if Girl.permanent_History["suck_breasts"]: #You've done it before
            $ approval_bonus += 15

        if not Girl.Clothes["bra"] and not Girl.Clothes["top"]:
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
    elif Action_type == "fondle_pussy":
        if Girl.permanent_History["fondle_pussy"]: #You've done it before
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
    elif Action_type == "eat_pussy":
        if Girl.permanent_History["eat_pussy"]: #You've done it before
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
    elif Action_type == "fondle_ass":
        if Girl.permanent_History["fondle_ass"]: #You've done it before
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
    elif Action_type == "finger_ass":
        if Girl.permanent_History["finger_ass"]: #You've done it before
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
    elif Action_type == "eat_ass":
        if Girl.permanent_History["eat_ass"]: #You've done it before
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
    elif Action_type == "handjob":
        if Girl.permanent_History[Action_type] >= 7: # She loves it
            $ approval_bonus += 10
        elif Girl.permanent_History[Action_type] >= 3: #You've done it before several times
            $ approval_bonus += 7
        elif Girl.permanent_History[Action_type]: #You've done it before
            $ approval_bonus += 3

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (3*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 40

        if Girl.addiction >= 75 and Girl.permanent_History["swallowed"] >= 3: #She's really strung out and has swallowed
            $ approval_bonus += 15
        if Girl.addiction >= 75:
            $ approval_bonus += 5

        if context == "shift":
            $ approval_bonus += 15
    elif Action_type == "footjob":
        if Girl.permanent_History[Action_type] >= 7: # She loves it
            $ approval_bonus += 10
        elif Girl.permanent_History[Action_type] >= 3: #You've done it before several times
            $ approval_bonus += 7
        elif Girl.permanent_History[Action_type]: #You've done it before
            $ approval_bonus += 3

        if Girl.addiction >= 75 and Girl.permanent_History["swallowed"] > = 3: #She's really strung out and has swallowed
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
    elif Action_type == "titjob":
        if Girl.permanent_History[Action_type] >= 7: # She loves it
            $ approval_bonus += 10
        elif Girl.permanent_History[Action_type] >= 3: #You've done it before several times
            $ approval_bonus += 7
        elif Girl.permanent_History[Action_type]: #You've done it before
            $ approval_bonus += 5

        if Girl.seen_breasts and approval_check(Girl, 500): # You've seen her tits.
            $ approval_bonus += 10
        if not Girl.Clothes["bra"] and not Girl.Clothes["top"]: #She's already topless
            $ approval_bonus += 10

        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (5*taboo)

        if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
            $ approval_bonus += 10
        elif "ex" in Girl.traits:
            $ approval_bonus -= 30

        if Girl.lust > 75: #She's really horny
            $ approval_bonus += 10

        if Girl.addiction >= 75 and Girl.permanent_History["swallowed"] >= 3: #She's really strung out and has swallowed
            $ approval_bonus += 15
        if Girl.addiction >= 75:
            $ approval_bonus += 5

        if context == "shift":
            $ approval_bonus += 15
    elif Action_type == "blowjob":
        if Girl.permanent_History[Action_type] >= 7: # She loves it
            $ approval_bonus += 15
        elif Girl.permanent_History[Action_type] >= 3: #You've done it before several times
            $ approval_bonus += 10
        elif Girl.permanent_History[Action_type]: #You've done it before
            $ approval_bonus += 7

        if Girl.addiction >= 75 and Girl.permanent_History["swallowed"] > = 3: #She's really strung out and has swallowed
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
    elif Action_type == "dildo_pussy":
        if Girl.permanent_History[Action_type]: #You've done it before
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
    elif Action_type == "dildo_ass":
        if Girl.used_to_anal:
            $ approval_bonus += 30
        elif "anal" in Girl.recent_history or "dildo_ass" in Girl.recent_history:
            $ approval_bonus -= 20
        elif "anal" in Girl.daily_history or "dildo_ass" in Girl.daily_history:
            $ approval_bonus -= 10
        elif (Girl.permanent_History["anal"] + Girl.permanent_History["dildo_ass"]) > 0 or Girl.Clothes["buttplug"]: #You've done it before
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
    elif Action_type == "sex":
        if Girl.permanent_History["sex"] >= 7: # She loves it
            $ approval_bonus += 15
        elif Girl.permanent_History["sex"] >= 3: #You've done it before several times
            $ approval_bonus += 12
        elif Girl.permanent_History["sex"]: #You've done it before
            $ approval_bonus += 10

        if Girl.addiction >= 75 and (Girl.permanent_History["creampied"] + Girl.permanent_History["anal_creampied"]) > = 3: #She's really strung out and has creampied
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
    elif Action_type == "anal":
        if Girl.permanent_History["anal"]  >= 7: # She loves it
            $ approval_bonus += 20
        elif Girl.permanent_History["anal"]  >= 3: #You've done it before several times
            $ approval_bonus += 17
        elif Girl.permanent_History["anal"] : #You've done it before
            $ approval_bonus += 15

        if Girl.addiction >= 75 and (Girl.permanent_History["creampied"] + Girl.permanent_History["anal_creampied"]) > = 3: #She's really strung out and has creampied
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
    elif Action_type == "hotdog":
        if Girl.permanent_History["hotdog"] >= 3: #You've done it before several times
            $ approval_bonus += 10
        elif Girl.permanent_History["hotdog"]: #You've done it before
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

    if Girl.permanent_History["forced"] and not Girl.forced:
        $ approval_bonus -= 5*Girl.permanent_History["forced"]

    if taboo and "no_taboo" in Girl.daily_history:
        $ approval_bonus -= 10

    if "no_" + Action_type in Girl.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_" + Action_type in Girl.recent_history else 0

    return approval_bonus

label end_of_Action_round(Girl, Action_type):
    $ Player.climax = 50 if not Player.semen and Player.climax >= 50 else Player.focus

    if Player.climax >= 100 or Girl.lust >= 100:
        $ orgasmed = False

        if Player.climax >= 100:
            $ orgasmed = True

        if orgasmed:
            if not Player.semen:
                if Action_type in sex_Action_types:
                    $ line = renpy.random.choice(["She's emptied you out, you'll need to take a break."
                        "You're pretty wiped, better stop for now."])

                    "[line]"

                    return [None, "stop"]
                else:
                    "You're emptied out, you should probably take a break."

    if round == 10:
        call ten_rounds_left_lines(Girl, Action_type)
    elif round == 5:
        call five_rounds_left_lines(Girl, Action_type)

    return [None, "continue"]

label set_secondary_Action(Girl):
    menu:
        "Also kiss her." if Player.primary_Action.type not in mouth_Action_types and Player.secondary_Action.type != "kiss":
            "You lean in and start kissing her."

            $ Action_type = "kiss"
        "Also fondle her breasts." if "fondle_breasts" not in [Player.primary_Action.type, Player.secondary_Action.type]:
            $ Action_type = "fondle_breasts"
        "Also suck her breasts." if Player.primary_Action.type not in mouth_Action_types and Player.secondary_Action.type != "suck_breasts":
            $ Action_type = "suck_breasts"
        "Also fondle her pussy." if "fondle_pussy" not in [Player.primary_Action.type, Player.secondary_Action.type]:
            $ Action_type = "fondle_pussy"
        "Also finger her pussy." if Player.primary_Action.type not in pussy_insertion_Action_types and Player.secondary_Action.type not in pussy_insertion_Action_types:
            $ Action_type = "finger_pussy"
        "Also put a dildo in her pussy." if Player.primary_Action.type not in pussy_insertion_Action_types and Player.secondary_Action.type not in pussy_insertion_Action_types:
            $ Action_type = "dildo_pussy"
        "Also fondle her ass." if "fondle_ass" not in [Player.primary_Action.type, Player.secondary_Action.type]:
            $ Action_type = "fondle_ass"
        "Also finger her ass." if Player.primary_Action.type not in anal_insertion_Action_types and Player.secondary_Action.type not in anal_insertion_Action_types:
            $ Action_type = "finger_ass"
        "Also put a dildo in her ass." if Player.primary_Action.type not in anal_insertion_Action_types and Player.secondary_Action.type not in anal_insertion_Action_types:
            $ Action_type = "dildo_ass"
        "Never mind.":
            return "continue"

    $ Player.secondary_Action = ActionClass(Action_type, Target = Girl)

    return "continue"

label sex_over(put_clothes_on = True):
    call stop_all_Actions

    $ temp_Girls = Present[:]
    $ renpy.random.shuffle(temp_Girls)

    while temp_Girls:
        call show_full_body(temp_Girls[0])

        $ temp_Girls.remove(temp_Girls[0])

    if put_clothes_on:
        python:
            for G in Present:
                G.fix_clothing()

        call get_dressed

    $ checkout()
    call reset_player

    return

label slap_ass(Girl):
    call punch

    $ Girl.permanent_History["ass_slapped"] += 1

    return





label jerking_off(Girl = None):
    if not Girl:
        python:
            for G in all_Girls:
                if G.location == Player.location:
                    Girl = G

                    break

    if "unseen" in Girl.recent_history:
        $ Player.recent_history.append("cockout")

        $ Player.secondary_Action.type = "jerking_off"

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

        $ Player.secondary_Action.type = "jerking_off"

        if "jerking_off" in Girl.recent_history:
            return "continue"

        $ Girl.add_word(0, "jerking_off", "jerking_off", 0, 0)

        if Girl == EmmaX and "classcaught" not in Girl.history:
            $ Girl.change_face("surprised", 1)
            $ Girl.eyes = "down"

            ch_e "Wait . ."

            $ Girl.change_face("angry", 1)

            ch_e "That really isn't appropriate."

            call change_Girl_stat(Girl, "lust", 7)

            if not approval_check(EmmaX, 1200, taboo_modifier = 3):
                $ Girl.add_word(0, "angry", "angry", 0, 0)

                return "stop"

        if Girl.SEXP < 10 and Girl not in [JeanX, StormX]:
            $ Girl.change_face("surprised", 2)
            $ Girl.eyes = "down"

            if Girl == LauraX:
                $ Girl.brows = "confused"

                "[Girl.name] seems perplexed that you would do something like that."
            else:
                "[Girl.name] blushes furiously, shocked at your behavior."

            $ Girl.change_face("angry", 1)
            call change_Girl_stat(Girl, "lust", 5)

            if not approval_check(Girl, 1200, taboo_modifier = 3):
                $ Girl.add_word(0, "angry", "angry", 0, 0)

                return "stop"
        elif Girl.SEXP <= 15:
            $ Girl.change_face("surprised", 2)
            $ Girl.eyes = "down"

            if Girl == EmmaX:
                $ Girl.blushing = "_blush1"

                "[Girl.name] looks down at your cock with some surprise."

                call change_Girl_stat(Girl, "lust", 2)
            else:
                "[Girl.name] looks down at your cock with surprise."

            $ Girl.change_face("perplexed", 1)
            call change_Girl_stat(Girl, "lust", 8)

            if not approval_check(Girl, 1200, taboo_modifier = 3) and Girl != JeanX:
                return "stop"
        elif approval_check(Girl, 1100, taboo_modifier = 3):
            $ Girl.change_face("surprised", 1)
            $ Girl.eyes = "down"

            "[Girl.name] looks down at your cock and smiles."

            $ Girl.change_face("sly", 1)
            call change_Girl_stat(Girl, "lust", 12])
        elif approval_check(Girl, 500, "I", taboo_modifier=2):
            $ Girl.change_face("surprised", 1)
            $ Girl.eyes = "down"

            "[Girl.name] glances at it, but just smiles in amusement."

            $ Girl.change_face("sly", 1)
            call change_Girl_stat(Girl, "lust", 15])
        else:
            $ Girl.change_face("angry", 1)
            $ Girl.eyes = "down"

            "[Girl.name] glances down at your cock with a scowl."

            $ Girl.eyes = "sexy"
            $ Girl.add_word(0, "angry", "angry", 0, 0)

            return "stop"

        if Girl.remaining_Action_types and Girl.location == Player.location:
            $ options = ["none"]

            $ counter = 0

            if Girl.permanent_History["handjob"] >= 5 and approval_check(Girl, 1100, taboo_modifier = 3):
                $ counter = Girl.permanent_History["handjob"] - 4
                $ counter = 10 if counter > 10 else counter

                while counter:
                    $ options.append("handjob")

                    $ counter -= 1

            if Girl.permanent_History["blowjob"] >= 5 and approval_check(Girl, 1300, taboo_modifier = 3):
                $ counter = Girl.permanent_History["blowjob"] - 4
                $ counter = 10 if counter > 10 else counter
                $ counter += 5 if "hungry" in Girl.traits else 0

                while counter:
                    $ options.append("blowjob")

                    $ counter -= 1

            if Girl.permanent_History["titjob"] >= 5 and approval_check(Girl, 1200, taboo_modifier = 5):
                $ counter = Girl.permanent_History["titjob"] - 4
                $ counter = 10 if counter > 10 else counter

                while counter:
                    $ options.append("titjob")

                    $ counter -= 1

            if Girl.permanent_History["sex"] >= 5 and approval_check(Girl, 1400, taboo_modifier = 5):
                $ counter = Girl.permanent_History["sex"] - 4
                $ counter = 10 if counter > 10 else counter
                $ counter += 5 if Girl.lust >= 70 else 0

                while counter:
                    $ options.append("sex")

                    $ counter -= 1

            if Girl.permanent_History["anal"] >= 5 and approval_check(Girl, 1550, taboo_modifier = 5):
                $ counter = Girl.permanent_History["anal"] - 4
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
            elif options[0] == "blowjob" or (Girl == JubesX and JubesX.permanent_History["blowjob"]):
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
                    $ Girl.change_face("sly", 1, mouth = "tongue")

                    ch_v "I uh, wouldn't mind giving that my full attention. . ."

                    $ Girl.mouth = "smile"
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
                        $ Girl.change_face("perplexed", 1)

                        ch_e "Oh. . ."
                        ch_e "Carry on then, [Girl.player_petname]."

                        $ Girl.change_face("sly", 0, eyes = "down")
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

                    $ Player.secondary_Action.type = None

            if Player.primary_Action.type == "striptease":
                call Group_Strip_End
            elif Player.primary_Action.type == "masturbation":
                $ Girl.remaining_Action_types -= 1
                $ Girl.permanent_History["masturbation"] += 1

                $ checkout()
            elif Player.primary_Action.type:
                call after_Action_type(Girl, Player.primary_Action.type, "shift")

            call before_Action_type(Girl, options[0], "shift")

    return "continue"

label girl_touches_you(Girl, forced = False):
    $ shift_focus (Girl)

    $ gloves = Girl.Clothes["gloves"]

    $ Girl.arm_pose = 2

    if not forced:
        $ Girl.eyes = "closed"
        $ Girl.brows = "sad"

    if forced and Player.level >= 5:
        if gloves == "gloves":
            $ Girl.take_off("gloves")

            "She pulls off her gloves and reaches for your face."
        else:
            "She reaches out towards your face."

        menu:
            extend ""
            "Catch her arm [[refuse].":
                $ Girl.change_face("surprised", 1)

                "As she reaches out, you bat her arm away. The brief contact isn't enough for her."

                $ Girl.change_face("angry")
                call change_Girl_stat(Girl, "love", -10)

                if Girl.addiction >= 80 and not approval_check(Girl, 400, "O", Alt = [[RogueX], 600]):
                    $ Girl.eyes = "manic"

                    "She lashes out and leaps at you, grabbing you by the chin."

                    $ Girl.eyes = "squint"

                    if "no_tag" not in Girl.recent_history:
                        call change_Girl_stat(Girl, "obedience", -5)
                        call change_Girl_stat(Girl, "inhibition", 5)
                        call change_Girl_stat(Girl, "inhibition", 1)

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
                        call change_Girl_stat(Girl, "obedience", 5)
                        call change_Girl_stat(Girl, "obedience", 5)

                    $ Girl.recent_history.append("no_tag")
                    $ Girl.daily_history.append("no_tag")
                    $ Girl.Clothes["gloves"] = gloves
                    $ Girl.arm_pose = 1

                    return
            "Let her.":
                "She touches your face."
    else:
        $ Girl.addiction -= 10
        $ Girl.addiction_rate += 1 if Girl.addiction_rate < 5 else 0

        call change_Girl_stat(Girl, "lust", 5)

        if gloves == "gloves":
            $ Girl.take_off("gloves")

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

        call change_Girl_stat(Girl, "lust", 5)

        if Girl == RogueX:
            call change_Girl_stat(Girl, "lust", 5)
        elif forced:
            call change_Girl_stat(Girl, "obedience", 1)

        "She continues to touch you, and a slight shiver passes through her."

    if round <= 15:
        Girl.voice "I suppose we don't have time for any more than that."
    if gloves and not Girl.Clothes["gloves"]:
        "Appearing sated, she puts her gloves back on."

    $ Girl.blushing = "_blush1"
    $ Girl.Clothes["gloves"] = gloves
    $ Girl.arm_pose = 1
    $ Girl.change_face()

    if forced:
        $ Girl.recent_history.append("forced tag")
        $ Girl.daily_history.append("forced tag")

    $ Girl.recent_history.append("tag")
    $ Girl.daily_history.append("tag")

    return



label girl_initiates(Girl, Action_type):
    if Action_type == "kiss":
        "[Player.focused_Girl.name] presses her body against yours, and kisses you deeply."
    elif Action_type in breast_Action_types:
        if Action_type == "fondle_breasts":
            $ covered_phrase = "arm and shoves your hand against her covered breast"
            $ topless_phrase = "arm and shoves your hand against her breast"
        elif Action_type == "suck_breasts":
            $ covered_phrase = "head and shoves your face into her chest"
            $ topless_phrase = covered_phrase

        if (Girl.Clothes["top"] or Girl.Clothes["bra"]) and not Girl.top_pulled_up:
            if approval_check(Girl, 1250, taboo_modifier = 1) or (Girl.seen_breasts and approval_check(Girl, 500) and not taboo):
                $ Girl.top_pulled_up = 1

                $ line = Girl.Clothes["top"] if Girl.Clothes["top"] else Girl.Clothes["bra"]

                "With a mischievous grin, [Girl.name] pulls her [line] up over her breasts."

                call first_topless(Girl, silent = True)

                $ line = 0

                "She then grabs your [topless_phrase], clearly intending you to get to work."
            else:
                "[Girl.name] grabs your [covered_phrase], clearly intending you to get to work."
        else:
            "[Girl.name] grabs your [topless_phrase], clearly intending you to get to work."
    elif Action_type in ["fondle_pussy", "eat_pussy", "finger_ass"]:
        if Action_type == "fondle_pussy":
            if Girl in [JeanX, JubesX]:
                $ phrase = "grabs your arm and presses your hand into her crotch"
            elif Girl == StormX:
                $ phrase = "grabs your arm and strokes your hand across her crotch"
            else:
                $ phrase = "grabs your arm and shoves your hand into her crotch"
        elif Action_type == "eat_pussy":
            $ phrase = renpy.random.choice(["grabs your head and shoves your face into her crotch",
                "grabs your head and pulls it to her crotch",
                "grabs your head and wraps her thighs around it"])
        elif Action_type == "finger_ass":
            $ phrase = renpy.random.choice(["grabs your arm and presses your hand against her asshole",
                "grabs your arm and rubs your hand against her asshole"])


        if (Girl.Clothes["bottom"] and not Girl.upskirt) or (Girl.Clothes["underwear"] and not Girl.Clothes["underwear"].state):
            if approval_check(Girl, 1250, taboo_modifier = 1) or (Girl.seen_pussy and approval_check(Girl, 500) and not taboo):
                $ Girl.expose_pussy()

                $ line = 0

                if Girl.wearing_skirt:
                    $ line = Girl.name + " hikes up her skirt"
                elif Girl.Clothes["bottom"]:
                    $ line = Girl.name + " pulls down her " + Girl.Clothes["bottom"]
                else:
                    $ line = 0

                if Girl.Clothes["underwear"]:
                    if line:
                        "[line] and pulls her [Girl.Clothes[underwear].name] out of the way."
                        "She then [phrase], clearly intending you to get to work."
                    else:
                        "She pulls her [Girl.Clothes[underwear].name] out of the way, and then [phrase]."
                        "She clearly intends for you to get to work."
                else:
                    "[line], and then [phrase]."
                    "She clearly intends for you to get to work."

                call first_bottomless(Girl, 1)
            else:
                "[Girl.name] [phrase], clearly intending you to get to work."
        else:
            "[Girl.name] [phrase], clearly intending you to get to work."
    elif Action_type in job_Action_types:
        if Action_type == "handjob":
            if Player.secondary_Action.type == "jerking_off":
                "[Girl.name] brushes your hand aside and starts stroking your cock."
            else:
                "[Girl.name] gives you a mischevious smile, and starts to fondle your cock."
        elif Action_type == "footjob":
            "[Girl.name] leans forward and starts rubbing your cock between her feet."
        elif Action_type == "titjob":
            "[Girl.name] slides down and sandwiches your dick between her tits."
        elif Action_type == "blowjob":
            "[Girl.name] slides down and gives your cock a little lick."
    elif Action_type in dildo_Action_types:
        if Girl.wearing_skirt:
            "[Girl.name] grabs her dildo, hiking up her skirt as she does."

            $ Girl.upskirt = True
        elif Girl.wearing_pants:
            "[Girl.name] grabs her dildo, pulling down her pants as she does."

            $ Girl.Outfit.remove_Clothing(["pants", "skirt"])
        else:
            if Action_type == "dildo_pussy":
                "[Girl.name] grabs her dildo, rubbing it suggestively against her crotch."
            elif Action_type == "dildo_ass":
                "[Girl.name] grabs her dildo, rubbing is suggestively against her ass."

        $ Girl.seen_underwear = True

        if Action_type == "dildo_pussy":
            "She slides the tip along her pussy and seems to want you to insert it."
        elif Action_type == "dildo_ass":
            "She slides the tip against her asshole, and seems to want you to insert it."
    elif Action_type in sex_Action_types:
        if Action_type in ["sex", "anal"]:
            if Girl.wearing_skirt:
                $ line = renpy.random.choice(["[Girl.name] turns and backs up against your cock, sliding her skirt up as she does so.",
                    "[Girl.name] rolls back and pulls you toward her, sliding her skirt up as she does so.",
                    "[Girl.name] turns around, sliding her skirt up as she does so.",
                    "[Girl.name] pushes you back and climbs on top of you, sliding her skirt up as she does so.",
                    "[Girl.name] lays back, sliding her skirt up as she does so."])

                "[line]"

                $ Girl.upskirt = True
            elif Girl.wearing_pants:
                $ line = renpy.random.choice(["[Girl.name] turns and backs up against your cock, sliding her [Girl.Clothes[bottom].name] down as she does so.",
                    "[Girl.name] rolls back and pulls you against her, sliding her [Girl.Clothes[bottom].name] off as she does so.",
                    "[Girl.name] pushes you down and climbs on top of you, sliding her [Girl.Clothes[bottom].name] down as she does so.",
                    "[Girl.name] turns around, sliding her [Girl.Clothes[bottom].name] down as she does so.",
                    "[Girl.name] lays back, sliding her [Girl.Clothes[bottom].name] down as she does so."])

                "[line]"

                $ Girl.Clothes["pants"].state
            elif Girl.wearing_shorts:
                $ line = renpy.random.choice(["[Girl.name] rolls onto her back and pulls you against her, sliding her shorts off as she does so."])

                "[line]"

                $ Girl.Clothes["pants"].state
            else:
                $ line = renpy.random.choice(["[Girl.name] turns and backs up against your cock.",
                    "[Girl.name] rolls back and pulls you toward her.",
                    "[Girl.name] pushes you back and climbs on top of you.",
                    "[Girl.name] turns around and pulls you toward her."])
                "[line]"

            $ Girl.seen_underwear = True

            if Action_type == "sex":
                $ line = renpy.random.choice(["She slides the tip along her pussy and seems to want you to insert it."])
                "[line]"
            elif Action_type == "anal":
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

    if Action_type == "kiss":
        $ Action_type_line = "You lean in to the kiss"
        $ praise_line = "Mmm, this is a nice surprise, " + Girl.player_petname
        $ no_Action_type_line = "You pull back."
        $ reject_line = "Let's not do that right now, " + Girl.player_petname
    elif Action_type in ["fondle_breasts", "suck_breasts", "fondle_pussy", "eat_pussy", "finger_ass", "handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
        if Action_type == "fondle_breasts":
            $ Action_type_line = "You start to fondle them."
            $ praise_line = "I like the initiative, " + Girl.player_petname
            $ no_Action_type_line = "You pull your hand back."
            $ reject_line = "Let's not do that right now, " + Girl.player_petname
            $ rejection_response_line = Girl.name + " pulls back."
        elif Action_type == "suck_breasts":
            $ Action_type_line = "You start to run your tongue along her nipple."
            $ praise_line = "Mmm, I like this, " + Girl.player_petname
            $ no_Action_type_line = "You pull your head back."
            $ reject_line = "Let's not do that right now, " + Girl.player_petname
            $ rejection_response_line = Girl.name + " pulls away."
        elif Action_type == "fondle_pussy":
            $ Action_type_line = "You start to run your fingers along her pussy."
            $ praise_line = "I like the initiative, " + Girl.player_petname
            $ no_Action_type_line = "You pull your hand back."
            $ reject_line = "Let's not do that right now, " + Girl.player_petname
            $ rejection_response_line = Girl.name + " pulls back."
        elif Action_type == "eat_pussy":
            $ Action_type_line = "You start licking her slit."
            $ praise_line = "Mmm, I like this idea, " + Girl.player_petname
            $ no_Action_type_line = "You pull your head away."
            $ reject_line = "Let's not do that right now, " + Girl.player_petname
            $ rejection_response_line = Girl.name + " pulls back."
        elif Action_type == "finger_ass":
            $ Action_type_line = "You press your finger into her tight ass."
            $ praise_line = "Dirty girl, " + Girl.player_petname
            $ no_Action_type_line = "You pull your hand back."
            $ reject_line = "Let's not do that right now, " + Girl.player_petname
            $ rejection_response_line = Girl.name + " pulls back."
        elif Action_type == "handjob":
            $ Action_type_line = "[Girl.name] continues her Action_types."
            $ praise_line = "Oooh, that's good, [Girl.player_petname]."
            $ no_Action_type_line = None
            $ reject_line = "Let's not do that for now, [Girl.player_petname]."
            $ rejection_response_line = "[Girl.name] puts it down."
        elif Action_type == "footjob":
            $ Action_type_line = "[Girl.name] continues her Action_types."
            $ praise_line = "Oooh, that's good, [Girl.player_petname]."
            $ no_Action_type_line = None
            $ reject_line = "Let's not do that for now, [Girl.player_petname]."
            $ rejection_response_line = "[Girl.name] puts it down."
        elif Action_type == "titjob":
            $ Action_type_line = "[Girl.name] starts to slide them up and down."
            $ praise_line = "Oh, that sounds like a good idea, [Girl.player_petname]."
            $ no_Action_type_line = None
            $ reject_line = "Let's not do that for now, [Girl.player_petname]."
            $ rejection_response_line = "[Girl.name] lets it drop out from between her breasts."
        elif Action_type == "blowjob":
            $ Action_type_line = "[Girl.name] continues licking at it."
            $ praise_line = "Hmmm, keep doing that, [Girl.player_petname]."
            $ no_Action_type_line = None
            $ reject_line = "Let's not do that for now, [Girl.player_petname]."
            $ rejection_response_line = "[Girl.name] puts it down."
        elif Action_type == "dildo_pussy":
            $ Action_type_line = "[Girl.name] slides it in."
            $ praise_line = "Oh yeah, [Girl.player_petname], let's do this."
            $ no_Action_type_line = None
            $ reject_line = "Let's not do that for now, [Girl.player_petname]."
            $ rejection_response_line = "[Girl.name] sets the dildo down."
        elif Action_type == "dildo_ass":
            $ Action_type_line = "[Girl.name] slides it in."
            $ praise_line = "Hmmm, keep doing that, [Girl.player_petname]."
            $ no_Action_type_line = None
            $ reject_line = "Let's not do that for now, [Girl.player_petname]."
            $ rejection_response_line = "[Girl.name] sets the dildo down."
        elif Action_type == "sex":
            $ Action_type_line = "[Girl.name] slides it in."
            $ praise_line = "Oh yeah, [Girl.player_petname], let's do this."
            $ no_Action_type_line = None
            $ reject_line = "Let's not do that for now, [Girl.player_petname]."
            $ rejection_response_line = "[Girl.name] pulls back."
        elif Action_type == "anal":
            $ Action_type_line = "[Girl.name] slides it in."
            $ praise_line = "Ooo, dirty girl, [Girl.player_petname], let's do this."
            $ no_Action_type_line = None
            $ reject_line = "Let's not do that for now, [Girl.player_petname]."
            $ rejection_response_line = "[Girl.name] pulls back."
        elif Action_type == "hotdog":
            $ Action_type_line = renpy.random.choice([Girl.name + " starts to grind against you",
                Girl.name + " keeps grinding",
                Girl.name + " continues to grind"])
            $ praise_line = "Hmmm, that's good, [Girl.player_petname]."
            $ no_Action_type_line = None
            $ reject_line = "Let's not do that for now, [Girl.player_petname]."
            $ rejection_response_line = "[Girl.name] pulls back."

        menu:
            "What do you do?"
            "Get to work." if Action_type in ["fondle_breasts", "suck_breasts", "fondle_pussy", "eat_pussy", "finger_ass"]:
                call change_Girl_stat(Girl, "inhibition", 3)
                call change_Girl_stat(Girl, "inhibition", 2)

                "[Action_type_line]"
            "Nothing." if Action_type in job_Action_types:
                call change_Girl_stat(Girl, "inhibition", 3)
                call change_Girl_stat(Girl, "inhibition", 2)

                "[Action_type_line]"
            "Go with it." if Action_type in sex_Action_types:
                if Action_type in ["sex", "anal"]:
                    call change_Girl_stat(Girl, "inhibition", 3)
                    call change_Girl_stat(Girl, "inhibition", 2)
                elif Action_type in ["hotdog"]:
                    call change_Girl_stat(Girl, "inhibition", 3)

                "[Action_type_line]"
            "Go for it." if Action_type in dildo_Action_types:
                $ Girl.change_face("sexy", 1)
                call change_Girl_stat(Girl, "inhibition", 3)

                ch_p "[praise_line]"

                $ Girl.name_check() #checks reAction_type to petname

                "You grab the dildo and slide it in."

                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "obedience", 1)
                call change_Girl_stat(Girl, "obedience", 2)
            "Praise her." if Action_type not in dildo_Action_types:
                $ Girl.change_face("sexy", 1)

                if Action_type in ["fondle_breasts", "suck_breasts", "fondle_pussy", "eat_pussy", "finger_ass", "dildo_pussy", "dildo_ass", "sex", "anal"]:
                    call change_Girl_stat(Girl, "inhibition", 3)
                elif Action_type in job_Action_types:
                    call change_Girl_stat(Girl, "inhibition", 3)
                elif Action_type in ["hotdog"]:
                    call change_Girl_stat(Girl, "inhibition", 2)

                ch_p "[praise_line]"

                $ Girl.name_check() #checks reAction_type to petname

                "[Action_type_line]"

                if Action_type in ["fondle_breasts", "suck_breasts", "fondle_pussy", "eat_pussy", "finger_ass", "dildo_pussy", "dildo_ass", "sex", "anal"]:
                    call change_Girl_stat(Girl, "love", 1)
                elif Action_type in ["handjob", "footjob", "titjob", "blowjob", "hotdog"]:
                    call change_Girl_stat(Girl, "love", 1)

                call change_Girl_stat(Girl, "obedience", 1)
                call change_Girl_stat(Girl, "obedience", 2)
            "Ask her to stop.":
                if no_Action_type_line is not None:
                    "[no_Action_type_line]"

                $ Girl.change_face("surprised")
                call change_Girl_stat(Girl, "inhibition", 1)

                ch_p "[reject_line]"

                $ Girl.name_check() #checks reAction_type to petname

                if Girl == JeanX:
                    call change_Girl_stat(Girl, "love", -4)

                "[rejection_response_line]"

                if Action_type not in ["hotdog"]:
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "obedience", 2)
                else:
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "obedience", 2)

                $ Player.recent_history.append("nope")

                $ Girl.add_word(1, "refused", "refused")

                return "rejected"

    return "accepted"

label first_Action_approval(Girl, Action_type):
    if Girl.forced:
        call first_Action_approval_forced_reactions(Girl, Action_type)
    elif Girl.love >= (Girl.obedience + Girl.inhibition):
        call first_Action_approval_mostly_love_reactions(Girl, Action_type)
    elif Girl.obedience >= Girl.inhibition:
        call first_Action_approval_mostly_obedience_reactions(Girl, Action_type)
    elif Action_type in cock_Action_types and Girl.addiction >= 50:
        call first_Action_approval_addicted_reactions(Girl, Action_type)
    else:
        call first_Action_approval_reactions(Girl, Action_type)

    return

label first_Action_type_response(Girl, Action_type, context):
    if Action_type == "kiss":
        $ Girl.SEXP += 1

        if Girl == JubesX:
            "[Player.focused_Girl.name] bites your lip as she pulls back, and licks some blood off her lips."

            ch_v "Sorry about that. . ."
            ch_v "Won't happen again."
    if Action_type == "fondle_thighs":
        $ Girl.SEXP += 3
    elif Action_type in ["fondle_breasts", "suck_breasts", "fondle_ass"]:
        $ Girl.SEXP += 4
    elif Action_type in ["fondle_pussy"]:
        $ Girl.SEXP += 7
    elif Action_type in ["finger_pussy", "eat_pussy", "handjob", "footjob", "dildo_pussy", "hotdog"]:
        $ Girl.SEXP += 10
    elif Action_type in ["finger_ass", "titjob"]:
        $ Girl.SEXP += 12
    elif Action_type in ["eat_ass", "blowjob"]:
        $ Girl.SEXP += 15
    elif Action_type in ["sex"]:
        $ Girl.SEXP += 20
    elif Action_type in ["anal"]:
        $ Girl.SEXP += 25

    if not context:
        if Girl.love >= 500 and "unsatisfied" not in Girl.recent_history:
            $ Girl.mouth = "smile"
            call satisfied_lines(Girl, Action_type)
        elif Action_type in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass", "dildo_pussy", "dildo_ass"] and Girl.obedience <= 500 and Player.climax <= 20:
            $ Girl.change_face("perplexed", 1)

            call was_that_enough_lines(Girl, Action_type)
        elif Action_type in cock_Action_types and Player.climax <= 20:
            $ Girl.mouth = "sad"

            call was_that_enough_lines(Girl, Action_type)

    return

label Action_specific_consequences(Girl, Action_type):
    $ achievement = None

    $ Girl.permanent_History[Action_type] += 1

    if Action_type == "kiss":
        call Partner_Like(Girl, 1)
    if Action_type == "fondle_thighs":
        call Partner_Like(Girl, 1, 0)
    elif Action_type in ["fondle_breasts", "suck_breasts", "fondle_pussy", "finger_pussy", "fondle_ass", "finger_ass", "eat_ass"]:
        call Partner_Like(Girl, 2)
    elif Action_type == "eat_pussy":
        if Girl == RogueX and Partner == EmmaX:
            call Partner_Like(Girl,4,3)
        elif Girl not in [KittyX, StormX] and Partner == RogueX:
            call Partner_Like(Girl, 3, 3)
        elif Girl == RogueX:
            call Partner_Like(Girl,3, 2)
        else:
            call Partner_Like(Girl, 2)
    elif Action_type == "handjob":
        $ achievement = Girl.tag + " Handi-Queen"

        call Partner_Like(Girl, 2)
    elif Action_type == "footjob":
        $ achievement = Girl.tag + "_pedi"

        call Partner_Like(Girl, 1)
    elif Action_type == "titjob":
        call Partner_Like(Girl, 3)
    elif Action_type == "blowjob":
        $ achievement = Girl.tag + " Jobber"

        if Girl == RogueX and Partner == EmmaX:
            call Partner_Like(Girl, 3)
        else:
            call Partner_Like(Girl, 2)
    elif Action_type in dildo_Action_types:
        call Partner_Like(Girl, 2)
    elif Action_type == "sex":
        $ achievement = Girl.tag + " Sex Addict"

        call Partner_Like(Girl, 3, 2)
    elif Action_type == "anal":
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
    elif Action_type == "hotdog":
        $ achievement = Girl.tag + " Full Buns"

        if Girl == RogueX:
            call Partner_Like(Girl, 1)
        elif Girl in [KittyX, EmmaX, LauraX]:
            call Partner_Like(Girl, 2)

    call Action_type_specific_changes(Girl, Action_type)

    return

label Action_type_approved(Girl, Action_type):
    $ Girl.change_face("sexy", 1)

    if Girl.forced:
        $ Girl.change_face("sad")
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "love", 1)

        call Action_type_forcefully_approved_lines(Girl, Action_type)
    elif not taboo and "no_taboo" in Girl.daily_history:
        call private_enough_lines(Girl, Action_type)
    elif Girl.permanent_History[Action_type] < 3:
        $ Girl.change_face("sexy", 1)
        $ Girl.brows = "confused"
        $ Girl.mouth = "kiss"

        call before_Action_type_less_than_three_times_lines(Girl, Action_type)
    else:
        $ Girl.change_face("sexy", 1)
        $ Girl.arm_pose = 2

        call used_to_Action_type_lines(Girl, Action_type)

    return

label Action_type_disapproved(Girl, Action_type):
    if Action_type in fondle_Action_types:
        $ Girl.change_face("angry", 1)
    elif Action_type in ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "sex"]:
        $ Girl.change_face("angry")
    elif Action_type in ["finger_pussy"]:
        $ Girl.change_face("bemused", 2)

    if "no_" + Action_type in Girl.recent_history:
        call said_no_recently_lines(Girl, Action_type)
    elif taboo and "no_taboo" in Girl.daily_history and "no_" + Action_type in Girl.daily_history:
        call taboo_and_said_no_today_lines(Girl, Action_type)
    elif "no_" + Action_type in Girl.daily_history:
        call said_no_today_lines(Girl, Action_type)
    elif taboo and "no_taboo" in Girl.daily_history:
        call taboo_lines(Girl, Action_type)
    elif not Girl.permanent_History[Action_type]:
        $ Girl.change_face("bemused")

        call Action_type_not_done_yet_lines(Girl, Action_type)
    elif Action_type in anal_insertion_Action_types and not Girl.used_to_anal and Action_type not in Girl.daily_history:
        $ Girl.change_face("perplexed")

        call anal_insertion_not_loose_lines(Girl, Action_type)
    else:
        $ Girl.change_face("bemused")

        call otherwise_not_interested_lines(Girl, Action_type)

        if Girl in [RogueX, KittyX, EmmaX, StormX]:
            $ Girl.blushing = "_blush1"
        else:
            $ Girl.blushing = ""

    call begging_menu(Girl, Action_type)

    if _return == "rejected":
        return "rejected"
    else:
        return _return

label Action_type_accepted(Girl, Action_type):
    $ Girl.change_face("bemused", 1)

    if Action_type in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy"]:
        if Girl.forced:
            $ Girl.change_face("sad")

            call forced_Action_type_accepted_changes(Girl, Action_type)

        call Action_type_accepted_enthusiastically_lines(Girl, Action_type)
    else:
        if Girl.forced:
            $ Girl.change_face("sad")

            call forced_Action_type_accepted_changes(Girl, Action_type)
            call Action_type_forcefully_accepted_lines(Girl, Action_type)
        elif "no_" + Action_type in Girl.daily_history:
            call convinced_after_saying_no_lines(Girl, Action_type)
        else:
            if Action_type in ["fondle_ass"]:
                $ Girl.change_face("bemused", 1)
            else:
                $ Girl.change_face("sexy", 1)

            call not_forced_Action_type_accepted_changes(Girl, Action_type)
            call accepted_without_question_lines(Girl, Action_type)

    call Action_type_accepted_changes(Girl, Action_type)

    return

label Action_type_rejected(Girl, Action_type):
    $ Girl.arm_pose = 1

    if "no_" + Action_type in Girl.daily_history:
        $ Girl.change_face("angry", 1)

        call Action_type_already_rejected_lines(Girl, Action_type)

        $ Girl.add_word(1, "angry", "angry")
    elif Girl.forced:
        call forced_Action_type_rejected_reactions(Girl, Action_type)

        $ Girl.add_word(1, "angry", "angry")
    elif taboo:
        call taboo_Action_type_rejected_reactions(Girl, Action_type)

        $ Girl.add_word(1, "no_taboo", "no_taboo")
    elif Action_type in anal_insertion_Action_types and not Girl.used_to_anal and Action_type in Girl.daily_history:
        call anal_insertion_not_loose_done_today_reactions(Girl, Action_type)
    elif Girl.permanent_History[Action_type]:
        $ Girl.change_face("sad")

        call previous_Action_type_rejected_lines(Girl, Action_type)
    else:
        call otherwise_rejected_reactions(Girl, Action_type)

    $ Girl.recent_history.append("no_" + Action_type)
    $ Girl.daily_history.append("no_" + Action_type)

    return

label forced_Action_type(Girl, Action_type):
    call forced_approval_checks(Girl, Action_type)
    $ approval = _return

    if approval > 1 or (approval and Girl.forced):
        call forced_but_not_unwelcome_reactions(Girl, Action_type)

        if approval < 2:
            $ Girl.forced = True

        return "accepted"
    else:
        call forced_rejected_reactions(Girl, Action_type)

        $ Girl.recent_history.append("no_" + Action_type)
        $ Girl.daily_history.append("no_" + Action_type)
        $ Girl.add_word(1, "angry", "angry")

        return "rejected"
