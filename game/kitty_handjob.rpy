
label Kitty_Handjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (KittyX)
    if KittyX.action_counter["handjob"] >= 7:
        $ approval_bonus += 10
    elif KittyX.action_counter["handjob"] >= 3:
        $ approval_bonus += 7
    elif KittyX.action_counter["handjob"]:
        $ approval_bonus += 3

    if KittyX.addiction >= 75 and KittyX.event_counter["swallowed"] >=3:
        $ approval_bonus += 15
    if KittyX.addiction >= 75:
        $ approval_bonus += 5

    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in KittyX.Traits:
        $ approval_bonus += (3*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in KittyX.Traits:
        $ approval_bonus -= 40
    if KittyX.event_counter["forced"] and not KittyX.Forced:
        $ approval_bonus -= 5*KittyX.event_counter["forced"]

    if Taboo and "no_taboo" in KittyX.daily_history:
        $ approval_bonus -= 10

    if "no_handjob" in KittyX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_handjob" in KittyX.recent_history else 0

    $ Approval = ApprovalCheck(KittyX, 1100, TabM = 3)

    if not KittyX.action_counter["handjob"] and "no_handjob" not in KittyX.recent_history:
        $ KittyX.change_face("confused", 2)
        ch_k "So you want a handy then?"
        $ KittyX.blushing = 1

    if not KittyX.action_counter["handjob"] and Approval:
        if KittyX.Forced:
            $ KittyX.change_face("sad",1)
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
        elif KittyX.love >= (KittyX.obedience + KittyX.inhibition):
            $ KittyX.change_face("sexy",1)
            $ KittyX.brows = "sad"
            $ KittyX.mouth = "smile"
            ch_k "I guess it could be interesting. . ."
        elif KittyX.obedience >= KittyX.inhibition:
            $ KittyX.change_face("normal",1)
            ch_k "If you want, [KittyX.player_petname]. . ."
        elif KittyX.addiction >= 50:
            $ KittyX.change_face("manic", 1)
            ch_k "I kind of {i}need{/i} to. . ."
        else:
            $ KittyX.change_face("lipbite",1)
            ch_k "I guess. . ."

    elif Approval:
        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
            ch_k "That's it, right?"
        elif not Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "Well, I guess if it's here. . ."
        elif "handjob" in KittyX.recent_history:
            $ KittyX.change_face("sexy", 1)
            ch_k "You're giving me carpal tunnel. . ."
            jump Kitty_HJ_Prep
        elif "handjob" in KittyX.daily_history:
            $ KittyX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Another one?",   
                "You're going to give me calluses.", 
                "Didn't get enough earlier?",
                "My hand's kinda sore from earlier.",
                "My hand's kinda sore from earlier."])
            ch_k "[Line]"
        elif KittyX.action_counter["handjob"] < 3:
            $ KittyX.change_face("sexy", 1)
            $ KittyX.brows = "confused"
            $ KittyX.mouth = "kiss"
            ch_k "Hmm, magic fingers. . ."
        else:
            $ KittyX.change_face("sexy", 1)
            $ KittyX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this?",                 
                "So you'd like another handy?",                 
                "A little. . . [fist pumping hand gestures]?", 
                "A little TLC?"])
            ch_k "[Line]"
        $ Line = 0

    if Approval >= 2:
        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("obedience", 90, 1)
            $ KittyX.change_stat("inhibition", 60, 1)
            ch_k "Ok, fine."
        elif "no_handjob" in KittyX.daily_history:
            ch_k "OK, geeze!"
        else:
            $ KittyX.change_face("sexy", 1)
            $ KittyX.change_stat("love", 90, 1)
            $ KittyX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Sure, I guess.",                 
                "Ooooookay.",                 
                "Cool, lemme see it.", 
                "I guess I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Heh, ok, ok."])
            ch_k "[Line]"
            $ Line = 0
        $ KittyX.change_stat("obedience", 20, 1)
        $ KittyX.change_stat("obedience", 60, 1)
        $ KittyX.change_stat("inhibition", 70, 2)
        jump Kitty_HJ_Prep
    else:

        $ KittyX.change_face("angry")
        if "no_handjob" in KittyX.recent_history:
            ch_k "You don't[KittyX.like]listen do you, [KittyX.player_petname]."
        elif Taboo and "no_taboo" in KittyX.daily_history and "no_handjob" in KittyX.daily_history:
            ch_k "I said not in public!"
        elif "no_handjob" in KittyX.daily_history:
            ch_k "I told you \"no,\" [KittyX.player_petname]."
        elif Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "I said not in public!"
        elif not KittyX.action_counter["handjob"]:
            $ KittyX.change_face("bemused")
            ch_k "I don't know, [KittyX.player_petname]. . ."
        else:
            $ KittyX.change_face("bemused")
            ch_k "Not now, ok?"
        menu:
            extend ""
            "Sorry, never mind." if "no_handjob" in KittyX.daily_history:
                $ KittyX.change_face("bemused")
                ch_k "Yeah."
                return
            "Maybe later?" if "no_handjob" not in KittyX.daily_history:
                $ KittyX.change_face("sexy")
                ch_k ". . ."
                ch_k "Maybe."
                $ KittyX.change_stat("love", 80, 2)
                $ KittyX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ KittyX.recent_history.append("no_taboo")
                    $ KittyX.daily_history.append("no_taboo")
                $ KittyX.recent_history.append("no_handjob")
                $ KittyX.daily_history.append("no_handjob")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ KittyX.change_face("sexy")
                    $ KittyX.change_stat("obedience", 90, 2)
                    $ KittyX.change_stat("obedience", 50, 2)
                    $ KittyX.change_stat("inhibition", 70, 3)
                    $ KittyX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Sure, I guess.",                 
                            "Ooooookay.",                 
                            "Cool, lemme see it.", 
                            "I guess I could. . .",
                            "Ok. . . [She gestures for you to come over].",
                            "Heh, ok, ok."])
                    ch_k "[Line]"
                    $ Line = 0
                    jump Kitty_HJ_Prep
                else:
                    pass
            "Come on, get to work.":

                $ Approval = ApprovalCheck(KittyX, 350, "OI", TabM = 3)
                if Approval > 1 or (Approval and KittyX.Forced):
                    $ KittyX.change_face("sad")
                    $ KittyX.change_stat("love", 70, -5, 1)
                    $ KittyX.change_stat("love", 200, -2)
                    ch_k "Ok, fine."
                    $ KittyX.change_stat("obedience", 50, 4)
                    $ KittyX.change_stat("inhibition", 80, 1)
                    $ KittyX.change_stat("inhibition", 60, 3)
                    $ KittyX.Forced = 1
                    jump Kitty_HJ_Prep
                else:
                    $ KittyX.change_stat("love", 200, -15)
                    $ KittyX.recent_history.append("angry")
                    $ KittyX.daily_history.append("angry")


    $ KittyX.ArmPose = 1
    if "no_handjob" in KittyX.daily_history:
        $ KittyX.change_face("angry", 1)
        ch_k "I'm not telling you again."
        $ KittyX.recent_history.append("angry")
        $ KittyX.daily_history.append("angry")
    elif KittyX.Forced:
        $ KittyX.change_face("angry", 1)
        ch_k "Not even if you had a ten foot pole."
        $ KittyX.change_face("surprised", 2)
        ch_k "I mean. . ."
        $ KittyX.change_face("angry", 1)
        ch_k "You know what I mean!"
        $ KittyX.change_stat("lust", 200, 5)
        if KittyX.love > 300:
            $ KittyX.change_stat("love", 70, -2)
        $ KittyX.change_stat("obedience", 50, -2)
        $ KittyX.recent_history.append("angry")
        $ KittyX.daily_history.append("angry")
    elif Taboo:
        $ KittyX.change_face("angry", 1)
        $ KittyX.daily_history.append("no_taboo")
        ch_k "Not here, not anywhere near here."
        $ KittyX.change_stat("lust", 200, 5)
        $ KittyX.change_stat("obedience", 50, -3)
    elif KittyX.action_counter["handjob"]:
        $ KittyX.change_face("sad")
        ch_k "I'm not feeling it today. . ."
    else:
        $ KittyX.change_face("normal", 1)
        ch_k "I don't wanna touch that."
    $ KittyX.recent_history.append("no_handjob")
    $ KittyX.daily_history.append("no_handjob")
    $ approval_bonus = 0
    return


label Kitty_HJ_Prep:
    if offhand_action == "handjob":
        return

    if Taboo:
        $ KittyX.inhibition += int(Taboo/10)
        $ KittyX.lust += int(Taboo/5)

    $ KittyX.change_face("sexy")
    if KittyX.Forced:
        $ KittyX.change_face("sad")
    elif not KittyX.action_counter["handjob"]:
        $ KittyX.brows = "confused"
        $ KittyX.eyes = "sexy"
        $ KittyX.mouth = "smile"

    call Seen_First_Peen (KittyX, Partner, React=action_context)
    call Kitty_HJ_Launch ("L")

    if action_context == KittyX:

        $ action_context = 0
        if offhand_action == "jackin":
            "[KittyX.name] brushes your hand aside and starts stroking your cock."
        else:
            "[KittyX.name] gives you a mischevious smile, and starts to fondle your cock."
        menu:
            "What do you do?"
            "Nothing.":
                $ KittyX.change_stat("inhibition", 70, 3)
                $ KittyX.change_stat("inhibition", 30, 2)
                "[KittyX.name] continues her actions."
            "Praise her.":
                $ KittyX.change_face("sexy", 1)
                $ KittyX.change_stat("inhibition", 70, 3)
                ch_p "Oooh, that's good, [KittyX.petname]."
                $ KittyX.nameCheck()
                "[KittyX.name] continues her actions."
                $ KittyX.change_stat("love", 80, 1)
                $ KittyX.change_stat("obedience", 90, 1)
                $ KittyX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ KittyX.change_face("surprised")
                $ KittyX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that for now, [KittyX.petname]."
                $ KittyX.nameCheck()
                "[KittyX.name] puts it down."
                $ KittyX.change_stat("obedience", 90, 1)
                $ KittyX.change_stat("obedience", 50, 1)
                $ KittyX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ KittyX.AddWord(1,"refused","refused")
                return

    if not KittyX.action_counter["handjob"]:
        if KittyX.Forced:
            $ KittyX.change_stat("love", 90, -20)
            $ KittyX.change_stat("obedience", 70, 25)
            $ KittyX.change_stat("inhibition", 80, 30)
        else:
            $ KittyX.change_stat("love", 90, 5)
            $ KittyX.change_stat("obedience", 70, 20)
            $ KittyX.change_stat("inhibition", 80, 20)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ KittyX.DrainWord("no_taboo")
    $ KittyX.DrainWord("no_handjob")
    $ KittyX.recent_history.append("handjob")
    $ KittyX.daily_history.append("handjob")

label Kitty_HJ_Cycle:
    while Round > 0:
        call shift_focus (KittyX)
        call Kitty_HJ_Launch
        $ KittyX.lust_face()

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
                            if KittyX.remaining_actions and multi_action:
                                $ offhand_action = "fondle_breasts"
                                "You start to fondle her breasts."
                                $ KittyX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (KittyX, "tired")
                        "Shift primary action":

                            if KittyX.remaining_actions and multi_action:
                                menu:
                                    "How about a blowjob?":
                                        if KittyX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Kitty_HJ_After
                                            call Kitty_Blowjob
                                        else:
                                            ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."
                                    "Never Mind":








                                        jump Kitty_HJ_Cycle
                            else:
                                call Sex_Basic_Dialog (KittyX, "tired")

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [KittyX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (KittyX)
                                "Ask [KittyX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (KittyX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (KittyX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Kitty_HJ_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Kitty_HJ_Cycle
                                "Never mind":
                                    jump Kitty_HJ_Cycle
                        "Undress [KittyX.name]":
                            call Girl_Undress (KittyX)
                        "Clean up [KittyX.name] (locked)" if not KittyX.Spunk:
                            pass
                        "Clean up [KittyX.name]" if KittyX.Spunk:
                            call Girl_Cleanup (KittyX, "ask")
                        "Never mind":
                            jump Kitty_HJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Kitty_HJ_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Kitty_HJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Kitty_HJ_Reset
                    $ Line = 0
                    jump Kitty_HJ_After


        call shift_focus (KittyX)
        call Sex_Dialog (KittyX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or KittyX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (KittyX)
                if "angry" in KittyX.recent_history:
                    call Kitty_HJ_Reset
                    return
                $ KittyX.change_stat("lust", 200, 5)
                if 100 > KittyX.lust >= 70 and KittyX.session_orgasms < 2 and KittyX.SEXP >= 20:
                    $ KittyX.recent_history.append("unsatisfied")
                    $ KittyX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Kitty_HJ_After
                $ Line = "came"

            if KittyX.lust >= 100:

                call Girl_Cumming (KittyX)
                if action_context == "shift" or "angry" in KittyX.recent_history:
                    jump Kitty_HJ_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in KittyX.recent_history:
                    "[KittyX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Kitty_HJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if counter == 20:
            $ KittyX.brows = "angry"
            menu:
                ch_k "Ouch, hand cramp, can we[KittyX.like]take a break?"
                "How about a BJ?" if KittyX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Kitty_HJ_After
                    call Kitty_Blowjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    jump Kitty_HJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Kitty_HJ_Reset
                    $ action_context = "shift"
                    jump Kitty_HJ_After
                "No, get back down there.":
                    if ApprovalCheck(KittyX, 1200) or ApprovalCheck(KittyX, 500, "O"):
                        $ KittyX.change_stat("love", 200, -5)
                        $ KittyX.change_stat("obedience", 50, 3)
                        $ KittyX.change_stat("obedience", 80, 2)
                        "She grumbles but gets back to work."
                    else:
                        $ KittyX.change_face("angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        ch_k "Hey, I've got better things to do if you're[KittyX.like]going to be a dick about it."
                        $ KittyX.change_stat("love", 50, -3, 1)
                        $ KittyX.change_stat("love", 80, -4, 1)
                        $ KittyX.change_stat("obedience", 30, -1, 1)
                        $ KittyX.change_stat("obedience", 50, -1, 1)
                        $ KittyX.recent_history.append("angry")
                        $ KittyX.daily_history.append("angry")
                        jump Kitty_HJ_After
        elif counter == 10 and KittyX.SEXP <= 100 and not ApprovalCheck(KittyX, 1200, "LO"):
            $ KittyX.brows = "confused"
            ch_k "Can we[KittyX.Like]be done with this now? I'm getting sore."


        call Escalation (KittyX)

        if Round == 10:
            ch_k "It's kind of time to get moving."
        elif Round == 5:
            ch_k "For real[KittyX.like]time's up."


    $ KittyX.change_face("bemused", 0)
    $ Line = 0
    ch_k "Ok, we need to take a break."

label Kitty_HJ_After:
    $ KittyX.change_face("sexy")

    $ KittyX.action_counter["handjob"] += 1
    $ KittyX.remaining_actions -=1
    $ KittyX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ KittyX.addiction_rate += 1
    $ KittyX.change_stat("lust", 90, 5)

    call Partner_Like (KittyX, 1)

    if "Kitty Handi-Queen" in Achievements:
        pass
    elif KittyX.action_counter["handjob"] >= 10:
        $ KittyX.change_face("smile", 1)
        ch_k "I've kinda become[KittyX.like]a \"Handi-Queen\" or something."
        $ Achievements.append("Kitty Handi-Queen")
        $ KittyX.SEXP += 5
    elif KittyX.action_counter["handjob"] == 1:
        $ KittyX.SEXP += 10
        if KittyX.love >= 500:
            $ KittyX.mouth = "smile"
            ch_k "It was so warm to the touch. . ."
        elif Player.focus <= 20:
            $ KittyX.mouth = "sad"
            ch_k "Did that work out for you?"
    elif KittyX.action_counter["handjob"] == 5:
        ch_k "Let me know any time you need me to give you a hand."

    $ approval_bonus = 0
    if action_context == "shift":
        ch_k "Ok, so what were you thinking?"
    else:
        call Kitty_HJ_Reset
    call checkout
    return





label Kitty_Titjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (KittyX)
    if KittyX.action_counter["titjob"] >= 7:
        $ approval_bonus += 10
    elif KittyX.action_counter["titjob"] >= 3:
        $ approval_bonus += 7
    elif KittyX.action_counter["titjob"]:
        $ approval_bonus += 5

    if KittyX.addiction >= 75 and KittyX.event_counter["swallowed"] >=3:
        $ approval_bonus += 15
    elif KittyX.addiction >= 75:
        $ approval_bonus += 5

    if KittyX.SeenChest and ApprovalCheck(KittyX, 500):
        $ approval_bonus += 10
    if not KittyX.bra and not KittyX.top:
        $ approval_bonus += 10
    if KittyX.lust > 75:
        $ approval_bonus += 10
    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in KittyX.Traits:
        $ approval_bonus += (5*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in KittyX.Traits:
        $ approval_bonus -= 30
    if KittyX.event_counter["forced"] and not KittyX.Forced:
        $ approval_bonus -= 5*KittyX.event_counter["forced"]

    if Taboo and "no_taboo" in KittyX.daily_history:
        $ approval_bonus -= 10

    if "no_titjob" in KittyX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_titjob" in KittyX.recent_history else 0

    $ Approval = ApprovalCheck(KittyX, 1200, TabM = 5)

    if not KittyX.action_counter["titjob"] and "no_titjob" not in KittyX.recent_history:
        $ KittyX.change_face("surprised", 1)
        $ KittyX.mouth = "kiss"
        ch_k "You want to rub your cock against my. . . breasts?"

    if not KittyX.action_counter["titjob"] and Approval:
        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
        elif KittyX.love >= (KittyX.obedience + KittyX.inhibition):
            $ KittyX.change_face("sexy")
            $ KittyX.brows = "sad"
            $ KittyX.mouth = "smile"
            ch_k "It's nice that you even thought about it."
        elif KittyX.obedience >= KittyX.inhibition:
            $ KittyX.change_face("normal")
            ch_k "I mean. . ."
        elif KittyX.addiction >= 50:
            $ KittyX.change_face("manic", 1)
            ch_k "Hmmmm. . . ."
        else:
            $ KittyX.change_face("sad")
            $ KittyX.mouth = "smile"
            ch_k "Hadn't really considered that."
    elif Approval:
        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
            ch_k "This isn't going to become a habit, will it?"
        elif not Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "Ok, I guess this is private enough. . ."
        elif "titjob" in KittyX.recent_history:
            $ KittyX.change_face("sexy", 1)
            ch_k "Mmm, again?"
            jump Kitty_TJ_Prep
        elif "titjob" in KittyX.daily_history:
            $ KittyX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",   
                "You're going to make me sore.", 
                "Didn't get enough earlier?",
                "My tits are still kinda sore from earlier."])
            ch_k "[Line]"
        elif KittyX.action_counter["titjob"] < 3:
            $ KittyX.change_face("sexy", 1)
            $ KittyX.brows = "confused"
            $ KittyX.mouth = "kiss"
            ch_k "So you'd like another titjob?"
        else:
            $ KittyX.change_face("sexy", 1)
            $ KittyX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action [rubs her chest]?",                 
                "So you'd like another titjob?",                  
                "So you'd like another titjob?",                               
                "So you'd like another titjob?",                              
                "A little. . . puffpuff?", 
                "A little soft embrace?"])
            ch_k "[Line]"
        $ Line = 0

    if Approval >= 2:
        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("obedience", 90, 1)
            $ KittyX.change_stat("inhibition", 60, 1)
            ch_k "Well, could be worse. . ."
        elif "no_titjob" in KittyX.daily_history:
            ch_k "Hmm, I guess. . ."
        else:
            $ KittyX.change_face("sexy", 1)
            $ KittyX.change_stat("love", 90, 1)
            $ KittyX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, put it here.",                 
                "Well. . . ok.",                 
                "Yum.", 
                "Sure, whip it out.",
                "Fine. . . [She drools a bit into her cleavage].",
                "Heh, ok."])
            ch_k "[Line]"
            $ Line = 0
        $ KittyX.change_stat("obedience", 20, 1)
        $ KittyX.change_stat("obedience", 70, 1)
        $ KittyX.change_stat("inhibition", 80, 2)
        jump Kitty_TJ_Prep
    else:

        $ KittyX.change_face("angry")
        if "no_titjob" in KittyX.recent_history:
            ch_k "I {i}just{/i} told you \"no,\" [KittyX.player_petname]."
        elif Taboo and "no_taboo" in KittyX.daily_history and "no_titjob" in KittyX.daily_history:
            ch_k "This is just way too exposed!"
        elif "no_titjob" in KittyX.daily_history:
            ch_k "I already told you \"no,\" [KittyX.player_petname]."
        elif Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "This is just way too exposed!"
        elif not KittyX.action_counter["titjob"]:
            $ KittyX.change_face("bemused")
            ch_k "I'm not really up for that, [KittyX.player_petname]. . ."
        else:
            $ KittyX.change_face("bemused")
            ch_k "Not, right now [KittyX.player_petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_titjob" in KittyX.daily_history:
                $ KittyX.change_face("bemused")
                ch_k "Yeah, ok, [KittyX.player_petname]."
                return
            "Maybe later?" if "no_titjob" not in KittyX.daily_history:
                $ KittyX.change_face("sexy")
                ch_k "Maybe."
                $ KittyX.change_stat("love", 80, 2)
                $ KittyX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ KittyX.recent_history.append("no_taboo")
                    $ KittyX.daily_history.append("no_taboo")
                $ KittyX.recent_history.append("no_titjob")
                $ KittyX.daily_history.append("no_titjob")
                return
            "I think this could be fun for both of us. . .":
                if Approval:
                    $ KittyX.change_face("sexy")
                    $ KittyX.change_stat("obedience", 80, 2)
                    $ KittyX.change_stat("obedience", 40, 2)
                    $ KittyX.change_stat("inhibition", 70, 3)
                    $ KittyX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Well, ok, put it here.",                 
                        "Well. . . ok.",                 
                        "I guess.", 
                        "I guess, whip it out.",
                        "Fine. . . [She drools a bit into her cleavage].",
                        "Heh, ok."])
                    ch_k "[Line]"
                    $ Line = 0
                    jump Kitty_TJ_Prep
                else:
                    $ Approval = ApprovalCheck(KittyX, 1100, TabM = 3)
                    if Approval >= 2 and KittyX.action_counter["blowjob"]:
                        $ KittyX.change_stat("inhibition", 80, 1)
                        $ KittyX.change_stat("inhibition", 60, 3)
                        $ KittyX.change_face("confused", 1)
                        ch_k "Could I[KittyX.like]. . . blow you instead?"
                        menu:
                            ch_k "What do you say [[blowjob]?"
                            "Ok, get down there.":
                                $ KittyX.change_stat("love", 80, 2)
                                $ KittyX.change_stat("inhibition", 60, 1)
                                $ KittyX.change_stat("obedience", 50, 1)
                                jump Kitty_BJ_Prep
                            "Nah, it's all about dem titties.":
                                $ Line = "no_BJ"
                    if Approval and KittyX.action_counter["handjob"]:
                        $ KittyX.change_stat("inhibition", 80, 1)
                        $ KittyX.change_stat("inhibition", 60, 3)
                        $ KittyX.change_face("confused", 1)
                        ch_k "Maybe you'd[KittyX.like]settle for a handy?"
                        menu:
                            ch_k "What do you say?"
                            "Sure, that's fine.":
                                $ KittyX.change_stat("love", 80, 2)
                                $ KittyX.change_stat("inhibition", 60, 1)
                                $ KittyX.change_stat("obedience", 50, 1)
                                jump Kitty_HJ_Prep
                            "Seriously, titties." if Line == "no_BJ":
                                $ Line = 0
                            "Nah, it's all about dem titties." if Line != "no_BJ":
                                pass
                    $ KittyX.change_stat("love", 200, -2)
                    ch_k "Nah."
                    $ KittyX.change_stat("obedience", 70, 2)
            "Come on, let me fuck those titties, [KittyX.petname]":


                $ KittyX.nameCheck()
                $ Approval = ApprovalCheck(KittyX, 700, "OI", TabM = 4)
                if Approval > 1 or (Approval and KittyX.Forced):
                    $ KittyX.change_face("sad")
                    $ KittyX.change_stat("love", 70, -5, 1)
                    $ KittyX.change_stat("love", 200, -2)
                    ch_k "Ok, fine, whip it out."
                    $ KittyX.change_stat("obedience", 50, 4)
                    $ KittyX.change_stat("inhibition", 80, 1)
                    $ KittyX.change_stat("inhibition", 60, 3)
                    $ KittyX.Forced = 1
                    jump Kitty_TJ_Prep
                else:
                    $ KittyX.change_stat("love", 200, -15)
                    $ KittyX.recent_history.append("angry")
                    $ KittyX.daily_history.append("angry")


    if "no_titjob" in KittyX.daily_history:
        $ KittyX.change_face("angry", 1)
        ch_k "Look, I already told you no thanks, [KittyX.player_petname]."
        $ KittyX.recent_history.append("angry")
        $ KittyX.daily_history.append("angry")
    elif KittyX.Forced:
        $ KittyX.change_face("angry", 1)
        ch_k "No, that's just weird."
        $ KittyX.change_stat("lust", 200, 5)
        if KittyX.love > 300:
            $ KittyX.change_stat("love", 70, -2)
        $ KittyX.change_stat("obedience", 50, -2)
        $ KittyX.recent_history.append("angry")
        $ KittyX.daily_history.append("angry")
    elif Taboo:
        $ KittyX.change_face("angry", 1)
        $ KittyX.daily_history.append("no_taboo")
        ch_k "You really expect me to do that here? You realize how. . . exposed that would be?"
        $ KittyX.change_stat("lust", 200, 5)
        $ KittyX.change_stat("obedience", 50, -3)
    elif KittyX.action_counter["titjob"]:
        $ KittyX.change_face("sad")
        ch_k "I think I'll let you know when I want you touching these again."
    else:
        $ KittyX.change_face("normal", 1)
        ch_k "How about let's not, [KittyX.player_petname]."
    $ KittyX.recent_history.append("no_titjob")
    $ KittyX.daily_history.append("no_titjob")
    $ approval_bonus = 0
    return

label Kitty_TJ_Prep:

    if Taboo:
        $ KittyX.inhibition += int(Taboo/10)
        $ KittyX.lust += int(Taboo/5)


    $ KittyX.change_face("sexy")
    if KittyX.Forced:
        $ KittyX.change_face("sad")
    elif not KittyX.action_counter["titjob"]:
        $ KittyX.brows = "confused"
        $ KittyX.eyes = "sexy"
        $ KittyX.mouth = "smile"

    call Seen_First_Peen (KittyX, Partner, React=action_context)
    call Kitty_TJ_Launch ("L")

    if action_context == KittyX:

        $ action_context = 0
        call Kitty_TJ_Launch ("L")
        "[KittyX.name] slides down and presses your dick between her tits."
        menu:
            "What do you do?"
            "Nothing.":
                $ KittyX.change_stat("inhibition", 80, 3)
                $ KittyX.change_stat("inhibition", 40, 2)
                "[KittyX.name] starts to slide up and down."
            "Praise her.":
                $ KittyX.change_face("sexy", 1)
                $ KittyX.change_stat("inhibition", 80, 3)
                ch_p "Oh, that sounds like a good idea, [KittyX.petname]."
                $ KittyX.nameCheck()
                "[KittyX.name] continues her actions."
                $ KittyX.change_stat("love", 85, 1)
                $ KittyX.change_stat("obedience", 90, 1)
                $ KittyX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ KittyX.change_face("confused")
                $ KittyX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that for now, [KittyX.petname]."
                $ KittyX.nameCheck()
                "[KittyX.name] lets it drop out from between her breasts."
                $ KittyX.change_stat("obedience", 90, 1)
                $ KittyX.change_stat("obedience", 50, 3)
                $ Player.recent_history.append("nope")
                $ KittyX.AddWord(1,"refused","refused")
                return
    if not KittyX.action_counter["titjob"]:
        if KittyX.Forced:
            $ KittyX.change_stat("love", 90, -25)
            $ KittyX.change_stat("obedience", 70, 30)
            $ KittyX.change_stat("inhibition", 80, 35)
        else:
            $ KittyX.change_stat("love", 90, 5)
            $ KittyX.change_stat("obedience", 70, 25)
            $ KittyX.change_stat("inhibition", 80, 30)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ KittyX.DrainWord("no_taboo")
    $ KittyX.DrainWord("no_titjob")
    $ KittyX.recent_history.append("titjob")
    $ KittyX.daily_history.append("titjob")

label Kitty_TJ_Cycle:
    while Round > 0:
        call shift_focus (KittyX)
        call Kitty_TJ_Launch
        $ KittyX.lust_face()

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
                            if KittyX.remaining_actions and multi_action:
                                $ offhand_action = "fondle_breasts"
                                "You start to fondle her breasts."
                                $ KittyX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (KittyX, "tired")
                        "Shift primary action":

                            if KittyX.remaining_actions and multi_action:
                                menu:
                                    "How about a blowjob?":
                                        if KittyX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Kitty_TJ_After
                                            call Kitty_Blowjob
                                        else:
                                            ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."
                                    "How about a handy?":

                                        if KittyX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Kitty_BJ_After
                                            call Kitty_Handjob
                                        else:
                                            ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."
                                    "Never Mind":
                                        jump Kitty_TJ_Cycle
                            else:
                                call Sex_Basic_Dialog (KittyX, "tired")

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [KittyX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (KittyX)
                                "Ask [KittyX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (KittyX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (KittyX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Kitty_TJ_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Kitty_TJ_Cycle
                                "Never mind":
                                    jump Kitty_TJ_Cycle
                        "Undress [KittyX.name]":
                            call Girl_Undress (KittyX)
                        "Clean up [KittyX.name] (locked)" if not KittyX.Spunk:
                            pass
                        "Clean up [KittyX.name]" if KittyX.Spunk:
                            call Girl_Cleanup (KittyX, "ask")
                        "Never mind":
                            jump Kitty_TJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Kitty_TJ_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Kitty_TJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Kitty_TJ_Reset
                    $ Line = 0
                    jump Kitty_TJ_After


        call shift_focus (KittyX)
        call Sex_Dialog (KittyX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or KittyX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (KittyX)
                if "angry" in KittyX.recent_history:
                    call Kitty_TJ_Reset
                    return
                $ KittyX.change_stat("lust", 200, 5)
                if 100 > KittyX.lust >= 70 and KittyX.session_orgasms < 2 and KittyX.SEXP >= 20:
                    $ KittyX.recent_history.append("unsatisfied")
                    $ KittyX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Kitty_TJ_After
                $ Line = "came"

            if KittyX.lust >= 100:

                call Girl_Cumming (KittyX)
                if action_context == "shift" or "angry" in KittyX.recent_history:
                    jump Kitty_TJ_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in KittyX.recent_history:
                    "[KittyX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Kitty_TJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if KittyX.SEXP >= 100 or ApprovalCheck(KittyX, 1200, "LO"):
            pass
        elif counter == (5 + KittyX.action_counter["titjob"]):
            $ KittyX.brows = "confused"
            ch_k "Are you getting close here? I'm getting as little sore."
        if counter == (10 + KittyX.action_counter["titjob"]):
            $ KittyX.brows = "angry"
            menu:
                ch_k "I'm getting rug-burn here [KittyX.player_petname]. Can we do something else?"
                "How about a BJ?" if KittyX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Kitty_TJ_After
                    call Kitty_Blowjob
                    return
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    jump Kitty_TJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Kitty_TJ_Reset
                    $ action_context = "shift"
                    jump Kitty_TJ_After
                "No, get back down there.":
                    if ApprovalCheck(KittyX, 1200) or ApprovalCheck(KittyX, 500, "O"):
                        $ KittyX.change_stat("love", 200, -5)
                        $ KittyX.change_stat("obedience", 50, 3)
                        $ KittyX.change_stat("obedience", 80, 2)
                        "She grumbles but gets back to work."
                    else:
                        $ KittyX.change_face("angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        ch_k "Well fuck you then."
                        $ KittyX.change_stat("love", 50, -3, 1)
                        $ KittyX.change_stat("love", 80, -4, 1)
                        $ KittyX.change_stat("obedience", 30, -1, 1)
                        $ KittyX.change_stat("obedience", 50, -1, 1)
                        $ KittyX.recent_history.append("angry")
                        $ KittyX.daily_history.append("angry")
                        jump Kitty_TJ_After


        call Escalation (KittyX)

        if Round == 10:
            ch_k "It's kinda time to get moving."
        elif Round == 5:
            ch_k "For real[KittyX.like]time's up."


    $ KittyX.change_face("bemused", 0)
    $ Line = 0
    ch_k "Ok, we need to take a break."

label Kitty_TJ_After:
    $ KittyX.change_face("sexy")

    $ KittyX.action_counter["titjob"] += 1
    $ KittyX.remaining_actions -=1
    $ KittyX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ KittyX.addiction_rate += 1

    call Partner_Like (KittyX, 4)

    if KittyX.action_counter["titjob"] > 5:
        pass
    elif KittyX.action_counter["titjob"] == 1:
        $ KittyX.SEXP += 12
        if KittyX.love >= 500:
            $ KittyX.mouth = "smile"
            ch_k "That was kinda fun."
        elif Player.focus <= 20:
            $ KittyX.mouth = "sad"
            ch_k "Well I hope you got something out of that."
    elif KittyX.action_counter["titjob"] == 5:
        ch_k "Huh, I guess these are good for something."

    $ approval_bonus = 0

    if action_context == "shift":
        ch_k "Mmm, so what else did you have in mind?"
    else:
        call Kitty_TJ_Reset
    call checkout
    return





label Kitty_Blowjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (KittyX)
    if KittyX.action_counter["blowjob"] >= 7:
        $ approval_bonus += 15
    elif KittyX.action_counter["blowjob"] >= 3:
        $ approval_bonus += 10
    elif KittyX.action_counter["blowjob"]:
        $ approval_bonus += 7

    if KittyX.addiction >= 75 and KittyX.event_counter["swallowed"] >=3:
        $ approval_bonus += 25
    elif KittyX.addiction >= 75:
        $ approval_bonus += 15

    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in KittyX.Traits:
        $ approval_bonus += (4*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in KittyX.Traits:
        $ approval_bonus -= 40
    if KittyX.event_counter["forced"] and not KittyX.Forced:
        $ approval_bonus -= 5*KittyX.event_counter["forced"]

    if Taboo and "no_taboo" in KittyX.daily_history:
        $ approval_bonus -= 10

    if "no_blowjob" in KittyX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_blowjob" in KittyX.recent_history else 0

    $ Approval = ApprovalCheck(KittyX, 1300, TabM = 4)

    if not KittyX.action_counter["blowjob"] and "no_blowjob" not in KittyX.recent_history:
        $ KittyX.change_face("surprised", 2)
        $ KittyX.mouth = "kiss"
        ch_k "You want me to suck your dick?"
        if KittyX.action_counter["handjob"]:
            $ KittyX.mouth = "smile"
            ch_k "Not satisfied with handies?"
        $ KittyX.blushing = 1

    if not KittyX.action_counter["blowjob"] and Approval:
        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
        elif KittyX.love >= (KittyX.obedience + KittyX.inhibition):
            $ KittyX.change_face("sexy")
            $ KittyX.brows = "sad"
            $ KittyX.mouth = "smile"
            ch_k "I have wondered what you. . . taste like."
        elif KittyX.obedience >= KittyX.inhibition:
            $ KittyX.change_face("normal")
            ch_k "If you want me to. . ."
        elif KittyX.addiction >= 50:
            $ KittyX.change_face("manic", 1)
            ch_k "My mouth is watering. . ."
        else:
            $ KittyX.change_face("sad")
            $ KittyX.mouth = "smile"
            ch_k "[KittyX.Like]sure. . ."
    elif Approval:
        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
            ch_k "You want me to do that again?"
        elif not Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "Ok, I guess this is private enough. . ."
        elif "blowjob" in KittyX.recent_history:
            $ KittyX.change_face("sexy", 1)
            ch_k "Mmm, again? [[stretches her jaw]"
            jump Kitty_BJ_Prep
        elif "blowjob" in KittyX.daily_history:
            $ KittyX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",   
                "You're going to give me lockhee- . . . jaw.", 
                "Let me get some saliva going.",
                "Didn't get enough earlier?",
                "My jaw's still a bit sore from earlier.",
                "My jaw's still a bit sore from earlier."])
            ch_k "[Line]"
        elif KittyX.action_counter["blowjob"] < 3:
            $ KittyX.change_face("sexy", 1)
            $ KittyX.brows = "confused"
            $ KittyX.mouth = "kiss"
            ch_k "So you'd like another blowjob?"
        else:
            $ KittyX.change_face("sexy", 1)
            $ KittyX.ArmPose = 2
            $ Line = renpy.random.choice(["You want me to [mimes blowing]?",                 
                "So you wanna 'nother blowjob?",                 
                "A little. . . lick?", 
                "You want me to suck you off?",
                "A little tlc?"])
            ch_k "[Line]"
        $ Line = 0

    if Approval >= 2:
        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("obedience", 90, 1)
            $ KittyX.change_stat("inhibition", 60, 1)
            ch_k "Whatever."
        elif "no_blowjob" in KittyX.daily_history:
            ch_k "Ok, fine, I suppose it isn't {i}sooo{/i} bad. . ."
        else:
            $ KittyX.change_face("sexy", 1)
            $ KittyX.change_stat("love", 90, 1)
            $ KittyX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, ahhhhhh.",                 
                "Well. . . ok.",                 
                "Yum.", 
                "Sure, whip it out.",
                "Ok. . . [She licks her lips].",
                "Lol, ok, alright."])
            ch_k "[Line]"
            $ Line = 0
        $ KittyX.change_stat("obedience", 20, 1)
        $ KittyX.change_stat("obedience", 70, 1)
        $ KittyX.change_stat("inhibition", 80, 2)
        jump Kitty_BJ_Prep
    else:

        $ KittyX.change_face("angry")
        if "no_blowjob" in KittyX.recent_history:
            ch_k "What did I[KittyX.like]{i}just{/i} tell you [KittyX.player_petname]."
        elif Taboo and "no_taboo" in KittyX.daily_history and "no_blowjob" in KittyX.daily_history:
            ch_k "I told you, not in public!"
        elif "no_blowjob" in KittyX.daily_history:
            ch_k "I told you \"no,\" [KittyX.player_petname]."
        elif Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "I told you this is too public!"
        elif not KittyX.action_counter["blowjob"]:
            $ KittyX.change_face("bemused")
            ch_k "I don't know about the taste, [KittyX.player_petname]. . ."
        else:
            $ KittyX.change_face("bemused")
            ch_k "Later, [KittyX.player_petname]!"
        menu:
            extend ""
            "Sorry, never mind." if "no_blowjob" in KittyX.daily_history:
                $ KittyX.change_face("bemused")
                ch_k "Aw, it's ok, [KittyX.player_petname]."
                return
            "Maybe later?" if "no_blowjob" not in KittyX.daily_history:
                $ KittyX.change_face("sexy")
                ch_k "You[KittyX.like]never know, [KittyX.player_petname]."
                $ KittyX.change_stat("love", 80, 2)
                $ KittyX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ KittyX.recent_history.append("no_taboo")
                    $ KittyX.daily_history.append("no_taboo")
                $ KittyX.recent_history.append("no_blowjob")
                $ KittyX.daily_history.append("no_blowjob")
                return
            "Come on, please?":
                if Approval:
                    $ KittyX.change_face("sexy")
                    $ KittyX.change_stat("obedience", 90, 2)
                    $ KittyX.change_stat("obedience", 50, 2)
                    $ KittyX.change_stat("inhibition", 70, 3)
                    $ KittyX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Well, sure, I guess.",                 
                        "Well. . . ok.",                 
                        "I could maybe give it a try.", 
                        "I guess I could. . .",
                        "Fiiine. . . [She licks her lips].",
                        "Heh, ok, fine."])
                    ch_k "[Line]"
                    $ Line = 0
                    jump Kitty_BJ_Prep
                else:
                    if ApprovalCheck(KittyX, 1100, TabM = 3):
                        $ KittyX.change_stat("inhibition", 80, 1)
                        $ KittyX.change_stat("inhibition", 60, 3)
                        $ KittyX.change_face("confused", 1)
                        $ KittyX.ArmPose = 1
                        if KittyX.action_counter["handjob"]:
                            ch_k "Maybe I could just use my hand?"
                        else:
                            ch_k "I could maybe. . . [[she makes a jerking motion with her hand]?"
                        menu:
                            ch_k "Would that work?"
                            "Sure, that's fine.":
                                $ KittyX.change_stat("love", 80, 2)
                                $ KittyX.change_stat("inhibition", 60, 1)
                                $ KittyX.change_stat("obedience", 50, 1)
                                jump Kitty_HJ_Prep
                            "Nah, if it's not a BJ, forget it.":
                                $ KittyX.change_stat("love", 200, -2)
                                $ KittyX.ArmPose = 0
                                ch_k "Ok, your loss."
                                $ KittyX.change_stat("obedience", 70, 2)
            "Suck it, [KittyX.petname]":


                $ KittyX.nameCheck()
                $ Approval = ApprovalCheck(KittyX, 750, "OI", TabM = 3)
                if Approval > 1 or (Approval and KittyX.Forced):
                    $ KittyX.change_face("sad")
                    $ KittyX.change_stat("love", 70, -5, 1)
                    $ KittyX.change_stat("love", 200, -2)
                    ch_k "Ok, fine. . ."
                    $ KittyX.change_stat("obedience", 50, 4)
                    $ KittyX.change_stat("inhibition", 80, 1)
                    $ KittyX.change_stat("inhibition", 60, 3)
                    $ KittyX.Forced = 1
                    jump Kitty_BJ_Prep
                else:
                    $ KittyX.change_stat("love", 200, -15)
                    $ KittyX.recent_history.append("angry")
                    $ KittyX.daily_history.append("angry")


    if "no_blowjob" in KittyX.daily_history:
        $ KittyX.change_face("angry", 1)
        ch_k "You can eat a dick, 'cos I'm not."
        $ KittyX.recent_history.append("angry")
        $ KittyX.daily_history.append("angry")
    elif KittyX.Forced:
        $ KittyX.change_face("angry", 1)
        ch_k "I just can't do that!"
        $ KittyX.change_stat("lust", 200, 5)
        if KittyX.love > 300:
            $ KittyX.change_stat("love", 70, -2)
        $ KittyX.change_stat("obedience", 50, -2)
        $ KittyX.recent_history.append("angry")
        $ KittyX.daily_history.append("angry")
        $ KittyX.recent_history.append("no_blowjob")
        $ KittyX.daily_history.append("no_blowjob")
        return
    elif Taboo:
        $ KittyX.change_face("angry", 1)
        $ KittyX.daily_history.append("no_taboo")
        ch_k "This is way too exposed!"
        $ KittyX.change_stat("lust", 200, 5)
        $ KittyX.change_stat("obedience", 50, -3)
        return
    elif KittyX.action_counter["blowjob"]:
        $ KittyX.change_face("sad")
        ch_k "No, not this time."
    else:
        $ KittyX.change_face("normal", 1)
        ch_k "Nope."
    $ KittyX.recent_history.append("no_blowjob")
    $ KittyX.daily_history.append("no_blowjob")
    $ approval_bonus = 0
    return


label Kitty_BJ_Prep:
    if renpy.showing("Kitty_HJ_Animation"):
        hide Kitty_HJ_Animation with easeoutbottom
    if Taboo:
        $ KittyX.inhibition += int(Taboo/10)
        $ KittyX.lust += int(Taboo/5)

    $ KittyX.change_face("sexy")
    if KittyX.Forced:
        $ KittyX.change_face("sad")
    elif not KittyX.action_counter["blowjob"]:
        $ KittyX.brows = "confused"
        $ KittyX.eyes = "sexy"
        $ KittyX.mouth = "smile"

    call Seen_First_Peen (KittyX, Partner, React=action_context)
    call Kitty_BJ_Launch ("L")

    if action_context == KittyX:

        $ action_context = 0
        "[KittyX.name] slides down and gives your cock a little lick."
        menu:
            "What do you do?"
            "Nothing.":
                $ KittyX.change_stat("inhibition", 80, 3)
                $ KittyX.change_stat("inhibition", 40, 2)
                "[KittyX.name] continues licking at it."
            "Praise her.":
                $ KittyX.change_face("sexy", 1)
                $ KittyX.change_stat("inhibition", 80, 3)
                ch_p "Hmmm, keep doing that, [KittyX.petname]."
                $ KittyX.nameCheck()
                "[KittyX.name] continues her actions."
                $ KittyX.change_stat("love", 85, 1)
                $ KittyX.change_stat("obedience", 90, 1)
                $ KittyX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ KittyX.change_face("surprised")
                $ KittyX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that for now, [KittyX.petname]."
                $ KittyX.nameCheck()
                "[KittyX.name] puts it down."
                $ KittyX.change_stat("obedience", 90, 1)
                $ KittyX.change_stat("obedience", 50, 3)
                $ Player.recent_history.append("nope")
                $ KittyX.AddWord(1,"refused","refused")
                return
    if not KittyX.action_counter["blowjob"]:
        if KittyX.Forced:
            $ KittyX.change_stat("love", 90, -70)
            $ KittyX.change_stat("obedience", 70, 45)
            $ KittyX.change_stat("inhibition", 80, 60)
        else:
            $ KittyX.change_stat("love", 90, 5)
            $ KittyX.change_stat("obedience", 70, 35)
            $ KittyX.change_stat("inhibition", 80, 40)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ KittyX.DrainWord("no_taboo")
    $ KittyX.DrainWord("no_blowjob")
    $ KittyX.recent_history.append("blowjob")
    $ KittyX.daily_history.append("blowjob")

label Kitty_BJ_Cycle:
    while Round > 0:
        call shift_focus (KittyX)
        call Kitty_BJ_Launch
        $ KittyX.lust_face()

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
                    if "pushed" in KittyX.recent_history:
                        ch_k "Sorry, I just can't handle all of you yet."
                    elif KittyX.action_counter["blowjob"] < 5:
                        $ KittyX.change_stat("love", 80, -(20-(2*KittyX.action_counter["blowjob"])))
                        $ KittyX.change_stat("obedience", 80, (30-(3*KittyX.action_counter["blowjob"])))
                        "She gags on it slightly and moves back to a more comfortable pace."
                        $ KittyX.recent_history.append("pushed")
                    else:
                        if offhand_action == "jackin" and action_speed != 3:
                            "She takes it to the root, and you move your hand out of the way."
                        $ action_speed = 4
                "Take it deeper. (locked)" if action_speed == 4:
                    pass
                "Set your own pace. . .":

                    "[KittyX.name] hums contentedly."
                    if "setpace" not in KittyX.recent_history:
                        $ KittyX.change_stat("love", 80, 2)
                    $ D20 = renpy.random.randint(1, 20)
                    if KittyX.action_counter["blowjob"] < 5:
                        $ D20 -= 10
                    elif KittyX.action_counter["blowjob"] < 10:
                        $ D20 -= 5

                    if D20 > 15:
                        $ action_speed = 4
                        if "setpace" not in KittyX.recent_history:
                            $ KittyX.change_stat("inhibition", 80, 3)
                    elif D20 > 10:
                        $ action_speed = 3
                    elif D20 > 5:
                        $ action_speed = 2
                    else:
                        $ action_speed = 1
                    $ KittyX.recent_history.append("setpace")

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
                            if KittyX.remaining_actions and multi_action:
                                $ offhand_action = "fondle_breasts"
                                "You start to fondle her breasts."
                                $ KittyX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (KittyX, "tired")
                        "Shift primary action":

                            if KittyX.remaining_actions and multi_action:
                                menu:
                                    "How about a handy?":
                                        if KittyX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Kitty_BJ_After
                                            call Kitty_Handjob
                                        else:
                                            ch_k "I'm kinda tired, could we just wrap this up. . ."
                                    "How about a titjob?":
                                        if KittyX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Kitty_BJ_After
                                            call Kitty_Titjob
                                        else:
                                            ch_k "I'm kinda tired, could we just wrap this up. . ."
                                    "Never Mind":
                                        jump Kitty_BJ_Cycle
                            else:
                                call Sex_Basic_Dialog (KittyX, "tired")

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [KittyX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (KittyX)
                                "Ask [KittyX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (KittyX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (KittyX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Kitty_BJ_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Kitty_BJ_Cycle
                                "Never mind":
                                    jump Kitty_BJ_Cycle
                        "Undress [KittyX.name]":
                            call Girl_Undress (KittyX)
                        "Clean up [KittyX.name] (locked)" if not KittyX.Spunk:
                            pass
                        "Clean up [KittyX.name]" if KittyX.Spunk:
                            call Girl_Cleanup (KittyX, "ask")
                        "Never mind":
                            jump Kitty_BJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Kitty_BJ_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Kitty_BJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Kitty_BJ_Reset
                    $ Line = 0
                    jump Kitty_BJ_After


        call shift_focus (KittyX)
        call Sex_Dialog (KittyX, Partner)



        $ counter += 1
        $ Round -= 1
        if action_speed:
            $ Player.Wet = 1
            $ Player.Spunk = 0 if Player.Spunk else Player.Spunk

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or KittyX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (KittyX)
                if "angry" in KittyX.recent_history:
                    call Kitty_BJ_Reset
                    return
                $ KittyX.change_stat("lust", 200, 5)
                if 100 > KittyX.lust >= 70 and KittyX.session_orgasms < 2 and KittyX.SEXP >= 20:
                    $ KittyX.recent_history.append("unsatisfied")
                    $ KittyX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Kitty_BJ_After
                $ Line = "came"

            if KittyX.lust >= 100:

                call Girl_Cumming (KittyX)
                if action_context == "shift" or "angry" in KittyX.recent_history:
                    jump Kitty_BJ_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."

                if "unsatisfied" in KittyX.recent_history:
                    "[KittyX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Kitty_BJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if KittyX.SEXP >= 100 or ApprovalCheck(KittyX, 1200, "LO"):
            pass
        elif counter == (10 + KittyX.action_counter["blowjob"]):
            $ KittyX.brows = "angry"
            menu:
                ch_k "I'm[KittyX.like]totally worn out here. Can we do something else?"
                "How about a Handy?" if KittyX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Kitty_BJ_After
                    call Kitty_Handjob
                    return
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    jump Kitty_BJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Kitty_BJ_Reset
                    $ action_context = "shift"
                    jump Kitty_BJ_After
                "No, get back down there.":
                    if ApprovalCheck(KittyX, 1200) or ApprovalCheck(KittyX, 500, "O"):
                        $ KittyX.change_stat("love", 200, -5)
                        $ KittyX.change_stat("obedience", 50, 3)
                        $ KittyX.change_stat("obedience", 80, 2)
                        "She grumbles but gets back to work."
                    else:
                        $ KittyX.change_face("angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        ch_k "Well fuck you then."
                        $ KittyX.change_stat("love", 50, -3, 1)
                        $ KittyX.change_stat("love", 80, -4, 1)
                        $ KittyX.change_stat("obedience", 30, -1, 1)
                        $ KittyX.change_stat("obedience", 50, -1, 1)
                        $ KittyX.recent_history.append("angry")
                        $ KittyX.daily_history.append("angry")
                        jump Kitty_BJ_After
        elif counter == (5 + KittyX.action_counter["blowjob"]) and KittyX.SEXP <= 100 and not ApprovalCheck(KittyX, 1200, "LO"):
            $ KittyX.brows = "confused"
            ch_k "Are you getting close here? I'm cramping up."


        call Escalation (KittyX)

        if Round == 10:
            ch_k "It's kind of time to get moving."
        elif Round == 5:
            ch_k "For real[KittyX.like]time's up."


    $ KittyX.change_face("bemused", 0)
    $ Line = 0
    ch_k "Ok, I gotta rest my jaw for a minute. . ."

label Kitty_BJ_After:
    $ KittyX.change_face("sexy")

    $ KittyX.action_counter["blowjob"] += 1
    $ KittyX.remaining_actions -=1
    $ KittyX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ KittyX.addiction_rate += 1

    call Partner_Like (KittyX, 2)

    if "Kitty Jobber" in Achievements:
        pass
    elif KittyX.action_counter["blowjob"] >= 10:
        $ KittyX.change_face("smile", 1)
        ch_k "I can't[KittyX.like]get your taste out of my mind."
        $ Achievements.append("Kitty Jobber")
        $ KittyX.SEXP += 5
    elif action_context == "shift":
        pass
    elif KittyX.action_counter["blowjob"] == 1:
        $ KittyX.SEXP += 15
        if KittyX.love >= 500:
            $ KittyX.mouth = "smile"
            ch_k "Huh, that wasn't bad."
        elif Player.focus <= 20:
            $ KittyX.mouth = "sad"
            ch_k "I hope you enjoyed that."
    elif KittyX.action_counter["blowjob"] == 5:
        ch_k "I'm getting better at this. . . right?"
        menu:
            "[[nod]":
                $ KittyX.change_face("smile", 1)
                $ KittyX.change_stat("love", 90, 15)
                $ KittyX.change_stat("obedience", 80, 5)
                $ KittyX.change_stat("inhibition", 90, 10)
            "[[shake head \"no\"]":
                if ApprovalCheck(KittyX, 500, "O"):
                    $ KittyX.change_face("sad", 2)
                    $ KittyX.change_stat("love", 200, -5)
                else:
                    $ KittyX.change_face("angry", 2)
                    $ KittyX.change_stat("love", 200, -25)
                $ KittyX.change_stat("obedience", 80, 10)
                ch_k ". . ."
                $ KittyX.change_face("sad", 1)

    $ approval_bonus = 0
    if action_context != "shift":
        call Kitty_BJ_Reset
    call checkout
    return






label Kitty_Dildo_Check:
    if "dildo" in Player.Inventory:
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in KittyX.Inventory:
        "You ask [KittyX.name] to get out her favorite Dildo."
    else:
        "You don't have one of those on you."
        return 0
    return 1

label Kitty_Dildo_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (KittyX)
    call Kitty_Dildo_Check
    if not _return:
        return

    if KittyX.action_counter["dildo_pussy"]:
        $ approval_bonus += 15
    if KittyX.PantsNum() > 6:
        $ approval_bonus -= 20

    if KittyX.lust > 95:
        $ approval_bonus += 20
    elif KittyX.lust > 85:
        $ approval_bonus += 15

    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in KittyX.Traits:
        $ approval_bonus += (5*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in KittyX.Traits:
        $ approval_bonus -= 40
    if KittyX.event_counter["forced"] and not KittyX.Forced:
        $ approval_bonus -= 5*KittyX.event_counter["forced"]

    if Taboo and "no_taboo" in KittyX.daily_history:
        $ approval_bonus -= 10

    if "no_dildo" in KittyX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_dildo" in KittyX.recent_history else 0

    $ Approval = ApprovalCheck(KittyX, 1250, TabM = 4)

    if action_context == KittyX:
        if Approval > 2:
            if KittyX.PantsNum() == 5:
                "[KittyX.name] grabs her dildo, hiking up her skirt as she does."
                $ KittyX.Upskirt = 1
            elif KittyX.PantsNum() > 6:
                "[KittyX.name] grabs her dildo, pulling down her pants as she does."
                $ KittyX.legs = 0
            else:
                "[KittyX.name] grabs her dildo, rubbing is suggestively against her crotch."
            $ KittyX.SeenPanties = 1
            "She slides the tip along her pussy and seems to want you to insert it."
            menu:
                "What do you do?"
                "Nothing.":
                    $ KittyX.change_stat("inhibition", 80, 3)
                    $ KittyX.change_stat("inhibition", 50, 2)
                    "[KittyX.name] slides it in."
                "Go for it.":
                    $ KittyX.change_face("sexy", 1)
                    $ KittyX.change_stat("inhibition", 80, 3)
                    ch_p "Oh yeah, [KittyX.petname], let's do this."
                    $ KittyX.nameCheck()
                    "You grab the dildo and slide it in."
                    $ KittyX.change_stat("love", 85, 1)
                    $ KittyX.change_stat("obedience", 90, 1)
                    $ KittyX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ KittyX.change_face("surprised")
                    $ KittyX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that right now, [KittyX.petname]."
                    $ KittyX.nameCheck()
                    "[KittyX.name] sets the dildo down."
                    $ KittyX.change_outfit()
                    $ KittyX.change_stat("obedience", 90, 1)
                    $ KittyX.change_stat("obedience", 50, 1)
                    $ KittyX.change_stat("obedience", 30, 2)
                    return
            jump Kitty_DP_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
        return

    if action_context == "auto":
        "You rub the dildo across her body, and along her moist slit."
        $ KittyX.change_face("surprised", 1)

        if (KittyX.action_counter["dildo_pussy"] and Approval) or (Approval > 1):
            "[KittyX.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            $ KittyX.change_face("sexy")
            $ KittyX.change_stat("obedience", 70, 3)
            $ KittyX.change_stat("inhibition", 50, 3)
            $ KittyX.change_stat("inhibition", 70, 1)
            ch_k "Ooo, [KittyX.player_petname], toys!"
            jump Kitty_DP_Prep
        else:
            $ KittyX.brows = "angry"
            menu:
                ch_k "Hey, what are you planning to do with that?!"
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ KittyX.change_face("sexy", 1)
                        $ KittyX.change_stat("obedience", 70, 3)
                        $ KittyX.change_stat("inhibition", 50, 3)
                        $ KittyX.change_stat("inhibition", 70, 1)
                        ch_k "Well, now that you mention it. . ."
                        jump Kitty_DP_Prep
                    "You pull back before you really get it in."
                    $ KittyX.change_face("bemused", 1)
                    if KittyX.action_counter["dildo_pussy"]:
                        ch_k "Well ok, [KittyX.player_petname], maybe warn me next time?"
                    else:
                        ch_k "Well ok, [KittyX.player_petname], that's a little much. . . for now . . ."
                "Just playing with my favorite toys.":
                    $ KittyX.change_stat("love", 80, -10, 1)
                    $ KittyX.change_stat("love", 200, -10)
                    "You press it inside some more."
                    $ KittyX.change_stat("obedience", 70, 3)
                    $ KittyX.change_stat("inhibition", 50, 3)
                    if not ApprovalCheck(KittyX, 700, "O", TabM=1):
                        $ KittyX.change_face("angry")
                        "[KittyX.name] shoves you away and slaps you in the face."
                        ch_k "Jerk!"
                        ch_k "Ask nice if you want to stick something in my pussy!"
                        $ KittyX.change_stat("love", 50, -10, 1)
                        $ KittyX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        if renpy.showing("Kitty_SexSprite"):
                            call Kitty_Sex_Reset
                        $ KittyX.recent_history.append("angry")
                        $ KittyX.daily_history.append("angry")
                    else:
                        $ KittyX.change_face("sad")
                        "[KittyX.name] doesn't seem to be into this, you're lucky she's so obedient."
                        jump Kitty_DP_Prep
        return


    if not KittyX.action_counter["dildo_pussy"]:

        $ KittyX.change_face("surprised", 1)
        $ KittyX.mouth = "kiss"
        ch_k "Hmmm, so you'd like to try out some toys?"
        if KittyX.Forced:
            $ KittyX.change_face("sad")
            ch_k "I suppose there are worst things you could ask for."

    if not KittyX.action_counter["dildo_pussy"] and Approval:

        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
        elif KittyX.love >= (KittyX.obedience + KittyX.inhibition):
            $ KittyX.change_face("sexy")
            $ KittyX.brows = "sad"
            $ KittyX.mouth = "smile"
            ch_k "I've had a reasonable amount of experience with these, you know. . ."
        elif KittyX.obedience >= KittyX.inhibition:
            $ KittyX.change_face("normal")
            ch_k "If that's what you want, [KittyX.player_petname]. . ."
        else:
            $ KittyX.change_face("sad")
            $ KittyX.mouth = "smile"
            ch_k "I guess it could be fun with a partner. . ."

    elif Approval:

        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
            ch_k "The toys again?"
        elif not Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "Well, at least you got us some privacy this time. . ."
        elif "dildo_pussy" in KittyX.recent_history:
            $ KittyX.change_face("sexy", 1)
            ch_k "Mmm, again? Ok, let's get to it."
            jump Kitty_DP_Prep
        elif "dildo_pussy" in KittyX.daily_history:
            $ KittyX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "You're going to wear me out."])
            ch_k "[Line]"
        elif KittyX.action_counter["dildo_pussy"] < 3:
            $ KittyX.change_face("sexy", 1)
            $ KittyX.brows = "confused"
            $ KittyX.mouth = "kiss"
            ch_k "You want to stick it in my pussy again?"
        else:
            $ KittyX.change_face("sexy", 1)
            $ KittyX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my pussy again?",
                    "You want me ta lube up your toy?"])
            ch_k "[Line]"
            $ Line = 0

    if Approval >= 2:

        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("obedience", 90, 1)
            $ KittyX.change_stat("inhibition", 60, 1)
            ch_k "Ok, fine."
        else:
            $ KittyX.change_face("sexy", 1)
            $ KittyX.change_stat("love", 90, 1)
            $ KittyX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                    "Well. . . ok.",                 
                    "Sure!", 
                    "I guess I could. . . stick it in.",
                    "Hells yeah.",
                    "Heh, ok, ok."])
            ch_k "[Line]"
            $ Line = 0
        $ KittyX.change_stat("obedience", 20, 1)
        $ KittyX.change_stat("obedience", 60, 1)
        $ KittyX.change_stat("inhibition", 70, 2)
        jump Kitty_DP_Prep
    else:


        $ KittyX.change_face("angry")
        if "no_dildo" in KittyX.recent_history:
            ch_k "What part of \"no,\" did you not get, [KittyX.player_petname]?"
        elif Taboo and "no_taboo" in KittyX.daily_history and "no_dildo" in KittyX.daily_history:
            ch_k "Stop swinging that thing around in public!"
        elif "no_dildo" in KittyX.daily_history:
            ch_k "I already told you \"no,\" [KittyX.player_petname]."
        elif Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "Stop swinging that thing around in public!"
        elif not KittyX.action_counter["dildo_pussy"]:
            $ KittyX.change_face("bemused")
            ch_k "I'm just not into toys, [KittyX.player_petname]. . ."
        else:
            $ KittyX.change_face("bemused")
            ch_k "I don't think we need any toys, [KittyX.player_petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no_dildo" in KittyX.daily_history:
                $ KittyX.change_face("bemused")
                ch_k "Yeah, ok, [KittyX.player_petname]."
                return
            "Maybe later?" if "no_dildo" not in KittyX.daily_history:
                $ KittyX.change_face("sexy")
                ch_k "Maybe I'll practice on my own time, [KittyX.player_petname]."
                $ KittyX.change_stat("love", 80, 2)
                $ KittyX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ KittyX.recent_history.append("no_taboo")
                    $ KittyX.daily_history.append("no_taboo")
                $ KittyX.recent_history.append("no_dildo")
                $ KittyX.daily_history.append("no_dildo")
                return
            "I think you'd like it. . .":
                if Approval:
                    $ KittyX.change_face("sexy")
                    $ KittyX.change_stat("obedience", 90, 2)
                    $ KittyX.change_stat("obedience", 50, 2)
                    $ KittyX.change_stat("inhibition", 70, 3)
                    $ KittyX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                            "I suppose. . .", 
                            "You've got me there."])
                    ch_k "[Line]"
                    $ Line = 0
                    jump Kitty_DP_Prep
                else:
                    pass
            "[[press it against her]":

                $ Approval = ApprovalCheck(KittyX, 950, "OI", TabM = 3)
                if Approval > 1 or (Approval and KittyX.Forced):
                    $ KittyX.change_face("sad")
                    $ KittyX.change_stat("love", 70, -5, 1)
                    $ KittyX.change_stat("love", 200, -5)
                    ch_k "Ok, fine. If we're going to do this, stick it in already."
                    $ KittyX.change_stat("obedience", 80, 4)
                    $ KittyX.change_stat("inhibition", 80, 1)
                    $ KittyX.change_stat("inhibition", 60, 3)
                    $ KittyX.Forced = 1
                    jump Kitty_DP_Prep
                else:
                    $ KittyX.change_stat("love", 200, -20)
                    $ KittyX.recent_history.append("angry")
                    $ KittyX.daily_history.append("angry")


    $ KittyX.ArmPose = 1
    if "no_dildo" in KittyX.daily_history:
        ch_k "Learn to take \"no\" for an answer, [KittyX.player_petname]."
        $ KittyX.recent_history.append("angry")
        $ KittyX.daily_history.append("angry")
    elif KittyX.Forced:
        $ KittyX.change_face("angry", 1)
        ch_k "I'm not going to let you use that on me."
        $ KittyX.change_stat("lust", 200, 5)
        if KittyX.love > 300:
            $ KittyX.change_stat("love", 70, -2)
        $ KittyX.change_stat("obedience", 50, -2)
        $ KittyX.recent_history.append("angry")
        $ KittyX.daily_history.append("angry")
    elif Taboo:
        $ KittyX.change_face("angry", 1)
        $ KittyX.recent_history.append("no_taboo")
        $ KittyX.daily_history.append("no_taboo")
        ch_k "Not here!"
        $ KittyX.change_stat("lust", 200, 5)
        $ KittyX.change_stat("obedience", 50, -3)
    elif KittyX.action_counter["dildo_pussy"]:
        $ KittyX.change_face("sad")
        ch_k "Sorry, you can keep your toys to yourself."
    else:
        $ KittyX.change_face("normal", 1)
        ch_k "No way."
    $ KittyX.recent_history.append("no_dildo")
    $ KittyX.daily_history.append("no_dildo")
    $ approval_bonus = 0
    return

label Kitty_DP_Prep:
    if offhand_action == "dildo_pussy":
        return

    if not KittyX.Forced and action_context != "auto":
        $ approval_bonus = 15 if KittyX.PantsNum() > 6 else 0
        call Bottoms_Off (KittyX)
        if "angry" in KittyX.recent_history:
            return

    $ approval_bonus = 0
    call Kitty_Pussy_Launch ("dildo_pussy")
    if not KittyX.action_counter["dildo_pussy"]:
        if KittyX.Forced:
            $ KittyX.change_stat("love", 90, -75)
            $ KittyX.change_stat("obedience", 70, 60)
            $ KittyX.change_stat("inhibition", 80, 35)
        else:
            $ KittyX.change_stat("love", 90, 10)
            $ KittyX.change_stat("obedience", 70, 20)
            $ KittyX.change_stat("inhibition", 80, 45)
    if Taboo:
        $ KittyX.inhibition += int(Taboo/10)
        $ KittyX.lust += int(Taboo/5)


    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ KittyX.DrainWord("no_taboo")
    $ KittyX.DrainWord("no_dildo")
    $ KittyX.recent_history.append("dildo_pussy")
    $ KittyX.daily_history.append("dildo_pussy")

label Kitty_DP_Cycle:
    while Round > 0:
        call shift_focus (KittyX)
        call Kitty_Pussy_Launch ("dildo_pussy")
        $ KittyX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (KittyX)
                    jump Kitty_DP_Cycle

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
                            if KittyX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ KittyX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (KittyX, "tired")
                        "Shift primary action":

                            if KittyX.remaining_actions and multi_action:
                                menu:
                                    "I want to stick a finger in her ass.":
                                        $ action_context = "shift"
                                        call Kitty_DP_After
                                        call Kitty_Insert_Ass
                                    "Just stick a finger in her ass without asking.":
                                        $ action_context = "auto"
                                        call Kitty_DP_After
                                        call Kitty_Insert_Ass
                                    "I want to shift the dildo to her ass.":
                                        $ action_context = "shift"
                                        call Kitty_DP_After
                                        call Kitty_Dildo_Ass
                                    "Never Mind":
                                        jump Kitty_DP_Cycle
                            else:
                                call Sex_Basic_Dialog (KittyX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Kitty_DP_After
                            call Offhand_Set
                        "Shift your focus (locked)" if not offhand_action:
                            pass
                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [KittyX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (KittyX)
                                "Ask [KittyX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (KittyX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (KittyX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Kitty_DP_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Kitty_DP_Cycle
                                "Never mind":
                                    jump Kitty_DP_Cycle
                        "Undress [KittyX.name]":
                            call Girl_Undress (KittyX)
                        "Clean up [KittyX.name] (locked)" if not KittyX.Spunk:
                            pass
                        "Clean up [KittyX.name]" if KittyX.Spunk:
                            call Girl_Cleanup (KittyX, "ask")
                        "Never mind":
                            jump Kitty_DP_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Kitty_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Kitty_DP_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Kitty_Pos_Reset
                    $ Line = 0
                    jump Kitty_DP_After


        if KittyX.underwear or KittyX.PantsNum() > 6 or KittyX.HoseNum() >= 5:
            call Girl_Undress (KittyX, "auto")

        call shift_focus (KittyX)
        call Sex_Dialog (KittyX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or KittyX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (KittyX)
                if "angry" in KittyX.recent_history:
                    call Kitty_Pos_Reset
                    return
                $ KittyX.change_stat("lust", 200, 5)
                if 100 > KittyX.lust >= 70 and KittyX.session_orgasms < 2:
                    $ KittyX.recent_history.append("unsatisfied")
                    $ KittyX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Kitty_DP_After
                $ Line = "came"

            if KittyX.lust >= 100:

                call Girl_Cumming (KittyX)
                if action_context == "shift" or "angry" in KittyX.recent_history:
                    jump Kitty_DP_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in KittyX.recent_history:
                    "[KittyX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Kitty_DP_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if KittyX.SEXP >= 100 or ApprovalCheck(KittyX, 1200, "LO"):
            pass
        elif counter == (5 + KittyX.action_counter["dildo_pussy"]):
            $ KittyX.brows = "confused"
            ch_k "What are you even doing down there?"
        elif KittyX.lust >= 80:
            pass
        elif counter == (15 + KittyX.action_counter["dildo_pussy"]) and KittyX.SEXP >= 15 and not ApprovalCheck(KittyX, 1500):
            $ KittyX.brows = "confused"
            menu:
                ch_k "[KittyX.player_petname], this is getting uncomfortable, maybe we could try something else."
                "Finish up.":
                    "You let go. . ."
                    jump Kitty_DP_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Kitty_DP_After
                "No, this is fun.":
                    if ApprovalCheck(KittyX, 1200) or ApprovalCheck(KittyX, 500, "O"):
                        $ KittyX.change_stat("love", 200, -5)
                        $ KittyX.change_stat("obedience", 50, 3)
                        $ KittyX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ KittyX.change_face("angry", 1)
                        call Kitty_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_k "Well if that's your attitude, I don't need your \"help\"."
                        $ KittyX.change_stat("love", 50, -3, 1)
                        $ KittyX.change_stat("love", 80, -4, 1)
                        $ KittyX.change_stat("obedience", 30, -1, 1)
                        $ KittyX.change_stat("obedience", 50, -1, 1)
                        $ KittyX.recent_history.append("angry")
                        $ KittyX.daily_history.append("angry")
                        jump Kitty_DP_After


        if Round == 10:
            ch_k "It's kind of time to get moving."
        elif Round == 5:
            ch_k "For real[KittyX.like]time's up."


    $ KittyX.change_face("bemused", 0)
    $ Line = 0
    ch_k "Ok, we need to take a break."


label Kitty_DP_After:
    if not action_context:
        call Kitty_Pos_Reset

    $ KittyX.change_face("sexy")

    $ KittyX.action_counter["dildo_pussy"] += 1
    $ KittyX.remaining_actions -=1

    call Partner_Like (KittyX, 1)

    if KittyX.action_counter["dildo_pussy"] == 1:
        $ KittyX.SEXP += 10
        if not action_context:
            if KittyX.love >= 500 and "unsatisfied" not in KittyX.recent_history:
                ch_k "Thanks for the extra hand. . ."
            elif KittyX.obedience <= 500 and Player.focus <= 20:
                $ KittyX.change_face("perplexed", 1)
                ch_k "Did you like that?"

    $ approval_bonus = 0


    call checkout
    return






label Kitty_Dildo_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (KittyX)
    call Kitty_Dildo_Check
    if not _return:
        return

    if KittyX.used_to_anal:
        $ approval_bonus += 30
    elif "anal" in KittyX.recent_history or "dildo_anal" in KittyX.recent_history:
        $ approval_bonus -= 20
    elif "anal" in KittyX.daily_history or "dildo_anal" in KittyX.daily_history:
        $ approval_bonus -= 10
    elif (KittyX.action_counter["anal"] + KittyX.action_counter["dildo_ass"] + KittyX.Plug) > 0:
        $ approval_bonus += 20

    if KittyX.PantsNum() > 6:
        $ approval_bonus -= 20

    if KittyX.lust > 95:
        $ approval_bonus += 20
    elif KittyX.lust > 85:
        $ approval_bonus += 15

    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in KittyX.Traits:
        $ approval_bonus += (5*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in KittyX.Traits:
        $ approval_bonus -= 40
    if KittyX.event_counter["forced"] and not KittyX.Forced:
        $ approval_bonus -= 5*KittyX.event_counter["forced"]

    if Taboo and "no_taboo" in KittyX.daily_history:
        $ approval_bonus -= 10

    if "no_dildo" in KittyX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_dildo" in KittyX.recent_history else 0

    $ Approval = ApprovalCheck(KittyX, 1450, TabM = 4)

    if action_context == KittyX:

        if Approval > 2:
            if KittyX.PantsNum() == 5:
                "[KittyX.name] grabs her dildo, hiking up her skirt as she does."
                $ KittyX.Upskirt = 1
            elif KittyX.PantsNum() > 6:
                "[KittyX.name] grabs her dildo, pulling down her pants as she does."
                $ KittyX.legs = 0
            else:
                "[KittyX.name] grabs her dildo, rubbing is suggestively against her ass."
            $ KittyX.SeenPanties = 1
            "She slides the tip against her asshole, and seems to want you to insert it."
            menu:
                "What do you do?"
                "Nothing.":
                    $ KittyX.change_stat("inhibition", 80, 3)
                    $ KittyX.change_stat("inhibition", 50, 2)
                    "[KittyX.name] slides it in."
                "Go for it.":
                    $ KittyX.change_face("sexy", 1)
                    $ KittyX.change_stat("inhibition", 80, 3)
                    ch_p "Oh yeah, [KittyX.petname], let's do this."
                    $ KittyX.nameCheck()
                    "You grab the dildo and slide it in."
                    $ KittyX.change_stat("love", 85, 1)
                    $ KittyX.change_stat("obedience", 90, 1)
                    $ KittyX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ KittyX.change_face("surprised")
                    $ KittyX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that right now, [KittyX.petname]."
                    $ KittyX.nameCheck()
                    "[KittyX.name] sets the dildo down."
                    $ KittyX.change_outfit()
                    $ KittyX.change_stat("obedience", 90, 1)
                    $ KittyX.change_stat("obedience", 50, 1)
                    $ KittyX.change_stat("obedience", 30, 2)
                    return
            jump Kitty_DA_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
        return

    if action_context == "auto":
        "You rub the dildo across her body, and against her tight anus."
        $ KittyX.change_face("surprised", 1)

        if (KittyX.action_counter["dildo_ass"] and Approval) or (Approval > 1):

            "[KittyX.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            $ KittyX.change_face("sexy")
            $ KittyX.change_stat("obedience", 70, 3)
            $ KittyX.change_stat("inhibition", 50, 3)
            $ KittyX.change_stat("inhibition", 70, 1)
            ch_k "Ooo, [KittyX.player_petname], toys!"
            jump Kitty_DA_Prep
        else:

            $ KittyX.brows = "angry"
            menu:
                ch_k "Hey, what are you planning to do with that?!"
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ KittyX.change_face("sexy", 1)
                        $ KittyX.change_stat("obedience", 70, 3)
                        $ KittyX.change_stat("inhibition", 50, 3)
                        $ KittyX.change_stat("inhibition", 70, 1)
                        ch_k "Well, now that you mention it. . ."
                        jump Kitty_DA_Prep
                    "You pull back before you really get it in."
                    $ KittyX.change_face("bemused", 1)
                    if KittyX.action_counter["dildo_ass"]:
                        ch_k "Well ok, [KittyX.player_petname], maybe warn me next time?"
                    else:
                        ch_k "Well ok, [KittyX.player_petname], that's a little much. . . for now . . ."
                "Just playing with my favorite toys.":
                    $ KittyX.change_stat("love", 80, -10, 1)
                    $ KittyX.change_stat("love", 200, -10)
                    "You press it inside some more."
                    $ KittyX.change_stat("obedience", 70, 3)
                    $ KittyX.change_stat("inhibition", 50, 3)
                    if not ApprovalCheck(KittyX, 700, "O", TabM=1):
                        $ KittyX.change_face("angry")
                        "[KittyX.name] shoves you away and slaps you in the face."
                        ch_k "Jerk!"
                        ch_k "Ask nice if you want to stick something in my ass!"
                        $ KittyX.change_stat("love", 50, -10, 1)
                        $ KittyX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        if renpy.showing("Kitty_SexSprite"):
                            call Kitty_Sex_Reset
                        $ KittyX.recent_history.append("angry")
                        $ KittyX.daily_history.append("angry")
                    else:
                        $ KittyX.change_face("sad")
                        "[KittyX.name] doesn't seem to be into this, you're lucky she's so obedient."
                        jump Kitty_DA_Prep
        return


    if not KittyX.action_counter["dildo_ass"]:

        $ KittyX.change_face("surprised", 1)
        $ KittyX.mouth = "kiss"
        ch_k "You want to try and fit that. . .?"
        if KittyX.Forced:
            $ KittyX.change_face("sad")
            ch_k "Always about the butt, huh?"

    if not KittyX.used_to_anal and ("dildo_anal" in KittyX.recent_history or "anal" in KittyX.recent_history or "dildo_anal" in KittyX.daily_history or "anal" in KittyX.daily_history):
        $ KittyX.change_face("bemused", 1)
        ch_k "I'm still[KittyX.like]sore from earlier. . ."

    if not KittyX.action_counter["dildo_ass"] and Approval:

        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
        elif KittyX.love >= (KittyX.obedience + KittyX.inhibition):
            $ KittyX.change_face("sexy")
            $ KittyX.brows = "sad"
            $ KittyX.mouth = "smile"
            ch_k "I[KittyX.like]haven't actually used one of these, back there before. . ."
        elif KittyX.obedience >= KittyX.inhibition:
            $ KittyX.change_face("normal")
            ch_k "If that's what you want, [KittyX.player_petname]. . ."
        else:
            $ KittyX.change_face("sad")
            $ KittyX.mouth = "smile"
            ch_k "I guess it could be fun two-player. . ."

    elif Approval:

        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
            ch_k "The toys again?"
        elif not Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "Well, at least you got us some privacy this time. . ."
        elif "dildo_anal" in KittyX.daily_history and not KittyX.used_to_anal:
            pass
        elif "dildo_anal" in KittyX.daily_history:
            $ KittyX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "I'm still a bit sore from earlier.",
                    "You're going to wear me out."])
            ch_k "[Line]"
        elif KittyX.action_counter["dildo_ass"] < 3:
            $ KittyX.change_face("sexy", 1)
            $ KittyX.brows = "confused"
            $ KittyX.mouth = "kiss"
            ch_k "You want to stick it in my ass again?"
        else:
            $ KittyX.change_face("sexy", 1)
            $ KittyX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my ass again?",
                    "You want me ta lube up your toy?"])
            ch_k "[Line]"
            $ Line = 0

    if Approval >= 2:

        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("obedience", 90, 1)
            $ KittyX.change_stat("inhibition", 60, 1)
            ch_k "Ok, fine."
        else:
            $ KittyX.change_face("sexy", 1)
            $ KittyX.change_stat("love", 90, 1)
            $ KittyX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                    "Well. . . ok.",                 
                    "Sure!", 
                    "I guess I could. . . stick it in.",
                    "Hells yeah.",
                    "Heh, ok, ok."])
            ch_k "[Line]"
            $ Line = 0
        $ KittyX.change_stat("obedience", 20, 1)
        $ KittyX.change_stat("obedience", 60, 1)
        $ KittyX.change_stat("inhibition", 70, 2)
        jump Kitty_DA_Prep
    else:


        $ KittyX.change_face("angry")
        if "no_dildo" in KittyX.recent_history:
            ch_k "What part of \"no,\" did you not get, [KittyX.player_petname]?"
        elif Taboo and "no_taboo" in KittyX.daily_history and "no_dildo" in KittyX.daily_history:
            ch_k "Stop swinging that thing around in public!"
        elif "no_dildo" in KittyX.daily_history:
            ch_k "I already told you \"no,\" [KittyX.player_petname]."
        elif Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "I already told you that I wouldn't do that out here!"
        elif not KittyX.action_counter["dildo_ass"]:
            $ KittyX.change_face("bemused")
            ch_k "I'm just not into toys, [KittyX.player_petname]. . ."
        elif not KittyX.used_to_anal and "dildo_anal" not in KittyX.daily_history:
            $ KittyX.change_face("perplexed")
            ch_k "You could have been a bit more gentle last time, [KittyX.player_petname]. . ."
        else:
            $ KittyX.change_face("bemused")
            ch_k "I don't think we need any toys, [KittyX.player_petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no_dildo" in KittyX.daily_history:
                $ KittyX.change_face("bemused")
                ch_k "Yeah, ok, [KittyX.player_petname]."
                return
            "Maybe later?" if "no_dildo" not in KittyX.daily_history:
                $ KittyX.change_face("sexy")
                ch_k "Maybe I'll practice on my own time, [KittyX.player_petname]."
                $ KittyX.change_stat("love", 80, 2)
                $ KittyX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ KittyX.recent_history.append("no_taboo")
                    $ KittyX.daily_history.append("no_taboo")
                $ KittyX.recent_history.append("no_dildo")
                $ KittyX.daily_history.append("no_dildo")
                return
            "I think you'd like it. . .":
                if Approval:
                    $ KittyX.change_face("sexy")
                    $ KittyX.change_stat("obedience", 90, 2)
                    $ KittyX.change_stat("obedience", 50, 2)
                    $ KittyX.change_stat("inhibition", 70, 3)
                    $ KittyX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                            "I suppose. . .", 
                            "You've got me there."])
                    ch_k "[Line]"
                    $ Line = 0
                    jump Kitty_DA_Prep
                else:
                    pass
            "[[press it against her]":

                $ Approval = ApprovalCheck(KittyX, 1050, "OI", TabM = 3)
                if Approval > 1 or (Approval and KittyX.Forced):
                    $ KittyX.change_face("sad")
                    $ KittyX.change_stat("love", 70, -5, 1)
                    $ KittyX.change_stat("love", 200, -5)
                    ch_k "Ok, fine. If we're going to do this, stick it in already."
                    $ KittyX.change_stat("obedience", 80, 4)
                    $ KittyX.change_stat("inhibition", 80, 1)
                    $ KittyX.change_stat("inhibition", 60, 3)
                    $ KittyX.Forced = 1
                    jump Kitty_DA_Prep
                else:
                    $ KittyX.change_stat("love", 200, -20)
                    $ KittyX.recent_history.append("angry")
                    $ KittyX.daily_history.append("angry")


    $ KittyX.ArmPose = 1
    if "no_dildo" in KittyX.daily_history:
        ch_k "Learn to take \"no\" for an answer, [KittyX.player_petname]."
        $ KittyX.recent_history.append("angry")
        $ KittyX.daily_history.append("angry")
    elif KittyX.Forced:
        $ KittyX.change_face("angry", 1)
        ch_k "I'm not going to let you use that on me."
        $ KittyX.change_stat("lust", 200, 5)
        if KittyX.love > 300:
            $ KittyX.change_stat("love", 70, -2)
        $ KittyX.change_stat("obedience", 50, -2)
        $ KittyX.recent_history.append("angry")
        $ KittyX.daily_history.append("angry")
    elif Taboo:
        $ KittyX.change_face("angry", 1)
        $ KittyX.recent_history.append("no_taboo")
        $ KittyX.daily_history.append("no_taboo")
        ch_k "Not here!"
        $ KittyX.change_stat("lust", 200, 5)
        $ KittyX.change_stat("obedience", 50, -3)
    elif not KittyX.used_to_anal and "dildo_anal" in KittyX.daily_history:
        $ KittyX.change_face("bemused")
        ch_k "Sorry, I just need a little break back there, [KittyX.player_petname]."
    elif KittyX.action_counter["dildo_ass"]:
        $ KittyX.change_face("sad")
        ch_k "Sorry, you can keep your toys out of there."
    else:
        $ KittyX.change_face("normal", 1)
        ch_k "No way."
    $ KittyX.recent_history.append("no_dildo")
    $ KittyX.daily_history.append("no_dildo")
    $ approval_bonus = 0
    return

label Kitty_DA_Prep:
    if offhand_action == "dildo_anal":
        return

    if not KittyX.Forced and action_context != "auto":
        $ approval_bonus = 20 if KittyX.PantsNum() > 6 else 0
        call Bottoms_Off (KittyX)
        if "angry" in KittyX.recent_history:
            return

    $ approval_bonus = 0
    call Kitty_Pussy_Launch ("dildo_anal")
    if not KittyX.action_counter["dildo_ass"]:
        if KittyX.Forced:
            $ KittyX.change_stat("love", 90, -75)
            $ KittyX.change_stat("obedience", 70, 60)
            $ KittyX.change_stat("inhibition", 80, 35)
        else:
            $ KittyX.change_stat("love", 90, 10)
            $ KittyX.change_stat("obedience", 70, 20)
            $ KittyX.change_stat("inhibition", 80, 45)
    if Taboo:
        $ KittyX.inhibition += int(Taboo/10)
        $ KittyX.lust += int(Taboo/5)


    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ KittyX.DrainWord("no_taboo")
    $ KittyX.DrainWord("no_dildo")
    $ KittyX.recent_history.append("dildo_anal")
    $ KittyX.daily_history.append("dildo_anal")

label Kitty_DA_Cycle:
    while Round > 0:
        call shift_focus (KittyX)
        call Kitty_Pussy_Launch ("dildo_anal")
        $ KittyX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (KittyX)
                    jump Kitty_DA_Cycle

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
                            if KittyX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ KittyX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (KittyX, "tired")
                        "Shift primary action":

                            if KittyX.remaining_actions and multi_action:
                                menu:
                                    "I want to stick a finger in her pussy.":
                                        $ action_context = "shift"
                                        call Kitty_DA_After
                                        call Kitty_Fondle_Pussy
                                    "Just stick a finger in her pussy without asking.":
                                        $ action_context = "auto"
                                        call Kitty_DA_After
                                        call Kitty_Fondle_Pussy
                                    "I want to shift the dildo to her pussy.":
                                        $ action_context = "shift"
                                        call Kitty_DA_After
                                        call Kitty_Dildo_Pussy
                                    "Never Mind":
                                        jump Kitty_DA_Cycle
                            else:
                                call Sex_Basic_Dialog (KittyX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Kitty_DA_After
                            call Offhand_Set
                        "Shift your focus (locked)" if not offhand_action:
                            pass
                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [KittyX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (KittyX)
                                "Ask [KittyX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (KittyX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (KittyX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Kitty_DA_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Kitty_DA_Cycle
                        "Never mind":
                            jump Kitty_DA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Kitty_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Kitty_DA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Kitty_Pos_Reset
                    $ Line = 0
                    jump Kitty_DA_After


        if KittyX.underwear or KittyX.PantsNum() > 6 or KittyX.HoseNum() >= 5:
            call Girl_Undress (KittyX, "auto")

        call shift_focus (KittyX)
        call Sex_Dialog (KittyX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or KittyX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (KittyX)
                if "angry" in KittyX.recent_history:
                    call Kitty_Pos_Reset
                    return
                $ KittyX.change_stat("lust", 200, 5)
                if 100 > KittyX.lust >= 70 and KittyX.session_orgasms < 2:
                    $ KittyX.recent_history.append("unsatisfied")
                    $ KittyX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Kitty_DA_After
                $ Line = "came"

            if KittyX.lust >= 100:

                call Girl_Cumming (KittyX)
                if action_context == "shift" or "angry" in KittyX.recent_history:
                    jump Kitty_DA_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in KittyX.recent_history:
                    "[KittyX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Kitty_DA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if KittyX.SEXP >= 100 or ApprovalCheck(KittyX, 1200, "LO"):
            pass
        elif counter == (5 + KittyX.action_counter["dildo_ass"]):
            $ KittyX.brows = "confused"
            ch_k "What are you even doing down there?"
        elif KittyX.lust >= 80:
            pass
        elif counter == (15 + KittyX.action_counter["dildo_ass"]) and KittyX.SEXP >= 15 and not ApprovalCheck(KittyX, 1500):
            $ KittyX.brows = "confused"
            menu:
                ch_k "[KittyX.player_petname], this is getting uncomfortable, maybe we could try something else."
                "Finish up.":
                    "You let go. . ."
                    jump Kitty_DA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Kitty_DA_After
                "No, this is fun.":
                    if ApprovalCheck(KittyX, 1200) or ApprovalCheck(KittyX, 500, "O"):
                        $ KittyX.change_stat("love", 200, -5)
                        $ KittyX.change_stat("obedience", 50, 3)
                        $ KittyX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ KittyX.change_face("angry", 1)
                        call Kitty_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_k "Well if that's your attitude, I don't need your \"help\"."
                        $ KittyX.change_stat("love", 50, -3, 1)
                        $ KittyX.change_stat("love", 80, -4, 1)
                        $ KittyX.change_stat("obedience", 30, -1, 1)
                        $ KittyX.change_stat("obedience", 50, -1, 1)
                        $ KittyX.recent_history.append("angry")
                        $ KittyX.daily_history.append("angry")
                        jump Kitty_DA_After


        if Round == 10:
            ch_k "It's kind of time to get moving."
        elif Round == 5:
            ch_k "For real[KittyX.like]time's up."


    $ KittyX.change_face("bemused", 0)
    $ Line = 0
    ch_k "Ok, we need to take a break."

label Kitty_DA_After:
    if not action_context:
        call Kitty_Pos_Reset

    $ KittyX.change_face("sexy")

    $ KittyX.action_counter["dildo_ass"] += 1
    $ KittyX.remaining_actions -=1

    call Partner_Like (KittyX, 1)

    if KittyX.action_counter["dildo_ass"] == 1:
        $ KittyX.SEXP += 10
        if not action_context:
            if KittyX.love >= 500 and "unsatisfied" not in KittyX.recent_history:
                if KittyX.used_to_anal:
                    ch_k "That was. . . interesting. . ."
                else:
                    ch_k "Ouch. . ."
            elif KittyX.obedience <= 500 and Player.focus <= 20:
                $ KittyX.change_face("perplexed", 1)
                ch_k "Did you like that?"

    $ approval_bonus = 0


    call checkout
    return



label Kitty_Vibrator_Check:
    if "vibrator" in Player.Inventory:
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in KittyX.Inventory:
        "You ask [KittyX.name] to get out her vibrator."
    else:
        "You don't have one of those on you."
        return 0
    return 1


label Kitty_Footjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (KittyX)
    if KittyX.action_counter["footjob"] >= 7:
        $ approval_bonus += 10
    elif KittyX.action_counter["footjob"] >= 3:
        $ approval_bonus += 7
    elif KittyX.action_counter["footjob"]:
        $ approval_bonus += 3

    if KittyX.addiction >= 75 and KittyX.event_counter["swallowed"] >=3:
        $ approval_bonus += 10
    if KittyX.addiction >= 75:
        $ approval_bonus += 5

    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in KittyX.Traits:
        $ approval_bonus += (3*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in KittyX.Traits:
        $ approval_bonus -= 40
    if KittyX.event_counter["forced"] and not KittyX.Forced:
        $ approval_bonus -= 5*KittyX.event_counter["forced"]

    if Taboo and "no_taboo" in KittyX.daily_history:
        $ approval_bonus -= 10

    if "no_foot" in KittyX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_foot" in KittyX.recent_history else 0

    $ Approval = ApprovalCheck(KittyX, 1250, TabM = 3)

    if action_context == KittyX:
        if Approval > 2:
            "[KittyX.name] leans back and starts rubbing your cock between her feet."
            menu:
                "What do you do?"
                "Nothing.":
                    $ KittyX.change_stat("inhibition", 70, 3)
                    $ KittyX.change_stat("inhibition", 30, 2)
                    "[KittyX.name] continues her actions."
                "Praise her.":
                    $ KittyX.change_face("sexy", 1)
                    $ KittyX.change_stat("inhibition", 70, 3)
                    ch_p "Oooh, that's good, [KittyX.petname]."
                    $ KittyX.nameCheck()
                    "[KittyX.name] continues her actions."
                    $ KittyX.change_stat("love", 80, 1)
                    $ KittyX.change_stat("obedience", 90, 1)
                    $ KittyX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ KittyX.change_face("surprised")
                    $ KittyX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that for now, [KittyX.petname]."
                    $ KittyX.nameCheck()
                    "[KittyX.name] puts it down."
                    $ KittyX.change_stat("obedience", 90, 1)
                    $ KittyX.change_stat("obedience", 50, 1)
                    $ KittyX.change_stat("obedience", 30, 2)
                    return
            if primary_action:
                $ girl_offhand_action = "foot"
                return
            jump Kitty_FJ_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if not KittyX.action_counter["footjob"] and "no_foot" not in KittyX.recent_history:
        $ KittyX.change_face("confused", 2)
        ch_k "Huh, so you'd like me to touch your cock with my feet?"
        $ KittyX.blushing = 1

    if not KittyX.action_counter["footjob"] and Approval:
        if KittyX.Forced:
            $ KittyX.change_face("sad",1)
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
        elif KittyX.love >= (KittyX.obedience + KittyX.inhibition):
            $ KittyX.change_face("sexy",1)
            $ KittyX.brows = "sad"
            $ KittyX.mouth = "smile"
            ch_k "I guess it couldn't hurt. . ."
        elif KittyX.obedience >= KittyX.inhibition:
            $ KittyX.change_face("normal",1)
            ch_k "If you want, [KittyX.player_petname]. . ."
        elif KittyX.addiction >= 50:
            $ KittyX.change_face("manic", 1)
            ch_k "Okay. . ."
        else:
            $ KittyX.change_face("lipbite",1)
            ch_k "Sure. . ."

    elif Approval:
        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
            ch_k "That's all?"
        elif not Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "Um, I guess this is secluded enough. . ."
        elif "foot" in KittyX.recent_history:
            $ KittyX.change_face("sexy", 1)
            ch_k "I'm getting foot cramps. . ."
            jump Kitty_FJ_Prep
        elif "foot" in KittyX.daily_history:
            $ KittyX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Another one?",   
                "You're going to give me calluses.", 
                "Didn't get enough earlier?",
                "My feet are kinda sore from earlier.",
                "My feet are kinda sore from earlier."])
            ch_k "[Line]"
        elif KittyX.action_counter["footjob"] < 3:
            $ KittyX.change_face("sexy", 1)
            $ KittyX.brows = "confused"
            $ KittyX.mouth = "kiss"
            ch_k "Hmm, magic toes. . ."
        else:
            $ KittyX.change_face("sexy", 1)
            $ KittyX.ArmPose = 2
            $ Line = renpy.random.choice(["You want me to use my feet?",                 
                "So you'd like another foot sesh?",                 
                "A little. . . [she rubs her foot along your leg]?", 
                "A little TLC?"])
            ch_k "[Line]"
        $ Line = 0

    if Approval >= 2:
        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("obedience", 90, 1)
            $ KittyX.change_stat("inhibition", 60, 1)
            ch_k "Ok, fine."
        elif "no_foot" in KittyX.daily_history:
            ch_k "OK, geeze!"
        else:
            $ KittyX.change_face("sexy", 1)
            $ KittyX.change_stat("love", 90, 1)
            $ KittyX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Sure, I guess.",                 
                "Ooooookay.",                 
                "Cool, lemme see it.", 
                "I guess I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Heh, ok, ok."])
            ch_k "[Line]"
            $ Line = 0
        $ KittyX.change_stat("obedience", 20, 1)
        $ KittyX.change_stat("obedience", 60, 1)
        $ KittyX.change_stat("inhibition", 70, 2)
        jump Kitty_FJ_Prep
    else:

        $ KittyX.change_face("angry")
        if "no_foot" in KittyX.recent_history:
            ch_k "You don't[KittyX.like]listen do you, [KittyX.player_petname]."
        elif Taboo and "no_taboo" in KittyX.daily_history and "no_foot" in KittyX.daily_history:
            ch_k "I said not in public!"
        elif "no_foot" in KittyX.daily_history:
            ch_k "I told you \"no,\" [KittyX.player_petname]."
        elif Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "I said not in public!"
        elif not KittyX.action_counter["footjob"]:
            $ KittyX.change_face("bemused")
            ch_k "I don't know, [KittyX.player_petname]. . ."
        else:
            $ KittyX.change_face("bemused")
            ch_k "Not now, ok?"
        menu:
            extend ""
            "Sorry, never mind." if "no_foot" in KittyX.daily_history:
                $ KittyX.change_face("bemused")
                ch_k "Yeah."
                return
            "Maybe later?" if "no_foot" not in KittyX.daily_history:
                $ KittyX.change_face("sexy")
                ch_k ". . ."
                ch_k "Maybe."
                $ KittyX.change_stat("love", 80, 2)
                $ KittyX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ KittyX.recent_history.append("no_taboo")
                    $ KittyX.daily_history.append("no_taboo")
                $ KittyX.recent_history.append("no_foot")
                $ KittyX.daily_history.append("no_foot")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ KittyX.change_face("sexy")
                    $ KittyX.change_stat("obedience", 90, 2)
                    $ KittyX.change_stat("obedience", 50, 2)
                    $ KittyX.change_stat("inhibition", 70, 3)
                    $ KittyX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Sure, I guess.",                 
                            "Ooooookay.",                 
                            "Cool, lemme see it.", 
                            "I guess I could. . .",
                            "Ok. . . [She gestures for you to come over].",
                            "Heh, ok, ok."])
                    ch_k "[Line]"
                    $ Line = 0
                    jump Kitty_FJ_Prep
                else:
                    pass
            "Come on, get to work.":

                $ Approval = ApprovalCheck(KittyX, 400, "OI", TabM = 3)
                if Approval > 1 or (Approval and KittyX.Forced):
                    $ KittyX.change_face("sad")
                    $ KittyX.change_stat("love", 70, -5, 1)
                    $ KittyX.change_stat("love", 200, -2)
                    ch_k "Ok, fine."
                    $ KittyX.change_stat("obedience", 50, 4)
                    $ KittyX.change_stat("inhibition", 80, 1)
                    $ KittyX.change_stat("inhibition", 60, 3)
                    $ KittyX.Forced = 1
                    jump Kitty_FJ_Prep
                else:
                    $ KittyX.change_stat("love", 200, -15)
                    $ KittyX.recent_history.append("angry")
                    $ KittyX.daily_history.append("angry")


    $ KittyX.ArmPose = 1
    if "no_foot" in KittyX.daily_history:
        $ KittyX.change_face("angry", 1)
        ch_k "I'm not telling you again."
        $ KittyX.recent_history.append("angry")
        $ KittyX.daily_history.append("angry")
    elif KittyX.Forced:
        $ KittyX.change_face("angry", 1)
        ch_k "I don't even want to step on it."
        $ KittyX.change_stat("lust", 200, 5)
        if KittyX.love > 300:
            $ KittyX.change_stat("love", 70, -2)
        $ KittyX.change_stat("obedience", 50, -2)
        $ KittyX.recent_history.append("angry")
        $ KittyX.daily_history.append("angry")
    elif Taboo:
        $ KittyX.change_face("angry", 1)
        $ KittyX.daily_history.append("no_taboo")
        ch_k "Not here, not anywhere near here."
        $ KittyX.change_stat("lust", 200, 5)
        $ KittyX.change_stat("obedience", 50, -3)
    elif KittyX.action_counter["footjob"]:
        $ KittyX.change_face("sad")
        ch_k "I'm not feeling it today. . ."
    else:
        $ KittyX.change_face("normal", 1)
        ch_k "I don't know about using my feet for. . . that."
    $ KittyX.recent_history.append("no_foot")
    $ KittyX.daily_history.append("no_foot")
    $ approval_bonus = 0
    return


label Kitty_FJ_Prep:
    if offhand_action == "foot":
        return

    if Taboo:
        $ KittyX.inhibition += int(Taboo/10)
        $ KittyX.lust += int(Taboo/5)

    $ KittyX.change_face("sexy")
    if KittyX.Forced:
        $ KittyX.change_face("sad")
    elif not KittyX.action_counter["footjob"]:
        $ KittyX.brows = "confused"
        $ KittyX.eyes = "sexy"
        $ KittyX.mouth = "smile"

    call Seen_First_Peen (KittyX, Partner, React=action_context)

    if not KittyX.action_counter["footjob"]:
        if KittyX.Forced:
            $ KittyX.change_stat("love", 90, -20)
            $ KittyX.change_stat("obedience", 70, 25)
            $ KittyX.change_stat("inhibition", 80, 30)
        else:
            $ KittyX.change_stat("love", 90, 5)
            $ KittyX.change_stat("obedience", 70, 20)
            $ KittyX.change_stat("inhibition", 80, 20)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ KittyX.DrainWord("no_taboo")
    $ KittyX.DrainWord("no_foot")
    $ KittyX.recent_history.append("foot")
    $ KittyX.daily_history.append("foot")

label Kitty_FJ_Cycle:
    while Round > 0:
        call shift_focus (KittyX)
        call Kitty_Sex_Launch ("foot")
        $ KittyX.lust_face()

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
                "Turn her Around":

                    $ KittyX.pose = "doggy" if KittyX.pose != "doggy" else "sex"
                    "You turn her around. . ."
                    jump Kitty_FJ_Cycle
                "Other options":

                    menu:
                        "Offhand action":
                            if KittyX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ KittyX.remaining_actions -= 1
                            else:
                                ch_k "I kinda need a break, so if we could wrap this up?"
                        "Shift primary action":

                            if KittyX.remaining_actions and multi_action:
                                menu:
                                    "How about a blowjob?":
                                        if KittyX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Kitty_FJ_After
                                            call Kitty_Blowjob
                                        else:
                                            ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."
                                    "How about a handjob?":
                                        if KittyX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Kitty_FJ_After
                                            call Kitty_Handjob
                                        else:
                                            ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."
                                    "Never Mind":











                                        jump Kitty_FJ_Cycle
                            else:
                                call Sex_Basic_Dialog (KittyX, "tired")

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [KittyX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (KittyX)
                                "Ask [KittyX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (KittyX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (KittyX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Kitty_FJ_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Kitty_FJ_Cycle
                                "Never mind":
                                    jump Kitty_FJ_Cycle
                        "Undress [KittyX.name]":
                            call Girl_Undress (KittyX)
                        "Clean up [KittyX.name] (locked)" if not KittyX.Spunk:
                            pass
                        "Clean up [KittyX.name]" if KittyX.Spunk:
                            call Girl_Cleanup (KittyX, "ask")
                        "Never mind":
                            jump Kitty_FJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Kitty_Sex_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Kitty_FJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Kitty_Sex_Reset
                    $ Line = 0
                    jump Kitty_FJ_After


        call shift_focus (KittyX)
        call Sex_Dialog (KittyX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or KittyX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (KittyX)
                if "angry" in KittyX.recent_history:
                    call Kitty_Sex_Reset
                    return
                $ KittyX.change_stat("lust", 200, 5)
                if 100 > KittyX.lust >= 70 and KittyX.session_orgasms < 2:
                    $ KittyX.recent_history.append("unsatisfied")
                    $ KittyX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Kitty_FJ_After
                $ Line = "came"

            if KittyX.lust >= 100:

                call Girl_Cumming (KittyX)
                if action_context == "shift" or "angry" in KittyX.recent_history:
                    jump Kitty_FJ_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in KittyX.recent_history:
                    "[KittyX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Kitty_FJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if counter == 20:
            $ KittyX.brows = "angry"
            menu:
                ch_k "Ouch, foot cramp, can we[KittyX.like]take a break?"
                "How about a BJ?" if KittyX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Kitty_FJ_After
                    call Kitty_Blowjob
                "How about a Handy?" if KittyX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Kitty_FJ_After
                    call Kitty_Handjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    $ counter += 1
                    "[Line]"
                    jump Kitty_FJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Kitty_Sex_Reset
                    $ action_context = "shift"
                    jump Kitty_FJ_After
                "No, get back down there.":
                    if ApprovalCheck(KittyX, 1200) or ApprovalCheck(KittyX, 500, "O"):
                        $ KittyX.change_stat("love", 200, -5)
                        $ KittyX.change_stat("obedience", 50, 3)
                        $ KittyX.change_stat("obedience", 80, 2)
                        "She grumbles but gets back to work."
                    else:
                        $ KittyX.change_face("angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        ch_k "Hey, I've got better things to do if you're[KittyX.like]going to be a dick about it."
                        $ KittyX.change_stat("love", 50, -3, 1)
                        $ KittyX.change_stat("love", 80, -4, 1)
                        $ KittyX.change_stat("obedience", 30, -1, 1)
                        $ KittyX.change_stat("obedience", 50, -1, 1)
                        $ KittyX.recent_history.append("angry")
                        $ KittyX.daily_history.append("angry")
                        jump Kitty_FJ_After
        elif counter == 10 and KittyX.SEXP <= 100 and not ApprovalCheck(KittyX, 1200, "LO"):
            $ KittyX.brows = "confused"
            ch_k "Can we[KittyX.Like]be done with this now? I'm getting sore."


        call Escalation (KittyX)

        if Round == 10:
            ch_k "It's kind of time to get moving."
        elif Round == 5:
            ch_k "For real[KittyX.like]time's up."


    $ KittyX.change_face("bemused", 0)
    $ Line = 0
    ch_k "Ok, we need to take a break."

label Kitty_FJ_After:
    $ KittyX.change_face("sexy")

    $ KittyX.action_counter["footjob"] += 1
    $ KittyX.remaining_actions -=1
    $ KittyX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ KittyX.addiction_rate += 1
    $ KittyX.change_stat("lust", 90, 5)

    call Partner_Like (KittyX, 1)

    if "Kittypedi" in Achievements:
        pass
    elif KittyX.action_counter["footjob"] >= 10:
        $ KittyX.change_face("smile", 1)
        ch_k "I guess I've gotten pretty smooth at the \"Kittypedi.\""
        $ Achievements.append("Kittypedi")
        $ KittyX.SEXP += 5
    elif KittyX.action_counter["footjob"] == 1:
        $ KittyX.SEXP += 10
        if KittyX.love >= 500:
            $ KittyX.mouth = "smile"
            ch_k "I could feel you down there. . ."
        elif Player.focus <= 20:
            $ KittyX.mouth = "sad"
            ch_k "Did that work out for you?"
    elif KittyX.action_counter["footjob"] == 5:
        ch_k "Let me know any time you need me to \"foot you up.\""

    $ approval_bonus = 0
    if action_context == "shift":
        ch_k "Ok, so what were you thinking?"
    else:
        call Kitty_Sex_Reset
    call checkout
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
