
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
    elif Act == "kissing":
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

label Rogue_SexMenu:
    call shift_focus (RogueX)
    $ primary_action = 0
    $ offhand_action = 0
    $ girl_offhand_action = 0
    $ action_context = 0
    call Rogue_Hide
    $ RogueX.ArmPose = 1
    call set_the_scene (1, 0, 0, 0, 1)

    if not Player.semen:
        "You're a little out of juice at the moment, you might want to wait a bit."
    if Player.focus >= 95:
        "You're practically buzzing, the slightest breeze could set you off."
    if not RogueX.remaining_actions:
        "[RogueX.name]'s looking a bit tired out, maybe let her rest a bit."

    if "caught" in RogueX.recent_history or "angry" in RogueX.recent_history:
        if RogueX.location == bg_current:
            ch_r "I don't want to deal with you right now."
        $ RogueX.change_outfit(Changed=0)
        $ RogueX.DrainWord("caught",1,0)
        return

    if Round < 5:
        ch_r "We've been at it for a while now, let's take a breather."
        return

    menu Rogue_SMenu:
        ch_r "So what would you like to do?"
        "Do you want to make out?":
            if RogueX.remaining_actions:
                call Makeout (RogueX)
            else:
                ch_r "Sorry, [RogueX.player_petname], but I'm a bit worn out."
        "Could I touch you?":

            if RogueX.remaining_actions:
                $ RogueX.mouth = "smile"
                menu:
                    ch_r "Well where exactly were you interested in touching, [RogueX.player_petname]?"
                    "Could I give you a massage?":
                        call Massage (RogueX)
                    "Your breasts?":
                        call Rogue_Fondle_Breasts
                    "Suck your breasts?" if RogueX.remaining_actions and RogueX.action_counter["suck_breasts"]:
                        call Rogue_Suck_Breasts
                    "Your thighs?" if RogueX.remaining_actions:
                        call Rogue_Fondle_Thighs
                    "Your pussy?" if RogueX.remaining_actions:
                        call Rogue_Fondle_Pussy
                    "Lick your pussy?" if RogueX.remaining_actions and RogueX.action_counter["eat_pussy"]:
                        call Rogue_Lick_Pussy
                    "Your Ass?":
                        call Rogue_Fondle_Ass
                    "Never mind [[something else]":
                        jump Rogue_SMenu
            else:
                ch_r "That sounds lovely, [RogueX.player_petname], but I'm a bit worn out."
        "Could you take care of something for me? [[Your dick, you mean your dick]":

            if Player.semen and RogueX.remaining_actions:
                menu:
                    ch_r "What did you have in mind, [RogueX.player_petname]?"
                    "Could you give me a handjob?":
                        call Rogue_Handjob
                    "Could you give me a titjob?":
                        call Rogue_Titjob
                    "Could you suck my cock?":
                        call Rogue_Blowjob
                    "Could use your feet?":
                        call Rogue_Footjob
                    "Never mind [[something else]":
                        jump Rogue_SMenu
            elif not RogueX.remaining_actions:
                ch_r "Sorry [RogueX.player_petname], I'm a bit worn out."
            else:
                "You really don't have it in you, maybe take a break."
        "Could you put on a show for me?":

            menu:
                ch_r "What sort of show were you expecting?"
                "Dance for me?":
                    if RogueX.remaining_actions:
                        call Group_Strip (RogueX)
                    else:
                        ch_r "Sorry [RogueX.player_petname], I'm a bit worn out."
                "Could you undress for me?":

                    call Girl_Undress (RogueX)

                "You've got a little something. . . [[clean-up]" if RogueX.Spunk:
                    ch_r "Oh?"
                    call Girl_Cleanup (RogueX, "ask")
                "Could I watch you get yourself off? [[masturbate]":

                    if RogueX.remaining_actions:
                        call Rogue_Masturbate
                    else:
                        ch_r "Sorry [RogueX.player_petname], I'm a bit worn out."

                "Maybe make out with [KittyX.name]?" if KittyX.location == bg_current:
                    call LesScene (RogueX)
                "Maybe make out with [EmmaX.name]?" if EmmaX.location == bg_current:
                    call LesScene (RogueX)
                "Maybe make out with [LauraX.name]?" if LauraX.location == bg_current:
                    call LesScene (RogueX)
                "Maybe make out with [JeanX.name]?" if JeanX.location == bg_current:
                    call LesScene (RogueX)
                "Maybe make out with [StormX.name]?" if StormX.location == bg_current:
                    call LesScene (RogueX)
                "Maybe make out with [JubesX.name]?" if JubesX.location == bg_current:
                    call LesScene (RogueX)
                "Never mind [[something else]":



                    jump Rogue_SMenu
        "Could we maybe?. . . [[fuck]":

            if RogueX.remaining_actions:
                menu:
                    "What did you want to do?"
                    "Turn around, I've got something in mind. . .":
                        if Player.semen:
                            call Rogue_Sex_H
                        else:
                            "The spirit is apparently willing, but the flesh is spongy and bruised."
                    "Fuck your pussy.":
                        if Player.semen:
                            call Rogue_Sex_P
                        else:
                            "The spirit is apparently willing, but the flesh is spongy and bruised."
                    "Fuck your ass.":
                        if Player.semen:
                            call Rogue_Sex_A
                        else:
                            "The spirit is apparently willing, but the flesh is spongy and bruised."
                    "How about some toys? [[Pussy]":
                        call Rogue_Dildo_Pussy
                    "How about some toys? [[Anal]":
                        call Rogue_Dildo_Ass
                    "Never mind [[something else]":
                        jump Rogue_SMenu
            else:
                ch_r "Sorry [RogueX.player_petname], I'm a bit worn out."

        "Hey, do you want in on this? [[Threesome]" if not Partner:
            call Sex_Menu_Threesome (RogueX)
            jump Rogue_SMenu

        "Hey, [Partner.name]? [[Switch lead]" if Partner:
            call expression Partner.Tag + "_SexAct" pass ("switch")
            return

        "Cheat Menu" if config.developer:
            call Cheat_Menu (RogueX)
        "Never mind. [[End]":

            if RogueX.lust >= 50 or RogueX.addiction >= 50:
                $ RogueX.change_face("sad")
                if RogueX.remaining_actions and RogueX.SEXP >= 15 and Round > 20:
                    if "round2" not in RogueX.recent_history:
                        ch_r "Are you sure, [RogueX.player_petname]? I could really use some company."
                        $ RogueX.change_stat("inhibition", 30, 2)
                        $ RogueX.change_stat("inhibition", 50, 1)
                    elif RogueX.addiction >= 50:
                        ch_r "I still need a little. . . contact."
                    else:
                        ch_r "Don't leave my hang'in, [RogueX.player_petname]."
                    menu:
                        extend ""
                        "Yeah, I'm done for now." if Player.semen and "round2" not in RogueX.recent_history:
                            if "unsatisfied" in RogueX.recent_history and not RogueX.session_orgasms:
                                $ RogueX.change_face("angry")
                                $ RogueX.eyes = "side"
                                $ RogueX.change_stat("love", 70, -2)
                                $ RogueX.change_stat("love", 90, -4)
                                $ RogueX.change_stat("obedience", 30, 2)
                                $ RogueX.change_stat("obedience", 70, 1)
                                ch_r "Way to leave a girl in the lurch. . ."
                            else:
                                $ RogueX.change_face("bemused", 1)
                                $ RogueX.change_stat("obedience", 50, 2)
                                ch_r "Well, you did at least do your part. . ."
                        "I gave it a shot." if "round2" in RogueX.recent_history:
                            if "unsatisfied" in RogueX.recent_history and not RogueX.session_orgasms:
                                $ RogueX.change_face("angry")
                                $ RogueX.eyes = "side"
                                ch_r "Way to leave a girl in the lurch. . ."
                            else:
                                $ RogueX.change_face("bemused", 1)
                                ch_r "Well, fair enough. . ."
                        "Hey, I did my part." if RogueX.session_orgasms > 2:
                            $ RogueX.change_face("sly", 1)
                            ch_r "I guess you did at that. . ."
                        "I'm tapped out for the moment, let's try again later." if not Player.semen:
                            $ RogueX.change_face("normal")
                            ch_r "Huh, can't be helped, I s'pose."
                        "Ok, we can try something else." if multi_action and "round2" not in RogueX.recent_history:
                            $ RogueX.change_face("smile")
                            $ RogueX.change_stat("love", 70, 2)
                            $ RogueX.change_stat("love", 90, 1)
                            ch_r "Mmmm. . ."
                            $ RogueX.recent_history.append("round2")
                            $ RogueX.daily_history.append("round2")
                            jump Rogue_SexMenu
                        "Again? Ok, fine." if multi_action and "round2" in RogueX.recent_history:
                            $ RogueX.change_face("sly")
                            ch_r "Yeah, again. . ."
                            jump Rogue_SexMenu
                else:

                    $ RogueX.change_face("bemused", 1)
                    ch_r "I guess I'm a bit tuckered out too, [RogueX.player_petname]. I guess we can take a breather."
                    $ RogueX.change_stat("inhibition", 30, 2)
                    $ RogueX.change_stat("inhibition", 50, 1)
            else:
                ch_r "Huh? Ok."
            $ RogueX.change_face()
            call Sex_Over
            return
    if RogueX.location != bg_current:
        call set_the_scene
        call Trig_Reset
        return
    if not multi_action:
        $ RogueX.session_orgasms = 0
        call Trig_Reset
        call set_the_scene
        ch_r "That's it. . . for now."
        return
    call GirlsAngry
    jump Rogue_SexMenu





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
    if "exhibitionist" in RogueX.Traits:
        $ approval_bonus += (3*Taboo)
    if RogueX in Player.Harem or "sex friend" in RogueX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in RogueX.Traits:
        $ approval_bonus -= 40
    if RogueX.event_counter["forced"] and not RogueX.Forced:
        $ approval_bonus -= 5*RogueX.event_counter["forced"]

    $ Approval = ApprovalCheck(RogueX, 1200, TabM = 2)

    $ RogueX.DrainWord("unseen",1,0)

    if action_context == "join":
        if Approval > 1 or (Approval and RogueX.lust >= 50):
            $ Player.AddWord(1,"join")
            menu:
                extend ""
                "Would you like some help? I could lend some helping hands. . ." if Player.semen and RogueX.remaining_actions:
                    $ RogueX.change_stat("love", 90, 1)
                    $ RogueX.change_stat("obedience", 50, 2)
                    $ RogueX.change_face("sexy")
                    ch_r "Well, [RogueX.player_petname], I suppose I could use some help with these. . ."
                    $ RogueX.change_stat("obedience", 70, 2)
                    $ RogueX.change_stat("inhibition", 70, 1)
                    $ offhand_action = "fondle_breasts"
                    $ RogueX.action_counter["masturbation"] += 1
                    jump Rogue_M_Cycle
                "Would you like some help? I could. . . up to you, I guess." if Player.semen and RogueX.remaining_actions:
                    $ RogueX.change_stat("love", 70, 2)
                    $ RogueX.change_stat("love", 90, 1)
                    $ RogueX.change_face("sexy")
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
                    $ RogueX.change_face("sexy")
                    ch_r "Well what did you have in mind?"
                    $ renpy.pop_call()
                    return
                "You look like you have things well in hand. . .":
                    if RogueX.lust >= 50:
                        $ RogueX.change_stat("love", 70, 2)
                        $ RogueX.change_stat("love", 90, 1)
                        $ RogueX.change_face("sexy")
                        ch_r "Well, [RogueX.player_petname], I suppose I do at that . ."
                        $ RogueX.change_stat("obedience", 80, 3)
                        $ RogueX.change_stat("inhibition", 80, 5)
                        jump Rogue_M_Cycle
                    elif ApprovalCheck(RogueX, 1000):
                        $ RogueX.change_face("sly")
                        ch_r "Well I did, but I think I've got it taken care of for now. . ."
                    else:
                        $ RogueX.change_face("angry")
                        ch_r "Well I did, but now you've blown the mood."


        $ RogueX.ArmPose = 1
        $ RogueX.change_outfit(Changed=0)
        $ RogueX.remaining_actions -= 1
        $ Player.change_stat("focus", 50, 30)
        call Checkout (1)
        $ Line = 0
        $ action_context = 0
        $ renpy.pop_call()
        if Approval:
            $ RogueX.change_face("bemused", 2)
            if bg_current == "bg_rogue":
                ch_r "So what did you come over for anyway, [RogueX.player_petname]?"
            else:
                ch_r "So . . . fancy bumping into you here, [RogueX.player_petname]. . ."
            $ RogueX.blushing = 1
        else:
            $ RogueX.change_stat("love", 200, -5)
            $ RogueX.change_face("angry")
            $ RogueX.recent_history.append("angry")
            $ RogueX.daily_history.append("angry")
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
        if Approval > 2:
            if RogueX.PantsNum() == 5:
                "[RogueX.name]'s hand snakes down her body, and hikes up her skirt."
                $ RogueX.Upskirt = 1
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
                    $ RogueX.change_face("surprised")
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
        $ RogueX.change_face("surprised", 1)
        $ RogueX.mouth = "kiss"
        ch_r "You want me to get myself off, while you watch?"
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            ch_r "So you just want to watch then?"



    if not RogueX.action_counter["masturbation"] and Approval:
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
        elif RogueX.love >= (RogueX.obedience + RogueX.inhibition):
            $ RogueX.change_face("sexy")
            $ RogueX.brows = "sad"
            $ RogueX.mouth = "smile"
            ch_r "Since my love life's been a bit. . . limited, I've gotten pretty good at this."
        elif RogueX.obedience >= RogueX.inhibition:
            $ RogueX.change_face("normal")
            ch_r "If that's what you want, [RogueX.player_petname]. . ."
        else:
            $ RogueX.change_face("sad")
            $ RogueX.mouth = "smile"
            ch_r "I guess it could be fun with you watching. . ."



    elif Approval:
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
            ch_r "You want to watch me again?"
        elif Approval and "masturbation" in RogueX.recent_history:
            $ RogueX.change_face("sexy", 1)
            ch_r "I guess I have a bit more in me. . ."
            jump Rogue_M_Prep
        elif Approval and "masturbation" in RogueX.daily_history:
            $ RogueX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["You enjoyed the show?",       
                    "Didn't get enough earlier?",
                    "It is nice to have an audience. . ."])
            ch_r "[Line]"
        elif RogueX.action_counter["masturbation"] < 3:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.brows = "confused"
            ch_r "You like to watch, huh?"
        else:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.ArmPose = 2
            $ Line = renpy.random.choice(["You sure do like to watch.",                 
                    "So you'd like me to go again?",                 
                    "You want to watch some more?",
                    "You want me ta diddle myself?"])
            ch_r "[Line]"
            $ Line = 0



    if Approval >= 2:
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("obedience", 90, 1)
            $ RogueX.change_stat("inhibition", 60, 1)
            ch_r "I suppose, let me get comfortable. . ."
        else:
            $ RogueX.change_face("sexy", 1)
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
                $ RogueX.change_face("sexy", 1)
                if RogueX.lust > 50:
                    ch_r "Well, definitely later. . . but I'll have to think about inviting you."
                else:
                    ch_r "Hmm, maybe. . . I'll let you know."
                $ RogueX.change_stat("love", 80, 2)
                $ RogueX.change_stat("inhibition", 70, 2)
                return
            "You look like you could use it. . .":
                if Approval:
                    $ RogueX.change_face("sexy")
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

                $ Approval = ApprovalCheck(RogueX, 450, "OI", TabM = 2)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.change_face("sad")
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
                    $ RogueX.recent_history.append("angry")
                    $ RogueX.daily_history.append("angry")



    $ RogueX.ArmPose = 1
    if RogueX.Forced:
        $ RogueX.change_face("angry", 1)
        ch_r "I'm not doing something so. . . intimate with you watching."
        $ RogueX.change_stat("lust", 90, 5)
        if RogueX.love > 300:
            $ RogueX.change_stat("love", 70, -2)
        $ RogueX.change_stat("obedience", 50, -2)
        $ RogueX.recent_history.append("angry")
        $ RogueX.daily_history.append("angry")
        $ RogueX.recent_history.append("no_masturbation")
        $ RogueX.daily_history.append("no_masturbation")
        return
    elif Taboo:
        $ RogueX.change_face("angry", 1)
        $ RogueX.daily_history.append("no_taboo")
        ch_r "I can't do that here!"
        $ RogueX.change_stat("lust", 90, 5)
        $ RogueX.change_stat("obedience", 50, -3)
        return
    elif RogueX.action_counter["masturbation"]:
        $ RogueX.change_face("sad")
        ch_r "Nope, not anymore, you'll have to go back to Internet porn."
    else:
        $ RogueX.change_face("normal", 1)
        ch_r "Heh, no, I'm not doing that."
    $ RogueX.recent_history.append("no_masturbation")
    $ RogueX.daily_history.append("no_masturbation")
    $ approval_bonus = 0
    return

label Rogue_M_Prep:
    $ RogueX.Upskirt = 1
    $ RogueX.underwearDown = 1
    call Rogue_First_Bottomless (1)
    call set_the_scene (Dress=0)


    if "unseen" in RogueX.recent_history:
        $ RogueX.change_face("sexy")
        $ RogueX.eyes = "closed"
        $ RogueX.ArmPose = 2
        "You see [RogueX.name] leaning back, masturbating. You don't think she's noticed you yet."
    else:
        $ RogueX.change_face("sexy")
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
        $ RogueX.DrainWord("no_taboo")
    $ RogueX.DrainWord("no_masturbation")
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
            $ RogueX.eyes = "closed"

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

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.Traits:
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
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
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
                        "Clean up [RogueX.name] (locked)" if not RogueX.Spunk:
                            pass
                        "Clean up [RogueX.name]" if RogueX.Spunk:
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
                    if "angry" in RogueX.recent_history:
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


    $ RogueX.change_face("bemused", 0)
    $ Line = 0
    if "unseen" not in RogueX.recent_history:
        ch_r "Ok, [RogueX.player_petname], that's enough of that for now."

label Rogue_M_Interupted:


    if "unseen" in RogueX.recent_history:
        $ RogueX.change_face("surprised", 1)
        "[RogueX.name] stops what she's doing with a start, eyes wide."
        call Rogue_First_Bottomless (1)
        $ RogueX.change_face("surprised", 1)


        if offhand_action == "jackin":
            ch_r "H- how long you been stand'in there, [RogueX.player_petname]?"
            $ RogueX.eyes = "down"
            menu:
                ch_r "And why is your cock out like that?!"
                "Long enough, it was an excellent show.":
                    $ RogueX.change_face("sexy")
                    $ RogueX.change_stat("obedience", 50, 3)
                    $ RogueX.change_stat("obedience", 70, 2)
                    ch_r "Well, I imagine it was. . ."
                    if RogueX.love >= 800 or RogueX.obedience >= 500 or RogueX.inhibition >= 500:
                        $ approval_bonus += 10
                        $ RogueX.change_stat("lust", 90, 5)
                        ch_r "And the view from this angle ain't so bad either. . ."
                "I. . . just got here?":

                    $ RogueX.change_face("angry")
                    $ RogueX.change_stat("love", 70, 2)
                    $ RogueX.change_stat("love", 90, 1)
                    $ RogueX.change_stat("obedience", 50, 2)
                    $ RogueX.change_stat("obedience", 70, 2)
                    "She looks pointedly at your cock,"
                    ch_r "A likely story . . ."
                    if RogueX.love >= 800 or RogueX.obedience >= 500 or RogueX.inhibition >= 500:
                        $ approval_bonus += 10
                        $ RogueX.change_stat("lust", 90, 5)
                        $ RogueX.change_face("bemused", 1)
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
                    $ RogueX.change_face("sexy", 1)
                    $ RogueX.change_stat("obedience", 50, 3)
                    $ RogueX.change_stat("obedience", 70, 2)
                    ch_r "Well I hope you got a good show out of it. . ."
                "I just got here.":
                    $ RogueX.change_face("bemused", 1)
                    $ RogueX.change_stat("love", 70, 2)
                    $ RogueX.change_stat("love", 90, 1)
                    ch_r "A likely story . . ."
                    $ RogueX.change_stat("obedience", 50, 2)
                    $ RogueX.change_stat("obedience", 70, 2)

        $ RogueX.DrainWord("unseen",1,0)
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
    call Checkout
    if action_context == "shift":
        $ action_context = 0
        return
    $ action_context = 0

    if RogueX.location != bg_current:
        return

    if Round <= 10:
        ch_r "I need to take a little break here, [RogueX.player_petname]."
        return
    $ RogueX.change_face("sexy", 1)
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
            $ RogueX.change_face("sly")
            if RogueX.remaining_actions and Round >= 10:
                ch_r "Well, alright. . ."
                jump Rogue_M_Cycle
            else:
                ch_r "I'm kinda worn out, maybe time for a break. . ."
        "I'm good here. [[Stop]":
            if RogueX.love < 800 and RogueX.inhibition < 500 and RogueX.obedience < 500:
                $ RogueX.change_outfit(Changed=0)
            $ RogueX.change_face("normal")
            $ RogueX.brows = "confused"
            ch_r "Well. . . ok then. . ."
            $ RogueX.brows = "normal"
        "You should probably stop for now." if RogueX.lust > 30:
            $ RogueX.change_face("angry")
            ch_r "Well if you say so."
    return







label Rogue_Sex_P:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (RogueX)
    if RogueX.action_counter["sex"] >= 7:
        $ approval_bonus += 15
    elif RogueX.action_counter["sex"] >= 3:
        $ approval_bonus += 12
    elif RogueX.action_counter["sex"]:
        $ approval_bonus += 10

    if RogueX.addiction >= 75 and (RogueX.event_counter["creampied"] + RogueX.event_counter["anal_creampied"]) >=3:
        $ approval_bonus += 20
    elif RogueX.addiction >= 75:
        $ approval_bonus += 15

    if RogueX.lust > 85:
        $ approval_bonus += 10
    elif RogueX.lust > 75:
        $ approval_bonus += 5

    if action_context == "shift":
        $ approval_bonus += 10
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

    if "no_sex" in RogueX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_sex" in RogueX.recent_history else 0


    $ Approval = ApprovalCheck(RogueX, 1400, TabM = 5)

    if action_context == "auto":
        $ RogueX.pose = "doggy"
        call Rogue_Sex_Launch ("sex")
        if RogueX.PantsNum() == 5:
            "You press up against [RogueX.name]'s backside, sliding her skirt up as you go."
            $ RogueX.Upskirt = 1
        elif RogueX.PantsNum() > 6:
            "You press up against [RogueX.name]'s backside, sliding her pants down as you do."
            $ RogueX.legs = 0
        else:
            "You press up against [RogueX.name]'s backside."
        $ RogueX.SeenPanties = 1
        "You rub the tip of your cock against her moist slit."
        $ RogueX.change_face("surprised", 1)

        if (RogueX.action_counter["sex"] and Approval) or (Approval > 1):
            "[RogueX.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            $ RogueX.change_face("sexy")
            $ RogueX.change_stat("obedience", 70, 3)
            $ RogueX.change_stat("inhibition", 50, 3)
            $ RogueX.change_stat("inhibition", 70, 1)
            ch_r "Ok, [RogueX.player_petname], let's do this."
            jump Rogue_SexPrep
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
                        jump Rogue_SexPrep
                    "You pull back before you really get it in."
                    $ RogueX.change_face("bemused", 1)
                    if RogueX.action_counter["sex"]:
                        ch_r "Well ok, [RogueX.player_petname], no harm done. Just give me a little warning next time."
                    else:
                        ch_r "Well ok, [RogueX.player_petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."
                "Just fucking.":
                    $ RogueX.change_stat("love", 80, -10, 1)
                    $ RogueX.change_stat("love", 200, -10)
                    "You press inside some more."
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
                        call Rogue_Sex_Reset
                        $ RogueX.recent_history.append("angry")
                        $ RogueX.daily_history.append("angry")
                    else:
                        $ RogueX.change_face("sad")
                        "[RogueX.name] doesn't seem to be into this, you're lucky she's so obedient."
                        jump Rogue_SexPrep
        return


    if not RogueX.action_counter["sex"] and "no_sex" not in RogueX.recent_history:
        $ RogueX.change_face("surprised", 1)
        $ RogueX.mouth = "kiss"
        ch_r "So, you'd like to take this to the next level? Actual sex? . . ."
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            ch_r "You'd really take it that far?"


    if not RogueX.action_counter["sex"] and Approval:
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -30, 1)
            $ RogueX.change_stat("love", 20, -20, 1)
        elif RogueX.love >= (RogueX.obedience + RogueX.inhibition):
            $ RogueX.change_face("sexy")
            $ RogueX.brows = "sad"
            $ RogueX.mouth = "smile"
            ch_r "Well, I've never been able to do this before now, so this might be fun."
        elif RogueX.obedience >= RogueX.inhibition:
            $ RogueX.change_face("normal")
            ch_r "If that's what you want, [RogueX.player_petname]. . ."
        elif RogueX.addiction >= 50:
            $ RogueX.change_face("manic", 1)
            ch_r "Well. . . I bet it would feel really good down there."
        else:
            $ RogueX.change_face("sad")
            $ RogueX.mouth = "smile"
            ch_r "Hmm, I've always wanted to try it. . ."

    elif Approval:
        $ RogueX.change_face("sexy", 1)
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
            ch_r "That's really what you want?"
        elif not Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "Well, at least you got us some privacy this time. . ."
        elif "sex" in RogueX.recent_history:
            ch_r "You want to go again? Ok."
            jump Rogue_SexPrep
        elif "sex" in RogueX.daily_history:
            $ Line = renpy.random.choice(["Back again so soon?",                 
                "So you'd like another go?",                 
                "You can't stay away from this. . .", 
                "Didn't get enough earlier?",
                "You're going to wear me out."])
            ch_r "[Line]"
        elif RogueX.action_counter["sex"] < 3:
            $ RogueX.brows = "confused"
            $ RogueX.mouth = "kiss"
            ch_r "So you'd like another go?"
        else:
            $ Line = renpy.random.choice(["You want some of this action?",                 
                "So you'd like another go?",                 
                "You can't stay away from this. . .", 
                "You want me to ride your pole?",
                "You wanna dip your wick?"])
            ch_r "[Line]"
        $ Line = 0

    if Approval >= 2:
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("obedience", 90, 1)
            $ RogueX.change_stat("inhibition", 60, 1)
            ch_r "Ok, fine."
        elif "no_sex" in RogueX.daily_history:
            ch_r "Ok, you've won me over on this one. . ."
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
        jump Rogue_SexPrep
    else:

        $ RogueX.change_face("angry")
        if "no_sex" in RogueX.recent_history:
            ch_r "I {i}just{/i} told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history and "no_sex" in RogueX.daily_history:
            ch_r "I already told you that I wouldn't bang you in public!"
        elif "no_sex" in RogueX.daily_history:
            ch_r "I already told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "I already told you this is too public!"
        elif not RogueX.action_counter["sex"]:
            $ RogueX.change_face("bemused")
            ch_r "I just don't think I'm ready yet, [RogueX.player_petname]. . ."
        else:
            $ RogueX.change_face("bemused")
            ch_r "Not, right now [RogueX.player_petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_sex" in RogueX.daily_history:
                $ RogueX.change_face("bemused")
                ch_r "Yeah, ok, [RogueX.player_petname]."
                return
            "Maybe later?" if "no_sex" not in RogueX.daily_history:
                $ RogueX.change_face("sexy")
                ch_r "I'll give it some thought, [RogueX.player_petname]."
                $ RogueX.change_stat("love", 80, 2)
                $ RogueX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ RogueX.recent_history.append("no_taboo")
                    $ RogueX.daily_history.append("no_taboo")
                $ RogueX.recent_history.append("no_sex")
                $ RogueX.daily_history.append("no_sex")
                return
            "I think you'd enjoy it as much as I would. . .":
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
                    jump Rogue_SexPrep
            "Bend over.":
                $ Approval = ApprovalCheck(RogueX, 1150, "OI", TabM = 3)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.change_face("sad")
                    $ RogueX.change_stat("love", 70, -5, 1)
                    $ RogueX.change_stat("love", 200, -5)
                    ch_r "Ok, fine. If we're going to do this, stick it in already."
                    $ RogueX.change_stat("obedience", 80, 4)
                    $ RogueX.change_stat("inhibition", 80, 1)
                    $ RogueX.change_stat("inhibition", 60, 3)
                    $ RogueX.Forced = 1
                    jump Rogue_SexPrep
                else:
                    $ RogueX.change_stat("love", 200, -20)
                    $ RogueX.recent_history.append("angry")
                    $ RogueX.daily_history.append("angry")


    $ RogueX.ArmPose = 1
    if "no_sex" in RogueX.daily_history:
        ch_r "Learn to take \"no\" for an answer, [RogueX.player_petname]."
        $ RogueX.recent_history.append("angry")
        $ RogueX.daily_history.append("angry")
    elif RogueX.Forced:
        $ RogueX.change_face("angry", 1)
        ch_r "I'm not doing that just because you have me over a barrel."
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
        ch_r "Even if I wanted to, it certainly wouldn't be here!"
        $ RogueX.change_stat("lust", 200, 5)
        $ RogueX.change_stat("obedience", 50, -3)
    elif RogueX.action_counter["sex"]:
        $ RogueX.change_face("sad")
        ch_r "Maybe you could go fuck yourself instead."
    else:
        $ RogueX.change_face("normal", 1)
        ch_r "No way."
    $ RogueX.recent_history.append("no_sex")
    $ RogueX.daily_history.append("no_sex")
    $ approval_bonus = 0
    return

label Rogue_SexPrep:
    call Seen_First_Peen (RogueX, Partner, React=action_context)
    $ RogueX.pose = "doggy"
    call Rogue_Sex_Launch ("hotdog")

    if action_context == RogueX:

        $ action_context = 0
        if RogueX.PantsNum() == 5:
            "[RogueX.name] turns and backs up against your cock, sliding her skirt up as she does so."
            $ RogueX.Upskirt = 1
        elif RogueX.PantsNum() > 6:
            "[RogueX.name] turns and backs up against your cock, sliding her pants down as she does so."
            $ RogueX.Upskirt = 1
        else:
            "[RogueX.name] turns and backs up against your cock."
        $ RogueX.SeenPanties = 1
        "She slides the tip along her pussy and seems to want you to insert it."
        menu:
            "What do you do?"
            "Go with it.":
                $ RogueX.change_stat("inhibition", 80, 3)
                $ RogueX.change_stat("inhibition", 50, 2)
                "[RogueX.name] slides it in."
            "Praise her.":
                $ RogueX.change_face("sexy", 1)
                $ RogueX.change_stat("inhibition", 80, 3)
                ch_p "Oh yeah, [RogueX.petname], let's do this."
                $ RogueX.nameCheck()
                "[RogueX.name] slides it in."
                $ RogueX.change_stat("love", 85, 1)
                $ RogueX.change_stat("obedience", 90, 1)
                $ RogueX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ RogueX.change_face("surprised")
                $ RogueX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [RogueX.petname]."
                $ RogueX.nameCheck()
                "[RogueX.name] pulls back."
                $ RogueX.change_stat("obedience", 90, 1)
                $ RogueX.change_stat("obedience", 50, 1)
                $ RogueX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ RogueX.AddWord(1,"refused","refused")
                return
        $ RogueX.underwearDown = 1
        call Rogue_First_Bottomless (1)

    elif action_context != "auto":
        call AutoStrip (RogueX)

        if Taboo:
            if not RogueX.action_counter["sex"]:
                "[RogueX.name] glances around for voyeurs. . ."
                "She hesitantly pulls down your pants and slowly backs up against your rigid member."
                "You guide it into place and slide it in."
            else:
                "[RogueX.name] glances around to see if anyone notices what she's doing, then backs her ass up against your cock."
                "You guide your cock into place and ram it home."
            $ RogueX.inhibition += int(Taboo/10)
            $ RogueX.lust += int(Taboo/5)
        else:
            if not RogueX.action_counter["sex"]:
                "[RogueX.name] hesitantly pulls down your pants slowly backs up against your rigid member."
                "You press her folds aside and nudge your cock in."
            else:
                "[RogueX.name] bends over and presses her backside against you suggestively."
                "You take careful aim and then ram your cock in."
    else:


        if (RogueX.PantsNum() > 6 and not RogueX.Upskirt) and (RogueX.underwear and not RogueX.underwearDown):
            "You quickly pull down her pants and her [RogueX.underwear] and press against her slit."
        elif (RogueX.underwear and not RogueX.underwearDown):
            "You quickly pull down her [RogueX.underwear] and press against her slit."
        $ RogueX.Upskirt = 1
        $ RogueX.underwearDown = 1
        $ RogueX.SeenPanties = 1
        call Rogue_First_Bottomless (1)

    if not RogueX.action_counter["sex"]:
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -150)
            $ RogueX.change_stat("obedience", 70, 60)
            $ RogueX.change_stat("inhibition", 80, 50)
        else:
            $ RogueX.change_stat("love", 90, 30)
            $ RogueX.change_stat("obedience", 70, 30)
            $ RogueX.change_stat("inhibition", 80, 60)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    $ Player.Cock = "in"
    $ primary_action = "sex"
    $ action_speed = 1
    if Taboo:
        $ RogueX.DrainWord("no_taboo")
    $ RogueX.DrainWord("no_sex")
    $ RogueX.recent_history.append("sex")
    $ RogueX.daily_history.append("sex")

label Rogue_Sex_Cycle:
    while Round > 0:
        call shift_focus (RogueX)
        call Rogue_Sex_Launch ("sex")
        $ RogueX.lust_face()
        $ Player.Cock = "in"
        $ primary_action = "sex"

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

                    call Slap_Ass (RogueX)
                    $ counter += 1
                    $ Round -= 1
                    jump Rogue_Sex_Cycle
                "Turn her Around":

                    $ RogueX.pose = "doggy" if RogueX.pose != "doggy" else "sex"
                    "You turn her around. . ."
                    jump Rogue_Sex_Cycle

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
                                    "How about anal?":
                                        $ action_context = "shift"
                                        call Rogue_SexAfter
                                        call Rogue_Sex_A
                                    "Just stick it in her ass [[without asking].":
                                        $ action_context = "auto"
                                        call Rogue_SexAfter
                                        call Rogue_Sex_A
                                    "Pull back to hotdog her.":
                                        $ action_context = "pullback"
                                        call Rogue_SexAfter
                                        call Rogue_Sex_H
                                    "Never Mind":
                                        jump Rogue_Sex_Cycle
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
                                    jump Rogue_Sex_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Rogue_Sex_Cycle
                                "Never mind":
                                    jump Rogue_Sex_Cycle
                        "Just take a look at her.":
                            $ Player.Cock = 0
                            $ action_speed = 0

                        "Show her feet" if not ShowFeet and (RogueX.pose == "doggy" or RogueX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (RogueX.pose == "doggy" or RogueX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [RogueX.name]":

                            call Girl_Undress (RogueX)
                        "Clean up [RogueX.name] (locked)" if not RogueX.Spunk:
                            pass
                        "Clean up [RogueX.name]" if RogueX.Spunk:
                            call Girl_Cleanup (RogueX, "ask")
                        "Never mind":
                            jump Rogue_Sex_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Rogue_Sex_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Rogue_SexAfter
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Rogue_Sex_Reset
                    $ Line = 0
                    jump Rogue_SexAfter


        call shift_focus (RogueX)
        call Sex_Dialog (RogueX, Partner)

        $ counter += 1
        $ Round -= 1
        $ Player.Wet = 1
        $ Player.Spunk = 0 if (Player.Spunk and "in" not in RogueX.Spunk) else Player.Spunk

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or RogueX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (RogueX)
                if "angry" in RogueX.recent_history:
                    call Rogue_Sex_Reset
                    return
                $ RogueX.change_stat("lust", 200, 5)
                if 100 > RogueX.lust >= 70 and RogueX.session_orgasms < 2:
                    $ RogueX.recent_history.append("unsatisfied")
                    $ RogueX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Rogue_SexAfter
                $ Line = "came"

            if RogueX.lust >= 100:

                call Girl_Cumming (RogueX)
                if action_context == "shift" or "angry" in RogueX.recent_history:
                    jump Rogue_SexAfter

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "She's emptied you out, you'll need to take a break."
                    jump Rogue_SexAfter
                elif "unsatisfied" in RogueX.recent_history:

                    $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                    "[Line] Keep going?"
                    menu:
                        extend ""
                        "Yes, keep going for a bit." if Player.semen:
                            $ Line = "You get back into it"
                            jump Rogue_Sex_Cycle
                        "No, I'm done." if Player.semen:
                            "You pull back."
                            jump Rogue_SexAfter
                        "No, I'm spent." if not Player.semen:
                            "You pull back."
                            jump Rogue_SexAfter
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif counter == (5 + RogueX.Sex):
            $ RogueX.brows = "confused"
            ch_r "Are you getting close here? I'm getting as little sore."
        elif counter == (10 + RogueX.Sex):
            $ RogueX.brows = "angry"
            ch_r "I'm . . .getting . . .worn out. . . here, . . [RogueX.player_petname]."
            menu:
                ch_r "Can we. . . do something. . . else?"
                "How about a BJ?" if RogueX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Rogue_SexAfter
                    call Rogue_Blowjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    jump Rogue_Sex_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Rogue_Sex_Reset
                    $ action_context = "shift"
                    jump Rogue_SexAfter
                "No, get back down there.":
                    if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):
                        $ RogueX.change_stat("love", 200, -5)
                        $ RogueX.change_stat("obedience", 50, 3)
                        $ RogueX.change_stat("obedience", 80, 2)
                        "She grumbles but keeps moving."
                    else:
                        $ RogueX.change_face("angry", 1)
                        call Rogue_Sex_Reset
                        "She scowls at you and pulls out."
                        ch_r "Well if that's your attitude you can handle your own business."
                        $ RogueX.change_stat("love", 50, -3, 1)
                        $ RogueX.change_stat("love", 80, -4, 1)
                        $ RogueX.change_stat("obedience", 30, -1, 1)
                        $ RogueX.change_stat("obedience", 50, -1, 1)
                        $ RogueX.recent_history.append("angry")
                        $ RogueX.daily_history.append("angry")
                        jump Rogue_SexAfter


        call Escalation (RogueX)

        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."


    $ RogueX.change_face("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.player_petname], that's enough of that for now."

label Rogue_SexAfter:
    if not action_context:
        $ Player.Sprite = 0
        $ Player.Cock = "out"
        call Rogue_Sex_Reset

    $ RogueX.change_face("sexy")

    $ RogueX.action_counter["sex"] += 1
    $ RogueX.remaining_actions -=1
    $ RogueX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ RogueX.addiction_rate += 1
    $ RogueX.change_stat("inhibition", 30, 2)
    $ RogueX.change_stat("inhibition", 70, 1)

    call Partner_Like (RogueX, 3, 2)

    if "Rogue Sex Addict" in Achievements:
        pass

    elif RogueX.action_counter["sex"] >= 10:
        $ RogueX.SEXP += 5
        $ Achievements.append("Rogue Sex Addict")
        if not action_context:
            $ RogueX.change_face("smile", 1)
            ch_r "I think I'm getting addicted to this."
    elif RogueX.action_counter["sex"] == 1:
        $ RogueX.SEXP += 20
        if not action_context:
            if RogueX.love >= 500 and "unsatisfied" not in RogueX.recent_history:
                ch_r "That was really great, [RogueX.player_petname], we'll have to do that again sometime."
            elif RogueX.obedience <= 500 and Player.focus <= 20:
                $ RogueX.mouth = "sad"
                ch_r "Did you get what you needed here?"
    elif RogueX.action_counter["sex"] == 5:
        ch_r "We're making a regular habit of this."
    elif not action_context:
        if "unsatisfied" in RogueX.recent_history:
            $ RogueX.change_face("angry")
            $ RogueX.eyes = "side"
            ch_r "I didn't exactly get off there. . ."

    $ approval_bonus = 0


    call Checkout
    return






label Rogue_Sex_A:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (RogueX)
    if RogueX.action_counter["anal"] >= 7:
        $ approval_bonus += 20
    elif RogueX.action_counter["anal"] >= 3:
        $ approval_bonus += 17
    elif RogueX.action_counter["anal"]:
        $ approval_bonus += 15

    if RogueX.addiction >= 75 and (RogueX.event_counter["creampied"] + RogueX.event_counter["anal_creampied"]) >=3:
        $ approval_bonus += 25
    elif RogueX.addiction >= 75:
        $ approval_bonus += 15

    if RogueX.lust > 85:
        $ approval_bonus += 10
    elif RogueX.lust > 75:
        $ approval_bonus += 5

    if RogueX.used_to_anal:
        $ approval_bonus += 10
    elif "anal" in RogueX.recent_history:
        $ approval_bonus -= 20
    elif "anal" in RogueX.daily_history:
        $ approval_bonus -= 10

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
    if "no_anal" in RogueX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_anal" in RogueX.recent_history else 0

    $ Approval = ApprovalCheck(RogueX, 1550, TabM = 5)

    if action_context == "auto":
        $ RogueX.pose = "doggy"
        call Rogue_Sex_Launch ("anal")
        if RogueX.PantsNum() == 5:
            "You press up against [RogueX.name]'s backside, sliding her skirt up as you go."
            $ RogueX.Upskirt = 1
        elif RogueX.PantsNum() > 6:
            "You press up against [RogueX.name]'s backside, sliding her pants down as you do."
            $ RogueX.legs = 0
        else:
            "You press up against [RogueX.name]'s backside."
        $ RogueX.SeenPanties = 1
        "You press the tip of your cock against her tight rim."
        $ RogueX.change_face("surprised", 1)

        if (RogueX.action_counter["anal"] and Approval) or (Approval > 1):
            "[RogueX.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            $ RogueX.change_face("sexy")
            $ RogueX.change_stat("obedience", 70, 3)
            $ RogueX.change_stat("inhibition", 50, 3)
            $ RogueX.change_stat("inhibition", 70, 1)
            ch_r "Hmm, stick it in. . ."
            jump Rogue_AnalPrep
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
                        ch_r "I guess if you really want to try it. . ."
                        jump Rogue_AnalPrep
                    "You pull back before you really get it in."
                    $ RogueX.change_face("bemused", 1)
                    if RogueX.action_counter["anal"]:
                        ch_r "Well ok, [RogueX.player_petname], no harm done. Just give me a little warning next time."
                    else:
                        ch_r "Well ok, [RogueX.player_petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."
                "Just fucking.":
                    $ RogueX.change_stat("love", 80, -10, 1)
                    $ RogueX.change_stat("love", 200, -8)
                    "You press into her."
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
                        call Rogue_Sex_Reset
                        $ RogueX.recent_history.append("angry")
                        $ RogueX.daily_history.append("angry")
                    else:
                        $ RogueX.change_face("sad")
                        "[RogueX.name] doesn't seem to be into this, you're lucky she's so obedient."
                        jump Rogue_AnalPrep
        return


    if not RogueX.action_counter["anal"] and "no_anal" not in RogueX.recent_history:
        $ RogueX.change_face("surprised", 1)
        $ RogueX.mouth = "kiss"
        ch_r "Wait, so you want to stick it in my butt?!"

        if RogueX.Forced:
            $ RogueX.change_face("sad")
            ch_r "Seriously?"

    if not RogueX.used_to_anal and ("dildo_anal" in RogueX.daily_history or "anal" in RogueX.daily_history):
        $ RogueX.change_face("bemused", 1)
        ch_r "I'm still a little sore from earlier."

    elif "anal" in RogueX.recent_history:
        $ RogueX.change_face("sexy", 1)
        ch_r "You want to go again? Ok."
        jump Rogue_AnalPrep


    if not RogueX.action_counter["anal"] and Approval:
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
        elif RogueX.love >= (RogueX.obedience + RogueX.inhibition):
            $ RogueX.change_face("sexy")
            $ RogueX.brows = "sad"
            $ RogueX.mouth = "smile"
            ch_r "I guess if you really want to try it. . ."
        elif RogueX.obedience >= RogueX.inhibition:
            $ RogueX.change_face("normal")
            ch_r "Ok, [RogueX.player_petname], I'm ready."
        elif RogueX.addiction >= 50:
            $ RogueX.change_face("manic", 1)
            ch_r "Well. . . I bet it would feel really good down there."
        else:
            $ RogueX.change_face("sad")
            $ RogueX.mouth = "smile"
            ch_r "Hmm, it has been on my list. . ."

    elif Approval:
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
            ch_r "That's really what you want?"
        elif not Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "Well, at least you got us some privacy this time. . ."
        elif "anal" in RogueX.daily_history and not RogueX.used_to_anal:
            pass
        elif "anal" in RogueX.recent_history:
            ch_r "I think I'm warmed up. . ."
            jump Rogue_AnalPrep
        elif "anal" in RogueX.daily_history:
            $ RogueX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",                 
                "So you'd like another go?",                 
                "I'm still a little sore from earlier.", 
                "Didn't get enough earlier?",
                "You're going to wear me out."])
            ch_r "[Line]"
        elif RogueX.action_counter["anal"] < 3:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.brows = "confused"
            $ RogueX.mouth = "kiss"
            ch_r "So you'd like another go?"
        else:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                "So you'd like another go?",                 
                "You can't stay away from this booty.", 
                "You want me to ride your pole?",
                "You wanna dip your wick?"])
            ch_r "[Line]"
        $ Line = 0

    if Approval >= 2:
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("obedience", 90, 1)
            $ RogueX.change_stat("inhibition", 60, 1)
            ch_r "Ok, fine."
        elif "no_anal" in RogueX.daily_history:
            ch_r "Ok, ok, I have been itching for this. . ."
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
        jump Rogue_AnalPrep
    else:

        $ RogueX.change_face("angry")
        if "no_anal" in RogueX.recent_history:
            ch_r "What part of \"no,\" did you not get, [RogueX.player_petname]?"
        elif Taboo and "no_taboo" in RogueX.daily_history and "no_anal" in RogueX.daily_history:
            ch_r "I already told you that I wouldn't do that out here!"
        elif "no_anal" in RogueX.daily_history:
            ch_r "I already told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "I already told you that I wouldn't do that out here!"
        elif not RogueX.action_counter["anal"]:
            $ RogueX.change_face("bemused")
            ch_r "I'm just not into that, [RogueX.player_petname]. . ."
        elif not RogueX.used_to_anal and "anal" not in RogueX.daily_history:
            $ RogueX.change_face("perplexed")
            ch_r "You could have been a bit more gentle last time, [RogueX.player_petname]. . ."
        else:
            $ RogueX.change_face("bemused")
            ch_r "Not, right now [RogueX.player_petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_anal" in RogueX.daily_history:
                $ RogueX.change_face("bemused")
                ch_r "Yeah, ok, [RogueX.player_petname]."
                return
            "Maybe later?" if "no_anal" not in RogueX.daily_history:
                $ RogueX.change_face("sexy")
                ch_r "I'll give it some thought, [RogueX.player_petname]."
                $ RogueX.change_stat("love", 80, 2)
                $ RogueX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ RogueX.recent_history.append("no_taboo")
                    $ RogueX.daily_history.append("no_taboo")
                $ RogueX.recent_history.append("no_anal")
                $ RogueX.daily_history.append("no_anal")
                return
            "I bet it would feel really good. . .":
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
                    jump Rogue_AnalPrep
                else:
                    pass
            "Bend over.":

                $ Approval = ApprovalCheck(RogueX, 1250, "OI", TabM = 3)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.change_face("sad")
                    $ RogueX.change_stat("love", 70, -5, 1)
                    $ RogueX.change_stat("love", 200, -5)
                    ch_r "Ok, fine. If we're going to do this, stick it in already."
                    $ RogueX.change_stat("obedience", 80, 4)
                    $ RogueX.change_stat("inhibition", 80, 1)
                    $ RogueX.change_stat("inhibition", 60, 3)
                    $ RogueX.Forced = 1
                    jump Rogue_AnalPrep
                else:
                    $ RogueX.change_stat("love", 200, -20)
                    $ RogueX.recent_history.append("angry")
                    $ RogueX.daily_history.append("angry")


    $ RogueX.ArmPose = 1
    if "no_anal" in RogueX.daily_history:
        ch_r "Learn to take \"no\" for an answer, [RogueX.player_petname]."
        $ RogueX.recent_history.append("angry")
        $ RogueX.daily_history.append("angry")
    elif RogueX.Forced:
        $ RogueX.change_face("angry", 1)
        ch_r "That's a bit much, even for you."
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
        ch_r "That you would even suggest such a thing in a place like this. . ."
        $ RogueX.change_stat("lust", 200, 5)
        $ RogueX.change_stat("obedience", 50, -3)
    elif not RogueX.used_to_anal and "anal" in RogueX.daily_history:
        $ RogueX.change_face("bemused")
        ch_r "Sorry, I just need a little break back there, [RogueX.player_petname]."
    elif RogueX.action_counter["anal"]:
        $ RogueX.change_face("sad")
        ch_r "The only thing you can do with my ass is kiss it, [RogueX.player_petname]."
        ch_r ". . .Don't get any ideas."
    else:
        $ RogueX.change_face("normal", 1)
        ch_r "Not happening."
    $ RogueX.recent_history.append("no_anal")
    $ RogueX.daily_history.append("no_anal")
    $ approval_bonus = 0
    return

label Rogue_AnalPrep:
    call Seen_First_Peen (RogueX, Partner, React=action_context)
    $ RogueX.pose = "doggy"
    call Rogue_Sex_Launch ("hotdog")

    if action_context == RogueX:

        $ action_context = 0
        if RogueX.PantsNum() == 5:
            "[RogueX.name] turns and backs up against your cock, sliding her skirt up as she does so."
            $ RogueX.Upskirt = 1
        elif RogueX.PantsNum() > 6:
            "[RogueX.name] turns and backs up against your cock, sliding her pants down as she does so."
            $ RogueX.Upskirt = 1
        else:
            "[RogueX.name] turns and backs up against your cock."
        $ RogueX.SeenPanties = 1
        "She slides the tip up to her anus, and presses against it."
        menu:
            "What do you do?"
            "Go with it.":
                $ RogueX.change_stat("inhibition", 80, 3)
                $ RogueX.change_stat("inhibition", 50, 2)
                "[RogueX.name] slides it in."
            "Praise her.":
                $ RogueX.change_face("sexy", 1)
                $ RogueX.change_stat("inhibition", 80, 3)
                ch_p "Ooo, dirty girl, [RogueX.petname], let's do this."
                $ RogueX.nameCheck()
                "[RogueX.name] slides it in."
                $ RogueX.change_stat("love", 85, 1)
                $ RogueX.change_stat("obedience", 90, 1)
                $ RogueX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ RogueX.change_face("surprised")
                $ RogueX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [RogueX.petname]."
                $ RogueX.nameCheck()
                "[RogueX.name] pulls back."
                $ RogueX.change_stat("obedience", 90, 1)
                $ RogueX.change_stat("obedience", 50, 1)
                $ RogueX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ RogueX.AddWord(1,"refused","refused")
                return
        $ RogueX.underwearDown = 1
        call Rogue_First_Bottomless (1)

    elif action_context != "auto":
        call AutoStrip (RogueX)

        if Taboo:
            if RogueX.action_counter["anal"]:
                "[RogueX.name] glances around to see if anyone notices what she's doing, then backs her ass up against your cock."
                "You guide your cock into place and ram it home."
            else:

                "[RogueX.name] glances around for voyeurs. . ."
                "She hesitantly pulls down your pants and slowly backs up against your rigid member."
                "You guide it into place and slide it in."
            $ RogueX.inhibition += int(Taboo/10)
            $ RogueX.lust += int(Taboo/5)
        else:
            if not RogueX.action_counter["anal"]:
                "[RogueX.name] bends over and presses her backside against you suggestively."
                "You take careful aim and then push your cock in."
            else:
                "[RogueX.name] hesitantly pulls down your pants slowly backs up against your rigid member."
                "You press against her rim and nudge your cock in."
    else:


        if (RogueX.PantsNum() > 6 and not RogueX.Upskirt) and (RogueX.underwear and not RogueX.underwearDown):
            "You quickly pull down her pants and her [RogueX.underwear] and press against her ass."
        elif (RogueX.underwear and not RogueX.underwearDown):
            "You quickly pull down her [RogueX.underwear] and press against her ass."

        $ RogueX.Upskirt = 1
        $ RogueX.underwearDown = 1
        $ RogueX.SeenPanties = 1
        call Rogue_First_Bottomless (1)

    if not RogueX.action_counter["anal"]:
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -150)
            $ RogueX.change_stat("obedience", 70, 70)
            $ RogueX.change_stat("inhibition", 80, 40)
        else:
            $ RogueX.change_stat("love", 90, 10)
            $ RogueX.change_stat("obedience", 70, 30)
            $ RogueX.change_stat("inhibition", 80, 70)
    elif not RogueX.used_to_anal:
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -20)
            $ RogueX.change_stat("obedience", 70, 10)
            $ RogueX.change_stat("inhibition", 80, 5)
        else:
            $ RogueX.change_stat("obedience", 70, 7)
            $ RogueX.change_stat("inhibition", 80, 5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    $ Player.Cock = "anal"
    $ primary_action = "anal"
    $ action_speed = 1
    if Taboo:
        $ RogueX.DrainWord("no_taboo")
    $ RogueX.DrainWord("no_anal")
    $ RogueX.recent_history.append("anal")
    $ RogueX.daily_history.append("anal")

label Rogue_Anal_Cycle:
    while Round > 0:
        call shift_focus (RogueX)
        call Rogue_Sex_Launch ("anal")
        $ RogueX.lust_face()
        $ Player.Cock = "anal"
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

                    call Slap_Ass (RogueX)
                    $ counter += 1
                    $ Round -= 1
                    jump Rogue_Anal_Cycle
                "Turn her Around":

                    $ RogueX.pose = "doggy" if RogueX.pose != "doggy" else "sex"
                    "You turn her around. . ."
                    jump Rogue_Anal_Cycle

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
                                    "How about sex?":
                                        $ action_context = "shift"
                                        call Rogue_AnalAfter
                                        call Rogue_Sex_P
                                    "Just stick it in her pussy [[without asking].":
                                        $ action_context = "auto"
                                        call Rogue_AnalAfter
                                        call Rogue_Sex_P
                                    "Pull back to hotdog her.":
                                        $ action_context = "pullback"
                                        call Rogue_AnalAfter
                                        call Rogue_Sex_H
                                    "Never Mind":
                                        jump Rogue_Anal_Cycle
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
                                    jump Rogue_Anal_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Rogue_Anal_Cycle
                                "Never mind":
                                    jump Rogue_Anal_Cycle
                        "Just take a look at her.":
                            $ Player.Cock = 0
                            $ action_speed = 0

                        "Show her feet" if not ShowFeet and (RogueX.pose == "doggy" or RogueX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (RogueX.pose == "doggy" or RogueX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [RogueX.name]":

                            call Girl_Undress (RogueX)
                        "Clean up [RogueX.name] (locked)" if not RogueX.Spunk:
                            pass
                        "Clean up [RogueX.name]" if RogueX.Spunk:
                            call Girl_Cleanup (RogueX, "ask")
                        "Never mind":
                            jump Rogue_Anal_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Rogue_Sex_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Rogue_AnalAfter
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Rogue_Sex_Reset
                    $ Line = 0
                    jump Rogue_AnalAfter


        call shift_focus (RogueX)
        call Sex_Dialog (RogueX, Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or RogueX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (RogueX)
                if "angry" in RogueX.recent_history:
                    call Rogue_Sex_Reset
                    return
                $ RogueX.change_stat("lust", 200, 5)
                if 100 > RogueX.lust >= 70 and RogueX.session_orgasms < 2:
                    $ RogueX.recent_history.append("unsatisfied")
                    $ RogueX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Rogue_AnalAfter
                $ Line = "came"

            if RogueX.lust >= 100:

                call Girl_Cumming (RogueX)
                if action_context == "shift" or "angry" in RogueX.recent_history:
                    jump Rogue_AnalAfter

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "She's emptied you out, you'll need to take a break."
                    jump Rogue_AnalAfter
                elif "unsatisfied" in RogueX.recent_history:

                    $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                    "[Line] Keep going?"
                    menu:
                        extend ""
                        "Yes, keep going for a bit." if Player.semen:
                            $ Line = "You get back into it"
                            jump Rogue_Anal_Cycle
                        "No, I'm done." if Player.semen:
                            "You pull back."
                            jump Rogue_AnalAfter
                        "No, I'm spent." if not Player.semen:
                            "You pull back."
                            jump Rogue_AnalAfter
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif counter == (5 + RogueX.action_counter["anal"]):
            $ RogueX.brows = "confused"
            ch_r "Are you getting close here? I'm getting as little sore."
        elif counter == (10 + RogueX.action_counter["anal"]):
            $ RogueX.brows = "angry"
            ch_r "I'm . . .getting . . .worn out. . . here, . . [RogueX.player_petname]."
            menu:
                ch_r "Can we. . . do something. . . else?"
                "How about a BJ?" if RogueX.remaining_actions and multi_action:
                    if RogueX.action_counter["anal"] >= 5 and RogueX.action_counter["blowjob"] >= 10 and RogueX.SEXP >= 50:
                        $ action_context = "shift"
                        call Rogue_AnalAfter
                        call Rogue_Blowjob
                    else:
                        ch_r "No thanks, [RogueX.player_petname]. Maybe a Handy instead?"
                        $ action_context = "shift"
                        call Rogue_AnalAfter
                        call Rogue_HJ_Prep
                "How about a Handy?" if RogueX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Rogue_AnalAfter
                    call Rogue_Handjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    jump Rogue_Anal_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Rogue_Sex_Reset
                    $ action_context = "shift"
                    jump Rogue_AnalAfter
                "No, get back down there.":
                    if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):
                        $ RogueX.change_stat("love", 200, -5)
                        $ RogueX.change_stat("obedience", 50, 3)
                        $ RogueX.change_stat("obedience", 80, 2)
                        "She grumbles but keeps moving."
                    else:
                        $ RogueX.change_face("angry", 1)
                        call Rogue_Sex_Reset
                        "She scowls at you and pulls out."
                        ch_r "Well if that's your attitude you can handle your own business."
                        $ RogueX.change_stat("love", 50, -3, 1)
                        $ RogueX.change_stat("love", 80, -4, 1)
                        $ RogueX.change_stat("obedience", 30, -1, 1)
                        $ RogueX.change_stat("obedience", 50, -1, 1)
                        $ RogueX.recent_history.append("angry")
                        $ RogueX.daily_history.append("angry")
                        jump Rogue_AnalAfter


        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."


    $ RogueX.change_face("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.player_petname], that's enough of that for now."

label Rogue_AnalAfter:
    if not action_context:
        $ Player.Sprite = 0
        $ Player.Cock = "out"
        call Rogue_Sex_Reset

    $ RogueX.change_face("sexy")

    $ RogueX.action_counter["anal"] += 1
    $ RogueX.remaining_actions -=1
    $ RogueX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ RogueX.addiction_rate += 1
    $ RogueX.change_stat("inhibition", 30, 3)
    $ RogueX.change_stat("inhibition", 70, 1)

    if Partner == "Kitty":
        call Partner_Like (RogueX, 3, 1)
    else:
        call Partner_Like (RogueX, 4, 2)

    if "Rogue Anal Addict" in Achievements:
        pass

    elif RogueX.action_counter["anal"] >= 10:
        $ RogueX.SEXP += 7
        $ Achievements.append("Rogue Anal Addict")
        if not action_context:
            $ RogueX.change_face("bemused", 1)
            ch_r "I. . . really think I enjoy this. . ."
    elif RogueX.action_counter["anal"] == 1:
        $ RogueX.SEXP += 25
        if not action_context:
            if RogueX.love >= 500 and "unsatisfied" not in RogueX.recent_history:
                ch_r "That was . . . interesting [RogueX.player_petname]. We'll have to do that again sometime."
            elif RogueX.obedience <= 500 and Player.focus <= 20:
                $ RogueX.mouth = "sad"
                ch_r "Ouch."
                ch_r "Did you get what you needed here?"
    elif RogueX.action_counter["anal"] == 5:
        ch_r "We're making a regular habit of this."
    elif not action_context:
        if "unsatisfied" in RogueX.recent_history:
            $ RogueX.change_face("angry")
            $ RogueX.eyes = "side"
            ch_r "Hmm, you seemed to get more out of that than me. . ."

    $ approval_bonus = 0


    call Checkout
    return








label Rogue_Sex_H:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (RogueX)
    if RogueX.action_counter["hotdog"] >= 3:
        $ approval_bonus += 10
    elif RogueX.action_counter["hotdog"]:
        $ approval_bonus += 5

    if RogueX.lust > 85:
        $ approval_bonus += 10
    elif RogueX.lust > 75:
        $ approval_bonus += 5
    if action_context == "shift":
        $ approval_bonus += 10
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

    if "no_hotdog" in RogueX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_hotdog" in RogueX.recent_history else 0

    $ Approval = ApprovalCheck(RogueX, 1000, TabM = 3)

    if action_context == "auto":
        $ RogueX.pose = "doggy"
        call Rogue_Sex_Launch ("hotdog")
        "You press up against [RogueX.name]'s backside."
        $ RogueX.change_face("surprised", 1)

        if (RogueX.action_counter["hotdog"] and Approval) or (Approval > 1):
            "[RogueX.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            $ RogueX.change_face("sexy")
            $ RogueX.change_stat("obedience", 70, 3)
            $ RogueX.change_stat("inhibition", 50, 3)
            $ RogueX.change_stat("inhibition", 70, 1)
            ch_r "Hmm, I've apparently got someone's attention. . ."
            jump Rogue_HotdogPrep
        else:
            $ RogueX.brows = "angry"
            menu:
                ch_r "Hmm, kinda rude, [RogueX.player_petname]."
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ RogueX.change_face("sexy", 1)
                        $ RogueX.change_stat("obedience", 70, 3)
                        $ RogueX.change_stat("inhibition", 50, 3)
                        $ RogueX.change_stat("inhibition", 70, 1)
                        ch_r "I guess it doesn't feel so bad. . ."
                        jump Rogue_HotdogPrep
                    "You pull back before you really get it in."
                    $ RogueX.change_face("bemused", 1)
                    if RogueX.action_counter["hotdog"]:
                        ch_r "Well ok, [RogueX.player_petname], it has been kinda fun."
                    else:
                        ch_r "Well ok, [RogueX.player_petname], that's a bit dirty, maybe ask a girl?"
                "You'll see.":
                    $ RogueX.change_stat("love", 80, -10, 1)
                    $ RogueX.change_stat("love", 200, -8)
                    "You grind against her asscrack."
                    $ RogueX.change_stat("obedience", 70, 3)
                    $ RogueX.change_stat("inhibition", 50, 3)
                    if not ApprovalCheck(RogueX, 500, "O", TabM=1):
                        $ RogueX.change_face("angry")
                        "[RogueX.name] shoves you away."
                        ch_r "Dick!"
                        ch_r "If that's how you want want to act, I'm out of here!"
                        $ RogueX.change_stat("love", 50, -10, 1)
                        $ RogueX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        call Rogue_Sex_Reset
                        $ RogueX.recent_history.append("angry")
                        $ RogueX.daily_history.append("angry")
                    else:
                        $ RogueX.change_face("sad")
                        "[RogueX.name] doesn't seem to be into this, but she knows her place."
                        jump Rogue_HotdogPrep
        return


    if not RogueX.action_counter["hotdog"] and "no_hotdog" not in RogueX.recent_history:
        $ RogueX.change_face("surprised", 1)
        $ RogueX.mouth = "kiss"
        ch_r "Wait, so you want to grind against my butt?!"

        if RogueX.Forced:
            $ RogueX.change_face("sad")
            ch_r ". . . That's all?"


    if not RogueX.action_counter["hotdog"] and Approval:
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
        elif RogueX.love >= (RogueX.obedience + RogueX.inhibition):
            $ RogueX.change_face("sexy")
            $ RogueX.brows = "sad"
            $ RogueX.mouth = "smile"
            ch_r "It looks like you need some relief. . ."
        elif RogueX.obedience >= RogueX.inhibition:
            $ RogueX.change_face("normal")
            ch_r "If that's what you need, [RogueX.player_petname]."
        elif RogueX.addiction >= 50:
            $ RogueX.change_face("manic", 1)
            ch_r "Hmmm. . ."
        else:
            $ RogueX.change_face("sad")
            $ RogueX.mouth = "smile"
            ch_r "Hmm, you look ready for it, at least. . ."

    elif Approval:
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
            ch_r "That's all you want?"
        elif not Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "Well, at least you got us some privacy this time. . ."
        elif "hotdog" in RogueX.recent_history:
            $ RogueX.change_face("sexy", 1)
            ch_r "You want to go again? Ok."
            jump Rogue_HotdogPrep
        elif "hotdog" in RogueX.daily_history:
            $ RogueX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",                 
                "So you'd like another go?",                 
                "You can't stay away from this booty. . .", 
                "Are you sure that's all you want?"])
            ch_r "[Line]"
        elif RogueX.action_counter["hotdog"] < 3:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.brows = "confused"
            $ RogueX.mouth = "kiss"
            ch_r "So you'd like another go?"
        else:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                "So you'd like another go?",                 
                "You can't stay away from this booty.", 
                "You want me to slick your pole?"])
            ch_r "[Line]"
        $ Line = 0

    if Approval >= 2:
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("obedience", 80, 1)
            $ RogueX.change_stat("inhibition", 60, 1)
            ch_r "Ok, fine."
        elif "no_hotdog" in RogueX.daily_history:
            ch_r "Well, I guess it's not so bad. . ."
        else:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.change_stat("love", 80, 1)
            $ RogueX.change_stat("inhibition", 50, 2)
            $ Line = renpy.random.choice(["Well, sure, give it a rub.",                 
                "Well. . . ok.",                 
                "Sure!", 
                "I guess we could do that.",
                "Hells yeah.",
                "Heh, ok, ok."])
            ch_r "[Line]"
            $ Line = 0
        $ RogueX.change_stat("obedience", 60, 1)
        $ RogueX.change_stat("inhibition", 70, 2)
        jump Rogue_HotdogPrep
    else:

        $ RogueX.change_face("angry")
        if "no_hotdog" in RogueX.recent_history:
            ch_r "I {i}just{/i} told you \"no,\" [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history and "no_hotdog" in RogueX.daily_history:
            ch_r "I told you that I didn't want you rubb'in up on me in public!"
        elif "no_hotdog" in RogueX.daily_history:
            ch_r "I told you \"no\" earlier, [RogueX.player_petname]."
        elif Taboo and "no_taboo" in RogueX.daily_history:
            ch_r "I told you that I didn't want you rubb'in up on me in public!"
        elif not RogueX.action_counter["hotdog"]:
            $ RogueX.change_face("bemused")
            ch_r "That's kinda naughty, [RogueX.player_petname]. . ."
        else:
            $ RogueX.change_face("bemused")
            ch_r "Not, right now [RogueX.player_petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_hotdog" in RogueX.daily_history:
                $ RogueX.change_face("bemused")
                ch_r "Yeah, ok, [RogueX.player_petname]."
                return
            "Maybe later?" if "no_hotdog" not in RogueX.daily_history:
                $ RogueX.change_face("sexy")
                ch_r "Yeah, maybe, [RogueX.player_petname]."
                $ RogueX.change_stat("love", 80, 1)
                $ RogueX.change_stat("inhibition", 50, 1)
                if Taboo:
                    $ RogueX.recent_history.append("no_taboo")
                    $ RogueX.daily_history.append("no_taboo")
                $ RogueX.recent_history.append("no_hotdog")
                $ RogueX.daily_history.append("no_hotdog")
                return
            "You might like it. . .":
                if Approval:
                    $ RogueX.change_face("sexy")
                    $ RogueX.change_stat("obedience", 60, 2)
                    $ RogueX.change_stat("inhibition", 50, 2)
                    $ Line = renpy.random.choice(["Well, sure, give it a rub.",     
                        "I suppose. . .", 
                        "You've got me there."])
                    ch_r "[Line]"
                    $ Line = 0
                    jump Rogue_HotdogPrep
                else:
                    pass
            "Bend over.":

                $ Approval = ApprovalCheck(RogueX, 350, "OI", TabM = 3)
                if Approval > 1 or (Approval and RogueX.Forced):
                    $ RogueX.change_face("sad")
                    $ RogueX.change_stat("love", 70, -2, 1)
                    $ RogueX.change_stat("love", 200, -2)
                    ch_r "Ok, fine. Whatever."
                    $ RogueX.change_stat("obedience", 80, 4)
                    $ RogueX.change_stat("inhibition", 60, 2)
                    $ RogueX.Forced = 1
                    jump Rogue_HotdogPrep
                else:
                    $ RogueX.change_stat("love", 200, -10)
                    $ RogueX.recent_history.append("angry")
                    $ RogueX.daily_history.append("angry")


    $ RogueX.ArmPose = 1

    if "no_hotdog" in RogueX.daily_history:
        ch_r "I just don't want to, [RogueX.player_petname]."
        $ RogueX.recent_history.append("angry")
        $ RogueX.daily_history.append("angry")
    if RogueX.Forced:
        $ RogueX.change_face("angry", 1)
        ch_r "Even that's not worth it."
        $ RogueX.change_stat("lust", 200, 5)
        if RogueX.love > 300:
            $ RogueX.change_stat("love", 70, -1)
        $ RogueX.change_stat("obedience", 50, -1)
        $ RogueX.recent_history.append("angry")
        $ RogueX.daily_history.append("angry")
    elif Taboo:
        $ RogueX.change_face("angry", 1)
        $ RogueX.recent_history.append("no_taboo")
        $ RogueX.daily_history.append("no_taboo")
        ch_r "I'd be a bit embarassed doing that here."
        $ RogueX.change_stat("lust", 200, 5)
        $ RogueX.change_stat("obedience", 50, -3)
    elif RogueX.action_counter["hotdog"]:
        $ RogueX.change_face("sad")
        ch_r "Eh-eh, not anymore, [RogueX.player_petname]."
    else:
        $ RogueX.change_face("normal", 1)
        ch_r "Not interested."
    $ RogueX.recent_history.append("no_hotdog")
    $ RogueX.daily_history.append("no_hotdog")
    $ approval_bonus = 0
    return

label Rogue_HotdogPrep:
    call Seen_First_Peen (RogueX, Partner, React=action_context)
    $ RogueX.pose = "doggy"
    call Rogue_Sex_Launch ("hotdog")

    if action_context == RogueX:

        $ action_context = 0
        "[RogueX.name] turns and backs up against your cock, rubbing it against her ass."
        menu:
            "What do you do?"
            "Go with it.":
                $ RogueX.change_stat("inhibition", 50, 3)
                "[RogueX.name] starts to grind against you."
            "Praise her.":
                $ RogueX.change_face("sexy", 1)
                $ RogueX.change_stat("inhibition", 80, 2)
                ch_p "Hmmm, that's good, [RogueX.petname]."
                $ RogueX.nameCheck()
                "[RogueX.name] starts to grind against you."
                $ RogueX.change_stat("love", 85, 1)
                $ RogueX.change_stat("obedience", 60, 2)
            "Ask her to stop.":
                $ RogueX.change_face("surprised")
                $ RogueX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [RogueX.petname]."
                $ RogueX.nameCheck()
                "[RogueX.name] pulls back."
                $ RogueX.change_stat("obedience", 80, 1)
                $ RogueX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ RogueX.AddWord(1,"refused","refused")
                return
    elif action_context != "auto":
        call Bottoms_Off (RogueX)

        if Taboo:
            if RogueX.action_counter["hotdog"]:
                "[RogueX.name] glances around to see if anyone notices what she's doing, then backs her ass up against your cock."
            else:

                "[RogueX.name] glances around for voyeurs. . ."
                "She hesitantly pulls down your pants and slowly backs up against your rigid member."
            $ RogueX.inhibition += int(Taboo/10)
            $ RogueX.lust += int(Taboo/5)
        else:
            if not RogueX.action_counter["hotdog"]:
                "[RogueX.name] bends over and presses her backside against you suggestively."
            else:
                "[RogueX.name] hesitantly pulls down your pants slowly backs up against your rigid member."
    else:

        "You press yourself against her ass."

    if not RogueX.action_counter["hotdog"]:
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -5)
            $ RogueX.change_stat("obedience", 70, 20)
            $ RogueX.change_stat("inhibition", 80, 10)
        else:
            $ RogueX.change_stat("love", 90, 20)
            $ RogueX.change_stat("obedience", 70, 20)
            $ RogueX.change_stat("inhibition", 80, 20)


    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    $ primary_action = "hotdog"
    $ action_speed = 1
    if Taboo:
        $ RogueX.DrainWord("no_taboo")
    $ RogueX.DrainWord("no_hotdog")
    $ RogueX.recent_history.append("hotdog")
    $ RogueX.daily_history.append("hotdog")

label Rogue_Hotdog_Cycle:
    while Round > 0:
        call shift_focus (RogueX)
        call Rogue_Sex_Launch ("hotdog")
        $ RogueX.lust_face()
        if action_speed:
            $ Player.Cock = "out"
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

                    call Slap_Ass (RogueX)
                    $ counter += 1
                    $ Round -= 1
                    jump Rogue_Hotdog_Cycle
                "Turn her Around":

                    $ RogueX.pose = "doggy" if RogueX.pose != "doggy" else "sex"
                    "You turn her around. . ."
                    jump Rogue_Hotdog_Cycle

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
                                    "How about sex?":
                                        $ action_context = "shift"
                                        call Rogue_HotdogAfter
                                        call Rogue_Sex_P
                                    "Just stick it in her pussy [[without asking].":
                                        $ action_context = "auto"
                                        call Rogue_HotdogAfter
                                        call Rogue_Sex_P
                                    "How about anal?":
                                        $ action_context = "shift"
                                        call Rogue_HotdogAfter
                                        call Rogue_Sex_A
                                    "Just stick it in her ass [[without asking].":
                                        $ action_context = "auto"
                                        call Rogue_HotdogAfter
                                        call Rogue_Sex_A
                                    "Never Mind":
                                        jump Rogue_Hotdog_Cycle
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
                                    jump Rogue_Hotdog_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Rogue_Hotdog_Cycle
                                "Never mind":
                                    jump Rogue_Hotdog_Cycle
                        "Just take a look at her.":
                            $ Player.Cock = 0
                            $ action_speed = 0

                        "Show her feet" if not ShowFeet and (RogueX.pose == "doggy" or RogueX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (RogueX.pose == "doggy" or RogueX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [RogueX.name]":

                            call Girl_Undress (RogueX)
                        "Clean up [RogueX.name] (locked)" if not RogueX.Spunk:
                            pass
                        "Clean up [RogueX.name]" if RogueX.Spunk:
                            call Girl_Cleanup (RogueX, "ask")
                        "Never mind":
                            jump Rogue_Hotdog_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Rogue_Sex_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Rogue_HotdogAfter
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Rogue_Sex_Reset
                    $ Line = 0
                    jump Rogue_HotdogAfter


        call shift_focus (RogueX)
        call Sex_Dialog (RogueX, Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or RogueX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (RogueX)
                if "angry" in RogueX.recent_history:
                    call Rogue_Sex_Reset
                    return
                $ RogueX.change_stat("lust", 200, 5)
                if 100 > RogueX.lust >= 70 and RogueX.session_orgasms < 2:
                    $ RogueX.recent_history.append("unsatisfied")
                    $ RogueX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Rogue_HotdogAfter
                $ Line = "came"

            if RogueX.lust >= 100:

                call Girl_Cumming (RogueX)
                if action_context == "shift" or "angry" in RogueX.recent_history:
                    jump Rogue_HotdogAfter

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "She's emptied you out, you'll need to take a break."
                    jump Rogue_HotdogAfter
                elif "unsatisfied" in RogueX.recent_history:

                    $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                    "[Line] Keep going?"
                    menu:
                        extend ""
                        "Yes, keep going for a bit." if Player.semen:
                            $ Line = "You get back into it"
                            jump Rogue_Hotdog_Cycle
                        "No, I'm done." if Player.semen:
                            "You pull back."
                            jump Rogue_HotdogAfter
                        "No, I'm spent." if not Player.semen:
                            "You pull back."
                            jump Rogue_HotdogAfter
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if RogueX.SEXP >= 100 or ApprovalCheck(RogueX, 1200, "LO"):
            pass
        elif counter == (5 + RogueX.action_counter["hotdog"]):
            $ RogueX.brows = "confused"
            ch_r "Are you getting close here?"
        elif counter == (10 + RogueX.action_counter["hotdog"]):
            $ RogueX.brows = "angry"
            menu:
                ch_r "I'm kinda done with this, [RogueX.player_petname]."
                "How about a BJ?" if RogueX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Rogue_HotdogAfter
                    call Rogue_Blowjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    jump Rogue_Hotdog_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Rogue_Sex_Reset
                    $ action_context = "shift"
                    jump Rogue_HotdogAfter
                "No, get back down there.":
                    if ApprovalCheck(RogueX, 1200) or ApprovalCheck(RogueX, 500, "O"):
                        $ RogueX.change_stat("love", 200, -5)
                        $ RogueX.change_stat("obedience", 50, 3)
                        $ RogueX.change_stat("obedience", 80, 2)
                        "She grumbles but keeps moving."
                    else:
                        $ RogueX.change_face("angry", 1)
                        call Rogue_Sex_Reset
                        "She scowls at you and pulls away."
                        ch_r "Well if that's your attitude you can handle your own business."
                        $ RogueX.change_stat("love", 50, -3, 1)
                        $ RogueX.change_stat("love", 80, -4, 1)
                        $ RogueX.change_stat("obedience", 30, -1, 1)
                        $ RogueX.change_stat("obedience", 50, -1, 1)
                        $ RogueX.recent_history.append("angry")
                        $ RogueX.daily_history.append("angry")
                        jump Rogue_HotdogAfter


        call Escalation (RogueX)

        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."


    $ RogueX.change_face("bemused", 0)
    $ Line = 0
    ch_r "Ok, [RogueX.player_petname], that's enough of that for now."

label Rogue_HotdogAfter:
    if not action_context:
        $ Player.Sprite = 0
        $ Player.Cock = "out"
        call Rogue_Sex_Reset

    $ RogueX.change_face("sexy")

    $ RogueX.action_counter["hotdog"] += 1
    $ RogueX.remaining_actions -=1
    $ RogueX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ RogueX.addiction_rate += 1
    $ RogueX.change_stat("inhibition", 30, 1)
    $ RogueX.change_stat("inhibition", 70, 1)

    call Partner_Like (RogueX, 1)

    if "Rogue Full Buns" in Achievements:
        pass

    elif RogueX.action_counter["hotdog"] >= 10:
        $ RogueX.SEXP += 5
        $ Achievements.append("Rogue Full Buns")
        if not action_context:
            $ RogueX.change_face("smile", 1)
            ch_r "I think I'm getting addicted to this."
    elif RogueX.action_counter["hotdog"] == 1:
        $ RogueX.SEXP += 10
        if not action_context:
            if RogueX.love >= 500 and "unsatisfied" not in RogueX.recent_history:
                ch_r "That was pretty hot, [RogueX.player_petname], we'll have to do that again sometime."
            elif RogueX.obedience <= 500 and Player.focus <= 20:
                $ RogueX.mouth = "sad"
                ch_r "Did you get what you needed here?"
    elif RogueX.action_counter["hotdog"] == 5:
        ch_r "This is. . . interesting."
    elif not action_context:
        if "unsatisfied" in RogueX.recent_history:
            $ RogueX.change_face("angry")
            $ RogueX.eyes = "side"
            ch_r "That didn't really do it for me. . ."

    $ approval_bonus = 0


    call Checkout
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
