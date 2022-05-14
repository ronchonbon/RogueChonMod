## Girl.Handjob //////////////////////////////////////////////////////////////////////
label Storm_Handjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(Girl)
    if Girl.Hand >= 7: # She loves it
        $ temp_modifier += 10
    elif Girl.Hand >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif Girl.Hand: #You've done it before
        $ temp_modifier += 3

    if Girl.Addict >= 75 and Girl.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 15
    if Girl.Addict >= 75:
        $ temp_modifier += 5

    if action_context == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in Girl.Traits:
        $ temp_modifier += (3*Taboo)
    if Girl in Player.Harem or "sex friend" in Girl.Petnames:
        $ temp_modifier += 10
    elif "ex" in Girl.Traits:
        $ temp_modifier -= 40
    if Girl.ForcedCount and not Girl.Forced:
        $ temp_modifier -= 5 * Girl.ForcedCount

    if Taboo and "tabno" in Girl.daily_history:
        $ temp_modifier -= 10

    if "no hand" in Girl.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no hand" in Girl.recent_history else 0

    $ Approval = ApprovalCheck(Girl, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if not Girl.Hand and "no hand" not in Girl.recent_history:
        $ Girl.change_face("sly", 2)
        ch_s "You would like me to jerk you off?"

    if not Girl.Hand and Approval:                                                 #First time dialog
        if Girl.Forced:
            $ Girl.change_face("sad",1)
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
        elif Girl.love >= (Girl.obedience + Girl.inhibition):
            $ Girl.change_face("sexy",1)
            $ Girl.Brows = "sad"
            $ Girl.Mouth = "smile"
            ch_s "I might enjoy that. . ."
        elif Girl.obedience >= Girl.inhibition:
            $ Girl.change_face("normal",1)
            ch_s "If that is what you want, [Girl.Petname]. . ."
        elif Girl.Addict >= 50:
            $ Girl.change_face("manic", 1)
            ch_s "Mmmmmmmm. . ."
        else: # Uninhibited
            $ Girl.change_face("lipbite",1,Eyes="side")
            ch_s "I suppose. . ."

    elif Approval:                                                                       #Second time+ dialog
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
            ch_s "Nothing more than that?"
        elif not Taboo and "tabno" in Girl.daily_history:
            ch_s "Here, hmm?. . ."
        elif "hand" in Girl.recent_history:
            $ Girl.change_face("sexy", 1)
            ch_s "I do not know if I have it in me. . ."
            jump Storm_HJ_Prep
        elif "hand" in Girl.daily_history:
            $ Girl.change_face("sexy", 1)
            $ line = renpy.random.choice(["Another?",
                "My arm will wear out.",
                "You did not get enough earlier?",
                "My hand is quite sore from earlier.",
                "My hand is rather sore from before."])
            ch_s "[line]"
        elif Girl.Hand < 3:
            $ Girl.change_face("sly", 1)
            ch_s "You enjoyed it last time?. . ."
        else:
            $ Girl.change_face("sexy", 1)
            $ Girl.ArmPose = 2
            $ line = renpy.random.choice(["You want more?",
                "So you would like another?",
                "More of this? [fist pumping hand gestures]",
                "Oh, did you want some attention?"])
            ch_s "[line]"
        $ line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 60, 1)
            ch_s "Fine, we can do this."
        elif "no hand" in Girl.daily_history:
            ch_s "Oh, very well. . ."
        else:
            $ Girl.change_face("sexy", 1)
            $ Girl.change_stat("love", 90, 1)
            $ Girl.change_stat("inhibition", 50, 3)
            $ line = renpy.random.choice(["Oh, I suppose we might.",
                "I would do this.",
                "Very well, give it here.",
                "I suppose that I could. . .",
                ". . .Fine.[She gestures for you to come over]",
                "Ok, ok."])
            ch_s "[line]"
            $ line = 0
        $ Girl.change_stat("obedience", 20, 1)
        $ Girl.change_stat("obedience", 60, 1)
        $ Girl.change_stat("inhibition", 70, 2)
        jump Storm_HJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ Girl.change_face("angry")
        if "no hand" in Girl.daily_history:
            ch_s "You will need to accept a \"no\", [Girl.Petname]."
        elif Taboo and "tabno" in Girl.daily_history:
            ch_s "I was very clear, this is too public."
        elif not Girl.Hand:
            $ Girl.change_face("bemused")
            ch_s "Are you certain, [Girl.Petname]? . ."
        else:
            $ Girl.change_face("bemused")
            ch_s "I would rather not right now though."
        menu:
            extend ""
            "Sorry, never mind." if "no hand" in Girl.daily_history:
                $ Girl.change_face("bemused")
                ch_s "I understand."
                return
            "Maybe later?" if "no hand" not in Girl.daily_history:
                $ Girl.change_face("sexy")
                ch_s ". . ."
                ch_s "Perhaps. . ."
                $ Girl.change_stat("love", 80, 2)
                $ Girl.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ Girl.recent_history.append("tabno")
                    $ Girl.daily_history.append("tabno")
                $ Girl.recent_history.append("no hand")
                $ Girl.daily_history.append("no hand")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ Girl.change_face("sexy")
                    $ Girl.change_stat("obedience", 90, 2)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("inhibition", 70, 3)
                    $ Girl.change_stat("inhibition", 40, 2)
                    $ line = renpy.random.choice(["Oh, I suppose we might.",
                        "I would do this.",
                        "Very well, give it here.",
                        "I suppose that I could. . .",
                        ". . .Fine.[She gestures for you to come over]",
                        "Ok, ok."])
                    ch_s "[line]"
                    $ line = 0
                    jump Storm_HJ_Prep

            "Come on, get to work.":                                               # Pressured into it
                call forced_action(Girl, "handjob")

    #She refused all offers.
    $ Girl.ArmPose = 1
    if "no hand" in Girl.daily_history:
        $ Girl.change_face("angry", 1)

        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
    elif Girl.Forced:
        $ Girl.change_face("angry", 1)
        ch_s "I am not comfortable with that."
        $ Girl.change_stat("lust", 200, 5)
        if Girl.love > 300:
                $ Girl.change_stat("love", 70, -2)
        $ Girl.change_stat("obedience", 50, -2)
        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ Girl.change_face("angry", 1)
        $ Girl.daily_history.append("tabno")
        ch_s "I could not possibly do that here."
        $ Girl.change_stat("lust", 200, 5)
        $ Girl.change_stat("obedience", 50, -3)
    elif Girl.Hand:
        $ Girl.change_face("sad")
        ch_s ". . . I would rather not."
    else:
        $ Girl.change_face("normal", 1)
        ch_s "No, I do not think so, [Girl.Petname]."
    $ Girl.recent_history.append("no hand")
    $ Girl.daily_history.append("no hand")
    $ temp_modifier = 0
    return


label Storm_HJ_Prep:
    if offhand_action == "hand":
        return

    if Taboo:
        $ Girl.inhibition += int(Taboo/10)
        $ Girl.lust += int(Taboo/5)

    $ Girl.change_face("sexy")
    if Girl.Forced:
        $ Girl.change_face("sad")
    elif not Girl.Hand:
        $ Girl.Brows = "confused"
        $ Girl.Eyes = "sexy"
        $ Girl.Mouth = "smile"

    call Seen_First_Peen(Girl,Partner,React=action_context)
    call Storm_HJ_Launch("L")

    if action_context == Girl:
            #Storm auto-starts
            $ action_context = 0
            if offhand_action == "jackin":
                "[Girl.name] brushes your hand aside and starts stroking your cock."
            else:
                "[Girl.name] draws her fingers across your cock, and begins to stroke it."
            menu:
                "What do you do?"
                "Nothing.":
                    $ Girl.change_stat("inhibition", 70, 3)
                    $ Girl.change_stat("inhibition", 30, 2)
                    "[Girl.name] continues her actions."
                "Praise her.":
                    $ Girl.change_face("sexy", 1)
                    $ Girl.change_stat("inhibition", 70, 3)
                    ch_p "Oooh, that's good, [Girl.Pet]."
                    $ Girl.nameCheck() #checks reaction to petname
                    "[Girl.name] continues her actions."
                    $ Girl.change_stat("love", 80, 1)
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ Girl.change_face("surprised")
                    $ Girl.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that for now, [Girl.Pet]."
                    $ Girl.nameCheck() #checks reaction to petname
                    "[Girl.name] puts it down."
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Girl.change_stat("obedience", 30, 2)
                    $ Player.recent_history.append("nope")
                    $ Girl.AddWord(1,"refused","refused")
                    return

    if not Girl.Hand:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -20)
            $ Girl.change_stat("obedience", 70, 25)
            $ Girl.change_stat("inhibition", 80, 30)
        else:
            $ Girl.change_stat("love", 90, 5)
            $ Girl.change_stat("obedience", 70, 20)
            $ Girl.change_stat("inhibition", 80, 20)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ line = 0
    $ counter = 0
    if Taboo:
        $ Girl.DrainWord("tabno")
    $ Girl.DrainWord("no hand")
    $ Girl.recent_history.append("hand")
    $ Girl.daily_history.append("hand")

label Storm_HJ_Cycle:
    while Round > 0:
        call Shift_Focus(Girl)
        call Storm_HJ_Launch
        $ Girl.lustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if action_speed:
                                    pass

                        "Start moving? . ." if not action_speed:
                                    $ action_speed = 1

                        "action_speed up. . ." if action_speed < 2:
                                    $ action_speed = 2
                                    "You ask her to up the pace a bit."
                        "action_speed up. . . (locked)" if action_speed >= 2:
                                    pass

                        "Slow Down. . ." if action_speed:
                                    $ action_speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not action_speed:
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
                                    "I also want to fondle her breasts." if offhand_action != "fondle breasts":
                                            if Girl.Action and MultiAction:
                                                $ offhand_action = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ Girl.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Shift primary action":
                                            if Girl.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                $ action_context = "shift"
                                                                call Storm_HJ_After
                                                                call Storm_Blowjob

                                                        "How about a titjob?":
                                                                $ action_context = "shift"
                                                                call Storm_HJ_After
                                                                call Storm_Titjob
                                                        "Never Mind":
                                                                jump Storm_HJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [Girl.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(Girl)
                                            "Asks [Girl.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                call Three_Change(Girl)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(Girl)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Storm_HJ_Cycle
                                            "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Storm_HJ_Cycle
                                            "Never mind":
                                                        jump Storm_HJ_Cycle
                                    "Undress [Girl.name]":
                                            call Girl_Undress(Girl)
                                    "Clean up [Girl.name] (locked)" if not Girl.Spunk:
                                            pass
                                    "Clean up [Girl.name]" if Girl.Spunk:
                                            call Girl_Cleanup(Girl,"ask")
                                    "Never mind":
                                            jump Storm_HJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Storm_HJ_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Storm_HJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Storm_HJ_Reset
                                    $ line = 0
                                    jump Storm_HJ_After
        #End menu (if line)

        call Shift_Focus(Girl)
        call Sex_Dialog(Girl,Partner)

        #If either of you could cum

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or Girl.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(Girl)
                            if "angry" in Girl.recent_history:
                                call Storm_HJ_Reset
                                return
                            $ Girl.change_stat("lust", 200, 5)
                            if 100 > Girl.lust >= 70 and Girl.OCount < 2 and Girl.SEXP >= 20:
                                $ Girl.recent_history.append("unsatisfied")
                                $ Girl.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Storm_HJ_After
                            $ line = "came"

                    if Girl.lust >= 100:
                            #If [Girl.name] can cum
                            call Girl_Cumming(Girl)
                            if action_context == "shift" or "angry" in Girl.recent_history:
                                jump Storm_HJ_After

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in Girl.recent_history:#And [Girl.name] is unsatisfied,
                                    "[Girl.name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Storm_HJ_After
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if counter == 20:
                    $ Girl.Brows = "angry"
                    ch_s "Hmm, I am developing a hand cramp here."
                    menu:
                        ch_s "Mind if we take a break?"
                        "How about a BJ?" if Girl.Action and MultiAction:
                                $ action_context = "shift"
                                call Storm_HJ_After
                                call Storm_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ counter += 1
                                "[line]"
                                jump Storm_HJ_Cycle
                        "Let's try something else." if MultiAction:
                                $ line = 0
                                call Storm_HJ_Reset
                                $ action_context = "shift"
                                jump Storm_HJ_After
                        "No, get back down there.":
                                if ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "O"):
                                    $ Girl.change_stat("love", 200, -5)
                                    $ Girl.change_stat("obedience", 50, 3)
                                    $ Girl.change_stat("obedience", 80, 2)
                                    "She scowls but gets back to work."
                                else:
                                    $ Girl.change_face("angry", 1)
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_s "Perhaps some time alone would help you better evaluate your choices."
                                    $ Girl.change_stat("love", 50, -3, 1)
                                    $ Girl.change_stat("love", 80, -4, 1)
                                    $ Girl.change_stat("obedience", 30, -1, 1)
                                    $ Girl.change_stat("obedience", 50, -1, 1)
                                    $ Girl.recent_history.append("angry")
                                    $ Girl.daily_history.append("angry")
                                    jump Storm_HJ_After
        elif counter == 10 and Girl.SEXP <= 100 and not ApprovalCheck(Girl, 1200, "LO"):
                    $ Girl.Brows = "confused"
                    ch_s "Are you certain you didn't have anything else in mind?"
        #End Count check

        call Escalation(Girl) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(Girl,10) #"It is getting late, [Girl.Petname]. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(Girl,5)   #"We should take a break soon."

    #Round = 0 loop breaks
    $ Girl.change_face("bemused", 0)
    $ line = 0
    call Sex_Basic_Dialog(Girl,"done") # ch_s "I need to take a moment to collect myself."

label Storm_HJ_After:
    $ Girl.change_face("sexy")

    $ Girl.Hand += 1
    $ Girl.Action -=1
    $ Girl.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ Girl.Addictionrate += 1
    $ Girl.change_stat("lust", 90, 5)

    call Partner_Like(Girl,1)

    if "Storm Handi-Queen" in Achievements:
            pass
    elif Girl.Hand >= 10:
            $ Girl.change_face("smile", 1)
            ch_s "I seem to have become the \"queen\" of good handjobs."
            $ Achievements.append("Storm Handi-Queen")
            $Girl.SEXP += 5
    elif Girl.Hand == 1:
            $Girl.SEXP += 10
            if not Girl.Forced:
                $ Girl.Mouth = "smile"
                ch_s "That was more enjoyable than I had expected. . ."
            elif Player.Focus <= 20:
                $ Girl.Mouth = "sad"
                ch_s "Did that satisfy you?"
    elif Girl.Hand == 5:
                ch_s "I have gotten used to these. . ."

    $ temp_modifier = 0
    if action_context == "shift":
        ch_s "Very well, what did you want to do?"
    else:
        call Storm_HJ_Reset
    call Checkout
    return

## end Girl.Handjob //////////////////////////////////////////////////////////////////////




## Girl.Titjob //////////////////////////////////////////////////////////////////////
label Storm_Titjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(Girl)
    if Girl.Tit >= 7: # She loves it
        $ temp_modifier += 10
    elif Girl.Tit >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif Girl.Tit: #You've done it before
        $ temp_modifier += 5

    if Girl.Addict >= 75 and Girl.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 15
    elif Girl.Addict >= 75:
        $ temp_modifier += 5

    if Girl.SeenChest and ApprovalCheck(Girl, 500): # You've seen her tits.
        $ temp_modifier += 10
    if not Girl.Chest and not Girl.Over: #She's already topless
        $ temp_modifier += 10
    if Girl.lust > 75: #She's really horny
        $ temp_modifier += 10
    if action_context == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in Girl.Traits:
        $ temp_modifier += (5*Taboo)
    if Girl in Player.Harem or "sex friend" in Girl.Petnames:
        $ temp_modifier += 10
    elif "ex" in Girl.Traits:
        $ temp_modifier -= 30
    if Girl.ForcedCount and not Girl.Forced:
        $ temp_modifier -= 5 * Girl.ForcedCount

    if Taboo and "tabno" in Girl.daily_history:
        $ temp_modifier -= 10

    if "no titjob" in Girl.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no titjob" in Girl.recent_history else 0

    $ Approval = ApprovalCheck(Girl, 1200, TabM = 5) # 120, 135, 150, Taboo -200(320)

    if not Girl.Tit and "no titjob" not in Girl.recent_history:
        $ Girl.change_face("surprised", 1)
        $ Girl.Mouth = "kiss"
        ch_s "My breasts are really appealing to you, [Girl.Petname]?"

    if not Girl.Tit and Approval:
        #First time dialog
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
        elif Girl.love >= (Girl.obedience + Girl.inhibition):
            $ Girl.change_face("sexy")
            $ Girl.Brows = "sad"
            $ Girl.Mouth = "smile"
            ch_s "I suppose you've earned something special. . ."
        elif Girl.obedience >= Girl.inhibition:
            $ Girl.change_face("normal")
            ch_s "If that is what you want. . ."
        elif Girl.Addict >= 50:
            $ Girl.change_face("manic", 1)
            ch_s "Hmmmm. . . ."
        else: # Uninhibited
            $ Girl.change_face("sad")
            $ Girl.Mouth = "smile"
            ch_s "Hmm, I was expecting you to ask. . ."

    elif Approval:
        #Second time+ dialog
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
            ch_s "You enjoy making use of these?"
        elif not Taboo and "tabno" in Girl.daily_history:
            ch_s "I suppose this is secluded enough. . ."
        elif "titjob" in Girl.recent_history:
            $ Girl.change_face("sexy", 1)
            ch_s "You cannot get enough?"
            jump Storm_TJ_Prep
        elif "titjob" in Girl.daily_history:
            $ Girl.change_face("sexy", 1)
            $ line = renpy.random.choice(["Back again so soon?",
                "You will wear them out like this.",
                "You did not get enough earlier?",
                "I am still a bit sore from earlier."])
            ch_s "[line]"
        elif Girl.Tit < 3:
            $ Girl.change_face("sly", 1)
            ch_s "Hmm, another titjob?"
        else:
            $ Girl.change_face("sexy", 1)
            $ Girl.ArmPose = 2
            $ line = renpy.random.choice(["You wish to use these? [jiggles her tits]",
                "So you would like another titjob?",
                ". . . [bounces tits]?",
                "You would like to give it a hug?"])
            ch_s "[line]"
        $ line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 60, 1)
            ch_s "I suppose this would not be too unpleasant. . ."
        elif "no titjob" in Girl.daily_history:
            ch_s "Very well then. . ."
        else:
            $ Girl.change_face("sexy", 1)
            $ Girl.change_stat("love", 90, 1)
            $ Girl.change_stat("inhibition", 50, 3)
            $ line = renpy.random.choice(["Fine, come over here.",
                "Oh, very well.",
                "Mmmmm.",
                "Fine, show me.",
                "Fine. . . [She drools a bit into her cleavage].",
                "Oh, all right."])
            ch_s "[line]"
            $ line = 0
        $ Girl.change_stat("obedience", 20, 1)
        $ Girl.change_stat("obedience", 70, 1)
        $ Girl.change_stat("inhibition", 80, 2)
        jump Storm_TJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ Girl.change_face("angry")
        if "no titjob" in Girl.daily_history:
            ch_s "You will need to accept a \"no\", [Girl.Petname]."
        elif Taboo and "tabno" in Girl.daily_history and "no titjob" in Girl.daily_history:
            ch_s "This is not an appropriate location for that. !"
        elif "no titjob" in Girl.daily_history:
            ch_s "I already refused, [Girl.Petname]."
        elif Taboo and "tabno" in Girl.daily_history:
            ch_s "This is not an appropriate place for that."
        else:
            $ Girl.change_face("bemused")
            ch_s "Perhaps later, [Girl.Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no titjob" in Girl.daily_history:
                $ Girl.change_face("bemused")
                ch_s "That is fine, [Girl.Petname]."
                return
            "Maybe later?" if "no titjob" not in Girl.daily_history:
                $ Girl.change_face("sexy")
                ch_s "Perhaps."
                $ Girl.change_stat("love", 80, 2)
                $ Girl.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ Girl.recent_history.append("tabno")
                    $ Girl.daily_history.append("tabno")
                $ Girl.recent_history.append("no titjob")
                $ Girl.daily_history.append("no titjob")
                return
            "I think this could be fun for both of us. . .":
                if Approval:
                    $ Girl.change_face("sexy")
                    $ Girl.change_stat("obedience", 80, 2)
                    $ Girl.change_stat("obedience", 40, 2)
                    $ Girl.change_stat("inhibition", 70, 3)
                    $ Girl.change_stat("inhibition", 40, 2)
                    $ line = renpy.random.choice(["Fine, come over here.",
                        "Oh, very well.",
                        "Mmmmm.",
                        "Fine, show me.",
                        "Fine. . . [She drools a bit into her cleavage].",
                        "Oh, all right."])
                    ch_s "[line]"
                    $ line = 0
                    jump Storm_TJ_Prep
                else:
                    $ Approval = ApprovalCheck(Girl, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)             Handy instead?
                    if Approval >= 2:
                        $ Girl.change_stat("inhibition", 80, 1)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.change_face("confused", 1)
                        if Girl.Blow:
                            ch_s "You seemed to enjoy blowjobs, would that work instead?"
                        else:
                            ch_s "Would you perhaps prefer a blowjob?"
                        menu:
                            extend ""
                            "Ok, get down there.":
                                $ Girl.change_stat("love", 80, 2)
                                $ Girl.change_stat("inhibition", 60, 1)
                                $ Girl.change_stat("obedience", 50, 1)
                                jump Storm_BJ_Prep
                            "Nah, it's all about dem titties.":
                                $ line = "no BJ"
                    if Approval:
                        $ Girl.change_stat("inhibition", 80, 1)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.change_face("confused", 1)
                        ch_s "Perhaps a handjob?"
                        menu:
                            ch_s "Perhaps a handjob?"
                            "Sure, that's fine.":
                                $ Girl.change_stat("love", 80, 2)
                                $ Girl.change_stat("inhibition", 60, 1)
                                $ Girl.change_stat("obedience", 50, 1)
                                jump Storm_HJ_Prep
                            "Seriously, titties." if line == "no BJ":
                                $ line = 0
                            "Nah, it's all about dem titties." if line != "no BJ":
                                pass
                    $ Girl.change_stat("love", 200, -2)
                    ch_s "Well. That is unfortunate. . ."
                    $ Girl.change_stat("obedience", 70, 2)


            "Come on, let me fuck those titties, [Girl.Pet]":                                               # Pressured into it
                $ Girl.nameCheck() #checks reaction to petname
                $ Approval = ApprovalCheck(Girl, 700, "OI", TabM = 4) # 70, 85, 100, -160(230)
                if Approval > 1 or (Approval and Girl.Forced):
                    $ Girl.change_face("sad")
                    $ Girl.change_stat("love", 70, -5, 1)
                    $ Girl.change_stat("love", 200, -2)

                    $ Girl.change_stat("obedience", 50, 4)
                    $ Girl.change_stat("inhibition", 80, 1)
                    $ Girl.change_stat("inhibition", 60, 3)
                    $ Girl.Forced = 1
                    jump Storm_TJ_Prep
                else:
                    $ Girl.change_stat("love", 200, -15)
                    $ Girl.recent_history.append("angry")
                    $ Girl.daily_history.append("angry")

    #She refused all offers.
    if "no titjob" in Girl.daily_history:
        $ Girl.change_face("angry", 1)

        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
    elif Girl.Forced:
        $ Girl.change_face("angry", 1)
        ch_s "I do not wish to do this."
        $ Girl.change_stat("lust", 200, 5)
        if Girl.love > 300:
                $ Girl.change_stat("love", 70, -2)
        $ Girl.change_stat("obedience", 50, -2)
        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ Girl.change_face("angry", 1)
        $ Girl.daily_history.append("tabno")
        ch_s "I do not wish to make a spectacle."
        $ Girl.change_stat("lust", 200, 5)
        $ Girl.change_stat("obedience", 50, -3)
    elif Girl.Tit:
        $ Girl.change_face("sad")
        ch_s "Our time together was a memory."
    else:
        $ Girl.change_face("normal", 1)
        ch_s "I would rather not, [Girl.Petname]."
    $ Girl.recent_history.append("no titjob")
    $ Girl.daily_history.append("no titjob")
    $ temp_modifier = 0
    return

label Storm_TJ_Prep:
    if Taboo:
        $ Girl.inhibition += int(Taboo/10)
        $ Girl.lust += int(Taboo/5)


    $ Girl.change_face("sexy")
    if Girl.Forced:
        $ Girl.change_face("sad")
    elif not Girl.Tit:
        $ Girl.Brows = "confused"
        $ Girl.Eyes = "sexy"
        $ Girl.Mouth = "smile"

    call Seen_First_Peen(Girl,Partner,React=action_context)
    call Storm_TJ_Launch("L")

    if action_context == Girl:
            #Storm auto-starts
            $ action_context = 0
            call Storm_TJ_Launch("L")
            "[Girl.name] slides down and wraps her tits around your dick."
            menu:
                "What do you do?"
                "Nothing.":
                    $ Girl.change_stat("inhibition", 80, 3)
                    $ Girl.change_stat("inhibition", 40, 2)
                    "[Girl.name] starts to slide them up and down."
                "Praise her.":
                    $ Girl.change_face("sexy", 1)
                    $ Girl.change_stat("inhibition", 80, 3)
                    ch_p "Oh, that sounds like a good idea, [Girl.Pet]."
                    $ Girl.nameCheck() #checks reaction to petname
                    "[Girl.name] continues her actions."
                    $ Girl.change_stat("love", 85, 1)
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ Girl.change_face("confused")
                    $ Girl.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that for now, [Girl.Pet]."
                    $ Girl.nameCheck() #checks reaction to petname
                    "[Girl.name] lets it drop out from between her breasts."
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Player.recent_history.append("nope")
                    $ Girl.AddWord(1,"refused","refused")
                    return
    if not Girl.Tit:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -25)
            $ Girl.change_stat("obedience", 70, 30)
            $ Girl.change_stat("inhibition", 80, 35)
        else:
            $ Girl.change_stat("love", 90, 5)
            $ Girl.change_stat("obedience", 70, 25)
            $ Girl.change_stat("inhibition", 80, 30)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ line = 0
    $ counter = 0
    if Taboo:
        $ Girl.DrainWord("tabno")
    $ Girl.DrainWord("no titjob")
    $ Girl.recent_history.append("titjob")
    $ Girl.daily_history.append("titjob")


label Storm_TJ_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(Girl)
        call Storm_TJ_Launch
        $ Girl.lustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if action_speed:
                                    pass

                        "Start moving? . ." if action_speed == 0:
                                    $ action_speed = 1

                        "action_speed up. . ." if  action_speed == 1:
                                    $ action_speed = 2
                                    "You ask her to up the pace a bit."
                        "action_speed up. . . (locked)" if action_speed >= 2:
                                    pass

                        "Stop moving" if action_speed == 1 or action_speed == 3:
                                    $ action_speed = 0
                        "Slow Down. . ." if action_speed == 2:
                                    $ action_speed = 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not action_speed:
                                    pass

                        "Lick it" if action_speed != 3:
                                    $ action_speed = 3
                        "Lick it (locked)" if action_speed == 3:
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
                                    "I also want to fondle her breasts." if offhand_action != "fondle breasts":
                                            if Girl.Action and MultiAction:
                                                $ offhand_action = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ Girl.Action -= 1
                                            else:
                                                ch_s "I would prefer to finish this."

                                    "Shift primary action":
                                            if Girl.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                $ action_context = "shift"
                                                                call Storm_TJ_After
                                                                call Storm_Blowjob
                                                        "How about a handy?":
                                                                $ action_context = "shift"
                                                                call Storm_BJ_After
                                                                call Storm_Handjob
                                                        "Never Mind":
                                                                jump Storm_TJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [Girl.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(Girl)
                                            "Asks [Girl.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(Girl)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(Girl)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Storm_TJ_Cycle
                                            "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Storm_TJ_Cycle
                                            "Never mind":
                                                        jump Storm_TJ_Cycle
                                    "Undress [Girl.name]":
                                            call Girl_Undress(Girl)
                                    "Clean up [Girl.name] (locked)" if not Girl.Spunk:
                                            pass
                                    "Clean up [Girl.name]" if Girl.Spunk:
                                            call Girl_Cleanup(Girl,"ask")
                                    "Never mind":
                                            jump Storm_TJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Storm_TJ_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Storm_TJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Storm_TJ_Reset
                                    $ line = 0
                                    jump Storm_TJ_After
        #End menu (if line)

        call Shift_Focus(Girl)
        call Sex_Dialog(Girl,Partner)

        #If either of you could cum

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or Girl.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(Girl)
                            if "angry" in Girl.recent_history:
                                call Storm_TJ_Reset
                                return
                            $ Girl.change_stat("lust", 200, 5)
                            if 100 > Girl.lust >= 70 and Girl.OCount < 2 and Girl.SEXP >= 20:
                                $ Girl.recent_history.append("unsatisfied")
                                $ Girl.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Storm_TJ_After
                            $ line = "came"

                    if Girl.lust >= 100:
                            #If [Girl.name] can cum
                            call Girl_Cumming(Girl)
                            if action_context == "shift" or "angry" in Girl.recent_history:
                                jump Storm_TJ_After

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in Girl.recent_history:#And [Girl.name] is unsatisfied,
                                "[Girl.name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Storm_TJ_After
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Girl.SEXP >= 100 or ApprovalCheck(Girl, 1200, "LO"):
            pass
        elif counter == (5 + Girl.Tit):
                    $ Girl.Brows = "confused"
                    ch_s "Are you getting close? This is making me a bit sore. . ."
        elif counter == (10 + Girl.Tit):
                    $ Girl.Brows = "angry"
                    menu:
                        ch_s "This is becoming uncomfortable, is there some way I could finish you off?"
                        "How about a BJ?" if Girl.Action and MultiAction:
                                $ action_context = "shift"
                                call Storm_TJ_After
                                call Storm_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                jump Storm_TJ_Cycle
                        "Let's try something else." if MultiAction:
                                $ line = 0
                                call Storm_TJ_Reset
                                $ action_context = "shift"
                                jump Storm_TJ_After
                        "No, get back down there.":
                                if ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "O"):
                                    $ Girl.change_stat("love", 200, -5)
                                    $ Girl.change_stat("obedience", 50, 3)
                                    $ Girl.change_stat("obedience", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    $ Girl.change_face("angry", 1)
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_s "Then I suppose you can handle this yourself."
                                    $ Girl.change_stat("love", 50, -3, 1)
                                    $ Girl.change_stat("love", 80, -4, 1)
                                    $ Girl.change_stat("obedience", 30, -1, 1)
                                    $ Girl.change_stat("obedience", 50, -1, 1)
                                    $ Girl.recent_history.append("angry")
                                    $ Girl.daily_history.append("angry")
                                    jump Storm_TJ_After
        #End Count check

        call Escalation(Girl) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(Girl,10) #"It is getting late, [Girl.Petname]. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(Girl,5)   #"We should take a break soon."

    #Round = 0 loop breaks
    $ Girl.change_face("bemused", 0)
    $ line = 0
    call Sex_Basic_Dialog(Girl,"done") # ch_s "I need to take a moment to collect myself."

label Storm_TJ_After:
    $ Girl.change_face("sexy")

    $ Girl.Tit += 1
    $ Girl.Action -=1
    $ Girl.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ Girl.Addictionrate += 1

    if Partner == "Kitty":
        call Partner_Like(Girl,4,2)
    else:
        call Partner_Like(Girl,3)

    if Girl.Tit > 5:
            pass
    elif Girl.Tit == 1:
        $Girl.SEXP += 12
        if Girl.love >= 500:
            $ Girl.Mouth = "smile"
            ch_s "Mmm, I did quite enjoy that!"
        elif Player.Focus <= 20:
            $ Girl.Mouth = "sad"
            ch_s "I hope that met your standards."
    elif Girl.Tit == 5:
            ch_s "You do seem to enjoy this."


    $ temp_modifier = 0
    if action_context == "shift":
            ch_s "Mmm, so what else did you have in mind?"
    else:
            call Storm_TJ_Reset
    call Checkout
    return

## end Girl.Titjob //////////////////////////////////////////////////////////////////////


# Girl.Blowjob //////////////////////////////////////////////////////////////////////

label Storm_Blowjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(Girl)
    if Girl.Blow >= 7: # She loves it
        $ temp_modifier += 15
    elif Girl.Blow >= 3: #You've done it before several times
        $ temp_modifier += 10
    elif Girl.Blow: #You've done it before
        $ temp_modifier += 7

    if Girl.Addict >= 75 and Girl.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 25
    elif Girl.Addict >= 75: #She's really strung out
        $ temp_modifier += 15

    if action_context == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in Girl.Traits:
        $ temp_modifier += (4*Taboo)
    if Girl in Player.Harem or "sex friend" in Girl.Petnames:
        $ temp_modifier += 10
    elif "ex" in Girl.Traits:
        $ temp_modifier -= 40
    if Girl.ForcedCount and not Girl.Forced:
        $ temp_modifier -= 5 * Girl.ForcedCount

    if Taboo and "tabno" in Girl.daily_history:
        $ temp_modifier -= 10

    if "no blow" in Girl.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no blow" in Girl.recent_history else 0

    $ Approval = ApprovalCheck(Girl, 1300, TabM = 4) # 130, 145, 160, Taboo -160(290)

    if not Girl.Blow and "no blow" not in Girl.recent_history:
        $ Girl.change_face("sly")
        ch_s "You would like me to suck on your penis?"

    if not Girl.Blow and Approval:                                                 #First time dialog
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
        elif Girl.love >= (Girl.obedience + Girl.inhibition):
            $ Girl.change_face("sexy")
            $ Girl.Brows = "sad"
            $ Girl.Mouth = "smile"
            ch_s "I have been curious. . ."
        elif Girl.obedience >= Girl.inhibition:
            $ Girl.change_face("normal")
            ch_s "If that is what you want. . ."
        elif Girl.Addict >= 50:
            $ Girl.change_face("manic", 1)
            ch_s "I might enjoy that. . ."
        else: # Uninhibited
            $ Girl.change_face("sad")
            $ Girl.Mouth = "smile"
            ch_s "I suppose. . ."
    elif Approval:                                                                       #Second time+ dialog
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
            ch_s "Tsk, again?"
        elif not Taboo and "tabno" in Girl.daily_history:
            ch_s "Fine, I suppose this is secluded enough. . ."
        elif "blow" in Girl.recent_history:
            $ Girl.change_face("sexy", 1)
            ch_s "Mmm, again?"
            jump Storm_BJ_Prep
        elif "blow" in Girl.daily_history:
            $ Girl.change_face("sexy", 1)
            $ line = renpy.random.choice(["Back so soon?",
                "I must prepare myself.",
                "You did not get enough earlier?",
                "My jaw is still rather sore.",
                "My jaw is still recovering."])
            ch_s "[line]"
        elif Girl.Blow < 3:
            $ Girl.change_face("sexy", 1)
            $ Girl.Brows = "confused"
            $ Girl.Mouth = "kiss"
            ch_s "Another blowjob?"
        else:
            $ Girl.change_face("sexy", 1)
            $ Girl.ArmPose = 2
            $ line = renpy.random.choice([". . . [mimes blowing]?",
                "So you would like another blowjob?",
                "You wish for me to suck you off?",
                "Are you asking if I am hungry?"])
            ch_s "[line]"
        $ line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 60, 1)
            ch_s "Fine."
        elif "no blow" in Girl.daily_history:
            ch_s "Fine, I suppose you have earned it. . ."
        else:
            $ Girl.change_face("sexy", 1)
            $ Girl.change_stat("love", 90, 1)
            $ Girl.change_stat("inhibition", 50, 3)
            $ line = renpy.random.choice([". . . ok.",
                "Well. . . ok.",
                "Mmmm.",
                "Sure, let me have it.",
                "Mmmm. . . [She licks her lips].",
                "Ok, fine."])
            ch_s "[line]"
            $ line = 0
        $ Girl.change_stat("obedience", 20, 1)
        $ Girl.change_stat("obedience", 70, 1)
        $ Girl.change_stat("inhibition", 80, 2)
        jump Storm_BJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ Girl.change_face("angry")
        if "no blow" in Girl.daily_history:
            ch_s "You will need to accept a \"no\", [Girl.Petname]."
        elif Taboo and "tabno" in Girl.daily_history and "no blow" in Girl.daily_history:
            ch_s "I told you, this is too public!"
        elif "no blow" in Girl.daily_history:
            ch_s "I told you \"no,\" [Girl.Petname]."
        elif Taboo and "tabno" in Girl.daily_history:
            ch_s "I told you this is too public!"
        elif not Girl.Blow:
            $ Girl.change_face("bemused")
            ch_s "I am not sure I would enjoy this, [Girl.Petname]. . ."
        else:
            $ Girl.change_face("bemused")
            ch_s "Perhaps later, [Girl.Petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no blow" in Girl.daily_history:
                $ Girl.change_face("bemused")
                ch_s "It is fine, [Girl.Petname]."
                return
            "Maybe later?" if "no blow" not in Girl.daily_history:
                $ Girl.change_face("sexy")
                ch_s "I would not rule it out, [Girl.Petname]."
                $ Girl.change_stat("love", 80, 2)
                $ Girl.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ Girl.recent_history.append("tabno")
                    $ Girl.daily_history.append("tabno")
                $ Girl.recent_history.append("no blow")
                $ Girl.daily_history.append("no blow")
                return
            "Come on, please?":
                if Approval:
                    $ Girl.change_face("sexy")
                    $ Girl.change_stat("obedience", 90, 2)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("inhibition", 70, 3)
                    $ Girl.change_stat("inhibition", 40, 2)
                    $ line = renpy.random.choice(["Well, I suppose.",
                        "Well. . . ok.",
                        "I could perhaps give it a try.",
                        "I suppose that I could. . .",
                        "Fine. . . [She licks her lips].",
                        "Hmph, ok, fine."])
                    ch_s "[line]"
                    $ line = 0
                    jump Storm_BJ_Prep
                else:
                    if ApprovalCheck(Girl, 1100, TabM = 3): # 110, 125, 140, Taboo -120(230)             Handy instead?
                        $ Girl.change_stat("inhibition", 80, 1)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.change_face("confused", 1)
                        $ Girl.ArmPose = 2
                        if Girl.Hand:
                            ch_s "I could just stroke you off, perhaps?"
                        else:
                            ch_s "Would my hand be an adequate substitute?"
                        menu:
                            extend ""
                            "Sure, that's fine.":
                                $ Girl.change_stat("love", 80, 2)
                                $ Girl.change_stat("inhibition", 60, 1)
                                $ Girl.change_stat("obedience", 50, 1)
                                jump Storm_HJ_Prep
                            "Nah, if it's not your mouth, forget it.":
                                $ Girl.change_stat("love", 200, -2)
                                $ Girl.ArmPose = 1
                                ch_s "That is unfortunate."
                                $ Girl.change_stat("obedience", 70, 2)


            "Suck it, [Girl.Pet]":                                               # Pressured into it
                $ Girl.nameCheck() #checks reaction to petname
                $ Approval = ApprovalCheck(Girl, 750, "OI", TabM = 3) # 75, 90, 105, -120(195)
                if Approval > 1 or (Approval and Girl.Forced):
                    $ Girl.change_face("sad")
                    $ Girl.change_stat("love", 70, -5, 1)
                    $ Girl.change_stat("love", 200, -2)

                    $ Girl.change_stat("obedience", 50, 4)
                    $ Girl.change_stat("inhibition", 80, 1)
                    $ Girl.change_stat("inhibition", 60, 3)
                    $ Girl.Forced = 1
                    jump Storm_BJ_Prep
                else:
                    $ Girl.change_stat("love", 200, -15)
                    $ Girl.recent_history.append("angry")
                    $ Girl.daily_history.append("angry")

    #She refused all offers.
    if "no blow" in Girl.daily_history:
        $ Girl.change_face("angry", 1)

        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
    elif Girl.Forced:
        $ Girl.change_face("angry", 1)
        ch_s "You go too far!"
        $ Girl.change_stat("lust", 200, 5)
        if Girl.love > 300:
                $ Girl.change_stat("love", 70, -2)
        $ Girl.change_stat("obedience", 50, -2)
        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
        $ Girl.recent_history.append("no blow")
        $ Girl.daily_history.append("no blow")
        return
    elif Taboo:                             # she refuses and this is too public a place for her
        $ Girl.change_face("angry", 1)
        $ Girl.daily_history.append("tabno")
        ch_s "This is much too exposed."
        $ Girl.change_stat("lust", 200, 5)
        $ Girl.change_stat("obedience", 50, -3)
        return
    elif Girl.Blow:
        $ Girl.change_face("sad")
        ch_s "I am just not in the mood, [Girl.Petname]."
    else:
        $ Girl.change_face("normal", 1)
        ch_s "I do not think that I will."
    $ Girl.recent_history.append("no blow")
    $ Girl.daily_history.append("no blow")
    $ temp_modifier = 0
    return


label Storm_BJ_Prep:
    if renpy.showing("Storm_HJ_Animation"):
        hide Storm_HJ_Animation with easeoutbottom
    if Taboo:
        $ Girl.inhibition += int(Taboo/10)
        $ Girl.lust += int(Taboo/5)

    $ Girl.change_face("sexy")
    if Girl.Forced:
        $ Girl.change_face("sad")

    call Seen_First_Peen(Girl,Partner,React=action_context)
    call Storm_BJ_Launch("L")

    if action_context == Girl:
            #Storm auto-starts
            $ action_context = 0
            "[Girl.name] slides down and places your cock against her lips."
            menu:
                "What do you do?"
                "Nothing.":
                    $ Girl.change_stat("inhibition", 80, 3)
                    $ Girl.change_stat("inhibition", 40, 2)
                    "[Girl.name] continues licking at it."
                "Praise her.":
                    $ Girl.change_face("sexy", 1)
                    $ Girl.change_stat("inhibition", 80, 3)
                    ch_p "Hmmm, keep doing that, [Girl.Pet]."
                    $ Girl.nameCheck() #checks reaction to petname
                    "[Girl.name] continues her actions."
                    $ Girl.change_stat("love", 85, 1)
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ Girl.change_face("surprised")
                    $ Girl.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that for now, [Girl.Pet]."
                    $ Girl.nameCheck() #checks reaction to petname
                    "[Girl.name] puts it down."
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Player.recent_history.append("nope")
                    $ Girl.AddWord(1,"refused","refused")
                    return
    if not Girl.Blow:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -70)
            $ Girl.change_stat("obedience", 70, 45)
            $ Girl.change_stat("inhibition", 80, 60)
        else:
            $ Girl.change_stat("love", 90, 5)
            $ Girl.change_stat("obedience", 70, 35)
            $ Girl.change_stat("inhibition", 80, 40)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ line = 0
    $ counter = 0
    if Taboo:
        $ Girl.DrainWord("tabno")
    $ Girl.DrainWord("no blow")
    $ Girl.recent_history.append("blow")
    $ Girl.daily_history.append("blow")

label Storm_BJ_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(Girl)
        call Storm_BJ_Launch
        $ Girl.lustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if action_speed:
                                    pass

                        "Lick it. . ." if action_speed != 1:
                                $ action_speed = 1
                        "Lick it. . . (locked)" if action_speed == 1:
                                pass

                        "Just the head. . ." if action_speed != 2:
                            $ action_speed = 2
                        "Just the head. . . (locked)" if action_speed == 2:
                                pass

                        "Suck on it." if action_speed != 3:
                                $ action_speed = 3
                                if offhand_action == "jackin":
                                    "She dips her head a bit lower, and you move your hand out of the way."

                        "Suck on it. (locked)" if action_speed == 3:
                                pass

                        "Take it deeper." if action_speed != 4:
                                if "pushed" not in Girl.recent_history and Girl.Blow < 5:
                                    $ Girl.change_stat("love", 80, -(20-(2*Girl.Blow)))
                                    $ Girl.change_stat("obedience", 80, (30-(3*Girl.Blow)))
                                    $ Girl.recent_history.append("pushed")
                                if offhand_action == "jackin" and action_speed != 3:
                                    "She takes it to the root, and you move your hand out of the way."
                                $ action_speed = 4
                        "Take it deeper. (locked)" if action_speed == 4:
                                pass

                        "Set your own pace. . .":
                                "[Girl.name] hums contentedly."
                                if "setpace" not in Girl.recent_history:
                                    $ Girl.change_stat("love", 80, 2)
                                $ D20 = renpy.random.randint(1, 20)
                                if Girl.Blow < 5:
                                    $ D20 -= 10
                                elif Girl.Blow < 10:
                                    $ D20 -= 5

                                if D20 > 15:
                                    $ action_speed = 4
                                    if "setpace" not in Girl.recent_history:
                                        $ Girl.change_stat("inhibition", 80, 3)
                                elif D20 > 10:
                                    $ action_speed = 3
                                elif D20 > 5:
                                    $ action_speed = 2
                                else:
                                    $ action_speed = 1
                                $ Girl.recent_history.append("setpace")

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
                                    "I also want to fondle her breasts." if offhand_action != "fondle breasts":
                                            if Girl.Action and MultiAction:
                                                $ offhand_action = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ Girl.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Shift primary action":
                                            if Girl.Action and MultiAction:
                                                    menu:
                                                        "How about a handy?":
                                                                $ action_context = "shift"
                                                                call Storm_BJ_After
                                                                call Storm_Handjob
                                                        "How about a titjob?":
                                                                $ action_context = "shift"
                                                                call Storm_BJ_After
                                                                call Storm_Titjob
                                                        "Never Mind":
                                                                jump Storm_BJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [Girl.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(Girl)
                                            "Asks [Girl.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(Girl)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(Girl)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Storm_BJ_Cycle
                                            "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Storm_BJ_Cycle
                                            "Never mind":
                                                        jump Storm_BJ_Cycle
                                    "Undress [Girl.name]":
                                            call Girl_Undress(Girl)
                                    "Clean up [Girl.name] (locked)" if not Girl.Spunk:
                                            pass
                                    "Clean up [Girl.name]" if Girl.Spunk:
                                            call Girl_Cleanup(Girl,"ask")
                                    "Never mind":
                                            jump Storm_BJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Storm_BJ_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Storm_BJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Storm_BJ_Reset
                                    $ line = 0
                                    jump Storm_BJ_After
        #End menu (if line)

        call Shift_Focus(Girl)
        call Sex_Dialog(Girl,Partner)

        #If either of you could cum

        $ counter += 1
        $ Round -= 1
        if action_speed:
            $ Player.Wet = 1 #wets penis
            $ Player.Spunk = 0 if Player.Spunk else Player.Spunk #cleans you off after one cycle

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or Girl.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(Girl)
                            if "angry" in Girl.recent_history:
                                call Storm_BJ_Reset
                                return
                            $ Girl.change_stat("lust", 200, 5)
                            if 100 > Girl.lust >= 70 and Girl.OCount < 2 and Girl.SEXP >= 20:
                                $ Girl.recent_history.append("unsatisfied")
                                $ Girl.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Storm_BJ_After
                            $ line = "came"

                    if Girl.lust >= 100:
                            #If [Girl.name] can cum
                            call Girl_Cumming(Girl)
                            if action_context == "shift" or "angry" in Girl.recent_history:
                                jump Storm_BJ_After

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in Girl.recent_history:#And [Girl.name] is unsatisfied,
                                    "[Girl.name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Storm_BJ_After
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if Girl.SEXP >= 100 or ApprovalCheck(Girl, 1200, "LO"):
            pass
        elif counter == (15 + Girl.Blow):
                $ Girl.Brows = "angry"
                menu:
                    ch_s "My jaw is becoming uncomfortable, could we do something else?"
                    "How about a Handy?" if Girl.Action and MultiAction:
                            $ action_context = "shift"
                            call Storm_BJ_After
                            call Storm_Handjob
                            return
                    "Finish up." if Player.FocusX:
                            "You release your concentration. . ."
                            $ Player.FocusX = 0
                            $ Player.Focus += 15
                            $ counter += 1
                            "[line]."
                            jump Storm_BJ_Cycle
                    "Let's try something else." if MultiAction:
                            $ line = 0
                            call Storm_BJ_Reset
                            $ action_context = "shift"
                            jump Storm_BJ_After
                    "No, get back down there.":
                            if ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "O"):
                                $ Girl.change_stat("love", 200, -5)
                                $ Girl.change_stat("obedience", 50, 3)
                                $ Girl.change_stat("obedience", 80, 2)
                                "She scowls but gets back to work."
                            else:
                                $ Girl.change_face("angry", 1)
                                "She scowls at you, drops you cock and pulls back."
                                ch_s "Well then."
                                $ Girl.change_stat("love", 50, -3, 1)
                                $ Girl.change_stat("love", 80, -4, 1)
                                $ Girl.change_stat("obedience", 30, -1, 1)
                                $ Girl.change_stat("obedience", 50, -1, 1)
                                $ Girl.recent_history.append("angry")
                                $ Girl.daily_history.append("angry")
                                jump Storm_BJ_After
        elif counter == (10 + Girl.Blow) and Girl.SEXP <= 100 and not ApprovalCheck(Girl, 1200, "LO"):
                    $ Girl.Brows = "confused"
                    ch_s "Are you about finished? I am growing tired of this."
        #End Count check

        call Escalation(Girl) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(Girl,10) #"It is getting late, [Girl.Petname]. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(Girl,5)   #"We should take a break soon."

    #Round = 0 loop breaks
    $ Girl.change_face("bemused", 0)
    $ line = 0
    call Sex_Basic_Dialog(Girl,"done") # ch_s "I need to take a moment to collect myself."

label Storm_BJ_After:
    $ Girl.change_face("sexy")

    $ Girl.Blow += 1
    $ Girl.Action -=1
    $ Girl.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ Girl.Addictionrate += 1

    call Partner_Like(Girl,2)

    if "Storm Jobber" in Achievements:
        pass
    elif Girl.Blow >= 10:
        $ Girl.change_face("smile", 1)
        ch_s "I cannot imagine how I went this long without such a delicacy, [Girl.Petname]."
        $ Achievements.append("Storm Jobber")
        $Girl.SEXP += 5
    elif action_context == "shift":
        pass
    elif Girl.Blow == 1:
            $Girl.SEXP += 15
            if Girl.love >= 500:
                $ Girl.Mouth = "smile"
                ch_s "Hmm, that certainly was enjoyable . ."
            elif Player.Focus <= 20:
                $ Girl.Mouth = "sad"
                ch_s "did that meet your expectations?"
    elif Girl.Blow == 5:
        ch_s "I expect that you enjoyed that."
    $ temp_modifier = 0
    if action_context != "shift":
        call Storm_BJ_Reset
    call Checkout
    return



# end Girl.Blowjob                                 //////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy
label Storm_Dildo_Check:
    if "dildo" in Player.Inventory:
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in Girl.Inventory:
        "You ask [Girl.name] to get out her favorite Dildo."
    else:
        "You don't have one of those on you."
        return 0
    return 1

label Storm_Dildo_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(Girl)
    call Storm_Dildo_Check
    if not _return:
        return

    if Girl.DildoP: #You've done it before
        $ temp_modifier += 15
    if Girl.PantsNum() >= 6: # she's got pants on.
        $ temp_modifier -= 20

    if Girl.lust > 95:
        $ temp_modifier += 20
    elif Girl.lust > 85: #She's really horny
        $ temp_modifier += 15

    if action_context == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in Girl.Traits:
        $ temp_modifier += (5*Taboo)
    if Girl in Player.Harem or "sex friend" in Girl.Petnames:
        $ temp_modifier += 10
    elif "ex" in Girl.Traits:
        $ temp_modifier -= 40
    if Girl.ForcedCount and not Girl.Forced:
        $ temp_modifier -= 5 * Girl.ForcedCount

    if Taboo and "tabno" in Girl.daily_history:
        $ temp_modifier -= 10

    if "no dildo" in Girl.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no dildo" in Girl.recent_history else 0

    $ Approval = ApprovalCheck(Girl, 1250, TabM = 4) # 125, 140, 155, Taboo -160(335)

    if action_context == Girl:                                                                  #Storm auto-starts
                if Approval > 2:                                                      # fix, add emma auto stuff here
                    if Girl.wearing_skirt:
                        "[Girl.name] grabs her dildo, hiking up her skirt as she does."
                        $ Girl.Upskirt = 1
                    elif Girl.PantsNum() > 6:
                        "[Girl.name] grabs her dildo, pulling down her pants as she does."
                        $ Girl.Legs = 0
                    else:
                        "[Girl.name] grabs her dildo, rubbing is suggestively against her crotch."
                    $ Girl.SeenPanties = 1
                    "She slides the tip along her pussy and seems to want you to insert it."
                    menu:
                        "What do you do?"
                        "Nothing.":
                            $ Girl.change_stat("inhibition", 80, 3)
                            $ Girl.change_stat("inhibition", 50, 2)
                            "[Girl.name] slides it in."
                        "Go for it.":
                            $ Girl.change_face("sexy", 1)
                            $ Girl.change_stat("inhibition", 80, 3)
                            ch_p "Oh yeah, [Girl.Pet], let's do this."
                            $ Girl.nameCheck() #checks reaction to petname
                            "You grab the dildo and slide it in."
                            $ Girl.change_stat("love", 85, 1)
                            $ Girl.change_stat("obedience", 90, 1)
                            $ Girl.change_stat("obedience", 50, 2)
                        "Ask her to stop.":
                            $ Girl.change_face("surprised")
                            $ Girl.change_stat("inhibition", 70, 1)
                            ch_p "Let's not do that right now, [Girl.Pet]."
                            $ Girl.nameCheck() #checks reaction to petname
                            "[Girl.name] sets the dildo down."
                            $ Girl.OutfitChange()
                            $ Girl.change_stat("obedience", 90, 1)
                            $ Girl.change_stat("obedience", 50, 1)
                            $ Girl.change_stat("obedience", 30, 2)
                            return
                    jump Storm_DP_Prep
                else:
                    $ temp_modifier = 0                               # fix, add emma auto stuff here
                    $ offhand_action = 0
                return

    if action_context == "auto":
                "You rub the dildo across her body, and along her moist slit."
                $ Girl.change_face("surprised", 1)

                if (Girl.DildoP and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
                    "[Girl.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                    $ Girl.change_face("sexy")
                    $ Girl.change_stat("obedience", 70, 3)
                    $ Girl.change_stat("inhibition", 50, 3)
                    $ Girl.change_stat("inhibition", 70, 1)
                    ch_s "Hmm, [Girl.Petname], toys!"
                    jump Storm_DP_Prep
                else:                                                                                                            #she's questioning it
                    $ Girl.Brows = "angry"
                    menu:
                        ch_s "Excuse yourself, what are you planning to do with that?!"
                        "Sorry, sorry! Never mind.":
                            if Approval:
                                $ Girl.change_face("sexy", 1)
                                $ Girl.change_stat("obedience", 70, 3)
                                $ Girl.change_stat("inhibition", 50, 3)
                                $ Girl.change_stat("inhibition", 70, 1)
                                ch_s "Well, now that you mention it. . ."
                                jump Storm_DP_Prep
                            "You pull back before you really get it in."
                            $ Girl.change_face("bemused", 1)
                            if Girl.DildoP:
                                ch_s "Well, [Girl.Petname], maybe warn me next time?"
                            else:
                                ch_s "Well, [Girl.Petname], that's a little much. . . for now . . ."
                        "Just playing with my favorite toys.":
                            $ Girl.change_stat("love", 80, -10, 1)
                            $ Girl.change_stat("love", 200, -10)
                            "You press it inside some more."
                            $ Girl.change_stat("obedience", 70, 3)
                            $ Girl.change_stat("inhibition", 50, 3)
                            if not ApprovalCheck(Girl, 700, "O", TabM=1): #Checks if obedience is 700+
                                $ Girl.change_face("angry")
                                "[Girl.name] shoves you away and slaps you in the face."
                                ch_s "Ask nicely before trying anything like that!"
                                $ Girl.change_stat("love", 50, -10, 1)
                                $ Girl.change_stat("obedience", 50, 3)
                                $ renpy.pop_call()
                                if action_context:
                                    $ renpy.pop_call()
                                if renpy.showing("Storm_SexSprite"):
                                    call Storm_Sex_Reset
                                $ Girl.recent_history.append("angry")
                                $ Girl.daily_history.append("angry")
                            else:
                                $ Girl.change_face("sad")
                                "[Girl.name] doesn't seem to be into this, you're lucky she's so obedient."
                                jump Storm_DP_Prep
                return
    #end Auto

    if not Girl.DildoP:
            #first time
            $ Girl.change_face("surprised", 1)
            $ Girl.Mouth = "kiss"
            ch_s "Hmmm, so you'd like to try out some toys?"
            if Girl.Forced:
                $ Girl.change_face("sad")
                ch_s "I suppose there are worst things you could ask for."

    if not Girl.DildoP and Approval:
            #First time dialog
            if Girl.Forced:
                $ Girl.change_face("sad")
                $ Girl.change_stat("love", 70, -3, 1)
                $ Girl.change_stat("love", 20, -2, 1)
            elif Girl.love >= (Girl.obedience + Girl.inhibition):
                $ Girl.change_face("sexy")
                $ Girl.Brows = "sad"
                $ Girl.Mouth = "smile"
                ch_s "I've had a reasonable amount of experience with these, you know. . ."
            elif Girl.obedience >= Girl.inhibition:
                $ Girl.change_face("normal")
                ch_s "If that is what you want, [Girl.Petname]. . ."
            else: # Uninhibited
                $ Girl.change_face("sad")
                $ Girl.Mouth = "smile"
                ch_s "I guess it could be fun with a partner. . ."

    elif Approval:
            #Second time+ dialog
            if Girl.Forced:
                $ Girl.change_face("sad")
                $ Girl.change_stat("love", 70, -3, 1)
                $ Girl.change_stat("love", 20, -2, 1)
                ch_s "The toys again?"
            elif not Taboo and "tabno" in Girl.daily_history:
                ch_s "Well, at least you got us some privacy this time. . ."
            elif "dildo pussy" in Girl.recent_history:
                $ Girl.change_face("sexy", 1)
                ch_s "Mmm, again? Ok, let's get to it."
                jump Storm_DP_Prep
            elif "dildo pussy" in Girl.daily_history:
                $ Girl.change_face("sexy", 1)
                $ line = renpy.random.choice(["Breaking out the toys again?",
                    "You did not get enough earlier?",
                    "You're going to wear me out."])
                ch_s "[line]"
            elif Girl.DildoP < 3:
                $ Girl.change_face("sexy", 1)
                $ Girl.Brows = "confused"
                $ Girl.Mouth = "kiss"
                ch_s "You want to stick it in my pussy again?"
            else:
                $ Girl.change_face("sexy", 1)
                $ Girl.ArmPose = 2
                $ line = renpy.random.choice(["You want some of this action?",
                    "So you'd like another go?",
                    "You want to stick it in my pussy again?",
                    "You want me ta lube up your toy?"])
                ch_s "[line]"
                $ line = 0

    if Approval >= 2:
            #She's into it. . .
            if Girl.Forced:
                $ Girl.change_face("sad")
                $ Girl.change_stat("obedience", 90, 1)
                $ Girl.change_stat("inhibition", 60, 1)
                ch_s "Ok, fine."
            else:
                $ Girl.change_face("sexy", 1)
                $ Girl.change_stat("love", 90, 1)
                $ Girl.change_stat("inhibition", 50, 3)
                $ line = renpy.random.choice(["Well, sure, stick it in.",
                    "Well. . . ok.",
                    "Sure!",
                    "I guess I could. . . stick it in.",
                    "Delightful.",
                    "Hmm, ok, ok."])
                ch_s "[line]"
                $ line = 0
            $ Girl.change_stat("obedience", 20, 1)
            $ Girl.change_stat("obedience", 60, 1)
            $ Girl.change_stat("inhibition", 70, 2)
            jump Storm_DP_Prep

    else:
            #She's not into it, but maybe. . .
            $ Girl.change_face("angry")
            if "no dildo" in Girl.recent_history:
                ch_s "What part of \"no,\" did you not get, [Girl.Petname]?"
            elif Taboo and "tabno" in Girl.daily_history and "no dildo" in Girl.daily_history:
                ch_s "Stop showing that thing around in public!"
            elif "no dildo" in Girl.daily_history:
                ch_s "I already told you \"no,\" [Girl.Petname]."
            elif Taboo and "tabno" in Girl.daily_history:
                ch_s "Stop showing that thing around in public!"
            elif not Girl.DildoP:
                $ Girl.change_face("bemused")
                ch_s "I'm a bit past toys, [Girl.Petname]. . ."
            else:
                $ Girl.change_face("bemused")
                ch_s "We don't need any toys, do we, [Girl.Petname]?"
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in Girl.daily_history:
                    $ Girl.change_face("bemused")
                    ch_s "I thought as much, [Girl.Petname]."
                    return
                "Maybe later?" if "no dildo" not in Girl.daily_history:
                    $ Girl.change_face("sexy")
                    ch_s "Maybe I'll practice on my own time, [Girl.Petname]."
                    $ Girl.change_stat("love", 80, 2)
                    $ Girl.change_stat("inhibition", 70, 2)
                    if Taboo:
                        $ Girl.recent_history.append("tabno")
                        $ Girl.daily_history.append("tabno")
                    $ Girl.recent_history.append("no dildo")
                    $ Girl.daily_history.append("no dildo")
                    return
                "I think you'd like it. . .":
                    if Approval:
                        $ Girl.change_face("sexy")
                        $ Girl.change_stat("obedience", 90, 2)
                        $ Girl.change_stat("obedience", 50, 2)
                        $ Girl.change_stat("inhibition", 70, 3)
                        $ Girl.change_stat("inhibition", 40, 2)
                        $ line = renpy.random.choice(["Well, sure, stick it in.",
                            "I suppose. . .",
                            "You make a compelling argument."])
                        ch_s "[line]"
                        $ line = 0
                        jump Storm_DP_Prep
                    else:
                        pass

                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck(Girl, 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                    if Approval > 1 or (Approval and Girl.Forced):
                        $ Girl.change_face("sad")
                        $ Girl.change_stat("love", 70, -5, 1)
                        $ Girl.change_stat("love", 200, -5)
                        ch_s
                        $ Girl.change_stat("obedience", 80, 4)
                        $ Girl.change_stat("inhibition", 80, 1)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.Forced = 1
                        jump Storm_DP_Prep
                    else:
                        $ Girl.change_stat("love", 200, -20)
                        $ Girl.recent_history.append("angry")
                        $ Girl.daily_history.append("angry")

    #She refused all offers.
    $ Girl.ArmPose = 1
    if "no dildo" in Girl.daily_history:

            $ Girl.recent_history.append("angry")
            $ Girl.daily_history.append("angry")
    elif Girl.Forced:
            $ Girl.change_face("angry", 1)
            ch_s "I'm not going to let you use that on me."
            $ Girl.change_stat("lust", 200, 5)
            if Girl.love > 300:
                    $ Girl.change_stat("love", 70, -2)
            $ Girl.change_stat("obedience", 50, -2)
            $ Girl.recent_history.append("angry")
            $ Girl.daily_history.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
            $ Girl.change_face("angry", 1)
            $ Girl.recent_history.append("tabno")
            $ Girl.daily_history.append("tabno")
            ch_s "Not here!"
            $ Girl.change_stat("lust", 200, 5)
            $ Girl.change_stat("obedience", 50, -3)
    elif Girl.DildoP:
            $ Girl.change_face("sad")
            ch_s "Sorry, you can keep your toys to yourself."
    else:
            $ Girl.change_face("normal", 1)
            ch_s "No way."
    $ Girl.recent_history.append("no dildo")
    $ Girl.daily_history.append("no dildo")
    $ temp_modifier = 0
    return

label Storm_DP_Prep: #Animation set-up
    if offhand_action == "dildo pussy":
        return

    if not Girl.Forced and action_context != "auto":
        $ temp_modifier = 15 if Girl.PantsNum() > 6 else 0
        call Bottoms_Off(Girl)
        if "angry" in Girl.recent_history:
            return

    $ temp_modifier = 0
    call Storm_Pussy_Launch("dildo pussy")
    if not Girl.DildoP:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -75)
            $ Girl.change_stat("obedience", 70, 60)
            $ Girl.change_stat("inhibition", 80, 35)
        else:
            $ Girl.change_stat("love", 90, 10)
            $ Girl.change_stat("obedience", 70, 20)
            $ Girl.change_stat("inhibition", 80, 45)
    if Taboo:
        $ Girl.inhibition += int(Taboo/10)
        $ Girl.lust += int(Taboo/5)


    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ line = 0
    $ counter = 0
    if Taboo:
        $ Girl.DrainWord("tabno")
    $ Girl.DrainWord("no dildo")
    $ Girl.recent_history.append("dildo pussy")
    $ Girl.daily_history.append("dildo pussy")

label Storm_DP_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(Girl)
        call Storm_Pussy_Launch("dildo pussy")
        $ Girl.lustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                call Slap_Ass(Girl)
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
                                            if Girl.Action and MultiAction:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ Girl.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Shift primary action":
                                            if Girl.Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in her ass.":
                                                                $ action_context = "shift"
                                                                call Storm_DP_After
                                                                call Storm_Insert_Ass
                                                        "Just stick a finger in her ass without asking.":
                                                                $ action_context = "auto"
                                                                call Storm_DP_After
                                                                call Storm_Insert_Ass
                                                        "I want to shift the dildo to her ass.":
                                                                $ action_context = "shift"
                                                                call Storm_DP_After
                                                                call Storm_Dildo_Ass
                                                        "Never Mind":
                                                                jump Storm_DP_Cycle
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Shift your focus" if offhand_action:
                                                $ action_context = "shift focus"
                                                call Storm_DP_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not offhand_action:
                                                pass
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [Girl.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(Girl)
                                            "Asks [Girl.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(Girl)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(Girl)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Storm_DP_Cycle
                                            "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Storm_DP_Cycle
                                            "Never mind":
                                                        jump Storm_DP_Cycle
                                    "Undress [Girl.name]":
                                            call Girl_Undress(Girl)
                                    "Clean up [Girl.name] (locked)" if not Girl.Spunk:
                                            pass
                                    "Clean up [Girl.name]" if Girl.Spunk:
                                            call Girl_Cleanup(Girl,"ask")
                                    "Never mind":
                                            jump Storm_DP_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Storm_Pos_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Storm_DP_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Storm_Pos_Reset
                                    $ line = 0
                                    jump Storm_DP_After
        #End menu (if line)

        if Girl.Panties or Girl.PantsNum() > 6 or Girl.HoseNum() >= 5: #This checks if [Girl.name] wants to strip down.
                call Girl_Undress(Girl,"auto")

        call Shift_Focus(Girl)
        call Sex_Dialog(Girl,Partner)

        #If either of you could cum

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or Girl.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(Girl)
                            if "angry" in Girl.recent_history:
                                call Storm_Pos_Reset
                                return
                            $ Girl.change_stat("lust", 200, 5)
                            if 100 > Girl.lust >= 70 and Girl.OCount < 2:
                                $ Girl.recent_history.append("unsatisfied")
                                $ Girl.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Storm_DP_After
                            $ line = "came"
                    if Girl.lust >= 100:
                            #If [Girl.name] can cum
                            call Girl_Cumming(Girl)
                            if action_context == "shift" or "angry" in Girl.recent_history:
                                jump Storm_DP_After
                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."
                            if "unsatisfied" in Girl.recent_history:#And [Girl.name] is unsatisfied,
                                    "[Girl.name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Storm_DP_After
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if Girl.SEXP >= 100 or ApprovalCheck(Girl, 1200, "LO"):
            pass
        elif counter == (5 + Girl.DildoP):
                    $ Girl.Brows = "confused"
                    ch_s "What are you even doing down there?"
        elif Girl.lust >= 80:
                    pass
        elif counter == (15 + Girl.DildoP) and Girl.SEXP >= 15 and not ApprovalCheck(Girl, 1500):
                    $ Girl.Brows = "confused"
                    menu:
                        ch_s "[Girl.Petname], this is getting uncomfortable, maybe we could try something else."
                        "Finish up.":
                                "You let go. . ."
                                jump Storm_DP_After
                        "Let's try something else." if MultiAction:
                                $ line = 0
                                $ action_context = "shift"
                                jump Storm_DP_After
                        "No, this is fun.":
                                if ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "O"):
                                    $ Girl.change_stat("love", 200, -5)
                                    $ Girl.change_stat("obedience", 50, 3)
                                    $ Girl.change_stat("obedience", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ Girl.change_face("angry", 1)
                                    call Storm_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_s "Well if that's your attitude, I don't need your \"help\"."
                                    $ Girl.change_stat("love", 50, -3, 1)
                                    $ Girl.change_stat("love", 80, -4, 1)
                                    $ Girl.change_stat("obedience", 30, -1, 1)
                                    $ Girl.change_stat("obedience", 50, -1, 1)
                                    $ Girl.recent_history.append("angry")
                                    $ Girl.daily_history.append("angry")
                                    jump Storm_DP_After
        #End Count check

        if Round == 10:
                call Sex_Basic_Dialog(Girl,10) #"It is getting late, [Girl.Petname]. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(Girl,5)   #"We should take a break soon."

    #Round = 0 loop breaks
    $ Girl.change_face("bemused", 0)
    $ line = 0
    call Sex_Basic_Dialog(Girl,"done") # ch_s "I need to take a moment to collect myself."


label Storm_DP_After:
    if not action_context: #fix  action_context != "shift" and action_context != "auto" and action_context != "pullback":
        call Storm_Pos_Reset

    $ Girl.change_face("sexy")

    $ Girl.DildoP += 1
    $ Girl.Action -=1

    call Partner_Like(Girl,1)

    if Girl.DildoP == 1:
            $ Girl.SEXP += 10
            if not action_context:
                if Girl.love >= 500 and "unsatisfied" not in Girl.recent_history:
                    ch_s "I appreciate the work you put in. . ."
                elif Girl.obedience <= 500 and Player.Focus <= 20:
                    $ Girl.change_face("perplexed", 1)
                    ch_s "Did you enjoy that?"

    $ temp_modifier = 0
#    if action_context == "shift":
#        ch_s "Mmm, so what else did you have in mind?"
    call Checkout
    return

# end Girl.Dildo Pussy /////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////Start Insert Ass

label Storm_Dildo_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(Girl)
    call Storm_Dildo_Check
    if not _return:
        return

    if Girl.Loose:
        $ temp_modifier += 30
    elif "anal" in Girl.recent_history or "dildo anal" in Girl.recent_history:
        $ temp_modifier -= 20
    elif "anal" in Girl.daily_history or "dildo anal" in Girl.daily_history:
        $ temp_modifier -= 10
    elif (Girl.Anal + Girl.DildoA + Girl.Plug) > 0: #You've done it before
        $ temp_modifier += 20

    if Girl.PantsNum() >= 6: # she's got pants on.
        $ temp_modifier -= 20

    if Girl.lust > 95:
        $ temp_modifier += 20
    elif Girl.lust > 85: #She's really horny
        $ temp_modifier += 15

    if action_context == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in Girl.Traits:
        $ temp_modifier += (5*Taboo)
    if Girl in Player.Harem or "sex friend" in Girl.Petnames:
        $ temp_modifier += 10
    elif "ex" in Girl.Traits:
        $ temp_modifier -= 40
    if Girl.ForcedCount and not Girl.Forced:
        $ temp_modifier -= 5 * Girl.ForcedCount

    if Taboo and "tabno" in Girl.daily_history:
        $ temp_modifier -= 10

    if "no dildo" in Girl.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no dildo" in Girl.recent_history else 0

    $ Approval = ApprovalCheck(Girl, 1450, TabM = 4) # 145, 160, 175, Taboo -160(355)

    if action_context == Girl:
            #Storm auto-starts
            if Approval > 2:                                                      # fix, add emma auto stuff here
                if Girl.wearing_skirt:
                    "[Girl.name] grabs her dildo, hiking up her skirt as she does."
                    $ Girl.Upskirt = 1
                elif Girl.PantsNum() > 6:
                    "[Girl.name] grabs her dildo, pulling down her pants as she does."
                    $ Girl.Legs = 0
                else:
                    "[Girl.name] grabs her dildo, rubbing is suggestively against her ass."
                $ Girl.SeenPanties = 1
                "She slides the tip against her asshole, and seems to want you to insert it."
                menu:
                    "What do you do?"
                    "Nothing.":
                        $ Girl.change_stat("inhibition", 80, 3)
                        $ Girl.change_stat("inhibition", 50, 2)
                        "[Girl.name] slides it in."
                    "Go for it.":
                        $ Girl.change_face("sexy", 1)
                        $ Girl.change_stat("inhibition", 80, 3)
                        ch_p "Oh yeah, [Girl.Pet], let's do this."
                        $ Girl.nameCheck() #checks reaction to petname
                        "You grab the dildo and slide it in."
                        $ Girl.change_stat("love", 85, 1)
                        $ Girl.change_stat("obedience", 90, 1)
                        $ Girl.change_stat("obedience", 50, 2)
                    "Ask her to stop.":
                        $ Girl.change_face("surprised")
                        $ Girl.change_stat("inhibition", 70, 1)
                        ch_p "Let's not do that right now, [Girl.Pet]."
                        $ Girl.nameCheck() #checks reaction to petname
                        "[Girl.name] sets the dildo down."
                        $ Girl.OutfitChange()
                        $ Girl.change_stat("obedience", 90, 1)
                        $ Girl.change_stat("obedience", 50, 1)
                        $ Girl.change_stat("obedience", 30, 2)
                        return
                jump Storm_DA_Prep
            else:
                $ temp_modifier = 0                               # fix, add emma auto stuff here
                $ offhand_action = 0
            return

    if action_context == "auto":
            "You rub the dildo across her body, and against her tight anus."
            $ Girl.change_face("surprised", 1)

            if (Girl.DildoA and Approval) or (Approval > 1):
                #this is not the first time you've had sex, or she's into it
                "[Girl.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                $ Girl.change_face("sexy")
                $ Girl.change_stat("obedience", 70, 3)
                $ Girl.change_stat("inhibition", 50, 3)
                $ Girl.change_stat("inhibition", 70, 1)
                ch_s "Mmmm, [Girl.Petname], toys. . ."
                jump Storm_DA_Prep
            else:
                #she's questioning it
                $ Girl.Brows = "angry"
                menu:
                    ch_s "Excuse yourself, what are you planning to do with that?!"
                    "Sorry, sorry! Never mind.":
                        if Approval:
                            $ Girl.change_face("sexy", 1)
                            $ Girl.change_stat("obedience", 70, 3)
                            $ Girl.change_stat("inhibition", 50, 3)
                            $ Girl.change_stat("inhibition", 70, 1)
                            ch_s "Well, now that you mention it. . ."
                            jump Storm_DA_Prep
                        "You pull back before you really get it in."
                        $ Girl.change_face("bemused", 1)
                        if Girl.DildoA:
                            ch_s "Well, [Girl.Petname], maybe warn me next time?"
                        else:
                            ch_s "Well, [Girl.Petname], that's a little much. . . for now . . ."
                    "Just playing with my favorite toys.":
                        $ Girl.change_stat("love", 80, -10, 1)
                        $ Girl.change_stat("love", 200, -10)
                        "You press it inside some more."
                        $ Girl.change_stat("obedience", 70, 3)
                        $ Girl.change_stat("inhibition", 50, 3)
                        if not ApprovalCheck(Girl, 700, "O", TabM=1): #Checks if obedience is 700+
                            $ Girl.change_face("angry")
                            "[Girl.name] shoves you away and slaps you in the face."
                            ch_s "Ask nicely if you want to stick something in my ass!"
                            $ Girl.change_stat("love", 50, -10, 1)
                            $ Girl.change_stat("obedience", 50, 3)
                            $ renpy.pop_call()
                            if action_context:
                                $ renpy.pop_call()
                            if renpy.showing("Storm_SexSprite"):
                                call Storm_Sex_Reset
                            $ Girl.recent_history.append("angry")
                            $ Girl.daily_history.append("angry")
                        else:
                            $ Girl.change_face("sad")
                            "[Girl.name] doesn't seem to be into this, you're lucky she's so obedient."
                            jump Storm_DA_Prep
            return
    #end auto

    if not Girl.DildoA:
            #first time
            $ Girl.change_face("surprised", 1)
            $ Girl.Mouth = "kiss"
            ch_s "Hmm, you don't take half measures. . ."
            if Girl.Forced:
                $ Girl.change_face("sad")
                ch_s "They always go for the butt. . ."

    if not Girl.DildoA and Approval:
            #First time dialog
            if Girl.Forced:
                $ Girl.change_face("sad")
                $ Girl.change_stat("love", 70, -3, 1)
                $ Girl.change_stat("love", 20, -2, 1)
            elif Girl.love >= (Girl.obedience + Girl.inhibition):
                $ Girl.change_face("sexy")
                $ Girl.Brows = "sad"
                $ Girl.Mouth = "smile"
                ch_s "I suppose you might enjoy that. . ."
            elif Girl.obedience >= Girl.inhibition:
                $ Girl.change_face("normal")
                ch_s "If that is what you want, [Girl.Petname]. . ."
            else: # Uninhibited
                $ Girl.change_face("sad")
                $ Girl.Mouth = "smile"
                ch_s "I suppose I could enjoy that. . ."

    elif Approval:
            #Second time+ dialog
            if Girl.Forced:
                $ Girl.change_face("sad")
                $ Girl.change_stat("love", 70, -3, 1)
                $ Girl.change_stat("love", 20, -2, 1)
                ch_s "The toys again?"
            elif not Taboo and "tabno" in Girl.daily_history:
                ch_s "Well, at least you got us some privacy this time. . ."
            elif "dildo anal" in Girl.daily_history and not Girl.Loose:
                pass
            elif Girl.DildoA < 3:
                $ Girl.change_face("sexy", 1)
                $ Girl.Brows = "confused"
                $ Girl.Mouth = "kiss"
                ch_s "You want to stick it in my ass again?"
            else:
                $ Girl.change_face("sexy", 1)
                $ Girl.ArmPose = 2
                $ line = renpy.random.choice(["You want some of this action?",
                    "So you'd like another go?",
                    "You'd like to stick it in my ass again?",
                    "You'd like me to lube up your toy?"])
                ch_s "[line]"
                $ line = 0

    if Approval >= 2:
            #She's into it. . .
            if Girl.Forced:
                $ Girl.change_face("sad")
                $ Girl.change_stat("obedience", 90, 1)
                $ Girl.change_stat("inhibition", 60, 1)
                ch_s "Oh, fine."
            else:
                $ Girl.change_face("sexy", 1)
                $ Girl.change_stat("love", 90, 1)
                $ Girl.change_stat("inhibition", 50, 3)
                $ line = renpy.random.choice(["Well, sure, stick it in.",
                    "Hmm. . . ok.",
                    "Sure!",
                    "I guess I could. . . stick it in.",
                    "Delightful.",
                    "Hmm, ok, ok."])
                ch_s "[line]"
                $ line = 0
            $ Girl.change_stat("obedience", 20, 1)
            $ Girl.change_stat("obedience", 60, 1)
            $ Girl.change_stat("inhibition", 70, 2)
            jump Storm_DA_Prep

    else:
            #She's not into it, but maybe. . .
            $ Girl.change_face("angry")
            if "no dildo" in Girl.recent_history:
                ch_s "What part of \"no,\" did you not get, [Girl.Petname]?"
            elif Taboo and "tabno" in Girl.daily_history and "no dildo" in Girl.daily_history:
                ch_s "Stop swinging that thing around in public!"
            elif "no dildo" in Girl.daily_history:
                ch_s "I already told you \"no,\" [Girl.Petname]."
            elif Taboo and "tabno" in Girl.daily_history:
                ch_s "I already told you that I wouldn't do that out here!"
            elif not Girl.DildoA:
                $ Girl.change_face("bemused")
                ch_s "I'm just not into toys, [Girl.Petname]. . ."
            else:
                $ Girl.change_face("bemused")
                ch_s "I don't think we need any toys, [Girl.Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in Girl.daily_history:
                    $ Girl.change_face("bemused")
                    ch_s "I'm sure, [Girl.Petname]."
                    return
                "Maybe later?" if "no dildo" not in Girl.daily_history:
                    $ Girl.change_face("sexy")
                    ch_s "Perhaps I'll practice on my own time, [Girl.Petname]."
                    $ Girl.change_stat("love", 80, 2)
                    $ Girl.change_stat("inhibition", 70, 2)
                    if Taboo:
                        $ Girl.recent_history.append("tabno")
                        $ Girl.daily_history.append("tabno")
                    $ Girl.recent_history.append("no dildo")
                    $ Girl.daily_history.append("no dildo")
                    return
                "I think you'd like it. . .":
                    if Approval:
                        $ Girl.change_face("sexy")
                        $ Girl.change_stat("obedience", 90, 2)
                        $ Girl.change_stat("obedience", 50, 2)
                        $ Girl.change_stat("inhibition", 70, 3)
                        $ Girl.change_stat("inhibition", 40, 2)
                        $ line = renpy.random.choice(["Very well, stick it in.",
                            "I suppose. . .",
                            "You make a compelling argument."])
                        ch_s "[line]"
                        $ line = 0
                        jump Storm_DA_Prep
                    else:
                        pass

                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck(Girl, 1050, "OI", TabM = 3) # 105, 120, 135, -120(225)
                    if Approval > 1 or (Approval and Girl.Forced):
                        $ Girl.change_face("sad")
                        $ Girl.change_stat("love", 70, -5, 1)
                        $ Girl.change_stat("love", 200, -5)

                        $ Girl.change_stat("obedience", 80, 4)
                        $ Girl.change_stat("inhibition", 80, 1)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.Forced = 1
                        jump Storm_DA_Prep
                    else:
                        $ Girl.change_stat("love", 200, -20)
                        $ Girl.recent_history.append("angry")
                        $ Girl.daily_history.append("angry")

    #She refused all offers.
    $ Girl.ArmPose = 1
    if "no dildo" in Girl.daily_history:

            $ Girl.recent_history.append("angry")
            $ Girl.daily_history.append("angry")
    elif Girl.Forced:
            $ Girl.change_face("angry", 1)
            ch_s "I'm not going to let you use that on me."
            $ Girl.change_stat("lust", 200, 5)
            if Girl.love > 300:
                    $ Girl.change_stat("love", 70, -2)
            $ Girl.change_stat("obedience", 50, -2)
            $ Girl.recent_history.append("angry")
            $ Girl.daily_history.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
            $ Girl.change_face("angry", 1)
            $ Girl.recent_history.append("tabno")
            $ Girl.daily_history.append("tabno")
            ch_s "Not here!"
            $ Girl.change_stat("lust", 200, 5)
            $ Girl.change_stat("obedience", 50, -3)
    elif Girl.DildoA:
            $ Girl.change_face("sad")
            ch_s "Sorry, you can keep your toys out of there."
    else:
            $ Girl.change_face("normal", 1)
            ch_s "No, thank you."
    $ Girl.recent_history.append("no dildo")
    $ Girl.daily_history.append("no dildo")
    $ temp_modifier = 0
    return

label Storm_DA_Prep: #Animation set-up
    if offhand_action == "dildo anal":
        return

    if not Girl.Forced and action_context != "auto":
        $ temp_modifier = 20 if Girl.PantsNum() > 6 else 0
        call Bottoms_Off(Girl)
        if "angry" in Girl.recent_history:
            return

    $ temp_modifier = 0
    call Storm_Pussy_Launch("dildo anal")
    if not Girl.DildoA:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -75)
            $ Girl.change_stat("obedience", 70, 60)
            $ Girl.change_stat("inhibition", 80, 35)
        else:
            $ Girl.change_stat("love", 90, 10)
            $ Girl.change_stat("obedience", 70, 20)
            $ Girl.change_stat("inhibition", 80, 45)
    if Taboo:
        $ Girl.inhibition += int(Taboo/10)
        $ Girl.lust += int(Taboo/5)


    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ line = 0
    $ counter = 0
    if Taboo:
        $ Girl.DrainWord("tabno")
    $ Girl.DrainWord("no dildo")
    $ Girl.recent_history.append("dildo anal")
    $ Girl.daily_history.append("dildo anal")

label Storm_DA_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(Girl)
        call Storm_Pussy_Launch("dildo anal")
        $ Girl.lustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                call Slap_Ass(Girl)
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
                                            if Girl.Action and MultiAction:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ Girl.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Shift primary action":
                                            if Girl.Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in her pussy.":
                                                                $ action_context = "shift"
                                                                call Storm_DA_After
                                                                call Storm_Fondle_Pussy
                                                        "Just stick a finger in her pussy without asking.":
                                                                $ action_context = "auto"
                                                                call Storm_DA_After
                                                                call Storm_Fondle_Pussy
                                                        "I want to shift the dildo to her pussy.":
                                                                $ action_context = "shift"
                                                                call Storm_DA_After
                                                                call Storm_Dildo_Pussy
                                                        "Never Mind":
                                                                jump Storm_DA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Shift your focus" if offhand_action:
                                                $ action_context = "shift focus"
                                                call Storm_DA_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not offhand_action:
                                                pass
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [Girl.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(Girl)
                                            "Asks [Girl.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(Girl)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(Girl)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Storm_DA_Cycle
                                            "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Storm_DA_Cycle
                                            "Never mind":
                                                        jump Storm_DA_Cycle
                                    "Undress [Girl.name]":
                                            call Girl_Undress(Girl)
                                    "Clean up [Girl.name] (locked)" if not Girl.Spunk:
                                            pass
                                    "Clean up [Girl.name]" if Girl.Spunk:
                                            call Girl_Cleanup(Girl,"ask")
                                    "Never mind":
                                            jump Storm_DA_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Storm_Pos_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Storm_DA_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Storm_Pos_Reset
                                    $ line = 0
                                    jump Storm_DA_After
        #End menu (if line)

        if Girl.Panties or Girl.PantsNum() > 6 or Girl.HoseNum() >= 5: #This checks if [Girl.name] wants to strip down.
                call Girl_Undress(Girl,"auto")

        call Shift_Focus(Girl)
        call Sex_Dialog(Girl,Partner)

        #If either of you could cum

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or Girl.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(Girl)
                            if "angry" in Girl.recent_history:
                                call Storm_Pos_Reset
                                return
                            $ Girl.change_stat("lust", 200, 5)
                            if 100 > Girl.lust >= 70 and Girl.OCount < 2:
                                $ Girl.recent_history.append("unsatisfied")
                                $ Girl.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Storm_DA_After
                            $ line = "came"

                    if Girl.lust >= 100:
                            #If [Girl.name] can cum
                            call Girl_Cumming(Girl)
                            if action_context == "shift" or "angry" in Girl.recent_history:
                                jump Storm_DA_After

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in Girl.recent_history:#And [Girl.name] is unsatisfied,
                                    "[Girl.name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Storm_DA_After
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if Girl.SEXP >= 100 or ApprovalCheck(Girl, 1200, "LO"):
            pass
        elif counter == (5 + Girl.DildoA):
                    $ Girl.Brows = "confused"
                    ch_s "What are you even doing down there?"
        elif Girl.lust >= 80:
                    pass
        elif counter == (15 + Girl.DildoA) and Girl.SEXP >= 15 and not ApprovalCheck(Girl, 1500):
                    $ Girl.Brows = "confused"
                    menu:
                        ch_s "[Girl.Petname], this is getting uncomfortable, maybe we could try something else."
                        "Finish up.":
                                "You let go. . ."
                                jump Storm_DA_After
                        "Let's try something else." if MultiAction:
                                $ line = 0
                                $ action_context = "shift"
                                jump Storm_DA_After
                        "No, this is fun.":
                                if ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "O"):
                                    $ Girl.change_stat("love", 200, -5)
                                    $ Girl.change_stat("obedience", 50, 3)
                                    $ Girl.change_stat("obedience", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ Girl.change_face("angry", 1)
                                    call Storm_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_s "Well if that's your attitude, I don't need your \"help\"."
                                    $ Girl.change_stat("love", 50, -3, 1)
                                    $ Girl.change_stat("love", 80, -4, 1)
                                    $ Girl.change_stat("obedience", 30, -1, 1)
                                    $ Girl.change_stat("obedience", 50, -1, 1)
                                    $ Girl.recent_history.append("angry")
                                    $ Girl.daily_history.append("angry")
                                    jump Storm_DA_After
        #End Count check

        if Round == 10:
                call Sex_Basic_Dialog(Girl,10) #"It is getting late, [Girl.Petname]. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(Girl,5)   #"We should take a break soon."

    #Round = 0 loop breaks
    $ Girl.change_face("bemused", 0)
    $ line = 0
    call Sex_Basic_Dialog(Girl,"done") # ch_s "I need to take a moment to collect myself."


label Storm_DA_After:
    if not action_context: #fix  action_context != "shift" and action_context != "auto" and action_context != "pullback":
        call Storm_Pos_Reset

    $ Girl.change_face("sexy")

    $ Girl.DildoA += 1
    $ Girl.Action -=1

    call Partner_Like(Girl,1)

    if Girl.DildoA == 1:
            $ Girl.SEXP += 10
            if not action_context:
                if Girl.love >= 500 and "unsatisfied" not in Girl.recent_history:
                    ch_s "That was. . . engaging. . ."
                elif Girl.obedience <= 500 and Player.Focus <= 20:
                    $ Girl.change_face("perplexed", 1)
                    ch_s "Did you enjoy that?"

    $ temp_modifier = 0
#    if action_context == "shift":
#        ch_s "Mmm, so what else did you have in mind?"
    call Checkout
    return

# end Girl.Dildo Ass /////////////////////////////////////////////////////////////////////////////

label Storm_Vibrator_Check:                                                                                 #fix this whole section is copy/paste unfinished
    if "vibrator" in Player.Inventory:
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in Girl.Inventory:
        "You ask [Girl.name] to get out her vibrator."
    else:
        "You don't have one of those on you."
        return 0
    return 1

## Girl.Footjob //////////////////////////////////////////////////////////////////////
label Storm_Footjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(Girl)
    if Girl.Foot >= 7: # She loves it
        $ temp_modifier += 10
    elif Girl.Foot >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif Girl.Foot: #You've done it before
        $ temp_modifier += 3

    if Girl.Addict >= 75 and Girl.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 10
    if Girl.Addict >= 75:
        $ temp_modifier += 5

    if action_context == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in Girl.Traits:
        $ temp_modifier += (3*Taboo)
    if Girl in Player.Harem or "sex friend" in Girl.Petnames:
        $ temp_modifier += 10
    elif "ex" in Girl.Traits:
        $ temp_modifier -= 40
    if Girl.ForcedCount and not Girl.Forced:
        $ temp_modifier -= 5 * Girl.ForcedCount

    if Taboo and "tabno" in Girl.daily_history:
        $ temp_modifier -= 10

    if "no foot" in Girl.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no foot" in Girl.recent_history else 0

    $ Approval = ApprovalCheck(Girl, 1250, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if action_context == Girl:                                                                  #Storm auto-starts
        if Approval > 2:                                                      # fix, add emma auto stuff here
            if offhand_action == "jackin":
                "[Girl.name] lays back and starts rubbing her feet along your cock."
            else:
                "[Girl.name] gives you a mischevious smile, and starts to rub her feet along your cock."
            menu:
                "What do you do?"
                "Nothing.":
                    $ Girl.change_stat("inhibition", 70, 3)
                    $ Girl.change_stat("inhibition", 30, 2)
                    "[Girl.name] continues her actions."
                "Praise her.":
                    $ Girl.change_face("sexy", 1)
                    $ Girl.change_stat("inhibition", 70, 3)
                    ch_p "Oooh, that's good, [Girl.Pet]."
                    $ Girl.nameCheck() #checks reaction to petname
                    "[Girl.name] continues her actions."
                    $ Girl.change_stat("love", 80, 1)
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ Girl.change_face("surprised")
                    $ Girl.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that for now, [Girl.Pet]."
                    $ Girl.nameCheck() #checks reaction to petname
                    "[Girl.name] puts it down."
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Girl.change_stat("obedience", 30, 2)
                    return
            if primary_action:
                $ girl_offhand_action = "foot"
                return
            jump Storm_FJ_Prep
        else:
            $ temp_modifier = 0                               # fix, add emma auto stuff here
            $ offhand_action = 0
            return

    if not Girl.Foot and "no foot" not in Girl.recent_history:
        $ Girl.change_face("confused", 2)
        ch_s "Oh, you would like me to use my feet, [Girl.Petname]?"
        $ Girl.Blush = 1

    if not Girl.Foot and Approval:                                                 #First time dialog
        if Girl.Forced:
            $ Girl.change_face("sad",1)
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
        elif Girl.love >= (Girl.obedience + Girl.inhibition):
            $ Girl.change_face("sexy",1)
            $ Girl.Brows = "sad"
            $ Girl.Mouth = "smile"
            ch_s "I could enjoy that. . ."
        elif Girl.obedience >= Girl.inhibition:
            $ Girl.change_face("normal",1)
            ch_s "If you enjoy that, [Girl.Petname]. . ."
        elif Girl.Addict >= 50:
            $ Girl.change_face("manic", 1)
            ch_s "Very well. . ."
        else: # Uninhibited
            $ Girl.change_face("lipbite",1)
            ch_s "Very well. . ."

    elif Approval:                                                                       #Second time+ dialog
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
            ch_s "That is all you want?"
        elif not Taboo and "tabno" in Girl.daily_history:
            ch_s "I suppose this is secluded enough. . ."
        elif "foot" in Girl.recent_history:
            $ Girl.change_face("sexy", 1)
            ch_s "I suppose so. . ."
            jump Storm_FJ_Prep
        elif "foot" in Girl.daily_history:
            $ Girl.change_face("sexy", 1)
            $ line = renpy.random.choice(["Another?",
                "You did not get enough earlier?",
                "My feet are rather sore from earlier.",
                "My feet are rather sore from earlier."])
            ch_s "[line]"
        elif Girl.Foot < 3:
            $ Girl.change_face("sexy", 1)
            $ Girl.Brows = "confused"
            $ Girl.Mouth = "kiss"
            ch_s "Oh, very well. . ."
        else:
            $ Girl.change_face("sexy", 1)
            $ Girl.ArmPose = 2
            $ line = renpy.random.choice(["You would like me to use my feet again?",
                "So you would like another footjob?",
                "Mmmm, some. . . [she rubs her foot along your leg]?",
                "A little foot rub?"])
            ch_s "[line]"
        $ line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 60, 1)
            ch_s "I supose that would be fine."
        elif "no foot" in Girl.daily_history:
            ch_s "Oh, very well."
        else:
            $ Girl.change_face("sexy", 1)
            $ Girl.change_stat("love", 90, 1)
            $ Girl.change_stat("inhibition", 50, 3)
            $ line = renpy.random.choice(["Hmm, I suppose.",
                "Fine.",
                "Very well, bring it out.",
                "I suppose that I could. . .",
                "Fine. . . [She gestures for you to come over].",
                "Hmm, ok."])
            ch_s "[line]"
            $ line = 0
        $ Girl.change_stat("obedience", 20, 1)
        $ Girl.change_stat("obedience", 60, 1)
        $ Girl.change_stat("inhibition", 70, 2)
        jump Storm_FJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ Girl.change_face("angry")
        if "no foot" in Girl.recent_history:
            ch_s "I have made myself clear, [Girl.Petname]."
        elif Taboo and "tabno" in Girl.daily_history and "no foot" in Girl.daily_history:
            ch_s "I refuse to do this in public."
        elif "no foot" in Girl.daily_history:
            ch_s "I said \"no,\" [Girl.Petname]."
        elif Taboo and "tabno" in Girl.daily_history:
            ch_s "I informed you, not in public!"
        elif not Girl.Foot:
            $ Girl.change_face("bemused")
            ch_s "I am unsure, [Girl.Petname]. . ."
        else:
            $ Girl.change_face("bemused")
            ch_s "Not now, [Girl.Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no foot" in Girl.daily_history:
                $ Girl.change_face("bemused")
                ch_s "Thank you."
                return
            "Maybe later?" if "no foot" not in Girl.daily_history:
                $ Girl.change_face("sexy")
                ch_s ". . ."
                ch_s "Perhaps."
                $ Girl.change_stat("love", 80, 2)
                $ Girl.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ Girl.recent_history.append("tabno")
                    $ Girl.daily_history.append("tabno")
                $ Girl.recent_history.append("no foot")
                $ Girl.daily_history.append("no foot")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ Girl.change_face("sexy")
                    $ Girl.change_stat("obedience", 90, 2)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("inhibition", 70, 3)
                    $ Girl.change_stat("inhibition", 40, 2)
                    $ line = renpy.random.choice(["Hmm, I suppose.",
                            "Fine.",
                            "Very well, bring it out.",
                            "I suppose that I could. . .",
                            "Fine. . . [She gestures for you to come over].",
                            "Hmm, ok."])
                    ch_s "[line]"
                    $ line = 0
                    jump Storm_FJ_Prep
                else:
                    pass

            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck(Girl, 400, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and Girl.Forced):
                    $ Girl.change_face("sad")
                    $ Girl.change_stat("love", 70, -5, 1)
                    $ Girl.change_stat("love", 200, -2)

                    $ Girl.change_stat("obedience", 50, 4)
                    $ Girl.change_stat("inhibition", 80, 1)
                    $ Girl.change_stat("inhibition", 60, 3)
                    $ Girl.Forced = 1
                    jump Storm_FJ_Prep
                else:
                    $ Girl.change_stat("love", 200, -15)
                    $ Girl.recent_history.append("angry")
                    $ Girl.daily_history.append("angry")

    #She refused all offers.
    $ Girl.ArmPose = 1
    if "no foot" in Girl.daily_history:
        $ Girl.change_face("angry", 1)

        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
    elif Girl.Forced:
        $ Girl.change_face("angry", 1)
        ch_s "Do not tempt me to show you what my feet can do."
        $ Girl.change_stat("lust", 200, 5)
        if Girl.love > 300:
                $ Girl.change_stat("love", 70, -2)
        $ Girl.change_stat("obedience", 50, -2)
        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ Girl.change_face("angry", 1)
        $ Girl.daily_history.append("tabno")
        ch_s "This truly is not an appropriate place for that."
        $ Girl.change_stat("lust", 200, 5)
        $ Girl.change_stat("obedience", 50, -3)
    elif Girl.Foot:
        $ Girl.change_face("sad")
        ch_s "I am in no mood, [Girl.Petname]. . ."
    else:
        $ Girl.change_face("normal", 1)
        ch_s "I am truly in no mood for footplay today. . ."
    $ Girl.recent_history.append("no foot")
    $ Girl.daily_history.append("no foot")
    $ temp_modifier = 0
    return


label Storm_FJ_Prep:
    if offhand_action == "foot":
        return

    if Taboo:
        $ Girl.inhibition += int(Taboo/10)
        $ Girl.lust += int(Taboo/5)

    $ Girl.change_face("sexy")
    if Girl.Forced:
        $ Girl.change_face("sad")
    elif not Girl.Foot:
        $ Girl.Brows = "confused"
        $ Girl.Eyes = "sexy"
        $ Girl.Mouth = "smile"

    call Seen_First_Peen(Girl,Partner,React=action_context)
    if not Girl.Foot:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -20)
            $ Girl.change_stat("obedience", 70, 25)
            $ Girl.change_stat("inhibition", 80, 30)
        else:
            $ Girl.change_stat("love", 90, 5)
            $ Girl.change_stat("obedience", 70, 20)
            $ Girl.change_stat("inhibition", 80, 20)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ line = 0
    $ counter = 0
    if Taboo:
        $ Girl.DrainWord("tabno")
    $ Girl.DrainWord("no foot")
    $ Girl.recent_history.append("foot")
    $ Girl.daily_history.append("foot")

label Storm_FJ_Cycle:
    while Round > 0:
        call Shift_Focus(Girl)
        call Storm_Sex_Launch("foot")
        $ Girl.lustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if action_speed:
                                    pass

                        "Start moving? . ." if not action_speed:
                                    $ action_speed = 1

                        "action_speed up. . ." if action_speed < 2:
                                    $ action_speed = 2
                                    "You ask her to up the pace a bit."
                        "action_speed up. . . (locked)" if action_speed >= 2:
                                    pass

                        "Slow Down. . ." if action_speed:
                                    $ action_speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not action_speed:
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
                                    "I also want to fondle her thighs." if offhand_action != "fondle thighs":
                                            if MultiAction:
                                                $ offhand_action = "fondle thighs"
                                                "You start to fondle her thighs."
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Shift primary action":
                                            if Girl.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                $ action_context = "shift"
                                                                call Storm_FJ_After
                                                                call Storm_Blowjob
                                                        "How about a handjob?":
                                                                $ action_context = "shift"
                                                                call Storm_FJ_After
                                                                call Storm_Handjob
                                                        "How about a titjob?":
                                                                $ action_context = "shift"
                                                                call Storm_FJ_After
                                                                call Storm_Titjob

                                                        "Never Mind":
                                                                jump Storm_FJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [Girl.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(Girl)
                                            "Asks [Girl.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(Girl)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(Girl)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Storm_FJ_Cycle
                                            "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Storm_FJ_Cycle
                                            "Never mind":
                                                        jump Storm_FJ_Cycle
                                    "Undress [Girl.name]":
                                            call Girl_Undress(Girl)
                                    "Clean up [Girl.name] (locked)" if not Girl.Spunk:
                                            pass
                                    "Clean up [Girl.name]" if Girl.Spunk:
                                            call Girl_Cleanup(Girl,"ask")
                                    "Never mind":
                                            jump Storm_FJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Storm_Sex_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Storm_FJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Storm_Sex_Reset
                                    $ line = 0
                                    jump Storm_FJ_After
        #End menu (if line)

        call Shift_Focus(Girl)
        call Sex_Dialog(Girl,Partner)

        #If either of you could cum

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or Girl.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(Girl)
                            if "angry" in Girl.recent_history:
                                call Storm_Sex_Reset
                                return
                            $ Girl.change_stat("lust", 200, 5)
                            if 100 > Girl.lust >= 70 and Girl.OCount < 2:
                                $ Girl.recent_history.append("unsatisfied")
                                $ Girl.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Storm_FJ_After
                            $ line = "came"

                    if Girl.lust >= 100:
                            #If [Girl.name] can cum
                            call Girl_Cumming(Girl)
                            if action_context == "shift" or "angry" in Girl.recent_history:
                                jump Storm_FJ_After

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in Girl.recent_history:#And [Girl.name] is unsatisfied,
                                    "[Girl.name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Storm_FJ_After
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if counter == 20:
                    $ Girl.Brows = "angry"
                    menu:
                        ch_s "Hmm, foot cramp. Could we take a short break?"
                        "How about a BJ?" if Girl.Action and MultiAction:
                                $ action_context = "shift"
                                call Storm_FJ_After
                                call Storm_Blowjob
                        "How about a Handy?" if Girl.Action and MultiAction:
                                $ action_context = "shift"
                                call Storm_FJ_After
                                call Storm_Handjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ counter += 1
                                "[line]"
                                jump Storm_FJ_Cycle
                        "Let's try something else." if MultiAction:
                                $ line = 0
                                call Storm_Sex_Reset
                                $ action_context = "shift"
                                jump Storm_FJ_After
                        "No, keep going.":
                                if ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "O"):
                                    $ Girl.change_stat("love", 200, -5)
                                    $ Girl.change_stat("obedience", 50, 3)
                                    $ Girl.change_stat("obedience", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    $ Girl.change_face("angry", 1)
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_s "I do have better things I could be doing."
                                    $ Girl.change_stat("love", 50, -3, 1)
                                    $ Girl.change_stat("love", 80, -4, 1)
                                    $ Girl.change_stat("obedience", 30, -1, 1)
                                    $ Girl.change_stat("obedience", 50, -1, 1)
                                    $ Girl.recent_history.append("angry")
                                    $ Girl.daily_history.append("angry")
                                    jump Storm_FJ_After
        elif counter == 10 and Girl.SEXP <= 100 and not ApprovalCheck(Girl, 1200, "LO"):
                    $ Girl.Brows = "confused"
                    ch_s "Could we be done here, my feet are getting sore."
        #End Count check

        call Escalation(Girl) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(Girl,10) #"It is getting late, [Girl.Petname]. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(Girl,5)   #"We should take a break soon."

    #Round = 0 loop breaks
    $ Girl.change_face("bemused", 0)
    $ line = 0
    call Sex_Basic_Dialog(Girl,"done") # ch_s "I need to take a moment to collect myself."

label Storm_FJ_After:
    $ Girl.change_face("sexy")

    $ Girl.Foot += 1
    $ Girl.Action -=1
    $ Girl.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ Girl.Addictionrate += 1
    $ Girl.change_stat("lust", 90, 5)

    call Partner_Like(Girl,1)

    if "Stormpedi" in Achievements:
            pass
    elif Girl.Foot >= 10:
            $ Girl.change_face("smile", 1)
            ch_s "I am glad that you convinced me to try this."
            ch_s "It feels so. . . intimate."
            $ Achievements.append("Stormpedi")
            $ Girl.SEXP += 5
    elif Girl.Foot == 1:
            $ Girl.SEXP += 10
            if Girl.love >= 500:
                $ Girl.Mouth = "smile"
                ch_s "That certainly was an interesting experience. . ."
            elif Player.Focus <= 20:
                $ Girl.Mouth = "sad"
                ch_s "Did you enjoy that?"
    elif Girl.Foot == 5:
                ch_s "I'm enjoying this experience."

    $ temp_modifier = 0
    if action_context == "shift":
        ch_s "Ok then, what were you thinking?"
    else:
        call Storm_Sex_Reset
    call Checkout
    return

## end Girl.Footjob //////////////////////////////////////////////////////////////////////
