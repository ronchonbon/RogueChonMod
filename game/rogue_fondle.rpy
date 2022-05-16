
label Rogue_Fondle:
    $ RogueX.mouth = "smile"
    if not RogueX.remaining_actions:
        ch_r "I'm a bit worn out right now, [RogueX.player_petname], maybe later."
        return
    menu:
        ch_r "Well where exactly were you interested in touching, [RogueX.player_petname]?"
        "Your breasts?" if RogueX.remaining_actions:
            jump Rogue_Fondle_Breasts
        "Suck your breasts?" if RogueX.remaining_actions and RogueX.action_counter["suck_breasts"]:
            jump Rogue_Suck_Breasts
        "Your thighs?" if RogueX.remaining_actions:
            jump Rogue_Fondle_Thighs
        "Your pussy?" if RogueX.remaining_actions:
            jump Rogue_Fondle_Pussy
        "Lick your pussy?" if RogueX.remaining_actions and RogueX.action_counter["eat_pussy"]:
            jump Rogue_Lick_Pussy
        "Your Ass?" if RogueX.remaining_actions:
            jump Rogue_Fondle_Ass
        "Never mind.":
            return
    return



label Rogue_Fondle_Breasts:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (RogueX)


    if RogueX.action_counter["fondle_breasts"]:
        $ approval_bonus += 15
    if RogueX.lust > 75:
        $ approval_bonus += 20
    if "exhibitionist" in RogueX.Traits:
        $ approval_bonus += (3*Taboo)
    if RogueX in Player.Harem or "sex friend" in RogueX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in RogueX.Traits:
        $ approval_bonus -= 20
    if RogueX.event_counter["forced"] and not RogueX.Forced:
        $ approval_bonus -= 5*RogueX.event_counter["forced"]

    if Taboo and "no_taboo" in RogueX.daily_history:
        $ approval_bonus -= 10

    if "no_fondle breasts" in RogueX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle breasts" in RogueX.recent_history else 0

    $ Approval = ApprovalCheck(RogueX, 950, TabM = 3)

    if action_context == "auto":
        if Approval:
            $ RogueX.change_face("sexy")
            $ RogueX.change_stat("obedience", 90, 1)
            $ RogueX.change_stat("obedience", 70, 2)
            $ RogueX.change_stat("inhibition", 70, 3)
            $ RogueX.change_stat("inhibition", 30, 2)
            "As you cup her breast, [RogueX.name] gently nods."
            jump Rogue_FB_Prep
        else:
            $ RogueX.change_face("surprised")
            $ RogueX.brows = "confused"
            $ RogueX.change_stat("obedience", 50, -2)
            ch_r "Ah, ah, Just keep doing what you were doing, [RogueX.player_petname]."
            $ approval_bonus = 0
            $ offhand_action = 0
            return



    if Approval:
        $ RogueX.change_face("sexy", 1)
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
        elif not Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "I guess this is private enough. . ."

    if "fondle_breasts" in RogueX.recent_history:
        $ RogueX.change_face("sexy", 1)
        ch_r "Mmm, again? Ok."
        jump Rogue_FB_Prep
    elif "fondle_breasts" in RogueX.daily_history:
        $ RogueX.change_face("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Maybe not so hard this time though.",
            "Mmm. . ."])
        ch_r "[Line]"

    if Approval >= 2:
        $ RogueX.change_face("bemused", 1)
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
            $ RogueX.change_stat("obedience", 90, 1)
            $ RogueX.change_stat("inhibition", 60, 1)
        ch_r "Ok [RogueX.player_petname], come and get'em."
        $ RogueX.change_stat("love", 90, 1)
        $ RogueX.change_stat("inhibition", 50, 3)
        jump Rogue_FB_Prep
    else:

        $ RogueX.change_face("angry", 1)
        if "no_fondle breasts" in RogueX.recent_history:
            ch_r "I {i}just{/i} told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history and "no_fondle breasts" in RogueX.daily_history:
            ch_r "I told you not to touch me like that in public!"
        elif "no_fondle breasts" in RogueX.daily_history:
            ch_r "I already told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "I told you not in public!"
        elif not RogueX.action_counter["fondle_breasts"]:
            $ RogueX.change_face("bemused")
            ch_r "I just don't think I'm ready yet, [RogueX.player_petname]. . ."
        else:
            $ RogueX.change_face("bemused")
            ch_r "I'd really rather not."
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle breasts" in RogueX.daily_history:
                $ RogueX.change_face("bemused")
                ch_r "Ok, no problem, [RogueX.player_petname]."
                return
            "Maybe later?" if "no_fondle breasts" not in RogueX.daily_history:
                $ RogueX.change_face("sexy")
                "She re-adjusts her cleavage."
                ch_r "I'll give it some thought, [RogueX.player_petname]."
                $ RogueX.change_stat("love", 80, 1)
                $ RogueX.change_stat("love", 50, 1)
                $ RogueX.change_stat("inhibition", 30, 2)
                if Taboo:
                    $ RogueX.AddWord(1,"no_taboo","no_taboo")
                $ RogueX.recent_history.append("no_fondle breasts")
                $ RogueX.daily_history.append("no_fondle breasts")
                return
            "Come on, Please?":
                if Approval:
                    $ RogueX.change_face("sexy")
                    $ RogueX.change_stat("obedience", 90, 1)
                    $ RogueX.change_stat("obedience", 50, 2)
                    $ RogueX.change_stat("inhibition", 60, 3)
                    $ RogueX.change_stat("inhibition", 30, 2)
                    ch_r "Heh, I suppose I can hardly refuse ya when you use the magic words . . ."
                    jump Rogue_FB_Prep
                else:
                    $ RogueX.change_face("sexy")
                    ch_r "I'm afraid not this time, sorry [RogueX.player_petname]."
            "[[Grab her chest anyway]":


                $ Approval = ApprovalCheck(RogueX, 350, "OI", TabM = 3)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.change_face("sad")
                    $ RogueX.change_stat("love", 70, -5, 1)
                    $ RogueX.change_stat("love", 20, -2, 1)
                    ch_r "Fine, if that's what you want."
                    $ RogueX.change_stat("obedience", 90, 2)
                    $ RogueX.change_stat("obedience", 50, 4)
                    $ RogueX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ RogueX.Forced = 1
                    jump Rogue_FB_Prep
                else:
                    $ RogueX.change_stat("love", 200, -10)
                    $ RogueX.change_face("angry", 1)
                    "She slaps your hand away."
                    $ RogueX.AddWord(1,"angry","angry")

    if "no_fondle breasts" in RogueX.daily_history:
        ch_r "Learn to take \"no\" for an answer, [RogueX.player_petname]."
        $ RogueX.AddWord(1,"angry","angry")
    elif RogueX.Forced:
        $ RogueX.change_face("angry", 1)
        ch_r "I don't want you touching me."
        $ RogueX.change_stat("lust", 60, 5)
        $ RogueX.change_stat("obedience", 50, -2)
        $ RogueX.AddWord(1,"angry","angry")
    elif Taboo:
        $ RogueX.change_face("angry", 1)
        $ RogueX.AddWord(1,"no_taboo","no_taboo")
        ch_r "I really don't think this is the right place for that!"
    elif RogueX.action_counter["fondle_breasts"]:
        $ RogueX.change_face("sad")
        ch_r "Sorry, [RogueX.player_petname], you aren't touching these again."
    else:
        $ RogueX.change_face("sexy")
        $ RogueX.mouth = "sad"
        ch_r "Not hap'nin."
    $ RogueX.recent_history.append("no_fondle breasts")
    $ RogueX.daily_history.append("no_fondle breasts")
    $ approval_bonus = 0
    return


label Rogue_FB_Prep:
    if primary_action == "kiss":
        $ primary_action = "fondle_breasts"
        return

    if offhand_action == "fondle_breasts":
        return

    call Rogue_Breasts_Launch ("fondle_breasts")

    if action_context == RogueX:

        $ action_context = 0
        if (RogueX.top or RogueX.bra) and not RogueX.Uptop:

            if ApprovalCheck(RogueX, 1250, TabM = 1) or (RogueX.SeenChest and ApprovalCheck(RogueX, 500) and not Taboo):
                $ RogueX.Uptop = 1
                $ Line = RogueX.top if RogueX.top else RogueX.bra
                "With a miscevious grin, [RogueX.name] pulls her [Line] up over her breasts."
                call Rogue_First_Topless (1)
                $ Line = 0
                "She then grabs your arm and shoves your hand against her breast, clearly intending you to get to work."
            else:
                "[RogueX.name] grabs your arm and shoves your hand against her covered breast, clearly intending you to get to work."
        else:
            "[RogueX.name] grabs your arm and shoves your hand against her breast, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ RogueX.change_stat("inhibition", 80, 3)
                $ RogueX.change_stat("inhibition", 50, 2)
                "You start to fondle it."
            "Praise her.":
                $ RogueX.change_face("sexy", 1)
                $ RogueX.change_stat("inhibition", 80, 3)
                ch_p "I like the initiative, [RogueX.petname]."
                $ RogueX.nameCheck()
                "You start to fondle it."
                $ RogueX.change_stat("love", 85, 1)
                $ RogueX.change_stat("obedience", 90, 1)
                $ RogueX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your hand back."
                $ RogueX.change_face("surprised")
                $ RogueX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [RogueX.petname]."
                $ RogueX.nameCheck()
                "[RogueX.name] pulls back."
                $ RogueX.change_stat("obedience", 90, 1)
                $ RogueX.change_stat("obedience", 50, 1)
                $ RogueX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ RogueX.AddWord(1,"refused","refused")
                return


    if not RogueX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Top_Off (RogueX)
        if "angry" in RogueX.recent_history:
            return

    $ approval_bonus = 0
    if not RogueX.action_counter["fondle_breasts"]:
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -20)
            $ RogueX.change_stat("obedience", 70, 25)
            $ RogueX.change_stat("inhibition", 80, 15)
        else:
            $ RogueX.change_stat("love", 90, 10)
            $ RogueX.change_stat("obedience", 70, 5)
            $ RogueX.change_stat("inhibition", 80, 15)

    if Taboo:
        $ RogueX.inhibition += int(Taboo/10)
        $ RogueX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ RogueX.DrainWord("no_taboo")
    $ RogueX.DrainWord("no_fondle breasts")
    $ RogueX.AddWord(0,"fondle_breasts","fondle_breasts")
    call Rogue_Breasts_Launch ("fondle_breasts")

label Rogue_FB_Cycle:
    while Round > 0:
        call ViewShift (RogueX, RogueX.pose, 0, "fondle_breasts")
        call shift_focus (RogueX)
        $ RogueX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (RogueX)
                    $ counter += 1
                    $ Round -= 1
                    jump Rogue_FB_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (RogueX, "menu")
                    jump Rogue_FB_Cycle
                "Other options":

                    menu:
                        "Offhand action":
                            if RogueX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ RogueX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (RogueX, "tired")
                        "Shift primary action":

                            if RogueX.remaining_actions and multi_action:
                                menu:
                                    "Ask to suck on them.":
                                        if RogueX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Rogue_FB_After
                                            call Rogue_Suck_Breasts
                                        else:
                                            call Sex_Basic_Dialog (RogueX, "tired")
                                    "Just suck on them without asking.":
                                        if RogueX.remaining_actions and multi_action:
                                            $ action_context = "auto"
                                            call Rogue_FB_After
                                            call Rogue_Suck_Breasts
                                        else:
                                            "As you lean in to suck on her breast, she grabs your head and pushes back."
                                            call Sex_Basic_Dialog (RogueX, "tired")
                                    "Never Mind":
                                        jump Rogue_FB_Cycle
                            else:
                                call Sex_Basic_Dialog (RogueX, "tired")

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [RogueX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (RogueX)
                                "Ask [RogueX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (RogueX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (RogueX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Rogue_FB_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Rogue_FB_Cycle
                                "Never mind":
                                    jump Rogue_FB_Cycle

                        "Show her feet" if not ShowFeet and (RogueX.pose == "doggy" or RogueX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (RogueX.pose == "doggy" or RogueX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [RogueX.name]":

                            call Girl_Undress (RogueX)
                        "Clean up [RogueX.name] (locked)" if not RogueX.Spunk:
                            pass
                        "Clean up [RogueX.name]" if RogueX.Spunk:
                            call Girl_Cleanup (RogueX, "ask")
                        "Never mind":
                            jump Rogue_FB_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Rogue_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Rogue_FB_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Rogue_Pos_Reset
                    $ Line = 0
                    jump Rogue_FB_After


        call shift_focus (RogueX)
        call Sex_Dialog (RogueX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or RogueX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (RogueX)
                if "angry" in RogueX.recent_history:
                    call Rogue_Pos_Reset
                    return
                $ RogueX.change_stat("lust", 200, 5)
                if 100 > RogueX.lust >= 70 and RogueX.session_orgasms < 2 and RogueX.SEXP >= 20:
                    $ RogueX.AddWord(0,"unsatisfied","unsatisfied")
                if Player.focus > 80:
                    jump Rogue_FB_After
                $ Line = "came"

            if RogueX.lust >= 100:

                call Girl_Cumming (RogueX)
                if action_context == "shift" or "angry" in RogueX.recent_history:
                    jump Rogue_FB_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in RogueX.recent_history:
                    "[RogueX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Rogue_FB_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif counter == (5 + RogueX.action_counter["fondle_breasts"]):
            $ RogueX.brows = "confused"
            ch_r "You're just going at them, huh?"
        elif RogueX.lust >= 85:
            pass
        elif counter == (15 + RogueX.action_counter["fondle_breasts"]) and RogueX.SEXP >= 15 and not ApprovalCheck(RogueX, 1500):
            $ RogueX.brows = "confused"
            menu:
                ch_r "I know you're having fun, but maybe we could try something else [RogueX.player_petname]."
                "Finish up.":
                    "You let go. . ."
                    jump Rogue_FB_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Rogue_FB_After
                "No, this is fun.":
                    if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):
                        $ RogueX.change_stat("love", 200, -5)
                        $ RogueX.change_stat("obedience", 50, 3)
                        $ RogueX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ RogueX.change_face("angry", 1)
                        call Rogue_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_r "Well if that's your attitude, I don't need your \"help\"."
                        $ RogueX.change_stat("love", 50, -3, 1)
                        $ RogueX.change_stat("love", 80, -4, 1)
                        $ RogueX.change_stat("obedience", 30, -1, 1)
                        $ RogueX.change_stat("obedience", 50, -1, 1)
                        $ RogueX.AddWord(1,"angry","angry")
                        jump Rogue_FB_After


        call Escalation (RogueX)

        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."

        if RogueX.lust >= 50 and not RogueX.Uptop and (RogueX.bra or RogueX.top):
            $ RogueX.Uptop = 1
            "[RogueX.name] shrugs and pulls her top open."
            call Rogue_First_Topless


    $ RogueX.change_face("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.player_petname], that's enough of that for now."

label Rogue_FB_After:
    if not action_context:
        call Rogue_Pos_Reset

    $ RogueX.change_face("sexy")

    $ RogueX.action_counter["fondle_breasts"]+= 1
    $ RogueX.remaining_actions -=1
    $ RogueX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ RogueX.addiction_rate += 1

    call Partner_Like (RogueX, 2)

    if RogueX.action_counter["fondle_breasts"]== 1:
        $ RogueX.SEXP += 4
        if not action_context:
            if RogueX.love >= 500 and "unsatisfied" not in RogueX.recent_history:
                ch_r "That was . . . real pleasant, [RogueX.player_petname]."
            elif RogueX.obedience <= 500 and Player.focus <= 20:
                $ RogueX.change_face("perplexed", 1)
                ch_r "Did you get your jollies?"

    $ approval_bonus = 0
    call checkout
    return






label Rogue_Suck_Breasts:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (RogueX)

    if RogueX.action_counter["suck_breasts"]:
        $ approval_bonus += 15
    if not RogueX.bra and not RogueX.top:
        $ approval_bonus += 15
    if RogueX.lust > 75:
        $ approval_bonus += 20
    if RogueX.lust > 75 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in RogueX.Traits:
        $ approval_bonus += (4*Taboo)
    if RogueX in Player.Harem or "sex friend" in RogueX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in RogueX.Traits:
        $ approval_bonus -= 25
    if RogueX.event_counter["forced"] and not RogueX.Forced:
        $ approval_bonus -= 5*RogueX.event_counter["forced"]

    if Taboo and "no_taboo" in RogueX.daily_history:
        $ approval_bonus -= 10

    if "no_suck breasts" in RogueX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_suck breasts" in RogueX.recent_history else 0

    $ Approval = ApprovalCheck(RogueX, 1050, TabM = 4)

    if action_context == "auto":
        if Approval:
            $ RogueX.change_face("sexy")
            $ RogueX.change_stat("obedience", 90, 1)
            $ RogueX.change_stat("obedience", 70, 2)
            $ RogueX.change_stat("inhibition", 70, 3)
            $ RogueX.change_stat("inhibition", 30, 2)
            "As you dive in, [RogueX.name] seems a bit surprised, but just makes a little \"coo.\""
            jump Rogue_SB_Prep
        else:
            $ RogueX.change_face("surprised")
            $ RogueX.change_stat("obedience", 50, -2)
            ch_r "Hey, just keep doing what you were doing, [RogueX.player_petname]."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "suck_breasts" in RogueX.recent_history:
        $ RogueX.change_face("sexy", 1)
        ch_r "Mmm, again? Ok."
        jump Rogue_SB_Prep
    elif "suck_breasts" in RogueX.daily_history:
        $ RogueX.change_face("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Maybe not so hard this time though.",
            "Mmm. . ."])
        ch_r "[Line]"

    if Approval >= 2:
        $ RogueX.change_face("bemused", 1)
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
            $ RogueX.change_stat("obedience", 90, 1)
            $ RogueX.change_stat("inhibition", 60, 1)
        ch_r "Ok [RogueX.player_petname], come and get'em."
        $ RogueX.change_stat("love", 90, 1)
        $ RogueX.change_stat("inhibition", 50, 3)
        jump Rogue_SB_Prep
    else:

        $ RogueX.change_face("angry", 1)
        if "no_suck breasts" in RogueX.recent_history:
            ch_r "I {i}just{/i} told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history and "no_suck breasts" in RogueX.daily_history:
            ch_r "I told you we can't do that in public!"
        elif "no_suck breasts" in RogueX.daily_history:
            ch_r "I already told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "I told you not in public!"
        elif not RogueX.action_counter["suck_breasts"]:
            $ RogueX.change_face("bemused")
            ch_r "I just don't think I'm ready yet, [RogueX.player_petname]. . ."
        else:
            $ RogueX.change_face("bemused")
            ch_r "I'd really rather not."
        menu:
            extend ""
            "Sorry, never mind." if "no_suck breasts" in RogueX.daily_history:
                $ RogueX.change_face("bemused")
                ch_r "Yeah, fine, [RogueX.player_petname]."
                return
            "Maybe later?" if "no_suck breasts" not in RogueX.daily_history:
                $ RogueX.change_face("sexy")
                ch_r "I'll give it some thought, [RogueX.player_petname]."
                $ RogueX.change_stat("love", 80, 1)
                $ RogueX.change_stat("love", 50, 1)
                $ RogueX.change_stat("inhibition", 30, 2)
                if Taboo:
                    $ RogueX.AddWord(1,"no_taboo","no_taboo")
                $ RogueX.recent_history.append("no_suck breasts")
                $ RogueX.daily_history.append("no_suck breasts")
                return
            "Come on, Please?":
                if Approval:
                    $ RogueX.change_face("sexy")
                    $ RogueX.change_stat("obedience", 90, 1)
                    $ RogueX.change_stat("obedience", 50, 2)
                    $ RogueX.change_stat("inhibition", 60, 3)
                    $ RogueX.change_stat("inhibition", 30, 2)
                    ch_r "You better work your mouth that hard on these."
                    jump Rogue_SB_Prep
                else:
                    $ RogueX.change_face("sexy")
                    ch_r "I'm afraid not this time, sorry [RogueX.player_petname]."
            "[[Start sucking anyway]":

                $ Approval = ApprovalCheck(RogueX, 450, "OI", TabM = 3)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.change_face("sad")
                    $ RogueX.change_stat("love", 70, -5, 1)
                    $ RogueX.change_stat("love", 20, -2, 1)
                    ch_r "Hmmph, well I guess you can go to town. . ."
                    $ RogueX.change_stat("obedience", 90, 2)
                    $ RogueX.change_stat("obedience", 50, 4)
                    $ RogueX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ RogueX.Forced = 1
                    jump Rogue_SB_Prep
                else:
                    $ RogueX.change_stat("love", 200, -10)
                    $ RogueX.change_face("angry", 1)
                    "She shoves your head back out."
                    $ RogueX.AddWord(1,"angry","angry")

    if "no_suck breasts" in RogueX.daily_history:
        ch_r "Learn to take \"no\" for an answer, [RogueX.player_petname]."
        $ RogueX.AddWord(1,"angry","angry")
    elif RogueX.Forced:
        $ RogueX.change_face("angry", 1)
        ch_r "I don't want your lips on me."
        $ RogueX.change_stat("lust", 60, 5)
        $ RogueX.change_stat("obedience", 50, -2)
        $ RogueX.AddWord(1,"angry","angry")
    elif Taboo:
        $ RogueX.change_face("angry", 1)
        $ RogueX.AddWord(1,"no_taboo","no_taboo")
        ch_r "I really don't think this is the right place for that!"
    elif RogueX.action_counter["suck_breasts"]:
        $ RogueX.change_face("sad")
        ch_r "Sorry, [RogueX.player_petname], you aren't getting these in your mouth."
    else:
        $ RogueX.change_face("sexy")
        $ RogueX.mouth = "sad"
        ch_r "Not hap'nin, [RogueX.player_petname]."
    $ RogueX.recent_history.append("no_suck breasts")
    $ RogueX.daily_history.append("no_suck breasts")
    $ approval_bonus = 0
    return


ch_r "Sorry, I don't even know how I got here. . ."
return

label Rogue_SB_Prep:

    if offhand_action == "suck_breasts":
        return

    call Rogue_Breasts_Launch ("suck_breasts")

    if action_context == RogueX:

        $ action_context = 0
        if (RogueX.top or RogueX.bra) and not RogueX.Uptop:

            if ApprovalCheck(RogueX, 1250, TabM = 1) or (RogueX.SeenChest and ApprovalCheck(RogueX, 500) and not Taboo):
                $ RogueX.Uptop = 1
                $ Line = RogueX.top if RogueX.top else RogueX.bra
                "With a miscevious grin, [RogueX.name] pulls her [Line] up over her breasts."
                call Rogue_First_Topless (1)
                $ Line = 0
                "She then grabs your head and shoves your face into her chest, clearly intending you to get to work."
            else:
                "[RogueX.name] grabs your head and shoves your face into her chest, clearly intending you to get to work."
        else:
            "[RogueX.name] grabs your head and shoves your face into her chest, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ RogueX.change_stat("inhibition", 80, 3)
                $ RogueX.change_stat("inhibition", 50, 2)
                "You start to run your tongue along her nipple."
            "Praise her.":
                $ RogueX.change_face("sexy", 1)
                $ RogueX.change_stat("inhibition", 80, 3)
                ch_p "Mmm, I like this, [RogueX.petname]."
                $ RogueX.nameCheck()
                "You start to fondle it."
                $ RogueX.change_stat("love", 85, 1)
                $ RogueX.change_stat("obedience", 90, 1)
                $ RogueX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your head back."
                $ RogueX.change_face("surprised")
                $ RogueX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [RogueX.petname]."
                $ RogueX.nameCheck()
                "[RogueX.name] pulls away."
                $ RogueX.change_stat("obedience", 90, 1)
                $ RogueX.change_stat("obedience", 50, 1)
                $ RogueX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ RogueX.AddWord(1,"refused","refused")
                return


    if not RogueX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Top_Off (RogueX)
        if "angry" in RogueX.recent_history:
            return

    $ approval_bonus = 0
    if not RogueX.action_counter["suck_breasts"]:
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -25)
            $ RogueX.change_stat("obedience", 70, 25)
            $ RogueX.change_stat("inhibition", 80, 17)
        else:
            $ RogueX.change_stat("love", 90, 10)
            $ RogueX.change_stat("obedience", 70, 10)
            $ RogueX.change_stat("inhibition", 80, 15)

    if Taboo:
        $ RogueX.inhibition += int(Taboo/10)
        $ RogueX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ RogueX.DrainWord("no_taboo")
    $ RogueX.DrainWord("no_suck breasts")
    $ RogueX.AddWord(0,"suck_breasts","suck_breasts")
    call Rogue_Breasts_Launch ("suck_breasts")

label Rogue_SB_Cycle:
    if offhand_action == "kiss":
        $ offhand_action = 0
    while Round > 0:
        call ViewShift (RogueX, RogueX.pose, 0, "suck_breasts")
        call shift_focus (RogueX)
        $ RogueX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (RogueX)
                    $ counter += 1
                    $ Round -= 1
                    jump Rogue_SB_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (RogueX, "menu")
                    jump Rogue_SB_Cycle
                "Other options":

                    menu:
                        "Offhand action":
                            if RogueX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ RogueX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (RogueX, "tired")
                        "Shift primary action":

                            if RogueX.remaining_actions and multi_action:
                                menu:
                                    "Pull back to fondling.":
                                        if RogueX.remaining_actions and multi_action:
                                            $ action_context = "pullback"
                                            call Rogue_SB_After
                                            call Rogue_Fondle_Breasts
                                        else:
                                            "As you pull back, [RogueX.name] pushes you back in close."
                                            call Sex_Basic_Dialog (RogueX, "tired")
                                    "Never Mind":
                                        jump Rogue_SB_Cycle
                            else:
                                call Sex_Basic_Dialog (RogueX, "tired")

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [RogueX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (RogueX)
                                "Ask [RogueX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (RogueX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (RogueX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Rogue_SB_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Rogue_SB_Cycle
                                "Never mind":
                                    jump Rogue_SB_Cycle

                        "Show her feet" if not ShowFeet and (RogueX.pose == "doggy" or RogueX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (RogueX.pose == "doggy" or RogueX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [RogueX.name]":

                            call Girl_Undress (RogueX)
                        "Clean up [RogueX.name] (locked)" if not RogueX.Spunk:
                            pass
                        "Clean up [RogueX.name]" if RogueX.Spunk:
                            call Girl_Cleanup (RogueX, "ask")
                        "Never mind":
                            jump Rogue_SB_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Rogue_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Rogue_SB_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Rogue_Pos_Reset
                    $ Line = 0
                    jump Rogue_SB_After


        call shift_focus (RogueX)
        call Sex_Dialog (RogueX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or RogueX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (RogueX)
                if "angry" in RogueX.recent_history:
                    call Rogue_Pos_Reset
                    return
                $ RogueX.change_stat("lust", 200, 5)
                if 100 > RogueX.lust >= 70 and RogueX.session_orgasms < 2:
                    $ RogueX.AddWord(0,"unsatisfied","unsatisfied")

                if Player.focus > 80:
                    jump Rogue_SB_After
                $ Line = "came"

            if RogueX.lust >= 100:

                call Girl_Cumming (RogueX)
                if action_context == "shift" or "angry" in RogueX.recent_history:
                    jump Rogue_SB_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."

                if "unsatisfied" in RogueX.recent_history:
                    "[RogueX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Rogue_SB_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif counter == (5 + RogueX.action_counter["suck_breasts"]):
            $ RogueX.brows = "confused"
            ch_r "You're just going at them, huh?"
        elif RogueX.lust >= 85:
            pass
        elif counter == (15 + RogueX.action_counter["suck_breasts"]) and RogueX.SEXP >= 15 and not ApprovalCheck(RogueX, 1500):
            $ RogueX.brows = "confused"
            menu:
                ch_r "I know you're having fun, but maybe we could try something else [RogueX.player_petname]."
                "Finish up.":
                    "You let go. . ."
                    jump Rogue_SB_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Rogue_SB_After
                "No, this is fun.":
                    if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):
                        $ RogueX.change_stat("love", 200, -5)
                        $ RogueX.change_stat("obedience", 50, 3)
                        $ RogueX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ RogueX.change_face("angry", 1)
                        call Rogue_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_r "Well if that's your attitude, I don't need your \"help\"."
                        $ RogueX.change_stat("love", 50, -3, 1)
                        $ RogueX.change_stat("love", 80, -4, 1)
                        $ RogueX.change_stat("obedience", 30, -1, 1)
                        $ RogueX.change_stat("obedience", 50, -1, 1)
                        $ RogueX.AddWord(1,"angry","angry")
                        jump Rogue_SB_After


        call Escalation (RogueX)

        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."

        if RogueX.lust >= 50 and not RogueX.Uptop and (RogueX.bra or RogueX.top):
            $ RogueX.Uptop = 1
            "Rogue shrugs and pulls her top open."
            call Rogue_First_Topless


    $ RogueX.change_face("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.player_petname], that's enough of that for now."


label Rogue_SB_After:
    if not action_context:
        call Rogue_Pos_Reset

    $ RogueX.change_face("sexy")

    $ RogueX.action_counter["suck_breasts"] += 1
    $ RogueX.remaining_actions -=1
    $ RogueX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ RogueX.addiction_rate += 1

    call Partner_Like (RogueX, 2)

    if RogueX.action_counter["suck_breasts"] == 1:
        $ RogueX.SEXP += 4
        if not action_context:
            if RogueX.love >= 500 and "unsatisfied" not in RogueX.recent_history:
                ch_r "I . . . really liked that, [RogueX.player_petname]."
            elif RogueX.obedience <= 500 and Player.focus <= 20:
                $ RogueX.change_face("perplexed", 1)
                ch_r "Did you like the taste?"

    $ approval_bonus = 0
    call checkout
    return





label Rogue_Fondle_Thighs:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (RogueX)

    if RogueX.action_counter["fondle_thighs"]:
        $ approval_bonus += 10
    if RogueX.PantsNum() >= 6 or RogueX.HoseNum() >= 5:
        $ approval_bonus -= 5
    if RogueX.lust > 75:
        $ approval_bonus += 10
    if "exhibitionist" in RogueX.Traits:
        $ approval_bonus += Taboo
    if RogueX in Player.Harem or "sex friend" in RogueX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in RogueX.Traits:
        $ approval_bonus -= 25
    if RogueX.event_counter["forced"] and not RogueX.Forced:
        $ approval_bonus -= 5*RogueX.event_counter["forced"]

    if Taboo and "no_taboo" in RogueX.daily_history:
        $ approval_bonus -= 10

    if "no_fondle thighs" in RogueX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle thighs" in RogueX.recent_history else 0

    $ Approval = ApprovalCheck(RogueX, 750, TabM=1)

    if action_context == "auto":
        if Approval:
            $ RogueX.change_face("sexy")
            $ RogueX.change_stat("obedience", 50, 1)
            $ RogueX.change_stat("inhibition", 30, 2)
            "As you caress her thigh, Rogue glances at you, and smiles."
            jump Rogue_FT_Prep
        else:
            $ RogueX.change_face("surprised")
            $ RogueX.change_stat("obedience", 50, -2)
            ch_r "Hands off the merchandise, [RogueX.player_petname]."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if action_context == "pullback":
        $ RogueX.change_face("surprised")
        $ RogueX.brows = "sad"
        if RogueX.lust > 60:
            $ RogueX.change_stat("love", 70, -3)
        $ RogueX.change_stat("obedience", 90, 1)
        $ RogueX.change_stat("obedience", 70, 2)
        "As you pull back, Rogue looks a little sad."
        jump Rogue_FT_Prep
    elif "fondle_thighs" in RogueX.recent_history:
        $ RogueX.change_face("sexy", 1)
        ch_r "Mmm, again? Ok."
        jump Rogue_FT_Prep
    elif "fondle_thighs" in RogueX.daily_history:
        $ RogueX.change_face("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "You do have a smooth touch. . .",
            "Mmm. . ."])
        ch_r "[Line]"

    if Approval >= 2:
        $ RogueX.change_face("bemused", 1)
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("obedience", 90, 1)
            $ RogueX.change_stat("inhibition", 60, 1)
        ch_r "Ok [RogueX.player_petname], go ahead."
        $ RogueX.change_stat("love", 90, 1)
        $ RogueX.change_stat("inhibition", 50, 3)
        jump Rogue_FT_Prep
    else:

        $ RogueX.change_face("angry", 1)
        if "no_fondle thighs" in RogueX.recent_history:
            ch_r "I {i}just{/i} told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history and "no_fondle thighs" in RogueX.daily_history:
            ch_r "I told you not to touch me like that in public!"
        elif "no_fondle thighs" in RogueX.daily_history:
            ch_r "I already told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "I told you not in public!"
        elif not RogueX.action_counter["fondle_thighs"]:
            $ RogueX.change_face("bemused")
            ch_r "I just don't think I'm ready yet, [RogueX.player_petname]. . ."
        else:
            $ RogueX.change_face("bemused")
            ch_r "I'd really rather not."
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle thighs" in RogueX.daily_history:
                $ RogueX.change_face("bemused")
                ch_r "Yeah, ok, [RogueX.player_petname]."
                return
            "Maybe later?" if "no_fondle thighs" not in RogueX.daily_history:
                $ RogueX.change_face("sexy")
                ch_r "Heh, maybe, [RogueX.player_petname]."
                $ RogueX.change_stat("love", 80, 1)
                $ RogueX.change_stat("inhibition", 30, 2)
                if Taboo:
                    $ RogueX.AddWord(1,"no_taboo","no_taboo")
                $ RogueX.recent_history.append("no_fondle thighs")
                $ RogueX.daily_history.append("no_fondle thighs")
                return
            "Come on, Please?":
                if Approval:
                    $ RogueX.change_face("sexy")
                    $ RogueX.change_stat("obedience", 60, 1)
                    $ RogueX.change_stat("obedience", 30, 2)
                    $ RogueX.change_stat("inhibition", 50, 1)
                    $ RogueX.change_stat("inhibition", 30, 2)
                    ch_r "Heh, I suppose I can hardly refuse ya when you use the magic words . . ."
                    jump Rogue_FT_Prep
                else:
                    $ RogueX.change_face("sexy")
                    ch_r "I'm afraid not this time, sorry [RogueX.player_petname]."
            "[[Start caressing her thigh anyway]":

                $ Approval = ApprovalCheck(RogueX, 350, "OI", TabM = 2)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.change_face("sad")
                    $ RogueX.change_stat("love", 70, -5, 1)
                    $ RogueX.change_stat("love", 20, -2, 1)
                    ch_r "Hmmph."
                    $ RogueX.change_stat("obedience", 50, 3)
                    $ RogueX.change_stat("inhibition", 60, 2)
                    if Approval < 2:
                        $ RogueX.Forced = 1
                    jump Rogue_FT_Prep
                else:
                    $ RogueX.change_stat("love", 200, -8)
                    $ RogueX.change_face("angry", 1)
                    "She slaps your hand away."
                    $ RogueX.AddWord(1,"angry","angry")

    if "no_fondle thighs" in RogueX.daily_history:
        ch_r "Learn to take \"no\" for an answer, [RogueX.player_petname]."
        $ RogueX.AddWord(1,"angry","angry")
    elif RogueX.Forced:
        $ RogueX.change_face("angry", 1)
        ch_r "Not even that much."
        $ RogueX.change_stat("lust", 50, 2)
        $ RogueX.change_stat("obedience", 50, -1)
        $ RogueX.AddWord(1,"angry","angry")
    elif Taboo:
        $ RogueX.change_face("angry", 1)
        $ RogueX.AddWord(1,"no_taboo","no_taboo")
        ch_r "I really don't think this is the right place for that!"
    elif RogueX.action_counter["fondle_thighs"]:
        $ RogueX.change_face("sad")
        ch_r "Fresh!"
    else:
        $ RogueX.change_face("sexy")
        $ RogueX.mouth = "sad"
        ch_r "No luck, [RogueX.player_petname]."
    $ RogueX.recent_history.append("no_fondle thighs")
    $ RogueX.daily_history.append("no_fondle thighs")
    $ approval_bonus = 0
    return

label Rogue_FT_Prep:
    if primary_action == "kiss":
        $ primary_action = "fondle_thighs"
        return

    if offhand_action == "fondle_thighs":
        return

    if not RogueX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (RogueX)
        if "angry" in RogueX.recent_history:
            return

    $ approval_bonus = 0
    call Rogue_Pussy_Launch ("fondle_thighs")
    if not RogueX.action_counter["fondle_thighs"]:
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -10)
            $ RogueX.change_stat("obedience", 70, 15)
            $ RogueX.change_stat("inhibition", 80, 10)
        else:
            $ RogueX.change_stat("love", 90, 5)
            $ RogueX.change_stat("obedience", 70, 10)
            $ RogueX.change_stat("inhibition", 80, 15)

    if Taboo:
        $ RogueX.change_stat("lust", 200, (int(Taboo/5)))
        $ RogueX.change_stat("inhibition", 200, (2*(int(Taboo/5))))

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ RogueX.DrainWord("no_taboo")
    $ RogueX.DrainWord("no_fondle thighs")
    $ RogueX.AddWord(0,"fondle_thighs","fondle_thighs")
    call Rogue_Pussy_Launch ("fondle_thighs")

label Rogue_FT_Cycle:
    while Round > 0:
        call ViewShift (RogueX, RogueX.pose, 0, "fondle_thighs")
        call shift_focus (RogueX)
        $ RogueX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (RogueX)
                    $ counter += 1
                    $ Round -= 1
                    jump Rogue_FT_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (RogueX, "menu")
                    jump Rogue_FT_Cycle
                "Other options":

                    menu:
                        "Offhand action":
                            if RogueX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ RogueX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (RogueX, "tired")
                        "Shift primary action":

                            if RogueX.remaining_actions and multi_action:
                                menu:
                                    "Can I do a little deeper?":
                                        if RogueX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Rogue_FT_After
                                            call Rogue_Fondle_Pussy
                                        else:
                                            call Sex_Basic_Dialog (RogueX, "tired")
                                    "Shift your hands a bit higher without asking":
                                        if RogueX.remaining_actions and multi_action:
                                            $ action_context = "auto"
                                            call Rogue_FT_After
                                            call Rogue_Fondle_Pussy
                                        else:
                                            "As your hands creep upwards, she grabs your wrists."
                                            call Sex_Basic_Dialog (RogueX, "tired")
                                    "Never Mind":
                                        jump Rogue_FT_Cycle
                            else:
                                call Sex_Basic_Dialog (RogueX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Rogue_FT_After
                            call Offhand_Set
                        "Shift your focus (locked)" if not offhand_action:
                            pass

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [RogueX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (RogueX)
                                "Ask [RogueX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (RogueX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (RogueX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Rogue_FT_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Rogue_FT_Cycle
                                "Never mind":
                                    jump Rogue_FT_Cycle

                        "Show her feet" if not ShowFeet and (RogueX.pose == "doggy" or RogueX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (RogueX.pose == "doggy" or RogueX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [RogueX.name]":

                            call Girl_Undress (RogueX)
                        "Clean up [RogueX.name] (locked)" if not RogueX.Spunk:
                            pass
                        "Clean up [RogueX.name]" if RogueX.Spunk:
                            call Girl_Cleanup (RogueX, "ask")
                        "Never mind":
                            jump Rogue_FT_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Rogue_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Rogue_FT_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Rogue_Pos_Reset
                    $ Line = 0
                    jump Rogue_FT_After


        call shift_focus (RogueX)
        call Sex_Dialog (RogueX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or RogueX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (RogueX)
                if "angry" in RogueX.recent_history:
                    call Rogue_Pos_Reset
                    return
                $ RogueX.change_stat("lust", 200, 5)
                if 100 > RogueX.lust >= 70 and RogueX.session_orgasms < 2 and RogueX.SEXP >= 20:
                    $ RogueX.AddWord(0,"unsatisfied","unsatisfied")

                if Player.focus > 80:
                    jump Rogue_FT_After
                $ Line = "came"

            if RogueX.lust >= 100:

                call Girl_Cumming (RogueX)
                if action_context == "shift" or "angry" in RogueX.recent_history:
                    jump Rogue_FT_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in RogueX.recent_history:
                    "[RogueX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Rogue_FT_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif counter == (5 + RogueX.action_counter["fondle_thighs"]):
            $ RogueX.brows = "confused"
            ch_r "You like how those feel, huh?"
        elif counter == (15 + RogueX.action_counter["fondle_thighs"]) and RogueX.SEXP >= 15 and not ApprovalCheck(RogueX, 1500):
            $ RogueX.brows = "confused"
            menu:
                ch_r "I know you're having fun, but maybe we could try something else [RogueX.player_petname]."
                "Finish up.":
                    "You let go. . ."
                    jump Rogue_FT_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Rogue_FT_After
                "No, this is fun.":
                    if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):
                        $ RogueX.change_stat("love", 200, -5)
                        $ RogueX.change_stat("obedience", 50, 3)
                        $ RogueX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ RogueX.change_face("angry", 1)
                        call Rogue_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_r "Well if that's your attitude, I don't need your \"help\"."
                        $ RogueX.change_stat("love", 50, -3, 1)
                        $ RogueX.change_stat("love", 80, -4, 1)
                        $ RogueX.change_stat("obedience", 30, -1, 1)
                        $ RogueX.change_stat("obedience", 50, -1, 1)
                        $ RogueX.AddWord(1,"angry","angry")
                        jump Rogue_FT_After


        call Escalation (RogueX)

        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."


    $ RogueX.change_face("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.player_petname], that's enough of that for now."


label Rogue_FT_After:
    if not action_context:
        call Rogue_Pos_Reset

    $ RogueX.change_face("sexy")

    $ RogueX.action_counter["fondle_thighs"]+= 1
    $ RogueX.remaining_actions -=1
    if RogueX.PantsNum() < 6 or RogueX.Upskirt:
        $ RogueX.addiction_rate += 1
        if "addictive" in Player.Traits:
            $ RogueX.addiction_rate += 1

        call Partner_Like (RogueX, 1, 0)

    if RogueX.action_counter["fondle_thighs"]== 1:
        $ RogueX.SEXP += 3
        if not action_context:
            if RogueX.love >= 500 and "unsatisfied" not in RogueX.recent_history:
                ch_r "That was. . . nice."
            elif RogueX.obedience <= 500 and Player.focus <= 20:
                $ RogueX.change_face("perplexed", 1)
                ch_r "Was that enough for you?"

    $ approval_bonus = 0
    call checkout
    return


label Rogue_Fondle_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (RogueX)

    if RogueX.action_counter["fondle_pussy"]:
        $ approval_bonus += 20
    if RogueX.PantsNum() >= 6 or RogueX.HoseNum() >= 5:
        $ approval_bonus -= 10
    if RogueX.lust > 75:
        $ approval_bonus += 15
    if RogueX.lust > 75 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in RogueX.Traits:
        $ approval_bonus += (2*Taboo)
    if RogueX in Player.Harem or "sex friend" in RogueX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in RogueX.Traits:
        $ approval_bonus -= 25
    if RogueX.event_counter["forced"] and not RogueX.Forced:
        $ approval_bonus -= 5*RogueX.event_counter["forced"]

    if Taboo and "no_taboo" in RogueX.daily_history:
        $ approval_bonus -= 10

    if "no_fondle pussy" in RogueX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle pussy" in RogueX.recent_history else 0

    $ Approval = ApprovalCheck(RogueX, 1050, TabM = 2)

    if action_context == "auto":
        if Approval:
            $ RogueX.change_face("sexy")
            $ RogueX.change_stat("obedience", 90, 1)
            $ RogueX.change_stat("obedience", 70, 2)
            $ RogueX.change_stat("inhibition", 70, 3)
            $ RogueX.change_stat("inhibition", 30, 2)
            "As your hand creeps up her thigh, [RogueX.name] seems a bit surprised, but then nods."
            jump Rogue_FP_Prep
        else:
            $ RogueX.change_face("surprised")
            $ RogueX.change_stat("obedience", 50, -2)
            ch_r "Hey, just keep doing what you were doing, [RogueX.player_petname]."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if action_context == "pullback":
        $ RogueX.change_face("surprised")
        $ RogueX.brows = "sad"
        if RogueX.lust > 80:
            $ RogueX.change_stat("love", 70, -4)
        $ RogueX.change_stat("obedience", 90, 1)
        $ RogueX.change_stat("obedience", 70, 2)
        "As your hand pulls out, [RogueX.name] gasps and looks upset."
        jump Rogue_FP_Prep
    elif "fondle_pussy" in RogueX.recent_history:
        $ RogueX.change_face("sexy", 1)
        ch_r "Mmm, again? Ok."
        jump Rogue_FP_Prep
    elif "fondle_pussy" in RogueX.daily_history:
        $ RogueX.change_face("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Maybe not so hard this time though.",
            "Take it a bit gently, I'm still quivering from earlier.",
            "Mmm. . ."])
        ch_r "[Line]"

    if Approval >= 2:
        $ RogueX.change_face("bemused", 1)
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
            $ RogueX.change_stat("obedience", 90, 1)
            $ RogueX.change_stat("inhibition", 60, 1)
        ch_r "Sure, get in there."
        $ RogueX.change_stat("love", 90, 1)
        $ RogueX.change_stat("inhibition", 50, 3)
        jump Rogue_FP_Prep
    else:

        $ RogueX.change_face("angry", 1)
        if "no_fondle pussy" in RogueX.recent_history:
            ch_r "I {i}just{/i} told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history and "no_fondle pussy" in RogueX.daily_history:
            ch_r "I told you not to touch me like that in public!"
        elif "no_fondle pussy" in RogueX.daily_history:
            ch_r "I already told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "I told you not in public!"
        elif not RogueX.action_counter["fondle_pussy"]:
            $ RogueX.change_face("bemused")
            ch_r "Um, not down there, [RogueX.player_petname]. . ."
        else:
            $ RogueX.change_face("bemused")
            ch_r "I'd really rather not."
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle pussy" in RogueX.daily_history:
                $ RogueX.change_face("bemused")
                ch_r "Yeah, ok, [RogueX.player_petname]."
                return
            "Maybe later?" if "no_fondle pussy" not in RogueX.daily_history:
                $ RogueX.change_face("sexy")
                ch_r "I'll give it some thought, [RogueX.player_petname]."
                $ RogueX.change_stat("love", 80, 2)
                $ RogueX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ RogueX.AddWord(1,"no_taboo","no_taboo")
                $ RogueX.recent_history.append("no_fondle pussy")
                $ RogueX.daily_history.append("no_fondle pussy")
                return
            "Come on, Please?":
                if Approval:
                    $ RogueX.change_face("sexy")
                    $ RogueX.change_stat("obedience", 90, 2)
                    $ RogueX.change_stat("obedience", 50, 2)
                    $ RogueX.change_stat("inhibition", 70, 3)
                    $ RogueX.change_stat("inhibition", 40, 2)
                    ch_r "Well, if you're gonna beg. . ."
                    jump Rogue_FP_Prep
                else:
                    $ RogueX.change_face("sexy")
                    ch_r "Tsk, not this time, [RogueX.player_petname]."
            "[[Start fondling anyway]":

                $ Approval = ApprovalCheck(RogueX, 450, "OI", TabM = 2)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.change_face("sad")
                    $ RogueX.change_stat("love", 70, -5, 1)
                    $ RogueX.change_stat("love", 200, -2)
                    ch_r "Well, at least make it worth it."
                    $ RogueX.change_stat("obedience", 50, 4)
                    $ RogueX.change_stat("inhibition", 80, 1)
                    $ RogueX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ RogueX.Forced = 1
                    jump Rogue_FP_Prep
                else:
                    $ RogueX.change_stat("love", 200, -15)
                    $ RogueX.change_face("angry", 1)
                    "She slaps your hand away."
                    $ RogueX.AddWord(1,"angry","angry")

    if "no_fondle pussy" in RogueX.daily_history:
        ch_r "Learn to take \"no\" for an answer, [RogueX.player_petname]."
        $ RogueX.AddWord(1,"angry","angry")
    elif RogueX.Forced:
        $ RogueX.change_face("angry", 1)
        ch_r "Stay out of my pants, [RogueX.player_petname]."
        $ RogueX.change_stat("lust", 70, 5)
        $ RogueX.change_stat("obedience", 50, -2)
        $ RogueX.AddWord(1,"angry","angry")
    elif Taboo:
        $ RogueX.change_face("angry", 1)
        $ RogueX.AddWord(1,"no_taboo","no_taboo")
        ch_r "I really don't think this is the right place for that!"
    elif RogueX.action_counter["fondle_pussy"]:
        $ RogueX.change_face("sad")
        ch_r "Sorry, keep your hands out of there."
    else:
        $ RogueX.change_face("sexy")
        $ RogueX.mouth = "sad"
        ch_r "No luck [RogueX.player_petname]."
    $ RogueX.recent_history.append("no_fondle pussy")
    $ RogueX.daily_history.append("no_fondle pussy")
    $ approval_bonus = 0
    return

ch_r "Sorry, I don't even know how I got here. . ."
return

label Rogue_FP_Prep:
    if offhand_action == "fondle_pussy":
        return

    call Rogue_Pussy_Launch ("fondle_pussy")

    if action_context == RogueX:

        $ action_context = 0
        if (RogueX.legs and not RogueX.Upskirt) or (RogueX.underwear and not RogueX.underwearDown):

            if ApprovalCheck(RogueX, 1250, TabM = 1) or (RogueX.SeenPussy and ApprovalCheck(RogueX, 500) and not Taboo):
                $ RogueX.Upskirt = 1
                $ RogueX.underwearDown = 1
                $ Line = 0
                if RogueX.PantsNum() == 5:
                    $ Line = RogueX.name+" hikes up her_skirt"
                elif RogueX.PantsNum() > 6:
                    $ Line = RogueX.name+" pulls down her " + RogueX.legs
                else:
                    $ Line = 0
                if RogueX.underwear:
                    if Line:

                        "[Line] and pulls her [RogueX.underwear] out of the way."
                        "She then grabs your arm and shoves your hand into her crotch, clearly intending you to get to work."
                    else:

                        "She pulls her [RogueX.underwear] out of the way, and then shoves your hand into her crotch."
                        "She clearly intends for you to get to work."
                else:

                    "[Line], and then shoves your hand into her crotch."
                    "She clearly intends for you to get to work."
                call Rogue_First_Bottomless (1)
            else:
                "[RogueX.name] grabs your arm and shoves your hand into her crotch, clearly intending you to get to work."
        else:
            "[RogueX.name] grabs your arm and shoves your hand into her crotch, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ RogueX.change_stat("inhibition", 80, 3)
                $ RogueX.change_stat("inhibition", 50, 2)
                "You start to run your fingers along her pussy."
            "Praise her.":
                $ RogueX.change_face("sexy", 1)
                $ RogueX.change_stat("inhibition", 80, 3)
                ch_p "I like the initiative, [RogueX.petname]."
                $ RogueX.nameCheck()
                "You start to run your fingers along her pussy."
                $ RogueX.change_stat("love", 85, 1)
                $ RogueX.change_stat("obedience", 90, 1)
                $ RogueX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your hand back."
                $ RogueX.change_face("surprised")
                $ RogueX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [RogueX.petname]."
                $ RogueX.nameCheck()
                "[RogueX.name] pulls back."
                $ RogueX.change_stat("obedience", 90, 1)
                $ RogueX.change_stat("obedience", 50, 1)
                $ RogueX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ RogueX.AddWord(1,"refused","refused")
                return


    if not RogueX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (RogueX)
        if "angry" in RogueX.recent_history:
            return
    $ approval_bonus = 0
    if not RogueX.action_counter["fondle_pussy"]:
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -50)
            $ RogueX.change_stat("obedience", 70, 35)
            $ RogueX.change_stat("inhibition", 80, 25)
        else:
            $ RogueX.change_stat("love", 90, 10)
            $ RogueX.change_stat("obedience", 70, 10)
            $ RogueX.change_stat("inhibition", 80, 15)
    if Taboo:
        $ RogueX.inhibition += int(Taboo/10)
        $ RogueX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ RogueX.DrainWord("no_taboo")
    $ RogueX.DrainWord("no_fondle pussy")
    $ RogueX.AddWord(0,"fondle_pussy","fondle_pussy")
    call Rogue_Pussy_Launch ("fondle_pussy")

    $ action_speed = 1

label Rogue_FP_Cycle:
    while Round > 0:
        call ViewShift (RogueX, RogueX.pose, 0, "fondle_pussy")
        call shift_focus (RogueX)
        $ RogueX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass

                "I want to stick a finger in. . ." if action_speed != 2:
                    if RogueX.action_counter["finger_pussy"]:
                        $ action_speed = 2
                    else:
                        menu:
                            "Ask her first":
                                $ action_context = "shift"
                            "Don't ask first [[just stick it in]":
                                $ action_context = "auto"
                        call Rogue_Insert_Pussy

                "Pull back a bit. . ." if action_speed == 2:
                    $ action_speed = 0
                "Slap her ass":

                    call Slap_Ass (RogueX)
                    $ counter += 1
                    $ Round -= 1
                    jump Rogue_FP_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (RogueX, "menu")
                    jump Rogue_FP_Cycle
                "Other options":

                    menu:
                        "Offhand action":
                            if RogueX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ RogueX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (RogueX, "tired")
                        "Shift primary action":

                            if RogueX.remaining_actions and multi_action:
                                menu:
                                    "I want to lick your pussy.":
                                        $ action_context = "shift"
                                        call Rogue_FP_After
                                        call Rogue_Lick_Pussy
                                    "Just start licking":
                                        $ action_context = "auto"
                                        call Rogue_FP_After
                                        call Rogue_Lick_Pussy
                                    "Pull back to the thighs":
                                        $ action_context = "pullback"
                                        call Rogue_FP_After
                                        call Rogue_Fondle_Thighs
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Rogue_FP_After
                                        call Rogue_Dildo_Pussy
                                    "Never Mind":
                                        jump Rogue_FP_Cycle
                            else:
                                call Sex_Basic_Dialog (RogueX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Rogue_FP_After
                            call Offhand_Set
                        "Shift your focus (locked)" if not offhand_action:
                            pass

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [RogueX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (RogueX)
                                "Ask [RogueX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (RogueX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (RogueX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Rogue_FP_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Rogue_FP_Cycle
                                "Never mind":
                                    jump Rogue_FP_Cycle

                        "Show her feet" if not ShowFeet and (RogueX.pose == "doggy" or RogueX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (RogueX.pose == "doggy" or RogueX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [RogueX.name]":

                            call Girl_Undress (RogueX)
                        "Clean up [RogueX.name] (locked)" if not RogueX.Spunk:
                            pass
                        "Clean up [RogueX.name]" if RogueX.Spunk:
                            call Girl_Cleanup (RogueX, "ask")
                        "Never mind":
                            jump Rogue_FP_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Rogue_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Rogue_FP_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Rogue_Pos_Reset
                    $ Line = 0
                    jump Rogue_FP_After


        call shift_focus (RogueX)
        call Sex_Dialog (RogueX, Partner)



        $ counter += 1
        $ Round -= 1
        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or RogueX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (RogueX)
                if "angry" in RogueX.recent_history:
                    call Rogue_Pos_Reset
                    return
                $ RogueX.change_stat("lust", 200, 5)
                if 100 > RogueX.lust >= 70 and RogueX.session_orgasms < 2:
                    $ RogueX.AddWord(0,"unsatisfied","unsatisfied")

                if Player.focus > 80:
                    jump Rogue_FP_After
                $ Line = "came"

            if RogueX.lust >= 100:

                call Girl_Cumming (RogueX)
                if action_context == "shift" or "angry" in RogueX.recent_history:
                    jump Rogue_FP_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in RogueX.recent_history:
                    "[RogueX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Rogue_FP_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif counter == (5 + RogueX.action_counter["fondle_pussy"]):
            $ RogueX.brows = "confused"
            ch_r "You like how that feels, huh?"
        elif RogueX.lust >= 80:
            pass
        elif counter == (15 + RogueX.action_counter["fondle_pussy"]) and RogueX.SEXP >= 15 and not ApprovalCheck(RogueX, 1500):
            $ RogueX.brows = "confused"
            menu:
                ch_r "I know you're having fun, but maybe we could try something else [RogueX.player_petname]."
                "Finish up.":
                    "You let go. . ."
                    jump Rogue_FP_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Rogue_FP_After
                "No, this is fun.":
                    if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):
                        $ RogueX.change_stat("love", 200, -5)
                        $ RogueX.change_stat("obedience", 50, 3)
                        $ RogueX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ RogueX.change_face("angry", 1)
                        call Rogue_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_r "Well if that's your attitude, I don't need your \"help\"."
                        $ RogueX.change_stat("love", 50, -3, 1)
                        $ RogueX.change_stat("love", 80, -4, 1)
                        $ RogueX.change_stat("obedience", 30, -1, 1)
                        $ RogueX.change_stat("obedience", 50, -1, 1)
                        $ RogueX.AddWord(1,"angry","angry")
                        jump Rogue_FP_After


        call Escalation (RogueX)

        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."


    $ RogueX.change_face("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.player_petname], that's enough of that for now."


label Rogue_FP_After:
    if not action_context:
        call Rogue_Pos_Reset

    $ RogueX.change_face("sexy")

    $ RogueX.action_counter["fondle_pussy"] += 1
    $ RogueX.remaining_actions -=1
    if RogueX.PantsNum() < 6 or RogueX.Upskirt:
        $ RogueX.addiction_rate += 1
        if "addictive" in Player.Traits:
            $ RogueX.addiction_rate += 1

    call Partner_Like (RogueX, 2)

    if RogueX.action_counter["fondle_pussy"] == 1:
        $ RogueX.SEXP += 7
        if not action_context:
            if RogueX.love >= 500 and "unsatisfied" not in RogueX.recent_history:
                ch_r "Certainly different with someone else at the wheel."
            elif RogueX.obedience <= 500 and Player.focus <= 20:
                $ RogueX.change_face("perplexed", 1)
                ch_r "Was that enough for you?"

    $ approval_bonus = 0


    call checkout
    return




label Rogue_Insert_Pussy:
    call shift_focus (RogueX)
    if action_context == "auto":
        if ApprovalCheck(RogueX, 1100, TabM = 2):
            $ RogueX.change_face("surprised")
            $ RogueX.change_stat("obedience", 90, 1)
            $ RogueX.change_stat("obedience", 70, 2)
            $ RogueX.change_stat("inhibition", 70, 3)
            $ RogueX.change_stat("inhibition", 30, 2)
            "As you slide a finger in, [RogueX.name] seems a bit surprised, but seems into it."
            jump Rogue_IP_Prep
        else:
            $ RogueX.change_face("surprised")
            $ RogueX.change_stat("love", 80, -2)
            $ RogueX.change_stat("obedience", 50, -3)
            ch_r "Keep it outside, [RogueX.player_petname]."
            return

    if ApprovalCheck(RogueX, 1100, TabM = 2):
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
            $ RogueX.change_stat("obedience", 90, 1)
            $ RogueX.change_stat("inhibition", 60, 1)
            ch_r "Sure, get in there."
        else:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.change_stat("love", 90, 1)
            $ RogueX.change_stat("inhibition", 50, 3)
            ch_r "God yes."
        $ RogueX.change_stat("obedience", 20, 1)
        $ RogueX.change_stat("obedience", 60, 1)
        $ RogueX.change_stat("inhibition", 70, 2)
        jump Rogue_IP_Prep
    else:

        $ RogueX.change_face("bemused", 2)
        ch_r "Um, no thanks, [RogueX.player_petname]."
        $ RogueX.blushing = 1
    return


label Rogue_IP_Prep:
    if not RogueX.action_counter["finger_pussy"]:
        $ RogueX.action_counter["finger_pussy"] = 1
        $ RogueX.SEXP += 10
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -60)
            $ RogueX.change_stat("obedience", 70, 55)
            $ RogueX.change_stat("inhibition", 80, 35)
        else:
            $ RogueX.change_stat("love", 90, 10)
            $ RogueX.change_stat("obedience", 70, 20)
            $ RogueX.change_stat("inhibition", 80, 25)

    if not RogueX.Forced and action_context != "auto":
        call Girl_Undress (RogueX, "bottom")
        if "angry" in RogueX.recent_history:
            return

    if Taboo:
        $ RogueX.inhibition += int(Taboo/10)
        $ RogueX.lust += int(Taboo/5)

    $ Line = 0
    $ action_speed = 2
    return







label Rogue_Lick_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (RogueX)

    if RogueX.action_counter["eat_pussy"]:
        $ approval_bonus += 15
    if RogueX.PantsNum() >= 6 or RogueX.HoseNum() >= 5:
        $ approval_bonus -= 15
    if RogueX.lust > 95:
        $ approval_bonus += 20
    elif RogueX.lust > 85:
        $ approval_bonus += 15
    if action_context == "shift":
        $ approval_bonus += 10
    if RogueX.lust > 85 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in RogueX.Traits:
        $ approval_bonus += (4*Taboo)
    if RogueX in Player.Harem or "sex friend" in RogueX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in RogueX.Traits:
        $ approval_bonus -= 25
    if RogueX.event_counter["forced"] and not RogueX.Forced:
        $ approval_bonus -= 5*RogueX.event_counter["forced"]

    if Taboo and "no_taboo" in RogueX.daily_history:
        $ approval_bonus -= 10

    if "no_lick pussy" in RogueX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_lick pussy" in RogueX.recent_history else 0

    $ Approval = ApprovalCheck(RogueX, 1250, TabM = 4)

    if action_context == "auto":
        if Approval:
            $ RogueX.change_face("surprised")
            $ RogueX.change_stat("obedience", 90, 1)
            $ RogueX.change_stat("obedience", 70, 2)
            $ RogueX.change_stat("inhibition", 70, 3)
            $ RogueX.change_stat("inhibition", 30, 2)
            "As you crouch down and start to lick her pussy, [RogueX.name] startles, but then sinks into the sensation."
            $ RogueX.change_face("sexy")
            jump Rogue_LP_Prep
        else:
            $ RogueX.change_face("surprised")
            $ RogueX.change_stat("love", 80, -2)
            $ RogueX.change_stat("obedience", 50, -3)
            ch_r "Oh! No, no thank you, [RogueX.player_petname]."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "eat_pussy" in RogueX.recent_history:
        $ RogueX.change_face("sexy", 1)
        ch_r "Mmm, again? Ok."
        jump Rogue_LP_Prep
    elif "eat_pussy" in RogueX.daily_history:
        $ RogueX.change_face("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Again? Oh, you're insatiable!",
            "Must be my lucky day!",
            "You sure know how to keep a girl satisfied. . .",
            "Mmm. . ."])
        ch_r "[Line]"

    if Approval >= 2:
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
            $ RogueX.change_stat("obedience", 90, 1)
            $ RogueX.change_stat("inhibition", 60, 1)
            ch_r "Sure, get in there."
        else:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.eyes = "closed"
            $ RogueX.change_stat("love", 90, 1)
            $ RogueX.change_stat("inhibition", 50, 3)
            $ RogueX.change_stat("lust", 200, 3)
            ch_r "Oooooooh. . ."
        $ RogueX.change_stat("obedience", 20, 1)
        $ RogueX.change_stat("obedience", 60, 1)
        $ RogueX.change_stat("inhibition", 70, 2)
        jump Rogue_LP_Prep
    else:

        $ RogueX.change_face("angry", 1)
        if "no_lick pussy" in RogueX.recent_history:
            ch_r "I {i}just{/i} told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history and "no_lick pussy" in RogueX.daily_history:
            ch_r "You already got your answer!"
        elif "no_lick pussy" in RogueX.daily_history:
            ch_r "I already told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "I told you not in public!"
        elif not RogueX.action_counter["eat_pussy"]:
            $ RogueX.change_face("bemused")
            ch_r "That's pretty intimate, [RogueX.player_petname]. . ."
        else:
            $ RogueX.change_face("bemused")
            ch_r "Oh, um, no, I'm not really comfortable with that. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_lick pussy" in RogueX.daily_history:
                $ RogueX.change_face("bemused")
                ch_r "Yeah, ok, [RogueX.player_petname]."
                return
            "I'm sure I can convince you later. . ." if "no_lick pussy" not in RogueX.daily_history:
                $ RogueX.change_face("sexy")
                ch_r "I'll be thinking about it, [RogueX.player_petname]."
                $ RogueX.change_stat("love", 80, 2)
                $ RogueX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ RogueX.AddWord(1,"no_taboo","no_taboo")
                $ RogueX.recent_history.append("no_lick pussy")
                $ RogueX.daily_history.append("no_lick pussy")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ RogueX.change_face("sexy")
                    $ RogueX.change_stat("obedience", 90, 2)
                    $ RogueX.change_stat("obedience", 50, 2)
                    ch_r "Ok, you're probably right. . ."
                    $ RogueX.change_stat("inhibition", 70, 3)
                    $ RogueX.change_stat("inhibition", 40, 2)
                    jump Rogue_LP_Prep
                else:
                    $ RogueX.change_face("sexy")
                    ch_r "Tsk, not this time, [RogueX.player_petname], that just seems. . . intimate."
            "[[Get in there anyway]":

                $ Approval = ApprovalCheck(RogueX, 750, "OI", TabM = 4)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.change_face("sad")
                    $ RogueX.change_stat("love", 70, -5, 1)
                    $ RogueX.change_stat("love", 200, -2)
                    ch_r "Ok, get in there if you're so determined."
                    $ RogueX.change_stat("obedience", 50, 4)
                    $ RogueX.change_stat("inhibition", 80, 1)
                    $ RogueX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ RogueX.Forced = 1
                    jump Rogue_LP_Prep
                else:
                    $ RogueX.change_stat("love", 200, -15)
                    $ RogueX.change_face("angry", 1)
                    "She shoves your head back."
                    $ RogueX.AddWord(1,"angry","angry")

    if "no_lick pussy" in RogueX.daily_history:
        ch_r "Learn to take \"no\" for an answer, [RogueX.player_petname]."
        $ RogueX.AddWord(1,"angry","angry")
    elif RogueX.Forced:
        $ RogueX.change_face("angry", 1)
        ch_r "Not even, [RogueX.player_petname]."
        $ RogueX.change_stat("lust", 80, 5)
        $ RogueX.change_stat("obedience", 50, -2)
        $ RogueX.AddWord(1,"angry","angry")
    elif Taboo:
        $ RogueX.change_face("angry", 1)
        $ RogueX.AddWord(1,"no_taboo","no_taboo")
        ch_r "This just really isn't the time or place, [RogueX.player_petname]!"
    elif RogueX.action_counter["eat_pussy"]:
        $ RogueX.change_face("sad")
        ch_r "Sorry, keep your tongue in your mouth."
    else:
        $ RogueX.change_face("surprised")
        ch_r "Ew!"
        $ RogueX.change_face()
    $ RogueX.recent_history.append("no_lick pussy")
    $ RogueX.daily_history.append("no_lick pussy")
    $ approval_bonus = 0
    return

label Rogue_LP_Prep:
    if offhand_action == "eat_pussy":
        return

    call Rogue_Pussy_Launch ("eat_pussy")


    if action_context == RogueX:

        $ action_context = 0
        if (RogueX.legs and not RogueX.Upskirt) or (RogueX.underwear and not RogueX.underwearDown):

            if ApprovalCheck(RogueX, 1250, TabM = 1) or (RogueX.SeenPussy and ApprovalCheck(RogueX, 500) and not Taboo):
                $ RogueX.Upskirt = 1
                $ RogueX.underwearDown = 1
                $ Line = 0
                if RogueX.PantsNum() == 5:
                    $ Line = RogueX.name+" hikes up her_skirt"
                elif RogueX.PantsNum() > 6:
                    $ Line = RogueX.name+" pulls down her " + RogueX.legs
                else:
                    $ Line = 0
                if RogueX.underwear:
                    if Line:

                        "[Line] and pulls her [RogueX.underwear] out of the way."
                        "She then grabs your head and pulls it to her crotch, clearly intending you to get to work."
                    else:

                        "She pulls her [RogueX.underwear] out of the way, and then shoves your face into her crotch."
                        "She clearly intends for you to get to work."
                else:

                    "[Line], and then shoves your face into her crotch."
                    "She clearly intends for you to get to work."
                call Rogue_First_Bottomless (1)
            else:
                "[RogueX.name] grabs your head and pulls it to her crotch, clearly intending you to get to work."
        else:
            "[RogueX.name] grabs your head and pulls it to her crotch, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ RogueX.change_stat("inhibition", 80, 3)
                $ RogueX.change_stat("inhibition", 50, 2)
                "You start licking."
            "Praise her.":
                $ RogueX.change_face("sexy", 1)
                $ RogueX.change_stat("inhibition", 80, 3)
                ch_p "Mmm, I like this idea, [RogueX.petname]."
                $ RogueX.nameCheck()
                "You start licking."
                $ RogueX.change_stat("love", 85, 1)
                $ RogueX.change_stat("obedience", 90, 1)
                $ RogueX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your head away."
                $ RogueX.change_face("surprised")
                $ RogueX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [RogueX.petname]."
                $ RogueX.nameCheck()
                "[RogueX.name] pulls back."
                $ RogueX.change_stat("obedience", 90, 1)
                $ RogueX.change_stat("obedience", 50, 1)
                $ RogueX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ RogueX.AddWord(1,"refused","refused")
                return


    if not RogueX.Forced and action_context != "auto":
        $ approval_bonus = 0
        if RogueX.PantsNum() >= 6:
            $ approval_bonus = 15
        call Bottoms_Off (RogueX)
        if "angry" in RogueX.recent_history:
            return

    $ approval_bonus = 0
    if not RogueX.action_counter["eat_pussy"]:
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -30)
            $ RogueX.change_stat("obedience", 70, 35)
            $ RogueX.change_stat("inhibition", 80, 75)
        else:
            $ RogueX.change_stat("love", 90, 35)
            $ RogueX.change_stat("obedience", 70, 15)
            $ RogueX.change_stat("inhibition", 80, 35)
    if Taboo:
        $ RogueX.inhibition += int(Taboo/10)
        $ RogueX.lust += int(Taboo/5)
    if action_context:
        $ renpy.pop_call()
        $ action_context = 0

    if RogueX.PantsNum() == 5:
        $ RogueX.Upskirt = 1
        $ RogueX.SeenPanties = 1
    call Rogue_First_Bottomless (1)

    $ Line = 0
    $ counter = 0
    if Taboo:
        $ RogueX.DrainWord("no_taboo")
    $ RogueX.DrainWord("no_lick pussy")
    $ RogueX.AddWord(0,"eat_pussy","eat_pussy")
    call Rogue_Pussy_Launch ("eat_pussy")

label Rogue_LP_Cycle:
    if offhand_action == "kiss":
        $ offhand_action = 0
    while Round > 0:
        call ViewShift (RogueX, RogueX.pose, 0, "eat_pussy")
        call shift_focus (RogueX)
        $ RogueX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (RogueX)
                    $ counter += 1
                    $ Round -= 1
                    jump Rogue_LP_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (RogueX, "menu")
                    jump Rogue_LP_Cycle
                "Other options":

                    menu:
                        "Offhand action":
                            if RogueX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ RogueX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (RogueX, "tired")
                        "Shift primary action":

                            if RogueX.remaining_actions and multi_action:
                                menu:
                                    "Pull out and start rubbing again.":
                                        if RogueX.remaining_actions and multi_action:
                                            $ action_context = "pullback"
                                            call Rogue_LP_After
                                            call Rogue_Fondle_Pussy
                                        else:
                                            call Sex_Basic_Dialog (RogueX, "tired")
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Rogue_LP_After
                                        call Rogue_Dildo_Pussy
                                    "Never Mind":
                                        jump Rogue_LP_Cycle
                            else:
                                call Sex_Basic_Dialog (RogueX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Rogue_LP_After
                            call Offhand_Set
                        "Shift your focus (locked)" if not offhand_action:
                            pass

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [RogueX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (RogueX)
                                "Ask [RogueX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (RogueX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (RogueX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Rogue_LP_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Rogue_LP_Cycle
                                "Never mind":
                                    jump Rogue_LP_Cycle

                        "Show her feet" if not ShowFeet and (RogueX.pose == "doggy" or RogueX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (RogueX.pose == "doggy" or RogueX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [RogueX.name]":

                            call Girl_Undress (RogueX)
                        "Clean up [RogueX.name] (locked)" if not RogueX.Spunk:
                            pass
                        "Clean up [RogueX.name]" if RogueX.Spunk:
                            call Girl_Cleanup (RogueX, "ask")
                        "Never mind":
                            jump Rogue_LP_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Rogue_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Rogue_LP_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Rogue_Pos_Reset
                    $ Line = 0
                    jump Rogue_LP_After


        if RogueX.underwear or RogueX.PantsNum() >= 6 or RogueX.HoseNum() >= 5:
            call Girl_Undress (RogueX, "auto")

        call shift_focus (RogueX)
        call Sex_Dialog (RogueX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or RogueX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (RogueX)
                if "angry" in RogueX.recent_history:
                    call Rogue_Pos_Reset
                    return
                $ RogueX.change_stat("lust", 200, 5)
                if 100 > RogueX.lust >= 70 and RogueX.session_orgasms < 2:
                    $ RogueX.AddWord(0,"unsatisfied","unsatisfied")

                if Player.focus > 80:
                    jump Rogue_LP_After
                $ Line = "came"

            if RogueX.lust >= 100:

                call Girl_Cumming (RogueX)
                if action_context == "shift" or "angry" in RogueX.recent_history:
                    jump Rogue_LP_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in RogueX.recent_history:
                    "[RogueX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Rogue_LP_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif counter == (5 + RogueX.action_counter["eat_pussy"]):
            $ RogueX.brows = "confused"
            ch_r "You like it down there?"
        elif RogueX.lust >= 80:
            pass
        elif counter == (15 + RogueX.action_counter["eat_pussy"]) and RogueX.SEXP >= 15 and not ApprovalCheck(RogueX, 1500):
            $ RogueX.brows = "confused"
            menu:
                ch_r "[RogueX.player_petname], I know you're having fun down there, but maybe we could try something else."
                "Finish up.":
                    "You let go. . ."
                    jump Rogue_LP_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Rogue_LP_After
                "No, this is fun.":
                    if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):
                        $ RogueX.change_stat("love", 200, -5)
                        $ RogueX.change_stat("obedience", 50, 3)
                        $ RogueX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ RogueX.change_face("angry", 1)
                        call Rogue_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_r "Well if that's your attitude, I don't need your \"help\"."
                        $ RogueX.change_stat("love", 50, -3, 1)
                        $ RogueX.change_stat("love", 80, -4, 1)
                        $ RogueX.change_stat("obedience", 30, -1, 1)
                        $ RogueX.change_stat("obedience", 50, -1, 1)
                        $ RogueX.AddWord(1,"angry","angry")
                        jump Rogue_LP_After


        call Escalation (RogueX)

        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."


    $ RogueX.change_face("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.player_petname], that's enough of that for now."


label Rogue_LP_After:
    if not action_context:
        call Rogue_Pos_Reset

    $ RogueX.change_face("sexy")

    $ RogueX.action_counter["eat_pussy"] += 1
    $ RogueX.remaining_actions -=1
    if RogueX.PantsNum() < 6 or RogueX.Upskirt:
        $ RogueX.addiction_rate += 1
        if "addictive" in Player.Traits:
            $ RogueX.addiction_rate += 1

    if Partner == EmmaX:
        call Partner_Like (RogueX, 4, 3)
    else:
        call Partner_Like (RogueX, 3, 3)

    if RogueX.action_counter["eat_pussy"] == 1:
        $ RogueX.SEXP += 10
        if not action_context:
            if RogueX.love >= 500 and "unsatisfied" not in RogueX.recent_history:
                ch_r "I. . . how'd I taste?"
            elif RogueX.obedience <= 500 and Player.focus <= 20:
                $ RogueX.change_face("perplexed", 1)
                ch_r "Did you like that?"

    $ approval_bonus = 0


    call checkout
    return






label Rogue_Fondle_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (RogueX)

    if RogueX.action_counter["fondle_ass"]:
        $ approval_bonus += 10
    if RogueX.PantsNum() >= 6 or RogueX.HoseNum() >= 5:
        $ approval_bonus -= 5
    if RogueX.lust > 75:
        $ approval_bonus += 15
    if "exhibitionist" in RogueX.Traits:
        $ approval_bonus += Taboo
    if RogueX in Player.Harem or "sex friend" in RogueX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in RogueX.Traits:
        $ approval_bonus -= 25
    if RogueX.event_counter["forced"] and not RogueX.Forced:
        $ approval_bonus -= 5*RogueX.event_counter["forced"]

    if Taboo and "no_taboo" in RogueX.daily_history:
        $ approval_bonus -= 10

    if "no_fondle ass" in RogueX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle ass" in RogueX.recent_history else 0

    $ Approval = ApprovalCheck(RogueX, 850, TabM=1)

    if action_context == "auto":
        if Approval:
            $ RogueX.change_face("surprised", 1)
            $ RogueX.change_stat("obedience", 70, 2)
            $ RogueX.change_stat("inhibition", 40, 2)
            "As your hand creeps down her backside, [RogueX.name] seems a bit surprised, but then nods."
            $ RogueX.change_face("sexy")
            jump Rogue_FA_Prep
        else:
            $ RogueX.change_face("surprised")
            $ RogueX.change_stat("obedience", 50, -3)
            ch_r "Hands off, [RogueX.player_petname]."
            $ RogueX.change_face("bemused")
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if action_context == "pullback":
        $ RogueX.change_face("surprised")
        $ RogueX.brows = "sad"
        if RogueX.lust > 80:
            $ RogueX.change_stat("love", 70, -4)
        $ RogueX.change_stat("obedience", 90, 1)
        $ RogueX.change_stat("obedience", 70, 2)
        "As your hand slides out, [RogueX.name] gasps and looks upset."
        jump Rogue_FA_Prep
    elif "fondle_ass" in RogueX.recent_history:
        $ RogueX.change_face("sexy", 1)
        ch_r "Mmm, again? Ok."
        jump Rogue_FA_Prep
    elif "fondle_ass" in RogueX.daily_history:
        $ RogueX.change_face("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Maybe not so rough this time though.",
            "Mmm. . ."])
        ch_r "[Line]"

    if Approval >= 2:
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -2, 1)
            $ RogueX.change_stat("obedience", 90, 2)
            $ RogueX.change_stat("inhibition", 60, 2)
            ch_r "Fine, grab a cheek."
        else:
            $ RogueX.change_face("bemused, 1")
            ch_r "Sure, grab a cheek."
        $ RogueX.change_stat("lust", 200, 3)
        $ RogueX.change_stat("obedience", 60, 1)
        $ RogueX.change_stat("inhibition", 70, 1)
        jump Rogue_FA_Prep
    else:

        $ RogueX.change_face("angry", 1)
        if "no_fondle ass" in RogueX.recent_history:
            ch_r "I {i}just{/i} told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history and "no_fondle ass" in RogueX.daily_history:
            ch_r "I told you not to touch me like that in public!"
        elif "no_fondle ass" in RogueX.daily_history:
            ch_r "I already told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "I told you not in public!"
        elif not RogueX.action_counter["fondle_ass"]:
            $ RogueX.change_face("bemused")
            ch_r "Not yet, [RogueX.player_petname]. . ."
        else:
            $ RogueX.change_face("bemused")
            ch_r "Let's not, ok [RogueX.player_petname]?"
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle ass" in RogueX.daily_history:
                $ RogueX.change_face("bemused")
                ch_r "Yeah, ok, [RogueX.player_petname]."
                return
            "Maybe later?" if "no_fondle ass" not in RogueX.daily_history:
                $ RogueX.change_face("sexy")
                ch_r "Heh, maybe, [RogueX.player_petname]."
                $ RogueX.change_stat("love", 80, 2)
                $ RogueX.change_stat("inhibition", 50, 2)
                if Taboo:
                    $ RogueX.AddWord(1,"no_taboo","no_taboo")
                $ RogueX.recent_history.append("no_fondle ass")
                $ RogueX.daily_history.append("no_fondle ass")
                return
            "Just one good squeeze?":
                if Approval:
                    $ RogueX.change_face("sexy")
                    $ RogueX.change_stat("obedience", 90, 1)
                    $ RogueX.change_stat("obedience", 50, 2)
                    ch_r "Well, if you're gonna beg. . ."
                    $ RogueX.change_stat("inhibition", 70, 1)
                    $ RogueX.change_stat("inhibition", 40, 2)
                    jump Rogue_FA_Prep
                else:
                    $ RogueX.change_face("sexy")
                    ch_r "Tsk, not this time, [RogueX.player_petname]."
            "[[Start fondling anyway]":

                $ Approval = ApprovalCheck(RogueX, 250, "OI", TabM = 3)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.change_face("sad")
                    $ RogueX.change_stat("love", 70, -3, 1)
                    $ RogueX.change_stat("love", 200, -1)
                    ch_r "Fine, I suppose."
                    $ RogueX.change_stat("obedience", 50, 3)
                    $ RogueX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ RogueX.Forced = 1
                    jump Rogue_FA_Prep
                else:
                    $ RogueX.change_stat("love", 200, -10)
                    $ RogueX.change_face("angry", 1)
                    "She slaps your hand away."
                    $ RogueX.AddWord(1,"angry","angry")

    if "no_fondle ass" in RogueX.daily_history:
        ch_r "Learn to take \"no\" for an answer, [RogueX.player_petname]."
        $ RogueX.AddWord(1,"angry","angry")
    elif RogueX.Forced:
        $ RogueX.change_face("angry", 1)
        ch_r "Hands off the booty!"
        $ RogueX.change_stat("lust", 60, 5)
        $ RogueX.change_stat("obedience", 50, -2)
        $ RogueX.AddWord(1,"angry","angry")
    elif Taboo:
        $ RogueX.change_face("angry", 1)
        $ RogueX.AddWord(1,"no_taboo","no_taboo")
        ch_r "[RogueX.player_petname]! Not in public!"
    elif RogueX.action_counter["fondle_ass"]:
        $ RogueX.change_face("sad")
        ch_r "Sorry, hands off the booty."
    else:
        $ RogueX.change_face("sexy")
        $ RogueX.mouth = "sad"
        ch_r "Shoo, [RogueX.player_petname]."
    $ RogueX.recent_history.append("no_fondle ass")
    $ RogueX.daily_history.append("no_fondle ass")
    $ approval_bonus = 0
    return

ch_r "Sorry, I don't even know how I got here. . ."
return

label Rogue_FA_Prep:
    if offhand_action == "fondle_ass":
        return
    if not RogueX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (RogueX)
        if "angry" in RogueX.recent_history:
            return
    $ approval_bonus = 0
    call Rogue_Pussy_Launch ("fondle_ass")
    if not RogueX.action_counter["fondle_ass"]:
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -20)
            $ RogueX.change_stat("obedience", 70, 20)
            $ RogueX.change_stat("inhibition", 80, 15)
        else:
            $ RogueX.change_stat("love", 90, 10)
            $ RogueX.change_stat("obedience", 70, 12)
            $ RogueX.change_stat("inhibition", 80, 20)
    if Taboo:
        $ RogueX.inhibition += int(Taboo/10)
        $ RogueX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ RogueX.DrainWord("no_taboo")
    $ RogueX.DrainWord("no_fondle ass")
    $ RogueX.AddWord(0,"fondle_ass","fondle_ass")
    call Rogue_Pussy_Launch ("fondle_ass")

label Rogue_FA_Cycle:
    while Round > 0:
        call ViewShift (RogueX, RogueX.pose, 0, "fondle_ass")
        call shift_focus (RogueX)
        $ RogueX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (RogueX)
                    $ counter += 1
                    $ Round -= 1
                    jump Rogue_FA_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (RogueX, "menu")
                    jump Rogue_FA_Cycle
                "Other options":

                    menu:
                        "Offhand action":
                            if RogueX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ RogueX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (RogueX, "tired")
                        "Shift primary action":

                            if RogueX.remaining_actions and multi_action:
                                menu:
                                    "I want to stick a finger in.":
                                        $ action_context = "shift"
                                        call Rogue_FA_After
                                        call Rogue_Insert_Ass
                                    "Just stick a finger in without asking.":
                                        $ action_context = "auto"
                                        call Rogue_FA_After
                                        call Rogue_Insert_Ass
                                    "I want to lick your asshole.":
                                        $ action_context = "shift"
                                        call Rogue_FA_After
                                        call Rogue_Lick_Ass
                                    "Just start licking.":
                                        $ action_context = "auto"
                                        call Rogue_FA_After
                                        call Rogue_Lick_Ass
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Rogue_FA_After
                                        call Rogue_Dildo_Ass
                                    "Never Mind":
                                        jump Rogue_FA_Cycle
                            else:
                                call Sex_Basic_Dialog (RogueX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Rogue_FA_After
                            call Offhand_Set
                        "Shift your focus (locked)" if not offhand_action:
                            pass

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [RogueX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (RogueX)
                                "Ask [RogueX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (RogueX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (RogueX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Rogue_FA_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Rogue_FA_Cycle
                                "Never mind":
                                    jump Rogue_FA_Cycle

                        "Show her feet" if not ShowFeet and (RogueX.pose == "doggy" or RogueX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (RogueX.pose == "doggy" or RogueX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [RogueX.name]":

                            call Girl_Undress (RogueX)
                        "Clean up [RogueX.name] (locked)" if not RogueX.Spunk:
                            pass
                        "Clean up [RogueX.name]" if RogueX.Spunk:
                            call Girl_Cleanup (RogueX, "ask")
                        "Never mind":
                            jump Rogue_FA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Rogue_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Rogue_FA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Rogue_Pos_Reset
                    $ Line = 0
                    jump Rogue_FA_After


        if RogueX.underwear or RogueX.PantsNum() >= 6 or RogueX.HoseNum() >= 5:
            call Girl_Undress (RogueX, "auto")

        call shift_focus (RogueX)
        call Sex_Dialog (RogueX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or RogueX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (RogueX)
                if "angry" in RogueX.recent_history:
                    call Rogue_Pos_Reset
                    return
                $ RogueX.change_stat("lust", 200, 5)
                if 100 > RogueX.lust >= 70 and RogueX.session_orgasms < 2 and RogueX.SEXP >= 20:
                    $ RogueX.AddWord(0,"unsatisfied","unsatisfied")

                if Player.focus > 80:
                    jump Rogue_FA_After
                $ Line = "came"

            if RogueX.lust >= 100:

                call Girl_Cumming (RogueX)
                if action_context == "shift" or "angry" in RogueX.recent_history:
                    jump Rogue_FA_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in RogueX.recent_history:
                    "[RogueX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Rogue_FA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif counter == (5 + RogueX.action_counter["fondle_ass"]):
            $ RogueX.brows = "confused"
            ch_r "Uh, that's nice, but. . ."
        elif RogueX.lust >= 80:
            pass
        elif counter == (15 + RogueX.action_counter["fondle_ass"]) and RogueX.SEXP >= 15 and not ApprovalCheck(RogueX, 1500):
            $ RogueX.brows = "confused"
            menu:
                ch_r "[RogueX.player_petname], this is nice, but could we do something else?"
                "Finish up.":
                    "You let go. . ."
                    jump Rogue_FA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Rogue_FA_After
                "No, this is fun.":
                    if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):
                        $ RogueX.change_stat("love", 200, -5)
                        $ RogueX.change_stat("obedience", 50, 3)
                        $ RogueX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ RogueX.change_face("angry", 1)
                        call Rogue_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_r "Well if that's your attitude, I don't need your \"help\"."
                        $ RogueX.change_stat("love", 50, -3, 1)
                        $ RogueX.change_stat("love", 80, -4, 1)
                        $ RogueX.change_stat("obedience", 30, -1, 1)
                        $ RogueX.change_stat("obedience", 50, -1, 1)
                        $ RogueX.AddWord(1,"angry","angry")
                        jump Rogue_FA_After


        call Escalation (RogueX)

        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."


    $ RogueX.change_face("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.player_petname], that's enough of that for now."


label Rogue_FA_After:
    if not action_context:
        call Rogue_Pos_Reset

    $ RogueX.change_face("sexy")

    $ RogueX.action_counter["fondle_ass"] += 1
    $ RogueX.remaining_actions -=1
    if RogueX.PantsNum() < 6 or RogueX.Upskirt:
        $ RogueX.addiction_rate += 1
        if "addictive" in Player.Traits:
            $ RogueX.addiction_rate += 1

        call Partner_Like (RogueX, 2)

    if RogueX.action_counter["fondle_ass"] == 1:
        $ RogueX.SEXP += 4
        if not action_context:
            if RogueX.love >= 500 and "unsatisfied" not in RogueX.recent_history:
                ch_r "That was. . . nice. . ."
            elif RogueX.obedience <= 500 and Player.focus <= 20:
                $ RogueX.change_face("perplexed", 1)
                ch_r "Did you like that?"

    $ approval_bonus = 0


    call checkout
    return





label Rogue_Insert_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (RogueX)
    if RogueX.action_counter["finger_ass"]:
        $ approval_bonus += 25
    if RogueX.PantsNum() >= 6 or RogueX.HoseNum() >= 5:
        $ approval_bonus -= 15
    if RogueX.lust > 85 and RogueX.used_to_anal:
        $ approval_bonus += 15
    if RogueX.lust > 95 and RogueX.used_to_anal:
        $ approval_bonus += 5
    if action_context == "shift":
        $ approval_bonus += 10
    if RogueX.lust > 85 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in RogueX.Traits:
        $ approval_bonus += (4*Taboo)
    if RogueX in Player.Harem or "sex friend" in RogueX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in RogueX.Traits:
        $ approval_bonus -= 25
    if RogueX.event_counter["forced"] and not RogueX.Forced:
        $ approval_bonus -= 5*RogueX.event_counter["forced"]

    if Taboo and "no_taboo" in RogueX.daily_history:
        $ approval_bonus -= 10

    if "no_insert ass" in RogueX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_insert ass" in RogueX.recent_history else 0

    $ Approval = ApprovalCheck(RogueX, 1300, TabM = 3)

    if action_context == "auto":
        if Approval:
            $ RogueX.change_face("surprised")
            $ RogueX.change_stat("obedience", 90, 2)
            $ RogueX.change_stat("obedience", 70, 2)
            $ RogueX.change_stat("inhibition", 80, 2)
            $ RogueX.change_stat("inhibition", 30, 2)
            "As you slide a finger in, [RogueX.name] tightens around it in surprise, but seems into it."
            $ RogueX.change_face("sexy")
            jump Rogue_IA_Prep
        else:
            $ RogueX.change_face("surprised")
            $ RogueX.change_stat("love", 80, -2)
            $ RogueX.change_stat("obedience", 50, -3)
            ch_r "Keep it out of there, [RogueX.player_petname]."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "finger_ass" in RogueX.daily_history and not RogueX.used_to_anal:
        $ RogueX.change_face("bemused", 1)
        ch_r "I'm still a little sore from earlier, [RogueX.player_petname]."
    elif "finger_ass" in RogueX.daily_history:
        $ RogueX.change_face("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Maybe not so hard this time though.",
            "Mmm. . ."])
        ch_r "[Line]"

    if Approval >= 2:
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
            $ RogueX.change_stat("obedience", 90, 1)
            $ RogueX.change_stat("inhibition", 60, 1)
            ch_r "Sure, get in there."
        else:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.eyes = "closed"
            $ RogueX.change_stat("love", 90, 1)
            $ RogueX.change_stat("inhibition", 50, 3)
            $ RogueX.change_stat("lust", 200, 3)
            ch_r "Oooooooh. . ."
        $ RogueX.change_stat("obedience", 20, 1)
        $ RogueX.change_stat("obedience", 60, 1)
        $ RogueX.change_stat("inhibition", 70, 2)
        jump Rogue_IA_Prep
    else:

        $ RogueX.change_face("angry", 1)
        if "no_insert ass" in RogueX.recent_history:
            ch_r "I {i}just{/i} told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history and "no_insert ass" in RogueX.daily_history:
            ch_r "I told you that wasn't appropriate!"
        elif "no_insert ass" in RogueX.daily_history:
            ch_r "I already told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "I told you not in public!"
        elif not RogueX.action_counter["finger_ass"]:
            $ RogueX.change_face("perplexed", 1)
            ch_r "I. . . don't think that's. . ."
        else:
            $ RogueX.change_face("bemused")
            ch_r "Oh, um, no, I'm not really comfortable with that. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_insert ass" in RogueX.daily_history:
                $ RogueX.change_face("bemused")
                ch_r "Yeah, ok, [RogueX.player_petname]."
                return
            "Maybe later?" if "no_insert ass" not in RogueX.daily_history:
                $ RogueX.change_face("sexy")
                ch_r "It's. . . possible, [RogueX.player_petname]."
                $ RogueX.change_stat("love", 80, 2)
                $ RogueX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ RogueX.AddWord(1,"no_taboo","no_taboo")
                $ RogueX.recent_history.append("no_insert ass")
                $ RogueX.daily_history.append("no_insert ass")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ RogueX.change_face("sexy")
                    $ RogueX.change_stat("obedience", 90, 2)
                    $ RogueX.change_stat("obedience", 50, 2)
                    ch_r "Ok, you're probably right. . ."
                    $ RogueX.change_stat("inhibition", 70, 3)
                    $ RogueX.change_stat("inhibition", 40, 2)
                    jump Rogue_IA_Prep
                else:
                    $ RogueX.change_face("bemused")
                    ch_r "I really don't think that I would."
            "[[Slide a finger in anyway]":

                $ Approval = ApprovalCheck(RogueX, 950, "OI", TabM = 3)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.change_face("surprised", 1)
                    $ RogueX.change_stat("love", 70, -5, 1)
                    $ RogueX.change_stat("love", 200, -2)
                    ch_r "Oh. . . well, ok then. . ."
                    $ RogueX.change_face("sad")
                    $ RogueX.change_stat("obedience", 50, 4)
                    $ RogueX.change_stat("inhibition", 80, 1)
                    $ RogueX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ RogueX.Forced = 1
                    jump Rogue_IA_Prep
                else:
                    $ RogueX.change_stat("love", 200, -15)
                    $ RogueX.change_face("angry", 1)
                    "She slaps your hand away."
                    $ RogueX.AddWord(1,"angry","angry")

    if "no_insert ass" in RogueX.daily_history:
        ch_r "Learn to take \"no\" for an answer, [RogueX.player_petname]."
        $ RogueX.AddWord(1,"angry","angry")
    elif RogueX.Forced:
        $ RogueX.change_face("angry", 1)
        ch_r "Um, no way."
        if ApprovalCheck(RogueX, 500, "I"):
            $ RogueX.change_stat("lust", 80, 10)
        else:
            $ RogueX.change_stat("lust", 50, 3)
        $ RogueX.change_stat("obedience", 50, -2)
        $ RogueX.AddWord(1,"angry","angry")
    elif Taboo:
        $ RogueX.change_face("angry", 1)
        $ RogueX.AddWord(1,"no_taboo","no_taboo")
        ch_r "[RogueX.player_petname]! This just really isn't the time or place!"
    elif RogueX.action_counter["finger_ass"]:
        $ RogueX.change_face("sad")
        ch_r "I think you should keep your fingers to yourself."
    else:
        $ RogueX.change_face("surprised")
        ch_r "I. . . not there!!"
        $ RogueX.change_face()
    $ RogueX.recent_history.append("no_insert ass")
    $ RogueX.daily_history.append("no_insert ass")
    $ approval_bonus = 0
    return


label Rogue_IA_Prep:
    if offhand_action == "finger_ass":
        return

    call Rogue_Pussy_Launch ("finger_ass")

    if action_context == RogueX:

        $ action_context = 0
        if (RogueX.legs and not RogueX.Upskirt) or (RogueX.underwear and not RogueX.underwearDown):

            if ApprovalCheck(RogueX, 1250, TabM = 1) or (RogueX.SeenPussy and ApprovalCheck(RogueX, 500) and not Taboo):
                $ RogueX.Upskirt = 1
                $ RogueX.underwearDown = 1
                $ Line = 0
                if RogueX.PantsNum() == 5:
                    $ Line = RogueX.name+" hikes up her_skirt"
                elif RogueX.PantsNum() > 6:
                    $ Line = RogueX.name+" pulls down her " + RogueX.legs
                else:
                    $ Line = 0
                if RogueX.underwear:
                    if Line:

                        "[Line] and pulls her [RogueX.underwear] out of the way."
                        "She then grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
                    else:

                        "She pulls her [RogueX.underwear] out of the way, and then presses your hand against her asshole."
                        "She clearly intends for you to get to work."
                else:

                    "[Line], and then presses your hand against her asshole."
                    "She clearly intends for you to get to work."
                call Rogue_First_Bottomless (1)
            else:
                "[RogueX.name] grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
        else:
            "[RogueX.name] grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ RogueX.change_stat("inhibition", 80, 3)
                $ RogueX.change_stat("inhibition", 50, 2)
                "You press your finger into it."
            "Praise her.":
                $ RogueX.change_face("sexy", 1)
                $ RogueX.change_stat("inhibition", 80, 3)
                ch_p "Dirty girl, [RogueX.petname]."
                $ RogueX.nameCheck()
                "You press your finger into it."
                $ RogueX.change_stat("love", 85, 1)
                $ RogueX.change_stat("obedience", 90, 1)
                $ RogueX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your hand back."
                $ RogueX.change_face("surprised")
                $ RogueX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [RogueX.petname]."
                $ RogueX.nameCheck()
                "[RogueX.name] pulls back."
                $ RogueX.change_stat("obedience", 90, 1)
                $ RogueX.change_stat("obedience", 50, 1)
                $ RogueX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ RogueX.AddWord(1,"refused","refused")
                return


    if not RogueX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (RogueX)
        if "angry" in RogueX.recent_history:
            return

    $ approval_bonus = 0
    if not RogueX.action_counter["finger_ass"]:
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -50)
            $ RogueX.change_stat("obedience", 70, 60)
            $ RogueX.change_stat("inhibition", 80, 35)
        else:
            $ RogueX.change_stat("love", 90, 10)
            $ RogueX.change_stat("obedience", 70, 20)
            $ RogueX.change_stat("inhibition", 80, 25)

    if Taboo:
        $ RogueX.inhibition += int(Taboo/10)
        $ RogueX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ RogueX.DrainWord("no_taboo")
    $ RogueX.DrainWord("no_insert ass")
    $ RogueX.AddWord(0,"finger_ass","finger_ass")
    call Rogue_Pussy_Launch ("finger_ass")

label Rogue_IA_Cycle:
    while Round > 0:
        call ViewShift (RogueX, RogueX.pose, 0, "finger_ass")
        call shift_focus (RogueX)
        $ RogueX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (RogueX)
                    $ counter += 1
                    $ Round -= 1
                    jump Rogue_IA_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (RogueX, "menu")
                    jump Rogue_IA_Cycle
                "Other options":

                    menu:
                        "Offhand action":
                            if RogueX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ RogueX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (RogueX, "tired")
                        "Shift primary action":

                            if RogueX.remaining_actions and multi_action:
                                menu:
                                    "Pull out and start rubbing again.":
                                        $ action_context = "pullback"
                                        call Rogue_IA_After
                                        call Rogue_Fondle_Ass
                                    "I want to lick your asshole.":
                                        $ action_context = "shift"
                                        call Rogue_IA_After
                                        call Rogue_Lick_Ass
                                    "Just start licking.":
                                        $ action_context = "auto"
                                        call Rogue_IA_After
                                        call Rogue_Lick_Ass
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Rogue_IA_After
                                        call Rogue_Dildo_Ass
                                    "Never Mind":
                                        jump Rogue_IA_Cycle
                            else:
                                call Sex_Basic_Dialog (RogueX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Rogue_IA_After
                            call Offhand_Set
                        "Shift your focus (locked)" if not offhand_action:
                            pass

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [RogueX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (RogueX)
                                "Ask [RogueX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (RogueX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (RogueX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Rogue_IA_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Rogue_IA_Cycle
                                "Never mind":
                                    jump Rogue_IA_Cycle

                        "Show her feet" if not ShowFeet and (RogueX.pose == "doggy" or RogueX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (RogueX.pose == "doggy" or RogueX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [RogueX.name]":

                            call Girl_Undress (RogueX)
                        "Clean up [RogueX.name] (locked)" if not RogueX.Spunk:
                            pass
                        "Clean up [RogueX.name]" if RogueX.Spunk:
                            call Girl_Cleanup (RogueX, "ask")
                        "Never mind":
                            jump Rogue_IA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Rogue_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Rogue_IA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Rogue_Pos_Reset
                    $ Line = 0
                    jump Rogue_IA_After


        if RogueX.underwear or RogueX.PantsNum() >= 6 or RogueX.HoseNum() >= 5:
            call Girl_Undress (RogueX, "auto")

        call shift_focus (RogueX)
        call Sex_Dialog (RogueX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or RogueX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (RogueX)
                if "angry" in RogueX.recent_history:
                    call Rogue_Pos_Reset
                    return
                $ RogueX.change_stat("lust", 200, 5)
                if 100 > RogueX.lust >= 70 and RogueX.session_orgasms < 2:
                    $ RogueX.AddWord(0,"unsatisfied","unsatisfied")

                if Player.focus > 80:
                    jump Rogue_IA_After
                $ Line = "came"

            if RogueX.lust >= 100:

                call Girl_Cumming (RogueX)
                if action_context == "shift" or "angry" in RogueX.recent_history:
                    jump Rogue_IA_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in RogueX.recent_history:
                    "[RogueX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Rogue_IA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif counter == (5 + RogueX.action_counter["finger_ass"]):
            $ RogueX.brows = "confused"
            ch_r "What are you even doing down there?"
        elif RogueX.lust >= 80:
            pass
        elif counter == (15 + RogueX.action_counter["finger_ass"]) and RogueX.SEXP >= 15 and not ApprovalCheck(RogueX, 1500):
            $ RogueX.brows = "confused"
            menu:
                ch_r "[RogueX.player_petname], this is getting uncomfortable, maybe we could try something else."
                "Finish up.":
                    "You let go. . ."
                    jump Rogue_IA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Rogue_IA_After
                "No, this is fun.":
                    if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):
                        $ RogueX.change_stat("love", 200, -5)
                        $ RogueX.change_stat("obedience", 50, 3)
                        $ RogueX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ RogueX.change_face("angry", 1)
                        call Rogue_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_r "Well if that's your attitude, I don't need your \"help\"."
                        $ RogueX.change_stat("love", 50, -3, 1)
                        $ RogueX.change_stat("love", 80, -4, 1)
                        $ RogueX.change_stat("obedience", 30, -1, 1)
                        $ RogueX.change_stat("obedience", 50, -1, 1)
                        $ RogueX.AddWord(1,"angry","angry")
                        jump Rogue_IA_After


        call Escalation (RogueX)

        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."


    $ RogueX.change_face("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.player_petname], that's enough of that for now."


label Rogue_IA_After:
    if not action_context:
        call Rogue_Pos_Reset

    $ RogueX.change_face("sexy")

    $ RogueX.action_counter["finger_ass"] += 1
    $ RogueX.remaining_actions -=1
    $ RogueX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ RogueX.addiction_rate += 1

    call Partner_Like (RogueX, 2)

    if RogueX.action_counter["finger_ass"] == 1:
        $ RogueX.SEXP += 12
        if not action_context:
            if RogueX.love >= 500 and "unsatisfied" not in RogueX.recent_history:
                ch_r "That felt. . . interesting. . ."
            elif RogueX.obedience <= 500 and Player.focus <= 20:
                $ RogueX.change_face("perplexed", 1)
                ch_r "Did you like that?"

    $ approval_bonus = 0
    call checkout
    return








label Rogue_Lick_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (RogueX)

    if RogueX.action_counter["eat_ass"]:
        $ approval_bonus += 20
    if RogueX.PantsNum() >= 6 or RogueX.HoseNum() >= 5:
        $ approval_bonus -= 25
    if RogueX.lust > 95:
        $ approval_bonus += 20
    elif RogueX.lust > 85:
        $ approval_bonus += 15
    if RogueX.lust > 85 and action_context == "auto":
        $ approval_bonus += 10
    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in RogueX.Traits:
        $ approval_bonus += (4*Taboo)
    if RogueX in Player.Harem or "sex friend" in RogueX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in RogueX.Traits:
        $ approval_bonus -= 25
    if RogueX.event_counter["forced"] and not RogueX.Forced:
        $ approval_bonus -= 5*RogueX.event_counter["forced"]

    if Taboo and "no_taboo" in RogueX.daily_history:
        $ approval_bonus -= 10

    if "no_lick ass" in RogueX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_lick ass" in RogueX.recent_history else 0

    $ Approval = ApprovalCheck(RogueX, 1550, TabM = 4)

    if action_context == "auto":
        if Approval:
            $ RogueX.change_face("surprised")
            $ RogueX.change_stat("obedience", 90, 1)
            $ RogueX.change_stat("inhibition", 80, 3)
            $ RogueX.change_stat("inhibition", 40, 2)
            "As you crouch down and start to lick her asshole, [RogueX.name] startles briefly, but then begins to melt."
            $ RogueX.change_face("sexy")
            jump Rogue_LA_Prep
        else:
            $ RogueX.change_face("surprised")
            $ RogueX.change_stat("love", 80, -2)
            $ RogueX.change_stat("obedience", 50, -3)
            ch_r "Um, no, I'm not really. . . don't."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "eat_ass" in RogueX.recent_history:
        $ RogueX.change_face("sexy", 1)
        ch_r "Mmm, again? Ok."
        jump Rogue_LA_Prep
    elif "eat_ass" in RogueX.daily_history:
        $ RogueX.change_face("sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "I'm still tingling a bit from earlier.",
            "Mmm. . ."])
        ch_r "[Line]"


    if Approval >= 2:
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
            $ RogueX.change_stat("obedience", 90, 2)
            $ RogueX.change_stat("inhibition", 60, 2)
            ch_r "Sure, get in there."
        else:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.eyes = "closed"
            $ RogueX.change_stat("love", 90, 1)
            $ RogueX.change_stat("inhibition", 60, 2)
            $ RogueX.change_stat("lust", 200, 3)
            ch_r "Oooooooh. . ."
        $ RogueX.change_stat("obedience", 20, 1)
        $ RogueX.change_stat("obedience", 60, 1)
        $ RogueX.change_stat("inhibition", 80, 2)
        jump Rogue_LA_Prep
    else:

        $ RogueX.change_face("angry", 1)
        if "no_lick ass" in RogueX.recent_history:
            ch_r "I {i}just{/i} told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history and "no_lick ass" in RogueX.daily_history:
            ch_r "I told you not to touch me like that in public!"
        elif "no_lick ass" in RogueX.daily_history:
            ch_r "I already told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "I told you not in public!"
        elif not RogueX.action_counter["eat_ass"]:
            $ RogueX.change_face("bemused", 1)
            if RogueX.love >= RogueX.obedience and RogueX.love >= RogueX.inhibition:
                ch_r "I'm not really sure I want you lick'in down there. . ."
            elif RogueX.obedience >= RogueX.inhibition:
                ch_r "You really don't have to if you don't want to."
            else:
                $ RogueX.eyes = "sexy"
                ch_r "Hmm. . . it's worth a shot. . ."
        else:
            $ RogueX.change_face("bemused")
            ch_r "Not now, [RogueX.player_petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no_lick ass" in RogueX.daily_history:
                $ RogueX.change_face("bemused")
                ch_r "Yeah, ok, [RogueX.player_petname]."
                return
            "I'm sure I can convince you later. . ." if "no_lick ass" not in RogueX.daily_history:
                $ RogueX.change_face("sexy")
                ch_r "Anything's possible, [RogueX.player_petname]."
                $ RogueX.change_stat("love", 80, 2)
                $ RogueX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ RogueX.AddWord(1,"no_taboo","no_taboo")
                $ RogueX.recent_history.append("no_lick ass")
                $ RogueX.daily_history.append("no_lick ass")
                return
            "I think you'd really enjoy it. . .":
                if Approval:
                    $ RogueX.change_face("sexy")
                    $ RogueX.change_stat("obedience", 90, 2)
                    $ RogueX.change_stat("obedience", 50, 2)
                    ch_r "Ok, you're probably right. . ."
                    $ RogueX.change_stat("inhibition", 70, 3)
                    $ RogueX.change_stat("inhibition", 40, 2)
                    jump Rogue_LA_Prep
                else:
                    $ RogueX.change_face("sexy")
                    ch_r "Tsk, not this time, [RogueX.player_petname], that just seems. . . dirty."
            "[[Start licking anyway]":

                $ Approval = ApprovalCheck(RogueX, 1100, "OI", TabM = 4)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.change_face("sad")
                    $ RogueX.change_stat("love", 70, -5, 1)
                    $ RogueX.change_stat("love", 200, -2)
                    ch_r "Ok, get in there if you're so determined."
                    $ RogueX.change_stat("obedience", 50, 4)
                    $ RogueX.change_stat("inhibition", 80, 1)
                    $ RogueX.change_stat("inhibition", 60, 3)
                    if Approval < 2:
                        $ RogueX.Forced = 1
                    jump Rogue_LA_Prep
                else:
                    $ RogueX.change_stat("love", 200, -15)
                    $ RogueX.change_face("angry", 1)
                    "She shoves your head back."
                    $ RogueX.AddWord(1,"angry","angry")

    if "no_lick ass" in RogueX.daily_history:
        ch_r "Learn to take \"no\" for an answer, [RogueX.player_petname]."
        $ RogueX.AddWord(1,"angry","angry")
    elif RogueX.Forced:
        $ RogueX.change_face("angry", 1)
        ch_r "Ew, no way."
        if ApprovalCheck(RogueX, 500, "I"):
            $ RogueX.change_stat("lust", 80, 10)
        else:
            $ RogueX.change_stat("lust", 50, 3)
        $ RogueX.change_stat("obedience", 50, -2)
        $ RogueX.AddWord(1,"angry","angry")
    elif Taboo:
        $ RogueX.change_face("angry", 1)
        $ RogueX.AddWord(1,"no_taboo","no_taboo")
        ch_r "This just really isn't the time or place, [RogueX.player_petname]!"
    elif RogueX.action_counter["eat_pussy"]:
        $ RogueX.change_face("sad")
        ch_r "Sorry, keep your tongue in your mouth."
    else:
        $ RogueX.change_face("surprised")
        ch_r "What?! Gross!"
        $ RogueX.change_face()
    $ RogueX.recent_history.append("no_lick ass")
    $ RogueX.daily_history.append("no_lick ass")
    $ approval_bonus = 0
    return

label Rogue_LA_Prep:
    if offhand_action == "eat_ass":
        return
    if not RogueX.Forced and action_context != "auto":
        $ approval_bonus = 0
        if RogueX.PantsNum() >= 6:
            $ approval_bonus = 15
        call Bottoms_Off (RogueX)
        if "angry" in RogueX.recent_history:
            return
    $ approval_bonus = 0
    call Rogue_Pussy_Launch ("eat_ass")
    if not RogueX.action_counter["eat_ass"]:
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -30)
            $ RogueX.change_stat("obedience", 70, 40)
            $ RogueX.change_stat("inhibition", 80, 80)
        else:
            $ RogueX.change_stat("love", 90, 35)
            $ RogueX.change_stat("obedience", 70, 25)
            $ RogueX.change_stat("inhibition", 80, 55)
    if Taboo:
        $ RogueX.inhibition += int(Taboo/10)
        $ RogueX.lust += int(Taboo/5)
    if action_context:
        $ renpy.pop_call()
        $ action_context = 0

    $ RogueX.Upskirt = 1
    if RogueX.PantsNum() == 5:
        $ RogueX.SeenPanties = 1
    call Rogue_First_Bottomless (1)
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ RogueX.DrainWord("no_taboo")
    $ RogueX.DrainWord("no_lick ass")

    $ RogueX.AddWord(1,"lick","lick")
    $ RogueX.AddWord(1,"ass","ass")
    $ RogueX.AddWord(0,"eat_ass","eat_ass")
    call Rogue_Pussy_Launch ("eat_ass")

label Rogue_LA_Cycle:
    if offhand_action == "kiss":
        $ offhand_action = 0
    while Round > 0:
        call ViewShift (RogueX, RogueX.pose, 0, "eat_ass")
        call shift_focus (RogueX)
        $ RogueX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (RogueX)
                    $ counter += 1
                    $ Round -= 1
                    jump Rogue_LA_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (RogueX, "menu")
                    jump Rogue_LA_Cycle
                "Other options":

                    menu:
                        "Offhand action":
                            if RogueX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ RogueX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (RogueX, "tired")
                        "Shift primary action":

                            if RogueX.remaining_actions and multi_action:
                                menu:
                                    "Switch to fondling.":
                                        $ action_context = "pullback"
                                        call Rogue_LA_After
                                        call Rogue_Fondle_Ass
                                    "I want to stick a finger in.":
                                        $ action_context = "shift"
                                        call Rogue_LA_After
                                        call Rogue_Insert_Ass
                                    "Just stick a finger in [[without asking].":
                                        $ action_context = "auto"
                                        call Rogue_LA_After
                                        call Rogue_Insert_Ass
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Rogue_LA_After
                                        call Rogue_Dildo_Ass
                                    "Never Mind":
                                        jump Rogue_LA_Cycle
                            else:
                                call Sex_Basic_Dialog (RogueX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Rogue_LA_After
                            call Offhand_Set
                        "Shift your focus (locked)" if not offhand_action:
                            pass

                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [RogueX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (RogueX)
                                "Ask [RogueX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (RogueX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (RogueX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Rogue_LA_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Rogue_LA_Cycle
                                "Never mind":
                                    jump Rogue_LA_Cycle

                        "Show her feet" if not ShowFeet and (RogueX.pose == "doggy" or RogueX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (RogueX.pose == "doggy" or RogueX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [RogueX.name]":

                            call Girl_Undress (RogueX)
                        "Clean up [RogueX.name] (locked)" if not RogueX.Spunk:
                            pass
                        "Clean up [RogueX.name]" if RogueX.Spunk:
                            call Girl_Cleanup (RogueX, "ask")
                        "Never mind":
                            jump Rogue_LA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Rogue_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Rogue_LA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Rogue_Pos_Reset
                    $ Line = 0
                    jump Rogue_LA_After


        if RogueX.underwear or RogueX.PantsNum() >= 6 or RogueX.HoseNum() >= 5:
            call Girl_Undress (RogueX, "auto")

        call shift_focus (RogueX)
        call Sex_Dialog (RogueX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or RogueX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (RogueX)
                if "angry" in RogueX.recent_history:
                    call Rogue_Pos_Reset
                    return
                $ RogueX.change_stat("lust", 200, 5)
                if 100 > RogueX.lust >= 70 and RogueX.session_orgasms < 2:
                    $ RogueX.AddWord(0,"unsatisfied","unsatisfied")

                if Player.focus > 80:
                    jump Rogue_LA_After
                $ Line = "came"

            if RogueX.lust >= 100:

                call Girl_Cumming (RogueX)
                if action_context == "shift" or "angry" in RogueX.recent_history:
                    jump Rogue_LA_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."

                if "unsatisfied" in RogueX.recent_history:
                    "[RogueX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Rogue_LA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif counter == (5 + RogueX.action_counter["eat_ass"]):
            $ RogueX.brows = "confused"
            ch_r "What are you even doing down there?"
        elif RogueX.lust >= 80:
            pass
        elif counter == (15 + RogueX.action_counter["eat_ass"]) and RogueX.SEXP >= 15 and not ApprovalCheck(RogueX, 1500):
            $ RogueX.brows = "confused"
            menu:
                ch_r "[RogueX.player_petname], this is getting uncomfortable, maybe we could try something else."
                "Finish up.":
                    "You let go. . ."
                    jump Rogue_LA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Rogue_LA_After
                "No, this is fun.":
                    if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):
                        $ RogueX.change_stat("love", 200, -5)
                        $ RogueX.change_stat("obedience", 50, 3)
                        $ RogueX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ RogueX.change_face("angry", 1)
                        call Rogue_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_r "Well if that's your attitude, I don't need your \"help\"."
                        $ RogueX.change_stat("love", 50, -3, 1)
                        $ RogueX.change_stat("love", 80, -4, 1)
                        $ RogueX.change_stat("obedience", 30, -1, 1)
                        $ RogueX.change_stat("obedience", 50, -1, 1)
                        $ RogueX.AddWord(1,"angry","angry")
                        jump Rogue_LA_After


        call Escalation (RogueX)

        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."


    $ RogueX.change_face("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.player_petname], that's enough of that for now."


label Rogue_LA_After:
    if not action_context:
        call Rogue_Pos_Reset

    $ RogueX.change_face("sexy")

    $ RogueX.action_counter["eat_ass"] += 1
    $ RogueX.remaining_actions -=1
    if RogueX.PantsNum() < 6 or RogueX.Upskirt:
        $ RogueX.addiction_rate += 1
        if "addictive" in Player.Traits:
            $ RogueX.addiction_rate += 1

    call Partner_Like (RogueX, 2)

    if RogueX.action_counter["eat_ass"] == 1:
        $ RogueX.SEXP += 15
        if not action_context:
            if RogueX.love >= 500 and "unsatisfied" not in RogueX.recent_history:
                ch_r "Was. . . that something you liked?"
            elif RogueX.obedience <= 500 and Player.focus <= 20:
                $ RogueX.change_face("perplexed", 1)
                ch_r "Did you like that?"

    $ approval_bonus = 0


    call checkout
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
