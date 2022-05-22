label Rogue_SexAct(Act=0):
    if AloneCheck(Girl) and Girl.Taboo == 20:
        $ Girl.Taboo = 0
        $ Taboo = 0
    call shift_focus (Girl)
    if Act == "SkipTo":
        $ renpy.pop_call()
        $ renpy.pop_call()

        call SkipTo (Girl)
    elif Act == "switch":
        $ renpy.pop_call()


    elif Act == "masturbate":
        call Rogue_M_Prep
        if not action_context:
            return
    elif Act == "lesbian":
        call Les_Prep (Girl)
        if not action_context:
            return
    elif Act == "kiss":
        call KissPrep (Girl)
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
    $ round -= 5 if round > 5 else (round-1)
    call shift_focus(Girl)
    call set_approval_bonus(Girl, primary_action)
    call action_approval_checks(Girl, primary_action)

    $ Girl.drain_word("unseen",1,0)

    if action_context == "join":
        if approval > 1 or (approval and Girl.lust >= 50):
            $ Player.add_word(1,"join")
            menu:
                extend ""
                "Would you like some help? I could lend some helping hands. . ." if Player.semen and Girl.remaining_actions:
                    $ Girl.change_stat("love", 90, 1)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_face("_sexy")

                    call lend_some_helping_hands_lines(Girl, primary_action)

                    $ Girl.change_stat("obedience", 70, 2)
                    $ Girl.change_stat("inhibition", 70, 1)
                    $ offhand_action = "fondle_breasts"
                    $ Girl.action_counter["masturbation"] += 1
                    jump Rogue_M_Cycle
                "Would you like some help? I could. . . up to you, I guess." if Player.semen and Girl.remaining_actions:
                    $ Girl.change_stat("love", 70, 2)
                    $ Girl.change_stat("love", 90, 1)
                    $ Girl.change_face("_sexy")

                    call lend_some_helping_hands_lines(Girl, primary_action)

                    $ Girl.change_stat("obedience", 70, 2)
                    $ Girl.change_stat("inhibition", 70, 1)
                    $ D20 = renpy.random.randint(1, 20)
                    if D20 > 10:
                        $ offhand_action = "fondle_breasts"
                    else:
                        $ offhand_action = "suck_breasts"
                    $ Girl.action_counter["masturbation"] += 1
                    jump Rogue_M_Cycle
                "Why don't we take care of each other?" if Player.semen and Girl.remaining_actions:
                    $ Girl.change_face("_sexy")

                    call why_dont_we_take_care_of_each_other_lines(Girl, primary_action)

                    $ renpy.pop_call()
                    return
                "You look like you have things well in hand. . .":
                    if Girl.lust >= 50:
                        $ Girl.change_stat("love", 70, 2)
                        $ Girl.change_stat("love", 90, 1)
                        $ Girl.change_face("_sexy")

                        call well_in_hand_lust_lines(Girl, primary_action)

                        $ Girl.change_stat("obedience", 80, 3)
                        $ Girl.change_stat("inhibition", 80, 5)
                        jump Rogue_M_Cycle
                    elif approval_check(Girl, 1000):
                        $ Girl.change_face("_sly")

                        call well_in_hand_approved_lines(Girl, primary_action)
                    else:
                        $ Girl.change_face("_angry")

                        call well_in_hand_disapproved_lines(Girl, primary_action)

        $ Girl.ArmPose = 1
        $ Girl.change_outfit(Changed=0)
        $ Girl.remaining_actions -= 1
        $ Player.change_stat("focus", 50, 30)
        call checkout (1)
        $ Line = 0
        $ action_context = None
        $ renpy.pop_call()
        if approval:
            $ Girl.change_face("_bemused", 2)
            if bg_current == "bg_rogue":
                call what_did_you_come_over_for_approval_lines(Girl, primary_action)
            else:
                call fancy_bumping_into_you_approval_lines(Girl, primary_action)

            $ Girl.blushing = "_blush1"
        else:
            $ Girl.change_stat("love", 200, -5)
            $ Girl.change_face("_angry")
            $ Girl.recent_history.append("_angry")
            $ Girl.daily_history.append("_angry")
            if bg_current == "bg_rogue":
                call what_did_you_come_over_for_disapproval_lines(Girl, primary_action)

                $ renpy.pop_call()

                jump Campus_Map
            else:
                call fancy_bumping_into_you_disapproval_lines(Girl, primary_action)
                call remove_girl (Girl)
        return




    if action_context == Girl:
        if approval > 2:
            if Girl.PantsNum() == 5:
                "[Girl.name]'s hand snakes down her body, and hikes up her skirt."
                $ Girl.upskirt = 1
            elif Girl.PantsNum() > 6:
                "[Girl.name] slides her hand down her body and into her jeans."
            elif Girl.HoseNum() >= 5:
                "[Girl.name]'s hand slides down her body and under her [Girl.hose]."
            elif Girl.underwear:
                "[Girl.name]'s hand slides down her body and under her [Girl.underwear]."
            else:
                "[Girl.name]'s hand slides down her body and begins to caress her pussy."
            $ Girl.SeenPanties = 1
            "She starts to slowly rub herself."
            call Rogue_First_Bottomless
            menu:
                "What do you do?"
                "Nothing.":
                    $ Girl.change_stat("inhibition", 80, 3)
                    $ Girl.change_stat("inhibition", 60, 2)
                    "[Girl.name] begins to masturbate."
                "Go for it.":
                    $ Girl.change_face("sexy, 1")
                    $ Girl.change_stat("inhibition", 80, 3)
                    ch_p "That is so sexy, [Girl.petname]."
                    $ Girl.nameCheck()
                    "You lean back and enjoy the show."
                    $ Girl.change_stat("love", 80, 1)
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ Girl.change_face("_surprised")
                    $ Girl.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that right now, [Girl.petname]."
                    $ Girl.nameCheck()
                    "[Girl.name] pulls her hands away from herself."
                    $ Girl.change_outfit(Changed=0)
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Girl.change_stat("obedience", 30, 2)
                    return
            jump Rogue_M_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
        return



    if not Girl.action_counter["masturbation"]:
        call first_time_asking_reactions(Girl, primary_action)

        $ Girl.change_face("_surprised", 1)
        $ Girl.mouth = "_kiss"
        if Girl.forced:
            $ Girl.change_face("_sad")

            call action_forcefully_approved_lines(Girl, primary_action)

    if not Girl.action_counter["masturbation"] and approval:
        call first_action_approval(Girl, primary_action)

        if Girl.forced:
            $ Girl.change_face("_sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
        elif Girl.love >= (Girl.obedience + Girl.inhibition):
            $ Girl.change_face("_sexy")
            $ Girl.brows = "_sad"
            $ Girl.mouth = "_smile"

            call first_action_approval_mostly_love_lines(Girl, primary_action)
        elif Girl.obedience >= Girl.inhibition:
            $ Girl.change_face("_normal")

            call first_action_approval_mostly_obedience_lines(Girl, primary_action)
        else:
            $ Girl.change_face("_sad")
            $ Girl.mouth = "_smile"

            call first_action_approval_lines(Girl, primary_action)
    elif approval:
        call action_approved(Girl, primary_action)

        if Girl.forced:
            $ Girl.change_face("_sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)

            ch_r "You want to watch me again?"
            ch_k "Again? Just looking?"
            ch_e "Again? Just you only want to watch?"
            ch_l "Hmm, again?"
            ch_j "Hmm, again?"
            ch_s "You only like to watch?"
            ch_v "Hmm, again?"
        elif approval and "masturbation" in Girl.recent_history:
            $ Girl.change_face("_sexy", 1)

            call recent_action_lines(Girl, primary_action)
            jump Rogue_M_Prep
        elif approval and "masturbation" in Girl.daily_history:
            $ Girl.change_face("_sexy", 1)

            call daily_action_lines(Girl, primary_action)
        elif Girl.action_counter["masturbation"] < 3:
            $ Girl.change_face("_sexy", 1)
            $ Girl.brows = "_confused"

            cacll before_action_less_than_three_times_lines(Girl, primary_action)
        else:
            $ Girl.change_face("_sexy", 1)
            $ Girl.ArmPose = 2
            $ Line = renpy.random.choice(["You sure do like to watch.",
                    "So you'd like me to go again?",
                    "You want to watch some more?",
                    "You want me ta diddle myself?"])
            ch_r "[Line]"
            $ Line = renpy.random.choice(["You really like to watch.",
                    "Again?",
                    "You like to watch me.",
                    "You want me to get myself off?"])
            ch_k "[Line]"
            $ Line = renpy.random.choice(["You really do like to watch.",
                    "Once more?",
                    "You enjoy watching me.",
                    "You want me to take care of myself?"])
            ch_e "[Line]"
            $ Line = renpy.random.choice(["You like to watch.",
                    "Again?",
                    "You really like to watch me.",
                    "You want me to masturbate again?"])
            ch_l "[Line]"
            $ Line = renpy.random.choice(["You do like to watch.",
                    "Again?",
                    "You like to watch me.",
                    "You'd like me to masturbate again?"])
            ch_j "[Line]"
            $ Line = renpy.random.choice(["You really do like to watch.",
                    "Once more?",
                    "You enjoy watching me do that?",
                    "You want me to take care of myself?"])
            ch_s "[Line]"
            $ Line = renpy.random.choice(["You do enjoy watching.",
                    "Again?",
                    "You really enjoy watching me.",
                    "You want me to shlick again?"])
            ch_v "[Line]"
            $ Line = 0



    if approval >= 2:
        call action_accepted(Girl, primary_action)
        label begging_approved:

        if Girl.forced:
            $ Girl.change_face("_sad")
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 60, 1)

            ch_r "I suppose, let me get comfortable. . ."
            ch_k "Fine. . ."
            ch_e "Fine. . ."
            ch_l "Whatever. . ."
            ch_j "Oh. . . fine. . ."
            ch_s ". . .Fine"
            ch_v "Whatevs. . ."
        else:
            $ Girl.change_face("_sexy", 1)
            $ Girl.change_stat("love", 90, 1)
            $ Girl.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well. . . ok.",
                    "I suppose it would help to have something nice to look at. . .",
                    "I've kind of needed this anyways. . .",
                    "Sure!",
                    "I guess I could. . . give it a go.",
                    "Heh, ok, ok."])
            ch_r "[Line]"
            $ Line = renpy.random.choice(["Huh. Ok.",
                    "Couldn't hurt having you around. . .",
                    "Two birds with one stone. . .",
                    "K.",
                    "Sure, why not?",
                    "Lol, ok."])
            ch_k "[Line]"
            $ Line = renpy.random.choice(["Ok.",
                    "It couldn't hurt having you around. . .",
                    "Very well.",
                    "Sure, why not?",
                    "[[chuckles]. . . ok."])
            ch_e "[Line]"
            $ Line = renpy.random.choice(["Huh. Ok.",
                    "Couldn't hurt. . .",
                    "Alright.",
                    "Sure.",
                    "Heh, ok."])
            ch_l "[Line]"
            $ Line = renpy.random.choice(["Sure. Ok.",
                    "Couldn't hurt. . .",
                    "All right.",
                    "Sure.",
                    "Sure, why not. . ."])
            ch_j "[Line]"
            $ Line = renpy.random.choice(["Fine.",
                    "It could not hurt having you around. . .",
                    "Very well.",
                    "Sure, why not?",
                    "[[chuckles]. . . Fine."])
            ch_s "[Line]"
            $ Line = renpy.random.choice(["Huh. Ok.",
                    "Couldn't hurt. . .",
                    "Allright.",
                    "Sure.",
                    "Heh, ok."])
            ch_v "[Line]"
            $ Line = 0

        $ Girl.change_stat("obedience", 20, 1)
        $ Girl.change_stat("obedience", 60, 1)
        $ Girl.change_stat("inhibition", 70, 2)
        jump Rogue_M_Prep
    else:
        call action_disapproved(Girl, primary_action)
        ch_r "That's. . . a little intimate, [RogueX.player_petname]."
        ch_k "That's. . . private? You know?"
        ch_e "I don't know that I want to perform."
        ch_l "I don't know that I want to do that right now."
        ch_j "I don't know, it's kind of a bad time. . ."
        ch_s "I am unsure about this."
        ch_v "I don't know, I'm not really into it right now."

        menu:
            "Maybe later?":
                $ Girl.change_face("_sexy", 1)
                if Girl.lust > 50:
                    ch_r "Well, definitely later. . . but I'll have to think about inviting you."
                    ch_k "Well, I know what {i}I'll{/i} be doing later. Not sure if you can come.{p}I mean- you know, be there.{p}I'm not sure you'll {i}be{/i} there.{p}. . .coming."

                    ch_e "I have plans for. . . later, but perhaps you could take part."
                    ch_l "I probably will be, but not with an audience."
                    ch_j "Well -I- will, but after you leave."
                    ch_s "I expect that I will be finished by then. . ."
                    ch_v "Maybe, just not with so many eyes on me. . ."
                else:
                    ch_r "Hmm, maybe. . . I'll let you know."
                    ch_k "Hmm, maybe. . . I'll text you?"
                    ch_e "I couldn't say."
                    ch_l "Hmm, maybe. . ."
                    ch_j "Well. . . maybe. . ."
                    ch_s "We shall see."
                    ch_v "Hmm, maaaybe. . ."
                $ Girl.change_stat("love", 80, 2)
                $ Girl.change_stat("inhibition", 70, 2)
                return
            "You look like you could use it. . .":
                if approval:
                    $ Girl.change_face("_sexy")
                    $ Girl.change_stat("obedience", 90, 2)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("inhibition", 70, 3)
                    $ Girl.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Well. . . ok.",
                            "I suppose it would help to have something nice to look at. . .",
                            "I've kind of needed this anyways. . .",
                            "Sure!",
                            "I guess I could. . . give it a go.",
                            "Heh, ok, ok."])
                    ch_r "[Line]"
                    $ Line = renpy.random.choice(["Huh. Ok.",
                                "Couldn't hurt having you around. . .",
                                "Two birds with one stone. . .",
                                "K.",
                                "Sure, why not?",
                                "Lol, ok."])
                    ch_k "[Line]"
                    $ Line = renpy.random.choice(["Ok.",
                            "It couldn't hurt having you around. . .",
                            "Very well.",
                            "Sure, why not?",
                            "[[chuckles]. . . ok."])
                    ch_e "[Line]"
                    $ Line = renpy.random.choice(["Huh. Ok.",
                                "Couldn't hurt. . .",
                                "Allright.",
                                "Sure.",
                                "Heh, ok."])
                    ch_l "[Line]"
                    $ Line = renpy.random.choice(["Sure. Ok.",
                                "Couldn't hurt. . .",
                                "All right.",
                                "Sure.",
                                "Sure, why not. . ."])
                    ch_j "[Line]"
                    $ Line = renpy.random.choice(["You really do like to watch.",
                            "Once more?",
                            "You enjoy watching me do that?",
                            "You want me to take care of myself?"])
                    ch_s "[Line]"
                    $ Line = renpy.random.choice(["Huh. Ok.",
                                "Couldn't hurt. . .",
                                "Alright.",
                                "Sure.",
                                "Heh, ok."])
                    ch_v "[Line]"
                    $ Line = 0
                    jump Rogue_M_Prep
            "Just get at it already.":

                $ approval = approval_check(Girl, 450, "OI", TabM = 2)
                if approval > 1 or (approval and Girl.forced):
                    $ Girl.change_face("_sad")
                    $ Girl.change_stat("love", 70, -5, 1)
                    $ Girl.change_stat("love", 200, -5)
                    ch_r "Ok, fine. I'll give it a try."
                    ch_k "Fiiine, geeze."
                    ch_e "Oh, if it will shut you up."
                    ch_l "Whatever."
                    ch_j "Oh. . . fine. . ."
                    ch_s "Fine, if you insist."
                    ch_v "Whatever."
                    $ Girl.change_stat("obedience", 80, 4)
                    $ Girl.change_stat("inhibition", 80, 1)
                    $ Girl.change_stat("inhibition", 60, 3)
                    $ Girl.forced = 1
                    jump Rogue_M_Prep
                else:
                    $ Girl.change_stat("love", 200, -20)
                    $ Girl.recent_history.append("_angry")
                    $ Girl.daily_history.append("_angry")

    call action_rejected(Girl, primary_action)
    label begging_rejected:

label Rogue_M_Prep:
    $ Girl.upskirt = 1
    $ Girl.underwear_pulled_down = 1
    call Rogue_First_Bottomless (1)
    call set_the_scene (Dress=0)


    if "unseen" in Girl.recent_history:
        $ Girl.change_face("_sexy")
        $ Girl.eyes = "_closed"
        $ Girl.ArmPose = 2
        "You see [Girl.name] leaning back, masturbating. You don't think she's noticed you yet."
    else:
        $ Girl.change_face("_sexy")
        $ Girl.ArmPose = 2
        "[Girl.name] lays back and starts to toy with herself."
        if not Girl.action_counter["masturbation"]:
            if Girl.forced:
                $ Girl.change_stat("love", 90, -20)
                $ Girl.change_stat("obedience", 70, 45)
                $ Girl.change_stat("inhibition", 80, 35)
            else:
                $ Girl.change_stat("love", 90, 15)
                $ Girl.change_stat("obedience", 70, 35)
                $ Girl.change_stat("inhibition", 80, 40)


    $ primary_action = "masturbation"
    if not girl_offhand_action:
        $ girl_offhand_action = "fondle_pussy"

    if action_context:
        $ renpy.pop_call()
        $ action_context = None
    $ Line = 0
    if Taboo:
        $ Girl.drain_word("no_taboo")
    $ Girl.drain_word("no_masturbation")
    $ Girl.recent_history.append("masturbation")
    $ Girl.daily_history.append("masturbation")

label Rogue_M_Cycle:
    if action_context == "join":

        $ renpy.pop_call()
        $ action_context = None

    while round > 0:
        call Rogue_Pos_Reset ("masturbation")
        call shift_focus (Girl)
        $ Girl.lust_face
        if "unseen" in Girl.recent_history:
            $ Girl.eyes = "_closed"

        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if Player.focus < 100:

            menu:
                "Keep Watching.":
                    pass

                "[Girl.name]. . .[[jump in]" if "unseen" not in Girl.recent_history and "join" not in Player.recent_history and Girl.location == bg_current:
                    "[Girl.name] slows what she's doing with a sly grin."

                    call masturbation_join_in_lines(Girl, primary_action)
                    ch_r "Yeah, did you want something, [RogueX.player_petname]?"
                    ch_k "Like what you see?"
                    ch_e "Enjoying the show?"
                    ch_l "Are you enjoying this?"
                    ch_j "Like what you see?"
                    ch_s "Enjoying yourself?"
                    ch_v "Oh, are you having fun?"

                    $ action_context = "join"
                    call Rogue_Masturbate
                "\"Ahem. . .\"" if "unseen" in Girl.recent_history:
                    jump Rogue_M_Interupted

                "Start jack'in it." if offhand_action != "jackin":
                    call Jackin (Girl)
                "Stop jack'in it." if offhand_action == "jackin":
                    $ offhand_action = 0

                "Slap her ass" if Girl.location == bg_current:
                    if "unseen" in Girl.recent_history:
                        "You smack [Girl.name] firmly on the ass!"
                        jump Rogue_M_Interupted
                    else:
                        call Slap_Ass (Girl)
                        $ counter += 1
                        $ round -= 1
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
                        "Offhand action" if Girl.location == bg_current:
                            if Girl.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ Girl.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (Girl, "tired")

                        "Threesome actions (locked)" if not Partner or "unseen" in Girl.recent_history or Girl.location == bg_current:
                            pass
                        "Threesome actions" if Girl.location == bg_current and Partner and "unseen" not in Girl.recent_history:
                            menu:
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (Girl)
                                "Swap to [Partner.name]":
                                    call primary_action_Swap (Girl)
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

                        "Show her feet" if not ShowFeet and (Girl.pose == "doggy" or Girl.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (Girl.pose == "doggy" or Girl.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [Girl.name]":

                            if "unseen" in Girl.recent_history:
                                ch_p "Oh, yeah, take it off. . ."
                                jump Rogue_M_Interupted
                            else:
                                call Girl_Undress (Girl)
                        "Clean up [Girl.name] (locked)" if not Girl.spunk:
                            pass
                        "Clean up [Girl.name]" if Girl.spunk:
                            if "unseen" in Girl.recent_history:
                                ch_p "You've got a little something on you. . ."
                                jump Rogue_M_Interupted
                            else:
                                call Girl_Cleanup (Girl, "ask")
                        "Never mind":
                            jump Rogue_M_Cycle

                "Back to Sex Menu" if multi_action and Girl.location == bg_current:
                    ch_p "Let's try something else."
                    call Rogue_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Rogue_M_Interupted
                "End Scene" if not multi_action or Girl.location != bg_current:
                    ch_p "Let's stop for now."
                    call Rogue_Pos_Reset
                    $ Line = 0
                    jump Rogue_M_Interupted


        call shift_focus (Girl)
        call Sex_Dialog (Girl, Partner)



        $ counter += 1
        $ round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus

        if Player.focus >= 100 or Girl.lust >= 100:

            if Player.focus >= 100:
                if "unseen" not in Girl.recent_history:

                    call Player_Cumming (Girl)
                    if "_angry" in Girl.recent_history:
                        call Rogue_Pos_Reset
                        return
                    $ Girl.change_stat("lust", 200, 5)
                    if 100 > Girl.lust >= 70 and Girl.session_orgasms < 2:
                        $ Girl.recent_history.append("unsatisfied")
                        $ Girl.daily_history.append("unsatisfied")
                    $ Line = "came"
                else:
                    "You grunt and try to hold it in."
                    $ Player.focus = 95
                    if Girl.location == bg_current:
                        jump Rogue_M_Interupted


            if Girl.lust >= 100:
                call Girl_Cumming (Girl)
                if Girl.location == bg_current:
                    jump Rogue_M_Interupted

            if Line == "came":
                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."
                    $ offhand_action = 0 if offhand_action == "jackin" else offhand_action


                if "unsatisfied" in Girl.recent_history:
                    "[Girl.name] still seems a bit unsatisfied with the experience."
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


        if "unseen" in Girl.recent_history:
            if round == 10:
                "It's getting a bit late, [Girl.name] will probably be wrapping up soon."
            elif round == 5:
                "She's definitely going to stop soon."
        else:
            if Girl.location == bg_current:
                call Escalation (Girl)

            if round == 10:
                ch_r "We might want to wrap this up, it's getting late."
                $ Girl.lust += 10
            elif round == 5:
                ch_r "Seriously, it'll be time to stop soon."
                $ Girl.lust += 25


    $ Girl.change_face("_bemused", 0)
    $ Line = 0
    if "unseen" not in Girl.recent_history:
        ch_r "Ok, [Girl.player_petname], that's enough of that for now."

label Rogue_M_Interupted:


    if "unseen" in Girl.recent_history:
        $ Girl.change_face("_surprised", 1)
        "[Girl.name] stops what she's doing with a start, eyes wide."
        call Rogue_First_Bottomless (1)
        $ Girl.change_face("_surprised", 1)


        if offhand_action == "jackin":
            call caught_masturbating_lines(Girl)
            $ Girl.eyes = "_down"
            call notices_penis_is_out_lines(Girl)
            menu:
                "Long enough, it was an excellent show.":
                    $ Girl.change_face("_sexy")
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_stat("obedience", 70, 2)

                    call masturbation_excellent_show_cock_out(Girl, primary_action)
                    ch_r "Well, I imagine it was. . ."
                    ch_k "Um, I mean. . . yeah. . ."
                    ch_e "Well, obviously. . ."
                    ch_l "Really? Weird. . ."
                    ch_j "True. . ."
                    ch_s "I imagine it was. . ."
                    ch_v "Oh. . . um. . .thanks?"
                    if Girl.love >= 800 or Girl.obedience >= 500 or Girl.inhibition >= 500:
                        $ approval_bonus += 10
                        $ Girl.change_stat("lust", 90, 5)

                        call masturbation_excellent_show_cock_out_happy_lines(Girl, primary_action)
                        ch_r "And the view from this angle ain't so bad either. . ."
                        ch_k "I um. . . like what I'm seeing too. . ."
                        ch_e "and I suppose you bring a lot to the table as well, don't you. . ."
                        ch_l "I um. . . you're not so bad yourself. . ."
                        ch_j "And you can put on quite a show yourself. . ."
                        ch_s "and I have been missing a show myself. . ."
                        ch_v "I, um. . . you're not so bad yourself. . ."
                "I. . . just got here?":

                    $ Girl.change_face("_angry")
                    $ Girl.change_stat("love", 70, 2)
                    $ Girl.change_stat("love", 90, 1)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("obedience", 70, 2)
                    "She looks pointedly at your cock,"

                    call masturbation_just_got_here_cock_out_lines(Girl, primary_action)
                    ch_r "A likely story . . ."
                    ch_k "Long enough to whip that out?"
                    $ EmmaX.eyes = "_squint"
                    ch_e "Long enough to raise your sails?"
                    ch_l "Long enough to whip that out?"
                    ch_j "A likely story. . ."
                    ch_s "Long enough, it would appear. . ."
                    ch_v "Not by the looks of that thing."
                    if Girl.love >= 800 or Girl.obedience >= 500 or Girl.inhibition >= 500:
                        $ approval_bonus += 10
                        $ Girl.change_stat("lust", 90, 5)
                        $ Girl.change_face("_bemused", 1)

                        call masturbation_just_got_here_cock_out_happy_lines(Girl, primary_action)
                        ch_r "Still, can't blame a fella for take'in inspirations."
                        ch_k "I, um, guess I should be flattered?"
                        ch_e "I suppose you couldn't help yourself under the circumstances. . ."
                        ch_l "It was really that interesting?"
                        ch_j "I guess I can't blame you. . ."
                        ch_s "I expect that you could not contain your enthusiasm. . ."
                        ch_v "I guess I made an impression?"
                    else:
                        $ approval_bonus -= 10
                        $ Girl.change_stat("lust", 200, -5)

            call Seen_First_Peen (Girl, Partner)

            Girl.voice "Hmm. . ."
        else:
            call caught_masturbating_lines(Girl)
            menu:
                extend ""
                "Long enough.":
                    $ Girl.change_face("_sexy", 1)
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_stat("obedience", 70, 2)

                    call masturbation_watching_for_long_enough_lines(Girl, primary_action)
                    ch_r "Well I hope you got a good show out of it. . ."
                    ch_k "I hope I kept you entertained. . ."
                    ch_e "Enjoying the show?"
                    ch_l "I must have put on a show. . ."
                    ch_j "Nice of you to let me know. . ."
                    ch_s "And I assume you enjoyed the show?"
                    ch_v "I guess it must have been interesting. . ."
                "I just got here.":
                    $ Girl.change_face("_bemused", 1)
                    $ Girl.change_stat("love", 70, 2)
                    $ Girl.change_stat("love", 90, 1)

                    call masturbation_just_got_here_lines(Girl, primary_action)
                    ch_r "A likely story . . ."
                    ch_k "Yeah, I just bet. . ."
                    ch_e "Yes, I'm sure. . ."
                    ch_l "Uh-huh. . ."
                    ch_j "Uh-huh. . ."
                    ch_s "That seems likely. . ."
                    ch_v "Suuuure. . ."

                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("obedience", 70, 2)

        $ Girl.drain_word("unseen",1,0)
        $ Girl.action_counter["masturbation"] += 1
        if round <= 10:
            call too_late_to_masturbate_lines(Girl)
            ch_r "It's getting too late to do much about it right now though."
            return
        $ action_context = "join"
        call Rogue_Masturbate
        "error: report this if you see it."
        return



    $ Girl.remaining_actions -= 1
    $ Girl.action_counter["masturbation"] += 1

    if Partner == EmmaX:
        call Partner_Like (Girl, 4)
    else:
        call Partner_Like (Girl, 3)
    call checkout
    if action_context == "shift":
        $ action_context = None
        return
    $ action_context = None

    if Girl.location != bg_current:
        return

    if round <= 10:
        call masturbation_worn_out_lines(Girl, primary_action)
        ch_r "I need to take a little break here, [RogueX.player_petname]."
        ch_k "Gimme a minute, I need to collect myself here. . ."
        ch_e "Allow me to collect myself. . ."
        ch_l "I need a minute here. . ."
        ch_j "I need a minute here. . ."
        ch_s "Give me a moment to recover. . ."
        ch_v "I need a break anyway. . ."
        return
    $ Girl.change_face("_sexy", 1)
    if Girl.lust < 20:
        call end_of_masturbation_satisfied_lines(Girl, primary_action)
        ch_r "That really worked for me, [RogueX.player_petname]. How about you?"
        ch_k "Well that worked for me, how 'bout you?"
        ch_e "I suppose that took care of my needs, at least."
        ch_l "I guess that worked out, how about you?"
        ch_j "I got off, how about you?"
        ch_s "I enjoyed that, at least."
        ch_v "Well. . . I certainly enjoyed that. . ."
    else:
        call end_of_masturbation_lines(Girl, primary_action)
        ch_r "Yeah, what did you want?"
        ch_k "Um, yeah?"
        ch_e "Yes?"
        ch_l "So, what next?"
        ch_j "So, what next?"
        ch_s "Yes?"
        ch_v "So, what'd you wanna do next?"

    menu:
        extend ""
        "Well, I have something you could take care of. . ." if Player.semen and Girl.remaining_actions:
            $ action_context = "shift"
            return
        "You could just keep going. . ." if Player.semen:
            $ Girl.change_face("_sly")
            if Girl.remaining_actions and round >= 10:
                call masturbation_keep_going_lines(Girl, primary_action)
                ch_r "Well, alright. . ."
                ch_k "Sure. . ."
                ch_e "I suppose. . ."
                ch_l "Ok. . ."
                ch_j "Ok. . ."
                ch_s "I could. . ."
                ch_v "Ok. . ."

                jump Rogue_M_Cycle
            else:
                call masturbation_worn_out_lines(Girl, primary_action)
                ch_r "I'm kinda worn out, maybe time for a break. . ."
                ch_k "Gimme a minute, I need to collect myself here. . ."
                ch_e "Gimme a minute, I need to collect myself here. . ."
                ch_l "I need a minute here. . ."
                ch_j "I need a minute here. . ."
                ch_s "Give me a moment to recover. . ."
                ch_v "I need a minute here. . ."
        "I'm good here. [[Stop]":
            if Girl.love < 800 and Girl.inhibition < 500 and Girl.obedience < 500:
                $ Girl.change_outfit(Changed=0)
            $ Girl.change_face("_normal")
            $ Girl.brows = "_confused"

            call masturbation_good_here_lines(Girl, primary_action)
            ch_r "Well. . . ok then. . ."
            ch_k "Well. . . ok. . ."
            ch_e "Well. . . yes. . ."
            ch_l "Ok."
            ch_j "Ok."
            ch_s ". . . fine then. . ."
            ch_v "Ok, cool. . ."

            $ Girl.brows = "_normal"
        "You should probably stop for now." if Girl.lust > 30:
            $ Girl.change_face("_angry")

            call masturbation_stop_for_now_lines(Girl, primary_action)
            ch_r "Well if you say so."
            ch_k "I guess? . ."
            ch_e "I . . . yes . ."
            ch_l "Hrmm."
            ch_j "Hrmm."
            ch_s "I . . . fine . ."
            ch_v "Hrmm."
    return
