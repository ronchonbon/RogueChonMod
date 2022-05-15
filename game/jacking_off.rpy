# Start Jackin it check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Jackin(Girl=0,counter=0,Girls=[]): #rkeljsv
        #Called when you try to jack it from inside a sex action
        #should include a girl's name, if not, one is randomly picked from the room.
        if not Girl or Girl not in all_Girls:
                $ Girls = all_Girls[:]
                while Girls:
                        if Girls[0].location == bg_current:
                                $ Girl = Girls[0]
                                $ Girls = [1]
                        $ Girls.remove(Girls[0])

        if "unseen" in Girl.recent_history:
                $ Player.recent_history.append("cockout")
                $ offhand_action = "jackin"
                "You whip out your cock and start working it."
        else:
                if not Player.Semen:
                        "You don't think that would accomplish much, the poor thing is napping."
                        return

                if "cockout" in Player.recent_history:
                        "You start working your cock."
                else:
                        "You whip out your cock and start working it."
                        $ Player.recent_history.append("cockout")
                        call Seen_First_Peen(Girl,Partner)

                $ offhand_action = "jackin"
                if "jackin" in Girl.recent_history:
                    return
                $ Girl.AddWord(0,"jackin","jackin",0,0)

                if Girl == EmmaX and "classcaught" not in Girl.History:
                        $ Girl.change_face("surprised", 1)
                        $ Girl.Eyes = "down"
                        ch_e "Wait. . ."
                        $ Girl.change_face("angry", 1)
                        ch_e "That really isn't appropriate."
                        $ Girl.change_stat("lust", 50, 7)
                        if not ApprovalCheck(EmmaX, 1200, TabM = 3):
                                $ Girl.AddWord(0,"angry","angry",0,0)
                                $ renpy.pop_call()
                                return

                if Girl.SEXP < 10 and Girl not in (JeanX,StormX):
                        $ Girl.change_face("surprised", 2)
                        $ Girl.Eyes = "down"
                        if Girl == LauraX:
                                $ Girl.Brows = "confused"
                                "[Girl.name] seems perplexed that you would do something like that."
                        else:
                                "[Girl.name] blushes furiously, shocked at your behavior."
                        $ Girl.change_face("angry", 1)
                        $ Girl.change_stat("lust", 50, 5)
                        if not ApprovalCheck(Girl, 1200, TabM = 3):
                                $ Girl.AddWord(0,"angry","angry",0,0)
                                $ renpy.pop_call()
                                return
                elif Girl.SEXP <= 15:
                        $ Girl.change_face("surprised", 2)
                        $ Girl.Eyes = "down"
                        if Girl == EmmaX:
                                $ Girl.Blush = 1
                                "[Girl.name] looks down at your cock with some surprise."
                                $ Girl.change_stat("lust", 60, 2)
                        else:
                                "[Girl.name] looks down at your cock with surprise."
                        $ Girl.change_face("perplexed", 1)
                        $ Girl.change_stat("lust", 60, 8)
                        if not ApprovalCheck(Girl, 1200, TabM = 3) and Girl != JeanX:
                                return
                elif ApprovalCheck(Girl, 1100, TabM = 3):
                        $ Girl.change_face("surprised", 1)
                        $ Girl.Eyes = "down"
                        "[Girl.name] looks down at your cock and smiles."
                        $ Girl.change_face("sly", 1)
                        $ Girl.change_stat("lust", 70, 8, alternates = {"Emma": {"check": 60, "value": 12})
                elif ApprovalCheck(Girl, 500, "I", TabM=2):
                        $ Girl.change_face("surprised", 1)
                        $ Girl.Eyes = "down"
                        "[Girl.name] glances at it, but just smiles in amusement."
                        $ Girl.change_face("sly", 1)
                        $ Girl.change_stat("lust", 70, 10, alternates = {"Emma": {"check": 60, "value": 15})
                else:
                        $ Girl.change_face("angry", 1)
                        $ Girl.Eyes = "down"
                        "[Girl.name] glances down at your cock with a scowl."
                        $ Girl.Eyes = "sexy"
                        $ Girl.AddWord(0,"angry","angry",0,0)
                        return

                if Girl.Action and Girl.location == bg_current:
                    $ Girls = ["none"]

                    if Girl.Hand >= 5 and ApprovalCheck(Girl, 1100, TabM = 3):
                            $ counter = Girl.Hand - 4
                            $ counter = 10 if counter > 10 else counter
                            while counter:
                                $ Girls.append("handjob")
                                $ counter -= 1
                    if Girl.Blow >= 5 and ApprovalCheck(Girl, 1300, TabM = 3):
                            $ counter = Girl.Blow - 4
                            $ counter = 10 if counter > 10 else counter
                            $ counter += 5 if "hungry" in Girl.Traits else 0
                            while counter:
                                $ Girls.append("blowjob")
                                $ counter -= 1
                    if Girl.Tit >= 5 and ApprovalCheck(Girl, 1200, TabM = 5):
                            $ counter = Girl.Tit - 4
                            $ counter = 10 if counter > 10 else counter
                            while counter:
                                $ Girls.append("Tit")
                                $ counter -= 1
                    if Girl.Sex >= 5 and ApprovalCheck(Girl, 1400, TabM = 5):
                            $ counter = Girl.Sex - 4
                            $ counter = 10 if counter > 10 else counter
                            $ counter += 5 if Girl.lust >= 70 else 0
                            while counter:
                                $ Girls.append("sex")
                                $ counter -= 1
                    if Girl.Anal >= 5 and ApprovalCheck(Girl, 1550, TabM = 5):
                            $ counter = Girl.Anal - 4
                            $ counter = 10 if counter > 10 else counter
                            $ counter += 5 if Girl.lust >= 70 and Girl.Loose else 0
                            while counter:
                                $ Girls.append("anal")
                                $ counter -= 1

                    $ renpy.random.shuffle(Girls)

                    if Girls[0] == "handjob":
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
                    elif Girls[0] == "blowjob" or (Girl == JubesX and JubesX.Blow):
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
                                    $ Girl.change_face("sly", 1,Mouth="tongue")
                                    ch_v "I uh, wouldn't mind giving that my full attention. . ."
                                    $ Girl.Mouth="smile"
                    elif Girls[0] == "tit":
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
                    elif Girls[0] == "sex":
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
                    elif Girls[0] == "anal":
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
                                        ch_r "Your loss, [Girl.Petname]."
                                elif Girl == KittyX:
                                        ch_k "What ev, [Girl.Petname]."
                                elif Girl == EmmaX:
                                        $ Girl.change_face("perplexed", 1)
                                        ch_e "Oh. . ."
                                        ch_e "Carry on then, [Girl.Petname]."
                                        $ Girl.change_face("sly", 0,Eyes="down")
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
                    #Close out what you were doing
                    if primary_action == "strip":
                            call Group_Strip_End
                    elif primary_action == "masturbation":
                            $ Girl.Action -= 1
                            $ Girl.Mast += 1
                            call Checkout
                    elif primary_action:
                            call CloseOut(Girl)

                    show blackscreen onlayer black
                    hide blackscreen onlayer black
                    if Girls[0] == "handjob":
                            jump expression Girl.Tag + "_HJ_Prep"
                    elif Girls[0] == "blowjob":
                            jump expression Girl.Tag + "_BJ_Prep"
                    elif Girls[0] == "tit":
                            jump expression Girl.Tag + "_TJ_Prep"
                    elif Girls[0] == "sex":
                            jump expression Girl.Tag + "_SexPrep"
                    elif Girls[0] == "anal":
                            jump expression Girl.Tag + "_AnalPrep"
        return
# end Jackin it check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# For when she tags you to drain you start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Tag(Girl=0,Forced = 0,Gloves=0): #rkeljsv
        #Called mostly by Addiction
        $ Girl = GirlCheck(Girl)
        call shift_focus(Girl)
        $ Gloves = Girl.Arms
        $ Girl.ArmPose = 2
        if not Forced:
                $ Girl.Eyes = "closed"
                $ Girl.Brows = "sad"

        if Forced and Player.Lvl >= 5:
            if Gloves == "gloves":
                    $ Girl.Arms = 0
                    "She pulls off her gloves and reaches for your face."
            else:
                    "She reaches out towards your face."
            menu:
                extend ""
                "Catch her arm [[refuse].":
                        $ Girl.change_face("surprised", 1)
                        "As she reaches out, you bat her arm away. The brief contact isn't enough for her."
                        $ Girl.change_face("angry")
                        $ Girl.change_stat("love", 80, -10)
                        if Girl.Addict >= 80 and not ApprovalCheck(Girl, 400, "O",Alt=[[RogueX],600]):
                                #if she's strung out and not obedient
                                $ Girl.Eyes = "manic"
                                "She lashes out and leaps at you, grabbing you by the chin."
                                $ Girl.Eyes = "sly"
                                if "no_tag" not in Girl.recent_history:
                                        $ Girl.change_stat("obedience", 50, -5)
                                        $ Girl.change_stat("inhibition", 30, 5)
                                        $ Girl.change_stat("inhibition", 90, 1)
                                $ Forced = 1
                        else:
                                if Girl == RogueX:
                                        ch_r "Not cool, [Girl.Petname]."
                                elif Girl == KittyX:
                                        ch_k "[Girl.Like]so not cool, [Girl.Petname]."
                                elif Girl == EmmaX:
                                        ch_e "You don't want me as an enemy, [Player.name]."
                                elif Girl == LauraX:
                                        ch_l "Don't push me, [Girl.Petname]."
                                elif Girl == JeanX:
                                        ch_j "You won't like me when I'm angry, [Girl.Petname]."
                                elif Girl == StormX:
                                        ch_s "Do not toy with me, [Girl.Petname]."
                                elif Girl == JubesX:
                                        ch_v "Please. . ."
                                if "no_tag" not in Girl.recent_history:
                                        $ Girl.change_stat("obedience", 50, 5)
                                        $ Girl.change_stat("obedience", 80, 5)
                                $ Girl.recent_history.append("no_tag")
                                $ Girl.daily_history.append("no_tag")
                                $ Girl.Arms = Gloves
                                $ Girl.ArmPose = 1
                                return
                "Let her.":
                        "She touches your face."
        else:
                $ Girl.Addict -= 10
                $ Girl.Addictionrate += 1 if Girl.Addictionrate < 5 else 0
                $ Girl.change_stat("lust", 90, 5)
                if Gloves == "gloves":
                        $ Girl.Arms = 0
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
        $ Girl.Blush = 2

        if Round <= 15:
                $ Girl.Addict -= 15 if Girl.Addict > 15 else Girl.Addict
        while Girl.Addict > 20 and Round > 15:
                $ Girl.Addictionrate += 1 if Girl.Addictionrate < 5 else 0
                $ Girl.Addict -= 15
                $ Round -= 5
                $ Girl.change_stat("lust", 90, 5)
                if Girl == RogueX:
                        $ Girl.change_stat("lust", 90, 5)
                elif Forced:
                        $ Girl.change_stat("obedience", 50, 1)
                "She continues to touch you, and a slight shiver passes through her."
        if Round <= 15:
                call Anyline(Girl,"I suppose we don't have time for any more than that.")
        if Gloves and not Girl.Arms:
                "Appearing sated, she puts her gloves back on."
        $ Girl.Blush = 1
        $ Girl.Arms = Gloves
        $ Girl.ArmPose = 1
        $ Girl.change_face()
        if Forced:
                $ Girl.recent_history.append("forced tag")
                $ Girl.daily_history.append("forced tag")
        $ Girl.recent_history.append("tag")
        $ Girl.daily_history.append("tag")
        return
# End "tag" action / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
