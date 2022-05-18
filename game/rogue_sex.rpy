
label Rogue_SexAct(Act=0):
    if AloneCheck(RogueX) and RogueX.Taboo == 20:
        $ RogueX.Taboo = 0
        $ Taboo = 0
    call shift_focus (RogueX)
    if Act == "SkipTo":
        $ renpy.pop_call()
        $ renpy.pop_call()

        call SkipTo (RogueX)
    elif Act == "switch":
        $ renpy.pop_call()


    elif Act == "masturbate":
        call Rogue_M_Prep
        if not action_context:
            return
    elif Act == "lesbian":
        call Les_Prep (RogueX)
        if not action_context:
            return
    elif Act == "kiss":
        call KissPrep (RogueX)
        if not action_context:
            return
    elif Act == "breasts":
        call Rogue_Fondle_Breasts
        if not action_context:
            return
    elif Act == "blowjob":
        call Rogue_BJ_Prep
        if not action_context:
            return
    elif Act == "handjob":
        call Rogue_HJ_Prep
        if not action_context:
            return
    elif Act == "sex":
        call Rogue_SexPrep
        if not action_context:
            return


label Rogue_Masturbate:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (RogueX)
    if RogueX.action_counter["masturbation"]:
        $ approval_bonus += 10
    if RogueX.SEXP >= 50:
        $ approval_bonus += 25
    elif RogueX.SEXP >= 30:
        $ approval_bonus += 15
    elif RogueX.SEXP >= 15:
        $ approval_bonus += 5
    if RogueX.lust >= 90:
        $ approval_bonus += 20
    elif RogueX.lust >= 75:
        $ approval_bonus += 5
    if "exhibitionist" in RogueX.traits:
        $ approval_bonus += (3*Taboo)
    if RogueX in Player.Harem or "sex friend" in RogueX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in RogueX.traits:
        $ approval_bonus -= 40
    if RogueX.event_counter["forced"] and not RogueX.Forced:
        $ approval_bonus -= 5*RogueX.event_counter["forced"]

    $ approval = approval_check(RogueX, 1200, TabM = 2)

    $ RogueX.drain_word("unseen",1,0)

    if action_context == "join":
        if approval > 1 or (approval and RogueX.lust >= 50):
            $ Player.add_word(1,"join")
            menu:
                extend ""
                "Would you like some help? I could lend some helping hands. . ." if Player.semen and RogueX.remaining_actions:
                    $ RogueX.change_stat("love", 90, 1)
                    $ RogueX.change_stat("obedience", 50, 2)
                    $ RogueX.change_face("_sexy")
                    ch_r "Well, [RogueX.player_petname], I suppose I could use some help with these. . ."
                    $ RogueX.change_stat("obedience", 70, 2)
                    $ RogueX.change_stat("inhibition", 70, 1)
                    $ offhand_action = "fondle_breasts"
                    $ RogueX.action_counter["masturbation"] += 1
                    jump Rogue_M_Cycle
                "Would you like some help? I could. . . up to you, I guess." if Player.semen and RogueX.remaining_actions:
                    $ RogueX.change_stat("love", 70, 2)
                    $ RogueX.change_stat("love", 90, 1)
                    $ RogueX.change_face("_sexy")
                    ch_r "Well, [RogueX.player_petname], I suppose you could help me with these. . ."
                    $ RogueX.change_stat("obedience", 70, 2)
                    $ RogueX.change_stat("inhibition", 70, 1)
                    $ D20 = renpy.random.randint(1, 20)
                    if D20 > 10:
                        $ offhand_action = "fondle_breasts"
                    else:
                        $ offhand_action = "suck_breasts"
                    $ RogueX.action_counter["masturbation"] += 1
                    jump Rogue_M_Cycle
                "Why don't we take care of each other?" if Player.semen and RogueX.remaining_actions:
                    $ RogueX.change_face("_sexy")
                    ch_r "Well what did you have in mind?"
                    $ renpy.pop_call()
                    return
                "You look like you have things well in hand. . .":
                    if RogueX.lust >= 50:
                        $ RogueX.change_stat("love", 70, 2)
                        $ RogueX.change_stat("love", 90, 1)
                        $ RogueX.change_face("_sexy")
                        ch_r "Well, [RogueX.player_petname], I suppose I do at that . ."
                        $ RogueX.change_stat("obedience", 80, 3)
                        $ RogueX.change_stat("inhibition", 80, 5)
                        jump Rogue_M_Cycle
                    elif approval_check(RogueX, 1000):
                        $ RogueX.change_face("_sly")
                        ch_r "Well I did, but I think I've got it taken care of for now. . ."
                    else:
                        $ RogueX.change_face("_angry")
                        ch_r "Well I did, but now you've blown the mood."


        $ RogueX.ArmPose = 1
        $ RogueX.change_outfit(Changed=0)
        $ RogueX.remaining_actions -= 1
        $ Player.change_stat("focus", 50, 30)
        call checkout (1)
        $ Line = 0
        $ action_context = 0
        $ renpy.pop_call()
        if approval:
            $ RogueX.change_face("_bemused", 2)
            if bg_current == "bg_rogue":
                ch_r "So what did you come over for anyway, [RogueX.player_petname]?"
            else:
                ch_r "So . . . fancy bumping into you here, [RogueX.player_petname]. . ."
            $ RogueX.blushing = "_blush1"
        else:
            $ RogueX.change_stat("love", 200, -5)
            $ RogueX.change_face("_angry")
            $ RogueX.recent_history.append("_angry")
            $ RogueX.daily_history.append("_angry")
            if bg_current == "bg_rogue":
                ch_r "Well if you don't mind, I'd kind of appreciate you getting out of here. Maybe knock next time?"
                "[RogueX.name] kicks you out of her room."
                $ renpy.pop_call()
                jump Campus_Map
            else:
                ch_r "Well if you don't mind, I'm getting out of here. Maybe knock next time?"
                call Remove_Girl (RogueX)
        return




    if action_context == RogueX:
        if approval > 2:
            if RogueX.PantsNum() == 5:
                "[RogueX.name]'s hand snakes down her body, and hikes up her skirt."
                $ RogueX.upskirt = 1
            elif RogueX.PantsNum() > 6:
                "[RogueX.name] slides her hand down her body and into her jeans."
            elif RogueX.HoseNum() >= 5:
                "[RogueX.name]'s hand slides down her body and under her [RogueX.hose]."
            elif RogueX.underwear:
                "[RogueX.name]'s hand slides down her body and under her [RogueX.underwear]."
            else:
                "[RogueX.name]'s hand slides down her body and begins to caress her pussy."
            $ RogueX.SeenPanties = 1
            "She starts to slowly rub herself."
            call Rogue_First_Bottomless
            menu:
                "What do you do?"
                "Nothing.":
                    $ RogueX.change_stat("inhibition", 80, 3)
                    $ RogueX.change_stat("inhibition", 60, 2)
                    "[RogueX.name] begins to masturbate."
                "Go for it.":
                    $ RogueX.change_face("sexy, 1")
                    $ RogueX.change_stat("inhibition", 80, 3)
                    ch_p "That is so sexy, [RogueX.petname]."
                    $ RogueX.nameCheck()
                    "You lean back and enjoy the show."
                    $ RogueX.change_stat("love", 80, 1)
                    $ RogueX.change_stat("obedience", 90, 1)
                    $ RogueX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ RogueX.change_face("_surprised")
                    $ RogueX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that right now, [RogueX.petname]."
                    $ RogueX.nameCheck()
                    "[RogueX.name] pulls her hands away from herself."
                    $ RogueX.change_outfit(Changed=0)
                    $ RogueX.change_stat("obedience", 90, 1)
                    $ RogueX.change_stat("obedience", 50, 1)
                    $ RogueX.change_stat("obedience", 30, 2)
                    return
            jump Rogue_M_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
        return



    if not RogueX.action_counter["masturbation"]:
        $ RogueX.change_face("_surprised", 1)
        $ RogueX.mouth = "_kiss"
        ch_r "You want me to get myself off, while you watch?"
        if RogueX.Forced:
            $ RogueX.change_face("_sad")
            ch_r "So you just want to watch then?"



    if not RogueX.action_counter["masturbation"] and approval:
        if RogueX.Forced:
            $ RogueX.change_face("_sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
        elif RogueX.love >= (RogueX.obedience + RogueX.inhibition):
            $ RogueX.change_face("_sexy")
            $ RogueX.brows = "_sad"
            $ RogueX.mouth = "_smile"
            ch_r "Since my love life's been a bit. . . limited, I've gotten pretty good at this."
        elif RogueX.obedience >= RogueX.inhibition:
            $ RogueX.change_face("_normal")
            ch_r "If that's what you want, [RogueX.player_petname]. . ."
        else:
            $ RogueX.change_face("_sad")
            $ RogueX.mouth = "_smile"
            ch_r "I guess it could be fun with you watching. . ."



    elif approval:
        if RogueX.Forced:
            $ RogueX.change_face("_sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
            ch_r "You want to watch me again?"
        elif approval and "masturbation" in RogueX.recent_history:
            $ RogueX.change_face("_sexy", 1)
            ch_r "I guess I have a bit more in me. . ."
            jump Rogue_M_Prep
        elif approval and "masturbation" in RogueX.daily_history:
            $ RogueX.change_face("_sexy", 1)
            $ Line = renpy.random.choice(["You enjoyed the show?",
                    "Didn't get enough earlier?",
                    "It is nice to have an audience. . ."])
            ch_r "[Line]"
        elif RogueX.action_counter["masturbation"] < 3:
            $ RogueX.change_face("_sexy", 1)
            $ RogueX.brows = "_confused"
            ch_r "You like to watch, huh?"
        else:
            $ RogueX.change_face("_sexy", 1)
            $ RogueX.ArmPose = 2
            $ Line = renpy.random.choice(["You sure do like to watch.",
                    "So you'd like me to go again?",
                    "You want to watch some more?",
                    "You want me ta diddle myself?"])
            ch_r "[Line]"
            $ Line = 0



    if approval >= 2:
        if RogueX.Forced:
            $ RogueX.change_face("_sad")
            $ RogueX.change_stat("obedience", 90, 1)
            $ RogueX.change_stat("inhibition", 60, 1)
            ch_r "I suppose, let me get comfortable. . ."
        else:
            $ RogueX.change_face("_sexy", 1)
            $ RogueX.change_stat("love", 90, 1)
            $ RogueX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well. . . ok.",
                    "I suppose it would help to have something nice to look at. . .",
                    "I've kind of needed this anyways. . .",
                    "Sure!",
                    "I guess I could. . . give it a go.",
                    "Heh, ok, ok."])
            ch_r "[Line]"
            $ Line = 0
        $ RogueX.change_stat("obedience", 20, 1)
        $ RogueX.change_stat("obedience", 60, 1)
        $ RogueX.change_stat("inhibition", 70, 2)
        jump Rogue_M_Prep
    else:


        menu:
            ch_r "That's. . . a little intimate, [RogueX.player_petname]."
            "Maybe later?":
                $ RogueX.change_face("_sexy", 1)
                if RogueX.lust > 50:
                    ch_r "Well, definitely later. . . but I'll have to think about inviting you."
                else:
                    ch_r "Hmm, maybe. . . I'll let you know."
                $ RogueX.change_stat("love", 80, 2)
                $ RogueX.change_stat("inhibition", 70, 2)
                return
            "You look like you could use it. . .":
                if approval:
                    $ RogueX.change_face("_sexy")
                    $ RogueX.change_stat("obedience", 90, 2)
                    $ RogueX.change_stat("obedience", 50, 2)
                    $ RogueX.change_stat("inhibition", 70, 3)
                    $ RogueX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Well. . . ok.",
                            "I suppose it would help to have something nice to look at. . .",
                            "I've kind of needed this anyways. . .",
                            "Sure!",
                            "I guess I could. . . give it a go.",
                            "Heh, ok, ok."])
                    ch_r "[Line]"
                    $ Line = 0
                    jump Rogue_M_Prep
            "Just get at it already.":

                $ approval = approval_check(RogueX, 450, "OI", TabM = 2)
                if approval > 1 or (approval and RogueX.Forced):
                    $ RogueX.change_face("_sad")
                    $ RogueX.change_stat("love", 70, -5, 1)
                    $ RogueX.change_stat("love", 200, -5)
                    ch_r "Ok, fine. I'll give it a try."
                    $ RogueX.change_stat("obedience", 80, 4)
                    $ RogueX.change_stat("inhibition", 80, 1)
                    $ RogueX.change_stat("inhibition", 60, 3)
                    $ RogueX.Forced = 1
                    jump Rogue_M_Prep
                else:
                    $ RogueX.change_stat("love", 200, -20)
                    $ RogueX.recent_history.append("_angry")
                    $ RogueX.daily_history.append("_angry")



    $ RogueX.ArmPose = 1
    if RogueX.Forced:
        $ RogueX.change_face("_angry", 1)
        ch_r "I'm not doing something so. . . intimate with you watching."
        $ RogueX.change_stat("lust", 90, 5)
        if RogueX.love > 300:
            $ RogueX.change_stat("love", 70, -2)
        $ RogueX.change_stat("obedience", 50, -2)
        $ RogueX.recent_history.append("_angry")
        $ RogueX.daily_history.append("_angry")
        $ RogueX.recent_history.append("no_masturbation")
        $ RogueX.daily_history.append("no_masturbation")
        return
    elif Taboo:
        $ RogueX.change_face("_angry", 1)
        $ RogueX.daily_history.append("no_taboo")
        ch_r "I can't do that here!"
        $ RogueX.change_stat("lust", 90, 5)
        $ RogueX.change_stat("obedience", 50, -3)
        return
    elif RogueX.action_counter["masturbation"]:
        $ RogueX.change_face("_sad")
        ch_r "Nope, not anymore, you'll have to go back to Internet porn."
    else:
        $ RogueX.change_face("_normal", 1)
        ch_r "Heh, no, I'm not doing that."
    $ RogueX.recent_history.append("no_masturbation")
    $ RogueX.daily_history.append("no_masturbation")
    $ approval_bonus = 0
    return

label Rogue_M_Prep:
    $ RogueX.upskirt = 1
    $ RogueX.underwear_pulled_down = 1
    call Rogue_First_Bottomless (1)
    call set_the_scene (Dress=0)


    if "unseen" in RogueX.recent_history:
        $ RogueX.change_face("_sexy")
        $ RogueX.eyes = "_closed"
        $ RogueX.ArmPose = 2
        "You see [RogueX.name] leaning back, masturbating. You don't think she's noticed you yet."
    else:
        $ RogueX.change_face("_sexy")
        $ RogueX.ArmPose = 2
        "[RogueX.name] lays back and starts to toy with herself."
        if not RogueX.action_counter["masturbation"]:
            if RogueX.Forced:
                $ RogueX.change_stat("love", 90, -20)
                $ RogueX.change_stat("obedience", 70, 45)
                $ RogueX.change_stat("inhibition", 80, 35)
            else:
                $ RogueX.change_stat("love", 90, 15)
                $ RogueX.change_stat("obedience", 70, 35)
                $ RogueX.change_stat("inhibition", 80, 40)


    $ primary_action = "masturbation"
    if not girl_offhand_action:
        $ girl_offhand_action = "fondle_pussy"

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    if Taboo:
        $ RogueX.drain_word("no_taboo")
    $ RogueX.drain_word("no_masturbation")
    $ RogueX.recent_history.append("masturbation")
    $ RogueX.daily_history.append("masturbation")

label Rogue_M_Cycle:
    if action_context == "join":

        $ renpy.pop_call()
        $ action_context = 0

    while Round > 0:
        call Rogue_Pos_Reset ("masturbation")
        call shift_focus (RogueX)
        $ RogueX.lust_face
        if "unseen" in RogueX.recent_history:
            $ RogueX.eyes = "_closed"

        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if Player.focus < 100:

            menu:
                "Keep Watching.":
                    pass

                "[RogueX.name]. . .[[jump in]" if "unseen" not in RogueX.recent_history and "join" not in Player.recent_history and RogueX.location == bg_current:
                    "[RogueX.name] slows what she's doing with a sly grin."
                    ch_r "Yeah, did you want something, [RogueX.player_petname]?"
                    $ action_context = "join"
                    call Rogue_Masturbate
                "\"Ahem. . .\"" if "unseen" in RogueX.recent_history:
                    jump Rogue_M_Interupted

                "Start jack'in it." if offhand_action != "jackin":
                    call Jackin (RogueX)
                "Stop jack'in it." if offhand_action == "jackin":
                    $ offhand_action = 0

                "Slap her ass" if RogueX.location == bg_current:
                    if "unseen" in RogueX.recent_history:
                        "You smack [RogueX.name] firmly on the ass!"
                        jump Rogue_M_Interupted
                    else:
                        call Slap_Ass (RogueX)
                        $ counter += 1
                        $ Round -= 1
                        jump Rogue_M_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "Change what I'm doing":

                    menu:
                        "Offhand action" if RogueX.location == bg_current:
                            if RogueX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ RogueX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (RogueX, "tired")

                        "Threesome actions (locked)" if not Partner or "unseen" in RogueX.recent_history or RogueX.location == bg_current:
                            pass
                        "Threesome actions" if RogueX.location == bg_current and Partner and "unseen" not in RogueX.recent_history:
                            menu:
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (RogueX)
                                "Swap to [Partner.name]":
                                    call primary_action_Swap (RogueX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Rogue_M_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Rogue_M_Cycle
                                "Never mind":
                                    jump Rogue_M_Cycle

                        "Show her feet" if not ShowFeet and (RogueX.pose == "doggy" or RogueX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (RogueX.pose == "doggy" or RogueX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [RogueX.name]":

                            if "unseen" in RogueX.recent_history:
                                ch_p "Oh, yeah, take it off. . ."
                                jump Rogue_M_Interupted
                            else:
                                call Girl_Undress (RogueX)
                        "Clean up [RogueX.name] (locked)" if not RogueX.spunk:
                            pass
                        "Clean up [RogueX.name]" if RogueX.spunk:
                            if "unseen" in RogueX.recent_history:
                                ch_p "You've got a little something on you. . ."
                                jump Rogue_M_Interupted
                            else:
                                call Girl_Cleanup (RogueX, "ask")
                        "Never mind":
                            jump Rogue_M_Cycle

                "Back to Sex Menu" if multi_action and RogueX.location == bg_current:
                    ch_p "Let's try something else."
                    call Rogue_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Rogue_M_Interupted
                "End Scene" if not multi_action or RogueX.location != bg_current:
                    ch_p "Let's stop for now."
                    call Rogue_Pos_Reset
                    $ Line = 0
                    jump Rogue_M_Interupted


        call shift_focus (RogueX)
        call Sex_Dialog (RogueX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus

        if Player.focus >= 100 or RogueX.lust >= 100:

            if Player.focus >= 100:
                if "unseen" not in RogueX.recent_history:

                    call Player_Cumming (RogueX)
                    if "_angry" in RogueX.recent_history:
                        call Rogue_Pos_Reset
                        return
                    $ RogueX.change_stat("lust", 200, 5)
                    if 100 > RogueX.lust >= 70 and RogueX.session_orgasms < 2:
                        $ RogueX.recent_history.append("unsatisfied")
                        $ RogueX.daily_history.append("unsatisfied")
                    $ Line = "came"
                else:
                    "You grunt and try to hold it in."
                    $ Player.focus = 95
                    if RogueX.location == bg_current:
                        jump Rogue_M_Interupted


            if RogueX.lust >= 100:
                call Girl_Cumming (RogueX)
                if RogueX.location == bg_current:
                    jump Rogue_M_Interupted

            if Line == "came":
                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."
                    $ offhand_action = 0 if offhand_action == "jackin" else offhand_action


                if "unsatisfied" in RogueX.recent_history:
                    "[RogueX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Let her keep going?"
                        "Yes, keep going for a bit.":
                            $ Line = "You let her get back into it"
                            jump Rogue_M_Cycle
                        "No, I'm done.":
                            "You ask her to stop."
                            return
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        if "unseen" in RogueX.recent_history:
            if Round == 10:
                "It's getting a bit late, [RogueX.name] will probably be wrapping up soon."
            elif Round == 5:
                "She's definitely going to stop soon."
        else:
            if RogueX.location == bg_current:
                call Escalation (RogueX)

            if Round == 10:
                ch_r "We might want to wrap this up, it's getting late."
                $ RogueX.lust += 10
            elif Round == 5:
                ch_r "Seriously, it'll be time to stop soon."
                $ RogueX.lust += 25


    $ RogueX.change_face("_bemused", 0)
    $ Line = 0
    if "unseen" not in RogueX.recent_history:
        ch_r "Ok, [RogueX.player_petname], that's enough of that for now."

label Rogue_M_Interupted:


    if "unseen" in RogueX.recent_history:
        $ RogueX.change_face("_surprised", 1)
        "[RogueX.name] stops what she's doing with a start, eyes wide."
        call Rogue_First_Bottomless (1)
        $ RogueX.change_face("_surprised", 1)


        if offhand_action == "jackin":
            ch_r "H- how long you been stand'in there, [RogueX.player_petname]?"
            $ RogueX.eyes = "_down"
            menu:
                ch_r "And why is your cock out like that?!"
                "Long enough, it was an excellent show.":
                    $ RogueX.change_face("_sexy")
                    $ RogueX.change_stat("obedience", 50, 3)
                    $ RogueX.change_stat("obedience", 70, 2)
                    ch_r "Well, I imagine it was. . ."
                    if RogueX.love >= 800 or RogueX.obedience >= 500 or RogueX.inhibition >= 500:
                        $ approval_bonus += 10
                        $ RogueX.change_stat("lust", 90, 5)
                        ch_r "And the view from this angle ain't so bad either. . ."
                "I. . . just got here?":

                    $ RogueX.change_face("_angry")
                    $ RogueX.change_stat("love", 70, 2)
                    $ RogueX.change_stat("love", 90, 1)
                    $ RogueX.change_stat("obedience", 50, 2)
                    $ RogueX.change_stat("obedience", 70, 2)
                    "She looks pointedly at your cock,"
                    ch_r "A likely story . . ."
                    if RogueX.love >= 800 or RogueX.obedience >= 500 or RogueX.inhibition >= 500:
                        $ approval_bonus += 10
                        $ RogueX.change_stat("lust", 90, 5)
                        $ RogueX.change_face("_bemused", 1)
                        ch_r "Still, can't blame a fella for take'in inspirations."
                    else:
                        $ approval_bonus -= 10
                        $ RogueX.change_stat("lust", 200, -5)
            call Seen_First_Peen (RogueX, Partner)
            ch_r "Hmm. . ."
        else:


            ch_r "H- how long you been stand'in there, [RogueX.player_petname]?"
            menu:
                extend ""
                "Long enough.":
                    $ RogueX.change_face("_sexy", 1)
                    $ RogueX.change_stat("obedience", 50, 3)
                    $ RogueX.change_stat("obedience", 70, 2)
                    ch_r "Well I hope you got a good show out of it. . ."
                "I just got here.":
                    $ RogueX.change_face("_bemused", 1)
                    $ RogueX.change_stat("love", 70, 2)
                    $ RogueX.change_stat("love", 90, 1)
                    ch_r "A likely story . . ."
                    $ RogueX.change_stat("obedience", 50, 2)
                    $ RogueX.change_stat("obedience", 70, 2)

        $ RogueX.drain_word("unseen",1,0)
        $ RogueX.action_counter["masturbation"] += 1
        if Round <= 10:
            ch_r "It's getting too late to do much about it right now though."
            return
        $ action_context = "join"
        call Rogue_Masturbate
        "error: report this if you see it."
        return



    $ RogueX.remaining_actions -= 1
    $ RogueX.action_counter["masturbation"] += 1

    if Partner == EmmaX:
        call Partner_Like (RogueX, 4)
    else:
        call Partner_Like (RogueX, 3)
    call checkout
    if action_context == "shift":
        $ action_context = 0
        return
    $ action_context = 0

    if RogueX.location != bg_current:
        return

    if Round <= 10:
        ch_r "I need to take a little break here, [RogueX.player_petname]."
        return
    $ RogueX.change_face("_sexy", 1)
    if RogueX.lust < 20:
        ch_r "That really worked for me, [RogueX.player_petname]. How about you?"
    else:
        ch_r "Yeah, what did you want?"
    menu:
        extend ""
        "Well, I have something you could take care of. . ." if Player.semen and RogueX.remaining_actions:
            $ action_context = "shift"
            return
        "You could just keep going. . ." if Player.semen:
            $ RogueX.change_face("_sly")
            if RogueX.remaining_actions and Round >= 10:
                ch_r "Well, alright. . ."
                jump Rogue_M_Cycle
            else:
                ch_r "I'm kinda worn out, maybe time for a break. . ."
        "I'm good here. [[Stop]":
            if RogueX.love < 800 and RogueX.inhibition < 500 and RogueX.obedience < 500:
                $ RogueX.change_outfit(Changed=0)
            $ RogueX.change_face("_normal")
            $ RogueX.brows = "_confused"
            ch_r "Well. . . ok then. . ."
            $ RogueX.brows = "_normal"
        "You should probably stop for now." if RogueX.lust > 30:
            $ RogueX.change_face("_angry")
            ch_r "Well if you say so."
    return





image AssBase:
    "images/RogueDoggy/Rogue_Doggy_Ass.png"

image Dildo_Animation:
    contains:
        "UI_Dildo"
        block:
            ease 1 pos (100,300)
            ease 1 pos (100,400)
            repeat

image AssTest:

    AlphaMask("Dildo_Animation", "AssBase")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
