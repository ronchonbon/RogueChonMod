
label Kitty_SexAct(Act=0):
    call shift_focus (KittyX)
    if AloneCheck(KittyX) and KittyX.Taboo == 20:
        $ KittyX.Taboo = 0
        $ Taboo = 0
    if Act == "SkipTo":
        $ renpy.pop_call()
        $ renpy.pop_call()

        call SkipTo (KittyX)
    elif Act == "switch":
        $ renpy.pop_call()


    elif Act == "masturbate":
        call Kitty_M_Prep
        if not action_context:
            return
    elif Act == "lesbian":
        call Les_Prep (KittyX)
        if not action_context:
            return
    elif Act == "kissing":
        call KissPrep (KittyX)
        if not action_context:
            return
    elif Act == "breasts":
        call Kitty_Fondle_Breasts
        if not action_context:
            return
    elif Act == "blowjob":
        call Kitty_BJ_Prep
        if not action_context:
            return
    elif Act == "handjob":
        call Kitty_HJ_Prep
        if not action_context:
            return
    elif Act == "sex":
        call Kitty_SexPrep
        if not action_context:
            return



label Kitty_Masturbate:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (KittyX)
    if KittyX.action_counter["masturbation"]:
        $ approval_bonus += 10
    if KittyX.SEXP >= 50:
        $ approval_bonus += 25
    elif KittyX.SEXP >= 30:
        $ approval_bonus += 15
    elif KittyX.SEXP >= 15:
        $ approval_bonus += 5
    if KittyX.lust >= 90:
        $ approval_bonus += 20
    elif KittyX.lust >= 75:
        $ approval_bonus += 5
    if "exhibitionist" in KittyX.traits:
        $ approval_bonus += (3*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in KittyX.traits:
        $ approval_bonus -= 40
    if KittyX.event_counter["forced"] and not KittyX.Forced:
        $ approval_bonus -= 5*KittyX.event_counter["forced"]

    $ approval = approval_check(KittyX, 1300, TabM = 2)

    $ KittyX.drain_word("unseen",1,0)

    if action_context == "join":
        if approval > 1 or (approval and KittyX.lust >= 50):
            $ Player.add_word(1,"join")
            menu:
                extend ""
                "Would you like some help? I could lend some helping hands. . ." if Player.semen and KittyX.remaining_actions:
                    $ KittyX.change_stat("love", 90, 1)
                    $ KittyX.change_stat("obedience", 50, 2)
                    $ KittyX.change_face("sexy")
                    ch_k "Um, you know, maybe start up top?"
                    $ KittyX.change_stat("obedience", 70, 2)
                    $ KittyX.change_stat("inhibition", 70, 1)
                    $ offhand_action = "fondle_breasts"
                    $ KittyX.action_counter["masturbation"] += 1
                    jump Kitty_M_Cycle
                "Would you like some help? I could. . . up to you, I guess." if Player.semen and KittyX.remaining_actions:
                    $ KittyX.change_stat("love", 70, 2)
                    $ KittyX.change_stat("love", 90, 1)
                    $ KittyX.change_face("sexy")
                    ch_k "I'd[KittyX.like]love it if you could give me a hand. . ."
                    $ KittyX.change_stat("obedience", 70, 2)
                    $ KittyX.change_stat("inhibition", 70, 1)
                    $ D20 = renpy.random.randint(1, 20)
                    if D20 > 10:
                        $ offhand_action = "fondle_breasts"
                    else:
                        $ offhand_action = "suck_breasts"
                    $ KittyX.action_counter["masturbation"] += 1
                    jump Kitty_M_Cycle
                "Why don't we take care of each other?" if Player.semen and KittyX.remaining_actions:
                    $ KittyX.change_face("sexy")
                    ch_k "I think I could help with that. . ."
                    $ renpy.pop_call()
                    return
                "You look like you have things well in hand. . .":
                    if KittyX.lust >= 50:
                        $ KittyX.change_stat("love", 70, 2)
                        $ KittyX.change_stat("love", 90, 1)
                        $ KittyX.change_face("sexy")
                        ch_k "Well {i}I{/i} think so. . ."
                        $ KittyX.change_stat("obedience", 80, 3)
                        $ KittyX.change_stat("inhibition", 80, 5)
                        jump Kitty_M_Cycle
                    elif approval_check(KittyX, 1200):
                        $ KittyX.change_face("sly")
                        ch_k "Yeah. . . but I think I'm kinda done. . ."
                    else:
                        $ KittyX.change_face("angry")
                        ch_k "Hrmph, yeah, I kinda {i}did.{/i}"


        $ KittyX.ArmPose = 1
        $ KittyX.change_outfit()
        $ KittyX.remaining_actions -= 1
        $ Player.change_stat("focus", 50, 30)
        call checkout (1)
        $ Line = 0
        $ action_context = 0
        $ renpy.pop_call()
        if approval:
            $ KittyX.change_face("bemused", 2)
            if bg_current == "bg_kitty":
                ch_k "So what are you[KittyX.like]even doing here?"
            else:
                ch_k "I[KittyX.like]didn't expect to see you here. . ."
            $ KittyX.blushing = 1
        else:
            $ KittyX.change_stat("love", 200, -5)
            $ KittyX.change_face("angry")
            $ KittyX.recent_history.append("angry")
            $ KittyX.daily_history.append("angry")
            if bg_current == "bg_kitty":
                ch_k "So in case you couldn't tell, I was a little {i}busy?{/i} Maybe knock sometime?"
                "[KittyX.name] kicks you out of her room."
                $ renpy.pop_call()
                jump Campus_Map
            else:
                ch_k "So. . . I'm getting out of here? Maybe knock sometime?"
                hide Kitty_Sprite with easeoutbottom
                call Remove_Girl (KittyX)
        return




    if action_context == KittyX:
        if approval > 2:
            if KittyX.PantsNum() == 5:
                "[KittyX.name]'s hand snakes down her body, and hikes up her skirt."
                $ KittyX.upskirt = 1
            elif KittyX.PantsNum() > 6:
                "[KittyX.name] slides her hand down her body and into her jeans."
            elif KittyX.HoseNum() >= 5:
                "[KittyX.name]'s hand slides down her body and under her [KittyX.hose]."
            elif KittyX.underwear:
                "[KittyX.name]'s hand slides down her body and under her [KittyX.underwear]."
            else:
                "[KittyX.name]'s hand slides down her body and begins to caress her pussy."
            $ KittyX.SeenPanties = 1
            "She starts to slowly rub herself."
            call Kitty_First_Bottomless
            menu:
                "What do you do?"
                "Nothing.":
                    $ KittyX.change_stat("inhibition", 80, 3)
                    $ KittyX.change_stat("inhibition", 60, 2)
                    "[KittyX.name] begins to masturbate."
                "Go for it.":
                    $ KittyX.change_face("sexy, 1")
                    $ KittyX.change_stat("inhibition", 80, 3)
                    ch_p "That is so sexy, [KittyX.petname]."
                    $ KittyX.nameCheck()
                    "You lean back and enjoy the show."
                    $ KittyX.change_stat("love", 80, 1)
                    $ KittyX.change_stat("obedience", 90, 1)
                    $ KittyX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ KittyX.change_face("surprised")
                    $ KittyX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that right now, [KittyX.petname]."
                    $ KittyX.nameCheck()
                    "[KittyX.name] pulls her hands away from herself."
                    $ KittyX.change_outfit()
                    $ KittyX.change_stat("obedience", 90, 1)
                    $ KittyX.change_stat("obedience", 50, 1)
                    $ KittyX.change_stat("obedience", 30, 2)
                    return
            jump Kitty_M_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
        return



    if not KittyX.action_counter["masturbation"]:
        $ KittyX.change_face("surprised", 1)
        $ KittyX.mouth = "kiss"
        ch_k "You want me to. . . touch myself?"
        ch_k "And you're going to . . .watch?"
        if KittyX.Forced:
            $ KittyX.change_face("sad")
            ch_k "So you {i}just{/i} want to watch. . ."



    if not KittyX.action_counter["masturbation"] and approval:
        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
        elif KittyX.love >= KittyX.obedience and KittyX.love >= KittyX.inhibition:
            $ KittyX.change_face("sexy")
            $ KittyX.brows = "sad"
            $ KittyX.mouth = "smile"
            ch_k "This is kind of {i}intimate{/i} . . ."
        elif KittyX.obedience >= KittyX.inhibition:
            $ KittyX.change_face("normal")
            ch_k "Ok by me, [KittyX.player_petname]. . ."
        else:
            $ KittyX.change_face("sad")
            $ KittyX.mouth = "smile"
            ch_k "This could be kinda fun . . ."



    elif approval:
        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
            ch_k "Again? Just looking?"
        elif approval and "masturbation" in KittyX.recent_history:
            $ KittyX.change_face("sexy", 1)
            ch_k "I guess I could give it another go. . ."
            jump Kitty_M_Prep
        elif approval and "masturbation" in KittyX.daily_history:
            $ KittyX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Was it that good?",
                    "Didn't get enough earlier?",
                    "I kinda liked the audience. . ."])
            ch_k "[Line]"
        elif KittyX.action_counter["masturbation"] < 3:
            $ KittyX.change_face("sexy", 1)
            $ KittyX.brows = "confused"
            ch_k "Did you. . . like it last time?"
        else:
            $ KittyX.change_face("sexy", 1)
            $ KittyX.ArmPose = 2
            $ Line = renpy.random.choice(["You really like to watch.",
                    "Again?",
                    "You like to watch me.",
                    "You want me to get myself off?"])
            ch_k "[Line]"
            $ Line = 0



    if approval >= 2:
        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("obedience", 90, 1)
            $ KittyX.change_stat("inhibition", 60, 1)
            ch_k "Fine. . ."
        else:
            $ KittyX.change_face("sexy", 1)
            $ KittyX.change_stat("love", 90, 1)
            $ KittyX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Huh. Ok.",
                    "Couldn't hurt having you around. . .",
                    "Two birds with one stone. . .",
                    "K.",
                    "Sure, why not?",
                    "Lol, ok."])
            ch_k "[Line]"
            $ Line = 0
        $ KittyX.change_stat("obedience", 20, 1)
        $ KittyX.change_stat("obedience", 60, 1)
        $ KittyX.change_stat("inhibition", 70, 2)
        jump Kitty_M_Prep
    else:


        menu:
            ch_k "That's. . . private? You know?"
            "Maybe later?":
                $ KittyX.change_face("sexy", 1)
                if KittyX.lust > 70:
                    ch_k "Well, I know what {i}I'll{/i} be doing later. Not sure if you can come."
                    ch_k "I mean- you know, be there."
                    ch_k "I'm not sure you'll {i}be{/i} there."
                    ch_k ". . .coming."
                else:
                    ch_k "Hmm, maybe. . . I'll text you?"
                $ KittyX.change_stat("love", 80, 2)
                $ KittyX.change_stat("inhibition", 70, 2)
                return
            "You look like you could use it. . .":
                if approval:
                    $ KittyX.change_face("sexy")
                    $ KittyX.change_stat("obedience", 90, 2)
                    $ KittyX.change_stat("obedience", 50, 2)
                    $ KittyX.change_stat("inhibition", 70, 3)
                    $ KittyX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Huh. Ok.",
                                "Couldn't hurt having you around. . .",
                                "Two birds with one stone. . .",
                                "K.",
                                "Sure, why not?",
                                "Lol, ok."])
                    ch_k "[Line]"
                    $ Line = 0
                    jump Kitty_M_Prep
            "Just get at it already.":

                $ approval = approval_check(KittyX, 450, "OI", TabM = 2)
                if approval > 1 or (approval and KittyX.Forced):
                    $ KittyX.change_face("sad")
                    $ KittyX.change_stat("love", 70, -5, 1)
                    $ KittyX.change_stat("love", 200, -5)
                    ch_k "Fiiine, geeze."
                    $ KittyX.change_stat("obedience", 80, 4)
                    $ KittyX.change_stat("inhibition", 80, 1)
                    $ KittyX.change_stat("inhibition", 60, 3)
                    $ KittyX.Forced = 1
                    jump Kitty_M_Prep
                else:
                    $ KittyX.change_stat("love", 200, -20)
                    $ KittyX.recent_history.append("angry")
                    $ KittyX.daily_history.append("angry")



    $ KittyX.ArmPose = 1
    if KittyX.Forced:
        $ KittyX.change_face("angry", 1)
        ch_k "I. . . can't, not with you watching."
        $ KittyX.change_stat("lust", 90, 5)
        if KittyX.love > 300:
            $ KittyX.change_stat("love", 70, -2)
        $ KittyX.change_stat("obedience", 50, -2)
        $ KittyX.recent_history.append("angry")
        $ KittyX.daily_history.append("angry")
        $ KittyX.recent_history.append("no_masturbation")
        $ KittyX.daily_history.append("no_masturbation")
        return
    elif Taboo:
        $ KittyX.change_face("angry", 1)
        $ KittyX.daily_history.append("no_taboo")
        ch_k "Certainly not here!"
        $ KittyX.change_stat("lust", 90, 5)
        $ KittyX.change_stat("obedience", 50, -3)
        return
    elif KittyX.action_counter["masturbation"]:
        $ KittyX.change_face("sad")
        ch_k "Sorry, maybe try a porn game or something."
    else:
        $ KittyX.change_face("normal", 1)
        ch_k "Um, no."
    $ KittyX.recent_history.append("no_masturbation")
    $ KittyX.daily_history.append("no_masturbation")
    $ approval_bonus = 0
    return

label Kitty_M_Prep:
    $ KittyX.upskirt = 1
    $ KittyX.underwear_pulled_down = 1
    call Kitty_First_Bottomless (1)
    call set_the_scene (Dress=0)


    if "unseen" in KittyX.recent_history:
        $ KittyX.change_face("sexy")
        $ KittyX.eyes = "closed"
        $ KittyX.ArmPose = 2
        "You see [KittyX.name] leaning back, masturbating. You don't think she's noticed you yet."
    else:
        $ KittyX.change_face("sexy")
        $ KittyX.ArmPose = 2
        "[KittyX.name] lays back and starts to toy with herself."
        if not KittyX.action_counter["masturbation"]:
            if KittyX.Forced:
                $ KittyX.change_stat("love", 90, -20)
                $ KittyX.change_stat("obedience", 70, 45)
                $ KittyX.change_stat("inhibition", 80, 35)
            else:
                $ KittyX.change_stat("love", 90, 15)
                $ KittyX.change_stat("obedience", 70, 35)
                $ KittyX.change_stat("inhibition", 80, 40)


    $ primary_action = "masturbation"
    if not girl_offhand_action:
        $ girl_offhand_action = "fondle_pussy"
    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    if Taboo:
        $ KittyX.drain_word("no_taboo")
    $ KittyX.drain_word("no_masturbation")
    $ KittyX.recent_history.append("masturbation")
    $ KittyX.daily_history.append("masturbation")

label Kitty_M_Cycle:
    if action_context == "join":
        $ renpy.pop_call()
        $ action_context = 0

    while Round > 0:
        call Kitty_Pos_Reset ("masturbation")
        call shift_focus (KittyX)
        $ KittyX.lust_face()
        if "unseen" in KittyX.recent_history:
            $ KittyX.eyes = "closed"

        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if Player.focus < 100:

            menu:
                "Keep Watching.":
                    pass

                "[KittyX.name]. . .[[jump in]" if "unseen" not in KittyX.recent_history and "join" not in Player.recent_history and KittyX.location == bg_current:
                    "[KittyX.name] slows what she's doing with a sly grin."
                    ch_k "Like what you see?"
                    $ action_context = "join"
                    call Kitty_Masturbate
                "\"Ahem. . .\"" if "unseen" in KittyX.recent_history and KittyX.location == bg_current:
                    jump Kitty_M_Interupted

                "Start jack'in it." if offhand_action != "jackin":
                    call Jackin (KittyX)
                "Stop jack'in it." if offhand_action == "jackin":
                    $ offhand_action = 0

                "Slap her ass" if KittyX.location == bg_current:
                    if "unseen" in KittyX.recent_history:
                        "You smack [KittyX.name] firmly on the ass!"
                        jump Kitty_M_Interupted
                    else:
                        call Slap_Ass (KittyX)
                        $ counter += 1
                        $ Round -= 1
                        jump Kitty_M_Cycle

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
                        "Offhand action" if KittyX.location == bg_current:
                            if KittyX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ KittyX.remaining_actions -= 1
                            else:
                                ch_k "I'm actually getting a little tired, so maybe we could wrap this up?"

                        "Threesome actions (locked)" if not Partner or "unseen" in KittyX.recent_history or KittyX.location != bg_current:
                            pass
                        "Threesome actions" if Partner and "unseen" not in KittyX.recent_history and KittyX.location == bg_current:
                            menu:
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (KittyX)
                                "Swap to [Partner.name]":
                                    call primary_action_Swap (KittyX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Kitty_M_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Kitty_M_Cycle
                                "Never mind":
                                    jump Kitty_M_Cycle

                        "Show her feet" if not ShowFeet and (KittyX.pose == "doggy" or KittyX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (KittyX.pose == "doggy" or KittyX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [KittyX.name]":

                            if "unseen" in KittyX.recent_history:
                                ch_p "Oh, yeah, take it off. . ."
                                jump Kitty_M_Interupted
                            else:
                                call Girl_Undress (KittyX)
                        "Clean up [KittyX.name] (locked)" if not KittyX.spunk:
                            pass
                        "Clean up [KittyX.name]" if KittyX.spunk:
                            if "unseen" in KittyX.recent_history:
                                ch_p "You've got a little something on you. . ."
                                jump Kitty_M_Interupted
                            else:
                                call Girl_Cleanup (KittyX, "ask")
                        "Never mind":
                            jump Kitty_M_Cycle

                "Back to Sex Menu" if multi_action and KittyX.location == bg_current:
                    ch_p "Let's try something else."
                    call Kitty_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Kitty_M_Interupted
                "End Scene" if not multi_action or KittyX.location != bg_current:
                    ch_p "Let's stop for now."
                    call Kitty_Pos_Reset
                    $ Line = 0
                    jump Kitty_M_Interupted


        call shift_focus (KittyX)
        call Sex_Dialog (KittyX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus

        if Player.focus >= 100 or KittyX.lust >= 100:

            if Player.focus >= 100:
                if "unseen" not in KittyX.recent_history:

                    call Player_Cumming (KittyX)
                    if "angry" in KittyX.recent_history:
                        call Kitty_Pos_Reset
                        return
                    $ KittyX.change_stat("lust", 200, 5)
                    if 100 > KittyX.lust >= 70 and KittyX.session_orgasms < 2:
                        $ KittyX.recent_history.append("unsatisfied")
                        $ KittyX.daily_history.append("unsatisfied")
                    $ Line = "came"
                else:
                    "You grunt and try to hold it in."
                    $ Player.focus = 95
                    if KittyX.location == bg_current:
                        jump Kitty_M_Interupted


            if KittyX.lust >= 100:
                call Girl_Cumming (KittyX)
                if KittyX.location == bg_current:
                    jump Kitty_M_Interupted

            if Line == "came":
                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."
                    $ offhand_action = 0 if offhand_action == "jackin" else offhand_action


                if "unsatisfied" in KittyX.recent_history:
                    "[KittyX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Let her keep going?"
                        "Yes, keep going for a bit.":
                            $ Line = "You let her get back into it"
                            jump Kitty_M_Cycle
                        "No, I'm done.":
                            "You ask her to stop."
                            return
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        if "unseen" in KittyX.recent_history:
            if Round == 10:
                "It's getting a bit late, [KittyX.name] will probably be wrapping up soon."
            elif Round == 5:
                "She's definitely going to stop soon."
        else:
            if KittyX.location == bg_current:
                call Escalation (KittyX)

            if Round == 10:
                ch_k "We might want to wrap this up, it's getting late."
                $ KittyX.lust += 10
            elif Round == 5:
                ch_k "Seriously, it'll be time to stop soon."
                $ KittyX.lust += 25


    $ KittyX.change_face("bemused", 0)
    $ Line = 0
    if "unseen" not in KittyX.recent_history:
        ch_k "Ok, I'm kinda done for now, I need a break."

label Kitty_M_Interupted:


    if "unseen" in KittyX.recent_history:
        $ KittyX.change_face("surprised", 2)
        "[KittyX.name] stops what she's doing with a start, eyes wide."
        call Kitty_First_Bottomless (1)
        $ KittyX.change_face("surprised", 2)


        if offhand_action == "jackin":
            ch_k "Eeep!"
            ch_k "When did you get here?!"
            $ KittyX.eyes = "down"
            menu:
                ch_k "And um. . . your cock is out. . . "
                "A while back, it was an excellent show.":
                    $ KittyX.change_face("sexy",1)
                    $ KittyX.change_stat("obedience", 50, 3)
                    $ KittyX.change_stat("obedience", 70, 2)
                    ch_k "Um, I mean. . . yeah. . ."
                    if KittyX.love >= 800 or KittyX.obedience >= 500 or KittyX.inhibition >= 500:
                        $ approval_bonus += 10
                        $ KittyX.change_stat("lust", 90, 5)
                        ch_k "I um. . . like what I'm seeing too. . ."
                "I. . . just got here?":

                    $ KittyX.change_face("angry",1)
                    $ KittyX.change_stat("love", 70, 2)
                    $ KittyX.change_stat("love", 90, 1)
                    $ KittyX.change_stat("obedience", 50, 2)
                    $ KittyX.change_stat("obedience", 70, 2)
                    "She looks pointedly at your cock,"
                    ch_k "Long enough to whip that out?"
                    if KittyX.love >= 800 or KittyX.obedience >= 500 or KittyX.inhibition >= 500:
                        $ approval_bonus += 10
                        $ KittyX.change_stat("lust", 90, 5)
                        $ KittyX.change_face("bemused", 1)
                        ch_k "I, um, guess I should be flattered?"
                    else:
                        $ approval_bonus -= 10
                        $ KittyX.change_stat("lust", 200, -5)
            call Seen_First_Peen (KittyX, Partner)
            ch_k "Hmm. . ."
        else:


            ch_k "Eeep!"
            ch_k "When did you get here?!"
            menu:
                extend ""
                "A while back.":
                    $ KittyX.change_face("sexy", 1)
                    $ KittyX.change_stat("obedience", 50, 3)
                    $ KittyX.change_stat("obedience", 70, 2)
                    ch_k "I hope I kept you entertained. . ."
                "I just got here.":
                    $ KittyX.change_face("bemused", 1)
                    $ KittyX.change_stat("love", 70, 2)
                    $ KittyX.change_stat("love", 90, 1)
                    ch_k "Yeah, I just bet. . ."
                    $ KittyX.change_stat("obedience", 50, 2)
                    $ KittyX.change_stat("obedience", 70, 2)

        $ KittyX.drain_word("unseen",1,0)
        $ KittyX.action_counter["masturbation"] += 1
        if Round <= 10:
            ch_k "It's getting kinda late to do anything about it. . ."
            return
        $ action_context = "join"
        call Kitty_Masturbate
        "error: report this if you see it."
        return



    $ KittyX.remaining_actions -= 1
    $ KittyX.action_counter["masturbation"] += 1
    call checkout
    if action_context == "shift":
        $ action_context = 0
        return
    $ action_context = 0

    call Partner_Like (KittyX, 3)

    if KittyX.location != bg_current:
        return

    if Round <= 10:
        ch_k "Gimme a minute, I need to collect myself here. . ."
        return
    $ KittyX.change_face("sexy", 1)
    if KittyX.lust < 20:
        ch_k "Well that worked for me, how 'bout you?"
    else:
        ch_k "Um, yeah?"
    menu:
        extend ""
        "Well, I have something you could take care of. . ." if Player.semen and KittyX.remaining_actions:
            $ action_context = "shift"
            return
        "You could just keep going. . ." if Player.semen:
            $ KittyX.change_face("sly")
            if KittyX.remaining_actions and Round >= 10:
                ch_k "Sure. . ."
                jump Kitty_M_Cycle
            else:
                ch_k "Gimme a minute, I need to collect myself here. . ."
        "I'm good here. [[Stop]":
            if KittyX.love < 800 and KittyX.inhibition < 500 and KittyX.obedience < 500:
                $ KittyX.change_outfit()
            $ KittyX.change_face("normal")
            $ KittyX.brows = "confused"
            ch_k "Well. . . ok. . ."
            $ KittyX.brows = "normal"
        "You should probably stop for now." if KittyX.lust > 30:
            $ KittyX.change_face("angry")
            ch_k "I guess? . ."
    return






label Kitty_Sex_P:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (KittyX)
    if KittyX.action_counter["sex"] >= 7:
        $ approval_bonus += 15
    elif KittyX.action_counter["sex"] >= 3:
        $ approval_bonus += 12
    elif KittyX.action_counter["sex"]:
        $ approval_bonus += 10

    if KittyX.addiction >= 75 and (KittyX.event_counter["creampied"] + KittyX.event_counter["anal_creampied"]) >=3:
        $ approval_bonus += 20
    elif KittyX.addiction >= 75:
        $ approval_bonus += 15

    if KittyX.lust > 85:
        $ approval_bonus += 10
    elif KittyX.lust > 75:
        $ approval_bonus += 5

    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in KittyX.traits:
        $ approval_bonus += (4*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in KittyX.traits:
        $ approval_bonus -= 40
    if KittyX.event_counter["forced"] and not KittyX.Forced:
        $ approval_bonus -= 5*KittyX.event_counter["forced"]



    if Taboo and "no_taboo" in KittyX.daily_history:
        $ approval_bonus -= 10

    if "no_sex" in KittyX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_sex" in KittyX.recent_history else 0


    $ approval = approval_check(KittyX, 1400, TabM = 5)

    if action_context == "auto":
        call Kitty_Sex_Launch ("sex")
        if KittyX.PantsNum() == 5:
            "You press [KittyX.name] down onto her back, sliding her skirt up as you go."
            $ KittyX.upskirt = 1
        elif KittyX.PantsNum() > 6:
            "You press [KittyX.name] down onto her back, sliding her pants down as you do."
            $ KittyX.upskirt = 1
        elif KittyX.PantsNum() == 6:
            "You press [KittyX.name] down onto her back, sliding her shorts down as you do."
            $ KittyX.upskirt = 1
        else:
            "You press [KittyX.name] down onto her back."
        $ KittyX.SeenPanties = 1
        "You rub the tip of your cock against her moist slit."
        $ KittyX.change_face("surprised", 1)

        if (KittyX.action_counter["sex"] and approval) or (approval > 1):

            "[KittyX.name] is briefly startled, but melts into a sly smile."
            $ KittyX.change_face("sexy")
            $ KittyX.change_stat("obedience", 70, 3)
            $ KittyX.change_stat("inhibition", 50, 3)
            $ KittyX.change_stat("inhibition", 70, 1)
            ch_k "Oh. . . game on, [KittyX.player_petname]."
            jump Kitty_SexPrep
        else:

            $ KittyX.brows = "angry"
            menu:
                ch_k "Um, what do you think you're doing?"
                "Sorry, sorry! Never mind.":
                    if approval:
                        $ KittyX.change_face("sexy", 1)
                        $ KittyX.change_stat("obedience", 70, 3)
                        $ KittyX.change_stat("inhibition", 50, 3)
                        $ KittyX.change_stat("inhibition", 70, 1)
                        ch_k "{i}Well. . .{/i} I didn't say I didn't want to. . ."
                        jump Kitty_SexPrep
                    else:
                        "You pull back before you really get it in."
                        $ KittyX.change_face("bemused", 1)
                        if KittyX.action_counter["sex"]:
                            ch_k "Maybe you could[KittyX.like]warn me?"
                        else:
                            ch_k "Maybe you could[KittyX.like]warn me? I don't know that I'm[KittyX.like]ready for that sort of thing. . ."
                "Just fucking.":
                    $ KittyX.change_stat("love", 80, -10, 1)
                    $ KittyX.change_stat("love", 200, -10)
                    "You press inside some more."
                    $ KittyX.change_stat("obedience", 70, 3)
                    $ KittyX.change_stat("inhibition", 50, 3)
                    if not approval_check(KittyX, 700, "O", TabM=1):
                        $ KittyX.change_face("angry")
                        "[KittyX.name] shoves you away and slaps you in the face."
                        ch_k "Jerk!"
                        ch_k "I am not putting up with that shit!"
                        $ KittyX.change_stat("love", 50, -10, 1)
                        $ KittyX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        call Kitty_Sex_Reset
                        $ KittyX.recent_history.append("angry")
                        $ KittyX.daily_history.append("angry")
                    else:
                        $ KittyX.change_face("sad")
                        "[KittyX.name] doesn't seem to be into this, you're lucky she's so obedient."
                        jump Kitty_SexPrep
        return



    if not KittyX.action_counter["sex"] and "no_sex" not in KittyX.recent_history:

        $ KittyX.change_face("surprised", 1)
        $ KittyX.mouth = "kiss"
        ch_k "I haven't really had much experience with this. . . "
        if KittyX.Forced:
            $ KittyX.change_face("sad")
            ch_k "You'd really do this when you have me over a barrel?"


    if not KittyX.action_counter["sex"] and approval:

        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("love", 70, -30, 1)
            $ KittyX.change_stat("love", 20, -20, 1)
        elif KittyX.love >= (KittyX.obedience + KittyX.inhibition):
            $ KittyX.change_face("sexy")
            $ KittyX.brows = "sad"
            $ KittyX.mouth = "smile"
            ch_k "I don't want you to think I'm some kind of slut. . ."
        elif KittyX.obedience >= KittyX.inhibition:
            $ KittyX.change_face("normal")
            ch_k "I suppose if it's you, [KittyX.player_petname]. . ."
        elif KittyX.addiction >= 50:
            $ KittyX.change_face("manic", 1)
            ch_k "I have kind of been hoping you might. . ."
        else:
            $ KittyX.change_face("sad")
            $ KittyX.mouth = "smile"
            ch_k "I can't say it hasn't crossed my mind. . ."


    elif approval:

        $ KittyX.change_face("sexy", 1)
        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
            ch_k "Again? Why do you do this to me?"
        elif not Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "I guess this is more secluded. . ."
        elif "sex" in KittyX.recent_history:
            ch_k "Another round? {i}Fine.{/i}"
            jump Kitty_SexPrep
        elif "sex" in KittyX.daily_history:
            $ Line = renpy.random.choice(["Back again so soon?",
                    "So you'd like another round?",
                    "You can't stay away from this. . .",
                    "Didn't get enough earlier?",
                    "You're wearing me out here!"])
            ch_k "[Line]"
        elif KittyX.action_counter["sex"] < 3:
            $ KittyX.brows = "confused"
            $ KittyX.mouth = "kiss"
            ch_k "So you'd like another round?"
        else:
            $ Line = renpy.random.choice(["Oooh, you want some of this?",
                    "So you'd like another round?",
                    "You can't stay away from this. . .",
                    "You gonna make me purr?",
                    "You wanna slide into me?"])
            ch_k "[Line]"
        $ Line = 0


    if approval >= 2:

        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("obedience", 90, 1)
            $ KittyX.change_stat("inhibition", 60, 1)
            ch_k "Ok, fiiiiine."
        elif "no_sex" in KittyX.daily_history:
            ch_k "You've made your case. . ."
        else:
            $ KittyX.change_face("sexy", 1)
            $ KittyX.change_stat("love", 90, 1)
            $ KittyX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well. . . ok.",
                    "Sure!",
                    "You could, I guess.",
                    "Um, yeah.",
                    "Heh, ok, ok."])
            ch_k "[Line]"
            $ Line = 0
        $ KittyX.change_stat("obedience", 20, 1)
        $ KittyX.change_stat("obedience", 60, 1)
        $ KittyX.change_stat("inhibition", 70, 2)
        jump Kitty_SexPrep
    else:


        $ KittyX.change_face("angry")
        if "no_sex" in KittyX.recent_history:
            ch_k "I{i}just{/i}[KittyX.like]told you \"no!\""
        elif Taboo and "no_taboo" in KittyX.daily_history and "no_sex" in KittyX.daily_history:
            ch_k "I already told you. . .not in public!"
        elif "no_sex" in KittyX.daily_history:
            ch_k "I already[KittyX.like]told you \"no.\""
        elif Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "I already told you this is too public!"
        elif not KittyX.action_counter["sex"]:
            $ KittyX.change_face("bemused")
            ch_k "I don't know that I'm. . .[KittyX.like]ready? . ."
        else:
            $ KittyX.change_face("bemused")
            ch_k "Maybe[KittyX.like]not right now? . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_sex" in KittyX.daily_history:
                $ KittyX.change_face("bemused")
                ch_k "It's cool."
                return
            "Maybe later?" if "no_sex" not in KittyX.daily_history:
                $ KittyX.change_face("sexy")
                ch_k "Maybe, you never know."
                $ KittyX.change_stat("love", 80, 2)
                $ KittyX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ KittyX.recent_history.append("no_taboo")
                    $ KittyX.daily_history.append("no_taboo")
                $ KittyX.recent_history.append("no_sex")
                $ KittyX.daily_history.append("no_sex")
                return
            "I think you'd enjoy it as much as I would. . .":
                if approval:
                    $ KittyX.change_face("sexy")
                    $ KittyX.change_stat("obedience", 90, 2)
                    $ KittyX.change_stat("obedience", 50, 2)
                    $ KittyX.change_stat("inhibition", 70, 3)
                    $ KittyX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["That's. . . true. . .",
                                "I suppose. . .",
                                "That's. . . that's a good point. . ."])
                    ch_k "[Line]"
                    $ Line = 0
                    jump Kitty_SexPrep
            "Just deal with it.":
                $ approval = approval_check(KittyX, 1150, "OI", TabM = 3)
                if approval > 1 or (approval and KittyX.Forced):
                    $ KittyX.change_face("sad")
                    $ KittyX.change_stat("love", 70, -5, 1)
                    $ KittyX.change_stat("love", 200, -5)
                    ch_k "Well! . . ok, fine, stick it in."
                    $ KittyX.change_stat("obedience", 80, 4)
                    $ KittyX.change_stat("inhibition", 80, 1)
                    $ KittyX.change_stat("inhibition", 60, 3)
                    $ KittyX.Forced = 1
                    jump Kitty_SexPrep
                else:
                    $ KittyX.change_stat("love", 200, -20)
                    $ KittyX.recent_history.append("angry")
                    $ KittyX.daily_history.append("angry")




    $ KittyX.ArmPose = 1
    if "no_sex" in KittyX.daily_history:
        ch_k "Maybe[KittyX.like]take \"no\" for an answer?"
        $ KittyX.recent_history.append("angry")
        $ KittyX.daily_history.append("angry")
    elif KittyX.Forced:
        $ KittyX.change_face("angry", 1)
        ch_k "Not even."
        $ KittyX.change_stat("lust", 200, 5)
        if KittyX.love > 300:
            $ KittyX.change_stat("love", 70, -2)
        $ KittyX.change_stat("obedience", 50, -2)
        $ KittyX.recent_history.append("angry")
        $ KittyX.daily_history.append("angry")
    elif Taboo:
        $ KittyX.change_face("angry", 1)
        $ KittyX.recent_history.append("no_taboo")
        $ KittyX.daily_history.append("no_taboo")
        ch_k "I can't believe you'd even consider it around here!"
        $ KittyX.change_stat("lust", 200, 5)
        $ KittyX.change_stat("obedience", 50, -3)
    elif KittyX.action_counter["sex"]:
        $ KittyX.change_face("sad")
        ch_k "Maybe just[KittyX.like]fuck yourself, huh?"
    else:
        $ KittyX.change_face("normal", 1)
        ch_k "Nuhuh."
    $ KittyX.recent_history.append("no_sex")
    $ KittyX.daily_history.append("no_sex")
    $ approval_bonus = 0
    return

label Kitty_SexPrep:
    call Seen_First_Peen (KittyX, Partner, React=action_context)
    call Kitty_Sex_Launch ("hotdog")

    if action_context == KittyX:

        $ action_context = 0
        if KittyX.PantsNum() == 5:
            "[KittyX.name] rolls back and pulls you toward her, sliding her skirt up as she does so."
            $ KittyX.upskirt = 1
        elif KittyX.PantsNum() > 6:
            "[KittyX.name] rolls back and pulls you against her, sliding her pants off as she does so."
            $ KittyX.upskirt = 1
        elif KittyX.PantsNum() == 6:
            "[KittyX.name] rolls onto her back and pulls you against her, sliding her shorts off as she does so."
            $ KittyX.upskirt = 1
        else:
            "[KittyX.name] rolls back and pulls you toward her."
        $ KittyX.SeenPanties = 1
        "She slides the tip along her pussy and seems to want you to insert it."
        menu:
            "What do you do?"
            "Go with it.":
                $ KittyX.change_stat("inhibition", 80, 3)
                $ KittyX.change_stat("inhibition", 50, 2)
                "[KittyX.name] slides it in."
            "Praise her.":
                $ KittyX.change_face("sexy", 1)
                $ KittyX.change_stat("inhibition", 80, 3)
                ch_p "Oh yeah, [KittyX.petname], let's do this."
                $ KittyX.nameCheck()
                "[KittyX.name] slides it in."
                $ KittyX.change_stat("love", 85, 1)
                $ KittyX.change_stat("obedience", 90, 1)
                $ KittyX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ KittyX.change_face("surprised")
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
        $ KittyX.underwear_pulled_down = 1
        call Kitty_First_Bottomless (1)

    elif action_context != "auto":
        call AutoStrip (KittyX)

        if Taboo:
            if not KittyX.action_counter["sex"]:
                "[KittyX.name] glances around for voyeurs. . ."
                if "cockout" in Player.recent_history:
                    "[KittyX.name] slowly presses against your rigid member."
                else:
                    "[KittyX.name] hesitantly pulls down your pants and slowly presses against your rigid member."
                "You guide it into place and slide it in."
            else:
                "[KittyX.name] glances around to see if anyone notices what she's doing, then presses firmly against your cock."
                "You guide your cock into place and ram it home."
            $ KittyX.inhibition += int(Taboo/10)
            $ KittyX.lust += int(Taboo/5)
        else:
            if not KittyX.action_counter["sex"]:
                if "cockout" in Player.recent_history:
                    "[KittyX.name] slowly presses against your rigid member."
                else:
                    "[KittyX.name] hesitantly pulls down your pants and slowly presses against your rigid member."
                "You press her folds aside and nudge your cock in."
            else:
                "[KittyX.name] leans back and presses against you suggestively."
                "You take careful aim and then ram your cock in."
    else:

        if (KittyX.PantsNum() > 6 and not KittyX.upskirt) and (KittyX.underwear and not KittyX.underwear_pulled_down):
            "You quickly pull down her pants and her [KittyX.underwear] and press against her slit."
        elif (KittyX.underwear and not KittyX.underwear_pulled_down):
            "You quickly pull down her [KittyX.underwear] and press against her slit."
        $ KittyX.upskirt = 1
        $ KittyX.underwear_pulled_down = 1
        $ KittyX.SeenPanties = 1
        call Kitty_First_Bottomless (1)

    if not KittyX.action_counter["sex"]:
        if KittyX.Forced:
            $ KittyX.change_stat("love", 90, -150)
            $ KittyX.change_stat("obedience", 70, 60)
            $ KittyX.change_stat("inhibition", 80, 50)
        else:
            $ KittyX.change_stat("love", 90, 30)
            $ KittyX.change_stat("obedience", 70, 30)
            $ KittyX.change_stat("inhibition", 80, 60)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    $ Player.cock_position = "in"
    $ primary_action = "sex"
    $ action_speed = 1
    if Taboo:
        $ KittyX.drain_word("no_taboo")
    $ KittyX.drain_word("no_sex")
    $ KittyX.recent_history.append("sex")
    $ KittyX.daily_history.append("sex")

label Kitty_Sex_Cycle:
    while Round > 0:
        call shift_focus (KittyX)
        call Kitty_Sex_Launch ("sex")
        $ KittyX.lust_face()
        $ Player.cock_position = "in"
        $ primary_action = "sex"
        $ KittyX.upskirt = 1
        $ KittyX.underwear_pulled_down = 1

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

                    call Slap_Ass (KittyX)
                    $ counter += 1
                    $ Round -= 1
                    jump Kitty_Sex_Cycle
                "Turn her Around":

                    $ KittyX.pose = "doggy" if KittyX.pose != "doggy" else "sex"
                    "You turn her around. . ."
                    jump Kitty_Sex_Cycle

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
                            if KittyX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ KittyX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (KittyX, "tired")
                        "Shift primary action":

                            if KittyX.remaining_actions and multi_action:
                                menu:
                                    "How about anal?":
                                        $ action_context = "shift"
                                        call Kitty_SexAfter
                                        call Kitty_Sex_A
                                    "Just stick it in her ass [[without asking].":
                                        $ action_context = "auto"
                                        call Kitty_SexAfter
                                        call Kitty_Sex_A
                                    "Pull back to hotdog her.":
                                        $ action_context = "pullback"
                                        call Kitty_SexAfter
                                        call Kitty_Sex_H
                                    "Never Mind":
                                        jump Kitty_Sex_Cycle
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
                                    jump Kitty_Sex_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Kitty_Sex_Cycle
                                "Never mind":
                                    jump Kitty_Sex_Cycle
                        "Just take a look at her.":
                            $ Player.cock_position = 0
                            $ action_speed = 0

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
                            jump Kitty_Sex_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Kitty_Sex_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Kitty_SexAfter
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Kitty_Sex_Reset
                    $ Line = 0
                    jump Kitty_SexAfter


        call shift_focus (KittyX)
        call Sex_Dialog (KittyX, Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or KittyX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (KittyX)
                if "angry" in KittyX.recent_history:
                    call Kitty_Sex_Reset
                    return
                $ KittyX.change_stat("lust", 200, 5)
                if 100 > KittyX.lust >= 70 and KittyX.session_orgasms < 2:
                    $ KittyX.recent_history.append("unsatisfied")
                    $ KittyX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Kitty_SexAfter
                $ Line = "came"

            if KittyX.lust >= 100:

                call Girl_Cumming (KittyX)
                if action_context == "shift" or "angry" in KittyX.recent_history:
                    jump Kitty_SexAfter

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "She's emptied you out, you'll need to take a break."
                    jump Kitty_SexAfter
                elif "unsatisfied" in KittyX.recent_history:

                    $ Line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                    "[Line] Keep going?"
                    menu:
                        extend ""
                        "Yes, keep going for a bit." if Player.semen:
                            $ Line = "You get back into it"
                            jump Kitty_Sex_Cycle
                        "No, I'm done." if Player.semen:
                            "You pull back."
                            jump Kitty_SexAfter
                        "No, I'm spent." if not Player.semen:
                            "You pull back."
                            jump Kitty_SexAfter
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if KittyX.SEXP >= 100 or approval_check(KittyX, 1200, "LO"):
            pass
        elif counter == (5 + KittyX.action_counter["sex"]):
            $ KittyX.brows = "confused"
            ch_k "So are we[KittyX.like]getting close here?"
        elif counter == (10 + KittyX.action_counter["sex"]):
            $ KittyX.brows = "angry"
            ch_k "I'm . . .getting . . kinda tired. . . here. . ."
            menu:
                ch_k "Can we. . . do something. . . else?"
                "How about a BJ?" if KittyX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Kitty_SexAfter
                    call Kitty_Blowjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    $ counter += 1
                    jump Kitty_Sex_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Kitty_Sex_Reset
                    $ action_context = "shift"
                    jump Kitty_SexAfter
                "No, get back down there.":
                    if approval_check(KittyX, 1200) or approval_check(KittyX, 500, "O"):
                        $ KittyX.change_stat("love", 200, -5)
                        $ KittyX.change_stat("obedience", 50, 3)
                        $ KittyX.change_stat("obedience", 80, 2)
                        "She grumbles but keeps moving."
                    else:
                        $ KittyX.change_face("angry", 1)
                        call Kitty_Sex_Reset
                        "She scowls at you and pulls out."
                        ch_k "Not with that attitude, mister!"
                        $ KittyX.change_stat("love", 50, -3, 1)
                        $ KittyX.change_stat("love", 80, -4, 1)
                        $ KittyX.change_stat("obedience", 30, -1, 1)
                        $ KittyX.change_stat("obedience", 50, -1, 1)
                        $ KittyX.recent_history.append("angry")
                        $ KittyX.daily_history.append("angry")
                        jump Kitty_SexAfter


        call Escalation (KittyX)

        if Round == 10:
            ch_k "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_k "Seriously, it'll be time to stop soon."


    $ KittyX.change_face("bemused", 0)
    $ Line = 0
    ch_k "Ok, [KittyX.player_petname], that's enough of that for now."

label Kitty_SexAfter:
    if not action_context:
        $ Player.sprite = 0
        $ Player.cock_position = "out"
        call Kitty_Sex_Reset

    $ KittyX.change_face("sexy")

    $ KittyX.action_counter["sex"] += 1
    $ KittyX.remaining_actions -=1
    $ KittyX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ KittyX.addiction_rate += 1
    $ KittyX.change_stat("inhibition", 30, 2)
    $ KittyX.change_stat("inhibition", 70, 1)

    call Partner_Like (KittyX, 3, 2)

    if "Kitty Sex Addict" in Achievements:
        pass

    elif KittyX.action_counter["sex"] >= 10:
        $ KittyX.SEXP += 5
        $ Achievements.append("Kitty Sex Addict")
        if not action_context:
            $ KittyX.change_face("smile", 1)
            ch_k "I just can't seem to quit you."
    elif KittyX.action_counter["sex"] == 1:
        $ KittyX.SEXP += 20
        if not action_context:
            if KittyX.love >= 500 and "unsatisfied" not in KittyX.recent_history:
                ch_k "I feel like I've been waiting[KittyX.like]a million years for that."
            elif KittyX.obedience <= 500 and Player.focus <= 20:
                $ KittyX.mouth = "sad"
                ch_k "I hope that was worth the wait."
    elif KittyX.action_counter["sex"] == 5:
        ch_k "Why did we not do this sooner?!"
    elif not action_context:
        if "unsatisfied" in KittyX.recent_history:
            $ KittyX.change_face("angry")
            $ KittyX.eyes = "side"
            ch_k "Could you have maybe paid more attention? . ."

    $ approval_bonus = 0


    call checkout
    return






label Kitty_Sex_A:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (KittyX)
    if KittyX.action_counter["anal"] >= 7:
        $ approval_bonus += 20
    elif KittyX.action_counter["anal"] >= 3:
        $ approval_bonus += 17
    elif KittyX.action_counter["anal"]:
        $ approval_bonus += 15

    if KittyX.addiction >= 75 and (KittyX.event_counter["creampied"] + KittyX.event_counter["anal_creampied"]) >=3:
        $ approval_bonus += 25
    elif KittyX.addiction >= 75:
        $ approval_bonus += 15

    if KittyX.lust > 85:
        $ approval_bonus += 10
    elif KittyX.lust > 75:
        $ approval_bonus += 5

    if KittyX.used_to_anal:
        $ approval_bonus += 10
    elif "anal" in KittyX.recent_history:
        $ approval_bonus -= 20
    elif "anal" in KittyX.daily_history:
        $ approval_bonus -= 10

    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in KittyX.traits:
        $ approval_bonus += (5*Taboo)

    if KittyX in Player.Harem or "sex friend" in KittyX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in KittyX.traits:
        $ approval_bonus -= 40
    if KittyX.event_counter["forced"] and not KittyX.Forced:
        $ approval_bonus -= 5*KittyX.event_counter["forced"]

    if Taboo and "no_taboo" in KittyX.daily_history:
        $ approval_bonus -= 10
    if "no_anal" in KittyX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_anal" in KittyX.recent_history else 0

    $ approval = approval_check(KittyX, 1550, TabM = 5)

    if action_context == "auto":
        call Kitty_Sex_Launch ("anal")
        if KittyX.PantsNum() == 5:
            "You press [KittyX.name] down onto her back, sliding her skirt up as you go."
            $ KittyX.upskirt = 1
        elif KittyX.PantsNum() > 6:
            "You press [KittyX.name] down onto her back, sliding her pants down as you do."
            $ KittyX.upskirt = 1
        elif KittyX.PantsNum() == 6:
            "You press [KittyX.name] down onto her back, sliding her shorts down as you do."
            $ KittyX.upskirt = 1
        else:
            "You press [KittyX.name] down onto her back."
        $ KittyX.SeenPanties = 1
        "You press the tip of your cock against her tight rim."
        $ KittyX.change_face("surprised", 1)

        if (KittyX.action_counter["anal"] and approval) or (approval > 1):

            $ KittyX.change_stat("obedience", 70, 3)
            $ KittyX.change_stat("inhibition", 50, 3)
            $ KittyX.change_stat("inhibition", 70, 1)
            if KittyX.used_to_anal:
                "[KittyX.name] is briefly startled, but melts into a sly smile."
                ch_k "Hmm, stick it in. . ."
            else:
                "[KittyX.name] is briefly startled, but shrugs."
                ch_k "Oookay. . ."
            jump Kitty_AnalPrep
        else:

            $ KittyX.brows = "angry"
            menu:
                ch_k "Um[KittyX.like]what are you doing back there?!"
                "Sorry, sorry! Never mind.":
                    if approval:
                        $ KittyX.change_face("sexy", 1)
                        $ KittyX.change_stat("obedience", 70, 3)
                        $ KittyX.change_stat("inhibition", 50, 3)
                        $ KittyX.change_stat("inhibition", 70, 1)
                        ch_k "Well[KittyX.like]just take it easy, ok? . ."
                        jump Kitty_AnalPrep
                    "You pull back before you really get it in."
                    $ KittyX.change_face("bemused", 1)

                    if KittyX.action_counter["anal"]:
                        ch_k "Maybe you could[KittyX.like]warn me?"
                    else:
                        ch_k "Maybe you could[KittyX.like]warn me? I don't know that I'm[KittyX.like]ready for that sort of thing. . ."
                "Just fucking.":
                    $ KittyX.change_stat("love", 80, -10, 1)
                    $ KittyX.change_stat("love", 200, -8)
                    "You press into her."
                    $ KittyX.change_stat("obedience", 70, 3)
                    $ KittyX.change_stat("inhibition", 50, 3)
                    if not approval_check(KittyX, 700, "O", TabM=1):
                        $ KittyX.change_face("angry")
                        "[KittyX.name] shoves you away and slaps you in the face."
                        ch_k "Asshole!"
                        ch_k "You need to ask nicer than that!"
                        $ KittyX.change_stat("love", 50, -10, 1)
                        $ KittyX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        call Kitty_Sex_Reset
                        $ KittyX.recent_history.append("angry")
                        $ KittyX.daily_history.append("angry")
                    else:
                        $ KittyX.change_face("sad")
                        "[KittyX.name] doesn't seem to be into this, you're lucky she's so obedient."
                        jump Kitty_AnalPrep
        return



    if not KittyX.action_counter["anal"] and "no_anal" not in KittyX.recent_history:

        $ KittyX.change_face("surprised", 1)
        $ KittyX.mouth = "kiss"
        ch_k "You want to go in the \"out\" door?!"

        if KittyX.Forced:
            $ KittyX.change_face("sad")
            ch_k "Anal? Really?"

    if not KittyX.used_to_anal and ("dildo_anal" in KittyX.daily_history or "anal" in KittyX.daily_history):

        $ KittyX.change_face("bemused", 1)
        ch_k "I'm not really over the last time, but. . ."
    elif "anal" in KittyX.recent_history:
        $ KittyX.change_face("sexy", 1)
        ch_k "Again? K."
        jump Kitty_AnalPrep


    if not KittyX.action_counter["anal"] and approval:

        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
        elif KittyX.love >= (KittyX.obedience + KittyX.inhibition):
            $ KittyX.change_face("sexy")
            $ KittyX.brows = "sad"
            $ KittyX.mouth = "smile"
            ch_k "I guess? . ."
        elif KittyX.obedience >= KittyX.inhibition:
            $ KittyX.change_face("normal")
            ch_k "Well. . ."
        elif KittyX.addiction >= 50:
            $ KittyX.change_face("manic", 1)
            ch_k "I. . . if that's how you want to do it. . . maybe?"
        else:
            $ KittyX.change_face("sad")
            $ KittyX.mouth = "smile"
            ch_k "Anything's worth a shot. . ."

    elif approval:

        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
            ch_k "You really ask a lot here. . ."
        elif not Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "I guess this is out of the way. . ."
        elif "anal" in KittyX.daily_history and not KittyX.used_to_anal:
            pass
        elif "anal" in KittyX.recent_history:
            ch_k "I guess I'm warmed up. . ."
            jump Kitty_AnalPrep
        elif "anal" in KittyX.daily_history:
            $ KittyX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",
                    "So you'd like another round?",
                    "I'm still a little sore from earlier.",
                    "Didn't get enough earlier?",
                    "You're wearing me out here!"])
            ch_k "[Line]"
        else:
            $ KittyX.change_face("sexy", 1)
            $ KittyX.ArmPose = 2
            $ Line = renpy.random.choice(["Oooh, you want some of this?",
                    "So you'd like another round?",
                    "I do have booty for days. . .",
                    "You gonna make me purr?",
                    "You wanna slide into me?"])
            ch_k "[Line]"
        $ Line = 0

    if approval >= 2:

        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("obedience", 90, 1)
            $ KittyX.change_stat("inhibition", 60, 1)
            ch_k "Ok, fine."
        elif "no_anal" in KittyX.daily_history:
            ch_k "Well, ok, I've given it some thought, fine. . ."
        else:
            $ KittyX.change_face("sexy", 1)
            $ KittyX.change_stat("love", 90, 1)
            $ KittyX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well. . . ok.",
                    "Sure!",
                    "You could, I guess.",
                    "Um, yeah.",
                    "Heh, ok, ok."])
            ch_k "[Line]"
            $ Line = 0
        $ KittyX.change_stat("obedience", 20, 1)
        $ KittyX.change_stat("obedience", 60, 1)
        $ KittyX.change_stat("inhibition", 70, 2)
        jump Kitty_AnalPrep
    else:


        $ KittyX.change_face("angry")
        if "no_anal" in KittyX.recent_history:
            ch_k "I{i}just{/i}[KittyX.like]told you \"no!\""
        elif Taboo and "no_taboo" in KittyX.daily_history and "no_anal" in KittyX.daily_history:
            ch_k "I already told you. . .not in public!"
        elif "no_anal" in KittyX.daily_history:
            ch_k "I already[KittyX.like]told you \"no.\""
        elif Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "I already told you this is too public!"
        elif not KittyX.action_counter["anal"]:
            $ KittyX.change_face("bemused")
            ch_k "I don't know that I'm. . .[KittyX.like]that kind of girl?"
        elif not KittyX.used_to_anal and "anal" not in KittyX.daily_history:
            $ KittyX.change_face("perplexed")
            ch_k "That was kind of. . . rough last time?"
        else:
            $ KittyX.change_face("bemused")
            ch_k "Maybe[KittyX.like]not right now? . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_anal" in KittyX.daily_history:
                $ KittyX.change_face("bemused")
                ch_k "It's cool."
                return
            "Maybe later?" if "no_anal" not in KittyX.daily_history:
                $ KittyX.change_face("sexy")
                ch_k "Maybe, you never know."
                $ KittyX.change_stat("love", 80, 2)
                $ KittyX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ KittyX.recent_history.append("no_taboo")
                    $ KittyX.daily_history.append("no_taboo")
                $ KittyX.recent_history.append("no_anal")
                $ KittyX.daily_history.append("no_anal")
                return
            "I bet it would feel really good. . .":
                if approval:
                    $ KittyX.change_face("sexy")
                    $ KittyX.change_stat("obedience", 90, 2)
                    $ KittyX.change_stat("obedience", 50, 2)
                    $ KittyX.change_stat("inhibition", 70, 3)
                    $ KittyX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["That's. . . true. . .",
                            "I suppose. . .",
                            "That's. . . that's a good point. . ."])
                    ch_k "[Line]"
                    $ Line = 0
                    jump Kitty_AnalPrep
                else:
                    pass
            "Just deal with it.":

                $ approval = approval_check(KittyX, 1250, "OI", TabM = 3)
                if approval > 1 or (approval and KittyX.Forced):
                    $ KittyX.change_face("sad")
                    $ KittyX.change_stat("love", 70, -5, 1)
                    $ KittyX.change_stat("love", 200, -5)
                    ch_k "Well! . . ok, fine, stick it in."
                    $ KittyX.change_stat("obedience", 80, 4)
                    $ KittyX.change_stat("inhibition", 80, 1)
                    $ KittyX.change_stat("inhibition", 60, 3)
                    $ KittyX.Forced = 1
                    jump Kitty_AnalPrep
                else:
                    $ KittyX.change_stat("love", 200, -20)
                    $ KittyX.recent_history.append("angry")
                    $ KittyX.daily_history.append("angry")


    $ KittyX.ArmPose = 1
    if "no_anal" in KittyX.daily_history:
        ch_k "Maybe[KittyX.like]take \"no\" for an answer?"
        $ KittyX.recent_history.append("angry")
        $ KittyX.daily_history.append("angry")
    elif KittyX.Forced:
        $ KittyX.change_face("angry", 1)
        ch_k "That's a bit much, even for you."
        $ KittyX.change_stat("lust", 200, 5)
        if KittyX.love > 300:
            $ KittyX.change_stat("love", 70, -2)
        $ KittyX.change_stat("obedience", 50, -2)
        $ KittyX.recent_history.append("angry")
        $ KittyX.daily_history.append("angry")
    elif Taboo:

        $ KittyX.change_face("angry", 1)
        $ KittyX.recent_history.append("no_taboo")
        $ KittyX.daily_history.append("no_taboo")
        ch_k "You're being ridiculous. That? Here?!"
        $ KittyX.change_stat("lust", 200, 5)
        $ KittyX.change_stat("obedience", 50, -3)
    elif not KittyX.used_to_anal and "anal" in KittyX.daily_history:
        $ KittyX.change_face("bemused")
        ch_k "I'm[KittyX.like]a little sore here?"
    elif KittyX.action_counter["anal"]:
        $ KittyX.change_face("sad")
        ch_k "That's[KittyX.like]totally off the table."
    else:
        $ KittyX.change_face("normal", 1)
        ch_k "Noooope."
    $ KittyX.recent_history.append("no_anal")
    $ KittyX.daily_history.append("no_anal")
    $ approval_bonus = 0
    return

label Kitty_AnalPrep:
    call Seen_First_Peen (KittyX, Partner, React=action_context)
    call Kitty_Sex_Launch ("hotdog")

    if action_context == KittyX:

        $ action_context = 0

        if KittyX.PantsNum() == 5:
            "[KittyX.name] rolls back and pulls you toward her, sliding her skirt up as she does so."
            $ KittyX.upskirt = 1
        elif KittyX.PantsNum() > 6:
            "[KittyX.name] rolls back and pulls you against her, sliding her pants off as she does so."
            $ KittyX.upskirt = 1
        elif KittyX.PantsNum() == 6:
            "[KittyX.name] rolls onto her back and pulls you against her, sliding her shorts off as she does so."
            $ KittyX.upskirt = 1
        else:
            "[KittyX.name] rolls back and pulls you toward her."
        $ KittyX.SeenPanties = 1
        "She slides the tip along her ass and seems to want you to insert it."
        menu:
            "What do you do?"
            "Go with it.":
                $ KittyX.change_stat("inhibition", 80, 3)
                $ KittyX.change_stat("inhibition", 50, 2)
                "[KittyX.name] slides it in."
            "Praise her.":
                $ KittyX.change_face("sexy", 1)
                $ KittyX.change_stat("inhibition", 80, 3)
                ch_p "Oh yeah, [KittyX.petname], let's do this."
                $ KittyX.nameCheck()
                "[KittyX.name] slides it in."
                $ KittyX.change_stat("love", 85, 1)
                $ KittyX.change_stat("obedience", 90, 1)
                $ KittyX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ KittyX.change_face("surprised")
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
        $ KittyX.underwear_pulled_down = 1
        call Kitty_First_Bottomless (1)

    elif action_context != "auto":
        call AutoStrip (KittyX)

        if Taboo:
            if KittyX.action_counter["anal"]:
                "[KittyX.name] glances around to see if anyone notices what she's doing, then presses firmly against your cock."
                "You guide your cock into place and ram it home."
            else:

                "Kitty glances around for voyeurs. . ."
                if "cockout" in Player.recent_history:
                    "[KittyX.name] slowly presses against your rigid member."
                else:
                    "[KittyX.name] hesitantly pulls down your pants and slowly presses against your rigid member."
                "You guide it into place and slide it in."
            $ KittyX.inhibition += int(Taboo/10)
            $ KittyX.lust += int(Taboo/5)
        else:
            if not KittyX.action_counter["anal"]:
                "[KittyX.name] leans back and presses against you suggestively."
                "You take careful aim and then push your cock in."
            else:
                if "cockout" in Player.recent_history:
                    "[KittyX.name] slowly presses against your rigid member."
                else:
                    "[KittyX.name] hesitantly pulls down your pants slowly presses against your rigid member."
                "You press against her rim and nudge your cock in."
    else:

        if (KittyX.PantsNum() > 6 and not KittyX.upskirt) and (KittyX.underwear and not KittyX.underwear_pulled_down):
            "You quickly pull down her pants and her [KittyX.underwear] and press against her back door."
        elif (KittyX.underwear and not KittyX.underwear_pulled_down):
            "You quickly pull down her [KittyX.underwear] and press against her back door."
        $ KittyX.upskirt = 1
        $ KittyX.underwear_pulled_down = 1
        $ KittyX.SeenPanties = 1
        call Kitty_First_Bottomless (1)

    if not KittyX.action_counter["anal"]:
        if KittyX.Forced:
            $ KittyX.change_stat("love", 90, -150)
            $ KittyX.change_stat("obedience", 70, 70)
            $ KittyX.change_stat("inhibition", 80, 40)
        else:
            $ KittyX.change_stat("love", 90, 10)
            $ KittyX.change_stat("obedience", 70, 30)
            $ KittyX.change_stat("inhibition", 80, 70)
    elif not KittyX.used_to_anal:
        if KittyX.Forced:
            $ KittyX.change_stat("love", 90, -20)
            $ KittyX.change_stat("obedience", 70, 10)
            $ KittyX.change_stat("inhibition", 80, 5)
        else:
            $ KittyX.change_stat("obedience", 70, 7)
            $ KittyX.change_stat("inhibition", 80, 5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    $ Player.cock_position = "anal"
    $ primary_action = "anal"
    $ action_speed = 1
    if Taboo:
        $ KittyX.drain_word("no_taboo")
    $ KittyX.drain_word("no_anal")
    $ KittyX.recent_history.append("anal")
    $ KittyX.daily_history.append("anal")

label Kitty_Anal_Cycle:
    while Round > 0:
        call shift_focus (KittyX)
        call Kitty_Sex_Launch ("anal")
        $ KittyX.lust_face()
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

                    call Slap_Ass (KittyX)
                    $ counter += 1
                    $ Round -= 1
                    jump Kitty_Anal_Cycle
                "Turn her Around":
                    $ KittyX.pose = "doggy" if KittyX.pose != "doggy" else "sex"
                    "You turn her around. . ."
                    jump Kitty_Anal_Cycle

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
                            if KittyX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ KittyX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (KittyX, "tired")
                        "Shift primary action":

                            if KittyX.remaining_actions and multi_action:
                                menu:
                                    "How about sex?":
                                        $ action_context = "shift"
                                        call Kitty_AnalAfter
                                        call Kitty_Sex_P
                                    "Just stick it in her pussy [[without asking].":
                                        $ action_context = "auto"
                                        call Kitty_AnalAfter
                                        call Kitty_Sex_P
                                    "Pull back to hotdog her.":
                                        $ action_context = "pullback"
                                        call Kitty_AnalAfter
                                        call Kitty_Sex_H
                                    "Never Mind":
                                        jump Kitty_Anal_Cycle
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
                                    jump Kitty_Anal_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Kitty_Anal_Cycle
                                "Never mind":
                                    jump Kitty_Anal_Cycle
                        "Just take a look at her.":
                            $ Player.cock_position = 0
                            $ action_speed = 0

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
                            jump Kitty_Anal_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Kitty_Sex_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Kitty_AnalAfter
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Kitty_Sex_Reset
                    $ Line = 0
                    jump Kitty_AnalAfter


        call shift_focus (KittyX)
        call Sex_Dialog (KittyX, Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or KittyX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (KittyX)
                if "angry" in KittyX.recent_history:
                    call Kitty_Sex_Reset
                    return
                $ KittyX.change_stat("lust", 200, 5)
                if 100 > KittyX.lust >= 70 and KittyX.session_orgasms < 2:
                    $ KittyX.recent_history.append("unsatisfied")
                    $ KittyX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Kitty_AnalAfter
                $ Line = "came"

            if KittyX.lust >= 100:

                call Girl_Cumming (KittyX)
                if action_context == "shift" or "angry" in KittyX.recent_history:
                    jump Kitty_AnalAfter

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "She's emptied you out, you'll need to take a break."
                    jump Kitty_AnalAfter
                elif "unsatisfied" in KittyX.recent_history:

                    $ Line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                    "[Line] Keep going?"
                    menu:
                        extend ""
                        "Yes, keep going for a bit." if Player.semen:
                            $ Line = "You get back into it"
                            jump Kitty_Anal_Cycle
                        "No, I'm done." if Player.semen:
                            "You pull back."
                            jump Kitty_AnalAfter
                        "No, I'm spent." if not Player.semen:
                            "You pull back."
                            jump Kitty_AnalAfter
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if KittyX.SEXP >= 100 or approval_check(KittyX, 1200, "LO"):
            pass
        elif counter == (5 + KittyX.action_counter["anal"]):
            $ KittyX.brows = "confused"
            if KittyX.used_to_anal:
                ch_k "So are we[KittyX.like]getting close here?"
            else:
                ch_k "So are we[KittyX.like]getting close here? This is not super pleasant. . ."
        elif counter == (10 + KittyX.action_counter["anal"]):
            $ KittyX.brows = "angry"
            ch_k "I'm . . .getting . . kinda tired. . . of this. . ."
            menu:
                ch_k "Can we. . . do something. . . else?"
                "How about a BJ?" if KittyX.remaining_actions and multi_action:
                    if KittyX.action_counter["anal"] >= 5 and KittyX.action_counter["blowjob"] >= 10 and KittyX.SEXP >= 50:
                        $ action_context = "shift"
                        call Kitty_AnalAfter
                        call Kitty_Blowjob
                    else:
                        ch_k "No thanks, [KittyX.player_petname]. Maybe a Handy instead?"
                        $ action_context = "shift"
                        call Kitty_AnalAfter
                        call Kitty_HJ_Prep
                "How about a Handy?" if KittyX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Kitty_AnalAfter
                    call Kitty_Handjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    $ counter += 1
                    jump Kitty_Anal_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Kitty_Sex_Reset
                    $ action_context = "shift"
                    jump Kitty_AnalAfter
                "No, get back down there.":
                    if approval_check(KittyX, 1200) or approval_check(KittyX, 500, "O"):
                        $ KittyX.change_stat("love", 200, -5)
                        $ KittyX.change_stat("obedience", 50, 3)
                        $ KittyX.change_stat("obedience", 80, 2)
                        "She grumbles but keeps moving."
                    else:
                        $ KittyX.change_face("angry", 1)
                        call Kitty_Sex_Reset
                        "She scowls at you and pulls out."
                        ch_k "Not with that attitude, mister!"
                        $ KittyX.change_stat("love", 50, -3, 1)
                        $ KittyX.change_stat("love", 80, -4, 1)
                        $ KittyX.change_stat("obedience", 30, -1, 1)
                        $ KittyX.change_stat("obedience", 50, -1, 1)
                        $ KittyX.recent_history.append("angry")
                        $ KittyX.daily_history.append("angry")
                        jump Kitty_AnalAfter


        if Round == 10:
            ch_k "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_k "Seriously, it'll be time to stop soon."


    $ KittyX.change_face("bemused", 0)
    $ Line = 0
    ch_k "Ok, [KittyX.player_petname], that's enough of that for now."

label Kitty_AnalAfter:
    if not action_context:
        $ Player.sprite = 0
        $ Player.cock_position = "out"
        call Kitty_Sex_Reset

    $ KittyX.change_face("sexy")

    $ KittyX.action_counter["anal"] += 1
    $ KittyX.remaining_actions -=1
    $ KittyX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ KittyX.addiction_rate += 1
    $ KittyX.change_stat("inhibition", 30, 3)
    $ KittyX.change_stat("inhibition", 70, 1)

    if Partner == "Emma":
        call Partner_Like (KittyX, 4, 3)
    else:
        call Partner_Like (KittyX, 3, 3)

    if "Kitty Anal Addict" in Achievements:
        pass

    elif KittyX.action_counter["anal"] >= 10:
        $ KittyX.SEXP += 7
        $ Achievements.append("Kitty Anal Addict")
        if not action_context:
            $ KittyX.change_face("bemused", 1)
            ch_k "I didn't think I'd love this so much!"
    elif KittyX.action_counter["anal"] == 1:
        $ KittyX.SEXP += 25
        if not action_context:
            if KittyX.love >= 500 and "unsatisfied" not in KittyX.recent_history:
                ch_k "Anal. . . huh, who knew?"
            elif KittyX.obedience <= 500 and Player.focus <= 20:
                $ KittyX.mouth = "sad"
                ch_k "Ouch."
                ch_k "I guess you got what you needed?"
    elif KittyX.action_counter["anal"] == 5:
        ch_k "I'm really starting to love this."
    elif not action_context:
        if "unsatisfied" in KittyX.recent_history:
            $ KittyX.change_face("angry")
            $ KittyX.eyes = "side"
            ch_k "Hmm, you seemed to get more out of that than me. . ."

    $ approval_bonus = 0


    call checkout
    return








label Kitty_Sex_H:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (KittyX)
    if KittyX.action_counter["hotdog"] >= 3:
        $ approval_bonus += 10
    elif KittyX.action_counter["hotdog"]:
        $ approval_bonus += 5

    if KittyX.lust > 85:
        $ approval_bonus += 10
    elif KittyX.lust > 75:
        $ approval_bonus += 5
    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in KittyX.traits:
        $ approval_bonus += (3*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in KittyX.traits:
        $ approval_bonus -= 40
    if KittyX.event_counter["forced"] and not KittyX.Forced:
        $ approval_bonus -= 5*KittyX.event_counter["forced"]

    if Taboo and "no_taboo" in KittyX.daily_history:
        $ approval_bonus -= 10

    if "no_hotdog" in KittyX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_hotdog" in KittyX.recent_history else 0

    $ approval = approval_check(KittyX, 1000, TabM = 3)

    if action_context == "auto":
        call Kitty_Sex_Launch ("hotdog")
        "You press [KittyX.name] down onto her back and press your cock against her."
        $ KittyX.change_face("surprised", 1)

        if (KittyX.action_counter["hotdog"] and approval) or (approval > 1):
            "[KittyX.name] is briefly startled, but melts into a sly smile."
            $ KittyX.change_face("sexy")
            $ KittyX.change_stat("obedience", 70, 3)
            $ KittyX.change_stat("inhibition", 50, 3)
            $ KittyX.change_stat("inhibition", 70, 1)
            ch_k "Hmm, I've apparently got someone's attention. . ."
            jump Kitty_HotdogPrep
        else:
            $ KittyX.brows = "angry"
            menu:
                ch_k "Hmm, kinda rude, [KittyX.player_petname]."
                "Sorry, sorry! Never mind.":
                    if approval:
                        $ KittyX.change_face("sexy", 1)
                        $ KittyX.change_stat("obedience", 70, 3)
                        $ KittyX.change_stat("inhibition", 50, 3)
                        $ KittyX.change_stat("inhibition", 70, 1)
                        ch_k "I guess it doesn't feel so bad. . ."
                        jump Kitty_HotdogPrep
                    "You pull back from her."
                    $ KittyX.change_face("bemused", 1)
                    ch_k "Thanks, not that it's {i}so{/i} bad, just maybe ask first?"
                "You'll see.":
                    $ KittyX.change_stat("love", 80, -10, 1)
                    $ KittyX.change_stat("love", 200, -8)
                    "You grind against her crotch."
                    $ KittyX.change_stat("obedience", 70, 3)
                    $ KittyX.change_stat("inhibition", 50, 3)
                    if not approval_check(KittyX, 500, "O", TabM=1):
                        $ KittyX.change_face("angry")
                        "[KittyX.name] shoves you away."
                        ch_k "Jerk!"
                        ch_k "I'm not into that!"
                        $ KittyX.change_stat("love", 50, -10, 1)
                        $ KittyX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        call Kitty_Sex_Reset
                        $ KittyX.recent_history.append("angry")
                        $ KittyX.daily_history.append("angry")
                    else:
                        $ KittyX.change_face("sad")
                        "[KittyX.name] doesn't seem to be into this, but she knows her place."
                        jump Kitty_HotdogPrep
        return



    if not KittyX.action_counter["hotdog"] and "no_hotdog" not in KittyX.recent_history:

        $ KittyX.change_face("surprised", 1)
        $ KittyX.mouth = "kiss"
        ch_k "So, just grinding against me?"

        if KittyX.Forced:
            $ KittyX.change_face("sad")
            ch_k ". . . That's it?"


    if not KittyX.action_counter["hotdog"] and approval:

        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
        elif KittyX.love >= (KittyX.obedience + KittyX.inhibition):
            $ KittyX.change_face("sexy")
            $ KittyX.brows = "sad"
            $ KittyX.mouth = "smile"
            ch_k "It does look a bit swolen. . ."
        elif KittyX.obedience >= KittyX.inhibition:
            $ KittyX.change_face("normal")
            ch_k "If you want. . ."
        elif KittyX.addiction >= 50:
            $ KittyX.change_face("manic", 1)
            ch_k "Hmmm. . ."
        else:
            $ KittyX.change_face("sad")
            $ KittyX.mouth = "smile"
            ch_k "Hmm, you look ready to go. . ."

    elif approval:

        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("love", 70, -3, 1)
            $ KittyX.change_stat("love", 20, -2, 1)
            ch_k "That's {i}all{/i} you want?"
        elif not Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "I guess this is a better location . ."
        elif "hotdog" in KittyX.recent_history:
            $ KittyX.change_face("sexy", 1)
            ch_k "Again? Ok."
            jump Kitty_HotdogPrep
        elif "hotdog" in KittyX.daily_history:
            $ KittyX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",
                    "So you'd like another round?",
                    "You're really digging this. . .",
                    "Are you sure that's all you want?"])
            ch_k "[Line]"
        else:
            $ KittyX.change_face("sexy", 1)
            $ KittyX.ArmPose = 2
            $ Line = renpy.random.choice(["Oooh, you want some of this?",
                    "So you'd like another round?",
                    "You're really digging this. . .",
                    "You want another rub?"])
            ch_k "[Line]"
        $ Line = 0

    if approval >= 2:

        if KittyX.Forced:
            $ KittyX.change_face("sad")
            $ KittyX.change_stat("obedience", 80, 1)
            $ KittyX.change_stat("inhibition", 60, 1)
            ch_k "Ok, fine."
        elif "no_hotdog" in KittyX.daily_history:
            ch_k "Well, I guess it's not so bad. . ."
        else:
            $ KittyX.change_face("sexy", 1)
            $ KittyX.change_stat("love", 80, 1)
            $ KittyX.change_stat("inhibition", 50, 2)
            $ Line = renpy.random.choice(["Well, sure, give it a rub.",
                    "Well. . . ok.",
                    "Sure!",
                    "I guess we could do that.",
                    "Um, yeah.",
                    "Heh, ok, ok."])
            ch_k "[Line]"
            $ Line = 0
        $ KittyX.change_stat("obedience", 60, 1)
        $ KittyX.change_stat("inhibition", 70, 2)
        jump Kitty_HotdogPrep
    else:


        $ KittyX.change_face("angry")
        if "no_hotdog" in KittyX.recent_history:
            ch_k "I{i}just{/i}[KittyX.like]told you \"no!\""
        elif Taboo and "no_taboo" in KittyX.daily_history and "no_hotdog" in KittyX.daily_history:
            ch_k "I{i}just{/i}[KittyX.like]told, not in public!"
        elif "no_hotdog" in KittyX.daily_history:
            ch_k "I{i}just{/i}[KittyX.like]told you \"no\" earlier!"
        elif Taboo and "no_taboo" in KittyX.daily_history:
            ch_k "I{i}just{/i}[KittyX.like]told you, not in public!"
        elif not KittyX.action_counter["hotdog"]:
            $ KittyX.change_face("bemused")
            ch_k "That's kinda hot, [KittyX.player_petname]. . ."
        else:
            $ KittyX.change_face("bemused")
            ch_k "Not. . . now. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_hotdog" in KittyX.daily_history:
                $ KittyX.change_face("bemused")
                ch_k "No problem."
                return
            "Maybe later?" if "no_hotdog" not in KittyX.daily_history:
                $ KittyX.change_face("sexy")
                ch_k "Yeah, maybe, [KittyX.player_petname]."
                $ KittyX.change_stat("love", 80, 1)
                $ KittyX.change_stat("inhibition", 50, 1)
                if Taboo:
                    $ KittyX.recent_history.append("no_taboo")
                    $ KittyX.daily_history.append("no_taboo")
                $ KittyX.recent_history.append("no_hotdog")
                $ KittyX.daily_history.append("no_hotdog")
                return
            "You might like it. . .":
                if approval:
                    $ KittyX.change_face("sexy")
                    $ KittyX.change_stat("obedience", 60, 2)
                    $ KittyX.change_stat("inhibition", 50, 2)
                    $ Line = renpy.random.choice(["Well, sure, ok.",
                            "I suppose. . .",
                            "That's. . . that's a good point. . ."])
                    ch_k "[Line]"
                    $ Line = 0
                    jump Kitty_HotdogPrep
                else:
                    pass
            "Just deal with it.":

                $ approval = approval_check(KittyX, 350, "OI", TabM = 3)
                if approval > 1 or (approval and KittyX.Forced):
                    $ KittyX.change_face("sad")
                    $ KittyX.change_stat("love", 70, -2, 1)
                    $ KittyX.change_stat("love", 200, -2)
                    ch_k "Ok, fine. Whatever."
                    $ KittyX.change_stat("obedience", 80, 4)
                    $ KittyX.change_stat("inhibition", 60, 2)
                    $ KittyX.Forced = 1
                    jump Kitty_HotdogPrep
                else:
                    $ KittyX.change_stat("love", 200, -10)
                    $ KittyX.recent_history.append("angry")
                    $ KittyX.daily_history.append("angry")


    $ KittyX.ArmPose = 1

    if "no_hotdog" in KittyX.daily_history:
        ch_k "I'm just not into that."
        $ KittyX.recent_history.append("angry")
        $ KittyX.daily_history.append("angry")
    if KittyX.Forced:
        $ KittyX.change_face("angry", 1)
        ch_k "Yeah, not happening."
        $ KittyX.change_stat("lust", 200, 5)
        if KittyX.love > 300:
            $ KittyX.change_stat("love", 70, -1)
        $ KittyX.change_stat("obedience", 50, -1)
        $ KittyX.recent_history.append("angry")
        $ KittyX.daily_history.append("angry")
    elif Taboo:
        $ KittyX.change_face("angry", 1)
        $ KittyX.recent_history.append("no_taboo")
        $ KittyX.daily_history.append("no_taboo")
        ch_k "[KittyX.Like]not here though?"
        $ KittyX.change_stat("lust", 200, 5)
        $ KittyX.change_stat("obedience", 50, -3)
    elif KittyX.action_counter["hotdog"]:
        $ KittyX.change_face("sad")
        ch_k "Yeah, not again."
    else:
        $ KittyX.change_face("normal", 1)
        ch_k "Noooop."
    $ KittyX.recent_history.append("no_hotdog")
    $ KittyX.daily_history.append("no_hotdog")
    $ approval_bonus = 0
    return

label Kitty_HotdogPrep:
    call Seen_First_Peen (KittyX, Partner, React=action_context)
    call Kitty_Sex_Launch ("hotdog")


    if action_context == KittyX:

        $ action_context = 0
        "[KittyX.name] rolls back and pulls you toward her, rubbing her pussy against your cock."
        menu:
            "What do you do?"
            "Go with it.":
                $ KittyX.change_stat("inhibition", 80, 3)
                $ KittyX.change_stat("inhibition", 50, 2)
                "[KittyX.name] keeps grinding."
            "Praise her.":
                $ KittyX.change_face("sexy", 1)
                $ KittyX.change_stat("inhibition", 80, 3)
                ch_p "Oh yeah, [KittyX.petname], let's do this."
                $ KittyX.nameCheck()
                "[KittyX.name] keeps grinding."
                $ KittyX.change_stat("love", 85, 1)
                $ KittyX.change_stat("obedience", 90, 1)
                $ KittyX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ KittyX.change_face("surprised")
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
    elif action_context != "auto":


        if Taboo:
            if KittyX.action_counter["hotdog"]:
                "[KittyX.name] glances around to see if anyone notices what she's doing, then presses firmly against your cock."
            else:

                "[KittyX.name] glances around for voyeurs. . ."
                if "cockout" in Player.recent_history:
                    "[KittyX.name] slowly presses against your rigid member."
                else:
                    "[KittyX.name] hesitantly pulls down your pants and slowly presses against your rigid member."
            $ KittyX.inhibition += int(Taboo/10)
            $ KittyX.lust += int(Taboo/5)
        else:
            if "cockout" in Player.recent_history:
                "[KittyX.name] slowly presses against your rigid member."
            else:
                "[KittyX.name] hesitantly pulls down your pants slowly presses against your rigid member."
    else:

        "You press yourself against her mound."

    if not KittyX.action_counter["hotdog"]:
        if KittyX.Forced:
            $ KittyX.change_stat("love", 90, -5)
            $ KittyX.change_stat("obedience", 70, 20)
            $ KittyX.change_stat("inhibition", 80, 10)
        else:
            $ KittyX.change_stat("love", 90, 20)
            $ KittyX.change_stat("obedience", 70, 20)
            $ KittyX.change_stat("inhibition", 80, 20)


    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    $ primary_action = "hotdog"
    $ action_speed = 1
    if Taboo:
        $ KittyX.drain_word("no_taboo")
    $ KittyX.drain_word("no_hotdog")
    $ KittyX.recent_history.append("hotdog")
    $ KittyX.daily_history.append("hotdog")

label Kitty_Hotdog_Cycle:
    while Round > 0:
        call shift_focus (KittyX)
        call Kitty_Sex_Launch ("hotdog")
        $ KittyX.lust_face()
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

                    call Slap_Ass (KittyX)
                    $ counter += 1
                    $ Round -= 1
                    jump Kitty_Hotdog_Cycle
                "Turn her Around":
                    $ KittyX.pose = "doggy" if KittyX.pose != "doggy" else "sex"
                    "You turn her around. . ."
                    jump Kitty_Hotdog_Cycle

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
                            if KittyX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ KittyX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (KittyX, "tired")
                        "Shift primary action":

                            if KittyX.remaining_actions and multi_action:
                                menu:
                                    "How about sex?":
                                        $ action_context = "shift"
                                        call Kitty_HotdogAfter
                                        call Kitty_Sex_P
                                    "Just stick it in her pussy [[without asking].":
                                        $ action_context = "auto"
                                        call Kitty_HotdogAfter
                                        call Kitty_Sex_P
                                    "How about anal?":
                                        $ action_context = "shift"
                                        call Kitty_HotdogAfter
                                        call Kitty_Sex_A
                                    "Just stick it in her ass [[without asking].":
                                        $ action_context = "auto"
                                        call Kitty_HotdogAfter
                                        call Kitty_Sex_A
                                    "Never Mind":
                                        jump Kitty_Hotdog_Cycle
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
                                    jump Kitty_Hotdog_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Kitty_Hotdog_Cycle
                                "Never mind":
                                    jump Kitty_Hotdog_Cycle
                        "Just take a look at her.":
                            $ Player.cock_position = 0
                            $ action_speed = 0

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
                            jump Kitty_Hotdog_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Kitty_Sex_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Kitty_HotdogAfter
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Kitty_Sex_Reset
                    $ Line = 0
                    jump Kitty_HotdogAfter


        call shift_focus (KittyX)
        call Sex_Dialog (KittyX, Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or KittyX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (KittyX)
                if "angry" in KittyX.recent_history:
                    call Kitty_Sex_Reset
                    return
                $ KittyX.change_stat("lust", 200, 5)
                if 100 > KittyX.lust >= 70 and KittyX.session_orgasms < 2:
                    $ KittyX.recent_history.append("unsatisfied")
                    $ KittyX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Kitty_HotdogAfter
                $ Line = "came"

            if KittyX.lust >= 100:

                call Girl_Cumming (KittyX)
                if action_context == "shift" or "angry" in KittyX.recent_history:
                    jump Kitty_HotdogAfter

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "She's emptied you out, you'll need to take a break."
                    jump Kitty_HotdogAfter
                elif "unsatisfied" in KittyX.recent_history:

                    $ Line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                    "[Line] Keep going?"
                    menu:
                        extend ""
                        "Yes, keep going for a bit." if Player.semen:
                            $ Line = "You get back into it"
                            jump Kitty_Hotdog_Cycle
                        "No, I'm done." if Player.semen:
                            "You pull back."
                            jump Kitty_HotdogAfter
                        "No, I'm spent." if not Player.semen:
                            "You pull back."
                            jump Kitty_HotdogAfter
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if KittyX.SEXP >= 100 or approval_check(KittyX, 1200, "LO"):
            pass
        elif counter == (5 + KittyX.action_counter["hotdog"]):
            $ KittyX.brows = "confused"
            ch_k "Are you getting close here?"
        elif counter == (10 + KittyX.action_counter["hotdog"]):
            $ KittyX.brows = "angry"
            menu:
                ch_k "This is getting a bit dull."
                "How about a BJ?" if KittyX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Kitty_HotdogAfter
                    call Kitty_Blowjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    $ counter += 1
                    jump Kitty_Hotdog_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Kitty_Sex_Reset
                    $ action_context = "shift"
                    jump Kitty_HotdogAfter
                "No, get back down there.":
                    if approval_check(KittyX, 1200) or approval_check(KittyX, 500, "O"):
                        $ KittyX.change_stat("love", 200, -5)
                        $ KittyX.change_stat("obedience", 50, 3)
                        $ KittyX.change_stat("obedience", 80, 2)
                        "She grumbles but keeps moving."
                    else:
                        $ KittyX.change_face("angry", 1)
                        call Kitty_Sex_Reset
                        "She scowls at you and pulls away."
                        ch_k "Not with that attitude, mister!"
                        $ KittyX.change_stat("love", 50, -3, 1)
                        $ KittyX.change_stat("love", 80, -4, 1)
                        $ KittyX.change_stat("obedience", 30, -1, 1)
                        $ KittyX.change_stat("obedience", 50, -1, 1)
                        $ KittyX.recent_history.append("angry")
                        $ KittyX.daily_history.append("angry")
                        jump Kitty_HotdogAfter


        call Escalation (KittyX)

        if Round == 10:
            ch_k "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_k "Seriously, it'll be time to stop soon."


    $ KittyX.change_face("bemused", 0)
    $ Line = 0
    ch_k "Ok, [KittyX.player_petname], that's enough of that for now."

label Kitty_HotdogAfter:
    if not action_context:
        $ Player.sprite = 0
        $ Player.cock_position = "out"
        call Kitty_Sex_Reset

    $ KittyX.change_face("sexy")

    $ KittyX.action_counter["hotdog"] += 1
    $ KittyX.remaining_actions -=1
    $ KittyX.addiction_rate += 1
    if "addictive" in Player.traits:
        $ KittyX.addiction_rate += 1
    $ KittyX.change_stat("inhibition", 30, 1)
    $ KittyX.change_stat("inhibition", 70, 1)

    call Partner_Like (KittyX, 2)

    if KittyX.action_counter["hotdog"] == 10:
        $ KittyX.SEXP += 5
    elif KittyX.action_counter["hotdog"] == 1:
        $ KittyX.SEXP += 10
        if not action_context:
            if KittyX.love >= 500 and "unsatisfied" not in KittyX.recent_history:
                ch_k "I. . . liked that a lot."
            elif KittyX.obedience <= 500 and Player.focus <= 20:
                $ KittyX.mouth = "sad"
                ch_k "Well, did that work for you?"
    elif KittyX.action_counter["hotdog"] == 5:
        ch_k "I'm surprised how much I enjoy this."
    elif not action_context:
        if "unsatisfied" in KittyX.recent_history:
            $ KittyX.change_face("angry")
            $ KittyX.eyes = "side"
            ch_k "I didn't get much out of that. . ."

    $ approval_bonus = 0


    call checkout
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
