# Emma_SexMenu //////////////////////////////////////////////////////////////////////
label Emma_SexAct(Act = 0):
        if AloneCheck(EmmaX) and EmmaX.Taboo == 20:
                $ EmmaX.Taboo = 0
                $ Taboo = 0
        call Shift_Focus(EmmaX)
        if Taboo > 20 and "taboo" not in EmmaX.History:
                # If she's yet to agree to taboo stuff
                call Emma_Taboo_Talk
                if bg_current == "bg_classroom":
                        ch_p "We could just lock the door, right?"
                        ch_e "We certainly could. . ."
                        "[EmmaX.name] walks to the door and locks it behind her."
                        $ Taboo = 0
                else:
                        return

        if Act == "SkipTo":
            $ renpy.pop_call() #causes it to skip past the primary_action Swap
            $ renpy.pop_call() #causes it to skip past the cycle you were in before
            #$ renpy.pop_call() #causes it to skip past the sex menu you were in before that
            call SkipTo(EmmaX)
        elif Act == "switch":
            $ renpy.pop_call() #causes it to skip past call here from Sex_Menu_Threesome
            #$ renpy.pop_call() #causes it to skip past call to Sex_Menu_Threesome
            # drops through to sex menu
        elif Act == "masturbate":
            call Emma_M_Prep
            if not action_context:
                return
        elif Act == "lesbian":
            call Les_Prep(EmmaX)
            if not action_context:
                return
        elif Act == "kissing":
            call KissPrep(EmmaX)
            if not action_context:
                return
        elif Act == "breasts":
            call Emma_Fondle_Breasts
            if not action_context:
                return
        elif Act == "blow":
            call Emma_BJ_Prep
            if not action_context:
                return
        elif Act == "hand":
            call Emma_HJ_Prep
            if not action_context:
                return
        elif Act == "sex":
            call Emma_SexPrep
            if not action_context:
                return

##  EmmaX.Masturbating //////////////////////////////////////////////////////////////////////
# counter 1 means she's seen you, counter 0 means she hasn't.
label Emma_Masturbate: #(action_context = action_context):
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(EmmaX)
    if EmmaX.Mast:
        $ temp_modifier += 10
    if EmmaX.SEXP >= 50:
        $ temp_modifier += 25
    elif EmmaX.SEXP >= 30:
        $ temp_modifier += 15
    elif EmmaX.SEXP >= 15:
        $ temp_modifier += 5
    if EmmaX.lust >= 90:
        $ temp_modifier += 20
    elif EmmaX.lust >= 75:
        $ temp_modifier += 5
    if "exhibitionist" in EmmaX.Traits:
        $ temp_modifier += (3*Taboo)
    if EmmaX in Player.Harem or "sex friend" in EmmaX.Petnames:
        $ temp_modifier += 10
    elif "ex" in EmmaX.Traits:
        $ temp_modifier -= 40
    if EmmaX.ForcedCount and not EmmaX.Forced:
        $ temp_modifier -= 5 * EmmaX.ForcedCount

    $ Approval = ApprovalCheck(EmmaX, 1300, TabM = 2) # 120, 135, 150, Taboo -80(200)

    $ EmmaX.DrainWord("unseen",1,0) #She sees you, so remove unseens

    if action_context == "join":       # This triggers if you ask to join in
                if Approval > 1 or (Approval and EmmaX.lust >= 50):
                    $ Player.AddWord(1,"join")
                    menu:
                        extend ""
                        "Would you like some help? I could lend some helping hands. . ."  if Player.Semen and EmmaX.Action:
                                $ EmmaX.change_stat("love", 90, 1)
                                $ EmmaX.change_stat("obedience", 50, 2)
                                $ EmmaX.change_face("sexy")
                                ch_e "Hm, well I do have my hands full with these. . ."
                                $ EmmaX.change_stat("obedience", 70, 2)
                                $ EmmaX.change_stat("inhibition", 70, 1)
                                $ offhand_action = "fondle breasts"
                                $ EmmaX.Mast += 1
                                jump Emma_M_Cycle
                        "Would you like some help? I could. . . up to you, I guess." if Player.Semen and EmmaX.Action:
                                $ EmmaX.change_stat("love", 70, 2)
                                $ EmmaX.change_stat("love", 90, 1)
                                $ EmmaX.change_face("sexy")
                                ch_e "I suppose I could use some added attention. . ."
                                $ EmmaX.change_stat("obedience", 70, 2)
                                $ EmmaX.change_stat("inhibition", 70, 1)
                                $ D20 = renpy.random.randint(1, 20)
                                if D20 > 10:
                                    $ offhand_action = "fondle breasts"
                                else:
                                    $ offhand_action = "suck breasts"
                                $ EmmaX.Mast += 1
                                jump Emma_M_Cycle
                        "Why don't we take care of each other?" if Player.Semen and EmmaX.Action:
                                $ EmmaX.change_face("sexy")
                                ch_e "I suppose I could spare some attention. . ."
                                $ renpy.pop_call()          #removes the call to this label
                                return                      #returns to sexmenu=
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

                #else: You've failed all checks so she kicks you out.
                $ EmmaX.ArmPose = 1
                $ EmmaX.OutfitChange()
                $ EmmaX.Action -= 1
                $ Player.change_stat("Focus", 50, 30)
                call Checkout(1)
                $ line = 0
                $ action_context = 0
                $ renpy.pop_call()          #removes the call to this label
                if Approval:
                        $ EmmaX.change_face("bemused", 1)
                        if bg_current == "bg_emma":
                            ch_e "Why are you even in my room?"
                        else:
                            ch_e "I wasn't expecting visitors. . ."
                        $ EmmaX.Blush = 0
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
                            call Remove_Girl(EmmaX)
                return                      #returns to sexmenu, which returns to original
    #End of "Join" option



    if action_context == EmmaX:                                                                  #Emma auto-starts
                if Approval > 2:                                                      # fix, add emma auto stuff here
                        if EmmaX.wearing_skirt:
                            "[EmmaX.name]'s hand snakes down her body, and hikes up her skirt."
                            $ EmmaX.Upskirt = 1
                        elif EmmaX.PantsNum() > 6:
                            "[EmmaX.name] slides her hand down her body and into her pants."
                        elif EmmaX.HoseNum() >= 5:
                            "[EmmaX.name]'s hand slides down her body and under her [EmmaX.Hose]."
                        elif EmmaX.Panties:
                            "[EmmaX.name]'s hand slides down her body and under her [EmmaX.Panties]."
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
                                    ch_p "That is so sexy, [EmmaX.Pet]."
                                    $ EmmaX.nameCheck() #checks reaction to petname
                                    "You lean back and enjoy the show."
                                    $ EmmaX.change_stat("love", 80, 1)
                                    $ EmmaX.change_stat("obedience", 90, 1)
                                    $ EmmaX.change_stat("obedience", 50, 2)
                            "Ask her to stop.":
                                    $ EmmaX.change_face("surprised")
                                    $ EmmaX.change_stat("inhibition", 70, 1)
                                    ch_p "Let's not do that right now, [EmmaX.Pet]."
                                    $ EmmaX.nameCheck() #checks reaction to petname
                                    "[EmmaX.name] pulls her hands away from herself."
                                    $ EmmaX.OutfitChange()
                                    $ EmmaX.change_stat("obedience", 90, 1)
                                    $ EmmaX.change_stat("obedience", 50, 1)
                                    $ EmmaX.change_stat("obedience", 30, 2)
                                    return
                        jump Emma_M_Prep
                else:
                        $ temp_modifier = 0                               # fix, add emma auto stuff here
                        $ offhand_action = 0
                return
    #End if [EmmaX.name] intitiates this action

    #first time
    if not EmmaX.Mast:
            $ EmmaX.change_face("surprised", 1)
            $ EmmaX.Mouth = "kiss"
            ch_e "So you enjoy a good show then. . ."
            if EmmaX.Forced:
                $ EmmaX.change_face("sad")
                ch_e "but. . . {i}only{/i} a show?"


    #First time dialog
    if not EmmaX.Mast and Approval:
            if EmmaX.Forced:
                $ EmmaX.change_face("sad")
                $ EmmaX.change_stat("love", 70, -3, 1)
                $ EmmaX.change_stat("love", 20, -2, 1)
            elif EmmaX.love >= EmmaX.obedience and EmmaX.love >= EmmaX.inhibition:
                $ EmmaX.change_face("sexy")
                $ EmmaX.Brows = "sad"
                $ EmmaX.Mouth = "smile"
                ch_e "I don't usually show this side . . ."
            elif EmmaX.obedience >= EmmaX.inhibition:
                $ EmmaX.change_face("normal")
                ch_e "If that's what you're into, [EmmaX.Petname]. . ."
            else: # Uninhibited
                $ EmmaX.change_face("sad")
                $ EmmaX.Mouth = "smile"
                ch_e "I do enjoy a good performance . . ."


    #Second time+ initial dialog
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
                $ line = renpy.random.choice(["I was that good?",
                    "Didn't get enough earlier?",
                    "I did enjoy the audience participation. . ."])
                ch_e "[line]"
            elif EmmaX.Mast < 3:
                $ EmmaX.change_face("sexy", 1)
                $ EmmaX.Brows = "confused"
                ch_e "You enjoyed the show?"
            else:
                $ EmmaX.change_face("sexy", 1)
                $ EmmaX.ArmPose = 2
                $ line = renpy.random.choice(["You really do like to watch.",
                    "Once more?",
                    "You enjoy watching me.",
                    "You want me to take care of myself?"])
                ch_e "[line]"
                $ line = 0
    #End second time+ initial dialog

    #If she's into it. . .
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
                $ line = renpy.random.choice(["Ok.",
                    "It couldn't hurt having you around. . .",
                    "Very well.",
                    "Sure, why not?",
                    "[[chuckles]. . . ok."])
                ch_e "[line]"
                $ line = 0
            $ EmmaX.change_stat("obedience", 20, 1)
            $ EmmaX.change_stat("obedience", 60, 1)
            $ EmmaX.change_stat("inhibition", 70, 2)
            jump Emma_M_Prep

    #If she's not into it, but maybe. . .
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
                        $ line = renpy.random.choice(["Ok.",
                            "It couldn't hurt having you around. . .",
                            "Very well.",
                            "Sure, why not?",
                            "[[chuckles]. . . ok."])
                        ch_e "[line]"
                        $ line = 0
                        jump Emma_M_Prep

            "Just get at it already.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(EmmaX, 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
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
    # end of asking her to do it

    #She refused all offers.
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
            $ EmmaX.recent_history.append("no masturbation")
            $ EmmaX.daily_history.append("no masturbation")
            return
    elif Taboo:                             # she refuses and this is too public a place for her
            $ EmmaX.change_face("angry", 1)
            $ EmmaX.daily_history.append("tabno")
            ch_e "Obviously not in someplace so exposed."
            $ EmmaX.change_stat("lust", 90, 5)
            $ EmmaX.change_stat("obedience", 50, -3)
            return
    elif EmmaX.Mast:
            $ EmmaX.change_face("sad")
            ch_e "I'm sure you can find something else to watch."
    else:
            $ EmmaX.change_face("normal", 1)
            ch_e "I don't think so, [EmmaX.Petname]."
    $ EmmaX.recent_history.append("no masturbation")
    $ EmmaX.daily_history.append("no masturbation")
    $ temp_modifier = 0
    return

label Emma_M_Prep:
    $ EmmaX.Upskirt = 1
    $ EmmaX.PantiesDown = 1
    call Emma_First_Bottomless(1)
    call set_the_scene(Dress=0)

    #if she hasn't seen you yet. . .
    if "unseen" in EmmaX.recent_history:
            $ EmmaX.change_face("sexy")
            $ EmmaX.Eyes = "closed"
            $ EmmaX.ArmPose = 2
            "You see [EmmaX.name] leaning back, masturbating. You don't think she's noticed you yet."
    else:
            $ EmmaX.change_face("sexy")
            $ EmmaX.ArmPose = 2
            "[EmmaX.name] lays back and starts to toy with herself."
            if not EmmaX.Mast:#First time
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
        $ girl_offhand_action = "fondle pussy"

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ line = 0
    if Taboo:
        $ EmmaX.DrainWord("tabno")
    $ EmmaX.DrainWord("no masturbation")
    $ EmmaX.recent_history.append("masturbation")
    $ EmmaX.daily_history.append("masturbation")

label Emma_M_Cycle:
    if action_context == "join":
        $ renpy.pop_call()
        $ action_context = 0

    while Round > 0:
        call reset_position(EmmaX, trigger = "masturbation")
        call Shift_Focus(EmmaX)
        $ EmmaX.lustFace()
        if "unseen" in EmmaX.recent_history:
                $ EmmaX.Eyes = "closed"

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep Watching.":
                                pass

                        "[EmmaX.name]. . .[[jump in]" if "unseen" not in EmmaX.recent_history and "join" not in Player.recent_history and EmmaX.Loc == bg_current:
                                "[EmmaX.name] slows what she's doing with a sly grin."
                                ch_e "Enjoying the show?"
                                $ action_context = "join"
                                call Emma_Masturbate
                        "\"Ahem. . .\"" if "unseen" in EmmaX.recent_history and EmmaX.Loc == bg_current:
                                jump Emma_M_Interupted

                        "Start jack'in it." if offhand_action != "jackin":
                                call Jackin(EmmaX)
                        "Stop jack'in it." if offhand_action == "jackin":
                                $ offhand_action = 0

                        "Slap her ass" if EmmaX.Loc == bg_current:
                                if "unseen" in EmmaX.recent_history:
                                        "You smack [EmmaX.name] firmly on the ass!"
                                        jump Emma_M_Interupted
                                else:
                                        call Slap_Ass(EmmaX)
                                        $ counter += 1
                                        $ Round -= 1
                                        jump Emma_M_Cycle

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
                                    "Offhand action" if EmmaX.Loc == bg_current:
                                            if EmmaX.Action and multi_action:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ EmmaX.Action -= 1
                                            else:
                                                ch_e "I'm actually getting a little tired, perhaps we could wrap this up?"

                                    "Threesome actions (locked)" if not Partner or "unseen" in EmmaX.recent_history or EmmaX.Loc != bg_current:
                                        pass
                                    "Threesome actions" if Partner and "unseen" not in EmmaX.recent_history and EmmaX.Loc == bg_current:
                                        menu:
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(EmmaX)
                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(EmmaX)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Emma_M_Cycle
                                            "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_M_Cycle
                                            "Never mind":
                                                        jump Emma_M_Cycle

                                    "Show her feet" if not ShowFeet and EmmaX.Pose == "doggy":
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and EmmaX.Pose == "doggy":
                                            $ ShowFeet = 0

                                    "Undress [EmmaX.name]":
                                            if "unseen" in EmmaX.recent_history:
                                                    ch_p "Oh, yeah, take it off. . ."
                                                    jump Emma_M_Interupted
                                            else:
                                                    call Girl_Undress(EmmaX)
                                    "Clean up [EmmaX.name] (locked)" if not EmmaX.Spunk:
                                            pass
                                    "Clean up [EmmaX.name]" if EmmaX.Spunk:
                                            if "unseen" in EmmaX.recent_history:
                                                    ch_p "You've got a little something on you. . ."
                                                    jump Emma_M_Interupted
                                            else:
                                                    call Girl_Cleanup(EmmaX,"ask")
                                    "Never mind":
                                            jump Emma_M_Cycle

                        "Back to Sex Menu" if multi_action and EmmaX.Loc == bg_current:
                                    ch_p "Let's try something else."
                                    call reset_position(EmmaX)
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Emma_M_Interupted
                        "End Scene" if not multi_action or EmmaX.Loc != bg_current:
                                    ch_p "Let's stop for now."
                                    call reset_position(EmmaX)
                                    $ line = 0
                                    jump Emma_M_Interupted
        #End menu (if line)

        call Shift_Focus(EmmaX)
        call Sex_Dialog(EmmaX,Partner)

        #If either of you could cum

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up

        if Player.Focus >= 100 or EmmaX.lust >= 100:
                    #If you can cum:
                    if Player.Focus >= 100:
                        if "unseen" not in EmmaX.recent_history:
                            #if she knows you're there
                            call Player_Cumming(EmmaX)
                            if "angry" in EmmaX.recent_history:
                                call reset_position(EmmaX)
                                return
                            $ EmmaX.change_stat("lust", 200, 5)
                            if 100 > EmmaX.lust >= 70 and EmmaX.OCount < 2:
                                $ EmmaX.recent_history.append("unsatisfied")
                                $ EmmaX.daily_history.append("unsatisfied")
                            $ line = "came"
                        else: #If she wasn't aware you were there
                            "You grunt and try to hold it in."
                            $ Player.Focus = 95
                            if EmmaX.Loc == bg_current or EmmaX.Loc == "bg_desk":
                                    jump Emma_M_Interupted

                    #If [EmmaX.name] can cum
                    if EmmaX.lust >= 100:
                        call Girl_Cumming(EmmaX)
                        if EmmaX.Loc == bg_current or EmmaX.Loc == "bg_desk":
                                jump Emma_M_Interupted

                    if line == "came":
                        $ line = 0
                        if not Player.Semen:
                            "You're emptied out, you should probably take a break."
                            $ offhand_action = 0 if offhand_action == "jackin" else offhand_action


                        if "unsatisfied" in EmmaX.recent_history:#And [EmmaX.name] is unsatisfied,
                            "[EmmaX.name] still seems a bit unsatisfied with the experience."
                            menu:
                                "Let her keep going?"
                                "Yes, keep going for a bit.":
                                    $ line = "You let her get back into it"
                                    jump Emma_M_Cycle
                                "No, I'm done.":
                                    "You ask her to stop."
                                    return
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        if "unseen" in EmmaX.recent_history:
                if Round == 10:
                    "It's getting a bit late, [EmmaX.name] will probably be wrapping up soon."
                elif Round == 5:
                    "She's definitely going to stop soon."
        else:
                if EmmaX.Loc == bg_current:
                        call Escalation(EmmaX) #sees if she wants to escalate things

                if Round == 10:
                    ch_e "I think I'll probably take a break soon."
                    $ EmmaX.lust += 10
                elif Round == 5:
                    ch_e "Ung, I'm almost finished. . ."
                    $ EmmaX.lust += 25

    #Round = 0 loop breaks
    $ EmmaX.change_face("bemused", 0)
    $ line = 0
    if "unseen" not in EmmaX.recent_history:
        ch_e "That's probably enough of that."

label Emma_M_Interupted:

    # If she hasn't noticed you're there before cumming
    if "unseen" in EmmaX.recent_history:
                $ EmmaX.change_face("surprised", 2)
                "[EmmaX.name] stops what she's doing with a start, eyes wide."
                call Emma_First_Bottomless(1)
                $ EmmaX.change_face("confused", 1, Eyes="surprised")
                if EmmaX.Loc == "bg_desk":
                        $ EmmaX.Loc = bg_current
                        call Display_Girl(EmmaX)
                        "She approaches you."

                #If you've been jacking it
                if offhand_action == "jackin":
                        ch_e "!"
                        ch_e "How long have you been there?!"
                        $ EmmaX.Eyes = "down"
                        menu:
                            ch_e "And I see you've been busy. . . "
                            "A little while, it was an excellent show.":
                                    $ EmmaX.change_face("sexy",1)
                                    $ EmmaX.change_stat("obedience", 50, 3)
                                    $ EmmaX.change_stat("obedience", 70, 2)
                                    ch_e "Well, obviously. . ."
                                    if EmmaX.love >= 800 or EmmaX.obedience >= 500 or EmmaX.inhibition >= 500:
                                        $ temp_modifier += 10
                                        $ EmmaX.change_stat("lust", 90, 5)
                                    ch_e "and I suppose you bring a lot to the table as well, don't you. . ."

                            "I. . . just got here?":
                                    $ EmmaX.change_face("angry",1, Eyes="down")
                                    $ EmmaX.change_stat("love", 70, 2)
                                    $ EmmaX.change_stat("love", 90, 1)
                                    $ EmmaX.change_stat("obedience", 50, 2)
                                    $ EmmaX.change_stat("obedience", 70, 2)
                                    "She looks pointedly at your cock,"
                                    $ EmmaX.Eyes = "squint"
                                    ch_e "Long enough to raise your sails?"
                                    if EmmaX.love >= 800 or EmmaX.obedience >= 500 or EmmaX.inhibition >= 500:
                                            $ temp_modifier += 10
                                            $ EmmaX.change_stat("lust", 90, 5)
                                            $ EmmaX.change_face("bemused", 1)
                                            ch_e "I suppose you couldn't help yourself under the circumstances. . ."
                                    else:
                                            $ temp_modifier -= 10
                                            $ EmmaX.change_stat("lust", 200, -5)

                        if "Historia" not in Player.Traits:
                                    call Seen_First_Peen(EmmaX,Partner)
                                    ch_e "Hmm. . ."

                #you haven't been jacking it
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

                $ EmmaX.DrainWord("unseen",1,0) #She sees you, so remove unseens
                $ EmmaX.Mast += 1
                if "classcaught" not in EmmaX.History or "Historia" in Player.Traits:
                    # this activates if it's the first time in class
                    return
                if Round <= 10:
                    ch_e "Unfortunately it's getting rather late."
                    return
                $ action_context = "join"
                call Emma_Masturbate
                "error: report this if you see it."
                return #should be redundant
    #End Unseen

    #else, if She's seen you already
    $ EmmaX.Action -= 1
    $ EmmaX.Mast += 1
    call Checkout
    if action_context == "shift":
        $ action_context = 0
        return
    $ action_context = 0

    if Partner == "Kitty":
        call Partner_Like(EmmaX,4,2)
    else:
        call Partner_Like(EmmaX,3,2)

    if EmmaX.Loc != bg_current and EmmaX.Loc != "bg_desk":
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
        "Well, I have something you could take care of. . ." if Player.Semen and EmmaX.Action and multi_action:
                $ action_context = "shift"
                return
        "You could just keep going. . ." if Player.Semen:
                $ EmmaX.change_face("sly")
                if EmmaX.Action and Round >= 10:
                    ch_e "I suppose. . ."
                    jump Emma_M_Cycle
                else:
                    ch_e "Gimme a minute, I need to collect myself here. . ."
        "I'm good here. [[Stop]":
                if EmmaX.love < 800 and EmmaX.inhibition < 500 and EmmaX.obedience < 500:
                    $ EmmaX.OutfitChange()
                $ EmmaX.change_face("normal")
                $ EmmaX.Brows = "confused"
                ch_e "Well. . . yes. . ."
                $ EmmaX.Brows = "normal"
        "You should probably stop for now." if EmmaX.lust > 30:
                $ EmmaX.change_face("angry")
                ch_e "I . . . yes . ."
    if offhand_action == "jackin":
        $ offhand_action = 0
    return

## end EmmaX.Masturbating ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Start [EmmaX.name] Sex pose //////////////////////////////////////////////////////////////////////////////////
# EmmaX.Sex_P //////////////////////////////////////////////////////////////////////

label Emma_Sex_P:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(EmmaX)
    if EmmaX.Sex >= 7: # She loves it
        $ temp_modifier += 15
    elif EmmaX.Sex >= 3: #You've done it before several times
        $ temp_modifier += 12
    elif EmmaX.Sex: #You've done it before
        $ temp_modifier += 10

    if EmmaX.Addict >= 75 and (EmmaX.CreamP + EmmaX.CreamA) >=3: #She's really strung out and has creampied
        $ temp_modifier += 20
    elif EmmaX.Addict >= 75:
        $ temp_modifier += 15

    if EmmaX.lust > 85:
        $ temp_modifier += 10
    elif EmmaX.lust > 75: #She's really horny
        $ temp_modifier += 5

    if action_context == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in EmmaX.Traits:
        $ temp_modifier += (4*Taboo)
    if EmmaX in Player.Harem or "sex friend" in EmmaX.Petnames:
        $ temp_modifier += 10
    elif "ex" in EmmaX.Traits:
        $ temp_modifier -= 40
    if EmmaX.ForcedCount and not EmmaX.Forced:
        $ temp_modifier -= 5 * EmmaX.ForcedCount



    if Taboo and "tabno" in EmmaX.daily_history:
        $ temp_modifier -= 10

    if "no sex" in EmmaX.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no sex" in EmmaX.recent_history else 0


    $ Approval = ApprovalCheck(EmmaX, 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)

    if action_context == "auto":
                call Emma_Sex_Launch("sex")
                if EmmaX.wearing_skirt:
                    "You roll back, pulling [EmmaX.name] on top of you, sliding her skirt up as you go."
                    $ EmmaX.Upskirt = 1
                elif EmmaX.PantsNum() >= 6:
                    "You roll back, pulling [EmmaX.name] on top of you, sliding her [EmmaX.Legs] down as you do."
                    $ EmmaX.Legs = 0
                else:
                    "You roll back, pulling [EmmaX.name] on top of you."
                $ EmmaX.SeenPanties = 1
                "You rub the tip of your cock against her moist slit."
                $ EmmaX.change_face("surprised", 1)

                if (EmmaX.Sex and Approval) or (Approval > 1):
                    #this is not the first time you've had sex, or she's into it
                    "[EmmaX.name] is briefly startled, but melts into a sly smile."
                    $ EmmaX.change_face("sly")
                    $ EmmaX.change_stat("obedience", 70, 3)
                    $ EmmaX.change_stat("inhibition", 50, 3)
                    $ EmmaX.change_stat("inhibition", 70, 1)
                    ch_e "Mmm, if you insist, [EmmaX.Petname]."
                    jump Emma_SexPrep
                else:
                    #she's questioning it
                    $ EmmaX.Brows = "angry"
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
                                    if EmmaX.Sex:
                                        ch_e "Perhaps ask first, [EmmaX.Petname]."
                                    else:
                                        ch_e "Perhaps some other time, when you ask nicely."
                        "Just fucking.":
                            $ EmmaX.change_stat("love", 80, -10, 1)
                            $ EmmaX.change_stat("love", 200, -10)
                            "You press inside some more."
                            $ EmmaX.change_stat("obedience", 70, 3)
                            $ EmmaX.change_stat("inhibition", 50, 3)
                            if not ApprovalCheck(EmmaX, 700, "O", TabM=1):   #Checks if obedience is 700+
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
    #End Auto


    if not EmmaX.Sex and "no sex" not in EmmaX.recent_history:
            #first time
            $ EmmaX.change_face("surprised", 1)
            $ EmmaX.Mouth = "kiss"
            ch_e "Hmm, are you sure you're really prepared for this? . . "
            if EmmaX.Forced:
                $ EmmaX.change_face("sad")
                ch_e "Are you sure this is how you'd like to use your. . . influence?"


    if not EmmaX.Sex and Approval:
            #First time dialog
            if EmmaX.Forced:
                $ EmmaX.change_face("sad")
                $ EmmaX.change_stat("love", 70, -30, 1)
                $ EmmaX.change_stat("love", 20, -20, 1)
            elif EmmaX.love >= (EmmaX.obedience + EmmaX.inhibition):
                $ EmmaX.change_face("sexy")
                $ EmmaX.Brows = "sad"
                $ EmmaX.Mouth = "smile"
                ch_e "I wouldn't want you to get hurt. . ."
            elif EmmaX.obedience >= EmmaX.inhibition:
                $ EmmaX.change_face("normal")
                ch_e "If you insist, [EmmaX.Petname]. . ."
            elif EmmaX.Addict >= 50:
                $ EmmaX.change_face("manic", 1)
                ch_e "I was wondering how it would feel with you. . ."
            else: # Uninhibited
                $ EmmaX.change_face("sad")
                $ EmmaX.Mouth = "smile"
                ch_e "I was hoping you'd ask. . ."
            #End first time dialog

    elif Approval:
            #Second time+ dialog
            $ EmmaX.change_face("sexy", 1)
            if EmmaX.Forced:
                $ EmmaX.change_face("sad")
                $ EmmaX.change_stat("love", 70, -3, 1)
                $ EmmaX.change_stat("love", 20, -2, 1)
                ch_e "Again? You're really wearing out your welcome."
            elif not Taboo and "tabno" in EmmaX.daily_history:
                ch_e "I suppose this is more private."
            elif "sex" in EmmaX.recent_history:
                ch_e "Again? [EmmaX.Petname], you're insatiable!"
                jump Emma_SexPrep
            elif "sex" in EmmaX.daily_history:
                $ line = renpy.random.choice(["Back again?",
                    "You'd like another round?",
                    "I suppose I am irresistible. . .",
                    "Didn't get enough earlier?",
                    "You're wearing me out, " + EmmaX.Petname + "."])
                ch_e "[line]"
            elif EmmaX.Sex < 3:
                $ EmmaX.Brows = "confused"
                $ EmmaX.Mouth = "kiss"
                ch_e "Oh? Another round?"
            else:
                $ line = renpy.random.choice(["Oh, you want some of this?",
                    "You'd like another round?",
                    "I suppose I am irresistible. . .",
                    "Do you intend to make me melt?",
                    "You want me to ride you?"])
                ch_e "[line]"
            $ line = 0
            #end Second time+ dialog

    if Approval >= 2:
            #She's into it. . .
            if EmmaX.Forced:
                $ EmmaX.change_face("sad")
                $ EmmaX.change_stat("obedience", 90, 1)
                $ EmmaX.change_stat("inhibition", 60, 1)
                ch_e "Oh, fine, if it will shut you up."
            elif "no sex" in EmmaX.daily_history:
                ch_e "Very well, you've convinced me. . ."
            else:
                $ EmmaX.change_face("sexy", 1)
                $ EmmaX.change_stat("love", 90, 1)
                $ EmmaX.change_stat("inhibition", 50, 3)
                $ line = renpy.random.choice(["Well. . . fine, I accept.",
                    "Sure!",
                    "We could, I suppose.",
                    "Hmmm, yes.",
                    "How could I refuse?"])
                ch_e "[line]"
                $ line = 0
            $ EmmaX.change_stat("obedience", 20, 1)
            $ EmmaX.change_stat("obedience", 60, 1)
            $ EmmaX.change_stat("inhibition", 70, 2)
            jump Emma_SexPrep

    else:
            #She's not into it, but maybe. . .
            $ EmmaX.change_face("angry")
            if "no sex" in EmmaX.recent_history:
                ch_e "I'm afraid that \"no\" is my final answer, [EmmaX.Petname]."
            elif Taboo and "tabno" in EmmaX.daily_history and "no sex" in EmmaX.daily_history:
                ch_e "I already told you. . .not in such an exposed location."
            elif "no sex" in EmmaX.daily_history:
                ch_e "I believe I just told you \"no,\" [EmmaX.Petname]."
            elif Taboo and "tabno" in EmmaX.daily_history:
                ch_e "I already told you this is too public!"
            elif not EmmaX.Sex:
                $ EmmaX.change_face("bemused")
                ch_e "I really doubt you understand what you're in for. . ."
            else:
                $ EmmaX.change_face("bemused")
                ch_e "Perhaps another time would be better? . ."
            menu:
                extend ""
                "Sorry, never mind." if "no sex" in EmmaX.daily_history:
                        $ EmmaX.change_face("bemused")
                        ch_e "I can appreciate your. . . drive."
                        return
                "Maybe later?" if "no sex" not in EmmaX.daily_history:
                        $ EmmaX.change_face("sexy")
                        ch_e "Oh, most certainly. . ."
                        $ EmmaX.change_stat("love", 80, 2)
                        $ EmmaX.change_stat("inhibition", 70, 2)
                        if Taboo:
                            $ EmmaX.recent_history.append("tabno")
                            $ EmmaX.daily_history.append("tabno")
                        $ EmmaX.recent_history.append("no sex")
                        $ EmmaX.daily_history.append("no sex")
                        return
                "I think you'd enjoy it as much as I would. . .":
                        if Approval:
                            $ EmmaX.change_face("sexy")
                            $ EmmaX.change_stat("obedience", 90, 2)
                            $ EmmaX.change_stat("obedience", 50, 2)
                            $ EmmaX.change_stat("inhibition", 70, 3)
                            $ EmmaX.change_stat("inhibition", 40, 2)
                            $ line = renpy.random.choice(["I can't exactly argue with that. . .",
                                "I suppose. . .",
                                "You raise a good point. . ."])
                            ch_e "[line]"
                            $ line = 0
                            jump Emma_SexPrep
                "Just deal with it.":                                               # Pressured into it
                        $ Approval = ApprovalCheck(EmmaX, 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
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
                #end menu
    #end Approval check

    #She refused all offers.
    $ EmmaX.ArmPose = 1
    if "no sex" in EmmaX.daily_history:
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
    elif Taboo:                             # she refuses and this is too public a place for her
        $ EmmaX.change_face("angry", 1)
        $ EmmaX.recent_history.append("tabno")
        $ EmmaX.daily_history.append("tabno")
        ch_e "How can you imagine this would be an appropriate location?"
        $ EmmaX.change_stat("lust", 200, 5)
        $ EmmaX.change_stat("obedience", 50, -3)
    elif EmmaX.Sex:
        $ EmmaX.change_face("sad")
        ch_e "I'm sure you can figure out how to take care of that yourself."
    else:
        $ EmmaX.change_face("normal", 1)
        ch_e "I'm afraid not."
    $ EmmaX.recent_history.append("no sex")
    $ EmmaX.daily_history.append("no sex")
    $ temp_modifier = 0
    return

label Emma_Sex_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(EmmaX)
        call Emma_Sex_Launch("sex")
        $ action_speed = 2 if action_speed >= 4 else action_speed
        $ EmmaX.lustFace()
        $ Player.Cock = "in"
        $ primary_action = "sex"
        $ EmmaX.Upskirt = 1
        $ EmmaX.PantiesDown = 1

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
                                    call Slap_Ass(EmmaX)
                                    $ counter += 1
                                    $ Round -= 1
                                    jump Emma_Sex_Cycle

                        "Turn her Around":
                                    $ EmmaX.Pose = "doggy" if EmmaX.Pose != "doggy" else "sex"
                                    "You turn her around. . ."
                                    jump Emma_Sex_Cycle

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
                                            if EmmaX.Action and multi_action:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ EmmaX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(EmmaX,"tired")

                                    "Shift primary action":
                                            if EmmaX.Action and multi_action:
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
                                                call Sex_Basic_Dialog(EmmaX,"tired")
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [EmmaX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(EmmaX)
                                            "Asks [EmmaX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(EmmaX)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(EmmaX)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Emma_Sex_Cycle
                                            "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_Sex_Cycle
                                            "Never mind":
                                                        jump Emma_Sex_Cycle
                                    "Just take a look at her.":
                                            $ Player.Cock = 0
                                            $ action_speed = 0

                                    "Show her feet" if not ShowFeet and EmmaX.Pose == "doggy":
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and EmmaX.Pose == "doggy":
                                            $ ShowFeet = 0

                                    "Undress [EmmaX.name]":
                                            call Girl_Undress(EmmaX)
                                    "Clean up [EmmaX.name] (locked)" if not EmmaX.Spunk:
                                            pass
                                    "Clean up [EmmaX.name]" if EmmaX.Spunk:
                                            call Girl_Cleanup(EmmaX,"ask")
                                    "Never mind":
                                            jump Emma_Sex_Cycle

                        "Back to Sex Menu" if multi_action:
                                    ch_p "Let's try something else."
                                    call Emma_Sex_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Emma_SexAfter
                        "End Scene" if not multi_action:
                                    ch_p "Let's stop for now."
                                    call Emma_Sex_Reset
                                    $ line = 0
                                    jump Emma_SexAfter
        #End menu (if line)

        call Shift_Focus(EmmaX)
        call Sex_Dialog(EmmaX,Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or EmmaX.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(EmmaX)
                            if "angry" in EmmaX.recent_history:
                                call Emma_Sex_Reset
                                return
                            $ EmmaX.change_stat("lust", 200, 5)
                            if 100 > EmmaX.lust >= 70 and EmmaX.OCount < 2:
                                    $ EmmaX.recent_history.append("unsatisfied")
                                    $ EmmaX.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Emma_SexAfter
                            $ line = "came"

                    if EmmaX.lust >= 100:
                            #If you're still going at it and [EmmaX.name] can cum
                            call Girl_Cumming(EmmaX)
                            if action_context == "shift" or "angry" in EmmaX.recent_history:
                                jump Emma_SexAfter

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Emma_SexAfter
                            elif "unsatisfied" in EmmaX.recent_history:
                                #And [EmmaX.name] is unsatisfied,
                                $ line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ line = "You get back into it"
                                        jump Emma_Sex_Cycle
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Emma_SexAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Emma_SexAfter
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif counter == (5 + EmmaX.Sex):
                    $ EmmaX.Brows = "confused"
                    ch_e "So are we getting close?"
        elif counter == (10 + EmmaX.Sex):
                    $ EmmaX.Brows = "angry"
                    ch_e "I'm . . .getting . . a bit. . . tired. . . here. . ."
                    menu:
                        ch_e "Could we. . . do something. . . else?"
                        "How about a BJ?" if EmmaX.Action and multi_action:
                                $ action_context = "shift"
                                call Emma_SexAfter
                                call Emma_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ counter += 1
                                jump Emma_Sex_Cycle
                        "Let's try something else." if multi_action:
                                $ line = 0
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
        #End Count check

        call Escalation(EmmaX) #sees if she wants to escalate things

        if Round == 10:
            ch_e "You might want to think about your endgame here. . ."
        elif Round == 5:
            ch_e "We'll need a break soon."

    #Round = 0 loop breaks
    $ EmmaX.change_face("bemused", 0)
    $ line = 0
    ch_e "Ok, [EmmaX.Petname], that's enough of that for now."

# [EmmaX.name] anal //////////////////////////////////////////////////////////////////////

label Emma_Sex_A:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(EmmaX)
    if EmmaX.Anal >= 7: # She loves it
        $ temp_modifier += 20
    elif EmmaX.Anal >= 3: #You've done it before several times
        $ temp_modifier += 17
    elif EmmaX.Anal: #You've done it before
        $ temp_modifier += 15

    if EmmaX.Addict >= 75 and (EmmaX.CreamP + EmmaX.CreamA) >=3: #She's really strung out and has creampied
        $ temp_modifier += 25
    elif EmmaX.Addict >= 75:
        $ temp_modifier += 15

    if EmmaX.lust > 85:
        $ temp_modifier += 10
    elif EmmaX.lust > 75: #She's really horny
        $ temp_modifier += 5

    $ temp_modifier += 10  # she starts out loose

    if action_context == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in EmmaX.Traits:
        $ temp_modifier += (5*Taboo)

    if EmmaX in Player.Harem or "sex friend" in EmmaX.Petnames:
        $ temp_modifier += 10
    elif "ex" in EmmaX.Traits:
        $ temp_modifier -= 40
    if EmmaX.ForcedCount and not EmmaX.Forced:
        $ temp_modifier -= 5 * EmmaX.ForcedCount

    if Taboo and "tabno" in EmmaX.daily_history:
        $ temp_modifier -= 10
    if "no anal" in EmmaX.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no anal" in EmmaX.recent_history else 0

    $ Approval = ApprovalCheck(EmmaX, 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)

    if action_context == "auto":
            call Emma_Sex_Launch("anal")
            if EmmaX.wearing_skirt:
                "You roll back, pulling [EmmaX.name] on top of you, sliding her skirt up as you go."
                $ EmmaX.Upskirt = 1
            elif EmmaX.PantsNum() >= 6:
                "You roll back, pulling [EmmaX.name] on top of you, sliding her [EmmaX.Legs] down as you do."
                $ EmmaX.Legs = 0
            else:
                "You roll back, pulling [EmmaX.name] on top of you."
            $ EmmaX.SeenPanties = 1
            "You press the tip of your cock against her tight rim."
            $ EmmaX.change_face("surprised", 1)

            if (EmmaX.Anal and Approval) or (Approval > 1):
                #this is not the first time you've had sex, or she's into it
                $ EmmaX.change_stat("obedience", 70, 3)
                $ EmmaX.change_stat("inhibition", 50, 3)
                $ EmmaX.change_stat("inhibition", 70, 1)
                "[EmmaX.name] is briefly startled, but melts into a sly smile."
                ch_e "Oooh, naughty boy. . ."
                jump Emma_AnalPrep
            else:
                #she's questioning it
                $ EmmaX.Brows = "angry"
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

                        if EmmaX.Anal:
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
            #end "auto"


    if not EmmaX.Anal and "no anal" not in EmmaX.recent_history:
            #first time
            $ EmmaX.change_face("surprised", 1)
            $ EmmaX.Mouth = "kiss"
            ch_e "Oooh, naughty boy. Anal?"

            if EmmaX.Forced:
                $ EmmaX.change_face("sad")
                ch_e "Anal? That's your goto?"

    if "anal" in EmmaX.recent_history:
            $ EmmaX.change_face("sexy", 1)
            ch_e "Alright."
            jump Emma_AnalPrep


    if not EmmaX.Anal and Approval:
            #First time dialog
            if EmmaX.Forced:
                $ EmmaX.change_face("sad")
                $ EmmaX.change_stat("love", 70, -3, 1)
                $ EmmaX.change_stat("love", 20, -2, 1)
            elif EmmaX.love >= (EmmaX.obedience + EmmaX.inhibition):
                $ EmmaX.change_face("sexy")
                $ EmmaX.Brows = "sad"
                $ EmmaX.Mouth = "smile"
                ch_e "I was wondering when you'd ask. . ."
            elif EmmaX.obedience >= EmmaX.inhibition:
                $ EmmaX.change_face("normal")
                ch_e "I expected we'd get here at some point. . ."
            elif EmmaX.Addict >= 50:
                $ EmmaX.change_face("manic", 1)
                ch_e "Hmm, that would be an interesting experience. . ."
            else: # Uninhibited
                $ EmmaX.change_face("sad")
                $ EmmaX.Mouth = "smile"
                ch_e "I was getting tired of waiting. . ."

    elif Approval:
            #Second time+ dialog
            if EmmaX.Forced:
                $ EmmaX.change_face("sad")
                $ EmmaX.change_stat("love", 70, -3, 1)
                $ EmmaX.change_stat("love", 20, -2, 1)
                ch_e "You don't hold back. . ."
            elif not Taboo and "tabno" in EmmaX.daily_history:
                ch_e "I suppose this is secluded enough. . ."
            elif "anal" in EmmaX.daily_history and not EmmaX.Loose:
                pass
            elif "anal" in EmmaX.recent_history:
                ch_e "I am warmed up. . ."
                jump Emma_AnalPrep
            elif "anal" in EmmaX.daily_history:
                $ EmmaX.change_face("sexy", 1)
                $ line = renpy.random.choice(["Back again so soon?",
                    "So you'd like another round?",
                    "I'm still a little sore from earlier.",
                    "Didn't get enough earlier?",
                    "You're wearing me out, " + EmmaX.Petname + "."])
                ch_e "[line]"
            else:
                $ EmmaX.change_face("sexy", 1)
                $ EmmaX.ArmPose = 2
                $ line = renpy.random.choice(["Oooh, you want some of this?",
                    "So you'd like another round?",
                    "I knew you enjoyed it. . .",
                    "Do you intend to make me melt?",
                    "You want me to ride you?"])
                ch_e "[line]"
            $ line = 0

    if Approval >= 2:
            #She's into it. . .
            if EmmaX.Forced:
                $ EmmaX.change_face("sad")
                $ EmmaX.change_stat("obedience", 90, 1)
                $ EmmaX.change_stat("inhibition", 60, 1)
                ch_e "Oh very well."
            elif "no anal" in EmmaX.daily_history:
                ch_e "After some consideration. . ."
                ch_e "It might be entertaining."
            else:
                $ EmmaX.change_face("sexy", 1)
                $ EmmaX.change_stat("love", 90, 1)
                $ EmmaX.change_stat("inhibition", 50, 3)
                $ line = renpy.random.choice(["Well. . . ok.",
                    "Sure!",
                    "You could, I guess.",
                    "Um, yeah.",
                    "Heh, ok, ok."])
                ch_e "[line]"
                $ line = 0
            $ EmmaX.change_stat("obedience", 20, 1)
            $ EmmaX.change_stat("obedience", 60, 1)
            $ EmmaX.change_stat("inhibition", 70, 2)
            jump Emma_AnalPrep

    else:
            #She's not into it, but maybe. . .
            $ EmmaX.change_face("angry")
            if "no anal" in EmmaX.recent_history:
                ch_e "I'm afraid that \"no\" is my final answer, [EmmaX.Petname]."
            elif Taboo and "tabno" in EmmaX.daily_history and "no anal" in EmmaX.daily_history:
                ch_e "I already told you. . .not in such an exposed location."
            elif "no anal" in EmmaX.daily_history:
                ch_e "I believe I just told you \"no,\" [EmmaX.Petname]."
            elif Taboo and "tabno" in EmmaX.daily_history:
                ch_e "I already told you this is too public!"
            elif not EmmaX.Anal:
                $ EmmaX.change_face("bemused")
                ch_e "I don't know that you're ready for that yet."
            else:
                $ EmmaX.change_face("bemused")
                ch_e "Perhaps we can work up to that."
            menu:
                extend ""
                "Sorry, never mind." if "no anal" in EmmaX.daily_history:
                    $ EmmaX.change_face("bemused")
                    ch_e "I don't blame you for your. . . enthusiasm."
                    return
                "Maybe later?" if "no anal" not in EmmaX.daily_history:
                    $ EmmaX.change_face("sexy")
                    ch_e "I imagine we will. . ."
                    ch_e ". . . often."
                    $ EmmaX.change_stat("love", 80, 2)
                    $ EmmaX.change_stat("inhibition", 70, 2)
                    if Taboo:
                        $ EmmaX.recent_history.append("tabno")
                        $ EmmaX.daily_history.append("tabno")
                    $ EmmaX.recent_history.append("no anal")
                    $ EmmaX.daily_history.append("no anal")
                    return
                "I bet it would feel really good. . .":
                    if Approval:
                        $ EmmaX.change_face("sexy")
                        $ EmmaX.change_stat("obedience", 90, 2)
                        $ EmmaX.change_stat("obedience", 50, 2)
                        $ EmmaX.change_stat("inhibition", 70, 3)
                        $ EmmaX.change_stat("inhibition", 40, 2)
                        $ line = renpy.random.choice(["I can't exactly argue with that. . .",
                                "I suppose. . .",
                                "You raise a good point. . ."])
                        ch_e "[line]"
                        $ line = 0
                        jump Emma_AnalPrep
                    else:
                        pass

                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(EmmaX, 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
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

    #She refused all offers.
    $ EmmaX.ArmPose = 1
    if "no anal" in EmmaX.daily_history:
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
        # she refuses and this is too public a place for her
        $ EmmaX.change_face("angry", 1)
        $ EmmaX.recent_history.append("tabno")
        $ EmmaX.daily_history.append("tabno")
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
    elif EmmaX.Anal:
        $ EmmaX.change_face("sad")
        ch_e "You'll have to show me you're worth it again."
    else:
        $ EmmaX.change_face("normal", 1)
        ch_e "I don't think you've earned that yet."
    $ EmmaX.recent_history.append("no anal")
    $ EmmaX.daily_history.append("no anal")
    $ temp_modifier = 0
    return

label Emma_AnalPrep:
    call Seen_First_Peen(EmmaX,Partner,React=action_context)
    call Emma_Sex_Launch("hotdog")

    if action_context == EmmaX:
            #Emma auto-starts
            $ action_context = 0
            if EmmaX.wearing_skirt:
                "[EmmaX.name] pushes you back and climbs on top of you, sliding her skirt up as she does so."
                $ EmmaX.Upskirt = 1
            elif EmmaX.PantsNum() >= 6:
                "[EmmaX.name] pushes you down and climbs on top of you, sliding her [EmmaX.Legs] down as she does so."
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
                    ch_p "Oh yeah, [EmmaX.Pet], let's do this."
                    $ EmmaX.nameCheck() #checks reaction to petname
                    "[EmmaX.name] slides it in."
                    $ EmmaX.change_stat("love", 85, 1)
                    $ EmmaX.change_stat("obedience", 90, 1)
                    $ EmmaX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ EmmaX.change_face("surprised")
                    $ EmmaX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that right now, [EmmaX.Pet]."
                    $ EmmaX.nameCheck() #checks reaction to petname
                    "[EmmaX.name] pulls back."
                    $ EmmaX.change_stat("obedience", 90, 1)
                    $ EmmaX.change_stat("obedience", 50, 1)
                    $ EmmaX.change_stat("obedience", 30, 2)
                    $ Player.recent_history.append("nope")
                    $ EmmaX.AddWord(1,"refused","refused")
                    return
            $ EmmaX.PantiesDown = 1
            call Emma_First_Bottomless(1)

    elif action_context != "auto":
        call AutoStrip(EmmaX)

        if Taboo: # [EmmaX.name] gets started. . .
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

    else: #if action_context == "auto"
        if (EmmaX.PantsNum() > 6 and not EmmaX.Upskirt) and (EmmaX.Panties and not EmmaX.PantiesDown):
            "You quickly pull down her pants and her [EmmaX.Panties] and press against her back door."
        elif (EmmaX.Panties and not EmmaX.PantiesDown):
            "You quickly pull down her [EmmaX.Panties] and press against her back door."
        $ EmmaX.Upskirt = 1
        $ EmmaX.PantiesDown = 1
        $ EmmaX.SeenPanties = 1
        call Emma_First_Bottomless(1)

    if not EmmaX.Anal:                                                      #First time stat buffs
        if EmmaX.Forced:
            $ EmmaX.change_stat("love", 90, -150)
            $ EmmaX.change_stat("obedience", 70, 70)
            $ EmmaX.change_stat("inhibition", 80, 40)
        else:
            $ EmmaX.change_stat("love", 90, 10)
            $ EmmaX.change_stat("obedience", 70, 30)
            $ EmmaX.change_stat("inhibition", 80, 70)
    elif not EmmaX.Loose:                                                   #first few times stat buffs
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
    $ line = 0
    $ counter = 0
    $ Player.Cock = "anal"
    $ primary_action = "anal"
    $ action_speed = 1
    if Taboo:
        $ EmmaX.DrainWord("tabno")
    $ EmmaX.DrainWord("no anal")
    $ EmmaX.recent_history.append("anal")
    $ EmmaX.daily_history.append("anal")

label Emma_Anal_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(EmmaX)
        call Emma_Sex_Launch("anal")
        $ action_speed = 2 if action_speed >= 4 else action_speed
        $ EmmaX.lustFace()
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
                                    call Slap_Ass(EmmaX)
                                    $ counter += 1
                                    $ Round -= 1
                                    jump Emma_Anal_Cycle

                        "Turn her Around":
                                    $ EmmaX.Pose = "doggy" if EmmaX.Pose != "doggy" else "sex"
                                    "You turn her around. . ."
                                    jump Emma_Anal_Cycle

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
                                            if EmmaX.Action and multi_action:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ EmmaX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(EmmaX,"tired")

                                    "Shift primary action":
                                            if EmmaX.Action and multi_action:
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
                                                call Sex_Basic_Dialog(EmmaX,"tired")
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [EmmaX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(EmmaX)
                                            "Asks [EmmaX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(EmmaX)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(EmmaX)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Emma_Anal_Cycle
                                            "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_Anal_Cycle
                                            "Never mind":
                                                        jump Emma_Anal_Cycle
                                    "Just take a look at her.":
                                            $ Player.Cock = 0
                                            $ action_speed = 0

                                    "Show her feet" if not ShowFeet and EmmaX.Pose == "doggy":
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and EmmaX.Pose == "doggy":
                                            $ ShowFeet = 0

                                    "Undress [EmmaX.name]":
                                            call Girl_Undress(EmmaX)
                                    "Clean up [EmmaX.name] (locked)" if not EmmaX.Spunk:
                                            pass
                                    "Clean up [EmmaX.name]" if EmmaX.Spunk:
                                            call Girl_Cleanup(EmmaX,"ask")
                                    "Never mind":
                                            jump Emma_Anal_Cycle

                        "Back to Sex Menu" if multi_action:
                                    ch_p "Let's try something else."
                                    call Emma_Sex_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Emma_AnalAfter
                        "End Scene" if not multi_action:
                                    ch_p "Let's stop for now."
                                    call Emma_Sex_Reset
                                    $ line = 0
                                    jump Emma_AnalAfter
        #End menu (if line)

        call Shift_Focus(EmmaX)
        call Sex_Dialog(EmmaX,Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or EmmaX.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(EmmaX)
                            if "angry" in EmmaX.recent_history:
                                call Emma_Sex_Reset
                                return
                            $ EmmaX.change_stat("lust", 200, 5)
                            if 100 > EmmaX.lust >= 70 and EmmaX.OCount < 2:
                                    $ EmmaX.recent_history.append("unsatisfied")
                                    $ EmmaX.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Emma_AnalAfter
                            $ line = "came"

                    if EmmaX.lust >= 100:
                            #If you're still going at it and [EmmaX.name] can cum
                            call Girl_Cumming(EmmaX)
                            if action_context == "shift" or "angry" in EmmaX.recent_history:
                                jump Emma_AnalAfter

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Emma_AnalAfter
                            elif "unsatisfied" in EmmaX.recent_history:
                                #And [EmmaX.name] is unsatisfied,
                                $ line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ line = "You get back into it"
                                        jump Emma_Anal_Cycle
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Emma_AnalAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Emma_AnalAfter
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif counter == (5 + EmmaX.Anal):
                    $ EmmaX.Brows = "confused"
                    ch_e "So are we getting close here?"
        elif counter == (10 + EmmaX.Anal):
                    $ EmmaX.Brows = "angry"
                    ch_e "I'm . . .getting . . a bit. . . tired. . . of this. . ."
                    menu:
                        ch_e "Can we. . . do something. . . else?"
                        "How about a BJ?" if EmmaX.Action and multi_action:
                                $ action_context = "shift"
                                call Emma_AnalAfter
                                call Emma_Blowjob
                        "How about a Handy?" if EmmaX.Action and multi_action:
                                $ action_context = "shift"
                                call Emma_AnalAfter
                                call Emma_Handjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ counter += 1
                                jump Emma_Anal_Cycle
                        "Let's try something else." if multi_action:
                                $ line = 0
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
        #End Count check

        if Round == 10:
            ch_e "You might want to think about your endgame here. . ."
        elif Round == 5:
            ch_e "We'll need a break soon."

    #Round = 0 loop breaks
    $ EmmaX.change_face("bemused", 0)
    $ line = 0
    ch_e "Ok, [EmmaX.Petname], that's enough of that for now."


# End [EmmaX.name] Anal //////////////////////////////////////////////////////////////////////////////////



# [EmmaX.name] hotdog //////////////////////////////////////////////////////////////////////

label Emma_Sex_H:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(EmmaX)
    if EmmaX.Hotdog >= 3: #You've done it before several times
        $ temp_modifier += 10
    elif EmmaX.Hotdog: #You've done it before
        $ temp_modifier += 5

    if EmmaX.lust > 85:
        $ temp_modifier += 10
    elif EmmaX.lust > 75: #She's really horny
        $ temp_modifier += 5
    if action_context == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in EmmaX.Traits:
        $ temp_modifier += (3*Taboo)
    if EmmaX in Player.Harem or "sex friend" in EmmaX.Petnames:
        $ temp_modifier += 10
    elif "ex" in EmmaX.Traits:
        $ temp_modifier -= 40
    if EmmaX.ForcedCount and not EmmaX.Forced:
        $ temp_modifier -= 5 * EmmaX.ForcedCount

    if Taboo and "tabno" in EmmaX.daily_history:
        $ temp_modifier -= 10

    if "no hotdog" in EmmaX.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no hotdog" in EmmaX.recent_history else 0

    $ Approval = ApprovalCheck(EmmaX, 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)

    if action_context == "auto":
            call Emma_Sex_Launch("hotdog")
            "You roll back, pulling [EmmaX.name] on top of you, and press your cock against her."
            $ EmmaX.change_face("surprised", 1)

            if (EmmaX.Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
                "[EmmaX.name] is briefly startled, but melts into a sly smile."
                $ EmmaX.change_face("sly")
                $ EmmaX.change_stat("obedience", 70, 3)
                $ EmmaX.change_stat("inhibition", 50, 3)
                $ EmmaX.change_stat("inhibition", 70, 1)
                ch_e "Now what shall we do with that . ."
                jump Emma_HotdogPrep
            else:                                                                                                            #she's questioning it
                $ EmmaX.Brows = "angry"
                menu:
                    ch_e "You might want to take a step back, [EmmaX.Petname]?"
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
                        if not ApprovalCheck(EmmaX, 500, "O", TabM=1): #Checks if obedience is 700+
                            $ EmmaX.change_face("angry")
                            "[EmmaX.name] shoves you away."
                            ch_e "Don't push your luck, [EmmaX.Petname]."
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
            #end auto


    if not EmmaX.Hotdog and "no hotdog" not in EmmaX.recent_history:
            #first time
            $ EmmaX.change_face("surprised", 1)
            $ EmmaX.Mouth = "kiss"
            ch_e "You just want me to grind against you then?"

            if EmmaX.Forced:
                $ EmmaX.change_face("sad")
                ch_e ". . . nothing more than that?"


    if not EmmaX.Hotdog and Approval:
            #First time dialog
            if EmmaX.Forced:
                $ EmmaX.change_face("sad")
                $ EmmaX.change_stat("love", 70, -3, 1)
                $ EmmaX.change_stat("love", 20, -2, 1)
            elif EmmaX.love >= (EmmaX.obedience + EmmaX.inhibition):
                $ EmmaX.change_face("sexy")
                $ EmmaX.Brows = "sad"
                $ EmmaX.Mouth = "smile"
                ch_e "I wouldn't want to leave you. . . unattended. . ."
            elif EmmaX.obedience >= EmmaX.inhibition:
                $ EmmaX.change_face("normal")
                ch_e "If that's what works for you. . ."
            elif EmmaX.Addict >= 50:
                $ EmmaX.change_face("manic", 1)
                ch_e "Hrmm. . ."
            else: # Uninhibited
                $ EmmaX.change_face("sad")
                $ EmmaX.Mouth = "smile"
                ch_e "Well if that's what gets you off. . ."

    elif Approval:
            #Second time+ dialog
            if EmmaX.Forced:
                $ EmmaX.change_face("sad")
                $ EmmaX.change_stat("love", 70, -3, 1)
                $ EmmaX.change_stat("love", 20, -2, 1)
                ch_e "Maybe that's going a bit too far. . ."
            elif not Taboo and "tabno" in EmmaX.daily_history:
                ch_e "I suppose this is a better location . ."
            elif "hotdog" in EmmaX.recent_history:
                $ EmmaX.change_face("sexy", 1)
                ch_e "Again? Oh, very well."
                jump Emma_HotdogPrep
            elif "hotdog" in EmmaX.daily_history:
                $ EmmaX.change_face("sexy", 1)
                $ line = renpy.random.choice(["Back again so soon?",
                    "So you'd like another round?",
                    "You're really into this. . .",
                    "Are you sure that's all you want?"])
                ch_e "[line]"
            else:
                $ EmmaX.change_face("sexy", 1)
                $ EmmaX.ArmPose = 2
                $ line = renpy.random.choice(["Oooh, you want some of this?",
                    "So you'd like another round?",
                    "You're really into this. . .",
                    "You want another rub?"])
                ch_e "[line]"
            $ line = 0

    if Approval >= 2:
            #She's into it. . .
            if EmmaX.Forced:
                $ EmmaX.change_face("sad")
                $ EmmaX.change_stat("obedience", 80, 1)
                $ EmmaX.change_stat("inhibition", 60, 1)
                ch_e "Ok, fine."
            elif "no hotdog" in EmmaX.daily_history:
                ch_e "It was rather entertaining. . ."
            else:
                $ EmmaX.change_face("sexy", 1)
                $ EmmaX.change_stat("love", 80, 1)
                $ EmmaX.change_stat("inhibition", 50, 2)
                $ line = renpy.random.choice(["Well, sure, let me give it a rub.",
                    "Very well.",
                    "Nice!",
                    "I suppose we could do that.",
                    "Allow me. . .",
                    "Heh, ok, ok."])
                ch_e "[line]"
                $ line = 0
            $ EmmaX.change_stat("obedience", 60, 1)
            $ EmmaX.change_stat("inhibition", 70, 2)
            jump Emma_HotdogPrep

    else:
            #She's not into it, but maybe. . .
            $ EmmaX.change_face("angry")
            if "no hotdog" in EmmaX.recent_history:
                ch_e "I'm afraid that \"no\" is my final answer, [EmmaX.Petname]."
            elif Taboo and "tabno" in EmmaX.daily_history and "no hotdog" in EmmaX.daily_history:
                ch_e "I just told you. . .not in such an exposed location."
            elif "no hotdog" in EmmaX.daily_history:
                ch_e "I believe I just told you \"no,\" [EmmaX.Petname]."
            elif Taboo and "tabno" in EmmaX.daily_history:
                ch_e "I already told you. . .not in such an exposed location."
            elif not EmmaX.Hotdog:
                $ EmmaX.change_face("bemused")
                ch_e "Hmm, that could be amusing, [EmmaX.Petname]. . ."
            else:
                $ EmmaX.change_face("bemused")
                ch_e "I don't think that would be appropriate. . ."
            menu:
                extend ""
                "Sorry, never mind." if "no hotdog" in EmmaX.daily_history:
                    $ EmmaX.change_face("bemused")
                    ch_e "No harm in asking. Once."
                    return
                "Maybe later?" if "no hotdog" not in EmmaX.daily_history:
                    $ EmmaX.change_face("sexy")
                    ch_e "I imagine it will happen at some point, [EmmaX.Petname]."
                    $ EmmaX.change_stat("love", 80, 1)
                    $ EmmaX.change_stat("inhibition", 50, 1)
                    if Taboo:
                        $ EmmaX.recent_history.append("tabno")
                        $ EmmaX.daily_history.append("tabno")
                    $ EmmaX.recent_history.append("no hotdog")
                    $ EmmaX.daily_history.append("no hotdog")
                    return
                "You might like it. . .":
                    if Approval:
                        $ EmmaX.change_face("sexy")
                        $ EmmaX.change_stat("obedience", 60, 2)
                        $ EmmaX.change_stat("inhibition", 50, 2)
                        $ line = renpy.random.choice(["I can't exactly argue with that. . .",
                                "I suppose. . .",
                                "You raise a good point. . ."])
                        ch_e "[line]"
                        $ line = 0
                        jump Emma_HotdogPrep
                    else:
                        pass

                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(EmmaX, 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
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

    #She refused all offers.
    $ EmmaX.ArmPose = 1

    if "no hotdog" in EmmaX.daily_history:
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
    elif Taboo:                             # she refuses and this is too public a place for her
        $ EmmaX.change_face("angry", 1)
        $ EmmaX.recent_history.append("tabno")
        $ EmmaX.daily_history.append("tabno")
        ch_e "This area is a bit too exposed for that sort of thing. . ."
        $ EmmaX.change_stat("lust", 200, 5)
        $ EmmaX.change_stat("obedience", 50, -3)
    elif EmmaX.Hotdog:
        $ EmmaX.change_face("sad")
        ch_e "Not under the circumstances."
    else:
        $ EmmaX.change_face("normal", 1)
        ch_e "No, thank you."
    $ EmmaX.recent_history.append("no hotdog")
    $ EmmaX.daily_history.append("no hotdog")
    $ temp_modifier = 0
    return

label Emma_Hotdog_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(EmmaX)
        call Emma_Sex_Launch("hotdog")
        $ action_speed = 2 if action_speed >= 4 else action_speed
        $ EmmaX.lustFace()
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
                                    call Slap_Ass(EmmaX)
                                    $ counter += 1
                                    $ Round -= 1
                                    jump Emma_Hotdog_Cycle

                        "Turn her Around":
                                    $ EmmaX.Pose = "doggy" if EmmaX.Pose != "doggy" else "sex"
                                    "You turn her around. . ."
                                    jump Emma_Hotdog_Cycle

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
                                            if EmmaX.Action and multi_action:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ EmmaX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(EmmaX,"tired")

                                    "Shift primary action":
                                            if EmmaX.Action and multi_action:
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
                                                call Sex_Basic_Dialog(EmmaX,"tired")
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [EmmaX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(EmmaX)
                                            "Asks [EmmaX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(EmmaX)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(EmmaX)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Emma_Hotdog_Cycle
                                            "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_Hotdog_Cycle
                                            "Never mind":
                                                        jump Emma_Hotdog_Cycle
                                    "Just take a look at her.":
                                            $ Player.Cock = 0
                                            $ action_speed = 0

                                    "Show her feet" if not ShowFeet and EmmaX.Pose == "doggy":
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and EmmaX.Pose == "doggy":
                                            $ ShowFeet = 0

                                    "Undress [EmmaX.name]":
                                            call Girl_Undress(EmmaX)
                                    "Clean up [EmmaX.name] (locked)" if not EmmaX.Spunk:
                                            pass
                                    "Clean up [EmmaX.name]" if EmmaX.Spunk:
                                            call Girl_Cleanup(EmmaX,"ask")
                                    "Never mind":
                                            jump Emma_Hotdog_Cycle

                        "Back to Sex Menu" if multi_action:
                                    ch_p "Let's try something else."
                                    call Emma_Sex_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Emma_HotdogAfter
                        "End Scene" if not multi_action:
                                    ch_p "Let's stop for now."
                                    call Emma_Sex_Reset
                                    $ line = 0
                                    jump Emma_HotdogAfter
        #End menu (if line)

        call Shift_Focus(EmmaX)
        call Sex_Dialog(EmmaX,Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or EmmaX.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(EmmaX)
                            if "angry" in EmmaX.recent_history:
                                call Emma_Sex_Reset
                                return
                            $ EmmaX.change_stat("lust", 200, 5)
                            if 100 > EmmaX.lust >= 70 and EmmaX.OCount < 2:
                                    $ EmmaX.recent_history.append("unsatisfied")
                                    $ EmmaX.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Emma_HotdogAfter
                            $ line = "came"

                    if EmmaX.lust >= 100:
                            #If you're still going at it and [EmmaX.name] can cum
                            call Girl_Cumming(EmmaX)
                            if action_context == "shift" or "angry" in EmmaX.recent_history:
                                jump Emma_HotdogAfter

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Emma_HotdogAfter
                            elif "unsatisfied" in EmmaX.recent_history:
                                #And [EmmaX.name] is unsatisfied,
                                $ line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ line = "You get back into it"
                                        jump Emma_Hotdog_Cycle
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Emma_HotdogAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Emma_HotdogAfter
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if EmmaX.SEXP >= 100 or ApprovalCheck(EmmaX, 1200, "LO"):
            pass
        elif counter == (5 + EmmaX.Hotdog):
                    $ EmmaX.Brows = "confused"
                    ch_e "Are we getting close here?"
        elif counter == (10 + EmmaX.Hotdog):
                    $ EmmaX.Brows = "angry"
                    menu:
                        ch_e "I'm a bit bored by this."
                        "How about a BJ?" if EmmaX.Action and multi_action:
                                $ action_context = "shift"
                                call Emma_HotdogAfter
                                call Emma_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ counter += 1
                                jump Emma_Hotdog_Cycle
                        "Let's try something else." if multi_action:
                                $ line = 0
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
        #End Count check

        call Escalation(EmmaX) #sees if she wants to escalate things

        if Round == 10:
            ch_e "You might want to think about your endgame here. . ."
        elif Round == 5:
            ch_e "We'll need a break soon."

    #Round = 0 loop breaks
    $ EmmaX.change_face("bemused", 0)
    $ line = 0
    ch_e "Ok, [EmmaX.Petname], that's enough of that for now."
