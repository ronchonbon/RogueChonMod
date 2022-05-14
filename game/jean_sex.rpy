# Jean_SexMenu //////////////////////////////////////////////////////////////////////
label Jean_SexAct(Act = 0):
        if AloneCheck(JeanX) and JeanX.Taboo == 20:
                $ JeanX.Taboo = 0
                $ Taboo = 0
        call Shift_Focus(JeanX)
        if Act == "SkipTo":
            $ renpy.pop_call() #causes it to skip past the primary_action Swap
            $ renpy.pop_call() #causes it to skip past the cycle you were in before
            #$ renpy.pop_call() #causes it to skip past the sex menu you were in before that
            call SkipTo(JeanX)
        elif Act == "switch":
            $ renpy.pop_call() #causes it to skip past call here from Sex_Menu_Threesome
            #$ renpy.pop_call() #causes it to skip past call to Sex_Menu_Threesome
            # drops through to sex menu
        elif Act == "masturbate":
            call Jean_M_Prep
            if not action_context:
                return
        elif Act == "lesbian":
            call Les_Prep(JeanX) #nee call Jean_Les_Prep
            if not action_context:
                return
        elif Act == "kissing":
            call KissPrep(JeanX)
            if not action_context:
                return
        elif Act == "breasts":
            call Jean_Fondle_Breasts
            if not action_context:
                return
        elif Act == "blow":
            call Jean_BJ_Prep
            if not action_context:
                return
        elif Act == "hand":
            call Jean_HJ_Prep
            if not action_context:
                return
        elif Act == "sex":
            call Jean_SexPrep
            if not action_context:
                return

##  JeanX.Masturbating //////////////////////////////////////////////////////////////////////
# counter 1 means she's seen you, counter 0 means she hasn't.
label Jean_Masturbate: #(action_context = action_context):
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JeanX)
    if JeanX.Mast:
        $ temp_modifier += 10
    if JeanX.SEXP >= 50:
        $ temp_modifier += 25
    elif JeanX.SEXP >= 30:
        $ temp_modifier += 15
    elif JeanX.SEXP >= 15:
        $ temp_modifier += 5
    if JeanX.lust >= 90:
        $ temp_modifier += 20
    elif JeanX.lust >= 75:
        $ temp_modifier += 5
    if "exhibitionist" in JeanX.Traits:
        $ temp_modifier += (3*Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JeanX.Traits:
        $ temp_modifier -= 40
    if JeanX.ForcedCount and not JeanX.Forced:
        $ temp_modifier -= 5 * JeanX.ForcedCount

    $ Approval = ApprovalCheck(JeanX, 1300, TabM = 2) # 120, 135, 150, Taboo -80(200)

    $ JeanX.DrainWord("unseen",1,0) #She sees you, so remove unseens

    if action_context == "join":       # This triggers if you ask to join in
                if Approval > 1 or (Approval and JeanX.lust >= 50):
                    $ Player.AddWord(1,"join")
                    menu:
                        extend ""
                        "Would you like some help? I could lend some helping hands. . ."  if Player.Semen and JeanX.Action:
                                $ JeanX.change_stat("love", 90, 1)
                                $ JeanX.change_stat("obedience", 50, 2)
                                $ JeanX.change_face("sexy")
                                ch_j "Hmm, ok, give these a squeeze. . ."
                                $ JeanX.change_stat("obedience", 70, 2)
                                $ JeanX.change_stat("inhibition", 70, 1)
                                $ offhand_action = "fondle breasts"
                                $ JeanX.Mast += 1
                                jump Jean_M_Cycle
                        "Would you like some help? I could. . . up to you, I guess." if Player.Semen and JeanX.Action:
                                $ JeanX.change_stat("love", 70, 2)
                                $ JeanX.change_stat("love", 90, 1)
                                $ JeanX.change_face("sexy")
                                ch_j "Ok, sure. . ."
                                $ JeanX.change_stat("obedience", 70, 2)
                                $ JeanX.change_stat("inhibition", 70, 1)
                                $ D20 = renpy.random.randint(1, 20)
                                if D20 > 10:
                                    $ offhand_action = "fondle breasts"
                                else:
                                    $ offhand_action = "suck breasts"
                                $ JeanX.Mast += 1
                                jump Jean_M_Cycle
                        "Why don't we take care of each other?" if Player.Semen and JeanX.Action:
                                $ JeanX.change_face("sexy")
                                ch_j "Like what?"
                                $ renpy.pop_call()          #removes the call to this label
                                return                      #returns to sexmenu=
                        "You look like you have things well in hand. . .":
                                if JeanX.lust >= 50:
                                    $ JeanX.change_stat("love", 70, 2)
                                    $ JeanX.change_stat("love", 90, 1)
                                    $ JeanX.change_face("sexy")
                                    ch_j "I'm getting there. . ."
                                    $ JeanX.change_stat("obedience", 80, 3)
                                    $ JeanX.change_stat("inhibition", 80, 5)
                                    jump Jean_M_Cycle
                                elif ApprovalCheck(JeanX, 1200):
                                    $ JeanX.change_face("sly")
                                    ch_j "Yeah. . . but I can take a break. . ."
                                else:
                                    $ JeanX.change_face("angry")
                                    ch_j "-well I -was.-"

                #else: You've failed all checks so she kicks you out.
                $ JeanX.ArmPose = 1
                $ JeanX.OutfitChange()
                $ JeanX.Action -= 1
                $ Player.change_stat("Focus", 50, 30)
                call Checkout(1)
                $ line = 0
                $ action_context = 0
                $ renpy.pop_call()          #removes the call to this label
                if Approval:
                        $ JeanX.change_face("bemused", 2)
                        if bg_current == JeanX.Home:
                            ch_j "Why are you in my room?"
                        else:
                            ch_j "I didn't call for anyone. . ."
                        $ JeanX.Blush = 1
                else:
                        $ JeanX.change_stat("love", 200, -5)
                        $ JeanX.change_face("angry")
                        $ JeanX.recent_history.append("angry")
                        $ JeanX.daily_history.append("angry")
                        if bg_current == JeanX.Home:
                            ch_j "I was busy, so get out."
                            "[JeanX.name] kicks you out of her room."
                            $ renpy.pop_call()
                            jump Campus_Map
                        else:
                            ch_j "I'm leaving, but maybe knock next time?"
                            call Remove_Girl(JeanX)
                return                      #returns to sexmenu, which returns to original
    #End of "Join" option



    if action_context == JeanX:                                                                  #Jean auto-starts
                if Approval > 2:
                        if JeanX.wearing_skirt:
                            "[JeanX.name]'s hand snakes down her body, and hikes up her skirt."
                            $ JeanX.Upskirt = 1
                        elif JeanX.PantsNum() >= 6:
                            "[JeanX.name] slides her hand down her body and into her pants."
                        elif JeanX.HoseNum() >= 5:
                            "[JeanX.name]'s hand slides down her body and under her [JeanX.Hose]."
                        elif JeanX.Panties:
                            "[JeanX.name]'s hand slides down her body and under her [JeanX.Panties]."
                        else:
                            "[JeanX.name]'s hand slides down her body and begins to caress her pussy."
                        $ JeanX.SeenPanties = 1
                        call Jean_First_Bottomless(1)
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
                                    ch_p "That is so sexy, [JeanX.Pet]."
                                    $ JeanX.nameCheck() #checks reaction to petname
                                    "You lean back and enjoy the show."
                                    $ JeanX.change_stat("love", 80, 1)
                                    $ JeanX.change_stat("obedience", 90, 1)
                                    $ JeanX.change_stat("obedience", 50, 2)
                            "Ask her to stop.":
                                    $ JeanX.change_face("surprised")
                                    $ JeanX.change_stat("inhibition", 70, 1)
                                    ch_p "Let's not do that right now, [JeanX.Pet]."
                                    $ JeanX.nameCheck() #checks reaction to petname
                                    "[JeanX.name] pulls her hands away from herself."
                                    $ JeanX.OutfitChange()
                                    $ JeanX.change_stat("obedience", 90, 1)
                                    $ JeanX.change_stat("obedience", 50, 1)
                                    $ JeanX.change_stat("obedience", 30, 2)
                                    return
                        jump Jean_M_Prep
                else:
                        $ temp_modifier = 0
                        $ offhand_action = 0
                return
    #End if Jean intitiates this action

    #first time
    if not JeanX.Mast:
            $ JeanX.change_face("surprised", 1)
            $ JeanX.Mouth = "kiss"
            ch_j "Oh, so you want to watch while I get off?"
            if JeanX.Forced:
                $ JeanX.change_face("sad")
                ch_j "But -just- watch, right? . ."


    #First time dialog
    if not JeanX.Mast and Approval:
            if JeanX.Forced:
                $ JeanX.change_face("sad")
                $ JeanX.change_stat("love", 70, -3, 1)
                $ JeanX.change_stat("love", 20, -2, 1)
            elif JeanX.love >= JeanX.obedience and JeanX.love >= (JeanX.inhibition - JeanX.IX):
                $ JeanX.change_face("sexy")
                $ JeanX.Brows = "sad"
                $ JeanX.Mouth = "smile"
                ch_j "Well. . ."
            elif JeanX.obedience >= (JeanX.inhibition - JeanX.IX):
                $ JeanX.change_face("normal")
                ch_j "If that's what you're into. . ."
            else: # Uninhibited
                $ JeanX.change_face("sad")
                $ JeanX.Mouth = "smile"
                ch_j "I do have some time. . ."


    #Second time+ initial dialog
    elif Approval:
            if JeanX.Forced:
                $ JeanX.change_face("sad")
                $ JeanX.change_stat("love", 70, -3, 1)
                $ JeanX.change_stat("love", 20, -2, 1)
                ch_j "Hmm, again?"
            elif Approval and "masturbation" in JeanX.recent_history:
                $ JeanX.change_face("sexy", 1)
                ch_j "Mmmm . . ."
                jump Jean_M_Prep
            elif Approval and "masturbation" in JeanX.daily_history:
                $ JeanX.change_face("sexy", 1)
                $ line = renpy.random.choice(["Did you enjoy that?",
                    "Didn't get enough earlier?",
                    "I do like having an audience. . ."])
                ch_j "[line]"
            elif JeanX.Mast < 3:
                $ JeanX.change_face("sexy", 1)
                $ JeanX.Brows = "confused"
                ch_j "You enjoyed that, huh."
            else:
                $ JeanX.change_face("sexy", 1)
                $ JeanX.ArmPose = 2
                $ line = renpy.random.choice(["You do like to watch.",
                    "Again?",
                    "You like to watch me.",
                    "You'd like me to masturbate again?"])
                ch_j "[line]"
                $ line = 0
    #End second time+ initial dialog

    #If she's into it. . .
    if Approval >= 2:
            if JeanX.Forced:
                $ JeanX.change_face("sad")
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("inhibition", 60, 1)
                ch_j "Oh. . . fine. . ."
            else:
                $ JeanX.change_face("sexy", 1)
                $ JeanX.change_stat("love", 90, 1)
                $ JeanX.change_stat("inhibition", 50, 3)
                $ line = renpy.random.choice(["Sure. Ok.",
                    "Couldn't hurt. . .",
                    "All right.",
                    "Sure.",
                    "Sure, why not. . ."])
                ch_j "[line]"
                $ line = 0
            $ JeanX.change_stat("obedience", 20, 1)
            $ JeanX.change_stat("obedience", 60, 1)
            $ JeanX.change_stat("inhibition", 70, 2)
            jump Jean_M_Prep

    #If she's not into it, but maybe. . .
    else:
        menu:
            ch_j "I don't know, it's kind of a bad time. . ."
            "Maybe later?":
                    $ JeanX.change_face("sexy", 1)
                    if JeanX.lust > 70:
                        ch_j "Well -I- will, but after you leave."
                    else:
                        ch_j "Wel. . . maybe. . ."
                    $ JeanX.change_stat("love", 80, 2)
                    $ JeanX.change_stat("inhibition", 70, 2)
                    return
            "You look like you could use it. . .":
                    if Approval:
                        $ JeanX.change_face("sexy")
                        $ JeanX.change_stat("obedience", 90, 2)
                        $ JeanX.change_stat("obedience", 50, 2)
                        $ JeanX.change_stat("inhibition", 70, 3)
                        $ JeanX.change_stat("inhibition", 40, 2)
                        $ line = renpy.random.choice(["Sure. Ok.",
                                "Couldn't hurt. . .",
                                "All right.",
                                "Sure.",
                                "Sure, why not. . ."])
                        ch_j "[line]"
                        $ line = 0
                        jump Jean_M_Prep

            "Just get at it already.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(JeanX, 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                    if Approval > 1 or (Approval and JeanX.Forced):
                        $ JeanX.change_face("sad")
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
                        $ JeanX.recent_history.append("angry")
                        $ JeanX.daily_history.append("angry")
    # end of asking her to do it

    #She refused all offers.
    $ JeanX.ArmPose = 1
    if JeanX.Forced:
            $ JeanX.change_face("angry", 1)
            ch_j "Nope, too kinky."
            $ JeanX.change_stat("lust", 90, 5)
            if JeanX.love > 300:
                $ JeanX.change_stat("love", 70, -2)
            $ JeanX.change_stat("obedience", 50, -2)
            $ JeanX.recent_history.append("angry")
            $ JeanX.daily_history.append("angry")
            $ JeanX.recent_history.append("no masturbation")
            $ JeanX.daily_history.append("no masturbation")
            return
    elif JeanX.Taboo:                             # she refuses and this is too public a place for her
            $ JeanX.change_face("angry", 1)
            $ JeanX.daily_history.append("tabno")
            ch_j "I. . . couldn't do that in public. . ."
            $ JeanX.change_stat("lust", 90, 5)
            $ JeanX.change_stat("obedience", 50, -3)
            return
    elif JeanX.Mast:
            $ JeanX.change_face("sad")
            ch_j "Eh, I think I'm ok for now. . ."
    else:
            $ JeanX.change_face("normal", 1)
            ch_j "Um, no."
    $ JeanX.recent_history.append("no masturbation")
    $ JeanX.daily_history.append("no masturbation")
    $ temp_modifier = 0
    return

label Jean_M_Prep:
    $ JeanX.Upskirt = 1
    $ JeanX.PantiesDown = 1
    call Jean_First_Bottomless(1)
    call set_the_scene(Dress=0)

    #if she hasn't seen you yet. . .
    if "unseen" in JeanX.recent_history:
            $ JeanX.change_face("sexy")
            $ JeanX.Eyes = "closed"
            $ JeanX.ArmPose = 2
            "You see [JeanX.name] leaning back, masturbating. You don't think she's noticed you yet."
    else:
            $ JeanX.change_face("sexy")
            $ JeanX.ArmPose = 2
            "[JeanX.name] lays back and starts to toy with herself."
            if not JeanX.Mast:#First time
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
        $ girl_offhand_action = "fondle pussy"

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ line = 0
    if JeanX.Taboo:
        $ JeanX.DrainWord("tabno")
    $ JeanX.DrainWord("no masturbation")
    $ JeanX.recent_history.append("masturbation")
    $ JeanX.daily_history.append("masturbation")

label Jean_M_Cycle:
    if action_context == "join":
        $ renpy.pop_call()
        $ action_context = 0

    while Round > 0:
        call Jean_Pos_Reset("masturbation")
        call Shift_Focus(JeanX)
        $ JeanX.lustFace()

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep Watching.":
                                pass

                        "[JeanX.name]. . .[[jump in]" if "unseen" not in JeanX.recent_history and "join" not in Player.recent_history and JeanX.Loc == bg_current:
                                "[JeanX.name] slows what she's doing with a sly grin."
                                ch_j "Like what you see?"
                                $ action_context = "join"
                                call Jean_Masturbate
                        "\"Ahem. . .\"" if "unseen" in JeanX.recent_history and JeanX.Loc == bg_current:
                                jump Jean_M_Interupted

                        "Start jack'in it." if offhand_action != "jackin":
                                call Jackin(JeanX)
                        "Stop jack'in it." if offhand_action == "jackin":
                                $ offhand_action = 0

                        "Slap her ass" if JeanX.Loc == bg_current:
                                if "unseen" in JeanX.recent_history:
                                        "You smack [JeanX.name] firmly on the ass!"
                                        jump Jean_M_Interupted
                                else:
                                        call Slap_Ass(JeanX)
                                        $ counter += 1
                                        $ Round -= 1
                                        jump Jean_M_Cycle

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
                                    "Offhand action" if JeanX.Loc == bg_current:
                                            if JeanX.Action and multi_action:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ JeanX.Action -= 1
                                            else:
                                                ch_j "I'd like to stick with this."

                                    "Threesome actions (locked)" if not Partner or "unseen" in JeanX.recent_history or JeanX.Loc != bg_current:
                                        pass
                                    "Threesome actions" if Partner and "unseen" not in JeanX.recent_history and JeanX.Loc == bg_current:
                                        menu:
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(JeanX)
                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(JeanX)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jean_M_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jean_M_Cycle
                                            "Never mind":
                                                        jump Jean_M_Cycle

                                    "Show her feet" if not ShowFeet and JeanX.Pose == "doggy":
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and JeanX.Pose == "doggy":
                                            $ ShowFeet = 0

                                    "Undress [JeanX.name]":
                                            if "unseen" in JeanX.recent_history:
                                                    ch_p "Oh, yeah, take it off. . ."
                                                    jump Jean_M_Interupted
                                            else:
                                                    call Girl_Undress(JeanX)
                                    "Clean up [JeanX.name] (locked)" if not JeanX.Spunk:
                                            pass
                                    "Clean up [JeanX.name]" if JeanX.Spunk:
                                            if "unseen" in JeanX.recent_history:
                                                    ch_p "You've got a little something on you. . ."
                                                    jump Jean_M_Interupted
                                            else:
                                                    call Girl_Cleanup(JeanX,"ask")
                                    "Never mind":
                                                    jump Jean_M_Cycle

                        "Back to Sex Menu" if multi_action and JeanX.Loc == bg_current:
                                    ch_p "Let's try something else."
                                    call Jean_Pos_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Jean_M_Interupted
                        "End Scene" if not multi_action or JeanX.Loc != bg_current:
                                    ch_p "Let's stop for now."
                                    call Jean_Pos_Reset
                                    $ line = 0
                                    jump Jean_M_Interupted
        #End menu (if line)

        call Shift_Focus(JeanX)
        call Sex_Dialog(JeanX,Partner)

        #If either of you could cum

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up

        if Player.Focus >= 100 or JeanX.lust >= 100:
                    #If you can cum:
                    if Player.Focus >= 100:
                        if "unseen" not in JeanX.recent_history:
                            #if she knows you're there
                            call Player_Cumming(JeanX)
                            if "angry" in JeanX.recent_history:
                                call Jean_Pos_Reset
                                return
                            $ JeanX.change_stat("lust", 200, 5)
                            if 100 > JeanX.lust >= 70 and JeanX.OCount < 2:
                                $ JeanX.recent_history.append("unsatisfied")
                                $ JeanX.daily_history.append("unsatisfied")
                            $ line = "came"
                        else: #If she wasn't aware you were there
                            "You grunt and try to hold it in."
                            $ Player.Focus = 95
                            if JeanX.Loc == bg_current:
                                    jump Jean_M_Interupted

                    #If Jean can cum
                    if JeanX.lust >= 100:
                        call Girl_Cumming(JeanX)
                        if JeanX.Loc == bg_current:
                                jump Jean_M_Interupted

                    if line == "came":
                        $ line = 0
                        if not Player.Semen:
                            "You're emptied out, you should probably take a break."
                            $ offhand_action = 0 if offhand_action == "jackin" else offhand_action


                        if "unsatisfied" in JeanX.recent_history:#And Jean is unsatisfied,
                            "[JeanX.name] still seems a bit unsatisfied with the experience."
                            menu:
                                "Let her keep going?"
                                "Yes, keep going for a bit.":
                                    $ line = "You let her get back into it"
                                    jump Jean_M_Cycle
                                "No, I'm done.":
                                    "You ask her to stop."
                                    return
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        if "unseen" in JeanX.recent_history:
                if Round == 10:
                    "It's getting a bit late, [JeanX.name] will probably be wrapping up soon."
                elif Round == 5:
                    "She's definitely going to stop soon."
        else:
                if JeanX.Loc == bg_current:
                        call Escalation(JeanX) #sees if she wants to escalate things

                if Round == 10:
                    ch_j "Wow, look at the time. . ."
                    $ JeanX.lust += 10
                elif Round == 5:
                    ch_j "Ok, can we take a break?"
                    $ JeanX.lust += 25

    #Round = 0 loop breaks
    $ JeanX.change_face("bemused", 0)
    $ line = 0
    if "unseen" not in JeanX.recent_history:
        ch_j "Ok, that's it, break time."

label Jean_M_Interupted:

    # If she hasn't noticed you're there before cumming
    if "unseen" in JeanX.recent_history:
                $ JeanX.change_face("surprised", 2)
                "[JeanX.name] stops what she's doing with a start, eyes wide."
                call Jean_First_Bottomless(1)
                $ JeanX.change_face("surprised", 2)

                #If you've been jacking it
                if offhand_action == "jackin":
                        ch_j "Oh, hey. . .[JeanX.Petname]."
                        ch_j "When did you get here?"
                        $ JeanX.Eyes = "down"
                        menu:
                            ch_j "I see you've been making yourself at home. . . "
                            "A while back, it was an excellent show.":
                                    $ JeanX.change_face("sexy",1)
                                    $ JeanX.change_stat("obedience", 50, 3)
                                    $ JeanX.change_stat("obedience", 70, 2)
                                    ch_j "True. . ."
                                    if JeanX.love >= 800 or JeanX.obedience >= 500 or (JeanX.inhibition - JeanX.IX) >= 500:
                                        $ temp_modifier += 10
                                        $ JeanX.change_stat("lust", 90, 5)
                                        ch_j "And you can put on quite a show yourself. . ."

                            "I. . . just got here?":
                                    $ JeanX.change_face("angry",1)
                                    $ JeanX.change_stat("love", 70, 2)
                                    $ JeanX.change_stat("love", 90, 1)
                                    $ JeanX.change_stat("obedience", 50, 2)
                                    $ JeanX.change_stat("obedience", 70, 2)
                                    "She looks pointedly at your cock,"
                                    ch_j "A likely story. . ."
                                    if JeanX.love >= 800 or JeanX.obedience >= 500 or (JeanX.inhibition - JeanX.IX) >= 500:
                                            $ temp_modifier += 10
                                            $ JeanX.change_stat("lust", 90, 5)
                                            $ JeanX.change_face("bemused", 1)
                                            ch_j "I guess I can't blame you. . ."
                                    else:
                                            $ temp_modifier -= 10
                                            $ JeanX.change_stat("lust", 200, -5)
                        call Seen_First_Peen(JeanX,Partner)
                        ch_j "Hmm. . ."

                #you haven't been jacking it
                else:
                        ch_j "Oh, hey. . .[JeanX.Petname]."
                        ch_j "When did you get here?"
                        menu:
                            extend ""
                            "A while back.":
                                    $ JeanX.change_face("sexy", 1)
                                    $ JeanX.change_stat("obedience", 50, 3)
                                    $ JeanX.change_stat("obedience", 70, 2)
                                    ch_j "Nice of you to let me know. . ."
                            "I just got here.":
                                    $ JeanX.change_face("bemused", 1)
                                    $ JeanX.change_stat("love", 70, 2)
                                    $ JeanX.change_stat("love", 90, 1)
                                    ch_j "Uh-huh. . ."
                                    $ JeanX.change_stat("obedience", 50, 2)
                                    $ JeanX.change_stat("obedience", 70, 2)

                $ JeanX.DrainWord("unseen",1,0) #She sees you, so remove unseens
                $ JeanX.Mast += 1
                if Round <= 10:
                    ch_j "I could use a break anyway. . ."
                    return
                $ action_context = "join"
                call Jean_Masturbate
                "error: report this if you see it."
                return #should be redundant
    #End Unseen

    #else, if She's seen you already
    $ JeanX.Action -= 1
    $ JeanX.Mast += 1
    call Checkout
    if action_context == "shift":
        $ action_context = 0
        return
    $ action_context = 0

    if Partner == EmmaX:
        call Partner_Like(JeanX,3)
    else:
        call Partner_Like(JeanX,2)

    if JeanX.Loc != bg_current:
        return

    if Round <= 10:
            ch_j "I need a minute here. . ."
            return
    $ JeanX.change_face("sexy", 1)
    if JeanX.lust < 20:
        ch_j "I got off, how about you?"
    else:
        ch_j "So, what next?"
    menu:
        extend ""
        "Well, I have something you could take care of. . ." if Player.Semen and JeanX.Action:
                $ action_context = "shift"
                return
        "You could just keep going. . ." if Player.Semen:
                $ JeanX.change_face("sly")
                if JeanX.Action and Round >= 10:
                    ch_j "Ok. . ."
                    jump Jean_M_Cycle
                else:
                    ch_j "I need a minute here. . ."
        "I'm good here. [[Stop]":
                if JeanX.love < 800 and JeanX.inhibition < 500 and JeanX.obedience < 500:
                    $ JeanX.OutfitChange()
                $ JeanX.change_face("normal")
                $ JeanX.Brows = "confused"
                ch_j "Ok."
                $ JeanX.Brows = "normal"
        "You should probably stop for now." if JeanX.lust > 30:
                $ JeanX.change_face("angry")
                ch_j "Hrmm."
    return

## end JeanX.Masturbating ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



# Start Jean Sex pose //////////////////////////////////////////////////////////////////////////////////
# JeanX.Sex_P //////////////////////////////////////////////////////////////////////

label Jean_Sex_P:

    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JeanX)
    if JeanX.Sex >= 7: # She loves it
        $ temp_modifier += 15
    elif JeanX.Sex >= 3: #You've done it before several times
        $ temp_modifier += 12
    elif JeanX.Sex: #You've done it before
        $ temp_modifier += 10

    if JeanX.Addict >= 75 and (JeanX.CreamP + JeanX.CreamA) >=3: #She's really strung out and has creampied
        $ temp_modifier += 20
    elif JeanX.Addict >= 75:
        $ temp_modifier += 15

    if JeanX.lust > 85:
        $ temp_modifier += 10
    elif JeanX.lust > 75: #She's really horny
        $ temp_modifier += 5

    if action_context == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in JeanX.Traits:
        $ temp_modifier += (4*Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JeanX.Traits:
        $ temp_modifier -= 40
    if JeanX.ForcedCount and not JeanX.Forced:
        $ temp_modifier -= 5 * JeanX.ForcedCount



    if JeanX.Taboo and "tabno" in JeanX.daily_history:
        $ temp_modifier -= 10

    if "no sex" in JeanX.daily_history:
        $ temp_modifier -= 15 if "no sex" in JeanX.recent_history else 5


    $ Approval = ApprovalCheck(JeanX, 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)

    if action_context == "auto":
                call Jean_Sex_Launch("sex")
                if JeanX.wearing_skirt:
                    "You flip [JeanX.name] around, sliding her skirt up as you go."
                    $ JeanX.Upskirt = 1
                elif JeanX.PantsNum() >= 6:
                    "You flip [JeanX.name] around, sliding her pants down as you do."
                    $ JeanX.Upskirt = 1
                else:
                    "You flip [JeanX.name] around."
                $ JeanX.SeenPanties = 1
                "You rub the tip of your cock against her moist slit."
                $ JeanX.change_face("surprised", 1)

                if (JeanX.Sex and Approval) or (Approval > 1):
                    #this is not the first time you've had sex, or she's into it
                    "[JeanX.name] glances back and then breaks into a smile."
                    $ JeanX.change_face("sly")
                    $ JeanX.change_stat("obedience", 70, 3)
                    $ JeanX.change_stat("inhibition", 50, 3)
                    $ JeanX.change_stat("inhibition", 70, 1)
                    ch_j "Oh, if you must, [JeanX.Petname]."
                    jump Jean_SexPrep
                else:
                    #she's questioning it
                    $ JeanX.Brows = "angry"
                    menu:
                        ch_j "Just sticking it in?"
                        "Sorry, sorry! Never mind.":
                            if Approval:
                                    $ JeanX.change_face("sexy", 1)
                                    $ JeanX.change_stat("obedience", 70, 3)
                                    $ JeanX.change_stat("inhibition", 50, 3)
                                    $ JeanX.change_stat("inhibition", 70, 1)
                                    ch_j "Oh, no, it's fine."
                                    jump Jean_SexPrep
                            else:
                                    "You pull back before you really get it in."
                                    $ JeanX.change_face("bemused", 1)
                                    #if JeanX.Sex:
                                    ch_j "You should ask first, [JeanX.Petname]."
                                    #else:
                                        #ch_j "Maybe if you'd asked first. . ."
                        "Just fucking.":
                            $ JeanX.change_stat("love", 80, -10, 1)
                            $ JeanX.change_stat("love", 200, -10)
                            "You press inside some more."
                            $ JeanX.change_stat("obedience", 70, 3)
                            $ JeanX.change_stat("inhibition", 50, 3)
                            if not ApprovalCheck(JeanX, 700, "O", TabM=1):   #Checks if obedience is 700+
                                $ JeanX.change_face("angry")
                                "[JeanX.name] shoves you away and backhands you in the face."
                                ch_j "Hey, I don't need my powers to hurt you."
                                $ JeanX.change_stat("love", 50, -10, 1)
                                $ JeanX.change_stat("obedience", 50, 3)
                                $ renpy.pop_call()
                                if action_context:
                                    $ renpy.pop_call()
                                call Jean_Sex_Reset
                                $ JeanX.recent_history.append("angry")
                                $ JeanX.daily_history.append("angry")
                            else:
                                $ JeanX.change_face("sad")
                                "[JeanX.name] doesn't seem to be into this, you're lucky she's willing to give it a try."
                                jump Jean_SexPrep
                return
    #End Auto


    if not JeanX.Sex and "no sex" not in JeanX.recent_history:
            #first time
            $ JeanX.change_face("surprised", 1)
            $ JeanX.Mouth = "kiss"
            ch_j "Oh, you wanna fuck . . "
            if JeanX.Forced:
                $ JeanX.change_face("sad")
                ch_j "Pretty bold of you. . ."


    if not JeanX.Sex and Approval:
            #First time dialog
            if JeanX.Forced:
                $ JeanX.change_face("sad")
                $ JeanX.change_stat("love", 70, -30, 1)
                $ JeanX.change_stat("love", 20, -20, 1)
            elif JeanX.love >= (JeanX.obedience + JeanX.inhibition - JeanX.IX):
                $ JeanX.change_face("sexy")
                $ JeanX.Brows = "sad"
                $ JeanX.Mouth = "smile"
                ch_j "I was wondering when this would come up. . ."
            elif JeanX.obedience >= (JeanX.inhibition - JeanX.IX):
                $ JeanX.change_face("normal")
                ch_j "Ok, [JeanX.Petname]. . ."
            elif JeanX.Addict >= 50:
                $ JeanX.change_face("manic", 1)
                ch_j "That does sound fun. . ."
            else: # Uninhibited
                $ JeanX.change_face("sad")
                $ JeanX.Mouth = "smile"
                ch_j "I was wondering when this would come up. . ."
            #End first time dialog

    elif Approval:
            #Second time+ dialog
            $ JeanX.change_face("sexy", 1)
            if JeanX.Forced:
                $ JeanX.change_face("sad")
                $ JeanX.change_stat("love", 70, -3, 1)
                $ JeanX.change_stat("love", 20, -2, 1)
                ch_j "You'll pay for this eventually. . ."
            elif not JeanX.Taboo and "tabno" in JeanX.daily_history:
                ch_j "Ok, yeah, this is better."
            elif "sex" in JeanX.recent_history:
                ch_j "Again? Your funeral."
                jump Jean_SexPrep
            elif "sex" in JeanX.daily_history:
                $ line = renpy.random.choice(["Back again?",
                    "You'd like another round?",
                    "I must be better than I thought.",
                    "Didn't get enough earlier?",
                    "Your funeral, " + JeanX.Petname + "."])
                ch_j "[line]"
            elif JeanX.Sex < 3:
                $ JeanX.Brows = "confused"
                $ JeanX.Mouth = "kiss"
                ch_j "Oh? Another round?"
            else:
                $ line = renpy.random.choice(["Oh, you want some of this?",
                    "You'd like another round?",
                    "I must be better than I thought.",
                    "I hope you don't plan on wearing me out.",
                    "You want to fuck me?"])
                ch_j "[line]"
            $ line = 0
            #end Second time+ dialog

    if Approval >= 2:
            #She's into it. . .
            if JeanX.Forced:
                $ JeanX.change_face("sad")
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("inhibition", 60, 1)
                ch_j "Ok, fine. Just make it good."
            elif "no sex" in JeanX.daily_history:
                ch_j "Ok, whatever. . ."
            else:
                $ JeanX.change_face("sexy", 1)
                $ JeanX.change_stat("love", 90, 1)
                $ JeanX.change_stat("inhibition", 50, 3)
                $ line = renpy.random.choice(["Well. . . fine, let's do it.",
                    "Sure.",
                    "We could, I guess.",
                    "Hmmm, sure.",
                    "Sounds fun."])
                ch_j "[line]"
                $ line = 0
            $ JeanX.change_stat("obedience", 20, 1)
            $ JeanX.change_stat("obedience", 60, 1)
            $ JeanX.change_stat("inhibition", 70, 2)
            jump Jean_SexPrep

    else:
            #She's not into it, but maybe. . .
            $ JeanX.change_face("angry")
            if "no sex" in JeanX.recent_history:
                ch_j "I don't repeat myself."
            elif JeanX.Taboo and "tabno" in JeanX.daily_history and "no sex" in JeanX.daily_history:
                ch_j "I'm not comfortable with that. . ."
            elif "no sex" in JeanX.daily_history:
                ch_j "Not today."
            elif JeanX.Taboo and "tabno" in JeanX.daily_history:
                ch_j "I told you, I'm not comfortable with that. . ."
            elif not JeanX.Sex:
                $ JeanX.change_face("bemused")
                ch_j "Oh, this would be interesting. . ."
            else:
                $ JeanX.change_face("bemused")
                ch_j "I'm not in the mood right now . ."
            menu:
                extend ""
                "Sorry, never mind." if "no sex" in JeanX.daily_history:
                        $ JeanX.change_face("bemused")
                        ch_j "Keep trying. . ."
                        return
                "Maybe later?" if "no sex" not in JeanX.daily_history:
                        $ JeanX.change_face("sexy")
                        ch_j "Sure, whatever. . ."
                        $ JeanX.change_stat("love", 80, 2)
                        $ JeanX.change_stat("inhibition", 70, 2)
                        if JeanX.Taboo:
                            $ JeanX.recent_history.append("tabno")
                            $ JeanX.daily_history.append("tabno")
                        $ JeanX.recent_history.append("no sex")
                        $ JeanX.daily_history.append("no sex")
                        return
                "I think you'd enjoy it as much as I would. . .":
                        if Approval:
                            $ JeanX.change_face("sexy")
                            $ JeanX.change_stat("obedience", 90, 2)
                            $ JeanX.change_stat("obedience", 50, 2)
                            $ JeanX.change_stat("inhibition", 70, 3)
                            $ JeanX.change_stat("inhibition", 40, 2)
                            $ line = renpy.random.choice(["Yeah, probably. . .",
                                "I guess. . .",
                                "Good point. . ."])
                            ch_j "[line]"
                            $ line = 0
                            jump Jean_SexPrep
                "Just deal with it.":                                               # Pressured into it
                        $ Approval = ApprovalCheck(JeanX, 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
                        if Approval > 1 or (Approval and JeanX.Forced):
                            $ JeanX.change_face("confused",Eyes="side")
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
                            $ JeanX.recent_history.append("angry")
                            $ JeanX.daily_history.append("angry")
                #end menu
    #end Approval check

    #She refused all offers.
    $ JeanX.ArmPose = 1
    if "no sex" in JeanX.daily_history:
        ch_j "Don't push your luck, [JeanX.Petname]."
        $ JeanX.recent_history.append("angry")
        $ JeanX.daily_history.append("angry")
    elif JeanX.Forced:
        $ JeanX.change_face("angry", 1)
        ch_j "I'm the queen here!"
        $ JeanX.change_stat("lust", 200, 5)
        if JeanX.love > 300:
                $ JeanX.change_stat("love", 70, -2)
        $ JeanX.change_stat("obedience", 50, -2)
        ch_j "I do not take orders."
        $ JeanX.recent_history.append("angry")
        $ JeanX.daily_history.append("angry")
    elif JeanX.Taboo:                             # she refuses and this is too public a place for her
        $ JeanX.change_face("angry", 1)
        $ JeanX.recent_history.append("tabno")
        $ JeanX.daily_history.append("tabno")
        ch_j "I'm just not comfortable with that right now. . ."
        $ JeanX.change_stat("lust", 200, 5)
        $ JeanX.change_stat("obedience", 50, -3)
    elif JeanX.Sex:
        $ JeanX.change_face("sad")
        ch_j "Maybe just fuck one of the others."
    else:
        $ JeanX.change_face("normal", 1)
        ch_j "Not interested."
    $ JeanX.recent_history.append("no sex")
    $ JeanX.daily_history.append("no sex")
    $ temp_modifier = 0
    return

label Jean_Sex_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(JeanX)
        call Jean_Sex_Launch("sex")
        if action_speed >= 4:
            $ action_speed = 2
#            call action_speed_Shift(2)
        $ JeanX.lustFace()
        $ Player.Sprite = 1
        $ Player.Cock = "in"
        $ primary_action = "sex"
        $ JeanX.Upskirt = 1
        $ JeanX.PantiesDown = 1

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if action_speed:
                                    pass
                        "Keep going. . . (locked)" if not action_speed:
                                    pass

                        "Start moving? . ." if not action_speed:
                                    $ action_speed = 1
#                                    call action_speed_Shift(1)
                        "action_speed up. . ." if 0 < action_speed < 3:
                                    $ action_speed += 1
#                                    call action_speed_Shift(action_speed+1)
                                    "You ask her to up the pace a bit."
                        "action_speed up. . . (locked)" if action_speed >= 3:
                                    pass

                        "Slow Down. . ." if action_speed:
                                    $ action_speed -= 1
#                                    call action_speed_Shift(action_speed-1)
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not action_speed:
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(JeanX)
                                    $ counter += 1
                                    $ Round -= 1
                                    jump Jean_Sex_Cycle
                        "Turn her Around":
                                    $ JeanX.Pose = "doggy" if JeanX.Pose != "doggy" else "sex"
                                    "You turn her around. . ."
                                    jump Jean_Sex_Cycle

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
                                            if JeanX.Action and multi_action:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ JeanX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Shift primary action":
                                            if JeanX.Action and multi_action:
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
                                                call Sex_Basic_Dialog(JeanX,"tired")
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [JeanX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(JeanX)
                                            "Ask [JeanX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(JeanX)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(JeanX)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jean_Sex_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jean_Sex_Cycle
                                            "Never mind":
                                                        jump Jean_Sex_Cycle
                                    "Just take a look at her.":
                                            $ Player.Cock = 0
                                            $ action_speed = 0

                                    "Show her feet" if not ShowFeet and JeanX.Pose == "doggy":
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and JeanX.Pose == "doggy":
                                            $ ShowFeet = 0

                                    "Undress [JeanX.name]":
                                            call Girl_Undress(JeanX)
                                    "Clean up [JeanX.name] (locked)" if not JeanX.Spunk:
                                            pass
                                    "Clean up [JeanX.name]" if JeanX.Spunk:
                                            call Girl_Cleanup(JeanX,"ask")
                                    "Never mind":
                                            jump Jean_Sex_Cycle

                        "Back to Sex Menu" if multi_action:
                                    ch_p "Let's try something else."
                                    call Jean_Sex_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Jean_SexAfter
                        "End Scene" if not multi_action:
                                    ch_p "Let's stop for now."
                                    call Jean_Sex_Reset
                                    $ line = 0
                                    jump Jean_SexAfter
        #End menu (if line)

        call Shift_Focus(JeanX)
        call Sex_Dialog(JeanX,Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JeanX.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JeanX)
                            if "angry" in JeanX.recent_history:
                                call Jean_Sex_Reset
                                return
                            $ JeanX.change_stat("lust", 200, 5)
                            if 100 > JeanX.lust >= 70 and JeanX.OCount < 2:
                                    $ JeanX.recent_history.append("unsatisfied")
                                    $ JeanX.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jean_SexAfter
                            $ line = "came"

                    if JeanX.lust >= 100:
                            #If you're still going at it and Jean can cum
                            call Girl_Cumming(JeanX)
                            if action_context == "shift" or "angry" in JeanX.recent_history:
                                jump Jean_SexAfter

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Jean_SexAfter
                            elif "unsatisfied" in JeanX.recent_history:
                                #And Jean is unsatisfied,
                                $ line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ line = "You get back into it"
                                        jump Jean_Sex_Cycle
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Jean_SexAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Jean_SexAfter
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if JeanX.SEXP >= 100 or ApprovalCheck(JeanX, 1200, "LO"):
            pass
        elif counter == (5 + JeanX.Sex):
                    $ JeanX.Brows = "confused"
                    ch_j "Ok, had enough yet?"
        elif counter == (10 + JeanX.Sex):
                    $ JeanX.Brows = "angry"
                    menu:
                        ch_j "Hey. . . you. . . about done. . . there?"
                        "How about a BJ?" if JeanX.Action and multi_action:
                                $ action_context = "shift"
                                call Jean_SexAfter
                                call Jean_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ counter += 1
                                jump Jean_Sex_Cycle
                        "Let's try something else." if multi_action:
                                $ line = 0
                                call Jean_Sex_Reset
                                $ action_context = "shift"
                                jump Jean_SexAfter
                        "No, get back down there.":
                                if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                                    $ JeanX.change_stat("love", 200, -5)
                                    $ JeanX.change_stat("obedience", 50, 3)
                                    $ JeanX.change_stat("obedience", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    $ JeanX.change_face("angry", 1)
                                    call Jean_Sex_Reset
                                    "She scowls at you and pulls out."
                                    ch_j "Don't overestimate yourself."
                                    $ JeanX.change_stat("love", 50, -3, 1)
                                    $ JeanX.change_stat("love", 80, -4, 1)
                                    $ JeanX.change_stat("obedience", 30, -1, 1)
                                    $ JeanX.change_stat("obedience", 50, -1, 1)
                                    $ JeanX.recent_history.append("angry")
                                    $ JeanX.daily_history.append("angry")
                                    jump Jean_SexAfter
        #End Count check

        call Escalation(JeanX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(JeanX,10) #"You might want to wrap this up, it's getting late."
        elif Round == 5:
                call Sex_Basic_Dialog(JeanX,5)   #"Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ JeanX.change_face("bemused", 0)
    $ line = 0
    call Sex_Basic_Dialog(JeanX,"done")   #"Ok, [Girl.Petname], that's enough of that for now."


# Jean anal //////////////////////////////////////////////////////////////////////

label Jean_Sex_A:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JeanX)
    if JeanX.Anal >= 7: # She loves it
        $ temp_modifier += 20
    elif JeanX.Anal >= 3: #You've done it before several times
        $ temp_modifier += 17
    elif JeanX.Anal: #You've done it before
        $ temp_modifier += 15

    if JeanX.Addict >= 75 and (JeanX.CreamP + JeanX.CreamA) >=3: #She's really strung out and has creampied
        $ temp_modifier += 25
    elif JeanX.Addict >= 75:
        $ temp_modifier += 15

    if JeanX.lust > 85:
        $ temp_modifier += 10
    elif JeanX.lust > 75: #She's really horny
        $ temp_modifier += 5

    $ temp_modifier += 10  # she starts out loose

    if action_context == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in JeanX.Traits:
        $ temp_modifier += (5*Taboo)

    if JeanX in Player.Harem or "sex friend" in JeanX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JeanX.Traits:
        $ temp_modifier -= 40
    if JeanX.ForcedCount and not JeanX.Forced:
        $ temp_modifier -= 5 * JeanX.ForcedCount

    if JeanX.Taboo and "tabno" in JeanX.daily_history:
        $ temp_modifier -= 10
    if "no anal" in JeanX.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no anal" in JeanX.recent_history else 0

    $ Approval = ApprovalCheck(JeanX, 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)

    if action_context == "auto":
            call Jean_Sex_Launch("anal")
            if JeanX.wearing_skirt:
                "You flip [JeanX.name] around, sliding her skirt up as you go."
                $ JeanX.Upskirt = 1
            elif JeanX.PantsNum() >= 6:
                "You flip [JeanX.name] around, sliding her pants down as you do."
                $ JeanX.Legs = 0
            else:
                "You flip [JeanX.name] around."
            $ JeanX.SeenPanties = 1
            "You press the tip of your cock against her tight rim."
            $ JeanX.change_face("surprised", 1)
            call Jean_First_Bottomless(1)

            if (JeanX.Anal and Approval) or (Approval > 1):
                #this is not the first time you've had sex, or she's into it
                $ JeanX.change_stat("obedience", 70, 3)
                $ JeanX.change_stat("inhibition", 50, 3)
                $ JeanX.change_stat("inhibition", 70, 1)
                "[JeanX.name] glances back and then breaks into a smile."
                ch_j "Oh! Sure. . ."
                jump Jean_AnalPrep
            else:
                #she's questioning it
                $ JeanX.Brows = "angry"
                menu:
                    ch_j "Sticking in the back?"
                    "Sorry, sorry! Never mind.":
                        if Approval:
                            $ JeanX.change_face("sexy", 1)
                            $ JeanX.change_stat("obedience", 70, 3)
                            $ JeanX.change_stat("inhibition", 50, 3)
                            $ JeanX.change_stat("inhibition", 70, 1)
                            ch_j "Sure, works for me. . ."
                            ch_j "Get in there."
                            jump Jean_AnalPrep
                        "You pull back before you really get it in."
                        $ JeanX.change_face("bemused", 1)

                        #if JeanX.Anal:
                            #ch_j "You coulda warned me. . ."
                        #else:
                        ch_j "Hey, just ask first. . ."
                    "Just fucking.":
                        $ JeanX.change_stat("love", 80, -10, 1)
                        $ JeanX.change_stat("love", 200, -8)
                        "You press into her."
                        $ JeanX.change_stat("obedience", 70, 3)
                        $ JeanX.change_stat("inhibition", 50, 3)
                        if not ApprovalCheck(JeanX, 700, "O", TabM=1):
                            $ JeanX.change_face("angry")
                            "[JeanX.name] shoves you away and backhands you in the face."
                            ch_j "Tsk tsk."
                            $ JeanX.change_stat("love", 50, -10, 1)
                            $ JeanX.change_stat("obedience", 50, 3)
                            $ renpy.pop_call()
                            if action_context:
                                $ renpy.pop_call()
                            call Jean_Sex_Reset
                            $ JeanX.recent_history.append("angry")
                            $ JeanX.daily_history.append("angry")
                        else:
                            $ JeanX.change_face("sad")
                            "[JeanX.name] doesn't seem to be into this, you're lucky she's willing to give it a try."
                            jump Jean_AnalPrep
            return
            #end "auto"


    if not JeanX.Anal and "no anal" not in JeanX.recent_history:
            #first time
            $ JeanX.change_face("surprised", 1)
            $ JeanX.Mouth = "kiss"
            ch_j "Oh, you're into anal?"

            if JeanX.Forced:
                $ JeanX.change_face("sad")
                ch_j "That's the card you're going to play?"

    if "anal" in JeanX.recent_history:
            $ JeanX.change_face("sexy", 1)
            ch_j "Ok, sure."
            jump Jean_AnalPrep


    if not JeanX.Anal and Approval:
            #First time dialog
            if JeanX.Forced:
                $ JeanX.change_face("sad")
                $ JeanX.change_stat("love", 70, -3, 1)
                $ JeanX.change_stat("love", 20, -2, 1)
            elif JeanX.love >= (JeanX.obedience + JeanX.inhibition - JeanX.IX):
                $ JeanX.change_face("sexy")
                $ JeanX.Brows = "sad"
                $ JeanX.Mouth = "smile"
                ch_j "I was expecting this. . ."
            elif JeanX.obedience >= (JeanX.inhibition - JeanX.IX):
                $ JeanX.change_face("normal")
                ch_j "I expected that. . ."
            elif JeanX.Addict >= 50:
                $ JeanX.change_face("manic", 1)
                ch_j "Hmm, sounds fun. . ."
            else: # Uninhibited
                $ JeanX.change_face("sad")
                $ JeanX.Mouth = "smile"
                ch_j "I was tired of waiting. . ."

    elif Approval:
            #Second time+ dialog
            if JeanX.Forced:
                $ JeanX.change_face("sad")
                $ JeanX.change_stat("love", 70, -3, 1)
                $ JeanX.change_stat("love", 20, -2, 1)
                ch_j "Well you're optimistic. . ."
            elif not JeanX.Taboo and "tabno" in JeanX.daily_history:
                ch_j "I guess here is fine. . ."
            elif "anal" in JeanX.daily_history and not JeanX.Loose:
                pass
            elif "anal" in JeanX.recent_history:
                ch_j "I am warmed up. . ."
                jump Jean_AnalPrep
            elif "anal" in JeanX.daily_history:
                $ JeanX.change_face("sexy", 1)
                $ line = renpy.random.choice(["Back again so soon?",
                    "So you'd like another round?",
                    "Again? Sure.",
                    "Didn't get enough earlier?",
                    "Your funeral, " + JeanX.Petname + "."])
                ch_j "[line]"
            else:
                $ JeanX.change_face("sexy", 1)
                $ JeanX.ArmPose = 2
                $ line = renpy.random.choice(["Oooh, you want some of this?",
                    "So you'd like another round?",
                    "I knew you enjoyed it. . .",
                    "I hope you don't plan on wearing me out.",
                    "You want to plow me?"])
                ch_j "[line]"
            $ line = 0

    if Approval >= 2:
            #She's into it. . .
            if JeanX.Forced:
                $ JeanX.change_face("sad")
                $ JeanX.change_stat("obedience", 90, 1)
                $ JeanX.change_stat("inhibition", 60, 1)
                ch_j "Whatever."
            elif "no anal" in JeanX.daily_history:
                ch_j "Well, if you're going to keep asking. . ."
                ch_j "Might be fun. . ."
            else:
                $ JeanX.change_face("sexy", 1)
                $ JeanX.change_stat("love", 90, 1)
                $ JeanX.change_stat("inhibition", 50, 3)
                $ line = renpy.random.choice(["Well. . . ok.",
                    "Sure.",
                    "You could, I guess.",
                    "Um, yeah.",
                    "Heh, ok, ok."])
                ch_j "[line]"
                $ line = 0
            $ JeanX.change_stat("obedience", 20, 1)
            $ JeanX.change_stat("obedience", 60, 1)
            $ JeanX.change_stat("inhibition", 70, 2)
            jump Jean_AnalPrep

    else:
            #She's not into it, but maybe. . .
            $ JeanX.change_face("angry")
            if "no anal" in JeanX.recent_history:
                ch_j "I don't repeat myself."
            elif JeanX.Taboo and "tabno" in JeanX.daily_history and "no anal" in JeanX.daily_history:
                ch_j "I'm not comfortable with that. . ."
            elif "no anal" in JeanX.daily_history:
                ch_j "Not today."
            elif JeanX.Taboo and "tabno" in JeanX.daily_history:
                ch_j "I told you, I'm not comfortable with that. . ."
            elif not JeanX.Anal:
                $ JeanX.change_face("bemused")
                ch_j "I don't know that you're ready for that yet."
            else:
                $ JeanX.change_face("bemused")
                ch_j "Maybe eventually. . ."
            menu:
                extend ""
                "Sorry, never mind." if "no anal" in JeanX.daily_history:
                    $ JeanX.change_face("bemused")
                    ch_j "I get it."
                    return
                "Maybe later?" if "no anal" not in JeanX.daily_history:
                    $ JeanX.change_face("sexy")
                    ch_j "Oh, probably. . ."
                    $ JeanX.change_stat("love", 80, 2)
                    $ JeanX.change_stat("inhibition", 70, 2)
                    if JeanX.Taboo:
                        $ JeanX.recent_history.append("tabno")
                        $ JeanX.daily_history.append("tabno")
                    $ JeanX.recent_history.append("no anal")
                    $ JeanX.daily_history.append("no anal")
                    return
                "I bet it would feel really good. . .":
                    if Approval:
                        $ JeanX.change_face("sexy")
                        $ JeanX.change_stat("obedience", 90, 2)
                        $ JeanX.change_stat("obedience", 50, 2)
                        $ JeanX.change_stat("inhibition", 70, 3)
                        $ JeanX.change_stat("inhibition", 40, 2)
                        $ line = renpy.random.choice(["Yeah, sure. . .",
                                "I guess. . .",
                                "Good point. . ."])
                        ch_j "[line]"
                        $ line = 0
                        jump Jean_AnalPrep
                    else:
                        pass

                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(JeanX, 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
                    if Approval > 1 or (Approval and JeanX.Forced):
                        $ JeanX.change_face("confused")
                        $ JeanX.change_stat("love", 70, -5, 1)
                        $ JeanX.change_stat("love", 200, -5)
                        $ JeanX.change_face("angry",Eyes="side")
                        ch_j "Oh fine, get it over with."
                        $ JeanX.change_stat("obedience", 80, 4)
                        $ JeanX.change_stat("inhibition", 80, 1)
                        $ JeanX.change_stat("inhibition", 60, 3)
                        $ JeanX.Forced = 1
                        jump Jean_AnalPrep
                    else:
                        $ JeanX.change_stat("love", 200, -20)
                        $ JeanX.recent_history.append("angry")
                        $ JeanX.daily_history.append("angry")

    #She refused all offers.
    $ JeanX.ArmPose = 1
    if "no anal" in JeanX.daily_history:
        ch_j "Know when to stop."
        $ JeanX.recent_history.append("angry")
        $ JeanX.daily_history.append("angry")
    elif JeanX.Forced:
        $ JeanX.change_face("angry", 1)
        ch_j "You're overestimating your power here."
        $ JeanX.change_stat("lust", 200, 5)
        if JeanX.love > 300:
                $ JeanX.change_stat("love", 70, -2)
        $ JeanX.change_stat("obedience", 50, -2)
        $ JeanX.recent_history.append("angry")
        $ JeanX.daily_history.append("angry")
    elif JeanX.Taboo:
        # she refuses and this is too public a place for her
        $ JeanX.change_face("angry", 1)
        $ JeanX.recent_history.append("tabno")
        $ JeanX.daily_history.append("tabno")
        ch_j "I'm just not comfortable with that right now. . ."
        $ JeanX.change_stat("lust", 200, 5)
        $ JeanX.change_stat("obedience", 50, -3)
    elif "anal" in JeanX.daily_history:
        $ JeanX.change_face("bemused")
        ch_j "Not right now."
    elif JeanX.Anal:
        $ JeanX.change_face("sad")
        ch_j "You'll have to earn that one. . ."
    else:
        $ JeanX.change_face("normal", 1)
        ch_j "You haven't earned it yet."
    $ JeanX.recent_history.append("no anal")
    $ JeanX.daily_history.append("no anal")
    $ temp_modifier = 0
    return

label Jean_Anal_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(JeanX)
        call Jean_Sex_Launch("anal")
        if action_speed >= 4:
            $ Shift = 2
#            call action_speed_Shift(2)
        $ JeanX.lustFace()
        $ Player.Sprite = 1
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
#                                    call action_speed_Shift(1)
                        "action_speed up. . ." if 0 < action_speed < 3:
                                    $ action_speed += 1
#                                    call action_speed_Shift(action_speed+1)
                                    "You ask her to up the pace a bit."
                        "action_speed up. . . (locked)" if action_speed >= 3:
                                    pass

                        "Slow Down. . ." if action_speed:
                                    $ action_speed -= 1
#                                    call action_speed_Shift(action_speed-1)
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not action_speed:
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(JeanX)
                                    $ counter += 1
                                    $ Round -= 1
                                    jump Jean_Anal_Cycle
                        "Turn her Around":
                                    $ JeanX.Pose = "doggy" if JeanX.Pose != "doggy" else "sex"
                                    "You turn her around. . ."
                                    jump Jean_Anal_Cycle

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
                                            if JeanX.Action and multi_action:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ JeanX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Shift primary action":
                                            if JeanX.Action and multi_action:
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
                                                call Sex_Basic_Dialog(JeanX,"tired")
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [JeanX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(JeanX)
                                            "Ask [JeanX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(JeanX)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(JeanX)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jean_Anal_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jean_Anal_Cycle
                                            "Never mind":
                                                        jump Jean_Anal_Cycle
                                    "Just take a look at her.":
                                            $ Player.Cock = 0
                                            $ action_speed = 0

                                    "Show her feet" if not ShowFeet and JeanX.Pose == "doggy":
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and JeanX.Pose == "doggy":
                                            $ ShowFeet = 0

                                    "Undress [JeanX.name]":
                                            call Girl_Undress(JeanX)
                                    "Clean up [JeanX.name] (locked)" if not JeanX.Spunk:
                                            pass
                                    "Clean up [JeanX.name]" if JeanX.Spunk:
                                            call Girl_Cleanup(JeanX,"ask")
                                    "Never mind":
                                            jump Jean_Anal_Cycle

                        "Back to Sex Menu" if multi_action:
                                    ch_p "Let's try something else."
                                    call Jean_Sex_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Jean_AnalAfter
                        "End Scene" if not multi_action:
                                    ch_p "Let's stop for now."
                                    call Jean_Sex_Reset
                                    $ line = 0
                                    jump Jean_AnalAfter
        #End menu (if line)

        call Shift_Focus(JeanX)
        call Sex_Dialog(JeanX,Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JeanX.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JeanX)
                            if "angry" in JeanX.recent_history:
                                call Jean_Sex_Reset
                                return
                            $ JeanX.change_stat("lust", 200, 5)
                            if 100 > JeanX.lust >= 70 and JeanX.OCount < 2:
                                    $ JeanX.recent_history.append("unsatisfied")
                                    $ JeanX.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jean_AnalAfter
                            $ line = "came"

                    if JeanX.lust >= 100:
                            #If you're still going at it and Jean can cum
                            call Girl_Cumming(JeanX)
                            if action_context == "shift" or "angry" in JeanX.recent_history:
                                jump Jean_AnalAfter

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Jean_AnalAfter
                            elif "unsatisfied" in JeanX.recent_history:
                                #And Jean is unsatisfied,
                                $ line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ line = "You get back into it"
                                        jump Jean_Anal_Cycle
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Jean_AnalAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Jean_AnalAfter
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if JeanX.SEXP >= 100 or ApprovalCheck(JeanX, 1200, "LO"):
            pass
        elif counter == (5 + JeanX.Anal):
                    $ JeanX.Brows = "confused"
                    ch_j "Ok, that good enough?"
        elif counter == (10 + JeanX.Anal):
                    $ JeanX.Brows = "angry"
                    menu:
                        ch_j "Can we. . . do something. . . else?"
                        "How about a BJ?" if JeanX.Action and multi_action:
                                $ action_context = "shift"
                                call Jean_AnalAfter
                                call Jean_Blowjob
                        "How about a Handy?" if JeanX.Action and multi_action:
                                $ action_context = "shift"
                                call Jean_AnalAfter
                                call Jean_Handjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ counter += 1
                                jump Jean_Anal_Cycle
                        "Let's try something else." if multi_action:
                                $ line = 0
                                call Jean_Sex_Reset
                                $ action_context = "shift"
                                jump Jean_AnalAfter
                        "No, get back down there.":
                                if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                                    $ JeanX.change_stat("love", 200, -5)
                                    $ JeanX.change_stat("obedience", 50, 3)
                                    $ JeanX.change_stat("obedience", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    $ JeanX.change_face("angry", 1)
                                    call Jean_Sex_Reset
                                    "She scowls at you and pulls out."
                                    ch_j "Don't overestimate yourself."
                                    $ JeanX.change_stat("love", 50, -3, 1)
                                    $ JeanX.change_stat("love", 80, -4, 1)
                                    $ JeanX.change_stat("obedience", 30, -1, 1)
                                    $ JeanX.change_stat("obedience", 50, -1, 1)
                                    $ JeanX.recent_history.append("angry")
                                    $ JeanX.daily_history.append("angry")
                                    jump Jean_AnalAfter
        #End Count check

        if Round == 10:
                call Sex_Basic_Dialog(JeanX,10) #"You might want to wrap this up, it's getting late."
        elif Round == 5:
                call Sex_Basic_Dialog(JeanX,5)   #"Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ JeanX.change_face("bemused", 0)
    $ line = 0
    call Sex_Basic_Dialog(JeanX,"done")   #"Ok, [Girl.Petname], that's enough of that for now."



# Jean hotdog //////////////////////////////////////////////////////////////////////

label Jean_Sex_H:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JeanX)
    if JeanX.Hotdog >= 3: #You've done it before several times
        $ temp_modifier += 10
    elif JeanX.Hotdog: #You've done it before
        $ temp_modifier += 5

    if JeanX.lust > 85:
        $ temp_modifier += 10
    elif JeanX.lust > 75: #She's really horny
        $ temp_modifier += 5
    if action_context == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in JeanX.Traits:
        $ temp_modifier += (3*Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JeanX.Traits:
        $ temp_modifier -= 40
    if JeanX.ForcedCount and not JeanX.Forced:
        $ temp_modifier -= 5 * JeanX.ForcedCount

    if JeanX.Taboo and "tabno" in JeanX.daily_history:
        $ temp_modifier -= 10

    if "no hotdog" in JeanX.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no hotdog" in JeanX.recent_history else 0

    $ Approval = ApprovalCheck(JeanX, 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)

    if action_context == "auto":
            call Jean_Sex_Launch("hotdog")
            "You push [JeanX.name] down, and press your cock against her."
            $ JeanX.change_face("surprised", 1)

            if (JeanX.Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
                "[JeanX.name] glances back and then breaks into a smile."
                $ JeanX.change_face("sly")
                $ JeanX.change_stat("obedience", 70, 3)
                $ JeanX.change_stat("inhibition", 50, 3)
                $ JeanX.change_stat("inhibition", 70, 1)
                ch_j "Oh, what did you have in mind with that? . ."
                jump Jean_HotdogPrep
            else:                                                                                                            #she's questioning it
                $ JeanX.Brows = "angry"
                menu:
                    ch_j "Little close there, [JeanX.Petname]?"
                    "Sorry, sorry! Never mind.":
                        if Approval:
                            $ JeanX.change_face("sexy", 1)
                            $ JeanX.change_stat("obedience", 70, 3)
                            $ JeanX.change_stat("inhibition", 50, 3)
                            $ JeanX.change_stat("inhibition", 70, 1)
                            ch_j "I didn't say I minded. . ."
                            jump Jean_HotdogPrep
                        "You pull back from her."
                        $ JeanX.change_face("bemused", 1)
                        ch_j "Just ask first."
                    "You'll see.":
                        $ JeanX.change_stat("love", 80, -10, 1)
                        $ JeanX.change_stat("love", 200, -8)
                        "You grind against her crotch."
                        $ JeanX.change_stat("obedience", 70, 3)
                        $ JeanX.change_stat("inhibition", 50, 3)
                        if not ApprovalCheck(JeanX, 500, "O", TabM=1): #Checks if obedience is 700+
                            $ JeanX.change_face("angry")
                            "[JeanX.name] shoves you away."
                            ch_j "Don't push it, [JeanX.Petname]."
                            $ JeanX.change_stat("love", 50, -10, 1)
                            $ JeanX.change_stat("obedience", 50, 3)
                            $ renpy.pop_call()
                            if action_context:
                                $ renpy.pop_call()
                            call Jean_Sex_Reset
                            $ JeanX.recent_history.append("angry")
                            $ JeanX.daily_history.append("angry")
                        else:
                            $ JeanX.change_face("sad")
                            "[JeanX.name] doesn't seem to be into this, but she knows her place."
                            jump Jean_HotdogPrep
            return
            #end auto


    if not JeanX.Hotdog and "no hotdog" not in JeanX.recent_history:
            #first time
            $ JeanX.change_face("surprised", 1)
            $ JeanX.Mouth = "kiss"
            ch_j "What, just grinding?"

            if JeanX.Forced:
                $ JeanX.change_face("sad")
                ch_j ". . . nothing more?"
                if Approval:
                    ch_j "Which of us has a pussy here?"


    if not JeanX.Hotdog and Approval:
            #First time dialog
            if JeanX.Forced:
                $ JeanX.change_face("sad")
                $ JeanX.change_stat("love", 70, -3, 1)
                $ JeanX.change_stat("love", 20, -2, 1)
            elif JeanX.love >= (JeanX.obedience + JeanX.inhibition - JeanX.IX):
                $ JeanX.change_face("sexy")
                $ JeanX.Brows = "sad"
                $ JeanX.Mouth = "smile"
                ch_j "Ok, we can start with that. . ."
            elif JeanX.obedience >= (JeanX.inhibition - JeanX.IX):
                $ JeanX.change_face("normal")
                ch_j "Ok, we can start with that. . ."
            elif JeanX.Addict >= 50:
                $ JeanX.change_face("manic", 1)
                ch_j "Hrmm. . ."
            else: # Uninhibited
                $ JeanX.change_face("sad")
                $ JeanX.Mouth = "smile"
                ch_j "Ok, we can start with that. . ."

    elif Approval:
            #Second time+ dialog
            if JeanX.Forced:
                $ JeanX.change_face("sad")
                $ JeanX.change_stat("love", 70, -3, 1)
                $ JeanX.change_stat("love", 20, -2, 1)
                ch_j "Odd. . ."
            elif not JeanX.Taboo and "tabno" in JeanX.daily_history:
                ch_j "I guess this is a better location . ."
            elif "hotdog" in JeanX.recent_history:
                $ JeanX.change_face("sexy", 1)
                ch_j "Again? Fine, whatever."
                jump Jean_HotdogPrep
            elif "hotdog" in JeanX.daily_history:
                $ JeanX.change_face("sexy", 1)
                $ line = renpy.random.choice(["Back again so soon?",
                    "So you'd like another round?",
                    "You're really into this. . .",
                    "Are you sure that's all you want?"])
                ch_j "[line]"
            else:
                $ JeanX.change_face("sexy", 1)
                $ JeanX.ArmPose = 2
                $ line = renpy.random.choice(["Oooh, you want some of this?",
                    "So you'd like another round?",
                    "You're really into this. . .",
                    "You want another rub?"])
                ch_j "[line]"
            $ line = 0

    if Approval >= 2:
            #She's into it. . .
            if JeanX.Forced:
                $ JeanX.change_face("sad")
                $ JeanX.change_stat("obedience", 80, 1)
                $ JeanX.change_stat("inhibition", 60, 1)
                ch_j "Ok, fine."
            elif "no hotdog" in JeanX.daily_history:
                ch_j "It was fun enough. . ."
            else:
                $ JeanX.change_face("sexy", 1)
                $ JeanX.change_stat("love", 80, 1)
                $ JeanX.change_stat("inhibition", 50, 2)
                $ line = renpy.random.choice(["Well, sure, let me give it a rub.",
                    "Very well.",
                    "Nice!",
                    "I guess we could do that.",
                    "Ok, let me. . .",
                    "Heh, ok, ok."])
                ch_j "[line]"
                $ line = 0
            $ JeanX.change_stat("obedience", 60, 1)
            $ JeanX.change_stat("inhibition", 70, 2)
            jump Jean_HotdogPrep

    else:
            #She's not into it, but maybe. . .
            $ JeanX.change_face("angry")
            if "no hotdog" in JeanX.recent_history:
                ch_j "I don't repeat myself."
            elif JeanX.Taboo and "tabno" in JeanX.daily_history and "no hotdog" in JeanX.daily_history:
                ch_j "I just told you. . .not in such an exposed location."
            elif "no hotdog" in JeanX.daily_history:
                ch_j "I'm believe I just told you \"no,\" [JeanX.Petname]."
            elif JeanX.Taboo and "tabno" in JeanX.daily_history:
                ch_j "I'm not comfortable with that. . ."
            elif not JeanX.Hotdog:
                $ JeanX.change_face("bemused")
                ch_j "Hmm, that could be amusing, [JeanX.Petname]. . ."
            else:
                $ JeanX.change_face("bemused")
                ch_j "I don't think that would be appropriate. . ."
            menu:
                extend ""
                "Sorry, never mind." if "no hotdog" in JeanX.daily_history:
                    $ JeanX.change_face("bemused")
                    ch_j "So long as you don't push it."
                    return
                "Maybe later?" if "no hotdog" not in JeanX.daily_history:
                    $ JeanX.change_face("sexy")
                    ch_j "I guess eventually. . ."
                    $ JeanX.change_stat("love", 80, 1)
                    $ JeanX.change_stat("inhibition", 50, 1)
                    if JeanX.Taboo:
                        $ JeanX.recent_history.append("tabno")
                        $ JeanX.daily_history.append("tabno")
                    $ JeanX.recent_history.append("no hotdog")
                    $ JeanX.daily_history.append("no hotdog")
                    return
                "You might like it. . .":
                    if Approval:
                        $ JeanX.change_face("sexy")
                        $ JeanX.change_stat("obedience", 60, 2)
                        $ JeanX.change_stat("inhibition", 50, 2)
                        $ line = renpy.random.choice(["Yeah, probably. . .",
                                "I guess. . .",
                                "Good point. . ."])
                        ch_j "[line]"
                        $ line = 0
                        jump Jean_HotdogPrep
                    else:
                        pass

                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(JeanX, 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                    if Approval > 1 or (Approval and JeanX.Forced):
                        $ JeanX.change_face("confused")
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
                        $ JeanX.recent_history.append("angry")
                        $ JeanX.daily_history.append("angry")

    #She refused all offers.
    $ JeanX.ArmPose = 1

    if "no hotdog" in JeanX.daily_history:
        ch_j "What did I tell you?"
        $ JeanX.recent_history.append("angry")
        $ JeanX.daily_history.append("angry")
    if JeanX.Forced:
        $ JeanX.change_face("angry", 1)
        ch_j "There's no point trying."
        $ JeanX.change_stat("lust", 200, 5)
        if JeanX.love > 300:
                $ JeanX.change_stat("love", 70, -1)
        $ JeanX.change_stat("obedience", 50, -1)
        $ JeanX.recent_history.append("angry")
        $ JeanX.daily_history.append("angry")
    elif JeanX.Taboo:                             # she refuses and this is too public a place for her
        $ JeanX.change_face("angry", 1)
        $ JeanX.recent_history.append("tabno")
        $ JeanX.daily_history.append("tabno")
        ch_j "This area is a bit too exposed for that sort of thing. . ."
        $ JeanX.change_stat("lust", 200, 5)
        $ JeanX.change_stat("obedience", 50, -3)
    elif JeanX.Hotdog:
        $ JeanX.change_face("sad")
        ch_j "Not anymore."
    else:
        $ JeanX.change_face("normal", 1)
        ch_j "No thanks."
    $ JeanX.recent_history.append("no hotdog")
    $ JeanX.daily_history.append("no hotdog")
    $ temp_modifier = 0
    return

label Jean_Hotdog_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(JeanX)
        call Jean_Sex_Launch("hotdog")
        if action_speed >= 4:
            $ action_speed = 2
#            call action_speed_Shift(2)
        $ JeanX.lustFace()
        $ Player.Cock = "out"
        $ Player.Sprite = 1
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
#                                    call action_speed_Shift(1)
                        "action_speed up. . ." if 0 < action_speed < 3:
                                    $ action_speed += 1
#                                    call action_speed_Shift(action_speed+1)
                                    "You ask her to up the pace a bit."
                        "action_speed up. . . (locked)" if action_speed >= 3:
                                    pass

                        "Slow Down. . ." if action_speed:
                                    $ action_speed -= 1
#                                    call action_speed_Shift(action_speed-1)
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not action_speed:
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(JeanX)
                                    $ counter += 1
                                    $ Round -= 1
                                    jump Jean_Hotdog_Cycle
                        "Turn her Around":
                                    $ JeanX.Pose = "doggy" if JeanX.Pose != "doggy" else "sex"
                                    "You turn her around. . ."
                                    jump Jean_Hotdog_Cycle

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
                                            if JeanX.Action and multi_action:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ JeanX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Shift primary action":
                                            if JeanX.Action and multi_action:
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
                                                call Sex_Basic_Dialog(JeanX,"tired")
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [JeanX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(JeanX)
                                            "Ask [JeanX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(JeanX)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(JeanX)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jean_Hotdog_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jean_Hotdog_Cycle
                                            "Never mind":
                                                        jump Jean_Hotdog_Cycle
                                    "Just take a look at her.":
                                            $ Player.Cock = 0
                                            $ action_speed = 0

                                    "Show her feet" if not ShowFeet and JeanX.Pose == "doggy":
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and JeanX.Pose == "doggy":
                                            $ ShowFeet = 0

                                    "Undress [JeanX.name]":
                                            call Girl_Undress(JeanX)
                                    "Clean up [JeanX.name] (locked)" if not JeanX.Spunk:
                                            pass
                                    "Clean up [JeanX.name]" if JeanX.Spunk:
                                            call Girl_Cleanup(JeanX,"ask")
                                    "Never mind":
                                            jump Jean_Hotdog_Cycle

                        "Back to Sex Menu" if multi_action:
                                    ch_p "Let's try something else."
                                    call Jean_Sex_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Jean_HotdogAfter
                        "End Scene" if not multi_action:
                                    ch_p "Let's stop for now."
                                    call Jean_Sex_Reset
                                    $ line = 0
                                    jump Jean_HotdogAfter
        #End menu (if line)

        call Shift_Focus(JeanX)
        call Sex_Dialog(JeanX,Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JeanX.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JeanX)
                            if "angry" in JeanX.recent_history:
                                call Jean_Sex_Reset
                                return
                            $ JeanX.change_stat("lust", 200, 5)
                            if 100 > JeanX.lust >= 70 and JeanX.OCount < 2:
                                    $ JeanX.recent_history.append("unsatisfied")
                                    $ JeanX.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jean_HotdogAfter
                            $ line = "came"

                    if JeanX.lust >= 100:
                            #If you're still going at it and Jean can cum
                            call Girl_Cumming(JeanX)
                            if action_context == "shift" or "angry" in JeanX.recent_history:
                                jump Jean_HotdogAfter

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Jean_HotdogAfter
                            elif "unsatisfied" in JeanX.recent_history:
                                #And Jean is unsatisfied,
                                $ line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ line = "You get back into it"
                                        jump Jean_Hotdog_Cycle
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Jean_HotdogAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Jean_HotdogAfter
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if JeanX.SEXP >= 100 or ApprovalCheck(JeanX, 1200, "LO"):
            pass
        elif counter == (5 + JeanX.Hotdog):
                    $ JeanX.Brows = "confused"
                    ch_j "'bout done there?"
        elif counter == (10 + JeanX.Hotdog):
                    $ JeanX.Brows = "angry"
                    menu:
                        ch_j "Well this is not fun."
                        "How about a BJ?" if JeanX.Action and multi_action:
                                $ action_context = "shift"
                                call Jean_HotdogAfter
                                call Jean_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ counter += 1
                                jump Jean_Hotdog_Cycle
                        "Let's try something else." if multi_action:
                                $ line = 0
                                call Jean_Sex_Reset
                                $ action_context = "shift"
                                jump Jean_HotdogAfter
                        "No, get back down there.":
                                if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                                    $ JeanX.change_stat("love", 200, -5)
                                    $ JeanX.change_stat("obedience", 50, 3)
                                    $ JeanX.change_stat("obedience", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    $ JeanX.change_face("angry", 1)
                                    call Jean_Sex_Reset
                                    "She scowls at you and pulls away."
                                    ch_j "Don't overestimate yourself."
                                    $ JeanX.change_stat("love", 50, -3, 1)
                                    $ JeanX.change_stat("love", 80, -4, 1)
                                    $ JeanX.change_stat("obedience", 30, -1, 1)
                                    $ JeanX.change_stat("obedience", 50, -1, 1)
                                    $ JeanX.recent_history.append("angry")
                                    $ JeanX.daily_history.append("angry")
                                    jump Jean_HotdogAfter
        #End Count check

        call Escalation(JeanX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(JeanX,10) #"You might want to wrap this up, it's getting late."
        elif Round == 5:
                call Sex_Basic_Dialog(JeanX,5)   #"Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ JeanX.change_face("bemused", 0)
    $ line = 0
    call Sex_Basic_Dialog(JeanX,"done")   #"Ok, [Girl.Petname], that's enough of that for now."
