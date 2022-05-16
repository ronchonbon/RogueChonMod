
label Storm_SexAct(Act=0):
    if AloneCheck(StormX) and StormX.Taboo == 20:
        $ StormX.Taboo = 0
        $ Taboo = 0
    call shift_focus (StormX)
    if Act == "SkipTo":
        $ renpy.pop_call()
        $ renpy.pop_call()

        call SkipTo (StormX)
    elif Act == "switch":
        $ renpy.pop_call()


    elif Act == "masturbate":
        call Storm_M_Prep
        if not action_context:
            return
    elif Act == "lesbian":
        call Les_Prep (StormX)
        if not action_context:
            return
    elif Act == "kissing":
        call KissPrep (StormX)
        if not action_context:
            return
    elif Act == "breasts":
        call Storm_Fondle_Breasts
        if not action_context:
            return
    elif Act == "blowjob":
        call Storm_BJ_Prep
        if not action_context:
            return
    elif Act == "handjob":
        call Storm_HJ_Prep
        if not action_context:
            return
    elif Act == "sex":
        call Storm_SexPrep
        if not action_context:
            return

label Storm_SexMenu:
    call shift_focus (StormX)
    $ primary_action = 0
    $ offhand_action = 0
    $ girl_offhand_action = 0
    $ action_context = 0
    call Storm_Hide
    $ StormX.ArmPose = 1
    if "detention" in StormX.recent_history:
        $ approval_bonus = 20 if approval_bonus <= 20 else approval_bonus
    call set_the_scene (1, 0, 0, 0, 1)

    if not Player.semen:
        "You're a little out of juice at the moment, you might want to wait a bit."
    if Player.focus >= 95:
        "You're practically buzzing, the slightest breeze could set you off."
    if not StormX.remaining_actions:
        "[StormX.name]'s looking a bit tired out, maybe let her rest a bit."

    if "caught" in StormX.recent_history or "angry" in StormX.recent_history:
        if StormX.location == bg_current:
            ch_s "I do not want to deal with you right now."
        $ StormX.change_outfit()
        $ StormX.DrainWord("caught",1,0)
        return

    if Round < 5:
        ch_s "I think we could both do with a short break."
        return
    menu Storm_SMenu:
        ch_s "So, what was it you hoped to do?"
        "Do you want to make out?":
            if StormX.remaining_actions:
                call Makeout (StormX)
            else:
                ch_s "I am sorry, [StormX.player_petname], I need to take a break."
        "Could I touch you?":

            if StormX.remaining_actions:
                $ StormX.change_face("sly")
                menu:
                    ch_s "What did you wish to touch, [StormX.player_petname]?"
                    "Could I give you a massage?":
                        call Massage (StormX)
                    "Your breasts?":
                        call Storm_Fondle_Breasts
                    "Suck your breasts?" if StormX.remaining_actions and StormX.action_counter["suck_breasts"]:
                        call Storm_Suck_Breasts
                    "Your thighs?" if StormX.remaining_actions:
                        call Storm_Fondle_Thighs
                    "Your pussy?" if StormX.remaining_actions:
                        call Storm_Fondle_Pussy
                    "Lick your pussy?" if StormX.remaining_actions and StormX.action_counter["eat_pussy"]:
                        call Storm_Lick_Pussy
                    "Your Ass?":
                        call Storm_Fondle_Ass
                    "Never mind [[something else]":
                        jump Storm_SMenu
            else:
                ch_s "I'm sorry, [StormX.player_petname], but I need a break."
        "Could you take care of something for me? [[Your dick, you mean your dick]":

            if Player.semen and StormX.remaining_actions:
                menu:
                    ch_s "What did you want me to do?"
                    "Could you give me a handjob?":
                        call Storm_Handjob
                    "Could you give me a titjob?":
                        call Storm_Titjob
                    "Could you suck my cock?":
                        call Storm_Blowjob
                    "Could use your feet?":
                        call Storm_Footjob
                    "Never mind [[something else]":
                        jump Storm_SMenu
            elif not StormX.remaining_actions:
                ch_s "I am sorry, [StormX.player_petname], I need to take a break."
            else:
                "You really don't have it in you, maybe take a break."
        "Could you put on a show for me?":

            menu:
                ch_s "What did you want to see?"
                "Dance for me?":
                    if StormX.remaining_actions:
                        call Group_Strip (StormX)
                    else:
                        ch_s "I am sorry, [StormX.player_petname], I need to take a break."
                "Could you undress for me?":

                    call Girl_Undress (StormX)

                "You've got a little something. . . [[clean-up]" if StormX.Spunk:
                    ch_s "Oh, what do you mean?"
                    call Girl_Cleanup (StormX, "ask")
                "Could I watch you get yourself off? [[masturbate]":

                    if StormX.remaining_actions:
                        call Storm_Masturbate
                    else:
                        ch_s "I am sorry, [StormX.player_petname], I need to take a break."

                "Maybe make out with [RogueX.name]?" if RogueX.location == bg_current:
                    call LesScene (StormX)
                "Maybe make out with [KittyX.name]?" if KittyX.location == bg_current:
                    call LesScene (StormX)
                "Maybe make out with [EmmaX.name]?" if EmmaX.location == bg_current:
                    call LesScene (StormX)
                "Maybe make out with [LauraX.name]?" if LauraX.location == bg_current:
                    call LesScene (StormX)
                "Maybe make out with [JeanX.name]?" if JeanX.location == bg_current:
                    call LesScene (StormX)
                "Maybe make out with [JubesX.name]?" if JubesX.location == bg_current:
                    call LesScene (StormX)
                "Never mind [[something else]":

                    jump Storm_SMenu
        "Could we maybe?. . . [[fuck]":




            if StormX.remaining_actions:
                menu:
                    "What did you want to do?"
                    "Come over here, I've got something in mind. . .":
                        if Player.semen:
                            call Storm_Sex_H
                        else:
                            "The spirit is apparently willing, but the flesh is spongy and bruised."
                    "Fuck your pussy.":
                        if Player.semen:
                            call Storm_Sex_P
                        else:
                            "The spirit is apparently willing, but the flesh is spongy and bruised."
                    "Fuck your ass.":
                        if Player.semen:
                            call Storm_Sex_A
                        else:
                            "The spirit is apparently willing, but the flesh is spongy and bruised."
                    "How about some toys? [[Pussy]":
                        call Storm_Dildo_Pussy
                    "How about some toys? [[Anal]":
                        call Storm_Dildo_Ass
                    "Never mind [[something else]":
                        jump Storm_SMenu
            else:
                ch_s "I am sorry, [StormX.player_petname], I need to take a break."
        "Hey, do you want in on this? [[Threesome]":

            call Sex_Menu_Threesome (StormX)
            jump Storm_SMenu

        "Hey, [Partner.name]? [[Switch lead]" if Partner:
            call expression Partner.Tag + "_SexAct" pass ("switch")
            return

        "Cheat Menu" if config.developer:
            call Cheat_Menu (StormX)
        "Never mind. [[exit]":
            if StormX.lust >= 50 or StormX.addiction >= 50:
                $ StormX.change_face("sad")
                if StormX.remaining_actions and StormX.SEXP >= 15 and Round > 20:
                    if "round2" not in StormX.recent_history:
                        ch_s "Are you certain, [StormX.player_petname]? Are you perhaps forgetting something?"
                        $ StormX.change_stat("inhibition", 30, 2)
                        $ StormX.change_stat("inhibition", 50, 1)
                    elif StormX.addiction >= 50:
                        ch_s "I need your touch."
                    else:
                        ch_s "That was not enough to satisfy me."
                    menu:
                        extend ""
                        "Yeah, I'm done for now." if Player.semen and "round2" not in StormX.recent_history:
                            if "unsatisfied" in StormX.recent_history and not StormX.session_orgasms:
                                $ StormX.change_face("angry")
                                $ StormX.eyes = "side"
                                $ StormX.change_stat("love", 70, -2)
                                $ StormX.change_stat("love", 90, -4)
                                $ StormX.change_stat("obedience", 30, 2)
                                $ StormX.change_stat("obedience", 70, 1)
                                ch_s "Perhaps I need to teach you to be more generous."
                            else:
                                $ StormX.change_face("bemused", 1)
                                $ StormX.change_stat("obedience", 50, 2)
                                ch_s "Perhaps I need to teach you to be more generous."
                        "I gave it a shot." if "round2" in StormX.recent_history:
                            if "unsatisfied" in StormX.recent_history and not StormX.session_orgasms:
                                $ StormX.change_face("angry")
                                $ StormX.eyes = "side"
                                ch_s "So that was the best you could achieve. . ."
                            else:
                                $ StormX.change_face("bemused", 1)
                                ch_s "So that was the best you could achieve. . ."
                        "Hey, I did my part." if StormX.session_orgasms > 2:
                            $ StormX.change_face("sly", 1)
                            ch_s "I had hoped for better. . ."
                        "I'm tapped out for the moment, let's try again later." if not Player.semen:
                            $ StormX.change_face("normal")
                            ch_s "Well, I cannot push you to breaking. . ."
                        "Ok, we can try something else." if multi_action and "round2" not in StormX.recent_history:
                            $ StormX.change_face("smile")
                            $ StormX.change_stat("love", 70, 2)
                            $ StormX.change_stat("love", 90, 1)
                            ch_s "Thank you."
                            $ StormX.recent_history.append("round2")
                            $ StormX.daily_history.append("round2")
                            jump Storm_SexMenu
                        "Again? Ok, fine." if multi_action and "round2" in StormX.recent_history:
                            $ StormX.change_face("sly")
                            ch_s "Always. . ."
                            jump Storm_SexMenu
                else:

                    $ StormX.change_face("bemused", 1)
                    ch_s "I could use some rest as well, [StormX.player_petname]."
                    $ StormX.change_stat("inhibition", 30, 2)
                    $ StormX.change_stat("inhibition", 50, 1)
                $ StormX.change_face()
            else:
                ch_s "That is fine."
            call Sex_Over
            return
    if StormX.location != bg_current:
        call set_the_scene
        call Trig_Reset
        return
    if not multi_action:
        call set_the_scene
        ch_s "I think that you have had enough for the moment."
        $ StormX.session_orgasms = 0
        call Trig_Reset
        return
    call GirlsAngry
    jump Storm_SexMenu





label Storm_Masturbate:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (StormX)
    if StormX.action_counter["masturbation"]:
        $ approval_bonus += 10
    if StormX.SEXP >= 50:
        $ approval_bonus += 25
    elif StormX.SEXP >= 30:
        $ approval_bonus += 15
    elif StormX.SEXP >= 15:
        $ approval_bonus += 5
    if StormX.lust >= 90:
        $ approval_bonus += 20
    elif StormX.lust >= 75:
        $ approval_bonus += 5
    if "exhibitionist" in StormX.Traits:
        $ approval_bonus += (3*Taboo)
    if StormX in Player.Harem or "sex friend" in StormX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in StormX.Traits:
        $ approval_bonus -= 40
    if StormX.event_counter["forced"] and not StormX.Forced:
        $ approval_bonus -= 5*StormX.event_counter["forced"]

    $ Approval = ApprovalCheck(StormX, 1300, TabM = 2)

    $ StormX.DrainWord("unseen",1,0)

    if action_context == "join":
        if Approval > 1 or (Approval and StormX.lust >= 50):
            $ Player.AddWord(1,"join")
            menu:
                extend ""
                "Would you like some help? I could lend some helping hands. . ." if Player.semen and StormX.remaining_actions:
                    $ StormX.change_stat("love", 90, 1)
                    $ StormX.change_stat("obedience", 50, 2)
                    $ StormX.change_face("sexy")
                    ch_s "You could give me a breast massage. . ."
                    $ StormX.change_stat("obedience", 70, 2)
                    $ StormX.change_stat("inhibition", 70, 1)
                    $ offhand_action = "fondle_breasts"
                    $ StormX.action_counter["masturbation"] += 1
                    jump Storm_M_Cycle
                "Would you like some help? I could. . . up to you, I guess." if Player.semen and StormX.remaining_actions:
                    $ StormX.change_stat("love", 70, 2)
                    $ StormX.change_stat("love", 90, 1)
                    $ StormX.change_face("sexy")
                    ch_s "You could give me a breast massage. . ."
                    $ StormX.change_stat("obedience", 70, 2)
                    $ StormX.change_stat("inhibition", 70, 1)
                    $ D20 = renpy.random.randint(1, 20)
                    if D20 > 10:
                        $ offhand_action = "fondle_breasts"
                    else:
                        $ offhand_action = "suck_breasts"
                    $ StormX.action_counter["masturbation"] += 1
                    jump Storm_M_Cycle
                "Why don't we take care of each other?" if Player.semen and StormX.remaining_actions:
                    $ StormX.change_face("sexy")
                    ch_s "Oh, what did you have in mind?"
                    $ renpy.pop_call()
                    return
                "You look like you have things well in hand. . .":
                    if StormX.lust >= 50:
                        $ StormX.change_stat("love", 70, 2)
                        $ StormX.change_stat("love", 90, 1)
                        $ StormX.change_face("sexy")
                        ch_s "I see you prefer to watch. . ."
                        $ StormX.change_stat("obedience", 80, 3)
                        $ StormX.change_stat("inhibition", 80, 5)
                        jump Storm_M_Cycle
                    elif ApprovalCheck(StormX, 1200):
                        $ StormX.change_face("sly")
                        ch_s "True, but I was not expecting an audience."
                    else:
                        $ StormX.change_face("angry")
                        ch_s "Well, I had, before you interrupted. . ."


        $ StormX.ArmPose = 1
        $ StormX.change_outfit()
        $ StormX.remaining_actions -= 1
        $ Player.change_stat("focus", 50, 30)
        call Checkout (1)
        $ Line = 0
        $ action_context = 0
        $ renpy.pop_call()
        if Approval:
            $ StormX.change_face("bemused", 2)
            if bg_current == "bg_storm":
                ch_s "What brought you here?"
            else:
                ch_s "I did not expect interruptions. . ."
            $ StormX.blushing = 0
        else:
            $ StormX.change_stat("love", 200, -5)
            $ StormX.change_face("angry")
            $ StormX.recent_history.append("angry")
            $ StormX.daily_history.append("angry")
            if bg_current == "bg_storm":
                ch_s "I am afraid that I do not have time to deal with you right now. . ."
                "[StormX.name] kicks you out of her room."
                $ renpy.pop_call()
                jump Campus_Map
            else:
                ch_s "I will be leaving now, if you do not mind."
                call Remove_Girl (StormX)
        return




    if action_context == StormX:
        if Approval > 2:
            if StormX.PantsNum() == 5:
                "[StormX.name]'s hand snakes down her body, and hikes up her skirt."
                $ StormX.Upskirt = 1
            elif StormX.PantsNum() > 6:
                "[StormX.name] slides her hand down her body and into her pants."
            elif StormX.HoseNum() >= 5:
                "[StormX.name]'s hand slides down her body and under her [StormX.hose]."
            elif StormX.underwear:
                "[StormX.name]'s hand slides down her body and under her [StormX.underwear]."
            else:
                "[StormX.name]'s hand slides down her body and begins to caress her pussy."
            $ StormX.SeenPanties = 1
            "She starts to slowly rub herself."
            call Storm_First_Bottomless
            menu:
                "What do you do?"
                "Nothing.":
                    $ StormX.change_stat("inhibition", 80, 3)
                    $ StormX.change_stat("inhibition", 60, 2)
                    "[StormX.name] begins to masturbate."
                "Go for it.":
                    $ StormX.change_face("sexy, 1")
                    $ StormX.change_stat("inhibition", 80, 3)
                    ch_p "That is so sexy, [StormX.petname]."
                    $ StormX.nameCheck()
                    "You lean back and enjoy the show."
                    $ StormX.change_stat("love", 80, 1)
                    $ StormX.change_stat("obedience", 90, 1)
                    $ StormX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ StormX.change_face("surprised")
                    $ StormX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that right now, [StormX.petname]."
                    $ StormX.nameCheck()
                    "[StormX.name] pulls her hands away from herself."
                    $ StormX.change_outfit()
                    $ StormX.change_stat("obedience", 90, 1)
                    $ StormX.change_stat("obedience", 50, 1)
                    $ StormX.change_stat("obedience", 30, 2)
                    return
            jump Storm_M_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
        return



    if not StormX.action_counter["masturbation"]:
        $ StormX.change_face("surprised", 1)
        $ StormX.mouth = "kiss"
        ch_s "Oh, so you like the watch? . ."
        if StormX.Forced:
            $ StormX.change_face("sad")
            ch_s "and that is -all- that you expect?"



    if not StormX.action_counter["masturbation"] and Approval:
        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
        elif StormX.love >= StormX.obedience and StormX.love >= StormX.inhibition:
            $ StormX.change_face("sexy")
            $ StormX.brows = "sad"
            $ StormX.mouth = "smile"
            ch_s "I am usually alone for this . . ."
        elif StormX.obedience >= StormX.inhibition:
            $ StormX.change_face("normal")
            ch_s "If you enjoy watching, [StormX.player_petname]. . ."
        else:
            $ StormX.change_face("sad")
            $ StormX.mouth = "smile"
            ch_s "I do not mind an audience . . ."



    elif Approval:
        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
            ch_s "You only like to watch?"
        elif Approval and "masturbation" in StormX.recent_history:
            $ StormX.change_face("sexy", 1)
            ch_s "I suppose that I was not. . . finished. . ."
            jump Storm_M_Prep
        elif Approval and "masturbation" in StormX.daily_history:
            $ StormX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["I put on quite the show?",       
                    "You did not get enough earlier?",
                    "I did enjoy the audience participation. . ."])
            ch_s "[Line]"
        elif StormX.action_counter["masturbation"] < 3:
            $ StormX.change_face("sexy", 1)
            $ StormX.brows = "confused"
            ch_s "You enjoyed the show?"
        else:
            $ StormX.change_face("sexy", 1)
            $ StormX.ArmPose = 2
            $ Line = renpy.random.choice(["You really do like to watch.",                 
                    "Once more?",                 
                    "You enjoy watching me do that?",
                    "You want me to take care of myself?"])
            ch_s "[Line]"
            $ Line = 0



    if Approval >= 2:
        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("obedience", 90, 1)
            $ StormX.change_stat("inhibition", 60, 1)
            ch_s ". . .Fine"
        else:
            $ StormX.change_face("sexy", 1)
            $ StormX.change_stat("love", 90, 1)
            $ StormX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Fine.",                 
                    "It could not hurt having you around. . .",
                    "Very well.", 
                    "Sure, why not?",
                    "[[chuckles]. . . Fine."])
            ch_s "[Line]"
            $ Line = 0
        $ StormX.change_stat("obedience", 20, 1)
        $ StormX.change_stat("obedience", 60, 1)
        $ StormX.change_stat("inhibition", 70, 2)
        jump Storm_M_Prep
    else:


        menu:
            ch_s "I am unsure about this."
            "Maybe later?":
                $ StormX.change_face("sexy", 1)
                if StormX.lust > 70:
                    ch_s "I expect that I will be finished by then. . ."
                else:
                    ch_s "We shall see."
                $ StormX.change_stat("love", 80, 2)
                $ StormX.change_stat("inhibition", 70, 2)
                return
            "You look like you could use it. . .":
                if Approval:
                    $ StormX.change_face("sexy")
                    $ StormX.change_stat("obedience", 90, 2)
                    $ StormX.change_stat("obedience", 50, 2)
                    $ StormX.change_stat("inhibition", 70, 3)
                    $ StormX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["You really do like to watch.",                 
                            "Once more?",                 
                            "You enjoy watching me do that?",
                            "You want me to take care of myself?"])
                    ch_s "[Line]"
                    $ Line = 0
                    jump Storm_M_Prep
            "Just get at it already.":

                $ Approval = ApprovalCheck(StormX, 450, "OI", TabM = 2)
                if Approval > 1 or (Approval and StormX.Forced):
                    $ StormX.change_face("sad")
                    $ StormX.change_stat("love", 70, -5, 1)
                    $ StormX.change_stat("love", 200, -5)
                    ch_s "Fine, if you insist."
                    $ StormX.change_stat("obedience", 80, 4)
                    $ StormX.change_stat("inhibition", 80, 1)
                    $ StormX.change_stat("inhibition", 60, 3)
                    $ StormX.Forced = 1
                    jump Storm_M_Prep
                else:
                    $ StormX.change_stat("love", 200, -20)
                    $ StormX.recent_history.append("angry")
                    $ StormX.daily_history.append("angry")



    $ StormX.ArmPose = 1
    if StormX.Forced:
        $ StormX.change_face("angry", 1)
        ch_s "I will not do that."
        $ StormX.change_stat("lust", 90, 5)
        if StormX.love > 300:
            $ StormX.change_stat("love", 70, -2)
        $ StormX.change_stat("obedience", 50, -2)
        $ StormX.recent_history.append("angry")
        $ StormX.daily_history.append("angry")
        $ StormX.recent_history.append("no_masturbation")
        $ StormX.daily_history.append("no_masturbation")
        return
    elif Taboo:
        $ StormX.change_face("angry", 1)
        $ StormX.daily_history.append("no_taboo")
        ch_s "I cannot do that here."
        $ StormX.change_stat("lust", 90, 5)
        $ StormX.change_stat("obedience", 50, -3)
        return
    elif StormX.action_counter["masturbation"]:
        $ StormX.change_face("sad")
        ch_s "I expect that you can entertain yourself elsewhere."
    else:
        $ StormX.change_face("normal", 1)
        ch_s "I do not think so, [StormX.player_petname]."
    $ StormX.recent_history.append("no_masturbation")
    $ StormX.daily_history.append("no_masturbation")
    $ approval_bonus = 0
    return

label Storm_M_Prep:
    $ StormX.Upskirt = 1
    $ StormX.underwearDown = 1
    call Storm_First_Bottomless (1)
    call set_the_scene (Dress=0)


    if "unseen" in StormX.recent_history:
        $ StormX.change_face("sexy")
        $ StormX.eyes = "closed"
        $ StormX.ArmPose = 2
        "You see [StormX.name] leaning back, masturbating. You don't think she's noticed you yet."
    else:
        $ StormX.change_face("sexy")
        $ StormX.ArmPose = 2
        "[StormX.name] lays back and starts to toy with herself."
        if not StormX.action_counter["masturbation"]:
            if StormX.Forced:
                $ StormX.change_stat("love", 90, -20)
                $ StormX.change_stat("obedience", 70, 45)
                $ StormX.change_stat("inhibition", 80, 35)
            else:
                $ StormX.change_stat("love", 90, 15)
                $ StormX.change_stat("obedience", 70, 35)
                $ StormX.change_stat("inhibition", 80, 40)


    $ primary_action = "masturbation"
    if not girl_offhand_action:
        $ girl_offhand_action = "fondle_pussy"

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    if Taboo:
        $ StormX.DrainWord("no_taboo")
    $ StormX.DrainWord("no_masturbation")
    $ StormX.recent_history.append("masturbation")
    $ StormX.daily_history.append("masturbation")

label Storm_M_Cycle:
    if action_context == "join":
        $ renpy.pop_call()
        $ action_context = 0

    while Round >=0:
        call Storm_Pos_Reset ("masturbation")
        call shift_focus (StormX)
        $ StormX.lust_face()
        if "unseen" in StormX.recent_history:
            $ StormX.eyes = "closed"

        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if Player.focus < 100:

            menu:
                "Keep Watching.":
                    pass

                "[StormX.name]. . .[[jump in]" if "unseen" not in StormX.recent_history and "join" not in Player.recent_history and StormX.location == bg_current:
                    "[StormX.name] slows what she's doing with a sly grin."
                    ch_s "Enjoying yourself?"
                    $ action_context = "join"
                    call Storm_Masturbate
                "\"Ahem. . .\"" if "unseen" in StormX.recent_history and StormX.location == bg_current:
                    jump Storm_M_Interupted

                "Start jack'in it." if offhand_action != "jackin":
                    call Jackin (StormX)
                "Stop jack'in it." if offhand_action == "jackin":
                    $ offhand_action = 0

                "Slap her ass" if StormX.location == bg_current:
                    if "unseen" in StormX.recent_history:
                        "You smack [StormX.name] firmly on the ass!"
                        jump Storm_M_Interupted
                    else:
                        call Slap_Ass (StormX)
                        $ counter += 1
                        $ Round -= 1
                        jump Storm_M_Cycle

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
                        "Offhand action" if StormX.location == bg_current:
                            if StormX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ StormX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (StormX, "tired")

                        "Threesome actions (locked)" if not Partner or "unseen" in StormX.recent_history or StormX.location != bg_current:
                            pass
                        "Threesome actions" if Partner and "unseen" not in StormX.recent_history and StormX.location == bg_current:
                            menu:
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (StormX)
                                "Swap to [Partner.name]":
                                    call primary_action_Swap (StormX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Storm_M_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Storm_M_Cycle
                                "Never mind":
                                    jump Storm_M_Cycle

                        "Show her feet" if not ShowFeet and (StormX.pose == "doggy" or StormX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (StormX.pose == "doggy" or StormX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [StormX.name]":

                            if "unseen" in StormX.recent_history:
                                ch_p "Oh, yeah, take it off. . ."
                                jump Storm_M_Interupted
                            else:
                                call Girl_Undress (StormX)
                        "Clean up [StormX.name] (locked)" if not StormX.Spunk:
                            pass
                        "Clean up [StormX.name]" if StormX.Spunk:
                            if "unseen" in StormX.recent_history:
                                ch_p "You've got a little something on you. . ."
                                jump Storm_M_Interupted
                            else:
                                call Girl_Cleanup (StormX, "ask")
                        "Never mind":
                            jump Storm_M_Cycle

                "Back to Sex Menu" if multi_action and StormX.location == bg_current:
                    ch_p "Let's try something else."
                    call Storm_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Storm_M_Interupted
                "End Scene" if not multi_action or StormX.location != bg_current:
                    ch_p "Let's stop for now."
                    call Storm_Pos_Reset
                    $ Line = 0
                    jump Storm_M_Interupted


        call shift_focus (StormX)
        call Sex_Dialog (StormX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus

        if Player.focus >= 100 or StormX.lust >= 100:

            if Player.focus >= 100:
                if "unseen" not in StormX.recent_history:

                    call Player_Cumming (StormX)
                    if "angry" in StormX.recent_history:
                        call Storm_Pos_Reset
                        return
                    $ StormX.change_stat("lust", 200, 5)
                    if 100 > StormX.lust >= 70 and StormX.session_orgasms < 2:
                        $ StormX.recent_history.append("unsatisfied")
                        $ StormX.daily_history.append("unsatisfied")
                    $ Line = "came"
                else:
                    "You grunt and try to hold it in."
                    $ Player.focus = 95
                    if StormX.location == bg_current or StormX.location == "bg_desk":
                        jump Storm_M_Interupted


            if StormX.lust >= 100:
                call Girl_Cumming (StormX)
                if StormX.location == bg_current or StormX.location == "bg_desk":
                    jump Storm_M_Interupted

            if Line == "came":
                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."
                    $ offhand_action = 0 if offhand_action == "jackin" else offhand_action


                if "unsatisfied" in StormX.recent_history:
                    "[StormX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Let her keep going?"
                        "Yes, keep going for a bit.":
                            $ Line = "You let her get back into it"
                            jump Storm_M_Cycle
                        "No, I'm done.":
                            "You ask her to stop."
                            return
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        if "unseen" in StormX.recent_history:
            if Round == 10:
                "It's getting a bit late, [StormX.name] will probably be wrapping up soon."
            elif Round == 5:
                "She's definitely going to stop soon."
        else:
            if StormX.location == bg_current:
                call Escalation (StormX)

            if Round == 10:
                ch_s "I will probably take a break soon."
                $ StormX.lust += 10
            elif Round == 5:
                ch_s "Ah! I am nearly finished. . ."
                $ StormX.lust += 25


    $ StormX.change_face("bemused", 0)
    $ Line = 0
    if "unseen" not in StormX.recent_history:
        ch_s "That is enough of that."

label Storm_M_Interupted:


    if "unseen" in StormX.recent_history:
        $ StormX.change_face("surprised", 2)
        "[StormX.name] stops what she's doing with a start, eyes wide."
        call Storm_First_Bottomless (1)
        $ StormX.change_face("confused", 1, Eyes="surprised")
        if StormX.location == "bg_desk":
            $ StormX.location = bg_current
            call Display_Girl (StormX)
            "She approaches you."


        if offhand_action == "jackin":
            ch_s "!"
            ch_s "How long have you been there?!"
            $ StormX.eyes = "down"
            menu:
                ch_s ". . . I notice you're taken care of yourself. . . "
                "A little while, it was an excellent show.":
                    $ StormX.change_face("sexy",1)
                    $ StormX.change_stat("obedience", 50, 3)
                    $ StormX.change_stat("obedience", 70, 2)
                    ch_s "I imagine it was. . ."
                    if StormX.love >= 800 or StormX.obedience >= 500 or StormX.inhibition >= 500:
                        $ approval_bonus += 10
                        $ StormX.change_stat("lust", 90, 5)
                    ch_s "and I have been missing a show myself. . ."
                "I. . . just got here?":

                    $ StormX.change_face("angry",1, Eyes="down")
                    $ StormX.change_stat("love", 70, 2)
                    $ StormX.change_stat("love", 90, 1)
                    $ StormX.change_stat("obedience", 50, 2)
                    $ StormX.change_stat("obedience", 70, 2)
                    "She looks pointedly at your cock,"
                    $ StormX.eyes = "squint"
                    ch_s "Long enough, it would appear. . ."
                    if StormX.love >= 800 or StormX.obedience >= 500 or StormX.inhibition >= 500:
                        $ approval_bonus += 10
                        $ StormX.change_stat("lust", 90, 5)
                        $ StormX.change_face("bemused", 1)
                        ch_s "I expect that you could not contain your enthusiasm. . ."
                    else:
                        $ approval_bonus -= 10
                        $ StormX.change_stat("lust", 200, -5)

            if "Historia" not in Player.Traits:
                call Seen_First_Peen (StormX, Partner)
                ch_s "Hmm. . ."
        else:


            ch_s "!"
            ch_s "How long have you been there?!"
            menu:
                extend ""
                "A little while.":
                    $ StormX.change_face("sexy", 1)
                    $ StormX.change_stat("obedience", 50, 3)
                    $ StormX.change_stat("obedience", 70, 2)
                    ch_s "And I assume you enjoyed the show?"
                "I just got here.":
                    $ StormX.change_face("bemused", 1)
                    $ StormX.change_stat("love", 70, 2)
                    $ StormX.change_stat("love", 90, 1)
                    ch_s "That seems likely. . ."
                    $ StormX.change_stat("obedience", 50, 2)
                    $ StormX.change_stat("obedience", 70, 2)

        $ StormX.DrainWord("unseen",1,0)
        $ StormX.action_counter["masturbation"] += 1
        if "classcaught" not in StormX.history or "Historia" in Player.Traits:

            return
        if Round <= 10:
            ch_s "It seems that it has gotten late while I was. . . distracted."
            return
        $ action_context = "join"
        call Storm_Masturbate
        "error: report this if you see it."
        return



    $ StormX.remaining_actions -= 1
    $ StormX.action_counter["masturbation"] += 1
    call Checkout
    if action_context == "shift":
        $ action_context = 0
        return
    $ action_context = 0

    if Partner == "Kitty":
        call Partner_Like (StormX, 4, 2)
    else:
        call Partner_Like (StormX, 3, 2)

    if StormX.location != bg_current and StormX.location != "bg_desk":
        return

    if Round <= 10:
        ch_s "Give me a moment to recover. . ."
        return
    $ StormX.change_face("sexy", 1)
    if StormX.lust < 20:
        ch_s "I enjoyed that, at least."
    else:
        ch_s "Yes?"
    menu:
        extend ""
        "Well, I have something you could take care of. . ." if Player.semen and StormX.remaining_actions and multi_action:
            $ action_context = "shift"
            return
        "You could just keep going. . ." if Player.semen:
            $ StormX.change_face("sly")
            if StormX.remaining_actions and Round >= 10:
                ch_s "I could. . ."
                jump Storm_M_Cycle
            else:
                ch_s "Give me a moment to recover. . ."
        "I'm good here. [[Stop]":
            if StormX.love < 800 and StormX.inhibition < 500 and StormX.obedience < 500:
                $ StormX.change_outfit()
            $ StormX.change_face("normal")
            $ StormX.brows = "confused"
            ch_s ". . . fine then. . ."
            $ StormX.brows = "normal"
        "You should probably stop for now." if StormX.lust > 30:
            $ StormX.change_face("angry")
            ch_s "I . . . fine . ."
    if offhand_action == "jackin":
        $ offhand_action = 0
    return






label Storm_Sex_P:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (StormX)
    if StormX.action_counter["sex"] >= 7:
        $ approval_bonus += 15
    elif StormX.action_counter["sex"] >= 3:
        $ approval_bonus += 12
    elif StormX.action_counter["sex"]:
        $ approval_bonus += 10

    if StormX.addiction >= 75 and (StormX.event_counter["creampied"] + StormX.event_counter["anal_creampied"]) >=3:
        $ approval_bonus += 20
    elif StormX.addiction >= 75:
        $ approval_bonus += 15

    if StormX.lust > 85:
        $ approval_bonus += 10
    elif StormX.lust > 75:
        $ approval_bonus += 5

    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in StormX.Traits:
        $ approval_bonus += (4*Taboo)
    if StormX in Player.Harem or "sex friend" in StormX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in StormX.Traits:
        $ approval_bonus -= 40
    if StormX.event_counter["forced"] and not StormX.Forced:
        $ approval_bonus -= 5*StormX.event_counter["forced"]



    if Taboo and "no_taboo" in StormX.daily_history:
        $ approval_bonus -= 10

    if "no_sex" in StormX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_sex" in StormX.recent_history else 0


    $ Approval = ApprovalCheck(StormX, 1400, TabM = 5)

    if action_context == "auto":
        call Storm_Sex_Launch ("sex")
        if StormX.PantsNum() == 5:
            "You roll back, pulling [StormX.name] on top of you, sliding her skirt up as you go."
            $ StormX.Upskirt = 1
        elif StormX.PantsNum() >= 6:
            "You roll back, pulling [StormX.name] on top of you, sliding her [StormX.legs] down as you do."
            $ StormX.legs = 0
        else:
            "You roll back, pulling [StormX.name] on top of you."
        $ StormX.SeenPanties = 1
        "You rub the tip of your cock against her moist slit."
        $ StormX.change_face("surprised", 1)

        if (StormX.action_counter["sex"] and Approval) or (Approval > 1):

            "[StormX.name] is briefly startled, but melts into a sly smile."
            $ StormX.change_face("sly")
            $ StormX.change_stat("obedience", 70, 3)
            $ StormX.change_stat("inhibition", 50, 3)
            $ StormX.change_stat("inhibition", 70, 1)
            ch_s "Mmm, if you insist, [StormX.player_petname]."
            jump Storm_SexPrep
        else:

            $ StormX.brows = "angry"
            menu:
                ch_s "Are you certain that is what you want?"
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ StormX.change_face("sexy", 1)
                        $ StormX.change_stat("obedience", 70, 3)
                        $ StormX.change_stat("inhibition", 50, 3)
                        $ StormX.change_stat("inhibition", 70, 1)
                        ch_s "I am willing to give it a try if you are. . ."
                        jump Storm_SexPrep
                    else:
                        "You pull back before you really get it in."
                        $ StormX.change_face("bemused", 1)
                        if StormX.action_counter["sex"]:
                            ch_s "Perhaps ask first, [StormX.player_petname]."
                        else:
                            ch_s "Some other time, perhaps. . ."
                "Just fucking.":
                    $ StormX.change_stat("love", 80, -10, 1)
                    $ StormX.change_stat("love", 200, -10)
                    "You press inside some more."
                    $ StormX.change_stat("obedience", 70, 3)
                    $ StormX.change_stat("inhibition", 50, 3)
                    if not ApprovalCheck(StormX, 700, "O", TabM=1):
                        $ StormX.change_face("angry")
                        "[StormX.name] shoves you away and backhands you in the face."
                        ch_s "That is unfortunate."
                        ch_s "I am afraid that is -not- what will happen here."
                        $ StormX.change_stat("love", 50, -10, 1)
                        $ StormX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        call Storm_Sex_Reset
                        $ StormX.recent_history.append("angry")
                        $ StormX.daily_history.append("angry")
                    else:
                        $ StormX.change_face("sad")
                        "[StormX.name] doesn't seem to be into this, you're lucky she's so obedient."
                        jump Storm_SexPrep
        return



    if not StormX.action_counter["sex"] and "no_sex" not in StormX.recent_history:

        $ StormX.change_face("surprised", 1)
        $ StormX.mouth = "kiss"
        ch_s "Hmm, are you certain you are prepared for this? . . "
        if StormX.Forced:
            $ StormX.change_face("sad")
            ch_s "This is what you would have me do?"


    if not StormX.action_counter["sex"] and Approval:

        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("love", 70, -30, 1)
            $ StormX.change_stat("love", 20, -20, 1)
        elif StormX.love >= (StormX.obedience + StormX.inhibition):
            $ StormX.change_face("sexy")
            $ StormX.brows = "sad"
            $ StormX.mouth = "smile"
            ch_s "I would not want to. . . overwhelm you. . ."
        elif StormX.obedience >= StormX.inhibition:
            $ StormX.change_face("normal")
            ch_s "If that is what you wish, [StormX.player_petname]. . ."
        elif StormX.addiction >= 50:
            $ StormX.change_face("manic", 1)
            ch_s "I was curious as to the effect that would have. . ."
        else:
            $ StormX.change_face("sad")
            $ StormX.mouth = "smile"
            ch_s "I was hoping you would ask. . ."


    elif Approval:

        $ StormX.change_face("sexy", 1)
        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
            ch_s "Oh, again?"
        elif not Taboo and "no_taboo" in StormX.daily_history:
            ch_s "I do suppose this is more private."
        elif "sex" in StormX.recent_history:
            ch_s "Again? [StormX.player_petname], you are a lion!"
            jump Storm_SexPrep
        elif "sex" in StormX.daily_history:
            $ Line = renpy.random.choice(["Back again?",                 
                    "You would like another round?",                 
                    "I suppose that I can be irresistible. . .", 
                    "Did you not get enough earlier?",
                    "You are wearing me out, " + StormX.player_petname + "."])
            ch_s "[Line]"
        elif StormX.action_counter["sex"] < 3:
            $ StormX.brows = "confused"
            $ StormX.mouth = "kiss"
            ch_s "Oh? Another round?"
        else:
            $ Line = renpy.random.choice(["Oh, did you want some of this?",                 
                    "You wouldd like another round?",         
                    "I suppose that I can be irresistible. . .", 
                    "I could get used to this. . .",
                    "Did you want me to ride you?"])
            ch_s "[Line]"
        $ Line = 0


    if Approval >= 2:

        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("obedience", 90, 1)
            $ StormX.change_stat("inhibition", 60, 1)
            ch_s "Oh, very well, if it will satisfy you."
        elif "no_sex" in StormX.daily_history:
            ch_s "Very well, I am convinced. . ."
        else:
            $ StormX.change_face("sexy", 1)
            $ StormX.change_stat("love", 90, 1)
            $ StormX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well. . . fine, I accept.",                 
                    "Of course!", 
                    "We could, I suppose.",
                    "Hmmm, yes.",
                    "How could I refuse?"])
            ch_s "[Line]"
            $ Line = 0
        $ StormX.change_stat("obedience", 20, 1)
        $ StormX.change_stat("obedience", 60, 1)
        $ StormX.change_stat("inhibition", 70, 2)
        jump Storm_SexPrep
    else:


        $ StormX.change_face("angry")
        if "no_sex" in StormX.recent_history:
            ch_s "I am afraid that \"no\" is my final answer, [StormX.player_petname]."
        elif Taboo and "no_taboo" in StormX.daily_history and "no_sex" in StormX.daily_history:
            ch_s "I have already informed you. . . not in such an exposed location."
        elif "no_sex" in StormX.daily_history:
            ch_s "I believe that I just told you \"no,\" [StormX.player_petname]."
        elif Taboo and "no_taboo" in StormX.daily_history:
            ch_s "I have already informed you, this is too public!"
        elif not StormX.action_counter["sex"]:
            $ StormX.change_face("bemused")
            ch_s "I seriously doubt that you understand what you would be in for. . ."
        else:
            $ StormX.change_face("bemused")
            ch_s "Perhaps another time? . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_sex" in StormX.daily_history:
                $ StormX.change_face("bemused")
                ch_s "I can appreciate your. . . desires."
                return
            "Maybe later?" if "no_sex" not in StormX.daily_history:
                $ StormX.change_face("sexy")
                ch_s "Oh, of that I am certain. . ."
                $ StormX.change_stat("love", 80, 2)
                $ StormX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ StormX.recent_history.append("no_taboo")
                    $ StormX.daily_history.append("no_taboo")
                $ StormX.recent_history.append("no_sex")
                $ StormX.daily_history.append("no_sex")
                return
            "I think you'd enjoy it as much as I would. . .":
                if Approval:
                    $ StormX.change_face("sexy")
                    $ StormX.change_stat("obedience", 90, 2)
                    $ StormX.change_stat("obedience", 50, 2)
                    $ StormX.change_stat("inhibition", 70, 3)
                    $ StormX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["I cannot argue with that. . .",     
                                "I suppose you have a point. . .", 
                                "You do raise a worthy point. . ."])
                    ch_s "[Line]"
                    $ Line = 0
                    jump Storm_SexPrep
            "Just deal with it.":
                $ Approval = ApprovalCheck(StormX, 1150, "OI", TabM = 3)
                if Approval > 1 or (Approval and StormX.Forced):
                    $ StormX.change_face("sad")
                    $ StormX.change_stat("love", 70, -5, 1)
                    $ StormX.change_stat("love", 200, -5)
                    ch_s "Fine, if it will silence you."
                    $ StormX.change_stat("obedience", 80, 4)
                    $ StormX.change_stat("inhibition", 80, 1)
                    $ StormX.change_stat("inhibition", 60, 3)
                    $ StormX.Forced = 1
                    jump Storm_SexPrep
                else:
                    $ StormX.change_stat("love", 200, -20)
                    $ StormX.recent_history.append("angry")
                    $ StormX.daily_history.append("angry")




    $ StormX.ArmPose = 1
    if "no_sex" in StormX.daily_history:
        ch_s "Do not question me again."
        $ StormX.recent_history.append("angry")
        $ StormX.daily_history.append("angry")
    elif StormX.Forced:
        $ StormX.change_face("angry", 1)
        ch_s "Do not overestimate your power here."
        $ StormX.change_stat("lust", 200, 5)
        if StormX.love > 300:
            $ StormX.change_stat("love", 70, -2)
        $ StormX.change_stat("obedience", 50, -2)
        $ StormX.recent_history.append("angry")
        $ StormX.daily_history.append("angry")
    elif Taboo:
        $ StormX.change_face("angry", 1)
        $ StormX.recent_history.append("no_taboo")
        $ StormX.daily_history.append("no_taboo")
        ch_s "How could you imagine that this would be an appropriate location?"
        $ StormX.change_stat("lust", 200, 5)
        $ StormX.change_stat("obedience", 50, -3)
    elif StormX.action_counter["sex"]:
        $ StormX.change_face("sad")
        ch_s "I am certain you can take care of that yourself."
    else:
        $ StormX.change_face("normal", 1)
        ch_s "I must refuse."
    $ StormX.recent_history.append("no_sex")
    $ StormX.daily_history.append("no_sex")
    $ approval_bonus = 0
    return

label Storm_SexPrep:
    call Seen_First_Peen (StormX, Partner, React=action_context)
    call Storm_Sex_Launch ("hotdog")

    if action_context == StormX:

        $ action_context = 0
        if StormX.PantsNum() == 5:
            "[StormX.name] pushes you back and climbs on top of you, sliding her skirt up as she does so."
            $ StormX.Upskirt = 1
        elif StormX.PantsNum() >= 6:
            "[StormX.name] pushes you down and climbs on top of you, sliding her [StormX.legs] down as she does so."
            $ StormX.Upskirt = 1
        else:
            "[StormX.name] pushes you back and climbs on top of you."
        $ StormX.SeenPanties = 1
        "She slides the tip along her pussy and seems to want you to insert it."
        menu:
            "What do you do?"
            "Go with it.":
                $ StormX.change_stat("inhibition", 80, 3)
                $ StormX.change_stat("inhibition", 50, 2)
                "[StormX.name] slides it in."
            "Praise her.":
                $ StormX.change_face("sexy", 1)
                $ StormX.change_stat("inhibition", 80, 3)
                ch_p "Oh yeah, [StormX.petname], let's do this."
                $ StormX.nameCheck()
                "[StormX.name] slides it in."
                $ StormX.change_stat("love", 85, 1)
                $ StormX.change_stat("obedience", 90, 1)
                $ StormX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ StormX.change_face("surprised")
                $ StormX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [StormX.petname]."
                $ StormX.nameCheck()
                "[StormX.name] pulls back."
                $ StormX.change_stat("obedience", 90, 1)
                $ StormX.change_stat("obedience", 50, 1)
                $ StormX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ StormX.AddWord(1,"refused","refused")
                return
        $ StormX.underwearDown = 1
        call Storm_First_Bottomless (1)

    elif action_context != "auto":
        call AutoStrip (StormX)

        if Taboo:
            "[StormX.name] glances around to see if anyone notices what she's doing."
            if "cockout" in Player.recent_history:
                "Then she pushes you back and slowly presses against your rigid member."
            else:
                "Then she pulls down your pants and climbs on top of you."
                "She slowly presses against your rigid member."
            $ StormX.inhibition += int(Taboo/10)
            $ StormX.lust += int(Taboo/5)
        else:
            if "cockout" in Player.recent_history:
                "[StormX.name] pushes you back and slowly presses against your rigid member."
            else:
                "[StormX.name] pulls down your pants and climbs on top of you."
                "She slowly presses against your rigid member."
        "She leans back a bit and your cock slides in."
    else:

        if (StormX.PantsNum() > 6 and not StormX.Upskirt) and (StormX.underwear and not StormX.underwearDown):
            "You quickly pull down her pants and her [StormX.underwear] and press against her slit."
        elif (StormX.underwear and not StormX.underwearDown):
            "You quickly pull down her [StormX.underwear] and press against her slit."
        $ StormX.Upskirt = 1
        $ StormX.underwearDown = 1
        $ StormX.SeenPanties = 1
        call Storm_First_Bottomless (1)

    if Player.focus >= 50:
        ch_s "I must say [StormX.player_petname], you certainly do seem to be. . . excited."
    if not StormX.action_counter["sex"]:
        if StormX.Forced:
            $ StormX.change_stat("love", 90, -150)
            $ StormX.change_stat("obedience", 70, 60)
            $ StormX.change_stat("inhibition", 80, 50)
        else:
            $ StormX.change_stat("love", 90, 30)
            $ StormX.change_stat("obedience", 70, 30)
            $ StormX.change_stat("inhibition", 80, 60)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    $ Player.Cock = "in"
    $ primary_action = "sex"
    $ action_speed = 1
    if Taboo:
        $ StormX.DrainWord("no_taboo")
    $ StormX.DrainWord("no_sex")
    $ StormX.recent_history.append("sex")
    $ StormX.daily_history.append("sex")

label Storm_Sex_Cycle:
    while Round >=0:
        call shift_focus (StormX)
        call Storm_Sex_Launch ("sex")
        $ action_speed = 2 if action_speed >= 4 else action_speed
        $ StormX.lust_face()
        $ Player.Cock = "in"
        $ primary_action = "sex"
        $ StormX.Upskirt = 1
        $ StormX.underwearDown = 1

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

                    call Slap_Ass (StormX)
                    $ counter += 1
                    $ Round -= 1
                    jump Storm_Sex_Cycle

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
                            if StormX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ StormX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (StormX, "tired")
                        "Shift primary action":

                            if StormX.remaining_actions and multi_action:
                                menu:
                                    "How about anal?":
                                        $ action_context = "shift"
                                        call Storm_SexAfter
                                        call Storm_Sex_A
                                    "Just stick it in her ass [[without asking].":
                                        $ action_context = "auto"
                                        call Storm_SexAfter
                                        call Storm_Sex_A
                                    "Pull back to hotdog her.":
                                        $ action_context = "pullback"
                                        call Storm_SexAfter
                                        call Storm_Sex_H
                                    "Never Mind":
                                        jump Storm_Sex_Cycle
                            else:
                                call Sex_Basic_Dialog (StormX, "tired")
                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Asks [StormX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (StormX)
                                "Asks [StormX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (StormX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (StormX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Storm_Sex_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Storm_Sex_Cycle
                                "Never mind":
                                    jump Storm_Sex_Cycle
                        "Just take a look at her.":
                            $ Player.Cock = 0
                            $ action_speed = 0

                        "Show her feet" if not ShowFeet and (StormX.pose == "doggy" or StormX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (StormX.pose == "doggy" or StormX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [StormX.name]":

                            call Girl_Undress (StormX)
                        "Clean up [StormX.name] (locked)" if not StormX.Spunk:
                            pass
                        "Clean up [StormX.name]" if StormX.Spunk:
                            call Girl_Cleanup (StormX, "ask")
                        "Never mind":
                            jump Storm_Sex_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Storm_Sex_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Storm_SexAfter
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Storm_Sex_Reset
                    $ Line = 0
                    jump Storm_SexAfter


        call shift_focus (StormX)
        call Sex_Dialog (StormX, Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or StormX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (StormX)
                if "angry" in StormX.recent_history:
                    call Storm_Sex_Reset
                    return
                $ StormX.change_stat("lust", 200, 5)
                if 100 > StormX.lust >= 70 and StormX.session_orgasms < 2:
                    $ StormX.recent_history.append("unsatisfied")
                    $ StormX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Storm_SexAfter
                $ Line = "came"

            if StormX.lust >= 100:

                call Girl_Cumming (StormX)
                if action_context == "shift" or "angry" in StormX.recent_history:
                    jump Storm_SexAfter

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "She's emptied you out, you'll need to take a break."
                    jump Storm_SexAfter
                elif "unsatisfied" in StormX.recent_history:

                    $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                    "[Line] Keep going?"
                    menu:
                        extend ""
                        "Yes, keep going for a bit." if Player.semen:
                            $ Line = "You get back into it"
                            jump Storm_Sex_Cycle
                        "No, I'm done." if Player.semen:
                            "You pull back."
                            jump Storm_SexAfter
                        "No, I'm spent." if not Player.semen:
                            "You pull back."
                            jump Storm_SexAfter
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if StormX.SEXP >= 100 or ApprovalCheck(StormX, 1200, "LO"):
            pass
        elif counter == (5 + StormX.Sex):
            $ StormX.brows = "confused"
            ch_s "Are you nearly finished?"
        elif counter == (10 + StormX.Sex):
            $ StormX.brows = "angry"
            ch_s "I am . . .becoming . . a bit. . . worn out. . . here. . ."
            menu:
                ch_s "Would you mind. . . a different. . . option?"
                "How about a BJ?" if StormX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Storm_SexAfter
                    call Storm_Blowjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    $ counter += 1
                    jump Storm_Sex_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Storm_Sex_Reset
                    $ action_context = "shift"
                    jump Storm_SexAfter
                "No, get back down there.":
                    if ApprovalCheck(StormX, 1200) or ApprovalCheck(StormX, 500, "O"):
                        $ StormX.change_stat("love", 200, -5)
                        $ StormX.change_stat("obedience", 50, 3)
                        $ StormX.change_stat("obedience", 80, 2)
                        "She grumbles but keeps moving."
                    else:
                        $ StormX.change_face("angry", 1)
                        call Storm_Sex_Reset
                        "She scowls at you and pulls out."
                        ch_s "No, I think not."
                        $ StormX.change_stat("love", 50, -3, 1)
                        $ StormX.change_stat("love", 80, -4, 1)
                        $ StormX.change_stat("obedience", 30, -1, 1)
                        $ StormX.change_stat("obedience", 50, -1, 1)
                        $ StormX.recent_history.append("angry")
                        $ StormX.daily_history.append("angry")
                        jump Storm_SexAfter


        call Escalation (StormX)

        if Round == 10:
            ch_s "You might want to consider finishing. . ."
        elif Round == 5:
            ch_s "We shall require a break soon."


    $ StormX.change_face("bemused", 0)
    $ Line = 0
    ch_s "[StormX.player_petname], that will be enough for now."

label Storm_SexAfter:
    if not action_context:
        $ Player.Sprite = 0
        $ Player.Cock = "out"
        call Storm_Sex_Reset

    $ StormX.change_face("sexy")

    $ StormX.action_counter["sex"] += 1
    $ StormX.remaining_actions -=1
    $ StormX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ StormX.addiction_rate += 1
    $ StormX.change_stat("inhibition", 30, 2)
    $ StormX.change_stat("inhibition", 70, 1)

    call Partner_Like (StormX, 3, 2)

    if "Storm Sex Addict" in Achievements:
        pass

    elif StormX.action_counter["sex"] >= 10:
        $ StormX.SEXP += 5
        $ Achievements.append("Storm Sex Addict")
        if not action_context:
            $ StormX.change_face("smile", 1)
            ch_s "We do go well together. . ."
    elif StormX.action_counter["sex"] == 1:
        $ StormX.SEXP += 20
        if not action_context:
            if StormX.love >= 500 and "unsatisfied" not in StormX.recent_history:
                ch_s "I hope that was as enjoyable for you as it was for me."
            elif StormX.obedience <= 500 and Player.focus <= 20:
                $ StormX.mouth = "sad"
                ch_s "I hope you found that satisfactory."
    elif StormX.action_counter["sex"] == 5:
        ch_s "You are quite skilled at this."
        ch_s "I am glad you \"bumped into\" me."
    elif not action_context:
        if "unsatisfied" in StormX.recent_history:
            $ StormX.change_face("angry")
            $ StormX.eyes = "side"
            ch_s "I could have used some more attention to my needs. . ."

    $ approval_bonus = 0


    call Checkout
    return






label Storm_Sex_A:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (StormX)
    if StormX.action_counter["anal"] >= 7:
        $ approval_bonus += 20
    elif StormX.action_counter["anal"] >= 3:
        $ approval_bonus += 17
    elif StormX.action_counter["anal"]:
        $ approval_bonus += 15

    if StormX.addiction >= 75 and (StormX.event_counter["creampied"] + StormX.event_counter["anal_creampied"]) >=3:
        $ approval_bonus += 25
    elif StormX.addiction >= 75:
        $ approval_bonus += 15

    if StormX.lust > 85:
        $ approval_bonus += 10
    elif StormX.lust > 75:
        $ approval_bonus += 5

    $ approval_bonus += 10

    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in StormX.Traits:
        $ approval_bonus += (5*Taboo)

    if StormX in Player.Harem or "sex friend" in StormX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in StormX.Traits:
        $ approval_bonus -= 40
    if StormX.event_counter["forced"] and not StormX.Forced:
        $ approval_bonus -= 5*StormX.event_counter["forced"]

    if Taboo and "no_taboo" in StormX.daily_history:
        $ approval_bonus -= 10
    if "no_anal" in StormX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_anal" in StormX.recent_history else 0

    $ Approval = ApprovalCheck(StormX, 1550, TabM = 5)

    if action_context == "auto":
        call Storm_Sex_Launch ("anal")
        if StormX.PantsNum() == 5:
            "You roll back, pulling [StormX.name] on top of you, sliding her skirt up as you go."
            $ StormX.Upskirt = 1
        elif StormX.PantsNum() >= 6:
            "You roll back, pulling [StormX.name] on top of you, sliding her [StormX.legs] down as you do."
            $ StormX.legs = 0
        else:
            "You roll back, pulling [StormX.name] on top of you."
        $ StormX.SeenPanties = 1
        "You press the tip of your cock against her tight rim."
        $ StormX.change_face("surprised", 1)

        if (StormX.action_counter["anal"] and Approval) or (Approval > 1):

            $ StormX.change_stat("obedience", 70, 3)
            $ StormX.change_stat("inhibition", 50, 3)
            $ StormX.change_stat("inhibition", 70, 1)
            "[StormX.name] is briefly startled, but melts into a sly smile."
            ch_s "[StormX.player_petname], I am surprised at you. . ."
            jump Storm_AnalPrep
        else:

            $ StormX.brows = "angry"
            menu:
                ch_s "Excuse me, what are you aiming at?"
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ StormX.change_face("sexy", 1)
                        $ StormX.change_stat("obedience", 70, 3)
                        $ StormX.change_stat("inhibition", 50, 3)
                        $ StormX.change_stat("inhibition", 70, 1)
                        ch_s "Oh, that is unfortunate. . ."
                        ch_s "I did not say that I was opposed. . ."
                        jump Storm_AnalPrep
                    "You pull back before you really get it in."
                    $ StormX.change_face("bemused", 1)

                    if StormX.action_counter["anal"]:
                        ch_s "I do appreciate some warning. . ."
                    else:
                        ch_s "We could work up to that, perhaps. . ."
                "Just fucking.":
                    $ StormX.change_stat("love", 80, -10, 1)
                    $ StormX.change_stat("love", 200, -8)
                    "You press into her."
                    $ StormX.change_stat("obedience", 70, 3)
                    $ StormX.change_stat("inhibition", 50, 3)
                    if not ApprovalCheck(StormX, 700, "O", TabM=1):
                        $ StormX.change_face("angry")
                        "[StormX.name] shoves you away and backhands you in the face."
                        ch_s "That is unfortunate."
                        ch_s "I am afraid that is -not- what will happen here."
                        $ StormX.change_stat("love", 50, -10, 1)
                        $ StormX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        call Storm_Sex_Reset
                        $ StormX.recent_history.append("angry")
                        $ StormX.daily_history.append("angry")
                    else:
                        $ StormX.change_face("sad")
                        "[StormX.name] doesn't seem to be into this, you're lucky she's so obedient."
                        jump Storm_AnalPrep
        return



    if not StormX.action_counter["anal"] and "no_anal" not in StormX.recent_history:

        $ StormX.change_face("surprised", 1)
        $ StormX.mouth = "kiss"
        ch_s "I am shocked! Anal?"

        if StormX.Forced:
            $ StormX.change_face("sad")
            ch_s "Oh. Of course it would be anal."

    if "anal" in StormX.recent_history:
        $ StormX.change_face("sexy", 1)
        ch_s "Of course."
        jump Storm_AnalPrep


    if not StormX.action_counter["anal"] and Approval:

        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
        elif StormX.love >= (StormX.obedience + StormX.inhibition):
            $ StormX.change_face("sexy")
            $ StormX.brows = "sad"
            $ StormX.mouth = "smile"
            ch_s "I was hoping that you would ask. . ."
        elif StormX.obedience >= StormX.inhibition:
            $ StormX.change_face("normal")
            ch_s "I expected we would get here at some point. . ."
        elif StormX.addiction >= 50:
            $ StormX.change_face("manic", 1)
            ch_s "Hmm, that would certainly be interesting. . ."
        else:
            $ StormX.change_face("sad")
            $ StormX.mouth = "smile"
            ch_s "I was getting tired of waiting. . ."

    elif Approval:

        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
            ch_s "You do not restrain yourself. . ."
        elif not Taboo and "no_taboo" in StormX.daily_history:
            ch_s "I suppose this is secluded enough. . ."
        elif "anal" in StormX.daily_history and not StormX.used_to_anal:
            pass
        elif "anal" in StormX.recent_history:
            ch_s "I am properly stretched out. . ."
            jump Storm_AnalPrep
        elif "anal" in StormX.daily_history:
            $ StormX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",                 
                    "So you would like another round?",                 
                    "I am still rather sore from earlier.", 
                    "You did not get enough earlier?",
                    "You are tiring me, " + StormX.player_petname + "."])
            ch_s "[Line]"
        else:
            $ StormX.change_face("sexy", 1)
            $ StormX.ArmPose = 2
            $ Line = renpy.random.choice(["Oooh, you wanted some of this?",                 
                    "So you would like another round?",                 
                    "I knew you would enjoy it. . .", 
                    "You want me to ride you?"])
            ch_s "[Line]"
        $ Line = 0

    if Approval >= 2:

        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("obedience", 90, 1)
            $ StormX.change_stat("inhibition", 60, 1)
            ch_s "Oh very well."
        elif "no_anal" in StormX.daily_history:
            ch_s "After some consideration. . ."
            ch_s "It might entertain me."
        else:
            $ StormX.change_face("sexy", 1)
            $ StormX.change_stat("love", 90, 1)
            $ StormX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well. . . I suppose.",                 
                    "Of course!", 
                    "We could, I suppose.",
                    "Hmm, yes. Fine.",
                    "Heh. Ok, ok."])
            ch_s "[Line]"
            $ Line = 0
        $ StormX.change_stat("obedience", 20, 1)
        $ StormX.change_stat("obedience", 60, 1)
        $ StormX.change_stat("inhibition", 70, 2)
        jump Storm_AnalPrep
    else:


        $ StormX.change_face("angry")
        if "no_anal" in StormX.recent_history:
            ch_s "I am afraid that \"no\" is my final answer, [StormX.player_petname]."
        elif Taboo and "no_taboo" in StormX.daily_history and "no_anal" in StormX.daily_history:
            ch_s "I have already informed you. . . not in such an exposed location."
        elif "no_anal" in StormX.daily_history:
            ch_s "I believe that I just told you \"no,\" [StormX.player_petname]."
        elif Taboo and "no_taboo" in StormX.daily_history:
            ch_s "I have already informed you, this is too public!"
        elif not StormX.action_counter["anal"]:
            $ StormX.change_face("bemused")
            ch_s "I do not know that you are yet prepared for that."
        else:
            $ StormX.change_face("bemused")
            ch_s "Perhaps we could work up to that."
        menu:
            extend ""
            "Sorry, never mind." if "no_anal" in StormX.daily_history:
                $ StormX.change_face("bemused")
                ch_s "I cannot blame you for your. . . desires."
                return
            "Maybe later?" if "no_anal" not in StormX.daily_history:
                $ StormX.change_face("sexy")
                ch_s "I imagine at some point we shall. . ."
                ch_s ". . . frequently."
                $ StormX.change_stat("love", 80, 2)
                $ StormX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ StormX.recent_history.append("no_taboo")
                    $ StormX.daily_history.append("no_taboo")
                $ StormX.recent_history.append("no_anal")
                $ StormX.daily_history.append("no_anal")
                return
            "I bet it would feel really good. . .":
                if Approval:
                    $ StormX.change_face("sexy")
                    $ StormX.change_stat("obedience", 90, 2)
                    $ StormX.change_stat("obedience", 50, 2)
                    $ StormX.change_stat("inhibition", 70, 3)
                    $ StormX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["I cannot exactly argue with that. . .",     
                                "I suppose. . .", 
                                "You do raise a good point. . ."])
                    ch_s "[Line]"
                    $ Line = 0
                    jump Storm_AnalPrep
                else:
                    pass
            "Just deal with it.":

                $ Approval = ApprovalCheck(StormX, 1250, "OI", TabM = 3)
                if Approval > 1 or (Approval and StormX.Forced):
                    $ StormX.change_face("sad")
                    $ StormX.change_stat("love", 70, -5, 1)
                    $ StormX.change_stat("love", 200, -5)
                    ch_s "Oh, very well, if you must."
                    $ StormX.change_stat("obedience", 80, 4)
                    $ StormX.change_stat("inhibition", 80, 1)
                    $ StormX.change_stat("inhibition", 60, 3)
                    $ StormX.Forced = 1
                    jump Storm_AnalPrep
                else:
                    $ StormX.change_stat("love", 200, -20)
                    $ StormX.recent_history.append("angry")
                    $ StormX.daily_history.append("angry")


    $ StormX.ArmPose = 1
    if "no_anal" in StormX.daily_history:
        ch_s "Do not question me again."
        $ StormX.recent_history.append("angry")
        $ StormX.daily_history.append("angry")
    elif StormX.Forced:
        $ StormX.change_face("angry", 1)
        ch_s "You certainly are not wasting your shot."
        $ StormX.change_stat("lust", 200, 5)
        if StormX.love > 300:
            $ StormX.change_stat("love", 70, -2)
        $ StormX.change_stat("obedience", 50, -2)
        $ StormX.recent_history.append("angry")
        $ StormX.daily_history.append("angry")
    elif Taboo:

        $ StormX.change_face("angry", 1)
        $ StormX.recent_history.append("no_taboo")
        $ StormX.daily_history.append("no_taboo")
        ch_s "How could you imagine that this would be an appropriate location?"
        $ StormX.change_stat("lust", 200, 5)
        $ StormX.change_stat("obedience", 50, -3)
    elif "anal" in StormX.daily_history:
        $ StormX.change_face("bemused")
        ch_s "Do not wear me out here."
    elif StormX.action_counter["anal"]:
        $ StormX.change_face("sad")
        ch_s "You shall have to display your worth to me again."
    else:
        $ StormX.change_face("normal", 1)
        ch_s "I do not think you have earned that yet."
    $ StormX.recent_history.append("no_anal")
    $ StormX.daily_history.append("no_anal")
    $ approval_bonus = 0
    return

label Storm_AnalPrep:
    call Seen_First_Peen (StormX, Partner, React=action_context)
    call Storm_Sex_Launch ("hotdog")
    if action_context == StormX:

        $ action_context = 0
        if StormX.PantsNum() == 5:
            "[StormX.name] pushes you back and climbs on top of you, sliding her skirt up as she does so."
            $ StormX.Upskirt = 1
        elif StormX.PantsNum() >= 6:
            "[StormX.name] pushes you down and climbs on top of you, sliding her [StormX.legs] down as she does so."
            $ StormX.Upskirt = 1
        else:
            "[StormX.name] pushes you back and climbs on top of you."
        $ StormX.SeenPanties = 1
        "She slides the tip against her ass and seems to want you to insert it."
        menu:
            "What do you do?"
            "Go with it.":
                $ StormX.change_stat("inhibition", 80, 3)
                $ StormX.change_stat("inhibition", 50, 2)
                "[StormX.name] slides it in."
            "Praise her.":
                $ StormX.change_face("sexy", 1)
                $ StormX.change_stat("inhibition", 80, 3)
                ch_p "Oh yeah, [StormX.petname], let's do this."
                $ StormX.nameCheck()
                "[StormX.name] slides it in."
                $ StormX.change_stat("love", 85, 1)
                $ StormX.change_stat("obedience", 90, 1)
                $ StormX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ StormX.change_face("surprised")
                $ StormX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [StormX.petname]."
                $ StormX.nameCheck()
                "[StormX.name] pulls back."
                $ StormX.change_stat("obedience", 90, 1)
                $ StormX.change_stat("obedience", 50, 1)
                $ StormX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ StormX.AddWord(1,"refused","refused")
                return
        $ StormX.underwearDown = 1
        call Storm_First_Bottomless (1)
    elif action_context != "auto":
        call AutoStrip (StormX)
        if Taboo:
            "[StormX.name] glances around to see if anyone notices what she's doing."
            if "cockout" in Player.recent_history:
                "Then she pushes you back and slowly presses against your rigid member."
            else:
                "Then she pulls down your pants and climbs on top of you."
                "She slowly presses against your rigid member."
            $ StormX.inhibition += int(Taboo/10)
            $ StormX.lust += int(Taboo/5)
        else:
            if "cockout" in Player.recent_history:
                "[StormX.name] pushes you back and slowly presses against your rigid member."
            else:
                "[StormX.name] pulls down your pants and climbs on top of you."
                "She slowly presses against your rigid member."
        "She leans back a bit and your cock pops in."
    else:
        if (StormX.PantsNum() > 6 and not StormX.Upskirt) and (StormX.underwear and not StormX.underwearDown):
            "You quickly pull down her pants and her [StormX.underwear] and press against her back door."
        elif (StormX.underwear and not StormX.underwearDown):
            "You quickly pull down her [StormX.underwear] and press against her back door."
        $ StormX.Upskirt = 1
        $ StormX.underwearDown = 1
        $ StormX.SeenPanties = 1
        call Storm_First_Bottomless (1)

    if not StormX.action_counter["anal"]:
        if StormX.Forced:
            $ StormX.change_stat("love", 90, -150)
            $ StormX.change_stat("obedience", 70, 70)
            $ StormX.change_stat("inhibition", 80, 40)
        else:
            $ StormX.change_stat("love", 90, 10)
            $ StormX.change_stat("obedience", 70, 30)
            $ StormX.change_stat("inhibition", 80, 70)
    elif not StormX.used_to_anal:
        if StormX.Forced:
            $ StormX.change_stat("love", 90, -20)
            $ StormX.change_stat("obedience", 70, 10)
            $ StormX.change_stat("inhibition", 80, 5)
        else:
            $ StormX.change_stat("obedience", 70, 7)
            $ StormX.change_stat("inhibition", 80, 5)
    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    $ Player.Cock = "anal"
    $ primary_action = "anal"
    $ action_speed = 1
    if Taboo:
        $ StormX.DrainWord("no_taboo")
    $ StormX.DrainWord("no_anal")
    $ StormX.recent_history.append("anal")
    $ StormX.daily_history.append("anal")

label Storm_Anal_Cycle:
    while Round >=0:
        call shift_focus (StormX)
        call Storm_Sex_Launch ("anal")
        $ action_speed = 2 if action_speed >= 4 else action_speed
        $ StormX.lust_face()
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

                    call Slap_Ass (StormX)
                    $ counter += 1
                    $ Round -= 1
                    jump Storm_Anal_Cycle

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
                            if StormX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ StormX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (StormX, "tired")
                        "Shift primary action":

                            if StormX.remaining_actions and multi_action:
                                menu:
                                    "How about sex?":
                                        $ action_context = "shift"
                                        call Storm_AnalAfter
                                        call Storm_Sex_P
                                    "Just stick it in her pussy [[without asking].":
                                        $ action_context = "auto"
                                        call Storm_AnalAfter
                                        call Storm_Sex_P
                                    "Pull back to hotdog her.":
                                        $ action_context = "pullback"
                                        call Storm_AnalAfter
                                        call Storm_Sex_H
                                    "Never Mind":
                                        jump Storm_Anal_Cycle
                            else:
                                call Sex_Basic_Dialog (StormX, "tired")
                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Asks [StormX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (StormX)
                                "Asks [StormX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (StormX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (StormX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Storm_Anal_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Storm_Anal_Cycle
                                "Never mind":
                                    jump Storm_Anal_Cycle
                        "Just take a look at her.":
                            $ Player.Cock = 0
                            $ action_speed = 0

                        "Show her feet" if not ShowFeet and (StormX.pose == "doggy" or StormX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (StormX.pose == "doggy" or StormX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [StormX.name]":

                            call Girl_Undress (StormX)
                        "Clean up [StormX.name] (locked)" if not StormX.Spunk:
                            pass
                        "Clean up [StormX.name]" if StormX.Spunk:
                            call Girl_Cleanup (StormX, "ask")
                        "Never mind":
                            jump Storm_Anal_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Storm_Sex_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Storm_AnalAfter
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Storm_Sex_Reset
                    $ Line = 0
                    jump Storm_AnalAfter


        call shift_focus (StormX)
        call Sex_Dialog (StormX, Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or StormX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (StormX)
                if "angry" in StormX.recent_history:
                    call Storm_Sex_Reset
                    return
                $ StormX.change_stat("lust", 200, 5)
                if 100 > StormX.lust >= 70 and StormX.session_orgasms < 2:
                    $ StormX.recent_history.append("unsatisfied")
                    $ StormX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Storm_AnalAfter
                $ Line = "came"

            if StormX.lust >= 100:

                call Girl_Cumming (StormX)
                if action_context == "shift" or "angry" in StormX.recent_history:
                    jump Storm_AnalAfter

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "She's emptied you out, you'll need to take a break."
                    jump Storm_AnalAfter
                elif "unsatisfied" in StormX.recent_history:

                    $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                    "[Line] Keep going?"
                    menu:
                        extend ""
                        "Yes, keep going for a bit." if Player.semen:
                            $ Line = "You get back into it"
                            jump Storm_Anal_Cycle
                        "No, I'm done." if Player.semen:
                            "You pull back."
                            jump Storm_AnalAfter
                        "No, I'm spent." if not Player.semen:
                            "You pull back."
                            jump Storm_AnalAfter
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if StormX.SEXP >= 100 or ApprovalCheck(StormX, 1200, "LO"):
            pass
        elif counter == (5 + StormX.action_counter["anal"]):
            $ StormX.brows = "confused"
            ch_s "So are you nearly finished?"
        elif counter == (10 + StormX.action_counter["anal"]):
            $ StormX.brows = "angry"
            ch_s "This is . . .becoming . . rather. . . uncomfortable. . ."
            menu:
                ch_s "Could we. . . do something. . . else?"
                "How about a BJ?" if StormX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Storm_AnalAfter
                    call Storm_Blowjob
                "How about a Handy?" if StormX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Storm_AnalAfter
                    call Storm_Handjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    $ counter += 1
                    jump Storm_Anal_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Storm_Sex_Reset
                    $ action_context = "shift"
                    jump Storm_AnalAfter
                "No, get back down there.":
                    if ApprovalCheck(StormX, 1200) or ApprovalCheck(StormX, 500, "O"):
                        $ StormX.change_stat("love", 200, -5)
                        $ StormX.change_stat("obedience", 50, 3)
                        $ StormX.change_stat("obedience", 80, 2)
                        "She grumbles but keeps moving."
                    else:
                        $ StormX.change_face("angry", 1)
                        call Storm_Sex_Reset
                        "She scowls at you and pulls out."
                        ch_s "No, I think not."
                        $ StormX.change_stat("love", 50, -3, 1)
                        $ StormX.change_stat("love", 80, -4, 1)
                        $ StormX.change_stat("obedience", 30, -1, 1)
                        $ StormX.change_stat("obedience", 50, -1, 1)
                        $ StormX.recent_history.append("angry")
                        $ StormX.daily_history.append("angry")
                        jump Storm_AnalAfter


        if Round == 10:
            ch_s "You might want to consider finishing. . ."
        elif Round == 5:
            ch_s "We shall require a break soon."


    $ StormX.change_face("bemused", 0)
    $ Line = 0
    ch_s "[StormX.player_petname], that will be enough for now."

label Storm_AnalAfter:
    if not action_context:
        $ Player.Sprite = 0
        $ Player.Cock = "out"
        call Storm_Sex_Reset

    $ StormX.change_face("sexy")

    $ StormX.action_counter["anal"] += 1
    $ StormX.remaining_actions -=1
    $ StormX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ StormX.addiction_rate += 1
    $ StormX.change_stat("inhibition", 30, 3)
    $ StormX.change_stat("inhibition", 70, 1)

    if Partner == "Kitty":
        call Partner_Like (StormX, 4, 2)
    else:
        call Partner_Like (StormX, 3, 2)

    if "Storm Anal Addict" in Achievements:
        pass

    elif StormX.action_counter["anal"] >= 10:
        $ StormX.SEXP += 7
        $ Achievements.append("Storm Anal Addict")
        if not action_context:
            $ StormX.change_face("bemused", 1)
            ch_s "I have certainly come to enjoy this."
    elif StormX.action_counter["anal"] == 1:
        $ StormX.SEXP += 25
        if not action_context:
            if StormX.love >= 500 and "unsatisfied" not in StormX.recent_history:
                pass
            elif StormX.obedience <= 500 and Player.focus <= 20:
                $ StormX.mouth = "sad"
                ch_s "Well. . ."
            ch_s "That was quite an experience. . ."
    elif StormX.action_counter["anal"] == 5:
        ch_s "You do certainly make the experience enjoyable."
    elif not action_context:
        if "unsatisfied" in StormX.recent_history:
            $ StormX.change_face("angry")
            $ StormX.eyes = "side"
            ch_s "I am afraid that you got more out of that than I. . ."

    $ approval_bonus = 0


    call Checkout
    return








label Storm_Sex_H:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (StormX)
    if StormX.action_counter["hotdog"] >= 3:
        $ approval_bonus += 10
    elif StormX.action_counter["hotdog"]:
        $ approval_bonus += 5

    if StormX.lust > 85:
        $ approval_bonus += 10
    elif StormX.lust > 75:
        $ approval_bonus += 5
    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in StormX.Traits:
        $ approval_bonus += (3*Taboo)
    if StormX in Player.Harem or "sex friend" in StormX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in StormX.Traits:
        $ approval_bonus -= 40
    if StormX.event_counter["forced"] and not StormX.Forced:
        $ approval_bonus -= 5*StormX.event_counter["forced"]

    if Taboo and "no_taboo" in StormX.daily_history:
        $ approval_bonus -= 10

    if "no_hotdog" in StormX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_hotdog" in StormX.recent_history else 0

    $ Approval = ApprovalCheck(StormX, 1000, TabM = 3)

    if action_context == "auto":
        call Storm_Sex_Launch ("hotdog")
        "You roll back, pulling [StormX.name] on top of you, and press your cock against her."
        $ StormX.change_face("surprised", 1)

        if (StormX.action_counter["hotdog"] and Approval) or (Approval > 1):
            "[StormX.name] is briefly startled, but melts into a sly smile."
            $ StormX.change_face("sly")
            $ StormX.change_stat("obedience", 70, 3)
            $ StormX.change_stat("inhibition", 50, 3)
            $ StormX.change_stat("inhibition", 70, 1)
            ch_s "Now what shall we do with that . ."
            jump Storm_HotdogPrep
        else:
            $ StormX.brows = "angry"
            menu:
                ch_s "You are rather close, [StormX.player_petname]. . ."
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ StormX.change_face("sexy", 1)
                        $ StormX.change_stat("obedience", 70, 3)
                        $ StormX.change_stat("inhibition", 50, 3)
                        $ StormX.change_stat("inhibition", 70, 1)
                        ch_s "Or perhaps not. . ."
                        jump Storm_HotdogPrep
                    "You pull back from her."
                    $ StormX.change_face("bemused", 1)
                    ch_s "You might find better results if you asked first?"
                "You'll see.":
                    $ StormX.change_stat("love", 80, -10, 1)
                    $ StormX.change_stat("love", 200, -8)
                    "You grind against her crotch."
                    $ StormX.change_stat("obedience", 70, 3)
                    $ StormX.change_stat("inhibition", 50, 3)
                    if not ApprovalCheck(StormX, 500, "O", TabM=1):
                        $ StormX.change_face("angry")
                        "[StormX.name] shoves you away."
                        ch_s "Do not go beyond yourself, [StormX.player_petname]."
                        $ StormX.change_stat("love", 50, -10, 1)
                        $ StormX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        call Storm_Sex_Reset
                        $ StormX.recent_history.append("angry")
                        $ StormX.daily_history.append("angry")
                    else:
                        $ StormX.change_face("sad")
                        "[StormX.name] doesn't seem to be into this, but she knows her place."
                        jump Storm_HotdogPrep
        return



    if not StormX.action_counter["hotdog"] and "no_hotdog" not in StormX.recent_history:

        $ StormX.change_face("surprised", 1)
        $ StormX.mouth = "kiss"
        ch_s "You would just like to press against each other like this?"

        if StormX.Forced:
            $ StormX.change_face("sad")
            ch_s ". . . and no more than that?"


    if not StormX.action_counter["hotdog"] and Approval:

        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
        elif StormX.love >= (StormX.obedience + StormX.inhibition):
            $ StormX.change_face("sexy")
            $ StormX.brows = "sad"
            $ StormX.mouth = "smile"
            ch_s "I would not wish to leave you. . . un-tended. . ."
        elif StormX.obedience >= StormX.inhibition:
            $ StormX.change_face("normal")
            ch_s "If that is what works for you. . ."
        elif StormX.addiction >= 50:
            $ StormX.change_face("manic", 1)
            ch_s "Hrmm. . ."
        else:
            $ StormX.change_face("sad")
            $ StormX.mouth = "smile"
            ch_s "Well if that is what satisfies you. . ."

    elif Approval:

        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("love", 70, -3, 1)
            $ StormX.change_stat("love", 20, -2, 1)
            ch_s "Perhaps that is going a bit too far. . ."
        elif not Taboo and "no_taboo" in StormX.daily_history:
            ch_s "I suppose that this is a better location . ."
        elif "hotdog" in StormX.recent_history:
            $ StormX.change_face("sexy", 1)
            ch_s "Again? Oh, very well."
            jump Storm_HotdogPrep
        elif "hotdog" in StormX.daily_history:
            $ StormX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",                 
                    "So you would like another round?",                 
                    "You really are into this. . .", 
                    "Are you sure that is all you would want?"])
            ch_s "[Line]"
        else:
            $ StormX.change_face("sexy", 1)
            $ StormX.ArmPose = 2
            $ Line = renpy.random.choice(["Oooh, you want some of this?",                 
                    "So you would like another round?",                       
                    "You really are into this. . .", 
                    "You want another rub?"])
            ch_s "[Line]"
        $ Line = 0

    if Approval >= 2:

        if StormX.Forced:
            $ StormX.change_face("sad")
            $ StormX.change_stat("obedience", 80, 1)
            $ StormX.change_stat("inhibition", 60, 1)
            ch_s "Fine then."
        elif "no_hotdog" in StormX.daily_history:
            ch_s "It was rather entertaining. . ."
        else:
            $ StormX.change_face("sexy", 1)
            $ StormX.change_stat("love", 80, 1)
            $ StormX.change_stat("inhibition", 50, 2)
            $ Line = renpy.random.choice(["ery well then, let me give it a rub.",                 
                    "Very well.",                 
                    "Of course!", 
                    "I suppose that we could do that.",
                    "Allow me. . .",
                    "Heh, ok, ok."])
            ch_s "[Line]"
            $ Line = 0
        $ StormX.change_stat("obedience", 60, 1)
        $ StormX.change_stat("inhibition", 70, 2)
        jump Storm_HotdogPrep
    else:


        $ StormX.change_face("angry")
        if "no_hotdog" in StormX.recent_history:
            ch_s "I am afraid that \"no\" is my final answer, [StormX.player_petname]."
        elif Taboo and "no_taboo" in StormX.daily_history and "no_hotdog" in StormX.daily_history:
            ch_s "I just informed you. . .not in such an exposed location."
        elif "no_hotdog" in StormX.daily_history:
            ch_s "I believe that I just told you \"no,\" [StormX.player_petname]."
        elif Taboo and "no_taboo" in StormX.daily_history:
            ch_s "I already informed you. . .not in such an exposed location."
        elif not StormX.action_counter["hotdog"]:
            $ StormX.change_face("bemused")
            ch_s "Hmm, that could be entertaining, [StormX.player_petname]. . ."
        else:
            $ StormX.change_face("bemused")
            ch_s "I do not believe that would be appropriate. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_hotdog" in StormX.daily_history:
                $ StormX.change_face("bemused")
                ch_s "There is no harm in asking."
                return
            "Maybe later?" if "no_hotdog" not in StormX.daily_history:
                $ StormX.change_face("sexy")
                ch_s "I expect it will happen at some point, [StormX.player_petname]."
                $ StormX.change_stat("love", 80, 1)
                $ StormX.change_stat("inhibition", 50, 1)
                if Taboo:
                    $ StormX.recent_history.append("no_taboo")
                    $ StormX.daily_history.append("no_taboo")
                $ StormX.recent_history.append("no_hotdog")
                $ StormX.daily_history.append("no_hotdog")
                return
            "You might like it. . .":
                if Approval:
                    $ StormX.change_face("sexy")
                    $ StormX.change_stat("obedience", 60, 2)
                    $ StormX.change_stat("inhibition", 50, 2)
                    $ Line = renpy.random.choice(["I cannot exactly argue with that. . .",     
                                "I suppose so. . .", 
                                "You do raise a good point. . ."])
                    ch_s "[Line]"
                    $ Line = 0
                    jump Storm_HotdogPrep
                else:
                    pass
            "Just deal with it.":

                $ Approval = ApprovalCheck(StormX, 350, "OI", TabM = 3)
                if Approval > 1 or (Approval and StormX.Forced):
                    $ StormX.change_face("sad")
                    $ StormX.change_stat("love", 70, -2, 1)
                    $ StormX.change_stat("love", 200, -2)
                    ch_s "Alright, fine then. Lie back."
                    $ StormX.change_stat("obedience", 80, 4)
                    $ StormX.change_stat("inhibition", 60, 2)
                    $ StormX.Forced = 1
                    jump Storm_HotdogPrep
                else:
                    $ StormX.change_stat("love", 200, -10)
                    $ StormX.recent_history.append("angry")
                    $ StormX.daily_history.append("angry")


    $ StormX.ArmPose = 1

    if "no_hotdog" in StormX.daily_history:
        ch_s "I believe I have made myself clear."
        $ StormX.recent_history.append("angry")
        $ StormX.daily_history.append("angry")
    if StormX.Forced:
        $ StormX.change_face("angry", 1)
        ch_s "I just do not understand the benefit."
        $ StormX.change_stat("lust", 200, 5)
        if StormX.love > 300:
            $ StormX.change_stat("love", 70, -1)
        $ StormX.change_stat("obedience", 50, -1)
        $ StormX.recent_history.append("angry")
        $ StormX.daily_history.append("angry")
    elif Taboo:
        $ StormX.change_face("angry", 1)
        $ StormX.recent_history.append("no_taboo")
        $ StormX.daily_history.append("no_taboo")
        ch_s "This area is a bit too exposed for that sort of thing. . ."
        $ StormX.change_stat("lust", 200, 5)
        $ StormX.change_stat("obedience", 50, -3)
    elif StormX.action_counter["hotdog"]:
        $ StormX.change_face("sad")
        ch_s "Not under the circumstances."
    else:
        $ StormX.change_face("normal", 1)
        ch_s "Thank you, but no."
    $ StormX.recent_history.append("no_hotdog")
    $ StormX.daily_history.append("no_hotdog")
    $ approval_bonus = 0
    return

label Storm_HotdogPrep:
    call Seen_First_Peen (StormX, Partner, React=action_context)
    call Storm_Sex_Launch ("hotdog")


    if action_context == StormX:

        $ action_context = 0
        "[StormX.name] pushes you back and climbs on top of you, sliding back and forth along your shaft."
        menu:
            "What do you do?"
            "Go with it.":
                $ StormX.change_stat("inhibition", 80, 3)
                $ StormX.change_stat("inhibition", 50, 2)
                "[StormX.name] starts to grind against you."
            "Praise her.":
                $ StormX.change_face("sexy", 1)
                $ StormX.change_stat("inhibition", 80, 3)
                ch_p "Oh yeah, [StormX.petname], let's do this."
                $ StormX.nameCheck()
                "[StormX.name] starts to grind against you."
                $ StormX.change_stat("love", 85, 1)
                $ StormX.change_stat("obedience", 90, 1)
                $ StormX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ StormX.change_face("surprised")
                $ StormX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [StormX.petname]."
                $ StormX.nameCheck()
                "[StormX.name] pulls back."
                $ StormX.change_stat("obedience", 90, 1)
                $ StormX.change_stat("obedience", 50, 1)
                $ StormX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ StormX.AddWord(1,"refused","refused")
                return

    elif action_context != "auto":


        if Taboo:
            "[StormX.name] glances around to see if anyone notices what she's doing."
            if "cockout" in Player.recent_history:
                "Then she pushes you back and slowly presses against your rigid member."
            else:
                "Then she pulls down your pants and climbs on top of you."
                "She slowly presses against your rigid member."
            $ StormX.inhibition += int(Taboo/10)
            $ StormX.lust += int(Taboo/5)
        else:
            if "cockout" in Player.recent_history:
                "[StormX.name] pushes you back and slowly presses against your rigid member."
            else:
                "[StormX.name] pulls down your pants and climbs on top of you."
                "She slowly presses against your rigid member."
    else:

        "You roll back, pulling her on top of you and your rigid member."

    if not StormX.action_counter["hotdog"]:
        if StormX.Forced:
            $ StormX.change_stat("love", 90, -5)
            $ StormX.change_stat("obedience", 70, 20)
            $ StormX.change_stat("inhibition", 80, 10)
        else:
            $ StormX.change_stat("love", 90, 20)
            $ StormX.change_stat("obedience", 70, 20)
            $ StormX.change_stat("inhibition", 80, 20)


    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    $ primary_action = "hotdog"
    $ action_speed = 1
    if Taboo:
        $ StormX.DrainWord("no_taboo")
    $ StormX.DrainWord("no_hotdog")
    $ StormX.recent_history.append("hotdog")
    $ StormX.daily_history.append("hotdog")

label Storm_Hotdog_Cycle:
    while Round >=0:
        call shift_focus (StormX)
        call Storm_Sex_Launch ("hotdog")
        $ action_speed = 2 if action_speed >= 4 else action_speed
        $ StormX.lust_face()
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

                    call Slap_Ass (StormX)
                    $ counter += 1
                    $ Round -= 1
                    jump Storm_Hotdog_Cycle

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
                            if StormX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ StormX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (StormX, "tired")
                        "Shift primary action":

                            if StormX.remaining_actions and multi_action:
                                menu:
                                    "How about sex?":
                                        $ action_context = "shift"
                                        call Storm_HotdogAfter
                                        call Storm_Sex_P
                                    "Just stick it in her pussy [[without asking].":
                                        $ action_context = "auto"
                                        call Storm_HotdogAfter
                                        call Storm_Sex_P
                                    "How about anal?":
                                        $ action_context = "shift"
                                        call Storm_HotdogAfter
                                        call Storm_Sex_A
                                    "Just stick it in her ass [[without asking].":
                                        $ action_context = "auto"
                                        call Storm_HotdogAfter
                                        call Storm_Sex_A
                                    "Never Mind":
                                        jump Storm_Hotdog_Cycle
                            else:
                                call Sex_Basic_Dialog (StormX, "tired")
                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Asks [StormX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change (StormX)
                                "Asks [StormX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (StormX)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_primary_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_primary_action:
                                    $ position_timer = 0
                                "Swap to [Partner.name]":

                                    call primary_action_Swap (StormX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Storm_Hotdog_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Storm_Hotdog_Cycle
                                "Never mind":
                                    jump Storm_Hotdog_Cycle
                        "Just take a look at her.":
                            $ Player.Cock = 0
                            $ action_speed = 0

                        "Show her feet" if not ShowFeet and (StormX.pose == "doggy" or StormX.pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (StormX.pose == "doggy" or StormX.pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [StormX.name]":

                            call Girl_Undress (StormX)
                        "Clean up [StormX.name] (locked)" if not StormX.Spunk:
                            pass
                        "Clean up [StormX.name]" if StormX.Spunk:
                            call Girl_Cleanup (StormX, "ask")
                        "Never mind":
                            jump Storm_Hotdog_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Storm_Sex_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Storm_HotdogAfter
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Storm_Sex_Reset
                    $ Line = 0
                    jump Storm_HotdogAfter


        call shift_focus (StormX)
        call Sex_Dialog (StormX, Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or StormX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (StormX)
                if "angry" in StormX.recent_history:
                    call Storm_Sex_Reset
                    return
                $ StormX.change_stat("lust", 200, 5)
                if 100 > StormX.lust >= 70 and StormX.session_orgasms < 2:
                    $ StormX.recent_history.append("unsatisfied")
                    $ StormX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Storm_HotdogAfter
                $ Line = "came"

            if StormX.lust >= 100:

                call Girl_Cumming (StormX)
                if action_context == "shift" or "angry" in StormX.recent_history:
                    jump Storm_HotdogAfter

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "She's emptied you out, you'll need to take a break."
                    jump Storm_HotdogAfter
                elif "unsatisfied" in StormX.recent_history:

                    $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                    "[Line] Keep going?"
                    menu:
                        extend ""
                        "Yes, keep going for a bit." if Player.semen:
                            $ Line = "You get back into it"
                            jump Storm_Hotdog_Cycle
                        "No, I'm done." if Player.semen:
                            "You pull back."
                            jump Storm_HotdogAfter
                        "No, I'm spent." if not Player.semen:
                            "You pull back."
                            jump Storm_HotdogAfter
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if StormX.SEXP >= 100 or ApprovalCheck(StormX, 1200, "LO"):
            pass
        elif counter == (5 + StormX.action_counter["hotdog"]):
            $ StormX.brows = "confused"
            ch_s "Are you nearly satisfied?"
        elif counter == (10 + StormX.action_counter["hotdog"]):
            $ StormX.brows = "angry"
            menu:
                ch_s "I am getting rather tired of this."
                "How about a BJ?" if StormX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Storm_HotdogAfter
                    call Storm_Blowjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    $ counter += 1
                    jump Storm_Hotdog_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Storm_Sex_Reset
                    $ action_context = "shift"
                    jump Storm_HotdogAfter
                "No, get back down there.":
                    if ApprovalCheck(StormX, 1200) or ApprovalCheck(StormX, 500, "O"):
                        $ StormX.change_stat("love", 200, -5)
                        $ StormX.change_stat("obedience", 50, 3)
                        $ StormX.change_stat("obedience", 80, 2)
                        "She grumbles but keeps moving."
                    else:
                        $ StormX.change_face("angry", 1)
                        call Storm_Sex_Reset
                        "She scowls at you and pulls away."
                        ch_s "No, I think not."
                        $ StormX.change_stat("love", 50, -3, 1)
                        $ StormX.change_stat("love", 80, -4, 1)
                        $ StormX.change_stat("obedience", 30, -1, 1)
                        $ StormX.change_stat("obedience", 50, -1, 1)
                        $ StormX.recent_history.append("angry")
                        $ StormX.daily_history.append("angry")
                        jump Storm_HotdogAfter


        call Escalation (StormX)

        if Round == 10:
            ch_s "You might want to consider finishing. . ."
        elif Round == 5:
            ch_s "We shall require a break soon."


    $ StormX.change_face("bemused", 0)
    $ Line = 0
    ch_s "[StormX.player_petname], that will be enough for now."

label Storm_HotdogAfter:
    if not action_context:
        $ Player.Sprite = 0
        $ Player.Cock = "out"
        call Storm_Sex_Reset

    $ StormX.change_face("sexy")

    $ StormX.action_counter["hotdog"] += 1
    $ StormX.remaining_actions -=1
    $ StormX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ StormX.addiction_rate += 1
    $ StormX.change_stat("inhibition", 30, 1)
    $ StormX.change_stat("inhibition", 70, 1)

    call Partner_Like (StormX, 2)

    if StormX.action_counter["hotdog"] == 10:
        $ StormX.SEXP += 5
    elif StormX.action_counter["hotdog"] == 1:
        $ StormX.SEXP += 10
        if not action_context:
            if StormX.love >= 500 and "unsatisfied" not in StormX.recent_history:
                ch_s "That was. . . enjoyable."
            elif StormX.obedience <= 500 and Player.focus <= 20:
                $ StormX.mouth = "sad"
                ch_s "Was that satisfactory?"
    elif not action_context:
        if "unsatisfied" in StormX.recent_history:
            $ StormX.change_face("angry")
            $ StormX.eyes = "side"
            ch_s "I am afraid that did not do much for me. . ."

    $ approval_bonus = 0


    call Checkout
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
