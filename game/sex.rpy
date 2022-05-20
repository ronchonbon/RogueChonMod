
label Jackin(Girl=0, counter=0, BO=[]):


    if not Girl or Girl not in all_Girls:
        $ BO = all_Girls[:]
        while BO:
            if BO[0].location == bg_current:
                $ Girl = BO[0]
                $ BO = [1]
            $ BO.remove(BO[0])

    if "unseen" in Girl.recent_history:
        $ Player.recent_history.append("cockout")
        $ offhand_action = "jackin"
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

        $ offhand_action = "jackin"
        if "jackin" in Girl.recent_history:
            return
        $ Girl.add_word(0,"jackin","jackin",0,0)

        if Girl == EmmaX and "classcaught" not in Girl.history:
            $ Girl.change_face("_surprised", 1)
            $ Girl.eyes = "_down"
            ch_e "Wait. . ."
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
            $ BO = ["none"]

            if Girl.action_counter["handjob"] >= 5 and approval_check(Girl, 1100, TabM = 3):
                $ counter = Girl.action_counter["handjob"] - 4
                $ counter = 10 if counter > 10 else counter
                while counter:
                    $ BO.append("handjob")
                    $ counter -= 1
            if Girl.action_counter["blowjob"] >= 5 and approval_check(Girl, 1300, TabM = 3):
                $ counter = Girl.action_counter["blowjob"] - 4
                $ counter = 10 if counter > 10 else counter
                $ counter += 5 if "hungry" in Girl.traits else 0
                while counter:
                    $ BO.append("blowjob")
                    $ counter -= 1
            if Girl.action_counter["titjob"] >= 5 and approval_check(Girl, 1200, TabM = 5):
                $ counter = Girl.action_counter["titjob"] - 4
                $ counter = 10 if counter > 10 else counter
                while counter:
                    $ BO.append("Tit")
                    $ counter -= 1
            if Girl.action_counter["sex"] >= 5 and approval_check(Girl, 1400, TabM = 5):
                $ counter = Girl.action_counter["sex"] - 4
                $ counter = 10 if counter > 10 else counter
                $ counter += 5 if Girl.lust >= 70 else 0
                while counter:
                    $ BO.append("sex")
                    $ counter -= 1
            if Girl.action_counter["anal"] >= 5 and approval_check(Girl, 1550, TabM = 5):
                $ counter = Girl.action_counter["anal"] - 4
                $ counter = 10 if counter > 10 else counter
                $ counter += 5 if Girl.lust >= 70 and Girl.used_to_anal else 0
                while counter:
                    $ BO.append("anal")
                    $ counter -= 1

            $ renpy.random.shuffle(BO)

            if BO[0] == "handjob":
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
            elif BO[0] == "blowjob" or (Girl == JubesX and JubesX.action_counter["blowjob"]):
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
            elif BO[0] == "titjob":
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
            elif BO[0] == "sex":
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
            elif BO[0] == "anal":
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
            if BO[0] == "handjob":
                jump expression Girl.tag + "_HJ_Prep"
            elif BO[0] == "blowjob":
                jump expression Girl.tag + "_BJ_Prep"
            elif BO[0] == "titjob":
                jump expression Girl.tag + "_TJ_Prep"
            elif BO[0] == "sex":
                jump expression Girl.tag + "_SexPrep"
            elif BO[0] == "anal":
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

    if Round <= 15:
        $ Girl.addiction -= 15 if Girl.addiction > 15 else Girl.addiction
    while Girl.addiction > 20 and Round > 15:
        $ Girl.addiction_rate += 1 if Girl.addiction_rate < 5 else 0
        $ Girl.addiction -= 15
        $ Round -= 5
        $ Girl.change_stat("lust", 90, 5)
        if Girl == RogueX:
            $ Girl.change_stat("lust", 90, 5)
        elif Forced:
            $ Girl.change_stat("obedience", 50, 1)
        "She continues to touch you, and a slight shiver passes through her."
    if Round <= 15:
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




label Massage(Girl=0, Current=0, Past=0, MCount=0):
    $ Girl = GirlCheck(Girl)
    call shift_focus (Girl)
    $ approval_bonus = 0
    if "_angry" in Girl.recent_history:
        return

    $ approval = approval_check(Girl, 500, TabM = 1)

    if Girl == JeanX and not JeanX.Taboo:
        $ approval = 2
    if approval >= 2:
        $ Girl.change_face("_bemused", 1)
        if Girl.Forced:
            $ Girl.change_face("_sad")
            $ Girl.change_stat("love", 20, -2, 1)
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 60, 1)
        if Girl == RogueX:
            ch_r "Ok [Girl.player_petname], sure."
        elif Girl == KittyX:
            ch_k "Sure, why not."
        elif Girl == EmmaX:
            ch_e "I could use it, [Girl.player_petname]."
        elif Girl == LauraX:
            ch_l "I guess I could use a rubdown."
        elif Girl == JeanX:
            ch_j "Oh, sure, get to work."
        elif Girl == StormX:
            ch_s "I could certainly use it."
        elif Girl == JubesX:
            ch_v "Oh, yeah, sure."
        $ Girl.change_stat("love", 90, 1)
        $ Girl.change_stat("inhibition", 50, 3)
        jump Massage_Prep
    else:

        $ Girl.change_face("_angry", 1)
        if "no_massage" in Girl.recent_history:
            if Girl == RogueX:
                ch_r "Heh, I {i}just{/i} told you \"no,\" [Girl.player_petname]."
            elif Girl == KittyX:
                ch_k "Come on, I {i}just{/i} told you \"no,\" [Girl.player_petname]."
            elif Girl == EmmaX:
                ch_e "I only {i}just{/i} refused you, [Girl.player_petname]."
            elif Girl == LauraX:
                ch_l "I only {i}just{/i} refused you, [Girl.player_petname]."
            elif Girl == JeanX:
                ch_j "I {i}just{/i} told you \"no,\" [Girl.player_petname]."
            elif Girl == StormX:
                ch_s "I have made myself clear on the matter."
            elif Girl == JubesX:
                ch_v "Ok, you can stop asking."
        elif "no_massage" in Girl.daily_history:
            if Girl == RogueX:
                ch_r "I told you \"no,\" earlier [Girl.player_petname]."
            elif Girl == KittyX:
                ch_k "I already told you \"no.\""
            elif Girl == EmmaX:
                ch_e "I told you \"no\" earlier, [Girl.player_petname]."
            elif Girl == LauraX:
                ch_l "I told you \"no\" earlier, [Girl.player_petname]."
            elif Girl == JeanX:
                ch_j "I told you \"no,\" earlier [Girl.player_petname]."
            elif Girl == StormX:
                ch_s "I refused earlier. I have not moved."
            elif Girl == JubesX:
                ch_v "Seriously, stop asking."
        else:
            $ Girl.change_face("_bemused")
            if Girl == RogueX:
                ch_r "I don't know, not right now."
            elif Girl == KittyX:
                ch_k "I don't know, not right now."
            elif Girl == EmmaX:
                ch_e "I'm not interested at the moment, [Girl.player_petname]."
            elif Girl == LauraX:
                ch_l "I'm not interested at the moment, [Girl.player_petname]."
            elif Girl == JeanX:
                ch_j "Not right now."
            elif Girl == StormX:
                ch_s "I would rather not."
            elif Girl == JubesX:
                ch_v "Nah, that's ok."
        menu:
            extend ""
            "Sorry, never mind." if "no_massage" in Girl.daily_history:
                $ Girl.change_face("_bemused")
                if Girl == RogueX:
                    ch_r "Ok, no problem, [Girl.player_petname]."
                elif Girl == KittyX:
                    ch_k "It's cool, [Girl.player_petname]."
                elif Girl == EmmaX:
                    ch_e "Don't concern yourself, [Girl.player_petname]."
                elif Girl == LauraX:
                    ch_l "No worries."
                elif Girl == JeanX:
                    ch_j "It's fine, maybe later."
                elif Girl == StormX:
                    ch_s "No harm done, certainly."
                elif Girl == JubesX:
                    ch_v "No prob."
                return
            "Maybe later?" if "no_massage" not in Girl.daily_history:
                $ Girl.change_face("_sexy")
                $ Girl.change_stat("love", 80, 1)
                $ Girl.change_stat("inhibition", 20, 1)
                $ Girl.change_stat("obedience", 20, 1)
                if Girl == RogueX:
                    ch_r "Sure, maybe."
                elif Girl == KittyX:
                    ch_k "Yeah, maybe."
                elif Girl == EmmaX:
                    ch_e "Perhaps."
                elif Girl == LauraX:
                    ch_l "Maybe?"
                elif Girl == JeanX:
                    ch_j "Probably, yeah."
                elif Girl == StormX:
                    ch_s "It is certainly possible."
                elif Girl == JubesX:
                    ch_v "Maybe, I guess."
                $ Girl.recent_history.append("no_massage")
                $ Girl.daily_history.append("no_massage")
                return
            "Come on, Please?":
                if approval:
                    $ Girl.change_face("_sexy")
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 40, 2)
                    $ Girl.change_stat("inhibition", 30, 2)
                    if Girl == RogueX:
                        ch_r "Well, if you're that desperate. . ."
                    elif Girl == KittyX:
                        ch_k "I guess I could use some relaxation. . ."
                    elif Girl == EmmaX:
                        ch_e "I do have some tension built up. . ."
                    elif Girl == LauraX:
                        ch_l "Ok, ok, I do have some knots. . ."
                    elif Girl == JeanX:
                        ch_j "Oh, fine."
                    elif Girl == StormX:
                        ch_s "If you insist. . ."
                    elif Girl == JubesX:
                        ch_v "Ok, fine."
                    jump Massage_Prep
                else:
                    $ Girl.change_face("_sexy")
                    if Girl == RogueX:
                        ch_r "Heh, no thanks, [Girl.player_petname]."
                    elif Girl == KittyX:
                        ch_k "Heh, sorry, [Girl.player_petname]."
                    else:
                        $ Girl.change_face("_sly", Brows="_confused")
                        Girl.voice "No."

    if "no_massage" in Girl.daily_history:
        if Girl == RogueX:
            ch_r "You're starting to skeeve me out, [Girl.player_petname]."
        elif Girl == KittyX:
            ch_k "Um, get a clue, [Girl.player_petname]."
        elif Girl == EmmaX:
            ch_e "I've made myself clear on this, [Girl.player_petname]."
        elif Girl == LauraX:
            ch_l "I've made myself clear on this, [Girl.player_petname]."
        elif Girl == JeanX:
            ch_j "Stop asking, it's sad."
        elif Girl == StormX:
            ch_s "I am unlikely to bend on this."
        elif Girl == JubesX:
            ch_v "This is getting totally weird."
        $ Girl.recent_history.append("_angry")
        $ Girl.daily_history.append("_angry")
    elif Girl.Forced:
        $ Girl.change_face("_angry", 1)
        $ Girl.change_stat("lust", 60, 5)
        $ Girl.change_stat("obedience", 50, -2)
        if Girl == RogueX:
            ch_r "I don't even want you touching me."
        elif Girl == KittyX:
            ch_k "Even that's too much."
        elif Girl == EmmaX:
            ch_e "You'll have to keep your hands limber for yourself."
        elif Girl == LauraX:
            ch_l "You'll have to keep your hands limber for yourself."
        elif Girl == JeanX:
            ch_j "Don't even ask."
        elif Girl == StormX:
            ch_s "I am uninterested."
        elif Girl == JubesX:
            ch_v "Definitely not."
        $ Girl.recent_history.append("_angry")
        $ Girl.daily_history.append("_angry")
    elif Girl.Taboo:
        $ Girl.change_face("_angry", 1)
        if Girl == RogueX:
            ch_r "I don't want you touching me in public."
        elif Girl == KittyX:
            ch_k "Not[Girl.like]in public."
        elif Girl == EmmaX:
            ch_e "I can't been seen doing that with you."
        elif Girl == LauraX:
            ch_l "I try to stay off the radar."
        elif Girl == JeanX:
            ch_j "I don't want to be seen getting a massage. . ."
        elif Girl == StormX:
            ch_s "People would get the wrong idea."
        elif Girl == JubesX:
            ch_v "This is too public. . ."
    else:
        $ Girl.change_face("_sexy")
        $ Girl.mouth = "_sad"
        if Girl == RogueX:
            ch_r "Seriously, no thanks, [Girl.player_petname]."
        elif Girl == KittyX:
            ch_k "Seriously, no thank you!"
        elif Girl == EmmaX:
            ch_e "I really can't."
        elif Girl == LauraX:
            ch_l "So not into it."
        elif Girl == JeanX:
            ch_j "Back away."
        elif Girl == StormX:
            ch_s "Stop."
        elif Girl == JubesX:
            ch_v "No way."
    $ Girl.recent_history.append("no_massage")
    $ Girl.daily_history.append("no_massage")
    $ approval_bonus = 0
    return

label Massage_Prep(Girl=focused_Girl, Current=0, Past=0, MCount=0):
    call Top_Off (Girl, "massage")
    if not Girl.top and "no_topless" not in Girl.recent_history:
        $ Girl.change_stat("obedience", 50, 3)
        $ Girl.change_stat("inhibition", 50, 3)
    elif Girl.Forced:

        if "no_topless" in Girl.recent_history:
            if Girl == RogueX:
                ch_r "Look, we can still do this, so long as I can touch you after."
            elif Girl == KittyX:
                ch_k "Even with my top on, we can still do this. . ."
            elif Girl == EmmaX:
                ch_e "I think we can manage with my top left on. . ."
            elif Girl == LauraX:
                ch_l "We can still do something here. . ."
            elif Girl == JeanX:
                ch_j "We can worry about that later."
            elif Girl == StormX:
                ch_s "We can discuss skin contact later."
            elif Girl == JubesX:
                ch_v "I'd prefer to keep the top on."
            menu:
                extend ""
                "Sure, ok.":
                    $ Girl.change_stat("obedience", 50, 5)
                    $ Girl.change_stat("inhibition", 50, 5)
                "Nope, not worth it.":
                    if Girl == RogueX:
                        ch_r "Fine then! What else?"
                    elif Girl == KittyX:
                        ch_k "Well!"
                    elif Girl == EmmaX:
                        ch_e "Pity. Any other ideas?"
                    elif Girl == LauraX:
                        ch_l "Ok."
                    elif Girl == JeanX:
                        ch_j "Fair enough."
                    elif Girl == StormX:
                        ch_s "Very well."
                    elif Girl == JubesX:
                        ch_v "Well ok then, be that way."
                    return
        else:
            $ Girl.change_stat("obedience", 50, 5)
            $ Girl.change_stat("inhibition", 50, 5)
            if Girl == RogueX:
                ch_r "Ok, but after we do this, I get a little touch too."
            elif Girl == KittyX:
                ch_k "Sure, but after this, I'll still need to touch you."
            elif Girl == EmmaX:
                ch_e "Fine, but I will still need some other contact."
            elif Girl == LauraX:
                ch_l "Yeah, but, I'll need to touch you after this."
            elif Girl == StormX:
                ch_s "So long as I get some skin contact from this. . ."
            elif Girl == JubesX:
                ch_v "But you know, give me som contact after."
                if Girl.accessory and Girl.top:
                    $ Girl.accessory = ""
                    "She does take off the jacket though."
    if "_angry" in Girl.recent_history:
        return

label Massage_Cycle:


    $ Girl.add_word(1,"massage","massage",0,0)

    if Girl.pose == "doggy" or Girl.pose == "sex":
        call expression Girl.tag + "_Sex_Launch" pass ("massage")

    $ primary_action = "massage"

    while Round >= 10 and MCount < 10:
        call shift_focus (Girl)
        $ Girl.lust_face()

        call ViewShift (Girl, Girl.pose, 0)










        menu Massage_Choices:
            "Where do you touch?"
            "Her Upper Body":
                menu:
                    "Her Neck":
                        $ Past = Current
                        $ Current = "neck"
                    "Her Shoulders":
                        $ Past = Current
                        $ Current = "shoulders"
                    "Her Back":
                        $ Past = Current
                        $ Current = "back"
                    "Her Breasts":
                        $ Past = Current
                        $ Current = "breasts"
                    "Her Arms":
                        $ Past = Current
                        $ Current = "arms"
                    "Her Hands":
                        $ Past = Current
                        $ Current = "hands"
                    "Back":
                        jump Massage_Choices
            "Her Legs":
                menu:
                    "Her Hips":
                        $ Past = Current
                        $ Current = "hips"
                    "Her Ass":
                        $ Past = Current
                        $ Current = "ass"
                    "Her Pussy":
                        $ Past = Current
                        $ Current = "pussy"
                    "Her Thighs":
                        $ Past = Current
                        $ Current = "thighs"
                    "Her Calves":
                        $ Past = Current
                        $ Current = "calves"
                    "Her Feet":
                        $ Past = Current
                        $ Current = "feet"
                    "Back":
                        jump Massage_Choices
            "Her Neck" if Current in ("neck","shoulders","back"):
                $ Past = Current
                $ Current = "neck"
            "Her Shoulders" if Current in ("neck","shoulders","back","arms"):
                $ Past = Current
                $ Current = "shoulders"
            "Her Back" if Current in ("neck","shoulders","back","breasts","hips"):
                $ Past = Current
                $ Current = "back"
            "Her Breasts" if Current in ("breasts","back"):
                $ Past = Current
                $ Current = "breasts"
            "Her Arms" if Current in ("shoulders","arms","hands"):
                $ Past = Current
                $ Current = "arms"
            "Her Hands" if Current in ("arms","hands"):
                $ Past = Current
                $ Current = "hands"
            "Her Hips" if Current in ("back","hips","ass","pussy","thighs"):
                $ Past = Current
                $ Current = "hips"
            "Her Ass" if Current in ("back","hips","ass","pussy","thighs"):
                $ Past = Current
                $ Current = "ass"
            "Her Pussy" if Current in ("hips","ass","pussy","thighs"):
                $ Past = Current
                $ Current = "pussy"
            "Her Thighs" if Current in ("hips","ass","pussy","thighs","calves"):
                $ Past = Current
                $ Current = "thighs"
            "Her Calves" if Current in ("thighs","calves","feet"):
                $ Past = Current
                $ Current = "calves"
            "Her Feet" if Current in ("calves","feet"):
                $ Past = Current
                $ Current = "feet"
            "Her clothes":
                call Girl_Undress (Girl)
                jump Massage_Choices
            "I don't have time for this. [[Auto]":
                menu:
                    "Just do a little Massage and wrap it up?"
                    "Yeah [[Auto complete]":
                        "Ok."
                        "You just do a quick massage, hitting all the basics and working out her muscles."
                        $ D20 = renpy.random.randint(2,5)
                        $ Girl.addiction -= (10 + (4*D20))
                        $ MCount = D20
                        $ Girl.lust += (5*D20)
                        jump Massage_After
                    "No [[Full Manual]":
                        jump Massage_Cycle
            "View":


                call ViewShift (Girl, "menu")
                jump Massage_Cycle
            "Stop":








                jump Massage_After


        if Girl.pose == "doggy" or Girl.pose == "sex":
            if Current in ("calves","feet"):
                $ ShowFeet = 1
            else:
                $ ShowFeet = 0

        elif Current in ("neck","shoulders","back","breasts","arms","hands"):
            $ Girl.pose = "breasts"
        elif Current in ("hips","ass","pussy","thighs"):
            $ Girl.pose = "pussy"

        call ViewShift (Girl, Girl.pose, 0)

        if Current == "neck":
            if Past in ("shoulders","back"):
                $ Line = "You slide your hands toward " +Girl.name+ "'s " +Current
                $ Check = 400
            else:
                $ Line = "You begin to massage " +Girl.name+ "'s " +Current
                $ Check = 500

            if Girl.massage_chart[MCount] == Current and approval_check(Girl, Check):

                $ Girl.change_stat("lust", 60, 2)
                $ Girl.change_stat("lust", 90, 1)
                if Past == Current:
                    $ Girl.change_stat("lust", 90, 2)
                    "You really dig into her neck muscles, and she lets out a long groan of pleasure."
                else:
                    "[Line]. She stretches out in obvious pleasure as the knots release."

            $ Girl.addiction -= 2
        elif Current == "shoulders":
            if Past in ("back","neck","arms"):
                $ Line = "You slide your hands toward " +Girl.name+ "'s " +Current
                $ Check = 400
            else:
                $ Line = "You begin to massage " +Girl.name+ "'s " +Current
                $ Check = 500

            if Girl.massage_chart[MCount] == Current and approval_check(Girl, Check):

                $ Girl.change_stat("lust", 60, 2)
                $ Girl.change_stat("lust", 90, 2)
                if Past == Current:
                    $ Girl.change_stat("lust", 90, 2)
                    "You really dig into her shoulders, and she wriggles them and moans."
                else:
                    "[Line]. She stretches out in obvious pleasure as the knots release."
            elif Past == Current:
                $ Check = 600
                $ Line = "You continue to massage " +Girl.name+ "'s " +Current

            if not Girl.top:
                $ Girl.addiction -= 3
        elif Current == "back":
            if Past in ("neck","shoulders","breasts","hips"):
                $ Line = "You slide your hands toward " +Girl.name+ "'s " +Current
                $ Check = 400
            else:
                $ Line = "You begin to massage " +Girl.name+ "'s " +Current
                $ Check = 500

            if Girl.massage_chart[MCount] == Current and approval_check(Girl, Check):

                $ Girl.change_stat("lust", 60, 2)
                $ Girl.change_stat("lust", 90, 2)
                if Past == Current:
                    $ Girl.change_stat("lust", 90, 2)
                    "You really put the pressure into her spine, and she lets out a long groan of pleasure."
                else:
                    "[Line]. She moans as you hear her vertebrae stretch."
            elif Past == Current:
                $ Check = 600
                $ Line = "You continue to massage " +Girl.name+ "'s " +Current

            if not Girl.top:
                $ Girl.addiction -= 2
            if not Girl.bra:
                $ Girl.addiction -= 2
        elif Current == "breasts":
            if Past == "back":
                $ Line = "You slide your hands around and grasp " +Girl.name+ "'s " +Current
                $ Check = 1000
            else:
                $ Line = "You move your hands to grab " +Girl.name+ "'s " +Current
                $ Check = 1050

            if Girl.massage_chart[MCount] == Current and approval_check(Girl, Check):

                $ Girl.change_stat("lust", 60, 1)
                $ Girl.change_stat("lust", 90, 2)
                $ Girl.change_stat("lust", 200, 3)
                if Past == Current:
                    $ Girl.change_stat("lust", 200, 2)
                    "You knead her breasts firmly and she lets out a low moan."
                else:
                    "[Line]. Her nipples grow sharp in your palms."
            elif Past == Current:
                $ Check = 1050
                $ Girl.change_stat("lust", 200, 2)
                $ Line = "You continue to rub " +Girl.name+ "'s " +Current

            if not Girl.top and not Girl.bra:
                $ Girl.addiction -= 5
        elif Current == "arms":
            if Past == "shoulders":
                $ Line = "You slide your hands down " +Girl.name+ "'s " +Current
                $ Check = 400
            elif Past == "hands":
                $ Line = "You slide your hands up " +Girl.name+ "'s " +Current
                $ Check = 400
            else:
                $ Line = "You begin to massage " +Girl.name+ "'s " +Current
                $ Check = 500

            if Girl.massage_chart[MCount] == Current and approval_check(Girl, Check):

                $ Girl.change_stat("lust", 60, 2)
                $ Girl.change_stat("lust", 90, 1)
                if Past == Current:
                    $ Girl.change_stat("lust", 90, 2)
                    "You really dig into her triceps, and she seemed really knotted up."
                else:
                    "[Line]. Her hands flex involuntarily and she coos in pleasure."
            elif Past == Current:
                $ Check = 600
                $ Line = "You continue to massage " +Girl.name+ "'s " +Current

            if Girl.top not in ("_mesh_top","_pink_top","_jacket"):
                $ Girl.addiction -= 3
        elif Current == "hands":
            if Past == "arms":
                $ Line = "You slide your hands down and grasp " +Girl.name+ "'s " +Current
                $ Check = 400
            else:
                $ Line = "You pick up " +Girl.name+ "'s " +Current+ " and begin to massage them"
                $ Check = 500

            if Girl.massage_chart[MCount] == Current and approval_check(Girl, Check):

                $ Girl.change_stat("lust", 70, 2)
                if Past == Current:
                    $ Girl.change_stat("lust", 70, 2)
                    "You stretch each finger and rub along the joints. She lets out a small gasp."
                else:
                    "[Line]. Her fingers flex with pleasure."
            elif Past == Current:
                $ Check = 600
                $ Line = "You continue to massage " +Girl.name+ "'s " +Current

            $ Girl.addiction -= 3
        elif Current == "hips":
            if Past == "back":
                $ Line = "You slide your hands down toward " +Girl.name+ "'s " +Current
                $ Check = 400
            elif Past in ("ass","pussy","thighs"):
                $ Line = "You slide your hands up toward " +Girl.name+ "'s " +Current
                $ Check = 400
            else:
                $ Line = "You begin to massage " +Girl.name+ "'s " +Current
                $ Check = 500

            if Girl.massage_chart[MCount] == Current and approval_check(Girl, Check):

                $ Girl.change_stat("lust", 60, 2)
                $ Girl.change_stat("lust", 90, 1)
                if Past == Current:
                    "You really dig into her hips, and she lets out a long groan of pleasure."
                else:
                    "[Line]. Her back arches out in obvious pleasure as the knots release."
            elif Past == Current:
                $ Check = 600
                $ Line = "You continue to massage " +Girl.name+ "'s " +Current

            if not Girl.legs and Girl.HoseNum() < 10:
                $ Girl.addiction -= 1
        elif Current == "ass":
            if Past in ("back","hips"):
                $ Line = "You slide your hands down toward " +Girl.name+ "'s " +Current
                $ Check = 900
            elif Past in ("pussy","thighs"):
                $ Line = "You slide your hands up to " +Girl.name+ "'s " +Current
                $ Check = 900
            else:
                $ Line = "You begin to massage " +Girl.name+ "'s " +Current
                $ Check = 950

            if Girl.massage_chart[MCount] == Current and approval_check(Girl, Check):

                $ Girl.change_stat("lust", 60, 2)
                $ Girl.change_stat("lust", 90, 1)
                $ Girl.change_stat("lust", 200, 3)
                if Past == Current:
                    $ Girl.change_stat("lust", 200, 2)
                    "You move across her ass in a wavelike pattern as her back wriggles in pleasure."
                else:
                    "[Line]. Her muscles tighten and release as you squeeze them."
            elif Past == Current:
                $ Check = 950
                $ Girl.change_stat("lust", 90, 2)
                $ Line = "You continue to massage " +Girl.name+ "'s " +Current

            if not Girl.legs and not Girl.underwear and Girl.HoseNum() < 10:
                $ Girl.addiction -= 3
        elif Current == "pussy":
            if Past in ("hips","ass"):
                $ Line = "You slide your hands around toward " +Girl.name+ "'s " +Current
                $ Check = 1200
            elif Past == "thighs":
                $ Line = "You slide your hands up and into " +Girl.name+ "'s groin"
                $ Check = 1100
            else:
                $ Line = "You begin to massage " +Girl.name+ "'s " +Current
                $ Check = 1200

            if Girl.massage_chart[MCount] == Current and approval_check(Girl, Check):

                $ Girl.change_stat("lust", 60, 2)
                $ Girl.change_stat("lust", 90, 2)
                $ Girl.change_stat("lust", 200, 3)
                if Past == Current:
                    $ Girl.change_stat("lust", 200, 5)
                    "You draw your thumbs across her clit and she shudders with pleasure."
                else:
                    "[Line]. Her back arches with pleasure and she releases a soft moan."
            elif Past == Current:
                $ Check = 1200
                $ Girl.change_stat("lust", 200, 3)
                $ Line = "You continue to rub " +Girl.name+ "'s " +Current

            if not Girl.legs and not Girl.underwear and Girl.HoseNum() < 10:
                $ Girl.addiction -= 5
        elif Current == "thighs":
            if Past == "calves":
                $ Line = "You slide your hands up toward " +Girl.name+ "'s " +Current
                $ Check = 500
            elif Past in ("hips","ass","pussy"):
                $ Line = "You slide your hands down toward " +Girl.name+ "'s " +Current
                $ Check = 400
            else:
                $ Line = "You begin to massage " +Girl.name+ "'s " +Current
                $ Check = 600

            if Girl.massage_chart[MCount] == Current and approval_check(Girl, Check):

                $ Girl.change_stat("lust", 60, 2)
                $ Girl.change_stat("lust", 90, 1)
                if Past == Current:
                    $ Girl.change_stat("lust", 60, 1)
                    "You really put some pressure into stretching out her quads, and she groans in pleasure."
                else:
                    "[Line]. Her legs stretch out with clear satisfaction."
            elif Past == Current:
                $ Check = 600
                $ Line = "You continue to massage " +Girl.name+ "'s " +Current

            if Girl.PantsNum() <= 6 and Girl.HoseNum() < 10:
                $ Girl.addiction -= 3
        elif Current == "calves":
            if Past == "feet":
                $ Line = "You slide your hands up and stroke " +Girl.name+ "'s " +Current
                $ Check = 400
            elif Past == "thighs":
                $ Line = "You slide your hands up to grab " +Girl.name+ "'s " +Current
                $ Check = 400
            else:
                $ Line = "You begin to massage " +Girl.name+ "'s " +Current
                $ Check = 500

            if Girl.massage_chart[MCount] == Current and approval_check(Girl, Check):

                $ Girl.change_stat("lust", 60, 2)
                $ Girl.change_stat("lust", 90, 1)
                if Past == Current:
                    $ Girl.change_stat("lust", 60, 1)
                    "You stretch her ankles back and forth, as you work out her tensed calves."
                else:
                    "[Line]. She flexes her toes in satisfaction as her muscles stretch out."
            elif Past == Current:
                $ Check = 600
                $ Line = "You continue to massage " +Girl.name+ "'s " +Current

            if Girl.PantsNum() <= 6 and Girl.HoseNum() < 10:
                $ Girl.addiction -= 2
        elif Current == "feet":
            if Past == "calves":
                $ Line = "You slide your hands down and grasp " +Girl.name+ "'s " +Current
                $ Check = 400
            else:
                $ Line = "You begin to rub " +Girl.name+ "'s " +Current
                $ Check = 600

            if Girl.massage_chart[MCount] == Current and approval_check(Girl, Check):

                $ Girl.change_stat("lust", 60, 2)
                $ Girl.change_stat("lust", 90, 1)
                if Past == Current:
                    $ Girl.change_stat("lust", 90, 2)
                    "You press your thumbs deeply into her arches, and her toes curl around them."
                else:
                    "[Line]. She stretches her toes and lets out a soft moan."
            elif Past == Current:
                $ Check = 600
                $ Line = "You continue to rub " +Girl.name+ "'s " +Current

            if Girl.accessory != "boots" and Girl.HoseNum() < 10:
                $ Girl.addiction -= 3



        if Girl.massage_chart[MCount] == Current and approval_check(Girl, Check):

            if Girl == JeanX:
                $ Girl.change_stat("love", 60, 1)
                $ Girl.change_stat("obedience", 30, 1)
        elif approval_check(Girl, Check):

            $ Line = Line + renpy.random.choice([". She wriggles a little in contentment.",
                                ". She lets out a little hum.",
                                ". She really seems to enjoy it.",
                                ". She seems comfortable with this.",
                                ". She lets out a small purr of pleasure."])
            $ Girl.change_stat("lust", 60, 2)
            $ Girl.change_stat("lust", 90, 1)
            "[Line]"
            if Current == Past and Current in ("breasts","ass","pussy"):


                call Massage_After
                $ Girl.remaining_actions += 1
                if Current == "breasts":
                    call expression Girl.tag + "_FB_Prep"
                elif Current == "ass":
                    call expression Girl.tag + "_FA_Prep"
                elif Current == "pussy":
                    call expression Girl.tag + "_FP_Prep"
                return
        elif approval_check(Girl, Check-200) or "massagefail" in Girl.recent_history:

            $ Line = Line + renpy.random.choice([". She stiffens a bit, but settles back into it.",
                                ". She doesn't seem to enjoy it.",
                                ". She doesn't seem comfortable with this.",
                                ". She lets out a small tsk of irritation."])
            $ Girl.change_stat("lust", 60, -1)
            $ Girl.change_stat("lust", 90, -2)
            "[Line]"
            if Current == Past and Current in ("breasts","ass","pussy"):

                call Massage_BadEnd
                menu:
                    extend ""
                    "Sorry, yeah":
                        "You pull your hands back."
                        $ Past = Current
                        $ Current = 0
                    "I'm enjoying this":
                        $ Girl.add_word(1,"massagefail")
                        jump Massage_BadEnd
            $ Girl.add_word(1,"massagefail")
        else:

            "[Line]. She stiffens and sits up."
            $ Girl.add_word(1,"massagefail")
            jump Massage_BadEnd

        $ Round -= 6
        if Girl.massage_chart[MCount] == Current:

            if MCount == 2:
                "You feel like you're on to something here, whatever you're doing seems to be working."
            elif MCount == 7:
                "She really seems to be getting into it, she's practically vibrating."
            $ MCount += 1



        if not Girl.Taboo:

            $ primary_action = "massage"
            $ Line = 0
            call Girl_Self_Lines (Girl, "T3", girl_offhand_action)
            if Line:
                $ Line3 = Line + "."

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        $ Player.focus = 80 if Player.focus >= 80 and girl_offhand_action != "handjob" else Player.focus

        if Player.focus >= 100 or Girl.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (Girl)
                if "_angry" in Girl.recent_history:
                    call expression Girl.tag + "_Pos_Reset" pass (0)
                    call expression Partner.tag + "_Pos_Reset" pass (0)
                    return
                $ Girl.change_stat("lust", 200, 5)
                if 100 > Girl.lust >= 70 and Girl.session_orgasms < 2:
                    $ Girl.recent_history.append("unsatisfied")
                    $ Girl.daily_history.append("unsatisfied")
                $ Line = "came"

            if Girl.lust >= 100:

                if approval_check(Girl, 1000, TabM = 1):
                    call Girl_Cumming (Girl)
                else:
                    call Girl_Cumming (Girl, 1)
                    $ Girl.change_face("_bemused",2,Eyes="_side")
                    if Girl == RogueX:
                        ch_r "Oh. . . wow. . . um. . ."
                        ch_r "That was nice. . ."
                    elif Girl == KittyX:
                        ch_k ". . ."
                        ch_k "That was. . . that was nothing. . ."
                        ch_k "Nothing to see here. . ."
                    elif Girl == EmmaX:
                        ch_e ". . ."
                        ch_e "I'm not sure what you think just happened, but don't let it get to your head."
                    elif Girl == LauraX:
                        ch_l "Huh. . ."
                        $ Girl.change_face("_sexy",1)
                        ch_l "Good job."
                    elif Girl == JeanX:
                        ch_j "Wow, you really know what you're doing there. . ."
                        if Girl.event_counter["orgasmed"]< 2:
                            $ Girl.change_stat("love", 80, 2)
                            $ Girl.change_stat("obedience", 50, 2)
                    elif Girl == StormX:
                        ch_s ". . ."
                        ch_s "Well that was unexpected. . ."
                        ch_s "You deliver a -very- good massage."
                    elif Girl == JubesX:
                        ch_v "Oh!"
                        ch_v "Um. . ."
                        ch_v "Yes, that was fantastic."
                    $ Girl.change_face("_sexy",1)

                jump Massage_After

            if Line == "came":
                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)



label Massage_After:
    call expression Girl.tag + "_Pos_Reset" pass (0)
    if MCount >= 3:
        $ Girl.change_stat("love", 90, 1)
        $ Girl.change_stat("love", 50, 2)
        $ Girl.change_stat("obedience", 30, 2)

    $ Girl.action_counter["massage"] += 1
    $ Girl.remaining_actions -= 1
    $ Girl.addiction_rate += 2 if Girl.addiction_rate < 5 else Girl.addiction_rate
    if "addictive" in Player.traits:
        $ Girl.addiction_rate += 1

    $ Girl.change_face("_smile",1)
    if MCount == 10 and not Girl.Forced:

        if Girl == RogueX:
            ch_r "Hnnnng, that was ama-zing, [Girl.player_petname]!"
            ch_r "Did you have anything else in mind?"
        elif Girl == KittyX:
            ch_k "Wowwww, [Girl.player_petname], that was fantastic!"
            ch_k "What do you have for round two?"
        elif Girl == EmmaX:
            ch_e ". . ."
            ch_e "Incredible, [Girl.player_petname]."
            ch_e "Did you want to. . . continue?"
        elif Girl == LauraX:
            ch_l "Nnnnn, [Girl.player_petname], that was great!"
            ch_l "That felt amazing, did you have anything else in mind?"
        elif Girl == JeanX:
            ch_j "Mmmm. . . that was fantastic!"
            $ Girl.change_stat("love", 80, 2)
            $ Girl.change_stat("love", 50, 2)
            $ Girl.change_stat("obedience", 50, 2)
            ch_j "Did you have any other plans?"
        elif Girl == StormX:
            ch_s "That was a truly exceptional massage, [Girl.player_petname]."
            ch_s "I really must have you do that again some time."
        elif Girl == JubesX:
            ch_v "That really did the trick. . ."
            ch_v "Head, shoulder, knees, toes. . ."
    elif Girl.action_counter["massage"] == 1:

        if Girl == RogueX:
            ch_r "That was very relaxing, [Girl.player_petname]."
        elif Girl == KittyX:
            ch_k "That was niiiiice, [Girl.player_petname]."
        elif Girl == EmmaX:
            ch_e "That was very. . . pleasant, [Girl.player_petname]."
        elif Girl == LauraX:
            ch_l "Think that worked out some. . . kinks, [Girl.player_petname]."
        elif Girl == JeanX:
            ch_j "You know your way around, [Girl.player_petname]."
        elif Girl == StormX:
            ch_s "That was an excellent massage, [Girl.player_petname]."
        elif Girl == JubesX:
            ch_v "Hey, you're really good at this, [Girl.player_petname]."
    else:

        if Girl == RogueX:
            ch_r "I do enjoy a nice massage, [Girl.player_petname]."
        elif Girl == KittyX:
            ch_k "Hmm, I enjoyed that one, [Girl.player_petname]."
        elif Girl == EmmaX:
            ch_e "That was very. . . pleasant, [Girl.player_petname]."
        elif Girl == LauraX:
            ch_l "Thanks for that one, [Girl.player_petname]."
        elif Girl == JeanX:
            ch_j "That was very nice, [Girl.player_petname]. Good job."
        elif Girl == StormX:
            ch_s "Thank you, [Girl.player_petname]."
        elif Girl == JubesX:
            ch_v "Hey, good job with that one."
    $ Girl.change_stat("love", 90, int(MCount/2))
    $ approval_bonus = 0
    call checkout
    return

label Massage_BadEnd:

    $ Girl.change_face("_angry",1)
    if "massagefail" in Girl.recent_history:

        $ Girl.action_counter["massage"] += 1
        $ Girl.remaining_actions -=1
        $ Girl.addiction_rate += 2 if Girl.addiction_rate < 5 else Girl.addiction_rate
        if "addictive" in Player.traits:
            $ Girl.addiction_rate += 1
        if Girl == RogueX:
            ch_r "Ok, enough out of you, [Girl.player_petname]."
        elif Girl == KittyX:
            ch_k "Bad touch!"
        elif Girl == EmmaX:
            ch_e "That will be enough of that."
        elif Girl == LauraX:
            ch_l "Ok, you're benched."
        elif Girl == JeanX:
            ch_j "Ok, you've had enough. . ."
        elif Girl == StormX:
            ch_s "Thank you, [Girl.player_petname], I think that's quite enough."
        elif Girl == JubesX:
            ch_v "Ok, cut that out, [Girl.player_petname]."
        $ approval_bonus = 0
        call checkout
    elif Current == "breasts":
        if Girl == RogueX:
            ch_r "I think you should probably watch your hands there, [Girl.player_petname]."
        elif Girl == KittyX:
            ch_k "Hey! Um, stay away from my. . . breasts."
        elif Girl == EmmaX:
            ch_e "[Girl.player_petname]! I contain your enthusiasm!"
        elif Girl == LauraX:
            ch_l "Hey. I thought this was about me, not you."
        elif Girl == JeanX:
            ch_j "A little less squeezing and a little more massage. . ."
        elif Girl == StormX:
            ch_s "I think you're allowing your enthusiasm to get the best of you, [Girl.player_petname]."
        elif Girl == JubesX:
            ch_v "Whoa, not so fast. . ."
    elif Current == "ass":
        if Girl == RogueX:
            ch_r "You might want to keep things above the belt, [Girl.player_petname]."
        elif Girl == KittyX:
            ch_k "Hey[Girl.like]keep your hands off my butt!"
        elif Girl == EmmaX:
            ch_e "[Girl.player_petname]! I'd appreciate you not fondling my rear?"
        elif Girl == LauraX:
            ch_l "I don't really need my ass worked on right now."
        elif Girl == JeanX:
            ch_j "Maybe don't worry about my ass. . ."
        elif Girl == StormX:
            ch_s "That really isn't the best place to be touching, [Girl.player_petname]."
        elif Girl == JubesX:
            ch_v "Whoa, not there."
    elif Current == "pussy":
        if Girl == RogueX:
            ch_r "Whoa there, [Girl.player_petname]! Keep your hands out of there!"
        elif Girl == KittyX:
            ch_r "Whoa! I know my name is \"Kitty\" and all, but that's not an invitation!"
        elif Girl == EmmaX:
            ch_e "[Girl.player_petname]! Buy a girl a drink first. Or another, at least."
        elif Girl == LauraX:
            ch_l "I'll let you know when I need -that- massaged."
        elif Girl == JeanX:
            ch_j "Well, that's one part of my body, but maybe not the part that needed attention. . ."
        elif Girl == StormX:
            ch_s "I think perhaps you misunderstood my needs here, [Girl.player_petname]."
        elif Girl == JubesX:
            ch_v "That's getting a little personal, isn't it?"
    else:
        if Girl == RogueX:
            ch_r "I think you should probably watch your hands there, [Girl.player_petname]."
        elif Girl == KittyX:
            ch_k "Ooh, not there."
        elif Girl == EmmaX:
            ch_e "[Girl.player_petname]! I expect you to remain more professional than that."
        elif Girl == LauraX:
            ch_l "You should probably avoid that area right now."
        elif Girl == JeanX:
            ch_j "Maybe try to avoid that area? . ."
        elif Girl == StormX:
            ch_s "Could you perhaps try someplace else, [Girl.player_petname]?"
        elif Girl == JubesX:
            ch_v "Maybe try somehting else, [Girl.player_petname]?"
    return











label Group_Strip(Girl=0, approval_bonus=approval_bonus, approval_bonusP=[0,0], BO=[]):

    $ Present = []
    $ BO = all_Girls[:]
    while BO:
        if BO[0].location == bg_current:
            $ Present.append(BO[0])
        $ BO.remove(BO[0])

    if not Present:
        "Nobody's here."
        "You dance alone."
        return

    while len(Present) > 2:

        call Remove_Girl (Present[2])


    if len(Present) == 2:
        $ renpy.random.shuffle(Present)
        if Girl and Present[0] != Girl:
            $ Party.reverse()
        elif approval_check(Present[0],Check=1) <= approval_check(Present[1],Check=1):

            $ Present.reverse()

    call shift_focus (Present[0])

    $ Round -= 5 if Round > 5 else (Round-1)
    call set_the_scene (1, 0, 0, 0)

    $ Present[0].change_face("_sexy",1)
    if len(Present) >= 2:
        if Present[1] in all_Girls:
            $ Present[1].change_face("_sexy",1)
        else:
            $ Present.remove(Present[1])

    $ counter = len(Present)
    while counter:
        $ counter -= 1
        if Girl == EmmaX and "classcaught" in EmmaX.recent_history and AloneCheck(EmmaX):

            pass
        elif not approval_check(Present[counter], 600, TabM = 1,Alt=[[EmmaX],(650+Taboo*10)]) or (Present[counter] == EmmaX and Taboo and "taboo" not in EmmaX.history):
            if not approval_check(Present[counter], 400):
                if Present[counter] == RogueX:
                    ch_r "I'm just some sort'a gogo dancer now?"
                elif Present[counter] == KittyX:
                    ch_k "Like I would just dance for you?"
                elif Present[counter] == EmmaX:
                    ch_e "Oh, you think I'll dance to your tune?"
                elif Present[counter] == LauraX:
                    ch_l "I don't dance."
                elif Present[counter] == JeanX:
                    ch_j "I'm not in the mood."
                elif Present[counter] == StormX:
                    ch_s "I do not dance."
                elif Present[counter] == JubesX:
                    ch_v "I don't wanna dance, weirdo. . ."
            elif Present[counter].Taboo:
                if Present[counter] == RogueX:
                    ch_r "I don't think this is the best place for dance'n."
                elif Present[counter] == KittyX:
                    ch_k "I don't know, this really isn't a good place for it?"
                elif Present[counter] == EmmaX:
                    ch_e "You must be joking. Here?"
                elif Present[counter] == LauraX:
                    if approval_check(LauraX, 600, TabM = 0):
                        $ Present.append(LauraX)
                    else:
                        ch_l "I don't feel like it."
                elif Present[counter] == JeanX:
                    ch_j "I don't want to just randomly dance in public."
                elif Present[counter] == StormX:
                    ch_s "I would not want to make a scene."
                elif Present[counter] == JubesX:
                    ch_v "This isn't really the place for it. . ."
            else:
                if Present[counter] == RogueX:
                    ch_r "I dont feel it right now."
                elif Present[counter] == KittyX:
                    ch_k "I don't know, I don't really feel like dancing right now."
                elif Present[counter] == EmmaX:
                    ch_e "I don't really feel like dancing at the moment."
                elif Present[counter] == LauraX:
                    ch_l "I don't feel like it."
                elif Present[counter] == JeanX:
                    ch_j "I'm not in the mood."
                elif Present[counter] == StormX:
                    ch_s "I do not wish to dance right now."
                elif Present[counter] == JubesX:
                    ch_v "Yeah, I don't feel like dancing right now. . ."
            $ Present.remove(Present[counter])

    if not Present:
        return

    if EmmaX.location == bg_current and EmmaX not in Present:

        if "classcaught" not in EmmaX.history:
            if EmmaX.location == EmmaX.home:

                ch_e "If the two of you would like to dance, please do it elsewhere."
                $ Present = []
                return
            else:
                ch_e "I should really be going."
                call Remove_Girl (EmmaX)

    if "stripping" in Present[0].daily_history and approval_check(Present[0], 500, TabM = 3):
        $ Line = renpy.random.choice(["You liked the show earlier?",
                    "Didn't get enough earlier?",
                    "You're going to wear me out."])
    else:
        $ Line = renpy.random.choice(["Ok, that sounds fun.",
                    "I could get into that.",
                    "Yeah, ok."])

    Present[0].voice "[Line]"
    $ Line = 0

    call AllReset ("All")


    $ counter = len(Present)
    while counter:
        $ counter -= 1
        if Present[counter] == RogueX:
            show Rogue_sprite at Girl_Dance1(RogueX)
        elif Present[counter] == KittyX:
            show Kitty_sprite at Girl_Dance1(KittyX)
        elif Present[counter] == EmmaX:
            show Emma_Sprite at Girl_Dance1(EmmaX)
        elif Present[counter] == LauraX:
            show Laura_Sprite at Girl_Dance1(LauraX)
        elif Present[counter] == JeanX:
            show Jean_Sprite at Girl_Dance1(JeanX)
        elif Present[counter] == StormX:
            show Storm_Sprite at Girl_Dance1(StormX)
        elif Present[counter] == JubesX:
            show Jubes_Sprite at Girl_Dance1(JubesX)
        $ Present[counter].recent_history.append("stripping")
        $ Present[counter].daily_history.append("stripping")
        $ Present[counter].Strip += 1
        $ Present[counter].remaining_actions -= 1
        $ approval_bonusP[counter] = approval_bonus
        if Present[counter].SeenChest or Present[counter].SeenPussy:

            $ approval_bonusP[counter] += 20
        if Present[counter].SeenPanties:

            $ approval_bonusP[counter] += 5
        if "exhibitionist" in Present[counter].traits:
            $ approval_bonusP[counter] += (4*Taboo)
        if ("sex friend" in Present[counter].player_petnames or Present[counter] in Player.Harem) and not Taboo:
            $ approval_bonusP[counter] += 15
        elif "ex" in Present[counter].traits:
            $ approval_bonusP[counter] -= 40
        elif Present[counter].event_counter["forced"] and not Present[counter].Forced:
            $ approval_bonusP[counter] -= 5*Present[counter].event_counter["forced"]

    if len(Present) >= 2:
        "They start to dance."
        $ Partner = Present[1]
        $ between_event_count = 1
    else:
        "She starts to dance."
        $ between_event_count = 0
        $ Partner = 0


    if Girl == EmmaX and "classcaught" in EmmaX.recent_history and AloneCheck(EmmaX):

        $ Count = 0
        jump Group_Stripping


    $ BO = all_Girls[:]
    while BO:
        if BO[0].location == bg_current and BO[0] not in Present:
            $ Present.append(BO[0])
            if "stopdancing" not in BO[0].recent_history:
                $ BO[0].recent_history.append("stopdancing")
        $ BO.remove(BO[0])

    $ approval_bonus = approval_bonusP[0]
    $ primary_action = "strip"
    $ Count = 1

    while Count and Round >=10:

        $ Round -= 2 if Round > 2 else Round
        if len(Present) >= 2:
            $ Present[0].GLG(Present[1],600,1,1)
            $ Present[1].GLG(Present[0],600,1,1)
        menu:
            "Continue":
                pass
            "Would you kindly take off some clothes?":

                Present[0].voice "Hmm?"
                $ Count = 0
            "Stop":
                jump Group_Strip_End


    if EmmaX.location == bg_current and len(Present) >= 2:

        if "classcaught" not in EmmaX.history or "three" not in EmmaX.history or (Taboo and "taboo" not in EmmaX.history):
            if EmmaX.location == "bg_emma":

                ch_e "If the two of you would like to get indecent, please do it elsewhere."
                $ Present = []
                return
            else:
                ch_e "I should really be going."
                call Remove_Girl (EmmaX)

label Group_Stripping:
    while Round >= 10 and Present:
        $ Round -= 2 if Round > 2 else Round

        if Present[Count] != focused_Girl:
            call shift_focus (Present[Count])

        call Girl_Stripping (Present[Count])

        if len(Present) < 2 and Count != 0:
            $ Count = 0
        if not Present or not Present[Count]:
            jump Group_Strip_End
        if "stopdancing" in Present[Count].recent_history:

            if len(Present) >= 2 and "stopdancing" in Present[0].recent_history and "stopdancing" in Present[1].recent_history:
                jump Group_Strip_End

        $ primary_action = "strip"

        if not Present:

            jump Group_Strip_End

        if len(Present) >= 2 and Count != between_event_count:
            $ Present[Count].GLG(Present[between_event_count],800,2,1)
            $ Present[between_event_count].GLG(Present[Count],800,2,1)

        if len(Present) >= 2:


            if Count == 0 and "stopdancing" not in Present[1].recent_history:
                $ Count = 1
                $ between_event_count = 0
                $ approval_bonusP[1] = approval_bonus
                $ approval_bonus = approval_bonusP[0]
            elif Count == 1 and "stopdancing" not in Present[0].recent_history:
                $ Count = 0
                $ between_event_count = 1
                $ approval_bonusP[0] = approval_bonus
                $ approval_bonus = approval_bonusP[1]
            call shift_focus (Present[Count])


            call Activity_Check (focused_Girl, Partner)

        if len(Present) < 2 or "stopdancing" in Present[1].recent_history:

            $ approval_bonus = approval_bonusP[Count]
            $ Count = 0
            $ between_event_count = 0
            $ Partner = 0

            call Activity_Check (focused_Girl, Partner)

            if not Present or "stopdancing" in Present[0].recent_history:
                jump Group_Strip_End

    if Present and Round <=15:
        Present[0].voice "It's getting late, we should probably take a break."

label Group_Strip_End:

    if Present:
        $ Present[0].drain_word("stopdancing",1,0,0)
        $ Present[0].drain_word("keepdancing",1,0,0)
    if len(Present) >= 2:
        $ Present[1].drain_word("stopdancing",1,0,0)
        $ Present[1].drain_word("keepdancing",1,0,0)

    call set_the_scene (1, 0, 0, 0)
    $ Count = 0
    $ between_event_count = 0

    return




label Girl_Stripping(Girl=0, Nudist=0):

    if "stopdancing" in Girl.recent_history:

        return

    $ Girl.ArmPose = 2
    $ Girl.lust_face(1)

    if Girl == StormX and (StormX in Rules or Girl.Taboo <= 20):

        if Girl.Forced:
            $ Nudist = -40
        else:
            $ Nudist = Girl.Taboo
    if "keepdancing" not in Girl.recent_history:

        if Girl == JubesX and Girl.accessory and (Girl.top or Girl.bra) and (Girl.underwear or Girl.legs or Girl.HoseNum() >= 10):

            if approval_check(Girl, 750, TabM = 3):
                $ Girl.change_stat("obedience", 50, 1)
                $ Girl.change_stat("inhibition", 25, 1)
                $ Player.change_stat("focus", 60, 3)
                $ Line = Girl.accessory
                $ Girl.accessory = ""
                "She shrugs off her [Line] and throws it behind her."
            else:
                jump Strip_Ultimatum
        elif Girl == JubesX and Girl.accessory and Girl.top and (Girl.underwear or Girl.legs or Girl.HoseNum() >= 10):

            if approval_check(Girl, 750, TabM = 3):
                $ Girl.change_stat("obedience", 50, 1)
                $ Girl.change_stat("inhibition", 25, 1)
                $ Player.change_stat("focus", 60, 3)
                $ Line = Girl.accessory
                $ Girl.accessory = ""
                "She shrugs off her [Line] and throws it behind her."
            else:
                jump Strip_Ultimatum
        elif Girl.top and Girl.bra and (Girl.underwear or Girl.legs or Girl.HoseNum() >= 10):

            if approval_check(Girl, 750, TabM = 3,Alt=[[StormX],(300-Nudist*3)]):
                $ Girl.change_stat("obedience", 50, 1)
                $ Girl.change_stat("inhibition", 25, 1)
                $ Player.change_stat("focus", 60, 3)
                $ Line = Girl.top
                $ Girl.top = ""
                if Girl == KittyX:
                    "She drops her shoulders and her [Line] falls to the floor."
                else:
                    "She pulls her [Line] over her head and throws it behind her."
            else:
                jump Strip_Ultimatum

        elif Girl.legs and (Girl.underwear or Girl.HoseNum() >= 10):

            if approval_check(Girl, 1200, TabM = 3,Alt=[[StormX],(600-Nudist*3)]) or (Girl.SeenPanties and approval_check(Girl, 900, TabM = 3) and not Girl.Taboo):
                $ Girl.change_stat("lust", 50, 5)
                $ Girl.change_stat("obedience", 50, 1)
                $ Girl.change_stat("inhibition", 30, 1)
                $ Player.change_stat("focus", 60, 5)
                $ Line = Girl.legs
                $ Girl.legs = ""
                if Girl == KittyX:
                    "Her [Line] slide through her legs until they're only on her toes, before she kicks them to the floor."
                else:
                    "She unzips and pulls down her [Line], dropping them to the floor."
                if not Girl.SeenPanties:
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("obedience", 200, 3)
                    $ Girl.change_stat("inhibition", 50, 3)
                    $ Girl.change_stat("inhibition", 200, 2)
                    $ Girl.SeenPanties = 1
            else:
                jump Strip_Ultimatum

        elif Girl.hose:

            if Girl.HoseNum() >= 10:
                if approval_check(Girl, 1200, TabM = 3):
                    $ Girl.change_stat("lust", 50, 6)
                    $ Player.change_stat("focus", 60, 6)
                else:
                    jump Strip_Ultimatum

            elif Girl.HoseNum() >= 6 and approval_check(Girl, 1200, TabM = 3):
                if approval_check(Girl, 1200, TabM = 3,Alt=[[StormX],(600-Nudist*3)]):
                    $ Girl.change_stat("lust", 50, 4)
                    $ Player.change_stat("focus", 60, 4)
                else:
                    jump Strip_Ultimatum
            else:
                $ Player.change_stat("focus", 60, 3)
            $ Line = Girl.hose
            $ Girl.hose = ""
            if Girl == KittyX:
                "Her [Line] slide down off her legs, leaving them in a small pile."
            else:
                "She rolls the [Line] down off her legs, leaving them in a small pile."
            call expression Girl.tag + "_First_Bottomless" pass (1)

        elif Girl == JubesX and Girl.accessory and (Girl.underwear or Girl.legs or Girl.HoseNum() >= 10):

            if approval_check(Girl, 1250, TabM = 3) or (Girl.SeenChest and approval_check(Girl, 1000, TabM = 3) and not Girl.Taboo):
                $ Girl.change_stat("lust", 60, 5)
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("inhibition", 50, 10)
                $ Player.change_stat("focus", 80, 15)
                $ Line = Girl.accessory
                $ Girl.accessory = ""
                "She shrugs off her [Line] and throws it behind her."
                if not Girl.SeenChest:
                    $ Girl.change_face("_bemused", 1)
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_stat("obedience", 200, 4)
                    $ Girl.change_stat("inhibition", 50, 3)
                    $ Girl.change_stat("inhibition", 200, 3)
                    "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                    call expression Girl.tag + "_First_Topless" pass (1)
            else:
                jump Strip_Ultimatum
        elif Girl.top and not Girl.bra and (Girl.underwear or Girl.HoseNum() >= 10):

            if approval_check(Girl, 1250, TabM = 3,Alt=[[StormX],(650-Nudist*3)]) or (Girl.SeenChest and approval_check(Girl, 1000, TabM = 3) and not Girl.Taboo):
                $ Girl.change_stat("lust", 60, 5)
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("inhibition", 50, 10)
                $ Player.change_stat("focus", 80, 15)
                $ Line = Girl.top
                $ Girl.top = ""
                if not Girl.SeenChest:
                    $ Girl.change_face("_bemused", 1)
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_stat("obedience", 200, 4)
                    $ Girl.change_stat("inhibition", 50, 3)
                    $ Girl.change_stat("inhibition", 200, 3)
                    if Girl == KittyX:
                        "She hesitantly glances your way, and then with tug her [Line] passes through her, tossing it to the ground."
                    elif Girl in (EmmaX,LauraX,StormX):
                        "She glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                    else:
                        "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                    call expression Girl.tag + "_First_Topless" pass (1)
                else:
                    if Girl == KittyX:
                        "She drops her shoulders and her [Line] falls to the floor."
                    else:
                        "She pulls her [Line] over her head, tossing it to the ground."
            else:
                jump Strip_Ultimatum

        elif Girl.bra and not Girl.top:

            if approval_check(Girl, 1250, TabM = 3,Alt=[[StormX],(650-Nudist*3)]) or (Girl.SeenChest and approval_check(Girl, 1000, TabM = 3) and not Girl.Taboo):
                $ Girl.change_stat("lust", 60, 5)
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("inhibition", 50, 1)
                $ Player.change_stat("focus", 80, 15)
                $ Line = Girl.bra
                $ Girl.bra = ""
                if not Girl.SeenChest:
                    $ Girl.change_face("_bemused", 1)
                    if Girl == KittyX:
                        "She hesitantly glances your way, and then with a shrug pulls her [Line] through herself, tossing it to the ground."
                    elif Girl in (EmmaX,LauraX,StormX):
                        "She glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                    else:
                        "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_stat("obedience", 200, 4)
                    $ Girl.change_stat("inhibition", 50, 3)
                    $ Girl.change_stat("inhibition", 200, 3)
                    call expression Girl.tag + "_First_Topless" pass (1)
                else:
                    $ Girl.change_face("_sexy")
                    if Girl == KittyX:
                        "She pulls her [Line] through herself, tossing it to the ground."
                    else:
                        "She pulls her [Line] over her head, tossing it to the ground."
            else:
                jump Strip_Ultimatum

        elif Girl.legs:

            if approval_check(Girl, 1350, TabM = 3,Alt=[[StormX],(800-Nudist*3)]) or (Girl.SeenPussy and approval_check(Girl, 1100, TabM = 3) and not Girl.Taboo):
                $ Girl.change_stat("lust", 75, 10)
                $ Line = Girl.legs
                $ Girl.legs = ""
                if not Girl.SeenPussy:
                    $ Girl.change_stat("obedience", 60, 3)
                    $ Girl.change_stat("obedience", 200, 5)
                    $ Girl.change_stat("inhibition", 50, 4)
                    $ Girl.change_stat("inhibition", 200, 4)
                    if Girl == KittyX:
                        "She shyly looks up at you, and then slowly lets her [Line] slide to the floor."
                    elif Girl in (EmmaX,LauraX,JeanX):
                        "She hesitantly looks up at you, and then slowly unzips and pulls down her [Line], dropping them to the floor."
                    else:
                        "She shyly looks up at you, and then slowly unzips and pulls down her [Line], dropping them to the floor."
                    call expression Girl.tag + "_First_Bottomless" pass (1)
                else:
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Girl.change_stat("obedience", 75, 1)
                    if Girl == KittyX:
                        "She lets her [Line] pass through her legs, dropping them to the floor."
                    else:
                        "She unzips and pulls down her [Line], dropping them to the floor."
                    $ Girl.change_stat("inhibition", 70, 2)
                $ Player.change_stat("focus", 85, 15)
            else:
                jump Strip_Ultimatum

        elif Girl == JubesX and Girl.accessory:

            if approval_check(Girl, 1350, TabM = 3) or (Girl.SeenPussy and approval_check(Girl, 1100, TabM = 3) and not Girl.Taboo):
                $ Line = Girl.accessory
                $ Girl.accessory = ""
                if not Girl.SeenPussy:
                    $ Girl.change_stat("obedience", 60, 3)
                    $ Girl.change_stat("obedience", 200, 5)
                    $ Girl.change_stat("inhibition", 50, 4)
                    $ Girl.change_stat("inhibition", 200, 4)
                    "She hesitantly glances your way, and then with a shrug pulls her [Line] off, tossing it to the ground."
                    call expression Girl.tag + "_First_Bottomless" pass (1)
                else:
                    "She shrugs her [Line] off, tossing it to the ground."

                if not Girl.bra or Girl.top_pulled_up:
                    if not Girl.SeenChest:
                        $ Girl.change_stat("obedience", 50, 3)
                        $ Girl.change_stat("inhibition", 50, 3)
                        call expression Girl.tag + "_First_Topless" pass (1)
                    else:
                        $ Girl.change_stat("lust", 60, 15)
                        $ Girl.change_stat("obedience", 50, 3)
                        $ Girl.change_stat("obedience", 75, 1)
                        $ Girl.change_stat("inhibition", 50, 3)
                else:
                    $ Girl.change_stat("lust", 75, 10)
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Girl.change_stat("obedience", 75, 1)
                    $ Girl.change_stat("inhibition", 70, 2)
                $ Player.change_stat("focus", 85, 15)
            else:
                jump Strip_Ultimatum
        elif Girl.top and not Girl.underwear:

            if approval_check(Girl, 1350, TabM = 3,Alt=[[StormX],(800-Nudist*3)]) or (Girl.SeenPussy and approval_check(Girl, 1100, TabM = 3) and not Girl.Taboo):
                $ Line = Girl.top
                $ Girl.top = ""
                if not Girl.SeenPussy:
                    $ Girl.change_stat("obedience", 60, 3)
                    $ Girl.change_stat("obedience", 200, 5)
                    $ Girl.change_stat("inhibition", 50, 4)
                    $ Girl.change_stat("inhibition", 200, 4)
                    if Girl == KittyX:
                        "She hesitantly glances your way, and then with a tug pulls her [Line] through herself, tossing it to the ground."
                    elif Girl in (EmmaX,LauraX,StormX):
                        "She glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                    else:
                        "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                    call expression Girl.tag + "_First_Bottomless" pass (1)
                else:
                    if Girl == KittyX:
                        "She drops her shoulders and her [Line] falls to the floor."
                    else:
                        "She pulls her [Line] over her head, tossing it to the ground."

                if not Girl.bra or Girl.top_pulled_up:
                    if not Girl.SeenChest:
                        $ Girl.change_stat("obedience", 50, 3)
                        $ Girl.change_stat("inhibition", 50, 3)
                        call expression Girl.tag + "_First_Topless" pass (1)
                    else:
                        $ Girl.change_stat("lust", 60, 15)
                        $ Girl.change_stat("obedience", 50, 3)
                        $ Girl.change_stat("obedience", 75, 1)
                        $ Girl.change_stat("inhibition", 50, 3)
                else:
                    $ Girl.change_stat("lust", 75, 10)
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Girl.change_stat("obedience", 75, 1)
                    $ Girl.change_stat("inhibition", 70, 2)
                $ Player.change_stat("focus", 85, 15)
            else:
                jump Strip_Ultimatum

        elif Girl.bra:

            if approval_check(Girl, 1250, TabM = 3,Alt=[[StormX],(750-Nudist*3)]) or (Girl.SeenChest and approval_check(Girl, 1100, TabM = 3) and not Girl.Taboo):
                $ Girl.change_stat("lust", 60, 5)
                $ Line = Girl.bra
                $ Girl.bra = ""
                if not Girl.SeenChest:
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_stat("obedience", 200, 4)
                    $ Girl.change_stat("inhibition", 50, 3)
                    $ Girl.change_stat("inhibition", 200, 3)
                    if Girl == KittyX:
                        "She hesitantly glances your way, and then with a tug pulls her [Line] through herself, tossing it to the ground."
                    elif Girl in (EmmaX,LauraX,StormX):
                        "She glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                    else:
                        "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                    call expression Girl.tag + "_First_Topless" pass (1)
                else:
                    $ Girl.change_stat("obedience", 50, 2)
                    if Girl == KittyX:
                        "She drops her shoulders and her [Line] falls to the floor."
                    else:
                        "She pulls her [Line] over her head, tossing it to the ground."
                    $ Girl.change_stat("inhibition", 50, 1)
                $ Player.change_stat("focus", 80, 15)
            else:
                jump Strip_Ultimatum

        elif Girl.underwear:

            if approval_check(Girl, 1350, TabM = 3,Alt=[[StormX],(800-Nudist*3)]) or (Girl.SeenPussy and approval_check(Girl, 1100, TabM = 3) and not Girl.Taboo):
                $ Girl.change_stat("lust", 75, 10)
                $ Line = Girl.underwear
                $ Girl.underwear = ""
                if not Girl.SeenPussy:
                    $ Girl.change_stat("obedience", 60, 3)
                    $ Girl.change_stat("obedience", 200, 5)
                    $ Girl.change_stat("inhibition", 50, 4)
                    $ Girl.change_stat("inhibition", 200, 4)
                    if Girl == KittyX:
                        "She shyly looks up at you, and then slowly tugs her [Line] off, flinging them to the side."
                    elif Girl in (EmmaX,LauraX):
                        "She looks up at you, and then slowly pulls her [Line] down, kicking them off to the side."
                    else:
                        "She shyly looks up at you, and then slowly pulls her [Line] down, kicking them off to the side."
                    call expression Girl.tag + "_First_Bottomless" pass (1)
                else:
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Girl.change_stat("obedience", 75, 1)
                    if Girl == KittyX:
                        "She looks up at you, and then gently pulls her [Line] off, flicking them to the side."
                    else:
                        "She looks up at you, and then gently pulls her [Line] down, kicking them off to the side."
                    $ Girl.change_stat("inhibition", 70, 2)
                $ Player.change_stat("focus", 85, 15)
            else:
                jump Strip_Ultimatum
        else:

            $ Girl.change_face("_sexy")
            if Girl == RogueX:
                ch_r "I'm afraid that's all I have on, [Girl.player_petname]. . ."
            elif Girl == KittyX:
                ch_k "It looks like I've run out of clothes. . ."
            elif Girl == EmmaX:
                ch_e "Well, it appears I've run out of clothes, [Girl.player_petname]. . ."
            elif Girl == LauraX:
                ch_l "Well, that's all I've got, [Girl.player_petname]. . ."
            elif Girl == JeanX:
                ch_j "I'm all out of clothes. . ."
            elif Girl == StormX:
                ch_s "I appear to have lost my clothing. . ."
            elif Girl == JubesX:
                ch_v "Well, it looks like I'm done here. . ."
            menu:
                extend ""
                "Ok, you can stop":
                    $ Girl.recent_history.append("stopdancing")
                    call expression Girl.tag + "_Pos_Reset"
                "Keep on dancing":
                    $ Girl.recent_history.append("keepdancing")


    $ Girl.change_stat("lust", 70, 2)
    if "exhibitionist" in Girl.traits:
        $ Girl.change_stat("lust", 200, 2)
    $ Player.change_stat("focus", 60, 3)
    if offhand_action == "jackin":
        $ Girl.change_stat("lust", 200, 2)
        $ Player.change_stat("focus", 200, 5)

    if not Player.semen and Player.focus >= 50:
        $ Player.focus = 50

    if Player.focus >= 100 or Girl.lust >= 100:


        if Player.focus >= 100:

            call Player_Cumming (Girl)
            if "_angry" in Girl.recent_history:
                return
            $ Girl.change_stat("lust", 200, 5)
            if not Player.semen and offhand_action == "jackin":
                "You're spitting dust here, maybe just watch quietly for a while."
                $ offhand_action = 0
            if Player.focus > 80:
                jump Group_Strip_End

        if Girl.lust >= 100:

            call Girl_Cumming (Girl)
            if action_context == "shift" or "_angry" in Girl.recent_history:
                $ Count = 0
                jump Group_Strip_End

        call AllReset (Girl)

        if Girl == RogueX:
            show Rogue_sprite at Girl_Dance1(Girl)
        elif Girl == KittyX:
            show Kitty_sprite at Girl_Dance1(Girl)
        elif Girl == EmmaX:
            show Emma_Sprite at Girl_Dance1(Girl)
        elif Girl == LauraX:
            show Laura_Sprite at Girl_Dance1(Girl)
        elif Girl == JeanX:
            show Jean_Sprite at Girl_Dance1(Girl)
        elif Girl == StormX:
            show Storm_Sprite at Girl_Dance1(Girl)
        elif Girl == JubesX:
            show Jubes_Sprite at Girl_Dance1(Girl)

        "[Girl.name] begins to dance again."

    if Partner and Partner.lust >= 100:

        call Girl_Cumming (Partner)

    menu:
        "[Girl.name] should. . ."
        "Keep Going. . ." if "keepdancing" not in Girl.recent_history:
            $ Girl.eyes = "_sexy"
            if Girl.love >= 700 or Girl.obedience >= 500:
                if not approval_bonus:
                    $ approval_bonus = 10
                elif approval_bonus <= 20:
                    $ approval_bonus += 1
            if Taboo and Girl.Strip <= 10:
                $ Girl.change_stat("obedience", 50, 7)
            elif Taboo or Girl.Strip <= 10:
                $ Girl.change_stat("obedience", 50, 5)
            elif Girl.Strip <= 50:
                $ Girl.change_stat("obedience", 50, 3)
        "Keep Dancing. . ." if "keepdancing" in Girl.recent_history:
            $ Girl.eyes = "_sexy"

        "Stop stripping, keep dancing" if "keepdancing" not in Girl.recent_history:
            if Girl == RogueX:
                ch_r "Ok. . ."
            elif Girl == KittyX:
                ch_k "K. . ."
            elif Girl == EmmaX:
                ch_e "Oh? Very well."
            elif Girl == LauraX:
                ch_l "Huh? I guess. . ."
            elif Girl == JeanX:
                ch_j "Ok, sure."
            elif Girl == StormX:
                ch_s "Fine. . ."
            elif Girl == JubesX:
                ch_v "Oh, well ok. . ."
            $ Girl.recent_history.append("keepdancing")

        "Start stripping again" if "keepdancing" in Girl.recent_history:
            $ Girl.recent_history.remove("keepdancing")
            if "stripforced" in Girl.recent_history:
                Girl.voice ". . ."
            else:
                if Girl == RogueX:
                    ch_r "Hmm. . ."
                elif Girl == KittyX:
                    ch_k "Huh?"
                else:
                    Girl.voice "Hmm. . ."
        "Just watch silently":

            if "watching" not in Girl.recent_history:
                if "keepdancing" not in Girl.recent_history:
                    if Taboo and Girl.Strip <= 10:
                        $ Girl.change_stat("inhibition", 50, 3)
                    elif Taboo or Girl.Strip <= 10:
                        $ Girl.change_stat("inhibition", 50, 1)
                elif Girl.Strip <= 50:
                    $ Girl.change_stat("inhibition", 50, 2)
                    $ Girl.change_stat("lust", 70, 2)
                $ Girl.recent_history.append("watching")

        "Start jack'in it." if offhand_action != "jackin":
            call Jackin (Girl)
        "Stop jack'in it." if offhand_action == "jackin":
            $ offhand_action = 0

        "Lose the [Girl.arms]. . ." if Girl.arms:
            $ Girl.change_face("_surprised")
            $ Girl.mouth = "_kiss"
            Girl.voice "All right, [Girl.player_petname]."
            $ Girl.change_face("_sexy")
            $ Girl.arms = ""
        "Ok, that's enough.":

            if Girl == RogueX:
                ch_r "Ok, [Girl.player_petname]. . . "
            elif Girl == KittyX:
                ch_k "Ok. . ."
            else:
                Girl.voice "Alright, [Girl.player_petname]."
            $ renpy.pop_call()
            jump Group_Strip_End

    return


label Strip_Ultimatum:
    if "keepdancing" in Girl.recent_history:
        return

    call expression Girl.tag + "_Pos_Reset"

    $ Girl.change_face("_bemused", 1)
    if "stripforced" in Girl.recent_history:
        $ Girl.change_face("_sad", 1)
        if Girl == RogueX:
            ch_r "That's as far as I care to go, [Girl.player_petname]."
        elif Girl == KittyX:
            ch_k "That's all you get."
        elif Girl == EmmaX:
            ch_e "I think that's plenty, [Girl.player_petname]."
        elif Girl == LauraX:
            ch_l "Last call, [Girl.player_petname]."
        elif Girl == JeanX:
            ch_j "Ok, that's my limit."
        elif Girl == StormX:
            ch_s "I will go no further. . ."
        elif Girl == JubesX:
            ch_v "Ok, that's all you get. . ."
    else:
        if Girl == RogueX:
            ch_r "I'm sorry, [Girl.player_petname], I'm not ready to show you more. . . Yet."
        elif Girl == KittyX:
            ch_k "I don't know, [Girl.player_petname], that's as far as I'll go for now."
        elif Girl == EmmaX:
            ch_e "I'm afraid that's as far as I'm ready to go, [Girl.player_petname]. . . for now."
        elif Girl == LauraX:
            ch_l "Ok, that's enough, [Girl.player_petname]. . . for now."
        elif Girl == JeanX:
            ch_j "Ok, I think you've seen enough. . ."
        elif Girl == StormX:
            ch_s "That's enough for now. . ."
        elif Girl == JubesX:
            ch_v "I'm kinda done here. . ."
    menu:
        extend ""
        "That's ok, you can stop.":
            if "ultimatum" not in Girl.daily_history:
                $ Girl.change_stat("love", 50, 2)
                $ Girl.change_stat("love", 90, 2)
                $ Girl.change_stat("inhibition", 50, 2)
                $ Girl.daily_history.append("ultimatum")
            $ Girl.recent_history.append("stopdancing")
            return
        "That's ok, but keep dancing for a bit. . .":
            if "ultimatum" not in Girl.daily_history:
                $ Girl.change_stat("love", 50, 2)
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("inhibition", 50, 2)
                $ Girl.daily_history.append("ultimatum")
            $ Girl.recent_history.append("keepdancing")
            if "stripforced" in Girl.recent_history:
                Girl.voice ". . ."
            else:
                if Girl == RogueX:
                    ch_r "Heh, ok [Girl.player_petname]."
                elif Girl == KittyX:
                    ch_k "Heh, alright."
                elif Girl == EmmaX:
                    ch_e "Oh, if I must, [Girl.player_petname]."
                elif Girl == LauraX:
                    ch_l "Eh? Fine."
                elif Girl == JeanX:
                    ch_j "Ok, sure."
                elif Girl == StormX:
                    ch_s "Very well. . ."
                elif Girl == JubesX:
                    ch_v "Ok, sure. . ."
        "You'd better." if Girl.Forced:
            if not approval_check(Girl, 500, "O", TabM=5) and not approval_check(Girl, 800, "L", TabM=5):
                $ Girl.change_face("_angry")
                if Girl == RogueX:
                    ch_r "I don't know who you think I am, but I ain't gonna just jump when you say \"toad\"."
                    ch_r "I think we're done here for now."
                elif Girl == KittyX:
                    ch_k "I'm not just going to do \"whatever\"!"
                    ch_k "I'm done with this."
                elif Girl == EmmaX:
                    ch_e "I think you're overstepping your bounds here, [Girl.player_petname]."
                    ch_e "Remember your place."
                elif Girl == LauraX:
                    ch_l "I don't like that tone, [Girl.player_petname]."
                elif Girl == JeanX:
                    ch_j "Don't talk to me like that. -I- talk to -you- like that."
                elif Girl == StormX:
                    ch_s "I do not appreciate that tone."
                elif Girl == JubesX:
                    ch_v "I'd better not break your face either. . ."
                $ Girl.recent_history.append("_angry")
                $ Girl.daily_history.append("_angry")
                call Remove_Girl (Girl)
                return
            $ approval_bonus += 20
            $ Girl.Forced += 1
            $ Girl.change_face("_sad")
            if "stripforced" in Girl.recent_history:
                $ Girl.change_face("_angry")
                Girl.voice ". . ."
            else:
                if Girl == RogueX:
                    ch_r "I. . . guess I could. . ."
                elif Girl == KittyX:
                    ch_k "I. . . could show a bit more. . ."
                elif Girl == EmmaX:
                    ch_e "Hmm, forceful. . ."
                elif Girl == LauraX:
                    ch_l "Grrrr. . ."
                elif Girl == JeanX:
                    ch_j ". . . fine."
                elif Girl == StormX:
                    ch_s ". . ."
                elif Girl == JubesX:
                    ch_v "Well. . . ok. . ."
                $ Girl.recent_history.append("stripforced")
            $ Girl.change_stat("love", 200, -40)
        "You can do better than that. Keep going." if not Girl.Forced:
            if not approval_check(Girl, 300, "O", TabM=5) and not approval_check(Girl, 700, "L", TabM=5):
                $ Girl.change_face("_angry")
                if Girl == RogueX:
                    ch_r "I don't know who you think I am, but I ain't gonna just jump when you say \"toad\"."
                    ch_r "I think we're done here for now."
                elif Girl == KittyX:
                    ch_k "I'm not just going to do \"whatever\"!"
                    ch_k "I'm done with this."
                elif Girl == EmmaX:
                    ch_e "I think you're overstepping your bounds here, [Girl.player_petname]."
                    ch_e "Remember your place."
                elif Girl == LauraX:
                    ch_l "I don't like that tone, [Girl.player_petname]."
                elif Girl == JeanX:
                    ch_j "Don't talk to me like that. -I- talk to -you- like that."
                elif Girl == StormX:
                    ch_s "No, I do not think so."
                elif Girl == JubesX:
                    ch_v "Oh, I can, but you're not goinna see it. . ."
                $ Girl.recent_history.append("_angry")
                $ Girl.daily_history.append("_angry")
                call Remove_Girl (Girl)
                return
            $ Girl.change_stat("love", 200, -10)
            $ Girl.change_stat("obedience", 50, 3)
            $ Girl.change_stat("obedience", 75, 5)
            $ approval_bonus += 20
            $ Girl.Forced += 1
            $ Girl.change_face("_sad")
            if Girl == RogueX:
                ch_r "Well, if you insist. . ."
            elif Girl == KittyX:
                ch_k "I mean, maybe. . ."
            elif Girl == EmmaX:
                ch_e "I can't imagine doing better than \"perfection\". . ."
            elif Girl == LauraX:
                ch_l ". . . Right. . ."
            elif Girl == JeanX:
                ch_j "I don't see how anyone could. . ."
            elif Girl == StormX:
                ch_s "We shall see. . ."
            elif Girl == JubesX:
                ch_v "Ok, how about this. . ."
    if "ultimatum" not in Girl.daily_history:
        $ Girl.daily_history.append("ultimatum")

    if Girl == RogueX:
        show Rogue_sprite at Girl_Dance1(Girl)
    elif Girl == KittyX:
        show Kitty_sprite at Girl_Dance1(Girl)
    elif Girl == EmmaX:
        show Emma_Sprite at Girl_Dance1(Girl)
    elif Girl == LauraX:
        show Laura_Sprite at Girl_Dance1(Girl)
    elif Girl == JeanX:
        show Jean_Sprite at Girl_Dance1(Girl)
    elif Girl == StormX:
        show Storm_Sprite at Girl_Dance1(Girl)
    elif Girl == JubesX:
        show Jubes_Sprite at Girl_Dance1(Girl)
    "[Girl.name] begins to dance again."
    return

transform Girl_Dance1(Chr=focused_Girl):
    subpixel True
    pos (Chr.sprite_location, 50)
    xoffset 0
    yoffset 0
    choice:
        parallel:
            ease 2.5 xoffset -40
            ease 2.5 xoffset 0
        parallel:
            easeout 1.0 yoffset 30
            linear 0.5 yoffset 40
            easein 1.0 yoffset 0
            easeout 1.0 yoffset 40
            linear 0.5 yoffset 50
            easein 1.0 yoffset 0
    choice:
        parallel:
            ease 2.5 xoffset 40
            ease 2.5 xoffset 0
        parallel:
            easeout 1.0 yoffset 30
            linear 0.5 yoffset 40
            easein 1.0 yoffset 0
            easeout 1.0 yoffset 40
            linear 0.5 yoffset 50
            easein 1.0 yoffset 0
    choice (0.3):
        parallel:
            ease 2.5 xoffset -30
            ease 2.5 xoffset 0
        parallel:
            ease 1.5 yoffset 150
            ease 3.5 yoffset 0
    repeat
