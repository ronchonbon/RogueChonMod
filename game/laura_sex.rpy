
label Laura_SexAct(Act=0):
    if AloneCheck(LauraX) and LauraX.Taboo == 20:
        $ LauraX.Taboo = 0
        $ Taboo = 0
    call shift_focus (LauraX)
    if Act == "SkipTo":
        $ renpy.pop_call()
        $ renpy.pop_call()

        call SkipTo (LauraX)
    elif Act == "switch":
        $ renpy.pop_call()


    elif Act == "masturbate":
        call Laura_M_Prep
        if not action_context:
            return
    elif Act == "lesbian":
        call Les_Prep (LauraX)
        if not action_context:
            return
    elif Act == "kissing":
        call KissPrep (LauraX)
        if not action_context:
            return
    elif Act == "breasts":
        call Laura_Fondle_Breasts
        if not action_context:
            return
    elif Act == "blowjob":
        call Laura_BJ_Prep
        if not action_context:
            return
    elif Act == "handjob":
        call Laura_HJ_Prep
        if not action_context:
            return
    elif Act == "sex":
        call Laura_SexPrep
        if not action_context:
            return





label Laura_Masturbate:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (LauraX)
    if LauraX.action_counter["masturbation"]:
        $ approval_bonus += 10
    if LauraX.SEXP >= 50:
        $ approval_bonus += 25
    elif LauraX.SEXP >= 30:
        $ approval_bonus += 15
    elif LauraX.SEXP >= 15:
        $ approval_bonus += 5
    if LauraX.lust >= 90:
        $ approval_bonus += 20
    elif LauraX.lust >= 75:
        $ approval_bonus += 5
    if "exhibitionist" in LauraX.traits:
        $ approval_bonus += (3*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in LauraX.traits:
        $ approval_bonus -= 40
    if LauraX.event_counter["forced"] and not LauraX.Forced:
        $ approval_bonus -= 5*LauraX.event_counter["forced"]

    $ approval = approval_check(LauraX, 1300, TabM = 2)

    $ LauraX.drain_word("unseen",1,0)

    if action_context == "join":
        $ Player.add_word(1,"join")
        if approval > 1 or (approval and LauraX.lust >= 50):
            menu:
                extend ""
                "Would you like some help? I could lend some helping hands. . ." if Player.semen and LauraX.remaining_actions:
                    $ LauraX.change_stat("love", 90, 1)
                    $ LauraX.change_stat("obedience", 50, 2)
                    $ LauraX.change_face("sexy")
                    ch_l "Huh. Well I guess you could work the top?"
                    $ LauraX.change_stat("obedience", 70, 2)
                    $ LauraX.change_stat("inhibition", 70, 1)
                    $ offhand_action = "fondle_breasts"
                    $ LauraX.action_counter["masturbation"] += 1
                    jump Laura_M_Cycle
                "Would you like some help? I could. . . up to you, I guess." if Player.semen and LauraX.remaining_actions:
                    $ LauraX.change_stat("love", 70, 2)
                    $ LauraX.change_stat("love", 90, 1)
                    $ LauraX.change_face("sexy")
                    ch_l "Yeah, I guess? . ."
                    $ LauraX.change_stat("obedience", 70, 2)
                    $ LauraX.change_stat("inhibition", 70, 1)
                    $ D20 = renpy.random.randint(1, 20)
                    if D20 > 10:
                        $ offhand_action = "fondle_breasts"
                    else:
                        $ offhand_action = "suck_breasts"
                    $ LauraX.action_counter["masturbation"] += 1
                    jump Laura_M_Cycle
                "Why don't we take care of each other?" if Player.semen and LauraX.remaining_actions:
                    $ LauraX.change_face("sexy")
                    ch_l "Like what?"
                    $ renpy.pop_call()
                    return
                "You look like you have things well in hand. . .":
                    if LauraX.lust >= 50:
                        $ LauraX.change_stat("love", 70, 2)
                        $ LauraX.change_stat("love", 90, 1)
                        $ LauraX.change_face("sexy")
                        ch_l "I am getting pretty close. . ."
                        $ LauraX.change_stat("obedience", 80, 3)
                        $ LauraX.change_stat("inhibition", 80, 5)
                        jump Laura_M_Cycle
                    elif approval_check(LauraX, 1200):
                        $ LauraX.change_face("sly")
                        ch_l "Yeah. . . but I can take a break. . ."
                    else:
                        $ LauraX.change_face("angry")
                        ch_l "-until you messed it up."


        $ LauraX.ArmPose = 1
        $ LauraX.change_outfit()
        $ LauraX.remaining_actions -= 1
        $ Player.change_stat("focus", 50, 30)
        call checkout (1)
        $ Line = 0
        $ action_context = 0
        $ renpy.pop_call()
        if approval:
            $ LauraX.change_face("bemused", 2)
            if bg_current == "bg_laura":
                ch_l "Why are you in my room?"
            else:
                ch_l "I wasn't expecting company. . ."
            $ LauraX.blushing = 1
        else:
            $ LauraX.change_stat("love", 200, -5)
            $ LauraX.change_face("angry")
            $ LauraX.recent_history.append("angry")
            $ LauraX.daily_history.append("angry")
            if bg_current == "bg_laura":
                ch_l "I was kinda busy, so get out."
                "[LauraX.name] kicks you out of her room."
                $ renpy.pop_call()
                jump Campus_Map
            else:
                ch_l "I'm getting out of here, but maybe knock next time."
                call Remove_Girl (LauraX)
        return




    if action_context == LauraX:
        if approval > 2:
            if LauraX.PantsNum() == 5:
                "[LauraX.name]'s hand snakes down her body, and hikes up her skirt."
                $ LauraX.upskirt = 1
            elif LauraX.PantsNum() >= 6:
                "[LauraX.name] slides her hand down her body and into her pants."
            elif LauraX.HoseNum() >= 5:
                "[LauraX.name]'s hand slides down her body and under her [LauraX.hose]."
            elif LauraX.underwear:
                "[LauraX.name]'s hand slides down her body and under her [LauraX.underwear]."
            else:
                "[LauraX.name]'s hand slides down her body and begins to caress her pussy."
            $ LauraX.SeenPanties = 1
            call Laura_First_Bottomless (1)
            "She starts to slowly rub herself."
            menu:
                "What do you do?"
                "Nothing.":
                    $ LauraX.change_stat("inhibition", 80, 3)
                    $ LauraX.change_stat("inhibition", 60, 2)
                    "[LauraX.name] begins to masturbate."
                "Go for it.":
                    $ LauraX.change_face("sexy, 1")
                    $ LauraX.change_stat("inhibition", 80, 3)
                    ch_p "That is so sexy, [LauraX.petname]."
                    $ LauraX.nameCheck()
                    "You lean back and enjoy the show."
                    $ LauraX.change_stat("love", 80, 1)
                    $ LauraX.change_stat("obedience", 90, 1)
                    $ LauraX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ LauraX.change_face("surprised")
                    $ LauraX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that right now, [LauraX.petname]."
                    $ LauraX.nameCheck()
                    "[LauraX.name] pulls her hands away from herself."
                    $ LauraX.change_outfit()
                    $ LauraX.change_stat("obedience", 90, 1)
                    $ LauraX.change_stat("obedience", 50, 1)
                    $ LauraX.change_stat("obedience", 30, 2)
                    return
            jump Laura_M_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
        return



    if not LauraX.action_counter["masturbation"]:
        $ LauraX.change_face("surprised", 1)
        $ LauraX.mouth = "kiss"
        ch_l "So you want me to masturbate while you watch?"
        if LauraX.Forced:
            $ LauraX.change_face("sad")
            ch_l "And you {i}just{/i} want to watch. . ."



    if not LauraX.action_counter["masturbation"] and approval:
        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
        elif LauraX.love >= LauraX.obedience and LauraX.love >= LauraX.inhibition:
            $ LauraX.change_face("sexy")
            $ LauraX.brows = "sad"
            $ LauraX.mouth = "smile"
            ch_l "I don't know, are you sure?"
        elif LauraX.obedience >= LauraX.inhibition:
            $ LauraX.change_face("normal")
            ch_l "If that's what you're into. . ."
        else:
            $ LauraX.change_face("sad")
            $ LauraX.mouth = "smile"
            ch_l "I do have some free time. . ."



    elif approval:
        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
            ch_l "Hmm, again?"
        elif approval and "masturbation" in LauraX.recent_history:
            $ LauraX.change_face("sexy", 1)
            ch_l "I have built up some more tension. . ."
            jump Laura_M_Prep
        elif approval and "masturbation" in LauraX.daily_history:
            $ LauraX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Did you enjoy that?",
                    "Didn't get enough earlier?",
                    "I liked having an audience. . ."])
            ch_l "[Line]"
        elif LauraX.action_counter["masturbation"] < 3:
            $ LauraX.change_face("sexy", 1)
            $ LauraX.brows = "confused"
            ch_l "Did you. . . like it last time?"
        else:
            $ LauraX.change_face("sexy", 1)
            $ LauraX.ArmPose = 2
            $ Line = renpy.random.choice(["You like to watch.",
                    "Again?",
                    "You really like to watch me.",
                    "You want me to masturbate again?"])
            ch_l "[Line]"
            $ Line = 0



    if approval >= 2:
        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("obedience", 90, 1)
            $ LauraX.change_stat("inhibition", 60, 1)
            ch_l "Whatever. . ."
        else:
            $ LauraX.change_face("sexy", 1)
            $ LauraX.change_stat("love", 90, 1)
            $ LauraX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Huh. Ok.",
                    "Couldn't hurt. . .",
                    "Alright.",
                    "Sure.",
                    "Heh, ok."])
            ch_l "[Line]"
            $ Line = 0
        $ LauraX.change_stat("obedience", 20, 1)
        $ LauraX.change_stat("obedience", 60, 1)
        $ LauraX.change_stat("inhibition", 70, 2)
        jump Laura_M_Prep
    else:


        menu:
            ch_l "I don't know that I want to do that right now."
            "Maybe later?":
                $ LauraX.change_face("sexy", 1)
                if LauraX.lust > 70:
                    ch_l "I probably will be, but not with an audience."
                else:
                    ch_l "Hmm, maybe. . ."
                $ LauraX.change_stat("love", 80, 2)
                $ LauraX.change_stat("inhibition", 70, 2)
                return
            "You look like you could use it. . .":
                if approval:
                    $ LauraX.change_face("sexy")
                    $ LauraX.change_stat("obedience", 90, 2)
                    $ LauraX.change_stat("obedience", 50, 2)
                    $ LauraX.change_stat("inhibition", 70, 3)
                    $ LauraX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Huh. Ok.",
                                "Couldn't hurt. . .",
                                "Allright.",
                                "Sure.",
                                "Heh, ok."])
                    ch_l "[Line]"
                    $ Line = 0
                    jump Laura_M_Prep
            "Just get at it already.":

                $ approval = approval_check(LauraX, 450, "OI", TabM = 2)
                if approval > 1 or (approval and LauraX.Forced):
                    $ LauraX.change_face("sad")
                    $ LauraX.change_stat("love", 70, -5, 1)
                    $ LauraX.change_stat("love", 200, -5)
                    ch_l "Whatever."
                    $ LauraX.change_stat("obedience", 80, 4)
                    $ LauraX.change_stat("inhibition", 80, 1)
                    $ LauraX.change_stat("inhibition", 60, 3)
                    $ LauraX.Forced = 1
                    jump Laura_M_Prep
                else:
                    $ LauraX.change_stat("love", 200, -20)
                    $ LauraX.recent_history.append("angry")
                    $ LauraX.daily_history.append("angry")



    $ LauraX.ArmPose = 1
    if LauraX.Forced:
        $ LauraX.change_face("angry", 1)
        ch_l "This is just too weird for me."
        $ LauraX.change_stat("lust", 90, 5)
        if LauraX.love > 300:
            $ LauraX.change_stat("love", 70, -2)
        $ LauraX.change_stat("obedience", 50, -2)
        $ LauraX.recent_history.append("angry")
        $ LauraX.daily_history.append("angry")
        $ LauraX.recent_history.append("no_masturbation")
        $ LauraX.daily_history.append("no_masturbation")
        return
    elif Taboo:
        $ LauraX.change_face("angry", 1)
        $ LauraX.daily_history.append("no_taboo")
        ch_l "I couldn't do that in public."
        $ LauraX.change_stat("lust", 90, 5)
        $ LauraX.change_stat("obedience", 50, -3)
        return
    elif LauraX.action_counter["masturbation"]:
        $ LauraX.change_face("sad")
        ch_l "I'm not into it right now."
    else:
        $ LauraX.change_face("normal", 1)
        ch_l "Um, no."
    $ LauraX.recent_history.append("no_masturbation")
    $ LauraX.daily_history.append("no_masturbation")
    $ approval_bonus = 0
    return

label Laura_M_Prep:
    $ LauraX.upskirt = 1
    $ LauraX.underwear_pulled_down = 1
    call Laura_First_Bottomless (1)
    call set_the_scene (Dress=0)


    if "unseen" in LauraX.recent_history:
        $ LauraX.change_face("sexy")
        $ LauraX.eyes = "closed"
        $ LauraX.ArmPose = 2
        "You see [LauraX.name] leaning back, masturbating. You don't think she's noticed you yet."
    else:
        $ LauraX.change_face("sexy")
        $ LauraX.ArmPose = 2
        "[LauraX.name] lays back and starts to toy with herself."
        if not LauraX.action_counter["masturbation"]:
            if LauraX.Forced:
                $ LauraX.change_stat("love", 90, -20)
                $ LauraX.change_stat("obedience", 70, 45)
                $ LauraX.change_stat("inhibition", 80, 35)
            else:
                $ LauraX.change_stat("love", 90, 15)
                $ LauraX.change_stat("obedience", 70, 35)
                $ LauraX.change_stat("inhibition", 80, 40)


    $ primary_action = "masturbation"
    if not girl_offhand_action:
        $ girl_offhand_action = "fondle_pussy"

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    if Taboo:
        $ LauraX.drain_word("no_taboo")
    $ LauraX.drain_word("no_masturbation")
    $ LauraX.recent_history.append("masturbation")
    $ LauraX.daily_history.append("masturbation")

label Laura_M_Cycle:
    if action_context == "join":
        $ renpy.pop_call()
        $ action_context = 0

    while Round > 0:
        call Laura_Pos_Reset ("masturbation")
        call shift_focus (LauraX)
        $ LauraX.lust_face()
        if "unseen" in LauraX.recent_history and LauraX.location == bg_current:
            $ LauraX.eyes = "closed"
            if LauraX.ScentTimer >= 3:
                $ LauraX.ScentTimer = 0
                "[LauraX.name]'s nose twitches and she seems to be sniffing the air."
                jump Laura_M_Interupted
            $ LauraX.ScentTimer += 1

        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if Player.focus < 100:

            menu:
                "Keep Watching.":
                    pass

                "[LauraX.name]. . .[[jump in]" if "unseen" not in LauraX.recent_history and "join" not in Player.recent_history and LauraX.location == bg_current:
                    "[LauraX.name] slows what she's doing with a sly grin."
                    ch_l "Are you enjoying this?"
                    $ action_context = "join"
                    call Laura_Masturbate
                "\"Ahem. . .\"" if "unseen" in LauraX.recent_history and LauraX.location == bg_current:
                    jump Laura_M_Interupted

                "Start jack'in it." if offhand_action != "jackin":
                    call Jackin (LauraX)
                "Stop jack'in it." if offhand_action == "jackin":
                    $ offhand_action = 0

                "Slap her ass" if LauraX.location == bg_current:
                    if "unseen" in LauraX.recent_history:
                        "You smack [LauraX.name] firmly on the ass!"
                        jump Laura_M_Interupted
                    else:
                        call Slap_Ass (LauraX)
                        $ counter += 1
                        $ Round -= 1
                        jump Laura_M_Cycle
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
                        "Offhand action" if LauraX.location == bg_current:
                            if LauraX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ LauraX.remaining_actions -= 1
                            else:
                                ch_l "Maybe we could finish this up for now?"

                        "Threesome actions (locked)" if not Partner or "unseen" in LauraX.recent_history or LauraX.location != bg_current:
                            pass
                        "Threesome actions" if Partner and "unseen" not in LauraX.recent_history and LauraX.location == bg_current:
                            menu:
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (LauraX)
                                "Swap to [Partner.name]":
                                    call primary_action_Swap (LauraX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Laura_M_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Laura_M_Cycle
                                "Never mind":
                                    jump Laura_M_Cycle

                        "Show her feet" if not ShowFeet and LauraX.pose == "doggy":
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and LauraX.pose == "doggy":
                            $ ShowFeet = 0
                        "Undress [LauraX.name]":

                            if "unseen" in LauraX.recent_history:
                                ch_p "Oh, yeah, take it off. . ."
                                jump Laura_M_Interupted
                            else:
                                call Girl_Undress (LauraX)
                        "Clean up [LauraX.name] (locked)" if not LauraX.spunk:
                            pass
                        "Clean up [LauraX.name]" if LauraX.spunk:
                            if "unseen" in LauraX.recent_history:
                                ch_p "You've got a little something on you. . ."
                                jump Laura_M_Interupted
                            else:
                                call Girl_Cleanup (LauraX, "ask")
                        "Never mind":
                            jump Laura_M_Cycle

                "Back to Sex Menu" if multi_action and LauraX.location == bg_current:
                    ch_p "Let's try something else."
                    call Laura_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Laura_M_Interupted
                "End Scene" if not multi_action or LauraX.location != bg_current:
                    ch_p "Let's stop for now."
                    call Laura_Pos_Reset
                    $ Line = 0
                    jump Laura_M_Interupted


        call shift_focus (LauraX)
        call Sex_Dialog (LauraX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus

        if Player.focus >= 100 or LauraX.lust >= 100:

            if Player.focus >= 100:
                if "unseen" not in LauraX.recent_history:

                    call Player_Cumming (LauraX)
                    if "angry" in LauraX.recent_history:
                        call Laura_Pos_Reset
                        return
                    $ LauraX.change_stat("lust", 200, 5)
                    if 100 > LauraX.lust >= 70 and LauraX.session_orgasms < 2:
                        $ LauraX.recent_history.append("unsatisfied")
                        $ LauraX.daily_history.append("unsatisfied")
                    $ Line = "came"
                else:
                    "You grunt and try to hold it in."
                    $ Player.focus = 95
                    if LauraX.location == bg_current:
                        jump Laura_M_Interupted


            if LauraX.lust >= 100:
                call Girl_Cumming (LauraX)
                if LauraX.location == bg_current:
                    jump Laura_M_Interupted

            if Line == "came":
                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."
                    $ offhand_action = 0 if offhand_action == "jackin" else offhand_action


                if "unsatisfied" in LauraX.recent_history:
                    "[LauraX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Let her keep going?"
                        "Yes, keep going for a bit.":
                            $ Line = "You let her get back into it"
                            jump Laura_M_Cycle
                        "No, I'm done.":
                            "You ask her to stop."
                            return
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        if "unseen" in LauraX.recent_history:
            if Round == 10:
                "It's getting a bit late, [LauraX.name] will probably be wrapping up soon."
            elif Round == 5:
                "She's definitely going to stop soon."
        else:
            if LauraX.location == bg_current:
                call Escalation (LauraX)

            if Round == 10:
                ch_l "We might want to wrap this up, it's getting late."
                $ LauraX.lust += 10
            elif Round == 5:
                ch_l "Five minutes, maybe."
                $ LauraX.lust += 25


    $ LauraX.change_face("bemused", 0)
    $ Line = 0
    if "unseen" not in LauraX.recent_history:
        ch_l "Ok, I'm kinda done for now, I need a break."

label Laura_M_Interupted:


    if "unseen" in LauraX.recent_history:
        $ LauraX.change_face("surprised", 2)
        "[LauraX.name] stops what she's doing with a start, eyes wide."
        call Laura_First_Bottomless (1)
        $ LauraX.change_face("surprised", 2)


        if offhand_action == "jackin":
            ch_l "Huh."
            ch_l "When did you get here?"
            $ LauraX.eyes = "down"
            menu:
                ch_l "And um. . . you have your penis out. . . "
                "A while back, it was an excellent show.":
                    $ LauraX.change_face("sexy",1)
                    $ LauraX.change_stat("obedience", 50, 3)
                    $ LauraX.change_stat("obedience", 70, 2)
                    ch_l "Really? Weird. . ."
                    if LauraX.love >= 800 or LauraX.obedience >= 500 or LauraX.inhibition >= 500:
                        $ approval_bonus += 10
                        $ LauraX.change_stat("lust", 90, 5)
                        ch_l "I um. . . you're not so bad yourself. . ."
                "I. . . just got here?":

                    $ LauraX.change_face("angry",1)
                    $ LauraX.change_stat("love", 70, 2)
                    $ LauraX.change_stat("love", 90, 1)
                    $ LauraX.change_stat("obedience", 50, 2)
                    $ LauraX.change_stat("obedience", 70, 2)
                    "She looks pointedly at your cock,"
                    ch_l "Long enough to whip that out?"
                    if LauraX.love >= 800 or LauraX.obedience >= 500 or LauraX.inhibition >= 500:
                        $ approval_bonus += 10
                        $ LauraX.change_stat("lust", 90, 5)
                        $ LauraX.change_face("bemused", 1)
                        ch_l "It was really that interesting?"
                    else:
                        $ approval_bonus -= 10
                        $ LauraX.change_stat("lust", 200, -5)
            call Seen_First_Peen (LauraX, Partner)
            ch_l "Hmm. . ."
        else:


            ch_l "Huh."
            ch_l "When did you get here?"
            menu:
                extend ""
                "A while back.":
                    $ LauraX.change_face("sexy", 1)
                    $ LauraX.change_stat("obedience", 50, 3)
                    $ LauraX.change_stat("obedience", 70, 2)
                    ch_l "I must have put on a show. . ."
                "I just got here.":
                    $ LauraX.change_face("bemused", 1)
                    $ LauraX.change_stat("love", 70, 2)
                    $ LauraX.change_stat("love", 90, 1)
                    ch_l "Uh-huh. . ."
                    $ LauraX.change_stat("obedience", 50, 2)
                    $ LauraX.change_stat("obedience", 70, 2)

        $ LauraX.drain_word("unseen",1,0)
        $ LauraX.action_counter["masturbation"] += 1
        if Round <= 10:
            ch_l "I kinda needed a break anyway. . ."
            return
        $ action_context = "join"
        call Laura_Masturbate
        "error: report this if you see it."
        return



    $ LauraX.remaining_actions -= 1
    $ LauraX.action_counter["masturbation"] += 1
    call checkout
    if action_context == "shift":
        $ action_context = 0
        return
    $ action_context = 0

    if Partner == EmmaX:
        call Partner_Like (LauraX, 3)
    else:
        call Partner_Like (LauraX, 2)

    if LauraX.location != bg_current:
        return

    if Round <= 10:
        ch_l "I need a minute here. . ."
        return
    $ LauraX.change_face("sexy", 1)
    if LauraX.lust < 20:
        ch_l "I guess that worked out, how about you?"
    else:
        ch_l "So, what next?"
    menu:
        extend ""
        "Well, I have something you could take care of. . ." if Player.semen and LauraX.remaining_actions:
            $ action_context = "shift"
            return
        "You could just keep going. . ." if Player.semen:
            $ LauraX.change_face("sly")
            if LauraX.remaining_actions and Round >= 10:
                ch_l "Ok. . ."
                jump Laura_M_Cycle
            else:
                ch_l "I need a minute here. . ."
        "I'm good here. [[Stop]":
            if LauraX.love < 800 and LauraX.inhibition < 500 and LauraX.obedience < 500:
                $ LauraX.change_outfit()
            $ LauraX.change_face("normal")
            $ LauraX.brows = "confused"
            ch_l "Ok."
            $ LauraX.brows = "normal"
        "You should probably stop for now." if LauraX.lust > 30:
            $ LauraX.change_face("angry")
            ch_l "Hrmm."
    return








label Laura_Sex_P:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (LauraX)
    if LauraX.action_counter["sex"] >= 7:
        $ approval_bonus += 15
    elif LauraX.action_counter["sex"] >= 3:
        $ approval_bonus += 12
    elif LauraX.action_counter["sex"]:
        $ approval_bonus += 10

    if LauraX.addiction >= 75 and (LauraX.event_counter["creampied"] + LauraX.event_counter["anal_creampied"]) >=3:
        $ approval_bonus += 20
    elif LauraX.addiction >= 75:
        $ approval_bonus += 15

    if LauraX.lust > 85:
        $ approval_bonus += 10
    elif LauraX.lust > 75:
        $ approval_bonus += 5

    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in LauraX.traits:
        $ approval_bonus += (4*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in LauraX.traits:
        $ approval_bonus -= 40
    if LauraX.event_counter["forced"] and not LauraX.Forced:
        $ approval_bonus -= 5*LauraX.event_counter["forced"]



    if Taboo and "no_taboo" in LauraX.daily_history:
        $ approval_bonus -= 10

    if "no_sex" in LauraX.daily_history:
        $ approval_bonus -= 15 if "no_sex" in LauraX.recent_history else 5


    $ approval = approval_check(LauraX, 1400, TabM = 5)

    if action_context == "auto":
        call Laura_Sex_Launch ("sex")
        if LauraX.PantsNum() == 5:
            "You push [LauraX.name] onto her back, sliding her skirt up as you go."
            $ LauraX.upskirt = 1
        elif LauraX.PantsNum() >= 6:
            "You push [LauraX.name] onto her back, sliding her pants down as you do."
            $ LauraX.upskirt = 1
        else:
            "You push [LauraX.name] onto her back."
        $ LauraX.SeenPanties = 1
        "You rub the tip of your cock against her moist slit."
        $ LauraX.change_face("surprised", 1)

        if (LauraX.action_counter["sex"] and approval) or (approval > 1):

            "[LauraX.name] glances down and then breaks into a smile."
            $ LauraX.change_face("sly")
            $ LauraX.change_stat("obedience", 70, 3)
            $ LauraX.change_stat("inhibition", 50, 3)
            $ LauraX.change_stat("inhibition", 70, 1)
            ch_l "Fine by me, [LauraX.player_petname]."
            jump Laura_SexPrep
        else:

            $ LauraX.brows = "angry"
            menu:
                ch_l "Oh, taking it all the way, are we?"
                "Sorry, sorry! Never mind.":
                    if approval:
                        $ LauraX.change_face("sexy", 1)
                        $ LauraX.change_stat("obedience", 70, 3)
                        $ LauraX.change_stat("inhibition", 50, 3)
                        $ LauraX.change_stat("inhibition", 70, 1)
                        ch_l "No no, not a problem. . ."
                        jump Laura_SexPrep
                    else:
                        "You pull back before you really get it in."
                        $ LauraX.change_face("bemused", 1)
                        if LauraX.action_counter["sex"]:
                            ch_l "Maybe ask first, [LauraX.player_petname]?"
                        else:
                            ch_l "Maybe if you'd asked first. . ."
                "Just fucking.":
                    $ LauraX.change_stat("love", 80, -10, 1)
                    $ LauraX.change_stat("love", 200, -10)
                    "You press inside some more."
                    $ LauraX.change_stat("obedience", 70, 3)
                    $ LauraX.change_stat("inhibition", 50, 3)
                    if not approval_check(LauraX, 700, "O", TabM=1):
                        $ LauraX.change_face("angry")
                        "[LauraX.name] shoves you away and backhands you in the face."
                        ch_l "Dick."
                        ch_l "Don't push me."
                        $ LauraX.change_stat("love", 50, -10, 1)
                        $ LauraX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        call Laura_Sex_Reset
                        $ LauraX.recent_history.append("angry")
                        $ LauraX.daily_history.append("angry")
                    else:
                        $ LauraX.change_face("sad")
                        "[LauraX.name] doesn't seem to be into this, you're lucky she's so obedient."
                        jump Laura_SexPrep
        return



    if not LauraX.action_counter["sex"] and "no_sex" not in LauraX.recent_history:

        $ LauraX.change_face("surprised", 1)
        $ LauraX.mouth = "kiss"
        ch_l "Huh, you wanna fuck me? . . "
        if LauraX.Forced:
            $ LauraX.change_face("sad")
            ch_l "Pretty bold of you. . ."


    if not LauraX.action_counter["sex"] and approval:

        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("love", 70, -30, 1)
            $ LauraX.change_stat("love", 20, -20, 1)
        elif LauraX.love >= (LauraX.obedience + LauraX.inhibition):
            $ LauraX.change_face("sexy")
            $ LauraX.brows = "sad"
            $ LauraX.mouth = "smile"
            ch_l "Well, you look so cute when you ask. . ."
        elif LauraX.obedience >= LauraX.inhibition:
            $ LauraX.change_face("normal")
            ch_l "Yes, [LauraX.player_petname]. . ."
        elif LauraX.addiction >= 50:
            $ LauraX.change_face("manic", 1)
            ch_l "Sounds fun. . ."
        else:
            $ LauraX.change_face("sad")
            $ LauraX.mouth = "smile"
            ch_l "I was hoping you'd ask. . ."


    elif approval:

        $ LauraX.change_face("sexy", 1)
        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
            ch_l "I hope I don't wear you out."
        elif not Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "Yeah, this is more covert."
        elif "sex" in LauraX.recent_history:
            ch_l "Again? Your funeral."
            jump Laura_SexPrep
        elif "sex" in LauraX.daily_history:
            $ Line = renpy.random.choice(["Back again?",
                    "You'd like another round?",
                    "I must be better than I thought.",
                    "Didn't get enough earlier?",
                    "Your funeral, " + LauraX.player_petname + "."])
            ch_l "[Line]"
        elif LauraX.action_counter["sex"] < 3:
            $ LauraX.brows = "confused"
            $ LauraX.mouth = "kiss"
            ch_l "Oh? Another round?"
        else:
            $ Line = renpy.random.choice(["Oh, you want some of this?",
                    "You'd like another round?",
                    "I must be better than I thought.",
                    "I hope you don't plan on wearing me out.",
                    "You want to plow me?"])
            ch_l "[Line]"
        $ Line = 0


    if approval >= 2:

        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("obedience", 90, 1)
            $ LauraX.change_stat("inhibition", 60, 1)
            ch_l "Ok, fine. Just make it good."
        elif "no_sex" in LauraX.daily_history:
            ch_l "Ok, whatever. . ."
        else:
            $ LauraX.change_face("sexy", 1)
            $ LauraX.change_stat("love", 90, 1)
            $ LauraX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well. . . fine, let's do it.",
                    "Sure.",
                    "We could, I guess.",
                    "Hmmm, sure.",
                    "Sounds fun."])
            ch_l "[Line]"
            $ Line = 0
        $ LauraX.change_stat("obedience", 20, 1)
        $ LauraX.change_stat("obedience", 60, 1)
        $ LauraX.change_stat("inhibition", 70, 2)
        jump Laura_SexPrep
    else:


        $ LauraX.change_face("angry")
        if "no_sex" in LauraX.recent_history:
            ch_l "Sorry, [LauraX.player_petname] \"no.\""
        elif Taboo and "no_taboo" in LauraX.daily_history and "no_sex" in LauraX.daily_history:
            ch_l "I told you. . . this place is too exposed."
        elif "no_sex" in LauraX.daily_history:
            ch_l "I just told you \"no.\""
        elif Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "I already told you this is too public!"
        elif not LauraX.action_counter["sex"]:
            $ LauraX.change_face("bemused")
            ch_l "Oh, you have no idea what you're in for. . ."
        else:
            $ LauraX.change_face("bemused")
            ch_l "Maybe later? . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_sex" in LauraX.daily_history:
                $ LauraX.change_face("bemused")
                ch_l "Well, you are persistant."
                return
            "Maybe later?" if "no_sex" not in LauraX.daily_history:
                $ LauraX.change_face("sexy")
                ch_l "Probably. . ."
                $ LauraX.change_stat("love", 80, 2)
                $ LauraX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ LauraX.recent_history.append("no_taboo")
                    $ LauraX.daily_history.append("no_taboo")
                $ LauraX.recent_history.append("no_sex")
                $ LauraX.daily_history.append("no_sex")
                return
            "I think you'd enjoy it as much as I would. . .":
                if approval:
                    $ LauraX.change_face("sexy")
                    $ LauraX.change_stat("obedience", 90, 2)
                    $ LauraX.change_stat("obedience", 50, 2)
                    $ LauraX.change_stat("inhibition", 70, 3)
                    $ LauraX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Yeah, probably. . .",
                                "I guess. . .",
                                "Good point. . ."])
                    ch_l "[Line]"
                    $ Line = 0
                    jump Laura_SexPrep
            "Just deal with it.":
                $ approval = approval_check(LauraX, 1150, "OI", TabM = 3)
                if approval > 1 or (approval and LauraX.Forced):
                    $ LauraX.change_face("sad")
                    $ LauraX.change_stat("love", 70, -5, 1)
                    $ LauraX.change_stat("love", 200, -5)
                    ch_l "Fine, if it'll shut you up."
                    $ LauraX.change_stat("obedience", 80, 4)
                    $ LauraX.change_stat("inhibition", 80, 1)
                    $ LauraX.change_stat("inhibition", 60, 3)
                    $ LauraX.Forced = 1
                    jump Laura_SexPrep
                else:
                    $ LauraX.change_stat("love", 200, -20)
                    $ LauraX.recent_history.append("angry")
                    $ LauraX.daily_history.append("angry")




    $ LauraX.ArmPose = 1
    if "no_sex" in LauraX.daily_history:
        ch_l "Don't push me."
        $ LauraX.recent_history.append("angry")
        $ LauraX.daily_history.append("angry")
    elif LauraX.Forced:
        $ LauraX.change_face("angry", 1)
        ch_l "I'm over taking orders."
        $ LauraX.change_stat("lust", 200, 5)
        if LauraX.love > 300:
            $ LauraX.change_stat("love", 70, -2)
        $ LauraX.change_stat("obedience", 50, -2)
        $ LauraX.recent_history.append("angry")
        $ LauraX.daily_history.append("angry")
    elif Taboo:
        $ LauraX.change_face("angry", 1)
        $ LauraX.recent_history.append("no_taboo")
        $ LauraX.daily_history.append("no_taboo")
        ch_l "This place is way too exposed."
        $ LauraX.change_stat("lust", 200, 5)
        $ LauraX.change_stat("obedience", 50, -3)
    elif LauraX.action_counter["sex"]:
        $ LauraX.change_face("sad")
        ch_l "Just jack it or something."
    else:
        $ LauraX.change_face("normal", 1)
        ch_l "Yeah, no."
    $ LauraX.recent_history.append("no_sex")
    $ LauraX.daily_history.append("no_sex")
    $ approval_bonus = 0
    return

label Laura_SexPrep:
    call Seen_First_Peen (LauraX, Partner, React=action_context)
    call Laura_Sex_Launch ("hotdog")

    if action_context == LauraX:

        $ action_context = 0
        if LauraX.PantsNum() == 5:
            "[LauraX.name] lays back, sliding her skirt up as she does so."
            $ LauraX.upskirt = 1
        elif LauraX.PantsNum() >= 6:
            "[LauraX.name] lays back, sliding her [LauraX.legs] down as she does so."
            $ LauraX.upskirt = 1
        else:
            "[LauraX.name] rolls back and pulls you toward her."
        $ LauraX.SeenPanties = 1
        "She slides the tip along her pussy and seems to want you to insert it."
        menu:
            "What do you do?"
            "Go with it.":
                $ LauraX.change_stat("inhibition", 80, 3)
                $ LauraX.change_stat("inhibition", 50, 2)
                "[LauraX.name] slides it in."
            "Praise her.":
                $ LauraX.change_face("sexy", 1)
                $ LauraX.change_stat("inhibition", 80, 3)
                ch_p "Oh yeah, [LauraX.petname], let's do this."
                $ LauraX.nameCheck()
                "Laura slides it in."
                $ LauraX.change_stat("love", 85, 1)
                $ LauraX.change_stat("obedience", 90, 1)
                $ LauraX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ LauraX.change_face("surprised")
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
        $ LauraX.underwear_pulled_down = 1
        call Laura_First_Bottomless (1)

    elif action_context != "auto":
        call AutoStrip (LauraX)

        if Taboo:
            "[LauraX.name] glances around to see if anyone notices what she's doing."
            if "cockout" in Player.recent_history:
                "Then she lays back and slowly presses against your rigid member."
            else:
                "Then she pulls down your pants and lays back."
                "She slowly presses against your rigid member."
            $ LauraX.inhibition += int(Taboo/10)
            $ LauraX.lust += int(Taboo/5)
        else:
            if "cockout" in Player.recent_history:
                "[LauraX.name] lays back and slowly presses against your rigid member."
            else:
                "[LauraX.name] pulls down your pants and lays back."
                "She slowly presses against your rigid member."
        "She leans back a bit and your cock slides in."
    else:

        if (LauraX.PantsNum() >= 6 and not LauraX.upskirt) and (LauraX.underwear and not LauraX.underwear_pulled_down):
            "You quickly pull down her pants and her [LauraX.underwear] and press against her slit."
        elif (LauraX.underwear and not LauraX.underwear_pulled_down):
            "You quickly pull down her [LauraX.underwear] and press against her slit."
        $ LauraX.upskirt = 1
        $ LauraX.underwear_pulled_down = 1
        $ LauraX.SeenPanties = 1
        call Laura_First_Bottomless (1)

    if Player.focus >= 50:
        ch_l "Nice to see you're ready for business. . ."
    if not LauraX.action_counter["sex"]:
        if LauraX.Forced:
            $ LauraX.change_stat("love", 90, -150)
            $ LauraX.change_stat("obedience", 70, 60)
            $ LauraX.change_stat("inhibition", 80, 50)
        else:
            $ LauraX.change_stat("love", 90, 30)
            $ LauraX.change_stat("obedience", 70, 30)
            $ LauraX.change_stat("inhibition", 80, 60)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    $ Player.cock_position = "in"
    $ primary_action = "sex"
    $ action_speed = 1
    if Taboo:
        $ LauraX.drain_word("no_taboo")
    $ LauraX.drain_word("no_sex")
    $ LauraX.recent_history.append("sex")
    $ LauraX.daily_history.append("sex")

label Laura_Sex_Cycle:
    while Round > 0:
        call shift_focus (LauraX)
        call Laura_Sex_Launch ("sex")
        if action_speed >= 4:
            $ action_speed = 2

        $ LauraX.lust_face()
        $ Player.cock_position = "in"
        $ primary_action = "sex"
        $ LauraX.upskirt = 1
        $ LauraX.underwear_pulled_down = 1

        if Player.focus < 100:

            menu:
                "Keep going. . ." if action_speed:
                    pass
                "Keep going. . . (locked)" if not action_speed:
                    pass

                "Start moving? . ." if not action_speed:
                    $ action_speed = 1

                "Speed up. . ." if 0 < action_speed < 3:
                    $ action_speed += 1

                    "You ask her to up the pace a bit."
                "Speed up. . . (locked)" if action_speed >= 3:
                    pass

                "Slow Down. . ." if action_speed:
                    $ action_speed -= 1

                    "You ask her to slow it down a bit."
                "Slow Down. . . (locked)" if not action_speed:
                    pass
                "Slap her ass":

                    call Slap_Ass (LauraX)
                    $ counter += 1
                    $ Round -= 1
                    jump Laura_Sex_Cycle
                "Turn her Around":

                    $ LauraX.pose = "doggy" if LauraX.pose != "doggy" else 0
                    "You turn her around. . ."
                    jump Laura_Sex_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
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
                                    "How about anal?":
                                        $ action_context = "shift"
                                        call Laura_SexAfter
                                        call Laura_Sex_A
                                    "Just stick it in her ass [[without asking].":
                                        $ action_context = "auto"
                                        call Laura_SexAfter
                                        call Laura_Sex_A
                                    "Pull back to hotdog her.":
                                        $ action_context = "pullback"
                                        call Laura_SexAfter
                                        call Laura_Sex_H
                                    "Never Mind":
                                        jump Laura_Sex_Cycle
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
                                    jump Laura_Sex_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Laura_Sex_Cycle
                                "Never mind":
                                    jump Laura_Sex_Cycle
                        "Just take a look at her.":
                            $ Player.cock_position = 0
                            $ action_speed = 0
                        "Undress [LauraX.name]":
                            call Girl_Undress (LauraX)
                        "Clean up [LauraX.name] (locked)" if not LauraX.spunk:
                            pass
                        "Clean up [LauraX.name]" if LauraX.spunk:
                            call Girl_Cleanup (LauraX, "ask")
                        "Never mind":
                            jump Laura_Sex_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Laura_Sex_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Laura_SexAfter
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Laura_Sex_Reset
                    $ Line = 0
                    jump Laura_SexAfter


        call shift_focus (LauraX)
        call Sex_Dialog (LauraX, Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or LauraX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (LauraX)
                if "angry" in LauraX.recent_history:
                    call Laura_Sex_Reset
                    return
                $ LauraX.change_stat("lust", 200, 5)
                if 100 > LauraX.lust >= 70 and LauraX.session_orgasms < 2:
                    $ LauraX.recent_history.append("unsatisfied")
                    $ LauraX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Laura_SexAfter
                $ Line = "came"

            if LauraX.lust >= 100:

                call Girl_Cumming (LauraX)
                if action_context == "shift" or "angry" in LauraX.recent_history:
                    jump Laura_SexAfter

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "She's emptied you out, you'll need to take a break."
                    jump Laura_SexAfter
                elif "unsatisfied" in LauraX.recent_history:

                    $ Line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                    "[Line] Keep going?"
                    menu:
                        extend ""
                        "Yes, keep going for a bit." if Player.semen:
                            $ Line = "You get back into it"
                            jump Laura_Sex_Cycle
                        "No, I'm done." if Player.semen:
                            "You pull back."
                            jump Laura_SexAfter
                        "No, I'm spent." if not Player.semen:
                            "You pull back."
                            jump Laura_SexAfter
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if LauraX.SEXP >= 100 or approval_check(LauraX, 1200, "LO"):
            pass
        elif counter == (5 + LauraX.action_counter["sex"]):
            $ LauraX.brows = "confused"
            ch_l "So are we getting close?"
        elif counter == (10 + LauraX.action_counter["sex"]):
            $ LauraX.brows = "angry"
            menu:
                ch_l "Hey. . . could we. . . try something. . . else?"
                "How about a BJ?" if LauraX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Laura_SexAfter
                    call Laura_Blowjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    $ counter += 1
                    jump Laura_Sex_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Laura_Sex_Reset
                    $ action_context = "shift"
                    jump Laura_SexAfter
                "No, get back down there.":
                    if approval_check(LauraX, 1200) or approval_check(LauraX, 500, "O"):
                        $ LauraX.change_stat("love", 200, -5)
                        $ LauraX.change_stat("obedience", 50, 3)
                        $ LauraX.change_stat("obedience", 80, 2)
                        "She grumbles but keeps moving."
                    else:
                        $ LauraX.change_face("angry", 1)
                        call Laura_Sex_Reset
                        "She scowls at you and pulls out."
                        ch_l "Not with that attitude."
                        $ LauraX.change_stat("love", 50, -3, 1)
                        $ LauraX.change_stat("love", 80, -4, 1)
                        $ LauraX.change_stat("obedience", 30, -1, 1)
                        $ LauraX.change_stat("obedience", 50, -1, 1)
                        $ LauraX.recent_history.append("angry")
                        $ LauraX.daily_history.append("angry")
                        jump Laura_SexAfter


        call Escalation (LauraX)

        if Round == 10:
            ch_l "It's getting kinda late. . ."
        elif Round == 5:
            ch_l "We should take a break for a minute."


    $ LauraX.change_face("bemused", 0)
    $ Line = 0
    ch_l "Ok, that's enough of that for now."

label Laura_SexAfter:
    if not action_context:
        $ Player.sprite = 0
        $ Player.cock_position = "out"
        call Laura_Sex_Reset

    $ LauraX.change_face("sexy")

    $ LauraX.action_counter["sex"] += 1
    $ LauraX.remaining_actions -=1
    $ LauraX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ LauraX.addiction_rate += 1
    $ LauraX.change_stat("inhibition", 30, 2)
    $ LauraX.change_stat("inhibition", 70, 1)

    call Partner_Like (LauraX, 3, 2)

    if "Laura Sex Addict" in Achievements:
        pass

    elif LauraX.action_counter["sex"] >= 10:
        $ LauraX.SEXP += 5
        $ Achievements.append("Laura Sex Addict")
        if not action_context:
            $ LauraX.change_face("smile", 1)
            ch_l "We're making this a regular thing, huh. . ."
    elif LauraX.action_counter["sex"] == 1:
        $ LauraX.SEXP += 20
        if not action_context:
            if LauraX.love >= 500 and "unsatisfied" not in LauraX.recent_history:
                ch_l "I can tell, I was the best you've had."
            elif LauraX.obedience <= 500 and Player.focus <= 20:
                $ LauraX.mouth = "sad"
                ch_l "Satisfied?"
    elif LauraX.action_counter["sex"] == 5:
        ch_l "You know, this was a good idea."
    elif not action_context:
        if "unsatisfied" in LauraX.recent_history:
            $ LauraX.change_face("angry")
            $ LauraX.eyes = "side"
            ch_l "Forgetting someone? . ."

    $ approval_bonus = 0


    call checkout
    return






label Laura_Sex_A:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (LauraX)
    if LauraX.action_counter["anal"] >= 7:
        $ approval_bonus += 20
    elif LauraX.action_counter["anal"] >= 3:
        $ approval_bonus += 17
    elif LauraX.action_counter["anal"]:
        $ approval_bonus += 15

    if LauraX.addiction >= 75 and (LauraX.event_counter["creampied"] + LauraX.event_counter["anal_creampied"]) >=3:
        $ approval_bonus += 25
    elif LauraX.addiction >= 75:
        $ approval_bonus += 15

    if LauraX.lust > 85:
        $ approval_bonus += 10
    elif LauraX.lust > 75:
        $ approval_bonus += 5

    $ approval_bonus += 10

    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in LauraX.traits:
        $ approval_bonus += (5*Taboo)

    if LauraX in Player.Harem or "sex friend" in LauraX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in LauraX.traits:
        $ approval_bonus -= 40
    if LauraX.event_counter["forced"] and not LauraX.Forced:
        $ approval_bonus -= 5*LauraX.event_counter["forced"]

    if Taboo and "no_taboo" in LauraX.daily_history:
        $ approval_bonus -= 10
    if "no_anal" in LauraX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_anal" in LauraX.recent_history else 0

    $ approval = approval_check(LauraX, 1550, TabM = 5)

    if action_context == "auto":
        call Laura_Sex_Launch ("anal")
        if LauraX.PantsNum() == 5:
            "You push [LauraX.name] onto her back, sliding her skirt up as you go."
            $ LauraX.upskirt = 1
        elif LauraX.PantsNum() >= 6:
            "You push [LauraX.name] onto her back, sliding her pants down as you do."
            $ LauraX.legs = 0
        else:
            "You push [LauraX.name] onto her back."
        $ LauraX.SeenPanties = 1
        "You press the tip of your cock against her tight rim."
        $ LauraX.change_face("surprised", 1)
        call Laura_First_Bottomless (1)

        if (LauraX.action_counter["anal"] and approval) or (approval > 1):

            $ LauraX.change_stat("obedience", 70, 3)
            $ LauraX.change_stat("inhibition", 50, 3)
            $ LauraX.change_stat("inhibition", 70, 1)
            "[LauraX.name] glances down and then breaks into a smile."
            ch_l "Yeah, ok. . ."
            jump Laura_AnalPrep
        else:

            $ LauraX.brows = "angry"
            menu:
                ch_l "Oh? A backdoor intruder?"
                "Sorry, sorry! Never mind.":
                    if approval:
                        $ LauraX.change_face("sexy", 1)
                        $ LauraX.change_stat("obedience", 70, 3)
                        $ LauraX.change_stat("inhibition", 50, 3)
                        $ LauraX.change_stat("inhibition", 70, 1)
                        ch_l "Hey, whatever floats your boat. . ."
                        ch_l "Get in there."
                        jump Laura_AnalPrep
                    "You pull back before you really get it in."
                    $ LauraX.change_face("bemused", 1)

                    if LauraX.action_counter["anal"]:
                        ch_l "You coulda warned me. . ."
                    else:
                        ch_l "Hey, all I expect is a little warning. . ."
                "Just fucking.":
                    $ LauraX.change_stat("love", 80, -10, 1)
                    $ LauraX.change_stat("love", 200, -8)
                    "You press into her."
                    $ LauraX.change_stat("obedience", 70, 3)
                    $ LauraX.change_stat("inhibition", 50, 3)
                    if not approval_check(LauraX, 700, "O", TabM=1):
                        $ LauraX.change_face("angry")
                        "[LauraX.name] shoves you away and backhands you in the face."
                        ch_l "Yeah, not like that you won't."
                        $ LauraX.change_stat("love", 50, -10, 1)
                        $ LauraX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        call Laura_Sex_Reset
                        $ LauraX.recent_history.append("angry")
                        $ LauraX.daily_history.append("angry")
                    else:
                        $ LauraX.change_face("sad")
                        "[LauraX.name] doesn't seem to be into this, you're lucky she's so obedient."
                        jump Laura_AnalPrep
        return



    if not LauraX.action_counter["anal"] and "no_anal" not in LauraX.recent_history:

        $ LauraX.change_face("surprised", 1)
        $ LauraX.mouth = "kiss"
        ch_l "Huh, anal?"

        if LauraX.Forced:
            $ LauraX.change_face("sad")
            ch_l "Anal? That's what you're pushing for?"

    if "anal" in LauraX.recent_history:
        $ LauraX.change_face("sexy", 1)
        ch_l "Sure, get in there."
        jump Laura_AnalPrep


    if not LauraX.action_counter["anal"] and approval:

        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
        elif LauraX.love >= (LauraX.obedience + LauraX.inhibition):
            $ LauraX.change_face("sexy")
            $ LauraX.brows = "sad"
            $ LauraX.mouth = "smile"
            ch_l "I was hoping you'd ask. . ."
        elif LauraX.obedience >= LauraX.inhibition:
            $ LauraX.change_face("normal")
            ch_l "I expected that. . ."
        elif LauraX.addiction >= 50:
            $ LauraX.change_face("manic", 1)
            ch_l "Hmm, sounds fun. . ."
        else:
            $ LauraX.change_face("sad")
            $ LauraX.mouth = "smile"
            ch_l "I was tired of waiting. . ."

    elif approval:

        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
            ch_l "You don't hold back. . ."
        elif not Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "I guess this is secluded enough. . ."
        elif "anal" in LauraX.daily_history and not LauraX.used_to_anal:
            pass
        elif "anal" in LauraX.recent_history:
            ch_l "I am warmed up. . ."
            jump Laura_AnalPrep
        elif "anal" in LauraX.daily_history:
            $ LauraX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",
                    "So you'd like another round?",
                    "Again? Sure.",
                    "Didn't get enough earlier?",
                    "Your funeral, " + LauraX.player_petname + "."])
            ch_l "[Line]"
        else:
            $ LauraX.change_face("sexy", 1)
            $ LauraX.ArmPose = 2
            $ Line = renpy.random.choice(["Oooh, you want some of this?",
                    "So you'd like another round?",
                    "I knew you enjoyed it. . .",
                    "I hope you don't plan on wearing me out.",
                    "You want to plow me?"])
            ch_l "[Line]"
        $ Line = 0

    if approval >= 2:

        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("obedience", 90, 1)
            $ LauraX.change_stat("inhibition", 60, 1)
            ch_l "Whatever."
        elif "no_anal" in LauraX.daily_history:
            ch_l "Well, if you're going to keep asking. . ."
            ch_l "Might be fun. . ."
        else:
            $ LauraX.change_face("sexy", 1)
            $ LauraX.change_stat("love", 90, 1)
            $ LauraX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well. . . ok.",
                    "Sure.",
                    "You could, I guess.",
                    "Um, yeah.",
                    "Heh, ok, ok."])
            ch_l "[Line]"
            $ Line = 0
        $ LauraX.change_stat("obedience", 20, 1)
        $ LauraX.change_stat("obedience", 60, 1)
        $ LauraX.change_stat("inhibition", 70, 2)
        jump Laura_AnalPrep
    else:


        $ LauraX.change_face("angry")
        if "no_anal" in LauraX.recent_history:
            ch_l "Sorry, [LauraX.player_petname] \"no.\""
        elif Taboo and "no_taboo" in LauraX.daily_history and "no_anal" in LauraX.daily_history:
            ch_l "I told you. . . this place is too exposed."
        elif "no_anal" in LauraX.daily_history:
            ch_l "I just told you \"no.\""
        elif Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "I already told you this is too public!"
        elif not LauraX.action_counter["anal"]:
            $ LauraX.change_face("bemused")
            ch_l "I don't know that you're ready for that yet."
        else:
            $ LauraX.change_face("bemused")
            ch_l "Maybe eventually. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_anal" in LauraX.daily_history:
                $ LauraX.change_face("bemused")
                ch_l "Hey, I can't blame you."
                return
            "Maybe later?" if "no_anal" not in LauraX.daily_history:
                $ LauraX.change_face("sexy")
                ch_l "Oh, probably. . ."
                ch_l ". . . often."
                $ LauraX.change_stat("love", 80, 2)
                $ LauraX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ LauraX.recent_history.append("no_taboo")
                    $ LauraX.daily_history.append("no_taboo")
                $ LauraX.recent_history.append("no_anal")
                $ LauraX.daily_history.append("no_anal")
                return
            "I bet it would feel really good. . .":
                if approval:
                    $ LauraX.change_face("sexy")
                    $ LauraX.change_stat("obedience", 90, 2)
                    $ LauraX.change_stat("obedience", 50, 2)
                    $ LauraX.change_stat("inhibition", 70, 3)
                    $ LauraX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Yeah, probably. . .",
                                "I guess. . .",
                                "Good point. . ."])
                    ch_l "[Line]"
                    $ Line = 0
                    jump Laura_AnalPrep
                else:
                    pass
            "Just deal with it.":

                $ approval = approval_check(LauraX, 1250, "OI", TabM = 3)
                if approval > 1 or (approval and LauraX.Forced):
                    $ LauraX.change_face("sad")
                    $ LauraX.change_stat("love", 70, -5, 1)
                    $ LauraX.change_stat("love", 200, -5)
                    ch_l "Oh fine, get it over with."
                    $ LauraX.change_stat("obedience", 80, 4)
                    $ LauraX.change_stat("inhibition", 80, 1)
                    $ LauraX.change_stat("inhibition", 60, 3)
                    $ LauraX.Forced = 1
                    jump Laura_AnalPrep
                else:
                    $ LauraX.change_stat("love", 200, -20)
                    $ LauraX.recent_history.append("angry")
                    $ LauraX.daily_history.append("angry")


    $ LauraX.ArmPose = 1
    if "no_anal" in LauraX.daily_history:
        ch_l "Don't push it."
        $ LauraX.recent_history.append("angry")
        $ LauraX.daily_history.append("angry")
    elif LauraX.Forced:
        $ LauraX.change_face("angry", 1)
        ch_l "You're going too far."
        $ LauraX.change_stat("lust", 200, 5)
        if LauraX.love > 300:
            $ LauraX.change_stat("love", 70, -2)
        $ LauraX.change_stat("obedience", 50, -2)
        $ LauraX.recent_history.append("angry")
        $ LauraX.daily_history.append("angry")
    elif Taboo:

        $ LauraX.change_face("angry", 1)
        $ LauraX.recent_history.append("no_taboo")
        $ LauraX.daily_history.append("no_taboo")
        ch_l "This place is way too exposed."
        $ LauraX.change_stat("lust", 200, 5)
        $ LauraX.change_stat("obedience", 50, -3)
    elif "anal" in LauraX.daily_history:
        $ LauraX.change_face("bemused")
        ch_l "Not right now."
    elif LauraX.action_counter["anal"]:
        $ LauraX.change_face("sad")
        ch_l "You'll have to earn it."
    else:
        $ LauraX.change_face("normal", 1)
        ch_l "You haven't earned it yet."
    $ LauraX.recent_history.append("no_anal")
    $ LauraX.daily_history.append("no_anal")
    $ approval_bonus = 0
    return

label Laura_AnalPrep:
    call Seen_First_Peen (LauraX, Partner, React=action_context)
    call Laura_Sex_Launch ("hotdog")

    if action_context == LauraX:

        $ action_context = 0
        if LauraX.PantsNum() == 5:
            "[LauraX.name] lays back, sliding her skirt up as she does so."
            $ LauraX.upskirt = 1
        elif LauraX.PantsNum() >= 6:
            "[LauraX.name] lays back, sliding her [LauraX.legs] down as she does so."
            $ LauraX.upskirt = 1
        else:
            "[LauraX.name] rolls back and pulls you toward her."
        $ LauraX.SeenPanties = 1
        "She slides the tip along her asshole, and seems to want you to insert it."
        menu:
            "What do you do?"
            "Go with it.":
                $ LauraX.change_stat("inhibition", 80, 3)
                $ LauraX.change_stat("inhibition", 50, 2)
                "[LauraX.name] slides it in."
            "Praise her.":
                $ LauraX.change_face("sexy", 1)
                $ LauraX.change_stat("inhibition", 80, 3)
                ch_p "Oh yeah, [LauraX.petname], let's do this."
                $ LauraX.nameCheck()
                "[LauraX.name] slides it in."
                $ LauraX.change_stat("love", 85, 1)
                $ LauraX.change_stat("obedience", 90, 1)
                $ LauraX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ LauraX.change_face("surprised")
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
        $ LauraX.underwear_pulled_down = 1
        call Laura_First_Bottomless (1)
    elif action_context != "auto":
        call AutoStrip (LauraX)

        if Taboo:
            "[LauraX.name] glances around to see if anyone notices what she's doing."
            if "cockout" in Player.recent_history:
                "Then she lays back and slowly presses against your rigid member."
            else:
                "Then she pulls down your pants and lays back."
                "She slowly presses against your rigid member."
            $ LauraX.inhibition += int(Taboo/10)
            $ LauraX.lust += int(Taboo/5)
        else:
            if "cockout" in Player.recent_history:
                "[LauraX.name] lays back and slowly presses against your rigid member."
            else:
                "[LauraX.name] pulls down your pants and lays back."
                "She slowly presses against your rigid member."
        "She leans back a bit and your cock pops in."
    else:

        if (LauraX.PantsNum() >= 6 and not LauraX.upskirt) and (LauraX.underwear and not LauraX.underwear_pulled_down):
            "You quickly pull down her pants and her [LauraX.underwear] and press against her back door."
        elif (LauraX.underwear and not LauraX.underwear_pulled_down):
            "You quickly pull down her [LauraX.underwear] and press against her back door."
        $ LauraX.upskirt = 1
        $ LauraX.underwear_pulled_down = 1
        $ LauraX.SeenPanties = 1
        call Laura_First_Bottomless (1)

    if not LauraX.action_counter["anal"]:
        if LauraX.Forced:
            $ LauraX.change_stat("love", 90, -150)
            $ LauraX.change_stat("obedience", 70, 70)
            $ LauraX.change_stat("inhibition", 80, 40)
        else:
            $ LauraX.change_stat("love", 90, 10)
            $ LauraX.change_stat("obedience", 70, 30)
            $ LauraX.change_stat("inhibition", 80, 70)
    elif not LauraX.used_to_anal:
        if LauraX.Forced:
            $ LauraX.change_stat("love", 90, -20)
            $ LauraX.change_stat("obedience", 70, 10)
            $ LauraX.change_stat("inhibition", 80, 5)
        else:
            $ LauraX.change_stat("obedience", 70, 7)
            $ LauraX.change_stat("inhibition", 80, 5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    $ Player.cock_position = "anal"
    $ primary_action = "anal"
    $ action_speed = 1
    if Taboo:
        $ LauraX.drain_word("no_taboo")
    $ LauraX.drain_word("no_anal")
    $ LauraX.recent_history.append("anal")
    $ LauraX.daily_history.append("anal")

label Laura_Anal_Cycle:
    while Round > 0:
        call shift_focus (LauraX)
        call Laura_Sex_Launch ("anal")
        if action_speed >= 4:
            $ Shift = 2

        $ LauraX.lust_face()
        $ Player.cock_position = "anal"
        $ primary_action = "anal"

        if Player.focus < 100:

            menu:
                "Keep going. . ." if action_speed:
                    pass
                "Keep going. . . (locked)" if not action_speed:
                    pass

                "Start moving? . ." if not action_speed:
                    $ action_speed = 1

                "Speed up. . ." if 0 < action_speed < 3:
                    $ action_speed += 1

                    "You ask her to up the pace a bit."
                "Speed up. . . (locked)" if action_speed >= 3:
                    pass

                "Slow Down. . ." if action_speed:
                    $ action_speed -= 1

                    "You ask her to slow it down a bit."
                "Slow Down. . . (locked)" if not action_speed:
                    pass
                "Slap her ass":

                    call Slap_Ass (LauraX)
                    $ counter += 1
                    $ Round -= 1
                    jump Laura_Anal_Cycle
                "Turn her Around":

                    $ LauraX.pose = "doggy" if LauraX.pose != "doggy" else 0
                    "You turn her around. . ."
                    jump Laura_Anal_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
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
                                    "How about sex?":
                                        $ action_context = "shift"
                                        call Laura_AnalAfter
                                        call Laura_Sex_P
                                    "Just stick it in her pussy [[without asking].":
                                        $ action_context = "auto"
                                        call Laura_AnalAfter
                                        call Laura_Sex_P
                                    "Pull back to hotdog her.":
                                        $ action_context = "pullback"
                                        call Laura_AnalAfter
                                        call Laura_Sex_H
                                    "Never Mind":
                                        jump Laura_Anal_Cycle
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
                                    jump Laura_Anal_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Laura_Anal_Cycle
                                "Never mind":
                                    jump Laura_Anal_Cycle
                        "Just take a look at her.":
                            $ Player.cock_position = 0
                            $ action_speed = 0

                        "Show her feet" if not ShowFeet and LauraX.pose == "doggy":
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and LauraX.pose == "doggy":
                            $ ShowFeet = 0
                        "Undress [LauraX.name]":

                            call Girl_Undress (LauraX)
                        "Clean up [LauraX.name] (locked)" if not LauraX.spunk:
                            pass
                        "Clean up [LauraX.name]" if LauraX.spunk:
                            call Girl_Cleanup (LauraX, "ask")
                        "Never mind":
                            jump Laura_Anal_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Laura_Sex_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Laura_AnalAfter
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Laura_Sex_Reset
                    $ Line = 0
                    jump Laura_AnalAfter


        call shift_focus (LauraX)
        call Sex_Dialog (LauraX, Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or LauraX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (LauraX)
                if "angry" in LauraX.recent_history:
                    call Laura_Sex_Reset
                    return
                $ LauraX.change_stat("lust", 200, 5)
                if 100 > LauraX.lust >= 70 and LauraX.session_orgasms < 2:
                    $ LauraX.recent_history.append("unsatisfied")
                    $ LauraX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Laura_AnalAfter
                $ Line = "came"

            if LauraX.lust >= 100:

                call Girl_Cumming (LauraX)
                if action_context == "shift" or "angry" in LauraX.recent_history:
                    jump Laura_AnalAfter

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "She's emptied you out, you'll need to take a break."
                    jump Laura_AnalAfter
                elif "unsatisfied" in LauraX.recent_history:

                    $ Line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                    "[Line] Keep going?"
                    menu:
                        extend ""
                        "Yes, keep going for a bit." if Player.semen:
                            $ Line = "You get back into it"
                            jump Laura_Anal_Cycle
                        "No, I'm done." if Player.semen:
                            "You pull back."
                            jump Laura_AnalAfter
                        "No, I'm spent." if not Player.semen:
                            "You pull back."
                            jump Laura_AnalAfter
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if LauraX.SEXP >= 100 or approval_check(LauraX, 1200, "LO"):
            pass
        elif counter == (5 + LauraX.action_counter["anal"]):
            $ LauraX.brows = "confused"
            ch_l "We getting close here?"
        elif counter == (10 + LauraX.action_counter["anal"]):
            $ LauraX.brows = "angry"
            menu:
                ch_l "Can we. . . do something. . . else?"
                "How about a BJ?" if LauraX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Laura_AnalAfter
                    call Laura_Blowjob
                "How about a Handy?" if LauraX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Laura_AnalAfter
                    call Laura_Handjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    $ counter += 1
                    jump Laura_Anal_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Laura_Sex_Reset
                    $ action_context = "shift"
                    jump Laura_AnalAfter
                "No, get back down there.":
                    if approval_check(LauraX, 1200) or approval_check(LauraX, 500, "O"):
                        $ LauraX.change_stat("love", 200, -5)
                        $ LauraX.change_stat("obedience", 50, 3)
                        $ LauraX.change_stat("obedience", 80, 2)
                        "She grumbles but keeps moving."
                    else:
                        $ LauraX.change_face("angry", 1)
                        call Laura_Sex_Reset
                        "She scowls at you and pulls out."
                        ch_l "Not with that attitude."
                        $ LauraX.change_stat("love", 50, -3, 1)
                        $ LauraX.change_stat("love", 80, -4, 1)
                        $ LauraX.change_stat("obedience", 30, -1, 1)
                        $ LauraX.change_stat("obedience", 50, -1, 1)
                        $ LauraX.recent_history.append("angry")
                        $ LauraX.daily_history.append("angry")
                        jump Laura_AnalAfter


        if Round == 10:
            ch_l "It's getting kinda late. . ."
        elif Round == 5:
            ch_l "We should take a break for a minute."


    $ LauraX.change_face("bemused", 0)
    $ Line = 0
    ch_l "Ok, that's enough of that for now."

label Laura_AnalAfter:
    if not action_context:
        $ Player.sprite = 0
        $ Player.cock_position = "out"
        call Laura_Sex_Reset

    $ LauraX.change_face("sexy")

    $ LauraX.action_counter["anal"] += 1
    $ LauraX.remaining_actions -=1
    $ LauraX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ LauraX.addiction_rate += 1
    $ LauraX.change_stat("inhibition", 30, 3)
    $ LauraX.change_stat("inhibition", 70, 1)

    if Partner == "Kitty":
        call Partner_Like (LauraX, 4, 2)
    else:
        call Partner_Like (LauraX, 3, 2)

    if "Laura Anal Addict" in Achievements:
        pass

    elif LauraX.action_counter["anal"] >= 10:
        $ LauraX.SEXP += 7
        $ Achievements.append("Laura Anal Addict")
        if not action_context:
            $ LauraX.change_face("bemused", 1)
            ch_l "I think you've got a knack for that."
    elif LauraX.action_counter["anal"] == 1:
        $ LauraX.SEXP += 25
        if not action_context:
            if LauraX.love >= 500 and "unsatisfied" not in LauraX.recent_history:
                ch_l "You seem to know your way around back there."
            elif LauraX.obedience <= 500 and Player.focus <= 20:
                $ LauraX.mouth = "sad"
                ch_l "That was pleasant."
    elif LauraX.action_counter["anal"] == 5:
        ch_l "I'm glad you're into this."
    elif not action_context:
        if "unsatisfied" in LauraX.recent_history:
            $ LauraX.change_face("angry")
            $ LauraX.eyes = "side"
            ch_l "Forgetting someone? . ."

    $ approval_bonus = 0


    call checkout
    return








label Laura_Sex_H:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (LauraX)
    if LauraX.action_counter["hotdog"] >= 3:
        $ approval_bonus += 10
    elif LauraX.action_counter["hotdog"]:
        $ approval_bonus += 5

    if LauraX.lust > 85:
        $ approval_bonus += 10
    elif LauraX.lust > 75:
        $ approval_bonus += 5
    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in LauraX.traits:
        $ approval_bonus += (3*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in LauraX.traits:
        $ approval_bonus -= 40
    if LauraX.event_counter["forced"] and not LauraX.Forced:
        $ approval_bonus -= 5*LauraX.event_counter["forced"]

    if Taboo and "no_taboo" in LauraX.daily_history:
        $ approval_bonus -= 10

    if "no_hotdog" in LauraX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_hotdog" in LauraX.recent_history else 0

    $ approval = approval_check(LauraX, 1000, TabM = 3)

    if action_context == "auto":
        call Laura_Sex_Launch ("hotdog")
        "You push [LauraX.name] down, and press your cock against her."
        $ LauraX.change_face("surprised", 1)

        if (LauraX.action_counter["hotdog"] and approval) or (approval > 1):
            "[LauraX.name] glances down and then breaks into a smile."
            $ LauraX.change_face("sly")
            $ LauraX.change_stat("obedience", 70, 3)
            $ LauraX.change_stat("inhibition", 50, 3)
            $ LauraX.change_stat("inhibition", 70, 1)
            ch_l "Oh, what did you have in mind with that? . ."
            jump Laura_HotdogPrep
        else:
            $ LauraX.brows = "angry"
            menu:
                ch_l "You might want to take a step back, [LauraX.player_petname]?"
                "Sorry, sorry! Never mind.":
                    if approval:
                        $ LauraX.change_face("sexy", 1)
                        $ LauraX.change_stat("obedience", 70, 3)
                        $ LauraX.change_stat("inhibition", 50, 3)
                        $ LauraX.change_stat("inhibition", 70, 1)
                        ch_l "Or not. . ."
                        jump Laura_HotdogPrep
                    "You pull back from her."
                    $ LauraX.change_face("bemused", 1)
                    ch_l "Maybe ask first?"
                "You'll see.":
                    $ LauraX.change_stat("love", 80, -10, 1)
                    $ LauraX.change_stat("love", 200, -8)
                    "You grind against her crotch."
                    $ LauraX.change_stat("obedience", 70, 3)
                    $ LauraX.change_stat("inhibition", 50, 3)
                    if not approval_check(LauraX, 500, "O", TabM=1):
                        $ LauraX.change_face("angry")
                        "[LauraX.name] shoves you away."
                        ch_l "Don't push it, [LauraX.player_petname]."
                        $ LauraX.change_stat("love", 50, -10, 1)
                        $ LauraX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        call Laura_Sex_Reset
                        $ LauraX.recent_history.append("angry")
                        $ LauraX.daily_history.append("angry")
                    else:
                        $ LauraX.change_face("sad")
                        "[LauraX.name] doesn't seem to be into this, but she knows her place."
                        jump Laura_HotdogPrep
        return



    if not LauraX.action_counter["hotdog"] and "no_hotdog" not in LauraX.recent_history:

        $ LauraX.change_face("surprised", 1)
        $ LauraX.mouth = "kiss"
        ch_l "What, just grinding?"

        if LauraX.Forced:
            $ LauraX.change_face("sad")
            ch_l ". . . nothing more?"


    if not LauraX.action_counter["hotdog"] and approval:

        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
        elif LauraX.love >= (LauraX.obedience + LauraX.inhibition):
            $ LauraX.change_face("sexy")
            $ LauraX.brows = "sad"
            $ LauraX.mouth = "smile"
            ch_l "If that's what you're into. . ."
        elif LauraX.obedience >= LauraX.inhibition:
            $ LauraX.change_face("normal")
            ch_l "If that's what works for you. . ."
        elif LauraX.addiction >= 50:
            $ LauraX.change_face("manic", 1)
            ch_l "Hrmm. . ."
        else:
            $ LauraX.change_face("sad")
            $ LauraX.mouth = "smile"
            ch_l "Well if that's what gets you off. . ."

    elif approval:

        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("love", 70, -3, 1)
            $ LauraX.change_stat("love", 20, -2, 1)
            ch_l "That's pushing it. . ."
        elif not Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "I guess this is a better location . ."
        elif "hotdog" in LauraX.recent_history:
            $ LauraX.change_face("sexy", 1)
            ch_l "Again? Fine, whatever."
            jump Laura_HotdogPrep
        elif "hotdog" in LauraX.daily_history:
            $ LauraX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",
                    "So you'd like another round?",
                    "You're really into this. . .",
                    "Are you sure that's all you want?"])
            ch_l "[Line]"
        else:
            $ LauraX.change_face("sexy", 1)
            $ LauraX.ArmPose = 2
            $ Line = renpy.random.choice(["Oooh, you want some of this?",
                    "So you'd like another round?",
                    "You're really into this. . .",
                    "You want another rub?"])
            ch_l "[Line]"
        $ Line = 0

    if approval >= 2:

        if LauraX.Forced:
            $ LauraX.change_face("sad")
            $ LauraX.change_stat("obedience", 80, 1)
            $ LauraX.change_stat("inhibition", 60, 1)
            ch_l "Ok, fine."
        elif "no_hotdog" in LauraX.daily_history:
            ch_l "It was rather entertaining. . ."
        else:
            $ LauraX.change_face("sexy", 1)
            $ LauraX.change_stat("love", 80, 1)
            $ LauraX.change_stat("inhibition", 50, 2)
            $ Line = renpy.random.choice(["Well, sure, let me give it a rub.",
                    "Very well.",
                    "Nice!",
                    "I guess we could do that.",
                    "Ok, let me. . .",
                    "Heh, ok, ok."])
            ch_l "[Line]"
            $ Line = 0
        $ LauraX.change_stat("obedience", 60, 1)
        $ LauraX.change_stat("inhibition", 70, 2)
        jump Laura_HotdogPrep
    else:


        $ LauraX.change_face("angry")
        if "no_hotdog" in LauraX.recent_history:
            ch_l "Sorry, [LauraX.player_petname] \"no.\""
        elif Taboo and "no_taboo" in LauraX.daily_history and "no_hotdog" in LauraX.daily_history:
            ch_l "I just told you. . .not in such an exposed location."
        elif "no_hotdog" in LauraX.daily_history:
            ch_l "I'm believe I just told you \"no,\" [LauraX.player_petname]."
        elif Taboo and "no_taboo" in LauraX.daily_history:
            ch_l "I told you. . . this place is too exposed."
        elif not LauraX.action_counter["hotdog"]:
            $ LauraX.change_face("bemused")
            ch_l "Hmm, that could be amusing, [LauraX.player_petname]. . ."
        else:
            $ LauraX.change_face("bemused")
            ch_l "I don't think that would be appropriate. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_hotdog" in LauraX.daily_history:
                $ LauraX.change_face("bemused")
                ch_l "So long as you don't push it."
                return
            "Maybe later?" if "no_hotdog" not in LauraX.daily_history:
                $ LauraX.change_face("sexy")
                ch_l "I gues eventually. . ."
                $ LauraX.change_stat("love", 80, 1)
                $ LauraX.change_stat("inhibition", 50, 1)
                if Taboo:
                    $ LauraX.recent_history.append("no_taboo")
                    $ LauraX.daily_history.append("no_taboo")
                $ LauraX.recent_history.append("no_hotdog")
                $ LauraX.daily_history.append("no_hotdog")
                return
            "You might like it. . .":
                if approval:
                    $ LauraX.change_face("sexy")
                    $ LauraX.change_stat("obedience", 60, 2)
                    $ LauraX.change_stat("inhibition", 50, 2)
                    $ Line = renpy.random.choice(["Yeah, probably. . .",
                                "I guess. . .",
                                "Good point. . ."])
                    ch_l "[Line]"
                    $ Line = 0
                    jump Laura_HotdogPrep
                else:
                    pass
            "Just deal with it.":

                $ approval = approval_check(LauraX, 350, "OI", TabM = 3)
                if approval > 1 or (approval and LauraX.Forced):
                    $ LauraX.change_face("sad")
                    $ LauraX.change_stat("love", 70, -2, 1)
                    $ LauraX.change_stat("love", 200, -2)
                    ch_l "Alright, fine."
                    $ LauraX.change_stat("obedience", 80, 4)
                    $ LauraX.change_stat("inhibition", 60, 2)
                    $ LauraX.Forced = 1
                    jump Laura_HotdogPrep
                else:
                    $ LauraX.change_stat("love", 200, -10)
                    $ LauraX.recent_history.append("angry")
                    $ LauraX.daily_history.append("angry")


    $ LauraX.ArmPose = 1

    if "no_hotdog" in LauraX.daily_history:
        ch_l "What did I tell you?"
        $ LauraX.recent_history.append("angry")
        $ LauraX.daily_history.append("angry")
    if LauraX.Forced:
        $ LauraX.change_face("angry", 1)
        ch_l "There's no point trying."
        $ LauraX.change_stat("lust", 200, 5)
        if LauraX.love > 300:
            $ LauraX.change_stat("love", 70, -1)
        $ LauraX.change_stat("obedience", 50, -1)
        $ LauraX.recent_history.append("angry")
        $ LauraX.daily_history.append("angry")
    elif Taboo:
        $ LauraX.change_face("angry", 1)
        $ LauraX.recent_history.append("no_taboo")
        $ LauraX.daily_history.append("no_taboo")
        ch_l "This area is a bit too exposed for that sort of thing. . ."
        $ LauraX.change_stat("lust", 200, 5)
        $ LauraX.change_stat("obedience", 50, -3)
    elif LauraX.action_counter["hotdog"]:
        $ LauraX.change_face("sad")
        ch_l "Not anymore."
    else:
        $ LauraX.change_face("normal", 1)
        ch_l "No thanks."
    $ LauraX.recent_history.append("no_hotdog")
    $ LauraX.daily_history.append("no_hotdog")
    $ approval_bonus = 0
    return

label Laura_HotdogPrep:
    call Seen_First_Peen (LauraX, Partner, React=action_context)
    call Laura_Sex_Launch ("hotdog")

    if action_context == LauraX:

        $ action_context = 0
        "[LauraX.name] rolls back and pulls you toward her, grinding against your cock."
        menu:
            "What do you do?"
            "Go with it.":
                $ LauraX.change_stat("inhibition", 80, 3)
                $ LauraX.change_stat("inhibition", 50, 2)
                "[LauraX.name] continues to grind."
            "Praise her.":
                $ LauraX.change_face("sexy", 1)
                $ LauraX.change_stat("inhibition", 80, 3)
                ch_p "Oh yeah, [LauraX.petname], let's do this."
                $ LauraX.nameCheck()
                "[LauraX.name] continues to grind."
                $ LauraX.change_stat("love", 85, 1)
                $ LauraX.change_stat("obedience", 90, 1)
                $ LauraX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ LauraX.change_face("surprised")
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
    elif action_context != "auto":


        if Taboo:
            "[LauraX.name] glances around to see if anyone notices what she's doing."
            if "cockout" in Player.recent_history:
                "Then she lays back and slowly presses against your rigid member."
            else:
                "Then she pulls down your pants and lays back."
                "She slowly presses against your rigid member."
            $ LauraX.inhibition += int(Taboo/10)
            $ LauraX.lust += int(Taboo/5)
        else:
            if "cockout" in Player.recent_history:
                "[LauraX.name] lays back and slowly presses against your rigid member."
            else:
                "[LauraX.name] pulls down your pants and lays back."
                "She slowly presses against your rigid member."
    else:

        "She lays back, pulling you against her with your rigid member."

    if not LauraX.action_counter["hotdog"]:
        if LauraX.Forced:
            $ LauraX.change_stat("love", 90, -5)
            $ LauraX.change_stat("obedience", 70, 20)
            $ LauraX.change_stat("inhibition", 80, 10)
        else:
            $ LauraX.change_stat("love", 90, 20)
            $ LauraX.change_stat("obedience", 70, 20)
            $ LauraX.change_stat("inhibition", 80, 20)


    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    $ primary_action = "hotdog"
    $ action_speed = 1
    if Taboo:
        $ LauraX.drain_word("no_taboo")
    $ LauraX.drain_word("no_hotdog")
    $ LauraX.recent_history.append("hotdog")
    $ LauraX.daily_history.append("hotdog")

label Laura_Hotdog_Cycle:
    while Round > 0:
        call shift_focus (LauraX)
        call Laura_Sex_Launch ("hotdog")
        if action_speed >= 4:
            $ action_speed = 2

        $ LauraX.lust_face()
        $ Player.cock_position = "out"
        $ primary_action = "hotdog"

        if Player.focus < 100:

            menu:
                "Keep going. . ." if action_speed:
                    pass
                "Keep going. . . (locked)" if not action_speed:
                    pass

                "Start moving? . ." if not action_speed:
                    $ action_speed = 1

                "Speed up. . ." if 0 < action_speed < 3:
                    $ action_speed += 1

                    "You ask her to up the pace a bit."
                "Speed up. . . (locked)" if action_speed >= 3:
                    pass

                "Slow Down. . ." if action_speed:
                    $ action_speed -= 1

                    "You ask her to slow it down a bit."
                "Slow Down. . . (locked)" if not action_speed:
                    pass
                "Slap her ass":

                    call Slap_Ass (LauraX)
                    $ counter += 1
                    $ Round -= 1
                    jump Laura_Hotdog_Cycle
                "Turn her Around":

                    $ LauraX.pose = "doggy" if LauraX.pose != "doggy" else 0
                    "You turn her around. . ."
                    jump Laura_Hotdog_Cycle

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
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
                                    "How about sex?":
                                        $ action_context = "shift"
                                        call Laura_HotdogAfter
                                        call Laura_Sex_P
                                    "Just stick it in her pussy [[without asking].":
                                        $ action_context = "auto"
                                        call Laura_HotdogAfter
                                        call Laura_Sex_P
                                    "How about anal?":
                                        $ action_context = "shift"
                                        call Laura_HotdogAfter
                                        call Laura_Sex_A
                                    "Just stick it in her ass [[without asking].":
                                        $ action_context = "auto"
                                        call Laura_HotdogAfter
                                        call Laura_Sex_A
                                    "Never Mind":
                                        jump Laura_Hotdog_Cycle
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
                                    jump Laura_Hotdog_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Laura_Hotdog_Cycle
                                "Never mind":
                                    jump Laura_Hotdog_Cycle
                        "Just take a look at her.":
                            $ Player.cock_position = 0
                            $ action_speed = 0

                        "Show her feet" if not ShowFeet and LauraX.pose == "doggy":
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and LauraX.pose == "doggy":
                            $ ShowFeet = 0
                        "Undress [LauraX.name]":

                            call Girl_Undress (LauraX)
                        "Clean up [LauraX.name] (locked)" if not LauraX.spunk:
                            pass
                        "Clean up [LauraX.name]" if LauraX.spunk:
                            call Girl_Cleanup (LauraX, "ask")
                        "Never mind":
                            jump Laura_Hotdog_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Laura_Sex_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Laura_HotdogAfter
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Laura_Sex_Reset
                    $ Line = 0
                    jump Laura_HotdogAfter


        call shift_focus (LauraX)
        call Sex_Dialog (LauraX, Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or LauraX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (LauraX)
                if "angry" in LauraX.recent_history:
                    call Laura_Sex_Reset
                    return
                $ LauraX.change_stat("lust", 200, 5)
                if 100 > LauraX.lust >= 70 and LauraX.session_orgasms < 2:
                    $ LauraX.recent_history.append("unsatisfied")
                    $ LauraX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Laura_HotdogAfter
                $ Line = "came"

            if LauraX.lust >= 100:

                call Girl_Cumming (LauraX)
                if action_context == "shift" or "angry" in LauraX.recent_history:
                    jump Laura_HotdogAfter

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "She's emptied you out, you'll need to take a break."
                    jump Laura_HotdogAfter
                elif "unsatisfied" in LauraX.recent_history:

                    $ Line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                    "[Line] Keep going?"
                    menu:
                        extend ""
                        "Yes, keep going for a bit." if Player.semen:
                            $ Line = "You get back into it"
                            jump Laura_Hotdog_Cycle
                        "No, I'm done." if Player.semen:
                            "You pull back."
                            jump Laura_HotdogAfter
                        "No, I'm spent." if not Player.semen:
                            "You pull back."
                            jump Laura_HotdogAfter
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if LauraX.SEXP >= 100 or approval_check(LauraX, 1200, "LO"):
            pass
        elif counter == (5 + LauraX.action_counter["hotdog"]):
            $ LauraX.brows = "confused"
            ch_l "Are we getting close here?"
        elif counter == (10 + LauraX.action_counter["hotdog"]):
            $ LauraX.brows = "angry"
            menu:
                ch_l "I'm kinda bored by this."
                "How about a BJ?" if LauraX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Laura_HotdogAfter
                    call Laura_Blowjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    $ counter += 1
                    jump Laura_Hotdog_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Laura_Sex_Reset
                    $ action_context = "shift"
                    jump Laura_HotdogAfter
                "No, get back down there.":
                    if approval_check(LauraX, 1200) or approval_check(LauraX, 500, "O"):
                        $ LauraX.change_stat("love", 200, -5)
                        $ LauraX.change_stat("obedience", 50, 3)
                        $ LauraX.change_stat("obedience", 80, 2)
                        "She grumbles but keeps moving."
                    else:
                        $ LauraX.change_face("angry", 1)
                        call Laura_Sex_Reset
                        "She scowls at you and pulls away."
                        ch_l "Not with that attitude."
                        $ LauraX.change_stat("love", 50, -3, 1)
                        $ LauraX.change_stat("love", 80, -4, 1)
                        $ LauraX.change_stat("obedience", 30, -1, 1)
                        $ LauraX.change_stat("obedience", 50, -1, 1)
                        $ LauraX.recent_history.append("angry")
                        $ LauraX.daily_history.append("angry")
                        jump Laura_HotdogAfter


        call Escalation (LauraX)

        if Round == 10:
            ch_l "It's getting kinda late. . ."
        elif Round == 5:
            ch_l "We should take a break for a minute."


    $ LauraX.change_face("bemused", 0)
    $ Line = 0
    ch_l "Ok, that's enough of that for now."

label Laura_HotdogAfter:
    if not action_context:
        $ Player.sprite = 0
        $ Player.cock_position = "out"
        call Laura_Sex_Reset

    $ LauraX.change_face("sexy")

    $ LauraX.action_counter["hotdog"] += 1
    $ LauraX.remaining_actions -=1
    $ LauraX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ LauraX.addiction_rate += 1
    $ LauraX.change_stat("inhibition", 30, 1)
    $ LauraX.change_stat("inhibition", 70, 1)

    call Partner_Like (LauraX, 2)

    if LauraX.action_counter["hotdog"] == 10:
        $ LauraX.SEXP += 5
    elif LauraX.action_counter["hotdog"] == 1:
        $ LauraX.SEXP += 10
        if not action_context:
            if LauraX.love >= 500 and "unsatisfied" not in LauraX.recent_history:
                ch_l "That was. . . nice."
            elif LauraX.obedience <= 500 and Player.focus <= 20:
                $ LauraX.mouth = "sad"
                ch_l "Enough for you?"
    elif not action_context:
        if "unsatisfied" in LauraX.recent_history:
            $ LauraX.change_face("angry")
            $ LauraX.eyes = "side"
            ch_l "That didn't do much for me. . ."

    $ approval_bonus = 0


    call checkout
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
