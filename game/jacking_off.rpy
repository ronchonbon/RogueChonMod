# Start Jackin it check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Jackin(Girl=0,Cnt=0,BO=[]): #rkeljsv
        #Called when you try to jack it from inside a sex action
        #should include a girl's name, if not, one is randomly picked from the room.
        if not Girl or Girl not in TotalGirls:
                $ BO = TotalGirls[:]
                while BO:
                        if BO[0].Loc == bg_current:
                                $ Girl = BO[0]
                                $ BO = [1]
                        $ BO.remove(BO[0])

        if "unseen" in Girl.RecentActions:
                $ Player.RecentActions.append("cockout")
                $ Trigger2 = "jackin"
                "You whip out your cock and start working it."
        else:
                if not Player.Semen:
                        "You don't think that would accomplish much, the poor thing is napping."
                        return

                if "cockout" in Player.RecentActions:
                        "You start working your cock."
                else:
                        "You whip out your cock and start working it."
                        $ Player.RecentActions.append("cockout")
                        call Seen_First_Peen(Girl,Partner)

                $ Trigger2 = "jackin"
                if "jackin" in Girl.RecentActions:
                    return
                $ Girl.AddWord(0,"jackin","jackin",0,0)

                if Girl == EmmaX and "classcaught" not in Girl.History:
                        $ Girl.FaceChange("surprised", 1)
                        $ Girl.Eyes = "down"
                        ch_e "Wait. . ."
                        $ Girl.FaceChange("angry", 1)
                        ch_e "That really isn't appropriate."
                        $ Girl.Statup("Lust", 50, 7)
                        if not ApprovalCheck(EmmaX, 1200, TabM = 3):
                                $ Girl.AddWord(0,"angry","angry",0,0)
                                $ renpy.pop_call()
                                return

                if Girl.SEXP < 10 and Girl not in (JeanX,StormX):
                        $ Girl.FaceChange("surprised", 2)
                        $ Girl.Eyes = "down"
                        if Girl == LauraX:
                                $ Girl.Brows = "confused"
                                "[Girl.Name] seems perplexed that you would do something like that."
                        else:
                                "[Girl.Name] blushes furiously, shocked at your behavior."
                        $ Girl.FaceChange("angry", 1)
                        $ Girl.Statup("Lust", 50, 5)
                        if not ApprovalCheck(Girl, 1200, TabM = 3):
                                $ Girl.AddWord(0,"angry","angry",0,0)
                                $ renpy.pop_call()
                                return
                elif Girl.SEXP <= 15:
                        $ Girl.FaceChange("surprised", 2)
                        $ Girl.Eyes = "down"
                        if Girl == EmmaX:
                                $ Girl.Blush = 1
                                "[Girl.Name] looks down at your cock with some surprise."
                                $ Girl.Statup("Lust", 60, 2)
                        else:
                                "[Girl.Name] looks down at your cock with surprise."
                        $ Girl.FaceChange("perplexed", 1)
                        $ Girl.Statup("Lust", 60, 8)
                        if not ApprovalCheck(Girl, 1200, TabM = 3) and Girl != JeanX:
                                return
                elif ApprovalCheck(Girl, 1100, TabM = 3):
                        $ Girl.FaceChange("surprised", 1)
                        $ Girl.Eyes = "down"
                        "[Girl.Name] looks down at your cock and smiles."
                        $ Girl.FaceChange("sly", 1)
                        $ Girl.Statup("Lust", 70, 8,Alt=[[EmmaX],60,12])
                elif ApprovalCheck(Girl, 500, "I", TabM=2):
                        $ Girl.FaceChange("surprised", 1)
                        $ Girl.Eyes = "down"
                        "[Girl.Name] glances at it, but just smiles in amusement."
                        $ Girl.FaceChange("sly", 1)
                        $ Girl.Statup("Lust", 70, 10,Alt=[[EmmaX],60,15])
                else:
                        $ Girl.FaceChange("angry", 1)
                        $ Girl.Eyes = "down"
                        "[Girl.Name] glances down at your cock with a scowl."
                        $ Girl.Eyes = "sexy"
                        $ Girl.AddWord(0,"angry","angry",0,0)
                        return

                if Girl.Action and Girl.Loc == bg_current:
                    $ BO = ["none"]

                    if Girl.Hand >= 5 and ApprovalCheck(Girl, 1100, TabM = 3):
                            $ Cnt = Girl.Hand - 4
                            $ Cnt = 10 if Cnt > 10 else Cnt
                            while Cnt:
                                $ BO.append("hand")
                                $ Cnt -= 1
                    if Girl.Blow >= 5 and ApprovalCheck(Girl, 1300, TabM = 3):
                            $ Cnt = Girl.Blow - 4
                            $ Cnt = 10 if Cnt > 10 else Cnt
                            $ Cnt += 5 if "hungry" in Girl.Traits else 0
                            while Cnt:
                                $ BO.append("blow")
                                $ Cnt -= 1
                    if Girl.Tit >= 5 and ApprovalCheck(Girl, 1200, TabM = 5):
                            $ Cnt = Girl.Tit - 4
                            $ Cnt = 10 if Cnt > 10 else Cnt
                            while Cnt:
                                $ BO.append("Tit")
                                $ Cnt -= 1
                    if Girl.Sex >= 5 and ApprovalCheck(Girl, 1400, TabM = 5):
                            $ Cnt = Girl.Sex - 4
                            $ Cnt = 10 if Cnt > 10 else Cnt
                            $ Cnt += 5 if Girl.Lust >= 70 else 0
                            while Cnt:
                                $ BO.append("sex")
                                $ Cnt -= 1
                    if Girl.Anal >= 5 and ApprovalCheck(Girl, 1550, TabM = 5):
                            $ Cnt = Girl.Anal - 4
                            $ Cnt = 10 if Cnt > 10 else Cnt
                            $ Cnt += 5 if Girl.Lust >= 70 and Girl.Loose else 0
                            while Cnt:
                                $ BO.append("anal")
                                $ Cnt -= 1

                    $ renpy.random.shuffle(BO)

                    if BO[0] == "hand":
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
                    elif BO[0] == "blow" or (Girl == JubesX and JubesX.Blow):
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
                                    $ Girl.FaceChange("sly", 1,Mouth="tongue")
                                    ch_v "I uh, wouldn't mind giving that my full attention. . ."
                                    $ Girl.Mouth="smile"
                    elif BO[0] == "tit":
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
                                        ch_r "Your loss, [Girl.Petname]."
                                elif Girl == KittyX:
                                        ch_k "What ev, [Girl.Petname]."
                                elif Girl == EmmaX:
                                        $ Girl.FaceChange("perplexed", 1)
                                        ch_e "Oh. . ."
                                        ch_e "Carry on then, [Girl.Petname]."
                                        $ Girl.FaceChange("sly", 0,Eyes="down")
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
                                $ Situation = "shift"

                    $ Trigger2 = 0
                    #Close out what you were doing
                    if Trigger == "strip":
                            call Group_Strip_End
                    elif Trigger == "masturbation":
                            $ Girl.Action -= 1
                            $ Girl.Mast += 1
                            call Checkout
                    elif Trigger:
                            call CloseOut(Girl)

                    show blackscreen onlayer black
                    hide blackscreen onlayer black
                    if BO[0] == "hand":
                            jump expression Girl.Tag + "_HJ_Prep"
                    elif BO[0] == "blow":
                            jump expression Girl.Tag + "_BJ_Prep"
                    elif BO[0] == "tit":
                            jump expression Girl.Tag + "_TJ_Prep"
                    elif BO[0] == "sex":
                            jump expression Girl.Tag + "_SexPrep"
                    elif BO[0] == "anal":
                            jump expression Girl.Tag + "_AnalPrep"
        return
# end Jackin it check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# For when she tags you to drain you start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Tag(Girl=0,Forced = 0,Gloves=0): #rkeljsv
        #Called mostly by Addiction
        $ Girl = GirlCheck(Girl)
        call Shift_Focus(Girl)
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
                        $ Girl.FaceChange("surprised", 1)
                        "As she reaches out, you bat her arm away. The brief contact isn't enough for her."
                        $ Girl.FaceChange("angry")
                        $ Girl.Statup("Love", 80, -10)
                        if Girl.Addict >= 80 and not ApprovalCheck(Girl, 400, "O",Alt=[[RogueX],600]):
                                #if she's strung out and not obedient
                                $ Girl.Eyes = "manic"
                                "She lashes out and leaps at you, grabbing you by the chin."
                                $ Girl.Eyes = "sly"
                                if "no tag" not in Girl.RecentActions:
                                        $ Girl.Statup("Obed", 50, -5)
                                        $ Girl.Statup("Inbt", 30, 5)
                                        $ Girl.Statup("Inbt", 90, 1)
                                $ Forced = 1
                        else:
                                if Girl == RogueX:
                                        ch_r "Not cool, [Girl.Petname]."
                                elif Girl == KittyX:
                                        ch_k "[Girl.Like]so not cool, [Girl.Petname]."
                                elif Girl == EmmaX:
                                        ch_e "You don't want me as an enemy, [Player.Name]."
                                elif Girl == LauraX:
                                        ch_l "Don't push me, [Girl.Petname]."
                                elif Girl == JeanX:
                                        ch_j "You won't like me when I'm angry, [Girl.Petname]."
                                elif Girl == StormX:
                                        ch_s "Do not toy with me, [Girl.Petname]."
                                elif Girl == JubesX:
                                        ch_v "Please. . ."
                                if "no tag" not in Girl.RecentActions:
                                        $ Girl.Statup("Obed", 50, 5)
                                        $ Girl.Statup("Obed", 80, 5)
                                $ Girl.RecentActions.append("no tag")
                                $ Girl.DailyActions.append("no tag")
                                $ Girl.Arms = Gloves
                                $ Girl.ArmPose = 1
                                return
                "Let her.":
                        "She touches your face."
        else:
                $ Girl.Addict -= 10
                $ Girl.Addictionrate += 1 if Girl.Addictionrate < 5 else 0
                $ Girl.Statup("Lust", 90, 5)
                if Gloves == "gloves":
                        $ Girl.Arms = 0
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
        $ Girl.Blush = 2

        if Round <= 15:
                $ Girl.Addict -= 15 if Girl.Addict > 15 else Girl.Addict
        while Girl.Addict > 20 and Round > 15:
                $ Girl.Addictionrate += 1 if Girl.Addictionrate < 5 else 0
                $ Girl.Addict -= 15
                $ Round -= 5
                $ Girl.Statup("Lust", 90, 5)
                if Girl == RogueX:
                        $ Girl.Statup("Lust", 90, 5)
                elif Forced:
                        $ Girl.Statup("Obed", 50, 1)
                "She continues to touch you, and a slight shiver passes through her."
        if Round <= 15:
                call AnyLine(Girl,"I suppose we don't have time for any more than that.")
        if Gloves and not Girl.Arms:
                "Appearing sated, she puts her gloves back on."
        $ Girl.Blush = 1
        $ Girl.Arms = Gloves
        $ Girl.ArmPose = 1
        $ Girl.FaceChange()
        if Forced:
                $ Girl.RecentActions.append("forced tag")
                $ Girl.DailyActions.append("forced tag")
        $ Girl.RecentActions.append("tag")
        $ Girl.DailyActions.append("tag")
        return
# End "tag" action / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
