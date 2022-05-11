## JeanX.Handjob //////////////////////////////////////////////////////////////////////
label Jean_Handjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JeanX)
    if JeanX.Hand >= 7: # She loves it
        $ temp_modifier += 10
    elif JeanX.Hand >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif JeanX.Hand: #You've done it before
        $ temp_modifier += 3

    if JeanX.Addict >= 75 and JeanX.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 15
    if JeanX.Addict >= 75:
        $ temp_modifier += 5

    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in JeanX.Traits:
        $ temp_modifier += (3*Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JeanX.Traits:
        $ temp_modifier -= 40
    if JeanX.ForcedCount and not JeanX.Forced:
        $ temp_modifier -= 5 * JeanX.ForcedCount    

    if JeanX.Taboo and "tabno" in JeanX.DailyActions:
        $ temp_modifier -= 10

    if "no hand" in JeanX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no hand" in JeanX.RecentActions else 0

    $ Approval = ApprovalCheck(JeanX, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if not JeanX.Hand and "no hand" not in JeanX.RecentActions:
        $ JeanX.FaceChange("confused", 2)
        ch_j "You want a handjob, hmm. . ."
        $ JeanX.Blush = 1

    if not JeanX.Hand and Approval:                                                 #First time dialog
        if JeanX.Forced:
            $ JeanX.FaceChange("sad",1)
            $ JeanX.Statup("Love", 70, -3, 1)
            $ JeanX.Statup("Love", 20, -2, 1)
            ch_j ". . ."
        elif JeanX.Love >= (JeanX.Obed + JeanX.Inbt - JeanX.IX):
            $ JeanX.FaceChange("sexy",1)
            $ JeanX.Brows = "sad"
            $ JeanX.Mouth = "smile"
            ch_j "Well, I guess it wouldn't be so bad. . ."
        elif JeanX.Obed >= (JeanX.Inbt - JeanX.IX):
            $ JeanX.FaceChange("normal",1)
            ch_j "If you want, [JeanX.Petname]. . ."
        else: # Uninhibited
            $ JeanX.FaceChange("lipbite",1)
            ch_j "Hmm. . ."

    elif Approval:                                                                       #Second time+ dialog
        if JeanX.Forced:
            $ JeanX.FaceChange("sad")
            $ JeanX.Statup("Love", 70, -3, 1)
            $ JeanX.Statup("Love", 20, -2, 1)
            ch_j "And that's it?"
        elif not JeanX.Taboo and "tabno" in JeanX.DailyActions:
            ch_j "Well, I guess here might not be that bad. . ."
        elif "hand" in JeanX.RecentActions:
            $ JeanX.FaceChange("sexy", 1)
            ch_j "Well, I guess another wouldn't hurt. . ."
            jump Jean_HJ_Prep
        elif "hand" in JeanX.DailyActions:
            $ JeanX.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Another one?",
                "Didn't get enough earlier?",
                "Again the with handjobs, huh?",
                "I guess you want more."])
            ch_j "[Line]"
        elif JeanX.Hand < 3:
            $ JeanX.FaceChange("sexy", 1)
            $ JeanX.Brows = "confused"
            $ JeanX.Mouth = "kiss"
            ch_j "I guess you're getting used to these. . ."
        else:
            $ JeanX.FaceChange("sexy", 1)
            $ JeanX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some more?",
                "So you'd like another handjob?",
                "You want a. . . [fist pumping hand gestures]?",
                "Another handjob?"])
            ch_j "[Line]"
        $ Line = 0

    if ApprovalCheck(JeanX, 1000) and (Approval < 2 or "psysex" not in JeanX.History):
            #sees if you're up for psychic handy
            call Psychic_Sex(JeanX)

    if Approval >= 2:                                                                   #She's into it. . .
        if JeanX.Forced:
            $ JeanX.FaceChange("sad")
            $ JeanX.Statup("Obed", 90, 1)
            $ JeanX.Statup("Inbt", 60, 1)
            ch_j "Ok, fine."
        elif "no hand" in JeanX.DailyActions:
            ch_j "Oh, -fine-. . ."
        else:
            $ JeanX.FaceChange("sexy", 1)
            $ JeanX.Statup("Love", 90, 1)
            $ JeanX.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Sure, I guess.",
                "Okay. . . ",
                "Fine.",
                "I suppose I could. . .",
                "Ok. . . Get over here. . .",
                "Ok, ok."])
            ch_j "[Line]"
            $ Line = 0
        $ JeanX.Statup("Obed", 20, 1)
        $ JeanX.Statup("Obed", 60, 1)
        $ JeanX.Statup("Inbt", 70, 2)
        jump Jean_HJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ JeanX.FaceChange("angry")
        if "no hand" in JeanX.RecentActions:
            ch_j "I just told you no, [JeanX.Petname]."
        elif JeanX.Taboo and "tabno" in JeanX.DailyActions and "no hand" in JeanX.DailyActions:
            ch_j "I told you I wasn't comfortable in public. . ."
        elif "no hand" in JeanX.DailyActions:
            ch_j "I told you \"no,\" [JeanX.Petname]."
        elif JeanX.Taboo and "tabno" in JeanX.DailyActions:
            ch_j "I told you I wasn't comfortable in public. . ."
        elif not JeanX.Hand:
            $ JeanX.FaceChange("bemused")
            ch_j "Seriously, [JeanX.Petname]. . ."
        else:
            $ JeanX.FaceChange("bemused")
            ch_j "Nope."
        menu:
            extend ""
            "Sorry, never mind." if "no hand" in JeanX.DailyActions:
                $ JeanX.FaceChange("bemused")
                ch_j "It's fine."
                return
            "Maybe later?" if "no hand" not in JeanX.DailyActions:
                $ JeanX.FaceChange("bemused")
                ch_j "Maybe."
                $ JeanX.Statup("Love", 80, 2)
                $ JeanX.Statup("Inbt", 70, 2)
                if JeanX.Taboo:
                    $ JeanX.RecentActions.append("tabno")
                    $ JeanX.DailyActions.append("tabno")
                $ JeanX.RecentActions.append("no hand")
                $ JeanX.DailyActions.append("no hand")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ JeanX.FaceChange("sexy")
                    $ JeanX.Statup("Obed", 90, 2)
                    $ JeanX.Statup("Obed", 50, 2)
                    $ JeanX.Statup("Inbt", 70, 3)
                    $ JeanX.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Sure, I guess.",
                        "Okay. . . ",
                        "Fine.",
                        "I suppose I could. . .",
                        "Ok. . . Get over here. . .",
                        "Ok, ok."])
                    ch_j "[Line]"
                    $ Line = 0
                    jump Jean_HJ_Prep
                else:
                    pass

            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck(JeanX, 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and JeanX.Forced):
                    $ JeanX.FaceChange("sad")
                    $ JeanX.Statup("Love", 70, -5, 1)
                    $ JeanX.Statup("Love", 200, -2)
                    ch_j ". . . Ok, whatever."
                    $ JeanX.Statup("Obed", 50, 4)
                    $ JeanX.Statup("Inbt", 80, 1)
                    $ JeanX.Statup("Inbt", 60, 3)
                    $ JeanX.Forced = 1
                    jump Jean_HJ_Prep
                else:
                    $ JeanX.Statup("Love", 200, -15)
                    $ JeanX.RecentActions.append("angry")
                    $ JeanX.DailyActions.append("angry")

    #She refused all offers.
    $ JeanX.ArmPose = 1
    if "no hand" in JeanX.DailyActions:
        $ JeanX.FaceChange("angry", 1)
        ch_j "Don't ask again."
        $ JeanX.RecentActions.append("angry")
        $ JeanX.DailyActions.append("angry")
    elif JeanX.Forced:
        $ JeanX.FaceChange("angry", 1)
        ch_j "No."
        $ JeanX.Statup("Lust", 200, 5)
        if JeanX.Love > 300:
                $ JeanX.Statup("Love", 70, -2)
        $ JeanX.Statup("Obed", 50, -2)
        $ JeanX.RecentActions.append("angry")
        $ JeanX.DailyActions.append("angry")
    elif JeanX.Taboo:                             # she refuses and this is too public a place for her
        $ JeanX.FaceChange("angry", 1)
        $ JeanX.DailyActions.append("tabno")
        ch_j "I'm not comfortable in public right now. . ."
        $ JeanX.Statup("Lust", 200, 5)
        $ JeanX.Statup("Obed", 50, -3)
    elif JeanX.Hand:
        $ JeanX.FaceChange("sad")
        ch_j "I'm not into it today. . ."
    else:
        $ JeanX.FaceChange("normal", 1)
        ch_j "I'd really prefer not touching that."
    $ JeanX.RecentActions.append("no hand")
    $ JeanX.DailyActions.append("no hand")
    $ temp_modifier = 0
    return


label Jean_HJ_Prep:
    if Trigger2 == "hand":
        return

    if JeanX.Taboo:
        $ JeanX.Statup("Inbt", 90, int(Taboo/10))
        $ JeanX.Statup("Lust", 50, int(Taboo/5))

    $ JeanX.FaceChange("sexy")
    if JeanX.Forced:
        $ JeanX.FaceChange("sad")
    elif not JeanX.Hand:
        $ JeanX.Brows = "confused"
        $ JeanX.Eyes = "sexy"
        $ JeanX.Mouth = "smile"

    call Seen_First_Peen(JeanX,Partner,React=Situation)
    call Jean_HJ_Launch("L")

    if Situation == JeanX:
            #Jean auto-starts
            $ Situation = 0
            if Trigger2 == "jackin":
                "[JeanX.Name] brushes your hand aside and starts stroking your cock."
            else:
                "[JeanX.Name] gives you a mischevious smile, and starts to fondle your cock."
            menu:
                "What do you do?"
                "Nothing.":
                    $ JeanX.Statup("Inbt", 70, 3)
                    $ JeanX.Statup("Inbt", 30, 2)
                    "[JeanX.Name] continues her actions."
                "Praise her.":
                    $ JeanX.FaceChange("sexy", 1)
                    $ JeanX.Statup("Inbt", 70, 3)
                    ch_p "Oooh, that's good, [JeanX.Pet]."
                    $ JeanX.NameCheck() #checks reaction to petname
                    "[JeanX.Name] continues her actions."
                    $ JeanX.Statup("Love", 80, 1)
                    $ JeanX.Statup("Obed", 90, 1)
                    $ JeanX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ JeanX.FaceChange("surprised")
                    $ JeanX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [JeanX.Pet]."
                    $ JeanX.NameCheck() #checks reaction to petname
                    "[JeanX.Name] puts it down."
                    $ JeanX.Statup("Obed", 90, 1)
                    $ JeanX.Statup("Obed", 50, 1)
                    $ JeanX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ JeanX.AddWord(1,"refused","refused")
                    return

    if not JeanX.Hand:
        if JeanX.Forced:
            $ JeanX.Statup("Love", 90, -20)
            $ JeanX.Statup("Obed", 70, 25)
            $ JeanX.Statup("Inbt", 80, 30)
        else:
            $ JeanX.Statup("Love", 90, 5)
            $ JeanX.Statup("Obed", 70, 20)
            $ JeanX.Statup("Inbt", 80, 20)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if JeanX.Taboo:
        $ JeanX.DrainWord("tabno")
    $ JeanX.DrainWord("no hand")
    $ JeanX.RecentActions.append("hand")
    $ JeanX.DailyActions.append("hand")

label Jean_HJ_Cycle:
    while Round > 0:
        call Shift_Focus(JeanX)
        call Jean_HJ_Launch
        $ JeanX.LustFace()

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
                                            if JeanX.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ JeanX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Shift primary action":
                                            if JeanX.Action and MultiAction:
                                                    menu:
#                                                        "How about a blowjob?":
#                                                                    if JeanX.Action and MultiAction:
#                                                                        $ Situation = "shift"
#                                                                        call Jean_HJ_After
#                                                                        call Jean_Blowjob
#                                                                    else:
#                                                                        call Sex_Basic_Dialog(JeanX,"tired")

#                                                        "How about a titjob?":
#                                                                    if JeanX.Action and MultiAction:
#                                                                        $ Situation = "shift"
#                                                                        call Jean_HJ_After
#                                                                        call Jean_Titjob
#                                                                    else:
#                                                                        call Sex_Basic_Dialog(JeanX,"tired")
                                                        "Never Mind":
                                                                jump Jean_HJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [JeanX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(JeanX)
                                            "Ask [JeanX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(JeanX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(JeanX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jean_HJ_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jean_HJ_Cycle
                                            "Never mind":
                                                        jump Jean_HJ_Cycle
                                    "undress [JeanX.Name]":
                                            call Girl_Undress(JeanX)
                                    "Clean up [JeanX.Name] (locked)" if not JeanX.Spunk:
                                            pass
                                    "Clean up [JeanX.Name]" if JeanX.Spunk:
                                            call Girl_Cleanup(JeanX,"ask")
                                    "Never mind":
                                            jump Jean_HJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Jean_HJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Jean_HJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Jean_HJ_Reset
                                    $ Line = 0
                                    jump Jean_HJ_After
        #End menu (if Line)

        call Shift_Focus(JeanX)
        call Sex_Dialog(JeanX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JeanX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JeanX)
                            if "angry" in JeanX.RecentActions:
                                call Jean_HJ_Reset
                                return
                            $ JeanX.Statup("Lust", 200, 5)
                            if 100 > JeanX.Lust >= 70 and JeanX.OCount < 2 and JeanX.SEXP >= 20:
                                $ JeanX.RecentActions.append("unsatisfied")
                                $ JeanX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jean_HJ_After
                            $ Line = "came"

                    if JeanX.Lust >= 100:
                            #If Jean can cum
                            call Girl_Cumming(JeanX)
                            if Situation == "shift" or "angry" in JeanX.RecentActions:
                                jump Jean_HJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in JeanX.RecentActions:#And Jean is unsatisfied,
                                "[JeanX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Jean_HJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Cnt == 20:
                    $ JeanX.Brows = "angry"
                    menu:
                        ch_j "Ok, I'm bored now. Can we try something else?"
#                        "How about a BJ?" if JeanX.Action and MultiAction:
#                                $ Situation = "shift"
#                                call Jean_HJ_After
#                                call Jean_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                jump Jean_HJ_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Jean_HJ_Reset
                                $ Situation = "shift"
                                jump Jean_HJ_After
                        "No, get back down there.":
                                if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                                    $ JeanX.Statup("Love", 200, -5)
                                    $ JeanX.Statup("Obed", 50, 3)
                                    $ JeanX.Statup("Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    $ JeanX.FaceChange("angry", 1)
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_j "I have better things to do with my time."
                                    $ JeanX.Statup("Love", 50, -3, 1)
                                    $ JeanX.Statup("Love", 80, -4, 1)
                                    $ JeanX.Statup("Obed", 30, -1, 1)
                                    $ JeanX.Statup("Obed", 50, -1, 1)
                                    $ JeanX.RecentActions.append("angry")
                                    $ JeanX.DailyActions.append("angry")
                                    jump Jean_HJ_After
        elif Cnt == 10 and JeanX.SEXP <= 100 and not ApprovalCheck(JeanX, 1200, "LO"):
                    $ JeanX.Brows = "confused"
                    ch_j "Nice, right?"
        #End Count check

        call Escalation(JeanX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(JeanX,10) #"You might want to wrap this up, it's getting late."
        elif Round == 5:
                call Sex_Basic_Dialog(JeanX,5)   #"Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ JeanX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(JeanX,"done")   #"Ok, [Girl.Petname], that's enough of that for now."

label Jean_HJ_After:
    $ JeanX.FaceChange("sexy")

    $ JeanX.Hand += 1
    $ JeanX.Action -=1
    $ JeanX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ JeanX.Addictionrate += 1
    $ JeanX.Statup("Lust", 90, 5)

    call Partner_Like(JeanX,1)

    if "Jean Handi-Queen" in Achievements:
            pass
    elif JeanX.Hand >= 10:
            $ JeanX.FaceChange("smile", 1)
            ch_j "This seems to be all we do lately. . ."
            $ Achievements.append("Jean Handi-Queen")
            $JeanX.SEXP += 5
    elif JeanX.Hand == 1:
            $JeanX.SEXP += 10
            if JeanX.Love >= 500:
                $ JeanX.Mouth = "smile"
                ch_j "That was kinda fun. . ."
            elif Player.Focus <= 20:
                $ JeanX.Mouth = "sad"
                ch_j "Pretty nice, right?"
    elif JeanX.Hand == 5:
                ch_j "I'm pretty good at this, right?"

    $ temp_modifier = 0
    if Situation == "shift":
        ch_j "Ok, so what did you have in mind?"
    else:
        call Jean_HJ_Reset
    call Checkout
    return

## end JeanX.Handjob //////////////////////////////////////////////////////////////////////


## JeanX.Titjob //////////////////////////////////////////////////////////////////////
label Jean_Titjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JeanX)
    if JeanX.Tit >= 7: # She loves it
        $ temp_modifier += 10
    elif JeanX.Tit >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif JeanX.Tit: #You've done it before
        $ temp_modifier += 5

    if JeanX.Addict >= 75 and JeanX.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 15
    elif JeanX.Addict >= 75:
        $ temp_modifier += 5

    if JeanX.SeenChest and ApprovalCheck(JeanX, 500): # You've seen her tits.
        $ temp_modifier += 10
    if not JeanX.Chest and not JeanX.Over: #She's already topless
        $ temp_modifier += 10
    if JeanX.Lust > 75: #She's really horny
        $ temp_modifier += 10
    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in JeanX.Traits:
        $ temp_modifier += (5*Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JeanX.Traits:
        $ temp_modifier -= 30
    if JeanX.ForcedCount and not JeanX.Forced:
        $ temp_modifier -= 5 * JeanX.ForcedCount

    if JeanX.Taboo and "tabno" in JeanX.DailyActions:
        $ temp_modifier -= 10

    if "no titjob" in JeanX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no titjob" in JeanX.RecentActions else 0

    $ Approval = ApprovalCheck(JeanX, 1200, TabM = 4) # 120, 135, 150, Taboo -200(320)

    if not JeanX.Tit and "no titjob" not in JeanX.RecentActions:
        $ JeanX.FaceChange("surprised", 1)
        $ JeanX.Mouth = "kiss"
        ch_j "Oh, you want me to put these to work. . ."
        $ JeanX.FaceChange("sly", 1)
        ch_j "I can't blame you. . ."

    if not JeanX.Tit and Approval:                                                 #First time dialog
        if JeanX.Forced:
            $ JeanX.FaceChange("sad")
            $ JeanX.Statup("Love", 70, -3, 1)
            $ JeanX.Statup("Love", 20, -2, 1)
        elif JeanX.Love >= (JeanX.Obed + JeanX.Inbt - JeanX.IX):
            $ JeanX.FaceChange("sexy")
            $ JeanX.Brows = "sad"
            $ JeanX.Mouth = "smile"
            ch_j "I'd love to, but. . .."
        elif JeanX.Obed >= (JeanX.Inbt - JeanX.IX):
            $ JeanX.FaceChange("normal")
            ch_j "If you'd want that. . ."
        elif JeanX.Addict >= 50:
            $ JeanX.FaceChange("manic", 1)
            ch_j "Hmmmm. . . ."
        else: # Uninhibited
            $ JeanX.FaceChange("sad")
            $ JeanX.Mouth = "smile"
            ch_j "Sounds fun, but. . ."
    elif Approval:                                                                       #Second time+ dialog
        if JeanX.Forced:
            $ JeanX.FaceChange("sad")
            $ JeanX.Statup("Love", 70, -3, 1)
            $ JeanX.Statup("Love", 20, -2, 1)
            ch_j "Well that's a big ask. . ."
        elif not JeanX.Taboo and "tabno" in JeanX.DailyActions:
            ch_j "Ok, I guess this is secluded enough. . ."
        elif "titjob" in JeanX.RecentActions:
            $ JeanX.FaceChange("sexy", 1)
            ch_j "Huh, again?"
            jump Jean_TJ_Prep
        elif "titjob" in JeanX.DailyActions:
            $ JeanX.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Back for more?",
                "You're really working these babies.",
                "Didn't get enough earlier?",
                "You're really working these babies."])
            ch_j "[Line]"
        elif JeanX.Tit < 3:
            $ JeanX.FaceChange("sexy", 1)
            $ JeanX.Brows = "confused"
            $ JeanX.Mouth = "kiss"
            ch_j "Again with the tits, uh?"
        else:
            $ JeanX.FaceChange("sexy", 1)
            $ JeanX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action [rubs her chest]?",
                "So you'd like another titjob?",
                "So you'd like another titjob?",
                "So you'd like another titjob?",
                "Another titjob?",
                "A little [points at her chest]?"])
            ch_j "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if JeanX.Forced:
            $ JeanX.FaceChange("sad")
            $ JeanX.Statup("Obed", 90, 1)
            $ JeanX.Statup("Inbt", 60, 1)
            ch_j "I can't fault your taste. . ."
        elif "no titjob" in JeanX.DailyActions:
            ch_j "Hmm, I guess. . ."
        else:
            $ JeanX.FaceChange("sexy", 1)
            $ JeanX.Statup("Love", 90, 1)
            $ JeanX.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, put it here.",
                "Well. . . ok.",
                "Yum.",
                "Sure, whip it out.",
                "Heh, ok."])
            ch_j "[Line]"
            $ Line = 0
        $ JeanX.Statup("Obed", 20, 1)
        $ JeanX.Statup("Obed", 70, 1)
        $ JeanX.Statup("Inbt", 80, 2)
        jump Jean_TJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ JeanX.FaceChange("angry")
        if "no titjob" in JeanX.RecentActions:
            ch_j "I {i}just{/i} told you \"no,\" [JeanX.Petname]."
        elif JeanX.Taboo and "tabno" in JeanX.DailyActions and "no titjob" in JeanX.DailyActions:
            ch_j "I don't want to show off the goods like that!"
        elif "no titjob" in JeanX.DailyActions:
            ch_j "I already told you \"no,\" [JeanX.Petname]."
        elif JeanX.Taboo and "tabno" in JeanX.DailyActions:
            ch_j "I don't want to show off the goods like that!"
        elif not JeanX.Tit:
            $ JeanX.FaceChange("bemused")
            ch_j "Not really my thing, [JeanX.Petname]. . ."
        else:
            $ JeanX.FaceChange("bemused")
            ch_j "Not right now [JeanX.Petname]. . ."

        menu:
            extend ""
            "Sorry, never mind." if "no titjob" in JeanX.DailyActions:
                $ JeanX.FaceChange("bemused")
                ch_j "Ok, fine, [JeanX.Petname]."
                return
            "Maybe later?" if "no titjob" not in JeanX.DailyActions:
                $ JeanX.FaceChange("sexy")
                ch_j ". . . maybe."
                $ JeanX.Statup("Love", 80, 2)
                $ JeanX.Statup("Inbt", 70, 2)
                if JeanX.Taboo:
                    $ JeanX.RecentActions.append("tabno")
                    $ JeanX.DailyActions.append("tabno")
                $ JeanX.RecentActions.append("no titjob")
                $ JeanX.DailyActions.append("no titjob")
                return
            "I think this could be fun for both of us. . .":
                if Approval:
                    $ JeanX.FaceChange("sexy")
                    $ JeanX.Statup("Obed", 80, 2)
                    $ JeanX.Statup("Obed", 40, 2)
                    $ JeanX.Statup("Inbt", 70, 3)
                    $ JeanX.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Well, ok, put it here.",
                        "Well. . . ok.",
                        "I guess.",
                        "I guess, whip it out.",
                        "Heh, ok."])
                    ch_j "[Line]"
                    $ Line = 0
                    jump Jean_TJ_Prep
                else:
                    $ Approval = ApprovalCheck(JeanX, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)             Handy instead?
                    if Approval >= 2 and JeanX.Blow:
                        $ JeanX.Statup("Inbt", 80, 1)
                        $ JeanX.Statup("Inbt", 60, 3)
                        $ JeanX.FaceChange("confused", 1)
                        ch_j "What about a blowjob then?"
                        menu:
                            ch_j "What about a blowjob then?"
                            "Ok, get down there.":
                                $ JeanX.Statup("Love", 80, 2)
                                $ JeanX.Statup("Inbt", 60, 1)
                                $ JeanX.Statup("Obed", 50, 1)
                                jump Jean_BJ_Prep
                            "Nah, it's all about dem titties.":
                                $ Line = "no BJ"
                    if Approval and JeanX.Hand:
                        $ JeanX.Statup("Inbt", 80, 1)
                        $ JeanX.Statup("Inbt", 60, 3)
                        $ JeanX.FaceChange("confused", 1)
                        ch_j "I could give you a hand job?"
                        menu:
                            ch_j "What do you say?"
                            "Sure, that's fine.":
                                $ JeanX.Statup("Love", 80, 2)
                                $ JeanX.Statup("Inbt", 60, 1)
                                $ JeanX.Statup("Obed", 50, 1)
                                jump Jean_HJ_Prep
                            "Seriously, titties." if Line == "no BJ":
                                $ Line = 0
                            "Nah, it's all about dem titties." if Line != "no BJ":
                                pass
                    $ JeanX.Statup("Love", 200, -2)
                    ch_j "Well then too bad, I guess."
                    $ JeanX.Statup("Obed", 70, 2)


            "Come on, let me fuck those titties, [JeanX.Pet]":                                               # Pressured into it
                $ JeanX.NameCheck() #checks reaction to petname
                $ Approval = ApprovalCheck(JeanX, 700, "OI", TabM = 4) # 70, 85, 100, -160(230)
                if Approval > 1 or (Approval and JeanX.Forced):
                    $ JeanX.FaceChange("angry",1)
                    $ JeanX.Statup("Love", 70, -5, 1)
                    $ JeanX.Statup("Love", 200, -2)
                    ch_j ". . ."
                    $ JeanX.FaceChange("angry",1,Eyes="side")
                    ch_j "Ok, fine, whip it out."
                    $ JeanX.Statup("Obed", 50, 4)
                    $ JeanX.Statup("Inbt", 80, 1)
                    $ JeanX.Statup("Inbt", 60, 3)
                    $ JeanX.Forced = 1
                    jump Jean_TJ_Prep
                else:
                    $ JeanX.Statup("Love", 200, -15)
                    $ JeanX.RecentActions.append("angry")
                    $ JeanX.DailyActions.append("angry")

    #She refused all offers.
    if "no titjob" in JeanX.DailyActions:
        $ JeanX.FaceChange("angry", 1)
        ch_j "I already told you no."
        $ JeanX.RecentActions.append("angry")
        $ JeanX.DailyActions.append("angry")
    elif JeanX.Forced:
        $ JeanX.FaceChange("angry", 1)
        ch_j "No, try something else."
        $ JeanX.Statup("Lust", 200, 5)
        if JeanX.Love > 300:
                $ JeanX.Statup("Love", 70, -2)
        $ JeanX.Statup("Obed", 50, -2)
        $ JeanX.RecentActions.append("angry")
        $ JeanX.DailyActions.append("angry")
    elif JeanX.Taboo:                             # she refuses and this is too public a place for her
        $ JeanX.FaceChange("angry", 1)
        $ JeanX.DailyActions.append("tabno")
        ch_j "You really expect me to do that here?"
        ch_j "You know I can't \"take care of that\" anymore. . ."
        $ JeanX.Statup("Lust", 200, 5)
        $ JeanX.Statup("Obed", 50, -3)
    elif JeanX.Tit:
        $ JeanX.FaceChange("sad")
        ch_j "You'll know when it's time for that."
    else:
        $ JeanX.FaceChange("normal", 1)
        ch_j "Nah."
    $ JeanX.RecentActions.append("no titjob")
    $ JeanX.DailyActions.append("no titjob")
    $ temp_modifier = 0
    return

label Jean_TJ_Prep:
    if JeanX.Taboo:
        $ JeanX.Statup("Inbt", 90, int(Taboo/10))
        $ JeanX.Statup("Lust", 50, int(Taboo/5))


    $ JeanX.FaceChange("sexy")
    if JeanX.Forced:
        $ JeanX.FaceChange("sad")
    elif not JeanX.Tit:
        $ JeanX.Brows = "confused"
        $ JeanX.Eyes = "sexy"
        $ JeanX.Mouth = "smile"

    call Seen_First_Peen(JeanX,Partner,React=Situation)
    call Jean_TJ_Launch("L")

    if Situation == JeanX:
            #Jean auto-starts
            $ Situation = 0
            "[JeanX.Name] slides down and sandwiches your dick between her tits."
            menu:
                "What do you do?"
                "Nothing.":
                    $ JeanX.Statup("Inbt", 80, 3)
                    $ JeanX.Statup("Inbt", 40, 2)
                    "[JeanX.Name] starts to slide them up and down."
                "Praise her.":
                    $ JeanX.FaceChange("sexy", 1)
                    $ JeanX.Statup("Inbt", 80, 3)
                    ch_p "Oh, that sounds like a good idea, [JeanX.Pet]."
                    $ JeanX.NameCheck() #checks reaction to petname
                    "[JeanX.Name] continues her actions."
                    $ JeanX.Statup("Love", 85, 1)
                    $ JeanX.Statup("Obed", 90, 1)
                    $ JeanX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ JeanX.FaceChange("confused")
                    $ JeanX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [JeanX.Pet]."
                    $ JeanX.NameCheck() #checks reaction to petname
                    "[JeanX.Name] lets it drop out from between her breasts."
                    $ JeanX.Statup("Obed", 90, 1)
                    $ JeanX.Statup("Obed", 50, 3)
                    $ Player.RecentActions.append("nope")
                    $ JeanX.AddWord(1,"refused","refused")
                    return

    if not JeanX.Tit:
        if JeanX.Forced:
            $ JeanX.Statup("Love", 90, -25)
            $ JeanX.Statup("Obed", 70, 30)
            $ JeanX.Statup("Inbt", 80, 35)
        else:
            $ JeanX.Statup("Love", 90, 5)
            $ JeanX.Statup("Obed", 70, 25)
            $ JeanX.Statup("Inbt", 80, 30)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if JeanX.Taboo:
        $ JeanX.DrainWord("tabno")
    $ JeanX.DrainWord("no titjob")
    $ JeanX.RecentActions.append("titjob")
    $ JeanX.DailyActions.append("titjob")

label Jean_TJ_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(JeanX)
        call Jean_TJ_Launch
        $ JeanX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass

                        "Start moving? . ." if Speed == 0:
                                    call Speed_Shift(1)

                        "Speed up. . ." if  Speed == 1:
                                    call Speed_Shift(2)
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 2:
                                    pass

                        "Stop moving" if Speed != 0:
                                    call Speed_Shift(0)
                        "Slow Down. . ." if Speed == 2:
                                    call Speed_Shift(1)
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
                                            if JeanX.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ JeanX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Shift primary action":
                                            if JeanX.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                    $ Situation = "shift"
                                                                    call Jean_TJ_After
                                                                    call Jean_Blowjob
                                                        "How about a handy?":
                                                                    $ Situation = "shift"
                                                                    call Jean_BJ_After
                                                                    call Jean_Handjob
                                                        "Never Mind":
                                                                jump Jean_TJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [JeanX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(JeanX)
                                            "Ask [JeanX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(JeanX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(JeanX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jean_TJ_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jean_TJ_Cycle
                                            "Never mind":
                                                        jump Jean_TJ_Cycle
                                    "undress [JeanX.Name]":
                                            call Girl_Undress(JeanX)
                                    "Clean up [JeanX.Name] (locked)" if not JeanX.Spunk:
                                            pass
                                    "Clean up [JeanX.Name]" if JeanX.Spunk:
                                            call Girl_Cleanup(JeanX,"ask")
                                    "Never mind":
                                            jump Jean_TJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Jean_TJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Jean_TJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Jean_TJ_Reset
                                    $ Line = 0
                                    jump Jean_TJ_After
        #End menu (if Line)

        call Shift_Focus(JeanX)
        call Sex_Dialog(JeanX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JeanX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JeanX)
                            if "angry" in JeanX.RecentActions:
                                call Jean_TJ_Reset
                                return
                            $ JeanX.Statup("Lust", 200, 5)
                            if 100 > JeanX.Lust >= 70 and JeanX.OCount < 2 and JeanX.SEXP >= 20:
                                $ JeanX.RecentActions.append("unsatisfied")
                                $ JeanX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jean_TJ_After
                            $ Line = "came"

                    if JeanX.Lust >= 100:
                            #If Jean can cum
                            call Girl_Cumming(JeanX)
                            if Situation == "shift" or "angry" in JeanX.RecentActions:
                                jump Jean_TJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in JeanX.RecentActions:#And Jean is unsatisfied,
                                "[JeanX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Jean_TJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        if Speed >= 4:
                call Speed_Shift(0) #resets speed after orgasm
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if JeanX.SEXP >= 100 or ApprovalCheck(JeanX, 1200, "LO"):
                pass
        elif Cnt == (5 + JeanX.Tit):
                $ JeanX.Brows = "confused"
                ch_j "Hey, how you doing up there? About done?"
        if Cnt == (10 + JeanX.Tit):
                $ JeanX.Brows = "angry"
                menu:
                    ch_j "Ok, seriously, can't we do something else?"
                    "How about a BJ?" if JeanX.Action and MultiAction:
                        $ Situation = "shift"
                        call Jean_TJ_After
                        call Jean_Blowjob
                        return
                    "Finish up." if Player.FocusX:
                        "You release your concentration. . ."
                        $ Player.FocusX = 0
                        $ Player.Focus += 15
                        jump Jean_TJ_Cycle
                    "Let's try something else." if MultiAction:
                        $ Line = 0
                        call Jean_TJ_Reset
                        $ Situation = "shift"
                        jump Jean_TJ_After
                    "No, get back down there.":
                        if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                            $ JeanX.Statup("Love", 200, -5)
                            $ JeanX.Statup("Obed", 50, 3)
                            $ JeanX.Statup("Obed", 80, 2)
                            "She grumbles but gets back to work."
                        else:
                            $ JeanX.FaceChange("angry", 1)
                            "She scowls at you, drops you cock and pulls back."
                            ch_j "Well fuck you then."
                            $ JeanX.Statup("Love", 50, -3, 1)
                            $ JeanX.Statup("Love", 80, -4, 1)
                            $ JeanX.Statup("Obed", 30, -1, 1)
                            $ JeanX.Statup("Obed", 50, -1, 1)
                            $ JeanX.RecentActions.append("angry")
                            $ JeanX.DailyActions.append("angry")
                            jump Jean_TJ_After
            #End Count check

        call Escalation(JeanX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(JeanX,10) #"You might want to wrap this up, it's getting late."
        elif Round == 5:
                call Sex_Basic_Dialog(JeanX,5)   #"Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ JeanX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(JeanX,"done")   #"Ok, [Girl.Petname], that's enough of that for now."

label Jean_TJ_After:
    $ JeanX.FaceChange("sexy")

    $ JeanX.Tit += 1
    $ JeanX.Action -=1
    $ JeanX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ JeanX.Addictionrate += 1

    call Partner_Like(JeanX,4)

    if JeanX.Tit > 5:
        pass
    elif JeanX.Tit == 1:
        $ JeanX.SEXP += 12
        if JeanX.Love >= 500:
            $ JeanX.Mouth = "smile"
            ch_j "OK, that was fun."
        elif Player.Focus <= 20:
            $ JeanX.Mouth = "sad"
            ch_j "I hope that worked out for you. . ."
    elif JeanX.Tit == 5:
            ch_j "Fun, right?"

    $ temp_modifier = 0

    if Situation == "shift":
            ch_j "Mmm, so what else did you have in mind?"
    else:
            call Jean_TJ_Reset
    call Checkout
    return

## end JeanX.Titjob //////////////////////////////////////////////////////////////////////



# JeanX.Blowjob //////////////////////////////////////////////////////////////////////

label Jean_Blowjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JeanX)
    if JeanX.Blow >= 7: # She loves it
        $ temp_modifier += 15
    elif JeanX.Blow >= 3: #You've done it before several times
        $ temp_modifier += 10
    elif JeanX.Blow: #You've done it before
        $ temp_modifier += 7

    if JeanX.Addict >= 75 and JeanX.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 25
    elif JeanX.Addict >= 75: #She's really strung out
        $ temp_modifier += 15

    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in JeanX.Traits:
        $ temp_modifier += (4*Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JeanX.Traits:
        $ temp_modifier -= 40
    if JeanX.ForcedCount and not JeanX.Forced:
        $ temp_modifier -= 5 * JeanX.ForcedCount

    if JeanX.Taboo and "tabno" in JeanX.DailyActions:
        $ temp_modifier -= 10

    if "no blow" in JeanX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no blow" in JeanX.RecentActions else 0

    $ Approval = ApprovalCheck(JeanX, 1300, TabM = 4) # 130, 145, 160, Taboo -160(290)

    if not JeanX.Blow and "no blow" not in JeanX.RecentActions:
        $ JeanX.FaceChange("surprised", 2)
        $ JeanX.Mouth = "kiss"
        ch_j "Oh! You want me to suck you off?"

    if not JeanX.Blow and Approval:                                                 #First time dialog
        if JeanX.Forced:
            $ JeanX.FaceChange("sad")
            $ JeanX.Statup("Love", 70, -3, 1)
            $ JeanX.Statup("Love", 20, -2, 1)
        elif JeanX.Love >= (JeanX.Obed + JeanX.Inbt - JeanX.IX):
            $ JeanX.FaceChange("sexy")
            $ JeanX.Brows = "sad"
            $ JeanX.Mouth = "smile"
            ch_j "Well, I could hardly turn down that offer. . ."
        elif JeanX.Obed >= (JeanX.Inbt - JeanX.IX):
            $ JeanX.FaceChange("normal")
            ch_j "I could do that, I guess. . ."
        elif JeanX.Addict >= 50:
            $ JeanX.FaceChange("manic", 1)
            ch_j "Mmmmm. . ."
        else: # Uninhibited
            $ JeanX.FaceChange("sad")
            $ JeanX.Mouth = "smile"
            ch_j "Huh. . ."
    elif Approval:                                                                       #Second time+ dialog
        if JeanX.Forced:
            $ JeanX.FaceChange("sad")
            $ JeanX.Statup("Love", 70, -3, 1)
            $ JeanX.Statup("Love", 20, -2, 1)
            ch_j "Again?"
        elif not JeanX.Taboo and "tabno" in JeanX.DailyActions:
            ch_j "Hmm, this is private enough. . ."
        elif "blow" in JeanX.RecentActions:
            $ JeanX.FaceChange("sexy", 1)
            ch_j "Mmm, again?"
            jump Jean_BJ_Prep
        elif "blow" in JeanX.DailyActions:
            $ JeanX.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",
                "You're wearing me out here.",
                "I must be too good at this.",
                "Didn't get enough earlier?"])
            ch_j "[Line]"
        elif JeanX.Blow < 3:
            $ JeanX.FaceChange("sexy", 1)
            $ JeanX.Brows = "confused"
            $ JeanX.Mouth = "kiss"
            ch_j "You'd like another blowjob?"
        else:
            $ JeanX.FaceChange("sexy", 1)
            $ JeanX.ArmPose = 2
            $ Line = renpy.random.choice(["You want me to [mimes blowing]?",
                "So you want another blowjob?",
                "You want me to lick you?",
                "You want me to suck you off?",
                "A BJ?"])
            ch_j "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if JeanX.Forced:
            $ JeanX.FaceChange("sad")
            $ JeanX.Statup("Obed", 90, 1)
            $ JeanX.Statup("Inbt", 60, 1)
            ch_j "Fine, let's get this over with."
        elif "no blow" in JeanX.DailyActions:
            ch_j "Fine. . ."
        else:
            $ JeanX.FaceChange("sexy", 1)
            $ JeanX.Statup("Love", 90, 1)
            $ JeanX.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Sure. Ahhhhhh.",
                "Well. . . alright.",
                "Yum.",
                "Sure, whip it out.",
                "Ok. . . [She licks her lips].",
                "Alright, let's see it."])
            ch_j "[Line]"
            $ Line = 0
        $ JeanX.Statup("Obed", 20, 1)
        $ JeanX.Statup("Obed", 70, 1)
        $ JeanX.Statup("Inbt", 80, 2)
        jump Jean_BJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ JeanX.FaceChange("angry")
        if "no blow" in JeanX.RecentActions:
            ch_j "Just told you I wouldn't, [JeanX.Petname]."
        elif JeanX.Taboo and "tabno" in JeanX.DailyActions and "no blow" in JeanX.DailyActions:
            ch_j "Like I said, not in public."
        elif "no blow" in JeanX.DailyActions:
            ch_j "Told you \"no,\" [JeanX.Petname]."
        elif JeanX.Taboo and "tabno" in JeanX.DailyActions:
            ch_j "Like I said, too public!"
        elif not JeanX.Blow:
            $ JeanX.FaceChange("bemused")
            ch_j "I have been wondering what you taste like, [JeanX.Petname]. . ."
        else:
            $ JeanX.FaceChange("bemused")
            ch_j "I don't know, [JeanX.Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no blow" in JeanX.DailyActions:
                $ JeanX.FaceChange("bemused")
                ch_j "Ok then."
                return
            "Maybe later?" if "no blow" not in JeanX.DailyActions:
                $ JeanX.FaceChange("sexy")
                ch_j "Sure, whatever, [JeanX.Petname]."
                $ JeanX.Statup("Love", 80, 2)
                $ JeanX.Statup("Inbt", 70, 2)
                if JeanX.Taboo:
                    $ JeanX.RecentActions.append("tabno")
                    $ JeanX.DailyActions.append("tabno")
                $ JeanX.RecentActions.append("no blow")
                $ JeanX.DailyActions.append("no blow")
                return
            "Come on, please?":
                if Approval:
                    $ JeanX.FaceChange("sexy")
                    $ JeanX.Statup("Obed", 90, 2)
                    $ JeanX.Statup("Obed", 50, 2)
                    $ JeanX.Statup("Inbt", 70, 3)
                    $ JeanX.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Sure. Ahhhhhh.",
                        "Well. . . alright.",
                        "Yum.",
                        "Sure, whip it out.",
                        "Ok. . . [She licks her lips].",
                        "Alright, let's see it."])
                    ch_j "[Line]"
                    $ Line = 0
                    jump Jean_BJ_Prep
                else:
                    if ApprovalCheck(JeanX, 1100, TabM = 3): # 110, 125, 140, Taboo -120(230)             Handy instead?
                        $ JeanX.Statup("Inbt", 80, 1)
                        $ JeanX.Statup("Inbt", 60, 3)
                        $ JeanX.FaceChange("confused", 1)
                        $ JeanX.Arms = 1
                        if "psysex" in JeanX.History:
                            ch_j "Couldn't I just do the mind thing again?"
                            $ JeanX.FaceChange("sly", 1)
                            ch_j "You seemed to enjoy that one. . ."
                        else:
                            ch_j "What if I just used my telekinesis?"
                            $ JeanX.FaceChange("confused", 1)
                            ch_j "It would feel great, I promise. . ."
                        menu:
                            extend ""
                            "Sure, that's fine.":
                                $ JeanX.Statup("Love", 80, 2)
                                $ JeanX.Statup("Inbt", 60, 1)
                                $ JeanX.Statup("Obed", 50, 1)
                                jump Jean_PJ_Prep
                            "Nah, if it's not a BJ, forget it.":
                                $ JeanX.Statup("Love", 200, -2)
                                $ JeanX.Arms = 0
                                ch_j "too bad then."
                                $ JeanX.Statup("Obed", 70, 2)


            "Suck it, [JeanX.Pet]":                                               # Pressured into it
                $ JeanX.NameCheck() #checks reaction to petname
                $ Approval = ApprovalCheck(JeanX, 750, "OI", TabM = 3) # 75, 90, 105, -120(195)
                if Approval > 1 or (Approval and JeanX.Forced):
                    $ JeanX.FaceChange("angry",2)
                    $ JeanX.Statup("Love", 70, -5, 1)
                    $ JeanX.Statup("Love", 200, -2)
                    ch_j ". . ."
                    $ JeanX.FaceChange("angry",1,Eyes="side")
                    ch_j "Whatever. . ."
                    $ JeanX.Statup("Obed", 50, 4)
                    $ JeanX.Statup("Inbt", 80, 1)
                    $ JeanX.Statup("Inbt", 60, 3)
                    $ JeanX.Forced = 1
                    jump Jean_BJ_Prep
                else:
                    $ JeanX.Statup("Love", 200, -15)
                    $ JeanX.RecentActions.append("angry")
                    $ JeanX.DailyActions.append("angry")

    #She refused all offers.
    if "no blow" in JeanX.DailyActions:
        $ JeanX.FaceChange("angry", 1)
        $ JeanX.ArmPose = 2
        ch_j "You want me to make you suck yourself?"
        $ JeanX.ArmPose = 1
        $ JeanX.FaceChange("angry",1,Eyes="side")
        ch_j "Damn. . . forgot I can't do that. . ."
        $ JeanX.RecentActions.append("angry")
        $ JeanX.DailyActions.append("angry")
    elif JeanX.Forced:
        $ JeanX.FaceChange("angry", 1)
        ch_j "I'm not doing that."
        $ JeanX.Statup("Lust", 200, 5)
        if JeanX.Love > 300:
                $ JeanX.Statup("Love", 70, -2)
        $ JeanX.Statup("Obed", 50, -2)
        $ JeanX.RecentActions.append("angry")
        $ JeanX.DailyActions.append("angry")
        $ JeanX.RecentActions.append("no blow")
        $ JeanX.DailyActions.append("no blow")
        return
    elif JeanX.Taboo:                             # she refuses and this is too public a place for her
        $ JeanX.FaceChange("angry", 1)
        $ JeanX.DailyActions.append("tabno")
        ch_j "I'm not comfortable in public right now. . ."
        $ JeanX.Statup("Lust", 200, 5)
        $ JeanX.Statup("Obed", 50, -3)
        return
    elif JeanX.Blow:
        $ JeanX.FaceChange("sad")
        ch_j "Nah, not this time."
    else:
        $ JeanX.FaceChange("smile", 1)
        ch_j "Ha! Good one."
    $ JeanX.RecentActions.append("no blow")
    $ JeanX.DailyActions.append("no blow")
    $ temp_modifier = 0
    return


label Jean_BJ_Prep:
    if renpy.showing("Jean_HJ_Animation"):
        hide Jean_HJ_Animation with easeoutbottom
    if JeanX.Taboo:
        $ JeanX.Statup("Inbt", 90, int(Taboo/10))
        $ JeanX.Statup("Lust", 50, int(Taboo/5))

    $ JeanX.FaceChange("sexy")
    if JeanX.Forced:
        $ JeanX.FaceChange("sad")
    elif not JeanX.Blow:
        $ JeanX.Brows = "confused"
        $ JeanX.Eyes = "sexy"
        $ JeanX.Mouth = "smile"

    call Seen_First_Peen(JeanX,Partner,React=Situation)
    call Jean_BJ_Launch("L")
    if Situation == JeanX:
            #Jean auto-starts
            $ Situation = 0
            "[JeanX.Name] slides down and gives your cock a little lick."
            menu:
                "What do you do?"
                "Nothing.":
                    $ JeanX.Statup("Inbt", 80, 3)
                    $ JeanX.Statup("Inbt", 40, 2)
                    "[JeanX.Name] continues licking at it."
                "Praise her.":
                    $ JeanX.FaceChange("sexy", 1)
                    $ JeanX.Statup("Inbt", 80, 3)
                    ch_p "Hmmm, keep doing that, [JeanX.Pet]."
                    $ JeanX.NameCheck() #checks reaction to petname
                    "[JeanX.Name] continues her actions."
                    $ JeanX.Statup("Love", 85, 1)
                    $ JeanX.Statup("Obed", 90, 1)
                    $ JeanX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ JeanX.FaceChange("surprised")
                    $ JeanX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [JeanX.Pet]."
                    $ JeanX.NameCheck() #checks reaction to petname
                    "[JeanX.Name] puts it down."
                    $ JeanX.Statup("Obed", 90, 1)
                    $ JeanX.Statup("Obed", 50, 3)
                    $ Player.RecentActions.append("nope")
                    $ JeanX.AddWord(1,"refused","refused")
                    return
    if not JeanX.Blow:
        if JeanX.Forced:
            $ JeanX.Statup("Love", 90, -70)
            $ JeanX.Statup("Obed", 70, 45)
            $ JeanX.Statup("Inbt", 80, 60)
        else:
            $ JeanX.Statup("Love", 90, 5)
            $ JeanX.Statup("Obed", 70, 35)
            $ JeanX.Statup("Inbt", 80, 40)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if JeanX.Taboo:
        $ JeanX.DrainWord("tabno")
    $ JeanX.DrainWord("no blow")
    $ JeanX.RecentActions.append("blow")
    $ JeanX.DailyActions.append("blow")

label Jean_BJ_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(JeanX)
        call Jean_BJ_Launch
        $ JeanX.LustFace()

        if Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass

                        "Lick it. . ." if Speed != 1:
                                call Speed_Shift(1)
                        "Lick it. . . (locked)" if Speed == 1:
                                pass

                        "Just the head. . ." if Speed != 2:
                                call Speed_Shift(2)
                        "Just the head. . . (locked)" if Speed == 2:
                                pass

                        "Suck on it." if Speed != 3:
                                call Speed_Shift(3)
                                if Trigger2 == "jackin":
                                    "She dips her head a bit lower, and you move your hand out of the way."

                        "Suck on it. (locked)" if Speed == 3:
                                pass

                        "Take it deeper." if Speed != 4:
                                    if Trigger2 == "jackin" and Speed != 3:
                                        "She takes it to the root, and you move your hand out of the way."
                                    call Speed_Shift(4)
                        "Take it deeper. (locked)" if Speed == 4:
                                pass

                        "Set your own pace. . .":
                                "[JeanX.Name] hums contentedly."
                                if "setpace" not in JeanX.RecentActions:
                                    $ JeanX.Statup("Love", 80, 2)
                                $ D20 = renpy.random.randint(1, 20)
                                if JeanX.Blow < 5:
                                    $ D20 -= 10
                                elif JeanX.Blow < 10:
                                    $ D20 -= 5

                                if D20 > 15:
                                    call Speed_Shift(4)
                                    if "setpace" not in JeanX.RecentActions:
                                        $ JeanX.Statup("Inbt", 80, 3)
                                elif D20 > 10:
                                    call Speed_Shift(3)
                                elif D20 > 5:
                                    call Speed_Shift(2)
                                else:
                                    call Speed_Shift(1)
                                $ JeanX.RecentActions.append("setpace")

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
                                            if JeanX.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ JeanX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Shift primary action":
                                            if JeanX.Action and MultiAction:
                                                    menu:
                                                        "How about a handy?":
                                                                    $ Situation = "shift"
                                                                    call Jean_BJ_After
                                                                    call Jean_Handjob
                                                        "How about a titjob?":
                                                                    $ Situation = "shift"
                                                                    call Jean_BJ_After
                                                                    call Jean_Titjob
                                                        "Never Mind":
                                                                jump Jean_BJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [JeanX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(JeanX)
                                            "Ask [JeanX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(JeanX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(JeanX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jean_BJ_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jean_BJ_Cycle
                                            "Never mind":
                                                        jump Jean_BJ_Cycle
                                    "undress [JeanX.Name]":
                                            call Girl_Undress(JeanX)
                                    "Clean up [JeanX.Name] (locked)" if not JeanX.Spunk:
                                            pass
                                    "Clean up [JeanX.Name]" if JeanX.Spunk:
                                            call Girl_Cleanup(JeanX,"ask")
                                    "Never mind":
                                            jump Jean_BJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Jean_BJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Jean_BJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Jean_BJ_Reset
                                    $ Line = 0
                                    jump Jean_BJ_After
        #End menu (if Line)

        call Shift_Focus(JeanX)
        call Sex_Dialog(JeanX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1
        if Speed:
            $ Player.Wet = 1 #wets penis
            $ Player.Spunk = 0 if Player.Spunk else Player.Spunk #cleans you off after one cycle

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JeanX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JeanX)
                            if "angry" in JeanX.RecentActions:
                                call Jean_BJ_Reset
                                return
                            $ JeanX.Statup("Lust", 200, 5)
                            if 100 > JeanX.Lust >= 70 and JeanX.OCount < 2 and JeanX.SEXP >= 20:
                                $ JeanX.RecentActions.append("unsatisfied")
                                $ JeanX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jean_BJ_After
                            $ Line = "came"

                    if JeanX.Lust >= 100:
                            #If Jean can cum
                            call Girl_Cumming(JeanX)
                            if Situation == "shift" or "angry" in JeanX.RecentActions:
                                jump Jean_BJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."

                            if "unsatisfied" in JeanX.RecentActions:#And Jean is unsatisfied,
                                "[JeanX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Jean_BJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if JeanX.SEXP >= 100 or ApprovalCheck(JeanX, 1200, "LO"):
            pass
        elif Cnt == (10 + JeanX.Blow):
                $ JeanX.Brows = "angry"
                menu:
                    ch_j "Ok, that's enough of that. Can we do something else?"
                    "How about a Handy?" if JeanX.Action and MultiAction:
                            $ Situation = "shift"
                            call Jean_BJ_After
                            call Jean_Handjob
                            return
                    "Finish up." if Player.FocusX:
                            "You release your concentration. . ."
                            $ Player.FocusX = 0
                            $ Player.Focus += 15
                            jump Jean_BJ_Cycle
                    "Let's try something else." if MultiAction:
                            $ Line = 0
                            call Jean_BJ_Reset
                            $ Situation = "shift"
                            jump Jean_BJ_After
                    "No, get back down there.":
                            if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                                $ JeanX.Statup("Love", 200, -5)
                                $ JeanX.Statup("Obed", 50, 3)
                                $ JeanX.Statup("Obed", 80, 2)
                                "She grumbles but gets back to work."
                            else:
                                $ JeanX.FaceChange("angry", 1)
                                "She scowls at you, drops you cock and pulls back."
                                ch_j "Ok, have fun with that then."
                                $ JeanX.Statup("Love", 50, -3, 1)
                                $ JeanX.Statup("Love", 80, -4, 1)
                                $ JeanX.Statup("Obed", 30, -1, 1)
                                $ JeanX.Statup("Obed", 50, -1, 1)
                                $ JeanX.RecentActions.append("angry")
                                $ JeanX.DailyActions.append("angry")
                                jump Jean_BJ_After
        elif Cnt == (5 + JeanX.Blow) and JeanX.SEXP <= 100 and not ApprovalCheck(JeanX, 1200, "LO"):
                    $ JeanX.Brows = "confused"
                    ch_j "Hey, you about done up there?"
        #End Count check

        call Escalation(JeanX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(JeanX,10) #"You might want to wrap this up, it's getting late."
        elif Round == 5:
                call Sex_Basic_Dialog(JeanX,5)   #"Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ JeanX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(JeanX,"done")   #"Ok, [Girl.Petname], that's enough of that for now."

label Jean_BJ_After:
    $ JeanX.FaceChange("sexy")

    $ JeanX.Blow += 1
    $ JeanX.Action -=1
    $ JeanX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ JeanX.Addictionrate += 1

    call Partner_Like(JeanX,2)

    if "Jean Jobber" in Achievements:
        pass
    elif JeanX.Blow >= 10:
        $ JeanX.FaceChange("confused", 1,Eyes="side")
        ch_j "Wow, you know. . . I don't always love this. . ."
        $ JeanX.FaceChange("smile", 2)
        ch_j "but I guess with you it's different somehow. . ."
        $ JeanX.Blush = 1
        $ Achievements.append("Jean Jobber")
        $JeanX.SEXP += 5
    elif Situation == "shift":
        pass
    elif JeanX.Blow == 1:
            $JeanX.SEXP += 15
            if JeanX.Love >= 500:
                $ JeanX.Mouth = "smile"
                ch_j "Mmm, yeah, that was as good as I expected. . ."
            elif Player.Focus <= 20:
                $ JeanX.Mouth = "sad"
                ch_j "Well, got what you wanted from that?"
    elif JeanX.Blow == 5:
        ch_j "I am loving this. You too, right?"
        menu:
            "[[nod]":
                $ JeanX.FaceChange("smile", 1)
                $ JeanX.Statup("Love", 90, 15)
                $ JeanX.Statup("Obed", 80, 5)
                $ JeanX.Statup("Inbt", 90, 10)
            "[[shake head \"no\"]":
                if ApprovalCheck(JeanX, 500, "O"):
                    $ JeanX.FaceChange("sad", 2)
                    $ JeanX.Statup("Love", 200, -5)
                else:
                    $ JeanX.FaceChange("angry", 2)
                    $ JeanX.Statup("Love", 200, -25)
                $ JeanX.Statup("Obed", 80, 10)
                ch_j ". . ."
                $ JeanX.FaceChange("angry", 1)

    $ temp_modifier = 0
    if Situation != "shift":
        call Jean_BJ_Reset
    call Checkout
    return



# end JeanX.Blowjob                                 //////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy
label Jean_Dildo_Check:
    if "dildo" in Player.Inventory:
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in JeanX.Inventory:
        "You ask [JeanX.Name] to get out her favorite Dildo."
    else:
        "You don't have one of those on you."
        return 0
    return 1

label Jean_Dildo_Pussy:

    ch_j "You know what? I'm just not into this right now. . ."
    "[[not yet implemented]"
    return

    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JeanX)
    call Jean_Dildo_Check
    if not _return:
        return

    if JeanX.DildoP: #You've done it before
        $ temp_modifier += 15
    if JeanX.Legs == "pants:": # she's got pants on.
        $ temp_modifier -= 20

    if JeanX.Lust > 95:
        $ temp_modifier += 20
    elif JeanX.Lust > 85: #She's really horny
        $ temp_modifier += 15

    if Situation == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in JeanX.Traits:
        $ temp_modifier += (5*Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JeanX.Traits:
        $ temp_modifier -= 40
    if JeanX.ForcedCount and not JeanX.Forced:
        $ temp_modifier -= 5 * JeanX.ForcedCount

    if JeanX.Taboo and "tabno" in JeanX.DailyActions:
        $ temp_modifier -= 10

    if "no dildo" in JeanX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no dildo" in JeanX.RecentActions else 0

    $ Approval = ApprovalCheck(JeanX, 1250, TabM = 4) # 125, 140, 155, Taboo -160(335)

    if Situation == JeanX:                                                                  #Jean auto-starts
                if Approval > 2:                                                      # fix, add Jean auto stuff here
                    if JeanX.PantsNum() == 5:
                        "[JeanX.Name] grabs her dildo, hiking up her skirt as she does."
                        $ JeanX.Upskirt = 1
                    elif JeanX.PantsNum() >= 6:
                        "[JeanX.Name] grabs her dildo, pulling down her pants as she does."
                        $ JeanX.Legs = 0
                    else:
                        "[JeanX.Name] grabs her dildo, rubbing is suggestively against her crotch."
                    $ JeanX.SeenPanties = 1
                    call Jean_First_Bottomless(1)
                    "She slides the tip along her pussy and seems to want you to insert it."
                    menu:
                        "What do you do?"
                        "Nothing.":
                            $ JeanX.Statup("Inbt", 80, 3)
                            $ JeanX.Statup("Inbt", 50, 2)
                            "[JeanX.Name] slides it in."
                        "Go for it.":
                            $ JeanX.FaceChange("sexy", 1)
                            $ JeanX.Statup("Inbt", 80, 3)
                            ch_p "Oh yeah, [JeanX.Pet], let's do this."
                            $ JeanX.NameCheck() #checks reaction to petname
                            "You grab the dildo and slide it in."
                            $ JeanX.Statup("Love", 85, 1)
                            $ JeanX.Statup("Obed", 90, 1)
                            $ JeanX.Statup("Obed", 50, 2)
                        "Ask her to stop.":
                            $ JeanX.FaceChange("surprised")
                            $ JeanX.Statup("Inbt", 70, 1)
                            ch_p "Let's not do that right now, [JeanX.Pet]."
                            $ JeanX.NameCheck() #checks reaction to petname
                            "[JeanX.Name] sets the dildo down."
                            $ JeanX.OutfitChange()
                            $ JeanX.Statup("Obed", 90, 1)
                            $ JeanX.Statup("Obed", 50, 1)
                            $ JeanX.Statup("Obed", 30, 2)
                            return
                    jump Jean_DP_Prep
                else:
                    $ temp_modifier = 0                               # fix, add Jean auto stuff here
                    $ Trigger2 = 0
                return

    if Situation == "auto":
                "You rub the dildo across her body, and along her moist slit."
                $ JeanX.FaceChange("surprised", 1)

                if (JeanX.DildoP and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
                    "[JeanX.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                    $ JeanX.FaceChange("sexy")
                    $ JeanX.Statup("Obed", 70, 3)
                    $ JeanX.Statup("Inbt", 50, 3)
                    $ JeanX.Statup("Inbt", 70, 1)
                    ch_j "Ooo, [JeanX.Petname], toys!"
                    jump Jean_DP_Prep
                else:                                                                                                            #she's questioning it
                    $ JeanX.Brows = "angry"
                    menu:
                        ch_j "Hey, what are you planning to do with that?!"
                        "Sorry, sorry! Never mind.":
                            if Approval:
                                $ JeanX.FaceChange("sexy", 1)
                                $ JeanX.Statup("Obed", 70, 3)
                                $ JeanX.Statup("Inbt", 50, 3)
                                $ JeanX.Statup("Inbt", 70, 1)
                                ch_j "Well, now that you mention it. . ."
                                jump Jean_DP_Prep
                            "You pull back before you really get it in."
                            $ JeanX.FaceChange("bemused", 1)
                            if JeanX.DildoP:
                                ch_j "Well ok, [JeanX.Petname], maybe warn me next time?"
                            else:
                                ch_j "Well ok, [JeanX.Petname], that's a little much. . . for now . . ."
                        "Just playing with my favorite toys.":
                            $ JeanX.Statup("Love", 80, -10, 1)
                            $ JeanX.Statup("Love", 200, -10)
                            "You press it inside some more."
                            $ JeanX.Statup("Obed", 70, 3)
                            $ JeanX.Statup("Inbt", 50, 3)
                            if not ApprovalCheck(JeanX, 700, "O", TabM=1): #Checks if Obed is 700+
                                $ JeanX.FaceChange("angry")
                                "[JeanX.Name] shoves you away and slaps you in the face."
                                ch_j "Jerk!"
                                ch_j "Ask nice if you want to stick something in my pussy!"
                                $ JeanX.Statup("Love", 50, -10, 1)
                                $ JeanX.Statup("Obed", 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                if renpy.showing("Jean_SexSprite"):
                                    call Jean_Sex_Reset
                                $ JeanX.RecentActions.append("angry")
                                $ JeanX.DailyActions.append("angry")
                            else:
                                $ JeanX.FaceChange("sad")
                                "[JeanX.Name] doesn't seem to be into this, you're lucky she's so obedient."
                                jump Jean_DP_Prep
                return
    #end Auto

    if not JeanX.DildoP:
            #first time
            $ JeanX.FaceChange("surprised", 1)
            $ JeanX.Mouth = "kiss"
            ch_j "Hmmm, so you'd like to try out some toys?"
            if JeanX.Forced:
                $ JeanX.FaceChange("sad")
                ch_j "I suppose there are worst things you could ask for."

    if not JeanX.DildoP and Approval:
            #First time dialog
            if JeanX.Forced:
                $ JeanX.FaceChange("sad")
                $ JeanX.Statup("Love", 70, -3, 1)
                $ JeanX.Statup("Love", 20, -2, 1)
            elif JeanX.Love >= (JeanX.Obed + JeanX.Inbt - JeanX.IX):
                $ JeanX.FaceChange("sexy")
                $ JeanX.Brows = "sad"
                $ JeanX.Mouth = "smile"
                ch_j "I've had a reasonable amount of experience with these, you know. . ."
            elif JeanX.Obed >= (JeanX.Inbt - JeanX.IX):
                $ JeanX.FaceChange("normal")
                ch_j "If that's what you want, [JeanX.Petname]. . ."
            else: # Uninhibited
                $ JeanX.FaceChange("sad")
                $ JeanX.Mouth = "smile"
                ch_j "I guess it could be fun with a partner. . ."

    elif Approval:
            #Second time+ dialog
            if JeanX.Forced:
                $ JeanX.FaceChange("sad")
                $ JeanX.Statup("Love", 70, -3, 1)
                $ JeanX.Statup("Love", 20, -2, 1)
                ch_j "The toys again?"
            elif not JeanX.Taboo and "tabno" in JeanX.DailyActions:
                ch_j "Well, at least you got us some privacy this time. . ."
            elif "dildo pussy" in JeanX.RecentActions:
                $ JeanX.FaceChange("sexy", 1)
                ch_j "Mmm, again? Ok, let's get to it."
                jump Jean_DP_Prep
            elif "dildo pussy" in JeanX.DailyActions:
                $ JeanX.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Breaking out the toys again?",
                    "Didn't get enough earlier?",
                    "You're going to wear me out."])
                ch_j "[Line]"
            elif JeanX.DildoP < 3:
                $ JeanX.FaceChange("sexy", 1)
                $ JeanX.Brows = "confused"
                $ JeanX.Mouth = "kiss"
                ch_j "You want to stick it in my pussy again?"
            else:
                $ JeanX.FaceChange("sexy", 1)
                $ JeanX.ArmPose = 2
                $ Line = renpy.random.choice(["You want some of this action?",
                    "So you'd like another go?",
                    "You want to stick it in my pussy again?",
                    "You want me ta lube up your toy?"])
                ch_j "[Line]"
                $ Line = 0

    if Approval >= 2:
            #She's into it. . .
            if JeanX.Forced:
                $ JeanX.FaceChange("sad")
                $ JeanX.Statup("Obed", 90, 1)
                $ JeanX.Statup("Inbt", 60, 1)
                ch_j "Ok, fine."
            else:
                $ JeanX.FaceChange("sexy", 1)
                $ JeanX.Statup("Love", 90, 1)
                $ JeanX.Statup("Inbt", 50, 3)
                $ Line = renpy.random.choice(["Well, sure, stick it in.",
                    "Well. . . ok.",
                    "Sure!",
                    "I guess I could. . . stick it in.",
                    "Hells yeah.",
                    "Heh, ok, ok."])
                ch_j "[Line]"
                $ Line = 0
            $ JeanX.Statup("Obed", 20, 1)
            $ JeanX.Statup("Obed", 60, 1)
            $ JeanX.Statup("Inbt", 70, 2)
            jump Jean_DP_Prep

    else:
            #She's not into it, but maybe. . .
            $ JeanX.FaceChange("angry")
            if "no dildo" in JeanX.RecentActions:
                ch_j "What part of \"no,\" did you not get, [JeanX.Petname]?"
            elif JeanX.Taboo and "tabno" in JeanX.DailyActions and "no dildo" in JeanX.DailyActions:
                ch_j "Stop swinging that thing around in public!"
            elif "no dildo" in JeanX.DailyActions:
                ch_j "I already told you \"no,\" [JeanX.Petname]."
            elif JeanX.Taboo and "tabno" in JeanX.DailyActions:
                ch_j "Stop swinging that thing around in public!"
            elif not JeanX.DildoP:
                $ JeanX.FaceChange("bemused")
                ch_j "I'm just not into toys, [JeanX.Petname]. . ."
            else:
                $ JeanX.FaceChange("bemused")
                ch_j "I don't think we need any toys, [JeanX.Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in JeanX.DailyActions:
                    $ JeanX.FaceChange("bemused")
                    ch_j "Yeah, ok, [JeanX.Petname]."
                    return
                "Maybe later?" if "no dildo" not in JeanX.DailyActions:
                    $ JeanX.FaceChange("sexy")
                    ch_j "Maybe I'll practice on my own time, [JeanX.Petname]."
                    $ JeanX.Statup("Love", 80, 2)
                    $ JeanX.Statup("Inbt", 70, 2)
                    if JeanX.Taboo:
                        $ JeanX.RecentActions.append("tabno")
                        $ JeanX.DailyActions.append("tabno")
                    $ JeanX.RecentActions.append("no dildo")
                    $ JeanX.DailyActions.append("no dildo")
                    return
                "I think you'd like it. . .":
                    if Approval:
                        $ JeanX.FaceChange("sexy")
                        $ JeanX.Statup("Obed", 90, 2)
                        $ JeanX.Statup("Obed", 50, 2)
                        $ JeanX.Statup("Inbt", 70, 3)
                        $ JeanX.Statup("Inbt", 40, 2)
                        $ Line = renpy.random.choice(["Well, sure, stick it in.",
                            "I suppose. . .",
                            "You've got me there."])
                        ch_j "[Line]"
                        $ Line = 0
                        jump Jean_DP_Prep
                    else:
                        pass

                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck(JeanX, 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                    if Approval > 1 or (Approval and JeanX.Forced):
                        $ JeanX.FaceChange("sad")
                        $ JeanX.Statup("Love", 70, -5, 1)
                        $ JeanX.Statup("Love", 200, -5)
                        ch_j "Ok, fine. If we're going to do this, stick it in already."
                        $ JeanX.Statup("Obed", 80, 4)
                        $ JeanX.Statup("Inbt", 80, 1)
                        $ JeanX.Statup("Inbt", 60, 3)
                        $ JeanX.Forced = 1
                        jump Jean_DP_Prep
                    else:
                        $ JeanX.Statup("Love", 200, -20)
                        $ JeanX.RecentActions.append("angry")
                        $ JeanX.DailyActions.append("angry")

    #She refused all offers.
    $ JeanX.ArmPose = 1
    if "no dildo" in JeanX.DailyActions:
            ch_j "Learn to take \"no\" for an answer, [JeanX.Petname]."
            $ JeanX.RecentActions.append("angry")
            $ JeanX.DailyActions.append("angry")
    elif JeanX.Forced:
            $ JeanX.FaceChange("angry", 1)
            ch_j "I'm not going to let you use that on me."
            $ JeanX.Statup("Lust", 200, 5)
            if JeanX.Love > 300:
                    $ JeanX.Statup("Love", 70, -2)
            $ JeanX.Statup("Obed", 50, -2)
            $ JeanX.RecentActions.append("angry")
            $ JeanX.DailyActions.append("angry")
    elif JeanX.Taboo:                             # she refuses and this is too public a place for her
            $ JeanX.FaceChange("angry", 1)
            $ JeanX.RecentActions.append("tabno")
            $ JeanX.DailyActions.append("tabno")
            ch_j "Not here!"
            $ JeanX.Statup("Lust", 200, 5)
            $ JeanX.Statup("Obed", 50, -3)
    elif JeanX.DildoP:
            $ JeanX.FaceChange("sad")
            ch_j "Sorry, you can keep your toys to yourself."
    else:
            $ JeanX.FaceChange("normal", 1)
            ch_j "No way."
    $ JeanX.RecentActions.append("no dildo")
    $ JeanX.DailyActions.append("no dildo")
    $ temp_modifier = 0
    return

label Jean_DP_Prep: #Animation set-up
    if Trigger2 == "dildo pussy":
        return

    if not JeanX.Forced and Situation != "auto":
        $ temp_modifier = 15 if JeanX.PantsNum() >= 6 else 0
        call Bottoms_Off(JeanX)
        if "angry" in JeanX.RecentActions:
            return

    $ temp_modifier = 0
    call Jean_Pussy_Launch("dildo pussy")
    if not JeanX.DildoP:
        if JeanX.Forced:
            $ JeanX.Statup("Love", 90, -75)
            $ JeanX.Statup("Obed", 70, 60)
            $ JeanX.Statup("Inbt", 80, 35)
        else:
            $ JeanX.Statup("Love", 90, 10)
            $ JeanX.Statup("Obed", 70, 20)
            $ JeanX.Statup("Inbt", 80, 45)
    if JeanX.Taboo:
        $ JeanX.Statup("Inbt", 90, int(Taboo/10))
        $ JeanX.Statup("Lust", 50, int(Taboo/5))


    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if JeanX.Taboo:
        $ JeanX.DrainWord("tabno")
    $ JeanX.DrainWord("no dildo")
    $ JeanX.RecentActions.append("dildo pussy")
    $ JeanX.DailyActions.append("dildo pussy")

label Jean_DP_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(JeanX)
        call Jean_Pussy_Launch("dildo pussy")
        $ JeanX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                call Slap_Ass(JeanX)
                                jump Jean_DP_Cycle

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
                                            if JeanX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ JeanX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Shift primary action":
                                            if JeanX.Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in her ass.":
                                                                $ Situation = "shift"
                                                                call Jean_DP_After
                                                                call Jean_Insert_Ass
                                                        "Just stick a finger in her ass without asking.":
                                                                $ Situation = "auto"
                                                                call Jean_DP_After
                                                                call Jean_Insert_Ass
                                                        "I want to shift the dildo to her ass.":
                                                                $ Situation = "shift"
                                                                call Jean_DP_After
                                                                call Jean_Dildo_Ass
                                                        "Never Mind":
                                                                jump Jean_DP_Cycle
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Jean_DP_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [JeanX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(JeanX)
                                            "Ask [JeanX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(JeanX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(JeanX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jean_DP_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jean_DP_Cycle
                                            "Never mind":
                                                        jump Jean_DP_Cycle
                                    "undress [JeanX.Name]":
                                            call Girl_Undress(JeanX)
                                    "Clean up [JeanX.Name] (locked)" if not JeanX.Spunk:
                                            pass
                                    "Clean up [JeanX.Name]" if JeanX.Spunk:
                                            call Girl_Cleanup(JeanX,"ask")
                                    "Never mind":
                                            jump Jean_DP_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Jean_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Jean_DP_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Jean_Pos_Reset
                                    $ Line = 0
                                    jump Jean_DP_After
        #End menu (if Line)

        if JeanX.Panties or JeanX.PantsNum() >= 6 or JeanX.HoseNum() >= 5: #This checks if Jean wants to strip down.
                call Girl_Undress(JeanX,"auto")

        call Shift_Focus(JeanX)
        call Sex_Dialog(JeanX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JeanX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JeanX)
                            if "angry" in JeanX.RecentActions:
                                call Jean_Pos_Reset
                                return
                            $ JeanX.Statup("Lust", 200, 5)
                            if 100 > JeanX.Lust >= 70 and JeanX.OCount < 2:
                                $ JeanX.RecentActions.append("unsatisfied")
                                $ JeanX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jean_DP_After
                            $ Line = "came"

                    if JeanX.Lust >= 100:
                            #If Jean can cum
                            call Girl_Cumming(JeanX)
                            if Situation == "shift" or "angry" in JeanX.RecentActions:
                                jump Jean_DP_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in JeanX.RecentActions:#And Jean is unsatisfied,
                                "[JeanX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Jean_DP_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if JeanX.SEXP >= 100 or ApprovalCheck(JeanX, 1200, "LO"):
            pass
        elif Cnt == (5 + JeanX.DildoP):
                    $ JeanX.Brows = "confused"
                    ch_j "What are you even doing down there?"
        elif JeanX.Lust >= 80:
                    pass
        elif Cnt == (15 + JeanX.DildoP) and JeanX.SEXP >= 15 and not ApprovalCheck(JeanX, 1500):
                    $ JeanX.Brows = "confused"
                    menu:
                        ch_j "[JeanX.Petname], this is getting uncomfortable, maybe we could try something else."
                        "Finish up.":
                                "You let go. . ."
                                jump Jean_DP_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Jean_DP_After
                        "No, this is fun.":
                                if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                                    $ JeanX.Statup("Love", 200, -5)
                                    $ JeanX.Statup("Obed", 50, 3)
                                    $ JeanX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ JeanX.FaceChange("angry", 1)
                                    call Jean_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_j "Well if that's your attitude, I don't need your \"help\"."
                                    $ JeanX.Statup("Love", 50, -3, 1)
                                    $ JeanX.Statup("Love", 80, -4, 1)
                                    $ JeanX.Statup("Obed", 30, -1, 1)
                                    $ JeanX.Statup("Obed", 50, -1, 1)
                                    $ JeanX.RecentActions.append("angry")
                                    $ JeanX.DailyActions.append("angry")
                                    jump Jean_DP_After
        #End Count check

        if Round == 10:
                call Sex_Basic_Dialog(JeanX,10) #"You might want to wrap this up, it's getting late."
        elif Round == 5:
                call Sex_Basic_Dialog(JeanX,5)   #"Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ JeanX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(JeanX,"done")   #"Ok, [Girl.Petname], that's enough of that for now."

label Jean_DP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Jean_Pos_Reset

    $ JeanX.FaceChange("sexy")

    $ JeanX.DildoP += 1
    $ JeanX.Action -=1

    call Partner_Like(JeanX,1)

    if JeanX.DildoP == 1:
            $ JeanX.SEXP += 10
            if not Situation:
                if JeanX.Love >= 500 and "unsatisfied" not in JeanX.RecentActions:
                    ch_j "Thanks for the extra hand. . ."
                elif JeanX.Obed <= 500 and Player.Focus <= 20:
                    $ JeanX.FaceChange("perplexed", 1)
                    ch_j "Did you like that?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_j "Mmm, so what else did you have in mind?"
    call Checkout
    return

# end JeanX.Dildo Pussy /////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////Start Insert Ass

label Jean_Dildo_Ass:

    ch_j "You know what? I'm just not into this right now. . ."
    "[[not yet implemented]"
    return

    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JeanX)
    call Jean_Dildo_Check
    if not _return:
        return

    if JeanX.Loose:
        $ temp_modifier += 30
    elif "anal" in JeanX.RecentActions or "dildo anal" in JeanX.RecentActions:
        $ temp_modifier -= 20
    elif "anal" in JeanX.DailyActions or "dildo anal" in JeanX.DailyActions:
        $ temp_modifier -= 10
    elif (JeanX.Anal + JeanX.DildoA + JeanX.Plug) > 0: #You've done it before
        $ temp_modifier += 20

    if JeanX.Legs == "pants:": # she's got pants on.
        $ temp_modifier -= 20

    if JeanX.Lust > 95:
        $ temp_modifier += 20
    elif JeanX.Lust > 85: #She's really horny
        $ temp_modifier += 15

    if Situation == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in JeanX.Traits:
        $ temp_modifier += (5*Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JeanX.Traits:
        $ temp_modifier -= 40
    if JeanX.ForcedCount and not JeanX.Forced:
        $ temp_modifier -= 5 * JeanX.ForcedCount

    if JeanX.Taboo and "tabno" in JeanX.DailyActions:
        $ temp_modifier -= 10

    if "no dildo" in JeanX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no dildo" in JeanX.RecentActions else 0

    $ Approval = ApprovalCheck(JeanX, 1450, TabM = 4) # 145, 160, 175, Taboo -160(355)

    if Situation == JeanX:
            #Jean auto-starts
            if Approval > 2:                                                      # fix, add Jean auto stuff here
                if JeanX.PantsNum() == 5:
                    "[JeanX.Name] grabs her dildo, hiking up her skirt as she does."
                    $ JeanX.Upskirt = 1
                elif JeanX.PantsNum() >= 6:
                    "[JeanX.Name] grabs her dildo, pulling down her pants as she does."
                    $ JeanX.Legs = 0
                else:
                    "[JeanX.Name] grabs her dildo, rubbing is suggestively against her ass."
                $ JeanX.SeenPanties = 1
                call Jean_First_Bottomless(1)
                "She slides the tip against her asshole, and seems to want you to insert it."
                menu:
                    "What do you do?"
                    "Nothing.":
                        $ JeanX.Statup("Inbt", 80, 3)
                        $ JeanX.Statup("Inbt", 50, 2)
                        "[JeanX.Name] slides it in."
                    "Go for it.":
                        $ JeanX.FaceChange("sexy", 1)
                        $ JeanX.Statup("Inbt", 80, 3)
                        ch_p "Oh yeah, [JeanX.Pet], let's do this."
                        $ JeanX.NameCheck() #checks reaction to petname
                        "You grab the dildo and slide it in."
                        $ JeanX.Statup("Love", 85, 1)
                        $ JeanX.Statup("Obed", 90, 1)
                        $ JeanX.Statup("Obed", 50, 2)
                    "Ask her to stop.":
                        $ JeanX.FaceChange("surprised")
                        $ JeanX.Statup("Inbt", 70, 1)
                        ch_p "Let's not do that right now, [JeanX.Pet]."
                        $ JeanX.NameCheck() #checks reaction to petname
                        "[JeanX.Name] sets the dildo down."
                        $ JeanX.OutfitChange()
                        $ JeanX.Statup("Obed", 90, 1)
                        $ JeanX.Statup("Obed", 50, 1)
                        $ JeanX.Statup("Obed", 30, 2)
                        return
                jump Jean_DA_Prep
            else:
                $ temp_modifier = 0                               # fix, add Jean auto stuff here
                $ Trigger2 = 0
            return

    if Situation == "auto":
            "You rub the dildo across her body, and against her tight anus."
            $ JeanX.FaceChange("surprised", 1)

            if (JeanX.DildoA and Approval) or (Approval > 1):
                #this is not the first time you've had sex, or she's into it
                "[JeanX.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                $ JeanX.FaceChange("sexy")
                $ JeanX.Statup("Obed", 70, 3)
                $ JeanX.Statup("Inbt", 50, 3)
                $ JeanX.Statup("Inbt", 70, 1)
                ch_j "Ooo, [JeanX.Petname], toys!"
                jump Jean_DA_Prep
            else:
                #she's questioning it
                $ JeanX.Brows = "angry"
                menu:
                    ch_j "Hey, what are you planning to do with that?!"
                    "Sorry, sorry! Never mind.":
                        if Approval:
                            $ JeanX.FaceChange("sexy", 1)
                            $ JeanX.Statup("Obed", 70, 3)
                            $ JeanX.Statup("Inbt", 50, 3)
                            $ JeanX.Statup("Inbt", 70, 1)
                            ch_j "Well, now that you mention it. . ."
                            jump Jean_DA_Prep
                        "You pull back before you really get it in."
                        $ JeanX.FaceChange("bemused", 1)
                        if JeanX.DildoA:
                            ch_j "Well ok, [JeanX.Petname], maybe warn me next time?"
                        else:
                            ch_j "Well ok, [JeanX.Petname], that's a little much. . . for now . . ."
                    "Just playing with my favorite toys.":
                        $ JeanX.Statup("Love", 80, -10, 1)
                        $ JeanX.Statup("Love", 200, -10)
                        "You press it inside some more."
                        $ JeanX.Statup("Obed", 70, 3)
                        $ JeanX.Statup("Inbt", 50, 3)
                        if not ApprovalCheck(JeanX, 700, "O", TabM=1): #Checks if Obed is 700+
                            $ JeanX.FaceChange("angry")
                            "[JeanX.Name] shoves you away and slaps you in the face."
                            ch_j "Jerk!"
                            ch_j "Ask nice if you want to stick something in my ass!"
                            $ JeanX.Statup("Love", 50, -10, 1)
                            $ JeanX.Statup("Obed", 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            if renpy.showing("Jean_SexSprite"):
                                call Jean_Sex_Reset
                            $ JeanX.RecentActions.append("angry")
                            $ JeanX.DailyActions.append("angry")
                        else:
                            $ JeanX.FaceChange("sad")
                            "[JeanX.Name] doesn't seem to be into this, you're lucky she's so obedient."
                            jump Jean_DA_Prep
            return
    #end auto

    if not JeanX.DildoA:
            #first time
            $ JeanX.FaceChange("surprised", 1)
            $ JeanX.Mouth = "kiss"
            ch_j "You want to try and fit that. . .?"
            if JeanX.Forced:
                $ JeanX.FaceChange("sad")
                ch_j "Always about the butt, huh?"

    if not JeanX.Loose and ("dildo anal" in JeanX.RecentActions or "anal" in JeanX.RecentActions or "dildo anal" in JeanX.DailyActions or "anal" in JeanX.DailyActions):
            $ JeanX.FaceChange("bemused", 1)
            ch_j "I'm still sore from earlier. . ."

    if not JeanX.DildoA and Approval:
            #First time dialog
            if JeanX.Forced:
                $ JeanX.FaceChange("sad")
                $ JeanX.Statup("Love", 70, -3, 1)
                $ JeanX.Statup("Love", 20, -2, 1)
            elif JeanX.Love >= (JeanX.Obed + JeanX.Inbt - JeanX.IX):
                $ JeanX.FaceChange("sexy")
                $ JeanX.Brows = "sad"
                $ JeanX.Mouth = "smile"
                ch_j "I haven't actually used one of these, back there before. . ."
            elif JeanX.Obed >= (JeanX.Inbt - JeanX.IX):
                $ JeanX.FaceChange("normal")
                ch_j "If that's what you want, [JeanX.Petname]. . ."
            else: # Uninhibited
                $ JeanX.FaceChange("sad")
                $ JeanX.Mouth = "smile"
                ch_j "I guess it could be fun two-player. . ."

    elif Approval:
            #Second time+ dialog
            if JeanX.Forced:
                $ JeanX.FaceChange("sad")
                $ JeanX.Statup("Love", 70, -3, 1)
                $ JeanX.Statup("Love", 20, -2, 1)
                ch_j "The toys again?"
            elif not JeanX.Taboo and "tabno" in JeanX.DailyActions:
                ch_j "Well, at least you got us some privacy this time. . ."
            elif "dildo anal" in JeanX.DailyActions and not JeanX.Loose:
                pass
            elif "dildo anal" in JeanX.DailyActions:
                $ JeanX.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Breaking out the toys again?",
                    "Didn't get enough earlier?",
                    "I'm still a bit sore from earlier.",
                    "You're going to wear me out."])
                ch_j "[Line]"
            elif JeanX.DildoA < 3:
                $ JeanX.FaceChange("sexy", 1)
                $ JeanX.Brows = "confused"
                $ JeanX.Mouth = "kiss"
                ch_j "You want to stick it in my ass again?"
            else:
                $ JeanX.FaceChange("sexy", 1)
                $ JeanX.ArmPose = 2
                $ Line = renpy.random.choice(["You want some of this action?",
                    "So you'd like another go?",
                    "You want to stick it in my ass again?",
                    "You want me ta lube up your toy?"])
                ch_j "[Line]"
                $ Line = 0

    if Approval >= 2:
            #She's into it. . .
            if JeanX.Forced:
                $ JeanX.FaceChange("sad")
                $ JeanX.Statup("Obed", 90, 1)
                $ JeanX.Statup("Inbt", 60, 1)
                ch_j "Ok, fine."
            else:
                $ JeanX.FaceChange("sexy", 1)
                $ JeanX.Statup("Love", 90, 1)
                $ JeanX.Statup("Inbt", 50, 3)
                $ Line = renpy.random.choice(["Well, sure, stick it in.",
                    "Well. . . ok.",
                    "Sure!",
                    "I guess I could. . . stick it in.",
                    "Hells yeah.",
                    "Heh, ok, ok."])
                ch_j "[Line]"
                $ Line = 0
            $ JeanX.Statup("Obed", 20, 1)
            $ JeanX.Statup("Obed", 60, 1)
            $ JeanX.Statup("Inbt", 70, 2)
            jump Jean_DA_Prep

    else:
            #She's not into it, but maybe. . .
            $ JeanX.FaceChange("angry")
            if "no dildo" in JeanX.RecentActions:
                ch_j "What part of \"no,\" did you not get, [JeanX.Petname]?"
            elif JeanX.Taboo and "tabno" in JeanX.DailyActions and "no dildo" in JeanX.DailyActions:
                ch_j "Stop swinging that thing around in public!"
            elif "no dildo" in JeanX.DailyActions:
                ch_j "I already told you \"no,\" [JeanX.Petname]."
            elif JeanX.Taboo and "tabno" in JeanX.DailyActions:
                ch_j "I already told you that I wouldn't do that out here!"
            elif not JeanX.DildoA:
                $ JeanX.FaceChange("bemused")
                ch_j "I'm just not into toys, [JeanX.Petname]. . ."
            elif not JeanX.Loose and "dildo anal" not in JeanX.DailyActions:
                $ JeanX.FaceChange("perplexed")
                ch_j "You could have been a bit more gentle last time, [JeanX.Petname]. . ."
            else:
                $ JeanX.FaceChange("bemused")
                ch_j "I don't think we need any toys, [JeanX.Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in JeanX.DailyActions:
                    $ JeanX.FaceChange("bemused")
                    ch_j "Yeah, ok, [JeanX.Petname]."
                    return
                "Maybe later?" if "no dildo" not in JeanX.DailyActions:
                    $ JeanX.FaceChange("sexy")
                    ch_j "Maybe I'll practice on my own time, [JeanX.Petname]."
                    $ JeanX.Statup("Love", 80, 2)
                    $ JeanX.Statup("Inbt", 70, 2)
                    if JeanX.Taboo:
                        $ JeanX.RecentActions.append("tabno")
                        $ JeanX.DailyActions.append("tabno")
                    $ JeanX.RecentActions.append("no dildo")
                    $ JeanX.DailyActions.append("no dildo")
                    return
                "I think you'd like it. . .":
                    if Approval:
                        $ JeanX.FaceChange("sexy")
                        $ JeanX.Statup("Obed", 90, 2)
                        $ JeanX.Statup("Obed", 50, 2)
                        $ JeanX.Statup("Inbt", 70, 3)
                        $ JeanX.Statup("Inbt", 40, 2)
                        $ Line = renpy.random.choice(["Well, sure, stick it in.",
                            "I suppose. . .",
                            "You've got me there."])
                        ch_j "[Line]"
                        $ Line = 0
                        jump Jean_DA_Prep
                    else:
                        pass

                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck(JeanX, 1050, "OI", TabM = 3) # 105, 120, 135, -120(225)
                    if Approval > 1 or (Approval and JeanX.Forced):
                        $ JeanX.FaceChange("sad")
                        $ JeanX.Statup("Love", 70, -5, 1)
                        $ JeanX.Statup("Love", 200, -5)
                        ch_j "Ok, fine. If we're going to do this, stick it in already."
                        $ JeanX.Statup("Obed", 80, 4)
                        $ JeanX.Statup("Inbt", 80, 1)
                        $ JeanX.Statup("Inbt", 60, 3)
                        $ JeanX.Forced = 1
                        jump Jean_DA_Prep
                    else:
                        $ JeanX.Statup("Love", 200, -20)
                        $ JeanX.RecentActions.append("angry")
                        $ JeanX.DailyActions.append("angry")

    #She refused all offers.
    $ JeanX.ArmPose = 1
    if "no dildo" in JeanX.DailyActions:
            ch_j "Learn to take \"no\" for an answer, [JeanX.Petname]."
            $ JeanX.RecentActions.append("angry")
            $ JeanX.DailyActions.append("angry")
    elif JeanX.Forced:
            $ JeanX.FaceChange("angry", 1)
            ch_j "I'm not going to let you use that on me."
            $ JeanX.Statup("Lust", 200, 5)
            if JeanX.Love > 300:
                    $ JeanX.Statup("Love", 70, -2)
            $ JeanX.Statup("Obed", 50, -2)
            $ JeanX.RecentActions.append("angry")
            $ JeanX.DailyActions.append("angry")
    elif JeanX.Taboo:                             # she refuses and this is too public a place for her
            $ JeanX.FaceChange("angry", 1)
            $ JeanX.RecentActions.append("tabno")
            $ JeanX.DailyActions.append("tabno")
            ch_j "Not here!"
            $ JeanX.Statup("Lust", 200, 5)
            $ JeanX.Statup("Obed", 50, -3)
    elif not JeanX.Loose and "dildo anal" in JeanX.DailyActions:
            $ JeanX.FaceChange("bemused")
            ch_j "Sorry, I just need a little break back there, [JeanX.Petname]."
    elif JeanX.DildoA:
            $ JeanX.FaceChange("sad")
            ch_j "Sorry, you can keep your toys out of there."
    else:
            $ JeanX.FaceChange("normal", 1)
            ch_j "No way."
    $ JeanX.RecentActions.append("no dildo")
    $ JeanX.DailyActions.append("no dildo")
    $ temp_modifier = 0
    return

label Jean_DA_Prep: #Animation set-up
    if Trigger2 == "dildo anal":
        return

    if not JeanX.Forced and Situation != "auto":
        $ temp_modifier = 20 if JeanX.PantsNum() >= 6 else 0
        call Bottoms_Off(JeanX)
        if "angry" in JeanX.RecentActions:
            return

    $ temp_modifier = 0
    call Jean_Pussy_Launch("dildo anal")
    if not JeanX.DildoA:
        if JeanX.Forced:
            $ JeanX.Statup("Love", 90, -75)
            $ JeanX.Statup("Obed", 70, 60)
            $ JeanX.Statup("Inbt", 80, 35)
        else:
            $ JeanX.Statup("Love", 90, 10)
            $ JeanX.Statup("Obed", 70, 20)
            $ JeanX.Statup("Inbt", 80, 45)
    if JeanX.Taboo:
        $ JeanX.Statup("Inbt", 90, int(Taboo/10))
        $ JeanX.Statup("Lust", 50, int(Taboo/5))


    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if JeanX.Taboo:
        $ JeanX.DrainWord("tabno")
    $ JeanX.DrainWord("no dildo")
    $ JeanX.RecentActions.append("dildo anal")
    $ JeanX.DailyActions.append("dildo anal")

label Jean_DA_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(JeanX)
        call Jean_Pussy_Launch("dildo anal")
        $ JeanX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                call Slap_Ass(JeanX)
                                jump Jean_DA_Cycle

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
                                            if JeanX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ JeanX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Shift primary action":
                                            if JeanX.Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in her pussy.":
                                                                $ Situation = "shift"
                                                                call Jean_DA_After
                                                                call Jean_Fondle_Pussy
                                                        "Just stick a finger in her pussy without asking.":
                                                                $ Situation = "auto"
                                                                call Jean_DA_After
                                                                call Jean_Fondle_Pussy
                                                        "I want to shift the dildo to her pussy.":
                                                                $ Situation = "shift"
                                                                call Jean_DA_After
                                                                call Jean_Dildo_Pussy
                                                        "Never Mind":
                                                                jump Jean_DA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Jean_DA_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [JeanX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(JeanX)
                                            "Ask [JeanX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(JeanX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(JeanX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jean_DA_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jean_DA_Cycle
                                    "Never mind":
                                            jump Jean_DA_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Jean_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Jean_DA_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Jean_Pos_Reset
                                    $ Line = 0
                                    jump Jean_DA_After
        #End menu (if Line)

        if JeanX.Panties or JeanX.PantsNum() >= 6 or JeanX.HoseNum() >= 5: #This checks if Jean wants to strip down.
                call Girl_Undress(JeanX,"auto")

        call Shift_Focus(JeanX)
        call Sex_Dialog(JeanX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JeanX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JeanX)
                            if "angry" in JeanX.RecentActions:
                                call Jean_Pos_Reset
                                return
                            $ JeanX.Statup("Lust", 200, 5)
                            if 100 > JeanX.Lust >= 70 and JeanX.OCount < 2:
                                $ JeanX.RecentActions.append("unsatisfied")
                                $ JeanX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jean_DA_After
                            $ Line = "came"

                    if JeanX.Lust >= 100:
                            #If Jean can cum
                            call Girl_Cumming(JeanX)
                            if Situation == "shift" or "angry" in JeanX.RecentActions:
                                jump Jean_DA_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in JeanX.RecentActions:#And Jean is unsatisfied,
                                "[JeanX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Jean_DA_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if JeanX.SEXP >= 100 or ApprovalCheck(JeanX, 1200, "LO"):
            pass
        elif Cnt == (5 + JeanX.DildoA):
                    $ JeanX.Brows = "confused"
                    ch_j "What are you even doing down there?"
        elif JeanX.Lust >= 80:
                    pass
        elif Cnt == (15 + JeanX.DildoA) and JeanX.SEXP >= 15 and not ApprovalCheck(JeanX, 1500):
                    $ JeanX.Brows = "confused"
                    menu:
                        ch_j "[JeanX.Petname], this is getting uncomfortable, maybe we could try something else."
                        "Finish up.":
                                "You let go. . ."
                                jump Jean_DA_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Jean_DA_After
                        "No, this is fun.":
                                if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                                    $ JeanX.Statup("Love", 200, -5)
                                    $ JeanX.Statup("Obed", 50, 3)
                                    $ JeanX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ JeanX.FaceChange("angry", 1)
                                    call Jean_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_j "Well if that's your attitude, I don't need your \"help\"."
                                    $ JeanX.Statup("Love", 50, -3, 1)
                                    $ JeanX.Statup("Love", 80, -4, 1)
                                    $ JeanX.Statup("Obed", 30, -1, 1)
                                    $ JeanX.Statup("Obed", 50, -1, 1)
                                    $ JeanX.RecentActions.append("angry")
                                    $ JeanX.DailyActions.append("angry")
                                    jump Jean_DA_After
        #End Count check

        if Round == 10:
                call Sex_Basic_Dialog(JeanX,10) #"You might want to wrap this up, it's getting late."
        elif Round == 5:
                call Sex_Basic_Dialog(JeanX,5)   #"Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ JeanX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(JeanX,"done")   #"Ok, [Girl.Petname], that's enough of that for now."

label Jean_DA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Jean_Pos_Reset

    $ JeanX.FaceChange("sexy")

    $ JeanX.DildoA += 1
    $ JeanX.Action -=1

    call Partner_Like(JeanX,1)

    if JeanX.DildoA == 1:
            $ JeanX.SEXP += 10
            if not Situation:
                if JeanX.Love >= 500 and "unsatisfied" not in JeanX.RecentActions:
                    if JeanX.Loose:
                        ch_j "That was. . . interesting. . ."
                    else:
                        ch_j "Ouch. . ."
                elif JeanX.Obed <= 500 and Player.Focus <= 20:
                    $ JeanX.FaceChange("perplexed", 1)
                    ch_j "Did you like that?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_j "Mmm, so what else did you have in mind?"
    call Checkout
    return

# end JeanX.Dildo Ass /////////////////////////////////////////////////////////////////////////////

label Jean_Vibrator_Check:                                                                                 #fix this whole section is copy/paste unfinished
    if "vibrator" in Player.Inventory:
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in JeanX.Inventory:
        "You ask [JeanX.Name] to get out her vibrator."
    else:
        "You don't have one of those on you."
        return 0
    return 1

## JeanX.Footjob //////////////////////////////////////////////////////////////////////
label Jean_Footjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JeanX)
    if JeanX.Foot >= 7: # She loves it
        $ temp_modifier += 10
    elif JeanX.Foot >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif JeanX.Foot: #You've done it before
        $ temp_modifier += 3

    if JeanX.Addict >= 75 and JeanX.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 10
    if JeanX.Addict >= 75:
        $ temp_modifier += 5

    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in JeanX.Traits:
        $ temp_modifier += (3*Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JeanX.Traits:
        $ temp_modifier -= 40
    if JeanX.ForcedCount and not JeanX.Forced:
        $ temp_modifier -= 5 * JeanX.ForcedCount

    if JeanX.Taboo and "tabno" in JeanX.DailyActions:
        $ temp_modifier -= 10

    if "no foot" in JeanX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no foot" in JeanX.RecentActions else 0

    $ Approval = ApprovalCheck(JeanX, 1250, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if Situation == JeanX:                                                                  #Jean auto-starts
        if Approval > 2:                                                      # fix, add Jean auto stuff here
            "[JeanX.Name] leans back  and starts rubbing your cock with her foot."
            menu:
                "What do you do?"
                "Nothing.":
                    $ JeanX.Statup("Inbt", 70, 3)
                    $ JeanX.Statup("Inbt", 30, 2)
                    "[JeanX.Name] continues her actions."
                "Praise her.":
                    $ JeanX.FaceChange("sexy", 1)
                    $ JeanX.Statup("Inbt", 70, 3)
                    ch_p "Oooh, that's good, [JeanX.Pet]."
                    $ JeanX.NameCheck() #checks reaction to petname
                    "[JeanX.Name] continues her actions."
                    $ JeanX.Statup("Love", 80, 1)
                    $ JeanX.Statup("Obed", 90, 1)
                    $ JeanX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ JeanX.FaceChange("surprised")
                    $ JeanX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [JeanX.Pet]."
                    $ JeanX.NameCheck() #checks reaction to petname
                    "[JeanX.Name] puts it down."
                    $ JeanX.Statup("Obed", 90, 1)
                    $ JeanX.Statup("Obed", 50, 1)
                    $ JeanX.Statup("Obed", 30, 2)
                    return
            if Trigger:
                $ Trigger3 = "foot"
                return
            jump Jean_FJ_Prep
        else:
            $ temp_modifier = 0                               # fix, add Jean auto stuff here
            $ Trigger2 = 0
            return

    if not JeanX.Foot and "no foot" not in JeanX.RecentActions:
        $ JeanX.FaceChange("confused", 2)
        ch_j "Oh, a foot person, eh?"
        $ JeanX.Blush = 1

    if not JeanX.Foot and Approval:                                                 #First time dialog
        if JeanX.Forced:
            $ JeanX.FaceChange("sad",1)
            $ JeanX.Statup("Love", 70, -3, 1)
            $ JeanX.Statup("Love", 20, -2, 1)
        elif JeanX.Love >= (JeanX.Obed + JeanX.Inbt - JeanX.IX):
            $ JeanX.FaceChange("sexy",1)
            $ JeanX.Brows = "sad"
            $ JeanX.Mouth = "smile"
            ch_j "I suppose. . ."
        elif JeanX.Obed >= (JeanX.Inbt - JeanX.IX):
            $ JeanX.FaceChange("normal",1)
            ch_j "If you want, [JeanX.Petname]. . ."
        elif JeanX.Addict >= 50:
            $ JeanX.FaceChange("manic", 1)
            ch_j "Okay. . ."
        else: # Uninhibited
            $ JeanX.FaceChange("lipbite",1)
            ch_j "Sure. . ."

    elif Approval:                                                                       #Second time+ dialog
        if JeanX.Forced:
            $ JeanX.FaceChange("sad")
            $ JeanX.Statup("Love", 70, -3, 1)
            $ JeanX.Statup("Love", 20, -2, 1)
            ch_j "That's it?"
        elif not JeanX.Taboo and "tabno" in JeanX.DailyActions:
            ch_j "Um, I guess we're alone enough like this. . ."
        elif "foot" in JeanX.DailyActions:
            $ JeanX.FaceChange("sexy", 1)
            ch_j "More of that, huh. . ."
            jump Jean_FJ_Prep
#        elif "foot" in JeanX.DailyActions:
#            $ JeanX.FaceChange("sexy", 1)
#            $ Line = renpy.random.choice(["Another one?",
#                "Didn't get enough earlier?",
#                "My feet are kinda sore from earlier.",
#                "My feet are kinda sore from earlier."])
#            ch_j "[Line]"
        elif JeanX.Foot < 3:
            $ JeanX.FaceChange("sexy", 1)
            $ JeanX.Brows = "confused"
            $ JeanX.Mouth = "kiss"
            ch_j "Hmm, it is kinda fun. . ."
        else:
            $ JeanX.FaceChange("sexy", 1)
            $ JeanX.ArmPose = 2
            $ Line = renpy.random.choice(["You want me to use my feet?",
                "So you'd like another footjob?",
                "A little. . . [she rubs her foot along your leg]?",
                "A little foot rub?"])
            ch_j "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if JeanX.Forced:
            $ JeanX.FaceChange("sad")
            $ JeanX.Statup("Obed", 90, 1)
            $ JeanX.Statup("Inbt", 60, 1)
            ch_j "Ok, sure."
        elif "no foot" in JeanX.DailyActions:
            ch_j "Fine."
        else:
            $ JeanX.FaceChange("sexy", 1)
            $ JeanX.Statup("Love", 90, 1)
            $ JeanX.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Sure, I guess.",
                "OK.",
                "Fine, lemme see it.",
                "I guess I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Heh, ok, ok."])
            ch_j "[Line]"
            $ Line = 0
        $ JeanX.Statup("Obed", 20, 1)
        $ JeanX.Statup("Obed", 60, 1)
        $ JeanX.Statup("Inbt", 70, 2)
        jump Jean_FJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ JeanX.FaceChange("angry")
        if "no foot" in JeanX.RecentActions:
            ch_j "Don't make me repeat myself again, [JeanX.Petname]."
        elif JeanX.Taboo and "tabno" in JeanX.DailyActions and "no foot" in JeanX.DailyActions:
            ch_j "I told you I wasn't comfortable in public. . ."
        elif "no foot" in JeanX.DailyActions:
            ch_j "I told you \"no,\" [JeanX.Petname]."
        elif JeanX.Taboo and "tabno" in JeanX.DailyActions:
            ch_j "I said not in public!"
        elif not JeanX.Foot:
            $ JeanX.FaceChange("bemused")
            ch_j "Well. . ."
        else:
            $ JeanX.FaceChange("bemused")
            ch_j "Not now, ok?"
        menu:
            extend ""
            "Sorry, never mind." if "no foot" in JeanX.DailyActions:
                $ JeanX.FaceChange("bemused")
                ch_j "Sure, it's fine."
                return
            "Maybe later?" if "no foot" not in JeanX.DailyActions:
                $ JeanX.FaceChange("sexy")
                ch_j "Well. . ."
                ch_j "Maybe."
                $ JeanX.Statup("Love", 80, 2)
                $ JeanX.Statup("Inbt", 70, 2)
                if JeanX.Taboo:
                    $ JeanX.RecentActions.append("tabno")
                    $ JeanX.DailyActions.append("tabno")
                $ JeanX.RecentActions.append("no foot")
                $ JeanX.DailyActions.append("no foot")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ JeanX.FaceChange("sexy")
                    $ JeanX.Statup("Obed", 90, 2)
                    $ JeanX.Statup("Obed", 50, 2)
                    $ JeanX.Statup("Inbt", 70, 3)
                    $ JeanX.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Sure, I guess.",
                        "OK.",
                        "Fine, lemme see it.",
                        "I guess I could. . .",
                        "Ok. . . [She gestures for you to come over].",
                        "Heh, ok, ok."])
                    ch_j "[Line]"
                    $ Line = 0
                    jump Jean_FJ_Prep
                else:
                    pass

            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck(JeanX, 400, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and JeanX.Forced):
                    $ JeanX.FaceChange("sad")
                    $ JeanX.Statup("Love", 70, -5, 1)
                    $ JeanX.Statup("Love", 200, -2)
                    ch_j "Fine."
                    $ JeanX.Statup("Obed", 50, 4)
                    $ JeanX.Statup("Inbt", 80, 1)
                    $ JeanX.Statup("Inbt", 60, 3)
                    $ JeanX.Forced = 1
                    jump Jean_FJ_Prep
                else:
                    $ JeanX.Statup("Love", 200, -15)
                    $ JeanX.RecentActions.append("angry")
                    $ JeanX.DailyActions.append("angry")

    #She refused all offers.
    $ JeanX.ArmPose = 1
    if "no foot" in JeanX.DailyActions:
        $ JeanX.FaceChange("angry", 1)
        ch_j "I'm not telling you again."
        $ JeanX.RecentActions.append("angry")
        $ JeanX.DailyActions.append("angry")
    elif JeanX.Forced:
        $ JeanX.FaceChange("angry", 1)
        ch_j "Don't push it. . ."
        $ JeanX.Statup("Lust", 200, 5)
        if JeanX.Love > 300:
                $ JeanX.Statup("Love", 70, -2)
        $ JeanX.Statup("Obed", 50, -2)
        $ JeanX.RecentActions.append("angry")
        $ JeanX.DailyActions.append("angry")
    elif JeanX.Taboo:                             # she refuses and this is too public a place for her
        $ JeanX.FaceChange("angry", 1)
        $ JeanX.DailyActions.append("tabno")
        ch_j "This is too public."
        $ JeanX.Statup("Lust", 200, 5)
        $ JeanX.Statup("Obed", 50, -3)
    elif JeanX.Foot:
        $ JeanX.FaceChange("sad")
        ch_j "Not right now."
    else:
        $ JeanX.FaceChange("normal", 1)
        ch_j "I'd rather not."
    $ JeanX.RecentActions.append("no foot")
    $ JeanX.DailyActions.append("no foot")
    $ temp_modifier = 0
    return


label Jean_FJ_Prep:
    if Trigger2 == "foot":
        return

    if JeanX.Taboo:
        $ JeanX.Statup("Inbt", 90, int(Taboo/10))
        $ JeanX.Statup("Lust", 50, int(Taboo/5))

    $ JeanX.FaceChange("sexy")
    if JeanX.Forced:
        $ JeanX.FaceChange("sad")
    elif not JeanX.Foot:
        $ JeanX.Brows = "confused"
        $ JeanX.Eyes = "sexy"
        $ JeanX.Mouth = "smile"

    call Seen_First_Peen(JeanX,Partner)

    if not JeanX.Foot:
        if JeanX.Forced:
            $ JeanX.Statup("Love", 90, -20)
            $ JeanX.Statup("Obed", 70, 25)
            $ JeanX.Statup("Inbt", 80, 30)
        else:
            $ JeanX.Statup("Love", 90, 5)
            $ JeanX.Statup("Obed", 70, 20)
            $ JeanX.Statup("Inbt", 80, 20)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if JeanX.Taboo:
        $ JeanX.DrainWord("tabno")
    $ JeanX.DrainWord("no foot")
    $ JeanX.RecentActions.append("foot")
    $ JeanX.DailyActions.append("foot")

label Jean_FJ_Cycle:
    while Round > 0:
        call Shift_Focus(JeanX)
        call Jean_Sex_Launch("foot")
        $ JeanX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass

                        "Start moving? . ." if not Speed:
                                    $ Speed = 1

                        "Speed up. . ." if Speed < 2:
                                    $ Speed += 1
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
                                    "Offhand action":
                                            if JeanX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ JeanX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Shift primary action":
                                            if JeanX.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                    if JeanX.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Jean_FJ_After
                                                                        call Jean_Blowjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(JeanX,"tired")
                                                        "How about a handjob?":
                                                                    if JeanX.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Jean_FJ_After
                                                                        call Jean_Handjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(JeanX,"tired")

                                                        "How about a titjob?":
                                                                    if JeanX.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Jean_FJ_After
                                                                        call Jean_Titjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(JeanX,"tired")



                                                        "Never Mind":
                                                                jump Jean_FJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [JeanX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(JeanX)
                                            "Ask [JeanX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(JeanX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(JeanX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jean_FJ_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jean_FJ_Cycle
                                            "Never mind":
                                                        jump Jean_FJ_Cycle
                                    "undress [JeanX.Name]":
                                            call Girl_Undress(JeanX)
                                    "Clean up [JeanX.Name] (locked)" if not JeanX.Spunk:
                                            pass
                                    "Clean up [JeanX.Name]" if JeanX.Spunk:
                                            call Girl_Cleanup(JeanX,"ask")
                                    "Never mind":
                                            jump Jean_FJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Jean_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Jean_FJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Jean_Sex_Reset
                                    $ Line = 0
                                    jump Jean_FJ_After
        #End menu (if Line)

        call Shift_Focus(JeanX)
        call Sex_Dialog(JeanX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JeanX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JeanX)
                            if "angry" in JeanX.RecentActions:
                                call Jean_Sex_Reset
                                return
                            $ JeanX.Statup("Lust", 200, 5)
                            if 100 > JeanX.Lust >= 70 and JeanX.OCount < 2:
                                $ JeanX.RecentActions.append("unsatisfied")
                                $ JeanX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jean_FJ_After
                            $ Line = "came"

                    if JeanX.Lust >= 100:
                            #If Jean can cum
                            call Girl_Cumming(JeanX)
                            if Situation == "shift" or "angry" in JeanX.RecentActions:
                                jump Jean_FJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in JeanX.RecentActions:#And Jean is unsatisfied,
                                "[JeanX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Jean_FJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Cnt == 20:
                    $ JeanX.Brows = "angry"
                    menu:
                        ch_j "Hmm, my feet are cramping up here. . ."
                        "How about a BJ?" if JeanX.Action and MultiAction:
                                $ Situation = "shift"
                                call Jean_FJ_After
                                call Jean_Blowjob
                        "How about a Handy?" if JeanX.Action and MultiAction:
                                $ Situation = "shift"
                                call Jean_FJ_After
                                call Jean_Handjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump Jean_FJ_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Jean_Sex_Reset
                                $ Situation = "shift"
                                jump Jean_FJ_After
                        "No, get back down there.":
                                if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                                    $ JeanX.Statup("Love", 200, -5)
                                    $ JeanX.Statup("Obed", 50, 3)
                                    $ JeanX.Statup("Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    $ JeanX.FaceChange("angry", 1)
                                    "She scowls at you and pulls back."
                                    ch_j "Not interested."
                                    $ JeanX.Statup("Love", 50, -3, 1)
                                    $ JeanX.Statup("Love", 80, -4, 1)
                                    $ JeanX.Statup("Obed", 30, -1, 1)
                                    $ JeanX.Statup("Obed", 50, -1, 1)
                                    $ JeanX.RecentActions.append("angry")
                                    $ JeanX.DailyActions.append("angry")
                                    jump Jean_FJ_After
        elif Cnt == 10 and JeanX.SEXP <= 100 and not ApprovalCheck(JeanX, 1200, "LO"):
                    $ JeanX.Brows = "confused"
                    ch_j "Ok, seriously, let's try something different."
        #End Count check

        call Escalation(JeanX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(JeanX,10) #"You might want to wrap this up, it's getting late."
        elif Round == 5:
                call Sex_Basic_Dialog(JeanX,5)   #"Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ JeanX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(JeanX,"done")   #"Ok, [Girl.Petname], that's enough of that for now."

label Jean_FJ_After:
    $ JeanX.FaceChange("sexy")

    $ JeanX.Foot += 1
    $ JeanX.Action -=1
    $ JeanX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ JeanX.Addictionrate += 1
    $ JeanX.Statup("Lust", 90, 5)

    call Partner_Like(JeanX,1)

    if "Jeanpedi" in Achievements:
            pass
    elif JeanX.Foot >= 10:
            $ JeanX.FaceChange("smile", 1)
            ch_j "Hmm, this is kinda fun. . ."
            $ Achievements.append("Jeanpedi")
            $ JeanX.SEXP += 5
    elif JeanX.Foot == 1:
            $ JeanX.SEXP += 10
            if JeanX.Love >= 500:
                $ JeanX.Mouth = "smile"
                ch_j "Did you enjoy that? . ."
            elif Player.Focus <= 20:
                $ JeanX.Mouth = "sad"
                ch_j "Did that do it for you?"
    elif JeanX.Foot == 5:
                ch_j "I'm getting used to this. . ."

    $ temp_modifier = 0
    if Situation == "shift":
        ch_j "Ok, so what did you have in mind?"
    else:
        call Jean_Sex_Reset
    call Checkout
    return

## end JeanX.Footjob //////////////////////////////////////////////////////////////////////


label Psychic_Sex(Girl=0,Act=0):
    if Girl.Addict >= 50 and "ultimatum" in Girl.RecentActions:
            #skip this if she's addicted
            return
    elif "psysex" in Girl.History:
            #if you've done it before. . .
            ch_j "Well did you want another psychic handjob?"
    elif Girl.Taboo:
            ch_j "I'd rather not do that around here. . ."
            ch_j "Well what if I were to use my psychic powers instead?"
    else:
            ch_j "I don't know that I want to. . . touch you. . ."
            ch_j "Well what if I were to use my psychic powers instead?"
    menu PS_Menu:
            extend ""
            "Sure, that'd be great.":
                    $ Girl.Statup("Love", 80, 2)
                    $ Girl.Statup("Inbt", 70, 2)
                    ch_j "Fantastic. . ."
                    $ Situation = "psy"
                    jump Jean_PJ_Prep
            "What do you mean by that?" if "psysex" not in Girl.History and "ask" not in Player.RecentActions:
                    ch_j "Well, you know, I can \"touch\" things with my mind. . ."
                    $ Girl.Statup("Inbt", 70, 2)
                    ch_j "All sorts of things. . ."
                    ch_j "I could make you feel really good that way. . ."
                    $ Player.RecentActions.append("ask")
                    jump PS_Menu
            "No, I'd like you to be more \"hands on.\"":
                    $ Girl.Statup("Obed", 90, 2)
                    if Approval < 2:
                            $ Girl.FaceChange("sad")
                            $ Girl.Statup("Love", 80, -2)
                            ch_j "Well!"
                            ch_j ". . ."
                            $ Girl.FaceChange("normal")
                    #returns to previous menu.
                    return
    return

label Jean_PJ_Prep:
    if JeanX.Taboo:
        $ JeanX.Statup("Inbt", 90, int(Taboo/10))
        $ JeanX.Statup("Lust", 50, int(Taboo/5))

    $ JeanX.FaceChange("sexy")
    if JeanX.Forced:
        $ JeanX.FaceChange("sad")

    call Seen_First_Peen(JeanX,Partner,React=Situation)
    call Jean_PJ_Launch

    if Situation == JeanX:
            #Jean auto-starts
            $ Situation = 0
            if Trigger2 == "jackin":
                "An invisible pressure brushes your hand aside and starts stroking your cock."
            else:
                "[JeanX.Name] gives you a mischevious smile, and a gentle pressure starts to fondle your cock."
            menu:
                "What do you do?"
                "Nothing.":
                    $ JeanX.Statup("Inbt", 70, 3)
                    $ JeanX.Statup("Inbt", 30, 2)
                    "[JeanX.Name] continues her actions."
                "Praise her.":
                    $ JeanX.FaceChange("sexy", 1)
                    $ JeanX.Statup("Inbt", 70, 3)
                    ch_p "Oooh, that's good, [JeanX.Pet]."
                    $ JeanX.NameCheck() #checks reaction to petname
                    "[JeanX.Name] continues her actions."
                    $ JeanX.Statup("Love", 80, 1)
                    $ JeanX.Statup("Obed", 90, 1)
                    $ JeanX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ JeanX.FaceChange("surprised")
                    $ JeanX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [JeanX.Pet]."
                    $ JeanX.NameCheck() #checks reaction to petname
                    "[JeanX.Name] puts it down."
                    $ JeanX.Statup("Obed", 90, 1)
                    $ JeanX.Statup("Obed", 50, 1)
                    $ JeanX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ JeanX.AddWord(1,"refused","refused")
                    return

    if "psysex" not in JeanX.History:
        if JeanX.Forced:
            $ JeanX.Statup("Love", 90, -10)
            $ JeanX.Statup("Obed", 70, 15)
            $ JeanX.Statup("Inbt", 80, 20)
        else:
            $ JeanX.Statup("Love", 90, 5)
            $ JeanX.Statup("Obed", 70, 15)
            $ JeanX.Statup("Inbt", 80, 15)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ JeanX.RecentActions.append("psysex")
    $ JeanX.DailyActions.append("psysex")

label Jean_PJ_Cycle:
    $ Trigger = "psy"
    while Round > 0:
        call Shift_Focus(JeanX)
        call Jean_PJ_Launch
        $ JeanX.LustFace()

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
                        "View":
                                    call ViewShift(JeanX,"menu")
                                    jump Jean_PJ_Cycle
                        "Change Construct":
                                    menu:
                                        "What do you want to feel?"
                                        "Hand":
                                            if ApprovalCheck(JeanX, 1000):
                                                    $ Psychic = "hand"
                                            else:
                                                    ch_j "I'd rather not."
                                        "Mouth":
                                            if ApprovalCheck(JeanX, 1100):
                                                    $ Psychic = "mouth"
                                            else:
                                                    ch_j "Uh-uh."
                                        "Tits":
                                            if ApprovalCheck(JeanX, 1000):
                                                    $ Psychic = "tits"
                                            else:
                                                    ch_j "I'd rather not."
                                        "Pussy":
                                            if ApprovalCheck(JeanX, 1200):
                                                    $ Psychic = "pussy"
                                            else:
                                                    ch_j "Um. . . no."
                                        "Anal":
                                            if ApprovalCheck(JeanX, 1300):
                                                    $ Psychic = "anal"
                                            else:
                                                    ch_j "You wish."
                        "Other options":
                                menu:
                                    "I also want to fondle her breasts." if Trigger2 != "fondle breasts":
                                            if JeanX.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ JeanX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Shift primary action":
                                            if JeanX.Action and MultiAction:
                                                    menu:
#                                                        "How about a blowjob?":
#                                                                    if JeanX.Action and MultiAction:
#                                                                        $ Situation = "shift"
#                                                                        call Jean_PJ_After
#                                                                        call Jean_Blowjob
#                                                                    else:
#                                                                        call Sex_Basic_Dialog(JeanX,"tired")

#                                                        "How about a titjob?":
#                                                                    if JeanX.Action and MultiAction:
#                                                                        $ Situation = "shift"
#                                                                        call Jean_PJ_After
#                                                                        call Jean_Titjob
#                                                                    else:
#                                                                        call Sex_Basic_Dialog(JeanX,"tired")
                                                        "Never Mind":
                                                                jump Jean_PJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [JeanX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(JeanX)
                                            "Ask [JeanX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(JeanX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(JeanX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jean_PJ_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jean_PJ_Cycle
                                            "Never mind":
                                                        jump Jean_PJ_Cycle
                                    "undress [JeanX.Name]":
                                            call Girl_Undress(JeanX)
                                    "Clean up [JeanX.Name] (locked)" if not JeanX.Spunk:
                                            pass
                                    "Clean up [JeanX.Name]" if JeanX.Spunk:
                                            call Girl_Cleanup(JeanX,"ask")
                                    "Never mind":
                                            jump Jean_PJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Jean_PJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Jean_PJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Jean_PJ_Reset
                                    $ Line = 0
                                    jump Jean_PJ_After
        #End menu (if Line)

        call Shift_Focus(JeanX)
        call Sex_Dialog(JeanX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JeanX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JeanX)
                            if "angry" in JeanX.RecentActions:
                                call Jean_PJ_Reset
                                return
                            $ JeanX.Statup("Lust", 200, 5)
                            if 100 > JeanX.Lust >= 70 and JeanX.OCount < 2 and JeanX.SEXP >= 20:
                                $ JeanX.RecentActions.append("unsatisfied")
                                $ JeanX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jean_PJ_After
                            $ Line = "came"

                    if JeanX.Lust >= 100:
                            #If Jean can cum
                            call Girl_Cumming(JeanX)
                            if Situation == "shift" or "angry" in JeanX.RecentActions:
                                jump Jean_PJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in JeanX.RecentActions:#And Jean is unsatisfied,
                                "[JeanX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Jean_PJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Cnt == 20:
                    $ JeanX.Brows = "angry"
                    menu:
                        ch_j "Ok, I'm bored now. Can we try something else?"
#                        "How about a BJ?" if JeanX.Action and MultiAction:
#                                $ Situation = "shift"
#                                call Jean_PJ_After
#                                call Jean_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                jump Jean_PJ_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Jean_PJ_Reset
                                $ Situation = "shift"
                                jump Jean_PJ_After
                        "No, get back down there.":
                                if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                                    $ JeanX.Statup("Love", 200, -5)
                                    $ JeanX.Statup("Obed", 50, 3)
                                    $ JeanX.Statup("Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    $ JeanX.FaceChange("angry", 1)
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_j "I have better things to do with my time."
                                    $ JeanX.Statup("Love", 50, -3, 1)
                                    $ JeanX.Statup("Love", 80, -4, 1)
                                    $ JeanX.Statup("Obed", 30, -1, 1)
                                    $ JeanX.Statup("Obed", 50, -1, 1)
                                    $ JeanX.RecentActions.append("angry")
                                    $ JeanX.DailyActions.append("angry")
                                    jump Jean_PJ_After
        elif Cnt == 10 and JeanX.SEXP <= 100 and not ApprovalCheck(JeanX, 1200, "LO"):
                    $ JeanX.Brows = "confused"
                    ch_j "Nice, right?"
        #End Count check

        call Escalation(JeanX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(JeanX,10) #"You might want to wrap this up, it's getting late."
        elif Round == 5:
                call Sex_Basic_Dialog(JeanX,5)   #"Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ JeanX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(JeanX,"done")   #"Ok, [Girl.Petname], that's enough of that for now."

label Jean_PJ_After:
    $ JeanX.FaceChange("sexy")

    $ JeanX.Action -=1

    $ JeanX.Statup("Lust", 90, 5)

    call Partner_Like(JeanX,1)

    if "psysex" not in JeanX.History:
            ch_j "Pretty great, right?"
    $ JeanX.AddWord(1,0,0,0,"psysex")

    $ temp_modifier = 0
    if Situation == "shift":
        ch_j "Ok, so what did you have in mind?"
    call Jean_PJ_Reset
    call Checkout
    return

## end JeanX.Psychic Handjob //////////////////////////////////////////////////////////////////////
