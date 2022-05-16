
label Laura_Handjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (LauraX)
    if LauraX.action_counter["handjob"] >= 7:
        $ approval_bonus += 10
    elif LauraX.action_counter["handjob"] >= 3:
        $ approval_bonus += 7
    elif LauraX.action_counter["handjob"]:
        $ approval_bonus += 3

    if LauraX.addiction >= 75 and LauraX.event_counter["swallowed"] >=3:
        $ approval_bonus += 15
    if LauraX.addiction >= 75:
        $ approval_bonus += 5

    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in LauraX.traits:
        $ approval_bonus += (3*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in LauraX.traits:
        $ approval_bonus -= 40
    if LauraX.event_counter["forced"] and not LauraX.Forced:
        $ approval_bonus -= 5*LauraX.event_counter["forced"]

    if Taboo and "no_taboo" in LauraX.daily_history:
        $ approval_bonus -= 10

    if "no_handjob" in LauraX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_handjob" in LauraX.recent_history else 0

    $ approval = approval_check(LauraX, 1100, TabM = 3)

    if not LauraX.action_counter["handjob"] and "no_handjob" not in LauraX.recent_history:
        $ LauraX.change_face("confused", 2)
        ch_l "Handjob, huh. . ."
        $ LauraX.blushing = 1

    if not LauraX.action_counter["handjob"] and approval:
        if LauraX.Forced:
            $ LauraX.change_face("sad",1)
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
        elif LauraX.love >= (LauraX.obedience + LauraX.inhibition):
            $ LauraX.change_face("sexy",1)
            $ LauraX.brows = "sad"
            $ LauraX.mouth = "smile"
            ch_l "You'd like that. . ."
        elif LauraX.obedience >= LauraX.inhibition:
            $ LauraX.change_face("normal",1)
            ch_l "If you want, [LauraX.player_petname]. . ."
        else:
            $ LauraX.change_face("lipbite",1)
            ch_l "Hmm. . ."

    elif approval:
        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
            ch_l "Nothing more than that?"
        elif not Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "Well,this is a bit more secure. . ."
        elif "handjob" in LauraX.recent_history:
            $ LauraX.change_face("sexy", 1)
            ch_l "Hmm, another handy then. . ."
            jump Laura_HJ_Prep
        elif "handjob" in LauraX.daily_history:
            $ LauraX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Another one?",   
                "I'm glad I don't grow calluses.", 
                "Didn't get enough earlier?",
                "Again the with handjobs, huh?",
                "I guess you want more."])
            ch_l "[Line]"
        elif LauraX.action_counter["handjob"] < 3:
            $ LauraX.change_face("sexy", 1)
            $ LauraX.brows = "confused"
            $ LauraX.mouth = "kiss"
            ch_l "You seem to like this one. . ."
        else:
            $ LauraX.change_face("sexy", 1)
            $ LauraX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some more?",                 
                "So you'd like another handy?",                 
                "You want a. . . [fist pumping hand gestures]?", 
                "Another handjob?"])
            ch_l "[Line]"
        $ Line = 0

    if approval >= 2:
        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("obedience", 90, 1)
            $ LauraX.change_stat("inhibition", 60, 1)
            ch_l "Ok, fine."
        elif "no_handjob" in LauraX.daily_history:
            ch_l "If it'll get you off my back. . ."
        else:
            $ LauraX.change_face("sexy", 1)
            $ LauraX.change_stat("love", 90, 1)
            $ LauraX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Sure, I guess.",                 
                "O-kay.",                 
                "Fine.", 
                "I suppose I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Ok, ok."])
            ch_l "[Line]"
            $ Line = 0
        $ LauraX.change_stat("obedience", 20, 1)
        $ LauraX.change_stat("obedience", 60, 1)
        $ LauraX.change_stat("inhibition", 70, 2)
        jump Laura_HJ_Prep
    else:

        $ LauraX.change_face("angry")
        if "no_handjob" in LauraX.recent_history:
            ch_l "I just told you no, [LauraX.player_petname]."
        elif Taboo and "no_taboo" in LauraX.daily_history and "no_handjob" in LauraX.daily_history:
            ch_l "I said not in public."
        elif "no_handjob" in LauraX.daily_history:
            ch_l "I told you \"no,\" [LauraX.player_petname]."
        elif Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "I said not in public."
        elif not LauraX.action_counter["handjob"]:
            $ LauraX.change_face("bemused")
            ch_l "Seriously, [LauraX.player_petname]. . ."
        else:
            $ LauraX.change_face("bemused")
            ch_l "Nah."
        menu:
            extend ""
            "Sorry, never mind." if "no_handjob" in LauraX.daily_history:
                $ LauraX.change_face("bemused")
                ch_l "It's fine."
                return
            "Maybe later?" if "no_handjob" not in LauraX.daily_history:
                $ LauraX.change_face("bemused")
                ch_l "Maybe."
                $ LauraX.change_stat("love", 80, 2)
                $ LauraX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ LauraX.recent_history.append("no_taboo")
                    $ LauraX.daily_history.append("no_taboo")
                $ LauraX.recent_history.append("no_handjob")
                $ LauraX.daily_history.append("no_handjob")
                return
            "I'd really appreciate it. . .":
                if approval:
                    $ LauraX.change_face("sexy")
                    $ LauraX.change_stat("obedience", 90, 2)
                    $ LauraX.change_stat("obedience", 50, 2)
                    $ LauraX.change_stat("inhibition", 70, 3)
                    $ LauraX.change_stat("inhibition", 40, 2)
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
            "Come on, get to work.":

                $ approval = approval_check(LauraX, 350, "OI", TabM = 3)
                if approval > 1 or (approval and LauraX.Forced):
                    $ LauraX.change_face("sad")
                    $ LauraX.change_stat("love", 70, -5, 1)
                    $ LauraX.change_stat("love", 200, -2)
                    ch_l "Ok, fine."
                    $ LauraX.change_stat("obedience", 50, 4)
                    $ LauraX.change_stat("inhibition", 80, 1)
                    $ LauraX.change_stat("inhibition", 60, 3)
                    $ LauraX.Forced = 1
                    jump Laura_HJ_Prep
                else:
                    $ LauraX.change_stat("love", 200, -15)
                    $ LauraX.recent_history.append("angry")
                    $ LauraX.daily_history.append("angry")


    $ LauraX.ArmPose = 1
    if "no_handjob" in LauraX.daily_history:
        $ LauraX.change_face("angry", 1)
        ch_l "Don't ask again."
        $ LauraX.recent_history.append("angry")
        $ LauraX.daily_history.append("angry")
    elif LauraX.Forced:
        $ LauraX.change_face("angry", 1)
        ch_l "No."
        $ LauraX.change_stat("lust", 200, 5)
        if LauraX.love > 300:
            $ LauraX.change_stat("love", 70, -2)
        $ LauraX.change_stat("obedience", 50, -2)
        $ LauraX.recent_history.append("angry")
        $ LauraX.daily_history.append("angry")
    elif Taboo:
        $ LauraX.change_face("angry", 1)
        $ LauraX.daily_history.append("no_taboo")
        ch_l "This area's too exposed."
        $ LauraX.change_stat("lust", 200, 5)
        $ LauraX.change_stat("obedience", 50, -3)
    elif LauraX.action_counter["handjob"]:
        $ LauraX.change_face("sad")
        ch_l "I'm not into it today. . ."
    else:
        $ LauraX.change_face("normal", 1)
        ch_l "I don't know where that's been lately."
    $ LauraX.recent_history.append("no_handjob")
    $ LauraX.daily_history.append("no_handjob")
    $ approval_bonus = 0
    return


label Laura_HJ_Prep:
    if offhand_action == "handjob":
        return

    if Taboo:
        $ LauraX.inhibition += int(Taboo/10)
        $ LauraX.lust += int(Taboo/5)

    $ LauraX.change_face("sexy")
    if LauraX.Forced:
        $ LauraX.change_face("sad")
    elif not LauraX.action_counter["handjob"]:
        $ LauraX.brows = "confused"
        $ LauraX.eyes = "sexy"
        $ LauraX.mouth = "smile"

    call Seen_First_Peen (LauraX, Partner, React=action_context)
    call Laura_HJ_Launch ("L")

    if action_context == LauraX:

        $ action_context = 0
        if offhand_action == "jackin":
            "[LauraX.name] brushes your hand aside and starts stroking your cock."
        else:
            "[LauraX.name] gives you a mischevious smile, and starts to fondle your cock."
        menu:
            "What do you do?"
            "Nothing.":
                $ LauraX.change_stat("inhibition", 70, 3)
                $ LauraX.change_stat("inhibition", 30, 2)
                "[LauraX.name] continues her actions."
            "Praise her.":
                $ LauraX.change_face("sexy", 1)
                $ LauraX.change_stat("inhibition", 70, 3)
                ch_p "Oooh, that's good, [LauraX.petname]."
                $ LauraX.nameCheck()
                "[LauraX.name] continues her actions."
                $ LauraX.change_stat("love", 80, 1)
                $ LauraX.change_stat("obedience", 90, 1)
                $ LauraX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ LauraX.change_face("surprised")
                $ LauraX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that for now, [LauraX.petname]."
                $ LauraX.nameCheck()
                "[LauraX.name] puts it down."
                $ LauraX.change_stat("obedience", 90, 1)
                $ LauraX.change_stat("obedience", 50, 1)
                $ LauraX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ LauraX.add_word(1,"refused","refused")
                return

    if not LauraX.action_counter["handjob"]:
        if LauraX.Forced:
            $ LauraX.change_stat("love", 90, -20)
            $ LauraX.change_stat("obedience", 70, 25)
            $ LauraX.change_stat("inhibition", 80, 30)
        else:
            $ LauraX.change_stat("love", 90, 5)
            $ LauraX.change_stat("obedience", 70, 20)
            $ LauraX.change_stat("inhibition", 80, 20)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ LauraX.drain_word("no_taboo")
    $ LauraX.drain_word("no_handjob")
    $ LauraX.recent_history.append("handjob")
    $ LauraX.daily_history.append("handjob")

label Laura_HJ_Cycle:
    while Round > 0:
        call shift_focus (LauraX)
        call Laura_HJ_Launch
        $ LauraX.lust_face()

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
                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "Other options":

                    menu:
                        "I also want to fondle her breasts." if offhand_action != "fondle_breasts":
                            if LauraX.remaining_actions and multi_action:
                                $ offhand_action = "fondle_breasts"
                                "You start to fondle her breasts."
                                $ LauraX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (LauraX, "tired")
                        "Shift primary action":

                            if LauraX.remaining_actions and multi_action:
                                menu:
                                    "How about a blowjob?":
                                        if LauraX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Laura_HJ_After
                                            call Laura_Blowjob
                                        else:
                                            call Sex_Basic_Dialog (LauraX, "tired")
                                    "How about a titjob?":

                                        if LauraX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Laura_HJ_After
                                            call Laura_Titjob
                                        else:
                                            call Sex_Basic_Dialog (LauraX, "tired")
                                    "Never Mind":
                                        jump Laura_HJ_Cycle
                            else:
                                call Sex_Basic_Dialog (LauraX, "tired")

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [LauraX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (LauraX)
                                "Ask [LauraX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (LauraX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (LauraX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Laura_HJ_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Laura_HJ_Cycle
                                "Never mind":
                                    jump Laura_HJ_Cycle
                        "undress [LauraX.name]":
                            call Girl_Undress (LauraX)
                        "Clean up [LauraX.name] (locked)" if not LauraX.spunk:
                            pass
                        "Clean up [LauraX.name]" if LauraX.spunk:
                            call Girl_Cleanup (LauraX, "ask")
                        "Never mind":
                            jump Laura_HJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Laura_HJ_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Laura_HJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Laura_HJ_Reset
                    $ Line = 0
                    jump Laura_HJ_After


        call shift_focus (LauraX)
        call Sex_Dialog (LauraX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or LauraX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (LauraX)
                if "angry" in LauraX.recent_history:
                    call Laura_HJ_Reset
                    return
                $ LauraX.change_stat("lust", 200, 5)
                if 100 > LauraX.lust >= 70 and LauraX.session_orgasms < 2 and LauraX.SEXP >= 20:
                    $ LauraX.recent_history.append("unsatisfied")
                    $ LauraX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Laura_HJ_After
                $ Line = "came"

            if LauraX.lust >= 100:

                call Girl_Cumming (LauraX)
                if action_context == "shift" or "angry" in LauraX.recent_history:
                    jump Laura_HJ_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in LauraX.recent_history:
                    "[LauraX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Laura_HJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if counter == 20:
            $ LauraX.brows = "angry"
            menu:
                ch_l "Hmm, this is boring, can we take a break?"
                "How about a BJ?" if LauraX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Laura_HJ_After
                    call Laura_Blowjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    jump Laura_HJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Laura_HJ_Reset
                    $ action_context = "shift"
                    jump Laura_HJ_After
                "No, get back down there.":
                    if approval_check(LauraX, 1200) or approval_check(LauraX, 500, "O"):
                        $ LauraX.change_stat("love", 200, -5)
                        $ LauraX.change_stat("obedience", 50, 3)
                        $ LauraX.change_stat("obedience", 80, 2)
                        "She grumbles but gets back to work."
                    else:
                        $ LauraX.change_face("angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        ch_l "I have better things to do with my time."
                        $ LauraX.change_stat("love", 50, -3, 1)
                        $ LauraX.change_stat("love", 80, -4, 1)
                        $ LauraX.change_stat("obedience", 30, -1, 1)
                        $ LauraX.change_stat("obedience", 50, -1, 1)
                        $ LauraX.recent_history.append("angry")
                        $ LauraX.daily_history.append("angry")
                        jump Laura_HJ_After
        elif counter == 10 and LauraX.SEXP <= 100 and not approval_check(LauraX, 1200, "LO"):
            $ LauraX.brows = "confused"
            ch_l "This working for you?"


        call Escalation (LauraX)

        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [LauraX.player_petname]."


    $ LauraX.change_face("bemused", 0)
    $ Line = 0
    ch_l "Ok, [LauraX.player_petname], breaktime."

label Laura_HJ_After:
    $ LauraX.change_face("sexy")

    $ LauraX.action_counter["handjob"] += 1
    $ LauraX.remaining_actions -=1
    $ LauraX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ LauraX.addiction_rate += 1
    $ LauraX.change_stat("lust", 90, 5)

    call Partner_Like (LauraX, 1)

    if "Laura Handi-Queen" in Achievements:
        pass
    elif LauraX.action_counter["handjob"] >= 10:
        $ LauraX.change_face("smile", 1)
        ch_l "Looks like you filled out the punch card, [LauraX.player_petname]."
        $ Achievements.append("Laura Handi-Queen")
        $ LauraX.SEXP += 5
    elif LauraX.action_counter["handjob"] == 1:
        $ LauraX.SEXP += 10
        if LauraX.love >= 500:
            $ LauraX.mouth = "smile"
            ch_l "That was kind of. . . pleasant. . ."
        elif Player.focus <= 20:
            $ LauraX.mouth = "sad"
            ch_l "Did that do it for you?"
    elif LauraX.action_counter["handjob"] == 5:
        ch_l "I think I've got this down, maybe I should get a punch card."

    $ approval_bonus = 0
    if action_context == "shift":
        ch_l "Ok, so what did you have in mind?"
    else:
        call Laura_HJ_Reset
    call checkout
    return





label Laura_Titjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (LauraX)
    if LauraX.action_counter["titjob"] >= 7:
        $ approval_bonus += 10
    elif LauraX.action_counter["titjob"] >= 3:
        $ approval_bonus += 7
    elif LauraX.action_counter["titjob"]:
        $ approval_bonus += 5

    if LauraX.addiction >= 75 and LauraX.event_counter["swallowed"] >=3:
        $ approval_bonus += 15
    elif LauraX.addiction >= 75:
        $ approval_bonus += 5

    if LauraX.SeenChest and approval_check(LauraX, 500):
        $ approval_bonus += 10
    if not LauraX.bra and not LauraX.top:
        $ approval_bonus += 10
    if LauraX.lust > 75:
        $ approval_bonus += 10
    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in LauraX.traits:
        $ approval_bonus += (5*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in LauraX.traits:
        $ approval_bonus -= 30
    if LauraX.event_counter["forced"] and not LauraX.Forced:
        $ approval_bonus -= 5*LauraX.event_counter["forced"]

    if Taboo and "no_taboo" in LauraX.daily_history:
        $ approval_bonus -= 10

    if "no_titjob" in LauraX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_titjob" in LauraX.recent_history else 0

    $ approval = approval_check(LauraX, 1200, TabM = 4)

    if not LauraX.action_counter["titjob"] and "no_titjob" not in LauraX.recent_history:
        $ LauraX.change_face("surprised", 1)
        $ LauraX.mouth = "kiss"
        ch_l "You want a titjob, huh?"

    if not LauraX.action_counter["titjob"] and approval:
        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
        elif LauraX.love >= (LauraX.obedience + LauraX.inhibition):
            $ LauraX.change_face("sexy")
            $ LauraX.brows = "sad"
            $ LauraX.mouth = "smile"
            ch_l "Well, maybe you deserve it."
        elif LauraX.obedience >= LauraX.inhibition:
            $ LauraX.change_face("normal")
            ch_l "If you'd like that. . ."
        elif LauraX.addiction >= 50:
            $ LauraX.change_face("manic", 1)
            ch_l "Hmmmm. . . ."
        else:
            $ LauraX.change_face("sad")
            $ LauraX.mouth = "smile"
            ch_l "Sounds fun. . ."
    elif approval:
        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
            ch_l "You're kinda pushing it."
        elif not Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "Ok, I guess this is secluded enough. . ."
        elif "titjob" in LauraX.recent_history:
            $ LauraX.change_face("sexy", 1)
            ch_l "Huh, again?"
            jump Laura_TJ_Prep
        elif "titjob" in LauraX.daily_history:
            $ LauraX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Back for more?",   
                "You're really working these puppies.", 
                "Didn't get enough earlier?",  
                "You're really working these puppies."])
            ch_l "[Line]"
        elif LauraX.action_counter["titjob"] < 3:
            $ LauraX.change_face("sexy", 1)
            $ LauraX.brows = "confused"
            $ LauraX.mouth = "kiss"
            ch_l "Another titjob??"
        else:
            $ LauraX.change_face("sexy", 1)
            $ LauraX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action [rubs her chest]?",                 
                "So you'd like another titjob?",                  
                "So you'd like another titjob?",                               
                "So you'd like another titjob?",                              
                "Another titjob?", 
                "A little [points at her chest]?"])
            ch_l "[Line]"
        $ Line = 0

    if approval >= 2:
        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("obedience", 90, 1)
            $ LauraX.change_stat("inhibition", 60, 1)
            ch_l "Well, could be worse. . ."
        elif "no_titjob" in LauraX.daily_history:
            ch_l "Hmm, I guess. . ."
        else:
            $ LauraX.change_face("sexy", 1)
            $ LauraX.change_stat("love", 90, 1)
            $ LauraX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, put it here.",                 
                "Well. . . ok.",                 
                "Yum.", 
                "Sure, whip it out.",
                "Fine. . . [She drools a bit into her cleavage].",
                "Heh, ok."])
            ch_l "[Line]"
            $ Line = 0
        $ LauraX.change_stat("obedience", 20, 1)
        $ LauraX.change_stat("obedience", 70, 1)
        $ LauraX.change_stat("inhibition", 80, 2)
        jump Laura_TJ_Prep
    else:

        $ LauraX.change_face("angry")
        if "no_titjob" in LauraX.recent_history:
            ch_l "I {i}just{/i} told you \"no,\" [LauraX.player_petname]."
        elif Taboo and "no_taboo" in LauraX.daily_history and "no_titjob" in LauraX.daily_history:
            ch_l "This is just way too exposed!"
        elif "no_titjob" in LauraX.daily_history:
            ch_l "I already told you \"no,\" [LauraX.player_petname]."
        elif Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "This is just way too exposed!"
        elif not LauraX.action_counter["titjob"]:
            $ LauraX.change_face("bemused")
            ch_l "I'm not really into that, [LauraX.player_petname]. . ."
        else:
            $ LauraX.change_face("bemused")
            ch_l "Not right now [LauraX.player_petname]. . ."

        menu:
            extend ""
            "Sorry, never mind." if "no_titjob" in LauraX.daily_history:
                $ LauraX.change_face("bemused")
                ch_l "Yeah, ok, [LauraX.player_petname]."
                return
            "Maybe later?" if "no_titjob" not in LauraX.daily_history:
                $ LauraX.change_face("sexy")
                ch_l "Maybe."
                $ LauraX.change_stat("love", 80, 2)
                $ LauraX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ LauraX.recent_history.append("no_taboo")
                    $ LauraX.daily_history.append("no_taboo")
                $ LauraX.recent_history.append("no_titjob")
                $ LauraX.daily_history.append("no_titjob")
                return
            "I think this could be fun for both of us. . .":
                if approval:
                    $ LauraX.change_face("sexy")
                    $ LauraX.change_stat("obedience", 80, 2)
                    $ LauraX.change_stat("obedience", 40, 2)
                    $ LauraX.change_stat("inhibition", 70, 3)
                    $ LauraX.change_stat("inhibition", 40, 2)
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
                    $ approval = approval_check(LauraX, 1100, TabM = 3)
                    if approval >= 2 and LauraX.action_counter["blowjob"]:
                        $ LauraX.change_stat("inhibition", 80, 1)
                        $ LauraX.change_stat("inhibition", 60, 3)
                        $ LauraX.change_face("confused", 1)
                        ch_l "I could maybe blow you?"
                        menu:
                            ch_l "How about that [[blowjob]?"
                            "Ok, get down there.":
                                $ LauraX.change_stat("love", 80, 2)
                                $ LauraX.change_stat("inhibition", 60, 1)
                                $ LauraX.change_stat("obedience", 50, 1)
                                jump Laura_BJ_Prep
                            "Nah, it's all about dem titties.":
                                $ Line = "no_BJ"
                    if approval and LauraX.action_counter["handjob"]:
                        $ LauraX.change_stat("inhibition", 80, 1)
                        $ LauraX.change_stat("inhibition", 60, 3)
                        $ LauraX.change_face("confused", 1)
                        ch_l "I could give you a handy?"
                        menu:
                            ch_l "What do you say?"
                            "Sure, that's fine.":
                                $ LauraX.change_stat("love", 80, 2)
                                $ LauraX.change_stat("inhibition", 60, 1)
                                $ LauraX.change_stat("obedience", 50, 1)
                                jump Laura_HJ_Prep
                            "Seriously, titties." if Line == "no_BJ":
                                $ Line = 0
                            "Nah, it's all about dem titties." if Line != "no_BJ":
                                pass
                    $ LauraX.change_stat("love", 200, -2)
                    ch_l "Nah."
                    $ LauraX.change_stat("obedience", 70, 2)
            "Come on, let me fuck those titties, [LauraX.petname]":


                $ LauraX.nameCheck()
                $ approval = approval_check(LauraX, 700, "OI", TabM = 4)
                if approval > 1 or (approval and LauraX.Forced):
                    $ LauraX.change_face("sad")
                    $ LauraX.change_stat("love", 70, -5, 1)
                    $ LauraX.change_stat("love", 200, -2)
                    ch_l "Ok, fine, whip it out."
                    $ LauraX.change_stat("obedience", 50, 4)
                    $ LauraX.change_stat("inhibition", 80, 1)
                    $ LauraX.change_stat("inhibition", 60, 3)
                    $ LauraX.Forced = 1
                    jump Laura_TJ_Prep
                else:
                    $ LauraX.change_stat("love", 200, -15)
                    $ LauraX.recent_history.append("angry")
                    $ LauraX.daily_history.append("angry")


    if "no_titjob" in LauraX.daily_history:
        $ LauraX.change_face("angry", 1)
        ch_l "Look, I already told you no."
        $ LauraX.recent_history.append("angry")
        $ LauraX.daily_history.append("angry")
    elif LauraX.Forced:
        $ LauraX.change_face("angry", 1)
        ch_l "No, try something else."
        $ LauraX.change_stat("lust", 200, 5)
        if LauraX.love > 300:
            $ LauraX.change_stat("love", 70, -2)
        $ LauraX.change_stat("obedience", 50, -2)
        $ LauraX.recent_history.append("angry")
        $ LauraX.daily_history.append("angry")
    elif Taboo:
        $ LauraX.change_face("angry", 1)
        $ LauraX.daily_history.append("no_taboo")
        ch_l "You really expect me to do that here? This isn't exactly \"covert.\""
        $ LauraX.change_stat("lust", 200, 5)
        $ LauraX.change_stat("obedience", 50, -3)
    elif LauraX.action_counter["titjob"]:
        $ LauraX.change_face("sad")
        ch_l "You'll know when it's time for that."
    else:
        $ LauraX.change_face("normal", 1)
        ch_l "Nah."
    $ LauraX.recent_history.append("no_titjob")
    $ LauraX.daily_history.append("no_titjob")
    $ approval_bonus = 0
    return

label Laura_TJ_Prep:

    if Taboo:
        $ LauraX.inhibition += int(Taboo/10)
        $ LauraX.lust += int(Taboo/5)


    $ LauraX.change_face("sexy")
    if LauraX.Forced:
        $ LauraX.change_face("sad")
    elif not LauraX.action_counter["titjob"]:
        $ LauraX.brows = "confused"
        $ LauraX.eyes = "sexy"
        $ LauraX.mouth = "smile"

    call Seen_First_Peen (LauraX, Partner, React=action_context)
    call Laura_TJ_Launch ("L")

    if action_context == LauraX:

        $ action_context = 0
        "[LauraX.name] slides down and sandwiches your dick between her tits."
        menu:
            "What do you do?"
            "Nothing.":
                $ LauraX.change_stat("inhibition", 80, 3)
                $ LauraX.change_stat("inhibition", 40, 2)
                "[LauraX.name] starts to slide them up and down."
            "Praise her.":
                $ LauraX.change_face("sexy", 1)
                $ LauraX.change_stat("inhibition", 80, 3)
                ch_p "Oh, that sounds like a good idea, [LauraX.petname]."
                $ LauraX.nameCheck()
                "[LauraX.name] continues her actions."
                $ LauraX.change_stat("love", 85, 1)
                $ LauraX.change_stat("obedience", 90, 1)
                $ LauraX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ LauraX.change_face("confused")
                $ LauraX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that for now, [LauraX.petname]."
                $ LauraX.nameCheck()
                "[LauraX.name] lets it drop out from between her breasts."
                $ LauraX.change_stat("obedience", 90, 1)
                $ LauraX.change_stat("obedience", 50, 3)
                $ Player.recent_history.append("nope")
                $ LauraX.add_word(1,"refused","refused")
                return

    if not LauraX.action_counter["titjob"]:
        if LauraX.Forced:
            $ LauraX.change_stat("love", 90, -25)
            $ LauraX.change_stat("obedience", 70, 30)
            $ LauraX.change_stat("inhibition", 80, 35)
        else:
            $ LauraX.change_stat("love", 90, 5)
            $ LauraX.change_stat("obedience", 70, 25)
            $ LauraX.change_stat("inhibition", 80, 30)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ LauraX.drain_word("no_taboo")
    $ LauraX.drain_word("no_titjob")
    $ LauraX.recent_history.append("titjob")
    $ LauraX.daily_history.append("titjob")

label Laura_TJ_Cycle:
    while Round > 0:
        call shift_focus (LauraX)
        call Laura_TJ_Launch
        $ LauraX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . ." if action_speed:
                    pass

                "Start moving? . ." if action_speed == 0:
                    call action_speed_Shift (1)

                "Speed up. . ." if action_speed == 1:
                    call action_speed_Shift (2)
                    "You ask her to up the pace a bit."
                "Speed up. . . (locked)" if action_speed >= 2:
                    pass

                "Stop moving" if action_speed != 0:
                    call action_speed_Shift (0)
                "Slow Down. . ." if action_speed == 2:
                    call action_speed_Shift (1)
                    "You ask her to slow it down a bit."
                "Slow Down. . . (locked)" if not action_speed:
                    pass


                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "Other options":

                    menu:
                        "I also want to fondle her breasts." if offhand_action != "fondle_breasts":
                            if LauraX.remaining_actions and multi_action:
                                $ offhand_action = "fondle_breasts"
                                "You start to fondle her breasts."
                                $ LauraX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (LauraX, "tired")
                        "Shift primary action":

                            if LauraX.remaining_actions and multi_action:
                                menu:
                                    "How about a blowjob?":
                                        if LauraX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Laura_TJ_After
                                            call Laura_Blowjob
                                        else:
                                            call Sex_Basic_Dialog (LauraX, "tired")
                                    "How about a handy?":

                                        if LauraX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Laura_BJ_After
                                            call Laura_Handjob
                                        else:
                                            call Sex_Basic_Dialog (LauraX, "tired")
                                    "Never Mind":
                                        jump Laura_TJ_Cycle
                            else:
                                call Sex_Basic_Dialog (LauraX, "tired")

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [LauraX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (LauraX)
                                "Ask [LauraX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (LauraX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (LauraX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Laura_TJ_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Laura_TJ_Cycle
                                "Never mind":
                                    jump Laura_TJ_Cycle
                        "undress [LauraX.name]":
                            call Girl_Undress (LauraX)
                        "Clean up [LauraX.name] (locked)" if not LauraX.spunk:
                            pass
                        "Clean up [LauraX.name]" if LauraX.spunk:
                            call Girl_Cleanup (LauraX, "ask")
                        "Never mind":
                            jump Laura_TJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Laura_TJ_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Laura_TJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Laura_TJ_Reset
                    $ Line = 0
                    jump Laura_TJ_After


        call shift_focus (LauraX)
        call Sex_Dialog (LauraX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or LauraX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (LauraX)
                if "angry" in LauraX.recent_history:
                    call Laura_TJ_Reset
                    return
                $ LauraX.change_stat("lust", 200, 5)
                if 100 > LauraX.lust >= 70 and LauraX.session_orgasms < 2 and LauraX.SEXP >= 20:
                    $ LauraX.recent_history.append("unsatisfied")
                    $ LauraX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Laura_TJ_After
                $ Line = "came"

            if LauraX.lust >= 100:

                call Girl_Cumming (LauraX)
                if action_context == "shift" or "angry" in LauraX.recent_history:
                    jump Laura_TJ_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in LauraX.recent_history:
                    "[LauraX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Laura_TJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)
        if action_speed >= 4:
            call action_speed_Shift (0)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if LauraX.SEXP >= 100 or approval_check(LauraX, 1200, "LO"):
            pass
        elif counter == (5 + LauraX.action_counter["titjob"]):
            $ LauraX.brows = "confused"
            ch_l "Are you getting close here? I'm getting bored."
        if counter == (10 + LauraX.action_counter["titjob"]):
            $ LauraX.brows = "angry"
            menu:
                ch_l "Seriously, can we do something else?"
                "How about a BJ?" if LauraX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Laura_TJ_After
                    call Laura_Blowjob
                    return
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    jump Laura_TJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Laura_TJ_Reset
                    $ action_context = "shift"
                    jump Laura_TJ_After
                "No, get back down there.":
                    if approval_check(LauraX, 1200) or approval_check(LauraX, 500, "O"):
                        $ LauraX.change_stat("love", 200, -5)
                        $ LauraX.change_stat("obedience", 50, 3)
                        $ LauraX.change_stat("obedience", 80, 2)
                        "She grumbles but gets back to work."
                    else:
                        $ LauraX.change_face("angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        ch_l "Well fuck you then."
                        $ LauraX.change_stat("love", 50, -3, 1)
                        $ LauraX.change_stat("love", 80, -4, 1)
                        $ LauraX.change_stat("obedience", 30, -1, 1)
                        $ LauraX.change_stat("obedience", 50, -1, 1)
                        $ LauraX.recent_history.append("angry")
                        $ LauraX.daily_history.append("angry")
                        jump Laura_TJ_After


        call Escalation (LauraX)

        if Round == 10:
            ch_l "It's kinda time to get moving."
        elif Round == 5:
            ch_l "Tic tock, [LauraX.player_petname]."


    $ LauraX.change_face("bemused", 0)
    $ Line = 0
    ch_l "Ok, [LauraX.player_petname], breaktime."

label Laura_TJ_After:
    $ LauraX.change_face("sexy")

    $ LauraX.action_counter["titjob"] += 1
    $ LauraX.remaining_actions -=1
    $ LauraX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ LauraX.addiction_rate += 1

    call Partner_Like (LauraX, 4)

    if LauraX.action_counter["titjob"] > 5:
        pass
    elif LauraX.action_counter["titjob"] == 1:
        $ LauraX.SEXP += 12
        if LauraX.love >= 500:
            $ LauraX.mouth = "smile"
            ch_l "That was fun."
        elif Player.focus <= 20:
            $ LauraX.mouth = "sad"
            ch_l "Well I hope you got something out of that."
    elif LauraX.action_counter["titjob"] == 5:
        ch_l "You seem to enjoy that."

    $ approval_bonus = 0

    if action_context == "shift":
        ch_l "Mmm, so what else did you have in mind?"
    else:
        call Laura_TJ_Reset
    call checkout
    return







label Laura_Blowjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (LauraX)
    if LauraX.action_counter["blowjob"] >= 7:
        $ approval_bonus += 15
    elif LauraX.action_counter["blowjob"] >= 3:
        $ approval_bonus += 10
    elif LauraX.action_counter["blowjob"]:
        $ approval_bonus += 7

    if LauraX.addiction >= 75 and LauraX.event_counter["swallowed"] >=3:
        $ approval_bonus += 25
    elif LauraX.addiction >= 75:
        $ approval_bonus += 15

    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in LauraX.traits:
        $ approval_bonus += (4*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in LauraX.traits:
        $ approval_bonus -= 40
    if LauraX.event_counter["forced"] and not LauraX.Forced:
        $ approval_bonus -= 5*LauraX.event_counter["forced"]

    if Taboo and "no_taboo" in LauraX.daily_history:
        $ approval_bonus -= 10

    if "no_blowjob" in LauraX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_blowjob" in LauraX.recent_history else 0

    $ approval = approval_check(LauraX, 1300, TabM = 4)

    if not LauraX.action_counter["blowjob"] and "no_blowjob" not in LauraX.recent_history:
        $ LauraX.change_face("surprised", 2)
        $ LauraX.mouth = "kiss"
        ch_l "You want me to suck your cock?"
        if LauraX.action_counter["handjob"]:
            $ LauraX.mouth = "smile"
            ch_l "Handjobs not enough now?"
        $ LauraX.blushing = 1

    if not LauraX.action_counter["blowjob"] and approval:
        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
        elif LauraX.love >= (LauraX.obedience + LauraX.inhibition):
            $ LauraX.change_face("sexy")
            $ LauraX.brows = "sad"
            $ LauraX.mouth = "smile"
            ch_l "I have wondered how you taste."
        elif LauraX.obedience >= LauraX.inhibition:
            $ LauraX.change_face("normal")
            ch_l "If that's what you want. . ."
        elif LauraX.addiction >= 50:
            $ LauraX.change_face("manic", 1)
            ch_l "[[wipes away a little drool]"
        else:
            $ LauraX.change_face("sad")
            $ LauraX.mouth = "smile"
            ch_l "Huh. . ."
    elif approval:
        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
            ch_l "Again?"
        elif not Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "Hmm, this is private enough. . ."
        elif "blowjob" in LauraX.recent_history:
            $ LauraX.change_face("sexy", 1)
            ch_l "Mmm, again? [[yawns]"
            jump Laura_BJ_Prep
        elif "blowjob" in LauraX.daily_history:
            $ LauraX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",   
                "Wear'in me out here.",  
                "I must be too good at this.", 
                "Let me get some saliva going.",
                "Didn't get enough earlier?"])
            ch_l "[Line]"
        elif LauraX.action_counter["blowjob"] < 3:
            $ LauraX.change_face("sexy", 1)
            $ LauraX.brows = "confused"
            $ LauraX.mouth = "kiss"
            ch_l "You'd like another blowjob?"
        else:
            $ LauraX.change_face("sexy", 1)
            $ LauraX.ArmPose = 2
            $ Line = renpy.random.choice(["You want me to [mimes blowing]?",                 
                "So you want another blowjob?",                 
                "You want me to lick you?", 
                "You want me to suck you off?",
                "A little bj?"])
            ch_l "[Line]"
        $ Line = 0

    if approval >= 2:
        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("obedience", 90, 1)
            $ LauraX.change_stat("inhibition", 60, 1)
            ch_l "Whatever."
        elif "no_blowjob" in LauraX.daily_history:
            ch_l "Fine. . ."
        else:
            $ LauraX.change_face("sexy", 1)
            $ LauraX.change_stat("love", 90, 1)
            $ LauraX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Sure. Ahhhhhh.",                 
                "Well. . . alright.",                 
                "Yum.", 
                "Sure, whip it out.",
                "Ok. . . [She licks her lips].",
                "Alright, let's see it."])
            ch_l "[Line]"
            $ Line = 0
        $ LauraX.change_stat("obedience", 20, 1)
        $ LauraX.change_stat("obedience", 70, 1)
        $ LauraX.change_stat("inhibition", 80, 2)
        jump Laura_BJ_Prep
    else:

        $ LauraX.change_face("angry")
        if "no_blowjob" in LauraX.recent_history:
            ch_l "Just told you I wouldn't, [LauraX.player_petname]."
        elif Taboo and "no_taboo" in LauraX.daily_history and "no_blowjob" in LauraX.daily_history:
            ch_l "Like I told you, not in public."
        elif "no_blowjob" in LauraX.daily_history:
            ch_l "Told you \"no,\" [LauraX.player_petname]."
        elif Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "Like I told you, too public!"
        elif not LauraX.action_counter["blowjob"]:
            $ LauraX.change_face("bemused")
            ch_l "I don't know if your taste will match your scent, [LauraX.player_petname]. . ."
        else:
            $ LauraX.change_face("bemused")
            ch_l "I don't know, [LauraX.player_petname]!"
        menu:
            extend ""
            "Sorry, never mind." if "no_blowjob" in LauraX.daily_history:
                $ LauraX.change_face("bemused")
                ch_l "Cool."
                return
            "Maybe later?" if "no_blowjob" not in LauraX.daily_history:
                $ LauraX.change_face("sexy")
                ch_l "Yeah, maybe, [LauraX.player_petname]."
                $ LauraX.change_stat("love", 80, 2)
                $ LauraX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ LauraX.recent_history.append("no_taboo")
                    $ LauraX.daily_history.append("no_taboo")
                $ LauraX.recent_history.append("no_blowjob")
                $ LauraX.daily_history.append("no_blowjob")
                return
            "Come on, please?":
                if approval:
                    $ LauraX.change_face("sexy")
                    $ LauraX.change_stat("obedience", 90, 2)
                    $ LauraX.change_stat("obedience", 50, 2)
                    $ LauraX.change_stat("inhibition", 70, 3)
                    $ LauraX.change_stat("inhibition", 40, 2)
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
                    if approval_check(LauraX, 1100, TabM = 3):
                        $ LauraX.change_stat("inhibition", 80, 1)
                        $ LauraX.change_stat("inhibition", 60, 3)
                        $ LauraX.change_face("confused", 1)
                        $ LauraX.ArmPose = 2
                        if LauraX.action_counter["handjob"]:
                            ch_l "Couldn't I just use my hand again?"
                            ch_l "You seemed to like that."
                        else:
                            ch_l "I could maybe use my hand instead, how's that sound?"
                        menu:
                            extend ""
                            "Sure, that's fine.":
                                $ LauraX.change_stat("love", 80, 2)
                                $ LauraX.change_stat("inhibition", 60, 1)
                                $ LauraX.change_stat("obedience", 50, 1)
                                jump Laura_HJ_Prep
                            "Nah, if it's not a BJ, forget it.":
                                $ LauraX.change_stat("love", 200, -2)
                                $ LauraX.ArmPose = 1
                                ch_l "Fine, be that way."
                                $ LauraX.change_stat("obedience", 70, 2)
            "Suck it, [LauraX.petname]":


                $ LauraX.nameCheck()
                $ approval = approval_check(LauraX, 750, "OI", TabM = 3)
                if approval > 1 or (approval and LauraX.Forced):
                    $ LauraX.change_face("sad")
                    $ LauraX.change_stat("love", 70, -5, 1)
                    $ LauraX.change_stat("love", 200, -2)
                    ch_l "Whatever. . ."
                    $ LauraX.change_stat("obedience", 50, 4)
                    $ LauraX.change_stat("inhibition", 80, 1)
                    $ LauraX.change_stat("inhibition", 60, 3)
                    $ LauraX.Forced = 1
                    jump Laura_BJ_Prep
                else:
                    $ LauraX.change_stat("love", 200, -15)
                    $ LauraX.recent_history.append("angry")
                    $ LauraX.daily_history.append("angry")


    if "no_blowjob" in LauraX.daily_history:
        $ LauraX.change_face("angry", 1)
        $ LauraX.ArmPose = 2
        $ LauraX.Claws = 1
        ch_l "Suck this then."
        $ LauraX.ArmPose = 1
        $ LauraX.Claws = 0
        $ LauraX.recent_history.append("angry")
        $ LauraX.daily_history.append("angry")
    elif LauraX.Forced:
        $ LauraX.change_face("angry", 1)
        ch_l "That's just pushing it."
        $ LauraX.change_stat("lust", 200, 5)
        if LauraX.love > 300:
            $ LauraX.change_stat("love", 70, -2)
        $ LauraX.change_stat("obedience", 50, -2)
        $ LauraX.recent_history.append("angry")
        $ LauraX.daily_history.append("angry")
        $ LauraX.recent_history.append("no_blowjob")
        $ LauraX.daily_history.append("no_blowjob")
        return
    elif Taboo:
        $ LauraX.change_face("angry", 1)
        $ LauraX.daily_history.append("no_taboo")
        ch_l "This area's too exposed."
        $ LauraX.change_stat("lust", 200, 5)
        $ LauraX.change_stat("obedience", 50, -3)
        return
    elif LauraX.action_counter["blowjob"]:
        $ LauraX.change_face("sad")
        ch_l "Nah, not this time."
    else:
        $ LauraX.change_face("normal", 1)
        ch_l "Nope."
    $ LauraX.recent_history.append("no_blowjob")
    $ LauraX.daily_history.append("no_blowjob")
    $ approval_bonus = 0
    return


label Laura_BJ_Prep:
    if renpy.showing("Laura_HJ_Animation"):
        hide Laura_HJ_Animation with easeoutbottom
    if Taboo:
        $ LauraX.inhibition += int(Taboo/10)
        $ LauraX.lust += int(Taboo/5)

    $ LauraX.change_face("sexy")
    if LauraX.Forced:
        $ LauraX.change_face("sad")
    elif not LauraX.action_counter["blowjob"]:
        $ LauraX.brows = "confused"
        $ LauraX.eyes = "sexy"
        $ LauraX.mouth = "smile"

    call Seen_First_Peen (LauraX, Partner, React=action_context)
    call Laura_BJ_Launch ("L")
    if action_context == LauraX:

        $ action_context = 0
        "[LauraX.name] slides down and gives your cock a little lick."
        menu:
            "What do you do?"
            "Nothing.":
                $ LauraX.change_stat("inhibition", 80, 3)
                $ LauraX.change_stat("inhibition", 40, 2)
                "[LauraX.name] continues licking at it."
            "Praise her.":
                $ LauraX.change_face("sexy", 1)
                $ LauraX.change_stat("inhibition", 80, 3)
                ch_p "Hmmm, keep doing that, [LauraX.petname]."
                $ LauraX.nameCheck()
                "[LauraX.name] continues her actions."
                $ LauraX.change_stat("love", 85, 1)
                $ LauraX.change_stat("obedience", 90, 1)
                $ LauraX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ LauraX.change_face("surprised")
                $ LauraX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that for now, [LauraX.petname]."
                $ LauraX.nameCheck()
                "[LauraX.name] puts it down."
                $ LauraX.change_stat("obedience", 90, 1)
                $ LauraX.change_stat("obedience", 50, 3)
                $ Player.recent_history.append("nope")
                $ LauraX.add_word(1,"refused","refused")
                return
    if not LauraX.action_counter["blowjob"]:
        if LauraX.Forced:
            $ LauraX.change_stat("love", 90, -70)
            $ LauraX.change_stat("obedience", 70, 45)
            $ LauraX.change_stat("inhibition", 80, 60)
        else:
            $ LauraX.change_stat("love", 90, 5)
            $ LauraX.change_stat("obedience", 70, 35)
            $ LauraX.change_stat("inhibition", 80, 40)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ LauraX.drain_word("no_taboo")
    $ LauraX.drain_word("no_blowjob")
    $ LauraX.recent_history.append("blowjob")
    $ LauraX.daily_history.append("blowjob")

label Laura_BJ_Cycle:
    while Round > 0:
        call shift_focus (LauraX)
        call Laura_BJ_Launch
        $ LauraX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . ." if action_speed:
                    pass

                "Lick it. . ." if action_speed != 1:
                    call action_speed_Shift (1)
                "Lick it. . . (locked)" if action_speed == 1:
                    pass

                "Just the head. . ." if action_speed != 2:
                    call action_speed_Shift (2)
                "Just the head. . . (locked)" if action_speed == 2:
                    pass

                "Suck on it." if action_speed != 3:
                    call action_speed_Shift (3)
                    if offhand_action == "jackin":
                        "She dips her head a bit lower, and you move your hand out of the way."

                    if "Gwentro" not in LauraX.history:
                        call Gwentro

                "Suck on it. (locked)" if action_speed == 3:
                    pass

                "Take it deeper." if action_speed != 4:
                    if offhand_action == "jackin" and action_speed != 3:
                        "She takes it to the root, and you move your hand out of the way."
                    call action_speed_Shift (4)
                "Take it deeper. (locked)" if action_speed == 4:
                    pass
                "Set your own pace. . .":

                    "[LauraX.name] hums contentedly."
                    if "setpace" not in LauraX.recent_history:
                        $ LauraX.change_stat("love", 80, 2)
                    $ D20 = renpy.random.randint(1, 20)
                    if LauraX.action_counter["blowjob"] < 5:
                        $ D20 -= 10
                    elif LauraX.action_counter["blowjob"] < 10:
                        $ D20 -= 5

                    if D20 > 15:
                        call action_speed_Shift (4)
                        if "setpace" not in LauraX.recent_history:
                            $ LauraX.change_stat("inhibition", 80, 3)
                    elif D20 > 10:
                        call action_speed_Shift (3)
                    elif D20 > 5:
                        call action_speed_Shift (2)
                    else:
                        call action_speed_Shift (1)
                    $ LauraX.recent_history.append("setpace")

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "Other options":

                    menu:
                        "I also want to fondle her breasts." if offhand_action != "fondle_breasts":
                            if LauraX.remaining_actions and multi_action:
                                $ offhand_action = "fondle_breasts"
                                "You start to fondle her breasts."
                                $ LauraX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (LauraX, "tired")
                        "Shift primary action":

                            if LauraX.remaining_actions and multi_action:
                                menu:
                                    "How about a handy?":
                                        if LauraX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Laura_BJ_After
                                            call Laura_Handjob
                                        else:
                                            ch_l "I need a break, can we wrap on this?"
                                    "How about a titjob?":
                                        if LauraX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Laura_BJ_After
                                            call Laura_Titjob
                                        else:
                                            ch_l "I need a break, can we wrap on this?"
                                    "Never Mind":
                                        jump Laura_BJ_Cycle
                            else:
                                call Sex_Basic_Dialog (LauraX, "tired")

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [LauraX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (LauraX)
                                "Ask [LauraX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (LauraX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (LauraX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Laura_BJ_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Laura_BJ_Cycle
                                "Never mind":
                                    jump Laura_BJ_Cycle
                        "undress [LauraX.name]":
                            call Girl_Undress (LauraX)
                        "Clean up [LauraX.name] (locked)" if not LauraX.spunk:
                            pass
                        "Clean up [LauraX.name]" if LauraX.spunk:
                            call Girl_Cleanup (LauraX, "ask")
                        "Never mind":
                            jump Laura_BJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Laura_BJ_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Laura_BJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Laura_BJ_Reset
                    $ Line = 0
                    jump Laura_BJ_After


        call shift_focus (LauraX)
        call Sex_Dialog (LauraX, Partner)



        $ counter += 1
        $ Round -= 1
        if action_speed:
            $ Player.cock_wet = 1
            $ Player.spunk = 0 if Player.spunk else Player.spunk

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or LauraX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (LauraX)
                if "angry" in LauraX.recent_history:
                    call Laura_BJ_Reset
                    return
                $ LauraX.change_stat("lust", 200, 5)
                if 100 > LauraX.lust >= 70 and LauraX.session_orgasms < 2 and LauraX.SEXP >= 20:
                    $ LauraX.recent_history.append("unsatisfied")
                    $ LauraX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Laura_BJ_After
                $ Line = "came"

            if LauraX.lust >= 100:

                call Girl_Cumming (LauraX)
                if action_context == "shift" or "angry" in LauraX.recent_history:
                    jump Laura_BJ_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."

                if "unsatisfied" in LauraX.recent_history:
                    "[LauraX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Laura_BJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if LauraX.SEXP >= 100 or approval_check(LauraX, 1200, "LO"):
            pass
        elif counter == (10 + LauraX.action_counter["blowjob"]):
            $ LauraX.brows = "angry"
            menu:
                ch_l "I'm getting kinda bored. Can we do something else?"
                "How about a Handy?" if LauraX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Laura_BJ_After
                    call Laura_Handjob
                    return
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    jump Laura_BJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Laura_BJ_Reset
                    $ action_context = "shift"
                    jump Laura_BJ_After
                "No, get back down there.":
                    if approval_check(LauraX, 1200) or approval_check(LauraX, 500, "O"):
                        $ LauraX.change_stat("love", 200, -5)
                        $ LauraX.change_stat("obedience", 50, 3)
                        $ LauraX.change_stat("obedience", 80, 2)
                        "She grumbles but gets back to work."
                    else:
                        $ LauraX.change_face("angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        ch_l "Well fuck you then."
                        $ LauraX.change_stat("love", 50, -3, 1)
                        $ LauraX.change_stat("love", 80, -4, 1)
                        $ LauraX.change_stat("obedience", 30, -1, 1)
                        $ LauraX.change_stat("obedience", 50, -1, 1)
                        $ LauraX.recent_history.append("angry")
                        $ LauraX.daily_history.append("angry")
                        jump Laura_BJ_After
        elif counter == (5 + LauraX.action_counter["blowjob"]) and LauraX.SEXP <= 100 and not approval_check(LauraX, 1200, "LO"):
            $ LauraX.brows = "confused"
            ch_l "Are you getting close here? I'm bored."


        call Escalation (LauraX)

        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [LauraX.player_petname]."


    $ LauraX.change_face("bemused", 0)
    $ Line = 0
    ch_l "Ok, I'm taking a quick break. . ."

label Laura_BJ_After:
    $ LauraX.change_face("sexy")

    $ LauraX.action_counter["blowjob"] += 1
    $ LauraX.remaining_actions -=1
    $ LauraX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ LauraX.addiction_rate += 1

    call Partner_Like (LauraX, 2)

    if "Laura Jobber" in Achievements:
        pass
    elif LauraX.action_counter["blowjob"] >= 10:
        $ LauraX.change_face("smile", 1)
        ch_l "Your flavor is intoxicating."
        $ Achievements.append("Laura Jobber")
        $ LauraX.SEXP += 5
    elif action_context == "shift":
        pass
    elif LauraX.action_counter["blowjob"] == 1:
        $ LauraX.SEXP += 15
        if LauraX.love >= 500:
            $ LauraX.mouth = "smile"
            ch_l "Hey, whaddaya know, that wasn't bad."
        elif Player.focus <= 20:
            $ LauraX.mouth = "sad"
            ch_l "I hope you enjoyed that."
    elif LauraX.action_counter["blowjob"] == 5:
        ch_l "I'm really getting the hang of this. . . right?"
        menu:
            "[[nod]":
                $ LauraX.change_face("smile", 1)
                $ LauraX.change_stat("love", 90, 15)
                $ LauraX.change_stat("obedience", 80, 5)
                $ LauraX.change_stat("inhibition", 90, 10)
            "[[shake head \"no\"]":
                if approval_check(LauraX, 500, "O"):
                    $ LauraX.change_face("sad", 2)
                    $ LauraX.change_stat("love", 200, -5)
                else:
                    $ LauraX.change_face("angry", 2)
                    $ LauraX.change_stat("love", 200, -25)
                $ LauraX.change_stat("obedience", 80, 10)
                ch_l ". . ."
                $ LauraX.change_face("sad", 1)

    $ approval_bonus = 0
    if action_context != "shift":
        call Laura_BJ_Reset
    call checkout
    return






label Laura_Dildo_Check:
    if "dildo" in Player.inventory:
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in LauraX.inventory:
        "You ask [LauraX.name] to get out her favorite Dildo."
    else:
        "You don't have one of those on you."
        return 0
    return 1

label Laura_Dildo_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (LauraX)
    call Laura_Dildo_Check
    if not _return:
        return

    if LauraX.action_counter["dildo_pussy"]:
        $ approval_bonus += 15
    if LauraX.legs == "pants:":
        $ approval_bonus -= 20

    if LauraX.lust > 95:
        $ approval_bonus += 20
    elif LauraX.lust > 85:
        $ approval_bonus += 15

    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in LauraX.traits:
        $ approval_bonus += (5*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in LauraX.traits:
        $ approval_bonus -= 40
    if LauraX.event_counter["forced"] and not LauraX.Forced:
        $ approval_bonus -= 5*LauraX.event_counter["forced"]

    if Taboo and "no_taboo" in LauraX.daily_history:
        $ approval_bonus -= 10

    if "no_dildo" in LauraX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_dildo" in LauraX.recent_history else 0

    $ approval = approval_check(LauraX, 1250, TabM = 4)

    if action_context == LauraX:
        if approval > 2:
            if LauraX.PantsNum() == 5:
                "[LauraX.name] grabs her dildo, hiking up her skirt as she does."
                $ LauraX.upskirt = 1
            elif LauraX.PantsNum() >= 6:
                "[LauraX.name] grabs her dildo, pulling down her pants as she does."
                $ LauraX.legs = 0
            else:
                "[LauraX.name] grabs her dildo, rubbing is suggestively against her crotch."
            $ LauraX.SeenPanties = 1
            call Laura_First_Bottomless (1)
            "She slides the tip along her pussy and seems to want you to insert it."
            menu:
                "What do you do?"
                "Nothing.":
                    $ LauraX.change_stat("inhibition", 80, 3)
                    $ LauraX.change_stat("inhibition", 50, 2)
                    "[LauraX.name] slides it in."
                "Go for it.":
                    $ LauraX.change_face("sexy", 1)
                    $ LauraX.change_stat("inhibition", 80, 3)
                    ch_p "Oh yeah, [LauraX.petname], let's do this."
                    $ LauraX.nameCheck()
                    "You grab the dildo and slide it in."
                    $ LauraX.change_stat("love", 85, 1)
                    $ LauraX.change_stat("obedience", 90, 1)
                    $ LauraX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ LauraX.change_face("surprised")
                    $ LauraX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that right now, [LauraX.petname]."
                    $ LauraX.nameCheck()
                    "[LauraX.name] sets the dildo down."
                    $ LauraX.change_outfit()
                    $ LauraX.change_stat("obedience", 90, 1)
                    $ LauraX.change_stat("obedience", 50, 1)
                    $ LauraX.change_stat("obedience", 30, 2)
                    return
            jump Laura_DP_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
        return

    if action_context == "auto":
        "You rub the dildo across her body, and along her moist slit."
        $ LauraX.change_face("surprised", 1)

        if (LauraX.action_counter["dildo_pussy"] and approval) or (approval > 1):
            "[LauraX.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            $ LauraX.change_face("sexy")
            $ LauraX.change_stat("obedience", 70, 3)
            $ LauraX.change_stat("inhibition", 50, 3)
            $ LauraX.change_stat("inhibition", 70, 1)
            ch_l "Ooo, [LauraX.player_petname], toys!"
            jump Laura_DP_Prep
        else:
            $ LauraX.brows = "angry"
            menu:
                ch_l "Hey, what are you planning to do with that?!"
                "Sorry, sorry! Never mind.":
                    if approval:
                        $ LauraX.change_face("sexy", 1)
                        $ LauraX.change_stat("obedience", 70, 3)
                        $ LauraX.change_stat("inhibition", 50, 3)
                        $ LauraX.change_stat("inhibition", 70, 1)
                        ch_l "Well, now that you mention it. . ."
                        jump Laura_DP_Prep
                    "You pull back before you really get it in."
                    $ LauraX.change_face("bemused", 1)
                    if LauraX.action_counter["dildo_pussy"]:
                        ch_l "Well ok, [LauraX.player_petname], maybe warn me next time?"
                    else:
                        ch_l "Well ok, [LauraX.player_petname], that's a little much. . . for now . . ."
                "Just playing with my favorite toys.":
                    $ LauraX.change_stat("love", 80, -10, 1)
                    $ LauraX.change_stat("love", 200, -10)
                    "You press it inside some more."
                    $ LauraX.change_stat("obedience", 70, 3)
                    $ LauraX.change_stat("inhibition", 50, 3)
                    if not approval_check(LauraX, 700, "O", TabM=1):
                        $ LauraX.change_face("angry")
                        "[LauraX.name] shoves you away and slaps you in the face."
                        ch_l "Jerk!"
                        ch_l "Ask nice if you want to stick something in my pussy!"
                        $ LauraX.change_stat("love", 50, -10, 1)
                        $ LauraX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        if renpy.showing("Laura_SexSprite"):
                            call Laura_Sex_Reset
                        $ LauraX.recent_history.append("angry")
                        $ LauraX.daily_history.append("angry")
                    else:
                        $ LauraX.change_face("sad")
                        "[LauraX.name] doesn't seem to be into this, you're lucky she's so obedient."
                        jump Laura_DP_Prep
        return


    if not LauraX.action_counter["dildo_pussy"]:

        $ LauraX.change_face("surprised", 1)
        $ LauraX.mouth = "kiss"
        ch_l "Hmmm, so you'd like to try out some toys?"
        if LauraX.Forced:
            $ LauraX.change_face("sad")
            ch_l "I suppose there are worst things you could ask for."

    if not LauraX.action_counter["dildo_pussy"] and approval:

        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
        elif LauraX.love >= (LauraX.obedience + LauraX.inhibition):
            $ LauraX.change_face("sexy")
            $ LauraX.brows = "sad"
            $ LauraX.mouth = "smile"
            ch_l "I've had a reasonable amount of experience with these, you know. . ."
        elif LauraX.obedience >= LauraX.inhibition:
            $ LauraX.change_face("normal")
            ch_l "If that's what you want, [LauraX.player_petname]. . ."
        else:
            $ LauraX.change_face("sad")
            $ LauraX.mouth = "smile"
            ch_l "I guess it could be fun with a partner. . ."

    elif approval:

        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
            ch_l "The toys again?"
        elif not Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "Well, at least you got us some privacy this time. . ."
        elif "dildo_pussy" in LauraX.recent_history:
            $ LauraX.change_face("sexy", 1)
            ch_l "Mmm, again? Ok, let's get to it."
            jump Laura_DP_Prep
        elif "dildo_pussy" in LauraX.daily_history:
            $ LauraX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "You're going to wear me out."])
            ch_l "[Line]"
        elif LauraX.action_counter["dildo_pussy"] < 3:
            $ LauraX.change_face("sexy", 1)
            $ LauraX.brows = "confused"
            $ LauraX.mouth = "kiss"
            ch_l "You want to stick it in my pussy again?"
        else:
            $ LauraX.change_face("sexy", 1)
            $ LauraX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my pussy again?",
                    "You want me ta lube up your toy?"])
            ch_l "[Line]"
            $ Line = 0

    if approval >= 2:

        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("obedience", 90, 1)
            $ LauraX.change_stat("inhibition", 60, 1)
            ch_l "Ok, fine."
        else:
            $ LauraX.change_face("sexy", 1)
            $ LauraX.change_stat("love", 90, 1)
            $ LauraX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                    "Well. . . ok.",                 
                    "Sure!", 
                    "I guess I could. . . stick it in.",
                    "Hells yeah.",
                    "Heh, ok, ok."])
            ch_l "[Line]"
            $ Line = 0
        $ LauraX.change_stat("obedience", 20, 1)
        $ LauraX.change_stat("obedience", 60, 1)
        $ LauraX.change_stat("inhibition", 70, 2)
        jump Laura_DP_Prep
    else:


        $ LauraX.change_face("angry")
        if "no_dildo" in LauraX.recent_history:
            ch_l "What part of \"no,\" did you not get, [LauraX.player_petname]?"
        elif Taboo and "no_taboo" in LauraX.daily_history and "no_dildo" in LauraX.daily_history:
            ch_l "Stop swinging that thing around in public!"
        elif "no_dildo" in LauraX.daily_history:
            ch_l "I already told you \"no,\" [LauraX.player_petname]."
        elif Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "Stop swinging that thing around in public!"
        elif not LauraX.action_counter["dildo_pussy"]:
            $ LauraX.change_face("bemused")
            ch_l "I'm just not into toys, [LauraX.player_petname]. . ."
        else:
            $ LauraX.change_face("bemused")
            ch_l "I don't think we need any toys, [LauraX.player_petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no_dildo" in LauraX.daily_history:
                $ LauraX.change_face("bemused")
                ch_l "Yeah, ok, [LauraX.player_petname]."
                return
            "Maybe later?" if "no_dildo" not in LauraX.daily_history:
                $ LauraX.change_face("sexy")
                ch_l "Maybe I'll practice on my own time, [LauraX.player_petname]."
                $ LauraX.change_stat("love", 80, 2)
                $ LauraX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ LauraX.recent_history.append("no_taboo")
                    $ LauraX.daily_history.append("no_taboo")
                $ LauraX.recent_history.append("no_dildo")
                $ LauraX.daily_history.append("no_dildo")
                return
            "I think you'd like it. . .":
                if approval:
                    $ LauraX.change_face("sexy")
                    $ LauraX.change_stat("obedience", 90, 2)
                    $ LauraX.change_stat("obedience", 50, 2)
                    $ LauraX.change_stat("inhibition", 70, 3)
                    $ LauraX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                            "I suppose. . .", 
                            "You've got me there."])
                    ch_l "[Line]"
                    $ Line = 0
                    jump Laura_DP_Prep
                else:
                    pass
            "[[press it against her]":

                $ approval = approval_check(LauraX, 950, "OI", TabM = 3)
                if approval > 1 or (approval and LauraX.Forced):
                    $ LauraX.change_face("sad")
                    $ LauraX.change_stat("love", 70, -5, 1)
                    $ LauraX.change_stat("love", 200, -5)
                    ch_l "Ok, fine. If we're going to do this, stick it in already."
                    $ LauraX.change_stat("obedience", 80, 4)
                    $ LauraX.change_stat("inhibition", 80, 1)
                    $ LauraX.change_stat("inhibition", 60, 3)
                    $ LauraX.Forced = 1
                    jump Laura_DP_Prep
                else:
                    $ LauraX.change_stat("love", 200, -20)
                    $ LauraX.recent_history.append("angry")
                    $ LauraX.daily_history.append("angry")


    $ LauraX.ArmPose = 1
    if "no_dildo" in LauraX.daily_history:
        ch_l "Learn to take \"no\" for an answer, [LauraX.player_petname]."
        $ LauraX.recent_history.append("angry")
        $ LauraX.daily_history.append("angry")
    elif LauraX.Forced:
        $ LauraX.change_face("angry", 1)
        ch_l "I'm not going to let you use that on me."
        $ LauraX.change_stat("lust", 200, 5)
        if LauraX.love > 300:
            $ LauraX.change_stat("love", 70, -2)
        $ LauraX.change_stat("obedience", 50, -2)
        $ LauraX.recent_history.append("angry")
        $ LauraX.daily_history.append("angry")
    elif Taboo:
        $ LauraX.change_face("angry", 1)
        $ LauraX.recent_history.append("no_taboo")
        $ LauraX.daily_history.append("no_taboo")
        ch_l "Not here!"
        $ LauraX.change_stat("lust", 200, 5)
        $ LauraX.change_stat("obedience", 50, -3)
    elif LauraX.action_counter["dildo_pussy"]:
        $ LauraX.change_face("sad")
        ch_l "Sorry, you can keep your toys to yourself."
    else:
        $ LauraX.change_face("normal", 1)
        ch_l "No way."
    $ LauraX.recent_history.append("no_dildo")
    $ LauraX.daily_history.append("no_dildo")
    $ approval_bonus = 0
    return

label Laura_DP_Prep:
    if offhand_action == "dildo_pussy":
        return

    if not LauraX.Forced and action_context != "auto":
        $ approval_bonus = 15 if LauraX.PantsNum() >= 6 else 0
        call Bottoms_Off (LauraX)
        if "angry" in LauraX.recent_history:
            return

    $ approval_bonus = 0
    call Laura_Pussy_Launch ("dildo_pussy")
    if not LauraX.action_counter["dildo_pussy"]:
        if LauraX.Forced:
            $ LauraX.change_stat("love", 90, -75)
            $ LauraX.change_stat("obedience", 70, 60)
            $ LauraX.change_stat("inhibition", 80, 35)
        else:
            $ LauraX.change_stat("love", 90, 10)
            $ LauraX.change_stat("obedience", 70, 20)
            $ LauraX.change_stat("inhibition", 80, 45)
    if Taboo:
        $ LauraX.inhibition += int(Taboo/10)
        $ LauraX.lust += int(Taboo/5)


    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ LauraX.drain_word("no_taboo")
    $ LauraX.drain_word("no_dildo")
    $ LauraX.recent_history.append("dildo_pussy")
    $ LauraX.daily_history.append("dildo_pussy")

label Laura_DP_Cycle:
    while Round > 0:
        call shift_focus (LauraX)
        call Laura_Pussy_Launch ("dildo_pussy")
        $ LauraX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (LauraX)
                    jump Laura_DP_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "Other options":

                    menu:
                        "Offhand action":
                            if LauraX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ LauraX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (LauraX, "tired")
                        "Shift primary action":

                            if LauraX.remaining_actions and multi_action:
                                menu:
                                    "I want to stick a finger in her ass.":
                                        $ action_context = "shift"
                                        call Laura_DP_After
                                        call Laura_Insert_Ass
                                    "Just stick a finger in her ass without asking.":
                                        $ action_context = "auto"
                                        call Laura_DP_After
                                        call Laura_Insert_Ass
                                    "I want to shift the dildo to her ass.":
                                        $ action_context = "shift"
                                        call Laura_DP_After
                                        call Laura_Dildo_Ass
                                    "Never Mind":
                                        jump Laura_DP_Cycle
                            else:
                                call Sex_Basic_Dialog (LauraX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Laura_DP_After
                            call Offhand_Set
                        "Shift your focus (locked)" if not offhand_action:
                            pass
                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [LauraX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (LauraX)
                                "Ask [LauraX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (LauraX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (LauraX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Laura_DP_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Laura_DP_Cycle
                                "Never mind":
                                    jump Laura_DP_Cycle
                        "undress [LauraX.name]":
                            call Girl_Undress (LauraX)
                        "Clean up [LauraX.name] (locked)" if not LauraX.spunk:
                            pass
                        "Clean up [LauraX.name]" if LauraX.spunk:
                            call Girl_Cleanup (LauraX, "ask")
                        "Never mind":
                            jump Laura_DP_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Laura_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Laura_DP_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Laura_Pos_Reset
                    $ Line = 0
                    jump Laura_DP_After


        if LauraX.underwear or LauraX.PantsNum() >= 6 or LauraX.HoseNum() >= 5:
            call Girl_Undress (LauraX, "auto")

        call shift_focus (LauraX)
        call Sex_Dialog (LauraX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or LauraX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (LauraX)
                if "angry" in LauraX.recent_history:
                    call Laura_Pos_Reset
                    return
                $ LauraX.change_stat("lust", 200, 5)
                if 100 > LauraX.lust >= 70 and LauraX.session_orgasms < 2:
                    $ LauraX.recent_history.append("unsatisfied")
                    $ LauraX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Laura_DP_After
                $ Line = "came"

            if LauraX.lust >= 100:

                call Girl_Cumming (LauraX)
                if action_context == "shift" or "angry" in LauraX.recent_history:
                    jump Laura_DP_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in LauraX.recent_history:
                    "[LauraX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Laura_DP_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if LauraX.SEXP >= 100 or approval_check(LauraX, 1200, "LO"):
            pass
        elif counter == (5 + LauraX.action_counter["dildo_pussy"]):
            $ LauraX.brows = "confused"
            ch_l "What are you even doing down there?"
        elif LauraX.lust >= 80:
            pass
        elif counter == (15 + LauraX.action_counter["dildo_pussy"]) and LauraX.SEXP >= 15 and not approval_check(LauraX, 1500):
            $ LauraX.brows = "confused"
            menu:
                ch_l "[LauraX.player_petname], this is getting uncomfortable, maybe we could try something else."
                "Finish up.":
                    "You let go. . ."
                    jump Laura_DP_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Laura_DP_After
                "No, this is fun.":
                    if approval_check(LauraX, 1200) or approval_check(LauraX, 500, "O"):
                        $ LauraX.change_stat("love", 200, -5)
                        $ LauraX.change_stat("obedience", 50, 3)
                        $ LauraX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ LauraX.change_face("angry", 1)
                        call Laura_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_l "Well if that's your attitude, I don't need your \"help\"."
                        $ LauraX.change_stat("love", 50, -3, 1)
                        $ LauraX.change_stat("love", 80, -4, 1)
                        $ LauraX.change_stat("obedience", 30, -1, 1)
                        $ LauraX.change_stat("obedience", 50, -1, 1)
                        $ LauraX.recent_history.append("angry")
                        $ LauraX.daily_history.append("angry")
                        jump Laura_DP_After


        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [LauraX.player_petname]."


    $ LauraX.change_face("bemused", 0)
    $ Line = 0
    ch_l "Ok, [LauraX.player_petname], breaktime."


label Laura_DP_After:
    if not action_context:
        call Laura_Pos_Reset

    $ LauraX.change_face("sexy")

    $ LauraX.action_counter["dildo_pussy"] += 1
    $ LauraX.remaining_actions -=1

    call Partner_Like (LauraX, 1)

    if LauraX.action_counter["dildo_pussy"] == 1:
        $ LauraX.SEXP += 10
        if not action_context:
            if LauraX.love >= 500 and "unsatisfied" not in LauraX.recent_history:
                ch_l "Thanks for the extra hand. . ."
            elif LauraX.obedience <= 500 and Player.focus <= 20:
                $ LauraX.change_face("perplexed", 1)
                ch_l "Did you like that?"

    $ approval_bonus = 0


    call checkout
    return






label Laura_Dildo_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (LauraX)
    call Laura_Dildo_Check
    if not _return:
        return

    if LauraX.used_to_anal:
        $ approval_bonus += 30
    elif "anal" in LauraX.recent_history or "dildo_anal" in LauraX.recent_history:
        $ approval_bonus -= 20
    elif "anal" in LauraX.daily_history or "dildo_anal" in LauraX.daily_history:
        $ approval_bonus -= 10
    elif (LauraX.action_counter["anal"] + LauraX.action_counter["dildo_ass"] + LauraX.Plug) > 0:
        $ approval_bonus += 20

    if LauraX.legs == "pants:":
        $ approval_bonus -= 20

    if LauraX.lust > 95:
        $ approval_bonus += 20
    elif LauraX.lust > 85:
        $ approval_bonus += 15

    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in LauraX.traits:
        $ approval_bonus += (5*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in LauraX.traits:
        $ approval_bonus -= 40
    if LauraX.event_counter["forced"] and not LauraX.Forced:
        $ approval_bonus -= 5*LauraX.event_counter["forced"]

    if Taboo and "no_taboo" in LauraX.daily_history:
        $ approval_bonus -= 10

    if "no_dildo" in LauraX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_dildo" in LauraX.recent_history else 0

    $ approval = approval_check(LauraX, 1450, TabM = 4)

    if action_context == LauraX:

        if approval > 2:
            if LauraX.PantsNum() == 5:
                "[LauraX.name] grabs her dildo, hiking up her skirt as she does."
                $ LauraX.upskirt = 1
            elif LauraX.PantsNum() >= 6:
                "[LauraX.name] grabs her dildo, pulling down her pants as she does."
                $ LauraX.legs = 0
            else:
                "[LauraX.name] grabs her dildo, rubbing is suggestively against her ass."
            $ LauraX.SeenPanties = 1
            call Laura_First_Bottomless (1)
            "She slides the tip against her asshole, and seems to want you to insert it."
            menu:
                "What do you do?"
                "Nothing.":
                    $ LauraX.change_stat("inhibition", 80, 3)
                    $ LauraX.change_stat("inhibition", 50, 2)
                    "[LauraX.name] slides it in."
                "Go for it.":
                    $ LauraX.change_face("sexy", 1)
                    $ LauraX.change_stat("inhibition", 80, 3)
                    ch_p "Oh yeah, [LauraX.petname], let's do this."
                    $ LauraX.nameCheck()
                    "You grab the dildo and slide it in."
                    $ LauraX.change_stat("love", 85, 1)
                    $ LauraX.change_stat("obedience", 90, 1)
                    $ LauraX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ LauraX.change_face("surprised")
                    $ LauraX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that right now, [LauraX.petname]."
                    $ LauraX.nameCheck()
                    "[LauraX.name] sets the dildo down."
                    $ LauraX.change_outfit()
                    $ LauraX.change_stat("obedience", 90, 1)
                    $ LauraX.change_stat("obedience", 50, 1)
                    $ LauraX.change_stat("obedience", 30, 2)
                    return
            jump Laura_DA_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
        return

    if action_context == "auto":
        "You rub the dildo across her body, and against her tight anus."
        $ LauraX.change_face("surprised", 1)

        if (LauraX.action_counter["dildo_ass"] and approval) or (approval > 1):

            "[LauraX.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            $ LauraX.change_face("sexy")
            $ LauraX.change_stat("obedience", 70, 3)
            $ LauraX.change_stat("inhibition", 50, 3)
            $ LauraX.change_stat("inhibition", 70, 1)
            ch_l "Ooo, [LauraX.player_petname], toys!"
            jump Laura_DA_Prep
        else:

            $ LauraX.brows = "angry"
            menu:
                ch_l "Hey, what are you planning to do with that?!"
                "Sorry, sorry! Never mind.":
                    if approval:
                        $ LauraX.change_face("sexy", 1)
                        $ LauraX.change_stat("obedience", 70, 3)
                        $ LauraX.change_stat("inhibition", 50, 3)
                        $ LauraX.change_stat("inhibition", 70, 1)
                        ch_l "Well, now that you mention it. . ."
                        jump Laura_DA_Prep
                    "You pull back before you really get it in."
                    $ LauraX.change_face("bemused", 1)
                    if LauraX.action_counter["dildo_ass"]:
                        ch_l "Well ok, [LauraX.player_petname], maybe warn me next time?"
                    else:
                        ch_l "Well ok, [LauraX.player_petname], that's a little much. . . for now . . ."
                "Just playing with my favorite toys.":
                    $ LauraX.change_stat("love", 80, -10, 1)
                    $ LauraX.change_stat("love", 200, -10)
                    "You press it inside some more."
                    $ LauraX.change_stat("obedience", 70, 3)
                    $ LauraX.change_stat("inhibition", 50, 3)
                    if not approval_check(LauraX, 700, "O", TabM=1):
                        $ LauraX.change_face("angry")
                        "[LauraX.name] shoves you away and slaps you in the face."
                        ch_l "Jerk!"
                        ch_l "Ask nice if you want to stick something in my ass!"
                        $ LauraX.change_stat("love", 50, -10, 1)
                        $ LauraX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        if renpy.showing("Laura_SexSprite"):
                            call Laura_Sex_Reset
                        $ LauraX.recent_history.append("angry")
                        $ LauraX.daily_history.append("angry")
                    else:
                        $ LauraX.change_face("sad")
                        "[LauraX.name] doesn't seem to be into this, you're lucky she's so obedient."
                        jump Laura_DA_Prep
        return


    if not LauraX.action_counter["dildo_ass"]:

        $ LauraX.change_face("surprised", 1)
        $ LauraX.mouth = "kiss"
        ch_l "You want to try and fit that. . .?"
        if LauraX.Forced:
            $ LauraX.change_face("sad")
            ch_l "Always about the butt, huh?"

    if not LauraX.used_to_anal and ("dildo_anal" in LauraX.recent_history or "anal" in LauraX.recent_history or "dildo_anal" in LauraX.daily_history or "anal" in LauraX.daily_history):
        $ LauraX.change_face("bemused", 1)
        ch_l "I'm still sore from earlier. . ."

    if not LauraX.action_counter["dildo_ass"] and approval:

        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
        elif LauraX.love >= (LauraX.obedience + LauraX.inhibition):
            $ LauraX.change_face("sexy")
            $ LauraX.brows = "sad"
            $ LauraX.mouth = "smile"
            ch_l "I haven't actually used one of these, back there before. . ."
        elif LauraX.obedience >= LauraX.inhibition:
            $ LauraX.change_face("normal")
            ch_l "If that's what you want, [LauraX.player_petname]. . ."
        else:
            $ LauraX.change_face("sad")
            $ LauraX.mouth = "smile"
            ch_l "I guess it could be fun two-player. . ."

    elif approval:

        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
            ch_l "The toys again?"
        elif not Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "Well, at least you got us some privacy this time. . ."
        elif "dildo_anal" in LauraX.daily_history and not LauraX.used_to_anal:
            pass
        elif "dildo_anal" in LauraX.daily_history:
            $ LauraX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "I'm still a bit sore from earlier.",
                    "You're going to wear me out."])
            ch_l "[Line]"
        elif LauraX.action_counter["dildo_ass"] < 3:
            $ LauraX.change_face("sexy", 1)
            $ LauraX.brows = "confused"
            $ LauraX.mouth = "kiss"
            ch_l "You want to stick it in my ass again?"
        else:
            $ LauraX.change_face("sexy", 1)
            $ LauraX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my ass again?",
                    "You want me ta lube up your toy?"])
            ch_l "[Line]"
            $ Line = 0

    if approval >= 2:

        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("obedience", 90, 1)
            $ LauraX.change_stat("inhibition", 60, 1)
            ch_l "Ok, fine."
        else:
            $ LauraX.change_face("sexy", 1)
            $ LauraX.change_stat("love", 90, 1)
            $ LauraX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                    "Well. . . ok.",                 
                    "Sure!", 
                    "I guess I could. . . stick it in.",
                    "Hells yeah.",
                    "Heh, ok, ok."])
            ch_l "[Line]"
            $ Line = 0
        $ LauraX.change_stat("obedience", 20, 1)
        $ LauraX.change_stat("obedience", 60, 1)
        $ LauraX.change_stat("inhibition", 70, 2)
        jump Laura_DA_Prep
    else:


        $ LauraX.change_face("angry")
        if "no_dildo" in LauraX.recent_history:
            ch_l "What part of \"no,\" did you not get, [LauraX.player_petname]?"
        elif Taboo and "no_taboo" in LauraX.daily_history and "no_dildo" in LauraX.daily_history:
            ch_l "Stop swinging that thing around in public!"
        elif "no_dildo" in LauraX.daily_history:
            ch_l "I already told you \"no,\" [LauraX.player_petname]."
        elif Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "I already told you that I wouldn't do that out here!"
        elif not LauraX.action_counter["dildo_ass"]:
            $ LauraX.change_face("bemused")
            ch_l "I'm just not into toys, [LauraX.player_petname]. . ."
        elif not LauraX.used_to_anal and "dildo_anal" not in LauraX.daily_history:
            $ LauraX.change_face("perplexed")
            ch_l "You could have been a bit more gentle last time, [LauraX.player_petname]. . ."
        else:
            $ LauraX.change_face("bemused")
            ch_l "I don't think we need any toys, [LauraX.player_petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no_dildo" in LauraX.daily_history:
                $ LauraX.change_face("bemused")
                ch_l "Yeah, ok, [LauraX.player_petname]."
                return
            "Maybe later?" if "no_dildo" not in LauraX.daily_history:
                $ LauraX.change_face("sexy")
                ch_l "Maybe I'll practice on my own time, [LauraX.player_petname]."
                $ LauraX.change_stat("love", 80, 2)
                $ LauraX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ LauraX.recent_history.append("no_taboo")
                    $ LauraX.daily_history.append("no_taboo")
                $ LauraX.recent_history.append("no_dildo")
                $ LauraX.daily_history.append("no_dildo")
                return
            "I think you'd like it. . .":
                if approval:
                    $ LauraX.change_face("sexy")
                    $ LauraX.change_stat("obedience", 90, 2)
                    $ LauraX.change_stat("obedience", 50, 2)
                    $ LauraX.change_stat("inhibition", 70, 3)
                    $ LauraX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                            "I suppose. . .", 
                            "You've got me there."])
                    ch_l "[Line]"
                    $ Line = 0
                    jump Laura_DA_Prep
                else:
                    pass
            "[[press it against her]":

                $ approval = approval_check(LauraX, 1050, "OI", TabM = 3)
                if approval > 1 or (approval and LauraX.Forced):
                    $ LauraX.change_face("sad")
                    $ LauraX.change_stat("love", 70, -5, 1)
                    $ LauraX.change_stat("love", 200, -5)
                    ch_l "Ok, fine. If we're going to do this, stick it in already."
                    $ LauraX.change_stat("obedience", 80, 4)
                    $ LauraX.change_stat("inhibition", 80, 1)
                    $ LauraX.change_stat("inhibition", 60, 3)
                    $ LauraX.Forced = 1
                    jump Laura_DA_Prep
                else:
                    $ LauraX.change_stat("love", 200, -20)
                    $ LauraX.recent_history.append("angry")
                    $ LauraX.daily_history.append("angry")


    $ LauraX.ArmPose = 1
    if "no_dildo" in LauraX.daily_history:
        ch_l "Learn to take \"no\" for an answer, [LauraX.player_petname]."
        $ LauraX.recent_history.append("angry")
        $ LauraX.daily_history.append("angry")
    elif LauraX.Forced:
        $ LauraX.change_face("angry", 1)
        ch_l "I'm not going to let you use that on me."
        $ LauraX.change_stat("lust", 200, 5)
        if LauraX.love > 300:
            $ LauraX.change_stat("love", 70, -2)
        $ LauraX.change_stat("obedience", 50, -2)
        $ LauraX.recent_history.append("angry")
        $ LauraX.daily_history.append("angry")
    elif Taboo:
        $ LauraX.change_face("angry", 1)
        $ LauraX.recent_history.append("no_taboo")
        $ LauraX.daily_history.append("no_taboo")
        ch_l "Not here!"
        $ LauraX.change_stat("lust", 200, 5)
        $ LauraX.change_stat("obedience", 50, -3)
    elif not LauraX.used_to_anal and "dildo_anal" in LauraX.daily_history:
        $ LauraX.change_face("bemused")
        ch_l "Sorry, I just need a little break back there, [LauraX.player_petname]."
    elif LauraX.action_counter["dildo_ass"]:
        $ LauraX.change_face("sad")
        ch_l "Sorry, you can keep your toys out of there."
    else:
        $ LauraX.change_face("normal", 1)
        ch_l "No way."
    $ LauraX.recent_history.append("no_dildo")
    $ LauraX.daily_history.append("no_dildo")
    $ approval_bonus = 0
    return

label Laura_DA_Prep:
    if offhand_action == "dildo_anal":
        return

    if not LauraX.Forced and action_context != "auto":
        $ approval_bonus = 20 if LauraX.PantsNum() >= 6 else 0
        call Bottoms_Off (LauraX)
        if "angry" in LauraX.recent_history:
            return

    $ approval_bonus = 0
    call Laura_Pussy_Launch ("dildo_anal")
    if not LauraX.action_counter["dildo_ass"]:
        if LauraX.Forced:
            $ LauraX.change_stat("love", 90, -75)
            $ LauraX.change_stat("obedience", 70, 60)
            $ LauraX.change_stat("inhibition", 80, 35)
        else:
            $ LauraX.change_stat("love", 90, 10)
            $ LauraX.change_stat("obedience", 70, 20)
            $ LauraX.change_stat("inhibition", 80, 45)
    if Taboo:
        $ LauraX.inhibition += int(Taboo/10)
        $ LauraX.lust += int(Taboo/5)


    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ LauraX.drain_word("no_taboo")
    $ LauraX.drain_word("no_dildo")
    $ LauraX.recent_history.append("dildo_anal")
    $ LauraX.daily_history.append("dildo_anal")

label Laura_DA_Cycle:
    while Round > 0:
        call shift_focus (LauraX)
        call Laura_Pussy_Launch ("dildo_anal")
        $ LauraX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (LauraX)
                    jump Laura_DA_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "Other options":

                    menu:
                        "Offhand action":
                            if LauraX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ LauraX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (LauraX, "tired")
                        "Shift primary action":

                            if LauraX.remaining_actions and multi_action:
                                menu:
                                    "I want to stick a finger in her pussy.":
                                        $ action_context = "shift"
                                        call Laura_DA_After
                                        call Laura_Fondle_Pussy
                                    "Just stick a finger in her pussy without asking.":
                                        $ action_context = "auto"
                                        call Laura_DA_After
                                        call Laura_Fondle_Pussy
                                    "I want to shift the dildo to her pussy.":
                                        $ action_context = "shift"
                                        call Laura_DA_After
                                        call Laura_Dildo_Pussy
                                    "Never Mind":
                                        jump Laura_DA_Cycle
                            else:
                                call Sex_Basic_Dialog (LauraX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Laura_DA_After
                            call Offhand_Set
                        "Shift your focus (locked)" if not offhand_action:
                            pass
                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [LauraX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (LauraX)
                                "Ask [LauraX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (LauraX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (LauraX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Laura_DA_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Laura_DA_Cycle
                        "Never mind":
                            jump Laura_DA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Laura_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Laura_DA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Laura_Pos_Reset
                    $ Line = 0
                    jump Laura_DA_After


        if LauraX.underwear or LauraX.PantsNum() >= 6 or LauraX.HoseNum() >= 5:
            call Girl_Undress (LauraX, "auto")

        call shift_focus (LauraX)
        call Sex_Dialog (LauraX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or LauraX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (LauraX)
                if "angry" in LauraX.recent_history:
                    call Laura_Pos_Reset
                    return
                $ LauraX.change_stat("lust", 200, 5)
                if 100 > LauraX.lust >= 70 and LauraX.session_orgasms < 2:
                    $ LauraX.recent_history.append("unsatisfied")
                    $ LauraX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Laura_DA_After
                $ Line = "came"

            if LauraX.lust >= 100:

                call Girl_Cumming (LauraX)
                if action_context == "shift" or "angry" in LauraX.recent_history:
                    jump Laura_DA_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in LauraX.recent_history:
                    "[LauraX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Laura_DA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if LauraX.SEXP >= 100 or approval_check(LauraX, 1200, "LO"):
            pass
        elif counter == (5 + LauraX.action_counter["dildo_ass"]):
            $ LauraX.brows = "confused"
            ch_l "What are you even doing down there?"
        elif LauraX.lust >= 80:
            pass
        elif counter == (15 + LauraX.action_counter["dildo_ass"]) and LauraX.SEXP >= 15 and not approval_check(LauraX, 1500):
            $ LauraX.brows = "confused"
            menu:
                ch_l "[LauraX.player_petname], this is getting uncomfortable, maybe we could try something else."
                "Finish up.":
                    "You let go. . ."
                    jump Laura_DA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Laura_DA_After
                "No, this is fun.":
                    if approval_check(LauraX, 1200) or approval_check(LauraX, 500, "O"):
                        $ LauraX.change_stat("love", 200, -5)
                        $ LauraX.change_stat("obedience", 50, 3)
                        $ LauraX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ LauraX.change_face("angry", 1)
                        call Laura_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_l "Well if that's your attitude, I don't need your \"help\"."
                        $ LauraX.change_stat("love", 50, -3, 1)
                        $ LauraX.change_stat("love", 80, -4, 1)
                        $ LauraX.change_stat("obedience", 30, -1, 1)
                        $ LauraX.change_stat("obedience", 50, -1, 1)
                        $ LauraX.recent_history.append("angry")
                        $ LauraX.daily_history.append("angry")
                        jump Laura_DA_After


        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [LauraX.player_petname]."


    $ LauraX.change_face("bemused", 0)
    $ Line = 0
    ch_l "Ok, [LauraX.player_petname], breaktime."

label Laura_DA_After:
    if not action_context:
        call Laura_Pos_Reset

    $ LauraX.change_face("sexy")

    $ LauraX.action_counter["dildo_ass"] += 1
    $ LauraX.remaining_actions -=1

    call Partner_Like (LauraX, 1)

    if LauraX.action_counter["dildo_ass"] == 1:
        $ LauraX.SEXP += 10
        if not action_context:
            if LauraX.love >= 500 and "unsatisfied" not in LauraX.recent_history:
                if LauraX.used_to_anal:
                    ch_l "That was. . . interesting. . ."
                else:
                    ch_l "Ouch. . ."
            elif LauraX.obedience <= 500 and Player.focus <= 20:
                $ LauraX.change_face("perplexed", 1)
                ch_l "Did you like that?"

    $ approval_bonus = 0


    call checkout
    return



label Laura_Vibrator_Check:
    if "vibrator" in Player.inventory:
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in LauraX.inventory:
        "You ask [LauraX.name] to get out her vibrator."
    else:
        "You don't have one of those on you."
        return 0
    return 1


label Laura_Footjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (LauraX)
    if LauraX.action_counter["footjob"] >= 7:
        $ approval_bonus += 10
    elif LauraX.action_counter["footjob"] >= 3:
        $ approval_bonus += 7
    elif LauraX.action_counter["footjob"]:
        $ approval_bonus += 3

    if LauraX.addiction >= 75 and LauraX.event_counter["swallowed"] >=3:
        $ approval_bonus += 10
    if LauraX.addiction >= 75:
        $ approval_bonus += 5

    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in LauraX.traits:
        $ approval_bonus += (3*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in LauraX.traits:
        $ approval_bonus -= 40
    if LauraX.event_counter["forced"] and not LauraX.Forced:
        $ approval_bonus -= 5*LauraX.event_counter["forced"]

    if Taboo and "no_taboo" in LauraX.daily_history:
        $ approval_bonus -= 10

    if "no_foot" in LauraX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_foot" in LauraX.recent_history else 0

    $ approval = approval_check(LauraX, 1250, TabM = 3)

    if action_context == LauraX:
        if approval > 2:
            "[LauraX.name] leans back and starts rubbing your cock with her foot."
            menu:
                "What do you do?"
                "Nothing.":
                    $ LauraX.change_stat("inhibition", 70, 3)
                    $ LauraX.change_stat("inhibition", 30, 2)
                    "[LauraX.name] continues her actions."
                "Praise her.":
                    $ LauraX.change_face("sexy", 1)
                    $ LauraX.change_stat("inhibition", 70, 3)
                    ch_p "Oooh, that's good, [LauraX.petname]."
                    $ LauraX.nameCheck()
                    "[LauraX.name] continues her actions."
                    $ LauraX.change_stat("love", 80, 1)
                    $ LauraX.change_stat("obedience", 90, 1)
                    $ LauraX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ LauraX.change_face("surprised")
                    $ LauraX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that for now, [LauraX.petname]."
                    $ LauraX.nameCheck()
                    "[LauraX.name] puts it down."
                    $ LauraX.change_stat("obedience", 90, 1)
                    $ LauraX.change_stat("obedience", 50, 1)
                    $ LauraX.change_stat("obedience", 30, 2)
                    return
            if primary_action:
                $ girl_offhand_action = "foot"
                return
            jump Laura_FJ_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if not LauraX.action_counter["footjob"] and "no_foot" not in LauraX.recent_history:
        $ LauraX.change_face("confused", 2)
        ch_l "Standard footjob?"
        $ LauraX.blushing = 1

    if not LauraX.action_counter["footjob"] and approval:
        if LauraX.Forced:
            $ LauraX.change_face("sad",1)
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
        elif LauraX.love >= (LauraX.obedience + LauraX.inhibition):
            $ LauraX.change_face("sexy",1)
            $ LauraX.brows = "sad"
            $ LauraX.mouth = "smile"
            ch_l "I guess it couldn't hurt. . ."
        elif LauraX.obedience >= LauraX.inhibition:
            $ LauraX.change_face("normal",1)
            ch_l "If you want, [LauraX.player_petname]. . ."
        elif LauraX.addiction >= 50:
            $ LauraX.change_face("manic", 1)
            ch_l "Okay. . ."
        else:
            $ LauraX.change_face("lipbite",1)
            ch_l "Sure. . ."

    elif approval:
        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
            ch_l "That's it?"
        elif not Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "Um, I guess this is secure enough. . ."
        elif "foot" in LauraX.daily_history:
            $ LauraX.change_face("sexy", 1)
            ch_l "More of that, huh. . ."
            jump Laura_FJ_Prep







        elif LauraX.action_counter["footjob"] < 3:
            $ LauraX.change_face("sexy", 1)
            $ LauraX.brows = "confused"
            $ LauraX.mouth = "kiss"
            ch_l "Hmm, magic toes. . ."
        else:
            $ LauraX.change_face("sexy", 1)
            $ LauraX.ArmPose = 2
            $ Line = renpy.random.choice(["You want me to use my feet?",                 
                "So you'd like another footjob?",                 
                "A little. . . [she rubs her foot along your leg]?", 
                "A little TLC?"])
            ch_l "[Line]"
        $ Line = 0

    if approval >= 2:
        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("obedience", 90, 1)
            $ LauraX.change_stat("inhibition", 60, 1)
            ch_l "Ok, sure."
        elif "no_foot" in LauraX.daily_history:
            ch_l "Fine."
        else:
            $ LauraX.change_face("sexy", 1)
            $ LauraX.change_stat("love", 90, 1)
            $ LauraX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Sure, I guess.",                 
                "OK.",                 
                "Fine, lemme see it.", 
                "I guess I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Heh, ok, ok."])
            ch_l "[Line]"
            $ Line = 0
        $ LauraX.change_stat("obedience", 20, 1)
        $ LauraX.change_stat("obedience", 60, 1)
        $ LauraX.change_stat("inhibition", 70, 2)
        jump Laura_FJ_Prep
    else:

        $ LauraX.change_face("angry")
        if "no_foot" in LauraX.recent_history:
            ch_l "You should listen better, [LauraX.player_petname]."
        elif Taboo and "no_taboo" in LauraX.daily_history and "no_foot" in LauraX.daily_history:
            ch_l "I said not in public."
        elif "no_foot" in LauraX.daily_history:
            ch_l "I told you \"no,\" [LauraX.player_petname]."
        elif Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "I said not in public!"
        elif not LauraX.action_counter["footjob"]:
            $ LauraX.change_face("bemused")
            ch_l "Eh, [LauraX.player_petname]. . ."
        else:
            $ LauraX.change_face("bemused")
            ch_l "Not now, ok?"
        menu:
            extend ""
            "Sorry, never mind." if "no_foot" in LauraX.daily_history:
                $ LauraX.change_face("bemused")
                ch_l "Sure, no problem."
                return
            "Maybe later?" if "no_foot" not in LauraX.daily_history:
                $ LauraX.change_face("sexy")
                ch_l ". . ."
                ch_l "Maybe."
                $ LauraX.change_stat("love", 80, 2)
                $ LauraX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ LauraX.recent_history.append("no_taboo")
                    $ LauraX.daily_history.append("no_taboo")
                $ LauraX.recent_history.append("no_foot")
                $ LauraX.daily_history.append("no_foot")
                return
            "I'd really appreciate it. . .":
                if approval:
                    $ LauraX.change_face("sexy")
                    $ LauraX.change_stat("obedience", 90, 2)
                    $ LauraX.change_stat("obedience", 50, 2)
                    $ LauraX.change_stat("inhibition", 70, 3)
                    $ LauraX.change_stat("inhibition", 40, 2)
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
            "Come on, get to work.":

                $ approval = approval_check(LauraX, 400, "OI", TabM = 3)
                if approval > 1 or (approval and LauraX.Forced):
                    $ LauraX.change_face("sad")
                    $ LauraX.change_stat("love", 70, -5, 1)
                    $ LauraX.change_stat("love", 200, -2)
                    ch_l "Fine."
                    $ LauraX.change_stat("obedience", 50, 4)
                    $ LauraX.change_stat("inhibition", 80, 1)
                    $ LauraX.change_stat("inhibition", 60, 3)
                    $ LauraX.Forced = 1
                    jump Laura_FJ_Prep
                else:
                    $ LauraX.change_stat("love", 200, -15)
                    $ LauraX.recent_history.append("angry")
                    $ LauraX.daily_history.append("angry")


    $ LauraX.ArmPose = 1
    if "no_foot" in LauraX.daily_history:
        $ LauraX.change_face("angry", 1)
        ch_l "I'm not telling you again."
        $ LauraX.recent_history.append("angry")
        $ LauraX.daily_history.append("angry")
    elif LauraX.Forced:
        $ LauraX.change_face("angry", 1)
        ch_l "You understand that I have claws down there too. . ."
        $ LauraX.change_stat("lust", 200, 5)
        if LauraX.love > 300:
            $ LauraX.change_stat("love", 70, -2)
        $ LauraX.change_stat("obedience", 50, -2)
        $ LauraX.recent_history.append("angry")
        $ LauraX.daily_history.append("angry")
    elif Taboo:
        $ LauraX.change_face("angry", 1)
        $ LauraX.daily_history.append("no_taboo")
        ch_l "This is too exposed."
        $ LauraX.change_stat("lust", 200, 5)
        $ LauraX.change_stat("obedience", 50, -3)
    elif LauraX.action_counter["footjob"]:
        $ LauraX.change_face("sad")
        ch_l "Not right now."
    else:
        $ LauraX.change_face("normal", 1)
        ch_l "I'd rather not."
    $ LauraX.recent_history.append("no_foot")
    $ LauraX.daily_history.append("no_foot")
    $ approval_bonus = 0
    return


label Laura_FJ_Prep:
    if offhand_action == "foot":
        return

    if Taboo:
        $ LauraX.inhibition += int(Taboo/10)
        $ LauraX.lust += int(Taboo/5)

    $ LauraX.change_face("sexy")
    if LauraX.Forced:
        $ LauraX.change_face("sad")
    elif not LauraX.action_counter["footjob"]:
        $ LauraX.brows = "confused"
        $ LauraX.eyes = "sexy"
        $ LauraX.mouth = "smile"

    call Seen_First_Peen (LauraX, Partner)

    if not LauraX.action_counter["footjob"]:
        if LauraX.Forced:
            $ LauraX.change_stat("love", 90, -20)
            $ LauraX.change_stat("obedience", 70, 25)
            $ LauraX.change_stat("inhibition", 80, 30)
        else:
            $ LauraX.change_stat("love", 90, 5)
            $ LauraX.change_stat("obedience", 70, 20)
            $ LauraX.change_stat("inhibition", 80, 20)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ LauraX.drain_word("no_taboo")
    $ LauraX.drain_word("no_foot")
    $ LauraX.recent_history.append("foot")
    $ LauraX.daily_history.append("foot")

label Laura_FJ_Cycle:
    while Round > 0:
        call shift_focus (LauraX)
        call Laura_Sex_Launch ("foot")
        $ LauraX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . ." if action_speed:
                    pass

                "Start moving? . ." if not action_speed:
                    $ action_speed = 1

                "Speed up. . ." if action_speed < 2:
                    $ action_speed += 1
                    "You ask her to up the pace a bit."
                "Speed up. . . (locked)" if action_speed >= 2:
                    pass

                "Slow Down. . ." if action_speed:
                    $ action_speed -= 1
                    "You ask her to slow it down a bit."
                "Slow Down. . . (locked)" if not action_speed:
                    pass
                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "Turn her Around":

                    $ LauraX.pose = "doggy" if LauraX.pose != "doggy" else "sex"
                    "You turn her around. . ."
                    jump Laura_FJ_Cycle
                "Other options":

                    menu:
                        "Offhand action":
                            if LauraX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ LauraX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (LauraX, "tired")
                        "Shift primary action":

                            if LauraX.remaining_actions and multi_action:
                                menu:
                                    "How about a blowjob?":
                                        if LauraX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Laura_FJ_After
                                            call Laura_Blowjob
                                        else:
                                            call Sex_Basic_Dialog (LauraX, "tired")
                                    "How about a handjob?":
                                        if LauraX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Laura_FJ_After
                                            call Laura_Handjob
                                        else:
                                            call Sex_Basic_Dialog (LauraX, "tired")
                                    "How about a titjob?":

                                        if LauraX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Laura_FJ_After
                                            call Laura_Titjob
                                        else:
                                            call Sex_Basic_Dialog (LauraX, "tired")
                                    "Never Mind":



                                        jump Laura_FJ_Cycle
                            else:
                                call Sex_Basic_Dialog (LauraX, "tired")

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [LauraX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (LauraX)
                                "Ask [LauraX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (LauraX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (LauraX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Laura_FJ_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Laura_FJ_Cycle
                                "Never mind":
                                    jump Laura_FJ_Cycle
                        "undress [LauraX.name]":
                            call Girl_Undress (LauraX)
                        "Clean up [LauraX.name] (locked)" if not LauraX.spunk:
                            pass
                        "Clean up [LauraX.name]" if LauraX.spunk:
                            call Girl_Cleanup (LauraX, "ask")
                        "Never mind":
                            jump Laura_FJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Laura_Sex_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Laura_FJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Laura_Sex_Reset
                    $ Line = 0
                    jump Laura_FJ_After


        call shift_focus (LauraX)
        call Sex_Dialog (LauraX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or LauraX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (LauraX)
                if "angry" in LauraX.recent_history:
                    call Laura_Sex_Reset
                    return
                $ LauraX.change_stat("lust", 200, 5)
                if 100 > LauraX.lust >= 70 and LauraX.session_orgasms < 2:
                    $ LauraX.recent_history.append("unsatisfied")
                    $ LauraX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Laura_FJ_After
                $ Line = "came"

            if LauraX.lust >= 100:

                call Girl_Cumming (LauraX)
                if action_context == "shift" or "angry" in LauraX.recent_history:
                    jump Laura_FJ_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in LauraX.recent_history:
                    "[LauraX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Laura_FJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if counter == 20:
            $ LauraX.brows = "angry"
            menu:
                ch_l "Hmm, this is getting a bit boring."
                "How about a BJ?" if LauraX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Laura_FJ_After
                    call Laura_Blowjob
                "How about a Handy?" if LauraX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Laura_FJ_After
                    call Laura_Handjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    $ counter += 1
                    "[Line]"
                    jump Laura_FJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Laura_Sex_Reset
                    $ action_context = "shift"
                    jump Laura_FJ_After
                "No, get back down there.":
                    if approval_check(LauraX, 1200) or approval_check(LauraX, 500, "O"):
                        $ LauraX.change_stat("love", 200, -5)
                        $ LauraX.change_stat("obedience", 50, 3)
                        $ LauraX.change_stat("obedience", 80, 2)
                        "She grumbles but gets back to work."
                    else:
                        $ LauraX.change_face("angry", 1)
                        "She scowls at you and pulls back."
                        ch_l "Not interested."
                        $ LauraX.change_stat("love", 50, -3, 1)
                        $ LauraX.change_stat("love", 80, -4, 1)
                        $ LauraX.change_stat("obedience", 30, -1, 1)
                        $ LauraX.change_stat("obedience", 50, -1, 1)
                        $ LauraX.recent_history.append("angry")
                        $ LauraX.daily_history.append("angry")
                        jump Laura_FJ_After
        elif counter == 10 and LauraX.SEXP <= 100 and not approval_check(LauraX, 1200, "LO"):
            $ LauraX.brows = "confused"
            ch_l "Ok, seriously, let's try something different."


        call Escalation (LauraX)

        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [LauraX.player_petname]."


    $ LauraX.change_face("bemused", 0)
    $ Line = 0
    ch_l "Ok, [LauraX.player_petname], breaktime."

label Laura_FJ_After:
    $ LauraX.change_face("sexy")

    $ LauraX.action_counter["footjob"] += 1
    $ LauraX.remaining_actions -=1
    $ LauraX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ LauraX.addiction_rate += 1
    $ LauraX.change_stat("lust", 90, 5)

    call Partner_Like (LauraX, 1)

    if "Laurapedi" in Achievements:
        pass
    elif LauraX.action_counter["footjob"] >= 10:
        $ LauraX.change_face("smile", 1)
        ch_l "I think I'm finally back into practice on this."
        $ Achievements.append("Laurapedi")
        $ LauraX.SEXP += 5
    elif LauraX.action_counter["footjob"] == 1:
        $ LauraX.SEXP += 10
        if LauraX.love >= 500:
            $ LauraX.mouth = "smile"
            ch_l "Did you like that? . ."
        elif Player.focus <= 20:
            $ LauraX.mouth = "sad"
            ch_l "Did that do it for you?"
    elif LauraX.action_counter["footjob"] == 5:
        ch_l "I'm getting used to this. . ."

    $ approval_bonus = 0
    if action_context == "shift":
        ch_l "Ok, so what did you have in mind?"
    else:
        call Laura_Sex_Reset
    call checkout
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
