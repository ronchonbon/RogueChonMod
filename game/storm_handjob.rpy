
label Storm_Handjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (StormX)
    if StormX.action_counter["handjob"] >= 7:
        $ approval_bonus += 10
    elif StormX.action_counter["handjob"] >= 3:
        $ approval_bonus += 7
    elif StormX.action_counter["handjob"]:
        $ approval_bonus += 3

    if StormX.addiction >= 75 and StormX.event_counter["swallowed"] >=3:
        $ approval_bonus += 15
    if StormX.addiction >= 75:
        $ approval_bonus += 5

    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in StormX.Traits:
        $ approval_bonus += (3*Taboo)
    if StormX in Player.Harem or "sex friend" in StormX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in StormX.Traits:
        $ approval_bonus -= 40
    if StormX.event_counter["forced"] and not StormX.Forced:
        $ approval_bonus -= 5*StormX.event_counter["forced"]

    if Taboo and "no_taboo" in StormX.daily_history:
        $ approval_bonus -= 10

    if "no_handjob" in StormX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_handjob" in StormX.recent_history else 0

    $ Approval = ApprovalCheck(StormX, 1100, TabM = 3)

    if not StormX.action_counter["handjob"] and "no_handjob" not in StormX.recent_history:
        $ StormX.change_face("sly", 2)
        ch_s "You would like me to jerk you off?"

    if not StormX.action_counter["handjob"] and Approval:
        if StormX.Forced:
            $ StormX.change_face("sad",1)
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
        elif StormX.love >= (StormX.obedience + StormX.inhibition):
            $ StormX.change_face("sexy",1)
            $ StormX.brows = "sad"
            $ StormX.mouth = "smile"
            ch_s "I might enjoy that. . ."
        elif StormX.obedience >= StormX.inhibition:
            $ StormX.change_face("normal",1)
            ch_s "If that is what you want, [StormX.player_petname]. . ."
        elif StormX.addiction >= 50:
            $ StormX.change_face("manic", 1)
            ch_s "Mmmmmmmm. . ."
        else:
            $ StormX.change_face("lipbite",1,Eyes="side")
            ch_s "I suppose. . ."

    elif Approval:
        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
            ch_s "Nothing more than that?"
        elif not Taboo and "no_taboo" in StormX.daily_history:
            ch_s "Here, hmm?. . ."
        elif "handjob" in StormX.recent_history:
            $ StormX.change_face("sexy", 1)
            ch_s "I do not know if I have it in me. . ."
            jump Storm_HJ_Prep
        elif "handjob" in StormX.daily_history:
            $ StormX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Another?",   
                "My arm will wear out.", 
                "You did not get enough earlier?",
                "My hand is quite sore from earlier.",
                "My hand is rather sore from before."])
            ch_s "[Line]"
        elif StormX.action_counter["handjob"] < 3:
            $ StormX.change_face("sly", 1)
            ch_s "You enjoyed it last time?. . ."
        else:
            $ StormX.change_face("sexy", 1)
            $ StormX.ArmPose = 2
            $ Line = renpy.random.choice(["You want more?",                 
                "So you would like another?",                 
                "More of this? [fist pumping hand gestures]", 
                "Oh, did you want some attention?"])
            ch_s "[Line]"
        $ Line = 0

    if Approval >= 2:
        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("obedience", 90, 1)
            $ StormX.change_stat("inhibition", 60, 1)
            ch_s "Fine, we can do this."
        elif "no_handjob" in StormX.daily_history:
            ch_s "Oh, very well. . ."
        else:
            $ StormX.change_face("sexy", 1)
            $ StormX.change_stat("love", 90, 1)
            $ StormX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Oh, I suppose we might.",                 
                "I would do this.",                 
                "Very well, give it here.", 
                "I suppose that I could. . .",
                ". . .Fine.[She gestures for you to come over]",
                "Ok, ok."])
            ch_s "[Line]"
            $ Line = 0
        $ StormX.change_stat("obedience", 20, 1)
        $ StormX.change_stat("obedience", 60, 1)
        $ StormX.change_stat("inhibition", 70, 2)
        jump Storm_HJ_Prep
    else:

        $ StormX.change_face("angry")
        if "no_handjob" in StormX.daily_history:
            ch_s "You will need to accept a \"no\", [StormX.player_petname]."
        elif Taboo and "no_taboo" in StormX.daily_history:
            ch_s "I was very clear, this is too public."
        elif not StormX.action_counter["handjob"]:
            $ StormX.change_face("bemused")
            ch_s "Are you certain, [StormX.player_petname]? . ."
        else:
            $ StormX.change_face("bemused")
            ch_s "I would rather not right now though."
        menu:
            extend ""
            "Sorry, never mind." if "no_handjob" in StormX.daily_history:
                $ StormX.change_face("bemused")
                ch_s "I understand."
                return
            "Maybe later?" if "no_handjob" not in StormX.daily_history:
                $ StormX.change_face("sexy")
                ch_s ". . ."
                ch_s "Perhaps. . ."
                $ StormX.change_stat("love", 80, 2)
                $ StormX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ StormX.recent_history.append("no_taboo")
                    $ StormX.daily_history.append("no_taboo")
                $ StormX.recent_history.append("no_handjob")
                $ StormX.daily_history.append("no_handjob")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ StormX.change_face("sexy")
                    $ StormX.change_stat("obedience", 90, 2)
                    $ StormX.change_stat("obedience", 50, 2)
                    $ StormX.change_stat("inhibition", 70, 3)
                    $ StormX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Oh, I suppose we might.",                 
                        "I would do this.",                 
                        "Very well, give it here.", 
                        "I suppose that I could. . .",
                        ". . .Fine.[She gestures for you to come over]",
                        "Ok, ok."])
                    ch_s "[Line]"
                    $ Line = 0
                    jump Storm_HJ_Prep
            "Come on, get to work.":

                $ Approval = ApprovalCheck(StormX, 350, "OI", TabM = 3)
                if Approval > 1 or (Approval and StormX.Forced):
                    $ StormX.change_face("angry")
                    $ StormX.change_stat("love", 70, -5, 1)
                    $ StormX.change_stat("love", 200, -2)
                    ch_s ". . . fine."
                    $ StormX.change_stat("obedience", 50, 4)
                    $ StormX.change_stat("inhibition", 80, 1)
                    $ StormX.change_stat("inhibition", 60, 3)
                    $ StormX.Forced = 1
                    jump Storm_HJ_Prep
                else:
                    $ StormX.change_stat("love", 200, -15)
                    $ StormX.recent_history.append("angry")
                    $ StormX.daily_history.append("angry")


    $ StormX.ArmPose = 1
    if "no_handjob" in StormX.daily_history:
        $ StormX.change_face("angry", 1)
        ch_s "Do not make me repeat myself."
        $ StormX.recent_history.append("angry")
        $ StormX.daily_history.append("angry")
    elif StormX.Forced:
        $ StormX.change_face("angry", 1)
        ch_s "I am not comfortable with that."
        $ StormX.change_stat("lust", 200, 5)
        if StormX.love > 300:
            $ StormX.change_stat("love", 70, -2)
        $ StormX.change_stat("obedience", 50, -2)
        $ StormX.recent_history.append("angry")
        $ StormX.daily_history.append("angry")
    elif Taboo:
        $ StormX.change_face("angry", 1)
        $ StormX.daily_history.append("no_taboo")
        ch_s "I could not possibly do that here."
        $ StormX.change_stat("lust", 200, 5)
        $ StormX.change_stat("obedience", 50, -3)
    elif StormX.action_counter["handjob"]:
        $ StormX.change_face("sad")
        ch_s ". . . I would rather not."
    else:
        $ StormX.change_face("normal", 1)
        ch_s "No, I do not think so, [StormX.player_petname]."
    $ StormX.recent_history.append("no_handjob")
    $ StormX.daily_history.append("no_handjob")
    $ approval_bonus = 0
    return


label Storm_HJ_Prep:
    if offhand_action == "handjob":
        return

    if Taboo:
        $ StormX.inhibition += int(Taboo/10)
        $ StormX.lust += int(Taboo/5)

    $ StormX.change_face("sexy")
    if StormX.Forced:
        $ StormX.change_face("sad")
    elif not StormX.action_counter["handjob"]:
        $ StormX.brows = "confused"
        $ StormX.eyes = "sexy"
        $ StormX.mouth = "smile"

    call Seen_First_Peen (StormX, Partner, React=action_context)
    call Storm_HJ_Launch ("L")

    if action_context == StormX:

        $ action_context = 0
        if offhand_action == "jackin":
            "[StormX.name] brushes your hand aside and starts stroking your cock."
        else:
            "[StormX.name] draws her fingers across your cock, and begins to stroke it."
        menu:
            "What do you do?"
            "Nothing.":
                $ StormX.change_stat("inhibition", 70, 3)
                $ StormX.change_stat("inhibition", 30, 2)
                "[StormX.name] continues her actions."
            "Praise her.":
                $ StormX.change_face("sexy", 1)
                $ StormX.change_stat("inhibition", 70, 3)
                ch_p "Oooh, that's good, [StormX.petname]."
                $ StormX.nameCheck()
                "[StormX.name] continues her actions."
                $ StormX.change_stat("love", 80, 1)
                $ StormX.change_stat("obedience", 90, 1)
                $ StormX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ StormX.change_face("surprised")
                $ StormX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that for now, [StormX.petname]."
                $ StormX.nameCheck()
                "[StormX.name] puts it down."
                $ StormX.change_stat("obedience", 90, 1)
                $ StormX.change_stat("obedience", 50, 1)
                $ StormX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ StormX.AddWord(1,"refused","refused")
                return

    if not StormX.action_counter["handjob"]:
        if StormX.Forced:
            $ StormX.change_stat("love", 90, -20)
            $ StormX.change_stat("obedience", 70, 25)
            $ StormX.change_stat("inhibition", 80, 30)
        else:
            $ StormX.change_stat("love", 90, 5)
            $ StormX.change_stat("obedience", 70, 20)
            $ StormX.change_stat("inhibition", 80, 20)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ StormX.DrainWord("no_taboo")
    $ StormX.DrainWord("no_handjob")
    $ StormX.recent_history.append("handjob")
    $ StormX.daily_history.append("handjob")

label Storm_HJ_Cycle:
    while Round > 0:
        call shift_focus (StormX)
        call Storm_HJ_Launch
        $ StormX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . ." if action_speed:
                    pass

                "Start moving? . ." if not action_speed:
                    $ action_speed = 1

                "Speed up. . ." if action_speed < 2:
                    $ action_speed = 2
                    "You ask her to up the pace a bit."
                "Speed up. . . (locked)" if action_speed >= 2:
                    pass

                "Slow Down. . ." if action_speed:
                    $ action_speed -= 1
                    "You ask her to slow it down a bit."
                "Slow Down. . . (locked)" if not action_speed:
                    pass
                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "Other options":

                    menu:
                        "I also want to fondle her breasts." if offhand_action != "fondle_breasts":
                            if StormX.remaining_actions and multi_action:
                                $ offhand_action = "fondle_breasts"
                                "You start to fondle her breasts."
                                $ StormX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (StormX, "tired")
                        "Shift primary action":

                            if StormX.remaining_actions and multi_action:
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
                                call Sex_Basic_Dialog (StormX, "tired")

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Asks [StormX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (StormX)
                                "Asks [StormX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (StormX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (StormX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Storm_HJ_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Storm_HJ_Cycle
                                "Never mind":
                                    jump Storm_HJ_Cycle
                        "Undress [StormX.name]":
                            call Girl_Undress (StormX)
                        "Clean up [StormX.name] (locked)" if not StormX.Spunk:
                            pass
                        "Clean up [StormX.name]" if StormX.Spunk:
                            call Girl_Cleanup (StormX, "ask")
                        "Never mind":
                            jump Storm_HJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Storm_HJ_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Storm_HJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Storm_HJ_Reset
                    $ Line = 0
                    jump Storm_HJ_After


        call shift_focus (StormX)
        call Sex_Dialog (StormX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or StormX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (StormX)
                if "angry" in StormX.recent_history:
                    call Storm_HJ_Reset
                    return
                $ StormX.change_stat("lust", 200, 5)
                if 100 > StormX.lust >= 70 and StormX.session_orgasms < 2 and StormX.SEXP >= 20:
                    $ StormX.recent_history.append("unsatisfied")
                    $ StormX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Storm_HJ_After
                $ Line = "came"

            if StormX.lust >= 100:

                call Girl_Cumming (StormX)
                if action_context == "shift" or "angry" in StormX.recent_history:
                    jump Storm_HJ_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in StormX.recent_history:
                    "[StormX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Storm_HJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if counter == 20:
            $ StormX.brows = "angry"
            ch_s "Hmm, I am developing a hand cramp here."
            menu:
                ch_s "Mind if we take a break?"
                "How about a BJ?" if StormX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Storm_HJ_After
                    call Storm_Blowjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    $ counter += 1
                    "[Line]"
                    jump Storm_HJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Storm_HJ_Reset
                    $ action_context = "shift"
                    jump Storm_HJ_After
                "No, get back down there.":
                    if ApprovalCheck(StormX, 1200) or ApprovalCheck(StormX, 500, "O"):
                        $ StormX.change_stat("love", 200, -5)
                        $ StormX.change_stat("obedience", 50, 3)
                        $ StormX.change_stat("obedience", 80, 2)
                        "She scowls but gets back to work."
                    else:
                        $ StormX.change_face("angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        ch_s "Perhaps some time alone would help you better evaluate your choices."
                        $ StormX.change_stat("love", 50, -3, 1)
                        $ StormX.change_stat("love", 80, -4, 1)
                        $ StormX.change_stat("obedience", 30, -1, 1)
                        $ StormX.change_stat("obedience", 50, -1, 1)
                        $ StormX.recent_history.append("angry")
                        $ StormX.daily_history.append("angry")
                        jump Storm_HJ_After
        elif counter == 10 and StormX.SEXP <= 100 and not ApprovalCheck(StormX, 1200, "LO"):
            $ StormX.brows = "confused"
            ch_s "Are you certain you didn't have anything else in mind?"


        call Escalation (StormX)

        if Round == 10:
            call Sex_Basic_Dialog (StormX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (StormX, 5)


    $ StormX.change_face("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (StormX, "done")

label Storm_HJ_After:
    $ StormX.change_face("sexy")

    $ StormX.action_counter["handjob"] += 1
    $ StormX.remaining_actions -=1
    $ StormX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ StormX.addiction_rate += 1
    $ StormX.change_stat("lust", 90, 5)

    call Partner_Like (StormX, 1)

    if "Storm Handi-Queen" in Achievements:
        pass
    elif StormX.action_counter["handjob"] >= 10:
        $ StormX.change_face("smile", 1)
        ch_s "I seem to have become the \"queen\" of good handjobs."
        $ Achievements.append("Storm Handi-Queen")
        $ StormX.SEXP += 5
    elif StormX.action_counter["handjob"] == 1:
        $ StormX.SEXP += 10
        if not StormX.Forced:
            $ StormX.mouth = "smile"
            ch_s "That was more enjoyable than I had expected. . ."
        elif Player.focus <= 20:
            $ StormX.mouth = "sad"
            ch_s "Did that satisfy you?"
    elif StormX.action_counter["handjob"] == 5:
        ch_s "I have gotten used to these. . ."

    $ approval_bonus = 0
    if action_context == "shift":
        ch_s "Very well, what did you want to do?"
    else:
        call Storm_HJ_Reset
    call Checkout
    return







label Storm_Titjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (StormX)
    if StormX.action_counter["titjob"] >= 7:
        $ approval_bonus += 10
    elif StormX.action_counter["titjob"] >= 3:
        $ approval_bonus += 7
    elif StormX.action_counter["titjob"]:
        $ approval_bonus += 5

    if StormX.addiction >= 75 and StormX.event_counter["swallowed"] >=3:
        $ approval_bonus += 15
    elif StormX.addiction >= 75:
        $ approval_bonus += 5

    if StormX.SeenChest and ApprovalCheck(StormX, 500):
        $ approval_bonus += 10
    if not StormX.bra and not StormX.top:
        $ approval_bonus += 10
    if StormX.lust > 75:
        $ approval_bonus += 10
    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in StormX.Traits:
        $ approval_bonus += (5*Taboo)
    if StormX in Player.Harem or "sex friend" in StormX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in StormX.Traits:
        $ approval_bonus -= 30
    if StormX.event_counter["forced"] and not StormX.Forced:
        $ approval_bonus -= 5*StormX.event_counter["forced"]

    if Taboo and "no_taboo" in StormX.daily_history:
        $ approval_bonus -= 10

    if "no_titjob" in StormX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_titjob" in StormX.recent_history else 0

    $ Approval = ApprovalCheck(StormX, 1200, TabM = 5)

    if not StormX.action_counter["titjob"] and "no_titjob" not in StormX.recent_history:
        $ StormX.change_face("surprised", 1)
        $ StormX.mouth = "kiss"
        ch_s "My breasts are really appealing to you, [StormX.player_petname]?"

    if not StormX.action_counter["titjob"] and Approval:

        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
        elif StormX.love >= (StormX.obedience + StormX.inhibition):
            $ StormX.change_face("sexy")
            $ StormX.brows = "sad"
            $ StormX.mouth = "smile"
            ch_s "I suppose you've earned something special. . ."
        elif StormX.obedience >= StormX.inhibition:
            $ StormX.change_face("normal")
            ch_s "If that is what you want. . ."
        elif StormX.addiction >= 50:
            $ StormX.change_face("manic", 1)
            ch_s "Hmmmm. . . ."
        else:
            $ StormX.change_face("sad")
            $ StormX.mouth = "smile"
            ch_s "Hmm, I was expecting you to ask. . ."

    elif Approval:

        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
            ch_s "You enjoy making use of these?"
        elif not Taboo and "no_taboo" in StormX.daily_history:
            ch_s "I suppose this is secluded enough. . ."
        elif "titjob" in StormX.recent_history:
            $ StormX.change_face("sexy", 1)
            ch_s "You cannot get enough?"
            jump Storm_TJ_Prep
        elif "titjob" in StormX.daily_history:
            $ StormX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",   
                "You will wear them out like this.", 
                "You did not get enough earlier?",
                "I am still a bit sore from earlier."])
            ch_s "[Line]"
        elif StormX.action_counter["titjob"] < 3:
            $ StormX.change_face("sly", 1)
            ch_s "Hmm, another titjob?"
        else:
            $ StormX.change_face("sexy", 1)
            $ StormX.ArmPose = 2
            $ Line = renpy.random.choice(["You wish to use these? [jiggles her tits]",                 
                "So you would like another titjob?",                 
                ". . . [bounces tits]?", 
                "You would like to give it a hug?"])
            ch_s "[Line]"
        $ Line = 0

    if Approval >= 2:
        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("obedience", 90, 1)
            $ StormX.change_stat("inhibition", 60, 1)
            ch_s "I suppose this would not be too unpleasant. . ."
        elif "no_titjob" in StormX.daily_history:
            ch_s "Very well then. . ."
        else:
            $ StormX.change_face("sexy", 1)
            $ StormX.change_stat("love", 90, 1)
            $ StormX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Fine, come over here.",                 
                "Oh, very well.",                 
                "Mmmmm.", 
                "Fine, show me.",
                "Fine. . . [She drools a bit into her cleavage].",
                "Oh, all right."])
            ch_s "[Line]"
            $ Line = 0
        $ StormX.change_stat("obedience", 20, 1)
        $ StormX.change_stat("obedience", 70, 1)
        $ StormX.change_stat("inhibition", 80, 2)
        jump Storm_TJ_Prep
    else:

        $ StormX.change_face("angry")
        if "no_titjob" in StormX.daily_history:
            ch_s "You will need to accept a \"no\", [StormX.player_petname]."
        elif Taboo and "no_taboo" in StormX.daily_history and "no_titjob" in StormX.daily_history:
            ch_s "This is not an appropriate location for that. !"
        elif "no_titjob" in StormX.daily_history:
            ch_s "I already refused, [StormX.player_petname]."
        elif Taboo and "no_taboo" in StormX.daily_history:
            ch_s "This is not an appropriate place for that."
        else:
            $ StormX.change_face("bemused")
            ch_s "Perhaps later, [StormX.player_petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_titjob" in StormX.daily_history:
                $ StormX.change_face("bemused")
                ch_s "That is fine, [StormX.player_petname]."
                return
            "Maybe later?" if "no_titjob" not in StormX.daily_history:
                $ StormX.change_face("sexy")
                ch_s "Perhaps."
                $ StormX.change_stat("love", 80, 2)
                $ StormX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ StormX.recent_history.append("no_taboo")
                    $ StormX.daily_history.append("no_taboo")
                $ StormX.recent_history.append("no_titjob")
                $ StormX.daily_history.append("no_titjob")
                return
            "I think this could be fun for both of us. . .":
                if Approval:
                    $ StormX.change_face("sexy")
                    $ StormX.change_stat("obedience", 80, 2)
                    $ StormX.change_stat("obedience", 40, 2)
                    $ StormX.change_stat("inhibition", 70, 3)
                    $ StormX.change_stat("inhibition", 40, 2)
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
                    $ Approval = ApprovalCheck(StormX, 1100, TabM = 3)
                    if Approval >= 2:
                        $ StormX.change_stat("inhibition", 80, 1)
                        $ StormX.change_stat("inhibition", 60, 3)
                        $ StormX.change_face("confused", 1)
                        if StormX.action_counter["blowjob"]:
                            ch_s "You seemed to enjoy blowjobs, would that work instead?"
                        else:
                            ch_s "Would you perhaps prefer a blowjob?"
                        menu:
                            extend ""
                            "Ok, get down there.":
                                $ StormX.change_stat("love", 80, 2)
                                $ StormX.change_stat("inhibition", 60, 1)
                                $ StormX.change_stat("obedience", 50, 1)
                                jump Storm_BJ_Prep
                            "Nah, it's all about dem titties.":
                                $ Line = "no_BJ"
                    if Approval:
                        $ StormX.change_stat("inhibition", 80, 1)
                        $ StormX.change_stat("inhibition", 60, 3)
                        $ StormX.change_face("confused", 1)
                        ch_s "Perhaps a handjob?"
                        menu:
                            ch_s "Perhaps a handjob?"
                            "Sure, that's fine.":
                                $ StormX.change_stat("love", 80, 2)
                                $ StormX.change_stat("inhibition", 60, 1)
                                $ StormX.change_stat("obedience", 50, 1)
                                jump Storm_HJ_Prep
                            "Seriously, titties." if Line == "no_BJ":
                                $ Line = 0
                            "Nah, it's all about dem titties." if Line != "no_BJ":
                                pass
                    $ StormX.change_stat("love", 200, -2)
                    ch_s "Well. That is unfortunate. . ."
                    $ StormX.change_stat("obedience", 70, 2)
            "Come on, let me fuck those titties, [StormX.petname]":


                $ StormX.nameCheck()
                $ Approval = ApprovalCheck(StormX, 700, "OI", TabM = 4)
                if Approval > 1 or (Approval and StormX.Forced):
                    $ StormX.change_face("sad")
                    $ StormX.change_stat("love", 70, -5, 1)
                    $ StormX.change_stat("love", 200, -2)
                    ch_s "Oh, very well."
                    $ StormX.change_stat("obedience", 50, 4)
                    $ StormX.change_stat("inhibition", 80, 1)
                    $ StormX.change_stat("inhibition", 60, 3)
                    $ StormX.Forced = 1
                    jump Storm_TJ_Prep
                else:
                    $ StormX.change_stat("love", 200, -15)
                    $ StormX.recent_history.append("angry")
                    $ StormX.daily_history.append("angry")


    if "no_titjob" in StormX.daily_history:
        $ StormX.change_face("angry", 1)
        ch_s "I have refused. Learnt o accept that."
        $ StormX.recent_history.append("angry")
        $ StormX.daily_history.append("angry")
    elif StormX.Forced:
        $ StormX.change_face("angry", 1)
        ch_s "I do not wish to do this."
        $ StormX.change_stat("lust", 200, 5)
        if StormX.love > 300:
            $ StormX.change_stat("love", 70, -2)
        $ StormX.change_stat("obedience", 50, -2)
        $ StormX.recent_history.append("angry")
        $ StormX.daily_history.append("angry")
    elif Taboo:
        $ StormX.change_face("angry", 1)
        $ StormX.daily_history.append("no_taboo")
        ch_s "I do not wish to make a spectacle."
        $ StormX.change_stat("lust", 200, 5)
        $ StormX.change_stat("obedience", 50, -3)
    elif StormX.action_counter["titjob"]:
        $ StormX.change_face("sad")
        ch_s "Our time together was a memory."
    else:
        $ StormX.change_face("normal", 1)
        ch_s "I would rather not, [StormX.player_petname]."
    $ StormX.recent_history.append("no_titjob")
    $ StormX.daily_history.append("no_titjob")
    $ approval_bonus = 0
    return

label Storm_TJ_Prep:
    if Taboo:
        $ StormX.inhibition += int(Taboo/10)
        $ StormX.lust += int(Taboo/5)


    $ StormX.change_face("sexy")
    if StormX.Forced:
        $ StormX.change_face("sad")
    elif not StormX.action_counter["titjob"]:
        $ StormX.brows = "confused"
        $ StormX.eyes = "sexy"
        $ StormX.mouth = "smile"

    call Seen_First_Peen (StormX, Partner, React=action_context)
    call Storm_TJ_Launch ("L")

    if action_context == StormX:

        $ action_context = 0
        call Storm_TJ_Launch ("L")
        "[StormX.name] slides down and wraps her tits around your dick."
        menu:
            "What do you do?"
            "Nothing.":
                $ StormX.change_stat("inhibition", 80, 3)
                $ StormX.change_stat("inhibition", 40, 2)
                "[StormX.name] starts to slide them up and down."
            "Praise her.":
                $ StormX.change_face("sexy", 1)
                $ StormX.change_stat("inhibition", 80, 3)
                ch_p "Oh, that sounds like a good idea, [StormX.petname]."
                $ StormX.nameCheck()
                "[StormX.name] continues her actions."
                $ StormX.change_stat("love", 85, 1)
                $ StormX.change_stat("obedience", 90, 1)
                $ StormX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ StormX.change_face("confused")
                $ StormX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that for now, [StormX.petname]."
                $ StormX.nameCheck()
                "[StormX.name] lets it drop out from between her breasts."
                $ StormX.change_stat("obedience", 90, 1)
                $ StormX.change_stat("obedience", 50, 3)
                $ Player.recent_history.append("nope")
                $ StormX.AddWord(1,"refused","refused")
                return
    if not StormX.action_counter["titjob"]:
        if StormX.Forced:
            $ StormX.change_stat("love", 90, -25)
            $ StormX.change_stat("obedience", 70, 30)
            $ StormX.change_stat("inhibition", 80, 35)
        else:
            $ StormX.change_stat("love", 90, 5)
            $ StormX.change_stat("obedience", 70, 25)
            $ StormX.change_stat("inhibition", 80, 30)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ StormX.DrainWord("no_taboo")
    $ StormX.DrainWord("no_titjob")
    $ StormX.recent_history.append("titjob")
    $ StormX.daily_history.append("titjob")


label Storm_TJ_Cycle:
    while Round > 0:
        call shift_focus (StormX)
        call Storm_TJ_Launch
        $ StormX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . ." if action_speed:
                    pass

                "Start moving? . ." if action_speed == 0:
                    $ action_speed = 1

                "Speed up. . ." if action_speed == 1:
                    $ action_speed = 2
                    "You ask her to up the pace a bit."
                "Speed up. . . (locked)" if action_speed >= 2:
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
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "Other options":

                    menu:
                        "I also want to fondle her breasts." if offhand_action != "fondle_breasts":
                            if StormX.remaining_actions and multi_action:
                                $ offhand_action = "fondle_breasts"
                                "You start to fondle her breasts."
                                $ StormX.remaining_actions -= 1
                            else:
                                ch_s "I would prefer to finish this."
                        "Shift primary action":

                            if StormX.remaining_actions and multi_action:
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
                                call Sex_Basic_Dialog (StormX, "tired")

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Asks [StormX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (StormX)
                                "Asks [StormX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (StormX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (StormX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Storm_TJ_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Storm_TJ_Cycle
                                "Never mind":
                                    jump Storm_TJ_Cycle
                        "Undress [StormX.name]":
                            call Girl_Undress (StormX)
                        "Clean up [StormX.name] (locked)" if not StormX.Spunk:
                            pass
                        "Clean up [StormX.name]" if StormX.Spunk:
                            call Girl_Cleanup (StormX, "ask")
                        "Never mind":
                            jump Storm_TJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Storm_TJ_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Storm_TJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Storm_TJ_Reset
                    $ Line = 0
                    jump Storm_TJ_After


        call shift_focus (StormX)
        call Sex_Dialog (StormX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or StormX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (StormX)
                if "angry" in StormX.recent_history:
                    call Storm_TJ_Reset
                    return
                $ StormX.change_stat("lust", 200, 5)
                if 100 > StormX.lust >= 70 and StormX.session_orgasms < 2 and StormX.SEXP >= 20:
                    $ StormX.recent_history.append("unsatisfied")
                    $ StormX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Storm_TJ_After
                $ Line = "came"

            if StormX.lust >= 100:

                call Girl_Cumming (StormX)
                if action_context == "shift" or "angry" in StormX.recent_history:
                    jump Storm_TJ_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in StormX.recent_history:
                    "[StormX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Storm_TJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if StormX.SEXP >= 100 or ApprovalCheck(StormX, 1200, "LO"):
            pass
        elif counter == (5 + StormX.action_counter["titjob"]):
            $ StormX.brows = "confused"
            ch_s "Are you getting close? This is making me a bit sore. . ."
        elif counter == (10 + StormX.action_counter["titjob"]):
            $ StormX.brows = "angry"
            menu:
                ch_s "This is becoming uncomfortable, is there some way I could finish you off?"
                "How about a BJ?" if StormX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Storm_TJ_After
                    call Storm_Blowjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    jump Storm_TJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Storm_TJ_Reset
                    $ action_context = "shift"
                    jump Storm_TJ_After
                "No, get back down there.":
                    if ApprovalCheck(StormX, 1200) or ApprovalCheck(StormX, 500, "O"):
                        $ StormX.change_stat("love", 200, -5)
                        $ StormX.change_stat("obedience", 50, 3)
                        $ StormX.change_stat("obedience", 80, 2)
                        "She grumbles but gets back to work."
                    else:
                        $ StormX.change_face("angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        ch_s "Then I suppose you can handle this yourself."
                        $ StormX.change_stat("love", 50, -3, 1)
                        $ StormX.change_stat("love", 80, -4, 1)
                        $ StormX.change_stat("obedience", 30, -1, 1)
                        $ StormX.change_stat("obedience", 50, -1, 1)
                        $ StormX.recent_history.append("angry")
                        $ StormX.daily_history.append("angry")
                        jump Storm_TJ_After


        call Escalation (StormX)

        if Round == 10:
            call Sex_Basic_Dialog (StormX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (StormX, 5)


    $ StormX.change_face("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (StormX, "done")

label Storm_TJ_After:
    $ StormX.change_face("sexy")

    $ StormX.action_counter["titjob"] += 1
    $ StormX.remaining_actions -=1
    $ StormX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ StormX.addiction_rate += 1

    if Partner == "Kitty":
        call Partner_Like (StormX, 4, 2)
    else:
        call Partner_Like (StormX, 3)

    if StormX.action_counter["titjob"] > 5:
        pass
    elif StormX.action_counter["titjob"] == 1:
        $ StormX.SEXP += 12
        if StormX.love >= 500:
            $ StormX.mouth = "smile"
            ch_s "Mmm, I did quite enjoy that!"
        elif Player.focus <= 20:
            $ StormX.mouth = "sad"
            ch_s "I hope that met your standards."
    elif StormX.action_counter["titjob"] == 5:
        ch_s "You do seem to enjoy this."


    $ approval_bonus = 0
    if action_context == "shift":
        ch_s "Mmm, so what else did you have in mind?"
    else:
        call Storm_TJ_Reset
    call Checkout
    return






label Storm_Blowjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (StormX)
    if StormX.action_counter["blowjob"] >= 7:
        $ approval_bonus += 15
    elif StormX.action_counter["blowjob"] >= 3:
        $ approval_bonus += 10
    elif StormX.action_counter["blowjob"]:
        $ approval_bonus += 7

    if StormX.addiction >= 75 and StormX.event_counter["swallowed"] >=3:
        $ approval_bonus += 25
    elif StormX.addiction >= 75:
        $ approval_bonus += 15

    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in StormX.Traits:
        $ approval_bonus += (4*Taboo)
    if StormX in Player.Harem or "sex friend" in StormX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in StormX.Traits:
        $ approval_bonus -= 40
    if StormX.event_counter["forced"] and not StormX.Forced:
        $ approval_bonus -= 5*StormX.event_counter["forced"]

    if Taboo and "no_taboo" in StormX.daily_history:
        $ approval_bonus -= 10

    if "no_blowjob" in StormX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_blowjob" in StormX.recent_history else 0

    $ Approval = ApprovalCheck(StormX, 1300, TabM = 4)

    if not StormX.action_counter["blowjob"] and "no_blowjob" not in StormX.recent_history:
        $ StormX.change_face("sly")
        ch_s "You would like me to suck on your penis?"

    if not StormX.action_counter["blowjob"] and Approval:
        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
        elif StormX.love >= (StormX.obedience + StormX.inhibition):
            $ StormX.change_face("sexy")
            $ StormX.brows = "sad"
            $ StormX.mouth = "smile"
            ch_s "I have been curious. . ."
        elif StormX.obedience >= StormX.inhibition:
            $ StormX.change_face("normal")
            ch_s "If that is what you want. . ."
        elif StormX.addiction >= 50:
            $ StormX.change_face("manic", 1)
            ch_s "I might enjoy that. . ."
        else:
            $ StormX.change_face("sad")
            $ StormX.mouth = "smile"
            ch_s "I suppose. . ."
    elif Approval:
        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
            ch_s "Tsk, again?"
        elif not Taboo and "no_taboo" in StormX.daily_history:
            ch_s "Fine, I suppose this is secluded enough. . ."
        elif "blowjob" in StormX.recent_history:
            $ StormX.change_face("sexy", 1)
            ch_s "Mmm, again?"
            jump Storm_BJ_Prep
        elif "blowjob" in StormX.daily_history:
            $ StormX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Back so soon?",   
                "I must prepare myself.",
                "You did not get enough earlier?",
                "My jaw is still rather sore.",
                "My jaw is still recovering."])
            ch_s "[Line]"
        elif StormX.action_counter["blowjob"] < 3:
            $ StormX.change_face("sexy", 1)
            $ StormX.brows = "confused"
            $ StormX.mouth = "kiss"
            ch_s "Another blowjob?"
        else:
            $ StormX.change_face("sexy", 1)
            $ StormX.ArmPose = 2
            $ Line = renpy.random.choice([". . . [mimes blowing]?",                 
                "So you would like another blowjob?", 
                "You wish for me to suck you off?",
                "Are you asking if I am hungry?"])
            ch_s "[Line]"
        $ Line = 0

    if Approval >= 2:
        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("obedience", 90, 1)
            $ StormX.change_stat("inhibition", 60, 1)
            ch_s "Fine."
        elif "no_blowjob" in StormX.daily_history:
            ch_s "Fine, I suppose you have earned it. . ."
        else:
            $ StormX.change_face("sexy", 1)
            $ StormX.change_stat("love", 90, 1)
            $ StormX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice([". . . ok.",                 
                "Well. . . ok.",                 
                "Mmmm.", 
                "Sure, let me have it.",
                "Mmmm. . . [She licks her lips].",
                "Ok, fine."])
            ch_s "[Line]"
            $ Line = 0
        $ StormX.change_stat("obedience", 20, 1)
        $ StormX.change_stat("obedience", 70, 1)
        $ StormX.change_stat("inhibition", 80, 2)
        jump Storm_BJ_Prep
    else:

        $ StormX.change_face("angry")
        if "no_blowjob" in StormX.daily_history:
            ch_s "You will need to accept a \"no\", [StormX.player_petname]."
        elif Taboo and "no_taboo" in StormX.daily_history and "no_blowjob" in StormX.daily_history:
            ch_s "I told you, this is too public!"
        elif "no_blowjob" in StormX.daily_history:
            ch_s "I told you \"no,\" [StormX.player_petname]."
        elif Taboo and "no_taboo" in StormX.daily_history:
            ch_s "I told you this is too public!"
        elif not StormX.action_counter["blowjob"]:
            $ StormX.change_face("bemused")
            ch_s "I am not sure I would enjoy this, [StormX.player_petname]. . ."
        else:
            $ StormX.change_face("bemused")
            ch_s "Perhaps later, [StormX.player_petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no_blowjob" in StormX.daily_history:
                $ StormX.change_face("bemused")
                ch_s "It is fine, [StormX.player_petname]."
                return
            "Maybe later?" if "no_blowjob" not in StormX.daily_history:
                $ StormX.change_face("sexy")
                ch_s "I would not rule it out, [StormX.player_petname]."
                $ StormX.change_stat("love", 80, 2)
                $ StormX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ StormX.recent_history.append("no_taboo")
                    $ StormX.daily_history.append("no_taboo")
                $ StormX.recent_history.append("no_blowjob")
                $ StormX.daily_history.append("no_blowjob")
                return
            "Come on, please?":
                if Approval:
                    $ StormX.change_face("sexy")
                    $ StormX.change_stat("obedience", 90, 2)
                    $ StormX.change_stat("obedience", 50, 2)
                    $ StormX.change_stat("inhibition", 70, 3)
                    $ StormX.change_stat("inhibition", 40, 2)
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
                    if ApprovalCheck(StormX, 1100, TabM = 3):
                        $ StormX.change_stat("inhibition", 80, 1)
                        $ StormX.change_stat("inhibition", 60, 3)
                        $ StormX.change_face("confused", 1)
                        $ StormX.ArmPose = 2
                        if StormX.action_counter["handjob"]:
                            ch_s "I could just stroke you off, perhaps?"
                        else:
                            ch_s "Would my hand be an adequate substitute?"
                        menu:
                            extend ""
                            "Sure, that's fine.":
                                $ StormX.change_stat("love", 80, 2)
                                $ StormX.change_stat("inhibition", 60, 1)
                                $ StormX.change_stat("obedience", 50, 1)
                                jump Storm_HJ_Prep
                            "Nah, if it's not your mouth, forget it.":
                                $ StormX.change_stat("love", 200, -2)
                                $ StormX.ArmPose = 1
                                ch_s "That is unfortunate."
                                $ StormX.change_stat("obedience", 70, 2)
            "Suck it, [StormX.petname]":


                $ StormX.nameCheck()
                $ Approval = ApprovalCheck(StormX, 750, "OI", TabM = 3)
                if Approval > 1 or (Approval and StormX.Forced):
                    $ StormX.change_face("sad")
                    $ StormX.change_stat("love", 70, -5, 1)
                    $ StormX.change_stat("love", 200, -2)
                    ch_s ". . . fine. . ."
                    $ StormX.change_stat("obedience", 50, 4)
                    $ StormX.change_stat("inhibition", 80, 1)
                    $ StormX.change_stat("inhibition", 60, 3)
                    $ StormX.Forced = 1
                    jump Storm_BJ_Prep
                else:
                    $ StormX.change_stat("love", 200, -15)
                    $ StormX.recent_history.append("angry")
                    $ StormX.daily_history.append("angry")


    if "no_blowjob" in StormX.daily_history:
        $ StormX.change_face("angry", 1)
        ch_s "Then I hope you can take care of yourself."
        $ StormX.recent_history.append("angry")
        $ StormX.daily_history.append("angry")
    elif StormX.Forced:
        $ StormX.change_face("angry", 1)
        ch_s "You go too far!"
        $ StormX.change_stat("lust", 200, 5)
        if StormX.love > 300:
            $ StormX.change_stat("love", 70, -2)
        $ StormX.change_stat("obedience", 50, -2)
        $ StormX.recent_history.append("angry")
        $ StormX.daily_history.append("angry")
        $ StormX.recent_history.append("no_blowjob")
        $ StormX.daily_history.append("no_blowjob")
        return
    elif Taboo:
        $ StormX.change_face("angry", 1)
        $ StormX.daily_history.append("no_taboo")
        ch_s "This is much too exposed."
        $ StormX.change_stat("lust", 200, 5)
        $ StormX.change_stat("obedience", 50, -3)
        return
    elif StormX.action_counter["blowjob"]:
        $ StormX.change_face("sad")
        ch_s "I am just not in the mood, [StormX.player_petname]."
    else:
        $ StormX.change_face("normal", 1)
        ch_s "I do not think that I will."
    $ StormX.recent_history.append("no_blowjob")
    $ StormX.daily_history.append("no_blowjob")
    $ approval_bonus = 0
    return


label Storm_BJ_Prep:
    if renpy.showing("Storm_HJ_Animation"):
        hide Storm_HJ_Animation with easeoutbottom
    if Taboo:
        $ StormX.inhibition += int(Taboo/10)
        $ StormX.lust += int(Taboo/5)

    $ StormX.change_face("sexy")
    if StormX.Forced:
        $ StormX.change_face("sad")

    call Seen_First_Peen (StormX, Partner, React=action_context)
    call Storm_BJ_Launch ("L")

    if action_context == StormX:

        $ action_context = 0
        "[StormX.name] slides down and places your cock against her lips."
        menu:
            "What do you do?"
            "Nothing.":
                $ StormX.change_stat("inhibition", 80, 3)
                $ StormX.change_stat("inhibition", 40, 2)
                "[StormX.name] continues licking at it."
            "Praise her.":
                $ StormX.change_face("sexy", 1)
                $ StormX.change_stat("inhibition", 80, 3)
                ch_p "Hmmm, keep doing that, [StormX.petname]."
                $ StormX.nameCheck()
                "[StormX.name] continues her actions."
                $ StormX.change_stat("love", 85, 1)
                $ StormX.change_stat("obedience", 90, 1)
                $ StormX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ StormX.change_face("surprised")
                $ StormX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that for now, [StormX.petname]."
                $ StormX.nameCheck()
                "[StormX.name] puts it down."
                $ StormX.change_stat("obedience", 90, 1)
                $ StormX.change_stat("obedience", 50, 3)
                $ Player.recent_history.append("nope")
                $ StormX.AddWord(1,"refused","refused")
                return
    if not StormX.action_counter["blowjob"]:
        if StormX.Forced:
            $ StormX.change_stat("love", 90, -70)
            $ StormX.change_stat("obedience", 70, 45)
            $ StormX.change_stat("inhibition", 80, 60)
        else:
            $ StormX.change_stat("love", 90, 5)
            $ StormX.change_stat("obedience", 70, 35)
            $ StormX.change_stat("inhibition", 80, 40)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ StormX.DrainWord("no_taboo")
    $ StormX.DrainWord("no_blowjob")
    $ StormX.recent_history.append("blowjob")
    $ StormX.daily_history.append("blowjob")

label Storm_BJ_Cycle:
    while Round > 0:
        call shift_focus (StormX)
        call Storm_BJ_Launch
        $ StormX.lust_face()

        if Player.focus < 100:

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
                    if "pushed" not in StormX.recent_history and StormX.action_counter["blowjob"] < 5:
                        $ StormX.change_stat("love", 80, -(20-(2*StormX.action_counter["blowjob"])))
                        $ StormX.change_stat("obedience", 80, (30-(3*StormX.action_counter["blowjob"])))
                        $ StormX.recent_history.append("pushed")
                    if offhand_action == "jackin" and action_speed != 3:
                        "She takes it to the root, and you move your hand out of the way."
                    $ action_speed = 4
                "Take it deeper. (locked)" if action_speed == 4:
                    pass
                "Set your own pace. . .":

                    "[StormX.name] hums contentedly."
                    if "setpace" not in StormX.recent_history:
                        $ StormX.change_stat("love", 80, 2)
                    $ D20 = renpy.random.randint(1, 20)
                    if StormX.action_counter["blowjob"] < 5:
                        $ D20 -= 10
                    elif StormX.action_counter["blowjob"] < 10:
                        $ D20 -= 5

                    if D20 > 15:
                        $ action_speed = 4
                        if "setpace" not in StormX.recent_history:
                            $ StormX.change_stat("inhibition", 80, 3)
                    elif D20 > 10:
                        $ action_speed = 3
                    elif D20 > 5:
                        $ action_speed = 2
                    else:
                        $ action_speed = 1
                    $ StormX.recent_history.append("setpace")

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "Other options":

                    menu:
                        "I also want to fondle her breasts." if offhand_action != "fondle_breasts":
                            if StormX.remaining_actions and multi_action:
                                $ offhand_action = "fondle_breasts"
                                "You start to fondle her breasts."
                                $ StormX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (StormX, "tired")
                        "Shift primary action":

                            if StormX.remaining_actions and multi_action:
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
                                call Sex_Basic_Dialog (StormX, "tired")

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Asks [StormX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (StormX)
                                "Asks [StormX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (StormX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (StormX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Storm_BJ_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Storm_BJ_Cycle
                                "Never mind":
                                    jump Storm_BJ_Cycle
                        "Undress [StormX.name]":
                            call Girl_Undress (StormX)
                        "Clean up [StormX.name] (locked)" if not StormX.Spunk:
                            pass
                        "Clean up [StormX.name]" if StormX.Spunk:
                            call Girl_Cleanup (StormX, "ask")
                        "Never mind":
                            jump Storm_BJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Storm_BJ_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Storm_BJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Storm_BJ_Reset
                    $ Line = 0
                    jump Storm_BJ_After


        call shift_focus (StormX)
        call Sex_Dialog (StormX, Partner)



        $ counter += 1
        $ Round -= 1
        if action_speed:
            $ Player.Wet = 1
            $ Player.Spunk = 0 if Player.Spunk else Player.Spunk

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or StormX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (StormX)
                if "angry" in StormX.recent_history:
                    call Storm_BJ_Reset
                    return
                $ StormX.change_stat("lust", 200, 5)
                if 100 > StormX.lust >= 70 and StormX.session_orgasms < 2 and StormX.SEXP >= 20:
                    $ StormX.recent_history.append("unsatisfied")
                    $ StormX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Storm_BJ_After
                $ Line = "came"

            if StormX.lust >= 100:

                call Girl_Cumming (StormX)
                if action_context == "shift" or "angry" in StormX.recent_history:
                    jump Storm_BJ_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in StormX.recent_history:
                    "[StormX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Storm_BJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if StormX.SEXP >= 100 or ApprovalCheck(StormX, 1200, "LO"):
            pass
        elif counter == (15 + StormX.action_counter["blowjob"]):
            $ StormX.brows = "angry"
            menu:
                ch_s "My jaw is becoming uncomfortable, could we do something else?"
                "How about a Handy?" if StormX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Storm_BJ_After
                    call Storm_Handjob
                    return
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    $ counter += 1
                    "[Line]."
                    jump Storm_BJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Storm_BJ_Reset
                    $ action_context = "shift"
                    jump Storm_BJ_After
                "No, get back down there.":
                    if ApprovalCheck(StormX, 1200) or ApprovalCheck(StormX, 500, "O"):
                        $ StormX.change_stat("love", 200, -5)
                        $ StormX.change_stat("obedience", 50, 3)
                        $ StormX.change_stat("obedience", 80, 2)
                        "She scowls but gets back to work."
                    else:
                        $ StormX.change_face("angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        ch_s "Well then."
                        $ StormX.change_stat("love", 50, -3, 1)
                        $ StormX.change_stat("love", 80, -4, 1)
                        $ StormX.change_stat("obedience", 30, -1, 1)
                        $ StormX.change_stat("obedience", 50, -1, 1)
                        $ StormX.recent_history.append("angry")
                        $ StormX.daily_history.append("angry")
                        jump Storm_BJ_After
        elif counter == (10 + StormX.action_counter["blowjob"]) and StormX.SEXP <= 100 and not ApprovalCheck(StormX, 1200, "LO"):
            $ StormX.brows = "confused"
            ch_s "Are you about finished? I am growing tired of this."


        call Escalation (StormX)

        if Round == 10:
            call Sex_Basic_Dialog (StormX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (StormX, 5)


    $ StormX.change_face("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (StormX, "done")

label Storm_BJ_After:
    $ StormX.change_face("sexy")

    $ StormX.action_counter["blowjob"] += 1
    $ StormX.remaining_actions -=1
    $ StormX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ StormX.addiction_rate += 1

    call Partner_Like (StormX, 2)

    if "Storm Jobber" in Achievements:
        pass
    elif StormX.action_counter["blowjob"] >= 10:
        $ StormX.change_face("smile", 1)
        ch_s "I cannot imagine how I went this long without such a delicacy, [StormX.player_petname]."
        $ Achievements.append("Storm Jobber")
        $ StormX.SEXP += 5
    elif action_context == "shift":
        pass
    elif StormX.action_counter["blowjob"] == 1:
        $ StormX.SEXP += 15
        if StormX.love >= 500:
            $ StormX.mouth = "smile"
            ch_s "Hmm, that certainly was enjoyable . ."
        elif Player.focus <= 20:
            $ StormX.mouth = "sad"
            ch_s "did that meet your expectations?"
    elif StormX.action_counter["blowjob"] == 5:
        ch_s "I expect that you enjoyed that."
    $ approval_bonus = 0
    if action_context != "shift":
        call Storm_BJ_Reset
    call Checkout
    return






label Storm_Dildo_Check:
    if "dildo" in Player.Inventory:
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in StormX.Inventory:
        "You ask [StormX.name] to get out her favorite Dildo."
    else:
        "You don't have one of those on you."
        return 0
    return 1

label Storm_Dildo_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (StormX)
    call Storm_Dildo_Check
    if not _return:
        return

    if StormX.action_counter["dildo_pussy"]:
        $ approval_bonus += 15
    if StormX.PantsNum() >= 6:
        $ approval_bonus -= 20

    if StormX.lust > 95:
        $ approval_bonus += 20
    elif StormX.lust > 85:
        $ approval_bonus += 15

    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in StormX.Traits:
        $ approval_bonus += (5*Taboo)
    if StormX in Player.Harem or "sex friend" in StormX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in StormX.Traits:
        $ approval_bonus -= 40
    if StormX.event_counter["forced"] and not StormX.Forced:
        $ approval_bonus -= 5*StormX.event_counter["forced"]

    if Taboo and "no_taboo" in StormX.daily_history:
        $ approval_bonus -= 10

    if "no_dildo" in StormX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_dildo" in StormX.recent_history else 0

    $ Approval = ApprovalCheck(StormX, 1250, TabM = 4)

    if action_context == StormX:
        if Approval > 2:
            if StormX.PantsNum() == 5:
                "[StormX.name] grabs her dildo, hiking up her skirt as she does."
                $ StormX.Upskirt = 1
            elif StormX.PantsNum() > 6:
                "[StormX.name] grabs her dildo, pulling down her pants as she does."
                $ StormX.legs = 0
            else:
                "[StormX.name] grabs her dildo, rubbing is suggestively against her crotch."
            $ StormX.SeenPanties = 1
            "She slides the tip along her pussy and seems to want you to insert it."
            menu:
                "What do you do?"
                "Nothing.":
                    $ StormX.change_stat("inhibition", 80, 3)
                    $ StormX.change_stat("inhibition", 50, 2)
                    "[StormX.name] slides it in."
                "Go for it.":
                    $ StormX.change_face("sexy", 1)
                    $ StormX.change_stat("inhibition", 80, 3)
                    ch_p "Oh yeah, [StormX.petname], let's do this."
                    $ StormX.nameCheck()
                    "You grab the dildo and slide it in."
                    $ StormX.change_stat("love", 85, 1)
                    $ StormX.change_stat("obedience", 90, 1)
                    $ StormX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ StormX.change_face("surprised")
                    $ StormX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that right now, [StormX.petname]."
                    $ StormX.nameCheck()
                    "[StormX.name] sets the dildo down."
                    $ StormX.change_outfit()
                    $ StormX.change_stat("obedience", 90, 1)
                    $ StormX.change_stat("obedience", 50, 1)
                    $ StormX.change_stat("obedience", 30, 2)
                    return
            jump Storm_DP_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
        return

    if action_context == "auto":
        "You rub the dildo across her body, and along her moist slit."
        $ StormX.change_face("surprised", 1)

        if (StormX.action_counter["dildo_pussy"] and Approval) or (Approval > 1):
            "[StormX.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            $ StormX.change_face("sexy")
            $ StormX.change_stat("obedience", 70, 3)
            $ StormX.change_stat("inhibition", 50, 3)
            $ StormX.change_stat("inhibition", 70, 1)
            ch_s "Hmm, [StormX.player_petname], toys!"
            jump Storm_DP_Prep
        else:
            $ StormX.brows = "angry"
            menu:
                ch_s "Excuse yourself, what are you planning to do with that?!"
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ StormX.change_face("sexy", 1)
                        $ StormX.change_stat("obedience", 70, 3)
                        $ StormX.change_stat("inhibition", 50, 3)
                        $ StormX.change_stat("inhibition", 70, 1)
                        ch_s "Well, now that you mention it. . ."
                        jump Storm_DP_Prep
                    "You pull back before you really get it in."
                    $ StormX.change_face("bemused", 1)
                    if StormX.action_counter["dildo_pussy"]:
                        ch_s "Well, [StormX.player_petname], maybe warn me next time?"
                    else:
                        ch_s "Well, [StormX.player_petname], that's a little much. . . for now . . ."
                "Just playing with my favorite toys.":
                    $ StormX.change_stat("love", 80, -10, 1)
                    $ StormX.change_stat("love", 200, -10)
                    "You press it inside some more."
                    $ StormX.change_stat("obedience", 70, 3)
                    $ StormX.change_stat("inhibition", 50, 3)
                    if not ApprovalCheck(StormX, 700, "O", TabM=1):
                        $ StormX.change_face("angry")
                        "[StormX.name] shoves you away and slaps you in the face."
                        ch_s "Ask nicely before trying anything like that!"
                        $ StormX.change_stat("love", 50, -10, 1)
                        $ StormX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        if renpy.showing("Storm_SexSprite"):
                            call Storm_Sex_Reset
                        $ StormX.recent_history.append("angry")
                        $ StormX.daily_history.append("angry")
                    else:
                        $ StormX.change_face("sad")
                        "[StormX.name] doesn't seem to be into this, you're lucky she's so obedient."
                        jump Storm_DP_Prep
        return


    if not StormX.action_counter["dildo_pussy"]:

        $ StormX.change_face("surprised", 1)
        $ StormX.mouth = "kiss"
        ch_s "Hmmm, so you'd like to try out some toys?"
        if StormX.Forced:
            $ StormX.change_face("sad")
            ch_s "I suppose there are worst things you could ask for."

    if not StormX.action_counter["dildo_pussy"] and Approval:

        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
        elif StormX.love >= (StormX.obedience + StormX.inhibition):
            $ StormX.change_face("sexy")
            $ StormX.brows = "sad"
            $ StormX.mouth = "smile"
            ch_s "I've had a reasonable amount of experience with these, you know. . ."
        elif StormX.obedience >= StormX.inhibition:
            $ StormX.change_face("normal")
            ch_s "If that is what you want, [StormX.player_petname]. . ."
        else:
            $ StormX.change_face("sad")
            $ StormX.mouth = "smile"
            ch_s "I guess it could be fun with a partner. . ."

    elif Approval:

        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
            ch_s "The toys again?"
        elif not Taboo and "no_taboo" in StormX.daily_history:
            ch_s "Well, at least you got us some privacy this time. . ."
        elif "dildo_pussy" in StormX.recent_history:
            $ StormX.change_face("sexy", 1)
            ch_s "Mmm, again? Ok, let's get to it."
            jump Storm_DP_Prep
        elif "dildo_pussy" in StormX.daily_history:
            $ StormX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "You did not get enough earlier?",
                    "You're going to wear me out."])
            ch_s "[Line]"
        elif StormX.action_counter["dildo_pussy"] < 3:
            $ StormX.change_face("sexy", 1)
            $ StormX.brows = "confused"
            $ StormX.mouth = "kiss"
            ch_s "You want to stick it in my pussy again?"
        else:
            $ StormX.change_face("sexy", 1)
            $ StormX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my pussy again?",
                    "You want me ta lube up your toy?"])
            ch_s "[Line]"
            $ Line = 0

    if Approval >= 2:

        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("obedience", 90, 1)
            $ StormX.change_stat("inhibition", 60, 1)
            ch_s "Ok, fine."
        else:
            $ StormX.change_face("sexy", 1)
            $ StormX.change_stat("love", 90, 1)
            $ StormX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                    "Well. . . ok.",                 
                    "Sure!", 
                    "I guess I could. . . stick it in.",
                    "Delightful.",
                    "Hmm, ok, ok."])
            ch_s "[Line]"
            $ Line = 0
        $ StormX.change_stat("obedience", 20, 1)
        $ StormX.change_stat("obedience", 60, 1)
        $ StormX.change_stat("inhibition", 70, 2)
        jump Storm_DP_Prep
    else:


        $ StormX.change_face("angry")
        if "no_dildo" in StormX.recent_history:
            ch_s "What part of \"no,\" did you not get, [StormX.player_petname]?"
        elif Taboo and "no_taboo" in StormX.daily_history and "no_dildo" in StormX.daily_history:
            ch_s "Stop showing that thing around in public!"
        elif "no_dildo" in StormX.daily_history:
            ch_s "I already told you \"no,\" [StormX.player_petname]."
        elif Taboo and "no_taboo" in StormX.daily_history:
            ch_s "Stop showing that thing around in public!"
        elif not StormX.action_counter["dildo_pussy"]:
            $ StormX.change_face("bemused")
            ch_s "I'm a bit past toys, [StormX.player_petname]. . ."
        else:
            $ StormX.change_face("bemused")
            ch_s "We don't need any toys, do we, [StormX.player_petname]?"
        menu:
            extend ""
            "Sorry, never mind." if "no_dildo" in StormX.daily_history:
                $ StormX.change_face("bemused")
                ch_s "I thought as much, [StormX.player_petname]."
                return
            "Maybe later?" if "no_dildo" not in StormX.daily_history:
                $ StormX.change_face("sexy")
                ch_s "Maybe I'll practice on my own time, [StormX.player_petname]."
                $ StormX.change_stat("love", 80, 2)
                $ StormX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ StormX.recent_history.append("no_taboo")
                    $ StormX.daily_history.append("no_taboo")
                $ StormX.recent_history.append("no_dildo")
                $ StormX.daily_history.append("no_dildo")
                return
            "I think you'd like it. . .":
                if Approval:
                    $ StormX.change_face("sexy")
                    $ StormX.change_stat("obedience", 90, 2)
                    $ StormX.change_stat("obedience", 50, 2)
                    $ StormX.change_stat("inhibition", 70, 3)
                    $ StormX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                            "I suppose. . .", 
                            "You make a compelling argument."])
                    ch_s "[Line]"
                    $ Line = 0
                    jump Storm_DP_Prep
                else:
                    pass
            "[[press it against her]":

                $ Approval = ApprovalCheck(StormX, 950, "OI", TabM = 3)
                if Approval > 1 or (Approval and StormX.Forced):
                    $ StormX.change_face("sad")
                    $ StormX.change_stat("love", 70, -5, 1)
                    $ StormX.change_stat("love", 200, -5)
                    ch_s "Ok, fine. If we're going to do this, stick it in already."
                    $ StormX.change_stat("obedience", 80, 4)
                    $ StormX.change_stat("inhibition", 80, 1)
                    $ StormX.change_stat("inhibition", 60, 3)
                    $ StormX.Forced = 1
                    jump Storm_DP_Prep
                else:
                    $ StormX.change_stat("love", 200, -20)
                    $ StormX.recent_history.append("angry")
                    $ StormX.daily_history.append("angry")


    $ StormX.ArmPose = 1
    if "no_dildo" in StormX.daily_history:
        ch_s "Learn to take \"no\" for an answer, [StormX.player_petname]."
        $ StormX.recent_history.append("angry")
        $ StormX.daily_history.append("angry")
    elif StormX.Forced:
        $ StormX.change_face("angry", 1)
        ch_s "I'm not going to let you use that on me."
        $ StormX.change_stat("lust", 200, 5)
        if StormX.love > 300:
            $ StormX.change_stat("love", 70, -2)
        $ StormX.change_stat("obedience", 50, -2)
        $ StormX.recent_history.append("angry")
        $ StormX.daily_history.append("angry")
    elif Taboo:
        $ StormX.change_face("angry", 1)
        $ StormX.recent_history.append("no_taboo")
        $ StormX.daily_history.append("no_taboo")
        ch_s "Not here!"
        $ StormX.change_stat("lust", 200, 5)
        $ StormX.change_stat("obedience", 50, -3)
    elif StormX.action_counter["dildo_pussy"]:
        $ StormX.change_face("sad")
        ch_s "Sorry, you can keep your toys to yourself."
    else:
        $ StormX.change_face("normal", 1)
        ch_s "No way."
    $ StormX.recent_history.append("no_dildo")
    $ StormX.daily_history.append("no_dildo")
    $ approval_bonus = 0
    return

label Storm_DP_Prep:
    if offhand_action == "dildo_pussy":
        return

    if not StormX.Forced and action_context != "auto":
        $ approval_bonus = 15 if StormX.PantsNum() > 6 else 0
        call Bottoms_Off (StormX)
        if "angry" in StormX.recent_history:
            return

    $ approval_bonus = 0
    call Storm_Pussy_Launch ("dildo_pussy")
    if not StormX.action_counter["dildo_pussy"]:
        if StormX.Forced:
            $ StormX.change_stat("love", 90, -75)
            $ StormX.change_stat("obedience", 70, 60)
            $ StormX.change_stat("inhibition", 80, 35)
        else:
            $ StormX.change_stat("love", 90, 10)
            $ StormX.change_stat("obedience", 70, 20)
            $ StormX.change_stat("inhibition", 80, 45)
    if Taboo:
        $ StormX.inhibition += int(Taboo/10)
        $ StormX.lust += int(Taboo/5)


    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ StormX.DrainWord("no_taboo")
    $ StormX.DrainWord("no_dildo")
    $ StormX.recent_history.append("dildo_pussy")
    $ StormX.daily_history.append("dildo_pussy")

label Storm_DP_Cycle:
    while Round > 0:
        call shift_focus (StormX)
        call Storm_Pussy_Launch ("dildo_pussy")
        $ StormX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (StormX)
                    jump Storm_DP_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "Other options":

                    menu:
                        "Offhand action":
                            if StormX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ StormX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (StormX, "tired")
                        "Shift primary action":

                            if StormX.remaining_actions and multi_action:
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
                                call Sex_Basic_Dialog (StormX, "tired")

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
                                "Asks [StormX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (StormX)
                                "Asks [StormX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (StormX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (StormX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Storm_DP_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Storm_DP_Cycle
                                "Never mind":
                                    jump Storm_DP_Cycle
                        "Undress [StormX.name]":
                            call Girl_Undress (StormX)
                        "Clean up [StormX.name] (locked)" if not StormX.Spunk:
                            pass
                        "Clean up [StormX.name]" if StormX.Spunk:
                            call Girl_Cleanup (StormX, "ask")
                        "Never mind":
                            jump Storm_DP_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Storm_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Storm_DP_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Storm_Pos_Reset
                    $ Line = 0
                    jump Storm_DP_After


        if StormX.underwear or StormX.PantsNum() > 6 or StormX.HoseNum() >= 5:
            call Girl_Undress (StormX, "auto")

        call shift_focus (StormX)
        call Sex_Dialog (StormX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or StormX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (StormX)
                if "angry" in StormX.recent_history:
                    call Storm_Pos_Reset
                    return
                $ StormX.change_stat("lust", 200, 5)
                if 100 > StormX.lust >= 70 and StormX.session_orgasms < 2:
                    $ StormX.recent_history.append("unsatisfied")
                    $ StormX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Storm_DP_After
                $ Line = "came"
            if StormX.lust >= 100:

                call Girl_Cumming (StormX)
                if action_context == "shift" or "angry" in StormX.recent_history:
                    jump Storm_DP_After
            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."
                if "unsatisfied" in StormX.recent_history:
                    "[StormX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Storm_DP_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if StormX.SEXP >= 100 or ApprovalCheck(StormX, 1200, "LO"):
            pass
        elif counter == (5 + StormX.action_counter["dildo_pussy"]):
            $ StormX.brows = "confused"
            ch_s "What are you even doing down there?"
        elif StormX.lust >= 80:
            pass
        elif counter == (15 + StormX.action_counter["dildo_pussy"]) and StormX.SEXP >= 15 and not ApprovalCheck(StormX, 1500):
            $ StormX.brows = "confused"
            menu:
                ch_s "[StormX.player_petname], this is getting uncomfortable, maybe we could try something else."
                "Finish up.":
                    "You let go. . ."
                    jump Storm_DP_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Storm_DP_After
                "No, this is fun.":
                    if ApprovalCheck(StormX, 1200) or ApprovalCheck(StormX, 500, "O"):
                        $ StormX.change_stat("love", 200, -5)
                        $ StormX.change_stat("obedience", 50, 3)
                        $ StormX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ StormX.change_face("angry", 1)
                        call Storm_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_s "Well if that's your attitude, I don't need your \"help\"."
                        $ StormX.change_stat("love", 50, -3, 1)
                        $ StormX.change_stat("love", 80, -4, 1)
                        $ StormX.change_stat("obedience", 30, -1, 1)
                        $ StormX.change_stat("obedience", 50, -1, 1)
                        $ StormX.recent_history.append("angry")
                        $ StormX.daily_history.append("angry")
                        jump Storm_DP_After


        if Round == 10:
            call Sex_Basic_Dialog (StormX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (StormX, 5)


    $ StormX.change_face("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (StormX, "done")


label Storm_DP_After:
    if not action_context:
        call Storm_Pos_Reset

    $ StormX.change_face("sexy")

    $ StormX.action_counter["dildo_pussy"] += 1
    $ StormX.remaining_actions -=1

    call Partner_Like (StormX, 1)

    if StormX.action_counter["dildo_pussy"] == 1:
        $ StormX.SEXP += 10
        if not action_context:
            if StormX.love >= 500 and "unsatisfied" not in StormX.recent_history:
                ch_s "I appreciate the work you put in. . ."
            elif StormX.obedience <= 500 and Player.focus <= 20:
                $ StormX.change_face("perplexed", 1)
                ch_s "Did you enjoy that?"

    $ approval_bonus = 0


    call Checkout
    return






label Storm_Dildo_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (StormX)
    call Storm_Dildo_Check
    if not _return:
        return

    if StormX.used_to_anal:
        $ approval_bonus += 30
    elif "anal" in StormX.recent_history or "dildo_anal" in StormX.recent_history:
        $ approval_bonus -= 20
    elif "anal" in StormX.daily_history or "dildo_anal" in StormX.daily_history:
        $ approval_bonus -= 10
    elif (StormX.action_counter["anal"] + StormX.action_counter["dildo_ass"] + StormX.Plug) > 0:
        $ approval_bonus += 20

    if StormX.PantsNum() >= 6:
        $ approval_bonus -= 20

    if StormX.lust > 95:
        $ approval_bonus += 20
    elif StormX.lust > 85:
        $ approval_bonus += 15

    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in StormX.Traits:
        $ approval_bonus += (5*Taboo)
    if StormX in Player.Harem or "sex friend" in StormX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in StormX.Traits:
        $ approval_bonus -= 40
    if StormX.event_counter["forced"] and not StormX.Forced:
        $ approval_bonus -= 5*StormX.event_counter["forced"]

    if Taboo and "no_taboo" in StormX.daily_history:
        $ approval_bonus -= 10

    if "no_dildo" in StormX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_dildo" in StormX.recent_history else 0

    $ Approval = ApprovalCheck(StormX, 1450, TabM = 4)

    if action_context == StormX:

        if Approval > 2:
            if StormX.PantsNum() == 5:
                "[StormX.name] grabs her dildo, hiking up her skirt as she does."
                $ StormX.Upskirt = 1
            elif StormX.PantsNum() > 6:
                "[StormX.name] grabs her dildo, pulling down her pants as she does."
                $ StormX.legs = 0
            else:
                "[StormX.name] grabs her dildo, rubbing is suggestively against her ass."
            $ StormX.SeenPanties = 1
            "She slides the tip against her asshole, and seems to want you to insert it."
            menu:
                "What do you do?"
                "Nothing.":
                    $ StormX.change_stat("inhibition", 80, 3)
                    $ StormX.change_stat("inhibition", 50, 2)
                    "[StormX.name] slides it in."
                "Go for it.":
                    $ StormX.change_face("sexy", 1)
                    $ StormX.change_stat("inhibition", 80, 3)
                    ch_p "Oh yeah, [StormX.petname], let's do this."
                    $ StormX.nameCheck()
                    "You grab the dildo and slide it in."
                    $ StormX.change_stat("love", 85, 1)
                    $ StormX.change_stat("obedience", 90, 1)
                    $ StormX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ StormX.change_face("surprised")
                    $ StormX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that right now, [StormX.petname]."
                    $ StormX.nameCheck()
                    "[StormX.name] sets the dildo down."
                    $ StormX.change_outfit()
                    $ StormX.change_stat("obedience", 90, 1)
                    $ StormX.change_stat("obedience", 50, 1)
                    $ StormX.change_stat("obedience", 30, 2)
                    return
            jump Storm_DA_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
        return

    if action_context == "auto":
        "You rub the dildo across her body, and against her tight anus."
        $ StormX.change_face("surprised", 1)

        if (StormX.action_counter["dildo_ass"] and Approval) or (Approval > 1):

            "[StormX.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            $ StormX.change_face("sexy")
            $ StormX.change_stat("obedience", 70, 3)
            $ StormX.change_stat("inhibition", 50, 3)
            $ StormX.change_stat("inhibition", 70, 1)
            ch_s "Mmmm, [StormX.player_petname], toys. . ."
            jump Storm_DA_Prep
        else:

            $ StormX.brows = "angry"
            menu:
                ch_s "Excuse yourself, what are you planning to do with that?!"
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ StormX.change_face("sexy", 1)
                        $ StormX.change_stat("obedience", 70, 3)
                        $ StormX.change_stat("inhibition", 50, 3)
                        $ StormX.change_stat("inhibition", 70, 1)
                        ch_s "Well, now that you mention it. . ."
                        jump Storm_DA_Prep
                    "You pull back before you really get it in."
                    $ StormX.change_face("bemused", 1)
                    if StormX.action_counter["dildo_ass"]:
                        ch_s "Well, [StormX.player_petname], maybe warn me next time?"
                    else:
                        ch_s "Well, [StormX.player_petname], that's a little much. . . for now . . ."
                "Just playing with my favorite toys.":
                    $ StormX.change_stat("love", 80, -10, 1)
                    $ StormX.change_stat("love", 200, -10)
                    "You press it inside some more."
                    $ StormX.change_stat("obedience", 70, 3)
                    $ StormX.change_stat("inhibition", 50, 3)
                    if not ApprovalCheck(StormX, 700, "O", TabM=1):
                        $ StormX.change_face("angry")
                        "[StormX.name] shoves you away and slaps you in the face."
                        ch_s "Ask nicely if you want to stick something in my ass!"
                        $ StormX.change_stat("love", 50, -10, 1)
                        $ StormX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        if renpy.showing("Storm_SexSprite"):
                            call Storm_Sex_Reset
                        $ StormX.recent_history.append("angry")
                        $ StormX.daily_history.append("angry")
                    else:
                        $ StormX.change_face("sad")
                        "[StormX.name] doesn't seem to be into this, you're lucky she's so obedient."
                        jump Storm_DA_Prep
        return


    if not StormX.action_counter["dildo_ass"]:

        $ StormX.change_face("surprised", 1)
        $ StormX.mouth = "kiss"
        ch_s "Hmm, you don't take half measures. . ."
        if StormX.Forced:
            $ StormX.change_face("sad")
            ch_s "They always go for the butt. . ."

    if not StormX.action_counter["dildo_ass"] and Approval:

        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
        elif StormX.love >= (StormX.obedience + StormX.inhibition):
            $ StormX.change_face("sexy")
            $ StormX.brows = "sad"
            $ StormX.mouth = "smile"
            ch_s "I suppose you might enjoy that. . ."
        elif StormX.obedience >= StormX.inhibition:
            $ StormX.change_face("normal")
            ch_s "If that is what you want, [StormX.player_petname]. . ."
        else:
            $ StormX.change_face("sad")
            $ StormX.mouth = "smile"
            ch_s "I suppose I could enjoy that. . ."

    elif Approval:

        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
            ch_s "The toys again?"
        elif not Taboo and "no_taboo" in StormX.daily_history:
            ch_s "Well, at least you got us some privacy this time. . ."
        elif "dildo_anal" in StormX.daily_history and not StormX.used_to_anal:
            pass
        elif StormX.action_counter["dildo_ass"] < 3:
            $ StormX.change_face("sexy", 1)
            $ StormX.brows = "confused"
            $ StormX.mouth = "kiss"
            ch_s "You want to stick it in my ass again?"
        else:
            $ StormX.change_face("sexy", 1)
            $ StormX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You'd like to stick it in my ass again?",
                    "You'd like me to lube up your toy?"])
            ch_s "[Line]"
            $ Line = 0

    if Approval >= 2:

        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("obedience", 90, 1)
            $ StormX.change_stat("inhibition", 60, 1)
            ch_s "Oh, fine."
        else:
            $ StormX.change_face("sexy", 1)
            $ StormX.change_stat("love", 90, 1)
            $ StormX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                    "Hmm. . . ok.",                 
                    "Sure!", 
                    "I guess I could. . . stick it in.",
                    "Delightful.",
                    "Hmm, ok, ok."])
            ch_s "[Line]"
            $ Line = 0
        $ StormX.change_stat("obedience", 20, 1)
        $ StormX.change_stat("obedience", 60, 1)
        $ StormX.change_stat("inhibition", 70, 2)
        jump Storm_DA_Prep
    else:


        $ StormX.change_face("angry")
        if "no_dildo" in StormX.recent_history:
            ch_s "What part of \"no,\" did you not get, [StormX.player_petname]?"
        elif Taboo and "no_taboo" in StormX.daily_history and "no_dildo" in StormX.daily_history:
            ch_s "Stop swinging that thing around in public!"
        elif "no_dildo" in StormX.daily_history:
            ch_s "I already told you \"no,\" [StormX.player_petname]."
        elif Taboo and "no_taboo" in StormX.daily_history:
            ch_s "I already told you that I wouldn't do that out here!"
        elif not StormX.action_counter["dildo_ass"]:
            $ StormX.change_face("bemused")
            ch_s "I'm just not into toys, [StormX.player_petname]. . ."
        else:
            $ StormX.change_face("bemused")
            ch_s "I don't think we need any toys, [StormX.player_petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no_dildo" in StormX.daily_history:
                $ StormX.change_face("bemused")
                ch_s "I'm sure, [StormX.player_petname]."
                return
            "Maybe later?" if "no_dildo" not in StormX.daily_history:
                $ StormX.change_face("sexy")
                ch_s "Perhaps I'll practice on my own time, [StormX.player_petname]."
                $ StormX.change_stat("love", 80, 2)
                $ StormX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ StormX.recent_history.append("no_taboo")
                    $ StormX.daily_history.append("no_taboo")
                $ StormX.recent_history.append("no_dildo")
                $ StormX.daily_history.append("no_dildo")
                return
            "I think you'd like it. . .":
                if Approval:
                    $ StormX.change_face("sexy")
                    $ StormX.change_stat("obedience", 90, 2)
                    $ StormX.change_stat("obedience", 50, 2)
                    $ StormX.change_stat("inhibition", 70, 3)
                    $ StormX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Very well, stick it in.",     
                            "I suppose. . .", 
                            "You make a compelling argument."])
                    ch_s "[Line]"
                    $ Line = 0
                    jump Storm_DA_Prep
                else:
                    pass
            "[[press it against her]":

                $ Approval = ApprovalCheck(StormX, 1050, "OI", TabM = 3)
                if Approval > 1 or (Approval and StormX.Forced):
                    $ StormX.change_face("sad")
                    $ StormX.change_stat("love", 70, -5, 1)
                    $ StormX.change_stat("love", 200, -5)
                    ch_s "Ok, fine. If we're going to do this, stick it in already."
                    $ StormX.change_stat("obedience", 80, 4)
                    $ StormX.change_stat("inhibition", 80, 1)
                    $ StormX.change_stat("inhibition", 60, 3)
                    $ StormX.Forced = 1
                    jump Storm_DA_Prep
                else:
                    $ StormX.change_stat("love", 200, -20)
                    $ StormX.recent_history.append("angry")
                    $ StormX.daily_history.append("angry")


    $ StormX.ArmPose = 1
    if "no_dildo" in StormX.daily_history:
        ch_s "Learn to take \"no\" for an answer, [StormX.player_petname]."
        $ StormX.recent_history.append("angry")
        $ StormX.daily_history.append("angry")
    elif StormX.Forced:
        $ StormX.change_face("angry", 1)
        ch_s "I'm not going to let you use that on me."
        $ StormX.change_stat("lust", 200, 5)
        if StormX.love > 300:
            $ StormX.change_stat("love", 70, -2)
        $ StormX.change_stat("obedience", 50, -2)
        $ StormX.recent_history.append("angry")
        $ StormX.daily_history.append("angry")
    elif Taboo:
        $ StormX.change_face("angry", 1)
        $ StormX.recent_history.append("no_taboo")
        $ StormX.daily_history.append("no_taboo")
        ch_s "Not here!"
        $ StormX.change_stat("lust", 200, 5)
        $ StormX.change_stat("obedience", 50, -3)
    elif StormX.action_counter["dildo_ass"]:
        $ StormX.change_face("sad")
        ch_s "Sorry, you can keep your toys out of there."
    else:
        $ StormX.change_face("normal", 1)
        ch_s "No, thank you."
    $ StormX.recent_history.append("no_dildo")
    $ StormX.daily_history.append("no_dildo")
    $ approval_bonus = 0
    return

label Storm_DA_Prep:
    if offhand_action == "dildo_anal":
        return

    if not StormX.Forced and action_context != "auto":
        $ approval_bonus = 20 if StormX.PantsNum() > 6 else 0
        call Bottoms_Off (StormX)
        if "angry" in StormX.recent_history:
            return

    $ approval_bonus = 0
    call Storm_Pussy_Launch ("dildo_anal")
    if not StormX.action_counter["dildo_ass"]:
        if StormX.Forced:
            $ StormX.change_stat("love", 90, -75)
            $ StormX.change_stat("obedience", 70, 60)
            $ StormX.change_stat("inhibition", 80, 35)
        else:
            $ StormX.change_stat("love", 90, 10)
            $ StormX.change_stat("obedience", 70, 20)
            $ StormX.change_stat("inhibition", 80, 45)
    if Taboo:
        $ StormX.inhibition += int(Taboo/10)
        $ StormX.lust += int(Taboo/5)


    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ StormX.DrainWord("no_taboo")
    $ StormX.DrainWord("no_dildo")
    $ StormX.recent_history.append("dildo_anal")
    $ StormX.daily_history.append("dildo_anal")

label Storm_DA_Cycle:
    while Round > 0:
        call shift_focus (StormX)
        call Storm_Pussy_Launch ("dildo_anal")
        $ StormX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (StormX)
                    jump Storm_DA_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "Other options":

                    menu:
                        "Offhand action":
                            if StormX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ StormX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (StormX, "tired")
                        "Shift primary action":

                            if StormX.remaining_actions and multi_action:
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
                                call Sex_Basic_Dialog (StormX, "tired")

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
                                "Asks [StormX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (StormX)
                                "Asks [StormX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (StormX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (StormX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Storm_DA_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Storm_DA_Cycle
                                "Never mind":
                                    jump Storm_DA_Cycle
                        "Undress [StormX.name]":
                            call Girl_Undress (StormX)
                        "Clean up [StormX.name] (locked)" if not StormX.Spunk:
                            pass
                        "Clean up [StormX.name]" if StormX.Spunk:
                            call Girl_Cleanup (StormX, "ask")
                        "Never mind":
                            jump Storm_DA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Storm_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Storm_DA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Storm_Pos_Reset
                    $ Line = 0
                    jump Storm_DA_After


        if StormX.underwear or StormX.PantsNum() > 6 or StormX.HoseNum() >= 5:
            call Girl_Undress (StormX, "auto")

        call shift_focus (StormX)
        call Sex_Dialog (StormX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or StormX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (StormX)
                if "angry" in StormX.recent_history:
                    call Storm_Pos_Reset
                    return
                $ StormX.change_stat("lust", 200, 5)
                if 100 > StormX.lust >= 70 and StormX.session_orgasms < 2:
                    $ StormX.recent_history.append("unsatisfied")
                    $ StormX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Storm_DA_After
                $ Line = "came"

            if StormX.lust >= 100:

                call Girl_Cumming (StormX)
                if action_context == "shift" or "angry" in StormX.recent_history:
                    jump Storm_DA_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in StormX.recent_history:
                    "[StormX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Storm_DA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if StormX.SEXP >= 100 or ApprovalCheck(StormX, 1200, "LO"):
            pass
        elif counter == (5 + StormX.action_counter["dildo_ass"]):
            $ StormX.brows = "confused"
            ch_s "What are you even doing down there?"
        elif StormX.lust >= 80:
            pass
        elif counter == (15 + StormX.action_counter["dildo_ass"]) and StormX.SEXP >= 15 and not ApprovalCheck(StormX, 1500):
            $ StormX.brows = "confused"
            menu:
                ch_s "[StormX.player_petname], this is getting uncomfortable, maybe we could try something else."
                "Finish up.":
                    "You let go. . ."
                    jump Storm_DA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Storm_DA_After
                "No, this is fun.":
                    if ApprovalCheck(StormX, 1200) or ApprovalCheck(StormX, 500, "O"):
                        $ StormX.change_stat("love", 200, -5)
                        $ StormX.change_stat("obedience", 50, 3)
                        $ StormX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ StormX.change_face("angry", 1)
                        call Storm_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_s "Well if that's your attitude, I don't need your \"help\"."
                        $ StormX.change_stat("love", 50, -3, 1)
                        $ StormX.change_stat("love", 80, -4, 1)
                        $ StormX.change_stat("obedience", 30, -1, 1)
                        $ StormX.change_stat("obedience", 50, -1, 1)
                        $ StormX.recent_history.append("angry")
                        $ StormX.daily_history.append("angry")
                        jump Storm_DA_After


        if Round == 10:
            call Sex_Basic_Dialog (StormX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (StormX, 5)


    $ StormX.change_face("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (StormX, "done")


label Storm_DA_After:
    if not action_context:
        call Storm_Pos_Reset

    $ StormX.change_face("sexy")

    $ StormX.action_counter["dildo_ass"] += 1
    $ StormX.remaining_actions -=1

    call Partner_Like (StormX, 1)

    if StormX.action_counter["dildo_ass"] == 1:
        $ StormX.SEXP += 10
        if not action_context:
            if StormX.love >= 500 and "unsatisfied" not in StormX.recent_history:
                ch_s "That was. . . engaging. . ."
            elif StormX.obedience <= 500 and Player.focus <= 20:
                $ StormX.change_face("perplexed", 1)
                ch_s "Did you enjoy that?"

    $ approval_bonus = 0


    call Checkout
    return



label Storm_Vibrator_Check:
    if "vibrator" in Player.Inventory:
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in StormX.Inventory:
        "You ask [StormX.name] to get out her vibrator."
    else:
        "You don't have one of those on you."
        return 0
    return 1


label Storm_Footjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (StormX)
    if StormX.action_counter["footjob"] >= 7:
        $ approval_bonus += 10
    elif StormX.action_counter["footjob"] >= 3:
        $ approval_bonus += 7
    elif StormX.action_counter["footjob"]:
        $ approval_bonus += 3

    if StormX.addiction >= 75 and StormX.event_counter["swallowed"] >=3:
        $ approval_bonus += 10
    if StormX.addiction >= 75:
        $ approval_bonus += 5

    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in StormX.Traits:
        $ approval_bonus += (3*Taboo)
    if StormX in Player.Harem or "sex friend" in StormX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in StormX.Traits:
        $ approval_bonus -= 40
    if StormX.event_counter["forced"] and not StormX.Forced:
        $ approval_bonus -= 5*StormX.event_counter["forced"]

    if Taboo and "no_taboo" in StormX.daily_history:
        $ approval_bonus -= 10

    if "no_foot" in StormX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_foot" in StormX.recent_history else 0

    $ Approval = ApprovalCheck(StormX, 1250, TabM = 3)

    if action_context == StormX:
        if Approval > 2:
            if offhand_action == "jackin":
                "[StormX.name] lays back and starts rubbing her feet along your cock."
            else:
                "[StormX.name] gives you a mischevious smile, and starts to rub her feet along your cock."
            menu:
                "What do you do?"
                "Nothing.":
                    $ StormX.change_stat("inhibition", 70, 3)
                    $ StormX.change_stat("inhibition", 30, 2)
                    "[StormX.name] continues her actions."
                "Praise her.":
                    $ StormX.change_face("sexy", 1)
                    $ StormX.change_stat("inhibition", 70, 3)
                    ch_p "Oooh, that's good, [StormX.petname]."
                    $ StormX.nameCheck()
                    "[StormX.name] continues her actions."
                    $ StormX.change_stat("love", 80, 1)
                    $ StormX.change_stat("obedience", 90, 1)
                    $ StormX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ StormX.change_face("surprised")
                    $ StormX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that for now, [StormX.petname]."
                    $ StormX.nameCheck()
                    "[StormX.name] puts it down."
                    $ StormX.change_stat("obedience", 90, 1)
                    $ StormX.change_stat("obedience", 50, 1)
                    $ StormX.change_stat("obedience", 30, 2)
                    return
            if primary_action:
                $ girl_offhand_action = "foot"
                return
            jump Storm_FJ_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if not StormX.action_counter["footjob"] and "no_foot" not in StormX.recent_history:
        $ StormX.change_face("confused", 2)
        ch_s "Oh, you would like me to use my feet, [StormX.player_petname]?"
        $ StormX.blushing = 1

    if not StormX.action_counter["footjob"] and Approval:
        if StormX.Forced:
            $ StormX.change_face("sad",1)
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
        elif StormX.love >= (StormX.obedience + StormX.inhibition):
            $ StormX.change_face("sexy",1)
            $ StormX.brows = "sad"
            $ StormX.mouth = "smile"
            ch_s "I could enjoy that. . ."
        elif StormX.obedience >= StormX.inhibition:
            $ StormX.change_face("normal",1)
            ch_s "If you enjoy that, [StormX.player_petname]. . ."
        elif StormX.addiction >= 50:
            $ StormX.change_face("manic", 1)
            ch_s "Very well. . ."
        else:
            $ StormX.change_face("lipbite",1)
            ch_s "Very well. . ."

    elif Approval:
        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
            ch_s "That is all you want?"
        elif not Taboo and "no_taboo" in StormX.daily_history:
            ch_s "I suppose this is secluded enough. . ."
        elif "foot" in StormX.recent_history:
            $ StormX.change_face("sexy", 1)
            ch_s "I suppose so. . ."
            jump Storm_FJ_Prep
        elif "foot" in StormX.daily_history:
            $ StormX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Another?",   
                "You did not get enough earlier?",
                "My feet are rather sore from earlier.",
                "My feet are rather sore from earlier."])
            ch_s "[Line]"
        elif StormX.action_counter["footjob"] < 3:
            $ StormX.change_face("sexy", 1)
            $ StormX.brows = "confused"
            $ StormX.mouth = "kiss"
            ch_s "Oh, very well. . ."
        else:
            $ StormX.change_face("sexy", 1)
            $ StormX.ArmPose = 2
            $ Line = renpy.random.choice(["You would like me to use my feet again?",                 
                "So you would like another footjob?",                 
                "Mmmm, some. . . [she rubs her foot along your leg]?", 
                "A little foot rub?"])
            ch_s "[Line]"
        $ Line = 0

    if Approval >= 2:
        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("obedience", 90, 1)
            $ StormX.change_stat("inhibition", 60, 1)
            ch_s "I supose that would be fine."
        elif "no_foot" in StormX.daily_history:
            ch_s "Oh, very well."
        else:
            $ StormX.change_face("sexy", 1)
            $ StormX.change_stat("love", 90, 1)
            $ StormX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Hmm, I suppose.",                 
                "Fine.",                 
                "Very well, bring it out.", 
                "I suppose that I could. . .",
                "Fine. . . [She gestures for you to come over].",
                "Hmm, ok."])
            ch_s "[Line]"
            $ Line = 0
        $ StormX.change_stat("obedience", 20, 1)
        $ StormX.change_stat("obedience", 60, 1)
        $ StormX.change_stat("inhibition", 70, 2)
        jump Storm_FJ_Prep
    else:

        $ StormX.change_face("angry")
        if "no_foot" in StormX.recent_history:
            ch_s "I have made myself clear, [StormX.player_petname]."
        elif Taboo and "no_taboo" in StormX.daily_history and "no_foot" in StormX.daily_history:
            ch_s "I refuse to do this in public."
        elif "no_foot" in StormX.daily_history:
            ch_s "I said \"no,\" [StormX.player_petname]."
        elif Taboo and "no_taboo" in StormX.daily_history:
            ch_s "I informed you, not in public!"
        elif not StormX.action_counter["footjob"]:
            $ StormX.change_face("bemused")
            ch_s "I am unsure, [StormX.player_petname]. . ."
        else:
            $ StormX.change_face("bemused")
            ch_s "Not now, [StormX.player_petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_foot" in StormX.daily_history:
                $ StormX.change_face("bemused")
                ch_s "Thank you."
                return
            "Maybe later?" if "no_foot" not in StormX.daily_history:
                $ StormX.change_face("sexy")
                ch_s ". . ."
                ch_s "Perhaps."
                $ StormX.change_stat("love", 80, 2)
                $ StormX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ StormX.recent_history.append("no_taboo")
                    $ StormX.daily_history.append("no_taboo")
                $ StormX.recent_history.append("no_foot")
                $ StormX.daily_history.append("no_foot")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ StormX.change_face("sexy")
                    $ StormX.change_stat("obedience", 90, 2)
                    $ StormX.change_stat("obedience", 50, 2)
                    $ StormX.change_stat("inhibition", 70, 3)
                    $ StormX.change_stat("inhibition", 40, 2)
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
            "Come on, get to work.":

                $ Approval = ApprovalCheck(StormX, 400, "OI", TabM = 3)
                if Approval > 1 or (Approval and StormX.Forced):
                    $ StormX.change_face("sad")
                    $ StormX.change_stat("love", 70, -5, 1)
                    $ StormX.change_stat("love", 200, -2)
                    ch_s "Oh, very well."
                    $ StormX.change_stat("obedience", 50, 4)
                    $ StormX.change_stat("inhibition", 80, 1)
                    $ StormX.change_stat("inhibition", 60, 3)
                    $ StormX.Forced = 1
                    jump Storm_FJ_Prep
                else:
                    $ StormX.change_stat("love", 200, -15)
                    $ StormX.recent_history.append("angry")
                    $ StormX.daily_history.append("angry")


    $ StormX.ArmPose = 1
    if "no_foot" in StormX.daily_history:
        $ StormX.change_face("angry", 1)
        ch_s "I shall not repeat myself."
        $ StormX.recent_history.append("angry")
        $ StormX.daily_history.append("angry")
    elif StormX.Forced:
        $ StormX.change_face("angry", 1)
        ch_s "Do not tempt me to show you what my feet can do."
        $ StormX.change_stat("lust", 200, 5)
        if StormX.love > 300:
            $ StormX.change_stat("love", 70, -2)
        $ StormX.change_stat("obedience", 50, -2)
        $ StormX.recent_history.append("angry")
        $ StormX.daily_history.append("angry")
    elif Taboo:
        $ StormX.change_face("angry", 1)
        $ StormX.daily_history.append("no_taboo")
        ch_s "This truly is not an appropriate place for that."
        $ StormX.change_stat("lust", 200, 5)
        $ StormX.change_stat("obedience", 50, -3)
    elif StormX.action_counter["footjob"]:
        $ StormX.change_face("sad")
        ch_s "I am in no mood, [StormX.player_petname]. . ."
    else:
        $ StormX.change_face("normal", 1)
        ch_s "I am truly in no mood for footplay today. . ."
    $ StormX.recent_history.append("no_foot")
    $ StormX.daily_history.append("no_foot")
    $ approval_bonus = 0
    return


label Storm_FJ_Prep:
    if offhand_action == "foot":
        return

    if Taboo:
        $ StormX.inhibition += int(Taboo/10)
        $ StormX.lust += int(Taboo/5)

    $ StormX.change_face("sexy")
    if StormX.Forced:
        $ StormX.change_face("sad")
    elif not StormX.action_counter["footjob"]:
        $ StormX.brows = "confused"
        $ StormX.eyes = "sexy"
        $ StormX.mouth = "smile"

    call Seen_First_Peen (StormX, Partner, React=action_context)
    if not StormX.action_counter["footjob"]:
        if StormX.Forced:
            $ StormX.change_stat("love", 90, -20)
            $ StormX.change_stat("obedience", 70, 25)
            $ StormX.change_stat("inhibition", 80, 30)
        else:
            $ StormX.change_stat("love", 90, 5)
            $ StormX.change_stat("obedience", 70, 20)
            $ StormX.change_stat("inhibition", 80, 20)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ StormX.DrainWord("no_taboo")
    $ StormX.DrainWord("no_foot")
    $ StormX.recent_history.append("foot")
    $ StormX.daily_history.append("foot")

label Storm_FJ_Cycle:
    while Round > 0:
        call shift_focus (StormX)
        call Storm_Sex_Launch ("foot")
        $ StormX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . ." if action_speed:
                    pass

                "Start moving? . ." if not action_speed:
                    $ action_speed = 1

                "Speed up. . ." if action_speed < 2:
                    $ action_speed = 2
                    "You ask her to up the pace a bit."
                "Speed up. . . (locked)" if action_speed >= 2:
                    pass

                "Slow Down. . ." if action_speed:
                    $ action_speed -= 1
                    "You ask her to slow it down a bit."
                "Slow Down. . . (locked)" if not action_speed:
                    pass
                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "Other options":

                    menu:
                        "I also want to fondle her thighs." if offhand_action != "fondle_thighs":
                            if multi_action:
                                $ offhand_action = "fondle_thighs"
                                "You start to fondle her thighs."
                            else:
                                call Sex_Basic_Dialog (StormX, "tired")
                        "Shift primary action":

                            if StormX.remaining_actions and multi_action:
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
                                call Sex_Basic_Dialog (StormX, "tired")

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Asks [StormX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (StormX)
                                "Asks [StormX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (StormX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (StormX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Storm_FJ_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Storm_FJ_Cycle
                                "Never mind":
                                    jump Storm_FJ_Cycle
                        "Undress [StormX.name]":
                            call Girl_Undress (StormX)
                        "Clean up [StormX.name] (locked)" if not StormX.Spunk:
                            pass
                        "Clean up [StormX.name]" if StormX.Spunk:
                            call Girl_Cleanup (StormX, "ask")
                        "Never mind":
                            jump Storm_FJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Storm_Sex_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Storm_FJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Storm_Sex_Reset
                    $ Line = 0
                    jump Storm_FJ_After


        call shift_focus (StormX)
        call Sex_Dialog (StormX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or StormX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (StormX)
                if "angry" in StormX.recent_history:
                    call Storm_Sex_Reset
                    return
                $ StormX.change_stat("lust", 200, 5)
                if 100 > StormX.lust >= 70 and StormX.session_orgasms < 2:
                    $ StormX.recent_history.append("unsatisfied")
                    $ StormX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Storm_FJ_After
                $ Line = "came"

            if StormX.lust >= 100:

                call Girl_Cumming (StormX)
                if action_context == "shift" or "angry" in StormX.recent_history:
                    jump Storm_FJ_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in StormX.recent_history:
                    "[StormX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Storm_FJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if counter == 20:
            $ StormX.brows = "angry"
            menu:
                ch_s "Hmm, foot cramp. Could we take a short break?"
                "How about a BJ?" if StormX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Storm_FJ_After
                    call Storm_Blowjob
                "How about a Handy?" if StormX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Storm_FJ_After
                    call Storm_Handjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    $ counter += 1
                    "[Line]"
                    jump Storm_FJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Storm_Sex_Reset
                    $ action_context = "shift"
                    jump Storm_FJ_After
                "No, keep going.":
                    if ApprovalCheck(StormX, 1200) or ApprovalCheck(StormX, 500, "O"):
                        $ StormX.change_stat("love", 200, -5)
                        $ StormX.change_stat("obedience", 50, 3)
                        $ StormX.change_stat("obedience", 80, 2)
                        "She grumbles but gets back to work."
                    else:
                        $ StormX.change_face("angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        ch_s "I do have better things I could be doing."
                        $ StormX.change_stat("love", 50, -3, 1)
                        $ StormX.change_stat("love", 80, -4, 1)
                        $ StormX.change_stat("obedience", 30, -1, 1)
                        $ StormX.change_stat("obedience", 50, -1, 1)
                        $ StormX.recent_history.append("angry")
                        $ StormX.daily_history.append("angry")
                        jump Storm_FJ_After
        elif counter == 10 and StormX.SEXP <= 100 and not ApprovalCheck(StormX, 1200, "LO"):
            $ StormX.brows = "confused"
            ch_s "Could we be done here, my feet are getting sore."


        call Escalation (StormX)

        if Round == 10:
            call Sex_Basic_Dialog (StormX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (StormX, 5)


    $ StormX.change_face("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (StormX, "done")

label Storm_FJ_After:
    $ StormX.change_face("sexy")

    $ StormX.action_counter["footjob"] += 1
    $ StormX.remaining_actions -=1
    $ StormX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ StormX.addiction_rate += 1
    $ StormX.change_stat("lust", 90, 5)

    call Partner_Like (StormX, 1)

    if "Stormpedi" in Achievements:
        pass
    elif StormX.action_counter["footjob"] >= 10:
        $ StormX.change_face("smile", 1)
        ch_s "I am glad that you convinced me to try this."
        ch_s "It feels so. . . intimate."
        $ Achievements.append("Stormpedi")
        $ StormX.SEXP += 5
    elif StormX.action_counter["footjob"] == 1:
        $ StormX.SEXP += 10
        if StormX.love >= 500:
            $ StormX.mouth = "smile"
            ch_s "That certainly was an interesting experience. . ."
        elif Player.focus <= 20:
            $ StormX.mouth = "sad"
            ch_s "Did you enjoy that?"
    elif StormX.action_counter["footjob"] == 5:
        ch_s "I'm enjoying this experience."

    $ approval_bonus = 0
    if action_context == "shift":
        ch_s "Ok then, what were you thinking?"
    else:
        call Storm_Sex_Reset
    call Checkout
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
