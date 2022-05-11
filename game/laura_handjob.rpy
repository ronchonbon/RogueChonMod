## LauraX.Handjob //////////////////////////////////////////////////////////////////////
label Laura_Handjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(LauraX)
    if LauraX.Hand >= 7: # She loves it
        $ temp_modifier += 10
    elif LauraX.Hand >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif LauraX.Hand: #You've done it before
        $ temp_modifier += 3

    if LauraX.Addict >= 75 and LauraX.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 15
    if LauraX.Addict >= 75:
        $ temp_modifier += 5

    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in LauraX.Traits:
        $ temp_modifier += (3*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.Petnames:
        $ temp_modifier += 10
    elif "ex" in LauraX.Traits:
        $ temp_modifier -= 40
    if LauraX.ForcedCount and not LauraX.Forced:
        $ temp_modifier -= 5 * LauraX.ForcedCount

    if Taboo and "tabno" in LauraX.DailyActions:
        $ temp_modifier -= 10 

    if "no hand" in LauraX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no hand" in LauraX.RecentActions else 0

    $ Approval = ApprovalCheck(LauraX, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if not LauraX.Hand and "no hand" not in LauraX.RecentActions:
        $ LauraX.FaceChange("confused", 2)
        ch_l "Handjob, huh. . ."
        $ LauraX.Blush = 1

    if not LauraX.Hand and Approval:                                                 #First time dialog
        if LauraX.Forced:
            $ LauraX.FaceChange("sad",1)
            $ LauraX.Statup("Love", 70, -3, 1)
            $ LauraX.Statup("Love", 20, -2, 1)
        elif LauraX.Love >= (LauraX.Obed + LauraX.Inbt):
            $ LauraX.FaceChange("sexy",1)
            $ LauraX.Brows = "sad"
            $ LauraX.Mouth = "smile"
            ch_l "You'd like that. . ."
        elif LauraX.Obed >= LauraX.Inbt:
            $ LauraX.FaceChange("normal",1)
            ch_l "If you want, [LauraX.Petname]. . ."
        else: # Uninhibited
            $ LauraX.FaceChange("lipbite",1)
            ch_l "Hmm. . ."

    elif Approval:                                                                       #Second time+ dialog
        if LauraX.Forced:
            $ LauraX.FaceChange("sad")
            $ LauraX.Statup("Love", 70, -3, 1)
            $ LauraX.Statup("Love", 20, -2, 1)
            ch_l "Nothing more than that?"
        elif not Taboo and "tabno" in LauraX.DailyActions:
            ch_l "Well,this is a bit more secure. . ."
        elif "hand" in LauraX.RecentActions:
            $ LauraX.FaceChange("sexy", 1)
            ch_l "Hmm, another handy then. . ."
            jump Laura_HJ_Prep
        elif "hand" in LauraX.DailyActions:
            $ LauraX.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Another one?",
                "I'm glad I don't grow calluses.",
                "Didn't get enough earlier?",
                "Again the with handjobs, huh?",
                "I guess you want more."])
            ch_l "[Line]"
        elif LauraX.Hand < 3:
            $ LauraX.FaceChange("sexy", 1)
            $ LauraX.Brows = "confused"
            $ LauraX.Mouth = "kiss"
            ch_l "You seem to like this one. . ."
        else:
            $ LauraX.FaceChange("sexy", 1)
            $ LauraX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some more?",
                "So you'd like another handy?",
                "You want a. . . [fist pumping hand gestures]?",
                "Another handjob?"])
            ch_l "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if LauraX.Forced:
            $ LauraX.FaceChange("sad")
            $ LauraX.Statup("Obed", 90, 1)
            $ LauraX.Statup("Inbt", 60, 1)
            ch_l "Ok, fine."
        elif "no hand" in LauraX.DailyActions:
            ch_l "If it'll get you off my back. . ."
        else:
            $ LauraX.FaceChange("sexy", 1)
            $ LauraX.Statup("Love", 90, 1)
            $ LauraX.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Sure, I guess.",
                "O-kay.",
                "Fine.",
                "I suppose I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Ok, ok."])
            ch_l "[Line]"
            $ Line = 0
        $ LauraX.Statup("Obed", 20, 1)
        $ LauraX.Statup("Obed", 60, 1)
        $ LauraX.Statup("Inbt", 70, 2)
        jump Laura_HJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ LauraX.FaceChange("angry")
        if "no hand" in LauraX.RecentActions:
            ch_l "I just told you no, [LauraX.Petname]."
        elif Taboo and "tabno" in LauraX.DailyActions and "no hand" in LauraX.DailyActions:
            ch_l "I said not in public."
        elif "no hand" in LauraX.DailyActions:
            ch_l "I told you \"no,\" [LauraX.Petname]."
        elif Taboo and "tabno" in LauraX.DailyActions:
            ch_l "I said not in public."
        elif not LauraX.Hand:
            $ LauraX.FaceChange("bemused")
            ch_l "Seriously, [LauraX.Petname]. . ."
        else:
            $ LauraX.FaceChange("bemused")
            ch_l "Nah."
        menu:
            extend ""
            "Sorry, never mind." if "no hand" in LauraX.DailyActions:
                $ LauraX.FaceChange("bemused")
                ch_l "It's fine."
                return
            "Maybe later?" if "no hand" not in LauraX.DailyActions:
                $ LauraX.FaceChange("bemused")
                ch_l "Maybe."
                $ LauraX.Statup("Love", 80, 2)
                $ LauraX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ LauraX.RecentActions.append("tabno")
                    $ LauraX.DailyActions.append("tabno")
                $ LauraX.RecentActions.append("no hand")
                $ LauraX.DailyActions.append("no hand")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ LauraX.FaceChange("sexy")
                    $ LauraX.Statup("Obed", 90, 2)
                    $ LauraX.Statup("Obed", 50, 2)
                    $ LauraX.Statup("Inbt", 70, 3)
                    $ LauraX.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Sure, I guess.",
                        "O-kay.",
                        "Fine.",
                        "I suppose I could. . .",
                        "Ok. . . [She gestures for you to come over].",
                        "Ok, ok."])
                    ch_l "[Line]"
                    $ Line = 0
                    jump Laura_HJ_Prep
                else:
                    pass

            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck(LauraX, 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and LauraX.Forced):
                    $ LauraX.FaceChange("sad")
                    $ LauraX.Statup("Love", 70, -5, 1)
                    $ LauraX.Statup("Love", 200, -2)
                    ch_l "Ok, fine."
                    $ LauraX.Statup("Obed", 50, 4)
                    $ LauraX.Statup("Inbt", 80, 1)
                    $ LauraX.Statup("Inbt", 60, 3)
                    $ LauraX.Forced = 1
                    jump Laura_HJ_Prep
                else:
                    $ LauraX.Statup("Love", 200, -15)
                    $ LauraX.RecentActions.append("angry")
                    $ LauraX.DailyActions.append("angry")

    #She refused all offers.
    $ LauraX.ArmPose = 1
    if "no hand" in LauraX.DailyActions:
        $ LauraX.FaceChange("angry", 1)
        ch_l "Don't ask again."
        $ LauraX.RecentActions.append("angry")
        $ LauraX.DailyActions.append("angry")
    elif LauraX.Forced:
        $ LauraX.FaceChange("angry", 1)
        ch_l "No."
        $ LauraX.Statup("Lust", 200, 5)
        if LauraX.Love > 300:
                $ LauraX.Statup("Love", 70, -2)
        $ LauraX.Statup("Obed", 50, -2)
        $ LauraX.RecentActions.append("angry")
        $ LauraX.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ LauraX.FaceChange("angry", 1)
        $ LauraX.DailyActions.append("tabno")
        ch_l "This area's too exposed."
        $ LauraX.Statup("Lust", 200, 5)
        $ LauraX.Statup("Obed", 50, -3)
    elif LauraX.Hand:
        $ LauraX.FaceChange("sad")
        ch_l "I'm not into it today. . ."
    else:
        $ LauraX.FaceChange("normal", 1)
        ch_l "I don't know where that's been lately."
    $ LauraX.RecentActions.append("no hand")
    $ LauraX.DailyActions.append("no hand")
    $ temp_modifier = 0
    return


label Laura_HJ_Prep:
    if Trigger2 == "hand":
        return

    if Taboo:
        $ LauraX.Inbt += int(Taboo/10)
        $ LauraX.Lust += int(Taboo/5)

    $ LauraX.FaceChange("sexy")
    if LauraX.Forced:
        $ LauraX.FaceChange("sad")
    elif not LauraX.Hand:
        $ LauraX.Brows = "confused"
        $ LauraX.Eyes = "sexy"
        $ LauraX.Mouth = "smile"

    call Seen_First_Peen(LauraX,Partner,React=Situation)
    call Laura_HJ_Launch("L")

    if Situation == LauraX:
            #Laura auto-starts
            $ Situation = 0
            if Trigger2 == "jackin":
                "[LauraX.Name] brushes your hand aside and starts stroking your cock."
            else:
                "[LauraX.Name] gives you a mischevious smile, and starts to fondle your cock."
            menu:
                "What do you do?"
                "Nothing.":
                    $ LauraX.Statup("Inbt", 70, 3)
                    $ LauraX.Statup("Inbt", 30, 2)
                    "[LauraX.Name] continues her actions."
                "Praise her.":
                    $ LauraX.FaceChange("sexy", 1)
                    $ LauraX.Statup("Inbt", 70, 3)
                    ch_p "Oooh, that's good, [LauraX.Pet]."
                    $ LauraX.NameCheck() #checks reaction to petname
                    "[LauraX.Name] continues her actions."
                    $ LauraX.Statup("Love", 80, 1)
                    $ LauraX.Statup("Obed", 90, 1)
                    $ LauraX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ LauraX.FaceChange("surprised")
                    $ LauraX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [LauraX.Pet]."
                    $ LauraX.NameCheck() #checks reaction to petname
                    "[LauraX.Name] puts it down."
                    $ LauraX.Statup("Obed", 90, 1)
                    $ LauraX.Statup("Obed", 50, 1)
                    $ LauraX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ LauraX.AddWord(1,"refused","refused")
                    return

    if not LauraX.Hand:
        if LauraX.Forced:
            $ LauraX.Statup("Love", 90, -20)
            $ LauraX.Statup("Obed", 70, 25)
            $ LauraX.Statup("Inbt", 80, 30)
        else:
            $ LauraX.Statup("Love", 90, 5)
            $ LauraX.Statup("Obed", 70, 20)
            $ LauraX.Statup("Inbt", 80, 20)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ LauraX.DrainWord("tabno")
    $ LauraX.DrainWord("no hand")
    $ LauraX.RecentActions.append("hand")
    $ LauraX.DailyActions.append("hand")

label Laura_HJ_Cycle:
    while Round > 0:
        call Shift_Focus(LauraX)
        call Laura_HJ_Launch
        $ LauraX.LustFace()

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
                                            if LauraX.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ LauraX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")

                                    "Shift primary action":
                                            if LauraX.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                    if LauraX.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Laura_HJ_After
                                                                        call Laura_Blowjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(LauraX,"tired")

                                                        "How about a titjob?":
                                                                    if LauraX.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Laura_HJ_After
                                                                        call Laura_Titjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(LauraX,"tired")
                                                        "Never Mind":
                                                                jump Laura_HJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [LauraX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(LauraX)
                                            "Ask [LauraX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(LauraX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(LauraX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Laura_HJ_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Laura_HJ_Cycle
                                            "Never mind":
                                                        jump Laura_HJ_Cycle
                                    "undress [LauraX.Name]":
                                            call Girl_Undress(LauraX)
                                    "Clean up [LauraX.Name] (locked)" if not LauraX.Spunk:
                                            pass
                                    "Clean up [LauraX.Name]" if LauraX.Spunk:
                                            call Girl_Cleanup(LauraX,"ask")
                                    "Never mind":
                                            jump Laura_HJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Laura_HJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Laura_HJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Laura_HJ_Reset
                                    $ Line = 0
                                    jump Laura_HJ_After
        #End menu (if Line)

        call Shift_Focus(LauraX)
        call Sex_Dialog(LauraX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or LauraX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(LauraX)
                            if "angry" in LauraX.RecentActions:
                                call Laura_HJ_Reset
                                return
                            $ LauraX.Statup("Lust", 200, 5)
                            if 100 > LauraX.Lust >= 70 and LauraX.OCount < 2 and LauraX.SEXP >= 20:
                                $ LauraX.RecentActions.append("unsatisfied")
                                $ LauraX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Laura_HJ_After
                            $ Line = "came"

                    if LauraX.Lust >= 100:
                            #If Laura can cum
                            call Girl_Cumming(LauraX)
                            if Situation == "shift" or "angry" in LauraX.RecentActions:
                                jump Laura_HJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in LauraX.RecentActions:#And Laura is unsatisfied,
                                "[LauraX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Laura_HJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Cnt == 20:
                    $ LauraX.Brows = "angry"
                    menu:
                        ch_l "Hmm, this is boring, can we take a break?"
                        "How about a BJ?" if LauraX.Action and MultiAction:
                                $ Situation = "shift"
                                call Laura_HJ_After
                                call Laura_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                jump Laura_HJ_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Laura_HJ_Reset
                                $ Situation = "shift"
                                jump Laura_HJ_After
                        "No, get back down there.":
                                if ApprovalCheck(LauraX, 1200) or ApprovalCheck(LauraX, 500, "O"):
                                    $ LauraX.Statup("Love", 200, -5)
                                    $ LauraX.Statup("Obed", 50, 3)
                                    $ LauraX.Statup("Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    $ LauraX.FaceChange("angry", 1)
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_l "I have better things to do with my time."
                                    $ LauraX.Statup("Love", 50, -3, 1)
                                    $ LauraX.Statup("Love", 80, -4, 1)
                                    $ LauraX.Statup("Obed", 30, -1, 1)
                                    $ LauraX.Statup("Obed", 50, -1, 1)
                                    $ LauraX.RecentActions.append("angry")
                                    $ LauraX.DailyActions.append("angry")
                                    jump Laura_HJ_After
        elif Cnt == 10 and LauraX.SEXP <= 100 and not ApprovalCheck(LauraX, 1200, "LO"):
                    $ LauraX.Brows = "confused"
                    ch_l "This working for you?"
        #End Count check

        call Escalation(LauraX) #sees if she wants to escalate things

        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [LauraX.Petname]."

    #Round = 0 loop breaks
    $ LauraX.FaceChange("bemused", 0)
    $ Line = 0
    ch_l "Ok, [LauraX.Petname], breaktime."

label Laura_HJ_After:
    $ LauraX.FaceChange("sexy")

    $ LauraX.Hand += 1
    $ LauraX.Action -=1
    $ LauraX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ LauraX.Addictionrate += 1
    $ LauraX.Statup("Lust", 90, 5)

    call Partner_Like(LauraX,1)

    if "Laura Handi-Queen" in Achievements:
            pass
    elif LauraX.Hand >= 10:
            $ LauraX.FaceChange("smile", 1)
            ch_l "Looks like you filled out the punch card, [LauraX.Petname]."
            $ Achievements.append("Laura Handi-Queen")
            $LauraX.SEXP += 5
    elif LauraX.Hand == 1:
            $LauraX.SEXP += 10
            if LauraX.Love >= 500:
                $ LauraX.Mouth = "smile"
                ch_l "That was kind of. . . pleasant. . ."
            elif Player.Focus <= 20:
                $ LauraX.Mouth = "sad"
                ch_l "Did that do it for you?"
    elif LauraX.Hand == 5:
                ch_l "I think I've got this down, maybe I should get a punch card."

    $ temp_modifier = 0
    if Situation == "shift":
        ch_l "Ok, so what did you have in mind?"
    else:
        call Laura_HJ_Reset
    call Checkout
    return

## end LauraX.Handjob //////////////////////////////////////////////////////////////////////


## LauraX.Titjob //////////////////////////////////////////////////////////////////////              Not finished
label Laura_Titjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(LauraX)
    if LauraX.Tit >= 7: # She loves it
        $ temp_modifier += 10
    elif LauraX.Tit >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif LauraX.Tit: #You've done it before
        $ temp_modifier += 5

    if LauraX.Addict >= 75 and LauraX.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 15
    elif LauraX.Addict >= 75:
        $ temp_modifier += 5

    if LauraX.SeenChest and ApprovalCheck(LauraX, 500): # You've seen her tits.
        $ temp_modifier += 10
    if not LauraX.Chest and not LauraX.Over: #She's already topless
        $ temp_modifier += 10
    if LauraX.Lust > 75: #She's really horny
        $ temp_modifier += 10
    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in LauraX.Traits:
        $ temp_modifier += (5*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.Petnames:
        $ temp_modifier += 10
    elif "ex" in LauraX.Traits:
        $ temp_modifier -= 30
    if LauraX.ForcedCount and not LauraX.Forced:
        $ temp_modifier -= 5 * LauraX.ForcedCount

    if Taboo and "tabno" in LauraX.DailyActions:
        $ temp_modifier -= 10

    if "no titjob" in LauraX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no titjob" in LauraX.RecentActions else 0

    $ Approval = ApprovalCheck(LauraX, 1200, TabM = 4) # 120, 135, 150, Taboo -200(320)

    if not LauraX.Tit and "no titjob" not in LauraX.RecentActions:
        $ LauraX.FaceChange("surprised", 1)
        $ LauraX.Mouth = "kiss"
        ch_l "You want a titjob, huh?"

    if not LauraX.Tit and Approval:                                                 #First time dialog
        if LauraX.Forced:
            $ LauraX.FaceChange("sad")
            $ LauraX.Statup("Love", 70, -3, 1)
            $ LauraX.Statup("Love", 20, -2, 1)
        elif LauraX.Love >= (LauraX.Obed + LauraX.Inbt):
            $ LauraX.FaceChange("sexy")
            $ LauraX.Brows = "sad"
            $ LauraX.Mouth = "smile"
            ch_l "Well, maybe you deserve it."
        elif LauraX.Obed >= LauraX.Inbt:
            $ LauraX.FaceChange("normal")
            ch_l "If you'd like that. . ."
        elif LauraX.Addict >= 50:
            $ LauraX.FaceChange("manic", 1)
            ch_l "Hmmmm. . . ."
        else: # Uninhibited
            $ LauraX.FaceChange("sad")
            $ LauraX.Mouth = "smile"
            ch_l "Sounds fun. . ."
    elif Approval:                                                                       #Second time+ dialog
        if LauraX.Forced:
            $ LauraX.FaceChange("sad")
            $ LauraX.Statup("Love", 70, -3, 1)
            $ LauraX.Statup("Love", 20, -2, 1)
            ch_l "You're kinda pushing it."
        elif not Taboo and "tabno" in LauraX.DailyActions:
            ch_l "Ok, I guess this is secluded enough. . ."
        elif "titjob" in LauraX.RecentActions:
            $ LauraX.FaceChange("sexy", 1)
            ch_l "Huh, again?"
            jump Laura_TJ_Prep
        elif "titjob" in LauraX.DailyActions:
            $ LauraX.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Back for more?",
                "You're really working these puppies.",
                "Didn't get enough earlier?",
                "You're really working these puppies."])
            ch_l "[Line]"
        elif LauraX.Tit < 3:
            $ LauraX.FaceChange("sexy", 1)
            $ LauraX.Brows = "confused"
            $ LauraX.Mouth = "kiss"
            ch_l "Another titjob??"
        else:
            $ LauraX.FaceChange("sexy", 1)
            $ LauraX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action [rubs her chest]?",
                "So you'd like another titjob?",
                "So you'd like another titjob?",
                "So you'd like another titjob?",
                "Another titjob?",
                "A little [points at her chest]?"])
            ch_l "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if LauraX.Forced:
            $ LauraX.FaceChange("sad")
            $ LauraX.Statup("Obed", 90, 1)
            $ LauraX.Statup("Inbt", 60, 1)
            ch_l "Well, could be worse. . ."
        elif "no titjob" in LauraX.DailyActions:
            ch_l "Hmm, I guess. . ."
        else:
            $ LauraX.FaceChange("sexy", 1)
            $ LauraX.Statup("Love", 90, 1)
            $ LauraX.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, put it here.",
                "Well. . . ok.",
                "Yum.",
                "Sure, whip it out.",
                "Fine. . . [She drools a bit into her cleavage].",
                "Heh, ok."])
            ch_l "[Line]"
            $ Line = 0
        $ LauraX.Statup("Obed", 20, 1)
        $ LauraX.Statup("Obed", 70, 1)
        $ LauraX.Statup("Inbt", 80, 2)
        jump Laura_TJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ LauraX.FaceChange("angry")
        if "no titjob" in LauraX.RecentActions:
            ch_l "I {i}just{/i} told you \"no,\" [LauraX.Petname]."
        elif Taboo and "tabno" in LauraX.DailyActions and "no titjob" in LauraX.DailyActions:
            ch_l "This is just way too exposed!"
        elif "no titjob" in LauraX.DailyActions:
            ch_l "I already told you \"no,\" [LauraX.Petname]."
        elif Taboo and "tabno" in LauraX.DailyActions:
            ch_l "This is just way too exposed!"
        elif not LauraX.Tit:
            $ LauraX.FaceChange("bemused")
            ch_l "I'm not really into that, [LauraX.Petname]. . ."
        else:
            $ LauraX.FaceChange("bemused")
            ch_l "Not right now [LauraX.Petname]. . ."

        menu:
            extend ""
            "Sorry, never mind." if "no titjob" in LauraX.DailyActions:
                $ LauraX.FaceChange("bemused")
                ch_l "Yeah, ok, [LauraX.Petname]."
                return
            "Maybe later?" if "no titjob" not in LauraX.DailyActions:
                $ LauraX.FaceChange("sexy")
                ch_l "Maybe."
                $ LauraX.Statup("Love", 80, 2)
                $ LauraX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ LauraX.RecentActions.append("tabno")
                    $ LauraX.DailyActions.append("tabno")
                $ LauraX.RecentActions.append("no titjob")
                $ LauraX.DailyActions.append("no titjob")
                return
            "I think this could be fun for both of us. . .":
                if Approval:
                    $ LauraX.FaceChange("sexy")
                    $ LauraX.Statup("Obed", 80, 2)
                    $ LauraX.Statup("Obed", 40, 2)
                    $ LauraX.Statup("Inbt", 70, 3)
                    $ LauraX.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Well, ok, put it here.",
                        "Well. . . ok.",
                        "I guess.",
                        "I guess, whip it out.",
                        "Fine. . . [She drools a bit into her cleavage].",
                        "Heh, ok."])
                    ch_l "[Line]"
                    $ Line = 0
                    jump Laura_TJ_Prep
                else:
                    $ Approval = ApprovalCheck(LauraX, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)             Handy instead?
                    if Approval >= 2 and LauraX.Blow:
                        $ LauraX.Statup("Inbt", 80, 1)
                        $ LauraX.Statup("Inbt", 60, 3)
                        $ LauraX.FaceChange("confused", 1)
                        ch_l "I could maybe blow you?"
                        menu:
                            ch_l "How about that [[blowjob]?"
                            "Ok, get down there.":
                                $ LauraX.Statup("Love", 80, 2)
                                $ LauraX.Statup("Inbt", 60, 1)
                                $ LauraX.Statup("Obed", 50, 1)
                                jump Laura_BJ_Prep
                            "Nah, it's all about dem titties.":
                                $ Line = "no BJ"
                    if Approval and LauraX.Hand:
                        $ LauraX.Statup("Inbt", 80, 1)
                        $ LauraX.Statup("Inbt", 60, 3)
                        $ LauraX.FaceChange("confused", 1)
                        ch_l "I could give you a handy?"
                        menu:
                            ch_l "What do you say?"
                            "Sure, that's fine.":
                                $ LauraX.Statup("Love", 80, 2)
                                $ LauraX.Statup("Inbt", 60, 1)
                                $ LauraX.Statup("Obed", 50, 1)
                                jump Laura_HJ_Prep
                            "Seriously, titties." if Line == "no BJ":
                                $ Line = 0
                            "Nah, it's all about dem titties." if Line != "no BJ":
                                pass
                    $ LauraX.Statup("Love", 200, -2)
                    ch_l "Nah."
                    $ LauraX.Statup("Obed", 70, 2)


            "Come on, let me fuck those titties, [LauraX.Pet]":                                               # Pressured into it
                $ LauraX.NameCheck() #checks reaction to petname
                $ Approval = ApprovalCheck(LauraX, 700, "OI", TabM = 4) # 70, 85, 100, -160(230)
                if Approval > 1 or (Approval and LauraX.Forced):
                    $ LauraX.FaceChange("sad")
                    $ LauraX.Statup("Love", 70, -5, 1)
                    $ LauraX.Statup("Love", 200, -2)
                    ch_l "Ok, fine, whip it out."
                    $ LauraX.Statup("Obed", 50, 4)
                    $ LauraX.Statup("Inbt", 80, 1)
                    $ LauraX.Statup("Inbt", 60, 3)
                    $ LauraX.Forced = 1
                    jump Laura_TJ_Prep
                else:
                    $ LauraX.Statup("Love", 200, -15)
                    $ LauraX.RecentActions.append("angry")
                    $ LauraX.DailyActions.append("angry")

    #She refused all offers.
    if "no titjob" in LauraX.DailyActions:
        $ LauraX.FaceChange("angry", 1)
        ch_l "Look, I already told you no."
        $ LauraX.RecentActions.append("angry")
        $ LauraX.DailyActions.append("angry")
    elif LauraX.Forced:
        $ LauraX.FaceChange("angry", 1)
        ch_l "No, try something else."
        $ LauraX.Statup("Lust", 200, 5)
        if LauraX.Love > 300:
                $ LauraX.Statup("Love", 70, -2)
        $ LauraX.Statup("Obed", 50, -2)
        $ LauraX.RecentActions.append("angry")
        $ LauraX.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ LauraX.FaceChange("angry", 1)
        $ LauraX.DailyActions.append("tabno")
        ch_l "You really expect me to do that here? This isn't exactly \"covert.\""
        $ LauraX.Statup("Lust", 200, 5)
        $ LauraX.Statup("Obed", 50, -3)
    elif LauraX.Tit:
        $ LauraX.FaceChange("sad")
        ch_l "You'll know when it's time for that."
    else:
        $ LauraX.FaceChange("normal", 1)
        ch_l "Nah."
    $ LauraX.RecentActions.append("no titjob")
    $ LauraX.DailyActions.append("no titjob")
    $ temp_modifier = 0
    return

label Laura_TJ_Prep:

    if Taboo:
        $ LauraX.Inbt += int(Taboo/10)
        $ LauraX.Lust += int(Taboo/5)


    $ LauraX.FaceChange("sexy")
    if LauraX.Forced:
        $ LauraX.FaceChange("sad")
    elif not LauraX.Tit:
        $ LauraX.Brows = "confused"
        $ LauraX.Eyes = "sexy"
        $ LauraX.Mouth = "smile"

    call Seen_First_Peen(LauraX,Partner,React=Situation)
    call Laura_TJ_Launch("L")

    if Situation == LauraX:
            #Laura auto-starts
            $ Situation = 0
            "[LauraX.Name] slides down and sandwiches your dick between her tits."
            menu:
                "What do you do?"
                "Nothing.":
                    $ LauraX.Statup("Inbt", 80, 3)
                    $ LauraX.Statup("Inbt", 40, 2)
                    "[LauraX.Name] starts to slide them up and down."
                "Praise her.":
                    $ LauraX.FaceChange("sexy", 1)
                    $ LauraX.Statup("Inbt", 80, 3)
                    ch_p "Oh, that sounds like a good idea, [LauraX.Pet]."
                    $ LauraX.NameCheck() #checks reaction to petname
                    "[LauraX.Name] continues her actions."
                    $ LauraX.Statup("Love", 85, 1)
                    $ LauraX.Statup("Obed", 90, 1)
                    $ LauraX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ LauraX.FaceChange("confused")
                    $ LauraX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [LauraX.Pet]."
                    $ LauraX.NameCheck() #checks reaction to petname
                    "[LauraX.Name] lets it drop out from between her breasts."
                    $ LauraX.Statup("Obed", 90, 1)
                    $ LauraX.Statup("Obed", 50, 3)
                    $ Player.RecentActions.append("nope")
                    $ LauraX.AddWord(1,"refused","refused")
                    return

    if not LauraX.Tit:
        if LauraX.Forced:
            $ LauraX.Statup("Love", 90, -25)
            $ LauraX.Statup("Obed", 70, 30)
            $ LauraX.Statup("Inbt", 80, 35)
        else:
            $ LauraX.Statup("Love", 90, 5)
            $ LauraX.Statup("Obed", 70, 25)
            $ LauraX.Statup("Inbt", 80, 30)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ LauraX.DrainWord("tabno")
    $ LauraX.DrainWord("no titjob")
    $ LauraX.RecentActions.append("titjob")
    $ LauraX.DailyActions.append("titjob")

label Laura_TJ_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(LauraX)
        call Laura_TJ_Launch
        $ LauraX.LustFace()

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
                                            if LauraX.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ LauraX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")

                                    "Shift primary action":
                                            if LauraX.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                if LauraX.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Laura_TJ_After
                                                                    call Laura_Blowjob
                                                                else:
                                                                    call Sex_Basic_Dialog(LauraX,"tired")

                                                        "How about a handy?":
                                                                if LauraX.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Laura_BJ_After
                                                                    call Laura_Handjob
                                                                else:
                                                                    call Sex_Basic_Dialog(LauraX,"tired")
                                                        "Never Mind":
                                                                jump Laura_TJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [LauraX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(LauraX)
                                            "Ask [LauraX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(LauraX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(LauraX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Laura_TJ_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Laura_TJ_Cycle
                                            "Never mind":
                                                        jump Laura_TJ_Cycle
                                    "undress [LauraX.Name]":
                                            call Girl_Undress(LauraX)
                                    "Clean up [LauraX.Name] (locked)" if not LauraX.Spunk:
                                            pass
                                    "Clean up [LauraX.Name]" if LauraX.Spunk:
                                            call Girl_Cleanup(LauraX,"ask")
                                    "Never mind":
                                            jump Laura_TJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Laura_TJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Laura_TJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Laura_TJ_Reset
                                    $ Line = 0
                                    jump Laura_TJ_After
        #End menu (if Line)

        call Shift_Focus(LauraX)
        call Sex_Dialog(LauraX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or LauraX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(LauraX)
                            if "angry" in LauraX.RecentActions:
                                call Laura_TJ_Reset
                                return
                            $ LauraX.Statup("Lust", 200, 5)
                            if 100 > LauraX.Lust >= 70 and LauraX.OCount < 2 and LauraX.SEXP >= 20:
                                $ LauraX.RecentActions.append("unsatisfied")
                                $ LauraX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Laura_TJ_After
                            $ Line = "came"

                    if LauraX.Lust >= 100:
                            #If Laura can cum
                            call Girl_Cumming(LauraX)
                            if Situation == "shift" or "angry" in LauraX.RecentActions:
                                jump Laura_TJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in LauraX.RecentActions:#And Laura is unsatisfied,
                                "[LauraX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Laura_TJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        if Speed >= 4:
                call Speed_Shift(0) #resets speed after orgasm
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if LauraX.SEXP >= 100 or ApprovalCheck(LauraX, 1200, "LO"):
                pass
        elif Cnt == (5 + LauraX.Tit):
                $ LauraX.Brows = "confused"
                ch_l "Are you getting close here? I'm getting bored."
        if Cnt == (10 + LauraX.Tit):
                $ LauraX.Brows = "angry"
                menu:
                    ch_l "Seriously, can we do something else?"
                    "How about a BJ?" if LauraX.Action and MultiAction:
                        $ Situation = "shift"
                        call Laura_TJ_After
                        call Laura_Blowjob
                        return
                    "Finish up." if Player.FocusX:
                        "You release your concentration. . ."
                        $ Player.FocusX = 0
                        $ Player.Focus += 15
                        jump Laura_TJ_Cycle
                    "Let's try something else." if MultiAction:
                        $ Line = 0
                        call Laura_TJ_Reset
                        $ Situation = "shift"
                        jump Laura_TJ_After
                    "No, get back down there.":
                        if ApprovalCheck(LauraX, 1200) or ApprovalCheck(LauraX, 500, "O"):
                            $ LauraX.Statup("Love", 200, -5)
                            $ LauraX.Statup("Obed", 50, 3)
                            $ LauraX.Statup("Obed", 80, 2)
                            "She grumbles but gets back to work."
                        else:
                            $ LauraX.FaceChange("angry", 1)
                            "She scowls at you, drops you cock and pulls back."
                            ch_l "Well fuck you then."
                            $ LauraX.Statup("Love", 50, -3, 1)
                            $ LauraX.Statup("Love", 80, -4, 1)
                            $ LauraX.Statup("Obed", 30, -1, 1)
                            $ LauraX.Statup("Obed", 50, -1, 1)
                            $ LauraX.RecentActions.append("angry")
                            $ LauraX.DailyActions.append("angry")
                            jump Laura_TJ_After
            #End Count check

        call Escalation(LauraX) #sees if she wants to escalate things

        if Round == 10:
            ch_l "It's kinda time to get moving."
        elif Round == 5:
            ch_l "Tic tock, [LauraX.Petname]."

    #Round = 0 loop breaks
    $ LauraX.FaceChange("bemused", 0)
    $ Line = 0
    ch_l "Ok, [LauraX.Petname], breaktime."

label Laura_TJ_After:
    $ LauraX.FaceChange("sexy")

    $ LauraX.Tit += 1
    $ LauraX.Action -=1
    $ LauraX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ LauraX.Addictionrate += 1

    call Partner_Like(LauraX,4)

    if LauraX.Tit > 5:
        pass
    elif LauraX.Tit == 1:
        $ LauraX.SEXP += 12
        if LauraX.Love >= 500:
            $ LauraX.Mouth = "smile"
            ch_l "That was fun."
        elif Player.Focus <= 20:
            $ LauraX.Mouth = "sad"
            ch_l "Well I hope you got something out of that."
    elif LauraX.Tit == 5:
            ch_l "You seem to enjoy that."

    $ temp_modifier = 0

    if Situation == "shift":
            ch_l "Mmm, so what else did you have in mind?"
    else:
            call Laura_TJ_Reset
    call Checkout
    return

## end LauraX.Titjob //////////////////////////////////////////////////////////////////////



# LauraX.Blowjob //////////////////////////////////////////////////////////////////////

label Laura_Blowjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(LauraX)
    if LauraX.Blow >= 7: # She loves it
        $ temp_modifier += 15
    elif LauraX.Blow >= 3: #You've done it before several times
        $ temp_modifier += 10
    elif LauraX.Blow: #You've done it before
        $ temp_modifier += 7

    if LauraX.Addict >= 75 and LauraX.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 25
    elif LauraX.Addict >= 75: #She's really strung out
        $ temp_modifier += 15

    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in LauraX.Traits:
        $ temp_modifier += (4*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.Petnames:
        $ temp_modifier += 10
    elif "ex" in LauraX.Traits:
        $ temp_modifier -= 40
    if LauraX.ForcedCount and not LauraX.Forced:
        $ temp_modifier -= 5 * LauraX.ForcedCount

    if Taboo and "tabno" in LauraX.DailyActions:
        $ temp_modifier -= 10

    if "no blow" in LauraX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no blow" in LauraX.RecentActions else 0

    $ Approval = ApprovalCheck(LauraX, 1300, TabM = 4) # 130, 145, 160, Taboo -160(290)

    if not LauraX.Blow and "no blow" not in LauraX.RecentActions:
        $ LauraX.FaceChange("surprised", 2)
        $ LauraX.Mouth = "kiss"
        ch_l "You want me to suck your cock?"
        if LauraX.Hand:
            $ LauraX.Mouth = "smile"
            ch_l "Handjobs not enough now?"
        $ LauraX.Blush = 1

    if not LauraX.Blow and Approval:                                                 #First time dialog
        if LauraX.Forced:
            $ LauraX.FaceChange("sad")
            $ LauraX.Statup("Love", 70, -3, 1)
            $ LauraX.Statup("Love", 20, -2, 1)
        elif LauraX.Love >= (LauraX.Obed + LauraX.Inbt):
            $ LauraX.FaceChange("sexy")
            $ LauraX.Brows = "sad"
            $ LauraX.Mouth = "smile"
            ch_l "I have wondered how you taste."
        elif LauraX.Obed >= LauraX.Inbt:
            $ LauraX.FaceChange("normal")
            ch_l "If that's what you want. . ."
        elif LauraX.Addict >= 50:
            $ LauraX.FaceChange("manic", 1)
            ch_l "[[wipes away a little drool]"
        else: # Uninhibited
            $ LauraX.FaceChange("sad")
            $ LauraX.Mouth = "smile"
            ch_l "Huh. . ."
    elif Approval:                                                                       #Second time+ dialog
        if LauraX.Forced:
            $ LauraX.FaceChange("sad")
            $ LauraX.Statup("Love", 70, -3, 1)
            $ LauraX.Statup("Love", 20, -2, 1)
            ch_l "Again?"
        elif not Taboo and "tabno" in LauraX.DailyActions:
            ch_l "Hmm, this is private enough. . ."
        elif "blow" in LauraX.RecentActions:
            $ LauraX.FaceChange("sexy", 1)
            ch_l "Mmm, again? [[yawns]"
            jump Laura_BJ_Prep
        elif "blow" in LauraX.DailyActions:
            $ LauraX.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",
                "Wear'in me out here.",
                "I must be too good at this.",
                "Let me get some saliva going.",
                "Didn't get enough earlier?"])
            ch_l "[Line]"
        elif LauraX.Blow < 3:
            $ LauraX.FaceChange("sexy", 1)
            $ LauraX.Brows = "confused"
            $ LauraX.Mouth = "kiss"
            ch_l "You'd like another blowjob?"
        else:
            $ LauraX.FaceChange("sexy", 1)
            $ LauraX.ArmPose = 2
            $ Line = renpy.random.choice(["You want me to [mimes blowing]?",
                "So you want another blowjob?",
                "You want me to lick you?",
                "You want me to suck you off?",
                "A little bj?"])
            ch_l "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if LauraX.Forced:
            $ LauraX.FaceChange("sad")
            $ LauraX.Statup("Obed", 90, 1)
            $ LauraX.Statup("Inbt", 60, 1)
            ch_l "Whatever."
        elif "no blow" in LauraX.DailyActions:
            ch_l "Fine. . ."
        else:
            $ LauraX.FaceChange("sexy", 1)
            $ LauraX.Statup("Love", 90, 1)
            $ LauraX.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Sure. Ahhhhhh.",
                "Well. . . alright.",
                "Yum.",
                "Sure, whip it out.",
                "Ok. . . [She licks her lips].",
                "Alright, let's see it."])
            ch_l "[Line]"
            $ Line = 0
        $ LauraX.Statup("Obed", 20, 1)
        $ LauraX.Statup("Obed", 70, 1)
        $ LauraX.Statup("Inbt", 80, 2)
        jump Laura_BJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ LauraX.FaceChange("angry")
        if "no blow" in LauraX.RecentActions:
            ch_l "Just told you I wouldn't, [LauraX.Petname]."
        elif Taboo and "tabno" in LauraX.DailyActions and "no blow" in LauraX.DailyActions:
            ch_l "Like I told you, not in public."
        elif "no blow" in LauraX.DailyActions:
            ch_l "Told you \"no,\" [LauraX.Petname]."
        elif Taboo and "tabno" in LauraX.DailyActions:
            ch_l "Like I told you, too public!"
        elif not LauraX.Blow:
            $ LauraX.FaceChange("bemused")
            ch_l "I don't know if your taste will match your scent, [LauraX.Petname]. . ."
        else:
            $ LauraX.FaceChange("bemused")
            ch_l "I don't know, [LauraX.Petname]!"
        menu:
            extend ""
            "Sorry, never mind." if "no blow" in LauraX.DailyActions:
                $ LauraX.FaceChange("bemused")
                ch_l "Cool."
                return
            "Maybe later?" if "no blow" not in LauraX.DailyActions:
                $ LauraX.FaceChange("sexy")
                ch_l "Yeah, maybe, [LauraX.Petname]."
                $ LauraX.Statup("Love", 80, 2)
                $ LauraX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ LauraX.RecentActions.append("tabno")
                    $ LauraX.DailyActions.append("tabno")
                $ LauraX.RecentActions.append("no blow")
                $ LauraX.DailyActions.append("no blow")
                return
            "Come on, please?":
                if Approval:
                    $ LauraX.FaceChange("sexy")
                    $ LauraX.Statup("Obed", 90, 2)
                    $ LauraX.Statup("Obed", 50, 2)
                    $ LauraX.Statup("Inbt", 70, 3)
                    $ LauraX.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Sure. Ahhhhhh.",
                        "Well. . . alright.",
                        "Yum.",
                        "Sure, whip it out.",
                        "Ok. . . [She licks her lips].",
                        "Alright, let's see it."])
                    ch_l "[Line]"
                    $ Line = 0
                    jump Laura_BJ_Prep
                else:
                    if ApprovalCheck(LauraX, 1100, TabM = 3): # 110, 125, 140, Taboo -120(230)             Handy instead?
                        $ LauraX.Statup("Inbt", 80, 1)
                        $ LauraX.Statup("Inbt", 60, 3)
                        $ LauraX.FaceChange("confused", 1)
                        $ LauraX.ArmPose = 2
                        if LauraX.Hand:
                            ch_l "Couldn't I just use my hand again?"
                            ch_l "You seemed to like that."
                        else:
                            ch_l "I could maybe use my hand instead, how's that sound?"
                        menu:
                            extend ""
                            "Sure, that's fine.":
                                $ LauraX.Statup("Love", 80, 2)
                                $ LauraX.Statup("Inbt", 60, 1)
                                $ LauraX.Statup("Obed", 50, 1)
                                jump Laura_HJ_Prep
                            "Nah, if it's not a BJ, forget it.":
                                $ LauraX.Statup("Love", 200, -2)
                                $ LauraX.ArmPose = 1
                                ch_l "Fine, be that way."
                                $ LauraX.Statup("Obed", 70, 2)


            "Suck it, [LauraX.Pet]":                                               # Pressured into it
                $ LauraX.NameCheck() #checks reaction to petname
                $ Approval = ApprovalCheck(LauraX, 750, "OI", TabM = 3) # 75, 90, 105, -120(195)
                if Approval > 1 or (Approval and LauraX.Forced):
                    $ LauraX.FaceChange("sad")
                    $ LauraX.Statup("Love", 70, -5, 1)
                    $ LauraX.Statup("Love", 200, -2)
                    ch_l "Whatever. . ."
                    $ LauraX.Statup("Obed", 50, 4)
                    $ LauraX.Statup("Inbt", 80, 1)
                    $ LauraX.Statup("Inbt", 60, 3)
                    $ LauraX.Forced = 1
                    jump Laura_BJ_Prep
                else:
                    $ LauraX.Statup("Love", 200, -15)
                    $ LauraX.RecentActions.append("angry")
                    $ LauraX.DailyActions.append("angry")

    #She refused all offers.
    if "no blow" in LauraX.DailyActions:
        $ LauraX.FaceChange("angry", 1)
        $ LauraX.ArmPose = 2
        $ LauraX.Claws = 1
        ch_l "Suck this then."
        $ LauraX.ArmPose = 1
        $ LauraX.Claws = 0
        $ LauraX.RecentActions.append("angry")
        $ LauraX.DailyActions.append("angry")
    elif LauraX.Forced:
        $ LauraX.FaceChange("angry", 1)
        ch_l "That's just pushing it."
        $ LauraX.Statup("Lust", 200, 5)
        if LauraX.Love > 300:
                $ LauraX.Statup("Love", 70, -2)
        $ LauraX.Statup("Obed", 50, -2)
        $ LauraX.RecentActions.append("angry")
        $ LauraX.DailyActions.append("angry")
        $ LauraX.RecentActions.append("no blow")
        $ LauraX.DailyActions.append("no blow")
        return
    elif Taboo:                             # she refuses and this is too public a place for her
        $ LauraX.FaceChange("angry", 1)
        $ LauraX.DailyActions.append("tabno")
        ch_l "This area's too exposed."
        $ LauraX.Statup("Lust", 200, 5)
        $ LauraX.Statup("Obed", 50, -3)
        return
    elif LauraX.Blow:
        $ LauraX.FaceChange("sad")
        ch_l "Nah, not this time."
    else:
        $ LauraX.FaceChange("normal", 1)
        ch_l "Nope."
    $ LauraX.RecentActions.append("no blow")
    $ LauraX.DailyActions.append("no blow")
    $ temp_modifier = 0
    return


label Laura_BJ_Prep:
    if renpy.showing("Laura_HJ_Animation"):
        hide Laura_HJ_Animation with easeoutbottom
    if Taboo:
        $ LauraX.Inbt += int(Taboo/10)
        $ LauraX.Lust += int(Taboo/5)

    $ LauraX.FaceChange("sexy")
    if LauraX.Forced:
        $ LauraX.FaceChange("sad")
    elif not LauraX.Blow:
        $ LauraX.Brows = "confused"
        $ LauraX.Eyes = "sexy"
        $ LauraX.Mouth = "smile"

    call Seen_First_Peen(LauraX,Partner,React=Situation)
    call Laura_BJ_Launch("L")
    if Situation == LauraX:
            #Laura auto-starts
            $ Situation = 0
            "[LauraX.Name] slides down and gives your cock a little lick."
            menu:
                "What do you do?"
                "Nothing.":
                    $ LauraX.Statup("Inbt", 80, 3)
                    $ LauraX.Statup("Inbt", 40, 2)
                    "[LauraX.Name] continues licking at it."
                "Praise her.":
                    $ LauraX.FaceChange("sexy", 1)
                    $ LauraX.Statup("Inbt", 80, 3)
                    ch_p "Hmmm, keep doing that, [LauraX.Pet]."
                    $ LauraX.NameCheck() #checks reaction to petname
                    "[LauraX.Name] continues her actions."
                    $ LauraX.Statup("Love", 85, 1)
                    $ LauraX.Statup("Obed", 90, 1)
                    $ LauraX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ LauraX.FaceChange("surprised")
                    $ LauraX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [LauraX.Pet]."
                    $ LauraX.NameCheck() #checks reaction to petname
                    "[LauraX.Name] puts it down."
                    $ LauraX.Statup("Obed", 90, 1)
                    $ LauraX.Statup("Obed", 50, 3)
                    $ Player.RecentActions.append("nope")
                    $ LauraX.AddWord(1,"refused","refused")
                    return
    if not LauraX.Blow:
        if LauraX.Forced:
            $ LauraX.Statup("Love", 90, -70)
            $ LauraX.Statup("Obed", 70, 45)
            $ LauraX.Statup("Inbt", 80, 60)
        else:
            $ LauraX.Statup("Love", 90, 5)
            $ LauraX.Statup("Obed", 70, 35)
            $ LauraX.Statup("Inbt", 80, 40)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ LauraX.DrainWord("tabno")
    $ LauraX.DrainWord("no blow")
    $ LauraX.RecentActions.append("blow")
    $ LauraX.DailyActions.append("blow")

label Laura_BJ_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(LauraX)
        call Laura_BJ_Launch
        $ LauraX.LustFace()

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

                                if "Gwentro" not in LauraX.History: #calls the special Gwentro event
                                            call Gwentro

                        "Suck on it. (locked)" if Speed == 3:
                                pass

                        "Take it deeper." if Speed != 4:
                                    if Trigger2 == "jackin" and Speed != 3:
                                        "She takes it to the root, and you move your hand out of the way."
                                    call Speed_Shift(4)
                        "Take it deeper. (locked)" if Speed == 4:
                                pass

                        "Set your own pace. . .":
                                "[LauraX.Name] hums contentedly."
                                if "setpace" not in LauraX.RecentActions:
                                    $ LauraX.Statup("Love", 80, 2)
                                $ D20 = renpy.random.randint(1, 20)
                                if LauraX.Blow < 5:
                                    $ D20 -= 10
                                elif LauraX.Blow < 10:
                                    $ D20 -= 5

                                if D20 > 15:
                                    call Speed_Shift(4)
                                    if "setpace" not in LauraX.RecentActions:
                                        $ LauraX.Statup("Inbt", 80, 3)
                                elif D20 > 10:
                                    call Speed_Shift(3)
                                elif D20 > 5:
                                    call Speed_Shift(2)
                                else:
                                    call Speed_Shift(1)
                                $ LauraX.RecentActions.append("setpace")

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
                                            if LauraX.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ LauraX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")

                                    "Shift primary action":
                                            if LauraX.Action and MultiAction:
                                                    menu:
                                                        "How about a handy?":
                                                                if LauraX.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Laura_BJ_After
                                                                    call Laura_Handjob
                                                                else:
                                                                    ch_l "I need a break, can we wrap on this?"
                                                        "How about a titjob?":
                                                                if LauraX.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Laura_BJ_After
                                                                    call Laura_Titjob
                                                                else:
                                                                    ch_l "I need a break, can we wrap on this?"
                                                        "Never Mind":
                                                                jump Laura_BJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [LauraX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(LauraX)
                                            "Ask [LauraX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(LauraX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(LauraX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Laura_BJ_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Laura_BJ_Cycle
                                            "Never mind":
                                                        jump Laura_BJ_Cycle
                                    "undress [LauraX.Name]":
                                            call Girl_Undress(LauraX)
                                    "Clean up [LauraX.Name] (locked)" if not LauraX.Spunk:
                                            pass
                                    "Clean up [LauraX.Name]" if LauraX.Spunk:
                                            call Girl_Cleanup(LauraX,"ask")
                                    "Never mind":
                                            jump Laura_BJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Laura_BJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Laura_BJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Laura_BJ_Reset
                                    $ Line = 0
                                    jump Laura_BJ_After
        #End menu (if Line)

        call Shift_Focus(LauraX)
        call Sex_Dialog(LauraX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1
        if Speed:
            $ Player.Wet = 1 #wets penis
            $ Player.Spunk = 0 if Player.Spunk else Player.Spunk #cleans you off after one cycle

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or LauraX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(LauraX)
                            if "angry" in LauraX.RecentActions:
                                call Laura_BJ_Reset
                                return
                            $ LauraX.Statup("Lust", 200, 5)
                            if 100 > LauraX.Lust >= 70 and LauraX.OCount < 2 and LauraX.SEXP >= 20:
                                $ LauraX.RecentActions.append("unsatisfied")
                                $ LauraX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Laura_BJ_After
                            $ Line = "came"

                    if LauraX.Lust >= 100:
                            #If Laura can cum
                            call Girl_Cumming(LauraX)
                            if Situation == "shift" or "angry" in LauraX.RecentActions:
                                jump Laura_BJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."

                            if "unsatisfied" in LauraX.RecentActions:#And Laura is unsatisfied,
                                "[LauraX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Laura_BJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if LauraX.SEXP >= 100 or ApprovalCheck(LauraX, 1200, "LO"):
            pass
        elif Cnt == (10 + LauraX.Blow):
                $ LauraX.Brows = "angry"
                menu:
                    ch_l "I'm getting kinda bored. Can we do something else?"
                    "How about a Handy?" if LauraX.Action and MultiAction:
                            $ Situation = "shift"
                            call Laura_BJ_After
                            call Laura_Handjob
                            return
                    "Finish up." if Player.FocusX:
                            "You release your concentration. . ."
                            $ Player.FocusX = 0
                            $ Player.Focus += 15
                            jump Laura_BJ_Cycle
                    "Let's try something else." if MultiAction:
                            $ Line = 0
                            call Laura_BJ_Reset
                            $ Situation = "shift"
                            jump Laura_BJ_After
                    "No, get back down there.":
                            if ApprovalCheck(LauraX, 1200) or ApprovalCheck(LauraX, 500, "O"):
                                $ LauraX.Statup("Love", 200, -5)
                                $ LauraX.Statup("Obed", 50, 3)
                                $ LauraX.Statup("Obed", 80, 2)
                                "She grumbles but gets back to work."
                            else:
                                $ LauraX.FaceChange("angry", 1)
                                "She scowls at you, drops you cock and pulls back."
                                ch_l "Well fuck you then."
                                $ LauraX.Statup("Love", 50, -3, 1)
                                $ LauraX.Statup("Love", 80, -4, 1)
                                $ LauraX.Statup("Obed", 30, -1, 1)
                                $ LauraX.Statup("Obed", 50, -1, 1)
                                $ LauraX.RecentActions.append("angry")
                                $ LauraX.DailyActions.append("angry")
                                jump Laura_BJ_After
        elif Cnt == (5 + LauraX.Blow) and LauraX.SEXP <= 100 and not ApprovalCheck(LauraX, 1200, "LO"):
                    $ LauraX.Brows = "confused"
                    ch_l "Are you getting close here? I'm bored."
        #End Count check

        call Escalation(LauraX) #sees if she wants to escalate things

        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [LauraX.Petname]."

    #Round = 0 loop breaks
    $ LauraX.FaceChange("bemused", 0)
    $ Line = 0
    ch_l "Ok, I'm taking a quick break. . ."

label Laura_BJ_After:
    $ LauraX.FaceChange("sexy")

    $ LauraX.Blow += 1
    $ LauraX.Action -=1
    $ LauraX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ LauraX.Addictionrate += 1

    call Partner_Like(LauraX,2)

    if "Laura Jobber" in Achievements:
        pass
    elif LauraX.Blow >= 10:
        $ LauraX.FaceChange("smile", 1)
        ch_l "Your flavor is intoxicating."
        $ Achievements.append("Laura Jobber")
        $LauraX.SEXP += 5
    elif Situation == "shift":
        pass
    elif LauraX.Blow == 1:
            $LauraX.SEXP += 15
            if LauraX.Love >= 500:
                $ LauraX.Mouth = "smile"
                ch_l "Hey, whaddaya know, that wasn't bad."
            elif Player.Focus <= 20:
                $ LauraX.Mouth = "sad"
                ch_l "I hope you enjoyed that."
    elif LauraX.Blow == 5:
        ch_l "I'm really getting the hang of this. . . right?"
        menu:
            "[[nod]":
                $ LauraX.FaceChange("smile", 1)
                $ LauraX.Statup("Love", 90, 15)
                $ LauraX.Statup("Obed", 80, 5)
                $ LauraX.Statup("Inbt", 90, 10)
            "[[shake head \"no\"]":
                if ApprovalCheck(LauraX, 500, "O"):
                    $ LauraX.FaceChange("sad", 2)
                    $ LauraX.Statup("Love", 200, -5)
                else:
                    $ LauraX.FaceChange("angry", 2)
                    $ LauraX.Statup("Love", 200, -25)
                $ LauraX.Statup("Obed", 80, 10)
                ch_l ". . ."
                $ LauraX.FaceChange("sad", 1)

    $ temp_modifier = 0
    if Situation != "shift":
        call Laura_BJ_Reset
    call Checkout
    return



# end LauraX.Blowjob                                 //////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy
label Laura_Dildo_Check:
    if "dildo" in Player.Inventory:
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in LauraX.Inventory:
        "You ask [LauraX.Name] to get out her favorite Dildo."
    else:
        "You don't have one of those on you."
        return 0
    return 1

label Laura_Dildo_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(LauraX)
    call Laura_Dildo_Check
    if not _return:
        return

    if LauraX.DildoP: #You've done it before
        $ temp_modifier += 15
    if LauraX.Legs == "pants:": # she's got pants on.
        $ temp_modifier -= 20

    if LauraX.Lust > 95:
        $ temp_modifier += 20
    elif LauraX.Lust > 85: #She's really horny
        $ temp_modifier += 15

    if Situation == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in LauraX.Traits:
        $ temp_modifier += (5*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.Petnames:
        $ temp_modifier += 10
    elif "ex" in LauraX.Traits:
        $ temp_modifier -= 40
    if LauraX.ForcedCount and not LauraX.Forced:
        $ temp_modifier -= 5 * LauraX.ForcedCount

    if Taboo and "tabno" in LauraX.DailyActions:
        $ temp_modifier -= 10

    if "no dildo" in LauraX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no dildo" in LauraX.RecentActions else 0

    $ Approval = ApprovalCheck(LauraX, 1250, TabM = 4) # 125, 140, 155, Taboo -160(335)

    if Situation == LauraX:                                                                  #Laura auto-starts
                if Approval > 2:                                                      # fix, add laura auto stuff here
                    if LauraX.PantsNum() == 5:
                        "[LauraX.Name] grabs her dildo, hiking up her skirt as she does."
                        $ LauraX.Upskirt = 1
                    elif LauraX.PantsNum() >= 6:
                        "[LauraX.Name] grabs her dildo, pulling down her pants as she does."
                        $ LauraX.Legs = 0
                    else:
                        "[LauraX.Name] grabs her dildo, rubbing is suggestively against her crotch."
                    $ LauraX.SeenPanties = 1
                    call Laura_First_Bottomless(1)
                    "She slides the tip along her pussy and seems to want you to insert it."
                    menu:
                        "What do you do?"
                        "Nothing.":
                            $ LauraX.Statup("Inbt", 80, 3)
                            $ LauraX.Statup("Inbt", 50, 2)
                            "[LauraX.Name] slides it in."
                        "Go for it.":
                            $ LauraX.FaceChange("sexy", 1)
                            $ LauraX.Statup("Inbt", 80, 3)
                            ch_p "Oh yeah, [LauraX.Pet], let's do this."
                            $ LauraX.NameCheck() #checks reaction to petname
                            "You grab the dildo and slide it in."
                            $ LauraX.Statup("Love", 85, 1)
                            $ LauraX.Statup("Obed", 90, 1)
                            $ LauraX.Statup("Obed", 50, 2)
                        "Ask her to stop.":
                            $ LauraX.FaceChange("surprised")
                            $ LauraX.Statup("Inbt", 70, 1)
                            ch_p "Let's not do that right now, [LauraX.Pet]."
                            $ LauraX.NameCheck() #checks reaction to petname
                            "[LauraX.Name] sets the dildo down."
                            $ LauraX.OutfitChange()
                            $ LauraX.Statup("Obed", 90, 1)
                            $ LauraX.Statup("Obed", 50, 1)
                            $ LauraX.Statup("Obed", 30, 2)
                            return
                    jump Laura_DP_Prep
                else:
                    $ temp_modifier = 0                               # fix, add laura auto stuff here
                    $ Trigger2 = 0
                return

    if Situation == "auto":
                "You rub the dildo across her body, and along her moist slit."
                $ LauraX.FaceChange("surprised", 1)

                if (LauraX.DildoP and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
                    "[LauraX.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                    $ LauraX.FaceChange("sexy")
                    $ LauraX.Statup("Obed", 70, 3)
                    $ LauraX.Statup("Inbt", 50, 3)
                    $ LauraX.Statup("Inbt", 70, 1)
                    ch_l "Ooo, [LauraX.Petname], toys!"
                    jump Laura_DP_Prep
                else:                                                                                                            #she's questioning it
                    $ LauraX.Brows = "angry"
                    menu:
                        ch_l "Hey, what are you planning to do with that?!"
                        "Sorry, sorry! Never mind.":
                            if Approval:
                                $ LauraX.FaceChange("sexy", 1)
                                $ LauraX.Statup("Obed", 70, 3)
                                $ LauraX.Statup("Inbt", 50, 3)
                                $ LauraX.Statup("Inbt", 70, 1)
                                ch_l "Well, now that you mention it. . ."
                                jump Laura_DP_Prep
                            "You pull back before you really get it in."
                            $ LauraX.FaceChange("bemused", 1)
                            if LauraX.DildoP:
                                ch_l "Well ok, [LauraX.Petname], maybe warn me next time?"
                            else:
                                ch_l "Well ok, [LauraX.Petname], that's a little much. . . for now . . ."
                        "Just playing with my favorite toys.":
                            $ LauraX.Statup("Love", 80, -10, 1)
                            $ LauraX.Statup("Love", 200, -10)
                            "You press it inside some more."
                            $ LauraX.Statup("Obed", 70, 3)
                            $ LauraX.Statup("Inbt", 50, 3)
                            if not ApprovalCheck(LauraX, 700, "O", TabM=1): #Checks if Obed is 700+
                                $ LauraX.FaceChange("angry")
                                "[LauraX.Name] shoves you away and slaps you in the face."
                                ch_l "Jerk!"
                                ch_l "Ask nice if you want to stick something in my pussy!"
                                $ LauraX.Statup("Love", 50, -10, 1)
                                $ LauraX.Statup("Obed", 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                if renpy.showing("Laura_SexSprite"):
                                    call Laura_Sex_Reset
                                $ LauraX.RecentActions.append("angry")
                                $ LauraX.DailyActions.append("angry")
                            else:
                                $ LauraX.FaceChange("sad")
                                "[LauraX.Name] doesn't seem to be into this, you're lucky she's so obedient."
                                jump Laura_DP_Prep
                return
    #end Auto

    if not LauraX.DildoP:
            #first time
            $ LauraX.FaceChange("surprised", 1)
            $ LauraX.Mouth = "kiss"
            ch_l "Hmmm, so you'd like to try out some toys?"
            if LauraX.Forced:
                $ LauraX.FaceChange("sad")
                ch_l "I suppose there are worst things you could ask for."

    if not LauraX.DildoP and Approval:
            #First time dialog
            if LauraX.Forced:
                $ LauraX.FaceChange("sad")
                $ LauraX.Statup("Love", 70, -3, 1)
                $ LauraX.Statup("Love", 20, -2, 1)
            elif LauraX.Love >= (LauraX.Obed + LauraX.Inbt):
                $ LauraX.FaceChange("sexy")
                $ LauraX.Brows = "sad"
                $ LauraX.Mouth = "smile"
                ch_l "I've had a reasonable amount of experience with these, you know. . ."
            elif LauraX.Obed >= LauraX.Inbt:
                $ LauraX.FaceChange("normal")
                ch_l "If that's what you want, [LauraX.Petname]. . ."
            else: # Uninhibited
                $ LauraX.FaceChange("sad")
                $ LauraX.Mouth = "smile"
                ch_l "I guess it could be fun with a partner. . ."

    elif Approval:
            #Second time+ dialog
            if LauraX.Forced:
                $ LauraX.FaceChange("sad")
                $ LauraX.Statup("Love", 70, -3, 1)
                $ LauraX.Statup("Love", 20, -2, 1)
                ch_l "The toys again?"
            elif not Taboo and "tabno" in LauraX.DailyActions:
                ch_l "Well, at least you got us some privacy this time. . ."
            elif "dildo pussy" in LauraX.RecentActions:
                $ LauraX.FaceChange("sexy", 1)
                ch_l "Mmm, again? Ok, let's get to it."
                jump Laura_DP_Prep
            elif "dildo pussy" in LauraX.DailyActions:
                $ LauraX.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Breaking out the toys again?",
                    "Didn't get enough earlier?",
                    "You're going to wear me out."])
                ch_l "[Line]"
            elif LauraX.DildoP < 3:
                $ LauraX.FaceChange("sexy", 1)
                $ LauraX.Brows = "confused"
                $ LauraX.Mouth = "kiss"
                ch_l "You want to stick it in my pussy again?"
            else:
                $ LauraX.FaceChange("sexy", 1)
                $ LauraX.ArmPose = 2
                $ Line = renpy.random.choice(["You want some of this action?",
                    "So you'd like another go?",
                    "You want to stick it in my pussy again?",
                    "You want me ta lube up your toy?"])
                ch_l "[Line]"
                $ Line = 0

    if Approval >= 2:
            #She's into it. . .
            if LauraX.Forced:
                $ LauraX.FaceChange("sad")
                $ LauraX.Statup("Obed", 90, 1)
                $ LauraX.Statup("Inbt", 60, 1)
                ch_l "Ok, fine."
            else:
                $ LauraX.FaceChange("sexy", 1)
                $ LauraX.Statup("Love", 90, 1)
                $ LauraX.Statup("Inbt", 50, 3)
                $ Line = renpy.random.choice(["Well, sure, stick it in.",
                    "Well. . . ok.",
                    "Sure!",
                    "I guess I could. . . stick it in.",
                    "Hells yeah.",
                    "Heh, ok, ok."])
                ch_l "[Line]"
                $ Line = 0
            $ LauraX.Statup("Obed", 20, 1)
            $ LauraX.Statup("Obed", 60, 1)
            $ LauraX.Statup("Inbt", 70, 2)
            jump Laura_DP_Prep

    else:
            #She's not into it, but maybe. . .
            $ LauraX.FaceChange("angry")
            if "no dildo" in LauraX.RecentActions:
                ch_l "What part of \"no,\" did you not get, [LauraX.Petname]?"
            elif Taboo and "tabno" in LauraX.DailyActions and "no dildo" in LauraX.DailyActions:
                ch_l "Stop swinging that thing around in public!"
            elif "no dildo" in LauraX.DailyActions:
                ch_l "I already told you \"no,\" [LauraX.Petname]."
            elif Taboo and "tabno" in LauraX.DailyActions:
                ch_l "Stop swinging that thing around in public!"
            elif not LauraX.DildoP:
                $ LauraX.FaceChange("bemused")
                ch_l "I'm just not into toys, [LauraX.Petname]. . ."
            else:
                $ LauraX.FaceChange("bemused")
                ch_l "I don't think we need any toys, [LauraX.Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in LauraX.DailyActions:
                    $ LauraX.FaceChange("bemused")
                    ch_l "Yeah, ok, [LauraX.Petname]."
                    return
                "Maybe later?" if "no dildo" not in LauraX.DailyActions:
                    $ LauraX.FaceChange("sexy")
                    ch_l "Maybe I'll practice on my own time, [LauraX.Petname]."
                    $ LauraX.Statup("Love", 80, 2)
                    $ LauraX.Statup("Inbt", 70, 2)
                    if Taboo:
                        $ LauraX.RecentActions.append("tabno")
                        $ LauraX.DailyActions.append("tabno")
                    $ LauraX.RecentActions.append("no dildo")
                    $ LauraX.DailyActions.append("no dildo")
                    return
                "I think you'd like it. . .":
                    if Approval:
                        $ LauraX.FaceChange("sexy")
                        $ LauraX.Statup("Obed", 90, 2)
                        $ LauraX.Statup("Obed", 50, 2)
                        $ LauraX.Statup("Inbt", 70, 3)
                        $ LauraX.Statup("Inbt", 40, 2)
                        $ Line = renpy.random.choice(["Well, sure, stick it in.",
                            "I suppose. . .",
                            "You've got me there."])
                        ch_l "[Line]"
                        $ Line = 0
                        jump Laura_DP_Prep
                    else:
                        pass

                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck(LauraX, 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                    if Approval > 1 or (Approval and LauraX.Forced):
                        $ LauraX.FaceChange("sad")
                        $ LauraX.Statup("Love", 70, -5, 1)
                        $ LauraX.Statup("Love", 200, -5)
                        ch_l "Ok, fine. If we're going to do this, stick it in already."
                        $ LauraX.Statup("Obed", 80, 4)
                        $ LauraX.Statup("Inbt", 80, 1)
                        $ LauraX.Statup("Inbt", 60, 3)
                        $ LauraX.Forced = 1
                        jump Laura_DP_Prep
                    else:
                        $ LauraX.Statup("Love", 200, -20)
                        $ LauraX.RecentActions.append("angry")
                        $ LauraX.DailyActions.append("angry")

    #She refused all offers.
    $ LauraX.ArmPose = 1
    if "no dildo" in LauraX.DailyActions:
            ch_l "Learn to take \"no\" for an answer, [LauraX.Petname]."
            $ LauraX.RecentActions.append("angry")
            $ LauraX.DailyActions.append("angry")
    elif LauraX.Forced:
            $ LauraX.FaceChange("angry", 1)
            ch_l "I'm not going to let you use that on me."
            $ LauraX.Statup("Lust", 200, 5)
            if LauraX.Love > 300:
                    $ LauraX.Statup("Love", 70, -2)
            $ LauraX.Statup("Obed", 50, -2)
            $ LauraX.RecentActions.append("angry")
            $ LauraX.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
            $ LauraX.FaceChange("angry", 1)
            $ LauraX.RecentActions.append("tabno")
            $ LauraX.DailyActions.append("tabno")
            ch_l "Not here!"
            $ LauraX.Statup("Lust", 200, 5)
            $ LauraX.Statup("Obed", 50, -3)
    elif LauraX.DildoP:
            $ LauraX.FaceChange("sad")
            ch_l "Sorry, you can keep your toys to yourself."
    else:
            $ LauraX.FaceChange("normal", 1)
            ch_l "No way."
    $ LauraX.RecentActions.append("no dildo")
    $ LauraX.DailyActions.append("no dildo")
    $ temp_modifier = 0
    return

label Laura_DP_Prep: #Animation set-up
    if Trigger2 == "dildo pussy":
        return

    if not LauraX.Forced and Situation != "auto":
        $ temp_modifier = 15 if LauraX.PantsNum() >= 6 else 0
        call Bottoms_Off(LauraX)
        if "angry" in LauraX.RecentActions:
            return

    $ temp_modifier = 0
    call Laura_Pussy_Launch("dildo pussy")
    if not LauraX.DildoP:
        if LauraX.Forced:
            $ LauraX.Statup("Love", 90, -75)
            $ LauraX.Statup("Obed", 70, 60)
            $ LauraX.Statup("Inbt", 80, 35)
        else:
            $ LauraX.Statup("Love", 90, 10)
            $ LauraX.Statup("Obed", 70, 20)
            $ LauraX.Statup("Inbt", 80, 45)
    if Taboo:
        $ LauraX.Inbt += int(Taboo/10)
        $ LauraX.Lust += int(Taboo/5)


    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ LauraX.DrainWord("tabno")
    $ LauraX.DrainWord("no dildo")
    $ LauraX.RecentActions.append("dildo pussy")
    $ LauraX.DailyActions.append("dildo pussy")

label Laura_DP_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(LauraX)
        call Laura_Pussy_Launch("dildo pussy")
        $ LauraX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                call Slap_Ass(LauraX)
                                jump Laura_DP_Cycle

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
                                            if LauraX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ LauraX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")

                                    "Shift primary action":
                                            if LauraX.Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in her ass.":
                                                                $ Situation = "shift"
                                                                call Laura_DP_After
                                                                call Laura_Insert_Ass
                                                        "Just stick a finger in her ass without asking.":
                                                                $ Situation = "auto"
                                                                call Laura_DP_After
                                                                call Laura_Insert_Ass
                                                        "I want to shift the dildo to her ass.":
                                                                $ Situation = "shift"
                                                                call Laura_DP_After
                                                                call Laura_Dildo_Ass
                                                        "Never Mind":
                                                                jump Laura_DP_Cycle
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Laura_DP_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [LauraX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(LauraX)
                                            "Ask [LauraX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(LauraX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(LauraX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Laura_DP_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Laura_DP_Cycle
                                            "Never mind":
                                                        jump Laura_DP_Cycle
                                    "undress [LauraX.Name]":
                                            call Girl_Undress(LauraX)
                                    "Clean up [LauraX.Name] (locked)" if not LauraX.Spunk:
                                            pass
                                    "Clean up [LauraX.Name]" if LauraX.Spunk:
                                            call Girl_Cleanup(LauraX,"ask")
                                    "Never mind":
                                            jump Laura_DP_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Laura_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Laura_DP_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Laura_Pos_Reset
                                    $ Line = 0
                                    jump Laura_DP_After
        #End menu (if Line)

        if LauraX.Panties or LauraX.PantsNum() >= 6 or LauraX.HoseNum() >= 5: #This checks if Laura wants to strip down.
                call Girl_Undress(LauraX,"auto")

        call Shift_Focus(LauraX)
        call Sex_Dialog(LauraX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or LauraX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(LauraX)
                            if "angry" in LauraX.RecentActions:
                                call Laura_Pos_Reset
                                return
                            $ LauraX.Statup("Lust", 200, 5)
                            if 100 > LauraX.Lust >= 70 and LauraX.OCount < 2:
                                $ LauraX.RecentActions.append("unsatisfied")
                                $ LauraX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Laura_DP_After
                            $ Line = "came"

                    if LauraX.Lust >= 100:
                            #If Laura can cum
                            call Girl_Cumming(LauraX)
                            if Situation == "shift" or "angry" in LauraX.RecentActions:
                                jump Laura_DP_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in LauraX.RecentActions:#And Laura is unsatisfied,
                                "[LauraX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Laura_DP_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if LauraX.SEXP >= 100 or ApprovalCheck(LauraX, 1200, "LO"):
            pass
        elif Cnt == (5 + LauraX.DildoP):
                    $ LauraX.Brows = "confused"
                    ch_l "What are you even doing down there?"
        elif LauraX.Lust >= 80:
                    pass
        elif Cnt == (15 + LauraX.DildoP) and LauraX.SEXP >= 15 and not ApprovalCheck(LauraX, 1500):
                    $ LauraX.Brows = "confused"
                    menu:
                        ch_l "[LauraX.Petname], this is getting uncomfortable, maybe we could try something else."
                        "Finish up.":
                                "You let go. . ."
                                jump Laura_DP_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Laura_DP_After
                        "No, this is fun.":
                                if ApprovalCheck(LauraX, 1200) or ApprovalCheck(LauraX, 500, "O"):
                                    $ LauraX.Statup("Love", 200, -5)
                                    $ LauraX.Statup("Obed", 50, 3)
                                    $ LauraX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ LauraX.FaceChange("angry", 1)
                                    call Laura_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_l "Well if that's your attitude, I don't need your \"help\"."
                                    $ LauraX.Statup("Love", 50, -3, 1)
                                    $ LauraX.Statup("Love", 80, -4, 1)
                                    $ LauraX.Statup("Obed", 30, -1, 1)
                                    $ LauraX.Statup("Obed", 50, -1, 1)
                                    $ LauraX.RecentActions.append("angry")
                                    $ LauraX.DailyActions.append("angry")
                                    jump Laura_DP_After
        #End Count check

        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [LauraX.Petname]."

    #Round = 0 loop breaks
    $ LauraX.FaceChange("bemused", 0)
    $ Line = 0
    ch_l "Ok, [LauraX.Petname], breaktime."


label Laura_DP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Laura_Pos_Reset

    $ LauraX.FaceChange("sexy")

    $ LauraX.DildoP += 1
    $ LauraX.Action -=1

    call Partner_Like(LauraX,1)

    if LauraX.DildoP == 1:
            $ LauraX.SEXP += 10
            if not Situation:
                if LauraX.Love >= 500 and "unsatisfied" not in LauraX.RecentActions:
                    ch_l "Thanks for the extra hand. . ."
                elif LauraX.Obed <= 500 and Player.Focus <= 20:
                    $ LauraX.FaceChange("perplexed", 1)
                    ch_l "Did you like that?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_l "Mmm, so what else did you have in mind?"
    call Checkout
    return

# end LauraX.Dildo Pussy /////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////Start Insert Ass

label Laura_Dildo_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(LauraX)
    call Laura_Dildo_Check
    if not _return:
        return

    if LauraX.Loose:
        $ temp_modifier += 30
    elif "anal" in LauraX.RecentActions or "dildo anal" in LauraX.RecentActions:
        $ temp_modifier -= 20
    elif "anal" in LauraX.DailyActions or "dildo anal" in LauraX.DailyActions:
        $ temp_modifier -= 10
    elif (LauraX.Anal + LauraX.DildoA + LauraX.Plug) > 0: #You've done it before
        $ temp_modifier += 20

    if LauraX.Legs == "pants:": # she's got pants on.
        $ temp_modifier -= 20

    if LauraX.Lust > 95:
        $ temp_modifier += 20
    elif LauraX.Lust > 85: #She's really horny
        $ temp_modifier += 15

    if Situation == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in LauraX.Traits:
        $ temp_modifier += (5*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.Petnames:
        $ temp_modifier += 10
    elif "ex" in LauraX.Traits:
        $ temp_modifier -= 40
    if LauraX.ForcedCount and not LauraX.Forced:
        $ temp_modifier -= 5 * LauraX.ForcedCount

    if Taboo and "tabno" in LauraX.DailyActions:
        $ temp_modifier -= 10

    if "no dildo" in LauraX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no dildo" in LauraX.RecentActions else 0

    $ Approval = ApprovalCheck(LauraX, 1450, TabM = 4) # 145, 160, 175, Taboo -160(355)

    if Situation == LauraX:
            #Laura auto-starts
            if Approval > 2:                                                      # fix, add laura auto stuff here
                if LauraX.PantsNum() == 5:
                    "[LauraX.Name] grabs her dildo, hiking up her skirt as she does."
                    $ LauraX.Upskirt = 1
                elif LauraX.PantsNum() >= 6:
                    "[LauraX.Name] grabs her dildo, pulling down her pants as she does."
                    $ LauraX.Legs = 0
                else:
                    "[LauraX.Name] grabs her dildo, rubbing is suggestively against her ass."
                $ LauraX.SeenPanties = 1
                call Laura_First_Bottomless(1)
                "She slides the tip against her asshole, and seems to want you to insert it."
                menu:
                    "What do you do?"
                    "Nothing.":
                        $ LauraX.Statup("Inbt", 80, 3)
                        $ LauraX.Statup("Inbt", 50, 2)
                        "[LauraX.Name] slides it in."
                    "Go for it.":
                        $ LauraX.FaceChange("sexy", 1)
                        $ LauraX.Statup("Inbt", 80, 3)
                        ch_p "Oh yeah, [LauraX.Pet], let's do this."
                        $ LauraX.NameCheck() #checks reaction to petname
                        "You grab the dildo and slide it in."
                        $ LauraX.Statup("Love", 85, 1)
                        $ LauraX.Statup("Obed", 90, 1)
                        $ LauraX.Statup("Obed", 50, 2)
                    "Ask her to stop.":
                        $ LauraX.FaceChange("surprised")
                        $ LauraX.Statup("Inbt", 70, 1)
                        ch_p "Let's not do that right now, [LauraX.Pet]."
                        $ LauraX.NameCheck() #checks reaction to petname
                        "[LauraX.Name] sets the dildo down."
                        $ LauraX.OutfitChange()
                        $ LauraX.Statup("Obed", 90, 1)
                        $ LauraX.Statup("Obed", 50, 1)
                        $ LauraX.Statup("Obed", 30, 2)
                        return
                jump Laura_DA_Prep
            else:
                $ temp_modifier = 0                               # fix, add laura auto stuff here
                $ Trigger2 = 0
            return

    if Situation == "auto":
            "You rub the dildo across her body, and against her tight anus."
            $ LauraX.FaceChange("surprised", 1)

            if (LauraX.DildoA and Approval) or (Approval > 1):
                #this is not the first time you've had sex, or she's into it
                "[LauraX.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                $ LauraX.FaceChange("sexy")
                $ LauraX.Statup("Obed", 70, 3)
                $ LauraX.Statup("Inbt", 50, 3)
                $ LauraX.Statup("Inbt", 70, 1)
                ch_l "Ooo, [LauraX.Petname], toys!"
                jump Laura_DA_Prep
            else:
                #she's questioning it
                $ LauraX.Brows = "angry"
                menu:
                    ch_l "Hey, what are you planning to do with that?!"
                    "Sorry, sorry! Never mind.":
                        if Approval:
                            $ LauraX.FaceChange("sexy", 1)
                            $ LauraX.Statup("Obed", 70, 3)
                            $ LauraX.Statup("Inbt", 50, 3)
                            $ LauraX.Statup("Inbt", 70, 1)
                            ch_l "Well, now that you mention it. . ."
                            jump Laura_DA_Prep
                        "You pull back before you really get it in."
                        $ LauraX.FaceChange("bemused", 1)
                        if LauraX.DildoA:
                            ch_l "Well ok, [LauraX.Petname], maybe warn me next time?"
                        else:
                            ch_l "Well ok, [LauraX.Petname], that's a little much. . . for now . . ."
                    "Just playing with my favorite toys.":
                        $ LauraX.Statup("Love", 80, -10, 1)
                        $ LauraX.Statup("Love", 200, -10)
                        "You press it inside some more."
                        $ LauraX.Statup("Obed", 70, 3)
                        $ LauraX.Statup("Inbt", 50, 3)
                        if not ApprovalCheck(LauraX, 700, "O", TabM=1): #Checks if Obed is 700+
                            $ LauraX.FaceChange("angry")
                            "[LauraX.Name] shoves you away and slaps you in the face."
                            ch_l "Jerk!"
                            ch_l "Ask nice if you want to stick something in my ass!"
                            $ LauraX.Statup("Love", 50, -10, 1)
                            $ LauraX.Statup("Obed", 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            if renpy.showing("Laura_SexSprite"):
                                call Laura_Sex_Reset
                            $ LauraX.RecentActions.append("angry")
                            $ LauraX.DailyActions.append("angry")
                        else:
                            $ LauraX.FaceChange("sad")
                            "[LauraX.Name] doesn't seem to be into this, you're lucky she's so obedient."
                            jump Laura_DA_Prep
            return
    #end auto

    if not LauraX.DildoA:
            #first time
            $ LauraX.FaceChange("surprised", 1)
            $ LauraX.Mouth = "kiss"
            ch_l "You want to try and fit that. . .?"
            if LauraX.Forced:
                $ LauraX.FaceChange("sad")
                ch_l "Always about the butt, huh?"

    if not LauraX.Loose and ("dildo anal" in LauraX.RecentActions or "anal" in LauraX.RecentActions or "dildo anal" in LauraX.DailyActions or "anal" in LauraX.DailyActions):
            $ LauraX.FaceChange("bemused", 1)
            ch_l "I'm still sore from earlier. . ."

    if not LauraX.DildoA and Approval:
            #First time dialog
            if LauraX.Forced:
                $ LauraX.FaceChange("sad")
                $ LauraX.Statup("Love", 70, -3, 1)
                $ LauraX.Statup("Love", 20, -2, 1)
            elif LauraX.Love >= (LauraX.Obed + LauraX.Inbt):
                $ LauraX.FaceChange("sexy")
                $ LauraX.Brows = "sad"
                $ LauraX.Mouth = "smile"
                ch_l "I haven't actually used one of these, back there before. . ."
            elif LauraX.Obed >= LauraX.Inbt:
                $ LauraX.FaceChange("normal")
                ch_l "If that's what you want, [LauraX.Petname]. . ."
            else: # Uninhibited
                $ LauraX.FaceChange("sad")
                $ LauraX.Mouth = "smile"
                ch_l "I guess it could be fun two-player. . ."

    elif Approval:
            #Second time+ dialog
            if LauraX.Forced:
                $ LauraX.FaceChange("sad")
                $ LauraX.Statup("Love", 70, -3, 1)
                $ LauraX.Statup("Love", 20, -2, 1)
                ch_l "The toys again?"
            elif not Taboo and "tabno" in LauraX.DailyActions:
                ch_l "Well, at least you got us some privacy this time. . ."
            elif "dildo anal" in LauraX.DailyActions and not LauraX.Loose:
                pass
            elif "dildo anal" in LauraX.DailyActions:
                $ LauraX.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Breaking out the toys again?",
                    "Didn't get enough earlier?",
                    "I'm still a bit sore from earlier.",
                    "You're going to wear me out."])
                ch_l "[Line]"
            elif LauraX.DildoA < 3:
                $ LauraX.FaceChange("sexy", 1)
                $ LauraX.Brows = "confused"
                $ LauraX.Mouth = "kiss"
                ch_l "You want to stick it in my ass again?"
            else:
                $ LauraX.FaceChange("sexy", 1)
                $ LauraX.ArmPose = 2
                $ Line = renpy.random.choice(["You want some of this action?",
                    "So you'd like another go?",
                    "You want to stick it in my ass again?",
                    "You want me ta lube up your toy?"])
                ch_l "[Line]"
                $ Line = 0

    if Approval >= 2:
            #She's into it. . .
            if LauraX.Forced:
                $ LauraX.FaceChange("sad")
                $ LauraX.Statup("Obed", 90, 1)
                $ LauraX.Statup("Inbt", 60, 1)
                ch_l "Ok, fine."
            else:
                $ LauraX.FaceChange("sexy", 1)
                $ LauraX.Statup("Love", 90, 1)
                $ LauraX.Statup("Inbt", 50, 3)
                $ Line = renpy.random.choice(["Well, sure, stick it in.",
                    "Well. . . ok.",
                    "Sure!",
                    "I guess I could. . . stick it in.",
                    "Hells yeah.",
                    "Heh, ok, ok."])
                ch_l "[Line]"
                $ Line = 0
            $ LauraX.Statup("Obed", 20, 1)
            $ LauraX.Statup("Obed", 60, 1)
            $ LauraX.Statup("Inbt", 70, 2)
            jump Laura_DA_Prep

    else:
            #She's not into it, but maybe. . .
            $ LauraX.FaceChange("angry")
            if "no dildo" in LauraX.RecentActions:
                ch_l "What part of \"no,\" did you not get, [LauraX.Petname]?"
            elif Taboo and "tabno" in LauraX.DailyActions and "no dildo" in LauraX.DailyActions:
                ch_l "Stop swinging that thing around in public!"
            elif "no dildo" in LauraX.DailyActions:
                ch_l "I already told you \"no,\" [LauraX.Petname]."
            elif Taboo and "tabno" in LauraX.DailyActions:
                ch_l "I already told you that I wouldn't do that out here!"
            elif not LauraX.DildoA:
                $ LauraX.FaceChange("bemused")
                ch_l "I'm just not into toys, [LauraX.Petname]. . ."
            elif not LauraX.Loose and "dildo anal" not in LauraX.DailyActions:
                $ LauraX.FaceChange("perplexed")
                ch_l "You could have been a bit more gentle last time, [LauraX.Petname]. . ."
            else:
                $ LauraX.FaceChange("bemused")
                ch_l "I don't think we need any toys, [LauraX.Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in LauraX.DailyActions:
                    $ LauraX.FaceChange("bemused")
                    ch_l "Yeah, ok, [LauraX.Petname]."
                    return
                "Maybe later?" if "no dildo" not in LauraX.DailyActions:
                    $ LauraX.FaceChange("sexy")
                    ch_l "Maybe I'll practice on my own time, [LauraX.Petname]."
                    $ LauraX.Statup("Love", 80, 2)
                    $ LauraX.Statup("Inbt", 70, 2)
                    if Taboo:
                        $ LauraX.RecentActions.append("tabno")
                        $ LauraX.DailyActions.append("tabno")
                    $ LauraX.RecentActions.append("no dildo")
                    $ LauraX.DailyActions.append("no dildo")
                    return
                "I think you'd like it. . .":
                    if Approval:
                        $ LauraX.FaceChange("sexy")
                        $ LauraX.Statup("Obed", 90, 2)
                        $ LauraX.Statup("Obed", 50, 2)
                        $ LauraX.Statup("Inbt", 70, 3)
                        $ LauraX.Statup("Inbt", 40, 2)
                        $ Line = renpy.random.choice(["Well, sure, stick it in.",
                            "I suppose. . .",
                            "You've got me there."])
                        ch_l "[Line]"
                        $ Line = 0
                        jump Laura_DA_Prep
                    else:
                        pass

                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck(LauraX, 1050, "OI", TabM = 3) # 105, 120, 135, -120(225)
                    if Approval > 1 or (Approval and LauraX.Forced):
                        $ LauraX.FaceChange("sad")
                        $ LauraX.Statup("Love", 70, -5, 1)
                        $ LauraX.Statup("Love", 200, -5)
                        ch_l "Ok, fine. If we're going to do this, stick it in already."
                        $ LauraX.Statup("Obed", 80, 4)
                        $ LauraX.Statup("Inbt", 80, 1)
                        $ LauraX.Statup("Inbt", 60, 3)
                        $ LauraX.Forced = 1
                        jump Laura_DA_Prep
                    else:
                        $ LauraX.Statup("Love", 200, -20)
                        $ LauraX.RecentActions.append("angry")
                        $ LauraX.DailyActions.append("angry")

    #She refused all offers.
    $ LauraX.ArmPose = 1
    if "no dildo" in LauraX.DailyActions:
            ch_l "Learn to take \"no\" for an answer, [LauraX.Petname]."
            $ LauraX.RecentActions.append("angry")
            $ LauraX.DailyActions.append("angry")
    elif LauraX.Forced:
            $ LauraX.FaceChange("angry", 1)
            ch_l "I'm not going to let you use that on me."
            $ LauraX.Statup("Lust", 200, 5)
            if LauraX.Love > 300:
                    $ LauraX.Statup("Love", 70, -2)
            $ LauraX.Statup("Obed", 50, -2)
            $ LauraX.RecentActions.append("angry")
            $ LauraX.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
            $ LauraX.FaceChange("angry", 1)
            $ LauraX.RecentActions.append("tabno")
            $ LauraX.DailyActions.append("tabno")
            ch_l "Not here!"
            $ LauraX.Statup("Lust", 200, 5)
            $ LauraX.Statup("Obed", 50, -3)
    elif not LauraX.Loose and "dildo anal" in LauraX.DailyActions:
            $ LauraX.FaceChange("bemused")
            ch_l "Sorry, I just need a little break back there, [LauraX.Petname]."
    elif LauraX.DildoA:
            $ LauraX.FaceChange("sad")
            ch_l "Sorry, you can keep your toys out of there."
    else:
            $ LauraX.FaceChange("normal", 1)
            ch_l "No way."
    $ LauraX.RecentActions.append("no dildo")
    $ LauraX.DailyActions.append("no dildo")
    $ temp_modifier = 0
    return

label Laura_DA_Prep: #Animation set-up
    if Trigger2 == "dildo anal":
        return

    if not LauraX.Forced and Situation != "auto":
        $ temp_modifier = 20 if LauraX.PantsNum() >= 6 else 0
        call Bottoms_Off(LauraX)
        if "angry" in LauraX.RecentActions:
            return

    $ temp_modifier = 0
    call Laura_Pussy_Launch("dildo anal")
    if not LauraX.DildoA:
        if LauraX.Forced:
            $ LauraX.Statup("Love", 90, -75)
            $ LauraX.Statup("Obed", 70, 60)
            $ LauraX.Statup("Inbt", 80, 35)
        else:
            $ LauraX.Statup("Love", 90, 10)
            $ LauraX.Statup("Obed", 70, 20)
            $ LauraX.Statup("Inbt", 80, 45)
    if Taboo:
        $ LauraX.Inbt += int(Taboo/10)
        $ LauraX.Lust += int(Taboo/5)


    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ LauraX.DrainWord("tabno")
    $ LauraX.DrainWord("no dildo")
    $ LauraX.RecentActions.append("dildo anal")
    $ LauraX.DailyActions.append("dildo anal")

label Laura_DA_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(LauraX)
        call Laura_Pussy_Launch("dildo anal")
        $ LauraX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                call Slap_Ass(LauraX)
                                jump Laura_DA_Cycle

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
                                            if LauraX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ LauraX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")

                                    "Shift primary action":
                                            if LauraX.Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in her pussy.":
                                                                $ Situation = "shift"
                                                                call Laura_DA_After
                                                                call Laura_Fondle_Pussy
                                                        "Just stick a finger in her pussy without asking.":
                                                                $ Situation = "auto"
                                                                call Laura_DA_After
                                                                call Laura_Fondle_Pussy
                                                        "I want to shift the dildo to her pussy.":
                                                                $ Situation = "shift"
                                                                call Laura_DA_After
                                                                call Laura_Dildo_Pussy
                                                        "Never Mind":
                                                                jump Laura_DA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Laura_DA_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [LauraX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(LauraX)
                                            "Ask [LauraX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(LauraX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(LauraX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Laura_DA_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Laura_DA_Cycle
                                    "Never mind":
                                            jump Laura_DA_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Laura_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Laura_DA_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Laura_Pos_Reset
                                    $ Line = 0
                                    jump Laura_DA_After
        #End menu (if Line)

        if LauraX.Panties or LauraX.PantsNum() >= 6 or LauraX.HoseNum() >= 5: #This checks if Laura wants to strip down.
                call Girl_Undress(LauraX,"auto")

        call Shift_Focus(LauraX)
        call Sex_Dialog(LauraX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or LauraX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(LauraX)
                            if "angry" in LauraX.RecentActions:
                                call Laura_Pos_Reset
                                return
                            $ LauraX.Statup("Lust", 200, 5)
                            if 100 > LauraX.Lust >= 70 and LauraX.OCount < 2:
                                $ LauraX.RecentActions.append("unsatisfied")
                                $ LauraX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Laura_DA_After
                            $ Line = "came"

                    if LauraX.Lust >= 100:
                            #If Laura can cum
                            call Girl_Cumming(LauraX)
                            if Situation == "shift" or "angry" in LauraX.RecentActions:
                                jump Laura_DA_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in LauraX.RecentActions:#And Laura is unsatisfied,
                                "[LauraX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Laura_DA_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if LauraX.SEXP >= 100 or ApprovalCheck(LauraX, 1200, "LO"):
            pass
        elif Cnt == (5 + LauraX.DildoA):
                    $ LauraX.Brows = "confused"
                    ch_l "What are you even doing down there?"
        elif LauraX.Lust >= 80:
                    pass
        elif Cnt == (15 + LauraX.DildoA) and LauraX.SEXP >= 15 and not ApprovalCheck(LauraX, 1500):
                    $ LauraX.Brows = "confused"
                    menu:
                        ch_l "[LauraX.Petname], this is getting uncomfortable, maybe we could try something else."
                        "Finish up.":
                                "You let go. . ."
                                jump Laura_DA_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Laura_DA_After
                        "No, this is fun.":
                                if ApprovalCheck(LauraX, 1200) or ApprovalCheck(LauraX, 500, "O"):
                                    $ LauraX.Statup("Love", 200, -5)
                                    $ LauraX.Statup("Obed", 50, 3)
                                    $ LauraX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ LauraX.FaceChange("angry", 1)
                                    call Laura_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_l "Well if that's your attitude, I don't need your \"help\"."
                                    $ LauraX.Statup("Love", 50, -3, 1)
                                    $ LauraX.Statup("Love", 80, -4, 1)
                                    $ LauraX.Statup("Obed", 30, -1, 1)
                                    $ LauraX.Statup("Obed", 50, -1, 1)
                                    $ LauraX.RecentActions.append("angry")
                                    $ LauraX.DailyActions.append("angry")
                                    jump Laura_DA_After
        #End Count check

        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [LauraX.Petname]."

    #Round = 0 loop breaks
    $ LauraX.FaceChange("bemused", 0)
    $ Line = 0
    ch_l "Ok, [LauraX.Petname], breaktime."

label Laura_DA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Laura_Pos_Reset

    $ LauraX.FaceChange("sexy")

    $ LauraX.DildoA += 1
    $ LauraX.Action -=1

    call Partner_Like(LauraX,1)

    if LauraX.DildoA == 1:
            $ LauraX.SEXP += 10
            if not Situation:
                if LauraX.Love >= 500 and "unsatisfied" not in LauraX.RecentActions:
                    if LauraX.Loose:
                        ch_l "That was. . . interesting. . ."
                    else:
                        ch_l "Ouch. . ."
                elif LauraX.Obed <= 500 and Player.Focus <= 20:
                    $ LauraX.FaceChange("perplexed", 1)
                    ch_l "Did you like that?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_l "Mmm, so what else did you have in mind?"
    call Checkout
    return

# end LauraX.Dildo Ass /////////////////////////////////////////////////////////////////////////////

label Laura_Vibrator_Check:                                                                                 #fix this whole section is copy/paste unfinished
    if "vibrator" in Player.Inventory:
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in LauraX.Inventory:
        "You ask [LauraX.Name] to get out her vibrator."
    else:
        "You don't have one of those on you."
        return 0
    return 1

## LauraX.Footjob //////////////////////////////////////////////////////////////////////
label Laura_Footjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(LauraX)
    if LauraX.Foot >= 7: # She loves it
        $ temp_modifier += 10
    elif LauraX.Foot >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif LauraX.Foot: #You've done it before
        $ temp_modifier += 3

    if LauraX.Addict >= 75 and LauraX.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 10
    if LauraX.Addict >= 75:
        $ temp_modifier += 5

    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in LauraX.Traits:
        $ temp_modifier += (3*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.Petnames:
        $ temp_modifier += 10
    elif "ex" in LauraX.Traits:
        $ temp_modifier -= 40
    if LauraX.ForcedCount and not LauraX.Forced:
        $ temp_modifier -= 5 * LauraX.ForcedCount

    if Taboo and "tabno" in LauraX.DailyActions:
        $ temp_modifier -= 10

    if "no foot" in LauraX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no foot" in LauraX.RecentActions else 0

    $ Approval = ApprovalCheck(LauraX, 1250, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if Situation == LauraX:                                                                  #Laura auto-starts
        if Approval > 2:                                                      # fix, add laura auto stuff here
            "[LauraX.Name] leans back  and starts rubbing your cock with her foot."
            menu:
                "What do you do?"
                "Nothing.":
                    $ LauraX.Statup("Inbt", 70, 3)
                    $ LauraX.Statup("Inbt", 30, 2)
                    "[LauraX.Name] continues her actions."
                "Praise her.":
                    $ LauraX.FaceChange("sexy", 1)
                    $ LauraX.Statup("Inbt", 70, 3)
                    ch_p "Oooh, that's good, [LauraX.Pet]."
                    $ LauraX.NameCheck() #checks reaction to petname
                    "[LauraX.Name] continues her actions."
                    $ LauraX.Statup("Love", 80, 1)
                    $ LauraX.Statup("Obed", 90, 1)
                    $ LauraX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ LauraX.FaceChange("surprised")
                    $ LauraX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [LauraX.Pet]."
                    $ LauraX.NameCheck() #checks reaction to petname
                    "[LauraX.Name] puts it down."
                    $ LauraX.Statup("Obed", 90, 1)
                    $ LauraX.Statup("Obed", 50, 1)
                    $ LauraX.Statup("Obed", 30, 2)
                    return
            if Trigger:
                $ Trigger3 = "foot"
                return
            jump Laura_FJ_Prep
        else:
            $ temp_modifier = 0                               # fix, add laura auto stuff here
            $ Trigger2 = 0
            return

    if not LauraX.Foot and "no foot" not in LauraX.RecentActions:
        $ LauraX.FaceChange("confused", 2)
        ch_l "Standard footjob?"
        $ LauraX.Blush = 1

    if not LauraX.Foot and Approval:                                                 #First time dialog
        if LauraX.Forced:
            $ LauraX.FaceChange("sad",1)
            $ LauraX.Statup("Love", 70, -3, 1)
            $ LauraX.Statup("Love", 20, -2, 1)
        elif LauraX.Love >= (LauraX.Obed + LauraX.Inbt):
            $ LauraX.FaceChange("sexy",1)
            $ LauraX.Brows = "sad"
            $ LauraX.Mouth = "smile"
            ch_l "I guess it couldn't hurt. . ."
        elif LauraX.Obed >= LauraX.Inbt:
            $ LauraX.FaceChange("normal",1)
            ch_l "If you want, [LauraX.Petname]. . ."
        elif LauraX.Addict >= 50:
            $ LauraX.FaceChange("manic", 1)
            ch_l "Okay. . ."
        else: # Uninhibited
            $ LauraX.FaceChange("lipbite",1)
            ch_l "Sure. . ."

    elif Approval:                                                                       #Second time+ dialog
        if LauraX.Forced:
            $ LauraX.FaceChange("sad")
            $ LauraX.Statup("Love", 70, -3, 1)
            $ LauraX.Statup("Love", 20, -2, 1)
            ch_l "That's it?"
        elif not Taboo and "tabno" in LauraX.DailyActions:
            ch_l "Um, I guess this is secure enough. . ."
        elif "foot" in LauraX.DailyActions:
            $ LauraX.FaceChange("sexy", 1)
            ch_l "More of that, huh. . ."
            jump Laura_FJ_Prep
#        elif "foot" in LauraX.DailyActions:
#            $ LauraX.FaceChange("sexy", 1)
#            $ Line = renpy.random.choice(["Another one?",
#                "Didn't get enough earlier?",
#                "My feet are kinda sore from earlier.",
#                "My feet are kinda sore from earlier."])
#            ch_l "[Line]"
        elif LauraX.Foot < 3:
            $ LauraX.FaceChange("sexy", 1)
            $ LauraX.Brows = "confused"
            $ LauraX.Mouth = "kiss"
            ch_l "Hmm, magic toes. . ."
        else:
            $ LauraX.FaceChange("sexy", 1)
            $ LauraX.ArmPose = 2
            $ Line = renpy.random.choice(["You want me to use my feet?",
                "So you'd like another footjob?",
                "A little. . . [she rubs her foot along your leg]?",
                "A little TLC?"])
            ch_l "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if LauraX.Forced:
            $ LauraX.FaceChange("sad")
            $ LauraX.Statup("Obed", 90, 1)
            $ LauraX.Statup("Inbt", 60, 1)
            ch_l "Ok, sure."
        elif "no foot" in LauraX.DailyActions:
            ch_l "Fine."
        else:
            $ LauraX.FaceChange("sexy", 1)
            $ LauraX.Statup("Love", 90, 1)
            $ LauraX.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Sure, I guess.",
                "OK.",
                "Fine, lemme see it.",
                "I guess I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Heh, ok, ok."])
            ch_l "[Line]"
            $ Line = 0
        $ LauraX.Statup("Obed", 20, 1)
        $ LauraX.Statup("Obed", 60, 1)
        $ LauraX.Statup("Inbt", 70, 2)
        jump Laura_FJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ LauraX.FaceChange("angry")
        if "no foot" in LauraX.RecentActions:
            ch_l "You should listen better, [LauraX.Petname]."
        elif Taboo and "tabno" in LauraX.DailyActions and "no foot" in LauraX.DailyActions:
            ch_l "I said not in public."
        elif "no foot" in LauraX.DailyActions:
            ch_l "I told you \"no,\" [LauraX.Petname]."
        elif Taboo and "tabno" in LauraX.DailyActions:
            ch_l "I said not in public!"
        elif not LauraX.Foot:
            $ LauraX.FaceChange("bemused")
            ch_l "Eh, [LauraX.Petname]. . ."
        else:
            $ LauraX.FaceChange("bemused")
            ch_l "Not now, ok?"
        menu:
            extend ""
            "Sorry, never mind." if "no foot" in LauraX.DailyActions:
                $ LauraX.FaceChange("bemused")
                ch_l "Sure, no problem."
                return
            "Maybe later?" if "no foot" not in LauraX.DailyActions:
                $ LauraX.FaceChange("sexy")
                ch_l ". . ."
                ch_l "Maybe."
                $ LauraX.Statup("Love", 80, 2)
                $ LauraX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ LauraX.RecentActions.append("tabno")
                    $ LauraX.DailyActions.append("tabno")
                $ LauraX.RecentActions.append("no foot")
                $ LauraX.DailyActions.append("no foot")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ LauraX.FaceChange("sexy")
                    $ LauraX.Statup("Obed", 90, 2)
                    $ LauraX.Statup("Obed", 50, 2)
                    $ LauraX.Statup("Inbt", 70, 3)
                    $ LauraX.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Sure, I guess.",
                        "OK.",
                        "Fine, lemme see it.",
                        "I guess I could. . .",
                        "Ok. . . [She gestures for you to come over].",
                        "Heh, ok, ok."])
                    ch_l "[Line]"
                    $ Line = 0
                    jump Laura_FJ_Prep
                else:
                    pass

            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck(LauraX, 400, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and LauraX.Forced):
                    $ LauraX.FaceChange("sad")
                    $ LauraX.Statup("Love", 70, -5, 1)
                    $ LauraX.Statup("Love", 200, -2)
                    ch_l "Fine."
                    $ LauraX.Statup("Obed", 50, 4)
                    $ LauraX.Statup("Inbt", 80, 1)
                    $ LauraX.Statup("Inbt", 60, 3)
                    $ LauraX.Forced = 1
                    jump Laura_FJ_Prep
                else:
                    $ LauraX.Statup("Love", 200, -15)
                    $ LauraX.RecentActions.append("angry")
                    $ LauraX.DailyActions.append("angry")

    #She refused all offers.
    $ LauraX.ArmPose = 1
    if "no foot" in LauraX.DailyActions:
        $ LauraX.FaceChange("angry", 1)
        ch_l "I'm not telling you again."
        $ LauraX.RecentActions.append("angry")
        $ LauraX.DailyActions.append("angry")
    elif LauraX.Forced:
        $ LauraX.FaceChange("angry", 1)
        ch_l "You understand that I have claws down there too. . ."
        $ LauraX.Statup("Lust", 200, 5)
        if LauraX.Love > 300:
                $ LauraX.Statup("Love", 70, -2)
        $ LauraX.Statup("Obed", 50, -2)
        $ LauraX.RecentActions.append("angry")
        $ LauraX.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ LauraX.FaceChange("angry", 1)
        $ LauraX.DailyActions.append("tabno")
        ch_l "This is too exposed."
        $ LauraX.Statup("Lust", 200, 5)
        $ LauraX.Statup("Obed", 50, -3)
    elif LauraX.Foot:
        $ LauraX.FaceChange("sad")
        ch_l "Not right now."
    else:
        $ LauraX.FaceChange("normal", 1)
        ch_l "I'd rather not."
    $ LauraX.RecentActions.append("no foot")
    $ LauraX.DailyActions.append("no foot")
    $ temp_modifier = 0
    return


label Laura_FJ_Prep:
    if Trigger2 == "foot":
        return

    if Taboo:
        $ LauraX.Inbt += int(Taboo/10)
        $ LauraX.Lust += int(Taboo/5)

    $ LauraX.FaceChange("sexy")
    if LauraX.Forced:
        $ LauraX.FaceChange("sad")
    elif not LauraX.Foot:
        $ LauraX.Brows = "confused"
        $ LauraX.Eyes = "sexy"
        $ LauraX.Mouth = "smile"

    call Seen_First_Peen(LauraX,Partner)

    if not LauraX.Foot:
        if LauraX.Forced:
            $ LauraX.Statup("Love", 90, -20)
            $ LauraX.Statup("Obed", 70, 25)
            $ LauraX.Statup("Inbt", 80, 30)
        else:
            $ LauraX.Statup("Love", 90, 5)
            $ LauraX.Statup("Obed", 70, 20)
            $ LauraX.Statup("Inbt", 80, 20)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ LauraX.DrainWord("tabno")
    $ LauraX.DrainWord("no foot")
    $ LauraX.RecentActions.append("foot")
    $ LauraX.DailyActions.append("foot")

label Laura_FJ_Cycle:
    while Round > 0:
        call Shift_Focus(LauraX)
        call Laura_Sex_Launch("foot")
        $ LauraX.LustFace()

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

                        "Turn her Around":
                                    $ LauraX.Pose = "doggy" if LauraX.Pose != "doggy" else "sex"
                                    "You turn her around. . ."
                                    jump Laura_FJ_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if LauraX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ LauraX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")

                                    "Shift primary action":
                                            if LauraX.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                    if LauraX.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Laura_FJ_After
                                                                        call Laura_Blowjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(LauraX,"tired")
                                                        "How about a handjob?":
                                                                    if LauraX.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Laura_FJ_After
                                                                        call Laura_Handjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(LauraX,"tired")

                                                        "How about a titjob?":
                                                                    if LauraX.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Laura_FJ_After
                                                                        call Laura_Titjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(LauraX,"tired")



                                                        "Never Mind":
                                                                jump Laura_FJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [LauraX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(LauraX)
                                            "Ask [LauraX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(LauraX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(LauraX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Laura_FJ_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Laura_FJ_Cycle
                                            "Never mind":
                                                        jump Laura_FJ_Cycle
                                    "undress [LauraX.Name]":
                                            call Girl_Undress(LauraX)
                                    "Clean up [LauraX.Name] (locked)" if not LauraX.Spunk:
                                            pass
                                    "Clean up [LauraX.Name]" if LauraX.Spunk:
                                            call Girl_Cleanup(LauraX,"ask")
                                    "Never mind":
                                            jump Laura_FJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Laura_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Laura_FJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Laura_Sex_Reset
                                    $ Line = 0
                                    jump Laura_FJ_After
        #End menu (if Line)

        call Shift_Focus(LauraX)
        call Sex_Dialog(LauraX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or LauraX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(LauraX)
                            if "angry" in LauraX.RecentActions:
                                call Laura_Sex_Reset
                                return
                            $ LauraX.Statup("Lust", 200, 5)
                            if 100 > LauraX.Lust >= 70 and LauraX.OCount < 2:
                                $ LauraX.RecentActions.append("unsatisfied")
                                $ LauraX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Laura_FJ_After
                            $ Line = "came"

                    if LauraX.Lust >= 100:
                            #If Laura can cum
                            call Girl_Cumming(LauraX)
                            if Situation == "shift" or "angry" in LauraX.RecentActions:
                                jump Laura_FJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in LauraX.RecentActions:#And Laura is unsatisfied,
                                "[LauraX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Laura_FJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Cnt == 20:
                    $ LauraX.Brows = "angry"
                    menu:
                        ch_l "Hmm, this is getting a bit boring."
                        "How about a BJ?" if LauraX.Action and MultiAction:
                                $ Situation = "shift"
                                call Laura_FJ_After
                                call Laura_Blowjob
                        "How about a Handy?" if LauraX.Action and MultiAction:
                                $ Situation = "shift"
                                call Laura_FJ_After
                                call Laura_Handjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump Laura_FJ_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Laura_Sex_Reset
                                $ Situation = "shift"
                                jump Laura_FJ_After
                        "No, get back down there.":
                                if ApprovalCheck(LauraX, 1200) or ApprovalCheck(LauraX, 500, "O"):
                                    $ LauraX.Statup("Love", 200, -5)
                                    $ LauraX.Statup("Obed", 50, 3)
                                    $ LauraX.Statup("Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    $ LauraX.FaceChange("angry", 1)
                                    "She scowls at you and pulls back."
                                    ch_l "Not interested."
                                    $ LauraX.Statup("Love", 50, -3, 1)
                                    $ LauraX.Statup("Love", 80, -4, 1)
                                    $ LauraX.Statup("Obed", 30, -1, 1)
                                    $ LauraX.Statup("Obed", 50, -1, 1)
                                    $ LauraX.RecentActions.append("angry")
                                    $ LauraX.DailyActions.append("angry")
                                    jump Laura_FJ_After
        elif Cnt == 10 and LauraX.SEXP <= 100 and not ApprovalCheck(LauraX, 1200, "LO"):
                    $ LauraX.Brows = "confused"
                    ch_l "Ok, seriously, let's try something different."
        #End Count check

        call Escalation(LauraX) #sees if she wants to escalate things

        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [LauraX.Petname]."

    #Round = 0 loop breaks
    $ LauraX.FaceChange("bemused", 0)
    $ Line = 0
    ch_l "Ok, [LauraX.Petname], breaktime."

label Laura_FJ_After:
    $ LauraX.FaceChange("sexy")

    $ LauraX.Foot += 1
    $ LauraX.Action -=1
    $ LauraX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ LauraX.Addictionrate += 1
    $ LauraX.Statup("Lust", 90, 5)

    call Partner_Like(LauraX,1)

    if "Laurapedi" in Achievements:
            pass
    elif LauraX.Foot >= 10:
            $ LauraX.FaceChange("smile", 1)
            ch_l "I think I'm finally back into practice on this."
            $ Achievements.append("Laurapedi")
            $ LauraX.SEXP += 5
    elif LauraX.Foot == 1:
            $ LauraX.SEXP += 10
            if LauraX.Love >= 500:
                $ LauraX.Mouth = "smile"
                ch_l "Did you like that? . ."
            elif Player.Focus <= 20:
                $ LauraX.Mouth = "sad"
                ch_l "Did that do it for you?"
    elif LauraX.Foot == 5:
                ch_l "I'm getting used to this. . ."

    $ temp_modifier = 0
    if Situation == "shift":
        ch_l "Ok, so what did you have in mind?"
    else:
        call Laura_Sex_Reset
    call Checkout
    return

## end LauraX.Footjob //////////////////////////////////////////////////////////////////////
