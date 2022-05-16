
label Rogue_Fondle:
    $ RogueX.mouth = "smile"
    if not RogueX.remaining_actions:
        ch_r "I'm a bit worn out right now, [RogueX.player_petname], maybe later."
        return
    menu:
        ch_r "Well where exactly were you interested in touching, [RogueX.player_petname]?"
        "Your breasts?" if RogueX.remaining_actions:
            jump Rogue_Fondle_Breasts
        "Suck your breasts?" if RogueX.remaining_actions and RogueX.action_counter["suck_breasts"]:
            jump Rogue_Suck_Breasts
        "Your thighs?" if RogueX.remaining_actions:
            jump Rogue_Fondle_Thighs
        "Your pussy?" if RogueX.remaining_actions:
            jump Rogue_Fondle_Pussy
        "Lick your pussy?" if RogueX.remaining_actions and RogueX.action_counter["eat_pussy"]:
            jump Rogue_Lick_Pussy
        "Your Ass?" if RogueX.remaining_actions:
            jump Rogue_Fondle_Ass
        "Never mind.":
            return
    return

label Rogue_FB_Prep:
    if primary_action == "kiss":
        $ primary_action = "fondle_breasts"
        return


    call Rogue_Breasts_Launch ("fondle_breasts")

    if action_context == RogueX:

        $ action_context = 0
        if (RogueX.top or RogueX.bra) and not RogueX.Uptop:

            if approval_check(RogueX, 1250, TabM = 1) or (RogueX.SeenChest and approval_check(RogueX, 500) and not Taboo):
                $ RogueX.Uptop = 1
                $ Line = RogueX.top if RogueX.top else RogueX.bra
                "With a miscevious grin, [RogueX.name] pulls her [Line] up over her breasts."
                call Rogue_First_Topless (1)
                $ Line = 0
                "She then grabs your arm and shoves your hand against her breast, clearly intending you to get to work."
            else:
                "[RogueX.name] grabs your arm and shoves your hand against her covered breast, clearly intending you to get to work."
        else:
            "[RogueX.name] grabs your arm and shoves your hand against her breast, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ RogueX.change_stat("inhibition", 80, 3)
                $ RogueX.change_stat("inhibition", 50, 2)
                "You start to fondle it."
            "Praise her.":
                $ RogueX.change_face("sexy", 1)
                $ RogueX.change_stat("inhibition", 80, 3)
                ch_p "I like the initiative, [RogueX.petname]."
                $ RogueX.nameCheck()
                "You start to fondle it."
                $ RogueX.change_stat("love", 85, 1)
                $ RogueX.change_stat("obedience", 90, 1)
                $ RogueX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your hand back."
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


    if not RogueX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Top_Off (RogueX)
        if "angry" in RogueX.recent_history:
            return

    $ approval_bonus = 0
    if not RogueX.action_counter["fondle_breasts"]:
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -20)
            $ RogueX.change_stat("obedience", 70, 25)
            $ RogueX.change_stat("inhibition", 80, 15)
        else:
            $ RogueX.change_stat("love", 90, 10)
            $ RogueX.change_stat("obedience", 70, 5)
            $ RogueX.change_stat("inhibition", 80, 15)



label Rogue_SB_Prep:


    call Rogue_Breasts_Launch ("suck_breasts")

    if action_context == RogueX:

        $ action_context = 0
        if (RogueX.top or RogueX.bra) and not RogueX.Uptop:

            if approval_check(RogueX, 1250, TabM = 1) or (RogueX.SeenChest and approval_check(RogueX, 500) and not Taboo):
                $ RogueX.Uptop = 1
                $ Line = RogueX.top if RogueX.top else RogueX.bra
                "With a miscevious grin, [RogueX.name] pulls her [Line] up over her breasts."
                call Rogue_First_Topless (1)
                $ Line = 0
                "She then grabs your head and shoves your face into her chest, clearly intending you to get to work."
            else:
                "[RogueX.name] grabs your head and shoves your face into her chest, clearly intending you to get to work."
        else:
            "[RogueX.name] grabs your head and shoves your face into her chest, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ RogueX.change_stat("inhibition", 80, 3)
                $ RogueX.change_stat("inhibition", 50, 2)
                "You start to run your tongue along her nipple."
            "Praise her.":
                $ RogueX.change_face("sexy", 1)
                $ RogueX.change_stat("inhibition", 80, 3)
                ch_p "Mmm, I like this, [RogueX.petname]."
                $ RogueX.nameCheck()
                "You start to fondle it."
                $ RogueX.change_stat("love", 85, 1)
                $ RogueX.change_stat("obedience", 90, 1)
                $ RogueX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your head back."
                $ RogueX.change_face("surprised")
                $ RogueX.change_stat("inhibition", 70, 1)
                ch_p "Let's not do that right now, [RogueX.petname]."
                $ RogueX.nameCheck()
                "[RogueX.name] pulls away."
                $ RogueX.change_stat("obedience", 90, 1)
                $ RogueX.change_stat("obedience", 50, 1)
                $ RogueX.change_stat("obedience", 30, 2)
                $ Player.recent_history.append("nope")
                $ RogueX.AddWord(1,"refused","refused")
                return


    if not RogueX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Top_Off (RogueX)
        if "angry" in RogueX.recent_history:
            return

    $ approval_bonus = 0
    if not RogueX.action_counter["suck_breasts"]:
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -25)
            $ RogueX.change_stat("obedience", 70, 25)
            $ RogueX.change_stat("inhibition", 80, 17)
        else:
            $ RogueX.change_stat("love", 90, 10)
            $ RogueX.change_stat("obedience", 70, 10)
            $ RogueX.change_stat("inhibition", 80, 15)



label Rogue_FT_Prep:
    if primary_action == "kiss":
        $ primary_action = "fondle_thighs"
        return

    if not RogueX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (RogueX)
        if "angry" in RogueX.recent_history:
            return

    $ approval_bonus = 0
    call Rogue_Pussy_Launch ("fondle_thighs")
    if not RogueX.action_counter["fondle_thighs"]:
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -10)
            $ RogueX.change_stat("obedience", 70, 15)
            $ RogueX.change_stat("inhibition", 80, 10)
        else:
            $ RogueX.change_stat("love", 90, 5)
            $ RogueX.change_stat("obedience", 70, 10)
            $ RogueX.change_stat("inhibition", 80, 15)





label Rogue_FP_Prep:

    call Rogue_Pussy_Launch ("fondle_pussy")

    if action_context == RogueX:

        $ action_context = 0
        if (RogueX.legs and not RogueX.Upskirt) or (RogueX.underwear and not RogueX.underwearDown):

            if approval_check(RogueX, 1250, TabM = 1) or (RogueX.SeenPussy and approval_check(RogueX, 500) and not Taboo):
                $ RogueX.Upskirt = 1
                $ RogueX.underwearDown = 1
                $ Line = 0
                if RogueX.PantsNum() == 5:
                    $ Line = RogueX.name+" hikes up her_skirt"
                elif RogueX.PantsNum() > 6:
                    $ Line = RogueX.name+" pulls down her " + RogueX.legs
                else:
                    $ Line = 0
                if RogueX.underwear:
                    if Line:

                        "[Line] and pulls her [RogueX.underwear] out of the way."
                        "She then grabs your arm and shoves your hand into her crotch, clearly intending you to get to work."
                    else:

                        "She pulls her [RogueX.underwear] out of the way, and then shoves your hand into her crotch."
                        "She clearly intends for you to get to work."
                else:

                    "[Line], and then shoves your hand into her crotch."
                    "She clearly intends for you to get to work."
                call Rogue_First_Bottomless (1)
            else:
                "[RogueX.name] grabs your arm and shoves your hand into her crotch, clearly intending you to get to work."
        else:
            "[RogueX.name] grabs your arm and shoves your hand into her crotch, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ RogueX.change_stat("inhibition", 80, 3)
                $ RogueX.change_stat("inhibition", 50, 2)
                "You start to run your fingers along her pussy."
            "Praise her.":
                $ RogueX.change_face("sexy", 1)
                $ RogueX.change_stat("inhibition", 80, 3)
                ch_p "I like the initiative, [RogueX.petname]."
                $ RogueX.nameCheck()
                "You start to run your fingers along her pussy."
                $ RogueX.change_stat("love", 85, 1)
                $ RogueX.change_stat("obedience", 90, 1)
                $ RogueX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your hand back."
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


    if not RogueX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (RogueX)
        if "angry" in RogueX.recent_history:
            return
    $ approval_bonus = 0
    if not RogueX.action_counter["fondle_pussy"]:
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -50)
            $ RogueX.change_stat("obedience", 70, 35)
            $ RogueX.change_stat("inhibition", 80, 25)
        else:
            $ RogueX.change_stat("love", 90, 10)
            $ RogueX.change_stat("obedience", 70, 10)
            $ RogueX.change_stat("inhibition", 80, 15)





label Rogue_Insert_Pussy:
    call shift_focus (RogueX)
    if action_context == "auto":
        if approval_check(RogueX, 1100, TabM = 2):
            $ RogueX.change_face("surprised")
            $ RogueX.change_stat("obedience", 90, 1)
            $ RogueX.change_stat("obedience", 70, 2)
            $ RogueX.change_stat("inhibition", 70, 3)
            $ RogueX.change_stat("inhibition", 30, 2)
            "As you slide a finger in, [RogueX.name] seems a bit surprised, but seems into it."
            jump Rogue_IP_Prep
        else:
            $ RogueX.change_face("surprised")
            $ RogueX.change_stat("love", 80, -2)
            $ RogueX.change_stat("obedience", 50, -3)
            ch_r "Keep it outside, [RogueX.player_petname]."
            return

    if approval_check(RogueX, 1100, TabM = 2):
        if RogueX.Forced:
            $ RogueX.change_face("sad")
            $ RogueX.change_stat("love", 70, -3, 1)
            $ RogueX.change_stat("love", 20, -2, 1)
            $ RogueX.change_stat("obedience", 90, 1)
            $ RogueX.change_stat("inhibition", 60, 1)
            ch_r "Sure, get in there."
        else:
            $ RogueX.change_face("sexy", 1)
            $ RogueX.change_stat("love", 90, 1)
            $ RogueX.change_stat("inhibition", 50, 3)
            ch_r "God yes."
        $ RogueX.change_stat("obedience", 20, 1)
        $ RogueX.change_stat("obedience", 60, 1)
        $ RogueX.change_stat("inhibition", 70, 2)
        jump Rogue_IP_Prep
    else:

        $ RogueX.change_face("bemused", 2)
        ch_r "Um, no thanks, [RogueX.player_petname]."
        $ RogueX.blushing = 1
    return


label Rogue_IP_Prep:
    if not RogueX.action_counter["finger_pussy"]:
        $ RogueX.action_counter["finger_pussy"] = 1
        $ RogueX.SEXP += 10
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -60)
            $ RogueX.change_stat("obedience", 70, 55)
            $ RogueX.change_stat("inhibition", 80, 35)
        else:
            $ RogueX.change_stat("love", 90, 10)
            $ RogueX.change_stat("obedience", 70, 20)
            $ RogueX.change_stat("inhibition", 80, 25)

    if not RogueX.Forced and action_context != "auto":
        call Girl_Undress (RogueX, "bottom")
        if "angry" in RogueX.recent_history:
            return

    if Taboo:
        $ RogueX.inhibition += int(Taboo/10)
        $ RogueX.lust += int(Taboo/5)

    $ Line = 0
    $ action_speed = 2
    return



label Rogue_LP_Prep:

    call Rogue_Pussy_Launch ("eat_pussy")


    if action_context == RogueX:

        $ action_context = 0
        if (RogueX.legs and not RogueX.Upskirt) or (RogueX.underwear and not RogueX.underwearDown):

            if approval_check(RogueX, 1250, TabM = 1) or (RogueX.SeenPussy and approval_check(RogueX, 500) and not Taboo):
                $ RogueX.Upskirt = 1
                $ RogueX.underwearDown = 1
                $ Line = 0
                if RogueX.PantsNum() == 5:
                    $ Line = RogueX.name+" hikes up her_skirt"
                elif RogueX.PantsNum() > 6:
                    $ Line = RogueX.name+" pulls down her " + RogueX.legs
                else:
                    $ Line = 0
                if RogueX.underwear:
                    if Line:

                        "[Line] and pulls her [RogueX.underwear] out of the way."
                        "She then grabs your head and pulls it to her crotch, clearly intending you to get to work."
                    else:

                        "She pulls her [RogueX.underwear] out of the way, and then shoves your face into her crotch."
                        "She clearly intends for you to get to work."
                else:

                    "[Line], and then shoves your face into her crotch."
                    "She clearly intends for you to get to work."
                call Rogue_First_Bottomless (1)
            else:
                "[RogueX.name] grabs your head and pulls it to her crotch, clearly intending you to get to work."
        else:
            "[RogueX.name] grabs your head and pulls it to her crotch, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ RogueX.change_stat("inhibition", 80, 3)
                $ RogueX.change_stat("inhibition", 50, 2)
                "You start licking."
            "Praise her.":
                $ RogueX.change_face("sexy", 1)
                $ RogueX.change_stat("inhibition", 80, 3)
                ch_p "Mmm, I like this idea, [RogueX.petname]."
                $ RogueX.nameCheck()
                "You start licking."
                $ RogueX.change_stat("love", 85, 1)
                $ RogueX.change_stat("obedience", 90, 1)
                $ RogueX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your head away."
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


    if not RogueX.Forced and action_context != "auto":
        $ approval_bonus = 0
        if RogueX.PantsNum() >= 6:
            $ approval_bonus = 15
        call Bottoms_Off (RogueX)
        if "angry" in RogueX.recent_history:
            return

    $ approval_bonus = 0
    if not RogueX.action_counter["eat_pussy"]:
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -30)
            $ RogueX.change_stat("obedience", 70, 35)
            $ RogueX.change_stat("inhibition", 80, 75)
        else:
            $ RogueX.change_stat("love", 90, 35)
            $ RogueX.change_stat("obedience", 70, 15)
            $ RogueX.change_stat("inhibition", 80, 35)






label Rogue_FA_Prep:


    call Rogue_Pussy_Launch ("fondle_ass")
    if not RogueX.action_counter["fondle_ass"]:
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -20)
            $ RogueX.change_stat("obedience", 70, 20)
            $ RogueX.change_stat("inhibition", 80, 15)
        else:
            $ RogueX.change_stat("love", 90, 10)
            $ RogueX.change_stat("obedience", 70, 12)
            $ RogueX.change_stat("inhibition", 80, 20)




label Rogue_IA_Prep:

    call Rogue_Pussy_Launch ("finger_ass")

    if action_context == RogueX:

        $ action_context = 0
        if (RogueX.legs and not RogueX.Upskirt) or (RogueX.underwear and not RogueX.underwearDown):

            if approval_check(RogueX, 1250, TabM = 1) or (RogueX.SeenPussy and approval_check(RogueX, 500) and not Taboo):
                $ RogueX.Upskirt = 1
                $ RogueX.underwearDown = 1
                $ Line = 0
                if RogueX.PantsNum() == 5:
                    $ Line = RogueX.name+" hikes up her_skirt"
                elif RogueX.PantsNum() > 6:
                    $ Line = RogueX.name+" pulls down her " + RogueX.legs
                else:
                    $ Line = 0
                if RogueX.underwear:
                    if Line:

                        "[Line] and pulls her [RogueX.underwear] out of the way."
                        "She then grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
                    else:

                        "She pulls her [RogueX.underwear] out of the way, and then presses your hand against her asshole."
                        "She clearly intends for you to get to work."
                else:

                    "[Line], and then presses your hand against her asshole."
                    "She clearly intends for you to get to work."
                call Rogue_First_Bottomless (1)
            else:
                "[RogueX.name] grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
        else:
            "[RogueX.name] grabs your arm and presses your hand against her asshole, clearly intending you to get to work."
        menu:
            "What do you do?"
            "Get to work.":
                $ RogueX.change_stat("inhibition", 80, 3)
                $ RogueX.change_stat("inhibition", 50, 2)
                "You press your finger into it."
            "Praise her.":
                $ RogueX.change_face("sexy", 1)
                $ RogueX.change_stat("inhibition", 80, 3)
                ch_p "Dirty girl, [RogueX.petname]."
                $ RogueX.nameCheck()
                "You press your finger into it."
                $ RogueX.change_stat("love", 85, 1)
                $ RogueX.change_stat("obedience", 90, 1)
                $ RogueX.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                "You pull your hand back."
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


    if not RogueX.Forced and action_context != "auto":
        $ approval_bonus = 0
        call Bottoms_Off (RogueX)
        if "angry" in RogueX.recent_history:
            return

    $ approval_bonus = 0
    if not RogueX.action_counter["finger_ass"]:
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -50)
            $ RogueX.change_stat("obedience", 70, 60)
            $ RogueX.change_stat("inhibition", 80, 35)
        else:
            $ RogueX.change_stat("love", 90, 10)
            $ RogueX.change_stat("obedience", 70, 20)
            $ RogueX.change_stat("inhibition", 80, 25)





label Rogue_LA_Prep:

    if not RogueX.Forced and action_context != "auto":
        $ approval_bonus = 0
        if RogueX.PantsNum() >= 6:
            $ approval_bonus = 15
        call Bottoms_Off (RogueX)
        if "angry" in RogueX.recent_history:
            return
    $ approval_bonus = 0
    call Rogue_Pussy_Launch ("eat_ass")
    if not RogueX.action_counter["eat_ass"]:
        if RogueX.Forced:
            $ RogueX.change_stat("love", 90, -30)
            $ RogueX.change_stat("obedience", 70, 40)
            $ RogueX.change_stat("inhibition", 80, 80)
        else:
            $ RogueX.change_stat("love", 90, 35)
            $ RogueX.change_stat("obedience", 70, 25)
            $ RogueX.change_stat("inhibition", 80, 55)
