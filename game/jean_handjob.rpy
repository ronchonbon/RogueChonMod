
label Jean_Handjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JeanX)
    if JeanX.action_counter["handjob"] >= 7:
        $ approval_bonus += 10
    elif JeanX.action_counter["handjob"] >= 3:
        $ approval_bonus += 7
    elif JeanX.action_counter["handjob"]:
        $ approval_bonus += 3

    if JeanX.addiction >= 75 and JeanX.event_counter["swallowed"] >=3:
        $ approval_bonus += 15
    if JeanX.addiction >= 75:
        $ approval_bonus += 5

    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in JeanX.traits:
        $ approval_bonus += (3*Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JeanX.traits:
        $ approval_bonus -= 40
    if JeanX.event_counter["forced"] and not JeanX.Forced:
        $ approval_bonus -= 5*JeanX.event_counter["forced"]

    if JeanX.Taboo and "no_taboo" in JeanX.daily_history:
        $ approval_bonus -= 10

    if "no_handjob" in JeanX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_handjob" in JeanX.recent_history else 0

    $ approval = approval_check(JeanX, 1100, TabM = 3)

    if not JeanX.action_counter["handjob"] and "no_handjob" not in JeanX.recent_history:
        $ JeanX.change_face("_confused", 2)
        ch_j "You want a handjob, hmm. . ."
        $ JeanX.blushing = "_blush1"

    if not JeanX.action_counter["handjob"] and approval:
        if JeanX.Forced:
            $ JeanX.change_face("_sad",1)
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
            ch_j ". . ."
        elif JeanX.love >= (JeanX.obedience + JeanX.inhibition - JeanX.IX):
            $ JeanX.change_face("_sexy",1)
            $ JeanX.brows = "_sad"
            $ JeanX.mouth = "_smile"
            ch_j "Well, I guess it wouldn't be so bad. . ."
        elif JeanX.obedience >= (JeanX.inhibition - JeanX.IX):
            $ JeanX.change_face("_normal",1)
            ch_j "If you want, [JeanX.player_petname]. . ."
        else:
            $ JeanX.change_face("_lipbite",1)
            ch_j "Hmm. . ."

    elif approval:
        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
            ch_j "And that's it?"
        elif not JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "Well, I guess here might not be that bad. . ."
        elif "handjob" in JeanX.recent_history:
            $ JeanX.change_face("_sexy", 1)
            ch_j "Well, I guess another wouldn't hurt. . ."
            jump Jean_HJ_Prep
        elif "handjob" in JeanX.daily_history:
            $ JeanX.change_face("_sexy", 1)
            $ Line = renpy.random.choice(["Another one?",   
                "Didn't get enough earlier?",
                "Again the with handjobs, huh?",
                "I guess you want more."])
            ch_j "[Line]"
        elif JeanX.action_counter["handjob"] < 3:
            $ JeanX.change_face("_sexy", 1)
            $ JeanX.brows = "_confused"
            $ JeanX.mouth = "_kiss"
            ch_j "I guess you're getting used to these. . ."
        else:
            $ JeanX.change_face("_sexy", 1)
            $ JeanX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some more?",                 
                "So you'd like another handjob?",                 
                "You want a. . . [fist pumping hand gestures]?", 
                "Another handjob?"])
            ch_j "[Line]"
        $ Line = 0

    if approval_check(JeanX, 1000) and (approval < 2 or "psysex" not in JeanX.history):

        call Psychic_Sex (JeanX)

    if approval >= 2:
        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("obedience", 90, 1)
            $ JeanX.change_stat("inhibition", 60, 1)
            ch_j "Ok, fine."
        elif "no_handjob" in JeanX.daily_history:
            ch_j "Oh, -fine-. . ."
        else:
            $ JeanX.change_face("_sexy", 1)
            $ JeanX.change_stat("love", 90, 1)
            $ JeanX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Sure, I guess.",                 
                "Okay. . . ",                 
                "Fine.", 
                "I suppose I could. . .",
                "Ok. . . Get over here. . .",
                "Ok, ok."])
            ch_j "[Line]"
            $ Line = 0
        $ JeanX.change_stat("obedience", 20, 1)
        $ JeanX.change_stat("obedience", 60, 1)
        $ JeanX.change_stat("inhibition", 70, 2)
        jump Jean_HJ_Prep
    else:

        $ JeanX.change_face("_angry")
        if "no_handjob" in JeanX.recent_history:
            ch_j "I just told you no, [JeanX.player_petname]."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history and "no_handjob" in JeanX.daily_history:
            ch_j "I told you I wasn't comfortable in public. . ."
        elif "no_handjob" in JeanX.daily_history:
            ch_j "I told you \"no,\" [JeanX.player_petname]."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "I told you I wasn't comfortable in public. . ."
        elif not JeanX.action_counter["handjob"]:
            $ JeanX.change_face("_bemused")
            ch_j "Seriously, [JeanX.player_petname]. . ."
        else:
            $ JeanX.change_face("_bemused")
            ch_j "Nope."
        menu:
            extend ""
            "Sorry, never mind." if "no_handjob" in JeanX.daily_history:
                $ JeanX.change_face("_bemused")
                ch_j "It's fine."
                return
            "Maybe later?" if "no_handjob" not in JeanX.daily_history:
                $ JeanX.change_face("_bemused")
                ch_j "Maybe."
                $ JeanX.change_stat("love", 80, 2)
                $ JeanX.change_stat("inhibition", 70, 2)
                if JeanX.Taboo:
                    $ JeanX.recent_history.append("no_taboo")
                    $ JeanX.daily_history.append("no_taboo")
                $ JeanX.recent_history.append("no_handjob")
                $ JeanX.daily_history.append("no_handjob")
                return
            "I'd really appreciate it. . .":
                if approval:
                    $ JeanX.change_face("_sexy")
                    $ JeanX.change_stat("obedience", 90, 2)
                    $ JeanX.change_stat("obedience", 50, 2)
                    $ JeanX.change_stat("inhibition", 70, 3)
                    $ JeanX.change_stat("inhibition", 40, 2)
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
            "Come on, get to work.":

                $ approval = approval_check(JeanX, 350, "OI", TabM = 3)
                if approval > 1 or (approval and JeanX.Forced):
                    $ JeanX.change_face("_sad")
                    $ JeanX.change_stat("love", 70, -5, 1)
                    $ JeanX.change_stat("love", 200, -2)
                    ch_j ". . . Ok, whatever."
                    $ JeanX.change_stat("obedience", 50, 4)
                    $ JeanX.change_stat("inhibition", 80, 1)
                    $ JeanX.change_stat("inhibition", 60, 3)
                    $ JeanX.Forced = 1
                    jump Jean_HJ_Prep
                else:
                    $ JeanX.change_stat("love", 200, -15)
                    $ JeanX.recent_history.append("_angry")
                    $ JeanX.daily_history.append("_angry")


    $ JeanX.ArmPose = 1
    if "no_handjob" in JeanX.daily_history:
        $ JeanX.change_face("_angry", 1)
        ch_j "Don't ask again."
        $ JeanX.recent_history.append("_angry")
        $ JeanX.daily_history.append("_angry")
    elif JeanX.Forced:
        $ JeanX.change_face("_angry", 1)
        ch_j "No."
        $ JeanX.change_stat("lust", 200, 5)
        if JeanX.love > 300:
            $ JeanX.change_stat("love", 70, -2)
        $ JeanX.change_stat("obedience", 50, -2)
        $ JeanX.recent_history.append("_angry")
        $ JeanX.daily_history.append("_angry")
    elif JeanX.Taboo:
        $ JeanX.change_face("_angry", 1)
        $ JeanX.daily_history.append("no_taboo")
        ch_j "I'm not comfortable in public right now. . ."
        $ JeanX.change_stat("lust", 200, 5)
        $ JeanX.change_stat("obedience", 50, -3)
    elif JeanX.action_counter["handjob"]:
        $ JeanX.change_face("_sad")
        ch_j "I'm not into it today. . ."
    else:
        $ JeanX.change_face("_normal", 1)
        ch_j "I'd really prefer not touching that."
    $ JeanX.recent_history.append("no_handjob")
    $ JeanX.daily_history.append("no_handjob")
    $ approval_bonus = 0
    return


label Jean_HJ_Prep:
    if offhand_action == "handjob":
        return

    if JeanX.Taboo:
        $ JeanX.change_stat("inhibition", 90, int(Taboo/10))
        $ JeanX.change_stat("lust", 50, int(Taboo/5))

    $ JeanX.change_face("_sexy")
    if JeanX.Forced:
        $ JeanX.change_face("_sad")
    elif not JeanX.action_counter["handjob"]:
        $ JeanX.brows = "_confused"
        $ JeanX.eyes = "_sexy"
        $ JeanX.mouth = "_smile"

    call Seen_First_Peen (JeanX, Partner, React=action_context)
    call Jean_HJ_Launch ("L")

    if action_context == JeanX:

        $ action_context = 0
        if offhand_action == "jackin":
            "[JeanX.name] brushes your hand aside and starts stroking your cock."
        else:
            "[JeanX.name] gives you a mischevious smile, and starts to fondle your cock."
        menu:
            "What do you do?"
            "Nothing.":
                $ JeanX.change_stat("inhibition", 70, 3)
                $ JeanX.change_stat("inhibition", 30, 2)
                "[JeanX.name] continues her actions."
            "Praise her.":
                $ JeanX.change_face("_sexy", 1)
                $ JeanX.change_stat("inhibition", 70, 3)
                ch_p "Oooh, that's good, [JeanX.petname]."
                $ JeanX.nameCheck()
                "[JeanX.name] continues her actions."
                $ JeanX.change_stat("love", 80, 1)
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ JeanX.change_face("_surprised")
                $ JeanX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that for now, [JeanX.petname]."
                $ JeanX.nameCheck()
                "[JeanX.name] puts it down."
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("obedience", 50, 1)
                $ JeanX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ JeanX.add_word(1,"refused","refused")
                return

    if not JeanX.action_counter["handjob"]:
        if JeanX.Forced:
            $ JeanX.change_stat("love", 90, -20)
            $ JeanX.change_stat("obedience", 70, 25)
            $ JeanX.change_stat("inhibition", 80, 30)
        else:
            $ JeanX.change_stat("love", 90, 5)
            $ JeanX.change_stat("obedience", 70, 20)
            $ JeanX.change_stat("inhibition", 80, 20)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if JeanX.Taboo:
        $ JeanX.drain_word("no_taboo")
    $ JeanX.drain_word("no_handjob")
    $ JeanX.recent_history.append("handjob")
    $ JeanX.daily_history.append("handjob")

label Jean_HJ_Cycle:
    while Round > 0:
        call shift_focus (JeanX)
        call Jean_HJ_Launch
        $ JeanX.lust_face()

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
                            if JeanX.remaining_actions and multi_action:
                                $ offhand_action = "fondle_breasts"
                                "You start to fondle her breasts."
                                $ JeanX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (JeanX, "tired")
                        "Shift primary action":

                            if JeanX.remaining_actions and multi_action:
                                menu:
                                    "Never Mind":















                                        jump Jean_HJ_Cycle
                            else:
                                call Sex_Basic_Dialog (JeanX, "tired")

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [JeanX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (JeanX)
                                "Ask [JeanX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (JeanX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (JeanX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Jean_HJ_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jean_HJ_Cycle
                                "Never mind":
                                    jump Jean_HJ_Cycle
                        "undress [JeanX.name]":
                            call Girl_Undress (JeanX)
                        "Clean up [JeanX.name] (locked)" if not JeanX.spunk:
                            pass
                        "Clean up [JeanX.name]" if JeanX.spunk:
                            call Girl_Cleanup (JeanX, "ask")
                        "Never mind":
                            jump Jean_HJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jean_HJ_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jean_HJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jean_HJ_Reset
                    $ Line = 0
                    jump Jean_HJ_After


        call shift_focus (JeanX)
        call Sex_Dialog (JeanX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or JeanX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (JeanX)
                if "_angry" in JeanX.recent_history:
                    call Jean_HJ_Reset
                    return
                $ JeanX.change_stat("lust", 200, 5)
                if 100 > JeanX.lust >= 70 and JeanX.session_orgasms < 2 and JeanX.SEXP >= 20:
                    $ JeanX.recent_history.append("unsatisfied")
                    $ JeanX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jean_HJ_After
                $ Line = "came"

            if JeanX.lust >= 100:

                call Girl_Cumming (JeanX)
                if action_context == "shift" or "_angry" in JeanX.recent_history:
                    jump Jean_HJ_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in JeanX.recent_history:
                    "[JeanX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Jean_HJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if counter == 20:
            $ JeanX.brows = "_angry"
            menu:
                ch_j "Ok, I'm bored now. Can we try something else?"




                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    jump Jean_HJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Jean_HJ_Reset
                    $ action_context = "shift"
                    jump Jean_HJ_After
                "No, get back down there.":
                    if approval_check(JeanX, 1200) or approval_check(JeanX, 500, "O"):
                        $ JeanX.change_stat("love", 200, -5)
                        $ JeanX.change_stat("obedience", 50, 3)
                        $ JeanX.change_stat("obedience", 80, 2)
                        "She grumbles but gets back to work."
                    else:
                        $ JeanX.change_face("_angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        ch_j "I have better things to do with my time."
                        $ JeanX.change_stat("love", 50, -3, 1)
                        $ JeanX.change_stat("love", 80, -4, 1)
                        $ JeanX.change_stat("obedience", 30, -1, 1)
                        $ JeanX.change_stat("obedience", 50, -1, 1)
                        $ JeanX.recent_history.append("_angry")
                        $ JeanX.daily_history.append("_angry")
                        jump Jean_HJ_After
        elif counter == 10 and JeanX.SEXP <= 100 and not approval_check(JeanX, 1200, "LO"):
            $ JeanX.brows = "_confused"
            ch_j "Nice, right?"


        call Escalation (JeanX)

        if Round == 10:
            call Sex_Basic_Dialog (JeanX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JeanX, 5)


    $ JeanX.change_face("_bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JeanX, "done")

label Jean_HJ_After:
    $ JeanX.change_face("_sexy")

    $ JeanX.action_counter["handjob"] += 1
    $ JeanX.remaining_actions -=1
    $ JeanX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ JeanX.addiction_rate += 1
    $ JeanX.change_stat("lust", 90, 5)

    call Partner_Like (JeanX, 1)

    if "Jean Handi-Queen" in Achievements:
        pass
    elif JeanX.action_counter["handjob"] >= 10:
        $ JeanX.change_face("_smile", 1)
        ch_j "This seems to be all we do lately. . ."
        $ Achievements.append("Jean Handi-Queen")
        $ JeanX.SEXP += 5
    elif JeanX.action_counter["handjob"] == 1:
        $ JeanX.SEXP += 10
        if JeanX.love >= 500:
            $ JeanX.mouth = "_smile"
            ch_j "That was kinda fun. . ."
        elif Player.focus <= 20:
            $ JeanX.mouth = "_sad"
            ch_j "Pretty nice, right?"
    elif JeanX.action_counter["handjob"] == 5:
        ch_j "I'm pretty good at this, right?"

    $ approval_bonus = 0
    if action_context == "shift":
        ch_j "Ok, so what did you have in mind?"
    else:
        call Jean_HJ_Reset
    call checkout
    return





label Jean_Titjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JeanX)
    if JeanX.action_counter["titjob"] >= 7:
        $ approval_bonus += 10
    elif JeanX.action_counter["titjob"] >= 3:
        $ approval_bonus += 7
    elif JeanX.action_counter["titjob"]:
        $ approval_bonus += 5

    if JeanX.addiction >= 75 and JeanX.event_counter["swallowed"] >=3:
        $ approval_bonus += 15
    elif JeanX.addiction >= 75:
        $ approval_bonus += 5

    if JeanX.SeenChest and approval_check(JeanX, 500):
        $ approval_bonus += 10
    if not JeanX.bra and not JeanX.top:
        $ approval_bonus += 10
    if JeanX.lust > 75:
        $ approval_bonus += 10
    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in JeanX.traits:
        $ approval_bonus += (5*Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JeanX.traits:
        $ approval_bonus -= 30
    if JeanX.event_counter["forced"] and not JeanX.Forced:
        $ approval_bonus -= 5*JeanX.event_counter["forced"]

    if JeanX.Taboo and "no_taboo" in JeanX.daily_history:
        $ approval_bonus -= 10

    if "no_titjob" in JeanX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_titjob" in JeanX.recent_history else 0

    $ approval = approval_check(JeanX, 1200, TabM = 4)

    if not JeanX.action_counter["titjob"] and "no_titjob" not in JeanX.recent_history:
        $ JeanX.change_face("_surprised", 1)
        $ JeanX.mouth = "_kiss"
        ch_j "Oh, you want me to put these to work. . ."
        $ JeanX.change_face("_sly", 1)
        ch_j "I can't blame you. . ."

    if not JeanX.action_counter["titjob"] and approval:
        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
        elif JeanX.love >= (JeanX.obedience + JeanX.inhibition - JeanX.IX):
            $ JeanX.change_face("_sexy")
            $ JeanX.brows = "_sad"
            $ JeanX.mouth = "_smile"
            ch_j "I'd love to, but. . ."
        elif JeanX.obedience >= (JeanX.inhibition - JeanX.IX):
            $ JeanX.change_face("_normal")
            ch_j "If you'd want that. . ."
        elif JeanX.addiction >= 50:
            $ JeanX.change_face("_manic", 1)
            ch_j "Hmmmm. . . ."
        else:
            $ JeanX.change_face("_sad")
            $ JeanX.mouth = "_smile"
            ch_j "Sounds fun, but. . ."
    elif approval:
        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
            ch_j "Well that's a big ask. . ."
        elif not JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "Ok, I guess this is secluded enough. . ."
        elif "titjob" in JeanX.recent_history:
            $ JeanX.change_face("_sexy", 1)
            ch_j "Huh, again?"
            jump Jean_TJ_Prep
        elif "titjob" in JeanX.daily_history:
            $ JeanX.change_face("_sexy", 1)
            $ Line = renpy.random.choice(["Back for more?",   
                "You're really working these babies.", 
                "Didn't get enough earlier?",  
                "You're really working these babies."])
            ch_j "[Line]"
        elif JeanX.action_counter["titjob"] < 3:
            $ JeanX.change_face("_sexy", 1)
            $ JeanX.brows = "_confused"
            $ JeanX.mouth = "_kiss"
            ch_j "Again with the tits, uh?"
        else:
            $ JeanX.change_face("_sexy", 1)
            $ JeanX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action [rubs her chest]?",                 
                "So you'd like another titjob?",                  
                "So you'd like another titjob?",                               
                "So you'd like another titjob?",                              
                "Another titjob?", 
                "A little [points at her chest]?"])
            ch_j "[Line]"
        $ Line = 0

    if approval >= 2:
        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("obedience", 90, 1)
            $ JeanX.change_stat("inhibition", 60, 1)
            ch_j "I can't fault your taste. . ."
        elif "no_titjob" in JeanX.daily_history:
            ch_j "Hmm, I guess. . ."
        else:
            $ JeanX.change_face("_sexy", 1)
            $ JeanX.change_stat("love", 90, 1)
            $ JeanX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, put it here.",                 
                "Well. . . ok.",                 
                "Yum.", 
                "Sure, whip it out.",
                "Heh, ok."])
            ch_j "[Line]"
            $ Line = 0
        $ JeanX.change_stat("obedience", 20, 1)
        $ JeanX.change_stat("obedience", 70, 1)
        $ JeanX.change_stat("inhibition", 80, 2)
        jump Jean_TJ_Prep
    else:

        $ JeanX.change_face("_angry")
        if "no_titjob" in JeanX.recent_history:
            ch_j "I {i}just{/i} told you \"no,\" [JeanX.player_petname]."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history and "no_titjob" in JeanX.daily_history:
            ch_j "I don't want to show off the goods like that!"
        elif "no_titjob" in JeanX.daily_history:
            ch_j "I already told you \"no,\" [JeanX.player_petname]."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "I don't want to show off the goods like that!"
        elif not JeanX.action_counter["titjob"]:
            $ JeanX.change_face("_bemused")
            ch_j "Not really my thing, [JeanX.player_petname]. . ."
        else:
            $ JeanX.change_face("_bemused")
            ch_j "Not right now [JeanX.player_petname]. . ."

        menu:
            extend ""
            "Sorry, never mind." if "no_titjob" in JeanX.daily_history:
                $ JeanX.change_face("_bemused")
                ch_j "Ok, fine, [JeanX.player_petname]."
                return
            "Maybe later?" if "no_titjob" not in JeanX.daily_history:
                $ JeanX.change_face("_sexy")
                ch_j ". . . maybe."
                $ JeanX.change_stat("love", 80, 2)
                $ JeanX.change_stat("inhibition", 70, 2)
                if JeanX.Taboo:
                    $ JeanX.recent_history.append("no_taboo")
                    $ JeanX.daily_history.append("no_taboo")
                $ JeanX.recent_history.append("no_titjob")
                $ JeanX.daily_history.append("no_titjob")
                return
            "I think this could be fun for both of us. . .":
                if approval:
                    $ JeanX.change_face("_sexy")
                    $ JeanX.change_stat("obedience", 80, 2)
                    $ JeanX.change_stat("obedience", 40, 2)
                    $ JeanX.change_stat("inhibition", 70, 3)
                    $ JeanX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Well, ok, put it here.",                 
                        "Well. . . ok.",                 
                        "I guess.", 
                        "I guess, whip it out.",
                        "Heh, ok."])
                    ch_j "[Line]"
                    $ Line = 0
                    jump Jean_TJ_Prep
                else:
                    $ approval = approval_check(JeanX, 1100, TabM = 3)
                    if approval >= 2 and JeanX.action_counter["blowjob"]:
                        $ JeanX.change_stat("inhibition", 80, 1)
                        $ JeanX.change_stat("inhibition", 60, 3)
                        $ JeanX.change_face("_confused", 1)
                        ch_j "What about a blowjob then?"
                        menu:
                            ch_j "What about a blowjob then?"
                            "Ok, get down there.":
                                $ JeanX.change_stat("love", 80, 2)
                                $ JeanX.change_stat("inhibition", 60, 1)
                                $ JeanX.change_stat("obedience", 50, 1)
                                jump Jean_BJ_Prep
                            "Nah, it's all about dem titties.":
                                $ Line = "no_BJ"
                    if approval and JeanX.action_counter["handjob"]:
                        $ JeanX.change_stat("inhibition", 80, 1)
                        $ JeanX.change_stat("inhibition", 60, 3)
                        $ JeanX.change_face("_confused", 1)
                        ch_j "I could give you a hand job?"
                        menu:
                            ch_j "What do you say?"
                            "Sure, that's fine.":
                                $ JeanX.change_stat("love", 80, 2)
                                $ JeanX.change_stat("inhibition", 60, 1)
                                $ JeanX.change_stat("obedience", 50, 1)
                                jump Jean_HJ_Prep
                            "Seriously, titties." if Line == "no_BJ":
                                $ Line = 0
                            "Nah, it's all about dem titties." if Line != "no_BJ":
                                pass
                    $ JeanX.change_stat("love", 200, -2)
                    ch_j "Well then too bad, I guess."
                    $ JeanX.change_stat("obedience", 70, 2)
            "Come on, let me fuck those titties, [JeanX.petname]":


                $ JeanX.nameCheck()
                $ approval = approval_check(JeanX, 700, "OI", TabM = 4)
                if approval > 1 or (approval and JeanX.Forced):
                    $ JeanX.change_face("_angry",1)
                    $ JeanX.change_stat("love", 70, -5, 1)
                    $ JeanX.change_stat("love", 200, -2)
                    ch_j ". . ."
                    $ JeanX.change_face("_angry",1,Eyes="_side")
                    ch_j "Ok, fine, whip it out."
                    $ JeanX.change_stat("obedience", 50, 4)
                    $ JeanX.change_stat("inhibition", 80, 1)
                    $ JeanX.change_stat("inhibition", 60, 3)
                    $ JeanX.Forced = 1
                    jump Jean_TJ_Prep
                else:
                    $ JeanX.change_stat("love", 200, -15)
                    $ JeanX.recent_history.append("_angry")
                    $ JeanX.daily_history.append("_angry")


    if "no_titjob" in JeanX.daily_history:
        $ JeanX.change_face("_angry", 1)
        ch_j "I already told you no."
        $ JeanX.recent_history.append("_angry")
        $ JeanX.daily_history.append("_angry")
    elif JeanX.Forced:
        $ JeanX.change_face("_angry", 1)
        ch_j "No, try something else."
        $ JeanX.change_stat("lust", 200, 5)
        if JeanX.love > 300:
            $ JeanX.change_stat("love", 70, -2)
        $ JeanX.change_stat("obedience", 50, -2)
        $ JeanX.recent_history.append("_angry")
        $ JeanX.daily_history.append("_angry")
    elif JeanX.Taboo:
        $ JeanX.change_face("_angry", 1)
        $ JeanX.daily_history.append("no_taboo")
        ch_j "You really expect me to do that here?"
        ch_j "You know I can't \"take care of that\" anymore. . ."
        $ JeanX.change_stat("lust", 200, 5)
        $ JeanX.change_stat("obedience", 50, -3)
    elif JeanX.action_counter["titjob"]:
        $ JeanX.change_face("_sad")
        ch_j "You'll know when it's time for that."
    else:
        $ JeanX.change_face("_normal", 1)
        ch_j "Nah."
    $ JeanX.recent_history.append("no_titjob")
    $ JeanX.daily_history.append("no_titjob")
    $ approval_bonus = 0
    return

label Jean_TJ_Prep:
    if JeanX.Taboo:
        $ JeanX.change_stat("inhibition", 90, int(Taboo/10))
        $ JeanX.change_stat("lust", 50, int(Taboo/5))


    $ JeanX.change_face("_sexy")
    if JeanX.Forced:
        $ JeanX.change_face("_sad")
    elif not JeanX.action_counter["titjob"]:
        $ JeanX.brows = "_confused"
        $ JeanX.eyes = "_sexy"
        $ JeanX.mouth = "_smile"

    call Seen_First_Peen (JeanX, Partner, React=action_context)
    call Jean_TJ_Launch ("L")

    if action_context == JeanX:

        $ action_context = 0
        "[JeanX.name] slides down and sandwiches your dick between her tits."
        menu:
            "What do you do?"
            "Nothing.":
                $ JeanX.change_stat("inhibition", 80, 3)
                $ JeanX.change_stat("inhibition", 40, 2)
                "[JeanX.name] starts to slide them up and down."
            "Praise her.":
                $ JeanX.change_face("_sexy", 1)
                $ JeanX.change_stat("inhibition", 80, 3)
                ch_p "Oh, that sounds like a good idea, [JeanX.petname]."
                $ JeanX.nameCheck()
                "[JeanX.name] continues her actions."
                $ JeanX.change_stat("love", 85, 1)
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ JeanX.change_face("_confused")
                $ JeanX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that for now, [JeanX.petname]."
                $ JeanX.nameCheck()
                "[JeanX.name] lets it drop out from between her breasts."
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("obedience", 50, 3)
                $ Player.recent_history.append("nope")
                $ JeanX.add_word(1,"refused","refused")
                return

    if not JeanX.action_counter["titjob"]:
        if JeanX.Forced:
            $ JeanX.change_stat("love", 90, -25)
            $ JeanX.change_stat("obedience", 70, 30)
            $ JeanX.change_stat("inhibition", 80, 35)
        else:
            $ JeanX.change_stat("love", 90, 5)
            $ JeanX.change_stat("obedience", 70, 25)
            $ JeanX.change_stat("inhibition", 80, 30)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if JeanX.Taboo:
        $ JeanX.drain_word("no_taboo")
    $ JeanX.drain_word("no_titjob")
    $ JeanX.recent_history.append("titjob")
    $ JeanX.daily_history.append("titjob")

label Jean_TJ_Cycle:
    while Round > 0:
        call shift_focus (JeanX)
        call Jean_TJ_Launch
        $ JeanX.lust_face()

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
                            if JeanX.remaining_actions and multi_action:
                                $ offhand_action = "fondle_breasts"
                                "You start to fondle her breasts."
                                $ JeanX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (JeanX, "tired")
                        "Shift primary action":

                            if JeanX.remaining_actions and multi_action:
                                menu:
                                    "How about a blowjob?":
                                        $ action_context = "shift"
                                        call Jean_TJ_After
                                        call Jean_Blowjob
                                    "How about a handy?":
                                        $ action_context = "shift"
                                        call Jean_BJ_After
                                        call Jean_Handjob
                                    "Never Mind":
                                        jump Jean_TJ_Cycle
                            else:
                                call Sex_Basic_Dialog (JeanX, "tired")

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [JeanX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (JeanX)
                                "Ask [JeanX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (JeanX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (JeanX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Jean_TJ_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jean_TJ_Cycle
                                "Never mind":
                                    jump Jean_TJ_Cycle
                        "undress [JeanX.name]":
                            call Girl_Undress (JeanX)
                        "Clean up [JeanX.name] (locked)" if not JeanX.spunk:
                            pass
                        "Clean up [JeanX.name]" if JeanX.spunk:
                            call Girl_Cleanup (JeanX, "ask")
                        "Never mind":
                            jump Jean_TJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jean_TJ_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jean_TJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jean_TJ_Reset
                    $ Line = 0
                    jump Jean_TJ_After


        call shift_focus (JeanX)
        call Sex_Dialog (JeanX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or JeanX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (JeanX)
                if "_angry" in JeanX.recent_history:
                    call Jean_TJ_Reset
                    return
                $ JeanX.change_stat("lust", 200, 5)
                if 100 > JeanX.lust >= 70 and JeanX.session_orgasms < 2 and JeanX.SEXP >= 20:
                    $ JeanX.recent_history.append("unsatisfied")
                    $ JeanX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jean_TJ_After
                $ Line = "came"

            if JeanX.lust >= 100:

                call Girl_Cumming (JeanX)
                if action_context == "shift" or "_angry" in JeanX.recent_history:
                    jump Jean_TJ_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in JeanX.recent_history:
                    "[JeanX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Jean_TJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)
        if action_speed >= 4:
            call action_speed_Shift (0)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if JeanX.SEXP >= 100 or approval_check(JeanX, 1200, "LO"):
            pass
        elif counter == (5 + JeanX.action_counter["titjob"]):
            $ JeanX.brows = "_confused"
            ch_j "Hey, how you doing up there? About done?"
        if counter == (10 + JeanX.action_counter["titjob"]):
            $ JeanX.brows = "_angry"
            menu:
                ch_j "Ok, seriously, can't we do something else?"
                "How about a BJ?" if JeanX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Jean_TJ_After
                    call Jean_Blowjob
                    return
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    jump Jean_TJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Jean_TJ_Reset
                    $ action_context = "shift"
                    jump Jean_TJ_After
                "No, get back down there.":
                    if approval_check(JeanX, 1200) or approval_check(JeanX, 500, "O"):
                        $ JeanX.change_stat("love", 200, -5)
                        $ JeanX.change_stat("obedience", 50, 3)
                        $ JeanX.change_stat("obedience", 80, 2)
                        "She grumbles but gets back to work."
                    else:
                        $ JeanX.change_face("_angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        ch_j "Well fuck you then."
                        $ JeanX.change_stat("love", 50, -3, 1)
                        $ JeanX.change_stat("love", 80, -4, 1)
                        $ JeanX.change_stat("obedience", 30, -1, 1)
                        $ JeanX.change_stat("obedience", 50, -1, 1)
                        $ JeanX.recent_history.append("_angry")
                        $ JeanX.daily_history.append("_angry")
                        jump Jean_TJ_After


        call Escalation (JeanX)

        if Round == 10:
            call Sex_Basic_Dialog (JeanX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JeanX, 5)


    $ JeanX.change_face("_bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JeanX, "done")

label Jean_TJ_After:
    $ JeanX.change_face("_sexy")

    $ JeanX.action_counter["titjob"] += 1
    $ JeanX.remaining_actions -=1
    $ JeanX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ JeanX.addiction_rate += 1

    call Partner_Like (JeanX, 4)

    if JeanX.action_counter["titjob"] > 5:
        pass
    elif JeanX.action_counter["titjob"] == 1:
        $ JeanX.SEXP += 12
        if JeanX.love >= 500:
            $ JeanX.mouth = "_smile"
            ch_j "OK, that was fun."
        elif Player.focus <= 20:
            $ JeanX.mouth = "_sad"
            ch_j "I hope that worked out for you. . ."
    elif JeanX.action_counter["titjob"] == 5:
        ch_j "Fun, right?"

    $ approval_bonus = 0

    if action_context == "shift":
        ch_j "Mmm, so what else did you have in mind?"
    else:
        call Jean_TJ_Reset
    call checkout
    return







label Jean_Blowjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JeanX)
    if JeanX.action_counter["blowjob"] >= 7:
        $ approval_bonus += 15
    elif JeanX.action_counter["blowjob"] >= 3:
        $ approval_bonus += 10
    elif JeanX.action_counter["blowjob"]:
        $ approval_bonus += 7

    if JeanX.addiction >= 75 and JeanX.event_counter["swallowed"] >=3:
        $ approval_bonus += 25
    elif JeanX.addiction >= 75:
        $ approval_bonus += 15

    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in JeanX.traits:
        $ approval_bonus += (4*Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JeanX.traits:
        $ approval_bonus -= 40
    if JeanX.event_counter["forced"] and not JeanX.Forced:
        $ approval_bonus -= 5*JeanX.event_counter["forced"]

    if JeanX.Taboo and "no_taboo" in JeanX.daily_history:
        $ approval_bonus -= 10

    if "no_blowjob" in JeanX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_blowjob" in JeanX.recent_history else 0

    $ approval = approval_check(JeanX, 1300, TabM = 4)

    if not JeanX.action_counter["blowjob"] and "no_blowjob" not in JeanX.recent_history:
        $ JeanX.change_face("_surprised", 2)
        $ JeanX.mouth = "_kiss"
        ch_j "Oh! You want me to suck you off?"

    if not JeanX.action_counter["blowjob"] and approval:
        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
        elif JeanX.love >= (JeanX.obedience + JeanX.inhibition - JeanX.IX):
            $ JeanX.change_face("_sexy")
            $ JeanX.brows = "_sad"
            $ JeanX.mouth = "_smile"
            ch_j "Well, I could hardly turn down that offer. . ."
        elif JeanX.obedience >= (JeanX.inhibition - JeanX.IX):
            $ JeanX.change_face("_normal")
            ch_j "I could do that, I guess. . ."
        elif JeanX.addiction >= 50:
            $ JeanX.change_face("_manic", 1)
            ch_j "Mmmmm. . ."
        else:
            $ JeanX.change_face("_sad")
            $ JeanX.mouth = "_smile"
            ch_j "Huh. . ."
    elif approval:
        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
            ch_j "Again?"
        elif not JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "Hmm, this is private enough. . ."
        elif "blowjob" in JeanX.recent_history:
            $ JeanX.change_face("_sexy", 1)
            ch_j "Mmm, again?"
            jump Jean_BJ_Prep
        elif "blowjob" in JeanX.daily_history:
            $ JeanX.change_face("_sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",   
                "You're wearing me out here.",  
                "I must be too good at this.", 
                "Didn't get enough earlier?"])
            ch_j "[Line]"
        elif JeanX.action_counter["blowjob"] < 3:
            $ JeanX.change_face("_sexy", 1)
            $ JeanX.brows = "_confused"
            $ JeanX.mouth = "_kiss"
            ch_j "You'd like another blowjob?"
        else:
            $ JeanX.change_face("_sexy", 1)
            $ JeanX.ArmPose = 2
            $ Line = renpy.random.choice(["You want me to [mimes blowing]?",                 
                "So you want another blowjob?",                 
                "You want me to lick you?", 
                "You want me to suck you off?",
                "A BJ?"])
            ch_j "[Line]"
        $ Line = 0

    if approval >= 2:
        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("obedience", 90, 1)
            $ JeanX.change_stat("inhibition", 60, 1)
            ch_j "Fine, let's get this over with."
        elif "no_blowjob" in JeanX.daily_history:
            ch_j "Fine. . ."
        else:
            $ JeanX.change_face("_sexy", 1)
            $ JeanX.change_stat("love", 90, 1)
            $ JeanX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Sure. Ahhhhhh.",                 
                "Well. . . alright.",                 
                "Yum.", 
                "Sure, whip it out.",
                "Ok. . . [She licks her lips].",
                "Alright, let's see it."])
            ch_j "[Line]"
            $ Line = 0
        $ JeanX.change_stat("obedience", 20, 1)
        $ JeanX.change_stat("obedience", 70, 1)
        $ JeanX.change_stat("inhibition", 80, 2)
        jump Jean_BJ_Prep
    else:

        $ JeanX.change_face("_angry")
        if "no_blowjob" in JeanX.recent_history:
            ch_j "Just told you I wouldn't, [JeanX.player_petname]."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history and "no_blowjob" in JeanX.daily_history:
            ch_j "Like I said, not in public."
        elif "no_blowjob" in JeanX.daily_history:
            ch_j "Told you \"no,\" [JeanX.player_petname]."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "Like I said, too public!"
        elif not JeanX.action_counter["blowjob"]:
            $ JeanX.change_face("_bemused")
            ch_j "I have been wondering what you taste like, [JeanX.player_petname]. . ."
        else:
            $ JeanX.change_face("_bemused")
            ch_j "I don't know, [JeanX.player_petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_blowjob" in JeanX.daily_history:
                $ JeanX.change_face("_bemused")
                ch_j "Ok then."
                return
            "Maybe later?" if "no_blowjob" not in JeanX.daily_history:
                $ JeanX.change_face("_sexy")
                ch_j "Sure, whatever, [JeanX.player_petname]."
                $ JeanX.change_stat("love", 80, 2)
                $ JeanX.change_stat("inhibition", 70, 2)
                if JeanX.Taboo:
                    $ JeanX.recent_history.append("no_taboo")
                    $ JeanX.daily_history.append("no_taboo")
                $ JeanX.recent_history.append("no_blowjob")
                $ JeanX.daily_history.append("no_blowjob")
                return
            "Come on, please?":
                if approval:
                    $ JeanX.change_face("_sexy")
                    $ JeanX.change_stat("obedience", 90, 2)
                    $ JeanX.change_stat("obedience", 50, 2)
                    $ JeanX.change_stat("inhibition", 70, 3)
                    $ JeanX.change_stat("inhibition", 40, 2)
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
                    if approval_check(JeanX, 1100, TabM = 3):
                        $ JeanX.change_stat("inhibition", 80, 1)
                        $ JeanX.change_stat("inhibition", 60, 3)
                        $ JeanX.change_face("_confused", 1)
                        $ JeanX.arms = 1
                        if "psysex" in JeanX.history:
                            ch_j "Couldn't I just do the mind thing again?"
                            $ JeanX.change_face("_sly", 1)
                            ch_j "You seemed to enjoy that one. . ."
                        else:
                            ch_j "What if I just used my telekinesis?"
                            $ JeanX.change_face("_confused", 1)
                            ch_j "It would feel great, I promise. . ."
                        menu:
                            extend ""
                            "Sure, that's fine.":
                                $ JeanX.change_stat("love", 80, 2)
                                $ JeanX.change_stat("inhibition", 60, 1)
                                $ JeanX.change_stat("obedience", 50, 1)
                                jump Jean_PJ_Prep
                            "Nah, if it's not a BJ, forget it.":
                                $ JeanX.change_stat("love", 200, -2)
                                $ JeanX.arms = ""
                                ch_j "too bad then."
                                $ JeanX.change_stat("obedience", 70, 2)
            "Suck it, [JeanX.petname]":


                $ JeanX.nameCheck()
                $ approval = approval_check(JeanX, 750, "OI", TabM = 3)
                if approval > 1 or (approval and JeanX.Forced):
                    $ JeanX.change_face("_angry",2)
                    $ JeanX.change_stat("love", 70, -5, 1)
                    $ JeanX.change_stat("love", 200, -2)
                    ch_j ". . ."
                    $ JeanX.change_face("_angry",1,Eyes="_side")
                    ch_j "Whatever. . ."
                    $ JeanX.change_stat("obedience", 50, 4)
                    $ JeanX.change_stat("inhibition", 80, 1)
                    $ JeanX.change_stat("inhibition", 60, 3)
                    $ JeanX.Forced = 1
                    jump Jean_BJ_Prep
                else:
                    $ JeanX.change_stat("love", 200, -15)
                    $ JeanX.recent_history.append("_angry")
                    $ JeanX.daily_history.append("_angry")


    if "no_blowjob" in JeanX.daily_history:
        $ JeanX.change_face("_angry", 1)
        $ JeanX.ArmPose = 2
        ch_j "You want me to make you suck yourself?"
        $ JeanX.ArmPose = 1
        $ JeanX.change_face("_angry",1,Eyes="_side")
        ch_j "Damn. . . forgot I can't do that. . ."
        $ JeanX.recent_history.append("_angry")
        $ JeanX.daily_history.append("_angry")
    elif JeanX.Forced:
        $ JeanX.change_face("_angry", 1)
        ch_j "I'm not doing that."
        $ JeanX.change_stat("lust", 200, 5)
        if JeanX.love > 300:
            $ JeanX.change_stat("love", 70, -2)
        $ JeanX.change_stat("obedience", 50, -2)
        $ JeanX.recent_history.append("_angry")
        $ JeanX.daily_history.append("_angry")
        $ JeanX.recent_history.append("no_blowjob")
        $ JeanX.daily_history.append("no_blowjob")
        return
    elif JeanX.Taboo:
        $ JeanX.change_face("_angry", 1)
        $ JeanX.daily_history.append("no_taboo")
        ch_j "I'm not comfortable in public right now. . ."
        $ JeanX.change_stat("lust", 200, 5)
        $ JeanX.change_stat("obedience", 50, -3)
        return
    elif JeanX.action_counter["blowjob"]:
        $ JeanX.change_face("_sad")
        ch_j "Nah, not this time."
    else:
        $ JeanX.change_face("_smile", 1)
        ch_j "Ha! Good one."
    $ JeanX.recent_history.append("no_blowjob")
    $ JeanX.daily_history.append("no_blowjob")
    $ approval_bonus = 0
    return


label Jean_BJ_Prep:
    if renpy.showing("Jean_HJ_Animation"):
        hide Jean_HJ_Animation with easeoutbottom
    if JeanX.Taboo:
        $ JeanX.change_stat("inhibition", 90, int(Taboo/10))
        $ JeanX.change_stat("lust", 50, int(Taboo/5))

    $ JeanX.change_face("_sexy")
    if JeanX.Forced:
        $ JeanX.change_face("_sad")
    elif not JeanX.action_counter["blowjob"]:
        $ JeanX.brows = "_confused"
        $ JeanX.eyes = "_sexy"
        $ JeanX.mouth = "_smile"

    call Seen_First_Peen (JeanX, Partner, React=action_context)
    call Jean_BJ_Launch ("L")
    if action_context == JeanX:

        $ action_context = 0
        "[JeanX.name] slides down and gives your cock a little lick."
        menu:
            "What do you do?"
            "Nothing.":
                $ JeanX.change_stat("inhibition", 80, 3)
                $ JeanX.change_stat("inhibition", 40, 2)
                "[JeanX.name] continues licking at it."
            "Praise her.":
                $ JeanX.change_face("_sexy", 1)
                $ JeanX.change_stat("inhibition", 80, 3)
                ch_p "Hmmm, keep doing that, [JeanX.petname]."
                $ JeanX.nameCheck()
                "[JeanX.name] continues her actions."
                $ JeanX.change_stat("love", 85, 1)
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ JeanX.change_face("_surprised")
                $ JeanX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that for now, [JeanX.petname]."
                $ JeanX.nameCheck()
                "[JeanX.name] puts it down."
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("obedience", 50, 3)
                $ Player.recent_history.append("nope")
                $ JeanX.add_word(1,"refused","refused")
                return
    if not JeanX.action_counter["blowjob"]:
        if JeanX.Forced:
            $ JeanX.change_stat("love", 90, -70)
            $ JeanX.change_stat("obedience", 70, 45)
            $ JeanX.change_stat("inhibition", 80, 60)
        else:
            $ JeanX.change_stat("love", 90, 5)
            $ JeanX.change_stat("obedience", 70, 35)
            $ JeanX.change_stat("inhibition", 80, 40)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if JeanX.Taboo:
        $ JeanX.drain_word("no_taboo")
    $ JeanX.drain_word("no_blowjob")
    $ JeanX.recent_history.append("blowjob")
    $ JeanX.daily_history.append("blowjob")

label Jean_BJ_Cycle:
    while Round > 0:
        call shift_focus (JeanX)
        call Jean_BJ_Launch
        $ JeanX.lust_face()

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

                "Suck on it. (locked)" if action_speed == 3:
                    pass

                "Take it deeper." if action_speed != 4:
                    if offhand_action == "jackin" and action_speed != 3:
                        "She takes it to the root, and you move your hand out of the way."
                    call action_speed_Shift (4)
                "Take it deeper. (locked)" if action_speed == 4:
                    pass
                "Set your own pace. . .":

                    "[JeanX.name] hums contentedly."
                    if "setpace" not in JeanX.recent_history:
                        $ JeanX.change_stat("love", 80, 2)
                    $ D20 = renpy.random.randint(1, 20)
                    if JeanX.action_counter["blowjob"] < 5:
                        $ D20 -= 10
                    elif JeanX.action_counter["blowjob"] < 10:
                        $ D20 -= 5

                    if D20 > 15:
                        call action_speed_Shift (4)
                        if "setpace" not in JeanX.recent_history:
                            $ JeanX.change_stat("inhibition", 80, 3)
                    elif D20 > 10:
                        call action_speed_Shift (3)
                    elif D20 > 5:
                        call action_speed_Shift (2)
                    else:
                        call action_speed_Shift (1)
                    $ JeanX.recent_history.append("setpace")

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
                            if JeanX.remaining_actions and multi_action:
                                $ offhand_action = "fondle_breasts"
                                "You start to fondle her breasts."
                                $ JeanX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (JeanX, "tired")
                        "Shift primary action":

                            if JeanX.remaining_actions and multi_action:
                                menu:
                                    "How about a handy?":
                                        $ action_context = "shift"
                                        call Jean_BJ_After
                                        call Jean_Handjob
                                    "How about a titjob?":
                                        $ action_context = "shift"
                                        call Jean_BJ_After
                                        call Jean_Titjob
                                    "Never Mind":
                                        jump Jean_BJ_Cycle
                            else:
                                call Sex_Basic_Dialog (JeanX, "tired")

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [JeanX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (JeanX)
                                "Ask [JeanX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (JeanX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (JeanX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Jean_BJ_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jean_BJ_Cycle
                                "Never mind":
                                    jump Jean_BJ_Cycle
                        "undress [JeanX.name]":
                            call Girl_Undress (JeanX)
                        "Clean up [JeanX.name] (locked)" if not JeanX.spunk:
                            pass
                        "Clean up [JeanX.name]" if JeanX.spunk:
                            call Girl_Cleanup (JeanX, "ask")
                        "Never mind":
                            jump Jean_BJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jean_BJ_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jean_BJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jean_BJ_Reset
                    $ Line = 0
                    jump Jean_BJ_After


        call shift_focus (JeanX)
        call Sex_Dialog (JeanX, Partner)



        $ counter += 1
        $ Round -= 1
        if action_speed:
            $ Player.cock_wet = 1
            $ Player.spunk = 0 if Player.spunk else Player.spunk

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or JeanX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (JeanX)
                if "_angry" in JeanX.recent_history:
                    call Jean_BJ_Reset
                    return
                $ JeanX.change_stat("lust", 200, 5)
                if 100 > JeanX.lust >= 70 and JeanX.session_orgasms < 2 and JeanX.SEXP >= 20:
                    $ JeanX.recent_history.append("unsatisfied")
                    $ JeanX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jean_BJ_After
                $ Line = "came"

            if JeanX.lust >= 100:

                call Girl_Cumming (JeanX)
                if action_context == "shift" or "_angry" in JeanX.recent_history:
                    jump Jean_BJ_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."

                if "unsatisfied" in JeanX.recent_history:
                    "[JeanX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Jean_BJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if JeanX.SEXP >= 100 or approval_check(JeanX, 1200, "LO"):
            pass
        elif counter == (10 + JeanX.action_counter["blowjob"]):
            $ JeanX.brows = "_angry"
            menu:
                ch_j "Ok, that's enough of that. Can we do something else?"
                "How about a Handy?" if JeanX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Jean_BJ_After
                    call Jean_Handjob
                    return
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    jump Jean_BJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Jean_BJ_Reset
                    $ action_context = "shift"
                    jump Jean_BJ_After
                "No, get back down there.":
                    if approval_check(JeanX, 1200) or approval_check(JeanX, 500, "O"):
                        $ JeanX.change_stat("love", 200, -5)
                        $ JeanX.change_stat("obedience", 50, 3)
                        $ JeanX.change_stat("obedience", 80, 2)
                        "She grumbles but gets back to work."
                    else:
                        $ JeanX.change_face("_angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        ch_j "Ok, have fun with that then."
                        $ JeanX.change_stat("love", 50, -3, 1)
                        $ JeanX.change_stat("love", 80, -4, 1)
                        $ JeanX.change_stat("obedience", 30, -1, 1)
                        $ JeanX.change_stat("obedience", 50, -1, 1)
                        $ JeanX.recent_history.append("_angry")
                        $ JeanX.daily_history.append("_angry")
                        jump Jean_BJ_After
        elif counter == (5 + JeanX.action_counter["blowjob"]) and JeanX.SEXP <= 100 and not approval_check(JeanX, 1200, "LO"):
            $ JeanX.brows = "_confused"
            ch_j "Hey, you about done up there?"


        call Escalation (JeanX)

        if Round == 10:
            call Sex_Basic_Dialog (JeanX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JeanX, 5)


    $ JeanX.change_face("_bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JeanX, "done")

label Jean_BJ_After:
    $ JeanX.change_face("_sexy")

    $ JeanX.action_counter["blowjob"] += 1
    $ JeanX.remaining_actions -=1
    $ JeanX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ JeanX.addiction_rate += 1

    call Partner_Like (JeanX, 2)

    if "Jean Jobber" in Achievements:
        pass
    elif JeanX.action_counter["blowjob"] >= 10:
        $ JeanX.change_face("_confused", 1,Eyes="_side")
        ch_j "Wow, you know. . . I don't always love this. . ."
        $ JeanX.change_face("_smile", 2)
        ch_j "but I guess with you it's different somehow. . ."
        $ JeanX.blushing = "_blush1"
        $ Achievements.append("Jean Jobber")
        $ JeanX.SEXP += 5
    elif action_context == "shift":
        pass
    elif JeanX.action_counter["blowjob"] == 1:
        $ JeanX.SEXP += 15
        if JeanX.love >= 500:
            $ JeanX.mouth = "_smile"
            ch_j "Mmm, yeah, that was as good as I expected. . ."
        elif Player.focus <= 20:
            $ JeanX.mouth = "_sad"
            ch_j "Well, got what you wanted from that?"
    elif JeanX.action_counter["blowjob"] == 5:
        ch_j "I am loving this. You too, right?"
        menu:
            "[[nod]":
                $ JeanX.change_face("_smile", 1)
                $ JeanX.change_stat("love", 90, 15)
                $ JeanX.change_stat("obedience", 80, 5)
                $ JeanX.change_stat("inhibition", 90, 10)
            "[[shake head \"no\"]":
                if approval_check(JeanX, 500, "O"):
                    $ JeanX.change_face("_sad", 2)
                    $ JeanX.change_stat("love", 200, -5)
                else:
                    $ JeanX.change_face("_angry", 2)
                    $ JeanX.change_stat("love", 200, -25)
                $ JeanX.change_stat("obedience", 80, 10)
                ch_j ". . ."
                $ JeanX.change_face("_angry", 1)

    $ approval_bonus = 0
    if action_context != "shift":
        call Jean_BJ_Reset
    call checkout
    return






label Jean_Dildo_Check:
    if "_dildo" in Player.inventory:
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "_dildo" in JeanX.inventory:
        "You ask [JeanX.name] to get out her favorite Dildo."
    else:
        "You don't have one of those on you."
        return 0
    return 1

label Jean_Dildo_Pussy:

    ch_j "You know what? I'm just not into this right now. . ."
    "[[not yet implemented]"
    return

    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JeanX)
    call Jean_Dildo_Check
    if not _return:
        return

    if JeanX.action_counter["dildo_pussy"]:
        $ approval_bonus += 15
    if JeanX.legs == "pants:":
        $ approval_bonus -= 20

    if JeanX.lust > 95:
        $ approval_bonus += 20
    elif JeanX.lust > 85:
        $ approval_bonus += 15

    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in JeanX.traits:
        $ approval_bonus += (5*Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JeanX.traits:
        $ approval_bonus -= 40
    if JeanX.event_counter["forced"] and not JeanX.Forced:
        $ approval_bonus -= 5*JeanX.event_counter["forced"]

    if JeanX.Taboo and "no_taboo" in JeanX.daily_history:
        $ approval_bonus -= 10

    if "no_dildo" in JeanX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_dildo" in JeanX.recent_history else 0

    $ approval = approval_check(JeanX, 1250, TabM = 4)

    if action_context == JeanX:
        if approval > 2:
            if JeanX.PantsNum() == 5:
                "[JeanX.name] grabs her dildo, hiking up her skirt as she does."
                $ JeanX.upskirt = 1
            elif JeanX.PantsNum() >= 6:
                "[JeanX.name] grabs her dildo, pulling down her pants as she does."
                $ JeanX.legs = ""
            else:
                "[JeanX.name] grabs her dildo, rubbing is suggestively against her crotch."
            $ JeanX.SeenPanties = 1
            call Jean_First_Bottomless (1)
            "She slides the tip along her pussy and seems to want you to insert it."
            menu:
                "What do you do?"
                "Nothing.":
                    $ JeanX.change_stat("inhibition", 80, 3)
                    $ JeanX.change_stat("inhibition", 50, 2)
                    "[JeanX.name] slides it in."
                "Go for it.":
                    $ JeanX.change_face("_sexy", 1)
                    $ JeanX.change_stat("inhibition", 80, 3)
                    ch_p "Oh yeah, [JeanX.petname], let's do this."
                    $ JeanX.nameCheck()
                    "You grab the dildo and slide it in."
                    $ JeanX.change_stat("love", 85, 1)
                    $ JeanX.change_stat("obedience", 90, 1)
                    $ JeanX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ JeanX.change_face("_surprised")
                    $ JeanX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that right now, [JeanX.petname]."
                    $ JeanX.nameCheck()
                    "[JeanX.name] sets the dildo down."
                    $ JeanX.change_outfit()
                    $ JeanX.change_stat("obedience", 90, 1)
                    $ JeanX.change_stat("obedience", 50, 1)
                    $ JeanX.change_stat("obedience", 30, 2)
                    return
            jump Jean_DP_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
        return

    if action_context == "auto":
        "You rub the dildo across her body, and along her moist slit."
        $ JeanX.change_face("_surprised", 1)

        if (JeanX.action_counter["dildo_pussy"] and approval) or (approval > 1):
            "[JeanX.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            $ JeanX.change_face("_sexy")
            $ JeanX.change_stat("obedience", 70, 3)
            $ JeanX.change_stat("inhibition", 50, 3)
            $ JeanX.change_stat("inhibition", 70, 1)
            ch_j "Ooo, [JeanX.player_petname], toys!"
            jump Jean_DP_Prep
        else:
            $ JeanX.brows = "_angry"
            menu:
                ch_j "Hey, what are you planning to do with that?!"
                "Sorry, sorry! Never mind.":
                    if approval:
                        $ JeanX.change_face("_sexy", 1)
                        $ JeanX.change_stat("obedience", 70, 3)
                        $ JeanX.change_stat("inhibition", 50, 3)
                        $ JeanX.change_stat("inhibition", 70, 1)
                        ch_j "Well, now that you mention it. . ."
                        jump Jean_DP_Prep
                    "You pull back before you really get it in."
                    $ JeanX.change_face("_bemused", 1)
                    if JeanX.action_counter["dildo_pussy"]:
                        ch_j "Well ok, [JeanX.player_petname], maybe warn me next time?"
                    else:
                        ch_j "Well ok, [JeanX.player_petname], that's a little much. . . for now . . ."
                "Just playing with my favorite toys.":
                    $ JeanX.change_stat("love", 80, -10, 1)
                    $ JeanX.change_stat("love", 200, -10)
                    "You press it inside some more."
                    $ JeanX.change_stat("obedience", 70, 3)
                    $ JeanX.change_stat("inhibition", 50, 3)
                    if not approval_check(JeanX, 700, "O", TabM=1):
                        $ JeanX.change_face("_angry")
                        "[JeanX.name] shoves you away and slaps you in the face."
                        ch_j "Jerk!"
                        ch_j "Ask nice if you want to stick something in my pussy!"
                        $ JeanX.change_stat("love", 50, -10, 1)
                        $ JeanX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        if renpy.showing("Jean_SexSprite"):
                            call Jean_Sex_Reset
                        $ JeanX.recent_history.append("_angry")
                        $ JeanX.daily_history.append("_angry")
                    else:
                        $ JeanX.change_face("_sad")
                        "[JeanX.name] doesn't seem to be into this, you're lucky she's so obedient."
                        jump Jean_DP_Prep
        return


    if not JeanX.action_counter["dildo_pussy"]:

        $ JeanX.change_face("_surprised", 1)
        $ JeanX.mouth = "_kiss"
        ch_j "Hmmm, so you'd like to try out some toys?"
        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            ch_j "I suppose there are worst things you could ask for."

    if not JeanX.action_counter["dildo_pussy"] and approval:

        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
        elif JeanX.love >= (JeanX.obedience + JeanX.inhibition - JeanX.IX):
            $ JeanX.change_face("_sexy")
            $ JeanX.brows = "_sad"
            $ JeanX.mouth = "_smile"
            ch_j "I've had a reasonable amount of experience with these, you know. . ."
        elif JeanX.obedience >= (JeanX.inhibition - JeanX.IX):
            $ JeanX.change_face("_normal")
            ch_j "If that's what you want, [JeanX.player_petname]. . ."
        else:
            $ JeanX.change_face("_sad")
            $ JeanX.mouth = "_smile"
            ch_j "I guess it could be fun with a partner. . ."

    elif approval:

        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
            ch_j "The toys again?"
        elif not JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "Well, at least you got us some privacy this time. . ."
        elif "dildo_pussy" in JeanX.recent_history:
            $ JeanX.change_face("_sexy", 1)
            ch_j "Mmm, again? Ok, let's get to it."
            jump Jean_DP_Prep
        elif "dildo_pussy" in JeanX.daily_history:
            $ JeanX.change_face("_sexy", 1)
            $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "You're going to wear me out."])
            ch_j "[Line]"
        elif JeanX.action_counter["dildo_pussy"] < 3:
            $ JeanX.change_face("_sexy", 1)
            $ JeanX.brows = "_confused"
            $ JeanX.mouth = "_kiss"
            ch_j "You want to stick it in my pussy again?"
        else:
            $ JeanX.change_face("_sexy", 1)
            $ JeanX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my pussy again?",
                    "You want me ta lube up your toy?"])
            ch_j "[Line]"
            $ Line = 0

    if approval >= 2:

        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("obedience", 90, 1)
            $ JeanX.change_stat("inhibition", 60, 1)
            ch_j "Ok, fine."
        else:
            $ JeanX.change_face("_sexy", 1)
            $ JeanX.change_stat("love", 90, 1)
            $ JeanX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                    "Well. . . ok.",                 
                    "Sure!", 
                    "I guess I could. . . stick it in.",
                    "Hells yeah.",
                    "Heh, ok, ok."])
            ch_j "[Line]"
            $ Line = 0
        $ JeanX.change_stat("obedience", 20, 1)
        $ JeanX.change_stat("obedience", 60, 1)
        $ JeanX.change_stat("inhibition", 70, 2)
        jump Jean_DP_Prep
    else:


        $ JeanX.change_face("_angry")
        if "no_dildo" in JeanX.recent_history:
            ch_j "What part of \"no,\" did you not get, [JeanX.player_petname]?"
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history and "no_dildo" in JeanX.daily_history:
            ch_j "Stop swinging that thing around in public!"
        elif "no_dildo" in JeanX.daily_history:
            ch_j "I already told you \"no,\" [JeanX.player_petname]."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "Stop swinging that thing around in public!"
        elif not JeanX.action_counter["dildo_pussy"]:
            $ JeanX.change_face("_bemused")
            ch_j "I'm just not into toys, [JeanX.player_petname]. . ."
        else:
            $ JeanX.change_face("_bemused")
            ch_j "I don't think we need any toys, [JeanX.player_petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no_dildo" in JeanX.daily_history:
                $ JeanX.change_face("_bemused")
                ch_j "Yeah, ok, [JeanX.player_petname]."
                return
            "Maybe later?" if "no_dildo" not in JeanX.daily_history:
                $ JeanX.change_face("_sexy")
                ch_j "Maybe I'll practice on my own time, [JeanX.player_petname]."
                $ JeanX.change_stat("love", 80, 2)
                $ JeanX.change_stat("inhibition", 70, 2)
                if JeanX.Taboo:
                    $ JeanX.recent_history.append("no_taboo")
                    $ JeanX.daily_history.append("no_taboo")
                $ JeanX.recent_history.append("no_dildo")
                $ JeanX.daily_history.append("no_dildo")
                return
            "I think you'd like it. . .":
                if approval:
                    $ JeanX.change_face("_sexy")
                    $ JeanX.change_stat("obedience", 90, 2)
                    $ JeanX.change_stat("obedience", 50, 2)
                    $ JeanX.change_stat("inhibition", 70, 3)
                    $ JeanX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                            "I suppose. . .", 
                            "You've got me there."])
                    ch_j "[Line]"
                    $ Line = 0
                    jump Jean_DP_Prep
                else:
                    pass
            "[[press it against her]":

                $ approval = approval_check(JeanX, 950, "OI", TabM = 3)
                if approval > 1 or (approval and JeanX.Forced):
                    $ JeanX.change_face("_sad")
                    $ JeanX.change_stat("love", 70, -5, 1)
                    $ JeanX.change_stat("love", 200, -5)
                    ch_j "Ok, fine. If we're going to do this, stick it in already."
                    $ JeanX.change_stat("obedience", 80, 4)
                    $ JeanX.change_stat("inhibition", 80, 1)
                    $ JeanX.change_stat("inhibition", 60, 3)
                    $ JeanX.Forced = 1
                    jump Jean_DP_Prep
                else:
                    $ JeanX.change_stat("love", 200, -20)
                    $ JeanX.recent_history.append("_angry")
                    $ JeanX.daily_history.append("_angry")


    $ JeanX.ArmPose = 1
    if "no_dildo" in JeanX.daily_history:
        ch_j "Learn to take \"no\" for an answer, [JeanX.player_petname]."
        $ JeanX.recent_history.append("_angry")
        $ JeanX.daily_history.append("_angry")
    elif JeanX.Forced:
        $ JeanX.change_face("_angry", 1)
        ch_j "I'm not going to let you use that on me."
        $ JeanX.change_stat("lust", 200, 5)
        if JeanX.love > 300:
            $ JeanX.change_stat("love", 70, -2)
        $ JeanX.change_stat("obedience", 50, -2)
        $ JeanX.recent_history.append("_angry")
        $ JeanX.daily_history.append("_angry")
    elif JeanX.Taboo:
        $ JeanX.change_face("_angry", 1)
        $ JeanX.recent_history.append("no_taboo")
        $ JeanX.daily_history.append("no_taboo")
        ch_j "Not here!"
        $ JeanX.change_stat("lust", 200, 5)
        $ JeanX.change_stat("obedience", 50, -3)
    elif JeanX.action_counter["dildo_pussy"]:
        $ JeanX.change_face("_sad")
        ch_j "Sorry, you can keep your toys to yourself."
    else:
        $ JeanX.change_face("_normal", 1)
        ch_j "No way."
    $ JeanX.recent_history.append("no_dildo")
    $ JeanX.daily_history.append("no_dildo")
    $ approval_bonus = 0
    return

label Jean_DP_Prep:
    if offhand_action == "dildo_pussy":
        return

    if not JeanX.Forced and action_context != "auto":
        $ approval_bonus = 15 if JeanX.PantsNum() >= 6 else 0
        call Bottoms_Off (JeanX)
        if "_angry" in JeanX.recent_history:
            return

    $ approval_bonus = 0
    call Jean_Pussy_Launch ("dildo_pussy")
    if not JeanX.action_counter["dildo_pussy"]:
        if JeanX.Forced:
            $ JeanX.change_stat("love", 90, -75)
            $ JeanX.change_stat("obedience", 70, 60)
            $ JeanX.change_stat("inhibition", 80, 35)
        else:
            $ JeanX.change_stat("love", 90, 10)
            $ JeanX.change_stat("obedience", 70, 20)
            $ JeanX.change_stat("inhibition", 80, 45)
    if JeanX.Taboo:
        $ JeanX.change_stat("inhibition", 90, int(Taboo/10))
        $ JeanX.change_stat("lust", 50, int(Taboo/5))


    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if JeanX.Taboo:
        $ JeanX.drain_word("no_taboo")
    $ JeanX.drain_word("no_dildo")
    $ JeanX.recent_history.append("dildo_pussy")
    $ JeanX.daily_history.append("dildo_pussy")

label Jean_DP_Cycle:
    while Round > 0:
        call shift_focus (JeanX)
        call Jean_Pussy_Launch ("dildo_pussy")
        $ JeanX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (JeanX)
                    jump Jean_DP_Cycle

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
                            if JeanX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ JeanX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (JeanX, "tired")
                        "Shift primary action":

                            if JeanX.remaining_actions and multi_action:
                                menu:
                                    "I want to stick a finger in her ass.":
                                        $ action_context = "shift"
                                        call Jean_DP_After
                                        call Jean_Insert_Ass
                                    "Just stick a finger in her ass without asking.":
                                        $ action_context = "auto"
                                        call Jean_DP_After
                                        call Jean_Insert_Ass
                                    "I want to shift the dildo to her ass.":
                                        $ action_context = "shift"
                                        call Jean_DP_After
                                        call Jean_Dildo_Ass
                                    "Never Mind":
                                        jump Jean_DP_Cycle
                            else:
                                call Sex_Basic_Dialog (JeanX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Jean_DP_After
                            call Offhand_Set
                        "Shift your focus (locked)" if not offhand_action:
                            pass
                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [JeanX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (JeanX)
                                "Ask [JeanX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (JeanX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (JeanX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Jean_DP_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jean_DP_Cycle
                                "Never mind":
                                    jump Jean_DP_Cycle
                        "undress [JeanX.name]":
                            call Girl_Undress (JeanX)
                        "Clean up [JeanX.name] (locked)" if not JeanX.spunk:
                            pass
                        "Clean up [JeanX.name]" if JeanX.spunk:
                            call Girl_Cleanup (JeanX, "ask")
                        "Never mind":
                            jump Jean_DP_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jean_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jean_DP_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jean_Pos_Reset
                    $ Line = 0
                    jump Jean_DP_After


        if JeanX.underwear or JeanX.PantsNum() >= 6 or JeanX.HoseNum() >= 5:
            call Girl_Undress (JeanX, "auto")

        call shift_focus (JeanX)
        call Sex_Dialog (JeanX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or JeanX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (JeanX)
                if "_angry" in JeanX.recent_history:
                    call Jean_Pos_Reset
                    return
                $ JeanX.change_stat("lust", 200, 5)
                if 100 > JeanX.lust >= 70 and JeanX.session_orgasms < 2:
                    $ JeanX.recent_history.append("unsatisfied")
                    $ JeanX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jean_DP_After
                $ Line = "came"

            if JeanX.lust >= 100:

                call Girl_Cumming (JeanX)
                if action_context == "shift" or "_angry" in JeanX.recent_history:
                    jump Jean_DP_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in JeanX.recent_history:
                    "[JeanX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Jean_DP_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if JeanX.SEXP >= 100 or approval_check(JeanX, 1200, "LO"):
            pass
        elif counter == (5 + JeanX.action_counter["dildo_pussy"]):
            $ JeanX.brows = "_confused"
            ch_j "What are you even doing down there?"
        elif JeanX.lust >= 80:
            pass
        elif counter == (15 + JeanX.action_counter["dildo_pussy"]) and JeanX.SEXP >= 15 and not approval_check(JeanX, 1500):
            $ JeanX.brows = "_confused"
            menu:
                ch_j "[JeanX.player_petname], this is getting uncomfortable, maybe we could try something else."
                "Finish up.":
                    "You let go. . ."
                    jump Jean_DP_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Jean_DP_After
                "No, this is fun.":
                    if approval_check(JeanX, 1200) or approval_check(JeanX, 500, "O"):
                        $ JeanX.change_stat("love", 200, -5)
                        $ JeanX.change_stat("obedience", 50, 3)
                        $ JeanX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ JeanX.change_face("_angry", 1)
                        call Jean_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_j "Well if that's your attitude, I don't need your \"help\"."
                        $ JeanX.change_stat("love", 50, -3, 1)
                        $ JeanX.change_stat("love", 80, -4, 1)
                        $ JeanX.change_stat("obedience", 30, -1, 1)
                        $ JeanX.change_stat("obedience", 50, -1, 1)
                        $ JeanX.recent_history.append("_angry")
                        $ JeanX.daily_history.append("_angry")
                        jump Jean_DP_After


        if Round == 10:
            call Sex_Basic_Dialog (JeanX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JeanX, 5)


    $ JeanX.change_face("_bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JeanX, "done")

label Jean_DP_After:
    if not action_context:
        call Jean_Pos_Reset

    $ JeanX.change_face("_sexy")

    $ JeanX.action_counter["dildo_pussy"] += 1
    $ JeanX.remaining_actions -=1

    call Partner_Like (JeanX, 1)

    if JeanX.action_counter["dildo_pussy"] == 1:
        $ JeanX.SEXP += 10
        if not action_context:
            if JeanX.love >= 500 and "unsatisfied" not in JeanX.recent_history:
                ch_j "Thanks for the extra hand. . ."
            elif JeanX.obedience <= 500 and Player.focus <= 20:
                $ JeanX.change_face("_perplexed", 1)
                ch_j "Did you like that?"

    $ approval_bonus = 0


    call checkout
    return






label Jean_Dildo_Ass:

    ch_j "You know what? I'm just not into this right now. . ."
    "[[not yet implemented]"
    return

    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JeanX)
    call Jean_Dildo_Check
    if not _return:
        return

    if JeanX.used_to_anal:
        $ approval_bonus += 30
    elif "anal" in JeanX.recent_history or "dildo_anal" in JeanX.recent_history:
        $ approval_bonus -= 20
    elif "anal" in JeanX.daily_history or "dildo_anal" in JeanX.daily_history:
        $ approval_bonus -= 10
    elif (JeanX.action_counter["anal"] + JeanX.action_counter["dildo_ass"] + JeanX.Plug) > 0:
        $ approval_bonus += 20

    if JeanX.legs == "pants:":
        $ approval_bonus -= 20

    if JeanX.lust > 95:
        $ approval_bonus += 20
    elif JeanX.lust > 85:
        $ approval_bonus += 15

    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in JeanX.traits:
        $ approval_bonus += (5*Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JeanX.traits:
        $ approval_bonus -= 40
    if JeanX.event_counter["forced"] and not JeanX.Forced:
        $ approval_bonus -= 5*JeanX.event_counter["forced"]

    if JeanX.Taboo and "no_taboo" in JeanX.daily_history:
        $ approval_bonus -= 10

    if "no_dildo" in JeanX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_dildo" in JeanX.recent_history else 0

    $ approval = approval_check(JeanX, 1450, TabM = 4)

    if action_context == JeanX:

        if approval > 2:
            if JeanX.PantsNum() == 5:
                "[JeanX.name] grabs her dildo, hiking up her skirt as she does."
                $ JeanX.upskirt = 1
            elif JeanX.PantsNum() >= 6:
                "[JeanX.name] grabs her dildo, pulling down her pants as she does."
                $ JeanX.legs = ""
            else:
                "[JeanX.name] grabs her dildo, rubbing is suggestively against her ass."
            $ JeanX.SeenPanties = 1
            call Jean_First_Bottomless (1)
            "She slides the tip against her asshole, and seems to want you to insert it."
            menu:
                "What do you do?"
                "Nothing.":
                    $ JeanX.change_stat("inhibition", 80, 3)
                    $ JeanX.change_stat("inhibition", 50, 2)
                    "[JeanX.name] slides it in."
                "Go for it.":
                    $ JeanX.change_face("_sexy", 1)
                    $ JeanX.change_stat("inhibition", 80, 3)
                    ch_p "Oh yeah, [JeanX.petname], let's do this."
                    $ JeanX.nameCheck()
                    "You grab the dildo and slide it in."
                    $ JeanX.change_stat("love", 85, 1)
                    $ JeanX.change_stat("obedience", 90, 1)
                    $ JeanX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ JeanX.change_face("_surprised")
                    $ JeanX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that right now, [JeanX.petname]."
                    $ JeanX.nameCheck()
                    "[JeanX.name] sets the dildo down."
                    $ JeanX.change_outfit()
                    $ JeanX.change_stat("obedience", 90, 1)
                    $ JeanX.change_stat("obedience", 50, 1)
                    $ JeanX.change_stat("obedience", 30, 2)
                    return
            jump Jean_DA_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
        return

    if action_context == "auto":
        "You rub the dildo across her body, and against her tight anus."
        $ JeanX.change_face("_surprised", 1)

        if (JeanX.action_counter["dildo_ass"] and approval) or (approval > 1):

            "[JeanX.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            $ JeanX.change_face("_sexy")
            $ JeanX.change_stat("obedience", 70, 3)
            $ JeanX.change_stat("inhibition", 50, 3)
            $ JeanX.change_stat("inhibition", 70, 1)
            ch_j "Ooo, [JeanX.player_petname], toys!"
            jump Jean_DA_Prep
        else:

            $ JeanX.brows = "_angry"
            menu:
                ch_j "Hey, what are you planning to do with that?!"
                "Sorry, sorry! Never mind.":
                    if approval:
                        $ JeanX.change_face("_sexy", 1)
                        $ JeanX.change_stat("obedience", 70, 3)
                        $ JeanX.change_stat("inhibition", 50, 3)
                        $ JeanX.change_stat("inhibition", 70, 1)
                        ch_j "Well, now that you mention it. . ."
                        jump Jean_DA_Prep
                    "You pull back before you really get it in."
                    $ JeanX.change_face("_bemused", 1)
                    if JeanX.action_counter["dildo_ass"]:
                        ch_j "Well ok, [JeanX.player_petname], maybe warn me next time?"
                    else:
                        ch_j "Well ok, [JeanX.player_petname], that's a little much. . . for now . . ."
                "Just playing with my favorite toys.":
                    $ JeanX.change_stat("love", 80, -10, 1)
                    $ JeanX.change_stat("love", 200, -10)
                    "You press it inside some more."
                    $ JeanX.change_stat("obedience", 70, 3)
                    $ JeanX.change_stat("inhibition", 50, 3)
                    if not approval_check(JeanX, 700, "O", TabM=1):
                        $ JeanX.change_face("_angry")
                        "[JeanX.name] shoves you away and slaps you in the face."
                        ch_j "Jerk!"
                        ch_j "Ask nice if you want to stick something in my ass!"
                        $ JeanX.change_stat("love", 50, -10, 1)
                        $ JeanX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        if renpy.showing("Jean_SexSprite"):
                            call Jean_Sex_Reset
                        $ JeanX.recent_history.append("_angry")
                        $ JeanX.daily_history.append("_angry")
                    else:
                        $ JeanX.change_face("_sad")
                        "[JeanX.name] doesn't seem to be into this, you're lucky she's so obedient."
                        jump Jean_DA_Prep
        return


    if not JeanX.action_counter["dildo_ass"]:

        $ JeanX.change_face("_surprised", 1)
        $ JeanX.mouth = "_kiss"
        ch_j "You want to try and fit that. . .?"
        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            ch_j "Always about the butt, huh?"

    if not JeanX.used_to_anal and ("dildo_anal" in JeanX.recent_history or "anal" in JeanX.recent_history or "dildo_anal" in JeanX.daily_history or "anal" in JeanX.daily_history):
        $ JeanX.change_face("_bemused", 1)
        ch_j "I'm still sore from earlier. . ."

    if not JeanX.action_counter["dildo_ass"] and approval:

        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
        elif JeanX.love >= (JeanX.obedience + JeanX.inhibition - JeanX.IX):
            $ JeanX.change_face("_sexy")
            $ JeanX.brows = "_sad"
            $ JeanX.mouth = "_smile"
            ch_j "I haven't actually used one of these, back there before. . ."
        elif JeanX.obedience >= (JeanX.inhibition - JeanX.IX):
            $ JeanX.change_face("_normal")
            ch_j "If that's what you want, [JeanX.player_petname]. . ."
        else:
            $ JeanX.change_face("_sad")
            $ JeanX.mouth = "_smile"
            ch_j "I guess it could be fun two-player. . ."

    elif approval:

        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
            ch_j "The toys again?"
        elif not JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "Well, at least you got us some privacy this time. . ."
        elif "dildo_anal" in JeanX.daily_history and not JeanX.used_to_anal:
            pass
        elif "dildo_anal" in JeanX.daily_history:
            $ JeanX.change_face("_sexy", 1)
            $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "I'm still a bit sore from earlier.",
                    "You're going to wear me out."])
            ch_j "[Line]"
        elif JeanX.action_counter["dildo_ass"] < 3:
            $ JeanX.change_face("_sexy", 1)
            $ JeanX.brows = "_confused"
            $ JeanX.mouth = "_kiss"
            ch_j "You want to stick it in my ass again?"
        else:
            $ JeanX.change_face("_sexy", 1)
            $ JeanX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my ass again?",
                    "You want me ta lube up your toy?"])
            ch_j "[Line]"
            $ Line = 0

    if approval >= 2:

        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("obedience", 90, 1)
            $ JeanX.change_stat("inhibition", 60, 1)
            ch_j "Ok, fine."
        else:
            $ JeanX.change_face("_sexy", 1)
            $ JeanX.change_stat("love", 90, 1)
            $ JeanX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                    "Well. . . ok.",                 
                    "Sure!", 
                    "I guess I could. . . stick it in.",
                    "Hells yeah.",
                    "Heh, ok, ok."])
            ch_j "[Line]"
            $ Line = 0
        $ JeanX.change_stat("obedience", 20, 1)
        $ JeanX.change_stat("obedience", 60, 1)
        $ JeanX.change_stat("inhibition", 70, 2)
        jump Jean_DA_Prep
    else:


        $ JeanX.change_face("_angry")
        if "no_dildo" in JeanX.recent_history:
            ch_j "What part of \"no,\" did you not get, [JeanX.player_petname]?"
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history and "no_dildo" in JeanX.daily_history:
            ch_j "Stop swinging that thing around in public!"
        elif "no_dildo" in JeanX.daily_history:
            ch_j "I already told you \"no,\" [JeanX.player_petname]."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "I already told you that I wouldn't do that out here!"
        elif not JeanX.action_counter["dildo_ass"]:
            $ JeanX.change_face("_bemused")
            ch_j "I'm just not into toys, [JeanX.player_petname]. . ."
        elif not JeanX.used_to_anal and "dildo_anal" not in JeanX.daily_history:
            $ JeanX.change_face("_perplexed")
            ch_j "You could have been a bit more gentle last time, [JeanX.player_petname]. . ."
        else:
            $ JeanX.change_face("_bemused")
            ch_j "I don't think we need any toys, [JeanX.player_petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no_dildo" in JeanX.daily_history:
                $ JeanX.change_face("_bemused")
                ch_j "Yeah, ok, [JeanX.player_petname]."
                return
            "Maybe later?" if "no_dildo" not in JeanX.daily_history:
                $ JeanX.change_face("_sexy")
                ch_j "Maybe I'll practice on my own time, [JeanX.player_petname]."
                $ JeanX.change_stat("love", 80, 2)
                $ JeanX.change_stat("inhibition", 70, 2)
                if JeanX.Taboo:
                    $ JeanX.recent_history.append("no_taboo")
                    $ JeanX.daily_history.append("no_taboo")
                $ JeanX.recent_history.append("no_dildo")
                $ JeanX.daily_history.append("no_dildo")
                return
            "I think you'd like it. . .":
                if approval:
                    $ JeanX.change_face("_sexy")
                    $ JeanX.change_stat("obedience", 90, 2)
                    $ JeanX.change_stat("obedience", 50, 2)
                    $ JeanX.change_stat("inhibition", 70, 3)
                    $ JeanX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                            "I suppose. . .", 
                            "You've got me there."])
                    ch_j "[Line]"
                    $ Line = 0
                    jump Jean_DA_Prep
                else:
                    pass
            "[[press it against her]":

                $ approval = approval_check(JeanX, 1050, "OI", TabM = 3)
                if approval > 1 or (approval and JeanX.Forced):
                    $ JeanX.change_face("_sad")
                    $ JeanX.change_stat("love", 70, -5, 1)
                    $ JeanX.change_stat("love", 200, -5)
                    ch_j "Ok, fine. If we're going to do this, stick it in already."
                    $ JeanX.change_stat("obedience", 80, 4)
                    $ JeanX.change_stat("inhibition", 80, 1)
                    $ JeanX.change_stat("inhibition", 60, 3)
                    $ JeanX.Forced = 1
                    jump Jean_DA_Prep
                else:
                    $ JeanX.change_stat("love", 200, -20)
                    $ JeanX.recent_history.append("_angry")
                    $ JeanX.daily_history.append("_angry")


    $ JeanX.ArmPose = 1
    if "no_dildo" in JeanX.daily_history:
        ch_j "Learn to take \"no\" for an answer, [JeanX.player_petname]."
        $ JeanX.recent_history.append("_angry")
        $ JeanX.daily_history.append("_angry")
    elif JeanX.Forced:
        $ JeanX.change_face("_angry", 1)
        ch_j "I'm not going to let you use that on me."
        $ JeanX.change_stat("lust", 200, 5)
        if JeanX.love > 300:
            $ JeanX.change_stat("love", 70, -2)
        $ JeanX.change_stat("obedience", 50, -2)
        $ JeanX.recent_history.append("_angry")
        $ JeanX.daily_history.append("_angry")
    elif JeanX.Taboo:
        $ JeanX.change_face("_angry", 1)
        $ JeanX.recent_history.append("no_taboo")
        $ JeanX.daily_history.append("no_taboo")
        ch_j "Not here!"
        $ JeanX.change_stat("lust", 200, 5)
        $ JeanX.change_stat("obedience", 50, -3)
    elif not JeanX.used_to_anal and "dildo_anal" in JeanX.daily_history:
        $ JeanX.change_face("_bemused")
        ch_j "Sorry, I just need a little break back there, [JeanX.player_petname]."
    elif JeanX.action_counter["dildo_ass"]:
        $ JeanX.change_face("_sad")
        ch_j "Sorry, you can keep your toys out of there."
    else:
        $ JeanX.change_face("_normal", 1)
        ch_j "No way."
    $ JeanX.recent_history.append("no_dildo")
    $ JeanX.daily_history.append("no_dildo")
    $ approval_bonus = 0
    return

label Jean_DA_Prep:
    if offhand_action == "dildo_anal":
        return

    if not JeanX.Forced and action_context != "auto":
        $ approval_bonus = 20 if JeanX.PantsNum() >= 6 else 0
        call Bottoms_Off (JeanX)
        if "_angry" in JeanX.recent_history:
            return

    $ approval_bonus = 0
    call Jean_Pussy_Launch ("dildo_anal")
    if not JeanX.action_counter["dildo_ass"]:
        if JeanX.Forced:
            $ JeanX.change_stat("love", 90, -75)
            $ JeanX.change_stat("obedience", 70, 60)
            $ JeanX.change_stat("inhibition", 80, 35)
        else:
            $ JeanX.change_stat("love", 90, 10)
            $ JeanX.change_stat("obedience", 70, 20)
            $ JeanX.change_stat("inhibition", 80, 45)
    if JeanX.Taboo:
        $ JeanX.change_stat("inhibition", 90, int(Taboo/10))
        $ JeanX.change_stat("lust", 50, int(Taboo/5))


    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if JeanX.Taboo:
        $ JeanX.drain_word("no_taboo")
    $ JeanX.drain_word("no_dildo")
    $ JeanX.recent_history.append("dildo_anal")
    $ JeanX.daily_history.append("dildo_anal")

label Jean_DA_Cycle:
    while Round > 0:
        call shift_focus (JeanX)
        call Jean_Pussy_Launch ("dildo_anal")
        $ JeanX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (JeanX)
                    jump Jean_DA_Cycle

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
                            if JeanX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ JeanX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (JeanX, "tired")
                        "Shift primary action":

                            if JeanX.remaining_actions and multi_action:
                                menu:
                                    "I want to stick a finger in her pussy.":
                                        $ action_context = "shift"
                                        call Jean_DA_After
                                        call Jean_Fondle_Pussy
                                    "Just stick a finger in her pussy without asking.":
                                        $ action_context = "auto"
                                        call Jean_DA_After
                                        call Jean_Fondle_Pussy
                                    "I want to shift the dildo to her pussy.":
                                        $ action_context = "shift"
                                        call Jean_DA_After
                                        call Jean_Dildo_Pussy
                                    "Never Mind":
                                        jump Jean_DA_Cycle
                            else:
                                call Sex_Basic_Dialog (JeanX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Jean_DA_After
                            call Offhand_Set
                        "Shift your focus (locked)" if not offhand_action:
                            pass
                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [JeanX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (JeanX)
                                "Ask [JeanX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (JeanX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (JeanX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Jean_DA_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jean_DA_Cycle
                        "Never mind":
                            jump Jean_DA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jean_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jean_DA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jean_Pos_Reset
                    $ Line = 0
                    jump Jean_DA_After


        if JeanX.underwear or JeanX.PantsNum() >= 6 or JeanX.HoseNum() >= 5:
            call Girl_Undress (JeanX, "auto")

        call shift_focus (JeanX)
        call Sex_Dialog (JeanX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or JeanX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (JeanX)
                if "_angry" in JeanX.recent_history:
                    call Jean_Pos_Reset
                    return
                $ JeanX.change_stat("lust", 200, 5)
                if 100 > JeanX.lust >= 70 and JeanX.session_orgasms < 2:
                    $ JeanX.recent_history.append("unsatisfied")
                    $ JeanX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jean_DA_After
                $ Line = "came"

            if JeanX.lust >= 100:

                call Girl_Cumming (JeanX)
                if action_context == "shift" or "_angry" in JeanX.recent_history:
                    jump Jean_DA_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in JeanX.recent_history:
                    "[JeanX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Jean_DA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if JeanX.SEXP >= 100 or approval_check(JeanX, 1200, "LO"):
            pass
        elif counter == (5 + JeanX.action_counter["dildo_ass"]):
            $ JeanX.brows = "_confused"
            ch_j "What are you even doing down there?"
        elif JeanX.lust >= 80:
            pass
        elif counter == (15 + JeanX.action_counter["dildo_ass"]) and JeanX.SEXP >= 15 and not approval_check(JeanX, 1500):
            $ JeanX.brows = "_confused"
            menu:
                ch_j "[JeanX.player_petname], this is getting uncomfortable, maybe we could try something else."
                "Finish up.":
                    "You let go. . ."
                    jump Jean_DA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Jean_DA_After
                "No, this is fun.":
                    if approval_check(JeanX, 1200) or approval_check(JeanX, 500, "O"):
                        $ JeanX.change_stat("love", 200, -5)
                        $ JeanX.change_stat("obedience", 50, 3)
                        $ JeanX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ JeanX.change_face("_angry", 1)
                        call Jean_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_j "Well if that's your attitude, I don't need your \"help\"."
                        $ JeanX.change_stat("love", 50, -3, 1)
                        $ JeanX.change_stat("love", 80, -4, 1)
                        $ JeanX.change_stat("obedience", 30, -1, 1)
                        $ JeanX.change_stat("obedience", 50, -1, 1)
                        $ JeanX.recent_history.append("_angry")
                        $ JeanX.daily_history.append("_angry")
                        jump Jean_DA_After


        if Round == 10:
            call Sex_Basic_Dialog (JeanX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JeanX, 5)


    $ JeanX.change_face("_bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JeanX, "done")

label Jean_DA_After:
    if not action_context:
        call Jean_Pos_Reset

    $ JeanX.change_face("_sexy")

    $ JeanX.action_counter["dildo_ass"] += 1
    $ JeanX.remaining_actions -=1

    call Partner_Like (JeanX, 1)

    if JeanX.action_counter["dildo_ass"] == 1:
        $ JeanX.SEXP += 10
        if not action_context:
            if JeanX.love >= 500 and "unsatisfied" not in JeanX.recent_history:
                if JeanX.used_to_anal:
                    ch_j "That was. . . interesting. . ."
                else:
                    ch_j "Ouch. . ."
            elif JeanX.obedience <= 500 and Player.focus <= 20:
                $ JeanX.change_face("_perplexed", 1)
                ch_j "Did you like that?"

    $ approval_bonus = 0


    call checkout
    return



label Jean_Vibrator_Check:
    if "_vibrator" in Player.inventory:
        "You pull out the \"shocker\" vibrator, handy."
    elif "_vibrator" in JeanX.inventory:
        "You ask [JeanX.name] to get out her vibrator."
    else:
        "You don't have one of those on you."
        return 0
    return 1


label Jean_Footjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JeanX)
    if JeanX.action_counter["footjob"] >= 7:
        $ approval_bonus += 10
    elif JeanX.action_counter["footjob"] >= 3:
        $ approval_bonus += 7
    elif JeanX.action_counter["footjob"]:
        $ approval_bonus += 3

    if JeanX.addiction >= 75 and JeanX.event_counter["swallowed"] >=3:
        $ approval_bonus += 10
    if JeanX.addiction >= 75:
        $ approval_bonus += 5

    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in JeanX.traits:
        $ approval_bonus += (3*Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JeanX.traits:
        $ approval_bonus -= 40
    if JeanX.event_counter["forced"] and not JeanX.Forced:
        $ approval_bonus -= 5*JeanX.event_counter["forced"]

    if JeanX.Taboo and "no_taboo" in JeanX.daily_history:
        $ approval_bonus -= 10

    if "no_foot" in JeanX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_foot" in JeanX.recent_history else 0

    $ approval = approval_check(JeanX, 1250, TabM = 3)

    if action_context == JeanX:
        if approval > 2:
            "[JeanX.name] leans back and starts rubbing your cock with her foot."
            menu:
                "What do you do?"
                "Nothing.":
                    $ JeanX.change_stat("inhibition", 70, 3)
                    $ JeanX.change_stat("inhibition", 30, 2)
                    "[JeanX.name] continues her actions."
                "Praise her.":
                    $ JeanX.change_face("_sexy", 1)
                    $ JeanX.change_stat("inhibition", 70, 3)
                    ch_p "Oooh, that's good, [JeanX.petname]."
                    $ JeanX.nameCheck()
                    "[JeanX.name] continues her actions."
                    $ JeanX.change_stat("love", 80, 1)
                    $ JeanX.change_stat("obedience", 90, 1)
                    $ JeanX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ JeanX.change_face("_surprised")
                    $ JeanX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that for now, [JeanX.petname]."
                    $ JeanX.nameCheck()
                    "[JeanX.name] puts it down."
                    $ JeanX.change_stat("obedience", 90, 1)
                    $ JeanX.change_stat("obedience", 50, 1)
                    $ JeanX.change_stat("obedience", 30, 2)
                    return
            if primary_action:
                $ girl_offhand_action = "footjob"
                return
            jump Jean_FJ_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if not JeanX.action_counter["footjob"] and "no_foot" not in JeanX.recent_history:
        $ JeanX.change_face("_confused", 2)
        ch_j "Oh, a foot person, eh?"
        $ JeanX.blushing = "_blush1"

    if not JeanX.action_counter["footjob"] and approval:
        if JeanX.Forced:
            $ JeanX.change_face("_sad",1)
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
        elif JeanX.love >= (JeanX.obedience + JeanX.inhibition - JeanX.IX):
            $ JeanX.change_face("_sexy",1)
            $ JeanX.brows = "_sad"
            $ JeanX.mouth = "_smile"
            ch_j "I suppose. . ."
        elif JeanX.obedience >= (JeanX.inhibition - JeanX.IX):
            $ JeanX.change_face("_normal",1)
            ch_j "If you want, [JeanX.player_petname]. . ."
        elif JeanX.addiction >= 50:
            $ JeanX.change_face("_manic", 1)
            ch_j "Okay. . ."
        else:
            $ JeanX.change_face("_lipbite",1)
            ch_j "Sure. . ."

    elif approval:
        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
            ch_j "That's it?"
        elif not JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "Um, I guess we're alone enough like this. . ."
        elif "footjob" in JeanX.daily_history:
            $ JeanX.change_face("_sexy", 1)
            ch_j "More of that, huh. . ."
            jump Jean_FJ_Prep







        elif JeanX.action_counter["footjob"] < 3:
            $ JeanX.change_face("_sexy", 1)
            $ JeanX.brows = "_confused"
            $ JeanX.mouth = "_kiss"
            ch_j "Hmm, it is kinda fun. . ."
        else:
            $ JeanX.change_face("_sexy", 1)
            $ JeanX.ArmPose = 2
            $ Line = renpy.random.choice(["You want me to use my feet?",                 
                "So you'd like another footjob?",                 
                "A little. . . [she rubs her foot along your leg]?", 
                "A little foot rub?"])
            ch_j "[Line]"
        $ Line = 0

    if approval >= 2:
        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("obedience", 90, 1)
            $ JeanX.change_stat("inhibition", 60, 1)
            ch_j "Ok, sure."
        elif "no_foot" in JeanX.daily_history:
            ch_j "Fine."
        else:
            $ JeanX.change_face("_sexy", 1)
            $ JeanX.change_stat("love", 90, 1)
            $ JeanX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Sure, I guess.",                 
                "OK.",                 
                "Fine, lemme see it.", 
                "I guess I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Heh, ok, ok."])
            ch_j "[Line]"
            $ Line = 0
        $ JeanX.change_stat("obedience", 20, 1)
        $ JeanX.change_stat("obedience", 60, 1)
        $ JeanX.change_stat("inhibition", 70, 2)
        jump Jean_FJ_Prep
    else:

        $ JeanX.change_face("_angry")
        if "no_foot" in JeanX.recent_history:
            ch_j "Don't make me repeat myself again, [JeanX.player_petname]."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history and "no_foot" in JeanX.daily_history:
            ch_j "I told you I wasn't comfortable in public. . ."
        elif "no_foot" in JeanX.daily_history:
            ch_j "I told you \"no,\" [JeanX.player_petname]."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "I said not in public!"
        elif not JeanX.action_counter["footjob"]:
            $ JeanX.change_face("_bemused")
            ch_j "Well. . ."
        else:
            $ JeanX.change_face("_bemused")
            ch_j "Not now, ok?"
        menu:
            extend ""
            "Sorry, never mind." if "no_foot" in JeanX.daily_history:
                $ JeanX.change_face("_bemused")
                ch_j "Sure, it's fine."
                return
            "Maybe later?" if "no_foot" not in JeanX.daily_history:
                $ JeanX.change_face("_sexy")
                ch_j "Well. . ."
                ch_j "Maybe."
                $ JeanX.change_stat("love", 80, 2)
                $ JeanX.change_stat("inhibition", 70, 2)
                if JeanX.Taboo:
                    $ JeanX.recent_history.append("no_taboo")
                    $ JeanX.daily_history.append("no_taboo")
                $ JeanX.recent_history.append("no_foot")
                $ JeanX.daily_history.append("no_foot")
                return
            "I'd really appreciate it. . .":
                if approval:
                    $ JeanX.change_face("_sexy")
                    $ JeanX.change_stat("obedience", 90, 2)
                    $ JeanX.change_stat("obedience", 50, 2)
                    $ JeanX.change_stat("inhibition", 70, 3)
                    $ JeanX.change_stat("inhibition", 40, 2)
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
            "Come on, get to work.":

                $ approval = approval_check(JeanX, 400, "OI", TabM = 3)
                if approval > 1 or (approval and JeanX.Forced):
                    $ JeanX.change_face("_sad")
                    $ JeanX.change_stat("love", 70, -5, 1)
                    $ JeanX.change_stat("love", 200, -2)
                    ch_j "Fine."
                    $ JeanX.change_stat("obedience", 50, 4)
                    $ JeanX.change_stat("inhibition", 80, 1)
                    $ JeanX.change_stat("inhibition", 60, 3)
                    $ JeanX.Forced = 1
                    jump Jean_FJ_Prep
                else:
                    $ JeanX.change_stat("love", 200, -15)
                    $ JeanX.recent_history.append("_angry")
                    $ JeanX.daily_history.append("_angry")


    $ JeanX.ArmPose = 1
    if "no_foot" in JeanX.daily_history:
        $ JeanX.change_face("_angry", 1)
        ch_j "I'm not telling you again."
        $ JeanX.recent_history.append("_angry")
        $ JeanX.daily_history.append("_angry")
    elif JeanX.Forced:
        $ JeanX.change_face("_angry", 1)
        ch_j "Don't push it. . ."
        $ JeanX.change_stat("lust", 200, 5)
        if JeanX.love > 300:
            $ JeanX.change_stat("love", 70, -2)
        $ JeanX.change_stat("obedience", 50, -2)
        $ JeanX.recent_history.append("_angry")
        $ JeanX.daily_history.append("_angry")
    elif JeanX.Taboo:
        $ JeanX.change_face("_angry", 1)
        $ JeanX.daily_history.append("no_taboo")
        ch_j "This is too public."
        $ JeanX.change_stat("lust", 200, 5)
        $ JeanX.change_stat("obedience", 50, -3)
    elif JeanX.action_counter["footjob"]:
        $ JeanX.change_face("_sad")
        ch_j "Not right now."
    else:
        $ JeanX.change_face("_normal", 1)
        ch_j "I'd rather not."
    $ JeanX.recent_history.append("no_foot")
    $ JeanX.daily_history.append("no_foot")
    $ approval_bonus = 0
    return


label Jean_FJ_Prep:
    if offhand_action == "footjob":
        return

    if JeanX.Taboo:
        $ JeanX.change_stat("inhibition", 90, int(Taboo/10))
        $ JeanX.change_stat("lust", 50, int(Taboo/5))

    $ JeanX.change_face("_sexy")
    if JeanX.Forced:
        $ JeanX.change_face("_sad")
    elif not JeanX.action_counter["footjob"]:
        $ JeanX.brows = "_confused"
        $ JeanX.eyes = "_sexy"
        $ JeanX.mouth = "_smile"

    call Seen_First_Peen (JeanX, Partner)

    if not JeanX.action_counter["footjob"]:
        if JeanX.Forced:
            $ JeanX.change_stat("love", 90, -20)
            $ JeanX.change_stat("obedience", 70, 25)
            $ JeanX.change_stat("inhibition", 80, 30)
        else:
            $ JeanX.change_stat("love", 90, 5)
            $ JeanX.change_stat("obedience", 70, 20)
            $ JeanX.change_stat("inhibition", 80, 20)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if JeanX.Taboo:
        $ JeanX.drain_word("no_taboo")
    $ JeanX.drain_word("no_foot")
    $ JeanX.recent_history.append("footjob")
    $ JeanX.daily_history.append("footjob")

label Jean_FJ_Cycle:
    while Round > 0:
        call shift_focus (JeanX)
        call Jean_Sex_Launch ("footjob")
        $ JeanX.lust_face()

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
                "Other options":

                    menu:
                        "Offhand action":
                            if JeanX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ JeanX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (JeanX, "tired")
                        "Shift primary action":

                            if JeanX.remaining_actions and multi_action:
                                menu:
                                    "How about a blowjob?":
                                        if JeanX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Jean_FJ_After
                                            call Jean_Blowjob
                                        else:
                                            call Sex_Basic_Dialog (JeanX, "tired")
                                    "How about a handjob?":
                                        if JeanX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Jean_FJ_After
                                            call Jean_Handjob
                                        else:
                                            call Sex_Basic_Dialog (JeanX, "tired")
                                    "How about a titjob?":

                                        if JeanX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Jean_FJ_After
                                            call Jean_Titjob
                                        else:
                                            call Sex_Basic_Dialog (JeanX, "tired")
                                    "Never Mind":



                                        jump Jean_FJ_Cycle
                            else:
                                call Sex_Basic_Dialog (JeanX, "tired")

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [JeanX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (JeanX)
                                "Ask [JeanX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (JeanX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (JeanX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Jean_FJ_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jean_FJ_Cycle
                                "Never mind":
                                    jump Jean_FJ_Cycle
                        "undress [JeanX.name]":
                            call Girl_Undress (JeanX)
                        "Clean up [JeanX.name] (locked)" if not JeanX.spunk:
                            pass
                        "Clean up [JeanX.name]" if JeanX.spunk:
                            call Girl_Cleanup (JeanX, "ask")
                        "Never mind":
                            jump Jean_FJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jean_Sex_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jean_FJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jean_Sex_Reset
                    $ Line = 0
                    jump Jean_FJ_After


        call shift_focus (JeanX)
        call Sex_Dialog (JeanX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or JeanX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (JeanX)
                if "_angry" in JeanX.recent_history:
                    call Jean_Sex_Reset
                    return
                $ JeanX.change_stat("lust", 200, 5)
                if 100 > JeanX.lust >= 70 and JeanX.session_orgasms < 2:
                    $ JeanX.recent_history.append("unsatisfied")
                    $ JeanX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jean_FJ_After
                $ Line = "came"

            if JeanX.lust >= 100:

                call Girl_Cumming (JeanX)
                if action_context == "shift" or "_angry" in JeanX.recent_history:
                    jump Jean_FJ_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in JeanX.recent_history:
                    "[JeanX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Jean_FJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if counter == 20:
            $ JeanX.brows = "_angry"
            menu:
                ch_j "Hmm, my feet are cramping up here. . ."
                "How about a BJ?" if JeanX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Jean_FJ_After
                    call Jean_Blowjob
                "How about a Handy?" if JeanX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Jean_FJ_After
                    call Jean_Handjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    $ counter += 1
                    "[Line]"
                    jump Jean_FJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Jean_Sex_Reset
                    $ action_context = "shift"
                    jump Jean_FJ_After
                "No, get back down there.":
                    if approval_check(JeanX, 1200) or approval_check(JeanX, 500, "O"):
                        $ JeanX.change_stat("love", 200, -5)
                        $ JeanX.change_stat("obedience", 50, 3)
                        $ JeanX.change_stat("obedience", 80, 2)
                        "She grumbles but gets back to work."
                    else:
                        $ JeanX.change_face("_angry", 1)
                        "She scowls at you and pulls back."
                        ch_j "Not interested."
                        $ JeanX.change_stat("love", 50, -3, 1)
                        $ JeanX.change_stat("love", 80, -4, 1)
                        $ JeanX.change_stat("obedience", 30, -1, 1)
                        $ JeanX.change_stat("obedience", 50, -1, 1)
                        $ JeanX.recent_history.append("_angry")
                        $ JeanX.daily_history.append("_angry")
                        jump Jean_FJ_After
        elif counter == 10 and JeanX.SEXP <= 100 and not approval_check(JeanX, 1200, "LO"):
            $ JeanX.brows = "_confused"
            ch_j "Ok, seriously, let's try something different."


        call Escalation (JeanX)

        if Round == 10:
            call Sex_Basic_Dialog (JeanX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JeanX, 5)


    $ JeanX.change_face("_bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JeanX, "done")

label Jean_FJ_After:
    $ JeanX.change_face("_sexy")

    $ JeanX.action_counter["footjob"] += 1
    $ JeanX.remaining_actions -=1
    $ JeanX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ JeanX.addiction_rate += 1
    $ JeanX.change_stat("lust", 90, 5)

    call Partner_Like (JeanX, 1)

    if "Jeanpedi" in Achievements:
        pass
    elif JeanX.action_counter["footjob"] >= 10:
        $ JeanX.change_face("_smile", 1)
        ch_j "Hmm, this is kinda fun. . ."
        $ Achievements.append("Jeanpedi")
        $ JeanX.SEXP += 5
    elif JeanX.action_counter["footjob"] == 1:
        $ JeanX.SEXP += 10
        if JeanX.love >= 500:
            $ JeanX.mouth = "_smile"
            ch_j "Did you enjoy that? . ."
        elif Player.focus <= 20:
            $ JeanX.mouth = "_sad"
            ch_j "Did that do it for you?"
    elif JeanX.action_counter["footjob"] == 5:
        ch_j "I'm getting used to this. . ."

    $ approval_bonus = 0
    if action_context == "shift":
        ch_j "Ok, so what did you have in mind?"
    else:
        call Jean_Sex_Reset
    call checkout
    return




label Psychic_Sex(Girl=0, Act=0):
    if Girl.addiction >= 50 and "ultimatum" in Girl.recent_history:

        return
    elif "psysex" in Girl.history:

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
            $ Girl.change_stat("love", 80, 2)
            $ Girl.change_stat("inhibition", 70, 2)
            ch_j "Fantastic. . ."
            $ action_context = "psy"
            jump Jean_PJ_Prep
        "What do you mean by that?" if "psysex" not in Girl.history and "ask" not in Player.recent_history:
            ch_j "Well, you know, I can \"touch\" things with my mind. . ."
            $ Girl.change_stat("inhibition", 70, 2)
            ch_j "All sorts of things. . ."
            ch_j "I could make you feel really good that way. . ."
            $ Player.recent_history.append("ask")
            jump PS_Menu
        "No, I'd like you to be more \"hands on.\"":
            $ Girl.change_stat("obedience", 90, 2)
            if approval < 2:
                $ Girl.change_face("_sad")
                $ Girl.change_stat("love", 80, -2)
                ch_j "Well!"
                ch_j ". . ."
                $ Girl.change_face("_normal")

            return
    return

label Jean_PJ_Prep:
    if JeanX.Taboo:
        $ JeanX.change_stat("inhibition", 90, int(Taboo/10))
        $ JeanX.change_stat("lust", 50, int(Taboo/5))

    $ JeanX.change_face("_sexy")
    if JeanX.Forced:
        $ JeanX.change_face("_sad")

    call Seen_First_Peen (JeanX, Partner, React=action_context)
    call Jean_PJ_Launch

    if action_context == JeanX:

        $ action_context = 0
        if offhand_action == "jackin":
            "An invisible pressure brushes your hand aside and starts stroking your cock."
        else:
            "[JeanX.name] gives you a mischevious smile, and a gentle pressure starts to fondle your cock."
        menu:
            "What do you do?"
            "Nothing.":
                $ JeanX.change_stat("inhibition", 70, 3)
                $ JeanX.change_stat("inhibition", 30, 2)
                "[JeanX.name] continues her actions."
            "Praise her.":
                $ JeanX.change_face("_sexy", 1)
                $ JeanX.change_stat("inhibition", 70, 3)
                ch_p "Oooh, that's good, [JeanX.petname]."
                $ JeanX.nameCheck()
                "[JeanX.name] continues her actions."
                $ JeanX.change_stat("love", 80, 1)
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ JeanX.change_face("_surprised")
                $ JeanX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that for now, [JeanX.petname]."
                $ JeanX.nameCheck()
                "[JeanX.name] puts it down."
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("obedience", 50, 1)
                $ JeanX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ JeanX.add_word(1,"refused","refused")
                return

    if "psysex" not in JeanX.history:
        if JeanX.Forced:
            $ JeanX.change_stat("love", 90, -10)
            $ JeanX.change_stat("obedience", 70, 15)
            $ JeanX.change_stat("inhibition", 80, 20)
        else:
            $ JeanX.change_stat("love", 90, 5)
            $ JeanX.change_stat("obedience", 70, 15)
            $ JeanX.change_stat("inhibition", 80, 15)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    $ JeanX.recent_history.append("psysex")
    $ JeanX.daily_history.append("psysex")

label Jean_PJ_Cycle:
    $ primary_action = "psy"
    while Round > 0:
        call shift_focus (JeanX)
        call Jean_PJ_Launch
        $ JeanX.lust_face()

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
                "View":
                    call ViewShift (JeanX, "menu")
                    jump Jean_PJ_Cycle
                "Change Construct":
                    menu:
                        "What do you want to feel?"
                        "Hand":
                            if approval_check(JeanX, 1000):
                                $ Psychic = "handjob"
                            else:
                                ch_j "I'd rather not."
                        "Mouth":
                            if approval_check(JeanX, 1100):
                                $ Psychic = "mouth"
                            else:
                                ch_j "Uh-uh."
                        "Tits":
                            if approval_check(JeanX, 1000):
                                $ Psychic = "tits"
                            else:
                                ch_j "I'd rather not."
                        "Pussy":
                            if approval_check(JeanX, 1200):
                                $ Psychic = "pussy"
                            else:
                                ch_j "Um. . . no."
                        "Anal":
                            if approval_check(JeanX, 1300):
                                $ Psychic = "anal"
                            else:
                                ch_j "You wish."
                "Other options":
                    menu:
                        "I also want to fondle her breasts." if offhand_action != "fondle_breasts":
                            if JeanX.remaining_actions and multi_action:
                                $ offhand_action = "fondle_breasts"
                                "You start to fondle her breasts."
                                $ JeanX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (JeanX, "tired")
                        "Shift primary action":

                            if JeanX.remaining_actions and multi_action:
                                menu:
                                    "Never Mind":















                                        jump Jean_PJ_Cycle
                            else:
                                call Sex_Basic_Dialog (JeanX, "tired")

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [JeanX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (JeanX)
                                "Ask [JeanX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (JeanX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (JeanX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Jean_PJ_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jean_PJ_Cycle
                                "Never mind":
                                    jump Jean_PJ_Cycle
                        "undress [JeanX.name]":
                            call Girl_Undress (JeanX)
                        "Clean up [JeanX.name] (locked)" if not JeanX.spunk:
                            pass
                        "Clean up [JeanX.name]" if JeanX.spunk:
                            call Girl_Cleanup (JeanX, "ask")
                        "Never mind":
                            jump Jean_PJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jean_PJ_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jean_PJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jean_PJ_Reset
                    $ Line = 0
                    jump Jean_PJ_After


        call shift_focus (JeanX)
        call Sex_Dialog (JeanX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or JeanX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (JeanX)
                if "_angry" in JeanX.recent_history:
                    call Jean_PJ_Reset
                    return
                $ JeanX.change_stat("lust", 200, 5)
                if 100 > JeanX.lust >= 70 and JeanX.session_orgasms < 2 and JeanX.SEXP >= 20:
                    $ JeanX.recent_history.append("unsatisfied")
                    $ JeanX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jean_PJ_After
                $ Line = "came"

            if JeanX.lust >= 100:

                call Girl_Cumming (JeanX)
                if action_context == "shift" or "_angry" in JeanX.recent_history:
                    jump Jean_PJ_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in JeanX.recent_history:
                    "[JeanX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Jean_PJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if counter == 20:
            $ JeanX.brows = "_angry"
            menu:
                ch_j "Ok, I'm bored now. Can we try something else?"




                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    jump Jean_PJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Jean_PJ_Reset
                    $ action_context = "shift"
                    jump Jean_PJ_After
                "No, get back down there.":
                    if approval_check(JeanX, 1200) or approval_check(JeanX, 500, "O"):
                        $ JeanX.change_stat("love", 200, -5)
                        $ JeanX.change_stat("obedience", 50, 3)
                        $ JeanX.change_stat("obedience", 80, 2)
                        "She grumbles but gets back to work."
                    else:
                        $ JeanX.change_face("_angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        ch_j "I have better things to do with my time."
                        $ JeanX.change_stat("love", 50, -3, 1)
                        $ JeanX.change_stat("love", 80, -4, 1)
                        $ JeanX.change_stat("obedience", 30, -1, 1)
                        $ JeanX.change_stat("obedience", 50, -1, 1)
                        $ JeanX.recent_history.append("_angry")
                        $ JeanX.daily_history.append("_angry")
                        jump Jean_PJ_After
        elif counter == 10 and JeanX.SEXP <= 100 and not approval_check(JeanX, 1200, "LO"):
            $ JeanX.brows = "_confused"
            ch_j "Nice, right?"


        call Escalation (JeanX)

        if Round == 10:
            call Sex_Basic_Dialog (JeanX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JeanX, 5)


    $ JeanX.change_face("_bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JeanX, "done")

label Jean_PJ_After:
    $ JeanX.change_face("_sexy")

    $ JeanX.remaining_actions -=1

    $ JeanX.change_stat("lust", 90, 5)

    call Partner_Like (JeanX, 1)

    if "psysex" not in JeanX.history:
        ch_j "Pretty great, right?"
    $ JeanX.add_word(1,0,0,0,"psysex")

    $ approval_bonus = 0
    if action_context == "shift":
        ch_j "Ok, so what did you have in mind?"
    call Jean_PJ_Reset
    call checkout
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
