## JubesX.Handjob //////////////////////////////////////////////////////////////////////
label Jubes_Handjob:
    #fix remove
    "This option is currently unavailable. It will be added in a later update."
    return
    #fix remove

    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JubesX)
    if JubesX.Hand >= 7: # She loves it
        $ temp_modifier += 10
    elif JubesX.Hand >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif JubesX.Hand: #You've done it before
        $ temp_modifier += 3

    if JubesX.Addict >= 75 and JubesX.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 15
    if JubesX.Addict >= 75:
        $ temp_modifier += 5

    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in JubesX.Traits:
        $ temp_modifier += (3*Taboo)
    if JubesX in Player.Harem or "sex friend" in JubesX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JubesX.Traits:
        $ temp_modifier -= 40
    if JubesX.ForcedCount and not JubesX.Forced:
        $ temp_modifier -= 5 * JubesX.ForcedCount

    if Taboo and "tabno" in JubesX.DailyActions:
        $ temp_modifier -= 10

    if "no hand" in JubesX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no hand" in JubesX.RecentActions else 0

    $ Approval = ApprovalCheck(JubesX, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if not JubesX.Hand and "no hand" not in JubesX.RecentActions:
        $ JubesX.FaceChange("confused", 2)
        ch_v "Handjob, huh. . ."
        $ JubesX.Blush = 1

    if not JubesX.Hand and Approval:                                                 #First time dialog
        if JubesX.Forced:
            $ JubesX.FaceChange("sad",1)
            $ JubesX.Statup("Love", 70, -3, 1)
            $ JubesX.Statup("Love", 20, -2, 1)
        elif JubesX.Love >= (JubesX.Obed + JubesX.Inbt):
            $ JubesX.FaceChange("sexy",1)
            $ JubesX.Brows = "sad"
            $ JubesX.Mouth = "smile"
            ch_v "You'd like that. . ."
        elif JubesX.Obed >= JubesX.Inbt:
            $ JubesX.FaceChange("normal",1)
            ch_v "If you want, [JubesX.Petname]. . ."
        else: # Uninhibited
            $ JubesX.FaceChange("lipbite",1)
            ch_v "Hmm. . ."

    elif Approval:                                                                       #Second time+ dialog
        if JubesX.Forced:
            $ JubesX.FaceChange("sad")
            $ JubesX.Statup("Love", 70, -3, 1)
            $ JubesX.Statup("Love", 20, -2, 1)
            ch_v "Nothing more than that?"
        elif not Taboo and "tabno" in JubesX.DailyActions:
            ch_v "Well,this is a bit more secure. . ."
        elif "hand" in JubesX.RecentActions:
            $ JubesX.FaceChange("sexy", 1)
            ch_v "Hmm, another handy then. . ."
            jump Jubes_HJ_Prep
        elif "hand" in JubesX.DailyActions:
            $ JubesX.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Another one?",
                "I'm glad I don't grow calluses.",
                "Didn't get enough earlier?",
                "Again the with handjobs, huh?",
                "I guess you want more."])
            ch_v "[Line]"
        elif JubesX.Hand < 3:
            $ JubesX.FaceChange("sexy", 1)
            $ JubesX.Brows = "confused"
            $ JubesX.Mouth = "kiss"
            ch_v "You seem to like this one. . ."
        else:
            $ JubesX.FaceChange("sexy", 1)
            $ JubesX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some more?",
                "So you'd like another handy?",
                "You want a. . . [fist pumping hand gestures]?",
                "Another handjob?"])
            ch_v "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if JubesX.Forced:
            $ JubesX.FaceChange("sad")
            $ JubesX.Statup("Obed", 90, 1)
            $ JubesX.Statup("Inbt", 60, 1)
            ch_v "Ok, fine."
        elif "no hand" in JubesX.DailyActions:
            ch_v "If it'll get you off my back. . ."
        else:
            $ JubesX.FaceChange("sexy", 1)
            $ JubesX.Statup("Love", 90, 1)
            $ JubesX.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Sure, I guess.",
                "O-kay.",
                "Fine.",
                "I suppose I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Ok, ok."])
            ch_v "[Line]"
            $ Line = 0
        $ JubesX.Statup("Obed", 20, 1)
        $ JubesX.Statup("Obed", 60, 1)
        $ JubesX.Statup("Inbt", 70, 2)
        jump Jubes_HJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ JubesX.FaceChange("angry")
        if "no hand" in JubesX.RecentActions:
            ch_v "I just told you no, [JubesX.Petname]."
        elif Taboo and "tabno" in JubesX.DailyActions and "no hand" in JubesX.DailyActions:
            ch_v "I said not in public."
        elif "no hand" in JubesX.DailyActions:
            ch_v "I told you \"no,\" [JubesX.Petname]."
        elif Taboo and "tabno" in JubesX.DailyActions:
            ch_v "I said not in public."
        elif not JubesX.Hand:
            $ JubesX.FaceChange("bemused")
            ch_v "Seriously, [JubesX.Petname]. . ."
        else:
            $ JubesX.FaceChange("bemused")
            ch_v "Nah."
        menu:
            extend ""
            "Sorry, never mind." if "no hand" in JubesX.DailyActions:
                $ JubesX.FaceChange("bemused")
                ch_v "It's fine."
                return
            "Maybe later?" if "no hand" not in JubesX.DailyActions:
                $ JubesX.FaceChange("bemused")
                ch_v "Maybe."
                $ JubesX.Statup("Love", 80, 2)
                $ JubesX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ JubesX.RecentActions.append("tabno")
                    $ JubesX.DailyActions.append("tabno")
                $ JubesX.RecentActions.append("no hand")
                $ JubesX.DailyActions.append("no hand")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ JubesX.FaceChange("sexy")
                    $ JubesX.Statup("Obed", 90, 2)
                    $ JubesX.Statup("Obed", 50, 2)
                    $ JubesX.Statup("Inbt", 70, 3)
                    $ JubesX.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Sure, I guess.",
                        "O-kay.",
                        "Fine.",
                        "I suppose I could. . .",
                        "Ok. . . [She gestures for you to come over].",
                        "Ok, ok."])
                    ch_v "[Line]"
                    $ Line = 0
                    jump Jubes_HJ_Prep
                else:
                    pass

            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck(JubesX, 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and JubesX.Forced):
                    $ JubesX.FaceChange("sad")
                    $ JubesX.Statup("Love", 70, -5, 1)
                    $ JubesX.Statup("Love", 200, -2)
                    ch_v "Ok, fine."
                    $ JubesX.Statup("Obed", 50, 4)
                    $ JubesX.Statup("Inbt", 80, 1)
                    $ JubesX.Statup("Inbt", 60, 3)
                    $ JubesX.Forced = 1
                    jump Jubes_HJ_Prep
                else:
                    $ JubesX.Statup("Love", 200, -15)
                    $ JubesX.RecentActions.append("angry")
                    $ JubesX.DailyActions.append("angry")

    #She refused all offers.
    $ JubesX.ArmPose = 1
    if "no hand" in JubesX.DailyActions:
        $ JubesX.FaceChange("angry", 1)
        ch_v "Don't ask again."
        $ JubesX.RecentActions.append("angry")
        $ JubesX.DailyActions.append("angry")
    elif JubesX.Forced:
        $ JubesX.FaceChange("angry", 1)
        ch_v "No."
        $ JubesX.Statup("Lust", 200, 5)
        if JubesX.Love > 300:
                $ JubesX.Statup("Love", 70, -2)
        $ JubesX.Statup("Obed", 50, -2)
        $ JubesX.RecentActions.append("angry")
        $ JubesX.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ JubesX.FaceChange("angry", 1)
        $ JubesX.DailyActions.append("tabno")
        ch_v "This area's too exposed."
        $ JubesX.Statup("Lust", 200, 5)
        $ JubesX.Statup("Obed", 50, -3)
    elif JubesX.Hand:
        $ JubesX.FaceChange("sad")
        ch_v "I'm not into it today. . ."
    else:
        $ JubesX.FaceChange("normal", 1)
        ch_v "I don't know where that's been lately."
    $ JubesX.RecentActions.append("no hand")
    $ JubesX.DailyActions.append("no hand")
    $ temp_modifier = 0
    return


label Jubes_HJ_Prep:
    #fix remove
    "This option is currently unavailable. It will be added in a later update."
    return
    #fix remove

    if Trigger2 == "hand":
        return

    if Taboo:
        $ JubesX.Inbt += int(Taboo/10)
        $ JubesX.Lust += int(Taboo/5)

    $ JubesX.FaceChange("sexy")
    if JubesX.Forced:
        $ JubesX.FaceChange("sad")
    elif not JubesX.Hand:
        $ JubesX.Brows = "confused"
        $ JubesX.Eyes = "sexy"
        $ JubesX.Mouth = "smile"

    call Seen_First_Peen(JubesX,Partner,React=Situation)
    call Jubes_HJ_Launch("L")

    if Situation == JubesX:
            #Jubes auto-starts
            $ Situation = 0
            if Trigger2 == "jackin":
                "[JubesX.Name] brushes your hand aside and starts stroking your cock."
            else:
                "[JubesX.Name] gives you a mischevious smile, and starts to fondle your cock."
            menu:
                "What do you do?"
                "Nothing.":
                    $ JubesX.Statup("Inbt", 70, 3)
                    $ JubesX.Statup("Inbt", 30, 2)
                    "[JubesX.Name] continues her actions."
                "Praise her.":
                    $ JubesX.FaceChange("sexy", 1)
                    $ JubesX.Statup("Inbt", 70, 3)
                    ch_p "Oooh, that's good, [JubesX.Pet]."
                    $ JubesX.NameCheck() #checks reaction to petname
                    "[JubesX.Name] continues her actions."
                    $ JubesX.Statup("Love", 80, 1)
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ JubesX.FaceChange("surprised")
                    $ JubesX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [JubesX.Pet]."
                    $ JubesX.NameCheck() #checks reaction to petname
                    "[JubesX.Name] puts it down."
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Obed", 50, 1)
                    $ JubesX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ JubesX.AddWord(1,"refused","refused")
                    return

    if not JubesX.Hand:
        if JubesX.Forced:
            $ JubesX.Statup("Love", 90, -20)
            $ JubesX.Statup("Obed", 70, 25)
            $ JubesX.Statup("Inbt", 80, 30)
        else:
            $ JubesX.Statup("Love", 90, 5)
            $ JubesX.Statup("Obed", 70, 20)
            $ JubesX.Statup("Inbt", 80, 20)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ JubesX.DrainWord("tabno")
    $ JubesX.DrainWord("no hand")
    $ JubesX.RecentActions.append("hand")
    $ JubesX.DailyActions.append("hand")

label Jubes_HJ_Cycle:
    while Round > 0:
        call Shift_Focus(JubesX)
        call Jubes_HJ_Launch
        $ JubesX.LustFace()

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
                                            if JubesX.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ JubesX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")

                                    "Shift primary action":
                                            if JubesX.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                    if JubesX.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Jubes_HJ_After
                                                                        call Jubes_Blowjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(JubesX,"tired")

                                                        "How about a titjob?":
                                                                    if JubesX.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Jubes_HJ_After
                                                                        call Jubes_Titjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(JubesX,"tired")
                                                        "Never Mind":
                                                                jump Jubes_HJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")

        #End menu (if Line)

        call Shift_Focus(JubesX)
        call Sex_Dialog(JubesX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JubesX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JubesX)
                            if "angry" in JubesX.RecentActions:
                                call Jubes_HJ_Reset
                                return
                            $ JubesX.Statup("Lust", 200, 5)
                            if 100 > JubesX.Lust >= 70 and JubesX.OCount < 2 and JubesX.SEXP >= 20:
                                $ JubesX.RecentActions.append("unsatisfied")
                                $ JubesX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jubes_HJ_After
                            $ Line = "came"

                    if JubesX.Lust >= 100:
                            #If Jubes can cum
                            call Girl_Cumming(JubesX)
                            if Situation == "shift" or "angry" in JubesX.RecentActions:
                                jump Jubes_HJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in JubesX.RecentActions:#And Jubes is unsatisfied,
                                "[JubesX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Jubes_HJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Cnt == 20:
                    $ JubesX.Brows = "angry"
                    menu:
                        ch_v "Hmm, this is boring, can we take a break?"
                        "How about a BJ?" if JubesX.Action and MultiAction:
                                $ Situation = "shift"
                                call Jubes_HJ_After
                                call Jubes_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                jump Jubes_HJ_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Jubes_HJ_Reset
                                $ Situation = "shift"
                                jump Jubes_HJ_After
                        "No, get back down there.":
                                if ApprovalCheck(JubesX, 1200) or ApprovalCheck(JubesX, 500, "O"):
                                    $ JubesX.Statup("Love", 200, -5)
                                    $ JubesX.Statup("Obed", 50, 3)
                                    $ JubesX.Statup("Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    $ JubesX.FaceChange("angry", 1)
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_v "I have better things to do with my time."
                                    $ JubesX.Statup("Love", 50, -3, 1)
                                    $ JubesX.Statup("Love", 80, -4, 1)
                                    $ JubesX.Statup("Obed", 30, -1, 1)
                                    $ JubesX.Statup("Obed", 50, -1, 1)
                                    $ JubesX.RecentActions.append("angry")
                                    $ JubesX.DailyActions.append("angry")
                                    jump Jubes_HJ_After
        elif Cnt == 10 and JubesX.SEXP <= 100 and not ApprovalCheck(JubesX, 1200, "LO"):
                    $ JubesX.Brows = "confused"
                    ch_v "This working for you?"
        #End Count check

        call Escalation(JubesX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(JubesX,10) #"I could use a break soon. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(JubesX,5)   #". . . I could really use a break here. . ."

    #Round = 0 loop breaks
    $ JubesX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(JubesX,"done") # ch_s "Ok, that's it, I need a break."

label Jubes_HJ_After:
    $ JubesX.FaceChange("sexy")

    $ JubesX.Hand += 1
    $ JubesX.Action -=1
    $ JubesX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ JubesX.Addictionrate += 1
    $ JubesX.Statup("Lust", 90, 5)

    call Partner_Like(JubesX,1)

    if "Jubes Handi-Queen" in Achievements:
            pass
    elif JubesX.Hand >= 10:
            $ JubesX.FaceChange("smile", 1)
            ch_v "Looks like you filled out the punch card, [JubesX.Petname]."
            $ Achievements.append("Jubes Handi-Queen")
            $JubesX.SEXP += 5
    elif JubesX.Hand == 1:
            $JubesX.SEXP += 10
            if JubesX.Love >= 500:
                $ JubesX.Mouth = "smile"
                ch_v "That was kind of. . . pleasant. . ."
            elif Player.Focus <= 20:
                $ JubesX.Mouth = "sad"
                ch_v "Did that do it for you?"
    elif JubesX.Hand == 5:
                ch_v "I think I've got this down, maybe I should get a punch card."

    $ temp_modifier = 0
    if Situation == "shift":
        ch_v "Ok, so what did you have in mind?"
    else:
        call Jubes_HJ_Reset
    call Checkout
    return

## end JubesX.Handjob //////////////////////////////////////////////////////////////////////


## JubesX.Titjob //////////////////////////////////////////////////////////////////////
label Jubes_Titjob:
    #fix remove
    "This option is currently unavailable. It will be added in a later update."
    return
    #fix remove

    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JubesX)
    if JubesX.Tit >= 7: # She loves it
        $ temp_modifier += 10
    elif JubesX.Tit >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif JubesX.Tit: #You've done it before
        $ temp_modifier += 5

    if JubesX.Addict >= 75 and JubesX.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 15
    elif JubesX.Addict >= 75:
        $ temp_modifier += 5

    if JubesX.SeenChest and ApprovalCheck(JubesX, 500): # You've seen her tits.
        $ temp_modifier += 10
    if not JubesX.Chest and not JubesX.Over: #She's already topless
        $ temp_modifier += 10
    if JubesX.Lust > 75: #She's really horny
        $ temp_modifier += 10
    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in JubesX.Traits:
        $ temp_modifier += (5*Taboo)
    if JubesX in Player.Harem or "sex friend" in JubesX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JubesX.Traits:
        $ temp_modifier -= 30
    if JubesX.ForcedCount and not JubesX.Forced:
        $ temp_modifier -= 5 * JubesX.ForcedCount

    if Taboo and "tabno" in JubesX.DailyActions:
        $ temp_modifier -= 10

    if "no titjob" in JubesX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no titjob" in JubesX.RecentActions else 0

    $ Approval = ApprovalCheck(JubesX, 1200, TabM = 4) # 120, 135, 150, Taboo -200(320)

    if not JubesX.Tit and "no titjob" not in JubesX.RecentActions:
        $ JubesX.FaceChange("surprised", 1)
        $ JubesX.Mouth = "kiss"
        ch_v "You want a titjob, huh?"

    if not JubesX.Tit and Approval:                                                 #First time dialog
        if JubesX.Forced:
            $ JubesX.FaceChange("sad")
            $ JubesX.Statup("Love", 70, -3, 1)
            $ JubesX.Statup("Love", 20, -2, 1)
        elif JubesX.Love >= (JubesX.Obed + JubesX.Inbt):
            $ JubesX.FaceChange("sexy")
            $ JubesX.Brows = "sad"
            $ JubesX.Mouth = "smile"
            ch_v "Well, maybe you deserve it."
        elif JubesX.Obed >= JubesX.Inbt:
            $ JubesX.FaceChange("normal")
            ch_v "If you'd like that. . ."
        elif JubesX.Addict >= 50:
            $ JubesX.FaceChange("manic", 1)
            ch_v "Hmmmm. . . ."
        else: # Uninhibited
            $ JubesX.FaceChange("sad")
            $ JubesX.Mouth = "smile"
            ch_v "Sounds fun. . ."
    elif Approval:                                                                       #Second time+ dialog
        if JubesX.Forced:
            $ JubesX.FaceChange("sad")
            $ JubesX.Statup("Love", 70, -3, 1)
            $ JubesX.Statup("Love", 20, -2, 1)
            ch_v "You're kinda pushing it."
        elif not Taboo and "tabno" in JubesX.DailyActions:
            ch_v "Ok, I guess this is secluded enough. . ."
        elif "titjob" in JubesX.RecentActions:
            $ JubesX.FaceChange("sexy", 1)
            ch_v "Huh, again?"
            jump Jubes_TJ_Prep
        elif "titjob" in JubesX.DailyActions:
            $ JubesX.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Back for more?",
                "You're really working these puppies.",
                "Didn't get enough earlier?",
                "You're really working these puppies."])
            ch_v "[Line]"
        elif JubesX.Tit < 3:
            $ JubesX.FaceChange("sexy", 1)
            $ JubesX.Brows = "confused"
            $ JubesX.Mouth = "kiss"
            ch_v "Another titjob??"
        else:
            $ JubesX.FaceChange("sexy", 1)
            $ JubesX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action [rubs her chest]?",
                "So you'd like another titjob?",
                "So you'd like another titjob?",
                "So you'd like another titjob?",
                "Another titjob?",
                "A little [points at her chest]?"])
            ch_v "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if JubesX.Forced:
            $ JubesX.FaceChange("sad")
            $ JubesX.Statup("Obed", 90, 1)
            $ JubesX.Statup("Inbt", 60, 1)
            ch_v "Well, could be worse. . ."
        elif "no titjob" in JubesX.DailyActions:
            ch_v "Hmm, I guess. . ."
        else:
            $ JubesX.FaceChange("sexy", 1)
            $ JubesX.Statup("Love", 90, 1)
            $ JubesX.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, put it here.",
                "Well. . . ok.",
                "Yum.",
                "Sure, whip it out.",
                "Fine. . . [She drools a bit into her cleavage].",
                "Heh, ok."])
            ch_v "[Line]"
            $ Line = 0
        $ JubesX.Statup("Obed", 20, 1)
        $ JubesX.Statup("Obed", 70, 1)
        $ JubesX.Statup("Inbt", 80, 2)
        jump Jubes_TJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ JubesX.FaceChange("angry")
        if "no titjob" in JubesX.RecentActions:
            ch_v "I {i}just{/i} told you \"no,\" [JubesX.Petname]."
        elif Taboo and "tabno" in JubesX.DailyActions and "no titjob" in JubesX.DailyActions:
            ch_v "This is just way too exposed!"
        elif "no titjob" in JubesX.DailyActions:
            ch_v "I already told you \"no,\" [JubesX.Petname]."
        elif Taboo and "tabno" in JubesX.DailyActions:
            ch_v "This is just way too exposed!"
        elif not JubesX.Tit:
            $ JubesX.FaceChange("bemused")
            ch_v "I'm not really into that, [JubesX.Petname]. . ."
        else:
            $ JubesX.FaceChange("bemused")
            ch_v "Not right now [JubesX.Petname]. . ."

        menu:
            extend ""
            "Sorry, never mind." if "no titjob" in JubesX.DailyActions:
                $ JubesX.FaceChange("bemused")
                ch_v "Yeah, ok, [JubesX.Petname]."
                return
            "Maybe later?" if "no titjob" not in JubesX.DailyActions:
                $ JubesX.FaceChange("sexy")
                ch_v "Maybe."
                $ JubesX.Statup("Love", 80, 2)
                $ JubesX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ JubesX.RecentActions.append("tabno")
                    $ JubesX.DailyActions.append("tabno")
                $ JubesX.RecentActions.append("no titjob")
                $ JubesX.DailyActions.append("no titjob")
                return
            "I think this could be fun for both of us. . .":
                if Approval:
                    $ JubesX.FaceChange("sexy")
                    $ JubesX.Statup("Obed", 80, 2)
                    $ JubesX.Statup("Obed", 40, 2)
                    $ JubesX.Statup("Inbt", 70, 3)
                    $ JubesX.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Well, ok, put it here.",
                        "Well. . . ok.",
                        "I guess.",
                        "I guess, whip it out.",
                        "Fine. . . [She drools a bit into her cleavage].",
                        "Heh, ok."])
                    ch_v "[Line]"
                    $ Line = 0
                    jump Jubes_TJ_Prep
                else:
                    $ Approval = ApprovalCheck(JubesX, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)             Handy instead?
                    if Approval >= 2 and JubesX.Blow:
                        $ JubesX.Statup("Inbt", 80, 1)
                        $ JubesX.Statup("Inbt", 60, 3)
                        $ JubesX.FaceChange("confused", 1)
                        ch_v "I could maybe blow you?"
                        menu:
                            ch_v "How about that [[blowjob]?"
                            "Ok, get down there.":
                                $ JubesX.Statup("Love", 80, 2)
                                $ JubesX.Statup("Inbt", 60, 1)
                                $ JubesX.Statup("Obed", 50, 1)
                                jump Jubes_BJ_Prep
                            "Nah, it's all about dem titties.":
                                $ Line = "no BJ"
                    if Approval and JubesX.Hand:
                        $ JubesX.Statup("Inbt", 80, 1)
                        $ JubesX.Statup("Inbt", 60, 3)
                        $ JubesX.FaceChange("confused", 1)
                        ch_v "I could give you a handy?"
                        menu:
                            ch_v "What do you say?"
                            "Sure, that's fine.":
                                $ JubesX.Statup("Love", 80, 2)
                                $ JubesX.Statup("Inbt", 60, 1)
                                $ JubesX.Statup("Obed", 50, 1)
                                jump Jubes_HJ_Prep
                            "Seriously, titties." if Line == "no BJ":
                                $ Line = 0
                            "Nah, it's all about dem titties." if Line != "no BJ":
                                pass
                    $ JubesX.Statup("Love", 200, -2)
                    ch_v "Nah."
                    $ JubesX.Statup("Obed", 70, 2)


            "Come on, let me fuck those titties, [JubesX.Pet]":                                               # Pressured into it
                $ JubesX.NameCheck() #checks reaction to petname
                $ Approval = ApprovalCheck(JubesX, 700, "OI", TabM = 4) # 70, 85, 100, -160(230)
                if Approval > 1 or (Approval and JubesX.Forced):
                    $ JubesX.FaceChange("sad")
                    $ JubesX.Statup("Love", 70, -5, 1)
                    $ JubesX.Statup("Love", 200, -2)
                    ch_v "Ok, fine, whip it out."
                    $ JubesX.Statup("Obed", 50, 4)
                    $ JubesX.Statup("Inbt", 80, 1)
                    $ JubesX.Statup("Inbt", 60, 3)
                    $ JubesX.Forced = 1
                    jump Jubes_TJ_Prep
                else:
                    $ JubesX.Statup("Love", 200, -15)
                    $ JubesX.RecentActions.append("angry")
                    $ JubesX.DailyActions.append("angry")

    #She refused all offers.
    if "no titjob" in JubesX.DailyActions:
        $ JubesX.FaceChange("angry", 1)
        ch_v "Look, I already told you no."
        $ JubesX.RecentActions.append("angry")
        $ JubesX.DailyActions.append("angry")
    elif JubesX.Forced:
        $ JubesX.FaceChange("angry", 1)
        ch_v "No, try something else."
        $ JubesX.Statup("Lust", 200, 5)
        if JubesX.Love > 300:
                $ JubesX.Statup("Love", 70, -2)
        $ JubesX.Statup("Obed", 50, -2)
        $ JubesX.RecentActions.append("angry")
        $ JubesX.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ JubesX.FaceChange("angry", 1)
        $ JubesX.DailyActions.append("tabno")
        ch_v "You really expect me to do that here? This isn't exactly \"covert.\""
        $ JubesX.Statup("Lust", 200, 5)
        $ JubesX.Statup("Obed", 50, -3)
    elif JubesX.Tit:
        $ JubesX.FaceChange("sad")
        ch_v "You'll know when it's time for that."
    else:
        $ JubesX.FaceChange("normal", 1)
        ch_v "Nah."
    $ JubesX.RecentActions.append("no titjob")
    $ JubesX.DailyActions.append("no titjob")
    $ temp_modifier = 0
    return

label Jubes_TJ_Prep:
    #fix remove
    "This option is currently unavailable. It will be added in a later update."
    return
    #fix remove

    if Taboo:
        $ JubesX.Inbt += int(Taboo/10)
        $ JubesX.Lust += int(Taboo/5)


    $ JubesX.FaceChange("sexy")
    if JubesX.Forced:
        $ JubesX.FaceChange("sad")
    elif not JubesX.Tit:
        $ JubesX.Brows = "confused"
        $ JubesX.Eyes = "sexy"
        $ JubesX.Mouth = "smile"

    call Seen_First_Peen(JubesX,Partner,React=Situation)
    call Jubes_TJ_Launch("L")

    if Situation == JubesX:
            #Jubes auto-starts
            $ Situation = 0
            "[JubesX.Name] slides down and sandwiches your dick between her tits."
            menu:
                "What do you do?"
                "Nothing.":
                    $ JubesX.Statup("Inbt", 80, 3)
                    $ JubesX.Statup("Inbt", 40, 2)
                    "[JubesX.Name] starts to slide them up and down."
                "Praise her.":
                    $ JubesX.FaceChange("sexy", 1)
                    $ JubesX.Statup("Inbt", 80, 3)
                    ch_p "Oh, that sounds like a good idea, [JubesX.Pet]."
                    $ JubesX.NameCheck() #checks reaction to petname
                    "[JubesX.Name] continues her actions."
                    $ JubesX.Statup("Love", 85, 1)
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ JubesX.FaceChange("confused")
                    $ JubesX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [JubesX.Pet]."
                    $ JubesX.NameCheck() #checks reaction to petname
                    "[JubesX.Name] lets it drop out from between her breasts."
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Obed", 50, 3)
                    $ Player.RecentActions.append("nope")
                    $ JubesX.AddWord(1,"refused","refused")
                    return

    if not JubesX.Tit:
        if JubesX.Forced:
            $ JubesX.Statup("Love", 90, -25)
            $ JubesX.Statup("Obed", 70, 30)
            $ JubesX.Statup("Inbt", 80, 35)
        else:
            $ JubesX.Statup("Love", 90, 5)
            $ JubesX.Statup("Obed", 70, 25)
            $ JubesX.Statup("Inbt", 80, 30)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ JubesX.DrainWord("tabno")
    $ JubesX.DrainWord("no titjob")
    $ JubesX.RecentActions.append("titjob")
    $ JubesX.DailyActions.append("titjob")

label Jubes_TJ_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(JubesX)
        call Jubes_TJ_Launch
        $ JubesX.LustFace()

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
                                            if JubesX.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ JubesX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")

                                    "Shift primary action":
                                            if JubesX.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                if JubesX.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Jubes_TJ_After
                                                                    call Jubes_Blowjob
                                                                else:
                                                                    call Sex_Basic_Dialog(JubesX,"tired")

                                                        "How about a handy?":
                                                                if JubesX.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Jubes_BJ_After
                                                                    call Jubes_Handjob
                                                                else:
                                                                    call Sex_Basic_Dialog(JubesX,"tired")
                                                        "Never Mind":
                                                                jump Jubes_TJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")

        #End menu (if Line)

        call Shift_Focus(JubesX)
        call Sex_Dialog(JubesX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JubesX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JubesX)
                            if "angry" in JubesX.RecentActions:
                                call Jubes_TJ_Reset
                                return
                            $ JubesX.Statup("Lust", 200, 5)
                            if 100 > JubesX.Lust >= 70 and JubesX.OCount < 2 and JubesX.SEXP >= 20:
                                $ JubesX.RecentActions.append("unsatisfied")
                                $ JubesX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jubes_TJ_After
                            $ Line = "came"

                    if JubesX.Lust >= 100:
                            #If Jubes can cum
                            call Girl_Cumming(JubesX)
                            if Situation == "shift" or "angry" in JubesX.RecentActions:
                                jump Jubes_TJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in JubesX.RecentActions:#And Jubes is unsatisfied,
                                "[JubesX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Jubes_TJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        if Speed >= 4:
                call Speed_Shift(0) #resets speed after orgasm
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if JubesX.SEXP >= 100 or ApprovalCheck(JubesX, 1200, "LO"):
                pass
        elif Cnt == (5 + JubesX.Tit):
                $ JubesX.Brows = "confused"
                ch_v "Are you getting close here? I'm getting bored."
        if Cnt == (10 + JubesX.Tit):
                $ JubesX.Brows = "angry"
                menu:
                    ch_v "Seriously, can we do something else?"
                    "How about a BJ?" if JubesX.Action and MultiAction:
                        $ Situation = "shift"
                        call Jubes_TJ_After
                        call Jubes_Blowjob
                        return
                    "Finish up." if Player.FocusX:
                        "You release your concentration. . ."
                        $ Player.FocusX = 0
                        $ Player.Focus += 15
                        jump Jubes_TJ_Cycle
                    "Let's try something else." if MultiAction:
                        $ Line = 0
                        call Jubes_TJ_Reset
                        $ Situation = "shift"
                        jump Jubes_TJ_After
                    "No, get back down there.":
                        if ApprovalCheck(JubesX, 1200) or ApprovalCheck(JubesX, 500, "O"):
                            $ JubesX.Statup("Love", 200, -5)
                            $ JubesX.Statup("Obed", 50, 3)
                            $ JubesX.Statup("Obed", 80, 2)
                            "She grumbles but gets back to work."
                        else:
                            $ JubesX.FaceChange("angry", 1)
                            "She scowls at you, drops you cock and pulls back."
                            ch_v "Well fuck you then."
                            $ JubesX.Statup("Love", 50, -3, 1)
                            $ JubesX.Statup("Love", 80, -4, 1)
                            $ JubesX.Statup("Obed", 30, -1, 1)
                            $ JubesX.Statup("Obed", 50, -1, 1)
                            $ JubesX.RecentActions.append("angry")
                            $ JubesX.DailyActions.append("angry")
                            jump Jubes_TJ_After
            #End Count check

        call Escalation(JubesX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(JubesX,10) #"I could use a break soon. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(JubesX,5)   #". . . I could really use a break here. . ."

    #Round = 0 loop breaks
    $ JubesX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(JubesX,"done") # ch_s "Ok, that's it, I need a break."

label Jubes_TJ_After:
    $ JubesX.FaceChange("sexy")

    $ JubesX.Tit += 1
    $ JubesX.Action -=1
    $ JubesX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ JubesX.Addictionrate += 1

    call Partner_Like(JubesX,4)

    if JubesX.Tit > 5:
        pass
    elif JubesX.Tit == 1:
        $ JubesX.SEXP += 12
        if JubesX.Love >= 500:
            $ JubesX.Mouth = "smile"
            ch_v "That was fun."
        elif Player.Focus <= 20:
            $ JubesX.Mouth = "sad"
            ch_v "Well I hope you got something out of that."
    elif JubesX.Tit == 5:
            ch_v "You seem to enjoy that."

    $ temp_modifier = 0

    if Situation == "shift":
            ch_v "Mmm, so what else did you have in mind?"
    else:
            call Jubes_TJ_Reset
    call Checkout
    return

## end JubesX.Titjob //////////////////////////////////////////////////////////////////////



# JubesX.Blowjob //////////////////////////////////////////////////////////////////////

label Jubes_Blowjob:
    #fix remove
    "This option is currently unavailable. It will be added in a later update."
    return
    #fix remove

    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JubesX)
    if JubesX.Blow >= 7: # She loves it
        $ temp_modifier += 15
    elif JubesX.Blow >= 3: #You've done it before several times
        $ temp_modifier += 10
    elif JubesX.Blow: #You've done it before
        $ temp_modifier += 7

    if JubesX.Addict >= 75 and JubesX.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 25
    elif JubesX.Addict >= 75: #She's really strung out
        $ temp_modifier += 15

    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in JubesX.Traits:
        $ temp_modifier += (4*Taboo)
    if JubesX in Player.Harem or "sex friend" in JubesX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JubesX.Traits:
        $ temp_modifier -= 40
    if JubesX.ForcedCount and not JubesX.Forced:
        $ temp_modifier -= 5 * JubesX.ForcedCount

    if Taboo and "tabno" in JubesX.DailyActions:
        $ temp_modifier -= 10

    if "no blow" in JubesX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no blow" in JubesX.RecentActions else 0

    $ Approval = ApprovalCheck(JubesX, 1300, TabM = 4) # 130, 145, 160, Taboo -160(290)

    if not JubesX.Blow and "no blow" not in JubesX.RecentActions:
        $ JubesX.FaceChange("surprised", 2)
        $ JubesX.Mouth = "kiss"
        ch_v "You want me to suck your cock?"
        if JubesX.Hand:
            $ JubesX.Mouth = "smile"
            ch_v "Handjobs not enough now?"
        $ JubesX.Blush = 1

    if not JubesX.Blow and Approval:                                                 #First time dialog
        if JubesX.Forced:
            $ JubesX.FaceChange("sad")
            $ JubesX.Statup("Love", 70, -3, 1)
            $ JubesX.Statup("Love", 20, -2, 1)
        elif JubesX.Love >= (JubesX.Obed + JubesX.Inbt):
            $ JubesX.FaceChange("sexy")
            $ JubesX.Brows = "sad"
            $ JubesX.Mouth = "smile"
            ch_v "I have wondered how you taste."
        elif JubesX.Obed >= JubesX.Inbt:
            $ JubesX.FaceChange("normal")
            ch_v "If that's what you want. . ."
        elif JubesX.Addict >= 50:
            $ JubesX.FaceChange("manic", 1)
            ch_v "[[wipes away a little drool]"
        else: # Uninhibited
            $ JubesX.FaceChange("sad")
            $ JubesX.Mouth = "smile"
            ch_v "Huh. . ."
    elif Approval:                                                                       #Second time+ dialog
        if JubesX.Forced:
            $ JubesX.FaceChange("sad")
            $ JubesX.Statup("Love", 70, -3, 1)
            $ JubesX.Statup("Love", 20, -2, 1)
            ch_v "Again?"
        elif not Taboo and "tabno" in JubesX.DailyActions:
            ch_v "Hmm, this is private enough. . ."
        elif "blow" in JubesX.RecentActions:
            $ JubesX.FaceChange("sexy", 1)
            ch_v "Mmm, again? [[yawns]"
            jump Jubes_BJ_Prep
        elif "blow" in JubesX.DailyActions:
            $ JubesX.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",
                "Wear'in me out here.",
                "I must be too good at this.",
                "Let me get some saliva going.",
                "Didn't get enough earlier?"])
            ch_v "[Line]"
        elif JubesX.Blow < 3:
            $ JubesX.FaceChange("sexy", 1)
            $ JubesX.Brows = "confused"
            $ JubesX.Mouth = "kiss"
            ch_v "You'd like another blowjob?"
        else:
            $ JubesX.FaceChange("sexy", 1)
            $ JubesX.ArmPose = 2
            $ Line = renpy.random.choice(["You want me to [mimes blowing]?",
                "So you want another blowjob?",
                "You want me to lick you?",
                "You want me to suck you off?",
                "A little bj?"])
            ch_v "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if JubesX.Forced:
            $ JubesX.FaceChange("sad")
            $ JubesX.Statup("Obed", 90, 1)
            $ JubesX.Statup("Inbt", 60, 1)
            ch_v "Whatever."
        elif "no blow" in JubesX.DailyActions:
            ch_v "Fine. . ."
        else:
            $ JubesX.FaceChange("sexy", 1)
            $ JubesX.Statup("Love", 90, 1)
            $ JubesX.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Sure. Ahhhhhh.",
                "Well. . . alright.",
                "Yum.",
                "Sure, whip it out.",
                "Ok. . . [She licks her lips].",
                "Alright, let's see it."])
            ch_v "[Line]"
            $ Line = 0
        $ JubesX.Statup("Obed", 20, 1)
        $ JubesX.Statup("Obed", 70, 1)
        $ JubesX.Statup("Inbt", 80, 2)
        jump Jubes_BJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ JubesX.FaceChange("angry")
        if "no blow" in JubesX.RecentActions:
            ch_v "Just told you I wouldn't, [JubesX.Petname]."
        elif Taboo and "tabno" in JubesX.DailyActions and "no blow" in JubesX.DailyActions:
            ch_v "Like I told you, not in public."
        elif "no blow" in JubesX.DailyActions:
            ch_v "Told you \"no,\" [JubesX.Petname]."
        elif Taboo and "tabno" in JubesX.DailyActions:
            ch_v "Like I told you, too public!"
        elif not JubesX.Blow:
            $ JubesX.FaceChange("bemused")
            ch_v "I don't know if your taste will match your scent, [JubesX.Petname]. . ."
        else:
            $ JubesX.FaceChange("bemused")
            ch_v "I don't know, [JubesX.Petname]!"
        menu:
            extend ""
            "Sorry, never mind." if "no blow" in JubesX.DailyActions:
                $ JubesX.FaceChange("bemused")
                ch_v "Cool."
                return
            "Maybe later?" if "no blow" not in JubesX.DailyActions:
                $ JubesX.FaceChange("sexy")
                ch_v "Yeah, maybe, [JubesX.Petname]."
                $ JubesX.Statup("Love", 80, 2)
                $ JubesX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ JubesX.RecentActions.append("tabno")
                    $ JubesX.DailyActions.append("tabno")
                $ JubesX.RecentActions.append("no blow")
                $ JubesX.DailyActions.append("no blow")
                return
            "Come on, please?":
                if Approval:
                    $ JubesX.FaceChange("sexy")
                    $ JubesX.Statup("Obed", 90, 2)
                    $ JubesX.Statup("Obed", 50, 2)
                    $ JubesX.Statup("Inbt", 70, 3)
                    $ JubesX.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Sure. Ahhhhhh.",
                        "Well. . . alright.",
                        "Yum.",
                        "Sure, whip it out.",
                        "Ok. . . [She licks her lips].",
                        "Alright, let's see it."])
                    ch_v "[Line]"
                    $ Line = 0
                    jump Jubes_BJ_Prep
                else:
                    if ApprovalCheck(JubesX, 1100, TabM = 3): # 110, 125, 140, Taboo -120(230)             Handy instead?
                        $ JubesX.Statup("Inbt", 80, 1)
                        $ JubesX.Statup("Inbt", 60, 3)
                        $ JubesX.FaceChange("confused", 1)
                        $ JubesX.ArmPose = 2
                        if JubesX.Hand:
                            ch_v "Couldn't I just use my hand again?"
                            ch_v "You seemed to like that."
                        else:
                            ch_v "I could maybe use my hand instead, how's that sound?"
                        menu:
                            extend ""
                            "Sure, that's fine.":
                                $ JubesX.Statup("Love", 80, 2)
                                $ JubesX.Statup("Inbt", 60, 1)
                                $ JubesX.Statup("Obed", 50, 1)
                                jump Jubes_HJ_Prep
                            "Nah, if it's not a BJ, forget it.":
                                $ JubesX.Statup("Love", 200, -2)
                                $ JubesX.ArmPose = 1
                                ch_v "Fine, be that way."
                                $ JubesX.Statup("Obed", 70, 2)


            "Suck it, [JubesX.Pet]":                                               # Pressured into it
                $ JubesX.NameCheck() #checks reaction to petname
                $ Approval = ApprovalCheck(JubesX, 750, "OI", TabM = 3) # 75, 90, 105, -120(195)
                if Approval > 1 or (Approval and JubesX.Forced):
                    $ JubesX.FaceChange("sad")
                    $ JubesX.Statup("Love", 70, -5, 1)
                    $ JubesX.Statup("Love", 200, -2)
                    ch_v "Whatever. . ."
                    $ JubesX.Statup("Obed", 50, 4)
                    $ JubesX.Statup("Inbt", 80, 1)
                    $ JubesX.Statup("Inbt", 60, 3)
                    $ JubesX.Forced = 1
                    jump Jubes_BJ_Prep
                else:
                    $ JubesX.Statup("Love", 200, -15)
                    $ JubesX.RecentActions.append("angry")
                    $ JubesX.DailyActions.append("angry")

    #She refused all offers.
    if "no blow" in JubesX.DailyActions:
        $ JubesX.FaceChange("angry", 1)
        $ JubesX.ArmPose = 2
        $ JubesX.Claws = 1
        ch_v "Suck this then."
        $ JubesX.ArmPose = 1
        $ JubesX.Claws = 0
        $ JubesX.RecentActions.append("angry")
        $ JubesX.DailyActions.append("angry")
    elif JubesX.Forced:
        $ JubesX.FaceChange("angry", 1)
        ch_v "That's just pushing it."
        $ JubesX.Statup("Lust", 200, 5)
        if JubesX.Love > 300:
                $ JubesX.Statup("Love", 70, -2)
        $ JubesX.Statup("Obed", 50, -2)
        $ JubesX.RecentActions.append("angry")
        $ JubesX.DailyActions.append("angry")
        $ JubesX.RecentActions.append("no blow")
        $ JubesX.DailyActions.append("no blow")
        return
    elif Taboo:                             # she refuses and this is too public a place for her
        $ JubesX.FaceChange("angry", 1)
        $ JubesX.DailyActions.append("tabno")
        ch_v "This area's too exposed."
        $ JubesX.Statup("Lust", 200, 5)
        $ JubesX.Statup("Obed", 50, -3)
        return
    elif JubesX.Blow:
        $ JubesX.FaceChange("sad")
        ch_v "Nah, not this time."
    else:
        $ JubesX.FaceChange("normal", 1)
        ch_v "Nope."
    $ JubesX.RecentActions.append("no blow")
    $ JubesX.DailyActions.append("no blow")
    $ temp_modifier = 0
    return


label Jubes_BJ_Prep:
    #fix remove
    "This option is currently unavailable. It will be added in a later update."
    return
    #fix remove

    if renpy.showing("Jubes_HJ_Animation"):
        hide Jubes_HJ_Animation with easeoutbottom
    if Taboo:
        $ JubesX.Inbt += int(Taboo/10)
        $ JubesX.Lust += int(Taboo/5)

    $ JubesX.FaceChange("sexy")
    if JubesX.Forced:
        $ JubesX.FaceChange("sad")
    elif not JubesX.Blow:
        $ JubesX.Brows = "confused"
        $ JubesX.Eyes = "sexy"
        $ JubesX.Mouth = "smile"

    call Seen_First_Peen(JubesX,Partner,React=Situation)
    call Jubes_BJ_Launch("L")
    if Situation == JubesX:
            #Jubes auto-starts
            $ Situation = 0
            "[JubesX.Name] slides down and gives your cock a little lick."
            menu:
                "What do you do?"
                "Nothing.":
                    $ JubesX.Statup("Inbt", 80, 3)
                    $ JubesX.Statup("Inbt", 40, 2)
                    "[JubesX.Name] continues licking at it."
                "Praise her.":
                    $ JubesX.FaceChange("sexy", 1)
                    $ JubesX.Statup("Inbt", 80, 3)
                    ch_p "Hmmm, keep doing that, [JubesX.Pet]."
                    $ JubesX.NameCheck() #checks reaction to petname
                    "[JubesX.Name] continues her actions."
                    $ JubesX.Statup("Love", 85, 1)
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ JubesX.FaceChange("surprised")
                    $ JubesX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [JubesX.Pet]."
                    $ JubesX.NameCheck() #checks reaction to petname
                    "[JubesX.Name] puts it down."
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Obed", 50, 3)
                    $ Player.RecentActions.append("nope")
                    $ JubesX.AddWord(1,"refused","refused")
                    return
    if not JubesX.Blow:
        if JubesX.Forced:
            $ JubesX.Statup("Love", 90, -70)
            $ JubesX.Statup("Obed", 70, 45)
            $ JubesX.Statup("Inbt", 80, 60)
        else:
            $ JubesX.Statup("Love", 90, 5)
            $ JubesX.Statup("Obed", 70, 35)
            $ JubesX.Statup("Inbt", 80, 40)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ JubesX.DrainWord("tabno")
    $ JubesX.DrainWord("no blow")
    $ JubesX.RecentActions.append("blow")
    $ JubesX.DailyActions.append("blow")

label Jubes_BJ_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(JubesX)
        call Jubes_BJ_Launch
        $ JubesX.LustFace()

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

                                if "Gwentro" not in JubesX.History: #calls the special Gwentro event
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
                                "[JubesX.Name] hums contentedly."
                                if "setpace" not in JubesX.RecentActions:
                                    $ JubesX.Statup("Love", 80, 2)
                                $ D20 = renpy.random.randint(1, 20)
                                if JubesX.Blow < 5:
                                    $ D20 -= 10
                                elif JubesX.Blow < 10:
                                    $ D20 -= 5

                                if D20 > 15:
                                    call Speed_Shift(4)
                                    if "setpace" not in JubesX.RecentActions:
                                        $ JubesX.Statup("Inbt", 80, 3)
                                elif D20 > 10:
                                    call Speed_Shift(3)
                                elif D20 > 5:
                                    call Speed_Shift(2)
                                else:
                                    call Speed_Shift(1)
                                $ JubesX.RecentActions.append("setpace")

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
                                            if JubesX.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ JubesX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")

                                    "Shift primary action":
                                            if JubesX.Action and MultiAction:
                                                    menu:
                                                        "How about a handy?":
                                                                if JubesX.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Jubes_BJ_After
                                                                    call Jubes_Handjob
                                                                else:
                                                                    ch_v "I need a break, can we wrap on this?"
                                                        "How about a titjob?":
                                                                if JubesX.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Jubes_BJ_After
                                                                    call Jubes_Titjob
                                                                else:
                                                                    ch_v "I need a break, can we wrap on this?"
                                                        "Never Mind":
                                                                jump Jubes_BJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")

        #End menu (if Line)

        call Shift_Focus(JubesX)
        call Sex_Dialog(JubesX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1
        if Speed:
            $ Player.Wet = 1 #wets penis
            $ Player.Spunk = 0 if Player.Spunk else Player.Spunk #cleans you off after one cycle

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JubesX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JubesX)
                            if "angry" in JubesX.RecentActions:
                                call Jubes_BJ_Reset
                                return
                            $ JubesX.Statup("Lust", 200, 5)
                            if 100 > JubesX.Lust >= 70 and JubesX.OCount < 2 and JubesX.SEXP >= 20:
                                $ JubesX.RecentActions.append("unsatisfied")
                                $ JubesX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jubes_BJ_After
                            $ Line = "came"

                    if JubesX.Lust >= 100:
                            #If Jubes can cum
                            call Girl_Cumming(JubesX)
                            if Situation == "shift" or "angry" in JubesX.RecentActions:
                                jump Jubes_BJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."

                            if "unsatisfied" in JubesX.RecentActions:#And Jubes is unsatisfied,
                                "[JubesX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Jubes_BJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if JubesX.SEXP >= 100 or ApprovalCheck(JubesX, 1200, "LO"):
            pass
        elif Cnt == (10 + JubesX.Blow):
                $ JubesX.Brows = "angry"
                menu:
                    ch_v "I'm getting kinda bored. Can we do something else?"
                    "How about a Handy?" if JubesX.Action and MultiAction:
                            $ Situation = "shift"
                            call Jubes_BJ_After
                            call Jubes_Handjob
                            return
                    "Finish up." if Player.FocusX:
                            "You release your concentration. . ."
                            $ Player.FocusX = 0
                            $ Player.Focus += 15
                            jump Jubes_BJ_Cycle
                    "Let's try something else." if MultiAction:
                            $ Line = 0
                            call Jubes_BJ_Reset
                            $ Situation = "shift"
                            jump Jubes_BJ_After
                    "No, get back down there.":
                            if ApprovalCheck(JubesX, 1200) or ApprovalCheck(JubesX, 500, "O"):
                                $ JubesX.Statup("Love", 200, -5)
                                $ JubesX.Statup("Obed", 50, 3)
                                $ JubesX.Statup("Obed", 80, 2)
                                "She grumbles but gets back to work."
                            else:
                                $ JubesX.FaceChange("angry", 1)
                                "She scowls at you, drops you cock and pulls back."
                                ch_v "Well fuck you then."
                                $ JubesX.Statup("Love", 50, -3, 1)
                                $ JubesX.Statup("Love", 80, -4, 1)
                                $ JubesX.Statup("Obed", 30, -1, 1)
                                $ JubesX.Statup("Obed", 50, -1, 1)
                                $ JubesX.RecentActions.append("angry")
                                $ JubesX.DailyActions.append("angry")
                                jump Jubes_BJ_After
        elif Cnt == (5 + JubesX.Blow) and JubesX.SEXP <= 100 and not ApprovalCheck(JubesX, 1200, "LO"):
                    $ JubesX.Brows = "confused"
                    ch_v "Are you getting close here? I'm bored."
        #End Count check

        call Escalation(JubesX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(JubesX,10) #"I could use a break soon. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(JubesX,5)   #". . . I could really use a break here. . ."

    #Round = 0 loop breaks
    $ JubesX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(JubesX,"done") # ch_s "Ok, that's it, I need a break."

label Jubes_BJ_After:
    $ JubesX.FaceChange("sexy")

    $ JubesX.Blow += 1
    $ JubesX.Action -=1
    $ JubesX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ JubesX.Addictionrate += 1

    call Partner_Like(JubesX,2)

    if "Jubes Jobber" in Achievements:
        pass
    elif JubesX.Blow >= 10:
        $ JubesX.FaceChange("smile", 1)
        ch_v "Your flavor is intoxicating."
        $ Achievements.append("Jubes Jobber")
        $JubesX.SEXP += 5
    elif Situation == "shift":
        pass
    elif JubesX.Blow == 1:
            $JubesX.SEXP += 15
            if JubesX.Love >= 500:
                $ JubesX.Mouth = "smile"
                ch_v "Hey, whaddaya know, that wasn't bad."
            elif Player.Focus <= 20:
                $ JubesX.Mouth = "sad"
                ch_v "I hope you enjoyed that."
    elif JubesX.Blow == 5:
        ch_v "I'm really getting the hang of this. . . right?"
        menu:
            "[[nod]":
                $ JubesX.FaceChange("smile", 1)
                $ JubesX.Statup("Love", 90, 15)
                $ JubesX.Statup("Obed", 80, 5)
                $ JubesX.Statup("Inbt", 90, 10)
            "[[shake head \"no\"]":
                if ApprovalCheck(JubesX, 500, "O"):
                    $ JubesX.FaceChange("sad", 2)
                    $ JubesX.Statup("Love", 200, -5)
                else:
                    $ JubesX.FaceChange("angry", 2)
                    $ JubesX.Statup("Love", 200, -25)
                $ JubesX.Statup("Obed", 80, 10)
                ch_v ". . ."
                $ JubesX.FaceChange("sad", 1)

    $ temp_modifier = 0
    if Situation != "shift":
        call Jubes_BJ_Reset
    call Checkout
    return



# end JubesX.Blowjob                                 //////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy
label Jubes_Dildo_Check:
    if "dildo" in Player.Inventory:
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in JubesX.Inventory:
        "You ask [JubesX.Name] to get out her favorite Dildo."
    else:
        "You don't have one of those on you."
        return 0
    return 1

label Jubes_Dildo_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JubesX)
    call Jubes_Dildo_Check
    if not _return:
        return

    if JubesX.DildoP: #You've done it before
        $ temp_modifier += 15
    if JubesX.Legs == "pants:": # she's got pants on.
        $ temp_modifier -= 20

    if JubesX.Lust > 95:
        $ temp_modifier += 20
    elif JubesX.Lust > 85: #She's really horny
        $ temp_modifier += 15

    if Situation == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in JubesX.Traits:
        $ temp_modifier += (5*Taboo)
    if JubesX in Player.Harem or "sex friend" in JubesX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JubesX.Traits:
        $ temp_modifier -= 40
    if JubesX.ForcedCount and not JubesX.Forced:
        $ temp_modifier -= 5 * JubesX.ForcedCount

    if Taboo and "tabno" in JubesX.DailyActions:
        $ temp_modifier -= 10

    if "no dildo" in JubesX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no dildo" in JubesX.RecentActions else 0

    $ Approval = ApprovalCheck(JubesX, 1250, TabM = 4) # 125, 140, 155, Taboo -160(335)

    if Situation == JubesX:                                                                  #Jubes auto-starts
                if Approval > 2:                                                      # fix, add jubes auto stuff here
                    if JubesX.PantsNum() == 5:
                        "[JubesX.Name] grabs her dildo, hiking up her skirt as she does."
                        $ JubesX.Upskirt = 1
                    elif JubesX.PantsNum() >= 6:
                        "[JubesX.Name] grabs her dildo, pulling down her pants as she does."
                        $ JubesX.Legs = 0
                    else:
                        "[JubesX.Name] grabs her dildo, rubbing is suggestively against her crotch."
                    $ JubesX.SeenPanties = 1
                    call Jubes_First_Bottomless(1)
                    "She slides the tip along her pussy and seems to want you to insert it."
                    menu:
                        "What do you do?"
                        "Nothing.":
                            $ JubesX.Statup("Inbt", 80, 3)
                            $ JubesX.Statup("Inbt", 50, 2)
                            "[JubesX.Name] slides it in."
                        "Go for it.":
                            $ JubesX.FaceChange("sexy", 1)
                            $ JubesX.Statup("Inbt", 80, 3)
                            ch_p "Oh yeah, [JubesX.Pet], let's do this."
                            $ JubesX.NameCheck() #checks reaction to petname
                            "You grab the dildo and slide it in."
                            $ JubesX.Statup("Love", 85, 1)
                            $ JubesX.Statup("Obed", 90, 1)
                            $ JubesX.Statup("Obed", 50, 2)
                        "Ask her to stop.":
                            $ JubesX.FaceChange("surprised")
                            $ JubesX.Statup("Inbt", 70, 1)
                            ch_p "Let's not do that right now, [JubesX.Pet]."
                            $ JubesX.NameCheck() #checks reaction to petname
                            "[JubesX.Name] sets the dildo down."
                            $ JubesX.OutfitChange()
                            $ JubesX.Statup("Obed", 90, 1)
                            $ JubesX.Statup("Obed", 50, 1)
                            $ JubesX.Statup("Obed", 30, 2)
                            return
                    jump Jubes_DP_Prep
                else:
                    $ temp_modifier = 0                               # fix, add jubes auto stuff here
                    $ Trigger2 = 0
                return

    if Situation == "auto":
                "You rub the dildo across her body, and along her moist slit."
                $ JubesX.FaceChange("surprised", 1)

                if (JubesX.DildoP and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
                    "[JubesX.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                    $ JubesX.FaceChange("sexy")
                    $ JubesX.Statup("Obed", 70, 3)
                    $ JubesX.Statup("Inbt", 50, 3)
                    $ JubesX.Statup("Inbt", 70, 1)
                    ch_v "Ooo, [JubesX.Petname], toys!"
                    jump Jubes_DP_Prep
                else:                                                                                                            #she's questioning it
                    $ JubesX.Brows = "angry"
                    menu:
                        ch_v "Hey, what are you planning to do with that?!"
                        "Sorry, sorry! Never mind.":
                            if Approval:
                                $ JubesX.FaceChange("sexy", 1)
                                $ JubesX.Statup("Obed", 70, 3)
                                $ JubesX.Statup("Inbt", 50, 3)
                                $ JubesX.Statup("Inbt", 70, 1)
                                ch_v "Well, now that you mention it. . ."
                                jump Jubes_DP_Prep
                            "You pull back before you really get it in."
                            $ JubesX.FaceChange("bemused", 1)
                            if JubesX.DildoP:
                                ch_v "Well ok, [JubesX.Petname], maybe warn me next time?"
                            else:
                                ch_v "Well ok, [JubesX.Petname], that's a little much. . . for now . . ."
                        "Just playing with my favorite toys.":
                            $ JubesX.Statup("Love", 80, -10, 1)
                            $ JubesX.Statup("Love", 200, -10)
                            "You press it inside some more."
                            $ JubesX.Statup("Obed", 70, 3)
                            $ JubesX.Statup("Inbt", 50, 3)
                            if not ApprovalCheck(JubesX, 700, "O", TabM=1): #Checks if Obed is 700+
                                $ JubesX.FaceChange("angry")
                                "[JubesX.Name] shoves you away and slaps you in the face."
                                ch_v "Jerk!"
                                ch_v "Ask nice if you want to stick something in my pussy!"
                                $ JubesX.Statup("Love", 50, -10, 1)
                                $ JubesX.Statup("Obed", 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                if renpy.showing("Jubes_SexSprite"):
                                    call Jubes_Sex_Reset
                                $ JubesX.RecentActions.append("angry")
                                $ JubesX.DailyActions.append("angry")
                            else:
                                $ JubesX.FaceChange("sad")
                                "[JubesX.Name] doesn't seem to be into this, you're lucky she's so obedient."
                                jump Jubes_DP_Prep
                return
    #end Auto

    if not JubesX.DildoP:
            #first time
            $ JubesX.FaceChange("surprised", 1)
            $ JubesX.Mouth = "kiss"
            ch_v "Hmmm, so you'd like to try out some toys?"
            if JubesX.Forced:
                $ JubesX.FaceChange("sad")
                ch_v "I suppose there are worst things you could ask for."

    if not JubesX.DildoP and Approval:
            #First time dialog
            if JubesX.Forced:
                $ JubesX.FaceChange("sad")
                $ JubesX.Statup("Love", 70, -3, 1)
                $ JubesX.Statup("Love", 20, -2, 1)
            elif JubesX.Love >= (JubesX.Obed + JubesX.Inbt):
                $ JubesX.FaceChange("sexy")
                $ JubesX.Brows = "sad"
                $ JubesX.Mouth = "smile"
                ch_v "I've had a reasonable amount of experience with these, you know. . ."
            elif JubesX.Obed >= JubesX.Inbt:
                $ JubesX.FaceChange("normal")
                ch_v "If that's what you want, [JubesX.Petname]. . ."
            else: # Uninhibited
                $ JubesX.FaceChange("sad")
                $ JubesX.Mouth = "smile"
                ch_v "I guess it could be fun with a partner. . ."

    elif Approval:
            #Second time+ dialog
            if JubesX.Forced:
                $ JubesX.FaceChange("sad")
                $ JubesX.Statup("Love", 70, -3, 1)
                $ JubesX.Statup("Love", 20, -2, 1)
                ch_v "The toys again?"
            elif not Taboo and "tabno" in JubesX.DailyActions:
                ch_v "Well, at least you got us some privacy this time. . ."
            elif "dildo pussy" in JubesX.RecentActions:
                $ JubesX.FaceChange("sexy", 1)
                ch_v "Mmm, again? Ok, let's get to it."
                jump Jubes_DP_Prep
            elif "dildo pussy" in JubesX.DailyActions:
                $ JubesX.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Breaking out the toys again?",
                    "Didn't get enough earlier?",
                    "You're going to wear me out."])
                ch_v "[Line]"
            elif JubesX.DildoP < 3:
                $ JubesX.FaceChange("sexy", 1)
                $ JubesX.Brows = "confused"
                $ JubesX.Mouth = "kiss"
                ch_v "You want to stick it in my pussy again?"
            else:
                $ JubesX.FaceChange("sexy", 1)
                $ JubesX.ArmPose = 2
                $ Line = renpy.random.choice(["You want some of this action?",
                    "So you'd like another go?",
                    "You want to stick it in my pussy again?",
                    "You want me ta lube up your toy?"])
                ch_v "[Line]"
                $ Line = 0

    if Approval >= 2:
            #She's into it. . .
            if JubesX.Forced:
                $ JubesX.FaceChange("sad")
                $ JubesX.Statup("Obed", 90, 1)
                $ JubesX.Statup("Inbt", 60, 1)
                ch_v "Ok, fine."
            else:
                $ JubesX.FaceChange("sexy", 1)
                $ JubesX.Statup("Love", 90, 1)
                $ JubesX.Statup("Inbt", 50, 3)
                $ Line = renpy.random.choice(["Well, sure, stick it in.",
                    "Well. . . ok.",
                    "Sure!",
                    "I guess I could. . . stick it in.",
                    "Hells yeah.",
                    "Heh, ok, ok."])
                ch_v "[Line]"
                $ Line = 0
            $ JubesX.Statup("Obed", 20, 1)
            $ JubesX.Statup("Obed", 60, 1)
            $ JubesX.Statup("Inbt", 70, 2)
            jump Jubes_DP_Prep

    else:
            #She's not into it, but maybe. . .
            $ JubesX.FaceChange("angry")
            if "no dildo" in JubesX.RecentActions:
                ch_v "What part of \"no,\" did you not get, [JubesX.Petname]?"
            elif Taboo and "tabno" in JubesX.DailyActions and "no dildo" in JubesX.DailyActions:
                ch_v "Stop swinging that thing around in public!"
            elif "no dildo" in JubesX.DailyActions:
                ch_v "I already told you \"no,\" [JubesX.Petname]."
            elif Taboo and "tabno" in JubesX.DailyActions:
                ch_v "Stop swinging that thing around in public!"
            elif not JubesX.DildoP:
                $ JubesX.FaceChange("bemused")
                ch_v "I'm just not into toys, [JubesX.Petname]. . ."
            else:
                $ JubesX.FaceChange("bemused")
                ch_v "I don't think we need any toys, [JubesX.Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in JubesX.DailyActions:
                    $ JubesX.FaceChange("bemused")
                    ch_v "Yeah, ok, [JubesX.Petname]."
                    return
                "Maybe later?" if "no dildo" not in JubesX.DailyActions:
                    $ JubesX.FaceChange("sexy")
                    ch_v "Maybe I'll practice on my own time, [JubesX.Petname]."
                    $ JubesX.Statup("Love", 80, 2)
                    $ JubesX.Statup("Inbt", 70, 2)
                    if Taboo:
                        $ JubesX.RecentActions.append("tabno")
                        $ JubesX.DailyActions.append("tabno")
                    $ JubesX.RecentActions.append("no dildo")
                    $ JubesX.DailyActions.append("no dildo")
                    return
                "I think you'd like it. . .":
                    if Approval:
                        $ JubesX.FaceChange("sexy")
                        $ JubesX.Statup("Obed", 90, 2)
                        $ JubesX.Statup("Obed", 50, 2)
                        $ JubesX.Statup("Inbt", 70, 3)
                        $ JubesX.Statup("Inbt", 40, 2)
                        $ Line = renpy.random.choice(["Well, sure, stick it in.",
                            "I suppose. . .",
                            "You've got me there."])
                        ch_v "[Line]"
                        $ Line = 0
                        jump Jubes_DP_Prep
                    else:
                        pass

                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck(JubesX, 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                    if Approval > 1 or (Approval and JubesX.Forced):
                        $ JubesX.FaceChange("sad")
                        $ JubesX.Statup("Love", 70, -5, 1)
                        $ JubesX.Statup("Love", 200, -5)
                        ch_v "Ok, fine. If we're going to do this, stick it in already."
                        $ JubesX.Statup("Obed", 80, 4)
                        $ JubesX.Statup("Inbt", 80, 1)
                        $ JubesX.Statup("Inbt", 60, 3)
                        $ JubesX.Forced = 1
                        jump Jubes_DP_Prep
                    else:
                        $ JubesX.Statup("Love", 200, -20)
                        $ JubesX.RecentActions.append("angry")
                        $ JubesX.DailyActions.append("angry")

    #She refused all offers.
    $ JubesX.ArmPose = 1
    if "no dildo" in JubesX.DailyActions:
            ch_v "Learn to take \"no\" for an answer, [JubesX.Petname]."
            $ JubesX.RecentActions.append("angry")
            $ JubesX.DailyActions.append("angry")
    elif JubesX.Forced:
            $ JubesX.FaceChange("angry", 1)
            ch_v "I'm not going to let you use that on me."
            $ JubesX.Statup("Lust", 200, 5)
            if JubesX.Love > 300:
                    $ JubesX.Statup("Love", 70, -2)
            $ JubesX.Statup("Obed", 50, -2)
            $ JubesX.RecentActions.append("angry")
            $ JubesX.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
            $ JubesX.FaceChange("angry", 1)
            $ JubesX.RecentActions.append("tabno")
            $ JubesX.DailyActions.append("tabno")
            ch_v "Not here!"
            $ JubesX.Statup("Lust", 200, 5)
            $ JubesX.Statup("Obed", 50, -3)
    elif JubesX.DildoP:
            $ JubesX.FaceChange("sad")
            ch_v "Sorry, you can keep your toys to yourself."
    else:
            $ JubesX.FaceChange("normal", 1)
            ch_v "No way."
    $ JubesX.RecentActions.append("no dildo")
    $ JubesX.DailyActions.append("no dildo")
    $ temp_modifier = 0
    return

label Jubes_DP_Prep: #Animation set-up
    if Trigger2 == "dildo pussy":
        return

    if not JubesX.Forced and Situation != "auto":
        $ temp_modifier = 15 if JubesX.PantsNum() >= 6 else 0
        call Bottoms_Off(JubesX)
        if "angry" in JubesX.RecentActions:
            return

    $ temp_modifier = 0
    call Jubes_Pussy_Launch("dildo pussy")
    if not JubesX.DildoP:
        if JubesX.Forced:
            $ JubesX.Statup("Love", 90, -75)
            $ JubesX.Statup("Obed", 70, 60)
            $ JubesX.Statup("Inbt", 80, 35)
        else:
            $ JubesX.Statup("Love", 90, 10)
            $ JubesX.Statup("Obed", 70, 20)
            $ JubesX.Statup("Inbt", 80, 45)
    if Taboo:
        $ JubesX.Inbt += int(Taboo/10)
        $ JubesX.Lust += int(Taboo/5)


    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ JubesX.DrainWord("tabno")
    $ JubesX.DrainWord("no dildo")
    $ JubesX.RecentActions.append("dildo pussy")
    $ JubesX.DailyActions.append("dildo pussy")

label Jubes_DP_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(JubesX)
        call Jubes_Pussy_Launch("dildo pussy")
        $ JubesX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                call Slap_Ass(JubesX)
                                jump Jubes_DP_Cycle

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
                                            if JubesX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ JubesX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")

                                    "Shift primary action":
                                            if JubesX.Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in her ass.":
                                                                $ Situation = "shift"
                                                                call Jubes_DP_After
                                                                call Jubes_Insert_Ass
                                                        "Just stick a finger in her ass without asking.":
                                                                $ Situation = "auto"
                                                                call Jubes_DP_After
                                                                call Jubes_Insert_Ass
                                                        "I want to shift the dildo to her ass.":
                                                                $ Situation = "shift"
                                                                call Jubes_DP_After
                                                                call Jubes_Dildo_Ass
                                                        "Never Mind":
                                                                jump Jubes_DP_Cycle
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")

        #End menu (if Line)

        if JubesX.Panties or JubesX.PantsNum() >= 6 or JubesX.HoseNum() >= 5: #This checks if Jubes wants to strip down.
                call Girl_Undress(JubesX,"auto")

        call Shift_Focus(JubesX)
        call Sex_Dialog(JubesX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JubesX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JubesX)
                            if "angry" in JubesX.RecentActions:
                                call Jubes_Pos_Reset
                                return
                            $ JubesX.Statup("Lust", 200, 5)
                            if 100 > JubesX.Lust >= 70 and JubesX.OCount < 2:
                                $ JubesX.RecentActions.append("unsatisfied")
                                $ JubesX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jubes_DP_After
                            $ Line = "came"

                    if JubesX.Lust >= 100:
                            #If Jubes can cum
                            call Girl_Cumming(JubesX)
                            if Situation == "shift" or "angry" in JubesX.RecentActions:
                                jump Jubes_DP_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in JubesX.RecentActions:#And Jubes is unsatisfied,
                                "[JubesX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Jubes_DP_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if JubesX.SEXP >= 100 or ApprovalCheck(JubesX, 1200, "LO"):
            pass
        elif Cnt == (5 + JubesX.DildoP):
                    $ JubesX.Brows = "confused"
                    ch_v "What are you even doing down there?"
        elif JubesX.Lust >= 80:
                    pass
        elif Cnt == (15 + JubesX.DildoP) and JubesX.SEXP >= 15 and not ApprovalCheck(JubesX, 1500):
                    $ JubesX.Brows = "confused"
                    menu:
                        ch_v "[JubesX.Petname], this is getting uncomfortable, maybe we could try something else."
                        "Finish up.":
                                "You let go. . ."
                                jump Jubes_DP_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Jubes_DP_After
                        "No, this is fun.":
                                if ApprovalCheck(JubesX, 1200) or ApprovalCheck(JubesX, 500, "O"):
                                    $ JubesX.Statup("Love", 200, -5)
                                    $ JubesX.Statup("Obed", 50, 3)
                                    $ JubesX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ JubesX.FaceChange("angry", 1)
                                    call Jubes_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_v "Well if that's your attitude, I don't need your \"help\"."
                                    $ JubesX.Statup("Love", 50, -3, 1)
                                    $ JubesX.Statup("Love", 80, -4, 1)
                                    $ JubesX.Statup("Obed", 30, -1, 1)
                                    $ JubesX.Statup("Obed", 50, -1, 1)
                                    $ JubesX.RecentActions.append("angry")
                                    $ JubesX.DailyActions.append("angry")
                                    jump Jubes_DP_After
        #End Count check

        if Round == 10:
                call Sex_Basic_Dialog(JubesX,10) #"I could use a break soon. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(JubesX,5)   #". . . I could really use a break here. . ."

    #Round = 0 loop breaks
    $ JubesX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(JubesX,"done") # ch_s "Ok, that's it, I need a break."


label Jubes_DP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Jubes_Pos_Reset

    $ JubesX.FaceChange("sexy")

    $ JubesX.DildoP += 1
    $ JubesX.Action -=1

    call Partner_Like(JubesX,1)

    if JubesX.DildoP == 1:
            $ JubesX.SEXP += 10
            if not Situation:
                if JubesX.Love >= 500 and "unsatisfied" not in JubesX.RecentActions:
                    ch_v "Thanks for the extra hand. . ."
                elif JubesX.Obed <= 500 and Player.Focus <= 20:
                    $ JubesX.FaceChange("perplexed", 1)
                    ch_v "Did you like that?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_v "Mmm, so what else did you have in mind?"
    call Checkout
    return

# end JubesX.Dildo Pussy /////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////Start Insert Ass

label Jubes_Dildo_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JubesX)
    call Jubes_Dildo_Check
    if not _return:
        return

    if JubesX.Loose:
        $ temp_modifier += 30
    elif "anal" in JubesX.RecentActions or "dildo anal" in JubesX.RecentActions:
        $ temp_modifier -= 20
    elif "anal" in JubesX.DailyActions or "dildo anal" in JubesX.DailyActions:
        $ temp_modifier -= 10
    elif (JubesX.Anal + JubesX.DildoA + JubesX.Plug) > 0: #You've done it before
        $ temp_modifier += 20

    if JubesX.Legs == "pants:": # she's got pants on.
        $ temp_modifier -= 20

    if JubesX.Lust > 95:
        $ temp_modifier += 20
    elif JubesX.Lust > 85: #She's really horny
        $ temp_modifier += 15

    if Situation == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in JubesX.Traits:
        $ temp_modifier += (5*Taboo)
    if JubesX in Player.Harem or "sex friend" in JubesX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JubesX.Traits:
        $ temp_modifier -= 40
    if JubesX.ForcedCount and not JubesX.Forced:
        $ temp_modifier -= 5 * JubesX.ForcedCount

    if Taboo and "tabno" in JubesX.DailyActions:
        $ temp_modifier -= 10

    if "no dildo" in JubesX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no dildo" in JubesX.RecentActions else 0

    $ Approval = ApprovalCheck(JubesX, 1450, TabM = 4) # 145, 160, 175, Taboo -160(355)

    if Situation == JubesX:
            #Jubes auto-starts
            if Approval > 2:                                                      # fix, add jubes auto stuff here
                if JubesX.PantsNum() == 5:
                    "[JubesX.Name] grabs her dildo, hiking up her skirt as she does."
                    $ JubesX.Upskirt = 1
                elif JubesX.PantsNum() >= 6:
                    "[JubesX.Name] grabs her dildo, pulling down her pants as she does."
                    $ JubesX.Legs = 0
                else:
                    "[JubesX.Name] grabs her dildo, rubbing is suggestively against her ass."
                $ JubesX.SeenPanties = 1
                call Jubes_First_Bottomless(1)
                "She slides the tip against her asshole, and seems to want you to insert it."
                menu:
                    "What do you do?"
                    "Nothing.":
                        $ JubesX.Statup("Inbt", 80, 3)
                        $ JubesX.Statup("Inbt", 50, 2)
                        "[JubesX.Name] slides it in."
                    "Go for it.":
                        $ JubesX.FaceChange("sexy", 1)
                        $ JubesX.Statup("Inbt", 80, 3)
                        ch_p "Oh yeah, [JubesX.Pet], let's do this."
                        $ JubesX.NameCheck() #checks reaction to petname
                        "You grab the dildo and slide it in."
                        $ JubesX.Statup("Love", 85, 1)
                        $ JubesX.Statup("Obed", 90, 1)
                        $ JubesX.Statup("Obed", 50, 2)
                    "Ask her to stop.":
                        $ JubesX.FaceChange("surprised")
                        $ JubesX.Statup("Inbt", 70, 1)
                        ch_p "Let's not do that right now, [JubesX.Pet]."
                        $ JubesX.NameCheck() #checks reaction to petname
                        "[JubesX.Name] sets the dildo down."
                        $ JubesX.OutfitChange()
                        $ JubesX.Statup("Obed", 90, 1)
                        $ JubesX.Statup("Obed", 50, 1)
                        $ JubesX.Statup("Obed", 30, 2)
                        return
                jump Jubes_DA_Prep
            else:
                $ temp_modifier = 0                               # fix, add jubes auto stuff here
                $ Trigger2 = 0
            return

    if Situation == "auto":
            "You rub the dildo across her body, and against her tight anus."
            $ JubesX.FaceChange("surprised", 1)

            if (JubesX.DildoA and Approval) or (Approval > 1):
                #this is not the first time you've had sex, or she's into it
                "[JubesX.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                $ JubesX.FaceChange("sexy")
                $ JubesX.Statup("Obed", 70, 3)
                $ JubesX.Statup("Inbt", 50, 3)
                $ JubesX.Statup("Inbt", 70, 1)
                ch_v "Ooo, [JubesX.Petname], toys!"
                jump Jubes_DA_Prep
            else:
                #she's questioning it
                $ JubesX.Brows = "angry"
                menu:
                    ch_v "Hey, what are you planning to do with that?!"
                    "Sorry, sorry! Never mind.":
                        if Approval:
                            $ JubesX.FaceChange("sexy", 1)
                            $ JubesX.Statup("Obed", 70, 3)
                            $ JubesX.Statup("Inbt", 50, 3)
                            $ JubesX.Statup("Inbt", 70, 1)
                            ch_v "Well, now that you mention it. . ."
                            jump Jubes_DA_Prep
                        "You pull back before you really get it in."
                        $ JubesX.FaceChange("bemused", 1)
                        if JubesX.DildoA:
                            ch_v "Well ok, [JubesX.Petname], maybe warn me next time?"
                        else:
                            ch_v "Well ok, [JubesX.Petname], that's a little much. . . for now . . ."
                    "Just playing with my favorite toys.":
                        $ JubesX.Statup("Love", 80, -10, 1)
                        $ JubesX.Statup("Love", 200, -10)
                        "You press it inside some more."
                        $ JubesX.Statup("Obed", 70, 3)
                        $ JubesX.Statup("Inbt", 50, 3)
                        if not ApprovalCheck(JubesX, 700, "O", TabM=1): #Checks if Obed is 700+
                            $ JubesX.FaceChange("angry")
                            "[JubesX.Name] shoves you away and slaps you in the face."
                            ch_v "Jerk!"
                            ch_v "Ask nice if you want to stick something in my ass!"
                            $ JubesX.Statup("Love", 50, -10, 1)
                            $ JubesX.Statup("Obed", 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            if renpy.showing("Jubes_SexSprite"):
                                call Jubes_Sex_Reset
                            $ JubesX.RecentActions.append("angry")
                            $ JubesX.DailyActions.append("angry")
                        else:
                            $ JubesX.FaceChange("sad")
                            "[JubesX.Name] doesn't seem to be into this, you're lucky she's so obedient."
                            jump Jubes_DA_Prep
            return
    #end auto

    if not JubesX.DildoA:
            #first time
            $ JubesX.FaceChange("surprised", 1)
            $ JubesX.Mouth = "kiss"
            ch_v "You want to try and fit that. . .?"
            if JubesX.Forced:
                $ JubesX.FaceChange("sad")
                ch_v "Always about the butt, huh?"

    if not JubesX.Loose and ("dildo anal" in JubesX.RecentActions or "anal" in JubesX.RecentActions or "dildo anal" in JubesX.DailyActions or "anal" in JubesX.DailyActions):
            $ JubesX.FaceChange("bemused", 1)
            ch_v "I'm still sore from earlier. . ."

    if not JubesX.DildoA and Approval:
            #First time dialog
            if JubesX.Forced:
                $ JubesX.FaceChange("sad")
                $ JubesX.Statup("Love", 70, -3, 1)
                $ JubesX.Statup("Love", 20, -2, 1)
            elif JubesX.Love >= (JubesX.Obed + JubesX.Inbt):
                $ JubesX.FaceChange("sexy")
                $ JubesX.Brows = "sad"
                $ JubesX.Mouth = "smile"
                ch_v "I haven't actually used one of these, back there before. . ."
            elif JubesX.Obed >= JubesX.Inbt:
                $ JubesX.FaceChange("normal")
                ch_v "If that's what you want, [JubesX.Petname]. . ."
            else: # Uninhibited
                $ JubesX.FaceChange("sad")
                $ JubesX.Mouth = "smile"
                ch_v "I guess it could be fun two-player. . ."

    elif Approval:
            #Second time+ dialog
            if JubesX.Forced:
                $ JubesX.FaceChange("sad")
                $ JubesX.Statup("Love", 70, -3, 1)
                $ JubesX.Statup("Love", 20, -2, 1)
                ch_v "The toys again?"
            elif not Taboo and "tabno" in JubesX.DailyActions:
                ch_v "Well, at least you got us some privacy this time. . ."
            elif "dildo anal" in JubesX.DailyActions and not JubesX.Loose:
                pass
            elif "dildo anal" in JubesX.DailyActions:
                $ JubesX.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Breaking out the toys again?",
                    "Didn't get enough earlier?",
                    "I'm still a bit sore from earlier.",
                    "You're going to wear me out."])
                ch_v "[Line]"
            elif JubesX.DildoA < 3:
                $ JubesX.FaceChange("sexy", 1)
                $ JubesX.Brows = "confused"
                $ JubesX.Mouth = "kiss"
                ch_v "You want to stick it in my ass again?"
            else:
                $ JubesX.FaceChange("sexy", 1)
                $ JubesX.ArmPose = 2
                $ Line = renpy.random.choice(["You want some of this action?",
                    "So you'd like another go?",
                    "You want to stick it in my ass again?",
                    "You want me ta lube up your toy?"])
                ch_v "[Line]"
                $ Line = 0

    if Approval >= 2:
            #She's into it. . .
            if JubesX.Forced:
                $ JubesX.FaceChange("sad")
                $ JubesX.Statup("Obed", 90, 1)
                $ JubesX.Statup("Inbt", 60, 1)
                ch_v "Ok, fine."
            else:
                $ JubesX.FaceChange("sexy", 1)
                $ JubesX.Statup("Love", 90, 1)
                $ JubesX.Statup("Inbt", 50, 3)
                $ Line = renpy.random.choice(["Well, sure, stick it in.",
                    "Well. . . ok.",
                    "Sure!",
                    "I guess I could. . . stick it in.",
                    "Hells yeah.",
                    "Heh, ok, ok."])
                ch_v "[Line]"
                $ Line = 0
            $ JubesX.Statup("Obed", 20, 1)
            $ JubesX.Statup("Obed", 60, 1)
            $ JubesX.Statup("Inbt", 70, 2)
            jump Jubes_DA_Prep

    else:
            #She's not into it, but maybe. . .
            $ JubesX.FaceChange("angry")
            if "no dildo" in JubesX.RecentActions:
                ch_v "What part of \"no,\" did you not get, [JubesX.Petname]?"
            elif Taboo and "tabno" in JubesX.DailyActions and "no dildo" in JubesX.DailyActions:
                ch_v "Stop swinging that thing around in public!"
            elif "no dildo" in JubesX.DailyActions:
                ch_v "I already told you \"no,\" [JubesX.Petname]."
            elif Taboo and "tabno" in JubesX.DailyActions:
                ch_v "I already told you that I wouldn't do that out here!"
            elif not JubesX.DildoA:
                $ JubesX.FaceChange("bemused")
                ch_v "I'm just not into toys, [JubesX.Petname]. . ."
            elif not JubesX.Loose and "dildo anal" not in JubesX.DailyActions:
                $ JubesX.FaceChange("perplexed")
                ch_v "You could have been a bit more gentle last time, [JubesX.Petname]. . ."
            else:
                $ JubesX.FaceChange("bemused")
                ch_v "I don't think we need any toys, [JubesX.Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in JubesX.DailyActions:
                    $ JubesX.FaceChange("bemused")
                    ch_v "Yeah, ok, [JubesX.Petname]."
                    return
                "Maybe later?" if "no dildo" not in JubesX.DailyActions:
                    $ JubesX.FaceChange("sexy")
                    ch_v "Maybe I'll practice on my own time, [JubesX.Petname]."
                    $ JubesX.Statup("Love", 80, 2)
                    $ JubesX.Statup("Inbt", 70, 2)
                    if Taboo:
                        $ JubesX.RecentActions.append("tabno")
                        $ JubesX.DailyActions.append("tabno")
                    $ JubesX.RecentActions.append("no dildo")
                    $ JubesX.DailyActions.append("no dildo")
                    return
                "I think you'd like it. . .":
                    if Approval:
                        $ JubesX.FaceChange("sexy")
                        $ JubesX.Statup("Obed", 90, 2)
                        $ JubesX.Statup("Obed", 50, 2)
                        $ JubesX.Statup("Inbt", 70, 3)
                        $ JubesX.Statup("Inbt", 40, 2)
                        $ Line = renpy.random.choice(["Well, sure, stick it in.",
                            "I suppose. . .",
                            "You've got me there."])
                        ch_v "[Line]"
                        $ Line = 0
                        jump Jubes_DA_Prep
                    else:
                        pass

                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck(JubesX, 1050, "OI", TabM = 3) # 105, 120, 135, -120(225)
                    if Approval > 1 or (Approval and JubesX.Forced):
                        $ JubesX.FaceChange("sad")
                        $ JubesX.Statup("Love", 70, -5, 1)
                        $ JubesX.Statup("Love", 200, -5)
                        ch_v "Ok, fine. If we're going to do this, stick it in already."
                        $ JubesX.Statup("Obed", 80, 4)
                        $ JubesX.Statup("Inbt", 80, 1)
                        $ JubesX.Statup("Inbt", 60, 3)
                        $ JubesX.Forced = 1
                        jump Jubes_DA_Prep
                    else:
                        $ JubesX.Statup("Love", 200, -20)
                        $ JubesX.RecentActions.append("angry")
                        $ JubesX.DailyActions.append("angry")

    #She refused all offers.
    $ JubesX.ArmPose = 1
    if "no dildo" in JubesX.DailyActions:
            ch_v "Learn to take \"no\" for an answer, [JubesX.Petname]."
            $ JubesX.RecentActions.append("angry")
            $ JubesX.DailyActions.append("angry")
    elif JubesX.Forced:
            $ JubesX.FaceChange("angry", 1)
            ch_v "I'm not going to let you use that on me."
            $ JubesX.Statup("Lust", 200, 5)
            if JubesX.Love > 300:
                    $ JubesX.Statup("Love", 70, -2)
            $ JubesX.Statup("Obed", 50, -2)
            $ JubesX.RecentActions.append("angry")
            $ JubesX.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
            $ JubesX.FaceChange("angry", 1)
            $ JubesX.RecentActions.append("tabno")
            $ JubesX.DailyActions.append("tabno")
            ch_v "Not here!"
            $ JubesX.Statup("Lust", 200, 5)
            $ JubesX.Statup("Obed", 50, -3)
    elif not JubesX.Loose and "dildo anal" in JubesX.DailyActions:
            $ JubesX.FaceChange("bemused")
            ch_v "Sorry, I just need a little break back there, [JubesX.Petname]."
    elif JubesX.DildoA:
            $ JubesX.FaceChange("sad")
            ch_v "Sorry, you can keep your toys out of there."
    else:
            $ JubesX.FaceChange("normal", 1)
            ch_v "No way."
    $ JubesX.RecentActions.append("no dildo")
    $ JubesX.DailyActions.append("no dildo")
    $ temp_modifier = 0
    return

label Jubes_DA_Prep: #Animation set-up
    if Trigger2 == "dildo anal":
        return

    if not JubesX.Forced and Situation != "auto":
        $ temp_modifier = 20 if JubesX.PantsNum() >= 6 else 0
        call Bottoms_Off(JubesX)
        if "angry" in JubesX.RecentActions:
            return

    $ temp_modifier = 0
    call Jubes_Pussy_Launch("dildo anal")
    if not JubesX.DildoA:
        if JubesX.Forced:
            $ JubesX.Statup("Love", 90, -75)
            $ JubesX.Statup("Obed", 70, 60)
            $ JubesX.Statup("Inbt", 80, 35)
        else:
            $ JubesX.Statup("Love", 90, 10)
            $ JubesX.Statup("Obed", 70, 20)
            $ JubesX.Statup("Inbt", 80, 45)
    if Taboo:
        $ JubesX.Inbt += int(Taboo/10)
        $ JubesX.Lust += int(Taboo/5)


    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ JubesX.DrainWord("tabno")
    $ JubesX.DrainWord("no dildo")
    $ JubesX.RecentActions.append("dildo anal")
    $ JubesX.DailyActions.append("dildo anal")

label Jubes_DA_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(JubesX)
        call Jubes_Pussy_Launch("dildo anal")
        $ JubesX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                call Slap_Ass(JubesX)
                                jump Jubes_DA_Cycle

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
                                            if JubesX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ JubesX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")

                                    "Shift primary action":
                                            if JubesX.Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in her pussy.":
                                                                $ Situation = "shift"
                                                                call Jubes_DA_After
                                                                call Jubes_Fondle_Pussy
                                                        "Just stick a finger in her pussy without asking.":
                                                                $ Situation = "auto"
                                                                call Jubes_DA_After
                                                                call Jubes_Fondle_Pussy
                                                        "I want to shift the dildo to her pussy.":
                                                                $ Situation = "shift"
                                                                call Jubes_DA_After
                                                                call Jubes_Dildo_Pussy
                                                        "Never Mind":
                                                                jump Jubes_DA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Jubes_DA_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

        #End menu (if Line)

        if JubesX.Panties or JubesX.PantsNum() >= 6 or JubesX.HoseNum() >= 5: #This checks if Jubes wants to strip down.
                call Girl_Undress(JubesX,"auto")

        call Shift_Focus(JubesX)
        call Sex_Dialog(JubesX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JubesX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JubesX)
                            if "angry" in JubesX.RecentActions:
                                call Jubes_Pos_Reset
                                return
                            $ JubesX.Statup("Lust", 200, 5)
                            if 100 > JubesX.Lust >= 70 and JubesX.OCount < 2:
                                $ JubesX.RecentActions.append("unsatisfied")
                                $ JubesX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jubes_DA_After
                            $ Line = "came"

                    if JubesX.Lust >= 100:
                            #If Jubes can cum
                            call Girl_Cumming(JubesX)
                            if Situation == "shift" or "angry" in JubesX.RecentActions:
                                jump Jubes_DA_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in JubesX.RecentActions:#And Jubes is unsatisfied,
                                "[JubesX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Jubes_DA_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if JubesX.SEXP >= 100 or ApprovalCheck(JubesX, 1200, "LO"):
            pass
        elif Cnt == (5 + JubesX.DildoA):
                    $ JubesX.Brows = "confused"
                    ch_v "What are you even doing down there?"
        elif JubesX.Lust >= 80:
                    pass
        elif Cnt == (15 + JubesX.DildoA) and JubesX.SEXP >= 15 and not ApprovalCheck(JubesX, 1500):
                    $ JubesX.Brows = "confused"
                    menu:
                        ch_v "[JubesX.Petname], this is getting uncomfortable, maybe we could try something else."
                        "Finish up.":
                                "You let go. . ."
                                jump Jubes_DA_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Jubes_DA_After
                        "No, this is fun.":
                                if ApprovalCheck(JubesX, 1200) or ApprovalCheck(JubesX, 500, "O"):
                                    $ JubesX.Statup("Love", 200, -5)
                                    $ JubesX.Statup("Obed", 50, 3)
                                    $ JubesX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ JubesX.FaceChange("angry", 1)
                                    call Jubes_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_v "Well if that's your attitude, I don't need your \"help\"."
                                    $ JubesX.Statup("Love", 50, -3, 1)
                                    $ JubesX.Statup("Love", 80, -4, 1)
                                    $ JubesX.Statup("Obed", 30, -1, 1)
                                    $ JubesX.Statup("Obed", 50, -1, 1)
                                    $ JubesX.RecentActions.append("angry")
                                    $ JubesX.DailyActions.append("angry")
                                    jump Jubes_DA_After
        #End Count check

        if Round == 10:
                call Sex_Basic_Dialog(JubesX,10) #"I could use a break soon. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(JubesX,5)   #". . . I could really use a break here. . ."

    #Round = 0 loop breaks
    $ JubesX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(JubesX,"done") # ch_s "Ok, that's it, I need a break."

label Jubes_DA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Jubes_Pos_Reset

    $ JubesX.FaceChange("sexy")

    $ JubesX.DildoA += 1
    $ JubesX.Action -=1

    call Partner_Like(JubesX,1)

    if JubesX.DildoA == 1:
            $ JubesX.SEXP += 10
            if not Situation:
                if JubesX.Love >= 500 and "unsatisfied" not in JubesX.RecentActions:
                    if JubesX.Loose:
                        ch_v "That was. . . interesting. . ."
                    else:
                        ch_v "Ouch. . ."
                elif JubesX.Obed <= 500 and Player.Focus <= 20:
                    $ JubesX.FaceChange("perplexed", 1)
                    ch_v "Did you like that?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_v "Mmm, so what else did you have in mind?"
    call Checkout
    return

# end JubesX.Dildo Ass /////////////////////////////////////////////////////////////////////////////

label Jubes_Vibrator_Check:                                                                                 #fix this whole section is copy/paste unfinished
    if "vibrator" in Player.Inventory:
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in JubesX.Inventory:
        "You ask [JubesX.Name] to get out her vibrator."
    else:
        "You don't have one of those on you."
        return 0
    return 1

## JubesX.Footjob //////////////////////////////////////////////////////////////////////
label Jubes_Footjob:
    #fix remove
    "This option is currently unavailable. It will be added in a later update."
    return
    #fix remove

    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JubesX)
    if JubesX.Foot >= 7: # She loves it
        $ temp_modifier += 10
    elif JubesX.Foot >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif JubesX.Foot: #You've done it before
        $ temp_modifier += 3

    if JubesX.Addict >= 75 and JubesX.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 10
    if JubesX.Addict >= 75:
        $ temp_modifier += 5

    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in JubesX.Traits:
        $ temp_modifier += (3*Taboo)
    if JubesX in Player.Harem or "sex friend" in JubesX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JubesX.Traits:
        $ temp_modifier -= 40
    if JubesX.ForcedCount and not JubesX.Forced:
        $ temp_modifier -= 5 * JubesX.ForcedCount

    if Taboo and "tabno" in JubesX.DailyActions:
        $ temp_modifier -= 10

    if "no foot" in JubesX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no foot" in JubesX.RecentActions else 0

    $ Approval = ApprovalCheck(JubesX, 1250, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if Situation == JubesX:                                                                  #Jubes auto-starts
        if Approval > 2:                                                      # fix, add jubes auto stuff here
            "[JubesX.Name] leans back  and starts rubbing your cock with her foot."
            menu:
                "What do you do?"
                "Nothing.":
                    $ JubesX.Statup("Inbt", 70, 3)
                    $ JubesX.Statup("Inbt", 30, 2)
                    "[JubesX.Name] continues her actions."
                "Praise her.":
                    $ JubesX.FaceChange("sexy", 1)
                    $ JubesX.Statup("Inbt", 70, 3)
                    ch_p "Oooh, that's good, [JubesX.Pet]."
                    $ JubesX.NameCheck() #checks reaction to petname
                    "[JubesX.Name] continues her actions."
                    $ JubesX.Statup("Love", 80, 1)
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ JubesX.FaceChange("surprised")
                    $ JubesX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [JubesX.Pet]."
                    $ JubesX.NameCheck() #checks reaction to petname
                    "[JubesX.Name] puts it down."
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Obed", 50, 1)
                    $ JubesX.Statup("Obed", 30, 2)
                    return
            if Trigger:
                $ Trigger3 = "foot"
                return
            jump Jubes_FJ_Prep
        else:
            $ temp_modifier = 0                               # fix, add jubes auto stuff here
            $ Trigger2 = 0
            return

    if not JubesX.Foot and "no foot" not in JubesX.RecentActions:
        $ JubesX.FaceChange("confused", 2)
        ch_v "Standard footjob?"
        $ JubesX.Blush = 1

    if not JubesX.Foot and Approval:                                                 #First time dialog
        if JubesX.Forced:
            $ JubesX.FaceChange("sad",1)
            $ JubesX.Statup("Love", 70, -3, 1)
            $ JubesX.Statup("Love", 20, -2, 1)
        elif JubesX.Love >= (JubesX.Obed + JubesX.Inbt):
            $ JubesX.FaceChange("sexy",1)
            $ JubesX.Brows = "sad"
            $ JubesX.Mouth = "smile"
            ch_v "I guess it couldn't hurt. . ."
        elif JubesX.Obed >= JubesX.Inbt:
            $ JubesX.FaceChange("normal",1)
            ch_v "If you want, [JubesX.Petname]. . ."
        elif JubesX.Addict >= 50:
            $ JubesX.FaceChange("manic", 1)
            ch_v "Okay. . ."
        else: # Uninhibited
            $ JubesX.FaceChange("lipbite",1)
            ch_v "Sure. . ."

    elif Approval:                                                                       #Second time+ dialog
        if JubesX.Forced:
            $ JubesX.FaceChange("sad")
            $ JubesX.Statup("Love", 70, -3, 1)
            $ JubesX.Statup("Love", 20, -2, 1)
            ch_v "That's it?"
        elif not Taboo and "tabno" in JubesX.DailyActions:
            ch_v "Um, I guess this is secure enough. . ."
        elif "foot" in JubesX.DailyActions:
            $ JubesX.FaceChange("sexy", 1)
            ch_v "More of that, huh. . ."
            jump Jubes_FJ_Prep
#        elif "foot" in JubesX.DailyActions:
#            $ JubesX.FaceChange("sexy", 1)
#            $ Line = renpy.random.choice(["Another one?",
#                "Didn't get enough earlier?",
#                "My feet are kinda sore from earlier.",
#                "My feet are kinda sore from earlier."])
#            ch_v "[Line]"
        elif JubesX.Foot < 3:
            $ JubesX.FaceChange("sexy", 1)
            $ JubesX.Brows = "confused"
            $ JubesX.Mouth = "kiss"
            ch_v "Hmm, magic toes. . ."
        else:
            $ JubesX.FaceChange("sexy", 1)
            $ JubesX.ArmPose = 2
            $ Line = renpy.random.choice(["You want me to use my feet?",
                "So you'd like another footjob?",
                "A little. . . [she rubs her foot along your leg]?",
                "A little TLC?"])
            ch_v "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if JubesX.Forced:
            $ JubesX.FaceChange("sad")
            $ JubesX.Statup("Obed", 90, 1)
            $ JubesX.Statup("Inbt", 60, 1)
            ch_v "Ok, sure."
        elif "no foot" in JubesX.DailyActions:
            ch_v "Fine."
        else:
            $ JubesX.FaceChange("sexy", 1)
            $ JubesX.Statup("Love", 90, 1)
            $ JubesX.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Sure, I guess.",
                "OK.",
                "Fine, lemme see it.",
                "I guess I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Heh, ok, ok."])
            ch_v "[Line]"
            $ Line = 0
        $ JubesX.Statup("Obed", 20, 1)
        $ JubesX.Statup("Obed", 60, 1)
        $ JubesX.Statup("Inbt", 70, 2)
        jump Jubes_FJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ JubesX.FaceChange("angry")
        if "no foot" in JubesX.RecentActions:
            ch_v "You should listen better, [JubesX.Petname]."
        elif Taboo and "tabno" in JubesX.DailyActions and "no foot" in JubesX.DailyActions:
            ch_v "I said not in public."
        elif "no foot" in JubesX.DailyActions:
            ch_v "I told you \"no,\" [JubesX.Petname]."
        elif Taboo and "tabno" in JubesX.DailyActions:
            ch_v "I said not in public!"
        elif not JubesX.Foot:
            $ JubesX.FaceChange("bemused")
            ch_v "Eh, [JubesX.Petname]. . ."
        else:
            $ JubesX.FaceChange("bemused")
            ch_v "Not now, ok?"
        menu:
            extend ""
            "Sorry, never mind." if "no foot" in JubesX.DailyActions:
                $ JubesX.FaceChange("bemused")
                ch_v "Sure, no problem."
                return
            "Maybe later?" if "no foot" not in JubesX.DailyActions:
                $ JubesX.FaceChange("sexy")
                ch_v ". . ."
                ch_v "Maybe."
                $ JubesX.Statup("Love", 80, 2)
                $ JubesX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ JubesX.RecentActions.append("tabno")
                    $ JubesX.DailyActions.append("tabno")
                $ JubesX.RecentActions.append("no foot")
                $ JubesX.DailyActions.append("no foot")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ JubesX.FaceChange("sexy")
                    $ JubesX.Statup("Obed", 90, 2)
                    $ JubesX.Statup("Obed", 50, 2)
                    $ JubesX.Statup("Inbt", 70, 3)
                    $ JubesX.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Sure, I guess.",
                        "OK.",
                        "Fine, lemme see it.",
                        "I guess I could. . .",
                        "Ok. . . [She gestures for you to come over].",
                        "Heh, ok, ok."])
                    ch_v "[Line]"
                    $ Line = 0
                    jump Jubes_FJ_Prep
                else:
                    pass

            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck(JubesX, 400, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and JubesX.Forced):
                    $ JubesX.FaceChange("sad")
                    $ JubesX.Statup("Love", 70, -5, 1)
                    $ JubesX.Statup("Love", 200, -2)
                    ch_v "Fine."
                    $ JubesX.Statup("Obed", 50, 4)
                    $ JubesX.Statup("Inbt", 80, 1)
                    $ JubesX.Statup("Inbt", 60, 3)
                    $ JubesX.Forced = 1
                    jump Jubes_FJ_Prep
                else:
                    $ JubesX.Statup("Love", 200, -15)
                    $ JubesX.RecentActions.append("angry")
                    $ JubesX.DailyActions.append("angry")

    #She refused all offers.
    $ JubesX.ArmPose = 1
    if "no foot" in JubesX.DailyActions:
        $ JubesX.FaceChange("angry", 1)
        ch_v "I'm not telling you again."
        $ JubesX.RecentActions.append("angry")
        $ JubesX.DailyActions.append("angry")
    elif JubesX.Forced:
        $ JubesX.FaceChange("angry", 1)
        ch_v "You understand that I have claws down there too. . ."
        $ JubesX.Statup("Lust", 200, 5)
        if JubesX.Love > 300:
                $ JubesX.Statup("Love", 70, -2)
        $ JubesX.Statup("Obed", 50, -2)
        $ JubesX.RecentActions.append("angry")
        $ JubesX.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ JubesX.FaceChange("angry", 1)
        $ JubesX.DailyActions.append("tabno")
        ch_v "This is too exposed."
        $ JubesX.Statup("Lust", 200, 5)
        $ JubesX.Statup("Obed", 50, -3)
    elif JubesX.Foot:
        $ JubesX.FaceChange("sad")
        ch_v "Not right now."
    else:
        $ JubesX.FaceChange("normal", 1)
        ch_v "I'd rather not."
    $ JubesX.RecentActions.append("no foot")
    $ JubesX.DailyActions.append("no foot")
    $ temp_modifier = 0
    return


label Jubes_FJ_Prep:
    if Trigger2 == "foot":
        return

    if Taboo:
        $ JubesX.Inbt += int(Taboo/10)
        $ JubesX.Lust += int(Taboo/5)

    $ JubesX.FaceChange("sexy")
    if JubesX.Forced:
        $ JubesX.FaceChange("sad")
    elif not JubesX.Foot:
        $ JubesX.Brows = "confused"
        $ JubesX.Eyes = "sexy"
        $ JubesX.Mouth = "smile"

    call Seen_First_Peen(JubesX,Partner)

    if not JubesX.Foot:
        if JubesX.Forced:
            $ JubesX.Statup("Love", 90, -20)
            $ JubesX.Statup("Obed", 70, 25)
            $ JubesX.Statup("Inbt", 80, 30)
        else:
            $ JubesX.Statup("Love", 90, 5)
            $ JubesX.Statup("Obed", 70, 20)
            $ JubesX.Statup("Inbt", 80, 20)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ JubesX.DrainWord("tabno")
    $ JubesX.DrainWord("no foot")
    $ JubesX.RecentActions.append("foot")
    $ JubesX.DailyActions.append("foot")

label Jubes_FJ_Cycle:
    while Round > 0:
        call Shift_Focus(JubesX)
        call Jubes_Sex_Launch("foot")
        $ JubesX.LustFace()

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
                                    $ JubesX.Pose = "doggy" if JubesX.Pose != "doggy" else "sex"
                                    "You turn her around. . ."
                                    jump Jubes_FJ_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if JubesX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ JubesX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")

                                    "Shift primary action":
                                            if JubesX.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                    if JubesX.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Jubes_FJ_After
                                                                        call Jubes_Blowjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(JubesX,"tired")
                                                        "How about a handjob?":
                                                                    if JubesX.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Jubes_FJ_After
                                                                        call Jubes_Handjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(JubesX,"tired")

                                                        "How about a titjob?":
                                                                    if JubesX.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Jubes_FJ_After
                                                                        call Jubes_Titjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(JubesX,"tired")



                                                        "Never Mind":
                                                                jump Jubes_FJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")
                                                
        #End menu (if Line)

        call Shift_Focus(JubesX)
        call Sex_Dialog(JubesX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JubesX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JubesX)
                            if "angry" in JubesX.RecentActions:
                                call Jubes_Sex_Reset
                                return
                            $ JubesX.Statup("Lust", 200, 5)
                            if 100 > JubesX.Lust >= 70 and JubesX.OCount < 2:
                                $ JubesX.RecentActions.append("unsatisfied")
                                $ JubesX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jubes_FJ_After
                            $ Line = "came"

                    if JubesX.Lust >= 100:
                            #If Jubes can cum
                            call Girl_Cumming(JubesX)
                            if Situation == "shift" or "angry" in JubesX.RecentActions:
                                jump Jubes_FJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in JubesX.RecentActions:#And Jubes is unsatisfied,
                                "[JubesX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Jubes_FJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Cnt == 20:
                    $ JubesX.Brows = "angry"
                    menu:
                        ch_v "Hmm, this is getting a bit boring."
                        "How about a BJ?" if JubesX.Action and MultiAction:
                                $ Situation = "shift"
                                call Jubes_FJ_After
                                call Jubes_Blowjob
                        "How about a Handy?" if JubesX.Action and MultiAction:
                                $ Situation = "shift"
                                call Jubes_FJ_After
                                call Jubes_Handjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump Jubes_FJ_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Jubes_Sex_Reset
                                $ Situation = "shift"
                                jump Jubes_FJ_After
                        "No, get back down there.":
                                if ApprovalCheck(JubesX, 1200) or ApprovalCheck(JubesX, 500, "O"):
                                    $ JubesX.Statup("Love", 200, -5)
                                    $ JubesX.Statup("Obed", 50, 3)
                                    $ JubesX.Statup("Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    $ JubesX.FaceChange("angry", 1)
                                    "She scowls at you and pulls back."
                                    ch_v "Not interested."
                                    $ JubesX.Statup("Love", 50, -3, 1)
                                    $ JubesX.Statup("Love", 80, -4, 1)
                                    $ JubesX.Statup("Obed", 30, -1, 1)
                                    $ JubesX.Statup("Obed", 50, -1, 1)
                                    $ JubesX.RecentActions.append("angry")
                                    $ JubesX.DailyActions.append("angry")
                                    jump Jubes_FJ_After
        elif Cnt == 10 and JubesX.SEXP <= 100 and not ApprovalCheck(JubesX, 1200, "LO"):
                    $ JubesX.Brows = "confused"
                    ch_v "Ok, seriously, let's try something different."
        #End Count check

        call Escalation(JubesX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(JubesX,10) #"I could use a break soon. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(JubesX,5)   #". . . I could really use a break here. . ."

    #Round = 0 loop breaks
    $ JubesX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(JubesX,"done") # ch_s "Ok, that's it, I need a break."

label Jubes_FJ_After:
    $ JubesX.FaceChange("sexy")

    $ JubesX.Foot += 1
    $ JubesX.Action -=1
    $ JubesX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ JubesX.Addictionrate += 1
    $ JubesX.Statup("Lust", 90, 5)

    call Partner_Like(JubesX,1)

    if "Jubespedi" in Achievements:
            pass
    elif JubesX.Foot >= 10:
            $ JubesX.FaceChange("smile", 1)
            ch_v "I think I'm finally back into practice on this."
            $ Achievements.append("Jubespedi")
            $ JubesX.SEXP += 5
    elif JubesX.Foot == 1:
            $ JubesX.SEXP += 10
            if JubesX.Love >= 500:
                $ JubesX.Mouth = "smile"
                ch_v "Did you like that? . ."
            elif Player.Focus <= 20:
                $ JubesX.Mouth = "sad"
                ch_v "Did that do it for you?"
    elif JubesX.Foot == 5:
                ch_v "I'm getting used to this. . ."

    $ temp_modifier = 0
    if Situation == "shift":
        ch_v "Ok, so what did you have in mind?"
    else:
        call Jubes_Sex_Reset
    call Checkout
    return

## end JubesX.Footjob //////////////////////////////////////////////////////////////////////
