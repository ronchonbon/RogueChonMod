
label jerking_off(Girl=0, counter=0, temp_Girls=[]):


    if not Girl or Girl not in all_Girls:
        $ temp_Girls = all_Girls[:]
        while temp_Girls:
            if temp_Girls[0].location == bg_current:
                $ Girl = temp_Girls[0]
                $ temp_Girls = [1]
            $ temp_Girls.remove(temp_Girls[0])

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
            ch_e "wait. . ."
            $ Girl.change_face("_angry", 1)
            ch_e "That really isn't appropriate."
            $ Girl.change_stat("lust", 50, 7)
            if not approval_check(EmmaX, 1200, TabM = 3):
                $ Girl.add_word(0,"_angry","_angry",0,0)
                $ renpy.pop_call()
                return

        if Girl.SEXP < 10 and Girl not in (JeanX,StormX):
            $ Girl.change_face("_surprised", 2)
            $ Girl.eyes = "_down"
            if Girl == LauraX:
                $ Girl.brows = "_confused"
                "[Girl.name] seems perplexed that you would do something like that."
            else:
                "[Girl.name] blushes furiously, shocked at your behavior."
            $ Girl.change_face("_angry", 1)
            $ Girl.change_stat("lust", 50, 5)
            if not approval_check(Girl, 1200, TabM = 3):
                $ Girl.add_word(0,"_angry","_angry",0,0)
                $ renpy.pop_call()
                return
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
            if not approval_check(Girl, 1200, TabM = 3) and Girl != JeanX:
                return
        elif approval_check(Girl, 1100, TabM = 3):
            $ Girl.change_face("_surprised", 1)
            $ Girl.eyes = "_down"
            "[Girl.name] looks down at your cock and smiles."
            $ Girl.change_face("_sly", 1)
            $ Girl.change_stat("lust", 70, 8,Alt=[[EmmaX],60,12])
        elif approval_check(Girl, 500, "I", TabM=2):
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
            return

        if Girl.remaining_actions and Girl.location == bg_current:
            $ temp_Girls = ["none"]

            if Girl.action_counter["handjob"] >= 5 and approval_check(Girl, 1100, TabM = 3):
                $ counter = Girl.action_counter["handjob"] - 4
                $ counter = 10 if counter > 10 else counter
                while counter:
                    $ temp_Girls.append("handjob")
                    $ counter -= 1
            if Girl.action_counter["blowjob"] >= 5 and approval_check(Girl, 1300, TabM = 3):
                $ counter = Girl.action_counter["blowjob"] - 4
                $ counter = 10 if counter > 10 else counter
                $ counter += 5 if "hungry" in Girl.traits else 0
                while counter:
                    $ temp_Girls.append("blowjob")
                    $ counter -= 1
            if Girl.action_counter["titjob"] >= 5 and approval_check(Girl, 1200, TabM = 5):
                $ counter = Girl.action_counter["titjob"] - 4
                $ counter = 10 if counter > 10 else counter
                while counter:
                    $ temp_Girls.append("Tit")
                    $ counter -= 1
            if Girl.action_counter["sex"] >= 5 and approval_check(Girl, 1400, TabM = 5):
                $ counter = Girl.action_counter["sex"] - 4
                $ counter = 10 if counter > 10 else counter
                $ counter += 5 if Girl.lust >= 70 else 0
                while counter:
                    $ temp_Girls.append("sex")
                    $ counter -= 1
            if Girl.action_counter["anal"] >= 5 and approval_check(Girl, 1550, TabM = 5):
                $ counter = Girl.action_counter["anal"] - 4
                $ counter = 10 if counter > 10 else counter
                $ counter += 5 if Girl.lust >= 70 and Girl.used_to_anal else 0
                while counter:
                    $ temp_Girls.append("anal")
                    $ counter -= 1

            $ renpy.random.shuffle(temp_Girls)

            if temp_Girls[0] == "handjob":
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
            elif temp_Girls[0] == "blowjob" or (Girl == JubesX and JubesX.action_counter["blowjob"]):
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
                    $ Girl.change_face("_sly", 1,Mouth="_tongue")
                    ch_v "I uh, wouldn't mind giving that my full attention. . ."
                    $ Girl.mouth="_smile"
            elif temp_Girls[0] == "titjob":
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
            elif temp_Girls[0] == "sex":
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
            elif temp_Girls[0] == "anal":
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
                        $ Girl.change_face("_sly", 0,Eyes="_down")
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
                    $ action_context = "shift"

            $ offhand_action = 0

            if primary_action == "strip":
                call Group_Strip_End
            elif primary_action == "masturbation":
                $ Girl.remaining_actions -= 1
                $ Girl.action_counter["masturbation"] += 1
                call checkout
            elif primary_action:
                call CloseOut (Girl)

            show blackscreen onlayer black
            hide blackscreen onlayer black
            if temp_Girls[0] == "handjob":
                jump expression Girl.tag + "_HJ_Prep"
            elif temp_Girls[0] == "blowjob":
                jump expression Girl.tag + "_BJ_Prep"
            elif temp_Girls[0] == "titjob":
                jump expression Girl.tag + "_TJ_Prep"
            elif temp_Girls[0] == "sex":
                jump expression Girl.tag + "_SexPrep"
            elif temp_Girls[0] == "anal":
                jump expression Girl.tag + "_AnalPrep"
    return



label Girl_Tag(Girl=0, Forced=0, Gloves=0):

    $ Girl = GirlCheck(Girl)
    call shift_focus (Girl)
    $ Gloves = Girl.arms
    $ Girl.ArmPose = 2
    if not Forced:
        $ Girl.eyes = "_closed"
        $ Girl.brows = "_sad"

    if Forced and Player.level >= 5:
        if Gloves == "_gloves":
            $ Girl.arms = ""
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
                    $ Forced = 1
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
                    $ Girl.arms = Gloves
                    $ Girl.ArmPose = 1
                    return
            "Let her.":
                "She touches your face."
    else:
        $ Girl.addiction -= 10
        $ Girl.addiction_rate += 1 if Girl.addiction_rate < 5 else 0
        $ Girl.change_stat("lust", 90, 5)
        if Gloves == "_gloves":
            $ Girl.arms = ""
            $ Line = "She pulls off her gloves and"
        else:
            $ Line = "She reaches out and"
        if Girl == RogueX:
            "[Line] touches your face for a moment."
        elif Girl == KittyX:
            "[Line] grabs both sides of your face, looking intently into your eyes."
        elif Girl == EmmaX:
            "[Line] rubs the back of her hand against your cheek."
        elif Girl == LauraX:
            "[Line] grabs your face in one hand, firmly smooshing your cheeks together."
        elif Girl == JeanX:
            "[Line] wraps her hand around the back of your neck."
        elif Girl == StormX:
            "[Line] strokes her hand across your cheek."
        elif Girl == JubesX:
            "[Line] strokes your neck and cups her hand under your jaw."
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
        elif Forced:
            $ Girl.change_stat("obedience", 50, 1)
        "She continues to touch you, and a slight shiver passes through her."
    if round <= 15:
        Girl.voice "I suppose we don't have time for any more than that."
    if Gloves and not Girl.arms:
        "Appearing sated, she puts her gloves back on."
    $ Girl.blushing = "_blush1"
    $ Girl.arms = Gloves
    $ Girl.ArmPose = 1
    $ Girl.change_face()
    if Forced:
        $ Girl.recent_history.append("forced tag")
        $ Girl.daily_history.append("forced tag")
    $ Girl.recent_history.append("tag")
    $ Girl.daily_history.append("tag")
    return



label Slap_Ass(Girl=0):
    if Girl not in all_Girls:
        return
    call shift_focus (Girl)

    call Punch

    $ Girl.event_counter["ass_slapped"] += 1

    $ Girl.blushing = "_blush2" if Taboo else 1
    if approval_check(Girl, 200, "O", TabM=1):
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

    if Taboo:
        if not approval_check(Girl, 800, TabM=2):
            if Girl.event_counter["ass_slapped"] <= 5:
                $ Girl.change_stat("obedience", 80, 2)
                $ Girl.change_stat("obedience", 50, 2)
            $ Girl.change_stat("love", 70, -2)
            $ Girl.change_stat("love", 50, -1)
            "She looks pretty mad though."
        elif not approval_check(Girl, 1500, TabM=2):
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
    if Girl.PantsNum() < 5 and Girl.PantiesNum() < 5:
        if approval_check(Girl, 500, "O") and Girl.recent_history.count("slap") < 4:
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("lust", 200, 3)
        else:
            $ Girl.change_stat("lust", 80, 1)
        $ Girl.addiction -= 1
    $ Girl.recent_history.append("slap") if Girl.recent_history.count("slap") < 4 else Girl.recent_history
    $ Girl.daily_history.append("slap") if Girl.daily_history.count("slap") < 10 else Girl.daily_history
    return
