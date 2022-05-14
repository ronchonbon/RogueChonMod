# Storm_SexMenu //////////////////////////////////////////////////////////////////////
label Storm_SexAct(Act = 0):
        if AloneCheck(StormX) and StormX.Taboo == 20:
                $ StormX.Taboo = 0
                $ Taboo = 0
        call Shift_Focus(StormX)
        if Act == "SkipTo":
            $ renpy.pop_call() #causes it to skip past the primary_action Swap
            $ renpy.pop_call() #causes it to skip past the cycle you were in before
            #$ renpy.pop_call() #causes it to skip past the sex menu you were in before that
            call SkipTo(StormX)
        elif Act == "switch":
            $ renpy.pop_call() #causes it to skip past call here from Sex_Menu_Threesome
            #$ renpy.pop_call() #causes it to skip past call to Sex_Menu_Threesome
            # drops through to sex menu
        elif Act == "masturbate":
            call Storm_M_Prep
            if not action_context:
                return
        elif Act == "lesbian":
            call Les_Prep(StormX)
            if not action_context:
                return
        elif Act == "kissing":
            call KissPrep(StormX)
            if not action_context:
                return
        elif Act == "breasts":
            call Storm_Fondle_Breasts
            if not action_context:
                return
        elif Act == "blow":
            call Storm_BJ_Prep
            if not action_context:
                return
        elif Act == "hand":
            call Storm_HJ_Prep
            if not action_context:
                return
        elif Act == "sex":
            call Storm_SexPrep
            if not action_context:
                return

##  StormX.Masturbating //////////////////////////////////////////////////////////////////////
# counter 1 means she's seen you, counter 0 means she hasn't.
label Storm_Masturbate: #(action_context = action_context):
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(StormX)
    if StormX.Mast:
        $ temp_modifier += 10
    if StormX.SEXP >= 50:
        $ temp_modifier += 25
    elif StormX.SEXP >= 30:
        $ temp_modifier += 15
    elif StormX.SEXP >= 15:
        $ temp_modifier += 5
    if StormX.lust >= 90:
        $ temp_modifier += 20
    elif StormX.lust >= 75:
        $ temp_modifier += 5
    if "exhibitionist" in StormX.Traits:
        $ temp_modifier += (3*Taboo)
    if StormX in Player.Harem or "sex friend" in StormX.Petnames:
        $ temp_modifier += 10
    elif "ex" in StormX.Traits:
        $ temp_modifier -= 40
    if StormX.ForcedCount and not StormX.Forced:
        $ temp_modifier -= 5 * StormX.ForcedCount

    $ Approval = ApprovalCheck(StormX, 1300, TabM = 2) # 120, 135, 150, Taboo -80(200)

    $ StormX.DrainWord("unseen",1,0) #She sees you, so remove unseens

    if action_context == "join":       # This triggers if you ask to join in
                if Approval > 1 or (Approval and StormX.lust >= 50):
                    $ Player.AddWord(1,"join")
                    menu:
                        extend ""
                        "Would you like some help? I could lend some helping hands. . ."  if Player.Semen and StormX.Action:
                                $ StormX.change_stat("love", 90, 1)
                                $ StormX.change_stat("obedience", 50, 2)
                                $ StormX.change_face("sexy")
                                ch_s "You could give me a breast massage. . ."
                                $ StormX.change_stat("obedience", 70, 2)
                                $ StormX.change_stat("inhibition", 70, 1)
                                $ offhand_action = "fondle breasts"
                                $ StormX.Mast += 1
                                jump Storm_M_Cycle
                        "Would you like some help? I could. . . up to you, I guess." if Player.Semen and StormX.Action:
                                $ StormX.change_stat("love", 70, 2)
                                $ StormX.change_stat("love", 90, 1)
                                $ StormX.change_face("sexy")
                                ch_s "You could give me a breast massage. . ."
                                $ StormX.change_stat("obedience", 70, 2)
                                $ StormX.change_stat("inhibition", 70, 1)
                                $ D20 = renpy.random.randint(1, 20)
                                if D20 > 10:
                                    $ offhand_action = "fondle breasts"
                                else:
                                    $ offhand_action = "suck breasts"
                                $ StormX.Mast += 1
                                jump Storm_M_Cycle
                        "Why don't we take care of each other?" if Player.Semen and StormX.Action:
                                $ StormX.change_face("sexy")
                                ch_s "Oh, what did you have in mind?"
                                $ renpy.pop_call()          #removes the call to this label
                                return                      #returns to sexmenu=
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

                #else: You've failed all checks so she kicks you out.
                $ StormX.ArmPose = 1
                $ StormX.OutfitChange()
                $ StormX.Action -= 1
                $ Player.change_stat("Focus", 50, 30)
                call Checkout(1)
                $ line = 0
                $ action_context = 0
                $ renpy.pop_call()          #removes the call to this label
                if Approval:
                        $ StormX.change_face("bemused", 2)
                        if bg_current == "bg_storm":
                            ch_s "What brought you here?"
                        else:
                            ch_s "I did not expect interruptions. . ."
                        $ StormX.Blush = 0
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
                            call Remove_Girl(StormX)
                return                      #returns to sexmenu, which returns to original
    #End of "Join" option



    if action_context == StormX:                                                                  #Storm auto-starts
                if Approval > 2:                                                      # fix, add storm auto stuff here
                        if StormX.wearing_skirt:
                            "[StormX.name]'s hand snakes down her body, and hikes up her skirt."
                            $ StormX.Upskirt = 1
                        elif StormX.PantsNum() > 6:
                            "[StormX.name] slides her hand down her body and into her pants."
                        elif StormX.HoseNum() >= 5:
                            "[StormX.name]'s hand slides down her body and under her [StormX.Hose]."
                        elif StormX.Panties:
                            "[StormX.name]'s hand slides down her body and under her [StormX.Panties]."
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
                                    ch_p "That is so sexy, [StormX.Pet]."
                                    $ StormX.nameCheck() #checks reaction to petname
                                    "You lean back and enjoy the show."
                                    $ StormX.change_stat("love", 80, 1)
                                    $ StormX.change_stat("obedience", 90, 1)
                                    $ StormX.change_stat("obedience", 50, 2)
                            "Ask her to stop.":
                                    $ StormX.change_face("surprised")
                                    $ StormX.change_stat("inhibition", 70, 1)
                                    ch_p "Let's not do that right now, [StormX.Pet]."
                                    $ StormX.nameCheck() #checks reaction to petname
                                    "[StormX.name] pulls her hands away from herself."
                                    $ StormX.OutfitChange()
                                    $ StormX.change_stat("obedience", 90, 1)
                                    $ StormX.change_stat("obedience", 50, 1)
                                    $ StormX.change_stat("obedience", 30, 2)
                                    return
                        jump Storm_M_Prep
                else:
                        $ temp_modifier = 0                               # fix, add storm auto stuff here
                        $ offhand_action = 0
                return
    #End if [StormX.name] intitiates this action

    #first time
    if not StormX.Mast:
            $ StormX.change_face("surprised", 1)
            $ StormX.Mouth = "kiss"
            ch_s "Oh, so you like the watch? . ."
            if StormX.Forced:
                $ StormX.change_face("sad")
                ch_s "and that is -all- that you expect?"


    #First time dialog
    if not StormX.Mast and Approval:
            if StormX.Forced:
                $ StormX.change_face("sad")
                $ StormX.change_stat("love", 70, -3, 1)
                $ StormX.change_stat("love", 20, -2, 1)
            elif StormX.love >= StormX.obedience and StormX.love >= StormX.inhibition:
                $ StormX.change_face("sexy")
                $ StormX.Brows = "sad"
                $ StormX.Mouth = "smile"
                ch_s "I am usually alone for this . . ."
            elif StormX.obedience >= StormX.inhibition:
                $ StormX.change_face("normal")
                ch_s "If you enjoy watching, [StormX.Petname]. . ."
            else: # Uninhibited
                $ StormX.change_face("sad")
                $ StormX.Mouth = "smile"
                ch_s "I do not mind an audience . . ."


    #Second time+ initial dialog
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
                $ line = renpy.random.choice(["I put on quite the show?",
                    "You did not get enough earlier?",
                    "I did enjoy the audience participation. . ."])
                ch_s "[line]"
            elif StormX.Mast < 3:
                $ StormX.change_face("sexy", 1)
                $ StormX.Brows = "confused"
                ch_s "You enjoyed the show?"
            else:
                $ StormX.change_face("sexy", 1)
                $ StormX.ArmPose = 2
                $ line = renpy.random.choice(["You really do like to watch.",
                    "Once more?",
                    "You enjoy watching me do that?",
                    "You want me to take care of myself?"])
                ch_s "[line]"
                $ line = 0
    #End second time+ initial dialog

    #If she's into it. . .
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
                $ line = renpy.random.choice(["Fine.",
                    "It could not hurt having you around. . .",
                    "Very well.",
                    "Sure, why not?",
                    "[[chuckles]. . . Fine."])
                ch_s "[line]"
                $ line = 0
            $ StormX.change_stat("obedience", 20, 1)
            $ StormX.change_stat("obedience", 60, 1)
            $ StormX.change_stat("inhibition", 70, 2)
            jump Storm_M_Prep

    #If she's not into it, but maybe. . .
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
                        $ line = renpy.random.choice(["You really do like to watch.",
                            "Once more?",
                            "You enjoy watching me do that?",
                            "You want me to take care of myself?"])
                        ch_s "[line]"
                        $ line = 0
                        jump Storm_M_Prep

            "Just get at it already.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(StormX, 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
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
    # end of asking her to do it

    #She refused all offers.
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
            $ StormX.recent_history.append("no masturbation")
            $ StormX.daily_history.append("no masturbation")
            return
    elif Taboo:                             # she refuses and this is too public a place for her
            $ StormX.change_face("angry", 1)
            $ StormX.daily_history.append("tabno")
            ch_s "I cannot do that here."
            $ StormX.change_stat("lust", 90, 5)
            $ StormX.change_stat("obedience", 50, -3)
            return
    elif StormX.Mast:
            $ StormX.change_face("sad")
            ch_s "I expect that you can entertain yourself elsewhere."
    else:
            $ StormX.change_face("normal", 1)
            ch_s "I do not think so, [StormX.Petname]."
    $ StormX.recent_history.append("no masturbation")
    $ StormX.daily_history.append("no masturbation")
    $ temp_modifier = 0
    return

label Storm_M_Prep:
    $ StormX.Upskirt = 1
    $ StormX.PantiesDown = 1
    call Storm_First_Bottomless(1)
    call set_the_scene(Dress=0)

    #if she hasn't seen you yet. . .
    if "unseen" in StormX.recent_history:
            $ StormX.change_face("sexy")
            $ StormX.Eyes = "closed"
            $ StormX.ArmPose = 2
            "You see [StormX.name] leaning back, masturbating. You don't think she's noticed you yet."
    else:
            $ StormX.change_face("sexy")
            $ StormX.ArmPose = 2
            "[StormX.name] lays back and starts to toy with herself."
            if not StormX.Mast:#First time
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
        $ girl_offhand_action = "fondle pussy"

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ line = 0
    if Taboo:
        $ StormX.DrainWord("tabno")
    $ StormX.DrainWord("no masturbation")
    $ StormX.recent_history.append("masturbation")
    $ StormX.daily_history.append("masturbation")

label Storm_M_Cycle:
    if action_context == "join":
        $ renpy.pop_call()
        $ action_context = 0

    while Round >=0:
        call Storm_Pos_Reset("masturbation")
        call Shift_Focus(StormX)
        $ StormX.lustFace()
        if "unseen" in StormX.recent_history:
                $ StormX.Eyes = "closed"

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep Watching.":
                                pass

                        "[StormX.name]. . .[[jump in]" if "unseen" not in StormX.recent_history and "join" not in Player.recent_history and StormX.Loc == bg_current:
                                "[StormX.name] slows what she's doing with a sly grin."
                                ch_s "Enjoying yourself?"
                                $ action_context = "join"
                                call Storm_Masturbate
                        "\"Ahem. . .\"" if "unseen" in StormX.recent_history and StormX.Loc == bg_current:
                                jump Storm_M_Interupted

                        "Start jack'in it." if offhand_action != "jackin":
                                call Jackin(StormX)
                        "Stop jack'in it." if offhand_action == "jackin":
                                $ offhand_action = 0

                        "Slap her ass" if StormX.Loc == bg_current:
                                if "unseen" in StormX.recent_history:
                                        "You smack [StormX.name] firmly on the ass!"
                                        jump Storm_M_Interupted
                                else:
                                        call Slap_Ass(StormX)
                                        $ counter += 1
                                        $ Round -= 1
                                        jump Storm_M_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0

                        "Change what I'm doing":
                                menu:
                                    "Offhand action" if StormX.Loc == bg_current:
                                            if StormX.Action and MultiAction:
                                                call Offhand_Set
                                                if offhand_action:
                                                    $ StormX.Action -= 1
                                            else:
                                                    call Sex_Basic_Dialog(StormX,"tired")

                                    "Threesome actions (locked)" if not Partner or "unseen" in StormX.recent_history or StormX.Loc != bg_current:
                                        pass
                                    "Threesome actions" if Partner and "unseen" not in StormX.recent_history and StormX.Loc == bg_current:
                                        menu:
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(StormX)
                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(StormX)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Storm_M_Cycle
                                            "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Storm_M_Cycle
                                            "Never mind":
                                                        jump Storm_M_Cycle

                                    "Show her feet" if not ShowFeet and (StormX.Pose == "doggy" or StormX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (StormX.Pose == "doggy" or StormX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [StormX.name]":
                                            if "unseen" in StormX.recent_history:
                                                    ch_p "Oh, yeah, take it off. . ."
                                                    jump Storm_M_Interupted
                                            else:
                                                    call Girl_Undress(StormX)
                                    "Clean up [StormX.name] (locked)" if not StormX.Spunk:
                                            pass
                                    "Clean up [StormX.name]" if StormX.Spunk:
                                            if "unseen" in StormX.recent_history:
                                                    ch_p "You've got a little something on you. . ."
                                                    jump Storm_M_Interupted
                                            else:
                                                    call Girl_Cleanup(StormX,"ask")
                                    "Never mind":
                                            jump Storm_M_Cycle

                        "Back to Sex Menu" if MultiAction and StormX.Loc == bg_current:
                                    ch_p "Let's try something else."
                                    call Storm_Pos_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Storm_M_Interupted
                        "End Scene" if not MultiAction or StormX.Loc != bg_current:
                                    ch_p "Let's stop for now."
                                    call Storm_Pos_Reset
                                    $ line = 0
                                    jump Storm_M_Interupted
        #End menu (if line)

        call Shift_Focus(StormX)
        call Sex_Dialog(StormX,Partner)

        #If either of you could cum

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up

        if Player.Focus >= 100 or StormX.lust >= 100:
                    #If you can cum:
                    if Player.Focus >= 100:
                        if "unseen" not in StormX.recent_history:
                            #if she knows you're there
                            call Player_Cumming(StormX)
                            if "angry" in StormX.recent_history:
                                call Storm_Pos_Reset
                                return
                            $ StormX.change_stat("lust", 200, 5)
                            if 100 > StormX.lust >= 70 and StormX.OCount < 2:
                                $ StormX.recent_history.append("unsatisfied")
                                $ StormX.daily_history.append("unsatisfied")
                            $ line = "came"
                        else: #If she wasn't aware you were there
                            "You grunt and try to hold it in."
                            $ Player.Focus = 95
                            if StormX.Loc == bg_current or StormX.Loc == "bg_desk":
                                    jump Storm_M_Interupted

                    #If [StormX.name] can cum
                    if StormX.lust >= 100:
                        call Girl_Cumming(StormX)
                        if StormX.Loc == bg_current or StormX.Loc == "bg_desk":
                                jump Storm_M_Interupted

                    if line == "came":
                        $ line = 0
                        if not Player.Semen:
                            "You're emptied out, you should probably take a break."
                            $ offhand_action = 0 if offhand_action == "jackin" else offhand_action


                        if "unsatisfied" in StormX.recent_history:#And [StormX.name] is unsatisfied,
                            "[StormX.name] still seems a bit unsatisfied with the experience."
                            menu:
                                "Let her keep going?"
                                "Yes, keep going for a bit.":
                                    $ line = "You let her get back into it"
                                    jump Storm_M_Cycle
                                "No, I'm done.":
                                    "You ask her to stop."
                                    return
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        if "unseen" in StormX.recent_history:
                if Round == 10:
                    "It's getting a bit late, [StormX.name] will probably be wrapping up soon."
                elif Round == 5:
                    "She's definitely going to stop soon."
        else:
                if StormX.Loc == bg_current:
                        call Escalation(StormX) #sees if she wants to escalate things

                if Round == 10:
                    ch_s "I will probably take a break soon."
                    $ StormX.lust += 10
                elif Round == 5:
                    ch_s "Ah! I am nearly finished. . ."
                    $ StormX.lust += 25

    #Round = 0 loop breaks
    $ StormX.change_face("bemused", 0)
    $ line = 0
    if "unseen" not in StormX.recent_history:
        ch_s "That is enough of that."

label Storm_M_Interupted:

    # If she hasn't noticed you're there before cumming
    if "unseen" in StormX.recent_history:
                $ StormX.change_face("surprised", 2)
                "[StormX.name] stops what she's doing with a start, eyes wide."
                call Storm_First_Bottomless(1)
                $ StormX.change_face("confused", 1, Eyes="surprised")
                if StormX.Loc == "bg_desk":
                        $ StormX.Loc = bg_current
                        call Display_Girl(StormX)
                        "She approaches you."

                #If you've been jacking it
                if offhand_action == "jackin":
                        ch_s "!"
                        ch_s "How long have you been there?!"
                        $ StormX.Eyes = "down"
                        menu:
                            ch_s ". . . I notice you're taken care of yourself. . . "
                            "A little while, it was an excellent show.":
                                    $ StormX.change_face("sexy",1)
                                    $ StormX.change_stat("obedience", 50, 3)
                                    $ StormX.change_stat("obedience", 70, 2)
                                    ch_s "I imagine it was. . ."
                                    if StormX.love >= 800 or StormX.obedience >= 500 or StormX.inhibition >= 500:
                                        $ temp_modifier += 10
                                        $ StormX.change_stat("lust", 90, 5)
                                    ch_s "and I have been missing a show myself. . ."

                            "I. . . just got here?":
                                    $ StormX.change_face("angry",1, Eyes="down")
                                    $ StormX.change_stat("love", 70, 2)
                                    $ StormX.change_stat("love", 90, 1)
                                    $ StormX.change_stat("obedience", 50, 2)
                                    $ StormX.change_stat("obedience", 70, 2)
                                    "She looks pointedly at your cock,"
                                    $ StormX.Eyes = "squint"
                                    ch_s "Long enough, it would appear. . ."
                                    if StormX.love >= 800 or StormX.obedience >= 500 or StormX.inhibition >= 500:
                                            $ temp_modifier += 10
                                            $ StormX.change_stat("lust", 90, 5)
                                            $ StormX.change_face("bemused", 1)
                                            ch_s "I expect that you could not contain your enthusiasm. . ."
                                    else:
                                            $ temp_modifier -= 10
                                            $ StormX.change_stat("lust", 200, -5)

                        if "Historia" not in Player.Traits:
                                    call Seen_First_Peen(StormX,Partner)
                                    ch_s "Hmm. . ."

                #you haven't been jacking it
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

                $ StormX.DrainWord("unseen",1,0) #She sees you, so remove unseens
                $ StormX.Mast += 1
                if "classcaught" not in StormX.History or "Historia" in Player.Traits:
                    # this activates if it's the first time in class
                    return
                if Round <= 10:
                    ch_s "It seems that it has gotten late while I was. . . distracted."
                    return
                $ action_context = "join"
                call Storm_Masturbate
                "error: report this if you see it."
                return #should be redundant
    #End Unseen

    #else, if She's seen you already
    $ StormX.Action -= 1
    $ StormX.Mast += 1
    call Checkout
    if action_context == "shift":
        $ action_context = 0
        return
    $ action_context = 0

    if Partner == "Kitty":
        call Partner_Like(StormX,4,2)
    else:
        call Partner_Like(StormX,3,2)

    if StormX.Loc != bg_current and StormX.Loc != "bg_desk":
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
        "Well, I have something you could take care of. . ." if Player.Semen and StormX.Action and MultiAction:
                $ action_context = "shift"
                return
        "You could just keep going. . ." if Player.Semen:
                $ StormX.change_face("sly")
                if StormX.Action and Round >= 10:
                    ch_s "I could. . ."
                    jump Storm_M_Cycle
                else:
                    ch_s "Give me a moment to recover. . ."
        "I'm good here. [[Stop]":
                if StormX.love < 800 and StormX.inhibition < 500 and StormX.obedience < 500:
                    $ StormX.OutfitChange()
                $ StormX.change_face("normal")
                $ StormX.Brows = "confused"
                ch_s ". . . fine then. . ."
                $ StormX.Brows = "normal"
        "You should probably stop for now." if StormX.lust > 30:
                $ StormX.change_face("angry")
                ch_s "I . . . fine . ."
    if offhand_action == "jackin":
        $ offhand_action = 0
    return

## end StormX.Masturbating ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Start [StormX.name] Sex pose //////////////////////////////////////////////////////////////////////////////////
# StormX.Sex_P //////////////////////////////////////////////////////////////////////

label Storm_Sex_P:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(StormX)
    if StormX.Sex >= 7: # She loves it
        $ temp_modifier += 15
    elif StormX.Sex >= 3: #You've done it before several times
        $ temp_modifier += 12
    elif StormX.Sex: #You've done it before
        $ temp_modifier += 10

    if StormX.Addict >= 75 and (StormX.CreamP + StormX.CreamA) >=3: #She's really strung out and has creampied
        $ temp_modifier += 20
    elif StormX.Addict >= 75:
        $ temp_modifier += 15

    if StormX.lust > 85:
        $ temp_modifier += 10
    elif StormX.lust > 75: #She's really horny
        $ temp_modifier += 5

    if action_context == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in StormX.Traits:
        $ temp_modifier += (4*Taboo)
    if StormX in Player.Harem or "sex friend" in StormX.Petnames:
        $ temp_modifier += 10
    elif "ex" in StormX.Traits:
        $ temp_modifier -= 40
    if StormX.ForcedCount and not StormX.Forced:
        $ temp_modifier -= 5 * StormX.ForcedCount



    if Taboo and "tabno" in StormX.daily_history:
        $ temp_modifier -= 10

    if "no sex" in StormX.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no sex" in StormX.recent_history else 0


    $ Approval = ApprovalCheck(StormX, 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)

    if action_context == "auto":
                call Storm_Sex_Launch("sex")
                if StormX.wearing_skirt:
                    "You roll back, pulling [StormX.name] on top of you, sliding her skirt up as you go."
                    $ StormX.Upskirt = 1
                elif StormX.PantsNum() >= 6:
                    "You roll back, pulling [StormX.name] on top of you, sliding her [StormX.Legs] down as you do."
                    $ StormX.Legs = 0
                else:
                    "You roll back, pulling [StormX.name] on top of you."
                $ StormX.SeenPanties = 1
                "You rub the tip of your cock against her moist slit."
                $ StormX.change_face("surprised", 1)

                if (StormX.Sex and Approval) or (Approval > 1):
                    #this is not the first time you've had sex, or she's into it
                    "[StormX.name] is briefly startled, but melts into a sly smile."
                    $ StormX.change_face("sly")
                    $ StormX.change_stat("obedience", 70, 3)
                    $ StormX.change_stat("inhibition", 50, 3)
                    $ StormX.change_stat("inhibition", 70, 1)
                    ch_s "Mmm, if you insist, [StormX.Petname]."
                    jump Storm_SexPrep
                else:
                    #she's questioning it
                    $ StormX.Brows = "angry"
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
                                    if StormX.Sex:
                                        ch_s "Perhaps ask first, [StormX.Petname]."
                                    else:
                                        ch_s "Some other time, perhaps. .  ."
                        "Just fucking.":
                            $ StormX.change_stat("love", 80, -10, 1)
                            $ StormX.change_stat("love", 200, -10)
                            "You press inside some more."
                            $ StormX.change_stat("obedience", 70, 3)
                            $ StormX.change_stat("inhibition", 50, 3)
                            if not ApprovalCheck(StormX, 700, "O", TabM=1):   #Checks if obedience is 700+
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
    #End Auto


    if not StormX.Sex and "no sex" not in StormX.recent_history:
            #first time
            $ StormX.change_face("surprised", 1)
            $ StormX.Mouth = "kiss"
            ch_s "Hmm, are you certain you are prepared for this? . . "
            if StormX.Forced:
                $ StormX.change_face("sad")
                ch_s "This is what you would have me do?"


    if not StormX.Sex and Approval:
            #First time dialog
            if StormX.Forced:
                $ StormX.change_face("sad")
                $ StormX.change_stat("love", 70, -30, 1)
                $ StormX.change_stat("love", 20, -20, 1)
            elif StormX.love >= (StormX.obedience + StormX.inhibition):
                $ StormX.change_face("sexy")
                $ StormX.Brows = "sad"
                $ StormX.Mouth = "smile"
                ch_s "I would not want to. . . overwhelm you. . ."
            elif StormX.obedience >= StormX.inhibition:
                $ StormX.change_face("normal")
                ch_s "If that is what you wish, [StormX.Petname]. . ."
            elif StormX.Addict >= 50:
                $ StormX.change_face("manic", 1)
                ch_s "I was curious as to the effect that would have. . ."
            else: # Uninhibited
                $ StormX.change_face("sad")
                $ StormX.Mouth = "smile"
                ch_s "I was hoping you would ask. . ."
            #End first time dialog

    elif Approval:
            #Second time+ dialog
            $ StormX.change_face("sexy", 1)
            if StormX.Forced:
                $ StormX.change_face("sad")
                $ StormX.change_stat("love", 70, -3, 1)
                $ StormX.change_stat("love", 20, -2, 1)
                ch_s "Oh, again?"
            elif not Taboo and "tabno" in StormX.daily_history:
                ch_s "I do suppose this is more private."
            elif "sex" in StormX.recent_history:
                ch_s "Again? [StormX.Petname], you are a lion!"
                jump Storm_SexPrep
            elif "sex" in StormX.daily_history:
                $ line = renpy.random.choice(["Back again?",
                    "You would like another round?",
                    "I suppose that I can be irresistible. . .",
                    "Did you not get enough earlier?",
                    "You are wearing me out, " + StormX.Petname + "."])
                ch_s "[line]"
            elif StormX.Sex < 3:
                $ StormX.Brows = "confused"
                $ StormX.Mouth = "kiss"
                ch_s "Oh? Another round?"
            else:
                $ line = renpy.random.choice(["Oh, did you want some of this?",
                    "You wouldd like another round?",
                    "I suppose that I can be irresistible. . .",
                    "I could get used to this. . .",
                    "Did you want me to ride you?"])
                ch_s "[line]"
            $ line = 0
            #end Second time+ dialog

    if Approval >= 2:
            #She's into it. . .
            if StormX.Forced:
                $ StormX.change_face("sad")
                $ StormX.change_stat("obedience", 90, 1)
                $ StormX.change_stat("inhibition", 60, 1)
                ch_s "Oh, very well, if it will satisfy you."
            elif "no sex" in StormX.daily_history:
                ch_s "Very well, I am convinced. . ."
            else:
                $ StormX.change_face("sexy", 1)
                $ StormX.change_stat("love", 90, 1)
                $ StormX.change_stat("inhibition", 50, 3)
                $ line = renpy.random.choice(["Well. . . fine, I accept.",
                    "Of course!",
                    "We could, I suppose.",
                    "Hmmm, yes.",
                    "How could I refuse?"])
                ch_s "[line]"
                $ line = 0
            $ StormX.change_stat("obedience", 20, 1)
            $ StormX.change_stat("obedience", 60, 1)
            $ StormX.change_stat("inhibition", 70, 2)
            jump Storm_SexPrep

    else:
            #She's not into it, but maybe. . .
            $ StormX.change_face("angry")
            if "no sex" in StormX.recent_history:
                ch_s "I am afraid that \"no\" is my final answer, [StormX.Petname]."
            elif Taboo and "tabno" in StormX.daily_history and "no sex" in StormX.daily_history:
                ch_s "I have already informed you. . . not in such an exposed location."
            elif "no sex" in StormX.daily_history:
                ch_s "I believe that I just told you \"no,\" [StormX.Petname]."
            elif Taboo and "tabno" in StormX.daily_history:
                ch_s "I have already informed you, this is too public!"
            elif not StormX.Sex:
                $ StormX.change_face("bemused")
                ch_s "I seriously doubt that you understand what you would be in for. . ."
            else:
                $ StormX.change_face("bemused")
                ch_s "Perhaps another time? . ."
            menu:
                extend ""
                "Sorry, never mind." if "no sex" in StormX.daily_history:
                        $ StormX.change_face("bemused")
                        ch_s "I can appreciate your. . . desires."
                        return
                "Maybe later?" if "no sex" not in StormX.daily_history:
                        $ StormX.change_face("sexy")
                        ch_s "Oh, of that I am certain. . ."
                        $ StormX.change_stat("love", 80, 2)
                        $ StormX.change_stat("inhibition", 70, 2)
                        if Taboo:
                            $ StormX.recent_history.append("tabno")
                            $ StormX.daily_history.append("tabno")
                        $ StormX.recent_history.append("no sex")
                        $ StormX.daily_history.append("no sex")
                        return
                "I think you'd enjoy it as much as I would. . .":
                        if Approval:
                            $ StormX.change_face("sexy")
                            $ StormX.change_stat("obedience", 90, 2)
                            $ StormX.change_stat("obedience", 50, 2)
                            $ StormX.change_stat("inhibition", 70, 3)
                            $ StormX.change_stat("inhibition", 40, 2)
                            $ line = renpy.random.choice(["I cannot argue with that. . .",
                                "I suppose you have a point. . .",
                                "You do raise a worthy point. . ."])
                            ch_s "[line]"
                            $ line = 0
                            jump Storm_SexPrep
                "Just deal with it.":                                               # Pressured into it
                        $ Approval = ApprovalCheck(StormX, 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
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
                #end menu
    #end Approval check

    #She refused all offers.
    $ StormX.ArmPose = 1
    if "no sex" in StormX.daily_history:
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
    elif Taboo:                             # she refuses and this is too public a place for her
        $ StormX.change_face("angry", 1)
        $ StormX.recent_history.append("tabno")
        $ StormX.daily_history.append("tabno")
        ch_s "How could you imagine that this would be an appropriate location?"
        $ StormX.change_stat("lust", 200, 5)
        $ StormX.change_stat("obedience", 50, -3)
    elif StormX.Sex:
        $ StormX.change_face("sad")
        ch_s "I am certain you can take care of that yourself."
    else:
        $ StormX.change_face("normal", 1)
        ch_s "I must refuse."
    $ StormX.recent_history.append("no sex")
    $ StormX.daily_history.append("no sex")
    $ temp_modifier = 0
    return

label Storm_SexPrep:
    call Seen_First_Peen(StormX,Partner,React=action_context)
    call Storm_Sex_Launch("hotdog")

    if action_context == StormX:
            #Storm auto-starts
            $ action_context = 0
            if StormX.wearing_skirt:
                "[StormX.name] pushes you back and climbs on top of you, sliding her skirt up as she does so."
                $ StormX.Upskirt = 1
            elif StormX.PantsNum() >= 6:
                "[StormX.name] pushes you down and climbs on top of you, sliding her [StormX.Legs] down as she does so."
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
                    ch_p "Oh yeah, [StormX.Pet], let's do this."
                    $ StormX.nameCheck() #checks reaction to petname
                    "[StormX.name] slides it in."
                    $ StormX.change_stat("love", 85, 1)
                    $ StormX.change_stat("obedience", 90, 1)
                    $ StormX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ StormX.change_face("surprised")
                    $ StormX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that right now, [StormX.Pet]."
                    $ StormX.nameCheck() #checks reaction to petname
                    "[StormX.name] pulls back."
                    $ StormX.change_stat("obedience", 90, 1)
                    $ StormX.change_stat("obedience", 50, 1)
                    $ StormX.change_stat("obedience", 30, 2)
                    $ Player.recent_history.append("nope")
                    $ StormX.AddWord(1,"refused","refused")
                    return
            $ StormX.PantiesDown = 1
            call Storm_First_Bottomless(1)

    elif action_context != "auto":
        call AutoStrip(StormX)

        if Taboo: # [StormX.name] gets started. . .
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

    else:  #if action_context == "auto"
        if (StormX.PantsNum() > 6 and not StormX.Upskirt) and (StormX.Panties and not StormX.PantiesDown):
            "You quickly pull down her pants and her [StormX.Panties] and press against her slit."
        elif (StormX.Panties and not StormX.PantiesDown):
            "You quickly pull down her [StormX.Panties] and press against her slit."
        $ StormX.Upskirt = 1
        $ StormX.PantiesDown = 1
        $ StormX.SeenPanties = 1
        call Storm_First_Bottomless(1)

    if Player.Focus >= 50:
            ch_s "I must say [StormX.Petname], you certainly do seem to be. . . excited."
    if not StormX.Sex:
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
    $ line = 0
    $ counter = 0
    $ Player.Cock = "in"
    $ primary_action = "sex"
    $ action_speed = 1
    if Taboo:
        $ StormX.DrainWord("tabno")
    $ StormX.DrainWord("no sex")
    $ StormX.recent_history.append("sex")
    $ StormX.daily_history.append("sex")

label Storm_Sex_Cycle: #Repeating strokes
    while Round >=0:
        call Shift_Focus(StormX)
        call Storm_Sex_Launch("sex")
        $ action_speed = 2 if action_speed >= 4 else action_speed
        $ StormX.lustFace()
        $ Player.Cock = "in"
        $ primary_action = "sex"
        $ StormX.Upskirt = 1
        $ StormX.PantiesDown = 1

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if action_speed:
                                    pass
                        "Keep going. . . (locked)" if not action_speed:
                                    pass

                        "Start moving? . ." if not action_speed:
                                    $ action_speed = 1
                        "action_speed up. . ." if 0 < action_speed < 3:
                                    $ action_speed += 1
                                    "You ask her to up the pace a bit."
                        "action_speed up. . . (locked)" if action_speed >= 3:
                                    pass

                        "Slow Down. . ." if action_speed:
                                    $ action_speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not action_speed:
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(StormX)
                                    $ counter += 1
                                    $ Round -= 1
                                    jump Storm_Sex_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if StormX.Action and MultiAction:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ StormX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(StormX,"tired")

                                    "Shift primary action":
                                            if StormX.Action and MultiAction:
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
                                                call Sex_Basic_Dialog(StormX,"tired")
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [StormX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(StormX)
                                            "Asks [StormX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(StormX)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(StormX)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Storm_Sex_Cycle
                                            "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Storm_Sex_Cycle
                                            "Never mind":
                                                        jump Storm_Sex_Cycle
                                    "Just take a look at her.":
                                            $ Player.Cock = 0
                                            $ action_speed = 0

                                    "Show her feet" if not ShowFeet and (StormX.Pose == "doggy" or StormX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (StormX.Pose == "doggy" or StormX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [StormX.name]":
                                            call Girl_Undress(StormX)
                                    "Clean up [StormX.name] (locked)" if not StormX.Spunk:
                                            pass
                                    "Clean up [StormX.name]" if StormX.Spunk:
                                            call Girl_Cleanup(StormX,"ask")
                                    "Never mind":
                                            jump Storm_Sex_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Storm_Sex_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Storm_SexAfter
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Storm_Sex_Reset
                                    $ line = 0
                                    jump Storm_SexAfter
        #End menu (if line)

        call Shift_Focus(StormX)
        call Sex_Dialog(StormX,Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or StormX.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(StormX)
                            if "angry" in StormX.recent_history:
                                call Storm_Sex_Reset
                                return
                            $ StormX.change_stat("lust", 200, 5)
                            if 100 > StormX.lust >= 70 and StormX.OCount < 2:
                                    $ StormX.recent_history.append("unsatisfied")
                                    $ StormX.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Storm_SexAfter
                            $ line = "came"

                    if StormX.lust >= 100:
                            #If you're still going at it and [StormX.name] can cum
                            call Girl_Cumming(StormX)
                            if action_context == "shift" or "angry" in StormX.recent_history:
                                jump Storm_SexAfter

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Storm_SexAfter
                            elif "unsatisfied" in StormX.recent_history:
                                #And [StormX.name] is unsatisfied,
                                $ line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ line = "You get back into it"
                                        jump Storm_Sex_Cycle
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Storm_SexAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Storm_SexAfter
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if StormX.SEXP >= 100 or ApprovalCheck(StormX, 1200, "LO"):
            pass
        elif counter == (5 + StormX.Sex):
                    $ StormX.Brows = "confused"
                    ch_s "Are you nearly finished?"
        elif counter == (10 + StormX.Sex):
                    $ StormX.Brows = "angry"
                    ch_s "I am . . .becoming . . a bit. . . worn out. . . here. . ."
                    menu:
                        ch_s "Would you mind. . . a different. . . option?"
                        "How about a BJ?" if StormX.Action and MultiAction:
                                $ action_context = "shift"
                                call Storm_SexAfter
                                call Storm_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ counter += 1
                                jump Storm_Sex_Cycle
                        "Let's try something else." if MultiAction:
                                $ line = 0
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
        #End Count check

        call Escalation(StormX) #sees if she wants to escalate things

        if Round == 10:
            ch_s "You might want to consider finishing. . ."
        elif Round == 5:
            ch_s "We shall require a break soon."

    #Round = 0 loop breaks
    $ StormX.change_face("bemused", 0)
    $ line = 0
    ch_s "[StormX.Petname], that will be enough for now."

# [StormX.name] anal //////////////////////////////////////////////////////////////////////

label Storm_Sex_A:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(StormX)
    if StormX.Anal >= 7: # She loves it
        $ temp_modifier += 20
    elif StormX.Anal >= 3: #You've done it before several times
        $ temp_modifier += 17
    elif StormX.Anal: #You've done it before
        $ temp_modifier += 15

    if StormX.Addict >= 75 and (StormX.CreamP + StormX.CreamA) >=3: #She's really strung out and has creampied
        $ temp_modifier += 25
    elif StormX.Addict >= 75:
        $ temp_modifier += 15

    if StormX.lust > 85:
        $ temp_modifier += 10
    elif StormX.lust > 75: #She's really horny
        $ temp_modifier += 5

    $ temp_modifier += 10  # she starts out loose

    if action_context == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in StormX.Traits:
        $ temp_modifier += (5*Taboo)

    if StormX in Player.Harem or "sex friend" in StormX.Petnames:
        $ temp_modifier += 10
    elif "ex" in StormX.Traits:
        $ temp_modifier -= 40
    if StormX.ForcedCount and not StormX.Forced:
        $ temp_modifier -= 5 * StormX.ForcedCount

    if Taboo and "tabno" in StormX.daily_history:
        $ temp_modifier -= 10
    if "no anal" in StormX.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no anal" in StormX.recent_history else 0

    $ Approval = ApprovalCheck(StormX, 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)

    if action_context == "auto":
            call Storm_Sex_Launch("anal")
            if StormX.wearing_skirt:
                "You roll back, pulling [StormX.name] on top of you, sliding her skirt up as you go."
                $ StormX.Upskirt = 1
            elif StormX.PantsNum() >= 6:
                "You roll back, pulling [StormX.name] on top of you, sliding her [StormX.Legs] down as you do."
                $ StormX.Legs = 0
            else:
                "You roll back, pulling [StormX.name] on top of you."
            $ StormX.SeenPanties = 1
            "You press the tip of your cock against her tight rim."
            $ StormX.change_face("surprised", 1)

            if (StormX.Anal and Approval) or (Approval > 1):
                #this is not the first time you've had sex, or she's into it
                $ StormX.change_stat("obedience", 70, 3)
                $ StormX.change_stat("inhibition", 50, 3)
                $ StormX.change_stat("inhibition", 70, 1)
                "[StormX.name] is briefly startled, but melts into a sly smile."
                ch_s "[StormX.Petname], I am surprised at you. . ."
                jump Storm_AnalPrep
            else:
                #she's questioning it
                $ StormX.Brows = "angry"
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

                        if StormX.Anal:
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
            #end "auto"


    if not StormX.Anal and "no anal" not in StormX.recent_history:
            #first time
            $ StormX.change_face("surprised", 1)
            $ StormX.Mouth = "kiss"
            ch_s "I am shocked! Anal?"

            if StormX.Forced:
                $ StormX.change_face("sad")
                ch_s "Oh. Of course it would be anal."

    if "anal" in StormX.recent_history:
            $ StormX.change_face("sexy", 1)
            ch_s "Of course."
            jump Storm_AnalPrep


    if not StormX.Anal and Approval:
            #First time dialog
            if StormX.Forced:
                $ StormX.change_face("sad")
                $ StormX.change_stat("love", 70, -3, 1)
                $ StormX.change_stat("love", 20, -2, 1)
            elif StormX.love >= (StormX.obedience + StormX.inhibition):
                $ StormX.change_face("sexy")
                $ StormX.Brows = "sad"
                $ StormX.Mouth = "smile"
                ch_s "I was hoping that you would ask. . ."
            elif StormX.obedience >= StormX.inhibition:
                $ StormX.change_face("normal")
                ch_s "I expected we would get here at some point. . ."
            elif StormX.Addict >= 50:
                $ StormX.change_face("manic", 1)
                ch_s "Hmm, that would certainly be interesting. . ."
            else: # Uninhibited
                $ StormX.change_face("sad")
                $ StormX.Mouth = "smile"
                ch_s "I was getting tired of waiting. . ."

    elif Approval:
            #Second time+ dialog
            if StormX.Forced:
                $ StormX.change_face("sad")
                $ StormX.change_stat("love", 70, -3, 1)
                $ StormX.change_stat("love", 20, -2, 1)
                ch_s "You do not restrain yourself. . ."
            elif not Taboo and "tabno" in StormX.daily_history:
                ch_s "I suppose this is secluded enough. . ."
            elif "anal" in StormX.daily_history and not StormX.Loose:
                pass
            elif "anal" in StormX.recent_history:
                ch_s "I am properly stretched out. . ."
                jump Storm_AnalPrep
            elif "anal" in StormX.daily_history:
                $ StormX.change_face("sexy", 1)
                $ line = renpy.random.choice(["Back again so soon?",
                    "So you would like another round?",
                    "I am still rather sore from earlier.",
                    "You did not get enough earlier?",
                    "You are tiring me, " + StormX.Petname + "."])
                ch_s "[line]"
            else:
                $ StormX.change_face("sexy", 1)
                $ StormX.ArmPose = 2
                $ line = renpy.random.choice(["Oooh, you wanted some of this?",
                    "So you would like another round?",
                    "I knew you would enjoy it. . .",
                    "You want me to ride you?"])
                ch_s "[line]"
            $ line = 0

    if Approval >= 2:
            #She's into it. . .
            if StormX.Forced:
                $ StormX.change_face("sad")
                $ StormX.change_stat("obedience", 90, 1)
                $ StormX.change_stat("inhibition", 60, 1)
                ch_s "Oh very well."
            elif "no anal" in StormX.daily_history:
                ch_s "After some consideration. . ."
                ch_s "It might entertain me."
            else:
                $ StormX.change_face("sexy", 1)
                $ StormX.change_stat("love", 90, 1)
                $ StormX.change_stat("inhibition", 50, 3)
                $ line = renpy.random.choice(["Well. . . I suppose.",
                    "Of course!",
                    "We could, I suppose.",
                    "Hmm, yes. Fine.",
                    "Heh. Ok, ok."])
                ch_s "[line]"
                $ line = 0
            $ StormX.change_stat("obedience", 20, 1)
            $ StormX.change_stat("obedience", 60, 1)
            $ StormX.change_stat("inhibition", 70, 2)
            jump Storm_AnalPrep

    else:
            #She's not into it, but maybe. . .
            $ StormX.change_face("angry")
            if "no anal" in StormX.recent_history:
                ch_s "I am afraid that \"no\" is my final answer, [StormX.Petname]."
            elif Taboo and "tabno" in StormX.daily_history and "no anal" in StormX.daily_history:
                ch_s "I have already informed you. . . not in such an exposed location."
            elif "no anal" in StormX.daily_history:
                ch_s "I believe that I just told you \"no,\" [StormX.Petname]."
            elif Taboo and "tabno" in StormX.daily_history:
                ch_s "I have already informed you, this is too public!"
            elif not StormX.Anal:
                $ StormX.change_face("bemused")
                ch_s "I do not know that you are yet prepared for that."
            else:
                $ StormX.change_face("bemused")
                ch_s "Perhaps we could work up to that."
            menu:
                extend ""
                "Sorry, never mind." if "no anal" in StormX.daily_history:
                    $ StormX.change_face("bemused")
                    ch_s "I cannot blame you for your. . . desires."
                    return
                "Maybe later?" if "no anal" not in StormX.daily_history:
                    $ StormX.change_face("sexy")
                    ch_s "I imagine at some point we shall. . ."
                    ch_s ". . . frequently."
                    $ StormX.change_stat("love", 80, 2)
                    $ StormX.change_stat("inhibition", 70, 2)
                    if Taboo:
                        $ StormX.recent_history.append("tabno")
                        $ StormX.daily_history.append("tabno")
                    $ StormX.recent_history.append("no anal")
                    $ StormX.daily_history.append("no anal")
                    return
                "I bet it would feel really good. . .":
                    if Approval:
                        $ StormX.change_face("sexy")
                        $ StormX.change_stat("obedience", 90, 2)
                        $ StormX.change_stat("obedience", 50, 2)
                        $ StormX.change_stat("inhibition", 70, 3)
                        $ StormX.change_stat("inhibition", 40, 2)
                        $ line = renpy.random.choice(["I cannot exactly argue with that. . .",
                                "I suppose. . .",
                                "You do raise a good point. . ."])
                        ch_s "[line]"
                        $ line = 0
                        jump Storm_AnalPrep
                    else:
                        pass

                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(StormX, 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
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

    #She refused all offers.
    $ StormX.ArmPose = 1
    if "no anal" in StormX.daily_history:
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
        # she refuses and this is too public a place for her
        $ StormX.change_face("angry", 1)
        $ StormX.recent_history.append("tabno")
        $ StormX.daily_history.append("tabno")
        ch_s "How could you imagine that this would be an appropriate location?"
        $ StormX.change_stat("lust", 200, 5)
        $ StormX.change_stat("obedience", 50, -3)
    elif "anal" in StormX.daily_history:
        $ StormX.change_face("bemused")
        ch_s "Do not wear me out here."
    elif StormX.Anal:
        $ StormX.change_face("sad")
        ch_s "You shall have to display your worth to me again."
    else:
        $ StormX.change_face("normal", 1)
        ch_s "I do not think you have earned that yet."
    $ StormX.recent_history.append("no anal")
    $ StormX.daily_history.append("no anal")
    $ temp_modifier = 0
    return

label Storm_Anal_Cycle: #Repeating strokes
    while Round >=0:
        call Shift_Focus(StormX)
        call Storm_Sex_Launch("anal")
        $ action_speed = 2 if action_speed >= 4 else action_speed
        $ StormX.lustFace()
        $ Player.Cock = "anal"
        $ primary_action = "anal"

        if Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if action_speed:
                                    pass
                        "Keep going. . . (locked)" if not action_speed:
                                    pass

                        "Start moving? . ." if not action_speed:
                                    $ action_speed = 1
                        "action_speed up. . ." if 0 < action_speed < 3:
                                    $ action_speed += 1
                                    "You ask her to up the pace a bit."
                        "action_speed up. . . (locked)" if action_speed >= 3:
                                    pass

                        "Slow Down. . ." if action_speed:
                                    $ action_speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not action_speed:
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(StormX)
                                    $ counter += 1
                                    $ Round -= 1
                                    jump Storm_Anal_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if StormX.Action and MultiAction:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ StormX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(StormX,"tired")

                                    "Shift primary action":
                                            if StormX.Action and MultiAction:
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
                                                call Sex_Basic_Dialog(StormX,"tired")
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [StormX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(StormX)
                                            "Asks [StormX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(StormX)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(StormX)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Storm_Anal_Cycle
                                            "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Storm_Anal_Cycle
                                            "Never mind":
                                                        jump Storm_Anal_Cycle
                                    "Just take a look at her.":
                                            $ Player.Cock = 0
                                            $ action_speed = 0

                                    "Show her feet" if not ShowFeet and (StormX.Pose == "doggy" or StormX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (StormX.Pose == "doggy" or StormX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [StormX.name]":
                                            call Girl_Undress(StormX)
                                    "Clean up [StormX.name] (locked)" if not StormX.Spunk:
                                            pass
                                    "Clean up [StormX.name]" if StormX.Spunk:
                                            call Girl_Cleanup(StormX,"ask")
                                    "Never mind":
                                            jump Storm_Anal_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Storm_Sex_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Storm_AnalAfter
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Storm_Sex_Reset
                                    $ line = 0
                                    jump Storm_AnalAfter
        #End menu (if line)

        call Shift_Focus(StormX)
        call Sex_Dialog(StormX,Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or StormX.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(StormX)
                            if "angry" in StormX.recent_history:
                                call Storm_Sex_Reset
                                return
                            $ StormX.change_stat("lust", 200, 5)
                            if 100 > StormX.lust >= 70 and StormX.OCount < 2:
                                    $ StormX.recent_history.append("unsatisfied")
                                    $ StormX.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Storm_AnalAfter
                            $ line = "came"

                    if StormX.lust >= 100:
                            #If you're still going at it and [StormX.name] can cum
                            call Girl_Cumming(StormX)
                            if action_context == "shift" or "angry" in StormX.recent_history:
                                jump Storm_AnalAfter

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Storm_AnalAfter
                            elif "unsatisfied" in StormX.recent_history:
                                #And [StormX.name] is unsatisfied,
                                $ line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ line = "You get back into it"
                                        jump Storm_Anal_Cycle
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Storm_AnalAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Storm_AnalAfter
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if StormX.SEXP >= 100 or ApprovalCheck(StormX, 1200, "LO"):
            pass
        elif counter == (5 + StormX.Anal):
                    $ StormX.Brows = "confused"
                    ch_s "So are you nearly finished?"
        elif counter == (10 + StormX.Anal):
                    $ StormX.Brows = "angry"
                    ch_s "This is . . .becoming . . rather. . . uncomfortable. . ."
                    menu:
                        ch_s "Could we. . . do something. . . else?"
                        "How about a BJ?" if StormX.Action and MultiAction:
                                $ action_context = "shift"
                                call Storm_AnalAfter
                                call Storm_Blowjob
                        "How about a Handy?" if StormX.Action and MultiAction:
                                $ action_context = "shift"
                                call Storm_AnalAfter
                                call Storm_Handjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ counter += 1
                                jump Storm_Anal_Cycle
                        "Let's try something else." if MultiAction:
                                $ line = 0
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
        #End Count check

        if Round == 10:
            ch_s "You might want to consider finishing. . ."
        elif Round == 5:
            ch_s "We shall require a break soon."

    #Round = 0 loop breaks
    $ StormX.change_face("bemused", 0)
    $ line = 0
    ch_s "[StormX.Petname], that will be enough for now."

label Storm_Sex_H:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(StormX)
    if StormX.Hotdog >= 3: #You've done it before several times
        $ temp_modifier += 10
    elif StormX.Hotdog: #You've done it before
        $ temp_modifier += 5

    if StormX.lust > 85:
        $ temp_modifier += 10
    elif StormX.lust > 75: #She's really horny
        $ temp_modifier += 5
    if action_context == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in StormX.Traits:
        $ temp_modifier += (3*Taboo)
    if StormX in Player.Harem or "sex friend" in StormX.Petnames:
        $ temp_modifier += 10
    elif "ex" in StormX.Traits:
        $ temp_modifier -= 40
    if StormX.ForcedCount and not StormX.Forced:
        $ temp_modifier -= 5 * StormX.ForcedCount

    if Taboo and "tabno" in StormX.daily_history:
        $ temp_modifier -= 10

    if "no hotdog" in StormX.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no hotdog" in StormX.recent_history else 0

    $ Approval = ApprovalCheck(StormX, 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)

    if action_context == "auto":
            call Storm_Sex_Launch("hotdog")
            "You roll back, pulling [StormX.name] on top of you, and press your cock against her."
            $ StormX.change_face("surprised", 1)

            if (StormX.Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
                "[StormX.name] is briefly startled, but melts into a sly smile."
                $ StormX.change_face("sly")
                $ StormX.change_stat("obedience", 70, 3)
                $ StormX.change_stat("inhibition", 50, 3)
                $ StormX.change_stat("inhibition", 70, 1)
                ch_s "Now what shall we do with that . ."
                jump Storm_HotdogPrep
            else:                                                                                                            #she's questioning it
                $ StormX.Brows = "angry"
                menu:
                    ch_s "You are rather close, [StormX.Petname]. . ."
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
                        if not ApprovalCheck(StormX, 500, "O", TabM=1): #Checks if obedience is 700+
                            $ StormX.change_face("angry")
                            "[StormX.name] shoves you away."
                            ch_s "Do not go beyond yourself, [StormX.Petname]."
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
            #end auto


    if not StormX.Hotdog and "no hotdog" not in StormX.recent_history:
            #first time
            $ StormX.change_face("surprised", 1)
            $ StormX.Mouth = "kiss"
            ch_s "You would just like to press against each other like this?"

            if StormX.Forced:
                $ StormX.change_face("sad")
                ch_s ". . . and no more than that?"


    if not StormX.Hotdog and Approval:
            #First time dialog
            if StormX.Forced:
                $ StormX.change_face("sad")
                $ StormX.change_stat("love", 70, -3, 1)
                $ StormX.change_stat("love", 20, -2, 1)
            elif StormX.love >= (StormX.obedience + StormX.inhibition):
                $ StormX.change_face("sexy")
                $ StormX.Brows = "sad"
                $ StormX.Mouth = "smile"
                ch_s "I would not wish to leave you. . . un-tended. . ."
            elif StormX.obedience >= StormX.inhibition:
                $ StormX.change_face("normal")
                ch_s "If that is what works for you. . ."
            elif StormX.Addict >= 50:
                $ StormX.change_face("manic", 1)
                ch_s "Hrmm. . ."
            else: # Uninhibited
                $ StormX.change_face("sad")
                $ StormX.Mouth = "smile"
                ch_s "Well if that is what satisfies you. . ."

    elif Approval:
            #Second time+ dialog
            if StormX.Forced:
                $ StormX.change_face("sad")
                $ StormX.change_stat("love", 70, -3, 1)
                $ StormX.change_stat("love", 20, -2, 1)
                ch_s "Perhaps that is going a bit too far. . ."
            elif not Taboo and "tabno" in StormX.daily_history:
                ch_s "I suppose that this is a better location . ."
            elif "hotdog" in StormX.recent_history:
                $ StormX.change_face("sexy", 1)
                ch_s "Again? Oh, very well."
                jump Storm_HotdogPrep
            elif "hotdog" in StormX.daily_history:
                $ StormX.change_face("sexy", 1)
                $ line = renpy.random.choice(["Back again so soon?",
                    "So you would like another round?",
                    "You really are into this. . .",
                    "Are you sure that is all you would want?"])
                ch_s "[line]"
            else:
                $ StormX.change_face("sexy", 1)
                $ StormX.ArmPose = 2
                $ line = renpy.random.choice(["Oooh, you want some of this?",
                    "So you would like another round?",
                    "You really are into this. . .",
                    "You want another rub?"])
                ch_s "[line]"
            $ line = 0

    if Approval >= 2:
            #She's into it. . .
            if StormX.Forced:
                $ StormX.change_face("sad")
                $ StormX.change_stat("obedience", 80, 1)
                $ StormX.change_stat("inhibition", 60, 1)
                ch_s "Fine then."
            elif "no hotdog" in StormX.daily_history:
                ch_s "It was rather entertaining. . ."
            else:
                $ StormX.change_face("sexy", 1)
                $ StormX.change_stat("love", 80, 1)
                $ StormX.change_stat("inhibition", 50, 2)
                $ line = renpy.random.choice(["ery well then, let me give it a rub.",
                    "Very well.",
                    "Of course!",
                    "I suppose that we could do that.",
                    "Allow me. . .",
                    "Heh, ok, ok."])
                ch_s "[line]"
                $ line = 0
            $ StormX.change_stat("obedience", 60, 1)
            $ StormX.change_stat("inhibition", 70, 2)
            jump Storm_HotdogPrep

    else:
            #She's not into it, but maybe. . .
            $ StormX.change_face("angry")
            if "no hotdog" in StormX.recent_history:
                ch_s "I am afraid that \"no\" is my final answer, [StormX.Petname]."
            elif Taboo and "tabno" in StormX.daily_history and "no hotdog" in StormX.daily_history:
                ch_s "I just informed you. . .not in such an exposed location."
            elif "no hotdog" in StormX.daily_history:
                ch_s "I believe that I just told you \"no,\" [StormX.Petname]."
            elif Taboo and "tabno" in StormX.daily_history:
                ch_s "I already informed you. . .not in such an exposed location."
            elif not StormX.Hotdog:
                $ StormX.change_face("bemused")
                ch_s "Hmm, that could be entertaining, [StormX.Petname]. . ."
            else:
                $ StormX.change_face("bemused")
                ch_s "I do not believe that would be appropriate. . ."
            menu:
                extend ""
                "Sorry, never mind." if "no hotdog" in StormX.daily_history:
                    $ StormX.change_face("bemused")
                    ch_s "There is no harm in asking."
                    return
                "Maybe later?" if "no hotdog" not in StormX.daily_history:
                    $ StormX.change_face("sexy")
                    ch_s "I expect it will happen at some point, [StormX.Petname]."
                    $ StormX.change_stat("love", 80, 1)
                    $ StormX.change_stat("inhibition", 50, 1)
                    if Taboo:
                        $ StormX.recent_history.append("tabno")
                        $ StormX.daily_history.append("tabno")
                    $ StormX.recent_history.append("no hotdog")
                    $ StormX.daily_history.append("no hotdog")
                    return
                "You might like it. . .":
                    if Approval:
                        $ StormX.change_face("sexy")
                        $ StormX.change_stat("obedience", 60, 2)
                        $ StormX.change_stat("inhibition", 50, 2)
                        $ line = renpy.random.choice(["I cannot exactly argue with that. . .",
                                "I suppose so. . .",
                                "You do raise a good point. . ."])
                        ch_s "[line]"
                        $ line = 0
                        jump Storm_HotdogPrep
                    else:
                        pass

                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(StormX, 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
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

    #She refused all offers.
    $ StormX.ArmPose = 1

    if "no hotdog" in StormX.daily_history:
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
    elif Taboo:                             # she refuses and this is too public a place for her
        $ StormX.change_face("angry", 1)
        $ StormX.recent_history.append("tabno")
        $ StormX.daily_history.append("tabno")
        ch_s "This area is a bit too exposed for that sort of thing. . ."
        $ StormX.change_stat("lust", 200, 5)
        $ StormX.change_stat("obedience", 50, -3)
    elif StormX.Hotdog:
        $ StormX.change_face("sad")
        ch_s "Not under the circumstances."
    else:
        $ StormX.change_face("normal", 1)
        ch_s "Thank you, but no."
    $ StormX.recent_history.append("no hotdog")
    $ StormX.daily_history.append("no hotdog")
    $ temp_modifier = 0
    return

label Storm_Hotdog_Cycle: #Repeating strokes
    while Round >=0:
        call Shift_Focus(StormX)
        call Storm_Sex_Launch("hotdog")
        $ action_speed = 2 if action_speed >= 4 else action_speed
        $ StormX.lustFace()
        $ Player.Cock = "out"
        $ primary_action = "hotdog"

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if action_speed:
                                    pass
                        "Keep going. . . (locked)" if not action_speed:
                                    pass

                        "Start moving? . ." if not action_speed:
                                    $ action_speed = 1
                        "action_speed up. . ." if 0 < action_speed < 3:
                                    $ action_speed += 1
                                    "You ask her to up the pace a bit."
                        "action_speed up. . . (locked)" if action_speed >= 3:
                                    pass

                        "Slow Down. . ." if action_speed:
                                    $ action_speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not action_speed:
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(StormX)
                                    $ counter += 1
                                    $ Round -= 1
                                    jump Storm_Hotdog_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if StormX.Action and MultiAction:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ StormX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(StormX,"tired")

                                    "Shift primary action":
                                            if StormX.Action and MultiAction:
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
                                                call Sex_Basic_Dialog(StormX,"tired")
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [StormX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(StormX)
                                            "Asks [StormX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(StormX)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(StormX)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Storm_Hotdog_Cycle
                                            "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Storm_Hotdog_Cycle
                                            "Never mind":
                                                        jump Storm_Hotdog_Cycle
                                    "Just take a look at her.":
                                            $ Player.Cock = 0
                                            $ action_speed = 0

                                    "Show her feet" if not ShowFeet and (StormX.Pose == "doggy" or StormX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (StormX.Pose == "doggy" or StormX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [StormX.name]":
                                            call Girl_Undress(StormX)
                                    "Clean up [StormX.name] (locked)" if not StormX.Spunk:
                                            pass
                                    "Clean up [StormX.name]" if StormX.Spunk:
                                            call Girl_Cleanup(StormX,"ask")
                                    "Never mind":
                                            jump Storm_Hotdog_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Storm_Sex_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Storm_HotdogAfter
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Storm_Sex_Reset
                                    $ line = 0
                                    jump Storm_HotdogAfter
        #End menu (if line)

        call Shift_Focus(StormX)
        call Sex_Dialog(StormX,Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or StormX.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(StormX)
                            if "angry" in StormX.recent_history:
                                call Storm_Sex_Reset
                                return
                            $ StormX.change_stat("lust", 200, 5)
                            if 100 > StormX.lust >= 70 and StormX.OCount < 2:
                                    $ StormX.recent_history.append("unsatisfied")
                                    $ StormX.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Storm_HotdogAfter
                            $ line = "came"

                    if StormX.lust >= 100:
                            #If you're still going at it and [StormX.name] can cum
                            call Girl_Cumming(StormX)
                            if action_context == "shift" or "angry" in StormX.recent_history:
                                jump Storm_HotdogAfter

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Storm_HotdogAfter
                            elif "unsatisfied" in StormX.recent_history:
                                #And [StormX.name] is unsatisfied,
                                $ line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ line = "You get back into it"
                                        jump Storm_Hotdog_Cycle
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Storm_HotdogAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Storm_HotdogAfter
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if StormX.SEXP >= 100 or ApprovalCheck(StormX, 1200, "LO"):
            pass
        elif counter == (5 + StormX.Hotdog):
                    $ StormX.Brows = "confused"
                    ch_s "Are you nearly satisfied?"
        elif counter == (10 + StormX.Hotdog):
                    $ StormX.Brows = "angry"
                    menu:
                        ch_s "I am getting rather tired of this."
                        "How about a BJ?" if StormX.Action and MultiAction:
                                $ action_context = "shift"
                                call Storm_HotdogAfter
                                call Storm_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ counter += 1
                                jump Storm_Hotdog_Cycle
                        "Let's try something else." if MultiAction:
                                $ line = 0
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
        #End Count check

        call Escalation(StormX) #sees if she wants to escalate things

        if Round == 10:
            ch_s "You might want to consider finishing. . ."
        elif Round == 5:
            ch_s "We shall require a break soon."

    #Round = 0 loop breaks
    $ StormX.change_face("bemused", 0)
    $ line = 0
    ch_s "[StormX.Petname], that will be enough for now."
