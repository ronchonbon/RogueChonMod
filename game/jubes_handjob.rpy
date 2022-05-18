
label Jubes_Handjob:

    "This option is currently unavailable. It will be added in a later update."
    return


    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JubesX)
    if JubesX.action_counter["handjob"] >= 7:
        $ approval_bonus += 10
    elif JubesX.action_counter["handjob"] >= 3:
        $ approval_bonus += 7
    elif JubesX.action_counter["handjob"]:
        $ approval_bonus += 3

    if JubesX.addiction >= 75 and JubesX.event_counter["swallowed"] >=3:
        $ approval_bonus += 15
    if JubesX.addiction >= 75:
        $ approval_bonus += 5

    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in JubesX.traits:
        $ approval_bonus += (3*Taboo)
    if JubesX in Player.Harem or "sex friend" in JubesX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JubesX.traits:
        $ approval_bonus -= 40
    if JubesX.event_counter["forced"] and not JubesX.Forced:
        $ approval_bonus -= 5*JubesX.event_counter["forced"]

    if Taboo and "no_taboo" in JubesX.daily_history:
        $ approval_bonus -= 10

    if "no_handjob" in JubesX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_handjob" in JubesX.recent_history else 0

    $ approval = approval_check(JubesX, 1100, TabM = 3)

    if not JubesX.action_counter["handjob"] and "no_handjob" not in JubesX.recent_history:
        $ JubesX.change_face("_confused", 2)
        ch_v "Handjob, huh. . ."
        $ JubesX.blushing = "_blush1"

    if not JubesX.action_counter["handjob"] and approval:
        if JubesX.Forced:
            $ JubesX.change_face("_sad",1)
            $ JubesX.change_stat("love", 70, -3, 1)
            $ JubesX.change_stat("love", 20, -2, 1)
        elif JubesX.love >= (JubesX.obedience + JubesX.inhibition):
            $ JubesX.change_face("_sexy",1)
            $ JubesX.brows = "_sad"
            $ JubesX.mouth = "_smile"
            ch_v "You'd like that. . ."
        elif JubesX.obedience >= JubesX.inhibition:
            $ JubesX.change_face("_normal",1)
            ch_v "If you want, [JubesX.player_petname]. . ."
        else:
            $ JubesX.change_face("_lipbite",1)
            ch_v "Hmm. . ."

    elif approval:
        if JubesX.Forced:
            $ JubesX.change_face("_sad")
            $ JubesX.change_stat("love", 70, -3, 1)
            $ JubesX.change_stat("love", 20, -2, 1)
            ch_v "Nothing more than that?"
        elif not Taboo and "no_taboo" in JubesX.daily_history:
            ch_v "Well,this is a bit more secure. . ."
        elif "handjob" in JubesX.recent_history:
            $ JubesX.change_face("_sexy", 1)
            ch_v "Hmm, another handy then. . ."
            jump Jubes_HJ_Prep
        elif "handjob" in JubesX.daily_history:
            $ JubesX.change_face("_sexy", 1)
            $ Line = renpy.random.choice(["Another one?",   
                "I'm glad I don't grow calluses.", 
                "Didn't get enough earlier?",
                "Again the with handjobs, huh?",
                "I guess you want more."])
            ch_v "[Line]"
        elif JubesX.action_counter["handjob"] < 3:
            $ JubesX.change_face("_sexy", 1)
            $ JubesX.brows = "_confused"
            $ JubesX.mouth = "_kiss"
            ch_v "You seem to like this one. . ."
        else:
            $ JubesX.change_face("_sexy", 1)
            $ JubesX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some more?",                 
                "So you'd like another handy?",                 
                "You want a. . . [fist pumping hand gestures]?", 
                "Another handjob?"])
            ch_v "[Line]"
        $ Line = 0

    if approval >= 2:
        if JubesX.Forced:
            $ JubesX.change_face("_sad")
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_stat("inhibition", 60, 1)
            ch_v "Ok, fine."
        elif "no_handjob" in JubesX.daily_history:
            ch_v "If it'll get you off my back. . ."
        else:
            $ JubesX.change_face("_sexy", 1)
            $ JubesX.change_stat("love", 90, 1)
            $ JubesX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Sure, I guess.",                 
                "O-kay.",                 
                "Fine.", 
                "I suppose I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Ok, ok."])
            ch_v "[Line]"
            $ Line = 0
        $ JubesX.change_stat("obedience", 20, 1)
        $ JubesX.change_stat("obedience", 60, 1)
        $ JubesX.change_stat("inhibition", 70, 2)
        jump Jubes_HJ_Prep
    else:

        $ JubesX.change_face("_angry")
        if "no_handjob" in JubesX.recent_history:
            ch_v "I just told you no, [JubesX.player_petname]."
        elif Taboo and "no_taboo" in JubesX.daily_history and "no_handjob" in JubesX.daily_history:
            ch_v "I said not in public."
        elif "no_handjob" in JubesX.daily_history:
            ch_v "I told you \"no,\" [JubesX.player_petname]."
        elif Taboo and "no_taboo" in JubesX.daily_history:
            ch_v "I said not in public."
        elif not JubesX.action_counter["handjob"]:
            $ JubesX.change_face("_bemused")
            ch_v "Seriously, [JubesX.player_petname]. . ."
        else:
            $ JubesX.change_face("_bemused")
            ch_v "Nah."
        menu:
            extend ""
            "Sorry, never mind." if "no_handjob" in JubesX.daily_history:
                $ JubesX.change_face("_bemused")
                ch_v "It's fine."
                return
            "Maybe later?" if "no_handjob" not in JubesX.daily_history:
                $ JubesX.change_face("_bemused")
                ch_v "Maybe."
                $ JubesX.change_stat("love", 80, 2)
                $ JubesX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ JubesX.recent_history.append("no_taboo")
                    $ JubesX.daily_history.append("no_taboo")
                $ JubesX.recent_history.append("no_handjob")
                $ JubesX.daily_history.append("no_handjob")
                return
            "I'd really appreciate it. . .":
                if approval:
                    $ JubesX.change_face("_sexy")
                    $ JubesX.change_stat("obedience", 90, 2)
                    $ JubesX.change_stat("obedience", 50, 2)
                    $ JubesX.change_stat("inhibition", 70, 3)
                    $ JubesX.change_stat("inhibition", 40, 2)
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
            "Come on, get to work.":

                $ approval = approval_check(JubesX, 350, "OI", TabM = 3)
                if approval > 1 or (approval and JubesX.Forced):
                    $ JubesX.change_face("_sad")
                    $ JubesX.change_stat("love", 70, -5, 1)
                    $ JubesX.change_stat("love", 200, -2)
                    ch_v "Ok, fine."
                    $ JubesX.change_stat("obedience", 50, 4)
                    $ JubesX.change_stat("inhibition", 80, 1)
                    $ JubesX.change_stat("inhibition", 60, 3)
                    $ JubesX.Forced = 1
                    jump Jubes_HJ_Prep
                else:
                    $ JubesX.change_stat("love", 200, -15)
                    $ JubesX.recent_history.append("_angry")
                    $ JubesX.daily_history.append("_angry")


    $ JubesX.ArmPose = 1
    if "no_handjob" in JubesX.daily_history:
        $ JubesX.change_face("_angry", 1)
        ch_v "Don't ask again."
        $ JubesX.recent_history.append("_angry")
        $ JubesX.daily_history.append("_angry")
    elif JubesX.Forced:
        $ JubesX.change_face("_angry", 1)
        ch_v "No."
        $ JubesX.change_stat("lust", 200, 5)
        if JubesX.love > 300:
            $ JubesX.change_stat("love", 70, -2)
        $ JubesX.change_stat("obedience", 50, -2)
        $ JubesX.recent_history.append("_angry")
        $ JubesX.daily_history.append("_angry")
    elif Taboo:
        $ JubesX.change_face("_angry", 1)
        $ JubesX.daily_history.append("no_taboo")
        ch_v "This area's too exposed."
        $ JubesX.change_stat("lust", 200, 5)
        $ JubesX.change_stat("obedience", 50, -3)
    elif JubesX.action_counter["handjob"]:
        $ JubesX.change_face("_sad")
        ch_v "I'm not into it today. . ."
    else:
        $ JubesX.change_face("_normal", 1)
        ch_v "I don't know where that's been lately."
    $ JubesX.recent_history.append("no_handjob")
    $ JubesX.daily_history.append("no_handjob")
    $ approval_bonus = 0
    return


label Jubes_HJ_Prep:

    "This option is currently unavailable. It will be added in a later update."
    return


    if offhand_action == "handjob":
        return

    if Taboo:
        $ JubesX.inhibition += int(Taboo/10)
        $ JubesX.lust += int(Taboo/5)

    $ JubesX.change_face("_sexy")
    if JubesX.Forced:
        $ JubesX.change_face("_sad")
    elif not JubesX.action_counter["handjob"]:
        $ JubesX.brows = "_confused"
        $ JubesX.eyes = "_sexy"
        $ JubesX.mouth = "_smile"

    call Seen_First_Peen (JubesX, Partner, React=action_context)
    call Jubes_HJ_Launch ("L")

    if action_context == JubesX:

        $ action_context = 0
        if offhand_action == "jackin":
            "[JubesX.name] brushes your hand aside and starts stroking your cock."
        else:
            "[JubesX.name] gives you a mischevious smile, and starts to fondle your cock."
        menu:
            "What do you do?"
            "Nothing.":
                $ JubesX.change_stat("inhibition", 70, 3)
                $ JubesX.change_stat("inhibition", 30, 2)
                "[JubesX.name] continues her actions."
            "Praise her.":
                $ JubesX.change_face("_sexy", 1)
                $ JubesX.change_stat("inhibition", 70, 3)
                ch_p "Oooh, that's good, [JubesX.petname]."
                $ JubesX.nameCheck()
                "[JubesX.name] continues her actions."
                $ JubesX.change_stat("love", 80, 1)
                $ JubesX.change_stat("obedience", 90, 1)
                $ JubesX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ JubesX.change_face("_surprised")
                $ JubesX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that for now, [JubesX.petname]."
                $ JubesX.nameCheck()
                "[JubesX.name] puts it down."
                $ JubesX.change_stat("obedience", 90, 1)
                $ JubesX.change_stat("obedience", 50, 1)
                $ JubesX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ JubesX.add_word(1,"refused","refused")
                return

    if not JubesX.action_counter["handjob"]:
        if JubesX.Forced:
            $ JubesX.change_stat("love", 90, -20)
            $ JubesX.change_stat("obedience", 70, 25)
            $ JubesX.change_stat("inhibition", 80, 30)
        else:
            $ JubesX.change_stat("love", 90, 5)
            $ JubesX.change_stat("obedience", 70, 20)
            $ JubesX.change_stat("inhibition", 80, 20)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ JubesX.drain_word("no_taboo")
    $ JubesX.drain_word("no_handjob")
    $ JubesX.recent_history.append("handjob")
    $ JubesX.daily_history.append("handjob")

label Jubes_HJ_Cycle:
    while Round > 0:
        call shift_focus (JubesX)
        call Jubes_HJ_Launch
        $ JubesX.lust_face()

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
                            if JubesX.remaining_actions and multi_action:
                                $ offhand_action = "fondle_breasts"
                                "You start to fondle her breasts."
                                $ JubesX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (JubesX, "tired")
                        "Shift primary action":

                            if JubesX.remaining_actions and multi_action:
                                menu:
                                    "How about a blowjob?":
                                        if JubesX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Jubes_HJ_After
                                            call Jubes_Blowjob
                                        else:
                                            call Sex_Basic_Dialog (JubesX, "tired")
                                    "How about a titjob?":

                                        if JubesX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Jubes_HJ_After
                                            call Jubes_Titjob
                                        else:
                                            call Sex_Basic_Dialog (JubesX, "tired")
                                    "Never Mind":
                                        jump Jubes_HJ_Cycle
                            else:
                                call Sex_Basic_Dialog (JubesX, "tired")

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [JubesX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (JubesX)
                                "Ask [JubesX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (JubesX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (JubesX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Jubes_HJ_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jubes_HJ_Cycle
                                "Never mind":
                                    jump Jubes_HJ_Cycle
                        "undress [JubesX.name]":
                            call Girl_Undress (JubesX)
                        "Clean up [JubesX.name] (locked)" if not JubesX.spunk:
                            pass
                        "Clean up [JubesX.name]" if JubesX.spunk:
                            call Girl_Cleanup (JubesX, "ask")
                        "Never mind":
                            jump Jubes_HJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jubes_HJ_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jubes_HJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jubes_HJ_Reset
                    $ Line = 0
                    jump Jubes_HJ_After


        call shift_focus (JubesX)
        call Sex_Dialog (JubesX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or JubesX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (JubesX)
                if "_angry" in JubesX.recent_history:
                    call Jubes_HJ_Reset
                    return
                $ JubesX.change_stat("lust", 200, 5)
                if 100 > JubesX.lust >= 70 and JubesX.session_orgasms < 2 and JubesX.SEXP >= 20:
                    $ JubesX.recent_history.append("unsatisfied")
                    $ JubesX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jubes_HJ_After
                $ Line = "came"

            if JubesX.lust >= 100:

                call Girl_Cumming (JubesX)
                if action_context == "shift" or "_angry" in JubesX.recent_history:
                    jump Jubes_HJ_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in JubesX.recent_history:
                    "[JubesX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Jubes_HJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if counter == 20:
            $ JubesX.brows = "_angry"
            menu:
                ch_v "Hmm, this is boring, can we take a break?"
                "How about a BJ?" if JubesX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Jubes_HJ_After
                    call Jubes_Blowjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    jump Jubes_HJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Jubes_HJ_Reset
                    $ action_context = "shift"
                    jump Jubes_HJ_After
                "No, get back down there.":
                    if approval_check(JubesX, 1200) or approval_check(JubesX, 500, "O"):
                        $ JubesX.change_stat("love", 200, -5)
                        $ JubesX.change_stat("obedience", 50, 3)
                        $ JubesX.change_stat("obedience", 80, 2)
                        "She grumbles but gets back to work."
                    else:
                        $ JubesX.change_face("_angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        ch_v "I have better things to do with my time."
                        $ JubesX.change_stat("love", 50, -3, 1)
                        $ JubesX.change_stat("love", 80, -4, 1)
                        $ JubesX.change_stat("obedience", 30, -1, 1)
                        $ JubesX.change_stat("obedience", 50, -1, 1)
                        $ JubesX.recent_history.append("_angry")
                        $ JubesX.daily_history.append("_angry")
                        jump Jubes_HJ_After
        elif counter == 10 and JubesX.SEXP <= 100 and not approval_check(JubesX, 1200, "LO"):
            $ JubesX.brows = "_confused"
            ch_v "This working for you?"


        call Escalation (JubesX)

        if Round == 10:
            call Sex_Basic_Dialog (JubesX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JubesX, 5)


    $ JubesX.change_face("_bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JubesX, "done")

label Jubes_HJ_After:
    $ JubesX.change_face("_sexy")

    $ JubesX.action_counter["handjob"] += 1
    $ JubesX.remaining_actions -=1
    $ JubesX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ JubesX.addiction_rate += 1
    $ JubesX.change_stat("lust", 90, 5)

    call Partner_Like (JubesX, 1)

    if "Jubes Handi-Queen" in Achievements:
        pass
    elif JubesX.action_counter["handjob"] >= 10:
        $ JubesX.change_face("_smile", 1)
        ch_v "Looks like you filled out the punch card, [JubesX.player_petname]."
        $ Achievements.append("Jubes Handi-Queen")
        $ JubesX.SEXP += 5
    elif JubesX.action_counter["handjob"] == 1:
        $ JubesX.SEXP += 10
        if JubesX.love >= 500:
            $ JubesX.mouth = "_smile"
            ch_v "That was kind of. . . pleasant. . ."
        elif Player.focus <= 20:
            $ JubesX.mouth = "_sad"
            ch_v "Did that do it for you?"
    elif JubesX.action_counter["handjob"] == 5:
        ch_v "I think I've got this down, maybe I should get a punch card."

    $ approval_bonus = 0
    if action_context == "shift":
        ch_v "Ok, so what did you have in mind?"
    else:
        call Jubes_HJ_Reset
    call checkout
    return





label Jubes_Titjob:

    "This option is currently unavailable. It will be added in a later update."
    return


    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JubesX)
    if JubesX.action_counter["titjob"] >= 7:
        $ approval_bonus += 10
    elif JubesX.action_counter["titjob"] >= 3:
        $ approval_bonus += 7
    elif JubesX.action_counter["titjob"]:
        $ approval_bonus += 5

    if JubesX.addiction >= 75 and JubesX.event_counter["swallowed"] >=3:
        $ approval_bonus += 15
    elif JubesX.addiction >= 75:
        $ approval_bonus += 5

    if JubesX.SeenChest and approval_check(JubesX, 500):
        $ approval_bonus += 10
    if not JubesX.bra and not JubesX.top:
        $ approval_bonus += 10
    if JubesX.lust > 75:
        $ approval_bonus += 10
    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in JubesX.traits:
        $ approval_bonus += (5*Taboo)
    if JubesX in Player.Harem or "sex friend" in JubesX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JubesX.traits:
        $ approval_bonus -= 30
    if JubesX.event_counter["forced"] and not JubesX.Forced:
        $ approval_bonus -= 5*JubesX.event_counter["forced"]

    if Taboo and "no_taboo" in JubesX.daily_history:
        $ approval_bonus -= 10

    if "no_titjob" in JubesX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_titjob" in JubesX.recent_history else 0

    $ approval = approval_check(JubesX, 1200, TabM = 4)

    if not JubesX.action_counter["titjob"] and "no_titjob" not in JubesX.recent_history:
        $ JubesX.change_face("_surprised", 1)
        $ JubesX.mouth = "_kiss"
        ch_v "You want a titjob, huh?"

    if not JubesX.action_counter["titjob"] and approval:
        if JubesX.Forced:
            $ JubesX.change_face("_sad")
            $ JubesX.change_stat("love", 70, -3, 1)
            $ JubesX.change_stat("love", 20, -2, 1)
        elif JubesX.love >= (JubesX.obedience + JubesX.inhibition):
            $ JubesX.change_face("_sexy")
            $ JubesX.brows = "_sad"
            $ JubesX.mouth = "_smile"
            ch_v "Well, maybe you deserve it."
        elif JubesX.obedience >= JubesX.inhibition:
            $ JubesX.change_face("_normal")
            ch_v "If you'd like that. . ."
        elif JubesX.addiction >= 50:
            $ JubesX.change_face("_manic", 1)
            ch_v "Hmmmm. . . ."
        else:
            $ JubesX.change_face("_sad")
            $ JubesX.mouth = "_smile"
            ch_v "Sounds fun. . ."
    elif approval:
        if JubesX.Forced:
            $ JubesX.change_face("_sad")
            $ JubesX.change_stat("love", 70, -3, 1)
            $ JubesX.change_stat("love", 20, -2, 1)
            ch_v "You're kinda pushing it."
        elif not Taboo and "no_taboo" in JubesX.daily_history:
            ch_v "Ok, I guess this is secluded enough. . ."
        elif "titjob" in JubesX.recent_history:
            $ JubesX.change_face("_sexy", 1)
            ch_v "Huh, again?"
            jump Jubes_TJ_Prep
        elif "titjob" in JubesX.daily_history:
            $ JubesX.change_face("_sexy", 1)
            $ Line = renpy.random.choice(["Back for more?",   
                "You're really working these puppies.", 
                "Didn't get enough earlier?",  
                "You're really working these puppies."])
            ch_v "[Line]"
        elif JubesX.action_counter["titjob"] < 3:
            $ JubesX.change_face("_sexy", 1)
            $ JubesX.brows = "_confused"
            $ JubesX.mouth = "_kiss"
            ch_v "Another titjob??"
        else:
            $ JubesX.change_face("_sexy", 1)
            $ JubesX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action [rubs her chest]?",                 
                "So you'd like another titjob?",                  
                "So you'd like another titjob?",                               
                "So you'd like another titjob?",                              
                "Another titjob?", 
                "A little [points at her chest]?"])
            ch_v "[Line]"
        $ Line = 0

    if approval >= 2:
        if JubesX.Forced:
            $ JubesX.change_face("_sad")
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_stat("inhibition", 60, 1)
            ch_v "Well, could be worse. . ."
        elif "no_titjob" in JubesX.daily_history:
            ch_v "Hmm, I guess. . ."
        else:
            $ JubesX.change_face("_sexy", 1)
            $ JubesX.change_stat("love", 90, 1)
            $ JubesX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, put it here.",                 
                "Well. . . ok.",                 
                "Yum.", 
                "Sure, whip it out.",
                "Fine. . . [She drools a bit into her cleavage].",
                "Heh, ok."])
            ch_v "[Line]"
            $ Line = 0
        $ JubesX.change_stat("obedience", 20, 1)
        $ JubesX.change_stat("obedience", 70, 1)
        $ JubesX.change_stat("inhibition", 80, 2)
        jump Jubes_TJ_Prep
    else:

        $ JubesX.change_face("_angry")
        if "no_titjob" in JubesX.recent_history:
            ch_v "I {i}just{/i} told you \"no,\" [JubesX.player_petname]."
        elif Taboo and "no_taboo" in JubesX.daily_history and "no_titjob" in JubesX.daily_history:
            ch_v "This is just way too exposed!"
        elif "no_titjob" in JubesX.daily_history:
            ch_v "I already told you \"no,\" [JubesX.player_petname]."
        elif Taboo and "no_taboo" in JubesX.daily_history:
            ch_v "This is just way too exposed!"
        elif not JubesX.action_counter["titjob"]:
            $ JubesX.change_face("_bemused")
            ch_v "I'm not really into that, [JubesX.player_petname]. . ."
        else:
            $ JubesX.change_face("_bemused")
            ch_v "Not right now [JubesX.player_petname]. . ."

        menu:
            extend ""
            "Sorry, never mind." if "no_titjob" in JubesX.daily_history:
                $ JubesX.change_face("_bemused")
                ch_v "Yeah, ok, [JubesX.player_petname]."
                return
            "Maybe later?" if "no_titjob" not in JubesX.daily_history:
                $ JubesX.change_face("_sexy")
                ch_v "Maybe."
                $ JubesX.change_stat("love", 80, 2)
                $ JubesX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ JubesX.recent_history.append("no_taboo")
                    $ JubesX.daily_history.append("no_taboo")
                $ JubesX.recent_history.append("no_titjob")
                $ JubesX.daily_history.append("no_titjob")
                return
            "I think this could be fun for both of us. . .":
                if approval:
                    $ JubesX.change_face("_sexy")
                    $ JubesX.change_stat("obedience", 80, 2)
                    $ JubesX.change_stat("obedience", 40, 2)
                    $ JubesX.change_stat("inhibition", 70, 3)
                    $ JubesX.change_stat("inhibition", 40, 2)
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
                    $ approval = approval_check(JubesX, 1100, TabM = 3)
                    if approval >= 2 and JubesX.action_counter["blowjob"]:
                        $ JubesX.change_stat("inhibition", 80, 1)
                        $ JubesX.change_stat("inhibition", 60, 3)
                        $ JubesX.change_face("_confused", 1)
                        ch_v "I could maybe blow you?"
                        menu:
                            ch_v "How about that [[blowjob]?"
                            "Ok, get down there.":
                                $ JubesX.change_stat("love", 80, 2)
                                $ JubesX.change_stat("inhibition", 60, 1)
                                $ JubesX.change_stat("obedience", 50, 1)
                                jump Jubes_BJ_Prep
                            "Nah, it's all about dem titties.":
                                $ Line = "no_BJ"
                    if approval and JubesX.action_counter["handjob"]:
                        $ JubesX.change_stat("inhibition", 80, 1)
                        $ JubesX.change_stat("inhibition", 60, 3)
                        $ JubesX.change_face("_confused", 1)
                        ch_v "I could give you a handy?"
                        menu:
                            ch_v "What do you say?"
                            "Sure, that's fine.":
                                $ JubesX.change_stat("love", 80, 2)
                                $ JubesX.change_stat("inhibition", 60, 1)
                                $ JubesX.change_stat("obedience", 50, 1)
                                jump Jubes_HJ_Prep
                            "Seriously, titties." if Line == "no_BJ":
                                $ Line = 0
                            "Nah, it's all about dem titties." if Line != "no_BJ":
                                pass
                    $ JubesX.change_stat("love", 200, -2)
                    ch_v "Nah."
                    $ JubesX.change_stat("obedience", 70, 2)
            "Come on, let me fuck those titties, [JubesX.petname]":


                $ JubesX.nameCheck()
                $ approval = approval_check(JubesX, 700, "OI", TabM = 4)
                if approval > 1 or (approval and JubesX.Forced):
                    $ JubesX.change_face("_sad")
                    $ JubesX.change_stat("love", 70, -5, 1)
                    $ JubesX.change_stat("love", 200, -2)
                    ch_v "Ok, fine, whip it out."
                    $ JubesX.change_stat("obedience", 50, 4)
                    $ JubesX.change_stat("inhibition", 80, 1)
                    $ JubesX.change_stat("inhibition", 60, 3)
                    $ JubesX.Forced = 1
                    jump Jubes_TJ_Prep
                else:
                    $ JubesX.change_stat("love", 200, -15)
                    $ JubesX.recent_history.append("_angry")
                    $ JubesX.daily_history.append("_angry")


    if "no_titjob" in JubesX.daily_history:
        $ JubesX.change_face("_angry", 1)
        ch_v "Look, I already told you no."
        $ JubesX.recent_history.append("_angry")
        $ JubesX.daily_history.append("_angry")
    elif JubesX.Forced:
        $ JubesX.change_face("_angry", 1)
        ch_v "No, try something else."
        $ JubesX.change_stat("lust", 200, 5)
        if JubesX.love > 300:
            $ JubesX.change_stat("love", 70, -2)
        $ JubesX.change_stat("obedience", 50, -2)
        $ JubesX.recent_history.append("_angry")
        $ JubesX.daily_history.append("_angry")
    elif Taboo:
        $ JubesX.change_face("_angry", 1)
        $ JubesX.daily_history.append("no_taboo")
        ch_v "You really expect me to do that here? This isn't exactly \"covert.\""
        $ JubesX.change_stat("lust", 200, 5)
        $ JubesX.change_stat("obedience", 50, -3)
    elif JubesX.action_counter["titjob"]:
        $ JubesX.change_face("_sad")
        ch_v "You'll know when it's time for that."
    else:
        $ JubesX.change_face("_normal", 1)
        ch_v "Nah."
    $ JubesX.recent_history.append("no_titjob")
    $ JubesX.daily_history.append("no_titjob")
    $ approval_bonus = 0
    return

label Jubes_TJ_Prep:

    "This option is currently unavailable. It will be added in a later update."
    return


    if Taboo:
        $ JubesX.inhibition += int(Taboo/10)
        $ JubesX.lust += int(Taboo/5)


    $ JubesX.change_face("_sexy")
    if JubesX.Forced:
        $ JubesX.change_face("_sad")
    elif not JubesX.action_counter["titjob"]:
        $ JubesX.brows = "_confused"
        $ JubesX.eyes = "_sexy"
        $ JubesX.mouth = "_smile"

    call Seen_First_Peen (JubesX, Partner, React=action_context)
    call Jubes_TJ_Launch ("L")

    if action_context == JubesX:

        $ action_context = 0
        "[JubesX.name] slides down and sandwiches your dick between her tits."
        menu:
            "What do you do?"
            "Nothing.":
                $ JubesX.change_stat("inhibition", 80, 3)
                $ JubesX.change_stat("inhibition", 40, 2)
                "[JubesX.name] starts to slide them up and down."
            "Praise her.":
                $ JubesX.change_face("_sexy", 1)
                $ JubesX.change_stat("inhibition", 80, 3)
                ch_p "Oh, that sounds like a good idea, [JubesX.petname]."
                $ JubesX.nameCheck()
                "[JubesX.name] continues her actions."
                $ JubesX.change_stat("love", 85, 1)
                $ JubesX.change_stat("obedience", 90, 1)
                $ JubesX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ JubesX.change_face("_confused")
                $ JubesX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that for now, [JubesX.petname]."
                $ JubesX.nameCheck()
                "[JubesX.name] lets it drop out from between her breasts."
                $ JubesX.change_stat("obedience", 90, 1)
                $ JubesX.change_stat("obedience", 50, 3)
                $ Player.recent_history.append("nope")
                $ JubesX.add_word(1,"refused","refused")
                return

    if not JubesX.action_counter["titjob"]:
        if JubesX.Forced:
            $ JubesX.change_stat("love", 90, -25)
            $ JubesX.change_stat("obedience", 70, 30)
            $ JubesX.change_stat("inhibition", 80, 35)
        else:
            $ JubesX.change_stat("love", 90, 5)
            $ JubesX.change_stat("obedience", 70, 25)
            $ JubesX.change_stat("inhibition", 80, 30)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ JubesX.drain_word("no_taboo")
    $ JubesX.drain_word("no_titjob")
    $ JubesX.recent_history.append("titjob")
    $ JubesX.daily_history.append("titjob")

label Jubes_TJ_Cycle:
    while Round > 0:
        call shift_focus (JubesX)
        call Jubes_TJ_Launch
        $ JubesX.lust_face()

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
                            if JubesX.remaining_actions and multi_action:
                                $ offhand_action = "fondle_breasts"
                                "You start to fondle her breasts."
                                $ JubesX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (JubesX, "tired")
                        "Shift primary action":

                            if JubesX.remaining_actions and multi_action:
                                menu:
                                    "How about a blowjob?":
                                        if JubesX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Jubes_TJ_After
                                            call Jubes_Blowjob
                                        else:
                                            call Sex_Basic_Dialog (JubesX, "tired")
                                    "How about a handy?":

                                        if JubesX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Jubes_BJ_After
                                            call Jubes_Handjob
                                        else:
                                            call Sex_Basic_Dialog (JubesX, "tired")
                                    "Never Mind":
                                        jump Jubes_TJ_Cycle
                            else:
                                call Sex_Basic_Dialog (JubesX, "tired")

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [JubesX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (JubesX)
                                "Ask [JubesX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (JubesX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (JubesX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Jubes_TJ_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jubes_TJ_Cycle
                                "Never mind":
                                    jump Jubes_TJ_Cycle
                        "undress [JubesX.name]":
                            call Girl_Undress (JubesX)
                        "Clean up [JubesX.name] (locked)" if not JubesX.spunk:
                            pass
                        "Clean up [JubesX.name]" if JubesX.spunk:
                            call Girl_Cleanup (JubesX, "ask")
                        "Never mind":
                            jump Jubes_TJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jubes_TJ_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jubes_TJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jubes_TJ_Reset
                    $ Line = 0
                    jump Jubes_TJ_After


        call shift_focus (JubesX)
        call Sex_Dialog (JubesX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or JubesX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (JubesX)
                if "_angry" in JubesX.recent_history:
                    call Jubes_TJ_Reset
                    return
                $ JubesX.change_stat("lust", 200, 5)
                if 100 > JubesX.lust >= 70 and JubesX.session_orgasms < 2 and JubesX.SEXP >= 20:
                    $ JubesX.recent_history.append("unsatisfied")
                    $ JubesX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jubes_TJ_After
                $ Line = "came"

            if JubesX.lust >= 100:

                call Girl_Cumming (JubesX)
                if action_context == "shift" or "_angry" in JubesX.recent_history:
                    jump Jubes_TJ_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in JubesX.recent_history:
                    "[JubesX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Jubes_TJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)
        if action_speed >= 4:
            call action_speed_Shift (0)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if JubesX.SEXP >= 100 or approval_check(JubesX, 1200, "LO"):
            pass
        elif counter == (5 + JubesX.action_counter["titjob"]):
            $ JubesX.brows = "_confused"
            ch_v "Are you getting close here? I'm getting bored."
        if counter == (10 + JubesX.action_counter["titjob"]):
            $ JubesX.brows = "_angry"
            menu:
                ch_v "Seriously, can we do something else?"
                "How about a BJ?" if JubesX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Jubes_TJ_After
                    call Jubes_Blowjob
                    return
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    jump Jubes_TJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Jubes_TJ_Reset
                    $ action_context = "shift"
                    jump Jubes_TJ_After
                "No, get back down there.":
                    if approval_check(JubesX, 1200) or approval_check(JubesX, 500, "O"):
                        $ JubesX.change_stat("love", 200, -5)
                        $ JubesX.change_stat("obedience", 50, 3)
                        $ JubesX.change_stat("obedience", 80, 2)
                        "She grumbles but gets back to work."
                    else:
                        $ JubesX.change_face("_angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        ch_v "Well fuck you then."
                        $ JubesX.change_stat("love", 50, -3, 1)
                        $ JubesX.change_stat("love", 80, -4, 1)
                        $ JubesX.change_stat("obedience", 30, -1, 1)
                        $ JubesX.change_stat("obedience", 50, -1, 1)
                        $ JubesX.recent_history.append("_angry")
                        $ JubesX.daily_history.append("_angry")
                        jump Jubes_TJ_After


        call Escalation (JubesX)

        if Round == 10:
            call Sex_Basic_Dialog (JubesX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JubesX, 5)


    $ JubesX.change_face("_bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JubesX, "done")

label Jubes_TJ_After:
    $ JubesX.change_face("_sexy")

    $ JubesX.action_counter["titjob"] += 1
    $ JubesX.remaining_actions -=1
    $ JubesX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ JubesX.addiction_rate += 1

    call Partner_Like (JubesX, 4)

    if JubesX.action_counter["titjob"] > 5:
        pass
    elif JubesX.action_counter["titjob"] == 1:
        $ JubesX.SEXP += 12
        if JubesX.love >= 500:
            $ JubesX.mouth = "_smile"
            ch_v "That was fun."
        elif Player.focus <= 20:
            $ JubesX.mouth = "_sad"
            ch_v "Well I hope you got something out of that."
    elif JubesX.action_counter["titjob"] == 5:
        ch_v "You seem to enjoy that."

    $ approval_bonus = 0

    if action_context == "shift":
        ch_v "Mmm, so what else did you have in mind?"
    else:
        call Jubes_TJ_Reset
    call checkout
    return







label Jubes_Blowjob:

    "This option is currently unavailable. It will be added in a later update."
    return


    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JubesX)
    if JubesX.action_counter["blowjob"] >= 7:
        $ approval_bonus += 15
    elif JubesX.action_counter["blowjob"] >= 3:
        $ approval_bonus += 10
    elif JubesX.action_counter["blowjob"]:
        $ approval_bonus += 7

    if JubesX.addiction >= 75 and JubesX.event_counter["swallowed"] >=3:
        $ approval_bonus += 25
    elif JubesX.addiction >= 75:
        $ approval_bonus += 15

    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in JubesX.traits:
        $ approval_bonus += (4*Taboo)
    if JubesX in Player.Harem or "sex friend" in JubesX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JubesX.traits:
        $ approval_bonus -= 40
    if JubesX.event_counter["forced"] and not JubesX.Forced:
        $ approval_bonus -= 5*JubesX.event_counter["forced"]

    if Taboo and "no_taboo" in JubesX.daily_history:
        $ approval_bonus -= 10

    if "no_blowjob" in JubesX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_blowjob" in JubesX.recent_history else 0

    $ approval = approval_check(JubesX, 1300, TabM = 4)

    if not JubesX.action_counter["blowjob"] and "no_blowjob" not in JubesX.recent_history:
        $ JubesX.change_face("_surprised", 2)
        $ JubesX.mouth = "_kiss"
        ch_v "You want me to suck your cock?"
        if JubesX.action_counter["handjob"]:
            $ JubesX.mouth = "_smile"
            ch_v "Handjobs not enough now?"
        $ JubesX.blushing = "_blush1"

    if not JubesX.action_counter["blowjob"] and approval:
        if JubesX.Forced:
            $ JubesX.change_face("_sad")
            $ JubesX.change_stat("love", 70, -3, 1)
            $ JubesX.change_stat("love", 20, -2, 1)
        elif JubesX.love >= (JubesX.obedience + JubesX.inhibition):
            $ JubesX.change_face("_sexy")
            $ JubesX.brows = "_sad"
            $ JubesX.mouth = "_smile"
            ch_v "I have wondered how you taste."
        elif JubesX.obedience >= JubesX.inhibition:
            $ JubesX.change_face("_normal")
            ch_v "If that's what you want. . ."
        elif JubesX.addiction >= 50:
            $ JubesX.change_face("_manic", 1)
            ch_v "[[wipes away a little drool]"
        else:
            $ JubesX.change_face("_sad")
            $ JubesX.mouth = "_smile"
            ch_v "Huh. . ."
    elif approval:
        if JubesX.Forced:
            $ JubesX.change_face("_sad")
            $ JubesX.change_stat("love", 70, -3, 1)
            $ JubesX.change_stat("love", 20, -2, 1)
            ch_v "Again?"
        elif not Taboo and "no_taboo" in JubesX.daily_history:
            ch_v "Hmm, this is private enough. . ."
        elif "blowjob" in JubesX.recent_history:
            $ JubesX.change_face("_sexy", 1)
            ch_v "Mmm, again? [[yawns]"
            jump Jubes_BJ_Prep
        elif "blowjob" in JubesX.daily_history:
            $ JubesX.change_face("_sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",   
                "Wear'in me out here.",  
                "I must be too good at this.", 
                "Let me get some saliva going.",
                "Didn't get enough earlier?"])
            ch_v "[Line]"
        elif JubesX.action_counter["blowjob"] < 3:
            $ JubesX.change_face("_sexy", 1)
            $ JubesX.brows = "_confused"
            $ JubesX.mouth = "_kiss"
            ch_v "You'd like another blowjob?"
        else:
            $ JubesX.change_face("_sexy", 1)
            $ JubesX.ArmPose = 2
            $ Line = renpy.random.choice(["You want me to [mimes blowing]?",                 
                "So you want another blowjob?",                 
                "You want me to lick you?", 
                "You want me to suck you off?",
                "A little bj?"])
            ch_v "[Line]"
        $ Line = 0

    if approval >= 2:
        if JubesX.Forced:
            $ JubesX.change_face("_sad")
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_stat("inhibition", 60, 1)
            ch_v "Whatever."
        elif "no_blowjob" in JubesX.daily_history:
            ch_v "Fine. . ."
        else:
            $ JubesX.change_face("_sexy", 1)
            $ JubesX.change_stat("love", 90, 1)
            $ JubesX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Sure. Ahhhhhh.",                 
                "Well. . . alright.",                 
                "Yum.", 
                "Sure, whip it out.",
                "Ok. . . [She licks her lips].",
                "Alright, let's see it."])
            ch_v "[Line]"
            $ Line = 0
        $ JubesX.change_stat("obedience", 20, 1)
        $ JubesX.change_stat("obedience", 70, 1)
        $ JubesX.change_stat("inhibition", 80, 2)
        jump Jubes_BJ_Prep
    else:

        $ JubesX.change_face("_angry")
        if "no_blowjob" in JubesX.recent_history:
            ch_v "Just told you I wouldn't, [JubesX.player_petname]."
        elif Taboo and "no_taboo" in JubesX.daily_history and "no_blowjob" in JubesX.daily_history:
            ch_v "Like I told you, not in public."
        elif "no_blowjob" in JubesX.daily_history:
            ch_v "Told you \"no,\" [JubesX.player_petname]."
        elif Taboo and "no_taboo" in JubesX.daily_history:
            ch_v "Like I told you, too public!"
        elif not JubesX.action_counter["blowjob"]:
            $ JubesX.change_face("_bemused")
            ch_v "I don't know if your taste will match your scent, [JubesX.player_petname]. . ."
        else:
            $ JubesX.change_face("_bemused")
            ch_v "I don't know, [JubesX.player_petname]!"
        menu:
            extend ""
            "Sorry, never mind." if "no_blowjob" in JubesX.daily_history:
                $ JubesX.change_face("_bemused")
                ch_v "Cool."
                return
            "Maybe later?" if "no_blowjob" not in JubesX.daily_history:
                $ JubesX.change_face("_sexy")
                ch_v "Yeah, maybe, [JubesX.player_petname]."
                $ JubesX.change_stat("love", 80, 2)
                $ JubesX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ JubesX.recent_history.append("no_taboo")
                    $ JubesX.daily_history.append("no_taboo")
                $ JubesX.recent_history.append("no_blowjob")
                $ JubesX.daily_history.append("no_blowjob")
                return
            "Come on, please?":
                if approval:
                    $ JubesX.change_face("_sexy")
                    $ JubesX.change_stat("obedience", 90, 2)
                    $ JubesX.change_stat("obedience", 50, 2)
                    $ JubesX.change_stat("inhibition", 70, 3)
                    $ JubesX.change_stat("inhibition", 40, 2)
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
                    if approval_check(JubesX, 1100, TabM = 3):
                        $ JubesX.change_stat("inhibition", 80, 1)
                        $ JubesX.change_stat("inhibition", 60, 3)
                        $ JubesX.change_face("_confused", 1)
                        $ JubesX.ArmPose = 2
                        if JubesX.action_counter["handjob"]:
                            ch_v "Couldn't I just use my hand again?"
                            ch_v "You seemed to like that."
                        else:
                            ch_v "I could maybe use my hand instead, how's that sound?"
                        menu:
                            extend ""
                            "Sure, that's fine.":
                                $ JubesX.change_stat("love", 80, 2)
                                $ JubesX.change_stat("inhibition", 60, 1)
                                $ JubesX.change_stat("obedience", 50, 1)
                                jump Jubes_HJ_Prep
                            "Nah, if it's not a BJ, forget it.":
                                $ JubesX.change_stat("love", 200, -2)
                                $ JubesX.ArmPose = 1
                                ch_v "Fine, be that way."
                                $ JubesX.change_stat("obedience", 70, 2)
            "Suck it, [JubesX.petname]":


                $ JubesX.nameCheck()
                $ approval = approval_check(JubesX, 750, "OI", TabM = 3)
                if approval > 1 or (approval and JubesX.Forced):
                    $ JubesX.change_face("_sad")
                    $ JubesX.change_stat("love", 70, -5, 1)
                    $ JubesX.change_stat("love", 200, -2)
                    ch_v "Whatever. . ."
                    $ JubesX.change_stat("obedience", 50, 4)
                    $ JubesX.change_stat("inhibition", 80, 1)
                    $ JubesX.change_stat("inhibition", 60, 3)
                    $ JubesX.Forced = 1
                    jump Jubes_BJ_Prep
                else:
                    $ JubesX.change_stat("love", 200, -15)
                    $ JubesX.recent_history.append("_angry")
                    $ JubesX.daily_history.append("_angry")


    if "no_blowjob" in JubesX.daily_history:
        $ JubesX.change_face("_angry", 1)
        $ JubesX.ArmPose = 2
        $ JubesX.Claws = 1
        ch_v "Suck this then."
        $ JubesX.ArmPose = 1
        $ JubesX.Claws = 0
        $ JubesX.recent_history.append("_angry")
        $ JubesX.daily_history.append("_angry")
    elif JubesX.Forced:
        $ JubesX.change_face("_angry", 1)
        ch_v "That's just pushing it."
        $ JubesX.change_stat("lust", 200, 5)
        if JubesX.love > 300:
            $ JubesX.change_stat("love", 70, -2)
        $ JubesX.change_stat("obedience", 50, -2)
        $ JubesX.recent_history.append("_angry")
        $ JubesX.daily_history.append("_angry")
        $ JubesX.recent_history.append("no_blowjob")
        $ JubesX.daily_history.append("no_blowjob")
        return
    elif Taboo:
        $ JubesX.change_face("_angry", 1)
        $ JubesX.daily_history.append("no_taboo")
        ch_v "This area's too exposed."
        $ JubesX.change_stat("lust", 200, 5)
        $ JubesX.change_stat("obedience", 50, -3)
        return
    elif JubesX.action_counter["blowjob"]:
        $ JubesX.change_face("_sad")
        ch_v "Nah, not this time."
    else:
        $ JubesX.change_face("_normal", 1)
        ch_v "Nope."
    $ JubesX.recent_history.append("no_blowjob")
    $ JubesX.daily_history.append("no_blowjob")
    $ approval_bonus = 0
    return


label Jubes_BJ_Prep:

    "This option is currently unavailable. It will be added in a later update."
    return


    if renpy.showing("Jubes_HJ_Animation"):
        hide Jubes_HJ_Animation with easeoutbottom
    if Taboo:
        $ JubesX.inhibition += int(Taboo/10)
        $ JubesX.lust += int(Taboo/5)

    $ JubesX.change_face("_sexy")
    if JubesX.Forced:
        $ JubesX.change_face("_sad")
    elif not JubesX.action_counter["blowjob"]:
        $ JubesX.brows = "_confused"
        $ JubesX.eyes = "_sexy"
        $ JubesX.mouth = "_smile"

    call Seen_First_Peen (JubesX, Partner, React=action_context)
    call Jubes_BJ_Launch ("L")
    if action_context == JubesX:

        $ action_context = 0
        "[JubesX.name] slides down and gives your cock a little lick."
        menu:
            "What do you do?"
            "Nothing.":
                $ JubesX.change_stat("inhibition", 80, 3)
                $ JubesX.change_stat("inhibition", 40, 2)
                "[JubesX.name] continues licking at it."
            "Praise her.":
                $ JubesX.change_face("_sexy", 1)
                $ JubesX.change_stat("inhibition", 80, 3)
                ch_p "Hmmm, keep doing that, [JubesX.petname]."
                $ JubesX.nameCheck()
                "[JubesX.name] continues her actions."
                $ JubesX.change_stat("love", 85, 1)
                $ JubesX.change_stat("obedience", 90, 1)
                $ JubesX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ JubesX.change_face("_surprised")
                $ JubesX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that for now, [JubesX.petname]."
                $ JubesX.nameCheck()
                "[JubesX.name] puts it down."
                $ JubesX.change_stat("obedience", 90, 1)
                $ JubesX.change_stat("obedience", 50, 3)
                $ Player.recent_history.append("nope")
                $ JubesX.add_word(1,"refused","refused")
                return
    if not JubesX.action_counter["blowjob"]:
        if JubesX.Forced:
            $ JubesX.change_stat("love", 90, -70)
            $ JubesX.change_stat("obedience", 70, 45)
            $ JubesX.change_stat("inhibition", 80, 60)
        else:
            $ JubesX.change_stat("love", 90, 5)
            $ JubesX.change_stat("obedience", 70, 35)
            $ JubesX.change_stat("inhibition", 80, 40)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ JubesX.drain_word("no_taboo")
    $ JubesX.drain_word("no_blowjob")
    $ JubesX.recent_history.append("blowjob")
    $ JubesX.daily_history.append("blowjob")

label Jubes_BJ_Cycle:
    while Round > 0:
        call shift_focus (JubesX)
        call Jubes_BJ_Launch
        $ JubesX.lust_face()

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

                    if "Gwentro" not in JubesX.history:
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

                    "[JubesX.name] hums contentedly."
                    if "setpace" not in JubesX.recent_history:
                        $ JubesX.change_stat("love", 80, 2)
                    $ D20 = renpy.random.randint(1, 20)
                    if JubesX.action_counter["blowjob"] < 5:
                        $ D20 -= 10
                    elif JubesX.action_counter["blowjob"] < 10:
                        $ D20 -= 5

                    if D20 > 15:
                        call action_speed_Shift (4)
                        if "setpace" not in JubesX.recent_history:
                            $ JubesX.change_stat("inhibition", 80, 3)
                    elif D20 > 10:
                        call action_speed_Shift (3)
                    elif D20 > 5:
                        call action_speed_Shift (2)
                    else:
                        call action_speed_Shift (1)
                    $ JubesX.recent_history.append("setpace")

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
                            if JubesX.remaining_actions and multi_action:
                                $ offhand_action = "fondle_breasts"
                                "You start to fondle her breasts."
                                $ JubesX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (JubesX, "tired")
                        "Shift primary action":

                            if JubesX.remaining_actions and multi_action:
                                menu:
                                    "How about a handy?":
                                        if JubesX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Jubes_BJ_After
                                            call Jubes_Handjob
                                        else:
                                            ch_v "I need a break, can we wrap on this?"
                                    "How about a titjob?":
                                        if JubesX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Jubes_BJ_After
                                            call Jubes_Titjob
                                        else:
                                            ch_v "I need a break, can we wrap on this?"
                                    "Never Mind":
                                        jump Jubes_BJ_Cycle
                            else:
                                call Sex_Basic_Dialog (JubesX, "tired")

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [JubesX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (JubesX)
                                "Ask [JubesX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (JubesX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (JubesX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Jubes_BJ_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jubes_BJ_Cycle
                                "Never mind":
                                    jump Jubes_BJ_Cycle
                        "undress [JubesX.name]":
                            call Girl_Undress (JubesX)
                        "Clean up [JubesX.name] (locked)" if not JubesX.spunk:
                            pass
                        "Clean up [JubesX.name]" if JubesX.spunk:
                            call Girl_Cleanup (JubesX, "ask")
                        "Never mind":
                            jump Jubes_BJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jubes_BJ_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jubes_BJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jubes_BJ_Reset
                    $ Line = 0
                    jump Jubes_BJ_After


        call shift_focus (JubesX)
        call Sex_Dialog (JubesX, Partner)



        $ counter += 1
        $ Round -= 1
        if action_speed:
            $ Player.cock_wet = 1
            $ Player.spunk = 0 if Player.spunk else Player.spunk

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or JubesX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (JubesX)
                if "_angry" in JubesX.recent_history:
                    call Jubes_BJ_Reset
                    return
                $ JubesX.change_stat("lust", 200, 5)
                if 100 > JubesX.lust >= 70 and JubesX.session_orgasms < 2 and JubesX.SEXP >= 20:
                    $ JubesX.recent_history.append("unsatisfied")
                    $ JubesX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jubes_BJ_After
                $ Line = "came"

            if JubesX.lust >= 100:

                call Girl_Cumming (JubesX)
                if action_context == "shift" or "_angry" in JubesX.recent_history:
                    jump Jubes_BJ_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."

                if "unsatisfied" in JubesX.recent_history:
                    "[JubesX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Jubes_BJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if JubesX.SEXP >= 100 or approval_check(JubesX, 1200, "LO"):
            pass
        elif counter == (10 + JubesX.action_counter["blowjob"]):
            $ JubesX.brows = "_angry"
            menu:
                ch_v "I'm getting kinda bored. Can we do something else?"
                "How about a Handy?" if JubesX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Jubes_BJ_After
                    call Jubes_Handjob
                    return
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    jump Jubes_BJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Jubes_BJ_Reset
                    $ action_context = "shift"
                    jump Jubes_BJ_After
                "No, get back down there.":
                    if approval_check(JubesX, 1200) or approval_check(JubesX, 500, "O"):
                        $ JubesX.change_stat("love", 200, -5)
                        $ JubesX.change_stat("obedience", 50, 3)
                        $ JubesX.change_stat("obedience", 80, 2)
                        "She grumbles but gets back to work."
                    else:
                        $ JubesX.change_face("_angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        ch_v "Well fuck you then."
                        $ JubesX.change_stat("love", 50, -3, 1)
                        $ JubesX.change_stat("love", 80, -4, 1)
                        $ JubesX.change_stat("obedience", 30, -1, 1)
                        $ JubesX.change_stat("obedience", 50, -1, 1)
                        $ JubesX.recent_history.append("_angry")
                        $ JubesX.daily_history.append("_angry")
                        jump Jubes_BJ_After
        elif counter == (5 + JubesX.action_counter["blowjob"]) and JubesX.SEXP <= 100 and not approval_check(JubesX, 1200, "LO"):
            $ JubesX.brows = "_confused"
            ch_v "Are you getting close here? I'm bored."


        call Escalation (JubesX)

        if Round == 10:
            call Sex_Basic_Dialog (JubesX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JubesX, 5)


    $ JubesX.change_face("_bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JubesX, "done")

label Jubes_BJ_After:
    $ JubesX.change_face("_sexy")

    $ JubesX.action_counter["blowjob"] += 1
    $ JubesX.remaining_actions -=1
    $ JubesX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ JubesX.addiction_rate += 1

    call Partner_Like (JubesX, 2)

    if "Jubes Jobber" in Achievements:
        pass
    elif JubesX.action_counter["blowjob"] >= 10:
        $ JubesX.change_face("_smile", 1)
        ch_v "Your flavor is intoxicating."
        $ Achievements.append("Jubes Jobber")
        $ JubesX.SEXP += 5
    elif action_context == "shift":
        pass
    elif JubesX.action_counter["blowjob"] == 1:
        $ JubesX.SEXP += 15
        if JubesX.love >= 500:
            $ JubesX.mouth = "_smile"
            ch_v "Hey, whaddaya know, that wasn't bad."
        elif Player.focus <= 20:
            $ JubesX.mouth = "_sad"
            ch_v "I hope you enjoyed that."
    elif JubesX.action_counter["blowjob"] == 5:
        ch_v "I'm really getting the hang of this. . . right?"
        menu:
            "[[nod]":
                $ JubesX.change_face("_smile", 1)
                $ JubesX.change_stat("love", 90, 15)
                $ JubesX.change_stat("obedience", 80, 5)
                $ JubesX.change_stat("inhibition", 90, 10)
            "[[shake head \"no\"]":
                if approval_check(JubesX, 500, "O"):
                    $ JubesX.change_face("_sad", 2)
                    $ JubesX.change_stat("love", 200, -5)
                else:
                    $ JubesX.change_face("_angry", 2)
                    $ JubesX.change_stat("love", 200, -25)
                $ JubesX.change_stat("obedience", 80, 10)
                ch_v ". . ."
                $ JubesX.change_face("_sad", 1)

    $ approval_bonus = 0
    if action_context != "shift":
        call Jubes_BJ_Reset
    call checkout
    return






label Jubes_Dildo_Check:
    if "_dildo" in Player.inventory:
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "_dildo" in JubesX.inventory:
        "You ask [JubesX.name] to get out her favorite Dildo."
    else:
        "You don't have one of those on you."
        return 0
    return 1

label Jubes_Dildo_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JubesX)
    call Jubes_Dildo_Check
    if not _return:
        return

    if JubesX.action_counter["dildo_pussy"]:
        $ approval_bonus += 15
    if JubesX.legs == "pants:":
        $ approval_bonus -= 20

    if JubesX.lust > 95:
        $ approval_bonus += 20
    elif JubesX.lust > 85:
        $ approval_bonus += 15

    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in JubesX.traits:
        $ approval_bonus += (5*Taboo)
    if JubesX in Player.Harem or "sex friend" in JubesX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JubesX.traits:
        $ approval_bonus -= 40
    if JubesX.event_counter["forced"] and not JubesX.Forced:
        $ approval_bonus -= 5*JubesX.event_counter["forced"]

    if Taboo and "no_taboo" in JubesX.daily_history:
        $ approval_bonus -= 10

    if "no_dildo" in JubesX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_dildo" in JubesX.recent_history else 0

    $ approval = approval_check(JubesX, 1250, TabM = 4)

    if action_context == JubesX:
        if approval > 2:
            if JubesX.PantsNum() == 5:
                "[JubesX.name] grabs her dildo, hiking up her skirt as she does."
                $ JubesX.upskirt = 1
            elif JubesX.PantsNum() >= 6:
                "[JubesX.name] grabs her dildo, pulling down her pants as she does."
                $ JubesX.legs = ""
            else:
                "[JubesX.name] grabs her dildo, rubbing is suggestively against her crotch."
            $ JubesX.SeenPanties = 1
            call Jubes_First_Bottomless (1)
            "She slides the tip along her pussy and seems to want you to insert it."
            menu:
                "What do you do?"
                "Nothing.":
                    $ JubesX.change_stat("inhibition", 80, 3)
                    $ JubesX.change_stat("inhibition", 50, 2)
                    "[JubesX.name] slides it in."
                "Go for it.":
                    $ JubesX.change_face("_sexy", 1)
                    $ JubesX.change_stat("inhibition", 80, 3)
                    ch_p "Oh yeah, [JubesX.petname], let's do this."
                    $ JubesX.nameCheck()
                    "You grab the dildo and slide it in."
                    $ JubesX.change_stat("love", 85, 1)
                    $ JubesX.change_stat("obedience", 90, 1)
                    $ JubesX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ JubesX.change_face("_surprised")
                    $ JubesX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that right now, [JubesX.petname]."
                    $ JubesX.nameCheck()
                    "[JubesX.name] sets the dildo down."
                    $ JubesX.change_outfit()
                    $ JubesX.change_stat("obedience", 90, 1)
                    $ JubesX.change_stat("obedience", 50, 1)
                    $ JubesX.change_stat("obedience", 30, 2)
                    return
            jump Jubes_DP_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
        return

    if action_context == "auto":
        "You rub the dildo across her body, and along her moist slit."
        $ JubesX.change_face("_surprised", 1)

        if (JubesX.action_counter["dildo_pussy"] and approval) or (approval > 1):
            "[JubesX.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            $ JubesX.change_face("_sexy")
            $ JubesX.change_stat("obedience", 70, 3)
            $ JubesX.change_stat("inhibition", 50, 3)
            $ JubesX.change_stat("inhibition", 70, 1)
            ch_v "Ooo, [JubesX.player_petname], toys!"
            jump Jubes_DP_Prep
        else:
            $ JubesX.brows = "_angry"
            menu:
                ch_v "Hey, what are you planning to do with that?!"
                "Sorry, sorry! Never mind.":
                    if approval:
                        $ JubesX.change_face("_sexy", 1)
                        $ JubesX.change_stat("obedience", 70, 3)
                        $ JubesX.change_stat("inhibition", 50, 3)
                        $ JubesX.change_stat("inhibition", 70, 1)
                        ch_v "Well, now that you mention it. . ."
                        jump Jubes_DP_Prep
                    "You pull back before you really get it in."
                    $ JubesX.change_face("_bemused", 1)
                    if JubesX.action_counter["dildo_pussy"]:
                        ch_v "Well ok, [JubesX.player_petname], maybe warn me next time?"
                    else:
                        ch_v "Well ok, [JubesX.player_petname], that's a little much. . . for now . . ."
                "Just playing with my favorite toys.":
                    $ JubesX.change_stat("love", 80, -10, 1)
                    $ JubesX.change_stat("love", 200, -10)
                    "You press it inside some more."
                    $ JubesX.change_stat("obedience", 70, 3)
                    $ JubesX.change_stat("inhibition", 50, 3)
                    if not approval_check(JubesX, 700, "O", TabM=1):
                        $ JubesX.change_face("_angry")
                        "[JubesX.name] shoves you away and slaps you in the face."
                        ch_v "Jerk!"
                        ch_v "Ask nice if you want to stick something in my pussy!"
                        $ JubesX.change_stat("love", 50, -10, 1)
                        $ JubesX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        if renpy.showing("Jubes_SexSprite"):
                            call Jubes_Sex_Reset
                        $ JubesX.recent_history.append("_angry")
                        $ JubesX.daily_history.append("_angry")
                    else:
                        $ JubesX.change_face("_sad")
                        "[JubesX.name] doesn't seem to be into this, you're lucky she's so obedient."
                        jump Jubes_DP_Prep
        return


    if not JubesX.action_counter["dildo_pussy"]:

        $ JubesX.change_face("_surprised", 1)
        $ JubesX.mouth = "_kiss"
        ch_v "Hmmm, so you'd like to try out some toys?"
        if JubesX.Forced:
            $ JubesX.change_face("_sad")
            ch_v "I suppose there are worst things you could ask for."

    if not JubesX.action_counter["dildo_pussy"] and approval:

        if JubesX.Forced:
            $ JubesX.change_face("_sad")
            $ JubesX.change_stat("love", 70, -3, 1)
            $ JubesX.change_stat("love", 20, -2, 1)
        elif JubesX.love >= (JubesX.obedience + JubesX.inhibition):
            $ JubesX.change_face("_sexy")
            $ JubesX.brows = "_sad"
            $ JubesX.mouth = "_smile"
            ch_v "I've had a reasonable amount of experience with these, you know. . ."
        elif JubesX.obedience >= JubesX.inhibition:
            $ JubesX.change_face("_normal")
            ch_v "If that's what you want, [JubesX.player_petname]. . ."
        else:
            $ JubesX.change_face("_sad")
            $ JubesX.mouth = "_smile"
            ch_v "I guess it could be fun with a partner. . ."

    elif approval:

        if JubesX.Forced:
            $ JubesX.change_face("_sad")
            $ JubesX.change_stat("love", 70, -3, 1)
            $ JubesX.change_stat("love", 20, -2, 1)
            ch_v "The toys again?"
        elif not Taboo and "no_taboo" in JubesX.daily_history:
            ch_v "Well, at least you got us some privacy this time. . ."
        elif "dildo_pussy" in JubesX.recent_history:
            $ JubesX.change_face("_sexy", 1)
            ch_v "Mmm, again? Ok, let's get to it."
            jump Jubes_DP_Prep
        elif "dildo_pussy" in JubesX.daily_history:
            $ JubesX.change_face("_sexy", 1)
            $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "You're going to wear me out."])
            ch_v "[Line]"
        elif JubesX.action_counter["dildo_pussy"] < 3:
            $ JubesX.change_face("_sexy", 1)
            $ JubesX.brows = "_confused"
            $ JubesX.mouth = "_kiss"
            ch_v "You want to stick it in my pussy again?"
        else:
            $ JubesX.change_face("_sexy", 1)
            $ JubesX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my pussy again?",
                    "You want me ta lube up your toy?"])
            ch_v "[Line]"
            $ Line = 0

    if approval >= 2:

        if JubesX.Forced:
            $ JubesX.change_face("_sad")
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_stat("inhibition", 60, 1)
            ch_v "Ok, fine."
        else:
            $ JubesX.change_face("_sexy", 1)
            $ JubesX.change_stat("love", 90, 1)
            $ JubesX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                    "Well. . . ok.",                 
                    "Sure!", 
                    "I guess I could. . . stick it in.",
                    "Hells yeah.",
                    "Heh, ok, ok."])
            ch_v "[Line]"
            $ Line = 0
        $ JubesX.change_stat("obedience", 20, 1)
        $ JubesX.change_stat("obedience", 60, 1)
        $ JubesX.change_stat("inhibition", 70, 2)
        jump Jubes_DP_Prep
    else:


        $ JubesX.change_face("_angry")
        if "no_dildo" in JubesX.recent_history:
            ch_v "What part of \"no,\" did you not get, [JubesX.player_petname]?"
        elif Taboo and "no_taboo" in JubesX.daily_history and "no_dildo" in JubesX.daily_history:
            ch_v "Stop swinging that thing around in public!"
        elif "no_dildo" in JubesX.daily_history:
            ch_v "I already told you \"no,\" [JubesX.player_petname]."
        elif Taboo and "no_taboo" in JubesX.daily_history:
            ch_v "Stop swinging that thing around in public!"
        elif not JubesX.action_counter["dildo_pussy"]:
            $ JubesX.change_face("_bemused")
            ch_v "I'm just not into toys, [JubesX.player_petname]. . ."
        else:
            $ JubesX.change_face("_bemused")
            ch_v "I don't think we need any toys, [JubesX.player_petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no_dildo" in JubesX.daily_history:
                $ JubesX.change_face("_bemused")
                ch_v "Yeah, ok, [JubesX.player_petname]."
                return
            "Maybe later?" if "no_dildo" not in JubesX.daily_history:
                $ JubesX.change_face("_sexy")
                ch_v "Maybe I'll practice on my own time, [JubesX.player_petname]."
                $ JubesX.change_stat("love", 80, 2)
                $ JubesX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ JubesX.recent_history.append("no_taboo")
                    $ JubesX.daily_history.append("no_taboo")
                $ JubesX.recent_history.append("no_dildo")
                $ JubesX.daily_history.append("no_dildo")
                return
            "I think you'd like it. . .":
                if approval:
                    $ JubesX.change_face("_sexy")
                    $ JubesX.change_stat("obedience", 90, 2)
                    $ JubesX.change_stat("obedience", 50, 2)
                    $ JubesX.change_stat("inhibition", 70, 3)
                    $ JubesX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                            "I suppose. . .", 
                            "You've got me there."])
                    ch_v "[Line]"
                    $ Line = 0
                    jump Jubes_DP_Prep
                else:
                    pass
            "[[press it against her]":

                $ approval = approval_check(JubesX, 950, "OI", TabM = 3)
                if approval > 1 or (approval and JubesX.Forced):
                    $ JubesX.change_face("_sad")
                    $ JubesX.change_stat("love", 70, -5, 1)
                    $ JubesX.change_stat("love", 200, -5)
                    ch_v "Ok, fine. If we're going to do this, stick it in already."
                    $ JubesX.change_stat("obedience", 80, 4)
                    $ JubesX.change_stat("inhibition", 80, 1)
                    $ JubesX.change_stat("inhibition", 60, 3)
                    $ JubesX.Forced = 1
                    jump Jubes_DP_Prep
                else:
                    $ JubesX.change_stat("love", 200, -20)
                    $ JubesX.recent_history.append("_angry")
                    $ JubesX.daily_history.append("_angry")


    $ JubesX.ArmPose = 1
    if "no_dildo" in JubesX.daily_history:
        ch_v "Learn to take \"no\" for an answer, [JubesX.player_petname]."
        $ JubesX.recent_history.append("_angry")
        $ JubesX.daily_history.append("_angry")
    elif JubesX.Forced:
        $ JubesX.change_face("_angry", 1)
        ch_v "I'm not going to let you use that on me."
        $ JubesX.change_stat("lust", 200, 5)
        if JubesX.love > 300:
            $ JubesX.change_stat("love", 70, -2)
        $ JubesX.change_stat("obedience", 50, -2)
        $ JubesX.recent_history.append("_angry")
        $ JubesX.daily_history.append("_angry")
    elif Taboo:
        $ JubesX.change_face("_angry", 1)
        $ JubesX.recent_history.append("no_taboo")
        $ JubesX.daily_history.append("no_taboo")
        ch_v "Not here!"
        $ JubesX.change_stat("lust", 200, 5)
        $ JubesX.change_stat("obedience", 50, -3)
    elif JubesX.action_counter["dildo_pussy"]:
        $ JubesX.change_face("_sad")
        ch_v "Sorry, you can keep your toys to yourself."
    else:
        $ JubesX.change_face("_normal", 1)
        ch_v "No way."
    $ JubesX.recent_history.append("no_dildo")
    $ JubesX.daily_history.append("no_dildo")
    $ approval_bonus = 0
    return

label Jubes_DP_Prep:
    if offhand_action == "dildo_pussy":
        return

    if not JubesX.Forced and action_context != "auto":
        $ approval_bonus = 15 if JubesX.PantsNum() >= 6 else 0
        call Bottoms_Off (JubesX)
        if "_angry" in JubesX.recent_history:
            return

    $ approval_bonus = 0
    call Jubes_Pussy_Launch ("dildo_pussy")
    if not JubesX.action_counter["dildo_pussy"]:
        if JubesX.Forced:
            $ JubesX.change_stat("love", 90, -75)
            $ JubesX.change_stat("obedience", 70, 60)
            $ JubesX.change_stat("inhibition", 80, 35)
        else:
            $ JubesX.change_stat("love", 90, 10)
            $ JubesX.change_stat("obedience", 70, 20)
            $ JubesX.change_stat("inhibition", 80, 45)
    if Taboo:
        $ JubesX.inhibition += int(Taboo/10)
        $ JubesX.lust += int(Taboo/5)


    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ JubesX.drain_word("no_taboo")
    $ JubesX.drain_word("no_dildo")
    $ JubesX.recent_history.append("dildo_pussy")
    $ JubesX.daily_history.append("dildo_pussy")

label Jubes_DP_Cycle:
    while Round > 0:
        call shift_focus (JubesX)
        call Jubes_Pussy_Launch ("dildo_pussy")
        $ JubesX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (JubesX)
                    jump Jubes_DP_Cycle

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
                            if JubesX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ JubesX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (JubesX, "tired")
                        "Shift primary action":

                            if JubesX.remaining_actions and multi_action:
                                menu:
                                    "I want to stick a finger in her ass.":
                                        $ action_context = "shift"
                                        call Jubes_DP_After
                                        call Jubes_Insert_Ass
                                    "Just stick a finger in her ass without asking.":
                                        $ action_context = "auto"
                                        call Jubes_DP_After
                                        call Jubes_Insert_Ass
                                    "I want to shift the dildo to her ass.":
                                        $ action_context = "shift"
                                        call Jubes_DP_After
                                        call Jubes_Dildo_Ass
                                    "Never Mind":
                                        jump Jubes_DP_Cycle
                            else:
                                call Sex_Basic_Dialog (JubesX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Jubes_DP_After
                            call Offhand_Set
                        "Shift your focus (locked)" if not offhand_action:
                            pass
                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [JubesX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (JubesX)
                                "Ask [JubesX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (JubesX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (JubesX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Jubes_DP_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jubes_DP_Cycle
                                "Never mind":
                                    jump Jubes_DP_Cycle
                        "undress [JubesX.name]":
                            call Girl_Undress (JubesX)
                        "Clean up [JubesX.name] (locked)" if not JubesX.spunk:
                            pass
                        "Clean up [JubesX.name]" if JubesX.spunk:
                            call Girl_Cleanup (JubesX, "ask")
                        "Never mind":
                            jump Jubes_DP_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jubes_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jubes_DP_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jubes_Pos_Reset
                    $ Line = 0
                    jump Jubes_DP_After


        if JubesX.underwear or JubesX.PantsNum() >= 6 or JubesX.HoseNum() >= 5:
            call Girl_Undress (JubesX, "auto")

        call shift_focus (JubesX)
        call Sex_Dialog (JubesX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or JubesX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (JubesX)
                if "_angry" in JubesX.recent_history:
                    call Jubes_Pos_Reset
                    return
                $ JubesX.change_stat("lust", 200, 5)
                if 100 > JubesX.lust >= 70 and JubesX.session_orgasms < 2:
                    $ JubesX.recent_history.append("unsatisfied")
                    $ JubesX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jubes_DP_After
                $ Line = "came"

            if JubesX.lust >= 100:

                call Girl_Cumming (JubesX)
                if action_context == "shift" or "_angry" in JubesX.recent_history:
                    jump Jubes_DP_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in JubesX.recent_history:
                    "[JubesX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Jubes_DP_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if JubesX.SEXP >= 100 or approval_check(JubesX, 1200, "LO"):
            pass
        elif counter == (5 + JubesX.action_counter["dildo_pussy"]):
            $ JubesX.brows = "_confused"
            ch_v "What are you even doing down there?"
        elif JubesX.lust >= 80:
            pass
        elif counter == (15 + JubesX.action_counter["dildo_pussy"]) and JubesX.SEXP >= 15 and not approval_check(JubesX, 1500):
            $ JubesX.brows = "_confused"
            menu:
                ch_v "[JubesX.player_petname], this is getting uncomfortable, maybe we could try something else."
                "Finish up.":
                    "You let go. . ."
                    jump Jubes_DP_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Jubes_DP_After
                "No, this is fun.":
                    if approval_check(JubesX, 1200) or approval_check(JubesX, 500, "O"):
                        $ JubesX.change_stat("love", 200, -5)
                        $ JubesX.change_stat("obedience", 50, 3)
                        $ JubesX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ JubesX.change_face("_angry", 1)
                        call Jubes_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_v "Well if that's your attitude, I don't need your \"help\"."
                        $ JubesX.change_stat("love", 50, -3, 1)
                        $ JubesX.change_stat("love", 80, -4, 1)
                        $ JubesX.change_stat("obedience", 30, -1, 1)
                        $ JubesX.change_stat("obedience", 50, -1, 1)
                        $ JubesX.recent_history.append("_angry")
                        $ JubesX.daily_history.append("_angry")
                        jump Jubes_DP_After


        if Round == 10:
            call Sex_Basic_Dialog (JubesX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JubesX, 5)


    $ JubesX.change_face("_bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JubesX, "done")


label Jubes_DP_After:
    if not action_context:
        call Jubes_Pos_Reset

    $ JubesX.change_face("_sexy")

    $ JubesX.action_counter["dildo_pussy"] += 1
    $ JubesX.remaining_actions -=1

    call Partner_Like (JubesX, 1)

    if JubesX.action_counter["dildo_pussy"] == 1:
        $ JubesX.SEXP += 10
        if not action_context:
            if JubesX.love >= 500 and "unsatisfied" not in JubesX.recent_history:
                ch_v "Thanks for the extra hand. . ."
            elif JubesX.obedience <= 500 and Player.focus <= 20:
                $ JubesX.change_face("_perplexed", 1)
                ch_v "Did you like that?"

    $ approval_bonus = 0


    call checkout
    return






label Jubes_Dildo_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JubesX)
    call Jubes_Dildo_Check
    if not _return:
        return

    if JubesX.used_to_anal:
        $ approval_bonus += 30
    elif "anal" in JubesX.recent_history or "dildo_anal" in JubesX.recent_history:
        $ approval_bonus -= 20
    elif "anal" in JubesX.daily_history or "dildo_anal" in JubesX.daily_history:
        $ approval_bonus -= 10
    elif (JubesX.action_counter["anal"] + JubesX.action_counter["dildo_ass"] + JubesX.Plug) > 0:
        $ approval_bonus += 20

    if JubesX.legs == "pants:":
        $ approval_bonus -= 20

    if JubesX.lust > 95:
        $ approval_bonus += 20
    elif JubesX.lust > 85:
        $ approval_bonus += 15

    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in JubesX.traits:
        $ approval_bonus += (5*Taboo)
    if JubesX in Player.Harem or "sex friend" in JubesX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JubesX.traits:
        $ approval_bonus -= 40
    if JubesX.event_counter["forced"] and not JubesX.Forced:
        $ approval_bonus -= 5*JubesX.event_counter["forced"]

    if Taboo and "no_taboo" in JubesX.daily_history:
        $ approval_bonus -= 10

    if "no_dildo" in JubesX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_dildo" in JubesX.recent_history else 0

    $ approval = approval_check(JubesX, 1450, TabM = 4)

    if action_context == JubesX:

        if approval > 2:
            if JubesX.PantsNum() == 5:
                "[JubesX.name] grabs her dildo, hiking up her skirt as she does."
                $ JubesX.upskirt = 1
            elif JubesX.PantsNum() >= 6:
                "[JubesX.name] grabs her dildo, pulling down her pants as she does."
                $ JubesX.legs = ""
            else:
                "[JubesX.name] grabs her dildo, rubbing is suggestively against her ass."
            $ JubesX.SeenPanties = 1
            call Jubes_First_Bottomless (1)
            "She slides the tip against her asshole, and seems to want you to insert it."
            menu:
                "What do you do?"
                "Nothing.":
                    $ JubesX.change_stat("inhibition", 80, 3)
                    $ JubesX.change_stat("inhibition", 50, 2)
                    "[JubesX.name] slides it in."
                "Go for it.":
                    $ JubesX.change_face("_sexy", 1)
                    $ JubesX.change_stat("inhibition", 80, 3)
                    ch_p "Oh yeah, [JubesX.petname], let's do this."
                    $ JubesX.nameCheck()
                    "You grab the dildo and slide it in."
                    $ JubesX.change_stat("love", 85, 1)
                    $ JubesX.change_stat("obedience", 90, 1)
                    $ JubesX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ JubesX.change_face("_surprised")
                    $ JubesX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that right now, [JubesX.petname]."
                    $ JubesX.nameCheck()
                    "[JubesX.name] sets the dildo down."
                    $ JubesX.change_outfit()
                    $ JubesX.change_stat("obedience", 90, 1)
                    $ JubesX.change_stat("obedience", 50, 1)
                    $ JubesX.change_stat("obedience", 30, 2)
                    return
            jump Jubes_DA_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
        return

    if action_context == "auto":
        "You rub the dildo across her body, and against her tight anus."
        $ JubesX.change_face("_surprised", 1)

        if (JubesX.action_counter["dildo_ass"] and approval) or (approval > 1):

            "[JubesX.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            $ JubesX.change_face("_sexy")
            $ JubesX.change_stat("obedience", 70, 3)
            $ JubesX.change_stat("inhibition", 50, 3)
            $ JubesX.change_stat("inhibition", 70, 1)
            ch_v "Ooo, [JubesX.player_petname], toys!"
            jump Jubes_DA_Prep
        else:

            $ JubesX.brows = "_angry"
            menu:
                ch_v "Hey, what are you planning to do with that?!"
                "Sorry, sorry! Never mind.":
                    if approval:
                        $ JubesX.change_face("_sexy", 1)
                        $ JubesX.change_stat("obedience", 70, 3)
                        $ JubesX.change_stat("inhibition", 50, 3)
                        $ JubesX.change_stat("inhibition", 70, 1)
                        ch_v "Well, now that you mention it. . ."
                        jump Jubes_DA_Prep
                    "You pull back before you really get it in."
                    $ JubesX.change_face("_bemused", 1)
                    if JubesX.action_counter["dildo_ass"]:
                        ch_v "Well ok, [JubesX.player_petname], maybe warn me next time?"
                    else:
                        ch_v "Well ok, [JubesX.player_petname], that's a little much. . . for now . . ."
                "Just playing with my favorite toys.":
                    $ JubesX.change_stat("love", 80, -10, 1)
                    $ JubesX.change_stat("love", 200, -10)
                    "You press it inside some more."
                    $ JubesX.change_stat("obedience", 70, 3)
                    $ JubesX.change_stat("inhibition", 50, 3)
                    if not approval_check(JubesX, 700, "O", TabM=1):
                        $ JubesX.change_face("_angry")
                        "[JubesX.name] shoves you away and slaps you in the face."
                        ch_v "Jerk!"
                        ch_v "Ask nice if you want to stick something in my ass!"
                        $ JubesX.change_stat("love", 50, -10, 1)
                        $ JubesX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        if renpy.showing("Jubes_SexSprite"):
                            call Jubes_Sex_Reset
                        $ JubesX.recent_history.append("_angry")
                        $ JubesX.daily_history.append("_angry")
                    else:
                        $ JubesX.change_face("_sad")
                        "[JubesX.name] doesn't seem to be into this, you're lucky she's so obedient."
                        jump Jubes_DA_Prep
        return


    if not JubesX.action_counter["dildo_ass"]:

        $ JubesX.change_face("_surprised", 1)
        $ JubesX.mouth = "_kiss"
        ch_v "You want to try and fit that. . .?"
        if JubesX.Forced:
            $ JubesX.change_face("_sad")
            ch_v "Always about the butt, huh?"

    if not JubesX.used_to_anal and ("dildo_anal" in JubesX.recent_history or "anal" in JubesX.recent_history or "dildo_anal" in JubesX.daily_history or "anal" in JubesX.daily_history):
        $ JubesX.change_face("_bemused", 1)
        ch_v "I'm still sore from earlier. . ."

    if not JubesX.action_counter["dildo_ass"] and approval:

        if JubesX.Forced:
            $ JubesX.change_face("_sad")
            $ JubesX.change_stat("love", 70, -3, 1)
            $ JubesX.change_stat("love", 20, -2, 1)
        elif JubesX.love >= (JubesX.obedience + JubesX.inhibition):
            $ JubesX.change_face("_sexy")
            $ JubesX.brows = "_sad"
            $ JubesX.mouth = "_smile"
            ch_v "I haven't actually used one of these, back there before. . ."
        elif JubesX.obedience >= JubesX.inhibition:
            $ JubesX.change_face("_normal")
            ch_v "If that's what you want, [JubesX.player_petname]. . ."
        else:
            $ JubesX.change_face("_sad")
            $ JubesX.mouth = "_smile"
            ch_v "I guess it could be fun two-player. . ."

    elif approval:

        if JubesX.Forced:
            $ JubesX.change_face("_sad")
            $ JubesX.change_stat("love", 70, -3, 1)
            $ JubesX.change_stat("love", 20, -2, 1)
            ch_v "The toys again?"
        elif not Taboo and "no_taboo" in JubesX.daily_history:
            ch_v "Well, at least you got us some privacy this time. . ."
        elif "dildo_anal" in JubesX.daily_history and not JubesX.used_to_anal:
            pass
        elif "dildo_anal" in JubesX.daily_history:
            $ JubesX.change_face("_sexy", 1)
            $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "I'm still a bit sore from earlier.",
                    "You're going to wear me out."])
            ch_v "[Line]"
        elif JubesX.action_counter["dildo_ass"] < 3:
            $ JubesX.change_face("_sexy", 1)
            $ JubesX.brows = "_confused"
            $ JubesX.mouth = "_kiss"
            ch_v "You want to stick it in my ass again?"
        else:
            $ JubesX.change_face("_sexy", 1)
            $ JubesX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my ass again?",
                    "You want me ta lube up your toy?"])
            ch_v "[Line]"
            $ Line = 0

    if approval >= 2:

        if JubesX.Forced:
            $ JubesX.change_face("_sad")
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_stat("inhibition", 60, 1)
            ch_v "Ok, fine."
        else:
            $ JubesX.change_face("_sexy", 1)
            $ JubesX.change_stat("love", 90, 1)
            $ JubesX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                    "Well. . . ok.",                 
                    "Sure!", 
                    "I guess I could. . . stick it in.",
                    "Hells yeah.",
                    "Heh, ok, ok."])
            ch_v "[Line]"
            $ Line = 0
        $ JubesX.change_stat("obedience", 20, 1)
        $ JubesX.change_stat("obedience", 60, 1)
        $ JubesX.change_stat("inhibition", 70, 2)
        jump Jubes_DA_Prep
    else:


        $ JubesX.change_face("_angry")
        if "no_dildo" in JubesX.recent_history:
            ch_v "What part of \"no,\" did you not get, [JubesX.player_petname]?"
        elif Taboo and "no_taboo" in JubesX.daily_history and "no_dildo" in JubesX.daily_history:
            ch_v "Stop swinging that thing around in public!"
        elif "no_dildo" in JubesX.daily_history:
            ch_v "I already told you \"no,\" [JubesX.player_petname]."
        elif Taboo and "no_taboo" in JubesX.daily_history:
            ch_v "I already told you that I wouldn't do that out here!"
        elif not JubesX.action_counter["dildo_ass"]:
            $ JubesX.change_face("_bemused")
            ch_v "I'm just not into toys, [JubesX.player_petname]. . ."
        elif not JubesX.used_to_anal and "dildo_anal" not in JubesX.daily_history:
            $ JubesX.change_face("_perplexed")
            ch_v "You could have been a bit more gentle last time, [JubesX.player_petname]. . ."
        else:
            $ JubesX.change_face("_bemused")
            ch_v "I don't think we need any toys, [JubesX.player_petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no_dildo" in JubesX.daily_history:
                $ JubesX.change_face("_bemused")
                ch_v "Yeah, ok, [JubesX.player_petname]."
                return
            "Maybe later?" if "no_dildo" not in JubesX.daily_history:
                $ JubesX.change_face("_sexy")
                ch_v "Maybe I'll practice on my own time, [JubesX.player_petname]."
                $ JubesX.change_stat("love", 80, 2)
                $ JubesX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ JubesX.recent_history.append("no_taboo")
                    $ JubesX.daily_history.append("no_taboo")
                $ JubesX.recent_history.append("no_dildo")
                $ JubesX.daily_history.append("no_dildo")
                return
            "I think you'd like it. . .":
                if approval:
                    $ JubesX.change_face("_sexy")
                    $ JubesX.change_stat("obedience", 90, 2)
                    $ JubesX.change_stat("obedience", 50, 2)
                    $ JubesX.change_stat("inhibition", 70, 3)
                    $ JubesX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                            "I suppose. . .", 
                            "You've got me there."])
                    ch_v "[Line]"
                    $ Line = 0
                    jump Jubes_DA_Prep
                else:
                    pass
            "[[press it against her]":

                $ approval = approval_check(JubesX, 1050, "OI", TabM = 3)
                if approval > 1 or (approval and JubesX.Forced):
                    $ JubesX.change_face("_sad")
                    $ JubesX.change_stat("love", 70, -5, 1)
                    $ JubesX.change_stat("love", 200, -5)
                    ch_v "Ok, fine. If we're going to do this, stick it in already."
                    $ JubesX.change_stat("obedience", 80, 4)
                    $ JubesX.change_stat("inhibition", 80, 1)
                    $ JubesX.change_stat("inhibition", 60, 3)
                    $ JubesX.Forced = 1
                    jump Jubes_DA_Prep
                else:
                    $ JubesX.change_stat("love", 200, -20)
                    $ JubesX.recent_history.append("_angry")
                    $ JubesX.daily_history.append("_angry")


    $ JubesX.ArmPose = 1
    if "no_dildo" in JubesX.daily_history:
        ch_v "Learn to take \"no\" for an answer, [JubesX.player_petname]."
        $ JubesX.recent_history.append("_angry")
        $ JubesX.daily_history.append("_angry")
    elif JubesX.Forced:
        $ JubesX.change_face("_angry", 1)
        ch_v "I'm not going to let you use that on me."
        $ JubesX.change_stat("lust", 200, 5)
        if JubesX.love > 300:
            $ JubesX.change_stat("love", 70, -2)
        $ JubesX.change_stat("obedience", 50, -2)
        $ JubesX.recent_history.append("_angry")
        $ JubesX.daily_history.append("_angry")
    elif Taboo:
        $ JubesX.change_face("_angry", 1)
        $ JubesX.recent_history.append("no_taboo")
        $ JubesX.daily_history.append("no_taboo")
        ch_v "Not here!"
        $ JubesX.change_stat("lust", 200, 5)
        $ JubesX.change_stat("obedience", 50, -3)
    elif not JubesX.used_to_anal and "dildo_anal" in JubesX.daily_history:
        $ JubesX.change_face("_bemused")
        ch_v "Sorry, I just need a little break back there, [JubesX.player_petname]."
    elif JubesX.action_counter["dildo_ass"]:
        $ JubesX.change_face("_sad")
        ch_v "Sorry, you can keep your toys out of there."
    else:
        $ JubesX.change_face("_normal", 1)
        ch_v "No way."
    $ JubesX.recent_history.append("no_dildo")
    $ JubesX.daily_history.append("no_dildo")
    $ approval_bonus = 0
    return

label Jubes_DA_Prep:
    if offhand_action == "dildo_anal":
        return

    if not JubesX.Forced and action_context != "auto":
        $ approval_bonus = 20 if JubesX.PantsNum() >= 6 else 0
        call Bottoms_Off (JubesX)
        if "_angry" in JubesX.recent_history:
            return

    $ approval_bonus = 0
    call Jubes_Pussy_Launch ("dildo_anal")
    if not JubesX.action_counter["dildo_ass"]:
        if JubesX.Forced:
            $ JubesX.change_stat("love", 90, -75)
            $ JubesX.change_stat("obedience", 70, 60)
            $ JubesX.change_stat("inhibition", 80, 35)
        else:
            $ JubesX.change_stat("love", 90, 10)
            $ JubesX.change_stat("obedience", 70, 20)
            $ JubesX.change_stat("inhibition", 80, 45)
    if Taboo:
        $ JubesX.inhibition += int(Taboo/10)
        $ JubesX.lust += int(Taboo/5)


    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ JubesX.drain_word("no_taboo")
    $ JubesX.drain_word("no_dildo")
    $ JubesX.recent_history.append("dildo_anal")
    $ JubesX.daily_history.append("dildo_anal")

label Jubes_DA_Cycle:
    while Round > 0:
        call shift_focus (JubesX)
        call Jubes_Pussy_Launch ("dildo_anal")
        $ JubesX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (JubesX)
                    jump Jubes_DA_Cycle

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
                            if JubesX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ JubesX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (JubesX, "tired")
                        "Shift primary action":

                            if JubesX.remaining_actions and multi_action:
                                menu:
                                    "I want to stick a finger in her pussy.":
                                        $ action_context = "shift"
                                        call Jubes_DA_After
                                        call Jubes_Fondle_Pussy
                                    "Just stick a finger in her pussy without asking.":
                                        $ action_context = "auto"
                                        call Jubes_DA_After
                                        call Jubes_Fondle_Pussy
                                    "I want to shift the dildo to her pussy.":
                                        $ action_context = "shift"
                                        call Jubes_DA_After
                                        call Jubes_Dildo_Pussy
                                    "Never Mind":
                                        jump Jubes_DA_Cycle
                            else:
                                call Sex_Basic_Dialog (JubesX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Jubes_DA_After
                            call Offhand_Set
                        "Shift your focus (locked)" if not offhand_action:
                            pass
                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [JubesX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (JubesX)
                                "Ask [JubesX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (JubesX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (JubesX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Jubes_DA_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jubes_DA_Cycle
                        "Never mind":
                            jump Jubes_DA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jubes_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jubes_DA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jubes_Pos_Reset
                    $ Line = 0
                    jump Jubes_DA_After


        if JubesX.underwear or JubesX.PantsNum() >= 6 or JubesX.HoseNum() >= 5:
            call Girl_Undress (JubesX, "auto")

        call shift_focus (JubesX)
        call Sex_Dialog (JubesX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or JubesX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (JubesX)
                if "_angry" in JubesX.recent_history:
                    call Jubes_Pos_Reset
                    return
                $ JubesX.change_stat("lust", 200, 5)
                if 100 > JubesX.lust >= 70 and JubesX.session_orgasms < 2:
                    $ JubesX.recent_history.append("unsatisfied")
                    $ JubesX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jubes_DA_After
                $ Line = "came"

            if JubesX.lust >= 100:

                call Girl_Cumming (JubesX)
                if action_context == "shift" or "_angry" in JubesX.recent_history:
                    jump Jubes_DA_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in JubesX.recent_history:
                    "[JubesX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Jubes_DA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if JubesX.SEXP >= 100 or approval_check(JubesX, 1200, "LO"):
            pass
        elif counter == (5 + JubesX.action_counter["dildo_ass"]):
            $ JubesX.brows = "_confused"
            ch_v "What are you even doing down there?"
        elif JubesX.lust >= 80:
            pass
        elif counter == (15 + JubesX.action_counter["dildo_ass"]) and JubesX.SEXP >= 15 and not approval_check(JubesX, 1500):
            $ JubesX.brows = "_confused"
            menu:
                ch_v "[JubesX.player_petname], this is getting uncomfortable, maybe we could try something else."
                "Finish up.":
                    "You let go. . ."
                    jump Jubes_DA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Jubes_DA_After
                "No, this is fun.":
                    if approval_check(JubesX, 1200) or approval_check(JubesX, 500, "O"):
                        $ JubesX.change_stat("love", 200, -5)
                        $ JubesX.change_stat("obedience", 50, 3)
                        $ JubesX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ JubesX.change_face("_angry", 1)
                        call Jubes_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_v "Well if that's your attitude, I don't need your \"help\"."
                        $ JubesX.change_stat("love", 50, -3, 1)
                        $ JubesX.change_stat("love", 80, -4, 1)
                        $ JubesX.change_stat("obedience", 30, -1, 1)
                        $ JubesX.change_stat("obedience", 50, -1, 1)
                        $ JubesX.recent_history.append("_angry")
                        $ JubesX.daily_history.append("_angry")
                        jump Jubes_DA_After


        if Round == 10:
            call Sex_Basic_Dialog (JubesX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JubesX, 5)


    $ JubesX.change_face("_bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JubesX, "done")

label Jubes_DA_After:
    if not action_context:
        call Jubes_Pos_Reset

    $ JubesX.change_face("_sexy")

    $ JubesX.action_counter["dildo_ass"] += 1
    $ JubesX.remaining_actions -=1

    call Partner_Like (JubesX, 1)

    if JubesX.action_counter["dildo_ass"] == 1:
        $ JubesX.SEXP += 10
        if not action_context:
            if JubesX.love >= 500 and "unsatisfied" not in JubesX.recent_history:
                if JubesX.used_to_anal:
                    ch_v "That was. . . interesting. . ."
                else:
                    ch_v "Ouch. . ."
            elif JubesX.obedience <= 500 and Player.focus <= 20:
                $ JubesX.change_face("_perplexed", 1)
                ch_v "Did you like that?"

    $ approval_bonus = 0


    call checkout
    return



label Jubes_Vibrator_Check:
    if "_vibrator" in Player.inventory:
        "You pull out the \"shocker\" vibrator, handy."
    elif "_vibrator" in JubesX.inventory:
        "You ask [JubesX.name] to get out her vibrator."
    else:
        "You don't have one of those on you."
        return 0
    return 1


label Jubes_Footjob:

    "This option is currently unavailable. It will be added in a later update."
    return


    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JubesX)
    if JubesX.action_counter["footjob"] >= 7:
        $ approval_bonus += 10
    elif JubesX.action_counter["footjob"] >= 3:
        $ approval_bonus += 7
    elif JubesX.action_counter["footjob"]:
        $ approval_bonus += 3

    if JubesX.addiction >= 75 and JubesX.event_counter["swallowed"] >=3:
        $ approval_bonus += 10
    if JubesX.addiction >= 75:
        $ approval_bonus += 5

    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in JubesX.traits:
        $ approval_bonus += (3*Taboo)
    if JubesX in Player.Harem or "sex friend" in JubesX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JubesX.traits:
        $ approval_bonus -= 40
    if JubesX.event_counter["forced"] and not JubesX.Forced:
        $ approval_bonus -= 5*JubesX.event_counter["forced"]

    if Taboo and "no_taboo" in JubesX.daily_history:
        $ approval_bonus -= 10

    if "no_foot" in JubesX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_foot" in JubesX.recent_history else 0

    $ approval = approval_check(JubesX, 1250, TabM = 3)

    if action_context == JubesX:
        if approval > 2:
            "[JubesX.name] leans back and starts rubbing your cock with her foot."
            menu:
                "What do you do?"
                "Nothing.":
                    $ JubesX.change_stat("inhibition", 70, 3)
                    $ JubesX.change_stat("inhibition", 30, 2)
                    "[JubesX.name] continues her actions."
                "Praise her.":
                    $ JubesX.change_face("_sexy", 1)
                    $ JubesX.change_stat("inhibition", 70, 3)
                    ch_p "Oooh, that's good, [JubesX.petname]."
                    $ JubesX.nameCheck()
                    "[JubesX.name] continues her actions."
                    $ JubesX.change_stat("love", 80, 1)
                    $ JubesX.change_stat("obedience", 90, 1)
                    $ JubesX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ JubesX.change_face("_surprised")
                    $ JubesX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that for now, [JubesX.petname]."
                    $ JubesX.nameCheck()
                    "[JubesX.name] puts it down."
                    $ JubesX.change_stat("obedience", 90, 1)
                    $ JubesX.change_stat("obedience", 50, 1)
                    $ JubesX.change_stat("obedience", 30, 2)
                    return
            if primary_action:
                $ girl_offhand_action = "footjob"
                return
            jump Jubes_FJ_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if not JubesX.action_counter["footjob"] and "no_foot" not in JubesX.recent_history:
        $ JubesX.change_face("_confused", 2)
        ch_v "Standard footjob?"
        $ JubesX.blushing = "_blush1"

    if not JubesX.action_counter["footjob"] and approval:
        if JubesX.Forced:
            $ JubesX.change_face("_sad",1)
            $ JubesX.change_stat("love", 70, -3, 1)
            $ JubesX.change_stat("love", 20, -2, 1)
        elif JubesX.love >= (JubesX.obedience + JubesX.inhibition):
            $ JubesX.change_face("_sexy",1)
            $ JubesX.brows = "_sad"
            $ JubesX.mouth = "_smile"
            ch_v "I guess it couldn't hurt. . ."
        elif JubesX.obedience >= JubesX.inhibition:
            $ JubesX.change_face("_normal",1)
            ch_v "If you want, [JubesX.player_petname]. . ."
        elif JubesX.addiction >= 50:
            $ JubesX.change_face("_manic", 1)
            ch_v "Okay. . ."
        else:
            $ JubesX.change_face("_lipbite",1)
            ch_v "Sure. . ."

    elif approval:
        if JubesX.Forced:
            $ JubesX.change_face("_sad")
            $ JubesX.change_stat("love", 70, -3, 1)
            $ JubesX.change_stat("love", 20, -2, 1)
            ch_v "That's it?"
        elif not Taboo and "no_taboo" in JubesX.daily_history:
            ch_v "Um, I guess this is secure enough. . ."
        elif "footjob" in JubesX.daily_history:
            $ JubesX.change_face("_sexy", 1)
            ch_v "More of that, huh. . ."
            jump Jubes_FJ_Prep







        elif JubesX.action_counter["footjob"] < 3:
            $ JubesX.change_face("_sexy", 1)
            $ JubesX.brows = "_confused"
            $ JubesX.mouth = "_kiss"
            ch_v "Hmm, magic toes. . ."
        else:
            $ JubesX.change_face("_sexy", 1)
            $ JubesX.ArmPose = 2
            $ Line = renpy.random.choice(["You want me to use my feet?",                 
                "So you'd like another footjob?",                 
                "A little. . . [she rubs her foot along your leg]?", 
                "A little TLC?"])
            ch_v "[Line]"
        $ Line = 0

    if approval >= 2:
        if JubesX.Forced:
            $ JubesX.change_face("_sad")
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_stat("inhibition", 60, 1)
            ch_v "Ok, sure."
        elif "no_foot" in JubesX.daily_history:
            ch_v "Fine."
        else:
            $ JubesX.change_face("_sexy", 1)
            $ JubesX.change_stat("love", 90, 1)
            $ JubesX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Sure, I guess.",                 
                "OK.",                 
                "Fine, lemme see it.", 
                "I guess I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Heh, ok, ok."])
            ch_v "[Line]"
            $ Line = 0
        $ JubesX.change_stat("obedience", 20, 1)
        $ JubesX.change_stat("obedience", 60, 1)
        $ JubesX.change_stat("inhibition", 70, 2)
        jump Jubes_FJ_Prep
    else:

        $ JubesX.change_face("_angry")
        if "no_foot" in JubesX.recent_history:
            ch_v "You should listen better, [JubesX.player_petname]."
        elif Taboo and "no_taboo" in JubesX.daily_history and "no_foot" in JubesX.daily_history:
            ch_v "I said not in public."
        elif "no_foot" in JubesX.daily_history:
            ch_v "I told you \"no,\" [JubesX.player_petname]."
        elif Taboo and "no_taboo" in JubesX.daily_history:
            ch_v "I said not in public!"
        elif not JubesX.action_counter["footjob"]:
            $ JubesX.change_face("_bemused")
            ch_v "Eh, [JubesX.player_petname]. . ."
        else:
            $ JubesX.change_face("_bemused")
            ch_v "Not now, ok?"
        menu:
            extend ""
            "Sorry, never mind." if "no_foot" in JubesX.daily_history:
                $ JubesX.change_face("_bemused")
                ch_v "Sure, no problem."
                return
            "Maybe later?" if "no_foot" not in JubesX.daily_history:
                $ JubesX.change_face("_sexy")
                ch_v ". . ."
                ch_v "Maybe."
                $ JubesX.change_stat("love", 80, 2)
                $ JubesX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ JubesX.recent_history.append("no_taboo")
                    $ JubesX.daily_history.append("no_taboo")
                $ JubesX.recent_history.append("no_foot")
                $ JubesX.daily_history.append("no_foot")
                return
            "I'd really appreciate it. . .":
                if approval:
                    $ JubesX.change_face("_sexy")
                    $ JubesX.change_stat("obedience", 90, 2)
                    $ JubesX.change_stat("obedience", 50, 2)
                    $ JubesX.change_stat("inhibition", 70, 3)
                    $ JubesX.change_stat("inhibition", 40, 2)
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
            "Come on, get to work.":

                $ approval = approval_check(JubesX, 400, "OI", TabM = 3)
                if approval > 1 or (approval and JubesX.Forced):
                    $ JubesX.change_face("_sad")
                    $ JubesX.change_stat("love", 70, -5, 1)
                    $ JubesX.change_stat("love", 200, -2)
                    ch_v "Fine."
                    $ JubesX.change_stat("obedience", 50, 4)
                    $ JubesX.change_stat("inhibition", 80, 1)
                    $ JubesX.change_stat("inhibition", 60, 3)
                    $ JubesX.Forced = 1
                    jump Jubes_FJ_Prep
                else:
                    $ JubesX.change_stat("love", 200, -15)
                    $ JubesX.recent_history.append("_angry")
                    $ JubesX.daily_history.append("_angry")


    $ JubesX.ArmPose = 1
    if "no_foot" in JubesX.daily_history:
        $ JubesX.change_face("_angry", 1)
        ch_v "I'm not telling you again."
        $ JubesX.recent_history.append("_angry")
        $ JubesX.daily_history.append("_angry")
    elif JubesX.Forced:
        $ JubesX.change_face("_angry", 1)
        ch_v "You understand that I have claws down there too. . ."
        $ JubesX.change_stat("lust", 200, 5)
        if JubesX.love > 300:
            $ JubesX.change_stat("love", 70, -2)
        $ JubesX.change_stat("obedience", 50, -2)
        $ JubesX.recent_history.append("_angry")
        $ JubesX.daily_history.append("_angry")
    elif Taboo:
        $ JubesX.change_face("_angry", 1)
        $ JubesX.daily_history.append("no_taboo")
        ch_v "This is too exposed."
        $ JubesX.change_stat("lust", 200, 5)
        $ JubesX.change_stat("obedience", 50, -3)
    elif JubesX.action_counter["footjob"]:
        $ JubesX.change_face("_sad")
        ch_v "Not right now."
    else:
        $ JubesX.change_face("_normal", 1)
        ch_v "I'd rather not."
    $ JubesX.recent_history.append("no_foot")
    $ JubesX.daily_history.append("no_foot")
    $ approval_bonus = 0
    return


label Jubes_FJ_Prep:
    if offhand_action == "footjob":
        return

    if Taboo:
        $ JubesX.inhibition += int(Taboo/10)
        $ JubesX.lust += int(Taboo/5)

    $ JubesX.change_face("_sexy")
    if JubesX.Forced:
        $ JubesX.change_face("_sad")
    elif not JubesX.action_counter["footjob"]:
        $ JubesX.brows = "_confused"
        $ JubesX.eyes = "_sexy"
        $ JubesX.mouth = "_smile"

    call Seen_First_Peen (JubesX, Partner)

    if not JubesX.action_counter["footjob"]:
        if JubesX.Forced:
            $ JubesX.change_stat("love", 90, -20)
            $ JubesX.change_stat("obedience", 70, 25)
            $ JubesX.change_stat("inhibition", 80, 30)
        else:
            $ JubesX.change_stat("love", 90, 5)
            $ JubesX.change_stat("obedience", 70, 20)
            $ JubesX.change_stat("inhibition", 80, 20)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ JubesX.drain_word("no_taboo")
    $ JubesX.drain_word("no_foot")
    $ JubesX.recent_history.append("footjob")
    $ JubesX.daily_history.append("footjob")

label Jubes_FJ_Cycle:
    while Round > 0:
        call shift_focus (JubesX)
        call Jubes_Sex_Launch ("footjob")
        $ JubesX.lust_face()

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

                    $ JubesX.pose = "doggy" if JubesX.pose != "doggy" else "sex"
                    "You turn her around. . ."
                    jump Jubes_FJ_Cycle
                "Other options":

                    menu:
                        "Offhand action":
                            if JubesX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ JubesX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (JubesX, "tired")
                        "Shift primary action":

                            if JubesX.remaining_actions and multi_action:
                                menu:
                                    "How about a blowjob?":
                                        if JubesX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Jubes_FJ_After
                                            call Jubes_Blowjob
                                        else:
                                            call Sex_Basic_Dialog (JubesX, "tired")
                                    "How about a handjob?":
                                        if JubesX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Jubes_FJ_After
                                            call Jubes_Handjob
                                        else:
                                            call Sex_Basic_Dialog (JubesX, "tired")
                                    "How about a titjob?":

                                        if JubesX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Jubes_FJ_After
                                            call Jubes_Titjob
                                        else:
                                            call Sex_Basic_Dialog (JubesX, "tired")
                                    "Never Mind":



                                        jump Jubes_FJ_Cycle
                            else:
                                call Sex_Basic_Dialog (JubesX, "tired")

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [JubesX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (JubesX)
                                "Ask [JubesX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (JubesX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (JubesX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Jubes_FJ_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jubes_FJ_Cycle
                                "Never mind":
                                    jump Jubes_FJ_Cycle
                        "undress [JubesX.name]":
                            call Girl_Undress (JubesX)
                        "Clean up [JubesX.name] (locked)" if not JubesX.spunk:
                            pass
                        "Clean up [JubesX.name]" if JubesX.spunk:
                            call Girl_Cleanup (JubesX, "ask")
                        "Never mind":
                            jump Jubes_FJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jubes_Sex_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jubes_FJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jubes_Sex_Reset
                    $ Line = 0
                    jump Jubes_FJ_After


        call shift_focus (JubesX)
        call Sex_Dialog (JubesX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or JubesX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (JubesX)
                if "_angry" in JubesX.recent_history:
                    call Jubes_Sex_Reset
                    return
                $ JubesX.change_stat("lust", 200, 5)
                if 100 > JubesX.lust >= 70 and JubesX.session_orgasms < 2:
                    $ JubesX.recent_history.append("unsatisfied")
                    $ JubesX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jubes_FJ_After
                $ Line = "came"

            if JubesX.lust >= 100:

                call Girl_Cumming (JubesX)
                if action_context == "shift" or "_angry" in JubesX.recent_history:
                    jump Jubes_FJ_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in JubesX.recent_history:
                    "[JubesX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Jubes_FJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if counter == 20:
            $ JubesX.brows = "_angry"
            menu:
                ch_v "Hmm, this is getting a bit boring."
                "How about a BJ?" if JubesX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Jubes_FJ_After
                    call Jubes_Blowjob
                "How about a Handy?" if JubesX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Jubes_FJ_After
                    call Jubes_Handjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    $ counter += 1
                    "[Line]"
                    jump Jubes_FJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Jubes_Sex_Reset
                    $ action_context = "shift"
                    jump Jubes_FJ_After
                "No, get back down there.":
                    if approval_check(JubesX, 1200) or approval_check(JubesX, 500, "O"):
                        $ JubesX.change_stat("love", 200, -5)
                        $ JubesX.change_stat("obedience", 50, 3)
                        $ JubesX.change_stat("obedience", 80, 2)
                        "She grumbles but gets back to work."
                    else:
                        $ JubesX.change_face("_angry", 1)
                        "She scowls at you and pulls back."
                        ch_v "Not interested."
                        $ JubesX.change_stat("love", 50, -3, 1)
                        $ JubesX.change_stat("love", 80, -4, 1)
                        $ JubesX.change_stat("obedience", 30, -1, 1)
                        $ JubesX.change_stat("obedience", 50, -1, 1)
                        $ JubesX.recent_history.append("_angry")
                        $ JubesX.daily_history.append("_angry")
                        jump Jubes_FJ_After
        elif counter == 10 and JubesX.SEXP <= 100 and not approval_check(JubesX, 1200, "LO"):
            $ JubesX.brows = "_confused"
            ch_v "Ok, seriously, let's try something different."


        call Escalation (JubesX)

        if Round == 10:
            call Sex_Basic_Dialog (JubesX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JubesX, 5)


    $ JubesX.change_face("_bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JubesX, "done")

label Jubes_FJ_After:
    $ JubesX.change_face("_sexy")

    $ JubesX.action_counter["footjob"] += 1
    $ JubesX.remaining_actions -=1
    $ JubesX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ JubesX.addiction_rate += 1
    $ JubesX.change_stat("lust", 90, 5)

    call Partner_Like (JubesX, 1)

    if "Jubespedi" in Achievements:
        pass
    elif JubesX.action_counter["footjob"] >= 10:
        $ JubesX.change_face("_smile", 1)
        ch_v "I think I'm finally back into practice on this."
        $ Achievements.append("Jubespedi")
        $ JubesX.SEXP += 5
    elif JubesX.action_counter["footjob"] == 1:
        $ JubesX.SEXP += 10
        if JubesX.love >= 500:
            $ JubesX.mouth = "_smile"
            ch_v "Did you like that? . ."
        elif Player.focus <= 20:
            $ JubesX.mouth = "_sad"
            ch_v "Did that do it for you?"
    elif JubesX.action_counter["footjob"] == 5:
        ch_v "I'm getting used to this. . ."

    $ approval_bonus = 0
    if action_context == "shift":
        ch_v "Ok, so what did you have in mind?"
    else:
        call Jubes_Sex_Reset
    call checkout
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
