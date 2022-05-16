
label Rogue_Handjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (RogueX)
    if RogueX.action_counter["handjob"] >= 7:
        $ approval_bonus += 10
    elif RogueX.action_counter["handjob"] >= 3:
        $ approval_bonus += 7
    elif RogueX.action_counter["handjob"]:
        $ approval_bonus += 3

    if RogueX.addiction >= 75 and RogueX.event_counter["swallowed"] >=3:
        $ approval_bonus += 15
    if RogueX.addiction >= 75:
        $ approval_bonus += 5

    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in RogueX.Traits:
        $ approval_bonus += (3*Taboo)
    if RogueX in Player.Harem or "sex friend" in RogueX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in RogueX.Traits:
        $ approval_bonus -= 40
    if RogueX.event_counter["forced"] and not RogueX.Forced:
        $ approval_bonus -= 5*RogueX.event_counter["forced"]

    if Taboo and "no_taboo" in RogueX.daily_history:
        $ approval_bonus -= 10

    if "no_handjob" in RogueX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_handjob" in RogueX.recent_history else 0

    $ Approval = ApprovalCheck(RogueX, 1100, TabM = 3)

    if not RogueX.action_counter["handjob"] and "no_handjob" not in RogueX.recent_history:
        $ RogueX.change_face("surprised", 1)
        $ RogueX.mouth = "kiss"
        ch_r "You want me to rub your cock, with my hand?"

    if not RogueX.action_counter["handjob"] and Approval:
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
        elif RogueX.love >= (RogueX.obedience + RogueX.inhibition):
            $ RogueX.change_face("sexy")
            $ RogueX.brows = "sad"
            $ RogueX.mouth = "smile"
            ch_r "Well, I've never really been able to touch people without draining them, this could be an interesting experience. . ."
        elif RogueX.obedience >= RogueX.inhibition:
            $ RogueX.change_face("normal")
            ch_r "If that's what you want, [RogueX.player_petname]. . ."
        elif RogueX.addiction >= 50:
            $ RogueX.change_face("manic", 1)
            ch_r "I think, if I could just touch that. . ."
        else:
            $ RogueX.change_face("sad")
            $ RogueX.mouth = "smile"
            ch_r "Hmm, could be fun. . ."

    elif Approval:
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
            ch_r "That's really what you want?"
        elif not Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "Ok, I guess this is private enough. . ."
        elif "handjob" in RogueX.recent_history:
            $ RogueX.change_face("sexy", 1)
            ch_r "Mmm, again? Let me flex my hand a bit. . ."
            jump Rogue_HJ_Prep
        elif "handjob" in RogueX.daily_history:
            $ RogueX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",   
                "You're going to give me calluses.", 
                "Didn't get enough earlier?",
                "My arm's still a bit sore from earlier.",
                "My arm's still a bit sore from earlier."])
            ch_r "[Line]"
        elif RogueX.action_counter["handjob"] < 3:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.brows = "confused"
            $ RogueX.mouth = "kiss"
            ch_r "So you'd like another handy?"
        else:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                "So you'd like another handy?",                 
                "A little. . . [fist pumping hand gestures]?", 
                "You want me to grease your skids?",
                "A little tender loving care?"])
            ch_r "[Line]"
        $ Line = 0

    if Approval >= 2:
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("obedience", 90, 1)
            $ RogueX.change_stat("inhibition", 60, 1)
            ch_r "Ok, fine."
        elif "no_handjob" in RogueX.daily_history:
            ch_r "I guess if it'll get you off. . ."
        else:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.change_stat("love", 90, 1)
            $ RogueX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, put'im here.",                 
                "Well. . . ok.",                 
                "I suppose, drop trou.", 
                "I guess I could. . . whip it out.",
                "Fine. . . [She gestures for you to come over].",
                "Heh, ok, ok."])
            ch_r "[Line]"
            $ Line = 0
        $ RogueX.change_stat("obedience", 20, 1)
        $ RogueX.change_stat("obedience", 60, 1)
        $ RogueX.change_stat("inhibition", 70, 2)
        jump Rogue_HJ_Prep
    else:

        $ RogueX.change_face("angry")
        if "no_handjob" in RogueX.recent_history:
            ch_r "I {i}just{/i} told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history and "no_handjob" in RogueX.daily_history:
            ch_r "I already told you that I wouldn't jerk you off in public!"
        elif "no_handjob" in RogueX.daily_history:
            ch_r "I already told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "I already told you this is too public!"
        elif not RogueX.action_counter["handjob"]:
            $ RogueX.change_face("bemused")
            ch_r "I don't really want to touch it, [RogueX.player_petname]. . ."
        else:
            $ RogueX.change_face("bemused")
            ch_r "Not, right now [RogueX.player_petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_handjob" in RogueX.daily_history:
                $ RogueX.change_face("bemused")
                ch_r "Fine."
                return
            "Maybe later?" if "no_handjob" not in RogueX.daily_history:
                $ RogueX.change_face("sexy")
                ch_r "I'll give it some thought, [RogueX.player_petname]."
                $ RogueX.change_stat("love", 80, 2)
                $ RogueX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ RogueX.recent_history.append("no_taboo")
                    $ RogueX.daily_history.append("no_taboo")
                $ RogueX.recent_history.append("no_handjob")
                $ RogueX.daily_history.append("no_handjob")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ RogueX.change_face("sexy")
                    $ RogueX.change_stat("obedience", 90, 2)
                    $ RogueX.change_stat("obedience", 50, 2)
                    $ RogueX.change_stat("inhibition", 70, 3)
                    $ RogueX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Sure, put'im here.",                 
                        "No Problem.",                 
                        "Sure. Drop trou.", 
                        "I suppose, whip it out.",
                        "Ok, [She gestures for you to come over].",
                        "Heh, ok."])
                    ch_r "[Line]"
                    $ Line = 0
                    jump Rogue_HJ_Prep
                else:
                    pass
            "Come on, get to work.":

                $ Approval = ApprovalCheck(RogueX, 350, "OI", TabM = 3)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.change_face("sad")
                    $ RogueX.change_stat("love", 70, -5, 1)
                    $ RogueX.change_stat("love", 200, -2)
                    ch_r "Ok, fine, whip it out."
                    $ RogueX.change_stat("obedience", 50, 4)
                    $ RogueX.change_stat("inhibition", 80, 1)
                    $ RogueX.change_stat("inhibition", 60, 3)
                    $ RogueX.Forced = 1
                    jump Rogue_HJ_Prep
                else:
                    $ RogueX.change_stat("love", 200, -15)
                    $ RogueX.recent_history.append("angry")
                    $ RogueX.daily_history.append("angry")


    $ RogueX.ArmPose = 1
    if "no_handjob" in RogueX.daily_history:
        $ RogueX.change_face("angry", 1)
        ch_r "I just don't want to, [RogueX.player_petname]."
        $ RogueX.recent_history.append("angry")
        $ RogueX.daily_history.append("angry")
    elif RogueX.Forced:
        $ RogueX.change_face("angry", 1)
        ch_r "I'm not that kind of girl!"
        $ RogueX.change_stat("lust", 200, 5)
        if RogueX.love > 300:
            $ RogueX.change_stat("love", 70, -2)
        $ RogueX.change_stat("obedience", 50, -2)
        $ RogueX.recent_history.append("angry")
        $ RogueX.daily_history.append("angry")
    elif Taboo:
        $ RogueX.change_face("angry", 1)
        $ RogueX.daily_history.append("no_taboo")
        ch_r "I really don't think this is the right place for that!"
        $ RogueX.change_stat("lust", 200, 5)
        $ RogueX.change_stat("obedience", 50, -3)
    elif RogueX.action_counter["handjob"]:
        $ RogueX.change_face("sad")
        ch_r "I think you can manage it yourself this time. . ."
    else:
        $ RogueX.change_face("normal", 1)
        ch_r "I'd really rather not."
    $ RogueX.recent_history.append("no_handjob")
    $ RogueX.daily_history.append("no_handjob")
    $ approval_bonus = 0
    return


label Rogue_HJ_Prep:
    if offhand_action == "handjob":
        return

    if Taboo:
        $ RogueX.inhibition += int(Taboo/10)
        $ RogueX.lust += int(Taboo/5)

    $ RogueX.change_face("sexy")
    if RogueX.Forced:
        $ RogueX.change_face("sad")
    elif not RogueX.action_counter["handjob"]:
        $ RogueX.brows = "confused"
        $ RogueX.eyes = "sexy"
        $ RogueX.mouth = "smile"

    call Seen_First_Peen (RogueX, Partner, React=action_context)
    call Rogue_HJ_Launch ("L")

    if action_context == RogueX:

        $ action_context = 0
        if offhand_action == "jackin":
            "[RogueX.name] brushes your hand aside and starts stroking your cock."
        else:
            "[RogueX.name] gives you a mischevious smile, and starts to fondle your cock."
        menu:
            "What do you do?"
            "Nothing.":
                $ RogueX.change_stat("inhibition", 70, 3)
                $ RogueX.change_stat("inhibition", 30, 2)
                "[RogueX.name] continues her actions."
            "Praise her.":
                $ RogueX.change_face("sexy", 1)
                $ RogueX.change_stat("inhibition", 70, 3)
                ch_p "Oooh, that's good, [RogueX.petname]."
                $ RogueX.nameCheck()
                "[RogueX.name] continues her actions."
                $ RogueX.change_stat("love", 80, 1)
                $ RogueX.change_stat("obedience", 90, 1)
                $ RogueX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ RogueX.change_face("surprised")
                $ RogueX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that for now, [RogueX.petname]."
                $ RogueX.nameCheck()
                "[RogueX.name] puts it down."
                $ RogueX.change_stat("obedience", 90, 1)
                $ RogueX.change_stat("obedience", 50, 1)
                $ RogueX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ RogueX.AddWord(1,"refused","refused")
                return

    if not RogueX.action_counter["handjob"]:
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -20)
            $ RogueX.change_stat("obedience", 70, 25)
            $ RogueX.change_stat("inhibition", 80, 30)
        else:
            $ RogueX.change_stat("love", 90, 5)
            $ RogueX.change_stat("obedience", 70, 20)
            $ RogueX.change_stat("inhibition", 80, 20)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ RogueX.DrainWord("no_taboo")
    $ RogueX.DrainWord("no_handjob")
    $ RogueX.recent_history.append("handjob")
    $ RogueX.daily_history.append("handjob")

label Rogue_HJ_Cycle:
    while Round > 0:
        call shift_focus (RogueX)
        call Rogue_HJ_Launch
        $ RogueX.lust_face()

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
                            if RogueX.remaining_actions and multi_action:
                                $ offhand_action = "fondle_breasts"
                                "You start to fondle her breasts."
                                $ RogueX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (RogueX, "tired")
                        "Shift primary action":

                            if RogueX.remaining_actions and multi_action:
                                menu:
                                    "How about a blowjob?":
                                        if RogueX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Rogue_HJ_After
                                            call Rogue_Blowjob
                                        else:
                                            call Sex_Basic_Dialog (RogueX, "tired")
                                    "How about a titjob?":

                                        if RogueX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Rogue_HJ_After
                                            call Rogue_Titjob
                                        else:
                                            call Sex_Basic_Dialog (RogueX, "tired")
                                    "Never Mind":
                                        jump Rogue_HJ_Cycle
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
                                    jump Rogue_HJ_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Rogue_HJ_Cycle
                                "Never mind":
                                    jump Rogue_HJ_Cycle
                        "Undress [RogueX.name]":
                            call Girl_Undress (RogueX)
                        "Clean up [RogueX.name] (locked)" if not RogueX.Spunk:
                            pass
                        "Clean up [RogueX.name]" if RogueX.Spunk:
                            call Girl_Cleanup (RogueX, "ask")
                        "Never mind":
                            jump Rogue_HJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Rogue_HJ_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Rogue_HJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Rogue_HJ_Reset
                    $ Line = 0
                    jump Rogue_HJ_After


        call shift_focus (RogueX)
        call Sex_Dialog (RogueX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or RogueX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (RogueX)
                if "angry" in RogueX.recent_history:
                    call Rogue_HJ_Reset
                    return
                $ RogueX.change_stat("lust", 200, 5)
                if 100 > RogueX.lust >= 70 and RogueX.session_orgasms < 2 and RogueX.SEXP >= 20:
                    $ RogueX.recent_history.append("unsatisfied")
                    $ RogueX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Rogue_HJ_After
                $ Line = "came"

            if RogueX.lust >= 100:

                call Girl_Cumming (RogueX)
                if action_context == "shift" or "angry" in RogueX.recent_history:
                    jump Rogue_HJ_After

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
                            jump Rogue_HJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif counter == (5 + RogueX.action_counter["handjob"]):
            $ RogueX.brows = "confused"
            ch_r "Are you getting close here? I'm getting a little sore."
        elif counter == (10 + RogueX.action_counter["handjob"]):
            $ RogueX.brows = "angry"
            menu:
                ch_r "I'm getting rug-burn here [RogueX.player_petname]. Can we do something else?"
                "How about a BJ?" if RogueX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Rogue_HJ_After
                    call Rogue_Blowjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    jump Rogue_HJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Rogue_HJ_Reset
                    $ action_context = "shift"
                    jump Rogue_HJ_After
                "No, get back down there.":
                    if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):
                        $ RogueX.change_stat("love", 200, -5)
                        $ RogueX.change_stat("obedience", 50, 3)
                        $ RogueX.change_stat("obedience", 80, 2)
                        "She grumbles but gets back to work."
                    else:
                        $ RogueX.change_face("angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        ch_r "Well if that's your attitude you can handle your own business."
                        $ RogueX.change_stat("love", 50, -3, 1)
                        $ RogueX.change_stat("love", 80, -4, 1)
                        $ RogueX.change_stat("obedience", 30, -1, 1)
                        $ RogueX.change_stat("obedience", 50, -1, 1)
                        $ RogueX.recent_history.append("angry")
                        $ RogueX.daily_history.append("angry")
                        jump Rogue_HJ_After


        call Escalation (RogueX)

        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."


    $ RogueX.change_face("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.player_petname], that's enough of that for now."

label Rogue_HJ_After:
    $ RogueX.change_face("sexy")

    $ RogueX.action_counter["handjob"] += 1
    $ RogueX.remaining_actions -=1
    $ RogueX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ RogueX.addiction_rate += 1
    $ RogueX.change_stat("lust", 90, 5)

    call Partner_Like (RogueX, 2)

    if "Rogue Handi-Queen" in Achievements:
        pass
    elif RogueX.action_counter["handjob"] >= 10:
        $ RogueX.change_face("smile", 1)
        ch_r "I guess you can call me \"Handi-Queen.\""
        $ Achievements.append("Rogue Handi-Queen")
        $ RogueX.SEXP += 5
    elif RogueX.action_counter["handjob"] == 1:
        $ RogueX.SEXP += 10
        if RogueX.love >= 500:
            $ RogueX.mouth = "smile"
            ch_r "Well, it's really nice to finally be able to reach out and touch someone."
        elif Player.focus <= 20:
            $ RogueX.mouth = "sad"
            ch_r "Well, I hope that got your rocks off."
    elif RogueX.action_counter["handjob"] == 5:
        ch_r "I think I've got this well in hand."

    $ approval_bonus = 0
    if action_context == "shift":
        ch_r "Mmm, so what else did you have in mind?"
    else:
        call Rogue_HJ_Reset
    call checkout
    return





label Rogue_Titjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (RogueX)
    if RogueX.action_counter["titjob"] >= 7:
        $ approval_bonus += 10
    elif RogueX.action_counter["titjob"] >= 3:
        $ approval_bonus += 7
    elif RogueX.action_counter["titjob"]:
        $ approval_bonus += 5

    if RogueX.addiction >= 75 and RogueX.event_counter["swallowed"] >=3:
        $ approval_bonus += 15
    elif RogueX.addiction >= 75:
        $ approval_bonus += 5

    if RogueX.SeenChest and ApprovalCheck(RogueX, 500):
        $ approval_bonus += 10
    if not RogueX.bra and not RogueX.top:
        $ approval_bonus += 10
    if RogueX.lust > 75:
        $ approval_bonus += 10
    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in RogueX.Traits:
        $ approval_bonus += (5*Taboo)
    if RogueX in Player.Harem or "sex friend" in RogueX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in RogueX.Traits:
        $ approval_bonus -= 30
    if RogueX.event_counter["forced"] and not RogueX.Forced:
        $ approval_bonus -= 5*RogueX.event_counter["forced"]

    if Taboo and "no_taboo" in RogueX.daily_history:
        $ approval_bonus -= 10

    if "no_titjob" in RogueX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_titjob" in RogueX.recent_history else 0

    $ Approval = ApprovalCheck(RogueX, 1200, TabM = 5)

    if not RogueX.action_counter["titjob"] and "no_titjob" not in RogueX.recent_history:
        $ RogueX.change_face("surprised", 1)
        $ RogueX.mouth = "kiss"
        ch_r "You want me to rub your cock with my breasts?"
        if RogueX.action_counter["blowjob"]:
            $ RogueX.mouth = "smile"
            ch_r "My mouth wasn't enough?"
        elif RogueX.action_counter["handjob"]:
            $ RogueX.mouth = "smile"
            ch_r "My hand wasn't enough?"

    if not RogueX.action_counter["titjob"] and Approval:
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
        elif RogueX.love >= (RogueX.obedience + RogueX.inhibition):
            $ RogueX.change_face("sexy")
            $ RogueX.brows = "sad"
            $ RogueX.mouth = "smile"
            ch_r "Huh, well that's certainly one way to get off."
        elif RogueX.obedience >= RogueX.inhibition:
            $ RogueX.change_face("normal")
            ch_r "If that's what you want. . ."
        elif RogueX.addiction >= 50:
            $ RogueX.change_face("manic", 1)
            ch_r "Hmmmm. . . ."
        else:
            $ RogueX.change_face("sad")
            $ RogueX.mouth = "smile"
            ch_r "Heh, might be fun."
    elif Approval:
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
            ch_r "This isn't going to become a habit, will it?"
        elif not Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "Ok, I guess this is private enough. . ."
        elif "titjob" in RogueX.recent_history:
            $ RogueX.change_face("sexy", 1)
            ch_r "Mmm, again? Ok, let me get the girls ready."
            jump Rogue_TJ_Prep
        elif "titjob" in RogueX.daily_history:
            $ RogueX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",   
                "You're going to give me calluses.", 
                "Didn't get enough earlier?",
                "My tits are still a bit sore from earlier."])
            ch_r "[Line]"
        elif RogueX.action_counter["titjob"] < 3:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.brows = "confused"
            $ RogueX.mouth = "kiss"
            ch_r "So you'd like another titjob?"
        else:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action [jiggles her tits]?",                 
                "So you'd like another titjob?",                 
                "A little. . . bounce?", 
                "You want me to pillow your crank?",
                "A little soft embrace?"])
            ch_r "[Line]"
        $ Line = 0

    if Approval >= 2:
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("obedience", 90, 1)
            $ RogueX.change_stat("inhibition", 60, 1)
            ch_r "Well, there are worst ways to get you off. . ."
        elif "no_titjob" in RogueX.daily_history:
            ch_r "Hmm, I suppose. . ."
        else:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.change_stat("love", 90, 1)
            $ RogueX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, put it here.",                 
                "Well. . . ok.",                 
                "Yum.", 
                "Sure, whip it out.",
                "Fine. . . [She drools a bit into her cleavage].",
                "Heh, ok, alright."])
            ch_r "[Line]"
            $ Line = 0
        $ RogueX.change_stat("obedience", 20, 1)
        $ RogueX.change_stat("obedience", 70, 1)
        $ RogueX.change_stat("inhibition", 80, 2)
        jump Rogue_TJ_Prep
    else:

        $ RogueX.change_face("angry")
        if "no_titjob" in RogueX.recent_history:
            ch_r "I {i}just{/i} told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history and "no_titjob" in RogueX.daily_history:
            ch_r "This is just way too exposed!"
        elif "no_titjob" in RogueX.daily_history:
            ch_r "I already told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "This is just way too exposed!"
        elif not RogueX.action_counter["titjob"]:
            $ RogueX.change_face("bemused")
            ch_r "I'm not really up for that, [RogueX.player_petname]. . ."
        else:
            $ RogueX.change_face("bemused")
            ch_r "Not, right now [RogueX.player_petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_titjob" in RogueX.daily_history:
                $ RogueX.change_face("bemused")
                ch_r "Yeah, ok, [RogueX.player_petname]."
                return
            "Maybe later?" if "no_titjob" not in RogueX.daily_history:
                $ RogueX.change_face("sexy")
                ch_r "We'll have to see."
                $ RogueX.change_stat("love", 80, 2)
                $ RogueX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ RogueX.recent_history.append("no_taboo")
                    $ RogueX.daily_history.append("no_taboo")
                $ RogueX.recent_history.append("no_titjob")
                $ RogueX.daily_history.append("no_titjob")
                return
            "I think this could be fun for both of us. . .":
                if Approval:
                    $ RogueX.change_face("sexy")
                    $ RogueX.change_stat("obedience", 80, 2)
                    $ RogueX.change_stat("obedience", 40, 2)
                    $ RogueX.change_stat("inhibition", 70, 3)
                    $ RogueX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Well, ok, put it here.",                 
                        "Well. . . ok.",                 
                        "I guess.", 
                        "I guess, whip it out.",
                        "Fine. . . [She drools a bit into her cleavage].",
                        "Heh, ok, alright."])
                    ch_r "[Line]"
                    $ Line = 0
                    jump Rogue_TJ_Prep
                else:
                    $ Approval = ApprovalCheck(RogueX, 1100, TabM = 3)
                    if Approval >= 2:
                        $ RogueX.change_stat("inhibition", 80, 1)
                        $ RogueX.change_stat("inhibition", 60, 3)
                        $ RogueX.change_face("confused", 1)
                        if RogueX.action_counter["blowjob"]:
                            ch_r "I could just. . . blow you instead?"
                        else:
                            ch_r "I could maybe. . . you know, [[she pushes her tongue against the side of her cheek]?"
                        menu:
                            extend ""
                            "Ok, get down there.":
                                $ RogueX.change_stat("love", 80, 2)
                                $ RogueX.change_stat("inhibition", 60, 1)
                                $ RogueX.change_stat("obedience", 50, 1)
                                jump Rogue_BJ_Prep
                            "Nah, it's all about dem titties.":
                                $ Line = "no_BJ"
                    if Approval:
                        $ RogueX.change_stat("inhibition", 80, 1)
                        $ RogueX.change_stat("inhibition", 60, 3)
                        $ RogueX.change_face("confused", 1)
                        if RogueX.action_counter["handjob"]:
                            ch_r "Maybe you'd settle for a handy?"
                        else:
                            ch_r "I could maybe. . . [[she makes a jerking motion with her hand]?"
                        menu:
                            extend ""
                            "Sure, that's fine.":
                                $ RogueX.change_stat("love", 80, 2)
                                $ RogueX.change_stat("inhibition", 60, 1)
                                $ RogueX.change_stat("obedience", 50, 1)
                                jump Rogue_HJ_Prep
                            "Seriously, titties." if Line == "no_BJ":
                                $ Line = 0
                            "Nah, it's all about dem titties." if Line != "no_BJ":
                                pass
                    $ RogueX.change_stat("love", 200, -2)
                    ch_r "Ok, whatever."
                    $ RogueX.change_stat("obedience", 70, 2)
            "Come on, let me fuck those titties, [RogueX.petname]":


                $ RogueX.nameCheck()
                $ Approval = ApprovalCheck(RogueX, 700, "OI", TabM = 4)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.change_face("sad")
                    $ RogueX.change_stat("love", 70, -5, 1)
                    $ RogueX.change_stat("love", 200, -2)
                    ch_r "Ok, fine, whip it out."
                    $ RogueX.change_stat("obedience", 50, 4)
                    $ RogueX.change_stat("inhibition", 80, 1)
                    $ RogueX.change_stat("inhibition", 60, 3)
                    $ RogueX.Forced = 1
                    jump Rogue_TJ_Prep
                else:
                    $ RogueX.change_stat("love", 200, -15)
                    $ RogueX.recent_history.append("angry")
                    $ RogueX.daily_history.append("angry")


    if "no_titjob" in RogueX.daily_history:
        $ RogueX.change_face("angry", 1)
        ch_r "Look, I already told you no thanks, [RogueX.player_petname]."
        $ RogueX.recent_history.append("angry")
        $ RogueX.daily_history.append("angry")
    elif RogueX.Forced:
        $ RogueX.change_face("angry", 1)
        ch_r "I'm not that kind of girl."
        $ RogueX.change_stat("lust", 200, 5)
        if RogueX.love > 300:
            $ RogueX.change_stat("love", 70, -2)
        $ RogueX.change_stat("obedience", 50, -2)
        $ RogueX.recent_history.append("angry")
        $ RogueX.daily_history.append("angry")
    elif Taboo:
        $ RogueX.change_face("angry", 1)
        $ RogueX.daily_history.append("no_taboo")
        ch_r "You really expect me to do that here? You realize how. . . exposed that would be?"
        $ RogueX.change_stat("lust", 200, 5)
        $ RogueX.change_stat("obedience", 50, -3)
    elif RogueX.action_counter["titjob"]:
        $ RogueX.change_face("sad")
        ch_r "I think I'll let you know when I want you touching these again."
    else:
        $ RogueX.change_face("normal", 1)
        ch_r "How about let's not, [RogueX.player_petname]."
    $ RogueX.recent_history.append("no_titjob")
    $ RogueX.daily_history.append("no_titjob")
    $ approval_bonus = 0
    return

label Rogue_TJ_Prep:

    if Taboo:
        $ RogueX.inhibition += int(Taboo/10)
        $ RogueX.lust += int(Taboo/5)


    $ RogueX.change_face("sexy")
    if RogueX.Forced:
        $ RogueX.change_face("sad")
    elif not RogueX.action_counter["titjob"]:
        $ RogueX.brows = "confused"
        $ RogueX.eyes = "sexy"
        $ RogueX.mouth = "smile"

    call Seen_First_Peen (RogueX, Partner, React=action_context)
    call Rogue_TJ_Launch ("L")

    if action_context == RogueX:

        $ action_context = 0
        "[RogueX.name] slides down and sandwiches your dick between her tits."
        menu:
            "What do you do?"
            "Nothing.":
                $ RogueX.change_stat("inhibition", 80, 3)
                $ RogueX.change_stat("inhibition", 40, 2)
                "[RogueX.name] starts to slide them up and down."
            "Praise her.":
                $ RogueX.change_face("sexy", 1)
                $ RogueX.change_stat("inhibition", 80, 3)
                ch_p "Oh, that sounds like a good idea, [RogueX.petname]."
                $ RogueX.nameCheck()
                "[RogueX.name] continues her actions."
                $ RogueX.change_stat("love", 85, 1)
                $ RogueX.change_stat("obedience", 90, 1)
                $ RogueX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ RogueX.change_face("confused")
                $ RogueX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that for now, [RogueX.petname]."
                $ RogueX.nameCheck()
                "[RogueX.name] lets it drop out from between her breasts."
                $ RogueX.change_stat("obedience", 90, 1)
                $ RogueX.change_stat("obedience", 50, 3)
                $ Player.recent_history.append("nope")
                $ RogueX.AddWord(1,"refused","refused")
                return

    if not RogueX.action_counter["titjob"]:
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -25)
            $ RogueX.change_stat("obedience", 70, 30)
            $ RogueX.change_stat("inhibition", 80, 35)
        else:
            $ RogueX.change_stat("love", 90, 5)
            $ RogueX.change_stat("obedience", 70, 25)
            $ RogueX.change_stat("inhibition", 80, 30)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ RogueX.DrainWord("no_taboo")
    $ RogueX.DrainWord("no_titjob")
    $ RogueX.recent_history.append("titjob")
    $ RogueX.daily_history.append("titjob")


label Rogue_TJ_Cycle:
    while Round > 0:
        call shift_focus (RogueX)
        call Rogue_TJ_Launch
        $ RogueX.lust_face()

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
                            if RogueX.remaining_actions and multi_action:
                                $ offhand_action = "fondle_breasts"
                                "You start to fondle her breasts."
                                $ RogueX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (RogueX, "tired")
                        "Shift primary action":

                            if RogueX.remaining_actions and multi_action:
                                menu:
                                    "How about a blowjob?":
                                        if RogueX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Rogue_TJ_After
                                            call Rogue_Blowjob
                                        else:
                                            call Sex_Basic_Dialog (RogueX, "tired")
                                    "How about a handy?":

                                        if RogueX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Rogue_TJ_After
                                            call Rogue_Handjob
                                        else:
                                            call Sex_Basic_Dialog (RogueX, "tired")
                                    "Never Mind":
                                        jump Rogue_TJ_Cycle
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
                                    jump Rogue_TJ_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Rogue_TJ_Cycle
                                "Never mind":
                                    jump Rogue_TJ_Cycle
                        "Undress [RogueX.name]":
                            call Girl_Undress (RogueX)
                        "Clean up [RogueX.name] (locked)" if not RogueX.Spunk:
                            pass
                        "Clean up [RogueX.name]" if RogueX.Spunk:
                            call Girl_Cleanup (RogueX, "ask")
                        "Never mind":
                            jump Rogue_TJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Rogue_TJ_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Rogue_TJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Rogue_TJ_Reset
                    $ Line = 0
                    jump Rogue_TJ_After


        call shift_focus (RogueX)
        call Sex_Dialog (RogueX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or RogueX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (RogueX)
                if "angry" in RogueX.recent_history:
                    call Rogue_TJ_Reset
                    return
                $ RogueX.change_stat("lust", 200, 5)
                if 100 > RogueX.lust >= 70 and RogueX.session_orgasms < 2 and RogueX.SEXP >= 20:
                    $ RogueX.recent_history.append("unsatisfied")
                    $ RogueX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Rogue_TJ_After
                $ Line = "came"

            if RogueX.lust >= 100:

                call Girl_Cumming (RogueX)
                if action_context == "shift" or "angry" in RogueX.recent_history:
                    jump Rogue_TJ_After

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
                            jump Rogue_TJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif counter == (5 + RogueX.action_counter["titjob"]):
            $ RogueX.brows = "confused"
            ch_r "Are you getting close here? I'm getting a little sore."
        elif counter == (10 + RogueX.action_counter["titjob"]):
            $ RogueX.brows = "angry"
            menu:
                ch_r "I'm getting rug-burn here [RogueX.player_petname]. Can we do something else?"
                "How about a BJ?" if RogueX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Rogue_TJ_After
                    call Rogue_Blowjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    jump Rogue_TJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Rogue_TJ_Reset
                    $ action_context = "shift"
                    jump Rogue_TJ_After
                "No, get back down there.":
                    if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):
                        $ RogueX.change_stat("love", 200, -5)
                        $ RogueX.change_stat("obedience", 50, 3)
                        $ RogueX.change_stat("obedience", 80, 2)
                        "She grumbles but gets back to work."
                    else:
                        $ RogueX.change_face("angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        ch_r "Well if that's your attitude you can handle your own business."
                        $ RogueX.change_stat("love", 50, -3, 1)
                        $ RogueX.change_stat("love", 80, -4, 1)
                        $ RogueX.change_stat("obedience", 30, -1, 1)
                        $ RogueX.change_stat("obedience", 50, -1, 1)
                        $ RogueX.recent_history.append("angry")
                        $ RogueX.daily_history.append("angry")
                        jump Rogue_TJ_After


        call Escalation (RogueX)

        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."


    $ RogueX.change_face("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.player_petname], that's enough of that for now."

label Rogue_TJ_After:
    $ RogueX.change_face("sexy")

    $ RogueX.action_counter["titjob"] += 1
    $ RogueX.remaining_actions -=1
    $ RogueX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ RogueX.addiction_rate += 1

    call Partner_Like (RogueX, 3)

    if RogueX.action_counter["titjob"] > 5:
        pass
    elif RogueX.action_counter["titjob"] == 1:
        $ RogueX.SEXP += 12
        if RogueX.love >= 500:
            $ RogueX.mouth = "smile"
            ch_r "Well, that was certainly interesting."
        elif Player.focus <= 20:
            $ RogueX.mouth = "sad"
            ch_r "Well, I hope that was enough for you."
    elif RogueX.action_counter["titjob"] == 5:
        ch_r "I think I've got the goods for this."


    $ approval_bonus = 0
    if action_context == "shift":
        ch_r "Mmm, so what else did you have in mind?"
    else:
        call Rogue_TJ_Reset
    call checkout
    return





label Rogue_Blowjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (RogueX)
    if RogueX.action_counter["blowjob"] >= 7:
        $ approval_bonus += 15
    elif RogueX.action_counter["blowjob"] >= 3:
        $ approval_bonus += 10
    elif RogueX.action_counter["blowjob"]:
        $ approval_bonus += 7

    if RogueX.addiction >= 75 and RogueX.event_counter["swallowed"] >=3:
        $ approval_bonus += 25
    elif RogueX.addiction >= 75:
        $ approval_bonus += 15

    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in RogueX.Traits:
        $ approval_bonus += (4*Taboo)
    if RogueX in Player.Harem or "sex friend" in RogueX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in RogueX.Traits:
        $ approval_bonus -= 40
    if RogueX.event_counter["forced"] and not RogueX.Forced:
        $ approval_bonus -= 5*RogueX.event_counter["forced"]

    if Taboo and "no_taboo" in RogueX.daily_history:
        $ approval_bonus -= 10

    if "no_blowjob" in RogueX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_blowjob" in RogueX.recent_history else 0

    $ Approval = ApprovalCheck(RogueX, 1300, TabM = 4)

    if not RogueX.action_counter["blowjob"] and "no_blowjob" not in RogueX.recent_history:
        $ RogueX.change_face("surprised", 1)
        $ RogueX.mouth = "kiss"
        ch_r "You want me to put your dick. . . in my mouth?"
        if RogueX.action_counter["handjob"]:
            $ RogueX.mouth = "smile"
            ch_r "My hand wasn't enough?"

    if not RogueX.action_counter["blowjob"] and Approval:
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
        elif RogueX.love >= (RogueX.obedience + RogueX.inhibition):
            $ RogueX.change_face("sexy")
            $ RogueX.brows = "sad"
            $ RogueX.mouth = "smile"
            ch_r "I've never really put something like that in my mouth. . . might be interesting."
        elif RogueX.obedience >= RogueX.inhibition:
            $ RogueX.change_face("normal")
            ch_r "I suppose, if that's what you want. . ."
        elif RogueX.addiction >= 50:
            $ RogueX.change_face("manic", 1)
            ch_r "I think. . . for some reason I really do want that in my mouth. . ."
        else:
            $ RogueX.change_face("sad")
            $ RogueX.mouth = "smile"
            ch_r "I guess. . ."
    elif Approval:
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
            ch_r "You want me to do that again?"
        elif not Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "Ok, I guess this is private enough. . ."
        elif "blowjob" in RogueX.recent_history:
            $ RogueX.change_face("sexy", 1)
            ch_r "Mmm, again? [[stretches her jaw]"
            jump Rogue_BJ_Prep
        elif "blowjob" in RogueX.daily_history:
            $ RogueX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",   
                "You're going to give me lockjaw.", 
                "Let me get some saliva going.",
                "Didn't get enough earlier?",
                "My jaw's still a bit sore from earlier.",
                "My jaw's still a bit sore from earlier."])
            ch_r "[Line]"
        elif RogueX.action_counter["blowjob"] < 3:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.brows = "confused"
            $ RogueX.mouth = "kiss"
            ch_r "So you'd like another blowjob?"
        else:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action [mimes blowing]?",                 
                "So you'd like another blowjob?",                 
                "A little. . . lick?", 
                "You want me to wet your willy?",
                "A little tender loving care?"])
            ch_r "[Line]"
        $ Line = 0

    if Approval >= 2:
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("obedience", 90, 1)
            $ RogueX.change_stat("inhibition", 60, 1)
            ch_r "Whatever."
        elif "no_blowjob" in RogueX.daily_history:
            ch_r "Oh, I suppose it isn't so bad. . ."
        else:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.change_stat("love", 90, 1)
            $ RogueX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, ahhhhhh.",                 
                "Well. . . ok.",                 
                "Yum.", 
                "Sure, whip it out.",
                "Fine. . . [She licks her lips].",
                "Heh, ok, alright."])
            ch_r "[Line]"
            $ Line = 0
        $ RogueX.change_stat("obedience", 20, 1)
        $ RogueX.change_stat("obedience", 70, 1)
        $ RogueX.change_stat("inhibition", 80, 2)
        jump Rogue_BJ_Prep
    else:

        $ RogueX.change_face("angry")
        if "no_blowjob" in RogueX.recent_history:
            ch_r "I {i}just{/i} told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history and "no_blowjob" in RogueX.daily_history:
            ch_r "I already told you that I wouldn't suck you off in public!"
        elif "no_blowjob" in RogueX.daily_history:
            ch_r "I already told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "I already told you this is too public!"
        elif not RogueX.action_counter["blowjob"]:
            $ RogueX.change_face("bemused")
            ch_r "I don't think I'd like the taste, [RogueX.player_petname]. . ."
        else:
            $ RogueX.change_face("bemused")
            ch_r "Not, right now [RogueX.player_petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_blowjob" in RogueX.daily_history:
                $ RogueX.change_face("bemused")
                ch_r "Yeah, ok, [RogueX.player_petname]."
                return
            "Maybe later?" if "no_blowjob" not in RogueX.daily_history:
                $ RogueX.change_face("sexy")
                ch_r "I might get hungry, [RogueX.player_petname]."
                $ RogueX.change_stat("love", 80, 2)
                $ RogueX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ RogueX.recent_history.append("no_taboo")
                    $ RogueX.daily_history.append("no_taboo")
                $ RogueX.recent_history.append("no_blowjob")
                $ RogueX.daily_history.append("no_blowjob")
                return
            "Come on, please?":
                if Approval:
                    $ RogueX.change_face("sexy")
                    $ RogueX.change_stat("obedience", 90, 2)
                    $ RogueX.change_stat("obedience", 50, 2)
                    $ RogueX.change_stat("inhibition", 70, 3)
                    $ RogueX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Well, sure, ahhhhhh.",                 
                        "Well. . . ok.",                 
                        "I guess a taste couldn't hurt.", 
                        "I guess I could. . . whip it out.",
                        "Fine. . . [She licks her lips].",
                        "Heh, ok, alright."])
                    ch_r "[Line]"
                    $ Line = 0
                    jump Rogue_BJ_Prep
                else:
                    if ApprovalCheck(RogueX, 1100, TabM = 3):
                        $ RogueX.change_stat("inhibition", 80, 1)
                        $ RogueX.change_stat("inhibition", 60, 3)
                        $ RogueX.change_face("confused", 1)
                        if RogueX.action_counter["handjob"]:
                            ch_r "Maybe you'd settle for a handy?"
                        else:
                            ch_r "I could maybe. . . [[she makes a jerking motion with her hand]?"
                        menu:
                            ch_r "What do you say?"
                            "Sure, that's fine.":
                                $ RogueX.change_stat("love", 80, 2)
                                $ RogueX.change_stat("inhibition", 60, 1)
                                $ RogueX.change_stat("obedience", 50, 1)
                                jump Rogue_HJ_Prep
                            "Nah, if it's not a BJ, forget it.":
                                $ RogueX.change_stat("love", 200, -2)
                                ch_r "Ok, whatever."
                                $ RogueX.change_stat("obedience", 70, 2)
            "Suck it, [RogueX.petname]":


                $ RogueX.nameCheck()
                $ Approval = ApprovalCheck(RogueX, 750, "OI", TabM = 3)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.change_face("sad")
                    $ RogueX.change_stat("love", 70, -5, 1)
                    $ RogueX.change_stat("love", 200, -2)
                    ch_r "Ok, fine, whip it out."
                    $ RogueX.change_stat("obedience", 50, 4)
                    $ RogueX.change_stat("inhibition", 80, 1)
                    $ RogueX.change_stat("inhibition", 60, 3)
                    $ RogueX.Forced = 1
                    jump Rogue_BJ_Prep
                else:
                    $ RogueX.change_stat("love", 200, -15)
                    $ RogueX.recent_history.append("angry")
                    $ RogueX.daily_history.append("angry")


    if "no_blowjob" in RogueX.daily_history:
        $ RogueX.change_face("angry", 1)
        ch_r "Read my lips, no."
        $ RogueX.recent_history.append("angry")
        $ RogueX.daily_history.append("angry")
    elif RogueX.Forced:
        $ RogueX.change_face("angry", 1)
        ch_r "That isn't something I'd want!"
        $ RogueX.change_stat("lust", 200, 5)
        if RogueX.love > 300:
            $ RogueX.change_stat("love", 70, -2)
        $ RogueX.change_stat("obedience", 50, -2)
        $ RogueX.recent_history.append("angry")
        $ RogueX.daily_history.append("angry")
        $ RogueX.recent_history.append("no_blowjob")
        $ RogueX.daily_history.append("no_blowjob")
        return
    elif Taboo:
        $ RogueX.change_face("angry", 1)
        $ RogueX.daily_history.append("no_taboo")
        ch_r "You really expect me to do that here?"
        $ RogueX.change_stat("lust", 200, 5)
        $ RogueX.change_stat("obedience", 50, -3)
        return
    elif RogueX.action_counter["blowjob"]:
        $ RogueX.change_face("sad")
        ch_r "I think I've got the taste out of my mouth, thanks."
    else:
        $ RogueX.change_face("normal", 1)
        ch_r "Not interested."
    $ RogueX.recent_history.append("no_blowjob")
    $ RogueX.daily_history.append("no_blowjob")
    $ approval_bonus = 0
    return


label Rogue_BJ_Prep:
    if Taboo:
        $ RogueX.inhibition += int(Taboo/10)
        $ RogueX.lust += int(Taboo/5)

    $ RogueX.change_face("sexy")
    if RogueX.Forced:
        $ RogueX.change_face("sad")
    elif not RogueX.action_counter["blowjob"]:
        $ RogueX.brows = "confused"
        $ RogueX.eyes = "sexy"
        $ RogueX.mouth = "smile"

    call Seen_First_Peen (RogueX, Partner, React=action_context)
    call Rogue_BJ_Launch ("L")

    if action_context == RogueX:

        $ action_context = 0
        "[RogueX.name] slides down and gives your cock a little lick."
        menu:
            "What do you do?"
            "Nothing.":
                $ RogueX.change_stat("inhibition", 80, 3)
                $ RogueX.change_stat("inhibition", 40, 2)
                "[RogueX.name] continues licking at it."
            "Praise her.":
                $ RogueX.change_face("sexy", 1)
                $ RogueX.change_stat("inhibition", 80, 3)
                ch_p "Hmmm, keep doing that, [RogueX.petname]."
                $ RogueX.nameCheck()
                "[RogueX.name] continues her actions."
                $ RogueX.change_stat("love", 85, 1)
                $ RogueX.change_stat("obedience", 90, 1)
                $ RogueX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ RogueX.change_face("surprised")
                $ RogueX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that for now, [RogueX.petname]."
                $ RogueX.nameCheck()
                "[RogueX.name] puts it down."
                $ RogueX.change_stat("obedience", 90, 1)
                $ RogueX.change_stat("obedience", 50, 3)
                $ Player.recent_history.append("nope")
                $ RogueX.AddWord(1,"refused","refused")
                return

    if not RogueX.action_counter["blowjob"]:
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -70)
            $ RogueX.change_stat("obedience", 70, 45)
            $ RogueX.change_stat("inhibition", 80, 60)
        else:
            $ RogueX.change_stat("love", 90, 5)
            $ RogueX.change_stat("obedience", 70, 35)
            $ RogueX.change_stat("inhibition", 80, 40)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ RogueX.DrainWord("no_taboo")
    $ RogueX.DrainWord("no_blowjob")
    $ RogueX.recent_history.append("blowjob")
    $ RogueX.daily_history.append("blowjob")

label Rogue_BJ_Cycle:
    while Round > 0:
        call shift_focus (RogueX)
        call Rogue_BJ_Launch
        $ RogueX.lust_face()

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
                    if "pushed" not in RogueX.recent_history and RogueX.action_counter["blowjob"] < 5:
                        $ RogueX.change_stat("love", 80, -(20-(2*RogueX.action_counter["blowjob"])))
                        $ RogueX.change_stat("obedience", 80, (30-(3*RogueX.action_counter["blowjob"])))
                        $ RogueX.recent_history.append("pushed")
                    if offhand_action == "jackin" and action_speed != 3:
                        "She takes it to the root, and you move your hand out of the way."
                    $ action_speed = 4
                "Take it deeper. (locked)" if action_speed == 4:
                    pass
                "Set your own pace. . .":

                    "[RogueX.name] hums contentedly."
                    if "setpace" not in RogueX.recent_history:
                        $ RogueX.change_stat("love", 80, 2)
                    $ D20 = renpy.random.randint(1, 20)
                    if RogueX.action_counter["blowjob"] < 5:
                        $ D20 -= 10
                    elif RogueX.action_counter["blowjob"] < 10:
                        $ D20 -= 5

                    if D20 > 15:
                        $ action_speed = 4
                        if "setpace" not in RogueX.recent_history:
                            $ RogueX.change_stat("inhibition", 80, 3)
                    elif D20 > 10:
                        $ action_speed = 3
                    elif D20 > 5:
                        $ action_speed = 2
                    else:
                        $ action_speed = 1
                    $ RogueX.recent_history.append("setpace")

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
                            if RogueX.remaining_actions and multi_action:
                                $ offhand_action = "fondle_breasts"
                                "You start to fondle her breasts."
                                $ RogueX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (RogueX, "tired")
                        "Shift primary action":

                            if RogueX.remaining_actions and multi_action:
                                menu:
                                    "How about a handy?":
                                        if RogueX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Rogue_BJ_After
                                            call Rogue_Handjob
                                        else:
                                            call Sex_Basic_Dialog (RogueX, "tired")
                                    "How about a titjob?":
                                        if RogueX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Rogue_BJ_After
                                            call Rogue_Titjob
                                        else:
                                            call Sex_Basic_Dialog (RogueX, "tired")
                                    "Never Mind":
                                        jump Rogue_BJ_Cycle
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
                                    jump Rogue_BJ_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Rogue_BJ_Cycle
                                "Never mind":
                                    jump Rogue_BJ_Cycle
                        "Undress [RogueX.name]":
                            call Girl_Undress (RogueX)
                        "Clean up [RogueX.name] (locked)" if not RogueX.Spunk:
                            pass
                        "Clean up [RogueX.name]" if RogueX.Spunk:
                            call Girl_Cleanup (RogueX, "ask")
                        "Never mind":
                            jump Rogue_BJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Rogue_BJ_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Rogue_BJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Rogue_BJ_Reset
                    $ Line = 0
                    jump Rogue_BJ_After


        call shift_focus (RogueX)
        call Sex_Dialog (RogueX, Partner)



        $ counter += 1
        $ Round -= 1
        if action_speed:
            $ Player.Wet = 1
            $ Player.Spunk = 0 if Player.Spunk else Player.Spunk

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or RogueX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (RogueX)
                if "angry" in RogueX.recent_history:
                    call Rogue_BJ_Reset
                    return
                $ RogueX.change_stat("lust", 200, 5)
                if 100 > RogueX.lust >= 70 and RogueX.session_orgasms < 2 and RogueX.SEXP >= 20:
                    $ RogueX.recent_history.append("unsatisfied")
                    $ RogueX.daily_history.append("unsatisfied")
                if Player.focus > 80:
                    jump Rogue_BJ_After
                $ Line = "came"

            if RogueX.lust >= 100:

                call Girl_Cumming (RogueX)
                if action_context == "shift" or "angry" in RogueX.recent_history:
                    jump Rogue_BJ_After

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
                            jump Rogue_BJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif counter == (5 + RogueX.action_counter["blowjob"]):
            $ RogueX.brows = "confused"
            ch_r "Are you getting close here? My jaw's getting pretty sore."
        elif counter == (10 + RogueX.action_counter["blowjob"]):
            $ RogueX.brows = "angry"
            ch_r "I'm getting a little tired, [RogueX.player_petname]. Can we do something else?"
            menu:
                ch_r "I'm getting a little tired, [RogueX.player_petname]. Can we do something else?"
                "Continue (locked)":
                    pass
                "How about a Handy?" if RogueX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Rogue_BJ_After
                    call Rogue_Handjob
                    return
                "How about a Handy? (locked)" if not RogueX.remaining_actions or not multi_action:
                    pass
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    jump Rogue_BJ_Cycle
                "Finish up. (locked)" if not Player.focusing:
                    pass
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Rogue_BJ_Reset
                    $ action_context = "shift"
                    jump Rogue_BJ_After
                "Let's try something else. (locked)" if not multi_action:
                    pass
                "No, get back down there.":
                    if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):
                        $ RogueX.change_stat("love", 200, -5)
                        $ RogueX.change_stat("obedience", 50, 3)
                        $ RogueX.change_stat("obedience", 80, 2)
                        "She grumbles but gets back to work."
                    else:
                        $ RogueX.change_face("angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        ch_r "Well if that's your attitude you can handle your own business."
                        $ RogueX.change_stat("love", 50, -3, 1)
                        $ RogueX.change_stat("love", 80, -4, 1)
                        $ RogueX.change_stat("obedience", 30, -1, 1)
                        $ RogueX.change_stat("obedience", 50, -1, 1)
                        $ RogueX.recent_history.append("angry")
                        $ RogueX.daily_history.append("angry")
                        jump Rogue_BJ_After


        call Escalation (RogueX)

        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."


    $ RogueX.change_face("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.player_petname], that's enough of that for now."

label Rogue_BJ_After:
    $ RogueX.change_face("sexy")
    $ RogueX.action_counter["blowjob"] += 1
    $ RogueX.remaining_actions -=1
    $ RogueX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ RogueX.addiction_rate += 1

    if Partner == EmmaX:
        call Partner_Like (RogueX, 3)
    else:
        call Partner_Like (RogueX, 2)

    if "Rogue Jobber" in Achievements:
        pass
    elif RogueX.action_counter["blowjob"] >= 10:
        $ RogueX.change_face("smile", 1)
        ch_r "I'm really starting to enjoy this."
        $ Achievements.append("Rogue Jobber")
        $ RogueX.SEXP += 5
    elif action_context == "shift":
        pass
    elif RogueX.action_counter["blowjob"] == 1:
        $ RogueX.SEXP += 15
        if RogueX.love >= 500:
            $ RogueX.mouth = "smile"
            ch_r "That really wasn't half bad."
        elif Player.focus <= 20:
            $ RogueX.mouth = "sad"
            ch_r "Well, I hope that got your rocks off."
    elif RogueX.action_counter["blowjob"] == 5:
        ch_r "I think I've got the hang of this."

    $ approval_bonus = 0
    if action_context != "shift":
        call Rogue_BJ_Reset
    call checkout
    return

return




label Rogue_Dildo_Check:
    if "dildo" in Player.Inventory:
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in RogueX.Inventory:
        "You ask [RogueX.name] to get out her favorite Dildo."
    else:
        "You don't have one of those on you."
        return 0
    return 1

label Rogue_Dildo_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (RogueX)
    call Rogue_Dildo_Check
    if not _return:
        return

    if RogueX.action_counter["dildo_pussy"]:
        $ approval_bonus += 15
    if RogueX.PantsNum() > 6:
        $ approval_bonus -= 20

    if RogueX.lust > 95:
        $ approval_bonus += 20
    elif RogueX.lust > 85:
        $ approval_bonus += 15

    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in RogueX.Traits:
        $ approval_bonus += (5*Taboo)
    if RogueX in Player.Harem or "sex friend" in RogueX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in RogueX.Traits:
        $ approval_bonus -= 40
    if RogueX.event_counter["forced"] and not RogueX.Forced:
        $ approval_bonus -= 5*RogueX.event_counter["forced"]

    if Taboo and "no_taboo" in RogueX.daily_history:
        $ approval_bonus -= 10

    if "no_dildo" in RogueX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_dildo" in RogueX.recent_history else 0

    $ Approval = ApprovalCheck(RogueX, 1250, TabM = 4)

    if action_context == RogueX:
        if Approval > 2:
            if RogueX.PantsNum() == 5:
                "[RogueX.name] grabs her dildo, hiking up her skirt as she does."
                $ RogueX.Upskirt = 1
            elif RogueX.PantsNum() > 6:
                "[RogueX.name] grabs her dildo, pulling down her pants as she does."
                $ RogueX.legs = 0
            else:
                "[RogueX.name] grabs her dildo, rubbing is suggestively against her crotch."
            $ RogueX.SeenPanties = 1
            "She slides the tip along her pussy and seems to want you to insert it."
            menu:
                "What do you do?"
                "Nothing.":
                    $ RogueX.change_stat("inhibition", 80, 3)
                    $ RogueX.change_stat("inhibition", 50, 2)
                    "[RogueX.name] slides it in."
                "Go for it.":
                    $ RogueX.change_face("sexy", 1)
                    $ RogueX.change_stat("inhibition", 80, 3)
                    ch_p "Oh yeah, [RogueX.petname], let's do this."
                    $ RogueX.nameCheck()
                    "You grab the dildo and slide it in."
                    $ RogueX.change_stat("love", 85, 1)
                    $ RogueX.change_stat("obedience", 90, 1)
                    $ RogueX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ RogueX.change_face("surprised")
                    $ RogueX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that right now, [RogueX.petname]."
                    $ RogueX.nameCheck()
                    "[RogueX.name] sets the dildo down."
                    $ RogueX.change_stat("obedience", 90, 1)
                    $ RogueX.change_stat("obedience", 50, 1)
                    $ RogueX.change_stat("obedience", 30, 2)
                    return
            jump Rogue_DP_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
        return

    if action_context == "auto":
        "You rub the dildo across her body, and along her moist slit."
        $ RogueX.change_face("surprised", 1)

        if (RogueX.action_counter["dildo_pussy"] and Approval) or (Approval > 1):
            "[RogueX.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            $ RogueX.change_face("sexy")
            $ RogueX.change_stat("obedience", 70, 3)
            $ RogueX.change_stat("inhibition", 50, 3)
            $ RogueX.change_stat("inhibition", 70, 1)
            ch_r "Ok, [RogueX.player_petname], let's do this."
            jump Rogue_DP_Prep
        else:
            $ RogueX.brows = "angry"
            menu:
                ch_r "Hey, what do you think you're doing back there?!"
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ RogueX.change_face("sexy", 1)
                        $ RogueX.change_stat("obedience", 70, 3)
                        $ RogueX.change_stat("inhibition", 50, 3)
                        $ RogueX.change_stat("inhibition", 70, 1)
                        ch_r "Well, since you're be'in so nice about it, I guess we can give it a go. . ."
                        jump Rogue_DP_Prep
                    "You pull back before you really get it in."
                    $ RogueX.change_face("bemused", 1)
                    if RogueX.action_counter["dildo_pussy"]:
                        ch_r "Well ok, [RogueX.player_petname], no harm done. Just give me a little warning next time."
                    else:
                        ch_r "Well ok, [RogueX.player_petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."
                "Just playing with my favorite toys.":
                    $ RogueX.change_stat("love", 80, -10, 1)
                    $ RogueX.change_stat("love", 200, -10)
                    "You press it inside some more."
                    $ RogueX.change_stat("obedience", 70, 3)
                    $ RogueX.change_stat("inhibition", 50, 3)
                    if not ApprovalCheck(RogueX, 700, "O", TabM=1):
                        $ RogueX.change_face("angry")
                        "[RogueX.name] shoves you away and slaps you in the face."
                        ch_r "Jackass!"
                        ch_r "If that's how you want to treat me, we're done here!"
                        $ RogueX.change_stat("love", 50, -10, 1)
                        $ RogueX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        if renpy.showing("Rogue_Doggy"):
                            call Rogue_Doggy_Reset
                        $ RogueX.recent_history.append("angry")
                        $ RogueX.daily_history.append("angry")
                    else:
                        $ RogueX.change_face("sad")
                        "[RogueX.name] doesn't seem to be into this, you're lucky she's so obedient."
                        jump Rogue_DP_Prep
        return


    if not RogueX.action_counter["dildo_pussy"]:

        $ RogueX.change_face("surprised", 1)
        $ RogueX.mouth = "kiss"
        ch_r "Hmmm, so you'd like to try out some toys?"
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            ch_r "I suppose there are worst things you could ask for."

    if not RogueX.action_counter["dildo_pussy"] and Approval:

        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
        elif RogueX.love >= (RogueX.obedience + RogueX.inhibition):
            $ RogueX.change_face("sexy")
            $ RogueX.brows = "sad"
            $ RogueX.mouth = "smile"
            ch_r "I've had a reasonable amount of experience with these, you know. . ."
        elif RogueX.obedience >= RogueX.inhibition:
            $ RogueX.change_face("normal")
            ch_r "If that's what you want, [RogueX.player_petname]. . ."
        else:
            $ RogueX.change_face("sad")
            $ RogueX.mouth = "smile"
            ch_r "I guess it could be fun with a partner. . ."

    elif Approval:

        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
            ch_r "The toys again?"
        elif not Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "Well, at least you got us some privacy this time. . ."
        elif "dildo_pussy" in RogueX.recent_history:
            $ RogueX.change_face("sexy", 1)
            ch_r "Mmm, again? Ok, let's get to it."
            jump Rogue_DP_Prep
        elif "dildo_pussy" in RogueX.daily_history:
            $ RogueX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "You're going to wear me out."])
            ch_r "[Line]"
        elif RogueX.action_counter["dildo_pussy"] < 3:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.brows = "confused"
            $ RogueX.mouth = "kiss"
            ch_r "You want to stick it in my pussy again?"
        else:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my pussy again?",
                    "You want me ta lube up your toy?"])
            ch_r "[Line]"
            $ Line = 0

    if Approval >= 2:

        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("obedience", 90, 1)
            $ RogueX.change_stat("inhibition", 60, 1)
            ch_r "Ok, fine."
        else:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.change_stat("love", 90, 1)
            $ RogueX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                    "Well. . . ok.",                 
                    "Sure!", 
                    "I guess I could. . . stick it in.",
                    "Hells yeah.",
                    "Heh, ok, ok."])
            ch_r "[Line]"
            $ Line = 0
        $ RogueX.change_stat("obedience", 20, 1)
        $ RogueX.change_stat("obedience", 60, 1)
        $ RogueX.change_stat("inhibition", 70, 2)
        jump Rogue_DP_Prep
    else:


        $ RogueX.change_face("angry")
        if "no_dildo" in RogueX.recent_history:
            ch_r "What part of \"no,\" did you not get, [RogueX.player_petname]?"
        elif Taboo and "no_taboo" in RogueX.daily_history and "no_dildo" in RogueX.daily_history:
            ch_r "Stop swinging that thing around in public!"
        elif "no_dildo" in RogueX.daily_history:
            ch_r "I already told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "Stop swinging that thing around in public!"
        elif not RogueX.action_counter["dildo_pussy"]:
            $ RogueX.change_face("bemused")
            ch_r "I'm just not into toys, [RogueX.player_petname]. . ."
        else:
            $ RogueX.change_face("bemused")
            ch_r "I don't think we need any toys, [RogueX.player_petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no_dildo" in RogueX.daily_history:
                $ RogueX.change_face("bemused")
                ch_r "Yeah, ok, [RogueX.player_petname]."
                return
            "Maybe later?" if "no_dildo" not in RogueX.daily_history:
                $ RogueX.change_face("sexy")
                ch_r "Maybe I'll practice on my own time, [RogueX.player_petname]."
                $ RogueX.change_stat("love", 80, 2)
                $ RogueX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ RogueX.recent_history.append("no_taboo")
                    $ RogueX.daily_history.append("no_taboo")
                $ RogueX.recent_history.append("no_dildo")
                $ RogueX.daily_history.append("no_dildo")
                return
            "I think you'd like it. . .":
                if Approval:
                    $ RogueX.change_face("sexy")
                    $ RogueX.change_stat("obedience", 90, 2)
                    $ RogueX.change_stat("obedience", 50, 2)
                    $ RogueX.change_stat("inhibition", 70, 3)
                    $ RogueX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                            "I suppose. . .", 
                            "You've got me there."])
                    ch_r "[Line]"
                    $ Line = 0
                    jump Rogue_DP_Prep
                else:
                    pass
            "[[press it against her]":

                $ Approval = ApprovalCheck(RogueX, 950, "OI", TabM = 3)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.change_face("sad")
                    $ RogueX.change_stat("love", 70, -5, 1)
                    $ RogueX.change_stat("love", 200, -5)
                    ch_r "Ok, fine. If we're going to do this, stick it in already."
                    $ RogueX.change_stat("obedience", 80, 4)
                    $ RogueX.change_stat("inhibition", 80, 1)
                    $ RogueX.change_stat("inhibition", 60, 3)
                    $ RogueX.Forced = 1
                    jump Rogue_DP_Prep
                else:
                    $ RogueX.change_stat("love", 200, -20)
                    $ RogueX.recent_history.append("angry")
                    $ RogueX.daily_history.append("angry")


    $ RogueX.ArmPose = 1
    if "no_dildo" in RogueX.daily_history:
        ch_r "Learn to take \"no\" for an answer, [RogueX.player_petname]."
        $ RogueX.recent_history.append("angry")
        $ RogueX.daily_history.append("angry")
    elif RogueX.Forced:
        $ RogueX.change_face("angry", 1)
        ch_r "I'm not going to let you use that on me."
        $ RogueX.change_stat("lust", 200, 5)
        if RogueX.love > 300:
            $ RogueX.change_stat("love", 70, -2)
        $ RogueX.change_stat("obedience", 50, -2)
        $ RogueX.recent_history.append("angry")
        $ RogueX.daily_history.append("angry")
    elif Taboo:
        $ RogueX.change_face("angry", 1)
        $ RogueX.recent_history.append("no_taboo")
        $ RogueX.daily_history.append("no_taboo")
        ch_r "Not here!"
        $ RogueX.change_stat("lust", 200, 5)
        $ RogueX.change_stat("obedience", 50, -3)
    elif RogueX.action_counter["dildo_pussy"]:
        $ RogueX.change_face("sad")
        ch_r "Sorry, you can keep your toys to yourself."
    else:
        $ RogueX.change_face("normal", 1)
        ch_r "No way."
    $ RogueX.recent_history.append("no_dildo")
    $ RogueX.daily_history.append("no_dildo")
    $ approval_bonus = 0
    return

label Rogue_DP_Prep:
    if offhand_action == "dildo_pussy":
        return

    if not RogueX.Forced and action_context != "auto":
        $ approval_bonus = 15 if RogueX.PantsNum() > 6 else 0
        call Bottoms_Off (RogueX)
        if "angry" in RogueX.recent_history:
            return

    $ approval_bonus = 0
    call Rogue_Pussy_Launch ("dildo_pussy")
    if not RogueX.action_counter["dildo_pussy"]:
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -75)
            $ RogueX.change_stat("obedience", 70, 60)
            $ RogueX.change_stat("inhibition", 80, 35)
        else:
            $ RogueX.change_stat("love", 90, 10)
            $ RogueX.change_stat("obedience", 70, 20)
            $ RogueX.change_stat("inhibition", 80, 45)
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
    $ RogueX.DrainWord("no_dildo")
    $ RogueX.recent_history.append("dildo_pussy")
    $ RogueX.daily_history.append("dildo_pussy")

label Rogue_DP_Cycle:
    while Round > 0:
        call shift_focus (RogueX)
        call ViewShift (RogueX, RogueX.pose, 0)
        $ RogueX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (RogueX)
                    jump Rogue_DP_Cycle

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
                    jump Rogue_DP_Cycle
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
                                    "I want to stick a finger in her ass.":
                                        $ action_context = "shift"
                                        call Rogue_DP_After
                                        call Rogue_Insert_Ass
                                    "Just stick a finger in her ass without asking.":
                                        $ action_context = "auto"
                                        call Rogue_DP_After
                                        call Rogue_Insert_Ass
                                    "I want to shift the dildo to her ass.":
                                        $ action_context = "shift"
                                        call Rogue_DP_After
                                        call Rogue_Dildo_Ass
                                    "Never Mind":
                                        jump Rogue_DP_Cycle
                            else:
                                call Sex_Basic_Dialog (RogueX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Rogue_DP_After
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
                                    jump Rogue_DP_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Rogue_DP_Cycle
                                "Never mind":
                                    jump Rogue_DP_Cycle
                        "Undress [RogueX.name]":
                            call Girl_Undress (RogueX)
                        "Clean up [RogueX.name] (locked)" if not RogueX.Spunk:
                            pass
                        "Clean up [RogueX.name]" if RogueX.Spunk:
                            call Girl_Cleanup (RogueX, "ask")
                        "Never mind":
                            jump Rogue_DP_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Rogue_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Rogue_DP_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Rogue_Pos_Reset
                    $ Line = 0
                    jump Rogue_DP_After


        if RogueX.underwear or RogueX.PantsNum() > 6 or RogueX.HoseNum() >= 5:
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
                    $ RogueX.recent_history.append("unsatisfied")
                    $ RogueX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Rogue_DP_After
                $ Line = "came"

            if RogueX.lust >= 100:

                call Girl_Cumming (RogueX)
                if action_context == "shift" or "angry" in RogueX.recent_history:
                    jump Rogue_DP_After

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
                            jump Rogue_DP_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)

        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif counter == (5 + RogueX.action_counter["dildo_ass"]):
            $ RogueX.brows = "confused"
            ch_r "What are you even doing down there?"
        elif RogueX.lust >= 80:
            pass
        elif counter == (15 + RogueX.action_counter["dildo_ass"]) and RogueX.SEXP >= 15 and not ApprovalCheck(RogueX, 1500):
            $ RogueX.brows = "confused"
            menu:
                ch_r "[RogueX.player_petname], this is getting uncomfortable, maybe we could try something else."
                "Finish up.":
                    "You let go. . ."
                    jump Rogue_DP_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Rogue_DP_After
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
                        $ RogueX.recent_history.append("angry")
                        $ RogueX.daily_history.append("angry")
                        jump Rogue_DP_After


        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."


    $ RogueX.change_face("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.player_petname], that's enough of that for now."

label Rogue_DP_After:
    if not action_context:
        call Rogue_Pos_Reset

    $ RogueX.change_face("sexy")

    $ RogueX.action_counter["dildo_pussy"] += 1
    $ RogueX.remaining_actions -=1

    call Partner_Like (RogueX, 2)

    if RogueX.action_counter["dildo_pussy"] == 1:
        $ RogueX.SEXP += 10
        if not action_context:
            if RogueX.love >= 500 and "unsatisfied" not in RogueX.recent_history:
                ch_r "Well I liked that. . ."
            elif RogueX.obedience <= 500 and Player.focus <= 20:
                $ RogueX.change_face("perplexed", 1)
                ch_r "Did you like that?"

    $ approval_bonus = 0


    call checkout
    return






label Rogue_Dildo_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (RogueX)
    call Rogue_Dildo_Check
    if not _return:
        return

    if RogueX.used_to_anal:
        $ approval_bonus += 30
    elif "anal" in RogueX.recent_history or "dildo_anal" in RogueX.recent_history:
        $ approval_bonus -= 20
    elif "anal" in RogueX.daily_history or "dildo_anal" in RogueX.daily_history:
        $ approval_bonus -= 10
    elif (RogueX.action_counter["anal"] + RogueX.action_counter["dildo_ass"] + RogueX.Plug) > 0:
        $ approval_bonus += 20

    if RogueX.PantsNum() > 6:
        $ approval_bonus -= 20

    if RogueX.lust > 95:
        $ approval_bonus += 20
    elif RogueX.lust > 85:
        $ approval_bonus += 15

    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in RogueX.Traits:
        $ approval_bonus += (5*Taboo)
    if RogueX in Player.Harem or "sex friend" in RogueX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in RogueX.Traits:
        $ approval_bonus -= 40
    if RogueX.event_counter["forced"] and not RogueX.Forced:
        $ approval_bonus -= 5*RogueX.event_counter["forced"]

    if Taboo and "no_taboo" in RogueX.daily_history:
        $ approval_bonus -= 10

    if "no_dildo" in RogueX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_dildo" in RogueX.recent_history else 0

    $ Approval = ApprovalCheck(RogueX, 1450, TabM = 4)

    if action_context == RogueX:

        if Approval > 2:
            if RogueX.PantsNum() == 5:
                "[RogueX.name] grabs her dildo, hiking up her skirt as she does."
                $ RogueX.Upskirt = 1
            elif RogueX.PantsNum() > 6:
                "[RogueX.name] grabs her dildo, pulling down her pants as she does."
                $ RogueX.legs = 0
            else:
                "[RogueX.name] grabs her dildo, rubbing is suggestively against her ass."
            $ RogueX.SeenPanties = 1
            "She slides the tip against her asshole, and seems to want you to insert it."
            menu:
                "What do you do?"
                "Nothing.":
                    $ RogueX.change_stat("inhibition", 80, 3)
                    $ RogueX.change_stat("inhibition", 50, 2)
                    "[RogueX.name] slides it in."
                "Go for it.":
                    $ RogueX.change_face("sexy", 1)
                    $ RogueX.change_stat("inhibition", 80, 3)
                    ch_p "Oh yeah, [RogueX.petname], let's do this."
                    $ RogueX.nameCheck()
                    "You grab the dildo and slide it in."
                    $ RogueX.change_stat("love", 85, 1)
                    $ RogueX.change_stat("obedience", 90, 1)
                    $ RogueX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ RogueX.change_face("surprised")
                    $ RogueX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that right now, [RogueX.petname]."
                    $ RogueX.nameCheck()
                    "[RogueX.name] sets the dildo down."
                    $ RogueX.change_stat("obedience", 90, 1)
                    $ RogueX.change_stat("obedience", 50, 1)
                    $ RogueX.change_stat("obedience", 30, 2)
                    return
            jump Rogue_DA_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
        return

    if action_context == "auto":
        "You rub the dildo across her body, and against her tight anus."
        $ RogueX.change_face("surprised", 1)

        if (RogueX.action_counter["dildo_ass"] and Approval) or (Approval > 1):

            "[RogueX.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            $ RogueX.change_face("sexy")
            $ RogueX.change_stat("obedience", 70, 3)
            $ RogueX.change_stat("inhibition", 50, 3)
            $ RogueX.change_stat("inhibition", 70, 1)
            ch_r "Ok, [RogueX.player_petname], let's do this."
            jump Rogue_DA_Prep
        else:

            $ RogueX.brows = "angry"
            menu:
                ch_r "Hey, what do you think you're doing back there?!"
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ RogueX.change_face("sexy", 1)
                        $ RogueX.change_stat("obedience", 70, 3)
                        $ RogueX.change_stat("inhibition", 50, 3)
                        $ RogueX.change_stat("inhibition", 70, 1)
                        ch_r "Well, since you're be'in so nice about it, I guess we can give it a go. . ."
                        jump Rogue_DA_Prep
                    "You pull back before you really get it in."
                    $ RogueX.change_face("bemused", 1)
                    if RogueX.action_counter["dildo_ass"]:
                        ch_r "Well ok, [RogueX.player_petname], no harm done. Just give me a little warning next time."
                    else:
                        ch_r "Well ok, [RogueX.player_petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."
                "Just playing with my favorite toys.":
                    $ RogueX.change_stat("love", 80, -10, 1)
                    $ RogueX.change_stat("love", 200, -10)
                    "You press it inside some more."
                    $ RogueX.change_stat("obedience", 70, 3)
                    $ RogueX.change_stat("inhibition", 50, 3)
                    if not ApprovalCheck(RogueX, 700, "O", TabM=1):
                        $ RogueX.change_face("angry")
                        "[RogueX.name] shoves you away and slaps you in the face."
                        ch_r "Jackass!"
                        ch_r "If that's how you want to treat me, we're done here!"
                        $ RogueX.change_stat("love", 50, -10, 1)
                        $ RogueX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        if renpy.showing("Rogue_Doggy"):
                            call Rogue_Doggy_Reset
                        $ RogueX.recent_history.append("angry")
                        $ RogueX.daily_history.append("angry")
                    else:
                        $ RogueX.change_face("sad")
                        "[RogueX.name] doesn't seem to be into this, you're lucky she's so obedient."
                        jump Rogue_DA_Prep
        return


    if not RogueX.action_counter["dildo_ass"]:

        $ RogueX.change_face("surprised", 1)
        $ RogueX.mouth = "kiss"
        ch_r "Hmmm, so you'd like to try out some toys?"
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            ch_r "You had to go for the butt, uh?"

    if not RogueX.used_to_anal and ("dildo_anal" in RogueX.recent_history or "anal" in RogueX.recent_history or "dildo_anal" in RogueX.daily_history or "anal" in RogueX.daily_history):
        $ RogueX.change_face("bemused", 1)
        ch_r "I'm still a bit sore from earlier. . ."

    if not RogueX.action_counter["dildo_ass"] and Approval:

        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
        elif RogueX.love >= (RogueX.obedience + RogueX.inhibition):
            $ RogueX.change_face("sexy")
            $ RogueX.brows = "sad"
            $ RogueX.mouth = "smile"
            ch_r "I haven't actually used one of these, back there before. . ."
        elif RogueX.obedience >= RogueX.inhibition:
            $ RogueX.change_face("normal")
            ch_r "If that's what you want, [RogueX.player_petname]. . ."
        else:
            $ RogueX.change_face("sad")
            $ RogueX.mouth = "smile"
            ch_r "I guess it could be fun with a partner. . ."

    elif Approval:

        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
            ch_r "The toys again?"
        elif not Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "Well, at least you got us some privacy this time. . ."
        elif "dildo_anal" in RogueX.daily_history and not RogueX.used_to_anal:
            pass
        elif "dildo_anal" in RogueX.daily_history:
            $ RogueX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "I'm still a bit sore from earlier.",
                    "You're going to wear me out."])
            ch_r "[Line]"
        elif RogueX.action_counter["dildo_ass"] < 3:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.brows = "confused"
            $ RogueX.mouth = "kiss"
            ch_r "You want to stick it in my ass again?"
        else:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my ass again?",
                    "You want me ta lube up your toy?"])
            ch_r "[Line]"
            $ Line = 0

    if Approval >= 2:

        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("obedience", 90, 1)
            $ RogueX.change_stat("inhibition", 60, 1)
            ch_r "Ok, fine."
        else:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.change_stat("love", 90, 1)
            $ RogueX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                    "Well. . . ok.",                 
                    "Sure!", 
                    "I guess I could. . . stick it in.",
                    "Hells yeah.",
                    "Heh, ok, ok."])
            ch_r "[Line]"
            $ Line = 0
        $ RogueX.change_stat("obedience", 20, 1)
        $ RogueX.change_stat("obedience", 60, 1)
        $ RogueX.change_stat("inhibition", 70, 2)
        jump Rogue_DA_Prep
    else:


        $ RogueX.change_face("angry")
        if "no_dildo" in RogueX.recent_history:
            ch_r "What part of \"no,\" did you not get, [RogueX.player_petname]?"
        elif Taboo and "no_taboo" in RogueX.daily_history and "no_dildo" in RogueX.daily_history:
            ch_r "Stop swinging that thing around in public!"
        elif "no_dildo" in RogueX.daily_history:
            ch_r "I already told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "I already told you that I wouldn't do that out here!"
        elif not RogueX.action_counter["dildo_ass"]:
            $ RogueX.change_face("bemused")
            ch_r "I'm just not into toys, [RogueX.player_petname]. . ."
        elif not RogueX.used_to_anal and "dildo_anal" not in RogueX.daily_history:
            $ RogueX.change_face("perplexed")
            ch_r "You could have been a bit more gentle last time, [RogueX.player_petname]. . ."
        else:
            $ RogueX.change_face("bemused")
            ch_r "I don't think we need any toys, [RogueX.player_petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no_dildo" in RogueX.daily_history:
                $ RogueX.change_face("bemused")
                ch_r "Yeah, ok, [RogueX.player_petname]."
                return
            "Maybe later?" if "no_dildo" not in RogueX.daily_history:
                $ RogueX.change_face("sexy")
                ch_r "Maybe I'll practice on my own time, [RogueX.player_petname]."
                $ RogueX.change_stat("love", 80, 2)
                $ RogueX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ RogueX.recent_history.append("no_taboo")
                    $ RogueX.daily_history.append("no_taboo")
                $ RogueX.recent_history.append("no_dildo")
                $ RogueX.daily_history.append("no_dildo")
                return
            "I think you'd like it. . .":
                if Approval:
                    $ RogueX.change_face("sexy")
                    $ RogueX.change_stat("obedience", 90, 2)
                    $ RogueX.change_stat("obedience", 50, 2)
                    $ RogueX.change_stat("inhibition", 70, 3)
                    $ RogueX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                            "I suppose. . .", 
                            "You've got me there."])
                    ch_r "[Line]"
                    $ Line = 0
                    jump Rogue_DA_Prep
                else:
                    pass
            "[[press it against her]":

                $ Approval = ApprovalCheck(RogueX, 1050, "OI", TabM = 3)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.change_face("sad")
                    $ RogueX.change_stat("love", 70, -5, 1)
                    $ RogueX.change_stat("love", 200, -5)
                    ch_r "Ok, fine. If we're going to do this, stick it in already."
                    $ RogueX.change_stat("obedience", 80, 4)
                    $ RogueX.change_stat("inhibition", 80, 1)
                    $ RogueX.change_stat("inhibition", 60, 3)
                    $ RogueX.Forced = 1
                    jump Rogue_DA_Prep
                else:
                    $ RogueX.change_stat("love", 200, -20)
                    $ RogueX.recent_history.append("angry")
                    $ RogueX.daily_history.append("angry")


    $ RogueX.ArmPose = 1
    if "no_dildo" in RogueX.daily_history:
        ch_r "Learn to take \"no\" for an answer, [RogueX.player_petname]."
        $ RogueX.recent_history.append("angry")
        $ RogueX.daily_history.append("angry")
    elif RogueX.Forced:
        $ RogueX.change_face("angry", 1)
        ch_r "I'm not going to let you use that on me."
        $ RogueX.change_stat("lust", 200, 5)
        if RogueX.love > 300:
            $ RogueX.change_stat("love", 70, -2)
        $ RogueX.change_stat("obedience", 50, -2)
        $ RogueX.recent_history.append("angry")
        $ RogueX.daily_history.append("angry")
    elif Taboo:
        $ RogueX.change_face("angry", 1)
        $ RogueX.recent_history.append("no_taboo")
        $ RogueX.daily_history.append("no_taboo")
        ch_r "Not here!"
        $ RogueX.change_stat("lust", 200, 5)
        $ RogueX.change_stat("obedience", 50, -3)
    elif not RogueX.used_to_anal and "dildo_anal" in RogueX.daily_history:
        $ RogueX.change_face("bemused")
        ch_r "Sorry, I just need a little break back there, [RogueX.player_petname]."
    elif RogueX.action_counter["dildo_ass"]:
        $ RogueX.change_face("sad")
        ch_r "Sorry, you can keep your toys out of there."
    else:
        $ RogueX.change_face("normal", 1)
        ch_r "No way."
    $ RogueX.recent_history.append("no_dildo")
    $ RogueX.daily_history.append("no_dildo")
    $ approval_bonus = 0
    return

label Rogue_DA_Prep:
    if offhand_action == "dildo_anal":
        return

    if not RogueX.Forced and action_context != "auto":
        $ approval_bonus = 20 if RogueX.PantsNum() > 6 else 0
        call Bottoms_Off (RogueX)
        if "angry" in RogueX.recent_history:
            return

    $ approval_bonus = 0
    call Rogue_Pussy_Launch ("dildo_anal")
    if not RogueX.action_counter["dildo_ass"]:
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -75)
            $ RogueX.change_stat("obedience", 70, 60)
            $ RogueX.change_stat("inhibition", 80, 35)
        else:
            $ RogueX.change_stat("love", 90, 10)
            $ RogueX.change_stat("obedience", 70, 20)
            $ RogueX.change_stat("inhibition", 80, 45)
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
    $ RogueX.DrainWord("no_dildo")
    $ RogueX.recent_history.append("dildo_anal")
    $ RogueX.daily_history.append("dildo_anal")

label Rogue_DA_Cycle:
    while Round > 0:
        call ViewShift (RogueX, RogueX.pose, 0)
        call shift_focus (RogueX)
        $ RogueX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (RogueX)
                    jump Rogue_DA_Cycle

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
                    jump Rogue_DA_Cycle
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
                                    "I want to stick a finger in her pussy.":
                                        $ action_context = "shift"
                                        call Rogue_DA_After
                                        call Rogue_Fondle_Pussy
                                    "Just stick a finger in her pussy without asking.":
                                        $ action_context = "auto"
                                        call Rogue_DA_After
                                        call Rogue_Fondle_Pussy
                                    "I want to shift the dildo to her pussy.":
                                        $ action_context = "shift"
                                        call Rogue_DA_After
                                        call Rogue_Dildo_Pussy
                                    "Never Mind":
                                        jump Rogue_DA_Cycle
                            else:
                                call Sex_Basic_Dialog (RogueX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Rogue_DA_After
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
                                    jump Rogue_DA_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Rogue_DA_Cycle
                                "Never mind":
                                    jump Rogue_DA_Cycle
                        "Undress [RogueX.name]":
                            call Girl_Undress (RogueX)
                        "Clean up [RogueX.name] (locked)" if not RogueX.Spunk:
                            pass
                        "Clean up [RogueX.name]" if RogueX.Spunk:
                            call Girl_Cleanup (RogueX, "ask")
                        "Never mind":
                            jump Rogue_DA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Rogue_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Rogue_DA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Rogue_Pos_Reset
                    $ Line = 0
                    jump Rogue_DA_After


        if RogueX.underwear or RogueX.PantsNum() > 6 or RogueX.HoseNum() >= 5:
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
                    $ RogueX.recent_history.append("unsatisfied")
                    $ RogueX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Rogue_DA_After
                $ Line = "came"

            if RogueX.lust >= 100:

                call Girl_Cumming (RogueX)
                if action_context == "shift" or "angry" in RogueX.recent_history:
                    jump Rogue_DA_After

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
                            jump Rogue_DA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif counter == (5 + RogueX.action_counter["dildo_ass"]):
            $ RogueX.brows = "confused"
            ch_r "What are you even doing down there?"
        elif RogueX.lust >= 80:
            pass
        elif counter == (15 + RogueX.action_counter["dildo_ass"]) and RogueX.SEXP >= 15 and not ApprovalCheck(RogueX, 1500):
            $ RogueX.brows = "confused"
            menu:
                ch_r "[RogueX.player_petname], this is getting uncomfortable, maybe we could try something else."
                "Finish up.":
                    "You let go. . ."
                    jump Rogue_DA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Rogue_DA_After
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
                        $ RogueX.recent_history.append("angry")
                        $ RogueX.daily_history.append("angry")
                        jump Rogue_DA_After


        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."


    $ RogueX.change_face("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.player_petname], that's enough of that for now."


label Rogue_DA_After:
    if not action_context:
        call Rogue_Pos_Reset

    $ RogueX.change_face("sexy")

    $ RogueX.action_counter["dildo_ass"] += 1
    $ RogueX.remaining_actions -=1

    call Partner_Like (RogueX, 2)

    if RogueX.action_counter["dildo_ass"] == 1:
        $ RogueX.SEXP += 10
        if not action_context:
            if RogueX.love >= 500 and "unsatisfied" not in RogueX.recent_history:
                if RogueX.used_to_anal:
                    ch_r "Well I liked that. . ."
                else:
                    ch_r "Well that was a bit rough. . ."
            elif RogueX.obedience <= 500 and Player.focus <= 20:
                $ RogueX.change_face("perplexed", 1)
                ch_r "Did you like that?"

    $ approval_bonus = 0


    call checkout
    return



label Rogue_Vibrator_Check:
    if "vibrator" in Player.Inventory:
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in RogueX.Inventory:
        "You ask [RogueX.name] to get out her vibrator."
    else:
        "You don't have one of those on you."
        return 0
    return 1




label Rogue_Footjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (RogueX)
    if RogueX.action_counter["footjob"] >= 7:
        $ approval_bonus += 10
    elif RogueX.action_counter["footjob"] >= 3:
        $ approval_bonus += 7
    elif RogueX.action_counter["footjob"]:
        $ approval_bonus += 3

    if RogueX.addiction >= 75 and RogueX.event_counter["swallowed"] >=3:
        $ approval_bonus += 10
    if RogueX.addiction >= 75:
        $ approval_bonus += 5

    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in RogueX.Traits:
        $ approval_bonus += (3*Taboo)
    if RogueX in Player.Harem or "sex friend" in RogueX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in RogueX.Traits:
        $ approval_bonus -= 40
    if RogueX.event_counter["forced"] and not RogueX.Forced:
        $ approval_bonus -= 5*RogueX.event_counter["forced"]

    if Taboo and "no_taboo" in RogueX.daily_history:
        $ approval_bonus -= 10

    if "no_foot" in RogueX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_foot" in RogueX.recent_history else 0

    $ Approval = ApprovalCheck(RogueX, 1250, TabM = 3)

    if action_context == RogueX:
        if Approval > 2:
            "[RogueX.name] leans forward and starts rubbing your cock between her feet."
            menu:
                "What do you do?"
                "Nothing.":
                    $ RogueX.change_stat("inhibition", 70, 3)
                    $ RogueX.change_stat("inhibition", 30, 2)
                    "[RogueX.name] continues her actions."
                "Praise her.":
                    $ RogueX.change_face("sexy", 1)
                    $ RogueX.change_stat("inhibition", 70, 3)
                    ch_p "Oooh, that's good, [RogueX.petname]."
                    $ RogueX.nameCheck()
                    "[RogueX.name] continues her actions."
                    $ RogueX.change_stat("love", 80, 1)
                    $ RogueX.change_stat("obedience", 90, 1)
                    $ RogueX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ RogueX.change_face("surprised")
                    $ RogueX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that for now, [RogueX.petname]."
                    $ RogueX.nameCheck()
                    "[RogueX.name] puts it down."
                    $ RogueX.change_stat("obedience", 90, 1)
                    $ RogueX.change_stat("obedience", 50, 1)
                    $ RogueX.change_stat("obedience", 30, 2)
                    return
            if primary_action:
                $ girl_offhand_action = "foot"
                return
            jump Rogue_FJ_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if not RogueX.action_counter["footjob"] and "no_foot" not in RogueX.recent_history:
        $ RogueX.change_face("confused", 2)
        ch_r "Huh, so like a handy, but with my feet?"
        $ RogueX.blushing = 1

    if not RogueX.action_counter["footjob"] and Approval:
        if RogueX.Forced:
            $ RogueX.change_face("sad",1)
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
        elif RogueX.love >= (RogueX.obedience + RogueX.inhibition):
            $ RogueX.change_face("sexy",1)
            $ RogueX.brows = "sad"
            $ RogueX.mouth = "smile"
            ch_r "If that's what you like. . ."
        elif RogueX.obedience >= RogueX.inhibition:
            $ RogueX.change_face("normal",1)
            ch_r "If that's what you want, [RogueX.player_petname]. . ."
        elif RogueX.addiction >= 50:
            $ RogueX.change_face("manic", 1)
            ch_r "I guess. . ."
        else:
            $ RogueX.change_face("lipbite",1)
            ch_r "Sure. . ."

    elif Approval:
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
            ch_r "That's it?"
        elif not Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "I guess here would be ok. . ."
        elif "foot" in RogueX.recent_history:
            $ RogueX.change_face("sexy", 1)
            ch_r "I don't want to wear them out. . ."
            jump Rogue_FJ_Prep
        elif "foot" in RogueX.daily_history:
            $ RogueX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Another one?",   
                "You're going to give me calluses.", 
                "Didn't get enough earlier?",
                "My feet are a bit sore from earlier.",
                "My feet are kinda sore from earlier."])
            ch_r "[Line]"
        elif RogueX.action_counter["footjob"] < 3:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.brows = "confused"
            $ RogueX.mouth = "kiss"
            ch_r "Again?"
        else:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.ArmPose = 2
            $ Line = renpy.random.choice(["You want me to use my feet?",                 
                "So you'd like another foot rub?",                 
                "So you'd like me to. . . [she rubs her foot along your leg]?", 
                "So you'd like another foot rub?"])
            ch_r "[Line]"
        $ Line = 0

    if Approval >= 2:
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("obedience", 90, 1)
            $ RogueX.change_stat("inhibition", 60, 1)
            ch_r ". . . Ok, if that's what you want."
        elif "no_foot" in RogueX.daily_history:
            ch_r "Fine!"
        else:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.change_stat("love", 90, 1)
            $ RogueX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Sure, I guess.",                 
                "Okay.",                 
                "Ok, lemme see it.", 
                "I guess. . .",
                "Ok. . . [She gestures for you to come over].",
                "Heh, ok, fine."])
            ch_r "[Line]"
            $ Line = 0
        $ RogueX.change_stat("obedience", 20, 1)
        $ RogueX.change_stat("obedience", 60, 1)
        $ RogueX.change_stat("inhibition", 70, 2)
        jump Rogue_FJ_Prep
    else:

        $ RogueX.change_face("angry")
        if "no_foot" in RogueX.recent_history:
            ch_r "I just said \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history and "no_foot" in RogueX.daily_history:
            ch_r "Not in public!"
        elif "no_foot" in RogueX.daily_history:
            ch_r "I told you \"no\" earlier [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "I said not in public!"
        elif not RogueX.action_counter["footjob"]:
            $ RogueX.change_face("bemused")
            ch_r ". . . well I don't know about that, [RogueX.player_petname]. . ."
        else:
            $ RogueX.change_face("bemused")
            ch_r "Maybe not right now, ok?"
        menu:
            extend ""
            "Sorry, never mind." if "no_foot" in RogueX.daily_history:
                $ RogueX.change_face("bemused")
                ch_r "No problem."
                return
            "Maybe later?" if "no_foot" not in RogueX.daily_history:
                $ RogueX.change_face("sexy")
                ch_r ". . ."
                ch_r "I guess?"
                $ RogueX.change_stat("love", 80, 2)
                $ RogueX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ RogueX.recent_history.append("no_taboo")
                    $ RogueX.daily_history.append("no_taboo")
                $ RogueX.recent_history.append("no_foot")
                $ RogueX.daily_history.append("no_foot")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ RogueX.change_face("sexy")
                    $ RogueX.change_stat("obedience", 90, 2)
                    $ RogueX.change_stat("obedience", 50, 2)
                    $ RogueX.change_stat("inhibition", 70, 3)
                    $ RogueX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Sure, I guess.",                 
                        "Okay.",                 
                        "Ok, lemme see it.", 
                        "I guess. . .",
                        "Ok. . . [She gestures for you to come over].",
                        "Heh, ok, fine."])
                    ch_r "[Line]"
                    $ Line = 0
                    jump Rogue_FJ_Prep
                else:
                    pass
            "Come on, get to work.":

                $ Approval = ApprovalCheck(RogueX, 400, "OI", TabM = 3)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.change_face("sad")
                    $ RogueX.change_stat("love", 70, -5, 1)
                    $ RogueX.change_stat("love", 200, -2)
                    ch_r "Ok, fine."
                    $ RogueX.change_stat("obedience", 50, 4)
                    $ RogueX.change_stat("inhibition", 80, 1)
                    $ RogueX.change_stat("inhibition", 60, 3)
                    $ RogueX.Forced = 1
                    jump Rogue_FJ_Prep
                else:
                    $ RogueX.change_stat("love", 200, -15)
                    $ RogueX.recent_history.append("angry")
                    $ RogueX.daily_history.append("angry")


    $ RogueX.ArmPose = 1
    if "no_foot" in RogueX.daily_history:
        $ RogueX.change_face("angry", 1)
        ch_r "I'aint tellin you again."
        $ RogueX.recent_history.append("angry")
        $ RogueX.daily_history.append("angry")
    elif RogueX.Forced:
        $ RogueX.change_face("angry", 1)
        ch_r "Not even with my feet."
        $ RogueX.change_stat("lust", 200, 5)
        if RogueX.love > 300:
            $ RogueX.change_stat("love", 70, -2)
        $ RogueX.change_stat("obedience", 50, -2)
        $ RogueX.recent_history.append("angry")
        $ RogueX.daily_history.append("angry")
    elif Taboo:
        $ RogueX.change_face("angry", 1)
        $ RogueX.daily_history.append("no_taboo")
        ch_r "Not in such an exposed place, [RogueX.player_petname]."
        $ RogueX.change_stat("lust", 200, 5)
        $ RogueX.change_stat("obedience", 50, -3)
    elif RogueX.action_counter["footjob"]:
        $ RogueX.change_face("sad")
        ch_r "Not right now, [RogueX.player_petname]. . ."
    else:
        $ RogueX.change_face("normal", 1)
        ch_r "That isn't really how I planned to use my feet today"
    $ RogueX.recent_history.append("no_foot")
    $ RogueX.daily_history.append("no_foot")
    $ approval_bonus = 0
    return


label Rogue_FJ_Prep:
    if offhand_action == "foot":
        return

    if Taboo:
        $ RogueX.inhibition += int(Taboo/10)
        $ RogueX.lust += int(Taboo/5)

    $ RogueX.change_face("sexy")
    if RogueX.Forced:
        $ RogueX.change_face("sad")
    elif not RogueX.action_counter["footjob"]:
        $ RogueX.brows = "confused"
        $ RogueX.eyes = "sexy"
        $ RogueX.mouth = "smile"

    call Seen_First_Peen (RogueX, Partner, React=action_context)

    if not RogueX.action_counter["footjob"]:
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -20)
            $ RogueX.change_stat("obedience", 70, 25)
            $ RogueX.change_stat("inhibition", 80, 30)
        else:
            $ RogueX.change_stat("love", 90, 5)
            $ RogueX.change_stat("obedience", 70, 20)
            $ RogueX.change_stat("inhibition", 80, 20)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ RogueX.DrainWord("no_taboo")
    $ RogueX.DrainWord("no_foot")
    $ RogueX.recent_history.append("foot")
    $ RogueX.daily_history.append("foot")
    call Rogue_Sex_Launch ("foot")

label Rogue_FJ_Cycle:
    while Round > 0:
        call Rogue_Sex_Launch ("foot")
        call shift_focus (RogueX)
        $ RogueX.lust_face()

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

                    $ RogueX.pose = "doggy" if RogueX.pose != "doggy" else "sex"
                    "You turn her around. . ."
                    jump Rogue_FJ_Cycle
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
                                    "How about a blowjob?":
                                        if RogueX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Rogue_FJ_After
                                            call Rogue_Blowjob
                                        else:
                                            call Sex_Basic_Dialog (RogueX, "tired")
                                    "How about a handjob?":
                                        if RogueX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Rogue_FJ_After
                                            call Rogue_Handjob
                                        else:
                                            call Sex_Basic_Dialog (RogueX, "tired")
                                    "How about a titjob?":

                                        if RogueX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Rogue_FJ_After
                                            call Rogue_Titjob
                                        else:
                                            call Sex_Basic_Dialog (RogueX, "tired")
                                    "Never Mind":

                                        jump Rogue_FJ_Cycle
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
                                    jump Rogue_FJ_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Rogue_FJ_Cycle
                                "Never mind":
                                    jump Rogue_FJ_Cycle
                        "Undress [RogueX.name]":
                            call Girl_Undress (RogueX)
                        "Clean up [RogueX.name] (locked)" if not RogueX.Spunk:
                            pass
                        "Clean up [RogueX.name]" if RogueX.Spunk:
                            call Girl_Cleanup (RogueX, "ask")
                        "Never mind":
                            jump Rogue_FJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Rogue_Doggy_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Rogue_FJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Rogue_Doggy_Reset
                    $ Line = 0
                    jump Rogue_FJ_After


        call shift_focus (RogueX)
        call Sex_Dialog (RogueX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or RogueX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (RogueX)
                if "angry" in RogueX.recent_history:
                    call Rogue_Doggy_Reset
                    return
                $ RogueX.change_stat("lust", 200, 5)
                if 100 > RogueX.lust >= 70 and RogueX.session_orgasms < 2:
                    $ RogueX.recent_history.append("unsatisfied")
                    $ RogueX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Rogue_FJ_After
                $ Line = "came"

            if RogueX.lust >= 100:

                call Girl_Cumming (RogueX)
                if action_context == "shift" or "angry" in RogueX.recent_history:
                    jump Rogue_FJ_After

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
                            jump Rogue_FJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if counter == 20:
            $ RogueX.brows = "angry"
            menu:
                ch_r "Ow, i'm not used to this. Mind if we take a break?"
                "How about a BJ?" if RogueX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Rogue_FJ_After
                    call Rogue_Blowjob
                "How about a Handy?" if RogueX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Rogue_FJ_After
                    call Rogue_Handjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    $ counter += 1
                    "[Line]"
                    jump Rogue_FJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Rogue_Doggy_Reset
                    $ action_context = "shift"
                    jump Rogue_FJ_After
                "No, get back down there.":
                    if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):
                        $ RogueX.change_stat("love", 200, -5)
                        $ RogueX.change_stat("obedience", 50, 3)
                        $ RogueX.change_stat("obedience", 80, 2)
                        "She grumbles but gets back to work."
                    else:
                        $ RogueX.change_face("angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        ch_r "Well if that's your attitude you can handle your own business."
                        $ RogueX.change_stat("love", 50, -3, 1)
                        $ RogueX.change_stat("love", 80, -4, 1)
                        $ RogueX.change_stat("obedience", 30, -1, 1)
                        $ RogueX.change_stat("obedience", 50, -1, 1)
                        $ RogueX.recent_history.append("angry")
                        $ RogueX.daily_history.append("angry")
                        jump Rogue_FJ_After
        elif counter == 10 and RogueX.SEXP <= 100 and not ApprovalCheck(RogueX, 1200, "LO"):
            $ RogueX.brows = "confused"
            ch_r "Can we be done with this now? I'm getting sore."


        call Escalation (RogueX)

        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."


    $ RogueX.change_face("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.player_petname], that's enough of that for now."

label Rogue_FJ_After:
    $ RogueX.change_face("sexy")

    $ RogueX.action_counter["footjob"] += 1
    $ RogueX.remaining_actions -=1
    $ RogueX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ RogueX.addiction_rate += 1
    $ RogueX.change_stat("lust", 90, 5)

    call Partner_Like (RogueX, 1)

    if "Roguepedi" in Achievements:
        pass
    elif RogueX.action_counter["footjob"] >= 10:
        $ RogueX.change_face("smile", 1)
        ch_r "I guess I've gotten used to this foot thing."
        $ Achievements.append("Roguepedi")
        $ RogueX.SEXP += 5
    elif RogueX.action_counter["footjob"] == 1:
        $ RogueX.SEXP += 10
        if RogueX.love >= 500:
            $ RogueX.mouth = "smile"
            ch_r "That was a real interesting experience. . ."
        elif Player.focus <= 20:
            $ RogueX.mouth = "sad"
            ch_r "Did that work for you?"
    elif RogueX.action_counter["footjob"] == 5:
        ch_r "I kinda like this sensation."
        ch_r "Never thought about touching people with my feet."

    $ approval_bonus = 0
    if action_context == "shift":
        ch_r "Mmm, so what else did you have in mind?"
    else:
        call Rogue_Doggy_Reset
    call checkout
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
