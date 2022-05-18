
label Laura_Fondle:

    $ LauraX.mouth = "_smile"
    if not LauraX.remaining_actions:
        ch_l "Maybe later, [LauraX.player_petname]"
        return
    menu:
        ch_l "Well? Where did you want to touch, [LauraX.player_petname]?"
        "Your breasts?" if LauraX.remaining_actions:
            jump Laura_Fondle_Breasts
        "Your thighs?" if LauraX.remaining_actions:
            jump Laura_Fondle_Thighs
        "Your pussy?" if LauraX.remaining_actions:
            jump Laura_Fondle_Pussy
        "Your Ass?" if LauraX.remaining_actions:
            jump Laura_Fondle_Ass
        "Never mind.":
            return
    return



label Laura_Fondle_Breasts:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (LauraX)


    if LauraX.action_counter["fondle_breasts"]:
        $ approval_bonus += 15
    if LauraX.lust > 75:
        $ approval_bonus += 20
    if "exhibitionist" in LauraX.traits:
        $ approval_bonus += (3*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in LauraX.traits:
        $ approval_bonus -= 20
    if LauraX.event_counter["forced"] and not LauraX.Forced:
        $ approval_bonus -= 5*LauraX.event_counter["forced"]

    if Taboo and "no_taboo" in LauraX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in LauraX.history:
        $ approval_bonus -= 20

    if "no_fondle breasts" in LauraX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle breasts" in LauraX.recent_history else 0

    $ approval = approval_check(LauraX, 950, TabM = 3)

    if action_context == "auto":
        if approval:
            $ LauraX.change_face("_sexy")
            $ LauraX.change_stat("obedience", 90, 1)
            $ LauraX.change_stat("obedience", 70, 2)
            $ LauraX.change_stat("inhibition", 70, 3)
            $ LauraX.change_stat("inhibition", 30, 2)
            "As you cup her breast, [LauraX.name] gently nods."
            jump Laura_FB_Prep
        else:
            $ LauraX.change_face("_surprised")
            $ LauraX.brows = "_confused"
            $ LauraX.change_stat("obedience", 50, -2)
            ch_l "Roll it back, [LauraX.player_petname]. . ."
            $ approval_bonus = 0
            $ offhand_action = 0
            return



    if approval:
        $ LauraX.change_face("_sexy", 1)
        if LauraX.Forced:
            $ LauraX.change_face("_sad")
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
        elif not Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "This does seem less. . . exposed."

    if "fondle_breasts" in LauraX.recent_history:
        $ LauraX.change_face("_sexy", 1)
        ch_l "Mmmm, again? I guess. . ."
        jump Laura_FB_Prep
    elif "fondle_breasts" in LauraX.daily_history:
        $ LauraX.change_face("_sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Chill. . .",
            "Mmm. . ."])
        ch_l "[Line]"

    if approval >= 2:
        $ LauraX.change_face("_bemused", 1)
        if LauraX.Forced:
            $ LauraX.change_face("_sad")
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
            $ LauraX.change_stat("obedience", 90, 1)
            $ LauraX.change_stat("inhibition", 60, 1)
        ch_l "Sure, sounds fun."
        $ LauraX.change_stat("love", 90, 1)
        $ LauraX.change_stat("inhibition", 50, 3)
        jump Laura_FB_Prep
    else:

        $ LauraX.change_face("_angry", 1)
        if "no_fondle breasts" in LauraX.recent_history:
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "no_taboo" in LauraX.daily_history and "no_fondle breasts" in LauraX.daily_history:
            ch_l "I've had enough of this today."
        elif "no_fondle breasts" in LauraX.daily_history:
            ch_l "Don't make me tell you again today."
        elif Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "I told you, not here, [LauraX.player_petname]."
        elif not LauraX.action_counter["fondle_breasts"]:
            $ LauraX.change_face("_bemused")
            ch_l "Look, I don't know if we're ready for that, [LauraX.player_petname]. . ."
        else:
            $ LauraX.change_face("_bemused")
            ch_l "Keep dreaming."
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle breasts" in LauraX.daily_history:
                $ LauraX.change_face("_bemused")
                ch_l "No worries."
                return
            "Maybe later?" if "no_fondle breasts" not in LauraX.daily_history:
                $ LauraX.change_face("_sexy")
                ch_l "Eh. Maybe."
                $ LauraX.change_stat("love", 80, 1)
                $ LauraX.change_stat("love", 50, 1)
                $ LauraX.change_stat("inhibition", 30, 2)
                if Taboo:
                    $ LauraX.recent_history.append("no_taboo")
                    $ LauraX.daily_history.append("no_taboo")
                $ LauraX.recent_history.append("no_fondle breasts")
                $ LauraX.daily_history.append("no_fondle breasts")
                return
            "Come on, Please?":
                if approval:
                    $ LauraX.change_face("_sexy")
                    $ LauraX.change_stat("obedience", 50, 2)
                    $ LauraX.change_stat("inhibition", 60, 3)
                    $ LauraX.change_stat("inhibition", 30, 2)
                    ch_l "Well if you're going to be a little bitch about it. . ."
                    jump Laura_FB_Prep
                else:
                    $ LauraX.change_face("_sexy")
                    ch_l "Well if you're going to be a little bitch about it. . ."
            "[[Grab her chest anyway]":


                $ approval = approval_check(LauraX, 350, "OI", TabM = 3)
                if approval > 1 or (approval and LauraX.Forced):
                    $ LauraX.change_face("_sad")
                    $ LauraX.change_stat("love", 70, -5, 1)
                    $ LauraX.change_stat("love", 20, -2, 1)
                    ch_l "Hey. . ."
                    ch_l "Eh, whatever. . ."
                    $ LauraX.change_stat("obedience", 90, 2)
                    $ LauraX.change_stat("obedience", 50, 4)
                    $ LauraX.change_stat("inhibition", 60, 3)
                    if approval < 2:
                        $ LauraX.Forced = 1
                    jump Laura_FB_Prep
                else:
                    $ LauraX.change_stat("love", 200, -10)
                    $ LauraX.change_face("_angry", 1)
                    "She slaps your hand away."
                    $ LauraX.recent_history.append("_angry")
                    $ LauraX.daily_history.append("_angry")

    if "no_fondle breasts" in LauraX.daily_history:
        ch_l "Listen to the words that are coming out of my mouth."
        $ LauraX.recent_history.append("_angry")
        $ LauraX.daily_history.append("_angry")
    elif LauraX.Forced:
        $ LauraX.change_face("_angry", 1)
        ch_l "No."
        $ LauraX.change_stat("lust", 60, 5)
        $ LauraX.change_stat("obedience", 50, -2)
        $ LauraX.recent_history.append("_angry")
        $ LauraX.daily_history.append("_angry")
    elif Taboo:
        $ LauraX.change_face("_angry", 1)
        $ LauraX.recent_history.append("no_taboo")
        $ LauraX.daily_history.append("no_taboo")
        ch_l "I try to stay off the radar."
    elif LauraX.action_counter["fondle_breasts"]:
        $ LauraX.change_face("_sad")
        ch_l "You'll have to earn that back."
    else:
        $ LauraX.change_face("_sexy")
        $ LauraX.mouth = "_sad"
        ch_l "No."
    $ LauraX.recent_history.append("no_fondle breasts")
    $ LauraX.daily_history.append("no_fondle breasts")
    $ approval_bonus = 0
    return


label Laura_FB_Prep:
    if primary_action == "kiss":
        $ primary_action = "fondle_breasts"
        return

    if offhand_action == "fondle_breasts":
        return

    call Laura_Breasts_Launch ("fondle_breasts")

    if action_context == LauraX:

        $ action_context = 0
        if (LauraX.top or LauraX.bra) and not LauraX.top_pulled_up:

            if approval_check(LauraX, 1250, TabM = 1) or (LauraX.SeenChest and approval_check(LauraX, 500) and not Taboo):
                $ LauraX.top_pulled_up = 1
                $ Line = LauraX.top if LauraX.top else LauraX.bra
                "With a hungry grin, [LauraX.name] pulls her [Line] up over her breasts."
                call Laura_First_Topless (1)
                $ Line = 0
                "She then grabs your arm and mashes your hand against her breast, clearly intending you to get to work."
            else:
                "[LauraX.name] grabs your arm and mashes your hand against her covered breast, clearly intending you to get to work."
        else:
            "[LauraX.name] grabs your arm and mashes your hand against her breast, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ LauraX.change_stat("inhibition", 80, 3)
                $ LauraX.change_stat("inhibition", 50, 2)
                "You start to fondle it."
            "Praise her.":
                $ LauraX.change_face("_sexy", 1)
                $ LauraX.change_stat("inhibition", 80, 3)
                ch_p "I like the initiative, [LauraX.petname]."
                $ LauraX.nameCheck()
                "You start to fondle it."
                $ LauraX.change_stat("love", 85, 1)
                $ LauraX.change_stat("obedience", 90, 1)
                $ LauraX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your hand back."
                $ LauraX.change_face("_surprised")
                $ LauraX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [LauraX.petname]."
                $ LauraX.nameCheck()
                "[LauraX.name] pulls back."
                $ LauraX.change_stat("obedience", 90, 1)
                $ LauraX.change_stat("obedience", 50, 1)
                $ LauraX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ LauraX.add_word(1,"refused","refused")
                return


    if not LauraX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Top_Off (LauraX)
        if "_angry" in LauraX.recent_history:
            return

    $ approval_bonus = 0
    if not LauraX.action_counter["fondle_breasts"]:
        if LauraX.Forced:
            $ LauraX.change_stat("love", 90, -20)
            $ LauraX.change_stat("obedience", 70, 25)
            $ LauraX.change_stat("inhibition", 80, 15)
        else:
            $ LauraX.change_stat("love", 90, 10)
            $ LauraX.change_stat("obedience", 70, 5)
            $ LauraX.change_stat("inhibition", 80, 15)

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
    $ LauraX.drain_word("no_fondle breasts")
    $ LauraX.recent_history.append("fondle_breasts")
    $ LauraX.daily_history.append("fondle_breasts")
    call Laura_Breasts_Launch ("fondle_breasts")

label Laura_FB_Cycle:
    while Round > 0:
        call ViewShift (LauraX, LauraX.pose, 0, "fondle_breasts")
        call shift_focus (LauraX)
        $ LauraX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (LauraX)
                    $ counter += 1
                    $ Round -= 1
                    jump Laura_FB_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (LauraX, "menu")
                    jump Laura_FB_Cycle
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
                                    "Ask to suck on them.":
                                        if LauraX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Laura_FB_After
                                            call Laura_Suck_Breasts
                                        else:
                                            call Sex_Basic_Dialog (LauraX, "tired")
                                    "Just suck on them without asking.":
                                        if LauraX.remaining_actions and multi_action:
                                            $ action_context = "auto"
                                            call Laura_FB_After
                                            call Laura_Suck_Breasts
                                        else:
                                            "As you lean in to suck on her breast, she grabs your head and pushes back."
                                            call Sex_Basic_Dialog (LauraX, "tired")
                                    "Never Mind":
                                        jump Laura_FB_Cycle
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
                                    jump Laura_FB_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Laura_FB_Cycle
                                "Never mind":
                                    jump Laura_FB_Cycle

                        "Show her feet" if not ShowFeet and (LauraX.pose == "doggy" or LauraX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (LauraX.pose == "doggy" or LauraX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [LauraX.name]":

                            call Girl_Undress (LauraX)
                        "Clean up [LauraX.name] (locked)" if not LauraX.spunk:
                            pass
                        "Clean up [LauraX.name]" if LauraX.spunk:
                            call Girl_Cleanup (LauraX, "ask")
                        "Never mind":
                            jump Laura_FB_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Laura_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Laura_FB_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Laura_Pos_Reset
                    $ Line = 0
                    jump Laura_FB_After


        call shift_focus (LauraX)
        call Sex_Dialog (LauraX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or LauraX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (LauraX)
                if "_angry" in LauraX.recent_history:
                    call Laura_Pos_Reset
                    return
                $ LauraX.change_stat("lust", 200, 5)
                if 100 > LauraX.lust >= 70 and LauraX.session_orgasms < 2:
                    $ LauraX.recent_history.append("unsatisfied")
                    $ LauraX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Laura_FB_After
                $ Line = "came"

            if LauraX.lust >= 100:

                call Girl_Cumming (LauraX)
                if action_context == "shift" or "_angry" in LauraX.recent_history:
                    jump Laura_FB_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in LauraX.recent_history and LauraX.SEXP >= 20:
                    "[LauraX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Laura_FB_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if LauraX.SEXP >= 100 or approval_check(LauraX, 1200, "LO"):
            pass
        elif counter == (5 + LauraX.action_counter["fondle_breasts"]):
            $ LauraX.brows = "_confused"
            ch_l "Enjoying yourself?"
        elif LauraX.lust >= 85:
            pass
        elif counter == (15 + LauraX.action_counter["fondle_breasts"]) and LauraX.SEXP >= 15 and not approval_check(LauraX, 1500):
            $ LauraX.brows = "_confused"
            menu:
                ch_l "Maybe it's time for something else, [LauraX.player_petname]?"
                "Finish up.":
                    "You let go. . ."
                    jump Laura_FB_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Laura_FB_After
                "No, this is fun.":
                    if approval_check(LauraX, 1200) or approval_check(LauraX, 500, "O"):
                        $ LauraX.change_stat("love", 200, -5)
                        $ LauraX.change_stat("obedience", 50, 3)
                        $ LauraX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ LauraX.change_face("_angry", 1)
                        call Laura_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_l "Well, I've got better things to be doing."
                        $ LauraX.change_stat("love", 50, -3, 1)
                        $ LauraX.change_stat("love", 80, -4, 1)
                        $ LauraX.change_stat("obedience", 30, -1, 1)
                        $ LauraX.change_stat("obedience", 50, -1, 1)
                        $ LauraX.recent_history.append("_angry")
                        $ LauraX.daily_history.append("_angry")
                        jump Laura_FB_After


        call Escalation (LauraX)

        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [LauraX.player_petname]."

        if LauraX.lust >= 50 and not LauraX.top_pulled_up and (LauraX.bra or LauraX.top):
            $ LauraX.top_pulled_up = 1
            "[LauraX.name] grunts and pulls her clothes aside."
            call Laura_First_Topless


    $ LauraX.change_face("_bemused", 0)
    $ Line = 0
    ch_l "Ok, [LauraX.player_petname], breaktime."

label Laura_FB_After:
    if not action_context:
        call Laura_Pos_Reset

    $ LauraX.change_face("_sexy")

    $ LauraX.action_counter["fondle_breasts"]+= 1
    $ LauraX.remaining_actions -=1
    $ LauraX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ LauraX.addiction_rate += 1

    call Partner_Like (LauraX, 2)

    if LauraX.action_counter["fondle_breasts"]== 1:
        $ LauraX.SEXP += 4
        if not action_context:
            if LauraX.love >= 500 and "unsatisfied" not in LauraX.recent_history:
                ch_l "Did you enjoy that?"
            elif LauraX.obedience <= 500 and Player.focus <= 20:
                $ LauraX.change_face("_perplexed", 1)
                ch_l "That worked out for you?"

    $ approval_bonus = 0


    call checkout
    return






label Laura_Suck_Breasts:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (LauraX)

    if LauraX.action_counter["suck_breasts"]:
        $ approval_bonus += 15
    if not LauraX.bra and not LauraX.top:
        $ approval_bonus += 15
    if LauraX.lust > 75:
        $ approval_bonus += 20
    if LauraX.lust > 75 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in LauraX.traits:
        $ approval_bonus += (4*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in LauraX.traits:
        $ approval_bonus -= 25
    if LauraX.event_counter["forced"] and not LauraX.Forced:
        $ approval_bonus -= 5*LauraX.event_counter["forced"]

    if Taboo and "no_taboo" in LauraX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in LauraX.history:
        $ approval_bonus -= 20

    if "no_suck breasts" in LauraX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_suck breasts" in LauraX.recent_history else 0

    $ approval = approval_check(LauraX, 1050, TabM = 4)

    if action_context == "auto":
        if approval:
            $ LauraX.change_face("_sexy")
            $ LauraX.change_stat("obedience", 90, 1)
            $ LauraX.change_stat("obedience", 70, 2)
            $ LauraX.change_stat("inhibition", 70, 3)
            $ LauraX.change_stat("inhibition", 30, 2)
            "As you dive in, [LauraX.name] seems a bit surprised, but just makes a little \"grunt.\""
            jump Laura_SB_Prep
        else:
            $ LauraX.change_face("_surprised")
            $ LauraX.change_stat("obedience", 50, -2)
            ch_l "Roll it back, [LauraX.player_petname]. . ."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "suck_breasts" in LauraX.recent_history:
        $ LauraX.change_face("_sexy", 1)
        ch_l "Mmmm, again? I guess. . ."
        jump Laura_SB_Prep
    elif "suck_breasts" in LauraX.daily_history:
        $ LauraX.change_face("_sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Chill. . .",
            "Mmm. . ."])
        ch_l "[Line]"

    if approval >= 2:
        $ LauraX.change_face("_bemused", 1)
        if LauraX.Forced:
            $ LauraX.change_face("_sad")
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
            $ LauraX.change_stat("obedience", 90, 1)
            $ LauraX.change_stat("inhibition", 60, 1)
        ch_l "Sure."
        $ LauraX.change_stat("love", 90, 1)
        $ LauraX.change_stat("inhibition", 50, 3)
        jump Laura_SB_Prep
    else:

        $ LauraX.change_face("_angry", 1)
        if "no_suck breasts" in LauraX.recent_history:
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "no_taboo" in LauraX.daily_history and "no_suck breasts" in LauraX.daily_history:
            ch_l "I told you, I couldn't be caught like that."
        elif "no_suck breasts" in LauraX.daily_history:
            ch_l "Don't make me tell you again today."
        elif Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "I told you, not here, [LauraX.player_petname]."
        elif not LauraX.action_counter["suck_breasts"]:
            $ LauraX.change_face("_bemused")
            ch_l "Let's work up to that maybe. ."
        else:
            $ LauraX.change_face("_bemused")
            ch_l "You wish."
        menu:
            extend ""
            "Sorry, never mind." if "no_suck breasts" in LauraX.daily_history:
                $ LauraX.change_face("_bemused")
                ch_l "It's cool."
                return
            "Maybe later?" if "no_suck breasts" not in LauraX.daily_history:
                $ LauraX.change_face("_sexy")
                ch_l "Maybe, [LauraX.player_petname]."
                $ LauraX.change_stat("love", 80, 1)
                $ LauraX.change_stat("love", 50, 1)
                $ LauraX.change_stat("inhibition", 30, 2)
                if Taboo:
                    $ LauraX.recent_history.append("no_taboo")
                    $ LauraX.daily_history.append("no_taboo")
                $ LauraX.recent_history.append("no_suck breasts")
                $ LauraX.daily_history.append("no_suck breasts")
                return
            "Come on, Please?":
                if approval:
                    $ LauraX.change_face("_sexy")
                    $ LauraX.change_stat("obedience", 90, 1)
                    $ LauraX.change_stat("obedience", 50, 2)
                    $ LauraX.change_stat("inhibition", 60, 3)
                    $ LauraX.change_stat("inhibition", 30, 2)
                    ch_l "Ok, fine. . ."
                    jump Laura_SB_Prep
                else:
                    $ LauraX.change_face("_sexy")
                    ch_l "Well if you're going to be a little bitch about it. . ."
            "[[Start sucking anyway]":

                $ approval = approval_check(LauraX, 450, "OI", TabM = 3)
                if approval > 1 or (approval and LauraX.Forced):
                    $ LauraX.change_face("_sad")
                    $ LauraX.change_stat("love", 70, -5, 1)
                    $ LauraX.change_stat("love", 20, -2, 1)
                    ch_l "Hmm. . . ok. . ."
                    $ LauraX.change_stat("obedience", 90, 2)
                    $ LauraX.change_stat("obedience", 50, 4)
                    $ LauraX.change_stat("inhibition", 60, 3)
                    if approval < 2:
                        $ LauraX.Forced = 1
                    jump Laura_SB_Prep
                else:
                    $ LauraX.change_stat("love", 200, -10)
                    $ LauraX.change_face("_angry", 1)
                    "She shoves your head back out."
                    $ LauraX.recent_history.append("_angry")
                    $ LauraX.daily_history.append("_angry")

    if "no_suck breasts" in LauraX.daily_history:
        ch_l "I don't like to repeat myself, [LauraX.player_petname]."
        $ LauraX.recent_history.append("_angry")
        $ LauraX.daily_history.append("_angry")
    elif LauraX.Forced:
        $ LauraX.change_face("_angry", 1)
        ch_l "Not worth it."
        $ LauraX.change_stat("lust", 60, 5)
        $ LauraX.change_stat("obedience", 50, -2)
        $ LauraX.recent_history.append("_angry")
        $ LauraX.daily_history.append("_angry")
    elif Taboo:
        $ LauraX.change_face("_angry", 1)
        $ LauraX.recent_history.append("no_taboo")
        $ LauraX.daily_history.append("no_taboo")
        ch_l "I try to stay off the radar."
    elif LauraX.action_counter["suck_breasts"]:
        $ LauraX.change_face("_sad")
        ch_l "You'll have to earn that back."
    else:
        $ LauraX.change_face("_sexy")
        $ LauraX.mouth = "_sad"
        ch_l "No."
    $ LauraX.recent_history.append("no_suck breasts")
    $ LauraX.daily_history.append("no_suck breasts")
    $ approval_bonus = 0
    return


label Laura_SB_Prep:

    if offhand_action == "suck_breasts":
        return

    call Laura_Breasts_Launch ("suck_breasts")

    if action_context == LauraX:

        $ action_context = 0
        if (LauraX.top or LauraX.bra) and not LauraX.top_pulled_up:

            if approval_check(LauraX, 1250, TabM = 1) or (LauraX.SeenChest and approval_check(LauraX, 500) and not Taboo):
                $ LauraX.top_pulled_up = 1
                $ Line = LauraX.top if LauraX.top else LauraX.bra
                "With a hungry grin, [LauraX.name] pulls her [Line] up over her breasts."
                call Laura_First_Topless (1)
                $ Line = 0
                "She then grabs your head and crams your face into her chest, clearly intending you to get to work."
            else:
                "[LauraX.name] grabs your head and crams your face into her chest, clearly intending you to get to work."
        else:
            "[LauraX.name] grabs your head and crams your face into her chest, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ LauraX.change_stat("inhibition", 80, 3)
                $ LauraX.change_stat("inhibition", 50, 2)
                "You start to run your tongue along her nipple."
            "Praise her.":
                $ LauraX.change_face("_sexy", 1)
                $ LauraX.change_stat("inhibition", 80, 3)
                ch_p "Mmm, I like this, [LauraX.petname]."
                $ LauraX.nameCheck()
                "You start to fondle it."
                $ LauraX.change_stat("love", 85, 1)
                $ LauraX.change_stat("obedience", 90, 1)
                $ LauraX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your head back."
                $ LauraX.change_face("_surprised")
                $ LauraX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [LauraX.petname]."
                $ LauraX.nameCheck()
                "[LauraX.name] pulls away."
                $ LauraX.change_stat("obedience", 90, 1)
                $ LauraX.change_stat("obedience", 50, 1)
                $ LauraX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ LauraX.add_word(1,"refused","refused")
                return


    if not LauraX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Top_Off (LauraX)
        if "_angry" in LauraX.recent_history:
            return

    $ approval_bonus = 0
    if not LauraX.action_counter["suck_breasts"]:
        if LauraX.Forced:
            $ LauraX.change_stat("love", 90, -25)
            $ LauraX.change_stat("obedience", 70, 25)
            $ LauraX.change_stat("inhibition", 80, 17)
        else:
            $ LauraX.change_stat("love", 90, 10)
            $ LauraX.change_stat("obedience", 70, 10)
            $ LauraX.change_stat("inhibition", 80, 15)

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
    $ LauraX.drain_word("no_suck breasts")
    $ LauraX.recent_history.append("suck_breasts")
    $ LauraX.daily_history.append("suck_breasts")
    call Laura_Breasts_Launch ("suck_breasts")

label Laura_SB_Cycle:
    if offhand_action == "kiss":
        $ offhand_action = 0
    while Round > 0:
        call ViewShift (LauraX, LauraX.pose, 0, "suck_breasts")
        call shift_focus (LauraX)
        $ LauraX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (LauraX)
                    $ counter += 1
                    $ Round -= 1
                    jump Laura_SB_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (LauraX, "menu")
                    jump Laura_SB_Cycle
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
                                    "Pull back to fondling.":
                                        if LauraX.remaining_actions and multi_action:
                                            $ action_context = "pullback"
                                            call Laura_SB_After
                                            call Laura_Fondle_Breasts
                                        else:
                                            "As you pull back, [LauraX.name] pushes you back in close."
                                            call Sex_Basic_Dialog (LauraX, "tired")
                                    "Never Mind":
                                        jump Laura_SB_Cycle
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
                                    jump Laura_SB_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Laura_SB_Cycle
                                "Never mind":
                                    jump Laura_SB_Cycle

                        "Show her feet" if not ShowFeet and (LauraX.pose == "doggy" or LauraX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (LauraX.pose == "doggy" or LauraX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [LauraX.name]":

                            call Girl_Undress (LauraX)
                        "Clean up [LauraX.name] (locked)" if not LauraX.spunk:
                            pass
                        "Clean up [LauraX.name]" if LauraX.spunk:
                            call Girl_Cleanup (LauraX, "ask")
                        "Never mind":
                            jump Laura_SB_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Laura_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Laura_SB_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Laura_Pos_Reset
                    $ Line = 0
                    jump Laura_SB_After


        call shift_focus (LauraX)
        call Sex_Dialog (LauraX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or LauraX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (LauraX)
                if "_angry" in LauraX.recent_history:
                    call Laura_Pos_Reset
                    return
                $ LauraX.change_stat("lust", 200, 5)
                if 100 > LauraX.lust >= 70 and LauraX.session_orgasms < 2:
                    $ LauraX.recent_history.append("unsatisfied")
                    $ LauraX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Laura_SB_After
                $ Line = "came"

            if LauraX.lust >= 100:

                call Girl_Cumming (LauraX)
                if action_context == "shift" or "_angry" in LauraX.recent_history:
                    jump Laura_SB_After

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
                            jump Laura_SB_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if LauraX.SEXP >= 100 or approval_check(LauraX, 1200, "LO"):
            pass
        elif counter == (5 + LauraX.action_counter["suck_breasts"]):
            $ LauraX.brows = "_sly"
            ch_l "This is kinda nice. . ."
        elif LauraX.lust >= 85:
            pass
        elif counter == (15 + LauraX.action_counter["suck_breasts"]) and LauraX.SEXP >= 15 and not approval_check(LauraX, 1500):
            $ LauraX.brows = "_confused"
            menu:
                ch_l "Maybe change things up a little?"
                "Finish up.":
                    "You let go. . ."
                    jump Laura_SB_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Laura_SB_After
                "No, this is fun.":
                    if approval_check(LauraX, 1200) or approval_check(LauraX, 500, "O"):
                        $ LauraX.change_stat("love", 200, -5)
                        $ LauraX.change_stat("obedience", 50, 3)
                        $ LauraX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ LauraX.change_face("_angry", 1)
                        call Laura_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_l "I'm kinda bored here."
                        $ LauraX.change_stat("love", 50, -3, 1)
                        $ LauraX.change_stat("love", 80, -4, 1)
                        $ LauraX.change_stat("obedience", 30, -1, 1)
                        $ LauraX.change_stat("obedience", 50, -1, 1)
                        $ LauraX.recent_history.append("_angry")
                        $ LauraX.daily_history.append("_angry")
                        jump Laura_SB_After


        call Escalation (LauraX)

        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [LauraX.player_petname]."

        if LauraX.lust >= 50 and not LauraX.top_pulled_up and (LauraX.bra or LauraX.top):
            $ LauraX.top_pulled_up = 1
            "[LauraX.name] grunts and pulls her clothes aside."
            call Laura_First_Topless


    $ LauraX.change_face("_bemused", 0)
    $ Line = 0
    ch_l "Ok, [LauraX.player_petname], breaktime."

label Laura_SB_After:
    if not action_context:
        call Laura_Pos_Reset

    $ LauraX.change_face("_sexy")

    $ LauraX.action_counter["suck_breasts"] += 1
    $ LauraX.remaining_actions -=1
    $ LauraX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ LauraX.addiction_rate += 1

    if Partner == "Kitty":
        call Partner_Like (LauraX, 2, 2)
    else:
        call Partner_Like (LauraX, 2)

    if LauraX.action_counter["suck_breasts"] == 1:
        $ LauraX.SEXP += 4
        if not action_context:
            if LauraX.love >= 500 and "unsatisfied" not in LauraX.recent_history:
                ch_l "That was kinda nice."
            elif LauraX.obedience <= 500 and Player.focus <= 20:
                $ LauraX.change_face("_perplexed", 1)
                ch_l "Did you get enough?"

    $ approval_bonus = 0


    call checkout
    return





label Laura_Fondle_Thighs:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (LauraX)

    if LauraX.action_counter["fondle_thighs"]:
        $ approval_bonus += 10
    if LauraX.PantsNum() >= 6 or LauraX.HoseNum() >= 5:
        $ approval_bonus -= 5
    if LauraX.lust > 75:
        $ approval_bonus += 10
    if "exhibitionist" in LauraX.traits:
        $ approval_bonus += Taboo
    if LauraX in Player.Harem or "sex friend" in LauraX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in LauraX.traits:
        $ approval_bonus -= 25
    if LauraX.event_counter["forced"] and not LauraX.Forced:
        $ approval_bonus -= 5*LauraX.event_counter["forced"]

    if Taboo and "no_taboo" in LauraX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in LauraX.history:
        $ approval_bonus -= 20

    if "no_fondle thighs" in LauraX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle thighs" in LauraX.recent_history else 0

    $ approval = approval_check(LauraX, 750, TabM=1)

    if action_context == "auto":
        if approval:
            $ LauraX.change_face("_sexy")
            $ LauraX.change_stat("obedience", 50, 1)
            $ LauraX.change_stat("inhibition", 30, 2)
            "As you caress her thigh, [LauraX.name] glances at you, and smiles."
            jump Laura_FT_Prep
        else:
            $ LauraX.change_face("_surprised")
            $ LauraX.change_stat("obedience", 50, -2)
            ch_l "Maybe we keep it above the waist, [LauraX.player_petname]."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if action_context == "pullback":
        $ LauraX.change_face("_surprised")
        $ LauraX.brows = "_sad"
        if LauraX.lust > 60:
            $ LauraX.change_stat("love", 70, -3)
        $ LauraX.change_stat("obedience", 90, 1)
        $ LauraX.change_stat("obedience", 70, 2)
        "As you pull back, [LauraX.name] looks a little annoyed."
        jump Laura_FT_Prep
    elif "fondle_thighs" in LauraX.recent_history:
        $ LauraX.change_face("_sexy", 1)
        ch_l "Mmmm, again? I guess. . ."
        jump Laura_FT_Prep
    elif "fondle_thighs" in LauraX.daily_history:
        $ LauraX.change_face("_sexy", 1)
        ch_l "You didn't get enough earlier?"

    if approval >= 2:
        $ LauraX.change_face("_bemused", 1)
        if LauraX.Forced:
            $ LauraX.change_face("_sad")
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("obedience", 90, 1)
            $ LauraX.change_stat("inhibition", 60, 1)
        ch_l "Ok [LauraX.player_petname], go ahead."
        $ LauraX.change_stat("love", 90, 1)
        $ LauraX.change_stat("inhibition", 50, 3)
        jump Laura_FT_Prep
    else:

        $ LauraX.change_face("_angry", 1)
        if "no_fondle thighs" in LauraX.recent_history:
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "no_taboo" in LauraX.daily_history and "no_fondle thighs" in LauraX.daily_history:
            ch_l "I told you not to touch me like that in public!"
        elif "no_fondle thighs" in LauraX.daily_history:
            ch_l "Don't make me tell you again today."
        elif Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "I told you, not here, [LauraX.player_petname]."
        elif not LauraX.action_counter["fondle_thighs"]:
            $ LauraX.change_face("_bemused")
            ch_l "Seems a bit aggressive, [LauraX.player_petname]."
        else:
            $ LauraX.change_face("_bemused")
            ch_l "You wish."
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle thighs" in LauraX.daily_history:
                $ LauraX.change_face("_bemused")
                ch_l "It's cool."
                return
            "Maybe later?" if "no_fondle thighs" not in LauraX.daily_history:
                $ LauraX.change_face("_sexy")
                ch_l "Maybe?"
                $ LauraX.change_stat("love", 80, 1)
                $ LauraX.change_stat("inhibition", 30, 2)
                if Taboo:
                    $ LauraX.recent_history.append("no_taboo")
                    $ LauraX.daily_history.append("no_taboo")
                $ LauraX.recent_history.append("no_fondle thighs")
                $ LauraX.daily_history.append("no_fondle thighs")
                return
            "Come on, Please?":
                if approval:
                    $ LauraX.change_face("_sexy")
                    $ LauraX.change_stat("obedience", 60, 1)
                    $ LauraX.change_stat("obedience", 30, 2)
                    $ LauraX.change_stat("inhibition", 50, 1)
                    $ LauraX.change_stat("inhibition", 30, 2)
                    ch_l "Well if you're going to be a little bitch about it. . ."
                    jump Laura_FT_Prep
                else:
                    $ LauraX.change_face("_sexy")
                    ch_l "Well if you're going to be a little bitch about it. . ."
            "[[Start caressing her thigh anyway]":

                $ approval = approval_check(LauraX, 350, "OI", TabM = 2)
                if approval > 1 or (approval and LauraX.Forced):
                    $ LauraX.change_face("_sad")
                    $ LauraX.change_stat("love", 70, -5, 1)
                    $ LauraX.change_stat("love", 20, -2, 1)
                    ch_l "Hmmph."
                    $ LauraX.change_stat("obedience", 50, 3)
                    $ LauraX.change_stat("inhibition", 60, 2)
                    if approval < 2:
                        $ LauraX.Forced = 1
                    jump Laura_FT_Prep
                else:
                    $ LauraX.change_stat("love", 200, -8)
                    $ LauraX.change_face("_angry", 1)
                    "She slaps your hand away."
                    $ LauraX.recent_history.append("_angry")
                    $ LauraX.daily_history.append("_angry")

    if "no_fondle thighs" in LauraX.daily_history:
        ch_l "I don't like to repeat myself, [LauraX.player_petname]."
        $ LauraX.recent_history.append("_angry")
        $ LauraX.daily_history.append("_angry")
    elif LauraX.Forced:
        $ LauraX.change_face("_angry", 1)
        ch_l "No."
        $ LauraX.change_stat("lust", 50, 2)
        $ LauraX.change_stat("obedience", 50, -1)
        $ LauraX.recent_history.append("_angry")
        $ LauraX.daily_history.append("_angry")
    elif Taboo:
        $ LauraX.change_face("_angry", 1)
        $ LauraX.recent_history.append("no_taboo")
        $ LauraX.daily_history.append("no_taboo")
        ch_l "I try to stay off the radar."
    elif LauraX.action_counter["fondle_thighs"]:
        $ LauraX.change_face("_sad")
        ch_l "Keep your hands to yourself."
    else:
        $ LauraX.change_face("_sexy")
        $ LauraX.mouth = "_sad"
        ch_l "No."
    $ LauraX.recent_history.append("no_fondle thighs")
    $ LauraX.daily_history.append("no_fondle thighs")
    $ approval_bonus = 0
    return

label Laura_FT_Prep:
    if primary_action == "kiss":
        $ primary_action = "fondle_thighs"
        return

    if offhand_action == "fondle_thighs":
        return

    if not LauraX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (LauraX)
        if "_angry" in LauraX.recent_history:
            return

    $ approval_bonus = 0
    call Laura_Pussy_Launch ("fondle_thighs")
    if not LauraX.action_counter["fondle_thighs"]:
        if LauraX.Forced:
            $ LauraX.change_stat("love", 90, -10)
            $ LauraX.change_stat("obedience", 70, 15)
            $ LauraX.change_stat("inhibition", 80, 10)
        else:
            $ LauraX.change_stat("love", 90, 5)
            $ LauraX.change_stat("obedience", 70, 10)
            $ LauraX.change_stat("inhibition", 80, 15)

    if Taboo:
        $ LauraX.change_stat("lust", 200, (int(Taboo/5)))
        $ LauraX.change_stat("inhibition", 200, (2*(int(Taboo/5))))

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ LauraX.drain_word("no_taboo")
    $ LauraX.drain_word("no_fondle thighs")
    $ LauraX.recent_history.append("fondle_thighs")
    $ LauraX.daily_history.append("fondle_thighs")
    call Laura_Pussy_Launch ("fondle_thighs")

label Laura_FT_Cycle:
    while Round > 0:
        call ViewShift (LauraX, LauraX.pose, 0, "fondle_thighs")
        call shift_focus (LauraX)
        $ LauraX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (LauraX)
                    $ counter += 1
                    $ Round -= 1
                    jump Laura_FT_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (LauraX, "menu")
                    jump Laura_FT_Cycle
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
                                    "Can I do a little deeper?":
                                        if LauraX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Laura_FT_After
                                            call Laura_Fondle_Pussy
                                        else:
                                            call Sex_Basic_Dialog (LauraX, "tired")
                                    "Shift your hands a bit higher without asking":
                                        if LauraX.remaining_actions and multi_action:
                                            $ action_context = "auto"
                                            call Laura_FT_After
                                            call Laura_Fondle_Pussy
                                        else:
                                            "As your hands creep upwards, she grabs your wrists."
                                            call Sex_Basic_Dialog (LauraX, "tired")
                                    "Never Mind":
                                        jump Laura_FT_Cycle
                            else:
                                call Sex_Basic_Dialog (LauraX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Laura_FT_After
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
                                    jump Laura_FT_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Laura_FT_Cycle
                                "Never mind":
                                    jump Laura_FT_Cycle

                        "Show her feet" if not ShowFeet and (LauraX.pose == "doggy" or LauraX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (LauraX.pose == "doggy" or LauraX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [LauraX.name]":

                            call Girl_Undress (LauraX)
                        "Clean up [LauraX.name] (locked)" if not LauraX.spunk:
                            pass
                        "Clean up [LauraX.name]" if LauraX.spunk:
                            call Girl_Cleanup (LauraX, "ask")
                        "Never mind":
                            jump Laura_FT_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Laura_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Laura_FT_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Laura_Pos_Reset
                    $ Line = 0
                    jump Laura_FT_After


        call shift_focus (LauraX)
        call Sex_Dialog (LauraX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or LauraX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (LauraX)
                if "_angry" in LauraX.recent_history:
                    call Laura_Pos_Reset
                    return
                $ LauraX.change_stat("lust", 200, 5)
                if 100 > LauraX.lust >= 70 and LauraX.session_orgasms < 2 and LauraX.SEXP >= 20:
                    $ LauraX.recent_history.append("unsatisfied")
                    $ LauraX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Laura_FT_After
                $ Line = "came"

            if LauraX.lust >= 100:

                call Girl_Cumming (LauraX)
                if action_context == "shift" or "_angry" in LauraX.recent_history:
                    jump Laura_FT_After

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."


                if "unsatisfied" in LauraX.recent_history and LauraX.SEXP >= 20:
                    "[LauraX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Finish her?"
                        "Yes, keep going for a bit.":
                            $ Line = "You get back into it"
                        "No, I'm done.":
                            "You pull back."
                            jump Laura_FT_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if LauraX.SEXP >= 100 or approval_check(LauraX, 1200, "LO"):
            pass
        elif counter == (5 + LauraX.action_counter["fondle_thighs"]):
            $ LauraX.brows = "_confused"
            ch_l "Kinda nice, but. . ."
        elif counter == (15 + LauraX.action_counter["fondle_thighs"]) and LauraX.SEXP >= 15 and not approval_check(LauraX, 1500):
            $ LauraX.brows = "_confused"
            menu:
                ch_l "Maybe change things up a little?"
                "Finish up.":
                    "You let go. . ."
                    jump Laura_FT_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Laura_FT_After
                "No, this is fun.":
                    if approval_check(LauraX, 1200) or approval_check(LauraX, 500, "O"):
                        $ LauraX.change_stat("love", 200, -5)
                        $ LauraX.change_stat("obedience", 50, 3)
                        $ LauraX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ LauraX.change_face("_angry", 1)
                        call Laura_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_l "I'm kinda bored here."
                        $ LauraX.change_stat("love", 50, -3, 1)
                        $ LauraX.change_stat("love", 80, -4, 1)
                        $ LauraX.change_stat("obedience", 30, -1, 1)
                        $ LauraX.change_stat("obedience", 50, -1, 1)
                        $ LauraX.recent_history.append("_angry")
                        $ LauraX.daily_history.append("_angry")
                        jump Laura_FT_After


        call Escalation (LauraX)

        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [LauraX.player_petname]."


    $ LauraX.change_face("_bemused", 0)
    $ Line = 0
    ch_l "Ok, [LauraX.player_petname], breaktime."


label Laura_FT_After:
    if not action_context:
        call Laura_Pos_Reset

    $ LauraX.change_face("_sexy")

    $ LauraX.action_counter["fondle_thighs"]+= 1
    $ LauraX.remaining_actions -=1
    if LauraX.PantsNum() < 6 or LauraX.upskirt:
        $ LauraX.addiction_rate += 1
        if "addictive" in Player.traits:
            $ LauraX.addiction_rate += 1

    if Partner == "Kitty":
        call Partner_Like (LauraX, 2)
    else:
        call Partner_Like (LauraX, 1)

    if LauraX.action_counter["fondle_thighs"]== 1:
        $ LauraX.SEXP += 3
        if not action_context:
            if LauraX.love >= 500 and "unsatisfied" not in LauraX.recent_history:
                ch_l "That was. . . interesting."
            elif LauraX.obedience <= 500 and Player.focus <= 20:
                $ LauraX.change_face("_perplexed", 1)
                ch_l "Was that enough?"

    $ approval_bonus = 0


    call checkout
    return


label Laura_Fondle_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (LauraX)

    if LauraX.action_counter["fondle_pussy"]:
        $ approval_bonus += 20
    if LauraX.PantsNum() >= 6 or LauraX.HoseNum() >= 5:
        $ approval_bonus -= 10
    if LauraX.lust > 75:
        $ approval_bonus += 15
    if LauraX.lust > 75 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in LauraX.traits:
        $ approval_bonus += (2*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in LauraX.traits:
        $ approval_bonus -= 25
    if LauraX.event_counter["forced"] and not LauraX.Forced:
        $ approval_bonus -= 5*LauraX.event_counter["forced"]

    if Taboo and "no_taboo" in LauraX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in LauraX.history:
        $ approval_bonus -= 20

    if "no_fondle pussy" in LauraX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle pussy" in LauraX.recent_history else 0

    $ approval = approval_check(LauraX, 1050, TabM = 2)

    if action_context == "auto":
        if approval:
            $ LauraX.change_face("_sexy")
            $ LauraX.change_stat("obedience", 90, 1)
            $ LauraX.change_stat("obedience", 70, 2)
            $ LauraX.change_stat("inhibition", 70, 3)
            $ LauraX.change_stat("inhibition", 30, 2)
            "As your hand creeps up her thigh, [LauraX.name] seems a bit surprised, but then nods."
            jump Laura_FP_Prep
        else:
            $ LauraX.change_face("_surprised")
            $ LauraX.change_stat("obedience", 50, -2)
            ch_l "Roll it back, [LauraX.player_petname]. . ."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if action_context == "pullback":
        $ LauraX.change_face("_surprised")
        $ LauraX.brows = "_sad"
        if LauraX.lust > 80:
            $ LauraX.change_stat("love", 70, -4)
        $ LauraX.change_stat("obedience", 90, 1)
        $ LauraX.change_stat("obedience", 70, 2)
        "As your hand pulls out, [LauraX.name] gasps and looks upset."
        jump Laura_FP_Prep
    elif "fondle_pussy" in LauraX.recent_history:
        $ LauraX.change_face("_sexy", 1)
        ch_l "Mmmm, again? I guess. . ."
        jump Laura_FP_Prep
    elif "fondle_pussy" in LauraX.daily_history:
        $ LauraX.change_face("_sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Chill. . .",
            "Take it slow, I'm still shaking from earlier.",
            "Mmm. . ."])
        ch_l "[Line]"

    if approval >= 2:
        $ LauraX.change_face("_bemused", 1)
        if LauraX.Forced:
            $ LauraX.change_face("_sad")
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
            $ LauraX.change_stat("obedience", 90, 1)
            $ LauraX.change_stat("inhibition", 60, 1)
        ch_l "Mmmm, I couldn't refuse. . ."
        $ LauraX.change_stat("love", 90, 1)
        $ LauraX.change_stat("inhibition", 50, 3)
        jump Laura_FP_Prep
    else:

        $ LauraX.change_face("_angry", 1)
        if "no_fondle pussy" in LauraX.recent_history:
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "no_taboo" in LauraX.daily_history and "no_fondle pussy" in LauraX.daily_history:
            ch_l "I told you not to touch me like that in public!"
        elif "no_fondle pussy" in LauraX.daily_history:
            ch_l "Don't make me tell you again today."
        elif Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "I told you, not here, [LauraX.player_petname]."
        elif not LauraX.action_counter["fondle_pussy"]:
            $ LauraX.change_face("_bemused")
            ch_l "I don't think we're there yet, [LauraX.player_petname]. . ."
        else:
            $ LauraX.change_face("_bemused")
            ch_l "You wish."
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle pussy" in LauraX.daily_history:
                $ LauraX.change_face("_bemused")
                ch_l "It's cool, [LauraX.player_petname]."
                return
            "Maybe later?" if "no_fondle pussy" not in LauraX.daily_history:
                $ LauraX.change_face("_sexy")
                ch_l "Maybe, [LauraX.player_petname]."
                $ LauraX.change_stat("love", 80, 2)
                $ LauraX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ LauraX.recent_history.append("no_taboo")
                    $ LauraX.daily_history.append("no_taboo")
                $ LauraX.recent_history.append("no_fondle pussy")
                $ LauraX.daily_history.append("no_fondle pussy")
                return
            "Come on, Please?":
                if approval:
                    $ LauraX.change_face("_sexy")
                    $ LauraX.change_stat("obedience", 90, 2)
                    $ LauraX.change_stat("obedience", 50, 2)
                    $ LauraX.change_stat("inhibition", 70, 3)
                    $ LauraX.change_stat("inhibition", 40, 2)
                    ch_l "Oooh, beg for me. . ."
                    jump Laura_FP_Prep
                else:
                    $ LauraX.change_face("_sexy")
                    ch_l "No."
            "[[Start fondling anyway]":

                $ approval = approval_check(LauraX, 450, "OI", TabM = 2)
                if approval > 1 or (approval and LauraX.Forced):
                    $ LauraX.change_face("_sad")
                    $ LauraX.change_stat("love", 70, -5, 1)
                    $ LauraX.change_stat("love", 200, -2)
                    ch_l "Ok, fine. . ."
                    $ LauraX.change_stat("obedience", 50, 4)
                    $ LauraX.change_stat("inhibition", 80, 1)
                    $ LauraX.change_stat("inhibition", 60, 3)
                    if approval < 2:
                        $ LauraX.Forced = 1
                    jump Laura_FP_Prep
                else:
                    $ LauraX.change_stat("love", 200, -15)
                    $ LauraX.change_face("_angry", 1)
                    "She slaps your hand away."
                    $ LauraX.recent_history.append("_angry")
                    $ LauraX.daily_history.append("_angry")

    if "no_fondle pussy" in LauraX.daily_history:
        ch_l "I don't like to repeat myself, [LauraX.player_petname]."
        $ LauraX.recent_history.append("_angry")
        $ LauraX.daily_history.append("_angry")
    elif LauraX.Forced:
        $ LauraX.change_face("_angry", 1)
        ch_l "I don't think so, [LauraX.player_petname]."
        $ LauraX.change_stat("lust", 70, 5)
        $ LauraX.change_stat("obedience", 50, -2)
        $ LauraX.recent_history.append("_angry")
        $ LauraX.daily_history.append("_angry")
    elif Taboo:
        $ LauraX.change_face("_angry", 1)
        $ LauraX.recent_history.append("no_taboo")
        $ LauraX.daily_history.append("no_taboo")
        ch_l "I try to stay off the radar."
    elif LauraX.action_counter["fondle_pussy"]:
        $ LauraX.change_face("_sad")
        ch_l "Sorry, fingers outside."
    else:
        $ LauraX.change_face("_sexy")
        $ LauraX.mouth = "_sad"
        ch_l "No thank you, [LauraX.player_petname]."
    $ LauraX.recent_history.append("no_fondle pussy")
    $ LauraX.daily_history.append("no_fondle pussy")
    $ approval_bonus = 0
    return

label Laura_FP_Prep:
    if offhand_action == "fondle_pussy":
        return

    call Laura_Pussy_Launch ("fondle_pussy")

    if action_context == LauraX:

        $ action_context = 0
        if (LauraX.legs and not LauraX.upskirt) or (LauraX.underwear and not LauraX.underwear_pulled_down):

            if approval_check(LauraX, 1250, TabM = 1) or (LauraX.SeenPussy and approval_check(LauraX, 500) and not Taboo):
                $ LauraX.upskirt = 1
                $ LauraX.underwear_pulled_down = 1
                $ Line = 0
                if LauraX.PantsNum() == 5:
                    $ Line = LauraX.name + " hikes up her_skirt"
                elif LauraX.PantsNum() >= 6:
                    $ Line = LauraX.name + " pulls down her " + LauraX.legs
                else:
                    $ Line = 0
                if LauraX.underwear:
                    if Line:

                        "[Line] and pulls her [LauraX.underwear] out of the way."
                        "She then grabs your arm and then presses your hand against her crotch, clearly intending you to get to work."
                    else:

                        "She pulls her [LauraX.underwear] out of the way, and then presses your hand against her crotch."
                        "She clearly intends for you to get to work."
                else:

                    "[Line], and then presses your hand against her crotch."
                    "She clearly intends for you to get to work."
                call Laura_First_Bottomless (1)
            else:
                "[LauraX.name] grabs your arm and presses your hand against her crotch, clearly intending you to get to work."
        else:
            "[LauraX.name] grabs your arm and presses your hand against her crotch, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ LauraX.change_stat("inhibition", 80, 3)
                $ LauraX.change_stat("inhibition", 50, 2)
                "You start to run your fingers along her pussy."
            "Praise her.":
                $ LauraX.change_face("_sexy", 1)
                $ LauraX.change_stat("inhibition", 80, 3)
                ch_p "I like the initiative, [LauraX.petname]."
                $ LauraX.nameCheck()
                "You start to run your fingers along her pussy."
                $ LauraX.change_stat("love", 85, 1)
                $ LauraX.change_stat("obedience", 90, 1)
                $ LauraX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your hand back."
                $ LauraX.change_face("_surprised")
                $ LauraX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [LauraX.petname]."
                $ LauraX.nameCheck()
                "[LauraX.name] pulls back."
                $ LauraX.change_stat("obedience", 90, 1)
                $ LauraX.change_stat("obedience", 50, 1)
                $ LauraX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ LauraX.add_word(1,"refused","refused")
                return


    if not LauraX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (LauraX)
        if "_angry" in LauraX.recent_history:
            return
    $ approval_bonus = 0

    if not LauraX.action_counter["fondle_pussy"]:
        if LauraX.Forced:
            $ LauraX.change_stat("love", 90, -50)
            $ LauraX.change_stat("obedience", 70, 35)
            $ LauraX.change_stat("inhibition", 80, 25)
        else:
            $ LauraX.change_stat("love", 90, 10)
            $ LauraX.change_stat("obedience", 70, 10)
            $ LauraX.change_stat("inhibition", 80, 15)
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
    $ LauraX.drain_word("no_fondle pussy")
    $ LauraX.recent_history.append("fondle_pussy")
    $ LauraX.daily_history.append("fondle_pussy")
    call Laura_Pussy_Launch ("fondle_pussy")
    $ action_speed = 1

label Laura_FP_Cycle:
    while Round > 0:
        call ViewShift (LauraX, LauraX.pose, 0, "fondle_pussy")
        call shift_focus (LauraX)
        $ LauraX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass

                "I want to stick a finger in. . ." if action_speed != 2:
                    if LauraX.action_counter["finger_pussy"]:
                        $ action_speed = 2
                    else:
                        menu:
                            "Ask her first":
                                $ action_context = "shift"
                            "Don't ask first [[just stick it in]":
                                $ action_context = "auto"
                        call Laura_Insert_Pussy

                "Pull back a bit. . ." if action_speed == 2:
                    $ action_speed = 0
                "Slap her ass":

                    call Slap_Ass (LauraX)
                    $ counter += 1
                    $ Round -= 1
                    jump Laura_FP_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (LauraX, "menu")
                    jump Laura_FP_Cycle
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
                                    "I want to lick your pussy.":
                                        $ action_context = "shift"
                                        call Laura_FP_After
                                        call Laura_Lick_Pussy
                                    "Just start licking":
                                        $ action_context = "auto"
                                        call Laura_FP_After
                                        call Laura_Lick_Pussy
                                    "Pull back to the thighs":
                                        $ action_context = "pullback"
                                        call Laura_FP_After
                                        call Laura_Fondle_Thighs
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Laura_FP_After
                                        call Laura_Dildo_Pussy
                                    "Never Mind":
                                        jump Laura_FP_Cycle
                            else:
                                call Sex_Basic_Dialog (LauraX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Laura_FP_After
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
                                    jump Laura_FP_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Laura_FP_Cycle
                                "Never mind":
                                    jump Laura_FP_Cycle

                        "Show her feet" if not ShowFeet and (LauraX.pose == "doggy" or LauraX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (LauraX.pose == "doggy" or LauraX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [LauraX.name]":

                            call Girl_Undress (LauraX)
                        "Clean up [LauraX.name] (locked)" if not LauraX.spunk:
                            pass
                        "Clean up [LauraX.name]" if LauraX.spunk:
                            call Girl_Cleanup (LauraX, "ask")
                        "Never mind":
                            jump Laura_FP_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Laura_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Laura_FP_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Laura_Pos_Reset
                    $ Line = 0
                    jump Laura_FP_After


        call shift_focus (LauraX)
        call Sex_Dialog (LauraX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or LauraX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (LauraX)
                if "_angry" in LauraX.recent_history:
                    call Laura_Pos_Reset
                    return
                $ LauraX.change_stat("lust", 200, 5)
                if 100 > LauraX.lust >= 70 and LauraX.session_orgasms < 2:
                    $ LauraX.recent_history.append("unsatisfied")
                    $ LauraX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Laura_FP_After
                $ Line = "came"

            if LauraX.lust >= 100:

                call Girl_Cumming (LauraX)
                if action_context == "shift" or "_angry" in LauraX.recent_history:
                    jump Laura_FP_After

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
                            jump Laura_FP_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if LauraX.SEXP >= 100 or approval_check(LauraX, 1200, "LO"):
            pass
        elif counter == (5 + LauraX.action_counter["fondle_pussy"]):
            $ LauraX.brows = "_confused"
            ch_l "Mmmm, you're enjoying that, huh?"
        elif LauraX.lust >= 80:
            pass
        elif counter == (15 + LauraX.action_counter["fondle_pussy"]) and LauraX.SEXP >= 15 and not approval_check(LauraX, 1500):
            $ LauraX.brows = "_confused"
            menu:
                ch_l "Maybe change things up a little?"
                "Finish up.":
                    "You let go. . ."
                    jump Laura_FP_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Laura_FP_After
                "No, this is fun.":
                    if approval_check(LauraX, 1200) or approval_check(LauraX, 500, "O"):
                        $ LauraX.change_stat("love", 200, -5)
                        $ LauraX.change_stat("obedience", 50, 3)
                        $ LauraX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ LauraX.change_face("_angry", 1)
                        call Laura_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_l "I'm kinda bored here."
                        $ LauraX.change_stat("love", 50, -3, 1)
                        $ LauraX.change_stat("love", 80, -4, 1)
                        $ LauraX.change_stat("obedience", 30, -1, 1)
                        $ LauraX.change_stat("obedience", 50, -1, 1)
                        $ LauraX.recent_history.append("_angry")
                        $ LauraX.daily_history.append("_angry")
                        jump Laura_FP_After


        call Escalation (LauraX)

        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [LauraX.player_petname]."


    $ LauraX.change_face("_bemused", 0)
    $ Line = 0
    ch_l "Ok, [LauraX.player_petname], breaktime."


label Laura_FP_After:
    if not action_context:
        call Laura_Pos_Reset

    $ LauraX.change_face("_sexy")

    $ LauraX.action_counter["fondle_pussy"] += 1
    $ LauraX.remaining_actions -=1
    if LauraX.PantsNum() < 6 or LauraX.upskirt:
        $ LauraX.addiction_rate += 1
        if "addictive" in Player.traits:
            $ LauraX.addiction_rate += 1

    call Partner_Like (LauraX, 2)

    if LauraX.action_counter["fondle_pussy"] == 1:
        $ LauraX.SEXP += 7
        if not action_context:
            if LauraX.love >= 500 and "unsatisfied" not in LauraX.recent_history:
                ch_l "You're really getting into the good stuff."
            elif LauraX.obedience <= 500 and Player.focus <= 20:
                $ LauraX.change_face("_perplexed", 1)
                ch_l "Did you find what you were looking for?"

    $ approval_bonus = 0


    call checkout
    return




label Laura_Insert_Pussy:
    call shift_focus (LauraX)
    if action_context == "auto":
        if approval_check(LauraX, 1100, TabM = 2):
            $ LauraX.change_face("_surprised")
            $ LauraX.change_stat("obedience", 90, 1)
            $ LauraX.change_stat("obedience", 70, 2)
            $ LauraX.change_stat("inhibition", 70, 3)
            $ LauraX.change_stat("inhibition", 30, 2)
            "As you slide a finger in, [LauraX.name] seems a bit surprised, but seems into it."
            jump Laura_IP_Prep
        else:
            $ LauraX.change_face("_surprised",2)
            $ LauraX.change_stat("love", 80, -2)
            $ LauraX.change_stat("obedience", 50, -3)
            ch_l "Oooh!"
            "She slaps your hand back."
            $ LauraX.change_face("_perplexed",1)
            ch_l "Watch your hands, or lose them."
            return

    if approval_check(LauraX, 1100, TabM = 2):
        if LauraX.Forced:
            $ LauraX.change_face("_sad")
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
            $ LauraX.change_stat("obedience", 90, 1)
            $ LauraX.change_stat("inhibition", 60, 1)
            ch_l "Going there, huh. . ."
        else:
            $ LauraX.change_face("_sexy", 1)
            $ LauraX.change_stat("love", 90, 1)
            $ LauraX.change_stat("inhibition", 50, 3)
            ch_l "Mmmmmm. . ."
        $ LauraX.change_stat("obedience", 20, 1)
        $ LauraX.change_stat("obedience", 60, 1)
        $ LauraX.change_stat("inhibition", 70, 2)
        jump Laura_IP_Prep
    else:

        $ LauraX.change_face("_bemused", 1)
        ch_l "Nope."
        $ LauraX.blushing = ""
    return


label Laura_IP_Prep:
    if not LauraX.action_counter["finger_pussy"]:
        $ LauraX.action_counter["finger_pussy"] = 1
        $ LauraX.SEXP += 10
        if LauraX.Forced:
            $ LauraX.change_stat("love", 90, -60)
            $ LauraX.change_stat("obedience", 70, 55)
            $ LauraX.change_stat("inhibition", 80, 35)
        else:
            $ LauraX.change_stat("love", 90, 10)
            $ LauraX.change_stat("obedience", 70, 20)
            $ LauraX.change_stat("inhibition", 80, 25)

    if not LauraX.Forced and action_context != "auto":
        call Girl_Undress (LauraX, "bottom")
        if "_angry" in LauraX.recent_history:
            return


    if Taboo:
        $ LauraX.inhibition += int(Taboo/10)
        $ LauraX.lust += int(Taboo/5)

    $ Line = 0
    $ action_speed = 2
    return







label Laura_Lick_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (LauraX)

    if LauraX.action_counter["eat_pussy"]:
        $ approval_bonus += 15
    if LauraX.PantsNum() >= 6 or LauraX.HoseNum() >= 5:
        $ approval_bonus -= 15
    if LauraX.lust > 95:
        $ approval_bonus += 20
    elif LauraX.lust > 85:
        $ approval_bonus += 15
    if action_context == "shift":
        $ approval_bonus += 10
    if LauraX.lust > 85 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in LauraX.traits:
        $ approval_bonus += (4*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in LauraX.traits:
        $ approval_bonus -= 25
    if LauraX.event_counter["forced"] and not LauraX.Forced:
        $ approval_bonus -= 5*LauraX.event_counter["forced"]

    if Taboo and "no_taboo" in LauraX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in LauraX.history:
        $ approval_bonus -= 20

    if "no_lick pussy" in LauraX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_lick pussy" in LauraX.recent_history else 0

    $ approval = approval_check(LauraX, 1250, TabM = 4)

    if action_context == "auto":
        if approval:
            $ LauraX.change_face("_surprised")
            $ LauraX.change_stat("obedience", 90, 1)
            $ LauraX.change_stat("obedience", 70, 2)
            $ LauraX.change_stat("inhibition", 70, 3)
            $ LauraX.change_stat("inhibition", 30, 2)
            "As you crouch down and start to lick her pussy, [LauraX.name] starts, but then softens."
            $ LauraX.change_face("_sexy")
            jump Laura_LP_Prep
        else:
            $ LauraX.change_face("_surprised")
            $ LauraX.change_stat("love", 80, -2)
            $ LauraX.change_stat("obedience", 50, -3)
            ch_l "Hey, good instincts, but maybe hold off?"
            $ LauraX.change_face("_perplexed",1)
            "She pushes your head back away from her."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "eat_pussy" in LauraX.recent_history:
        $ LauraX.change_face("_sexy", 1)
        ch_l "Mmmm, again? I guess. . ."
        jump Laura_LP_Prep
    elif "eat_pussy" in LauraX.daily_history:
        $ LauraX.change_face("_sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Huh? Again?",
            "I must have done something right.",
            "I do like this treatment. . .",
            "Mmm. . ."])
        ch_l "[Line]"

    if approval >= 2:
        if LauraX.Forced:
            $ LauraX.change_face("_sad")
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
            $ LauraX.change_stat("obedience", 90, 1)
            $ LauraX.change_stat("inhibition", 60, 1)
            ch_l "If you must. . ."
        else:
            $ LauraX.change_face("_sexy", 1)
            $ LauraX.eyes = "_closed"
            $ LauraX.change_stat("love", 90, 1)
            $ LauraX.change_stat("inhibition", 50, 3)
            $ LauraX.change_stat("lust", 200, 3)
            ch_l "Mmmmmm. . ."
        $ LauraX.change_stat("obedience", 20, 1)
        $ LauraX.change_stat("obedience", 60, 1)
        $ LauraX.change_stat("inhibition", 70, 2)
        jump Laura_LP_Prep
    else:

        $ LauraX.change_face("_angry", 1)
        if "no_lick pussy" in LauraX.recent_history:
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "no_taboo" in LauraX.daily_history and "no_lick pussy" in LauraX.daily_history:
            ch_l "You already got your answer!"
        elif "no_lick pussy" in LauraX.daily_history:
            ch_l "Don't make me tell you again today."
        elif Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "I told you, not here, [LauraX.player_petname]."
        elif not LauraX.action_counter["eat_pussy"]:
            $ LauraX.change_face("_bemused")
            ch_l "I'm not sure we're there yet, [LauraX.player_petname]. . ."
        else:
            $ LauraX.change_face("_bemused")
            ch_l "I'm really not cool with that. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_lick pussy" in LauraX.daily_history:
                $ LauraX.change_face("_bemused")
                ch_l "It's cool, [LauraX.player_petname]."
                return
            "I'm sure I can convince you later. . ." if "no_lick pussy" not in LauraX.daily_history:
                $ LauraX.change_face("_sexy")
                ch_l "I'll be thinking about it, [LauraX.player_petname]."
                $ LauraX.change_stat("love", 80, 2)
                $ LauraX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ LauraX.recent_history.append("no_taboo")
                    $ LauraX.daily_history.append("no_taboo")
                $ LauraX.recent_history.append("no_lick pussy")
                $ LauraX.daily_history.append("no_lick pussy")
                return
            "I think you'd really enjoy it. . .":
                if approval:
                    $ LauraX.change_face("_sexy")
                    $ LauraX.change_stat("obedience", 90, 2)
                    $ LauraX.change_stat("obedience", 50, 2)
                    ch_l "You make a good point. . ."
                    $ LauraX.change_stat("inhibition", 70, 3)
                    $ LauraX.change_stat("inhibition", 40, 2)
                    jump Laura_LP_Prep
                else:
                    $ LauraX.change_face("_sexy")
                    ch_l "I would, but still no, [LauraX.player_petname]."
            "[[Get in there anyway]":

                $ approval = approval_check(LauraX, 750, "OI", TabM = 4)
                if approval > 1 or (approval and LauraX.Forced):
                    $ LauraX.change_face("_sad")
                    $ LauraX.change_stat("love", 70, -5, 1)
                    $ LauraX.change_stat("love", 200, -2)
                    ch_l "If you insist. . ."
                    $ LauraX.change_stat("obedience", 50, 4)
                    $ LauraX.change_stat("inhibition", 80, 1)
                    $ LauraX.change_stat("inhibition", 60, 3)
                    if approval < 2:
                        $ LauraX.Forced = 1
                    jump Laura_LP_Prep
                else:
                    $ LauraX.change_stat("love", 200, -15)
                    $ LauraX.change_face("_angry", 1)
                    "She shoves your head back."
                    $ LauraX.recent_history.append("_angry")
                    $ LauraX.daily_history.append("_angry")

    if "no_lick pussy" in LauraX.daily_history:
        ch_l "I don't like to repeat myself, [LauraX.player_petname]."
        $ LauraX.recent_history.append("_angry")
        $ LauraX.daily_history.append("_angry")
    elif LauraX.Forced:
        $ LauraX.change_face("_angry", 1)
        ch_l "I really can't, [LauraX.player_petname]."
        $ LauraX.change_stat("lust", 80, 5)
        $ LauraX.change_stat("obedience", 50, -2)
        $ LauraX.recent_history.append("_angry")
        $ LauraX.daily_history.append("_angry")
    elif Taboo:
        $ LauraX.change_face("_angry", 1)
        $ LauraX.recent_history.append("no_taboo")
        $ LauraX.daily_history.append("no_taboo")
        ch_l "I try to stay off the radar."
    elif LauraX.action_counter["eat_pussy"]:
        $ LauraX.change_face("_sad")
        ch_l "Keep your head out of there."
    else:
        $ LauraX.change_face("_surprised")
        ch_l "Yeah, sorry."
        $ LauraX.change_face()
    $ LauraX.recent_history.append("no_lick pussy")
    $ LauraX.daily_history.append("no_lick pussy")
    $ approval_bonus = 0
    return

label Laura_LP_Prep:
    if offhand_action == "eat_pussy":
        return

    $ approval_bonus = 0
    call Laura_Pussy_Launch ("eat_pussy")

    if action_context == LauraX:

        $ action_context = 0
        if (LauraX.legs and not LauraX.upskirt) or (LauraX.underwear and not LauraX.underwear_pulled_down):

            if approval_check(LauraX, 1250, TabM = 1) or (LauraX.SeenPussy and approval_check(LauraX, 500) and not Taboo):
                $ LauraX.upskirt = 1
                $ LauraX.underwear_pulled_down = 1
                $ Line = 0
                if LauraX.PantsNum() == 5:
                    $ Line = LauraX.name + " hikes up her_skirt"
                elif LauraX.PantsNum() >= 6:
                    $ Line = LauraX.name + " pulls down her " + LauraX.legs
                else:
                    $ Line = 0
                if LauraX.underwear:
                    if Line:

                        "[Line] and pulls her [LauraX.underwear] out of the way."
                        "She then grabs your head and wraps her thighs around it, clearly intending you to get to work."
                    else:

                        "She pulls her [LauraX.underwear] out of the way, and then wraps her thighs around your head."
                        "She clearly intends for you to get to work."
                else:

                    "[Line], and then wraps her thighs around your head."
                    "She clearly intends for you to get to work."
                call Laura_First_Bottomless (1)
            else:
                "[LauraX.name] grabs your head and wraps her thighs around it, clearly intending you to get to work."
        else:
            "[LauraX.name] grabs your head and wraps her thighs around it, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ LauraX.change_stat("inhibition", 80, 3)
                $ LauraX.change_stat("inhibition", 50, 2)
                "You start licking."
            "Praise her.":
                $ LauraX.change_face("_sexy", 1)
                $ LauraX.change_stat("inhibition", 80, 3)
                ch_p "Mmm, I like this idea, [LauraX.petname]."
                $ LauraX.nameCheck()
                "You start licking."
                $ LauraX.change_stat("love", 85, 1)
                $ LauraX.change_stat("obedience", 90, 1)
                $ LauraX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your head away."
                $ LauraX.change_face("_surprised")
                $ LauraX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [LauraX.petname]."
                $ LauraX.nameCheck()
                "[LauraX.name] pulls back."
                $ LauraX.change_stat("obedience", 90, 1)
                $ LauraX.change_stat("obedience", 50, 1)
                $ LauraX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ LauraX.add_word(1,"refused","refused")
                return


    if not LauraX.Forced and action_context != "auto":
        $ approval_bonus = 0
        if LauraX.PantsNum() >= 6 and not LauraX.upskirt:
            $ approval_bonus = 15
        call Bottoms_Off (LauraX)
        if "_angry" in LauraX.recent_history:
            return

    if not LauraX.action_counter["eat_pussy"]:
        if LauraX.Forced:
            $ LauraX.change_stat("love", 90, -30)
            $ LauraX.change_stat("obedience", 70, 35)
            $ LauraX.change_stat("inhibition", 80, 75)
        else:
            $ LauraX.change_stat("love", 90, 35)
            $ LauraX.change_stat("obedience", 70, 15)
            $ LauraX.change_stat("inhibition", 80, 35)
    if Taboo:
        $ LauraX.inhibition += int(Taboo/10)
        $ LauraX.lust += int(Taboo/5)
    if action_context:
        $ renpy.pop_call()
        $ action_context = 0

    if LauraX.PantsNum() == 5:
        $ LauraX.upskirt = 1
        $ LauraX.SeenPanties = 1
    call Laura_First_Bottomless (1)

    $ Line = 0
    $ counter = 0
    if Taboo:
        $ LauraX.drain_word("no_taboo")
    $ LauraX.drain_word("no_lick pussy")
    $ LauraX.recent_history.append("eat_pussy")
    $ LauraX.daily_history.append("eat_pussy")
    call Laura_Pussy_Launch ("eat_pussy")

label Laura_LP_Cycle:
    if offhand_action == "kiss":
        $ offhand_action = 0
    while Round > 0:
        call ViewShift (LauraX, LauraX.pose, 0, "eat_pussy")
        call shift_focus (LauraX)
        $ LauraX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (LauraX)
                    $ counter += 1
                    $ Round -= 1
                    jump Laura_LP_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (LauraX, "menu")
                    jump Laura_LP_Cycle
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
                                    "Pull out and start rubbing again.":
                                        if LauraX.remaining_actions and multi_action:
                                            $ action_context = "pullback"
                                            call Laura_LP_After
                                            call Laura_Fondle_Pussy
                                        else:
                                            call Sex_Basic_Dialog (LauraX, "tired")
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Laura_LP_After
                                        call Laura_Dildo_Pussy
                                    "Never Mind":
                                        jump Laura_LP_Cycle
                            else:
                                call Sex_Basic_Dialog (LauraX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Laura_LP_After
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
                                    jump Laura_LP_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Laura_LP_Cycle
                                "Never mind":
                                    jump Laura_LP_Cycle

                        "Show her feet" if not ShowFeet and (LauraX.pose == "doggy" or LauraX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (LauraX.pose == "doggy" or LauraX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [LauraX.name]":

                            call Girl_Undress (LauraX)
                        "Clean up [LauraX.name] (locked)" if not LauraX.spunk:
                            pass
                        "Clean up [LauraX.name]" if LauraX.spunk:
                            call Girl_Cleanup (LauraX, "ask")
                        "Never mind":
                            jump Laura_LP_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Laura_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Laura_LP_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Laura_Pos_Reset
                    $ Line = 0
                    jump Laura_LP_After


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
                if "_angry" in LauraX.recent_history:
                    call Laura_Pos_Reset
                    return
                $ LauraX.change_stat("lust", 200, 5)
                if 100 > LauraX.lust >= 70 and LauraX.session_orgasms < 2:
                    $ LauraX.recent_history.append("unsatisfied")
                    $ LauraX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Laura_LP_After
                $ Line = "came"

            if LauraX.lust >= 100:

                call Girl_Cumming (LauraX)
                if action_context == "shift" or "_angry" in LauraX.recent_history:
                    jump Laura_LP_After

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
                            jump Laura_LP_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if LauraX.SEXP >= 100 or approval_check(LauraX, 1200, "LO"):
            pass
        elif counter == (5 + LauraX.action_counter["eat_pussy"]):
            $ LauraX.brows = "_confused"
            ch_l "Isn't it just delicious?"
        elif LauraX.lust >= 80:
            pass
        elif counter == (15 + LauraX.action_counter["eat_pussy"]) and LauraX.SEXP >= 15 and not approval_check(LauraX, 1500):
            $ LauraX.brows = "_confused"
            menu:
                ch_l "Maybe change things up a little?"
                "Finish up.":
                    "You let go. . ."
                    jump Laura_LP_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Laura_LP_After
                "No, this is fun.":
                    if approval_check(LauraX, 1200) or approval_check(LauraX, 500, "O"):
                        $ LauraX.change_stat("love", 200, -5)
                        $ LauraX.change_stat("obedience", 50, 3)
                        $ LauraX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ LauraX.change_face("_angry", 1)
                        call Laura_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_l "I'm kinda bored here."
                        $ LauraX.change_stat("love", 50, -3, 1)
                        $ LauraX.change_stat("love", 80, -4, 1)
                        $ LauraX.change_stat("obedience", 30, -1, 1)
                        $ LauraX.change_stat("obedience", 50, -1, 1)
                        $ LauraX.recent_history.append("_angry")
                        $ LauraX.daily_history.append("_angry")
                        jump Laura_LP_After


        call Escalation (LauraX)

        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [LauraX.player_petname]."


    $ LauraX.change_face("_bemused", 0)
    $ Line = 0
    ch_l "Ok, [LauraX.player_petname], breaktime."


label Laura_LP_After:
    if not action_context:
        call Laura_Pos_Reset

    $ LauraX.change_face("_sexy")

    $ LauraX.action_counter["eat_pussy"] += 1
    $ LauraX.remaining_actions -=1
    if LauraX.PantsNum() < 6 or LauraX.upskirt:
        $ LauraX.addiction_rate += 1
        if "addictive" in Player.traits:
            $ LauraX.addiction_rate += 1

    if Partner == "Rogue":
        call Partner_Like (LauraX, 3, 2)
    else:
        call Partner_Like (LauraX, 2)

    if LauraX.action_counter["eat_pussy"] == 1:
        $ LauraX.SEXP += 10
        if not action_context:
            if LauraX.love >= 500 and "unsatisfied" not in LauraX.recent_history:
                ch_l "That was a really good use of that tongue of yours."
            elif LauraX.obedience <= 500 and Player.focus <= 20:
                $ LauraX.change_face("_perplexed", 1)
                ch_l "I suppose we both got something out of that. . ."

    $ approval_bonus = 0


    call checkout
    return






label Laura_Fondle_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (LauraX)

    if LauraX.action_counter["fondle_ass"]:
        $ approval_bonus += 10
    if LauraX.PantsNum() >= 6 or LauraX.HoseNum() >= 5:
        $ approval_bonus -= 5
    if LauraX.lust > 75:
        $ approval_bonus += 15
    if "exhibitionist" in LauraX.traits:
        $ approval_bonus += Taboo
    if LauraX in Player.Harem or "sex friend" in LauraX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in LauraX.traits:
        $ approval_bonus -= 25
    if LauraX.event_counter["forced"] and not LauraX.Forced:
        $ approval_bonus -= 5*LauraX.event_counter["forced"]

    if Taboo and "no_taboo" in LauraX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in LauraX.history:
        $ approval_bonus -= 20

    if "no_fondle ass" in LauraX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle ass" in LauraX.recent_history else 0

    $ approval = approval_check(LauraX, 850, TabM=1)

    if action_context == "auto":
        if approval:
            $ LauraX.change_face("_surprised", 1)
            $ LauraX.change_stat("obedience", 70, 2)
            $ LauraX.change_stat("inhibition", 40, 2)
            "As your hand creeps down her backside, [LauraX.name] shivers a bit, and then relaxes."
            $ LauraX.change_face("_sexy")
            jump Laura_FA_Prep
        else:
            $ LauraX.change_face("_surprised")
            $ LauraX.change_stat("obedience", 50, -3)
            ch_l "Hands off, [LauraX.player_petname]."
            $ LauraX.change_face("_bemused")
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if action_context == "pullback":
        $ LauraX.change_face("_surprised")
        $ LauraX.brows = "_sad"
        if LauraX.lust > 80:
            $ LauraX.change_stat("love", 70, -4)
        $ LauraX.change_stat("obedience", 90, 1)
        $ LauraX.change_stat("obedience", 70, 2)
        "As your finger slides out, [LauraX.name] gasps and looks upset."
        jump Laura_FA_Prep
    elif "fondle_ass" in LauraX.recent_history:
        $ LauraX.change_face("_sexy", 1)
        ch_l "Mmmm, again? I guess. . ."
        jump Laura_FA_Prep
    elif "fondle_ass" in LauraX.daily_history:
        $ LauraX.change_face("_sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Mmm, you like that? . .",
            "Mmm. . ."])
        ch_l "[Line]"

    if approval >= 2:
        if LauraX.Forced:
            $ LauraX.change_face("_sad")
            $ LauraX.change_stat("love", 70, -2, 1)
            $ LauraX.change_stat("obedience", 90, 2)
            $ LauraX.change_stat("inhibition", 60, 2)
            ch_l "If you insist. . ."
        else:
            $ LauraX.change_face("bemused, 1")
            ch_l "Yeah, ok. . ."
        $ LauraX.change_stat("lust", 200, 3)
        $ LauraX.change_stat("obedience", 60, 1)
        $ LauraX.change_stat("inhibition", 70, 1)
        jump Laura_FA_Prep
    else:

        $ LauraX.change_face("_angry", 1)
        if "no_fondle ass" in LauraX.recent_history:
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "no_taboo" in LauraX.daily_history and "no_fondle ass" in LauraX.daily_history:
            ch_l "I told you not to touch me like that in public!"
        elif "no_fondle ass" in LauraX.daily_history:
            ch_l "Don't make me tell you again today."
        elif Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "I told you, not here, [LauraX.player_petname]."
        elif not LauraX.action_counter["fondle_ass"]:
            $ LauraX.change_face("_bemused")
            ch_l "Not yet, [LauraX.player_petname]. . ."
        else:
            $ LauraX.change_face("_bemused")
            ch_l "Let's not, ok [LauraX.player_petname]?"
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle ass" in LauraX.daily_history:
                $ LauraX.change_face("_bemused")
                ch_l "It's cool, [LauraX.player_petname]."
                return
            "Maybe later?" if "no_fondle ass" not in LauraX.daily_history:
                $ LauraX.change_face("_sexy")
                ch_l "Maybe?"
                $ LauraX.change_stat("love", 80, 2)
                $ LauraX.change_stat("inhibition", 50, 2)
                if Taboo:
                    $ LauraX.recent_history.append("no_taboo")
                    $ LauraX.daily_history.append("no_taboo")
                $ LauraX.recent_history.append("no_fondle ass")
                $ LauraX.daily_history.append("no_fondle ass")
                return
            "Just one good squeeze?":
                if approval:
                    $ LauraX.change_face("_sexy")
                    $ LauraX.change_stat("obedience", 90, 1)
                    $ LauraX.change_stat("obedience", 50, 2)
                    ch_l "Oooh, beg for me. . ."
                    $ LauraX.change_stat("inhibition", 70, 1)
                    $ LauraX.change_stat("inhibition", 40, 2)
                    jump Laura_FA_Prep
                else:
                    $ LauraX.change_face("_sexy")
                    ch_l "No."
            "[[Start fondling anyway]":

                $ approval = approval_check(LauraX, 250, "OI", TabM = 3)
                if approval > 1 or (approval and LauraX.Forced):
                    $ LauraX.change_face("_sad")
                    $ LauraX.change_stat("love", 70, -3, 1)
                    $ LauraX.change_stat("love", 200, -1)
                    ch_l "Fine, I guess."
                    $ LauraX.change_stat("obedience", 50, 3)
                    $ LauraX.change_stat("inhibition", 60, 3)
                    if approval < 2:
                        $ LauraX.Forced = 1
                    jump Laura_FA_Prep
                else:
                    $ LauraX.change_stat("love", 200, -10)
                    $ LauraX.change_face("_angry", 1)
                    "She slaps your hand away."
                    $ LauraX.recent_history.append("_angry")
                    $ LauraX.daily_history.append("_angry")

    if "no_fondle ass" in LauraX.daily_history:
        ch_l "I don't like to repeat myself, [LauraX.player_petname]."
        $ LauraX.recent_history.append("_angry")
        $ LauraX.daily_history.append("_angry")
    elif LauraX.Forced:
        $ LauraX.change_face("_angry", 1)
        ch_l "Do you want to keep those fingers?"
        $ LauraX.change_stat("lust", 60, 5)
        $ LauraX.change_stat("obedience", 50, -2)
        $ LauraX.recent_history.append("_angry")
        $ LauraX.daily_history.append("_angry")
    elif Taboo:
        $ LauraX.change_face("_angry", 1)
        $ LauraX.recent_history.append("no_taboo")
        $ LauraX.daily_history.append("no_taboo")
        ch_l "I try to stay off the radar."
    elif LauraX.action_counter["fondle_ass"]:
        $ LauraX.change_face("_sad")
        ch_l "Sorry, keep your hands to yourself."
    else:
        $ LauraX.change_face("_sexy")
        $ LauraX.mouth = "_sad"
        ch_l "No."
    $ LauraX.recent_history.append("no_fondle ass")
    $ LauraX.daily_history.append("no_fondle ass")
    $ approval_bonus = 0
    return

ch_l "Sorry, I don't even know how I got here. . ."
return

label Laura_FA_Prep:
    if offhand_action == "fondle_ass":
        return
    if not LauraX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (LauraX)
        if "_angry" in LauraX.recent_history:
            return
    $ approval_bonus = 0
    call Laura_Pussy_Launch ("fondle_ass")
    if not LauraX.action_counter["fondle_ass"]:
        if LauraX.Forced:
            $ LauraX.change_stat("love", 90, -20)
            $ LauraX.change_stat("obedience", 70, 20)
            $ LauraX.change_stat("inhibition", 80, 15)
        else:
            $ LauraX.change_stat("love", 90, 10)
            $ LauraX.change_stat("obedience", 70, 12)
            $ LauraX.change_stat("inhibition", 80, 20)
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
    $ LauraX.drain_word("no_fondle ass")
    $ LauraX.recent_history.append("fondle_ass")
    $ LauraX.daily_history.append("fondle_ass")
    call Laura_Pussy_Launch ("fondle_ass")

label Laura_FA_Cycle:
    while Round > 0:
        call ViewShift (LauraX, LauraX.pose, 0, "fondle_ass")
        call shift_focus (LauraX)
        $ LauraX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (LauraX)
                    $ counter += 1
                    $ Round -= 1
                    jump Laura_FA_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (LauraX, "menu")
                    jump Laura_FA_Cycle
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
                                    "I want to stick a finger in.":
                                        $ action_context = "shift"
                                        call Laura_FA_After
                                        call Laura_Insert_Ass
                                    "Just stick a finger in without asking.":
                                        $ action_context = "auto"
                                        call Laura_FA_After
                                        call Laura_Insert_Ass
                                    "I want to lick your asshole.":
                                        $ action_context = "shift"
                                        call Laura_FA_After
                                        call Laura_Lick_Ass
                                    "Just start licking.":
                                        $ action_context = "auto"
                                        call Laura_FA_After
                                        call Laura_Lick_Ass
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Laura_FA_After
                                        call Laura_Dildo_Ass
                                    "Never Mind":
                                        jump Laura_FA_Cycle
                            else:
                                call Sex_Basic_Dialog (LauraX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Laura_FA_After
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
                                    jump Laura_FA_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Laura_FA_Cycle
                                "Never mind":
                                    jump Laura_FA_Cycle

                        "Show her feet" if not ShowFeet and (LauraX.pose == "doggy" or LauraX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (LauraX.pose == "doggy" or LauraX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [LauraX.name]":

                            call Girl_Undress (LauraX)
                        "Clean up [LauraX.name] (locked)" if not LauraX.spunk:
                            pass
                        "Clean up [LauraX.name]" if LauraX.spunk:
                            call Girl_Cleanup (LauraX, "ask")
                        "Never mind":
                            jump Laura_FA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Laura_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Laura_FA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Laura_Pos_Reset
                    $ Line = 0
                    jump Laura_FA_After


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
                if "_angry" in LauraX.recent_history:
                    call Laura_Pos_Reset
                    return
                $ LauraX.change_stat("lust", 200, 5)
                if 100 > LauraX.lust >= 70 and LauraX.session_orgasms < 2 and LauraX.SEXP >= 20:
                    $ LauraX.recent_history.append("unsatisfied")
                    $ LauraX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Laura_FA_After
                $ Line = "came"

            if LauraX.lust >= 100:

                call Girl_Cumming (LauraX)
                if action_context == "shift" or "_angry" in LauraX.recent_history:
                    jump Laura_FA_After

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
                            jump Laura_FA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if LauraX.SEXP >= 100 or approval_check(LauraX, 1200, "LO"):
            pass
        elif counter == (5 + LauraX.action_counter["fondle_ass"]):
            $ LauraX.brows = "_confused"
            ch_l "Mmmm. . ."
        elif LauraX.lust >= 80:
            pass
        elif counter == (15 + LauraX.action_counter["fondle_ass"]) and LauraX.SEXP >= 15 and not approval_check(LauraX, 1500):
            $ LauraX.brows = "_confused"
            menu:
                ch_l "Maybe change things up a little?"
                "Finish up.":
                    "You let go. . ."
                    jump Laura_FA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Laura_FA_After
                "No, this is fun.":
                    if approval_check(LauraX, 1200) or approval_check(LauraX, 500, "O"):
                        $ LauraX.change_stat("love", 200, -5)
                        $ LauraX.change_stat("obedience", 50, 3)
                        $ LauraX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ LauraX.change_face("_angry", 1)
                        call Laura_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_l "I'm kinda bored here."
                        $ LauraX.change_stat("love", 50, -3, 1)
                        $ LauraX.change_stat("love", 80, -4, 1)
                        $ LauraX.change_stat("obedience", 30, -1, 1)
                        $ LauraX.change_stat("obedience", 50, -1, 1)
                        $ LauraX.recent_history.append("_angry")
                        $ LauraX.daily_history.append("_angry")
                        jump Laura_FA_After


        call Escalation (LauraX)

        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [LauraX.player_petname]."


    $ LauraX.change_face("_bemused", 0)
    $ Line = 0
    ch_l "Ok, [LauraX.player_petname], breaktime."


label Laura_FA_After:
    if not action_context:
        call Laura_Pos_Reset

    $ LauraX.change_face("_sexy")

    $ LauraX.action_counter["fondle_ass"] += 1
    $ LauraX.remaining_actions -=1
    if LauraX.PantsNum() < 6 or LauraX.upskirt:
        $ LauraX.addiction_rate += 1
        if "addictive" in Player.traits:
            $ LauraX.addiction_rate += 1

        call Partner_Like (LauraX, 2)

    if LauraX.action_counter["fondle_ass"] == 1:
        $ LauraX.SEXP += 4
        if not action_context:
            if LauraX.love >= 500 and "unsatisfied" not in LauraX.recent_history:
                ch_l "That was. . . nice. . ."
            elif LauraX.obedience <= 500 and Player.focus <= 20:
                $ LauraX.change_face("_perplexed", 1)
                ch_l "Did you enjoy that?"

    $ approval_bonus = 0


    call checkout
    return





label Laura_Insert_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (LauraX)

    if LauraX.action_counter["finger_ass"]:
        $ approval_bonus += 25
    if LauraX.PantsNum() >= 6 or LauraX.HoseNum() >= 5:
        $ approval_bonus -= 15
    if LauraX.lust > 85:
        $ approval_bonus += 15
    if LauraX.lust > 95:
        $ approval_bonus += 5
    if action_context == "shift":
        $ approval_bonus += 10
    if LauraX.lust > 85 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in LauraX.traits:
        $ approval_bonus += (4*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in LauraX.traits:
        $ approval_bonus -= 25
    if LauraX.event_counter["forced"] and not LauraX.Forced:
        $ approval_bonus -= 5*LauraX.event_counter["forced"]

    if Taboo and "no_taboo" in LauraX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in LauraX.history:
        $ approval_bonus -= 20

    if "no_insert ass" in LauraX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_insert ass" in LauraX.recent_history else 0

    $ approval = approval_check(LauraX, 1300, TabM = 3)

    if action_context == "auto":
        if approval:
            $ LauraX.change_face("_surprised")
            $ LauraX.change_stat("obedience", 90, 2)
            $ LauraX.change_stat("obedience", 70, 2)
            $ LauraX.change_stat("inhibition", 80, 2)
            $ LauraX.change_stat("inhibition", 30, 2)
            "As you slide a finger in, [LauraX.name] tightens around it in surprise, but seems into it."
            $ LauraX.change_face("_sexy")
            jump Laura_IA_Prep
        else:
            $ LauraX.change_face("_surprised")
            $ LauraX.change_stat("love", 80, -2)
            $ LauraX.change_stat("obedience", 50, -3)
            ch_l "Whoa, back off, [LauraX.player_petname]."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "finger_ass" in LauraX.daily_history:
        $ LauraX.change_face("_sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Chill. . .",
            "Mmm. . ."])
        ch_l "[Line]"

    if approval >= 2:
        if LauraX.Forced:
            $ LauraX.change_face("_sad")
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
            $ LauraX.change_stat("obedience", 90, 1)
            $ LauraX.change_stat("inhibition", 60, 1)
            ch_l "If you must. . ."
        else:
            $ LauraX.change_face("_sexy", 1)
            $ LauraX.eyes = "_closed"
            $ LauraX.change_stat("love", 90, 1)
            $ LauraX.change_stat("inhibition", 50, 3)
            $ LauraX.change_stat("lust", 200, 3)
            ch_l "Mmmmm. . ."
        $ LauraX.change_stat("obedience", 20, 1)
        $ LauraX.change_stat("obedience", 60, 1)
        $ LauraX.change_stat("inhibition", 70, 2)
        jump Laura_IA_Prep
    else:

        $ LauraX.change_face("_angry", 1)
        if "no_insert ass" in LauraX.recent_history:
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "no_taboo" in LauraX.daily_history and "no_insert ass" in LauraX.daily_history:
            ch_l "I told you that wasn't appropriate!"
        elif "no_insert ass" in LauraX.daily_history:
            ch_l "Don't make me tell you again today."
        elif Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "I told you, not here, [LauraX.player_petname]."
        elif not LauraX.action_counter["finger_ass"]:
            $ LauraX.change_face("_perplexed", 1)
            ch_l "That's really not my style. . ."
        else:
            $ LauraX.change_face("_bemused")
            ch_l "I'd rather not today. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_insert ass" in LauraX.daily_history:
                $ LauraX.change_face("_bemused")
                ch_l "It's cool, [LauraX.player_petname]."
                return
            "Maybe later?" if "no_insert ass" not in LauraX.daily_history:
                $ LauraX.change_face("_sexy")
                ch_l "It's. . . possible, [LauraX.player_petname]."
                $ LauraX.change_stat("love", 80, 2)
                $ LauraX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ LauraX.recent_history.append("no_taboo")
                    $ LauraX.daily_history.append("no_taboo")
                $ LauraX.recent_history.append("no_insert ass")
                $ LauraX.daily_history.append("no_insert ass")
                return
            "I think you'd really enjoy it. . .":
                if approval:
                    $ LauraX.change_face("_sexy")
                    $ LauraX.change_stat("obedience", 90, 2)
                    $ LauraX.change_stat("obedience", 50, 2)
                    ch_l "You're probably right. . ."
                    $ LauraX.change_stat("inhibition", 70, 3)
                    $ LauraX.change_stat("inhibition", 40, 2)
                    jump Laura_IA_Prep
                else:
                    $ LauraX.change_face("_bemused")
                    ch_l "I don't think that I would."
            "[[Slide a finger in anyway]":

                $ approval = approval_check(LauraX, 950, "OI", TabM = 3)
                if approval > 1 or (approval and LauraX.Forced):
                    $ LauraX.change_face("_surprised", 1)
                    $ LauraX.change_stat("love", 70, -5, 1)
                    $ LauraX.change_stat("love", 200, -2)
                    ch_l "Well hello there. . ."
                    $ LauraX.change_face("_sad")
                    $ LauraX.change_stat("obedience", 50, 4)
                    $ LauraX.change_stat("inhibition", 80, 1)
                    $ LauraX.change_stat("inhibition", 60, 3)
                    if approval < 2:
                        $ LauraX.Forced = 1
                    jump Laura_IA_Prep
                else:
                    $ LauraX.change_stat("love", 200, -15)
                    $ LauraX.change_face("_angry", 1)
                    "She slaps your hand away."
                    $ LauraX.recent_history.append("_angry")
                    $ LauraX.daily_history.append("_angry")

    if "no_insert ass" in LauraX.daily_history:
        ch_l "I don't like to repeat myself, [LauraX.player_petname]."
        $ LauraX.recent_history.append("_angry")
        $ LauraX.daily_history.append("_angry")
    elif LauraX.Forced:
        $ LauraX.change_face("_angry", 1)
        ch_l "I'm not going there today."
        if approval_check(LauraX, 500, "I"):
            $ LauraX.change_stat("lust", 80, 10)
        else:
            $ LauraX.change_stat("lust", 50, 3)
        $ LauraX.change_stat("obedience", 50, -2)
        $ LauraX.recent_history.append("_angry")
        $ LauraX.daily_history.append("_angry")
    elif Taboo:
        $ LauraX.change_face("_angry", 1)
        $ LauraX.recent_history.append("no_taboo")
        $ LauraX.daily_history.append("no_taboo")
        ch_l "I try to stay off the radar."
    elif LauraX.action_counter["finger_ass"]:
        $ LauraX.change_face("_sad")
        ch_l "I don't feel like it."
    else:
        $ LauraX.change_face("_surprised")
        ch_l "Not today, [LauraX.player_petname]."
        $ LauraX.change_face()
    $ LauraX.recent_history.append("no_insert ass")
    $ LauraX.daily_history.append("no_insert ass")
    $ approval_bonus = 0
    return


label Laura_IA_Prep:
    if offhand_action == "finger_ass":
        return

    call Laura_Pussy_Launch ("finger_ass")

    if action_context == LauraX:

        $ action_context = 0
        if (LauraX.legs and not LauraX.upskirt) or (LauraX.underwear and not LauraX.underwear_pulled_down):

            if approval_check(LauraX, 1250, TabM = 1) or (LauraX.SeenPussy and approval_check(LauraX, 500) and not Taboo):
                $ LauraX.upskirt = 1
                $ LauraX.underwear_pulled_down = 1
                $ Line = 0
                if LauraX.PantsNum() == 5:
                    $ Line = LauraX.name + " hikes up her_skirt"
                elif LauraX.PantsNum() >= 6:
                    $ Line = LauraX.name + " pulls down her " + LauraX.legs
                else:
                    $ Line = 0
                if LauraX.underwear:
                    if Line:

                        "[Line] and pulls her [LauraX.underwear] out of the way."
                        "She then grabs your arm and rubs your hand against her asshole, clearly intending you to get to work."
                    else:

                        "She pulls her [LauraX.underwear] out of the way, and then rubs your hand against her asshole."
                        "She clearly intends for you to get to work."
                else:

                    "[Line], and then rubs your hand against her asshole."
                    "She clearly intends for you to get to work."
                call Laura_First_Bottomless (1)
            else:
                "[LauraX.name] grabs your arm and rubs your hand against her asshole, clearly intending you to get to work."
        else:
            "[LauraX.name] grabs your arm and rubs your hand against her asshole, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ LauraX.change_stat("inhibition", 80, 3)
                $ LauraX.change_stat("inhibition", 50, 2)
                "You press your finger into it."
            "Praise her.":
                $ LauraX.change_face("_sexy", 1)
                $ LauraX.change_stat("inhibition", 80, 3)
                ch_p "Dirty girl, [LauraX.petname]."
                $ LauraX.nameCheck()
                "You press your finger into it."
                $ LauraX.change_stat("love", 85, 1)
                $ LauraX.change_stat("obedience", 90, 1)
                $ LauraX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your hand back."
                $ LauraX.change_face("_surprised")
                $ LauraX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [LauraX.petname]."
                $ LauraX.nameCheck()
                "[LauraX.name] pulls back."
                $ LauraX.change_stat("obedience", 90, 1)
                $ LauraX.change_stat("obedience", 50, 1)
                $ LauraX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ LauraX.add_word(1,"refused","refused")
                return


    if not LauraX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (LauraX)
        if "_angry" in LauraX.recent_history:
            return

    $ approval_bonus = 0
    if not LauraX.action_counter["finger_ass"]:
        if LauraX.Forced:
            $ LauraX.change_stat("love", 90, -50)
            $ LauraX.change_stat("obedience", 70, 60)
            $ LauraX.change_stat("inhibition", 80, 35)
        else:
            $ LauraX.change_stat("love", 90, 10)
            $ LauraX.change_stat("obedience", 70, 20)
            $ LauraX.change_stat("inhibition", 80, 25)

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
    $ LauraX.drain_word("no_insert ass")
    $ LauraX.recent_history.append("finger_ass")
    $ LauraX.daily_history.append("finger_ass")
    call Laura_Pussy_Launch ("finger_ass")

label Laura_IA_Cycle:
    while Round > 0:
        call ViewShift (LauraX, LauraX.pose, 0, "finger_ass")
        call shift_focus (LauraX)
        $ LauraX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (LauraX)
                    $ counter += 1
                    $ Round -= 1
                    jump Laura_IA_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (LauraX, "menu")
                    jump Laura_IA_Cycle
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
                                    "Pull out and start rubbing again.":
                                        $ action_context = "pullback"
                                        call Laura_IA_After
                                        call Laura_Fondle_Ass
                                    "I want to lick your asshole.":
                                        $ action_context = "shift"
                                        call Laura_IA_After
                                        call Laura_Lick_Ass
                                    "Just start licking.":
                                        $ action_context = "auto"
                                        call Laura_IA_After
                                        call Laura_Lick_Ass
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Laura_IA_After
                                        call Laura_Dildo_Ass
                                    "Never Mind":
                                        jump Laura_IA_Cycle
                            else:
                                call Sex_Basic_Dialog (LauraX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Laura_IA_After
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
                                    jump Laura_IA_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Laura_IA_Cycle
                                "Never mind":
                                    jump Laura_IA_Cycle

                        "Show her feet" if not ShowFeet and (LauraX.pose == "doggy" or LauraX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (LauraX.pose == "doggy" or LauraX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [LauraX.name]":

                            call Girl_Undress (LauraX)
                        "Clean up [LauraX.name] (locked)" if not LauraX.spunk:
                            pass
                        "Clean up [LauraX.name]" if LauraX.spunk:
                            call Girl_Cleanup (LauraX, "ask")
                        "Never mind":
                            jump Laura_IA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Laura_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Laura_IA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Laura_Pos_Reset
                    $ Line = 0
                    jump Laura_IA_After


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
                if "_angry" in LauraX.recent_history:
                    call Laura_Pos_Reset
                    return
                $ LauraX.change_stat("lust", 200, 5)
                if 100 > LauraX.lust >= 70 and LauraX.session_orgasms < 2:
                    $ LauraX.recent_history.append("unsatisfied")
                    $ LauraX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Laura_IA_After
                $ Line = "came"

            if LauraX.lust >= 100:

                call Girl_Cumming (LauraX)
                if action_context == "shift" or "_angry" in LauraX.recent_history:
                    jump Laura_IA_After

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
                            jump Laura_IA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if LauraX.SEXP >= 100 or approval_check(LauraX, 1200, "LO"):
            pass
        elif counter == (5 + LauraX.action_counter["finger_ass"]):
            $ LauraX.brows = "_confused"
            ch_l "Ungh, you're really getting in there. . ."
        elif LauraX.lust >= 80:
            pass
        elif counter == (15 + LauraX.action_counter["finger_ass"]) and LauraX.SEXP >= 15 and not approval_check(LauraX, 1500):
            $ LauraX.brows = "_confused"
            menu:
                ch_l "Maybe change things up a little?"
                "Finish up.":
                    "You let go. . ."
                    jump Laura_IA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Laura_IA_After
                "No, this is fun.":
                    if approval_check(LauraX, 1200) or approval_check(LauraX, 500, "O"):
                        $ LauraX.change_stat("love", 200, -5)
                        $ LauraX.change_stat("obedience", 50, 3)
                        $ LauraX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ LauraX.change_face("_angry", 1)
                        call Laura_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_l "I'm kinda bored here."
                        $ LauraX.change_stat("love", 50, -3, 1)
                        $ LauraX.change_stat("love", 80, -4, 1)
                        $ LauraX.change_stat("obedience", 30, -1, 1)
                        $ LauraX.change_stat("obedience", 50, -1, 1)
                        $ LauraX.recent_history.append("_angry")
                        $ LauraX.daily_history.append("_angry")
                        jump Laura_IA_After


        call Escalation (LauraX)

        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [LauraX.player_petname]."


    $ LauraX.change_face("_bemused", 0)
    $ Line = 0
    ch_l "Ok, [LauraX.player_petname], breaktime."

label Laura_IA_After:
    if not action_context:
        call Laura_Pos_Reset

    $ LauraX.change_face("_sexy")

    $ LauraX.action_counter["finger_ass"] += 1
    $ LauraX.remaining_actions -=1
    $ LauraX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ LauraX.addiction_rate += 1

    call Partner_Like (LauraX, 2)

    if LauraX.action_counter["finger_ass"] == 1:
        $ LauraX.SEXP += 12
        if not action_context:
            if LauraX.love >= 500 and "unsatisfied" not in LauraX.recent_history:
                ch_l "That was kinda wild. . ."
            elif LauraX.obedience <= 500 and Player.focus <= 20:
                $ LauraX.change_face("_perplexed", 1)
                ch_l "Did you enjoy that?"

    $ approval_bonus = 0


    call checkout
    return








label Laura_Lick_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (LauraX)

    if LauraX.action_counter["eat_ass"]:
        $ approval_bonus += 20
    if LauraX.PantsNum() >= 6 or LauraX.HoseNum() >= 5:
        $ approval_bonus -= 25
    if LauraX.lust > 95:
        $ approval_bonus += 20
    elif LauraX.lust > 85:
        $ approval_bonus += 15
    if LauraX.lust > 85 and action_context == "auto":
        $ approval_bonus += 10
    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in LauraX.traits:
        $ approval_bonus += (4*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in LauraX.traits:
        $ approval_bonus -= 25
    if LauraX.event_counter["forced"] and not LauraX.Forced:
        $ approval_bonus -= 5*LauraX.event_counter["forced"]

    if Taboo and "no_taboo" in LauraX.daily_history:
        $ approval_bonus -= 10
    if Taboo and "public" not in LauraX.history:
        $ approval_bonus -= 20

    if "no_lick ass" in LauraX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_lick ass" in LauraX.recent_history else 0

    $ approval = approval_check(LauraX, 1550, TabM = 4)

    if action_context == "auto":
        if approval:
            $ LauraX.change_face("_surprised")
            $ LauraX.change_stat("obedience", 90, 1)
            $ LauraX.change_stat("inhibition", 80, 3)
            $ LauraX.change_stat("inhibition", 40, 2)
            "As you crouch down and start to lick her asshole, [LauraX.name] startles briefly, but then begins to melt."
            $ LauraX.change_face("_sexy")
            jump Laura_LA_Prep
        else:
            $ LauraX.change_face("_surprised")
            $ LauraX.change_stat("love", 80, -2)
            $ LauraX.change_stat("obedience", 50, -3)
            ch_l "[LauraX.player_petname]! No. . ."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "eat_ass" in LauraX.recent_history:
        $ LauraX.change_face("_sexy", 1)
        ch_l "Mmmm, again? I guess. . ."
        jump Laura_LA_Prep
    elif "eat_ass" in LauraX.daily_history:
        $ LauraX.change_face("_sexy", 1)
        ch_l "You didn't get enough earlier?"


    if approval >= 2:
        if LauraX.Forced:
            $ LauraX.change_face("_sad")
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
            $ LauraX.change_stat("obedience", 90, 2)
            $ LauraX.change_stat("inhibition", 60, 2)
            ch_l "Meh. . ."
        else:
            $ LauraX.change_face("_sexy", 1)
            $ LauraX.eyes = "_closed"
            $ LauraX.change_stat("love", 90, 1)
            $ LauraX.change_stat("inhibition", 60, 2)
            $ LauraX.change_stat("lust", 200, 3)
            ch_l "Mmm. . . naughty."
        $ LauraX.change_stat("obedience", 20, 1)
        $ LauraX.change_stat("obedience", 60, 1)
        $ LauraX.change_stat("inhibition", 80, 2)
        jump Laura_LA_Prep
    else:

        $ LauraX.change_face("_angry", 1)
        if "no_lick ass" in LauraX.recent_history:
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "no_taboo" in LauraX.daily_history and "no_lick ass" in LauraX.daily_history:
            ch_l "I told you not to touch me like that in public!"
        elif "no_lick ass" in LauraX.daily_history:
            ch_l "Don't make me tell you again today."
        elif Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "I told you, not here, [LauraX.player_petname]."
        elif not LauraX.action_counter["eat_ass"]:
            $ LauraX.change_face("_bemused", 1)
            if LauraX.love >= LauraX.obedience and LauraX.love >= LauraX.inhibition:
                ch_l "Oh, we're there now?"
            elif LauraX.obedience >= LauraX.inhibition:
                ch_l "Is that what gets you off?"
            else:
                $ LauraX.eyes = "_sexy"
                ch_l "Hm, I didn't know that's what you were into."
        else:
            $ LauraX.change_face("_bemused")
            ch_l "Not now, [LauraX.player_petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no_lick ass" in LauraX.daily_history:
                $ LauraX.change_face("_bemused")
                ch_l "It's cool, [LauraX.player_petname]."
                return
            "I'm sure I can convince you later. . ." if "no_lick ass" not in LauraX.daily_history:
                $ LauraX.change_face("_sexy")
                ch_l "Anything's possible, [LauraX.player_petname]."
                $ LauraX.change_stat("love", 80, 2)
                $ LauraX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ LauraX.recent_history.append("no_taboo")
                    $ LauraX.daily_history.append("no_taboo")
                $ LauraX.recent_history.append("no_lick ass")
                $ LauraX.daily_history.append("no_lick ass")
                return
            "I think you'd really enjoy it. . .":
                if approval:
                    $ LauraX.change_face("_sexy")
                    $ LauraX.change_stat("obedience", 90, 2)
                    $ LauraX.change_stat("obedience", 50, 2)
                    ch_l "Ok, you're probably right. . ."
                    $ LauraX.change_stat("inhibition", 70, 3)
                    $ LauraX.change_stat("inhibition", 40, 2)
                    jump Laura_LA_Prep
                else:
                    $ LauraX.change_face("_sexy")
                    ch_l "I really don't think so."
            "[[Start licking anyway]":

                $ approval = approval_check(LauraX, 1100, "OI", TabM = 4)
                if approval > 1 or (approval and LauraX.Forced):
                    $ LauraX.change_face("_sad")
                    $ LauraX.change_stat("love", 70, -5, 1)
                    $ LauraX.change_stat("love", 200, -2)
                    ch_l "Suit yourself."
                    $ LauraX.change_stat("obedience", 50, 4)
                    $ LauraX.change_stat("inhibition", 80, 1)
                    $ LauraX.change_stat("inhibition", 60, 3)
                    if approval < 2:
                        $ LauraX.Forced = 1
                    jump Laura_LA_Prep
                else:
                    $ LauraX.change_stat("love", 200, -15)
                    $ LauraX.change_face("_angry", 1)
                    "She shoves your head back."
                    $ LauraX.recent_history.append("_angry")
                    $ LauraX.daily_history.append("_angry")

    if "no_lick ass" in LauraX.daily_history:
        ch_l "I don't like to repeat myself, [LauraX.player_petname]."
        $ LauraX.recent_history.append("_angry")
        $ LauraX.daily_history.append("_angry")
    elif LauraX.Forced:
        $ LauraX.change_face("_angry", 1)
        ch_l "I don't think so."
        if approval_check(LauraX, 500, "I"):
            $ LauraX.change_stat("lust", 80, 10)
        else:
            $ LauraX.change_stat("lust", 50, 3)
        $ LauraX.change_stat("obedience", 50, -2)
        $ LauraX.recent_history.append("_angry")
        $ LauraX.daily_history.append("_angry")
    elif Taboo:
        $ LauraX.change_face("_angry", 1)
        $ LauraX.recent_history.append("no_taboo")
        $ LauraX.daily_history.append("no_taboo")
        ch_l "I try to stay off the radar."
    elif LauraX.action_counter["eat_ass"]:
        $ LauraX.change_face("_sad")
        ch_l "Sorry, no more of that."
    else:
        $ LauraX.change_face("_surprised")
        ch_l "I'm sorry, not now."
        $ LauraX.change_face()
    $ LauraX.recent_history.append("no_lick ass")
    $ LauraX.daily_history.append("no_lick ass")
    $ approval_bonus = 0
    return

label Laura_LA_Prep:
    if offhand_action == "eat_ass":
        return
    if not LauraX.Forced and action_context != "auto":
        $ approval_bonus = 0
        if LauraX.PantsNum() >= 6:
            $ approval_bonus = 15
        call Bottoms_Off (LauraX)
        if "_angry" in LauraX.recent_history:
            return
    $ approval_bonus = 0
    call Laura_Pussy_Launch ("eat_ass")
    if not LauraX.action_counter["eat_ass"]:
        if LauraX.Forced:
            $ LauraX.change_stat("love", 90, -30)
            $ LauraX.change_stat("obedience", 70, 40)
            $ LauraX.change_stat("inhibition", 80, 80)
        else:
            $ LauraX.change_stat("love", 90, 35)
            $ LauraX.change_stat("obedience", 70, 25)
            $ LauraX.change_stat("inhibition", 80, 55)
    if Taboo:
        $ LauraX.inhibition += int(Taboo/10)
        $ LauraX.lust += int(Taboo/5)
    if action_context:
        $ renpy.pop_call()
        $ action_context = 0

    $ LauraX.upskirt = 1
    if LauraX.PantsNum() == 5:
        $ LauraX.SeenPanties = 1
    if not LauraX.underwear:
        call Laura_First_Bottomless (1)
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ LauraX.drain_word("no_taboo")
    $ LauraX.drain_word("no_lick ass")

    $ LauraX.recent_history.append("lick") if "lick" not in LauraX.recent_history else LauraX.recent_history
    $ LauraX.recent_history.append("ass") if "ass" not in LauraX.recent_history else LauraX.recent_history
    $ LauraX.recent_history.append("eat_ass")

    $ LauraX.daily_history.append("lick") if "lick" not in LauraX.daily_history else LauraX.recent_history
    $ LauraX.daily_history.append("ass") if "ass" not in LauraX.daily_history else LauraX.recent_history
    $ LauraX.daily_history.append("eat_ass")
    call Laura_Pussy_Launch ("eat_ass")
label Laura_LA_Cycle:
    if offhand_action == "kiss":
        $ offhand_action = 0
    while Round > 0:
        call ViewShift (LauraX, LauraX.pose, 0, "eat_ass")
        call shift_focus (LauraX)
        $ LauraX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (LauraX)
                    $ counter += 1
                    $ Round -= 1
                    jump Laura_LA_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (LauraX, "menu")
                    jump Laura_LA_Cycle
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
                                    "Switch to fondling.":
                                        $ action_context = "pullback"
                                        call Laura_LA_After
                                        call Laura_Fondle_Ass
                                    "I want to stick a finger in.":
                                        $ action_context = "shift"
                                        call Laura_LA_After
                                        call Laura_Insert_Ass
                                    "Just stick a finger in [[without asking].":
                                        $ action_context = "auto"
                                        call Laura_LA_After
                                        call Laura_Insert_Ass
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Laura_LA_After
                                        call Laura_Dildo_Ass
                                    "Never Mind":
                                        jump Laura_LA_Cycle
                            else:
                                call Sex_Basic_Dialog (LauraX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Laura_LA_After
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
                                    jump Laura_LA_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Laura_LA_Cycle
                                "Never mind":
                                    jump Laura_LA_Cycle

                        "Show her feet" if not ShowFeet and (LauraX.pose == "doggy" or LauraX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (LauraX.pose == "doggy" or LauraX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [LauraX.name]":

                            call Girl_Undress (LauraX)
                        "Clean up [LauraX.name] (locked)" if not LauraX.spunk:
                            pass
                        "Clean up [LauraX.name]" if LauraX.spunk:
                            call Girl_Cleanup (LauraX, "ask")
                        "Never mind":
                            jump Laura_LA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Laura_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Laura_LA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Laura_Pos_Reset
                    $ Line = 0
                    jump Laura_LA_After


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
                if "_angry" in LauraX.recent_history:
                    call Laura_Pos_Reset
                    return
                $ LauraX.change_stat("lust", 200, 5)
                if 100 > LauraX.lust >= 70 and LauraX.session_orgasms < 2:
                    $ LauraX.recent_history.append("unsatisfied")
                    $ LauraX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Laura_LA_After
                $ Line = "came"

            if LauraX.lust >= 100:

                call Girl_Cumming (LauraX)
                if action_context == "shift" or "_angry" in LauraX.recent_history:
                    jump Laura_LA_After

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
                            jump Laura_LA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if LauraX.SEXP >= 100 or approval_check(LauraX, 1200, "LO"):
            pass
        elif counter == (5 + LauraX.action_counter["eat_ass"]):
            $ LauraX.brows = "_confused"
            ch_l "You seem to be enjoying yourself. . ."
        elif LauraX.lust >= 80:
            pass
        elif counter == (15 + LauraX.action_counter["eat_ass"]) and LauraX.SEXP >= 15 and not approval_check(LauraX, 1500):
            $ LauraX.brows = "_confused"
            menu:
                ch_l "[LauraX.player_petname], could we try something different?"
                "Finish up.":
                    "You let go. . ."
                    jump Laura_LA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Laura_LA_After
                "No, this is fun.":
                    if approval_check(LauraX, 1200) or approval_check(LauraX, 500, "O"):
                        $ LauraX.change_stat("love", 200, -5)
                        $ LauraX.change_stat("obedience", 50, 3)
                        $ LauraX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ LauraX.change_face("_angry", 1)
                        call Laura_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_l "I'm kinda bored here."
                        $ LauraX.change_stat("love", 50, -3, 1)
                        $ LauraX.change_stat("love", 80, -4, 1)
                        $ LauraX.change_stat("obedience", 30, -1, 1)
                        $ LauraX.change_stat("obedience", 50, -1, 1)
                        $ LauraX.recent_history.append("_angry")
                        $ LauraX.daily_history.append("_angry")
                        jump Laura_LA_After


        call Escalation (LauraX)

        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [LauraX.player_petname]."


    $ LauraX.change_face("_bemused", 0)
    $ Line = 0
    ch_l "Ok, [LauraX.player_petname], breaktime."

label Laura_LA_After:
    if not action_context:
        call Laura_Pos_Reset

    $ LauraX.change_face("_sexy")

    $ LauraX.action_counter["eat_ass"] += 1
    $ LauraX.remaining_actions -=1
    if LauraX.PantsNum() < 6 or LauraX.upskirt:
        $ LauraX.addiction_rate += 1
        if "addictive" in Player.traits:
            $ LauraX.addiction_rate += 1

    call Partner_Like (LauraX, 2)

    if LauraX.action_counter["eat_ass"] == 1:
        $ LauraX.SEXP += 15
        if not action_context:
            if LauraX.love >= 500 and "unsatisfied" not in LauraX.recent_history:
                ch_l "That was. . . interesting."
            elif LauraX.obedience <= 500 and Player.focus <= 20:
                $ LauraX.change_face("_perplexed", 1)
                ch_l "Was that good for you?"

    $ approval_bonus = 0


    call checkout
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
