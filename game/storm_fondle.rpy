
label Storm_Fondle:

    $ StormX.mouth = "_smile"
    if not StormX.remaining_actions:
        call Sex_Basic_Dialog (StormX, "tired")
        return
    menu:
        ch_s "Where did you want to touch, [StormX.player_petname]?"
        "Your breasts?" if StormX.remaining_actions:
            jump Storm_Fondle_Breasts
        "Your thighs?" if StormX.remaining_actions:
            jump Storm_Fondle_Thighs
        "Your pussy?" if StormX.remaining_actions:
            jump Storm_Fondle_Pussy
        "Your Ass?" if StormX.remaining_actions:
            jump Storm_Fondle_Ass
        "Never mind.":
            return
    return



label Storm_Fondle_Breasts:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (StormX)


    if StormX.action_counter["fondle_breasts"]:
        $ approval_bonus += 15
    if StormX.lust > 75:
        $ approval_bonus += 20
    if "exhibitionist" in StormX.traits:
        $ approval_bonus += (3*Taboo)
    if StormX in Player.Harem or "sex friend" in StormX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in StormX.traits:
        $ approval_bonus -= 20
    if StormX.event_counter["forced"] and not StormX.Forced:
        $ approval_bonus -= 5*StormX.event_counter["forced"]

    if Taboo and "no_taboo" in StormX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in StormX.history:
        $ approval_bonus -= 20

    if "no_fondle breasts" in StormX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle breasts" in StormX.recent_history else 0

    $ approval = approval_check(StormX, 950, TabM = 3)

    if action_context == "auto":
        if approval:
            $ StormX.change_face("_sexy")
            $ StormX.change_stat("obedience", 90, 1)
            $ StormX.change_stat("obedience", 70, 2)
            $ StormX.change_stat("inhibition", 70, 3)
            $ StormX.change_stat("inhibition", 30, 2)
            "As you cup her breast, [StormX.name] gently nods."
            jump Storm_FB_Prep
        else:
            $ StormX.change_face("_surprised")
            $ StormX.brows = "_confused"
            $ StormX.change_stat("obedience", 50, -2)
            ch_s "Probably not, right now. . ."
            $ approval_bonus = 0
            $ offhand_action = 0
            return



    if approval:
        $ StormX.change_face("_sexy", 1)
        if StormX.Forced:
            $ StormX.change_face("_sad")
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
        elif not Taboo and "no_taboo" in StormX.daily_history:
            ch_s "This is a bit more secluded."

    if "fondle_breasts" in StormX.recent_history:
        $ StormX.change_face("_sexy", 1)
        ch_s "Mmmm, again? I suppose. . ."
        jump Storm_FB_Prep
    elif "fondle_breasts" in StormX.daily_history:
        $ StormX.change_face("_sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Gently. . . gently. . .",
            "Mmm. . ."])
        ch_s "[Line]"

    if approval >= 2:
        $ StormX.change_face("_bemused", 1)
        if StormX.Forced:
            $ StormX.change_face("_sad")
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
            $ StormX.change_stat("obedience", 90, 1)
            $ StormX.change_stat("inhibition", 60, 1)
        ch_s "I would love that. . ."
        $ StormX.change_stat("love", 90, 1)
        $ StormX.change_stat("inhibition", 50, 3)
        jump Storm_FB_Prep
    else:

        $ StormX.change_face("_angry", 1)
        if "no_fondle breasts" in StormX.recent_history:
            ch_s "Do not persist in this, [StormX.player_petname]."
        elif "no_fondle breasts" in StormX.daily_history:
            ch_s "I have already told you my answer."
        elif Taboo and "no_taboo" in StormX.daily_history:
            ch_s "This area is too public, [StormX.player_petname]."
        elif not StormX.action_counter["fondle_breasts"]:
            $ StormX.change_face("_bemused")
            ch_s "Perhaps some other time, [StormX.player_petname]. . ."
        else:
            $ StormX.change_face("_bemused")
            ch_s "Hmm, no."
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle breasts" in StormX.daily_history:
                $ StormX.change_face("_bemused")
                ch_s "Don't concern yourself, [StormX.player_petname]."
                return
            "Maybe later?" if "no_fondle breasts" not in StormX.daily_history:
                $ StormX.change_face("_sexy")
                "She re-adjusts her cleavage."
                ch_s "I will give it some thought, [StormX.player_petname]."
                $ StormX.change_stat("love", 80, 1)
                $ StormX.change_stat("love", 50, 1)
                $ StormX.change_stat("inhibition", 30, 2)
                if Taboo:
                    $ StormX.recent_history.append("no_taboo")
                    $ StormX.daily_history.append("no_taboo")
                $ StormX.recent_history.append("no_fondle breasts")
                $ StormX.daily_history.append("no_fondle breasts")
                return
            "Come on, Please?":
                if approval:
                    $ StormX.change_face("_sexy")
                    $ StormX.change_stat("obedience", 90, 1)
                    $ StormX.change_stat("obedience", 50, 2)
                    $ StormX.change_stat("inhibition", 60, 3)
                    $ StormX.change_stat("inhibition", 30, 2)
                    ch_s "Well, I suppose. . ."
                    jump Storm_FB_Prep
                else:
                    $ StormX.change_face("_sexy")
                    ch_s "No, thank you."
            "[[Grab her chest anyway]":


                $ approval = approval_check(StormX, 350, "OI", TabM = 3)
                if approval > 1 or (approval and StormX.Forced):
                    $ StormX.change_face("_sad")
                    $ StormX.change_stat("love", 70, -5, 1)
                    $ StormX.change_stat("love", 20, -2, 1)
                    ch_s "That is not appropriate. . ."
                    ch_s "but neither is it entirely unwelcome. . ."
                    $ StormX.change_stat("obedience", 90, 2)
                    $ StormX.change_stat("obedience", 50, 4)
                    $ StormX.change_stat("inhibition", 60, 3)
                    if approval < 2:
                        $ StormX.Forced = 1
                    jump Storm_FB_Prep
                else:
                    $ StormX.change_stat("love", 200, -10)
                    $ StormX.change_face("_angry", 1)
                    "She slaps your hand away."
                    $ StormX.recent_history.append("_angry")
                    $ StormX.daily_history.append("_angry")

    if "no_fondle breasts" in StormX.daily_history:
        ch_s "I have been clear on this."
        $ StormX.recent_history.append("_angry")
        $ StormX.daily_history.append("_angry")
    elif StormX.Forced:
        $ StormX.change_face("_angry", 1)
        ch_s "You go too far."
        $ StormX.change_stat("lust", 60, 5)
        $ StormX.change_stat("obedience", 50, -2)
        $ StormX.recent_history.append("_angry")
        $ StormX.daily_history.append("_angry")
    elif Taboo:
        $ StormX.change_face("_angry", 1)
        $ StormX.recent_history.append("no_taboo")
        $ StormX.daily_history.append("no_taboo")
        ch_s "I should not be seen doing that."
    elif StormX.action_counter["fondle_breasts"]:
        $ StormX.change_face("_sad")
        ch_s "No, I do not think so."
    else:
        $ StormX.change_face("_sexy")
        $ StormX.mouth = "_sad"
        ch_s "No, I do not think so."
    $ StormX.recent_history.append("no_fondle breasts")
    $ StormX.daily_history.append("no_fondle breasts")
    $ approval_bonus = 0
    return


label Storm_FB_Prep:
    if primary_action == "kiss":
        $ primary_action = "fondle_breasts"
        return

    if offhand_action == "fondle_breasts":
        return

    call Storm_Breasts_Launch ("fondle_breasts")

    if action_context == StormX:

        $ action_context = 0
        if (StormX.top or StormX.bra) and not StormX.top_pulled_up:

            if approval_check(StormX, 1250, TabM = 1) or (StormX.SeenChest and approval_check(StormX, 500) and not Taboo):
                $ StormX.top_pulled_up = 1
                $ Line = StormX.top if StormX.top else StormX.bra
                "With a devilish grin, [StormX.name] pulls her [Line] up over her breasts."
                call Storm_First_Topless (1)
                $ Line = 0
                "She then grabs your arm and mashes your hand against her breast, clearly intending you to get to work."
            else:
                "[StormX.name] grabs your arm and mashes your hand against her covered breast, clearly intending you to get to work."
        else:
            "[StormX.name] grabs your arm and mashes your hand against her breast, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ StormX.change_stat("inhibition", 80, 3)
                $ StormX.change_stat("inhibition", 50, 2)
                "You start to fondle it."
            "Praise her.":
                $ StormX.change_face("_sexy", 1)
                $ StormX.change_stat("inhibition", 80, 3)
                ch_p "I like the initiative, [StormX.petname]."
                $ StormX.nameCheck()
                "You start to fondle it."
                $ StormX.change_stat("love", 85, 1)
                $ StormX.change_stat("obedience", 90, 1)
                $ StormX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your hand back."
                $ StormX.change_face("_surprised")
                $ StormX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [StormX.petname]."
                $ StormX.nameCheck()
                "[StormX.name] pulls back."
                $ StormX.change_stat("obedience", 90, 1)
                $ StormX.change_stat("obedience", 50, 1)
                $ StormX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ StormX.add_word(1,"refused","refused")
                return


    if not StormX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Top_Off (StormX)
        if "_angry" in StormX.recent_history:
            return
    $ approval_bonus = 0
    if not StormX.action_counter["fondle_breasts"]:
        if StormX.Forced:
            $ StormX.change_stat("love", 90, -20)
            $ StormX.change_stat("obedience", 70, 25)
            $ StormX.change_stat("inhibition", 80, 15)
        else:
            $ StormX.change_stat("love", 90, 10)
            $ StormX.change_stat("obedience", 70, 5)
            $ StormX.change_stat("inhibition", 80, 15)

    if Taboo:
        $ StormX.inhibition += int(Taboo/10)
        $ StormX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ StormX.drain_word("no_taboo")
    $ StormX.drain_word("no_fondle breasts")
    $ StormX.recent_history.append("fondle_breasts")
    $ StormX.daily_history.append("fondle_breasts")
    call Storm_Breasts_Launch ("fondle_breasts")

label Storm_FB_Cycle:
    while Round > 0:
        call ViewShift (StormX, StormX.pose, 0, "fondle_breasts")
        call shift_focus (StormX)
        $ StormX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (StormX)
                    $ counter += 1
                    $ Round -= 1
                    jump Storm_FB_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (StormX, "menu")
                    jump Storm_FB_Cycle
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
                                    "Ask to suck on them.":
                                        if StormX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Storm_FB_After
                                            call Storm_Suck_Breasts
                                        else:
                                            call Sex_Basic_Dialog (StormX, "tired")
                                    "Just suck on them without asking.":
                                        if StormX.remaining_actions and multi_action:
                                            $ action_context = "auto"
                                            call Storm_FB_After
                                            call Storm_Suck_Breasts
                                        else:
                                            "As you lean in to suck on her breast, she grabs your head and pushes back."
                                            call Sex_Basic_Dialog (StormX, "tired")
                                    "Never Mind":
                                        jump Storm_FB_Cycle
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
                                    jump Storm_FB_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Storm_FB_Cycle
                                "Never mind":
                                    jump Storm_FB_Cycle

                        "Show her feet" if not ShowFeet and (StormX.pose == "doggy" or StormX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (StormX.pose == "doggy" or StormX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [StormX.name]":

                            call Girl_Undress (StormX)
                        "Clean up [StormX.name] (locked)" if not StormX.spunk:
                            pass
                        "Clean up [StormX.name]" if StormX.spunk:
                            call Girl_Cleanup (StormX, "ask")
                        "Never mind":
                            jump Storm_FB_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Storm_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Storm_FB_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Storm_Pos_Reset
                    $ Line = 0
                    jump Storm_FB_After


        call shift_focus (StormX)
        call Sex_Dialog (StormX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or StormX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (StormX)
                if "_angry" in StormX.recent_history:
                    call Storm_Pos_Reset
                    return
                $ StormX.change_stat("lust", 200, 5)
                if 100 > StormX.lust >= 70 and StormX.session_orgasms < 2 and StormX.SEXP >= 20:
                    $ StormX.recent_history.append("unsatisfied")
                    $ StormX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Storm_FB_After
                $ Line = "came"

            if StormX.lust >= 100:

                call Girl_Cumming (StormX)
                if action_context == "shift" or "_angry" in StormX.recent_history:
                    jump Storm_FB_After

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
                            jump Storm_FB_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if StormX.SEXP >= 100 or approval_check(StormX, 1200, "LO"):
            pass
        elif counter == (5 + StormX.action_counter["fondle_breasts"]):
            $ StormX.brows = "_confused"
            ch_s "You really seem to enjoy those. . ."
        elif StormX.lust >= 85:
            pass
        elif counter == (15 + StormX.action_counter["fondle_breasts"]) and StormX.SEXP >= 15 and not approval_check(StormX, 1500):
            $ StormX.brows = "_confused"
            menu:
                ch_s "I am sure that is fun, but could we try something different?"
                "Finish up.":
                    "You let go. . ."
                    jump Storm_FB_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Storm_FB_After
                "No, this is fun.":
                    if approval_check(StormX, 1200) or approval_check(StormX, 500, "O"):
                        $ StormX.change_stat("love", 200, -5)
                        $ StormX.change_stat("obedience", 50, 3)
                        $ StormX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ StormX.change_face("_angry", 1)
                        call Storm_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_s "Well however much you are enjoying yourself, I need to take a break."
                        $ StormX.change_stat("love", 50, -3, 1)
                        $ StormX.change_stat("love", 80, -4, 1)
                        $ StormX.change_stat("obedience", 30, -1, 1)
                        $ StormX.change_stat("obedience", 50, -1, 1)
                        $ StormX.recent_history.append("_angry")
                        $ StormX.daily_history.append("_angry")
                        jump Storm_FB_After


        call Escalation (StormX)

        if Round == 10:
            call Sex_Basic_Dialog (StormX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (StormX, 5)

        if StormX.lust >= 50 and not StormX.top_pulled_up and (StormX.bra or StormX.top):
            $ StormX.top_pulled_up = 1
            "[StormX.name] sighs and tugs her breasts free of her clothes."
            call Storm_First_Topless


    $ StormX.change_face("_bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (StormX, "done")

label Storm_FB_After:
    if not action_context:
        call Storm_Pos_Reset

    $ StormX.change_face("_sexy")

    $ StormX.action_counter["fondle_breasts"]+= 1
    $ StormX.remaining_actions -=1
    $ StormX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ StormX.addiction_rate += 1

    call Partner_Like (StormX, 2)

    if StormX.action_counter["fondle_breasts"]== 1:
        $ StormX.SEXP += 4
        if not action_context:
            if StormX.love >= 500 and "unsatisfied" not in StormX.recent_history:
                ch_s "That was quite fun. . ."
            elif StormX.obedience <= 500 and Player.focus <= 20:
                $ StormX.change_face("_perplexed", 1)
                ch_s "I expect you enjoyed that. . ."

    $ approval_bonus = 0


    call checkout
    return






label Storm_Suck_Breasts:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (StormX)

    if StormX.action_counter["suck_breasts"]:
        $ approval_bonus += 15
    if not StormX.bra and not StormX.top:
        $ approval_bonus += 15
    if StormX.lust > 75:
        $ approval_bonus += 20
    if StormX.lust > 75 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in StormX.traits:
        $ approval_bonus += (4*Taboo)
    if StormX in Player.Harem or "sex friend" in StormX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in StormX.traits:
        $ approval_bonus -= 25
    if StormX.event_counter["forced"] and not StormX.Forced:
        $ approval_bonus -= 5*StormX.event_counter["forced"]

    if Taboo and "no_taboo" in StormX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in StormX.history:
        $ approval_bonus -= 20

    if "no_suck breasts" in StormX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_suck breasts" in StormX.recent_history else 0

    $ approval = approval_check(StormX, 1050, TabM = 4)

    if action_context == "auto":
        if approval:
            $ StormX.change_face("_sexy")
            $ StormX.change_stat("obedience", 90, 1)
            $ StormX.change_stat("obedience", 70, 2)
            $ StormX.change_stat("inhibition", 70, 3)
            $ StormX.change_stat("inhibition", 30, 2)
            "As you dive in, [StormX.name] seems a bit surprised, but just makes a little \"growl.\""
            jump Storm_SB_Prep
        else:
            $ StormX.change_face("_surprised")
            $ StormX.change_stat("obedience", 50, -2)
            ch_s "Show some self control. . ."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "suck_breasts" in StormX.recent_history:
        $ StormX.change_face("_sexy", 1)
        ch_s "Mmmm, again? I suppose. . ."
        jump Storm_SB_Prep
    elif "suck_breasts" in StormX.daily_history:
        $ StormX.change_face("_sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax, gently. . .",
            "Mmm. . ."])
        ch_s "[Line]"

    if approval >= 2:
        $ StormX.change_face("_bemused", 1)
        if StormX.Forced:
            $ StormX.change_face("_sad")
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
            $ StormX.change_stat("obedience", 90, 1)
            $ StormX.change_stat("inhibition", 60, 1)
        ch_s "Oh very well. . ."
        $ StormX.change_stat("love", 90, 1)
        $ StormX.change_stat("inhibition", 50, 3)
        jump Storm_SB_Prep
    else:

        $ StormX.change_face("_angry", 1)
        if "no_suck breasts" in StormX.recent_history:
            ch_s "Your persistance is doing you no favors, [StormX.player_petname]."
        elif "no_suck breasts" in StormX.daily_history:
            ch_s "I have already told you my answer."
        elif Taboo and "no_taboo" in StormX.daily_history:
            ch_s "As I said, not here, [StormX.player_petname]."
        elif not StormX.action_counter["suck_breasts"]:
            $ StormX.change_face("_bemused")
            ch_s "Mmm. . . that would. . . no. . ."
        else:
            $ StormX.change_face("_bemused")
            ch_s "Hmm, no."
        menu:
            extend ""
            "Sorry, never mind." if "no_suck breasts" in StormX.daily_history:
                $ StormX.change_face("_bemused")
                ch_s "No offense taken. I get it."
                return
            "Maybe later?" if "no_suck breasts" not in StormX.daily_history:
                $ StormX.change_face("_sexy")
                ch_s "I will give it some thought, [StormX.player_petname]."
                $ StormX.change_stat("love", 80, 1)
                $ StormX.change_stat("love", 50, 1)
                $ StormX.change_stat("inhibition", 30, 2)
                if Taboo:
                    $ StormX.recent_history.append("no_taboo")
                    $ StormX.daily_history.append("no_taboo")
                $ StormX.recent_history.append("no_suck breasts")
                $ StormX.daily_history.append("no_suck breasts")
                return
            "Come on, Please?":
                if approval:
                    $ StormX.change_face("_sexy")
                    $ StormX.change_stat("obedience", 90, 1)
                    $ StormX.change_stat("obedience", 50, 2)
                    $ StormX.change_stat("inhibition", 60, 3)
                    $ StormX.change_stat("inhibition", 30, 2)
                    ch_s "Oh, if you insist. . ."
                    jump Storm_SB_Prep
                else:
                    $ StormX.change_face("_sexy")
                    ch_s "No, I do not think so. . ."
            "[[Start sucking anyway]":

                $ approval = approval_check(StormX, 450, "OI", TabM = 3)
                if approval > 1 or (approval and StormX.Forced):
                    $ StormX.change_face("_sad")
                    $ StormX.change_stat("love", 70, -5, 1)
                    $ StormX.change_stat("love", 20, -2, 1)
                    ch_s "Only if you do a good job. . ."
                    $ StormX.change_stat("obedience", 90, 2)
                    $ StormX.change_stat("obedience", 50, 4)
                    $ StormX.change_stat("inhibition", 60, 3)
                    if approval < 2:
                        $ StormX.Forced = 1
                    jump Storm_SB_Prep
                else:
                    $ StormX.change_stat("love", 200, -10)
                    $ StormX.change_face("_angry", 1)
                    "She shoves your head back out."
                    $ StormX.recent_history.append("_angry")
                    $ StormX.daily_history.append("_angry")

    if "no_suck breasts" in StormX.daily_history:
        ch_s "I have been clear on this."
        $ StormX.recent_history.append("_angry")
        $ StormX.daily_history.append("_angry")
    elif StormX.Forced:
        $ StormX.change_face("_angry", 1)
        ch_s "You go too far."
        $ StormX.change_stat("lust", 60, 5)
        $ StormX.change_stat("obedience", 50, -2)
        $ StormX.recent_history.append("_angry")
        $ StormX.daily_history.append("_angry")
    elif Taboo:
        $ StormX.change_face("_angry", 1)
        $ StormX.recent_history.append("no_taboo")
        $ StormX.daily_history.append("no_taboo")
        ch_s "I should not be seen doing that."
    elif StormX.action_counter["suck_breasts"]:
        $ StormX.change_face("_sad")
        ch_s "No, I do not think so."
    else:
        $ StormX.change_face("_sexy")
        $ StormX.mouth = "_sad"
        ch_s "No, I do not think so."
    $ StormX.recent_history.append("no_suck breasts")
    $ StormX.daily_history.append("no_suck breasts")
    $ approval_bonus = 0
    return


label Storm_SB_Prep:

    if offhand_action == "suck_breasts":
        return

    call Storm_Breasts_Launch ("suck_breasts")

    if action_context == StormX:

        $ action_context = 0
        if (StormX.top or StormX.bra) and not StormX.top_pulled_up:

            if approval_check(StormX, 1250, TabM = 1) or (StormX.SeenChest and approval_check(StormX, 500) and not Taboo):
                $ StormX.top_pulled_up = 1
                $ Line = StormX.top if StormX.top else StormX.bra
                "With a devilish grin, [StormX.name] pulls her [Line] up over her breasts."
                call Storm_First_Topless (1)
                $ Line = 0
                "She then grabs your head and crams your face into her chest, clearly intending you to get to work."
            else:
                "[StormX.name] grabs your head and crams your face into her chest, clearly intending you to get to work."
        else:
            "[StormX.name] grabs your head and crams your face into her chest, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ StormX.change_stat("inhibition", 80, 3)
                $ StormX.change_stat("inhibition", 50, 2)
                "You start to run your tongue along her nipple."
            "Praise her.":
                $ StormX.change_face("_sexy", 1)
                $ StormX.change_stat("inhibition", 80, 3)
                ch_p "Mmm, I like this, [StormX.petname]."
                $ StormX.nameCheck()
                "You start to fondle it."
                $ StormX.change_stat("love", 85, 1)
                $ StormX.change_stat("obedience", 90, 1)
                $ StormX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your head back."
                $ StormX.change_face("_surprised")
                $ StormX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [StormX.petname]."
                $ StormX.nameCheck()
                "[StormX.name] pulls away."
                $ StormX.change_stat("obedience", 90, 1)
                $ StormX.change_stat("obedience", 50, 1)
                $ StormX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ StormX.add_word(1,"refused","refused")
                return

    if not StormX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Top_Off (StormX)
        if "_angry" in StormX.recent_history:
            return

    $ approval_bonus = 0
    if not StormX.action_counter["suck_breasts"]:
        if StormX.Forced:
            $ StormX.change_stat("love", 90, -25)
            $ StormX.change_stat("obedience", 70, 25)
            $ StormX.change_stat("inhibition", 80, 17)
        else:
            $ StormX.change_stat("love", 90, 10)
            $ StormX.change_stat("obedience", 70, 10)
            $ StormX.change_stat("inhibition", 80, 15)

    if Taboo:
        $ StormX.inhibition += int(Taboo/10)
        $ StormX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ StormX.drain_word("no_taboo")
    $ StormX.drain_word("no_suck breasts")
    $ StormX.recent_history.append("suck_breasts")
    $ StormX.daily_history.append("suck_breasts")
    call Storm_Breasts_Launch ("suck_breasts")

label Storm_SB_Cycle:
    if offhand_action == "kiss":
        $ offhand_action = 0
    while Round > 0:
        $ primary_action = "suck_breasts"
        call ViewShift (StormX, StormX.pose, 0, "suck_breasts")
        call shift_focus (StormX)
        $ StormX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (StormX)
                    $ counter += 1
                    $ Round -= 1
                    jump Storm_SB_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (StormX, "menu")
                    jump Storm_SB_Cycle
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
                                    "Pull back to fondling.":
                                        if StormX.remaining_actions and multi_action:
                                            $ action_context = "pullback"
                                            call Storm_SB_After
                                            call Storm_Fondle_Breasts
                                        else:
                                            "As you pull back, [StormX.name] pushes you back in close."
                                            call Sex_Basic_Dialog (StormX, "tired")
                                    "Never Mind":
                                        jump Storm_SB_Cycle
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
                                    jump Storm_SB_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Storm_SB_Cycle
                                "Never mind":
                                    jump Storm_SB_Cycle

                        "Show her feet" if not ShowFeet and (StormX.pose == "doggy" or StormX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (StormX.pose == "doggy" or StormX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [StormX.name]":

                            call Girl_Undress (StormX)
                        "Clean up [StormX.name] (locked)" if not StormX.spunk:
                            pass
                        "Clean up [StormX.name]" if StormX.spunk:
                            call Girl_Cleanup (StormX, "ask")
                        "Never mind":
                            jump Storm_SB_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Storm_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Storm_SB_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Storm_Pos_Reset
                    $ Line = 0
                    jump Storm_SB_After


        call shift_focus (StormX)
        call Sex_Dialog (StormX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or StormX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (StormX)
                if "_angry" in StormX.recent_history:
                    call Storm_Pos_Reset
                    return
                $ StormX.change_stat("lust", 200, 5)
                if 100 > StormX.lust >= 70 and StormX.session_orgasms < 2:
                    $ StormX.recent_history.append("unsatisfied")
                    $ StormX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Storm_SB_After
                $ Line = "came"

            if StormX.lust >= 100:

                call Girl_Cumming (StormX)
                if action_context == "shift" or "_angry" in StormX.recent_history:
                    jump Storm_SB_After

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
                            jump Storm_SB_After
        if Partner:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if StormX.SEXP >= 100 or approval_check(StormX, 1200, "LO"):
            pass
        elif counter == (5 + StormX.action_counter["suck_breasts"]):
            $ StormX.brows = "_sly"
            ch_s "You really seem to enjoy those. . ."
        elif StormX.lust >= 85:
            pass
        elif counter == (15 + StormX.action_counter["suck_breasts"]) and StormX.SEXP >= 15 and not approval_check(StormX, 1500):
            $ StormX.brows = "_confused"
            menu:
                ch_s "I am sure that is fun, but could we try something different?"
                "Finish up.":
                    "You let go. . ."
                    jump Storm_SB_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Storm_SB_After
                "No, this is fun.":
                    if approval_check(StormX, 1200) or approval_check(StormX, 500, "O"):
                        $ StormX.change_stat("love", 200, -5)
                        $ StormX.change_stat("obedience", 50, 3)
                        $ StormX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ StormX.change_face("_angry", 1)
                        call Storm_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_s "Well however much you are enjoying yourself, I need to take a break."
                        $ StormX.change_stat("love", 50, -3, 1)
                        $ StormX.change_stat("love", 80, -4, 1)
                        $ StormX.change_stat("obedience", 30, -1, 1)
                        $ StormX.change_stat("obedience", 50, -1, 1)
                        $ StormX.recent_history.append("_angry")
                        $ StormX.daily_history.append("_angry")
                        jump Storm_SB_After


        if Round == 10:
            call Sex_Basic_Dialog (StormX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (StormX, 5)

        if StormX.lust >= 50 and not StormX.top_pulled_up and (StormX.bra or StormX.top):
            $ StormX.top_pulled_up = 1
            "[StormX.name] sighs and tugs her breasts free of her clothes."
            call Storm_First_Topless


    $ StormX.change_face("_bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (StormX, "done")

label Storm_SB_After:
    if not action_context:
        call Storm_Pos_Reset

    $ StormX.change_face("_sexy")

    $ StormX.action_counter["suck_breasts"] += 1
    $ StormX.remaining_actions -=1
    $ StormX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ StormX.addiction_rate += 1

    if Partner == "Kitty":
        call Partner_Like (StormX, 2, 2)
    else:
        call Partner_Like (StormX, 2)

    if StormX.action_counter["suck_breasts"] == 1:
        $ StormX.SEXP += 4
        if not action_context:
            if StormX.love >= 500 and "unsatisfied" not in StormX.recent_history:
                ch_s "That was certainly enjoyable."
            elif StormX.obedience <= 500 and Player.focus <= 20:
                $ StormX.change_face("_perplexed", 1)
                ch_s "Did you get enough?"

    $ approval_bonus = 0


    call checkout
    return





label Storm_Fondle_Thighs:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (StormX)

    if StormX.action_counter["fondle_thighs"]:
        $ approval_bonus += 10
    if StormX.PantsNum() > 6 or StormX.HoseNum() >= 5:
        $ approval_bonus -= 5
    if StormX.lust > 75:
        $ approval_bonus += 10
    if "exhibitionist" in StormX.traits:
        $ approval_bonus += Taboo
    if StormX in Player.Harem or "sex friend" in StormX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in StormX.traits:
        $ approval_bonus -= 25
    if StormX.event_counter["forced"] and not StormX.Forced:
        $ approval_bonus -= 5*StormX.event_counter["forced"]

    if Taboo and "no_taboo" in StormX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in StormX.history:
        $ approval_bonus -= 20

    if "no_fondle thighs" in StormX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle thighs" in StormX.recent_history else 0

    $ approval = approval_check(StormX, 700, TabM=1)

    if action_context == "auto":
        if approval:
            $ StormX.change_face("_sexy")
            $ StormX.change_stat("obedience", 50, 1)
            $ StormX.change_stat("inhibition", 30, 2)
            "As you caress her thigh, [StormX.name] glances at you, and smiles."
            jump Storm_FT_Prep
        else:
            $ StormX.change_face("_surprised")
            $ StormX.change_stat("obedience", 50, -2)
            ch_s "Perhaps we keep it above the waist, [StormX.player_petname]."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if action_context == "pullback":
        $ StormX.change_face("_surprised")
        $ StormX.brows = "_sad"
        if StormX.lust > 60:
            $ StormX.change_stat("love", 70, -3)
        $ StormX.change_stat("obedience", 90, 1)
        $ StormX.change_stat("obedience", 70, 2)
        "As you pull back, [StormX.name] looks a little sad."
        jump Storm_FT_Prep
    elif "fondle_thighs" in StormX.recent_history:
        $ StormX.change_face("_sexy", 1)
        ch_s "Mmmm, again? I suppose. . ."
        jump Storm_FT_Prep
    elif "fondle_thighs" in StormX.daily_history:
        $ StormX.change_face("_sexy", 1)
        ch_s "You didn't get enough earlier?"

    if approval >= 2:
        $ StormX.change_face("_bemused", 1)
        if StormX.Forced:
            $ StormX.change_face("_sad")
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("obedience", 90, 1)
            $ StormX.change_stat("inhibition", 60, 1)
        ch_s "Ok [StormX.player_petname], go ahead."
        $ StormX.change_stat("love", 90, 1)
        $ StormX.change_stat("inhibition", 50, 3)
        jump Storm_FT_Prep
    else:

        $ StormX.change_face("_angry", 1)
        if "no_fondle thighs" in StormX.recent_history:
            ch_s "Do not persist in this, [StormX.player_petname]."
        elif Taboo and "no_taboo" in StormX.daily_history and "no_fondle thighs" in StormX.daily_history:
            ch_s "I told you not to touch me like that in public!"
        elif "no_fondle thighs" in StormX.daily_history:
            ch_s "I believe you know my answer on this matter."
        elif Taboo and "no_taboo" in StormX.daily_history:
            ch_s "As I said, not here, [StormX.player_petname]."
        elif not StormX.action_counter["fondle_thighs"]:
            $ StormX.change_face("_bemused")
            ch_s "I would rather you did not, [StormX.player_petname]."
        else:
            $ StormX.change_face("_bemused")
            ch_s "Hmm, no."
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle thighs" in StormX.daily_history:
                $ StormX.change_face("_bemused")
                ch_s "I appreciate your restraint."
                return
            "Maybe later?" if "no_fondle thighs" not in StormX.daily_history:
                $ StormX.change_face("_sexy")
                ch_s "I will give it some thought, [StormX.player_petname]."
                $ StormX.change_stat("love", 80, 1)
                $ StormX.change_stat("inhibition", 30, 2)
                if Taboo:
                    $ StormX.recent_history.append("no_taboo")
                    $ StormX.daily_history.append("no_taboo")
                $ StormX.recent_history.append("no_fondle thighs")
                $ StormX.daily_history.append("no_fondle thighs")
                return
            "Come on, Please?":
                if approval:
                    $ StormX.change_face("_sexy")
                    $ StormX.change_stat("obedience", 60, 1)
                    $ StormX.change_stat("obedience", 30, 2)
                    $ StormX.change_stat("inhibition", 50, 1)
                    $ StormX.change_stat("inhibition", 30, 2)
                    ch_s "I suppose it does not hurt. . ."
                    jump Storm_FT_Prep
                else:
                    $ StormX.change_face("_sexy")
                    ch_s "It is not appropriate."
            "[[Start caressing her thigh anyway]":

                $ approval = approval_check(StormX, 350, "OI", TabM = 2)
                if approval > 1 or (approval and StormX.Forced):
                    $ StormX.change_face("_sad")
                    $ StormX.change_stat("love", 70, -5, 1)
                    $ StormX.change_stat("love", 20, -2, 1)
                    ch_s "Hmmph."
                    $ StormX.change_stat("obedience", 50, 3)
                    $ StormX.change_stat("inhibition", 60, 2)
                    if approval < 2:
                        $ StormX.Forced = 1
                    jump Storm_FT_Prep
                else:
                    $ StormX.change_stat("love", 200, -8)
                    $ StormX.change_face("_angry", 1)
                    "She slaps your hand away."
                    $ StormX.recent_history.append("_angry")
                    $ StormX.daily_history.append("_angry")

    if "no_fondle thighs" in StormX.daily_history:
        ch_s "I have been clear on this."
        $ StormX.recent_history.append("_angry")
        $ StormX.daily_history.append("_angry")
    elif StormX.Forced:
        $ StormX.change_face("_angry", 1)
        ch_s "You go too far."
        $ StormX.change_stat("lust", 50, 2)
        $ StormX.change_stat("obedience", 50, -1)
        $ StormX.recent_history.append("_angry")
        $ StormX.daily_history.append("_angry")
    elif Taboo:
        $ StormX.change_face("_angry", 1)
        $ StormX.recent_history.append("no_taboo")
        $ StormX.daily_history.append("no_taboo")
        ch_s "I should not be seen doing that."
    elif StormX.action_counter["fondle_thighs"]:
        $ StormX.change_face("_sad")
        ch_s "No, I do not think so."
    else:
        $ StormX.change_face("_sexy")
        $ StormX.mouth = "_sad"
        ch_s "No, I do not think so."
    $ StormX.recent_history.append("no_fondle thighs")
    $ StormX.daily_history.append("no_fondle thighs")
    $ approval_bonus = 0
    return

label Storm_FT_Prep:
    if primary_action == "kiss":
        $ primary_action = "fondle_thighs"
        return

    if offhand_action == "fondle_thighs":
        return

    if not StormX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (StormX)
        if "_angry" in StormX.recent_history:
            return

    $ approval_bonus = 0
    call Storm_Pussy_Launch ("fondle_thighs")
    if not StormX.action_counter["fondle_thighs"]:
        if StormX.Forced:
            $ StormX.change_stat("love", 90, -10)
            $ StormX.change_stat("obedience", 70, 15)
            $ StormX.change_stat("inhibition", 80, 10)
        else:
            $ StormX.change_stat("love", 90, 5)
            $ StormX.change_stat("obedience", 70, 10)
            $ StormX.change_stat("inhibition", 80, 15)

    if Taboo:
        $ StormX.change_stat("lust", 200, (int(Taboo/5)))
        $ StormX.change_stat("inhibition", 200, (2*(int(Taboo/5))))

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ StormX.drain_word("no_taboo")
    $ StormX.drain_word("no_fondle thighs")
    $ StormX.recent_history.append("fondle_thighs")
    $ StormX.daily_history.append("fondle_thighs")
    call Storm_Pussy_Launch ("fondle_thighs")

label Storm_FT_Cycle:
    while Round > 0:
        call ViewShift (StormX, StormX.pose, 0, "fondle_thighs")
        call shift_focus (StormX)
        $ StormX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (StormX)
                    $ counter += 1
                    $ Round -= 1
                    jump Storm_FT_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (StormX, "menu")
                    jump Storm_FT_Cycle
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
                                    "Can I do a little deeper?":
                                        if StormX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Storm_FT_After
                                            call Storm_Fondle_Pussy
                                        else:
                                            call Sex_Basic_Dialog (StormX, "tired")
                                    "Shift your hands a bit higher without asking":
                                        if StormX.remaining_actions and multi_action:
                                            $ action_context = "auto"
                                            call Storm_FT_After
                                            call Storm_Fondle_Pussy
                                        else:
                                            "As your hands creep upwards, she grabs your wrists."
                                            call Sex_Basic_Dialog (StormX, "tired")
                                    "Never Mind":
                                        jump Storm_FT_Cycle
                            else:
                                call Sex_Basic_Dialog (StormX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Storm_FT_After
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
                                    jump Storm_FT_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Storm_FT_Cycle
                                "Never mind":
                                    jump Storm_FT_Cycle

                        "Show her feet" if not ShowFeet and (StormX.pose == "doggy" or StormX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (StormX.pose == "doggy" or StormX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [StormX.name]":

                            call Girl_Undress (StormX)
                        "Clean up [StormX.name] (locked)" if not StormX.spunk:
                            pass
                        "Clean up [StormX.name]" if StormX.spunk:
                            call Girl_Cleanup (StormX, "ask")
                        "Never mind":
                            jump Storm_FT_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Storm_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Storm_FT_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Storm_Pos_Reset
                    $ Line = 0
                    jump Storm_FT_After


        call shift_focus (StormX)
        call Sex_Dialog (StormX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or StormX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (StormX)
                if "_angry" in StormX.recent_history:
                    call Storm_Pos_Reset
                    return
                $ StormX.change_stat("lust", 200, 5)
                if 100 > StormX.lust >= 70 and StormX.session_orgasms < 2 and StormX.SEXP >= 20:
                    $ StormX.recent_history.append("unsatisfied")
                    $ StormX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Storm_FT_After
                $ Line = "came"

            if StormX.lust >= 100:

                call Girl_Cumming (StormX)
                if action_context == "shift" or "_angry" in StormX.recent_history:
                    jump Storm_FT_After

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
                            jump Storm_FT_After
        if Partner:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if StormX.SEXP >= 100 or approval_check(StormX, 1200, "LO"):
            pass
        elif counter == (5 + StormX.action_counter["fondle_thighs"]):
            $ StormX.brows = "_confused"
            ch_s "Your hands are so warm. . ."
        elif counter == (15 + StormX.action_counter["fondle_thighs"]) and StormX.SEXP >= 15 and not approval_check(StormX, 1500):
            $ StormX.brows = "_confused"
            menu:
                ch_s "I am sure that is fun, but could we try something different?"
                "Finish up.":
                    "You let go. . ."
                    jump Storm_FT_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Storm_FT_After
                "No, this is fun.":
                    if approval_check(StormX, 1200) or approval_check(StormX, 500, "O"):
                        $ StormX.change_stat("love", 200, -5)
                        $ StormX.change_stat("obedience", 50, 3)
                        $ StormX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ StormX.change_face("_angry", 1)
                        call Storm_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_s "Well however much you are enjoying yourself, I need to take a break."
                        $ StormX.change_stat("love", 50, -3, 1)
                        $ StormX.change_stat("love", 80, -4, 1)
                        $ StormX.change_stat("obedience", 30, -1, 1)
                        $ StormX.change_stat("obedience", 50, -1, 1)
                        $ StormX.recent_history.append("_angry")
                        $ StormX.daily_history.append("_angry")
                        jump Storm_FT_After


        if Round == 10:
            call Sex_Basic_Dialog (StormX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (StormX, 5)


    $ StormX.change_face("_bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (StormX, "done")

label Storm_FT_After:
    if not action_context:
        call Storm_Pos_Reset

    $ StormX.change_face("_sexy")

    $ StormX.action_counter["fondle_thighs"]+= 1
    $ StormX.remaining_actions -=1
    if StormX.PantsNum() <= 6 or StormX.upskirt:
        $ StormX.addiction_rate += 1
        if "addictive" in Player.traits:
            $ StormX.addiction_rate += 1

    if Partner == "Kitty":
        call Partner_Like (StormX, 2)
    else:
        call Partner_Like (StormX, 1)

    if StormX.action_counter["fondle_thighs"]== 1:
        $ StormX.SEXP += 3
        if not action_context:
            if StormX.love >= 500 and "unsatisfied" not in StormX.recent_history:
                ch_s "Thank you for that."
            elif StormX.obedience <= 500 and Player.focus <= 20:
                $ StormX.change_face("_perplexed", 1)
                ch_s "Ok, was that good?"

    $ approval_bonus = 0


    call checkout
    return


label Storm_Fondle_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (StormX)

    if StormX.action_counter["fondle_pussy"]:
        $ approval_bonus += 20
    if StormX.PantsNum() > 6 or StormX.HoseNum() >= 5:
        $ approval_bonus -= 10
    if StormX.lust > 75:
        $ approval_bonus += 15
    if StormX.lust > 75 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in StormX.traits:
        $ approval_bonus += (2*Taboo)
    if StormX in Player.Harem or "sex friend" in StormX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in StormX.traits:
        $ approval_bonus -= 25
    if StormX.event_counter["forced"] and not StormX.Forced:
        $ approval_bonus -= 5*StormX.event_counter["forced"]

    if Taboo and "no_taboo" in StormX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in StormX.history:
        $ approval_bonus -= 20

    if "no_fondle pussy" in StormX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle pussy" in StormX.recent_history else 0

    $ approval = approval_check(StormX, 1050, TabM = 2)

    if action_context == "auto":
        if approval:
            $ StormX.change_face("_sexy")
            $ StormX.change_stat("obedience", 90, 1)
            $ StormX.change_stat("obedience", 70, 2)
            $ StormX.change_stat("inhibition", 70, 3)
            $ StormX.change_stat("inhibition", 30, 2)
            "As your hand creeps up her thigh, [StormX.name] seems a bit surprised, but then nods."
            jump Storm_FP_Prep
        else:
            $ StormX.change_face("_surprised")
            $ StormX.change_stat("obedience", 50, -2)
            ch_s "Perhaps show some control. . ."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if action_context == "pullback":
        $ StormX.change_face("_surprised")
        $ StormX.brows = "_sad"
        if StormX.lust > 80:
            $ StormX.change_stat("love", 70, -4)
        $ StormX.change_stat("obedience", 90, 1)
        $ StormX.change_stat("obedience", 70, 2)
        "As your hand pulls out, [StormX.name] gasps and looks upset."
        jump Storm_FP_Prep
    elif "fondle_pussy" in StormX.recent_history:
        $ StormX.change_face("_sexy", 1)
        ch_s "Mmmm, again? I suppose. . ."
        jump Storm_FP_Prep
    elif "fondle_pussy" in StormX.daily_history:
        $ StormX.change_face("_sexy", 1)
        $ Line = renpy.random.choice(["You did not get enough earlier?",
            "Relax, gently. . .",
            "Take it a bit gently, I am still glowing from earlier.",
            "Mmm. . ."])
        ch_s "[Line]"

    if approval >= 2:
        $ StormX.change_face("_bemused", 1)
        if StormX.Forced:
            $ StormX.change_face("_sad")
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
            $ StormX.change_stat("obedience", 90, 1)
            $ StormX.change_stat("inhibition", 60, 1)
        ch_s "Mmmm, I could not refuse. . ."
        $ StormX.change_stat("love", 90, 1)
        $ StormX.change_stat("inhibition", 50, 3)
        jump Storm_FP_Prep
    else:

        $ StormX.change_face("_angry", 1)
        if "no_fondle pussy" in StormX.recent_history:
            ch_s "Your persistance is doing you no favors, [StormX.player_petname]."
        elif "no_fondle pussy" in StormX.daily_history:
            ch_s "I have already told you my answer."
        elif Taboo and "no_taboo" in StormX.daily_history:
            ch_s "This area is too public, [StormX.player_petname]."
        elif not StormX.action_counter["fondle_pussy"]:
            $ StormX.change_face("_bemused")
            ch_s "Perhaps go slower, [StormX.player_petname]. . ."
        else:
            $ StormX.change_face("_bemused")
            ch_s "Hmm, no."
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle pussy" in StormX.daily_history:
                $ StormX.change_face("_bemused")
                ch_s "I appreciate your restraint, [StormX.player_petname]."
                return
            "Maybe later?" if "no_fondle pussy" not in StormX.daily_history:
                $ StormX.change_face("_sexy")
                ch_s "I will give it some thought, [StormX.player_petname]."
                $ StormX.change_stat("love", 80, 2)
                $ StormX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ StormX.recent_history.append("no_taboo")
                    $ StormX.daily_history.append("no_taboo")
                $ StormX.recent_history.append("no_fondle pussy")
                $ StormX.daily_history.append("no_fondle pussy")
                return
            "Come on, Please?":
                if approval:
                    $ StormX.change_face("_sexy")
                    $ StormX.change_stat("obedience", 90, 2)
                    $ StormX.change_stat("obedience", 50, 2)
                    $ StormX.change_stat("inhibition", 70, 3)
                    $ StormX.change_stat("inhibition", 40, 2)
                    ch_s "I suppose it could not hurt. . ."
                    jump Storm_FP_Prep
                else:
                    $ StormX.change_face("_sexy")
                    ch_s "No."
            "[[Start fondling anyway]":

                $ approval = approval_check(StormX, 450, "OI", TabM = 2)
                if approval > 1 or (approval and StormX.Forced):
                    $ StormX.change_face("_sad")
                    $ StormX.change_stat("love", 70, -5, 1)
                    $ StormX.change_stat("love", 200, -2)
                    ch_s "Oh, if you insist. . ."
                    $ StormX.change_stat("obedience", 50, 4)
                    $ StormX.change_stat("inhibition", 80, 1)
                    $ StormX.change_stat("inhibition", 60, 3)
                    if approval < 2:
                        $ StormX.Forced = 1
                    jump Storm_FP_Prep
                else:
                    $ StormX.change_stat("love", 200, -15)
                    $ StormX.change_face("_angry", 1)
                    "She slaps your hand away."
                    $ StormX.recent_history.append("_angry")
                    $ StormX.daily_history.append("_angry")

    if "no_fondle pussy" in StormX.daily_history:
        ch_s "I have been clear on this."
        $ StormX.recent_history.append("_angry")
        $ StormX.daily_history.append("_angry")
    elif StormX.Forced:
        $ StormX.change_face("_angry", 1)
        ch_s "You go too far."
        $ StormX.change_stat("lust", 70, 5)
        $ StormX.change_stat("obedience", 50, -2)
        $ StormX.recent_history.append("_angry")
        $ StormX.daily_history.append("_angry")
    elif Taboo:
        $ StormX.change_face("_angry", 1)
        $ StormX.recent_history.append("no_taboo")
        $ StormX.daily_history.append("no_taboo")
        ch_s "I should not be seen doing that."
    elif StormX.action_counter["fondle_pussy"]:
        $ StormX.change_face("_sad")
        ch_s "No, I do not think so."
    else:
        $ StormX.change_face("_sexy")
        $ StormX.mouth = "_sad"
        ch_s "No, I do not think so."
    $ StormX.recent_history.append("no_fondle pussy")
    $ StormX.daily_history.append("no_fondle pussy")
    $ approval_bonus = 0
    return

label Storm_FP_Prep:
    if offhand_action == "fondle_pussy":
        return

    call Storm_Pussy_Launch ("fondle_pussy")

    if action_context == StormX:

        $ action_context = 0
        if (StormX.legs and not StormX.upskirt) or (StormX.underwear and not StormX.underwear_pulled_down):

            if approval_check(StormX, 1250, TabM = 1) or (StormX.SeenPussy and approval_check(StormX, 500) and not Taboo):
                $ StormX.upskirt = 1
                $ StormX.underwear_pulled_down = 1
                $ Line = 0
                if StormX.PantsNum() == 5:
                    $ Line = StormX.name + " hikes up her_skirt"
                elif StormX.PantsNum() >= 6:
                    $ Line = StormX.name + " pulls down her " + StormX.legs
                else:
                    $ Line = 0
                if StormX.underwear:
                    if Line:

                        "[Line] and pulls her [StormX.underwear] out of the way."
                        "She then grabs your arm and then strokes your hand across her crotch, clearly intending you to get to work."
                    else:

                        "She pulls her [StormX.underwear] out of the way, and then strokes your hand across her crotch."
                        "She clearly intends for you to get to work."
                else:

                    "[Line], and then strokes your hand across her crotch."
                    "She clearly intends for you to get to work."
                call Storm_First_Bottomless (1)
            else:
                "[StormX.name] grabs your arm and strokes your hand across her crotch, clearly intending you to get to work."
        else:
            "[StormX.name] grabs your arm and strokes your hand across her crotch, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ StormX.change_stat("inhibition", 80, 3)
                $ StormX.change_stat("inhibition", 50, 2)
                "You start to run your fingers along her pussy."
            "Praise her.":
                $ StormX.change_face("_sexy", 1)
                $ StormX.change_stat("inhibition", 80, 3)
                ch_p "I like the initiative, [StormX.petname]."
                $ StormX.nameCheck()
                "You start to run your fingers along her pussy."
                $ StormX.change_stat("love", 85, 1)
                $ StormX.change_stat("obedience", 90, 1)
                $ StormX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your hand back."
                $ StormX.change_face("_surprised")
                $ StormX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [StormX.petname]."
                $ StormX.nameCheck()
                "[StormX.name] pulls back."
                $ StormX.change_stat("obedience", 90, 1)
                $ StormX.change_stat("obedience", 50, 1)
                $ StormX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ StormX.add_word(1,"refused","refused")
                return


    if not StormX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (StormX)
        if "_angry" in StormX.recent_history:
            return
    $ approval_bonus = 0

    if not StormX.action_counter["fondle_pussy"]:
        if StormX.Forced:
            $ StormX.change_stat("love", 90, -50)
            $ StormX.change_stat("obedience", 70, 35)
            $ StormX.change_stat("inhibition", 80, 25)
        else:
            $ StormX.change_stat("love", 90, 10)
            $ StormX.change_stat("obedience", 70, 10)
            $ StormX.change_stat("inhibition", 80, 15)
    if Taboo:
        $ StormX.inhibition += int(Taboo/10)
        $ StormX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ StormX.drain_word("no_taboo")
    $ StormX.drain_word("no_fondle pussy")
    $ StormX.recent_history.append("fondle_pussy")
    $ StormX.daily_history.append("fondle_pussy")
    call Storm_Pussy_Launch ("fondle_pussy")

    $ action_speed = 1

label Storm_FP_Cycle:
    while Round > 0:
        call ViewShift (StormX, StormX.pose, 0, "fondle_pussy")
        call shift_focus (StormX)
        $ StormX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass

                "I want to stick a finger in. . ." if action_speed != 2:
                    if StormX.action_counter["finger_pussy"]:
                        $ action_speed = 2
                    else:
                        menu:
                            "Ask her first":
                                $ action_context = "shift"
                            "Don't ask first [[just stick it in]":
                                $ action_context = "auto"
                        call Storm_Insert_Pussy

                "Pull back a bit. . ." if action_speed == 2:
                    $ action_speed = 0
                "Slap her ass":

                    call Slap_Ass (StormX)
                    $ counter += 1
                    $ Round -= 1
                    jump Storm_FP_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (StormX, "menu")
                    jump Storm_FP_Cycle
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
                                    "I want to lick your pussy.":
                                        $ action_context = "shift"
                                        call Storm_FP_After
                                        call Storm_Lick_Pussy
                                    "Just start licking":
                                        $ action_context = "auto"
                                        call Storm_FP_After
                                        call Storm_Lick_Pussy
                                    "Pull back to the thighs":
                                        $ action_context = "pullback"
                                        call Storm_FP_After
                                        call Storm_Fondle_Thighs
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Storm_FP_After
                                        call Storm_Dildo_Pussy
                                    "Never Mind":
                                        jump Storm_FP_Cycle
                            else:
                                call Sex_Basic_Dialog (StormX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Storm_FP_After
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
                                    jump Storm_FP_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Storm_FP_Cycle
                                "Never mind":
                                    jump Storm_FP_Cycle

                        "Show her feet" if not ShowFeet and (StormX.pose == "doggy" or StormX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (StormX.pose == "doggy" or StormX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [StormX.name]":

                            call Girl_Undress (StormX)
                        "Clean up [StormX.name] (locked)" if not StormX.spunk:
                            pass
                        "Clean up [StormX.name]" if StormX.spunk:
                            call Girl_Cleanup (StormX, "ask")
                        "Never mind":
                            jump Storm_FP_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Storm_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Storm_FP_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Storm_Pos_Reset
                    $ Line = 0
                    jump Storm_FP_After


        call shift_focus (StormX)
        call Sex_Dialog (StormX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or StormX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (StormX)
                if "_angry" in StormX.recent_history:
                    call Storm_Pos_Reset
                    return
                $ StormX.change_stat("lust", 200, 5)
                if 100 > StormX.lust >= 70 and StormX.session_orgasms < 2:
                    $ StormX.recent_history.append("unsatisfied")
                    $ StormX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Storm_FP_After
                $ Line = "came"

            if StormX.lust >= 100:

                call Girl_Cumming (StormX)
                if action_context == "shift" or "_angry" in StormX.recent_history:
                    jump Storm_FP_After

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
                            jump Storm_FP_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if StormX.SEXP >= 100 or approval_check(StormX, 1200, "LO"):
            pass
        elif counter == (5 + StormX.action_counter["fondle_pussy"]):
            $ StormX.brows = "_confused"
            ch_s "Mmmm, yes. . . deeper. . ."
        elif StormX.lust >= 80:
            pass
        elif counter == (15 + StormX.action_counter["fondle_pussy"]) and StormX.SEXP >= 15 and not approval_check(StormX, 1500):
            $ StormX.brows = "_confused"
            menu:
                ch_s "I am sure that is fun, but could we try something different?"
                "Finish up.":
                    "You let go. . ."
                    jump Storm_FP_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Storm_FP_After
                "No, this is fun.":
                    if approval_check(StormX, 1200) or approval_check(StormX, 500, "O"):
                        $ StormX.change_stat("love", 200, -5)
                        $ StormX.change_stat("obedience", 50, 3)
                        $ StormX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ StormX.change_face("_angry", 1)
                        call Storm_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_s "Well however much you are enjoying yourself, I need to take a break."
                        $ StormX.change_stat("love", 50, -3, 1)
                        $ StormX.change_stat("love", 80, -4, 1)
                        $ StormX.change_stat("obedience", 30, -1, 1)
                        $ StormX.change_stat("obedience", 50, -1, 1)
                        $ StormX.recent_history.append("_angry")
                        $ StormX.daily_history.append("_angry")
                        jump Storm_FP_After


        if Round == 10:
            call Sex_Basic_Dialog (StormX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (StormX, 5)


    $ StormX.change_face("_bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (StormX, "done")

label Storm_FP_After:
    if not action_context:
        call Storm_Pos_Reset

    $ StormX.change_face("_sexy")

    $ StormX.action_counter["fondle_pussy"] += 1
    $ StormX.remaining_actions -=1
    if StormX.PantsNum() <= 6 or StormX.upskirt:
        $ StormX.addiction_rate += 1
        if "addictive" in Player.traits:
            $ StormX.addiction_rate += 1

    call Partner_Like (StormX, 2)

    if StormX.action_counter["fondle_pussy"] == 1:
        $ StormX.SEXP += 7
        if not action_context:
            if StormX.love >= 500 and "unsatisfied" not in StormX.recent_history:
                ch_s "You certainly. . . reached some interesting places there. . ."
            elif StormX.obedience <= 500 and Player.focus <= 20:
                $ StormX.change_face("_perplexed", 1)
                ch_s "Did you enjoy that?"

    $ approval_bonus = 0


    call checkout
    return




label Storm_Insert_Pussy:
    call shift_focus (StormX)
    if action_context == "auto":
        if approval_check(StormX, 1100, TabM = 2):
            $ StormX.change_face("_surprised")
            $ StormX.change_stat("obedience", 90, 1)
            $ StormX.change_stat("obedience", 70, 2)
            $ StormX.change_stat("inhibition", 70, 3)
            $ StormX.change_stat("inhibition", 30, 2)
            "As you slide a finger in, [StormX.name] seems a bit surprised, but seems into it."
            jump Storm_IP_Prep
        else:
            $ StormX.change_face("_surprised",2)
            $ StormX.change_stat("love", 80, -2)
            $ StormX.change_stat("obedience", 50, -3)
            ch_s "Oooh!"
            "She slaps your hand back."
            $ StormX.change_face("_perplexed",1)
            ch_s "Careful what you put in there, you may not get it back."
            return

    if approval_check(StormX, 1100, TabM = 2):
        if StormX.Forced:
            $ StormX.change_face("_sad")
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
            $ StormX.change_stat("obedience", 90, 1)
            $ StormX.change_stat("inhibition", 60, 1)
            ch_s "If you must. . ."
        else:
            $ StormX.change_face("_sexy", 1)
            $ StormX.change_stat("love", 90, 1)
            $ StormX.change_stat("inhibition", 50, 3)
            ch_s "Mmmmmm. . ."
        $ StormX.change_stat("obedience", 20, 1)
        $ StormX.change_stat("obedience", 60, 1)
        $ StormX.change_stat("inhibition", 70, 2)
        jump Storm_IP_Prep
    else:

        $ StormX.change_face("_bemused", 2)
        ch_s "No. Thank you."
        $ StormX.blushing = "_blush1"
    return


label Storm_IP_Prep:
    if not StormX.action_counter["finger_pussy"]:
        $ StormX.action_counter["finger_pussy"] = 1
        $ StormX.SEXP += 10
        if StormX.Forced:
            $ StormX.change_stat("love", 90, -60)
            $ StormX.change_stat("obedience", 70, 55)
            $ StormX.change_stat("inhibition", 80, 35)
        else:
            $ StormX.change_stat("love", 90, 10)
            $ StormX.change_stat("obedience", 70, 20)
            $ StormX.change_stat("inhibition", 80, 25)

    if not StormX.Forced and action_context != "auto":
        call Girl_Undress (StormX, "bottom")
        if "_angry" in StormX.recent_history:
            return


    if Taboo:
        $ StormX.inhibition += int(Taboo/10)
        $ StormX.lust += int(Taboo/5)

    $ Line = 0
    $ action_speed = 2
    return







label Storm_Lick_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (StormX)

    if StormX.action_counter["eat_pussy"]:
        $ approval_bonus += 15
    if StormX.PantsNum() > 6 or StormX.HoseNum() >= 5:
        $ approval_bonus -= 15
    if StormX.lust > 95:
        $ approval_bonus += 20
    elif StormX.lust > 85:
        $ approval_bonus += 15
    if action_context == "shift":
        $ approval_bonus += 10
    if StormX.lust > 85 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in StormX.traits:
        $ approval_bonus += (4*Taboo)
    if StormX in Player.Harem or "sex friend" in StormX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in StormX.traits:
        $ approval_bonus -= 25
    if StormX.event_counter["forced"] and not StormX.Forced:
        $ approval_bonus -= 5*StormX.event_counter["forced"]

    if Taboo and "no_taboo" in StormX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in StormX.history:
        $ approval_bonus -= 20

    if "no_lick pussy" in StormX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_lick pussy" in StormX.recent_history else 0

    $ approval = approval_check(StormX, 1250, TabM = 4)

    if action_context == "auto":
        if approval:
            $ StormX.change_face("_surprised")
            $ StormX.change_stat("obedience", 90, 1)
            $ StormX.change_stat("obedience", 70, 2)
            $ StormX.change_stat("inhibition", 70, 3)
            $ StormX.change_stat("inhibition", 30, 2)
            "As you crouch down and start to lick her pussy, [StormX.name] jumps, but then softens."
            $ StormX.change_face("_sexy")
            jump Storm_LP_Prep
        else:
            $ StormX.change_face("_surprised")
            $ StormX.change_stat("love", 80, -2)
            $ StormX.change_stat("obedience", 50, -3)
            ch_s "I appreciate the intent, but this is not the time for it."
            $ StormX.change_face("_perplexed",1)
            "She pushes your head back away from her."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "eat_pussy" in StormX.recent_history:
        $ StormX.change_face("_sexy", 1)
        ch_s "Mmmm, again? I suppose. . ."
        jump Storm_LP_Prep
    elif "eat_pussy" in StormX.daily_history:
        $ StormX.change_face("_sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Huh? Again?",
            "I must have done something right.",
            "What a queen deserves. . .",
            "Mmm. . ."])
        ch_s "[Line]"

    if approval >= 2:
        if StormX.Forced:
            $ StormX.change_face("_sad")
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
            $ StormX.change_stat("obedience", 90, 1)
            $ StormX.change_stat("inhibition", 60, 1)
            ch_s "If you must. . ."
        else:
            $ StormX.change_face("_sexy", 1)
            $ StormX.eyes = "_closed"
            $ StormX.change_stat("love", 90, 1)
            $ StormX.change_stat("inhibition", 50, 3)
            $ StormX.change_stat("lust", 200, 3)
            ch_s "Mmmmmm. . ."
        $ StormX.change_stat("obedience", 20, 1)
        $ StormX.change_stat("obedience", 60, 1)
        $ StormX.change_stat("inhibition", 70, 2)
        jump Storm_LP_Prep
    else:

        $ StormX.change_face("_angry", 1)
        if "no_lick pussy" in StormX.recent_history:
            ch_s "Do not persist in this, [StormX.player_petname]."
        elif Taboo and "no_taboo" in StormX.daily_history and "no_lick pussy" in StormX.daily_history:
            ch_s "You already got your answer!"
        elif "no_lick pussy" in StormX.daily_history:
            ch_s "I believe you know my answer on this matter."
        elif Taboo and "no_taboo" in StormX.daily_history:
            ch_s "This area is too public, [StormX.player_petname]."
        elif not StormX.action_counter["eat_pussy"]:
            $ StormX.change_face("_bemused")
            ch_s "Oh, that would. . .perhaps not, [StormX.player_petname]. . ."
        else:
            $ StormX.change_face("_bemused")
            ch_s "I would be uncomfortable with that. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_lick pussy" in StormX.daily_history:
                $ StormX.change_face("_bemused")
                ch_s "I appreciate your restraint, [StormX.player_petname]."
                return
            "I'm sure I can convince you later. . ." if "no_lick pussy" not in StormX.daily_history:
                $ StormX.change_face("_sexy")
                ch_s "I will give it some thought, [StormX.player_petname]."
                $ StormX.change_stat("love", 80, 2)
                $ StormX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ StormX.recent_history.append("no_taboo")
                    $ StormX.daily_history.append("no_taboo")
                $ StormX.recent_history.append("no_lick pussy")
                $ StormX.daily_history.append("no_lick pussy")
                return
            "I think you'd really enjoy it. . .":
                if approval:
                    $ StormX.change_face("_sexy")
                    $ StormX.change_stat("obedience", 90, 2)
                    $ StormX.change_stat("obedience", 50, 2)
                    ch_s "I. . . would. . ."
                    $ StormX.change_stat("inhibition", 70, 3)
                    $ StormX.change_stat("inhibition", 40, 2)
                    jump Storm_LP_Prep
                else:
                    $ StormX.change_face("_sexy")
                    ch_s "I would, but still no, [StormX.player_petname]."
            "[[Get in there anyway]":

                $ approval = approval_check(StormX, 750, "OI", TabM = 4)
                if approval > 1 or (approval and StormX.Forced):
                    $ StormX.change_face("_sad")
                    $ StormX.change_stat("love", 70, -5, 1)
                    $ StormX.change_stat("love", 200, -2)
                    ch_s "If you insist. . ."
                    $ StormX.change_stat("obedience", 50, 4)
                    $ StormX.change_stat("inhibition", 80, 1)
                    $ StormX.change_stat("inhibition", 60, 3)
                    if approval < 2:
                        $ StormX.Forced = 1
                    jump Storm_LP_Prep
                else:
                    $ StormX.change_stat("love", 200, -15)
                    $ StormX.change_face("_angry", 1)
                    "She shoves your head back."
                    $ StormX.recent_history.append("_angry")
                    $ StormX.daily_history.append("_angry")

    if "no_lick pussy" in StormX.daily_history:
        ch_s "I have been clear on this."
        $ StormX.recent_history.append("_angry")
        $ StormX.daily_history.append("_angry")
    elif StormX.Forced:
        $ StormX.change_face("_angry", 1)
        ch_s "You go too far."
        $ StormX.change_stat("lust", 80, 5)
        $ StormX.change_stat("obedience", 50, -2)
        $ StormX.recent_history.append("_angry")
        $ StormX.daily_history.append("_angry")
    elif Taboo:
        $ StormX.change_face("_angry", 1)
        $ StormX.recent_history.append("no_taboo")
        $ StormX.daily_history.append("no_taboo")
        ch_s "I should not be seen doing that."
    elif StormX.action_counter["eat_pussy"]:
        $ StormX.change_face("_sad")
        ch_s "No, I do not think so."
    else:
        $ StormX.change_face("_surprised")
        ch_s "No, I do not think so."
        $ StormX.change_face()
    $ StormX.recent_history.append("no_lick pussy")
    $ StormX.daily_history.append("no_lick pussy")
    $ approval_bonus = 0
    return

label Storm_LP_Prep:
    if offhand_action == "eat_pussy":
        return

    call Storm_Pussy_Launch ("eat_pussy")

    if action_context == StormX:

        $ action_context = 0
        if (StormX.legs and not StormX.upskirt) or (StormX.underwear and not StormX.underwear_pulled_down):

            if approval_check(StormX, 1250, TabM = 1) or (StormX.SeenPussy and approval_check(StormX, 500) and not Taboo):
                $ StormX.upskirt = 1
                $ StormX.underwear_pulled_down = 1
                $ Line = 0
                if StormX.PantsNum() == 5:
                    $ Line = StormX.name + " hikes up her_skirt"
                elif StormX.PantsNum() >= 6:
                    $ Line = StormX.name + " pulls down her " + StormX.legs
                else:
                    $ Line = 0
                if StormX.underwear:
                    if Line:

                        "[Line] and pulls her [StormX.underwear] out of the way."
                        "She then grabs your head and pulls it to her crotch, clearly intending you to get to work."
                    else:

                        "She pulls her [StormX.underwear] out of the way, and then shoves your face into her crotch."
                        "She clearly intends for you to get to work."
                else:

                    "[Line], and then shoves your face into her crotch."
                    "She clearly intends for you to get to work."
                call Storm_First_Bottomless (1)
            else:
                "[StormX.name] grabs your head and pulls it to her crotch, clearly intending you to get to work."
        else:
            "[StormX.name] grabs your head and pulls it to her crotch, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ StormX.change_stat("inhibition", 80, 3)
                $ StormX.change_stat("inhibition", 50, 2)
                "You start licking."
            "Praise her.":
                $ StormX.change_face("_sexy", 1)
                $ StormX.change_stat("inhibition", 80, 3)
                ch_p "Mmm, I like this idea, [StormX.petname]."
                $ StormX.nameCheck()
                "You start licking."
                $ StormX.change_stat("love", 85, 1)
                $ StormX.change_stat("obedience", 90, 1)
                $ StormX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your head away."
                $ StormX.change_face("_surprised")
                $ StormX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [StormX.petname]."
                $ StormX.nameCheck()
                "[StormX.name] pulls back."
                $ StormX.change_stat("obedience", 90, 1)
                $ StormX.change_stat("obedience", 50, 1)
                $ StormX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ StormX.add_word(1,"refused","refused")
                return


    if not StormX.Forced and action_context != "auto":
        $ approval_bonus = 0
        if StormX.PantsNum() > 6:
            $ approval_bonus = 15
        call Bottoms_Off (StormX)
        if "_angry" in StormX.recent_history:
            return

    $ approval_bonus = 0
    if not StormX.action_counter["eat_pussy"]:
        if StormX.Forced:
            $ StormX.change_stat("love", 90, -30)
            $ StormX.change_stat("obedience", 70, 35)
            $ StormX.change_stat("inhibition", 80, 75)
        else:
            $ StormX.change_stat("love", 90, 35)
            $ StormX.change_stat("obedience", 70, 15)
            $ StormX.change_stat("inhibition", 80, 35)
    if Taboo:
        $ StormX.inhibition += int(Taboo/10)
        $ StormX.lust += int(Taboo/5)
    if action_context:
        $ renpy.pop_call()
        $ action_context = 0

    if StormX.PantsNum() == 5:
        $ StormX.upskirt = 1
        $ StormX.SeenPanties = 1
    call Storm_First_Bottomless (1)

    $ Line = 0
    $ counter = 0
    if Taboo:
        $ StormX.drain_word("no_taboo")
    $ StormX.drain_word("no_lick pussy")
    $ StormX.recent_history.append("eat_pussy")
    $ StormX.daily_history.append("eat_pussy")
    call Storm_Pussy_Launch ("eat_pussy")

label Storm_LP_Cycle:
    if offhand_action == "kiss":
        $ offhand_action = 0
    while Round > 0:
        call ViewShift (StormX, StormX.pose, 0, "eat_pussy")
        call shift_focus (StormX)
        $ StormX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (StormX)
                    $ counter += 1
                    $ Round -= 1
                    jump Storm_LP_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (StormX, "menu")
                    jump Storm_LP_Cycle
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
                                    "Pull out and start rubbing again.":
                                        if StormX.remaining_actions and multi_action:
                                            $ action_context = "pullback"
                                            call Storm_LP_After
                                            call Storm_Fondle_Pussy
                                        else:
                                            call Sex_Basic_Dialog (StormX, "tired")
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Storm_LP_After
                                        call Storm_Dildo_Pussy
                                    "Never Mind":
                                        jump Storm_LP_Cycle
                            else:
                                call Sex_Basic_Dialog (StormX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Storm_LP_After
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
                                    jump Storm_LP_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Storm_LP_Cycle
                                "Never mind":
                                    jump Storm_LP_Cycle

                        "Show her feet" if not ShowFeet and (StormX.pose == "doggy" or StormX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (StormX.pose == "doggy" or StormX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [StormX.name]":

                            call Girl_Undress (StormX)
                        "Clean up [StormX.name] (locked)" if not StormX.spunk:
                            pass
                        "Clean up [StormX.name]" if StormX.spunk:
                            call Girl_Cleanup (StormX, "ask")
                        "Never mind":
                            jump Storm_LP_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Storm_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Storm_LP_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Storm_Pos_Reset
                    $ Line = 0
                    jump Storm_LP_After


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
                if "_angry" in StormX.recent_history:
                    call Storm_Pos_Reset
                    return
                $ StormX.change_stat("lust", 200, 5)
                if 100 > StormX.lust >= 70 and StormX.session_orgasms < 2:
                    $ StormX.recent_history.append("unsatisfied")
                    $ StormX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Storm_LP_After
                $ Line = "came"

            if StormX.lust >= 100:

                call Girl_Cumming (StormX)
                if action_context == "shift" or "_angry" in StormX.recent_history:
                    jump Storm_LP_After

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
                            jump Storm_LP_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if StormX.SEXP >= 100 or approval_check(StormX, 1200, "LO"):
            pass
        elif counter == (5 + StormX.action_counter["eat_pussy"]):
            $ StormX.brows = "_confused"
            ch_s "Oh, that is delightful. . ."
        elif StormX.lust >= 80:
            pass
        elif counter == (15 + StormX.action_counter["eat_pussy"]) and StormX.SEXP >= 15 and not approval_check(StormX, 1500):
            $ StormX.brows = "_confused"
            menu:
                ch_s "I am sure that is fun, but could we try something different?"
                "Finish up.":
                    "You let go. . ."
                    jump Storm_LP_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Storm_LP_After
                "No, this is fun.":
                    if approval_check(StormX, 1200) or approval_check(StormX, 500, "O"):
                        $ StormX.change_stat("love", 200, -5)
                        $ StormX.change_stat("obedience", 50, 3)
                        $ StormX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ StormX.change_face("_angry", 1)
                        call Storm_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_s "Well however much you are enjoying yourself, I need to take a break."
                        $ StormX.change_stat("love", 50, -3, 1)
                        $ StormX.change_stat("love", 80, -4, 1)
                        $ StormX.change_stat("obedience", 30, -1, 1)
                        $ StormX.change_stat("obedience", 50, -1, 1)
                        $ StormX.recent_history.append("_angry")
                        $ StormX.daily_history.append("_angry")
                        jump Storm_LP_After


        call Escalation (StormX)

        if Round == 10:
            call Sex_Basic_Dialog (StormX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (StormX, 5)


    $ StormX.change_face("_bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (StormX, "done")

label Storm_LP_After:
    if not action_context:
        call Storm_Pos_Reset

    $ StormX.change_face("_sexy")

    $ StormX.action_counter["eat_pussy"] += 1
    $ StormX.remaining_actions -=1
    if StormX.PantsNum() <= 6 or StormX.upskirt:
        $ StormX.addiction_rate += 1
        if "addictive" in Player.traits:
            $ StormX.addiction_rate += 1

    call Partner_Like (StormX, 3, 2)

    if StormX.action_counter["eat_pussy"] == 1:
        $ StormX.SEXP += 10
        if not action_context:
            if StormX.love >= 500 and "unsatisfied" not in StormX.recent_history:
                ch_s "You really do have atalent for that. . ."
            elif StormX.obedience <= 500 and Player.focus <= 20:
                $ StormX.change_face("_perplexed", 1)
                ch_s "That was not so bad. . ."

    $ approval_bonus = 0


    call checkout
    return






label Storm_Fondle_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (StormX)

    if StormX.action_counter["fondle_ass"]:
        $ approval_bonus += 10
    if StormX.PantsNum() > 6 or StormX.HoseNum() >= 5:
        $ approval_bonus -= 5
    if StormX.lust > 75:
        $ approval_bonus += 15
    if "exhibitionist" in StormX.traits:
        $ approval_bonus += Taboo
    if StormX in Player.Harem or "sex friend" in StormX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in StormX.traits:
        $ approval_bonus -= 25
    if StormX.event_counter["forced"] and not StormX.Forced:
        $ approval_bonus -= 5*StormX.event_counter["forced"]

    if Taboo and "no_taboo" in StormX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in StormX.history:
        $ approval_bonus -= 20

    if "no_fondle ass" in StormX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle ass" in StormX.recent_history else 0

    $ approval = approval_check(StormX, 750, TabM=1)

    if action_context == "auto":
        if approval:
            $ StormX.change_face("_surprised", 1)
            $ StormX.change_stat("obedience", 70, 2)
            $ StormX.change_stat("inhibition", 40, 2)
            "As your hand creeps down her backside, [StormX.name] jumps a bit, and then relaxes."
            $ StormX.change_face("_sexy")
            jump Storm_FA_Prep
        else:
            $ StormX.change_face("_surprised")
            $ StormX.change_stat("obedience", 50, -3)
            ch_s "Release me, [StormX.player_petname]."
            $ StormX.change_face("_bemused")
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if action_context == "pullback":
        $ StormX.change_face("_surprised")
        $ StormX.brows = "_sad"
        if StormX.lust > 80:
            $ StormX.change_stat("love", 70, -4)
        $ StormX.change_stat("obedience", 90, 1)
        $ StormX.change_stat("obedience", 70, 2)
        "As your finger slides out, [StormX.name] gasps and looks upset."
        jump Storm_FA_Prep
    elif "fondle_ass" in StormX.recent_history:
        $ StormX.change_face("_sexy", 1)
        ch_s "Mmmm, again? I suppose. . ."
        jump Storm_FA_Prep
    elif "fondle_ass" in StormX.daily_history:
        $ StormX.change_face("_sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Perhaps not so rough this time?",
            "Mmm. . ."])
        ch_s "[Line]"

    if approval >= 2:
        if StormX.Forced:
            $ StormX.change_face("_sad")
            $ StormX.change_stat("love", 70, -2, 1)
            $ StormX.change_stat("obedience", 90, 2)
            $ StormX.change_stat("inhibition", 60, 2)
            ch_s "If you insist. . ."
        else:
            $ StormX.change_face("bemused, 1")
            ch_s "I suppose that is reasonable. . ."
        $ StormX.change_stat("lust", 200, 3)
        $ StormX.change_stat("obedience", 60, 1)
        $ StormX.change_stat("inhibition", 70, 1)
        jump Storm_FA_Prep
    else:

        $ StormX.change_face("_angry", 1)
        if "no_fondle ass" in StormX.recent_history:
            ch_s "Your persistance is doing you no favors, [StormX.player_petname]."
        elif "no_fondle ass" in StormX.daily_history:
            ch_s "I have already told you my answer."
        elif Taboo and "no_taboo" in StormX.daily_history:
            ch_s "This area is too public, [StormX.player_petname]."
        elif not StormX.action_counter["fondle_ass"]:
            $ StormX.change_face("_bemused")
            ch_s "I would rather not, [StormX.player_petname]. . ."
        else:
            $ StormX.change_face("_bemused")
            ch_s "Not now, [StormX.player_petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle ass" in StormX.daily_history:
                $ StormX.change_face("_bemused")
                ch_s "I appreciate your restraint, [StormX.player_petname]."
                return
            "Maybe later?" if "no_fondle ass" not in StormX.daily_history:
                $ StormX.change_face("_sexy")
                ch_s "I will give it some thought, [StormX.player_petname]."
                $ StormX.change_stat("love", 80, 2)
                $ StormX.change_stat("inhibition", 50, 2)
                if Taboo:
                    $ StormX.recent_history.append("no_taboo")
                    $ StormX.daily_history.append("no_taboo")
                $ StormX.recent_history.append("no_fondle ass")
                $ StormX.daily_history.append("no_fondle ass")
                return
            "Just one good squeeze?":
                if approval:
                    $ StormX.change_face("_sexy")
                    $ StormX.change_stat("obedience", 90, 1)
                    $ StormX.change_stat("obedience", 50, 2)
                    ch_s "Well, one could not hurt. . ."
                    $ StormX.change_stat("inhibition", 70, 1)
                    $ StormX.change_stat("inhibition", 40, 2)
                    jump Storm_FA_Prep
                else:
                    $ StormX.change_face("_sexy")
                    ch_s "No."
            "[[Start fondling anyway]":

                $ approval = approval_check(StormX, 250, "OI", TabM = 3)
                if approval > 1 or (approval and StormX.Forced):
                    $ StormX.change_face("_sad")
                    $ StormX.change_stat("love", 70, -3, 1)
                    $ StormX.change_stat("love", 200, -1)
                    ch_s ". . . I suppose."
                    $ StormX.change_stat("obedience", 50, 3)
                    $ StormX.change_stat("inhibition", 60, 3)
                    if approval < 2:
                        $ StormX.Forced = 1
                    jump Storm_FA_Prep
                else:
                    $ StormX.change_stat("love", 200, -10)
                    $ StormX.change_face("_angry", 1)
                    "She slaps your hand away."
                    $ StormX.recent_history.append("_angry")
                    $ StormX.daily_history.append("_angry")

    if "no_fondle ass" in StormX.daily_history:
        ch_s "I have been clear on this."
        $ StormX.recent_history.append("_angry")
        $ StormX.daily_history.append("_angry")
    elif StormX.Forced:
        $ StormX.change_face("_angry", 1)
        ch_s "You go too far."
        $ StormX.change_stat("lust", 60, 5)
        $ StormX.change_stat("obedience", 50, -2)
        $ StormX.recent_history.append("_angry")
        $ StormX.daily_history.append("_angry")
    elif Taboo:
        $ StormX.change_face("_angry", 1)
        $ StormX.recent_history.append("no_taboo")
        $ StormX.daily_history.append("no_taboo")
        ch_s "I should not be seen doing that."
    elif StormX.action_counter["fondle_ass"]:
        $ StormX.change_face("_sad")
        ch_s "No, I do not think so."
    else:
        $ StormX.change_face("_sexy")
        $ StormX.mouth = "_sad"
        ch_s "No, I do not think so."
    $ StormX.recent_history.append("no_fondle ass")
    $ StormX.daily_history.append("no_fondle ass")
    $ approval_bonus = 0
    return

ch_s "Sorry, I don't even know how I got here. . ."
return

label Storm_FA_Prep:
    if offhand_action == "fondle_ass":
        return
    if not StormX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (StormX)
        if "_angry" in StormX.recent_history:
            return
    $ approval_bonus = 0
    call Storm_Pussy_Launch ("fondle_ass")
    if not StormX.action_counter["fondle_ass"]:
        if StormX.Forced:
            $ StormX.change_stat("love", 90, -20)
            $ StormX.change_stat("obedience", 70, 20)
            $ StormX.change_stat("inhibition", 80, 15)
        else:
            $ StormX.change_stat("love", 90, 10)
            $ StormX.change_stat("obedience", 70, 12)
            $ StormX.change_stat("inhibition", 80, 20)
    if Taboo:
        $ StormX.inhibition += int(Taboo/10)
        $ StormX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ StormX.drain_word("no_taboo")
    $ StormX.drain_word("no_fondle ass")
    $ StormX.recent_history.append("fondle_ass")
    $ StormX.daily_history.append("fondle_ass")
    call Storm_Pussy_Launch ("fondle_ass")

label Storm_FA_Cycle:
    while Round > 0:
        call ViewShift (StormX, StormX.pose, 0, "fondle_ass")
        call shift_focus (StormX)
        $ StormX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (StormX)
                    $ counter += 1
                    $ Round -= 1
                    jump Storm_FA_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (StormX, "menu")
                    jump Storm_FA_Cycle
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
                                    "I want to stick a finger in.":
                                        $ action_context = "shift"
                                        call Storm_FA_After
                                        call Storm_Insert_Ass
                                    "Just stick a finger in without asking.":
                                        $ action_context = "auto"
                                        call Storm_FA_After
                                        call Storm_Insert_Ass
                                    "I want to lick your asshole.":
                                        $ action_context = "shift"
                                        call Storm_FA_After
                                        call Storm_Lick_Ass
                                    "Just start licking.":
                                        $ action_context = "auto"
                                        call Storm_FA_After
                                        call Storm_Lick_Ass
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Storm_FA_After
                                        call Storm_Dildo_Ass
                                    "Never Mind":
                                        jump Storm_FA_Cycle
                            else:
                                call Sex_Basic_Dialog (StormX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Storm_FA_After
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
                                    jump Storm_FA_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Storm_FA_Cycle
                                "Never mind":
                                    jump Storm_FA_Cycle

                        "Show her feet" if not ShowFeet and (StormX.pose == "doggy" or StormX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (StormX.pose == "doggy" or StormX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [StormX.name]":

                            call Girl_Undress (StormX)
                        "Clean up [StormX.name] (locked)" if not StormX.spunk:
                            pass
                        "Clean up [StormX.name]" if StormX.spunk:
                            call Girl_Cleanup (StormX, "ask")
                        "Never mind":
                            jump Storm_FA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Storm_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Storm_FA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Storm_Pos_Reset
                    $ Line = 0
                    jump Storm_FA_After


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
                if "_angry" in StormX.recent_history:
                    call Storm_Pos_Reset
                    return
                $ StormX.change_stat("lust", 200, 5)
                if 100 > StormX.lust >= 70 and StormX.session_orgasms < 2 and StormX.SEXP >= 20:
                    $ StormX.recent_history.append("unsatisfied")
                    $ StormX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Storm_FA_After
                $ Line = "came"

            if StormX.lust >= 100:

                call Girl_Cumming (StormX)
                if action_context == "shift" or "_angry" in StormX.recent_history:
                    jump Storm_FA_After

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
                            jump Storm_FA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if StormX.SEXP >= 100 or approval_check(StormX, 1200, "LO"):
            pass
        elif counter == (5 + StormX.action_counter["fondle_ass"]):
            $ StormX.brows = "_confused"
            ch_s "Mmmm. . ."
        elif StormX.lust >= 80:
            pass
        elif counter == (15 + StormX.action_counter["fondle_ass"]) and StormX.SEXP >= 15 and not approval_check(StormX, 1500):
            $ StormX.brows = "_confused"
            menu:
                ch_s "I am sure that is fun, but could we try something different?"
                "Finish up.":
                    "You let go. . ."
                    jump Storm_FA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Storm_FA_After
                "No, this is fun.":
                    if approval_check(StormX, 1200) or approval_check(StormX, 500, "O"):
                        $ StormX.change_stat("love", 200, -5)
                        $ StormX.change_stat("obedience", 50, 3)
                        $ StormX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ StormX.change_face("_angry", 1)
                        call Storm_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_s "Well however much you are enjoying yourself, I need to take a break."
                        $ StormX.change_stat("love", 50, -3, 1)
                        $ StormX.change_stat("love", 80, -4, 1)
                        $ StormX.change_stat("obedience", 30, -1, 1)
                        $ StormX.change_stat("obedience", 50, -1, 1)
                        $ StormX.recent_history.append("_angry")
                        $ StormX.daily_history.append("_angry")
                        jump Storm_FA_After


        call Escalation (StormX)

        if Round == 10:
            call Sex_Basic_Dialog (StormX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (StormX, 5)


    $ StormX.change_face("_bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (StormX, "done")

label Storm_FA_After:
    if not action_context:
        call Storm_Pos_Reset

    $ StormX.change_face("_sexy")

    $ StormX.action_counter["fondle_ass"] += 1
    $ StormX.remaining_actions -=1
    if StormX.PantsNum() <= 6 or StormX.upskirt:
        $ StormX.addiction_rate += 1
        if "addictive" in Player.traits:
            $ StormX.addiction_rate += 1

        call Partner_Like (StormX, 2)

    if StormX.action_counter["fondle_ass"] == 1:
        $ StormX.SEXP += 4
        if not action_context:
            if StormX.love >= 500 and "unsatisfied" not in StormX.recent_history:
                ch_s "That was. . . nice. . ."
            elif StormX.obedience <= 500 and Player.focus <= 20:
                $ StormX.change_face("_perplexed", 1)
                ch_s "Did you enjoy that?"

    $ approval_bonus = 0


    call checkout
    return





label Storm_Insert_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (StormX)

    if StormX.action_counter["finger_ass"]:
        $ approval_bonus += 25
    if StormX.PantsNum() > 6 or StormX.HoseNum() >= 5:
        $ approval_bonus -= 15
    if StormX.lust > 85:
        $ approval_bonus += 15
    if StormX.lust > 95:
        $ approval_bonus += 5
    if action_context == "shift":
        $ approval_bonus += 10
    if StormX.lust > 85 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in StormX.traits:
        $ approval_bonus += (4*Taboo)
    if StormX in Player.Harem or "sex friend" in StormX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in StormX.traits:
        $ approval_bonus -= 25
    if StormX.event_counter["forced"] and not StormX.Forced:
        $ approval_bonus -= 5*StormX.event_counter["forced"]

    if Taboo and "no_taboo" in StormX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in StormX.history:
        $ approval_bonus -= 20

    if "no_insert ass" in StormX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_insert ass" in StormX.recent_history else 0

    $ approval = approval_check(StormX, 1300, TabM = 3)

    if action_context == "auto":
        if approval:
            $ StormX.change_face("_surprised")
            $ StormX.change_stat("obedience", 90, 2)
            $ StormX.change_stat("obedience", 70, 2)
            $ StormX.change_stat("inhibition", 80, 2)
            $ StormX.change_stat("inhibition", 30, 2)
            "As you slide a finger in, [StormX.name] tightens around it in surprise, but seems into it."
            $ StormX.change_face("_sexy")
            jump Storm_IA_Prep
        else:
            $ StormX.change_face("_surprised")
            $ StormX.change_stat("love", 80, -2)
            $ StormX.change_stat("obedience", 50, -3)
            ch_s "You go too far, [StormX.player_petname]."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "finger_ass" in StormX.daily_history:
        $ StormX.change_face("_sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax, gently. . .",
            "Mmm. . ."])
        ch_s "[Line]"

    if approval >= 2:
        if StormX.Forced:
            $ StormX.change_face("_sad")
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
            $ StormX.change_stat("obedience", 90, 1)
            $ StormX.change_stat("inhibition", 60, 1)
            ch_s "If you must. . ."
        else:
            $ StormX.change_face("_sexy", 1)
            $ StormX.eyes = "_closed"
            $ StormX.change_stat("love", 90, 1)
            $ StormX.change_stat("inhibition", 50, 3)
            $ StormX.change_stat("lust", 200, 3)
            ch_s "Mmmmm. . ."
        $ StormX.change_stat("obedience", 20, 1)
        $ StormX.change_stat("obedience", 60, 1)
        $ StormX.change_stat("inhibition", 70, 2)
        jump Storm_IA_Prep
    else:

        $ StormX.change_face("_angry", 1)
        if "no_insert ass" in StormX.recent_history:
            ch_s "Do not persist in this, [StormX.player_petname]."
        elif "no_insert ass" in StormX.daily_history:
            ch_s "I have already told you my answer."
        elif Taboo and "no_taboo" in StormX.daily_history:
            ch_s "This area is too public, [StormX.player_petname]."
        elif not StormX.action_counter["finger_ass"]:
            $ StormX.change_face("_perplexed", 1)
            ch_s "I am unsure about that. . ."
        else:
            $ StormX.change_face("_bemused")
            ch_s "I would rather not. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_insert ass" in StormX.daily_history:
                $ StormX.change_face("_bemused")
                ch_s "I appreciate your restraint, [StormX.player_petname]."
                return
            "Maybe later?" if "no_insert ass" not in StormX.daily_history:
                $ StormX.change_face("_sexy")
                ch_s "I will give it some thought, [StormX.player_petname]."
                $ StormX.change_stat("love", 80, 2)
                $ StormX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ StormX.recent_history.append("no_taboo")
                    $ StormX.daily_history.append("no_taboo")
                $ StormX.recent_history.append("no_insert ass")
                $ StormX.daily_history.append("no_insert ass")
                return
            "I think you'd really enjoy it. . .":
                if approval:
                    $ StormX.change_face("_sexy")
                    $ StormX.change_stat("obedience", 90, 2)
                    $ StormX.change_stat("obedience", 50, 2)
                    ch_s "You may be correct. . ."
                    $ StormX.change_stat("inhibition", 70, 3)
                    $ StormX.change_stat("inhibition", 40, 2)
                    jump Storm_IA_Prep
                else:
                    $ StormX.change_face("_bemused")
                    ch_s "I do not think that I would."
            "[[Slide a finger in anyway]":

                $ approval = approval_check(StormX, 950, "OI", TabM = 3)
                if approval > 1 or (approval and StormX.Forced):
                    $ StormX.change_face("_surprised", 1)
                    $ StormX.change_stat("love", 70, -5, 1)
                    $ StormX.change_stat("love", 200, -2)
                    ch_s "That was unexpected. . ."
                    $ StormX.change_face("_sad")
                    $ StormX.change_stat("obedience", 50, 4)
                    $ StormX.change_stat("inhibition", 80, 1)
                    $ StormX.change_stat("inhibition", 60, 3)
                    if approval < 2:
                        $ StormX.Forced = 1
                    jump Storm_IA_Prep
                else:
                    $ StormX.change_stat("love", 200, -15)
                    $ StormX.change_face("_angry", 1)
                    "She slaps your hand away."
                    $ StormX.recent_history.append("_angry")
                    $ StormX.daily_history.append("_angry")

    if "no_insert ass" in StormX.daily_history:
        ch_s "I have been clear on this."
        $ StormX.recent_history.append("_angry")
        $ StormX.daily_history.append("_angry")
    elif StormX.Forced:
        $ StormX.change_face("_angry", 1)
        ch_s "You go too far."
        if approval_check(StormX, 500, "I"):
            $ StormX.change_stat("lust", 80, 10)
        else:
            $ StormX.change_stat("lust", 50, 3)
        $ StormX.change_stat("obedience", 50, -2)
        $ StormX.recent_history.append("_angry")
        $ StormX.daily_history.append("_angry")
    elif Taboo:
        $ StormX.change_face("_angry", 1)
        $ StormX.recent_history.append("no_taboo")
        $ StormX.daily_history.append("no_taboo")
        ch_s "I should not be seen doing that."
    elif StormX.action_counter["finger_ass"]:
        $ StormX.change_face("_sad")
        ch_s "No, I do not think so."
    else:
        $ StormX.change_face("_surprised")
        ch_s "No, I do not think so."
        $ StormX.change_face()
    $ StormX.recent_history.append("no_insert ass")
    $ StormX.daily_history.append("no_insert ass")
    $ approval_bonus = 0
    return


label Storm_IA_Prep:
    if offhand_action == "finger_ass":
        return

    call Storm_Pussy_Launch ("finger_ass")

    if action_context == StormX:

        $ action_context = 0
        if (StormX.legs and not StormX.upskirt) or (StormX.underwear and not StormX.underwear_pulled_down):

            if approval_check(StormX, 1250, TabM = 1) or (StormX.SeenPussy and approval_check(StormX, 500) and not Taboo):
                $ StormX.upskirt = 1
                $ StormX.underwear_pulled_down = 1
                $ Line = 0
                if StormX.PantsNum() == 5:
                    $ Line = StormX.name + " hikes up her_skirt"
                elif StormX.PantsNum() >= 6:
                    $ Line = StormX.name + " pulls down her " + StormX.legs
                else:
                    $ Line = 0
                if StormX.underwear:
                    if Line:

                        "[Line] and pulls her [StormX.underwear] out of the way."
                        "She then grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
                    else:

                        "She pulls her [StormX.underwear] out of the way, and then presses your hand against her asshole."
                        "She clearly intends for you to get to work."
                else:

                    "[Line], and then presses your hand against her asshole."
                    "She clearly intends for you to get to work."
                call Storm_First_Bottomless (1)
            else:
                "[StormX.name] grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
        else:
            "[StormX.name] grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ StormX.change_stat("inhibition", 80, 3)
                $ StormX.change_stat("inhibition", 50, 2)
                "You press your finger into it."
            "Praise her.":
                $ StormX.change_face("_sexy", 1)
                $ StormX.change_stat("inhibition", 80, 3)
                ch_p "Dirty girl, [StormX.petname]."
                $ StormX.nameCheck()
                "You press your finger into it."
                $ StormX.change_stat("love", 85, 1)
                $ StormX.change_stat("obedience", 90, 1)
                $ StormX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your hand back."
                $ StormX.change_face("_surprised")
                $ StormX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [StormX.petname]."
                $ StormX.nameCheck()
                "[StormX.name] pulls back."
                $ StormX.change_stat("obedience", 90, 1)
                $ StormX.change_stat("obedience", 50, 1)
                $ StormX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ StormX.add_word(1,"refused","refused")
                return


    if not StormX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (StormX)
        if "_angry" in StormX.recent_history:
            return

    $ approval_bonus = 0
    if not StormX.action_counter["finger_ass"]:
        if StormX.Forced:
            $ StormX.change_stat("love", 90, -50)
            $ StormX.change_stat("obedience", 70, 60)
            $ StormX.change_stat("inhibition", 80, 35)
        else:
            $ StormX.change_stat("love", 90, 10)
            $ StormX.change_stat("obedience", 70, 20)
            $ StormX.change_stat("inhibition", 80, 25)

    if Taboo:
        $ StormX.inhibition += int(Taboo/10)
        $ StormX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ StormX.drain_word("no_taboo")
    $ StormX.drain_word("no_insert ass")
    $ StormX.recent_history.append("finger_ass")
    $ StormX.daily_history.append("finger_ass")
    call Storm_Pussy_Launch ("finger_ass")

label Storm_IA_Cycle:
    while Round > 0:
        call ViewShift (StormX, StormX.pose, 0, "finger_ass")
        call shift_focus (StormX)
        $ StormX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (StormX)
                    $ counter += 1
                    $ Round -= 1
                    jump Storm_IA_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (StormX, "menu")
                    jump Storm_IA_Cycle
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
                                    "Pull out and start rubbing again.":
                                        $ action_context = "pullback"
                                        call Storm_IA_After
                                        call Storm_Fondle_Ass
                                    "I want to lick your asshole.":
                                        $ action_context = "shift"
                                        call Storm_IA_After
                                        call Storm_Lick_Ass
                                    "Just start licking.":
                                        $ action_context = "auto"
                                        call Storm_IA_After
                                        call Storm_Lick_Ass
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Storm_IA_After
                                        call Storm_Dildo_Ass
                                    "Never Mind":
                                        jump Storm_IA_Cycle
                            else:
                                call Sex_Basic_Dialog (StormX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Storm_IA_After
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
                                    jump Storm_IA_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Storm_IA_Cycle
                                "Never mind":
                                    jump Storm_IA_Cycle

                        "Show her feet" if not ShowFeet and (StormX.pose == "doggy" or StormX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (StormX.pose == "doggy" or StormX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [StormX.name]":

                            call Girl_Undress (StormX)
                        "Clean up [StormX.name] (locked)" if not StormX.spunk:
                            pass
                        "Clean up [StormX.name]" if StormX.spunk:
                            call Girl_Cleanup (StormX, "ask")
                        "Never mind":
                            jump Storm_IA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Storm_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Storm_IA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Storm_Pos_Reset
                    $ Line = 0
                    jump Storm_IA_After


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
                if "_angry" in StormX.recent_history:
                    call Storm_Pos_Reset
                    return
                $ StormX.change_stat("lust", 200, 5)
                if 100 > StormX.lust >= 70 and StormX.session_orgasms < 2:
                    $ StormX.recent_history.append("unsatisfied")
                    $ StormX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Storm_IA_After
                $ Line = "came"

            if StormX.lust >= 100:

                call Girl_Cumming (StormX)
                if action_context == "shift" or "_angry" in StormX.recent_history:
                    jump Storm_IA_After

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
                            jump Storm_IA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if StormX.SEXP >= 100 or approval_check(StormX, 1200, "LO"):
            pass
        elif counter == (5 + StormX.action_counter["finger_ass"]):
            $ StormX.brows = "_confused"
            ch_s "Ooh, watch it, watch it. . ."
        elif StormX.lust >= 80:
            pass
        elif counter == (15 + StormX.action_counter["finger_ass"]) and StormX.SEXP >= 15 and not approval_check(StormX, 1500):
            $ StormX.brows = "_confused"
            menu:
                ch_s "I am sure that is fun, but could we try something different?"
                "Finish up.":
                    "You let go. . ."
                    jump Storm_IA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Storm_IA_After
                "No, this is fun.":
                    if approval_check(StormX, 1200) or approval_check(StormX, 500, "O"):
                        $ StormX.change_stat("love", 200, -5)
                        $ StormX.change_stat("obedience", 50, 3)
                        $ StormX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ StormX.change_face("_angry", 1)
                        call Storm_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_s "Well however much you are enjoying yourself, I need to take a break."
                        $ StormX.change_stat("love", 50, -3, 1)
                        $ StormX.change_stat("love", 80, -4, 1)
                        $ StormX.change_stat("obedience", 30, -1, 1)
                        $ StormX.change_stat("obedience", 50, -1, 1)
                        $ StormX.recent_history.append("_angry")
                        $ StormX.daily_history.append("_angry")
                        jump Storm_IA_After


        call Escalation (StormX)

        if Round == 10:
            call Sex_Basic_Dialog (StormX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (StormX, 5)


    $ StormX.change_face("_bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (StormX, "done")

label Storm_IA_After:
    if not action_context:
        call Storm_Pos_Reset

    $ StormX.change_face("_sexy")

    $ StormX.action_counter["finger_ass"] += 1
    $ StormX.remaining_actions -=1
    $ StormX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ StormX.addiction_rate += 1

    call Partner_Like (StormX, 2)

    if StormX.action_counter["finger_ass"] == 1:
        $ StormX.SEXP += 12
        if not action_context:
            if StormX.love >= 500 and "unsatisfied" not in StormX.recent_history:
                ch_s "That one caught me by surprise. . ."
            elif StormX.obedience <= 500 and Player.focus <= 20:
                $ StormX.change_face("_perplexed", 1)
                ch_s "did that work for you?"

    $ approval_bonus = 0


    call checkout
    return








label Storm_Lick_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (StormX)

    if StormX.action_counter["eat_ass"]:
        $ approval_bonus += 20
    if StormX.PantsNum() > 6 or StormX.HoseNum() >= 5:
        $ approval_bonus -= 25
    if StormX.lust > 95:
        $ approval_bonus += 20
    elif StormX.lust > 85:
        $ approval_bonus += 15
    if StormX.lust > 85 and action_context == "auto":
        $ approval_bonus += 10
    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in StormX.traits:
        $ approval_bonus += (4*Taboo)
    if StormX in Player.Harem or "sex friend" in StormX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in StormX.traits:
        $ approval_bonus -= 25
    if StormX.event_counter["forced"] and not StormX.Forced:
        $ approval_bonus -= 5*StormX.event_counter["forced"]

    if Taboo and "no_taboo" in StormX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in StormX.history:
        $ approval_bonus -= 20

    if "no_lick ass" in StormX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_lick ass" in StormX.recent_history else 0

    $ approval = approval_check(StormX, 1550, TabM = 4)

    if action_context == "auto":
        if approval:
            $ StormX.change_face("_surprised")
            $ StormX.change_stat("obedience", 90, 1)
            $ StormX.change_stat("inhibition", 80, 3)
            $ StormX.change_stat("inhibition", 40, 2)
            "As you crouch down and start to lick her asshole, [StormX.name] startles briefly, but then begins to melt."
            $ StormX.change_face("_sexy")
            jump Storm_LA_Prep
        else:
            $ StormX.change_face("_surprised")
            $ StormX.change_stat("love", 80, -2)
            $ StormX.change_stat("obedience", 50, -3)
            ch_s "[StormX.player_petname]! Not now. . ."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "eat_ass" in StormX.recent_history:
        $ StormX.change_face("_sexy", 1)
        ch_s "Mmmm, again? I suppose. . ."
        jump Storm_LA_Prep
    elif "eat_ass" in StormX.daily_history:
        $ StormX.change_face("_sexy", 1)
        ch_s "You didn't get enough earlier?"


    if approval >= 2:
        if StormX.Forced:
            $ StormX.change_face("_sad")
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
            $ StormX.change_stat("obedience", 90, 2)
            $ StormX.change_stat("inhibition", 60, 2)
            ch_s "If you must. . ."
        else:
            $ StormX.change_face("_sexy", 1)
            $ StormX.eyes = "_closed"
            $ StormX.change_stat("love", 90, 1)
            $ StormX.change_stat("inhibition", 60, 2)
            $ StormX.change_stat("lust", 200, 3)
            ch_s "Mmm. . . naughty."
        $ StormX.change_stat("obedience", 20, 1)
        $ StormX.change_stat("obedience", 60, 1)
        $ StormX.change_stat("inhibition", 80, 2)
        jump Storm_LA_Prep
    else:

        $ StormX.change_face("_angry", 1)
        if "no_lick ass" in StormX.recent_history:
            ch_s "Do not persist in this, [StormX.player_petname]."
        elif "no_lick ass" in StormX.daily_history:
            ch_s "I have already told you my answer."
        elif Taboo and "no_taboo" in StormX.daily_history:
            ch_s "This area is too public, [StormX.player_petname]."
        elif not StormX.action_counter["eat_ass"]:
            $ StormX.change_face("_bemused", 1)
            if StormX.love >= StormX.obedience and StormX.love >= StormX.inhibition:
                ch_s "Oh, that is a bit forward!"
            elif StormX.obedience >= StormX.inhibition:
                ch_s "That is what you want?"
            else:
                $ StormX.eyes = "_sexy"
                ch_s "Hmmm, an interesting proposal. . ."
        else:
            $ StormX.change_face("_bemused")
            ch_s "Not now, [StormX.player_petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no_lick ass" in StormX.daily_history:
                $ StormX.change_face("_bemused")
                ch_s "I appreciate your restraint, [StormX.player_petname]."
                return
            "I'm sure I can convince you later. . ." if "no_lick ass" not in StormX.daily_history:
                $ StormX.change_face("_sexy")
                ch_s "I will give it some thought, [StormX.player_petname]."
                $ StormX.change_stat("love", 80, 2)
                $ StormX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ StormX.recent_history.append("no_taboo")
                    $ StormX.daily_history.append("no_taboo")
                $ StormX.recent_history.append("no_lick ass")
                $ StormX.daily_history.append("no_lick ass")
                return
            "I think you'd really enjoy it. . .":
                if approval:
                    $ StormX.change_face("_sexy")
                    $ StormX.change_stat("obedience", 90, 2)
                    $ StormX.change_stat("obedience", 50, 2)
                    ch_s "Well. . . I might at that. . ."
                    $ StormX.change_stat("inhibition", 70, 3)
                    $ StormX.change_stat("inhibition", 40, 2)
                    jump Storm_LA_Prep
                else:
                    $ StormX.change_face("_sexy")
                    ch_s "I really do not think so."
            "[[Start licking anyway]":

                $ approval = approval_check(StormX, 1100, "OI", TabM = 4)
                if approval > 1 or (approval and StormX.Forced):
                    $ StormX.change_face("_sad")
                    $ StormX.change_stat("love", 70, -5, 1)
                    $ StormX.change_stat("love", 200, -2)
                    ch_s "If you must. . ."
                    $ StormX.change_stat("obedience", 50, 4)
                    $ StormX.change_stat("inhibition", 80, 1)
                    $ StormX.change_stat("inhibition", 60, 3)
                    if approval < 2:
                        $ StormX.Forced = 1
                    jump Storm_LA_Prep
                else:
                    $ StormX.change_stat("love", 200, -15)
                    $ StormX.change_face("_angry", 1)
                    "She shoves your head back."
                    $ StormX.recent_history.append("_angry")
                    $ StormX.daily_history.append("_angry")

    if "no_lick ass" in StormX.daily_history:
        ch_s "I have been clear on this."
        $ StormX.recent_history.append("_angry")
        $ StormX.daily_history.append("_angry")
    elif StormX.Forced:
        $ StormX.change_face("_angry", 1)
        ch_s "You go too far."
        if approval_check(StormX, 500, "I"):
            $ StormX.change_stat("lust", 80, 10)
        else:
            $ StormX.change_stat("lust", 50, 3)
        $ StormX.change_stat("obedience", 50, -2)
        $ StormX.recent_history.append("_angry")
        $ StormX.daily_history.append("_angry")
    elif Taboo:
        $ StormX.change_face("_angry", 1)
        $ StormX.recent_history.append("no_taboo")
        $ StormX.daily_history.append("no_taboo")
        ch_s "I should not be seen doing that."
    elif StormX.action_counter["eat_ass"]:
        $ StormX.change_face("_sad")
        ch_s "No, I do not think so."
    else:
        $ StormX.change_face("_surprised")
        ch_s "No, I do not think so."
        $ StormX.change_face()
    $ StormX.recent_history.append("no_lick ass")
    $ StormX.daily_history.append("no_lick ass")
    $ approval_bonus = 0
    return

label Storm_LA_Prep:
    if offhand_action == "eat_ass":
        return
    if not StormX.Forced and action_context != "auto":
        $ approval_bonus = 0
        if StormX.PantsNum() > 6:
            $ approval_bonus = 15
        call Bottoms_Off (StormX)
        if "_angry" in StormX.recent_history:
            return
    $ approval_bonus = 0
    call Storm_Pussy_Launch ("eat_ass")
    if not StormX.action_counter["eat_ass"]:
        if StormX.Forced:
            $ StormX.change_stat("love", 90, -30)
            $ StormX.change_stat("obedience", 70, 40)
            $ StormX.change_stat("inhibition", 80, 80)
        else:
            $ StormX.change_stat("love", 90, 35)
            $ StormX.change_stat("obedience", 70, 25)
            $ StormX.change_stat("inhibition", 80, 55)
    if Taboo:
        $ StormX.inhibition += int(Taboo/10)
        $ StormX.lust += int(Taboo/5)
    if action_context:
        $ renpy.pop_call()
        $ action_context = 0

    $ StormX.upskirt = 1
    if StormX.PantsNum() == 5:
        $ StormX.SeenPanties = 1
    call Storm_First_Bottomless (1)
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ StormX.drain_word("no_taboo")
    $ StormX.drain_word("no_lick ass")

    $ StormX.recent_history.append("lick") if "lick" not in StormX.recent_history else StormX.recent_history
    $ StormX.recent_history.append("ass") if "ass" not in StormX.recent_history else StormX.recent_history
    $ StormX.recent_history.append("eat_ass")

    $ StormX.daily_history.append("lick") if "lick" not in StormX.daily_history else StormX.recent_history
    $ StormX.daily_history.append("ass") if "ass" not in StormX.daily_history else StormX.recent_history
    $ StormX.daily_history.append("eat_ass")
    call Storm_Pussy_Launch ("eat_ass")

label Storm_LA_Cycle:
    if offhand_action == "kiss":
        $ offhand_action = 0
    while Round > 0:
        call ViewShift (StormX, StormX.pose, 0, "eat_ass")
        call shift_focus (StormX)
        $ StormX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (StormX)
                    $ counter += 1
                    $ Round -= 1
                    jump Storm_LA_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (StormX, "menu")
                    jump Storm_LA_Cycle
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
                                    "Switch to fondling.":
                                        $ action_context = "pullback"
                                        call Storm_LA_After
                                        call Storm_Fondle_Ass
                                    "I want to stick a finger in.":
                                        $ action_context = "shift"
                                        call Storm_LA_After
                                        call Storm_Insert_Ass
                                    "Just stick a finger in [[without asking].":
                                        $ action_context = "auto"
                                        call Storm_LA_After
                                        call Storm_Insert_Ass
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Storm_LA_After
                                        call Storm_Dildo_Ass
                                    "Never Mind":
                                        jump Storm_LA_Cycle
                            else:
                                call Sex_Basic_Dialog (StormX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Storm_LA_After
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
                                    jump Storm_LA_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Storm_LA_Cycle
                                "Never mind":
                                    jump Storm_LA_Cycle

                        "Show her feet" if not ShowFeet and (StormX.pose == "doggy" or StormX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (StormX.pose == "doggy" or StormX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [StormX.name]":

                            call Girl_Undress (StormX)
                        "Clean up [StormX.name] (locked)" if not StormX.spunk:
                            pass
                        "Clean up [StormX.name]" if StormX.spunk:
                            call Girl_Cleanup (StormX, "ask")
                        "Never mind":
                            jump Storm_LA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Storm_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Storm_LA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Storm_Pos_Reset
                    $ Line = 0
                    jump Storm_LA_After


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
                if "_angry" in StormX.recent_history:
                    call Storm_Pos_Reset
                    return
                $ StormX.change_stat("lust", 200, 5)
                if 100 > StormX.lust >= 70 and StormX.session_orgasms < 2:
                    $ StormX.recent_history.append("unsatisfied")
                    $ StormX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Storm_LA_After
                $ Line = "came"

            if StormX.lust >= 100:

                call Girl_Cumming (StormX)
                if action_context == "shift" or "_angry" in StormX.recent_history:
                    jump Storm_LA_After

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
                            jump Storm_LA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if StormX.SEXP >= 100 or approval_check(StormX, 1200, "LO"):
            pass
        elif counter == (5 + StormX.action_counter["eat_ass"]):
            $ StormX.brows = "_confused"
            ch_s "You are quite enthusiastic. . ."
        elif StormX.lust >= 80:
            pass
        elif counter == (15 + StormX.action_counter["eat_ass"]) and StormX.SEXP >= 15 and not approval_check(StormX, 1500):
            $ StormX.brows = "_confused"
            menu:
                ch_s "I am sure that is fun, but could we try something different?"
                "Finish up.":
                    "You let go. . ."
                    jump Storm_LA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Storm_LA_After
                "No, this is fun.":
                    if approval_check(StormX, 1200) or approval_check(StormX, 500, "O"):
                        $ StormX.change_stat("love", 200, -5)
                        $ StormX.change_stat("obedience", 50, 3)
                        $ StormX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ StormX.change_face("_angry", 1)
                        call Storm_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_s "Well however much you are enjoying yourself, I need to take a break."
                        $ StormX.change_stat("love", 50, -3, 1)
                        $ StormX.change_stat("love", 80, -4, 1)
                        $ StormX.change_stat("obedience", 30, -1, 1)
                        $ StormX.change_stat("obedience", 50, -1, 1)
                        $ StormX.recent_history.append("_angry")
                        $ StormX.daily_history.append("_angry")
                        jump Storm_LA_After


        call Escalation (StormX)

        if Round == 10:
            call Sex_Basic_Dialog (StormX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (StormX, 5)


    $ StormX.change_face("_bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (StormX, "done")

label Storm_LA_After:
    if not action_context:
        call Storm_Pos_Reset

    $ StormX.change_face("_sexy")

    $ StormX.action_counter["eat_ass"] += 1
    $ StormX.remaining_actions -=1
    if StormX.PantsNum() <= 6 or StormX.upskirt:
        $ StormX.addiction_rate += 1
        if "addictive" in Player.traits:
            $ StormX.addiction_rate += 1

    call Partner_Like (StormX, 2)

    if StormX.action_counter["eat_ass"] == 1:
        $ StormX.SEXP += 15
        if not action_context:
            if StormX.love >= 500 and "unsatisfied" not in StormX.recent_history:
                ch_s "That was. . . certainly interesting. . ."
            elif StormX.obedience <= 500 and Player.focus <= 20:
                $ StormX.change_face("_perplexed", 1)
                ch_s "Did you enjoy that?"

    $ approval_bonus = 0


    call checkout
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
