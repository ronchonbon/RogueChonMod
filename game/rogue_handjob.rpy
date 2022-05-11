## RogueX.Handjob //////////////////////////////////////////////////////////////////////
label Rogue_Handjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(RogueX)
    if RogueX.Hand >= 7: # She loves it
        $ temp_modifier += 10
    elif RogueX.Hand >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif RogueX.Hand: #You've done it before
        $ temp_modifier += 3

    if RogueX.Addict >= 75 and RogueX.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 15
    if RogueX.Addict >= 75:
        $ temp_modifier += 5

    if Situation == "shift":
        $ temp_modifier += 15
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
        
    if "no hand" in RogueX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no hand" in RogueX.RecentActions else 0

    $ Approval = ApprovalCheck(RogueX, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if not RogueX.Hand and "no hand" not in RogueX.RecentActions:
        $ RogueX.FaceChange("surprised", 1)
        $ RogueX.Mouth = "kiss"
        ch_r "You want me to rub your cock, with my hand?"

    if not RogueX.Hand and Approval:                                                 #First time dialog
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Love", 70, -3, 1)
            $ RogueX.Statup("Love", 20, -2, 1)
        elif RogueX.Love >= (RogueX.Obed + RogueX.Inbt):
            $ RogueX.FaceChange("sexy")
            $ RogueX.Brows = "sad"
            $ RogueX.Mouth = "smile"
            ch_r "Well, I've never really been able to touch people without draining them, this could be an interesting experience. . ."
        elif RogueX.Obed >= RogueX.Inbt:
            $ RogueX.FaceChange("normal")
            ch_r "If that's what you want, [RogueX.Petname]. . ."
        elif RogueX.Addict >= 50:
            $ RogueX.FaceChange("manic", 1)
            ch_r "I think, if I could just touch that. . ."
        else: # Uninhibited
            $ RogueX.FaceChange("sad")
            $ RogueX.Mouth = "smile"
            ch_r "Hmm, could be fun. . ."

    elif Approval:                                                                       #Second time+ dialog
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Love", 70, -3, 1)
            $ RogueX.Statup("Love", 20, -2, 1)
            ch_r "That's really what you want?"
        elif not Taboo and "tabno" in RogueX.DailyActions:
            ch_r "Ok, I guess this is private enough. . ."
        elif "hand" in RogueX.RecentActions:
            $ RogueX.FaceChange("sexy", 1)
            ch_r "Mmm, again? Let me flex my hand a bit. . ."
            jump Rogue_HJ_Prep
        elif "hand" in RogueX.DailyActions:
            $ RogueX.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",
                "You're going to give me calluses.",
                "Didn't get enough earlier?",
                "My arm's still a bit sore from earlier.",
                "My arm's still a bit sore from earlier."])
            ch_r "[Line]"
        elif RogueX.Hand < 3:
            $ RogueX.FaceChange("sexy", 1)
            $ RogueX.Brows = "confused"
            $ RogueX.Mouth = "kiss"
            ch_r "So you'd like another handy?"
        else:
            $ RogueX.FaceChange("sexy", 1)
            $ RogueX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action?",
                "So you'd like another handy?",
                "A little. . . [fist pumping hand gestures]?",
                "You want me to grease your skids?",
                "A little tender loving care?"])
            ch_r "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Obed", 90, 1)
            $ RogueX.Statup("Inbt", 60, 1)
            ch_r "Ok, fine."
        elif "no hand" in RogueX.DailyActions:
            ch_r "I guess if it'll get you off. . ."
        else:
            $ RogueX.FaceChange("sexy", 1)
            $ RogueX.Statup("Love", 90, 1)
            $ RogueX.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, put'im here.",
                "Well. . . ok.",
                "I suppose, drop trou.",
                "I guess I could. . . whip it out.",
                "Fine. . . [She gestures for you to come over].",
                "Heh, ok, ok."])
            ch_r "[Line]"
            $ Line = 0
        $ RogueX.Statup("Obed", 20, 1)
        $ RogueX.Statup("Obed", 60, 1)
        $ RogueX.Statup("Inbt", 70, 2)
        jump Rogue_HJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ RogueX.FaceChange("angry")
        if "no hand" in RogueX.RecentActions:
            ch_r "I {i}just{/i} told you \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions and "no hand" in RogueX.DailyActions:
            ch_r "I already told you that I wouldn't jerk you off in public!"
        elif "no hand" in RogueX.DailyActions:
            ch_r "I already told you \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions:
            ch_r "I already told you this is too public!"
        elif not RogueX.Hand:
            $ RogueX.FaceChange("bemused")
            ch_r "I don't really want to touch it, [RogueX.Petname]. . ."
        else:
            $ RogueX.FaceChange("bemused")
            ch_r "Not, right now [RogueX.Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no hand" in RogueX.DailyActions:
                $ RogueX.FaceChange("bemused")
                ch_r "Fine."
                return
            "Maybe later?" if "no hand" not in RogueX.DailyActions:
                $ RogueX.FaceChange("sexy")
                ch_r "I'll give it some thought, [RogueX.Petname]."
                $ RogueX.Statup("Love", 80, 2)
                $ RogueX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ RogueX.RecentActions.append("tabno")
                    $ RogueX.DailyActions.append("tabno")
                $ RogueX.RecentActions.append("no hand")
                $ RogueX.DailyActions.append("no hand")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ RogueX.FaceChange("sexy")
                    $ RogueX.Statup("Obed", 90, 2)
                    $ RogueX.Statup("Obed", 50, 2)
                    $ RogueX.Statup("Inbt", 70, 3)
                    $ RogueX.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Sure, put'im here.",
                        "No Problem.",
                        "Sure. Drop trou.",
                        "I suppose, whip it out.",
                        "Ok, [She gestures for you to come over].",
                        "Heh, ok."])
                    ch_r "[Line]"
                    $ Line = 0
                    jump Rogue_HJ_Prep
                else:
                    pass

            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck(RogueX, 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.FaceChange("sad")
                    $ RogueX.Statup("Love", 70, -5, 1)
                    $ RogueX.Statup("Love", 200, -2)
                    ch_r "Ok, fine, whip it out."
                    $ RogueX.Statup("Obed", 50, 4)
                    $ RogueX.Statup("Inbt", 80, 1)
                    $ RogueX.Statup("Inbt", 60, 3)
                    $ RogueX.Forced = 1
                    jump Rogue_HJ_Prep
                else:
                    $ RogueX.Statup("Love", 200, -15)
                    $ RogueX.RecentActions.append("angry")
                    $ RogueX.DailyActions.append("angry")

    #She refused all offers.
    $ RogueX.ArmPose = 1
    if "no hand" in RogueX.DailyActions:
        $ RogueX.FaceChange("angry", 1)
        ch_r "I just don't want to, [RogueX.Petname]."
        $ RogueX.RecentActions.append("angry")
        $ RogueX.DailyActions.append("angry")
    elif RogueX.Forced:
        $ RogueX.FaceChange("angry", 1)
        ch_r "I'm not that kind of girl!"
        $ RogueX.Statup("Lust", 200, 5)
        if RogueX.Love > 300:
                $ RogueX.Statup("Love", 70, -2)
        $ RogueX.Statup("Obed", 50, -2)
        $ RogueX.RecentActions.append("angry")
        $ RogueX.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ RogueX.FaceChange("angry", 1)
        $ RogueX.DailyActions.append("tabno")
        ch_r "I really don't think this is the right place for that!"
        $ RogueX.Statup("Lust", 200, 5)
        $ RogueX.Statup("Obed", 50, -3)
    elif RogueX.Hand:
        $ RogueX.FaceChange("sad")
        ch_r "I think you can manage it yourself this time. . ."
    else:
        $ RogueX.FaceChange("normal", 1)
        ch_r "I'd really rather not."
    $ RogueX.RecentActions.append("no hand")
    $ RogueX.DailyActions.append("no hand")
    $ temp_modifier = 0
    return


label Rogue_HJ_Prep:
    if Trigger2 == "hand":
        return

    if Taboo:
        $ RogueX.Inbt += int(Taboo/10)
        $ RogueX.Lust += int(Taboo/5)

    $ RogueX.FaceChange("sexy")
    if RogueX.Forced:
        $ RogueX.FaceChange("sad")
    elif not RogueX.Hand:
        $ RogueX.Brows = "confused"
        $ RogueX.Eyes = "sexy"
        $ RogueX.Mouth = "smile"

    call Seen_First_Peen(RogueX,Partner,React=Situation)
    call Rogue_HJ_Launch("L")

    if Situation == RogueX:
            #Rogue auto-starts
            $ Situation = 0
            if Trigger2 == "jackin":
                "[RogueX.Name] brushes your hand aside and starts stroking your cock."
            else:
                "[RogueX.Name] gives you a mischevious smile, and starts to fondle your cock."
            menu:
                "What do you do?"
                "Nothing.":
                    $ RogueX.Statup("Inbt", 70, 3)
                    $ RogueX.Statup("Inbt", 30, 2)
                    "[RogueX.Name] continues her actions."
                "Praise her.":
                    $ RogueX.FaceChange("sexy", 1)
                    $ RogueX.Statup("Inbt", 70, 3)
                    ch_p "Oooh, that's good, [RogueX.Pet]."
                    $ RogueX.NameCheck() #checks reaction to petname
                    "[RogueX.Name] continues her actions."
                    $ RogueX.Statup("Love", 80, 1)
                    $ RogueX.Statup("Obed", 90, 1)
                    $ RogueX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ RogueX.FaceChange("surprised")
                    $ RogueX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [RogueX.Pet]."
                    $ RogueX.NameCheck() #checks reaction to petname
                    "[RogueX.Name] puts it down."
                    $ RogueX.Statup("Obed", 90, 1)
                    $ RogueX.Statup("Obed", 50, 1)
                    $ RogueX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ RogueX.AddWord(1,"refused","refused")
                    return

    if not RogueX.Hand:
        if RogueX.Forced:
            $ RogueX.Statup("Love", 90, -20)
            $ RogueX.Statup("Obed", 70, 25)
            $ RogueX.Statup("Inbt", 80, 30)
        else:
            $ RogueX.Statup("Love", 90, 5)
            $ RogueX.Statup("Obed", 70, 20)
            $ RogueX.Statup("Inbt", 80, 20)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ RogueX.DrainWord("tabno")
    $ RogueX.DrainWord("no hand")
    $ RogueX.RecentActions.append("hand")
    $ RogueX.DailyActions.append("hand")

label Rogue_HJ_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(RogueX)
        call Rogue_HJ_Launch
        $ RogueX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass

                        "Start moving? . ." if not Speed:
                                    $ Speed = 1

                        "Speed up. . ." if Speed < 2:
                                    $ Speed = 2
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 2:
                                    pass

                        "Slow Down. . ." if Speed:
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:
                                    pass
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
                                    "I also want to fondle her breasts." if Trigger2 != "fondle breasts":
                                            if RogueX.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ RogueX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(RogueX,"tired")

                                    "Shift primary action":
                                            if RogueX.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                    if RogueX.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Rogue_HJ_After
                                                                        call Rogue_Blowjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(RogueX,"tired")

                                                        "How about a titjob?":
                                                                    if RogueX.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Rogue_HJ_After
                                                                        call Rogue_Titjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(RogueX,"tired")
                                                        "Never Mind":
                                                                jump Rogue_HJ_Cycle
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
                                                        jump Rogue_HJ_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Rogue_HJ_Cycle
                                            "Never mind":
                                                        jump Rogue_HJ_Cycle
                                    "Undress [RogueX.Name]":
                                            call Girl_Undress(RogueX)
                                    "Clean up [RogueX.Name] (locked)" if not RogueX.Spunk:
                                            pass
                                    "Clean up [RogueX.Name]" if RogueX.Spunk:
                                            call Girl_Cleanup(RogueX,"ask")
                                    "Never mind":
                                            jump Rogue_HJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Rogue_HJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Rogue_HJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Rogue_HJ_Reset
                                    $ Line = 0
                                    jump Rogue_HJ_After
        #End menu (if Line)

        call Shift_Focus(RogueX)
        call Sex_Dialog(RogueX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or RogueX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(RogueX)
                            if "angry" in RogueX.RecentActions:
                                call Rogue_HJ_Reset
                                return
                            $ RogueX.Statup("Lust", 200, 5)
                            if 100 > RogueX.Lust >= 70 and RogueX.OCount < 2 and RogueX.SEXP >= 20:
                                $ RogueX.RecentActions.append("unsatisfied")
                                $ RogueX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Rogue_HJ_After
                            $ Line = "came"

                    if RogueX.Lust >= 100:
                            #If Rogue can cum
                            call Girl_Cumming(RogueX)
                            if Situation == "shift" or "angry" in RogueX.RecentActions:
                                jump Rogue_HJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in RogueX.RecentActions:#And Rogue is unsatisfied,
                                "[RogueX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Rogue_HJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif Cnt == (5 + RogueX.Hand):
                    $ RogueX.Brows = "confused"
                    ch_r "Are you getting close here? I'm getting a little sore."
        elif Cnt == (10 + RogueX.Hand):
                    $ RogueX.Brows = "angry"
                    menu:
                        ch_r "I'm getting rug-burn here [RogueX.Petname]. Can we do something else?"
                        "How about a BJ?" if RogueX.Action and MultiAction:
                                $ Situation = "shift"
                                call Rogue_HJ_After
                                call Rogue_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                jump Rogue_HJ_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Rogue_HJ_Reset
                                $ Situation = "shift"
                                jump Rogue_HJ_After
                        "No, get back down there.":
                                if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):
                                    $ RogueX.Statup("Love", 200, -5)
                                    $ RogueX.Statup("Obed", 50, 3)
                                    $ RogueX.Statup("Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    $ RogueX.FaceChange("angry", 1)
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_r "Well if that's your attitude you can handle your own business."
                                    $ RogueX.Statup("Love", 50, -3, 1)
                                    $ RogueX.Statup("Love", 80, -4, 1)
                                    $ RogueX.Statup("Obed", 30, -1, 1)
                                    $ RogueX.Statup("Obed", 50, -1, 1)
                                    $ RogueX.RecentActions.append("angry")
                                    $ RogueX.DailyActions.append("angry")
                                    jump Rogue_HJ_After
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

label Rogue_HJ_After:
    $ RogueX.FaceChange("sexy")

    $ RogueX.Hand += 1
    $ RogueX.Action -=1
    $ RogueX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ RogueX.Addictionrate += 1
    $ RogueX.Statup("Lust", 90, 5)

    call Partner_Like(RogueX,2)

    if "Rogue Handi-Queen" in Achievements:
            pass
    elif RogueX.Hand >= 10:
            $ RogueX.FaceChange("smile", 1)
            ch_r "I guess you can call me \"Handi-Queen.\""
            $ Achievements.append("Rogue Handi-Queen")
            $RogueX.SEXP += 5
    elif RogueX.Hand == 1:
            $RogueX.SEXP += 10
            if RogueX.Love >= 500:
                $ RogueX.Mouth = "smile"
                ch_r "Well, it's really nice to finally be able to reach out and touch someone."
            elif Player.Focus <= 20:
                $ RogueX.Mouth = "sad"
                ch_r "Well, I hope that got your rocks off."
    elif RogueX.Hand == 5:
            ch_r "I think I've got this well in hand."

    $ temp_modifier = 0
    if Situation == "shift":
        ch_r "Mmm, so what else did you have in mind?"
    else:
        call Rogue_HJ_Reset
    call Checkout
    return

## end RogueX.Handjob //////////////////////////////////////////////////////////////////////


## RogueX.Titjob //////////////////////////////////////////////////////////////////////
label Rogue_Titjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(RogueX)
    if RogueX.Tit >= 7: # She loves it
        $ temp_modifier += 10
    elif RogueX.Tit >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif RogueX.Tit: #You've done it before
        $ temp_modifier += 5

    if RogueX.Addict >= 75 and RogueX.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 15
    elif RogueX.Addict >= 75:
        $ temp_modifier += 5

    if RogueX.SeenChest and ApprovalCheck(RogueX, 500): # You've seen her tits.
        $ temp_modifier += 10
    if not RogueX.Chest and not RogueX.Over: #She's already topless
        $ temp_modifier += 10
    if RogueX.Lust > 75: #She's really horny
        $ temp_modifier += 10
    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in RogueX.Traits:
        $ temp_modifier += (5*Taboo)
    if RogueX in Player.Harem or "sex friend" in RogueX.Petnames:
        $ temp_modifier += 10
    elif "ex" in RogueX.Traits:
        $ temp_modifier -= 30
    if RogueX.ForcedCount and not RogueX.Forced:
        $ temp_modifier -= 5 * RogueX.ForcedCount

    if Taboo and "tabno" in RogueX.DailyActions:
        $ temp_modifier -= 10

    if "no titjob" in RogueX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no titjob" in RogueX.RecentActions else 0

    $ Approval = ApprovalCheck(RogueX, 1200, TabM = 5) # 120, 135, 150, Taboo -200(320)

    if not RogueX.Tit and "no titjob" not in RogueX.RecentActions:
        $ RogueX.FaceChange("surprised", 1)
        $ RogueX.Mouth = "kiss"
        ch_r "You want me to rub your cock with my breasts?"
        if RogueX.Blow:
            $ RogueX.Mouth = "smile"
            ch_r "My mouth wasn't enough?"
        elif RogueX.Hand:
            $ RogueX.Mouth = "smile"
            ch_r "My hand wasn't enough?"

    if not RogueX.Tit and Approval:                                                 #First time dialog
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Love", 70, -3, 1)
            $ RogueX.Statup("Love", 20, -2, 1)
        elif RogueX.Love >= (RogueX.Obed + RogueX.Inbt):
            $ RogueX.FaceChange("sexy")
            $ RogueX.Brows = "sad"
            $ RogueX.Mouth = "smile"
            ch_r "Huh, well that's certainly one way to get off."
        elif RogueX.Obed >= RogueX.Inbt:
            $ RogueX.FaceChange("normal")
            ch_r "If that's what you want. . ."
        elif RogueX.Addict >= 50:
            $ RogueX.FaceChange("manic", 1)
            ch_r "Hmmmm. . . ."
        else: # Uninhibited
            $ RogueX.FaceChange("sad")
            $ RogueX.Mouth = "smile"
            ch_r "Heh, might be fun."
    elif Approval:                                                                       #Second time+ dialog
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Love", 70, -3, 1)
            $ RogueX.Statup("Love", 20, -2, 1)
            ch_r "This isn't going to become a habit, will it?"
        elif not Taboo and "tabno" in RogueX.DailyActions:
            ch_r "Ok, I guess this is private enough. . ."
        elif "titjob" in RogueX.RecentActions:
            $ RogueX.FaceChange("sexy", 1)
            ch_r "Mmm, again? Ok, let me get the girls ready."
            jump Rogue_TJ_Prep
        elif "titjob" in RogueX.DailyActions:
            $ RogueX.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",
                "You're going to give me calluses.",
                "Didn't get enough earlier?",
                "My tits are still a bit sore from earlier."])
            ch_r "[Line]"
        elif RogueX.Tit < 3:
            $ RogueX.FaceChange("sexy", 1)
            $ RogueX.Brows = "confused"
            $ RogueX.Mouth = "kiss"
            ch_r "So you'd like another titjob?"
        else:
            $ RogueX.FaceChange("sexy", 1)
            $ RogueX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action [jiggles her tits]?",
                "So you'd like another titjob?",
                "A little. . . bounce?",
                "You want me to pillow your crank?",
                "A little soft embrace?"])
            ch_r "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Obed", 90, 1)
            $ RogueX.Statup("Inbt", 60, 1)
            ch_r "Well, there are worst ways to get you off. . ."
        elif "no titjob" in RogueX.DailyActions:
            ch_r "Hmm, I suppose. . ."
        else:
            $ RogueX.FaceChange("sexy", 1)
            $ RogueX.Statup("Love", 90, 1)
            $ RogueX.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, put it here.",
                "Well. . . ok.",
                "Yum.",
                "Sure, whip it out.",
                "Fine. . . [She drools a bit into her cleavage].",
                "Heh, ok, alright."])
            ch_r "[Line]"
            $ Line = 0
        $ RogueX.Statup("Obed", 20, 1)
        $ RogueX.Statup("Obed", 70, 1)
        $ RogueX.Statup("Inbt", 80, 2)
        jump Rogue_TJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ RogueX.FaceChange("angry")
        if "no titjob" in RogueX.RecentActions:
            ch_r "I {i}just{/i} told you \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions and "no titjob" in RogueX.DailyActions:
            ch_r "This is just way too exposed!"
        elif "no titjob" in RogueX.DailyActions:
            ch_r "I already told you \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions:
            ch_r "This is just way too exposed!"
        elif not RogueX.Tit:
            $ RogueX.FaceChange("bemused")
            ch_r "I'm not really up for that, [RogueX.Petname]. . ."
        else:
            $ RogueX.FaceChange("bemused")
            ch_r "Not, right now [RogueX.Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no titjob" in RogueX.DailyActions:
                $ RogueX.FaceChange("bemused")
                ch_r "Yeah, ok, [RogueX.Petname]."
                return
            "Maybe later?" if "no titjob" not in RogueX.DailyActions:
                $ RogueX.FaceChange("sexy")
                ch_r "We'll have to see."
                $ RogueX.Statup("Love", 80, 2)
                $ RogueX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ RogueX.RecentActions.append("tabno")
                    $ RogueX.DailyActions.append("tabno")
                $ RogueX.RecentActions.append("no titjob")
                $ RogueX.DailyActions.append("no titjob")
                return
            "I think this could be fun for both of us. . .":
                if Approval:
                    $ RogueX.FaceChange("sexy")
                    $ RogueX.Statup("Obed", 80, 2)
                    $ RogueX.Statup("Obed", 40, 2)
                    $ RogueX.Statup("Inbt", 70, 3)
                    $ RogueX.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Well, ok, put it here.",
                        "Well. . . ok.",
                        "I guess.",
                        "I guess, whip it out.",
                        "Fine. . . [She drools a bit into her cleavage].",
                        "Heh, ok, alright."])
                    ch_r "[Line]"
                    $ Line = 0
                    jump Rogue_TJ_Prep
                else:
                    $ Approval = ApprovalCheck(RogueX, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)             Handy instead?
                    if Approval >= 2:
                        $ RogueX.Statup("Inbt", 80, 1)
                        $ RogueX.Statup("Inbt", 60, 3)
                        $ RogueX.FaceChange("confused", 1)
                        if RogueX.Blow:
                            ch_r "I could just. . . blow you instead?"
                        else:
                            ch_r "I could maybe. . . you know, [[she pushes her tongue against the side of her cheek]?"
                        menu:
                            extend ""
                            "Ok, get down there.":
                                $ RogueX.Statup("Love", 80, 2)
                                $ RogueX.Statup("Inbt", 60, 1)
                                $ RogueX.Statup("Obed", 50, 1)
                                jump Rogue_BJ_Prep
                            "Nah, it's all about dem titties.":
                                $ Line = "no BJ"
                    if Approval:
                        $ RogueX.Statup("Inbt", 80, 1)
                        $ RogueX.Statup("Inbt", 60, 3)
                        $ RogueX.FaceChange("confused", 1)
                        if RogueX.Hand:
                            ch_r "Maybe you'd settle for a handy?"
                        else:
                            ch_r "I could maybe. . . [[she makes a jerking motion with her hand]?"
                        menu:
                            extend ""
                            "Sure, that's fine.":
                                $ RogueX.Statup("Love", 80, 2)
                                $ RogueX.Statup("Inbt", 60, 1)
                                $ RogueX.Statup("Obed", 50, 1)
                                jump Rogue_HJ_Prep
                            "Seriously, titties." if Line == "no BJ":
                                $ Line = 0
                            "Nah, it's all about dem titties." if Line != "no BJ":
                                pass
                    $ RogueX.Statup("Love", 200, -2)
                    ch_r "Ok, whatever."
                    $ RogueX.Statup("Obed", 70, 2)


            "Come on, let me fuck those titties, [RogueX.Pet]":                                               # Pressured into it
                $ RogueX.NameCheck() #checks reaction to petname
                $ Approval = ApprovalCheck(RogueX, 700, "OI", TabM = 4) # 70, 85, 100, -160(230)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.FaceChange("sad")
                    $ RogueX.Statup("Love", 70, -5, 1)
                    $ RogueX.Statup("Love", 200, -2)
                    ch_r "Ok, fine, whip it out."
                    $ RogueX.Statup("Obed", 50, 4)
                    $ RogueX.Statup("Inbt", 80, 1)
                    $ RogueX.Statup("Inbt", 60, 3)
                    $ RogueX.Forced = 1
                    jump Rogue_TJ_Prep
                else:
                    $ RogueX.Statup("Love", 200, -15)
                    $ RogueX.RecentActions.append("angry")
                    $ RogueX.DailyActions.append("angry")

    #She refused all offers.
    if "no titjob" in RogueX.DailyActions:
        $ RogueX.FaceChange("angry", 1)
        ch_r "Look, I already told you no thanks, [RogueX.Petname]."
        $ RogueX.RecentActions.append("angry")
        $ RogueX.DailyActions.append("angry")
    elif RogueX.Forced:
        $ RogueX.FaceChange("angry", 1)
        ch_r "I'm not that kind of girl."
        $ RogueX.Statup("Lust", 200, 5)
        if RogueX.Love > 300:
                $ RogueX.Statup("Love", 70, -2)
        $ RogueX.Statup("Obed", 50, -2)
        $ RogueX.RecentActions.append("angry")
        $ RogueX.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ RogueX.FaceChange("angry", 1)
        $ RogueX.DailyActions.append("tabno")
        ch_r "You really expect me to do that here? You realize how. . . exposed that would be?"
        $ RogueX.Statup("Lust", 200, 5)
        $ RogueX.Statup("Obed", 50, -3)
    elif RogueX.Tit:
        $ RogueX.FaceChange("sad")
        ch_r "I think I'll let you know when I want you touching these again."
    else:
        $ RogueX.FaceChange("normal", 1)
        ch_r "How about let's not, [RogueX.Petname]."
    $ RogueX.RecentActions.append("no titjob")
    $ RogueX.DailyActions.append("no titjob")
    $ temp_modifier = 0
    return

label Rogue_TJ_Prep:

    if Taboo:
        $ RogueX.Inbt += int(Taboo/10)
        $ RogueX.Lust += int(Taboo/5)


    $ RogueX.FaceChange("sexy")
    if RogueX.Forced:
        $ RogueX.FaceChange("sad")
    elif not RogueX.Tit:
        $ RogueX.Brows = "confused"
        $ RogueX.Eyes = "sexy"
        $ RogueX.Mouth = "smile"

    call Seen_First_Peen(RogueX,Partner,React=Situation)
    call Rogue_TJ_Launch("L")

    if Situation == RogueX:
            #Rogue auto-starts
            $ Situation = 0
            "[RogueX.Name] slides down and sandwiches your dick between her tits."
            menu:
                "What do you do?"
                "Nothing.":
                    $ RogueX.Statup("Inbt", 80, 3)
                    $ RogueX.Statup("Inbt", 40, 2)
                    "[RogueX.Name] starts to slide them up and down."
                "Praise her.":
                    $ RogueX.FaceChange("sexy", 1)
                    $ RogueX.Statup("Inbt", 80, 3)
                    ch_p "Oh, that sounds like a good idea, [RogueX.Pet]."
                    $ RogueX.NameCheck() #checks reaction to petname
                    "[RogueX.Name] continues her actions."
                    $ RogueX.Statup("Love", 85, 1)
                    $ RogueX.Statup("Obed", 90, 1)
                    $ RogueX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ RogueX.FaceChange("confused")
                    $ RogueX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [RogueX.Pet]."
                    $ RogueX.NameCheck() #checks reaction to petname
                    "[RogueX.Name] lets it drop out from between her breasts."
                    $ RogueX.Statup("Obed", 90, 1)
                    $ RogueX.Statup("Obed", 50, 3)
                    $ Player.RecentActions.append("nope")
                    $ RogueX.AddWord(1,"refused","refused")
                    return

    if not RogueX.Tit:
        if RogueX.Forced:
            $ RogueX.Statup("Love", 90, -25)
            $ RogueX.Statup("Obed", 70, 30)
            $ RogueX.Statup("Inbt", 80, 35)
        else:
            $ RogueX.Statup("Love", 90, 5)
            $ RogueX.Statup("Obed", 70, 25)
            $ RogueX.Statup("Inbt", 80, 30)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ RogueX.DrainWord("tabno")
    $ RogueX.DrainWord("no titjob")
    $ RogueX.RecentActions.append("titjob")
    $ RogueX.DailyActions.append("titjob")


label Rogue_TJ_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(RogueX)
        call Rogue_TJ_Launch
        $ RogueX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass

                        "Start moving? . ." if not Speed:
                                    $ Speed = 1

                        "Speed up. . ." if Speed < 2:
                                    $ Speed = 2
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 2:
                                    pass

                        "Slow Down. . ." if Speed:
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:
                                    pass
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
                                    "I also want to fondle her breasts." if Trigger2 != "fondle breasts":
                                            if RogueX.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ RogueX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(RogueX,"tired")

                                    "Shift primary action":
                                            if RogueX.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                if RogueX.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Rogue_TJ_After
                                                                    call Rogue_Blowjob
                                                                else:
                                                                    call Sex_Basic_Dialog(RogueX,"tired")

                                                        "How about a handy?":
                                                                if RogueX.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Rogue_TJ_After
                                                                    call Rogue_Handjob
                                                                else:
                                                                    call Sex_Basic_Dialog(RogueX,"tired")
                                                        "Never Mind":
                                                                jump Rogue_TJ_Cycle
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
                                                        jump Rogue_TJ_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Rogue_TJ_Cycle
                                            "Never mind":
                                                        jump Rogue_TJ_Cycle
                                    "Undress [RogueX.Name]":
                                            call Girl_Undress(RogueX)
                                    "Clean up [RogueX.Name] (locked)" if not RogueX.Spunk:
                                            pass
                                    "Clean up [RogueX.Name]" if RogueX.Spunk:
                                            call Girl_Cleanup(RogueX,"ask")
                                    "Never mind":
                                            jump Rogue_TJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Rogue_TJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Rogue_TJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Rogue_TJ_Reset
                                    $ Line = 0
                                    jump Rogue_TJ_After
        #End menu (if Line)

        call Shift_Focus(RogueX)
        call Sex_Dialog(RogueX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or RogueX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(RogueX)
                            if "angry" in RogueX.RecentActions:
                                call Rogue_TJ_Reset
                                return
                            $ RogueX.Statup("Lust", 200, 5)
                            if 100 > RogueX.Lust >= 70 and RogueX.OCount < 2 and RogueX.SEXP >= 20:
                                $ RogueX.RecentActions.append("unsatisfied")
                                $ RogueX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Rogue_TJ_After
                            $ Line = "came"

                    if RogueX.Lust >= 100:
                            #If Rogue can cum
                            call Girl_Cumming(RogueX)
                            if Situation == "shift" or "angry" in RogueX.RecentActions:
                                jump Rogue_TJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in RogueX.RecentActions:#And Rogue is unsatisfied,
                                "[RogueX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Rogue_TJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif Cnt == (5 + RogueX.Tit):
                    $ RogueX.Brows = "confused"
                    ch_r "Are you getting close here? I'm getting a little sore."
        elif Cnt == (10 + RogueX.Tit):
                    $ RogueX.Brows = "angry"
                    menu:
                        ch_r "I'm getting rug-burn here [RogueX.Petname]. Can we do something else?"
                        "How about a BJ?" if RogueX.Action and MultiAction:
                                $ Situation = "shift"
                                call Rogue_TJ_After
                                call Rogue_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                jump Rogue_TJ_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Rogue_TJ_Reset
                                $ Situation = "shift"
                                jump Rogue_TJ_After
                        "No, get back down there.":
                                if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):
                                    $ RogueX.Statup("Love", 200, -5)
                                    $ RogueX.Statup("Obed", 50, 3)
                                    $ RogueX.Statup("Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    $ RogueX.FaceChange("angry", 1)
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_r "Well if that's your attitude you can handle your own business."
                                    $ RogueX.Statup("Love", 50, -3, 1)
                                    $ RogueX.Statup("Love", 80, -4, 1)
                                    $ RogueX.Statup("Obed", 30, -1, 1)
                                    $ RogueX.Statup("Obed", 50, -1, 1)
                                    $ RogueX.RecentActions.append("angry")
                                    $ RogueX.DailyActions.append("angry")
                                    jump Rogue_TJ_After
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

label Rogue_TJ_After:
    $ RogueX.FaceChange("sexy")

    $ RogueX.Tit += 1
    $ RogueX.Action -=1
    $ RogueX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ RogueX.Addictionrate += 1

    call Partner_Like(RogueX,3)

    if RogueX.Tit > 5:
            pass
    elif RogueX.Tit == 1:
        $ RogueX.SEXP += 12
        if RogueX.Love >= 500:
            $ RogueX.Mouth = "smile"
            ch_r "Well, that was certainly interesting."
        elif Player.Focus <= 20:
            $ RogueX.Mouth = "sad"
            ch_r "Well, I hope that was enough for you."
    elif RogueX.Tit == 5:
            ch_r "I think I've got the goods for this."


    $ temp_modifier = 0
    if Situation == "shift":
            ch_r "Mmm, so what else did you have in mind?"
    else:
            call Rogue_TJ_Reset
    call Checkout
    return

## end RogueX.Titjob //////////////////////////////////////////////////////////////////////

# RogueX.Blowjob //////////////////////////////////////////////////////////////////////

label Rogue_Blowjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(RogueX)
    if RogueX.Blow >= 7: # She loves it
        $ temp_modifier += 15
    elif RogueX.Blow >= 3: #You've done it before several times
        $ temp_modifier += 10
    elif RogueX.Blow: #You've done it before
        $ temp_modifier += 7

    if RogueX.Addict >= 75 and RogueX.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 25
    elif RogueX.Addict >= 75: #She's really strung out
        $ temp_modifier += 15

    if Situation == "shift":
        $ temp_modifier += 15
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

    if "no blow" in RogueX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no blow" in RogueX.RecentActions else 0

    $ Approval = ApprovalCheck(RogueX, 1300, TabM = 4) # 130, 145, 160, Taboo -160(290)

    if not RogueX.Blow and "no blow" not in RogueX.RecentActions:
        $ RogueX.FaceChange("surprised", 1)
        $ RogueX.Mouth = "kiss"
        ch_r "You want me to put your dick. . . in my mouth?"
        if RogueX.Hand:
            $ RogueX.Mouth = "smile"
            ch_r "My hand wasn't enough?"

    if not RogueX.Blow and Approval:                                                 #First time dialog
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Love", 70, -3, 1)
            $ RogueX.Statup("Love", 20, -2, 1)
        elif RogueX.Love >= (RogueX.Obed + RogueX.Inbt):
            $ RogueX.FaceChange("sexy")
            $ RogueX.Brows = "sad"
            $ RogueX.Mouth = "smile"
            ch_r "I've never really put something like that in my mouth. . . might be interesting."
        elif RogueX.Obed >= RogueX.Inbt:
            $ RogueX.FaceChange("normal")
            ch_r "I suppose, if that's what you want. . ."
        elif RogueX.Addict >= 50:
            $ RogueX.FaceChange("manic", 1)
            ch_r "I think. . . for some reason I really do want that in my mouth. . ."
        else: # Uninhibited
            $ RogueX.FaceChange("sad")
            $ RogueX.Mouth = "smile"
            ch_r "I guess. . ."
    elif Approval:                                                                       #Second time+ dialog
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Love", 70, -3, 1)
            $ RogueX.Statup("Love", 20, -2, 1)
            ch_r "You want me to do that again?"
        elif not Taboo and "tabno" in RogueX.DailyActions:
            ch_r "Ok, I guess this is private enough. . ."
        elif "blow" in RogueX.RecentActions:
            $ RogueX.FaceChange("sexy", 1)
            ch_r "Mmm, again? [[stretches her jaw]"
            jump Rogue_BJ_Prep
        elif "blow" in RogueX.DailyActions:
            $ RogueX.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",
                "You're going to give me lockjaw.",
                "Let me get some saliva going.",
                "Didn't get enough earlier?",
                "My jaw's still a bit sore from earlier.",
                "My jaw's still a bit sore from earlier."])
            ch_r "[Line]"
        elif RogueX.Blow < 3:
            $ RogueX.FaceChange("sexy", 1)
            $ RogueX.Brows = "confused"
            $ RogueX.Mouth = "kiss"
            ch_r "So you'd like another blowjob?"
        else:
            $ RogueX.FaceChange("sexy", 1)
            $ RogueX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action [mimes blowing]?",
                "So you'd like another blowjob?",
                "A little. . . lick?",
                "You want me to wet your willy?",
                "A little tender loving care?"])
            ch_r "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Obed", 90, 1)
            $ RogueX.Statup("Inbt", 60, 1)
            ch_r "Whatever."
        elif "no blow" in RogueX.DailyActions:
            ch_r "Oh, I suppose it isn't so bad. . ."
        else:
            $ RogueX.FaceChange("sexy", 1)
            $ RogueX.Statup("Love", 90, 1)
            $ RogueX.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, ahhhhhh.",
                "Well. . . ok.",
                "Yum.",
                "Sure, whip it out.",
                "Fine. . . [She licks her lips].",
                "Heh, ok, alright."])
            ch_r "[Line]"
            $ Line = 0
        $ RogueX.Statup("Obed", 20, 1)
        $ RogueX.Statup("Obed", 70, 1)
        $ RogueX.Statup("Inbt", 80, 2)
        jump Rogue_BJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ RogueX.FaceChange("angry")
        if "no blow" in RogueX.RecentActions:
            ch_r "I {i}just{/i} told you \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions and "no blow" in RogueX.DailyActions:
            ch_r "I already told you that I wouldn't suck you off in public!"
        elif "no blow" in RogueX.DailyActions:
            ch_r "I already told you \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions:
            ch_r "I already told you this is too public!"
        elif not RogueX.Blow:
            $ RogueX.FaceChange("bemused")
            ch_r "I don't think I'd like the taste, [RogueX.Petname]. . ."
        else:
            $ RogueX.FaceChange("bemused")
            ch_r "Not, right now [RogueX.Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no blow" in RogueX.DailyActions:
                $ RogueX.FaceChange("bemused")
                ch_r "Yeah, ok, [RogueX.Petname]."
                return
            "Maybe later?" if "no blow" not in RogueX.DailyActions:
                $ RogueX.FaceChange("sexy")
                ch_r "I might get hungry, [RogueX.Petname]."
                $ RogueX.Statup("Love", 80, 2)
                $ RogueX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ RogueX.RecentActions.append("tabno")
                    $ RogueX.DailyActions.append("tabno")
                $ RogueX.RecentActions.append("no blow")
                $ RogueX.DailyActions.append("no blow")
                return
            "Come on, please?":
                if Approval:
                    $ RogueX.FaceChange("sexy")
                    $ RogueX.Statup("Obed", 90, 2)
                    $ RogueX.Statup("Obed", 50, 2)
                    $ RogueX.Statup("Inbt", 70, 3)
                    $ RogueX.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Well, sure, ahhhhhh.",
                        "Well. . . ok.",
                        "I guess a taste couldn't hurt.",
                        "I guess I could. . . whip it out.",
                        "Fine. . . [She licks her lips].",
                        "Heh, ok, alright."])
                    ch_r "[Line]"
                    $ Line = 0
                    jump Rogue_BJ_Prep
                else:
                    if ApprovalCheck(RogueX, 1100, TabM = 3): # 110, 125, 140, Taboo -120(230)             Handy instead?
                        $ RogueX.Statup("Inbt", 80, 1)
                        $ RogueX.Statup("Inbt", 60, 3)
                        $ RogueX.FaceChange("confused", 1)
                        if RogueX.Hand:
                            ch_r "Maybe you'd settle for a handy?"
                        else:
                            ch_r "I could maybe. . . [[she makes a jerking motion with her hand]?"
                        menu:
                            ch_r "What do you say?"
                            "Sure, that's fine.":
                                $ RogueX.Statup("Love", 80, 2)
                                $ RogueX.Statup("Inbt", 60, 1)
                                $ RogueX.Statup("Obed", 50, 1)
                                jump Rogue_HJ_Prep
                            "Nah, if it's not a BJ, forget it.":
                                $ RogueX.Statup("Love", 200, -2)
                                ch_r "Ok, whatever."
                                $ RogueX.Statup("Obed", 70, 2)


            "Suck it, [RogueX.Pet]":                                               # Pressured into it
                $ RogueX.NameCheck() #checks reaction to petname
                $ Approval = ApprovalCheck(RogueX, 750, "OI", TabM = 3) # 75, 90, 105, -120(195)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.FaceChange("sad")
                    $ RogueX.Statup("Love", 70, -5, 1)
                    $ RogueX.Statup("Love", 200, -2)
                    ch_r "Ok, fine, whip it out."
                    $ RogueX.Statup("Obed", 50, 4)
                    $ RogueX.Statup("Inbt", 80, 1)
                    $ RogueX.Statup("Inbt", 60, 3)
                    $ RogueX.Forced = 1
                    jump Rogue_BJ_Prep
                else:
                    $ RogueX.Statup("Love", 200, -15)
                    $ RogueX.RecentActions.append("angry")
                    $ RogueX.DailyActions.append("angry")

    #She refused all offers.
    if "no blow" in RogueX.DailyActions:
        $ RogueX.FaceChange("angry", 1)
        ch_r "Read my lips, no."
        $ RogueX.RecentActions.append("angry")
        $ RogueX.DailyActions.append("angry")
    elif RogueX.Forced:
        $ RogueX.FaceChange("angry", 1)
        ch_r "That isn't something I'd want!"
        $ RogueX.Statup("Lust", 200, 5)
        if RogueX.Love > 300:
                $ RogueX.Statup("Love", 70, -2)
        $ RogueX.Statup("Obed", 50, -2)
        $ RogueX.RecentActions.append("angry")
        $ RogueX.DailyActions.append("angry")
        $ RogueX.RecentActions.append("no blow")
        $ RogueX.DailyActions.append("no blow")
        return
    elif Taboo:                             # she refuses and this is too public a place for her
        $ RogueX.FaceChange("angry", 1)
        $ RogueX.DailyActions.append("tabno")
        ch_r "You really expect me to do that here?"
        $ RogueX.Statup("Lust", 200, 5)
        $ RogueX.Statup("Obed", 50, -3)
        return
    elif RogueX.Blow:
        $ RogueX.FaceChange("sad")
        ch_r "I think I've got the taste out of my mouth, thanks."
    else:
        $ RogueX.FaceChange("normal", 1)
        ch_r "Not interested."
    $ RogueX.RecentActions.append("no blow")
    $ RogueX.DailyActions.append("no blow")
    $ temp_modifier = 0
    return


label Rogue_BJ_Prep:
    if Taboo:
        $ RogueX.Inbt += int(Taboo/10)
        $ RogueX.Lust += int(Taboo/5)

    $ RogueX.FaceChange("sexy")
    if RogueX.Forced:
        $ RogueX.FaceChange("sad")
    elif not RogueX.Blow:
        $ RogueX.Brows = "confused"
        $ RogueX.Eyes = "sexy"
        $ RogueX.Mouth = "smile"

    call Seen_First_Peen(RogueX,Partner,React=Situation)
    call Rogue_BJ_Launch("L")

    if Situation == RogueX:
            #Rogue auto-starts
            $ Situation = 0
            "[RogueX.Name] slides down and gives your cock a little lick."
            menu:
                "What do you do?"
                "Nothing.":
                    $ RogueX.Statup("Inbt", 80, 3)
                    $ RogueX.Statup("Inbt", 40, 2)
                    "[RogueX.Name] continues licking at it."
                "Praise her.":
                    $ RogueX.FaceChange("sexy", 1)
                    $ RogueX.Statup("Inbt", 80, 3)
                    ch_p "Hmmm, keep doing that, [RogueX.Pet]."
                    $ RogueX.NameCheck() #checks reaction to petname
                    "[RogueX.Name] continues her actions."
                    $ RogueX.Statup("Love", 85, 1)
                    $ RogueX.Statup("Obed", 90, 1)
                    $ RogueX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ RogueX.FaceChange("surprised")
                    $ RogueX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [RogueX.Pet]."
                    $ RogueX.NameCheck() #checks reaction to petname
                    "[RogueX.Name] puts it down."
                    $ RogueX.Statup("Obed", 90, 1)
                    $ RogueX.Statup("Obed", 50, 3)
                    $ Player.RecentActions.append("nope")
                    $ RogueX.AddWord(1,"refused","refused")
                    return

    if not RogueX.Blow:
        if RogueX.Forced:
            $ RogueX.Statup("Love", 90, -70)
            $ RogueX.Statup("Obed", 70, 45)
            $ RogueX.Statup("Inbt", 80, 60)
        else:
            $ RogueX.Statup("Love", 90, 5)
            $ RogueX.Statup("Obed", 70, 35)
            $ RogueX.Statup("Inbt", 80, 40)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ RogueX.DrainWord("tabno")
    $ RogueX.DrainWord("no blow")
    $ RogueX.RecentActions.append("blow")
    $ RogueX.DailyActions.append("blow")

label Rogue_BJ_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(RogueX)
        call Rogue_BJ_Launch
        $ RogueX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass

                        "Lick it. . ." if Speed != 1:
                                $ Speed = 1
                        "Lick it. . . (locked)" if Speed == 1:
                                pass

                        "Just the head. . ." if Speed != 2:
                            $ Speed = 2
                        "Just the head. . . (locked)" if Speed == 2:
                                pass

                        "Suck on it." if Speed != 3:
                                $ Speed = 3
                                if Trigger2 == "jackin":
                                    "She dips her head a bit lower, and you move your hand out of the way."

                        "Suck on it. (locked)" if Speed == 3:
                                pass

                        "Take it deeper." if Speed != 4:
                                if "pushed" not in RogueX.RecentActions and RogueX.Blow < 5:
                                    $ RogueX.Statup("Love", 80, -(20-(2*RogueX.Blow)))
                                    $ RogueX.Statup("Obed", 80, (30-(3*RogueX.Blow)))
                                    $ RogueX.RecentActions.append("pushed")
                                if Trigger2 == "jackin" and Speed != 3:
                                    "She takes it to the root, and you move your hand out of the way."
                                $ Speed = 4
                        "Take it deeper. (locked)" if Speed == 4:
                                pass

                        "Set your own pace. . .":
                                "[RogueX.Name] hums contentedly."
                                if "setpace" not in RogueX.RecentActions:
                                    $ RogueX.Statup("Love", 80, 2)
                                $ D20 = renpy.random.randint(1, 20)
                                if RogueX.Blow < 5:
                                    $ D20 -= 10
                                elif RogueX.Blow < 10:
                                    $ D20 -= 5

                                if D20 > 15:
                                    $ Speed = 4
                                    if "setpace" not in RogueX.RecentActions:
                                        $ RogueX.Statup("Inbt", 80, 3)
                                elif D20 > 10:
                                    $ Speed = 3
                                elif D20 > 5:
                                    $ Speed = 2
                                else:
                                    $ Speed = 1
                                $ RogueX.RecentActions.append("setpace")

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
                                    "I also want to fondle her breasts." if Trigger2 != "fondle breasts":
                                            if RogueX.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ RogueX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(RogueX,"tired")

                                    "Shift primary action":
                                            if RogueX.Action and MultiAction:
                                                    menu:
                                                        "How about a handy?":
                                                                if RogueX.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Rogue_BJ_After
                                                                    call Rogue_Handjob
                                                                else:
                                                                    call Sex_Basic_Dialog(RogueX,"tired")
                                                        "How about a titjob?":
                                                                if RogueX.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Rogue_BJ_After
                                                                    call Rogue_Titjob
                                                                else:
                                                                    call Sex_Basic_Dialog(RogueX,"tired")
                                                        "Never Mind":
                                                                jump Rogue_BJ_Cycle
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
                                                        jump Rogue_BJ_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Rogue_BJ_Cycle
                                            "Never mind":
                                                        jump Rogue_BJ_Cycle
                                    "Undress [RogueX.Name]":
                                            call Girl_Undress(RogueX)
                                    "Clean up [RogueX.Name] (locked)" if not RogueX.Spunk:
                                            pass
                                    "Clean up [RogueX.Name]" if RogueX.Spunk:
                                            call Girl_Cleanup(RogueX,"ask")
                                    "Never mind":
                                            jump Rogue_BJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Rogue_BJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Rogue_BJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Rogue_BJ_Reset
                                    $ Line = 0
                                    jump Rogue_BJ_After
        #End menu (if Line)

        call Shift_Focus(RogueX)
        call Sex_Dialog(RogueX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1
        if Speed:
            $ Player.Wet = 1 #wets penis
            $ Player.Spunk = 0 if Player.Spunk else Player.Spunk #cleans you off after one cycle

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or RogueX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(RogueX)
                            if "angry" in RogueX.RecentActions:
                                call Rogue_BJ_Reset
                                return
                            $ RogueX.Statup("Lust", 200, 5)
                            if 100 > RogueX.Lust >= 70 and RogueX.OCount < 2 and RogueX.SEXP >= 20:
                                $ RogueX.RecentActions.append("unsatisfied")
                                $ RogueX.DailyActions.append("unsatisfied")
                            if Player.Focus > 80:
                                jump Rogue_BJ_After
                            $ Line = "came"

                    if RogueX.Lust >= 100:
                            #If Rogue can cum
                            call Girl_Cumming(RogueX)
                            if Situation == "shift" or "angry" in RogueX.RecentActions:
                                jump Rogue_BJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in RogueX.RecentActions:#And Rogue is unsatisfied,
                                "[RogueX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Rogue_BJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif Cnt == (5 + RogueX.Blow):
                    $ RogueX.Brows = "confused"
                    ch_r "Are you getting close here? My jaw's getting pretty sore."
        elif Cnt == (10 + RogueX.Blow):
                    $ RogueX.Brows = "angry"
                    ch_r "I'm getting a little tired, [RogueX.Petname]. Can we do something else?"
                    menu:
                        ch_r "I'm getting a little tired, [RogueX.Petname]. Can we do something else?"
                        "Continue (locked)":
                                pass
                        "How about a Handy?" if RogueX.Action and MultiAction:
                                $ Situation = "shift"
                                call Rogue_BJ_After
                                call Rogue_Handjob
                                return
                        "How about a Handy? (locked)" if not RogueX.Action or not MultiAction:
                                pass
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                jump Rogue_BJ_Cycle
                        "Finish up. (locked)" if not Player.FocusX:
                                pass
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Rogue_BJ_Reset
                                $ Situation = "shift"
                                jump Rogue_BJ_After
                        "Let's try something else. (locked)" if not MultiAction:
                                pass
                        "No, get back down there.":
                                if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):
                                    $ RogueX.Statup("Love", 200, -5)
                                    $ RogueX.Statup("Obed", 50, 3)
                                    $ RogueX.Statup("Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    $ RogueX.FaceChange("angry", 1)
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_r "Well if that's your attitude you can handle your own business."
                                    $ RogueX.Statup("Love", 50, -3, 1)
                                    $ RogueX.Statup("Love", 80, -4, 1)
                                    $ RogueX.Statup("Obed", 30, -1, 1)
                                    $ RogueX.Statup("Obed", 50, -1, 1)
                                    $ RogueX.RecentActions.append("angry")
                                    $ RogueX.DailyActions.append("angry")
                                    jump Rogue_BJ_After
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

label Rogue_BJ_After:
    $ RogueX.FaceChange("sexy")
    $ RogueX.Blow += 1
    $ RogueX.Action -=1
    $ RogueX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ RogueX.Addictionrate += 1

    if Partner == EmmaX:
        call Partner_Like(RogueX,3)
    else:
        call Partner_Like(RogueX,2)

    if "Rogue Jobber" in Achievements:
        pass
    elif RogueX.Blow >= 10:
        $ RogueX.FaceChange("smile", 1)
        ch_r "I'm really starting to enjoy this."
        $ Achievements.append("Rogue Jobber")
        $RogueX.SEXP += 5
    elif Situation == "shift":
        pass
    elif RogueX.Blow == 1:
            $RogueX.SEXP += 15
            if RogueX.Love >= 500:
                $ RogueX.Mouth = "smile"
                ch_r "That really wasn't half bad."
            elif Player.Focus <= 20:
                $ RogueX.Mouth = "sad"
                ch_r "Well, I hope that got your rocks off."
    elif RogueX.Blow == 5:
        ch_r "I think I've got the hang of this."

    $ temp_modifier = 0
    if Situation != "shift":
        call Rogue_BJ_Reset
    call Checkout
    return

return

# end RogueX.Blowjob                                 //////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy
label Rogue_Dildo_Check:
    if "dildo" in Player.Inventory:
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in RogueX.Inventory:
        "You ask [RogueX.Name] to get out her favorite Dildo."
    else:
        "You don't have one of those on you."
        return 0
    return 1

label Rogue_Dildo_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(RogueX)
    call Rogue_Dildo_Check
    if not _return:
        return

    if RogueX.DildoP: #You've done it before
        $ temp_modifier += 15
    if RogueX.PantsNum() > 6: # she's got pants on.
        $ temp_modifier -= 20

    if RogueX.Lust > 95:
        $ temp_modifier += 20
    elif RogueX.Lust > 85: #She's really horny
        $ temp_modifier += 15

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

    if "no dildo" in RogueX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no dildo" in RogueX.RecentActions else 0

    $ Approval = ApprovalCheck(RogueX, 1250, TabM = 4) # 125, 140, 155, Taboo -160(335)

    if Situation == RogueX:                                                                  #Rogue auto-starts
                if Approval > 2:                                                      # fix, add rogue auto stuff here
                    if RogueX.PantsNum() == 5:
                        "[RogueX.Name] grabs her dildo, hiking up her skirt as she does."
                        $ RogueX.Upskirt = 1
                    elif RogueX.PantsNum() > 6:
                        "[RogueX.Name] grabs her dildo, pulling down her pants as she does."
                        $ RogueX.Legs = 0
                    else:
                        "[RogueX.Name] grabs her dildo, rubbing is suggestively against her crotch."
                    $ RogueX.SeenPanties = 1
                    "She slides the tip along her pussy and seems to want you to insert it."
                    menu:
                        "What do you do?"
                        "Nothing.":
                            $ RogueX.Statup("Inbt", 80, 3)
                            $ RogueX.Statup("Inbt", 50, 2)
                            "[RogueX.Name] slides it in."
                        "Go for it.":
                            $ RogueX.FaceChange("sexy", 1)
                            $ RogueX.Statup("Inbt", 80, 3)
                            ch_p "Oh yeah, [RogueX.Pet], let's do this."
                            $ RogueX.NameCheck() #checks reaction to petname
                            "You grab the dildo and slide it in."
                            $ RogueX.Statup("Love", 85, 1)
                            $ RogueX.Statup("Obed", 90, 1)
                            $ RogueX.Statup("Obed", 50, 2)
                        "Ask her to stop.":
                            $ RogueX.FaceChange("surprised")
                            $ RogueX.Statup("Inbt", 70, 1)
                            ch_p "Let's not do that right now, [RogueX.Pet]."
                            $ RogueX.NameCheck() #checks reaction to petname
                            "[RogueX.Name] sets the dildo down."
                            $ RogueX.Statup("Obed", 90, 1)
                            $ RogueX.Statup("Obed", 50, 1)
                            $ RogueX.Statup("Obed", 30, 2)
                            return
                    jump Rogue_DP_Prep
                else:
                    $ temp_modifier = 0                               # fix, add rogue auto stuff here
                    $ Trigger2 = 0
                return

    if Situation == "auto":
                "You rub the dildo across her body, and along her moist slit."
                $ RogueX.FaceChange("surprised", 1)

                if (RogueX.DildoP and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
                    "[RogueX.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                    $ RogueX.FaceChange("sexy")
                    $ RogueX.Statup("Obed", 70, 3)
                    $ RogueX.Statup("Inbt", 50, 3)
                    $ RogueX.Statup("Inbt", 70, 1)
                    ch_r "Ok, [RogueX.Petname], let's do this."
                    jump Rogue_DP_Prep
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
                                jump Rogue_DP_Prep
                            "You pull back before you really get it in."
                            $ RogueX.FaceChange("bemused", 1)
                            if RogueX.DildoP:
                                ch_r "Well ok, [RogueX.Petname], no harm done. Just give me a little warning next time."
                            else:
                                ch_r "Well ok, [RogueX.Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."
                        "Just playing with my favorite toys.":
                            $ RogueX.Statup("Love", 80, -10, 1)
                            $ RogueX.Statup("Love", 200, -10)
                            "You press it inside some more."
                            $ RogueX.Statup("Obed", 70, 3)
                            $ RogueX.Statup("Inbt", 50, 3)
                            if not ApprovalCheck(RogueX, 700, "O", TabM=1): #Checks if Obed is 700+
                                $ RogueX.FaceChange("angry")
                                "[RogueX.Name] shoves you away and slaps you in the face."
                                ch_r "Jackass!"
                                ch_r "If that's how you want to treat me, we're done here!"
                                $ RogueX.Statup("Love", 50, -10, 1)
                                $ RogueX.Statup("Obed", 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                if renpy.showing("Rogue_Doggy"):
                                    call Rogue_Doggy_Reset
                                $ RogueX.RecentActions.append("angry")
                                $ RogueX.DailyActions.append("angry")
                            else:
                                $ RogueX.FaceChange("sad")
                                "[RogueX.Name] doesn't seem to be into this, you're lucky she's so obedient."
                                jump Rogue_DP_Prep
                return
    #end Auto

    if not RogueX.DildoP:
            #first time
            $ RogueX.FaceChange("surprised", 1)
            $ RogueX.Mouth = "kiss"
            ch_r "Hmmm, so you'd like to try out some toys?"
            if RogueX.Forced:
                $ RogueX.FaceChange("sad")
                ch_r "I suppose there are worst things you could ask for."

    if not RogueX.DildoP and Approval:
            #First time dialog
            if RogueX.Forced:
                $ RogueX.FaceChange("sad")
                $ RogueX.Statup("Love", 70, -3, 1)
                $ RogueX.Statup("Love", 20, -2, 1)
            elif RogueX.Love >= (RogueX.Obed + RogueX.Inbt):
                $ RogueX.FaceChange("sexy")
                $ RogueX.Brows = "sad"
                $ RogueX.Mouth = "smile"
                ch_r "I've had a reasonable amount of experience with these, you know. . ."
            elif RogueX.Obed >= RogueX.Inbt:
                $ RogueX.FaceChange("normal")
                ch_r "If that's what you want, [RogueX.Petname]. . ."
            else: # Uninhibited
                $ RogueX.FaceChange("sad")
                $ RogueX.Mouth = "smile"
                ch_r "I guess it could be fun with a partner. . ."

    elif Approval:
            #Second time+ dialog
            if RogueX.Forced:
                $ RogueX.FaceChange("sad")
                $ RogueX.Statup("Love", 70, -3, 1)
                $ RogueX.Statup("Love", 20, -2, 1)
                ch_r "The toys again?"
            elif not Taboo and "tabno" in RogueX.DailyActions:
                ch_r "Well, at least you got us some privacy this time. . ."
            elif "dildo pussy" in RogueX.RecentActions:
                $ RogueX.FaceChange("sexy", 1)
                ch_r "Mmm, again? Ok, let's get to it."
                jump Rogue_DP_Prep
            elif "dildo pussy" in RogueX.DailyActions:
                $ RogueX.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Breaking out the toys again?",
                    "Didn't get enough earlier?",
                    "You're going to wear me out."])
                ch_r "[Line]"
            elif RogueX.DildoP < 3:
                $ RogueX.FaceChange("sexy", 1)
                $ RogueX.Brows = "confused"
                $ RogueX.Mouth = "kiss"
                ch_r "You want to stick it in my pussy again?"
            else:
                $ RogueX.FaceChange("sexy", 1)
                $ RogueX.ArmPose = 2
                $ Line = renpy.random.choice(["You want some of this action?",
                    "So you'd like another go?",
                    "You want to stick it in my pussy again?",
                    "You want me ta lube up your toy?"])
                ch_r "[Line]"
                $ Line = 0

    if Approval >= 2:
            #She's into it. . .
            if RogueX.Forced:
                $ RogueX.FaceChange("sad")
                $ RogueX.Statup("Obed", 90, 1)
                $ RogueX.Statup("Inbt", 60, 1)
                ch_r "Ok, fine."
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
            jump Rogue_DP_Prep

    else:
            #She's not into it, but maybe. . .
            $ RogueX.FaceChange("angry")
            if "no dildo" in RogueX.RecentActions:
                ch_r "What part of \"no,\" did you not get, [RogueX.Petname]?"
            elif Taboo and "tabno" in RogueX.DailyActions and "no dildo" in RogueX.DailyActions:
                ch_r "Stop swinging that thing around in public!"
            elif "no dildo" in RogueX.DailyActions:
                ch_r "I already told you \"no,\" [RogueX.Petname]."
            elif Taboo and "tabno" in RogueX.DailyActions:
                ch_r "Stop swinging that thing around in public!"
            elif not RogueX.DildoP:
                $ RogueX.FaceChange("bemused")
                ch_r "I'm just not into toys, [RogueX.Petname]. . ."
            else:
                $ RogueX.FaceChange("bemused")
                ch_r "I don't think we need any toys, [RogueX.Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in RogueX.DailyActions:
                    $ RogueX.FaceChange("bemused")
                    ch_r "Yeah, ok, [RogueX.Petname]."
                    return
                "Maybe later?" if "no dildo" not in RogueX.DailyActions:
                    $ RogueX.FaceChange("sexy")
                    ch_r "Maybe I'll practice on my own time, [RogueX.Petname]."
                    $ RogueX.Statup("Love", 80, 2)
                    $ RogueX.Statup("Inbt", 70, 2)
                    if Taboo:
                        $ RogueX.RecentActions.append("tabno")
                        $ RogueX.DailyActions.append("tabno")
                    $ RogueX.RecentActions.append("no dildo")
                    $ RogueX.DailyActions.append("no dildo")
                    return
                "I think you'd like it. . .":
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
                        jump Rogue_DP_Prep
                    else:
                        pass

                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck(RogueX, 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                    if Approval > 1 or (Approval and RogueX.Forced):
                        $ RogueX.FaceChange("sad")
                        $ RogueX.Statup("Love", 70, -5, 1)
                        $ RogueX.Statup("Love", 200, -5)
                        ch_r "Ok, fine. If we're going to do this, stick it in already."
                        $ RogueX.Statup("Obed", 80, 4)
                        $ RogueX.Statup("Inbt", 80, 1)
                        $ RogueX.Statup("Inbt", 60, 3)
                        $ RogueX.Forced = 1
                        jump Rogue_DP_Prep
                    else:
                        $ RogueX.Statup("Love", 200, -20)
                        $ RogueX.RecentActions.append("angry")
                        $ RogueX.DailyActions.append("angry")

    #She refused all offers.
    $ RogueX.ArmPose = 1
    if "no dildo" in RogueX.DailyActions:
            ch_r "Learn to take \"no\" for an answer, [RogueX.Petname]."
            $ RogueX.RecentActions.append("angry")
            $ RogueX.DailyActions.append("angry")
    elif RogueX.Forced:
            $ RogueX.FaceChange("angry", 1)
            ch_r "I'm not going to let you use that on me."
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
            ch_r "Not here!"
            $ RogueX.Statup("Lust", 200, 5)
            $ RogueX.Statup("Obed", 50, -3)
    elif RogueX.DildoP:
            $ RogueX.FaceChange("sad")
            ch_r "Sorry, you can keep your toys to yourself."
    else:
            $ RogueX.FaceChange("normal", 1)
            ch_r "No way."
    $ RogueX.RecentActions.append("no dildo")
    $ RogueX.DailyActions.append("no dildo")
    $ temp_modifier = 0
    return

label Rogue_DP_Prep: #Animation set-up
    if Trigger2 == "dildo pussy":
        return

    if not RogueX.Forced and Situation != "auto":
        $ temp_modifier = 15 if RogueX.PantsNum() > 6 else 0
        call Bottoms_Off(RogueX)
        if "angry" in RogueX.RecentActions:
            return

    $ temp_modifier = 0
    call Rogue_Pussy_Launch("dildo pussy")
    if not RogueX.DildoP:
        if RogueX.Forced:
            $ RogueX.Statup("Love", 90, -75)
            $ RogueX.Statup("Obed", 70, 60)
            $ RogueX.Statup("Inbt", 80, 35)
        else:
            $ RogueX.Statup("Love", 90, 10)
            $ RogueX.Statup("Obed", 70, 20)
            $ RogueX.Statup("Inbt", 80, 45)
    if Taboo:
        $ RogueX.Inbt += int(Taboo/10)
        $ RogueX.Lust += int(Taboo/5)


    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ RogueX.DrainWord("tabno")
    $ RogueX.DrainWord("no dildo")
    $ RogueX.RecentActions.append("dildo pussy")
    $ RogueX.DailyActions.append("dildo pussy")

label Rogue_DP_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(RogueX)
        call ViewShift(RogueX,RogueX.Pose,0)
        $ RogueX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                call Slap_Ass(RogueX)
                                jump Rogue_DP_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0

                        "View":
                                    call ViewShift(RogueX,"menu")
                                    jump Rogue_DP_Cycle

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
                                                        "I want to stick a finger in her ass.":
                                                                $ Situation = "shift"
                                                                call Rogue_DP_After
                                                                call Rogue_Insert_Ass
                                                        "Just stick a finger in her ass without asking.":
                                                                $ Situation = "auto"
                                                                call Rogue_DP_After
                                                                call Rogue_Insert_Ass
                                                        "I want to shift the dildo to her ass.":
                                                                $ Situation = "shift"
                                                                call Rogue_DP_After
                                                                call Rogue_Dildo_Ass
                                                        "Never Mind":
                                                                jump Rogue_DP_Cycle
                                            else:
                                                call Sex_Basic_Dialog(RogueX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Rogue_DP_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
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
                                                        jump Rogue_DP_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Rogue_DP_Cycle
                                            "Never mind":
                                                        jump Rogue_DP_Cycle
                                    "Undress [RogueX.Name]":
                                            call Girl_Undress(RogueX)
                                    "Clean up [RogueX.Name] (locked)" if not RogueX.Spunk:
                                            pass
                                    "Clean up [RogueX.Name]" if RogueX.Spunk:
                                            call Girl_Cleanup(RogueX,"ask")
                                    "Never mind":
                                            jump Rogue_DP_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Rogue_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Rogue_DP_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Rogue_Pos_Reset
                                    $ Line = 0
                                    jump Rogue_DP_After
        #End menu (if Line)

        if RogueX.Panties or RogueX.PantsNum() > 6 or RogueX.HoseNum() >= 5: #This checks if Rogue wants to strip down.
                call Girl_Undress(RogueX,"auto")

        call Shift_Focus(RogueX)
        call Sex_Dialog(RogueX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or RogueX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(RogueX)
                            if "angry" in RogueX.RecentActions:
                                call Rogue_Pos_Reset
                                return
                            $ RogueX.Statup("Lust", 200, 5)
                            if 100 > RogueX.Lust >= 70 and RogueX.OCount < 2:
                                $ RogueX.RecentActions.append("unsatisfied")
                                $ RogueX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Rogue_DP_After
                            $ Line = "came"

                    if RogueX.Lust >= 100:
                            #If Rogue can cum
                            call Girl_Cumming(RogueX)
                            if Situation == "shift" or "angry" in RogueX.RecentActions:
                                jump Rogue_DP_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in RogueX.RecentActions:#And Rogue is unsatisfied,
                                "[RogueX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Rogue_DP_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif Cnt == (5 + RogueX.DildoA):
                    $ RogueX.Brows = "confused"
                    ch_r "What are you even doing down there?"
        elif RogueX.Lust >= 80:
                    pass
        elif Cnt == (15 + RogueX.DildoA) and RogueX.SEXP >= 15 and not ApprovalCheck(RogueX, 1500):
                    $ RogueX.Brows = "confused"
                    menu:
                        ch_r "[RogueX.Petname], this is getting uncomfortable, maybe we could try something else."
                        "Finish up.":
                                "You let go. . ."
                                jump Rogue_DP_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Rogue_DP_After
                        "No, this is fun.":
                                if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):
                                    $ RogueX.Statup("Love", 200, -5)
                                    $ RogueX.Statup("Obed", 50, 3)
                                    $ RogueX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ RogueX.FaceChange("angry", 1)
                                    call Rogue_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_r "Well if that's your attitude, I don't need your \"help\"."
                                    $ RogueX.Statup("Love", 50, -3, 1)
                                    $ RogueX.Statup("Love", 80, -4, 1)
                                    $ RogueX.Statup("Obed", 30, -1, 1)
                                    $ RogueX.Statup("Obed", 50, -1, 1)
                                    $ RogueX.RecentActions.append("angry")
                                    $ RogueX.DailyActions.append("angry")
                                    jump Rogue_DP_After
        #End Count check

        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ RogueX.FaceChange("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.Petname], that's enough of that for now."

label Rogue_DP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Rogue_Pos_Reset

    $ RogueX.FaceChange("sexy")

    $ RogueX.DildoP += 1
    $ RogueX.Action -=1

    call Partner_Like(RogueX,2)

    if RogueX.DildoP == 1:
            $ RogueX.SEXP += 10
            if not Situation:
                if RogueX.Love >= 500 and "unsatisfied" not in RogueX.RecentActions:
                    ch_r "Well I liked that. . ."
                elif RogueX.Obed <= 500 and Player.Focus <= 20:
                    $ RogueX.FaceChange("perplexed", 1)
                    ch_r "Did you like that?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_r "Mmm, so what else did you have in mind?"
    call Checkout
    return

# end RogueX.Dildo Pussy /////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////Start Insert Ass

label Rogue_Dildo_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(RogueX)
    call Rogue_Dildo_Check
    if not _return:
        return

    if RogueX.Loose:
        $ temp_modifier += 30
    elif "anal" in RogueX.RecentActions or "dildo anal" in RogueX.RecentActions:
        $ temp_modifier -= 20
    elif "anal" in RogueX.DailyActions or "dildo anal" in RogueX.DailyActions:
        $ temp_modifier -= 10
    elif (RogueX.Anal + RogueX.DildoA + RogueX.Plug) > 0: #You've done it before
        $ temp_modifier += 20

    if RogueX.PantsNum() > 6: # she's got pants on.
        $ temp_modifier -= 20

    if RogueX.Lust > 95:
        $ temp_modifier += 20
    elif RogueX.Lust > 85: #She's really horny
        $ temp_modifier += 15

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

    if "no dildo" in RogueX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no dildo" in RogueX.RecentActions else 0

    $ Approval = ApprovalCheck(RogueX, 1450, TabM = 4) # 145, 160, 175, Taboo -160(355)

    if Situation == RogueX:
            #Rogue auto-starts
            if Approval > 2:                                                      # fix, add rogue auto stuff here
                if RogueX.PantsNum() == 5:
                    "[RogueX.Name] grabs her dildo, hiking up her skirt as she does."
                    $ RogueX.Upskirt = 1
                elif RogueX.PantsNum() > 6:
                    "[RogueX.Name] grabs her dildo, pulling down her pants as she does."
                    $ RogueX.Legs = 0
                else:
                    "[RogueX.Name] grabs her dildo, rubbing is suggestively against her ass."
                $ RogueX.SeenPanties = 1
                "She slides the tip against her asshole, and seems to want you to insert it."
                menu:
                    "What do you do?"
                    "Nothing.":
                        $ RogueX.Statup("Inbt", 80, 3)
                        $ RogueX.Statup("Inbt", 50, 2)
                        "[RogueX.Name] slides it in."
                    "Go for it.":
                        $ RogueX.FaceChange("sexy", 1)
                        $ RogueX.Statup("Inbt", 80, 3)
                        ch_p "Oh yeah, [RogueX.Pet], let's do this."
                        $ RogueX.NameCheck() #checks reaction to petname
                        "You grab the dildo and slide it in."
                        $ RogueX.Statup("Love", 85, 1)
                        $ RogueX.Statup("Obed", 90, 1)
                        $ RogueX.Statup("Obed", 50, 2)
                    "Ask her to stop.":
                        $ RogueX.FaceChange("surprised")
                        $ RogueX.Statup("Inbt", 70, 1)
                        ch_p "Let's not do that right now, [RogueX.Pet]."
                        $ RogueX.NameCheck() #checks reaction to petname
                        "[RogueX.Name] sets the dildo down."
                        $ RogueX.Statup("Obed", 90, 1)
                        $ RogueX.Statup("Obed", 50, 1)
                        $ RogueX.Statup("Obed", 30, 2)
                        return
                jump Rogue_DA_Prep
            else:
                $ temp_modifier = 0                               # fix, add rogue auto stuff here
                $ Trigger2 = 0
            return

    if Situation == "auto":
            "You rub the dildo across her body, and against her tight anus."
            $ RogueX.FaceChange("surprised", 1)

            if (RogueX.DildoA and Approval) or (Approval > 1):
                #this is not the first time you've had sex, or she's into it
                "[RogueX.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                $ RogueX.FaceChange("sexy")
                $ RogueX.Statup("Obed", 70, 3)
                $ RogueX.Statup("Inbt", 50, 3)
                $ RogueX.Statup("Inbt", 70, 1)
                ch_r "Ok, [RogueX.Petname], let's do this."
                jump Rogue_DA_Prep
            else:
                #she's questioning it
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
                            jump Rogue_DA_Prep
                        "You pull back before you really get it in."
                        $ RogueX.FaceChange("bemused", 1)
                        if RogueX.DildoA:
                            ch_r "Well ok, [RogueX.Petname], no harm done. Just give me a little warning next time."
                        else:
                            ch_r "Well ok, [RogueX.Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."
                    "Just playing with my favorite toys.":
                        $ RogueX.Statup("Love", 80, -10, 1)
                        $ RogueX.Statup("Love", 200, -10)
                        "You press it inside some more."
                        $ RogueX.Statup("Obed", 70, 3)
                        $ RogueX.Statup("Inbt", 50, 3)
                        if not ApprovalCheck(RogueX, 700, "O", TabM=1): #Checks if Obed is 700+
                            $ RogueX.FaceChange("angry")
                            "[RogueX.Name] shoves you away and slaps you in the face."
                            ch_r "Jackass!"
                            ch_r "If that's how you want to treat me, we're done here!"
                            $ RogueX.Statup("Love", 50, -10, 1)
                            $ RogueX.Statup("Obed", 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            if renpy.showing("Rogue_Doggy"):
                                call Rogue_Doggy_Reset
                            $ RogueX.RecentActions.append("angry")
                            $ RogueX.DailyActions.append("angry")
                        else:
                            $ RogueX.FaceChange("sad")
                            "[RogueX.Name] doesn't seem to be into this, you're lucky she's so obedient."
                            jump Rogue_DA_Prep
            return
    #end auto

    if not RogueX.DildoA:
            #first time
            $ RogueX.FaceChange("surprised", 1)
            $ RogueX.Mouth = "kiss"
            ch_r "Hmmm, so you'd like to try out some toys?"
            if RogueX.Forced:
                $ RogueX.FaceChange("sad")
                ch_r "You had to go for the butt, uh?"

    if not RogueX.Loose and ("dildo anal" in RogueX.RecentActions or "anal" in RogueX.RecentActions or "dildo anal" in RogueX.DailyActions or "anal" in RogueX.DailyActions):
            $ RogueX.FaceChange("bemused", 1)
            ch_r "I'm still a bit sore from earlier. . ."

    if not RogueX.DildoA and Approval:
            #First time dialog
            if RogueX.Forced:
                $ RogueX.FaceChange("sad")
                $ RogueX.Statup("Love", 70, -3, 1)
                $ RogueX.Statup("Love", 20, -2, 1)
            elif RogueX.Love >= (RogueX.Obed + RogueX.Inbt):
                $ RogueX.FaceChange("sexy")
                $ RogueX.Brows = "sad"
                $ RogueX.Mouth = "smile"
                ch_r "I haven't actually used one of these, back there before. . ."
            elif RogueX.Obed >= RogueX.Inbt:
                $ RogueX.FaceChange("normal")
                ch_r "If that's what you want, [RogueX.Petname]. . ."
            else: # Uninhibited
                $ RogueX.FaceChange("sad")
                $ RogueX.Mouth = "smile"
                ch_r "I guess it could be fun with a partner. . ."

    elif Approval:
            #Second time+ dialog
            if RogueX.Forced:
                $ RogueX.FaceChange("sad")
                $ RogueX.Statup("Love", 70, -3, 1)
                $ RogueX.Statup("Love", 20, -2, 1)
                ch_r "The toys again?"
            elif not Taboo and "tabno" in RogueX.DailyActions:
                ch_r "Well, at least you got us some privacy this time. . ."
            elif "dildo anal" in RogueX.DailyActions and not RogueX.Loose:
                pass
            elif "dildo anal" in RogueX.DailyActions:
                $ RogueX.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Breaking out the toys again?",
                    "Didn't get enough earlier?",
                    "I'm still a bit sore from earlier.",
                    "You're going to wear me out."])
                ch_r "[Line]"
            elif RogueX.DildoA < 3:
                $ RogueX.FaceChange("sexy", 1)
                $ RogueX.Brows = "confused"
                $ RogueX.Mouth = "kiss"
                ch_r "You want to stick it in my ass again?"
            else:
                $ RogueX.FaceChange("sexy", 1)
                $ RogueX.ArmPose = 2
                $ Line = renpy.random.choice(["You want some of this action?",
                    "So you'd like another go?",
                    "You want to stick it in my ass again?",
                    "You want me ta lube up your toy?"])
                ch_r "[Line]"
                $ Line = 0

    if Approval >= 2:
            #She's into it. . .
            if RogueX.Forced:
                $ RogueX.FaceChange("sad")
                $ RogueX.Statup("Obed", 90, 1)
                $ RogueX.Statup("Inbt", 60, 1)
                ch_r "Ok, fine."
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
            jump Rogue_DA_Prep

    else:
            #She's not into it, but maybe. . .
            $ RogueX.FaceChange("angry")
            if "no dildo" in RogueX.RecentActions:
                ch_r "What part of \"no,\" did you not get, [RogueX.Petname]?"
            elif Taboo and "tabno" in RogueX.DailyActions and "no dildo" in RogueX.DailyActions:
                ch_r "Stop swinging that thing around in public!"
            elif "no dildo" in RogueX.DailyActions:
                ch_r "I already told you \"no,\" [RogueX.Petname]."
            elif Taboo and "tabno" in RogueX.DailyActions:
                ch_r "I already told you that I wouldn't do that out here!"
            elif not RogueX.DildoA:
                $ RogueX.FaceChange("bemused")
                ch_r "I'm just not into toys, [RogueX.Petname]. . ."
            elif not RogueX.Loose and "dildo anal" not in RogueX.DailyActions:
                $ RogueX.FaceChange("perplexed")
                ch_r "You could have been a bit more gentle last time, [RogueX.Petname]. . ."
            else:
                $ RogueX.FaceChange("bemused")
                ch_r "I don't think we need any toys, [RogueX.Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in RogueX.DailyActions:
                    $ RogueX.FaceChange("bemused")
                    ch_r "Yeah, ok, [RogueX.Petname]."
                    return
                "Maybe later?" if "no dildo" not in RogueX.DailyActions:
                    $ RogueX.FaceChange("sexy")
                    ch_r "Maybe I'll practice on my own time, [RogueX.Petname]."
                    $ RogueX.Statup("Love", 80, 2)
                    $ RogueX.Statup("Inbt", 70, 2)
                    if Taboo:
                        $ RogueX.RecentActions.append("tabno")
                        $ RogueX.DailyActions.append("tabno")
                    $ RogueX.RecentActions.append("no dildo")
                    $ RogueX.DailyActions.append("no dildo")
                    return
                "I think you'd like it. . .":
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
                        jump Rogue_DA_Prep
                    else:
                        pass

                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck(RogueX, 1050, "OI", TabM = 3) # 105, 120, 135, -120(225)
                    if Approval > 1 or (Approval and RogueX.Forced):
                        $ RogueX.FaceChange("sad")
                        $ RogueX.Statup("Love", 70, -5, 1)
                        $ RogueX.Statup("Love", 200, -5)
                        ch_r "Ok, fine. If we're going to do this, stick it in already."
                        $ RogueX.Statup("Obed", 80, 4)
                        $ RogueX.Statup("Inbt", 80, 1)
                        $ RogueX.Statup("Inbt", 60, 3)
                        $ RogueX.Forced = 1
                        jump Rogue_DA_Prep
                    else:
                        $ RogueX.Statup("Love", 200, -20)
                        $ RogueX.RecentActions.append("angry")
                        $ RogueX.DailyActions.append("angry")

    #She refused all offers.
    $ RogueX.ArmPose = 1
    if "no dildo" in RogueX.DailyActions:
            ch_r "Learn to take \"no\" for an answer, [RogueX.Petname]."
            $ RogueX.RecentActions.append("angry")
            $ RogueX.DailyActions.append("angry")
    elif RogueX.Forced:
            $ RogueX.FaceChange("angry", 1)
            ch_r "I'm not going to let you use that on me."
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
            ch_r "Not here!"
            $ RogueX.Statup("Lust", 200, 5)
            $ RogueX.Statup("Obed", 50, -3)
    elif not RogueX.Loose and "dildo anal" in RogueX.DailyActions:
            $ RogueX.FaceChange("bemused")
            ch_r "Sorry, I just need a little break back there, [RogueX.Petname]."
    elif RogueX.DildoA:
            $ RogueX.FaceChange("sad")
            ch_r "Sorry, you can keep your toys out of there."
    else:
            $ RogueX.FaceChange("normal", 1)
            ch_r "No way."
    $ RogueX.RecentActions.append("no dildo")
    $ RogueX.DailyActions.append("no dildo")
    $ temp_modifier = 0
    return

label Rogue_DA_Prep: #Animation set-up
    if Trigger2 == "dildo anal":
        return

    if not RogueX.Forced and Situation != "auto":
        $ temp_modifier = 20 if RogueX.PantsNum() > 6 else 0
        call Bottoms_Off(RogueX)
        if "angry" in RogueX.RecentActions:
            return

    $ temp_modifier = 0
    call Rogue_Pussy_Launch("dildo anal")
    if not RogueX.DildoA:
        if RogueX.Forced:
            $ RogueX.Statup("Love", 90, -75)
            $ RogueX.Statup("Obed", 70, 60)
            $ RogueX.Statup("Inbt", 80, 35)
        else:
            $ RogueX.Statup("Love", 90, 10)
            $ RogueX.Statup("Obed", 70, 20)
            $ RogueX.Statup("Inbt", 80, 45)
    if Taboo:
        $ RogueX.Inbt += int(Taboo/10)
        $ RogueX.Lust += int(Taboo/5)


    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ RogueX.DrainWord("tabno")
    $ RogueX.DrainWord("no dildo")
    $ RogueX.RecentActions.append("dildo anal")
    $ RogueX.DailyActions.append("dildo anal")

label Rogue_DA_Cycle: #Repeating strokes
    while Round > 0:
        call ViewShift(RogueX,RogueX.Pose,0)
        call Shift_Focus(RogueX)
        $ RogueX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                call Slap_Ass(RogueX)
                                jump Rogue_DA_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0

                        "View":
                                    call ViewShift(RogueX,"menu")
                                    jump Rogue_DA_Cycle

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
                                                        "I want to stick a finger in her pussy.":
                                                                $ Situation = "shift"
                                                                call Rogue_DA_After
                                                                call Rogue_Fondle_Pussy
                                                        "Just stick a finger in her pussy without asking.":
                                                                $ Situation = "auto"
                                                                call Rogue_DA_After
                                                                call Rogue_Fondle_Pussy
                                                        "I want to shift the dildo to her pussy.":
                                                                $ Situation = "shift"
                                                                call Rogue_DA_After
                                                                call Rogue_Dildo_Pussy
                                                        "Never Mind":
                                                                jump Rogue_DA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(RogueX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Rogue_DA_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
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
                                                        jump Rogue_DA_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Rogue_DA_Cycle
                                            "Never mind":
                                                        jump Rogue_DA_Cycle
                                    "Undress [RogueX.Name]":
                                            call Girl_Undress(RogueX)
                                    "Clean up [RogueX.Name] (locked)" if not RogueX.Spunk:
                                            pass
                                    "Clean up [RogueX.Name]" if RogueX.Spunk:
                                            call Girl_Cleanup(RogueX,"ask")
                                    "Never mind":
                                            jump Rogue_DA_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Rogue_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Rogue_DA_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Rogue_Pos_Reset
                                    $ Line = 0
                                    jump Rogue_DA_After
        #End menu (if Line)

        if RogueX.Panties or RogueX.PantsNum() > 6 or RogueX.HoseNum() >= 5: #This checks if Rogue wants to strip down.
                call Girl_Undress(RogueX,"auto")

        call Shift_Focus(RogueX)
        call Sex_Dialog(RogueX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or RogueX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(RogueX)
                            if "angry" in RogueX.RecentActions:
                                call Rogue_Pos_Reset
                                return
                            $ RogueX.Statup("Lust", 200, 5)
                            if 100 > RogueX.Lust >= 70 and RogueX.OCount < 2:
                                $ RogueX.RecentActions.append("unsatisfied")
                                $ RogueX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Rogue_DA_After
                            $ Line = "came"

                    if RogueX.Lust >= 100:
                            #If Rogue can cum
                            call Girl_Cumming(RogueX)
                            if Situation == "shift" or "angry" in RogueX.RecentActions:
                                jump Rogue_DA_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in RogueX.RecentActions:#And Rogue is unsatisfied,
                                "[RogueX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Rogue_DA_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif Cnt == (5 + RogueX.DildoA):
                    $ RogueX.Brows = "confused"
                    ch_r "What are you even doing down there?"
        elif RogueX.Lust >= 80:
                    pass
        elif Cnt == (15 + RogueX.DildoA) and RogueX.SEXP >= 15 and not ApprovalCheck(RogueX, 1500):
                    $ RogueX.Brows = "confused"
                    menu:
                        ch_r "[RogueX.Petname], this is getting uncomfortable, maybe we could try something else."
                        "Finish up.":
                                "You let go. . ."
                                jump Rogue_DA_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Rogue_DA_After
                        "No, this is fun.":
                                if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):
                                    $ RogueX.Statup("Love", 200, -5)
                                    $ RogueX.Statup("Obed", 50, 3)
                                    $ RogueX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ RogueX.FaceChange("angry", 1)
                                    call Rogue_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_r "Well if that's your attitude, I don't need your \"help\"."
                                    $ RogueX.Statup("Love", 50, -3, 1)
                                    $ RogueX.Statup("Love", 80, -4, 1)
                                    $ RogueX.Statup("Obed", 30, -1, 1)
                                    $ RogueX.Statup("Obed", 50, -1, 1)
                                    $ RogueX.RecentActions.append("angry")
                                    $ RogueX.DailyActions.append("angry")
                                    jump Rogue_DA_After
        #End Count check

        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ RogueX.FaceChange("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.Petname], that's enough of that for now."


label Rogue_DA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Rogue_Pos_Reset

    $ RogueX.FaceChange("sexy")

    $ RogueX.DildoA += 1
    $ RogueX.Action -=1

    call Partner_Like(RogueX,2)

    if RogueX.DildoA == 1:
            $ RogueX.SEXP += 10
            if not Situation:
                if RogueX.Love >= 500 and "unsatisfied" not in RogueX.RecentActions:
                    if RogueX.Loose:
                        ch_r "Well I liked that. . ."
                    else:
                        ch_r "Well that was a bit rough. . ."
                elif RogueX.Obed <= 500 and Player.Focus <= 20:
                    $ RogueX.FaceChange("perplexed", 1)
                    ch_r "Did you like that?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_r "Mmm, so what else did you have in mind?"
    call Checkout
    return

# end RogueX.Dildo Ass /////////////////////////////////////////////////////////////////////////////

label Rogue_Vibrator_Check:                                                                                 #fix this whole section is copy/paste unfinished
    if "vibrator" in Player.Inventory:
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in RogueX.Inventory:
        "You ask [RogueX.Name] to get out her vibrator."
    else:
        "You don't have one of those on you."
        return 0
    return 1



## RogueX.Footjob //////////////////////////////////////////////////////////////////////
label Rogue_Footjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(RogueX)
    if RogueX.Foot >= 7: # She loves it
        $ temp_modifier += 10
    elif RogueX.Foot >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif RogueX.Foot: #You've done it before
        $ temp_modifier += 3

    if RogueX.Addict >= 75 and RogueX.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 10
    if RogueX.Addict >= 75:
        $ temp_modifier += 5

    if Situation == "shift":
        $ temp_modifier += 15
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

    if "no foot" in RogueX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no foot" in RogueX.RecentActions else 0

    $ Approval = ApprovalCheck(RogueX, 1250, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if Situation == RogueX:                                                                  #Rogue auto-starts
        if Approval > 2:                                                      # fix, add rogue auto stuff here
            "[RogueX.Name] leans forward and starts rubbing your cock between her feet."
            menu:
                "What do you do?"
                "Nothing.":
                    $ RogueX.Statup("Inbt", 70, 3)
                    $ RogueX.Statup("Inbt", 30, 2)
                    "[RogueX.Name] continues her actions."
                "Praise her.":
                    $ RogueX.FaceChange("sexy", 1)
                    $ RogueX.Statup("Inbt", 70, 3)
                    ch_p "Oooh, that's good, [RogueX.Pet]."
                    $ RogueX.NameCheck() #checks reaction to petname
                    "[RogueX.Name] continues her actions."
                    $ RogueX.Statup("Love", 80, 1)
                    $ RogueX.Statup("Obed", 90, 1)
                    $ RogueX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ RogueX.FaceChange("surprised")
                    $ RogueX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [RogueX.Pet]."
                    $ RogueX.NameCheck() #checks reaction to petname
                    "[RogueX.Name] puts it down."
                    $ RogueX.Statup("Obed", 90, 1)
                    $ RogueX.Statup("Obed", 50, 1)
                    $ RogueX.Statup("Obed", 30, 2)
                    return
            if Trigger:
                $ Trigger3 = "foot"
                return
            jump Rogue_FJ_Prep
        else:
            $ temp_modifier = 0                               # fix, add rogue auto stuff here
            $ Trigger2 = 0
            return

    if not RogueX.Foot and "no foot" not in RogueX.RecentActions:
        $ RogueX.FaceChange("confused", 2)
        ch_r "Huh, so like a handy, but with my feet?"
        $ RogueX.Blush = 1

    if not RogueX.Foot and Approval:                                                 #First time dialog
        if RogueX.Forced:
            $ RogueX.FaceChange("sad",1)
            $ RogueX.Statup("Love", 70, -3, 1)
            $ RogueX.Statup("Love", 20, -2, 1)
        elif RogueX.Love >= (RogueX.Obed + RogueX.Inbt):
            $ RogueX.FaceChange("sexy",1)
            $ RogueX.Brows = "sad"
            $ RogueX.Mouth = "smile"
            ch_r "If that's what you like. . ."
        elif RogueX.Obed >= RogueX.Inbt:
            $ RogueX.FaceChange("normal",1)
            ch_r "If that's what you want, [RogueX.Petname]. . ."
        elif RogueX.Addict >= 50:
            $ RogueX.FaceChange("manic", 1)
            ch_r "I guess. . ."
        else: # Uninhibited
            $ RogueX.FaceChange("lipbite",1)
            ch_r "Sure. . ."

    elif Approval:                                                                       #Second time+ dialog
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Love", 70, -3, 1)
            $ RogueX.Statup("Love", 20, -2, 1)
            ch_r "That's it?"
        elif not Taboo and "tabno" in RogueX.DailyActions:
            ch_r "I guess here would be ok. . ."
        elif "foot" in RogueX.RecentActions:
            $ RogueX.FaceChange("sexy", 1)
            ch_r "I don't want to wear them out. . ."
            jump Rogue_FJ_Prep
        elif "foot" in RogueX.DailyActions:
            $ RogueX.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Another one?",
                "You're going to give me calluses.",
                "Didn't get enough earlier?",
                "My feet are a bit sore from earlier.",
                "My feet are kinda sore from earlier."])
            ch_r "[Line]"
        elif RogueX.Foot < 3:
            $ RogueX.FaceChange("sexy", 1)
            $ RogueX.Brows = "confused"
            $ RogueX.Mouth = "kiss"
            ch_r "Again?"
        else:
            $ RogueX.FaceChange("sexy", 1)
            $ RogueX.ArmPose = 2
            $ Line = renpy.random.choice(["You want me to use my feet?",
                "So you'd like another foot rub?",
                "So you'd like me to. . . [she rubs her foot along your leg]?",
                "So you'd like another foot rub?"])
            ch_r "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if RogueX.Forced:
            $ RogueX.FaceChange("sad")
            $ RogueX.Statup("Obed", 90, 1)
            $ RogueX.Statup("Inbt", 60, 1)
            ch_r ". . . Ok, if that's what you want."
        elif "no foot" in RogueX.DailyActions:
            ch_r "Fine!"
        else:
            $ RogueX.FaceChange("sexy", 1)
            $ RogueX.Statup("Love", 90, 1)
            $ RogueX.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Sure, I guess.",
                "Okay.",
                "Ok, lemme see it.",
                "I guess. . .",
                "Ok. . . [She gestures for you to come over].",
                "Heh, ok, fine."])
            ch_r "[Line]"
            $ Line = 0
        $ RogueX.Statup("Obed", 20, 1)
        $ RogueX.Statup("Obed", 60, 1)
        $ RogueX.Statup("Inbt", 70, 2)
        jump Rogue_FJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ RogueX.FaceChange("angry")
        if "no foot" in RogueX.RecentActions:
            ch_r "I just said \"no,\" [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions and "no foot" in RogueX.DailyActions:
            ch_r "Not in public!"
        elif "no foot" in RogueX.DailyActions:
            ch_r "I told you \"no\" earlier [RogueX.Petname]."
        elif Taboo and "tabno" in RogueX.DailyActions:
            ch_r "I said not in public!"
        elif not RogueX.Foot:
            $ RogueX.FaceChange("bemused")
            ch_r ". . . well I don't know about that, [RogueX.Petname]. . ."
        else:
            $ RogueX.FaceChange("bemused")
            ch_r "Maybe not right now, ok?"
        menu:
            extend ""
            "Sorry, never mind." if "no foot" in RogueX.DailyActions:
                $ RogueX.FaceChange("bemused")
                ch_r "No problem."
                return
            "Maybe later?" if "no foot" not in RogueX.DailyActions:
                $ RogueX.FaceChange("sexy")
                ch_r ". . ."
                ch_r "I guess?"
                $ RogueX.Statup("Love", 80, 2)
                $ RogueX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ RogueX.RecentActions.append("tabno")
                    $ RogueX.DailyActions.append("tabno")
                $ RogueX.RecentActions.append("no foot")
                $ RogueX.DailyActions.append("no foot")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ RogueX.FaceChange("sexy")
                    $ RogueX.Statup("Obed", 90, 2)
                    $ RogueX.Statup("Obed", 50, 2)
                    $ RogueX.Statup("Inbt", 70, 3)
                    $ RogueX.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Sure, I guess.",
                        "Okay.",
                        "Ok, lemme see it.",
                        "I guess. . .",
                        "Ok. . . [She gestures for you to come over].",
                        "Heh, ok, fine."])
                    ch_r "[Line]"
                    $ Line = 0
                    jump Rogue_FJ_Prep
                else:
                    pass

            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck(RogueX, 400, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.FaceChange("sad")
                    $ RogueX.Statup("Love", 70, -5, 1)
                    $ RogueX.Statup("Love", 200, -2)
                    ch_r "Ok, fine."
                    $ RogueX.Statup("Obed", 50, 4)
                    $ RogueX.Statup("Inbt", 80, 1)
                    $ RogueX.Statup("Inbt", 60, 3)
                    $ RogueX.Forced = 1
                    jump Rogue_FJ_Prep
                else:
                    $ RogueX.Statup("Love", 200, -15)
                    $ RogueX.RecentActions.append("angry")
                    $ RogueX.DailyActions.append("angry")

    #She refused all offers.
    $ RogueX.ArmPose = 1
    if "no foot" in RogueX.DailyActions:
        $ RogueX.FaceChange("angry", 1)
        ch_r "I'aint tellin you again."
        $ RogueX.RecentActions.append("angry")
        $ RogueX.DailyActions.append("angry")
    elif RogueX.Forced:
        $ RogueX.FaceChange("angry", 1)
        ch_r "Not even with my feet."
        $ RogueX.Statup("Lust", 200, 5)
        if RogueX.Love > 300:
                $ RogueX.Statup("Love", 70, -2)
        $ RogueX.Statup("Obed", 50, -2)
        $ RogueX.RecentActions.append("angry")
        $ RogueX.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ RogueX.FaceChange("angry", 1)
        $ RogueX.DailyActions.append("tabno")
        ch_r "Not in such an exposed place, [RogueX.Petname]."
        $ RogueX.Statup("Lust", 200, 5)
        $ RogueX.Statup("Obed", 50, -3)
    elif RogueX.Foot:
        $ RogueX.FaceChange("sad")
        ch_r "Not right now, [RogueX.Petname]. . ."
    else:
        $ RogueX.FaceChange("normal", 1)
        ch_r "That isn't really how I planned to use my feet today"
    $ RogueX.RecentActions.append("no foot")
    $ RogueX.DailyActions.append("no foot")
    $ temp_modifier = 0
    return


label Rogue_FJ_Prep:
    if Trigger2 == "foot":
        return

    if Taboo:
        $ RogueX.Inbt += int(Taboo/10)
        $ RogueX.Lust += int(Taboo/5)

    $ RogueX.FaceChange("sexy")
    if RogueX.Forced:
        $ RogueX.FaceChange("sad")
    elif not RogueX.Foot:
        $ RogueX.Brows = "confused"
        $ RogueX.Eyes = "sexy"
        $ RogueX.Mouth = "smile"

    call Seen_First_Peen(RogueX,Partner,React=Situation)

    if not RogueX.Foot:
        if RogueX.Forced:
            $ RogueX.Statup("Love", 90, -20)
            $ RogueX.Statup("Obed", 70, 25)
            $ RogueX.Statup("Inbt", 80, 30)
        else:
            $ RogueX.Statup("Love", 90, 5)
            $ RogueX.Statup("Obed", 70, 20)
            $ RogueX.Statup("Inbt", 80, 20)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ RogueX.DrainWord("tabno")
    $ RogueX.DrainWord("no foot")
    $ RogueX.RecentActions.append("foot")
    $ RogueX.DailyActions.append("foot")
    call Rogue_Sex_Launch("foot")

label Rogue_FJ_Cycle:
    while Round > 0:
        call Rogue_Sex_Launch("foot")
        call Shift_Focus(RogueX)
        $ RogueX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass

                        "Start moving? . ." if not Speed:
                                    $ Speed = 1

                        "Speed up. . ." if Speed < 2:
                                    $ Speed = 2
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 2:
                                    pass

                        "Slow Down. . ." if Speed:
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:
                                    pass
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0

                        "Turn her Around":
                                    $ RogueX.Pose = "doggy" if RogueX.Pose != "doggy" else "sex"
                                    "You turn her around. . ."
                                    jump Rogue_FJ_Cycle

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
                                                        "How about a blowjob?":
                                                                    if RogueX.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Rogue_FJ_After
                                                                        call Rogue_Blowjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(RogueX,"tired")
                                                        "How about a handjob?":
                                                                    if RogueX.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Rogue_FJ_After
                                                                        call Rogue_Handjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(RogueX,"tired")

                                                        "How about a titjob?":
                                                                    if RogueX.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Rogue_FJ_After
                                                                        call Rogue_Titjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(RogueX,"tired")

                                                        "Never Mind":
                                                                jump Rogue_FJ_Cycle
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
                                                        jump Rogue_FJ_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Rogue_FJ_Cycle
                                            "Never mind":
                                                        jump Rogue_FJ_Cycle
                                    "Undress [RogueX.Name]":
                                            call Girl_Undress(RogueX)
                                    "Clean up [RogueX.Name] (locked)" if not RogueX.Spunk:
                                            pass
                                    "Clean up [RogueX.Name]" if RogueX.Spunk:
                                            call Girl_Cleanup(RogueX,"ask")
                                    "Never mind":
                                            jump Rogue_FJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Rogue_Doggy_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Rogue_FJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Rogue_Doggy_Reset
                                    $ Line = 0
                                    jump Rogue_FJ_After
        #End menu (if Line)

        call Shift_Focus(RogueX)
        call Sex_Dialog(RogueX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or RogueX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(RogueX)
                            if "angry" in RogueX.RecentActions:
                                call Rogue_Doggy_Reset
                                return
                            $ RogueX.Statup("Lust", 200, 5)
                            if 100 > RogueX.Lust >= 70 and RogueX.OCount < 2:
                                $ RogueX.RecentActions.append("unsatisfied")
                                $ RogueX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Rogue_FJ_After
                            $ Line = "came"

                    if RogueX.Lust >= 100:
                            #If Rogue can cum
                            call Girl_Cumming(RogueX)
                            if Situation == "shift" or "angry" in RogueX.RecentActions:
                                jump Rogue_FJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in RogueX.RecentActions:#And Rogue is unsatisfied,
                                "[RogueX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Rogue_FJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Cnt == 20:
                    $ RogueX.Brows = "angry"
                    menu:
                        ch_r "Ow, i'm not used to this. Mind if we take a break?"
                        "How about a BJ?" if RogueX.Action and MultiAction:
                                $ Situation = "shift"
                                call Rogue_FJ_After
                                call Rogue_Blowjob
                        "How about a Handy?" if RogueX.Action and MultiAction:
                                $ Situation = "shift"
                                call Rogue_FJ_After
                                call Rogue_Handjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump Rogue_FJ_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Rogue_Doggy_Reset
                                $ Situation = "shift"
                                jump Rogue_FJ_After
                        "No, get back down there.":
                                if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):
                                    $ RogueX.Statup("Love", 200, -5)
                                    $ RogueX.Statup("Obed", 50, 3)
                                    $ RogueX.Statup("Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    $ RogueX.FaceChange("angry", 1)
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_r "Well if that's your attitude you can handle your own business."
                                    $ RogueX.Statup("Love", 50, -3, 1)
                                    $ RogueX.Statup("Love", 80, -4, 1)
                                    $ RogueX.Statup("Obed", 30, -1, 1)
                                    $ RogueX.Statup("Obed", 50, -1, 1)
                                    $ RogueX.RecentActions.append("angry")
                                    $ RogueX.DailyActions.append("angry")
                                    jump Rogue_FJ_After
        elif Cnt == 10 and RogueX.SEXP <= 100 and not ApprovalCheck(RogueX, 1200, "LO"):
                    $ RogueX.Brows = "confused"
                    ch_r "Can we be done with this now? I'm getting sore."
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

label Rogue_FJ_After:
    $ RogueX.FaceChange("sexy")

    $ RogueX.Foot += 1
    $ RogueX.Action -=1
    $ RogueX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ RogueX.Addictionrate += 1
    $ RogueX.Statup("Lust", 90, 5)

    call Partner_Like(RogueX,1)

    if "Roguepedi" in Achievements:
            pass
    elif RogueX.Foot >= 10:
            $ RogueX.FaceChange("smile", 1)
            ch_r "I guess I've gotten used to this foot thing."
            $ Achievements.append("Roguepedi")
            $ RogueX.SEXP += 5
    elif RogueX.Foot == 1:
            $ RogueX.SEXP += 10
            if RogueX.Love >= 500:
                $ RogueX.Mouth = "smile"
                ch_r "That was a real interesting experience. . ."
            elif Player.Focus <= 20:
                $ RogueX.Mouth = "sad"
                ch_r "Did that work for you?"
    elif RogueX.Foot == 5:
                ch_r "I kinda like this sensation."
                ch_r "Never thought about touching people with my feet."

    $ temp_modifier = 0
    if Situation == "shift":
        ch_r "Mmm, so what else did you have in mind?"
    else:
        call Rogue_Doggy_Reset
    call Checkout
    return

## end RogueX.Footjob //////////////////////////////////////////////////////////////////////
