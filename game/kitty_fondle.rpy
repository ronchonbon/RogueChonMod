
label Kitty_Fondle:

    $ KittyX.mouth = "_smile"
    if not KittyX.remaining_actions:
        ch_k "I'm kinda tired right now, [KittyX.player_petname], later?"
        return
    menu:
        ch_k "Um, what did you want to touch, [KittyX.player_petname]?"
        "Your breasts?" if KittyX.remaining_actions:
            jump Kitty_Fondle_Breasts
        "Your thighs?" if KittyX.remaining_actions:
            jump Kitty_Fondle_Thighs
        "Your pussy?" if KittyX.remaining_actions:
            jump Kitty_Fondle_Pussy
        "Your Ass?" if KittyX.remaining_actions:
            jump Kitty_Fondle_Ass
        "Never mind.":
            return
    return



label Kitty_Fondle_Breasts:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (KittyX)


    if KittyX.action_counter["fondle_breasts"]:
        $ approval_bonus += 15
    if KittyX.lust > 75:
        $ approval_bonus += 20
    if "exhibitionist" in KittyX.traits:
        $ approval_bonus += (3*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in KittyX.traits:
        $ approval_bonus -= 20
    if KittyX.event_counter["forced"] and not KittyX.Forced:
        $ approval_bonus -= 5*KittyX.event_counter["forced"]

    if Taboo and "no_taboo" in KittyX.daily_history:
        $ approval_bonus -= 10

    if "no_fondle breasts" in KittyX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle breasts" in KittyX.recent_history else 0

    $ approval = approval_check(KittyX, 950, TabM = 3)

    if action_context == "auto":
        if approval:
            $ KittyX.change_face("_sexy")
            $ KittyX.change_stat("obedience", 90, 1)
            $ KittyX.change_stat("obedience", 70, 2)
            $ KittyX.change_stat("inhibition", 70, 3)
            $ KittyX.change_stat("inhibition", 30, 2)
            "As you cup her breast, [KittyX.name] gently nods."
            jump Kitty_FB_Prep
        else:
            $ KittyX.change_face("_surprised")
            $ KittyX.brows = "_confused"
            $ KittyX.change_stat("obedience", 50, -2)
            ch_k "Nuh-uh, [KittyX.player_petname], get back to what you were doing."
            $ approval_bonus = 0
            $ offhand_action = 0
            return



    if approval:
        $ KittyX.change_face("_sexy", 1)
        if KittyX.Forced:
            $ KittyX.change_face("_sad")
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
        elif not Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "I guess here is fine. . ."

    if "fondle_breasts" in KittyX.recent_history:
        $ KittyX.change_face("_sexy", 1)
        ch_k "Mmm, again? Ok."
        jump Kitty_FB_Prep
    elif "fondle_breasts" in KittyX.daily_history:
        $ KittyX.change_face("_sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Take it easy though.",
            "Mmm. . ."])
        ch_k "[Line]"

    if approval >= 2:
        $ KittyX.change_face("_bemused", 1)
        if KittyX.Forced:
            $ KittyX.change_face("_sad")
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
            $ KittyX.change_stat("obedience", 90, 1)
            $ KittyX.change_stat("inhibition", 60, 1)
        ch_k "Ok [KittyX.player_petname], come and get'em."
        $ KittyX.change_stat("love", 90, 1)
        $ KittyX.change_stat("inhibition", 50, 3)
        jump Kitty_FB_Prep
    else:

        $ KittyX.change_face("_angry", 1)
        if "no_fondle breasts" in KittyX.recent_history:
            ch_k "[KittyX.Like]no way, [KittyX.player_petname]."
        elif Taboo and "no_taboo" in KittyX.daily_history and "no_fondle breasts" in KittyX.daily_history:
            ch_k "I told you not here!"
        elif "no_fondle breasts" in KittyX.daily_history:
            ch_k "I[KittyX.like]already told you \"no.\""
        elif Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "Not here!"
        elif not KittyX.action_counter["fondle_breasts"]:
            $ KittyX.change_face("_bemused")
            ch_k "I'm[KittyX.like]not ready for that, [KittyX.player_petname]. . ."
        else:
            $ KittyX.change_face("_bemused")
            ch_k "Um, no."
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle breasts" in KittyX.daily_history:
                $ KittyX.change_face("_bemused")
                ch_k "It's cool, [KittyX.player_petname]."
                return
            "Maybe later?" if "no_fondle breasts" not in KittyX.daily_history:
                $ KittyX.change_face("_sexy")
                "She re-adjusts her cleavage."
                ch_k "Um, yeah, maybe later."
                $ KittyX.change_stat("love", 80, 1)
                $ KittyX.change_stat("love", 50, 1)
                $ KittyX.change_stat("inhibition", 30, 2)
                if Taboo:
                    $ KittyX.recent_history.append("no_taboo")
                    $ KittyX.daily_history.append("no_taboo")
                $ KittyX.recent_history.append("no_fondle breasts")
                $ KittyX.daily_history.append("no_fondle breasts")
                return
            "Come on, Please?":
                if approval:
                    $ KittyX.change_face("_sexy")
                    $ KittyX.change_stat("obedience", 90, 1)
                    $ KittyX.change_stat("obedience", 50, 2)
                    $ KittyX.change_stat("inhibition", 60, 3)
                    $ KittyX.change_stat("inhibition", 30, 2)
                    ch_k "Well[KittyX.like]if you ask nicely. . ."
                    jump Kitty_FB_Prep
                else:
                    $ KittyX.change_face("_sexy")
                    ch_k "Um, still no."
            "[[Grab her chest anyway]":


                $ approval = approval_check(KittyX, 350, "OI", TabM = 3)
                if approval > 1 or (approval and KittyX.Forced):
                    $ KittyX.change_face("_sad")
                    $ KittyX.change_stat("love", 70, -5, 1)
                    $ KittyX.change_stat("love", 20, -2, 1)
                    ch_k "Rude! But. . . whatever."
                    $ KittyX.change_stat("obedience", 90, 2)
                    $ KittyX.change_stat("obedience", 50, 4)
                    $ KittyX.change_stat("inhibition", 60, 3)
                    if approval < 2:
                        $ KittyX.Forced = 1
                    jump Kitty_FB_Prep
                else:
                    $ KittyX.change_stat("love", 200, -10)
                    $ KittyX.change_face("_angry", 1)
                    "She slaps your hand away."
                    $ KittyX.recent_history.append("_angry")
                    $ KittyX.daily_history.append("_angry")

    if "no_fondle breasts" in KittyX.daily_history:
        ch_k "{i}Listen{/i}!"
        $ KittyX.recent_history.append("_angry")
        $ KittyX.daily_history.append("_angry")
    elif KittyX.Forced:
        $ KittyX.change_face("_angry", 1)
        ch_k "Not even."
        $ KittyX.change_stat("lust", 60, 5)
        $ KittyX.change_stat("obedience", 50, -2)
        $ KittyX.recent_history.append("_angry")
        $ KittyX.daily_history.append("_angry")
    elif Taboo:
        $ KittyX.change_face("_angry", 1)
        $ KittyX.recent_history.append("no_taboo")
        $ KittyX.daily_history.append("no_taboo")
        ch_k "I don't like being so. . . exposed."
    elif KittyX.action_counter["fondle_breasts"]:
        $ KittyX.change_face("_sad")
        ch_k "You had your shot."
    else:
        $ KittyX.change_face("_sexy")
        $ KittyX.mouth = "_sad"
        ch_k "No way."
    $ KittyX.recent_history.append("no_fondle breasts")
    $ KittyX.daily_history.append("no_fondle breasts")
    $ approval_bonus = 0
    return


label Kitty_FB_Prep:
    if primary_action == "kiss":
        $ primary_action = "fondle_breasts"
        return

    if offhand_action == "fondle_breasts":
        return

    call Kitty_Breasts_Launch ("fondle_breasts")

    if action_context == KittyX:

        $ action_context = 0
        if (KittyX.top or KittyX.bra) and not KittyX.top_pulled_up:

            if approval_check(KittyX, 1250, TabM = 1) or (KittyX.SeenChest and approval_check(KittyX, 500) and not Taboo):
                $ KittyX.top_pulled_up = 1
                $ Line = KittyX.top if KittyX.top else KittyX.bra
                "With a cheshire grin, [KittyX.name] pulls her [Line] up over her breasts."
                call Kitty_First_Topless (1)
                $ Line = 0
                "She then grabs your arm and mashes your hand against her breast, clearly intending you to get to work."
            else:
                "[KittyX.name] grabs your arm and mashes your hand against her covered breast, clearly intending you to get to work."
        else:
            "[KittyX.name] grabs your arm and mashes your hand against her breast, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ KittyX.change_stat("inhibition", 80, 3)
                $ KittyX.change_stat("inhibition", 50, 2)
                "You start to fondle it."
            "Praise her.":
                $ KittyX.change_face("_sexy", 1)
                $ KittyX.change_stat("inhibition", 80, 3)
                ch_p "I like the initiative, [KittyX.petname]."
                $ KittyX.nameCheck()
                "You start to fondle it."
                $ KittyX.change_stat("love", 85, 1)
                $ KittyX.change_stat("obedience", 90, 1)
                $ KittyX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your hand back."
                $ KittyX.change_face("_surprised")
                $ KittyX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [KittyX.petname]."
                $ KittyX.nameCheck()
                "[KittyX.name] pulls back."
                $ KittyX.change_stat("obedience", 90, 1)
                $ KittyX.change_stat("obedience", 50, 1)
                $ KittyX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ KittyX.add_word(1,"refused","refused")
                return


    if not KittyX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Top_Off (KittyX)
        if "_angry" in KittyX.recent_history:
            return

    $ approval_bonus = 0
    if not KittyX.action_counter["fondle_breasts"]:
        if KittyX.Forced:
            $ KittyX.change_stat("love", 90, -20)
            $ KittyX.change_stat("obedience", 70, 25)
            $ KittyX.change_stat("inhibition", 80, 15)
        else:
            $ KittyX.change_stat("love", 90, 10)
            $ KittyX.change_stat("obedience", 70, 5)
            $ KittyX.change_stat("inhibition", 80, 15)

    if Taboo:
        $ KittyX.inhibition += int(Taboo/10)
        $ KittyX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ KittyX.drain_word("no_taboo")
    $ KittyX.drain_word("no_fondle breasts")
    $ KittyX.recent_history.append("fondle_breasts")
    $ KittyX.daily_history.append("fondle_breasts")
    call Kitty_Breasts_Launch ("fondle_breasts")

label Kitty_FB_Cycle:
    while Round > 0:
        call ViewShift (KittyX, KittyX.pose, 0, "fondle_breasts")
        call shift_focus (KittyX)
        $ KittyX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (KittyX)
                    $ counter += 1
                    $ Round -= 1
                    jump Kitty_FB_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (KittyX, "menu")
                    jump Kitty_FB_Cycle
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
                                    "Ask to suck on them.":
                                        if KittyX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Kitty_FB_After
                                            call Kitty_Suck_Breasts
                                        else:
                                            call Sex_Basic_Dialog (KittyX, "tired")
                                    "Just suck on them without asking.":
                                        if KittyX.remaining_actions and multi_action:
                                            $ action_context = "auto"
                                            call Kitty_FB_After
                                            call Kitty_Suck_Breasts
                                        else:
                                            "As you lean in to suck on her breast, she grabs your head and pushes back."
                                            call Sex_Basic_Dialog (KittyX, "tired")
                                    "Never Mind":
                                        jump Kitty_FB_Cycle
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
                                    jump Kitty_FB_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Kitty_FB_Cycle
                                "Never mind":
                                    jump Kitty_FB_Cycle

                        "Show her feet" if not ShowFeet and (KittyX.pose == "doggy" or KittyX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (KittyX.pose == "doggy" or KittyX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [KittyX.name]":

                            call Girl_Undress (KittyX)
                        "Clean up [KittyX.name] (locked)" if not KittyX.spunk:
                            pass
                        "Clean up [KittyX.name]" if KittyX.spunk:
                            call Girl_Cleanup (KittyX, "ask")
                        "Never mind":
                            jump Kitty_FB_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Kitty_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Kitty_FB_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Kitty_Pos_Reset
                    $ Line = 0
                    jump Kitty_FB_After


        call shift_focus (KittyX)
        call Sex_Dialog (KittyX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or KittyX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (KittyX)
                if "_angry" in KittyX.recent_history:
                    call Kitty_Pos_Reset
                    return
                $ KittyX.change_stat("lust", 200, 5)
                if 100 > KittyX.lust >= 70 and KittyX.session_orgasms < 2 and KittyX.SEXP >= 20:
                    $ KittyX.recent_history.append("unsatisfied")
                    $ KittyX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Kitty_FB_After
                $ Line = "came"

            if KittyX.lust >= 100:

                call Girl_Cumming (KittyX)
                if action_context == "shift" or "_angry" in KittyX.recent_history:
                    jump Kitty_FB_After

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
                            jump Kitty_FB_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if KittyX.SEXP >= 100 or approval_check(KittyX, 1200, "LO"):
            pass
        elif counter == (5 + KittyX.action_counter["fondle_breasts"]):
            $ KittyX.brows = "_confused"
            ch_k "You're just going at them, huh?"
        elif KittyX.lust >= 85:
            pass
        elif counter == (15 + KittyX.action_counter["fondle_breasts"]) and KittyX.SEXP >= 15 and not approval_check(KittyX, 1500):
            $ KittyX.brows = "_confused"
            menu:
                ch_k "Maybe we could try something else here [KittyX.player_petname]?"
                "Finish up.":
                    "You let go. . ."
                    jump Kitty_FB_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Kitty_FB_After
                "No, this is fun.":
                    if approval_check(KittyX, 1200) or approval_check(KittyX, 500, "O"):
                        $ KittyX.change_stat("love", 200, -5)
                        $ KittyX.change_stat("obedience", 50, 3)
                        $ KittyX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ KittyX.change_face("_angry", 1)
                        call Kitty_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_k "Fun for you maybe, I'm tired of it."
                        $ KittyX.change_stat("love", 50, -3, 1)
                        $ KittyX.change_stat("love", 80, -4, 1)
                        $ KittyX.change_stat("obedience", 30, -1, 1)
                        $ KittyX.change_stat("obedience", 50, -1, 1)
                        $ KittyX.recent_history.append("_angry")
                        $ KittyX.daily_history.append("_angry")
                        jump Kitty_FB_After


        call Escalation (KittyX)

        if Round == 10:
            ch_k "It's[KittyX.like]getting kinda late."
        elif Round == 5:
            ch_k "We should wrap this up."

        if KittyX.lust >= 50 and not KittyX.top_pulled_up and (KittyX.bra or KittyX.top):
            $ KittyX.top_pulled_up = 1
            "[KittyX.name] laughs and pulls her top open."
            call Kitty_First_Topless


    $ KittyX.change_face("_bemused", 0)
    $ Line = 0
    ch_k "Time to take a little break, for now."

label Kitty_FB_After:
    if not action_context:
        call Kitty_Pos_Reset

    $ KittyX.change_face("_sexy")

    $ KittyX.action_counter["fondle_breasts"]+= 1
    $ KittyX.remaining_actions -=1
    $ KittyX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ KittyX.addiction_rate += 1

    call Partner_Like (KittyX, 2)

    if KittyX.action_counter["fondle_breasts"]== 1:
        $ KittyX.SEXP += 4
        if not action_context:
            if KittyX.love >= 500 and "unsatisfied" not in KittyX.recent_history:
                ch_k "I hope there was[KittyX.like]enough to work with."
            elif KittyX.obedience <= 500 and Player.focus <= 20:
                $ KittyX.change_face("_perplexed", 1)
                ch_k "Not a disappointment, right?"

    $ approval_bonus = 0


    call checkout
    return






label Kitty_Suck_Breasts:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (KittyX)

    if KittyX.action_counter["suck_breasts"]:
        $ approval_bonus += 15
    if not KittyX.bra and not KittyX.top:
        $ approval_bonus += 15
    if KittyX.lust > 75:
        $ approval_bonus += 20
    if KittyX.lust > 75 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in KittyX.traits:
        $ approval_bonus += (4*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in KittyX.traits:
        $ approval_bonus -= 25
    if KittyX.event_counter["forced"] and not KittyX.Forced:
        $ approval_bonus -= 5*KittyX.event_counter["forced"]

    if Taboo and "no_taboo" in KittyX.daily_history:
        $ approval_bonus -= 10

    if "no_suck breasts" in KittyX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_suck breasts" in KittyX.recent_history else 0

    $ approval = approval_check(KittyX, 1050, TabM = 4)

    if action_context == "auto":
        if approval:
            $ KittyX.change_face("_sexy")
            $ KittyX.change_stat("obedience", 90, 1)
            $ KittyX.change_stat("obedience", 70, 2)
            $ KittyX.change_stat("inhibition", 70, 3)
            $ KittyX.change_stat("inhibition", 30, 2)
            "As you dive in, [KittyX.name] seems a bit surprised, but just makes a little \"purr.\""
            jump Kitty_SB_Prep
        else:
            $ KittyX.change_face("_surprised")
            $ KittyX.change_stat("obedience", 50, -2)
            ch_k "Nuh-uh, [KittyX.player_petname], get back to what you were doing."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "suck_breasts" in KittyX.recent_history:
        $ KittyX.change_face("_sexy", 1)
        ch_k "Mmm, again? Ok."
        jump Kitty_SB_Prep
    elif "suck_breasts" in KittyX.daily_history:
        $ KittyX.change_face("_sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Take it easy though.",
            "Mmm. . ."])
        ch_k "[Line]"

    if approval >= 2:
        $ KittyX.change_face("_bemused", 1)
        if KittyX.Forced:
            $ KittyX.change_face("_sad")
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
            $ KittyX.change_stat("obedience", 90, 1)
            $ KittyX.change_stat("inhibition", 60, 1)
        ch_k "Ok, fiiiine."
        $ KittyX.change_stat("love", 90, 1)
        $ KittyX.change_stat("inhibition", 50, 3)
        jump Kitty_SB_Prep
    else:

        $ KittyX.change_face("_angry", 1)
        if "no_suck breasts" in KittyX.recent_history:
            ch_k "I[KittyX.like]{i}just{/i} told you \"no!\""
        elif Taboo and "no_taboo" in KittyX.daily_history and "no_suck breasts" in KittyX.daily_history:
            ch_k "I told you this was[KittyX.like]too public!"
        elif "no_suck breasts" in KittyX.daily_history:
            ch_k "[KittyX.Like]take a lesson, [KittyX.player_petname]."
        elif Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "Not here!"
        elif not KittyX.action_counter["suck_breasts"]:
            $ KittyX.change_face("_bemused")
            ch_k "Not. . . yet. . . maybe later."
        else:
            $ KittyX.change_face("_bemused")
            ch_k "Um, no."
        menu:
            extend ""
            "Sorry, never mind." if "no_suck breasts" in KittyX.daily_history:
                $ KittyX.change_face("_bemused")
                ch_k "No problem."
                return
            "Maybe later?" if "no_suck breasts" not in KittyX.daily_history:
                $ KittyX.change_face("_sexy")
                ch_k "I'll give it some thought, [KittyX.player_petname]."
                $ KittyX.change_stat("love", 80, 1)
                $ KittyX.change_stat("love", 50, 1)
                $ KittyX.change_stat("inhibition", 30, 2)
                if Taboo:
                    $ KittyX.recent_history.append("no_taboo")
                    $ KittyX.daily_history.append("no_taboo")
                $ KittyX.recent_history.append("no_suck breasts")
                $ KittyX.daily_history.append("no_suck breasts")
                return
            "Come on, Please?":
                if approval:
                    $ KittyX.change_face("_sexy")
                    $ KittyX.change_stat("obedience", 90, 1)
                    $ KittyX.change_stat("obedience", 50, 2)
                    $ KittyX.change_stat("inhibition", 60, 3)
                    $ KittyX.change_stat("inhibition", 30, 2)
                    ch_k "Only if you make it worth it."
                    jump Kitty_SB_Prep
                else:
                    $ KittyX.change_face("_sexy")
                    ch_k "Um, still no."
            "[[Start sucking anyway]":

                $ approval = approval_check(KittyX, 450, "OI", TabM = 3)
                if approval > 1 or (approval and KittyX.Forced):
                    $ KittyX.change_face("_sad")
                    $ KittyX.change_stat("love", 70, -5, 1)
                    $ KittyX.change_stat("love", 20, -2, 1)
                    ch_k "Ugh, I guess if you're so enthusiastic. . ."
                    $ KittyX.change_stat("obedience", 90, 2)
                    $ KittyX.change_stat("obedience", 50, 4)
                    $ KittyX.change_stat("inhibition", 60, 3)
                    if approval < 2:
                        $ KittyX.Forced = 1
                    jump Kitty_SB_Prep
                else:
                    $ KittyX.change_stat("love", 200, -10)
                    $ KittyX.change_face("_angry", 1)
                    "She shoves your head back out."
                    $ KittyX.recent_history.append("_angry")
                    $ KittyX.daily_history.append("_angry")

    if "no_suck breasts" in KittyX.daily_history:
        ch_k "How many times do I have to say \"no?\""
        $ KittyX.recent_history.append("_angry")
        $ KittyX.daily_history.append("_angry")
    elif KittyX.Forced:
        $ KittyX.change_face("_angry", 1)
        ch_k "[KittyX.Like]get your mouth away from me."
        $ KittyX.change_stat("lust", 60, 5)
        $ KittyX.change_stat("obedience", 50, -2)
        $ KittyX.recent_history.append("_angry")
        $ KittyX.daily_history.append("_angry")
    elif Taboo:
        $ KittyX.change_face("_angry", 1)
        $ KittyX.recent_history.append("no_taboo")
        $ KittyX.daily_history.append("no_taboo")
        ch_k "Time and place, [KittyX.player_petname]!"
    elif KittyX.action_counter["suck_breasts"]:
        $ KittyX.change_face("_sad")
        ch_k "Sorry, [KittyX.player_petname], maybe later?"
    else:
        $ KittyX.change_face("_sexy")
        $ KittyX.mouth = "_sad"
        ch_k "Nooope."
    $ KittyX.recent_history.append("no_suck breasts")
    $ KittyX.daily_history.append("no_suck breasts")
    $ approval_bonus = 0
    return


label Kitty_SB_Prep:
    if offhand_action == "suck_breasts":
        return

    call Kitty_Breasts_Launch ("suck_breasts")

    if action_context == KittyX:

        $ action_context = 0
        if (KittyX.top or KittyX.bra) and not KittyX.top_pulled_up:

            if approval_check(KittyX, 1250, TabM = 1) or (KittyX.SeenChest and approval_check(KittyX, 500) and not Taboo):
                $ KittyX.top_pulled_up = 1
                $ Line = KittyX.top if KittyX.top else KittyX.bra
                "With a cheshire grin, [KittyX.name] pulls her [Line] up over her breasts."
                call Kitty_First_Topless (1)
                $ Line = 0
                "She then grabs your head and crams your face into her chest, clearly intending you to get to work."
            else:
                "[KittyX.name] grabs your head and crams your face into her chest, clearly intending you to get to work."
        else:
            "[KittyX.name] grabs your head and crams your face into her chest, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ KittyX.change_stat("inhibition", 80, 3)
                $ KittyX.change_stat("inhibition", 50, 2)
                "You start to run your tongue along her nipple."
            "Praise her.":
                $ KittyX.change_face("_sexy", 1)
                $ KittyX.change_stat("inhibition", 80, 3)
                ch_p "Mmm, I like this, [KittyX.petname]."
                $ KittyX.nameCheck()
                "You start to fondle it."
                $ KittyX.change_stat("love", 85, 1)
                $ KittyX.change_stat("obedience", 90, 1)
                $ KittyX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your head back."
                $ KittyX.change_face("_surprised")
                $ KittyX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [KittyX.petname]."
                $ KittyX.nameCheck()
                "[KittyX.name] pulls away."
                $ KittyX.change_stat("obedience", 90, 1)
                $ KittyX.change_stat("obedience", 50, 1)
                $ KittyX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ KittyX.add_word(1,"refused","refused")
                return

    if not KittyX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Top_Off (KittyX)
        if "_angry" in KittyX.recent_history:
            return

    $ approval_bonus = 0
    if not KittyX.action_counter["suck_breasts"]:
        if KittyX.Forced:
            $ KittyX.change_stat("love", 90, -25)
            $ KittyX.change_stat("obedience", 70, 25)
            $ KittyX.change_stat("inhibition", 80, 17)
        else:
            $ KittyX.change_stat("love", 90, 10)
            $ KittyX.change_stat("obedience", 70, 10)
            $ KittyX.change_stat("inhibition", 80, 15)

    if Taboo:
        $ KittyX.inhibition += int(Taboo/10)
        $ KittyX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ KittyX.drain_word("no_taboo")
    $ KittyX.drain_word("no_suck breasts")
    $ KittyX.recent_history.append("suck_breasts")
    $ KittyX.daily_history.append("suck_breasts")
    call Kitty_Breasts_Launch ("suck_breasts")

label Kitty_SB_Cycle:
    if offhand_action == "kiss":
        $ offhand_action = 0
    while Round > 0:
        call ViewShift (KittyX, KittyX.pose, 0, "suck_breasts")
        call shift_focus (KittyX)
        $ KittyX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (KittyX)
                    $ counter += 1
                    $ Round -= 1
                    jump Kitty_SB_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (KittyX, "menu")
                    jump Kitty_SB_Cycle
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
                                    "Pull back to fondling.":
                                        if KittyX.remaining_actions and multi_action:
                                            $ action_context = "pullback"
                                            call Kitty_SB_After
                                            call Kitty_Fondle_Breasts
                                        else:
                                            "As you pull back, [KittyX.name] pushes you back in close."
                                            call Sex_Basic_Dialog (KittyX, "tired")
                                    "Never Mind":
                                        jump Kitty_SB_Cycle
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
                                    jump Kitty_SB_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Kitty_SB_Cycle
                                "Never mind":
                                    jump Kitty_SB_Cycle

                        "Show her feet" if not ShowFeet and (KittyX.pose == "doggy" or KittyX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (KittyX.pose == "doggy" or KittyX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [KittyX.name]":

                            call Girl_Undress (KittyX)
                        "Clean up [KittyX.name] (locked)" if not KittyX.spunk:
                            pass
                        "Clean up [KittyX.name]" if KittyX.spunk:
                            call Girl_Cleanup (KittyX, "ask")
                        "Never mind":
                            jump Kitty_SB_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Kitty_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Kitty_SB_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Kitty_Pos_Reset
                    $ Line = 0
                    jump Kitty_SB_After


        call shift_focus (KittyX)
        call Sex_Dialog (KittyX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or KittyX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (KittyX)
                if "_angry" in KittyX.recent_history:
                    call Kitty_Pos_Reset
                    return
                $ KittyX.change_stat("lust", 200, 5)
                if 100 > KittyX.lust >= 70 and KittyX.session_orgasms < 2:
                    $ KittyX.recent_history.append("unsatisfied")
                    $ KittyX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Kitty_SB_After
                $ Line = "came"

            if KittyX.lust >= 100:

                call Girl_Cumming (KittyX)
                if action_context == "shift" or "_angry" in KittyX.recent_history:
                    jump Kitty_SB_After

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
                            jump Kitty_SB_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if KittyX.SEXP >= 100 or approval_check(KittyX, 1200, "LO"):
            pass
        elif counter == (5 + KittyX.action_counter["suck_breasts"]):
            $ KittyX.brows = "_confused"
            ch_k "Are they keeping you satisfied?"
        elif KittyX.lust >= 85:
            pass
        elif counter == (15 + KittyX.action_counter["suck_breasts"]) and KittyX.SEXP >= 15 and not approval_check(KittyX, 1500):
            $ KittyX.brows = "_confused"
            menu:
                ch_k "You look like you're having fun there, but maybe we could[KittyX.like]try something else?"
                "Finish up.":
                    "You let go. . ."
                    jump Kitty_SB_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Kitty_SB_After
                "No, this is fun.":
                    if approval_check(KittyX, 1200) or approval_check(KittyX, 500, "O"):
                        $ KittyX.change_stat("love", 200, -5)
                        $ KittyX.change_stat("obedience", 50, 3)
                        $ KittyX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ KittyX.change_face("_angry", 1)
                        call Kitty_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_k "Fun for you maybe, I'm tired of it."
                        $ KittyX.change_stat("love", 50, -3, 1)
                        $ KittyX.change_stat("love", 80, -4, 1)
                        $ KittyX.change_stat("obedience", 30, -1, 1)
                        $ KittyX.change_stat("obedience", 50, -1, 1)
                        $ KittyX.recent_history.append("_angry")
                        $ KittyX.daily_history.append("_angry")
                        jump Kitty_SB_After


        call Escalation (KittyX)

        if Round == 10:
            ch_k "It's[KittyX.like]getting kinda late."
        elif Round == 5:
            ch_k "We should wrap this up."

        if KittyX.lust >= 50 and not KittyX.top_pulled_up and (KittyX.bra or KittyX.top):
            $ KittyX.top_pulled_up = 1
            "[KittyX.name] laughs and pulls her top open."
            call Kitty_First_Topless


    $ KittyX.change_face("_bemused", 0)
    $ Line = 0
    ch_k "Time to take a little break, for now."

label Kitty_SB_After:
    if not action_context:
        call Kitty_Pos_Reset

    $ KittyX.change_face("_sexy")

    $ KittyX.action_counter["suck_breasts"] += 1
    $ KittyX.remaining_actions -=1
    $ KittyX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ KittyX.addiction_rate += 1

    call Partner_Like (KittyX, 2)

    if KittyX.action_counter["suck_breasts"] == 1:
        $ KittyX.SEXP += 4
        if not action_context:
            if KittyX.love >= 500 and "unsatisfied" not in KittyX.recent_history:
                ch_k "I hope they were enough for you. . ."
            elif KittyX.obedience <= 500 and Player.focus <= 20:
                $ KittyX.change_face("_perplexed", 1)
                ch_k "Did that satisfy you?"

    $ approval_bonus = 0


    call checkout
    return





label Kitty_Fondle_Thighs:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (KittyX)

    if KittyX.action_counter["fondle_thighs"]:
        $ approval_bonus += 10
    if KittyX.PantsNum() > 6 or KittyX.HoseNum() >= 5:
        $ approval_bonus -= 5
    if KittyX.lust > 75:
        $ approval_bonus += 10
    if "exhibitionist" in KittyX.traits:
        $ approval_bonus += Taboo
    if KittyX in Player.Harem or "sex friend" in KittyX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in KittyX.traits:
        $ approval_bonus -= 25
    if KittyX.event_counter["forced"] and not KittyX.Forced:
        $ approval_bonus -= 5*KittyX.event_counter["forced"]

    if Taboo and "no_taboo" in KittyX.daily_history:
        $ approval_bonus -= 10

    if "no_fondle thighs" in KittyX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle thighs" in KittyX.recent_history else 0

    $ approval = approval_check(KittyX, 750, TabM=1)

    if action_context == "auto":
        if approval:
            $ KittyX.change_face("_sexy")
            $ KittyX.change_stat("obedience", 50, 1)
            $ KittyX.change_stat("inhibition", 30, 2)
            "As you caress her thigh, [KittyX.name] glances at you, and smiles."
            jump Kitty_FT_Prep
        else:
            $ KittyX.change_face("_surprised")
            $ KittyX.change_stat("obedience", 50, -2)
            ch_k "Heh, keep it above the belt, [KittyX.player_petname]."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if action_context == "pullback":
        $ KittyX.change_face("_surprised")
        $ KittyX.brows = "_sad"
        if KittyX.lust > 60:
            $ KittyX.change_stat("love", 70, -3)
        $ KittyX.change_stat("obedience", 90, 1)
        $ KittyX.change_stat("obedience", 70, 2)
        "As you pull back, [KittyX.name] looks a little sad."
        jump Kitty_FT_Prep
    elif "fondle_thighs" in KittyX.recent_history:
        $ KittyX.change_face("_sexy", 1)
        ch_k "Mmm, again? Ok."
        jump Kitty_FT_Prep
    elif "fondle_thighs" in KittyX.daily_history:
        $ KittyX.change_face("_sexy", 1)
        ch_k "Didn't get enough earlier?"

    if approval >= 2:
        $ KittyX.change_face("_bemused", 1)
        if KittyX.Forced:
            $ KittyX.change_face("_sad")
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("obedience", 90, 1)
            $ KittyX.change_stat("inhibition", 60, 1)
        ch_k "Ok [KittyX.player_petname], go ahead."
        $ KittyX.change_stat("love", 90, 1)
        $ KittyX.change_stat("inhibition", 50, 3)
        jump Kitty_FT_Prep
    else:

        $ KittyX.change_face("_angry", 1)
        if "no_fondle thighs" in KittyX.recent_history:
            ch_k "I[KittyX.like]{i}just{/i} told you \"no!\""
        elif Taboo and "no_taboo" in KittyX.daily_history and "no_fondle thighs" in KittyX.daily_history:
            ch_k "I told you not to touch me like that in public!"
        elif "no_fondle thighs" in KittyX.daily_history:
            ch_k "[KittyX.Like]take a lesson, [KittyX.player_petname]."
        elif Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "Not here!"
        elif not KittyX.action_counter["fondle_thighs"]:
            $ KittyX.change_face("_bemused")
            ch_k "Not. . . yet. . . maybe later."
        else:
            $ KittyX.change_face("_bemused")
            ch_k "Um, no."
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle thighs" in KittyX.daily_history:
                $ KittyX.change_face("_bemused")
                ch_k "Yeah, ok, [KittyX.player_petname]."
                return
            "Maybe later?" if "no_fondle thighs" not in KittyX.daily_history:
                $ KittyX.change_face("_sexy")
                ch_k "Heh, maybe, [KittyX.player_petname]."
                $ KittyX.change_stat("love", 80, 1)
                $ KittyX.change_stat("inhibition", 30, 2)
                if Taboo:
                    $ KittyX.recent_history.append("no_taboo")
                    $ KittyX.daily_history.append("no_taboo")
                $ KittyX.recent_history.append("no_fondle thighs")
                $ KittyX.daily_history.append("no_fondle thighs")
                return
            "Come on, Please?":
                if approval:
                    $ KittyX.change_face("_sexy")
                    $ KittyX.change_stat("obedience", 60, 1)
                    $ KittyX.change_stat("obedience", 30, 2)
                    $ KittyX.change_stat("inhibition", 50, 1)
                    $ KittyX.change_stat("inhibition", 30, 2)
                    ch_k "Well[KittyX.like]if you ask nicely. . ."
                    jump Kitty_FT_Prep
                else:
                    $ KittyX.change_face("_sexy")
                    ch_k "Um, still no."
            "[[Start caressing her thigh anyway]":

                $ approval = approval_check(KittyX, 350, "OI", TabM = 2)
                if approval > 1 or (approval and KittyX.Forced):
                    $ KittyX.change_face("_sad")
                    $ KittyX.change_stat("love", 70, -5, 1)
                    $ KittyX.change_stat("love", 20, -2, 1)
                    ch_k "Hmmph."
                    $ KittyX.change_stat("obedience", 50, 3)
                    $ KittyX.change_stat("inhibition", 60, 2)
                    if approval < 2:
                        $ KittyX.Forced = 1
                    jump Kitty_FT_Prep
                else:
                    $ KittyX.change_stat("love", 200, -8)
                    $ KittyX.change_face("_angry", 1)
                    "She slaps your hand away."
                    $ KittyX.recent_history.append("_angry")
                    $ KittyX.daily_history.append("_angry")

    if "no_fondle thighs" in KittyX.daily_history:
        ch_k "How many times do I have to say \"no?\""
        $ KittyX.recent_history.append("_angry")
        $ KittyX.daily_history.append("_angry")
    elif KittyX.Forced:
        $ KittyX.change_face("_angry", 1)
        ch_k "Not even."
        $ KittyX.change_stat("lust", 50, 2)
        $ KittyX.change_stat("obedience", 50, -1)
        $ KittyX.recent_history.append("_angry")
        $ KittyX.daily_history.append("_angry")
    elif Taboo:
        $ KittyX.change_face("_angry", 1)
        $ KittyX.recent_history.append("no_taboo")
        $ KittyX.daily_history.append("no_taboo")
        ch_k "Time and place, [KittyX.player_petname]!"
    elif KittyX.action_counter["fondle_thighs"]:
        $ KittyX.change_face("_sad")
        ch_k "Fresh!"
    else:
        $ KittyX.change_face("_sexy")
        $ KittyX.mouth = "_sad"
        ch_k "Nooope."
    $ KittyX.recent_history.append("no_fondle thighs")
    $ KittyX.daily_history.append("no_fondle thighs")
    $ approval_bonus = 0
    return

label Kitty_FT_Prep:
    if primary_action == "kiss":
        $ primary_action = "fondle_thighs"
        return

    if offhand_action == "fondle_thighs":
        return

    if not KittyX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (KittyX)
        if "_angry" in KittyX.recent_history:
            return

    $ approval_bonus = 0
    call Kitty_Pussy_Launch ("fondle_thighs")
    if not KittyX.action_counter["fondle_thighs"]:
        if KittyX.Forced:
            $ KittyX.change_stat("love", 90, -10)
            $ KittyX.change_stat("obedience", 70, 15)
            $ KittyX.change_stat("inhibition", 80, 10)
        else:
            $ KittyX.change_stat("love", 90, 5)
            $ KittyX.change_stat("obedience", 70, 10)
            $ KittyX.change_stat("inhibition", 80, 15)

    if Taboo:
        $ KittyX.change_stat("lust", 200, (int(Taboo/5)))
        $ KittyX.change_stat("inhibition", 200, (2*(int(Taboo/5))))

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ KittyX.drain_word("no_taboo")
    $ KittyX.drain_word("no_fondle thighs")
    $ KittyX.recent_history.append("fondle_thighs")
    $ KittyX.daily_history.append("fondle_thighs")
    call Kitty_Pussy_Launch ("fondle_thighs")
label Kitty_FT_Cycle:
    while Round > 0:
        call ViewShift (KittyX, KittyX.pose, 0, "fondle_thighs")
        call shift_focus (KittyX)
        $ KittyX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (KittyX)
                    $ counter += 1
                    $ Round -= 1
                    jump Kitty_FT_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (KittyX, "menu")
                    jump Kitty_FT_Cycle
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
                                    "Can I do a little deeper?":
                                        if KittyX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Kitty_FT_After
                                            call Kitty_Fondle_Pussy
                                        else:
                                            call Sex_Basic_Dialog (KittyX, "tired")
                                    "Shift your hands a bit higher without asking":
                                        if KittyX.remaining_actions and multi_action:
                                            $ action_context = "auto"
                                            call Kitty_FT_After
                                            call Kitty_Fondle_Pussy
                                        else:
                                            "As your hands creep upwards, she grabs your wrists."
                                            call Sex_Basic_Dialog (KittyX, "tired")
                                    "Never Mind":
                                        jump Kitty_FT_Cycle
                            else:
                                call Sex_Basic_Dialog (KittyX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Kitty_FT_After
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
                                    jump Kitty_FT_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Kitty_FT_Cycle
                                "Never mind":
                                    jump Kitty_FT_Cycle

                        "Show her feet" if not ShowFeet and (KittyX.pose == "doggy" or KittyX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (KittyX.pose == "doggy" or KittyX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [KittyX.name]":

                            call Girl_Undress (KittyX)
                        "Clean up [KittyX.name] (locked)" if not KittyX.spunk:
                            pass
                        "Clean up [KittyX.name]" if KittyX.spunk:
                            call Girl_Cleanup (KittyX, "ask")
                        "Never mind":
                            jump Kitty_FT_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Kitty_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Kitty_FT_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Kitty_Pos_Reset
                    $ Line = 0
                    jump Kitty_FT_After


        call shift_focus (KittyX)
        call Sex_Dialog (KittyX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or KittyX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (KittyX)
                if "_angry" in KittyX.recent_history:
                    call Kitty_Pos_Reset
                    return
                $ KittyX.change_stat("lust", 200, 5)
                if 100 > KittyX.lust >= 70 and KittyX.session_orgasms < 2 and KittyX.SEXP >= 20:
                    $ KittyX.recent_history.append("unsatisfied")
                    $ KittyX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Kitty_FT_After
                $ Line = "came"

            if KittyX.lust >= 100:

                call Girl_Cumming (KittyX)
                if action_context == "shift" or "_angry" in KittyX.recent_history:
                    jump Kitty_FT_After

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
                            jump Kitty_FT_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if KittyX.SEXP >= 100 or approval_check(KittyX, 1200, "LO"):
            pass
        elif counter == (5 + KittyX.action_counter["fondle_thighs"]):
            $ KittyX.brows = "_confused"
            ch_k "You like how those feel, huh?"
        elif counter == (15 + KittyX.action_counter["fondle_thighs"]) and KittyX.SEXP >= 15 and not approval_check(KittyX, 1500):
            $ KittyX.brows = "_confused"
            menu:
                ch_k "You look like you're having fun there, but maybe we could[KittyX.like]try something else?"
                "Finish up.":
                    "You let go. . ."
                    jump Kitty_FT_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Kitty_FT_After
                "No, this is fun.":
                    if approval_check(KittyX, 1200) or approval_check(KittyX, 500, "O"):
                        $ KittyX.change_stat("love", 200, -5)
                        $ KittyX.change_stat("obedience", 50, 3)
                        $ KittyX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ KittyX.change_face("_angry", 1)
                        call Kitty_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_k "Fun for you maybe, I'm tired of it."
                        $ KittyX.change_stat("love", 50, -3, 1)
                        $ KittyX.change_stat("love", 80, -4, 1)
                        $ KittyX.change_stat("obedience", 30, -1, 1)
                        $ KittyX.change_stat("obedience", 50, -1, 1)
                        $ KittyX.recent_history.append("_angry")
                        $ KittyX.daily_history.append("_angry")
                        jump Kitty_FT_After


        call Escalation (KittyX)

        if Round == 10:
            ch_k "It's[KittyX.like]getting kinda late."
        elif Round == 5:
            ch_k "We should wrap this up."


    $ KittyX.change_face("_bemused", 0)
    $ Line = 0
    ch_k "Time to take a little break, for now."

label Kitty_FT_After:
    if not action_context:
        call Kitty_Pos_Reset

    $ KittyX.change_face("_sexy")

    $ KittyX.action_counter["fondle_thighs"]+= 1
    $ KittyX.remaining_actions -=1
    if KittyX.PantsNum() < 6 or KittyX.upskirt:
        $ KittyX.addiction_rate += 1
        if "addictive" in Player.traits:
            $ KittyX.addiction_rate += 1

        call Partner_Like (KittyX, 1)

    if KittyX.action_counter["fondle_thighs"]== 1:
        $ KittyX.SEXP += 3
        if not action_context:
            if KittyX.love >= 500 and "unsatisfied" not in KittyX.recent_history:
                ch_k "I liked that."
            elif KittyX.obedience <= 500 and Player.focus <= 20:
                $ KittyX.change_face("_perplexed", 1)
                ch_k "Was that enough?"

    $ approval_bonus = 0


    call checkout
    return


label Kitty_Fondle_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (KittyX)

    if KittyX.action_counter["fondle_pussy"]:
        $ approval_bonus += 20
    if KittyX.PantsNum() > 6 or KittyX.HoseNum() >= 5:
        $ approval_bonus -= 10
    if KittyX.lust > 75:
        $ approval_bonus += 15
    if KittyX.lust > 75 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in KittyX.traits:
        $ approval_bonus += (2*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in KittyX.traits:
        $ approval_bonus -= 25
    if KittyX.event_counter["forced"] and not KittyX.Forced:
        $ approval_bonus -= 5*KittyX.event_counter["forced"]

    if Taboo and "no_taboo" in KittyX.daily_history:
        $ approval_bonus -= 10

    if "no_fondle pussy" in KittyX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle pussy" in KittyX.recent_history else 0

    $ approval = approval_check(KittyX, 1050, TabM = 2)

    if action_context == "auto":
        if approval:
            $ KittyX.change_face("_sexy")
            $ KittyX.change_stat("obedience", 90, 1)
            $ KittyX.change_stat("obedience", 70, 2)
            $ KittyX.change_stat("inhibition", 70, 3)
            $ KittyX.change_stat("inhibition", 30, 2)
            "As your hand creeps up her thigh, [KittyX.name] seems a bit surprised, but then nods."
            jump Kitty_FP_Prep
        else:
            $ KittyX.change_face("_surprised")
            $ KittyX.change_stat("obedience", 50, -2)
            ch_k "Nuh-uh, [KittyX.player_petname], get back to what you were doing."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if action_context == "pullback":
        $ KittyX.change_face("_surprised")
        $ KittyX.brows = "_sad"
        if KittyX.lust > 80:
            $ KittyX.change_stat("love", 70, -4)
        $ KittyX.change_stat("obedience", 90, 1)
        $ KittyX.change_stat("obedience", 70, 2)
        "As your hand pulls out, [KittyX.name] gasps and looks upset."
        jump Kitty_FP_Prep
    elif "fondle_pussy" in KittyX.recent_history:
        $ KittyX.change_face("_sexy", 1)
        ch_k "Mmm, again? Ok."
        jump Kitty_FP_Prep
    elif "fondle_pussy" in KittyX.daily_history:
        $ KittyX.change_face("_sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Take it easy though.",
            "Take it a bit gently, I'm still shaking from earlier.",
            "Mmm. . ."])
        ch_k "[Line]"

    if approval >= 2:
        $ KittyX.change_face("_bemused", 1)
        if KittyX.Forced:
            $ KittyX.change_face("_sad")
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
            $ KittyX.change_stat("obedience", 90, 1)
            $ KittyX.change_stat("inhibition", 60, 1)
        ch_k "Ok, whatever."
        $ KittyX.change_stat("love", 90, 1)
        $ KittyX.change_stat("inhibition", 50, 3)
        jump Kitty_FP_Prep
    else:

        $ KittyX.change_face("_angry", 1)
        if "no_fondle pussy" in KittyX.recent_history:
            ch_k "I[KittyX.like]{i}just{/i} told you \"no!\""
        elif Taboo and "no_taboo" in KittyX.daily_history and "no_fondle pussy" in KittyX.daily_history:
            ch_k "I told you not to touch me like that in public!"
        elif "no_fondle pussy" in KittyX.daily_history:
            ch_k "[KittyX.Like]take a lesson, [KittyX.player_petname]."
        elif Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "Not here!"
        elif not KittyX.action_counter["fondle_pussy"]:
            $ KittyX.change_face("_bemused")
            ch_k "Um, not down there, [KittyX.player_petname]. . ."
        else:
            $ KittyX.change_face("_bemused")
            ch_k "Um, no."
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle pussy" in KittyX.daily_history:
                $ KittyX.change_face("_bemused")
                ch_k "Yeah, ok, [KittyX.player_petname]."
                return
            "Maybe later?" if "no_fondle pussy" not in KittyX.daily_history:
                $ KittyX.change_face("_sexy")
                ch_k "I'll give it some thought, [KittyX.player_petname]."
                $ KittyX.change_stat("love", 80, 2)
                $ KittyX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ KittyX.recent_history.append("no_taboo")
                    $ KittyX.daily_history.append("no_taboo")
                $ KittyX.recent_history.append("no_fondle pussy")
                $ KittyX.daily_history.append("no_fondle pussy")
                return
            "Come on, Please?":
                if approval:
                    $ KittyX.change_face("_sexy")
                    $ KittyX.change_stat("obedience", 90, 2)
                    $ KittyX.change_stat("obedience", 50, 2)
                    $ KittyX.change_stat("inhibition", 70, 3)
                    $ KittyX.change_stat("inhibition", 40, 2)
                    ch_k "I like it when you beg. . ."
                    jump Kitty_FP_Prep
                else:
                    $ KittyX.change_face("_sexy")
                    ch_k "Nuh uh."
            "[[Start fondling anyway]":

                $ approval = approval_check(KittyX, 450, "OI", TabM = 2)
                if approval > 1 or (approval and KittyX.Forced):
                    $ KittyX.change_face("_sad")
                    $ KittyX.change_stat("love", 70, -5, 1)
                    $ KittyX.change_stat("love", 200, -2)
                    ch_k "Well. . . I guess. . ."
                    $ KittyX.change_stat("obedience", 50, 4)
                    $ KittyX.change_stat("inhibition", 80, 1)
                    $ KittyX.change_stat("inhibition", 60, 3)
                    if approval < 2:
                        $ KittyX.Forced = 1
                    jump Kitty_FP_Prep
                else:
                    $ KittyX.change_stat("love", 200, -15)
                    $ KittyX.change_face("_angry", 1)
                    "She slaps your hand away."
                    $ KittyX.recent_history.append("_angry")
                    $ KittyX.daily_history.append("_angry")

    if "no_fondle pussy" in KittyX.daily_history:
        ch_k "How many times do I have to say \"no?\""
        $ KittyX.recent_history.append("_angry")
        $ KittyX.daily_history.append("_angry")
    elif KittyX.Forced:
        $ KittyX.change_face("_angry", 1)
        ch_k "Keep away from my kitty, [KittyX.player_petname]."
        $ KittyX.change_stat("lust", 70, 5)
        $ KittyX.change_stat("obedience", 50, -2)
        $ KittyX.recent_history.append("_angry")
        $ KittyX.daily_history.append("_angry")
    elif Taboo:
        $ KittyX.change_face("_angry", 1)
        $ KittyX.recent_history.append("no_taboo")
        $ KittyX.daily_history.append("no_taboo")
        ch_k "Time and place, [KittyX.player_petname]!"
    elif KittyX.action_counter["fondle_pussy"]:
        $ KittyX.change_face("_sad")
        ch_k "Sorry, keep your hands out of there."
    else:
        $ KittyX.change_face("_sexy")
        $ KittyX.mouth = "_sad"
        ch_k "No luck [KittyX.player_petname]."
    $ KittyX.recent_history.append("no_fondle pussy")
    $ KittyX.daily_history.append("no_fondle pussy")
    $ approval_bonus = 0
    return

label Kitty_FP_Prep:
    if offhand_action == "fondle_pussy":
        return

    call Kitty_Pussy_Launch ("fondle_pussy")

    if action_context == KittyX:

        $ action_context = 0
        if (KittyX.legs and not KittyX.upskirt) or (KittyX.underwear and not KittyX.underwear_pulled_down):

            if approval_check(KittyX, 1250, TabM = 1) or (KittyX.SeenPussy and approval_check(KittyX, 500) and not Taboo):
                $ KittyX.upskirt = 1
                $ KittyX.underwear_pulled_down = 1
                $ Line = 0
                if KittyX.PantsNum() == 5:
                    $ Line = KittyX.name + " hikes up her_skirt"
                elif KittyX.PantsNum() >= 5:
                    $ Line = KittyX.name + " pulls down her " + KittyX.legs
                else:
                    $ Line = 0
                if KittyX.underwear:
                    if Line:

                        "[Line] and pulls her [KittyX.underwear] out of the way."
                        "She then grabs your arm and then presses your hand against her crotch, clearly intending you to get to work."
                    else:

                        "She pulls her [KittyX.underwear] out of the way, and then presses your hand against her crotch."
                        "She clearly intends for you to get to work."
                else:

                    "[Line], and then presses your hand against her crotch."
                    "She clearly intends for you to get to work."
                call Kitty_First_Bottomless (1)
            else:
                "[KittyX.name] grabs your arm and presses your hand against her crotch, clearly intending you to get to work."
        else:
            "[KittyX.name] grabs your arm and presses your hand against her crotch, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ KittyX.change_stat("inhibition", 80, 3)
                $ KittyX.change_stat("inhibition", 50, 2)
                "You start to run your fingers along her pussy."
            "Praise her.":
                $ KittyX.change_face("_sexy", 1)
                $ KittyX.change_stat("inhibition", 80, 3)
                ch_p "I like the initiative, [KittyX.petname]."
                $ KittyX.nameCheck()
                "You start to run your fingers along her pussy."
                $ KittyX.change_stat("love", 85, 1)
                $ KittyX.change_stat("obedience", 90, 1)
                $ KittyX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your hand back."
                $ KittyX.change_face("_surprised")
                $ KittyX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [KittyX.petname]."
                $ KittyX.nameCheck()
                "[KittyX.name] pulls back."
                $ KittyX.change_stat("obedience", 90, 1)
                $ KittyX.change_stat("obedience", 50, 1)
                $ KittyX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ KittyX.add_word(1,"refused","refused")
                return


    if not KittyX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (KittyX)
        if "_angry" in KittyX.recent_history:
            return
    $ approval_bonus = 0
    if not KittyX.action_counter["fondle_pussy"]:
        if KittyX.Forced:
            $ KittyX.change_stat("love", 90, -50)
            $ KittyX.change_stat("obedience", 70, 35)
            $ KittyX.change_stat("inhibition", 80, 25)
        else:
            $ KittyX.change_stat("love", 90, 10)
            $ KittyX.change_stat("obedience", 70, 10)
            $ KittyX.change_stat("inhibition", 80, 15)
    if Taboo:
        $ KittyX.inhibition += int(Taboo/10)
        $ KittyX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ KittyX.drain_word("no_taboo")
    $ KittyX.drain_word("no_fondle pussy")
    $ KittyX.recent_history.append("fondle_pussy")
    $ KittyX.daily_history.append("fondle_pussy")

    $ action_speed = 1
    call Kitty_Pussy_Launch ("fondle_pussy")

label Kitty_FP_Cycle:
    while Round > 0:
        call ViewShift (KittyX, KittyX.pose, 0, "fondle_pussy")
        call shift_focus (KittyX)
        $ KittyX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass

                "I want to stick a finger in. . ." if action_speed != 2:
                    if KittyX.action_counter["finger_pussy"]:
                        $ action_speed = 2
                    else:
                        menu:
                            "Ask her first":
                                $ action_context = "shift"
                            "Don't ask first [[just stick it in]":
                                $ action_context = "auto"
                        call Kitty_Insert_Pussy

                "Pull back a bit. . ." if action_speed == 2:
                    $ action_speed = 0
                "Slap her ass":

                    call Slap_Ass (KittyX)
                    $ counter += 1
                    $ Round -= 1
                    jump Kitty_FP_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (KittyX, "menu")
                    jump Kitty_FP_Cycle
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
                                    "I want to lick your pussy.":
                                        $ action_context = "shift"
                                        call Kitty_FP_After
                                        call Kitty_Lick_Pussy
                                    "Just start licking":
                                        $ action_context = "auto"
                                        call Kitty_FP_After
                                        call Kitty_Lick_Pussy
                                    "Pull back to the thighs":
                                        $ action_context = "pullback"
                                        call Kitty_FP_After
                                        call Kitty_Fondle_Thighs
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Kitty_FP_After
                                        call Kitty_Dildo_Pussy
                                    "Never Mind":
                                        jump Kitty_FP_Cycle
                            else:
                                call Sex_Basic_Dialog (KittyX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Kitty_FP_After
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
                                    jump Kitty_FP_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Kitty_FP_Cycle
                                "Never mind":
                                    jump Kitty_FP_Cycle

                        "Show her feet" if not ShowFeet and (KittyX.pose == "doggy" or KittyX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (KittyX.pose == "doggy" or KittyX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [KittyX.name]":

                            call Girl_Undress (KittyX)
                        "Clean up [KittyX.name] (locked)" if not KittyX.spunk:
                            pass
                        "Clean up [KittyX.name]" if KittyX.spunk:
                            call Girl_Cleanup (KittyX, "ask")
                        "Never mind":
                            jump Kitty_FP_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Kitty_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Kitty_FP_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Kitty_Pos_Reset
                    $ Line = 0
                    jump Kitty_FP_After


        call shift_focus (KittyX)
        call Sex_Dialog (KittyX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or KittyX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (KittyX)
                if "_angry" in KittyX.recent_history:
                    call Kitty_Pos_Reset
                    return
                $ KittyX.change_stat("lust", 200, 5)
                if 100 > KittyX.lust >= 70 and KittyX.session_orgasms < 2:
                    $ KittyX.recent_history.append("unsatisfied")
                    $ KittyX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Kitty_FP_After
                $ Line = "came"

            if KittyX.lust >= 100:

                call Girl_Cumming (KittyX)
                if action_context == "shift" or "_angry" in KittyX.recent_history:
                    jump Kitty_FP_After

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
                            jump Kitty_FP_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if KittyX.SEXP >= 100 or approval_check(KittyX, 1200, "LO"):
            pass
        elif counter == (5 + KittyX.action_counter["fondle_pussy"]):
            $ KittyX.brows = "_confused"
            ch_k "You like how that feels, huh?"
        elif KittyX.lust >= 80:
            pass
        elif counter == (15 + KittyX.action_counter["fondle_pussy"]) and KittyX.SEXP >= 15 and not approval_check(KittyX, 1500):
            $ KittyX.brows = "_confused"
            menu:
                ch_k "You look like you're having fun there, but maybe we could[KittyX.like]try something else?"
                "Finish up.":
                    "You let go. . ."
                    jump Kitty_FP_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Kitty_FP_After
                "No, this is fun.":
                    if approval_check(KittyX, 1200) or approval_check(KittyX, 500, "O"):
                        $ KittyX.change_stat("love", 200, -5)
                        $ KittyX.change_stat("obedience", 50, 3)
                        $ KittyX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ KittyX.change_face("_angry", 1)
                        call Kitty_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_k "Fun for you maybe, I'm tired of it."
                        $ KittyX.change_stat("love", 50, -3, 1)
                        $ KittyX.change_stat("love", 80, -4, 1)
                        $ KittyX.change_stat("obedience", 30, -1, 1)
                        $ KittyX.change_stat("obedience", 50, -1, 1)
                        $ KittyX.recent_history.append("_angry")
                        $ KittyX.daily_history.append("_angry")
                        jump Kitty_FP_After


        call Escalation (KittyX)

        if Round == 10:
            ch_k "It's[KittyX.like]getting kinda late."
        elif Round == 5:
            ch_k "We should wrap this up."


    $ KittyX.change_face("_bemused", 0)
    $ Line = 0
    ch_k "Time to take a little break, for now."

label Kitty_FP_After:
    if not action_context:
        call Kitty_Pos_Reset

    $ KittyX.change_face("_sexy")

    $ KittyX.action_counter["fondle_pussy"] += 1
    $ KittyX.remaining_actions -=1
    if KittyX.PantsNum() < 6 or KittyX.upskirt:
        $ KittyX.addiction_rate += 1
        if "addictive" in Player.traits:
            $ KittyX.addiction_rate += 1

    call Partner_Like (KittyX, 2)

    if KittyX.action_counter["fondle_pussy"] == 1:
        $ KittyX.SEXP += 7
        if not action_context:
            if KittyX.love >= 500 and "unsatisfied" not in KittyX.recent_history:
                ch_k "Your hand is. . . bigger than mine."
            elif KittyX.obedience <= 500 and Player.focus <= 20:
                $ KittyX.change_face("_perplexed", 1)
                ch_k "Did you get what you needed?"

    $ approval_bonus = 0


    call checkout
    return




label Kitty_Insert_Pussy:
    call shift_focus (KittyX)
    if action_context == "auto":
        if approval_check(KittyX, 1100, TabM = 2):
            $ KittyX.change_face("_surprised")
            $ KittyX.change_stat("obedience", 90, 1)
            $ KittyX.change_stat("obedience", 70, 2)
            $ KittyX.change_stat("inhibition", 70, 3)
            $ KittyX.change_stat("inhibition", 30, 2)
            "As you slide a finger in, [KittyX.name] seems a bit surprised, but seems into it."
            jump Kitty_IP_Prep
        else:
            $ KittyX.change_face("_surprised",2)
            $ KittyX.change_stat("love", 80, -2)
            $ KittyX.change_stat("obedience", 50, -3)
            ch_k "Oooh!"
            "She slaps your hand back."
            $ KittyX.change_face("_perplexed",1)
            ch_k "Um, no take that out."
            return

    if approval_check(KittyX, 1100, TabM = 2):
        if KittyX.Forced:
            $ KittyX.change_face("_sad")
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
            $ KittyX.change_stat("obedience", 90, 1)
            $ KittyX.change_stat("inhibition", 60, 1)
            ch_k "Ok, whatever."
        else:
            $ KittyX.change_face("_sexy", 1)
            $ KittyX.change_stat("love", 90, 1)
            $ KittyX.change_stat("inhibition", 50, 3)
            ch_k "Mmmmmm."
        $ KittyX.change_stat("obedience", 20, 1)
        $ KittyX.change_stat("obedience", 60, 1)
        $ KittyX.change_stat("inhibition", 70, 2)
        jump Kitty_IP_Prep
    else:

        $ KittyX.change_face("_bemused", 2)
        ch_k "Um, no thanks, [KittyX.player_petname]."
        $ KittyX.blushing = "_blush1"
    return


label Kitty_IP_Prep:
    if not KittyX.action_counter["finger_pussy"]:
        $ KittyX.action_counter["finger_pussy"] = 1
        $ KittyX.SEXP += 10
        if KittyX.Forced:
            $ KittyX.change_stat("love", 90, -60)
            $ KittyX.change_stat("obedience", 70, 55)
            $ KittyX.change_stat("inhibition", 80, 35)
        else:
            $ KittyX.change_stat("love", 90, 10)
            $ KittyX.change_stat("obedience", 70, 20)
            $ KittyX.change_stat("inhibition", 80, 25)

    if not KittyX.Forced and action_context != "auto":
        call Girl_Undress (KittyX, "bottom")
        if "_angry" in KittyX.recent_history:
            return


    if Taboo:
        $ KittyX.inhibition += int(Taboo/10)
        $ KittyX.lust += int(Taboo/5)

    $ Line = 0
    $ action_speed = 2
    return







label Kitty_Lick_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (KittyX)

    if KittyX.action_counter["eat_pussy"]:
        $ approval_bonus += 15
    if KittyX.PantsNum() > 6 or KittyX.HoseNum() >= 5:
        $ approval_bonus -= 15
    if KittyX.lust > 95:
        $ approval_bonus += 20
    elif KittyX.lust > 85:
        $ approval_bonus += 15
    if action_context == "shift":
        $ approval_bonus += 10
    if KittyX.lust > 85 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in KittyX.traits:
        $ approval_bonus += (4*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in KittyX.traits:
        $ approval_bonus -= 25
    if KittyX.event_counter["forced"] and not KittyX.Forced:
        $ approval_bonus -= 5*KittyX.event_counter["forced"]

    if Taboo and "no_taboo" in KittyX.daily_history:
        $ approval_bonus -= 10

    if "no_lick pussy" in KittyX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_lick pussy" in KittyX.recent_history else 0

    $ approval = approval_check(KittyX, 1250, TabM = 4)

    if action_context == "auto":
        if approval:
            $ KittyX.change_face("_surprised")
            $ KittyX.change_stat("obedience", 90, 1)
            $ KittyX.change_stat("obedience", 70, 2)
            $ KittyX.change_stat("inhibition", 70, 3)
            $ KittyX.change_stat("inhibition", 30, 2)
            "As you crouch down and start to lick her pussy, [KittyX.name] jumps, but then softens."
            $ KittyX.change_face("_sexy")
            jump Kitty_LP_Prep
        else:
            $ KittyX.change_face("_surprised")
            $ KittyX.change_stat("love", 80, -2)
            $ KittyX.change_stat("obedience", 50, -3)
            ch_k "Oooo! Um, no, no thanks. No. . ."
            $ KittyX.change_face("_perplexed",1)
            "She pushes your head back away from her."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "eat_pussy" in KittyX.recent_history:
        $ KittyX.change_face("_sexy", 1)
        ch_k "Mmm, again? Ok."
        jump Kitty_LP_Prep
    elif "eat_pussy" in KittyX.daily_history:
        $ KittyX.change_face("_sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Huh? Again?",
            "I must have done something right.",
            "What a girl wants. . .",
            "Mmm. . ."])
        ch_k "[Line]"

    if approval >= 2:
        if KittyX.Forced:
            $ KittyX.change_face("_sad")
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
            $ KittyX.change_stat("obedience", 90, 1)
            $ KittyX.change_stat("inhibition", 60, 1)
            ch_k "Ok, whatever."
        else:
            $ KittyX.change_face("_sexy", 1)
            $ KittyX.eyes = "_closed"
            $ KittyX.change_stat("love", 90, 1)
            $ KittyX.change_stat("inhibition", 50, 3)
            $ KittyX.change_stat("lust", 200, 3)
            ch_k "Oooooooh. . ."
        $ KittyX.change_stat("obedience", 20, 1)
        $ KittyX.change_stat("obedience", 60, 1)
        $ KittyX.change_stat("inhibition", 70, 2)
        jump Kitty_LP_Prep
    else:

        $ KittyX.change_face("_angry", 1)
        if "no_lick pussy" in KittyX.recent_history:
            ch_k "I[KittyX.like]{i}just{/i} told you \"no!\""
        elif Taboo and "no_taboo" in KittyX.daily_history and "no_lick pussy" in KittyX.daily_history:
            ch_k "You already got your answer!"
        elif "no_lick pussy" in KittyX.daily_history:
            ch_k "[KittyX.Like]take a lesson, [KittyX.player_petname]."
        elif Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "Not here!"
        elif not KittyX.action_counter["eat_pussy"]:
            $ KittyX.change_face("_bemused")
            ch_k "That's pretty intimate, [KittyX.player_petname]. . ."
        else:
            $ KittyX.change_face("_bemused")
            ch_k "Oh, um, no, I'm not really comfortable with that. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_lick pussy" in KittyX.daily_history:
                $ KittyX.change_face("_bemused")
                ch_k "Yeah, ok, [KittyX.player_petname]."
                return
            "I'm sure I can convince you later. . ." if "no_lick pussy" not in KittyX.daily_history:
                $ KittyX.change_face("_sexy")
                ch_k "I'll be thinking about it, [KittyX.player_petname]."
                $ KittyX.change_stat("love", 80, 2)
                $ KittyX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ KittyX.recent_history.append("no_taboo")
                    $ KittyX.daily_history.append("no_taboo")
                $ KittyX.recent_history.append("no_lick pussy")
                $ KittyX.daily_history.append("no_lick pussy")
                return
            "I think you'd really enjoy it. . .":
                if approval:
                    $ KittyX.change_face("_sexy")
                    $ KittyX.change_stat("obedience", 90, 2)
                    $ KittyX.change_stat("obedience", 50, 2)
                    ch_k "Oh. . . you're probably right. . ."
                    $ KittyX.change_stat("inhibition", 70, 3)
                    $ KittyX.change_stat("inhibition", 40, 2)
                    jump Kitty_LP_Prep
                else:
                    $ KittyX.change_face("_sexy")
                    ch_k "Um, not this time, [KittyX.player_petname], that's too. . ."
            "[[Get in there anyway]":

                $ approval = approval_check(KittyX, 750, "OI", TabM = 4)
                if approval > 1 or (approval and KittyX.Forced):
                    $ KittyX.change_face("_sad")
                    $ KittyX.change_stat("love", 70, -5, 1)
                    $ KittyX.change_stat("love", 200, -2)
                    ch_k "Ok, get in there if you're so determined."
                    $ KittyX.change_stat("obedience", 50, 4)
                    $ KittyX.change_stat("inhibition", 80, 1)
                    $ KittyX.change_stat("inhibition", 60, 3)
                    if approval < 2:
                        $ KittyX.Forced = 1
                    jump Kitty_LP_Prep
                else:
                    $ KittyX.change_stat("love", 200, -15)
                    $ KittyX.change_face("_angry", 1)
                    "She shoves your head back."
                    $ KittyX.recent_history.append("_angry")
                    $ KittyX.daily_history.append("_angry")

    if "no_lick pussy" in KittyX.daily_history:
        ch_k "How many times do I have to say \"no?\""
        $ KittyX.recent_history.append("_angry")
        $ KittyX.daily_history.append("_angry")
    elif KittyX.Forced:
        $ KittyX.change_face("_angry", 1)
        ch_k "Not even, [KittyX.player_petname]."
        $ KittyX.change_stat("lust", 80, 5)
        $ KittyX.change_stat("obedience", 50, -2)
        $ KittyX.recent_history.append("_angry")
        $ KittyX.daily_history.append("_angry")
    elif Taboo:
        $ KittyX.change_face("_angry", 1)
        $ KittyX.recent_history.append("no_taboo")
        $ KittyX.daily_history.append("no_taboo")
        ch_k "This just really isn't the time or place, [KittyX.player_petname]!"
    elif KittyX.action_counter["eat_pussy"]:
        $ KittyX.change_face("_sad")
        ch_k "Keep your head out of there."
    else:
        $ KittyX.change_face("_surprised")
        ch_k "Ugh!"
        $ KittyX.change_face()
    $ KittyX.recent_history.append("no_lick pussy")
    $ KittyX.daily_history.append("no_lick pussy")
    $ approval_bonus = 0
    return

label Kitty_LP_Prep:
    if offhand_action == "eat_pussy":
        return

    call Kitty_Pussy_Launch ("eat_pussy")

    if action_context == KittyX:

        $ action_context = 0
        if (KittyX.legs and not KittyX.upskirt) or (KittyX.underwear and not KittyX.underwear_pulled_down):

            if approval_check(KittyX, 1250, TabM = 1) or (KittyX.SeenPussy and approval_check(KittyX, 500) and not Taboo):
                $ KittyX.upskirt = 1
                $ KittyX.underwear_pulled_down = 1
                $ Line = 0
                if KittyX.PantsNum() == 5:
                    $ Line = KittyX.name + " hikes up her_skirt"
                elif KittyX.PantsNum() >= 5:
                    $ Line = KittyX.name + " pulls down her " + KittyX.legs
                else:
                    $ Line = 0
                if KittyX.underwear:
                    if Line:

                        "[Line] and pulls her [KittyX.underwear] out of the way."
                        "She then grabs your head and pulls it to her crotch, clearly intending you to get to work."
                    else:

                        "She pulls her [KittyX.underwear] out of the way, and then shoves your face into her crotch."
                        "She clearly intends for you to get to work."
                else:

                    "[Line], and then shoves your face into her crotch."
                    "She clearly intends for you to get to work."
                call Kitty_First_Bottomless (1)
            else:
                "[KittyX.name] grabs your head and pulls it to her crotch, clearly intending you to get to work."
        else:
            "[KittyX.name] grabs your head and pulls it to her crotch, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ KittyX.change_stat("inhibition", 80, 3)
                $ KittyX.change_stat("inhibition", 50, 2)
                "You start licking."
            "Praise her.":
                $ KittyX.change_face("_sexy", 1)
                $ KittyX.change_stat("inhibition", 80, 3)
                ch_p "Mmm, I like this idea, [KittyX.petname]."
                $ KittyX.nameCheck()
                "You start licking."
                $ KittyX.change_stat("love", 85, 1)
                $ KittyX.change_stat("obedience", 90, 1)
                $ KittyX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your head away."
                $ KittyX.change_face("_surprised")
                $ KittyX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [KittyX.petname]."
                $ KittyX.nameCheck()
                "[KittyX.name] pulls back."
                $ KittyX.change_stat("obedience", 90, 1)
                $ KittyX.change_stat("obedience", 50, 1)
                $ KittyX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ KittyX.add_word(1,"refused","refused")
                return


    if not KittyX.Forced and action_context != "auto":
        $ approval_bonus = 0
        if KittyX.PantsNum() > 6:
            $ approval_bonus = 15
        call Bottoms_Off (KittyX)
        if "_angry" in KittyX.recent_history:
            return

    $ approval_bonus = 0
    if not KittyX.action_counter["eat_pussy"]:
        if KittyX.Forced:
            $ KittyX.change_stat("love", 90, -30)
            $ KittyX.change_stat("obedience", 70, 35)
            $ KittyX.change_stat("inhibition", 80, 75)
        else:
            $ KittyX.change_stat("love", 90, 35)
            $ KittyX.change_stat("obedience", 70, 15)
            $ KittyX.change_stat("inhibition", 80, 35)
    if Taboo:
        $ KittyX.inhibition += int(Taboo/10)
        $ KittyX.lust += int(Taboo/5)
    if action_context:
        $ renpy.pop_call()
        $ action_context = 0

    if KittyX.PantsNum() == 5:
        $ KittyX.upskirt = 1
        $ KittyX.SeenPanties = 1
    if not KittyX.underwear:
        call Kitty_First_Bottomless (1)

    $ Line = 0
    $ counter = 0
    if Taboo:
        $ KittyX.drain_word("no_taboo")
    $ KittyX.drain_word("no_lick pussy")
    $ KittyX.recent_history.append("eat_pussy")
    $ KittyX.daily_history.append("eat_pussy")
    call Kitty_Pussy_Launch ("eat_pussy")

label Kitty_LP_Cycle:
    if offhand_action == "kiss":
        $ offhand_action = 0
    while Round > 0:
        call ViewShift (KittyX, KittyX.pose, 0, "eat_pussy")
        call shift_focus (KittyX)
        $ KittyX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (KittyX)
                    $ counter += 1
                    $ Round -= 1
                    jump Kitty_LP_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (KittyX, "menu")
                    jump Kitty_LP_Cycle
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
                                    "Pull out and start rubbing again.":
                                        if KittyX.remaining_actions and multi_action:
                                            $ action_context = "pullback"
                                            call Kitty_LP_After
                                            call Kitty_Fondle_Pussy
                                        else:
                                            call Sex_Basic_Dialog (KittyX, "tired")
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Kitty_LP_After
                                        call Kitty_Dildo_Pussy
                                    "Never Mind":
                                        jump Kitty_LP_Cycle
                            else:
                                call Sex_Basic_Dialog (KittyX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Kitty_LP_After
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
                                    jump Kitty_LP_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Kitty_LP_Cycle
                                "Never mind":
                                    jump Kitty_LP_Cycle

                        "Show her feet" if not ShowFeet and (KittyX.pose == "doggy" or KittyX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (KittyX.pose == "doggy" or KittyX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [KittyX.name]":

                            call Girl_Undress (KittyX)
                        "Clean up [KittyX.name] (locked)" if not KittyX.spunk:
                            pass
                        "Clean up [KittyX.name]" if KittyX.spunk:
                            call Girl_Cleanup (KittyX, "ask")
                        "Never mind":
                            jump Kitty_LP_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Kitty_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Kitty_LP_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Kitty_Pos_Reset
                    $ Line = 0
                    jump Kitty_LP_After


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
                if "_angry" in KittyX.recent_history:
                    call Kitty_Pos_Reset
                    return
                $ KittyX.change_stat("lust", 200, 5)
                if 100 > KittyX.lust >= 70 and KittyX.session_orgasms < 2:
                    $ KittyX.recent_history.append("unsatisfied")
                    $ KittyX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Kitty_LP_After
                $ Line = "came"

            if KittyX.lust >= 100:

                call Girl_Cumming (KittyX)
                if action_context == "shift" or "_angry" in KittyX.recent_history:
                    jump Kitty_LP_After

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
                            jump Kitty_LP_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if KittyX.SEXP >= 100 or approval_check(KittyX, 1200, "LO"):
            pass
        elif counter == (5 + KittyX.action_counter["eat_pussy"]):
            $ KittyX.brows = "_confused"
            ch_k "You like it down there?"
        elif KittyX.lust >= 80:
            pass
        elif counter == (15 + KittyX.action_counter["eat_pussy"]) and KittyX.SEXP >= 15 and not approval_check(KittyX, 1500):
            $ KittyX.brows = "_confused"
            menu:
                ch_k "[KittyX.player_petname], I know you're having fun down there, but maybe we could try something else."
                "Finish up.":
                    "You let go. . ."
                    jump Kitty_LP_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Kitty_LP_After
                "No, this is fun.":
                    if approval_check(KittyX, 1200) or approval_check(KittyX, 500, "O"):
                        $ KittyX.change_stat("love", 200, -5)
                        $ KittyX.change_stat("obedience", 50, 3)
                        $ KittyX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ KittyX.change_face("_angry", 1)
                        call Kitty_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_k "Fun for you maybe, I'm tired of it."
                        $ KittyX.change_stat("love", 50, -3, 1)
                        $ KittyX.change_stat("love", 80, -4, 1)
                        $ KittyX.change_stat("obedience", 30, -1, 1)
                        $ KittyX.change_stat("obedience", 50, -1, 1)
                        $ KittyX.recent_history.append("_angry")
                        $ KittyX.daily_history.append("_angry")
                        jump Kitty_LP_After


        call Escalation (KittyX)

        if Round == 10:
            ch_k "It's[KittyX.like]getting kinda late."
        elif Round == 5:
            ch_k "We should wrap this up."


    $ KittyX.change_face("_bemused", 0)
    $ Line = 0
    ch_k "Time to take a little break, for now."

label Kitty_LP_After:
    if not action_context:
        call Kitty_Pos_Reset

    $ KittyX.change_face("_sexy")

    $ KittyX.action_counter["eat_pussy"] += 1
    $ KittyX.remaining_actions -=1
    if KittyX.PantsNum() < 6 or KittyX.upskirt:
        $ KittyX.addiction_rate += 1
        if "addictive" in Player.traits:
            $ KittyX.addiction_rate += 1

    call Partner_Like (KittyX, 3, 2)

    if KittyX.action_counter["eat_pussy"] == 1:
        $ KittyX.SEXP += 10
        if not action_context:
            if KittyX.love >= 500 and "unsatisfied" not in KittyX.recent_history:
                ch_k "Was it. . . good?"
            elif KittyX.obedience <= 500 and Player.focus <= 20:
                $ KittyX.change_face("_perplexed", 1)
                ch_k "Well, did you like the taste?"

    $ approval_bonus = 0


    call checkout
    return






label Kitty_Fondle_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (KittyX)

    if KittyX.action_counter["fondle_ass"]:
        $ approval_bonus += 10
    if KittyX.PantsNum() > 6 or KittyX.HoseNum() >= 5:
        $ approval_bonus -= 5
    if KittyX.lust > 75:
        $ approval_bonus += 15
    if "exhibitionist" in KittyX.traits:
        $ approval_bonus += Taboo
    if KittyX in Player.Harem or "sex friend" in KittyX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in KittyX.traits:
        $ approval_bonus -= 25
    if KittyX.event_counter["forced"] and not KittyX.Forced:
        $ approval_bonus -= 5*KittyX.event_counter["forced"]

    if Taboo and "no_taboo" in KittyX.daily_history:
        $ approval_bonus -= 10

    if "no_fondle ass" in KittyX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_fondle ass" in KittyX.recent_history else 0

    $ approval = approval_check(KittyX, 850, TabM=1)

    if action_context == "auto":
        if approval:
            $ KittyX.change_face("_surprised", 1)
            $ KittyX.change_stat("obedience", 70, 2)
            $ KittyX.change_stat("inhibition", 40, 2)
            "As your hand creeps down her backside, [KittyX.name] jumps a bit, and then relaxes."
            $ KittyX.change_face("_sexy")
            jump Kitty_FA_Prep
        else:
            $ KittyX.change_face("_surprised")
            $ KittyX.change_stat("obedience", 50, -3)
            ch_k "Hands off, [KittyX.player_petname]."
            $ KittyX.change_face("_bemused")
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if action_context == "pullback":
        $ KittyX.change_face("_surprised")
        $ KittyX.brows = "_sad"
        if KittyX.lust > 80:
            $ KittyX.change_stat("love", 70, -4)
        $ KittyX.change_stat("obedience", 90, 1)
        $ KittyX.change_stat("obedience", 70, 2)
        "As your finger slides out, [KittyX.name] gasps and looks upset."
        jump Kitty_FA_Prep
    elif "fondle_ass" in KittyX.recent_history:
        $ KittyX.change_face("_sexy", 1)
        ch_k "Mmm, again? Ok."
        jump Kitty_FA_Prep
    elif "fondle_ass" in KittyX.daily_history:
        $ KittyX.change_face("_sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Maybe not so rough this time though.",
            "Mmm. . ."])
        ch_k "[Line]"

    if approval >= 2:
        if KittyX.Forced:
            $ KittyX.change_face("_sad")
            $ KittyX.change_stat("love", 70, -2, 1)
            $ KittyX.change_stat("obedience", 90, 2)
            $ KittyX.change_stat("inhibition", 60, 2)
            ch_k "Ok, geeze."
        else:
            $ KittyX.change_face("bemused, 1")
            ch_k "Ok, go for it."
        $ KittyX.change_stat("lust", 200, 3)
        $ KittyX.change_stat("obedience", 60, 1)
        $ KittyX.change_stat("inhibition", 70, 1)
        jump Kitty_FA_Prep
    else:

        $ KittyX.change_face("_angry", 1)
        if "no_fondle ass" in KittyX.recent_history:
            ch_k "I[KittyX.like]{i}just{/i} told you \"no!\""
        elif Taboo and "no_taboo" in KittyX.daily_history and "no_fondle ass" in KittyX.daily_history:
            ch_k "I told you not to touch me like that in public!"
        elif "no_fondle ass" in KittyX.daily_history:
            ch_k "[KittyX.Like]take a lesson, [KittyX.player_petname]."
        elif Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "Not here!"
        elif not KittyX.action_counter["fondle_ass"]:
            $ KittyX.change_face("_bemused")
            ch_k "Not yet, [KittyX.player_petname]. . ."
        else:
            $ KittyX.change_face("_bemused")
            ch_k "Let's not, ok [KittyX.player_petname]?"
        menu:
            extend ""
            "Sorry, never mind." if "no_fondle ass" in KittyX.daily_history:
                $ KittyX.change_face("_bemused")
                ch_k "Yeah, ok, [KittyX.player_petname]."
                return
            "Maybe later?" if "no_fondle ass" not in KittyX.daily_history:
                $ KittyX.change_face("_sexy")
                ch_k "Heh, maybe, [KittyX.player_petname]."
                $ KittyX.change_stat("love", 80, 2)
                $ KittyX.change_stat("inhibition", 50, 2)
                if Taboo:
                    $ KittyX.recent_history.append("no_taboo")
                    $ KittyX.daily_history.append("no_taboo")
                $ KittyX.recent_history.append("no_fondle ass")
                $ KittyX.daily_history.append("no_fondle ass")
                return
            "Just one good squeeze?":
                if approval:
                    $ KittyX.change_face("_sexy")
                    $ KittyX.change_stat("obedience", 90, 1)
                    $ KittyX.change_stat("obedience", 50, 2)
                    ch_k "I like it when you beg. . ."
                    $ KittyX.change_stat("inhibition", 70, 1)
                    $ KittyX.change_stat("inhibition", 40, 2)
                    jump Kitty_FA_Prep
                else:
                    $ KittyX.change_face("_sexy")
                    ch_k "Nuh uh."
            "[[Start fondling anyway]":

                $ approval = approval_check(KittyX, 250, "OI", TabM = 3)
                if approval > 1 or (approval and KittyX.Forced):
                    $ KittyX.change_face("_sad")
                    $ KittyX.change_stat("love", 70, -3, 1)
                    $ KittyX.change_stat("love", 200, -1)
                    ch_k "Fine, I suppose."
                    $ KittyX.change_stat("obedience", 50, 3)
                    $ KittyX.change_stat("inhibition", 60, 3)
                    if approval < 2:
                        $ KittyX.Forced = 1
                    jump Kitty_FA_Prep
                else:
                    $ KittyX.change_stat("love", 200, -10)
                    $ KittyX.change_face("_angry", 1)
                    "She slaps your hand away."
                    $ KittyX.recent_history.append("_angry")
                    $ KittyX.daily_history.append("_angry")

    if "no_fondle ass" in KittyX.daily_history:
        ch_k "How many times do I have to say \"no?\""
        $ KittyX.recent_history.append("_angry")
        $ KittyX.daily_history.append("_angry")
    elif KittyX.Forced:
        $ KittyX.change_face("_angry", 1)
        ch_k "Back off!"
        $ KittyX.change_stat("lust", 60, 5)
        $ KittyX.change_stat("obedience", 50, -2)
        $ KittyX.recent_history.append("_angry")
        $ KittyX.daily_history.append("_angry")
    elif Taboo:
        $ KittyX.change_face("_angry", 1)
        $ KittyX.recent_history.append("no_taboo")
        $ KittyX.daily_history.append("no_taboo")
        ch_k "[KittyX.player_petname]! Not here!"
    elif KittyX.action_counter["fondle_ass"]:
        $ KittyX.change_face("_sad")
        ch_k "Sorry, hands to yourself."
    else:
        $ KittyX.change_face("_sexy")
        $ KittyX.mouth = "_sad"
        ch_k "Scram, [KittyX.player_petname]."
    $ KittyX.recent_history.append("no_fondle ass")
    $ KittyX.daily_history.append("no_fondle ass")
    $ approval_bonus = 0
    return

ch_k "Sorry, I don't even know how I got here. . ."
return

label Kitty_FA_Prep:
    if offhand_action == "fondle_ass":
        return
    if not KittyX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (KittyX)
        if "_angry" in KittyX.recent_history:
            return
    $ approval_bonus = 0
    call Kitty_Pussy_Launch ("fondle_ass")
    if not KittyX.action_counter["fondle_ass"]:
        if KittyX.Forced:
            $ KittyX.change_stat("love", 90, -20)
            $ KittyX.change_stat("obedience", 70, 20)
            $ KittyX.change_stat("inhibition", 80, 15)
        else:
            $ KittyX.change_stat("love", 90, 10)
            $ KittyX.change_stat("obedience", 70, 12)
            $ KittyX.change_stat("inhibition", 80, 20)
    if Taboo:
        $ KittyX.inhibition += int(Taboo/10)
        $ KittyX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ KittyX.drain_word("no_taboo")
    $ KittyX.drain_word("no_fondle ass")
    $ KittyX.recent_history.append("fondle_ass")
    $ KittyX.daily_history.append("fondle_ass")
    call Kitty_Pussy_Launch ("fondle_ass")

label Kitty_FA_Cycle:
    while Round > 0:
        call ViewShift (KittyX, KittyX.pose, 0, "fondle_ass")
        call shift_focus (KittyX)
        $ KittyX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (KittyX)
                    $ counter += 1
                    $ Round -= 1
                    jump Kitty_FA_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (KittyX, "menu")
                    jump Kitty_FA_Cycle
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
                                    "I want to stick a finger in.":
                                        $ action_context = "shift"
                                        call Kitty_FA_After
                                        call Kitty_Insert_Ass
                                    "Just stick a finger in without asking.":
                                        $ action_context = "auto"
                                        call Kitty_FA_After
                                        call Kitty_Insert_Ass
                                    "I want to lick your asshole.":
                                        $ action_context = "shift"
                                        call Kitty_FA_After
                                        call Kitty_Lick_Ass
                                    "Just start licking.":
                                        $ action_context = "auto"
                                        call Kitty_FA_After
                                        call Kitty_Lick_Ass
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Kitty_FA_After
                                        call Kitty_Dildo_Ass
                                    "Never Mind":
                                        jump Kitty_FA_Cycle
                            else:
                                call Sex_Basic_Dialog (KittyX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Kitty_FA_After
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
                                    jump Kitty_FA_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Kitty_FA_Cycle
                                "Never mind":
                                    jump Kitty_FA_Cycle

                        "Show her feet" if not ShowFeet and (KittyX.pose == "doggy" or KittyX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (KittyX.pose == "doggy" or KittyX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [KittyX.name]":

                            call Girl_Undress (KittyX)
                        "Clean up [KittyX.name] (locked)" if not KittyX.spunk:
                            pass
                        "Clean up [KittyX.name]" if KittyX.spunk:
                            call Girl_Cleanup (KittyX, "ask")
                        "Never mind":
                            jump Kitty_FA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Kitty_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Kitty_FA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Kitty_Pos_Reset
                    $ Line = 0
                    jump Kitty_FA_After


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
                if "_angry" in KittyX.recent_history:
                    call Kitty_Pos_Reset
                    return
                $ KittyX.change_stat("lust", 200, 5)
                if 100 > KittyX.lust >= 70 and KittyX.session_orgasms < 2 and KittyX.SEXP >= 20:
                    $ KittyX.recent_history.append("unsatisfied")
                    $ KittyX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Kitty_FA_After
                $ Line = "came"

            if KittyX.lust >= 100:

                call Girl_Cumming (KittyX)
                if action_context == "shift" or "_angry" in KittyX.recent_history:
                    jump Kitty_FA_After

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
                            jump Kitty_FA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if KittyX.SEXP >= 100 or approval_check(KittyX, 1200, "LO"):
            pass
        elif counter == (5 + KittyX.action_counter["fondle_ass"]):
            $ KittyX.brows = "_confused"
            ch_k "Uh, that's nice, but. . ."
        elif KittyX.lust >= 80:
            pass
        elif counter == (15 + KittyX.action_counter["fondle_ass"]) and KittyX.SEXP >= 15 and not approval_check(KittyX, 1500):
            $ KittyX.brows = "_confused"
            menu:
                ch_k "[KittyX.player_petname], this is nice, but could we do something else?"
                "Finish up.":
                    "You let go. . ."
                    jump Kitty_FA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Kitty_FA_After
                "No, this is fun.":
                    if approval_check(KittyX, 1200) or approval_check(KittyX, 500, "O"):
                        $ KittyX.change_stat("love", 200, -5)
                        $ KittyX.change_stat("obedience", 50, 3)
                        $ KittyX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ KittyX.change_face("_angry", 1)
                        call Kitty_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_k "Fun for you maybe, I'm tired of it."
                        $ KittyX.change_stat("love", 50, -3, 1)
                        $ KittyX.change_stat("love", 80, -4, 1)
                        $ KittyX.change_stat("obedience", 30, -1, 1)
                        $ KittyX.change_stat("obedience", 50, -1, 1)
                        $ KittyX.recent_history.append("_angry")
                        $ KittyX.daily_history.append("_angry")
                        jump Kitty_FA_After


        call Escalation (KittyX)

        if Round == 10:
            ch_k "It's[KittyX.like]getting kinda late."
        elif Round == 5:
            ch_k "We should wrap this up."


    $ KittyX.change_face("_bemused", 0)
    $ Line = 0
    ch_k "Time to take a little break, for now."


label Kitty_FA_After:
    if not action_context:
        call Kitty_Pos_Reset

    $ KittyX.change_face("_sexy")

    $ KittyX.action_counter["fondle_ass"] += 1
    $ KittyX.remaining_actions -=1
    if KittyX.PantsNum() < 6 or KittyX.upskirt:
        $ KittyX.addiction_rate += 1
        if "addictive" in Player.traits:
            $ KittyX.addiction_rate += 1

        call Partner_Like (KittyX, 2)

    if KittyX.action_counter["fondle_ass"] == 1:
        $ KittyX.SEXP += 4
        if not action_context:
            if KittyX.love >= 500 and "unsatisfied" not in KittyX.recent_history:
                ch_k "Huh. . . um. . ."
            elif KittyX.obedience <= 500 and Player.focus <= 20:
                $ KittyX.change_face("_perplexed", 1)
                ch_k "Did you like that?"

    $ approval_bonus = 0


    call checkout
    return





label Kitty_Insert_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (KittyX)

    if KittyX.action_counter["finger_ass"]:
        $ approval_bonus += 25
    if KittyX.PantsNum() > 6 or KittyX.HoseNum() >= 5:
        $ approval_bonus -= 15
    if KittyX.lust > 85 and KittyX.used_to_anal:
        $ approval_bonus += 15
    if KittyX.lust > 95 and KittyX.used_to_anal:
        $ approval_bonus += 5
    if action_context == "shift":
        $ approval_bonus += 10
    if KittyX.lust > 85 and action_context == "auto":
        $ approval_bonus += 10
    if "exhibitionist" in KittyX.traits:
        $ approval_bonus += (4*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in KittyX.traits:
        $ approval_bonus -= 25
    if KittyX.event_counter["forced"] and not KittyX.Forced:
        $ approval_bonus -= 5*KittyX.event_counter["forced"]

    if Taboo and "no_taboo" in KittyX.daily_history:
        $ approval_bonus -= 10

    if "no_insert ass" in KittyX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_insert ass" in KittyX.recent_history else 0

    $ approval = approval_check(KittyX, 1300, TabM = 3)

    if action_context == "auto":
        if approval:
            $ KittyX.change_face("_surprised")
            $ KittyX.change_stat("obedience", 90, 2)
            $ KittyX.change_stat("obedience", 70, 2)
            $ KittyX.change_stat("inhibition", 80, 2)
            $ KittyX.change_stat("inhibition", 30, 2)
            "As you slide a finger in, [KittyX.name] tightens around it in surprise, but seems into it."
            $ KittyX.change_face("_sexy")
            jump Kitty_IA_Prep
        else:
            $ KittyX.change_face("_surprised")
            $ KittyX.change_stat("love", 80, -2)
            $ KittyX.change_stat("obedience", 50, -3)
            ch_k "Whoa, back off, [KittyX.player_petname]."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "finger_ass" in KittyX.daily_history and not KittyX.used_to_anal:
        $ KittyX.change_face("_bemused", 1)
        ch_k "I'm still a little sore from earlier, [KittyX.player_petname]."
    elif "finger_ass" in KittyX.daily_history:
        $ KittyX.change_face("_sexy", 1)
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Take it easy though.",
            "Mmm. . ."])
        ch_k "[Line]"

    if approval >= 2:
        if KittyX.Forced:
            $ KittyX.change_face("_sad")
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
            $ KittyX.change_stat("obedience", 90, 1)
            $ KittyX.change_stat("inhibition", 60, 1)
            ch_k "Ok, whatever."
        else:
            $ KittyX.change_face("_sexy", 1)
            $ KittyX.eyes = "_closed"
            $ KittyX.change_stat("love", 90, 1)
            $ KittyX.change_stat("inhibition", 50, 3)
            $ KittyX.change_stat("lust", 200, 3)
            ch_k "Mmmmm. . ."
        $ KittyX.change_stat("obedience", 20, 1)
        $ KittyX.change_stat("obedience", 60, 1)
        $ KittyX.change_stat("inhibition", 70, 2)
        jump Kitty_IA_Prep
    else:

        $ KittyX.change_face("_angry", 1)
        if "no_insert ass" in KittyX.recent_history:
            ch_k "I[KittyX.like]{i}just{/i} told you \"no!\""
        elif Taboo and "no_taboo" in KittyX.daily_history and "no_insert ass" in KittyX.daily_history:
            ch_k "I told you that wasn't appropriate!"
        elif "no_insert ass" in KittyX.daily_history:
            ch_k "[KittyX.Like]take a lesson, [KittyX.player_petname]."
        elif Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "Not here!"
        elif not KittyX.action_counter["finger_ass"]:
            $ KittyX.change_face("_perplexed", 1)
            ch_k "I. . . don't think that's. . ."
        else:
            $ KittyX.change_face("_bemused")
            ch_k "Oh, um, no, I'm not really comfortable with that. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_insert ass" in KittyX.daily_history:
                $ KittyX.change_face("_bemused")
                ch_k "Yeah, ok, [KittyX.player_petname]."
                return
            "Maybe later?" if "no_insert ass" not in KittyX.daily_history:
                $ KittyX.change_face("_sexy")
                ch_k "It's. . . possible, [KittyX.player_petname]."
                $ KittyX.change_stat("love", 80, 2)
                $ KittyX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ KittyX.recent_history.append("no_taboo")
                    $ KittyX.daily_history.append("no_taboo")
                $ KittyX.recent_history.append("no_insert ass")
                $ KittyX.daily_history.append("no_insert ass")
                return
            "I think you'd really enjoy it. . .":
                if approval:
                    $ KittyX.change_face("_sexy")
                    $ KittyX.change_stat("obedience", 90, 2)
                    $ KittyX.change_stat("obedience", 50, 2)
                    ch_k "Ok, you're probably right. . ."
                    $ KittyX.change_stat("inhibition", 70, 3)
                    $ KittyX.change_stat("inhibition", 40, 2)
                    jump Kitty_IA_Prep
                else:
                    $ KittyX.change_face("_bemused")
                    ch_k "I really don't think that I would."
            "[[Slide a finger in anyway]":

                $ approval = approval_check(KittyX, 950, "OI", TabM = 3)
                if approval > 1 or (approval and KittyX.Forced):
                    $ KittyX.change_face("_surprised", 1)
                    $ KittyX.change_stat("love", 70, -5, 1)
                    $ KittyX.change_stat("love", 200, -2)
                    ch_k "Oh. . . well, ok then. . ."
                    $ KittyX.change_face("_sad")
                    $ KittyX.change_stat("obedience", 50, 4)
                    $ KittyX.change_stat("inhibition", 80, 1)
                    $ KittyX.change_stat("inhibition", 60, 3)
                    if approval < 2:
                        $ KittyX.Forced = 1
                    jump Kitty_IA_Prep
                else:
                    $ KittyX.change_stat("love", 200, -15)
                    $ KittyX.change_face("_angry", 1)
                    "She slaps your hand away."
                    $ KittyX.recent_history.append("_angry")
                    $ KittyX.daily_history.append("_angry")

    if "no_insert ass" in KittyX.daily_history:
        ch_k "How many times do I have to say \"no?\""
        $ KittyX.recent_history.append("_angry")
        $ KittyX.daily_history.append("_angry")
    elif KittyX.Forced:
        $ KittyX.change_face("_angry", 1)
        ch_k "Um, no way."
        if approval_check(KittyX, 500, "I"):
            $ KittyX.change_stat("lust", 80, 10)
        else:
            $ KittyX.change_stat("lust", 50, 3)
        $ KittyX.change_stat("obedience", 50, -2)
        $ KittyX.recent_history.append("_angry")
        $ KittyX.daily_history.append("_angry")
    elif Taboo:
        $ KittyX.change_face("_angry", 1)
        $ KittyX.recent_history.append("no_taboo")
        $ KittyX.daily_history.append("no_taboo")
        ch_k "[KittyX.player_petname]! Time and place!"
    elif KittyX.action_counter["finger_ass"]:
        $ KittyX.change_face("_sad")
        ch_k "I don't feel like it."
    else:
        $ KittyX.change_face("_surprised")
        ch_k "That's. . . not cool."
        $ KittyX.change_face()
    $ KittyX.recent_history.append("no_insert ass")
    $ KittyX.daily_history.append("no_insert ass")
    $ approval_bonus = 0
    return


label Kitty_IA_Prep:
    if offhand_action == "finger_ass":
        return

    call Kitty_Pussy_Launch ("finger_ass")

    if action_context == KittyX:

        $ action_context = 0
        if (KittyX.legs and not KittyX.upskirt) or (KittyX.underwear and not KittyX.underwear_pulled_down):

            if approval_check(KittyX, 1250, TabM = 1) or (KittyX.SeenPussy and approval_check(KittyX, 500) and not Taboo):
                $ KittyX.upskirt = 1
                $ KittyX.underwear_pulled_down = 1
                $ Line = 0
                if KittyX.PantsNum() == 5:
                    $ Line = KittyX.name + " hikes up her_skirt"
                elif KittyX.PantsNum() >= 5:
                    $ Line = KittyX.name + " pulls down her " + KittyX.legs
                else:
                    $ Line = 0
                if KittyX.underwear:
                    if Line:

                        "[Line] and pulls her [KittyX.underwear] out of the way."
                        "She then grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
                    else:

                        "She pulls her [KittyX.underwear] out of the way, and then presses your hand against her asshole."
                        "She clearly intends for you to get to work."
                else:

                    "[Line], and then presses your hand against her asshole."
                    "She clearly intends for you to get to work."
                call Kitty_First_Bottomless (1)
            else:
                "[KittyX.name] grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
        else:
            "[KittyX.name] grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ KittyX.change_stat("inhibition", 80, 3)
                $ KittyX.change_stat("inhibition", 50, 2)
                "You press your finger into it."
            "Praise her.":
                $ KittyX.change_face("_sexy", 1)
                $ KittyX.change_stat("inhibition", 80, 3)
                ch_p "Dirty girl, [KittyX.petname]."
                $ KittyX.nameCheck()
                "You press your finger into it."
                $ KittyX.change_stat("love", 85, 1)
                $ KittyX.change_stat("obedience", 90, 1)
                $ KittyX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your hand back."
                $ KittyX.change_face("_surprised")
                $ KittyX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [KittyX.petname]."
                $ KittyX.nameCheck()
                "[KittyX.name] pulls back."
                $ KittyX.change_stat("obedience", 90, 1)
                $ KittyX.change_stat("obedience", 50, 1)
                $ KittyX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ KittyX.add_word(1,"refused","refused")
                return


    if not KittyX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (KittyX)
        if "_angry" in KittyX.recent_history:
            return

    $ approval_bonus = 0
    if not KittyX.action_counter["finger_ass"]:
        if KittyX.Forced:
            $ KittyX.change_stat("love", 90, -50)
            $ KittyX.change_stat("obedience", 70, 60)
            $ KittyX.change_stat("inhibition", 80, 35)
        else:
            $ KittyX.change_stat("love", 90, 10)
            $ KittyX.change_stat("obedience", 70, 20)
            $ KittyX.change_stat("inhibition", 80, 25)

    if Taboo:
        $ KittyX.inhibition += int(Taboo/10)
        $ KittyX.lust += int(Taboo/5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ KittyX.drain_word("no_taboo")
    $ KittyX.drain_word("no_insert ass")
    $ KittyX.recent_history.append("finger_ass")
    $ KittyX.daily_history.append("finger_ass")
    call Kitty_Pussy_Launch ("finger_ass")

label Kitty_IA_Cycle:
    while Round > 0:
        call ViewShift (KittyX, KittyX.pose, 0, "finger_ass")
        call shift_focus (KittyX)
        $ KittyX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (KittyX)
                    $ counter += 1
                    $ Round -= 1
                    jump Kitty_IA_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (KittyX, "menu")
                    jump Kitty_IA_Cycle
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
                                    "Pull out and start rubbing again.":
                                        $ action_context = "pullback"
                                        call Kitty_IA_After
                                        call Kitty_Fondle_Ass
                                    "I want to lick your asshole.":
                                        $ action_context = "shift"
                                        call Kitty_IA_After
                                        call Kitty_Lick_Ass
                                    "Just start licking.":
                                        $ action_context = "auto"
                                        call Kitty_IA_After
                                        call Kitty_Lick_Ass
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Kitty_IA_After
                                        call Kitty_Dildo_Ass
                                    "Never Mind":
                                        jump Kitty_IA_Cycle
                            else:
                                call Sex_Basic_Dialog (KittyX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Kitty_IA_After
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
                                    jump Kitty_IA_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Kitty_IA_Cycle
                                "Never mind":
                                    jump Kitty_IA_Cycle

                        "Show her feet" if not ShowFeet and (KittyX.pose == "doggy" or KittyX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (KittyX.pose == "doggy" or KittyX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [KittyX.name]":

                            call Girl_Undress (KittyX)
                        "Clean up [KittyX.name] (locked)" if not KittyX.spunk:
                            pass
                        "Clean up [KittyX.name]" if KittyX.spunk:
                            call Girl_Cleanup (KittyX, "ask")
                        "Never mind":
                            jump Kitty_IA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Kitty_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Kitty_IA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Kitty_Pos_Reset
                    $ Line = 0
                    jump Kitty_IA_After


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
                if "_angry" in KittyX.recent_history:
                    call Kitty_Pos_Reset
                    return
                $ KittyX.change_stat("lust", 200, 5)
                if 100 > KittyX.lust >= 70 and KittyX.session_orgasms < 2:
                    $ KittyX.recent_history.append("unsatisfied")
                    $ KittyX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Kitty_IA_After
                $ Line = "came"

            if KittyX.lust >= 100:

                call Girl_Cumming (KittyX)
                if action_context == "shift" or "_angry" in KittyX.recent_history:
                    jump Kitty_IA_After

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
                            jump Kitty_IA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if KittyX.SEXP >= 100 or approval_check(KittyX, 1200, "LO"):
            pass
        elif counter == (5 + KittyX.action_counter["finger_ass"]):
            $ KittyX.brows = "_confused"
            ch_k "What are you even?"
        elif KittyX.lust >= 80:
            pass
        elif counter == (15 + KittyX.action_counter["finger_ass"]) and KittyX.SEXP >= 15 and not approval_check(KittyX, 1500):
            $ KittyX.brows = "_confused"
            menu:
                ch_k "[KittyX.player_petname], this is getting kind sore, maybe we could try something else."
                "Finish up.":
                    "You let go. . ."
                    jump Kitty_IA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Kitty_IA_After
                "No, this is fun.":
                    if approval_check(KittyX, 1200) or approval_check(KittyX, 500, "O"):
                        $ KittyX.change_stat("love", 200, -5)
                        $ KittyX.change_stat("obedience", 50, 3)
                        $ KittyX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ KittyX.change_face("_angry", 1)
                        call Kitty_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_k "Fun for you maybe, I'm tired of it."
                        $ KittyX.change_stat("love", 50, -3, 1)
                        $ KittyX.change_stat("love", 80, -4, 1)
                        $ KittyX.change_stat("obedience", 30, -1, 1)
                        $ KittyX.change_stat("obedience", 50, -1, 1)
                        $ KittyX.recent_history.append("_angry")
                        $ KittyX.daily_history.append("_angry")
                        jump Kitty_IA_After


        call Escalation (KittyX)

        if Round == 10:
            ch_k "It's[KittyX.like]getting kinda late."
        elif Round == 5:
            ch_k "We should wrap this up."


    $ KittyX.change_face("_bemused", 0)
    $ Line = 0
    ch_k "Time to take a little break, for now."

label Kitty_IA_After:
    if not action_context:
        call Kitty_Pos_Reset

    $ KittyX.change_face("_sexy")

    $ KittyX.action_counter["finger_ass"] += 1
    $ KittyX.remaining_actions -=1
    $ KittyX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ KittyX.addiction_rate += 1

    call Partner_Like (KittyX, 2)

    if KittyX.action_counter["finger_ass"] == 1:
        $ KittyX.SEXP += 12
        if not action_context:
            if KittyX.love >= 500 and "unsatisfied" not in KittyX.recent_history:
                ch_k "That was odd. . ."
            elif KittyX.obedience <= 500 and Player.focus <= 20:
                $ KittyX.change_face("_perplexed", 1)
                ch_k "Well? Satisfied?"

    $ approval_bonus = 0


    call checkout
    return








label Kitty_Lick_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (KittyX)

    if KittyX.action_counter["eat_ass"]:
        $ approval_bonus += 20
    if KittyX.PantsNum() > 6 or KittyX.HoseNum() >= 5:
        $ approval_bonus -= 25
    if KittyX.lust > 95:
        $ approval_bonus += 20
    elif KittyX.lust > 85:
        $ approval_bonus += 15
    if KittyX.lust > 85 and action_context == "auto":
        $ approval_bonus += 10
    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in KittyX.traits:
        $ approval_bonus += (4*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in KittyX.traits:
        $ approval_bonus -= 25
    if KittyX.event_counter["forced"] and not KittyX.Forced:
        $ approval_bonus -= 5*KittyX.event_counter["forced"]

    if Taboo and "no_taboo" in KittyX.daily_history:
        $ approval_bonus -= 10

    if "no_lick ass" in KittyX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_lick ass" in KittyX.recent_history else 0

    $ approval = approval_check(KittyX, 1550, TabM = 4)

    if action_context == "auto":
        if approval:
            $ KittyX.change_face("_surprised")
            $ KittyX.change_stat("obedience", 90, 1)
            $ KittyX.change_stat("inhibition", 80, 3)
            $ KittyX.change_stat("inhibition", 40, 2)
            "As you crouch down and start to lick her asshole, [KittyX.name] startles briefly, but then begins to melt."
            $ KittyX.change_face("_sexy")
            jump Kitty_LA_Prep
        else:
            $ KittyX.change_face("_surprised")
            $ KittyX.change_stat("love", 80, -2)
            $ KittyX.change_stat("obedience", 50, -3)
            ch_k "Um, don't do that. . ."
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if "eat_ass" in KittyX.recent_history:
        $ KittyX.change_face("_sexy", 1)
        ch_k "Mmm, again? Ok."
        jump Kitty_LA_Prep
    elif "eat_ass" in KittyX.daily_history:
        $ KittyX.change_face("_sexy", 1)
        ch_k "Didn't get enough earlier?"


    if approval >= 2:
        if KittyX.Forced:
            $ KittyX.change_face("_sad")
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
            $ KittyX.change_stat("obedience", 90, 2)
            $ KittyX.change_stat("inhibition", 60, 2)
            ch_k "Ok, whatever."
        else:
            $ KittyX.change_face("_sexy", 1)
            $ KittyX.eyes = "_closed"
            $ KittyX.change_stat("love", 90, 1)
            $ KittyX.change_stat("inhibition", 60, 2)
            $ KittyX.change_stat("lust", 200, 3)
            ch_k "Wha. . ."
        $ KittyX.change_stat("obedience", 20, 1)
        $ KittyX.change_stat("obedience", 60, 1)
        $ KittyX.change_stat("inhibition", 80, 2)
        jump Kitty_LA_Prep
    else:

        $ KittyX.change_face("_angry", 1)
        if "no_lick ass" in KittyX.recent_history:
            ch_k "I[KittyX.like]{i}just{/i} told you \"no!\""
        elif Taboo and "no_taboo" in KittyX.daily_history and "no_lick ass" in KittyX.daily_history:
            ch_k "I told you not to touch me like that in public!"
        elif "no_lick ass" in KittyX.daily_history:
            ch_k "[KittyX.Like]take a lesson, [KittyX.player_petname]."
        elif Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "Not here!"
        elif not KittyX.action_counter["eat_ass"]:
            $ KittyX.change_face("_bemused", 1)
            if KittyX.love >= KittyX.obedience and KittyX.love >= KittyX.inhibition:
                ch_k "That's, I don't know. . ."
            elif KittyX.obedience >= KittyX.inhibition:
                ch_k "You don't have to do that."
            else:
                $ KittyX.eyes = "_sexy"
                ch_k "That's kinda gross. . ."
        else:
            $ KittyX.change_face("_bemused")
            ch_k "Not now, [KittyX.player_petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no_lick ass" in KittyX.daily_history:
                $ KittyX.change_face("_bemused")
                ch_k "Yeah, ok, [KittyX.player_petname]."
                return
            "I'm sure I can convince you later. . ." if "no_lick ass" not in KittyX.daily_history:
                $ KittyX.change_face("_sexy")
                ch_k "Anything's possible, [KittyX.player_petname]."
                $ KittyX.change_stat("love", 80, 2)
                $ KittyX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ KittyX.recent_history.append("no_taboo")
                    $ KittyX.daily_history.append("no_taboo")
                $ KittyX.recent_history.append("no_lick ass")
                $ KittyX.daily_history.append("no_lick ass")
                return
            "I think you'd really enjoy it. . .":
                if approval:
                    $ KittyX.change_face("_sexy")
                    $ KittyX.change_stat("obedience", 90, 2)
                    $ KittyX.change_stat("obedience", 50, 2)
                    ch_k "Ok, you're probably right. . ."
                    $ KittyX.change_stat("inhibition", 70, 3)
                    $ KittyX.change_stat("inhibition", 40, 2)
                    jump Kitty_LA_Prep
                else:
                    $ KittyX.change_face("_sexy")
                    ch_k "I really don't think so."
            "[[Start licking anyway]":

                $ approval = approval_check(KittyX, 1100, "OI", TabM = 4)
                if approval > 1 or (approval and KittyX.Forced):
                    $ KittyX.change_face("_sad")
                    $ KittyX.change_stat("love", 70, -5, 1)
                    $ KittyX.change_stat("love", 200, -2)
                    ch_k "Ok, {i}fine{/i}."
                    $ KittyX.change_stat("obedience", 50, 4)
                    $ KittyX.change_stat("inhibition", 80, 1)
                    $ KittyX.change_stat("inhibition", 60, 3)
                    if approval < 2:
                        $ KittyX.Forced = 1
                    jump Kitty_LA_Prep
                else:
                    $ KittyX.change_stat("love", 200, -15)
                    $ KittyX.change_face("_angry", 1)
                    "She shoves your head back."
                    $ KittyX.recent_history.append("_angry")
                    $ KittyX.daily_history.append("_angry")

    if "no_lick ass" in KittyX.daily_history:
        ch_k "How many times do I have to say \"no?\""
        $ KittyX.recent_history.append("_angry")
        $ KittyX.daily_history.append("_angry")
    elif KittyX.Forced:
        $ KittyX.change_face("_angry", 1)
        ch_k "Ew, no way."
        if approval_check(KittyX, 500, "I"):
            $ KittyX.change_stat("lust", 80, 10)
        else:
            $ KittyX.change_stat("lust", 50, 3)
        $ KittyX.change_stat("obedience", 50, -2)
        $ KittyX.recent_history.append("_angry")
        $ KittyX.daily_history.append("_angry")
    elif Taboo:
        $ KittyX.change_face("_angry", 1)
        $ KittyX.recent_history.append("no_taboo")
        $ KittyX.daily_history.append("no_taboo")
        ch_k "This just really isn't the time or place, [KittyX.player_petname]!"
    elif KittyX.action_counter["eat_ass"]:
        $ KittyX.change_face("_sad")
        ch_k "Sorry, no more of that."
    else:
        $ KittyX.change_face("_surprised")
        ch_k "Ew."
        $ KittyX.change_face()
    $ KittyX.recent_history.append("no_lick ass")
    $ KittyX.daily_history.append("no_lick ass")
    $ approval_bonus = 0
    return

label Kitty_LA_Prep:
    if offhand_action == "eat_ass":
        return
    if not KittyX.Forced and action_context != "auto":
        $ approval_bonus = 0
        if KittyX.PantsNum() > 6:
            $ approval_bonus = 15
        call Bottoms_Off (KittyX)
        if "_angry" in KittyX.recent_history:
            return
    $ approval_bonus = 0
    call Kitty_Pussy_Launch ("eat_ass")
    if not KittyX.action_counter["eat_ass"]:
        if KittyX.Forced:
            $ KittyX.change_stat("love", 90, -30)
            $ KittyX.change_stat("obedience", 70, 40)
            $ KittyX.change_stat("inhibition", 80, 80)
        else:
            $ KittyX.change_stat("love", 90, 35)
            $ KittyX.change_stat("obedience", 70, 25)
            $ KittyX.change_stat("inhibition", 80, 55)
    if Taboo:
        $ KittyX.inhibition += int(Taboo/10)
        $ KittyX.lust += int(Taboo/5)
    if action_context:
        $ renpy.pop_call()
        $ action_context = 0

    $ KittyX.upskirt = 1
    if KittyX.PantsNum() == 5:
        $ KittyX.SeenPanties = 1
    if not KittyX.underwear:
        call Kitty_First_Bottomless (1)
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ KittyX.drain_word("no_taboo")
    $ KittyX.drain_word("no_lick ass")

    $ KittyX.recent_history.append("lick") if "lick" not in KittyX.recent_history else KittyX.recent_history
    $ KittyX.recent_history.append("ass") if "ass" not in KittyX.recent_history else KittyX.recent_history
    $ KittyX.recent_history.append("eat_ass")

    $ KittyX.daily_history.append("lick") if "lick" not in KittyX.daily_history else KittyX.recent_history
    $ KittyX.daily_history.append("ass") if "ass" not in KittyX.daily_history else KittyX.recent_history
    $ KittyX.daily_history.append("eat_ass")
    call Kitty_Pussy_Launch ("eat_ass")
label Kitty_LA_Cycle:
    if offhand_action == "kiss":
        $ offhand_action = 0
    while Round > 0:
        call ViewShift (KittyX, KittyX.pose, 0, "eat_ass")
        call shift_focus (KittyX)
        $ KittyX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (KittyX)
                    $ counter += 1
                    $ Round -= 1
                    jump Kitty_LA_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "View":
                    call ViewShift (KittyX, "menu")
                    jump Kitty_LA_Cycle
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
                                    "Switch to fondling.":
                                        $ action_context = "pullback"
                                        call Kitty_LA_After
                                        call Kitty_Fondle_Ass
                                    "I want to stick a finger in.":
                                        $ action_context = "shift"
                                        call Kitty_LA_After
                                        call Kitty_Insert_Ass
                                    "Just stick a finger in [[without asking].":
                                        $ action_context = "auto"
                                        call Kitty_LA_After
                                        call Kitty_Insert_Ass
                                    "I want to stick a dildo in.":
                                        $ action_context = "shift"
                                        call Kitty_LA_After
                                        call Kitty_Dildo_Ass
                                    "Never Mind":
                                        jump Kitty_LA_Cycle
                            else:
                                call Sex_Basic_Dialog (KittyX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Kitty_LA_After
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
                                    jump Kitty_LA_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Kitty_LA_Cycle
                                "Never mind":
                                    jump Kitty_LA_Cycle

                        "Show her feet" if not ShowFeet and (KittyX.pose == "doggy" or KittyX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (KittyX.pose == "doggy" or KittyX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [KittyX.name]":

                            call Girl_Undress (KittyX)
                        "Clean up [KittyX.name] (locked)" if not KittyX.spunk:
                            pass
                        "Clean up [KittyX.name]" if KittyX.spunk:
                            call Girl_Cleanup (KittyX, "ask")
                        "Never mind":
                            jump Kitty_LA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Kitty_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Kitty_LA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Kitty_Pos_Reset
                    $ Line = 0
                    jump Kitty_LA_After


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
                if "_angry" in KittyX.recent_history:
                    call Kitty_Pos_Reset
                    return
                $ KittyX.change_stat("lust", 200, 5)
                if 100 > KittyX.lust >= 70 and KittyX.session_orgasms < 2:
                    $ KittyX.recent_history.append("unsatisfied")
                    $ KittyX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Kitty_LA_After
                $ Line = "came"

            if KittyX.lust >= 100:

                call Girl_Cumming (KittyX)
                if action_context == "shift" or "_angry" in KittyX.recent_history:
                    jump Kitty_LA_After

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
                            jump Kitty_LA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if KittyX.SEXP >= 100 or approval_check(KittyX, 1200, "LO"):
            pass
        elif counter == (5 + KittyX.action_counter["eat_ass"]):
            $ KittyX.brows = "_confused"
            ch_k "What are you even?"
        elif KittyX.lust >= 80:
            pass
        elif counter == (15 + KittyX.action_counter["eat_ass"]) and KittyX.SEXP >= 15 and not approval_check(KittyX, 1500):
            $ KittyX.brows = "_confused"
            menu:
                ch_k "[KittyX.player_petname], this is getting weird, maybe we could try something else."
                "Finish up.":
                    "You let go. . ."
                    jump Kitty_LA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Kitty_LA_After
                "No, this is fun.":
                    if approval_check(KittyX, 1200) or approval_check(KittyX, 500, "O"):
                        $ KittyX.change_stat("love", 200, -5)
                        $ KittyX.change_stat("obedience", 50, 3)
                        $ KittyX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ KittyX.change_face("_angry", 1)
                        call Kitty_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_k "Fun for you maybe, I'm tired of it."
                        $ KittyX.change_stat("love", 50, -3, 1)
                        $ KittyX.change_stat("love", 80, -4, 1)
                        $ KittyX.change_stat("obedience", 30, -1, 1)
                        $ KittyX.change_stat("obedience", 50, -1, 1)
                        $ KittyX.recent_history.append("_angry")
                        $ KittyX.daily_history.append("_angry")
                        jump Kitty_LA_After


        call Escalation (KittyX)

        if Round == 10:
            ch_k "It's[KittyX.like]getting kinda late."
        elif Round == 5:
            ch_k "We should wrap this up."


    $ KittyX.change_face("_bemused", 0)
    $ Line = 0
    ch_k "Time to take a little break, for now."

label Kitty_LA_After:
    if not action_context:
        call Kitty_Pos_Reset

    $ KittyX.change_face("_sexy")

    $ KittyX.action_counter["eat_ass"] += 1
    $ KittyX.remaining_actions -=1
    if KittyX.PantsNum() < 6 or KittyX.upskirt:
        $ KittyX.addiction_rate += 1
        if "addictive" in Player.traits:
            $ KittyX.addiction_rate += 1

    call Partner_Like (KittyX, 2)

    if KittyX.action_counter["eat_ass"] == 1:
        $ KittyX.SEXP += 15
        if not action_context:
            if KittyX.love >= 500 and "unsatisfied" not in KittyX.recent_history:
                ch_k "That was. . . good for you?"
            elif KittyX.obedience <= 500 and Player.focus <= 20:
                $ KittyX.change_face("_perplexed", 1)
                ch_k "Did that work for you?"

    $ approval_bonus = 0


    call checkout
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
