
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

            if Girl.top not in ("_mesh_top","_pink_top","jacket"):
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
            show Kitty_Sprite at Girl_Dance1(KittyX)
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
            show Kitty_Sprite at Girl_Dance1(Girl)
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
        show Kitty_Sprite at Girl_Dance1(Girl)
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




label Les_Interupted(Girl=0, BO=[]):
    $ Girl = GirlCheck(Girl)

    if "unseen" not in Girl.recent_history:
        if Girl.event_counter["orgasmed"]< 3 and Girl.remaining_actions:
            menu:
                "Did you want to stop them?"
                "Yeah.":
                    pass
                "No, let them keep going.":
                    $ Girl.remaining_actions -= 1 if Girl.remaining_actions > 0 else 0
                    jump Les_Cycle
        else:
            if Girl == LauraX:
                ch_l "Ahhh, that hit the spot. . ."
            else:
                Girl.voice "Ok, that's probably enough of that. . ."
        jump Les_After
    $ Girl.drain_word("unseen",1,0)
    $ Partner.drain_word("unseen",1,0)

    $ Girl.change_face("_surprised", 1)
    $ Partner.change_face("_surprised",2)

    "Suddenly, [Girl.name] jerks up from what she was doing with a start, and gives [Partner.name] a nudge."
    $ Girl.change_face("_bemused", 0)
    $ Partner.change_face("_perplexed",1)

    if Girl == RogueX:
        ch_r "Um, [Player.name], how long have you been watchin?"
    elif Girl == KittyX:
        ch_k "Eep! [Player.name], how long have you been there?!"
    elif Girl == EmmaX:
        ch_e "Hmm? [Girl.player_petname], enjoying the show?"
    elif Girl == LauraX:
        ch_l "Oh! Hey [Player.name], how long have you been there?"
    elif Girl == JeanX:
        ch_j "Oh, hey [Player.name], get a good look?"
    elif Girl == StormX:
        ch_s "Oh? Hello [Girl.player_petname]. Were you there long?"
    elif Girl == JubesX:
        ch_v "Oh? hey [Girl.player_petname]. What'd you see?"
    $ Girl.remaining_actions -= 1 if Girl.remaining_actions > 0 else 0
    call checkout (1)
    $ Line = 0


    if offhand_action == "jackin":
        $ Girl.eyes = "_down"
        if Girl == RogueX:
            ch_r "And why is your cock out like that?!"
        elif Girl == KittyX:
            ch_k "and why are you fapping?!"
        elif Girl == EmmaX:
            ch_e "and was. . . that. . really an appropriate reaction?"
        elif Girl == LauraX:
            ch_l "Looks like you're taking care of yourself."
        elif Girl == JeanX:
            ch_j "You seem to be enjoying yourself. . ."
        elif Girl == StormX:
            ch_s "It appears you kept yourself busy."
        elif Girl == JubesX:
            ch_v "Looks like it got your attention."
        menu:
            extend ""
            "Yeah, it was an excellent show.":
                $ Girl.change_face("_sexy")
                $ Girl.change_stat("obedience", 50, 3)
                $ Girl.change_stat("obedience", 70, 2)
                "[Girl.name] glances over at [Partner.name]."
                if Girl == RogueX:
                    ch_r "Well, I imagine it was. . ."
                elif Girl == KittyX:
                    ch_k "I mean, I guess. . ."
                elif Girl == EmmaX:
                    ch_e "I suppose it was. . ."
                elif Girl == LauraX:
                    ch_l "I get that. . ."
                elif Girl == JeanX:
                    ch_j "Yeah, she's ok. . ."
                elif Girl == StormX:
                    ch_s "Yes, I suppose so."
                elif Girl == JubesX:
                    ch_v "Hear that? We're stars."
                if Girl.love >= 800 or Girl.obedience >= 500 or Girl.inhibition >= 500:
                    $ approval_bonus += 10
                    $ Girl.change_stat("lust", 90, 5)
                    if Girl == RogueX:
                        ch_r "And the view from this angle ain't so bad either. . ."
                    elif Girl == KittyX:
                        ch_k "And[Girl.like]you're not so bad yourself. . ."
                    elif Girl == EmmaX:
                        ch_e "And at least you make good eye candy. . ."
                    elif Girl == LauraX:
                        ch_l "You're not so bad to look at either. . ."
                    elif Girl == JeanX:
                        ch_j "You're looking good too. . "
                    elif Girl == StormX:
                        ch_s "And you might make a fine addition. . ."
                    elif Girl == JubesX:
                        ch_v "Care to join us?"
            "I. . . just got here?":


                $ Girl.change_face("_angry")
                $ Girl.change_stat("love", 70, 2)
                $ Girl.change_stat("love", 90, 1)
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("obedience", 70, 2)
                "She looks pointedly at your cock,"
                if Girl == RogueX:
                    ch_r "Suuure . . ."
                elif Girl == KittyX:
                    ch_k "Riiight. . ."
                elif Girl == EmmaX:
                    ch_e "I'm sure. . ."
                elif Girl == LauraX:
                    ch_l "Uh HUH. . ."
                elif Girl == JeanX:
                    ch_j "Sure. . ."
                elif Girl == StormX:
                    ch_s "I believe you."
                elif Girl == JubesX:
                    ch_v "Of course you did."
                if Girl.love >= 800 or Girl.obedience >= 500 or Girl.inhibition >= 500:
                    $ approval_bonus += 10
                    $ Girl.change_stat("lust", 90, 5)
                    $ Girl.change_face("_bemused", 1)
                    if Girl == RogueX:
                        ch_r "-but I guess we were pretty tempting. . ."
                    elif Girl == KittyX:
                        ch_k "-I can't exactly blame you though. . ."
                    elif Girl == EmmaX:
                        ch_e "not that I can blame you. . ."
                    elif Girl == LauraX:
                        ch_l "-can't blame you though."
                    elif Girl == JeanX:
                        ch_j "You missed some fun stuff. . ."
                    elif Girl == StormX:
                        ch_s ". . . but it's too bad you missed the fun."
                    elif Girl == JubesX:
                        ch_v "Too bad you missed the fun. . ."
                else:
                    $ approval_bonus -= 10
                    $ Girl.change_stat("lust", 200, -5)

        call Seen_First_Peen (Girl, Partner)
    else:


        menu:
            extend ""
            "Long enough.":
                $ Girl.change_face("_sexy", 1)
                $ Girl.change_stat("obedience", 50, 3)
                $ Girl.change_stat("obedience", 70, 2)
                if Girl == RogueX:
                    ch_r "Well I hope you got a good show out of it. . ."
                elif Girl == KittyX:
                    ch_k "I guess we[Girl.like]really put on a show, huh. . ."
                elif Girl == EmmaX:
                    ch_e "I supppose we did make a show of ourselves. . ."
                elif Girl == LauraX:
                    ch_l "Didn't intend to put on a show. . ."
                elif Girl == JeanX:
                    ch_j "I'll bet. . ."
                elif Girl == StormX:
                    ch_s "Yes, I suppose so."
                elif Girl == JubesX:
                    ch_v "Hate to think you missed it. . ."
            "I just got here.":
                $ Girl.change_face("_bemused", 1)
                $ Girl.change_stat("love", 70, 2)
                $ Girl.change_stat("love", 90, 1)
                if Girl == RogueX:
                    ch_r "A likely story . . ."
                elif Girl == KittyX:
                    ch_k "Uh HUH. . ."
                elif Girl == EmmaX:
                    ch_e "I'm sure. . ."
                elif Girl == LauraX:
                    ch_l "Uh HUH. . ."
                elif Girl == JeanX:
                    ch_j "Sure. . ."
                elif Girl == StormX:
                    ch_s "I believe you."
                elif Girl == JubesX:
                    ch_v "Of course you did."
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("obedience", 70, 2)

    if not approval_check(Girl, 1350):

        $ Girl.change_stat("love", 200, -5)
        $ Girl.change_face("_angry")
        $ Girl.recent_history.append("_angry")
        $ Girl.daily_history.append("_angry")
        if Girl == RogueX:
            ch_r "You should get out of here right now, and maybe learn ta knock?"
        elif Girl == KittyX:
            ch_k "So maybe you could[Girl.like]leave us to it?"
        elif Girl == EmmaX:
            ch_e "So perhaps you could leave us to it?"
        elif Girl == LauraX:
            ch_l "So maybe just leave us to it?"
        elif Girl == JeanX:
            ch_j "Ok, so. . . we'd like to get back to it. . ."
        elif Girl == StormX:
            ch_s "If that will be all, I'd like you to leave."
        elif Girl == JubesX:
            ch_v "Ok, but, um, get going now."
        $ renpy.pop_call()
        $ renpy.pop_call()
        if bg_current == "bg_player":
            jump Campus_Map
        else:
            jump Player_Room

    if Round <= 10:

        if Girl == RogueX:
            ch_r "It's getting too late to do much about it right now though."
        elif Girl == KittyX:
            ch_k "We were just about to take a break though."
        elif Girl == EmmaX:
            ch_e "I suppose it was time for a break. . ."
        elif Girl == LauraX:
            ch_l "I guess we could take a break though."
        elif Girl == JeanX:
            ch_j "We could use a break though. . ."
        elif Girl == StormX:
            ch_s "I believe we were just about to take a break though. . ."
        elif Girl == JubesX:
            ch_v "We need to take a minute though. . ."
        return
    $ action_context = "interrupted"

label LesScene(Girl=0, Bonus=0, BO=[]):
    $ Girl = GirlCheck(Girl)
    call shift_focus (Girl)

    if not Girl.remaining_actions:

        call Sex_Basic_Dialog (Girl, "tired")
        return

    if Girl.event_counter["seen_with_girl"]:
        $ approval_bonus += 10
    elif Girl.event_counter["been_with_girl"]:
        $ approval_bonus += 5
    if Girl.SEXP >= 50:
        $ approval_bonus += 25
    elif Girl.SEXP >= 30:
        $ approval_bonus += 15
    elif Girl.SEXP >= 15:
        $ approval_bonus += 5

    if Girl.lust >= 90:
        $ approval_bonus += 5
    elif Girl.lust >= 75:
        $ approval_bonus += 5

    elif Girl.inhibition >= 750:
        $ approval_bonus += 5

    if "exhibitionist" in Girl.traits:
        $ approval_bonus += (3*Taboo)

    if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
        $ approval_bonus += 10
    elif "ex" in Girl.traits:
        $ approval_bonus -= 40

    if Partner not in all_Girls:
        $ Partner = 0
        $ BO = all_Girls[:]
        $ BO.remove(Girl)
        while BO:
            if BO[0].location == bg_current:
                $ Partner = BO[0]
                $ BO = [1]
            $ BO.remove(BO[0])

    if Girl == JeanX:

        call Girl_Whammy (Partner)
    elif Partner == JeanX:

        call Girl_Whammy (Girl)

    $ Line = Girl.GirlLikeCheck(Partner)
    if Line >= 900:
        $ Bonus += 150
    elif Line >= 800 or "poly "+Partner.tag in Girl.traits:
        $ Bonus += 100
    elif Line >= 700:
        $ Bonus += 50
    elif Line <= 200:
        $ Bonus -= 200
    elif Line <= 500:
        $ Bonus -= 100
    $ Partner.drain_word("unseen",1,0)
    $ Line = 0

    $ Girl.add_word(1,"noticed "+Partner.tag,"noticed "+Partner.tag)
    $ Partner.add_word(1,"noticed "+Girl.tag,"noticed "+Girl.tag)

    if bg_current in PersonalRooms:
        $ Taboo = 0
        $ Girl.Taboo = 0
        $ Partner.Taboo = 0
    if Girl.event_counter["forced"] and not Girl.Forced:
        $ approval_bonus -= 5*Girl.event_counter["forced"]

    $ approval = approval_check(Girl, 1350, TabM = 2, Bonus = Bonus)

    $ Girl.drain_word("unseen",1,0)

    if action_context == "interrupted":
        menu:
            extend ""
            "I guess I should probably get going then. . .":
                $ Girl.change_stat("love", 80, 3)
                if approval >= 2:

                    if Girl == RogueX:
                        ch_r "Well, I didn't say you had to leave. . ."
                    elif Girl == KittyX:
                        ch_k "Hmmmm, I don't know about that. . ."
                    elif Girl == EmmaX:
                        ch_e "Well, if [Partner.tag]'s game. . ."
                    elif Girl == LauraX:
                        ch_l "Hmmmm, I don't know about that. . ."
                    elif Girl == JeanX:
                        ch_j "Well, you don't -have- to. . ."
                    elif Girl == StormX:
                        ch_s "That really won't be necessary."
                    elif Girl == JubesX:
                        ch_v "Orrr. . . you could join us?"
                    call Les_Response (Partner, Girl, 3, B2=Bonus)
                    if not _return:
                        return
                else:

                    call Les_Response (Partner, Girl, 1, B2=Bonus)
                    if not _return:

                        if approval:
                            if Girl == RogueX:
                                ch_r "I mean, you can hang out. . ."
                            elif Girl == KittyX:
                                ch_k "You could at least stick around. . ."
                            elif Girl == EmmaX:
                                ch_e "Well, you could at least stay for a bit. . ."
                            elif Girl == LauraX:
                                ch_l "You could chill here."
                            elif Girl == JeanX:
                                ch_j "Well, you can still stick around. . ."
                            elif Girl == StormX:
                                ch_s "Then you could at least stay and chat for a bit."
                            elif Girl == JubesX:
                                ch_v "Well then, just hang out for a bit."
                            return
                        else:
                            if Girl == RogueX:
                                ch_r "Yeah, that's probably a good idea. . ."
                            elif Girl == KittyX:
                                ch_k "I guess so. . ."
                            elif Girl == EmmaX:
                                ch_e "I suppose. . ."
                            elif Girl == LauraX:
                                ch_l "Yeah. . ."
                            elif Girl == JeanX:
                                ch_j "Oh, fine. . ."
                            elif Girl == StormX:
                                ch_s "I am sorry, [Girl.player_petname]. Perhaps some other time."
                            elif Girl == JubesX:
                                ch_v "Oh, bummer, well see you later then."
                            $ renpy.pop_call()
                            $ renpy.pop_call()
                            if bg_current == "bg_player":
                                jump Campus_Map
                            else:
                                jump Player_Room
                    elif not approval:

                        if Girl == RogueX:
                            ch_r "I'm sorry [Girl.player_petname], I just am not interested in putting on a show."
                        elif Girl == KittyX:
                            ch_k "Sorry [Girl.player_petname], I guess we'd like to keep this private."
                        elif Girl == EmmaX:
                            ch_e "So sorry [Girl.player_petname], I suppose we'd like to keep this private."
                        elif Girl == LauraX:
                            ch_l "Sorry [Girl.player_petname], maybe come back later."
                        elif Girl == JeanX:
                            ch_j "Hope you enjoyed the show, but we're a little busy. . ."
                        elif Girl == StormX:
                            ch_s "Well I'm afraid that I would rather you didn't stay."
                        elif Girl == JubesX:
                            ch_v "Sorry, not interested."
                        return
                    elif not Girl.remaining_actions:

                        if Girl == RogueX:
                            ch_r "I'm sorry [Girl.player_petname], I'm just too tuckered out right now. . ."
                        elif Girl == KittyX:
                            ch_k "Sorry [Girl.player_petname], I'm kinda worn out already. . ."
                        elif Girl == EmmaX:
                            ch_e "So sorry [Girl.player_petname], I needed a break. . ."
                        elif Girl == LauraX:
                            ch_l "Sorry [Girl.player_petname], looks like we're taking a break. . ."
                        elif Girl == JeanX:
                            ch_j "I could use a break though. . ."
                        elif Girl == StormX:
                            ch_s "I did need to take a brief rest, however."
                        elif Girl == JubesX:
                            ch_v "I'm kinda worn out though."
                        return
                    else:

                        if Girl == RogueX:
                            ch_r "Ok, fine."
                        elif Girl == KittyX:
                            ch_k "Sure."
                        elif Girl == EmmaX:
                            ch_e "Very well."
                        elif Girl == LauraX:
                            ch_l "Sure."
                        elif Girl == JeanX:
                            ch_j "Nice."
                        elif Girl == StormX:
                            ch_s "Oh, excellent."
                        elif Girl == JubesX:
                            ch_v "Nice."

                $ focused_Girl = Girl
                jump Les_Prep

            "So maybe I could join you girls?" if Player.semen and Girl.remaining_actions:
                $ Girl.change_face("_sexy")
                if Girl == RogueX:
                    ch_r "Well what did you have in mind?"
                elif Girl == KittyX:
                    ch_k "Mmmm, what would you like?"
                elif Girl == EmmaX:
                    ch_e "Oh? What do you bring to the table?"
                elif Girl == LauraX:
                    ch_l "Oh, you have something to add here?"
                elif Girl == JeanX:
                    ch_j "Oh? Do tell. . ."
                elif Girl == StormX:
                    ch_s "I think that you might. . ."
                elif Girl == JubesX:
                    ch_v "Well, I think we could work with that. . ."
                $ action_context = "join"
                return
            "So maybe I could watch a bit longer?":
                $ Girl.change_face("_bemused", 1)



    if not Girl.event_counter["seen_with_girl"]:
        $ Girl.change_face("_surprised", 1,Mouth="kiss")
        if Girl == RogueX:
            ch_r "You want me and [Partner.name] to hook up, while you watch?"
        elif Girl == KittyX:
            ch_k "You wanna watch me and [Partner.name] hook up?"
        elif Girl == EmmaX:
            ch_e "You wanna watch me and [Partner.name] \"engaged?\""
        elif Girl == LauraX:
            ch_l "You want to watch me and [Partner.name] hook up?"
        elif Girl == JeanX:
            ch_j "Oh, you'd like to watch me and [Partner.name]?. . ."
        elif Girl == StormX:
            ch_s "Oh, so you would like to see the two of us together?"
        elif Girl == JubesX:
            ch_v "Oh, me and her? Together?"
        if Girl.Forced:
            $ Girl.change_face("_sad")
            if Girl == RogueX:
                ch_r "And {i}just{/i} watch?"
            elif Girl == KittyX:
                ch_k "but {i}just{/i} watch, right?"
            elif Girl == EmmaX:
                ch_e "nothing more than that though?"
            elif Girl == LauraX:
                ch_l "{i}Just{/i} watching, right?"
            elif Girl == JeanX:
                ch_j "-Just- watching. . ."
            elif Girl == StormX:
                ch_s "Nothing more than to watch?"
            elif Girl == JubesX:
                ch_v "But just watching though?"


    if approval and (Partner == RogueX or Girl == RogueX) and "touch" not in RogueX.traits:
        if Girl == RogueX:
            ch_r "I don't know, isn't my touch. . . dangerous?"
            ch_p "Don't worry, I can keep it turned off."
            ch_r "I suppose you can. . ."
        elif Girl == KittyX:
            ch_k "I don't know, isn't it kinda. . . dangerous to touch [RogueX.name]?"
            ch_p "Don't worry, I can keep it turned off."
            ch_k "Oh, well I guess. . ."
        elif Girl == EmmaX:
            ch_e "I'm not sure, [RogueX.name]'s touch can be. . . disruptive?"
            ch_p "Don't worry, I can keep it turned off."
            ch_e "Oh, I suppose you can at that. . ."
        elif Girl == LauraX:
            ch_l "I don't know, [RogueX.name]'s touch can be. . . intense. . ."
            ch_p "Don't worry, I can keep it turned off."
            ch_l "Oh, well I guess. . ."
        elif Girl == JeanX:
            ch_j "I guess I can use my TK to avoid direct contact. . ."
        elif Girl == StormX:
            ch_s "I'm unsure, [RogueX.name]'s touch can be a bit of an issue."
            ch_p "Don't worry, I can keep it turned off."
            ch_s "That is true. . ."
        elif Girl == JubesX:
            ch_v "I wouldn't want any trouble with [RogueX.name]'s. . . condition."
            ch_p "Don't worry, I can keep it turned off."
            ch_v "Oh, that'll work."


    if not Girl.event_counter["seen_with_girl"] and approval:

        if Girl.Forced:
            $ Girl.change_face("_sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
        elif Bonus >= 100:
            $ Girl.change_face("_sly", Eyes="_side")
            if Girl == RogueX:
                ch_r "Hmm, actually I might enjoy this more than you think. . ."
            elif Girl == KittyX:
                ch_k "Heh, you don't know what you're asking for. . ."
            elif Girl == EmmaX:
                ch_e "This won't be my first time. . ."
            elif Girl == LauraX:
                ch_l "Well you'd be in for a treat. . ."
            elif Girl == JeanX:
                ch_j "I won't turn down a round with her. . ."
            elif Girl == StormX:
                ch_s "I am certainly more than open to the idea."
            elif Girl == JubesX:
                ch_v "Oh, yeah, no prob."
        elif Girl.love >= (Girl.obedience + Girl.inhibition):
            $ Girl.change_face("_sexy")
            $ Girl.brows = "_sad"
            $ Girl.mouth = "_smile"
            if Girl == RogueX:
                ch_r "I haven't really given much thought to being with other people lately. . ."
            elif Girl == KittyX:
                ch_k "I hadn't really considered putting on a show like this. . ."
            elif Girl == EmmaX:
                ch_e "I hadn't considered this as one of your kinks. . ."
            elif Girl == LauraX:
                ch_l "I hadn't really considered putting on a show like this. . ."
            elif Girl == JeanX:
                ch_j "I don't make a habit of this. . ."
            elif Girl == StormX:
                ch_s "I might if that sort of thing interests you. . ."
            elif Girl == JubesX:
                ch_v "I guess I could be into it."
        elif Girl.obedience >= Girl.inhibition:
            $ Girl.change_face("_normal")
            if Girl == RogueX:
                ch_r "If that's what you want, [Girl.player_petname]. . ."
            elif Girl == KittyX:
                ch_k "If that's what you want, [Girl.player_petname]. . ."
            elif Girl == EmmaX:
                ch_e "If this is what gets you off, [Girl.player_petname]. . ."
            elif Girl == LauraX:
                ch_l "I'm ok with that, [Girl.player_petname]. . ."
            elif Girl == JeanX:
                ch_j "Ok, sure. . ."
            elif Girl == StormX:
                ch_s "I could be convinced. . ."
            elif Girl == JubesX:
                ch_v "If you like that. . ."
        else:
            $ Girl.change_face("_sad")
            $ Girl.mouth = "_smile"
            if Girl == RogueX:
                ch_r "I guess it could be fun with you watching. . ."
            elif Girl == KittyX:
                ch_k "I guess it could be fun with you watching. . ."
            elif Girl == EmmaX:
                ch_e "I do enjoy an audience. . ."
            elif Girl == LauraX:
                ch_l "Not that I mind. . ."
            elif Girl == JeanX:
                ch_j "I wouldn't mind an audience. . ."
            elif Girl == StormX:
                ch_s "I am open to the idea."
            elif Girl == JubesX:
                ch_v "Sure, I guess. . ."


    elif approval:

        if Girl.Forced:
            $ Girl.change_face("_sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
            if Girl == RogueX:
                ch_r "So you want to watch me with a girl again?"
            elif Girl == KittyX:
                ch_k "You really like this girl-on-girl stuff, huh?"
            elif Girl == EmmaX:
                ch_e "You enjoyed the last show?"
            elif Girl == LauraX:
                ch_l "This is what gets you off?"
            elif Girl == JeanX:
                ch_j "Enjoy the show, uh? . ."
            elif Girl == StormX:
                ch_s "So you enjoy these little plays?"
            elif Girl == JubesX:
                ch_v "This is the kind of thing you like?"
        elif approval and "lesbian" in Girl.recent_history:
            $ Girl.change_face("_sexy", 1)
            if Girl == RogueX:
                ch_r "I guess we could get a little closer. . ."
            elif Girl == KittyX:
                ch_k "A little more wouldn't hurt. . ."
            elif Girl == EmmaX:
                ch_e "Hmm, back for more?"
            elif Girl == LauraX:
                ch_l "I wouldn't mind a little more. . ."
            elif Girl == JeanX:
                ch_j "Ok then, back to it. . ."
            elif Girl == StormX:
                ch_s "Very well. . ."
            elif Girl == JubesX:
                ch_v "I guess we can do that for you. . ."
            $ focused_Girl = Girl
            jump Les_Prep
        elif approval and "lesbian" in Girl.daily_history:
            $ Girl.change_face("_sexy", 1)
            $ Line = renpy.random.choice(["Enjoyed the show?",
                                    "Didn't get enough earlier?",
                                    "I don't mind having an audience. . ."])
            Girl.voice "[Line]"
        elif Girl.event_counter["been_with_girl"] < 3:
            $ Girl.change_face("_sexy", 1)
            $ Girl.brows = "_confused"
            if Girl == RogueX:
                ch_r "You like to watch, huh?"
            elif Girl == KittyX:
                ch_k "You really do like to watch."
            elif Girl == EmmaX:
                ch_e "You do like to watch."
            elif Girl == LauraX:
                ch_l "You do like to watch."
            elif Girl == JeanX:
                ch_j "Can't get enough of me. . ."
            elif Girl == StormX:
                ch_s "So you enjoy these little plays?"
            elif Girl == JubesX:
                ch_v "I don't know. . ."
        else:
            $ Girl.change_face("_sexy", 1)
            $ Girl.ArmPose = 2
            $ Line = renpy.random.choice(["You do like to watch.",
                                    "So you'd like us to go again?",
                                    "You want to watch some more?",
                                    "You want me to get it on with "+Partner.tag+"?"])
            Girl.voice "[Line]"
        $ Line = 0


    if approval >= 2:

        if Girl.Forced:
            $ Girl.change_face("_sad")
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 60, 1)
            if Girl == RogueX:
                ch_r "Fine, I'm ok with it if she is. . ."
            elif Girl == KittyX:
                ch_k "Well, I guess if she's fine with it. . ."
            elif Girl == EmmaX:
                ch_e "So long as she finds it acceptable. . ."
            elif Girl == LauraX:
                ch_l "Not the worst way to spend some time. . ."
            elif Girl == JeanX:
                ch_j "Well, could be worse. . ."
            elif Girl == StormX:
                ch_s "I suppose a show would not hurt."
            elif Girl == JubesX:
                ch_v "Could be worse. . ."
        else:
            $ Girl.change_face("_sexy", 1)
            $ Girl.change_stat("love", 90, 1)
            $ Girl.change_stat("inhibition", 50, 3)
            if action_context == "interrupted":
                if Girl == RogueX:
                    ch_r "Well I could do some more. . ."
                elif Girl == KittyX:
                    ch_k "Well I guess we could get back to it. . ."
                elif Girl == EmmaX:
                    ch_e "Well I suppose we could continue. . ."
                elif Girl == LauraX:
                    ch_l "Well I could get back in there. . ."
                elif Girl == JeanX:
                    ch_j "I did want to try a few things. . ."
                elif Girl == StormX:
                    ch_s "Come here then, [Partner.name]."
                elif Girl == JubesX:
                    ch_v "Back to it then?"
            else:
                $ Line = renpy.random.choice(["Well. . . ok.",
                                        "I don't mind getting with her. . .",
                                        "A",
                                        "Sure.",
                                        "I guess. . .",
                                        "Heh, ok, fine."])
                if Line == "A":
                    if Girl == RogueX:
                        ch_r "I may have needed this anyway. . ."
                    elif Girl == KittyX:
                        ch_k "I kinda needed this anyways. . ."
                    elif Girl == EmmaX:
                        ch_e "I don't mind getting intimate with her. . ."
                    elif Girl == LauraX:
                        ch_l "I kinda needed to blow off some steam. . ."
                    elif Girl == JeanX:
                        ch_j "You haven't seen this one trick she has. . ."
                    elif Girl == StormX:
                        ch_s "You will enjoy this one."
                    elif Girl == JubesX:
                        ch_v "I still needed some attention anyway."
                else:
                    Girl.voice "[Line]"
                $ Line = 0
        $ Girl.change_stat("obedience", 20, 1)
        $ Girl.change_stat("obedience", 60, 1)
        $ Girl.change_stat("inhibition", 70, 2)
        jump Les_Partner
    else:


        if Girl == RogueX:
            ch_r "I'm not sure about that though, [Girl.player_petname]."
        elif Girl == KittyX:
            ch_k "I don't know about that, [Girl.player_petname]."
        elif Girl == EmmaX:
            ch_e "I'm not sure about that, [Girl.player_petname]."
        elif Girl == LauraX:
            ch_l "I don't know, [Girl.player_petname]."
        elif Girl == JeanX:
            ch_j "Hmm. . . I don't know. . ."
        elif Girl == StormX:
            ch_s "I am unsure. . ."
        elif Girl == JubesX:
            ch_v "Well, but. . ."
        menu:
            "Maybe later?":
                $ Girl.change_face("_sexy", 1)
                if Bonus >= 100:
                    $ Girl.change_stat("inhibition", 90, 5)
                    if Girl == RogueX:
                        ch_r "Well. . . definitely at some point. . ."
                    elif Girl == KittyX:
                        ch_k "I mean, eventually. . ."
                    elif Girl == EmmaX:
                        ch_e "Eventually. . ."
                    elif Girl == LauraX:
                        ch_l "Maybe some other time. . ."
                    elif Girl == JeanX:
                        ch_j "Sure, maybe. . ."
                    elif Girl == StormX:
                        ch_s "Yes, some other time, perhaps."
                    elif Girl == JubesX:
                        ch_v "Sure, maybe."
                elif Bonus >= 0:
                    $ Girl.GLG(Partner,800,3,1)
                    if Girl == RogueX:
                        ch_r "Um, I don't know. . . maybe?"
                    elif Girl == KittyX:
                        ch_k "Um, I don't know. . . maybe?"
                    elif Girl == EmmaX:
                        ch_e "One never knows. . ."
                    elif Girl == LauraX:
                        ch_l "Eh, I don't know. . ."
                    elif Girl == JeanX:
                        ch_j "Hmm. . . maybe. . ."
                    elif Girl == StormX:
                        ch_s "That may be better."
                    elif Girl == JubesX:
                        ch_v "Sure maybe."
                else:
                    $ Girl.change_face("_angry", 1, Eyes="_side")
                    if Girl == RogueX:
                        ch_r "Yeah, I really don't see that happening. . ."
                    elif Girl == KittyX:
                        ch_k "Not likely."
                    elif Girl == EmmaX:
                        ch_e "Unlikely."
                    elif Girl == LauraX:
                        ch_l "Probably not."
                    elif Girl == JeanX:
                        ch_j "Not likely. . ."
                    elif Girl == StormX:
                        ch_s "Doubtful."
                    elif Girl == JubesX:
                        ch_v "Doubtful."
                if Girl == RogueX:
                    ch_r "But thanks for being ok with that."
                elif Girl == KittyX:
                    ch_k "Thanks for being cool though. . ."
                elif Girl == EmmaX:
                    ch_e "I do appreciate your restraint."
                elif Girl == StormX:
                    ch_s "I am sorry about that."
                elif Girl == JubesX:
                    ch_v "Sorry."
                $ Girl.change_face("_smile", 1)
                $ Girl.change_stat("love", 80, 2)
                $ Girl.change_stat("inhibition", 70, 5)
                call Taboo_Level
                return
            "You look like you might be into it. . .":


                if approval:
                    $ Girl.change_face("_sexy")
                    $ Girl.change_stat("obedience", 90, 4)
                    $ Girl.change_stat("obedience", 50, 5)
                    $ Girl.change_stat("inhibition", 70, 4)
                    $ Girl.change_stat("inhibition", 40, 4)
                    $ Line = renpy.random.choice(["Well. . . ok.",
                                        "I don't mind getting with her. . .",
                                        "A",
                                        "Sure.",
                                        "I guess. . .",
                                        "Heh, ok, fine."])
                    if Line == "A":
                        if Girl == RogueX:
                            ch_r "I may have needed this anyway. . ."
                        elif Girl == KittyX:
                            ch_k "I kinda needed this anyways. . ."
                        elif Girl == EmmaX:
                            ch_e "I don't mind getting intimate with her. . ."
                        elif Girl == LauraX:
                            ch_l "I kinda needed to blow off some steam. . ."
                        elif Girl == JeanX:
                            ch_j "You haven't seen this one trick she has. . ."
                        elif Girl == StormX:
                            ch_s "You will enjoy this one."
                        elif Girl == JubesX:
                            ch_v "I mean, maybe."
                    else:
                        Girl.voice "[Line]"
                    Girl.voice "[Line]"
                    $ Line = 0
                    jump Les_Partner
            "Just get at it already.":


                $ approval = approval_check(Girl, 550, "OI", TabM = 2)
                if approval > 1 or (approval and Girl.Forced):
                    $ Girl.change_face("_sad")
                    $ Girl.change_stat("love", 70, -5, 1)
                    $ Girl.change_stat("love", 200, -5)
                    if Girl == RogueX:
                        ch_r "Ok, fine. I'll give it a try."
                    elif Girl == KittyX:
                        ch_k "Ok, whatever."
                    elif Girl == EmmaX:
                        ch_e "Oh, fine."
                    elif Girl == LauraX:
                        ch_l "Ok, if you insist."
                    elif Girl == JeanX:
                        ch_j "Oh, fine. . ."
                    elif Girl == StormX:
                        ch_s ". . ."
                    elif Girl == JubesX:
                        ch_v "Fine."
                    $ Girl.change_stat("obedience", 80, 4)
                    $ Girl.change_stat("inhibition", 80, 1)
                    $ Girl.change_stat("inhibition", 60, 3)
                    $ Girl.Forced = 1
                    jump Les_Partner
                else:
                    $ Girl.change_stat("love", 200, -20)
                    $ Girl.recent_history.append("_angry")
                    $ Girl.daily_history.append("_angry")


    call Les_Response (Partner, Girl, 1, B2=Bonus)
    if _return:

        $ Girl.change_face("_smile", 1)
        if Girl == RogueX:
            ch_r "Ok, fine! You've talked me into it."
            ch_r "Get over here. . ."
        elif Girl == KittyX:
            ch_k "Ok, if {i}you{/i} want to."
            ch_k "Commere. . ."
        elif Girl == EmmaX:
            ch_e "Well, if you insist, dear."
            $ Girl.change_face("_sly", 1)
            ch_e "Get over here. . ."
        elif Girl == LauraX:
            ch_l "Ok, if {i}you're{/i} into it."
            ch_l "Get over here. . ."
        elif Girl == JeanX:
            ch_j "Well, you're certainly enthusiastic. . ."
            ch_j "Ok, fine."
        elif Girl == StormX:
            ch_s "Well how could I refuse you, [Partner.name]?"
            ch_s "Very well, get over here. . ."
        elif Girl == JubesX:
            ch_v "Ok, fine, if you're into it."
            ch_v "Come on over here."
        $ focused_Girl = Girl
        jump Les_Prep



    $ Girl.ArmPose = 1
    if not Partner:
        if Girl == RogueX:
            ch_r "It would take two to tango, so. . ."
        elif Girl == KittyX:
            ch_k "Seems like she wasn't into it. . ."
        elif Girl == EmmaX:
            ch_e "Well, I can't exactly do this alone. . ."
        elif Girl == LauraX:
            ch_l "I don't know if I should feel insulted. . ."
        elif Girl == JeanX:
            ch_j "We will have -words- later. . ."
        elif Girl == StormX:
            ch_s "I'm afraid that settles that."
        elif Girl == JubesX:
            ch_v "Well, doesn't look like it's happening. . ."
    elif Girl.Forced:
        $ Girl.change_face("_angry", 1)
        if Girl == RogueX:
            ch_r "Look, that's just not on the table."
        elif Girl == KittyX:
            ch_k "I'm just not into that."
        elif Girl == EmmaX:
            ch_e "I'm just not into that."
        elif Girl == LauraX:
            ch_l "I'm not into that."
        elif Girl == JeanX:
            ch_j "Seems kinda sketch. . ."
        elif Girl == StormX:
            ch_s "I would prefer something else."
        elif Girl == JubesX:
            ch_v "Just not into it."
        $ Girl.change_stat("lust", 90, 5)
        if Girl.love > 300:
            $ Girl.change_stat("love", 70, -2)
        $ Girl.change_stat("obedience", 50, -2)
        $ Girl.recent_history.append("_angry")
        $ Girl.daily_history.append("_angry")
    elif Girl.Taboo > 20:

        $ Girl.change_face("_angry", 1)
        $ Girl.daily_history.append("no_taboo")
        if Girl == RogueX:
            ch_r "Definitely not around here."
        elif Girl == KittyX:
            ch_k "Totally not around here."
        elif Girl == EmmaX:
            ch_e "Totally not around here."
        elif Girl == LauraX:
            ch_l "Not someplace so public."
        elif Girl == JeanX:
            ch_j "I don't think this is the place for it?"
        elif Girl == StormX:
            ch_s "This area may be too public."
        elif Girl == JubesX:
            ch_v "It's too public here."
        $ Girl.change_stat("lust", 90, 5)
        $ Girl.change_stat("obedience", 50, -3)
    elif Girl.event_counter["been_with_girl"]:
        $ Girl.change_face("_sad")
        if Girl == RogueX:
            if Bonus >= 100:
                ch_r "I just don't think I'm ready for that sort of thing."
            else:
                ch_r "I just don't think I'm into that sort of thing."
        elif Girl == KittyX:
            if Bonus >= 100:
                ch_k "I'm not really comfortable with that."
            else:
                ch_k "I don't think I'm ready for an audience."
        elif Girl == EmmaX:
            if Bonus >= 100:
                ch_e "I'm not really comfortable with that."
            else:
                ch_e "I don't think I'm ready for an audience."
        elif Girl == LauraX:
            if Bonus >= 100:
                ch_l "I'm not up for that."
            else:
                ch_l "Not with an audience."
        elif Girl == JeanX:
            if Bonus >= 100:
                ch_j "I'm not cool with that."
            else:
                ch_j "I'd rather you didn't watch."
        elif Girl == StormX:
            if Bonus >= 100:
                ch_s "That's not really something I would want to do."
            else:
                ch_s "I don't think an audience would be appropriate."
        elif Girl == JubesX:
            if Bonus >= 100:
                ch_v "Just not into it."
            else:
                ch_v "I'd rather you weren't involved."
    else:
        $ Girl.change_face("_normal", 1)
        if Girl == RogueX:
            ch_r "Heh, noway, I am {i}not{/i} doing that."
        elif Girl == KittyX:
            ch_k "No way."
        elif Girl == EmmaX:
            ch_e "No way."
        elif Girl == LauraX:
            ch_l "Nope."
        elif Girl == JeanX:
            ch_j "No way. . ."
        elif Girl == StormX:
            ch_s "I'm afraid not."
        elif Girl == JubesX:
            ch_v "Nope."
    $ Girl.recent_history.append("no_lesbian")
    $ Girl.daily_history.append("no_lesbian")
    $ approval_bonus = 0
    call Taboo_Level
    return

label Les_Partner:



    $ BO = all_Girls[:]
    $ BO.remove(Girl)
    while BO:
        if BO[0].location == bg_current:
            call Les_Response (BO[0], Girl, 2)
            if not _return:

                return
        $ BO.remove(BO[0])


label Les_Prep(Girl=focused_Girl, BO=[]):

    $ Line = 0
    if Girl not in all_Girls or Girl == Partner:
        $ Girl = focused_Girl
        if Girl == Partner:
            $ Partner = 0
            $ Line = 1

    if Partner not in all_Girls:
        $ Partner = 0
        $ BO = all_Girls[:]
        $ BO.remove(Girl)
        while BO:
            if BO[0].location == bg_current:
                $ Partner = BO[0]
                $ BO = [1]
            $ BO.remove(BO[0])

    if Line:

        call shift_focus (Partner)

    $ Line = 0

    $ Girl.add_word(1,"noticed "+Partner.tag,"noticed "+Partner.tag)
    $ Partner.add_word(1,"noticed "+Girl.tag,"noticed "+Girl.tag)

    if "unseen" not in Girl.recent_history:

        $ Girl.change_face("_sexy")
        $ Girl.ArmPose = 2
        "[Girl.name] move's closer to [Partner.name] and wraps her arms around her neck."
        if not Girl.event_counter["seen_with_girl"]:

            if Girl.Forced:
                $ Girl.change_stat("love", 90, -20)
                $ Girl.change_stat("obedience", 70, 55)
                $ Girl.change_stat("inhibition", 80, 55)
            else:
                $ Girl.change_stat("love", 90, 5)
                $ Girl.change_stat("obedience", 70, 20)
                $ Girl.change_stat("inhibition", 80, 60)
        call Les_FirstKiss
        $ girl_offhand_action == "kiss girl"
        $ second_girl_primary_action == "kiss girl"

    $ primary_action = "lesbian"
    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    if Girl.Taboo:
        $ Girl.drain_word("no_taboo")
    $ Girl.drain_word("no_lesbian")
    $ Girl.add_word(0,"lesbian","lesbian")
    $ Partner.add_word(0,"lesbian","lesbian")

label Les_Cycle(Girl=focused_Girl):
    $ Girl = GirlCheck(Girl)
    while Round > 0:
        call shift_focus (Girl)
        call Les_Launch (Girl)
        $ Girl.lust_face()

        if Player.focus < 100:

            menu:
                "Keep watching. . .":
                    pass

                "\"Ahem. . .\"" if "unseen" in Girl.recent_history:
                    jump Les_Interupted

                "Start jack'in it." if offhand_action != "jackin":
                    call Jackin (Girl)
                "Stop jack'in it." if offhand_action == "jackin":
                    $ offhand_action = 0

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "Other options":

                    menu:
                        "Offhand action":
                            if Girl.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ Girl.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (Girl, "tired")
                        "Threesome actions":

                            menu:
                                "Ask [Girl.name] to do something else with [Partner.name]":
                                    if "unseen" in Girl.recent_history:
                                        ch_p "Oh yeah, why don't you. . ."
                                        jump Les_Interupted
                                    else:
                                        call Les_Change (Girl)
                                "Ask [Partner.name] to do something else":
                                    if "unseen" in Girl.recent_history:
                                        ch_p "Oh yeah, why don't you. . ."
                                        jump Les_Interupted
                                    else:
                                        call Three_Change (Girl)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    if "unseen" in Girl.recent_history:
                                        ch_p "Oh, that's good. . ."
                                        jump Les_Interupted
                                    else:
                                        $ position_timer = 0
                                "Undress [Partner.name]":



                                    if "unseen" in Girl.recent_history:
                                        ch_p "Oh, yeah, take it off. . ."
                                        jump Les_Interupted
                                    else:
                                        call Girl_Undress (Partner)
                                        call shift_focus (Partner)
                                        jump Les_Cycle
                                "Clean up Partner":
                                    if "unseen" in Girl.recent_history:
                                        ch_p "You've got a little something. . ."
                                        jump Les_Interupted
                                    else:
                                        call Girl_Cleanup (Partner, "ask")

                                        jump Les_Cycle
                                "Never mind":
                                    jump Les_Cycle
                        "undress [Girl.name]":
                            if "unseen" in Girl.recent_history:
                                ch_p "Oh yeah, why don't you. . ."
                                jump Les_Interupted
                            else:
                                call Girl_Undress (Girl)
                        "Clean up [Girl.name] (locked)" if not Girl.spunk:
                            pass
                        "Clean up [Girl.name]" if Girl.spunk:
                            if "unseen" in Girl.recent_history:
                                ch_p "You've got a little something. . ."
                                jump Les_Interupted
                            else:
                                call Girl_Cleanup (Girl, "ask")
                        "Never mind":
                            jump Les_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    $ action_context = "shift"
                    $ Line = 0
                    jump Les_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    $ Line = 0
                    jump Les_After


        call shift_focus (Girl)
        call Sex_Dialog (Girl, Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus

        if Player.focus >= 100 or Girl.lust >= 100:

            if Player.focus >= 100:

                if "unseen" not in Girl.recent_history:
                    call Player_Cumming (Girl)
                    if "_angry" in Girl.recent_history:
                        call expression Girl.tag + "_Pos_Reset"
                        call expression Partner.tag + "_Pos_Reset"
                        return
                    $ Girl.change_stat("lust", 200, 5)
                    if 100 > Girl.lust >= 70 and Girl.session_orgasms < 2:
                        $ Girl.recent_history.append("unsatisfied")
                        $ Girl.daily_history.append("unsatisfied")
                    $ Line = "came"
                else:
                    "You grunt and try to hold it in."
                    $ Player.focus = 95
                    jump Les_Interupted

            if Girl.lust >= 100:

                call Girl_Cumming (Girl)
                jump Les_Interupted

            if Line == "came":
                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)



        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if "unseen" in Girl.recent_history:
            if Round == 10:
                "It's getting a bit late, [Girl.name] and [Partner.name] will probably be wrapping up soon."
            elif Round == 5:
                "They're definitely going to stop soon."
        else:
            if Round == 10:
                call Sex_Basic_Dialog (Girl, 10)
            elif Round == 5:
                call Sex_Basic_Dialog (Girl, 5)

    $ Girl.change_face("_bemused", 0)
    $ Line = 0
    if "unseen" not in Girl.recent_history:
        call Sex_Basic_Dialog (Girl, "done")


label Les_After:
    call expression Girl.tag + "_Pos_Reset"
    if not Partner:
        $ approval_bonus = 0
        call checkout
        return
    call expression Partner.tag + "_Pos_Reset"
    $ Girl.change_face("_sexy")
    if Partner == EmmaX:
        call Partner_Like (Girl, 4)
    else:
        call Partner_Like (Girl, 3)

    $ Girl.event_counter["seen_with_girl"] += 1
    $ Partner.event_counter["seen_with_girl"] += 1
    if Girl.event_counter["seen_with_girl"] == 1:
        $ Girl.SEXP += 15
        if Girl.love >= 500 and Girl.Org:
            if Girl == RogueX:
                ch_r "I have to say, I really enjoyed that one. . ."
            elif Girl == KittyX:
                ch_k "Hmm, that's kinda fun with an audience. . ."
            elif Girl == EmmaX:
                ch_e "I do enjoy an audience. . ."
                $ Girl.change_face("_sly",1)
                ch_e "something to keep in mind?"
            elif Girl == LauraX:
                ch_l "I enjoyed the audience. . ."
            elif Girl == JeanX:
                ch_j "Nice having an audience there. . ."
            elif Girl == StormX:
                ch_s "I did enjoy being watched. . ."
            elif Girl == JubesX:
                ch_v "It was cool to have an audience. . ."
    if Partner.event_counter["seen_with_girl"] == 1:
        $ Partner.SEXP += 15
        if Partner.love >= 500 and Partner.Org:
            if Partner == RogueX:
                ch_r "I have to say, I really enjoyed that one. . ."
            elif Partner == KittyX:
                ch_k "Hmm, that's kinda fun with an audience. . ."
            elif Partner == EmmaX:
                ch_e "I do enjoy an audience. . ."
                $ Partner.change_face("_sly",1)
                ch_e "something to keep in mind?"
            elif Partner == LauraX:
                ch_l "I enjoyed the audience. . ."
            elif Partner == JeanX:
                ch_j "Nice having an audience there. . ."
            elif Girl == StormX:
                ch_s "I did enjoy being watched. . ."
            elif Girl == JubesX:
                ch_v "It was cool to have an audience. . ."
    if not action_context:
        call Post_Les_Dialog
    $ Girl.add_word(1,0,0,0,"les "+Partner.tag)
    $ Partner.add_word(1,0,0,0,"les "+Girl.tag)
    $ approval_bonus = 0
    call checkout
    return



label Post_Les_Dialog:

    if Girl == RogueX:
        ch_r "That was nice. . ."
    elif Girl == KittyX:
        ch_k "That was fun. . ."
    elif Girl == EmmaX:
        ch_e "That was enjoyable. . ."
    elif Girl == LauraX:
        ch_l "That was fun. . ."
    elif Girl == JeanX:
        ch_j "Hey, that was fun. . ."
    elif Girl == StormX:
        ch_s "That was. . . quite enjoyable."
    elif Girl == JubesX:
        ch_v "That was a blast. . ."

    if "les "+Partner.tag in Girl.history:

        if Partner == RogueX:
            ch_r "Mmmm yeah. . ."
        elif Partner == KittyX:
            ch_k "Mmmm yeah that was good. . ."
        elif Partner == EmmaX:
            ch_e "Certainly. . ."
        elif Partner == LauraX:
            ch_l "Yup. . ."
        elif Partner == JeanX:
            ch_j "Yeah, I guess it was. . ."
        elif Partner == StormX:
            ch_s "It certainly was. . ."
        elif Girl == JubesX:
            ch_v "Totally. . ."
    else:


        if Girl.GirlLikeCheck(Partner) >= 600:

            if Girl == RogueX:
                ch_r "You. . . really know what you're doing down there. . ."
            elif Girl == KittyX:
                ch_k "You're really good at that!"
            elif Girl == EmmaX:
                ch_e "You were delightful dear!"
            elif Girl == LauraX:
                ch_l "I liked that thing with the mouth work."
            elif Girl == JeanX:
                ch_j "You seemed. . . experienced. . ."
            elif Girl == StormX:
                ch_s "You certainly have a talent for this. . ."
            elif Girl == JubesX:
                ch_v "You're really great at this. . ."
        else:

            if Girl == RogueX:
                ch_r "That. . . wasn't awful. . ."
            elif Girl == KittyX:
                ch_k "That was. . . interesting. . ."
            elif Girl == EmmaX:
                ch_e "At least you could keep up. . ."
            elif Girl == LauraX:
                ch_l "That was ok. . ."
            elif Girl == JeanX:
                ch_j "Yeah, ok. . ."
            elif Girl == StormX:
                ch_s "That was. . . fine."
            elif Girl == JubesX:
                ch_v "You. . . tried. . ."


        if Partner.GirlLikeCheck(Girl) >= 600:

            if Partner == RogueX:
                ch_r "Um, yeah, you too. . ."
            elif Partner == KittyX:
                ch_k "Yeah, that was really hot. . ."
            elif Partner == EmmaX:
                ch_e "Practice, dear. . ."
            elif Partner == LauraX:
                ch_l "I can read a map."
            elif Partner == JeanX:
                ch_j "Well, I -can- read minds. . ."
            elif Partner == StormX:
                ch_s "Yes, you as well."
            elif Partner == JubesX:
                ch_v "Yeah, you were great. . ."
        else:

            if Partner == RogueX:
                ch_r "I guess. . ."
            elif Partner == KittyX:
                ch_k "I guess. . ."
            elif Partner == EmmaX:
                ch_e "You could certainly do with more practice. . ."
            elif Partner == LauraX:
                ch_l "Uh-huh."
            elif Partner == JeanX:
                ch_j "Sure, whatever. . ."
            elif Partner == StormX:
                ch_s "Yes. . ."
            elif Partner == JubesX:
                ch_v "I guess you tried. . ."
    return



label Les_Response(Speaker=0, Subject=0, Step=1, B=0, B2=0, approval_bonus=0, Result=0, approval=0):




    if Speaker not in all_Girls:
        $ Speaker = Partner
    if Subject not in all_Girls:
        $ Subject = focused_Girl
    if Speaker == EmmaX:

        if "three" not in EmmaX.history or "classcaught" not in EmmaX.history or (Taboo > 20 and "taboo" not in EmmaX.history):
            $ EmmaX.recent_history.append("no_lesbian")
            $ EmmaX.daily_history.append("no_lesbian")
            $ EmmaX.change_stat("obedience", 70, 5)
            $ EmmaX.change_stat("inhibition", 80, 5)
            $ EmmaX.change_stat("lust", 50, 10)
            $ Speaker.change_face("_sadside", 1)
            "[EmmaX.name] looks around furtively."
            if Subject == StormX:
                ch_e "Just to be clear, Ororo, I do -not- engage in sexual activities with students like [Player.name] here."
                ch_e "I suppose I should excuse myself."
                $ Subject.change_face("_bemused", 1)
                ch_s "Oh, yes, Ms. Frost. We would not wish to give the wrong impression."
            else:
                ch_e "I can't imagine why you would think I would engage in such behavior with a student!"
            call Remove_Girl (EmmaX)
            "She quickly leaves the room."
            return 0

    if not Speaker.remaining_actions:

        if Speaker == RogueX:
            ch_r "I'm sorry, I'm just worn out"
        elif Speaker == KittyX:
            ch_k "I'm too tired for this. . ."
        elif Speaker == EmmaX:
            ch_e "I'm exhausted, not now. . ."
        elif Speaker == LauraX:
            ch_l "I've got other things to be doing. . ."
        elif Speaker == JeanX:
            ch_j "I'm tired of this. . ."
        elif Speaker == StormX:
            ch_s "I cannot right now, I am sorry."
        elif Speaker == JubesX:
            ch_v "Sorry, I'm just worn out. . ."
        return 0

    if Speaker.event_counter["been_with_girl"]:
        $ approval_bonus += 10
    if Speaker.SEXP >= 50:
        $ approval_bonus += 25
    elif Speaker.SEXP >= 30:
        $ approval_bonus += 15
    elif Speaker.SEXP >= 15:
        $ approval_bonus += 5

    elif Speaker.inhibition >= 750:
        $ approval_bonus += 5

    if "exhibitionist" in Speaker.traits:
        $ approval_bonus += (3*Taboo)

    if Speaker in Player.Harem or "sex friend" in Speaker.player_petnames:
        $ approval_bonus += 10
    elif "ex" in Speaker.traits:
        $ approval_bonus -= 40


    if Speaker.GirlLikeCheck(Subject) >= 900:
        $ B += 150
    elif Speaker.GirlLikeCheck(Subject) >= 800 or "poly " + Subject.tag in Speaker.traits:
        $ B += 100
    elif Speaker.GirlLikeCheck(Subject) >= 700:
        $ B += 50
    elif Speaker.GirlLikeCheck(Subject) <= 200:
        $ B -= 200
    elif Speaker.GirlLikeCheck(Subject) <= 500:
        $ B -= 100

    if Speaker == JeanX:
        $ B += 100

    $ approval = approval_check(Speaker, 1300, TabM = 2, Bonus = B)

    if not approval:

        pass
    elif Step == 1:

        if approval >= 2 or B >= 150:
            $ Speaker.change_face("_sexy", 1)
            if Speaker == RogueX:
                ch_r "You sure [Subject.tag]? Could be a lot of fun?"
            elif Speaker == KittyX:
                ch_k "Come on [Subject.tag], it could be kinda fun."
            elif Speaker == EmmaX:
                ch_e "Oh come on [Subject.tag], I could show you a few things."
            elif Speaker == LauraX:
                ch_l "It's really not bad, give it a shot."
            elif Speaker == JeanX:
                ch_j "Come on. . . [Subject.tag], it could be fun."
                $ B2 += 50
            elif Speaker == StormX:
                ch_s "Now [Subject.tag], it would not be so bad, would it?"
            elif Speaker == JubesX:
                ch_v "Come on, you in, [Subject.tag]? . ."
            if B2 >= 100:
                $ Result = 1
                $ Speaker.GirlLikeUp(Subject,(int(B/10)))
                $ Subject.GirlLikeUp(Speaker,(int(B2/10)))
        else:
            return Result

    elif Step == 2:

        if approval >= 2:
            $ Speaker.change_face("_smile", 1)
            if Speaker == RogueX:
                ch_r "'Course!"
            elif Speaker == KittyX:
                ch_k "'Course!"
            elif Speaker == EmmaX:
                ch_e "Of course, [Speaker.player_petname]."
            elif Speaker == LauraX:
                ch_l "I'm in."
            elif Speaker == JeanX:
                ch_j "Sure, why not."
            elif Speaker == StormX:
                ch_s "Sounds fun."
            elif Speaker == JubesX:
                ch_v "Sure, sounds fun."
            $ Result = 1
            return Result

        $ Speaker.change_face("_sly", 2)
        if Speaker == RogueX:
            if B >= 100:
                ch_r "I don't know, maybe. . ."
            if B >= 0:
                ch_r "I'm not sure about her though. . ."
        elif Speaker == KittyX:
            if B >= 100:
                ch_k "Yeah, I mean I guess. . ."
            if B >= 0:
                ch_k "No offense [Subject.tag], but. . ."
        elif Speaker == EmmaX:
            if B >= 100:
                ch_e "Mmmmm, certainly. . ."
            if B >= 0:
                ch_e "[Subject.tag], dear, I don't really think so. . ."
        elif Speaker == LauraX:
            if B >= 100:
                ch_l "You're cute and all. . ."
            if B >= 0:
                ch_l "I don't know, [Subject.tag]. . ."
        elif Speaker == JeanX:
            if B >= 100:
                ch_j "She's not bad. . ."
            if B >= 0:
                ch_j "With her? . ."
        elif Speaker == StormX:
            if B >= 100:
                ch_s "Oh, yes. . ."
            if B >= 0:
                ch_s "I am unsure. . ."
        elif Speaker == JubesX:
            if B >= 100:
                ch_v "Definitely. . ."
            if B >= 0:
                ch_v "I dunno. . ."
        $ Speaker.blushing = "_blush1"
        menu:
            extend ""
            "Ok, that's fine. . .":
                if B >= 100:
                    if Speaker == RogueX:
                        ch_r "Never mind, I'm in."
                    elif Speaker == KittyX:
                        ch_k "No, no, let's do this."
                    elif Speaker == EmmaX:
                        ch_e "Oh, don't back out now. . ."
                    elif Speaker == LauraX:
                        ch_l "Oh, no, I'm in."
                    elif Speaker == JeanX:
                        ch_j "Oh, don't get me wrong, I'm on board."
                    elif Speaker == StormX:
                        ch_s "No, no, I -am- interested. . ."
                    elif Speaker == JubesX:
                        ch_v "Oh, wait, I'm in!"
                    $ Result = 1
                else:
                    $ Speaker.change_face("_smile")
                    if Speaker == RogueX:
                        ch_r "Thanks, I appreciate it."
                    elif Speaker == KittyX:
                        ch_k "Thanks, I appreciate it."
                    elif Speaker == EmmaX:
                        ch_e "I appreciate your restraint."
                    elif Speaker == LauraX:
                        ch_l "Yeah. . ."
                    elif Speaker == JeanX:
                        ch_j "Right. . ."
                    elif Speaker == StormX:
                        ch_s "I appreciate that, thank you."
                    elif Speaker == JubesX:
                        ch_v "Yeah, thanks."
            "Come on, you might enjoy it. . .":
                if B >= 50:
                    if Speaker == RogueX:
                        ch_r "Well, I suppose."
                    elif Speaker == KittyX:
                        ch_k "I mean, maybe?"
                    elif Speaker == EmmaX:
                        ch_e "I'm sure I would. . ."
                    elif Speaker == LauraX:
                        ch_l "Maybe. . "
                    elif Speaker == JeanX:
                        ch_j "Yeah, I guess. . ."
                    elif Speaker == StormX:
                        ch_s "I suppose that I might. . ."
                    elif Speaker == JubesX:
                        ch_v "I guess. . ."
                    $ Result = 1
                else:
                    $ Speaker.change_face("_sad", 2)
                    if Speaker == RogueX:
                        ch_r "I don't think so."
                    elif Speaker == KittyX:
                        ch_k "Probably not."
                    elif Speaker == EmmaX:
                        ch_e "Probably not."
                    elif Speaker == LauraX:
                        ch_l "I doubt it."
                    elif Speaker == JeanX:
                        ch_j "Doubt it."
                    elif Speaker == StormX:
                        ch_s "Not at the moment though."
                    elif Speaker == JubesX:
                        ch_v "I don't know, I don't think so. . ."
            "Get in there, now.":
                if approval_check(Speaker, 550, "OI", TabM = 2):
                    $ Speaker.change_face("_sadside", 1)
                    if Speaker == RogueX:
                        ch_r "Fine, whatever."
                    elif Speaker == KittyX:
                        ch_k "Fiiine."
                    elif Speaker == EmmaX:
                        ch_e "Oh, fine."
                    elif Speaker == LauraX:
                        ch_l "Fine."
                    elif Speaker == JeanX:
                        ch_j "Oh, whatever."
                    elif Speaker == StormX:
                        ch_s "Fine."
                    elif Speaker == JubesX:
                        ch_v "Oh, whatever."
                    $ Result = 1
                else:
                    $ Speaker.change_face("_angry")
                    if Speaker == RogueX:
                        ch_r "Who do you think you're talk'in to?"
                    elif Speaker == KittyX:
                        ch_k "You're not the boss of me!"
                    elif Speaker == EmmaX:
                        ch_e "Don't forget who's in charge here, [Speaker.player_petname]"
                    elif Speaker == LauraX:
                        ch_l "Don't push me."
                    elif Speaker == JeanX:
                        ch_j "Don't you tell me what to \"get into.\""
                    elif Speaker == StormX:
                        ch_s "This is not how one asks a favor."
                    elif Speaker == JubesX:
                        ch_v "No way!"
                    $ Speaker.add_word(1,"_angry","_angry")
            "[Subject.name], what do you think?":
                $ Subject.change_face("_sexy", 1)
                $ Speaker.GirlLikeUp(Subject,(int(B/10)))
                if B >= 50:
                    $ Subject.GirlLikeUp(Speaker,5)
                if Subject == RogueX:
                    if Speaker == KittyX:
                        if Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                            ch_r "You know that we work well together."
                        else:
                            ch_r "It could be a lot of fun."
                    elif Speaker == EmmaX:
                        if Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                            ch_r "You could do that thing from last time. . ."
                        else:
                            ch_r "I was hoping you could give me some after class lessons. . ."
                    else:
                        if Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                            ch_r "Oh, it's not that bad."
                        else:
                            ch_r "It could be a lot of fun."
                elif Subject == KittyX:
                    if Speaker == RogueX:
                        if Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                            ch_k "Come on [Speaker.tag], you know we have fun."
                        else:
                            ch_k "Come on [Speaker.tag], could be fun."
                    elif Speaker in (EmmaX,StormX):
                        if Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                            ch_k "I mean, it might be nice to show [Subject.player_petname] what you've taught me. . ."
                        else:
                            ch_k "I've seen you watching me in class. . ."
                    else:
                        if Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                            ch_k "We have so much fun together though."
                        else:
                            ch_k "It could be fun!"
                elif Subject == EmmaX:
                    if Speaker == StormX:
                        ch_e "I really think we have a few things we could teach [EmmaX.player_petname] here. . ."
                    elif Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                        ch_e "What's the matter [Speaker.name], too shy around [Player.name]?"
                    else:
                        ch_e "What's the matter [Speaker.name], I've seen how you look at me. . ."
                elif Subject == LauraX:
                    if Speaker == EmmaX:
                        if Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                            ch_l "Wow, you aren't this shy when [Subject.player_petname]'s not around."
                        else:
                            ch_l "Come on, you look really squishy."
                    else:
                        if Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                            ch_l "What, you don't want to fuck with [Player.name] around?"
                        else:
                            ch_l "Come on, you look like you have it in you."
                elif Subject == JeanX:
                    if Speaker == EmmaX:
                        ch_j "Come on, we both know you're into this shit."
                    else:
                        if Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                            ch_j "What, -now- you're getting shy?"
                        else:
                            ch_j "Come on, I bet you really get around."
                elif Subject == StormX:
                    if Speaker == KittyX:
                        if Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                            ch_s "Now [Speaker.tag], this certainly wouldn't be your first lesson. . ."
                        else:
                            ch_s "Now [Speaker.tag], haven't you taken -any- interest in me?"
                    elif Speaker == EmmaX:
                        if Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                            ch_s "Now [Subject.player_petname], that isn't what you've said in the past. . ."
                        else:
                            ch_s "Oh? You want to pass up the opportunity to teach [StormX.player_petname] a few things. . ."
                    else:
                        if Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                            ch_s "You haven't enjoyed our time together?"
                        else:
                            ch_s "I can promise you would enjoy yourself. . ."
                elif Subject == JubesX:
                    if Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                        ch_v "I mean, it's not like this is our -first time- or anything. . ."
                    else:
                        ch_v "I think I can carry my weight over here. . ."


                if B >= 50:

                    $ Speaker.change_face("_smile", 1)
                    if Speaker == RogueX:
                        ch_r "You know, I can't argue with that, [Subject.tag]."
                    elif Speaker == KittyX:
                        ch_k "Heh, I guess so, [Subject.tag]."
                    elif Speaker == EmmaX:
                        ch_e "If we must, [Subject.tag]."
                    elif Speaker == LauraX:
                        ch_l "I guess so."
                    elif Speaker == JeanX:
                        ch_j "Fair point. . ."
                    elif Speaker == StormX:
                        ch_s "Well you do make a compelling case. . ."
                    elif Speaker == JubesX:
                        ch_v "Well, that's true. . ."
                    $ Result = 1
                else:

                    $ Speaker.change_face("_angry", 1, Eyes="_side")
                    if Speaker == RogueX:
                        ch_r "Sorry [Subject.tag], nothin personal."
                    elif Speaker == KittyX:
                        ch_k "Sorry [Subject.tag], I don't mean anything personal."
                    elif Speaker == EmmaX:
                        ch_e "I'm sorry [Subject.tag], it's really not you."
                    elif Speaker == LauraX:
                        ch_l "Sorry [Subject.tag], it's not about you."
                    elif Speaker == JeanX:
                        ch_j "Yeah, I'm really not interested."
                    elif Speaker == StormX:
                        ch_s "I'm afraid not, [Subject.tag]."
                    elif Speaker == JubesX:
                        ch_v "No way, nothing personal, [Subject.tag]."

    if Step == 3:

        if approval:
            $ Speaker.change_face("_smile", 1)
            if Speaker == RogueX:
                ch_r "I mean, I guess so. . ."
            elif Speaker == KittyX:
                ch_k "I mean, I guess. . ."
            elif Speaker == EmmaX:
                ch_e "How could I back out now?"
            elif Speaker == LauraX:
                ch_l "Yeah. . ."
            elif Speaker == JeanX:
                ch_j "Well, I guess."
            elif Speaker == StormX:
                ch_s "I suppose we could continue. . ."
            elif Speaker == JubesX:
                ch_v "Well, I guess if you're into it. . ."
            $ Result = 1
        else:
            $ Speaker.change_face("_sadside", 1)
            if Speaker == RogueX:
                ch_r "I'm really not into that right now. . ."
            elif Speaker == KittyX:
                ch_k "I'm really not into it atm. . ."
            elif Speaker == EmmaX:
                ch_e "I'm afraid not. . ."
            elif Speaker == LauraX:
                ch_l "Not right now. . ."
            elif Speaker == JeanX:
                ch_j "Not into it."
            elif Speaker == StormX:
                ch_s "I would rather not."
            elif Speaker == JubesX:
                ch_v "Nah, not into it."
    if not Result:

        $ Speaker.recent_history.append("no_lesbian")
        $ Speaker.daily_history.append("no_lesbian")
        $ Speaker.change_face("_sadside", 1)
        $ Partner = 0
        if Speaker == RogueX:
            if B <= 0:
                ch_r "Sorry, [Speaker.player_petname], it's just not like that with her."
            if Speaker.Taboo > 20:
                ch_r "Sorry, [Speaker.player_petname], this isn't a good place for it."
            if B >= 100:
                ch_r "Sorry, [Speaker.player_petname], maybe if you weren't around. . ."
            else:
                ch_r "Sorry, [Speaker.player_petname], I'm just not interested."
        elif Speaker == KittyX:
            if B <= 0:
                ch_k "Sorry, [Speaker.player_petname], I'm just not into her."
            if Speaker.Taboo > 20:
                ch_k "Sorry, [Speaker.player_petname], this isn't exactly the right place for that."
            if B >= 100:
                ch_k "Sorry, [Speaker.player_petname], not with you watching. . ."
            else:
                ch_k "Sorry, [Speaker.player_petname], I'm just not into it."
        elif Speaker == EmmaX:
            if B <= 0:
                ch_e "I'm sorry, [Speaker.player_petname], she's just not my type."
            if Speaker.Taboo > 20:
                ch_e "I'm sorry, [Speaker.player_petname], this would cause a scandal."
            if B >= 100:
                ch_e "I'm sorry, [Speaker.player_petname], not with an audience. . ."
            else:
                ch_e "I'm sorry, [Speaker.player_petname], I'm just not interested in that."
        elif Speaker == LauraX:
            if B <= 0:
                ch_l "Sorry, [Speaker.player_petname], she's not my type."
            if Speaker.Taboo > 20:
                ch_l "Sorry, [Speaker.player_petname], this area's a bit exposed."
            if B >= 100:
                ch_l "Sorry, [Speaker.player_petname], I don't want an audience. . ."
            else:
                ch_l "Sorry, [Speaker.player_petname], I'm just not into that."
        elif Speaker == JeanX:
            if B <= 0:
                ch_l "Sorry, [Speaker.player_petname], I know I can do better than her."
            if Speaker.Taboo > 20:
                ch_l "Sorry, [Speaker.player_petname]. . . not in public."
            if B >= 100:
                ch_l "Sorry, [Speaker.player_petname], you'll have to earn that . ."
            else:
                ch_l "Sorry, [Speaker.player_petname], not right now."
        elif Speaker == StormX:
            if B <= 0:
                ch_s "Apologies, [Speaker.player_petname], I could not, with her."
            if Speaker.Taboo > 20:
                ch_s "Apologies, [Speaker.player_petname], this is not the place for it."
            if B >= 100:
                ch_s "Apologies, [Speaker.player_petname], this is a private affair. . ."
            else:
                ch_s "Apologies, [Speaker.player_petname], I am just uninterested."
        elif Speaker == JubesX:
            if B <= 0:
                ch_v "Sorry, [Speaker.player_petname], she's not my type."
            if Speaker.Taboo > 20:
                ch_v "Sorry, [Speaker.player_petname], not here, at least."
            if B >= 100:
                ch_v "Sorry, [Speaker.player_petname], I don't want an audience. . ."
            else:
                ch_v "Sorry, [Speaker.player_petname], I'm not into it."


    return Result



label Les_FirstKiss:

    if "les " + Partner.tag in Girl.history:

        $ Line = "experienced"
    elif Girl.event_counter["been_with_girl"] and Partner.event_counter["been_with_girl"]:

        $ Line = "first both"
    elif Girl.event_counter["been_with_girl"]:

        $ Line = "first girl"
    elif Partner.event_counter["been_with_girl"]:

        $ Line = "first partner"

    if Line == "experienced":
        "[Girl.name] and [Partner.name] move together in a passionate kiss."
        "[Girl.name]'s arms firmly grasp [Partner.name]'s neck and pull her close."
    else:
        if Line in ("first both", "first girl"):

            "[Girl.name] slowly moves in and gives [Partner.name] a soft kiss."
        else:

            "[Girl.name] casually places a hand on the back of [Partner.name]'s head and draws their lips together."
        if Line == "first partner":

            "[Partner.name] pulls back a bit, but slowly leans into the enbrace."
        else:

            "[Partner.name]'s lips curl up into a smile and she draws [Girl.name] even closer."
        "After a few seconds, it begins to grow more passionate."
    return





label Girl_Whammy(Other):

    if "nowhammy" not in JeanX.traits and Other.LikeJean < 800:

        $ Player.add_word(1,0,0,0,"whammied")
        if Other == EmmaX and EmmaX.level >= JeanX.level:
            ch_e "Oh, don't even try that nonsense with me, Ms. Grey."
            return
        if Other == JubesX and JubesX.level >= JeanX.level:
            ch_v "Vampire whammy beats mutant whammy!"
            return
        if "Jeaned" not in Other.traits:
            $ Other.traits.append("Jeaned")
            $ setattr(JeanX,"LikeS"+Other.tag,Other.LikeJean)
        $ Other.LikeJean += 500 if Other.LikeJean <= 900 else Other.LikeJean
        $ Other.LikeJean = 900 if Other.LikeJean >= 900 else Other.LikeJean
    return




label Les_Change(Primary=0, Secondary=Partner, D20S=0, PrimaryLust=0, SecondaryLust=0):



    if Primary not in all_Girls:
        return
    $ Line = 0
    menu:
        "Hey [Primary.name]. . ."
        "why don't you kiss her?" if second_girl_offhand_action != "kiss girl" and second_girl_offhand_action != "kiss both":
            call Threeway_Set (Primary, "kiss girl", "lesbian", girl_offhand_action, Secondary)
        "why don't you grab her tits?" if girl_offhand_action != "fondle_breasts":
            call Threeway_Set (Primary, "fondle_breasts", "lesbian", girl_offhand_action, Secondary)
        "why don't you suck her breasts?" if girl_offhand_action != "suck_breasts":
            call Threeway_Set (Primary, "suck_breasts", "lesbian", girl_offhand_action, Secondary)
        "why don't you finger her?" if girl_offhand_action != "fondle_pussy":
            call Threeway_Set (Primary, "fondle_pussy", "lesbian", girl_offhand_action, Secondary)
        "why don't you go down on her?" if girl_offhand_action != "eat_pussy":
            call Threeway_Set (Primary, "eat_pussy", "lesbian", girl_offhand_action, Secondary)
        "why don't you grab her ass?" if girl_offhand_action != "fondle_ass":
            call Threeway_Set (Primary, "fondle_ass", "lesbian", girl_offhand_action, Secondary)
        "why don't you lick her ass?" if girl_offhand_action != "eat_ass":
            call Threeway_Set (Primary, "eat_ass", "lesbian", girl_offhand_action, Secondary)
        "never mind.":
            pass
    if not Line:
        $ Line = "You return to what you were doing."
    else:
        $ action_context = "skip"
    "[Line]"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
