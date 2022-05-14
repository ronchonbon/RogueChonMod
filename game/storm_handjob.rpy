## character.Handjob //////////////////////////////////////////////////////////////////////
label Storm_Handjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(character)
    if character.Hand >= 7: # She loves it
        $ temp_modifier += 10
    elif character.Hand >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif character.Hand: #You've done it before
        $ temp_modifier += 3

    if character.Addict >= 75 and character.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 15
    if character.Addict >= 75:
        $ temp_modifier += 5

    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in character.Traits:
        $ temp_modifier += (3*Taboo)
    if character in Player.Harem or "sex friend" in character.Petnames:
        $ temp_modifier += 10
    elif "ex" in character.Traits:
        $ temp_modifier -= 40
    if character.ForcedCount and not character.Forced:
        $ temp_modifier -= 5 * character.ForcedCount

    if Taboo and "tabno" in character.DailyActions:
        $ temp_modifier -= 10

    if "no hand" in character.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no hand" in character.RecentActions else 0

    $ Approval = ApprovalCheck(character, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if not character.Hand and "no hand" not in character.RecentActions:
        $ character.FaceChange("sly", 2)
        ch_s "You would like me to jerk you off?"

    if not character.Hand and Approval:                                                 #First time dialog
        if character.Forced:
            $ character.FaceChange("sad",1)
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Love", 20, -2, 1)
        elif character.Love >= (character.Obed + character.Inbt):
            $ character.FaceChange("sexy",1)
            $ character.Brows = "sad"
            $ character.Mouth = "smile"
            ch_s "I might enjoy that. . ."
        elif character.Obed >= character.Inbt:
            $ character.FaceChange("normal",1)
            ch_s "If that is what you want, [character.Petname]. . ."
        elif character.Addict >= 50:
            $ character.FaceChange("manic", 1)
            ch_s "Mmmmmmmm. . ."
        else: # Uninhibited
            $ character.FaceChange("lipbite",1,Eyes="side")
            ch_s "I suppose. . ."

    elif Approval:                                                                       #Second time+ dialog
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Love", 20, -2, 1)
            ch_s "Nothing more than that?"
        elif not Taboo and "tabno" in character.DailyActions:
            ch_s "Here, hmm?. . ."
        elif "hand" in character.RecentActions:
            $ character.FaceChange("sexy", 1)
            ch_s "I do not know if I have it in me. . ."
            jump Storm_HJ_Prep
        elif "hand" in character.DailyActions:
            $ character.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Another?",
                "My arm will wear out.",
                "You did not get enough earlier?",
                "My hand is quite sore from earlier.",
                "My hand is rather sore from before."])
            ch_s "[Line]"
        elif character.Hand < 3:
            $ character.FaceChange("sly", 1)
            ch_s "You enjoyed it last time?. . ."
        else:
            $ character.FaceChange("sexy", 1)
            $ character.ArmPose = 2
            $ Line = renpy.random.choice(["You want more?",
                "So you would like another?",
                "More of this? [fist pumping hand gestures]",
                "Oh, did you want some attention?"])
            ch_s "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Obed", 90, 1)
            $ character.Statup("Inbt", 60, 1)
            ch_s "Fine, we can do this."
        elif "no hand" in character.DailyActions:
            ch_s "Oh, very well. . ."
        else:
            $ character.FaceChange("sexy", 1)
            $ character.Statup("Love", 90, 1)
            $ character.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Oh, I suppose we might.",
                "I would do this.",
                "Very well, give it here.",
                "I suppose that I could. . .",
                ". . .Fine.[She gestures for you to come over]",
                "Ok, ok."])
            ch_s "[Line]"
            $ Line = 0
        $ character.Statup("Obed", 20, 1)
        $ character.Statup("Obed", 60, 1)
        $ character.Statup("Inbt", 70, 2)
        jump Storm_HJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ character.FaceChange("angry")
        if "no hand" in character.DailyActions:
            ch_s "You will need to accept a \"no\", [character.Petname]."
        elif Taboo and "tabno" in character.DailyActions:
            ch_s "I was very clear, this is too public."
        elif not character.Hand:
            $ character.FaceChange("bemused")
            ch_s "Are you certain, [character.Petname]? . ."
        else:
            $ character.FaceChange("bemused")
            ch_s "I would rather not right now though."
        menu:
            extend ""
            "Sorry, never mind." if "no hand" in character.DailyActions:
                $ character.FaceChange("bemused")
                ch_s "I understand."
                return
            "Maybe later?" if "no hand" not in character.DailyActions:
                $ character.FaceChange("sexy")
                ch_s ". . ."
                ch_s "Perhaps. . ."
                $ character.Statup("Love", 80, 2)
                $ character.Statup("Inbt", 70, 2)
                if Taboo:
                    $ character.RecentActions.append("tabno")
                    $ character.DailyActions.append("tabno")
                $ character.RecentActions.append("no hand")
                $ character.DailyActions.append("no hand")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ character.FaceChange("sexy")
                    $ character.Statup("Obed", 90, 2)
                    $ character.Statup("Obed", 50, 2)
                    $ character.Statup("Inbt", 70, 3)
                    $ character.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Oh, I suppose we might.",
                        "I would do this.",
                        "Very well, give it here.",
                        "I suppose that I could. . .",
                        ". . .Fine.[She gestures for you to come over]",
                        "Ok, ok."])
                    ch_s "[Line]"
                    $ Line = 0
                    jump Storm_HJ_Prep

            "Come on, get to work.":                                               # Pressured into it
                call forced_action(character, "handjob")

    #She refused all offers.
    $ character.ArmPose = 1
    if "no hand" in character.DailyActions:
        $ character.FaceChange("angry", 1)

        $ character.RecentActions.append("angry")
        $ character.DailyActions.append("angry")
    elif character.Forced:
        $ character.FaceChange("angry", 1)
        ch_s "I am not comfortable with that."
        $ character.Statup("Lust", 200, 5)
        if character.Love > 300:
                $ character.Statup("Love", 70, -2)
        $ character.Statup("Obed", 50, -2)
        $ character.RecentActions.append("angry")
        $ character.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ character.FaceChange("angry", 1)
        $ character.DailyActions.append("tabno")
        ch_s "I could not possibly do that here."
        $ character.Statup("Lust", 200, 5)
        $ character.Statup("Obed", 50, -3)
    elif character.Hand:
        $ character.FaceChange("sad")
        ch_s ". . . I would rather not."
    else:
        $ character.FaceChange("normal", 1)
        ch_s "No, I do not think so, [character.Petname]."
    $ character.RecentActions.append("no hand")
    $ character.DailyActions.append("no hand")
    $ temp_modifier = 0
    return


label Storm_HJ_Prep:
    if Trigger2 == "hand":
        return

    if Taboo:
        $ character.Inbt += int(Taboo/10)
        $ character.Lust += int(Taboo/5)

    $ character.FaceChange("sexy")
    if character.Forced:
        $ character.FaceChange("sad")
    elif not character.Hand:
        $ character.Brows = "confused"
        $ character.Eyes = "sexy"
        $ character.Mouth = "smile"

    call Seen_First_Peen(character,Partner,React=Situation)
    call Storm_HJ_Launch("L")

    if Situation == character:
            #Storm auto-starts
            $ Situation = 0
            if Trigger2 == "jackin":
                "[character.Name] brushes your hand aside and starts stroking your cock."
            else:
                "[character.Name] draws her fingers across your cock, and begins to stroke it."
            menu:
                "What do you do?"
                "Nothing.":
                    $ character.Statup("Inbt", 70, 3)
                    $ character.Statup("Inbt", 30, 2)
                    "[character.Name] continues her actions."
                "Praise her.":
                    $ character.FaceChange("sexy", 1)
                    $ character.Statup("Inbt", 70, 3)
                    ch_p "Oooh, that's good, [character.Pet]."
                    $ character.NameCheck() #checks reaction to petname
                    "[character.Name] continues her actions."
                    $ character.Statup("Love", 80, 1)
                    $ character.Statup("Obed", 90, 1)
                    $ character.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ character.FaceChange("surprised")
                    $ character.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [character.Pet]."
                    $ character.NameCheck() #checks reaction to petname
                    "[character.Name] puts it down."
                    $ character.Statup("Obed", 90, 1)
                    $ character.Statup("Obed", 50, 1)
                    $ character.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ character.AddWord(1,"refused","refused")
                    return

    if not character.Hand:
        if character.Forced:
            $ character.Statup("Love", 90, -20)
            $ character.Statup("Obed", 70, 25)
            $ character.Statup("Inbt", 80, 30)
        else:
            $ character.Statup("Love", 90, 5)
            $ character.Statup("Obed", 70, 20)
            $ character.Statup("Inbt", 80, 20)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ character.DrainWord("tabno")
    $ character.DrainWord("no hand")
    $ character.RecentActions.append("hand")
    $ character.DailyActions.append("hand")

label Storm_HJ_Cycle:
    while Round > 0:
        call Shift_Focus(character)
        call Storm_HJ_Launch
        $ character.LustFace()

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
                                            if character.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ character.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(character,"tired")

                                    "Shift primary action":
                                            if character.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                $ Situation = "shift"
                                                                call Storm_HJ_After
                                                                call Storm_Blowjob

                                                        "How about a titjob?":
                                                                $ Situation = "shift"
                                                                call Storm_HJ_After
                                                                call Storm_Titjob
                                                        "Never Mind":
                                                                jump Storm_HJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(character,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [character.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(character)
                                            "Asks [character.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                call Three_Change(character)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(character)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Storm_HJ_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Storm_HJ_Cycle
                                            "Never mind":
                                                        jump Storm_HJ_Cycle
                                    "Undress [character.Name]":
                                            call Girl_Undress(character)
                                    "Clean up [character.Name] (locked)" if not character.Spunk:
                                            pass
                                    "Clean up [character.Name]" if character.Spunk:
                                            call Girl_Cleanup(character,"ask")
                                    "Never mind":
                                            jump Storm_HJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Storm_HJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Storm_HJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Storm_HJ_Reset
                                    $ Line = 0
                                    jump Storm_HJ_After
        #End menu (if Line)

        call Shift_Focus(character)
        call Sex_Dialog(character,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or character.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(character)
                            if "angry" in character.RecentActions:
                                call Storm_HJ_Reset
                                return
                            $ character.Statup("Lust", 200, 5)
                            if 100 > character.Lust >= 70 and character.OCount < 2 and character.SEXP >= 20:
                                $ character.RecentActions.append("unsatisfied")
                                $ character.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Storm_HJ_After
                            $ Line = "came"

                    if character.Lust >= 100:
                            #If [character.Name] can cum
                            call Girl_Cumming(character)
                            if Situation == "shift" or "angry" in character.RecentActions:
                                jump Storm_HJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in character.RecentActions:#And [character.Name] is unsatisfied,
                                    "[character.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Storm_HJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Cnt == 20:
                    $ character.Brows = "angry"
                    ch_s "Hmm, I am developing a hand cramp here."
                    menu:
                        ch_s "Mind if we take a break?"
                        "How about a BJ?" if character.Action and MultiAction:
                                $ Situation = "shift"
                                call Storm_HJ_After
                                call Storm_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump Storm_HJ_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Storm_HJ_Reset
                                $ Situation = "shift"
                                jump Storm_HJ_After
                        "No, get back down there.":
                                if ApprovalCheck(character, 1200) or ApprovalCheck(character, 500, "O"):
                                    $ character.Statup("Love", 200, -5)
                                    $ character.Statup("Obed", 50, 3)
                                    $ character.Statup("Obed", 80, 2)
                                    "She scowls but gets back to work."
                                else:
                                    $ character.FaceChange("angry", 1)
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_s "Perhaps some time alone would help you better evaluate your choices."
                                    $ character.Statup("Love", 50, -3, 1)
                                    $ character.Statup("Love", 80, -4, 1)
                                    $ character.Statup("Obed", 30, -1, 1)
                                    $ character.Statup("Obed", 50, -1, 1)
                                    $ character.RecentActions.append("angry")
                                    $ character.DailyActions.append("angry")
                                    jump Storm_HJ_After
        elif Cnt == 10 and character.SEXP <= 100 and not ApprovalCheck(character, 1200, "LO"):
                    $ character.Brows = "confused"
                    ch_s "Are you certain you didn't have anything else in mind?"
        #End Count check

        call Escalation(character) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(character,10) #"It is getting late, [Girl.Petname]. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(character,5)   #"We should take a break soon."

    #Round = 0 loop breaks
    $ character.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(character,"done") # ch_s "I need to take a moment to collect myself."

label Storm_HJ_After:
    $ character.FaceChange("sexy")

    $ character.Hand += 1
    $ character.Action -=1
    $ character.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ character.Addictionrate += 1
    $ character.Statup("Lust", 90, 5)

    call Partner_Like(character,1)

    if "Storm Handi-Queen" in Achievements:
            pass
    elif character.Hand >= 10:
            $ character.FaceChange("smile", 1)
            ch_s "I seem to have become the \"queen\" of good handjobs."
            $ Achievements.append("Storm Handi-Queen")
            $character.SEXP += 5
    elif character.Hand == 1:
            $character.SEXP += 10
            if not character.Forced:
                $ character.Mouth = "smile"
                ch_s "That was more enjoyable than I had expected. . ."
            elif Player.Focus <= 20:
                $ character.Mouth = "sad"
                ch_s "Did that satisfy you?"
    elif character.Hand == 5:
                ch_s "I have gotten used to these. . ."

    $ temp_modifier = 0
    if Situation == "shift":
        ch_s "Very well, what did you want to do?"
    else:
        call Storm_HJ_Reset
    call Checkout
    return

## end character.Handjob //////////////////////////////////////////////////////////////////////




## character.Titjob //////////////////////////////////////////////////////////////////////
label Storm_Titjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(character)
    if character.Tit >= 7: # She loves it
        $ temp_modifier += 10
    elif character.Tit >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif character.Tit: #You've done it before
        $ temp_modifier += 5

    if character.Addict >= 75 and character.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 15
    elif character.Addict >= 75:
        $ temp_modifier += 5

    if character.SeenChest and ApprovalCheck(character, 500): # You've seen her tits.
        $ temp_modifier += 10
    if not character.Chest and not character.Over: #She's already topless
        $ temp_modifier += 10
    if character.Lust > 75: #She's really horny
        $ temp_modifier += 10
    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in character.Traits:
        $ temp_modifier += (5*Taboo)
    if character in Player.Harem or "sex friend" in character.Petnames:
        $ temp_modifier += 10
    elif "ex" in character.Traits:
        $ temp_modifier -= 30
    if character.ForcedCount and not character.Forced:
        $ temp_modifier -= 5 * character.ForcedCount

    if Taboo and "tabno" in character.DailyActions:
        $ temp_modifier -= 10

    if "no titjob" in character.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no titjob" in character.RecentActions else 0

    $ Approval = ApprovalCheck(character, 1200, TabM = 5) # 120, 135, 150, Taboo -200(320)

    if not character.Tit and "no titjob" not in character.RecentActions:
        $ character.FaceChange("surprised", 1)
        $ character.Mouth = "kiss"
        ch_s "My breasts are really appealing to you, [character.Petname]?"

    if not character.Tit and Approval:
        #First time dialog
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Love", 20, -2, 1)
        elif character.Love >= (character.Obed + character.Inbt):
            $ character.FaceChange("sexy")
            $ character.Brows = "sad"
            $ character.Mouth = "smile"
            ch_s "I suppose you've earned something special. . ."
        elif character.Obed >= character.Inbt:
            $ character.FaceChange("normal")
            ch_s "If that is what you want. . ."
        elif character.Addict >= 50:
            $ character.FaceChange("manic", 1)
            ch_s "Hmmmm. . . ."
        else: # Uninhibited
            $ character.FaceChange("sad")
            $ character.Mouth = "smile"
            ch_s "Hmm, I was expecting you to ask. . ."

    elif Approval:
        #Second time+ dialog
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Love", 20, -2, 1)
            ch_s "You enjoy making use of these?"
        elif not Taboo and "tabno" in character.DailyActions:
            ch_s "I suppose this is secluded enough. . ."
        elif "titjob" in character.RecentActions:
            $ character.FaceChange("sexy", 1)
            ch_s "You cannot get enough?"
            jump Storm_TJ_Prep
        elif "titjob" in character.DailyActions:
            $ character.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",
                "You will wear them out like this.",
                "You did not get enough earlier?",
                "I am still a bit sore from earlier."])
            ch_s "[Line]"
        elif character.Tit < 3:
            $ character.FaceChange("sly", 1)
            ch_s "Hmm, another titjob?"
        else:
            $ character.FaceChange("sexy", 1)
            $ character.ArmPose = 2
            $ Line = renpy.random.choice(["You wish to use these? [jiggles her tits]",
                "So you would like another titjob?",
                ". . . [bounces tits]?",
                "You would like to give it a hug?"])
            ch_s "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Obed", 90, 1)
            $ character.Statup("Inbt", 60, 1)
            ch_s "I suppose this would not be too unpleasant. . ."
        elif "no titjob" in character.DailyActions:
            ch_s "Very well then. . ."
        else:
            $ character.FaceChange("sexy", 1)
            $ character.Statup("Love", 90, 1)
            $ character.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Fine, come over here.",
                "Oh, very well.",
                "Mmmmm.",
                "Fine, show me.",
                "Fine. . . [She drools a bit into her cleavage].",
                "Oh, all right."])
            ch_s "[Line]"
            $ Line = 0
        $ character.Statup("Obed", 20, 1)
        $ character.Statup("Obed", 70, 1)
        $ character.Statup("Inbt", 80, 2)
        jump Storm_TJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ character.FaceChange("angry")
        if "no titjob" in character.DailyActions:
            ch_s "You will need to accept a \"no\", [character.Petname]."
        elif Taboo and "tabno" in character.DailyActions and "no titjob" in character.DailyActions:
            ch_s "This is not an appropriate location for that. !"
        elif "no titjob" in character.DailyActions:
            ch_s "I already refused, [character.Petname]."
        elif Taboo and "tabno" in character.DailyActions:
            ch_s "This is not an appropriate place for that."
        else:
            $ character.FaceChange("bemused")
            ch_s "Perhaps later, [character.Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no titjob" in character.DailyActions:
                $ character.FaceChange("bemused")
                ch_s "That is fine, [character.Petname]."
                return
            "Maybe later?" if "no titjob" not in character.DailyActions:
                $ character.FaceChange("sexy")
                ch_s "Perhaps."
                $ character.Statup("Love", 80, 2)
                $ character.Statup("Inbt", 70, 2)
                if Taboo:
                    $ character.RecentActions.append("tabno")
                    $ character.DailyActions.append("tabno")
                $ character.RecentActions.append("no titjob")
                $ character.DailyActions.append("no titjob")
                return
            "I think this could be fun for both of us. . .":
                if Approval:
                    $ character.FaceChange("sexy")
                    $ character.Statup("Obed", 80, 2)
                    $ character.Statup("Obed", 40, 2)
                    $ character.Statup("Inbt", 70, 3)
                    $ character.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Fine, come over here.",
                        "Oh, very well.",
                        "Mmmmm.",
                        "Fine, show me.",
                        "Fine. . . [She drools a bit into her cleavage].",
                        "Oh, all right."])
                    ch_s "[Line]"
                    $ Line = 0
                    jump Storm_TJ_Prep
                else:
                    $ Approval = ApprovalCheck(character, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)             Handy instead?
                    if Approval >= 2:
                        $ character.Statup("Inbt", 80, 1)
                        $ character.Statup("Inbt", 60, 3)
                        $ character.FaceChange("confused", 1)
                        if character.Blow:
                            ch_s "You seemed to enjoy blowjobs, would that work instead?"
                        else:
                            ch_s "Would you perhaps prefer a blowjob?"
                        menu:
                            extend ""
                            "Ok, get down there.":
                                $ character.Statup("Love", 80, 2)
                                $ character.Statup("Inbt", 60, 1)
                                $ character.Statup("Obed", 50, 1)
                                jump Storm_BJ_Prep
                            "Nah, it's all about dem titties.":
                                $ Line = "no BJ"
                    if Approval:
                        $ character.Statup("Inbt", 80, 1)
                        $ character.Statup("Inbt", 60, 3)
                        $ character.FaceChange("confused", 1)
                        ch_s "Perhaps a handjob?"
                        menu:
                            ch_s "Perhaps a handjob?"
                            "Sure, that's fine.":
                                $ character.Statup("Love", 80, 2)
                                $ character.Statup("Inbt", 60, 1)
                                $ character.Statup("Obed", 50, 1)
                                jump Storm_HJ_Prep
                            "Seriously, titties." if Line == "no BJ":
                                $ Line = 0
                            "Nah, it's all about dem titties." if Line != "no BJ":
                                pass
                    $ character.Statup("Love", 200, -2)
                    ch_s "Well. That is unfortunate. . ."
                    $ character.Statup("Obed", 70, 2)


            "Come on, let me fuck those titties, [character.Pet]":                                               # Pressured into it
                $ character.NameCheck() #checks reaction to petname
                $ Approval = ApprovalCheck(character, 700, "OI", TabM = 4) # 70, 85, 100, -160(230)
                if Approval > 1 or (Approval and character.Forced):
                    $ character.FaceChange("sad")
                    $ character.Statup("Love", 70, -5, 1)
                    $ character.Statup("Love", 200, -2)

                    $ character.Statup("Obed", 50, 4)
                    $ character.Statup("Inbt", 80, 1)
                    $ character.Statup("Inbt", 60, 3)
                    $ character.Forced = 1
                    jump Storm_TJ_Prep
                else:
                    $ character.Statup("Love", 200, -15)
                    $ character.RecentActions.append("angry")
                    $ character.DailyActions.append("angry")

    #She refused all offers.
    if "no titjob" in character.DailyActions:
        $ character.FaceChange("angry", 1)

        $ character.RecentActions.append("angry")
        $ character.DailyActions.append("angry")
    elif character.Forced:
        $ character.FaceChange("angry", 1)
        ch_s "I do not wish to do this."
        $ character.Statup("Lust", 200, 5)
        if character.Love > 300:
                $ character.Statup("Love", 70, -2)
        $ character.Statup("Obed", 50, -2)
        $ character.RecentActions.append("angry")
        $ character.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ character.FaceChange("angry", 1)
        $ character.DailyActions.append("tabno")
        ch_s "I do not wish to make a spectacle."
        $ character.Statup("Lust", 200, 5)
        $ character.Statup("Obed", 50, -3)
    elif character.Tit:
        $ character.FaceChange("sad")
        ch_s "Our time together was a memory."
    else:
        $ character.FaceChange("normal", 1)
        ch_s "I would rather not, [character.Petname]."
    $ character.RecentActions.append("no titjob")
    $ character.DailyActions.append("no titjob")
    $ temp_modifier = 0
    return

label Storm_TJ_Prep:
    if Taboo:
        $ character.Inbt += int(Taboo/10)
        $ character.Lust += int(Taboo/5)


    $ character.FaceChange("sexy")
    if character.Forced:
        $ character.FaceChange("sad")
    elif not character.Tit:
        $ character.Brows = "confused"
        $ character.Eyes = "sexy"
        $ character.Mouth = "smile"

    call Seen_First_Peen(character,Partner,React=Situation)
    call Storm_TJ_Launch("L")

    if Situation == character:
            #Storm auto-starts
            $ Situation = 0
            call Storm_TJ_Launch("L")
            "[character.Name] slides down and wraps her tits around your dick."
            menu:
                "What do you do?"
                "Nothing.":
                    $ character.Statup("Inbt", 80, 3)
                    $ character.Statup("Inbt", 40, 2)
                    "[character.Name] starts to slide them up and down."
                "Praise her.":
                    $ character.FaceChange("sexy", 1)
                    $ character.Statup("Inbt", 80, 3)
                    ch_p "Oh, that sounds like a good idea, [character.Pet]."
                    $ character.NameCheck() #checks reaction to petname
                    "[character.Name] continues her actions."
                    $ character.Statup("Love", 85, 1)
                    $ character.Statup("Obed", 90, 1)
                    $ character.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ character.FaceChange("confused")
                    $ character.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [character.Pet]."
                    $ character.NameCheck() #checks reaction to petname
                    "[character.Name] lets it drop out from between her breasts."
                    $ character.Statup("Obed", 90, 1)
                    $ character.Statup("Obed", 50, 3)
                    $ Player.RecentActions.append("nope")
                    $ character.AddWord(1,"refused","refused")
                    return
    if not character.Tit:
        if character.Forced:
            $ character.Statup("Love", 90, -25)
            $ character.Statup("Obed", 70, 30)
            $ character.Statup("Inbt", 80, 35)
        else:
            $ character.Statup("Love", 90, 5)
            $ character.Statup("Obed", 70, 25)
            $ character.Statup("Inbt", 80, 30)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ character.DrainWord("tabno")
    $ character.DrainWord("no titjob")
    $ character.RecentActions.append("titjob")
    $ character.DailyActions.append("titjob")


label Storm_TJ_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(character)
        call Storm_TJ_Launch
        $ character.LustFace()

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
                                            if character.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ character.Action -= 1
                                            else:
                                                ch_s "I would prefer to finish this."

                                    "Shift primary action":
                                            if character.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                $ Situation = "shift"
                                                                call Storm_TJ_After
                                                                call Storm_Blowjob
                                                        "How about a handy?":
                                                                $ Situation = "shift"
                                                                call Storm_BJ_After
                                                                call Storm_Handjob
                                                        "Never Mind":
                                                                jump Storm_TJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(character,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [character.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(character)
                                            "Asks [character.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(character)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(character)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Storm_TJ_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Storm_TJ_Cycle
                                            "Never mind":
                                                        jump Storm_TJ_Cycle
                                    "Undress [character.Name]":
                                            call Girl_Undress(character)
                                    "Clean up [character.Name] (locked)" if not character.Spunk:
                                            pass
                                    "Clean up [character.Name]" if character.Spunk:
                                            call Girl_Cleanup(character,"ask")
                                    "Never mind":
                                            jump Storm_TJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Storm_TJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Storm_TJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Storm_TJ_Reset
                                    $ Line = 0
                                    jump Storm_TJ_After
        #End menu (if Line)

        call Shift_Focus(character)
        call Sex_Dialog(character,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or character.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(character)
                            if "angry" in character.RecentActions:
                                call Storm_TJ_Reset
                                return
                            $ character.Statup("Lust", 200, 5)
                            if 100 > character.Lust >= 70 and character.OCount < 2 and character.SEXP >= 20:
                                $ character.RecentActions.append("unsatisfied")
                                $ character.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Storm_TJ_After
                            $ Line = "came"

                    if character.Lust >= 100:
                            #If [character.Name] can cum
                            call Girl_Cumming(character)
                            if Situation == "shift" or "angry" in character.RecentActions:
                                jump Storm_TJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in character.RecentActions:#And [character.Name] is unsatisfied,
                                "[character.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Storm_TJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if character.SEXP >= 100 or ApprovalCheck(character, 1200, "LO"):
            pass
        elif Cnt == (5 + character.Tit):
                    $ character.Brows = "confused"
                    ch_s "Are you getting close? This is making me a bit sore. . ."
        elif Cnt == (10 + character.Tit):
                    $ character.Brows = "angry"
                    menu:
                        ch_s "This is becoming uncomfortable, is there some way I could finish you off?"
                        "How about a BJ?" if character.Action and MultiAction:
                                $ Situation = "shift"
                                call Storm_TJ_After
                                call Storm_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                jump Storm_TJ_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Storm_TJ_Reset
                                $ Situation = "shift"
                                jump Storm_TJ_After
                        "No, get back down there.":
                                if ApprovalCheck(character, 1200) or ApprovalCheck(character, 500, "O"):
                                    $ character.Statup("Love", 200, -5)
                                    $ character.Statup("Obed", 50, 3)
                                    $ character.Statup("Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    $ character.FaceChange("angry", 1)
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_s "Then I suppose you can handle this yourself."
                                    $ character.Statup("Love", 50, -3, 1)
                                    $ character.Statup("Love", 80, -4, 1)
                                    $ character.Statup("Obed", 30, -1, 1)
                                    $ character.Statup("Obed", 50, -1, 1)
                                    $ character.RecentActions.append("angry")
                                    $ character.DailyActions.append("angry")
                                    jump Storm_TJ_After
        #End Count check

        call Escalation(character) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(character,10) #"It is getting late, [Girl.Petname]. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(character,5)   #"We should take a break soon."

    #Round = 0 loop breaks
    $ character.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(character,"done") # ch_s "I need to take a moment to collect myself."

label Storm_TJ_After:
    $ character.FaceChange("sexy")

    $ character.Tit += 1
    $ character.Action -=1
    $ character.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ character.Addictionrate += 1

    if Partner == "Kitty":
        call Partner_Like(character,4,2)
    else:
        call Partner_Like(character,3)

    if character.Tit > 5:
            pass
    elif character.Tit == 1:
        $character.SEXP += 12
        if character.Love >= 500:
            $ character.Mouth = "smile"
            ch_s "Mmm, I did quite enjoy that!"
        elif Player.Focus <= 20:
            $ character.Mouth = "sad"
            ch_s "I hope that met your standards."
    elif character.Tit == 5:
            ch_s "You do seem to enjoy this."


    $ temp_modifier = 0
    if Situation == "shift":
            ch_s "Mmm, so what else did you have in mind?"
    else:
            call Storm_TJ_Reset
    call Checkout
    return

## end character.Titjob //////////////////////////////////////////////////////////////////////


# character.Blowjob //////////////////////////////////////////////////////////////////////

label Storm_Blowjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(character)
    if character.Blow >= 7: # She loves it
        $ temp_modifier += 15
    elif character.Blow >= 3: #You've done it before several times
        $ temp_modifier += 10
    elif character.Blow: #You've done it before
        $ temp_modifier += 7

    if character.Addict >= 75 and character.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 25
    elif character.Addict >= 75: #She's really strung out
        $ temp_modifier += 15

    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in character.Traits:
        $ temp_modifier += (4*Taboo)
    if character in Player.Harem or "sex friend" in character.Petnames:
        $ temp_modifier += 10
    elif "ex" in character.Traits:
        $ temp_modifier -= 40
    if character.ForcedCount and not character.Forced:
        $ temp_modifier -= 5 * character.ForcedCount

    if Taboo and "tabno" in character.DailyActions:
        $ temp_modifier -= 10

    if "no blow" in character.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no blow" in character.RecentActions else 0

    $ Approval = ApprovalCheck(character, 1300, TabM = 4) # 130, 145, 160, Taboo -160(290)

    if not character.Blow and "no blow" not in character.RecentActions:
        $ character.FaceChange("sly")
        ch_s "You would like me to suck on your penis?"

    if not character.Blow and Approval:                                                 #First time dialog
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Love", 20, -2, 1)
        elif character.Love >= (character.Obed + character.Inbt):
            $ character.FaceChange("sexy")
            $ character.Brows = "sad"
            $ character.Mouth = "smile"
            ch_s "I have been curious. . ."
        elif character.Obed >= character.Inbt:
            $ character.FaceChange("normal")
            ch_s "If that is what you want. . ."
        elif character.Addict >= 50:
            $ character.FaceChange("manic", 1)
            ch_s "I might enjoy that. . ."
        else: # Uninhibited
            $ character.FaceChange("sad")
            $ character.Mouth = "smile"
            ch_s "I suppose. . ."
    elif Approval:                                                                       #Second time+ dialog
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Love", 20, -2, 1)
            ch_s "Tsk, again?"
        elif not Taboo and "tabno" in character.DailyActions:
            ch_s "Fine, I suppose this is secluded enough. . ."
        elif "blow" in character.RecentActions:
            $ character.FaceChange("sexy", 1)
            ch_s "Mmm, again?"
            jump Storm_BJ_Prep
        elif "blow" in character.DailyActions:
            $ character.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Back so soon?",
                "I must prepare myself.",
                "You did not get enough earlier?",
                "My jaw is still rather sore.",
                "My jaw is still recovering."])
            ch_s "[Line]"
        elif character.Blow < 3:
            $ character.FaceChange("sexy", 1)
            $ character.Brows = "confused"
            $ character.Mouth = "kiss"
            ch_s "Another blowjob?"
        else:
            $ character.FaceChange("sexy", 1)
            $ character.ArmPose = 2
            $ Line = renpy.random.choice([". . . [mimes blowing]?",
                "So you would like another blowjob?",
                "You wish for me to suck you off?",
                "Are you asking if I am hungry?"])
            ch_s "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Obed", 90, 1)
            $ character.Statup("Inbt", 60, 1)
            ch_s "Fine."
        elif "no blow" in character.DailyActions:
            ch_s "Fine, I suppose you have earned it. . ."
        else:
            $ character.FaceChange("sexy", 1)
            $ character.Statup("Love", 90, 1)
            $ character.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice([". . . ok.",
                "Well. . . ok.",
                "Mmmm.",
                "Sure, let me have it.",
                "Mmmm. . . [She licks her lips].",
                "Ok, fine."])
            ch_s "[Line]"
            $ Line = 0
        $ character.Statup("Obed", 20, 1)
        $ character.Statup("Obed", 70, 1)
        $ character.Statup("Inbt", 80, 2)
        jump Storm_BJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ character.FaceChange("angry")
        if "no blow" in character.DailyActions:
            ch_s "You will need to accept a \"no\", [character.Petname]."
        elif Taboo and "tabno" in character.DailyActions and "no blow" in character.DailyActions:
            ch_s "I told you, this is too public!"
        elif "no blow" in character.DailyActions:
            ch_s "I told you \"no,\" [character.Petname]."
        elif Taboo and "tabno" in character.DailyActions:
            ch_s "I told you this is too public!"
        elif not character.Blow:
            $ character.FaceChange("bemused")
            ch_s "I am not sure I would enjoy this, [character.Petname]. . ."
        else:
            $ character.FaceChange("bemused")
            ch_s "Perhaps later, [character.Petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no blow" in character.DailyActions:
                $ character.FaceChange("bemused")
                ch_s "It is fine, [character.Petname]."
                return
            "Maybe later?" if "no blow" not in character.DailyActions:
                $ character.FaceChange("sexy")
                ch_s "I would not rule it out, [character.Petname]."
                $ character.Statup("Love", 80, 2)
                $ character.Statup("Inbt", 70, 2)
                if Taboo:
                    $ character.RecentActions.append("tabno")
                    $ character.DailyActions.append("tabno")
                $ character.RecentActions.append("no blow")
                $ character.DailyActions.append("no blow")
                return
            "Come on, please?":
                if Approval:
                    $ character.FaceChange("sexy")
                    $ character.Statup("Obed", 90, 2)
                    $ character.Statup("Obed", 50, 2)
                    $ character.Statup("Inbt", 70, 3)
                    $ character.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Well, I suppose.",
                        "Well. . . ok.",
                        "I could perhaps give it a try.",
                        "I suppose that I could. . .",
                        "Fine. . . [She licks her lips].",
                        "Hmph, ok, fine."])
                    ch_s "[Line]"
                    $ Line = 0
                    jump Storm_BJ_Prep
                else:
                    if ApprovalCheck(character, 1100, TabM = 3): # 110, 125, 140, Taboo -120(230)             Handy instead?
                        $ character.Statup("Inbt", 80, 1)
                        $ character.Statup("Inbt", 60, 3)
                        $ character.FaceChange("confused", 1)
                        $ character.ArmPose = 2
                        if character.Hand:
                            ch_s "I could just stroke you off, perhaps?"
                        else:
                            ch_s "Would my hand be an adequate substitute?"
                        menu:
                            extend ""
                            "Sure, that's fine.":
                                $ character.Statup("Love", 80, 2)
                                $ character.Statup("Inbt", 60, 1)
                                $ character.Statup("Obed", 50, 1)
                                jump Storm_HJ_Prep
                            "Nah, if it's not your mouth, forget it.":
                                $ character.Statup("Love", 200, -2)
                                $ character.ArmPose = 1
                                ch_s "That is unfortunate."
                                $ character.Statup("Obed", 70, 2)


            "Suck it, [character.Pet]":                                               # Pressured into it
                $ character.NameCheck() #checks reaction to petname
                $ Approval = ApprovalCheck(character, 750, "OI", TabM = 3) # 75, 90, 105, -120(195)
                if Approval > 1 or (Approval and character.Forced):
                    $ character.FaceChange("sad")
                    $ character.Statup("Love", 70, -5, 1)
                    $ character.Statup("Love", 200, -2)

                    $ character.Statup("Obed", 50, 4)
                    $ character.Statup("Inbt", 80, 1)
                    $ character.Statup("Inbt", 60, 3)
                    $ character.Forced = 1
                    jump Storm_BJ_Prep
                else:
                    $ character.Statup("Love", 200, -15)
                    $ character.RecentActions.append("angry")
                    $ character.DailyActions.append("angry")

    #She refused all offers.
    if "no blow" in character.DailyActions:
        $ character.FaceChange("angry", 1)

        $ character.RecentActions.append("angry")
        $ character.DailyActions.append("angry")
    elif character.Forced:
        $ character.FaceChange("angry", 1)
        ch_s "You go too far!"
        $ character.Statup("Lust", 200, 5)
        if character.Love > 300:
                $ character.Statup("Love", 70, -2)
        $ character.Statup("Obed", 50, -2)
        $ character.RecentActions.append("angry")
        $ character.DailyActions.append("angry")
        $ character.RecentActions.append("no blow")
        $ character.DailyActions.append("no blow")
        return
    elif Taboo:                             # she refuses and this is too public a place for her
        $ character.FaceChange("angry", 1)
        $ character.DailyActions.append("tabno")
        ch_s "This is much too exposed."
        $ character.Statup("Lust", 200, 5)
        $ character.Statup("Obed", 50, -3)
        return
    elif character.Blow:
        $ character.FaceChange("sad")
        ch_s "I am just not in the mood, [character.Petname]."
    else:
        $ character.FaceChange("normal", 1)
        ch_s "I do not think that I will."
    $ character.RecentActions.append("no blow")
    $ character.DailyActions.append("no blow")
    $ temp_modifier = 0
    return


label Storm_BJ_Prep:
    if renpy.showing("Storm_HJ_Animation"):
        hide Storm_HJ_Animation with easeoutbottom
    if Taboo:
        $ character.Inbt += int(Taboo/10)
        $ character.Lust += int(Taboo/5)

    $ character.FaceChange("sexy")
    if character.Forced:
        $ character.FaceChange("sad")

    call Seen_First_Peen(character,Partner,React=Situation)
    call Storm_BJ_Launch("L")

    if Situation == character:
            #Storm auto-starts
            $ Situation = 0
            "[character.Name] slides down and places your cock against her lips."
            menu:
                "What do you do?"
                "Nothing.":
                    $ character.Statup("Inbt", 80, 3)
                    $ character.Statup("Inbt", 40, 2)
                    "[character.Name] continues licking at it."
                "Praise her.":
                    $ character.FaceChange("sexy", 1)
                    $ character.Statup("Inbt", 80, 3)
                    ch_p "Hmmm, keep doing that, [character.Pet]."
                    $ character.NameCheck() #checks reaction to petname
                    "[character.Name] continues her actions."
                    $ character.Statup("Love", 85, 1)
                    $ character.Statup("Obed", 90, 1)
                    $ character.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ character.FaceChange("surprised")
                    $ character.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [character.Pet]."
                    $ character.NameCheck() #checks reaction to petname
                    "[character.Name] puts it down."
                    $ character.Statup("Obed", 90, 1)
                    $ character.Statup("Obed", 50, 3)
                    $ Player.RecentActions.append("nope")
                    $ character.AddWord(1,"refused","refused")
                    return
    if not character.Blow:
        if character.Forced:
            $ character.Statup("Love", 90, -70)
            $ character.Statup("Obed", 70, 45)
            $ character.Statup("Inbt", 80, 60)
        else:
            $ character.Statup("Love", 90, 5)
            $ character.Statup("Obed", 70, 35)
            $ character.Statup("Inbt", 80, 40)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ character.DrainWord("tabno")
    $ character.DrainWord("no blow")
    $ character.RecentActions.append("blow")
    $ character.DailyActions.append("blow")

label Storm_BJ_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(character)
        call Storm_BJ_Launch
        $ character.LustFace()

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
                                if "pushed" not in character.RecentActions and character.Blow < 5:
                                    $ character.Statup("Love", 80, -(20-(2*character.Blow)))
                                    $ character.Statup("Obed", 80, (30-(3*character.Blow)))
                                    $ character.RecentActions.append("pushed")
                                if Trigger2 == "jackin" and Speed != 3:
                                    "She takes it to the root, and you move your hand out of the way."
                                $ Speed = 4
                        "Take it deeper. (locked)" if Speed == 4:
                                pass

                        "Set your own pace. . .":
                                "[character.Name] hums contentedly."
                                if "setpace" not in character.RecentActions:
                                    $ character.Statup("Love", 80, 2)
                                $ D20 = renpy.random.randint(1, 20)
                                if character.Blow < 5:
                                    $ D20 -= 10
                                elif character.Blow < 10:
                                    $ D20 -= 5

                                if D20 > 15:
                                    $ Speed = 4
                                    if "setpace" not in character.RecentActions:
                                        $ character.Statup("Inbt", 80, 3)
                                elif D20 > 10:
                                    $ Speed = 3
                                elif D20 > 5:
                                    $ Speed = 2
                                else:
                                    $ Speed = 1
                                $ character.RecentActions.append("setpace")

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
                                            if character.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ character.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(character,"tired")

                                    "Shift primary action":
                                            if character.Action and MultiAction:
                                                    menu:
                                                        "How about a handy?":
                                                                $ Situation = "shift"
                                                                call Storm_BJ_After
                                                                call Storm_Handjob
                                                        "How about a titjob?":
                                                                $ Situation = "shift"
                                                                call Storm_BJ_After
                                                                call Storm_Titjob
                                                        "Never Mind":
                                                                jump Storm_BJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(character,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [character.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(character)
                                            "Asks [character.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(character)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(character)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Storm_BJ_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Storm_BJ_Cycle
                                            "Never mind":
                                                        jump Storm_BJ_Cycle
                                    "Undress [character.Name]":
                                            call Girl_Undress(character)
                                    "Clean up [character.Name] (locked)" if not character.Spunk:
                                            pass
                                    "Clean up [character.Name]" if character.Spunk:
                                            call Girl_Cleanup(character,"ask")
                                    "Never mind":
                                            jump Storm_BJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Storm_BJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Storm_BJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Storm_BJ_Reset
                                    $ Line = 0
                                    jump Storm_BJ_After
        #End menu (if Line)

        call Shift_Focus(character)
        call Sex_Dialog(character,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1
        if Speed:
            $ Player.Wet = 1 #wets penis
            $ Player.Spunk = 0 if Player.Spunk else Player.Spunk #cleans you off after one cycle

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or character.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(character)
                            if "angry" in character.RecentActions:
                                call Storm_BJ_Reset
                                return
                            $ character.Statup("Lust", 200, 5)
                            if 100 > character.Lust >= 70 and character.OCount < 2 and character.SEXP >= 20:
                                $ character.RecentActions.append("unsatisfied")
                                $ character.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Storm_BJ_After
                            $ Line = "came"

                    if character.Lust >= 100:
                            #If [character.Name] can cum
                            call Girl_Cumming(character)
                            if Situation == "shift" or "angry" in character.RecentActions:
                                jump Storm_BJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in character.RecentActions:#And [character.Name] is unsatisfied,
                                    "[character.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Storm_BJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if character.SEXP >= 100 or ApprovalCheck(character, 1200, "LO"):
            pass
        elif Cnt == (15 + character.Blow):
                $ character.Brows = "angry"
                menu:
                    ch_s "My jaw is becoming uncomfortable, could we do something else?"
                    "How about a Handy?" if character.Action and MultiAction:
                            $ Situation = "shift"
                            call Storm_BJ_After
                            call Storm_Handjob
                            return
                    "Finish up." if Player.FocusX:
                            "You release your concentration. . ."
                            $ Player.FocusX = 0
                            $ Player.Focus += 15
                            $ Cnt += 1
                            "[Line]."
                            jump Storm_BJ_Cycle
                    "Let's try something else." if MultiAction:
                            $ Line = 0
                            call Storm_BJ_Reset
                            $ Situation = "shift"
                            jump Storm_BJ_After
                    "No, get back down there.":
                            if ApprovalCheck(character, 1200) or ApprovalCheck(character, 500, "O"):
                                $ character.Statup("Love", 200, -5)
                                $ character.Statup("Obed", 50, 3)
                                $ character.Statup("Obed", 80, 2)
                                "She scowls but gets back to work."
                            else:
                                $ character.FaceChange("angry", 1)
                                "She scowls at you, drops you cock and pulls back."
                                ch_s "Well then."
                                $ character.Statup("Love", 50, -3, 1)
                                $ character.Statup("Love", 80, -4, 1)
                                $ character.Statup("Obed", 30, -1, 1)
                                $ character.Statup("Obed", 50, -1, 1)
                                $ character.RecentActions.append("angry")
                                $ character.DailyActions.append("angry")
                                jump Storm_BJ_After
        elif Cnt == (10 + character.Blow) and character.SEXP <= 100 and not ApprovalCheck(character, 1200, "LO"):
                    $ character.Brows = "confused"
                    ch_s "Are you about finished? I am growing tired of this."
        #End Count check

        call Escalation(character) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(character,10) #"It is getting late, [Girl.Petname]. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(character,5)   #"We should take a break soon."

    #Round = 0 loop breaks
    $ character.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(character,"done") # ch_s "I need to take a moment to collect myself."

label Storm_BJ_After:
    $ character.FaceChange("sexy")

    $ character.Blow += 1
    $ character.Action -=1
    $ character.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ character.Addictionrate += 1

    call Partner_Like(character,2)

    if "Storm Jobber" in Achievements:
        pass
    elif character.Blow >= 10:
        $ character.FaceChange("smile", 1)
        ch_s "I cannot imagine how I went this long without such a delicacy, [character.Petname]."
        $ Achievements.append("Storm Jobber")
        $character.SEXP += 5
    elif Situation == "shift":
        pass
    elif character.Blow == 1:
            $character.SEXP += 15
            if character.Love >= 500:
                $ character.Mouth = "smile"
                ch_s "Hmm, that certainly was enjoyable . ."
            elif Player.Focus <= 20:
                $ character.Mouth = "sad"
                ch_s "did that meet your expectations?"
    elif character.Blow == 5:
        ch_s "I expect that you enjoyed that."
    $ temp_modifier = 0
    if Situation != "shift":
        call Storm_BJ_Reset
    call Checkout
    return



# end character.Blowjob                                 //////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy
label Storm_Dildo_Check:
    if "dildo" in Player.Inventory:
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in character.Inventory:
        "You ask [character.Name] to get out her favorite Dildo."
    else:
        "You don't have one of those on you."
        return 0
    return 1

label Storm_Dildo_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(character)
    call Storm_Dildo_Check
    if not _return:
        return

    if character.DildoP: #You've done it before
        $ temp_modifier += 15
    if character.PantsNum() >= 6: # she's got pants on.
        $ temp_modifier -= 20

    if character.Lust > 95:
        $ temp_modifier += 20
    elif character.Lust > 85: #She's really horny
        $ temp_modifier += 15

    if Situation == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in character.Traits:
        $ temp_modifier += (5*Taboo)
    if character in Player.Harem or "sex friend" in character.Petnames:
        $ temp_modifier += 10
    elif "ex" in character.Traits:
        $ temp_modifier -= 40
    if character.ForcedCount and not character.Forced:
        $ temp_modifier -= 5 * character.ForcedCount

    if Taboo and "tabno" in character.DailyActions:
        $ temp_modifier -= 10

    if "no dildo" in character.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no dildo" in character.RecentActions else 0

    $ Approval = ApprovalCheck(character, 1250, TabM = 4) # 125, 140, 155, Taboo -160(335)

    if Situation == character:                                                                  #Storm auto-starts
                if Approval > 2:                                                      # fix, add emma auto stuff here
                    if character.PantsNum() == 5:
                        "[character.Name] grabs her dildo, hiking up her skirt as she does."
                        $ character.Upskirt = 1
                    elif character.PantsNum() > 6:
                        "[character.Name] grabs her dildo, pulling down her pants as she does."
                        $ character.Legs = 0
                    else:
                        "[character.Name] grabs her dildo, rubbing is suggestively against her crotch."
                    $ character.SeenPanties = 1
                    "She slides the tip along her pussy and seems to want you to insert it."
                    menu:
                        "What do you do?"
                        "Nothing.":
                            $ character.Statup("Inbt", 80, 3)
                            $ character.Statup("Inbt", 50, 2)
                            "[character.Name] slides it in."
                        "Go for it.":
                            $ character.FaceChange("sexy", 1)
                            $ character.Statup("Inbt", 80, 3)
                            ch_p "Oh yeah, [character.Pet], let's do this."
                            $ character.NameCheck() #checks reaction to petname
                            "You grab the dildo and slide it in."
                            $ character.Statup("Love", 85, 1)
                            $ character.Statup("Obed", 90, 1)
                            $ character.Statup("Obed", 50, 2)
                        "Ask her to stop.":
                            $ character.FaceChange("surprised")
                            $ character.Statup("Inbt", 70, 1)
                            ch_p "Let's not do that right now, [character.Pet]."
                            $ character.NameCheck() #checks reaction to petname
                            "[character.Name] sets the dildo down."
                            $ character.OutfitChange()
                            $ character.Statup("Obed", 90, 1)
                            $ character.Statup("Obed", 50, 1)
                            $ character.Statup("Obed", 30, 2)
                            return
                    jump Storm_DP_Prep
                else:
                    $ temp_modifier = 0                               # fix, add emma auto stuff here
                    $ Trigger2 = 0
                return

    if Situation == "auto":
                "You rub the dildo across her body, and along her moist slit."
                $ character.FaceChange("surprised", 1)

                if (character.DildoP and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
                    "[character.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                    $ character.FaceChange("sexy")
                    $ character.Statup("Obed", 70, 3)
                    $ character.Statup("Inbt", 50, 3)
                    $ character.Statup("Inbt", 70, 1)
                    ch_s "Hmm, [character.Petname], toys!"
                    jump Storm_DP_Prep
                else:                                                                                                            #she's questioning it
                    $ character.Brows = "angry"
                    menu:
                        ch_s "Excuse yourself, what are you planning to do with that?!"
                        "Sorry, sorry! Never mind.":
                            if Approval:
                                $ character.FaceChange("sexy", 1)
                                $ character.Statup("Obed", 70, 3)
                                $ character.Statup("Inbt", 50, 3)
                                $ character.Statup("Inbt", 70, 1)
                                ch_s "Well, now that you mention it. . ."
                                jump Storm_DP_Prep
                            "You pull back before you really get it in."
                            $ character.FaceChange("bemused", 1)
                            if character.DildoP:
                                ch_s "Well, [character.Petname], maybe warn me next time?"
                            else:
                                ch_s "Well, [character.Petname], that's a little much. . . for now . . ."
                        "Just playing with my favorite toys.":
                            $ character.Statup("Love", 80, -10, 1)
                            $ character.Statup("Love", 200, -10)
                            "You press it inside some more."
                            $ character.Statup("Obed", 70, 3)
                            $ character.Statup("Inbt", 50, 3)
                            if not ApprovalCheck(character, 700, "O", TabM=1): #Checks if Obed is 700+
                                $ character.FaceChange("angry")
                                "[character.Name] shoves you away and slaps you in the face."
                                ch_s "Ask nicely before trying anything like that!"
                                $ character.Statup("Love", 50, -10, 1)
                                $ character.Statup("Obed", 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                if renpy.showing("Storm_SexSprite"):
                                    call Storm_Sex_Reset
                                $ character.RecentActions.append("angry")
                                $ character.DailyActions.append("angry")
                            else:
                                $ character.FaceChange("sad")
                                "[character.Name] doesn't seem to be into this, you're lucky she's so obedient."
                                jump Storm_DP_Prep
                return
    #end Auto

    if not character.DildoP:
            #first time
            $ character.FaceChange("surprised", 1)
            $ character.Mouth = "kiss"
            ch_s "Hmmm, so you'd like to try out some toys?"
            if character.Forced:
                $ character.FaceChange("sad")
                ch_s "I suppose there are worst things you could ask for."

    if not character.DildoP and Approval:
            #First time dialog
            if character.Forced:
                $ character.FaceChange("sad")
                $ character.Statup("Love", 70, -3, 1)
                $ character.Statup("Love", 20, -2, 1)
            elif character.Love >= (character.Obed + character.Inbt):
                $ character.FaceChange("sexy")
                $ character.Brows = "sad"
                $ character.Mouth = "smile"
                ch_s "I've had a reasonable amount of experience with these, you know. . ."
            elif character.Obed >= character.Inbt:
                $ character.FaceChange("normal")
                ch_s "If that is what you want, [character.Petname]. . ."
            else: # Uninhibited
                $ character.FaceChange("sad")
                $ character.Mouth = "smile"
                ch_s "I guess it could be fun with a partner. . ."

    elif Approval:
            #Second time+ dialog
            if character.Forced:
                $ character.FaceChange("sad")
                $ character.Statup("Love", 70, -3, 1)
                $ character.Statup("Love", 20, -2, 1)
                ch_s "The toys again?"
            elif not Taboo and "tabno" in character.DailyActions:
                ch_s "Well, at least you got us some privacy this time. . ."
            elif "dildo pussy" in character.RecentActions:
                $ character.FaceChange("sexy", 1)
                ch_s "Mmm, again? Ok, let's get to it."
                jump Storm_DP_Prep
            elif "dildo pussy" in character.DailyActions:
                $ character.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Breaking out the toys again?",
                    "You did not get enough earlier?",
                    "You're going to wear me out."])
                ch_s "[Line]"
            elif character.DildoP < 3:
                $ character.FaceChange("sexy", 1)
                $ character.Brows = "confused"
                $ character.Mouth = "kiss"
                ch_s "You want to stick it in my pussy again?"
            else:
                $ character.FaceChange("sexy", 1)
                $ character.ArmPose = 2
                $ Line = renpy.random.choice(["You want some of this action?",
                    "So you'd like another go?",
                    "You want to stick it in my pussy again?",
                    "You want me ta lube up your toy?"])
                ch_s "[Line]"
                $ Line = 0

    if Approval >= 2:
            #She's into it. . .
            if character.Forced:
                $ character.FaceChange("sad")
                $ character.Statup("Obed", 90, 1)
                $ character.Statup("Inbt", 60, 1)
                ch_s "Ok, fine."
            else:
                $ character.FaceChange("sexy", 1)
                $ character.Statup("Love", 90, 1)
                $ character.Statup("Inbt", 50, 3)
                $ Line = renpy.random.choice(["Well, sure, stick it in.",
                    "Well. . . ok.",
                    "Sure!",
                    "I guess I could. . . stick it in.",
                    "Delightful.",
                    "Hmm, ok, ok."])
                ch_s "[Line]"
                $ Line = 0
            $ character.Statup("Obed", 20, 1)
            $ character.Statup("Obed", 60, 1)
            $ character.Statup("Inbt", 70, 2)
            jump Storm_DP_Prep

    else:
            #She's not into it, but maybe. . .
            $ character.FaceChange("angry")
            if "no dildo" in character.RecentActions:
                ch_s "What part of \"no,\" did you not get, [character.Petname]?"
            elif Taboo and "tabno" in character.DailyActions and "no dildo" in character.DailyActions:
                ch_s "Stop showing that thing around in public!"
            elif "no dildo" in character.DailyActions:
                ch_s "I already told you \"no,\" [character.Petname]."
            elif Taboo and "tabno" in character.DailyActions:
                ch_s "Stop showing that thing around in public!"
            elif not character.DildoP:
                $ character.FaceChange("bemused")
                ch_s "I'm a bit past toys, [character.Petname]. . ."
            else:
                $ character.FaceChange("bemused")
                ch_s "We don't need any toys, do we, [character.Petname]?"
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in character.DailyActions:
                    $ character.FaceChange("bemused")
                    ch_s "I thought as much, [character.Petname]."
                    return
                "Maybe later?" if "no dildo" not in character.DailyActions:
                    $ character.FaceChange("sexy")
                    ch_s "Maybe I'll practice on my own time, [character.Petname]."
                    $ character.Statup("Love", 80, 2)
                    $ character.Statup("Inbt", 70, 2)
                    if Taboo:
                        $ character.RecentActions.append("tabno")
                        $ character.DailyActions.append("tabno")
                    $ character.RecentActions.append("no dildo")
                    $ character.DailyActions.append("no dildo")
                    return
                "I think you'd like it. . .":
                    if Approval:
                        $ character.FaceChange("sexy")
                        $ character.Statup("Obed", 90, 2)
                        $ character.Statup("Obed", 50, 2)
                        $ character.Statup("Inbt", 70, 3)
                        $ character.Statup("Inbt", 40, 2)
                        $ Line = renpy.random.choice(["Well, sure, stick it in.",
                            "I suppose. . .",
                            "You make a compelling argument."])
                        ch_s "[Line]"
                        $ Line = 0
                        jump Storm_DP_Prep
                    else:
                        pass

                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck(character, 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                    if Approval > 1 or (Approval and character.Forced):
                        $ character.FaceChange("sad")
                        $ character.Statup("Love", 70, -5, 1)
                        $ character.Statup("Love", 200, -5)
                        ch_s
                        $ character.Statup("Obed", 80, 4)
                        $ character.Statup("Inbt", 80, 1)
                        $ character.Statup("Inbt", 60, 3)
                        $ character.Forced = 1
                        jump Storm_DP_Prep
                    else:
                        $ character.Statup("Love", 200, -20)
                        $ character.RecentActions.append("angry")
                        $ character.DailyActions.append("angry")

    #She refused all offers.
    $ character.ArmPose = 1
    if "no dildo" in character.DailyActions:

            $ character.RecentActions.append("angry")
            $ character.DailyActions.append("angry")
    elif character.Forced:
            $ character.FaceChange("angry", 1)
            ch_s "I'm not going to let you use that on me."
            $ character.Statup("Lust", 200, 5)
            if character.Love > 300:
                    $ character.Statup("Love", 70, -2)
            $ character.Statup("Obed", 50, -2)
            $ character.RecentActions.append("angry")
            $ character.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
            $ character.FaceChange("angry", 1)
            $ character.RecentActions.append("tabno")
            $ character.DailyActions.append("tabno")
            ch_s "Not here!"
            $ character.Statup("Lust", 200, 5)
            $ character.Statup("Obed", 50, -3)
    elif character.DildoP:
            $ character.FaceChange("sad")
            ch_s "Sorry, you can keep your toys to yourself."
    else:
            $ character.FaceChange("normal", 1)
            ch_s "No way."
    $ character.RecentActions.append("no dildo")
    $ character.DailyActions.append("no dildo")
    $ temp_modifier = 0
    return

label Storm_DP_Prep: #Animation set-up
    if Trigger2 == "dildo pussy":
        return

    if not character.Forced and Situation != "auto":
        $ temp_modifier = 15 if character.PantsNum() > 6 else 0
        call Bottoms_Off(character)
        if "angry" in character.RecentActions:
            return

    $ temp_modifier = 0
    call Storm_Pussy_Launch("dildo pussy")
    if not character.DildoP:
        if character.Forced:
            $ character.Statup("Love", 90, -75)
            $ character.Statup("Obed", 70, 60)
            $ character.Statup("Inbt", 80, 35)
        else:
            $ character.Statup("Love", 90, 10)
            $ character.Statup("Obed", 70, 20)
            $ character.Statup("Inbt", 80, 45)
    if Taboo:
        $ character.Inbt += int(Taboo/10)
        $ character.Lust += int(Taboo/5)


    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ character.DrainWord("tabno")
    $ character.DrainWord("no dildo")
    $ character.RecentActions.append("dildo pussy")
    $ character.DailyActions.append("dildo pussy")

label Storm_DP_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(character)
        call Storm_Pussy_Launch("dildo pussy")
        $ character.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                call Slap_Ass(character)
                                jump Storm_DP_Cycle

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
                                            if character.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ character.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(character,"tired")

                                    "Shift primary action":
                                            if character.Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in her ass.":
                                                                $ Situation = "shift"
                                                                call Storm_DP_After
                                                                call Storm_Insert_Ass
                                                        "Just stick a finger in her ass without asking.":
                                                                $ Situation = "auto"
                                                                call Storm_DP_After
                                                                call Storm_Insert_Ass
                                                        "I want to shift the dildo to her ass.":
                                                                $ Situation = "shift"
                                                                call Storm_DP_After
                                                                call Storm_Dildo_Ass
                                                        "Never Mind":
                                                                jump Storm_DP_Cycle
                                            else:
                                                call Sex_Basic_Dialog(character,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Storm_DP_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [character.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(character)
                                            "Asks [character.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(character)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(character)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Storm_DP_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Storm_DP_Cycle
                                            "Never mind":
                                                        jump Storm_DP_Cycle
                                    "Undress [character.Name]":
                                            call Girl_Undress(character)
                                    "Clean up [character.Name] (locked)" if not character.Spunk:
                                            pass
                                    "Clean up [character.Name]" if character.Spunk:
                                            call Girl_Cleanup(character,"ask")
                                    "Never mind":
                                            jump Storm_DP_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Storm_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Storm_DP_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Storm_Pos_Reset
                                    $ Line = 0
                                    jump Storm_DP_After
        #End menu (if Line)

        if character.Panties or character.PantsNum() > 6 or character.HoseNum() >= 5: #This checks if [character.Name] wants to strip down.
                call Girl_Undress(character,"auto")

        call Shift_Focus(character)
        call Sex_Dialog(character,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or character.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(character)
                            if "angry" in character.RecentActions:
                                call Storm_Pos_Reset
                                return
                            $ character.Statup("Lust", 200, 5)
                            if 100 > character.Lust >= 70 and character.OCount < 2:
                                $ character.RecentActions.append("unsatisfied")
                                $ character.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Storm_DP_After
                            $ Line = "came"
                    if character.Lust >= 100:
                            #If [character.Name] can cum
                            call Girl_Cumming(character)
                            if Situation == "shift" or "angry" in character.RecentActions:
                                jump Storm_DP_After
                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."
                            if "unsatisfied" in character.RecentActions:#And [character.Name] is unsatisfied,
                                    "[character.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Storm_DP_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if character.SEXP >= 100 or ApprovalCheck(character, 1200, "LO"):
            pass
        elif Cnt == (5 + character.DildoP):
                    $ character.Brows = "confused"
                    ch_s "What are you even doing down there?"
        elif character.Lust >= 80:
                    pass
        elif Cnt == (15 + character.DildoP) and character.SEXP >= 15 and not ApprovalCheck(character, 1500):
                    $ character.Brows = "confused"
                    menu:
                        ch_s "[character.Petname], this is getting uncomfortable, maybe we could try something else."
                        "Finish up.":
                                "You let go. . ."
                                jump Storm_DP_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Storm_DP_After
                        "No, this is fun.":
                                if ApprovalCheck(character, 1200) or ApprovalCheck(character, 500, "O"):
                                    $ character.Statup("Love", 200, -5)
                                    $ character.Statup("Obed", 50, 3)
                                    $ character.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ character.FaceChange("angry", 1)
                                    call Storm_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_s "Well if that's your attitude, I don't need your \"help\"."
                                    $ character.Statup("Love", 50, -3, 1)
                                    $ character.Statup("Love", 80, -4, 1)
                                    $ character.Statup("Obed", 30, -1, 1)
                                    $ character.Statup("Obed", 50, -1, 1)
                                    $ character.RecentActions.append("angry")
                                    $ character.DailyActions.append("angry")
                                    jump Storm_DP_After
        #End Count check

        if Round == 10:
                call Sex_Basic_Dialog(character,10) #"It is getting late, [Girl.Petname]. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(character,5)   #"We should take a break soon."

    #Round = 0 loop breaks
    $ character.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(character,"done") # ch_s "I need to take a moment to collect myself."


label Storm_DP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Storm_Pos_Reset

    $ character.FaceChange("sexy")

    $ character.DildoP += 1
    $ character.Action -=1

    call Partner_Like(character,1)

    if character.DildoP == 1:
            $ character.SEXP += 10
            if not Situation:
                if character.Love >= 500 and "unsatisfied" not in character.RecentActions:
                    ch_s "I appreciate the work you put in. . ."
                elif character.Obed <= 500 and Player.Focus <= 20:
                    $ character.FaceChange("perplexed", 1)
                    ch_s "Did you enjoy that?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_s "Mmm, so what else did you have in mind?"
    call Checkout
    return

# end character.Dildo Pussy /////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////Start Insert Ass

label Storm_Dildo_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(character)
    call Storm_Dildo_Check
    if not _return:
        return

    if character.Loose:
        $ temp_modifier += 30
    elif "anal" in character.RecentActions or "dildo anal" in character.RecentActions:
        $ temp_modifier -= 20
    elif "anal" in character.DailyActions or "dildo anal" in character.DailyActions:
        $ temp_modifier -= 10
    elif (character.Anal + character.DildoA + character.Plug) > 0: #You've done it before
        $ temp_modifier += 20

    if character.PantsNum() >= 6: # she's got pants on.
        $ temp_modifier -= 20

    if character.Lust > 95:
        $ temp_modifier += 20
    elif character.Lust > 85: #She's really horny
        $ temp_modifier += 15

    if Situation == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in character.Traits:
        $ temp_modifier += (5*Taboo)
    if character in Player.Harem or "sex friend" in character.Petnames:
        $ temp_modifier += 10
    elif "ex" in character.Traits:
        $ temp_modifier -= 40
    if character.ForcedCount and not character.Forced:
        $ temp_modifier -= 5 * character.ForcedCount

    if Taboo and "tabno" in character.DailyActions:
        $ temp_modifier -= 10

    if "no dildo" in character.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no dildo" in character.RecentActions else 0

    $ Approval = ApprovalCheck(character, 1450, TabM = 4) # 145, 160, 175, Taboo -160(355)

    if Situation == character:
            #Storm auto-starts
            if Approval > 2:                                                      # fix, add emma auto stuff here
                if character.PantsNum() == 5:
                    "[character.Name] grabs her dildo, hiking up her skirt as she does."
                    $ character.Upskirt = 1
                elif character.PantsNum() > 6:
                    "[character.Name] grabs her dildo, pulling down her pants as she does."
                    $ character.Legs = 0
                else:
                    "[character.Name] grabs her dildo, rubbing is suggestively against her ass."
                $ character.SeenPanties = 1
                "She slides the tip against her asshole, and seems to want you to insert it."
                menu:
                    "What do you do?"
                    "Nothing.":
                        $ character.Statup("Inbt", 80, 3)
                        $ character.Statup("Inbt", 50, 2)
                        "[character.Name] slides it in."
                    "Go for it.":
                        $ character.FaceChange("sexy", 1)
                        $ character.Statup("Inbt", 80, 3)
                        ch_p "Oh yeah, [character.Pet], let's do this."
                        $ character.NameCheck() #checks reaction to petname
                        "You grab the dildo and slide it in."
                        $ character.Statup("Love", 85, 1)
                        $ character.Statup("Obed", 90, 1)
                        $ character.Statup("Obed", 50, 2)
                    "Ask her to stop.":
                        $ character.FaceChange("surprised")
                        $ character.Statup("Inbt", 70, 1)
                        ch_p "Let's not do that right now, [character.Pet]."
                        $ character.NameCheck() #checks reaction to petname
                        "[character.Name] sets the dildo down."
                        $ character.OutfitChange()
                        $ character.Statup("Obed", 90, 1)
                        $ character.Statup("Obed", 50, 1)
                        $ character.Statup("Obed", 30, 2)
                        return
                jump Storm_DA_Prep
            else:
                $ temp_modifier = 0                               # fix, add emma auto stuff here
                $ Trigger2 = 0
            return

    if Situation == "auto":
            "You rub the dildo across her body, and against her tight anus."
            $ character.FaceChange("surprised", 1)

            if (character.DildoA and Approval) or (Approval > 1):
                #this is not the first time you've had sex, or she's into it
                "[character.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                $ character.FaceChange("sexy")
                $ character.Statup("Obed", 70, 3)
                $ character.Statup("Inbt", 50, 3)
                $ character.Statup("Inbt", 70, 1)
                ch_s "Mmmm, [character.Petname], toys. . ."
                jump Storm_DA_Prep
            else:
                #she's questioning it
                $ character.Brows = "angry"
                menu:
                    ch_s "Excuse yourself, what are you planning to do with that?!"
                    "Sorry, sorry! Never mind.":
                        if Approval:
                            $ character.FaceChange("sexy", 1)
                            $ character.Statup("Obed", 70, 3)
                            $ character.Statup("Inbt", 50, 3)
                            $ character.Statup("Inbt", 70, 1)
                            ch_s "Well, now that you mention it. . ."
                            jump Storm_DA_Prep
                        "You pull back before you really get it in."
                        $ character.FaceChange("bemused", 1)
                        if character.DildoA:
                            ch_s "Well, [character.Petname], maybe warn me next time?"
                        else:
                            ch_s "Well, [character.Petname], that's a little much. . . for now . . ."
                    "Just playing with my favorite toys.":
                        $ character.Statup("Love", 80, -10, 1)
                        $ character.Statup("Love", 200, -10)
                        "You press it inside some more."
                        $ character.Statup("Obed", 70, 3)
                        $ character.Statup("Inbt", 50, 3)
                        if not ApprovalCheck(character, 700, "O", TabM=1): #Checks if Obed is 700+
                            $ character.FaceChange("angry")
                            "[character.Name] shoves you away and slaps you in the face."
                            ch_s "Ask nicely if you want to stick something in my ass!"
                            $ character.Statup("Love", 50, -10, 1)
                            $ character.Statup("Obed", 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            if renpy.showing("Storm_SexSprite"):
                                call Storm_Sex_Reset
                            $ character.RecentActions.append("angry")
                            $ character.DailyActions.append("angry")
                        else:
                            $ character.FaceChange("sad")
                            "[character.Name] doesn't seem to be into this, you're lucky she's so obedient."
                            jump Storm_DA_Prep
            return
    #end auto

    if not character.DildoA:
            #first time
            $ character.FaceChange("surprised", 1)
            $ character.Mouth = "kiss"
            ch_s "Hmm, you don't take half measures. . ."
            if character.Forced:
                $ character.FaceChange("sad")
                ch_s "They always go for the butt. . ."

    if not character.DildoA and Approval:
            #First time dialog
            if character.Forced:
                $ character.FaceChange("sad")
                $ character.Statup("Love", 70, -3, 1)
                $ character.Statup("Love", 20, -2, 1)
            elif character.Love >= (character.Obed + character.Inbt):
                $ character.FaceChange("sexy")
                $ character.Brows = "sad"
                $ character.Mouth = "smile"
                ch_s "I suppose you might enjoy that. . ."
            elif character.Obed >= character.Inbt:
                $ character.FaceChange("normal")
                ch_s "If that is what you want, [character.Petname]. . ."
            else: # Uninhibited
                $ character.FaceChange("sad")
                $ character.Mouth = "smile"
                ch_s "I suppose I could enjoy that. . ."

    elif Approval:
            #Second time+ dialog
            if character.Forced:
                $ character.FaceChange("sad")
                $ character.Statup("Love", 70, -3, 1)
                $ character.Statup("Love", 20, -2, 1)
                ch_s "The toys again?"
            elif not Taboo and "tabno" in character.DailyActions:
                ch_s "Well, at least you got us some privacy this time. . ."
            elif "dildo anal" in character.DailyActions and not character.Loose:
                pass
            elif character.DildoA < 3:
                $ character.FaceChange("sexy", 1)
                $ character.Brows = "confused"
                $ character.Mouth = "kiss"
                ch_s "You want to stick it in my ass again?"
            else:
                $ character.FaceChange("sexy", 1)
                $ character.ArmPose = 2
                $ Line = renpy.random.choice(["You want some of this action?",
                    "So you'd like another go?",
                    "You'd like to stick it in my ass again?",
                    "You'd like me to lube up your toy?"])
                ch_s "[Line]"
                $ Line = 0

    if Approval >= 2:
            #She's into it. . .
            if character.Forced:
                $ character.FaceChange("sad")
                $ character.Statup("Obed", 90, 1)
                $ character.Statup("Inbt", 60, 1)
                ch_s "Oh, fine."
            else:
                $ character.FaceChange("sexy", 1)
                $ character.Statup("Love", 90, 1)
                $ character.Statup("Inbt", 50, 3)
                $ Line = renpy.random.choice(["Well, sure, stick it in.",
                    "Hmm. . . ok.",
                    "Sure!",
                    "I guess I could. . . stick it in.",
                    "Delightful.",
                    "Hmm, ok, ok."])
                ch_s "[Line]"
                $ Line = 0
            $ character.Statup("Obed", 20, 1)
            $ character.Statup("Obed", 60, 1)
            $ character.Statup("Inbt", 70, 2)
            jump Storm_DA_Prep

    else:
            #She's not into it, but maybe. . .
            $ character.FaceChange("angry")
            if "no dildo" in character.RecentActions:
                ch_s "What part of \"no,\" did you not get, [character.Petname]?"
            elif Taboo and "tabno" in character.DailyActions and "no dildo" in character.DailyActions:
                ch_s "Stop swinging that thing around in public!"
            elif "no dildo" in character.DailyActions:
                ch_s "I already told you \"no,\" [character.Petname]."
            elif Taboo and "tabno" in character.DailyActions:
                ch_s "I already told you that I wouldn't do that out here!"
            elif not character.DildoA:
                $ character.FaceChange("bemused")
                ch_s "I'm just not into toys, [character.Petname]. . ."
            else:
                $ character.FaceChange("bemused")
                ch_s "I don't think we need any toys, [character.Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in character.DailyActions:
                    $ character.FaceChange("bemused")
                    ch_s "I'm sure, [character.Petname]."
                    return
                "Maybe later?" if "no dildo" not in character.DailyActions:
                    $ character.FaceChange("sexy")
                    ch_s "Perhaps I'll practice on my own time, [character.Petname]."
                    $ character.Statup("Love", 80, 2)
                    $ character.Statup("Inbt", 70, 2)
                    if Taboo:
                        $ character.RecentActions.append("tabno")
                        $ character.DailyActions.append("tabno")
                    $ character.RecentActions.append("no dildo")
                    $ character.DailyActions.append("no dildo")
                    return
                "I think you'd like it. . .":
                    if Approval:
                        $ character.FaceChange("sexy")
                        $ character.Statup("Obed", 90, 2)
                        $ character.Statup("Obed", 50, 2)
                        $ character.Statup("Inbt", 70, 3)
                        $ character.Statup("Inbt", 40, 2)
                        $ Line = renpy.random.choice(["Very well, stick it in.",
                            "I suppose. . .",
                            "You make a compelling argument."])
                        ch_s "[Line]"
                        $ Line = 0
                        jump Storm_DA_Prep
                    else:
                        pass

                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck(character, 1050, "OI", TabM = 3) # 105, 120, 135, -120(225)
                    if Approval > 1 or (Approval and character.Forced):
                        $ character.FaceChange("sad")
                        $ character.Statup("Love", 70, -5, 1)
                        $ character.Statup("Love", 200, -5)

                        $ character.Statup("Obed", 80, 4)
                        $ character.Statup("Inbt", 80, 1)
                        $ character.Statup("Inbt", 60, 3)
                        $ character.Forced = 1
                        jump Storm_DA_Prep
                    else:
                        $ character.Statup("Love", 200, -20)
                        $ character.RecentActions.append("angry")
                        $ character.DailyActions.append("angry")

    #She refused all offers.
    $ character.ArmPose = 1
    if "no dildo" in character.DailyActions:

            $ character.RecentActions.append("angry")
            $ character.DailyActions.append("angry")
    elif character.Forced:
            $ character.FaceChange("angry", 1)
            ch_s "I'm not going to let you use that on me."
            $ character.Statup("Lust", 200, 5)
            if character.Love > 300:
                    $ character.Statup("Love", 70, -2)
            $ character.Statup("Obed", 50, -2)
            $ character.RecentActions.append("angry")
            $ character.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
            $ character.FaceChange("angry", 1)
            $ character.RecentActions.append("tabno")
            $ character.DailyActions.append("tabno")
            ch_s "Not here!"
            $ character.Statup("Lust", 200, 5)
            $ character.Statup("Obed", 50, -3)
    elif character.DildoA:
            $ character.FaceChange("sad")
            ch_s "Sorry, you can keep your toys out of there."
    else:
            $ character.FaceChange("normal", 1)
            ch_s "No, thank you."
    $ character.RecentActions.append("no dildo")
    $ character.DailyActions.append("no dildo")
    $ temp_modifier = 0
    return

label Storm_DA_Prep: #Animation set-up
    if Trigger2 == "dildo anal":
        return

    if not character.Forced and Situation != "auto":
        $ temp_modifier = 20 if character.PantsNum() > 6 else 0
        call Bottoms_Off(character)
        if "angry" in character.RecentActions:
            return

    $ temp_modifier = 0
    call Storm_Pussy_Launch("dildo anal")
    if not character.DildoA:
        if character.Forced:
            $ character.Statup("Love", 90, -75)
            $ character.Statup("Obed", 70, 60)
            $ character.Statup("Inbt", 80, 35)
        else:
            $ character.Statup("Love", 90, 10)
            $ character.Statup("Obed", 70, 20)
            $ character.Statup("Inbt", 80, 45)
    if Taboo:
        $ character.Inbt += int(Taboo/10)
        $ character.Lust += int(Taboo/5)


    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ character.DrainWord("tabno")
    $ character.DrainWord("no dildo")
    $ character.RecentActions.append("dildo anal")
    $ character.DailyActions.append("dildo anal")

label Storm_DA_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(character)
        call Storm_Pussy_Launch("dildo anal")
        $ character.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                call Slap_Ass(character)
                                jump Storm_DA_Cycle

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
                                            if character.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ character.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(character,"tired")

                                    "Shift primary action":
                                            if character.Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in her pussy.":
                                                                $ Situation = "shift"
                                                                call Storm_DA_After
                                                                call Storm_Fondle_Pussy
                                                        "Just stick a finger in her pussy without asking.":
                                                                $ Situation = "auto"
                                                                call Storm_DA_After
                                                                call Storm_Fondle_Pussy
                                                        "I want to shift the dildo to her pussy.":
                                                                $ Situation = "shift"
                                                                call Storm_DA_After
                                                                call Storm_Dildo_Pussy
                                                        "Never Mind":
                                                                jump Storm_DA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(character,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Storm_DA_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [character.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(character)
                                            "Asks [character.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(character)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(character)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Storm_DA_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Storm_DA_Cycle
                                            "Never mind":
                                                        jump Storm_DA_Cycle
                                    "Undress [character.Name]":
                                            call Girl_Undress(character)
                                    "Clean up [character.Name] (locked)" if not character.Spunk:
                                            pass
                                    "Clean up [character.Name]" if character.Spunk:
                                            call Girl_Cleanup(character,"ask")
                                    "Never mind":
                                            jump Storm_DA_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Storm_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Storm_DA_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Storm_Pos_Reset
                                    $ Line = 0
                                    jump Storm_DA_After
        #End menu (if Line)

        if character.Panties or character.PantsNum() > 6 or character.HoseNum() >= 5: #This checks if [character.Name] wants to strip down.
                call Girl_Undress(character,"auto")

        call Shift_Focus(character)
        call Sex_Dialog(character,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or character.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(character)
                            if "angry" in character.RecentActions:
                                call Storm_Pos_Reset
                                return
                            $ character.Statup("Lust", 200, 5)
                            if 100 > character.Lust >= 70 and character.OCount < 2:
                                $ character.RecentActions.append("unsatisfied")
                                $ character.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Storm_DA_After
                            $ Line = "came"

                    if character.Lust >= 100:
                            #If [character.Name] can cum
                            call Girl_Cumming(character)
                            if Situation == "shift" or "angry" in character.RecentActions:
                                jump Storm_DA_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in character.RecentActions:#And [character.Name] is unsatisfied,
                                    "[character.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Storm_DA_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if character.SEXP >= 100 or ApprovalCheck(character, 1200, "LO"):
            pass
        elif Cnt == (5 + character.DildoA):
                    $ character.Brows = "confused"
                    ch_s "What are you even doing down there?"
        elif character.Lust >= 80:
                    pass
        elif Cnt == (15 + character.DildoA) and character.SEXP >= 15 and not ApprovalCheck(character, 1500):
                    $ character.Brows = "confused"
                    menu:
                        ch_s "[character.Petname], this is getting uncomfortable, maybe we could try something else."
                        "Finish up.":
                                "You let go. . ."
                                jump Storm_DA_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Storm_DA_After
                        "No, this is fun.":
                                if ApprovalCheck(character, 1200) or ApprovalCheck(character, 500, "O"):
                                    $ character.Statup("Love", 200, -5)
                                    $ character.Statup("Obed", 50, 3)
                                    $ character.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ character.FaceChange("angry", 1)
                                    call Storm_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_s "Well if that's your attitude, I don't need your \"help\"."
                                    $ character.Statup("Love", 50, -3, 1)
                                    $ character.Statup("Love", 80, -4, 1)
                                    $ character.Statup("Obed", 30, -1, 1)
                                    $ character.Statup("Obed", 50, -1, 1)
                                    $ character.RecentActions.append("angry")
                                    $ character.DailyActions.append("angry")
                                    jump Storm_DA_After
        #End Count check

        if Round == 10:
                call Sex_Basic_Dialog(character,10) #"It is getting late, [Girl.Petname]. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(character,5)   #"We should take a break soon."

    #Round = 0 loop breaks
    $ character.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(character,"done") # ch_s "I need to take a moment to collect myself."


label Storm_DA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Storm_Pos_Reset

    $ character.FaceChange("sexy")

    $ character.DildoA += 1
    $ character.Action -=1

    call Partner_Like(character,1)

    if character.DildoA == 1:
            $ character.SEXP += 10
            if not Situation:
                if character.Love >= 500 and "unsatisfied" not in character.RecentActions:
                    ch_s "That was. . . engaging. . ."
                elif character.Obed <= 500 and Player.Focus <= 20:
                    $ character.FaceChange("perplexed", 1)
                    ch_s "Did you enjoy that?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_s "Mmm, so what else did you have in mind?"
    call Checkout
    return

# end character.Dildo Ass /////////////////////////////////////////////////////////////////////////////

label Storm_Vibrator_Check:                                                                                 #fix this whole section is copy/paste unfinished
    if "vibrator" in Player.Inventory:
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in character.Inventory:
        "You ask [character.Name] to get out her vibrator."
    else:
        "You don't have one of those on you."
        return 0
    return 1

## character.Footjob //////////////////////////////////////////////////////////////////////
label Storm_Footjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(character)
    if character.Foot >= 7: # She loves it
        $ temp_modifier += 10
    elif character.Foot >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif character.Foot: #You've done it before
        $ temp_modifier += 3

    if character.Addict >= 75 and character.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 10
    if character.Addict >= 75:
        $ temp_modifier += 5

    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in character.Traits:
        $ temp_modifier += (3*Taboo)
    if character in Player.Harem or "sex friend" in character.Petnames:
        $ temp_modifier += 10
    elif "ex" in character.Traits:
        $ temp_modifier -= 40
    if character.ForcedCount and not character.Forced:
        $ temp_modifier -= 5 * character.ForcedCount

    if Taboo and "tabno" in character.DailyActions:
        $ temp_modifier -= 10

    if "no foot" in character.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no foot" in character.RecentActions else 0

    $ Approval = ApprovalCheck(character, 1250, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if Situation == character:                                                                  #Storm auto-starts
        if Approval > 2:                                                      # fix, add emma auto stuff here
            if Trigger2 == "jackin":
                "[character.Name] lays back and starts rubbing her feet along your cock."
            else:
                "[character.Name] gives you a mischevious smile, and starts to rub her feet along your cock."
            menu:
                "What do you do?"
                "Nothing.":
                    $ character.Statup("Inbt", 70, 3)
                    $ character.Statup("Inbt", 30, 2)
                    "[character.Name] continues her actions."
                "Praise her.":
                    $ character.FaceChange("sexy", 1)
                    $ character.Statup("Inbt", 70, 3)
                    ch_p "Oooh, that's good, [character.Pet]."
                    $ character.NameCheck() #checks reaction to petname
                    "[character.Name] continues her actions."
                    $ character.Statup("Love", 80, 1)
                    $ character.Statup("Obed", 90, 1)
                    $ character.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ character.FaceChange("surprised")
                    $ character.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [character.Pet]."
                    $ character.NameCheck() #checks reaction to petname
                    "[character.Name] puts it down."
                    $ character.Statup("Obed", 90, 1)
                    $ character.Statup("Obed", 50, 1)
                    $ character.Statup("Obed", 30, 2)
                    return
            if Trigger:
                $ Trigger3 = "foot"
                return
            jump Storm_FJ_Prep
        else:
            $ temp_modifier = 0                               # fix, add emma auto stuff here
            $ Trigger2 = 0
            return

    if not character.Foot and "no foot" not in character.RecentActions:
        $ character.FaceChange("confused", 2)
        ch_s "Oh, you would like me to use my feet, [character.Petname]?"
        $ character.Blush = 1

    if not character.Foot and Approval:                                                 #First time dialog
        if character.Forced:
            $ character.FaceChange("sad",1)
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Love", 20, -2, 1)
        elif character.Love >= (character.Obed + character.Inbt):
            $ character.FaceChange("sexy",1)
            $ character.Brows = "sad"
            $ character.Mouth = "smile"
            ch_s "I could enjoy that. . ."
        elif character.Obed >= character.Inbt:
            $ character.FaceChange("normal",1)
            ch_s "If you enjoy that, [character.Petname]. . ."
        elif character.Addict >= 50:
            $ character.FaceChange("manic", 1)
            ch_s "Very well. . ."
        else: # Uninhibited
            $ character.FaceChange("lipbite",1)
            ch_s "Very well. . ."

    elif Approval:                                                                       #Second time+ dialog
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Love", 20, -2, 1)
            ch_s "That is all you want?"
        elif not Taboo and "tabno" in character.DailyActions:
            ch_s "I suppose this is secluded enough. . ."
        elif "foot" in character.RecentActions:
            $ character.FaceChange("sexy", 1)
            ch_s "I suppose so. . ."
            jump Storm_FJ_Prep
        elif "foot" in character.DailyActions:
            $ character.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Another?",
                "You did not get enough earlier?",
                "My feet are rather sore from earlier.",
                "My feet are rather sore from earlier."])
            ch_s "[Line]"
        elif character.Foot < 3:
            $ character.FaceChange("sexy", 1)
            $ character.Brows = "confused"
            $ character.Mouth = "kiss"
            ch_s "Oh, very well. . ."
        else:
            $ character.FaceChange("sexy", 1)
            $ character.ArmPose = 2
            $ Line = renpy.random.choice(["You would like me to use my feet again?",
                "So you would like another footjob?",
                "Mmmm, some. . . [she rubs her foot along your leg]?",
                "A little foot rub?"])
            ch_s "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Obed", 90, 1)
            $ character.Statup("Inbt", 60, 1)
            ch_s "I supose that would be fine."
        elif "no foot" in character.DailyActions:
            ch_s "Oh, very well."
        else:
            $ character.FaceChange("sexy", 1)
            $ character.Statup("Love", 90, 1)
            $ character.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Hmm, I suppose.",
                "Fine.",
                "Very well, bring it out.",
                "I suppose that I could. . .",
                "Fine. . . [She gestures for you to come over].",
                "Hmm, ok."])
            ch_s "[Line]"
            $ Line = 0
        $ character.Statup("Obed", 20, 1)
        $ character.Statup("Obed", 60, 1)
        $ character.Statup("Inbt", 70, 2)
        jump Storm_FJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ character.FaceChange("angry")
        if "no foot" in character.RecentActions:
            ch_s "I have made myself clear, [character.Petname]."
        elif Taboo and "tabno" in character.DailyActions and "no foot" in character.DailyActions:
            ch_s "I refuse to do this in public."
        elif "no foot" in character.DailyActions:
            ch_s "I said \"no,\" [character.Petname]."
        elif Taboo and "tabno" in character.DailyActions:
            ch_s "I informed you, not in public!"
        elif not character.Foot:
            $ character.FaceChange("bemused")
            ch_s "I am unsure, [character.Petname]. . ."
        else:
            $ character.FaceChange("bemused")
            ch_s "Not now, [character.Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no foot" in character.DailyActions:
                $ character.FaceChange("bemused")
                ch_s "Thank you."
                return
            "Maybe later?" if "no foot" not in character.DailyActions:
                $ character.FaceChange("sexy")
                ch_s ". . ."
                ch_s "Perhaps."
                $ character.Statup("Love", 80, 2)
                $ character.Statup("Inbt", 70, 2)
                if Taboo:
                    $ character.RecentActions.append("tabno")
                    $ character.DailyActions.append("tabno")
                $ character.RecentActions.append("no foot")
                $ character.DailyActions.append("no foot")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ character.FaceChange("sexy")
                    $ character.Statup("Obed", 90, 2)
                    $ character.Statup("Obed", 50, 2)
                    $ character.Statup("Inbt", 70, 3)
                    $ character.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Hmm, I suppose.",
                            "Fine.",
                            "Very well, bring it out.",
                            "I suppose that I could. . .",
                            "Fine. . . [She gestures for you to come over].",
                            "Hmm, ok."])
                    ch_s "[Line]"
                    $ Line = 0
                    jump Storm_FJ_Prep
                else:
                    pass

            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck(character, 400, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and character.Forced):
                    $ character.FaceChange("sad")
                    $ character.Statup("Love", 70, -5, 1)
                    $ character.Statup("Love", 200, -2)

                    $ character.Statup("Obed", 50, 4)
                    $ character.Statup("Inbt", 80, 1)
                    $ character.Statup("Inbt", 60, 3)
                    $ character.Forced = 1
                    jump Storm_FJ_Prep
                else:
                    $ character.Statup("Love", 200, -15)
                    $ character.RecentActions.append("angry")
                    $ character.DailyActions.append("angry")

    #She refused all offers.
    $ character.ArmPose = 1
    if "no foot" in character.DailyActions:
        $ character.FaceChange("angry", 1)

        $ character.RecentActions.append("angry")
        $ character.DailyActions.append("angry")
    elif character.Forced:
        $ character.FaceChange("angry", 1)
        ch_s "Do not tempt me to show you what my feet can do."
        $ character.Statup("Lust", 200, 5)
        if character.Love > 300:
                $ character.Statup("Love", 70, -2)
        $ character.Statup("Obed", 50, -2)
        $ character.RecentActions.append("angry")
        $ character.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ character.FaceChange("angry", 1)
        $ character.DailyActions.append("tabno")
        ch_s "This truly is not an appropriate place for that."
        $ character.Statup("Lust", 200, 5)
        $ character.Statup("Obed", 50, -3)
    elif character.Foot:
        $ character.FaceChange("sad")
        ch_s "I am in no mood, [character.Petname]. . ."
    else:
        $ character.FaceChange("normal", 1)
        ch_s "I am truly in no mood for footplay today. . ."
    $ character.RecentActions.append("no foot")
    $ character.DailyActions.append("no foot")
    $ temp_modifier = 0
    return


label Storm_FJ_Prep:
    if Trigger2 == "foot":
        return

    if Taboo:
        $ character.Inbt += int(Taboo/10)
        $ character.Lust += int(Taboo/5)

    $ character.FaceChange("sexy")
    if character.Forced:
        $ character.FaceChange("sad")
    elif not character.Foot:
        $ character.Brows = "confused"
        $ character.Eyes = "sexy"
        $ character.Mouth = "smile"

    call Seen_First_Peen(character,Partner,React=Situation)
    if not character.Foot:
        if character.Forced:
            $ character.Statup("Love", 90, -20)
            $ character.Statup("Obed", 70, 25)
            $ character.Statup("Inbt", 80, 30)
        else:
            $ character.Statup("Love", 90, 5)
            $ character.Statup("Obed", 70, 20)
            $ character.Statup("Inbt", 80, 20)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ character.DrainWord("tabno")
    $ character.DrainWord("no foot")
    $ character.RecentActions.append("foot")
    $ character.DailyActions.append("foot")

label Storm_FJ_Cycle:
    while Round > 0:
        call Shift_Focus(character)
        call Storm_Sex_Launch("foot")
        $ character.LustFace()

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
                                    "I also want to fondle her thighs." if Trigger2 != "fondle thighs":
                                            if MultiAction:
                                                $ Trigger2 = "fondle thighs"
                                                "You start to fondle her thighs."
                                            else:
                                                call Sex_Basic_Dialog(character,"tired")

                                    "Shift primary action":
                                            if character.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                $ Situation = "shift"
                                                                call Storm_FJ_After
                                                                call Storm_Blowjob
                                                        "How about a handjob?":
                                                                $ Situation = "shift"
                                                                call Storm_FJ_After
                                                                call Storm_Handjob
                                                        "How about a titjob?":
                                                                $ Situation = "shift"
                                                                call Storm_FJ_After
                                                                call Storm_Titjob

                                                        "Never Mind":
                                                                jump Storm_FJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(character,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [character.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(character)
                                            "Asks [character.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(character)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(character)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Storm_FJ_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Storm_FJ_Cycle
                                            "Never mind":
                                                        jump Storm_FJ_Cycle
                                    "Undress [character.Name]":
                                            call Girl_Undress(character)
                                    "Clean up [character.Name] (locked)" if not character.Spunk:
                                            pass
                                    "Clean up [character.Name]" if character.Spunk:
                                            call Girl_Cleanup(character,"ask")
                                    "Never mind":
                                            jump Storm_FJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Storm_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Storm_FJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Storm_Sex_Reset
                                    $ Line = 0
                                    jump Storm_FJ_After
        #End menu (if Line)

        call Shift_Focus(character)
        call Sex_Dialog(character,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or character.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(character)
                            if "angry" in character.RecentActions:
                                call Storm_Sex_Reset
                                return
                            $ character.Statup("Lust", 200, 5)
                            if 100 > character.Lust >= 70 and character.OCount < 2:
                                $ character.RecentActions.append("unsatisfied")
                                $ character.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Storm_FJ_After
                            $ Line = "came"

                    if character.Lust >= 100:
                            #If [character.Name] can cum
                            call Girl_Cumming(character)
                            if Situation == "shift" or "angry" in character.RecentActions:
                                jump Storm_FJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in character.RecentActions:#And [character.Name] is unsatisfied,
                                    "[character.Name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Storm_FJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Cnt == 20:
                    $ character.Brows = "angry"
                    menu:
                        ch_s "Hmm, foot cramp. Could we take a short break?"
                        "How about a BJ?" if character.Action and MultiAction:
                                $ Situation = "shift"
                                call Storm_FJ_After
                                call Storm_Blowjob
                        "How about a Handy?" if character.Action and MultiAction:
                                $ Situation = "shift"
                                call Storm_FJ_After
                                call Storm_Handjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump Storm_FJ_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Storm_Sex_Reset
                                $ Situation = "shift"
                                jump Storm_FJ_After
                        "No, keep going.":
                                if ApprovalCheck(character, 1200) or ApprovalCheck(character, 500, "O"):
                                    $ character.Statup("Love", 200, -5)
                                    $ character.Statup("Obed", 50, 3)
                                    $ character.Statup("Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    $ character.FaceChange("angry", 1)
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_s "I do have better things I could be doing."
                                    $ character.Statup("Love", 50, -3, 1)
                                    $ character.Statup("Love", 80, -4, 1)
                                    $ character.Statup("Obed", 30, -1, 1)
                                    $ character.Statup("Obed", 50, -1, 1)
                                    $ character.RecentActions.append("angry")
                                    $ character.DailyActions.append("angry")
                                    jump Storm_FJ_After
        elif Cnt == 10 and character.SEXP <= 100 and not ApprovalCheck(character, 1200, "LO"):
                    $ character.Brows = "confused"
                    ch_s "Could we be done here, my feet are getting sore."
        #End Count check

        call Escalation(character) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(character,10) #"It is getting late, [Girl.Petname]. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(character,5)   #"We should take a break soon."

    #Round = 0 loop breaks
    $ character.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(character,"done") # ch_s "I need to take a moment to collect myself."

label Storm_FJ_After:
    $ character.FaceChange("sexy")

    $ character.Foot += 1
    $ character.Action -=1
    $ character.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ character.Addictionrate += 1
    $ character.Statup("Lust", 90, 5)

    call Partner_Like(character,1)

    if "Stormpedi" in Achievements:
            pass
    elif character.Foot >= 10:
            $ character.FaceChange("smile", 1)
            ch_s "I am glad that you convinced me to try this."
            ch_s "It feels so. . . intimate."
            $ Achievements.append("Stormpedi")
            $ character.SEXP += 5
    elif character.Foot == 1:
            $ character.SEXP += 10
            if character.Love >= 500:
                $ character.Mouth = "smile"
                ch_s "That certainly was an interesting experience. . ."
            elif Player.Focus <= 20:
                $ character.Mouth = "sad"
                ch_s "Did you enjoy that?"
    elif character.Foot == 5:
                ch_s "I'm enjoying this experience."

    $ temp_modifier = 0
    if Situation == "shift":
        ch_s "Ok then, what were you thinking?"
    else:
        call Storm_Sex_Reset
    call Checkout
    return

## end character.Footjob //////////////////////////////////////////////////////////////////////
