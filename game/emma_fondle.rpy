
label Emma_Fondle:

    $ EmmaX.mouth = "smile"
    if not EmmaX.remaining_actions:
        ch_e "I'm rather tired right now, [EmmaX.player_petname], raincheck?"
        return
    menu:
        ch_e "Well? Where did you want to touch, [EmmaX.player_petname]?"
        "Your breasts?" if EmmaX.remaining_actions:
            jump Emma_Fondle_Breasts
        "Your thighs?" if EmmaX.remaining_actions:
            jump Emma_Fondle_Thighs
        "Your pussy?" if EmmaX.remaining_actions:
            jump Emma_Fondle_Pussy
        "Your Ass?" if EmmaX.remaining_actions:
            jump Emma_Fondle_Ass
        "Never mind.":
            return
    return



label Emma_Fondle_Breasts:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (EmmaX)


    if EmmaX.action_counter["fondle_breasts"]:
        $ approval_bonus += 15
    if EmmaX.lust > 75:
        $ approval_bonus += 20
    if "exhibitionist" in EmmaX.Traits:
        $ approval_bonus += (3*Taboo)
    if EmmaX in Player.Harem or "sex friend" in EmmaX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in EmmaX.Traits:
        $ approval_bonus -= 20
    if EmmaX.event_counter["forced"] and not EmmaX.Forced:
        $ approval_bonus -= 5*EmmaX.event_counter["forced"]

    if Taboo and "no_taboo" in EmmaX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in EmmaX.history:
        $ approval_bonus -= 20

    if "no_fondle breasts" in EmmaX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle breasts" in EmmaX.recent_history else 0

    $ Approval = ApprovalCheck(EmmaX, 950, TabM = 3)

    if action_context == "auto":
        if Approval:
            $ EmmaX.change_face("sexy")
            $ EmmaX.change_stat("obedience", 90, 1)
            $ EmmaX.change_stat("obedience", 70, 2)
            $ EmmaX.change_stat("inhibition", 70, 3)
            $ EmmaX.change_stat("inhibition", 30, 2)
            "As you cup her breast, [EmmaX.name] gently nods."
            jump Emma_FB_Prep
        else:
            $ EmmaX.change_face("surprised")
            $ EmmaX.brows = "confused"
            $ EmmaX.change_stat("obedience", 50, -2)
            ch_e "Down boy, you were doing so well. . ."
            $ approval_bonus = 0
            $ offhand_action = 0
            return



    if Approval:
        $ EmmaX.change_face("sexy", 1)
        if EmmaX.Forced:
            $ EmmaX.change_face("sad")
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
        elif not Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "This does seem less. . . exposed."

    if "fondle_breasts" in EmmaX.recent_history:
        $ EmmaX.change_face("sexy", 1)
        ch_e "Mmmm, again? I suppose. . ."
        jump Emma_FB_Prep
    elif "fondle_breasts" in EmmaX.daily_history:
        $ EmmaX.change_face("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax, gently. . .",
            "Mmm. . ."])
        ch_e "[Line]"

    if Approval >= 2:
        $ EmmaX.change_face("bemused", 1)
        if EmmaX.Forced:
            $ EmmaX.change_face("sad")
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
            $ EmmaX.change_stat("obedience", 90, 1)
            $ EmmaX.change_stat("inhibition", 60, 1)
        ch_e "That sounds lovely, ravish me."
        $ EmmaX.change_stat("love", 90, 1)
        $ EmmaX.change_stat("inhibition", 50, 3)
        jump Emma_FB_Prep
    else:

        $ EmmaX.change_face("angry", 1)
        if "no_fondle breasts" in EmmaX.recent_history:
            ch_e "Your persistance is doing you no favors, [EmmaX.player_petname]."
        elif Taboo and "no_taboo" in EmmaX.daily_history and "no_fondle breasts" in EmmaX.daily_history:
            ch_e "You've been warned."
        elif "no_fondle breasts" in EmmaX.daily_history:
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "As I said, not here, [EmmaX.player_petname]."
        elif not EmmaX.action_counter["fondle_breasts"]:
            $ EmmaX.change_face("bemused")
            ch_e "I highly doubt you could handle them, [EmmaX.player_petname]. . ."
        else:
            $ EmmaX.change_face("bemused")
            ch_e "You wish."
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle breasts" in EmmaX.daily_history:
                $ EmmaX.change_face("bemused")
                ch_e "Don't concern yourself, [EmmaX.player_petname]."
                return
            "Maybe later?" if "no_fondle breasts" not in EmmaX.daily_history:
                $ EmmaX.change_face("sexy")
                "She re-adjusts her cleavage."
                ch_e "Well, I can't rule it out. . ."
                $ EmmaX.change_stat("love", 80, 1)
                $ EmmaX.change_stat("love", 50, 1)
                $ EmmaX.change_stat("inhibition", 30, 2)
                if Taboo:
                    $ EmmaX.recent_history.append("no_taboo")
                    $ EmmaX.daily_history.append("no_taboo")
                $ EmmaX.recent_history.append("no_fondle breasts")
                $ EmmaX.daily_history.append("no_fondle breasts")
                return
            "Come on, Please?":
                if Approval:
                    $ EmmaX.change_face("sexy")
                    $ EmmaX.change_stat("obedience", 90, 1)
                    $ EmmaX.change_stat("obedience", 50, 2)
                    $ EmmaX.change_stat("inhibition", 60, 3)
                    $ EmmaX.change_stat("inhibition", 30, 2)
                    ch_e "Politeness can be rewarded. . ."
                    jump Emma_FB_Prep
                else:
                    $ EmmaX.change_face("sexy")
                    ch_e "This wasn't a \"tone\" issue."
            "[[Grab her chest anyway]":


                $ Approval = ApprovalCheck(EmmaX, 350, "OI", TabM = 3)
                if Approval > 1 or (Approval and EmmaX.Forced):
                    $ EmmaX.change_face("sad")
                    $ EmmaX.change_stat("love", 70, -5, 1)
                    $ EmmaX.change_stat("love", 20, -2, 1)
                    ch_e "That is not appropriate. . ."
                    ch_e "but neither is it entirely unwelcome. . ."
                    $ EmmaX.change_stat("obedience", 90, 2)
                    $ EmmaX.change_stat("obedience", 50, 4)
                    $ EmmaX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ EmmaX.Forced = 1
                    jump Emma_FB_Prep
                else:
                    $ EmmaX.change_stat("love", 200, -10)
                    $ EmmaX.change_face("angry", 1)
                    "She slaps your hand away."
                    $ EmmaX.recent_history.append("angry")
                    $ EmmaX.daily_history.append("angry")

    if "no_fondle breasts" in EmmaX.daily_history:
        ch_e "You need to pay attention when I speak to you."
        $ EmmaX.recent_history.append("angry")
        $ EmmaX.daily_history.append("angry")
    elif EmmaX.Forced:
        $ EmmaX.change_face("angry", 1)
        ch_e "Don't push your luck."
        $ EmmaX.change_stat("lust", 60, 5)
        $ EmmaX.change_stat("obedience", 50, -2)
        $ EmmaX.recent_history.append("angry")
        $ EmmaX.daily_history.append("angry")
    elif Taboo:
        $ EmmaX.change_face("angry", 1)
        $ EmmaX.recent_history.append("no_taboo")
        $ EmmaX.daily_history.append("no_taboo")
        ch_e "I can't been seen doing that with you."
    elif EmmaX.action_counter["fondle_breasts"]:
        $ EmmaX.change_face("sad")
        ch_e "I'm afraid you haven't earned back my good graces."
    else:
        $ EmmaX.change_face("sexy")
        $ EmmaX.mouth = "sad"
        ch_e "No."
    $ EmmaX.recent_history.append("no_fondle breasts")
    $ EmmaX.daily_history.append("no_fondle breasts")
    $ approval_bonus = 0
    return


label Emma_FB_Prep:
    if primary_action == "kiss":
        $ primary_action = "fondle_breasts"
        return

    if offhand_action == "fondle_breasts":
        return

    if EmmaX.pose in ("doggy","sex"):
        call ViewShift (EmmaX, EmmaX.pose, 0, "fondle_breasts")
    else:
        call ViewShift (EmmaX, "breasts", 0, "fondle_breasts")

    if action_context == EmmaX:

        $ action_context = 0
        if (EmmaX.top or EmmaX.bra) and not EmmaX.Uptop:

            if ApprovalCheck(EmmaX, 1250, TabM = 1) or (EmmaX.SeenChest and ApprovalCheck(EmmaX, 500) and not Taboo):
                $ EmmaX.Uptop = 1
                $ Line = EmmaX.top if EmmaX.top else EmmaX.bra
                "With a devilish grin, [EmmaX.name] pulls her [Line] up over her breasts."
                call Emma_First_Topless (1)
                $ Line = 0
                "She then grabs your arm and mashes your hand against her breast, clearly intending you to get to work."
            else:
                "[EmmaX.name] grabs your arm and mashes your hand against her covered breast, clearly intending you to get to work."
        else:
            "[EmmaX.name] grabs your arm and mashes your hand against her breast, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ EmmaX.change_stat("inhibition", 80, 3)
                $ EmmaX.change_stat("inhibition", 50, 2)
                "You start to fondle it."
            "Praise her.":
                $ EmmaX.change_face("sexy", 1)
                $ EmmaX.change_stat("inhibition", 80, 3)
                ch_p "I like the initiative, [EmmaX.petname]."
                $ EmmaX.nameCheck()
                "You start to fondle it."
                $ EmmaX.change_stat("love", 85, 1)
                $ EmmaX.change_stat("obedience", 90, 1)
                $ EmmaX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your hand back."
                $ EmmaX.change_face("surprised")
                $ EmmaX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [EmmaX.petname]."
                $ EmmaX.nameCheck()
                "[EmmaX.name] pulls back."
                $ EmmaX.change_stat("obedience", 90, 1)
                $ EmmaX.change_stat("obedience", 50, 1)
                $ EmmaX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ EmmaX.AddWord(1,"refused","refused")
                return


    if not EmmaX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Top_Off (EmmaX)
        if "angry" in EmmaX.recent_history:
            return
    $ approval_bonus = 0
    if not EmmaX.action_counter["fondle_breasts"]:
        if EmmaX.Forced:
            $ EmmaX.change_stat("love", 90, -20)
            $ EmmaX.change_stat("obedience", 70, 25)
            $ EmmaX.change_stat("inhibition", 80, 15)
        else:
            $ EmmaX.change_stat("love", 90, 10)
            $ EmmaX.change_stat("obedience", 70, 5)
            $ EmmaX.change_stat("inhibition", 80, 15)

    if Taboo:
        $ EmmaX.inhibition += int(Taboo/10)
        $ EmmaX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ EmmaX.DrainWord("no_taboo")
    $ EmmaX.DrainWord("no_fondle breasts")
    $ EmmaX.recent_history.append("fondle_breasts")
    $ EmmaX.daily_history.append("fondle_breasts")
    if EmmaX.pose in ("doggy","sex"):
        call ViewShift (EmmaX, EmmaX.pose, 0, "fondle_breasts")
    else:
        call ViewShift (EmmaX, "breasts", 0, "fondle_breasts")

label Emma_FB_Cycle:
    while Round > 0:
        call ViewShift (EmmaX, EmmaX.pose, 0, "fondle_breasts")
        call shift_focus (EmmaX)
        $ EmmaX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (EmmaX)
                    $ counter += 1
                    $ Round -= 1
                    jump Emma_FB_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (EmmaX, "menu")
                    jump Emma_FB_Cycle
                "Other options":

                    menu:
                        "Offhand action":
                            if EmmaX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ EmmaX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (EmmaX, "tired")
                        "Shift primary action":

                            if EmmaX.remaining_actions and multi_action:
                                menu:
                                    "Ask to suck on them.":
                                        if EmmaX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Emma_FB_After
                                            call Emma_Suck_Breasts
                                        else:
                                            call Sex_Basic_Dialog (EmmaX, "tired")
                                    "Just suck on them without asking.":
                                        if EmmaX.remaining_actions and multi_action:
                                            $ action_context = "auto"
                                            call Emma_FB_After
                                            call Emma_Suck_Breasts
                                        else:
                                            "As you lean in to suck on her breast, she grabs your head and pushes back."
                                            call Sex_Basic_Dialog (EmmaX, "tired")
                                    "Never Mind":
                                        jump Emma_FB_Cycle
                            else:
                                call Sex_Basic_Dialog (EmmaX, "tired")

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Asks [EmmaX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (EmmaX)
                                "Asks [EmmaX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (EmmaX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (EmmaX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Emma_FB_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Emma_FB_Cycle
                                "Never mind":
                                    jump Emma_FB_Cycle

                        "Show her feet" if not ShowFeet and (EmmaX.pose == "doggy" or EmmaX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (EmmaX.pose == "doggy" or EmmaX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [EmmaX.name]":

                            call Girl_Undress (EmmaX)
                        "Clean up [EmmaX.name] (locked)" if not EmmaX.Spunk:
                            pass
                        "Clean up [EmmaX.name]" if EmmaX.Spunk:
                            call Girl_Cleanup (EmmaX, "ask")
                        "Never mind":
                            jump Emma_FB_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Emma_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Emma_FB_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Emma_Pos_Reset
                    $ Line = 0
                    jump Emma_FB_After


        call shift_focus (EmmaX)
        call Sex_Dialog (EmmaX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or EmmaX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (EmmaX)
                if "angry" in EmmaX.recent_history:
                    call Emma_Pos_Reset
                    return
                $ EmmaX.change_stat("lust", 200, 5)
                if 100 > EmmaX.lust >= 70 and EmmaX.session_orgasms < 2 and EmmaX.SEXP >= 20:
                    $ EmmaX.recent_history.append("unsatisfied")
                    $ EmmaX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Emma_FB_After
                $ Line = "came"

            if EmmaX.lust >= 100:

                call Girl_Cumming (EmmaX)
                if action_context == "shift" or "angry" in EmmaX.recent_history:
                    jump Emma_FB_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in EmmaX.recent_history:
                    "[EmmaX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Emma_FB_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif counter == (5 + EmmaX.action_counter["fondle_breasts"]):
            $ EmmaX.brows = "confused"
            ch_e "They really are magnificent, aren't they?"
        elif EmmaX.lust >= 85:
            pass
        elif counter == (15 + EmmaX.action_counter["fondle_breasts"]) and EmmaX.SEXP >= 15 and not ApprovalCheck(EmmaX, 1500):
            $ EmmaX.brows = "confused"
            menu:
                ch_e "Perhaps we could try something else, [EmmaX.player_petname]?"
                "Finish up.":
                    "You let go. . ."
                    jump Emma_FB_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Emma_FB_After
                "No, this is fun.":
                    if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):
                        $ EmmaX.change_stat("love", 200, -5)
                        $ EmmaX.change_stat("obedience", 50, 3)
                        $ EmmaX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ EmmaX.change_face("angry", 1)
                        call Emma_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_e "You may be enjoying yourself, but I'm getting a bit sore."
                        $ EmmaX.change_stat("love", 50, -3, 1)
                        $ EmmaX.change_stat("love", 80, -4, 1)
                        $ EmmaX.change_stat("obedience", 30, -1, 1)
                        $ EmmaX.change_stat("obedience", 50, -1, 1)
                        $ EmmaX.recent_history.append("angry")
                        $ EmmaX.daily_history.append("angry")
                        jump Emma_FB_After


        call Escalation (EmmaX)

        if Round == 10:
            ch_e "It's getting late. . ."
        elif Round == 5:
            ch_e "We should take a break soon."

        if EmmaX.lust >= 50 and not EmmaX.Uptop and (EmmaX.bra or EmmaX.top):
            $ EmmaX.Uptop = 1
            "[EmmaX.name] sighs and tugs her breasts free of her clothes."
            call Emma_First_Topless


    $ EmmaX.change_face("bemused", 0)
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."

label Emma_FB_After:
    if not action_context:
        call Emma_Pos_Reset

    $ EmmaX.change_face("sexy")

    $ EmmaX.action_counter["fondle_breasts"]+= 1
    $ EmmaX.remaining_actions -=1
    $ EmmaX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ EmmaX.addiction_rate += 1

    call Partner_Like (EmmaX, 2)

    if EmmaX.action_counter["fondle_breasts"]== 1:
        $ EmmaX.SEXP += 4
        if not action_context:
            if EmmaX.love >= 500 and "unsatisfied" not in EmmaX.recent_history:
                ch_e "I'm sure it exceeded your expectations. . ."
            elif EmmaX.obedience <= 500 and Player.focus <= 20:
                $ EmmaX.change_face("perplexed", 1)
                ch_e "Well you certainly hit the jackpot."

    $ approval_bonus = 0


    call Checkout
    return






label Emma_Suck_Breasts:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (EmmaX)

    if EmmaX.action_counter["suck_breasts"]:
        $ approval_bonus += 15
    if not EmmaX.bra and not EmmaX.top:
        $ approval_bonus += 15
    if EmmaX.lust > 75:
        $ approval_bonus += 20
    if EmmaX.lust > 75 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in EmmaX.Traits:
        $ approval_bonus += (4*Taboo)
    if EmmaX in Player.Harem or "sex friend" in EmmaX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in EmmaX.Traits:
        $ approval_bonus -= 25
    if EmmaX.event_counter["forced"] and not EmmaX.Forced:
        $ approval_bonus -= 5*EmmaX.event_counter["forced"]

    if Taboo and "no_taboo" in EmmaX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in EmmaX.history:
        $ approval_bonus -= 20

    if "no_suck breasts" in EmmaX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_suck breasts" in EmmaX.recent_history else 0

    $ Approval = ApprovalCheck(EmmaX, 1050, TabM = 4)

    if action_context == "auto":
        if Approval:
            $ EmmaX.change_face("sexy")
            $ EmmaX.change_stat("obedience", 90, 1)
            $ EmmaX.change_stat("obedience", 70, 2)
            $ EmmaX.change_stat("inhibition", 70, 3)
            $ EmmaX.change_stat("inhibition", 30, 2)
            "As you dive in, [EmmaX.name] seems a bit surprised, but just makes a little \"coo.\""
            jump Emma_SB_Prep
        else:
            $ EmmaX.change_face("surprised")
            $ EmmaX.change_stat("obedience", 50, -2)
            ch_e "Down boy, you were doing so well. . ."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "suck_breasts" in EmmaX.recent_history:
        $ EmmaX.change_face("sexy", 1)
        ch_e "Mmmm, again? I suppose. . ."
        jump Emma_SB_Prep
    elif "suck_breasts" in EmmaX.daily_history:
        $ EmmaX.change_face("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax, gently. . .",
            "Mmm. . ."])
        ch_e "[Line]"

    if Approval >= 2:
        $ EmmaX.change_face("bemused", 1)
        if EmmaX.Forced:
            $ EmmaX.change_face("sad")
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
            $ EmmaX.change_stat("obedience", 90, 1)
            $ EmmaX.change_stat("inhibition", 60, 1)
        ch_e "Oh very well. . ."
        $ EmmaX.change_stat("love", 90, 1)
        $ EmmaX.change_stat("inhibition", 50, 3)
        jump Emma_SB_Prep
    else:

        $ EmmaX.change_face("angry", 1)
        if "no_suck breasts" in EmmaX.recent_history:
            ch_e "Your persistance is doing you no favors, [EmmaX.player_petname]."
        elif Taboo and "no_taboo" in EmmaX.daily_history and "no_suck breasts" in EmmaX.daily_history:
            ch_e "I told you I couldn't be seen like that."
        elif "no_suck breasts" in EmmaX.daily_history:
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "As I said, not here, [EmmaX.player_petname]."
        elif not EmmaX.action_counter["suck_breasts"]:
            $ EmmaX.change_face("bemused")
            ch_e "Let's work up to that, perhaps. . ."
        else:
            $ EmmaX.change_face("bemused")
            ch_e "You wish."
        menu:
            extend ""
            "Sorry, never mind." if "no_suck breasts" in EmmaX.daily_history:
                $ EmmaX.change_face("bemused")
                ch_e "No offense taken. I get it."
                return
            "Maybe later?" if "no_suck breasts" not in EmmaX.daily_history:
                $ EmmaX.change_face("sexy")
                ch_e "I'll give it some thought, [EmmaX.player_petname]."
                $ EmmaX.change_stat("love", 80, 1)
                $ EmmaX.change_stat("love", 50, 1)
                $ EmmaX.change_stat("inhibition", 30, 2)
                if Taboo:
                    $ EmmaX.recent_history.append("no_taboo")
                    $ EmmaX.daily_history.append("no_taboo")
                $ EmmaX.recent_history.append("no_suck breasts")
                $ EmmaX.daily_history.append("no_suck breasts")
                return
            "Come on, Please?":
                if Approval:
                    $ EmmaX.change_face("sexy")
                    $ EmmaX.change_stat("obedience", 90, 1)
                    $ EmmaX.change_stat("obedience", 50, 2)
                    $ EmmaX.change_stat("inhibition", 60, 3)
                    $ EmmaX.change_stat("inhibition", 30, 2)
                    ch_e "Oh, if you insist. . ."
                    jump Emma_SB_Prep
                else:
                    $ EmmaX.change_face("sexy")
                    ch_e "This wasn't a \"tone\" issue."
            "[[Start sucking anyway]":

                $ Approval = ApprovalCheck(EmmaX, 450, "OI", TabM = 3)
                if Approval > 1 or (Approval and EmmaX.Forced):
                    $ EmmaX.change_face("sad")
                    $ EmmaX.change_stat("love", 70, -5, 1)
                    $ EmmaX.change_stat("love", 20, -2, 1)
                    ch_e "You'd better shower them with praise. . ."
                    $ EmmaX.change_stat("obedience", 90, 2)
                    $ EmmaX.change_stat("obedience", 50, 4)
                    $ EmmaX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ EmmaX.Forced = 1
                    jump Emma_SB_Prep
                else:
                    $ EmmaX.change_stat("love", 200, -10)
                    $ EmmaX.change_face("angry", 1)
                    "She shoves your head back out."
                    $ EmmaX.recent_history.append("angry")
                    $ EmmaX.daily_history.append("angry")

    if "no_suck breasts" in EmmaX.daily_history:
        ch_e "I don't appreciate having to repeat myself, [EmmaX.player_petname]."
        $ EmmaX.recent_history.append("angry")
        $ EmmaX.daily_history.append("angry")
    elif EmmaX.Forced:
        $ EmmaX.change_face("angry", 1)
        ch_e "Not worth it."
        $ EmmaX.change_stat("lust", 60, 5)
        $ EmmaX.change_stat("obedience", 50, -2)
        $ EmmaX.recent_history.append("angry")
        $ EmmaX.daily_history.append("angry")
    elif Taboo:
        $ EmmaX.change_face("angry", 1)
        $ EmmaX.recent_history.append("no_taboo")
        $ EmmaX.daily_history.append("no_taboo")
        ch_e "I have a reputation to maintain."
    elif EmmaX.action_counter["suck_breasts"]:
        $ EmmaX.change_face("sad")
        ch_e "I am sorry about that, but perhaps later?"
    else:
        $ EmmaX.change_face("sexy")
        $ EmmaX.mouth = "sad"
        ch_e "No."
    $ EmmaX.recent_history.append("no_suck breasts")
    $ EmmaX.daily_history.append("no_suck breasts")
    $ approval_bonus = 0
    return


label Emma_SB_Prep:

    if offhand_action == "suck_breasts":
        return

    if EmmaX.pose in ("doggy","sex"):
        call ViewShift (EmmaX, EmmaX.pose, 0, "suck_breasts")
    else:
        call ViewShift (EmmaX, "breasts", 0, "suck_breasts")

    if action_context == EmmaX:

        $ action_context = 0
        if (EmmaX.top or EmmaX.bra) and not EmmaX.Uptop:

            if ApprovalCheck(EmmaX, 1250, TabM = 1) or (EmmaX.SeenChest and ApprovalCheck(EmmaX, 500) and not Taboo):
                $ EmmaX.Uptop = 1
                $ Line = EmmaX.top if EmmaX.top else EmmaX.bra
                "With a devilish grin, [EmmaX.name] pulls her [Line] up over her breasts."
                call Emma_First_Topless (1)
                $ Line = 0
                "She then grabs your head and crams your face into her chest, clearly intending you to get to work."
            else:
                "[EmmaX.name] grabs your head and crams your face into her chest, clearly intending you to get to work."
        else:
            "[EmmaX.name] grabs your head and crams your face into her chest, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ EmmaX.change_stat("inhibition", 80, 3)
                $ EmmaX.change_stat("inhibition", 50, 2)
                "You start to run your tongue along her nipple."
            "Praise her.":
                $ EmmaX.change_face("sexy", 1)
                $ EmmaX.change_stat("inhibition", 80, 3)
                ch_p "Mmm, I like this, [EmmaX.petname]."
                $ EmmaX.nameCheck()
                "You start to fondle it."
                $ EmmaX.change_stat("love", 85, 1)
                $ EmmaX.change_stat("obedience", 90, 1)
                $ EmmaX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your head back."
                $ EmmaX.change_face("surprised")
                $ EmmaX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [EmmaX.petname]."
                $ EmmaX.nameCheck()
                "[EmmaX.name] pulls away."
                $ EmmaX.change_stat("obedience", 90, 1)
                $ EmmaX.change_stat("obedience", 50, 1)
                $ EmmaX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ EmmaX.AddWord(1,"refused","refused")
                return

    if not EmmaX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Top_Off (EmmaX)
        if "angry" in EmmaX.recent_history:
            return

    $ approval_bonus = 0
    if not EmmaX.action_counter["suck_breasts"]:
        if EmmaX.Forced:
            $ EmmaX.change_stat("love", 90, -25)
            $ EmmaX.change_stat("obedience", 70, 25)
            $ EmmaX.change_stat("inhibition", 80, 17)
        else:
            $ EmmaX.change_stat("love", 90, 10)
            $ EmmaX.change_stat("obedience", 70, 10)
            $ EmmaX.change_stat("inhibition", 80, 15)

    if Taboo:
        $ EmmaX.inhibition += int(Taboo/10)
        $ EmmaX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ EmmaX.DrainWord("no_taboo")
    $ EmmaX.DrainWord("no_suck breasts")
    $ EmmaX.recent_history.append("suck_breasts")
    $ EmmaX.daily_history.append("suck_breasts")
    if EmmaX.pose in ("doggy","sex"):
        call ViewShift (EmmaX, EmmaX.pose, 0, "suck_breasts")
    else:
        call ViewShift (EmmaX, "breasts", 0, "suck_breasts")

label Emma_SB_Cycle:
    if offhand_action == "kiss":
        $ offhand_action = 0
    while Round > 0:
        call ViewShift (EmmaX, EmmaX.pose, 0, "suck_breasts")
        call shift_focus (EmmaX)
        $ EmmaX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (EmmaX)
                    $ counter += 1
                    $ Round -= 1
                    jump Emma_SB_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (EmmaX, "menu")
                    jump Emma_SB_Cycle
                "Other options":

                    menu:
                        "Offhand action":
                            if EmmaX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ EmmaX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (EmmaX, "tired")
                        "Shift primary action":

                            if EmmaX.remaining_actions and multi_action:
                                menu:
                                    "Pull back to fondling.":
                                        if EmmaX.remaining_actions and multi_action:
                                            $ action_context = "pullback"
                                            call Emma_SB_After
                                            call Emma_Fondle_Breasts
                                        else:
                                            "As you pull back, [EmmaX.name] pushes you back in close."
                                            call Sex_Basic_Dialog (EmmaX, "tired")
                                    "Never Mind":
                                        jump Emma_SB_Cycle
                            else:
                                call Sex_Basic_Dialog (EmmaX, "tired")

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Asks [EmmaX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (EmmaX)
                                "Asks [EmmaX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (EmmaX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (EmmaX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Emma_SB_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Emma_SB_Cycle
                                "Never mind":
                                    jump Emma_SB_Cycle

                        "Show her feet" if not ShowFeet and (EmmaX.pose == "doggy" or EmmaX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (EmmaX.pose == "doggy" or EmmaX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [EmmaX.name]":

                            call Girl_Undress (EmmaX)
                        "Clean up [EmmaX.name] (locked)" if not EmmaX.Spunk:
                            pass
                        "Clean up [EmmaX.name]" if EmmaX.Spunk:
                            call Girl_Cleanup (EmmaX, "ask")
                        "Never mind":
                            jump Emma_SB_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Emma_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Emma_SB_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Emma_Pos_Reset
                    $ Line = 0
                    jump Emma_SB_After


        call shift_focus (EmmaX)
        call Sex_Dialog (EmmaX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or EmmaX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (EmmaX)
                if "angry" in EmmaX.recent_history:
                    call Emma_Pos_Reset
                    return
                $ EmmaX.change_stat("lust", 200, 5)
                if 100 > EmmaX.lust >= 70 and EmmaX.session_orgasms < 2:
                    $ EmmaX.recent_history.append("unsatisfied")
                    $ EmmaX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Emma_SB_After
                $ Line = "came"

            if EmmaX.lust >= 100:

                call Girl_Cumming (EmmaX)
                if action_context == "shift" or "angry" in EmmaX.recent_history:
                    jump Emma_SB_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in EmmaX.recent_history:
                    "[EmmaX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Emma_SB_After
        if Partner:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif counter == (5 + EmmaX.action_counter["suck_breasts"]):
            $ EmmaX.brows = "sly"
            ch_e "Lovely, aren't they?"
        elif EmmaX.lust >= 85:
            pass
        elif counter == (15 + EmmaX.action_counter["suck_breasts"]) and EmmaX.SEXP >= 15 and not ApprovalCheck(EmmaX, 1500):
            $ EmmaX.brows = "confused"
            menu:
                ch_e "You certainly seem to be enjoying yourself, but perhaps we could add some variety?"
                "Finish up.":
                    "You let go. . ."
                    jump Emma_SB_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Emma_SB_After
                "No, this is fun.":
                    if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):
                        $ EmmaX.change_stat("love", 200, -5)
                        $ EmmaX.change_stat("obedience", 50, 3)
                        $ EmmaX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ EmmaX.change_face("angry", 1)
                        call Emma_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_e "You may be enjoying yourself, but I'm getting a bit sore."
                        $ EmmaX.change_stat("love", 50, -3, 1)
                        $ EmmaX.change_stat("love", 80, -4, 1)
                        $ EmmaX.change_stat("obedience", 30, -1, 1)
                        $ EmmaX.change_stat("obedience", 50, -1, 1)
                        $ EmmaX.recent_history.append("angry")
                        $ EmmaX.daily_history.append("angry")
                        jump Emma_SB_After


        if Round == 10:
            ch_e "It's getting late. . ."
        elif Round == 5:
            ch_e "We should take a break soon."

        if EmmaX.lust >= 50 and not EmmaX.Uptop and (EmmaX.bra or EmmaX.top):
            $ EmmaX.Uptop = 1
            "[EmmaX.name] sighs and tugs her breasts free of her clothes."
            call Emma_First_Topless


    $ EmmaX.change_face("bemused", 0)
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."

label Emma_SB_After:
    if not action_context:
        call Emma_Pos_Reset

    $ EmmaX.change_face("sexy")

    $ EmmaX.action_counter["suck_breasts"] += 1
    $ EmmaX.remaining_actions -=1
    $ EmmaX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ EmmaX.addiction_rate += 1

    if Partner == "Kitty":
        call Partner_Like (EmmaX, 2, 2)
    else:
        call Partner_Like (EmmaX, 2)

    if EmmaX.action_counter["suck_breasts"] == 1:
        $ EmmaX.SEXP += 4
        if not action_context:
            if EmmaX.love >= 500 and "unsatisfied" not in EmmaX.recent_history:
                ch_e "Delectable, weren't they."
            elif EmmaX.obedience <= 500 and Player.focus <= 20:
                $ EmmaX.change_face("perplexed", 1)
                ch_e "Did you get enough?"

    $ approval_bonus = 0


    call Checkout
    return





label Emma_Fondle_Thighs:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (EmmaX)

    if EmmaX.action_counter["fondle_thighs"]:
        $ approval_bonus += 10
    if EmmaX.PantsNum() > 6 or EmmaX.HoseNum() >= 5:
        $ approval_bonus -= 5
    if EmmaX.lust > 75:
        $ approval_bonus += 10
    if "exhibitionist" in EmmaX.Traits:
        $ approval_bonus += Taboo
    if EmmaX in Player.Harem or "sex friend" in EmmaX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in EmmaX.Traits:
        $ approval_bonus -= 25
    if EmmaX.event_counter["forced"] and not EmmaX.Forced:
        $ approval_bonus -= 5*EmmaX.event_counter["forced"]

    if Taboo and "no_taboo" in EmmaX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in EmmaX.history:
        $ approval_bonus -= 20

    if "no_fondle thighs" in EmmaX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle thighs" in EmmaX.recent_history else 0

    $ Approval = ApprovalCheck(EmmaX, 750, TabM=1)

    if action_context == "auto":
        if Approval:
            $ EmmaX.change_face("sexy")
            $ EmmaX.change_stat("obedience", 50, 1)
            $ EmmaX.change_stat("inhibition", 30, 2)
            "As you caress her thigh, [EmmaX.name] glances at you, and smiles."
            jump Emma_FT_Prep
        else:
            $ EmmaX.change_face("surprised")
            $ EmmaX.change_stat("obedience", 50, -2)
            ch_e "Perhaps we keep it above the waist, [EmmaX.player_petname]."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if action_context == "pullback":
        $ EmmaX.change_face("surprised")
        $ EmmaX.brows = "sad"
        if EmmaX.lust > 60:
            $ EmmaX.change_stat("love", 70, -3)
        $ EmmaX.change_stat("obedience", 90, 1)
        $ EmmaX.change_stat("obedience", 70, 2)
        "As you pull back, [EmmaX.name] looks a little sad."
        jump Emma_FT_Prep
    elif "fondle_thighs" in EmmaX.recent_history:
        $ EmmaX.change_face("sexy", 1)
        ch_e "Mmmm, again? I suppose. . ."
        jump Emma_FT_Prep
    elif "fondle_thighs" in EmmaX.daily_history:
        $ EmmaX.change_face("sexy", 1)
        ch_e "You didn't get enough earlier?"

    if Approval >= 2:
        $ EmmaX.change_face("bemused", 1)
        if EmmaX.Forced:
            $ EmmaX.change_face("sad")
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("obedience", 90, 1)
            $ EmmaX.change_stat("inhibition", 60, 1)
        ch_e "Ok [EmmaX.player_petname], go ahead."
        $ EmmaX.change_stat("love", 90, 1)
        $ EmmaX.change_stat("inhibition", 50, 3)
        jump Emma_FT_Prep
    else:

        $ EmmaX.change_face("angry", 1)
        if "no_fondle thighs" in EmmaX.recent_history:
            ch_e "Your persistance is doing you no favors, [EmmaX.player_petname]."
        elif Taboo and "no_taboo" in EmmaX.daily_history and "no_fondle thighs" in EmmaX.daily_history:
            ch_e "I told you not to touch me like that in public!"
        elif "no_fondle thighs" in EmmaX.daily_history:
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "As I said, not here, [EmmaX.player_petname]."
        elif not EmmaX.action_counter["fondle_thighs"]:
            $ EmmaX.change_face("bemused")
            ch_e "Seems a bit forward, [EmmaX.player_petname]."
        else:
            $ EmmaX.change_face("bemused")
            ch_e "You wish."
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle thighs" in EmmaX.daily_history:
                $ EmmaX.change_face("bemused")
                ch_e "I appreciate your restraint."
                return
            "Maybe later?" if "no_fondle thighs" not in EmmaX.daily_history:
                $ EmmaX.change_face("sexy")
                ch_e "Perhaps."
                $ EmmaX.change_stat("love", 80, 1)
                $ EmmaX.change_stat("inhibition", 30, 2)
                if Taboo:
                    $ EmmaX.recent_history.append("no_taboo")
                    $ EmmaX.daily_history.append("no_taboo")
                $ EmmaX.recent_history.append("no_fondle thighs")
                $ EmmaX.daily_history.append("no_fondle thighs")
                return
            "Come on, Please?":
                if Approval:
                    $ EmmaX.change_face("sexy")
                    $ EmmaX.change_stat("obedience", 60, 1)
                    $ EmmaX.change_stat("obedience", 30, 2)
                    $ EmmaX.change_stat("inhibition", 50, 1)
                    $ EmmaX.change_stat("inhibition", 30, 2)
                    ch_e "Politeness can be rewarded. . ."
                    jump Emma_FT_Prep
                else:
                    $ EmmaX.change_face("sexy")
                    ch_e "This wasn't a \"tone\" issue."
            "[[Start caressing her thigh anyway]":

                $ Approval = ApprovalCheck(EmmaX, 350, "OI", TabM = 2)
                if Approval > 1 or (Approval and EmmaX.Forced):
                    $ EmmaX.change_face("sad")
                    $ EmmaX.change_stat("love", 70, -5, 1)
                    $ EmmaX.change_stat("love", 20, -2, 1)
                    ch_e "Hmmph."
                    $ EmmaX.change_stat("obedience", 50, 3)
                    $ EmmaX.change_stat("inhibition", 60, 2)
                    if Approval < 2:
                        $ EmmaX.Forced = 1
                    jump Emma_FT_Prep
                else:
                    $ EmmaX.change_stat("love", 200, -8)
                    $ EmmaX.change_face("angry", 1)
                    "She slaps your hand away."
                    $ EmmaX.recent_history.append("angry")
                    $ EmmaX.daily_history.append("angry")

    if "no_fondle thighs" in EmmaX.daily_history:
        ch_e "I don't appreciate having to repeat myself, [EmmaX.player_petname]."
        $ EmmaX.recent_history.append("angry")
        $ EmmaX.daily_history.append("angry")
    elif EmmaX.Forced:
        $ EmmaX.change_face("angry", 1)
        ch_e "Don't push your luck."
        $ EmmaX.change_stat("lust", 50, 2)
        $ EmmaX.change_stat("obedience", 50, -1)
        $ EmmaX.recent_history.append("angry")
        $ EmmaX.daily_history.append("angry")
    elif Taboo:
        $ EmmaX.change_face("angry", 1)
        $ EmmaX.recent_history.append("no_taboo")
        $ EmmaX.daily_history.append("no_taboo")
        ch_e "I have a reputation to maintain."
    elif EmmaX.action_counter["fondle_thighs"]:
        $ EmmaX.change_face("sad")
        ch_e "Hands."
    else:
        $ EmmaX.change_face("sexy")
        $ EmmaX.mouth = "sad"
        ch_e "No."
    $ EmmaX.recent_history.append("no_fondle thighs")
    $ EmmaX.daily_history.append("no_fondle thighs")
    $ approval_bonus = 0
    return

label Emma_FT_Prep:
    if primary_action == "kiss":
        $ primary_action = "fondle_thighs"
        return

    if offhand_action == "fondle_thighs":
        return

    if not EmmaX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (EmmaX)
        if "angry" in EmmaX.recent_history:
            return

    $ approval_bonus = 0
    if EmmaX.pose in ("doggy","sex"):
        call ViewShift (EmmaX, EmmaX.pose, 0, "fondle_thighs")
    else:
        call ViewShift (EmmaX, "pussy", 0, "fondle_thighs")
    if not EmmaX.action_counter["fondle_thighs"]:
        if EmmaX.Forced:
            $ EmmaX.change_stat("love", 90, -10)
            $ EmmaX.change_stat("obedience", 70, 15)
            $ EmmaX.change_stat("inhibition", 80, 10)
        else:
            $ EmmaX.change_stat("love", 90, 5)
            $ EmmaX.change_stat("obedience", 70, 10)
            $ EmmaX.change_stat("inhibition", 80, 15)

    if Taboo:
        $ EmmaX.change_stat("lust", 200, (int(Taboo/5)))
        $ EmmaX.change_stat("inhibition", 200, (2*(int(Taboo/5))))

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ EmmaX.DrainWord("no_taboo")
    $ EmmaX.DrainWord("no_fondle thighs")
    $ EmmaX.recent_history.append("fondle_thighs")
    $ EmmaX.daily_history.append("fondle_thighs")
    if EmmaX.pose in ("doggy","sex"):
        call ViewShift (EmmaX, EmmaX.pose, 0, "fondle_thighs")
    else:
        call ViewShift (EmmaX, "pussy", 0, "fondle_thighs")

label Emma_FT_Cycle:
    while Round > 0:
        call ViewShift (EmmaX, EmmaX.pose, 0, "fondle_thighs")
        call shift_focus (EmmaX)
        $ EmmaX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (EmmaX)
                    $ counter += 1
                    $ Round -= 1
                    jump Emma_FT_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (EmmaX, "menu")
                    jump Emma_FT_Cycle
                "Other options":

                    menu:
                        "Offhand action":
                            if EmmaX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ EmmaX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (EmmaX, "tired")
                        "Shift primary action":

                            if EmmaX.remaining_actions and multi_action:
                                menu:
                                    "Can I do a little deeper?":
                                        if EmmaX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Emma_FT_After
                                            call Emma_Fondle_Pussy
                                        else:
                                            call Sex_Basic_Dialog (EmmaX, "tired")
                                    "Shift your hands a bit higher without asking":
                                        if EmmaX.remaining_actions and multi_action:
                                            $ action_context = "auto"
                                            call Emma_FT_After
                                            call Emma_Fondle_Pussy
                                        else:
                                            "As your hands creep upwards, she grabs your wrists."
                                            call Sex_Basic_Dialog (EmmaX, "tired")
                                    "Never Mind":
                                        jump Emma_FT_Cycle
                            else:
                                call Sex_Basic_Dialog (EmmaX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Emma_FT_After
                            call Offhand_Set
                        "Shift your focus (locked)" if not offhand_action:
                            pass

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Asks [EmmaX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (EmmaX)
                                "Asks [EmmaX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (EmmaX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (EmmaX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Emma_FT_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Emma_FT_Cycle
                                "Never mind":
                                    jump Emma_FT_Cycle

                        "Show her feet" if not ShowFeet and (EmmaX.pose == "doggy" or EmmaX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (EmmaX.pose == "doggy" or EmmaX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [EmmaX.name]":

                            call Girl_Undress (EmmaX)
                        "Clean up [EmmaX.name] (locked)" if not EmmaX.Spunk:
                            pass
                        "Clean up [EmmaX.name]" if EmmaX.Spunk:
                            call Girl_Cleanup (EmmaX, "ask")
                        "Never mind":
                            jump Emma_FT_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Emma_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Emma_FT_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Emma_Pos_Reset
                    $ Line = 0
                    jump Emma_FT_After


        call shift_focus (EmmaX)
        call Sex_Dialog (EmmaX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or EmmaX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (EmmaX)
                if "angry" in EmmaX.recent_history:
                    call Emma_Pos_Reset
                    return
                $ EmmaX.change_stat("lust", 200, 5)
                if 100 > EmmaX.lust >= 70 and EmmaX.session_orgasms < 2 and EmmaX.SEXP >= 20:
                    $ EmmaX.recent_history.append("unsatisfied")
                    $ EmmaX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Emma_FT_After
                $ Line = "came"

            if EmmaX.lust >= 100:

                call Girl_Cumming (EmmaX)
                if action_context == "shift" or "angry" in EmmaX.recent_history:
                    jump Emma_FT_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in EmmaX.recent_history:
                    "[EmmaX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Emma_FT_After
        if Partner:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif counter == (5 + EmmaX.action_counter["fondle_thighs"]):
            $ EmmaX.brows = "confused"
            ch_e "Luxurious, yes?"
        elif counter == (15 + EmmaX.action_counter["fondle_thighs"]) and EmmaX.SEXP >= 15 and not ApprovalCheck(EmmaX, 1500):
            $ EmmaX.brows = "confused"
            menu:
                ch_e "You certainly seem to be enjoying yourself, but perhaps we could add some variety?"
                "Finish up.":
                    "You let go. . ."
                    jump Emma_FT_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Emma_FT_After
                "No, this is fun.":
                    if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):
                        $ EmmaX.change_stat("love", 200, -5)
                        $ EmmaX.change_stat("obedience", 50, 3)
                        $ EmmaX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ EmmaX.change_face("angry", 1)
                        call Emma_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_e "Well perhaps you are enjoying yourself, but I'm tired of this."
                        $ EmmaX.change_stat("love", 50, -3, 1)
                        $ EmmaX.change_stat("love", 80, -4, 1)
                        $ EmmaX.change_stat("obedience", 30, -1, 1)
                        $ EmmaX.change_stat("obedience", 50, -1, 1)
                        $ EmmaX.recent_history.append("angry")
                        $ EmmaX.daily_history.append("angry")
                        jump Emma_FT_After


        if Round == 10:
            ch_e "It's getting late. . ."
        elif Round == 5:
            ch_e "We should take a break soon."


    $ EmmaX.change_face("bemused", 0)
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."


label Emma_FT_After:
    if not action_context:
        call Emma_Pos_Reset

    $ EmmaX.change_face("sexy")

    $ EmmaX.action_counter["fondle_thighs"]+= 1
    $ EmmaX.remaining_actions -=1
    if EmmaX.PantsNum() <= 6 or EmmaX.Upskirt:
        $ EmmaX.addiction_rate += 1
        if "addictive" in Player.Traits:
            $ EmmaX.addiction_rate += 1

    if Partner == "Kitty":
        call Partner_Like (EmmaX, 2)
    else:
        call Partner_Like (EmmaX, 1)

    if EmmaX.action_counter["fondle_thighs"]== 1:
        $ EmmaX.SEXP += 3
        if not action_context:
            if EmmaX.love >= 500 and "unsatisfied" not in EmmaX.recent_history:
                ch_e "That was. . . pleasant."
            elif EmmaX.obedience <= 500 and Player.focus <= 20:
                $ EmmaX.change_face("perplexed", 1)
                ch_e "Was that enough?"

    $ approval_bonus = 0


    call Checkout
    return


label Emma_Fondle_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (EmmaX)

    if EmmaX.action_counter["fondle_pussy"]:
        $ approval_bonus += 20
    if EmmaX.PantsNum() > 6 or EmmaX.HoseNum() >= 5:
        $ approval_bonus -= 10
    if EmmaX.lust > 75:
        $ approval_bonus += 15
    if EmmaX.lust > 75 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in EmmaX.Traits:
        $ approval_bonus += (2*Taboo)
    if EmmaX in Player.Harem or "sex friend" in EmmaX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in EmmaX.Traits:
        $ approval_bonus -= 25
    if EmmaX.event_counter["forced"] and not EmmaX.Forced:
        $ approval_bonus -= 5*EmmaX.event_counter["forced"]

    if Taboo and "no_taboo" in EmmaX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in EmmaX.history:
        $ approval_bonus -= 20

    if "no_fondle pussy" in EmmaX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle pussy" in EmmaX.recent_history else 0

    $ Approval = ApprovalCheck(EmmaX, 1050, TabM = 2)

    if action_context == "auto":
        if Approval:
            $ EmmaX.change_face("sexy")
            $ EmmaX.change_stat("obedience", 90, 1)
            $ EmmaX.change_stat("obedience", 70, 2)
            $ EmmaX.change_stat("inhibition", 70, 3)
            $ EmmaX.change_stat("inhibition", 30, 2)
            "As your hand creeps up her thigh, [EmmaX.name] seems a bit surprised, but then nods."
            jump Emma_FP_Prep
        else:
            $ EmmaX.change_face("surprised")
            $ EmmaX.change_stat("obedience", 50, -2)
            ch_e "Down boy, you were doing so well. . ."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if action_context == "pullback":
        $ EmmaX.change_face("surprised")
        $ EmmaX.brows = "sad"
        if EmmaX.lust > 80:
            $ EmmaX.change_stat("love", 70, -4)
        $ EmmaX.change_stat("obedience", 90, 1)
        $ EmmaX.change_stat("obedience", 70, 2)
        "As your hand pulls out, [EmmaX.name] gasps and looks upset."
        jump Emma_FP_Prep
    elif "fondle_pussy" in EmmaX.recent_history:
        $ EmmaX.change_face("sexy", 1)
        ch_e "Mmmm, again? I suppose. . ."
        jump Emma_FP_Prep
    elif "fondle_pussy" in EmmaX.daily_history:
        $ EmmaX.change_face("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax, gently. . .",
            "Take it a bit gently, I'm still shaking from earlier.",
            "Mmm. . ."])
        ch_e "[Line]"

    if Approval >= 2:
        $ EmmaX.change_face("bemused", 1)
        if EmmaX.Forced:
            $ EmmaX.change_face("sad")
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
            $ EmmaX.change_stat("obedience", 90, 1)
            $ EmmaX.change_stat("inhibition", 60, 1)
        ch_e "Mmmm, I couldn't refuse. . ."
        $ EmmaX.change_stat("love", 90, 1)
        $ EmmaX.change_stat("inhibition", 50, 3)
        jump Emma_FP_Prep
    else:

        $ EmmaX.change_face("angry", 1)
        if "no_fondle pussy" in EmmaX.recent_history:
            ch_e "Your persistance is doing you no favors, [EmmaX.player_petname]."
        elif Taboo and "no_taboo" in EmmaX.daily_history and "no_fondle pussy" in EmmaX.daily_history:
            ch_e "I told you not to touch me like that in public!"
        elif "no_fondle pussy" in EmmaX.daily_history:
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "As I said, not here, [EmmaX.player_petname]."
        elif not EmmaX.action_counter["fondle_pussy"]:
            $ EmmaX.change_face("bemused")
            ch_e "I don't think we're there yet, [EmmaX.player_petname]. . ."
        else:
            $ EmmaX.change_face("bemused")
            ch_e "You wish."
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle pussy" in EmmaX.daily_history:
                $ EmmaX.change_face("bemused")
                ch_e "I appreciate your restraint, [EmmaX.player_petname]."
                return
            "Maybe later?" if "no_fondle pussy" not in EmmaX.daily_history:
                $ EmmaX.change_face("sexy")
                ch_e "I'll give it some thought, [EmmaX.player_petname]."
                $ EmmaX.change_stat("love", 80, 2)
                $ EmmaX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ EmmaX.recent_history.append("no_taboo")
                    $ EmmaX.daily_history.append("no_taboo")
                $ EmmaX.recent_history.append("no_fondle pussy")
                $ EmmaX.daily_history.append("no_fondle pussy")
                return
            "Come on, Please?":
                if Approval:
                    $ EmmaX.change_face("sexy")
                    $ EmmaX.change_stat("obedience", 90, 2)
                    $ EmmaX.change_stat("obedience", 50, 2)
                    $ EmmaX.change_stat("inhibition", 70, 3)
                    $ EmmaX.change_stat("inhibition", 40, 2)
                    ch_e "I do enjoy hearing you beg. . ."
                    jump Emma_FP_Prep
                else:
                    $ EmmaX.change_face("sexy")
                    ch_e "No."
            "[[Start fondling anyway]":

                $ Approval = ApprovalCheck(EmmaX, 450, "OI", TabM = 2)
                if Approval > 1 or (Approval and EmmaX.Forced):
                    $ EmmaX.change_face("sad")
                    $ EmmaX.change_stat("love", 70, -5, 1)
                    $ EmmaX.change_stat("love", 200, -2)
                    ch_e "Oh, if you insist. . ."
                    $ EmmaX.change_stat("obedience", 50, 4)
                    $ EmmaX.change_stat("inhibition", 80, 1)
                    $ EmmaX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ EmmaX.Forced = 1
                    jump Emma_FP_Prep
                else:
                    $ EmmaX.change_stat("love", 200, -15)
                    $ EmmaX.change_face("angry", 1)
                    "She slaps your hand away."
                    $ EmmaX.recent_history.append("angry")
                    $ EmmaX.daily_history.append("angry")

    if "no_fondle pussy" in EmmaX.daily_history:
        ch_e "I don't appreciate having to repeat myself, [EmmaX.player_petname]."
        $ EmmaX.recent_history.append("angry")
        $ EmmaX.daily_history.append("angry")
    elif EmmaX.Forced:
        $ EmmaX.change_face("angry", 1)
        ch_e "I don't think so, [EmmaX.player_petname]."
        $ EmmaX.change_stat("lust", 70, 5)
        $ EmmaX.change_stat("obedience", 50, -2)
        $ EmmaX.recent_history.append("angry")
        $ EmmaX.daily_history.append("angry")
    elif Taboo:
        $ EmmaX.change_face("angry", 1)
        $ EmmaX.recent_history.append("no_taboo")
        $ EmmaX.daily_history.append("no_taboo")
        ch_e "I have a reputation to maintain."
    elif EmmaX.action_counter["fondle_pussy"]:
        $ EmmaX.change_face("sad")
        ch_e "Sorry, keep your hands out of there."
    else:
        $ EmmaX.change_face("sexy")
        $ EmmaX.mouth = "sad"
        ch_e "No thank you, [EmmaX.player_petname]."
    $ EmmaX.recent_history.append("no_fondle pussy")
    $ EmmaX.daily_history.append("no_fondle pussy")
    $ approval_bonus = 0
    return

label Emma_FP_Prep:
    if offhand_action == "fondle_pussy":
        return

    if EmmaX.pose in ("doggy","sex"):
        call ViewShift (EmmaX, EmmaX.pose, 0, "fondle_pussy")
    else:
        call ViewShift (EmmaX, "pussy", 0, "fondle_pussy")

    if action_context == EmmaX:

        $ action_context = 0
        if (EmmaX.legs and not EmmaX.Upskirt) or (EmmaX.underwear and not EmmaX.underwearDown):

            if ApprovalCheck(EmmaX, 1250, TabM = 1) or (EmmaX.SeenPussy and ApprovalCheck(EmmaX, 500) and not Taboo):
                $ EmmaX.Upskirt = 1
                $ EmmaX.underwearDown = 1
                $ Line = 0
                if EmmaX.PantsNum() == 5:
                    $ Line = EmmaX.name + " hikes up her_skirt"
                elif EmmaX.PantsNum() >= 6:
                    $ Line = EmmaX.name + " pulls down her " + EmmaX.legs
                else:
                    $ Line = 0
                if EmmaX.underwear:
                    if Line:

                        "[Line] and pulls her [EmmaX.underwear] out of the way."
                        "She then grabs your arm and then strokes your hand across her crotch, clearly intending you to get to work."
                    else:

                        "She pulls her [EmmaX.underwear] out of the way, and then strokes your hand across her crotch."
                        "She clearly intends for you to get to work."
                else:

                    "[Line], and then strokes your hand across her crotch."
                    "She clearly intends for you to get to work."
                call Emma_First_Bottomless (1)
            else:
                "[EmmaX.name] grabs your arm and strokes your hand across her crotch, clearly intending you to get to work."
        else:
            "[EmmaX.name] grabs your arm and strokes your hand across her crotch, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ EmmaX.change_stat("inhibition", 80, 3)
                $ EmmaX.change_stat("inhibition", 50, 2)
                "You start to run your fingers along her pussy."
            "Praise her.":
                $ EmmaX.change_face("sexy", 1)
                $ EmmaX.change_stat("inhibition", 80, 3)
                ch_p "I like the initiative, [EmmaX.petname]."
                $ EmmaX.nameCheck()
                "You start to run your fingers along her pussy."
                $ EmmaX.change_stat("love", 85, 1)
                $ EmmaX.change_stat("obedience", 90, 1)
                $ EmmaX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your hand back."
                $ EmmaX.change_face("surprised")
                $ EmmaX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [EmmaX.petname]."
                $ EmmaX.nameCheck()
                "[EmmaX.name] pulls back."
                $ EmmaX.change_stat("obedience", 90, 1)
                $ EmmaX.change_stat("obedience", 50, 1)
                $ EmmaX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ EmmaX.AddWord(1,"refused","refused")
                return


    if not EmmaX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (EmmaX)
        if "angry" in EmmaX.recent_history:
            return
    $ approval_bonus = 0

    if not EmmaX.action_counter["fondle_pussy"]:
        if EmmaX.Forced:
            $ EmmaX.change_stat("love", 90, -50)
            $ EmmaX.change_stat("obedience", 70, 35)
            $ EmmaX.change_stat("inhibition", 80, 25)
        else:
            $ EmmaX.change_stat("love", 90, 10)
            $ EmmaX.change_stat("obedience", 70, 10)
            $ EmmaX.change_stat("inhibition", 80, 15)
    if Taboo:
        $ EmmaX.inhibition += int(Taboo/10)
        $ EmmaX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ EmmaX.DrainWord("no_taboo")
    $ EmmaX.DrainWord("no_fondle pussy")
    $ EmmaX.recent_history.append("fondle_pussy")
    $ EmmaX.daily_history.append("fondle_pussy")
    if EmmaX.pose in ("doggy","sex"):
        call ViewShift (EmmaX, EmmaX.pose, 0, "fondle_pussy")
    else:
        call ViewShift (EmmaX, "pussy", 0, "fondle_pussy")

    $ action_speed = 1

label Emma_FP_Cycle:
    while Round > 0:
        call ViewShift (EmmaX, EmmaX.pose, 0, "fondle_pussy")
        call shift_focus (EmmaX)
        $ EmmaX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass

                "I want to stick a finger in. . ." if action_speed != 2:
                    if EmmaX.action_counter["finger_pussy"]:
                        $ action_speed = 2
                    else:
                        menu:
                            "Ask her first":
                                $ action_context = "shift"
                            "Don't ask first [[just stick it in]":
                                $ action_context = "auto"
                        call Emma_Insert_Pussy

                "Pull back a bit. . ." if action_speed == 2:
                    $ action_speed = 0
                "Slap her ass":

                    call Slap_Ass (EmmaX)
                    $ counter += 1
                    $ Round -= 1
                    jump Emma_FP_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (EmmaX, "menu")
                    jump Emma_FP_Cycle
                "Other options":

                    menu:
                        "Offhand action":
                            if EmmaX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ EmmaX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (EmmaX, "tired")
                        "Shift primary action":

                            if EmmaX.remaining_actions and multi_action:
                                menu:
                                    "I want to lick your pussy.":
                                        $ action_context = "shift"
                                        call Emma_FP_After
                                        call Emma_Lick_Pussy
                                    "Just start licking":
                                        $ action_context = "auto"
                                        call Emma_FP_After
                                        call Emma_Lick_Pussy
                                    "Pull back to the thighs":
                                        $ action_context = "pullback"
                                        call Emma_FP_After
                                        call Emma_Fondle_Thighs
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Emma_FP_After
                                        call Emma_Dildo_Pussy
                                    "Never Mind":
                                        jump Emma_FP_Cycle
                            else:
                                call Sex_Basic_Dialog (EmmaX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Emma_FP_After
                            call Offhand_Set
                        "Shift your focus (locked)" if not offhand_action:
                            pass

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Asks [EmmaX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (EmmaX)
                                "Asks [EmmaX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (EmmaX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (EmmaX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Emma_FP_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Emma_FP_Cycle
                                "Never mind":
                                    jump Emma_FP_Cycle

                        "Show her feet" if not ShowFeet and (EmmaX.pose == "doggy" or EmmaX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (EmmaX.pose == "doggy" or EmmaX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [EmmaX.name]":

                            call Girl_Undress (EmmaX)
                        "Clean up [EmmaX.name] (locked)" if not EmmaX.Spunk:
                            pass
                        "Clean up [EmmaX.name]" if EmmaX.Spunk:
                            call Girl_Cleanup (EmmaX, "ask")
                        "Never mind":
                            jump Emma_FP_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Emma_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Emma_FP_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Emma_Pos_Reset
                    $ Line = 0
                    jump Emma_FP_After


        call shift_focus (EmmaX)
        call Sex_Dialog (EmmaX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or EmmaX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (EmmaX)
                if "angry" in EmmaX.recent_history:
                    call Emma_Pos_Reset
                    return
                $ EmmaX.change_stat("lust", 200, 5)
                if 100 > EmmaX.lust >= 70 and EmmaX.session_orgasms < 2:
                    $ EmmaX.recent_history.append("unsatisfied")
                    $ EmmaX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Emma_FP_After
                $ Line = "came"

            if EmmaX.lust >= 100:

                call Girl_Cumming (EmmaX)
                if action_context == "shift" or "angry" in EmmaX.recent_history:
                    jump Emma_FP_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in EmmaX.recent_history:
                    "[EmmaX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Emma_FP_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif counter == (5 + EmmaX.action_counter["fondle_pussy"]):
            $ EmmaX.brows = "confused"
            ch_e "You like how that feels, huh?"
        elif EmmaX.lust >= 80:
            pass
        elif counter == (15 + EmmaX.action_counter["fondle_pussy"]) and EmmaX.SEXP >= 15 and not ApprovalCheck(EmmaX, 1500):
            $ EmmaX.brows = "confused"
            menu:
                ch_e "You certainly seem to be enjoying yourself, but perhaps we could add some variety?"
                "Finish up.":
                    "You let go. . ."
                    jump Emma_FP_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Emma_FP_After
                "No, this is fun.":
                    if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):
                        $ EmmaX.change_stat("love", 200, -5)
                        $ EmmaX.change_stat("obedience", 50, 3)
                        $ EmmaX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ EmmaX.change_face("angry", 1)
                        call Emma_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_e "Well perhaps you are enjoying yourself, but I'm tired of this."
                        $ EmmaX.change_stat("love", 50, -3, 1)
                        $ EmmaX.change_stat("love", 80, -4, 1)
                        $ EmmaX.change_stat("obedience", 30, -1, 1)
                        $ EmmaX.change_stat("obedience", 50, -1, 1)
                        $ EmmaX.recent_history.append("angry")
                        $ EmmaX.daily_history.append("angry")
                        jump Emma_FP_After


        if Round == 10:
            ch_e "It's getting late. . ."
        elif Round == 5:
            ch_e "We should take a break soon."


    $ EmmaX.change_face("bemused", 0)
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."


label Emma_FP_After:
    if not action_context:
        call Emma_Pos_Reset

    $ EmmaX.change_face("sexy")

    $ EmmaX.action_counter["fondle_pussy"] += 1
    $ EmmaX.remaining_actions -=1
    if EmmaX.PantsNum() <= 6 or EmmaX.Upskirt:
        $ EmmaX.addiction_rate += 1
        if "addictive" in Player.Traits:
            $ EmmaX.addiction_rate += 1

    call Partner_Like (EmmaX, 2)

    if EmmaX.action_counter["fondle_pussy"] == 1:
        $ EmmaX.SEXP += 7
        if not action_context:
            if EmmaX.love >= 500 and "unsatisfied" not in EmmaX.recent_history:
                ch_e "I do appreciate some rather. . . aggressive attention down there."
            elif EmmaX.obedience <= 500 and Player.focus <= 20:
                $ EmmaX.change_face("perplexed", 1)
                ch_e "Did you find what you were looking for?"

    $ approval_bonus = 0


    call Checkout
    return




label Emma_Insert_Pussy:
    call shift_focus (EmmaX)
    if action_context == "auto":
        if ApprovalCheck(EmmaX, 1100, TabM = 2):
            $ EmmaX.change_face("surprised")
            $ EmmaX.change_stat("obedience", 90, 1)
            $ EmmaX.change_stat("obedience", 70, 2)
            $ EmmaX.change_stat("inhibition", 70, 3)
            $ EmmaX.change_stat("inhibition", 30, 2)
            "As you slide a finger in, [EmmaX.name] seems a bit surprised, but seems into it."
            jump Emma_IP_Prep
        else:
            $ EmmaX.change_face("surprised",2)
            $ EmmaX.change_stat("love", 80, -2)
            $ EmmaX.change_stat("obedience", 50, -3)
            ch_e "Oooh!"
            "She slaps your hand back."
            $ EmmaX.change_face("perplexed",1)
            ch_e "Careful what you put in there, you may not get it back."
            return

    if ApprovalCheck(EmmaX, 1100, TabM = 2):
        if EmmaX.Forced:
            $ EmmaX.change_face("sad")
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
            $ EmmaX.change_stat("obedience", 90, 1)
            $ EmmaX.change_stat("inhibition", 60, 1)
            ch_e "If you must. . ."
        else:
            $ EmmaX.change_face("sexy", 1)
            $ EmmaX.change_stat("love", 90, 1)
            $ EmmaX.change_stat("inhibition", 50, 3)
            ch_e "Mmmmmm. . ."
        $ EmmaX.change_stat("obedience", 20, 1)
        $ EmmaX.change_stat("obedience", 60, 1)
        $ EmmaX.change_stat("inhibition", 70, 2)
        jump Emma_IP_Prep
    else:

        $ EmmaX.change_face("bemused", 2)
        ch_e "No. Thank you."
        $ EmmaX.blushing = 1
    return


label Emma_IP_Prep:
    if not EmmaX.action_counter["finger_pussy"]:
        $ EmmaX.action_counter["finger_pussy"] = 1
        $ EmmaX.SEXP += 10
        if EmmaX.Forced:
            $ EmmaX.change_stat("love", 90, -60)
            $ EmmaX.change_stat("obedience", 70, 55)
            $ EmmaX.change_stat("inhibition", 80, 35)
        else:
            $ EmmaX.change_stat("love", 90, 10)
            $ EmmaX.change_stat("obedience", 70, 20)
            $ EmmaX.change_stat("inhibition", 80, 25)

    if not EmmaX.Forced and action_context != "auto":
        call Girl_Undress (EmmaX, "bottom")
        if "angry" in EmmaX.recent_history:
            return


    if Taboo:
        $ EmmaX.inhibition += int(Taboo/10)
        $ EmmaX.lust += int(Taboo/5)

    $ Line = 0
    $ action_speed = 2
    return







label Emma_Lick_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (EmmaX)

    if EmmaX.action_counter["eat_pussy"]:
        $ approval_bonus += 15
    if EmmaX.PantsNum() > 6 or EmmaX.HoseNum() >= 5:
        $ approval_bonus -= 15
    if EmmaX.lust > 95:
        $ approval_bonus += 20
    elif EmmaX.lust > 85:
        $ approval_bonus += 15
    if action_context == "shift":
        $ approval_bonus += 10
    if EmmaX.lust > 85 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in EmmaX.Traits:
        $ approval_bonus += (4*Taboo)
    if EmmaX in Player.Harem or "sex friend" in EmmaX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in EmmaX.Traits:
        $ approval_bonus -= 25
    if EmmaX.event_counter["forced"] and not EmmaX.Forced:
        $ approval_bonus -= 5*EmmaX.event_counter["forced"]

    if Taboo and "no_taboo" in EmmaX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in EmmaX.history:
        $ approval_bonus -= 20

    if "no_lick pussy" in EmmaX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_lick pussy" in EmmaX.recent_history else 0

    $ Approval = ApprovalCheck(EmmaX, 1250, TabM = 4)

    if action_context == "auto":
        if Approval:
            $ EmmaX.change_face("surprised")
            $ EmmaX.change_stat("obedience", 90, 1)
            $ EmmaX.change_stat("obedience", 70, 2)
            $ EmmaX.change_stat("inhibition", 70, 3)
            $ EmmaX.change_stat("inhibition", 30, 2)
            "As you crouch down and start to lick her pussy, [EmmaX.name] jumps, but then softens."
            $ EmmaX.change_face("sexy")
            jump Emma_LP_Prep
        else:
            $ EmmaX.change_face("surprised")
            $ EmmaX.change_stat("love", 80, -2)
            $ EmmaX.change_stat("obedience", 50, -3)
            ch_e "I like where your head is at, so to speak, but perhaps hold off on that."
            $ EmmaX.change_face("perplexed",1)
            "She pushes your head back away from her."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "eat_pussy" in EmmaX.recent_history:
        $ EmmaX.change_face("sexy", 1)
        ch_e "Mmmm, again? I suppose. . ."
        jump Emma_LP_Prep
    elif "eat_pussy" in EmmaX.daily_history:
        $ EmmaX.change_face("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Huh? Again?",
            "I must have done something right.",
            "What a queen deserves. . .",
            "Mmm. . ."])
        ch_e "[Line]"

    if Approval >= 2:
        if EmmaX.Forced:
            $ EmmaX.change_face("sad")
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
            $ EmmaX.change_stat("obedience", 90, 1)
            $ EmmaX.change_stat("inhibition", 60, 1)
            ch_e "If you must. . ."
        else:
            $ EmmaX.change_face("sexy", 1)
            $ EmmaX.eyes = "closed"
            $ EmmaX.change_stat("love", 90, 1)
            $ EmmaX.change_stat("inhibition", 50, 3)
            $ EmmaX.change_stat("lust", 200, 3)
            ch_e "Mmmmmm. . ."
        $ EmmaX.change_stat("obedience", 20, 1)
        $ EmmaX.change_stat("obedience", 60, 1)
        $ EmmaX.change_stat("inhibition", 70, 2)
        jump Emma_LP_Prep
    else:

        $ EmmaX.change_face("angry", 1)
        if "no_lick pussy" in EmmaX.recent_history:
            ch_e "Your persistance is doing you no favors, [EmmaX.player_petname]."
        elif Taboo and "no_taboo" in EmmaX.daily_history and "no_lick pussy" in EmmaX.daily_history:
            ch_e "You already got your answer!"
        elif "no_lick pussy" in EmmaX.daily_history:
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "As I said, not here, [EmmaX.player_petname]."
        elif not EmmaX.action_counter["eat_pussy"]:
            $ EmmaX.change_face("bemused")
            ch_e "I'm not sure we're at that stage, [EmmaX.player_petname]. . ."
        else:
            $ EmmaX.change_face("bemused")
            ch_e "I'm really not comfortable with that. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_lick pussy" in EmmaX.daily_history:
                $ EmmaX.change_face("bemused")
                ch_e "I appreciate your restraint, [EmmaX.player_petname]."
                return
            "I'm sure I can convince you later. . ." if "no_lick pussy" not in EmmaX.daily_history:
                $ EmmaX.change_face("sexy")
                ch_e "I'll be thinking about it, [EmmaX.player_petname]."
                $ EmmaX.change_stat("love", 80, 2)
                $ EmmaX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ EmmaX.recent_history.append("no_taboo")
                    $ EmmaX.daily_history.append("no_taboo")
                $ EmmaX.recent_history.append("no_lick pussy")
                $ EmmaX.daily_history.append("no_lick pussy")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ EmmaX.change_face("sexy")
                    $ EmmaX.change_stat("obedience", 90, 2)
                    $ EmmaX.change_stat("obedience", 50, 2)
                    ch_e "You present a compelling case. . ."
                    $ EmmaX.change_stat("inhibition", 70, 3)
                    $ EmmaX.change_stat("inhibition", 40, 2)
                    jump Emma_LP_Prep
                else:
                    $ EmmaX.change_face("sexy")
                    ch_e "I would, but still no, [EmmaX.player_petname]."
            "[[Get in there anyway]":

                $ Approval = ApprovalCheck(EmmaX, 750, "OI", TabM = 4)
                if Approval > 1 or (Approval and EmmaX.Forced):
                    $ EmmaX.change_face("sad")
                    $ EmmaX.change_stat("love", 70, -5, 1)
                    $ EmmaX.change_stat("love", 200, -2)
                    ch_e "If you insist. . ."
                    $ EmmaX.change_stat("obedience", 50, 4)
                    $ EmmaX.change_stat("inhibition", 80, 1)
                    $ EmmaX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ EmmaX.Forced = 1
                    jump Emma_LP_Prep
                else:
                    $ EmmaX.change_stat("love", 200, -15)
                    $ EmmaX.change_face("angry", 1)
                    "She shoves your head back."
                    $ EmmaX.recent_history.append("angry")
                    $ EmmaX.daily_history.append("angry")

    if "no_lick pussy" in EmmaX.daily_history:
        ch_e "I don't appreciate having to repeat myself, [EmmaX.player_petname]."
        $ EmmaX.recent_history.append("angry")
        $ EmmaX.daily_history.append("angry")
    elif EmmaX.Forced:
        $ EmmaX.change_face("angry", 1)
        ch_e "I really can't, [EmmaX.player_petname]."
        $ EmmaX.change_stat("lust", 80, 5)
        $ EmmaX.change_stat("obedience", 50, -2)
        $ EmmaX.recent_history.append("angry")
        $ EmmaX.daily_history.append("angry")
    elif Taboo:
        $ EmmaX.change_face("angry", 1)
        $ EmmaX.recent_history.append("no_taboo")
        $ EmmaX.daily_history.append("no_taboo")
        ch_e "I have a reputation to maintain."
    elif EmmaX.action_counter["eat_pussy"]:
        $ EmmaX.change_face("sad")
        ch_e "Keep your head out of there."
    else:
        $ EmmaX.change_face("surprised")
        ch_e "I know, I'm as disappointed as you are."
        $ EmmaX.change_face()
    $ EmmaX.recent_history.append("no_lick pussy")
    $ EmmaX.daily_history.append("no_lick pussy")
    $ approval_bonus = 0
    return

label Emma_LP_Prep:
    if offhand_action == "eat_pussy":
        return

    if EmmaX.pose in ("doggy","sex"):
        call ViewShift (EmmaX, EmmaX.pose, 0, "eat_pussy")
    else:
        call ViewShift (EmmaX, "pussy", 0, "eat_pussy")

    if action_context == EmmaX:

        $ action_context = 0
        if (EmmaX.legs and not EmmaX.Upskirt) or (EmmaX.underwear and not EmmaX.underwearDown):

            if ApprovalCheck(EmmaX, 1250, TabM = 1) or (EmmaX.SeenPussy and ApprovalCheck(EmmaX, 500) and not Taboo):
                $ EmmaX.Upskirt = 1
                $ EmmaX.underwearDown = 1
                $ Line = 0
                if EmmaX.PantsNum() == 5:
                    $ Line = EmmaX.name + " hikes up her_skirt"
                elif EmmaX.PantsNum() >= 6:
                    $ Line = EmmaX.name + " pulls down her " + EmmaX.legs
                else:
                    $ Line = 0
                if EmmaX.underwear:
                    if Line:

                        "[Line] and pulls her [EmmaX.underwear] out of the way."
                        "She then grabs your head and pulls it to her crotch, clearly intending you to get to work."
                    else:

                        "She pulls her [EmmaX.underwear] out of the way, and then shoves your face into her crotch."
                        "She clearly intends for you to get to work."
                else:

                    "[Line], and then shoves your face into her crotch."
                    "She clearly intends for you to get to work."
                call Emma_First_Bottomless (1)
            else:
                "[EmmaX.name] grabs your head and pulls it to her crotch, clearly intending you to get to work."
        else:
            "[EmmaX.name] grabs your head and pulls it to her crotch, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ EmmaX.change_stat("inhibition", 80, 3)
                $ EmmaX.change_stat("inhibition", 50, 2)
                "You start licking."
            "Praise her.":
                $ EmmaX.change_face("sexy", 1)
                $ EmmaX.change_stat("inhibition", 80, 3)
                ch_p "Mmm, I like this idea, [EmmaX.petname]."
                $ EmmaX.nameCheck()
                "You start licking."
                $ EmmaX.change_stat("love", 85, 1)
                $ EmmaX.change_stat("obedience", 90, 1)
                $ EmmaX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your head away."
                $ EmmaX.change_face("surprised")
                $ EmmaX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [EmmaX.petname]."
                $ EmmaX.nameCheck()
                "[EmmaX.name] pulls back."
                $ EmmaX.change_stat("obedience", 90, 1)
                $ EmmaX.change_stat("obedience", 50, 1)
                $ EmmaX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ EmmaX.AddWord(1,"refused","refused")
                return


    if not EmmaX.Forced and action_context != "auto":
        $ approval_bonus = 0
        if EmmaX.PantsNum() > 6:
            $ approval_bonus = 15
        call Bottoms_Off (EmmaX)
        if "angry" in EmmaX.recent_history:
            return

    $ approval_bonus = 0
    if not EmmaX.action_counter["eat_pussy"]:
        if EmmaX.Forced:
            $ EmmaX.change_stat("love", 90, -30)
            $ EmmaX.change_stat("obedience", 70, 35)
            $ EmmaX.change_stat("inhibition", 80, 75)
        else:
            $ EmmaX.change_stat("love", 90, 35)
            $ EmmaX.change_stat("obedience", 70, 15)
            $ EmmaX.change_stat("inhibition", 80, 35)
    if Taboo:
        $ EmmaX.inhibition += int(Taboo/10)
        $ EmmaX.lust += int(Taboo/5)
    if action_context:
        $ renpy.pop_call()
        $ action_context = 0

    if EmmaX.PantsNum() == 5:
        $ EmmaX.Upskirt = 1
        $ EmmaX.SeenPanties = 1
    call Emma_First_Bottomless (1)

    $ Line = 0
    $ counter = 0
    if Taboo:
        $ EmmaX.DrainWord("no_taboo")
    $ EmmaX.DrainWord("no_lick pussy")
    $ EmmaX.recent_history.append("eat_pussy")
    $ EmmaX.daily_history.append("eat_pussy")
    if EmmaX.pose in ("doggy","sex"):
        call ViewShift (EmmaX, EmmaX.pose, 0, "eat_pussy")
    else:
        call ViewShift (EmmaX, "pussy", 0, "eat_pussy")


label Emma_LP_Cycle:
    if offhand_action == "kiss":
        $ offhand_action = 0
    while Round > 0:
        call ViewShift (EmmaX, EmmaX.pose, 0, "eat_pussy")
        call shift_focus (EmmaX)
        $ EmmaX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (EmmaX)
                    $ counter += 1
                    $ Round -= 1
                    jump Emma_LP_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (EmmaX, "menu")
                    jump Emma_LP_Cycle
                "Other options":

                    menu:
                        "Offhand action":
                            if EmmaX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ EmmaX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (EmmaX, "tired")
                        "Shift primary action":

                            if EmmaX.remaining_actions and multi_action:
                                menu:
                                    "Pull out and start rubbing again.":
                                        if EmmaX.remaining_actions and multi_action:
                                            $ action_context = "pullback"
                                            call Emma_LP_After
                                            call Emma_Fondle_Pussy
                                        else:
                                            call Sex_Basic_Dialog (EmmaX, "tired")
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Emma_LP_After
                                        call Emma_Dildo_Pussy
                                    "Never Mind":
                                        jump Emma_LP_Cycle
                            else:
                                call Sex_Basic_Dialog (EmmaX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Emma_LP_After
                            call Offhand_Set
                        "Shift your focus (locked)" if not offhand_action:
                            pass

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Asks [EmmaX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (EmmaX)
                                "Asks [EmmaX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (EmmaX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (EmmaX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Emma_LP_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Emma_LP_Cycle
                                "Never mind":
                                    jump Emma_LP_Cycle

                        "Show her feet" if not ShowFeet and (EmmaX.pose == "doggy" or EmmaX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (EmmaX.pose == "doggy" or EmmaX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [EmmaX.name]":

                            call Girl_Undress (EmmaX)
                        "Clean up [EmmaX.name] (locked)" if not EmmaX.Spunk:
                            pass
                        "Clean up [EmmaX.name]" if EmmaX.Spunk:
                            call Girl_Cleanup (EmmaX, "ask")
                        "Never mind":
                            jump Emma_LP_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Emma_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Emma_LP_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Emma_Pos_Reset
                    $ Line = 0
                    jump Emma_LP_After


        if EmmaX.underwear or EmmaX.PantsNum() > 6 or EmmaX.HoseNum() >= 5:
            call Girl_Undress (EmmaX, "auto")

        call shift_focus (EmmaX)
        call Sex_Dialog (EmmaX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or EmmaX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (EmmaX)
                if "angry" in EmmaX.recent_history:
                    call Emma_Pos_Reset
                    return
                $ EmmaX.change_stat("lust", 200, 5)
                if 100 > EmmaX.lust >= 70 and EmmaX.session_orgasms < 2:
                    $ EmmaX.recent_history.append("unsatisfied")
                    $ EmmaX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Emma_LP_After
                $ Line = "came"

            if EmmaX.lust >= 100:

                call Girl_Cumming (EmmaX)
                if action_context == "shift" or "angry" in EmmaX.recent_history:
                    jump Emma_LP_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in EmmaX.recent_history:
                    "[EmmaX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Emma_LP_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif counter == (5 + EmmaX.action_counter["eat_pussy"]):
            $ EmmaX.brows = "confused"
            ch_e "Isn't it just delicious?"
        elif EmmaX.lust >= 80:
            pass
        elif counter == (15 + EmmaX.action_counter["eat_pussy"]) and EmmaX.SEXP >= 15 and not ApprovalCheck(EmmaX, 1500):
            $ EmmaX.brows = "confused"
            menu:
                ch_e "[EmmaX.player_petname], I know you're having fun down there, but maybe we could try something else."
                "Finish up.":
                    "You let go. . ."
                    jump Emma_LP_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Emma_LP_After
                "No, this is fun.":
                    if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):
                        $ EmmaX.change_stat("love", 200, -5)
                        $ EmmaX.change_stat("obedience", 50, 3)
                        $ EmmaX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ EmmaX.change_face("angry", 1)
                        call Emma_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_e "Well perhaps you are enjoying yourself, but I'm tired of this."
                        $ EmmaX.change_stat("love", 50, -3, 1)
                        $ EmmaX.change_stat("love", 80, -4, 1)
                        $ EmmaX.change_stat("obedience", 30, -1, 1)
                        $ EmmaX.change_stat("obedience", 50, -1, 1)
                        $ EmmaX.recent_history.append("angry")
                        $ EmmaX.daily_history.append("angry")
                        jump Emma_LP_After


        call Escalation (EmmaX)

        if Round == 10:
            ch_e "It's getting late. . ."
        elif Round == 5:
            ch_e "We should take a break soon."


    $ EmmaX.change_face("bemused", 0)
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."


label Emma_LP_After:
    if not action_context:
        call Emma_Pos_Reset

    $ EmmaX.change_face("sexy")

    $ EmmaX.action_counter["eat_pussy"] += 1
    $ EmmaX.remaining_actions -=1
    if EmmaX.PantsNum() <= 6 or EmmaX.Upskirt:
        $ EmmaX.addiction_rate += 1
        if "addictive" in Player.Traits:
            $ EmmaX.addiction_rate += 1

    if Partner == "Rogue":
        call Partner_Like (EmmaX, 3, 2)
    else:
        call Partner_Like (EmmaX, 2)

    if EmmaX.action_counter["eat_pussy"] == 1:
        $ EmmaX.SEXP += 10
        if not action_context:
            if EmmaX.love >= 500 and "unsatisfied" not in EmmaX.recent_history:
                ch_e "I could really take advantage of your services more often. . ."
            elif EmmaX.obedience <= 500 and Player.focus <= 20:
                $ EmmaX.change_face("perplexed", 1)
                ch_e "I suppose that worked out for both of us. . ."

    $ approval_bonus = 0


    call Checkout
    return






label Emma_Fondle_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (EmmaX)

    if EmmaX.action_counter["fondle_ass"]:
        $ approval_bonus += 10
    if EmmaX.PantsNum() > 6 or EmmaX.HoseNum() >= 5:
        $ approval_bonus -= 5
    if EmmaX.lust > 75:
        $ approval_bonus += 15
    if "exhibitionist" in EmmaX.Traits:
        $ approval_bonus += Taboo
    if EmmaX in Player.Harem or "sex friend" in EmmaX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in EmmaX.Traits:
        $ approval_bonus -= 25
    if EmmaX.event_counter["forced"] and not EmmaX.Forced:
        $ approval_bonus -= 5*EmmaX.event_counter["forced"]

    if Taboo and "no_taboo" in EmmaX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in EmmaX.history:
        $ approval_bonus -= 20

    if "no_fondle ass" in EmmaX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle ass" in EmmaX.recent_history else 0

    $ Approval = ApprovalCheck(EmmaX, 850, TabM=1)

    if action_context == "auto":
        if Approval:
            $ EmmaX.change_face("surprised", 1)
            $ EmmaX.change_stat("obedience", 70, 2)
            $ EmmaX.change_stat("inhibition", 40, 2)
            "As your hand creeps down her backside, [EmmaX.name] jumps a bit, and then relaxes."
            $ EmmaX.change_face("sexy")
            jump Emma_FA_Prep
        else:
            $ EmmaX.change_face("surprised")
            $ EmmaX.change_stat("obedience", 50, -3)
            ch_e "Hands off, [EmmaX.player_petname]."
            $ EmmaX.change_face("bemused")
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if action_context == "pullback":
        $ EmmaX.change_face("surprised")
        $ EmmaX.brows = "sad"
        if EmmaX.lust > 80:
            $ EmmaX.change_stat("love", 70, -4)
        $ EmmaX.change_stat("obedience", 90, 1)
        $ EmmaX.change_stat("obedience", 70, 2)
        "As your finger slides out, [EmmaX.name] gasps and looks upset."
        jump Emma_FA_Prep
    elif "fondle_ass" in EmmaX.recent_history:
        $ EmmaX.change_face("sexy", 1)
        ch_e "Mmmm, again? I suppose. . ."
        jump Emma_FA_Prep
    elif "fondle_ass" in EmmaX.daily_history:
        $ EmmaX.change_face("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Perhaps not so rough this time?",
            "Mmm. . ."])
        ch_e "[Line]"

    if Approval >= 2:
        if EmmaX.Forced:
            $ EmmaX.change_face("sad")
            $ EmmaX.change_stat("love", 70, -2, 1)
            $ EmmaX.change_stat("obedience", 90, 2)
            $ EmmaX.change_stat("inhibition", 60, 2)
            ch_e "If you insist. . ."
        else:
            $ EmmaX.change_face("bemused, 1")
            ch_e "I can't exactly refuse. . ."
        $ EmmaX.change_stat("lust", 200, 3)
        $ EmmaX.change_stat("obedience", 60, 1)
        $ EmmaX.change_stat("inhibition", 70, 1)
        jump Emma_FA_Prep
    else:

        $ EmmaX.change_face("angry", 1)
        if "no_fondle ass" in EmmaX.recent_history:
            ch_e "Your persistance is doing you no favors, [EmmaX.player_petname]."
        elif Taboo and "no_taboo" in EmmaX.daily_history and "no_fondle ass" in EmmaX.daily_history:
            ch_e "I told you not to touch me like that in public!"
        elif "no_fondle ass" in EmmaX.daily_history:
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "As I said, not here, [EmmaX.player_petname]."
        elif not EmmaX.action_counter["fondle_ass"]:
            $ EmmaX.change_face("bemused")
            ch_e "Not yet, [EmmaX.player_petname]. . ."
        else:
            $ EmmaX.change_face("bemused")
            ch_e "Let's not, ok [EmmaX.player_petname]?"
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle ass" in EmmaX.daily_history:
                $ EmmaX.change_face("bemused")
                ch_e "I appreciate your restraint, [EmmaX.player_petname]."
                return
            "Maybe later?" if "no_fondle ass" not in EmmaX.daily_history:
                $ EmmaX.change_face("sexy")
                ch_e "Perhaps."
                $ EmmaX.change_stat("love", 80, 2)
                $ EmmaX.change_stat("inhibition", 50, 2)
                if Taboo:
                    $ EmmaX.recent_history.append("no_taboo")
                    $ EmmaX.daily_history.append("no_taboo")
                $ EmmaX.recent_history.append("no_fondle ass")
                $ EmmaX.daily_history.append("no_fondle ass")
                return
            "Just one good squeeze?":
                if Approval:
                    $ EmmaX.change_face("sexy")
                    $ EmmaX.change_stat("obedience", 90, 1)
                    $ EmmaX.change_stat("obedience", 50, 2)
                    ch_e "I do enjoy hearing you beg. . ."
                    $ EmmaX.change_stat("inhibition", 70, 1)
                    $ EmmaX.change_stat("inhibition", 40, 2)
                    jump Emma_FA_Prep
                else:
                    $ EmmaX.change_face("sexy")
                    ch_e "No."
            "[[Start fondling anyway]":

                $ Approval = ApprovalCheck(EmmaX, 250, "OI", TabM = 3)
                if Approval > 1 or (Approval and EmmaX.Forced):
                    $ EmmaX.change_face("sad")
                    $ EmmaX.change_stat("love", 70, -3, 1)
                    $ EmmaX.change_stat("love", 200, -1)
                    ch_e "Fine, I suppose."
                    $ EmmaX.change_stat("obedience", 50, 3)
                    $ EmmaX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ EmmaX.Forced = 1
                    jump Emma_FA_Prep
                else:
                    $ EmmaX.change_stat("love", 200, -10)
                    $ EmmaX.change_face("angry", 1)
                    "She slaps your hand away."
                    $ EmmaX.recent_history.append("angry")
                    $ EmmaX.daily_history.append("angry")

    if "no_fondle ass" in EmmaX.daily_history:
        ch_e "I don't appreciate having to repeat myself, [EmmaX.player_petname]."
        $ EmmaX.recent_history.append("angry")
        $ EmmaX.daily_history.append("angry")
    elif EmmaX.Forced:
        $ EmmaX.change_face("angry", 1)
        ch_e "Do you want to keep those fingers?"
        $ EmmaX.change_stat("lust", 60, 5)
        $ EmmaX.change_stat("obedience", 50, -2)
        $ EmmaX.recent_history.append("angry")
        $ EmmaX.daily_history.append("angry")
    elif Taboo:
        $ EmmaX.change_face("angry", 1)
        $ EmmaX.recent_history.append("no_taboo")
        $ EmmaX.daily_history.append("no_taboo")
        ch_e "I have a reputation to maintain."
    elif EmmaX.action_counter["fondle_ass"]:
        $ EmmaX.change_face("sad")
        ch_e "I'm sorry, keep your hands to yourself."
    else:
        $ EmmaX.change_face("sexy")
        $ EmmaX.mouth = "sad"
        ch_e "No."
    $ EmmaX.recent_history.append("no_fondle ass")
    $ EmmaX.daily_history.append("no_fondle ass")
    $ approval_bonus = 0
    return

ch_e "Sorry, I don't even know how I got here. . ."
return

label Emma_FA_Prep:
    if offhand_action == "fondle_ass":
        return
    if not EmmaX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (EmmaX)
        if "angry" in EmmaX.recent_history:
            return
    $ approval_bonus = 0
    if EmmaX.pose in ("doggy","sex"):
        call ViewShift (EmmaX, EmmaX.pose, 0, "fondle_ass")
    else:
        call ViewShift (EmmaX, "pussy", 0, "fondle_ass")
    if not EmmaX.action_counter["fondle_ass"]:
        if EmmaX.Forced:
            $ EmmaX.change_stat("love", 90, -20)
            $ EmmaX.change_stat("obedience", 70, 20)
            $ EmmaX.change_stat("inhibition", 80, 15)
        else:
            $ EmmaX.change_stat("love", 90, 10)
            $ EmmaX.change_stat("obedience", 70, 12)
            $ EmmaX.change_stat("inhibition", 80, 20)
    if Taboo:
        $ EmmaX.inhibition += int(Taboo/10)
        $ EmmaX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ EmmaX.DrainWord("no_taboo")
    $ EmmaX.DrainWord("no_fondle ass")
    $ EmmaX.recent_history.append("fondle_ass")
    $ EmmaX.daily_history.append("fondle_ass")
    if EmmaX.pose in ("doggy","sex"):
        call ViewShift (EmmaX, EmmaX.pose, 0, "fondle_ass")
    else:
        call ViewShift (EmmaX, "pussy", 0, "fondle_ass")

label Emma_FA_Cycle:
    while Round > 0:
        call ViewShift (EmmaX, EmmaX.pose, 0, "fondle_ass")
        call shift_focus (EmmaX)
        $ EmmaX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (EmmaX)
                    $ counter += 1
                    $ Round -= 1
                    jump Emma_FA_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (EmmaX, "menu")
                    jump Emma_FA_Cycle
                "Other options":

                    menu:
                        "Offhand action":
                            if EmmaX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ EmmaX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (EmmaX, "tired")
                        "Shift primary action":

                            if EmmaX.remaining_actions and multi_action:
                                menu:
                                    "I want to stick a finger in.":
                                        $ action_context = "shift"
                                        call Emma_FA_After
                                        call Emma_Insert_Ass
                                    "Just stick a finger in without asking.":
                                        $ action_context = "auto"
                                        call Emma_FA_After
                                        call Emma_Insert_Ass
                                    "I want to lick your asshole.":
                                        $ action_context = "shift"
                                        call Emma_FA_After
                                        call Emma_Lick_Ass
                                    "Just start licking.":
                                        $ action_context = "auto"
                                        call Emma_FA_After
                                        call Emma_Lick_Ass
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Emma_FA_After
                                        call Emma_Dildo_Ass
                                    "Never Mind":
                                        jump Emma_FA_Cycle
                            else:
                                call Sex_Basic_Dialog (EmmaX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Emma_FA_After
                            call Offhand_Set
                        "Shift your focus (locked)" if not offhand_action:
                            pass

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Asks [EmmaX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (EmmaX)
                                "Asks [EmmaX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (EmmaX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (EmmaX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Emma_FA_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Emma_FA_Cycle
                                "Never mind":
                                    jump Emma_FA_Cycle

                        "Show her feet" if not ShowFeet and (EmmaX.pose == "doggy" or EmmaX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (EmmaX.pose == "doggy" or EmmaX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [EmmaX.name]":

                            call Girl_Undress (EmmaX)
                        "Clean up [EmmaX.name] (locked)" if not EmmaX.Spunk:
                            pass
                        "Clean up [EmmaX.name]" if EmmaX.Spunk:
                            call Girl_Cleanup (EmmaX, "ask")
                        "Never mind":
                            jump Emma_FA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Emma_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Emma_FA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Emma_Pos_Reset
                    $ Line = 0
                    jump Emma_FA_After


        if EmmaX.underwear or EmmaX.PantsNum() > 6 or EmmaX.HoseNum() >= 5:
            call Girl_Undress (EmmaX, "auto")

        call shift_focus (EmmaX)
        call Sex_Dialog (EmmaX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or EmmaX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (EmmaX)
                if "angry" in EmmaX.recent_history:
                    call Emma_Pos_Reset
                    return
                $ EmmaX.change_stat("lust", 200, 5)
                if 100 > EmmaX.lust >= 70 and EmmaX.session_orgasms < 2 and EmmaX.SEXP >= 20:
                    $ EmmaX.recent_history.append("unsatisfied")
                    $ EmmaX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Emma_FA_After
                $ Line = "came"

            if EmmaX.lust >= 100:

                call Girl_Cumming (EmmaX)
                if action_context == "shift" or "angry" in EmmaX.recent_history:
                    jump Emma_FA_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in EmmaX.recent_history:
                    "[EmmaX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Emma_FA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif counter == (5 + EmmaX.action_counter["fondle_ass"]):
            $ EmmaX.brows = "confused"
            ch_e "Mmmm I do enjoy that. . ."
        elif EmmaX.lust >= 80:
            pass
        elif counter == (15 + EmmaX.action_counter["fondle_ass"]) and EmmaX.SEXP >= 15 and not ApprovalCheck(EmmaX, 1500):
            $ EmmaX.brows = "confused"
            menu:
                ch_e "[EmmaX.player_petname], this is nice, but could we do something else?"
                "Finish up.":
                    "You let go. . ."
                    jump Emma_FA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Emma_FA_After
                "No, this is fun.":
                    if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):
                        $ EmmaX.change_stat("love", 200, -5)
                        $ EmmaX.change_stat("obedience", 50, 3)
                        $ EmmaX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ EmmaX.change_face("angry", 1)
                        call Emma_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_e "Well perhaps you are enjoying yourself, but I'm tired of this."
                        $ EmmaX.change_stat("love", 50, -3, 1)
                        $ EmmaX.change_stat("love", 80, -4, 1)
                        $ EmmaX.change_stat("obedience", 30, -1, 1)
                        $ EmmaX.change_stat("obedience", 50, -1, 1)
                        $ EmmaX.recent_history.append("angry")
                        $ EmmaX.daily_history.append("angry")
                        jump Emma_FA_After


        call Escalation (EmmaX)

        if Round == 10:
            ch_e "It's getting late. . ."
        elif Round == 5:
            ch_e "We should take a break soon."


    $ EmmaX.change_face("bemused", 0)
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."


label Emma_FA_After:
    if not action_context:
        call Emma_Pos_Reset

    $ EmmaX.change_face("sexy")

    $ EmmaX.action_counter["fondle_ass"] += 1
    $ EmmaX.remaining_actions -=1
    if EmmaX.PantsNum() <= 6 or EmmaX.Upskirt:
        $ EmmaX.addiction_rate += 1
        if "addictive" in Player.Traits:
            $ EmmaX.addiction_rate += 1

        call Partner_Like (EmmaX, 2)

    if EmmaX.action_counter["fondle_ass"] == 1:
        $ EmmaX.SEXP += 4
        if not action_context:
            if EmmaX.love >= 500 and "unsatisfied" not in EmmaX.recent_history:
                ch_e "That was. . . nice. . ."
            elif EmmaX.obedience <= 500 and Player.focus <= 20:
                $ EmmaX.change_face("perplexed", 1)
                ch_e "Did you enjoy that?"

    $ approval_bonus = 0


    call Checkout
    return





label Emma_Insert_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (EmmaX)

    if EmmaX.action_counter["finger_ass"]:
        $ approval_bonus += 25
    if EmmaX.PantsNum() > 6 or EmmaX.HoseNum() >= 5:
        $ approval_bonus -= 15
    if EmmaX.lust > 85:
        $ approval_bonus += 15
    if EmmaX.lust > 95:
        $ approval_bonus += 5
    if action_context == "shift":
        $ approval_bonus += 10
    if EmmaX.lust > 85 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in EmmaX.Traits:
        $ approval_bonus += (4*Taboo)
    if EmmaX in Player.Harem or "sex friend" in EmmaX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in EmmaX.Traits:
        $ approval_bonus -= 25
    if EmmaX.event_counter["forced"] and not EmmaX.Forced:
        $ approval_bonus -= 5*EmmaX.event_counter["forced"]

    if Taboo and "no_taboo" in EmmaX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in EmmaX.history:
        $ approval_bonus -= 20

    if "no_insert ass" in EmmaX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_insert ass" in EmmaX.recent_history else 0

    $ Approval = ApprovalCheck(EmmaX, 1300, TabM = 3)

    if action_context == "auto":
        if Approval:
            $ EmmaX.change_face("surprised")
            $ EmmaX.change_stat("obedience", 90, 2)
            $ EmmaX.change_stat("obedience", 70, 2)
            $ EmmaX.change_stat("inhibition", 80, 2)
            $ EmmaX.change_stat("inhibition", 30, 2)
            "As you slide a finger in, [EmmaX.name] tightens around it in surprise, but seems into it."
            $ EmmaX.change_face("sexy")
            jump Emma_IA_Prep
        else:
            $ EmmaX.change_face("surprised")
            $ EmmaX.change_stat("love", 80, -2)
            $ EmmaX.change_stat("obedience", 50, -3)
            ch_e "Whoa, back off, [EmmaX.player_petname]."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "finger_ass" in EmmaX.daily_history:
        $ EmmaX.change_face("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax, gently. . .",
            "Mmm. . ."])
        ch_e "[Line]"

    if Approval >= 2:
        if EmmaX.Forced:
            $ EmmaX.change_face("sad")
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
            $ EmmaX.change_stat("obedience", 90, 1)
            $ EmmaX.change_stat("inhibition", 60, 1)
            ch_e "If you must. . ."
        else:
            $ EmmaX.change_face("sexy", 1)
            $ EmmaX.eyes = "closed"
            $ EmmaX.change_stat("love", 90, 1)
            $ EmmaX.change_stat("inhibition", 50, 3)
            $ EmmaX.change_stat("lust", 200, 3)
            ch_e "Mmmmm. . ."
        $ EmmaX.change_stat("obedience", 20, 1)
        $ EmmaX.change_stat("obedience", 60, 1)
        $ EmmaX.change_stat("inhibition", 70, 2)
        jump Emma_IA_Prep
    else:

        $ EmmaX.change_face("angry", 1)
        if "no_insert ass" in EmmaX.recent_history:
            ch_e "Your persistance is doing you no favors, [EmmaX.player_petname]."
        elif Taboo and "no_taboo" in EmmaX.daily_history and "no_insert ass" in EmmaX.daily_history:
            ch_e "I told you that wasn't appropriate!"
        elif "no_insert ass" in EmmaX.daily_history:
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "As I said, not here, [EmmaX.player_petname]."
        elif not EmmaX.action_counter["finger_ass"]:
            $ EmmaX.change_face("perplexed", 1)
            ch_e "That's really not my usual style. . ."
        else:
            $ EmmaX.change_face("bemused")
            ch_e "I'd rather not today. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_insert ass" in EmmaX.daily_history:
                $ EmmaX.change_face("bemused")
                ch_e "I appreciate your restraint, [EmmaX.player_petname]."
                return
            "Maybe later?" if "no_insert ass" not in EmmaX.daily_history:
                $ EmmaX.change_face("sexy")
                ch_e "It's. . . possible, [EmmaX.player_petname]."
                $ EmmaX.change_stat("love", 80, 2)
                $ EmmaX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ EmmaX.recent_history.append("no_taboo")
                    $ EmmaX.daily_history.append("no_taboo")
                $ EmmaX.recent_history.append("no_insert ass")
                $ EmmaX.daily_history.append("no_insert ass")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ EmmaX.change_face("sexy")
                    $ EmmaX.change_stat("obedience", 90, 2)
                    $ EmmaX.change_stat("obedience", 50, 2)
                    ch_e "You're probably right. . ."
                    $ EmmaX.change_stat("inhibition", 70, 3)
                    $ EmmaX.change_stat("inhibition", 40, 2)
                    jump Emma_IA_Prep
                else:
                    $ EmmaX.change_face("bemused")
                    ch_e "I don't think that I would."
            "[[Slide a finger in anyway]":

                $ Approval = ApprovalCheck(EmmaX, 950, "OI", TabM = 3)
                if Approval > 1 or (Approval and EmmaX.Forced):
                    $ EmmaX.change_face("surprised", 1)
                    $ EmmaX.change_stat("love", 70, -5, 1)
                    $ EmmaX.change_stat("love", 200, -2)
                    ch_e "Well hello there. . ."
                    $ EmmaX.change_face("sad")
                    $ EmmaX.change_stat("obedience", 50, 4)
                    $ EmmaX.change_stat("inhibition", 80, 1)
                    $ EmmaX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ EmmaX.Forced = 1
                    jump Emma_IA_Prep
                else:
                    $ EmmaX.change_stat("love", 200, -15)
                    $ EmmaX.change_face("angry", 1)
                    "She slaps your hand away."
                    $ EmmaX.recent_history.append("angry")
                    $ EmmaX.daily_history.append("angry")

    if "no_insert ass" in EmmaX.daily_history:
        ch_e "I don't appreciate having to repeat myself, [EmmaX.player_petname]."
        $ EmmaX.recent_history.append("angry")
        $ EmmaX.daily_history.append("angry")
    elif EmmaX.Forced:
        $ EmmaX.change_face("angry", 1)
        ch_e "I'm not going that far today."
        if ApprovalCheck(EmmaX, 500, "I"):
            $ EmmaX.change_stat("lust", 80, 10)
        else:
            $ EmmaX.change_stat("lust", 50, 3)
        $ EmmaX.change_stat("obedience", 50, -2)
        $ EmmaX.recent_history.append("angry")
        $ EmmaX.daily_history.append("angry")
    elif Taboo:
        $ EmmaX.change_face("angry", 1)
        $ EmmaX.recent_history.append("no_taboo")
        $ EmmaX.daily_history.append("no_taboo")
        ch_e "I have a reputation to maintain."
    elif EmmaX.action_counter["finger_ass"]:
        $ EmmaX.change_face("sad")
        ch_e "I don't feel like it."
    else:
        $ EmmaX.change_face("surprised")
        ch_e "Not today, [EmmaX.player_petname]."
        $ EmmaX.change_face()
    $ EmmaX.recent_history.append("no_insert ass")
    $ EmmaX.daily_history.append("no_insert ass")
    $ approval_bonus = 0
    return


label Emma_IA_Prep:
    if offhand_action == "finger_ass":
        return

    if EmmaX.pose in ("doggy","sex"):
        call ViewShift (EmmaX, EmmaX.pose, 0, "finger_ass")
    else:
        call ViewShift (EmmaX, "pussy", 0, "finger_ass")

    if action_context == EmmaX:

        $ action_context = 0
        if (EmmaX.legs and not EmmaX.Upskirt) or (EmmaX.underwear and not EmmaX.underwearDown):

            if ApprovalCheck(EmmaX, 1250, TabM = 1) or (EmmaX.SeenPussy and ApprovalCheck(EmmaX, 500) and not Taboo):
                $ EmmaX.Upskirt = 1
                $ EmmaX.underwearDown = 1
                $ Line = 0
                if EmmaX.PantsNum() == 5:
                    $ Line = EmmaX.name + " hikes up her_skirt"
                elif EmmaX.PantsNum() >= 6:
                    $ Line = EmmaX.name + " pulls down her " + EmmaX.legs
                else:
                    $ Line = 0
                if EmmaX.underwear:
                    if Line:

                        "[Line] and pulls her [EmmaX.underwear] out of the way."
                        "She then grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
                    else:

                        "She pulls her [EmmaX.underwear] out of the way, and then presses your hand against her asshole."
                        "She clearly intends for you to get to work."
                else:

                    "[Line], and then presses your hand against her asshole."
                    "She clearly intends for you to get to work."
                call Emma_First_Bottomless (1)
            else:
                "[EmmaX.name] grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
        else:
            "[EmmaX.name] grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ EmmaX.change_stat("inhibition", 80, 3)
                $ EmmaX.change_stat("inhibition", 50, 2)
                "You press your finger into it."
            "Praise her.":
                $ EmmaX.change_face("sexy", 1)
                $ EmmaX.change_stat("inhibition", 80, 3)
                ch_p "Dirty girl, [EmmaX.petname]."
                $ EmmaX.nameCheck()
                "You press your finger into it."
                $ EmmaX.change_stat("love", 85, 1)
                $ EmmaX.change_stat("obedience", 90, 1)
                $ EmmaX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your hand back."
                $ EmmaX.change_face("surprised")
                $ EmmaX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [EmmaX.petname]."
                $ EmmaX.nameCheck()
                "[EmmaX.name] pulls back."
                $ EmmaX.change_stat("obedience", 90, 1)
                $ EmmaX.change_stat("obedience", 50, 1)
                $ EmmaX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ EmmaX.AddWord(1,"refused","refused")
                return


    if not EmmaX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (EmmaX)
        if "angry" in EmmaX.recent_history:
            return

    $ approval_bonus = 0
    if not EmmaX.action_counter["finger_ass"]:
        if EmmaX.Forced:
            $ EmmaX.change_stat("love", 90, -50)
            $ EmmaX.change_stat("obedience", 70, 60)
            $ EmmaX.change_stat("inhibition", 80, 35)
        else:
            $ EmmaX.change_stat("love", 90, 10)
            $ EmmaX.change_stat("obedience", 70, 20)
            $ EmmaX.change_stat("inhibition", 80, 25)

    if Taboo:
        $ EmmaX.inhibition += int(Taboo/10)
        $ EmmaX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ EmmaX.DrainWord("no_taboo")
    $ EmmaX.DrainWord("no_insert ass")
    $ EmmaX.recent_history.append("finger_ass")
    $ EmmaX.daily_history.append("finger_ass")
    if EmmaX.pose in ("doggy","sex"):
        call ViewShift (EmmaX, EmmaX.pose, 0, "finger_ass")
    else:
        call ViewShift (EmmaX, "pussy", 0, "finger_ass")

label Emma_IA_Cycle:
    while Round > 0:
        call ViewShift (EmmaX, EmmaX.pose, 0, "finger_ass")
        call shift_focus (EmmaX)
        $ EmmaX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (EmmaX)
                    $ counter += 1
                    $ Round -= 1
                    jump Emma_IA_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (EmmaX, "menu")
                    jump Emma_IA_Cycle
                "Other options":

                    menu:
                        "Offhand action":
                            if EmmaX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ EmmaX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (EmmaX, "tired")
                        "Shift primary action":

                            if EmmaX.remaining_actions and multi_action:
                                menu:
                                    "Pull out and start rubbing again.":
                                        $ action_context = "pullback"
                                        call Emma_IA_After
                                        call Emma_Fondle_Ass
                                    "I want to lick your asshole.":
                                        $ action_context = "shift"
                                        call Emma_IA_After
                                        call Emma_Lick_Ass
                                    "Just start licking.":
                                        $ action_context = "auto"
                                        call Emma_IA_After
                                        call Emma_Lick_Ass
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Emma_IA_After
                                        call Emma_Dildo_Ass
                                    "Never Mind":
                                        jump Emma_IA_Cycle
                            else:
                                call Sex_Basic_Dialog (EmmaX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Emma_IA_After
                            call Offhand_Set
                        "Shift your focus (locked)" if not offhand_action:
                            pass

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Asks [EmmaX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (EmmaX)
                                "Asks [EmmaX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (EmmaX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (EmmaX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Emma_IA_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Emma_IA_Cycle
                                "Never mind":
                                    jump Emma_IA_Cycle

                        "Show her feet" if not ShowFeet and (EmmaX.pose == "doggy" or EmmaX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (EmmaX.pose == "doggy" or EmmaX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [EmmaX.name]":

                            call Girl_Undress (EmmaX)
                        "Clean up [EmmaX.name] (locked)" if not EmmaX.Spunk:
                            pass
                        "Clean up [EmmaX.name]" if EmmaX.Spunk:
                            call Girl_Cleanup (EmmaX, "ask")
                        "Never mind":
                            jump Emma_IA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Emma_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Emma_IA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Emma_Pos_Reset
                    $ Line = 0
                    jump Emma_IA_After


        if EmmaX.underwear or EmmaX.PantsNum() > 6 or EmmaX.HoseNum() >= 5:
            call Girl_Undress (EmmaX, "auto")

        call shift_focus (EmmaX)
        call Sex_Dialog (EmmaX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or EmmaX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (EmmaX)
                if "angry" in EmmaX.recent_history:
                    call Emma_Pos_Reset
                    return
                $ EmmaX.change_stat("lust", 200, 5)
                if 100 > EmmaX.lust >= 70 and EmmaX.session_orgasms < 2:
                    $ EmmaX.recent_history.append("unsatisfied")
                    $ EmmaX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Emma_IA_After
                $ Line = "came"

            if EmmaX.lust >= 100:

                call Girl_Cumming (EmmaX)
                if action_context == "shift" or "angry" in EmmaX.recent_history:
                    jump Emma_IA_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in EmmaX.recent_history:
                    "[EmmaX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Emma_IA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif counter == (5 + EmmaX.action_counter["finger_ass"]):
            $ EmmaX.brows = "confused"
            ch_e "Ungh, You're getting going there. . ."
        elif EmmaX.lust >= 80:
            pass
        elif counter == (15 + EmmaX.action_counter["finger_ass"]) and EmmaX.SEXP >= 15 and not ApprovalCheck(EmmaX, 1500):
            $ EmmaX.brows = "confused"
            menu:
                ch_e "[EmmaX.player_petname], this is getting kind sore, maybe we could try something else."
                "Finish up.":
                    "You let go. . ."
                    jump Emma_IA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Emma_IA_After
                "No, this is fun.":
                    if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):
                        $ EmmaX.change_stat("love", 200, -5)
                        $ EmmaX.change_stat("obedience", 50, 3)
                        $ EmmaX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ EmmaX.change_face("angry", 1)
                        call Emma_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_e "Well perhaps you are enjoying yourself, but I'm tired of this."
                        $ EmmaX.change_stat("love", 50, -3, 1)
                        $ EmmaX.change_stat("love", 80, -4, 1)
                        $ EmmaX.change_stat("obedience", 30, -1, 1)
                        $ EmmaX.change_stat("obedience", 50, -1, 1)
                        $ EmmaX.recent_history.append("angry")
                        $ EmmaX.daily_history.append("angry")
                        jump Emma_IA_After


        call Escalation (EmmaX)

        if Round == 10:
            ch_e "It's getting late. . ."
        elif Round == 5:
            ch_e "We should take a break soon."


    $ EmmaX.change_face("bemused", 0)
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."

label Emma_IA_After:
    if not action_context:
        call Emma_Pos_Reset

    $ EmmaX.change_face("sexy")

    $ EmmaX.action_counter["finger_ass"] += 1
    $ EmmaX.remaining_actions -=1
    $ EmmaX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ EmmaX.addiction_rate += 1

    call Partner_Like (EmmaX, 2)

    if EmmaX.action_counter["finger_ass"] == 1:
        $ EmmaX.SEXP += 12
        if not action_context:
            if EmmaX.love >= 500 and "unsatisfied" not in EmmaX.recent_history:
                ch_e "You certainly surprise me. . ."
            elif EmmaX.obedience <= 500 and Player.focus <= 20:
                $ EmmaX.change_face("perplexed", 1)
                ch_e "Was it everything you dreamed?"

    $ approval_bonus = 0


    call Checkout
    return








label Emma_Lick_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (EmmaX)

    if EmmaX.action_counter["eat_ass"]:
        $ approval_bonus += 20
    if EmmaX.PantsNum() > 6 or EmmaX.HoseNum() >= 5:
        $ approval_bonus -= 25
    if EmmaX.lust > 95:
        $ approval_bonus += 20
    elif EmmaX.lust > 85:
        $ approval_bonus += 15
    if EmmaX.lust > 85 and action_context == "auto":
        $ approval_bonus += 10
    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in EmmaX.Traits:
        $ approval_bonus += (4*Taboo)
    if EmmaX in Player.Harem or "sex friend" in EmmaX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in EmmaX.Traits:
        $ approval_bonus -= 25
    if EmmaX.event_counter["forced"] and not EmmaX.Forced:
        $ approval_bonus -= 5*EmmaX.event_counter["forced"]

    if Taboo and "no_taboo" in EmmaX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in EmmaX.history:
        $ approval_bonus -= 20

    if "no_lick ass" in EmmaX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_lick ass" in EmmaX.recent_history else 0

    $ Approval = ApprovalCheck(EmmaX, 1550, TabM = 4)

    if action_context == "auto":
        if Approval:
            $ EmmaX.change_face("surprised")
            $ EmmaX.change_stat("obedience", 90, 1)
            $ EmmaX.change_stat("inhibition", 80, 3)
            $ EmmaX.change_stat("inhibition", 40, 2)
            "As you crouch down and start to lick her asshole, [EmmaX.name] startles briefly, but then begins to melt."
            $ EmmaX.change_face("sexy")
            jump Emma_LA_Prep
        else:
            $ EmmaX.change_face("surprised")
            $ EmmaX.change_stat("love", 80, -2)
            $ EmmaX.change_stat("obedience", 50, -3)
            ch_e "[EmmaX.player_petname]! Not now. . ."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "eat_ass" in EmmaX.recent_history:
        $ EmmaX.change_face("sexy", 1)
        ch_e "Mmmm, again? I suppose. . ."
        jump Emma_LA_Prep
    elif "eat_ass" in EmmaX.daily_history:
        $ EmmaX.change_face("sexy", 1)
        ch_e "You didn't get enough earlier?"


    if Approval >= 2:
        if EmmaX.Forced:
            $ EmmaX.change_face("sad")
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
            $ EmmaX.change_stat("obedience", 90, 2)
            $ EmmaX.change_stat("inhibition", 60, 2)
            ch_e "If you must. . ."
        else:
            $ EmmaX.change_face("sexy", 1)
            $ EmmaX.eyes = "closed"
            $ EmmaX.change_stat("love", 90, 1)
            $ EmmaX.change_stat("inhibition", 60, 2)
            $ EmmaX.change_stat("lust", 200, 3)
            ch_e "Mmm. . . naughty."
        $ EmmaX.change_stat("obedience", 20, 1)
        $ EmmaX.change_stat("obedience", 60, 1)
        $ EmmaX.change_stat("inhibition", 80, 2)
        jump Emma_LA_Prep
    else:

        $ EmmaX.change_face("angry", 1)
        if "no_lick ass" in EmmaX.recent_history:
            ch_e "Your persistance is doing you no favors, [EmmaX.player_petname]."
        elif Taboo and "no_taboo" in EmmaX.daily_history and "no_lick ass" in EmmaX.daily_history:
            ch_e "I told you not to touch me like that in public!"
        elif "no_lick ass" in EmmaX.daily_history:
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "As I said, not here, [EmmaX.player_petname]."
        elif not EmmaX.action_counter["eat_ass"]:
            $ EmmaX.change_face("bemused", 1)
            if EmmaX.love >= EmmaX.obedience and EmmaX.love >= EmmaX.inhibition:
                ch_e "Oh, are we there now?"
            elif EmmaX.obedience >= EmmaX.inhibition:
                ch_e "Is that what gets you off?"
            else:
                $ EmmaX.eyes = "sexy"
                ch_e "Hm, I didn't know that's what you were into."
        else:
            $ EmmaX.change_face("bemused")
            ch_e "Not now, [EmmaX.player_petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no_lick ass" in EmmaX.daily_history:
                $ EmmaX.change_face("bemused")
                ch_e "I appreciate your restraint, [EmmaX.player_petname]."
                return
            "I'm sure I can convince you later. . ." if "no_lick ass" not in EmmaX.daily_history:
                $ EmmaX.change_face("sexy")
                ch_e "Anything's possible, [EmmaX.player_petname]."
                $ EmmaX.change_stat("love", 80, 2)
                $ EmmaX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ EmmaX.recent_history.append("no_taboo")
                    $ EmmaX.daily_history.append("no_taboo")
                $ EmmaX.recent_history.append("no_lick ass")
                $ EmmaX.daily_history.append("no_lick ass")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ EmmaX.change_face("sexy")
                    $ EmmaX.change_stat("obedience", 90, 2)
                    $ EmmaX.change_stat("obedience", 50, 2)
                    ch_e "Ok, you're probably right. . ."
                    $ EmmaX.change_stat("inhibition", 70, 3)
                    $ EmmaX.change_stat("inhibition", 40, 2)
                    jump Emma_LA_Prep
                else:
                    $ EmmaX.change_face("sexy")
                    ch_e "I really don't think so."
            "[[Start licking anyway]":

                $ Approval = ApprovalCheck(EmmaX, 1100, "OI", TabM = 4)
                if Approval > 1 or (Approval and EmmaX.Forced):
                    $ EmmaX.change_face("sad")
                    $ EmmaX.change_stat("love", 70, -5, 1)
                    $ EmmaX.change_stat("love", 200, -2)
                    ch_e "Suit yourself."
                    $ EmmaX.change_stat("obedience", 50, 4)
                    $ EmmaX.change_stat("inhibition", 80, 1)
                    $ EmmaX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ EmmaX.Forced = 1
                    jump Emma_LA_Prep
                else:
                    $ EmmaX.change_stat("love", 200, -15)
                    $ EmmaX.change_face("angry", 1)
                    "She shoves your head back."
                    $ EmmaX.recent_history.append("angry")
                    $ EmmaX.daily_history.append("angry")

    if "no_lick ass" in EmmaX.daily_history:
        ch_e "I don't appreciate having to repeat myself, [EmmaX.player_petname]."
        $ EmmaX.recent_history.append("angry")
        $ EmmaX.daily_history.append("angry")
    elif EmmaX.Forced:
        $ EmmaX.change_face("angry", 1)
        ch_e "I don't think so."
        if ApprovalCheck(EmmaX, 500, "I"):
            $ EmmaX.change_stat("lust", 80, 10)
        else:
            $ EmmaX.change_stat("lust", 50, 3)
        $ EmmaX.change_stat("obedience", 50, -2)
        $ EmmaX.recent_history.append("angry")
        $ EmmaX.daily_history.append("angry")
    elif Taboo:
        $ EmmaX.change_face("angry", 1)
        $ EmmaX.recent_history.append("no_taboo")
        $ EmmaX.daily_history.append("no_taboo")
        ch_e "I have a reputation to maintain."
    elif EmmaX.action_counter["eat_ass"]:
        $ EmmaX.change_face("sad")
        ch_e "Sorry, no more of that."
    else:
        $ EmmaX.change_face("surprised")
        ch_e "I'm sorry, not now."
        $ EmmaX.change_face()
    $ EmmaX.recent_history.append("no_lick ass")
    $ EmmaX.daily_history.append("no_lick ass")
    $ approval_bonus = 0
    return

label Emma_LA_Prep:
    if offhand_action == "eat_ass":
        return
    if not EmmaX.Forced and action_context != "auto":
        $ approval_bonus = 0
        if EmmaX.PantsNum() > 6:
            $ approval_bonus = 15
        call Bottoms_Off (EmmaX)
        if "angry" in EmmaX.recent_history:
            return
    $ approval_bonus = 0
    if EmmaX.pose in ("doggy","sex"):
        call ViewShift (EmmaX, EmmaX.pose, 0, "eat_ass")
    else:
        call ViewShift (EmmaX, "pussy", 0, "eat_ass")
    if not EmmaX.action_counter["eat_ass"]:
        if EmmaX.Forced:
            $ EmmaX.change_stat("love", 90, -30)
            $ EmmaX.change_stat("obedience", 70, 40)
            $ EmmaX.change_stat("inhibition", 80, 80)
        else:
            $ EmmaX.change_stat("love", 90, 35)
            $ EmmaX.change_stat("obedience", 70, 25)
            $ EmmaX.change_stat("inhibition", 80, 55)
    if Taboo:
        $ EmmaX.inhibition += int(Taboo/10)
        $ EmmaX.lust += int(Taboo/5)
    if action_context:
        $ renpy.pop_call()
        $ action_context = 0

    $ EmmaX.Upskirt = 1
    if EmmaX.PantsNum() == 5:
        $ EmmaX.SeenPanties = 1
    call Emma_First_Bottomless (1)
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ EmmaX.DrainWord("no_taboo")
    $ EmmaX.DrainWord("no_lick ass")

    $ EmmaX.recent_history.append("lick") if "lick" not in EmmaX.recent_history else EmmaX.recent_history
    $ EmmaX.recent_history.append("ass") if "ass" not in EmmaX.recent_history else EmmaX.recent_history
    $ EmmaX.recent_history.append("eat_ass")

    $ EmmaX.daily_history.append("lick") if "lick" not in EmmaX.daily_history else EmmaX.recent_history
    $ EmmaX.daily_history.append("ass") if "ass" not in EmmaX.daily_history else EmmaX.recent_history
    $ EmmaX.daily_history.append("eat_ass")

    if EmmaX.pose in ("doggy","sex"):
        call ViewShift (EmmaX, EmmaX.pose, 0, "eat_ass")
    else:
        call ViewShift (EmmaX, "pussy", 0, "eat_ass")

label Emma_LA_Cycle:
    if offhand_action == "kiss":
        $ offhand_action = 0
    while Round > 0:
        call ViewShift (EmmaX, EmmaX.pose, 0, "eat_ass")
        call shift_focus (EmmaX)
        $ EmmaX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (EmmaX)
                    $ counter += 1
                    $ Round -= 1
                    jump Emma_LA_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (EmmaX, "menu")
                    jump Emma_LA_Cycle
                "Other options":

                    menu:
                        "Offhand action":
                            if EmmaX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ EmmaX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (EmmaX, "tired")
                        "Shift primary action":

                            if EmmaX.remaining_actions and multi_action:
                                menu:
                                    "Switch to fondling.":
                                        $ action_context = "pullback"
                                        call Emma_LA_After
                                        call Emma_Fondle_Ass
                                    "I want to stick a finger in.":
                                        $ action_context = "shift"
                                        call Emma_LA_After
                                        call Emma_Insert_Ass
                                    "Just stick a finger in [[without asking].":
                                        $ action_context = "auto"
                                        call Emma_LA_After
                                        call Emma_Insert_Ass
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Emma_LA_After
                                        call Emma_Dildo_Ass
                                    "Never Mind":
                                        jump Emma_LA_Cycle
                            else:
                                call Sex_Basic_Dialog (EmmaX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Emma_LA_After
                            call Offhand_Set
                        "Shift your focus (locked)" if not offhand_action:
                            pass

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Asks [EmmaX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (EmmaX)
                                "Asks [EmmaX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (EmmaX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (EmmaX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Emma_LA_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Emma_LA_Cycle
                                "Never mind":
                                    jump Emma_LA_Cycle

                        "Show her feet" if not ShowFeet and (EmmaX.pose == "doggy" or EmmaX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (EmmaX.pose == "doggy" or EmmaX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [EmmaX.name]":

                            call Girl_Undress (EmmaX)
                        "Clean up [EmmaX.name] (locked)" if not EmmaX.Spunk:
                            pass
                        "Clean up [EmmaX.name]" if EmmaX.Spunk:
                            call Girl_Cleanup (EmmaX, "ask")
                        "Never mind":
                            jump Emma_LA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Emma_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Emma_LA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Emma_Pos_Reset
                    $ Line = 0
                    jump Emma_LA_After


        if EmmaX.underwear or EmmaX.PantsNum() > 6 or EmmaX.HoseNum() >= 5:
            call Girl_Undress (EmmaX, "auto")

        call shift_focus (EmmaX)
        call Sex_Dialog (EmmaX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or EmmaX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (EmmaX)
                if "angry" in EmmaX.recent_history:
                    call Emma_Pos_Reset
                    return
                $ EmmaX.change_stat("lust", 200, 5)
                if 100 > EmmaX.lust >= 70 and EmmaX.session_orgasms < 2:
                    $ EmmaX.recent_history.append("unsatisfied")
                    $ EmmaX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Emma_LA_After
                $ Line = "came"

            if EmmaX.lust >= 100:

                call Girl_Cumming (EmmaX)
                if action_context == "shift" or "angry" in EmmaX.recent_history:
                    jump Emma_LA_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in EmmaX.recent_history:
                    "[EmmaX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Emma_LA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif counter == (5 + EmmaX.action_counter["eat_ass"]):
            $ EmmaX.brows = "confused"
            ch_e "You certainly are enthusiastic. . ."
        elif EmmaX.lust >= 80:
            pass
        elif counter == (15 + EmmaX.action_counter["eat_ass"]) and EmmaX.SEXP >= 15 and not ApprovalCheck(EmmaX, 1500):
            $ EmmaX.brows = "confused"
            menu:
                ch_e "[EmmaX.player_petname], this is getting weird, maybe we could try something else."
                "Finish up.":
                    "You let go. . ."
                    jump Emma_LA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Emma_LA_After
                "No, this is fun.":
                    if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):
                        $ EmmaX.change_stat("love", 200, -5)
                        $ EmmaX.change_stat("obedience", 50, 3)
                        $ EmmaX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ EmmaX.change_face("angry", 1)
                        call Emma_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_e "Well perhaps you are enjoying yourself, but I'm tired of this."
                        $ EmmaX.change_stat("love", 50, -3, 1)
                        $ EmmaX.change_stat("love", 80, -4, 1)
                        $ EmmaX.change_stat("obedience", 30, -1, 1)
                        $ EmmaX.change_stat("obedience", 50, -1, 1)
                        $ EmmaX.recent_history.append("angry")
                        $ EmmaX.daily_history.append("angry")
                        jump Emma_LA_After


        call Escalation (EmmaX)

        if Round == 10:
            ch_e "It's getting late. . ."
        elif Round == 5:
            ch_e "We should take a break soon."


    $ EmmaX.change_face("bemused", 0)
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."

label Emma_LA_After:
    if not action_context:
        call Emma_Pos_Reset

    $ EmmaX.change_face("sexy")

    $ EmmaX.action_counter["eat_ass"] += 1
    $ EmmaX.remaining_actions -=1
    if EmmaX.PantsNum() <= 6 or EmmaX.Upskirt:
        $ EmmaX.addiction_rate += 1
        if "addictive" in Player.Traits:
            $ EmmaX.addiction_rate += 1

    call Partner_Like (EmmaX, 2)

    if EmmaX.action_counter["eat_ass"] == 1:
        $ EmmaX.SEXP += 15
        if not action_context:
            if EmmaX.love >= 500 and "unsatisfied" not in EmmaX.recent_history:
                ch_e "That was. . . invigorating."
            elif EmmaX.obedience <= 500 and Player.focus <= 20:
                $ EmmaX.change_face("perplexed", 1)
                ch_e "Was it all you dreamed of?"

    $ approval_bonus = 0


    call Checkout
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
