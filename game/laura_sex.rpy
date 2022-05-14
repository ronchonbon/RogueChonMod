# Laura_SexMenu //////////////////////////////////////////////////////////////////////
label Laura_SexAct(Act = 0): #rkeljs
        if AloneCheck(LauraX) and LauraX.Taboo == 20:
                $ LauraX.Taboo = 0
                $ Taboo = 0
        call Shift_Focus(LauraX)
        if Act == "SkipTo":
            $ renpy.pop_call() #causes it to skip past the primary_action Swap
            $ renpy.pop_call() #causes it to skip past the cycle you were in before
            #$ renpy.pop_call() #causes it to skip past the sex menu you were in before that
            call SkipTo(LauraX)
        elif Act == "switch":
            $ renpy.pop_call() #causes it to skip past call here from Sex_Menu_Threesome
            #$ renpy.pop_call() #causes it to skip past call to Sex_Menu_Threesome
            # drops through to sex menu
        elif Act == "masturbate":
            call Laura_M_Prep
            if not action_context:
                return
        elif Act == "lesbian":
            call Les_Prep(LauraX) #nee call Laura_Les_Prep
            if not action_context:
                return
        elif Act == "kissing":
            call KissPrep(LauraX)
            if not action_context:
                return
        elif Act == "breasts":
            call Laura_Fondle_Breasts
            if not action_context:
                return
        elif Act == "blow":
            call Laura_BJ_Prep
            if not action_context:
                return
        elif Act == "hand":
            call Laura_HJ_Prep
            if not action_context:
                return
        elif Act == "sex":
            call Laura_SexPrep
            if not action_context:
                return

##  LauraX.Masturbating //////////////////////////////////////////////////////////////////////
# counter 1 means she's seen you, counter 0 means she hasn't.
label Laura_Masturbate:  #rkelj
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(LauraX)
    if LauraX.Mast:
        $ temp_modifier += 10
    if LauraX.SEXP >= 50:
        $ temp_modifier += 25
    elif LauraX.SEXP >= 30:
        $ temp_modifier += 15
    elif LauraX.SEXP >= 15:
        $ temp_modifier += 5
    if LauraX.lust >= 90:
        $ temp_modifier += 20
    elif LauraX.lust >= 75:
        $ temp_modifier += 5
    if "exhibitionist" in LauraX.Traits:
        $ temp_modifier += (3*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.Petnames:
        $ temp_modifier += 10
    elif "ex" in LauraX.Traits:
        $ temp_modifier -= 40
    if LauraX.ForcedCount and not LauraX.Forced:
        $ temp_modifier -= 5 * LauraX.ForcedCount

    $ Approval = ApprovalCheck(LauraX, 1300, TabM = 2) # 120, 135, 150, Taboo -80(200)

    $ LauraX.DrainWord("unseen",1,0) #She sees you, so remove unseens

    if action_context == "join":       # This triggers if you ask to join in
                $ Player.AddWord(1,"join")
                if Approval > 1 or (Approval and LauraX.lust >= 50):
                    menu:
                        extend ""
                        "Would you like some help? I could lend some helping hands. . ."  if Player.Semen and LauraX.Action:
                                $ LauraX.change_stat("love", 90, 1)
                                $ LauraX.change_stat("obedience", 50, 2)
                                $ LauraX.change_face("sexy")
                                ch_l "Huh. Well I guess you could work the top?"
                                $ LauraX.change_stat("obedience", 70, 2)
                                $ LauraX.change_stat("inhibition", 70, 1)
                                $ offhand_action = "fondle breasts"
                                $ LauraX.Mast += 1
                                jump Laura_M_Cycle
                        "Would you like some help? I could. . . up to you, I guess." if Player.Semen and LauraX.Action:
                                $ LauraX.change_stat("love", 70, 2)
                                $ LauraX.change_stat("love", 90, 1)
                                $ LauraX.change_face("sexy")
                                ch_l "Yeah, I guess? . ."
                                $ LauraX.change_stat("obedience", 70, 2)
                                $ LauraX.change_stat("inhibition", 70, 1)
                                $ D20 = renpy.random.randint(1, 20)
                                if D20 > 10:
                                    $ offhand_action = "fondle breasts"
                                else:
                                    $ offhand_action = "suck breasts"
                                $ LauraX.Mast += 1
                                jump Laura_M_Cycle
                        "Why don't we take care of each other?" if Player.Semen and LauraX.Action:
                                $ LauraX.change_face("sexy")
                                ch_l "Like what?"
                                $ renpy.pop_call()          #removes the call to this label
                                return                      #returns to sexmenu=
                        "You look like you have things well in hand. . .":
                                if LauraX.lust >= 50:
                                    $ LauraX.change_stat("love", 70, 2)
                                    $ LauraX.change_stat("love", 90, 1)
                                    $ LauraX.change_face("sexy")
                                    ch_l "I am getting pretty close. . ."
                                    $ LauraX.change_stat("obedience", 80, 3)
                                    $ LauraX.change_stat("inhibition", 80, 5)
                                    jump Laura_M_Cycle
                                elif ApprovalCheck(LauraX, 1200):
                                    $ LauraX.change_face("sly")
                                    ch_l "Yeah. . . but I can take a break. . ."
                                else:
                                    $ LauraX.change_face("angry")
                                    ch_l "-until you messed it up."

                #else: You've failed all checks so she kicks you out.
                $ LauraX.ArmPose = 1
                $ LauraX.OutfitChange()
                $ LauraX.Action -= 1
                $ Player.change_stat("Focus", 50, 30)
                call Checkout(1)
                $ line = 0
                $ action_context = 0
                $ renpy.pop_call()          #removes the call to this label
                if Approval:
                        $ LauraX.change_face("bemused", 2)
                        if bg_current == "bg_laura":
                            ch_l "Why are you in my room?"
                        else:
                            ch_l "I wasn't expecting company. . ."
                        $ LauraX.Blush = 1
                else:
                        $ LauraX.change_stat("love", 200, -5)
                        $ LauraX.change_face("angry")
                        $ LauraX.recent_history.append("angry")
                        $ LauraX.daily_history.append("angry")
                        if bg_current == "bg_laura":
                            ch_l "I was kinda busy, so get out."
                            "[LauraX.name] kicks you out of her room."
                            $ renpy.pop_call()
                            jump Campus_Map
                        else:
                            ch_l "I'm getting out of here, but maybe knock next time."
                            call Remove_Girl(LauraX)
                return                      #returns to sexmenu, which returns to original
    #End of "Join" option



    if action_context == LauraX:                                                                  #Laura auto-starts
                if Approval > 2:                                                      # fix, add laura auto stuff here
                        if LauraX.wearing_skirt:
                            "[LauraX.name]'s hand snakes down her body, and hikes up her skirt."
                            $ LauraX.Upskirt = 1
                        elif LauraX.PantsNum() >= 6:
                            "[LauraX.name] slides her hand down her body and into her pants."
                        elif LauraX.HoseNum() >= 5:
                            "[LauraX.name]'s hand slides down her body and under her [LauraX.Hose]."
                        elif LauraX.Panties:
                            "[LauraX.name]'s hand slides down her body and under her [LauraX.Panties]."
                        else:
                            "[LauraX.name]'s hand slides down her body and begins to caress her pussy."
                        $ LauraX.SeenPanties = 1
                        call Laura_First_Bottomless(1)
                        "She starts to slowly rub herself."
                        menu:
                            "What do you do?"
                            "Nothing.":
                                    $ LauraX.change_stat("inhibition", 80, 3)
                                    $ LauraX.change_stat("inhibition", 60, 2)
                                    "[LauraX.name] begins to masturbate."
                            "Go for it.":
                                    $ LauraX.change_face("sexy, 1")
                                    $ LauraX.change_stat("inhibition", 80, 3)
                                    ch_p "That is so sexy, [LauraX.Pet]."
                                    $ LauraX.nameCheck() #checks reaction to petname
                                    "You lean back and enjoy the show."
                                    $ LauraX.change_stat("love", 80, 1)
                                    $ LauraX.change_stat("obedience", 90, 1)
                                    $ LauraX.change_stat("obedience", 50, 2)
                            "Ask her to stop.":
                                    $ LauraX.change_face("surprised")
                                    $ LauraX.change_stat("inhibition", 70, 1)
                                    ch_p "Let's not do that right now, [LauraX.Pet]."
                                    $ LauraX.nameCheck() #checks reaction to petname
                                    "[LauraX.name] pulls her hands away from herself."
                                    $ LauraX.OutfitChange()
                                    $ LauraX.change_stat("obedience", 90, 1)
                                    $ LauraX.change_stat("obedience", 50, 1)
                                    $ LauraX.change_stat("obedience", 30, 2)
                                    return
                        jump Laura_M_Prep
                else:
                        $ temp_modifier = 0                               # fix, add laura auto stuff here
                        $ offhand_action = 0
                return
    #End if Laura intitiates this action

    #first time
    if not LauraX.Mast:
            $ LauraX.change_face("surprised", 1)
            $ LauraX.Mouth = "kiss"
            ch_l "So you want me to masturbate while you watch?"
            if LauraX.Forced:
                $ LauraX.change_face("sad")
                ch_l "And you {i}just{/i} want to watch. . ."


    #First time dialog
    if not LauraX.Mast and Approval:
            if LauraX.Forced:
                $ LauraX.change_face("sad")
                $ LauraX.change_stat("love", 70, -3, 1)
                $ LauraX.change_stat("love", 20, -2, 1)
            elif LauraX.love >= LauraX.obedience and LauraX.love >= LauraX.inhibition:
                $ LauraX.change_face("sexy")
                $ LauraX.Brows = "sad"
                $ LauraX.Mouth = "smile"
                ch_l "I don't know, are you sure?"
            elif LauraX.obedience >= LauraX.inhibition:
                $ LauraX.change_face("normal")
                ch_l "If that's what you're into. . ."
            else: # Uninhibited
                $ LauraX.change_face("sad")
                $ LauraX.Mouth = "smile"
                ch_l "I do have some free time. . ."


    #Second time+ initial dialog
    elif Approval:
            if LauraX.Forced:
                $ LauraX.change_face("sad")
                $ LauraX.change_stat("love", 70, -3, 1)
                $ LauraX.change_stat("love", 20, -2, 1)
                ch_l "Hmm, again?"
            elif Approval and "masturbation" in LauraX.recent_history:
                $ LauraX.change_face("sexy", 1)
                ch_l "I have built up some more tension. . ."
                jump Laura_M_Prep
            elif Approval and "masturbation" in LauraX.daily_history:
                $ LauraX.change_face("sexy", 1)
                $ line = renpy.random.choice(["Did you enjoy that?",
                    "Didn't get enough earlier?",
                    "I liked having an audience. . ."])
                ch_l "[line]"
            elif LauraX.Mast < 3:
                $ LauraX.change_face("sexy", 1)
                $ LauraX.Brows = "confused"
                ch_l "Did you. . . like it last time?"
            else:
                $ LauraX.change_face("sexy", 1)
                $ LauraX.ArmPose = 2
                $ line = renpy.random.choice(["You like to watch.",
                    "Again?",
                    "You really like to watch me.",
                    "You want me to masturbate again?"])
                ch_l "[line]"
                $ line = 0
    #End second time+ initial dialog

    #If she's into it. . .
    if Approval >= 2:
            if LauraX.Forced:
                $ LauraX.change_face("sad")
                $ LauraX.change_stat("obedience", 90, 1)
                $ LauraX.change_stat("inhibition", 60, 1)
                ch_l "Whatever. . ."
            else:
                $ LauraX.change_face("sexy", 1)
                $ LauraX.change_stat("love", 90, 1)
                $ LauraX.change_stat("inhibition", 50, 3)
                $ line = renpy.random.choice(["Huh. Ok.",
                    "Couldn't hurt. . .",
                    "Alright.",
                    "Sure.",
                    "Heh, ok."])
                ch_l "[line]"
                $ line = 0
            $ LauraX.change_stat("obedience", 20, 1)
            $ LauraX.change_stat("obedience", 60, 1)
            $ LauraX.change_stat("inhibition", 70, 2)
            jump Laura_M_Prep

    #If she's not into it, but maybe. . .
    else:
        menu:
            ch_l "I don't know that I want to do that right now."
            "Maybe later?":
                    $ LauraX.change_face("sexy", 1)
                    if LauraX.lust > 70:
                        ch_l "I probably will be, but not with an audience."
                    else:
                        ch_l "Hmm, maybe. . ."
                    $ LauraX.change_stat("love", 80, 2)
                    $ LauraX.change_stat("inhibition", 70, 2)
                    return
            "You look like you could use it. . .":
                    if Approval:
                        $ LauraX.change_face("sexy")
                        $ LauraX.change_stat("obedience", 90, 2)
                        $ LauraX.change_stat("obedience", 50, 2)
                        $ LauraX.change_stat("inhibition", 70, 3)
                        $ LauraX.change_stat("inhibition", 40, 2)
                        $ line = renpy.random.choice(["Huh. Ok.",
                                "Couldn't hurt. . .",
                                "Allright.",
                                "Sure.",
                                "Heh, ok."])
                        ch_l "[line]"
                        $ line = 0
                        jump Laura_M_Prep

            "Just get at it already.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(LauraX, 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                    if Approval > 1 or (Approval and LauraX.Forced):
                        $ LauraX.change_face("sad")
                        $ LauraX.change_stat("love", 70, -5, 1)
                        $ LauraX.change_stat("love", 200, -5)
                        ch_l "Whatever."
                        $ LauraX.change_stat("obedience", 80, 4)
                        $ LauraX.change_stat("inhibition", 80, 1)
                        $ LauraX.change_stat("inhibition", 60, 3)
                        $ LauraX.Forced = 1
                        jump Laura_M_Prep
                    else:
                        $ LauraX.change_stat("love", 200, -20)
                        $ LauraX.recent_history.append("angry")
                        $ LauraX.daily_history.append("angry")
    # end of asking her to do it

    #She refused all offers.
    $ LauraX.ArmPose = 1
    if LauraX.Forced:
            $ LauraX.change_face("angry", 1)
            ch_l "This is just too weird for me."
            $ LauraX.change_stat("lust", 90, 5)
            if LauraX.love > 300:
                $ LauraX.change_stat("love", 70, -2)
            $ LauraX.change_stat("obedience", 50, -2)
            $ LauraX.recent_history.append("angry")
            $ LauraX.daily_history.append("angry")
            $ LauraX.recent_history.append("no masturbation")
            $ LauraX.daily_history.append("no masturbation")
            return
    elif Taboo:                             # she refuses and this is too public a place for her
            $ LauraX.change_face("angry", 1)
            $ LauraX.daily_history.append("tabno")
            ch_l "I couldn't do that in public."
            $ LauraX.change_stat("lust", 90, 5)
            $ LauraX.change_stat("obedience", 50, -3)
            return
    elif LauraX.Mast:
            $ LauraX.change_face("sad")
            ch_l "I'm not into it right now."
    else:
            $ LauraX.change_face("normal", 1)
            ch_l "Um, no."
    $ LauraX.recent_history.append("no masturbation")
    $ LauraX.daily_history.append("no masturbation")
    $ temp_modifier = 0
    return

label Laura_M_Prep:  #rkelj
    $ LauraX.Upskirt = 1
    $ LauraX.PantiesDown = 1
    call Laura_First_Bottomless(1)
    call set_the_scene(Dress=0)

    #if she hasn't seen you yet. . .
    if "unseen" in LauraX.recent_history:
            $ LauraX.change_face("sexy")
            $ LauraX.Eyes = "closed"
            $ LauraX.ArmPose = 2
            "You see [LauraX.name] leaning back, masturbating. You don't think she's noticed you yet."
    else:
            $ LauraX.change_face("sexy")
            $ LauraX.ArmPose = 2
            "[LauraX.name] lays back and starts to toy with herself."
            if not LauraX.Mast:#First time
                    if LauraX.Forced:
                        $ LauraX.change_stat("love", 90, -20)
                        $ LauraX.change_stat("obedience", 70, 45)
                        $ LauraX.change_stat("inhibition", 80, 35)
                    else:
                        $ LauraX.change_stat("love", 90, 15)
                        $ LauraX.change_stat("obedience", 70, 35)
                        $ LauraX.change_stat("inhibition", 80, 40)


    $ primary_action = "masturbation"
    if not girl_offhand_action:
        $ girl_offhand_action = "fondle pussy"

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ line = 0
    if Taboo:
        $ LauraX.DrainWord("tabno")
    $ LauraX.DrainWord("no masturbation")
    $ LauraX.recent_history.append("masturbation")
    $ LauraX.daily_history.append("masturbation")

label Laura_M_Cycle:
    if action_context == "join":
        $ renpy.pop_call()
        $ action_context = 0

    while Round > 0:
        call Laura_Pos_Reset("masturbation")
        call Shift_Focus(LauraX)
        $ LauraX.lustFace()
        if "unseen" in LauraX.recent_history and LauraX.Loc == bg_current:
                $ LauraX.Eyes = "closed"
                if LauraX.ScentTimer >= 3:
                        $ LauraX.ScentTimer = 0
                        "[LauraX.name]'s nose twitches and she seems to be sniffing the air."
                        jump Laura_M_Interupted
                $ LauraX.ScentTimer += 1

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep Watching.":
                                pass

                        "[LauraX.name]. . .[[jump in]" if "unseen" not in LauraX.recent_history and "join" not in Player.recent_history and LauraX.Loc == bg_current:
                                "[LauraX.name] slows what she's doing with a sly grin."
                                ch_l "Are you enjoying this?"
                                $ action_context = "join"
                                call Laura_Masturbate
                        "\"Ahem. . .\"" if "unseen" in LauraX.recent_history and LauraX.Loc == bg_current:
                                jump Laura_M_Interupted

                        "Start jack'in it." if offhand_action != "jackin":
                                call Jackin(LauraX)
                        "Stop jack'in it." if offhand_action == "jackin":
                                $ offhand_action = 0

                        "Slap her ass" if LauraX.Loc == bg_current:
                                if "unseen" in LauraX.recent_history:
                                        "You smack [LauraX.name] firmly on the ass!"
                                        jump Laura_M_Interupted
                                else:
                                        call Slap_Ass(LauraX)
                                        $ counter += 1
                                        $ Round -= 1
                                        jump Laura_M_Cycle
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
                                    "Offhand action" if LauraX.Loc == bg_current:
                                            if LauraX.Action and multi_action:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ LauraX.Action -= 1
                                            else:
                                                ch_l "Maybe we could finish this up for now?"

                                    "Threesome actions (locked)" if not Partner or "unseen" in LauraX.recent_history or LauraX.Loc != bg_current:
                                        pass
                                    "Threesome actions" if Partner and "unseen" not in LauraX.recent_history and LauraX.Loc == bg_current:
                                        menu:
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(LauraX)
                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(LauraX)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Laura_M_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Laura_M_Cycle
                                            "Never mind":
                                                        jump Laura_M_Cycle

                                    "Show her feet" if not ShowFeet and LauraX.Pose == "doggy":
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and LauraX.Pose == "doggy":
                                            $ ShowFeet = 0

                                    "Undress [LauraX.name]":
                                            if "unseen" in LauraX.recent_history:
                                                    ch_p "Oh, yeah, take it off. . ."
                                                    jump Laura_M_Interupted
                                            else:
                                                    call Girl_Undress(LauraX)
                                    "Clean up [LauraX.name] (locked)" if not LauraX.Spunk:
                                            pass
                                    "Clean up [LauraX.name]" if LauraX.Spunk:
                                            if "unseen" in LauraX.recent_history:
                                                    ch_p "You've got a little something on you. . ."
                                                    jump Laura_M_Interupted
                                            else:
                                                    call Girl_Cleanup(LauraX,"ask")
                                    "Never mind":
                                                    jump Laura_M_Cycle

                        "Back to Sex Menu" if multi_action and LauraX.Loc == bg_current:
                                    ch_p "Let's try something else."
                                    call Laura_Pos_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Laura_M_Interupted
                        "End Scene" if not multi_action or LauraX.Loc != bg_current:
                                    ch_p "Let's stop for now."
                                    call Laura_Pos_Reset
                                    $ line = 0
                                    jump Laura_M_Interupted
        #End menu (if line)

        call Shift_Focus(LauraX)
        call Sex_Dialog(LauraX,Partner)

        #If either of you could cum

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up

        if Player.Focus >= 100 or LauraX.lust >= 100:
                    #If you can cum:
                    if Player.Focus >= 100:
                        if "unseen" not in LauraX.recent_history:
                            #if she knows you're there
                            call Player_Cumming(LauraX)
                            if "angry" in LauraX.recent_history:
                                call Laura_Pos_Reset
                                return
                            $ LauraX.change_stat("lust", 200, 5)
                            if 100 > LauraX.lust >= 70 and LauraX.OCount < 2:
                                $ LauraX.recent_history.append("unsatisfied")
                                $ LauraX.daily_history.append("unsatisfied")
                            $ line = "came"
                        else: #If she wasn't aware you were there
                            "You grunt and try to hold it in."
                            $ Player.Focus = 95
                            if LauraX.Loc == bg_current:
                                    jump Laura_M_Interupted

                    #If Laura can cum
                    if LauraX.lust >= 100:
                        call Girl_Cumming(LauraX)
                        if LauraX.Loc == bg_current:
                                jump Laura_M_Interupted

                    if line == "came":
                        $ line = 0
                        if not Player.Semen:
                            "You're emptied out, you should probably take a break."
                            $ offhand_action = 0 if offhand_action == "jackin" else offhand_action


                        if "unsatisfied" in LauraX.recent_history:#And Laura is unsatisfied,
                            "[LauraX.name] still seems a bit unsatisfied with the experience."
                            menu:
                                "Let her keep going?"
                                "Yes, keep going for a bit.":
                                    $ line = "You let her get back into it"
                                    jump Laura_M_Cycle
                                "No, I'm done.":
                                    "You ask her to stop."
                                    return
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        if "unseen" in LauraX.recent_history:
                if Round == 10:
                    "It's getting a bit late, [LauraX.name] will probably be wrapping up soon."
                elif Round == 5:
                    "She's definitely going to stop soon."
        else:
                if LauraX.Loc == bg_current:
                        call Escalation(LauraX) #sees if she wants to escalate things

                if Round == 10:
                    ch_l "We might want to wrap this up, it's getting late."
                    $ LauraX.lust += 10
                elif Round == 5:
                    ch_l "Five minutes, maybe."
                    $ LauraX.lust += 25

    #Round = 0 loop breaks
    $ LauraX.change_face("bemused", 0)
    $ line = 0
    if "unseen" not in LauraX.recent_history:
        ch_l "Ok, I'm kinda done for now, I need a break."

label Laura_M_Interupted:

    # If she hasn't noticed you're there before cumming
    if "unseen" in LauraX.recent_history:
                $ LauraX.change_face("surprised", 2)
                "[LauraX.name] stops what she's doing with a start, eyes wide."
                call Laura_First_Bottomless(1)
                $ LauraX.change_face("surprised", 2)

                #If you've been jacking it
                if offhand_action == "jackin":
                        ch_l "Huh."
                        ch_l "When did you get here?"
                        $ LauraX.Eyes = "down"
                        menu:
                            ch_l "And um. . . you have your penis out. . . "
                            "A while back, it was an excellent show.":
                                    $ LauraX.change_face("sexy",1)
                                    $ LauraX.change_stat("obedience", 50, 3)
                                    $ LauraX.change_stat("obedience", 70, 2)
                                    ch_l "Really? Weird. . ."
                                    if LauraX.love >= 800 or LauraX.obedience >= 500 or LauraX.inhibition >= 500:
                                        $ temp_modifier += 10
                                        $ LauraX.change_stat("lust", 90, 5)
                                        ch_l "I um. . . you're not so bad yourself. . ."

                            "I. . . just got here?":
                                    $ LauraX.change_face("angry",1)
                                    $ LauraX.change_stat("love", 70, 2)
                                    $ LauraX.change_stat("love", 90, 1)
                                    $ LauraX.change_stat("obedience", 50, 2)
                                    $ LauraX.change_stat("obedience", 70, 2)
                                    "She looks pointedly at your cock,"
                                    ch_l "Long enough to whip that out?"
                                    if LauraX.love >= 800 or LauraX.obedience >= 500 or LauraX.inhibition >= 500:
                                            $ temp_modifier += 10
                                            $ LauraX.change_stat("lust", 90, 5)
                                            $ LauraX.change_face("bemused", 1)
                                            ch_l "It was really that interesting?"
                                    else:
                                            $ temp_modifier -= 10
                                            $ LauraX.change_stat("lust", 200, -5)
                        call Seen_First_Peen(LauraX,Partner)
                        ch_l "Hmm. . ."

                #you haven't been jacking it
                else:
                        ch_l "Huh."
                        ch_l "When did you get here?"
                        menu:
                            extend ""
                            "A while back.":
                                    $ LauraX.change_face("sexy", 1)
                                    $ LauraX.change_stat("obedience", 50, 3)
                                    $ LauraX.change_stat("obedience", 70, 2)
                                    ch_l "I must have put on a show. . ."
                            "I just got here.":
                                    $ LauraX.change_face("bemused", 1)
                                    $ LauraX.change_stat("love", 70, 2)
                                    $ LauraX.change_stat("love", 90, 1)
                                    ch_l "Uh-huh. . ."
                                    $ LauraX.change_stat("obedience", 50, 2)
                                    $ LauraX.change_stat("obedience", 70, 2)

                $ LauraX.DrainWord("unseen",1,0) #She sees you, so remove unseens
                $ LauraX.Mast += 1
                if Round <= 10:
                    ch_l "I kinda needed a break anyway. . ."
                    return
                $ action_context = "join"
                call Laura_Masturbate
                "error: report this if you see it."
                return #should be redundant
    #End Unseen

    #else, if She's seen you already
    $ LauraX.Action -= 1
    $ LauraX.Mast += 1
    call Checkout
    if action_context == "shift":
        $ action_context = 0
        return
    $ action_context = 0

    if Partner == EmmaX:
        call Partner_Like(LauraX,3)
    else:
        call Partner_Like(LauraX,2)

    if LauraX.Loc != bg_current:
        return

    if Round <= 10:
            ch_l "I need a minute here. . ."
            return
    $ LauraX.change_face("sexy", 1)
    if LauraX.lust < 20:
        ch_l "I guess that worked out, how about you?"
    else:
        ch_l "So, what next?"
    menu:
        extend ""
        "Well, I have something you could take care of. . ." if Player.Semen and LauraX.Action:
                $ action_context = "shift"
                return
        "You could just keep going. . ." if Player.Semen:
                $ LauraX.change_face("sly")
                if LauraX.Action and Round >= 10:
                    ch_l "Ok. . ."
                    jump Laura_M_Cycle
                else:
                    ch_l "I need a minute here. . ."
        "I'm good here. [[Stop]":
                if LauraX.love < 800 and LauraX.inhibition < 500 and LauraX.obedience < 500:
                    $ LauraX.OutfitChange()
                $ LauraX.change_face("normal")
                $ LauraX.Brows = "confused"
                ch_l "Ok."
                $ LauraX.Brows = "normal"
        "You should probably stop for now." if LauraX.lust > 30:
                $ LauraX.change_face("angry")
                ch_l "Hrmm."
    return

## end LauraX.Masturbating ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



# Start Laura Sex pose //////////////////////////////////////////////////////////////////////////////////
# LauraX.Sex_P //////////////////////////////////////////////////////////////////////

label Laura_Sex_P:   #rkelj
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(LauraX)
    if LauraX.Sex >= 7: # She loves it
        $ temp_modifier += 15
    elif LauraX.Sex >= 3: #You've done it before several times
        $ temp_modifier += 12
    elif LauraX.Sex: #You've done it before
        $ temp_modifier += 10

    if LauraX.Addict >= 75 and (LauraX.CreamP + LauraX.CreamA) >=3: #She's really strung out and has creampied
        $ temp_modifier += 20
    elif LauraX.Addict >= 75:
        $ temp_modifier += 15

    if LauraX.lust > 85:
        $ temp_modifier += 10
    elif LauraX.lust > 75: #She's really horny
        $ temp_modifier += 5

    if action_context == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in LauraX.Traits:
        $ temp_modifier += (4*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.Petnames:
        $ temp_modifier += 10
    elif "ex" in LauraX.Traits:
        $ temp_modifier -= 40
    if LauraX.ForcedCount and not LauraX.Forced:
        $ temp_modifier -= 5 * LauraX.ForcedCount



    if Taboo and "tabno" in LauraX.daily_history:
        $ temp_modifier -= 10

    if "no sex" in LauraX.daily_history:
        $ temp_modifier -= 15 if "no sex" in LauraX.recent_history else 5


    $ Approval = ApprovalCheck(LauraX, 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)

    if action_context == "auto":
                call Laura_Sex_Launch("sex")
                if LauraX.wearing_skirt:
                    "You push [LauraX.name] onto her back, sliding her skirt up as you go."
                    $ LauraX.Upskirt = 1
                elif LauraX.PantsNum() >= 6:
                    "You push [LauraX.name] onto her back, sliding her pants down as you do."
                    $ LauraX.Upskirt = 1
                else:
                    "You push [LauraX.name] onto her back."
                $ LauraX.SeenPanties = 1
                "You rub the tip of your cock against her moist slit."
                $ LauraX.change_face("surprised", 1)

                if (LauraX.Sex and Approval) or (Approval > 1):
                    #this is not the first time you've had sex, or she's into it
                    "[LauraX.name] glances down and then breaks into a smile."
                    $ LauraX.change_face("sly")
                    $ LauraX.change_stat("obedience", 70, 3)
                    $ LauraX.change_stat("inhibition", 50, 3)
                    $ LauraX.change_stat("inhibition", 70, 1)
                    ch_l "Fine by me, [LauraX.Petname]."
                    jump Laura_SexPrep
                else:
                    #she's questioning it
                    $ LauraX.Brows = "angry"
                    menu:
                        ch_l "Oh, taking it all the way, are we?"
                        "Sorry, sorry! Never mind.":
                            if Approval:
                                    $ LauraX.change_face("sexy", 1)
                                    $ LauraX.change_stat("obedience", 70, 3)
                                    $ LauraX.change_stat("inhibition", 50, 3)
                                    $ LauraX.change_stat("inhibition", 70, 1)
                                    ch_l "No no, not a problem. . ."
                                    jump Laura_SexPrep
                            else:
                                    "You pull back before you really get it in."
                                    $ LauraX.change_face("bemused", 1)
                                    if LauraX.Sex:
                                        ch_l "Maybe ask first, [LauraX.Petname]?"
                                    else:
                                        ch_l "Maybe if you'd asked first. . ."
                        "Just fucking.":
                            $ LauraX.change_stat("love", 80, -10, 1)
                            $ LauraX.change_stat("love", 200, -10)
                            "You press inside some more."
                            $ LauraX.change_stat("obedience", 70, 3)
                            $ LauraX.change_stat("inhibition", 50, 3)
                            if not ApprovalCheck(LauraX, 700, "O", TabM=1):   #Checks if obedience is 700+
                                $ LauraX.change_face("angry")
                                "[LauraX.name] shoves you away and backhands you in the face."
                                ch_l "Dick."
                                ch_l "Don't push me."
                                $ LauraX.change_stat("love", 50, -10, 1)
                                $ LauraX.change_stat("obedience", 50, 3)
                                $ renpy.pop_call()
                                if action_context:
                                    $ renpy.pop_call()
                                call Laura_Sex_Reset
                                $ LauraX.recent_history.append("angry")
                                $ LauraX.daily_history.append("angry")
                            else:
                                $ LauraX.change_face("sad")
                                "[LauraX.name] doesn't seem to be into this, you're lucky she's so obedient."
                                jump Laura_SexPrep
                return
    #End Auto


    if not LauraX.Sex and "no sex" not in LauraX.recent_history:
            #first time
            $ LauraX.change_face("surprised", 1)
            $ LauraX.Mouth = "kiss"
            ch_l "Huh, you wanna fuck me? . . "
            if LauraX.Forced:
                $ LauraX.change_face("sad")
                ch_l "Pretty bold of you. . ."


    if not LauraX.Sex and Approval:
            #First time dialog
            if LauraX.Forced:
                $ LauraX.change_face("sad")
                $ LauraX.change_stat("love", 70, -30, 1)
                $ LauraX.change_stat("love", 20, -20, 1)
            elif LauraX.love >= (LauraX.obedience + LauraX.inhibition):
                $ LauraX.change_face("sexy")
                $ LauraX.Brows = "sad"
                $ LauraX.Mouth = "smile"
                ch_l "Well, you look so cute when you ask. . ."
            elif LauraX.obedience >= LauraX.inhibition:
                $ LauraX.change_face("normal")
                ch_l "Yes, [LauraX.Petname]. . ."
            elif LauraX.Addict >= 50:
                $ LauraX.change_face("manic", 1)
                ch_l "Sounds fun. . ."
            else: # Uninhibited
                $ LauraX.change_face("sad")
                $ LauraX.Mouth = "smile"
                ch_l "I was hoping you'd ask. . ."
            #End first time dialog

    elif Approval:
            #Second time+ dialog
            $ LauraX.change_face("sexy", 1)
            if LauraX.Forced:
                $ LauraX.change_face("sad")
                $ LauraX.change_stat("love", 70, -3, 1)
                $ LauraX.change_stat("love", 20, -2, 1)
                ch_l "I hope I don't wear you out."
            elif not Taboo and "tabno" in LauraX.daily_history:
                ch_l "Yeah, this is more covert."
            elif "sex" in LauraX.recent_history:
                ch_l "Again? Your funeral."
                jump Laura_SexPrep
            elif "sex" in LauraX.daily_history:
                $ line = renpy.random.choice(["Back again?",
                    "You'd like another round?",
                    "I must be better than I thought.",
                    "Didn't get enough earlier?",
                    "Your funeral, " + LauraX.Petname + "."])
                ch_l "[line]"
            elif LauraX.Sex < 3:
                $ LauraX.Brows = "confused"
                $ LauraX.Mouth = "kiss"
                ch_l "Oh? Another round?"
            else:
                $ line = renpy.random.choice(["Oh, you want some of this?",
                    "You'd like another round?",
                    "I must be better than I thought.",
                    "I hope you don't plan on wearing me out.",
                    "You want to plow me?"])
                ch_l "[line]"
            $ line = 0
            #end Second time+ dialog

    if Approval >= 2:
            #She's into it. . .
            if LauraX.Forced:
                $ LauraX.change_face("sad")
                $ LauraX.change_stat("obedience", 90, 1)
                $ LauraX.change_stat("inhibition", 60, 1)
                ch_l "Ok, fine. Just make it good."
            elif "no sex" in LauraX.daily_history:
                ch_l "Ok, whatever. . ."
            else:
                $ LauraX.change_face("sexy", 1)
                $ LauraX.change_stat("love", 90, 1)
                $ LauraX.change_stat("inhibition", 50, 3)
                $ line = renpy.random.choice(["Well. . . fine, let's do it.",
                    "Sure.",
                    "We could, I guess.",
                    "Hmmm, sure.",
                    "Sounds fun."])
                ch_l "[line]"
                $ line = 0
            $ LauraX.change_stat("obedience", 20, 1)
            $ LauraX.change_stat("obedience", 60, 1)
            $ LauraX.change_stat("inhibition", 70, 2)
            jump Laura_SexPrep

    else:
            #She's not into it, but maybe. . .
            $ LauraX.change_face("angry")
            if "no sex" in LauraX.recent_history:
                ch_l "Sorry, [LauraX.Petname] \"no.\""
            elif Taboo and "tabno" in LauraX.daily_history and "no sex" in LauraX.daily_history:
                ch_l "I told you. . . this place is too exposed."
            elif "no sex" in LauraX.daily_history:
                ch_l "I just told you \"no.\""
            elif Taboo and "tabno" in LauraX.daily_history:
                ch_l "I already told you this is too public!"
            elif not LauraX.Sex:
                $ LauraX.change_face("bemused")
                ch_l "Oh, you have no idea what you're in for. . ."
            else:
                $ LauraX.change_face("bemused")
                ch_l "Maybe later? . ."
            menu:
                extend ""
                "Sorry, never mind." if "no sex" in LauraX.daily_history:
                        $ LauraX.change_face("bemused")
                        ch_l "Well, you are persistant."
                        return
                "Maybe later?" if "no sex" not in LauraX.daily_history:
                        $ LauraX.change_face("sexy")
                        ch_l "Probably. . ."
                        $ LauraX.change_stat("love", 80, 2)
                        $ LauraX.change_stat("inhibition", 70, 2)
                        if Taboo:
                            $ LauraX.recent_history.append("tabno")
                            $ LauraX.daily_history.append("tabno")
                        $ LauraX.recent_history.append("no sex")
                        $ LauraX.daily_history.append("no sex")
                        return
                "I think you'd enjoy it as much as I would. . .":
                        if Approval:
                            $ LauraX.change_face("sexy")
                            $ LauraX.change_stat("obedience", 90, 2)
                            $ LauraX.change_stat("obedience", 50, 2)
                            $ LauraX.change_stat("inhibition", 70, 3)
                            $ LauraX.change_stat("inhibition", 40, 2)
                            $ line = renpy.random.choice(["Yeah, probably. . .",
                                "I guess. . .",
                                "Good point. . ."])
                            ch_l "[line]"
                            $ line = 0
                            jump Laura_SexPrep
                "Just deal with it.":                                               # Pressured into it
                        $ Approval = ApprovalCheck(LauraX, 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
                        if Approval > 1 or (Approval and LauraX.Forced):
                            $ LauraX.change_face("sad")
                            $ LauraX.change_stat("love", 70, -5, 1)
                            $ LauraX.change_stat("love", 200, -5)
                            ch_l "Fine, if it'll shut you up."
                            $ LauraX.change_stat("obedience", 80, 4)
                            $ LauraX.change_stat("inhibition", 80, 1)
                            $ LauraX.change_stat("inhibition", 60, 3)
                            $ LauraX.Forced = 1
                            jump Laura_SexPrep
                        else:
                            $ LauraX.change_stat("love", 200, -20)
                            $ LauraX.recent_history.append("angry")
                            $ LauraX.daily_history.append("angry")
                #end menu
    #end Approval check

    #She refused all offers.
    $ LauraX.ArmPose = 1
    if "no sex" in LauraX.daily_history:
        ch_l "Don't push me."
        $ LauraX.recent_history.append("angry")
        $ LauraX.daily_history.append("angry")
    elif LauraX.Forced:
        $ LauraX.change_face("angry", 1)
        ch_l "I'm over taking orders."
        $ LauraX.change_stat("lust", 200, 5)
        if LauraX.love > 300:
                $ LauraX.change_stat("love", 70, -2)
        $ LauraX.change_stat("obedience", 50, -2)
        $ LauraX.recent_history.append("angry")
        $ LauraX.daily_history.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ LauraX.change_face("angry", 1)
        $ LauraX.recent_history.append("tabno")
        $ LauraX.daily_history.append("tabno")
        ch_l "This place is way too exposed."
        $ LauraX.change_stat("lust", 200, 5)
        $ LauraX.change_stat("obedience", 50, -3)
    elif LauraX.Sex:
        $ LauraX.change_face("sad")
        ch_l "Just jack it or something."
    else:
        $ LauraX.change_face("normal", 1)
        ch_l "Yeah, no."
    $ LauraX.recent_history.append("no sex")
    $ LauraX.daily_history.append("no sex")
    $ temp_modifier = 0
    return

label Laura_Sex_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(LauraX)
        call Laura_Sex_Launch("sex")
        if action_speed >= 4:
            $ action_speed = 2
#            call action_speed_Shift(2)
        $ LauraX.lustFace()
        $ Player.Cock = "in"
        $ primary_action = "sex"
        $ LauraX.Upskirt = 1
        $ LauraX.PantiesDown = 1

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
                                    call Slap_Ass(LauraX)
                                    $ counter += 1
                                    $ Round -= 1
                                    jump Laura_Sex_Cycle

                        "Turn her Around":
                                    $ LauraX.Pose = "doggy" if LauraX.Pose != "doggy" else 0
                                    "You turn her around. . ."
                                    jump Laura_Sex_Cycle

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
                                            if LauraX.Action and multi_action:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ LauraX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")

                                    "Shift primary action":
                                            if LauraX.Action and multi_action:
                                                    menu:
                                                        "How about anal?":
                                                                $ action_context = "shift"
                                                                call Laura_SexAfter
                                                                call Laura_Sex_A
                                                        "Just stick it in her ass [[without asking].":
                                                                $ action_context = "auto"
                                                                call Laura_SexAfter
                                                                call Laura_Sex_A
                                                        "Pull back to hotdog her.":
                                                                $ action_context = "pullback"
                                                                call Laura_SexAfter
                                                                call Laura_Sex_H
                                                        "Never Mind":
                                                                jump Laura_Sex_Cycle
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [LauraX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(LauraX)
                                            "Ask [LauraX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(LauraX)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(LauraX)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Laura_Sex_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Laura_Sex_Cycle
                                            "Never mind":
                                                        jump Laura_Sex_Cycle
                                    "Just take a look at her.":
                                            $ Player.Cock = 0
                                            $ action_speed = 0
                                    "Undress [LauraX.name]":
                                            call Girl_Undress(LauraX)
                                    "Clean up [LauraX.name] (locked)" if not LauraX.Spunk:
                                            pass
                                    "Clean up [LauraX.name]" if LauraX.Spunk:
                                            call Girl_Cleanup(LauraX,"ask")
                                    "Never mind":
                                            jump Laura_Sex_Cycle

                        "Back to Sex Menu" if multi_action:
                                    ch_p "Let's try something else."
                                    call Laura_Sex_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Laura_SexAfter
                        "End Scene" if not multi_action:
                                    ch_p "Let's stop for now."
                                    call Laura_Sex_Reset
                                    $ line = 0
                                    jump Laura_SexAfter
        #End menu (if line)

        call Shift_Focus(LauraX)
        call Sex_Dialog(LauraX,Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or LauraX.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(LauraX)
                            if "angry" in LauraX.recent_history:
                                call Laura_Sex_Reset
                                return
                            $ LauraX.change_stat("lust", 200, 5)
                            if 100 > LauraX.lust >= 70 and LauraX.OCount < 2:
                                    $ LauraX.recent_history.append("unsatisfied")
                                    $ LauraX.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Laura_SexAfter
                            $ line = "came"

                    if LauraX.lust >= 100:
                            #If you're still going at it and Laura can cum
                            call Girl_Cumming(LauraX)
                            if action_context == "shift" or "angry" in LauraX.recent_history:
                                jump Laura_SexAfter

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Laura_SexAfter
                            elif "unsatisfied" in LauraX.recent_history:
                                #And Laura is unsatisfied,
                                $ line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ line = "You get back into it"
                                        jump Laura_Sex_Cycle
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Laura_SexAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Laura_SexAfter
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if LauraX.SEXP >= 100 or ApprovalCheck(LauraX, 1200, "LO"):
            pass
        elif counter == (5 + LauraX.Sex):
                    $ LauraX.Brows = "confused"
                    ch_l "So are we getting close?"
        elif counter == (10 + LauraX.Sex):
                    $ LauraX.Brows = "angry"
                    menu:
                        ch_l "Hey. . . could we. . . try something. . . else?"
                        "How about a BJ?" if LauraX.Action and multi_action:
                                $ action_context = "shift"
                                call Laura_SexAfter
                                call Laura_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ counter += 1
                                jump Laura_Sex_Cycle
                        "Let's try something else." if multi_action:
                                $ line = 0
                                call Laura_Sex_Reset
                                $ action_context = "shift"
                                jump Laura_SexAfter
                        "No, get back down there.":
                                if ApprovalCheck(LauraX, 1200) or ApprovalCheck(LauraX, 500, "O"):
                                    $ LauraX.change_stat("love", 200, -5)
                                    $ LauraX.change_stat("obedience", 50, 3)
                                    $ LauraX.change_stat("obedience", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    $ LauraX.change_face("angry", 1)
                                    call Laura_Sex_Reset
                                    "She scowls at you and pulls out."
                                    ch_l "Not with that attitude."
                                    $ LauraX.change_stat("love", 50, -3, 1)
                                    $ LauraX.change_stat("love", 80, -4, 1)
                                    $ LauraX.change_stat("obedience", 30, -1, 1)
                                    $ LauraX.change_stat("obedience", 50, -1, 1)
                                    $ LauraX.recent_history.append("angry")
                                    $ LauraX.daily_history.append("angry")
                                    jump Laura_SexAfter
        #End Count check

        call Escalation(LauraX) #sees if she wants to escalate things

        if Round == 10:
            ch_l "It's getting kinda late. . ."
        elif Round == 5:
            ch_l "We should take a break for a minute."

    #Round = 0 loop breaks
    $ LauraX.change_face("bemused", 0)
    $ line = 0
    ch_l "Ok, that's enough of that for now."

label Laura_SexAfter:
    if not action_context: #fix  action_context != "shift" and action_context != "auto" and action_context != "pullback":
        $ Player.Sprite = 0
        $ Player.Cock = "out"
        call Laura_Sex_Reset

    $ LauraX.change_face("sexy")

    $ LauraX.Sex += 1
    $ LauraX.Action -=1
    $ LauraX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ LauraX.Addictionrate += 1
    $ LauraX.change_stat("inhibition", 30, 2)
    $ LauraX.change_stat("inhibition", 70, 1)

    call Partner_Like(LauraX,3,2)

    if "Laura Sex Addict" in Achievements:
            pass

    elif LauraX.Sex >= 10:
        $ LauraX.SEXP += 5
        $ Achievements.append("Laura Sex Addict")
        if not action_context:
            $ LauraX.change_face("smile", 1)
            ch_l "We're making this a regular thing, huh. . ."
    elif LauraX.Sex == 1:
            $LauraX.SEXP += 20
            if not action_context:
                if LauraX.love >= 500 and "unsatisfied" not in LauraX.recent_history:
                    ch_l "I can tell, I was the best you've had."
                elif LauraX.obedience <= 500 and Player.Focus <= 20:
                    $ LauraX.Mouth = "sad"
                    ch_l "Satisfied?"
    elif LauraX.Sex == 5:
            ch_l "You know, this was a good idea."
    elif not action_context: #fix  action_context != "shift" and action_context != "auto" and action_context != "pullback":
        if "unsatisfied" in LauraX.recent_history:
            $ LauraX.change_face("angry")
            $ LauraX.Eyes = "side"
            ch_l "Forgetting someone? . ."

    $ temp_modifier = 0
#    if action_context == "shift":
#        ch_l "Did you[LauraX.like]want to try something else?"
    call Checkout
    return

# End laura sex //////////////////////////////////////////////////////////////////////////////////


# Laura anal //////////////////////////////////////////////////////////////////////

label Laura_Sex_A: #rkelj
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(LauraX)
    if LauraX.Anal >= 7: # She loves it
        $ temp_modifier += 20
    elif LauraX.Anal >= 3: #You've done it before several times
        $ temp_modifier += 17
    elif LauraX.Anal: #You've done it before
        $ temp_modifier += 15

    if LauraX.Addict >= 75 and (LauraX.CreamP + LauraX.CreamA) >=3: #She's really strung out and has creampied
        $ temp_modifier += 25
    elif LauraX.Addict >= 75:
        $ temp_modifier += 15

    if LauraX.lust > 85:
        $ temp_modifier += 10
    elif LauraX.lust > 75: #She's really horny
        $ temp_modifier += 5

    $ temp_modifier += 10  # she starts out loose

    if action_context == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in LauraX.Traits:
        $ temp_modifier += (5*Taboo)

    if LauraX in Player.Harem or "sex friend" in LauraX.Petnames:
        $ temp_modifier += 10
    elif "ex" in LauraX.Traits:
        $ temp_modifier -= 40
    if LauraX.ForcedCount and not LauraX.Forced:
        $ temp_modifier -= 5 * LauraX.ForcedCount

    if Taboo and "tabno" in LauraX.daily_history:
        $ temp_modifier -= 10
    if "no anal" in LauraX.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no anal" in LauraX.recent_history else 0

    $ Approval = ApprovalCheck(LauraX, 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)

    if action_context == "auto":
            call Laura_Sex_Launch("anal")
            if LauraX.wearing_skirt:
                "You push [LauraX.name] onto her back, sliding her skirt up as you go."
                $ LauraX.Upskirt = 1
            elif LauraX.PantsNum() >= 6:
                "You push [LauraX.name] onto her back, sliding her pants down as you do."
                $ LauraX.Legs = 0
            else:
                "You push [LauraX.name] onto her back."
            $ LauraX.SeenPanties = 1
            "You press the tip of your cock against her tight rim."
            $ LauraX.change_face("surprised", 1)
            call Laura_First_Bottomless(1)

            if (LauraX.Anal and Approval) or (Approval > 1):
                #this is not the first time you've had sex, or she's into it
                $ LauraX.change_stat("obedience", 70, 3)
                $ LauraX.change_stat("inhibition", 50, 3)
                $ LauraX.change_stat("inhibition", 70, 1)
                "[LauraX.name] glances down and then breaks into a smile."
                ch_l "Yeah, ok. . ."
                jump Laura_AnalPrep
            else:
                #she's questioning it
                $ LauraX.Brows = "angry"
                menu:
                    ch_l "Oh? A backdoor intruder?"
                    "Sorry, sorry! Never mind.":
                        if Approval:
                            $ LauraX.change_face("sexy", 1)
                            $ LauraX.change_stat("obedience", 70, 3)
                            $ LauraX.change_stat("inhibition", 50, 3)
                            $ LauraX.change_stat("inhibition", 70, 1)
                            ch_l "Hey, whatever floats your boat. . ."
                            ch_l "Get in there."
                            jump Laura_AnalPrep
                        "You pull back before you really get it in."
                        $ LauraX.change_face("bemused", 1)

                        if LauraX.Anal:
                            ch_l "You coulda warned me. . ."
                        else:
                            ch_l "Hey, all I expect is a little warning. . ."
                    "Just fucking.":
                        $ LauraX.change_stat("love", 80, -10, 1)
                        $ LauraX.change_stat("love", 200, -8)
                        "You press into her."
                        $ LauraX.change_stat("obedience", 70, 3)
                        $ LauraX.change_stat("inhibition", 50, 3)
                        if not ApprovalCheck(LauraX, 700, "O", TabM=1):
                            $ LauraX.change_face("angry")
                            "[LauraX.name] shoves you away and backhands you in the face."
                            ch_l "Yeah, not like that you won't."
                            $ LauraX.change_stat("love", 50, -10, 1)
                            $ LauraX.change_stat("obedience", 50, 3)
                            $ renpy.pop_call()
                            if action_context:
                                $ renpy.pop_call()
                            call Laura_Sex_Reset
                            $ LauraX.recent_history.append("angry")
                            $ LauraX.daily_history.append("angry")
                        else:
                            $ LauraX.change_face("sad")
                            "[LauraX.name] doesn't seem to be into this, you're lucky she's so obedient."
                            jump Laura_AnalPrep
            return
            #end "auto"


    if not LauraX.Anal and "no anal" not in LauraX.recent_history:
            #first time
            $ LauraX.change_face("surprised", 1)
            $ LauraX.Mouth = "kiss"
            ch_l "Huh, anal?"

            if LauraX.Forced:
                $ LauraX.change_face("sad")
                ch_l "Anal? That's what you're pushing for?"

    if "anal" in LauraX.recent_history:
            $ LauraX.change_face("sexy", 1)
            ch_l "Sure, get in there."
            jump Laura_AnalPrep


    if not LauraX.Anal and Approval:
            #First time dialog
            if LauraX.Forced:
                $ LauraX.change_face("sad")
                $ LauraX.change_stat("love", 70, -3, 1)
                $ LauraX.change_stat("love", 20, -2, 1)
            elif LauraX.love >= (LauraX.obedience + LauraX.inhibition):
                $ LauraX.change_face("sexy")
                $ LauraX.Brows = "sad"
                $ LauraX.Mouth = "smile"
                ch_l "I was hoping you'd ask. . ."
            elif LauraX.obedience >= LauraX.inhibition:
                $ LauraX.change_face("normal")
                ch_l "I expected that. . ."
            elif LauraX.Addict >= 50:
                $ LauraX.change_face("manic", 1)
                ch_l "Hmm, sounds fun. . ."
            else: # Uninhibited
                $ LauraX.change_face("sad")
                $ LauraX.Mouth = "smile"
                ch_l "I was tired of waiting. . ."

    elif Approval:
            #Second time+ dialog
            if LauraX.Forced:
                $ LauraX.change_face("sad")
                $ LauraX.change_stat("love", 70, -3, 1)
                $ LauraX.change_stat("love", 20, -2, 1)
                ch_l "You don't hold back. . ."
            elif not Taboo and "tabno" in LauraX.daily_history:
                ch_l "I guess this is secluded enough. . ."
            elif "anal" in LauraX.daily_history and not LauraX.Loose:
                pass
            elif "anal" in LauraX.recent_history:
                ch_l "I am warmed up. . ."
                jump Laura_AnalPrep
            elif "anal" in LauraX.daily_history:
                $ LauraX.change_face("sexy", 1)
                $ line = renpy.random.choice(["Back again so soon?",
                    "So you'd like another round?",
                    "Again? Sure.",
                    "Didn't get enough earlier?",
                    "Your funeral, " + LauraX.Petname + "."])
                ch_l "[line]"
            else:
                $ LauraX.change_face("sexy", 1)
                $ LauraX.ArmPose = 2
                $ line = renpy.random.choice(["Oooh, you want some of this?",
                    "So you'd like another round?",
                    "I knew you enjoyed it. . .",
                    "I hope you don't plan on wearing me out.",
                    "You want to plow me?"])
                ch_l "[line]"
            $ line = 0

    if Approval >= 2:
            #She's into it. . .
            if LauraX.Forced:
                $ LauraX.change_face("sad")
                $ LauraX.change_stat("obedience", 90, 1)
                $ LauraX.change_stat("inhibition", 60, 1)
                ch_l "Whatever."
            elif "no anal" in LauraX.daily_history:
                ch_l "Well, if you're going to keep asking. . ."
                ch_l "Might be fun. . ."
            else:
                $ LauraX.change_face("sexy", 1)
                $ LauraX.change_stat("love", 90, 1)
                $ LauraX.change_stat("inhibition", 50, 3)
                $ line = renpy.random.choice(["Well. . . ok.",
                    "Sure.",
                    "You could, I guess.",
                    "Um, yeah.",
                    "Heh, ok, ok."])
                ch_l "[line]"
                $ line = 0
            $ LauraX.change_stat("obedience", 20, 1)
            $ LauraX.change_stat("obedience", 60, 1)
            $ LauraX.change_stat("inhibition", 70, 2)
            jump Laura_AnalPrep

    else:
            #She's not into it, but maybe. . .
            $ LauraX.change_face("angry")
            if "no anal" in LauraX.recent_history:
                ch_l "Sorry, [LauraX.Petname] \"no.\""
            elif Taboo and "tabno" in LauraX.daily_history and "no anal" in LauraX.daily_history:
                ch_l "I told you. . . this place is too exposed."
            elif "no anal" in LauraX.daily_history:
                ch_l "I just told you \"no.\""
            elif Taboo and "tabno" in LauraX.daily_history:
                ch_l "I already told you this is too public!"
            elif not LauraX.Anal:
                $ LauraX.change_face("bemused")
                ch_l "I don't know that you're ready for that yet."
            else:
                $ LauraX.change_face("bemused")
                ch_l "Maybe eventually. . ."
            menu:
                extend ""
                "Sorry, never mind." if "no anal" in LauraX.daily_history:
                    $ LauraX.change_face("bemused")
                    ch_l "Hey, I can't blame you."
                    return
                "Maybe later?" if "no anal" not in LauraX.daily_history:
                    $ LauraX.change_face("sexy")
                    ch_l "Oh, probably. . ."
                    ch_l ". . . often."
                    $ LauraX.change_stat("love", 80, 2)
                    $ LauraX.change_stat("inhibition", 70, 2)
                    if Taboo:
                        $ LauraX.recent_history.append("tabno")
                        $ LauraX.daily_history.append("tabno")
                    $ LauraX.recent_history.append("no anal")
                    $ LauraX.daily_history.append("no anal")
                    return
                "I bet it would feel really good. . .":
                    if Approval:
                        $ LauraX.change_face("sexy")
                        $ LauraX.change_stat("obedience", 90, 2)
                        $ LauraX.change_stat("obedience", 50, 2)
                        $ LauraX.change_stat("inhibition", 70, 3)
                        $ LauraX.change_stat("inhibition", 40, 2)
                        $ line = renpy.random.choice(["Yeah, probably. . .",
                                "I guess. . .",
                                "Good point. . ."])
                        ch_l "[line]"
                        $ line = 0
                        jump Laura_AnalPrep
                    else:
                        pass

                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(LauraX, 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
                    if Approval > 1 or (Approval and LauraX.Forced):
                        $ LauraX.change_face("sad")
                        $ LauraX.change_stat("love", 70, -5, 1)
                        $ LauraX.change_stat("love", 200, -5)
                        ch_l "Oh fine, get it over with."
                        $ LauraX.change_stat("obedience", 80, 4)
                        $ LauraX.change_stat("inhibition", 80, 1)
                        $ LauraX.change_stat("inhibition", 60, 3)
                        $ LauraX.Forced = 1
                        jump Laura_AnalPrep
                    else:
                        $ LauraX.change_stat("love", 200, -20)
                        $ LauraX.recent_history.append("angry")
                        $ LauraX.daily_history.append("angry")

    #She refused all offers.
    $ LauraX.ArmPose = 1
    if "no anal" in LauraX.daily_history:
        ch_l "Don't push it."
        $ LauraX.recent_history.append("angry")
        $ LauraX.daily_history.append("angry")
    elif LauraX.Forced:
        $ LauraX.change_face("angry", 1)
        ch_l "You're going too far."
        $ LauraX.change_stat("lust", 200, 5)
        if LauraX.love > 300:
                $ LauraX.change_stat("love", 70, -2)
        $ LauraX.change_stat("obedience", 50, -2)
        $ LauraX.recent_history.append("angry")
        $ LauraX.daily_history.append("angry")
    elif Taboo:
        # she refuses and this is too public a place for her
        $ LauraX.change_face("angry", 1)
        $ LauraX.recent_history.append("tabno")
        $ LauraX.daily_history.append("tabno")
        ch_l "This place is way too exposed."
        $ LauraX.change_stat("lust", 200, 5)
        $ LauraX.change_stat("obedience", 50, -3)
    elif "anal" in LauraX.daily_history:
        $ LauraX.change_face("bemused")
        ch_l "Not right now."
    elif LauraX.Anal:
        $ LauraX.change_face("sad")
        ch_l "You'll have to earn it."
    else:
        $ LauraX.change_face("normal", 1)
        ch_l "You haven't earned it yet."
    $ LauraX.recent_history.append("no anal")
    $ LauraX.daily_history.append("no anal")
    $ temp_modifier = 0
    return

label Laura_Anal_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(LauraX)
        call Laura_Sex_Launch("anal")
        if action_speed >= 4:
            $ Shift = 2
#            call action_speed_Shift(2)
        $ LauraX.lustFace()
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
                                    call Slap_Ass(LauraX)
                                    $ counter += 1
                                    $ Round -= 1
                                    jump Laura_Anal_Cycle

                        "Turn her Around":
                                    $ LauraX.Pose = "doggy" if LauraX.Pose != "doggy" else 0
                                    "You turn her around. . ."
                                    jump Laura_Anal_Cycle

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
                                            if LauraX.Action and multi_action:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ LauraX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")

                                    "Shift primary action":
                                            if LauraX.Action and multi_action:
                                                    menu:
                                                        "How about sex?":
                                                                $ action_context = "shift"
                                                                call Laura_AnalAfter
                                                                call Laura_Sex_P
                                                        "Just stick it in her pussy [[without asking].":
                                                                $ action_context = "auto"
                                                                call Laura_AnalAfter
                                                                call Laura_Sex_P
                                                        "Pull back to hotdog her.":
                                                                $ action_context = "pullback"
                                                                call Laura_AnalAfter
                                                                call Laura_Sex_H
                                                        "Never Mind":
                                                                jump Laura_Anal_Cycle
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [LauraX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(LauraX)
                                            "Ask [LauraX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(LauraX)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(LauraX)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Laura_Anal_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Laura_Anal_Cycle
                                            "Never mind":
                                                        jump Laura_Anal_Cycle
                                    "Just take a look at her.":
                                            $ Player.Cock = 0
                                            $ action_speed = 0

                                    "Show her feet" if not ShowFeet and LauraX.Pose == "doggy":
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and LauraX.Pose == "doggy":
                                            $ ShowFeet = 0

                                    "Undress [LauraX.name]":
                                            call Girl_Undress(LauraX)
                                    "Clean up [LauraX.name] (locked)" if not LauraX.Spunk:
                                            pass
                                    "Clean up [LauraX.name]" if LauraX.Spunk:
                                            call Girl_Cleanup(LauraX,"ask")
                                    "Never mind":
                                            jump Laura_Anal_Cycle

                        "Back to Sex Menu" if multi_action:
                                    ch_p "Let's try something else."
                                    call Laura_Sex_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Laura_AnalAfter
                        "End Scene" if not multi_action:
                                    ch_p "Let's stop for now."
                                    call Laura_Sex_Reset
                                    $ line = 0
                                    jump Laura_AnalAfter
        #End menu (if line)

        call Shift_Focus(LauraX)
        call Sex_Dialog(LauraX,Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or LauraX.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(LauraX)
                            if "angry" in LauraX.recent_history:
                                call Laura_Sex_Reset
                                return
                            $ LauraX.change_stat("lust", 200, 5)
                            if 100 > LauraX.lust >= 70 and LauraX.OCount < 2:
                                    $ LauraX.recent_history.append("unsatisfied")
                                    $ LauraX.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Laura_AnalAfter
                            $ line = "came"

                    if LauraX.lust >= 100:
                            #If you're still going at it and Laura can cum
                            call Girl_Cumming(LauraX)
                            if action_context == "shift" or "angry" in LauraX.recent_history:
                                jump Laura_AnalAfter

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Laura_AnalAfter
                            elif "unsatisfied" in LauraX.recent_history:
                                #And Laura is unsatisfied,
                                $ line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ line = "You get back into it"
                                        jump Laura_Anal_Cycle
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Laura_AnalAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Laura_AnalAfter
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if LauraX.SEXP >= 100 or ApprovalCheck(LauraX, 1200, "LO"):
            pass
        elif counter == (5 + LauraX.Anal):
                    $ LauraX.Brows = "confused"
                    ch_l "We getting close here?"
        elif counter == (10 + LauraX.Anal):
                    $ LauraX.Brows = "angry"
                    menu:
                        ch_l "Can we. . . do something. . . else?"
                        "How about a BJ?" if LauraX.Action and multi_action:
                                $ action_context = "shift"
                                call Laura_AnalAfter
                                call Laura_Blowjob
                        "How about a Handy?" if LauraX.Action and multi_action:
                                $ action_context = "shift"
                                call Laura_AnalAfter
                                call Laura_Handjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ counter += 1
                                jump Laura_Anal_Cycle
                        "Let's try something else." if multi_action:
                                $ line = 0
                                call Laura_Sex_Reset
                                $ action_context = "shift"
                                jump Laura_AnalAfter
                        "No, get back down there.":
                                if ApprovalCheck(LauraX, 1200) or ApprovalCheck(LauraX, 500, "O"):
                                    $ LauraX.change_stat("love", 200, -5)
                                    $ LauraX.change_stat("obedience", 50, 3)
                                    $ LauraX.change_stat("obedience", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    $ LauraX.change_face("angry", 1)
                                    call Laura_Sex_Reset
                                    "She scowls at you and pulls out."
                                    ch_l "Not with that attitude."
                                    $ LauraX.change_stat("love", 50, -3, 1)
                                    $ LauraX.change_stat("love", 80, -4, 1)
                                    $ LauraX.change_stat("obedience", 30, -1, 1)
                                    $ LauraX.change_stat("obedience", 50, -1, 1)
                                    $ LauraX.recent_history.append("angry")
                                    $ LauraX.daily_history.append("angry")
                                    jump Laura_AnalAfter
        #End Count check

        if Round == 10:
            ch_l "It's getting kinda late. . ."
        elif Round == 5:
            ch_l "We should take a break for a minute."

    #Round = 0 loop breaks
    $ LauraX.change_face("bemused", 0)
    $ line = 0
    ch_l "Ok, that's enough of that for now."

# Laura hotdog //////////////////////////////////////////////////////////////////////

label Laura_Sex_H: #rkelj
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(LauraX)
    if LauraX.Hotdog >= 3: #You've done it before several times
        $ temp_modifier += 10
    elif LauraX.Hotdog: #You've done it before
        $ temp_modifier += 5

    if LauraX.lust > 85:
        $ temp_modifier += 10
    elif LauraX.lust > 75: #She's really horny
        $ temp_modifier += 5
    if action_context == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in LauraX.Traits:
        $ temp_modifier += (3*Taboo)
    if LauraX in Player.Harem or "sex friend" in LauraX.Petnames:
        $ temp_modifier += 10
    elif "ex" in LauraX.Traits:
        $ temp_modifier -= 40
    if LauraX.ForcedCount and not LauraX.Forced:
        $ temp_modifier -= 5 * LauraX.ForcedCount

    if Taboo and "tabno" in LauraX.daily_history:
        $ temp_modifier -= 10

    if "no hotdog" in LauraX.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no hotdog" in LauraX.recent_history else 0

    $ Approval = ApprovalCheck(LauraX, 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)

    if action_context == "auto":
            call Laura_Sex_Launch("hotdog")
            "You push [LauraX.name] down, and press your cock against her."
            $ LauraX.change_face("surprised", 1)

            if (LauraX.Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
                "[LauraX.name] glances down and then breaks into a smile."
                $ LauraX.change_face("sly")
                $ LauraX.change_stat("obedience", 70, 3)
                $ LauraX.change_stat("inhibition", 50, 3)
                $ LauraX.change_stat("inhibition", 70, 1)
                ch_l "Oh, what did you have in mind with that? . ."
                jump Laura_HotdogPrep
            else:                                                                                                            #she's questioning it
                $ LauraX.Brows = "angry"
                menu:
                    ch_l "You might want to take a step back, [LauraX.Petname]?"
                    "Sorry, sorry! Never mind.":
                        if Approval:
                            $ LauraX.change_face("sexy", 1)
                            $ LauraX.change_stat("obedience", 70, 3)
                            $ LauraX.change_stat("inhibition", 50, 3)
                            $ LauraX.change_stat("inhibition", 70, 1)
                            ch_l "Or not. . ."
                            jump Laura_HotdogPrep
                        "You pull back from her."
                        $ LauraX.change_face("bemused", 1)
                        ch_l "Maybe ask first?"
                    "You'll see.":
                        $ LauraX.change_stat("love", 80, -10, 1)
                        $ LauraX.change_stat("love", 200, -8)
                        "You grind against her crotch."
                        $ LauraX.change_stat("obedience", 70, 3)
                        $ LauraX.change_stat("inhibition", 50, 3)
                        if not ApprovalCheck(LauraX, 500, "O", TabM=1): #Checks if obedience is 700+
                            $ LauraX.change_face("angry")
                            "[LauraX.name] shoves you away."
                            ch_l "Don't push it, [LauraX.Petname]."
                            $ LauraX.change_stat("love", 50, -10, 1)
                            $ LauraX.change_stat("obedience", 50, 3)
                            $ renpy.pop_call()
                            if action_context:
                                $ renpy.pop_call()
                            call Laura_Sex_Reset
                            $ LauraX.recent_history.append("angry")
                            $ LauraX.daily_history.append("angry")
                        else:
                            $ LauraX.change_face("sad")
                            "[LauraX.name] doesn't seem to be into this, but she knows her place."
                            jump Laura_HotdogPrep
            return
            #end auto


    if not LauraX.Hotdog and "no hotdog" not in LauraX.recent_history:
            #first time
            $ LauraX.change_face("surprised", 1)
            $ LauraX.Mouth = "kiss"
            ch_l "What, just grinding?"

            if LauraX.Forced:
                $ LauraX.change_face("sad")
                ch_l ". . . nothing more?"


    if not LauraX.Hotdog and Approval:
            #First time dialog
            if LauraX.Forced:
                $ LauraX.change_face("sad")
                $ LauraX.change_stat("love", 70, -3, 1)
                $ LauraX.change_stat("love", 20, -2, 1)
            elif LauraX.love >= (LauraX.obedience + LauraX.inhibition):
                $ LauraX.change_face("sexy")
                $ LauraX.Brows = "sad"
                $ LauraX.Mouth = "smile"
                ch_l "If that's what you're into. . ."
            elif LauraX.obedience >= LauraX.inhibition:
                $ LauraX.change_face("normal")
                ch_l "If that's what works for you. . ."
            elif LauraX.Addict >= 50:
                $ LauraX.change_face("manic", 1)
                ch_l "Hrmm. . ."
            else: # Uninhibited
                $ LauraX.change_face("sad")
                $ LauraX.Mouth = "smile"
                ch_l "Well if that's what gets you off. . ."

    elif Approval:
            #Second time+ dialog
            if LauraX.Forced:
                $ LauraX.change_face("sad")
                $ LauraX.change_stat("love", 70, -3, 1)
                $ LauraX.change_stat("love", 20, -2, 1)
                ch_l "That's pushing it. . ."
            elif not Taboo and "tabno" in LauraX.daily_history:
                ch_l "I guess this is a better location . ."
            elif "hotdog" in LauraX.recent_history:
                $ LauraX.change_face("sexy", 1)
                ch_l "Again? Fine, whatever."
                jump Laura_HotdogPrep
            elif "hotdog" in LauraX.daily_history:
                $ LauraX.change_face("sexy", 1)
                $ line = renpy.random.choice(["Back again so soon?",
                    "So you'd like another round?",
                    "You're really into this. . .",
                    "Are you sure that's all you want?"])
                ch_l "[line]"
            else:
                $ LauraX.change_face("sexy", 1)
                $ LauraX.ArmPose = 2
                $ line = renpy.random.choice(["Oooh, you want some of this?",
                    "So you'd like another round?",
                    "You're really into this. . .",
                    "You want another rub?"])
                ch_l "[line]"
            $ line = 0

    if Approval >= 2:
            #She's into it. . .
            if LauraX.Forced:
                $ LauraX.change_face("sad")
                $ LauraX.change_stat("obedience", 80, 1)
                $ LauraX.change_stat("inhibition", 60, 1)
                ch_l "Ok, fine."
            elif "no hotdog" in LauraX.daily_history:
                ch_l "It was rather entertaining. . ."
            else:
                $ LauraX.change_face("sexy", 1)
                $ LauraX.change_stat("love", 80, 1)
                $ LauraX.change_stat("inhibition", 50, 2)
                $ line = renpy.random.choice(["Well, sure, let me give it a rub.",
                    "Very well.",
                    "Nice!",
                    "I guess we could do that.",
                    "Ok, let me. . .",
                    "Heh, ok, ok."])
                ch_l "[line]"
                $ line = 0
            $ LauraX.change_stat("obedience", 60, 1)
            $ LauraX.change_stat("inhibition", 70, 2)
            jump Laura_HotdogPrep

    else:
            #She's not into it, but maybe. . .
            $ LauraX.change_face("angry")
            if "no hotdog" in LauraX.recent_history:
                ch_l "Sorry, [LauraX.Petname] \"no.\""
            elif Taboo and "tabno" in LauraX.daily_history and "no hotdog" in LauraX.daily_history:
                ch_l "I just told you. . .not in such an exposed location."
            elif "no hotdog" in LauraX.daily_history:
                ch_l "I'm believe I just told you \"no,\" [LauraX.Petname]."
            elif Taboo and "tabno" in LauraX.daily_history:
                ch_l "I told you. . . this place is too exposed."
            elif not LauraX.Hotdog:
                $ LauraX.change_face("bemused")
                ch_l "Hmm, that could be amusing, [LauraX.Petname]. . ."
            else:
                $ LauraX.change_face("bemused")
                ch_l "I don't think that would be appropriate. . ."
            menu:
                extend ""
                "Sorry, never mind." if "no hotdog" in LauraX.daily_history:
                    $ LauraX.change_face("bemused")
                    ch_l "So long as you don't push it."
                    return
                "Maybe later?" if "no hotdog" not in LauraX.daily_history:
                    $ LauraX.change_face("sexy")
                    ch_l "I gues eventually. . ."
                    $ LauraX.change_stat("love", 80, 1)
                    $ LauraX.change_stat("inhibition", 50, 1)
                    if Taboo:
                        $ LauraX.recent_history.append("tabno")
                        $ LauraX.daily_history.append("tabno")
                    $ LauraX.recent_history.append("no hotdog")
                    $ LauraX.daily_history.append("no hotdog")
                    return
                "You might like it. . .":
                    if Approval:
                        $ LauraX.change_face("sexy")
                        $ LauraX.change_stat("obedience", 60, 2)
                        $ LauraX.change_stat("inhibition", 50, 2)
                        $ line = renpy.random.choice(["Yeah, probably. . .",
                                "I guess. . .",
                                "Good point. . ."])
                        ch_l "[line]"
                        $ line = 0
                        jump Laura_HotdogPrep
                    else:
                        pass

                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(LauraX, 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                    if Approval > 1 or (Approval and LauraX.Forced):
                        $ LauraX.change_face("sad")
                        $ LauraX.change_stat("love", 70, -2, 1)
                        $ LauraX.change_stat("love", 200, -2)
                        ch_l "Alright, fine."
                        $ LauraX.change_stat("obedience", 80, 4)
                        $ LauraX.change_stat("inhibition", 60, 2)
                        $ LauraX.Forced = 1
                        jump Laura_HotdogPrep
                    else:
                        $ LauraX.change_stat("love", 200, -10)
                        $ LauraX.recent_history.append("angry")
                        $ LauraX.daily_history.append("angry")

    #She refused all offers.
    $ LauraX.ArmPose = 1

    if "no hotdog" in LauraX.daily_history:
        ch_l "What did I tell you?"
        $ LauraX.recent_history.append("angry")
        $ LauraX.daily_history.append("angry")
    if LauraX.Forced:
        $ LauraX.change_face("angry", 1)
        ch_l "There's no point trying."
        $ LauraX.change_stat("lust", 200, 5)
        if LauraX.love > 300:
                $ LauraX.change_stat("love", 70, -1)
        $ LauraX.change_stat("obedience", 50, -1)
        $ LauraX.recent_history.append("angry")
        $ LauraX.daily_history.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ LauraX.change_face("angry", 1)
        $ LauraX.recent_history.append("tabno")
        $ LauraX.daily_history.append("tabno")
        ch_l "This area is a bit too exposed for that sort of thing. . ."
        $ LauraX.change_stat("lust", 200, 5)
        $ LauraX.change_stat("obedience", 50, -3)
    elif LauraX.Hotdog:
        $ LauraX.change_face("sad")
        ch_l "Not anymore."
    else:
        $ LauraX.change_face("normal", 1)
        ch_l "No thanks."
    $ LauraX.recent_history.append("no hotdog")
    $ LauraX.daily_history.append("no hotdog")
    $ temp_modifier = 0
    return

label Laura_Hotdog_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(LauraX)
        call Laura_Sex_Launch("hotdog")
        if action_speed >= 4:
            $ action_speed = 2
#            call action_speed_Shift(2)
        $ LauraX.lustFace()
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
                                    call Slap_Ass(LauraX)
                                    $ counter += 1
                                    $ Round -= 1
                                    jump Laura_Hotdog_Cycle

                        "Turn her Around":
                                    $ LauraX.Pose = "doggy" if LauraX.Pose != "doggy" else 0
                                    "You turn her around. . ."
                                    jump Laura_Hotdog_Cycle

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
                                            if LauraX.Action and multi_action:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ LauraX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")

                                    "Shift primary action":
                                            if LauraX.Action and multi_action:
                                                    menu:
                                                        "How about sex?":
                                                            $ action_context = "shift"
                                                            call Laura_HotdogAfter
                                                            call Laura_Sex_P
                                                        "Just stick it in her pussy [[without asking].":
                                                            $ action_context = "auto"
                                                            call Laura_HotdogAfter
                                                            call Laura_Sex_P
                                                        "How about anal?":
                                                            $ action_context = "shift"
                                                            call Laura_HotdogAfter
                                                            call Laura_Sex_A
                                                        "Just stick it in her ass [[without asking].":
                                                            $ action_context = "auto"
                                                            call Laura_HotdogAfter
                                                            call Laura_Sex_A
                                                        "Never Mind":
                                                                jump Laura_Hotdog_Cycle
                                            else:
                                                call Sex_Basic_Dialog(LauraX,"tired")
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [LauraX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(LauraX)
                                            "Ask [LauraX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(LauraX)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(LauraX)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Laura_Hotdog_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Laura_Hotdog_Cycle
                                            "Never mind":
                                                        jump Laura_Hotdog_Cycle
                                    "Just take a look at her.":
                                            $ Player.Cock = 0
                                            $ action_speed = 0

                                    "Show her feet" if not ShowFeet and LauraX.Pose == "doggy":
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and LauraX.Pose == "doggy":
                                            $ ShowFeet = 0

                                    "Undress [LauraX.name]":
                                            call Girl_Undress(LauraX)
                                    "Clean up [LauraX.name] (locked)" if not LauraX.Spunk:
                                            pass
                                    "Clean up [LauraX.name]" if LauraX.Spunk:
                                            call Girl_Cleanup(LauraX,"ask")
                                    "Never mind":
                                            jump Laura_Hotdog_Cycle

                        "Back to Sex Menu" if multi_action:
                                    ch_p "Let's try something else."
                                    call Laura_Sex_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Laura_HotdogAfter
                        "End Scene" if not multi_action:
                                    ch_p "Let's stop for now."
                                    call Laura_Sex_Reset
                                    $ line = 0
                                    jump Laura_HotdogAfter
        #End menu (if line)

        call Shift_Focus(LauraX)
        call Sex_Dialog(LauraX,Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or LauraX.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(LauraX)
                            if "angry" in LauraX.recent_history:
                                call Laura_Sex_Reset
                                return
                            $ LauraX.change_stat("lust", 200, 5)
                            if 100 > LauraX.lust >= 70 and LauraX.OCount < 2:
                                    $ LauraX.recent_history.append("unsatisfied")
                                    $ LauraX.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Laura_HotdogAfter
                            $ line = "came"

                    if LauraX.lust >= 100:
                            #If you're still going at it and Laura can cum
                            call Girl_Cumming(LauraX)
                            if action_context == "shift" or "angry" in LauraX.recent_history:
                                jump Laura_HotdogAfter

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Laura_HotdogAfter
                            elif "unsatisfied" in LauraX.recent_history:
                                #And Laura is unsatisfied,
                                $ line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ line = "You get back into it"
                                        jump Laura_Hotdog_Cycle
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Laura_HotdogAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Laura_HotdogAfter
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if LauraX.SEXP >= 100 or ApprovalCheck(LauraX, 1200, "LO"):
            pass
        elif counter == (5 + LauraX.Hotdog):
                    $ LauraX.Brows = "confused"
                    ch_l "Are we getting close here?"
        elif counter == (10 + LauraX.Hotdog):
                    $ LauraX.Brows = "angry"
                    menu:
                        ch_l "I'm kinda bored by this."
                        "How about a BJ?" if LauraX.Action and multi_action:
                                $ action_context = "shift"
                                call Laura_HotdogAfter
                                call Laura_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ counter += 1
                                jump Laura_Hotdog_Cycle
                        "Let's try something else." if multi_action:
                                $ line = 0
                                call Laura_Sex_Reset
                                $ action_context = "shift"
                                jump Laura_HotdogAfter
                        "No, get back down there.":
                                if ApprovalCheck(LauraX, 1200) or ApprovalCheck(LauraX, 500, "O"):
                                    $ LauraX.change_stat("love", 200, -5)
                                    $ LauraX.change_stat("obedience", 50, 3)
                                    $ LauraX.change_stat("obedience", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    $ LauraX.change_face("angry", 1)
                                    call Laura_Sex_Reset
                                    "She scowls at you and pulls away."
                                    ch_l "Not with that attitude."
                                    $ LauraX.change_stat("love", 50, -3, 1)
                                    $ LauraX.change_stat("love", 80, -4, 1)
                                    $ LauraX.change_stat("obedience", 30, -1, 1)
                                    $ LauraX.change_stat("obedience", 50, -1, 1)
                                    $ LauraX.recent_history.append("angry")
                                    $ LauraX.daily_history.append("angry")
                                    jump Laura_HotdogAfter
        #End Count check

        call Escalation(LauraX) #sees if she wants to escalate things

        if Round == 10:
            ch_l "It's getting kinda late. . ."
        elif Round == 5:
            ch_l "We should take a break for a minute."

    #Round = 0 loop breaks
    $ LauraX.change_face("bemused", 0)
    $ line = 0
    ch_l "Ok, that's enough of that for now."
