
label Jubes_Fondle:

    $ JubesX.mouth = "smile"
    if not JubesX.remaining_actions:
        ch_v "Maybe later, [JubesX.player_petname]"
        return
    menu:
        ch_v "Well? Where did you want to touch, [JubesX.player_petname]?"
        "Your breasts?" if JubesX.remaining_actions:
            jump Jubes_Fondle_Breasts
        "Your thighs?" if JubesX.remaining_actions:
            jump Jubes_Fondle_Thighs
        "Your pussy?" if JubesX.remaining_actions:
            jump Jubes_Fondle_Pussy
        "Your Ass?" if JubesX.remaining_actions:
            jump Jubes_Fondle_Ass
        "Never mind.":
            return
    return



label Jubes_Fondle_Breasts:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JubesX)


    if JubesX.action_counter["fondle_breasts"]:
        $ approval_bonus += 15
    if JubesX.lust > 75:
        $ approval_bonus += 20
    if "exhibitionist" in JubesX.Traits:
        $ approval_bonus += (3*Taboo)
    if JubesX in Player.Harem or "sex friend" in JubesX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JubesX.Traits:
        $ approval_bonus -= 20
    if JubesX.event_counter["forced"] and not JubesX.Forced:
        $ approval_bonus -= 5*JubesX.event_counter["forced"]

    if Taboo and "no_taboo" in JubesX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in JubesX.history:
        $ approval_bonus -= 20

    if "no_fondle breasts" in JubesX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle breasts" in JubesX.recent_history else 0

    $ Approval = ApprovalCheck(JubesX, 950, TabM = 3)

    if action_context == "auto":
        if Approval:
            $ JubesX.change_face("sexy")
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_stat("obedience", 70, 2)
            $ JubesX.change_stat("inhibition", 70, 3)
            $ JubesX.change_stat("inhibition", 30, 2)
            "As you cup her breast, [JubesX.name] gently nods."
            jump Jubes_FB_Prep
        else:
            $ JubesX.change_face("surprised")
            $ JubesX.brows = "confused"
            $ JubesX.change_stat("obedience", 50, -2)
            ch_v "Cool your jets, [JubesX.player_petname]. . ."
            $ approval_bonus = 0
            $ offhand_action = 0
            return



    if Approval:
        $ JubesX.change_face("sexy", 1)
        if JubesX.Forced:
            $ JubesX.change_face("sad")
            $ JubesX.change_stat("love", 70, -3, 1)
            $ JubesX.change_stat("love", 20, -2, 1)
        elif not Taboo and "no_taboo" in JubesX.daily_history:
            ch_v "I guess this is less public. . ."

    if "fondle_breasts" in JubesX.recent_history:
        $ JubesX.change_face("sexy", 1)
        ch_v "Mmmm, again? I guess. . ."
        jump Jubes_FB_Prep
    elif "fondle_breasts" in JubesX.daily_history:
        $ JubesX.change_face("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax. . .",
            "Mmm. . ."])
        ch_v "[Line]"

    if Approval >= 2:
        $ JubesX.change_face("bemused", 1)
        if JubesX.Forced:
            $ JubesX.change_face("sad")
            $ JubesX.change_stat("love", 70, -3, 1)
            $ JubesX.change_stat("love", 20, -2, 1)
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_stat("inhibition", 60, 1)
        ch_v "Sure, sounds fun."
        $ JubesX.change_stat("love", 90, 1)
        $ JubesX.change_stat("inhibition", 50, 3)
        jump Jubes_FB_Prep
    else:

        $ JubesX.change_face("angry", 1)
        if "no_fondle breasts" in JubesX.recent_history:
            ch_v "I already told you, \"no\"."
        elif Taboo and "no_taboo" in JubesX.daily_history and "no_fondle breasts" in JubesX.daily_history:
            ch_v "I've had enough of this today."
        elif "no_fondle breasts" in JubesX.daily_history:
            ch_v "Don't make me tell you again today."
        elif Taboo and "no_taboo" in JubesX.daily_history:
            ch_v "I told you, not here, [JubesX.player_petname]."
        elif not JubesX.action_counter["fondle_breasts"]:
            $ JubesX.change_face("bemused")
            ch_v "Look, I don't know if we're ready for that, [JubesX.player_petname]. . ."
        else:
            $ JubesX.change_face("bemused")
            ch_v "Cute, but no."
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle breasts" in JubesX.daily_history:
                $ JubesX.change_face("bemused")
                ch_v "Yeah, whatever."
                return
            "Maybe later?" if "no_fondle breasts" not in JubesX.daily_history:
                $ JubesX.change_face("sexy")
                ch_v "Eh. Maybe."
                $ JubesX.change_stat("love", 80, 1)
                $ JubesX.change_stat("love", 50, 1)
                $ JubesX.change_stat("inhibition", 30, 2)
                if Taboo:
                    $ JubesX.recent_history.append("no_taboo")
                    $ JubesX.daily_history.append("no_taboo")
                $ JubesX.recent_history.append("no_fondle breasts")
                $ JubesX.daily_history.append("no_fondle breasts")
                return
            "Come on, Please?":
                if Approval:
                    $ JubesX.change_face("sexy")
                    $ JubesX.change_stat("obedience", 50, 2)
                    $ JubesX.change_stat("inhibition", 60, 3)
                    $ JubesX.change_stat("inhibition", 30, 2)
                    ch_v "Geeze, don't whine about it. . ."
                    jump Jubes_FB_Prep
                else:
                    $ JubesX.change_face("sexy")
                    ch_v "Geeze, don't whine about it. . ."
            "[[Grab her chest anyway]":


                $ Approval = ApprovalCheck(JubesX, 350, "OI", TabM = 3)
                if Approval > 1 or (Approval and JubesX.Forced):
                    $ JubesX.change_face("sad")
                    $ JubesX.change_stat("love", 70, -5, 1)
                    $ JubesX.change_stat("love", 20, -2, 1)
                    ch_v "Hey. . ."
                    ch_v "Well, whatever. . ."
                    $ JubesX.change_stat("obedience", 90, 2)
                    $ JubesX.change_stat("obedience", 50, 4)
                    $ JubesX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ JubesX.Forced = 1
                    jump Jubes_FB_Prep
                else:
                    $ JubesX.change_stat("love", 200, -10)
                    $ JubesX.change_face("angry", 1)
                    "She slaps your hand away."
                    $ JubesX.recent_history.append("angry")
                    $ JubesX.daily_history.append("angry")

    if "no_fondle breasts" in JubesX.daily_history:
        ch_v "I'm pretty clear on this, NO."
        $ JubesX.recent_history.append("angry")
        $ JubesX.daily_history.append("angry")
    elif JubesX.Forced:
        $ JubesX.change_face("angry", 1)
        ch_v "No."
        $ JubesX.change_stat("lust", 60, 5)
        $ JubesX.change_stat("obedience", 50, -2)
        $ JubesX.recent_history.append("angry")
        $ JubesX.daily_history.append("angry")
    elif Taboo:
        $ JubesX.change_face("angry", 1)
        $ JubesX.recent_history.append("no_taboo")
        $ JubesX.daily_history.append("no_taboo")
        ch_v "I don't wanna make a scene."
    elif JubesX.action_counter["fondle_breasts"]:
        $ JubesX.change_face("sad")
        ch_v "You'll have to earn that."
    else:
        $ JubesX.change_face("sexy")
        $ JubesX.mouth = "sad"
        ch_v "No."
    $ JubesX.recent_history.append("no_fondle breasts")
    $ JubesX.daily_history.append("no_fondle breasts")
    $ approval_bonus = 0
    return


label Jubes_FB_Prep:
    if primary_action == "kiss":
        $ primary_action = "fondle_breasts"
        return

    if offhand_action == "fondle_breasts":
        return

    call Jubes_Breasts_Launch ("fondle_breasts")

    if action_context == JubesX:

        $ action_context = 0
        if (JubesX.top or JubesX.bra) and not JubesX.Uptop:

            if ApprovalCheck(JubesX, 1250, TabM = 1) or (JubesX.SeenChest and ApprovalCheck(JubesX, 500) and not Taboo):
                $ JubesX.Uptop = 1
                $ Line = JubesX.top if JubesX.top else JubesX.bra
                "With a hungry grin, [JubesX.name] pulls her [Line] up over her breasts."
                call Jubes_First_Topless (1)
                $ Line = 0
                "She then grabs your arm and mashes your hand against her breast, clearly intending you to get to work."
            else:
                "[JubesX.name] grabs your arm and mashes your hand against her covered breast, clearly intending you to get to work."
        else:
            "[JubesX.name] grabs your arm and mashes your hand against her breast, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ JubesX.change_stat("inhibition", 80, 3)
                $ JubesX.change_stat("inhibition", 50, 2)
                "You start to fondle it."
            "Praise her.":
                $ JubesX.change_face("sexy", 1)
                $ JubesX.change_stat("inhibition", 80, 3)
                ch_p "I like the initiative, [JubesX.petname]."
                $ JubesX.nameCheck()
                "You start to fondle it."
                $ JubesX.change_stat("love", 85, 1)
                $ JubesX.change_stat("obedience", 90, 1)
                $ JubesX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your hand back."
                $ JubesX.change_face("surprised")
                $ JubesX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [JubesX.petname]."
                $ JubesX.nameCheck()
                "[JubesX.name] pulls back."
                $ JubesX.change_stat("obedience", 90, 1)
                $ JubesX.change_stat("obedience", 50, 1)
                $ JubesX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ JubesX.AddWord(1,"refused","refused")
                return


    if not JubesX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Top_Off (JubesX)
        if "angry" in JubesX.recent_history:
            return

    $ approval_bonus = 0
    if not JubesX.action_counter["fondle_breasts"]:
        if JubesX.Forced:
            $ JubesX.change_stat("love", 90, -20)
            $ JubesX.change_stat("obedience", 70, 25)
            $ JubesX.change_stat("inhibition", 80, 15)
        else:
            $ JubesX.change_stat("love", 90, 10)
            $ JubesX.change_stat("obedience", 70, 5)
            $ JubesX.change_stat("inhibition", 80, 15)

    if Taboo:
        $ JubesX.inhibition += int(Taboo/10)
        $ JubesX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ JubesX.DrainWord("no_taboo")
    $ JubesX.DrainWord("no_fondle breasts")
    $ JubesX.recent_history.append("fondle_breasts")
    $ JubesX.daily_history.append("fondle_breasts")
    call Jubes_Breasts_Launch ("fondle_breasts")

label Jubes_FB_Cycle:
    while Round > 0:
        call ViewShift (JubesX, JubesX.pose, 0, "fondle_breasts")
        call shift_focus (JubesX)
        $ JubesX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (JubesX)
                    $ counter += 1
                    $ Round -= 1
                    jump Jubes_FB_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (JubesX, "menu")
                    jump Jubes_FB_Cycle
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
                                    "Ask to suck on them.":
                                        if JubesX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Jubes_FB_After
                                            call Jubes_Suck_Breasts
                                        else:
                                            call Sex_Basic_Dialog (JubesX, "tired")
                                    "Just suck on them without asking.":
                                        if JubesX.remaining_actions and multi_action:
                                            $ action_context = "auto"
                                            call Jubes_FB_After
                                            call Jubes_Suck_Breasts
                                        else:
                                            "As you lean in to suck on her breast, she grabs your head and pushes back."
                                            call Sex_Basic_Dialog (JubesX, "tired")
                                    "Never Mind":
                                        jump Jubes_FB_Cycle
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
                                    jump Jubes_FB_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jubes_FB_Cycle
                                "Never mind":
                                    jump Jubes_FB_Cycle

                        "Show her feet" if not ShowFeet and (JubesX.pose == "doggy" or JubesX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (JubesX.pose == "doggy" or JubesX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [JubesX.name]":

                            call Girl_Undress (JubesX)
                        "Clean up [JubesX.name] (locked)" if not JubesX.Spunk:
                            pass
                        "Clean up [JubesX.name]" if JubesX.Spunk:
                            call Girl_Cleanup (JubesX, "ask")
                        "Never mind":
                            jump Jubes_FB_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jubes_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jubes_FB_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jubes_Pos_Reset
                    $ Line = 0
                    jump Jubes_FB_After


        call shift_focus (JubesX)
        call Sex_Dialog (JubesX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or JubesX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (JubesX)
                if "angry" in JubesX.recent_history:
                    call Jubes_Pos_Reset
                    return
                $ JubesX.change_stat("lust", 200, 5)
                if 100 > JubesX.lust >= 70 and JubesX.session_orgasms < 2:
                    $ JubesX.recent_history.append("unsatisfied")
                    $ JubesX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jubes_FB_After
                $ Line = "came"

            if JubesX.lust >= 100:

                call Girl_Cumming (JubesX)
                if action_context == "shift" or "angry" in JubesX.recent_history:
                    jump Jubes_FB_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in JubesX.recent_history and JubesX.SEXP >= 20:
                    "[JubesX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Jubes_FB_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if JubesX.SEXP >= 100 or ApprovalCheck(JubesX, 1200, "LO"):
            pass
        elif counter == (5 + JubesX.action_counter["fondle_breasts"]):
            $ JubesX.brows = "confused"
            ch_v "Having fun?"
        elif JubesX.lust >= 85:
            pass
        elif counter == (15 + JubesX.action_counter["fondle_breasts"]) and JubesX.SEXP >= 15 and not ApprovalCheck(JubesX, 1500):
            $ JubesX.brows = "confused"
            menu:
                ch_v "Could we maybe try. . . something else?"
                "Finish up.":
                    "You let go. . ."
                    jump Jubes_FB_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Jubes_FB_After
                "No, this is fun.":
                    if ApprovalCheck(JubesX, 1200) or ApprovalCheck(JubesX, 500, "O"):
                        $ JubesX.change_stat("love", 200, -5)
                        $ JubesX.change_stat("obedience", 50, 3)
                        $ JubesX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ JubesX.change_face("angry", 1)
                        call Jubes_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_v "This is kinda boring. . ."
                        $ JubesX.change_stat("love", 50, -3, 1)
                        $ JubesX.change_stat("love", 80, -4, 1)
                        $ JubesX.change_stat("obedience", 30, -1, 1)
                        $ JubesX.change_stat("obedience", 50, -1, 1)
                        $ JubesX.recent_history.append("angry")
                        $ JubesX.daily_history.append("angry")
                        jump Jubes_FB_After


        call Escalation (JubesX)

        if Round == 10:
            call Sex_Basic_Dialog (JubesX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JubesX, 5)

        if JubesX.lust >= 50 and not JubesX.Uptop and (JubesX.bra or JubesX.top):
            $ JubesX.Uptop = 1
            "[JubesX.name] grunts and pulls her clothes aside."
            call Jubes_First_Topless


    $ JubesX.change_face("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JubesX, "done")

label Jubes_FB_After:
    if not action_context:
        call Jubes_Pos_Reset

    $ JubesX.change_face("sexy")

    $ JubesX.action_counter["fondle_breasts"]+= 1
    $ JubesX.remaining_actions -=1
    $ JubesX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ JubesX.addiction_rate += 1

    call Partner_Like (JubesX, 2)

    if JubesX.action_counter["fondle_breasts"]== 1:
        $ JubesX.SEXP += 4
        if not action_context:
            if JubesX.love >= 500 and "unsatisfied" not in JubesX.recent_history:
                ch_v "Did you like that?"
            elif JubesX.obedience <= 500 and Player.focus <= 20:
                $ JubesX.change_face("perplexed", 1)
                ch_v "That worked out for you?"

    $ approval_bonus = 0


    call Checkout
    return






label Jubes_Suck_Breasts:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JubesX)

    if JubesX.action_counter["suck_breasts"]:
        $ approval_bonus += 15
    if not JubesX.bra and not JubesX.top:
        $ approval_bonus += 15
    if JubesX.lust > 75:
        $ approval_bonus += 20
    if JubesX.lust > 75 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in JubesX.Traits:
        $ approval_bonus += (4*Taboo)
    if JubesX in Player.Harem or "sex friend" in JubesX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JubesX.Traits:
        $ approval_bonus -= 25
    if JubesX.event_counter["forced"] and not JubesX.Forced:
        $ approval_bonus -= 5*JubesX.event_counter["forced"]

    if Taboo and "no_taboo" in JubesX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in JubesX.history:
        $ approval_bonus -= 20

    if "no_suck breasts" in JubesX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_suck breasts" in JubesX.recent_history else 0

    $ Approval = ApprovalCheck(JubesX, 1050, TabM = 4)

    if action_context == "auto":
        if Approval:
            $ JubesX.change_face("sexy")
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_stat("obedience", 70, 2)
            $ JubesX.change_stat("inhibition", 70, 3)
            $ JubesX.change_stat("inhibition", 30, 2)
            "As you dive in, [JubesX.name] seems a bit surprised, but just makes a little \"grunt.\""
            jump Jubes_SB_Prep
        else:
            $ JubesX.change_face("surprised")
            $ JubesX.change_stat("obedience", 50, -2)
            ch_v "Cool your jets, [JubesX.player_petname]. . ."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "suck_breasts" in JubesX.recent_history:
        $ JubesX.change_face("sexy", 1)
        ch_v "Mmmm, again? I guess. . ."
        jump Jubes_SB_Prep
    elif "suck_breasts" in JubesX.daily_history:
        $ JubesX.change_face("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax. . .",
            "Mmm. . ."])
        ch_v "[Line]"

    if Approval >= 2:
        $ JubesX.change_face("bemused", 1)
        if JubesX.Forced:
            $ JubesX.change_face("sad")
            $ JubesX.change_stat("love", 70, -3, 1)
            $ JubesX.change_stat("love", 20, -2, 1)
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_stat("inhibition", 60, 1)
        ch_v "Sure."
        $ JubesX.change_stat("love", 90, 1)
        $ JubesX.change_stat("inhibition", 50, 3)
        jump Jubes_SB_Prep
    else:

        $ JubesX.change_face("angry", 1)
        if "no_suck breasts" in JubesX.recent_history:
            ch_v "I already told you, \"no\"."
        elif Taboo and "no_taboo" in JubesX.daily_history and "no_suck breasts" in JubesX.daily_history:
            ch_v "I told you, I couldn't be caught like that."
        elif "no_suck breasts" in JubesX.daily_history:
            ch_v "Don't make me tell you again today."
        elif Taboo and "no_taboo" in JubesX.daily_history:
            ch_v "I told you, not here, [JubesX.player_petname]."
        elif not JubesX.action_counter["suck_breasts"]:
            $ JubesX.change_face("bemused")
            ch_v "Let's work up to that maybe. ."
        else:
            $ JubesX.change_face("bemused")
            ch_v "You wish."
        menu:
            extend ""
            "Sorry, never mind." if "no_suck breasts" in JubesX.daily_history:
                $ JubesX.change_face("bemused")
                ch_v "Yeah, whatever."
                return
            "Maybe later?" if "no_suck breasts" not in JubesX.daily_history:
                $ JubesX.change_face("sexy")
                ch_v "Maybe, [JubesX.player_petname]."
                $ JubesX.change_stat("love", 80, 1)
                $ JubesX.change_stat("love", 50, 1)
                $ JubesX.change_stat("inhibition", 30, 2)
                if Taboo:
                    $ JubesX.recent_history.append("no_taboo")
                    $ JubesX.daily_history.append("no_taboo")
                $ JubesX.recent_history.append("no_suck breasts")
                $ JubesX.daily_history.append("no_suck breasts")
                return
            "Come on, Please?":
                if Approval:
                    $ JubesX.change_face("sexy")
                    $ JubesX.change_stat("obedience", 90, 1)
                    $ JubesX.change_stat("obedience", 50, 2)
                    $ JubesX.change_stat("inhibition", 60, 3)
                    $ JubesX.change_stat("inhibition", 30, 2)
                    ch_v "Ok, fine. . ."
                    jump Jubes_SB_Prep
                else:
                    $ JubesX.change_face("sexy")
                    ch_v "Geeze, don't whine about it. . ."
            "[[Start sucking anyway]":

                $ Approval = ApprovalCheck(JubesX, 450, "OI", TabM = 3)
                if Approval > 1 or (Approval and JubesX.Forced):
                    $ JubesX.change_face("sad")
                    $ JubesX.change_stat("love", 70, -5, 1)
                    $ JubesX.change_stat("love", 20, -2, 1)
                    ch_v "Hmm. . . ok. . ."
                    $ JubesX.change_stat("obedience", 90, 2)
                    $ JubesX.change_stat("obedience", 50, 4)
                    $ JubesX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ JubesX.Forced = 1
                    jump Jubes_SB_Prep
                else:
                    $ JubesX.change_stat("love", 200, -10)
                    $ JubesX.change_face("angry", 1)
                    "She shoves your head back out."
                    $ JubesX.recent_history.append("angry")
                    $ JubesX.daily_history.append("angry")

    if "no_suck breasts" in JubesX.daily_history:
        ch_v "I'm pretty clear on this, NO."
        $ JubesX.recent_history.append("angry")
        $ JubesX.daily_history.append("angry")
    elif JubesX.Forced:
        $ JubesX.change_face("angry", 1)
        ch_v "Suck yourself."
        $ JubesX.change_stat("lust", 60, 5)
        $ JubesX.change_stat("obedience", 50, -2)
        $ JubesX.recent_history.append("angry")
        $ JubesX.daily_history.append("angry")
    elif Taboo:
        $ JubesX.change_face("angry", 1)
        $ JubesX.recent_history.append("no_taboo")
        $ JubesX.daily_history.append("no_taboo")
        ch_v "I don't wanna make a scene."
    elif JubesX.action_counter["suck_breasts"]:
        $ JubesX.change_face("sad")
        ch_v "You'll have to earn that back."
    else:
        $ JubesX.change_face("sexy")
        $ JubesX.mouth = "sad"
        ch_v "No."
    $ JubesX.recent_history.append("no_suck breasts")
    $ JubesX.daily_history.append("no_suck breasts")
    $ approval_bonus = 0
    return


label Jubes_SB_Prep:

    if offhand_action == "suck_breasts":
        return

    call Jubes_Breasts_Launch ("suck_breasts")

    if action_context == JubesX:

        $ action_context = 0
        if (JubesX.top or JubesX.bra) and not JubesX.Uptop:

            if ApprovalCheck(JubesX, 1250, TabM = 1) or (JubesX.SeenChest and ApprovalCheck(JubesX, 500) and not Taboo):
                $ JubesX.Uptop = 1
                $ Line = JubesX.top if JubesX.top else JubesX.bra
                "With a hungry grin, [JubesX.name] pulls her [Line] up over her breasts."
                call Jubes_First_Topless (1)
                $ Line = 0
                "She then grabs your head and crams your face into her chest, clearly intending you to get to work."
            else:
                "[JubesX.name] grabs your head and crams your face into her chest, clearly intending you to get to work."
        else:
            "[JubesX.name] grabs your head and crams your face into her chest, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ JubesX.change_stat("inhibition", 80, 3)
                $ JubesX.change_stat("inhibition", 50, 2)
                "You start to run your tongue along her nipple."
            "Praise her.":
                $ JubesX.change_face("sexy", 1)
                $ JubesX.change_stat("inhibition", 80, 3)
                ch_p "Mmm, I like this, [JubesX.petname]."
                $ JubesX.nameCheck()
                "You start to fondle it."
                $ JubesX.change_stat("love", 85, 1)
                $ JubesX.change_stat("obedience", 90, 1)
                $ JubesX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your head back."
                $ JubesX.change_face("surprised")
                $ JubesX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [JubesX.petname]."
                $ JubesX.nameCheck()
                "[JubesX.name] pulls away."
                $ JubesX.change_stat("obedience", 90, 1)
                $ JubesX.change_stat("obedience", 50, 1)
                $ JubesX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ JubesX.AddWord(1,"refused","refused")
                return


    if not JubesX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Top_Off (JubesX)
        if "angry" in JubesX.recent_history:
            return

    $ approval_bonus = 0
    if not JubesX.action_counter["suck_breasts"]:
        if JubesX.Forced:
            $ JubesX.change_stat("love", 90, -25)
            $ JubesX.change_stat("obedience", 70, 25)
            $ JubesX.change_stat("inhibition", 80, 17)
        else:
            $ JubesX.change_stat("love", 90, 10)
            $ JubesX.change_stat("obedience", 70, 10)
            $ JubesX.change_stat("inhibition", 80, 15)

    if Taboo:
        $ JubesX.inhibition += int(Taboo/10)
        $ JubesX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ JubesX.DrainWord("no_taboo")
    $ JubesX.DrainWord("no_suck breasts")
    $ JubesX.recent_history.append("suck_breasts")
    $ JubesX.daily_history.append("suck_breasts")
    call Jubes_Breasts_Launch ("suck_breasts")

label Jubes_SB_Cycle:
    if offhand_action == "kiss":
        $ offhand_action = 0
    while Round > 0:
        call ViewShift (JubesX, JubesX.pose, 0, "suck_breasts")
        call shift_focus (JubesX)
        $ JubesX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (JubesX)
                    $ counter += 1
                    $ Round -= 1
                    jump Jubes_SB_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (JubesX, "menu")
                    jump Jubes_SB_Cycle
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
                                    "Pull back to fondling.":
                                        if JubesX.remaining_actions and multi_action:
                                            $ action_context = "pullback"
                                            call Jubes_SB_After
                                            call Jubes_Fondle_Breasts
                                        else:
                                            "As you pull back, [JubesX.name] pushes you back in close."
                                            call Sex_Basic_Dialog (JubesX, "tired")
                                    "Never Mind":
                                        jump Jubes_SB_Cycle
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
                                    jump Jubes_SB_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jubes_SB_Cycle
                                "Never mind":
                                    jump Jubes_SB_Cycle

                        "Show her feet" if not ShowFeet and (JubesX.pose == "doggy" or JubesX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (JubesX.pose == "doggy" or JubesX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [JubesX.name]":

                            call Girl_Undress (JubesX)
                        "Clean up [JubesX.name] (locked)" if not JubesX.Spunk:
                            pass
                        "Clean up [JubesX.name]" if JubesX.Spunk:
                            call Girl_Cleanup (JubesX, "ask")
                        "Never mind":
                            jump Jubes_SB_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jubes_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jubes_SB_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jubes_Pos_Reset
                    $ Line = 0
                    jump Jubes_SB_After


        call shift_focus (JubesX)
        call Sex_Dialog (JubesX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or JubesX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (JubesX)
                if "angry" in JubesX.recent_history:
                    call Jubes_Pos_Reset
                    return
                $ JubesX.change_stat("lust", 200, 5)
                if 100 > JubesX.lust >= 70 and JubesX.session_orgasms < 2:
                    $ JubesX.recent_history.append("unsatisfied")
                    $ JubesX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jubes_SB_After
                $ Line = "came"

            if JubesX.lust >= 100:

                call Girl_Cumming (JubesX)
                if action_context == "shift" or "angry" in JubesX.recent_history:
                    jump Jubes_SB_After

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
                            jump Jubes_SB_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if JubesX.SEXP >= 100 or ApprovalCheck(JubesX, 1200, "LO"):
            pass
        elif counter == (5 + JubesX.action_counter["suck_breasts"]):
            $ JubesX.brows = "sly"
            ch_v "Having fun?"
        elif JubesX.lust >= 85:
            pass
        elif counter == (15 + JubesX.action_counter["suck_breasts"]) and JubesX.SEXP >= 15 and not ApprovalCheck(JubesX, 1500):
            $ JubesX.brows = "confused"
            menu:
                ch_v "Could we maybe try. . . something else?"
                "Finish up.":
                    "You let go. . ."
                    jump Jubes_SB_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Jubes_SB_After
                "No, this is fun.":
                    if ApprovalCheck(JubesX, 1200) or ApprovalCheck(JubesX, 500, "O"):
                        $ JubesX.change_stat("love", 200, -5)
                        $ JubesX.change_stat("obedience", 50, 3)
                        $ JubesX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ JubesX.change_face("angry", 1)
                        call Jubes_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_v "This is kinda boring. . ."
                        $ JubesX.change_stat("love", 50, -3, 1)
                        $ JubesX.change_stat("love", 80, -4, 1)
                        $ JubesX.change_stat("obedience", 30, -1, 1)
                        $ JubesX.change_stat("obedience", 50, -1, 1)
                        $ JubesX.recent_history.append("angry")
                        $ JubesX.daily_history.append("angry")
                        jump Jubes_SB_After


        call Escalation (JubesX)

        if Round == 10:
            call Sex_Basic_Dialog (JubesX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JubesX, 5)

        if JubesX.lust >= 50 and not JubesX.Uptop and (JubesX.bra or JubesX.top):
            $ JubesX.Uptop = 1
            "[JubesX.name] grunts and pulls her clothes aside."
            call Jubes_First_Topless


    $ JubesX.change_face("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JubesX, "done")

label Jubes_SB_After:
    if not action_context:
        call Jubes_Pos_Reset

    $ JubesX.change_face("sexy")

    $ JubesX.action_counter["suck_breasts"] += 1
    $ JubesX.remaining_actions -=1
    $ JubesX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ JubesX.addiction_rate += 1

    if Partner == "Kitty":
        call Partner_Like (JubesX, 2, 2)
    else:
        call Partner_Like (JubesX, 2)

    if JubesX.action_counter["suck_breasts"] == 1:
        $ JubesX.SEXP += 4
        if not action_context:
            if JubesX.love >= 500 and "unsatisfied" not in JubesX.recent_history:
                ch_v "That was kinda nice."
            elif JubesX.obedience <= 500 and Player.focus <= 20:
                $ JubesX.change_face("perplexed", 1)
                ch_v "Did you get enough?"

    $ approval_bonus = 0


    call Checkout
    return





label Jubes_Fondle_Thighs:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JubesX)

    if JubesX.action_counter["fondle_thighs"]:
        $ approval_bonus += 10
    if JubesX.PantsNum() >= 6 or JubesX.HoseNum() >= 5:
        $ approval_bonus -= 5
    if JubesX.lust > 75:
        $ approval_bonus += 10
    if "exhibitionist" in JubesX.Traits:
        $ approval_bonus += Taboo
    if JubesX in Player.Harem or "sex friend" in JubesX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JubesX.Traits:
        $ approval_bonus -= 25
    if JubesX.event_counter["forced"] and not JubesX.Forced:
        $ approval_bonus -= 5*JubesX.event_counter["forced"]

    if Taboo and "no_taboo" in JubesX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in JubesX.history:
        $ approval_bonus -= 20

    if "no_fondle thighs" in JubesX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle thighs" in JubesX.recent_history else 0

    $ Approval = ApprovalCheck(JubesX, 750, TabM=1)

    if action_context == "auto":
        if Approval:
            $ JubesX.change_face("sexy")
            $ JubesX.change_stat("obedience", 50, 1)
            $ JubesX.change_stat("inhibition", 30, 2)
            "As you caress her thigh, [JubesX.name] glances at you, and smiles."
            jump Jubes_FT_Prep
        else:
            $ JubesX.change_face("surprised")
            $ JubesX.change_stat("obedience", 50, -2)
            ch_v "Maybe we keep it above the waist, [JubesX.player_petname]."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if action_context == "pullback":
        $ JubesX.change_face("surprised")
        $ JubesX.brows = "sad"
        if JubesX.lust > 60:
            $ JubesX.change_stat("love", 70, -3)
        $ JubesX.change_stat("obedience", 90, 1)
        $ JubesX.change_stat("obedience", 70, 2)
        "As you pull back, [JubesX.name] looks a little annoyed."
        jump Jubes_FT_Prep
    elif "fondle_thighs" in JubesX.recent_history:
        $ JubesX.change_face("sexy", 1)
        ch_v "Mmmm, again? I guess. . ."
        jump Jubes_FT_Prep
    elif "fondle_thighs" in JubesX.daily_history:
        $ JubesX.change_face("sexy", 1)
        ch_v "You didn't get enough earlier?"

    if Approval >= 2:
        $ JubesX.change_face("bemused", 1)
        if JubesX.Forced:
            $ JubesX.change_face("sad")
            $ JubesX.change_stat("love", 70, -3, 1)
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_stat("inhibition", 60, 1)
        ch_v "Ok [JubesX.player_petname], go ahead."
        $ JubesX.change_stat("love", 90, 1)
        $ JubesX.change_stat("inhibition", 50, 3)
        jump Jubes_FT_Prep
    else:

        $ JubesX.change_face("angry", 1)
        if "no_fondle thighs" in JubesX.recent_history:
            ch_v "I already told you, \"no\"."
        elif Taboo and "no_taboo" in JubesX.daily_history and "no_fondle thighs" in JubesX.daily_history:
            ch_v "I told you not to touch me like that in public!"
        elif "no_fondle thighs" in JubesX.daily_history:
            ch_v "Don't make me tell you again today."
        elif Taboo and "no_taboo" in JubesX.daily_history:
            ch_v "I told you, not here, [JubesX.player_petname]."
        elif not JubesX.action_counter["fondle_thighs"]:
            $ JubesX.change_face("bemused")
            ch_v "Kinda forward, [JubesX.player_petname]."
        else:
            $ JubesX.change_face("bemused")
            ch_v "You wish."
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle thighs" in JubesX.daily_history:
                $ JubesX.change_face("bemused")
                ch_v "Yeah, whatever."
                return
            "Maybe later?" if "no_fondle thighs" not in JubesX.daily_history:
                $ JubesX.change_face("sexy")
                ch_v "Maybe?"
                $ JubesX.change_stat("love", 80, 1)
                $ JubesX.change_stat("inhibition", 30, 2)
                if Taboo:
                    $ JubesX.recent_history.append("no_taboo")
                    $ JubesX.daily_history.append("no_taboo")
                $ JubesX.recent_history.append("no_fondle thighs")
                $ JubesX.daily_history.append("no_fondle thighs")
                return
            "Come on, Please?":
                if Approval:
                    $ JubesX.change_face("sexy")
                    $ JubesX.change_stat("obedience", 60, 1)
                    $ JubesX.change_stat("obedience", 30, 2)
                    $ JubesX.change_stat("inhibition", 50, 1)
                    $ JubesX.change_stat("inhibition", 30, 2)
                    ch_v "Geeze, don't whine about it. . ."
                    jump Jubes_FT_Prep
                else:
                    $ JubesX.change_face("sexy")
                    ch_v "Geeze, don't whine about it. . ."
            "[[Start caressing her thigh anyway]":

                $ Approval = ApprovalCheck(JubesX, 350, "OI", TabM = 2)
                if Approval > 1 or (Approval and JubesX.Forced):
                    $ JubesX.change_face("sad")
                    $ JubesX.change_stat("love", 70, -5, 1)
                    $ JubesX.change_stat("love", 20, -2, 1)
                    ch_v "Hmmph."
                    $ JubesX.change_stat("obedience", 50, 3)
                    $ JubesX.change_stat("inhibition", 60, 2)
                    if Approval < 2:
                        $ JubesX.Forced = 1
                    jump Jubes_FT_Prep
                else:
                    $ JubesX.change_stat("love", 200, -8)
                    $ JubesX.change_face("angry", 1)
                    "She slaps your hand away."
                    $ JubesX.recent_history.append("angry")
                    $ JubesX.daily_history.append("angry")

    if "no_fondle thighs" in JubesX.daily_history:
        ch_v "I'm pretty clear on this, NO."
        $ JubesX.recent_history.append("angry")
        $ JubesX.daily_history.append("angry")
    elif JubesX.Forced:
        $ JubesX.change_face("angry", 1)
        ch_v "No."
        $ JubesX.change_stat("lust", 50, 2)
        $ JubesX.change_stat("obedience", 50, -1)
        $ JubesX.recent_history.append("angry")
        $ JubesX.daily_history.append("angry")
    elif Taboo:
        $ JubesX.change_face("angry", 1)
        $ JubesX.recent_history.append("no_taboo")
        $ JubesX.daily_history.append("no_taboo")
        ch_v "I don't wanna make a scene."
    elif JubesX.action_counter["fondle_thighs"]:
        $ JubesX.change_face("sad")
        ch_v "Keep your hands to yourself."
    else:
        $ JubesX.change_face("sexy")
        $ JubesX.mouth = "sad"
        ch_v "No."
    $ JubesX.recent_history.append("no_fondle thighs")
    $ JubesX.daily_history.append("no_fondle thighs")
    $ approval_bonus = 0
    return

label Jubes_FT_Prep:
    if primary_action == "kiss":
        $ primary_action = "fondle_thighs"
        return

    if offhand_action == "fondle_thighs":
        return

    if not JubesX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (JubesX)
        if "angry" in JubesX.recent_history:
            return

    $ approval_bonus = 0
    call Jubes_Pussy_Launch ("fondle_thighs")
    if not JubesX.action_counter["fondle_thighs"]:
        if JubesX.Forced:
            $ JubesX.change_stat("love", 90, -10)
            $ JubesX.change_stat("obedience", 70, 15)
            $ JubesX.change_stat("inhibition", 80, 10)
        else:
            $ JubesX.change_stat("love", 90, 5)
            $ JubesX.change_stat("obedience", 70, 10)
            $ JubesX.change_stat("inhibition", 80, 15)

    if Taboo:
        $ JubesX.change_stat("lust", 200, (int(Taboo/5)))
        $ JubesX.change_stat("inhibition", 200, (2*(int(Taboo/5))))

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ JubesX.DrainWord("no_taboo")
    $ JubesX.DrainWord("no_fondle thighs")
    $ JubesX.recent_history.append("fondle_thighs")
    $ JubesX.daily_history.append("fondle_thighs")
    call Jubes_Pussy_Launch ("fondle_thighs")

label Jubes_FT_Cycle:
    while Round > 0:
        call ViewShift (JubesX, JubesX.pose, 0, "fondle_thighs")
        call shift_focus (JubesX)
        $ JubesX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (JubesX)
                    $ counter += 1
                    $ Round -= 1
                    jump Jubes_FT_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (JubesX, "menu")
                    jump Jubes_FT_Cycle
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
                                    "Can I do a little deeper?":
                                        if JubesX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Jubes_FT_After
                                            call Jubes_Fondle_Pussy
                                        else:
                                            call Sex_Basic_Dialog (JubesX, "tired")
                                    "Shift your hands a bit higher without asking":
                                        if JubesX.remaining_actions and multi_action:
                                            $ action_context = "auto"
                                            call Jubes_FT_After
                                            call Jubes_Fondle_Pussy
                                        else:
                                            "As your hands creep upwards, she grabs your wrists."
                                            call Sex_Basic_Dialog (JubesX, "tired")
                                    "Never Mind":
                                        jump Jubes_FT_Cycle
                            else:
                                call Sex_Basic_Dialog (JubesX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Jubes_FT_After
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
                                    jump Jubes_FT_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jubes_FT_Cycle
                                "Never mind":
                                    jump Jubes_FT_Cycle

                        "Show her feet" if not ShowFeet and (JubesX.pose == "doggy" or JubesX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (JubesX.pose == "doggy" or JubesX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [JubesX.name]":

                            call Girl_Undress (JubesX)
                        "Clean up [JubesX.name] (locked)" if not JubesX.Spunk:
                            pass
                        "Clean up [JubesX.name]" if JubesX.Spunk:
                            call Girl_Cleanup (JubesX, "ask")
                        "Never mind":
                            jump Jubes_FT_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jubes_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jubes_FT_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jubes_Pos_Reset
                    $ Line = 0
                    jump Jubes_FT_After


        call shift_focus (JubesX)
        call Sex_Dialog (JubesX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or JubesX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (JubesX)
                if "angry" in JubesX.recent_history:
                    call Jubes_Pos_Reset
                    return
                $ JubesX.change_stat("lust", 200, 5)
                if 100 > JubesX.lust >= 70 and JubesX.session_orgasms < 2 and JubesX.SEXP >= 20:
                    $ JubesX.recent_history.append("unsatisfied")
                    $ JubesX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jubes_FT_After
                $ Line = "came"

            if JubesX.lust >= 100:

                call Girl_Cumming (JubesX)
                if action_context == "shift" or "angry" in JubesX.recent_history:
                    jump Jubes_FT_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in JubesX.recent_history and JubesX.SEXP >= 20:
                    "[JubesX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Jubes_FT_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if JubesX.SEXP >= 100 or ApprovalCheck(JubesX, 1200, "LO"):
            pass
        elif counter == (5 + JubesX.action_counter["fondle_thighs"]):
            $ JubesX.brows = "confused"
            ch_v "Ok, but, uh. . ."
        elif counter == (15 + JubesX.action_counter["fondle_thighs"]) and JubesX.SEXP >= 15 and not ApprovalCheck(JubesX, 1500):
            $ JubesX.brows = "confused"
            menu:
                ch_v "Could we maybe try. . . something else?"
                "Finish up.":
                    "You let go. . ."
                    jump Jubes_FT_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Jubes_FT_After
                "No, this is fun.":
                    if ApprovalCheck(JubesX, 1200) or ApprovalCheck(JubesX, 500, "O"):
                        $ JubesX.change_stat("love", 200, -5)
                        $ JubesX.change_stat("obedience", 50, 3)
                        $ JubesX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ JubesX.change_face("angry", 1)
                        call Jubes_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_v "This is kinda boring. . ."
                        $ JubesX.change_stat("love", 50, -3, 1)
                        $ JubesX.change_stat("love", 80, -4, 1)
                        $ JubesX.change_stat("obedience", 30, -1, 1)
                        $ JubesX.change_stat("obedience", 50, -1, 1)
                        $ JubesX.recent_history.append("angry")
                        $ JubesX.daily_history.append("angry")
                        jump Jubes_FT_After


        call Escalation (JubesX)

        if Round == 10:
            call Sex_Basic_Dialog (JubesX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JubesX, 5)


    $ JubesX.change_face("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JubesX, "done")


label Jubes_FT_After:
    if not action_context:
        call Jubes_Pos_Reset

    $ JubesX.change_face("sexy")

    $ JubesX.action_counter["fondle_thighs"]+= 1
    $ JubesX.remaining_actions -=1
    if JubesX.PantsNum() < 6 or JubesX.Upskirt:
        $ JubesX.addiction_rate += 1
        if "addictive" in Player.Traits:
            $ JubesX.addiction_rate += 1

    if JubesX.action_counter["fondle_thighs"]== 1:
        $ JubesX.SEXP += 3
        if not action_context:
            if JubesX.love >= 500 and "unsatisfied" not in JubesX.recent_history:
                ch_v "That was. . . interesting."
            elif JubesX.obedience <= 500 and Player.focus <= 20:
                $ JubesX.change_face("perplexed", 1)
                ch_v "Was that enough?"

    $ approval_bonus = 0


    call Checkout
    return


label Jubes_Fondle_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JubesX)

    if JubesX.action_counter["fondle_pussy"]:
        $ approval_bonus += 20
    if JubesX.PantsNum() >= 6 or JubesX.HoseNum() >= 5:
        $ approval_bonus -= 10
    if JubesX.lust > 75:
        $ approval_bonus += 15
    if JubesX.lust > 75 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in JubesX.Traits:
        $ approval_bonus += (2*Taboo)
    if JubesX in Player.Harem or "sex friend" in JubesX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JubesX.Traits:
        $ approval_bonus -= 25
    if JubesX.event_counter["forced"] and not JubesX.Forced:
        $ approval_bonus -= 5*JubesX.event_counter["forced"]

    if Taboo and "no_taboo" in JubesX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in JubesX.history:
        $ approval_bonus -= 20

    if "no_fondle pussy" in JubesX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle pussy" in JubesX.recent_history else 0

    $ Approval = ApprovalCheck(JubesX, 1050, TabM = 2)

    if action_context == "auto":
        if Approval:
            $ JubesX.change_face("sexy")
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_stat("obedience", 70, 2)
            $ JubesX.change_stat("inhibition", 70, 3)
            $ JubesX.change_stat("inhibition", 30, 2)
            "As your hand creeps up her thigh, [JubesX.name] seems a bit surprised, but then nods."
            jump Jubes_FP_Prep
        else:
            $ JubesX.change_face("surprised")
            $ JubesX.change_stat("obedience", 50, -2)
            ch_v "Cool your jets, [JubesX.player_petname]. . ."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if action_context == "pullback":
        $ JubesX.change_face("surprised")
        $ JubesX.brows = "sad"
        if JubesX.lust > 80:
            $ JubesX.change_stat("love", 70, -4)
        $ JubesX.change_stat("obedience", 90, 1)
        $ JubesX.change_stat("obedience", 70, 2)
        "As your hand pulls out, [JubesX.name] gasps and looks upset."
        jump Jubes_FP_Prep
    elif "fondle_pussy" in JubesX.recent_history:
        $ JubesX.change_face("sexy", 1)
        ch_v "Mmmm, again? I guess. . ."
        jump Jubes_FP_Prep
    elif "fondle_pussy" in JubesX.daily_history:
        $ JubesX.change_face("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax. . .",
            "Take it slow, I'm still shaking from earlier.",
            "Mmm. . ."])
        ch_v "[Line]"

    if Approval >= 2:
        $ JubesX.change_face("bemused", 1)
        if JubesX.Forced:
            $ JubesX.change_face("sad")
            $ JubesX.change_stat("love", 70, -3, 1)
            $ JubesX.change_stat("love", 20, -2, 1)
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_stat("inhibition", 60, 1)
        ch_v "Mmmm, I couldn't refuse. . ."
        $ JubesX.change_stat("love", 90, 1)
        $ JubesX.change_stat("inhibition", 50, 3)
        jump Jubes_FP_Prep
    else:

        $ JubesX.change_face("angry", 1)
        if "no_fondle pussy" in JubesX.recent_history:
            ch_v "I already told you, \"no\"."
        elif Taboo and "no_taboo" in JubesX.daily_history and "no_fondle pussy" in JubesX.daily_history:
            ch_v "I told you not to touch me like that in public!"
        elif "no_fondle pussy" in JubesX.daily_history:
            ch_v "Don't make me tell you again today."
        elif Taboo and "no_taboo" in JubesX.daily_history:
            ch_v "I told you, not here, [JubesX.player_petname]."
        elif not JubesX.action_counter["fondle_pussy"]:
            $ JubesX.change_face("bemused")
            ch_v "I don't think we're there yet, [JubesX.player_petname]. . ."
        else:
            $ JubesX.change_face("bemused")
            ch_v "You wish."
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle pussy" in JubesX.daily_history:
                $ JubesX.change_face("bemused")
                ch_v "Yeah, whatever."
                return
            "Maybe later?" if "no_fondle pussy" not in JubesX.daily_history:
                $ JubesX.change_face("sexy")
                ch_v "Maybe, [JubesX.player_petname]."
                $ JubesX.change_stat("love", 80, 2)
                $ JubesX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ JubesX.recent_history.append("no_taboo")
                    $ JubesX.daily_history.append("no_taboo")
                $ JubesX.recent_history.append("no_fondle pussy")
                $ JubesX.daily_history.append("no_fondle pussy")
                return
            "Come on, Please?":
                if Approval:
                    $ JubesX.change_face("sexy")
                    $ JubesX.change_stat("obedience", 90, 2)
                    $ JubesX.change_stat("obedience", 50, 2)
                    $ JubesX.change_stat("inhibition", 70, 3)
                    $ JubesX.change_stat("inhibition", 40, 2)
                    ch_v "Oooh, beg for me. . ."
                    jump Jubes_FP_Prep
                else:
                    $ JubesX.change_face("sexy")
                    ch_v "No."
            "[[Start fondling anyway]":

                $ Approval = ApprovalCheck(JubesX, 450, "OI", TabM = 2)
                if Approval > 1 or (Approval and JubesX.Forced):
                    $ JubesX.change_face("sad")
                    $ JubesX.change_stat("love", 70, -5, 1)
                    $ JubesX.change_stat("love", 200, -2)
                    ch_v "Ok, fine. . ."
                    $ JubesX.change_stat("obedience", 50, 4)
                    $ JubesX.change_stat("inhibition", 80, 1)
                    $ JubesX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ JubesX.Forced = 1
                    jump Jubes_FP_Prep
                else:
                    $ JubesX.change_stat("love", 200, -15)
                    $ JubesX.change_face("angry", 1)
                    "She slaps your hand away."
                    $ JubesX.recent_history.append("angry")
                    $ JubesX.daily_history.append("angry")

    if "no_fondle pussy" in JubesX.daily_history:
        ch_v "I'm pretty clear on this, NO."
        $ JubesX.recent_history.append("angry")
        $ JubesX.daily_history.append("angry")
    elif JubesX.Forced:
        $ JubesX.change_face("angry", 1)
        ch_v "I don't think so, [JubesX.player_petname]."
        $ JubesX.change_stat("lust", 70, 5)
        $ JubesX.change_stat("obedience", 50, -2)
        $ JubesX.recent_history.append("angry")
        $ JubesX.daily_history.append("angry")
    elif Taboo:
        $ JubesX.change_face("angry", 1)
        $ JubesX.recent_history.append("no_taboo")
        $ JubesX.daily_history.append("no_taboo")
        ch_v "I don't wanna make a scene."
    elif JubesX.action_counter["fondle_pussy"]:
        $ JubesX.change_face("sad")
        ch_v "Sorry, keep your fingers outside."
    else:
        $ JubesX.change_face("sexy")
        $ JubesX.mouth = "sad"
        ch_v "No thank you, [JubesX.player_petname]."
    $ JubesX.recent_history.append("no_fondle pussy")
    $ JubesX.daily_history.append("no_fondle pussy")
    $ approval_bonus = 0
    return

label Jubes_FP_Prep:
    if offhand_action == "fondle_pussy":
        return

    call Jubes_Pussy_Launch ("fondle_pussy")

    if action_context == JubesX:

        $ action_context = 0
        if (JubesX.legs and not JubesX.Upskirt) or (JubesX.underwear and not JubesX.underwearDown):

            if ApprovalCheck(JubesX, 1250, TabM = 1) or (JubesX.SeenPussy and ApprovalCheck(JubesX, 500) and not Taboo):
                $ JubesX.Upskirt = 1
                $ JubesX.underwearDown = 1
                $ Line = 0
                if JubesX.PantsNum() == 5:
                    $ Line = JubesX.name + " hikes up her_skirt"
                elif JubesX.PantsNum() >= 6:
                    $ Line = JubesX.name + " pulls down her " + JubesX.legs
                else:
                    $ Line = 0
                if JubesX.underwear:
                    if Line:

                        "[Line] and pulls her [JubesX.underwear] out of the way."
                        "She then grabs your arm and then presses your hand against her crotch, clearly intending you to get to work."
                    else:

                        "She pulls her [JubesX.underwear] out of the way, and then presses your hand against her crotch."
                        "She clearly intends for you to get to work."
                else:

                    "[Line], and then presses your hand against her crotch."
                    "She clearly intends for you to get to work."
                call Jubes_First_Bottomless (1)
            else:
                "[JubesX.name] grabs your arm and presses your hand against her crotch, clearly intending you to get to work."
        else:
            "[JubesX.name] grabs your arm and presses your hand against her crotch, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ JubesX.change_stat("inhibition", 80, 3)
                $ JubesX.change_stat("inhibition", 50, 2)
                "You start to run your fingers along her pussy."
            "Praise her.":
                $ JubesX.change_face("sexy", 1)
                $ JubesX.change_stat("inhibition", 80, 3)
                ch_p "I like the initiative, [JubesX.petname]."
                $ JubesX.nameCheck()
                "You start to run your fingers along her pussy."
                $ JubesX.change_stat("love", 85, 1)
                $ JubesX.change_stat("obedience", 90, 1)
                $ JubesX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your hand back."
                $ JubesX.change_face("surprised")
                $ JubesX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [JubesX.petname]."
                $ JubesX.nameCheck()
                "[JubesX.name] pulls back."
                $ JubesX.change_stat("obedience", 90, 1)
                $ JubesX.change_stat("obedience", 50, 1)
                $ JubesX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ JubesX.AddWord(1,"refused","refused")
                return


    if not JubesX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (JubesX)
        if "angry" in JubesX.recent_history:
            return
    $ approval_bonus = 0

    if not JubesX.action_counter["fondle_pussy"]:
        if JubesX.Forced:
            $ JubesX.change_stat("love", 90, -50)
            $ JubesX.change_stat("obedience", 70, 35)
            $ JubesX.change_stat("inhibition", 80, 25)
        else:
            $ JubesX.change_stat("love", 90, 10)
            $ JubesX.change_stat("obedience", 70, 10)
            $ JubesX.change_stat("inhibition", 80, 15)
    if Taboo:
        $ JubesX.inhibition += int(Taboo/10)
        $ JubesX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ JubesX.DrainWord("no_taboo")
    $ JubesX.DrainWord("no_fondle pussy")
    $ JubesX.recent_history.append("fondle_pussy")
    $ JubesX.daily_history.append("fondle_pussy")
    call Jubes_Pussy_Launch ("fondle_pussy")
    $ action_speed = 1

label Jubes_FP_Cycle:
    while Round > 0:
        call ViewShift (JubesX, JubesX.pose, 0, "fondle_pussy")
        call shift_focus (JubesX)
        $ JubesX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass

                "I want to stick a finger in. . ." if action_speed != 2:
                    if JubesX.action_counter["finger_pussy"]:
                        $ action_speed = 2
                    else:
                        menu:
                            "Ask her first":
                                $ action_context = "shift"
                            "Don't ask first [[just stick it in]":
                                $ action_context = "auto"
                        call Jubes_Insert_Pussy

                "Pull back a bit. . ." if action_speed == 2:
                    $ action_speed = 0
                "Slap her ass":

                    call Slap_Ass (JubesX)
                    $ counter += 1
                    $ Round -= 1
                    jump Jubes_FP_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (JubesX, "menu")
                    jump Jubes_FP_Cycle
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
                                    "I want to lick your pussy.":
                                        $ action_context = "shift"
                                        call Jubes_FP_After
                                        call Jubes_Lick_Pussy
                                    "Just start licking":
                                        $ action_context = "auto"
                                        call Jubes_FP_After
                                        call Jubes_Lick_Pussy
                                    "Pull back to the thighs":
                                        $ action_context = "pullback"
                                        call Jubes_FP_After
                                        call Jubes_Fondle_Thighs
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Jubes_FP_After
                                        call Jubes_Dildo_Pussy
                                    "Never Mind":
                                        jump Jubes_FP_Cycle
                            else:
                                call Sex_Basic_Dialog (JubesX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Jubes_FP_After
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
                                    jump Jubes_FP_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jubes_FP_Cycle
                                "Never mind":
                                    jump Jubes_FP_Cycle

                        "Show her feet" if not ShowFeet and (JubesX.pose == "doggy" or JubesX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (JubesX.pose == "doggy" or JubesX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [JubesX.name]":

                            call Girl_Undress (JubesX)
                        "Clean up [JubesX.name] (locked)" if not JubesX.Spunk:
                            pass
                        "Clean up [JubesX.name]" if JubesX.Spunk:
                            call Girl_Cleanup (JubesX, "ask")
                        "Never mind":
                            jump Jubes_FP_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jubes_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jubes_FP_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jubes_Pos_Reset
                    $ Line = 0
                    jump Jubes_FP_After


        call shift_focus (JubesX)
        call Sex_Dialog (JubesX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or JubesX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (JubesX)
                if "angry" in JubesX.recent_history:
                    call Jubes_Pos_Reset
                    return
                $ JubesX.change_stat("lust", 200, 5)
                if 100 > JubesX.lust >= 70 and JubesX.session_orgasms < 2:
                    $ JubesX.recent_history.append("unsatisfied")
                    $ JubesX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jubes_FP_After
                $ Line = "came"

            if JubesX.lust >= 100:

                call Girl_Cumming (JubesX)
                if action_context == "shift" or "angry" in JubesX.recent_history:
                    jump Jubes_FP_After

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
                            jump Jubes_FP_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if JubesX.SEXP >= 100 or ApprovalCheck(JubesX, 1200, "LO"):
            pass
        elif counter == (5 + JubesX.action_counter["fondle_pussy"]):
            $ JubesX.brows = "confused"
            ch_v "Having fun?"
        elif JubesX.lust >= 80:
            pass
        elif counter == (15 + JubesX.action_counter["fondle_pussy"]) and JubesX.SEXP >= 15 and not ApprovalCheck(JubesX, 1500):
            $ JubesX.brows = "confused"
            menu:
                ch_v "Could we maybe try. . . something else?"
                "Finish up.":
                    "You let go. . ."
                    jump Jubes_FP_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Jubes_FP_After
                "No, this is fun.":
                    if ApprovalCheck(JubesX, 1200) or ApprovalCheck(JubesX, 500, "O"):
                        $ JubesX.change_stat("love", 200, -5)
                        $ JubesX.change_stat("obedience", 50, 3)
                        $ JubesX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ JubesX.change_face("angry", 1)
                        call Jubes_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_v "This is kinda boring. . ."
                        $ JubesX.change_stat("love", 50, -3, 1)
                        $ JubesX.change_stat("love", 80, -4, 1)
                        $ JubesX.change_stat("obedience", 30, -1, 1)
                        $ JubesX.change_stat("obedience", 50, -1, 1)
                        $ JubesX.recent_history.append("angry")
                        $ JubesX.daily_history.append("angry")
                        jump Jubes_FP_After


        call Escalation (JubesX)

        if Round == 10:
            call Sex_Basic_Dialog (JubesX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JubesX, 5)


    $ JubesX.change_face("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JubesX, "done")


label Jubes_FP_After:
    if not action_context:
        call Jubes_Pos_Reset

    $ JubesX.change_face("sexy")

    $ JubesX.action_counter["fondle_pussy"] += 1
    $ JubesX.remaining_actions -=1
    if JubesX.PantsNum() < 6 or JubesX.Upskirt:
        $ JubesX.addiction_rate += 1
        if "addictive" in Player.Traits:
            $ JubesX.addiction_rate += 1

    call Partner_Like (JubesX, 2)

    if JubesX.action_counter["fondle_pussy"] == 1:
        $ JubesX.SEXP += 7
        if not action_context:
            if JubesX.love >= 500 and "unsatisfied" not in JubesX.recent_history:
                ch_v "Wow. . . that was nice. . ."
            elif JubesX.obedience <= 500 and Player.focus <= 20:
                $ JubesX.change_face("perplexed", 1)
                ch_v "Did you find anything in there?"

    $ approval_bonus = 0


    call Checkout
    return




label Jubes_Insert_Pussy:
    call shift_focus (JubesX)
    if action_context == "auto":
        if ApprovalCheck(JubesX, 1100, TabM = 2):
            $ JubesX.change_face("surprised")
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_stat("obedience", 70, 2)
            $ JubesX.change_stat("inhibition", 70, 3)
            $ JubesX.change_stat("inhibition", 30, 2)
            "As you slide a finger in, [JubesX.name] seems a bit surprised, but seems into it."
            jump Jubes_IP_Prep
        else:
            $ JubesX.change_face("surprised",2)
            $ JubesX.change_stat("love", 80, -2)
            $ JubesX.change_stat("obedience", 50, -3)
            ch_v "Oooh!"
            "She slaps your hand back."
            $ JubesX.change_face("perplexed",1)
            ch_v "Watch your hands, or lose them."
            return

    if ApprovalCheck(JubesX, 1100, TabM = 2):
        if JubesX.Forced:
            $ JubesX.change_face("sad")
            $ JubesX.change_stat("love", 70, -3, 1)
            $ JubesX.change_stat("love", 20, -2, 1)
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_stat("inhibition", 60, 1)
            ch_v "Going there, huh. . ."
        else:
            $ JubesX.change_face("sexy", 1)
            $ JubesX.change_stat("love", 90, 1)
            $ JubesX.change_stat("inhibition", 50, 3)
            ch_v "Mmmmmm. . ."
        $ JubesX.change_stat("obedience", 20, 1)
        $ JubesX.change_stat("obedience", 60, 1)
        $ JubesX.change_stat("inhibition", 70, 2)
        jump Jubes_IP_Prep
    else:

        $ JubesX.change_face("bemused", 1)
        ch_v "Nope."
        $ JubesX.blushing = 0
    return


label Jubes_IP_Prep:
    if not JubesX.action_counter["finger_pussy"]:
        $ JubesX.action_counter["finger_pussy"] = 1
        $ JubesX.SEXP += 10
        if JubesX.Forced:
            $ JubesX.change_stat("love", 90, -60)
            $ JubesX.change_stat("obedience", 70, 55)
            $ JubesX.change_stat("inhibition", 80, 35)
        else:
            $ JubesX.change_stat("love", 90, 10)
            $ JubesX.change_stat("obedience", 70, 20)
            $ JubesX.change_stat("inhibition", 80, 25)

    if not JubesX.Forced and action_context != "auto":
        call Girl_Undress (JubesX, "bottom")
        if "angry" in JubesX.recent_history:
            return


    if Taboo:
        $ JubesX.inhibition += int(Taboo/10)
        $ JubesX.lust += int(Taboo/5)

    $ Line = 0
    $ action_speed = 2
    return







label Jubes_Lick_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JubesX)

    if JubesX.action_counter["eat_pussy"]:
        $ approval_bonus += 15
    if JubesX.PantsNum() >= 6 or JubesX.HoseNum() >= 5:
        $ approval_bonus -= 15
    if JubesX.lust > 95:
        $ approval_bonus += 20
    elif JubesX.lust > 85:
        $ approval_bonus += 15
    if action_context == "shift":
        $ approval_bonus += 10
    if JubesX.lust > 85 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in JubesX.Traits:
        $ approval_bonus += (4*Taboo)
    if JubesX in Player.Harem or "sex friend" in JubesX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JubesX.Traits:
        $ approval_bonus -= 25
    if JubesX.event_counter["forced"] and not JubesX.Forced:
        $ approval_bonus -= 5*JubesX.event_counter["forced"]

    if Taboo and "no_taboo" in JubesX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in JubesX.history:
        $ approval_bonus -= 20

    if "no_lick pussy" in JubesX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_lick pussy" in JubesX.recent_history else 0

    $ Approval = ApprovalCheck(JubesX, 1250, TabM = 4)

    if action_context == "auto":
        if Approval:
            $ JubesX.change_face("surprised")
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_stat("obedience", 70, 2)
            $ JubesX.change_stat("inhibition", 70, 3)
            $ JubesX.change_stat("inhibition", 30, 2)
            "As you crouch down and start to lick her pussy, [JubesX.name] starts, but then softens."
            $ JubesX.change_face("sexy")
            jump Jubes_LP_Prep
        else:
            $ JubesX.change_face("surprised")
            $ JubesX.change_stat("love", 80, -2)
            $ JubesX.change_stat("obedience", 50, -3)
            ch_v "Hey, good instincts, but maybe hold off?"
            $ JubesX.change_face("perplexed",1)
            "She pushes your head back away from her."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "eat_pussy" in JubesX.recent_history:
        $ JubesX.change_face("sexy", 1)
        ch_v "Mmmm, again? I guess. . ."
        jump Jubes_LP_Prep
    elif "eat_pussy" in JubesX.daily_history:
        $ JubesX.change_face("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Huh? Again?",
            "I must have done something right.",
            "I guess fair's fair. . .",
            "Mmm. . ."])
        ch_v "[Line]"

    if Approval >= 2:
        if JubesX.Forced:
            $ JubesX.change_face("sad")
            $ JubesX.change_stat("love", 70, -3, 1)
            $ JubesX.change_stat("love", 20, -2, 1)
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_stat("inhibition", 60, 1)
            ch_v "If you haveta. . ."
        else:
            $ JubesX.change_face("sexy", 1)
            $ JubesX.eyes = "closed"
            $ JubesX.change_stat("love", 90, 1)
            $ JubesX.change_stat("inhibition", 50, 3)
            $ JubesX.change_stat("lust", 200, 3)
            ch_v "Mmmmmm. . ."
        $ JubesX.change_stat("obedience", 20, 1)
        $ JubesX.change_stat("obedience", 60, 1)
        $ JubesX.change_stat("inhibition", 70, 2)
        jump Jubes_LP_Prep
    else:

        $ JubesX.change_face("angry", 1)
        if "no_lick pussy" in JubesX.recent_history:
            ch_v "I already told you, \"no\"."
        elif Taboo and "no_taboo" in JubesX.daily_history and "no_lick pussy" in JubesX.daily_history:
            ch_v "You already got your answer!"
        elif "no_lick pussy" in JubesX.daily_history:
            ch_v "Don't make me tell you again today."
        elif Taboo and "no_taboo" in JubesX.daily_history:
            ch_v "I told you, not here, [JubesX.player_petname]."
        elif not JubesX.action_counter["eat_pussy"]:
            $ JubesX.change_face("bemused")
            ch_v "I'm not sure we're there yet, [JubesX.player_petname]. . ."
        else:
            $ JubesX.change_face("bemused")
            ch_v "I'm really not cool with that. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_lick pussy" in JubesX.daily_history:
                $ JubesX.change_face("bemused")
                ch_v "Yeah, whatever."
                return
            "I'm sure I can convince you later. . ." if "no_lick pussy" not in JubesX.daily_history:
                $ JubesX.change_face("sexy")
                ch_v "I'll be thinking about it, [JubesX.player_petname]."
                $ JubesX.change_stat("love", 80, 2)
                $ JubesX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ JubesX.recent_history.append("no_taboo")
                    $ JubesX.daily_history.append("no_taboo")
                $ JubesX.recent_history.append("no_lick pussy")
                $ JubesX.daily_history.append("no_lick pussy")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ JubesX.change_face("sexy")
                    $ JubesX.change_stat("obedience", 90, 2)
                    $ JubesX.change_stat("obedience", 50, 2)
                    ch_v "You make a good point. . ."
                    $ JubesX.change_stat("inhibition", 70, 3)
                    $ JubesX.change_stat("inhibition", 40, 2)
                    jump Jubes_LP_Prep
                else:
                    $ JubesX.change_face("sexy")
                    ch_v "I would, but still no, [JubesX.player_petname]."
            "[[Get in there anyway]":

                $ Approval = ApprovalCheck(JubesX, 750, "OI", TabM = 4)
                if Approval > 1 or (Approval and JubesX.Forced):
                    $ JubesX.change_face("sad")
                    $ JubesX.change_stat("love", 70, -5, 1)
                    $ JubesX.change_stat("love", 200, -2)
                    ch_v "Well I don't want to get in your way. . ."
                    $ JubesX.change_stat("obedience", 50, 4)
                    $ JubesX.change_stat("inhibition", 80, 1)
                    $ JubesX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ JubesX.Forced = 1
                    jump Jubes_LP_Prep
                else:
                    $ JubesX.change_stat("love", 200, -15)
                    $ JubesX.change_face("angry", 1)
                    "She shoves your head back."
                    $ JubesX.recent_history.append("angry")
                    $ JubesX.daily_history.append("angry")

    if "no_lick pussy" in JubesX.daily_history:
        ch_v "I'm pretty clear on this, NO."
        $ JubesX.recent_history.append("angry")
        $ JubesX.daily_history.append("angry")
    elif JubesX.Forced:
        $ JubesX.change_face("angry", 1)
        ch_v "I really can't, [JubesX.player_petname]."
        $ JubesX.change_stat("lust", 80, 5)
        $ JubesX.change_stat("obedience", 50, -2)
        $ JubesX.recent_history.append("angry")
        $ JubesX.daily_history.append("angry")
    elif Taboo:
        $ JubesX.change_face("angry", 1)
        $ JubesX.recent_history.append("no_taboo")
        $ JubesX.daily_history.append("no_taboo")
        ch_v "I don't wanna make a scene."
    elif JubesX.action_counter["eat_pussy"]:
        $ JubesX.change_face("sad")
        ch_v "Keep your head out of there."
    else:
        $ JubesX.change_face("surprised")
        ch_v "Yeah, sorry."
        $ JubesX.change_face()
    $ JubesX.recent_history.append("no_lick pussy")
    $ JubesX.daily_history.append("no_lick pussy")
    $ approval_bonus = 0
    return

label Jubes_LP_Prep:
    if offhand_action == "eat_pussy":
        return

    $ approval_bonus = 0
    call Jubes_Pussy_Launch ("eat_pussy")

    if action_context == JubesX:

        $ action_context = 0
        if (JubesX.legs and not JubesX.Upskirt) or (JubesX.underwear and not JubesX.underwearDown):

            if ApprovalCheck(JubesX, 1250, TabM = 1) or (JubesX.SeenPussy and ApprovalCheck(JubesX, 500) and not Taboo):
                $ JubesX.Upskirt = 1
                $ JubesX.underwearDown = 1
                $ Line = 0
                if JubesX.PantsNum() == 5:
                    $ Line = JubesX.name + " hikes up her_skirt"
                elif JubesX.PantsNum() >= 6:
                    $ Line = JubesX.name + " pulls down her " + JubesX.legs
                else:
                    $ Line = 0
                if JubesX.underwear:
                    if Line:

                        "[Line] and pulls her [JubesX.underwear] out of the way."
                        "She then grabs your head and wraps her thighs around it, clearly intending you to get to work."
                    else:

                        "She pulls her [JubesX.underwear] out of the way, and then wraps her thighs around your head."
                        "She clearly intends for you to get to work."
                else:

                    "[Line], and then wraps her thighs around your head."
                    "She clearly intends for you to get to work."
                call Jubes_First_Bottomless (1)
            else:
                "[JubesX.name] grabs your head and wraps her thighs around it, clearly intending you to get to work."
        else:
            "[JubesX.name] grabs your head and wraps her thighs around it, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ JubesX.change_stat("inhibition", 80, 3)
                $ JubesX.change_stat("inhibition", 50, 2)
                "You start licking."
            "Praise her.":
                $ JubesX.change_face("sexy", 1)
                $ JubesX.change_stat("inhibition", 80, 3)
                ch_p "Mmm, I like this idea, [JubesX.petname]."
                $ JubesX.nameCheck()
                "You start licking."
                $ JubesX.change_stat("love", 85, 1)
                $ JubesX.change_stat("obedience", 90, 1)
                $ JubesX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your head away."
                $ JubesX.change_face("surprised")
                $ JubesX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [JubesX.petname]."
                $ JubesX.nameCheck()
                "[JubesX.name] pulls back."
                $ JubesX.change_stat("obedience", 90, 1)
                $ JubesX.change_stat("obedience", 50, 1)
                $ JubesX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ JubesX.AddWord(1,"refused","refused")
                return


    if not JubesX.Forced and action_context != "auto":
        $ approval_bonus = 0
        if JubesX.PantsNum() >= 6 and not JubesX.Upskirt:
            $ approval_bonus = 15
        call Bottoms_Off (JubesX)
        if "angry" in JubesX.recent_history:
            return

    if not JubesX.action_counter["eat_pussy"]:
        if JubesX.Forced:
            $ JubesX.change_stat("love", 90, -30)
            $ JubesX.change_stat("obedience", 70, 35)
            $ JubesX.change_stat("inhibition", 80, 75)
        else:
            $ JubesX.change_stat("love", 90, 35)
            $ JubesX.change_stat("obedience", 70, 15)
            $ JubesX.change_stat("inhibition", 80, 35)
    if Taboo:
        $ JubesX.inhibition += int(Taboo/10)
        $ JubesX.lust += int(Taboo/5)
    if action_context:
        $ renpy.pop_call()
        $ action_context = 0

    if JubesX.PantsNum() == 5:
        $ JubesX.Upskirt = 1
        $ JubesX.SeenPanties = 1
    call Jubes_First_Bottomless (1)

    $ Line = 0
    $ counter = 0
    if Taboo:
        $ JubesX.DrainWord("no_taboo")
    $ JubesX.DrainWord("no_lick pussy")
    $ JubesX.recent_history.append("eat_pussy")
    $ JubesX.daily_history.append("eat_pussy")
    call Jubes_Pussy_Launch ("eat_pussy")

label Jubes_LP_Cycle:
    if offhand_action == "kiss":
        $ offhand_action = 0
    while Round > 0:
        call ViewShift (JubesX, JubesX.pose, 0, "eat_pussy")
        call shift_focus (JubesX)
        $ JubesX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (JubesX)
                    $ counter += 1
                    $ Round -= 1
                    jump Jubes_LP_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (JubesX, "menu")
                    jump Jubes_LP_Cycle
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
                                    "Pull out and start rubbing again.":
                                        if JubesX.remaining_actions and multi_action:
                                            $ action_context = "pullback"
                                            call Jubes_LP_After
                                            call Jubes_Fondle_Pussy
                                        else:
                                            call Sex_Basic_Dialog (JubesX, "tired")
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Jubes_LP_After
                                        call Jubes_Dildo_Pussy
                                    "Never Mind":
                                        jump Jubes_LP_Cycle
                            else:
                                call Sex_Basic_Dialog (JubesX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Jubes_LP_After
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
                                    jump Jubes_LP_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jubes_LP_Cycle
                                "Never mind":
                                    jump Jubes_LP_Cycle

                        "Show her feet" if not ShowFeet and (JubesX.pose == "doggy" or JubesX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (JubesX.pose == "doggy" or JubesX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [JubesX.name]":

                            call Girl_Undress (JubesX)
                        "Clean up [JubesX.name] (locked)" if not JubesX.Spunk:
                            pass
                        "Clean up [JubesX.name]" if JubesX.Spunk:
                            call Girl_Cleanup (JubesX, "ask")
                        "Never mind":
                            jump Jubes_LP_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jubes_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jubes_LP_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jubes_Pos_Reset
                    $ Line = 0
                    jump Jubes_LP_After


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
                if "angry" in JubesX.recent_history:
                    call Jubes_Pos_Reset
                    return
                $ JubesX.change_stat("lust", 200, 5)
                if 100 > JubesX.lust >= 70 and JubesX.session_orgasms < 2:
                    $ JubesX.recent_history.append("unsatisfied")
                    $ JubesX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jubes_LP_After
                $ Line = "came"

            if JubesX.lust >= 100:

                call Girl_Cumming (JubesX)
                if action_context == "shift" or "angry" in JubesX.recent_history:
                    jump Jubes_LP_After

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
                            jump Jubes_LP_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if JubesX.SEXP >= 100 or ApprovalCheck(JubesX, 1200, "LO"):
            pass
        elif counter == (5 + JubesX.action_counter["eat_pussy"]):
            $ JubesX.brows = "confused"
            ch_v "Yeah, I like that too. . ."
        elif JubesX.lust >= 80:
            pass
        elif counter == (15 + JubesX.action_counter["eat_pussy"]) and JubesX.SEXP >= 15 and not ApprovalCheck(JubesX, 1500):
            $ JubesX.brows = "confused"
            menu:
                ch_v "Could we maybe try. . . something else?"
                "Finish up.":
                    "You let go. . ."
                    jump Jubes_LP_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Jubes_LP_After
                "No, this is fun.":
                    if ApprovalCheck(JubesX, 1200) or ApprovalCheck(JubesX, 500, "O"):
                        $ JubesX.change_stat("love", 200, -5)
                        $ JubesX.change_stat("obedience", 50, 3)
                        $ JubesX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ JubesX.change_face("angry", 1)
                        call Jubes_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_v "This is kinda boring. . ."
                        $ JubesX.change_stat("love", 50, -3, 1)
                        $ JubesX.change_stat("love", 80, -4, 1)
                        $ JubesX.change_stat("obedience", 30, -1, 1)
                        $ JubesX.change_stat("obedience", 50, -1, 1)
                        $ JubesX.recent_history.append("angry")
                        $ JubesX.daily_history.append("angry")
                        jump Jubes_LP_After


        call Escalation (JubesX)

        if Round == 10:
            call Sex_Basic_Dialog (JubesX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JubesX, 5)


    $ JubesX.change_face("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JubesX, "done")


label Jubes_LP_After:
    if not action_context:
        call Jubes_Pos_Reset

    $ JubesX.change_face("sexy")

    $ JubesX.action_counter["eat_pussy"] += 1
    $ JubesX.remaining_actions -=1
    if JubesX.PantsNum() < 6 or JubesX.Upskirt:
        $ JubesX.addiction_rate += 1
        if "addictive" in Player.Traits:
            $ JubesX.addiction_rate += 1

    if Partner == "Rogue":
        call Partner_Like (JubesX, 3, 2)
    else:
        call Partner_Like (JubesX, 2)

    if JubesX.action_counter["eat_pussy"] == 1:
        $ JubesX.SEXP += 10
        if not action_context:
            if JubesX.love >= 500 and "unsatisfied" not in JubesX.recent_history:
                ch_v "You really give me a run for my money. . ."
            elif JubesX.obedience <= 500 and Player.focus <= 20:
                $ JubesX.change_face("perplexed", 1)
                ch_v "Well, that wasn't so bad. . ."

    $ approval_bonus = 0


    call Checkout
    return






label Jubes_Fondle_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JubesX)

    if JubesX.action_counter["fondle_ass"]:
        $ approval_bonus += 10
    if JubesX.PantsNum() >= 6 or JubesX.HoseNum() >= 5:
        $ approval_bonus -= 5
    if JubesX.lust > 75:
        $ approval_bonus += 15
    if "exhibitionist" in JubesX.Traits:
        $ approval_bonus += Taboo
    if JubesX in Player.Harem or "sex friend" in JubesX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JubesX.Traits:
        $ approval_bonus -= 25
    if JubesX.event_counter["forced"] and not JubesX.Forced:
        $ approval_bonus -= 5*JubesX.event_counter["forced"]

    if Taboo and "no_taboo" in JubesX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in JubesX.history:
        $ approval_bonus -= 20

    if "no_fondle ass" in JubesX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle ass" in JubesX.recent_history else 0

    $ Approval = ApprovalCheck(JubesX, 850, TabM=1)

    if action_context == "auto":
        if Approval:
            $ JubesX.change_face("surprised", 1)
            $ JubesX.change_stat("obedience", 70, 2)
            $ JubesX.change_stat("inhibition", 40, 2)
            "As your hand creeps down her backside, [JubesX.name] shivers a bit, and then relaxes."
            $ JubesX.change_face("sexy")
            jump Jubes_FA_Prep
        else:
            $ JubesX.change_face("surprised")
            $ JubesX.change_stat("obedience", 50, -3)
            ch_v "Hands off, [JubesX.player_petname]."
            $ JubesX.change_face("bemused")
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if action_context == "pullback":
        $ JubesX.change_face("surprised")
        $ JubesX.brows = "sad"
        if JubesX.lust > 80:
            $ JubesX.change_stat("love", 70, -4)
        $ JubesX.change_stat("obedience", 90, 1)
        $ JubesX.change_stat("obedience", 70, 2)
        "As your finger slides out, [JubesX.name] gasps and looks upset."
        jump Jubes_FA_Prep
    elif "fondle_ass" in JubesX.recent_history:
        $ JubesX.change_face("sexy", 1)
        ch_v "Mmmm, again? I guess. . ."
        jump Jubes_FA_Prep
    elif "fondle_ass" in JubesX.daily_history:
        $ JubesX.change_face("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Mmm, you like that? . .",
            "Mmm. . ."])
        ch_v "[Line]"

    if Approval >= 2:
        if JubesX.Forced:
            $ JubesX.change_face("sad")
            $ JubesX.change_stat("love", 70, -2, 1)
            $ JubesX.change_stat("obedience", 90, 2)
            $ JubesX.change_stat("inhibition", 60, 2)
            ch_v "If you insist. . ."
        else:
            $ JubesX.change_face("bemused, 1")
            ch_v "Yeah, ok. . ."
        $ JubesX.change_stat("lust", 200, 3)
        $ JubesX.change_stat("obedience", 60, 1)
        $ JubesX.change_stat("inhibition", 70, 1)
        jump Jubes_FA_Prep
    else:

        $ JubesX.change_face("angry", 1)
        if "no_fondle ass" in JubesX.recent_history:
            ch_v "I already told you, \"no\"."
        elif Taboo and "no_taboo" in JubesX.daily_history and "no_fondle ass" in JubesX.daily_history:
            ch_v "I told you not to touch me like that in public!"
        elif "no_fondle ass" in JubesX.daily_history:
            ch_v "Don't make me tell you again today."
        elif Taboo and "no_taboo" in JubesX.daily_history:
            ch_v "I told you, not here, [JubesX.player_petname]."
        elif not JubesX.action_counter["fondle_ass"]:
            $ JubesX.change_face("bemused")
            ch_v "Not yet, [JubesX.player_petname]. . ."
        else:
            $ JubesX.change_face("bemused")
            ch_v "Let's not, ok [JubesX.player_petname]?"
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle ass" in JubesX.daily_history:
                $ JubesX.change_face("bemused")
                ch_v "Yeah, whatever."
                return
            "Maybe later?" if "no_fondle ass" not in JubesX.daily_history:
                $ JubesX.change_face("sexy")
                ch_v "Maybe?"
                $ JubesX.change_stat("love", 80, 2)
                $ JubesX.change_stat("inhibition", 50, 2)
                if Taboo:
                    $ JubesX.recent_history.append("no_taboo")
                    $ JubesX.daily_history.append("no_taboo")
                $ JubesX.recent_history.append("no_fondle ass")
                $ JubesX.daily_history.append("no_fondle ass")
                return
            "Just one good squeeze?":
                if Approval:
                    $ JubesX.change_face("sexy")
                    $ JubesX.change_stat("obedience", 90, 1)
                    $ JubesX.change_stat("obedience", 50, 2)
                    ch_v "Oooh, beg for me. . ."
                    $ JubesX.change_stat("inhibition", 70, 1)
                    $ JubesX.change_stat("inhibition", 40, 2)
                    jump Jubes_FA_Prep
                else:
                    $ JubesX.change_face("sexy")
                    ch_v "No."
            "[[Start fondling anyway]":

                $ Approval = ApprovalCheck(JubesX, 250, "OI", TabM = 3)
                if Approval > 1 or (Approval and JubesX.Forced):
                    $ JubesX.change_face("sad")
                    $ JubesX.change_stat("love", 70, -3, 1)
                    $ JubesX.change_stat("love", 200, -1)
                    ch_v "Fine, I guess."
                    $ JubesX.change_stat("obedience", 50, 3)
                    $ JubesX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ JubesX.Forced = 1
                    jump Jubes_FA_Prep
                else:
                    $ JubesX.change_stat("love", 200, -10)
                    $ JubesX.change_face("angry", 1)
                    "She slaps your hand away."
                    $ JubesX.recent_history.append("angry")
                    $ JubesX.daily_history.append("angry")

    if "no_fondle ass" in JubesX.daily_history:
        ch_v "I'm pretty clear on this, NO."
        $ JubesX.recent_history.append("angry")
        $ JubesX.daily_history.append("angry")
    elif JubesX.Forced:
        $ JubesX.change_face("angry", 1)
        ch_v "Do you want to keep those fingers?"
        $ JubesX.change_stat("lust", 60, 5)
        $ JubesX.change_stat("obedience", 50, -2)
        $ JubesX.recent_history.append("angry")
        $ JubesX.daily_history.append("angry")
    elif Taboo:
        $ JubesX.change_face("angry", 1)
        $ JubesX.recent_history.append("no_taboo")
        $ JubesX.daily_history.append("no_taboo")
        ch_v "I don't wanna make a scene."
    elif JubesX.action_counter["fondle_ass"]:
        $ JubesX.change_face("sad")
        ch_v "Sorry, keep your hands to yourself."
    else:
        $ JubesX.change_face("sexy")
        $ JubesX.mouth = "sad"
        ch_v "No."
    $ JubesX.recent_history.append("no_fondle ass")
    $ JubesX.daily_history.append("no_fondle ass")
    $ approval_bonus = 0
    return

ch_v "Sorry, I don't even know how I got here. . ."
return

label Jubes_FA_Prep:
    if offhand_action == "fondle_ass":
        return
    if not JubesX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (JubesX)
        if "angry" in JubesX.recent_history:
            return
    $ approval_bonus = 0
    call Jubes_Pussy_Launch ("fondle_ass")
    if not JubesX.action_counter["fondle_ass"]:
        if JubesX.Forced:
            $ JubesX.change_stat("love", 90, -20)
            $ JubesX.change_stat("obedience", 70, 20)
            $ JubesX.change_stat("inhibition", 80, 15)
        else:
            $ JubesX.change_stat("love", 90, 10)
            $ JubesX.change_stat("obedience", 70, 12)
            $ JubesX.change_stat("inhibition", 80, 20)
    if Taboo:
        $ JubesX.inhibition += int(Taboo/10)
        $ JubesX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ JubesX.DrainWord("no_taboo")
    $ JubesX.DrainWord("no_fondle ass")
    $ JubesX.recent_history.append("fondle_ass")
    $ JubesX.daily_history.append("fondle_ass")
    call Jubes_Pussy_Launch ("fondle_ass")

label Jubes_FA_Cycle:
    while Round > 0:
        call ViewShift (JubesX, JubesX.pose, 0, "fondle_ass")
        call shift_focus (JubesX)
        $ JubesX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (JubesX)
                    $ counter += 1
                    $ Round -= 1
                    jump Jubes_FA_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (JubesX, "menu")
                    jump Jubes_FA_Cycle
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
                                    "I want to stick a finger in.":
                                        $ action_context = "shift"
                                        call Jubes_FA_After
                                        call Jubes_Insert_Ass
                                    "Just stick a finger in without asking.":
                                        $ action_context = "auto"
                                        call Jubes_FA_After
                                        call Jubes_Insert_Ass
                                    "I want to lick your asshole.":
                                        $ action_context = "shift"
                                        call Jubes_FA_After
                                        call Jubes_Lick_Ass
                                    "Just start licking.":
                                        $ action_context = "auto"
                                        call Jubes_FA_After
                                        call Jubes_Lick_Ass
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Jubes_FA_After
                                        call Jubes_Dildo_Ass
                                    "Never Mind":
                                        jump Jubes_FA_Cycle
                            else:
                                call Sex_Basic_Dialog (JubesX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Jubes_FA_After
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
                                    jump Jubes_FA_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jubes_FA_Cycle
                                "Never mind":
                                    jump Jubes_FA_Cycle

                        "Show her feet" if not ShowFeet and (JubesX.pose == "doggy" or JubesX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (JubesX.pose == "doggy" or JubesX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [JubesX.name]":

                            call Girl_Undress (JubesX)
                        "Clean up [JubesX.name] (locked)" if not JubesX.Spunk:
                            pass
                        "Clean up [JubesX.name]" if JubesX.Spunk:
                            call Girl_Cleanup (JubesX, "ask")
                        "Never mind":
                            jump Jubes_FA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jubes_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jubes_FA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jubes_Pos_Reset
                    $ Line = 0
                    jump Jubes_FA_After


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
                if "angry" in JubesX.recent_history:
                    call Jubes_Pos_Reset
                    return
                $ JubesX.change_stat("lust", 200, 5)
                if 100 > JubesX.lust >= 70 and JubesX.session_orgasms < 2 and JubesX.SEXP >= 20:
                    $ JubesX.recent_history.append("unsatisfied")
                    $ JubesX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jubes_FA_After
                $ Line = "came"

            if JubesX.lust >= 100:

                call Girl_Cumming (JubesX)
                if action_context == "shift" or "angry" in JubesX.recent_history:
                    jump Jubes_FA_After

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
                            jump Jubes_FA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if JubesX.SEXP >= 100 or ApprovalCheck(JubesX, 1200, "LO"):
            pass
        elif counter == (5 + JubesX.action_counter["fondle_ass"]):
            $ JubesX.brows = "confused"
            ch_v "Mmmm. . ."
        elif JubesX.lust >= 80:
            pass
        elif counter == (15 + JubesX.action_counter["fondle_ass"]) and JubesX.SEXP >= 15 and not ApprovalCheck(JubesX, 1500):
            $ JubesX.brows = "confused"
            menu:
                ch_v "Could we maybe try. . . something else?"
                "Finish up.":
                    "You let go. . ."
                    jump Jubes_FA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Jubes_FA_After
                "No, this is fun.":
                    if ApprovalCheck(JubesX, 1200) or ApprovalCheck(JubesX, 500, "O"):
                        $ JubesX.change_stat("love", 200, -5)
                        $ JubesX.change_stat("obedience", 50, 3)
                        $ JubesX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ JubesX.change_face("angry", 1)
                        call Jubes_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_v "This is kinda boring. . ."
                        $ JubesX.change_stat("love", 50, -3, 1)
                        $ JubesX.change_stat("love", 80, -4, 1)
                        $ JubesX.change_stat("obedience", 30, -1, 1)
                        $ JubesX.change_stat("obedience", 50, -1, 1)
                        $ JubesX.recent_history.append("angry")
                        $ JubesX.daily_history.append("angry")
                        jump Jubes_FA_After


        call Escalation (JubesX)

        if Round == 10:
            call Sex_Basic_Dialog (JubesX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JubesX, 5)


    $ JubesX.change_face("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JubesX, "done")


label Jubes_FA_After:
    if not action_context:
        call Jubes_Pos_Reset

    $ JubesX.change_face("sexy")

    $ JubesX.action_counter["fondle_ass"] += 1
    $ JubesX.remaining_actions -=1
    if JubesX.PantsNum() < 6 or JubesX.Upskirt:
        $ JubesX.addiction_rate += 1
        if "addictive" in Player.Traits:
            $ JubesX.addiction_rate += 1

        call Partner_Like (JubesX, 2)

    if JubesX.action_counter["fondle_ass"] == 1:
        $ JubesX.SEXP += 4
        if not action_context:
            if JubesX.love >= 500 and "unsatisfied" not in JubesX.recent_history:
                ch_v "That was. . . nice. . ."
            elif JubesX.obedience <= 500 and Player.focus <= 20:
                $ JubesX.change_face("perplexed", 1)
                ch_v "Did you like that?"

    $ approval_bonus = 0


    call Checkout
    return





label Jubes_Insert_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JubesX)

    if JubesX.action_counter["finger_ass"]:
        $ approval_bonus += 25
    if JubesX.PantsNum() >= 6 or JubesX.HoseNum() >= 5:
        $ approval_bonus -= 15
    if JubesX.lust > 85 and JubesX.used_to_anal:
        $ approval_bonus += 15
    if JubesX.lust > 95 and JubesX.used_to_anal:
        $ approval_bonus += 5
    if action_context == "shift":
        $ approval_bonus += 10
    if JubesX.lust > 85 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in JubesX.Traits:
        $ approval_bonus += (4*Taboo)
    if JubesX in Player.Harem or "sex friend" in JubesX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JubesX.Traits:
        $ approval_bonus -= 25
    if JubesX.event_counter["forced"] and not JubesX.Forced:
        $ approval_bonus -= 5*JubesX.event_counter["forced"]

    if Taboo and "no_taboo" in JubesX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in JubesX.history:
        $ approval_bonus -= 20

    if "no_insert ass" in JubesX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_insert ass" in JubesX.recent_history else 0

    $ Approval = ApprovalCheck(JubesX, 1300, TabM = 3)

    if action_context == "auto":
        if Approval:
            $ JubesX.change_face("surprised")
            $ JubesX.change_stat("obedience", 90, 2)
            $ JubesX.change_stat("obedience", 70, 2)
            $ JubesX.change_stat("inhibition", 80, 2)
            $ JubesX.change_stat("inhibition", 30, 2)
            "As you slide a finger in, [JubesX.name] tightens around it in surprise, but seems into it."
            $ JubesX.change_face("sexy")
            jump Jubes_IA_Prep
        else:
            $ JubesX.change_face("surprised")
            $ JubesX.change_stat("love", 80, -2)
            $ JubesX.change_stat("obedience", 50, -3)
            ch_v "Whoa, back off, [JubesX.player_petname]."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "finger_ass" in JubesX.daily_history and not JubesX.used_to_anal:
        $ JubesX.change_face("bemused", 1)
        ch_v "I'm still a little sore from earlier, [JubesX.player_petname]."
    elif "finger_ass" in JubesX.daily_history:
        $ JubesX.change_face("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax. . .",
            "Mmm. . ."])
        ch_v "[Line]"

    if Approval >= 2:
        if JubesX.Forced:
            $ JubesX.change_face("sad")
            $ JubesX.change_stat("love", 70, -3, 1)
            $ JubesX.change_stat("love", 20, -2, 1)
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_stat("inhibition", 60, 1)
            ch_v "If you haveta. . ."
        else:
            $ JubesX.change_face("sexy", 1)
            $ JubesX.eyes = "closed"
            $ JubesX.change_stat("love", 90, 1)
            $ JubesX.change_stat("inhibition", 50, 3)
            $ JubesX.change_stat("lust", 200, 3)
            ch_v "Mmmmm. . ."
        $ JubesX.change_stat("obedience", 20, 1)
        $ JubesX.change_stat("obedience", 60, 1)
        $ JubesX.change_stat("inhibition", 70, 2)
        jump Jubes_IA_Prep
    else:

        $ JubesX.change_face("angry", 1)
        if "no_insert ass" in JubesX.recent_history:
            ch_v "I already told you, \"no\"."
        elif Taboo and "no_taboo" in JubesX.daily_history and "no_insert ass" in JubesX.daily_history:
            ch_v "I told you that wasn't appropriate!"
        elif "no_insert ass" in JubesX.daily_history:
            ch_v "Don't make me tell you again today."
        elif Taboo and "no_taboo" in JubesX.daily_history:
            ch_v "I told you, not here, [JubesX.player_petname]."
        elif not JubesX.action_counter["finger_ass"]:
            $ JubesX.change_face("perplexed", 1)
            ch_v "That's really not my style. . ."
        else:
            $ JubesX.change_face("bemused")
            ch_v "I'd rather not today. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_insert ass" in JubesX.daily_history:
                $ JubesX.change_face("bemused")
                ch_v "Yeah, whatever."
                return
            "Maybe later?" if "no_insert ass" not in JubesX.daily_history:
                $ JubesX.change_face("sexy")
                ch_v "It's. . . possible, [JubesX.player_petname]."
                $ JubesX.change_stat("love", 80, 2)
                $ JubesX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ JubesX.recent_history.append("no_taboo")
                    $ JubesX.daily_history.append("no_taboo")
                $ JubesX.recent_history.append("no_insert ass")
                $ JubesX.daily_history.append("no_insert ass")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ JubesX.change_face("sexy")
                    $ JubesX.change_stat("obedience", 90, 2)
                    $ JubesX.change_stat("obedience", 50, 2)
                    ch_v "Um. . . maybe. . ."
                    $ JubesX.change_stat("inhibition", 70, 3)
                    $ JubesX.change_stat("inhibition", 40, 2)
                    jump Jubes_IA_Prep
                else:
                    $ JubesX.change_face("bemused")
                    ch_v "I really doubt that. . ."
            "[[Slide a finger in anyway]":

                $ Approval = ApprovalCheck(JubesX, 950, "OI", TabM = 3)
                if Approval > 1 or (Approval and JubesX.Forced):
                    $ JubesX.change_face("surprised", 1)
                    $ JubesX.change_stat("love", 70, -5, 1)
                    $ JubesX.change_stat("love", 200, -2)
                    ch_v "Um, hello? . ."
                    $ JubesX.change_face("sad")
                    $ JubesX.change_stat("obedience", 50, 4)
                    $ JubesX.change_stat("inhibition", 80, 1)
                    $ JubesX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ JubesX.Forced = 1
                    jump Jubes_IA_Prep
                else:
                    $ JubesX.change_stat("love", 200, -15)
                    $ JubesX.change_face("angry", 1)
                    "She slaps your hand away."
                    $ JubesX.recent_history.append("angry")
                    $ JubesX.daily_history.append("angry")

    if "no_insert ass" in JubesX.daily_history:
        ch_v "I'm pretty clear on this, NO."
        $ JubesX.recent_history.append("angry")
        $ JubesX.daily_history.append("angry")
    elif JubesX.Forced:
        $ JubesX.change_face("angry", 1)
        ch_v "I'm not going there today."
        if ApprovalCheck(JubesX, 500, "I"):
            $ JubesX.change_stat("lust", 80, 10)
        else:
            $ JubesX.change_stat("lust", 50, 3)
        $ JubesX.change_stat("obedience", 50, -2)
        $ JubesX.recent_history.append("angry")
        $ JubesX.daily_history.append("angry")
    elif Taboo:
        $ JubesX.change_face("angry", 1)
        $ JubesX.recent_history.append("no_taboo")
        $ JubesX.daily_history.append("no_taboo")
        ch_v "I don't wanna make a scene."
    elif JubesX.action_counter["finger_ass"]:
        $ JubesX.change_face("sad")
        ch_v "I'm not into it."
    else:
        $ JubesX.change_face("surprised")
        ch_v "Not today, [JubesX.player_petname]."
        $ JubesX.change_face()
    $ JubesX.recent_history.append("no_insert ass")
    $ JubesX.daily_history.append("no_insert ass")
    $ approval_bonus = 0
    return


label Jubes_IA_Prep:
    if offhand_action == "finger_ass":
        return

    call Jubes_Pussy_Launch ("finger_ass")

    if action_context == JubesX:

        $ action_context = 0
        if (JubesX.legs and not JubesX.Upskirt) or (JubesX.underwear and not JubesX.underwearDown):

            if ApprovalCheck(JubesX, 1250, TabM = 1) or (JubesX.SeenPussy and ApprovalCheck(JubesX, 500) and not Taboo):
                $ JubesX.Upskirt = 1
                $ JubesX.underwearDown = 1
                $ Line = 0
                if JubesX.PantsNum() == 5:
                    $ Line = JubesX.name + " hikes up her_skirt"
                elif JubesX.PantsNum() >= 6:
                    $ Line = JubesX.name + " pulls down her " + JubesX.legs
                else:
                    $ Line = 0
                if JubesX.underwear:
                    if Line:

                        "[Line] and pulls her [JubesX.underwear] out of the way."
                        "She then grabs your arm and rubs your hand against her asshole, clearly intending you to get to work."
                    else:

                        "She pulls her [JubesX.underwear] out of the way, and then rubs your hand against her asshole."
                        "She clearly intends for you to get to work."
                else:

                    "[Line], and then rubs your hand against her asshole."
                    "She clearly intends for you to get to work."
                call Jubes_First_Bottomless (1)
            else:
                "[JubesX.name] grabs your arm and rubs your hand against her asshole, clearly intending you to get to work."
        else:
            "[JubesX.name] grabs your arm and rubs your hand against her asshole, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ JubesX.change_stat("inhibition", 80, 3)
                $ JubesX.change_stat("inhibition", 50, 2)
                "You press your finger into it."
            "Praise her.":
                $ JubesX.change_face("sexy", 1)
                $ JubesX.change_stat("inhibition", 80, 3)
                ch_p "Dirty girl, [JubesX.petname]."
                $ JubesX.nameCheck()
                "You press your finger into it."
                $ JubesX.change_stat("love", 85, 1)
                $ JubesX.change_stat("obedience", 90, 1)
                $ JubesX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your hand back."
                $ JubesX.change_face("surprised")
                $ JubesX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [JubesX.petname]."
                $ JubesX.nameCheck()
                "[JubesX.name] pulls back."
                $ JubesX.change_stat("obedience", 90, 1)
                $ JubesX.change_stat("obedience", 50, 1)
                $ JubesX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ JubesX.AddWord(1,"refused","refused")
                return


    if not JubesX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (JubesX)
        if "angry" in JubesX.recent_history:
            return

    $ approval_bonus = 0
    if not JubesX.action_counter["finger_ass"]:
        if JubesX.Forced:
            $ JubesX.change_stat("love", 90, -50)
            $ JubesX.change_stat("obedience", 70, 60)
            $ JubesX.change_stat("inhibition", 80, 35)
        else:
            $ JubesX.change_stat("love", 90, 10)
            $ JubesX.change_stat("obedience", 70, 20)
            $ JubesX.change_stat("inhibition", 80, 25)

    if Taboo:
        $ JubesX.inhibition += int(Taboo/10)
        $ JubesX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ JubesX.DrainWord("no_taboo")
    $ JubesX.DrainWord("no_insert ass")
    $ JubesX.recent_history.append("finger_ass")
    $ JubesX.daily_history.append("finger_ass")
    call Jubes_Pussy_Launch ("finger_ass")

label Jubes_IA_Cycle:
    while Round > 0:
        call ViewShift (JubesX, JubesX.pose, 0, "finger_ass")
        call shift_focus (JubesX)
        $ JubesX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (JubesX)
                    $ counter += 1
                    $ Round -= 1
                    jump Jubes_IA_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (JubesX, "menu")
                    jump Jubes_IA_Cycle
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
                                    "Pull out and start rubbing again.":
                                        $ action_context = "pullback"
                                        call Jubes_IA_After
                                        call Jubes_Fondle_Ass
                                    "I want to lick your asshole.":
                                        $ action_context = "shift"
                                        call Jubes_IA_After
                                        call Jubes_Lick_Ass
                                    "Just start licking.":
                                        $ action_context = "auto"
                                        call Jubes_IA_After
                                        call Jubes_Lick_Ass
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Jubes_IA_After
                                        call Jubes_Dildo_Ass
                                    "Never Mind":
                                        jump Jubes_IA_Cycle
                            else:
                                call Sex_Basic_Dialog (JubesX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Jubes_IA_After
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
                                    jump Jubes_IA_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jubes_IA_Cycle
                                "Never mind":
                                    jump Jubes_IA_Cycle

                        "Show her feet" if not ShowFeet and (JubesX.pose == "doggy" or JubesX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (JubesX.pose == "doggy" or JubesX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [JubesX.name]":

                            call Girl_Undress (JubesX)
                        "Clean up [JubesX.name] (locked)" if not JubesX.Spunk:
                            pass
                        "Clean up [JubesX.name]" if JubesX.Spunk:
                            call Girl_Cleanup (JubesX, "ask")
                        "Never mind":
                            jump Jubes_IA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jubes_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jubes_IA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jubes_Pos_Reset
                    $ Line = 0
                    jump Jubes_IA_After


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
                if "angry" in JubesX.recent_history:
                    call Jubes_Pos_Reset
                    return
                $ JubesX.change_stat("lust", 200, 5)
                if 100 > JubesX.lust >= 70 and JubesX.session_orgasms < 2:
                    $ JubesX.recent_history.append("unsatisfied")
                    $ JubesX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jubes_IA_After
                $ Line = "came"

            if JubesX.lust >= 100:

                call Girl_Cumming (JubesX)
                if action_context == "shift" or "angry" in JubesX.recent_history:
                    jump Jubes_IA_After

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
                            jump Jubes_IA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if JubesX.SEXP >= 100 or ApprovalCheck(JubesX, 1200, "LO"):
            pass
        elif counter == (5 + JubesX.action_counter["finger_ass"]):
            $ JubesX.brows = "confused"
            ch_v "Having fun?"
        elif JubesX.lust >= 80:
            pass
        elif counter == (15 + JubesX.action_counter["finger_ass"]) and JubesX.SEXP >= 15 and not ApprovalCheck(JubesX, 1500):
            $ JubesX.brows = "confused"
            menu:
                ch_v "Could we maybe try. . . something else?"
                "Finish up.":
                    "You let go. . ."
                    jump Jubes_IA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Jubes_IA_After
                "No, this is fun.":
                    if ApprovalCheck(JubesX, 1200) or ApprovalCheck(JubesX, 500, "O"):
                        $ JubesX.change_stat("love", 200, -5)
                        $ JubesX.change_stat("obedience", 50, 3)
                        $ JubesX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ JubesX.change_face("angry", 1)
                        call Jubes_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_v "This is kinda boring. . ."
                        $ JubesX.change_stat("love", 50, -3, 1)
                        $ JubesX.change_stat("love", 80, -4, 1)
                        $ JubesX.change_stat("obedience", 30, -1, 1)
                        $ JubesX.change_stat("obedience", 50, -1, 1)
                        $ JubesX.recent_history.append("angry")
                        $ JubesX.daily_history.append("angry")
                        jump Jubes_IA_After


        call Escalation (JubesX)

        if Round == 10:
            call Sex_Basic_Dialog (JubesX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JubesX, 5)


    $ JubesX.change_face("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JubesX, "done")

label Jubes_IA_After:
    if not action_context:
        call Jubes_Pos_Reset

    $ JubesX.change_face("sexy")

    $ JubesX.action_counter["finger_ass"] += 1
    $ JubesX.remaining_actions -=1
    $ JubesX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ JubesX.addiction_rate += 1

    call Partner_Like (JubesX, 2)

    if JubesX.action_counter["finger_ass"] == 1:
        $ JubesX.SEXP += 12
        if not action_context:
            if JubesX.love >= 500 and "unsatisfied" not in JubesX.recent_history:
                ch_v "That was kinda weird. . ."
            elif JubesX.obedience <= 500 and Player.focus <= 20:
                $ JubesX.change_face("perplexed", 1)
                ch_v "Did you like that?"

    $ approval_bonus = 0


    call Checkout
    return








label Jubes_Lick_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JubesX)

    if JubesX.action_counter["eat_ass"]:
        $ approval_bonus += 20
    if JubesX.PantsNum() >= 6 or JubesX.HoseNum() >= 5:
        $ approval_bonus -= 25
    if JubesX.lust > 95:
        $ approval_bonus += 20
    elif JubesX.lust > 85:
        $ approval_bonus += 15
    if JubesX.lust > 85 and action_context == "auto":
        $ approval_bonus += 10
    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in JubesX.Traits:
        $ approval_bonus += (4*Taboo)
    if JubesX in Player.Harem or "sex friend" in JubesX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JubesX.Traits:
        $ approval_bonus -= 25
    if JubesX.event_counter["forced"] and not JubesX.Forced:
        $ approval_bonus -= 5*JubesX.event_counter["forced"]

    if Taboo and "no_taboo" in JubesX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in JubesX.history:
        $ approval_bonus -= 20

    if "no_lick ass" in JubesX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_lick ass" in JubesX.recent_history else 0

    $ Approval = ApprovalCheck(JubesX, 1550, TabM = 4)

    if action_context == "auto":
        if Approval:
            $ JubesX.change_face("surprised")
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_stat("inhibition", 80, 3)
            $ JubesX.change_stat("inhibition", 40, 2)
            "As you crouch down and start to lick her asshole, [JubesX.name] startles briefly, but then begins to melt."
            $ JubesX.change_face("sexy")
            jump Jubes_LA_Prep
        else:
            $ JubesX.change_face("surprised")
            $ JubesX.change_stat("love", 80, -2)
            $ JubesX.change_stat("obedience", 50, -3)
            ch_v "[JubesX.player_petname]! No. . ."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "eat_ass" in JubesX.recent_history:
        $ JubesX.change_face("sexy", 1)
        ch_v "Mmmm, again? I guess. . ."
        jump Jubes_LA_Prep
    elif "eat_ass" in JubesX.daily_history:
        $ JubesX.change_face("sexy", 1)
        ch_v "You didn't get enough earlier?"


    if Approval >= 2:
        if JubesX.Forced:
            $ JubesX.change_face("sad")
            $ JubesX.change_stat("love", 70, -3, 1)
            $ JubesX.change_stat("love", 20, -2, 1)
            $ JubesX.change_stat("obedience", 90, 2)
            $ JubesX.change_stat("inhibition", 60, 2)
            ch_v "Meh. . ."
        else:
            $ JubesX.change_face("sexy", 1)
            $ JubesX.eyes = "closed"
            $ JubesX.change_stat("love", 90, 1)
            $ JubesX.change_stat("inhibition", 60, 2)
            $ JubesX.change_stat("lust", 200, 3)
            ch_v "Mmm. . . naughty."
        $ JubesX.change_stat("obedience", 20, 1)
        $ JubesX.change_stat("obedience", 60, 1)
        $ JubesX.change_stat("inhibition", 80, 2)
        jump Jubes_LA_Prep
    else:

        $ JubesX.change_face("angry", 1)
        if "no_lick ass" in JubesX.recent_history:
            ch_v "I already told you, \"no\"."
        elif Taboo and "no_taboo" in JubesX.daily_history and "no_lick ass" in JubesX.daily_history:
            ch_v "I told you not to touch me like that in public!"
        elif "no_lick ass" in JubesX.daily_history:
            ch_v "Don't make me tell you again today."
        elif Taboo and "no_taboo" in JubesX.daily_history:
            ch_v "I told you, not here, [JubesX.player_petname]."
        elif not JubesX.action_counter["eat_ass"]:
            $ JubesX.change_face("bemused", 1)
            if JubesX.love >= JubesX.obedience and JubesX.love >= JubesX.inhibition:
                ch_v "What? What're you talking about?"
            elif JubesX.obedience >= JubesX.inhibition:
                ch_v "Is that what gets you off?"
            else:
                $ JubesX.eyes = "sexy"
                ch_v "Hm, I hadn't thought. . ."
        else:
            $ JubesX.change_face("bemused")
            ch_v "Not now, [JubesX.player_petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no_lick ass" in JubesX.daily_history:
                $ JubesX.change_face("bemused")
                ch_v "Yeah, whatever."
                return
            "I'm sure I can convince you later. . ." if "no_lick ass" not in JubesX.daily_history:
                $ JubesX.change_face("sexy")
                ch_v "Anything's possible, [JubesX.player_petname]."
                $ JubesX.change_stat("love", 80, 2)
                $ JubesX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ JubesX.recent_history.append("no_taboo")
                    $ JubesX.daily_history.append("no_taboo")
                $ JubesX.recent_history.append("no_lick ass")
                $ JubesX.daily_history.append("no_lick ass")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ JubesX.change_face("sexy")
                    $ JubesX.change_stat("obedience", 90, 2)
                    $ JubesX.change_stat("obedience", 50, 2)
                    ch_v "Um. . . maybe? . ."
                    $ JubesX.change_stat("inhibition", 70, 3)
                    $ JubesX.change_stat("inhibition", 40, 2)
                    jump Jubes_LA_Prep
                else:
                    $ JubesX.change_face("sexy")
                    ch_v "Doubt."
            "[[Start licking anyway]":

                $ Approval = ApprovalCheck(JubesX, 1100, "OI", TabM = 4)
                if Approval > 1 or (Approval and JubesX.Forced):
                    $ JubesX.change_face("sad")
                    $ JubesX.change_stat("love", 70, -5, 1)
                    $ JubesX.change_stat("love", 200, -2)
                    ch_v "Suit yourself."
                    $ JubesX.change_stat("obedience", 50, 4)
                    $ JubesX.change_stat("inhibition", 80, 1)
                    $ JubesX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ JubesX.Forced = 1
                    jump Jubes_LA_Prep
                else:
                    $ JubesX.change_stat("love", 200, -15)
                    $ JubesX.change_face("angry", 1)
                    "She shoves your head back."
                    $ JubesX.recent_history.append("angry")
                    $ JubesX.daily_history.append("angry")

    if "no_lick ass" in JubesX.daily_history:
        ch_v "I'm pretty clear on this, NO."
        $ JubesX.recent_history.append("angry")
        $ JubesX.daily_history.append("angry")
    elif JubesX.Forced:
        $ JubesX.change_face("angry", 1)
        ch_v "I don't think so."
        if ApprovalCheck(JubesX, 500, "I"):
            $ JubesX.change_stat("lust", 80, 10)
        else:
            $ JubesX.change_stat("lust", 50, 3)
        $ JubesX.change_stat("obedience", 50, -2)
        $ JubesX.recent_history.append("angry")
        $ JubesX.daily_history.append("angry")
    elif Taboo:
        $ JubesX.change_face("angry", 1)
        $ JubesX.recent_history.append("no_taboo")
        $ JubesX.daily_history.append("no_taboo")
        ch_v "I don't wanna make a scene."
    elif JubesX.action_counter["eat_ass"]:
        $ JubesX.change_face("sad")
        ch_v "Sorry, no more of that."
    else:
        $ JubesX.change_face("surprised")
        ch_v "I'm sorry, not now."
        $ JubesX.change_face()
    $ JubesX.recent_history.append("no_lick ass")
    $ JubesX.daily_history.append("no_lick ass")
    $ approval_bonus = 0
    return

label Jubes_LA_Prep:
    if offhand_action == "eat_ass":
        return
    if not JubesX.Forced and action_context != "auto":
        $ approval_bonus = 0
        if JubesX.PantsNum() >= 6:
            $ approval_bonus = 15
        call Bottoms_Off (JubesX)
        if "angry" in JubesX.recent_history:
            return
    $ approval_bonus = 0
    call Jubes_Pussy_Launch ("eat_ass")
    if not JubesX.action_counter["eat_ass"]:
        if JubesX.Forced:
            $ JubesX.change_stat("love", 90, -30)
            $ JubesX.change_stat("obedience", 70, 40)
            $ JubesX.change_stat("inhibition", 80, 80)
        else:
            $ JubesX.change_stat("love", 90, 35)
            $ JubesX.change_stat("obedience", 70, 25)
            $ JubesX.change_stat("inhibition", 80, 55)
    if Taboo:
        $ JubesX.inhibition += int(Taboo/10)
        $ JubesX.lust += int(Taboo/5)
    if action_context:
        $ renpy.pop_call()
        $ action_context = 0

    $ JubesX.Upskirt = 1
    if JubesX.PantsNum() == 5:
        $ JubesX.SeenPanties = 1
    if not JubesX.underwear:
        call Jubes_First_Bottomless (1)
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ JubesX.DrainWord("no_taboo")
    $ JubesX.DrainWord("no_lick ass")

    $ JubesX.recent_history.append("lick") if "lick" not in JubesX.recent_history else JubesX.recent_history
    $ JubesX.recent_history.append("ass") if "ass" not in JubesX.recent_history else JubesX.recent_history
    $ JubesX.recent_history.append("eat_ass")

    $ JubesX.daily_history.append("lick") if "lick" not in JubesX.daily_history else JubesX.recent_history
    $ JubesX.daily_history.append("ass") if "ass" not in JubesX.daily_history else JubesX.recent_history
    $ JubesX.daily_history.append("eat_ass")
    call Jubes_Pussy_Launch ("eat_ass")
label Jubes_LA_Cycle:
    if offhand_action == "kiss":
        $ offhand_action = 0
    while Round > 0:
        call ViewShift (JubesX, JubesX.pose, 0, "eat_ass")
        call shift_focus (JubesX)
        $ JubesX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (JubesX)
                    $ counter += 1
                    $ Round -= 1
                    jump Jubes_LA_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (JubesX, "menu")
                    jump Jubes_LA_Cycle
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
                                    "Switch to fondling.":
                                        $ action_context = "pullback"
                                        call Jubes_LA_After
                                        call Jubes_Fondle_Ass
                                    "I want to stick a finger in.":
                                        $ action_context = "shift"
                                        call Jubes_LA_After
                                        call Jubes_Insert_Ass
                                    "Just stick a finger in [[without asking].":
                                        $ action_context = "auto"
                                        call Jubes_LA_After
                                        call Jubes_Insert_Ass
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Jubes_LA_After
                                        call Jubes_Dildo_Ass
                                    "Never Mind":
                                        jump Jubes_LA_Cycle
                            else:
                                call Sex_Basic_Dialog (JubesX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Jubes_LA_After
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
                                    jump Jubes_LA_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jubes_LA_Cycle
                                "Never mind":
                                    jump Jubes_LA_Cycle

                        "Show her feet" if not ShowFeet and (JubesX.pose == "doggy" or JubesX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (JubesX.pose == "doggy" or JubesX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [JubesX.name]":

                            call Girl_Undress (JubesX)
                        "Clean up [JubesX.name] (locked)" if not JubesX.Spunk:
                            pass
                        "Clean up [JubesX.name]" if JubesX.Spunk:
                            call Girl_Cleanup (JubesX, "ask")
                        "Never mind":
                            jump Jubes_LA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jubes_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jubes_LA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jubes_Pos_Reset
                    $ Line = 0
                    jump Jubes_LA_After


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
                if "angry" in JubesX.recent_history:
                    call Jubes_Pos_Reset
                    return
                $ JubesX.change_stat("lust", 200, 5)
                if 100 > JubesX.lust >= 70 and JubesX.session_orgasms < 2:
                    $ JubesX.recent_history.append("unsatisfied")
                    $ JubesX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jubes_LA_After
                $ Line = "came"

            if JubesX.lust >= 100:

                call Girl_Cumming (JubesX)
                if action_context == "shift" or "angry" in JubesX.recent_history:
                    jump Jubes_LA_After

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
                            jump Jubes_LA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if JubesX.SEXP >= 100 or ApprovalCheck(JubesX, 1200, "LO"):
            pass
        elif counter == (5 + JubesX.action_counter["eat_ass"]):
            $ JubesX.brows = "confused"
            ch_v "Having fun?"
        elif JubesX.lust >= 80:
            pass
        elif counter == (15 + JubesX.action_counter["eat_ass"]) and JubesX.SEXP >= 15 and not ApprovalCheck(JubesX, 1500):
            $ JubesX.brows = "confused"
            menu:
                ch_v "Could we maybe try. . . something else?"
                "Finish up.":
                    "You let go. . ."
                    jump Jubes_LA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Jubes_LA_After
                "No, this is fun.":
                    if ApprovalCheck(JubesX, 1200) or ApprovalCheck(JubesX, 500, "O"):
                        $ JubesX.change_stat("love", 200, -5)
                        $ JubesX.change_stat("obedience", 50, 3)
                        $ JubesX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ JubesX.change_face("angry", 1)
                        call Jubes_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_v "This is kinda boring. . ."
                        $ JubesX.change_stat("love", 50, -3, 1)
                        $ JubesX.change_stat("love", 80, -4, 1)
                        $ JubesX.change_stat("obedience", 30, -1, 1)
                        $ JubesX.change_stat("obedience", 50, -1, 1)
                        $ JubesX.recent_history.append("angry")
                        $ JubesX.daily_history.append("angry")
                        jump Jubes_LA_After


        call Escalation (JubesX)

        if Round == 10:
            call Sex_Basic_Dialog (JubesX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JubesX, 5)


    $ JubesX.change_face("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JubesX, "done")

label Jubes_LA_After:
    if not action_context:
        call Jubes_Pos_Reset

    $ JubesX.change_face("sexy")

    $ JubesX.action_counter["eat_ass"] += 1
    $ JubesX.remaining_actions -=1
    if JubesX.PantsNum() < 6 or JubesX.Upskirt:
        $ JubesX.addiction_rate += 1
        if "addictive" in Player.Traits:
            $ JubesX.addiction_rate += 1

    call Partner_Like (JubesX, 2)

    if JubesX.action_counter["eat_ass"] == 1:
        $ JubesX.SEXP += 15
        if not action_context:
            if JubesX.love >= 500 and "unsatisfied" not in JubesX.recent_history:
                ch_v "That was. . . interesting."
            elif JubesX.obedience <= 500 and Player.focus <= 20:
                $ JubesX.change_face("perplexed", 1)
                ch_v "Was that good for you?"

    $ approval_bonus = 0


    call Checkout
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
