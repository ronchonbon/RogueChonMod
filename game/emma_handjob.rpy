
label Emma_Handjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (EmmaX)
    if EmmaX.action_counter["handjob"] >= 7:
        $ approval_bonus += 10
    elif EmmaX.action_counter["handjob"] >= 3:
        $ approval_bonus += 7
    elif EmmaX.action_counter["handjob"]:
        $ approval_bonus += 3

    if EmmaX.addiction >= 75 and EmmaX.event_counter["swallowed"] >=3:
        $ approval_bonus += 15
    if EmmaX.addiction >= 75:
        $ approval_bonus += 5

    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in EmmaX.traits:
        $ approval_bonus += (3*Taboo)
    if EmmaX in Player.Harem or "sex friend" in EmmaX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in EmmaX.traits:
        $ approval_bonus -= 40
    if EmmaX.event_counter["forced"] and not EmmaX.Forced:
        $ approval_bonus -= 5*EmmaX.event_counter["forced"]

    if Taboo and "no_taboo" in EmmaX.daily_history:
        $ approval_bonus -= 10

    if "no_handjob" in EmmaX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_handjob" in EmmaX.recent_history else 0

    $ approval = approval_check(EmmaX, 1100, TabM = 3)

    if not EmmaX.action_counter["handjob"] and "no_handjob" not in EmmaX.recent_history:
        $ EmmaX.change_face("_sly", 2)
        ch_e "You'd like me to take care of that for you?"

    if not EmmaX.action_counter["handjob"] and approval:
        if EmmaX.Forced:
            $ EmmaX.change_face("_sad",1)
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
        elif EmmaX.love >= (EmmaX.obedience + EmmaX.inhibition):
            $ EmmaX.change_face("_sexy",1)
            $ EmmaX.brows = "_sad"
            $ EmmaX.mouth = "_smile"
            ch_e "I suppose you've earned something. . ."
        elif EmmaX.obedience >= EmmaX.inhibition:
            $ EmmaX.change_face("_normal",1)
            ch_e "If that's what you'd like, [EmmaX.player_petname]. . ."
        elif EmmaX.addiction >= 50:
            $ EmmaX.change_face("_manic", 1)
            ch_e "Mmmmmmmm. . ."
        else:
            $ EmmaX.change_face("_lipbite",1,Eyes="_side")
            ch_e "I suppose. . ."

    elif approval:
        if EmmaX.Forced:
            $ EmmaX.change_face("_sad")
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
            ch_e "No more than that?"
        elif not Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "Here, hmm?. . ."
        elif "handjob" in EmmaX.recent_history:
            $ EmmaX.change_face("_sexy", 1)
            ch_e "I will need to grade papers later, you know. . ."
            jump Emma_HJ_Prep
        elif "handjob" in EmmaX.daily_history:
            $ EmmaX.change_face("_sexy", 1)
            $ Line = renpy.random.choice(["Another?",   
                "You're going to wear out my arm.", 
                "Didn't get enough earlier?",
                "My hand's a bit sore from earlier.",
                "My hand's rather sore from before."])
            ch_e "[Line]"
        elif EmmaX.action_counter["handjob"] < 3:
            $ EmmaX.change_face("_sly", 1)
            ch_e "Enjoyed last time?. . ."
        else:
            $ EmmaX.change_face("_sexy", 1)
            $ EmmaX.ArmPose = 2
            $ Line = renpy.random.choice(["You want more?",                 
                "So you'd like another?",                 
                "More of this? [fist pumping hand gestures]", 
                "Oh, did you want some attention?"])
            ch_e "[Line]"
        $ Line = 0

    if approval >= 2:
        if EmmaX.Forced:
            $ EmmaX.change_face("_sad")
            $ EmmaX.change_stat("obedience", 90, 1)
            $ EmmaX.change_stat("inhibition", 60, 1)
            ch_e "Very well."
        elif "no_handjob" in EmmaX.daily_history:
            ch_e "Oh, fine!"
        else:
            $ EmmaX.change_face("_sexy", 1)
            $ EmmaX.change_stat("love", 90, 1)
            $ EmmaX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Oh, I suppose.",                 
                "I'll do it.",                 
                "Well, give it here.", 
                "I suppose I could. . .",
                "Fine. . . [She gestures for you to come over].",
                "Ok, ok."])
            ch_e "[Line]"
            $ Line = 0
        $ EmmaX.change_stat("obedience", 20, 1)
        $ EmmaX.change_stat("obedience", 60, 1)
        $ EmmaX.change_stat("inhibition", 70, 2)
        jump Emma_HJ_Prep
    else:

        $ EmmaX.change_face("_angry")
        if "no_handjob" in EmmaX.recent_history:
            ch_e "You need to learn to take\"no\" for an answer, [EmmaX.player_petname]."
        elif "no_handjob" in EmmaX.daily_history:
            ch_e "I told you \"no,\" [EmmaX.player_petname]."
        elif Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "I told you, this is too public!"
        elif not EmmaX.action_counter["handjob"]:
            $ EmmaX.change_face("_bemused")
            ch_e "Are you sure though, [EmmaX.player_petname]?. . ."
        else:
            $ EmmaX.change_face("_bemused")
            ch_e "I'd rather not right now though."
        menu:
            extend ""
            "Sorry, never mind." if "no_handjob" in EmmaX.daily_history:
                $ EmmaX.change_face("_bemused")
                ch_e "Quite alright."
                return
            "Maybe later?" if "no_handjob" not in EmmaX.daily_history:
                $ EmmaX.change_face("_sexy")
                ch_e ". . ."
                ch_e "I couldn't rule it out. . ."
                $ EmmaX.change_stat("love", 80, 2)
                $ EmmaX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ EmmaX.recent_history.append("no_taboo")
                    $ EmmaX.daily_history.append("no_taboo")
                $ EmmaX.recent_history.append("no_handjob")
                $ EmmaX.daily_history.append("no_handjob")
                return
            "I'd really appreciate it. . .":
                if approval:
                    $ EmmaX.change_face("_sexy")
                    $ EmmaX.change_stat("obedience", 90, 2)
                    $ EmmaX.change_stat("obedience", 50, 2)
                    $ EmmaX.change_stat("inhibition", 70, 3)
                    $ EmmaX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Oh, I suppose.",                 
                        "I'll do it.",                 
                        "Well, give it here.", 
                        "I suppose I could. . .",
                        "Fine. . . [She gestures for you to come over].",
                        "Ok, ok."])
                    ch_e "[Line]"
                    $ Line = 0
                    jump Emma_HJ_Prep
            "Come on, get to work.":

                $ approval = approval_check(EmmaX, 350, "OI", TabM = 3)
                if approval > 1 or (approval and EmmaX.Forced):
                    $ EmmaX.change_face("_angry")
                    $ EmmaX.change_stat("love", 70, -5, 1)
                    $ EmmaX.change_stat("love", 200, -2)
                    ch_e "Hm. Alright, but don't push your luck, [EmmaX.player_petname]."
                    $ EmmaX.change_stat("obedience", 50, 4)
                    $ EmmaX.change_stat("inhibition", 80, 1)
                    $ EmmaX.change_stat("inhibition", 60, 3)
                    $ EmmaX.Forced = 1
                    jump Emma_HJ_Prep
                else:
                    $ EmmaX.change_stat("love", 200, -15)
                    $ EmmaX.recent_history.append("_angry")
                    $ EmmaX.daily_history.append("_angry")


    $ EmmaX.ArmPose = 1
    if "no_handjob" in EmmaX.daily_history:
        $ EmmaX.change_face("_angry", 1)
        ch_e "Don't make me repeat myself."
        $ EmmaX.recent_history.append("_angry")
        $ EmmaX.daily_history.append("_angry")
    elif EmmaX.Forced:
        $ EmmaX.change_face("_angry", 1)
        ch_e "Even that is asking too much."
        $ EmmaX.change_stat("lust", 200, 5)
        if EmmaX.love > 300:
            $ EmmaX.change_stat("love", 70, -2)
        $ EmmaX.change_stat("obedience", 50, -2)
        $ EmmaX.recent_history.append("_angry")
        $ EmmaX.daily_history.append("_angry")
    elif Taboo:
        $ EmmaX.change_face("_angry", 1)
        $ EmmaX.daily_history.append("no_taboo")
        ch_e "I couldn't possibly do that. . . here!"
        $ EmmaX.change_stat("lust", 200, 5)
        $ EmmaX.change_stat("obedience", 50, -3)
    elif EmmaX.action_counter["handjob"]:
        $ EmmaX.change_face("_sad")
        ch_e "I'd really rather not. . ."
    else:
        $ EmmaX.change_face("_normal", 1)
        ch_e "No, I don't think so, [EmmaX.player_petname]."
    $ EmmaX.recent_history.append("no_handjob")
    $ EmmaX.daily_history.append("no_handjob")
    $ approval_bonus = 0
    return


label Emma_HJ_Prep:
    if offhand_action == "handjob":
        return

    if Taboo:
        $ EmmaX.inhibition += int(Taboo/10)
        $ EmmaX.lust += int(Taboo/5)

    $ EmmaX.change_face("_sexy")
    if EmmaX.Forced:
        $ EmmaX.change_face("_sad")
    elif not EmmaX.action_counter["handjob"]:
        $ EmmaX.brows = "_confused"
        $ EmmaX.eyes = "_sexy"
        $ EmmaX.mouth = "_smile"

    call Seen_First_Peen (EmmaX, Partner, React=action_context)
    call Emma_HJ_Launch ("L")

    if action_context == EmmaX:

        $ action_context = 0
        if offhand_action == "jackin":
            "[EmmaX.name] brushes your hand aside and starts stroking your cock."
        else:
            "[EmmaX.name] draws her fingers across your cock, and begins to stroke it."
        menu:
            "What do you do?"
            "Nothing.":
                $ EmmaX.change_stat("inhibition", 70, 3)
                $ EmmaX.change_stat("inhibition", 30, 2)
                "[EmmaX.name] continues her actions."
            "Praise her.":
                $ EmmaX.change_face("_sexy", 1)
                $ EmmaX.change_stat("inhibition", 70, 3)
                ch_p "Oooh, that's good, [EmmaX.petname]."
                $ EmmaX.nameCheck()
                "[EmmaX.name] continues her actions."
                $ EmmaX.change_stat("love", 80, 1)
                $ EmmaX.change_stat("obedience", 90, 1)
                $ EmmaX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ EmmaX.change_face("_surprised")
                $ EmmaX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that for now, [EmmaX.petname]."
                $ EmmaX.nameCheck()
                "[EmmaX.name] puts it down."
                $ EmmaX.change_stat("obedience", 90, 1)
                $ EmmaX.change_stat("obedience", 50, 1)
                $ EmmaX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ EmmaX.add_word(1,"refused","refused")
                return

    if not EmmaX.action_counter["handjob"]:
        if EmmaX.Forced:
            $ EmmaX.change_stat("love", 90, -20)
            $ EmmaX.change_stat("obedience", 70, 25)
            $ EmmaX.change_stat("inhibition", 80, 30)
        else:
            $ EmmaX.change_stat("love", 90, 5)
            $ EmmaX.change_stat("obedience", 70, 20)
            $ EmmaX.change_stat("inhibition", 80, 20)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ EmmaX.drain_word("no_taboo")
    $ EmmaX.drain_word("no_handjob")
    $ EmmaX.recent_history.append("handjob")
    $ EmmaX.daily_history.append("handjob")

label Emma_HJ_Cycle:
    while Round > 0:
        call shift_focus (EmmaX)
        call Emma_HJ_Launch
        $ EmmaX.lust_face()

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
                        "I also want to fondle her breasts." if offhand_action != "fondle_breasts":
                            if EmmaX.remaining_actions and multi_action:
                                $ offhand_action = "fondle_breasts"
                                "You start to fondle her breasts."
                                $ EmmaX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (EmmaX, "tired")
                        "Shift primary action":

                            if EmmaX.remaining_actions and multi_action:
                                menu:
                                    "How about a blowjob?":
                                        if EmmaX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Emma_HJ_After
                                            call Emma_Blowjob
                                        else:
                                            call Sex_Basic_Dialog (EmmaX, "tired")
                                    "How about a titjob?":

                                        if EmmaX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Emma_HJ_After
                                            call Emma_Titjob
                                        else:
                                            call Sex_Basic_Dialog (EmmaX, "tired")
                                    "Never Mind":
                                        jump Emma_HJ_Cycle
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
                                    jump Emma_HJ_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Emma_HJ_Cycle
                                "Never mind":
                                    jump Emma_HJ_Cycle
                        "Undress [EmmaX.name]":
                            call Girl_Undress (EmmaX)
                        "Clean up [EmmaX.name] (locked)" if not EmmaX.spunk:
                            pass
                        "Clean up [EmmaX.name]" if EmmaX.spunk:
                            call Girl_Cleanup (EmmaX, "ask")
                        "Never mind":
                            jump Emma_HJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Emma_HJ_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Emma_HJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Emma_HJ_Reset
                    $ Line = 0
                    jump Emma_HJ_After


        call shift_focus (EmmaX)
        call Sex_Dialog (EmmaX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or EmmaX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (EmmaX)
                if "_angry" in EmmaX.recent_history:
                    call Emma_HJ_Reset
                    return
                $ EmmaX.change_stat("lust", 200, 5)
                if 100 > EmmaX.lust >= 70 and EmmaX.session_orgasms < 2 and EmmaX.SEXP >= 20:
                    $ EmmaX.recent_history.append("unsatisfied")
                    $ EmmaX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Emma_HJ_After
                $ Line = "came"

            if EmmaX.lust >= 100:

                call Girl_Cumming (EmmaX)
                if action_context == "shift" or "_angry" in EmmaX.recent_history:
                    jump Emma_HJ_After

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
                            jump Emma_HJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if counter == 20:
            $ EmmaX.brows = "_angry"
            ch_e "Hmm, I'm getting a bit of a cramp here."
            menu:
                ch_e "Mind if we take a break?"
                "How about a BJ?" if EmmaX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Emma_HJ_After
                    call Emma_Blowjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    $ counter += 1
                    "[Line]"
                    jump Emma_HJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Emma_HJ_Reset
                    $ action_context = "shift"
                    jump Emma_HJ_After
                "No, get back down there.":
                    if approval_check(EmmaX, 1200) or approval_check(EmmaX, 500, "O"):
                        $ EmmaX.change_stat("love", 200, -5)
                        $ EmmaX.change_stat("obedience", 50, 3)
                        $ EmmaX.change_stat("obedience", 80, 2)
                        "She scowls but gets back to work."
                    else:
                        $ EmmaX.change_face("_angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        ch_e "You know, I do have better things to do with my time than this."
                        $ EmmaX.change_stat("love", 50, -3, 1)
                        $ EmmaX.change_stat("love", 80, -4, 1)
                        $ EmmaX.change_stat("obedience", 30, -1, 1)
                        $ EmmaX.change_stat("obedience", 50, -1, 1)
                        $ EmmaX.recent_history.append("_angry")
                        $ EmmaX.daily_history.append("_angry")
                        jump Emma_HJ_After
        elif counter == 10 and EmmaX.SEXP <= 100 and not approval_check(EmmaX, 1200, "LO"):
            $ EmmaX.brows = "_confused"
            ch_e "Are you certain you didn't have anything else in mind?"


        call Escalation (EmmaX)

        if Round == 10:
            ch_e "It's about time for a break."
        elif Round == 5:
            ch_e "Ok, that's enough, for now. . ."


    $ EmmaX.change_face("_bemused", 0)
    $ Line = 0
    ch_e "Ok, seriously, I'm putting it down for a minute."

label Emma_HJ_After:
    $ EmmaX.change_face("_sexy")

    $ EmmaX.action_counter["handjob"] += 1
    $ EmmaX.remaining_actions -=1
    $ EmmaX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ EmmaX.addiction_rate += 1
    $ EmmaX.change_stat("lust", 90, 5)

    call Partner_Like (EmmaX, 1)

    if "Emma Handi-Queen" in Achievements:
        pass
    elif EmmaX.action_counter["handjob"] >= 10:
        $ EmmaX.change_face("_smile", 1)
        ch_e "I've apparently become the \"queen\" of handjobs as well."
        $ Achievements.append("Emma Handi-Queen")
        $ EmmaX.SEXP += 5
    elif EmmaX.action_counter["handjob"] == 1:
        $ EmmaX.SEXP += 10
        if not EmmaX.Forced:
            $ EmmaX.mouth = "_smile"
            ch_e "What a lovely experience. . ."
        elif Player.focus <= 20:
            $ EmmaX.mouth = "_sad"
            ch_e "Was that sufficient?"
    elif EmmaX.action_counter["handjob"] == 5:
        ch_e "Please do call again. . ."

    $ approval_bonus = 0
    if action_context == "shift":
        ch_e "Very well, what did you want to do?"
    else:
        call Emma_HJ_Reset
    call checkout
    return







label Emma_Titjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (EmmaX)
    if EmmaX.action_counter["titjob"] >= 7:
        $ approval_bonus += 10
    elif EmmaX.action_counter["titjob"] >= 3:
        $ approval_bonus += 7
    elif EmmaX.action_counter["titjob"]:
        $ approval_bonus += 5

    if EmmaX.addiction >= 75 and EmmaX.event_counter["swallowed"] >=3:
        $ approval_bonus += 15
    elif EmmaX.addiction >= 75:
        $ approval_bonus += 5

    if EmmaX.SeenChest and approval_check(EmmaX, 500):
        $ approval_bonus += 10
    if not EmmaX.bra and not EmmaX.top:
        $ approval_bonus += 10
    if EmmaX.lust > 75:
        $ approval_bonus += 10
    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in EmmaX.traits:
        $ approval_bonus += (5*Taboo)
    if EmmaX in Player.Harem or "sex friend" in EmmaX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in EmmaX.traits:
        $ approval_bonus -= 30
    if EmmaX.event_counter["forced"] and not EmmaX.Forced:
        $ approval_bonus -= 5*EmmaX.event_counter["forced"]

    if Taboo and "no_taboo" in EmmaX.daily_history:
        $ approval_bonus -= 10

    if "no_titjob" in EmmaX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_titjob" in EmmaX.recent_history else 0

    $ approval = approval_check(EmmaX, 1200, TabM = 5)

    if not EmmaX.action_counter["titjob"] and "no_titjob" not in EmmaX.recent_history:
        $ EmmaX.change_face("_surprised", 1)
        $ EmmaX.mouth = "_kiss"
        ch_e "Hmm, are you sure you can handle that, [EmmaX.player_petname]?"

    if not EmmaX.action_counter["titjob"] and approval:

        if EmmaX.Forced:
            $ EmmaX.change_face("_sad")
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
        elif EmmaX.love >= (EmmaX.obedience + EmmaX.inhibition):
            $ EmmaX.change_face("_sexy")
            $ EmmaX.brows = "_sad"
            $ EmmaX.mouth = "_smile"
            ch_e "I suppose you've earned something special. . ."
        elif EmmaX.obedience >= EmmaX.inhibition:
            $ EmmaX.change_face("_normal")
            ch_e "If that's what you want. . ."
        elif EmmaX.addiction >= 50:
            $ EmmaX.change_face("_manic", 1)
            ch_e "Hmmmm. . . ."
        else:
            $ EmmaX.change_face("_sad")
            $ EmmaX.mouth = "_smile"
            ch_e "Hmm, I was wondering when you'd ask. . ."

    elif approval:

        if EmmaX.Forced:
            $ EmmaX.change_face("_sad")
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
            ch_e "You aren't getting used to this service, are you?"
        elif not Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "I suppose this is secluded enough. . ."
        elif "titjob" in EmmaX.recent_history:
            $ EmmaX.change_face("_sexy", 1)
            ch_e "Oh! Back for more?"
            jump Emma_TJ_Prep
        elif "titjob" in EmmaX.daily_history:
            $ EmmaX.change_face("_sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",   
                "You're going to wear them out.", 
                "Didn't get enough earlier?",
                "I'm still a bit sore from earlier."])
            ch_e "[Line]"
        elif EmmaX.action_counter["titjob"] < 3:
            $ EmmaX.change_face("_sly", 1)
            ch_e "Hmm, another titjob?"
        else:
            $ EmmaX.change_face("_sexy", 1)
            $ EmmaX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of these? [jiggles her tits]",                 
                "So you'd like another titjob?",                 
                "A little. . . [bounces tits]?", 
                "A little warm embrace?"])
            ch_e "[Line]"
        $ Line = 0

    if approval >= 2:
        if EmmaX.Forced:
            $ EmmaX.change_face("_sad")
            $ EmmaX.change_stat("obedience", 90, 1)
            $ EmmaX.change_stat("inhibition", 60, 1)
            ch_e "I suppose there are worst ways to get you off. . ."
        elif "no_titjob" in EmmaX.daily_history:
            ch_e "Oh, very well then. . ."
        else:
            $ EmmaX.change_face("_sexy", 1)
            $ EmmaX.change_stat("love", 90, 1)
            $ EmmaX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, come over here.",                 
                "Oh, very well.",                 
                "Mmmmm.", 
                "Fine, whip it out.",
                "Fine. . . [She drools a bit into her cleavage].",
                "Oh, all right."])
            ch_e "[Line]"
            $ Line = 0
        $ EmmaX.change_stat("obedience", 20, 1)
        $ EmmaX.change_stat("obedience", 70, 1)
        $ EmmaX.change_stat("inhibition", 80, 2)
        jump Emma_TJ_Prep
    else:

        $ EmmaX.change_face("_angry")
        if "no_titjob" in EmmaX.recent_history:
            ch_e "I {i}just{/i} refused, [EmmaX.player_petname]."
        elif Taboo and "no_taboo" in EmmaX.daily_history and "no_titjob" in EmmaX.daily_history:
            ch_e "This is not an appropriate location for that. !"
        elif "no_titjob" in EmmaX.daily_history:
            ch_e "I already refused, [EmmaX.player_petname]."
        elif Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "This is not an appropriate place for that."
        else:
            $ EmmaX.change_face("_bemused")
            ch_e "Perhaps later, [EmmaX.player_petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_titjob" in EmmaX.daily_history:
                $ EmmaX.change_face("_bemused")
                ch_e "That's all right, [EmmaX.player_petname]."
                return
            "Maybe later?" if "no_titjob" not in EmmaX.daily_history:
                $ EmmaX.change_face("_sexy")
                ch_e "Perhaps."
                $ EmmaX.change_stat("love", 80, 2)
                $ EmmaX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ EmmaX.recent_history.append("no_taboo")
                    $ EmmaX.daily_history.append("no_taboo")
                $ EmmaX.recent_history.append("no_titjob")
                $ EmmaX.daily_history.append("no_titjob")
                return
            "I think this could be fun for both of us. . .":
                if approval:
                    $ EmmaX.change_face("_sexy")
                    $ EmmaX.change_stat("obedience", 80, 2)
                    $ EmmaX.change_stat("obedience", 40, 2)
                    $ EmmaX.change_stat("inhibition", 70, 3)
                    $ EmmaX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Well, sure, come over here.",                 
                            "Oh, very well.",                 
                            "Mmmmm.", 
                            "Fine, whip it out.",
                            "Fine. . . [She drools a bit into her cleavage].",
                            "Oh, all right."])
                    ch_e "[Line]"
                    $ Line = 0
                    jump Emma_TJ_Prep
                else:
                    $ approval = approval_check(EmmaX, 1100, TabM = 3)
                    if approval >= 2:
                        $ EmmaX.change_stat("inhibition", 80, 1)
                        $ EmmaX.change_stat("inhibition", 60, 3)
                        $ EmmaX.change_face("_confused", 1)
                        if EmmaX.action_counter["blowjob"]:
                            ch_e "You seemed to enjoy blowjobs, would that work instead?"
                        else:
                            ch_e "Would you perhaps prefer a blowjob?"
                        menu:
                            extend ""
                            "Ok, get down there.":
                                $ EmmaX.change_stat("love", 80, 2)
                                $ EmmaX.change_stat("inhibition", 60, 1)
                                $ EmmaX.change_stat("obedience", 50, 1)
                                jump Emma_BJ_Prep
                            "Nah, it's all about dem titties.":
                                $ Line = "no_BJ"
                    if approval:
                        $ EmmaX.change_stat("inhibition", 80, 1)
                        $ EmmaX.change_stat("inhibition", 60, 3)
                        $ EmmaX.change_face("_confused", 1)
                        ch_e "Perhaps a handjob?"
                        menu:
                            ch_e "Perhaps a handjob?"
                            "Sure, that's fine.":
                                $ EmmaX.change_stat("love", 80, 2)
                                $ EmmaX.change_stat("inhibition", 60, 1)
                                $ EmmaX.change_stat("obedience", 50, 1)
                                jump Emma_HJ_Prep
                            "Seriously, titties." if Line == "no_BJ":
                                $ Line = 0
                            "Nah, it's all about dem titties." if Line != "no_BJ":
                                pass
                    $ EmmaX.change_stat("love", 200, -2)
                    ch_e "Well, that's too bad."
                    $ EmmaX.change_stat("obedience", 70, 2)
            "Come on, let me fuck those titties, [EmmaX.petname]":


                $ EmmaX.nameCheck()
                $ approval = approval_check(EmmaX, 700, "OI", TabM = 4)
                if approval > 1 or (approval and EmmaX.Forced):
                    $ EmmaX.change_face("_sad")
                    $ EmmaX.change_stat("love", 70, -5, 1)
                    $ EmmaX.change_stat("love", 200, -2)
                    ch_e "Oh, very well."
                    $ EmmaX.change_stat("obedience", 50, 4)
                    $ EmmaX.change_stat("inhibition", 80, 1)
                    $ EmmaX.change_stat("inhibition", 60, 3)
                    $ EmmaX.Forced = 1
                    jump Emma_TJ_Prep
                else:
                    $ EmmaX.change_stat("love", 200, -15)
                    $ EmmaX.recent_history.append("_angry")
                    $ EmmaX.daily_history.append("_angry")


    if "no_titjob" in EmmaX.daily_history:
        $ EmmaX.change_face("_angry", 1)
        ch_e "I've refused, end of story."
        $ EmmaX.recent_history.append("_angry")
        $ EmmaX.daily_history.append("_angry")
    elif EmmaX.Forced:
        $ EmmaX.change_face("_angry", 1)
        ch_e "I couldn't put you through that."
        $ EmmaX.change_stat("lust", 200, 5)
        if EmmaX.love > 300:
            $ EmmaX.change_stat("love", 70, -2)
        $ EmmaX.change_stat("obedience", 50, -2)
        $ EmmaX.recent_history.append("_angry")
        $ EmmaX.daily_history.append("_angry")
    elif Taboo:
        $ EmmaX.change_face("_angry", 1)
        $ EmmaX.daily_history.append("no_taboo")
        ch_e "Can you imagine the scandal? Here?"
        $ EmmaX.change_stat("lust", 200, 5)
        $ EmmaX.change_stat("obedience", 50, -3)
    elif EmmaX.action_counter["titjob"]:
        $ EmmaX.change_face("_sad")
        ch_e "I'm afraid you'll just have to remember the last time."
    else:
        $ EmmaX.change_face("_normal", 1)
        ch_e "How about let's not, [EmmaX.player_petname]."
    $ EmmaX.recent_history.append("no_titjob")
    $ EmmaX.daily_history.append("no_titjob")
    $ approval_bonus = 0
    return

label Emma_TJ_Prep:

    if Taboo:
        $ EmmaX.inhibition += int(Taboo/10)
        $ EmmaX.lust += int(Taboo/5)


    $ EmmaX.change_face("_sexy")
    if EmmaX.Forced:
        $ EmmaX.change_face("_sad")
    elif not EmmaX.action_counter["titjob"]:
        $ EmmaX.brows = "_confused"
        $ EmmaX.eyes = "_sexy"
        $ EmmaX.mouth = "_smile"

    call Seen_First_Peen (EmmaX, Partner, React=action_context)
    call Emma_TJ_Launch ("L")

    if action_context == EmmaX:

        $ action_context = 0
        call Emma_TJ_Launch ("L")
        "[EmmaX.name] slides down and wraps her tits around your dick."
        menu:
            "What do you do?"
            "Nothing.":
                $ EmmaX.change_stat("inhibition", 80, 3)
                $ EmmaX.change_stat("inhibition", 40, 2)
                "[EmmaX.name] starts to slide them up and down."
            "Praise her.":
                $ EmmaX.change_face("_sexy", 1)
                $ EmmaX.change_stat("inhibition", 80, 3)
                ch_p "Oh, that sounds like a good idea, [EmmaX.petname]."
                $ EmmaX.nameCheck()
                "[EmmaX.name] continues her actions."
                $ EmmaX.change_stat("love", 85, 1)
                $ EmmaX.change_stat("obedience", 90, 1)
                $ EmmaX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ EmmaX.change_face("_confused")
                $ EmmaX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that for now, [EmmaX.petname]."
                $ EmmaX.nameCheck()
                "[EmmaX.name] lets it drop out from between her breasts."
                $ EmmaX.change_stat("obedience", 90, 1)
                $ EmmaX.change_stat("obedience", 50, 3)
                $ Player.recent_history.append("nope")
                $ EmmaX.add_word(1,"refused","refused")
                return
    if not EmmaX.action_counter["titjob"]:
        if EmmaX.Forced:
            $ EmmaX.change_stat("love", 90, -25)
            $ EmmaX.change_stat("obedience", 70, 30)
            $ EmmaX.change_stat("inhibition", 80, 35)
        else:
            $ EmmaX.change_stat("love", 90, 5)
            $ EmmaX.change_stat("obedience", 70, 25)
            $ EmmaX.change_stat("inhibition", 80, 30)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ EmmaX.drain_word("no_taboo")
    $ EmmaX.drain_word("no_titjob")
    $ EmmaX.recent_history.append("titjob")
    $ EmmaX.daily_history.append("titjob")


label Emma_TJ_Cycle:
    while Round > 0:
        call shift_focus (EmmaX)
        call Emma_TJ_Launch
        $ EmmaX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . ." if action_speed:
                    pass

                "Start moving? . ." if action_speed == 0:
                    $ action_speed = 1

                "Speed up. . ." if action_speed == 1:
                    $ action_speed = 2
                    "You ask her to up the pace a bit."
                "Speed up. . . (locked)" if action_speed >= 2:
                    pass

                "Stop moving" if action_speed == 1 or action_speed == 3:
                    $ action_speed = 0
                "Slow Down. . ." if action_speed == 2:
                    $ action_speed = 1
                    "You ask her to slow it down a bit."
                "Slow Down. . . (locked)" if not action_speed:
                    pass

                "Lick it" if action_speed != 3:
                    $ action_speed = 3
                "Lick it (locked)" if action_speed == 3:
                    pass

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
                        "I also want to fondle her breasts." if offhand_action != "fondle_breasts":
                            if EmmaX.remaining_actions and multi_action:
                                $ offhand_action = "fondle_breasts"
                                "You start to fondle her breasts."
                                $ EmmaX.remaining_actions -= 1
                            else:
                                ch_e "Actually, could we wrap this up soon?"
                        "Shift primary action":

                            if EmmaX.remaining_actions and multi_action:
                                menu:
                                    "How about a blowjob?":
                                        if EmmaX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Emma_TJ_After
                                            call Emma_Blowjob
                                        else:
                                            ch_e "Actually, could we wrap this up soon?"
                                    "How about a handy?":

                                        if EmmaX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Emma_BJ_After
                                            call Emma_Handjob
                                        else:
                                            ch_e "Actually, could we wrap this up soon?"
                                    "Never Mind":
                                        jump Emma_TJ_Cycle
                            else:
                                ch_e "Actually, could we wrap this up soon?"

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
                                    jump Emma_TJ_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Emma_TJ_Cycle
                                "Never mind":
                                    jump Emma_TJ_Cycle
                        "Undress [EmmaX.name]":
                            call Girl_Undress (EmmaX)
                        "Clean up [EmmaX.name] (locked)" if not EmmaX.spunk:
                            pass
                        "Clean up [EmmaX.name]" if EmmaX.spunk:
                            call Girl_Cleanup (EmmaX, "ask")
                        "Never mind":
                            jump Emma_TJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Emma_TJ_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Emma_TJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Emma_TJ_Reset
                    $ Line = 0
                    jump Emma_TJ_After


        call shift_focus (EmmaX)
        call Sex_Dialog (EmmaX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or EmmaX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (EmmaX)
                if "_angry" in EmmaX.recent_history:
                    call Emma_TJ_Reset
                    return
                $ EmmaX.change_stat("lust", 200, 5)
                if 100 > EmmaX.lust >= 70 and EmmaX.session_orgasms < 2 and EmmaX.SEXP >= 20:
                    $ EmmaX.recent_history.append("unsatisfied")
                    $ EmmaX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Emma_TJ_After
                $ Line = "came"

            if EmmaX.lust >= 100:

                call Girl_Cumming (EmmaX)
                if action_context == "shift" or "_angry" in EmmaX.recent_history:
                    jump Emma_TJ_After

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
                            jump Emma_TJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if EmmaX.SEXP >= 100 or approval_check(EmmaX, 1200, "LO"):
            pass
        elif counter == (5 + EmmaX.action_counter["titjob"]):
            $ EmmaX.brows = "_confused"
            ch_e "Are you getting close here? I'm getting a bit sore."
        elif counter == (10 + EmmaX.action_counter["titjob"]):
            $ EmmaX.brows = "_angry"
            menu:
                ch_e "I'm getting a bit worn out, could we settle this some other way?"
                "How about a BJ?" if EmmaX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Emma_TJ_After
                    call Emma_Blowjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    jump Emma_TJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Emma_TJ_Reset
                    $ action_context = "shift"
                    jump Emma_TJ_After
                "No, get back down there.":
                    if approval_check(EmmaX, 1200) or approval_check(EmmaX, 500, "O"):
                        $ EmmaX.change_stat("love", 200, -5)
                        $ EmmaX.change_stat("obedience", 50, 3)
                        $ EmmaX.change_stat("obedience", 80, 2)
                        "She grumbles but gets back to work."
                    else:
                        $ EmmaX.change_face("_angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        ch_e "Then I suppose you can handle this yourself."
                        $ EmmaX.change_stat("love", 50, -3, 1)
                        $ EmmaX.change_stat("love", 80, -4, 1)
                        $ EmmaX.change_stat("obedience", 30, -1, 1)
                        $ EmmaX.change_stat("obedience", 50, -1, 1)
                        $ EmmaX.recent_history.append("_angry")
                        $ EmmaX.daily_history.append("_angry")
                        jump Emma_TJ_After


        call Escalation (EmmaX)

        if Round == 10:
            ch_e "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."


    $ EmmaX.change_face("_bemused", 0)
    $ Line = 0
    ch_e "All right, [EmmaX.player_petname], that's plenty for now."

label Emma_TJ_After:
    $ EmmaX.change_face("_sexy")

    $ EmmaX.action_counter["titjob"] += 1
    $ EmmaX.remaining_actions -=1
    $ EmmaX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ EmmaX.addiction_rate += 1

    if Partner == "Kitty":
        call Partner_Like (EmmaX, 4, 2)
    else:
        call Partner_Like (EmmaX, 3)

    if EmmaX.action_counter["titjob"] > 5:
        pass
    elif EmmaX.action_counter["titjob"] == 1:
        $ EmmaX.SEXP += 12
        if EmmaX.love >= 500:
            $ EmmaX.mouth = "_smile"
            ch_e "Mmm, was that as good for you as it was for me?"
        elif Player.focus <= 20:
            $ EmmaX.mouth = "_sad"
            ch_e "I hope that lived up to expectations."
    elif EmmaX.action_counter["titjob"] == 5:
        ch_e "You certainly get a lot of milage out of these."


    $ approval_bonus = 0
    if action_context == "shift":
        ch_e "Mmm, so what else did you have in mind?"
    else:
        call Emma_TJ_Reset
    call checkout
    return






label Emma_Blowjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (EmmaX)
    if EmmaX.action_counter["blowjob"] >= 7:
        $ approval_bonus += 15
    elif EmmaX.action_counter["blowjob"] >= 3:
        $ approval_bonus += 10
    elif EmmaX.action_counter["blowjob"]:
        $ approval_bonus += 7

    if EmmaX.addiction >= 75 and EmmaX.event_counter["swallowed"] >=3:
        $ approval_bonus += 25
    elif EmmaX.addiction >= 75:
        $ approval_bonus += 15

    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in EmmaX.traits:
        $ approval_bonus += (4*Taboo)
    if EmmaX in Player.Harem or "sex friend" in EmmaX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in EmmaX.traits:
        $ approval_bonus -= 40
    if EmmaX.event_counter["forced"] and not EmmaX.Forced:
        $ approval_bonus -= 5*EmmaX.event_counter["forced"]

    if Taboo and "no_taboo" in EmmaX.daily_history:
        $ approval_bonus -= 10

    if "no_blowjob" in EmmaX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_blowjob" in EmmaX.recent_history else 0

    $ approval = approval_check(EmmaX, 1300, TabM = 4)

    if not EmmaX.action_counter["blowjob"] and "no_blowjob" not in EmmaX.recent_history:
        $ EmmaX.change_face("_sly")
        ch_e "So you'd like me to suck you off?"

    if not EmmaX.action_counter["blowjob"] and approval:
        if EmmaX.Forced:
            $ EmmaX.change_face("_sad")
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
        elif EmmaX.love >= (EmmaX.obedience + EmmaX.inhibition):
            $ EmmaX.change_face("_sexy")
            $ EmmaX.brows = "_sad"
            $ EmmaX.mouth = "_smile"
            ch_e "I am curious if it tastes as good as it looks. . ."
        elif EmmaX.obedience >= EmmaX.inhibition:
            $ EmmaX.change_face("_normal")
            ch_e "If that's what you want. . ."
        elif EmmaX.addiction >= 50:
            $ EmmaX.change_face("_manic", 1)
            ch_e "I don't know if I could wait. . ."
        else:
            $ EmmaX.change_face("_sad")
            $ EmmaX.mouth = "_smile"
            ch_e "I suppose. . ."
    elif approval:
        if EmmaX.Forced:
            $ EmmaX.change_face("_sad")
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
            ch_e "Ugh, that again?"
        elif not Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "Ok, I suppose this is secluded enough. . ."
        elif "blowjob" in EmmaX.recent_history:
            $ EmmaX.change_face("_sexy", 1)
            ch_e "Mmm, again? [[yawns]"
            jump Emma_BJ_Prep
        elif "blowjob" in EmmaX.daily_history:
            $ EmmaX.change_face("_sexy", 1)
            $ Line = renpy.random.choice(["Back so soon?",   
                "Let me get some saliva going.",
                "Didn't get enough earlier?",
                "My jaw's still sore from our prior engagement.",
                "My jaw's still a bit sore from earlier."])
            ch_e "[Line]"
        elif EmmaX.action_counter["blowjob"] < 3:
            $ EmmaX.change_face("_sexy", 1)
            $ EmmaX.brows = "_confused"
            $ EmmaX.mouth = "_kiss"
            ch_e "Another blowjob?"
        else:
            $ EmmaX.change_face("_sexy", 1)
            $ EmmaX.ArmPose = 2
            $ Line = renpy.random.choice(["You want me to [mimes blowing]?",                 
                "So you want another blowjob?", 
                "You want me to suck you off?",
                "Are you asking if I'm hungry?"])
            ch_e "[Line]"
        $ Line = 0

    if approval >= 2:
        if EmmaX.Forced:
            $ EmmaX.change_face("_sad")
            $ EmmaX.change_stat("obedience", 90, 1)
            $ EmmaX.change_stat("inhibition", 60, 1)
            ch_e "Fine."
        elif "no_blowjob" in EmmaX.daily_history:
            ch_e "Fine, I suppose you've earned it. . ."
        else:
            $ EmmaX.change_face("_sexy", 1)
            $ EmmaX.change_stat("love", 90, 1)
            $ EmmaX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well, ok.",                 
                "Well. . . ok.",                 
                "Mmmm.", 
                "Sure, let me have it.",
                "Mmmm. . . [She licks her lips].",
                "Ok, fine."])
            ch_e "[Line]"
            $ Line = 0
        $ EmmaX.change_stat("obedience", 20, 1)
        $ EmmaX.change_stat("obedience", 70, 1)
        $ EmmaX.change_stat("inhibition", 80, 2)
        jump Emma_BJ_Prep
    else:

        $ EmmaX.change_face("_angry")
        if "no_blowjob" in EmmaX.recent_history:
            ch_e "I believe I just told you, \"no.\""
        elif Taboo and "no_taboo" in EmmaX.daily_history and "no_blowjob" in EmmaX.daily_history:
            ch_e "I told you, this is too public!"
        elif "no_blowjob" in EmmaX.daily_history:
            ch_e "I told you \"no,\" [EmmaX.player_petname]."
        elif Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "I told you this is too public!"
        elif not EmmaX.action_counter["blowjob"]:
            $ EmmaX.change_face("_bemused")
            ch_e "I'm not sure you're up to my usual tastes, [EmmaX.player_petname]. . ."
        else:
            $ EmmaX.change_face("_bemused")
            ch_e "Perhaps later, [EmmaX.player_petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no_blowjob" in EmmaX.daily_history:
                $ EmmaX.change_face("_bemused")
                ch_e "No harm done, [EmmaX.player_petname]."
                return
            "Maybe later?" if "no_blowjob" not in EmmaX.daily_history:
                $ EmmaX.change_face("_sexy")
                ch_e "I wouldn't rule it out, [EmmaX.player_petname]."
                $ EmmaX.change_stat("love", 80, 2)
                $ EmmaX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ EmmaX.recent_history.append("no_taboo")
                    $ EmmaX.daily_history.append("no_taboo")
                $ EmmaX.recent_history.append("no_blowjob")
                $ EmmaX.daily_history.append("no_blowjob")
                return
            "Come on, please?":
                if approval:
                    $ EmmaX.change_face("_sexy")
                    $ EmmaX.change_stat("obedience", 90, 2)
                    $ EmmaX.change_stat("obedience", 50, 2)
                    $ EmmaX.change_stat("inhibition", 70, 3)
                    $ EmmaX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Well, I suppose.",                 
                        "Well. . . ok.",                 
                        "I could perhaps give it a try.", 
                        "I suppose I could. . .",
                        "Fine. . . [She licks her lips].",
                        "Hmph, ok, fine."])
                    ch_e "[Line]"
                    $ Line = 0
                    jump Emma_BJ_Prep
                else:
                    if approval_check(EmmaX, 1100, TabM = 3):
                        $ EmmaX.change_stat("inhibition", 80, 1)
                        $ EmmaX.change_stat("inhibition", 60, 3)
                        $ EmmaX.change_face("_confused", 1)
                        $ EmmaX.ArmPose = 2
                        if EmmaX.action_counter["handjob"]:
                            ch_e "I could just stroke you off, perhaps?"
                        else:
                            ch_e "Would my hand be an adequate substitute?"
                        menu:
                            extend ""
                            "Sure, that's fine.":
                                $ EmmaX.change_stat("love", 80, 2)
                                $ EmmaX.change_stat("inhibition", 60, 1)
                                $ EmmaX.change_stat("obedience", 50, 1)
                                jump Emma_HJ_Prep
                            "Nah, if it's not your mouth, forget it.":
                                $ EmmaX.change_stat("love", 200, -2)
                                $ EmmaX.ArmPose = 1
                                ch_e "Pitty."
                                $ EmmaX.change_stat("obedience", 70, 2)
            "Suck it, [EmmaX.petname]":


                $ EmmaX.nameCheck()
                $ approval = approval_check(EmmaX, 750, "OI", TabM = 3)
                if approval > 1 or (approval and EmmaX.Forced):
                    $ EmmaX.change_face("_sad")
                    $ EmmaX.change_stat("love", 70, -5, 1)
                    $ EmmaX.change_stat("love", 200, -2)
                    ch_e "Oh, fine. . ."
                    $ EmmaX.change_stat("obedience", 50, 4)
                    $ EmmaX.change_stat("inhibition", 80, 1)
                    $ EmmaX.change_stat("inhibition", 60, 3)
                    $ EmmaX.Forced = 1
                    jump Emma_BJ_Prep
                else:
                    $ EmmaX.change_stat("love", 200, -15)
                    $ EmmaX.recent_history.append("_angry")
                    $ EmmaX.daily_history.append("_angry")


    if "no_blowjob" in EmmaX.daily_history:
        $ EmmaX.change_face("_angry", 1)
        ch_e "Then I hope you can take care of yourself."
        $ EmmaX.recent_history.append("_angry")
        $ EmmaX.daily_history.append("_angry")
    elif EmmaX.Forced:
        $ EmmaX.change_face("_angry", 1)
        ch_e "You go too far!"
        $ EmmaX.change_stat("lust", 200, 5)
        if EmmaX.love > 300:
            $ EmmaX.change_stat("love", 70, -2)
        $ EmmaX.change_stat("obedience", 50, -2)
        $ EmmaX.recent_history.append("_angry")
        $ EmmaX.daily_history.append("_angry")
        $ EmmaX.recent_history.append("no_blowjob")
        $ EmmaX.daily_history.append("no_blowjob")
        return
    elif Taboo:
        $ EmmaX.change_face("_angry", 1)
        $ EmmaX.daily_history.append("no_taboo")
        ch_e "This is way too exposed!"
        $ EmmaX.change_stat("lust", 200, 5)
        $ EmmaX.change_stat("obedience", 50, -3)
        return
    elif EmmaX.action_counter["blowjob"]:
        $ EmmaX.change_face("_sad")
        ch_e "I'm just not in the mood, [EmmaX.player_petname]."
    else:
        $ EmmaX.change_face("_normal", 1)
        ch_e "I don't think I will."
    $ EmmaX.recent_history.append("no_blowjob")
    $ EmmaX.daily_history.append("no_blowjob")
    $ approval_bonus = 0
    return


label Emma_BJ_Prep:
    if renpy.showing("Emma_HJ_Animation"):
        hide Emma_HJ_Animation with easeoutbottom
    if Taboo:
        $ EmmaX.inhibition += int(Taboo/10)
        $ EmmaX.lust += int(Taboo/5)

    $ EmmaX.change_face("_sexy")
    if EmmaX.Forced:
        $ EmmaX.change_face("_sad")

    call Seen_First_Peen (EmmaX, Partner, React=action_context)
    call Emma_BJ_Launch ("L")

    if action_context == EmmaX:

        $ action_context = 0
        "[EmmaX.name] slides down and places your cock against her lips."
        menu:
            "What do you do?"
            "Nothing.":
                $ EmmaX.change_stat("inhibition", 80, 3)
                $ EmmaX.change_stat("inhibition", 40, 2)
                "[EmmaX.name] continues licking at it."
            "Praise her.":
                $ EmmaX.change_face("_sexy", 1)
                $ EmmaX.change_stat("inhibition", 80, 3)
                ch_p "Hmmm, keep doing that, [EmmaX.petname]."
                $ EmmaX.nameCheck()
                "[EmmaX.name] continues her actions."
                $ EmmaX.change_stat("love", 85, 1)
                $ EmmaX.change_stat("obedience", 90, 1)
                $ EmmaX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ EmmaX.change_face("_surprised")
                $ EmmaX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that for now, [EmmaX.petname]."
                $ EmmaX.nameCheck()
                "[EmmaX.name] puts it down."
                $ EmmaX.change_stat("obedience", 90, 1)
                $ EmmaX.change_stat("obedience", 50, 3)
                $ Player.recent_history.append("nope")
                $ EmmaX.add_word(1,"refused","refused")
                return
    if not EmmaX.action_counter["blowjob"]:
        if EmmaX.Forced:
            $ EmmaX.change_stat("love", 90, -70)
            $ EmmaX.change_stat("obedience", 70, 45)
            $ EmmaX.change_stat("inhibition", 80, 60)
        else:
            $ EmmaX.change_stat("love", 90, 5)
            $ EmmaX.change_stat("obedience", 70, 35)
            $ EmmaX.change_stat("inhibition", 80, 40)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ EmmaX.drain_word("no_taboo")
    $ EmmaX.drain_word("no_blowjob")
    $ EmmaX.recent_history.append("blowjob")
    $ EmmaX.daily_history.append("blowjob")

label Emma_BJ_Cycle:
    while Round > 0:
        call shift_focus (EmmaX)
        call Emma_BJ_Launch
        $ EmmaX.lust_face()

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
                    if "pushed" not in EmmaX.recent_history and EmmaX.action_counter["blowjob"] < 5:
                        $ EmmaX.change_stat("love", 80, -(20-(2*EmmaX.action_counter["blowjob"])))
                        $ EmmaX.change_stat("obedience", 80, (30-(3*EmmaX.action_counter["blowjob"])))
                        $ EmmaX.recent_history.append("pushed")
                    if offhand_action == "jackin" and action_speed != 3:
                        "She takes it to the root, and you move your hand out of the way."
                    $ action_speed = 4
                "Take it deeper. (locked)" if action_speed == 4:
                    pass
                "Set your own pace. . .":

                    "[EmmaX.name] hums contentedly."
                    if "setpace" not in EmmaX.recent_history:
                        $ EmmaX.change_stat("love", 80, 2)
                    $ D20 = renpy.random.randint(1, 20)
                    if EmmaX.action_counter["blowjob"] < 5:
                        $ D20 -= 10
                    elif EmmaX.action_counter["blowjob"] < 10:
                        $ D20 -= 5

                    if D20 > 15:
                        $ action_speed = 4
                        if "setpace" not in EmmaX.recent_history:
                            $ EmmaX.change_stat("inhibition", 80, 3)
                    elif D20 > 10:
                        $ action_speed = 3
                    elif D20 > 5:
                        $ action_speed = 2
                    else:
                        $ action_speed = 1
                    $ EmmaX.recent_history.append("setpace")

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
                        "I also want to fondle her breasts." if offhand_action != "fondle_breasts":
                            if EmmaX.remaining_actions and multi_action:
                                $ offhand_action = "fondle_breasts"
                                "You start to fondle her breasts."
                                $ EmmaX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (EmmaX, "tired")
                        "Shift primary action":

                            if EmmaX.remaining_actions and multi_action:
                                menu:
                                    "How about a handy?":
                                        if EmmaX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Emma_BJ_After
                                            call Emma_Handjob
                                        else:
                                            ch_e "I'm kinda tired, could we just wrap this up. . ."
                                    "How about a titjob?":
                                        if EmmaX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Emma_BJ_After
                                            call Emma_Titjob
                                        else:
                                            ch_e "I'm kinda tired, could we just wrap this up. . ."
                                    "Never Mind":
                                        jump Emma_BJ_Cycle
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
                                    jump Emma_BJ_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Emma_BJ_Cycle
                                "Never mind":
                                    jump Emma_BJ_Cycle
                        "Undress [EmmaX.name]":
                            call Girl_Undress (EmmaX)
                        "Clean up [EmmaX.name] (locked)" if not EmmaX.spunk:
                            pass
                        "Clean up [EmmaX.name]" if EmmaX.spunk:
                            call Girl_Cleanup (EmmaX, "ask")
                        "Never mind":
                            jump Emma_BJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Emma_BJ_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Emma_BJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Emma_BJ_Reset
                    $ Line = 0
                    jump Emma_BJ_After


        call shift_focus (EmmaX)
        call Sex_Dialog (EmmaX, Partner)



        $ counter += 1
        $ Round -= 1
        if action_speed:
            $ Player.cock_wet = 1
            $ Player.spunk = 0 if Player.spunk else Player.spunk

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or EmmaX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (EmmaX)
                if "_angry" in EmmaX.recent_history:
                    call Emma_BJ_Reset
                    return
                $ EmmaX.change_stat("lust", 200, 5)
                if 100 > EmmaX.lust >= 70 and EmmaX.session_orgasms < 2 and EmmaX.SEXP >= 20:
                    $ EmmaX.recent_history.append("unsatisfied")
                    $ EmmaX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Emma_BJ_After
                $ Line = "came"

            if EmmaX.lust >= 100:

                call Girl_Cumming (EmmaX)
                if action_context == "shift" or "_angry" in EmmaX.recent_history:
                    jump Emma_BJ_After

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
                            jump Emma_BJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if EmmaX.SEXP >= 100 or approval_check(EmmaX, 1200, "LO"):
            pass
        elif counter == (15 + EmmaX.action_counter["blowjob"]):
            $ EmmaX.brows = "_angry"
            menu:
                ch_e "I'm getting a bit worn out here, could we do something else?"
                "How about a Handy?" if EmmaX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Emma_BJ_After
                    call Emma_Handjob
                    return
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    $ counter += 1
                    "[Line]."
                    jump Emma_BJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Emma_BJ_Reset
                    $ action_context = "shift"
                    jump Emma_BJ_After
                "No, get back down there.":
                    if approval_check(EmmaX, 1200) or approval_check(EmmaX, 500, "O"):
                        $ EmmaX.change_stat("love", 200, -5)
                        $ EmmaX.change_stat("obedience", 50, 3)
                        $ EmmaX.change_stat("obedience", 80, 2)
                        "She scowls but gets back to work."
                    else:
                        $ EmmaX.change_face("_angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        ch_e "Well then."
                        $ EmmaX.change_stat("love", 50, -3, 1)
                        $ EmmaX.change_stat("love", 80, -4, 1)
                        $ EmmaX.change_stat("obedience", 30, -1, 1)
                        $ EmmaX.change_stat("obedience", 50, -1, 1)
                        $ EmmaX.recent_history.append("_angry")
                        $ EmmaX.daily_history.append("_angry")
                        jump Emma_BJ_After
        elif counter == (10 + EmmaX.action_counter["blowjob"]) and EmmaX.SEXP <= 100 and not approval_check(EmmaX, 1200, "LO"):
            $ EmmaX.brows = "_confused"
            ch_e "Are you about done? I'm a little tired of this."


        call Escalation (EmmaX)

        if Round == 10:
            ch_e "It's getting a bit late. . ."
        elif Round == 5:
            ch_e "Do you mind if we take a break?"


    $ EmmaX.change_face("_bemused", 0)
    $ Line = 0
    ch_e "Ok, I need to rest my jaw for a minute. . ."

label Emma_BJ_After:
    $ EmmaX.change_face("_sexy")

    $ EmmaX.action_counter["blowjob"] += 1
    $ EmmaX.remaining_actions -=1
    $ EmmaX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ EmmaX.addiction_rate += 1

    call Partner_Like (EmmaX, 2)

    if "Emma Jobber" in Achievements:
        pass
    elif EmmaX.action_counter["blowjob"] >= 10:
        $ EmmaX.change_face("_smile", 1)
        ch_e "You taste positively intoxicating, [EmmaX.player_petname]."
        $ Achievements.append("Emma Jobber")
        $ EmmaX.SEXP += 5
    elif action_context == "shift":
        pass
    elif EmmaX.action_counter["blowjob"] == 1:
        $ EmmaX.SEXP += 15
        if EmmaX.love >= 500:
            $ EmmaX.mouth = "_smile"
            ch_e "Hmm, better than I'd imagined. . ."
        elif Player.focus <= 20:
            $ EmmaX.mouth = "_sad"
            ch_e "Was it all you dreamed of?"
    elif EmmaX.action_counter["blowjob"] == 5:
        ch_e "Best you've had, I'm sure."
        menu:
            "[[nod]":
                $ EmmaX.change_face("_smile", 1)
                $ EmmaX.change_stat("love", 90, 10)
                $ EmmaX.change_stat("obedience", 80, 5)
                $ EmmaX.change_stat("inhibition", 90, 10)
            "[[shake head \"no\"]":
                if approval_check(EmmaX, 500, "O"):
                    $ EmmaX.change_face("_sad", 2)
                    $ EmmaX.change_stat("love", 200, -5)
                else:
                    $ EmmaX.change_face("_angry", 2)
                    $ EmmaX.change_stat("love", 200, -30)
                $ EmmaX.change_stat("obedience", 80, 20)
                ch_e ". . ."
                $ EmmaX.change_face("_sad", 1)

    $ approval_bonus = 0
    if action_context != "shift":
        call Emma_BJ_Reset
    call checkout
    return






label Emma_Dildo_Check:
    if "_dildo" in Player.inventory:
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "_dildo" in EmmaX.inventory:
        "You ask [EmmaX.name] to get out her favorite Dildo."
    else:
        "You don't have one of those on you."
        return 0
    return 1

label Emma_Dildo_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (EmmaX)
    call Emma_Dildo_Check
    if not _return:
        return

    if EmmaX.action_counter["dildo_pussy"]:
        $ approval_bonus += 15
    if EmmaX.PantsNum() >= 6:
        $ approval_bonus -= 20

    if EmmaX.lust > 95:
        $ approval_bonus += 20
    elif EmmaX.lust > 85:
        $ approval_bonus += 15

    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in EmmaX.traits:
        $ approval_bonus += (5*Taboo)
    if EmmaX in Player.Harem or "sex friend" in EmmaX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in EmmaX.traits:
        $ approval_bonus -= 40
    if EmmaX.event_counter["forced"] and not EmmaX.Forced:
        $ approval_bonus -= 5*EmmaX.event_counter["forced"]

    if Taboo and "no_taboo" in EmmaX.daily_history:
        $ approval_bonus -= 10

    if "no_dildo" in EmmaX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_dildo" in EmmaX.recent_history else 0

    $ approval = approval_check(EmmaX, 1250, TabM = 4)

    if action_context == EmmaX:
        if approval > 2:
            if EmmaX.PantsNum() == 5:
                "[EmmaX.name] grabs her dildo, hiking up her skirt as she does."
                $ EmmaX.upskirt = 1
            elif EmmaX.PantsNum() > 6:
                "[EmmaX.name] grabs her dildo, pulling down her pants as she does."
                $ EmmaX.legs = ""
            else:
                "[EmmaX.name] grabs her dildo, rubbing is suggestively against her crotch."
            $ EmmaX.SeenPanties = 1
            "She slides the tip along her pussy and seems to want you to insert it."
            menu:
                "What do you do?"
                "Nothing.":
                    $ EmmaX.change_stat("inhibition", 80, 3)
                    $ EmmaX.change_stat("inhibition", 50, 2)
                    "[EmmaX.name] slides it in."
                "Go for it.":
                    $ EmmaX.change_face("_sexy", 1)
                    $ EmmaX.change_stat("inhibition", 80, 3)
                    ch_p "Oh yeah, [EmmaX.petname], let's do this."
                    $ EmmaX.nameCheck()
                    "You grab the dildo and slide it in."
                    $ EmmaX.change_stat("love", 85, 1)
                    $ EmmaX.change_stat("obedience", 90, 1)
                    $ EmmaX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ EmmaX.change_face("_surprised")
                    $ EmmaX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that right now, [EmmaX.petname]."
                    $ EmmaX.nameCheck()
                    "[EmmaX.name] sets the dildo down."
                    $ EmmaX.change_outfit()
                    $ EmmaX.change_stat("obedience", 90, 1)
                    $ EmmaX.change_stat("obedience", 50, 1)
                    $ EmmaX.change_stat("obedience", 30, 2)
                    return
            jump Emma_DP_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
        return

    if action_context == "auto":
        "You rub the dildo across her body, and along her moist slit."
        $ EmmaX.change_face("_surprised", 1)

        if (EmmaX.action_counter["dildo_pussy"] and approval) or (approval > 1):
            "[EmmaX.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            $ EmmaX.change_face("_sexy")
            $ EmmaX.change_stat("obedience", 70, 3)
            $ EmmaX.change_stat("inhibition", 50, 3)
            $ EmmaX.change_stat("inhibition", 70, 1)
            ch_e "Hmm, [EmmaX.player_petname], toys!"
            jump Emma_DP_Prep
        else:
            $ EmmaX.brows = "_angry"
            menu:
                ch_e "Excuse yourself, what are you planning to do with that?!"
                "Sorry, sorry! Never mind.":
                    if approval:
                        $ EmmaX.change_face("_sexy", 1)
                        $ EmmaX.change_stat("obedience", 70, 3)
                        $ EmmaX.change_stat("inhibition", 50, 3)
                        $ EmmaX.change_stat("inhibition", 70, 1)
                        ch_e "Well, now that you mention it. . ."
                        jump Emma_DP_Prep
                    "You pull back before you really get it in."
                    $ EmmaX.change_face("_bemused", 1)
                    if EmmaX.action_counter["dildo_pussy"]:
                        ch_e "Well, [EmmaX.player_petname], maybe warn me next time?"
                    else:
                        ch_e "Well, [EmmaX.player_petname], that's a little much. . . for now . . ."
                "Just playing with my favorite toys.":
                    $ EmmaX.change_stat("love", 80, -10, 1)
                    $ EmmaX.change_stat("love", 200, -10)
                    "You press it inside some more."
                    $ EmmaX.change_stat("obedience", 70, 3)
                    $ EmmaX.change_stat("inhibition", 50, 3)
                    if not approval_check(EmmaX, 700, "O", TabM=1):
                        $ EmmaX.change_face("_angry")
                        "[EmmaX.name] shoves you away and slaps you in the face."
                        ch_e "Ask nicely before trying anything like that!"
                        $ EmmaX.change_stat("love", 50, -10, 1)
                        $ EmmaX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        if renpy.showing("Emma_SexSprite"):
                            call Emma_Sex_Reset
                        $ EmmaX.recent_history.append("_angry")
                        $ EmmaX.daily_history.append("_angry")
                    else:
                        $ EmmaX.change_face("_sad")
                        "[EmmaX.name] doesn't seem to be into this, you're lucky she's so obedient."
                        jump Emma_DP_Prep
        return


    if not EmmaX.action_counter["dildo_pussy"]:

        $ EmmaX.change_face("_surprised", 1)
        $ EmmaX.mouth = "_kiss"
        ch_e "Hmmm, so you'd like to try out some toys?"
        if EmmaX.Forced:
            $ EmmaX.change_face("_sad")
            ch_e "I suppose there are worst things you could ask for."

    if not EmmaX.action_counter["dildo_pussy"] and approval:

        if EmmaX.Forced:
            $ EmmaX.change_face("_sad")
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
        elif EmmaX.love >= (EmmaX.obedience + EmmaX.inhibition):
            $ EmmaX.change_face("_sexy")
            $ EmmaX.brows = "_sad"
            $ EmmaX.mouth = "_smile"
            ch_e "I've had a reasonable amount of experience with these, you know. . ."
        elif EmmaX.obedience >= EmmaX.inhibition:
            $ EmmaX.change_face("_normal")
            ch_e "If that's what you want, [EmmaX.player_petname]. . ."
        else:
            $ EmmaX.change_face("_sad")
            $ EmmaX.mouth = "_smile"
            ch_e "I guess it could be fun with a partner. . ."

    elif approval:

        if EmmaX.Forced:
            $ EmmaX.change_face("_sad")
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
            ch_e "The toys again?"
        elif not Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "Well, at least you got us some privacy this time. . ."
        elif "dildo_pussy" in EmmaX.recent_history:
            $ EmmaX.change_face("_sexy", 1)
            ch_e "Mmm, again? Ok, let's get to it."
            jump Emma_DP_Prep
        elif "dildo_pussy" in EmmaX.daily_history:
            $ EmmaX.change_face("_sexy", 1)
            $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "You're going to wear me out."])
            ch_e "[Line]"
        elif EmmaX.action_counter["dildo_pussy"] < 3:
            $ EmmaX.change_face("_sexy", 1)
            $ EmmaX.brows = "_confused"
            $ EmmaX.mouth = "_kiss"
            ch_e "You want to stick it in my pussy again?"
        else:
            $ EmmaX.change_face("_sexy", 1)
            $ EmmaX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my pussy again?",
                    "You want me ta lube up your toy?"])
            ch_e "[Line]"
            $ Line = 0

    if approval >= 2:

        if EmmaX.Forced:
            $ EmmaX.change_face("_sad")
            $ EmmaX.change_stat("obedience", 90, 1)
            $ EmmaX.change_stat("inhibition", 60, 1)
            ch_e "Ok, fine."
        else:
            $ EmmaX.change_face("_sexy", 1)
            $ EmmaX.change_stat("love", 90, 1)
            $ EmmaX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                    "Well. . . ok.",                 
                    "Sure!", 
                    "I guess I could. . . stick it in.",
                    "Delightful.",
                    "Hmm, ok, ok."])
            ch_e "[Line]"
            $ Line = 0
        $ EmmaX.change_stat("obedience", 20, 1)
        $ EmmaX.change_stat("obedience", 60, 1)
        $ EmmaX.change_stat("inhibition", 70, 2)
        jump Emma_DP_Prep
    else:


        $ EmmaX.change_face("_angry")
        if "no_dildo" in EmmaX.recent_history:
            ch_e "What part of \"no,\" did you not get, [EmmaX.player_petname]?"
        elif Taboo and "no_taboo" in EmmaX.daily_history and "no_dildo" in EmmaX.daily_history:
            ch_e "Stop showing that thing around in public!"
        elif "no_dildo" in EmmaX.daily_history:
            ch_e "I already told you \"no,\" [EmmaX.player_petname]."
        elif Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "Stop showing that thing around in public!"
        elif not EmmaX.action_counter["dildo_pussy"]:
            $ EmmaX.change_face("_bemused")
            ch_e "I'm a bit past toys, [EmmaX.player_petname]. . ."
        else:
            $ EmmaX.change_face("_bemused")
            ch_e "We don't need any toys, do we, [EmmaX.player_petname]?"
        menu:
            extend ""
            "Sorry, never mind." if "no_dildo" in EmmaX.daily_history:
                $ EmmaX.change_face("_bemused")
                ch_e "I thought as much, [EmmaX.player_petname]."
                return
            "Maybe later?" if "no_dildo" not in EmmaX.daily_history:
                $ EmmaX.change_face("_sexy")
                ch_e "Maybe I'll practice on my own time, [EmmaX.player_petname]."
                $ EmmaX.change_stat("love", 80, 2)
                $ EmmaX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ EmmaX.recent_history.append("no_taboo")
                    $ EmmaX.daily_history.append("no_taboo")
                $ EmmaX.recent_history.append("no_dildo")
                $ EmmaX.daily_history.append("no_dildo")
                return
            "I think you'd like it. . .":
                if approval:
                    $ EmmaX.change_face("_sexy")
                    $ EmmaX.change_stat("obedience", 90, 2)
                    $ EmmaX.change_stat("obedience", 50, 2)
                    $ EmmaX.change_stat("inhibition", 70, 3)
                    $ EmmaX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                            "I suppose. . .", 
                            "You make a compelling argument."])
                    ch_e "[Line]"
                    $ Line = 0
                    jump Emma_DP_Prep
                else:
                    pass
            "[[press it against her]":

                $ approval = approval_check(EmmaX, 950, "OI", TabM = 3)
                if approval > 1 or (approval and EmmaX.Forced):
                    $ EmmaX.change_face("_sad")
                    $ EmmaX.change_stat("love", 70, -5, 1)
                    $ EmmaX.change_stat("love", 200, -5)
                    ch_e "Ok, fine. If we're going to do this, stick it in already."
                    $ EmmaX.change_stat("obedience", 80, 4)
                    $ EmmaX.change_stat("inhibition", 80, 1)
                    $ EmmaX.change_stat("inhibition", 60, 3)
                    $ EmmaX.Forced = 1
                    jump Emma_DP_Prep
                else:
                    $ EmmaX.change_stat("love", 200, -20)
                    $ EmmaX.recent_history.append("_angry")
                    $ EmmaX.daily_history.append("_angry")


    $ EmmaX.ArmPose = 1
    if "no_dildo" in EmmaX.daily_history:
        ch_e "Learn to take \"no\" for an answer, [EmmaX.player_petname]."
        $ EmmaX.recent_history.append("_angry")
        $ EmmaX.daily_history.append("_angry")
    elif EmmaX.Forced:
        $ EmmaX.change_face("_angry", 1)
        ch_e "I'm not going to let you use that on me."
        $ EmmaX.change_stat("lust", 200, 5)
        if EmmaX.love > 300:
            $ EmmaX.change_stat("love", 70, -2)
        $ EmmaX.change_stat("obedience", 50, -2)
        $ EmmaX.recent_history.append("_angry")
        $ EmmaX.daily_history.append("_angry")
    elif Taboo:
        $ EmmaX.change_face("_angry", 1)
        $ EmmaX.recent_history.append("no_taboo")
        $ EmmaX.daily_history.append("no_taboo")
        ch_e "Not here!"
        $ EmmaX.change_stat("lust", 200, 5)
        $ EmmaX.change_stat("obedience", 50, -3)
    elif EmmaX.action_counter["dildo_pussy"]:
        $ EmmaX.change_face("_sad")
        ch_e "Sorry, you can keep your toys to yourself."
    else:
        $ EmmaX.change_face("_normal", 1)
        ch_e "No way."
    $ EmmaX.recent_history.append("no_dildo")
    $ EmmaX.daily_history.append("no_dildo")
    $ approval_bonus = 0
    return

label Emma_DP_Prep:
    if offhand_action == "dildo_pussy":
        return

    if not EmmaX.Forced and action_context != "auto":
        $ approval_bonus = 15 if EmmaX.PantsNum() > 6 else 0
        call Bottoms_Off (EmmaX)
        if "_angry" in EmmaX.recent_history:
            return

    $ approval_bonus = 0
    call Emma_Pussy_Launch ("dildo_pussy")
    if not EmmaX.action_counter["dildo_pussy"]:
        if EmmaX.Forced:
            $ EmmaX.change_stat("love", 90, -75)
            $ EmmaX.change_stat("obedience", 70, 60)
            $ EmmaX.change_stat("inhibition", 80, 35)
        else:
            $ EmmaX.change_stat("love", 90, 10)
            $ EmmaX.change_stat("obedience", 70, 20)
            $ EmmaX.change_stat("inhibition", 80, 45)
    if Taboo:
        $ EmmaX.inhibition += int(Taboo/10)
        $ EmmaX.lust += int(Taboo/5)


    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ EmmaX.drain_word("no_taboo")
    $ EmmaX.drain_word("no_dildo")
    $ EmmaX.recent_history.append("dildo_pussy")
    $ EmmaX.daily_history.append("dildo_pussy")

label Emma_DP_Cycle:
    while Round > 0:
        call shift_focus (EmmaX)
        call Emma_Pussy_Launch ("dildo_pussy")
        $ EmmaX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (EmmaX)
                    jump Emma_DP_Cycle

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
                            if EmmaX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ EmmaX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (EmmaX, "tired")
                        "Shift primary action":

                            if EmmaX.remaining_actions and multi_action:
                                menu:
                                    "I want to stick a finger in her ass.":
                                        $ action_context = "shift"
                                        call Emma_DP_After
                                        call Emma_Insert_Ass
                                    "Just stick a finger in her ass without asking.":
                                        $ action_context = "auto"
                                        call Emma_DP_After
                                        call Emma_Insert_Ass
                                    "I want to shift the dildo to her ass.":
                                        $ action_context = "shift"
                                        call Emma_DP_After
                                        call Emma_Dildo_Ass
                                    "Never Mind":
                                        jump Emma_DP_Cycle
                            else:
                                call Sex_Basic_Dialog (EmmaX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Emma_DP_After
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
                                    jump Emma_DP_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Emma_DP_Cycle
                                "Never mind":
                                    jump Emma_DP_Cycle
                        "Undress [EmmaX.name]":
                            call Girl_Undress (EmmaX)
                        "Clean up [EmmaX.name] (locked)" if not EmmaX.spunk:
                            pass
                        "Clean up [EmmaX.name]" if EmmaX.spunk:
                            call Girl_Cleanup (EmmaX, "ask")
                        "Never mind":
                            jump Emma_DP_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Emma_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Emma_DP_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Emma_Pos_Reset
                    $ Line = 0
                    jump Emma_DP_After


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
                if "_angry" in EmmaX.recent_history:
                    call Emma_Pos_Reset
                    return
                $ EmmaX.change_stat("lust", 200, 5)
                if 100 > EmmaX.lust >= 70 and EmmaX.session_orgasms < 2:
                    $ EmmaX.recent_history.append("unsatisfied")
                    $ EmmaX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Emma_DP_After
                $ Line = "came"
            if EmmaX.lust >= 100:

                call Girl_Cumming (EmmaX)
                if action_context == "shift" or "_angry" in EmmaX.recent_history:
                    jump Emma_DP_After
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
                            jump Emma_DP_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if EmmaX.SEXP >= 100 or approval_check(EmmaX, 1200, "LO"):
            pass
        elif counter == (5 + EmmaX.action_counter["dildo_pussy"]):
            $ EmmaX.brows = "_confused"
            ch_e "What are you even doing down there?"
        elif EmmaX.lust >= 80:
            pass
        elif counter == (15 + EmmaX.action_counter["dildo_pussy"]) and EmmaX.SEXP >= 15 and not approval_check(EmmaX, 1500):
            $ EmmaX.brows = "_confused"
            menu:
                ch_e "[EmmaX.player_petname], this is getting uncomfortable, maybe we could try something else."
                "Finish up.":
                    "You let go. . ."
                    jump Emma_DP_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Emma_DP_After
                "No, this is fun.":
                    if approval_check(EmmaX, 1200) or approval_check(EmmaX, 500, "O"):
                        $ EmmaX.change_stat("love", 200, -5)
                        $ EmmaX.change_stat("obedience", 50, 3)
                        $ EmmaX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ EmmaX.change_face("_angry", 1)
                        call Emma_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_e "Well if that's your attitude, I don't need your \"help\"."
                        $ EmmaX.change_stat("love", 50, -3, 1)
                        $ EmmaX.change_stat("love", 80, -4, 1)
                        $ EmmaX.change_stat("obedience", 30, -1, 1)
                        $ EmmaX.change_stat("obedience", 50, -1, 1)
                        $ EmmaX.recent_history.append("_angry")
                        $ EmmaX.daily_history.append("_angry")
                        jump Emma_DP_After


        if Round == 10:
            ch_e "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."


    $ EmmaX.change_face("_bemused", 0)
    $ Line = 0
    ch_e "Ok, [EmmaX.player_petname], that's enough of that for now."


label Emma_DP_After:
    if not action_context:
        call Emma_Pos_Reset

    $ EmmaX.change_face("_sexy")

    $ EmmaX.action_counter["dildo_pussy"] += 1
    $ EmmaX.remaining_actions -=1

    call Partner_Like (EmmaX, 1)

    if EmmaX.action_counter["dildo_pussy"] == 1:
        $ EmmaX.SEXP += 10
        if not action_context:
            if EmmaX.love >= 500 and "unsatisfied" not in EmmaX.recent_history:
                ch_e "I appreciate the work you put in. . ."
            elif EmmaX.obedience <= 500 and Player.focus <= 20:
                $ EmmaX.change_face("_perplexed", 1)
                ch_e "Did you enjoy that?"

    $ approval_bonus = 0


    call checkout
    return






label Emma_Dildo_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (EmmaX)
    call Emma_Dildo_Check
    if not _return:
        return

    if EmmaX.used_to_anal:
        $ approval_bonus += 30
    elif "anal" in EmmaX.recent_history or "dildo_anal" in EmmaX.recent_history:
        $ approval_bonus -= 20
    elif "anal" in EmmaX.daily_history or "dildo_anal" in EmmaX.daily_history:
        $ approval_bonus -= 10
    elif (EmmaX.action_counter["anal"] + EmmaX.action_counter["dildo_ass"] + EmmaX.Plug) > 0:
        $ approval_bonus += 20

    if EmmaX.PantsNum() >= 6:
        $ approval_bonus -= 20

    if EmmaX.lust > 95:
        $ approval_bonus += 20
    elif EmmaX.lust > 85:
        $ approval_bonus += 15

    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in EmmaX.traits:
        $ approval_bonus += (5*Taboo)
    if EmmaX in Player.Harem or "sex friend" in EmmaX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in EmmaX.traits:
        $ approval_bonus -= 40
    if EmmaX.event_counter["forced"] and not EmmaX.Forced:
        $ approval_bonus -= 5*EmmaX.event_counter["forced"]

    if Taboo and "no_taboo" in EmmaX.daily_history:
        $ approval_bonus -= 10

    if "no_dildo" in EmmaX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_dildo" in EmmaX.recent_history else 0

    $ approval = approval_check(EmmaX, 1450, TabM = 4)

    if action_context == EmmaX:

        if approval > 2:
            if EmmaX.PantsNum() == 5:
                "[EmmaX.name] grabs her dildo, hiking up her skirt as she does."
                $ EmmaX.upskirt = 1
            elif EmmaX.PantsNum() > 6:
                "[EmmaX.name] grabs her dildo, pulling down her pants as she does."
                $ EmmaX.legs = ""
            else:
                "[EmmaX.name] grabs her dildo, rubbing is suggestively against her ass."
            $ EmmaX.SeenPanties = 1
            "She slides the tip against her asshole, and seems to want you to insert it."
            menu:
                "What do you do?"
                "Nothing.":
                    $ EmmaX.change_stat("inhibition", 80, 3)
                    $ EmmaX.change_stat("inhibition", 50, 2)
                    "[EmmaX.name] slides it in."
                "Go for it.":
                    $ EmmaX.change_face("_sexy", 1)
                    $ EmmaX.change_stat("inhibition", 80, 3)
                    ch_p "Oh yeah, [EmmaX.petname], let's do this."
                    $ EmmaX.nameCheck()
                    "You grab the dildo and slide it in."
                    $ EmmaX.change_stat("love", 85, 1)
                    $ EmmaX.change_stat("obedience", 90, 1)
                    $ EmmaX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ EmmaX.change_face("_surprised")
                    $ EmmaX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that right now, [EmmaX.petname]."
                    $ EmmaX.nameCheck()
                    "[EmmaX.name] sets the dildo down."
                    $ EmmaX.change_outfit()
                    $ EmmaX.change_stat("obedience", 90, 1)
                    $ EmmaX.change_stat("obedience", 50, 1)
                    $ EmmaX.change_stat("obedience", 30, 2)
                    return
            jump Emma_DA_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
        return

    if action_context == "auto":
        "You rub the dildo across her body, and against her tight anus."
        $ EmmaX.change_face("_surprised", 1)

        if (EmmaX.action_counter["dildo_ass"] and approval) or (approval > 1):

            "[EmmaX.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            $ EmmaX.change_face("_sexy")
            $ EmmaX.change_stat("obedience", 70, 3)
            $ EmmaX.change_stat("inhibition", 50, 3)
            $ EmmaX.change_stat("inhibition", 70, 1)
            ch_e "Mmmm, [EmmaX.player_petname], toys. . ."
            jump Emma_DA_Prep
        else:

            $ EmmaX.brows = "_angry"
            menu:
                ch_e "Excuse yourself, what are you planning to do with that?!"
                "Sorry, sorry! Never mind.":
                    if approval:
                        $ EmmaX.change_face("_sexy", 1)
                        $ EmmaX.change_stat("obedience", 70, 3)
                        $ EmmaX.change_stat("inhibition", 50, 3)
                        $ EmmaX.change_stat("inhibition", 70, 1)
                        ch_e "Well, now that you mention it. . ."
                        jump Emma_DA_Prep
                    "You pull back before you really get it in."
                    $ EmmaX.change_face("_bemused", 1)
                    if EmmaX.action_counter["dildo_ass"]:
                        ch_e "Well, [EmmaX.player_petname], maybe warn me next time?"
                    else:
                        ch_e "Well, [EmmaX.player_petname], that's a little much. . . for now . . ."
                "Just playing with my favorite toys.":
                    $ EmmaX.change_stat("love", 80, -10, 1)
                    $ EmmaX.change_stat("love", 200, -10)
                    "You press it inside some more."
                    $ EmmaX.change_stat("obedience", 70, 3)
                    $ EmmaX.change_stat("inhibition", 50, 3)
                    if not approval_check(EmmaX, 700, "O", TabM=1):
                        $ EmmaX.change_face("_angry")
                        "[EmmaX.name] shoves you away and slaps you in the face."
                        ch_e "Ask nicely if you want to stick something in my ass!"
                        $ EmmaX.change_stat("love", 50, -10, 1)
                        $ EmmaX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        if renpy.showing("Emma_SexSprite"):
                            call Emma_Sex_Reset
                        $ EmmaX.recent_history.append("_angry")
                        $ EmmaX.daily_history.append("_angry")
                    else:
                        $ EmmaX.change_face("_sad")
                        "[EmmaX.name] doesn't seem to be into this, you're lucky she's so obedient."
                        jump Emma_DA_Prep
        return


    if not EmmaX.action_counter["dildo_ass"]:

        $ EmmaX.change_face("_surprised", 1)
        $ EmmaX.mouth = "_kiss"
        ch_e "Hmm, you don't take half measures. . ."
        if EmmaX.Forced:
            $ EmmaX.change_face("_sad")
            ch_e "They always go for the butt. . ."

    if not EmmaX.action_counter["dildo_ass"] and approval:

        if EmmaX.Forced:
            $ EmmaX.change_face("_sad")
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
        elif EmmaX.love >= (EmmaX.obedience + EmmaX.inhibition):
            $ EmmaX.change_face("_sexy")
            $ EmmaX.brows = "_sad"
            $ EmmaX.mouth = "_smile"
            ch_e "I suppose you might enjoy that. . ."
        elif EmmaX.obedience >= EmmaX.inhibition:
            $ EmmaX.change_face("_normal")
            ch_e "If that's what you want, [EmmaX.player_petname]. . ."
        else:
            $ EmmaX.change_face("_sad")
            $ EmmaX.mouth = "_smile"
            ch_e "I suppose I could enjoy that. . ."

    elif approval:

        if EmmaX.Forced:
            $ EmmaX.change_face("_sad")
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
            ch_e "The toys again?"
        elif not Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "Well, at least you got us some privacy this time. . ."
        elif "dildo_anal" in EmmaX.daily_history and not EmmaX.used_to_anal:
            pass
        elif EmmaX.action_counter["dildo_ass"] < 3:
            $ EmmaX.change_face("_sexy", 1)
            $ EmmaX.brows = "_confused"
            $ EmmaX.mouth = "_kiss"
            ch_e "You want to stick it in my ass again?"
        else:
            $ EmmaX.change_face("_sexy", 1)
            $ EmmaX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You'd like to stick it in my ass again?",
                    "You'd like me to lube up your toy?"])
            ch_e "[Line]"
            $ Line = 0

    if approval >= 2:

        if EmmaX.Forced:
            $ EmmaX.change_face("_sad")
            $ EmmaX.change_stat("obedience", 90, 1)
            $ EmmaX.change_stat("inhibition", 60, 1)
            ch_e "Oh, fine."
        else:
            $ EmmaX.change_face("_sexy", 1)
            $ EmmaX.change_stat("love", 90, 1)
            $ EmmaX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                    "Hmm. . . ok.",                 
                    "Sure!", 
                    "I guess I could. . . stick it in.",
                    "Delightful.",
                    "Hmm, ok, ok."])
            ch_e "[Line]"
            $ Line = 0
        $ EmmaX.change_stat("obedience", 20, 1)
        $ EmmaX.change_stat("obedience", 60, 1)
        $ EmmaX.change_stat("inhibition", 70, 2)
        jump Emma_DA_Prep
    else:


        $ EmmaX.change_face("_angry")
        if "no_dildo" in EmmaX.recent_history:
            ch_e "What part of \"no,\" did you not get, [EmmaX.player_petname]?"
        elif Taboo and "no_taboo" in EmmaX.daily_history and "no_dildo" in EmmaX.daily_history:
            ch_e "Stop swinging that thing around in public!"
        elif "no_dildo" in EmmaX.daily_history:
            ch_e "I already told you \"no,\" [EmmaX.player_petname]."
        elif Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "I already told you that I wouldn't do that out here!"
        elif not EmmaX.action_counter["dildo_ass"]:
            $ EmmaX.change_face("_bemused")
            ch_e "I'm just not into toys, [EmmaX.player_petname]. . ."
        else:
            $ EmmaX.change_face("_bemused")
            ch_e "I don't think we need any toys, [EmmaX.player_petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no_dildo" in EmmaX.daily_history:
                $ EmmaX.change_face("_bemused")
                ch_e "I'm sure, [EmmaX.player_petname]."
                return
            "Maybe later?" if "no_dildo" not in EmmaX.daily_history:
                $ EmmaX.change_face("_sexy")
                ch_e "Perhaps I'll practice on my own time, [EmmaX.player_petname]."
                $ EmmaX.change_stat("love", 80, 2)
                $ EmmaX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ EmmaX.recent_history.append("no_taboo")
                    $ EmmaX.daily_history.append("no_taboo")
                $ EmmaX.recent_history.append("no_dildo")
                $ EmmaX.daily_history.append("no_dildo")
                return
            "I think you'd like it. . .":
                if approval:
                    $ EmmaX.change_face("_sexy")
                    $ EmmaX.change_stat("obedience", 90, 2)
                    $ EmmaX.change_stat("obedience", 50, 2)
                    $ EmmaX.change_stat("inhibition", 70, 3)
                    $ EmmaX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Very well, stick it in.",     
                            "I suppose. . .", 
                            "You make a compelling argument."])
                    ch_e "[Line]"
                    $ Line = 0
                    jump Emma_DA_Prep
                else:
                    pass
            "[[press it against her]":

                $ approval = approval_check(EmmaX, 1050, "OI", TabM = 3)
                if approval > 1 or (approval and EmmaX.Forced):
                    $ EmmaX.change_face("_sad")
                    $ EmmaX.change_stat("love", 70, -5, 1)
                    $ EmmaX.change_stat("love", 200, -5)
                    ch_e "Ok, fine. If we're going to do this, stick it in already."
                    $ EmmaX.change_stat("obedience", 80, 4)
                    $ EmmaX.change_stat("inhibition", 80, 1)
                    $ EmmaX.change_stat("inhibition", 60, 3)
                    $ EmmaX.Forced = 1
                    jump Emma_DA_Prep
                else:
                    $ EmmaX.change_stat("love", 200, -20)
                    $ EmmaX.recent_history.append("_angry")
                    $ EmmaX.daily_history.append("_angry")


    $ EmmaX.ArmPose = 1
    if "no_dildo" in EmmaX.daily_history:
        ch_e "Learn to take \"no\" for an answer, [EmmaX.player_petname]."
        $ EmmaX.recent_history.append("_angry")
        $ EmmaX.daily_history.append("_angry")
    elif EmmaX.Forced:
        $ EmmaX.change_face("_angry", 1)
        ch_e "I'm not going to let you use that on me."
        $ EmmaX.change_stat("lust", 200, 5)
        if EmmaX.love > 300:
            $ EmmaX.change_stat("love", 70, -2)
        $ EmmaX.change_stat("obedience", 50, -2)
        $ EmmaX.recent_history.append("_angry")
        $ EmmaX.daily_history.append("_angry")
    elif Taboo:
        $ EmmaX.change_face("_angry", 1)
        $ EmmaX.recent_history.append("no_taboo")
        $ EmmaX.daily_history.append("no_taboo")
        ch_e "Not here!"
        $ EmmaX.change_stat("lust", 200, 5)
        $ EmmaX.change_stat("obedience", 50, -3)
    elif EmmaX.action_counter["dildo_ass"]:
        $ EmmaX.change_face("_sad")
        ch_e "Sorry, you can keep your toys out of there."
    else:
        $ EmmaX.change_face("_normal", 1)
        ch_e "No, thank you."
    $ EmmaX.recent_history.append("no_dildo")
    $ EmmaX.daily_history.append("no_dildo")
    $ approval_bonus = 0
    return

label Emma_DA_Prep:
    if offhand_action == "dildo_anal":
        return

    if not EmmaX.Forced and action_context != "auto":
        $ approval_bonus = 20 if EmmaX.PantsNum() > 6 else 0
        call Bottoms_Off (EmmaX)
        if "_angry" in EmmaX.recent_history:
            return

    $ approval_bonus = 0
    call Emma_Pussy_Launch ("dildo_anal")
    if not EmmaX.action_counter["dildo_ass"]:
        if EmmaX.Forced:
            $ EmmaX.change_stat("love", 90, -75)
            $ EmmaX.change_stat("obedience", 70, 60)
            $ EmmaX.change_stat("inhibition", 80, 35)
        else:
            $ EmmaX.change_stat("love", 90, 10)
            $ EmmaX.change_stat("obedience", 70, 20)
            $ EmmaX.change_stat("inhibition", 80, 45)
    if Taboo:
        $ EmmaX.inhibition += int(Taboo/10)
        $ EmmaX.lust += int(Taboo/5)


    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ EmmaX.drain_word("no_taboo")
    $ EmmaX.drain_word("no_dildo")
    $ EmmaX.recent_history.append("dildo_anal")
    $ EmmaX.daily_history.append("dildo_anal")

label Emma_DA_Cycle:
    while Round > 0:
        call shift_focus (EmmaX)
        call Emma_Pussy_Launch ("dildo_anal")
        $ EmmaX.lust_face()

        if Player.focus < 100:

            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":

                    call Slap_Ass (EmmaX)
                    jump Emma_DA_Cycle

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
                            if EmmaX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ EmmaX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (EmmaX, "tired")
                        "Shift primary action":

                            if EmmaX.remaining_actions and multi_action:
                                menu:
                                    "I want to stick a finger in her pussy.":
                                        $ action_context = "shift"
                                        call Emma_DA_After
                                        call Emma_Fondle_Pussy
                                    "Just stick a finger in her pussy without asking.":
                                        $ action_context = "auto"
                                        call Emma_DA_After
                                        call Emma_Fondle_Pussy
                                    "I want to shift the dildo to her pussy.":
                                        $ action_context = "shift"
                                        call Emma_DA_After
                                        call Emma_Dildo_Pussy
                                    "Never Mind":
                                        jump Emma_DA_Cycle
                            else:
                                call Sex_Basic_Dialog (EmmaX, "tired")

                        "Shift your focus" if offhand_action:
                            $ action_context = "shift focus"
                            call Emma_DA_After
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
                                    jump Emma_DA_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Emma_DA_Cycle
                                "Never mind":
                                    jump Emma_DA_Cycle
                        "Undress [EmmaX.name]":
                            call Girl_Undress (EmmaX)
                        "Clean up [EmmaX.name] (locked)" if not EmmaX.spunk:
                            pass
                        "Clean up [EmmaX.name]" if EmmaX.spunk:
                            call Girl_Cleanup (EmmaX, "ask")
                        "Never mind":
                            jump Emma_DA_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Emma_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Emma_DA_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Emma_Pos_Reset
                    $ Line = 0
                    jump Emma_DA_After


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
                if "_angry" in EmmaX.recent_history:
                    call Emma_Pos_Reset
                    return
                $ EmmaX.change_stat("lust", 200, 5)
                if 100 > EmmaX.lust >= 70 and EmmaX.session_orgasms < 2:
                    $ EmmaX.recent_history.append("unsatisfied")
                    $ EmmaX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Emma_DA_After
                $ Line = "came"

            if EmmaX.lust >= 100:

                call Girl_Cumming (EmmaX)
                if action_context == "shift" or "_angry" in EmmaX.recent_history:
                    jump Emma_DA_After

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
                            jump Emma_DA_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if EmmaX.SEXP >= 100 or approval_check(EmmaX, 1200, "LO"):
            pass
        elif counter == (5 + EmmaX.action_counter["dildo_ass"]):
            $ EmmaX.brows = "_confused"
            ch_e "What are you even doing down there?"
        elif EmmaX.lust >= 80:
            pass
        elif counter == (15 + EmmaX.action_counter["dildo_ass"]) and EmmaX.SEXP >= 15 and not approval_check(EmmaX, 1500):
            $ EmmaX.brows = "_confused"
            menu:
                ch_e "[EmmaX.player_petname], this is getting uncomfortable, maybe we could try something else."
                "Finish up.":
                    "You let go. . ."
                    jump Emma_DA_After
                "Let's try something else." if multi_action:
                    $ Line = 0
                    $ action_context = "shift"
                    jump Emma_DA_After
                "No, this is fun.":
                    if approval_check(EmmaX, 1200) or approval_check(EmmaX, 500, "O"):
                        $ EmmaX.change_stat("love", 200, -5)
                        $ EmmaX.change_stat("obedience", 50, 3)
                        $ EmmaX.change_stat("obedience", 80, 2)
                        "She grumbles but lets you keep going."
                    else:
                        $ EmmaX.change_face("_angry", 1)
                        call Emma_Pos_Reset
                        "She scowls at you and pulls back."
                        ch_e "Well if that's your attitude, I don't need your \"help\"."
                        $ EmmaX.change_stat("love", 50, -3, 1)
                        $ EmmaX.change_stat("love", 80, -4, 1)
                        $ EmmaX.change_stat("obedience", 30, -1, 1)
                        $ EmmaX.change_stat("obedience", 50, -1, 1)
                        $ EmmaX.recent_history.append("_angry")
                        $ EmmaX.daily_history.append("_angry")
                        jump Emma_DA_After


        if Round == 10:
            ch_e "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."


    $ EmmaX.change_face("_bemused", 0)
    $ Line = 0
    ch_e "Ok, [EmmaX.player_petname], that's enough of that for now."


label Emma_DA_After:
    if not action_context:
        call Emma_Pos_Reset

    $ EmmaX.change_face("_sexy")

    $ EmmaX.action_counter["dildo_ass"] += 1
    $ EmmaX.remaining_actions -=1

    call Partner_Like (EmmaX, 1)

    if EmmaX.action_counter["dildo_ass"] == 1:
        $ EmmaX.SEXP += 10
        if not action_context:
            if EmmaX.love >= 500 and "unsatisfied" not in EmmaX.recent_history:
                ch_e "That was. . . engaging. . ."
            elif EmmaX.obedience <= 500 and Player.focus <= 20:
                $ EmmaX.change_face("_perplexed", 1)
                ch_e "Did you enjoy that?"

    $ approval_bonus = 0


    call checkout
    return



label Emma_Vibrator_Check:
    if "_vibrator" in Player.inventory:
        "You pull out the \"shocker\" vibrator, handy."
    elif "_vibrator" in EmmaX.inventory:
        "You ask [EmmaX.name] to get out her vibrator."
    else:
        "You don't have one of those on you."
        return 0
    return 1


label Emma_Footjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (EmmaX)
    if EmmaX.action_counter["footjob"] >= 7:
        $ approval_bonus += 10
    elif EmmaX.action_counter["footjob"] >= 3:
        $ approval_bonus += 7
    elif EmmaX.action_counter["footjob"]:
        $ approval_bonus += 3

    if EmmaX.addiction >= 75 and EmmaX.event_counter["swallowed"] >=3:
        $ approval_bonus += 10
    if EmmaX.addiction >= 75:
        $ approval_bonus += 5

    if action_context == "shift":
        $ approval_bonus += 15
    if "exhibitionist" in EmmaX.traits:
        $ approval_bonus += (3*Taboo)
    if EmmaX in Player.Harem or "sex friend" in EmmaX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in EmmaX.traits:
        $ approval_bonus -= 40
    if EmmaX.event_counter["forced"] and not EmmaX.Forced:
        $ approval_bonus -= 5*EmmaX.event_counter["forced"]

    if Taboo and "no_taboo" in EmmaX.daily_history:
        $ approval_bonus -= 10

    if "no_foot" in EmmaX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_foot" in EmmaX.recent_history else 0

    $ approval = approval_check(EmmaX, 1250, TabM = 3)

    if action_context == EmmaX:
        if approval > 2:
            if offhand_action == "jackin":
                "[EmmaX.name] sits back and starts rubbing her foot along your cock."
            else:
                "[EmmaX.name] gives you a mischevious smile, and starts to rub her foot along your cock."
            menu:
                "What do you do?"
                "Nothing.":
                    $ EmmaX.change_stat("inhibition", 70, 3)
                    $ EmmaX.change_stat("inhibition", 30, 2)
                    "[EmmaX.name] continues her actions."
                "Praise her.":
                    $ EmmaX.change_face("_sexy", 1)
                    $ EmmaX.change_stat("inhibition", 70, 3)
                    ch_p "Oooh, that's good, [EmmaX.petname]."
                    $ EmmaX.nameCheck()
                    "[EmmaX.name] continues her actions."
                    $ EmmaX.change_stat("love", 80, 1)
                    $ EmmaX.change_stat("obedience", 90, 1)
                    $ EmmaX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ EmmaX.change_face("_surprised")
                    $ EmmaX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that for now, [EmmaX.petname]."
                    $ EmmaX.nameCheck()
                    "[EmmaX.name] puts it down."
                    $ EmmaX.change_stat("obedience", 90, 1)
                    $ EmmaX.change_stat("obedience", 50, 1)
                    $ EmmaX.change_stat("obedience", 30, 2)
                    return
            if primary_action:
                $ girl_offhand_action = "footjob"
                return
            jump Emma_FJ_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
            return

    if not EmmaX.action_counter["footjob"] and "no_foot" not in EmmaX.recent_history:
        $ EmmaX.change_face("_confused", 2)
        ch_e "Mmm, so you're into feet then, [EmmaX.player_petname]?"
        $ EmmaX.blushing = "_blush1"

    if not EmmaX.action_counter["footjob"] and approval:
        if EmmaX.Forced:
            $ EmmaX.change_face("_sad",1)
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
        elif EmmaX.love >= (EmmaX.obedience + EmmaX.inhibition):
            $ EmmaX.change_face("_sexy",1)
            $ EmmaX.brows = "_sad"
            $ EmmaX.mouth = "_smile"
            ch_e "I suppose it couldn't hurt. . ."
        elif EmmaX.obedience >= EmmaX.inhibition:
            $ EmmaX.change_face("_normal",1)
            ch_e "If you enjoy that, [EmmaX.player_petname]. . ."
        elif EmmaX.addiction >= 50:
            $ EmmaX.change_face("_manic", 1)
            ch_e "Very well. . ."
        else:
            $ EmmaX.change_face("_lipbite",1)
            ch_e "Very well. . ."

    elif approval:
        if EmmaX.Forced:
            $ EmmaX.change_face("_sad")
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
            ch_e "That's it?"
        elif not Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "Um, I suppose this is secluded enough. . ."
        elif "footjob" in EmmaX.recent_history:
            $ EmmaX.change_face("_sexy", 1)
            ch_e "You know, heels are nightmare on the arches. . ."
            jump Emma_FJ_Prep
        elif "footjob" in EmmaX.daily_history:
            $ EmmaX.change_face("_sexy", 1)
            $ Line = renpy.random.choice(["Another?",   
                "I'd rather not get calluses.", 
                "Didn't get enough earlier?",
                "My feet are rather sore from earlier.",
                "My feet are rather sore from earlier."])
            ch_e "[Line]"
        elif EmmaX.action_counter["footjob"] < 3:
            $ EmmaX.change_face("_sexy", 1)
            $ EmmaX.brows = "_confused"
            $ EmmaX.mouth = "_kiss"
            ch_e "Oh, very well. . ."
        else:
            $ EmmaX.change_face("_sexy", 1)
            $ EmmaX.ArmPose = 2
            $ Line = renpy.random.choice(["You'd like me to use my feet again?",                 
                "So you'd like another footjob?",                 
                "Mmmm, some. . . [she rubs her foot along your leg]?", 
                "A little foot rub?"])
            ch_e "[Line]"
        $ Line = 0

    if approval >= 2:
        if EmmaX.Forced:
            $ EmmaX.change_face("_sad")
            $ EmmaX.change_stat("obedience", 90, 1)
            $ EmmaX.change_stat("inhibition", 60, 1)
            ch_e "Oh, fine."
        elif "no_foot" in EmmaX.daily_history:
            ch_e "Oh, very well."
        else:
            $ EmmaX.change_face("_sexy", 1)
            $ EmmaX.change_stat("love", 90, 1)
            $ EmmaX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Sure, I suppose.",                 
                "Fine.",                 
                "Very well, bring it out.", 
                "I suppose I could. . .",
                "Fine. . . [She gestures for you to come over].",
                "Hmm, ok."])
            ch_e "[Line]"
            $ Line = 0
        $ EmmaX.change_stat("obedience", 20, 1)
        $ EmmaX.change_stat("obedience", 60, 1)
        $ EmmaX.change_stat("inhibition", 70, 2)
        jump Emma_FJ_Prep
    else:

        $ EmmaX.change_face("_angry")
        if "no_foot" in EmmaX.recent_history:
            ch_e "Pay attention, [EmmaX.player_petname]."
        elif Taboo and "no_taboo" in EmmaX.daily_history and "no_foot" in EmmaX.daily_history:
            ch_e "I refuse to do this in public."
        elif "no_foot" in EmmaX.daily_history:
            ch_e "I said \"no,\" [EmmaX.player_petname]."
        elif Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "I told you, not in public!"
        elif not EmmaX.action_counter["footjob"]:
            $ EmmaX.change_face("_bemused")
            ch_e "I'm unsure, [EmmaX.player_petname]. . ."
        else:
            $ EmmaX.change_face("_bemused")
            ch_e "Not now, [EmmaX.player_petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_foot" in EmmaX.daily_history:
                $ EmmaX.change_face("_bemused")
                ch_e "Thank you."
                return
            "Maybe later?" if "no_foot" not in EmmaX.daily_history:
                $ EmmaX.change_face("_sexy")
                ch_e ". . ."
                ch_e "Perhaps."
                $ EmmaX.change_stat("love", 80, 2)
                $ EmmaX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ EmmaX.recent_history.append("no_taboo")
                    $ EmmaX.daily_history.append("no_taboo")
                $ EmmaX.recent_history.append("no_foot")
                $ EmmaX.daily_history.append("no_foot")
                return
            "I'd really appreciate it. . .":
                if approval:
                    $ EmmaX.change_face("_sexy")
                    $ EmmaX.change_stat("obedience", 90, 2)
                    $ EmmaX.change_stat("obedience", 50, 2)
                    $ EmmaX.change_stat("inhibition", 70, 3)
                    $ EmmaX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Sure, I suppose.",                 
                            "Fine.",                 
                            "Very well, bring it out.", 
                            "I suppose I could. . .",
                            "Fine. . . [She gestures for you to come over].",
                            "Hmm, ok."])
                    ch_e "[Line]"
                    $ Line = 0
                    jump Emma_FJ_Prep
                else:
                    pass
            "Come on, get to work.":

                $ approval = approval_check(EmmaX, 400, "OI", TabM = 3)
                if approval > 1 or (approval and EmmaX.Forced):
                    $ EmmaX.change_face("_sad")
                    $ EmmaX.change_stat("love", 70, -5, 1)
                    $ EmmaX.change_stat("love", 200, -2)
                    ch_e "Oh, very well."
                    $ EmmaX.change_stat("obedience", 50, 4)
                    $ EmmaX.change_stat("inhibition", 80, 1)
                    $ EmmaX.change_stat("inhibition", 60, 3)
                    $ EmmaX.Forced = 1
                    jump Emma_FJ_Prep
                else:
                    $ EmmaX.change_stat("love", 200, -15)
                    $ EmmaX.recent_history.append("_angry")
                    $ EmmaX.daily_history.append("_angry")


    $ EmmaX.ArmPose = 1
    if "no_foot" in EmmaX.daily_history:
        $ EmmaX.change_face("_angry", 1)
        ch_e "I won't repeat myself."
        $ EmmaX.recent_history.append("_angry")
        $ EmmaX.daily_history.append("_angry")
    elif EmmaX.Forced:
        $ EmmaX.change_face("_angry", 1)
        ch_e "You really don't want my heels near your manhood."
        $ EmmaX.change_stat("lust", 200, 5)
        if EmmaX.love > 300:
            $ EmmaX.change_stat("love", 70, -2)
        $ EmmaX.change_stat("obedience", 50, -2)
        $ EmmaX.recent_history.append("_angry")
        $ EmmaX.daily_history.append("_angry")
    elif Taboo:
        $ EmmaX.change_face("_angry", 1)
        $ EmmaX.daily_history.append("no_taboo")
        ch_e "This truly isn't an appropriate place for that."
        $ EmmaX.change_stat("lust", 200, 5)
        $ EmmaX.change_stat("obedience", 50, -3)
    elif EmmaX.action_counter["footjob"]:
        $ EmmaX.change_face("_sad")
        ch_e "I'm not in the mood, [EmmaX.player_petname]. . ."
    else:
        $ EmmaX.change_face("_normal", 1)
        ch_e "I'm not in the mood for footplay today. . ."
    $ EmmaX.recent_history.append("no_foot")
    $ EmmaX.daily_history.append("no_foot")
    $ approval_bonus = 0
    return


label Emma_FJ_Prep:
    if offhand_action == "footjob":
        return

    if Taboo:
        $ EmmaX.inhibition += int(Taboo/10)
        $ EmmaX.lust += int(Taboo/5)

    $ EmmaX.change_face("_sexy")
    if EmmaX.Forced:
        $ EmmaX.change_face("_sad")
    elif not EmmaX.action_counter["footjob"]:
        $ EmmaX.brows = "_confused"
        $ EmmaX.eyes = "_sexy"
        $ EmmaX.mouth = "_smile"

    call Seen_First_Peen (EmmaX, Partner, React=action_context)
    if not EmmaX.action_counter["footjob"]:
        if EmmaX.Forced:
            $ EmmaX.change_stat("love", 90, -20)
            $ EmmaX.change_stat("obedience", 70, 25)
            $ EmmaX.change_stat("inhibition", 80, 30)
        else:
            $ EmmaX.change_stat("love", 90, 5)
            $ EmmaX.change_stat("obedience", 70, 20)
            $ EmmaX.change_stat("inhibition", 80, 20)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    if Taboo:
        $ EmmaX.drain_word("no_taboo")
    $ EmmaX.drain_word("no_foot")
    $ EmmaX.recent_history.append("footjob")
    $ EmmaX.daily_history.append("footjob")
    ch_e "Did you want me facing you, or from behind?"
    menu:
        extend ""
        "Facing me":
            $ EmmaX.pose = "footjob"
        "From behind.":
            $ EmmaX.pose = "doggy"

label Emma_FJ_Cycle:
    while Round > 0:
        call shift_focus (EmmaX)
        call Emma_FJ_Launch
        $ EmmaX.lust_face()

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
                "Turn her Around":

                    $ EmmaX.pose = "doggy" if EmmaX.pose != "doggy" else "footjob"
                    "You turn her around. . ."
                    jump Emma_FJ_Cycle


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
                        "I also want to fondle her thighs." if offhand_action != "fondle_thighs":
                            if multi_action:
                                $ offhand_action = "fondle_thighs"
                                "You start to fondle her thighs."
                            else:
                                call Sex_Basic_Dialog (EmmaX, "tired")
                        "Shift primary action":

                            if EmmaX.remaining_actions and multi_action:
                                menu:
                                    "How about a blowjob?":
                                        if EmmaX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Emma_FJ_After
                                            call Emma_Blowjob
                                        else:
                                            call Sex_Basic_Dialog (EmmaX, "tired")
                                    "How about a handjob?":
                                        if EmmaX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Emma_FJ_After
                                            call Emma_Handjob
                                        else:
                                            call Sex_Basic_Dialog (EmmaX, "tired")
                                    "How about a titjob?":

                                        if EmmaX.remaining_actions and multi_action:
                                            $ action_context = "shift"
                                            call Emma_FJ_After
                                            call Emma_Titjob
                                        else:
                                            call Sex_Basic_Dialog (EmmaX, "tired")
                                    "Never Mind":

                                        jump Emma_FJ_Cycle
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
                                    jump Emma_FJ_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Emma_FJ_Cycle
                                "Never mind":
                                    jump Emma_FJ_Cycle
                        "Undress [EmmaX.name]":
                            call Girl_Undress (EmmaX)
                        "Clean up [EmmaX.name] (locked)" if not EmmaX.spunk:
                            pass
                        "Clean up [EmmaX.name]" if EmmaX.spunk:
                            call Girl_Cleanup (EmmaX, "ask")
                        "Never mind":
                            jump Emma_FJ_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Emma_FJ_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Emma_FJ_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Emma_FJ_Reset
                    $ Line = 0
                    jump Emma_FJ_After


        call shift_focus (EmmaX)
        call Sex_Dialog (EmmaX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or EmmaX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (EmmaX)
                if "_angry" in EmmaX.recent_history:
                    call Emma_FJ_Reset
                    return
                $ EmmaX.change_stat("lust", 200, 5)
                if 100 > EmmaX.lust >= 70 and EmmaX.session_orgasms < 2:
                    $ EmmaX.recent_history.append("unsatisfied")
                    $ EmmaX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Emma_FJ_After
                $ Line = "came"

            if EmmaX.lust >= 100:

                call Girl_Cumming (EmmaX)
                if action_context == "shift" or "_angry" in EmmaX.recent_history:
                    jump Emma_FJ_After

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
                            jump Emma_FJ_After
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 10 if Player.focusing and Player.focus > 50 else 0

        if counter == 20:
            $ EmmaX.brows = "_angry"
            menu:
                ch_e "Hmm, foot cramp, could we take a short break?"
                "How about a BJ?" if EmmaX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Emma_FJ_After
                    call Emma_Blowjob
                "How about a Handy?" if EmmaX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Emma_FJ_After
                    call Emma_Handjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    $ counter += 1
                    "[Line]"
                    jump Emma_FJ_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Emma_Sex_Reset
                    $ action_context = "shift"
                    jump Emma_FJ_After
                "No, keep going.":
                    if approval_check(EmmaX, 1200) or approval_check(EmmaX, 500, "O"):
                        $ EmmaX.change_stat("love", 200, -5)
                        $ EmmaX.change_stat("obedience", 50, 3)
                        $ EmmaX.change_stat("obedience", 80, 2)
                        "She grumbles but gets back to work."
                    else:
                        $ EmmaX.change_face("_angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        ch_e "I do have better things I could be doing."
                        $ EmmaX.change_stat("love", 50, -3, 1)
                        $ EmmaX.change_stat("love", 80, -4, 1)
                        $ EmmaX.change_stat("obedience", 30, -1, 1)
                        $ EmmaX.change_stat("obedience", 50, -1, 1)
                        $ EmmaX.recent_history.append("_angry")
                        $ EmmaX.daily_history.append("_angry")
                        jump Emma_FJ_After
        elif counter == 10 and EmmaX.SEXP <= 100 and not approval_check(EmmaX, 1200, "LO"):
            $ EmmaX.brows = "_confused"
            ch_e "Could we be done here, my feet are getting sore."


        call Escalation (EmmaX)

        if Round == 10:
            ch_e "Ok, it's getting a bit late here."
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."


    $ EmmaX.change_face("_bemused", 0)
    $ Line = 0
    ch_e "Ok, [EmmaX.player_petname], that's enough of that for now."

label Emma_FJ_After:
    $ EmmaX.change_face("_sexy")

    $ EmmaX.action_counter["footjob"] += 1
    $ EmmaX.remaining_actions -=1
    $ EmmaX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ EmmaX.addiction_rate += 1
    $ EmmaX.change_stat("lust", 90, 5)

    call Partner_Like (EmmaX, 1)

    if "Emmapedi" in Achievements:
        pass
    elif EmmaX.action_counter["footjob"] >= 10:
        $ EmmaX.change_face("_smile", 1)
        ch_e "I'm glad that you enjoy my feet."
        ch_e "They've been trained well over the years."
        $ Achievements.append("Emmapedi")
        $ EmmaX.SEXP += 5
    elif EmmaX.action_counter["footjob"] == 1:
        $ EmmaX.SEXP += 10
        if EmmaX.love >= 500:
            $ EmmaX.mouth = "_smile"
            ch_e "Your cock was so warm . ."
        elif Player.focus <= 20:
            $ EmmaX.mouth = "_sad"
            ch_e "Did you enjoy that?"
    elif EmmaX.action_counter["footjob"] == 5:
        ch_e "I'm enjoying this experience."

    $ approval_bonus = 0
    if action_context == "shift":
        ch_e "Ok then, what were you thinking?"
    else:
        call Emma_Sex_Reset
    call checkout
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
