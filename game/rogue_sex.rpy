label Rogue_SexAct(Act = 0):
        if AloneCheck(RogueX) and RogueX.Taboo == 20:
                $ RogueX.Taboo = 0
                $ Taboo = 0
        call Shift_Focus(RogueX)
        if Act == "SkipTo":
                $ renpy.pop_call() #causes it to skip past the Trigger Swap
                $ renpy.pop_call() #causes it to skip past the cycle you were in before
                #$ renpy.pop_call() #causes it to skip past the sex menu you were in before that
                call SkipTo(RogueX)
        elif Act == "switch":
                $ renpy.pop_call() #causes it to skip past call here from Sex_Menu_Threesome
                #$ renpy.pop_call() #causes it to skip past call to Sex_Menu_Threesome
                # drops through to sex menu
        elif Act == "masturbate":
                call Rogue_M_Prep
                if not Situation:
                        return
        elif Act == "lesbian":
                call Les_Prep(RogueX)
                if not Situation:
                        return
        elif Act == "kissing":
                call KissPrep(RogueX)
                if not Situation:
                        return
        elif Act == "breasts":
                call Rogue_Fondle_Breasts
                if not Situation:
                        return
        elif Act == "blow":
                call Rogue_BJ_Prep
                if not Situation:
                        return
        elif Act == "hand":
                call Rogue_HJ_Prep
                if not Situation:
                        return
        elif Act == "sex":
                call sex_prep(RogueX)
                if not Situation:
                        return

label Rogue_Masturbate: #(Situation = Situation):
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(RogueX)
    if RogueX.Mast:
        $ temp_modifier += 10
    if RogueX.SEXP >= 50:
        $ temp_modifier += 25
    elif RogueX.SEXP >= 30:
        $ temp_modifier += 15
    elif RogueX.SEXP >= 15:
        $ temp_modifier += 5
    if RogueX.Lust >= 90:
        $ temp_modifier += 20
    elif RogueX.Lust >= 75:
        $ temp_modifier += 5
    if "exhibitionist" in RogueX.Traits:
        $ temp_modifier += (3*Taboo)
    if RogueX in Player.Harem or "sex friend" in RogueX.Petnames:
        $ temp_modifier += 10
    elif "ex" in RogueX.Traits:
        $ temp_modifier -= 40
    if RogueX.ForcedCount and not RogueX.Forced:
        $ temp_modifier -= 5 * RogueX.ForcedCount

    $ Approval = ApprovalCheck(RogueX, 1200, TabM = 2) # 120, 135, 150, Taboo -80(200)

    $ RogueX.DrainWord("unseen",1,0) #She sees you, so remove unseens

    if Situation == "join":       # This triggers if you ask to join in
                if Approval > 1 or (Approval and RogueX.Lust >= 50):
                    $ Player.AddWord(1,"join")
                    menu:
                        extend ""
                        "Would you like some help? I could lend some helping hands. . ."  if Player.Semen and RogueX.Action:
                                $ RogueX.Statup("Love", 90, 1)
                                $ RogueX.Statup("Obed", 50, 2)
                                $ RogueX.FaceChange("sexy")
                                ch_r "Well, [RogueX.Petname], I suppose I could use some help with these. . ."
                                $ RogueX.Statup("Obed", 70, 2)
                                $ RogueX.Statup("Inbt", 70, 1)
                                $ Trigger2 = "fondle breasts"
                                $ RogueX.Mast += 1
                                jump Rogue_M_Cycle
                        "Would you like some help? I could. . . up to you, I guess." if Player.Semen and RogueX.Action:
                                $ RogueX.Statup("Love", 70, 2)
                                $ RogueX.Statup("Love", 90, 1)
                                $ RogueX.FaceChange("sexy")
                                ch_r "Well, [RogueX.Petname], I suppose you could help me with these. . ."
                                $ RogueX.Statup("Obed", 70, 2)
                                $ RogueX.Statup("Inbt", 70, 1)
                                $ D20 = renpy.random.randint(1, 20)
                                if D20 > 10:
                                    $ Trigger2 = "fondle breasts"
                                else:
                                    $ Trigger2 = "suck breasts"
                                $ RogueX.Mast += 1
                                jump Rogue_M_Cycle
                        "Why don't we take care of each other?" if Player.Semen and RogueX.Action:
                                $ RogueX.FaceChange("sexy")
                                ch_r "Well what did you have in mind?"
                                $ renpy.pop_call()          #removes the call to this label
                                return                      #returns to sexmenu=
                        "You look like you have things well in hand. . .":
                                if RogueX.Lust >= 50:
                                    $ RogueX.Statup("Love", 70, 2)
                                    $ RogueX.Statup("Love", 90, 1)
                                    $ RogueX.FaceChange("sexy")
                                    ch_r "Well, [RogueX.Petname], I suppose I do at that . ."
                                    $ RogueX.Statup("Obed", 80, 3)
                                    $ RogueX.Statup("Inbt", 80, 5)
                                    jump Rogue_M_Cycle
                                elif ApprovalCheck(RogueX, 1000):
                                    $ RogueX.FaceChange("sly")
                                    ch_r "Well I did, but I think I've got it taken care of for now. . ."
                                else:
                                    $ RogueX.FaceChange("angry")
                                    ch_r "Well I did, but now you've blown the mood."

                #else: You've failed all checks so she kicks you out.
                $ RogueX.ArmPose = 1
                $ RogueX.OutfitChange(Changed=0)
                $ RogueX.Action -= 1
                $ Player.Statup("Focus", 50, 30)
                call Checkout(1)
                $ Line = 0
                $ Situation = 0
                $ renpy.pop_call()          #removes the call to this label
                if Approval:
                        $ RogueX.FaceChange("bemused", 2)
                        if bg_current == "bg rogue":
                            ch_r "So what did you come over for anyway, [RogueX.Petname]?"
                        else:
                            ch_r "So . . . fancy bumping into you here, [RogueX.Petname]. . ."
                        $ RogueX.Blush = 1
                else:
                        $ RogueX.Statup("Love", 200, -5)
                        $ RogueX.FaceChange("angry")
                        $ RogueX.RecentActions.append("angry")
                        $ RogueX.DailyActions.append("angry")
                        if bg_current == "bg rogue":
                            ch_r "Well if you don't mind, I'd kind of appreciate you getting out of here. Maybe knock next time?"
                            "[RogueX.Name] kicks you out of her room."
                            $ renpy.pop_call()
                            jump Campus_Map
                        else:
                            ch_r "Well if you don't mind, I'm getting out of here. Maybe knock next time?"
                            call Remove_Girl(RogueX)
                return                      #returns to sexmenu, which returns to original
    #End of "Join" option



    if Situation == RogueX:                                                                  #Rogue auto-starts
                if Approval > 2:                                                      # fix, add rogue auto stuff here
                        if RogueX.PantsNum() == 5:
                            "[RogueX.Name]'s hand snakes down her body, and hikes up her skirt."
                            $ RogueX.Upskirt = 1
                        elif RogueX.PantsNum() > 6:
                            "[RogueX.Name] slides her hand down her body and into her jeans."
                        elif RogueX.HoseNum() >= 5:
                            "[RogueX.Name]'s hand slides down her body and under her [RogueX.Hose]."
                        elif RogueX.Panties:
                            "[RogueX.Name]'s hand slides down her body and under her [RogueX.Panties]."
                        else:
                            "[RogueX.Name]'s hand slides down her body and begins to caress her pussy."
                        $ RogueX.SeenPanties = 1
                        "She starts to slowly rub herself."
                        call Rogue_First_Bottomless
                        menu:
                            "What do you do?"
                            "Nothing.":
                                    $ RogueX.Statup("Inbt", 80, 3)
                                    $ RogueX.Statup("Inbt", 60, 2)
                                    "[RogueX.Name] begins to masturbate."
                            "Go for it.":
                                    $ RogueX.FaceChange("sexy, 1")
                                    $ RogueX.Statup("Inbt", 80, 3)
                                    ch_p "That is so sexy, [RogueX.Pet]."
                                    $ RogueX.NameCheck() #checks reaction to petname
                                    "You lean back and enjoy the show."
                                    $ RogueX.Statup("Love", 80, 1)
                                    $ RogueX.Statup("Obed", 90, 1)
                                    $ RogueX.Statup("Obed", 50, 2)
                            "Ask her to stop.":
                                    $ RogueX.FaceChange("surprised")
                                    $ RogueX.Statup("Inbt", 70, 1)
                                    ch_p "Let's not do that right now, [RogueX.Pet]."
                                    $ RogueX.NameCheck() #checks reaction to petname
                                    "[RogueX.Name] pulls her hands away from herself."
                                    $ RogueX.OutfitChange(Changed=0)
                                    $ RogueX.Statup("Obed", 90, 1)
                                    $ RogueX.Statup("Obed", 50, 1)
                                    $ RogueX.Statup("Obed", 30, 2)
                                    return
                        jump Rogue_M_Prep
                else:
                        $ temp_modifier = 0                               # fix, add rogue auto stuff here
                        $ Trigger2 = 0
                return
    #End if Rogue intitiates this action

    #first time
    if not RogueX.Mast:
            $ RogueX.FaceChange("surprised", 1)
            $ RogueX.Mouth = "kiss"
            ch_r "You want me to get myself off, while you watch?"
            if RogueX.Forced:
                $ RogueX.FaceChange("sad")
                ch_r "So you just want to watch then?"


    #First time dialog
    if not RogueX.Mast and Approval:
            if RogueX.Forced:
                $ RogueX.FaceChange("sad")
                $ RogueX.Statup("Love", 70, -3, 1)
                $ RogueX.Statup("Love", 20, -2, 1)
            elif RogueX.Love >= (RogueX.Obed + RogueX.Inbt):
                $ RogueX.FaceChange("sexy")
                $ RogueX.Brows = "sad"
                $ RogueX.Mouth = "smile"
                ch_r "Since my love life's been a bit. . . limited, I've gotten pretty good at this."
            elif RogueX.Obed >= RogueX.Inbt:
                $ RogueX.FaceChange("normal")
                ch_r "If that's what you want, [RogueX.Petname]. . ."
            else: # Uninhibited
                $ RogueX.FaceChange("sad")
                $ RogueX.Mouth = "smile"
                ch_r "I guess it could be fun with you watching. . ."


    #Second time+ initial dialog
    elif Approval:
            if RogueX.Forced:
                $ RogueX.FaceChange("sad")
                $ RogueX.Statup("Love", 70, -3, 1)
                $ RogueX.Statup("Love", 20, -2, 1)
                ch_r "You want to watch me again?"
            elif Approval and "masturbation" in RogueX.RecentActions:
                $ RogueX.FaceChange("sexy", 1)
                ch_r "I guess I have a bit more in me. . ."
                jump Rogue_M_Prep
            elif Approval and "masturbation" in RogueX.DailyActions:
                $ RogueX.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["You enjoyed the show?",
                    "Didn't get enough earlier?",
                    "It is nice to have an audience. . ."])
                ch_r "[Line]"
            elif RogueX.Mast < 3:
                $ RogueX.FaceChange("sexy", 1)
                $ RogueX.Brows = "confused"
                ch_r "You like to watch, huh?"
            else:
                $ RogueX.FaceChange("sexy", 1)
                $ RogueX.ArmPose = 2
                $ Line = renpy.random.choice(["You sure do like to watch.",
                    "So you'd like me to go again?",
                    "You want to watch some more?",
                    "You want me ta diddle myself?"])
                ch_r "[Line]"
                $ Line = 0
    #End second time+ initial dialog

    #If she's into it. . .
    if Approval >= 2:
            if RogueX.Forced:
                $ RogueX.FaceChange("sad")
                $ RogueX.Statup("Obed", 90, 1)
                $ RogueX.Statup("Inbt", 60, 1)
                ch_r "I suppose, let me get comfortable. . ."
            else:
                $ RogueX.FaceChange("sexy", 1)
                $ RogueX.Statup("Love", 90, 1)
                $ RogueX.Statup("Inbt", 50, 3)
                $ Line = renpy.random.choice(["Well. . . ok.",
                    "I suppose it would help to have something nice to look at. . .",
                    "I've kind of needed this anyways. . .",
                    "Sure!",
                    "I guess I could. . . give it a go.",
                    "Heh, ok, ok."])
                ch_r "[Line]"
                $ Line = 0
            $ RogueX.Statup("Obed", 20, 1)
            $ RogueX.Statup("Obed", 60, 1)
            $ RogueX.Statup("Inbt", 70, 2)
            jump Rogue_M_Prep

    #If she's not into it, but maybe. . .
    else:
        menu:
            ch_r "That's. . . a little intimate, [RogueX.Petname]."
            "Maybe later?":
                    $ RogueX.FaceChange("sexy", 1)
                    if RogueX.Lust > 50:
                        ch_r "Well, definitely later. . . but I'll have to think about inviting you."
                    else:
                        ch_r "Hmm, maybe. . . I'll let you know."
                    $ RogueX.Statup("Love", 80, 2)
                    $ RogueX.Statup("Inbt", 70, 2)
                    return
            "You look like you could use it. . .":
                    if Approval:
                        $ RogueX.FaceChange("sexy")
                        $ RogueX.Statup("Obed", 90, 2)
                        $ RogueX.Statup("Obed", 50, 2)
                        $ RogueX.Statup("Inbt", 70, 3)
                        $ RogueX.Statup("Inbt", 40, 2)
                        $ Line = renpy.random.choice(["Well. . . ok.",
                            "I suppose it would help to have something nice to look at. . .",
                            "I've kind of needed this anyways. . .",
                            "Sure!",
                            "I guess I could. . . give it a go.",
                            "Heh, ok, ok."])
                        ch_r "[Line]"
                        $ Line = 0
                        jump Rogue_M_Prep

            "Just get at it already.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(RogueX, 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                    if Approval > 1 or (Approval and RogueX.Forced):
                        $ RogueX.FaceChange("sad")
                        $ RogueX.Statup("Love", 70, -5, 1)
                        $ RogueX.Statup("Love", 200, -5)
                        ch_r "Ok, fine. I'll give it a try."
                        $ RogueX.Statup("Obed", 80, 4)
                        $ RogueX.Statup("Inbt", 80, 1)
                        $ RogueX.Statup("Inbt", 60, 3)
                        $ RogueX.Forced = 1
                        jump Rogue_M_Prep
                    else:
                        $ RogueX.Statup("Love", 200, -20)
                        $ RogueX.RecentActions.append("angry")
                        $ RogueX.DailyActions.append("angry")
    # end of asking her to do it

    #She refused all offers.
    $ RogueX.ArmPose = 1
    if RogueX.Forced:
            $ RogueX.FaceChange("angry", 1)
            ch_r "I'm not doing something so. . . intimate with you watching."
            $ RogueX.Statup("Lust", 90, 5)
            if RogueX.Love > 300:
                $ RogueX.Statup("Love", 70, -2)
            $ RogueX.Statup("Obed", 50, -2)
            $ RogueX.RecentActions.append("angry")
            $ RogueX.DailyActions.append("angry")
            $ RogueX.RecentActions.append("no masturbation")
            $ RogueX.DailyActions.append("no masturbation")
            return
    elif Taboo:                             # she refuses and this is too public a place for her
            $ RogueX.FaceChange("angry", 1)
            $ RogueX.DailyActions.append("tabno")
            ch_r "I can't do that here!"
            $ RogueX.Statup("Lust", 90, 5)
            $ RogueX.Statup("Obed", 50, -3)
            return
    elif RogueX.Mast:
            $ RogueX.FaceChange("sad")
            ch_r "Nope, not anymore, you'll have to go back to Internet porn."
    else:
            $ RogueX.FaceChange("normal", 1)
            ch_r "Heh, no, I'm not doing that."
    $ RogueX.RecentActions.append("no masturbation")
    $ RogueX.DailyActions.append("no masturbation")
    $ temp_modifier = 0
    return

label Rogue_M_Prep:
    $ RogueX.Upskirt = 1
    $ RogueX.PantiesDown = 1
    call Rogue_First_Bottomless(1)
    call Set_The_Scene(Dress=0)

    #if she hasn't seen you yet. . .
    if "unseen" in RogueX.RecentActions:
            $ RogueX.FaceChange("sexy")
            $ RogueX.Eyes = "closed"
            $ RogueX.ArmPose = 2
            "You see [RogueX.Name] leaning back, masturbating. You don't think she's noticed you yet."
    else:
            $ RogueX.FaceChange("sexy")
            $ RogueX.ArmPose = 2
            "[RogueX.Name] lays back and starts to toy with herself."
            if not RogueX.Mast:#First time
                    if RogueX.Forced:
                        $ RogueX.Statup("Love", 90, -20)
                        $ RogueX.Statup("Obed", 70, 45)
                        $ RogueX.Statup("Inbt", 80, 35)
                    else:
                        $ RogueX.Statup("Love", 90, 15)
                        $ RogueX.Statup("Obed", 70, 35)
                        $ RogueX.Statup("Inbt", 80, 40)


    $ Trigger = "masturbation"
    if not Trigger3:
        $ Trigger3 = "fondle pussy"

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    if Taboo:
        $ RogueX.DrainWord("tabno")
    $ RogueX.DrainWord("no masturbation")
    $ RogueX.RecentActions.append("masturbation")
    $ RogueX.DailyActions.append("masturbation")

label Rogue_M_Cycle:
    if Situation == "join":
        # resets the call made to this option
        $ renpy.pop_call()
        $ Situation = 0

    while Round > 0:
        call Rogue_Pos_Reset("masturbation")
        call Shift_Focus(RogueX)
        $ RogueX.LustFace
        if "unseen" in RogueX.RecentActions:
                $ RogueX.Eyes = "closed"

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep Watching.":
                                pass

                        "[RogueX.Name]. . .[[jump in]" if "unseen" not in RogueX.RecentActions and "join" not in Player.RecentActions and RogueX.Loc == bg_current:
                                "[RogueX.Name] slows what she's doing with a sly grin."
                                ch_r "Yeah, did you want something, [RogueX.Petname]?"
                                $ Situation = "join"
                                call Rogue_Masturbate
                        "\"Ahem. . .\"" if "unseen" in RogueX.RecentActions:
                                jump Rogue_M_Interupted

                        "Start jack'in it." if Trigger2 != "jackin":
                                call Jackin(RogueX)
                        "Stop jack'in it." if Trigger2 == "jackin":
                                $ Trigger2 = 0

                        "Slap her ass" if RogueX.Loc == bg_current:
                                if "unseen" in RogueX.RecentActions:
                                        "You smack [RogueX.Name] firmly on the ass!"
                                        jump Rogue_M_Interupted
                                else:
                                        call Slap_Ass(RogueX)
                                        $ Cnt += 1
                                        $ Round -= 1
                                        jump Rogue_M_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0

                        "Change what I'm doing":
                                menu:
                                    "Offhand action" if RogueX.Loc == bg_current:
                                            if RogueX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ RogueX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(RogueX,"tired")

                                    "Threesome actions (locked)" if not Partner or "unseen" in RogueX.RecentActions or RogueX.Loc == bg_current:
                                        pass
                                    "Threesome actions" if RogueX.Loc == bg_current and Partner and "unseen" not in RogueX.RecentActions:
                                        menu:
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(RogueX)
                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(RogueX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Rogue_M_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Rogue_M_Cycle
                                            "Never mind":
                                                        jump Rogue_M_Cycle

                                    "Show her feet" if not ShowFeet and (RogueX.Pose == "doggy" or RogueX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (RogueX.Pose == "doggy" or RogueX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [RogueX.Name]":
                                            if "unseen" in RogueX.RecentActions:
                                                    ch_p "Oh, yeah, take it off. . ."
                                                    jump Rogue_M_Interupted
                                            else:
                                                    call Girl_Undress(RogueX)
                                    "Clean up [RogueX.Name] (locked)" if not RogueX.Spunk:
                                            pass
                                    "Clean up [RogueX.Name]" if RogueX.Spunk:
                                            if "unseen" in RogueX.RecentActions:
                                                    ch_p "You've got a little something on you. . ."
                                                    jump Rogue_M_Interupted
                                            else:
                                                    call Girl_Cleanup(RogueX,"ask")
                                    "Never mind":
                                            jump Rogue_M_Cycle

                        "Back to Sex Menu" if MultiAction and RogueX.Loc == bg_current:
                                    ch_p "Let's try something else."
                                    call Rogue_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Rogue_M_Interupted
                        "End Scene" if not MultiAction or RogueX.Loc != bg_current:
                                    ch_p "Let's stop for now."
                                    call Rogue_Pos_Reset
                                    $ Line = 0
                                    jump Rogue_M_Interupted
        #End menu (if Line)

        call Shift_Focus(RogueX)
        call Sex_Dialog(RogueX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up

        if Player.Focus >= 100 or RogueX.Lust >= 100:
                    #If you can cum:
                    if Player.Focus >= 100:
                        if "unseen" not in RogueX.RecentActions:
                            #if she knows you're there
                            call Player_Cumming(RogueX)
                            if "angry" in RogueX.RecentActions:
                                call Rogue_Pos_Reset
                                return
                            $ RogueX.Statup("Lust", 200, 5)
                            if 100 > RogueX.Lust >= 70 and RogueX.OCount < 2:
                                $ RogueX.RecentActions.append("unsatisfied")
                                $ RogueX.DailyActions.append("unsatisfied")
                            $ Line = "came"
                        else: #If she wasn't aware you were there
                            "You grunt and try to hold it in."
                            $ Player.Focus = 95
                            if RogueX.Loc == bg_current:
                                    jump Rogue_M_Interupted

                    #If Rogue can cum
                    if RogueX.Lust >= 100:
                        call Girl_Cumming(RogueX)
                        if RogueX.Loc == bg_current:
                                jump Rogue_M_Interupted

                    if Line == "came":
                        $ Line = 0
                        if not Player.Semen:
                            "You're emptied out, you should probably take a break."
                            $ Trigger2 = 0 if Trigger2 == "jackin" else Trigger2


                        if "unsatisfied" in RogueX.RecentActions:#And Rogue is unsatisfied,
                            "[RogueX.Name] still seems a bit unsatisfied with the experience."
                            menu:
                                "Let her keep going?"
                                "Yes, keep going for a bit.":
                                    $ Line = "You let her get back into it"
                                    jump Rogue_M_Cycle
                                "No, I'm done.":
                                    "You ask her to stop."
                                    return
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        if "unseen" in RogueX.RecentActions:
                if Round == 10:
                    "It's getting a bit late, [RogueX.Name] will probably be wrapping up soon."
                elif Round == 5:
                    "She's definitely going to stop soon."
        else:
                if RogueX.Loc == bg_current:
                        call Escalation(RogueX) #sees if she wants to escalate things

                if Round == 10:
                    ch_r "We might want to wrap this up, it's getting late."
                    $ RogueX.Lust += 10
                elif Round == 5:
                    ch_r "Seriously, it'll be time to stop soon."
                    $ RogueX.Lust += 25

    #Round = 0 loop breaks
    $ RogueX.FaceChange("bemused", 0)
    $ Line = 0
    if "unseen" not in RogueX.RecentActions:
        ch_r "Ok, [RogueX.Petname], that's enough of that for now."

label Rogue_M_Interupted:

    # If she hasn't noticed you're there before cumming
    if "unseen" in RogueX.RecentActions:
                $ RogueX.FaceChange("surprised", 1)
                "[RogueX.Name] stops what she's doing with a start, eyes wide."
                call Rogue_First_Bottomless(1)
                $ RogueX.FaceChange("surprised", 1)

                #If you've been jacking it
                if Trigger2 == "jackin":
                        ch_r "H- how long you been stand'in there, [RogueX.Petname]?"
                        $ RogueX.Eyes = "down"
                        menu:
                            ch_r "And why is your cock out like that?!"
                            "Long enough, it was an excellent show.":
                                    $ RogueX.FaceChange("sexy")
                                    $ RogueX.Statup("Obed", 50, 3)
                                    $ RogueX.Statup("Obed", 70, 2)
                                    ch_r "Well, I imagine it was. . ."
                                    if RogueX.Love >= 800 or RogueX.Obed >= 500 or RogueX.Inbt >= 500:
                                        $ temp_modifier += 10
                                        $ RogueX.Statup("Lust", 90, 5)
                                        ch_r "And the view from this angle ain't so bad either. . ."

                            "I. . . just got here?":
                                    $ RogueX.FaceChange("angry")
                                    $ RogueX.Statup("Love", 70, 2)
                                    $ RogueX.Statup("Love", 90, 1)
                                    $ RogueX.Statup("Obed", 50, 2)
                                    $ RogueX.Statup("Obed", 70, 2)
                                    "She looks pointedly at your cock,"
                                    ch_r "A likely story . . ."
                                    if RogueX.Love >= 800 or RogueX.Obed >= 500 or RogueX.Inbt >= 500:
                                            $ temp_modifier += 10
                                            $ RogueX.Statup("Lust", 90, 5)
                                            $ RogueX.FaceChange("bemused", 1)
                                            ch_r "Still, can't blame a fella for take'in inspirations."
                                    else:
                                            $ temp_modifier -= 10
                                            $ RogueX.Statup("Lust", 200, -5)
                        call Seen_First_Peen(RogueX,Partner)
                        ch_r "Hmm. . ."

                #you haven't been jacking it
                else:
                        ch_r "H- how long you been stand'in there, [RogueX.Petname]?"
                        menu:
                            extend ""
                            "Long enough.":
                                    $ RogueX.FaceChange("sexy", 1)
                                    $ RogueX.Statup("Obed", 50, 3)
                                    $ RogueX.Statup("Obed", 70, 2)
                                    ch_r "Well I hope you got a good show out of it. . ."
                            "I just got here.":
                                    $ RogueX.FaceChange("bemused", 1)
                                    $ RogueX.Statup("Love", 70, 2)
                                    $ RogueX.Statup("Love", 90, 1)
                                    ch_r "A likely story . . ."
                                    $ RogueX.Statup("Obed", 50, 2)
                                    $ RogueX.Statup("Obed", 70, 2)

                $ RogueX.DrainWord("unseen",1,0) #She sees you, so remove unseens
                $ RogueX.Mast += 1
                if Round <= 10:
                    ch_r "It's getting too late to do much about it right now though."
                    return
                $ Situation = "join"
                call Rogue_Masturbate
                "error: report this if you see it."
                return #should be redundant
    #End Unseen

    #else, if She's seen you already
    $ RogueX.Action -= 1
    $ RogueX.Mast += 1

    if Partner == EmmaX:
        call Partner_Like(RogueX,4)
    else:
        call Partner_Like(RogueX,3)
    call Checkout
    if Situation == "shift":
        $ Situation = 0
        return
    $ Situation = 0

    if RogueX.Loc != bg_current:
        return

    if Round <= 10:
            ch_r "I need to take a little break here, [RogueX.Petname]."
            return
    $ RogueX.FaceChange("sexy", 1)
    if RogueX.Lust < 20:
        ch_r "That really worked for me, [RogueX.Petname]. How about you?"
    else:
        ch_r "Yeah, what did you want?"
    menu:
        extend ""
        "Well, I have something you could take care of. . ." if Player.Semen and RogueX.Action:
                $ Situation = "shift"
                return
        "You could just keep going. . ." if Player.Semen:
                $ RogueX.FaceChange("sly")
                if RogueX.Action and Round >= 10:
                    ch_r "Well, alright. . ."
                    jump Rogue_M_Cycle
                else:
                    ch_r "I'm kinda worn out, maybe time for a break. . ."
        "I'm good here. [[Stop]":
                if RogueX.Love < 800 and RogueX.Inbt < 500 and RogueX.Obed < 500:
                    $ RogueX.OutfitChange(Changed=0)
                $ RogueX.FaceChange("normal")
                $ RogueX.Brows = "confused"
                ch_r "Well. . . ok then. . ."
                $ RogueX.Brows = "normal"
        "You should probably stop for now." if RogueX.Lust > 30:
                $ RogueX.FaceChange("angry")
                ch_r "Well if you say so."
    return

label Rogue_Sex_P:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(RogueX)
    if RogueX.Sex >= 7: # She loves it
        $ temp_modifier += 15
    elif RogueX.Sex >= 3: #You've done it before several times
        $ temp_modifier += 12
    elif RogueX.Sex: #You've done it before
        $ temp_modifier += 10

    if RogueX.Addict >= 75 and (RogueX.CreamP + RogueX.CreamA) >=3: #She's really strung out and has creampied
        $ temp_modifier += 20
    elif RogueX.Addict >= 75:
        $ temp_modifier += 15

    if RogueX.Lust > 85:
        $ temp_modifier += 10
    elif RogueX.Lust > 75: #She's really horny
        $ temp_modifier += 5

    if Situation == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in RogueX.Traits:
        $ temp_modifier += (4*Taboo)
    if RogueX in Player.Harem or "sex friend" in RogueX.Petnames:
        $ temp_modifier += 10
    elif "ex" in RogueX.Traits:
        $ temp_modifier -= 40
    if RogueX.ForcedCount and not RogueX.Forced:
        $ temp_modifier -= 5 * RogueX.ForcedCount



    if Taboo and "tabno" in RogueX.DailyActions:
        $ temp_modifier -= 10

    if "no sex" in RogueX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no sex" in RogueX.RecentActions else 0


    $ Approval = ApprovalCheck(RogueX, 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)

    if Situation == "auto":
        $ RogueX.Pose = "doggy"
        call Rogue_Sex_Launch("sex")
        if RogueX.PantsNum() == 5:
            "You press up against [RogueX.Name]'s backside, sliding her skirt up as you go."
            $ RogueX.Upskirt = 1
        elif RogueX.PantsNum() > 6:
            "You press up against [RogueX.Name]'s backside, sliding her pants down as you do."
            $ RogueX.Legs = 0
        else:
            "You press up against [RogueX.Name]'s backside."
        $ RogueX.SeenPanties = 1
        "You rub the tip of your cock against her moist slit."
        $ RogueX.FaceChange("surprised", 1)

        if (RogueX.Sex and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
            "[RogueX.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            $ RogueX.FaceChange("sexy")
            $ RogueX.Statup("Obed", 70, 3)
            $ RogueX.Statup("Inbt", 50, 3)
            $ RogueX.Statup("Inbt", 70, 1)
            ch_r "Ok, [RogueX.Petname], let's do this."
            call sex_prep(RogueX)
        else:                                                                                                            #she's questioning it
            $ RogueX.Brows = "angry"
            menu:
                ch_r "Hey, what do you think you're doing back there?!"
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ RogueX.FaceChange("sexy", 1)
                        $ RogueX.Statup("Obed", 70, 3)
                        $ RogueX.Statup("Inbt", 50, 3)
                        $ RogueX.Statup("Inbt", 70, 1)
                        ch_r "Well, since you're be'in so nice about it, I guess we can give it a go. . ."
                        call sex_prep(RogueX)
                    "You pull back before you really get it in."
                    $ RogueX.FaceChange("bemused", 1)
                    if RogueX.Sex:
                        ch_r "Well ok, [RogueX.Petname], no harm done. Just give me a little warning next time."
                    else:
                        ch_r "Well ok, [RogueX.Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."
                "Just fucking.":
                    $ RogueX.Statup("Love", 80, -10, 1)
                    $ RogueX.Statup("Love", 200, -10)
                    "You press inside some more."
                    $ RogueX.Statup("Obed", 70, 3)
                    $ RogueX.Statup("Inbt", 50, 3)
                    if not ApprovalCheck(RogueX, 700, "O", TabM=1):   #Checks if Obed is 700+
                        $ RogueX.FaceChange("angry")
                        "[RogueX.Name] shoves you away and slaps you in the face."
                        ch_r "Jackass!"
                        ch_r "If that's how you want to treat me, we're done here!"
                        $ RogueX.Statup("Love", 50, -10, 1)
                        $ RogueX.Statup("Obed", 50, 3)
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Rogue_Sex_Reset
                        $ RogueX.RecentActions.append("angry")
                        $ RogueX.DailyActions.append("angry")
                    else:
                        $ RogueX.FaceChange("sad")
                        "[RogueX.Name] doesn't seem to be into this, you're lucky she's so obedient."
                        call sex_prep(RogueX)
        return


    if not RogueX.Sex and "no sex" not in RogueX.RecentActions:                           #first time
        $ RogueX.FaceChange("surprised", 1)
        $ RogueX.Mouth = "kiss"
        ch_r "So, you'd like to take this to the next level? Actual sex? . . ."
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            ch_r "You'd really take it that far?"


    if not RogueX.Sex and Approval:                                                  #First time dialog
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Love", 70, -30, 1)
            $ RogueX.Statup("Love", 20, -20, 1)
        elif RogueX.Love >= (RogueX.Obed + RogueX.Inbt):
            $ RogueX.FaceChange("sexy")
            $ RogueX.Brows = "sad"
            $ RogueX.Mouth = "smile"
            ch_r "Well, I've never been able to do this before now, so this might be fun."
        elif RogueX.Obed >= RogueX.Inbt:
            $ RogueX.FaceChange("normal")
            ch_r "If that's what you want, [RogueX.Petname]. . ."
        elif RogueX.Addict >= 50:
            $ RogueX.FaceChange("manic", 1)
            ch_r "Well. . . I bet it would feel really good down there."
        else: # Uninhibited
            $ RogueX.FaceChange("sad")
            $ RogueX.Mouth = "smile"
            ch_r "Hmm, I've always wanted to try it. . ."

    elif Approval:                                                                       #Second time+ dialog
        $ RogueX.FaceChange("sexy", 1)
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Love", 70, -3, 1)
            $ RogueX.Statup("Love", 20, -2, 1)
            ch_r "That's really what you want?"
        elif not Taboo and "tabno" in RogueX.DailyActions:
            ch_r "Well, at least you got us some privacy this time. . ."
        elif "sex" in RogueX.RecentActions:
            ch_r "You want to go again? Ok."
            call sex_prep(RogueX)
        elif "sex" in RogueX.DailyActions:
            $ Line = renpy.random.choice(["Back again so soon?",
                "So you'd like another go?",
                "You can't stay away from this. . .",
                "Didn't get enough earlier?",
                "You're going to wear me out."])
            ch_r "[Line]"
        elif RogueX.Sex < 3:
            $ RogueX.Brows = "confused"
            $ RogueX.Mouth = "kiss"
            ch_r "So you'd like another go?"
        else:
            $ Line = renpy.random.choice(["You want some of this action?",
                "So you'd like another go?",
                "You can't stay away from this. . .",
                "You want me to ride your pole?",
                "You wanna dip your wick?"])
            ch_r "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Obed", 90, 1)
            $ RogueX.Statup("Inbt", 60, 1)
            ch_r "Ok, fine."
        elif "no sex" in RogueX.DailyActions:
            ch_r "Ok, you've won me over on this one. . ."
        else:
            $ RogueX.FaceChange("sexy", 1)
            $ RogueX.Statup("Love", 90, 1)
            $ RogueX.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, stick it in.",
                "Well. . . ok.",
                "Sure!",
                "I guess I could. . . stick it in.",
                "Hells yeah.",
                "Heh, ok, ok."])
            ch_r "[Line]"
            $ Line = 0
        $ RogueX.Statup("Obed", 20, 1)
        $ RogueX.Statup("Obed", 60, 1)
        $ RogueX.Statup("Inbt", 70, 2)
        call sex_prep(RogueX)

    else:                                                                               #She's not into it, but maybe. . .
        $ RogueX.FaceChange("angry")
        if "no sex" in RogueX.RecentActions:
            ch_r "I {i}just{/i} told you \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions and "no sex" in RogueX.DailyActions:
            ch_r "I already told you that I wouldn't bang you in public!"
        elif "no sex" in RogueX.DailyActions:
            ch_r "I already told you \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions:
            ch_r "I already told you this is too public!"
        elif not RogueX.Sex:
            $ RogueX.FaceChange("bemused")
            ch_r "I just don't think I'm ready yet, [RogueX.Petname]. . ."
        else:
            $ RogueX.FaceChange("bemused")
            ch_r "Not, right now [RogueX.Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no sex" in RogueX.DailyActions:
                $ RogueX.FaceChange("bemused")
                ch_r "Yeah, ok, [RogueX.Petname]."
                return
            "Maybe later?" if "no sex" not in RogueX.DailyActions:
                $ RogueX.FaceChange("sexy")
                ch_r "I'll give it some thought, [RogueX.Petname]."
                $ RogueX.Statup("Love", 80, 2)
                $ RogueX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ RogueX.RecentActions.append("tabno")
                    $ RogueX.DailyActions.append("tabno")
                $ RogueX.RecentActions.append("no sex")
                $ RogueX.DailyActions.append("no sex")
                return
            "I think you'd enjoy it as much as I would. . .":
                if Approval:
                    $ RogueX.FaceChange("sexy")
                    $ RogueX.Statup("Obed", 90, 2)
                    $ RogueX.Statup("Obed", 50, 2)
                    $ RogueX.Statup("Inbt", 70, 3)
                    $ RogueX.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",
                        "I suppose. . .",
                        "You've got me there."])
                    ch_r "[Line]"
                    $ Line = 0
                    call sex_prep(RogueX)
            "Bend over.":                                               # Pressured into it
                $ Approval = ApprovalCheck(RogueX, 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.FaceChange("sad")
                    $ RogueX.Statup("Love", 70, -5, 1)
                    $ RogueX.Statup("Love", 200, -5)
                    ch_r "Ok, fine. If we're going to do this, stick it in already."
                    $ RogueX.Statup("Obed", 80, 4)
                    $ RogueX.Statup("Inbt", 80, 1)
                    $ RogueX.Statup("Inbt", 60, 3)
                    $ RogueX.Forced = 1
                    call sex_prep(RogueX)
                else:
                    $ RogueX.Statup("Love", 200, -20)
                    $ RogueX.RecentActions.append("angry")
                    $ RogueX.DailyActions.append("angry")

    #She refused all offers.
    $ RogueX.ArmPose = 1
    if "no sex" in RogueX.DailyActions:
        ch_r "Learn to take \"no\" for an answer, [RogueX.Petname]."
        $ RogueX.RecentActions.append("angry")
        $ RogueX.DailyActions.append("angry")
    elif RogueX.Forced:
        $ RogueX.FaceChange("angry", 1)
        ch_r "I'm not doing that just because you have me over a barrel."
        $ RogueX.Statup("Lust", 200, 5)
        if RogueX.Love > 300:
                $ RogueX.Statup("Love", 70, -2)
        $ RogueX.Statup("Obed", 50, -2)
        $ RogueX.RecentActions.append("angry")
        $ RogueX.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ RogueX.FaceChange("angry", 1)
        $ RogueX.RecentActions.append("tabno")
        $ RogueX.DailyActions.append("tabno")
        ch_r "Even if I wanted to, it certainly wouldn't be here!"
        $ RogueX.Statup("Lust", 200, 5)
        $ RogueX.Statup("Obed", 50, -3)
    elif RogueX.Sex:
        $ RogueX.FaceChange("sad")
        ch_r "Maybe you could go fuck yourself instead."
    else:
        $ RogueX.FaceChange("normal", 1)
        ch_r "No way."
    $ RogueX.RecentActions.append("no sex")
    $ RogueX.DailyActions.append("no sex")
    $ temp_modifier = 0
    return


label Rogue_Sex_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(RogueX)
        call Rogue_Sex_Launch("sex")
        $ RogueX.LustFace()
        $ Player.Cock = "in"
        $ Trigger = "sex"

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass
                        "Keep going. . . (locked)" if not Speed:
                                    pass

                        "Start moving? . ." if not Speed:
                                    $ Speed = 1
                        "Speed up. . ." if 0 < Speed < 3:
                                    $ Speed += 1
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 3:
                                    pass

                        "Slow Down. . ." if Speed:
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(RogueX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Rogue_Sex_Cycle

                        "Turn her Around":
                                    $ RogueX.Pose = "doggy" if RogueX.Pose != "doggy" else "sex"
                                    "You turn her around. . ."
                                    jump Rogue_Sex_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if RogueX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ RogueX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(RogueX,"tired")

                                    "Shift primary action":
                                            if RogueX.Action and MultiAction:
                                                    menu:
                                                        "How about anal?":
                                                                $ Situation = "shift"
                                                                call sex_after(RogueX)
                                                                call Rogue_Sex_A
                                                        "Just stick it in her ass [[without asking].":
                                                                $ Situation = "auto"
                                                                call sex_after(RogueX)
                                                                call Rogue_Sex_A
                                                        "Pull back to hotdog her.":
                                                                $ Situation = "pullback"
                                                                call sex_after(RogueX)
                                                                call Rogue_Sex_H
                                                        "Never Mind":
                                                                jump Rogue_Sex_Cycle
                                            else:
                                                call Sex_Basic_Dialog(RogueX,"tired")
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [RogueX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(RogueX)
                                            "Ask [RogueX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(RogueX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(RogueX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Rogue_Sex_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Rogue_Sex_Cycle
                                            "Never mind":
                                                        jump Rogue_Sex_Cycle
                                    "Just take a look at her.":
                                            $ Player.Cock = 0
                                            $ Speed = 0

                                    "Show her feet" if not ShowFeet and (RogueX.Pose == "doggy" or RogueX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (RogueX.Pose == "doggy" or RogueX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [RogueX.Name]":
                                            call Girl_Undress(RogueX)
                                    "Clean up [RogueX.Name] (locked)" if not RogueX.Spunk:
                                            pass
                                    "Clean up [RogueX.Name]" if RogueX.Spunk:
                                            call Girl_Cleanup(RogueX,"ask")
                                    "Never mind":
                                            jump Rogue_Sex_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Rogue_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    call sex_after(RogueX)
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Rogue_Sex_Reset
                                    $ Line = 0
                                    call sex_after(RogueX)
        #End menu (if Line)

        call Shift_Focus(RogueX)
        call Sex_Dialog(RogueX,Partner)

        $ Cnt += 1
        $ Round -= 1
        $ Player.Wet = 1 #wets penis
        $ Player.Spunk = 0 if (Player.Spunk and "in" not in RogueX.Spunk) else Player.Spunk #cleans you off after one cycle

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or RogueX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(RogueX)
                            if "angry" in RogueX.RecentActions:
                                call Rogue_Sex_Reset
                                return
                            $ RogueX.Statup("Lust", 200, 5)
                            if 100 > RogueX.Lust >= 70 and RogueX.OCount < 2:
                                    $ RogueX.RecentActions.append("unsatisfied")
                                    $ RogueX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                call sex_after(RogueX)
                            $ Line = "came"

                    if RogueX.Lust >= 100:
                            #If you're still going at it and Rogue can cum
                            call Girl_Cumming(RogueX)
                            if Situation == "shift" or "angry" in RogueX.RecentActions:
                                call sex_after(RogueX)

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                call sex_after(RogueX)
                            elif "unsatisfied" in RogueX.RecentActions:
                                #And Rogue is unsatisfied,
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ Line = "You get back into it"
                                        jump Rogue_Sex_Cycle
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        call sex_after(RogueX)
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        call sex_after(RogueX)
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif Cnt == (5 + RogueX.Sex):
                    $ RogueX.Brows = "confused"
                    ch_r "Are you getting close here? I'm getting as little sore."
        elif Cnt == (10 + RogueX.Sex):
                    $ RogueX.Brows = "angry"
                    ch_r "I'm . . .getting . . .worn out. . . here, . . [RogueX.Petname]."
                    menu:
                        ch_r "Can we. . . do something. . . else?"
                        "How about a BJ?" if RogueX.Action and MultiAction:
                                $ Situation = "shift"
                                call sex_after(RogueX)
                                call Rogue_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                jump Rogue_Sex_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Rogue_Sex_Reset
                                $ Situation = "shift"
                                call sex_after(RogueX)
                        "No, get back down there.":
                                if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):
                                    $ RogueX.Statup("Love", 200, -5)
                                    $ RogueX.Statup("Obed", 50, 3)
                                    $ RogueX.Statup("Obed", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    $ RogueX.FaceChange("angry", 1)
                                    call Rogue_Sex_Reset
                                    "She scowls at you and pulls out."
                                    ch_r "Well if that's your attitude you can handle your own business."
                                    $ RogueX.Statup("Love", 50, -3, 1)
                                    $ RogueX.Statup("Love", 80, -4, 1)
                                    $ RogueX.Statup("Obed", 30, -1, 1)
                                    $ RogueX.Statup("Obed", 50, -1, 1)
                                    $ RogueX.RecentActions.append("angry")
                                    $ RogueX.DailyActions.append("angry")
                                    call sex_after(RogueX)
        #End Count check

        call Escalation(RogueX) #sees if she wants to escalate things

        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ RogueX.FaceChange("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.Petname], that's enough of that for now."


label Rogue_Sex_A:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(RogueX)
    if RogueX.Anal >= 7: # She loves it
        $ temp_modifier += 20
    elif RogueX.Anal >= 3: #You've done it before several times
        $ temp_modifier += 17
    elif RogueX.Anal: #You've done it before
        $ temp_modifier += 15

    if RogueX.Addict >= 75 and (RogueX.CreamP + RogueX.CreamA) >=3: #She's really strung out and has creampied
        $ temp_modifier += 25
    elif RogueX.Addict >= 75:
        $ temp_modifier += 15

    if RogueX.Lust > 85:
        $ temp_modifier += 10
    elif RogueX.Lust > 75: #She's really horny
        $ temp_modifier += 5

    if RogueX.Loose:
        $ temp_modifier += 10
    elif "anal" in RogueX.RecentActions:
        $ temp_modifier -= 20
    elif "anal" in RogueX.DailyActions:
        $ temp_modifier -= 10

    if Situation == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in RogueX.Traits:
        $ temp_modifier += (5*Taboo)

    if RogueX in Player.Harem or "sex friend" in RogueX.Petnames:
        $ temp_modifier += 10
    elif "ex" in RogueX.Traits:
        $ temp_modifier -= 40
    if RogueX.ForcedCount and not RogueX.Forced:
        $ temp_modifier -= 5 * RogueX.ForcedCount

    if Taboo and "tabno" in RogueX.DailyActions:
        $ temp_modifier -= 10
    if "no anal" in RogueX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no anal" in RogueX.RecentActions else 0

    $ Approval = ApprovalCheck(RogueX, 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)

    if Situation == "auto":
        $ RogueX.Pose = "doggy"
        call Rogue_Sex_Launch("anal")
        if RogueX.PantsNum() == 5:
            "You press up against [RogueX.Name]'s backside, sliding her skirt up as you go."
            $ RogueX.Upskirt = 1
        elif RogueX.PantsNum() > 6:
            "You press up against [RogueX.Name]'s backside, sliding her pants down as you do."
            $ RogueX.Legs = 0
        else:
            "You press up against [RogueX.Name]'s backside."
        $ RogueX.SeenPanties = 1
        "You press the tip of your cock against her tight rim."
        $ RogueX.FaceChange("surprised", 1)

        if (RogueX.Anal and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
            "[RogueX.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            $ RogueX.FaceChange("sexy")
            $ RogueX.Statup("Obed", 70, 3)
            $ RogueX.Statup("Inbt", 50, 3)
            $ RogueX.Statup("Inbt", 70, 1)
            ch_r "Hmm, stick it in. . ."
            call anal_prep(RogueX)
        else:                                                                                                            #she's questioning it
            $ RogueX.Brows = "angry"
            menu:
                ch_r "Hey, what do you think you're doing back there?!"
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ RogueX.FaceChange("sexy", 1)
                        $ RogueX.Statup("Obed", 70, 3)
                        $ RogueX.Statup("Inbt", 50, 3)
                        $ RogueX.Statup("Inbt", 70, 1)
                        ch_r "I guess if you really want to try it. . ."
                        call anal_prep(RogueX)
                    "You pull back before you really get it in."
                    $ RogueX.FaceChange("bemused", 1)
                    if RogueX.Anal:
                        ch_r "Well ok, [RogueX.Petname], no harm done. Just give me a little warning next time."
                    else:
                        ch_r "Well ok, [RogueX.Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."
                "Just fucking.":
                    $ RogueX.Statup("Love", 80, -10, 1)
                    $ RogueX.Statup("Love", 200, -8)
                    "You press into her."
                    $ RogueX.Statup("Obed", 70, 3)
                    $ RogueX.Statup("Inbt", 50, 3)
                    if not ApprovalCheck(RogueX, 700, "O", TabM=1):
                        $ RogueX.FaceChange("angry")
                        "[RogueX.Name] shoves you away and slaps you in the face."
                        ch_r "Jackass!"
                        ch_r "If that's how you want to treat me, we're done here!"
                        $ RogueX.Statup("Love", 50, -10, 1)
                        $ RogueX.Statup("Obed", 50, 3)
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Rogue_Sex_Reset
                        $ RogueX.RecentActions.append("angry")
                        $ RogueX.DailyActions.append("angry")
                    else:
                        $ RogueX.FaceChange("sad")
                        "[RogueX.Name] doesn't seem to be into this, you're lucky she's so obedient."
                        call anal_prep(RogueX)
        return


    if not RogueX.Anal and "no anal" not in RogueX.RecentActions:                                                               #first time
        $ RogueX.FaceChange("surprised", 1)
        $ RogueX.Mouth = "kiss"
        ch_r "Wait, so you want to stick it in my butt?!"

        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            ch_r "Seriously?"

    if not RogueX.Loose and ("dildo anal" in RogueX.DailyActions or "anal" in RogueX.DailyActions):
        $ RogueX.FaceChange("bemused", 1)
        ch_r "I'm still a little sore from earlier."

    elif "anal" in RogueX.RecentActions:
        $ RogueX.FaceChange("sexy", 1)
        ch_r "You want to go again? Ok."
        call anal_prep(RogueX)


    if not RogueX.Anal and Approval:                                                 #First time dialog
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Love", 70, -3, 1)
            $ RogueX.Statup("Love", 20, -2, 1)
        elif RogueX.Love >= (RogueX.Obed + RogueX.Inbt):
            $ RogueX.FaceChange("sexy")
            $ RogueX.Brows = "sad"
            $ RogueX.Mouth = "smile"
            ch_r "I guess if you really want to try it. . ."
        elif RogueX.Obed >= RogueX.Inbt:
            $ RogueX.FaceChange("normal")
            ch_r "Ok, [RogueX.Petname], I'm ready."
        elif RogueX.Addict >= 50:
            $ RogueX.FaceChange("manic", 1)
            ch_r "Well. . . I bet it would feel really good down there."
        else: # Uninhibited
            $ RogueX.FaceChange("sad")
            $ RogueX.Mouth = "smile"
            ch_r "Hmm, it has been on my list. . ."

    elif Approval:                                                                       #Second time+ dialog
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Love", 70, -3, 1)
            $ RogueX.Statup("Love", 20, -2, 1)
            ch_r "That's really what you want?"
        elif not Taboo and "tabno" in RogueX.DailyActions:
            ch_r "Well, at least you got us some privacy this time. . ."
        elif "anal" in RogueX.DailyActions and not RogueX.Loose:
            pass
        elif "anal" in RogueX.RecentActions:
            ch_r "I think I'm warmed up. . ."
            call anal_prep(RogueX)
        elif "anal" in RogueX.DailyActions:
            $ RogueX.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",
                "So you'd like another go?",
                "I'm still a little sore from earlier.",
                "Didn't get enough earlier?",
                "You're going to wear me out."])
            ch_r "[Line]"
        elif RogueX.Anal < 3:
            $ RogueX.FaceChange("sexy", 1)
            $ RogueX.Brows = "confused"
            $ RogueX.Mouth = "kiss"
            ch_r "So you'd like another go?"
        else:
            $ RogueX.FaceChange("sexy", 1)
            $ RogueX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action?",
                "So you'd like another go?",
                "You can't stay away from this booty.",
                "You want me to ride your pole?",
                "You wanna dip your wick?"])
            ch_r "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Obed", 90, 1)
            $ RogueX.Statup("Inbt", 60, 1)
            ch_r "Ok, fine."
        elif "no anal" in RogueX.DailyActions:
            ch_r "Ok, ok, I have been itching for this. . ."
        else:
            $ RogueX.FaceChange("sexy", 1)
            $ RogueX.Statup("Love", 90, 1)
            $ RogueX.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, stick it in.",
                "Well. . . ok.",
                "Sure!",
                "I guess I could. . . stick it in.",
                "Hells yeah.",
                "Heh, ok, ok."])
            ch_r "[Line]"
            $ Line = 0
        $ RogueX.Statup("Obed", 20, 1)
        $ RogueX.Statup("Obed", 60, 1)
        $ RogueX.Statup("Inbt", 70, 2)
        call anal_prep(RogueX)

    else:                                                                               #She's not into it, but maybe. . .
        $ RogueX.FaceChange("angry")
        if "no anal" in RogueX.RecentActions:
            ch_r "What part of \"no,\" did you not get, [RogueX.Petname]?"
        elif Taboo and "tabno" in RogueX.DailyActions and "no anal" in RogueX.DailyActions:
            ch_r "I already told you that I wouldn't do that out here!"
        elif "no anal" in RogueX.DailyActions:
            ch_r "I already told you \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions:
            ch_r "I already told you that I wouldn't do that out here!"
        elif not RogueX.Anal:
            $ RogueX.FaceChange("bemused")
            ch_r "I'm just not into that, [RogueX.Petname]. . ."
        elif not RogueX.Loose and "anal" not in RogueX.DailyActions:
            $ RogueX.FaceChange("perplexed")
            ch_r "You could have been a bit more gentle last time, [RogueX.Petname]. . ."
        else:
            $ RogueX.FaceChange("bemused")
            ch_r "Not, right now [RogueX.Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no anal" in RogueX.DailyActions:
                $ RogueX.FaceChange("bemused")
                ch_r "Yeah, ok, [RogueX.Petname]."
                return
            "Maybe later?" if "no anal" not in RogueX.DailyActions:
                $ RogueX.FaceChange("sexy")
                ch_r "I'll give it some thought, [RogueX.Petname]."
                $ RogueX.Statup("Love", 80, 2)
                $ RogueX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ RogueX.RecentActions.append("tabno")
                    $ RogueX.DailyActions.append("tabno")
                $ RogueX.RecentActions.append("no anal")
                $ RogueX.DailyActions.append("no anal")
                return
            "I bet it would feel really good. . .":
                if Approval:
                    $ RogueX.FaceChange("sexy")
                    $ RogueX.Statup("Obed", 90, 2)
                    $ RogueX.Statup("Obed", 50, 2)
                    $ RogueX.Statup("Inbt", 70, 3)
                    $ RogueX.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",
                        "I suppose. . .",
                        "You've got me there."])
                    ch_r "[Line]"
                    $ Line = 0
                    call anal_prep(RogueX)
                else:
                    pass

            "Bend over.":                                               # Pressured into it
                $ Approval = ApprovalCheck(RogueX, 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.FaceChange("sad")
                    $ RogueX.Statup("Love", 70, -5, 1)
                    $ RogueX.Statup("Love", 200, -5)
                    ch_r "Ok, fine. If we're going to do this, stick it in already."
                    $ RogueX.Statup("Obed", 80, 4)
                    $ RogueX.Statup("Inbt", 80, 1)
                    $ RogueX.Statup("Inbt", 60, 3)
                    $ RogueX.Forced = 1
                    call anal_prep(RogueX)
                else:
                    $ RogueX.Statup("Love", 200, -20)
                    $ RogueX.RecentActions.append("angry")
                    $ RogueX.DailyActions.append("angry")

    #She refused all offers.
    $ RogueX.ArmPose = 1
    if "no anal" in RogueX.DailyActions:
        ch_r "Learn to take \"no\" for an answer, [RogueX.Petname]."
        $ RogueX.RecentActions.append("angry")
        $ RogueX.DailyActions.append("angry")
    elif RogueX.Forced:
        $ RogueX.FaceChange("angry", 1)
        ch_r "That's a bit much, even for you."
        $ RogueX.Statup("Lust", 200, 5)
        if RogueX.Love > 300:
                $ RogueX.Statup("Love", 70, -2)
        $ RogueX.Statup("Obed", 50, -2)
        $ RogueX.RecentActions.append("angry")
        $ RogueX.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ RogueX.FaceChange("angry", 1)
        $ RogueX.RecentActions.append("tabno")
        $ RogueX.DailyActions.append("tabno")
        ch_r "That you would even suggest such a thing in a place like this. . ."
        $ RogueX.Statup("Lust", 200, 5)
        $ RogueX.Statup("Obed", 50, -3)
    elif not RogueX.Loose and "anal" in RogueX.DailyActions:
        $ RogueX.FaceChange("bemused")
        ch_r "Sorry, I just need a little break back there, [RogueX.Petname]."
    elif RogueX.Anal:
        $ RogueX.FaceChange("sad")
        ch_r "The only thing you can do with my ass is kiss it, [RogueX.Petname]."
        ch_r ". . .Don't get any ideas."
    else:
        $ RogueX.FaceChange("normal", 1)
        ch_r "Not happening."
    $ RogueX.RecentActions.append("no anal")
    $ RogueX.DailyActions.append("no anal")
    $ temp_modifier = 0
    return

label Rogue_Anal_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(RogueX)
        call Rogue_Sex_Launch("anal")
        $ RogueX.LustFace()
        $ Player.Cock = "anal"
        $ Trigger = "anal"

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass
                        "Keep going. . . (locked)" if not Speed:
                                    pass

                        "Start moving? . ." if not Speed:
                                    $ Speed = 1
                        "Speed up. . ." if 0 < Speed < 3:
                                    $ Speed += 1
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 3:
                                    pass

                        "Slow Down. . ." if Speed:
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(RogueX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Rogue_Anal_Cycle

                        "Turn her Around":
                                    $ RogueX.Pose = "doggy" if RogueX.Pose != "doggy" else "sex"
                                    "You turn her around. . ."
                                    jump Rogue_Anal_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if RogueX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ RogueX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(RogueX,"tired")

                                    "Shift primary action":
                                            if RogueX.Action and MultiAction:
                                                    menu:
                                                        "How about sex?":
                                                                $ Situation = "shift"
                                                                call anal_after(RogueX)
                                                                call Rogue_Sex_P
                                                        "Just stick it in her pussy [[without asking].":
                                                                $ Situation = "auto"
                                                                call anal_after(RogueX)
                                                                call Rogue_Sex_P
                                                        "Pull back to hotdog her.":
                                                                $ Situation = "pullback"
                                                                call anal_after(RogueX)
                                                                call Rogue_Sex_H
                                                        "Never Mind":
                                                                jump Rogue_Anal_Cycle
                                            else:
                                                call Sex_Basic_Dialog(RogueX,"tired")
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [RogueX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(RogueX)
                                            "Ask [RogueX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(RogueX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(RogueX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Rogue_Anal_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Rogue_Anal_Cycle
                                            "Never mind":
                                                        jump Rogue_Anal_Cycle
                                    "Just take a look at her.":
                                            $ Player.Cock = 0
                                            $ Speed = 0

                                    "Show her feet" if not ShowFeet and (RogueX.Pose == "doggy" or RogueX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (RogueX.Pose == "doggy" or RogueX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [RogueX.Name]":
                                            call Girl_Undress(RogueX)
                                    "Clean up [RogueX.Name] (locked)" if not RogueX.Spunk:
                                            pass
                                    "Clean up [RogueX.Name]" if RogueX.Spunk:
                                            call Girl_Cleanup(RogueX,"ask")
                                    "Never mind":
                                            jump Rogue_Anal_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Rogue_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    call anal_after(RogueX)
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Rogue_Sex_Reset
                                    $ Line = 0
                                    call anal_after(RogueX)
        #End menu (if Line)

        call Shift_Focus(RogueX)
        call Sex_Dialog(RogueX,Partner)

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or RogueX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(RogueX)
                            if "angry" in RogueX.RecentActions:
                                call Rogue_Sex_Reset
                                return
                            $ RogueX.Statup("Lust", 200, 5)
                            if 100 > RogueX.Lust >= 70 and RogueX.OCount < 2:
                                    $ RogueX.RecentActions.append("unsatisfied")
                                    $ RogueX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                call anal_after(RogueX)
                            $ Line = "came"

                    if RogueX.Lust >= 100:
                            #If you're still going at it and Rogue can cum
                            call Girl_Cumming(RogueX)
                            if Situation == "shift" or "angry" in RogueX.RecentActions:
                                call anal_after(RogueX)

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                call anal_after(RogueX)
                            elif "unsatisfied" in RogueX.RecentActions:
                                #And Rogue is unsatisfied,
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ Line = "You get back into it"
                                        jump Rogue_Anal_Cycle
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        call anal_after(RogueX)
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        call anal_after(RogueX)
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif Cnt == (5 + RogueX.Anal):
                    $ RogueX.Brows = "confused"
                    ch_r "Are you getting close here? I'm getting as little sore."
        elif Cnt == (10 + RogueX.Anal):
                    $ RogueX.Brows = "angry"
                    ch_r "I'm . . .getting . . .worn out. . . here, . . [RogueX.Petname]."
                    menu:
                        ch_r "Can we. . . do something. . . else?"
                        "How about a BJ?" if RogueX.Action and MultiAction:
                                if RogueX.Anal >= 5 and RogueX.Blow >= 10 and RogueX.SEXP >= 50:
                                    $ Situation = "shift"
                                    call anal_after(RogueX)
                                    call Rogue_Blowjob
                                else:
                                    ch_r "No thanks, [RogueX.Petname]. Maybe a Handy instead?"
                                    $ Situation = "shift"
                                    call anal_after(RogueX)
                                    call Rogue_HJ_Prep
                        "How about a Handy?" if RogueX.Action and MultiAction:
                                $ Situation = "shift"
                                call anal_after(RogueX)
                                call Rogue_Handjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                jump Rogue_Anal_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Rogue_Sex_Reset
                                $ Situation = "shift"
                                call anal_after(RogueX)
                        "No, get back down there.":
                                if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):
                                    $ RogueX.Statup("Love", 200, -5)
                                    $ RogueX.Statup("Obed", 50, 3)
                                    $ RogueX.Statup("Obed", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    $ RogueX.FaceChange("angry", 1)
                                    call Rogue_Sex_Reset
                                    "She scowls at you and pulls out."
                                    ch_r "Well if that's your attitude you can handle your own business."
                                    $ RogueX.Statup("Love", 50, -3, 1)
                                    $ RogueX.Statup("Love", 80, -4, 1)
                                    $ RogueX.Statup("Obed", 30, -1, 1)
                                    $ RogueX.Statup("Obed", 50, -1, 1)
                                    $ RogueX.RecentActions.append("angry")
                                    $ RogueX.DailyActions.append("angry")
                                    call anal_after(RogueX)
        #End Count check

        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ RogueX.FaceChange("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.Petname], that's enough of that for now."


label Rogue_Sex_H:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(RogueX)
    if RogueX.Hotdog >= 3: #You've done it before several times
        $ temp_modifier += 10
    elif RogueX.Hotdog: #You've done it before
        $ temp_modifier += 5

    if RogueX.Lust > 85:
        $ temp_modifier += 10
    elif RogueX.Lust > 75: #She's really horny
        $ temp_modifier += 5
    if Situation == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in RogueX.Traits:
        $ temp_modifier += (3*Taboo)
    if RogueX in Player.Harem or "sex friend" in RogueX.Petnames:
        $ temp_modifier += 10
    elif "ex" in RogueX.Traits:
        $ temp_modifier -= 40
    if RogueX.ForcedCount and not RogueX.Forced:
        $ temp_modifier -= 5 * RogueX.ForcedCount

    if Taboo and "tabno" in RogueX.DailyActions:
        $ temp_modifier -= 10

    if "no hotdog" in RogueX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no hotdog" in RogueX.RecentActions else 0

    $ Approval = ApprovalCheck(RogueX, 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)

    if Situation == "auto":
        $ RogueX.Pose = "doggy"
        call Rogue_Sex_Launch("hotdog")
        "You press up against [RogueX.Name]'s backside."
        $ RogueX.FaceChange("surprised", 1)

        if (RogueX.Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
            "[RogueX.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            $ RogueX.FaceChange("sexy")
            $ RogueX.Statup("Obed", 70, 3)
            $ RogueX.Statup("Inbt", 50, 3)
            $ RogueX.Statup("Inbt", 70, 1)
            ch_r "Hmm, I've apparently got someone's attention. . ."
            call hotdog_prep(RogueX)
        else:                                                                                                            #she's questioning it
            $ RogueX.Brows = "angry"
            menu:
                ch_r "Hmm, kinda rude, [RogueX.Petname]."
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ RogueX.FaceChange("sexy", 1)
                        $ RogueX.Statup("Obed", 70, 3)
                        $ RogueX.Statup("Inbt", 50, 3)
                        $ RogueX.Statup("Inbt", 70, 1)
                        ch_r "I guess it doesn't feel so bad. . ."
                        call hotdog_prep(RogueX)
                    "You pull back before you really get it in."
                    $ RogueX.FaceChange("bemused", 1)
                    if RogueX.Hotdog:
                        ch_r "Well ok, [RogueX.Petname], it has been kinda fun."
                    else:
                        ch_r "Well ok, [RogueX.Petname], that's a bit dirty, maybe ask a girl?"
                "You'll see.":
                    $ RogueX.Statup("Love", 80, -10, 1)
                    $ RogueX.Statup("Love", 200, -8)
                    "You grind against her asscrack."
                    $ RogueX.Statup("Obed", 70, 3)
                    $ RogueX.Statup("Inbt", 50, 3)
                    if not ApprovalCheck(RogueX, 500, "O", TabM=1): #Checks if Obed is 700+
                        $ RogueX.FaceChange("angry")
                        "[RogueX.Name] shoves you away."
                        ch_r "Dick!"
                        ch_r "If that's how you want want to act, I'm out of here!"
                        $ RogueX.Statup("Love", 50, -10, 1)
                        $ RogueX.Statup("Obed", 50, 3)
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Rogue_Sex_Reset
                        $ RogueX.RecentActions.append("angry")
                        $ RogueX.DailyActions.append("angry")
                    else:
                        $ RogueX.FaceChange("sad")
                        "[RogueX.Name] doesn't seem to be into this, but she knows her place."
                        call hotdog_prep(RogueX)
        return


    if not RogueX.Hotdog and "no hotdog" not in RogueX.RecentActions:                                                               #first time
        $ RogueX.FaceChange("surprised", 1)
        $ RogueX.Mouth = "kiss"
        ch_r "Wait, so you want to grind against my butt?!"

        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            ch_r ". . . That's all?"


    if not RogueX.Hotdog and Approval:                                                 #First time dialog
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Love", 70, -3, 1)
            $ RogueX.Statup("Love", 20, -2, 1)
        elif RogueX.Love >= (RogueX.Obed + RogueX.Inbt):
            $ RogueX.FaceChange("sexy")
            $ RogueX.Brows = "sad"
            $ RogueX.Mouth = "smile"
            ch_r "It looks like you need some relief. . ."
        elif RogueX.Obed >= RogueX.Inbt:
            $ RogueX.FaceChange("normal")
            ch_r "If that's what you need, [RogueX.Petname]."
        elif RogueX.Addict >= 50:
            $ RogueX.FaceChange("manic", 1)
            ch_r "Hmmm. . ."
        else: # Uninhibited
            $ RogueX.FaceChange("sad")
            $ RogueX.Mouth = "smile"
            ch_r "Hmm, you look ready for it, at least. . ."

    elif Approval:                                                                       #Second time+ dialog
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Love", 70, -3, 1)
            $ RogueX.Statup("Love", 20, -2, 1)
            ch_r "That's all you want?"
        elif not Taboo and "tabno" in RogueX.DailyActions:
            ch_r "Well, at least you got us some privacy this time. . ."
        elif "hotdog" in RogueX.RecentActions:
            $ RogueX.FaceChange("sexy", 1)
            ch_r "You want to go again? Ok."
            call hotdog_prep(RogueX)
        elif "hotdog" in RogueX.DailyActions:
            $ RogueX.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",
                "So you'd like another go?",
                "You can't stay away from this booty. . .",
                "Are you sure that's all you want?"])
            ch_r "[Line]"
        elif RogueX.Hotdog < 3:
            $ RogueX.FaceChange("sexy", 1)
            $ RogueX.Brows = "confused"
            $ RogueX.Mouth = "kiss"
            ch_r "So you'd like another go?"
        else:
            $ RogueX.FaceChange("sexy", 1)
            $ RogueX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action?",
                "So you'd like another go?",
                "You can't stay away from this booty.",
                "You want me to slick your pole?"])
            ch_r "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Obed", 80, 1)
            $ RogueX.Statup("Inbt", 60, 1)
            ch_r "Ok, fine."
        elif "no hotdog" in RogueX.DailyActions:
            ch_r "Well, I guess it's not so bad. . ."
        else:
            $ RogueX.FaceChange("sexy", 1)
            $ RogueX.Statup("Love", 80, 1)
            $ RogueX.Statup("Inbt", 50, 2)
            $ Line = renpy.random.choice(["Well, sure, give it a rub.",
                "Well. . . ok.",
                "Sure!",
                "I guess we could do that.",
                "Hells yeah.",
                "Heh, ok, ok."])
            ch_r "[Line]"
            $ Line = 0
        $ RogueX.Statup("Obed", 60, 1)
        $ RogueX.Statup("Inbt", 70, 2)
        call hotdog_prep(RogueX)

    else:                                                                               #She's not into it, but maybe. . .
        $ RogueX.FaceChange("angry")
        if "no hotdog" in RogueX.RecentActions:
            ch_r "I {i}just{/i} told you \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions and "no hotdog" in RogueX.DailyActions:
            ch_r "I told you that I didn't want you rubb'in up on me in public!"
        elif "no hotdog" in RogueX.DailyActions:
            ch_r "I told you \"no\" earlier, [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions:
            ch_r "I told you that I didn't want you rubb'in up on me in public!"
        elif not RogueX.Hotdog:
            $ RogueX.FaceChange("bemused")
            ch_r "That's kinda naughty, [RogueX.Petname]. . ."
        else:
            $ RogueX.FaceChange("bemused")
            ch_r "Not, right now [RogueX.Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no hotdog" in RogueX.DailyActions:
                $ RogueX.FaceChange("bemused")
                ch_r "Yeah, ok, [RogueX.Petname]."
                return
            "Maybe later?" if "no hotdog" not in RogueX.DailyActions:
                $ RogueX.FaceChange("sexy")
                ch_r "Yeah, maybe, [RogueX.Petname]."
                $ RogueX.Statup("Love", 80, 1)
                $ RogueX.Statup("Inbt", 50, 1)
                if Taboo:
                    $ RogueX.RecentActions.append("tabno")
                    $ RogueX.DailyActions.append("tabno")
                $ RogueX.RecentActions.append("no hotdog")
                $ RogueX.DailyActions.append("no hotdog")
                return
            "You might like it. . .":
                if Approval:
                    $ RogueX.FaceChange("sexy")
                    $ RogueX.Statup("Obed", 60, 2)
                    $ RogueX.Statup("Inbt", 50, 2)
                    $ Line = renpy.random.choice(["Well, sure, give it a rub.",
                        "I suppose. . .",
                        "You've got me there."])
                    ch_r "[Line]"
                    $ Line = 0
                    call hotdog_prep(RogueX)
                else:
                    pass

            "Bend over.":                                               # Pressured into it
                $ Approval = ApprovalCheck(RogueX, 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.FaceChange("sad")
                    $ RogueX.Statup("Love", 70, -2, 1)
                    $ RogueX.Statup("Love", 200, -2)
                    ch_r "Ok, fine. Whatever."
                    $ RogueX.Statup("Obed", 80, 4)
                    $ RogueX.Statup("Inbt", 60, 2)
                    $ RogueX.Forced = 1
                    call hotdog_prep(RogueX)
                else:
                    $ RogueX.Statup("Love", 200, -10)
                    $ RogueX.RecentActions.append("angry")
                    $ RogueX.DailyActions.append("angry")

    #She refused all offers.
    $ RogueX.ArmPose = 1

    if "no hotdog" in RogueX.DailyActions:
        ch_r "I just don't want to, [RogueX.Petname]."
        $ RogueX.RecentActions.append("angry")
        $ RogueX.DailyActions.append("angry")
    if RogueX.Forced:
        $ RogueX.FaceChange("angry", 1)
        ch_r "Even that's not worth it."
        $ RogueX.Statup("Lust", 200, 5)
        if RogueX.Love > 300:
                $ RogueX.Statup("Love", 70, -1)
        $ RogueX.Statup("Obed", 50, -1)
        $ RogueX.RecentActions.append("angry")
        $ RogueX.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ RogueX.FaceChange("angry", 1)
        $ RogueX.RecentActions.append("tabno")
        $ RogueX.DailyActions.append("tabno")
        ch_r "I'd be a bit embarassed doing that here."
        $ RogueX.Statup("Lust", 200, 5)
        $ RogueX.Statup("Obed", 50, -3)
    elif RogueX.Hotdog:
        $ RogueX.FaceChange("sad")
        ch_r "Eh-eh, not anymore, [RogueX.Petname]."
    else:
        $ RogueX.FaceChange("normal", 1)
        ch_r "Not interested."
    $ RogueX.RecentActions.append("no hotdog")
    $ RogueX.DailyActions.append("no hotdog")
    $ temp_modifier = 0
    return

label Rogue_Hotdog_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(RogueX)
        call Rogue_Sex_Launch("hotdog")
        $ RogueX.LustFace()
        if Speed:
                $ Player.Cock = "out"
        $ Trigger = "hotdog"

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass
                        "Keep going. . . (locked)" if not Speed:
                                    pass

                        "Start moving? . ." if not Speed:
                                    $ Speed = 1
                        "Speed up. . ." if 0 < Speed < 3:
                                    $ Speed += 1
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 3:
                                    pass

                        "Slow Down. . ." if Speed:
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(RogueX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Rogue_Hotdog_Cycle

                        "Turn her Around":
                                    $ RogueX.Pose = "doggy" if RogueX.Pose != "doggy" else "sex"
                                    "You turn her around. . ."
                                    jump Rogue_Hotdog_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if RogueX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ RogueX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(RogueX,"tired")

                                    "Shift primary action":
                                            if RogueX.Action and MultiAction:
                                                    menu:
                                                        "How about sex?":
                                                            $ Situation = "shift"
                                                            call hotdog_after(RogueX)
                                                            call Rogue_Sex_P
                                                        "Just stick it in her pussy [[without asking].":
                                                            $ Situation = "auto"
                                                            call hotdog_after(RogueX)
                                                            call Rogue_Sex_P
                                                        "How about anal?":
                                                            $ Situation = "shift"
                                                            call hotdog_after(RogueX)
                                                            call Rogue_Sex_A
                                                        "Just stick it in her ass [[without asking].":
                                                            $ Situation = "auto"
                                                            call hotdog_after(RogueX)
                                                            call Rogue_Sex_A
                                                        "Never Mind":
                                                                jump Rogue_Hotdog_Cycle
                                            else:
                                                call Sex_Basic_Dialog(RogueX,"tired")
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [RogueX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(RogueX)
                                            "Ask [RogueX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(RogueX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(RogueX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Rogue_Hotdog_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Rogue_Hotdog_Cycle
                                            "Never mind":
                                                        jump Rogue_Hotdog_Cycle
                                    "Just take a look at her.":
                                            $ Player.Cock = 0
                                            $ Speed = 0

                                    "Show her feet" if not ShowFeet and (RogueX.Pose == "doggy" or RogueX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (RogueX.Pose == "doggy" or RogueX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [RogueX.Name]":
                                            call Girl_Undress(RogueX)
                                    "Clean up [RogueX.Name] (locked)" if not RogueX.Spunk:
                                            pass
                                    "Clean up [RogueX.Name]" if RogueX.Spunk:
                                            call Girl_Cleanup(RogueX,"ask")
                                    "Never mind":
                                            jump Rogue_Hotdog_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Rogue_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    call hotdog_after(RogueX)
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Rogue_Sex_Reset
                                    $ Line = 0
                                    call hotdog_after(RogueX)
        #End menu (if Line)

        call Shift_Focus(RogueX)
        call Sex_Dialog(RogueX,Partner)

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or RogueX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(RogueX)
                            if "angry" in RogueX.RecentActions:
                                call Rogue_Sex_Reset
                                return
                            $ RogueX.Statup("Lust", 200, 5)
                            if 100 > RogueX.Lust >= 70 and RogueX.OCount < 2:
                                    $ RogueX.RecentActions.append("unsatisfied")
                                    $ RogueX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                call hotdog_after(RogueX)
                            $ Line = "came"

                    if RogueX.Lust >= 100:
                            #If you're still going at it and Rogue can cum
                            call Girl_Cumming(RogueX)
                            if Situation == "shift" or "angry" in RogueX.RecentActions:
                                call hotdog_after(RogueX)

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                call hotdog_after(RogueX)
                            elif "unsatisfied" in RogueX.RecentActions:
                                #And Rogue is unsatisfied,
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ Line = "You get back into it"
                                        jump Rogue_Hotdog_Cycle
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        call hotdog_after(RogueX)
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        call hotdog_after(RogueX)
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif Cnt == (5 + RogueX.Hotdog):
                    $ RogueX.Brows = "confused"
                    ch_r "Are you getting close here?"
        elif Cnt == (10 + RogueX.Hotdog):
                    $ RogueX.Brows = "angry"
                    menu:
                        ch_r "I'm kinda done with this, [RogueX.Petname]."
                        "How about a BJ?" if RogueX.Action and MultiAction:
                                $ Situation = "shift"
                                call hotdog_after(RogueX)
                                call Rogue_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                jump Rogue_Hotdog_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Rogue_Sex_Reset
                                $ Situation = "shift"
                                call hotdog_after(RogueX)
                        "No, get back down there.":
                                if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):
                                    $ RogueX.Statup("Love", 200, -5)
                                    $ RogueX.Statup("Obed", 50, 3)
                                    $ RogueX.Statup("Obed", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    $ RogueX.FaceChange("angry", 1)
                                    call Rogue_Sex_Reset
                                    "She scowls at you and pulls away."
                                    ch_r "Well if that's your attitude you can handle your own business."
                                    $ RogueX.Statup("Love", 50, -3, 1)
                                    $ RogueX.Statup("Love", 80, -4, 1)
                                    $ RogueX.Statup("Obed", 30, -1, 1)
                                    $ RogueX.Statup("Obed", 50, -1, 1)
                                    $ RogueX.RecentActions.append("angry")
                                    $ RogueX.DailyActions.append("angry")
                                    call hotdog_after(RogueX)
        #End Count check

        call Escalation(RogueX) #sees if she wants to escalate things

        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ RogueX.FaceChange("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.Petname], that's enough of that for now."


image AssBase:                  #This is the base image, used in masks
    "images/RogueDoggy/Rogue_Doggy_Ass.png"

image Dildo_Animation:
    contains:
        "UI_Dildo"
        block:
            ease 1 pos (100,300) #pos (0,50)
            ease 1 pos (100,400) #pos (0,0)
            repeat

image AssTest:
#    "Dildo_Animation"
    AlphaMask("Dildo_Animation", "AssBase")
