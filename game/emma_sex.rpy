
label Emma_SexAct(Act=0):
    if AloneCheck(EmmaX) and EmmaX.Taboo == 20:
        $ EmmaX.Taboo = 0
        $ Taboo = 0
    call shift_focus (EmmaX)
    if Taboo > 20 and "taboo" not in EmmaX.history:

        call Emma_Taboo_Talk
        if bg_current == "bg_classroom":
            ch_p "We could just lock the door, right?"
            ch_e "We certainly could. . ."
            "[EmmaX.name] walks to the door and locks it behind her."
            $ Taboo = 0
        else:
            return

    if Act == "SkipTo":
        $ renpy.pop_call()
        $ renpy.pop_call()

        call SkipTo (EmmaX)
    elif Act == "switch":
        $ renpy.pop_call()


    elif Act == "masturbate":
        call Emma_M_Prep
        if not action_context:
            return
    elif Act == "lesbian":
        call Les_Prep (EmmaX)
        if not action_context:
            return
    elif Act == "kissing":
        call KissPrep (EmmaX)
        if not action_context:
            return
    elif Act == "breasts":
        call Emma_Fondle_Breasts
        if not action_context:
            return
    elif Act == "blowjob":
        call Emma_BJ_Prep
        if not action_context:
            return
    elif Act == "handjob":
        call Emma_HJ_Prep
        if not action_context:
            return
    elif Act == "sex":
        call Emma_SexPrep
        if not action_context:
            return

label Emma_SexMenu:
    if "classcaught" not in EmmaX.history:
        ch_e "I can't imagine being a part of something so. . . tawdry."
        return
    if "three" not in EmmaX.history and not AloneCheck(EmmaX):

        call Emma_ThreeCheck
    if Taboo > 20 and "taboo" not in EmmaX.history:

        call Emma_Taboo_Talk
        if bg_current == "bg_classroom" or bg_current in PersonalRooms and AloneCheck(EmmaX):
            ch_p "We could just lock the door, right?"
            ch_e "We certainly could. . ."
            "[EmmaX.name] walks to the door and locks it behind her."
            $ Player.Traits.append("locked")
            call Taboo_Level
        else:

            return
    call shift_focus (EmmaX)
    $ primary_action = 0
    $ offhand_action = 0
    $ girl_offhand_action = 0
    $ action_context = 0
    call Emma_Hide
    $ EmmaX.ArmPose = 1
    if "detention" in EmmaX.recent_history:
        $ approval_bonus = 20 if approval_bonus <= 20 else approval_bonus
    call set_the_scene (1, 0, 0, 0, 1)

    if not Player.semen:
        "You're a little out of juice at the moment, you might want to wait a bit."
    if Player.focus >= 95:
        "You're practically buzzing, the slightest breeze could set you off."
    if not EmmaX.remaining_actions:
        "[EmmaX.name]'s looking a bit tired out, maybe let her rest a bit."

    if "caught" in EmmaX.recent_history or "angry" in EmmaX.recent_history:
        if EmmaX.location == bg_current:
            ch_e "I'd rather not deal with you at the moment."
        $ EmmaX.change_outfit()
        $ EmmaX.DrainWord("caught",1,0)
        return

    if Round < 5:
        ch_e "I think we could both do with a short break."
        return
    menu Emma_SMenu:
        ch_e "So, what was it you hoped to do?"
        "Do you want to make out?":
            if EmmaX.remaining_actions:
                call Makeout (EmmaX)
            else:
                ch_e "I'm sorry, [EmmaX.player_petname], but I need a break."
        "Could I touch you?":

            if EmmaX.remaining_actions:
                $ EmmaX.change_face("sly")
                menu:
                    ch_e "Um, what did you want to touch, [EmmaX.player_petname]?"
                    "Could I give you a massage?":
                        call Massage (EmmaX)
                    "Your breasts?":
                        call Emma_Fondle_Breasts
                    "Suck your breasts?" if EmmaX.remaining_actions and EmmaX.action_counter["suck_breasts"]:
                        call Emma_Suck_Breasts
                    "Your thighs?" if EmmaX.remaining_actions:
                        call Emma_Fondle_Thighs
                    "Your pussy?" if EmmaX.remaining_actions:
                        call Emma_Fondle_Pussy
                    "Lick your pussy?" if EmmaX.remaining_actions and EmmaX.action_counter["eat_pussy"]:
                        call Emma_Lick_Pussy
                    "Your Ass?":
                        call Emma_Fondle_Ass
                    "Never mind [[something else]":
                        jump Emma_SMenu
            else:
                ch_e "I'm sorry, [EmmaX.player_petname], but I need a break."
        "Could you take care of something for me? [[Your dick, you mean your dick]":

            if Player.semen and EmmaX.remaining_actions:
                menu:
                    ch_e "What did you want me to do?"
                    "Could you give me a handjob?":
                        call Emma_Handjob
                    "Could you give me a titjob?":
                        call Emma_Titjob
                    "Could you suck my cock?":
                        call Emma_Blowjob
                    "Could use your feet?":
                        call Emma_Footjob
                    "Never mind [[something else]":
                        jump Emma_SMenu
            elif not EmmaX.remaining_actions:
                "I'm sorry, [EmmaX.player_petname], but I need a break."
            else:
                "You really don't have it in you, maybe take a break."
        "Could you put on a show for me?":

            menu:
                ch_e "What did you want to see?"
                "Dance for me?":
                    if EmmaX.remaining_actions:
                        call Group_Strip (EmmaX)
                    else:
                        "I'm sorry, [EmmaX.player_petname], but I need a break."
                "Could you undress for me?":

                    call Girl_Undress (EmmaX)

                "You've got a little something. . . [[clean-up]" if EmmaX.Spunk:
                    ch_e "Huh?"
                    call Girl_Cleanup (EmmaX, "ask")
                "Could I watch you get yourself off? [[masturbate]":

                    if EmmaX.remaining_actions:
                        call Emma_Masturbate
                    else:
                        "I'm sorry, [EmmaX.player_petname], but I need a break."

                "Maybe make out with [RogueX.name]?" if RogueX.location == bg_current:
                    call LesScene (EmmaX)
                "Maybe make out with [KittyX.name]?" if KittyX.location == bg_current:
                    call LesScene (EmmaX)
                "Maybe make out with [LauraX.name]?" if LauraX.location == bg_current:
                    call LesScene (EmmaX)
                "Maybe make out with [JeanX.name]?" if JeanX.location == bg_current:
                    call LesScene (EmmaX)
                "Maybe make out with [StormX.name]?" if StormX.location == bg_current:
                    call LesScene (EmmaX)
                "Maybe make out with [JubesX.name]?" if JubesX.location == bg_current:
                    call LesScene (EmmaX)
                "Never mind [[something else]":

                    jump Emma_SMenu
        "Could we maybe?. . . [[fuck]":


            if EmmaX.remaining_actions:
                menu:
                    "What did you want to do?"
                    "Come over here, I've got something in mind. . .":
                        if Player.semen:
                            call Emma_Sex_H
                        else:
                            "The spirit is apparently willing, but the flesh is spongy and bruised."
                    "Fuck your pussy.":
                        if Player.semen:
                            call Emma_Sex_P
                        else:
                            "The spirit is apparently willing, but the flesh is spongy and bruised."
                    "Fuck your ass.":
                        if Player.semen:
                            call Emma_Sex_A
                        else:
                            "The spirit is apparently willing, but the flesh is spongy and bruised."
                    "How about some toys? [[Pussy]":
                        call Emma_Dildo_Pussy
                    "How about some toys? [[Anal]":
                        call Emma_Dildo_Ass
                    "Never mind [[something else]":
                        jump Emma_SMenu
            else:
                "I'm sorry, [EmmaX.player_petname], but I need a break."
        "Hey, do you want in on this? [[Threesome]":

            call Sex_Menu_Threesome (EmmaX)
            jump Emma_SMenu

        "Hey, [Partner.name]? [[Switch lead]" if Partner:
            call expression Partner.Tag + "_SexAct" pass ("switch")
            return

        "Cheat Menu" if config.developer:
            call Cheat_Menu (EmmaX)
        "Never mind. [[exit]":
            if EmmaX.lust >= 50 or EmmaX.addiction >= 50:
                $ EmmaX.change_face("sad")
                if EmmaX.remaining_actions and EmmaX.SEXP >= 15 and Round > 20:
                    if "round2" not in EmmaX.recent_history:
                        ch_e "Are you certain, [EmmaX.player_petname]? Are you perhaps forgetting something?"
                        $ EmmaX.change_stat("inhibition", 30, 2)
                        $ EmmaX.change_stat("inhibition", 50, 1)
                    elif EmmaX.addiction >= 50:
                        ch_e "I need more contact."
                    else:
                        ch_e "I'm afraid that still wasn't enough."
                    menu:
                        extend ""
                        "Yeah, I'm done for now." if Player.semen and "round2" not in EmmaX.recent_history:
                            if "unsatisfied" in EmmaX.recent_history and not EmmaX.session_orgasms:
                                $ EmmaX.change_face("angry")
                                $ EmmaX.eyes = "side"
                                $ EmmaX.change_stat("love", 70, -2)
                                $ EmmaX.change_stat("love", 90, -4)
                                $ EmmaX.change_stat("obedience", 30, 2)
                                $ EmmaX.change_stat("obedience", 70, 1)
                                ch_e "Well! This might count against you next time."
                            else:
                                $ EmmaX.change_face("bemused", 1)
                                $ EmmaX.change_stat("obedience", 50, 2)
                                ch_e "I suppose I'll have to blame myself as an educator."
                        "I gave it a shot." if "round2" in EmmaX.recent_history:
                            if "unsatisfied" in EmmaX.recent_history and not EmmaX.session_orgasms:
                                $ EmmaX.change_face("angry")
                                $ EmmaX.eyes = "side"
                                ch_e "Yes, disappointingly so. . ."
                            else:
                                $ EmmaX.change_face("bemused", 1)
                                ch_e "I suppose you did. . .shame you couldn't do better. . ."
                        "Hey, I did my part." if EmmaX.session_orgasms > 2:
                            $ EmmaX.change_face("sly", 1)
                            ch_e "Take it as a compliment that I expected more."
                        "I'm tapped out for the moment, let's try again later." if not Player.semen:
                            $ EmmaX.change_face("normal")
                            ch_e "I suppose that can't be helped. . ."
                        "Ok, we can try something else." if multi_action and "round2" not in EmmaX.recent_history:
                            $ EmmaX.change_face("smile")
                            $ EmmaX.change_stat("love", 70, 2)
                            $ EmmaX.change_stat("love", 90, 1)
                            ch_e "Excellent. . ."
                            $ EmmaX.recent_history.append("round2")
                            $ EmmaX.daily_history.append("round2")
                            jump Emma_SexMenu
                        "Again? Ok, fine." if multi_action and "round2" in EmmaX.recent_history:
                            $ EmmaX.change_face("sly")
                            ch_e "Always. . ."
                            jump Emma_SexMenu
                else:

                    $ EmmaX.change_face("bemused", 1)
                    ch_e "I suppose I'm tired as well, [EmmaX.player_petname]. We can take a breather. . ."
                    $ EmmaX.change_stat("inhibition", 30, 2)
                    $ EmmaX.change_stat("inhibition", 50, 1)
                $ EmmaX.change_face()
            else:
                ch_e "Fine."
            call Sex_Over
            return
    if EmmaX.location != bg_current:
        call set_the_scene
        call Trig_Reset
        return
    if not multi_action:
        call set_the_scene
        ch_e "That's all you get. . . for now."
        $ EmmaX.session_orgasms = 0
        call Trig_Reset
        return
    call GirlsAngry
    jump Emma_SexMenu





label Emma_Masturbate:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (EmmaX)
    if EmmaX.action_counter["masturbation"]:
        $ approval_bonus += 10
    if EmmaX.SEXP >= 50:
        $ approval_bonus += 25
    elif EmmaX.SEXP >= 30:
        $ approval_bonus += 15
    elif EmmaX.SEXP >= 15:
        $ approval_bonus += 5
    if EmmaX.lust >= 90:
        $ approval_bonus += 20
    elif EmmaX.lust >= 75:
        $ approval_bonus += 5
    if "exhibitionist" in EmmaX.Traits:
        $ approval_bonus += (3*Taboo)
    if EmmaX in Player.Harem or "sex friend" in EmmaX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in EmmaX.Traits:
        $ approval_bonus -= 40
    if EmmaX.event_counter["forced"] and not EmmaX.Forced:
        $ approval_bonus -= 5*EmmaX.event_counter["forced"]

    $ Approval = ApprovalCheck(EmmaX, 1300, TabM = 2)

    $ EmmaX.DrainWord("unseen",1,0)

    if action_context == "join":
        if Approval > 1 or (Approval and EmmaX.lust >= 50):
            $ Player.AddWord(1,"join")
            menu:
                extend ""
                "Would you like some help? I could lend some helping hands. . ." if Player.semen and EmmaX.remaining_actions:
                    $ EmmaX.change_stat("love", 90, 1)
                    $ EmmaX.change_stat("obedience", 50, 2)
                    $ EmmaX.change_face("sexy")
                    ch_e "Hm, well I do have my hands full with these. . ."
                    $ EmmaX.change_stat("obedience", 70, 2)
                    $ EmmaX.change_stat("inhibition", 70, 1)
                    $ offhand_action = "fondle_breasts"
                    $ EmmaX.action_counter["masturbation"] += 1
                    jump Emma_M_Cycle
                "Would you like some help? I could. . . up to you, I guess." if Player.semen and EmmaX.remaining_actions:
                    $ EmmaX.change_stat("love", 70, 2)
                    $ EmmaX.change_stat("love", 90, 1)
                    $ EmmaX.change_face("sexy")
                    ch_e "I suppose I could use some added attention. . ."
                    $ EmmaX.change_stat("obedience", 70, 2)
                    $ EmmaX.change_stat("inhibition", 70, 1)
                    $ D20 = renpy.random.randint(1, 20)
                    if D20 > 10:
                        $ offhand_action = "fondle_breasts"
                    else:
                        $ offhand_action = "suck_breasts"
                    $ EmmaX.action_counter["masturbation"] += 1
                    jump Emma_M_Cycle
                "Why don't we take care of each other?" if Player.semen and EmmaX.remaining_actions:
                    $ EmmaX.change_face("sexy")
                    ch_e "I suppose I could spare some attention. . ."
                    $ renpy.pop_call()
                    return
                "You look like you have things well in hand. . .":
                    if EmmaX.lust >= 50:
                        $ EmmaX.change_stat("love", 70, 2)
                        $ EmmaX.change_stat("love", 90, 1)
                        $ EmmaX.change_face("sexy")
                        ch_e "So you prefer to watch. . ."
                        $ EmmaX.change_stat("obedience", 80, 3)
                        $ EmmaX.change_stat("inhibition", 80, 5)
                        jump Emma_M_Cycle
                    elif ApprovalCheck(EmmaX, 1200):
                        $ EmmaX.change_face("sly")
                        ch_e "I did, but I wasn't intending perfomance art."
                    else:
                        $ EmmaX.change_face("angry")
                        ch_e "I did, but now the mood is ruined. . ."


        $ EmmaX.ArmPose = 1
        $ EmmaX.change_outfit()
        $ EmmaX.remaining_actions -= 1
        $ Player.change_stat("focus", 50, 30)
        call Checkout (1)
        $ Line = 0
        $ action_context = 0
        $ renpy.pop_call()
        if Approval:
            $ EmmaX.change_face("bemused", 1)
            if bg_current == "bg_emma":
                ch_e "Why are you even in my room?"
            else:
                ch_e "I wasn't expecting visitors. . ."
            $ EmmaX.blushing = 0
        else:
            $ EmmaX.change_stat("love", 200, -5)
            $ EmmaX.change_face("angry")
            $ EmmaX.recent_history.append("angry")
            $ EmmaX.daily_history.append("angry")
            if bg_current == "bg_emma":
                ch_e "You may have noticed, I had some work to take care of, so if you'll leave me to it. . ."
                "[EmmaX.name] kicks you out of her room."
                $ renpy.pop_call()
                jump Campus_Map
            else:
                ch_e "I think I'll be leaving, if you don't mind."
                call Remove_Girl (EmmaX)
        return




    if action_context == EmmaX:
        if Approval > 2:
            if EmmaX.PantsNum() == 5:
                "[EmmaX.name]'s hand snakes down her body, and hikes up her skirt."
                $ EmmaX.Upskirt = 1
            elif EmmaX.PantsNum() > 6:
                "[EmmaX.name] slides her hand down her body and into her pants."
            elif EmmaX.HoseNum() >= 5:
                "[EmmaX.name]'s hand slides down her body and under her [EmmaX.hose]."
            elif EmmaX.underwear:
                "[EmmaX.name]'s hand slides down her body and under her [EmmaX.underwear]."
            else:
                "[EmmaX.name]'s hand slides down her body and begins to caress her pussy."
            $ EmmaX.SeenPanties = 1
            "She starts to slowly rub herself."
            call Emma_First_Bottomless
            menu:
                "What do you do?"
                "Nothing.":
                    $ EmmaX.change_stat("inhibition", 80, 3)
                    $ EmmaX.change_stat("inhibition", 60, 2)
                    "[EmmaX.name] begins to masturbate."
                "Go for it.":
                    $ EmmaX.change_face("sexy, 1")
                    $ EmmaX.change_stat("inhibition", 80, 3)
                    ch_p "That is so sexy, [EmmaX.petname]."
                    $ EmmaX.nameCheck()
                    "You lean back and enjoy the show."
                    $ EmmaX.change_stat("love", 80, 1)
                    $ EmmaX.change_stat("obedience", 90, 1)
                    $ EmmaX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ EmmaX.change_face("surprised")
                    $ EmmaX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that right now, [EmmaX.petname]."
                    $ EmmaX.nameCheck()
                    "[EmmaX.name] pulls her hands away from herself."
                    $ EmmaX.change_outfit()
                    $ EmmaX.change_stat("obedience", 90, 1)
                    $ EmmaX.change_stat("obedience", 50, 1)
                    $ EmmaX.change_stat("obedience", 30, 2)
                    return
            jump Emma_M_Prep
        else:
            $ approval_bonus = 0
            $ offhand_action = 0
        return



    if not EmmaX.action_counter["masturbation"]:
        $ EmmaX.change_face("surprised", 1)
        $ EmmaX.mouth = "kiss"
        ch_e "So you enjoy a good show then. . ."
        if EmmaX.Forced:
            $ EmmaX.change_face("sad")
            ch_e "but. . . {i}only{/i} a show?"



    if not EmmaX.action_counter["masturbation"] and Approval:
        if EmmaX.Forced:
            $ EmmaX.change_face("sad")
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
        elif EmmaX.love >= EmmaX.obedience and EmmaX.love >= EmmaX.inhibition:
            $ EmmaX.change_face("sexy")
            $ EmmaX.brows = "sad"
            $ EmmaX.mouth = "smile"
            ch_e "I don't usually show this side . . ."
        elif EmmaX.obedience >= EmmaX.inhibition:
            $ EmmaX.change_face("normal")
            ch_e "If that's what you're into, [EmmaX.player_petname]. . ."
        else:
            $ EmmaX.change_face("sad")
            $ EmmaX.mouth = "smile"
            ch_e "I do enjoy a good performance . . ."



    elif Approval:
        if EmmaX.Forced:
            $ EmmaX.change_face("sad")
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
            ch_e "Again? Just you only want to watch?"
        elif Approval and "masturbation" in EmmaX.recent_history:
            $ EmmaX.change_face("sexy", 1)
            ch_e "I still have some. . . work I could be doing. . ."
            jump Emma_M_Prep
        elif Approval and "masturbation" in EmmaX.daily_history:
            $ EmmaX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["I was that good?",       
                    "Didn't get enough earlier?",
                    "I did enjoy the audience participation. . ."])
            ch_e "[Line]"
        elif EmmaX.action_counter["masturbation"] < 3:
            $ EmmaX.change_face("sexy", 1)
            $ EmmaX.brows = "confused"
            ch_e "You enjoyed the show?"
        else:
            $ EmmaX.change_face("sexy", 1)
            $ EmmaX.ArmPose = 2
            $ Line = renpy.random.choice(["You really do like to watch.",                 
                    "Once more?",                 
                    "You enjoy watching me.",
                    "You want me to take care of myself?"])
            ch_e "[Line]"
            $ Line = 0



    if Approval >= 2:
        if EmmaX.Forced:
            $ EmmaX.change_face("sad")
            $ EmmaX.change_stat("obedience", 90, 1)
            $ EmmaX.change_stat("inhibition", 60, 1)
            ch_e "Fine. . ."
        else:
            $ EmmaX.change_face("sexy", 1)
            $ EmmaX.change_stat("love", 90, 1)
            $ EmmaX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Ok.",                 
                    "It couldn't hurt having you around. . .",
                    "Very well.", 
                    "Sure, why not?",
                    "[[chuckles]. . . ok."])
            ch_e "[Line]"
            $ Line = 0
        $ EmmaX.change_stat("obedience", 20, 1)
        $ EmmaX.change_stat("obedience", 60, 1)
        $ EmmaX.change_stat("inhibition", 70, 2)
        jump Emma_M_Prep
    else:


        menu:
            ch_e "I don't know that I want to perform."
            "Maybe later?":
                $ EmmaX.change_face("sexy", 1)
                if EmmaX.lust > 70:
                    ch_e "I have plans for. . . later, but perhaps you could take part."
                else:
                    ch_e "I couldn't say."
                $ EmmaX.change_stat("love", 80, 2)
                $ EmmaX.change_stat("inhibition", 70, 2)
                return
            "You look like you could use it. . .":
                if Approval:
                    $ EmmaX.change_face("sexy")
                    $ EmmaX.change_stat("obedience", 90, 2)
                    $ EmmaX.change_stat("obedience", 50, 2)
                    $ EmmaX.change_stat("inhibition", 70, 3)
                    $ EmmaX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["Ok.",                 
                            "It couldn't hurt having you around. . .",
                            "Very well.", 
                            "Sure, why not?",
                            "[[chuckles]. . . ok."])
                    ch_e "[Line]"
                    $ Line = 0
                    jump Emma_M_Prep
            "Just get at it already.":

                $ Approval = ApprovalCheck(EmmaX, 450, "OI", TabM = 2)
                if Approval > 1 or (Approval and EmmaX.Forced):
                    $ EmmaX.change_face("sad")
                    $ EmmaX.change_stat("love", 70, -5, 1)
                    $ EmmaX.change_stat("love", 200, -5)
                    ch_e "Oh, if it will shut you up."
                    $ EmmaX.change_stat("obedience", 80, 4)
                    $ EmmaX.change_stat("inhibition", 80, 1)
                    $ EmmaX.change_stat("inhibition", 60, 3)
                    $ EmmaX.Forced = 1
                    jump Emma_M_Prep
                else:
                    $ EmmaX.change_stat("love", 200, -20)
                    $ EmmaX.recent_history.append("angry")
                    $ EmmaX.daily_history.append("angry")



    $ EmmaX.ArmPose = 1
    if EmmaX.Forced:
        $ EmmaX.change_face("angry", 1)
        ch_e "That's something I won't do."
        $ EmmaX.change_stat("lust", 90, 5)
        if EmmaX.love > 300:
            $ EmmaX.change_stat("love", 70, -2)
        $ EmmaX.change_stat("obedience", 50, -2)
        $ EmmaX.recent_history.append("angry")
        $ EmmaX.daily_history.append("angry")
        $ EmmaX.recent_history.append("no_masturbation")
        $ EmmaX.daily_history.append("no_masturbation")
        return
    elif Taboo:
        $ EmmaX.change_face("angry", 1)
        $ EmmaX.daily_history.append("no_taboo")
        ch_e "Obviously not in someplace so exposed."
        $ EmmaX.change_stat("lust", 90, 5)
        $ EmmaX.change_stat("obedience", 50, -3)
        return
    elif EmmaX.action_counter["masturbation"]:
        $ EmmaX.change_face("sad")
        ch_e "I'm sure you can find something else to watch."
    else:
        $ EmmaX.change_face("normal", 1)
        ch_e "I don't think so, [EmmaX.player_petname]."
    $ EmmaX.recent_history.append("no_masturbation")
    $ EmmaX.daily_history.append("no_masturbation")
    $ approval_bonus = 0
    return

label Emma_M_Prep:
    $ EmmaX.Upskirt = 1
    $ EmmaX.underwearDown = 1
    call Emma_First_Bottomless (1)
    call set_the_scene (Dress=0)


    if "unseen" in EmmaX.recent_history:
        $ EmmaX.change_face("sexy")
        $ EmmaX.eyes = "closed"
        $ EmmaX.ArmPose = 2
        "You see [EmmaX.name] leaning back, masturbating. You don't think she's noticed you yet."
    else:
        $ EmmaX.change_face("sexy")
        $ EmmaX.ArmPose = 2
        "[EmmaX.name] lays back and starts to toy with herself."
        if not EmmaX.action_counter["masturbation"]:
            if EmmaX.Forced:
                $ EmmaX.change_stat("love", 90, -20)
                $ EmmaX.change_stat("obedience", 70, 45)
                $ EmmaX.change_stat("inhibition", 80, 35)
            else:
                $ EmmaX.change_stat("love", 90, 15)
                $ EmmaX.change_stat("obedience", 70, 35)
                $ EmmaX.change_stat("inhibition", 80, 40)


    $ primary_action = "masturbation"
    if not girl_offhand_action:
        $ girl_offhand_action = "fondle_pussy"

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    if Taboo:
        $ EmmaX.DrainWord("no_taboo")
    $ EmmaX.DrainWord("no_masturbation")
    $ EmmaX.recent_history.append("masturbation")
    $ EmmaX.daily_history.append("masturbation")

label Emma_M_Cycle:
    if action_context == "join":
        $ renpy.pop_call()
        $ action_context = 0

    while Round > 0:
        call Emma_Pos_Reset ("masturbation")
        call shift_focus (EmmaX)
        $ EmmaX.lust_face()
        if "unseen" in EmmaX.recent_history:
            $ EmmaX.eyes = "closed"

        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if Player.focus < 100:

            menu:
                "Keep Watching.":
                    pass

                "[EmmaX.name]. . .[[jump in]" if "unseen" not in EmmaX.recent_history and "join" not in Player.recent_history and EmmaX.location == bg_current:
                    "[EmmaX.name] slows what she's doing with a sly grin."
                    ch_e "Enjoying the show?"
                    $ action_context = "join"
                    call Emma_Masturbate
                "\"Ahem. . .\"" if "unseen" in EmmaX.recent_history and EmmaX.location == bg_current:
                    jump Emma_M_Interupted

                "Start jack'in it." if offhand_action != "jackin":
                    call Jackin (EmmaX)
                "Stop jack'in it." if offhand_action == "jackin":
                    $ offhand_action = 0

                "Slap her ass" if EmmaX.location == bg_current:
                    if "unseen" in EmmaX.recent_history:
                        "You smack [EmmaX.name] firmly on the ass!"
                        jump Emma_M_Interupted
                    else:
                        call Slap_Ass (EmmaX)
                        $ counter += 1
                        $ Round -= 1
                        jump Emma_M_Cycle

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
                        "Offhand action" if EmmaX.location == bg_current:
                            if EmmaX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ EmmaX.remaining_actions -= 1
                            else:
                                ch_e "I'm actually getting a little tired, perhaps we could wrap this up?"

                        "Threesome actions (locked)" if not Partner or "unseen" in EmmaX.recent_history or EmmaX.location != bg_current:
                            pass
                        "Threesome actions" if Partner and "unseen" not in EmmaX.recent_history and EmmaX.location == bg_current:
                            menu:
                                "Ask [Partner.name] to do something else":
                                    call Three_Change (EmmaX)
                                "Swap to [Partner.name]":
                                    call primary_action_Swap (EmmaX)
                                "Undress [Partner.name]":
                                    call Girl_Undress (Partner)
                                    jump Emma_M_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Emma_M_Cycle
                                "Never mind":
                                    jump Emma_M_Cycle

                        "Show her feet" if not ShowFeet and EmmaX.pose == "doggy":
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and EmmaX.pose == "doggy":
                            $ ShowFeet = 0
                        "Undress [EmmaX.name]":

                            if "unseen" in EmmaX.recent_history:
                                ch_p "Oh, yeah, take it off. . ."
                                jump Emma_M_Interupted
                            else:
                                call Girl_Undress (EmmaX)
                        "Clean up [EmmaX.name] (locked)" if not EmmaX.Spunk:
                            pass
                        "Clean up [EmmaX.name]" if EmmaX.Spunk:
                            if "unseen" in EmmaX.recent_history:
                                ch_p "You've got a little something on you. . ."
                                jump Emma_M_Interupted
                            else:
                                call Girl_Cleanup (EmmaX, "ask")
                        "Never mind":
                            jump Emma_M_Cycle

                "Back to Sex Menu" if multi_action and EmmaX.location == bg_current:
                    ch_p "Let's try something else."
                    call Emma_Pos_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Emma_M_Interupted
                "End Scene" if not multi_action or EmmaX.location != bg_current:
                    ch_p "Let's stop for now."
                    call Emma_Pos_Reset
                    $ Line = 0
                    jump Emma_M_Interupted


        call shift_focus (EmmaX)
        call Sex_Dialog (EmmaX, Partner)



        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus

        if Player.focus >= 100 or EmmaX.lust >= 100:

            if Player.focus >= 100:
                if "unseen" not in EmmaX.recent_history:

                    call Player_Cumming (EmmaX)
                    if "angry" in EmmaX.recent_history:
                        call Emma_Pos_Reset
                        return
                    $ EmmaX.change_stat("lust", 200, 5)
                    if 100 > EmmaX.lust >= 70 and EmmaX.session_orgasms < 2:
                        $ EmmaX.recent_history.append("unsatisfied")
                        $ EmmaX.daily_history.append("unsatisfied")
                    $ Line = "came"
                else:
                    "You grunt and try to hold it in."
                    $ Player.focus = 95
                    if EmmaX.location == bg_current or EmmaX.location == "bg_desk":
                        jump Emma_M_Interupted


            if EmmaX.lust >= 100:
                call Girl_Cumming (EmmaX)
                if EmmaX.location == bg_current or EmmaX.location == "bg_desk":
                    jump Emma_M_Interupted

            if Line == "came":
                $ Line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."
                    $ offhand_action = 0 if offhand_action == "jackin" else offhand_action


                if "unsatisfied" in EmmaX.recent_history:
                    "[EmmaX.name] still seems a bit unsatisfied with the experience."
                    menu:
                        "Let her keep going?"
                        "Yes, keep going for a bit.":
                            $ Line = "You let her get back into it"
                            jump Emma_M_Cycle
                        "No, I'm done.":
                            "You ask her to stop."
                            return
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        if "unseen" in EmmaX.recent_history:
            if Round == 10:
                "It's getting a bit late, [EmmaX.name] will probably be wrapping up soon."
            elif Round == 5:
                "She's definitely going to stop soon."
        else:
            if EmmaX.location == bg_current:
                call Escalation (EmmaX)

            if Round == 10:
                ch_e "I think I'll probably take a break soon."
                $ EmmaX.lust += 10
            elif Round == 5:
                ch_e "Ung, I'm almost finished. . ."
                $ EmmaX.lust += 25


    $ EmmaX.change_face("bemused", 0)
    $ Line = 0
    if "unseen" not in EmmaX.recent_history:
        ch_e "That's probably enough of that."

label Emma_M_Interupted:


    if "unseen" in EmmaX.recent_history:
        $ EmmaX.change_face("surprised", 2)
        "[EmmaX.name] stops what she's doing with a start, eyes wide."
        call Emma_First_Bottomless (1)
        $ EmmaX.change_face("confused", 1, Eyes="surprised")
        if EmmaX.location == "bg_desk":
            $ EmmaX.location = bg_current
            call Display_Girl (EmmaX)
            "She approaches you."


        if offhand_action == "jackin":
            ch_e "!"
            ch_e "How long have you been there?!"
            $ EmmaX.eyes = "down"
            menu:
                ch_e "And I see you've been busy. . . "
                "A little while, it was an excellent show.":
                    $ EmmaX.change_face("sexy",1)
                    $ EmmaX.change_stat("obedience", 50, 3)
                    $ EmmaX.change_stat("obedience", 70, 2)
                    ch_e "Well, obviously. . ."
                    if EmmaX.love >= 800 or EmmaX.obedience >= 500 or EmmaX.inhibition >= 500:
                        $ approval_bonus += 10
                        $ EmmaX.change_stat("lust", 90, 5)
                    ch_e "and I suppose you bring a lot to the table as well, don't you. . ."
                "I. . . just got here?":

                    $ EmmaX.change_face("angry",1, Eyes="down")
                    $ EmmaX.change_stat("love", 70, 2)
                    $ EmmaX.change_stat("love", 90, 1)
                    $ EmmaX.change_stat("obedience", 50, 2)
                    $ EmmaX.change_stat("obedience", 70, 2)
                    "She looks pointedly at your cock,"
                    $ EmmaX.eyes = "squint"
                    ch_e "Long enough to raise your sails?"
                    if EmmaX.love >= 800 or EmmaX.obedience >= 500 or EmmaX.inhibition >= 500:
                        $ approval_bonus += 10
                        $ EmmaX.change_stat("lust", 90, 5)
                        $ EmmaX.change_face("bemused", 1)
                        ch_e "I suppose you couldn't help yourself under the circumstances. . ."
                    else:
                        $ approval_bonus -= 10
                        $ EmmaX.change_stat("lust", 200, -5)

            if "Historia" not in Player.Traits:
                call Seen_First_Peen (EmmaX, Partner)
                ch_e "Hmm. . ."
        else:


            ch_e "!"
            ch_e "How long have you been there?!"
            menu:
                extend ""
                "A little while.":
                    $ EmmaX.change_face("sexy", 1)
                    $ EmmaX.change_stat("obedience", 50, 3)
                    $ EmmaX.change_stat("obedience", 70, 2)
                    ch_e "Enjoying the show?"
                "I just got here.":
                    $ EmmaX.change_face("bemused", 1)
                    $ EmmaX.change_stat("love", 70, 2)
                    $ EmmaX.change_stat("love", 90, 1)
                    ch_e "Yes, I'm sure. . ."
                    $ EmmaX.change_stat("obedience", 50, 2)
                    $ EmmaX.change_stat("obedience", 70, 2)

        $ EmmaX.DrainWord("unseen",1,0)
        $ EmmaX.action_counter["masturbation"] += 1
        if "classcaught" not in EmmaX.history or "Historia" in Player.Traits:

            return
        if Round <= 10:
            ch_e "Unfortunately it's getting rather late."
            return
        $ action_context = "join"
        call Emma_Masturbate
        "error: report this if you see it."
        return



    $ EmmaX.remaining_actions -= 1
    $ EmmaX.action_counter["masturbation"] += 1
    call Checkout
    if action_context == "shift":
        $ action_context = 0
        return
    $ action_context = 0

    if Partner == "Kitty":
        call Partner_Like (EmmaX, 4, 2)
    else:
        call Partner_Like (EmmaX, 3, 2)

    if EmmaX.location != bg_current and EmmaX.location != "bg_desk":
        return

    if Round <= 10:
        ch_e "Allow me to collect myself. . ."
        return
    $ EmmaX.change_face("sexy", 1)
    if EmmaX.lust < 20:
        ch_e "I suppose that took care of my needs, at least."
    else:
        ch_e "Yes?"
    menu:
        extend ""
        "Well, I have something you could take care of. . ." if Player.semen and EmmaX.remaining_actions and multi_action:
            $ action_context = "shift"
            return
        "You could just keep going. . ." if Player.semen:
            $ EmmaX.change_face("sly")
            if EmmaX.remaining_actions and Round >= 10:
                ch_e "I suppose. . ."
                jump Emma_M_Cycle
            else:
                ch_e "Gimme a minute, I need to collect myself here. . ."
        "I'm good here. [[Stop]":
            if EmmaX.love < 800 and EmmaX.inhibition < 500 and EmmaX.obedience < 500:
                $ EmmaX.change_outfit()
            $ EmmaX.change_face("normal")
            $ EmmaX.brows = "confused"
            ch_e "Well. . . yes. . ."
            $ EmmaX.brows = "normal"
        "You should probably stop for now." if EmmaX.lust > 30:
            $ EmmaX.change_face("angry")
            ch_e "I . . . yes . ."
    if offhand_action == "jackin":
        $ offhand_action = 0
    return






label Emma_Sex_P:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (EmmaX)
    if EmmaX.action_counter["sex"] >= 7:
        $ approval_bonus += 15
    elif EmmaX.action_counter["sex"] >= 3:
        $ approval_bonus += 12
    elif EmmaX.action_counter["sex"]:
        $ approval_bonus += 10

    if EmmaX.addiction >= 75 and (EmmaX.event_counter["creampied"] + EmmaX.event_counter["anal_creampied"]) >=3:
        $ approval_bonus += 20
    elif EmmaX.addiction >= 75:
        $ approval_bonus += 15

    if EmmaX.lust > 85:
        $ approval_bonus += 10
    elif EmmaX.lust > 75:
        $ approval_bonus += 5

    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in EmmaX.Traits:
        $ approval_bonus += (4*Taboo)
    if EmmaX in Player.Harem or "sex friend" in EmmaX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in EmmaX.Traits:
        $ approval_bonus -= 40
    if EmmaX.event_counter["forced"] and not EmmaX.Forced:
        $ approval_bonus -= 5*EmmaX.event_counter["forced"]



    if Taboo and "no_taboo" in EmmaX.daily_history:
        $ approval_bonus -= 10

    if "no_sex" in EmmaX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_sex" in EmmaX.recent_history else 0


    $ Approval = ApprovalCheck(EmmaX, 1400, TabM = 5)

    if action_context == "auto":
        call Emma_Sex_Launch ("sex")
        if EmmaX.PantsNum() == 5:
            "You roll back, pulling [EmmaX.name] on top of you, sliding her skirt up as you go."
            $ EmmaX.Upskirt = 1
        elif EmmaX.PantsNum() >= 6:
            "You roll back, pulling [EmmaX.name] on top of you, sliding her [EmmaX.legs] down as you do."
            $ EmmaX.legs = 0
        else:
            "You roll back, pulling [EmmaX.name] on top of you."
        $ EmmaX.SeenPanties = 1
        "You rub the tip of your cock against her moist slit."
        $ EmmaX.change_face("surprised", 1)

        if (EmmaX.action_counter["sex"] and Approval) or (Approval > 1):

            "[EmmaX.name] is briefly startled, but melts into a sly smile."
            $ EmmaX.change_face("sly")
            $ EmmaX.change_stat("obedience", 70, 3)
            $ EmmaX.change_stat("inhibition", 50, 3)
            $ EmmaX.change_stat("inhibition", 70, 1)
            ch_e "Mmm, if you insist, [EmmaX.player_petname]."
            jump Emma_SexPrep
        else:

            $ EmmaX.brows = "angry"
            menu:
                ch_e "Do you really think you can handle that?"
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ EmmaX.change_face("sexy", 1)
                        $ EmmaX.change_stat("obedience", 70, 3)
                        $ EmmaX.change_stat("inhibition", 50, 3)
                        $ EmmaX.change_stat("inhibition", 70, 1)
                        ch_e "I am willing to give it a try if you are. . ."
                        jump Emma_SexPrep
                    else:
                        "You pull back before you really get it in."
                        $ EmmaX.change_face("bemused", 1)
                        if EmmaX.action_counter["sex"]:
                            ch_e "Perhaps ask first, [EmmaX.player_petname]."
                        else:
                            ch_e "Perhaps some other time, when you ask nicely."
                "Just fucking.":
                    $ EmmaX.change_stat("love", 80, -10, 1)
                    $ EmmaX.change_stat("love", 200, -10)
                    "You press inside some more."
                    $ EmmaX.change_stat("obedience", 70, 3)
                    $ EmmaX.change_stat("inhibition", 50, 3)
                    if not ApprovalCheck(EmmaX, 700, "O", TabM=1):
                        $ EmmaX.change_face("angry")
                        "[EmmaX.name] shoves you away and backhands you in the face."
                        ch_e "Impertinent!"
                        ch_e "do not test my patience with you."
                        $ EmmaX.change_stat("love", 50, -10, 1)
                        $ EmmaX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        call Emma_Sex_Reset
                        $ EmmaX.recent_history.append("angry")
                        $ EmmaX.daily_history.append("angry")
                    else:
                        $ EmmaX.change_face("sad")
                        "[EmmaX.name] doesn't seem to be into this, you're lucky she's so obedient."
                        jump Emma_SexPrep
        return



    if not EmmaX.action_counter["sex"] and "no_sex" not in EmmaX.recent_history:

        $ EmmaX.change_face("surprised", 1)
        $ EmmaX.mouth = "kiss"
        ch_e "Hmm, are you sure you're really prepared for this? . . "
        if EmmaX.Forced:
            $ EmmaX.change_face("sad")
            ch_e "Are you sure this is how you'd like to use your. . . influence?"


    if not EmmaX.action_counter["sex"] and Approval:

        if EmmaX.Forced:
            $ EmmaX.change_face("sad")
            $ EmmaX.change_stat("love", 70, -30, 1)
            $ EmmaX.change_stat("love", 20, -20, 1)
        elif EmmaX.love >= (EmmaX.obedience + EmmaX.inhibition):
            $ EmmaX.change_face("sexy")
            $ EmmaX.brows = "sad"
            $ EmmaX.mouth = "smile"
            ch_e "I wouldn't want you to get hurt. . ."
        elif EmmaX.obedience >= EmmaX.inhibition:
            $ EmmaX.change_face("normal")
            ch_e "If you insist, [EmmaX.player_petname]. . ."
        elif EmmaX.addiction >= 50:
            $ EmmaX.change_face("manic", 1)
            ch_e "I was wondering how it would feel with you. . ."
        else:
            $ EmmaX.change_face("sad")
            $ EmmaX.mouth = "smile"
            ch_e "I was hoping you'd ask. . ."


    elif Approval:

        $ EmmaX.change_face("sexy", 1)
        if EmmaX.Forced:
            $ EmmaX.change_face("sad")
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
            ch_e "Again? You're really wearing out your welcome."
        elif not Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "I suppose this is more private."
        elif "sex" in EmmaX.recent_history:
            ch_e "Again? [EmmaX.player_petname], you're insatiable!"
            jump Emma_SexPrep
        elif "sex" in EmmaX.daily_history:
            $ Line = renpy.random.choice(["Back again?",                 
                    "You'd like another round?",                 
                    "I suppose I am irresistible. . .", 
                    "Didn't get enough earlier?",
                    "You're wearing me out, " + EmmaX.player_petname + "."])
            ch_e "[Line]"
        elif EmmaX.action_counter["sex"] < 3:
            $ EmmaX.brows = "confused"
            $ EmmaX.mouth = "kiss"
            ch_e "Oh? Another round?"
        else:
            $ Line = renpy.random.choice(["Oh, you want some of this?",                 
                    "You'd like another round?",                 
                    "I suppose I am irresistible. . .", 
                    "Do you intend to make me melt?",
                    "You want me to ride you?"])
            ch_e "[Line]"
        $ Line = 0


    if Approval >= 2:

        if EmmaX.Forced:
            $ EmmaX.change_face("sad")
            $ EmmaX.change_stat("obedience", 90, 1)
            $ EmmaX.change_stat("inhibition", 60, 1)
            ch_e "Oh, fine, if it will shut you up."
        elif "no_sex" in EmmaX.daily_history:
            ch_e "Very well, you've convinced me. . ."
        else:
            $ EmmaX.change_face("sexy", 1)
            $ EmmaX.change_stat("love", 90, 1)
            $ EmmaX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well. . . fine, I accept.",                 
                    "Sure!", 
                    "We could, I suppose.",
                    "Hmmm, yes.",
                    "How could I refuse?"])
            ch_e "[Line]"
            $ Line = 0
        $ EmmaX.change_stat("obedience", 20, 1)
        $ EmmaX.change_stat("obedience", 60, 1)
        $ EmmaX.change_stat("inhibition", 70, 2)
        jump Emma_SexPrep
    else:


        $ EmmaX.change_face("angry")
        if "no_sex" in EmmaX.recent_history:
            ch_e "I'm afraid that \"no\" is my final answer, [EmmaX.player_petname]."
        elif Taboo and "no_taboo" in EmmaX.daily_history and "no_sex" in EmmaX.daily_history:
            ch_e "I already told you. . .not in such an exposed location."
        elif "no_sex" in EmmaX.daily_history:
            ch_e "I believe I just told you \"no,\" [EmmaX.player_petname]."
        elif Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "I already told you this is too public!"
        elif not EmmaX.action_counter["sex"]:
            $ EmmaX.change_face("bemused")
            ch_e "I really doubt you understand what you're in for. . ."
        else:
            $ EmmaX.change_face("bemused")
            ch_e "Perhaps another time would be better? . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_sex" in EmmaX.daily_history:
                $ EmmaX.change_face("bemused")
                ch_e "I can appreciate your. . . drive."
                return
            "Maybe later?" if "no_sex" not in EmmaX.daily_history:
                $ EmmaX.change_face("sexy")
                ch_e "Oh, most certainly. . ."
                $ EmmaX.change_stat("love", 80, 2)
                $ EmmaX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ EmmaX.recent_history.append("no_taboo")
                    $ EmmaX.daily_history.append("no_taboo")
                $ EmmaX.recent_history.append("no_sex")
                $ EmmaX.daily_history.append("no_sex")
                return
            "I think you'd enjoy it as much as I would. . .":
                if Approval:
                    $ EmmaX.change_face("sexy")
                    $ EmmaX.change_stat("obedience", 90, 2)
                    $ EmmaX.change_stat("obedience", 50, 2)
                    $ EmmaX.change_stat("inhibition", 70, 3)
                    $ EmmaX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["I can't exactly argue with that. . .",     
                                "I suppose. . .", 
                                "You raise a good point. . ."])
                    ch_e "[Line]"
                    $ Line = 0
                    jump Emma_SexPrep
            "Just deal with it.":
                $ Approval = ApprovalCheck(EmmaX, 1150, "OI", TabM = 3)
                if Approval > 1 or (Approval and EmmaX.Forced):
                    $ EmmaX.change_face("sad")
                    $ EmmaX.change_stat("love", 70, -5, 1)
                    $ EmmaX.change_stat("love", 200, -5)
                    ch_e "Fine, if it'll shut you up."
                    $ EmmaX.change_stat("obedience", 80, 4)
                    $ EmmaX.change_stat("inhibition", 80, 1)
                    $ EmmaX.change_stat("inhibition", 60, 3)
                    $ EmmaX.Forced = 1
                    jump Emma_SexPrep
                else:
                    $ EmmaX.change_stat("love", 200, -20)
                    $ EmmaX.recent_history.append("angry")
                    $ EmmaX.daily_history.append("angry")




    $ EmmaX.ArmPose = 1
    if "no_sex" in EmmaX.daily_history:
        ch_e "Don't question me again."
        $ EmmaX.recent_history.append("angry")
        $ EmmaX.daily_history.append("angry")
    elif EmmaX.Forced:
        $ EmmaX.change_face("angry", 1)
        ch_e "Don't overestimate your leverage here."
        $ EmmaX.change_stat("lust", 200, 5)
        if EmmaX.love > 300:
            $ EmmaX.change_stat("love", 70, -2)
        $ EmmaX.change_stat("obedience", 50, -2)
        $ EmmaX.recent_history.append("angry")
        $ EmmaX.daily_history.append("angry")
    elif Taboo:
        $ EmmaX.change_face("angry", 1)
        $ EmmaX.recent_history.append("no_taboo")
        $ EmmaX.daily_history.append("no_taboo")
        ch_e "How can you imagine this would be an appropriate location?"
        $ EmmaX.change_stat("lust", 200, 5)
        $ EmmaX.change_stat("obedience", 50, -3)
    elif EmmaX.action_counter["sex"]:
        $ EmmaX.change_face("sad")
        ch_e "I'm sure you can figure out how to take care of that yourself."
    else:
        $ EmmaX.change_face("normal", 1)
        ch_e "I'm afraid not."
    $ EmmaX.recent_history.append("no_sex")
    $ EmmaX.daily_history.append("no_sex")
    $ approval_bonus = 0
    return

label Emma_SexPrep:
    call Seen_First_Peen (EmmaX, Partner, React=action_context)
    call Emma_Sex_Launch ("hotdog")

    if action_context == EmmaX:

        $ action_context = 0
        if EmmaX.PantsNum() == 5:
            "[EmmaX.name] pushes you back and climbs on top of you, sliding her skirt up as she does so."
            $ EmmaX.Upskirt = 1
        elif EmmaX.PantsNum() >= 6:
            "[EmmaX.name] pushes you down and climbs on top of you, sliding her [EmmaX.legs] down as she does so."
            $ EmmaX.Upskirt = 1
        else:
            "[EmmaX.name] pushes you back and climbs on top of you."
        $ EmmaX.SeenPanties = 1
        "She slides the tip along her pussy and seems to want you to insert it."
        menu:
            "What do you do?"
            "Go with it.":
                $ EmmaX.change_stat("inhibition", 80, 3)
                $ EmmaX.change_stat("inhibition", 50, 2)
                "[EmmaX.name] slides it in."
            "Praise her.":
                $ EmmaX.change_face("sexy", 1)
                $ EmmaX.change_stat("inhibition", 80, 3)
                ch_p "Oh yeah, [EmmaX.petname], let's do this."
                $ EmmaX.nameCheck()
                "[EmmaX.name] slides it in."
                $ EmmaX.change_stat("love", 85, 1)
                $ EmmaX.change_stat("obedience", 90, 1)
                $ EmmaX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ EmmaX.change_face("surprised")
                $ EmmaX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [EmmaX.petname]."
                $ EmmaX.nameCheck()
                "[EmmaX.name] pulls back."
                $ EmmaX.change_stat("obedience", 90, 1)
                $ EmmaX.change_stat("obedience", 50, 1)
                $ EmmaX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ EmmaX.AddWord(1,"refused","refused")
                return
        $ EmmaX.underwearDown = 1
        call Emma_First_Bottomless (1)

    elif action_context != "auto":
        call AutoStrip (EmmaX)

        if Taboo:
            "[EmmaX.name] glances around to see if anyone notices what she's doing."
            if "cockout" in Player.recent_history:
                "Then she pushes you back and slowly presses against your rigid member."
            else:
                "Then she pulls down your pants and climbs on top of you."
                "She slowly presses against your rigid member."
            $ EmmaX.inhibition += int(Taboo/10)
            $ EmmaX.lust += int(Taboo/5)
        else:
            if "cockout" in Player.recent_history:
                "[EmmaX.name] pushes you back and slowly presses against your rigid member."
            else:
                "[EmmaX.name] pulls down your pants and climbs on top of you."
                "She slowly presses against your rigid member."
        "She leans back a bit and your cock slides in."
    else:

        if (EmmaX.PantsNum() > 6 and not EmmaX.Upskirt) and (EmmaX.underwear and not EmmaX.underwearDown):
            "You quickly pull down her pants and her [EmmaX.underwear] and press against her slit."
        elif (EmmaX.underwear and not EmmaX.underwearDown):
            "You quickly pull down her [EmmaX.underwear] and press against her slit."
        $ EmmaX.Upskirt = 1
        $ EmmaX.underwearDown = 1
        $ EmmaX.SeenPanties = 1
        call Emma_First_Bottomless (1)

    if Player.focus >= 50:
        ch_e "My word [EmmaX.player_petname], your member is hard enough to crack diamond..and I should know."
    if not EmmaX.action_counter["sex"]:
        if EmmaX.Forced:
            $ EmmaX.change_stat("love", 90, -150)
            $ EmmaX.change_stat("obedience", 70, 60)
            $ EmmaX.change_stat("inhibition", 80, 50)
        else:
            $ EmmaX.change_stat("love", 90, 30)
            $ EmmaX.change_stat("obedience", 70, 30)
            $ EmmaX.change_stat("inhibition", 80, 60)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    $ Player.Cock = "in"
    $ primary_action = "sex"
    $ action_speed = 1
    if Taboo:
        $ EmmaX.DrainWord("no_taboo")
    $ EmmaX.DrainWord("no_sex")
    $ EmmaX.recent_history.append("sex")
    $ EmmaX.daily_history.append("sex")

label Emma_Sex_Cycle:
    while Round > 0:
        call shift_focus (EmmaX)
        call Emma_Sex_Launch ("sex")
        $ action_speed = 2 if action_speed >= 4 else action_speed
        $ EmmaX.lust_face()
        $ Player.Cock = "in"
        $ primary_action = "sex"
        $ EmmaX.Upskirt = 1
        $ EmmaX.underwearDown = 1

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

                    call Slap_Ass (EmmaX)
                    $ counter += 1
                    $ Round -= 1
                    jump Emma_Sex_Cycle
                "Turn her Around":

                    $ EmmaX.pose = "doggy" if EmmaX.pose != "doggy" else "sex"
                    "You turn her around. . ."
                    jump Emma_Sex_Cycle

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
                            if EmmaX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ EmmaX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (EmmaX, "tired")
                        "Shift primary action":

                            if EmmaX.remaining_actions and multi_action:
                                menu:
                                    "How about anal?":
                                        $ action_context = "shift"
                                        call Emma_SexAfter
                                        call Emma_Sex_A
                                    "Just stick it in her ass [[without asking].":
                                        $ action_context = "auto"
                                        call Emma_SexAfter
                                        call Emma_Sex_A
                                    "Pull back to hotdog her.":
                                        $ action_context = "pullback"
                                        call Emma_SexAfter
                                        call Emma_Sex_H
                                    "Never Mind":
                                        jump Emma_Sex_Cycle
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
                                    jump Emma_Sex_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Emma_Sex_Cycle
                                "Never mind":
                                    jump Emma_Sex_Cycle
                        "Just take a look at her.":
                            $ Player.Cock = 0
                            $ action_speed = 0

                        "Show her feet" if not ShowFeet and EmmaX.pose == "doggy":
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and EmmaX.pose == "doggy":
                            $ ShowFeet = 0
                        "Undress [EmmaX.name]":

                            call Girl_Undress (EmmaX)
                        "Clean up [EmmaX.name] (locked)" if not EmmaX.Spunk:
                            pass
                        "Clean up [EmmaX.name]" if EmmaX.Spunk:
                            call Girl_Cleanup (EmmaX, "ask")
                        "Never mind":
                            jump Emma_Sex_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Emma_Sex_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Emma_SexAfter
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Emma_Sex_Reset
                    $ Line = 0
                    jump Emma_SexAfter


        call shift_focus (EmmaX)
        call Sex_Dialog (EmmaX, Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or EmmaX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (EmmaX)
                if "angry" in EmmaX.recent_history:
                    call Emma_Sex_Reset
                    return
                $ EmmaX.change_stat("lust", 200, 5)
                if 100 > EmmaX.lust >= 70 and EmmaX.session_orgasms < 2:
                    $ EmmaX.recent_history.append("unsatisfied")
                    $ EmmaX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Emma_SexAfter
                $ Line = "came"

            if EmmaX.lust >= 100:

                call Girl_Cumming (EmmaX)
                if action_context == "shift" or "angry" in EmmaX.recent_history:
                    jump Emma_SexAfter

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "She's emptied you out, you'll need to take a break."
                    jump Emma_SexAfter
                elif "unsatisfied" in EmmaX.recent_history:

                    $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                    "[Line] Keep going?"
                    menu:
                        extend ""
                        "Yes, keep going for a bit." if Player.semen:
                            $ Line = "You get back into it"
                            jump Emma_Sex_Cycle
                        "No, I'm done." if Player.semen:
                            "You pull back."
                            jump Emma_SexAfter
                        "No, I'm spent." if not Player.semen:
                            "You pull back."
                            jump Emma_SexAfter
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif counter == (5 + EmmaX.Sex):
            $ EmmaX.brows = "confused"
            ch_e "So are we getting close?"
        elif counter == (10 + EmmaX.Sex):
            $ EmmaX.brows = "angry"
            ch_e "I'm . . .getting . . a bit. . . tired. . . here. . ."
            menu:
                ch_e "Could we. . . do something. . . else?"
                "How about a BJ?" if EmmaX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Emma_SexAfter
                    call Emma_Blowjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    $ counter += 1
                    jump Emma_Sex_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Emma_Sex_Reset
                    $ action_context = "shift"
                    jump Emma_SexAfter
                "No, get back down there.":
                    if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):
                        $ EmmaX.change_stat("love", 200, -5)
                        $ EmmaX.change_stat("obedience", 50, 3)
                        $ EmmaX.change_stat("obedience", 80, 2)
                        "She grumbles but keeps moving."
                    else:
                        $ EmmaX.change_face("angry", 1)
                        call Emma_Sex_Reset
                        "She scowls at you and pulls out."
                        ch_e "No, I think not."
                        $ EmmaX.change_stat("love", 50, -3, 1)
                        $ EmmaX.change_stat("love", 80, -4, 1)
                        $ EmmaX.change_stat("obedience", 30, -1, 1)
                        $ EmmaX.change_stat("obedience", 50, -1, 1)
                        $ EmmaX.recent_history.append("angry")
                        $ EmmaX.daily_history.append("angry")
                        jump Emma_SexAfter


        call Escalation (EmmaX)

        if Round == 10:
            ch_e "You might want to think about your endgame here. . ."
        elif Round == 5:
            ch_e "We'll need a break soon."


    $ EmmaX.change_face("bemused", 0)
    $ Line = 0
    ch_e "Ok, [EmmaX.player_petname], that's enough of that for now."

label Emma_SexAfter:
    if not action_context:
        $ Player.Sprite = 0
        $ Player.Cock = "out"
        call Emma_Sex_Reset

    $ EmmaX.change_face("sexy")

    $ EmmaX.action_counter["sex"] += 1
    $ EmmaX.remaining_actions -=1
    $ EmmaX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ EmmaX.addiction_rate += 1
    $ EmmaX.change_stat("inhibition", 30, 2)
    $ EmmaX.change_stat("inhibition", 70, 1)

    call Partner_Like (EmmaX, 3, 2)

    if "Emma Sex Addict" in Achievements:
        pass

    elif EmmaX.action_counter["sex"] >= 10:
        $ EmmaX.SEXP += 5
        $ Achievements.append("Emma Sex Addict")
        if not action_context:
            $ EmmaX.change_face("smile", 1)
            ch_e "I seem to fit you like a glove. . ."
    elif EmmaX.action_counter["sex"] == 1:
        $ EmmaX.SEXP += 20
        if not action_context:
            if EmmaX.love >= 500 and "unsatisfied" not in EmmaX.recent_history:
                ch_e "I assume I rocked your entire world."
            elif EmmaX.obedience <= 500 and Player.focus <= 20:
                $ EmmaX.mouth = "sad"
                ch_e "I hope you enjoyed that."
    elif EmmaX.action_counter["sex"] == 5:
        ch_e "We really should have done this sooner."
        ch_e "I can't imagine why I waited so long."
    elif not action_context:
        if "unsatisfied" in EmmaX.recent_history:
            $ EmmaX.change_face("angry")
            $ EmmaX.eyes = "side"
            ch_e "Could you have perhaps been more attentive? . ."

    $ approval_bonus = 0


    call Checkout
    return






label Emma_Sex_A:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (EmmaX)
    if EmmaX.action_counter["anal"] >= 7:
        $ approval_bonus += 20
    elif EmmaX.action_counter["anal"] >= 3:
        $ approval_bonus += 17
    elif EmmaX.action_counter["anal"]:
        $ approval_bonus += 15

    if EmmaX.addiction >= 75 and (EmmaX.event_counter["creampied"] + EmmaX.event_counter["anal_creampied"]) >=3:
        $ approval_bonus += 25
    elif EmmaX.addiction >= 75:
        $ approval_bonus += 15

    if EmmaX.lust > 85:
        $ approval_bonus += 10
    elif EmmaX.lust > 75:
        $ approval_bonus += 5

    $ approval_bonus += 10

    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in EmmaX.Traits:
        $ approval_bonus += (5*Taboo)

    if EmmaX in Player.Harem or "sex friend" in EmmaX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in EmmaX.Traits:
        $ approval_bonus -= 40
    if EmmaX.event_counter["forced"] and not EmmaX.Forced:
        $ approval_bonus -= 5*EmmaX.event_counter["forced"]

    if Taboo and "no_taboo" in EmmaX.daily_history:
        $ approval_bonus -= 10
    if "no_anal" in EmmaX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_anal" in EmmaX.recent_history else 0

    $ Approval = ApprovalCheck(EmmaX, 1550, TabM = 5)

    if action_context == "auto":
        call Emma_Sex_Launch ("anal")
        if EmmaX.PantsNum() == 5:
            "You roll back, pulling [EmmaX.name] on top of you, sliding her skirt up as you go."
            $ EmmaX.Upskirt = 1
        elif EmmaX.PantsNum() >= 6:
            "You roll back, pulling [EmmaX.name] on top of you, sliding her [EmmaX.legs] down as you do."
            $ EmmaX.legs = 0
        else:
            "You roll back, pulling [EmmaX.name] on top of you."
        $ EmmaX.SeenPanties = 1
        "You press the tip of your cock against her tight rim."
        $ EmmaX.change_face("surprised", 1)

        if (EmmaX.action_counter["anal"] and Approval) or (Approval > 1):

            $ EmmaX.change_stat("obedience", 70, 3)
            $ EmmaX.change_stat("inhibition", 50, 3)
            $ EmmaX.change_stat("inhibition", 70, 1)
            "[EmmaX.name] is briefly startled, but melts into a sly smile."
            ch_e "Oooh, naughty boy. . ."
            jump Emma_AnalPrep
        else:

            $ EmmaX.brows = "angry"
            menu:
                ch_e "Oh? What exactly are you doing back there?"
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ EmmaX.change_face("sexy", 1)
                        $ EmmaX.change_stat("obedience", 70, 3)
                        $ EmmaX.change_stat("inhibition", 50, 3)
                        $ EmmaX.change_stat("inhibition", 70, 1)
                        ch_e "Well, so long as you know what you're doing . ."
                        ch_e "I didn't say I was opposed. . ."
                        jump Emma_AnalPrep
                    "You pull back before you really get it in."
                    $ EmmaX.change_face("bemused", 1)

                    if EmmaX.action_counter["anal"]:
                        ch_e "I do appreciate a little warning. . ."
                    else:
                        ch_e "Perhaps we could work up to that. . ."
                "Just fucking.":
                    $ EmmaX.change_stat("love", 80, -10, 1)
                    $ EmmaX.change_stat("love", 200, -8)
                    "You press into her."
                    $ EmmaX.change_stat("obedience", 70, 3)
                    $ EmmaX.change_stat("inhibition", 50, 3)
                    if not ApprovalCheck(EmmaX, 700, "O", TabM=1):
                        $ EmmaX.change_face("angry")
                        "[EmmaX.name] shoves you away and backhands you in the face."
                        ch_e "Impertinent!"
                        ch_e "You need to ask a lady first."
                        $ EmmaX.change_stat("love", 50, -10, 1)
                        $ EmmaX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        call Emma_Sex_Reset
                        $ EmmaX.recent_history.append("angry")
                        $ EmmaX.daily_history.append("angry")
                    else:
                        $ EmmaX.change_face("sad")
                        "[EmmaX.name] doesn't seem to be into this, you're lucky she's so obedient."
                        jump Emma_AnalPrep
        return



    if not EmmaX.action_counter["anal"] and "no_anal" not in EmmaX.recent_history:

        $ EmmaX.change_face("surprised", 1)
        $ EmmaX.mouth = "kiss"
        ch_e "Oooh, naughty boy. Anal?"

        if EmmaX.Forced:
            $ EmmaX.change_face("sad")
            ch_e "Anal? That's your goto?"

    if "anal" in EmmaX.recent_history:
        $ EmmaX.change_face("sexy", 1)
        ch_e "Alright."
        jump Emma_AnalPrep


    if not EmmaX.action_counter["anal"] and Approval:

        if EmmaX.Forced:
            $ EmmaX.change_face("sad")
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
        elif EmmaX.love >= (EmmaX.obedience + EmmaX.inhibition):
            $ EmmaX.change_face("sexy")
            $ EmmaX.brows = "sad"
            $ EmmaX.mouth = "smile"
            ch_e "I was wondering when you'd ask. . ."
        elif EmmaX.obedience >= EmmaX.inhibition:
            $ EmmaX.change_face("normal")
            ch_e "I expected we'd get here at some point. . ."
        elif EmmaX.addiction >= 50:
            $ EmmaX.change_face("manic", 1)
            ch_e "Hmm, that would be an interesting experience. . ."
        else:
            $ EmmaX.change_face("sad")
            $ EmmaX.mouth = "smile"
            ch_e "I was getting tired of waiting. . ."

    elif Approval:

        if EmmaX.Forced:
            $ EmmaX.change_face("sad")
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
            ch_e "You don't hold back. . ."
        elif not Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "I suppose this is secluded enough. . ."
        elif "anal" in EmmaX.daily_history and not EmmaX.used_to_anal:
            pass
        elif "anal" in EmmaX.recent_history:
            ch_e "I am warmed up. . ."
            jump Emma_AnalPrep
        elif "anal" in EmmaX.daily_history:
            $ EmmaX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",                 
                    "So you'd like another round?",                 
                    "I'm still a little sore from earlier.", 
                    "Didn't get enough earlier?",
                    "You're wearing me out, " + EmmaX.player_petname + "."])
            ch_e "[Line]"
        else:
            $ EmmaX.change_face("sexy", 1)
            $ EmmaX.ArmPose = 2
            $ Line = renpy.random.choice(["Oooh, you want some of this?",                 
                    "So you'd like another round?",                 
                    "I knew you enjoyed it. . .", 
                    "Do you intend to make me melt?",
                    "You want me to ride you?"])
            ch_e "[Line]"
        $ Line = 0

    if Approval >= 2:

        if EmmaX.Forced:
            $ EmmaX.change_face("sad")
            $ EmmaX.change_stat("obedience", 90, 1)
            $ EmmaX.change_stat("inhibition", 60, 1)
            ch_e "Oh very well."
        elif "no_anal" in EmmaX.daily_history:
            ch_e "After some consideration. . ."
            ch_e "It might be entertaining."
        else:
            $ EmmaX.change_face("sexy", 1)
            $ EmmaX.change_stat("love", 90, 1)
            $ EmmaX.change_stat("inhibition", 50, 3)
            $ Line = renpy.random.choice(["Well. . . ok.",                 
                    "Sure!", 
                    "You could, I guess.",
                    "Um, yeah.",
                    "Heh, ok, ok."])
            ch_e "[Line]"
            $ Line = 0
        $ EmmaX.change_stat("obedience", 20, 1)
        $ EmmaX.change_stat("obedience", 60, 1)
        $ EmmaX.change_stat("inhibition", 70, 2)
        jump Emma_AnalPrep
    else:


        $ EmmaX.change_face("angry")
        if "no_anal" in EmmaX.recent_history:
            ch_e "I'm afraid that \"no\" is my final answer, [EmmaX.player_petname]."
        elif Taboo and "no_taboo" in EmmaX.daily_history and "no_anal" in EmmaX.daily_history:
            ch_e "I already told you. . .not in such an exposed location."
        elif "no_anal" in EmmaX.daily_history:
            ch_e "I believe I just told you \"no,\" [EmmaX.player_petname]."
        elif Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "I already told you this is too public!"
        elif not EmmaX.action_counter["anal"]:
            $ EmmaX.change_face("bemused")
            ch_e "I don't know that you're ready for that yet."
        else:
            $ EmmaX.change_face("bemused")
            ch_e "Perhaps we can work up to that."
        menu:
            extend ""
            "Sorry, never mind." if "no_anal" in EmmaX.daily_history:
                $ EmmaX.change_face("bemused")
                ch_e "I don't blame you for your. . . enthusiasm."
                return
            "Maybe later?" if "no_anal" not in EmmaX.daily_history:
                $ EmmaX.change_face("sexy")
                ch_e "I imagine we will. . ."
                ch_e ". . . often."
                $ EmmaX.change_stat("love", 80, 2)
                $ EmmaX.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ EmmaX.recent_history.append("no_taboo")
                    $ EmmaX.daily_history.append("no_taboo")
                $ EmmaX.recent_history.append("no_anal")
                $ EmmaX.daily_history.append("no_anal")
                return
            "I bet it would feel really good. . .":
                if Approval:
                    $ EmmaX.change_face("sexy")
                    $ EmmaX.change_stat("obedience", 90, 2)
                    $ EmmaX.change_stat("obedience", 50, 2)
                    $ EmmaX.change_stat("inhibition", 70, 3)
                    $ EmmaX.change_stat("inhibition", 40, 2)
                    $ Line = renpy.random.choice(["I can't exactly argue with that. . .",     
                                "I suppose. . .", 
                                "You raise a good point. . ."])
                    ch_e "[Line]"
                    $ Line = 0
                    jump Emma_AnalPrep
                else:
                    pass
            "Just deal with it.":

                $ Approval = ApprovalCheck(EmmaX, 1250, "OI", TabM = 3)
                if Approval > 1 or (Approval and EmmaX.Forced):
                    $ EmmaX.change_face("sad")
                    $ EmmaX.change_stat("love", 70, -5, 1)
                    $ EmmaX.change_stat("love", 200, -5)
                    ch_e "Oh, very well, get it over with."
                    $ EmmaX.change_stat("obedience", 80, 4)
                    $ EmmaX.change_stat("inhibition", 80, 1)
                    $ EmmaX.change_stat("inhibition", 60, 3)
                    $ EmmaX.Forced = 1
                    jump Emma_AnalPrep
                else:
                    $ EmmaX.change_stat("love", 200, -20)
                    $ EmmaX.recent_history.append("angry")
                    $ EmmaX.daily_history.append("angry")


    $ EmmaX.ArmPose = 1
    if "no_anal" in EmmaX.daily_history:
        ch_e "Don't question me again."
        $ EmmaX.recent_history.append("angry")
        $ EmmaX.daily_history.append("angry")
    elif EmmaX.Forced:
        $ EmmaX.change_face("angry", 1)
        ch_e "You're really shooting for the fences on that one."
        $ EmmaX.change_stat("lust", 200, 5)
        if EmmaX.love > 300:
            $ EmmaX.change_stat("love", 70, -2)
        $ EmmaX.change_stat("obedience", 50, -2)
        $ EmmaX.recent_history.append("angry")
        $ EmmaX.daily_history.append("angry")
    elif Taboo:

        $ EmmaX.change_face("angry", 1)
        $ EmmaX.recent_history.append("no_taboo")
        $ EmmaX.daily_history.append("no_taboo")
        ch_e "How can you imagine this would be an appropriate location?"
        ch_e "This place, I mean, not anal."
        if ApprovalCheck(EmmaX, 500, "I"):
            ch_e "Anal can be nice, sometimes."
        if not Approval:
            ch_e "Maybe not with you."
        $ EmmaX.change_stat("lust", 200, 5)
        $ EmmaX.change_stat("obedience", 50, -3)
    elif "anal" in EmmaX.daily_history:
        $ EmmaX.change_face("bemused")
        ch_e "Don't wear me out here."
    elif EmmaX.action_counter["anal"]:
        $ EmmaX.change_face("sad")
        ch_e "You'll have to show me you're worth it again."
    else:
        $ EmmaX.change_face("normal", 1)
        ch_e "I don't think you've earned that yet."
    $ EmmaX.recent_history.append("no_anal")
    $ EmmaX.daily_history.append("no_anal")
    $ approval_bonus = 0
    return

label Emma_AnalPrep:
    call Seen_First_Peen (EmmaX, Partner, React=action_context)
    call Emma_Sex_Launch ("hotdog")

    if action_context == EmmaX:

        $ action_context = 0
        if EmmaX.PantsNum() == 5:
            "[EmmaX.name] pushes you back and climbs on top of you, sliding her skirt up as she does so."
            $ EmmaX.Upskirt = 1
        elif EmmaX.PantsNum() >= 6:
            "[EmmaX.name] pushes you down and climbs on top of you, sliding her [EmmaX.legs] down as she does so."
            $ EmmaX.Upskirt = 1
        else:
            "[EmmaX.name] pushes you back and climbs on top of you."
        $ EmmaX.SeenPanties = 1
        "She slides the tip against her ass and seems to want you to insert it."
        menu:
            "What do you do?"
            "Go with it.":
                $ EmmaX.change_stat("inhibition", 80, 3)
                $ EmmaX.change_stat("inhibition", 50, 2)
                "[EmmaX.name] slides it in."
            "Praise her.":
                $ EmmaX.change_face("sexy", 1)
                $ EmmaX.change_stat("inhibition", 80, 3)
                ch_p "Oh yeah, [EmmaX.petname], let's do this."
                $ EmmaX.nameCheck()
                "[EmmaX.name] slides it in."
                $ EmmaX.change_stat("love", 85, 1)
                $ EmmaX.change_stat("obedience", 90, 1)
                $ EmmaX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ EmmaX.change_face("surprised")
                $ EmmaX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [EmmaX.petname]."
                $ EmmaX.nameCheck()
                "[EmmaX.name] pulls back."
                $ EmmaX.change_stat("obedience", 90, 1)
                $ EmmaX.change_stat("obedience", 50, 1)
                $ EmmaX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ EmmaX.AddWord(1,"refused","refused")
                return
        $ EmmaX.underwearDown = 1
        call Emma_First_Bottomless (1)

    elif action_context != "auto":
        call AutoStrip (EmmaX)

        if Taboo:
            "[EmmaX.name] glances around to see if anyone notices what she's doing."
            if "cockout" in Player.recent_history:
                "Then she pushes you back and slowly presses against your rigid member."
            else:
                "Then she pulls down your pants and climbs on top of you."
                "She slowly presses against your rigid member."
            $ EmmaX.inhibition += int(Taboo/10)
            $ EmmaX.lust += int(Taboo/5)
        else:
            if "cockout" in Player.recent_history:
                "[EmmaX.name] pushes you back and slowly presses against your rigid member."
            else:
                "[EmmaX.name] pulls down your pants and climbs on top of you."
                "She slowly presses against your rigid member."
        "She leans back a bit and your cock pops in."
    else:

        if (EmmaX.PantsNum() > 6 and not EmmaX.Upskirt) and (EmmaX.underwear and not EmmaX.underwearDown):
            "You quickly pull down her pants and her [EmmaX.underwear] and press against her back door."
        elif (EmmaX.underwear and not EmmaX.underwearDown):
            "You quickly pull down her [EmmaX.underwear] and press against her back door."
        $ EmmaX.Upskirt = 1
        $ EmmaX.underwearDown = 1
        $ EmmaX.SeenPanties = 1
        call Emma_First_Bottomless (1)

    if not EmmaX.action_counter["anal"]:
        if EmmaX.Forced:
            $ EmmaX.change_stat("love", 90, -150)
            $ EmmaX.change_stat("obedience", 70, 70)
            $ EmmaX.change_stat("inhibition", 80, 40)
        else:
            $ EmmaX.change_stat("love", 90, 10)
            $ EmmaX.change_stat("obedience", 70, 30)
            $ EmmaX.change_stat("inhibition", 80, 70)
    elif not EmmaX.used_to_anal:
        if EmmaX.Forced:
            $ EmmaX.change_stat("love", 90, -20)
            $ EmmaX.change_stat("obedience", 70, 10)
            $ EmmaX.change_stat("inhibition", 80, 5)
        else:
            $ EmmaX.change_stat("obedience", 70, 7)
            $ EmmaX.change_stat("inhibition", 80, 5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    $ Player.Cock = "anal"
    $ primary_action = "anal"
    $ action_speed = 1
    if Taboo:
        $ EmmaX.DrainWord("no_taboo")
    $ EmmaX.DrainWord("no_anal")
    $ EmmaX.recent_history.append("anal")
    $ EmmaX.daily_history.append("anal")

label Emma_Anal_Cycle:
    while Round > 0:
        call shift_focus (EmmaX)
        call Emma_Sex_Launch ("anal")
        $ action_speed = 2 if action_speed >= 4 else action_speed
        $ EmmaX.lust_face()
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

                    call Slap_Ass (EmmaX)
                    $ counter += 1
                    $ Round -= 1
                    jump Emma_Anal_Cycle
                "Turn her Around":

                    $ EmmaX.pose = "doggy" if EmmaX.pose != "doggy" else "sex"
                    "You turn her around. . ."
                    jump Emma_Anal_Cycle

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
                            if EmmaX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ EmmaX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (EmmaX, "tired")
                        "Shift primary action":

                            if EmmaX.remaining_actions and multi_action:
                                menu:
                                    "How about sex?":
                                        $ action_context = "shift"
                                        call Emma_AnalAfter
                                        call Emma_Sex_P
                                    "Just stick it in her pussy [[without asking].":
                                        $ action_context = "auto"
                                        call Emma_AnalAfter
                                        call Emma_Sex_P
                                    "Pull back to hotdog her.":
                                        $ action_context = "pullback"
                                        call Emma_AnalAfter
                                        call Emma_Sex_H
                                    "Never Mind":
                                        jump Emma_Anal_Cycle
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
                                    jump Emma_Anal_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Emma_Anal_Cycle
                                "Never mind":
                                    jump Emma_Anal_Cycle
                        "Just take a look at her.":
                            $ Player.Cock = 0
                            $ action_speed = 0

                        "Show her feet" if not ShowFeet and EmmaX.pose == "doggy":
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and EmmaX.pose == "doggy":
                            $ ShowFeet = 0
                        "Undress [EmmaX.name]":

                            call Girl_Undress (EmmaX)
                        "Clean up [EmmaX.name] (locked)" if not EmmaX.Spunk:
                            pass
                        "Clean up [EmmaX.name]" if EmmaX.Spunk:
                            call Girl_Cleanup (EmmaX, "ask")
                        "Never mind":
                            jump Emma_Anal_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Emma_Sex_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Emma_AnalAfter
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Emma_Sex_Reset
                    $ Line = 0
                    jump Emma_AnalAfter


        call shift_focus (EmmaX)
        call Sex_Dialog (EmmaX, Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or EmmaX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (EmmaX)
                if "angry" in EmmaX.recent_history:
                    call Emma_Sex_Reset
                    return
                $ EmmaX.change_stat("lust", 200, 5)
                if 100 > EmmaX.lust >= 70 and EmmaX.session_orgasms < 2:
                    $ EmmaX.recent_history.append("unsatisfied")
                    $ EmmaX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Emma_AnalAfter
                $ Line = "came"

            if EmmaX.lust >= 100:

                call Girl_Cumming (EmmaX)
                if action_context == "shift" or "angry" in EmmaX.recent_history:
                    jump Emma_AnalAfter

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "She's emptied you out, you'll need to take a break."
                    jump Emma_AnalAfter
                elif "unsatisfied" in EmmaX.recent_history:

                    $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                    "[Line] Keep going?"
                    menu:
                        extend ""
                        "Yes, keep going for a bit." if Player.semen:
                            $ Line = "You get back into it"
                            jump Emma_Anal_Cycle
                        "No, I'm done." if Player.semen:
                            "You pull back."
                            jump Emma_AnalAfter
                        "No, I'm spent." if not Player.semen:
                            "You pull back."
                            jump Emma_AnalAfter
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif counter == (5 + EmmaX.action_counter["anal"]):
            $ EmmaX.brows = "confused"
            ch_e "So are we getting close here?"
        elif counter == (10 + EmmaX.action_counter["anal"]):
            $ EmmaX.brows = "angry"
            ch_e "I'm . . .getting . . a bit. . . tired. . . of this. . ."
            menu:
                ch_e "Can we. . . do something. . . else?"
                "How about a BJ?" if EmmaX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Emma_AnalAfter
                    call Emma_Blowjob
                "How about a Handy?" if EmmaX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Emma_AnalAfter
                    call Emma_Handjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    $ counter += 1
                    jump Emma_Anal_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Emma_Sex_Reset
                    $ action_context = "shift"
                    jump Emma_AnalAfter
                "No, get back down there.":
                    if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):
                        $ EmmaX.change_stat("love", 200, -5)
                        $ EmmaX.change_stat("obedience", 50, 3)
                        $ EmmaX.change_stat("obedience", 80, 2)
                        "She grumbles but keeps moving."
                    else:
                        $ EmmaX.change_face("angry", 1)
                        call Emma_Sex_Reset
                        "She scowls at you and pulls out."
                        ch_e "No, I think not."
                        $ EmmaX.change_stat("love", 50, -3, 1)
                        $ EmmaX.change_stat("love", 80, -4, 1)
                        $ EmmaX.change_stat("obedience", 30, -1, 1)
                        $ EmmaX.change_stat("obedience", 50, -1, 1)
                        $ EmmaX.recent_history.append("angry")
                        $ EmmaX.daily_history.append("angry")
                        jump Emma_AnalAfter


        if Round == 10:
            ch_e "You might want to think about your endgame here. . ."
        elif Round == 5:
            ch_e "We'll need a break soon."


    $ EmmaX.change_face("bemused", 0)
    $ Line = 0
    ch_e "Ok, [EmmaX.player_petname], that's enough of that for now."

label Emma_AnalAfter:
    if not action_context:
        $ Player.Sprite = 0
        $ Player.Cock = "out"
        call Emma_Sex_Reset

    $ EmmaX.change_face("sexy")

    $ EmmaX.action_counter["anal"] += 1
    $ EmmaX.remaining_actions -=1
    $ EmmaX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ EmmaX.addiction_rate += 1
    $ EmmaX.change_stat("inhibition", 30, 3)
    $ EmmaX.change_stat("inhibition", 70, 1)

    if Partner == "Kitty":
        call Partner_Like (EmmaX, 4, 2)
    else:
        call Partner_Like (EmmaX, 3, 2)

    if "Emma Anal Addict" in Achievements:
        pass

    elif EmmaX.action_counter["anal"] >= 10:
        $ EmmaX.SEXP += 7
        $ Achievements.append("Emma Anal Addict")
        if not action_context:
            $ EmmaX.change_face("bemused", 1)
            ch_e "You're one of the better partners I've had at that."
    elif EmmaX.action_counter["anal"] == 1:
        $ EmmaX.SEXP += 25
        if not action_context:
            if EmmaX.love >= 500 and "unsatisfied" not in EmmaX.recent_history:
                ch_e "You really took to that well."
            elif EmmaX.obedience <= 500 and Player.focus <= 20:
                $ EmmaX.mouth = "sad"
                ch_e "Oooh."
                ch_e "It's been a while."
    elif EmmaX.action_counter["anal"] == 5:
        ch_e "You're pretty good at that."
    elif not action_context:
        if "unsatisfied" in EmmaX.recent_history:
            $ EmmaX.change_face("angry")
            $ EmmaX.eyes = "side"
            ch_e "Hmm, you seemed to get more out of that than I did. . ."

    $ approval_bonus = 0


    call Checkout
    return








label Emma_Sex_H:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus (EmmaX)
    if EmmaX.action_counter["hotdog"] >= 3:
        $ approval_bonus += 10
    elif EmmaX.action_counter["hotdog"]:
        $ approval_bonus += 5

    if EmmaX.lust > 85:
        $ approval_bonus += 10
    elif EmmaX.lust > 75:
        $ approval_bonus += 5
    if action_context == "shift":
        $ approval_bonus += 10
    if "exhibitionist" in EmmaX.Traits:
        $ approval_bonus += (3*Taboo)
    if EmmaX in Player.Harem or "sex friend" in EmmaX.player_petnames:
        $ approval_bonus += 10
    elif "ex" in EmmaX.Traits:
        $ approval_bonus -= 40
    if EmmaX.event_counter["forced"] and not EmmaX.Forced:
        $ approval_bonus -= 5*EmmaX.event_counter["forced"]

    if Taboo and "no_taboo" in EmmaX.daily_history:
        $ approval_bonus -= 10

    if "no_hotdog" in EmmaX.daily_history:
        $ approval_bonus -= 5
        $ approval_bonus -= 10 if "no_hotdog" in EmmaX.recent_history else 0

    $ Approval = ApprovalCheck(EmmaX, 1000, TabM = 3)

    if action_context == "auto":
        call Emma_Sex_Launch ("hotdog")
        "You roll back, pulling [EmmaX.name] on top of you, and press your cock against her."
        $ EmmaX.change_face("surprised", 1)

        if (EmmaX.action_counter["hotdog"] and Approval) or (Approval > 1):
            "[EmmaX.name] is briefly startled, but melts into a sly smile."
            $ EmmaX.change_face("sly")
            $ EmmaX.change_stat("obedience", 70, 3)
            $ EmmaX.change_stat("inhibition", 50, 3)
            $ EmmaX.change_stat("inhibition", 70, 1)
            ch_e "Now what shall we do with that . ."
            jump Emma_HotdogPrep
        else:
            $ EmmaX.brows = "angry"
            menu:
                ch_e "You might want to take a step back, [EmmaX.player_petname]?"
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ EmmaX.change_face("sexy", 1)
                        $ EmmaX.change_stat("obedience", 70, 3)
                        $ EmmaX.change_stat("inhibition", 50, 3)
                        $ EmmaX.change_stat("inhibition", 70, 1)
                        ch_e "Or not. . ."
                        jump Emma_HotdogPrep
                    "You pull back from her."
                    $ EmmaX.change_face("bemused", 1)
                    ch_e "You might get better results if you asked first?"
                "You'll see.":
                    $ EmmaX.change_stat("love", 80, -10, 1)
                    $ EmmaX.change_stat("love", 200, -8)
                    "You grind against her crotch."
                    $ EmmaX.change_stat("obedience", 70, 3)
                    $ EmmaX.change_stat("inhibition", 50, 3)
                    if not ApprovalCheck(EmmaX, 500, "O", TabM=1):
                        $ EmmaX.change_face("angry")
                        "[EmmaX.name] shoves you away."
                        ch_e "Don't push your luck, [EmmaX.player_petname]."
                        $ EmmaX.change_stat("love", 50, -10, 1)
                        $ EmmaX.change_stat("obedience", 50, 3)
                        $ renpy.pop_call()
                        if action_context:
                            $ renpy.pop_call()
                        call Emma_Sex_Reset
                        $ EmmaX.recent_history.append("angry")
                        $ EmmaX.daily_history.append("angry")
                    else:
                        $ EmmaX.change_face("sad")
                        "[EmmaX.name] doesn't seem to be into this, but she knows her place."
                        jump Emma_HotdogPrep
        return



    if not EmmaX.action_counter["hotdog"] and "no_hotdog" not in EmmaX.recent_history:

        $ EmmaX.change_face("surprised", 1)
        $ EmmaX.mouth = "kiss"
        ch_e "You just want me to grind against you then?"

        if EmmaX.Forced:
            $ EmmaX.change_face("sad")
            ch_e ". . . nothing more than that?"


    if not EmmaX.action_counter["hotdog"] and Approval:

        if EmmaX.Forced:
            $ EmmaX.change_face("sad")
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
        elif EmmaX.love >= (EmmaX.obedience + EmmaX.inhibition):
            $ EmmaX.change_face("sexy")
            $ EmmaX.brows = "sad"
            $ EmmaX.mouth = "smile"
            ch_e "I wouldn't want to leave you. . . unattended. . ."
        elif EmmaX.obedience >= EmmaX.inhibition:
            $ EmmaX.change_face("normal")
            ch_e "If that's what works for you. . ."
        elif EmmaX.addiction >= 50:
            $ EmmaX.change_face("manic", 1)
            ch_e "Hrmm. . ."
        else:
            $ EmmaX.change_face("sad")
            $ EmmaX.mouth = "smile"
            ch_e "Well if that's what gets you off. . ."

    elif Approval:

        if EmmaX.Forced:
            $ EmmaX.change_face("sad")
            $ EmmaX.change_stat("love", 70, -3, 1)
            $ EmmaX.change_stat("love", 20, -2, 1)
            ch_e "Maybe that's going a bit too far. . ."
        elif not Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "I suppose this is a better location . ."
        elif "hotdog" in EmmaX.recent_history:
            $ EmmaX.change_face("sexy", 1)
            ch_e "Again? Oh, very well."
            jump Emma_HotdogPrep
        elif "hotdog" in EmmaX.daily_history:
            $ EmmaX.change_face("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",                 
                    "So you'd like another round?",                 
                    "You're really into this. . .", 
                    "Are you sure that's all you want?"])
            ch_e "[Line]"
        else:
            $ EmmaX.change_face("sexy", 1)
            $ EmmaX.ArmPose = 2
            $ Line = renpy.random.choice(["Oooh, you want some of this?",                 
                    "So you'd like another round?",                       
                    "You're really into this. . .", 
                    "You want another rub?"])
            ch_e "[Line]"
        $ Line = 0

    if Approval >= 2:

        if EmmaX.Forced:
            $ EmmaX.change_face("sad")
            $ EmmaX.change_stat("obedience", 80, 1)
            $ EmmaX.change_stat("inhibition", 60, 1)
            ch_e "Ok, fine."
        elif "no_hotdog" in EmmaX.daily_history:
            ch_e "It was rather entertaining. . ."
        else:
            $ EmmaX.change_face("sexy", 1)
            $ EmmaX.change_stat("love", 80, 1)
            $ EmmaX.change_stat("inhibition", 50, 2)
            $ Line = renpy.random.choice(["Well, sure, let me give it a rub.",                 
                    "Very well.",                 
                    "Nice!", 
                    "I suppose we could do that.",
                    "Allow me. . .",
                    "Heh, ok, ok."])
            ch_e "[Line]"
            $ Line = 0
        $ EmmaX.change_stat("obedience", 60, 1)
        $ EmmaX.change_stat("inhibition", 70, 2)
        jump Emma_HotdogPrep
    else:


        $ EmmaX.change_face("angry")
        if "no_hotdog" in EmmaX.recent_history:
            ch_e "I'm afraid that \"no\" is my final answer, [EmmaX.player_petname]."
        elif Taboo and "no_taboo" in EmmaX.daily_history and "no_hotdog" in EmmaX.daily_history:
            ch_e "I just told you. . .not in such an exposed location."
        elif "no_hotdog" in EmmaX.daily_history:
            ch_e "I believe I just told you \"no,\" [EmmaX.player_petname]."
        elif Taboo and "no_taboo" in EmmaX.daily_history:
            ch_e "I already told you. . .not in such an exposed location."
        elif not EmmaX.action_counter["hotdog"]:
            $ EmmaX.change_face("bemused")
            ch_e "Hmm, that could be amusing, [EmmaX.player_petname]. . ."
        else:
            $ EmmaX.change_face("bemused")
            ch_e "I don't think that would be appropriate. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no_hotdog" in EmmaX.daily_history:
                $ EmmaX.change_face("bemused")
                ch_e "No harm in asking. Once."
                return
            "Maybe later?" if "no_hotdog" not in EmmaX.daily_history:
                $ EmmaX.change_face("sexy")
                ch_e "I imagine it will happen at some point, [EmmaX.player_petname]."
                $ EmmaX.change_stat("love", 80, 1)
                $ EmmaX.change_stat("inhibition", 50, 1)
                if Taboo:
                    $ EmmaX.recent_history.append("no_taboo")
                    $ EmmaX.daily_history.append("no_taboo")
                $ EmmaX.recent_history.append("no_hotdog")
                $ EmmaX.daily_history.append("no_hotdog")
                return
            "You might like it. . .":
                if Approval:
                    $ EmmaX.change_face("sexy")
                    $ EmmaX.change_stat("obedience", 60, 2)
                    $ EmmaX.change_stat("inhibition", 50, 2)
                    $ Line = renpy.random.choice(["I can't exactly argue with that. . .",     
                                "I suppose. . .", 
                                "You raise a good point. . ."])
                    ch_e "[Line]"
                    $ Line = 0
                    jump Emma_HotdogPrep
                else:
                    pass
            "Just deal with it.":

                $ Approval = ApprovalCheck(EmmaX, 350, "OI", TabM = 3)
                if Approval > 1 or (Approval and EmmaX.Forced):
                    $ EmmaX.change_face("sad")
                    $ EmmaX.change_stat("love", 70, -2, 1)
                    $ EmmaX.change_stat("love", 200, -2)
                    ch_e "Alright, fine. Lay back."
                    $ EmmaX.change_stat("obedience", 80, 4)
                    $ EmmaX.change_stat("inhibition", 60, 2)
                    $ EmmaX.Forced = 1
                    jump Emma_HotdogPrep
                else:
                    $ EmmaX.change_stat("love", 200, -10)
                    $ EmmaX.recent_history.append("angry")
                    $ EmmaX.daily_history.append("angry")


    $ EmmaX.ArmPose = 1

    if "no_hotdog" in EmmaX.daily_history:
        ch_e "I've made myself clear."
        $ EmmaX.recent_history.append("angry")
        $ EmmaX.daily_history.append("angry")
    if EmmaX.Forced:
        $ EmmaX.change_face("angry", 1)
        ch_e "I just don't see the benefit."
        $ EmmaX.change_stat("lust", 200, 5)
        if EmmaX.love > 300:
            $ EmmaX.change_stat("love", 70, -1)
        $ EmmaX.change_stat("obedience", 50, -1)
        $ EmmaX.recent_history.append("angry")
        $ EmmaX.daily_history.append("angry")
    elif Taboo:
        $ EmmaX.change_face("angry", 1)
        $ EmmaX.recent_history.append("no_taboo")
        $ EmmaX.daily_history.append("no_taboo")
        ch_e "This area is a bit too exposed for that sort of thing. . ."
        $ EmmaX.change_stat("lust", 200, 5)
        $ EmmaX.change_stat("obedience", 50, -3)
    elif EmmaX.action_counter["hotdog"]:
        $ EmmaX.change_face("sad")
        ch_e "Not under the circumstances."
    else:
        $ EmmaX.change_face("normal", 1)
        ch_e "No, thank you."
    $ EmmaX.recent_history.append("no_hotdog")
    $ EmmaX.daily_history.append("no_hotdog")
    $ approval_bonus = 0
    return

label Emma_HotdogPrep:
    call Seen_First_Peen (EmmaX, Partner, React=action_context)
    call Emma_Sex_Launch ("hotdog")


    if action_context == EmmaX:

        $ action_context = 0
        "[EmmaX.name] pushes you back and climbs on top of you, sliding back and forth along your shaft."
        menu:
            "What do you do?"
            "Go with it.":
                $ EmmaX.change_stat("inhibition", 80, 3)
                $ EmmaX.change_stat("inhibition", 50, 2)
                "[EmmaX.name] starts to grind against you."
            "Praise her.":
                $ EmmaX.change_face("sexy", 1)
                $ EmmaX.change_stat("inhibition", 80, 3)
                ch_p "Oh yeah, [EmmaX.petname], let's do this."
                $ EmmaX.nameCheck()
                "[EmmaX.name] starts to grind against you."
                $ EmmaX.change_stat("love", 85, 1)
                $ EmmaX.change_stat("obedience", 90, 1)
                $ EmmaX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                $ EmmaX.change_face("surprised")
                $ EmmaX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [EmmaX.petname]."
                $ EmmaX.nameCheck()
                "[EmmaX.name] pulls back."
                $ EmmaX.change_stat("obedience", 90, 1)
                $ EmmaX.change_stat("obedience", 50, 1)
                $ EmmaX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ EmmaX.AddWord(1,"refused","refused")
                return

    elif action_context != "auto":


        if Taboo:
            "[EmmaX.name] glances around to see if anyone notices what she's doing."
            if "cockout" in Player.recent_history:
                "Then she pushes you back and slowly presses against your rigid member."
            else:
                "Then she pulls down your pants and climbs on top of you."
                "She slowly presses against your rigid member."
            $ EmmaX.inhibition += int(Taboo/10)
            $ EmmaX.lust += int(Taboo/5)
        else:
            if "cockout" in Player.recent_history:
                "[EmmaX.name] pushes you back and slowly presses against your rigid member."
            else:
                "[EmmaX.name] pulls down your pants and climbs on top of you."
                "She slowly presses against your rigid member."
    else:

        "You roll back, pulling her on top of you and your rigid member."

    if not EmmaX.action_counter["hotdog"]:
        if EmmaX.Forced:
            $ EmmaX.change_stat("love", 90, -5)
            $ EmmaX.change_stat("obedience", 70, 20)
            $ EmmaX.change_stat("inhibition", 80, 10)
        else:
            $ EmmaX.change_stat("love", 90, 20)
            $ EmmaX.change_stat("obedience", 70, 20)
            $ EmmaX.change_stat("inhibition", 80, 20)


    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ Line = 0
    $ counter = 0
    $ primary_action = "hotdog"
    $ action_speed = 1
    if Taboo:
        $ EmmaX.DrainWord("no_taboo")
    $ EmmaX.DrainWord("no_hotdog")
    $ EmmaX.recent_history.append("hotdog")
    $ EmmaX.daily_history.append("hotdog")

label Emma_Hotdog_Cycle:
    while Round > 0:
        call shift_focus (EmmaX)
        call Emma_Sex_Launch ("hotdog")
        $ action_speed = 2 if action_speed >= 4 else action_speed
        $ EmmaX.lust_face()
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

                    call Slap_Ass (EmmaX)
                    $ counter += 1
                    $ Round -= 1
                    jump Emma_Hotdog_Cycle
                "Turn her Around":

                    $ EmmaX.pose = "doggy" if EmmaX.pose != "doggy" else "sex"
                    "You turn her around. . ."
                    jump Emma_Hotdog_Cycle

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
                            if EmmaX.remaining_actions and multi_action:
                                call Offhand_Set
                                if offhand_action:
                                    $ EmmaX.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (EmmaX, "tired")
                        "Shift primary action":

                            if EmmaX.remaining_actions and multi_action:
                                menu:
                                    "How about sex?":
                                        $ action_context = "shift"
                                        call Emma_HotdogAfter
                                        call Emma_Sex_P
                                    "Just stick it in her pussy [[without asking].":
                                        $ action_context = "auto"
                                        call Emma_HotdogAfter
                                        call Emma_Sex_P
                                    "How about anal?":
                                        $ action_context = "shift"
                                        call Emma_HotdogAfter
                                        call Emma_Sex_A
                                    "Just stick it in her ass [[without asking].":
                                        $ action_context = "auto"
                                        call Emma_HotdogAfter
                                        call Emma_Sex_A
                                    "Never Mind":
                                        jump Emma_Hotdog_Cycle
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
                                    jump Emma_Hotdog_Cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup (Partner, "ask")
                                    jump Emma_Hotdog_Cycle
                                "Never mind":
                                    jump Emma_Hotdog_Cycle
                        "Just take a look at her.":
                            $ Player.Cock = 0
                            $ action_speed = 0

                        "Show her feet" if not ShowFeet and EmmaX.pose == "doggy":
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and EmmaX.pose == "doggy":
                            $ ShowFeet = 0
                        "Undress [EmmaX.name]":

                            call Girl_Undress (EmmaX)
                        "Clean up [EmmaX.name] (locked)" if not EmmaX.Spunk:
                            pass
                        "Clean up [EmmaX.name]" if EmmaX.Spunk:
                            call Girl_Cleanup (EmmaX, "ask")
                        "Never mind":
                            jump Emma_Hotdog_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    call Emma_Sex_Reset
                    $ action_context = "shift"
                    $ Line = 0
                    jump Emma_HotdogAfter
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    call Emma_Sex_Reset
                    $ Line = 0
                    jump Emma_HotdogAfter


        call shift_focus (EmmaX)
        call Sex_Dialog (EmmaX, Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus
        if Player.focus >= 100 or EmmaX.lust >= 100:

            if Player.focus >= 100:

                call Player_Cumming (EmmaX)
                if "angry" in EmmaX.recent_history:
                    call Emma_Sex_Reset
                    return
                $ EmmaX.change_stat("lust", 200, 5)
                if 100 > EmmaX.lust >= 70 and EmmaX.session_orgasms < 2:
                    $ EmmaX.recent_history.append("unsatisfied")
                    $ EmmaX.daily_history.append("unsatisfied")

                if Player.focus > 80:
                    jump Emma_HotdogAfter
                $ Line = "came"

            if EmmaX.lust >= 100:

                call Girl_Cumming (EmmaX)
                if action_context == "shift" or "angry" in EmmaX.recent_history:
                    jump Emma_HotdogAfter

            if Line == "came":

                $ Line = 0
                if not Player.semen:
                    "She's emptied you out, you'll need to take a break."
                    jump Emma_HotdogAfter
                elif "unsatisfied" in EmmaX.recent_history:

                    $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                    "[Line] Keep going?"
                    menu:
                        extend ""
                        "Yes, keep going for a bit." if Player.semen:
                            $ Line = "You get back into it"
                            jump Emma_Hotdog_Cycle
                        "No, I'm done." if Player.semen:
                            "You pull back."
                            jump Emma_HotdogAfter
                        "No, I'm spent." if not Player.semen:
                            "You pull back."
                            jump Emma_HotdogAfter
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)


        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif counter == (5 + EmmaX.action_counter["hotdog"]):
            $ EmmaX.brows = "confused"
            ch_e "Are we getting close here?"
        elif counter == (10 + EmmaX.action_counter["hotdog"]):
            $ EmmaX.brows = "angry"
            menu:
                ch_e "I'm a bit bored by this."
                "How about a BJ?" if EmmaX.remaining_actions and multi_action:
                    $ action_context = "shift"
                    call Emma_HotdogAfter
                    call Emma_Blowjob
                "Finish up." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                    $ Player.focus += 15
                    $ counter += 1
                    jump Emma_Hotdog_Cycle
                "Let's try something else." if multi_action:
                    $ Line = 0
                    call Emma_Sex_Reset
                    $ action_context = "shift"
                    jump Emma_HotdogAfter
                "No, get back down there.":
                    if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 500, "O"):
                        $ EmmaX.change_stat("love", 200, -5)
                        $ EmmaX.change_stat("obedience", 50, 3)
                        $ EmmaX.change_stat("obedience", 80, 2)
                        "She grumbles but keeps moving."
                    else:
                        $ EmmaX.change_face("angry", 1)
                        call Emma_Sex_Reset
                        "She scowls at you and pulls away."
                        ch_e "No, I think not."
                        $ EmmaX.change_stat("love", 50, -3, 1)
                        $ EmmaX.change_stat("love", 80, -4, 1)
                        $ EmmaX.change_stat("obedience", 30, -1, 1)
                        $ EmmaX.change_stat("obedience", 50, -1, 1)
                        $ EmmaX.recent_history.append("angry")
                        $ EmmaX.daily_history.append("angry")
                        jump Emma_HotdogAfter


        call Escalation (EmmaX)

        if Round == 10:
            ch_e "You might want to think about your endgame here. . ."
        elif Round == 5:
            ch_e "We'll need a break soon."


    $ EmmaX.change_face("bemused", 0)
    $ Line = 0
    ch_e "Ok, [EmmaX.player_petname], that's enough of that for now."

label Emma_HotdogAfter:
    if not action_context:
        $ Player.Sprite = 0
        $ Player.Cock = "out"
        call Emma_Sex_Reset

    $ EmmaX.change_face("sexy")

    $ EmmaX.action_counter["hotdog"] += 1
    $ EmmaX.remaining_actions -=1
    $ EmmaX.addiction_rate += 1
    if "addictive" in Player.Traits:
        $ EmmaX.addiction_rate += 1
    $ EmmaX.change_stat("inhibition", 30, 1)
    $ EmmaX.change_stat("inhibition", 70, 1)

    call Partner_Like (EmmaX, 2)

    if EmmaX.action_counter["hotdog"] == 10:
        $ EmmaX.SEXP += 5
    elif EmmaX.action_counter["hotdog"] == 1:
        $ EmmaX.SEXP += 10
        if not action_context:
            if EmmaX.love >= 500 and "unsatisfied" not in EmmaX.recent_history:
                ch_e "That was. . . pleasant."
            elif EmmaX.obedience <= 500 and Player.focus <= 20:
                $ EmmaX.mouth = "sad"
                ch_e "Was that enough for you?"
    elif not action_context:
        if "unsatisfied" in EmmaX.recent_history:
            $ EmmaX.change_face("angry")
            $ EmmaX.eyes = "side"
            ch_e "I'm afraid that didn't do much for me. . ."

    $ approval_bonus = 0


    call Checkout
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
