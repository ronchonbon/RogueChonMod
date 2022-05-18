
label Jean_SexAct(Act=0):
    if AloneCheck(JeanX) and JeanX.Taboo == 20:
        $ JeanX.Taboo = 0
        $ Taboo = 0
    call shift_focus (JeanX)
    if Act == "SkipTo":
        $ renpy.pop_call()
        $ renpy.pop_call()

        call SkipTo (JeanX)
    elif Act == "switch":
        $ renpy.pop_call()


    elif Act == "masturbate":
        call Jean_M_Prep
        if not action_context:
            return
    elif Act == "lesbian":
        call Les_Prep (JeanX)
        if not action_context:
            return
    elif Act == "kiss":
        call KissPrep (JeanX)
        if not action_context:
            return
    elif Act == "breasts":
        call Jean_Fondle_Breasts
        if not action_context:
            return
    elif Act == "blowjob":
        call Jean_BJ_Prep
        if not action_context:
            return
    elif Act == "handjob":
        call Jean_HJ_Prep
        if not action_context:
            return
    elif Act == "sex":
        call Jean_SexPrep
        if not action_context:
            return


label Jean_Masturbate:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JeanX)
    if JeanX.action_counter["masturbation"]:
        $ approval_bonus += 10
    if JeanX.SEXP >= 50:
        $ approval_bonus += 25
    elif JeanX.SEXP >= 30:
        $ approval_bonus += 15
    elif JeanX.SEXP >= 15:
        $ approval_bonus += 5
    if JeanX.lust >= 90:
        $ approval_bonus += 20
    elif JeanX.lust >= 75:
        $ approval_bonus += 5
    if "exhibitionist" in JeanX.traits:
        $ approval_bonus += (3*Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JeanX.traits:
        $ approval_bonus -= 40
    if JeanX.event_counter["forced"] and not JeanX.Forced:
        $ approval_bonus -= 5*JeanX.event_counter["forced"]

    $ approval = approval_check(JeanX, 1300, TabM = 2)

    $ JeanX.drain_word("unseen",1,0)

    if action_context == "join":
        if approval > 1 or (approval and JeanX.lust >= 50):
            $ Player.add_word(1,"join")
            menu:
                extend ""
                "Would you like some help? I could lend some helping hands. . ." if Player.semen and JeanX.remaining_actions:
                    $ JeanX.change_stat("love", 90, 1)
                    $ JeanX.change_stat("obedience", 50, 2)
                    $ JeanX.change_face("_sexy")
                    ch_j "Hmm, ok, give these a squeeze. . ."
                    $ JeanX.change_stat("obedience", 70, 2)
                    $ JeanX.change_stat("inhibition", 70, 1)
                    $ offhand_action = "fondle_breasts"
                    $ JeanX.action_counter["masturbation"] += 1
                    jump Jean_M_Cycle
                "Would you like some help? I could. . . up to you, I guess." if Player.semen and JeanX.remaining_actions:
                    $ JeanX.change_stat("love", 70, 2)
                    $ JeanX.change_stat("love", 90, 1)
                    $ JeanX.change_face("_sexy")
                    ch_j "Ok, sure. . ."
                    $ JeanX.change_stat("obedience", 70, 2)
                    $ JeanX.change_stat("inhibition", 70, 1)
                    $ D20 = renpy.random.randint(1, 20)
                    if D20 > 10:
                        $ offhand_action = "fondle_breasts"
                    else:
                        $ offhand_action = "suck_breasts"
                    $ JeanX.action_counter["masturbation"] += 1
                    jump Jean_M_Cycle
                "Why don't we take care of each other?" if Player.semen and JeanX.remaining_actions:
                    $ JeanX.change_face("_sexy")
                    ch_j "Like what?"
                    $ renpy.pop_call()
                    return
                "You look like you have things well in hand. . .":
                    if JeanX.lust >= 50:
                        $ JeanX.change_stat("love", 70, 2)
                        $ JeanX.change_stat("love", 90, 1)
                        $ JeanX.change_face("_sexy")
                        ch_j "I'm getting there. . ."
                        $ JeanX.change_stat("obedience", 80, 3)
                        $ JeanX.change_stat("inhibition", 80, 5)
                        jump Jean_M_Cycle
                    elif approval_check(JeanX, 1200):
                        $ JeanX.change_face("_sly")
                        ch_j "Yeah. . . but I can take a break. . ."
                    else:
                        $ JeanX.change_face("_angry")
                        ch_j "-well I -was.-"


        $ JeanX.ArmPose = 1
        $ JeanX.change_outfit()
        $ JeanX.remaining_actions -= 1
        $ Player.change_stat("focus", 50, 30)
        call checkout (1)
        $ Line = 0
        $ action_context = 0
        $ renpy.pop_call()
        if approval:
            $ JeanX.change_face("_bemused", 2)
            if bg_current == JeanX.home:
                ch_j "Why are you in my room?"
            else:
                ch_j "I didn't call for anyone. . ."
            $ JeanX.blushing = "_blush1"
        else:
            $ JeanX.change_stat("love", 200, -5)
            $ JeanX.change_face("_angry")
            $ JeanX.recent_history.append("_angry")
            $ JeanX.daily_history.append("_angry")
            if bg_current == JeanX.home:
                ch_j "I was busy, so get out."
                "[JeanX.name] kicks you out of her room."
                $ renpy.pop_call()
                jump Campus_Map
            else:
                ch_j "I'm leaving, but maybe knock next time?"
                call Remove_Girl (JeanX)
        return




    if action_context == JeanX:
        if approval > 2:
            if JeanX.PantsNum() == 5:
                "[JeanX.name]'s hand snakes down her body, and hikes up her skirt."
                $ JeanX.upskirt = 1
            elif JeanX.PantsNum() >= 6:
                "[JeanX.name] slides her hand down her body and into her pants."
            elif JeanX.HoseNum() >= 5:
                "[JeanX.name]'s hand slides down her body and under her [JeanX.hose]."
            elif JeanX.underwear:
                "[JeanX.name]'s hand slides down her body and under her [JeanX.underwear]."
            else:
                "[JeanX.name]'s hand slides down her body and begins to caress her pussy."
            $ JeanX.SeenPanties = 1
            call Jean_First_Bottomless (1)
            "She starts to slowly rub herself."
            menu:
                "What do you do?"
                "Nothing.":
                    $ JeanX.change_stat("inhibition", 80, 3)
                    $ JeanX.change_stat("inhibition", 60, 2)
                    "[JeanX.name] begins to masturbate."
                "Go for it.":
                    $ JeanX.change_face("sexy, 1")
                    $ JeanX.change_stat("inhibition", 80, 3)
                    ch_p "That is so sexy, [JeanX.petname]."
                    $ JeanX.nameCheck()
                    "You lean back and enjoy the show."
                    $ JeanX.change_stat("love", 80, 1)
                    $ JeanX.change_stat("obedience", 90, 1)
                    $ JeanX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ JeanX.change_face("_surprised")
                    $ JeanX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that right now, [JeanX.petname]."
                    $ JeanX.nameCheck()
                    "[JeanX.name] pulls her hands away from herself."
                    $ JeanX.change_outfit()
                    $ JeanX.change_stat("obedience", 90, 1)
                    $ JeanX.change_stat("obedience", 50, 1)
                    $ JeanX.change_stat("obedience", 30, 2)
                    return
            jump Jean_M_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
        return



    if not JeanX.action_counter["masturbation"]:
        $ JeanX.change_face("_surprised", 1)
        $ JeanX.mouth = "_kiss"
        ch_j "Oh, so you want to watch while I get off?"
        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            ch_j "But -just- watch, right? . ."



    if not JeanX.action_counter["masturbation"] and approval:
        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
        elif JeanX.love >= JeanX.obedience and JeanX.love >= (JeanX.inhibition - JeanX.IX):
            $ JeanX.change_face("_sexy")
            $ JeanX.brows = "_sad"
            $ JeanX.mouth = "_smile"
            ch_j "Well. . ."
        elif JeanX.obedience >= (JeanX.inhibition - JeanX.IX):
            $ JeanX.change_face("_normal")
            ch_j "If that's what you're into. . ."
        else:
            $ JeanX.change_face("_sad")
            $ JeanX.mouth = "_smile"
            ch_j "I do have some time. . ."



    elif approval:
        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
            ch_j "Hmm, again?"
        elif approval and "masturbation" in JeanX.recent_history:
            $ JeanX.change_face("_sexy", 1)
            ch_j "Mmmm . . ."
            jump Jean_M_Prep
        elif approval and "masturbation" in JeanX.daily_history:
            $ JeanX.change_face("_sexy", 1)
            $ Line = renpy.random.choice(["Did you enjoy that?",
                    "Didn't get enough earlier?",
                    "I do like having an audience. . ."])
            ch_j "[Line]"
        elif JeanX.action_counter["masturbation"] < 3:
            $ JeanX.change_face("_sexy", 1)
            $ JeanX.brows = "_confused"
            ch_j "You enjoyed that, huh."
        else:
            $ JeanX.change_face("_sexy", 1)
            $ JeanX.ArmPose = 2
            $ Line = renpy.random.choice(["You do like to watch.",
                    "Again?",
                    "You like to watch me.",
                    "You'd like me to masturbate again?"])
            ch_j "[Line]"
            $ Line = 0



    if approval >= 2:
        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("obedience", 90, 1)
            $ JeanX.change_stat("inhibition", 60, 1)
            ch_j "Oh. . . fine. . ."
        else:
            $ JeanX.change_face("_sexy", 1)
            $ JeanX.change_stat("love", 90, 1)
            $ JeanX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Sure. Ok.",
                    "Couldn't hurt. . .",
                    "All right.",
                    "Sure.",
                    "Sure, why not. . ."])
            ch_j "[Line]"
            $ Line = 0
        $ JeanX.change_stat("obedience", 20, 1)
        $ JeanX.change_stat("obedience", 60, 1)
        $ JeanX.change_stat("inhibition", 70, 2)
        jump Jean_M_Prep
    else:


        menu:
            ch_j "I don't know, it's kind of a bad time. . ."
            "Maybe later?":
                $ JeanX.change_face("_sexy", 1)
                if JeanX.lust > 70:
                    ch_j "Well -I- will, but after you leave."
                else:
                    ch_j "Wel. . . maybe. . ."
                $ JeanX.change_stat("love", 80, 2)
                $ JeanX.change_stat("inhibition", 70, 2)
                return
            "You look like you could use it. . .":
                if approval:
                    $ JeanX.change_face("_sexy")
                    $ JeanX.change_stat("obedience", 90, 2)
                    $ JeanX.change_stat("obedience", 50, 2)
                    $ JeanX.change_stat("inhibition", 70, 3)
                    $ JeanX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Sure. Ok.",
                                "Couldn't hurt. . .",
                                "All right.",
                                "Sure.",
                                "Sure, why not. . ."])
                    ch_j "[Line]"
                    $ Line = 0
                    jump Jean_M_Prep
            "Just get at it already.":

                $ approval = approval_check(JeanX, 450, "OI", TabM = 2)
                if approval > 1 or (approval and JeanX.Forced):
                    $ JeanX.change_face("_sad")
                    $ JeanX.change_stat("love", 70, -5, 1)
                    $ JeanX.change_stat("love", 200, -5)
                    ch_j "Oh. . . fine. . ."
                    $ JeanX.change_stat("obedience", 80, 4)
                    $ JeanX.change_stat("inhibition", 80, 1)
                    $ JeanX.change_stat("inhibition", 60, 3)
                    $ JeanX.Forced = 1
                    jump Jean_M_Prep
                else:
                    $ JeanX.change_stat("love", 200, -20)
                    $ JeanX.recent_history.append("_angry")
                    $ JeanX.daily_history.append("_angry")



    $ JeanX.ArmPose = 1
    if JeanX.Forced:
        $ JeanX.change_face("_angry", 1)
        ch_j "Nope, too kinky."
        $ JeanX.change_stat("lust", 90, 5)
        if JeanX.love > 300:
            $ JeanX.change_stat("love", 70, -2)
        $ JeanX.change_stat("obedience", 50, -2)
        $ JeanX.recent_history.append("_angry")
        $ JeanX.daily_history.append("_angry")
        $ JeanX.recent_history.append("no_masturbation")
        $ JeanX.daily_history.append("no_masturbation")
        return
    elif JeanX.Taboo:
        $ JeanX.change_face("_angry", 1)
        $ JeanX.daily_history.append("no_taboo")
        ch_j "I. . . couldn't do that in public. . ."
        $ JeanX.change_stat("lust", 90, 5)
        $ JeanX.change_stat("obedience", 50, -3)
        return
    elif JeanX.action_counter["masturbation"]:
        $ JeanX.change_face("_sad")
        ch_j "Eh, I think I'm ok for now. . ."
    else:
        $ JeanX.change_face("_normal", 1)
        ch_j "Um, no."
    $ JeanX.recent_history.append("no_masturbation")
    $ JeanX.daily_history.append("no_masturbation")
    $ approval_bonus = 0
    return

label Jean_M_Prep:
    $ JeanX.upskirt = 1
    $ JeanX.underwear_pulled_down = 1
    call Jean_First_Bottomless (1)
    call set_the_scene (Dress=0)


    if "unseen" in JeanX.recent_history:
        $ JeanX.change_face("_sexy")
        $ JeanX.eyes = "_closed"
        $ JeanX.ArmPose = 2
        "You see [JeanX.name] leaning back, masturbating. You don't think she's noticed you yet."
    else:
        $ JeanX.change_face("_sexy")
        $ JeanX.ArmPose = 2
        "[JeanX.name] lays back and starts to toy with herself."
        if not JeanX.action_counter["masturbation"]:
            if JeanX.Forced:
                $ JeanX.change_stat("love", 90, -20)
                $ JeanX.change_stat("obedience", 70, 45)
                $ JeanX.change_stat("inhibition", 80, 35)
            else:
                $ JeanX.change_stat("love", 90, 15)
                $ JeanX.change_stat("obedience", 70, 35)
                $ JeanX.change_stat("inhibition", 80, 40)


    $ primary_action = "masturbation"
    if not girl_offhand_action:
        $ girl_offhand_action = "fondle_pussy"

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    if JeanX.Taboo:
        $ JeanX.drain_word("no_taboo")
    $ JeanX.drain_word("no_masturbation")
    $ JeanX.recent_history.append("masturbation")
    $ JeanX.daily_history.append("masturbation")

label Jean_M_Cycle:
    if action_context == "join":
        $ renpy.pop_call()
        $ action_context = 0

    while Round > 0:
        call Jean_Pos_Reset ("masturbation")
        call shift_focus (JeanX)
        $ JeanX.lust_face()

        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if Player.focus < 100:

            menu:
                "Keep Watching.":
                    pass

                "[JeanX.name]. . .[[jump in]" if "unseen" not in JeanX.recent_history and "join" not in Player.recent_history and JeanX.location == bg_current:
                    "[JeanX.name] slows what she's doing with a sly grin."
                    ch_j "Like what you see?"
                    $ action_context = "join"
                    call Jean_Masturbate
                "\"Ahem. . .\"" if "unseen" in JeanX.recent_history and JeanX.location == bg_current:
                    jump Jean_M_Interupted

                "Start jack'in it." if offhand_action != "jackin":
                    call Jackin (JeanX)
                "Stop jack'in it." if offhand_action == "jackin":
                    $ offhand_action = 0

                "Slap her ass" if JeanX.location == bg_current:
                    if "unseen" in JeanX.recent_history:
                        "You smack [JeanX.name] firmly on the ass!"
                        jump Jean_M_Interupted
                    else:
                        call Slap_Ass (JeanX)
                        $ counter += 1
                        $ Round -= 1
                        jump Jean_M_Cycle

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
                        "Offhand action" if JeanX.location == bg_current:
                            if JeanX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ JeanX.remaining_actions -= 1
                            else:
                                ch_j "I'd like to stick with this."

                        "Threesome actions (locked)" if not Partner or "unseen" in JeanX.recent_history or JeanX.location != bg_current:
                            pass
                        "Threesome actions" if Partner and "unseen" not in JeanX.recent_history and JeanX.location == bg_current:
                            menu:
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (JeanX)
                                "Swap to [Partner.name]":
                                    call primary_action_Swap (JeanX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Jean_M_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jean_M_Cycle
                                "Never mind":
                                    jump Jean_M_Cycle

                        "Show her feet" if not ShowFeet and JeanX.pose == "doggy":
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and JeanX.pose == "doggy":
                            $ ShowFeet = 0
                        "Undress [JeanX.name]":

                            if "unseen" in JeanX.recent_history:
                                ch_p "Oh, yeah, take it off. . ."
                                jump Jean_M_Interupted
                            else:
                                call Girl_Undress (JeanX)
                        "Clean up [JeanX.name] (locked)" if not JeanX.spunk:
                            pass
                        "Clean up [JeanX.name]" if JeanX.spunk:
                            if "unseen" in JeanX.recent_history:
                                ch_p "You've got a little something on you. . ."
                                jump Jean_M_Interupted
                            else:
                                call Girl_Cleanup (JeanX, "ask")
                        "Never mind":
                            jump Jean_M_Cycle

                "Back to Sex Menu" if multi_action and JeanX.location == bg_current:
                    ch_p "Let's try something else."
                    call Jean_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jean_M_Interupted
                "End Scene" if not multi_action or JeanX.location != bg_current:
                    ch_p "Let's stop for now."
                    call Jean_Pos_Reset
                    $ Line = 0
                    jump Jean_M_Interupted


        call shift_focus (JeanX)
        call Sex_Dialog (JeanX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus

        if Player.focus >= 100 or JeanX.lust >= 100:

            if Player.focus >= 100:
                if "unseen" not in JeanX.recent_history:

                    call Player_Cumming (JeanX)
                    if "_angry" in JeanX.recent_history:
                        call Jean_Pos_Reset
                        return
                    $ JeanX.change_stat("lust", 200, 5)
                    if 100 > JeanX.lust >= 70 and JeanX.session_orgasms < 2:
                        $ JeanX.recent_history.append("unsatisfied")
                        $ JeanX.daily_history.append("unsatisfied")
                    $ Line = "came"
                else:
                    "You grunt and try to hold it in."
                    $ Player.focus = 95
                    if JeanX.location == bg_current:
                        jump Jean_M_Interupted


            if JeanX.lust >= 100:
                call Girl_Cumming (JeanX)
                if JeanX.location == bg_current:
                    jump Jean_M_Interupted

            if Line == "came":
                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."
                    $ offhand_action = 0 if offhand_action == "jackin" else offhand_action


                if "unsatisfied" in JeanX.recent_history:
                    "[JeanX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Let her keep going?"
                        "Yes, keep going for a bit.":
                            $ Line = "You let her get back into it"
                            jump Jean_M_Cycle
                        "No, I'm done.":
                            "You ask her to stop."
                            return
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        if "unseen" in JeanX.recent_history:
            if Round == 10:
                "It's getting a bit late, [JeanX.name] will probably be wrapping up soon."
            elif Round == 5:
                "She's definitely going to stop soon."
        else:
            if JeanX.location == bg_current:
                call Escalation (JeanX)

            if Round == 10:
                ch_j "Wow, look at the time. . ."
                $ JeanX.lust += 10
            elif Round == 5:
                ch_j "Ok, can we take a break?"
                $ JeanX.lust += 25


    $ JeanX.change_face("_bemused", 0)
    $ Line = 0
    if "unseen" not in JeanX.recent_history:
        ch_j "Ok, that's it, break time."

label Jean_M_Interupted:


    if "unseen" in JeanX.recent_history:
        $ JeanX.change_face("_surprised", 2)
        "[JeanX.name] stops what she's doing with a start, eyes wide."
        call Jean_First_Bottomless (1)
        $ JeanX.change_face("_surprised", 2)


        if offhand_action == "jackin":
            ch_j "Oh, hey. . .[JeanX.player_petname]."
            ch_j "When did you get here?"
            $ JeanX.eyes = "_down"
            menu:
                ch_j "I see you've been making yourself at home. . . "
                "A while back, it was an excellent show.":
                    $ JeanX.change_face("_sexy",1)
                    $ JeanX.change_stat("obedience", 50, 3)
                    $ JeanX.change_stat("obedience", 70, 2)
                    ch_j "True. . ."
                    if JeanX.love >= 800 or JeanX.obedience >= 500 or (JeanX.inhibition - JeanX.IX) >= 500:
                        $ approval_bonus += 10
                        $ JeanX.change_stat("lust", 90, 5)
                        ch_j "And you can put on quite a show yourself. . ."
                "I. . . just got here?":

                    $ JeanX.change_face("_angry",1)
                    $ JeanX.change_stat("love", 70, 2)
                    $ JeanX.change_stat("love", 90, 1)
                    $ JeanX.change_stat("obedience", 50, 2)
                    $ JeanX.change_stat("obedience", 70, 2)
                    "She looks pointedly at your cock,"
                    ch_j "A likely story. . ."
                    if JeanX.love >= 800 or JeanX.obedience >= 500 or (JeanX.inhibition - JeanX.IX) >= 500:
                        $ approval_bonus += 10
                        $ JeanX.change_stat("lust", 90, 5)
                        $ JeanX.change_face("_bemused", 1)
                        ch_j "I guess I can't blame you. . ."
                    else:
                        $ approval_bonus -= 10
                        $ JeanX.change_stat("lust", 200, -5)
            call Seen_First_Peen (JeanX, Partner)
            ch_j "Hmm. . ."
        else:


            ch_j "Oh, hey. . .[JeanX.player_petname]."
            ch_j "When did you get here?"
            menu:
                extend ""
                "A while back.":
                    $ JeanX.change_face("_sexy", 1)
                    $ JeanX.change_stat("obedience", 50, 3)
                    $ JeanX.change_stat("obedience", 70, 2)
                    ch_j "Nice of you to let me know. . ."
                "I just got here.":
                    $ JeanX.change_face("_bemused", 1)
                    $ JeanX.change_stat("love", 70, 2)
                    $ JeanX.change_stat("love", 90, 1)
                    ch_j "Uh-huh. . ."
                    $ JeanX.change_stat("obedience", 50, 2)
                    $ JeanX.change_stat("obedience", 70, 2)

        $ JeanX.drain_word("unseen",1,0)
        $ JeanX.action_counter["masturbation"] += 1
        if Round <= 10:
            ch_j "I could use a break anyway. . ."
            return
        $ action_context = "join"
        call Jean_Masturbate
        "error: report this if you see it."
        return



    $ JeanX.remaining_actions -= 1
    $ JeanX.action_counter["masturbation"] += 1
    call checkout
    if action_context == "shift":
        $ action_context = 0
        return
    $ action_context = 0

    if Partner == EmmaX:
        call Partner_Like (JeanX, 3)
    else:
        call Partner_Like (JeanX, 2)

    if JeanX.location != bg_current:
        return

    if Round <= 10:
        ch_j "I need a minute here. . ."
        return
    $ JeanX.change_face("_sexy", 1)
    if JeanX.lust < 20:
        ch_j "I got off, how about you?"
    else:
        ch_j "So, what next?"
    menu:
        extend ""
        "Well, I have something you could take care of. . ." if Player.semen and JeanX.remaining_actions:
            $ action_context = "shift"
            return
        "You could just keep going. . ." if Player.semen:
            $ JeanX.change_face("_sly")
            if JeanX.remaining_actions and Round >= 10:
                ch_j "Ok. . ."
                jump Jean_M_Cycle
            else:
                ch_j "I need a minute here. . ."
        "I'm good here. [[Stop]":
            if JeanX.love < 800 and JeanX.inhibition < 500 and JeanX.obedience < 500:
                $ JeanX.change_outfit()
            $ JeanX.change_face("_normal")
            $ JeanX.brows = "_confused"
            ch_j "Ok."
            $ JeanX.brows = "_normal"
        "You should probably stop for now." if JeanX.lust > 30:
            $ JeanX.change_face("_angry")
            ch_j "Hrmm."
    return








label Jean_Sex_P:

    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JeanX)
    if JeanX.action_counter["sex"] >= 7:
        $ approval_bonus += 15
    elif JeanX.action_counter["sex"] >= 3:
        $ approval_bonus += 12
    elif JeanX.action_counter["sex"]:
        $ approval_bonus += 10

    if JeanX.addiction >= 75 and (JeanX.event_counter["creampied"] + JeanX.event_counter["anal_creampied"]) >=3:
        $ approval_bonus += 20
    elif JeanX.addiction >= 75:
        $ approval_bonus += 15

    if JeanX.lust > 85:
        $ approval_bonus += 10
    elif JeanX.lust > 75:
        $ approval_bonus += 5

    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in JeanX.traits:
        $ approval_bonus += (4*Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JeanX.traits:
        $ approval_bonus -= 40
    if JeanX.event_counter["forced"] and not JeanX.Forced:
        $ approval_bonus -= 5*JeanX.event_counter["forced"]



    if JeanX.Taboo and "no_taboo" in JeanX.daily_history:
        $ approval_bonus -= 10

    if "no_sex" in JeanX.daily_history:
        $ approval_bonus -= 15 if "no_sex" in JeanX.recent_history else 5


    $ approval = approval_check(JeanX, 1400, TabM = 5)

    if action_context == "auto":
        call Jean_Sex_Launch ("sex")
        if JeanX.PantsNum() == 5:
            "You flip [JeanX.name] around, sliding her skirt up as you go."
            $ JeanX.upskirt = 1
        elif JeanX.PantsNum() >= 6:
            "You flip [JeanX.name] around, sliding her pants down as you do."
            $ JeanX.upskirt = 1
        else:
            "You flip [JeanX.name] around."
        $ JeanX.SeenPanties = 1
        "You rub the tip of your cock against her moist slit."
        $ JeanX.change_face("_surprised", 1)

        if (JeanX.action_counter["sex"] and approval) or (approval > 1):

            "[JeanX.name] glances back and then breaks into a smile."
            $ JeanX.change_face("_sly")
            $ JeanX.change_stat("obedience", 70, 3)
            $ JeanX.change_stat("inhibition", 50, 3)
            $ JeanX.change_stat("inhibition", 70, 1)
            ch_j "Oh, if you must, [JeanX.player_petname]."
            jump Jean_SexPrep
        else:

            $ JeanX.brows = "_angry"
            menu:
                ch_j "Just sticking it in?"
                "Sorry, sorry! Never mind.":
                    if approval:
                        $ JeanX.change_face("_sexy", 1)
                        $ JeanX.change_stat("obedience", 70, 3)
                        $ JeanX.change_stat("inhibition", 50, 3)
                        $ JeanX.change_stat("inhibition", 70, 1)
                        ch_j "Oh, no, it's fine."
                        jump Jean_SexPrep
                    else:
                        "You pull back before you really get it in."
                        $ JeanX.change_face("_bemused", 1)

                        ch_j "You should ask first, [JeanX.player_petname]."
                "Just fucking.":


                    $ JeanX.change_stat("love", 80, -10, 1)
                    $ JeanX.change_stat("love", 200, -10)
                    "You press inside some more."
                    $ JeanX.change_stat("obedience", 70, 3)
                    $ JeanX.change_stat("inhibition", 50, 3)
                    if not approval_check(JeanX, 700, "O", TabM=1):
                        $ JeanX.change_face("_angry")
                        "[JeanX.name] shoves you away and backhands you in the face."
                        ch_j "Hey, I don't need my powers to hurt you."
                        $ JeanX.change_stat("love", 50, -10, 1)
                        $ JeanX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        call Jean_Sex_Reset
                        $ JeanX.recent_history.append("_angry")
                        $ JeanX.daily_history.append("_angry")
                    else:
                        $ JeanX.change_face("_sad")
                        "[JeanX.name] doesn't seem to be into this, you're lucky she's willing to give it a try."
                        jump Jean_SexPrep
        return



    if not JeanX.action_counter["sex"] and "no_sex" not in JeanX.recent_history:

        $ JeanX.change_face("_surprised", 1)
        $ JeanX.mouth = "_kiss"
        ch_j "Oh, you wanna fuck . . "
        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            ch_j "Pretty bold of you. . ."


    if not JeanX.action_counter["sex"] and approval:

        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("love", 70, -30, 1)
            $ JeanX.change_stat("love", 20, -20, 1)
        elif JeanX.love >= (JeanX.obedience + JeanX.inhibition - JeanX.IX):
            $ JeanX.change_face("_sexy")
            $ JeanX.brows = "_sad"
            $ JeanX.mouth = "_smile"
            ch_j "I was wondering when this would come up. . ."
        elif JeanX.obedience >= (JeanX.inhibition - JeanX.IX):
            $ JeanX.change_face("_normal")
            ch_j "Ok, [JeanX.player_petname]. . ."
        elif JeanX.addiction >= 50:
            $ JeanX.change_face("_manic", 1)
            ch_j "That does sound fun. . ."
        else:
            $ JeanX.change_face("_sad")
            $ JeanX.mouth = "_smile"
            ch_j "I was wondering when this would come up. . ."


    elif approval:

        $ JeanX.change_face("_sexy", 1)
        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
            ch_j "You'll pay for this eventually. . ."
        elif not JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "Ok, yeah, this is better."
        elif "sex" in JeanX.recent_history:
            ch_j "Again? Your funeral."
            jump Jean_SexPrep
        elif "sex" in JeanX.daily_history:
            $ Line = renpy.random.choice(["Back again?",
                    "You'd like another round?",
                    "I must be better than I thought.",
                    "Didn't get enough earlier?",
                    "Your funeral, " + JeanX.player_petname + "."])
            ch_j "[Line]"
        elif JeanX.action_counter["sex"] < 3:
            $ JeanX.brows = "_confused"
            $ JeanX.mouth = "_kiss"
            ch_j "Oh? Another round?"
        else:
            $ Line = renpy.random.choice(["Oh, you want some of this?",
                    "You'd like another round?",
                    "I must be better than I thought.",
                    "I hope you don't plan on wearing me out.",
                    "You want to fuck me?"])
            ch_j "[Line]"
        $ Line = 0


    if approval >= 2:

        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("obedience", 90, 1)
            $ JeanX.change_stat("inhibition", 60, 1)
            ch_j "Ok, fine. Just make it good."
        elif "no_sex" in JeanX.daily_history:
            ch_j "Ok, whatever. . ."
        else:
            $ JeanX.change_face("_sexy", 1)
            $ JeanX.change_stat("love", 90, 1)
            $ JeanX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well. . . fine, let's do it.",
                    "Sure.",
                    "We could, I guess.",
                    "Hmmm, sure.",
                    "Sounds fun."])
            ch_j "[Line]"
            $ Line = 0
        $ JeanX.change_stat("obedience", 20, 1)
        $ JeanX.change_stat("obedience", 60, 1)
        $ JeanX.change_stat("inhibition", 70, 2)
        jump Jean_SexPrep
    else:


        $ JeanX.change_face("_angry")
        if "no_sex" in JeanX.recent_history:
            ch_j "I don't repeat myself."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history and "no_sex" in JeanX.daily_history:
            ch_j "I'm not comfortable with that. . ."
        elif "no_sex" in JeanX.daily_history:
            ch_j "Not today."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "I told you, I'm not comfortable with that. . ."
        elif not JeanX.action_counter["sex"]:
            $ JeanX.change_face("_bemused")
            ch_j "Oh, this would be interesting. . ."
        else:
            $ JeanX.change_face("_bemused")
            ch_j "I'm not in the mood right now . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_sex" in JeanX.daily_history:
                $ JeanX.change_face("_bemused")
                ch_j "Keep trying. . ."
                return
            "Maybe later?" if "no_sex" not in JeanX.daily_history:
                $ JeanX.change_face("_sexy")
                ch_j "Sure, whatever. . ."
                $ JeanX.change_stat("love", 80, 2)
                $ JeanX.change_stat("inhibition", 70, 2)
                if JeanX.Taboo:
                    $ JeanX.recent_history.append("no_taboo")
                    $ JeanX.daily_history.append("no_taboo")
                $ JeanX.recent_history.append("no_sex")
                $ JeanX.daily_history.append("no_sex")
                return
            "I think you'd enjoy it as much as I would. . .":
                if approval:
                    $ JeanX.change_face("_sexy")
                    $ JeanX.change_stat("obedience", 90, 2)
                    $ JeanX.change_stat("obedience", 50, 2)
                    $ JeanX.change_stat("inhibition", 70, 3)
                    $ JeanX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Yeah, probably. . .",
                                "I guess. . .",
                                "Good point. . ."])
                    ch_j "[Line]"
                    $ Line = 0
                    jump Jean_SexPrep
            "Just deal with it.":
                $ approval = approval_check(JeanX, 1150, "OI", TabM = 3)
                if approval > 1 or (approval and JeanX.Forced):
                    $ JeanX.change_face("_confused",Eyes="_side")
                    $ JeanX.change_stat("love", 70, -5, 1)
                    $ JeanX.change_stat("love", 200, -5)
                    ch_j ". . ."
                    ch_j ". . . Ok. . ."
                    $ JeanX.change_stat("obedience", 80, 4)
                    $ JeanX.change_stat("inhibition", 80, 1)
                    $ JeanX.change_stat("inhibition", 60, 3)
                    $ JeanX.Forced = 1
                    jump Jean_SexPrep
                else:
                    $ JeanX.change_stat("love", 200, -20)
                    $ JeanX.recent_history.append("_angry")
                    $ JeanX.daily_history.append("_angry")




    $ JeanX.ArmPose = 1
    if "no_sex" in JeanX.daily_history:
        ch_j "Don't push your luck, [JeanX.player_petname]."
        $ JeanX.recent_history.append("_angry")
        $ JeanX.daily_history.append("_angry")
    elif JeanX.Forced:
        $ JeanX.change_face("_angry", 1)
        ch_j "I'm the queen here!"
        $ JeanX.change_stat("lust", 200, 5)
        if JeanX.love > 300:
            $ JeanX.change_stat("love", 70, -2)
        $ JeanX.change_stat("obedience", 50, -2)
        ch_j "I do not take orders."
        $ JeanX.recent_history.append("_angry")
        $ JeanX.daily_history.append("_angry")
    elif JeanX.Taboo:
        $ JeanX.change_face("_angry", 1)
        $ JeanX.recent_history.append("no_taboo")
        $ JeanX.daily_history.append("no_taboo")
        ch_j "I'm just not comfortable with that right now. . ."
        $ JeanX.change_stat("lust", 200, 5)
        $ JeanX.change_stat("obedience", 50, -3)
    elif JeanX.action_counter["sex"]:
        $ JeanX.change_face("_sad")
        ch_j "Maybe just fuck one of the others."
    else:
        $ JeanX.change_face("_normal", 1)
        ch_j "Not interested."
    $ JeanX.recent_history.append("no_sex")
    $ JeanX.daily_history.append("no_sex")
    $ approval_bonus = 0
    return

label Jean_SexPrep:
    call Seen_First_Peen (JeanX, Partner, React=action_context)
    call Jean_Sex_Launch ("hotdog")

    if action_context == JeanX:

        $ action_context = 0
        if JeanX.PantsNum() == 5:
            "[JeanX.name] turns around, sliding her skirt up as she does so."
            $ JeanX.upskirt = 1
        elif JeanX.PantsNum() >= 6:
            "[JeanX.name] turns around, sliding her [JeanX.legs] down as she does so."
            $ JeanX.upskirt = 1
        else:
            "[JeanX.name] turns around and pulls you toward her."
        $ JeanX.SeenPanties = 1
        "She slides the tip along her pussy and seems to want you to insert it."
        menu:
            "What do you do?"
            "Go with it.":
                $ JeanX.change_stat("inhibition", 80, 3)
                $ JeanX.change_stat("inhibition", 50, 2)
                "[JeanX.name] slides it in."
            "Praise her.":
                $ JeanX.change_face("_sexy", 1)
                $ JeanX.change_stat("inhibition", 80, 3)
                ch_p "Oh yeah, [JeanX.petname], let's do this."
                $ JeanX.nameCheck()
                "Jean slides it in."
                $ JeanX.change_stat("love", 85, 1)
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ JeanX.change_face("_surprised")
                $ JeanX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [JeanX.petname]."
                $ JeanX.nameCheck()
                "[JeanX.name] pulls back."
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("obedience", 50, 1)
                $ JeanX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ JeanX.add_word(1,"refused","refused")
                return
        $ JeanX.underwear_pulled_down = 1
        call Jean_First_Bottomless (1)

    elif action_context != "auto":
        call AutoStrip (JeanX)

        if JeanX.Taboo:
            "[JeanX.name] glances around to see if anyone notices what she's doing."
            if "cockout" in Player.recent_history:
                "Then she turns around and slowly presses against your rigid member."
            else:
                "Then she pulls down your pants and turns around."
                "She slowly presses against your rigid member."
            $ JeanX.change_stat("inhibition", 90, int(Taboo/10))
            $ JeanX.change_stat("lust", 50, int(Taboo/5))
        else:
            if "cockout" in Player.recent_history:
                "[JeanX.name] turns around and slowly presses against your rigid member."
            else:
                "[JeanX.name] pulls down your pants and turns around."
                "She slowly presses against your rigid member."
        "She leans back a bit and your cock slides in."
    else:

        if (JeanX.PantsNum() >= 6 and not JeanX.upskirt) and (JeanX.underwear and not JeanX.underwear_pulled_down):
            "You quickly pull down her pants and her [JeanX.underwear] and press against her slit."
        elif (JeanX.underwear and not JeanX.underwear_pulled_down):
            "You quickly pull down her [JeanX.underwear] and press against her slit."
        $ JeanX.upskirt = 1
        $ JeanX.underwear_pulled_down = 1
        $ JeanX.SeenPanties = 1
        call Jean_First_Bottomless (1)

    if Player.focus >= 50:
        ch_j "I see you won't need any encouragement. . ."
    if not JeanX.action_counter["sex"]:
        if JeanX.Forced:
            $ JeanX.change_stat("love", 90, -150)
            $ JeanX.change_stat("obedience", 70, 60)
            $ JeanX.change_stat("inhibition", 80, 50)
        else:
            $ JeanX.change_stat("love", 90, 30)
            $ JeanX.change_stat("obedience", 70, 30)
            $ JeanX.change_stat("inhibition", 80, 60)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    $ Player.cock_position = "in"
    $ primary_action = "sex"
    $ action_speed = 1
    if JeanX.Taboo:
        $ JeanX.drain_word("no_taboo")
    $ JeanX.drain_word("no_sex")
    $ JeanX.recent_history.append("sex")
    $ JeanX.daily_history.append("sex")

label Jean_Sex_Cycle:
    while Round > 0:
        call shift_focus (JeanX)
        call Jean_Sex_Launch ("sex")
        if action_speed >= 4:
            $ action_speed = 2

        $ JeanX.lust_face()
        $ Player.sprite = 1
        $ Player.cock_position = "in"
        $ primary_action = "sex"
        $ JeanX.upskirt = 1
        $ JeanX.underwear_pulled_down = 1

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

                    call Slap_Ass (JeanX)
                    $ counter += 1
                    $ Round -= 1
                    jump Jean_Sex_Cycle
                "Turn her Around":
                    $ JeanX.pose = "doggy" if JeanX.pose != "doggy" else "sex"
                    "You turn her around. . ."
                    jump Jean_Sex_Cycle

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
                            if JeanX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ JeanX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (JeanX, "tired")
                        "Shift primary action":

                            if JeanX.remaining_actions and multi_action:
                                menu:
                                    "How about anal?":
                                        $ action_context = "shift"
                                        call Jean_SexAfter
                                        call Jean_Sex_A
                                    "Just stick it in her ass [[without asking].":
                                        $ action_context = "auto"
                                        call Jean_SexAfter
                                        call Jean_Sex_A
                                    "Pull back to hotdog her.":
                                        $ action_context = "pullback"
                                        call Jean_SexAfter
                                        call Jean_Sex_H
                                    "Never Mind":
                                        jump Jean_Sex_Cycle
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
                                    jump Jean_Sex_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jean_Sex_Cycle
                                "Never mind":
                                    jump Jean_Sex_Cycle
                        "Just take a look at her.":
                            $ Player.cock_position = 0
                            $ action_speed = 0

                        "Show her feet" if not ShowFeet and JeanX.pose == "doggy":
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and JeanX.pose == "doggy":
                            $ ShowFeet = 0
                        "Undress [JeanX.name]":

                            call Girl_Undress (JeanX)
                        "Clean up [JeanX.name] (locked)" if not JeanX.spunk:
                            pass
                        "Clean up [JeanX.name]" if JeanX.spunk:
                            call Girl_Cleanup (JeanX, "ask")
                        "Never mind":
                            jump Jean_Sex_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jean_Sex_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jean_SexAfter
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jean_Sex_Reset
                    $ Line = 0
                    jump Jean_SexAfter


        call shift_focus (JeanX)
        call Sex_Dialog (JeanX, Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or JeanX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (JeanX)
                if "_angry" in JeanX.recent_history:
                    call Jean_Sex_Reset
                    return
                $ JeanX.change_stat("lust", 200, 5)
                if 100 > JeanX.lust >= 70 and JeanX.session_orgasms < 2:
                    $ JeanX.recent_history.append("unsatisfied")
                    $ JeanX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jean_SexAfter
                $ Line = "came"

            if JeanX.lust >= 100:

                call Girl_Cumming (JeanX)
                if action_context == "shift" or "_angry" in JeanX.recent_history:
                    jump Jean_SexAfter

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "She's emptied you out, you'll need to take a break."
                    jump Jean_SexAfter
                elif "unsatisfied" in JeanX.recent_history:

                    $ Line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                    "[Line] Keep going?"
                    menu:
                        extend ""
                        "Yes, keep going for a bit." if Player.semen:
                            $ Line = "You get back into it"
                            jump Jean_Sex_Cycle
                        "No, I'm done." if Player.semen:
                            "You pull back."
                            jump Jean_SexAfter
                        "No, I'm spent." if not Player.semen:
                            "You pull back."
                            jump Jean_SexAfter
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if JeanX.SEXP >= 100 or approval_check(JeanX, 1200, "LO"):
            pass
        elif counter == (5 + JeanX.action_counter["sex"]):
            $ JeanX.brows = "_confused"
            ch_j "Ok, had enough yet?"
        elif counter == (10 + JeanX.action_counter["sex"]):
            $ JeanX.brows = "_angry"
            menu:
                ch_j "Hey. . . you. . . about done. . . there?"
                "How about a BJ?" if JeanX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Jean_SexAfter
                    call Jean_Blowjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    $ counter += 1
                    jump Jean_Sex_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Jean_Sex_Reset
                    $ action_context = "shift"
                    jump Jean_SexAfter
                "No, get back down there.":
                    if approval_check(JeanX, 1200) or approval_check(JeanX, 500, "O"):
                        $ JeanX.change_stat("love", 200, -5)
                        $ JeanX.change_stat("obedience", 50, 3)
                        $ JeanX.change_stat("obedience", 80, 2)
                        "She grumbles but keeps moving."
                    else:
                        $ JeanX.change_face("_angry", 1)
                        call Jean_Sex_Reset
                        "She scowls at you and pulls out."
                        ch_j "Don't overestimate yourself."
                        $ JeanX.change_stat("love", 50, -3, 1)
                        $ JeanX.change_stat("love", 80, -4, 1)
                        $ JeanX.change_stat("obedience", 30, -1, 1)
                        $ JeanX.change_stat("obedience", 50, -1, 1)
                        $ JeanX.recent_history.append("_angry")
                        $ JeanX.daily_history.append("_angry")
                        jump Jean_SexAfter


        call Escalation (JeanX)

        if Round == 10:
            call Sex_Basic_Dialog (JeanX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JeanX, 5)


    $ JeanX.change_face("_bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JeanX, "done")

label Jean_SexAfter:
    if not action_context:
        $ Player.sprite = 0
        $ Player.cock_position = "out"
        call Jean_Sex_Reset

    $ JeanX.change_face("_sexy")

    $ JeanX.action_counter["sex"] += 1
    $ JeanX.remaining_actions -=1
    $ JeanX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ JeanX.addiction_rate += 1
    $ JeanX.change_stat("inhibition", 30, 2)
    $ JeanX.change_stat("inhibition", 70, 1)

    call Partner_Like (JeanX, 3, 2)

    if "Jean Sex Addict" in Achievements:
        pass

    elif JeanX.action_counter["sex"] >= 10:
        $ JeanX.SEXP += 5
        $ Achievements.append("Jean Sex Addict")
        if not action_context:
            $ JeanX.change_face("_smile", 1)
            ch_j "Hey, I just noticed we've been doing this a lot. . ."
    elif JeanX.action_counter["sex"] == 1:
        $ JeanX.SEXP += 20
        if not action_context:

            ch_j "Blew your mind, uh?"



    elif JeanX.action_counter["sex"] == 5:
        ch_j "You're pretty good at this. . ."
    elif not action_context:
        if "unsatisfied" in JeanX.recent_history:
            $ JeanX.change_face("_angry")
            ch_j "I think you need to get back down there."

    $ approval_bonus = 0
    call checkout
    return






label Jean_Sex_A:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JeanX)
    if JeanX.action_counter["anal"] >= 7:
        $ approval_bonus += 20
    elif JeanX.action_counter["anal"] >= 3:
        $ approval_bonus += 17
    elif JeanX.action_counter["anal"]:
        $ approval_bonus += 15

    if JeanX.addiction >= 75 and (JeanX.event_counter["creampied"] + JeanX.event_counter["anal_creampied"]) >=3:
        $ approval_bonus += 25
    elif JeanX.addiction >= 75:
        $ approval_bonus += 15

    if JeanX.lust > 85:
        $ approval_bonus += 10
    elif JeanX.lust > 75:
        $ approval_bonus += 5

    $ approval_bonus += 10

    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in JeanX.traits:
        $ approval_bonus += (5*Taboo)

    if JeanX in Player.Harem or "sex friend" in JeanX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JeanX.traits:
        $ approval_bonus -= 40
    if JeanX.event_counter["forced"] and not JeanX.Forced:
        $ approval_bonus -= 5*JeanX.event_counter["forced"]

    if JeanX.Taboo and "no_taboo" in JeanX.daily_history:
        $ approval_bonus -= 10
    if "no_anal" in JeanX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_anal" in JeanX.recent_history else 0

    $ approval = approval_check(JeanX, 1550, TabM = 5)

    if action_context == "auto":
        call Jean_Sex_Launch ("anal")
        if JeanX.PantsNum() == 5:
            "You flip [JeanX.name] around, sliding her skirt up as you go."
            $ JeanX.upskirt = 1
        elif JeanX.PantsNum() >= 6:
            "You flip [JeanX.name] around, sliding her pants down as you do."
            $ JeanX.legs = ""
        else:
            "You flip [JeanX.name] around."
        $ JeanX.SeenPanties = 1
        "You press the tip of your cock against her tight rim."
        $ JeanX.change_face("_surprised", 1)
        call Jean_First_Bottomless (1)

        if (JeanX.action_counter["anal"] and approval) or (approval > 1):

            $ JeanX.change_stat("obedience", 70, 3)
            $ JeanX.change_stat("inhibition", 50, 3)
            $ JeanX.change_stat("inhibition", 70, 1)
            "[JeanX.name] glances back and then breaks into a smile."
            ch_j "Oh! Sure. . ."
            jump Jean_AnalPrep
        else:

            $ JeanX.brows = "_angry"
            menu:
                ch_j "Sticking in the back?"
                "Sorry, sorry! Never mind.":
                    if approval:
                        $ JeanX.change_face("_sexy", 1)
                        $ JeanX.change_stat("obedience", 70, 3)
                        $ JeanX.change_stat("inhibition", 50, 3)
                        $ JeanX.change_stat("inhibition", 70, 1)
                        ch_j "Sure, works for me. . ."
                        ch_j "Get in there."
                        jump Jean_AnalPrep
                    "You pull back before you really get it in."
                    $ JeanX.change_face("_bemused", 1)




                    ch_j "Hey, just ask first. . ."
                "Just fucking.":
                    $ JeanX.change_stat("love", 80, -10, 1)
                    $ JeanX.change_stat("love", 200, -8)
                    "You press into her."
                    $ JeanX.change_stat("obedience", 70, 3)
                    $ JeanX.change_stat("inhibition", 50, 3)
                    if not approval_check(JeanX, 700, "O", TabM=1):
                        $ JeanX.change_face("_angry")
                        "[JeanX.name] shoves you away and backhands you in the face."
                        ch_j "Tsk tsk."
                        $ JeanX.change_stat("love", 50, -10, 1)
                        $ JeanX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        call Jean_Sex_Reset
                        $ JeanX.recent_history.append("_angry")
                        $ JeanX.daily_history.append("_angry")
                    else:
                        $ JeanX.change_face("_sad")
                        "[JeanX.name] doesn't seem to be into this, you're lucky she's willing to give it a try."
                        jump Jean_AnalPrep
        return



    if not JeanX.action_counter["anal"] and "no_anal" not in JeanX.recent_history:

        $ JeanX.change_face("_surprised", 1)
        $ JeanX.mouth = "_kiss"
        ch_j "Oh, you're into anal?"

        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            ch_j "That's the card you're going to play?"

    if "anal" in JeanX.recent_history:
        $ JeanX.change_face("_sexy", 1)
        ch_j "Ok, sure."
        jump Jean_AnalPrep


    if not JeanX.action_counter["anal"] and approval:

        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
        elif JeanX.love >= (JeanX.obedience + JeanX.inhibition - JeanX.IX):
            $ JeanX.change_face("_sexy")
            $ JeanX.brows = "_sad"
            $ JeanX.mouth = "_smile"
            ch_j "I was expecting this. . ."
        elif JeanX.obedience >= (JeanX.inhibition - JeanX.IX):
            $ JeanX.change_face("_normal")
            ch_j "I expected that. . ."
        elif JeanX.addiction >= 50:
            $ JeanX.change_face("_manic", 1)
            ch_j "Hmm, sounds fun. . ."
        else:
            $ JeanX.change_face("_sad")
            $ JeanX.mouth = "_smile"
            ch_j "I was tired of waiting. . ."

    elif approval:

        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
            ch_j "Well you're optimistic. . ."
        elif not JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "I guess here is fine. . ."
        elif "anal" in JeanX.daily_history and not JeanX.used_to_anal:
            pass
        elif "anal" in JeanX.recent_history:
            ch_j "I am warmed up. . ."
            jump Jean_AnalPrep
        elif "anal" in JeanX.daily_history:
            $ JeanX.change_face("_sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",
                    "So you'd like another round?",
                    "Again? Sure.",
                    "Didn't get enough earlier?",
                    "Your funeral, " + JeanX.player_petname + "."])
            ch_j "[Line]"
        else:
            $ JeanX.change_face("_sexy", 1)
            $ JeanX.ArmPose = 2
            $ Line = renpy.random.choice(["Oooh, you want some of this?",
                    "So you'd like another round?",
                    "I knew you enjoyed it. . .",
                    "I hope you don't plan on wearing me out.",
                    "You want to plow me?"])
            ch_j "[Line]"
        $ Line = 0

    if approval >= 2:

        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("obedience", 90, 1)
            $ JeanX.change_stat("inhibition", 60, 1)
            ch_j "Whatever."
        elif "no_anal" in JeanX.daily_history:
            ch_j "Well, if you're going to keep asking. . ."
            ch_j "Might be fun. . ."
        else:
            $ JeanX.change_face("_sexy", 1)
            $ JeanX.change_stat("love", 90, 1)
            $ JeanX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well. . . ok.",
                    "Sure.",
                    "You could, I guess.",
                    "Um, yeah.",
                    "Heh, ok, ok."])
            ch_j "[Line]"
            $ Line = 0
        $ JeanX.change_stat("obedience", 20, 1)
        $ JeanX.change_stat("obedience", 60, 1)
        $ JeanX.change_stat("inhibition", 70, 2)
        jump Jean_AnalPrep
    else:


        $ JeanX.change_face("_angry")
        if "no_anal" in JeanX.recent_history:
            ch_j "I don't repeat myself."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history and "no_anal" in JeanX.daily_history:
            ch_j "I'm not comfortable with that. . ."
        elif "no_anal" in JeanX.daily_history:
            ch_j "Not today."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "I told you, I'm not comfortable with that. . ."
        elif not JeanX.action_counter["anal"]:
            $ JeanX.change_face("_bemused")
            ch_j "I don't know that you're ready for that yet."
        else:
            $ JeanX.change_face("_bemused")
            ch_j "Maybe eventually. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_anal" in JeanX.daily_history:
                $ JeanX.change_face("_bemused")
                ch_j "I get it."
                return
            "Maybe later?" if "no_anal" not in JeanX.daily_history:
                $ JeanX.change_face("_sexy")
                ch_j "Oh, probably. . ."
                $ JeanX.change_stat("love", 80, 2)
                $ JeanX.change_stat("inhibition", 70, 2)
                if JeanX.Taboo:
                    $ JeanX.recent_history.append("no_taboo")
                    $ JeanX.daily_history.append("no_taboo")
                $ JeanX.recent_history.append("no_anal")
                $ JeanX.daily_history.append("no_anal")
                return
            "I bet it would feel really good. . .":
                if approval:
                    $ JeanX.change_face("_sexy")
                    $ JeanX.change_stat("obedience", 90, 2)
                    $ JeanX.change_stat("obedience", 50, 2)
                    $ JeanX.change_stat("inhibition", 70, 3)
                    $ JeanX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Yeah, sure. . .",
                                "I guess. . .",
                                "Good point. . ."])
                    ch_j "[Line]"
                    $ Line = 0
                    jump Jean_AnalPrep
                else:
                    pass
            "Just deal with it.":

                $ approval = approval_check(JeanX, 1250, "OI", TabM = 3)
                if approval > 1 or (approval and JeanX.Forced):
                    $ JeanX.change_face("_confused")
                    $ JeanX.change_stat("love", 70, -5, 1)
                    $ JeanX.change_stat("love", 200, -5)
                    $ JeanX.change_face("_angry",Eyes="_side")
                    ch_j "Oh fine, get it over with."
                    $ JeanX.change_stat("obedience", 80, 4)
                    $ JeanX.change_stat("inhibition", 80, 1)
                    $ JeanX.change_stat("inhibition", 60, 3)
                    $ JeanX.Forced = 1
                    jump Jean_AnalPrep
                else:
                    $ JeanX.change_stat("love", 200, -20)
                    $ JeanX.recent_history.append("_angry")
                    $ JeanX.daily_history.append("_angry")


    $ JeanX.ArmPose = 1
    if "no_anal" in JeanX.daily_history:
        ch_j "Know when to stop."
        $ JeanX.recent_history.append("_angry")
        $ JeanX.daily_history.append("_angry")
    elif JeanX.Forced:
        $ JeanX.change_face("_angry", 1)
        ch_j "You're overestimating your power here."
        $ JeanX.change_stat("lust", 200, 5)
        if JeanX.love > 300:
            $ JeanX.change_stat("love", 70, -2)
        $ JeanX.change_stat("obedience", 50, -2)
        $ JeanX.recent_history.append("_angry")
        $ JeanX.daily_history.append("_angry")
    elif JeanX.Taboo:

        $ JeanX.change_face("_angry", 1)
        $ JeanX.recent_history.append("no_taboo")
        $ JeanX.daily_history.append("no_taboo")
        ch_j "I'm just not comfortable with that right now. . ."
        $ JeanX.change_stat("lust", 200, 5)
        $ JeanX.change_stat("obedience", 50, -3)
    elif "anal" in JeanX.daily_history:
        $ JeanX.change_face("_bemused")
        ch_j "Not right now."
    elif JeanX.action_counter["anal"]:
        $ JeanX.change_face("_sad")
        ch_j "You'll have to earn that one. . ."
    else:
        $ JeanX.change_face("_normal", 1)
        ch_j "You haven't earned it yet."
    $ JeanX.recent_history.append("no_anal")
    $ JeanX.daily_history.append("no_anal")
    $ approval_bonus = 0
    return

label Jean_AnalPrep:
    call Seen_First_Peen (JeanX, Partner, React=action_context)
    call Jean_Sex_Launch ("hotdog")

    if action_context == JeanX:

        $ action_context = 0
        if JeanX.PantsNum() == 5:
            "[JeanX.name] turns around, sliding her skirt up as she does so."
            $ JeanX.upskirt = 1
        elif JeanX.PantsNum() >= 6:
            "[JeanX.name] turns around, sliding her [JeanX.legs] down as she does so."
            $ JeanX.upskirt = 1
        else:
            "[JeanX.name] turns around and pulls you toward her."
        $ JeanX.SeenPanties = 1
        "She slides the tip along her asshole, and seems to want you to insert it."
        menu:
            "What do you do?"
            "Go with it.":
                $ JeanX.change_stat("inhibition", 80, 3)
                $ JeanX.change_stat("inhibition", 50, 2)
                "[JeanX.name] slides it in."
            "Praise her.":
                $ JeanX.change_face("_sexy", 1)
                $ JeanX.change_stat("inhibition", 80, 3)
                ch_p "Oh yeah, [JeanX.petname], let's do this."
                $ JeanX.nameCheck()
                "[JeanX.name] slides it in."
                $ JeanX.change_stat("love", 85, 1)
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ JeanX.change_face("_surprised")
                $ JeanX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [JeanX.petname]."
                $ JeanX.nameCheck()
                "[JeanX.name] pulls back."
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("obedience", 50, 1)
                $ JeanX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ JeanX.add_word(1,"refused","refused")
                return
        $ JeanX.underwear_pulled_down = 1
        call Jean_First_Bottomless (1)
    elif action_context != "auto":
        call AutoStrip (JeanX)

        if JeanX.Taboo:
            "[JeanX.name] glances around to see if anyone notices what she's doing."
            if "cockout" in Player.recent_history:
                "Then she turns around and slowly presses against your rigid member."
            else:
                "Then she pulls down your pants and turns around."
                "She slowly presses against your rigid member."
            $ JeanX.change_stat("inhibition", 90, int(Taboo/10))
            $ JeanX.change_stat("lust", 50, int(Taboo/5))
        else:
            if "cockout" in Player.recent_history:
                "[JeanX.name] turns around and slowly presses against your rigid member."
            else:
                "[JeanX.name] pulls down your pants and turns around."
                "She slowly presses against your rigid member."
        "She leans back a bit and your cock pops in."
    else:

        if (JeanX.PantsNum() >= 6 and not JeanX.upskirt) and (JeanX.underwear and not JeanX.underwear_pulled_down):
            "You quickly pull down her pants and her [JeanX.underwear] and press against her back door."
        elif (JeanX.underwear and not JeanX.underwear_pulled_down):
            "You quickly pull down her [JeanX.underwear] and press against her back door."
        $ JeanX.upskirt = 1
        $ JeanX.underwear_pulled_down = 1
        $ JeanX.SeenPanties = 1
        call Jean_First_Bottomless (1)

    if not JeanX.action_counter["anal"]:
        if JeanX.Forced:
            $ JeanX.change_stat("love", 90, -150)
            $ JeanX.change_stat("obedience", 70, 70)
            $ JeanX.change_stat("inhibition", 80, 40)
        else:
            $ JeanX.change_stat("love", 90, 10)
            $ JeanX.change_stat("obedience", 70, 30)
            $ JeanX.change_stat("inhibition", 80, 70)
    elif not JeanX.used_to_anal:
        if JeanX.Forced:
            $ JeanX.change_stat("love", 90, -20)
            $ JeanX.change_stat("obedience", 70, 10)
            $ JeanX.change_stat("inhibition", 80, 5)
        else:
            $ JeanX.change_stat("obedience", 70, 7)
            $ JeanX.change_stat("inhibition", 80, 5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    $ Player.cock_position = "anal"
    $ primary_action = "anal"
    $ action_speed = 1
    if JeanX.Taboo:
        $ JeanX.drain_word("no_taboo")
    $ JeanX.drain_word("no_anal")
    $ JeanX.recent_history.append("anal")
    $ JeanX.daily_history.append("anal")

label Jean_Anal_Cycle:
    while Round > 0:
        call shift_focus (JeanX)
        call Jean_Sex_Launch ("anal")
        if action_speed >= 4:
            $ Shift = 2

        $ JeanX.lust_face()
        $ Player.sprite = 1
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

                    call Slap_Ass (JeanX)
                    $ counter += 1
                    $ Round -= 1
                    jump Jean_Anal_Cycle
                "Turn her Around":
                    $ JeanX.pose = "doggy" if JeanX.pose != "doggy" else "sex"
                    "You turn her around. . ."
                    jump Jean_Anal_Cycle

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
                            if JeanX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ JeanX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (JeanX, "tired")
                        "Shift primary action":

                            if JeanX.remaining_actions and multi_action:
                                menu:
                                    "How about sex?":
                                        $ action_context = "shift"
                                        call Jean_AnalAfter
                                        call Jean_Sex_P
                                    "Just stick it in her pussy [[without asking].":
                                        $ action_context = "auto"
                                        call Jean_AnalAfter
                                        call Jean_Sex_P
                                    "Pull back to hotdog her.":
                                        $ action_context = "pullback"
                                        call Jean_AnalAfter
                                        call Jean_Sex_H
                                    "Never Mind":
                                        jump Jean_Anal_Cycle
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
                                    jump Jean_Anal_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jean_Anal_Cycle
                                "Never mind":
                                    jump Jean_Anal_Cycle
                        "Just take a look at her.":
                            $ Player.cock_position = 0
                            $ action_speed = 0

                        "Show her feet" if not ShowFeet and JeanX.pose == "doggy":
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and JeanX.pose == "doggy":
                            $ ShowFeet = 0
                        "Undress [JeanX.name]":

                            call Girl_Undress (JeanX)
                        "Clean up [JeanX.name] (locked)" if not JeanX.spunk:
                            pass
                        "Clean up [JeanX.name]" if JeanX.spunk:
                            call Girl_Cleanup (JeanX, "ask")
                        "Never mind":
                            jump Jean_Anal_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jean_Sex_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jean_AnalAfter
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jean_Sex_Reset
                    $ Line = 0
                    jump Jean_AnalAfter


        call shift_focus (JeanX)
        call Sex_Dialog (JeanX, Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or JeanX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (JeanX)
                if "_angry" in JeanX.recent_history:
                    call Jean_Sex_Reset
                    return
                $ JeanX.change_stat("lust", 200, 5)
                if 100 > JeanX.lust >= 70 and JeanX.session_orgasms < 2:
                    $ JeanX.recent_history.append("unsatisfied")
                    $ JeanX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jean_AnalAfter
                $ Line = "came"

            if JeanX.lust >= 100:

                call Girl_Cumming (JeanX)
                if action_context == "shift" or "_angry" in JeanX.recent_history:
                    jump Jean_AnalAfter

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "She's emptied you out, you'll need to take a break."
                    jump Jean_AnalAfter
                elif "unsatisfied" in JeanX.recent_history:

                    $ Line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                    "[Line] Keep going?"
                    menu:
                        extend ""
                        "Yes, keep going for a bit." if Player.semen:
                            $ Line = "You get back into it"
                            jump Jean_Anal_Cycle
                        "No, I'm done." if Player.semen:
                            "You pull back."
                            jump Jean_AnalAfter
                        "No, I'm spent." if not Player.semen:
                            "You pull back."
                            jump Jean_AnalAfter
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if JeanX.SEXP >= 100 or approval_check(JeanX, 1200, "LO"):
            pass
        elif counter == (5 + JeanX.action_counter["anal"]):
            $ JeanX.brows = "_confused"
            ch_j "Ok, that good enough?"
        elif counter == (10 + JeanX.action_counter["anal"]):
            $ JeanX.brows = "_angry"
            menu:
                ch_j "Can we. . . do something. . . else?"
                "How about a BJ?" if JeanX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Jean_AnalAfter
                    call Jean_Blowjob
                "How about a Handy?" if JeanX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Jean_AnalAfter
                    call Jean_Handjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    $ counter += 1
                    jump Jean_Anal_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Jean_Sex_Reset
                    $ action_context = "shift"
                    jump Jean_AnalAfter
                "No, get back down there.":
                    if approval_check(JeanX, 1200) or approval_check(JeanX, 500, "O"):
                        $ JeanX.change_stat("love", 200, -5)
                        $ JeanX.change_stat("obedience", 50, 3)
                        $ JeanX.change_stat("obedience", 80, 2)
                        "She grumbles but keeps moving."
                    else:
                        $ JeanX.change_face("_angry", 1)
                        call Jean_Sex_Reset
                        "She scowls at you and pulls out."
                        ch_j "Don't overestimate yourself."
                        $ JeanX.change_stat("love", 50, -3, 1)
                        $ JeanX.change_stat("love", 80, -4, 1)
                        $ JeanX.change_stat("obedience", 30, -1, 1)
                        $ JeanX.change_stat("obedience", 50, -1, 1)
                        $ JeanX.recent_history.append("_angry")
                        $ JeanX.daily_history.append("_angry")
                        jump Jean_AnalAfter


        if Round == 10:
            call Sex_Basic_Dialog (JeanX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JeanX, 5)


    $ JeanX.change_face("_bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JeanX, "done")

label Jean_AnalAfter:
    if not action_context:
        $ Player.sprite = 0
        $ Player.cock_position = "out"
        call Jean_Sex_Reset

    $ JeanX.change_face("_sexy")

    $ JeanX.action_counter["anal"] += 1
    $ JeanX.remaining_actions -=1
    $ JeanX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ JeanX.addiction_rate += 1
    $ JeanX.change_stat("inhibition", 30, 3)
    $ JeanX.change_stat("inhibition", 70, 1)

    if Partner == "Kitty":
        call Partner_Like (JeanX, 4, 2)
    else:
        call Partner_Like (JeanX, 3, 2)

    if "Jean Anal Addict" in Achievements:
        pass

    elif JeanX.action_counter["anal"] >= 10:
        $ JeanX.SEXP += 7
        $ Achievements.append("Jean Anal Addict")
        if not action_context:
            $ JeanX.change_face("_bemused", 1)
            ch_j "This has been fun exercise."
    elif JeanX.action_counter["anal"] == 1:
        $ JeanX.SEXP += 25
        if not action_context:
            if JeanX.love >= 500 and "unsatisfied" not in JeanX.recent_history:
                ch_j "Hmmm, that was nice. . ."
            elif JeanX.obedience <= 500 and Player.focus <= 20:
                $ JeanX.mouth = "_sad"
                ch_j "that was great. . ."
    elif JeanX.action_counter["anal"] == 5:
        ch_j "I'm glad we have similar interests. . ."
    elif not action_context:
        if "unsatisfied" in JeanX.recent_history:
            $ JeanX.change_face("_angry")
            ch_j "I think you need to get back down there."

    $ approval_bonus = 0


    call checkout
    return








label Jean_Sex_H:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (JeanX)
    if JeanX.action_counter["hotdog"] >= 3:
        $ approval_bonus += 10
    elif JeanX.action_counter["hotdog"]:
        $ approval_bonus += 5

    if JeanX.lust > 85:
        $ approval_bonus += 10
    elif JeanX.lust > 75:
        $ approval_bonus += 5
    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in JeanX.traits:
        $ approval_bonus += (3*Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in JeanX.traits:
        $ approval_bonus -= 40
    if JeanX.event_counter["forced"] and not JeanX.Forced:
        $ approval_bonus -= 5*JeanX.event_counter["forced"]

    if JeanX.Taboo and "no_taboo" in JeanX.daily_history:
        $ approval_bonus -= 10

    if "no_hotdog" in JeanX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_hotdog" in JeanX.recent_history else 0

    $ approval = approval_check(JeanX, 1000, TabM = 3)

    if action_context == "auto":
        call Jean_Sex_Launch ("hotdog")
        "You push [JeanX.name] down, and press your cock against her."
        $ JeanX.change_face("_surprised", 1)

        if (JeanX.action_counter["hotdog"] and approval) or (approval > 1):
            "[JeanX.name] glances back and then breaks into a smile."
            $ JeanX.change_face("_sly")
            $ JeanX.change_stat("obedience", 70, 3)
            $ JeanX.change_stat("inhibition", 50, 3)
            $ JeanX.change_stat("inhibition", 70, 1)
            ch_j "Oh, what did you have in mind with that? . ."
            jump Jean_HotdogPrep
        else:
            $ JeanX.brows = "_angry"
            menu:
                ch_j "Little close there, [JeanX.player_petname]?"
                "Sorry, sorry! Never mind.":
                    if approval:
                        $ JeanX.change_face("_sexy", 1)
                        $ JeanX.change_stat("obedience", 70, 3)
                        $ JeanX.change_stat("inhibition", 50, 3)
                        $ JeanX.change_stat("inhibition", 70, 1)
                        ch_j "I didn't say I minded. . ."
                        jump Jean_HotdogPrep
                    "You pull back from her."
                    $ JeanX.change_face("_bemused", 1)
                    ch_j "Just ask first."
                "You'll see.":
                    $ JeanX.change_stat("love", 80, -10, 1)
                    $ JeanX.change_stat("love", 200, -8)
                    "You grind against her crotch."
                    $ JeanX.change_stat("obedience", 70, 3)
                    $ JeanX.change_stat("inhibition", 50, 3)
                    if not approval_check(JeanX, 500, "O", TabM=1):
                        $ JeanX.change_face("_angry")
                        "[JeanX.name] shoves you away."
                        ch_j "Don't push it, [JeanX.player_petname]."
                        $ JeanX.change_stat("love", 50, -10, 1)
                        $ JeanX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        call Jean_Sex_Reset
                        $ JeanX.recent_history.append("_angry")
                        $ JeanX.daily_history.append("_angry")
                    else:
                        $ JeanX.change_face("_sad")
                        "[JeanX.name] doesn't seem to be into this, but she knows her place."
                        jump Jean_HotdogPrep
        return



    if not JeanX.action_counter["hotdog"] and "no_hotdog" not in JeanX.recent_history:

        $ JeanX.change_face("_surprised", 1)
        $ JeanX.mouth = "_kiss"
        ch_j "What, just grinding?"

        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            ch_j ". . . nothing more?"
            if approval:
                ch_j "Which of us has a pussy here?"


    if not JeanX.action_counter["hotdog"] and approval:

        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
        elif JeanX.love >= (JeanX.obedience + JeanX.inhibition - JeanX.IX):
            $ JeanX.change_face("_sexy")
            $ JeanX.brows = "_sad"
            $ JeanX.mouth = "_smile"
            ch_j "Ok, we can start with that. . ."
        elif JeanX.obedience >= (JeanX.inhibition - JeanX.IX):
            $ JeanX.change_face("_normal")
            ch_j "Ok, we can start with that. . ."
        elif JeanX.addiction >= 50:
            $ JeanX.change_face("_manic", 1)
            ch_j "Hrmm. . ."
        else:
            $ JeanX.change_face("_sad")
            $ JeanX.mouth = "_smile"
            ch_j "Ok, we can start with that. . ."

    elif approval:

        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("love", 70, -3, 1)
            $ JeanX.change_stat("love", 20, -2, 1)
            ch_j "Odd. . ."
        elif not JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "I guess this is a better location . ."
        elif "hotdog" in JeanX.recent_history:
            $ JeanX.change_face("_sexy", 1)
            ch_j "Again? Fine, whatever."
            jump Jean_HotdogPrep
        elif "hotdog" in JeanX.daily_history:
            $ JeanX.change_face("_sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",
                    "So you'd like another round?",
                    "You're really into this. . .",
                    "Are you sure that's all you want?"])
            ch_j "[Line]"
        else:
            $ JeanX.change_face("_sexy", 1)
            $ JeanX.ArmPose = 2
            $ Line = renpy.random.choice(["Oooh, you want some of this?",
                    "So you'd like another round?",
                    "You're really into this. . .",
                    "You want another rub?"])
            ch_j "[Line]"
        $ Line = 0

    if approval >= 2:

        if JeanX.Forced:
            $ JeanX.change_face("_sad")
            $ JeanX.change_stat("obedience", 80, 1)
            $ JeanX.change_stat("inhibition", 60, 1)
            ch_j "Ok, fine."
        elif "no_hotdog" in JeanX.daily_history:
            ch_j "It was fun enough. . ."
        else:
            $ JeanX.change_face("_sexy", 1)
            $ JeanX.change_stat("love", 80, 1)
            $ JeanX.change_stat("inhibition", 50, 2)
            $ Line = renpy.random.choice(["Well, sure, let me give it a rub.",
                    "Very well.",
                    "Nice!",
                    "I guess we could do that.",
                    "Ok, let me. . .",
                    "Heh, ok, ok."])
            ch_j "[Line]"
            $ Line = 0
        $ JeanX.change_stat("obedience", 60, 1)
        $ JeanX.change_stat("inhibition", 70, 2)
        jump Jean_HotdogPrep
    else:


        $ JeanX.change_face("_angry")
        if "no_hotdog" in JeanX.recent_history:
            ch_j "I don't repeat myself."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history and "no_hotdog" in JeanX.daily_history:
            ch_j "I just told you. . .not in such an exposed location."
        elif "no_hotdog" in JeanX.daily_history:
            ch_j "I'm believe I just told you \"no,\" [JeanX.player_petname]."
        elif JeanX.Taboo and "no_taboo" in JeanX.daily_history:
            ch_j "I'm not comfortable with that. . ."
        elif not JeanX.action_counter["hotdog"]:
            $ JeanX.change_face("_bemused")
            ch_j "Hmm, that could be amusing, [JeanX.player_petname]. . ."
        else:
            $ JeanX.change_face("_bemused")
            ch_j "I don't think that would be appropriate. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_hotdog" in JeanX.daily_history:
                $ JeanX.change_face("_bemused")
                ch_j "So long as you don't push it."
                return
            "Maybe later?" if "no_hotdog" not in JeanX.daily_history:
                $ JeanX.change_face("_sexy")
                ch_j "I guess eventually. . ."
                $ JeanX.change_stat("love", 80, 1)
                $ JeanX.change_stat("inhibition", 50, 1)
                if JeanX.Taboo:
                    $ JeanX.recent_history.append("no_taboo")
                    $ JeanX.daily_history.append("no_taboo")
                $ JeanX.recent_history.append("no_hotdog")
                $ JeanX.daily_history.append("no_hotdog")
                return
            "You might like it. . .":
                if approval:
                    $ JeanX.change_face("_sexy")
                    $ JeanX.change_stat("obedience", 60, 2)
                    $ JeanX.change_stat("inhibition", 50, 2)
                    $ Line = renpy.random.choice(["Yeah, probably. . .",
                                "I guess. . .",
                                "Good point. . ."])
                    ch_j "[Line]"
                    $ Line = 0
                    jump Jean_HotdogPrep
                else:
                    pass
            "Just deal with it.":

                $ approval = approval_check(JeanX, 350, "OI", TabM = 3)
                if approval > 1 or (approval and JeanX.Forced):
                    $ JeanX.change_face("_confused")
                    $ JeanX.change_stat("love", 70, -2, 1)
                    $ JeanX.change_stat("love", 200, -2)
                    ch_j ". . ."
                    ch_j ". . . fine."
                    $ JeanX.change_stat("obedience", 80, 4)
                    $ JeanX.change_stat("inhibition", 60, 2)
                    $ JeanX.Forced = 1
                    jump Jean_HotdogPrep
                else:
                    $ JeanX.change_stat("love", 200, -10)
                    $ JeanX.recent_history.append("_angry")
                    $ JeanX.daily_history.append("_angry")


    $ JeanX.ArmPose = 1

    if "no_hotdog" in JeanX.daily_history:
        ch_j "What did I tell you?"
        $ JeanX.recent_history.append("_angry")
        $ JeanX.daily_history.append("_angry")
    if JeanX.Forced:
        $ JeanX.change_face("_angry", 1)
        ch_j "There's no point trying."
        $ JeanX.change_stat("lust", 200, 5)
        if JeanX.love > 300:
            $ JeanX.change_stat("love", 70, -1)
        $ JeanX.change_stat("obedience", 50, -1)
        $ JeanX.recent_history.append("_angry")
        $ JeanX.daily_history.append("_angry")
    elif JeanX.Taboo:
        $ JeanX.change_face("_angry", 1)
        $ JeanX.recent_history.append("no_taboo")
        $ JeanX.daily_history.append("no_taboo")
        ch_j "This area is a bit too exposed for that sort of thing. . ."
        $ JeanX.change_stat("lust", 200, 5)
        $ JeanX.change_stat("obedience", 50, -3)
    elif JeanX.action_counter["hotdog"]:
        $ JeanX.change_face("_sad")
        ch_j "Not anymore."
    else:
        $ JeanX.change_face("_normal", 1)
        ch_j "No thanks."
    $ JeanX.recent_history.append("no_hotdog")
    $ JeanX.daily_history.append("no_hotdog")
    $ approval_bonus = 0
    return

label Jean_HotdogPrep:
    call Seen_First_Peen (JeanX, Partner, React=action_context)
    call Jean_Sex_Launch ("hotdog")

    if action_context == JeanX:

        $ action_context = 0
        "[JeanX.name] turns around and pulls you toward her, grinding against your cock."
        menu:
            "What do you do?"
            "Go with it.":
                $ JeanX.change_stat("inhibition", 80, 3)
                $ JeanX.change_stat("inhibition", 50, 2)
                "[JeanX.name] continues to grind."
            "Praise her.":
                $ JeanX.change_face("_sexy", 1)
                $ JeanX.change_stat("inhibition", 80, 3)
                ch_p "Oh yeah, [JeanX.petname], let's do this."
                $ JeanX.nameCheck()
                "[JeanX.name] continues to grind."
                $ JeanX.change_stat("love", 85, 1)
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ JeanX.change_face("_surprised")
                $ JeanX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [JeanX.petname]."
                $ JeanX.nameCheck()
                "[JeanX.name] pulls back."
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("obedience", 50, 1)
                $ JeanX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ JeanX.add_word(1,"refused","refused")
                return
    elif action_context != "auto":


        if JeanX.Taboo:
            "[JeanX.name] glances around to see if anyone notices what she's doing."
            if "cockout" in Player.recent_history:
                "Then she turns around and slowly presses against your rigid member."
            else:
                "Then she pulls down your pants and turns around."
                "She slowly presses against your rigid member."
            $ JeanX.change_stat("inhibition", 90, int(Taboo/10))
            $ JeanX.change_stat("lust", 50, int(Taboo/5))
        else:
            if "cockout" in Player.recent_history:
                "[JeanX.name] turns around and slowly presses against your rigid member."
            else:
                "[JeanX.name] pulls down your pants and turns around."
                "She slowly presses against your rigid member."
    else:

        "She turns around, pulling you against her with your rigid member."

    if not JeanX.action_counter["hotdog"]:
        if JeanX.Forced:
            $ JeanX.change_stat("love", 90, -5)
            $ JeanX.change_stat("obedience", 70, 20)
            $ JeanX.change_stat("inhibition", 80, 10)
        else:
            $ JeanX.change_stat("love", 90, 20)
            $ JeanX.change_stat("obedience", 70, 20)
            $ JeanX.change_stat("inhibition", 80, 20)


    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    $ primary_action = "hotdog"
    $ action_speed = 1
    if JeanX.Taboo:
        $ JeanX.drain_word("no_taboo")
    $ JeanX.drain_word("no_hotdog")
    $ JeanX.recent_history.append("hotdog")
    $ JeanX.daily_history.append("hotdog")

label Jean_Hotdog_Cycle:
    while Round > 0:
        call shift_focus (JeanX)
        call Jean_Sex_Launch ("hotdog")
        if action_speed >= 4:
            $ action_speed = 2

        $ JeanX.lust_face()
        $ Player.cock_position = "out"
        $ Player.sprite = 1
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

                    call Slap_Ass (JeanX)
                    $ counter += 1
                    $ Round -= 1
                    jump Jean_Hotdog_Cycle
                "Turn her Around":
                    $ JeanX.pose = "doggy" if JeanX.pose != "doggy" else "sex"
                    "You turn her around. . ."
                    jump Jean_Hotdog_Cycle

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
                            if JeanX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ JeanX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (JeanX, "tired")
                        "Shift primary action":

                            if JeanX.remaining_actions and multi_action:
                                menu:
                                    "How about sex?":
                                        $ action_context = "shift"
                                        call Jean_HotdogAfter
                                        call Jean_Sex_P
                                    "Just stick it in her pussy [[without asking].":
                                        $ action_context = "auto"
                                        call Jean_HotdogAfter
                                        call Jean_Sex_P
                                    "How about anal?":
                                        $ action_context = "shift"
                                        call Jean_HotdogAfter
                                        call Jean_Sex_A
                                    "Just stick it in her ass [[without asking].":
                                        $ action_context = "auto"
                                        call Jean_HotdogAfter
                                        call Jean_Sex_A
                                    "Never Mind":
                                        jump Jean_Hotdog_Cycle
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
                                    jump Jean_Hotdog_Cycle
                                "Clean up Partner":
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Jean_Hotdog_Cycle
                                "Never mind":
                                    jump Jean_Hotdog_Cycle
                        "Just take a look at her.":
                            $ Player.cock_position = 0
                            $ action_speed = 0

                        "Show her feet" if not ShowFeet and JeanX.pose == "doggy":
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and JeanX.pose == "doggy":
                            $ ShowFeet = 0
                        "Undress [JeanX.name]":

                            call Girl_Undress (JeanX)
                        "Clean up [JeanX.name] (locked)" if not JeanX.spunk:
                            pass
                        "Clean up [JeanX.name]" if JeanX.spunk:
                            call Girl_Cleanup (JeanX, "ask")
                        "Never mind":
                            jump Jean_Hotdog_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Jean_Sex_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Jean_HotdogAfter
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Jean_Sex_Reset
                    $ Line = 0
                    jump Jean_HotdogAfter


        call shift_focus (JeanX)
        call Sex_Dialog (JeanX, Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or JeanX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (JeanX)
                if "_angry" in JeanX.recent_history:
                    call Jean_Sex_Reset
                    return
                $ JeanX.change_stat("lust", 200, 5)
                if 100 > JeanX.lust >= 70 and JeanX.session_orgasms < 2:
                    $ JeanX.recent_history.append("unsatisfied")
                    $ JeanX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Jean_HotdogAfter
                $ Line = "came"

            if JeanX.lust >= 100:

                call Girl_Cumming (JeanX)
                if action_context == "shift" or "_angry" in JeanX.recent_history:
                    jump Jean_HotdogAfter

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "She's emptied you out, you'll need to take a break."
                    jump Jean_HotdogAfter
                elif "unsatisfied" in JeanX.recent_history:

                    $ Line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                    "[Line] Keep going?"
                    menu:
                        extend ""
                        "Yes, keep going for a bit." if Player.semen:
                            $ Line = "You get back into it"
                            jump Jean_Hotdog_Cycle
                        "No, I'm done." if Player.semen:
                            "You pull back."
                            jump Jean_HotdogAfter
                        "No, I'm spent." if not Player.semen:
                            "You pull back."
                            jump Jean_HotdogAfter
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if JeanX.SEXP >= 100 or approval_check(JeanX, 1200, "LO"):
            pass
        elif counter == (5 + JeanX.action_counter["hotdog"]):
            $ JeanX.brows = "_confused"
            ch_j "'bout done there?"
        elif counter == (10 + JeanX.action_counter["hotdog"]):
            $ JeanX.brows = "_angry"
            menu:
                ch_j "Well this is not fun."
                "How about a BJ?" if JeanX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Jean_HotdogAfter
                    call Jean_Blowjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    $ counter += 1
                    jump Jean_Hotdog_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Jean_Sex_Reset
                    $ action_context = "shift"
                    jump Jean_HotdogAfter
                "No, get back down there.":
                    if approval_check(JeanX, 1200) or approval_check(JeanX, 500, "O"):
                        $ JeanX.change_stat("love", 200, -5)
                        $ JeanX.change_stat("obedience", 50, 3)
                        $ JeanX.change_stat("obedience", 80, 2)
                        "She grumbles but keeps moving."
                    else:
                        $ JeanX.change_face("_angry", 1)
                        call Jean_Sex_Reset
                        "She scowls at you and pulls away."
                        ch_j "Don't overestimate yourself."
                        $ JeanX.change_stat("love", 50, -3, 1)
                        $ JeanX.change_stat("love", 80, -4, 1)
                        $ JeanX.change_stat("obedience", 30, -1, 1)
                        $ JeanX.change_stat("obedience", 50, -1, 1)
                        $ JeanX.recent_history.append("_angry")
                        $ JeanX.daily_history.append("_angry")
                        jump Jean_HotdogAfter


        call Escalation (JeanX)

        if Round == 10:
            call Sex_Basic_Dialog (JeanX, 10)
        elif Round == 5:
            call Sex_Basic_Dialog (JeanX, 5)


    $ JeanX.change_face("_bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog (JeanX, "done")


label Jean_HotdogAfter:
    if not action_context:
        $ Player.sprite = 0
        $ Player.cock_position = "out"
        call Jean_Sex_Reset

    $ JeanX.change_face("_sexy")

    $ JeanX.action_counter["hotdog"] += 1
    $ JeanX.remaining_actions -=1
    $ JeanX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ JeanX.addiction_rate += 1
    $ JeanX.change_stat("inhibition", 30, 1)
    $ JeanX.change_stat("inhibition", 70, 1)

    call Partner_Like (JeanX, 2)

    if JeanX.action_counter["hotdog"] == 10:
        $ JeanX.SEXP += 5
    elif JeanX.action_counter["hotdog"] == 1:
        $ JeanX.SEXP += 10
        if not action_context:
            if JeanX.love >= 500 and "unsatisfied" not in JeanX.recent_history:
                ch_j "Ok, that was. . . fine."
            elif JeanX.obedience <= 500 and Player.focus <= 20:
                $ JeanX.mouth = "_sad"
                ch_j "I guess that could have gone worse. . ."
    elif not action_context:
        if "unsatisfied" in JeanX.recent_history:
            $ JeanX.change_face("_angry")
            ch_j "I think you need to get back down there."

    $ approval_bonus = 0


    call checkout
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
