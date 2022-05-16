
label Jean_Fondle:

    $ JeanX.mouth = "smile"
    if not JeanX.remaining_actions:
        ch_j "Gimme a minute, k?"
        return
    menu:
        ch_j "Well? Where did you want to touch, [JeanX.player_petname]?"
        "Your breasts?" if JeanX.remaining_actions:
            jump Jean_Fondle_Breasts
        "Your thighs?" if JeanX.remaining_actions:
            jump Jean_Fondle_Thighs
        "Your pussy?" if JeanX.remaining_actions:
            jump Jean_Fondle_Pussy
        "Your Ass?" if JeanX.remaining_actions:
            jump Jean_Fondle_Ass
        "Never mind.":
            return
    return



label Jean_Fondle_Breasts:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JeanX)


    if JeanX.action_counter["fondle_breasts"]:
        $ approval_bonus += 15
    if JeanX.lust > 75:
        $ approval_bonus += 20
    if "exhibitionist" in JeanX.Traits:
        $ approval_bonus += (3*JeanX.Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JeanX.Traits:
        $ approval_bonus -= 20
    if JeanX.event_counter["forced"] and not JeanX.Forced:
        $ approval_bonus -= 5*JeanX.event_counter["forced"]

    if JeanX.Taboo and "no_taboo" in JeanX.daily_history:
        $ approval_bonus -= 10
    if JeanX.Taboo and "public" not in JeanX.history:
        $ approval_bonus -= 20

    if "no_fondle breasts" in JeanX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle breasts" in JeanX.recent_history else 0

    $ Approval = ApprovalCheck(JeanX, 950, TabM = 3)

    if action_context == "auto":
        if Approval:
            $ JeanX.change_face("sexy")
            $ JeanX.change_stat("obedience", 90, 1)
            $ JeanX.change_stat("obedience", 70, 2)
            $ JeanX.change_stat("inhibition", 70, 3)
            $ JeanX.change_stat("inhibition", 30, 2)
            "As you cup her breast, [JeanX.name] gently nods."
            jump Jean_FB_Prep
        else:
            $ JeanX.change_face("surprised")
            $ JeanX.brows = "confused"
            $ JeanX.change_stat("obedience", 50, -2)
            ch_j "Not so fast, [JeanX.player_petname]. . ."
            $ approval_bonus = 0
            $ offhand_action = 0
            return



    if Approval:
        $ JeanX.change_face("sexy", 1)
        if JeanX.Forced:
            $ JeanX.change_face("sad")
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
        elif not JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "I guess. . . maybe we could do it here. . ."

    if "fondle_breasts" in JeanX.recent_history:
        $ JeanX.change_face("sexy", 1)
        ch_j "Mmmm, again? I guess. . ."
        jump Jean_FB_Prep
    elif "fondle_breasts" in JeanX.daily_history:
        $ JeanX.change_face("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Chill. . .",
            "Mmm. . ."])
        ch_j "[Line]"

    if Approval >= 2:
        $ JeanX.change_face("bemused", 1)
        if JeanX.Forced:
            $ JeanX.change_face("sad")
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
            $ JeanX.change_stat("obedience", 90, 1)
            $ JeanX.change_stat("inhibition", 60, 1)
        ch_j "Sure, sounds fun."
        $ JeanX.change_stat("love", 90, 1)
        $ JeanX.change_stat("inhibition", 50, 3)
        jump Jean_FB_Prep
    else:

        $ JeanX.change_face("angry", 1)
        if "no_fondle breasts" in JeanX.recent_history:
            ch_j "I'm not used to repeating myself."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history and "no_fondle breasts" in JeanX.daily_history:
            ch_j "I've had enough of this today."
        elif "no_fondle breasts" in JeanX.daily_history:
            ch_j "Don't ask me again today."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "I told you. . . not here, [JeanX.player_petname]."
        elif not JeanX.action_counter["fondle_breasts"]:
            $ JeanX.change_face("bemused")
            ch_j "Look, don't touch, [JeanX.player_petname]. . ."
        else:
            $ JeanX.change_face("bemused")
            ch_j "Yeah, you wish."
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle breasts" in JeanX.daily_history:
                $ JeanX.change_face("bemused")
                ch_j "It's fine, I get it."
                return
            "Maybe later?" if "no_fondle breasts" not in JeanX.daily_history:
                $ JeanX.change_face("sexy")
                ch_j ". . . I guess? Maybe."
                $ JeanX.change_stat("love", 80, 1)
                $ JeanX.change_stat("love", 50, 1)
                $ JeanX.change_stat("inhibition", 30, 2)
                if JeanX.Taboo:
                    $ JeanX.recent_history.append("no_taboo")
                    $ JeanX.daily_history.append("no_taboo")
                $ JeanX.recent_history.append("no_fondle breasts")
                $ JeanX.daily_history.append("no_fondle breasts")
                return
            "Come on, Please?":
                if Approval:
                    $ JeanX.change_face("sexy")
                    $ JeanX.change_stat("obedience", 50, 2)
                    $ JeanX.change_stat("inhibition", 60, 3)
                    $ JeanX.change_stat("inhibition", 30, 2)
                    ch_j "Oh, fine, just don't start crying."
                    jump Jean_FB_Prep
                else:
                    $ JeanX.change_face("sexy")
                    ch_j "No way."
            "[[Grab her chest anyway]":


                $ Approval = ApprovalCheck(JeanX, 350, "OI", TabM = 3)
                if Approval > 1 or (Approval and JeanX.Forced):
                    $ JeanX.change_face("sad")
                    $ JeanX.change_stat("love", 70, -5, 1)
                    $ JeanX.change_stat("love", 20, -2, 1)
                    ch_j "Hey. . ."
                    ch_j ". . .whatever. . ."
                    $ JeanX.change_stat("obedience", 90, 2)
                    $ JeanX.change_stat("obedience", 50, 4)
                    $ JeanX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ JeanX.Forced = 1
                    jump Jean_FB_Prep
                else:
                    $ JeanX.change_stat("love", 200, -10)
                    $ JeanX.change_face("angry", 1)
                    "She slaps your hand away."
                    $ JeanX.recent_history.append("angry")
                    $ JeanX.daily_history.append("angry")

    if "no_fondle breasts" in JeanX.daily_history:
        ch_j "I don't want to have to go through this again."
        $ JeanX.recent_history.append("angry")
        $ JeanX.daily_history.append("angry")
    elif JeanX.Forced:
        $ JeanX.change_face("angry", 1)
        ch_j "No."
        $ JeanX.change_stat("lust", 60, 5)
        $ JeanX.change_stat("obedience", 50, -2)
        $ JeanX.recent_history.append("angry")
        $ JeanX.daily_history.append("angry")
    elif JeanX.Taboo:
        $ JeanX.change_face("angry", 1)
        $ JeanX.recent_history.append("no_taboo")
        $ JeanX.daily_history.append("no_taboo")
        ch_j "I'm. . . not comfortable. . . in public. . ."
    elif JeanX.action_counter["fondle_breasts"]:
        $ JeanX.change_face("sad")
        ch_j "We've had enough of that."
    else:
        $ JeanX.change_face("sexy")
        $ JeanX.mouth = "sad"
        ch_j "No."
    $ JeanX.recent_history.append("no_fondle breasts")
    $ JeanX.daily_history.append("no_fondle breasts")
    $ approval_bonus = 0
    return


label Jean_FB_Prep:
    if primary_action == "kiss":
        $ primary_action = "fondle_breasts"
        return

    if offhand_action == "fondle_breasts":
        return

    call Jean_Breasts_Launch ("fondle_breasts")

    if action_context == JeanX:

        $ action_context = 0
        if (JeanX.top or JeanX.bra) and not JeanX.Uptop:

            if ApprovalCheck(JeanX, 1250, TabM = 1) or (JeanX.SeenChest and ApprovalCheck(JeanX, 500) and not JeanX.Taboo):
                $ JeanX.Uptop = 1
                $ Line = JeanX.top if JeanX.top else JeanX.bra
                "With a hungry grin, [JeanX.name] pulls her [Line] up over her breasts."
                call Jean_First_Topless (1)
                $ Line = 0
                "She then grabs your arm and mashes your hand against her breast, clearly intending you to get to work."
            else:
                "[JeanX.name] grabs your arm and mashes your hand against her covered breast, clearly intending you to get to work."
        else:
            "[JeanX.name] grabs your arm and mashes your hand against her breast, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ JeanX.change_stat("inhibition", 80, 3)
                $ JeanX.change_stat("inhibition", 50, 2)
                "You start to fondle it."
            "Praise her.":
                $ JeanX.change_face("sexy", 1)
                $ JeanX.change_stat("inhibition", 80, 3)
                ch_p "I like the initiative, [JeanX.petname]."
                $ JeanX.nameCheck()
                "You start to fondle it."
                $ JeanX.change_stat("love", 85, 1)
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your hand back."
                $ JeanX.change_face("surprised")
                $ JeanX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [JeanX.petname]."
                $ JeanX.nameCheck()
                $ JeanX.change_stat("love", 70, -3)
                "[JeanX.name] pulls back."
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("obedience", 50, 1)
                $ JeanX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ JeanX.AddWord(1,"refused","refused")
                return


    if not JeanX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Top_Off (JeanX)
        if "angry" in JeanX.recent_history:
            return

    $ approval_bonus = 0
    if not JeanX.action_counter["fondle_breasts"]:
        if JeanX.Forced:
            $ JeanX.change_stat("love", 90, -20)
            $ JeanX.change_stat("obedience", 70, 25)
            $ JeanX.change_stat("inhibition", 80, 15)
        else:
            $ JeanX.change_stat("love", 90, 10)
            $ JeanX.change_stat("obedience", 70, 5)
            $ JeanX.change_stat("inhibition", 80, 15)

    if JeanX.Taboo:
        $ JeanX.change_stat("inhibition", 200, (int(Taboo/10)))
        $ JeanX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if JeanX.Taboo:
        $ JeanX.DrainWord("no_taboo")
    $ JeanX.DrainWord("no_fondle breasts")
    $ JeanX.recent_history.append("fondle_breasts")
    $ JeanX.daily_history.append("fondle_breasts")
    call Jean_Breasts_Launch ("fondle_breasts")

label Jean_FB_Cycle:
    while Round > 0:
        call ViewShift (JeanX, JeanX.pose, 0, "fondle_breasts")
        call shift_focus (JeanX)
        $ JeanX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (JeanX)
                    $ counter += 1
                    $ Round -= 1
                    jump Jean_FB_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (JeanX, "menu")
                    jump Jean_FB_Cycle
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
                                    "Ask to suck on them.":
                                        if JeanX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Jean_FB_After
                                            call Jean_Suck_Breasts
                                        else:
                                            call Sex_Basic_Dialog (JeanX, "tired")
                                    "Just suck on them without asking.":
                                        if JeanX.remaining_actions and multi_action:
                                            $ action_context = "auto"
                                            call Jean_FB_After
                                            call Jean_Suck_Breasts
                                        else:
                                            "As you lean in to suck on her breast, she grabs your head and pushes back."
                                            call Sex_Basic_Dialog (JeanX, "tired")
                                    "Never Mind":
                                        jump Jean_FB_Cycle
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
                                    jump Jean_FB_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jean_FB_Cycle
                                "Never mind":
                                    jump Jean_FB_Cycle

                        "Show her feet" if not ShowFeet and (JeanX.pose == "doggy" or JeanX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (JeanX.pose == "doggy" or JeanX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [JeanX.name]":

                            call Girl_Undress (JeanX)
                        "Clean up [JeanX.name] (locked)" if not JeanX.Spunk:
                            pass
                        "Clean up [JeanX.name]" if JeanX.Spunk:
                            call Girl_Cleanup (JeanX, "ask")
                        "Never mind":
                            jump Jean_FB_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jean_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jean_FB_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jean_Pos_Reset
                    $ Line = 0
                    jump Jean_FB_After


        call shift_focus (JeanX)
        call Sex_Dialog (JeanX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or JeanX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (JeanX)
                if "angry" in JeanX.recent_history:
                    call Jean_Pos_Reset
                    return
                $ JeanX.change_stat("lust", 200, 5)
                if 100 > JeanX.lust >= 70 and JeanX.session_orgasms < 2:
                    $ JeanX.recent_history.append("unsatisfied")
                    $ JeanX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jean_FB_After
                $ Line = "came"

            if JeanX.lust >= 100:

                call Girl_Cumming (JeanX)
                if action_context == "shift" or "angry" in JeanX.recent_history:
                    jump Jean_FB_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in JeanX.recent_history and JeanX.SEXP >= 20:
                    "[JeanX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Jean_FB_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if JeanX.SEXP >= 100 or ApprovalCheck(JeanX, 1200, "LO"):
            pass
        elif counter == (5 + JeanX.action_counter["fondle_breasts"]):
            $ JeanX.brows = "confused"
            ch_j "Having fun there?"
        elif JeanX.lust >= 85:
            pass
        elif counter == (15 + JeanX.action_counter["fondle_breasts"]) and JeanX.SEXP >= 15 and not ApprovalCheck(JeanX, 1500):
            $ JeanX.brows = "confused"
            menu:
                ch_j "Maybe it's time for something else, [JeanX.player_petname]?"
                "Finish up.":
                    "You let go. . ."
                    jump Jean_FB_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Jean_FB_After
                "No, this is fun.":
                    if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                        $ JeanX.change_stat("love", 200, -5)
                        $ JeanX.change_stat("obedience", 50, 3)
                        $ JeanX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ JeanX.change_face("angry", 1)
                        call Jean_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_j "Well, I've got better things to be doing."
                        $ JeanX.change_stat("love", 50, -3, 1)
                        $ JeanX.change_stat("love", 80, -4, 1)
                        $ JeanX.change_stat("obedience", 30, -1, 1)
                        $ JeanX.change_stat("obedience", 50, -1, 1)
                        $ JeanX.recent_history.append("angry")
                        $ JeanX.daily_history.append("angry")
                        jump Jean_FB_After


        call Escalation (JeanX)

        if Round == 10:
            call Sex_Basic_Dialog (JeanX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JeanX, 5)

        if JeanX.lust >= 50 and not JeanX.Uptop and (JeanX.bra or JeanX.top):
            $ JeanX.Uptop = 1
            "[JeanX.name] grunts and pulls her clothes aside."
            call Jean_First_Topless


    $ JeanX.change_face("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JeanX, "done")

label Jean_FB_After:
    if not action_context:
        call Jean_Pos_Reset

    $ JeanX.change_face("sexy")

    $ JeanX.action_counter["fondle_breasts"]+= 1
    $ JeanX.remaining_actions -=1
    $ JeanX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ JeanX.addiction_rate += 1

    call Partner_Like (JeanX, 2)

    if JeanX.action_counter["fondle_breasts"]== 1:
        $ JeanX.SEXP += 4
        if not action_context:
            if JeanX.love >= 500 and "unsatisfied" not in JeanX.recent_history:
                ch_j "I bet you enjoyed that."
            elif JeanX.obedience <= 500 and Player.focus <= 20:
                $ JeanX.change_face("perplexed", 1)
                ch_j "You get what you wanted out of that?"

    $ approval_bonus = 0


    call Checkout
    return






label Jean_Suck_Breasts:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JeanX)

    if JeanX.action_counter["suck_breasts"]:
        $ approval_bonus += 15
    if not JeanX.bra and not JeanX.top:
        $ approval_bonus += 15
    if JeanX.lust > 75:
        $ approval_bonus += 20
    if JeanX.lust > 75 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in JeanX.Traits:
        $ approval_bonus += (4*JeanX.Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JeanX.Traits:
        $ approval_bonus -= 25
    if JeanX.event_counter["forced"] and not JeanX.Forced:
        $ approval_bonus -= 5*JeanX.event_counter["forced"]

    if JeanX.Taboo and "no_taboo" in JeanX.daily_history:
        $ approval_bonus -= 10
    if JeanX.Taboo and "public" not in JeanX.history:
        $ approval_bonus -= 20

    if "no_suck breasts" in JeanX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_suck breasts" in JeanX.recent_history else 0

    $ Approval = ApprovalCheck(JeanX, 1050, TabM = 4)

    if action_context == "auto":
        if Approval:
            $ JeanX.change_face("sexy")
            $ JeanX.change_stat("obedience", 90, 1)
            $ JeanX.change_stat("obedience", 70, 2)
            $ JeanX.change_stat("inhibition", 70, 3)
            $ JeanX.change_stat("inhibition", 30, 2)
            "As you dive in, [JeanX.name] seems a bit surprised, but just makes a little \"grunt.\""
            jump Jean_SB_Prep
        else:
            $ JeanX.change_face("surprised")
            $ JeanX.change_stat("obedience", 50, -2)
            ch_j "Not so fast, [JeanX.player_petname]. . ."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "suck_breasts" in JeanX.recent_history:
        $ JeanX.change_face("sexy", 1)
        ch_j "Mmmm, again? I guess. . ."
        jump Jean_SB_Prep
    elif "suck_breasts" in JeanX.daily_history:
        $ JeanX.change_face("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Chill. . .",
            "Mmm. . ."])
        ch_j "[Line]"

    if Approval >= 2:
        $ JeanX.change_face("bemused", 1)
        if JeanX.Forced:
            $ JeanX.change_face("sad")
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
            $ JeanX.change_stat("obedience", 90, 1)
            $ JeanX.change_stat("inhibition", 60, 1)
        ch_j "Sure."
        $ JeanX.change_stat("love", 90, 1)
        $ JeanX.change_stat("inhibition", 50, 3)
        jump Jean_SB_Prep
    else:

        $ JeanX.change_face("angry", 1)
        if "no_suck breasts" in JeanX.recent_history:
            ch_j "I'm not used to repeating myself."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history and "no_suck breasts" in JeanX.daily_history:
            ch_j "I told you, I'm not comfortable in public."
        elif "no_suck breasts" in JeanX.daily_history:
            ch_j "Don't ask me again today."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "I told you. . . not here, [JeanX.player_petname]."
        elif not JeanX.action_counter["suck_breasts"]:
            $ JeanX.change_face("bemused")
            ch_j "Let's work up to that maybe. ."
        else:
            $ JeanX.change_face("bemused")
            ch_j "You wish."
        menu:
            extend ""
            "Sorry, never mind." if "no_suck breasts" in JeanX.daily_history:
                $ JeanX.change_face("bemused")
                ch_j "It's fine, I get it."
                return
            "Maybe later?" if "no_suck breasts" not in JeanX.daily_history:
                $ JeanX.change_face("sexy")
                ch_j ". . . I guess? Maybe."
                $ JeanX.change_stat("love", 80, 1)
                $ JeanX.change_stat("love", 50, 1)
                $ JeanX.change_stat("inhibition", 30, 2)
                if JeanX.Taboo:
                    $ JeanX.recent_history.append("no_taboo")
                    $ JeanX.daily_history.append("no_taboo")
                $ JeanX.recent_history.append("no_suck breasts")
                $ JeanX.daily_history.append("no_suck breasts")
                return
            "Come on, Please?":
                if Approval:
                    $ JeanX.change_face("sexy")
                    $ JeanX.change_stat("obedience", 90, 1)
                    $ JeanX.change_stat("obedience", 50, 2)
                    $ JeanX.change_stat("inhibition", 60, 3)
                    $ JeanX.change_stat("inhibition", 30, 2)
                    ch_j "Oh, fine, just don't start crying."
                    jump Jean_SB_Prep
                else:
                    $ JeanX.change_face("sexy")
                    ch_j "Oh, don't cry."
            "[[Start sucking anyway]":

                $ Approval = ApprovalCheck(JeanX, 450, "OI", TabM = 3)
                if Approval > 1 or (Approval and JeanX.Forced):
                    $ JeanX.change_face("sad")
                    $ JeanX.change_stat("love", 70, -5, 1)
                    $ JeanX.change_stat("love", 20, -2, 1)
                    ch_j ". . .whatever. . ."
                    $ JeanX.change_stat("obedience", 90, 2)
                    $ JeanX.change_stat("obedience", 50, 4)
                    $ JeanX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ JeanX.Forced = 1
                    jump Jean_SB_Prep
                else:
                    $ JeanX.change_stat("love", 200, -10)
                    $ JeanX.change_face("angry", 1)
                    "She shoves your head back out."
                    $ JeanX.recent_history.append("angry")
                    $ JeanX.daily_history.append("angry")

    if "no_suck breasts" in JeanX.daily_history:
        ch_j "I don't want to have to go through this again."
        $ JeanX.recent_history.append("angry")
        $ JeanX.daily_history.append("angry")
    elif JeanX.Forced:
        $ JeanX.change_face("angry", 1)
        ch_j ". . . no, not worth it."
        $ JeanX.change_stat("lust", 60, 5)
        $ JeanX.change_stat("obedience", 50, -2)
        $ JeanX.recent_history.append("angry")
        $ JeanX.daily_history.append("angry")
    elif JeanX.Taboo:
        $ JeanX.change_face("angry", 1)
        $ JeanX.recent_history.append("no_taboo")
        $ JeanX.daily_history.append("no_taboo")
        ch_j "I'm. . . not comfortable. . . in public. . ."
    elif JeanX.action_counter["suck_breasts"]:
        $ JeanX.change_face("sad")
        ch_j "We've had enough of that."
    else:
        $ JeanX.change_face("sexy")
        $ JeanX.mouth = "sad"
        ch_j "No."
    $ JeanX.recent_history.append("no_suck breasts")
    $ JeanX.daily_history.append("no_suck breasts")
    $ approval_bonus = 0
    return


label Jean_SB_Prep:

    if offhand_action == "suck_breasts":
        return

    call Jean_Breasts_Launch ("suck_breasts")

    if action_context == JeanX:

        $ action_context = 0
        if (JeanX.top or JeanX.bra) and not JeanX.Uptop:

            if ApprovalCheck(JeanX, 1250, TabM = 1) or (JeanX.SeenChest and ApprovalCheck(JeanX, 500) and not JeanX.Taboo):
                $ JeanX.Uptop = 1
                $ Line = JeanX.top if JeanX.top else JeanX.bra
                "With a hungry grin, [JeanX.name] pulls her [Line] up over her breasts."
                call Jean_First_Topless (1)
                $ Line = 0
                "She then grabs your head and crams your face into her chest, clearly intending you to get to work."
            else:
                "[JeanX.name] grabs your head and crams your face into her chest, clearly intending you to get to work."
        else:
            "[JeanX.name] grabs your head and crams your face into her chest, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ JeanX.change_stat("inhibition", 80, 3)
                $ JeanX.change_stat("inhibition", 50, 2)
                "You start to run your tongue along her nipple."
            "Praise her.":
                $ JeanX.change_face("sexy", 1)
                $ JeanX.change_stat("inhibition", 80, 3)
                ch_p "Mmm, I like this, [JeanX.petname]."
                $ JeanX.nameCheck()
                "You start to fondle it."
                $ JeanX.change_stat("love", 85, 1)
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your head back."
                $ JeanX.change_face("surprised")
                $ JeanX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [JeanX.petname]."
                $ JeanX.nameCheck()
                $ JeanX.change_stat("love", 70, -4)
                "[JeanX.name] pulls away."
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("obedience", 50, 1)
                $ JeanX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ JeanX.AddWord(1,"refused","refused")
                return


    if not JeanX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Top_Off (JeanX)
        if "angry" in JeanX.recent_history:
            return

    $ approval_bonus = 0
    if not JeanX.action_counter["suck_breasts"]:
        if JeanX.Forced:
            $ JeanX.change_stat("love", 90, -25)
            $ JeanX.change_stat("obedience", 70, 25)
            $ JeanX.change_stat("inhibition", 80, 17)
        else:
            $ JeanX.change_stat("love", 90, 10)
            $ JeanX.change_stat("obedience", 70, 10)
            $ JeanX.change_stat("inhibition", 80, 15)

    if JeanX.Taboo:
        $ JeanX.change_stat("inhibition", 200, (int(Taboo/10)))
        $ JeanX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if JeanX.Taboo:
        $ JeanX.DrainWord("no_taboo")
    $ JeanX.DrainWord("no_suck breasts")
    $ JeanX.recent_history.append("suck_breasts")
    $ JeanX.daily_history.append("suck_breasts")
    call Jean_Breasts_Launch ("suck_breasts")

label Jean_SB_Cycle:
    if offhand_action == "kiss":
        $ offhand_action = 0
    while Round > 0:
        call ViewShift (JeanX, JeanX.pose, 0, "suck_breasts")
        call shift_focus (JeanX)
        $ JeanX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (JeanX)
                    $ counter += 1
                    $ Round -= 1
                    jump Jean_SB_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (JeanX, "menu")
                    jump Jean_SB_Cycle
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
                                    "Pull back to fondling.":
                                        if JeanX.remaining_actions and multi_action:
                                            $ action_context = "pullback"
                                            call Jean_SB_After
                                            call Jean_Fondle_Breasts
                                        else:
                                            "As you pull back, [JeanX.name] pushes you back in close."
                                            call Sex_Basic_Dialog (JeanX, "tired")
                                    "Never Mind":
                                        jump Jean_SB_Cycle
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
                                    jump Jean_SB_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jean_SB_Cycle
                                "Never mind":
                                    jump Jean_SB_Cycle

                        "Show her feet" if not ShowFeet and (JeanX.pose == "doggy" or JeanX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (JeanX.pose == "doggy" or JeanX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [JeanX.name]":

                            call Girl_Undress (JeanX)
                        "Clean up [JeanX.name] (locked)" if not JeanX.Spunk:
                            pass
                        "Clean up [JeanX.name]" if JeanX.Spunk:
                            call Girl_Cleanup (JeanX, "ask")
                        "Never mind":
                            jump Jean_SB_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jean_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jean_SB_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jean_Pos_Reset
                    $ Line = 0
                    jump Jean_SB_After


        call shift_focus (JeanX)
        call Sex_Dialog (JeanX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or JeanX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (JeanX)
                if "angry" in JeanX.recent_history:
                    call Jean_Pos_Reset
                    return
                $ JeanX.change_stat("lust", 200, 5)
                if 100 > JeanX.lust >= 70 and JeanX.session_orgasms < 2:
                    $ JeanX.recent_history.append("unsatisfied")
                    $ JeanX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jean_SB_After
                $ Line = "came"

            if JeanX.lust >= 100:

                call Girl_Cumming (JeanX)
                if action_context == "shift" or "angry" in JeanX.recent_history:
                    jump Jean_SB_After

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
                            jump Jean_SB_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if JeanX.SEXP >= 100 or ApprovalCheck(JeanX, 1200, "LO"):
            pass
        elif counter == (5 + JeanX.action_counter["suck_breasts"]):
            $ JeanX.brows = "sly"
            ch_j "This is kinda nice. . ."
        elif JeanX.lust >= 85:
            pass
        elif counter == (15 + JeanX.action_counter["suck_breasts"]) and JeanX.SEXP >= 15 and not ApprovalCheck(JeanX, 1500):
            $ JeanX.brows = "confused"
            menu:
                ch_j "Maybe try something else?"
                "Finish up.":
                    "You let go. . ."
                    jump Jean_SB_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Jean_SB_After
                "No, this is fun.":
                    if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                        $ JeanX.change_stat("love", 200, -5)
                        $ JeanX.change_stat("obedience", 50, 3)
                        $ JeanX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ JeanX.change_face("angry", 1)
                        call Jean_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_j "Well -I'm- bored."
                        $ JeanX.change_stat("love", 50, -3, 1)
                        $ JeanX.change_stat("love", 80, -4, 1)
                        $ JeanX.change_stat("obedience", 30, -1, 1)
                        $ JeanX.change_stat("obedience", 50, -1, 1)
                        $ JeanX.recent_history.append("angry")
                        $ JeanX.daily_history.append("angry")
                        jump Jean_SB_After


        call Escalation (JeanX)

        if Round == 10:
            call Sex_Basic_Dialog (JeanX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JeanX, 5)

        if JeanX.lust >= 50 and not JeanX.Uptop and (JeanX.bra or JeanX.top):
            $ JeanX.Uptop = 1
            "[JeanX.name] grunts and pulls her clothes aside."
            call Jean_First_Topless


    $ JeanX.change_face("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JeanX, "done")

label Jean_SB_After:
    if not action_context:
        call Jean_Pos_Reset

    $ JeanX.change_face("sexy")

    $ JeanX.action_counter["suck_breasts"] += 1
    $ JeanX.remaining_actions -=1
    $ JeanX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ JeanX.addiction_rate += 1

    if Partner == "Kitty":
        call Partner_Like (JeanX, 2, 2)
    else:
        call Partner_Like (JeanX, 2)

    if JeanX.action_counter["suck_breasts"] == 1:
        $ JeanX.SEXP += 4
        if not action_context:
            if JeanX.love >= 500 and "unsatisfied" not in JeanX.recent_history:
                ch_j "Well that was fun."
            elif JeanX.obedience <= 500 and Player.focus <= 20:
                $ JeanX.change_face("perplexed", 1)
                ch_j "Did you get enough?"

    $ approval_bonus = 0


    call Checkout
    return





label Jean_Fondle_Thighs:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JeanX)

    if JeanX.action_counter["fondle_thighs"]:
        $ approval_bonus += 10
    if JeanX.PantsNum() >= 6 or JeanX.HoseNum() >= 5:
        $ approval_bonus -= 5
    if JeanX.lust > 75:
        $ approval_bonus += 10
    if "exhibitionist" in JeanX.Traits:
        $ approval_bonus += Taboo
    if JeanX in Player.Harem or "sex friend" in JeanX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JeanX.Traits:
        $ approval_bonus -= 25
    if JeanX.event_counter["forced"] and not JeanX.Forced:
        $ approval_bonus -= 5*JeanX.event_counter["forced"]

    if JeanX.Taboo and "no_taboo" in JeanX.daily_history:
        $ approval_bonus -= 10
    if JeanX.Taboo and "public" not in JeanX.history:
        $ approval_bonus -= 20

    if "no_fondle thighs" in JeanX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle thighs" in JeanX.recent_history else 0

    $ Approval = ApprovalCheck(JeanX, 750, TabM=1)

    if action_context == "auto":
        if Approval:
            $ JeanX.change_face("sexy")
            $ JeanX.change_stat("obedience", 50, 1)
            $ JeanX.change_stat("inhibition", 30, 2)
            "As you caress her thigh, [JeanX.name] glances at you, and smiles."
            jump Jean_FT_Prep
        else:
            $ JeanX.change_face("surprised")
            $ JeanX.change_stat("obedience", 50, -2)
            ch_j "Keep it above the waist, [JeanX.player_petname]."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if action_context == "pullback":
        $ JeanX.change_face("surprised")
        $ JeanX.brows = "sad"
        if JeanX.lust > 60:
            $ JeanX.change_stat("love", 70, -3)
        $ JeanX.change_stat("obedience", 90, 1)
        $ JeanX.change_stat("obedience", 70, 2)
        "As you pull back, [JeanX.name] looks a little annoyed."
        jump Jean_FT_Prep
    elif "fondle_thighs" in JeanX.recent_history:
        $ JeanX.change_face("sexy", 1)
        ch_j "Mmmm, again? I guess. . ."
        jump Jean_FT_Prep
    elif "fondle_thighs" in JeanX.daily_history:
        $ JeanX.change_face("sexy", 1)
        ch_j "You didn't get enough earlier?"

    if Approval >= 2:
        $ JeanX.change_face("bemused", 1)
        if JeanX.Forced:
            $ JeanX.change_face("sad")
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("obedience", 90, 1)
            $ JeanX.change_stat("inhibition", 60, 1)
        ch_j "Ok [JeanX.player_petname], go ahead."
        $ JeanX.change_stat("love", 90, 1)
        $ JeanX.change_stat("inhibition", 50, 3)
        jump Jean_FT_Prep
    else:

        $ JeanX.change_face("angry", 1)
        if "no_fondle thighs" in JeanX.recent_history:
            ch_j "I'm not used to repeating myself."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history and "no_fondle thighs" in JeanX.daily_history:
            ch_j "I told you not to touch me like that in public!"
        elif "no_fondle thighs" in JeanX.daily_history:
            ch_j "Don't ask me again today."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "I told you. . . not here, [JeanX.player_petname]."
        elif not JeanX.action_counter["fondle_thighs"]:
            $ JeanX.change_face("bemused")
            ch_j "Look, don't touch, [JeanX.player_petname]."
        else:
            $ JeanX.change_face("bemused")
            ch_j "You wish."
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle thighs" in JeanX.daily_history:
                $ JeanX.change_face("bemused")
                ch_j "It's fine, I get it."
                return
            "Maybe later?" if "no_fondle thighs" not in JeanX.daily_history:
                $ JeanX.change_face("sexy")
                ch_j ". . . I guess? Maybe."
                $ JeanX.change_stat("love", 80, 1)
                $ JeanX.change_stat("inhibition", 30, 2)
                if JeanX.Taboo:
                    $ JeanX.recent_history.append("no_taboo")
                    $ JeanX.daily_history.append("no_taboo")
                $ JeanX.recent_history.append("no_fondle thighs")
                $ JeanX.daily_history.append("no_fondle thighs")
                return
            "Come on, Please?":
                if Approval:
                    $ JeanX.change_face("sexy")
                    $ JeanX.change_stat("obedience", 60, 1)
                    $ JeanX.change_stat("obedience", 30, 2)
                    $ JeanX.change_stat("inhibition", 50, 1)
                    $ JeanX.change_stat("inhibition", 30, 2)
                    ch_j "Oh, fine, just don't start crying."
                    jump Jean_FT_Prep
                else:
                    $ JeanX.change_face("sexy")
                    ch_j "Oh, don't cry."
            "[[Start caressing her thigh anyway]":

                $ Approval = ApprovalCheck(JeanX, 350, "OI", TabM = 2)
                if Approval > 1 or (Approval and JeanX.Forced):
                    $ JeanX.change_face("sad")
                    $ JeanX.change_stat("love", 70, -5, 1)
                    $ JeanX.change_stat("love", 20, -2, 1)
                    ch_j ". . .whatever. . ."
                    $ JeanX.change_stat("obedience", 50, 3)
                    $ JeanX.change_stat("inhibition", 60, 2)
                    if Approval < 2:
                        $ JeanX.Forced = 1
                    jump Jean_FT_Prep
                else:
                    $ JeanX.change_stat("love", 200, -8)
                    $ JeanX.change_face("angry", 1)
                    "She slaps your hand away."
                    $ JeanX.recent_history.append("angry")
                    $ JeanX.daily_history.append("angry")

    if "no_fondle thighs" in JeanX.daily_history:
        ch_j "I don't want to have to go through this again."
        $ JeanX.recent_history.append("angry")
        $ JeanX.daily_history.append("angry")
    elif JeanX.Forced:
        $ JeanX.change_face("angry", 1)
        ch_j "No."
        $ JeanX.change_stat("lust", 50, 2)
        $ JeanX.change_stat("obedience", 50, -1)
        $ JeanX.recent_history.append("angry")
        $ JeanX.daily_history.append("angry")
    elif JeanX.Taboo:
        $ JeanX.change_face("angry", 1)
        $ JeanX.recent_history.append("no_taboo")
        $ JeanX.daily_history.append("no_taboo")
        ch_j "I'm. . . not comfortable. . . in public. . ."
    elif JeanX.action_counter["fondle_thighs"]:
        $ JeanX.change_face("sad")
        ch_j "Keep your hands to yourself."
    else:
        $ JeanX.change_face("sexy")
        $ JeanX.mouth = "sad"
        ch_j "No."
    $ JeanX.recent_history.append("no_fondle thighs")
    $ JeanX.daily_history.append("no_fondle thighs")
    $ approval_bonus = 0
    return

label Jean_FT_Prep:
    if primary_action == "kiss":
        $ primary_action = "fondle_thighs"
        return

    if offhand_action == "fondle_thighs":
        return

    if not JeanX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (JeanX)
        if "angry" in JeanX.recent_history:
            return

    $ approval_bonus = 0
    call Jean_Pussy_Launch ("fondle_thighs")
    if not JeanX.action_counter["fondle_thighs"]:
        if JeanX.Forced:
            $ JeanX.change_stat("love", 90, -10)
            $ JeanX.change_stat("obedience", 70, 15)
            $ JeanX.change_stat("inhibition", 80, 10)
        else:
            $ JeanX.change_stat("love", 90, 5)
            $ JeanX.change_stat("obedience", 70, 10)
            $ JeanX.change_stat("inhibition", 80, 15)

    if JeanX.Taboo:
        $ JeanX.change_stat("lust", 200, (int(Taboo/5)))
        $ JeanX.change_stat("inhibition", 200, (2*(int(Taboo/5))))

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if JeanX.Taboo:
        $ JeanX.DrainWord("no_taboo")
    $ JeanX.DrainWord("no_fondle thighs")
    $ JeanX.recent_history.append("fondle_thighs")
    $ JeanX.daily_history.append("fondle_thighs")
    call Jean_Pussy_Launch ("fondle_thighs")

label Jean_FT_Cycle:
    while Round > 0:
        call ViewShift (JeanX, JeanX.pose, 0, "fondle_thighs")
        call shift_focus (JeanX)
        $ JeanX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (JeanX)
                    $ counter += 1
                    $ Round -= 1
                    jump Jean_FT_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (JeanX, "menu")
                    jump Jean_FT_Cycle
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
                                    "Can I do a little deeper?":
                                        if JeanX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Jean_FT_After
                                            call Jean_Fondle_Pussy
                                        else:
                                            call Sex_Basic_Dialog (JeanX, "tired")
                                    "Shift your hands a bit higher without asking":
                                        if JeanX.remaining_actions and multi_action:
                                            $ action_context = "auto"
                                            call Jean_FT_After
                                            call Jean_Fondle_Pussy
                                        else:
                                            "As your hands creep upwards, she grabs your wrists."
                                            call Sex_Basic_Dialog (JeanX, "tired")
                                    "Never Mind":
                                        jump Jean_FT_Cycle
                            else:
                                call Sex_Basic_Dialog (JeanX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Jean_FT_After
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
                                    jump Jean_FT_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jean_FT_Cycle
                                "Never mind":
                                    jump Jean_FT_Cycle

                        "Show her feet" if not ShowFeet and (JeanX.pose == "doggy" or JeanX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (JeanX.pose == "doggy" or JeanX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [JeanX.name]":

                            call Girl_Undress (JeanX)
                        "Clean up [JeanX.name] (locked)" if not JeanX.Spunk:
                            pass
                        "Clean up [JeanX.name]" if JeanX.Spunk:
                            call Girl_Cleanup (JeanX, "ask")
                        "Never mind":
                            jump Jean_FT_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jean_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jean_FT_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jean_Pos_Reset
                    $ Line = 0
                    jump Jean_FT_After


        call shift_focus (JeanX)
        call Sex_Dialog (JeanX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or JeanX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (JeanX)
                if "angry" in JeanX.recent_history:
                    call Jean_Pos_Reset
                    return
                $ JeanX.change_stat("lust", 200, 5)
                if 100 > JeanX.lust >= 70 and JeanX.session_orgasms < 2 and JeanX.SEXP >= 20:
                    $ JeanX.recent_history.append("unsatisfied")
                    $ JeanX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jean_FT_After
                $ Line = "came"

            if JeanX.lust >= 100:

                call Girl_Cumming (JeanX)
                if action_context == "shift" or "angry" in JeanX.recent_history:
                    jump Jean_FT_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in JeanX.recent_history and JeanX.SEXP >= 20:
                    "[JeanX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Jean_FT_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if JeanX.SEXP >= 100 or ApprovalCheck(JeanX, 1200, "LO"):
            pass
        elif counter == (5 + JeanX.action_counter["fondle_thighs"]):
            $ JeanX.brows = "confused"
            ch_j "Kinda nice, but. . ."
        elif counter == (15 + JeanX.action_counter["fondle_thighs"]) and JeanX.SEXP >= 15 and not ApprovalCheck(JeanX, 1500):
            $ JeanX.brows = "confused"
            menu:
                ch_j "Maybe try something else?"
                "Finish up.":
                    "You let go. . ."
                    jump Jean_FT_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Jean_FT_After
                "No, this is fun.":
                    if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                        $ JeanX.change_stat("love", 200, -5)
                        $ JeanX.change_stat("obedience", 50, 3)
                        $ JeanX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ JeanX.change_face("angry", 1)
                        call Jean_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_j "Well -I'm- bored."
                        $ JeanX.change_stat("love", 50, -3, 1)
                        $ JeanX.change_stat("love", 80, -4, 1)
                        $ JeanX.change_stat("obedience", 30, -1, 1)
                        $ JeanX.change_stat("obedience", 50, -1, 1)
                        $ JeanX.recent_history.append("angry")
                        $ JeanX.daily_history.append("angry")
                        jump Jean_FT_After


        call Escalation (JeanX)

        if Round == 10:
            call Sex_Basic_Dialog (JeanX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JeanX, 5)


    $ JeanX.change_face("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JeanX, "done")

label Jean_FT_After:
    if not action_context:
        call Jean_Pos_Reset

    $ JeanX.change_face("sexy")

    $ JeanX.action_counter["fondle_thighs"]+= 1
    $ JeanX.remaining_actions -=1
    if JeanX.PantsNum() < 6 or JeanX.Upskirt:
        $ JeanX.addiction_rate += 1
        if "addictive" in Player.Traits:
            $ JeanX.addiction_rate += 1

    if Partner == "Kitty":
        call Partner_Like (JeanX, 2)
    else:
        call Partner_Like (JeanX, 1)

    if JeanX.action_counter["fondle_thighs"]== 1:
        $ JeanX.SEXP += 3
        if not action_context:
            if JeanX.love >= 500 and "unsatisfied" not in JeanX.recent_history:
                ch_j "Well that was. . . something."
            elif JeanX.obedience <= 500 and Player.focus <= 20:
                $ JeanX.change_face("perplexed", 1)
                ch_j "Was that enough?"

    $ approval_bonus = 0


    call Checkout
    return


label Jean_Fondle_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JeanX)

    if JeanX.action_counter["fondle_pussy"]:
        $ approval_bonus += 20
    if JeanX.PantsNum() >= 6 or JeanX.HoseNum() >= 5:
        $ approval_bonus -= 10
    if JeanX.lust > 75:
        $ approval_bonus += 15
    if JeanX.lust > 75 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in JeanX.Traits:
        $ approval_bonus += (2*JeanX.Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JeanX.Traits:
        $ approval_bonus -= 25
    if JeanX.event_counter["forced"] and not JeanX.Forced:
        $ approval_bonus -= 5*JeanX.event_counter["forced"]

    if JeanX.Taboo and "no_taboo" in JeanX.daily_history:
        $ approval_bonus -= 10
    if JeanX.Taboo and "public" not in JeanX.history:
        $ approval_bonus -= 20

    if "no_fondle pussy" in JeanX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle pussy" in JeanX.recent_history else 0

    $ Approval = ApprovalCheck(JeanX, 1050, TabM = 2)

    if action_context == "auto":
        if Approval:
            $ JeanX.change_face("sexy")
            $ JeanX.change_stat("obedience", 90, 1)
            $ JeanX.change_stat("obedience", 70, 2)
            $ JeanX.change_stat("inhibition", 70, 3)
            $ JeanX.change_stat("inhibition", 30, 2)
            "As your hand creeps up her thigh, [JeanX.name] seems a bit surprised, but then nods."
            jump Jean_FP_Prep
        else:
            $ JeanX.change_face("surprised")
            $ JeanX.change_stat("obedience", 50, -2)
            ch_j "Not so fast, [JeanX.player_petname]. . ."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if action_context == "pullback":
        $ JeanX.change_face("surprised")
        $ JeanX.brows = "sad"
        if JeanX.lust > 80:
            $ JeanX.change_stat("love", 70, -4)
        $ JeanX.change_stat("obedience", 90, 1)
        $ JeanX.change_stat("obedience", 70, 2)
        "As your hand pulls out, [JeanX.name] gasps and looks upset."
        jump Jean_FP_Prep
    elif "fondle_pussy" in JeanX.recent_history:
        $ JeanX.change_face("sexy", 1)
        ch_j "Mmmm, again? I guess. . ."
        jump Jean_FP_Prep
    elif "fondle_pussy" in JeanX.daily_history:
        $ JeanX.change_face("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Chill. . .",
            "Take it slow, I'm still shaking from earlier.",
            "Mmm. . ."])
        ch_j "[Line]"

    if Approval >= 2:
        $ JeanX.change_face("bemused", 1)
        if JeanX.Forced:
            $ JeanX.change_face("sad")
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
            $ JeanX.change_stat("obedience", 90, 1)
            $ JeanX.change_stat("inhibition", 60, 1)
        ch_j "Mmmm, I couldn't refuse. . ."
        $ JeanX.change_stat("love", 90, 1)
        $ JeanX.change_stat("inhibition", 50, 3)
        jump Jean_FP_Prep
    else:

        $ JeanX.change_face("angry", 1)
        if "no_fondle pussy" in JeanX.recent_history:
            ch_j "I'm not used to repeating myself."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history and "no_fondle pussy" in JeanX.daily_history:
            ch_j "I told you not to touch me like that in public!"
        elif "no_fondle pussy" in JeanX.daily_history:
            ch_j "Don't ask me again today."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "I told you. . . not here, [JeanX.player_petname]."
        elif not JeanX.action_counter["fondle_pussy"]:
            $ JeanX.change_face("bemused")
            ch_j "I don't think we're there yet, [JeanX.player_petname]. . ."
        else:
            $ JeanX.change_face("bemused")
            ch_j "You wish."
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle pussy" in JeanX.daily_history:
                $ JeanX.change_face("bemused")
                ch_j "It's fine, I get it."
                return
            "Maybe later?" if "no_fondle pussy" not in JeanX.daily_history:
                $ JeanX.change_face("sexy")
                ch_j ". . . I guess? Maybe."
                $ JeanX.change_stat("love", 80, 2)
                $ JeanX.change_stat("inhibition", 70, 2)
                if JeanX.Taboo:
                    $ JeanX.recent_history.append("no_taboo")
                    $ JeanX.daily_history.append("no_taboo")
                $ JeanX.recent_history.append("no_fondle pussy")
                $ JeanX.daily_history.append("no_fondle pussy")
                return
            "Come on, Please?":
                if Approval:
                    $ JeanX.change_face("sexy")
                    $ JeanX.change_stat("obedience", 90, 2)
                    $ JeanX.change_stat("obedience", 50, 2)
                    $ JeanX.change_stat("inhibition", 70, 3)
                    $ JeanX.change_stat("inhibition", 40, 2)
                    ch_j "Oooh, beg for me. . ."
                    jump Jean_FP_Prep
                else:
                    $ JeanX.change_face("sexy")
                    ch_j "No."
            "[[Start fondling anyway]":

                $ Approval = ApprovalCheck(JeanX, 450, "OI", TabM = 2)
                if Approval > 1 or (Approval and JeanX.Forced):
                    $ JeanX.change_face("sad")
                    $ JeanX.change_stat("love", 70, -5, 1)
                    $ JeanX.change_stat("love", 200, -2)
                    ch_j ". . .whatever. . ."
                    $ JeanX.change_stat("obedience", 50, 4)
                    $ JeanX.change_stat("inhibition", 80, 1)
                    $ JeanX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ JeanX.Forced = 1
                    jump Jean_FP_Prep
                else:
                    $ JeanX.change_stat("love", 200, -15)
                    $ JeanX.change_face("angry", 1)
                    "She slaps your hand away."
                    $ JeanX.recent_history.append("angry")
                    $ JeanX.daily_history.append("angry")

    if "no_fondle pussy" in JeanX.daily_history:
        ch_j "I don't want to have to go through this again."
        $ JeanX.recent_history.append("angry")
        $ JeanX.daily_history.append("angry")
    elif JeanX.Forced:
        $ JeanX.change_face("angry", 1)
        ch_j "I don't think so, [JeanX.player_petname]."
        $ JeanX.change_stat("lust", 70, 5)
        $ JeanX.change_stat("obedience", 50, -2)
        $ JeanX.recent_history.append("angry")
        $ JeanX.daily_history.append("angry")
    elif JeanX.Taboo:
        $ JeanX.change_face("angry", 1)
        $ JeanX.recent_history.append("no_taboo")
        $ JeanX.daily_history.append("no_taboo")
        ch_j "I'm. . . not comfortable. . . in public. . ."
    elif JeanX.action_counter["fondle_pussy"]:
        $ JeanX.change_face("sad")
        ch_j "You can keep those to yourself."
    else:
        $ JeanX.change_face("sexy")
        $ JeanX.mouth = "sad"
        ch_j "No thanks, [JeanX.player_petname]."
    $ JeanX.recent_history.append("no_fondle pussy")
    $ JeanX.daily_history.append("no_fondle pussy")
    $ approval_bonus = 0
    return

label Jean_FP_Prep:
    if offhand_action == "fondle_pussy":
        return

    call Jean_Pussy_Launch ("fondle_pussy")

    if action_context == JeanX:

        $ action_context = 0
        if (JeanX.legs and not JeanX.Upskirt) or (JeanX.underwear and not JeanX.underwearDown):

            if ApprovalCheck(JeanX, 1250, TabM = 1) or (JeanX.SeenPussy and ApprovalCheck(JeanX, 500) and not JeanX.Taboo):
                $ JeanX.Upskirt = 1
                $ JeanX.underwearDown = 1
                $ Line = 0
                if JeanX.PantsNum() == 5:
                    $ Line = JeanX.name + " hikes up her_skirt"
                elif JeanX.PantsNum() >= 6:
                    $ Line = JeanX.name + " pulls down her " + JeanX.legs
                else:
                    $ Line = 0
                if JeanX.underwear:
                    if Line:

                        "[Line] and pulls her [JeanX.underwear] out of the way."
                        "She then grabs your arm and then presses your hand against her crotch, clearly intending you to get to work."
                    else:

                        "She pulls her [JeanX.underwear] out of the way, and then presses your hand against her crotch."
                        "She clearly intends for you to get to work."
                else:

                    "[Line], and then presses your hand against her crotch."
                    "She clearly intends for you to get to work."
                call Jean_First_Bottomless (1)
            else:
                "[JeanX.name] grabs your arm and presses your hand against her crotch, clearly intending you to get to work."
        else:
            "[JeanX.name] grabs your arm and presses your hand against her crotch, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ JeanX.change_stat("inhibition", 80, 3)
                $ JeanX.change_stat("inhibition", 50, 2)
                "You start to run your fingers along her pussy."
            "Praise her.":
                $ JeanX.change_face("sexy", 1)
                $ JeanX.change_stat("inhibition", 80, 3)
                ch_p "I like the initiative, [JeanX.petname]."
                $ JeanX.nameCheck()
                "You start to run your fingers along her pussy."
                $ JeanX.change_stat("love", 85, 1)
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your hand back."
                $ JeanX.change_face("surprised")
                $ JeanX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [JeanX.petname]."
                $ JeanX.nameCheck()
                $ JeanX.change_stat("love", 70, -4)
                "[JeanX.name] pulls back."
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("obedience", 50, 1)
                $ JeanX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ JeanX.AddWord(1,"refused","refused")
                return


    if not JeanX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (JeanX)
        if "angry" in JeanX.recent_history:
            return
    $ approval_bonus = 0

    if not JeanX.action_counter["fondle_pussy"]:
        if JeanX.Forced:
            $ JeanX.change_stat("love", 90, -50)
            $ JeanX.change_stat("obedience", 70, 35)
            $ JeanX.change_stat("inhibition", 80, 25)
        else:
            $ JeanX.change_stat("love", 90, 10)
            $ JeanX.change_stat("obedience", 70, 10)
            $ JeanX.change_stat("inhibition", 80, 15)
    if JeanX.Taboo:
        $ JeanX.change_stat("inhibition", 200, (int(Taboo/10)))
        $ JeanX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if JeanX.Taboo:
        $ JeanX.DrainWord("no_taboo")
    $ JeanX.DrainWord("no_fondle pussy")
    $ JeanX.recent_history.append("fondle_pussy")
    $ JeanX.daily_history.append("fondle_pussy")
    call Jean_Pussy_Launch ("fondle_pussy")

    $ action_speed = 1

label Jean_FP_Cycle:
    while Round > 0:
        call ViewShift (JeanX, JeanX.pose, 0, "fondle_pussy")
        call shift_focus (JeanX)
        $ JeanX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass

                "I want to stick a finger in. . ." if action_speed != 2:
                    if JeanX.action_counter["finger_pussy"]:
                        $ action_speed = 2
                    else:
                        menu:
                            "Ask her first":
                                $ action_context = "shift"
                            "Don't ask first [[just stick it in]":
                                $ action_context = "auto"
                        call Jean_Insert_Pussy

                "Pull back a bit. . ." if action_speed == 2:
                    $ action_speed = 0
                "Slap her ass":

                    call Slap_Ass (JeanX)
                    $ counter += 1
                    $ Round -= 1
                    jump Jean_FP_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (JeanX, "menu")
                    jump Jean_FP_Cycle
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
                                    "I want to lick your pussy.":
                                        $ action_context = "shift"
                                        call Jean_FP_After
                                        call Jean_Lick_Pussy
                                    "Just start licking":
                                        $ action_context = "auto"
                                        call Jean_FP_After
                                        call Jean_Lick_Pussy
                                    "Pull back to the thighs":
                                        $ action_context = "pullback"
                                        call Jean_FP_After
                                        call Jean_Fondle_Thighs
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Jean_FP_After
                                        call Jean_Dildo_Pussy
                                    "Never Mind":
                                        jump Jean_FP_Cycle
                            else:
                                call Sex_Basic_Dialog (JeanX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Jean_FP_After
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
                                    jump Jean_FP_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jean_FP_Cycle
                                "Never mind":
                                    jump Jean_FP_Cycle

                        "Show her feet" if not ShowFeet and (JeanX.pose == "doggy" or JeanX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (JeanX.pose == "doggy" or JeanX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [JeanX.name]":

                            call Girl_Undress (JeanX)
                        "Clean up [JeanX.name] (locked)" if not JeanX.Spunk:
                            pass
                        "Clean up [JeanX.name]" if JeanX.Spunk:
                            call Girl_Cleanup (JeanX, "ask")
                        "Never mind":
                            jump Jean_FP_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jean_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jean_FP_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jean_Pos_Reset
                    $ Line = 0
                    jump Jean_FP_After


        call shift_focus (JeanX)
        call Sex_Dialog (JeanX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or JeanX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (JeanX)
                if "angry" in JeanX.recent_history:
                    call Jean_Pos_Reset
                    return
                $ JeanX.change_stat("lust", 200, 5)
                if 100 > JeanX.lust >= 70 and JeanX.session_orgasms < 2:
                    $ JeanX.recent_history.append("unsatisfied")
                    $ JeanX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jean_FP_After
                $ Line = "came"

            if JeanX.lust >= 100:

                call Girl_Cumming (JeanX)
                if action_context == "shift" or "angry" in JeanX.recent_history:
                    jump Jean_FP_After

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
                            jump Jean_FP_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if JeanX.SEXP >= 100 or ApprovalCheck(JeanX, 1200, "LO"):
            pass
        elif counter == (5 + JeanX.action_counter["fondle_pussy"]):
            $ JeanX.brows = "confused"
            ch_j "Mmmm, you're enjoying that, huh?"
        elif JeanX.lust >= 80:
            pass
        elif counter == (15 + JeanX.action_counter["fondle_pussy"]) and JeanX.SEXP >= 15 and not ApprovalCheck(JeanX, 1500):
            $ JeanX.brows = "confused"
            menu:
                ch_j "Maybe try something else?"
                "Finish up.":
                    "You let go. . ."
                    jump Jean_FP_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Jean_FP_After
                "No, this is fun.":
                    if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                        $ JeanX.change_stat("love", 200, -5)
                        $ JeanX.change_stat("obedience", 50, 3)
                        $ JeanX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ JeanX.change_face("angry", 1)
                        call Jean_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_j "Well -I'm- bored."
                        $ JeanX.change_stat("love", 50, -3, 1)
                        $ JeanX.change_stat("love", 80, -4, 1)
                        $ JeanX.change_stat("obedience", 30, -1, 1)
                        $ JeanX.change_stat("obedience", 50, -1, 1)
                        $ JeanX.recent_history.append("angry")
                        $ JeanX.daily_history.append("angry")
                        jump Jean_FP_After


        call Escalation (JeanX)

        if Round == 10:
            call Sex_Basic_Dialog (JeanX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JeanX, 5)


    $ JeanX.change_face("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JeanX, "done")

label Jean_FP_After:
    if not action_context:
        call Jean_Pos_Reset

    $ JeanX.change_face("sexy")

    $ JeanX.action_counter["fondle_pussy"] += 1
    $ JeanX.remaining_actions -=1
    if JeanX.PantsNum() < 6 or JeanX.Upskirt:
        $ JeanX.addiction_rate += 1
        if "addictive" in Player.Traits:
            $ JeanX.addiction_rate += 1

    call Partner_Like (JeanX, 2)

    if JeanX.action_counter["fondle_pussy"] == 1:
        $ JeanX.SEXP += 7
        if not action_context:
            if JeanX.love >= 500 and "unsatisfied" not in JeanX.recent_history:
                ch_j "Well, that was a nice surprise. . ."
            elif JeanX.obedience <= 500 and Player.focus <= 20:
                $ JeanX.change_face("perplexed", 1)
                ch_j "Did you find what you were looking for?"

    $ approval_bonus = 0


    call Checkout
    return




label Jean_Insert_Pussy:
    call shift_focus (JeanX)
    if action_context == "auto":
        if ApprovalCheck(JeanX, 1100, TabM = 2):
            $ JeanX.change_face("surprised")
            $ JeanX.change_stat("obedience", 90, 1)
            $ JeanX.change_stat("obedience", 70, 2)
            $ JeanX.change_stat("inhibition", 70, 3)
            $ JeanX.change_stat("inhibition", 30, 2)
            "As you slide a finger in, [JeanX.name] seems a bit surprised, but seems into it."
            jump Jean_IP_Prep
        else:
            $ JeanX.change_face("surprised",2)
            $ JeanX.change_stat("love", 80, -2)
            $ JeanX.change_stat("obedience", 50, -3)
            ch_j "Oooh!"
            "She slaps your hand back."
            $ JeanX.change_face("perplexed",1)
            ch_j "Not so fast, [JeanX.player_petname]. . ."
            return

    if ApprovalCheck(JeanX, 1100, TabM = 2):
        if JeanX.Forced:
            $ JeanX.change_face("sad")
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
            $ JeanX.change_stat("obedience", 90, 1)
            $ JeanX.change_stat("inhibition", 60, 1)
            ch_j "Going there, huh. . ."
        else:
            $ JeanX.change_face("sexy", 1)
            $ JeanX.change_stat("love", 90, 1)
            $ JeanX.change_stat("inhibition", 50, 3)
            ch_j "Mmmmmm. . ."
        $ JeanX.change_stat("obedience", 20, 1)
        $ JeanX.change_stat("obedience", 60, 1)
        $ JeanX.change_stat("inhibition", 70, 2)
        jump Jean_IP_Prep
    else:

        $ JeanX.change_face("bemused", 1)
        ch_j "Nope."
        $ JeanX.blushing = 0
    return


label Jean_IP_Prep:
    if not JeanX.action_counter["finger_pussy"]:
        $ JeanX.action_counter["finger_pussy"] = 1
        $ JeanX.SEXP += 10
        if JeanX.Forced:
            $ JeanX.change_stat("love", 90, -60)
            $ JeanX.change_stat("obedience", 70, 55)
            $ JeanX.change_stat("inhibition", 80, 35)
        else:
            $ JeanX.change_stat("love", 90, 10)
            $ JeanX.change_stat("obedience", 70, 20)
            $ JeanX.change_stat("inhibition", 80, 25)

    if not JeanX.Forced and action_context != "auto":
        call Girl_Undress (JeanX, "bottom")
        if "angry" in JeanX.recent_history:
            return


    if JeanX.Taboo:
        $ JeanX.change_stat("inhibition", 200, (int(Taboo/10)))
        $ JeanX.lust += int(Taboo/5)

    $ Line = 0
    $ action_speed = 2
    return







label Jean_Lick_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JeanX)

    if JeanX.action_counter["eat_pussy"]:
        $ approval_bonus += 15
    if JeanX.PantsNum() >= 6 or JeanX.HoseNum() >= 5:
        $ approval_bonus -= 15
    if JeanX.lust > 95:
        $ approval_bonus += 20
    elif JeanX.lust > 85:
        $ approval_bonus += 15
    if action_context == "shift":
        $ approval_bonus += 10
    if JeanX.lust > 85 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in JeanX.Traits:
        $ approval_bonus += (4*JeanX.Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JeanX.Traits:
        $ approval_bonus -= 25
    if JeanX.event_counter["forced"] and not JeanX.Forced:
        $ approval_bonus -= 5*JeanX.event_counter["forced"]

    if JeanX.Taboo and "no_taboo" in JeanX.daily_history:
        $ approval_bonus -= 10
    if JeanX.Taboo and "public" not in JeanX.history:
        $ approval_bonus -= 20

    if "no_lick pussy" in JeanX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_lick pussy" in JeanX.recent_history else 0

    $ Approval = ApprovalCheck(JeanX, 1250, TabM = 4)

    if action_context == "auto":
        if Approval:
            $ JeanX.change_face("surprised")
            $ JeanX.change_stat("obedience", 90, 1)
            $ JeanX.change_stat("obedience", 70, 2)
            $ JeanX.change_stat("inhibition", 70, 3)
            $ JeanX.change_stat("inhibition", 30, 2)
            "As you crouch down and start to lick her pussy, [JeanX.name] starts, but then softens."
            $ JeanX.change_face("sexy")
            jump Jean_LP_Prep
        else:
            $ JeanX.change_face("surprised")
            $ JeanX.change_stat("love", 80, -2)
            $ JeanX.change_stat("obedience", 50, -3)
            ch_j "Hmmm, not yet, [JeanX.player_petname]."
            $ JeanX.change_face("perplexed",1)
            "She pushes your head back away from her."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "eat_pussy" in JeanX.recent_history:
        $ JeanX.change_face("sexy", 1)
        ch_j "Mmmm, again? I guess. . ."
        jump Jean_LP_Prep
    elif "eat_pussy" in JeanX.daily_history:
        $ JeanX.change_face("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Huh? Again?",
            "I must have done something right.",
            "I do like this. . .",
            "Mmm. . ."])
        ch_j "[Line]"

    if Approval >= 2:
        if JeanX.Forced:
            $ JeanX.change_face("sad")
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
            $ JeanX.change_stat("obedience", 90, 1)
            $ JeanX.change_stat("inhibition", 60, 1)
            ch_j "If you must. . ."
        else:
            $ JeanX.change_face("sexy", 1)
            $ JeanX.eyes = "closed"
            $ JeanX.change_stat("love", 90, 1)
            $ JeanX.change_stat("inhibition", 50, 3)
            $ JeanX.change_stat("lust", 200, 3)
            ch_j "Mmmmmm. . ."
        $ JeanX.change_stat("obedience", 20, 1)
        $ JeanX.change_stat("obedience", 60, 1)
        $ JeanX.change_stat("inhibition", 70, 2)
        jump Jean_LP_Prep
    else:

        $ JeanX.change_face("angry", 1)
        if "no_lick pussy" in JeanX.recent_history:
            ch_j "I'm not used to repeating myself."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history and "no_lick pussy" in JeanX.daily_history:
            ch_j "You already got your answer!"
        elif "no_lick pussy" in JeanX.daily_history:
            ch_j "Don't ask me again today."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "I told you. . . not here, [JeanX.player_petname]."
        elif not JeanX.action_counter["eat_pussy"]:
            $ JeanX.change_face("bemused")
            ch_j "Mmmm, not right now, [JeanX.player_petname]. . ."
        else:
            $ JeanX.change_face("bemused")
            ch_j "I'd rather not."
        menu:
            extend ""
            "Sorry, never mind." if "no_lick pussy" in JeanX.daily_history:
                $ JeanX.change_face("bemused")
                ch_j "It's fine, I get it."
                return
            "I'm sure I can convince you later. . ." if "no_lick pussy" not in JeanX.daily_history:
                $ JeanX.change_face("sexy")
                ch_j "Well, I'll give it some thought, [JeanX.player_petname]."
                $ JeanX.change_stat("love", 80, 2)
                $ JeanX.change_stat("inhibition", 70, 2)
                if JeanX.Taboo:
                    $ JeanX.recent_history.append("no_taboo")
                    $ JeanX.daily_history.append("no_taboo")
                $ JeanX.recent_history.append("no_lick pussy")
                $ JeanX.daily_history.append("no_lick pussy")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ JeanX.change_face("sexy")
                    $ JeanX.change_stat("obedience", 90, 2)
                    $ JeanX.change_stat("obedience", 50, 2)
                    ch_j "You make a good point. . ."
                    $ JeanX.change_stat("inhibition", 70, 3)
                    $ JeanX.change_stat("inhibition", 40, 2)
                    jump Jean_LP_Prep
                else:
                    $ JeanX.change_face("sexy")
                    ch_j "I would, but still no, [JeanX.player_petname]."
            "[[Get in there anyway]":

                $ Approval = ApprovalCheck(JeanX, 750, "OI", TabM = 4)
                if Approval > 1 or (Approval and JeanX.Forced):
                    $ JeanX.change_face("sad")
                    $ JeanX.change_stat("love", 70, -5, 1)
                    $ JeanX.change_stat("love", 200, -2)
                    ch_j "I guess you won't take \"no\" for an answer. . ."
                    $ JeanX.change_stat("obedience", 50, 4)
                    $ JeanX.change_stat("inhibition", 80, 1)
                    $ JeanX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ JeanX.Forced = 1
                    jump Jean_LP_Prep
                else:
                    $ JeanX.change_stat("love", 200, -15)
                    $ JeanX.change_face("angry", 1)
                    "She shoves your head back."
                    $ JeanX.recent_history.append("angry")
                    $ JeanX.daily_history.append("angry")

    if "no_lick pussy" in JeanX.daily_history:
        ch_j "I don't want to have to go through this again."
        $ JeanX.recent_history.append("angry")
        $ JeanX.daily_history.append("angry")
    elif JeanX.Forced:
        $ JeanX.change_face("angry", 1)
        ch_j "I really can't, [JeanX.player_petname]."
        $ JeanX.change_stat("lust", 80, 5)
        $ JeanX.change_stat("obedience", 50, -2)
        $ JeanX.recent_history.append("angry")
        $ JeanX.daily_history.append("angry")
    elif JeanX.Taboo:
        $ JeanX.change_face("angry", 1)
        $ JeanX.recent_history.append("no_taboo")
        $ JeanX.daily_history.append("no_taboo")
        ch_j "I'm. . . not comfortable. . . in public. . ."
    elif JeanX.action_counter["eat_pussy"]:
        $ JeanX.change_face("sad")
        ch_j "Keep your tongue to yourself."
    else:
        $ JeanX.change_face("surprised")
        ch_j "Yeah, sorry."
        $ JeanX.change_face()
    $ JeanX.recent_history.append("no_lick pussy")
    $ JeanX.daily_history.append("no_lick pussy")
    $ approval_bonus = 0
    return

label Jean_LP_Prep:
    if offhand_action == "eat_pussy":
        return

    $ approval_bonus = 0
    call Jean_Pussy_Launch ("eat_pussy")

    if action_context == JeanX:

        $ action_context = 0
        if (JeanX.legs and not JeanX.Upskirt) or (JeanX.underwear and not JeanX.underwearDown):

            if ApprovalCheck(JeanX, 1250, TabM = 1) or (JeanX.SeenPussy and ApprovalCheck(JeanX, 500) and not JeanX.Taboo):
                $ JeanX.Upskirt = 1
                $ JeanX.underwearDown = 1
                $ Line = 0
                if JeanX.PantsNum() == 5:
                    $ Line = JeanX.name + " hikes up her_skirt"
                elif JeanX.PantsNum() >= 6:
                    $ Line = JeanX.name + " pulls down her " + JeanX.legs
                else:
                    $ Line = 0
                if JeanX.underwear:
                    if Line:

                        "[Line] and pulls her [JeanX.underwear] out of the way."
                        "She then grabs your head and wraps her thighs around it, clearly intending you to get to work."
                    else:

                        "She pulls her [JeanX.underwear] out of the way, and then wraps her thighs around your head."
                        "She clearly intends for you to get to work."
                else:

                    "[Line], and then wraps her thighs around your head."
                    "She clearly intends for you to get to work."
                call Jean_First_Bottomless (1)
            else:
                "[JeanX.name] grabs your head and wraps her thighs around it, clearly intending you to get to work."
        else:
            "[JeanX.name] grabs your head and wraps her thighs around it, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ JeanX.change_stat("inhibition", 80, 3)
                $ JeanX.change_stat("inhibition", 50, 2)
                "You start licking."
            "Praise her.":
                $ JeanX.change_face("sexy", 1)
                $ JeanX.change_stat("inhibition", 80, 3)
                ch_p "Mmm, I like this idea, [JeanX.petname]."
                $ JeanX.nameCheck()
                "You start licking."
                $ JeanX.change_stat("love", 85, 1)
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your head away."
                $ JeanX.change_face("surprised")
                $ JeanX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [JeanX.petname]."
                $ JeanX.nameCheck()
                $ JeanX.change_stat("love", 70, -5)
                "[JeanX.name] pulls back."
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("obedience", 50, 1)
                $ JeanX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ JeanX.AddWord(1,"refused","refused")
                return


    if not JeanX.Forced and action_context != "auto":
        $ approval_bonus = 0
        if JeanX.PantsNum() >= 6 and not JeanX.Upskirt:
            $ approval_bonus = 15
        call Bottoms_Off (JeanX)
        if "angry" in JeanX.recent_history:
            return

    if not JeanX.action_counter["eat_pussy"]:
        if JeanX.Forced:
            $ JeanX.change_stat("love", 90, -30)
            $ JeanX.change_stat("obedience", 70, 35)
            $ JeanX.change_stat("inhibition", 80, 75)
        else:
            $ JeanX.change_stat("love", 90, 35)
            $ JeanX.change_stat("obedience", 70, 15)
            $ JeanX.change_stat("inhibition", 80, 35)
    if JeanX.Taboo:
        $ JeanX.change_stat("inhibition", 200, (int(Taboo/10)))
        $ JeanX.lust += int(Taboo/5)
    if action_context:
        $ renpy.pop_call()
        $ action_context = 0

    if JeanX.PantsNum() == 5:
        $ JeanX.Upskirt = 1
        $ JeanX.SeenPanties = 1
    call Jean_First_Bottomless (1)

    $ Line = 0
    $ counter = 0
    if JeanX.Taboo:
        $ JeanX.DrainWord("no_taboo")
    $ JeanX.DrainWord("no_lick pussy")
    $ JeanX.recent_history.append("eat_pussy")
    $ JeanX.daily_history.append("eat_pussy")
    call Jean_Pussy_Launch ("eat_pussy")

label Jean_LP_Cycle:
    if offhand_action == "kiss":
        $ offhand_action = 0
    while Round > 0:
        call ViewShift (JeanX, JeanX.pose, 0, "eat_pussy")
        call shift_focus (JeanX)
        $ JeanX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (JeanX)
                    $ counter += 1
                    $ Round -= 1
                    jump Jean_LP_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (JeanX, "menu")
                    jump Jean_LP_Cycle
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
                                    "Pull out and start rubbing again.":
                                        if JeanX.remaining_actions and multi_action:
                                            $ action_context = "pullback"
                                            call Jean_LP_After
                                            call Jean_Fondle_Pussy
                                        else:
                                            call Sex_Basic_Dialog (JeanX, "tired")
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Jean_LP_After
                                        call Jean_Dildo_Pussy
                                    "Never Mind":
                                        jump Jean_LP_Cycle
                            else:
                                call Sex_Basic_Dialog (JeanX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Jean_LP_After
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
                                    jump Jean_LP_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jean_LP_Cycle
                                "Never mind":
                                    jump Jean_LP_Cycle

                        "Show her feet" if not ShowFeet and (JeanX.pose == "doggy" or JeanX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (JeanX.pose == "doggy" or JeanX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [JeanX.name]":

                            call Girl_Undress (JeanX)
                        "Clean up [JeanX.name] (locked)" if not JeanX.Spunk:
                            pass
                        "Clean up [JeanX.name]" if JeanX.Spunk:
                            call Girl_Cleanup (JeanX, "ask")
                        "Never mind":
                            jump Jean_LP_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jean_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jean_LP_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jean_Pos_Reset
                    $ Line = 0
                    jump Jean_LP_After


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
                if "angry" in JeanX.recent_history:
                    call Jean_Pos_Reset
                    return
                $ JeanX.change_stat("lust", 200, 5)
                if 100 > JeanX.lust >= 70 and JeanX.session_orgasms < 2:
                    $ JeanX.recent_history.append("unsatisfied")
                    $ JeanX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jean_LP_After
                $ Line = "came"

            if JeanX.lust >= 100:

                call Girl_Cumming (JeanX)
                if action_context == "shift" or "angry" in JeanX.recent_history:
                    jump Jean_LP_After

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
                            jump Jean_LP_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if JeanX.SEXP >= 100 or ApprovalCheck(JeanX, 1200, "LO"):
            pass
        elif counter == (5 + JeanX.action_counter["eat_pussy"]):
            $ JeanX.brows = "confused"
            ch_j "Isn't it just delicious?"
        elif JeanX.lust >= 80:
            pass
        elif counter == (15 + JeanX.action_counter["eat_pussy"]) and JeanX.SEXP >= 15 and not ApprovalCheck(JeanX, 1500):
            $ JeanX.brows = "confused"
            menu:
                ch_j "Maybe try something else?"
                "Finish up.":
                    "You let go. . ."
                    jump Jean_LP_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Jean_LP_After
                "No, this is fun.":
                    if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                        $ JeanX.change_stat("love", 200, -5)
                        $ JeanX.change_stat("obedience", 50, 3)
                        $ JeanX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ JeanX.change_face("angry", 1)
                        call Jean_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_j "Well -I'm- bored."
                        $ JeanX.change_stat("love", 50, -3, 1)
                        $ JeanX.change_stat("love", 80, -4, 1)
                        $ JeanX.change_stat("obedience", 30, -1, 1)
                        $ JeanX.change_stat("obedience", 50, -1, 1)
                        $ JeanX.recent_history.append("angry")
                        $ JeanX.daily_history.append("angry")
                        jump Jean_LP_After


        call Escalation (JeanX)

        if Round == 10:
            call Sex_Basic_Dialog (JeanX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JeanX, 5)


    $ JeanX.change_face("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JeanX, "done")

label Jean_LP_After:
    if not action_context:
        call Jean_Pos_Reset

    $ JeanX.change_face("sexy")

    $ JeanX.action_counter["eat_pussy"] += 1
    $ JeanX.remaining_actions -=1
    if JeanX.PantsNum() < 6 or JeanX.Upskirt:
        $ JeanX.addiction_rate += 1
        if "addictive" in Player.Traits:
            $ JeanX.addiction_rate += 1

    if Partner == "Rogue":
        call Partner_Like (JeanX, 3, 2)
    else:
        call Partner_Like (JeanX, 2)

    if JeanX.action_counter["eat_pussy"] == 1:
        $ JeanX.SEXP += 10
        if not action_context:
            if JeanX.love >= 500 and "unsatisfied" not in JeanX.recent_history:
                ch_j "You really put that tongue to work. . ."
            elif JeanX.obedience <= 500 and Player.focus <= 20:
                $ JeanX.change_face("perplexed", 1)
                ch_j "I guess that wasn't so bad. . ."

    $ approval_bonus = 0


    call Checkout
    return






label Jean_Fondle_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JeanX)

    if JeanX.action_counter["fondle_ass"]:
        $ approval_bonus += 10
    if JeanX.PantsNum() >= 6 or JeanX.HoseNum() >= 5:
        $ approval_bonus -= 5
    if JeanX.lust > 75:
        $ approval_bonus += 15
    if "exhibitionist" in JeanX.Traits:
        $ approval_bonus += Taboo
    if JeanX in Player.Harem or "sex friend" in JeanX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JeanX.Traits:
        $ approval_bonus -= 25
    if JeanX.event_counter["forced"] and not JeanX.Forced:
        $ approval_bonus -= 5*JeanX.event_counter["forced"]

    if JeanX.Taboo and "no_taboo" in JeanX.daily_history:
        $ approval_bonus -= 10
    if JeanX.Taboo and "public" not in JeanX.history:
        $ approval_bonus -= 20

    if "no_fondle ass" in JeanX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle ass" in JeanX.recent_history else 0

    $ Approval = ApprovalCheck(JeanX, 850, TabM=1)

    if action_context == "auto":
        if Approval:
            $ JeanX.change_face("surprised", 1)
            $ JeanX.change_stat("obedience", 70, 2)
            $ JeanX.change_stat("inhibition", 40, 2)
            "As your hand creeps down her backside, [JeanX.name] shivers a bit, and then relaxes."
            $ JeanX.change_face("sexy")
            jump Jean_FA_Prep
        else:
            $ JeanX.change_face("surprised")
            $ JeanX.change_stat("obedience", 50, -3)
            ch_j "Not so fast, [JeanX.player_petname]. . ."
            $ JeanX.change_face("bemused")
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if action_context == "pullback":
        $ JeanX.change_face("surprised")
        $ JeanX.brows = "sad"
        if JeanX.lust > 80:
            $ JeanX.change_stat("love", 70, -4)
        $ JeanX.change_stat("obedience", 90, 1)
        $ JeanX.change_stat("obedience", 70, 2)
        "As your finger slides out, [JeanX.name] gasps and looks upset."
        jump Jean_FA_Prep
    elif "fondle_ass" in JeanX.recent_history:
        $ JeanX.change_face("sexy", 1)
        ch_j "Mmmm, again? I guess. . ."
        jump Jean_FA_Prep
    elif "fondle_ass" in JeanX.daily_history:
        $ JeanX.change_face("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Mmm, you like that? . .",
            "Mmm. . ."])
        ch_j "[Line]"

    if Approval >= 2:
        if JeanX.Forced:
            $ JeanX.change_face("sad")
            $ JeanX.change_stat("love", 70, -2, 1)
            $ JeanX.change_stat("obedience", 90, 2)
            $ JeanX.change_stat("inhibition", 60, 2)
            ch_j "If you insist. . ."
        else:
            $ JeanX.change_face("bemused, 1")
            ch_j "Yeah, ok. . ."
        $ JeanX.change_stat("lust", 200, 3)
        $ JeanX.change_stat("obedience", 60, 1)
        $ JeanX.change_stat("inhibition", 70, 1)
        jump Jean_FA_Prep
    else:

        $ JeanX.change_face("angry", 1)
        if "no_fondle ass" in JeanX.recent_history:
            ch_j "I'm not used to repeating myself."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history and "no_fondle ass" in JeanX.daily_history:
            ch_j "I told you not to touch me like that in public!"
        elif "no_fondle ass" in JeanX.daily_history:
            ch_j "Don't ask me again today."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "I told you. . . not here, [JeanX.player_petname]."
        elif not JeanX.action_counter["fondle_ass"]:
            $ JeanX.change_face("bemused")
            ch_j "Not yet, [JeanX.player_petname]. . ."
        else:
            $ JeanX.change_face("bemused")
            ch_j "Let's not, ok [JeanX.player_petname]?"
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle ass" in JeanX.daily_history:
                $ JeanX.change_face("bemused")
                ch_j "It's fine, I get it."
                return
            "Maybe later?" if "no_fondle ass" not in JeanX.daily_history:
                $ JeanX.change_face("sexy")
                ch_j ". . . I guess? Maybe."
                $ JeanX.change_stat("love", 80, 2)
                $ JeanX.change_stat("inhibition", 50, 2)
                if JeanX.Taboo:
                    $ JeanX.recent_history.append("no_taboo")
                    $ JeanX.daily_history.append("no_taboo")
                $ JeanX.recent_history.append("no_fondle ass")
                $ JeanX.daily_history.append("no_fondle ass")
                return
            "Just one good squeeze?":
                if Approval:
                    $ JeanX.change_face("sexy")
                    $ JeanX.change_stat("obedience", 90, 1)
                    $ JeanX.change_stat("obedience", 50, 2)
                    ch_j "Oooh, beg for me. . ."
                    $ JeanX.change_stat("inhibition", 70, 1)
                    $ JeanX.change_stat("inhibition", 40, 2)
                    jump Jean_FA_Prep
                else:
                    $ JeanX.change_face("sexy")
                    ch_j "No."
            "[[Start fondling anyway]":

                $ Approval = ApprovalCheck(JeanX, 250, "OI", TabM = 3)
                if Approval > 1 or (Approval and JeanX.Forced):
                    $ JeanX.change_face("sad")
                    $ JeanX.change_stat("love", 70, -3, 1)
                    $ JeanX.change_stat("love", 200, -1)
                    ch_j ". . .whatever. . ."
                    $ JeanX.change_stat("obedience", 50, 3)
                    $ JeanX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ JeanX.Forced = 1
                    jump Jean_FA_Prep
                else:
                    $ JeanX.change_stat("love", 200, -10)
                    $ JeanX.change_face("angry", 1)
                    "She slaps your hand away."
                    $ JeanX.recent_history.append("angry")
                    $ JeanX.daily_history.append("angry")

    if "no_fondle ass" in JeanX.daily_history:
        ch_j "I don't want to have to go through this again."
        $ JeanX.recent_history.append("angry")
        $ JeanX.daily_history.append("angry")
    elif JeanX.Forced:
        $ JeanX.change_face("angry", 1)
        ch_j "Mmmm, no."
        $ JeanX.change_stat("lust", 60, 5)
        $ JeanX.change_stat("obedience", 50, -2)
        $ JeanX.recent_history.append("angry")
        $ JeanX.daily_history.append("angry")
    elif JeanX.Taboo:
        $ JeanX.change_face("angry", 1)
        $ JeanX.recent_history.append("no_taboo")
        $ JeanX.daily_history.append("no_taboo")
        ch_j "I'm. . . not comfortable. . . in public. . ."
    elif JeanX.action_counter["fondle_ass"]:
        $ JeanX.change_face("sad")
        ch_j "Sorry, keep your hands to yourself."
    else:
        $ JeanX.change_face("sexy")
        $ JeanX.mouth = "sad"
        ch_j "No."
    $ JeanX.recent_history.append("no_fondle ass")
    $ JeanX.daily_history.append("no_fondle ass")
    $ approval_bonus = 0
    return

ch_j "Sorry, I don't even know how I got here. . ."
return

label Jean_FA_Prep:
    if offhand_action == "fondle_ass":
        return
    if not JeanX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (JeanX)
        if "angry" in JeanX.recent_history:
            return
    $ approval_bonus = 0
    call Jean_Pussy_Launch ("fondle_ass")
    if not JeanX.action_counter["fondle_ass"]:
        if JeanX.Forced:
            $ JeanX.change_stat("love", 90, -20)
            $ JeanX.change_stat("obedience", 70, 20)
            $ JeanX.change_stat("inhibition", 80, 15)
        else:
            $ JeanX.change_stat("love", 90, 10)
            $ JeanX.change_stat("obedience", 70, 12)
            $ JeanX.change_stat("inhibition", 80, 20)
    if JeanX.Taboo:
        $ JeanX.change_stat("inhibition", 200, (int(Taboo/10)))
        $ JeanX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if JeanX.Taboo:
        $ JeanX.DrainWord("no_taboo")
    $ JeanX.DrainWord("no_fondle ass")
    $ JeanX.recent_history.append("fondle_ass")
    $ JeanX.daily_history.append("fondle_ass")
    call Jean_Pussy_Launch ("fondle_ass")

label Jean_FA_Cycle:
    while Round > 0:
        call ViewShift (JeanX, JeanX.pose, 0, "fondle_ass")
        call shift_focus (JeanX)
        $ JeanX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (JeanX)
                    $ counter += 1
                    $ Round -= 1
                    jump Jean_FA_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (JeanX, "menu")
                    jump Jean_FA_Cycle
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
                                    "I want to stick a finger in.":
                                        $ action_context = "shift"
                                        call Jean_FA_After
                                        call Jean_Insert_Ass
                                    "Just stick a finger in without asking.":
                                        $ action_context = "auto"
                                        call Jean_FA_After
                                        call Jean_Insert_Ass
                                    "I want to lick your asshole.":
                                        $ action_context = "shift"
                                        call Jean_FA_After
                                        call Jean_Lick_Ass
                                    "Just start licking.":
                                        $ action_context = "auto"
                                        call Jean_FA_After
                                        call Jean_Lick_Ass
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Jean_FA_After
                                        call Jean_Dildo_Ass
                                    "Never Mind":
                                        jump Jean_FA_Cycle
                            else:
                                call Sex_Basic_Dialog (JeanX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Jean_FA_After
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
                                    jump Jean_FA_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jean_FA_Cycle
                                "Never mind":
                                    jump Jean_FA_Cycle

                        "Show her feet" if not ShowFeet and (JeanX.pose == "doggy" or JeanX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (JeanX.pose == "doggy" or JeanX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [JeanX.name]":

                            call Girl_Undress (JeanX)
                        "Clean up [JeanX.name] (locked)" if not JeanX.Spunk:
                            pass
                        "Clean up [JeanX.name]" if JeanX.Spunk:
                            call Girl_Cleanup (JeanX, "ask")
                        "Never mind":
                            jump Jean_FA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jean_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jean_FA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jean_Pos_Reset
                    $ Line = 0
                    jump Jean_FA_After


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
                if "angry" in JeanX.recent_history:
                    call Jean_Pos_Reset
                    return
                $ JeanX.change_stat("lust", 200, 5)
                if 100 > JeanX.lust >= 70 and JeanX.session_orgasms < 2 and JeanX.SEXP >= 20:
                    $ JeanX.recent_history.append("unsatisfied")
                    $ JeanX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jean_FA_After
                $ Line = "came"

            if JeanX.lust >= 100:

                call Girl_Cumming (JeanX)
                if action_context == "shift" or "angry" in JeanX.recent_history:
                    jump Jean_FA_After

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
                            jump Jean_FA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if JeanX.SEXP >= 100 or ApprovalCheck(JeanX, 1200, "LO"):
            pass
        elif counter == (5 + JeanX.action_counter["fondle_ass"]):
            $ JeanX.brows = "confused"
            ch_j "Mmmm. . ."
        elif JeanX.lust >= 80:
            pass
        elif counter == (15 + JeanX.action_counter["fondle_ass"]) and JeanX.SEXP >= 15 and not ApprovalCheck(JeanX, 1500):
            $ JeanX.brows = "confused"
            menu:
                ch_j "Maybe try something else?"
                "Finish up.":
                    "You let go. . ."
                    jump Jean_FA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Jean_FA_After
                "No, this is fun.":
                    if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                        $ JeanX.change_stat("love", 200, -5)
                        $ JeanX.change_stat("obedience", 50, 3)
                        $ JeanX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ JeanX.change_face("angry", 1)
                        call Jean_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_j "Well -I'm- bored."
                        $ JeanX.change_stat("love", 50, -3, 1)
                        $ JeanX.change_stat("love", 80, -4, 1)
                        $ JeanX.change_stat("obedience", 30, -1, 1)
                        $ JeanX.change_stat("obedience", 50, -1, 1)
                        $ JeanX.recent_history.append("angry")
                        $ JeanX.daily_history.append("angry")
                        jump Jean_FA_After


        call Escalation (JeanX)

        if Round == 10:
            call Sex_Basic_Dialog (JeanX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JeanX, 5)


    $ JeanX.change_face("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JeanX, "done")

label Jean_FA_After:
    if not action_context:
        call Jean_Pos_Reset

    $ JeanX.change_face("sexy")

    $ JeanX.action_counter["fondle_ass"] += 1
    $ JeanX.remaining_actions -=1
    if JeanX.PantsNum() < 6 or JeanX.Upskirt:
        $ JeanX.addiction_rate += 1
        if "addictive" in Player.Traits:
            $ JeanX.addiction_rate += 1

        call Partner_Like (JeanX, 2)

    if JeanX.action_counter["fondle_ass"] == 1:
        $ JeanX.SEXP += 4
        if not action_context:
            if JeanX.love >= 500 and "unsatisfied" not in JeanX.recent_history:
                ch_j "That was. . . nice. . ."
            elif JeanX.obedience <= 500 and Player.focus <= 20:
                $ JeanX.change_face("perplexed", 1)
                ch_j "I bet you enjoyed that."

    $ approval_bonus = 0


    call Checkout
    return





label Jean_Insert_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JeanX)

    if JeanX.action_counter["finger_ass"]:
        $ approval_bonus += 25
    if JeanX.PantsNum() >= 6 or JeanX.HoseNum() >= 5:
        $ approval_bonus -= 15
    if JeanX.lust > 85:
        $ approval_bonus += 15
    if JeanX.lust > 95:
        $ approval_bonus += 5
    if action_context == "shift":
        $ approval_bonus += 10
    if JeanX.lust > 85 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in JeanX.Traits:
        $ approval_bonus += (4*JeanX.Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JeanX.Traits:
        $ approval_bonus -= 25
    if JeanX.event_counter["forced"] and not JeanX.Forced:
        $ approval_bonus -= 5*JeanX.event_counter["forced"]

    if JeanX.Taboo and "no_taboo" in JeanX.daily_history:
        $ approval_bonus -= 10
    if JeanX.Taboo and "public" not in JeanX.history:
        $ approval_bonus -= 20

    if "no_insert ass" in JeanX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_insert ass" in JeanX.recent_history else 0

    $ Approval = ApprovalCheck(JeanX, 1300, TabM = 3)

    if action_context == "auto":
        if Approval:
            $ JeanX.change_face("surprised")
            $ JeanX.change_stat("obedience", 90, 2)
            $ JeanX.change_stat("obedience", 70, 2)
            $ JeanX.change_stat("inhibition", 80, 2)
            $ JeanX.change_stat("inhibition", 30, 2)
            "As you slide a finger in, [JeanX.name] tightens around it in surprise, but seems into it."
            $ JeanX.change_face("sexy")
            jump Jean_IA_Prep
        else:
            $ JeanX.change_face("surprised")
            $ JeanX.change_stat("love", 80, -2)
            $ JeanX.change_stat("obedience", 50, -3)
            ch_j "Ooo! Not right now, [JeanX.player_petname]."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "finger_ass" in JeanX.daily_history:
        $ JeanX.change_face("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Chill. . .",
            "Mmm. . ."])
        ch_j "[Line]"

    if Approval >= 2:
        if JeanX.Forced:
            $ JeanX.change_face("sad")
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
            $ JeanX.change_stat("obedience", 90, 1)
            $ JeanX.change_stat("inhibition", 60, 1)
            ch_j "If you must. . ."
        else:
            $ JeanX.change_face("sexy", 1)
            $ JeanX.eyes = "closed"
            $ JeanX.change_stat("love", 90, 1)
            $ JeanX.change_stat("inhibition", 50, 3)
            $ JeanX.change_stat("lust", 200, 3)
            ch_j "Mmmmm. . ."
        $ JeanX.change_stat("obedience", 20, 1)
        $ JeanX.change_stat("obedience", 60, 1)
        $ JeanX.change_stat("inhibition", 70, 2)
        jump Jean_IA_Prep
    else:

        $ JeanX.change_face("angry", 1)
        if "no_insert ass" in JeanX.recent_history:
            ch_j "I'm not used to repeating myself."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history and "no_insert ass" in JeanX.daily_history:
            ch_j "I told you that wasn't appropriate!"
        elif "no_insert ass" in JeanX.daily_history:
            ch_j "Don't ask me again today."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "I told you. . . not here, [JeanX.player_petname]."
        elif not JeanX.action_counter["finger_ass"]:
            $ JeanX.change_face("perplexed", 1)
            ch_j "That's really not my style. . ."
        else:
            $ JeanX.change_face("bemused")
            ch_j "I'd rather not today. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_insert ass" in JeanX.daily_history:
                $ JeanX.change_face("bemused")
                ch_j "It's fine, I get it."
                return
            "Maybe later?" if "no_insert ass" not in JeanX.daily_history:
                $ JeanX.change_face("sexy")
                ch_j ". . . I guess? Maybe."
                $ JeanX.change_stat("love", 80, 2)
                $ JeanX.change_stat("inhibition", 70, 2)
                if JeanX.Taboo:
                    $ JeanX.recent_history.append("no_taboo")
                    $ JeanX.daily_history.append("no_taboo")
                $ JeanX.recent_history.append("no_insert ass")
                $ JeanX.daily_history.append("no_insert ass")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ JeanX.change_face("sexy")
                    $ JeanX.change_stat("obedience", 90, 2)
                    $ JeanX.change_stat("obedience", 50, 2)
                    ch_j "You're probably right. . ."
                    $ JeanX.change_stat("inhibition", 70, 3)
                    $ JeanX.change_stat("inhibition", 40, 2)
                    jump Jean_IA_Prep
                else:
                    $ JeanX.change_face("bemused")
                    ch_j "I don't think that I would."
            "[[Slide a finger in anyway]":

                $ Approval = ApprovalCheck(JeanX, 950, "OI", TabM = 3)
                if Approval > 1 or (Approval and JeanX.Forced):
                    $ JeanX.change_face("surprised", 1)
                    $ JeanX.change_stat("love", 70, -5, 1)
                    $ JeanX.change_stat("love", 200, -2)
                    ch_j "Ooo! Well ok then. . ."
                    $ JeanX.change_face("sad")
                    $ JeanX.change_stat("obedience", 50, 4)
                    $ JeanX.change_stat("inhibition", 80, 1)
                    $ JeanX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ JeanX.Forced = 1
                    jump Jean_IA_Prep
                else:
                    $ JeanX.change_stat("love", 200, -15)
                    $ JeanX.change_face("angry", 1)
                    "She slaps your hand away."
                    $ JeanX.recent_history.append("angry")
                    $ JeanX.daily_history.append("angry")

    if "no_insert ass" in JeanX.daily_history:
        ch_j "I don't want to have to go through this again."
        $ JeanX.recent_history.append("angry")
        $ JeanX.daily_history.append("angry")
    elif JeanX.Forced:
        $ JeanX.change_face("angry", 1)
        ch_j "I'm not going there today."
        if ApprovalCheck(JeanX, 500, "I"):
            $ JeanX.change_stat("lust", 80, 10)
        else:
            $ JeanX.change_stat("lust", 50, 3)
        $ JeanX.change_stat("obedience", 50, -2)
        $ JeanX.recent_history.append("angry")
        $ JeanX.daily_history.append("angry")
    elif JeanX.Taboo:
        $ JeanX.change_face("angry", 1)
        $ JeanX.recent_history.append("no_taboo")
        $ JeanX.daily_history.append("no_taboo")
        ch_j "I'm. . . not comfortable. . . in public. . ."
    elif JeanX.action_counter["finger_ass"]:
        $ JeanX.change_face("sad")
        ch_j "I don't feel like it."
    else:
        $ JeanX.change_face("surprised")
        ch_j "Not today, [JeanX.player_petname]."
        $ JeanX.change_face()
    $ JeanX.recent_history.append("no_insert ass")
    $ JeanX.daily_history.append("no_insert ass")
    $ approval_bonus = 0
    return


label Jean_IA_Prep:
    if offhand_action == "finger_ass":
        return

    call Jean_Pussy_Launch ("finger_ass")

    if action_context == JeanX:

        $ action_context = 0
        if (JeanX.legs and not JeanX.Upskirt) or (JeanX.underwear and not JeanX.underwearDown):

            if ApprovalCheck(JeanX, 1250, TabM = 1) or (JeanX.SeenPussy and ApprovalCheck(JeanX, 500) and not JeanX.Taboo):
                $ JeanX.Upskirt = 1
                $ JeanX.underwearDown = 1
                $ Line = 0
                if JeanX.PantsNum() == 5:
                    $ Line = JeanX.name + " hikes up her_skirt"
                elif JeanX.PantsNum() >= 6:
                    $ Line = JeanX.name + " pulls down her " + JeanX.legs
                else:
                    $ Line = 0
                if JeanX.underwear:
                    if Line:

                        "[Line] and pulls her [JeanX.underwear] out of the way."
                        "She then grabs your arm and rubs your hand against her asshole, clearly intending you to get to work."
                    else:

                        "She pulls her [JeanX.underwear] out of the way, and then rubs your hand against her asshole."
                        "She clearly intends for you to get to work."
                else:

                    "[Line], and then rubs your hand against her asshole."
                    "She clearly intends for you to get to work."
                call Jean_First_Bottomless (1)
            else:
                "[JeanX.name] grabs your arm and rubs your hand against her asshole, clearly intending you to get to work."
        else:
            "[JeanX.name] grabs your arm and rubs your hand against her asshole, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ JeanX.change_stat("inhibition", 80, 3)
                $ JeanX.change_stat("inhibition", 50, 2)
                "You press your finger into it."
            "Praise her.":
                $ JeanX.change_face("sexy", 1)
                $ JeanX.change_stat("inhibition", 80, 3)
                ch_p "Dirty girl, [JeanX.petname]."
                $ JeanX.nameCheck()
                "You press your finger into it."
                $ JeanX.change_stat("love", 85, 1)
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your hand back."
                $ JeanX.change_face("surprised")
                $ JeanX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [JeanX.petname]."
                $ JeanX.nameCheck()
                $ JeanX.change_stat("love", 70, -2)
                "[JeanX.name] pulls back."
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("obedience", 50, 1)
                $ JeanX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ JeanX.AddWord(1,"refused","refused")
                return


    if not JeanX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (JeanX)
        if "angry" in JeanX.recent_history:
            return

    $ approval_bonus = 0
    if not JeanX.action_counter["finger_ass"]:
        if JeanX.Forced:
            $ JeanX.change_stat("love", 90, -50)
            $ JeanX.change_stat("obedience", 70, 60)
            $ JeanX.change_stat("inhibition", 80, 35)
        else:
            $ JeanX.change_stat("love", 90, 10)
            $ JeanX.change_stat("obedience", 70, 20)
            $ JeanX.change_stat("inhibition", 80, 25)

    if JeanX.Taboo:
        $ JeanX.change_stat("inhibition", 200, (int(Taboo/10)))
        $ JeanX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if JeanX.Taboo:
        $ JeanX.DrainWord("no_taboo")
    $ JeanX.DrainWord("no_insert ass")
    $ JeanX.recent_history.append("finger_ass")
    $ JeanX.daily_history.append("finger_ass")
    call Jean_Pussy_Launch ("finger_ass")

label Jean_IA_Cycle:
    while Round > 0:
        call ViewShift (JeanX, JeanX.pose, 0, "finger_ass")
        call shift_focus (JeanX)
        $ JeanX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (JeanX)
                    $ counter += 1
                    $ Round -= 1
                    jump Jean_IA_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (JeanX, "menu")
                    jump Jean_IA_Cycle
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
                                    "Pull out and start rubbing again.":
                                        $ action_context = "pullback"
                                        call Jean_IA_After
                                        call Jean_Fondle_Ass
                                    "I want to lick your asshole.":
                                        $ action_context = "shift"
                                        call Jean_IA_After
                                        call Jean_Lick_Ass
                                    "Just start licking.":
                                        $ action_context = "auto"
                                        call Jean_IA_After
                                        call Jean_Lick_Ass
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Jean_IA_After
                                        call Jean_Dildo_Ass
                                    "Never Mind":
                                        jump Jean_IA_Cycle
                            else:
                                call Sex_Basic_Dialog (JeanX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Jean_IA_After
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
                                    jump Jean_IA_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jean_IA_Cycle
                                "Never mind":
                                    jump Jean_IA_Cycle

                        "Show her feet" if not ShowFeet and (JeanX.pose == "doggy" or JeanX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (JeanX.pose == "doggy" or JeanX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [JeanX.name]":

                            call Girl_Undress (JeanX)
                        "Clean up [JeanX.name] (locked)" if not JeanX.Spunk:
                            pass
                        "Clean up [JeanX.name]" if JeanX.Spunk:
                            call Girl_Cleanup (JeanX, "ask")
                        "Never mind":
                            jump Jean_IA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jean_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jean_IA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jean_Pos_Reset
                    $ Line = 0
                    jump Jean_IA_After


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
                if "angry" in JeanX.recent_history:
                    call Jean_Pos_Reset
                    return
                $ JeanX.change_stat("lust", 200, 5)
                if 100 > JeanX.lust >= 70 and JeanX.session_orgasms < 2:
                    $ JeanX.recent_history.append("unsatisfied")
                    $ JeanX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jean_IA_After
                $ Line = "came"

            if JeanX.lust >= 100:

                call Girl_Cumming (JeanX)
                if action_context == "shift" or "angry" in JeanX.recent_history:
                    jump Jean_IA_After

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
                            jump Jean_IA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if JeanX.SEXP >= 100 or ApprovalCheck(JeanX, 1200, "LO"):
            pass
        elif counter == (5 + JeanX.action_counter["finger_ass"]):
            $ JeanX.brows = "confused"
            ch_j "Ungh, you're really getting in there. . ."
        elif JeanX.lust >= 80:
            pass
        elif counter == (15 + JeanX.action_counter["finger_ass"]) and JeanX.SEXP >= 15 and not ApprovalCheck(JeanX, 1500):
            $ JeanX.brows = "confused"
            menu:
                ch_j "Maybe try something else?"
                "Finish up.":
                    "You let go. . ."
                    jump Jean_IA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Jean_IA_After
                "No, this is fun.":
                    if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                        $ JeanX.change_stat("love", 200, -5)
                        $ JeanX.change_stat("obedience", 50, 3)
                        $ JeanX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ JeanX.change_face("angry", 1)
                        call Jean_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_j "Well -I'm- bored."
                        $ JeanX.change_stat("love", 50, -3, 1)
                        $ JeanX.change_stat("love", 80, -4, 1)
                        $ JeanX.change_stat("obedience", 30, -1, 1)
                        $ JeanX.change_stat("obedience", 50, -1, 1)
                        $ JeanX.recent_history.append("angry")
                        $ JeanX.daily_history.append("angry")
                        jump Jean_IA_After


        call Escalation (JeanX)

        if Round == 10:
            call Sex_Basic_Dialog (JeanX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JeanX, 5)


    $ JeanX.change_face("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JeanX, "done")

label Jean_IA_After:
    if not action_context:
        call Jean_Pos_Reset

    $ JeanX.change_face("sexy")

    $ JeanX.action_counter["finger_ass"] += 1
    $ JeanX.remaining_actions -=1
    $ JeanX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ JeanX.addiction_rate += 1

    call Partner_Like (JeanX, 2)

    if JeanX.action_counter["finger_ass"] == 1:
        $ JeanX.SEXP += 12
        if not action_context:
            if JeanX.love >= 500 and "unsatisfied" not in JeanX.recent_history:
                ch_j "That was. . . interesting. . ."
            elif JeanX.obedience <= 500 and Player.focus <= 20:
                $ JeanX.change_face("perplexed", 1)
                ch_j "I bet you enjoyed that."

    $ approval_bonus = 0


    call Checkout
    return








label Jean_Lick_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JeanX)

    if JeanX.action_counter["eat_ass"]:
        $ approval_bonus += 20
    if JeanX.PantsNum() >= 6 or JeanX.HoseNum() >= 5:
        $ approval_bonus -= 25
    if JeanX.lust > 95:
        $ approval_bonus += 20
    elif JeanX.lust > 85:
        $ approval_bonus += 15
    if JeanX.lust > 85 and action_context == "auto":
        $ approval_bonus += 10
    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in JeanX.Traits:
        $ approval_bonus += (4*JeanX.Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JeanX.Traits:
        $ approval_bonus -= 25
    if JeanX.event_counter["forced"] and not JeanX.Forced:
        $ approval_bonus -= 5*JeanX.event_counter["forced"]

    if JeanX.Taboo and "no_taboo" in JeanX.daily_history:
        $ approval_bonus -= 10
    if JeanX.Taboo and "public" not in JeanX.history:
        $ approval_bonus -= 20

    if "no_lick ass" in JeanX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_lick ass" in JeanX.recent_history else 0

    $ Approval = ApprovalCheck(JeanX, 1550, TabM = 4)

    if action_context == "auto":
        if Approval:
            $ JeanX.change_face("surprised")
            $ JeanX.change_stat("obedience", 90, 1)
            $ JeanX.change_stat("inhibition", 80, 3)
            $ JeanX.change_stat("inhibition", 40, 2)
            "As you crouch down and start to lick her asshole, [JeanX.name] startles briefly, but then begins to melt."
            $ JeanX.change_face("sexy")
            jump Jean_LA_Prep
        else:
            $ JeanX.change_face("surprised")
            $ JeanX.change_stat("love", 80, -2)
            $ JeanX.change_stat("obedience", 50, -3)
            ch_j "Whoa there, [JeanX.player_petname]!"
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "eat_ass" in JeanX.recent_history:
        $ JeanX.change_face("sexy", 1)
        ch_j "Mmmm, again? I guess. . ."
        jump Jean_LA_Prep
    elif "eat_ass" in JeanX.daily_history:
        $ JeanX.change_face("sexy", 1)
        ch_j "You didn't get enough earlier?"


    if Approval >= 2:
        if JeanX.Forced:
            $ JeanX.change_face("sad")
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
            $ JeanX.change_stat("obedience", 90, 2)
            $ JeanX.change_stat("inhibition", 60, 2)
            ch_j "Whatever. . ."
        else:
            $ JeanX.change_face("sexy", 1)
            $ JeanX.eyes = "closed"
            $ JeanX.change_stat("love", 90, 1)
            $ JeanX.change_stat("inhibition", 60, 2)
            $ JeanX.change_stat("lust", 200, 3)
            ch_j "Mmm. . . naughty."
        $ JeanX.change_stat("obedience", 20, 1)
        $ JeanX.change_stat("obedience", 60, 1)
        $ JeanX.change_stat("inhibition", 80, 2)
        jump Jean_LA_Prep
    else:

        $ JeanX.change_face("angry", 1)
        if "no_lick ass" in JeanX.recent_history:
            ch_j "I'm not used to repeating myself."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history and "no_lick ass" in JeanX.daily_history:
            ch_j "I told you not to touch me like that in public!"
        elif "no_lick ass" in JeanX.daily_history:
            ch_j "Don't ask me again today."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "I told you. . . not here, [JeanX.player_petname]."
        elif not JeanX.action_counter["eat_ass"]:
            $ JeanX.change_face("bemused", 1)
            if JeanX.love >= JeanX.obedience and JeanX.love >= (JeanX.inhibition - JeanX.IX):
                ch_j "Oh, we're there now?"
            elif JeanX.obedience >= (JeanX.inhibition - JeanX.IX):
                ch_j "Is that what gets you off?"
            else:
                $ JeanX.eyes = "sexy"
                ch_j "Mmmm, you're into that?"
        else:
            $ JeanX.change_face("bemused")
            ch_j "Not now, [JeanX.player_petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no_lick ass" in JeanX.daily_history:
                $ JeanX.change_face("bemused")
                ch_j "It's fine, I get it."
                return
            "I'm sure I can convince you later. . ." if "no_lick ass" not in JeanX.daily_history:
                $ JeanX.change_face("sexy")
                ch_j ". . . I guess? Maybe."
                $ JeanX.change_stat("love", 80, 2)
                $ JeanX.change_stat("inhibition", 70, 2)
                if JeanX.Taboo:
                    $ JeanX.recent_history.append("no_taboo")
                    $ JeanX.daily_history.append("no_taboo")
                $ JeanX.recent_history.append("no_lick ass")
                $ JeanX.daily_history.append("no_lick ass")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ JeanX.change_face("sexy")
                    $ JeanX.change_stat("obedience", 90, 2)
                    $ JeanX.change_stat("obedience", 50, 2)
                    ch_j "Ok, you're probably right. . ."
                    $ JeanX.change_stat("inhibition", 70, 3)
                    $ JeanX.change_stat("inhibition", 40, 2)
                    jump Jean_LA_Prep
                else:
                    $ JeanX.change_face("sexy")
                    ch_j "I really don't think so."
            "[[Start licking anyway]":

                $ Approval = ApprovalCheck(JeanX, 1100, "OI", TabM = 4)
                if Approval > 1 or (Approval and JeanX.Forced):
                    $ JeanX.change_face("sad")
                    $ JeanX.change_stat("love", 70, -5, 1)
                    $ JeanX.change_stat("love", 200, -2)
                    ch_j ". . .whatever. . ."
                    $ JeanX.change_stat("obedience", 50, 4)
                    $ JeanX.change_stat("inhibition", 80, 1)
                    $ JeanX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ JeanX.Forced = 1
                    jump Jean_LA_Prep
                else:
                    $ JeanX.change_stat("love", 200, -15)
                    $ JeanX.change_face("angry", 1)
                    "She shoves your head back."
                    $ JeanX.recent_history.append("angry")
                    $ JeanX.daily_history.append("angry")

    if "no_lick ass" in JeanX.daily_history:
        ch_j "I don't want to have to go through this again."
        $ JeanX.recent_history.append("angry")
        $ JeanX.daily_history.append("angry")
    elif JeanX.Forced:
        $ JeanX.change_face("angry", 1)
        ch_j "I don't think so."
        if ApprovalCheck(JeanX, 500, "I"):
            $ JeanX.change_stat("lust", 80, 10)
        else:
            $ JeanX.change_stat("lust", 50, 3)
        $ JeanX.change_stat("obedience", 50, -2)
        $ JeanX.recent_history.append("angry")
        $ JeanX.daily_history.append("angry")
    elif JeanX.Taboo:
        $ JeanX.change_face("angry", 1)
        $ JeanX.recent_history.append("no_taboo")
        $ JeanX.daily_history.append("no_taboo")
        ch_j "I'm. . . not comfortable. . . in public. . ."
    elif JeanX.action_counter["eat_ass"]:
        $ JeanX.change_face("sad")
        ch_j "We've had enough of that."
    else:
        $ JeanX.change_face("surprised")
        ch_j "I'm sorry, not now."
        $ JeanX.change_face()
    $ JeanX.recent_history.append("no_lick ass")
    $ JeanX.daily_history.append("no_lick ass")
    $ approval_bonus = 0
    return

label Jean_LA_Prep:
    if offhand_action == "eat_ass":
        return
    if not JeanX.Forced and action_context != "auto":
        $ approval_bonus = 0
        if JeanX.PantsNum() >= 6:
            $ approval_bonus = 15
        call Bottoms_Off (JeanX)
        if "angry" in JeanX.recent_history:
            return
    $ approval_bonus = 0
    call Jean_Pussy_Launch ("eat_ass")
    if not JeanX.action_counter["eat_ass"]:
        if JeanX.Forced:
            $ JeanX.change_stat("love", 90, -30)
            $ JeanX.change_stat("obedience", 70, 40)
            $ JeanX.change_stat("inhibition", 80, 80)
        else:
            $ JeanX.change_stat("love", 90, 35)
            $ JeanX.change_stat("obedience", 70, 25)
            $ JeanX.change_stat("inhibition", 80, 55)
    if JeanX.Taboo:
        $ JeanX.change_stat("inhibition", 200, (int(Taboo/10)))
        $ JeanX.lust += int(Taboo/5)
    if action_context:
        $ renpy.pop_call()
        $ action_context = 0

    $ JeanX.Upskirt = 1
    if JeanX.PantsNum() == 5:
        $ JeanX.SeenPanties = 1
    if not JeanX.underwear:
        call Jean_First_Bottomless (1)
    $ Line = 0
    $ counter = 0
    if JeanX.Taboo:
        $ JeanX.DrainWord("no_taboo")
    $ JeanX.DrainWord("no_lick ass")

    $ JeanX.recent_history.append("lick") if "lick" not in JeanX.recent_history else JeanX.recent_history
    $ JeanX.recent_history.append("ass") if "ass" not in JeanX.recent_history else JeanX.recent_history
    $ JeanX.recent_history.append("eat_ass")

    $ JeanX.daily_history.append("lick") if "lick" not in JeanX.daily_history else JeanX.recent_history
    $ JeanX.daily_history.append("ass") if "ass" not in JeanX.daily_history else JeanX.recent_history
    $ JeanX.daily_history.append("eat_ass")
    call Jean_Pussy_Launch ("eat_ass")

label Jean_LA_Cycle:
    if offhand_action == "kiss":
        $ offhand_action = 0
    while Round > 0:
        call ViewShift (JeanX, JeanX.pose, 0, "eat_ass")
        call shift_focus (JeanX)
        $ JeanX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (JeanX)
                    $ counter += 1
                    $ Round -= 1
                    jump Jean_LA_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (JeanX, "menu")
                    jump Jean_LA_Cycle
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
                                    "Switch to fondling.":
                                        $ action_context = "pullback"
                                        call Jean_LA_After
                                        call Jean_Fondle_Ass
                                    "I want to stick a finger in.":
                                        $ action_context = "shift"
                                        call Jean_LA_After
                                        call Jean_Insert_Ass
                                    "Just stick a finger in [[without asking].":
                                        $ action_context = "auto"
                                        call Jean_LA_After
                                        call Jean_Insert_Ass
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Jean_LA_After
                                        call Jean_Dildo_Ass
                                    "Never Mind":
                                        jump Jean_LA_Cycle
                            else:
                                call Sex_Basic_Dialog (JeanX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Jean_LA_After
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
                                    jump Jean_LA_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jean_LA_Cycle
                                "Never mind":
                                    jump Jean_LA_Cycle

                        "Show her feet" if not ShowFeet and (JeanX.pose == "doggy" or JeanX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (JeanX.pose == "doggy" or JeanX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [JeanX.name]":

                            call Girl_Undress (JeanX)
                        "Clean up [JeanX.name] (locked)" if not JeanX.Spunk:
                            pass
                        "Clean up [JeanX.name]" if JeanX.Spunk:
                            call Girl_Cleanup (JeanX, "ask")
                        "Never mind":
                            jump Jean_LA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jean_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jean_LA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jean_Pos_Reset
                    $ Line = 0
                    jump Jean_LA_After


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
                if "angry" in JeanX.recent_history:
                    call Jean_Pos_Reset
                    return
                $ JeanX.change_stat("lust", 200, 5)
                if 100 > JeanX.lust >= 70 and JeanX.session_orgasms < 2:
                    $ JeanX.recent_history.append("unsatisfied")
                    $ JeanX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jean_LA_After
                $ Line = "came"

            if JeanX.lust >= 100:

                call Girl_Cumming (JeanX)
                if action_context == "shift" or "angry" in JeanX.recent_history:
                    jump Jean_LA_After

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
                            jump Jean_LA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if JeanX.SEXP >= 100 or ApprovalCheck(JeanX, 1200, "LO"):
            pass
        elif counter == (5 + JeanX.action_counter["eat_ass"]):
            $ JeanX.brows = "confused"
            ch_j "You seem to be enjoying yourself. . ."
        elif JeanX.lust >= 80:
            pass
        elif counter == (15 + JeanX.action_counter["eat_ass"]) and JeanX.SEXP >= 15 and not ApprovalCheck(JeanX, 1500):
            $ JeanX.brows = "confused"
            menu:
                ch_j "[JeanX.player_petname], could we try something different?"
                "Finish up.":
                    "You let go. . ."
                    jump Jean_LA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Jean_LA_After
                "No, this is fun.":
                    if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                        $ JeanX.change_stat("love", 200, -5)
                        $ JeanX.change_stat("obedience", 50, 3)
                        $ JeanX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ JeanX.change_face("angry", 1)
                        call Jean_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_j "Well -I'm- bored."
                        $ JeanX.change_stat("love", 50, -3, 1)
                        $ JeanX.change_stat("love", 80, -4, 1)
                        $ JeanX.change_stat("obedience", 30, -1, 1)
                        $ JeanX.change_stat("obedience", 50, -1, 1)
                        $ JeanX.recent_history.append("angry")
                        $ JeanX.daily_history.append("angry")
                        jump Jean_LA_After


        call Escalation (JeanX)

        if Round == 10:
            call Sex_Basic_Dialog (JeanX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JeanX, 5)


    $ JeanX.change_face("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JeanX, "done")

label Jean_LA_After:
    if not action_context:
        call Jean_Pos_Reset

    $ JeanX.change_face("sexy")

    $ JeanX.action_counter["eat_ass"] += 1
    $ JeanX.remaining_actions -=1
    if JeanX.PantsNum() < 6 or JeanX.Upskirt:
        $ JeanX.addiction_rate += 1
        if "addictive" in Player.Traits:
            $ JeanX.addiction_rate += 1

    call Partner_Like (JeanX, 2)

    if JeanX.action_counter["eat_ass"] == 1:
        $ JeanX.SEXP += 15
        if not action_context:
            if JeanX.love >= 500 and "unsatisfied" not in JeanX.recent_history:
                ch_j "That was. . . interesting."
            elif JeanX.obedience <= 500 and Player.focus <= 20:
                $ JeanX.change_face("perplexed", 1)
                ch_j "Was that good for you?"

    $ approval_bonus = 0


    call Checkout
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
