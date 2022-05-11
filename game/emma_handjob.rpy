## EmmaX.Handjob //////////////////////////////////////////////////////////////////////
label Emma_Handjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(EmmaX)
    if EmmaX.Hand >= 7: # She loves it
        $ temp_modifier += 10
    elif EmmaX.Hand >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif EmmaX.Hand: #You've done it before
        $ temp_modifier += 3

    if EmmaX.Addict >= 75 and EmmaX.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 15
    if EmmaX.Addict >= 75:
        $ temp_modifier += 5

    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in EmmaX.Traits:
        $ temp_modifier += (3*Taboo)
    if EmmaX in Player.Harem or "sex friend" in EmmaX.Petnames:
        $ temp_modifier += 10
    elif "ex" in EmmaX.Traits:
        $ temp_modifier -= 40
    if EmmaX.ForcedCount and not EmmaX.Forced:
        $ temp_modifier -= 5 * EmmaX.ForcedCount

    if Taboo and "tabno" in EmmaX.DailyActions:
        $ temp_modifier -= 10

    if "no hand" in EmmaX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no hand" in EmmaX.RecentActions else 0

    $ Approval = ApprovalCheck(EmmaX, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if not EmmaX.Hand and "no hand" not in EmmaX.RecentActions:
        $ EmmaX.FaceChange("sly", 2)
        ch_e "You'd like me to take care of that for you?"

    if not EmmaX.Hand and Approval:                                                 #First time dialog
        if EmmaX.Forced:
            $ EmmaX.FaceChange("sad",1)
            $ EmmaX.Statup("Love", 70, -3, 1)
            $ EmmaX.Statup("Love", 20, -2, 1)
        elif EmmaX.Love >= (EmmaX.Obed + EmmaX.Inbt):
            $ EmmaX.FaceChange("sexy",1)
            $ EmmaX.Brows = "sad"
            $ EmmaX.Mouth = "smile"
            ch_e "I suppose you've earned something. . ."
        elif EmmaX.Obed >= EmmaX.Inbt:
            $ EmmaX.FaceChange("normal",1)
            ch_e "If that's what you'd like, [EmmaX.Petname]. . ."
        elif EmmaX.Addict >= 50:
            $ EmmaX.FaceChange("manic", 1)
            ch_e "Mmmmmmmm. . ."
        else: # Uninhibited
            $ EmmaX.FaceChange("lipbite",1,Eyes="side")
            ch_e "I suppose. . ."

    elif Approval:                                                                       #Second time+ dialog
        if EmmaX.Forced:
            $ EmmaX.FaceChange("sad")
            $ EmmaX.Statup("Love", 70, -3, 1)
            $ EmmaX.Statup("Love", 20, -2, 1)
            ch_e "No more than that?"
        elif not Taboo and "tabno" in EmmaX.DailyActions:
            ch_e "Here, hmm?. . ."
        elif "hand" in EmmaX.RecentActions:
            $ EmmaX.FaceChange("sexy", 1)
            ch_e "I will need to grade papers later, you know. . ."
            jump Emma_HJ_Prep
        elif "hand" in EmmaX.DailyActions:
            $ EmmaX.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Another?",
                "You're going to wear out my arm.",
                "Didn't get enough earlier?",
                "My hand's a bit sore from earlier.",
                "My hand's rather sore from before."])
            ch_e "[Line]"
        elif EmmaX.Hand < 3:
            $ EmmaX.FaceChange("sly", 1)
            ch_e "Enjoyed last time?. . ."
        else:
            $ EmmaX.FaceChange("sexy", 1)
            $ EmmaX.ArmPose = 2
            $ Line = renpy.random.choice(["You want more?",
                "So you'd like another?",
                "More of this? [fist pumping hand gestures]",
                "Oh, did you want some attention?"])
            ch_e "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if EmmaX.Forced:
            $ EmmaX.FaceChange("sad")
            $ EmmaX.Statup("Obed", 90, 1)
            $ EmmaX.Statup("Inbt", 60, 1)
            ch_e "Very well."
        elif "no hand" in EmmaX.DailyActions:
            ch_e "Oh, fine!"
        else:
            $ EmmaX.FaceChange("sexy", 1)
            $ EmmaX.Statup("Love", 90, 1)
            $ EmmaX.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Oh, I suppose.",
                "I'll do it.",
                "Well, give it here.",
                "I suppose I could. . .",
                "Fine. . . [She gestures for you to come over].",
                "Ok, ok."])
            ch_e "[Line]"
            $ Line = 0
        $ EmmaX.Statup("Obed", 20, 1)
        $ EmmaX.Statup("Obed", 60, 1)
        $ EmmaX.Statup("Inbt", 70, 2)
        jump Emma_HJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ EmmaX.FaceChange("angry")
        if "no hand" in EmmaX.RecentActions:
            ch_e "You need to learn to take\"no\" for an answer, [EmmaX.Petname]."
        elif "no hand" in EmmaX.DailyActions:
            ch_e "I told you \"no,\" [EmmaX.Petname]."
        elif Taboo and "tabno" in EmmaX.DailyActions:
            ch_e "I told you, this is too public!"
        elif not EmmaX.Hand:
            $ EmmaX.FaceChange("bemused")
            ch_e "Are you sure though, [EmmaX.Petname]?. . ."
        else:
            $ EmmaX.FaceChange("bemused")
            ch_e "I'd rather not right now though."
        menu:
            extend ""
            "Sorry, never mind." if "no hand" in EmmaX.DailyActions:
                $ EmmaX.FaceChange("bemused")
                ch_e "Quite alright."
                return
            "Maybe later?" if "no hand" not in EmmaX.DailyActions:
                $ EmmaX.FaceChange("sexy")
                ch_e ". . ."
                ch_e "I couldn't rule it out. . ."
                $ EmmaX.Statup("Love", 80, 2)
                $ EmmaX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ EmmaX.RecentActions.append("tabno")
                    $ EmmaX.DailyActions.append("tabno")
                $ EmmaX.RecentActions.append("no hand")
                $ EmmaX.DailyActions.append("no hand")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ EmmaX.FaceChange("sexy")
                    $ EmmaX.Statup("Obed", 90, 2)
                    $ EmmaX.Statup("Obed", 50, 2)
                    $ EmmaX.Statup("Inbt", 70, 3)
                    $ EmmaX.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Oh, I suppose.",
                        "I'll do it.",
                        "Well, give it here.",
                        "I suppose I could. . .",
                        "Fine. . . [She gestures for you to come over].",
                        "Ok, ok."])
                    ch_e "[Line]"
                    $ Line = 0
                    jump Emma_HJ_Prep

            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck(EmmaX, 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and EmmaX.Forced):
                    $ EmmaX.FaceChange("angry")
                    $ EmmaX.Statup("Love", 70, -5, 1)
                    $ EmmaX.Statup("Love", 200, -2)
                    ch_e "Hm. Alright, but don't push your luck, [EmmaX.Petname]."
                    $ EmmaX.Statup("Obed", 50, 4)
                    $ EmmaX.Statup("Inbt", 80, 1)
                    $ EmmaX.Statup("Inbt", 60, 3)
                    $ EmmaX.Forced = 1
                    jump Emma_HJ_Prep
                else:
                    $ EmmaX.Statup("Love", 200, -15)
                    $ EmmaX.RecentActions.append("angry")
                    $ EmmaX.DailyActions.append("angry")

    #She refused all offers.
    $ EmmaX.ArmPose = 1
    if "no hand" in EmmaX.DailyActions:
        $ EmmaX.FaceChange("angry", 1)
        ch_e "Don't make me repeat myself."
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")
    elif EmmaX.Forced:
        $ EmmaX.FaceChange("angry", 1)
        ch_e "Even that is asking too much."
        $ EmmaX.Statup("Lust", 200, 5)
        if EmmaX.Love > 300:
                $ EmmaX.Statup("Love", 70, -2)
        $ EmmaX.Statup("Obed", 50, -2)
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ EmmaX.FaceChange("angry", 1)
        $ EmmaX.DailyActions.append("tabno")
        ch_e "I couldn't possibly do that. . . here!"
        $ EmmaX.Statup("Lust", 200, 5)
        $ EmmaX.Statup("Obed", 50, -3)
    elif EmmaX.Hand:
        $ EmmaX.FaceChange("sad")
        ch_e "I'd really rather not. . ."
    else:
        $ EmmaX.FaceChange("normal", 1)
        ch_e "No, I don't think so, [EmmaX.Petname]."
    $ EmmaX.RecentActions.append("no hand")
    $ EmmaX.DailyActions.append("no hand")
    $ temp_modifier = 0
    return


label Emma_HJ_Prep:
    if Trigger2 == "hand":
        return

    if Taboo:
        $ EmmaX.Inbt += int(Taboo/10)
        $ EmmaX.Lust += int(Taboo/5)

    $ EmmaX.FaceChange("sexy")
    if EmmaX.Forced:
        $ EmmaX.FaceChange("sad")
    elif not EmmaX.Hand:
        $ EmmaX.Brows = "confused"
        $ EmmaX.Eyes = "sexy"
        $ EmmaX.Mouth = "smile"

    call Seen_First_Peen(EmmaX,Partner,React=Situation)
    call Emma_HJ_Launch("L")

    if Situation == EmmaX:
            #Emma auto-starts
            $ Situation = 0
            if Trigger2 == "jackin":
                "[EmmaX.Name] brushes your hand aside and starts stroking your cock."
            else:
                "[EmmaX.Name] draws her fingers across your cock, and begins to stroke it."
            menu:
                "What do you do?"
                "Nothing.":
                    $ EmmaX.Statup("Inbt", 70, 3)
                    $ EmmaX.Statup("Inbt", 30, 2)
                    "[EmmaX.Name] continues her actions."
                "Praise her.":
                    $ EmmaX.FaceChange("sexy", 1)
                    $ EmmaX.Statup("Inbt", 70, 3)
                    ch_p "Oooh, that's good, [EmmaX.Pet]."
                    $ EmmaX.NameCheck() #checks reaction to petname
                    "[EmmaX.Name] continues her actions."
                    $ EmmaX.Statup("Love", 80, 1)
                    $ EmmaX.Statup("Obed", 90, 1)
                    $ EmmaX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ EmmaX.FaceChange("surprised")
                    $ EmmaX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [EmmaX.Pet]."
                    $ EmmaX.NameCheck() #checks reaction to petname
                    "[EmmaX.Name] puts it down."
                    $ EmmaX.Statup("Obed", 90, 1)
                    $ EmmaX.Statup("Obed", 50, 1)
                    $ EmmaX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ EmmaX.AddWord(1,"refused","refused")
                    return

    if not EmmaX.Hand:
        if EmmaX.Forced:
            $ EmmaX.Statup("Love", 90, -20)
            $ EmmaX.Statup("Obed", 70, 25)
            $ EmmaX.Statup("Inbt", 80, 30)
        else:
            $ EmmaX.Statup("Love", 90, 5)
            $ EmmaX.Statup("Obed", 70, 20)
            $ EmmaX.Statup("Inbt", 80, 20)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ EmmaX.DrainWord("tabno")
    $ EmmaX.DrainWord("no hand")
    $ EmmaX.RecentActions.append("hand")
    $ EmmaX.DailyActions.append("hand")

label Emma_HJ_Cycle:
    while Round > 0:
        call Shift_Focus(EmmaX)
        call Emma_HJ_Launch
        $ EmmaX.LustFace()

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
                                            if EmmaX.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ EmmaX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(EmmaX,"tired")

                                    "Shift primary action":
                                            if EmmaX.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                    if EmmaX.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Emma_HJ_After
                                                                        call Emma_Blowjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(EmmaX,"tired")

                                                        "How about a titjob?":
                                                                    if EmmaX.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Emma_HJ_After
                                                                        call Emma_Titjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(EmmaX,"tired")
                                                        "Never Mind":
                                                                jump Emma_HJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(EmmaX,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(EmmaX)
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                call Three_Change(EmmaX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(EmmaX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Emma_HJ_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_HJ_Cycle
                                            "Never mind":
                                                        jump Emma_HJ_Cycle
                                    "Undress [EmmaX.Name]":
                                            call Girl_Undress(EmmaX)
                                    "Clean up [EmmaX.Name] (locked)" if not EmmaX.Spunk:
                                            pass
                                    "Clean up [EmmaX.Name]" if EmmaX.Spunk:
                                            call Girl_Cleanup(EmmaX,"ask")
                                    "Never mind":
                                            jump Emma_HJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Emma_HJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Emma_HJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Emma_HJ_Reset
                                    $ Line = 0
                                    jump Emma_HJ_After
        #End menu (if Line)

        call Shift_Focus(EmmaX)
        call Sex_Dialog(EmmaX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or EmmaX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(EmmaX)
                            if "angry" in EmmaX.RecentActions:
                                call Emma_HJ_Reset
                                return
                            $ EmmaX.Statup("Lust", 200, 5)
                            if 100 > EmmaX.Lust >= 70 and EmmaX.OCount < 2 and EmmaX.SEXP >= 20:
                                $ EmmaX.RecentActions.append("unsatisfied")
                                $ EmmaX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Emma_HJ_After
                            $ Line = "came"

                    if EmmaX.Lust >= 100:
                            #If [EmmaX.Name] can cum
                            call Girl_Cumming(EmmaX)
                            if Situation == "shift" or "angry" in EmmaX.RecentActions:
                                jump Emma_HJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in EmmaX.RecentActions:#And [EmmaX.Name] is unsatisfied,
                                    "[EmmaX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Emma_HJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Cnt == 20:
                    $ EmmaX.Brows = "angry"
                    ch_e "Hmm, I'm getting a bit of a cramp here."
                    menu:
                        ch_e "Mind if we take a break?"
                        "How about a BJ?" if EmmaX.Action and MultiAction:
                                $ Situation = "shift"
                                call Emma_HJ_After
                                call Emma_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump Emma_HJ_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Emma_HJ_Reset
                                $ Situation = "shift"
                                jump Emma_HJ_After
                        "No, get back down there.":
                                if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):
                                    $ EmmaX.Statup("Love", 200, -5)
                                    $ EmmaX.Statup("Obed", 50, 3)
                                    $ EmmaX.Statup("Obed", 80, 2)
                                    "She scowls but gets back to work."
                                else:
                                    $ EmmaX.FaceChange("angry", 1)
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_e "You know, I do have better things to do with my time than this."
                                    $ EmmaX.Statup("Love", 50, -3, 1)
                                    $ EmmaX.Statup("Love", 80, -4, 1)
                                    $ EmmaX.Statup("Obed", 30, -1, 1)
                                    $ EmmaX.Statup("Obed", 50, -1, 1)
                                    $ EmmaX.RecentActions.append("angry")
                                    $ EmmaX.DailyActions.append("angry")
                                    jump Emma_HJ_After
        elif Cnt == 10 and EmmaX.SEXP <= 100 and not ApprovalCheck(EmmaX, 1200, "LO"):
                    $ EmmaX.Brows = "confused"
                    ch_e "Are you certain you didn't have anything else in mind?"
        #End Count check

        call Escalation(EmmaX) #sees if she wants to escalate things

        if Round == 10:
            ch_e "It's about time for a break."
        elif Round == 5:
            ch_e "Ok, that's enough, for now. . ."

    #Round = 0 loop breaks
    $ EmmaX.FaceChange("bemused", 0)
    $ Line = 0
    ch_e "Ok, seriously, I'm putting it down for a minute."

label Emma_HJ_After:
    $ EmmaX.FaceChange("sexy")

    $ EmmaX.Hand += 1
    $ EmmaX.Action -=1
    $ EmmaX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ EmmaX.Addictionrate += 1
    $ EmmaX.Statup("Lust", 90, 5)

    call Partner_Like(EmmaX,1)

    if "Emma Handi-Queen" in Achievements:
            pass
    elif EmmaX.Hand >= 10:
            $ EmmaX.FaceChange("smile", 1)
            ch_e "I've apparently become the \"queen\" of handjobs as well."
            $ Achievements.append("Emma Handi-Queen")
            $EmmaX.SEXP += 5
    elif EmmaX.Hand == 1:
            $EmmaX.SEXP += 10
            if not EmmaX.Forced:
                $ EmmaX.Mouth = "smile"
                ch_e "What a lovely experience. . ."
            elif Player.Focus <= 20:
                $ EmmaX.Mouth = "sad"
                ch_e "Was that sufficient?"
    elif EmmaX.Hand == 5:
                ch_e "Please do call again. . ."

    $ temp_modifier = 0
    if Situation == "shift":
        ch_e "Very well, what did you want to do?"
    else:
        call Emma_HJ_Reset
    call Checkout
    return

## end EmmaX.Handjob //////////////////////////////////////////////////////////////////////




## EmmaX.Titjob //////////////////////////////////////////////////////////////////////
label Emma_Titjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(EmmaX)
    if EmmaX.Tit >= 7: # She loves it
        $ temp_modifier += 10
    elif EmmaX.Tit >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif EmmaX.Tit: #You've done it before
        $ temp_modifier += 5

    if EmmaX.Addict >= 75 and EmmaX.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 15
    elif EmmaX.Addict >= 75:
        $ temp_modifier += 5

    if EmmaX.SeenChest and ApprovalCheck(EmmaX, 500): # You've seen her tits.
        $ temp_modifier += 10
    if not EmmaX.Chest and not EmmaX.Over: #She's already topless
        $ temp_modifier += 10
    if EmmaX.Lust > 75: #She's really horny
        $ temp_modifier += 10
    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in EmmaX.Traits:
        $ temp_modifier += (5*Taboo)
    if EmmaX in Player.Harem or "sex friend" in EmmaX.Petnames:
        $ temp_modifier += 10
    elif "ex" in EmmaX.Traits:
        $ temp_modifier -= 30
    if EmmaX.ForcedCount and not EmmaX.Forced:
        $ temp_modifier -= 5 * EmmaX.ForcedCount

    if Taboo and "tabno" in EmmaX.DailyActions:
        $ temp_modifier -= 10

    if "no titjob" in EmmaX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no titjob" in EmmaX.RecentActions else 0

    $ Approval = ApprovalCheck(EmmaX, 1200, TabM = 5) # 120, 135, 150, Taboo -200(320)

    if not EmmaX.Tit and "no titjob" not in EmmaX.RecentActions:
        $ EmmaX.FaceChange("surprised", 1)
        $ EmmaX.Mouth = "kiss"
        ch_e "Hmm, are you sure you can handle that, [EmmaX.Petname]?"

    if not EmmaX.Tit and Approval:
        #First time dialog
        if EmmaX.Forced:
            $ EmmaX.FaceChange("sad")
            $ EmmaX.Statup("Love", 70, -3, 1)
            $ EmmaX.Statup("Love", 20, -2, 1)
        elif EmmaX.Love >= (EmmaX.Obed + EmmaX.Inbt):
            $ EmmaX.FaceChange("sexy")
            $ EmmaX.Brows = "sad"
            $ EmmaX.Mouth = "smile"
            ch_e "I suppose you've earned something special. . ."
        elif EmmaX.Obed >= EmmaX.Inbt:
            $ EmmaX.FaceChange("normal")
            ch_e "If that's what you want. . ."
        elif EmmaX.Addict >= 50:
            $ EmmaX.FaceChange("manic", 1)
            ch_e "Hmmmm. . . ."
        else: # Uninhibited
            $ EmmaX.FaceChange("sad")
            $ EmmaX.Mouth = "smile"
            ch_e "Hmm, I was wondering when you'd ask. . ."

    elif Approval:
        #Second time+ dialog
        if EmmaX.Forced:
            $ EmmaX.FaceChange("sad")
            $ EmmaX.Statup("Love", 70, -3, 1)
            $ EmmaX.Statup("Love", 20, -2, 1)
            ch_e "You aren't getting used to this service, are you?"
        elif not Taboo and "tabno" in EmmaX.DailyActions:
            ch_e "I suppose this is secluded enough. . ."
        elif "titjob" in EmmaX.RecentActions:
            $ EmmaX.FaceChange("sexy", 1)
            ch_e "Oh! Back for more?"
            jump Emma_TJ_Prep
        elif "titjob" in EmmaX.DailyActions:
            $ EmmaX.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",
                "You're going to wear them out.",
                "Didn't get enough earlier?",
                "I'm still a bit sore from earlier."])
            ch_e "[Line]"
        elif EmmaX.Tit < 3:
            $ EmmaX.FaceChange("sly", 1)
            ch_e "Hmm, another titjob?"
        else:
            $ EmmaX.FaceChange("sexy", 1)
            $ EmmaX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of these? [jiggles her tits]",
                "So you'd like another titjob?",
                "A little. . . [bounces tits]?",
                "A little warm embrace?"])
            ch_e "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if EmmaX.Forced:
            $ EmmaX.FaceChange("sad")
            $ EmmaX.Statup("Obed", 90, 1)
            $ EmmaX.Statup("Inbt", 60, 1)
            ch_e "I suppose there are worst ways to get you off. . ."
        elif "no titjob" in EmmaX.DailyActions:
            ch_e "Oh, very well then. . ."
        else:
            $ EmmaX.FaceChange("sexy", 1)
            $ EmmaX.Statup("Love", 90, 1)
            $ EmmaX.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, come over here.",
                "Oh, very well.",
                "Mmmmm.",
                "Fine, whip it out.",
                "Fine. . . [She drools a bit into her cleavage].",
                "Oh, all right."])
            ch_e "[Line]"
            $ Line = 0
        $ EmmaX.Statup("Obed", 20, 1)
        $ EmmaX.Statup("Obed", 70, 1)
        $ EmmaX.Statup("Inbt", 80, 2)
        jump Emma_TJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ EmmaX.FaceChange("angry")
        if "no titjob" in EmmaX.RecentActions:
            ch_e "I {i}just{/i} refused, [EmmaX.Petname]."
        elif Taboo and "tabno" in EmmaX.DailyActions and "no titjob" in EmmaX.DailyActions:
            ch_e "This is not an appropriate location for that. !"
        elif "no titjob" in EmmaX.DailyActions:
            ch_e "I already refused, [EmmaX.Petname]."
        elif Taboo and "tabno" in EmmaX.DailyActions:
            ch_e "This is not an appropriate place for that."
        else:
            $ EmmaX.FaceChange("bemused")
            ch_e "Perhaps later, [EmmaX.Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no titjob" in EmmaX.DailyActions:
                $ EmmaX.FaceChange("bemused")
                ch_e "That's all right, [EmmaX.Petname]."
                return
            "Maybe later?" if "no titjob" not in EmmaX.DailyActions:
                $ EmmaX.FaceChange("sexy")
                ch_e "Perhaps."
                $ EmmaX.Statup("Love", 80, 2)
                $ EmmaX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ EmmaX.RecentActions.append("tabno")
                    $ EmmaX.DailyActions.append("tabno")
                $ EmmaX.RecentActions.append("no titjob")
                $ EmmaX.DailyActions.append("no titjob")
                return
            "I think this could be fun for both of us. . .":
                if Approval:
                    $ EmmaX.FaceChange("sexy")
                    $ EmmaX.Statup("Obed", 80, 2)
                    $ EmmaX.Statup("Obed", 40, 2)
                    $ EmmaX.Statup("Inbt", 70, 3)
                    $ EmmaX.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Well, sure, come over here.",
                            "Oh, very well.",
                            "Mmmmm.",
                            "Fine, whip it out.",
                            "Fine. . . [She drools a bit into her cleavage].",
                            "Oh, all right."])
                    ch_e "[Line]"
                    $ Line = 0
                    jump Emma_TJ_Prep
                else:
                    $ Approval = ApprovalCheck(EmmaX, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)             Handy instead?
                    if Approval >= 2:
                        $ EmmaX.Statup("Inbt", 80, 1)
                        $ EmmaX.Statup("Inbt", 60, 3)
                        $ EmmaX.FaceChange("confused", 1)
                        if EmmaX.Blow:
                            ch_e "You seemed to enjoy blowjobs, would that work instead?"
                        else:
                            ch_e "Would you perhaps prefer a blowjob?"
                        menu:
                            extend ""
                            "Ok, get down there.":
                                $ EmmaX.Statup("Love", 80, 2)
                                $ EmmaX.Statup("Inbt", 60, 1)
                                $ EmmaX.Statup("Obed", 50, 1)
                                jump Emma_BJ_Prep
                            "Nah, it's all about dem titties.":
                                $ Line = "no BJ"
                    if Approval:
                        $ EmmaX.Statup("Inbt", 80, 1)
                        $ EmmaX.Statup("Inbt", 60, 3)
                        $ EmmaX.FaceChange("confused", 1)
                        ch_e "Perhaps a handjob?"
                        menu:
                            ch_e "Perhaps a handjob?"
                            "Sure, that's fine.":
                                $ EmmaX.Statup("Love", 80, 2)
                                $ EmmaX.Statup("Inbt", 60, 1)
                                $ EmmaX.Statup("Obed", 50, 1)
                                jump Emma_HJ_Prep
                            "Seriously, titties." if Line == "no BJ":
                                $ Line = 0
                            "Nah, it's all about dem titties." if Line != "no BJ":
                                pass
                    $ EmmaX.Statup("Love", 200, -2)
                    ch_e "Well, that's too bad."
                    $ EmmaX.Statup("Obed", 70, 2)


            "Come on, let me fuck those titties, [EmmaX.Pet]":                                               # Pressured into it
                $ EmmaX.NameCheck() #checks reaction to petname
                $ Approval = ApprovalCheck(EmmaX, 700, "OI", TabM = 4) # 70, 85, 100, -160(230)
                if Approval > 1 or (Approval and EmmaX.Forced):
                    $ EmmaX.FaceChange("sad")
                    $ EmmaX.Statup("Love", 70, -5, 1)
                    $ EmmaX.Statup("Love", 200, -2)
                    ch_e "Oh, very well."
                    $ EmmaX.Statup("Obed", 50, 4)
                    $ EmmaX.Statup("Inbt", 80, 1)
                    $ EmmaX.Statup("Inbt", 60, 3)
                    $ EmmaX.Forced = 1
                    jump Emma_TJ_Prep
                else:
                    $ EmmaX.Statup("Love", 200, -15)
                    $ EmmaX.RecentActions.append("angry")
                    $ EmmaX.DailyActions.append("angry")

    #She refused all offers.
    if "no titjob" in EmmaX.DailyActions:
        $ EmmaX.FaceChange("angry", 1)
        ch_e "I've refused, end of story."
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")
    elif EmmaX.Forced:
        $ EmmaX.FaceChange("angry", 1)
        ch_e "I couldn't put you through that."
        $ EmmaX.Statup("Lust", 200, 5)
        if EmmaX.Love > 300:
                $ EmmaX.Statup("Love", 70, -2)
        $ EmmaX.Statup("Obed", 50, -2)
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ EmmaX.FaceChange("angry", 1)
        $ EmmaX.DailyActions.append("tabno")
        ch_e "Can you imagine the scandal? Here?"
        $ EmmaX.Statup("Lust", 200, 5)
        $ EmmaX.Statup("Obed", 50, -3)
    elif EmmaX.Tit:
        $ EmmaX.FaceChange("sad")
        ch_e "I'm afraid you'll just have to remember the last time."
    else:
        $ EmmaX.FaceChange("normal", 1)
        ch_e "How about let's not, [EmmaX.Petname]."
    $ EmmaX.RecentActions.append("no titjob")
    $ EmmaX.DailyActions.append("no titjob")
    $ temp_modifier = 0
    return

label Emma_TJ_Prep:

    if Taboo:
        $ EmmaX.Inbt += int(Taboo/10)
        $ EmmaX.Lust += int(Taboo/5)


    $ EmmaX.FaceChange("sexy")
    if EmmaX.Forced:
        $ EmmaX.FaceChange("sad")
    elif not EmmaX.Tit:
        $ EmmaX.Brows = "confused"
        $ EmmaX.Eyes = "sexy"
        $ EmmaX.Mouth = "smile"

    call Seen_First_Peen(EmmaX,Partner,React=Situation)
    call Emma_TJ_Launch("L")

    if Situation == EmmaX:
            #Emma auto-starts
            $ Situation = 0
            call Emma_TJ_Launch("L")
            "[EmmaX.Name] slides down and wraps her tits around your dick."
            menu:
                "What do you do?"
                "Nothing.":
                    $ EmmaX.Statup("Inbt", 80, 3)
                    $ EmmaX.Statup("Inbt", 40, 2)
                    "[EmmaX.Name] starts to slide them up and down."
                "Praise her.":
                    $ EmmaX.FaceChange("sexy", 1)
                    $ EmmaX.Statup("Inbt", 80, 3)
                    ch_p "Oh, that sounds like a good idea, [EmmaX.Pet]."
                    $ EmmaX.NameCheck() #checks reaction to petname
                    "[EmmaX.Name] continues her actions."
                    $ EmmaX.Statup("Love", 85, 1)
                    $ EmmaX.Statup("Obed", 90, 1)
                    $ EmmaX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ EmmaX.FaceChange("confused")
                    $ EmmaX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [EmmaX.Pet]."
                    $ EmmaX.NameCheck() #checks reaction to petname
                    "[EmmaX.Name] lets it drop out from between her breasts."
                    $ EmmaX.Statup("Obed", 90, 1)
                    $ EmmaX.Statup("Obed", 50, 3)
                    $ Player.RecentActions.append("nope")
                    $ EmmaX.AddWord(1,"refused","refused")
                    return
    if not EmmaX.Tit:
        if EmmaX.Forced:
            $ EmmaX.Statup("Love", 90, -25)
            $ EmmaX.Statup("Obed", 70, 30)
            $ EmmaX.Statup("Inbt", 80, 35)
        else:
            $ EmmaX.Statup("Love", 90, 5)
            $ EmmaX.Statup("Obed", 70, 25)
            $ EmmaX.Statup("Inbt", 80, 30)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ EmmaX.DrainWord("tabno")
    $ EmmaX.DrainWord("no titjob")
    $ EmmaX.RecentActions.append("titjob")
    $ EmmaX.DailyActions.append("titjob")


label Emma_TJ_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(EmmaX)
        call Emma_TJ_Launch
        $ EmmaX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass

                        "Start moving? . ." if Speed == 0:
                                    $ Speed = 1

                        "Speed up. . ." if  Speed == 1:
                                    $ Speed = 2
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 2:
                                    pass

                        "Stop moving" if Speed == 1 or Speed == 3:
                                    $ Speed = 0
                        "Slow Down. . ." if Speed == 2:
                                    $ Speed = 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:
                                    pass

                        "Lick it" if Speed != 3:
                                    $ Speed = 3
                        "Lick it (locked)" if Speed == 3:
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
                                            if EmmaX.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ EmmaX.Action -= 1
                                            else:
                                                ch_e "Actually, could we wrap this up soon?"

                                    "Shift primary action":
                                            if EmmaX.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                if EmmaX.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Emma_TJ_After
                                                                    call Emma_Blowjob
                                                                else:
                                                                    ch_e "Actually, could we wrap this up soon?"

                                                        "How about a handy?":
                                                                if EmmaX.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Emma_BJ_After
                                                                    call Emma_Handjob
                                                                else:
                                                                    ch_e "Actually, could we wrap this up soon?"
                                                        "Never Mind":
                                                                jump Emma_TJ_Cycle
                                            else:
                                                ch_e "Actually, could we wrap this up soon?"

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(EmmaX)
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(EmmaX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(EmmaX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Emma_TJ_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_TJ_Cycle
                                            "Never mind":
                                                        jump Emma_TJ_Cycle
                                    "Undress [EmmaX.Name]":
                                            call Girl_Undress(EmmaX)
                                    "Clean up [EmmaX.Name] (locked)" if not EmmaX.Spunk:
                                            pass
                                    "Clean up [EmmaX.Name]" if EmmaX.Spunk:
                                            call Girl_Cleanup(EmmaX,"ask")
                                    "Never mind":
                                            jump Emma_TJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Emma_TJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Emma_TJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Emma_TJ_Reset
                                    $ Line = 0
                                    jump Emma_TJ_After
        #End menu (if Line)

        call Shift_Focus(EmmaX)
        call Sex_Dialog(EmmaX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or EmmaX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(EmmaX)
                            if "angry" in EmmaX.RecentActions:
                                call Emma_TJ_Reset
                                return
                            $ EmmaX.Statup("Lust", 200, 5)
                            if 100 > EmmaX.Lust >= 70 and EmmaX.OCount < 2 and EmmaX.SEXP >= 20:
                                $ EmmaX.RecentActions.append("unsatisfied")
                                $ EmmaX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Emma_TJ_After
                            $ Line = "came"

                    if EmmaX.Lust >= 100:
                            #If [EmmaX.Name] can cum
                            call Girl_Cumming(EmmaX)
                            if Situation == "shift" or "angry" in EmmaX.RecentActions:
                                jump Emma_TJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in EmmaX.RecentActions:#And [EmmaX.Name] is unsatisfied,
                                "[EmmaX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Emma_TJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif Cnt == (5 + EmmaX.Tit):
                    $ EmmaX.Brows = "confused"
                    ch_e "Are you getting close here? I'm getting a bit sore."
        elif Cnt == (10 + EmmaX.Tit):
                    $ EmmaX.Brows = "angry"
                    menu:
                        ch_e "I'm getting a bit worn out, could we settle this some other way?"
                        "How about a BJ?" if EmmaX.Action and MultiAction:
                                $ Situation = "shift"
                                call Emma_TJ_After
                                call Emma_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                jump Emma_TJ_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Emma_TJ_Reset
                                $ Situation = "shift"
                                jump Emma_TJ_After
                        "No, get back down there.":
                                if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):
                                    $ EmmaX.Statup("Love", 200, -5)
                                    $ EmmaX.Statup("Obed", 50, 3)
                                    $ EmmaX.Statup("Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    $ EmmaX.FaceChange("angry", 1)
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_e "Then I suppose you can handle this yourself."
                                    $ EmmaX.Statup("Love", 50, -3, 1)
                                    $ EmmaX.Statup("Love", 80, -4, 1)
                                    $ EmmaX.Statup("Obed", 30, -1, 1)
                                    $ EmmaX.Statup("Obed", 50, -1, 1)
                                    $ EmmaX.RecentActions.append("angry")
                                    $ EmmaX.DailyActions.append("angry")
                                    jump Emma_TJ_After
        #End Count check

        call Escalation(EmmaX) #sees if she wants to escalate things

        if Round == 10:
            ch_e "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ EmmaX.FaceChange("bemused", 0)
    $ Line = 0
    ch_e "All right, [EmmaX.Petname], that's plenty for now."

label Emma_TJ_After:
    $ EmmaX.FaceChange("sexy")

    $ EmmaX.Tit += 1
    $ EmmaX.Action -=1
    $ EmmaX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ EmmaX.Addictionrate += 1

    if Partner == "Kitty":
        call Partner_Like(EmmaX,4,2)
    else:
        call Partner_Like(EmmaX,3)

    if EmmaX.Tit > 5:
            pass
    elif EmmaX.Tit == 1:
        $EmmaX.SEXP += 12
        if EmmaX.Love >= 500:
            $ EmmaX.Mouth = "smile"
            ch_e "Mmm, was that as good for you as it was for me?"
        elif Player.Focus <= 20:
            $ EmmaX.Mouth = "sad"
            ch_e "I hope that lived up to expectations."
    elif EmmaX.Tit == 5:
            ch_e "You certainly get a lot of milage out of these."


    $ temp_modifier = 0
    if Situation == "shift":
            ch_e "Mmm, so what else did you have in mind?"
    else:
            call Emma_TJ_Reset
    call Checkout
    return

## end EmmaX.Titjob //////////////////////////////////////////////////////////////////////


# EmmaX.Blowjob //////////////////////////////////////////////////////////////////////

label Emma_Blowjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(EmmaX)
    if EmmaX.Blow >= 7: # She loves it
        $ temp_modifier += 15
    elif EmmaX.Blow >= 3: #You've done it before several times
        $ temp_modifier += 10
    elif EmmaX.Blow: #You've done it before
        $ temp_modifier += 7

    if EmmaX.Addict >= 75 and EmmaX.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 25
    elif EmmaX.Addict >= 75: #She's really strung out
        $ temp_modifier += 15

    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in EmmaX.Traits:
        $ temp_modifier += (4*Taboo)
    if EmmaX in Player.Harem or "sex friend" in EmmaX.Petnames:
        $ temp_modifier += 10
    elif "ex" in EmmaX.Traits:
        $ temp_modifier -= 40
    if EmmaX.ForcedCount and not EmmaX.Forced:
        $ temp_modifier -= 5 * EmmaX.ForcedCount

    if Taboo and "tabno" in EmmaX.DailyActions:
        $ temp_modifier -= 10

    if "no blow" in EmmaX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no blow" in EmmaX.RecentActions else 0

    $ Approval = ApprovalCheck(EmmaX, 1300, TabM = 4) # 130, 145, 160, Taboo -160(290)

    if not EmmaX.Blow and "no blow" not in EmmaX.RecentActions:
        $ EmmaX.FaceChange("sly")
        ch_e "So you'd like me to suck you off?"

    if not EmmaX.Blow and Approval:                                                 #First time dialog
        if EmmaX.Forced:
            $ EmmaX.FaceChange("sad")
            $ EmmaX.Statup("Love", 70, -3, 1)
            $ EmmaX.Statup("Love", 20, -2, 1)
        elif EmmaX.Love >= (EmmaX.Obed + EmmaX.Inbt):
            $ EmmaX.FaceChange("sexy")
            $ EmmaX.Brows = "sad"
            $ EmmaX.Mouth = "smile"
            ch_e "I am curious if it tastes as good as it looks. . ."
        elif EmmaX.Obed >= EmmaX.Inbt:
            $ EmmaX.FaceChange("normal")
            ch_e "If that's what you want. . ."
        elif EmmaX.Addict >= 50:
            $ EmmaX.FaceChange("manic", 1)
            ch_e "I don't know if I could wait. . ."
        else: # Uninhibited
            $ EmmaX.FaceChange("sad")
            $ EmmaX.Mouth = "smile"
            ch_e "I suppose. . ."
    elif Approval:                                                                       #Second time+ dialog
        if EmmaX.Forced:
            $ EmmaX.FaceChange("sad")
            $ EmmaX.Statup("Love", 70, -3, 1)
            $ EmmaX.Statup("Love", 20, -2, 1)
            ch_e "Ugh, that again?"
        elif not Taboo and "tabno" in EmmaX.DailyActions:
            ch_e "Ok, I suppose this is secluded enough. . ."
        elif "blow" in EmmaX.RecentActions:
            $ EmmaX.FaceChange("sexy", 1)
            ch_e "Mmm, again? [[yawns]"
            jump Emma_BJ_Prep
        elif "blow" in EmmaX.DailyActions:
            $ EmmaX.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Back so soon?",
                "Let me get some saliva going.",
                "Didn't get enough earlier?",
                "My jaw's still sore from our prior engagement.",
                "My jaw's still a bit sore from earlier."])
            ch_e "[Line]"
        elif EmmaX.Blow < 3:
            $ EmmaX.FaceChange("sexy", 1)
            $ EmmaX.Brows = "confused"
            $ EmmaX.Mouth = "kiss"
            ch_e "Another blowjob?"
        else:
            $ EmmaX.FaceChange("sexy", 1)
            $ EmmaX.ArmPose = 2
            $ Line = renpy.random.choice(["You want me to [mimes blowing]?",
                "So you want another blowjob?",
                "You want me to suck you off?",
                "Are you asking if I'm hungry?"])
            ch_e "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if EmmaX.Forced:
            $ EmmaX.FaceChange("sad")
            $ EmmaX.Statup("Obed", 90, 1)
            $ EmmaX.Statup("Inbt", 60, 1)
            ch_e "Fine."
        elif "no blow" in EmmaX.DailyActions:
            ch_e "Fine, I suppose you've earned it. . ."
        else:
            $ EmmaX.FaceChange("sexy", 1)
            $ EmmaX.Statup("Love", 90, 1)
            $ EmmaX.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Well, ok.",
                "Well. . . ok.",
                "Mmmm.",
                "Sure, let me have it.",
                "Mmmm. . . [She licks her lips].",
                "Ok, fine."])
            ch_e "[Line]"
            $ Line = 0
        $ EmmaX.Statup("Obed", 20, 1)
        $ EmmaX.Statup("Obed", 70, 1)
        $ EmmaX.Statup("Inbt", 80, 2)
        jump Emma_BJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ EmmaX.FaceChange("angry")
        if "no blow" in EmmaX.RecentActions:
            ch_e "I believe I just told you, \"no.\""
        elif Taboo and "tabno" in EmmaX.DailyActions and "no blow" in EmmaX.DailyActions:
            ch_e "I told you, this is too public!"
        elif "no blow" in EmmaX.DailyActions:
            ch_e "I told you \"no,\" [EmmaX.Petname]."
        elif Taboo and "tabno" in EmmaX.DailyActions:
            ch_e "I told you this is too public!"
        elif not EmmaX.Blow:
            $ EmmaX.FaceChange("bemused")
            ch_e "I'm not sure you're up to my usual tastes, [EmmaX.Petname]. . ."
        else:
            $ EmmaX.FaceChange("bemused")
            ch_e "Perhaps later, [EmmaX.Petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no blow" in EmmaX.DailyActions:
                $ EmmaX.FaceChange("bemused")
                ch_e "No harm done, [EmmaX.Petname]."
                return
            "Maybe later?" if "no blow" not in EmmaX.DailyActions:
                $ EmmaX.FaceChange("sexy")
                ch_e "I wouldn't rule it out, [EmmaX.Petname]."
                $ EmmaX.Statup("Love", 80, 2)
                $ EmmaX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ EmmaX.RecentActions.append("tabno")
                    $ EmmaX.DailyActions.append("tabno")
                $ EmmaX.RecentActions.append("no blow")
                $ EmmaX.DailyActions.append("no blow")
                return
            "Come on, please?":
                if Approval:
                    $ EmmaX.FaceChange("sexy")
                    $ EmmaX.Statup("Obed", 90, 2)
                    $ EmmaX.Statup("Obed", 50, 2)
                    $ EmmaX.Statup("Inbt", 70, 3)
                    $ EmmaX.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Well, I suppose.",
                        "Well. . . ok.",
                        "I could perhaps give it a try.",
                        "I suppose I could. . .",
                        "Fine. . . [She licks her lips].",
                        "Hmph, ok, fine."])
                    ch_e "[Line]"
                    $ Line = 0
                    jump Emma_BJ_Prep
                else:
                    if ApprovalCheck(EmmaX, 1100, TabM = 3): # 110, 125, 140, Taboo -120(230)             Handy instead?
                        $ EmmaX.Statup("Inbt", 80, 1)
                        $ EmmaX.Statup("Inbt", 60, 3)
                        $ EmmaX.FaceChange("confused", 1)
                        $ EmmaX.ArmPose = 2
                        if EmmaX.Hand:
                            ch_e "I could just stroke you off, perhaps?"
                        else:
                            ch_e "Would my hand be an adequate substitute?"
                        menu:
                            extend ""
                            "Sure, that's fine.":
                                $ EmmaX.Statup("Love", 80, 2)
                                $ EmmaX.Statup("Inbt", 60, 1)
                                $ EmmaX.Statup("Obed", 50, 1)
                                jump Emma_HJ_Prep
                            "Nah, if it's not your mouth, forget it.":
                                $ EmmaX.Statup("Love", 200, -2)
                                $ EmmaX.ArmPose = 1
                                ch_e "Pitty."
                                $ EmmaX.Statup("Obed", 70, 2)


            "Suck it, [EmmaX.Pet]":                                               # Pressured into it
                $ EmmaX.NameCheck() #checks reaction to petname
                $ Approval = ApprovalCheck(EmmaX, 750, "OI", TabM = 3) # 75, 90, 105, -120(195)
                if Approval > 1 or (Approval and EmmaX.Forced):
                    $ EmmaX.FaceChange("sad")
                    $ EmmaX.Statup("Love", 70, -5, 1)
                    $ EmmaX.Statup("Love", 200, -2)
                    ch_e "Oh, fine. . ."
                    $ EmmaX.Statup("Obed", 50, 4)
                    $ EmmaX.Statup("Inbt", 80, 1)
                    $ EmmaX.Statup("Inbt", 60, 3)
                    $ EmmaX.Forced = 1
                    jump Emma_BJ_Prep
                else:
                    $ EmmaX.Statup("Love", 200, -15)
                    $ EmmaX.RecentActions.append("angry")
                    $ EmmaX.DailyActions.append("angry")

    #She refused all offers.
    if "no blow" in EmmaX.DailyActions:
        $ EmmaX.FaceChange("angry", 1)
        ch_e "Then I hope you can take care of yourself."
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")
    elif EmmaX.Forced:
        $ EmmaX.FaceChange("angry", 1)
        ch_e "You go too far!"
        $ EmmaX.Statup("Lust", 200, 5)
        if EmmaX.Love > 300:
                $ EmmaX.Statup("Love", 70, -2)
        $ EmmaX.Statup("Obed", 50, -2)
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")
        $ EmmaX.RecentActions.append("no blow")
        $ EmmaX.DailyActions.append("no blow")
        return
    elif Taboo:                             # she refuses and this is too public a place for her
        $ EmmaX.FaceChange("angry", 1)
        $ EmmaX.DailyActions.append("tabno")
        ch_e "This is way too exposed!"
        $ EmmaX.Statup("Lust", 200, 5)
        $ EmmaX.Statup("Obed", 50, -3)
        return
    elif EmmaX.Blow:
        $ EmmaX.FaceChange("sad")
        ch_e "I'm just not in the mood, [EmmaX.Petname]."
    else:
        $ EmmaX.FaceChange("normal", 1)
        ch_e "I don't think I will."
    $ EmmaX.RecentActions.append("no blow")
    $ EmmaX.DailyActions.append("no blow")
    $ temp_modifier = 0
    return


label Emma_BJ_Prep:
    if renpy.showing("Emma_HJ_Animation"):
        hide Emma_HJ_Animation with easeoutbottom
    if Taboo:
        $ EmmaX.Inbt += int(Taboo/10)
        $ EmmaX.Lust += int(Taboo/5)

    $ EmmaX.FaceChange("sexy")
    if EmmaX.Forced:
        $ EmmaX.FaceChange("sad")

    call Seen_First_Peen(EmmaX,Partner,React=Situation)
    call Emma_BJ_Launch("L")

    if Situation == EmmaX:
            #Emma auto-starts
            $ Situation = 0
            "[EmmaX.Name] slides down and places your cock against her lips."
            menu:
                "What do you do?"
                "Nothing.":
                    $ EmmaX.Statup("Inbt", 80, 3)
                    $ EmmaX.Statup("Inbt", 40, 2)
                    "[EmmaX.Name] continues licking at it."
                "Praise her.":
                    $ EmmaX.FaceChange("sexy", 1)
                    $ EmmaX.Statup("Inbt", 80, 3)
                    ch_p "Hmmm, keep doing that, [EmmaX.Pet]."
                    $ EmmaX.NameCheck() #checks reaction to petname
                    "[EmmaX.Name] continues her actions."
                    $ EmmaX.Statup("Love", 85, 1)
                    $ EmmaX.Statup("Obed", 90, 1)
                    $ EmmaX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ EmmaX.FaceChange("surprised")
                    $ EmmaX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [EmmaX.Pet]."
                    $ EmmaX.NameCheck() #checks reaction to petname
                    "[EmmaX.Name] puts it down."
                    $ EmmaX.Statup("Obed", 90, 1)
                    $ EmmaX.Statup("Obed", 50, 3)
                    $ Player.RecentActions.append("nope")
                    $ EmmaX.AddWord(1,"refused","refused")
                    return
    if not EmmaX.Blow:
        if EmmaX.Forced:
            $ EmmaX.Statup("Love", 90, -70)
            $ EmmaX.Statup("Obed", 70, 45)
            $ EmmaX.Statup("Inbt", 80, 60)
        else:
            $ EmmaX.Statup("Love", 90, 5)
            $ EmmaX.Statup("Obed", 70, 35)
            $ EmmaX.Statup("Inbt", 80, 40)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ EmmaX.DrainWord("tabno")
    $ EmmaX.DrainWord("no blow")
    $ EmmaX.RecentActions.append("blow")
    $ EmmaX.DailyActions.append("blow")

label Emma_BJ_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(EmmaX)
        call Emma_BJ_Launch
        $ EmmaX.LustFace()

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
                                if "pushed" not in EmmaX.RecentActions and EmmaX.Blow < 5:
                                    $ EmmaX.Statup("Love", 80, -(20-(2*EmmaX.Blow)))
                                    $ EmmaX.Statup("Obed", 80, (30-(3*EmmaX.Blow)))
                                    $ EmmaX.RecentActions.append("pushed")
                                if Trigger2 == "jackin" and Speed != 3:
                                    "She takes it to the root, and you move your hand out of the way."
                                $ Speed = 4
                        "Take it deeper. (locked)" if Speed == 4:
                                pass

                        "Set your own pace. . .":
                                "[EmmaX.Name] hums contentedly."
                                if "setpace" not in EmmaX.RecentActions:
                                    $ EmmaX.Statup("Love", 80, 2)
                                $ D20 = renpy.random.randint(1, 20)
                                if EmmaX.Blow < 5:
                                    $ D20 -= 10
                                elif EmmaX.Blow < 10:
                                    $ D20 -= 5

                                if D20 > 15:
                                    $ Speed = 4
                                    if "setpace" not in EmmaX.RecentActions:
                                        $ EmmaX.Statup("Inbt", 80, 3)
                                elif D20 > 10:
                                    $ Speed = 3
                                elif D20 > 5:
                                    $ Speed = 2
                                else:
                                    $ Speed = 1
                                $ EmmaX.RecentActions.append("setpace")

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
                                            if EmmaX.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ EmmaX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(EmmaX,"tired")

                                    "Shift primary action":
                                            if EmmaX.Action and MultiAction:
                                                    menu:
                                                        "How about a handy?":
                                                                if EmmaX.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Emma_BJ_After
                                                                    call Emma_Handjob
                                                                else:
                                                                    ch_e "I'm kinda tired, could we just wrap this up. . ."
                                                        "How about a titjob?":
                                                                if EmmaX.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Emma_BJ_After
                                                                    call Emma_Titjob
                                                                else:
                                                                    ch_e "I'm kinda tired, could we just wrap this up. . ."
                                                        "Never Mind":
                                                                jump Emma_BJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(EmmaX,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(EmmaX)
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(EmmaX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(EmmaX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Emma_BJ_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_BJ_Cycle
                                            "Never mind":
                                                        jump Emma_BJ_Cycle
                                    "Undress [EmmaX.Name]":
                                            call Girl_Undress(EmmaX)
                                    "Clean up [EmmaX.Name] (locked)" if not EmmaX.Spunk:
                                            pass
                                    "Clean up [EmmaX.Name]" if EmmaX.Spunk:
                                            call Girl_Cleanup(EmmaX,"ask")
                                    "Never mind":
                                            jump Emma_BJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Emma_BJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Emma_BJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Emma_BJ_Reset
                                    $ Line = 0
                                    jump Emma_BJ_After
        #End menu (if Line)

        call Shift_Focus(EmmaX)
        call Sex_Dialog(EmmaX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1
        if Speed:
            $ Player.Wet = 1 #wets penis
            $ Player.Spunk = 0 if Player.Spunk else Player.Spunk #cleans you off after one cycle

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or EmmaX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(EmmaX)
                            if "angry" in EmmaX.RecentActions:
                                call Emma_BJ_Reset
                                return
                            $ EmmaX.Statup("Lust", 200, 5)
                            if 100 > EmmaX.Lust >= 70 and EmmaX.OCount < 2 and EmmaX.SEXP >= 20:
                                $ EmmaX.RecentActions.append("unsatisfied")
                                $ EmmaX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Emma_BJ_After
                            $ Line = "came"

                    if EmmaX.Lust >= 100:
                            #If [EmmaX.Name] can cum
                            call Girl_Cumming(EmmaX)
                            if Situation == "shift" or "angry" in EmmaX.RecentActions:
                                jump Emma_BJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in EmmaX.RecentActions:#And [EmmaX.Name] is unsatisfied,
                                    "[EmmaX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Emma_BJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif Cnt == (15 + EmmaX.Blow):
                $ EmmaX.Brows = "angry"
                menu:
                    ch_e "I'm getting a bit worn out here, could we do something else?"
                    "How about a Handy?" if EmmaX.Action and MultiAction:
                            $ Situation = "shift"
                            call Emma_BJ_After
                            call Emma_Handjob
                            return
                    "Finish up." if Player.FocusX:
                            "You release your concentration. . ."
                            $ Player.FocusX = 0
                            $ Player.Focus += 15
                            $ Cnt += 1
                            "[Line]."
                            jump Emma_BJ_Cycle
                    "Let's try something else." if MultiAction:
                            $ Line = 0
                            call Emma_BJ_Reset
                            $ Situation = "shift"
                            jump Emma_BJ_After
                    "No, get back down there.":
                            if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):
                                $ EmmaX.Statup("Love", 200, -5)
                                $ EmmaX.Statup("Obed", 50, 3)
                                $ EmmaX.Statup("Obed", 80, 2)
                                "She scowls but gets back to work."
                            else:
                                $ EmmaX.FaceChange("angry", 1)
                                "She scowls at you, drops you cock and pulls back."
                                ch_e "Well then."
                                $ EmmaX.Statup("Love", 50, -3, 1)
                                $ EmmaX.Statup("Love", 80, -4, 1)
                                $ EmmaX.Statup("Obed", 30, -1, 1)
                                $ EmmaX.Statup("Obed", 50, -1, 1)
                                $ EmmaX.RecentActions.append("angry")
                                $ EmmaX.DailyActions.append("angry")
                                jump Emma_BJ_After
        elif Cnt == (10 + EmmaX.Blow) and EmmaX.SEXP <= 100 and not ApprovalCheck(EmmaX, 1200, "LO"):
                    $ EmmaX.Brows = "confused"
                    ch_e "Are you about done? I'm a little tired of this."
        #End Count check

        call Escalation(EmmaX) #sees if she wants to escalate things

        if Round == 10:
            ch_e "It's getting a bit late. . ."
        elif Round == 5:
            ch_e "Do you mind if we take a break?"

    #Round = 0 loop breaks
    $ EmmaX.FaceChange("bemused", 0)
    $ Line = 0
    ch_e "Ok, I need to rest my jaw for a minute. . ."

label Emma_BJ_After:
    $ EmmaX.FaceChange("sexy")

    $ EmmaX.Blow += 1
    $ EmmaX.Action -=1
    $ EmmaX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ EmmaX.Addictionrate += 1

    call Partner_Like(EmmaX,2)

    if "Emma Jobber" in Achievements:
        pass
    elif EmmaX.Blow >= 10:
        $ EmmaX.FaceChange("smile", 1)
        ch_e "You taste positively intoxicating, [EmmaX.Petname]."
        $ Achievements.append("Emma Jobber")
        $EmmaX.SEXP += 5
    elif Situation == "shift":
        pass
    elif EmmaX.Blow == 1:
            $EmmaX.SEXP += 15
            if EmmaX.Love >= 500:
                $ EmmaX.Mouth = "smile"
                ch_e "Hmm, better than I'd imagined. . ."
            elif Player.Focus <= 20:
                $ EmmaX.Mouth = "sad"
                ch_e "Was it all you dreamed of?"
    elif EmmaX.Blow == 5:
        ch_e "Best you've had, I'm sure."
        menu:
            "[[nod]":
                $ EmmaX.FaceChange("smile", 1)
                $ EmmaX.Statup("Love", 90, 10)
                $ EmmaX.Statup("Obed", 80, 5)
                $ EmmaX.Statup("Inbt", 90, 10)
            "[[shake head \"no\"]":
                if ApprovalCheck(EmmaX, 500, "O"):
                    $ EmmaX.FaceChange("sad", 2)
                    $ EmmaX.Statup("Love", 200, -5)
                else:
                    $ EmmaX.FaceChange("angry", 2)
                    $ EmmaX.Statup("Love", 200, -30)
                $ EmmaX.Statup("Obed", 80, 20)
                ch_e ". . ."
                $ EmmaX.FaceChange("sad", 1)

    $ temp_modifier = 0
    if Situation != "shift":
        call Emma_BJ_Reset
    call Checkout
    return



# end EmmaX.Blowjob                                 //////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy
label Emma_Dildo_Check:
    if "dildo" in Player.Inventory:
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in EmmaX.Inventory:
        "You ask [EmmaX.Name] to get out her favorite Dildo."
    else:
        "You don't have one of those on you."
        return 0
    return 1

label Emma_Dildo_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(EmmaX)
    call Emma_Dildo_Check
    if not _return:
        return

    if EmmaX.DildoP: #You've done it before
        $ temp_modifier += 15
    if EmmaX.PantsNum() >= 6: # she's got pants on.
        $ temp_modifier -= 20

    if EmmaX.Lust > 95:
        $ temp_modifier += 20
    elif EmmaX.Lust > 85: #She's really horny
        $ temp_modifier += 15

    if Situation == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in EmmaX.Traits:
        $ temp_modifier += (5*Taboo)
    if EmmaX in Player.Harem or "sex friend" in EmmaX.Petnames:
        $ temp_modifier += 10
    elif "ex" in EmmaX.Traits:
        $ temp_modifier -= 40
    if EmmaX.ForcedCount and not EmmaX.Forced:
        $ temp_modifier -= 5 * EmmaX.ForcedCount

    if Taboo and "tabno" in EmmaX.DailyActions:
        $ temp_modifier -= 10

    if "no dildo" in EmmaX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no dildo" in EmmaX.RecentActions else 0

    $ Approval = ApprovalCheck(EmmaX, 1250, TabM = 4) # 125, 140, 155, Taboo -160(335)

    if Situation == EmmaX:                                                                  #Emma auto-starts
                if Approval > 2:                                                      # fix, add emma auto stuff here
                    if EmmaX.PantsNum() == 5:
                        "[EmmaX.Name] grabs her dildo, hiking up her skirt as she does."
                        $ EmmaX.Upskirt = 1
                    elif EmmaX.PantsNum() > 6:
                        "[EmmaX.Name] grabs her dildo, pulling down her pants as she does."
                        $ EmmaX.Legs = 0
                    else:
                        "[EmmaX.Name] grabs her dildo, rubbing is suggestively against her crotch."
                    $ EmmaX.SeenPanties = 1
                    "She slides the tip along her pussy and seems to want you to insert it."
                    menu:
                        "What do you do?"
                        "Nothing.":
                            $ EmmaX.Statup("Inbt", 80, 3)
                            $ EmmaX.Statup("Inbt", 50, 2)
                            "[EmmaX.Name] slides it in."
                        "Go for it.":
                            $ EmmaX.FaceChange("sexy", 1)
                            $ EmmaX.Statup("Inbt", 80, 3)
                            ch_p "Oh yeah, [EmmaX.Pet], let's do this."
                            $ EmmaX.NameCheck() #checks reaction to petname
                            "You grab the dildo and slide it in."
                            $ EmmaX.Statup("Love", 85, 1)
                            $ EmmaX.Statup("Obed", 90, 1)
                            $ EmmaX.Statup("Obed", 50, 2)
                        "Ask her to stop.":
                            $ EmmaX.FaceChange("surprised")
                            $ EmmaX.Statup("Inbt", 70, 1)
                            ch_p "Let's not do that right now, [EmmaX.Pet]."
                            $ EmmaX.NameCheck() #checks reaction to petname
                            "[EmmaX.Name] sets the dildo down."
                            $ EmmaX.OutfitChange()
                            $ EmmaX.Statup("Obed", 90, 1)
                            $ EmmaX.Statup("Obed", 50, 1)
                            $ EmmaX.Statup("Obed", 30, 2)
                            return
                    jump Emma_DP_Prep
                else:
                    $ temp_modifier = 0                               # fix, add emma auto stuff here
                    $ Trigger2 = 0
                return

    if Situation == "auto":
                "You rub the dildo across her body, and along her moist slit."
                $ EmmaX.FaceChange("surprised", 1)

                if (EmmaX.DildoP and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
                    "[EmmaX.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                    $ EmmaX.FaceChange("sexy")
                    $ EmmaX.Statup("Obed", 70, 3)
                    $ EmmaX.Statup("Inbt", 50, 3)
                    $ EmmaX.Statup("Inbt", 70, 1)
                    ch_e "Hmm, [EmmaX.Petname], toys!"
                    jump Emma_DP_Prep
                else:                                                                                                            #she's questioning it
                    $ EmmaX.Brows = "angry"
                    menu:
                        ch_e "Excuse yourself, what are you planning to do with that?!"
                        "Sorry, sorry! Never mind.":
                            if Approval:
                                $ EmmaX.FaceChange("sexy", 1)
                                $ EmmaX.Statup("Obed", 70, 3)
                                $ EmmaX.Statup("Inbt", 50, 3)
                                $ EmmaX.Statup("Inbt", 70, 1)
                                ch_e "Well, now that you mention it. . ."
                                jump Emma_DP_Prep
                            "You pull back before you really get it in."
                            $ EmmaX.FaceChange("bemused", 1)
                            if EmmaX.DildoP:
                                ch_e "Well, [EmmaX.Petname], maybe warn me next time?"
                            else:
                                ch_e "Well, [EmmaX.Petname], that's a little much. . . for now . . ."
                        "Just playing with my favorite toys.":
                            $ EmmaX.Statup("Love", 80, -10, 1)
                            $ EmmaX.Statup("Love", 200, -10)
                            "You press it inside some more."
                            $ EmmaX.Statup("Obed", 70, 3)
                            $ EmmaX.Statup("Inbt", 50, 3)
                            if not ApprovalCheck(EmmaX, 700, "O", TabM=1): #Checks if Obed is 700+
                                $ EmmaX.FaceChange("angry")
                                "[EmmaX.Name] shoves you away and slaps you in the face."
                                ch_e "Ask nicely before trying anything like that!"
                                $ EmmaX.Statup("Love", 50, -10, 1)
                                $ EmmaX.Statup("Obed", 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                if renpy.showing("Emma_SexSprite"):
                                    call Emma_Sex_Reset
                                $ EmmaX.RecentActions.append("angry")
                                $ EmmaX.DailyActions.append("angry")
                            else:
                                $ EmmaX.FaceChange("sad")
                                "[EmmaX.Name] doesn't seem to be into this, you're lucky she's so obedient."
                                jump Emma_DP_Prep
                return
    #end Auto

    if not EmmaX.DildoP:
            #first time
            $ EmmaX.FaceChange("surprised", 1)
            $ EmmaX.Mouth = "kiss"
            ch_e "Hmmm, so you'd like to try out some toys?"
            if EmmaX.Forced:
                $ EmmaX.FaceChange("sad")
                ch_e "I suppose there are worst things you could ask for."

    if not EmmaX.DildoP and Approval:
            #First time dialog
            if EmmaX.Forced:
                $ EmmaX.FaceChange("sad")
                $ EmmaX.Statup("Love", 70, -3, 1)
                $ EmmaX.Statup("Love", 20, -2, 1)
            elif EmmaX.Love >= (EmmaX.Obed + EmmaX.Inbt):
                $ EmmaX.FaceChange("sexy")
                $ EmmaX.Brows = "sad"
                $ EmmaX.Mouth = "smile"
                ch_e "I've had a reasonable amount of experience with these, you know. . ."
            elif EmmaX.Obed >= EmmaX.Inbt:
                $ EmmaX.FaceChange("normal")
                ch_e "If that's what you want, [EmmaX.Petname]. . ."
            else: # Uninhibited
                $ EmmaX.FaceChange("sad")
                $ EmmaX.Mouth = "smile"
                ch_e "I guess it could be fun with a partner. . ."

    elif Approval:
            #Second time+ dialog
            if EmmaX.Forced:
                $ EmmaX.FaceChange("sad")
                $ EmmaX.Statup("Love", 70, -3, 1)
                $ EmmaX.Statup("Love", 20, -2, 1)
                ch_e "The toys again?"
            elif not Taboo and "tabno" in EmmaX.DailyActions:
                ch_e "Well, at least you got us some privacy this time. . ."
            elif "dildo pussy" in EmmaX.RecentActions:
                $ EmmaX.FaceChange("sexy", 1)
                ch_e "Mmm, again? Ok, let's get to it."
                jump Emma_DP_Prep
            elif "dildo pussy" in EmmaX.DailyActions:
                $ EmmaX.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Breaking out the toys again?",
                    "Didn't get enough earlier?",
                    "You're going to wear me out."])
                ch_e "[Line]"
            elif EmmaX.DildoP < 3:
                $ EmmaX.FaceChange("sexy", 1)
                $ EmmaX.Brows = "confused"
                $ EmmaX.Mouth = "kiss"
                ch_e "You want to stick it in my pussy again?"
            else:
                $ EmmaX.FaceChange("sexy", 1)
                $ EmmaX.ArmPose = 2
                $ Line = renpy.random.choice(["You want some of this action?",
                    "So you'd like another go?",
                    "You want to stick it in my pussy again?",
                    "You want me ta lube up your toy?"])
                ch_e "[Line]"
                $ Line = 0

    if Approval >= 2:
            #She's into it. . .
            if EmmaX.Forced:
                $ EmmaX.FaceChange("sad")
                $ EmmaX.Statup("Obed", 90, 1)
                $ EmmaX.Statup("Inbt", 60, 1)
                ch_e "Ok, fine."
            else:
                $ EmmaX.FaceChange("sexy", 1)
                $ EmmaX.Statup("Love", 90, 1)
                $ EmmaX.Statup("Inbt", 50, 3)
                $ Line = renpy.random.choice(["Well, sure, stick it in.",
                    "Well. . . ok.",
                    "Sure!",
                    "I guess I could. . . stick it in.",
                    "Delightful.",
                    "Hmm, ok, ok."])
                ch_e "[Line]"
                $ Line = 0
            $ EmmaX.Statup("Obed", 20, 1)
            $ EmmaX.Statup("Obed", 60, 1)
            $ EmmaX.Statup("Inbt", 70, 2)
            jump Emma_DP_Prep

    else:
            #She's not into it, but maybe. . .
            $ EmmaX.FaceChange("angry")
            if "no dildo" in EmmaX.RecentActions:
                ch_e "What part of \"no,\" did you not get, [EmmaX.Petname]?"
            elif Taboo and "tabno" in EmmaX.DailyActions and "no dildo" in EmmaX.DailyActions:
                ch_e "Stop showing that thing around in public!"
            elif "no dildo" in EmmaX.DailyActions:
                ch_e "I already told you \"no,\" [EmmaX.Petname]."
            elif Taboo and "tabno" in EmmaX.DailyActions:
                ch_e "Stop showing that thing around in public!"
            elif not EmmaX.DildoP:
                $ EmmaX.FaceChange("bemused")
                ch_e "I'm a bit past toys, [EmmaX.Petname]. . ."
            else:
                $ EmmaX.FaceChange("bemused")
                ch_e "We don't need any toys, do we, [EmmaX.Petname]?"
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in EmmaX.DailyActions:
                    $ EmmaX.FaceChange("bemused")
                    ch_e "I thought as much, [EmmaX.Petname]."
                    return
                "Maybe later?" if "no dildo" not in EmmaX.DailyActions:
                    $ EmmaX.FaceChange("sexy")
                    ch_e "Maybe I'll practice on my own time, [EmmaX.Petname]."
                    $ EmmaX.Statup("Love", 80, 2)
                    $ EmmaX.Statup("Inbt", 70, 2)
                    if Taboo:
                        $ EmmaX.RecentActions.append("tabno")
                        $ EmmaX.DailyActions.append("tabno")
                    $ EmmaX.RecentActions.append("no dildo")
                    $ EmmaX.DailyActions.append("no dildo")
                    return
                "I think you'd like it. . .":
                    if Approval:
                        $ EmmaX.FaceChange("sexy")
                        $ EmmaX.Statup("Obed", 90, 2)
                        $ EmmaX.Statup("Obed", 50, 2)
                        $ EmmaX.Statup("Inbt", 70, 3)
                        $ EmmaX.Statup("Inbt", 40, 2)
                        $ Line = renpy.random.choice(["Well, sure, stick it in.",
                            "I suppose. . .",
                            "You make a compelling argument."])
                        ch_e "[Line]"
                        $ Line = 0
                        jump Emma_DP_Prep
                    else:
                        pass

                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck(EmmaX, 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                    if Approval > 1 or (Approval and EmmaX.Forced):
                        $ EmmaX.FaceChange("sad")
                        $ EmmaX.Statup("Love", 70, -5, 1)
                        $ EmmaX.Statup("Love", 200, -5)
                        ch_e "Ok, fine. If we're going to do this, stick it in already."
                        $ EmmaX.Statup("Obed", 80, 4)
                        $ EmmaX.Statup("Inbt", 80, 1)
                        $ EmmaX.Statup("Inbt", 60, 3)
                        $ EmmaX.Forced = 1
                        jump Emma_DP_Prep
                    else:
                        $ EmmaX.Statup("Love", 200, -20)
                        $ EmmaX.RecentActions.append("angry")
                        $ EmmaX.DailyActions.append("angry")

    #She refused all offers.
    $ EmmaX.ArmPose = 1
    if "no dildo" in EmmaX.DailyActions:
            ch_e "Learn to take \"no\" for an answer, [EmmaX.Petname]."
            $ EmmaX.RecentActions.append("angry")
            $ EmmaX.DailyActions.append("angry")
    elif EmmaX.Forced:
            $ EmmaX.FaceChange("angry", 1)
            ch_e "I'm not going to let you use that on me."
            $ EmmaX.Statup("Lust", 200, 5)
            if EmmaX.Love > 300:
                    $ EmmaX.Statup("Love", 70, -2)
            $ EmmaX.Statup("Obed", 50, -2)
            $ EmmaX.RecentActions.append("angry")
            $ EmmaX.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
            $ EmmaX.FaceChange("angry", 1)
            $ EmmaX.RecentActions.append("tabno")
            $ EmmaX.DailyActions.append("tabno")
            ch_e "Not here!"
            $ EmmaX.Statup("Lust", 200, 5)
            $ EmmaX.Statup("Obed", 50, -3)
    elif EmmaX.DildoP:
            $ EmmaX.FaceChange("sad")
            ch_e "Sorry, you can keep your toys to yourself."
    else:
            $ EmmaX.FaceChange("normal", 1)
            ch_e "No way."
    $ EmmaX.RecentActions.append("no dildo")
    $ EmmaX.DailyActions.append("no dildo")
    $ temp_modifier = 0
    return

label Emma_DP_Prep: #Animation set-up
    if Trigger2 == "dildo pussy":
        return

    if not EmmaX.Forced and Situation != "auto":
        $ temp_modifier = 15 if EmmaX.PantsNum() > 6 else 0
        call Bottoms_Off(EmmaX)
        if "angry" in EmmaX.RecentActions:
            return

    $ temp_modifier = 0
    call Emma_Pussy_Launch("dildo pussy")
    if not EmmaX.DildoP:
        if EmmaX.Forced:
            $ EmmaX.Statup("Love", 90, -75)
            $ EmmaX.Statup("Obed", 70, 60)
            $ EmmaX.Statup("Inbt", 80, 35)
        else:
            $ EmmaX.Statup("Love", 90, 10)
            $ EmmaX.Statup("Obed", 70, 20)
            $ EmmaX.Statup("Inbt", 80, 45)
    if Taboo:
        $ EmmaX.Inbt += int(Taboo/10)
        $ EmmaX.Lust += int(Taboo/5)


    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ EmmaX.DrainWord("tabno")
    $ EmmaX.DrainWord("no dildo")
    $ EmmaX.RecentActions.append("dildo pussy")
    $ EmmaX.DailyActions.append("dildo pussy")

label Emma_DP_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(EmmaX)
        call Emma_Pussy_Launch("dildo pussy")
        $ EmmaX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                call Slap_Ass(EmmaX)
                                jump Emma_DP_Cycle

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
                                            if EmmaX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ EmmaX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(EmmaX,"tired")

                                    "Shift primary action":
                                            if EmmaX.Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in her ass.":
                                                                $ Situation = "shift"
                                                                call Emma_DP_After
                                                                call Emma_Insert_Ass
                                                        "Just stick a finger in her ass without asking.":
                                                                $ Situation = "auto"
                                                                call Emma_DP_After
                                                                call Emma_Insert_Ass
                                                        "I want to shift the dildo to her ass.":
                                                                $ Situation = "shift"
                                                                call Emma_DP_After
                                                                call Emma_Dildo_Ass
                                                        "Never Mind":
                                                                jump Emma_DP_Cycle
                                            else:
                                                call Sex_Basic_Dialog(EmmaX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Emma_DP_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(EmmaX)
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(EmmaX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(EmmaX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Emma_DP_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_DP_Cycle
                                            "Never mind":
                                                        jump Emma_DP_Cycle
                                    "Undress [EmmaX.Name]":
                                            call Girl_Undress(EmmaX)
                                    "Clean up [EmmaX.Name] (locked)" if not EmmaX.Spunk:
                                            pass
                                    "Clean up [EmmaX.Name]" if EmmaX.Spunk:
                                            call Girl_Cleanup(EmmaX,"ask")
                                    "Never mind":
                                            jump Emma_DP_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Emma_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Emma_DP_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Emma_Pos_Reset
                                    $ Line = 0
                                    jump Emma_DP_After
        #End menu (if Line)

        if EmmaX.Panties or EmmaX.PantsNum() > 6 or EmmaX.HoseNum() >= 5: #This checks if [EmmaX.Name] wants to strip down.
                call Girl_Undress(EmmaX,"auto")

        call Shift_Focus(EmmaX)
        call Sex_Dialog(EmmaX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or EmmaX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(EmmaX)
                            if "angry" in EmmaX.RecentActions:
                                call Emma_Pos_Reset
                                return
                            $ EmmaX.Statup("Lust", 200, 5)
                            if 100 > EmmaX.Lust >= 70 and EmmaX.OCount < 2:
                                $ EmmaX.RecentActions.append("unsatisfied")
                                $ EmmaX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Emma_DP_After
                            $ Line = "came"
                    if EmmaX.Lust >= 100:
                            #If [EmmaX.Name] can cum
                            call Girl_Cumming(EmmaX)
                            if Situation == "shift" or "angry" in EmmaX.RecentActions:
                                jump Emma_DP_After
                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."
                            if "unsatisfied" in EmmaX.RecentActions:#And [EmmaX.Name] is unsatisfied,
                                    "[EmmaX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Emma_DP_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif Cnt == (5 + EmmaX.DildoP):
                    $ EmmaX.Brows = "confused"
                    ch_e "What are you even doing down there?"
        elif EmmaX.Lust >= 80:
                    pass
        elif Cnt == (15 + EmmaX.DildoP) and EmmaX.SEXP >= 15 and not ApprovalCheck(EmmaX, 1500):
                    $ EmmaX.Brows = "confused"
                    menu:
                        ch_e "[EmmaX.Petname], this is getting uncomfortable, maybe we could try something else."
                        "Finish up.":
                                "You let go. . ."
                                jump Emma_DP_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Emma_DP_After
                        "No, this is fun.":
                                if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):
                                    $ EmmaX.Statup("Love", 200, -5)
                                    $ EmmaX.Statup("Obed", 50, 3)
                                    $ EmmaX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ EmmaX.FaceChange("angry", 1)
                                    call Emma_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_e "Well if that's your attitude, I don't need your \"help\"."
                                    $ EmmaX.Statup("Love", 50, -3, 1)
                                    $ EmmaX.Statup("Love", 80, -4, 1)
                                    $ EmmaX.Statup("Obed", 30, -1, 1)
                                    $ EmmaX.Statup("Obed", 50, -1, 1)
                                    $ EmmaX.RecentActions.append("angry")
                                    $ EmmaX.DailyActions.append("angry")
                                    jump Emma_DP_After
        #End Count check

        if Round == 10:
            ch_e "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ EmmaX.FaceChange("bemused", 0)
    $ Line = 0
    ch_e "Ok, [EmmaX.Petname], that's enough of that for now."


label Emma_DP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Emma_Pos_Reset

    $ EmmaX.FaceChange("sexy")

    $ EmmaX.DildoP += 1
    $ EmmaX.Action -=1

    call Partner_Like(EmmaX,1)

    if EmmaX.DildoP == 1:
            $ EmmaX.SEXP += 10
            if not Situation:
                if EmmaX.Love >= 500 and "unsatisfied" not in EmmaX.RecentActions:
                    ch_e "I appreciate the work you put in. . ."
                elif EmmaX.Obed <= 500 and Player.Focus <= 20:
                    $ EmmaX.FaceChange("perplexed", 1)
                    ch_e "Did you enjoy that?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_e "Mmm, so what else did you have in mind?"
    call Checkout
    return

# end EmmaX.Dildo Pussy /////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////Start Insert Ass

label Emma_Dildo_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(EmmaX)
    call Emma_Dildo_Check
    if not _return:
        return

    if EmmaX.Loose:
        $ temp_modifier += 30
    elif "anal" in EmmaX.RecentActions or "dildo anal" in EmmaX.RecentActions:
        $ temp_modifier -= 20
    elif "anal" in EmmaX.DailyActions or "dildo anal" in EmmaX.DailyActions:
        $ temp_modifier -= 10
    elif (EmmaX.Anal + EmmaX.DildoA + EmmaX.Plug) > 0: #You've done it before
        $ temp_modifier += 20

    if EmmaX.PantsNum() >= 6: # she's got pants on.
        $ temp_modifier -= 20

    if EmmaX.Lust > 95:
        $ temp_modifier += 20
    elif EmmaX.Lust > 85: #She's really horny
        $ temp_modifier += 15

    if Situation == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in EmmaX.Traits:
        $ temp_modifier += (5*Taboo)
    if EmmaX in Player.Harem or "sex friend" in EmmaX.Petnames:
        $ temp_modifier += 10
    elif "ex" in EmmaX.Traits:
        $ temp_modifier -= 40
    if EmmaX.ForcedCount and not EmmaX.Forced:
        $ temp_modifier -= 5 * EmmaX.ForcedCount

    if Taboo and "tabno" in EmmaX.DailyActions:
        $ temp_modifier -= 10

    if "no dildo" in EmmaX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no dildo" in EmmaX.RecentActions else 0

    $ Approval = ApprovalCheck(EmmaX, 1450, TabM = 4) # 145, 160, 175, Taboo -160(355)

    if Situation == EmmaX:
            #Emma auto-starts
            if Approval > 2:                                                      # fix, add emma auto stuff here
                if EmmaX.PantsNum() == 5:
                    "[EmmaX.Name] grabs her dildo, hiking up her skirt as she does."
                    $ EmmaX.Upskirt = 1
                elif EmmaX.PantsNum() > 6:
                    "[EmmaX.Name] grabs her dildo, pulling down her pants as she does."
                    $ EmmaX.Legs = 0
                else:
                    "[EmmaX.Name] grabs her dildo, rubbing is suggestively against her ass."
                $ EmmaX.SeenPanties = 1
                "She slides the tip against her asshole, and seems to want you to insert it."
                menu:
                    "What do you do?"
                    "Nothing.":
                        $ EmmaX.Statup("Inbt", 80, 3)
                        $ EmmaX.Statup("Inbt", 50, 2)
                        "[EmmaX.Name] slides it in."
                    "Go for it.":
                        $ EmmaX.FaceChange("sexy", 1)
                        $ EmmaX.Statup("Inbt", 80, 3)
                        ch_p "Oh yeah, [EmmaX.Pet], let's do this."
                        $ EmmaX.NameCheck() #checks reaction to petname
                        "You grab the dildo and slide it in."
                        $ EmmaX.Statup("Love", 85, 1)
                        $ EmmaX.Statup("Obed", 90, 1)
                        $ EmmaX.Statup("Obed", 50, 2)
                    "Ask her to stop.":
                        $ EmmaX.FaceChange("surprised")
                        $ EmmaX.Statup("Inbt", 70, 1)
                        ch_p "Let's not do that right now, [EmmaX.Pet]."
                        $ EmmaX.NameCheck() #checks reaction to petname
                        "[EmmaX.Name] sets the dildo down."
                        $ EmmaX.OutfitChange()
                        $ EmmaX.Statup("Obed", 90, 1)
                        $ EmmaX.Statup("Obed", 50, 1)
                        $ EmmaX.Statup("Obed", 30, 2)
                        return
                jump Emma_DA_Prep
            else:
                $ temp_modifier = 0                               # fix, add emma auto stuff here
                $ Trigger2 = 0
            return

    if Situation == "auto":
            "You rub the dildo across her body, and against her tight anus."
            $ EmmaX.FaceChange("surprised", 1)

            if (EmmaX.DildoA and Approval) or (Approval > 1):
                #this is not the first time you've had sex, or she's into it
                "[EmmaX.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                $ EmmaX.FaceChange("sexy")
                $ EmmaX.Statup("Obed", 70, 3)
                $ EmmaX.Statup("Inbt", 50, 3)
                $ EmmaX.Statup("Inbt", 70, 1)
                ch_e "Mmmm, [EmmaX.Petname], toys. . ."
                jump Emma_DA_Prep
            else:
                #she's questioning it
                $ EmmaX.Brows = "angry"
                menu:
                    ch_e "Excuse yourself, what are you planning to do with that?!"
                    "Sorry, sorry! Never mind.":
                        if Approval:
                            $ EmmaX.FaceChange("sexy", 1)
                            $ EmmaX.Statup("Obed", 70, 3)
                            $ EmmaX.Statup("Inbt", 50, 3)
                            $ EmmaX.Statup("Inbt", 70, 1)
                            ch_e "Well, now that you mention it. . ."
                            jump Emma_DA_Prep
                        "You pull back before you really get it in."
                        $ EmmaX.FaceChange("bemused", 1)
                        if EmmaX.DildoA:
                            ch_e "Well, [EmmaX.Petname], maybe warn me next time?"
                        else:
                            ch_e "Well, [EmmaX.Petname], that's a little much. . . for now . . ."
                    "Just playing with my favorite toys.":
                        $ EmmaX.Statup("Love", 80, -10, 1)
                        $ EmmaX.Statup("Love", 200, -10)
                        "You press it inside some more."
                        $ EmmaX.Statup("Obed", 70, 3)
                        $ EmmaX.Statup("Inbt", 50, 3)
                        if not ApprovalCheck(EmmaX, 700, "O", TabM=1): #Checks if Obed is 700+
                            $ EmmaX.FaceChange("angry")
                            "[EmmaX.Name] shoves you away and slaps you in the face."
                            ch_e "Ask nicely if you want to stick something in my ass!"
                            $ EmmaX.Statup("Love", 50, -10, 1)
                            $ EmmaX.Statup("Obed", 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            if renpy.showing("Emma_SexSprite"):
                                call Emma_Sex_Reset
                            $ EmmaX.RecentActions.append("angry")
                            $ EmmaX.DailyActions.append("angry")
                        else:
                            $ EmmaX.FaceChange("sad")
                            "[EmmaX.Name] doesn't seem to be into this, you're lucky she's so obedient."
                            jump Emma_DA_Prep
            return
    #end auto

    if not EmmaX.DildoA:
            #first time
            $ EmmaX.FaceChange("surprised", 1)
            $ EmmaX.Mouth = "kiss"
            ch_e "Hmm, you don't take half measures. . ."
            if EmmaX.Forced:
                $ EmmaX.FaceChange("sad")
                ch_e "They always go for the butt. . ."

    if not EmmaX.DildoA and Approval:
            #First time dialog
            if EmmaX.Forced:
                $ EmmaX.FaceChange("sad")
                $ EmmaX.Statup("Love", 70, -3, 1)
                $ EmmaX.Statup("Love", 20, -2, 1)
            elif EmmaX.Love >= (EmmaX.Obed + EmmaX.Inbt):
                $ EmmaX.FaceChange("sexy")
                $ EmmaX.Brows = "sad"
                $ EmmaX.Mouth = "smile"
                ch_e "I suppose you might enjoy that. . ."
            elif EmmaX.Obed >= EmmaX.Inbt:
                $ EmmaX.FaceChange("normal")
                ch_e "If that's what you want, [EmmaX.Petname]. . ."
            else: # Uninhibited
                $ EmmaX.FaceChange("sad")
                $ EmmaX.Mouth = "smile"
                ch_e "I suppose I could enjoy that. . ."

    elif Approval:
            #Second time+ dialog
            if EmmaX.Forced:
                $ EmmaX.FaceChange("sad")
                $ EmmaX.Statup("Love", 70, -3, 1)
                $ EmmaX.Statup("Love", 20, -2, 1)
                ch_e "The toys again?"
            elif not Taboo and "tabno" in EmmaX.DailyActions:
                ch_e "Well, at least you got us some privacy this time. . ."
            elif "dildo anal" in EmmaX.DailyActions and not EmmaX.Loose:
                pass
            elif EmmaX.DildoA < 3:
                $ EmmaX.FaceChange("sexy", 1)
                $ EmmaX.Brows = "confused"
                $ EmmaX.Mouth = "kiss"
                ch_e "You want to stick it in my ass again?"
            else:
                $ EmmaX.FaceChange("sexy", 1)
                $ EmmaX.ArmPose = 2
                $ Line = renpy.random.choice(["You want some of this action?",
                    "So you'd like another go?",
                    "You'd like to stick it in my ass again?",
                    "You'd like me to lube up your toy?"])
                ch_e "[Line]"
                $ Line = 0

    if Approval >= 2:
            #She's into it. . .
            if EmmaX.Forced:
                $ EmmaX.FaceChange("sad")
                $ EmmaX.Statup("Obed", 90, 1)
                $ EmmaX.Statup("Inbt", 60, 1)
                ch_e "Oh, fine."
            else:
                $ EmmaX.FaceChange("sexy", 1)
                $ EmmaX.Statup("Love", 90, 1)
                $ EmmaX.Statup("Inbt", 50, 3)
                $ Line = renpy.random.choice(["Well, sure, stick it in.",
                    "Hmm. . . ok.",
                    "Sure!",
                    "I guess I could. . . stick it in.",
                    "Delightful.",
                    "Hmm, ok, ok."])
                ch_e "[Line]"
                $ Line = 0
            $ EmmaX.Statup("Obed", 20, 1)
            $ EmmaX.Statup("Obed", 60, 1)
            $ EmmaX.Statup("Inbt", 70, 2)
            jump Emma_DA_Prep

    else:
            #She's not into it, but maybe. . .
            $ EmmaX.FaceChange("angry")
            if "no dildo" in EmmaX.RecentActions:
                ch_e "What part of \"no,\" did you not get, [EmmaX.Petname]?"
            elif Taboo and "tabno" in EmmaX.DailyActions and "no dildo" in EmmaX.DailyActions:
                ch_e "Stop swinging that thing around in public!"
            elif "no dildo" in EmmaX.DailyActions:
                ch_e "I already told you \"no,\" [EmmaX.Petname]."
            elif Taboo and "tabno" in EmmaX.DailyActions:
                ch_e "I already told you that I wouldn't do that out here!"
            elif not EmmaX.DildoA:
                $ EmmaX.FaceChange("bemused")
                ch_e "I'm just not into toys, [EmmaX.Petname]. . ."
            else:
                $ EmmaX.FaceChange("bemused")
                ch_e "I don't think we need any toys, [EmmaX.Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in EmmaX.DailyActions:
                    $ EmmaX.FaceChange("bemused")
                    ch_e "I'm sure, [EmmaX.Petname]."
                    return
                "Maybe later?" if "no dildo" not in EmmaX.DailyActions:
                    $ EmmaX.FaceChange("sexy")
                    ch_e "Perhaps I'll practice on my own time, [EmmaX.Petname]."
                    $ EmmaX.Statup("Love", 80, 2)
                    $ EmmaX.Statup("Inbt", 70, 2)
                    if Taboo:
                        $ EmmaX.RecentActions.append("tabno")
                        $ EmmaX.DailyActions.append("tabno")
                    $ EmmaX.RecentActions.append("no dildo")
                    $ EmmaX.DailyActions.append("no dildo")
                    return
                "I think you'd like it. . .":
                    if Approval:
                        $ EmmaX.FaceChange("sexy")
                        $ EmmaX.Statup("Obed", 90, 2)
                        $ EmmaX.Statup("Obed", 50, 2)
                        $ EmmaX.Statup("Inbt", 70, 3)
                        $ EmmaX.Statup("Inbt", 40, 2)
                        $ Line = renpy.random.choice(["Very well, stick it in.",
                            "I suppose. . .",
                            "You make a compelling argument."])
                        ch_e "[Line]"
                        $ Line = 0
                        jump Emma_DA_Prep
                    else:
                        pass

                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck(EmmaX, 1050, "OI", TabM = 3) # 105, 120, 135, -120(225)
                    if Approval > 1 or (Approval and EmmaX.Forced):
                        $ EmmaX.FaceChange("sad")
                        $ EmmaX.Statup("Love", 70, -5, 1)
                        $ EmmaX.Statup("Love", 200, -5)
                        ch_e "Ok, fine. If we're going to do this, stick it in already."
                        $ EmmaX.Statup("Obed", 80, 4)
                        $ EmmaX.Statup("Inbt", 80, 1)
                        $ EmmaX.Statup("Inbt", 60, 3)
                        $ EmmaX.Forced = 1
                        jump Emma_DA_Prep
                    else:
                        $ EmmaX.Statup("Love", 200, -20)
                        $ EmmaX.RecentActions.append("angry")
                        $ EmmaX.DailyActions.append("angry")

    #She refused all offers.
    $ EmmaX.ArmPose = 1
    if "no dildo" in EmmaX.DailyActions:
            ch_e "Learn to take \"no\" for an answer, [EmmaX.Petname]."
            $ EmmaX.RecentActions.append("angry")
            $ EmmaX.DailyActions.append("angry")
    elif EmmaX.Forced:
            $ EmmaX.FaceChange("angry", 1)
            ch_e "I'm not going to let you use that on me."
            $ EmmaX.Statup("Lust", 200, 5)
            if EmmaX.Love > 300:
                    $ EmmaX.Statup("Love", 70, -2)
            $ EmmaX.Statup("Obed", 50, -2)
            $ EmmaX.RecentActions.append("angry")
            $ EmmaX.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
            $ EmmaX.FaceChange("angry", 1)
            $ EmmaX.RecentActions.append("tabno")
            $ EmmaX.DailyActions.append("tabno")
            ch_e "Not here!"
            $ EmmaX.Statup("Lust", 200, 5)
            $ EmmaX.Statup("Obed", 50, -3)
    elif EmmaX.DildoA:
            $ EmmaX.FaceChange("sad")
            ch_e "Sorry, you can keep your toys out of there."
    else:
            $ EmmaX.FaceChange("normal", 1)
            ch_e "No, thank you."
    $ EmmaX.RecentActions.append("no dildo")
    $ EmmaX.DailyActions.append("no dildo")
    $ temp_modifier = 0
    return

label Emma_DA_Prep: #Animation set-up
    if Trigger2 == "dildo anal":
        return

    if not EmmaX.Forced and Situation != "auto":
        $ temp_modifier = 20 if EmmaX.PantsNum() > 6 else 0
        call Bottoms_Off(EmmaX)
        if "angry" in EmmaX.RecentActions:
            return

    $ temp_modifier = 0
    call Emma_Pussy_Launch("dildo anal")
    if not EmmaX.DildoA:
        if EmmaX.Forced:
            $ EmmaX.Statup("Love", 90, -75)
            $ EmmaX.Statup("Obed", 70, 60)
            $ EmmaX.Statup("Inbt", 80, 35)
        else:
            $ EmmaX.Statup("Love", 90, 10)
            $ EmmaX.Statup("Obed", 70, 20)
            $ EmmaX.Statup("Inbt", 80, 45)
    if Taboo:
        $ EmmaX.Inbt += int(Taboo/10)
        $ EmmaX.Lust += int(Taboo/5)


    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ EmmaX.DrainWord("tabno")
    $ EmmaX.DrainWord("no dildo")
    $ EmmaX.RecentActions.append("dildo anal")
    $ EmmaX.DailyActions.append("dildo anal")

label Emma_DA_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(EmmaX)
        call Emma_Pussy_Launch("dildo anal")
        $ EmmaX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                call Slap_Ass(EmmaX)
                                jump Emma_DA_Cycle

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
                                            if EmmaX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ EmmaX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(EmmaX,"tired")

                                    "Shift primary action":
                                            if EmmaX.Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in her pussy.":
                                                                $ Situation = "shift"
                                                                call Emma_DA_After
                                                                call Emma_Fondle_Pussy
                                                        "Just stick a finger in her pussy without asking.":
                                                                $ Situation = "auto"
                                                                call Emma_DA_After
                                                                call Emma_Fondle_Pussy
                                                        "I want to shift the dildo to her pussy.":
                                                                $ Situation = "shift"
                                                                call Emma_DA_After
                                                                call Emma_Dildo_Pussy
                                                        "Never Mind":
                                                                jump Emma_DA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(EmmaX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Emma_DA_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(EmmaX)
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(EmmaX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(EmmaX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Emma_DA_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_DA_Cycle
                                            "Never mind":
                                                        jump Emma_DA_Cycle
                                    "Undress [EmmaX.Name]":
                                            call Girl_Undress(EmmaX)
                                    "Clean up [EmmaX.Name] (locked)" if not EmmaX.Spunk:
                                            pass
                                    "Clean up [EmmaX.Name]" if EmmaX.Spunk:
                                            call Girl_Cleanup(EmmaX,"ask")
                                    "Never mind":
                                            jump Emma_DA_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Emma_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Emma_DA_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Emma_Pos_Reset
                                    $ Line = 0
                                    jump Emma_DA_After
        #End menu (if Line)

        if EmmaX.Panties or EmmaX.PantsNum() > 6 or EmmaX.HoseNum() >= 5: #This checks if [EmmaX.Name] wants to strip down.
                call Girl_Undress(EmmaX,"auto")

        call Shift_Focus(EmmaX)
        call Sex_Dialog(EmmaX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or EmmaX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(EmmaX)
                            if "angry" in EmmaX.RecentActions:
                                call Emma_Pos_Reset
                                return
                            $ EmmaX.Statup("Lust", 200, 5)
                            if 100 > EmmaX.Lust >= 70 and EmmaX.OCount < 2:
                                $ EmmaX.RecentActions.append("unsatisfied")
                                $ EmmaX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Emma_DA_After
                            $ Line = "came"

                    if EmmaX.Lust >= 100:
                            #If [EmmaX.Name] can cum
                            call Girl_Cumming(EmmaX)
                            if Situation == "shift" or "angry" in EmmaX.RecentActions:
                                jump Emma_DA_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in EmmaX.RecentActions:#And [EmmaX.Name] is unsatisfied,
                                    "[EmmaX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Emma_DA_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif Cnt == (5 + EmmaX.DildoA):
                    $ EmmaX.Brows = "confused"
                    ch_e "What are you even doing down there?"
        elif EmmaX.Lust >= 80:
                    pass
        elif Cnt == (15 + EmmaX.DildoA) and EmmaX.SEXP >= 15 and not ApprovalCheck(EmmaX, 1500):
                    $ EmmaX.Brows = "confused"
                    menu:
                        ch_e "[EmmaX.Petname], this is getting uncomfortable, maybe we could try something else."
                        "Finish up.":
                                "You let go. . ."
                                jump Emma_DA_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Emma_DA_After
                        "No, this is fun.":
                                if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):
                                    $ EmmaX.Statup("Love", 200, -5)
                                    $ EmmaX.Statup("Obed", 50, 3)
                                    $ EmmaX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ EmmaX.FaceChange("angry", 1)
                                    call Emma_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_e "Well if that's your attitude, I don't need your \"help\"."
                                    $ EmmaX.Statup("Love", 50, -3, 1)
                                    $ EmmaX.Statup("Love", 80, -4, 1)
                                    $ EmmaX.Statup("Obed", 30, -1, 1)
                                    $ EmmaX.Statup("Obed", 50, -1, 1)
                                    $ EmmaX.RecentActions.append("angry")
                                    $ EmmaX.DailyActions.append("angry")
                                    jump Emma_DA_After
        #End Count check

        if Round == 10:
            ch_e "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ EmmaX.FaceChange("bemused", 0)
    $ Line = 0
    ch_e "Ok, [EmmaX.Petname], that's enough of that for now."


label Emma_DA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Emma_Pos_Reset

    $ EmmaX.FaceChange("sexy")

    $ EmmaX.DildoA += 1
    $ EmmaX.Action -=1

    call Partner_Like(EmmaX,1)

    if EmmaX.DildoA == 1:
            $ EmmaX.SEXP += 10
            if not Situation:
                if EmmaX.Love >= 500 and "unsatisfied" not in EmmaX.RecentActions:
                    ch_e "That was. . . engaging. . ."
                elif EmmaX.Obed <= 500 and Player.Focus <= 20:
                    $ EmmaX.FaceChange("perplexed", 1)
                    ch_e "Did you enjoy that?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_e "Mmm, so what else did you have in mind?"
    call Checkout
    return

# end EmmaX.Dildo Ass /////////////////////////////////////////////////////////////////////////////

label Emma_Vibrator_Check:                                                                                 #fix this whole section is copy/paste unfinished
    if "vibrator" in Player.Inventory:
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in EmmaX.Inventory:
        "You ask [EmmaX.Name] to get out her vibrator."
    else:
        "You don't have one of those on you."
        return 0
    return 1

## EmmaX.Footjob //////////////////////////////////////////////////////////////////////
label Emma_Footjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(EmmaX)
    if EmmaX.Foot >= 7: # She loves it
        $ temp_modifier += 10
    elif EmmaX.Foot >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif EmmaX.Foot: #You've done it before
        $ temp_modifier += 3

    if EmmaX.Addict >= 75 and EmmaX.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 10
    if EmmaX.Addict >= 75:
        $ temp_modifier += 5

    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in EmmaX.Traits:
        $ temp_modifier += (3*Taboo)
    if EmmaX in Player.Harem or "sex friend" in EmmaX.Petnames:
        $ temp_modifier += 10
    elif "ex" in EmmaX.Traits:
        $ temp_modifier -= 40
    if EmmaX.ForcedCount and not EmmaX.Forced:
        $ temp_modifier -= 5 * EmmaX.ForcedCount

    if Taboo and "tabno" in EmmaX.DailyActions:
        $ temp_modifier -= 10

    if "no foot" in EmmaX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no foot" in EmmaX.RecentActions else 0

    $ Approval = ApprovalCheck(EmmaX, 1250, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if Situation == EmmaX:                                                                  #Emma auto-starts
        if Approval > 2:                                                      # fix, add emma auto stuff here
            if Trigger2 == "jackin":
                "[EmmaX.Name] sits back and starts rubbing her foot along your cock."
            else:
                "[EmmaX.Name] gives you a mischevious smile, and starts to rub her foot along your cock."
            menu:
                "What do you do?"
                "Nothing.":
                    $ EmmaX.Statup("Inbt", 70, 3)
                    $ EmmaX.Statup("Inbt", 30, 2)
                    "[EmmaX.Name] continues her actions."
                "Praise her.":
                    $ EmmaX.FaceChange("sexy", 1)
                    $ EmmaX.Statup("Inbt", 70, 3)
                    ch_p "Oooh, that's good, [EmmaX.Pet]."
                    $ EmmaX.NameCheck() #checks reaction to petname
                    "[EmmaX.Name] continues her actions."
                    $ EmmaX.Statup("Love", 80, 1)
                    $ EmmaX.Statup("Obed", 90, 1)
                    $ EmmaX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ EmmaX.FaceChange("surprised")
                    $ EmmaX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [EmmaX.Pet]."
                    $ EmmaX.NameCheck() #checks reaction to petname
                    "[EmmaX.Name] puts it down."
                    $ EmmaX.Statup("Obed", 90, 1)
                    $ EmmaX.Statup("Obed", 50, 1)
                    $ EmmaX.Statup("Obed", 30, 2)
                    return
            if Trigger:
                $ Trigger3 = "foot"
                return
            jump Emma_FJ_Prep
        else:
            $ temp_modifier = 0                               # fix, add emma auto stuff here
            $ Trigger2 = 0
            return

    if not EmmaX.Foot and "no foot" not in EmmaX.RecentActions:
        $ EmmaX.FaceChange("confused", 2)
        ch_e "Mmm, so you're into feet then, [EmmaX.Petname]?"
        $ EmmaX.Blush = 1

    if not EmmaX.Foot and Approval:                                                 #First time dialog
        if EmmaX.Forced:
            $ EmmaX.FaceChange("sad",1)
            $ EmmaX.Statup("Love", 70, -3, 1)
            $ EmmaX.Statup("Love", 20, -2, 1)
        elif EmmaX.Love >= (EmmaX.Obed + EmmaX.Inbt):
            $ EmmaX.FaceChange("sexy",1)
            $ EmmaX.Brows = "sad"
            $ EmmaX.Mouth = "smile"
            ch_e "I suppose it couldn't hurt. . ."
        elif EmmaX.Obed >= EmmaX.Inbt:
            $ EmmaX.FaceChange("normal",1)
            ch_e "If you enjoy that, [EmmaX.Petname]. . ."
        elif EmmaX.Addict >= 50:
            $ EmmaX.FaceChange("manic", 1)
            ch_e "Very well. . ."
        else: # Uninhibited
            $ EmmaX.FaceChange("lipbite",1)
            ch_e "Very well. . ."

    elif Approval:                                                                       #Second time+ dialog
        if EmmaX.Forced:
            $ EmmaX.FaceChange("sad")
            $ EmmaX.Statup("Love", 70, -3, 1)
            $ EmmaX.Statup("Love", 20, -2, 1)
            ch_e "That's it?"
        elif not Taboo and "tabno" in EmmaX.DailyActions:
            ch_e "Um, I suppose this is secluded enough. . ."
        elif "foot" in EmmaX.RecentActions:
            $ EmmaX.FaceChange("sexy", 1)
            ch_e "You know, heels are nightmare on the arches. . ."
            jump Emma_FJ_Prep
        elif "foot" in EmmaX.DailyActions:
            $ EmmaX.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Another?",
                "I'd rather not get calluses.",
                "Didn't get enough earlier?",
                "My feet are rather sore from earlier.",
                "My feet are rather sore from earlier."])
            ch_e "[Line]"
        elif EmmaX.Foot < 3:
            $ EmmaX.FaceChange("sexy", 1)
            $ EmmaX.Brows = "confused"
            $ EmmaX.Mouth = "kiss"
            ch_e "Oh, very well. . ."
        else:
            $ EmmaX.FaceChange("sexy", 1)
            $ EmmaX.ArmPose = 2
            $ Line = renpy.random.choice(["You'd like me to use my feet again?",
                "So you'd like another footjob?",
                "Mmmm, some. . . [she rubs her foot along your leg]?",
                "A little foot rub?"])
            ch_e "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if EmmaX.Forced:
            $ EmmaX.FaceChange("sad")
            $ EmmaX.Statup("Obed", 90, 1)
            $ EmmaX.Statup("Inbt", 60, 1)
            ch_e "Oh, fine."
        elif "no foot" in EmmaX.DailyActions:
            ch_e "Oh, very well."
        else:
            $ EmmaX.FaceChange("sexy", 1)
            $ EmmaX.Statup("Love", 90, 1)
            $ EmmaX.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Sure, I suppose.",
                "Fine.",
                "Very well, bring it out.",
                "I suppose I could. . .",
                "Fine. . . [She gestures for you to come over].",
                "Hmm, ok."])
            ch_e "[Line]"
            $ Line = 0
        $ EmmaX.Statup("Obed", 20, 1)
        $ EmmaX.Statup("Obed", 60, 1)
        $ EmmaX.Statup("Inbt", 70, 2)
        jump Emma_FJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ EmmaX.FaceChange("angry")
        if "no foot" in EmmaX.RecentActions:
            ch_e "Pay attention, [EmmaX.Petname]."
        elif Taboo and "tabno" in EmmaX.DailyActions and "no foot" in EmmaX.DailyActions:
            ch_e "I refuse to do this in public."
        elif "no foot" in EmmaX.DailyActions:
            ch_e "I said \"no,\" [EmmaX.Petname]."
        elif Taboo and "tabno" in EmmaX.DailyActions:
            ch_e "I told you, not in public!"
        elif not EmmaX.Foot:
            $ EmmaX.FaceChange("bemused")
            ch_e "I'm unsure, [EmmaX.Petname]. . ."
        else:
            $ EmmaX.FaceChange("bemused")
            ch_e "Not now, [EmmaX.Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no foot" in EmmaX.DailyActions:
                $ EmmaX.FaceChange("bemused")
                ch_e "Thank you."
                return
            "Maybe later?" if "no foot" not in EmmaX.DailyActions:
                $ EmmaX.FaceChange("sexy")
                ch_e ". . ."
                ch_e "Perhaps."
                $ EmmaX.Statup("Love", 80, 2)
                $ EmmaX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ EmmaX.RecentActions.append("tabno")
                    $ EmmaX.DailyActions.append("tabno")
                $ EmmaX.RecentActions.append("no foot")
                $ EmmaX.DailyActions.append("no foot")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ EmmaX.FaceChange("sexy")
                    $ EmmaX.Statup("Obed", 90, 2)
                    $ EmmaX.Statup("Obed", 50, 2)
                    $ EmmaX.Statup("Inbt", 70, 3)
                    $ EmmaX.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Sure, I suppose.",
                            "Fine.",
                            "Very well, bring it out.",
                            "I suppose I could. . .",
                            "Fine. . . [She gestures for you to come over].",
                            "Hmm, ok."])
                    ch_e "[Line]"
                    $ Line = 0
                    jump Emma_FJ_Prep
                else:
                    pass

            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck(EmmaX, 400, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and EmmaX.Forced):
                    $ EmmaX.FaceChange("sad")
                    $ EmmaX.Statup("Love", 70, -5, 1)
                    $ EmmaX.Statup("Love", 200, -2)
                    ch_e "Oh, very well."
                    $ EmmaX.Statup("Obed", 50, 4)
                    $ EmmaX.Statup("Inbt", 80, 1)
                    $ EmmaX.Statup("Inbt", 60, 3)
                    $ EmmaX.Forced = 1
                    jump Emma_FJ_Prep
                else:
                    $ EmmaX.Statup("Love", 200, -15)
                    $ EmmaX.RecentActions.append("angry")
                    $ EmmaX.DailyActions.append("angry")

    #She refused all offers.
    $ EmmaX.ArmPose = 1
    if "no foot" in EmmaX.DailyActions:
        $ EmmaX.FaceChange("angry", 1)
        ch_e "I won't repeat myself."
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")
    elif EmmaX.Forced:
        $ EmmaX.FaceChange("angry", 1)
        ch_e "You really don't want my heels near your manhood."
        $ EmmaX.Statup("Lust", 200, 5)
        if EmmaX.Love > 300:
                $ EmmaX.Statup("Love", 70, -2)
        $ EmmaX.Statup("Obed", 50, -2)
        $ EmmaX.RecentActions.append("angry")
        $ EmmaX.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ EmmaX.FaceChange("angry", 1)
        $ EmmaX.DailyActions.append("tabno")
        ch_e "This truly isn't an appropriate place for that."
        $ EmmaX.Statup("Lust", 200, 5)
        $ EmmaX.Statup("Obed", 50, -3)
    elif EmmaX.Foot:
        $ EmmaX.FaceChange("sad")
        ch_e "I'm not in the mood, [EmmaX.Petname]. . ."
    else:
        $ EmmaX.FaceChange("normal", 1)
        ch_e "I'm not in the mood for footplay today. . ."
    $ EmmaX.RecentActions.append("no foot")
    $ EmmaX.DailyActions.append("no foot")
    $ temp_modifier = 0
    return


label Emma_FJ_Prep:
    if Trigger2 == "foot":
        return

    if Taboo:
        $ EmmaX.Inbt += int(Taboo/10)
        $ EmmaX.Lust += int(Taboo/5)

    $ EmmaX.FaceChange("sexy")
    if EmmaX.Forced:
        $ EmmaX.FaceChange("sad")
    elif not EmmaX.Foot:
        $ EmmaX.Brows = "confused"
        $ EmmaX.Eyes = "sexy"
        $ EmmaX.Mouth = "smile"

    call Seen_First_Peen(EmmaX,Partner,React=Situation)
    if not EmmaX.Foot:
        if EmmaX.Forced:
            $ EmmaX.Statup("Love", 90, -20)
            $ EmmaX.Statup("Obed", 70, 25)
            $ EmmaX.Statup("Inbt", 80, 30)
        else:
            $ EmmaX.Statup("Love", 90, 5)
            $ EmmaX.Statup("Obed", 70, 20)
            $ EmmaX.Statup("Inbt", 80, 20)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ EmmaX.DrainWord("tabno")
    $ EmmaX.DrainWord("no foot")
    $ EmmaX.RecentActions.append("foot")
    $ EmmaX.DailyActions.append("foot")
    ch_e "Did you want me facing you, or from behind?"
    menu:
        extend ""
        "Facing me":
                $ EmmaX.Pose = "foot"
        "From behind.":
                $ EmmaX.Pose = "doggy"

label Emma_FJ_Cycle:
    while Round > 0:
        call Shift_Focus(EmmaX)
        call Emma_FJ_Launch
        $ EmmaX.LustFace()

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

                        "Turn her Around":
                                    $ EmmaX.Pose = "doggy" if EmmaX.Pose != "doggy" else "foot"
                                    "You turn her around. . ."
                                    jump Emma_FJ_Cycle


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
                                    "I also want to fondle her thighs." if Trigger2 != "fondle thighs":
                                            if MultiAction:
                                                $ Trigger2 = "fondle thighs"
                                                "You start to fondle her thighs."
                                            else:
                                                call Sex_Basic_Dialog(EmmaX,"tired")

                                    "Shift primary action":
                                            if EmmaX.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                    if EmmaX.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Emma_FJ_After
                                                                        call Emma_Blowjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(EmmaX,"tired")
                                                        "How about a handjob?":
                                                                    if EmmaX.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Emma_FJ_After
                                                                        call Emma_Handjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(EmmaX,"tired")

                                                        "How about a titjob?":
                                                                    if EmmaX.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Emma_FJ_After
                                                                        call Emma_Titjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(EmmaX,"tired")

                                                        "Never Mind":
                                                                jump Emma_FJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(EmmaX,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(EmmaX)
                                            "Asks [EmmaX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(EmmaX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(EmmaX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Emma_FJ_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_FJ_Cycle
                                            "Never mind":
                                                        jump Emma_FJ_Cycle
                                    "Undress [EmmaX.Name]":
                                            call Girl_Undress(EmmaX)
                                    "Clean up [EmmaX.Name] (locked)" if not EmmaX.Spunk:
                                            pass
                                    "Clean up [EmmaX.Name]" if EmmaX.Spunk:
                                            call Girl_Cleanup(EmmaX,"ask")
                                    "Never mind":
                                            jump Emma_FJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Emma_FJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Emma_FJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Emma_FJ_Reset
                                    $ Line = 0
                                    jump Emma_FJ_After
        #End menu (if Line)

        call Shift_Focus(EmmaX)
        call Sex_Dialog(EmmaX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or EmmaX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(EmmaX)
                            if "angry" in EmmaX.RecentActions:
                                call Emma_FJ_Reset
                                return
                            $ EmmaX.Statup("Lust", 200, 5)
                            if 100 > EmmaX.Lust >= 70 and EmmaX.OCount < 2:
                                $ EmmaX.RecentActions.append("unsatisfied")
                                $ EmmaX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Emma_FJ_After
                            $ Line = "came"

                    if EmmaX.Lust >= 100:
                            #If [EmmaX.Name] can cum
                            call Girl_Cumming(EmmaX)
                            if Situation == "shift" or "angry" in EmmaX.RecentActions:
                                jump Emma_FJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in EmmaX.RecentActions:#And [EmmaX.Name] is unsatisfied,
                                    "[EmmaX.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Emma_FJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Cnt == 20:
                    $ EmmaX.Brows = "angry"
                    menu:
                        ch_e "Hmm, foot cramp, could we take a short break?"
                        "How about a BJ?" if EmmaX.Action and MultiAction:
                                $ Situation = "shift"
                                call Emma_FJ_After
                                call Emma_Blowjob
                        "How about a Handy?" if EmmaX.Action and MultiAction:
                                $ Situation = "shift"
                                call Emma_FJ_After
                                call Emma_Handjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump Emma_FJ_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Emma_Sex_Reset
                                $ Situation = "shift"
                                jump Emma_FJ_After
                        "No, keep going.":
                                if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):
                                    $ EmmaX.Statup("Love", 200, -5)
                                    $ EmmaX.Statup("Obed", 50, 3)
                                    $ EmmaX.Statup("Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    $ EmmaX.FaceChange("angry", 1)
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_e "I do have better things I could be doing."
                                    $ EmmaX.Statup("Love", 50, -3, 1)
                                    $ EmmaX.Statup("Love", 80, -4, 1)
                                    $ EmmaX.Statup("Obed", 30, -1, 1)
                                    $ EmmaX.Statup("Obed", 50, -1, 1)
                                    $ EmmaX.RecentActions.append("angry")
                                    $ EmmaX.DailyActions.append("angry")
                                    jump Emma_FJ_After
        elif Cnt == 10 and EmmaX.SEXP <= 100 and not ApprovalCheck(EmmaX, 1200, "LO"):
                    $ EmmaX.Brows = "confused"
                    ch_e "Could we be done here, my feet are getting sore."
        #End Count check

        call Escalation(EmmaX) #sees if she wants to escalate things

        if Round == 10:
            ch_e "Ok, it's getting a bit late here."
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ EmmaX.FaceChange("bemused", 0)
    $ Line = 0
    ch_e "Ok, [EmmaX.Petname], that's enough of that for now."

label Emma_FJ_After:
    $ EmmaX.FaceChange("sexy")

    $ EmmaX.Foot += 1
    $ EmmaX.Action -=1
    $ EmmaX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ EmmaX.Addictionrate += 1
    $ EmmaX.Statup("Lust", 90, 5)

    call Partner_Like(EmmaX,1)

    if "Emmapedi" in Achievements:
            pass
    elif EmmaX.Foot >= 10:
            $ EmmaX.FaceChange("smile", 1)
            ch_e "I'm glad that you enjoy my feet."
            ch_e "They've been trained well over the years."
            $ Achievements.append("Emmapedi")
            $ EmmaX.SEXP += 5
    elif EmmaX.Foot == 1:
            $ EmmaX.SEXP += 10
            if EmmaX.Love >= 500:
                $ EmmaX.Mouth = "smile"
                ch_e "Your cock was so warm . ."
            elif Player.Focus <= 20:
                $ EmmaX.Mouth = "sad"
                ch_e "Did you enjoy that?"
    elif EmmaX.Foot == 5:
                ch_e "I'm enjoying this experience."

    $ temp_modifier = 0
    if Situation == "shift":
        ch_e "Ok then, what were you thinking?"
    else:
        call Emma_Sex_Reset
    call Checkout
    return

## end EmmaX.Footjob //////////////////////////////////////////////////////////////////////
