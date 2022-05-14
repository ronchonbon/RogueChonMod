# Jubes_SexMenu //////////////////////////////////////////////////////////////////////
label Jubes_SexAct(Act = 0): #rkeljsv
        if AloneCheck(JubesX) and JubesX.Taboo == 20:
                $ JubesX.Taboo = 0
                $ Taboo = 0
        call Shift_Focus(JubesX)
        if Act == "SkipTo":
            $ renpy.pop_call() #causes it to skip past the primary_action Swap
            $ renpy.pop_call() #causes it to skip past the cycle you were in before
            #$ renpy.pop_call() #causes it to skip past the sex menu you were in before that
            call SkipTo(JubesX)
        elif Act == "switch":
            $ renpy.pop_call() #causes it to skip past call here from Sex_Menu_Threesome
            #$ renpy.pop_call() #causes it to skip past call to Sex_Menu_Threesome
            # drops through to sex menu
        elif Act == "masturbate":
            call Jubes_M_Prep
            if not action_context:
                return
        elif Act == "lesbian":
            call Les_Prep(JubesX) #nee call Jubes_Les_Prep
            if not action_context:
                return
        elif Act == "kissing":
            call KissPrep(JubesX)
            if not action_context:
                return
        elif Act == "breasts":
            call Jubes_Fondle_Breasts
            if not action_context:
                return
        elif Act == "blow":
            call Jubes_BJ_Prep
            if not action_context:
                return
        elif Act == "hand":
            call Jubes_HJ_Prep
            if not action_context:
                return
        elif Act == "sex":
            call Jubes_SexPrep
            if not action_context:
                return

##  JubesX.Masturbating //////////////////////////////////////////////////////////////////////
# counter 1 means she's seen you, counter 0 means she hasn't.
label Jubes_Masturbate:  #rkeljs
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JubesX)
    if JubesX.Mast:
        $ temp_modifier += 10
    if JubesX.SEXP >= 50:
        $ temp_modifier += 25
    elif JubesX.SEXP >= 30:
        $ temp_modifier += 15
    elif JubesX.SEXP >= 15:
        $ temp_modifier += 5
    if JubesX.lust >= 90:
        $ temp_modifier += 20
    elif JubesX.lust >= 75:
        $ temp_modifier += 5
    if "exhibitionist" in JubesX.Traits:
        $ temp_modifier += (3*Taboo)
    if JubesX in Player.Harem or "sex friend" in JubesX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JubesX.Traits:
        $ temp_modifier -= 40
    if JubesX.ForcedCount and not JubesX.Forced:
        $ temp_modifier -= 5 * JubesX.ForcedCount

    $ Approval = ApprovalCheck(JubesX, 1300, TabM = 2) # 120, 135, 150, Taboo -80(200)

    $ JubesX.DrainWord("unseen",1,0) #She sees you, so remove unseens

    if action_context == "join":       # This triggers if you ask to join in
                if Approval > 1 or (Approval and JubesX.lust >= 50):
                    $ Player.AddWord(1,"join")
                    menu:
                        extend ""
                        "Would you like some help? I could lend some helping hands. . ."  if Player.Semen and JubesX.Action:
                                $ JubesX.change_stat("love", 90, 1)
                                $ JubesX.change_stat("obedience", 50, 2)
                                $ JubesX.change_face("sexy")
                                ch_v "Well, ok, gimme a hand with these?"
                                $ JubesX.change_stat("obedience", 70, 2)
                                $ JubesX.change_stat("inhibition", 70, 1)
                                $ offhand_action = "fondle breasts"
                                $ JubesX.Mast += 1
                                jump Jubes_M_Cycle
                        "Would you like some help? I could. . . up to you, I guess." if Player.Semen and JubesX.Action:
                                $ JubesX.change_stat("love", 70, 2)
                                $ JubesX.change_stat("love", 90, 1)
                                $ JubesX.change_face("sexy")
                                ch_v "Cool. . ."
                                $ JubesX.change_stat("obedience", 70, 2)
                                $ JubesX.change_stat("inhibition", 70, 1)
                                $ D20 = renpy.random.randint(1, 20)
                                if D20 > 10:
                                    $ offhand_action = "fondle breasts"
                                else:
                                    $ offhand_action = "suck breasts"
                                $ JubesX.Mast += 1
                                jump Jubes_M_Cycle
                        "Why don't we take care of each other?" if Player.Semen and JubesX.Action:
                                $ JubesX.change_face("sexy")
                                ch_v "Like what?"
                                $ renpy.pop_call()          #removes the call to this label
                                return                      #returns to sexmenu=
                        "You look like you have things well in hand. . .":
                                if JubesX.lust >= 50:
                                    $ JubesX.change_stat("love", 70, 2)
                                    $ JubesX.change_stat("love", 90, 1)
                                    $ JubesX.change_face("sexy")
                                    ch_v "Sure, just gimme a sec. . ."
                                    $ JubesX.change_stat("obedience", 80, 3)
                                    $ JubesX.change_stat("inhibition", 80, 5)
                                    jump Jubes_M_Cycle
                                elif ApprovalCheck(JubesX, 1200):
                                    $ JubesX.change_face("sly")
                                    ch_v "Yeah. . . but I could take a break. . ."
                                else:
                                    $ JubesX.change_face("angry")
                                    ch_v "Well I -did.-"

                #else: You've failed all checks so she kicks you out.
                $ JubesX.ArmPose = 1
                $ JubesX.OutfitChange()
                $ JubesX.Action -= 1
                $ Player.change_stat("Focus", 50, 30)
                call Checkout(1)
                $ line = 0
                $ action_context = 0
                $ renpy.pop_call()          #removes the call to this label
                if Approval:
                        $ JubesX.change_face("bemused", 2)
                        if bg_current == "bg_jubes":
                            ch_v "So, what're you doing here?"
                        else:
                            ch_v "I didn't think anyone would be dropping by. . ."
                        $ JubesX.Blush = 1
                else:
                        $ JubesX.change_stat("love", 200, -5)
                        $ JubesX.change_face("angry")
                        $ JubesX.recent_history.append("angry")
                        $ JubesX.daily_history.append("angry")
                        if bg_current == "bg_jubes":
                            ch_v "I was taking care of something, bye."
                            "[JubesX.name] kicks you out of her room."
                            $ renpy.pop_call()
                            jump Campus_Map
                        else:
                            ch_v "Ugh, I've got to get going anyway."
                            call Remove_Girl(JubesX)
                return                      #returns to sexmenu, which returns to original
    #End of "Join" option



    if action_context == JubesX:                                                                  #Jubes auto-starts
                if Approval > 2:                                                      # fix, add jubes auto stuff here
                        if JubesX.wearing_skirt:
                            "[JubesX.name]'s hand snakes down her body, and hikes up her skirt."
                            $ JubesX.Upskirt = 1
                        elif JubesX.PantsNum() >= 6:
                            "[JubesX.name] slides her hand down her body and into her [JubesX.Legs]."
                        elif JubesX.HoseNum() >= 5:
                            "[JubesX.name]'s hand slides down her body and under her [JubesX.Hose]."
                        elif JubesX.Panties:
                            "[JubesX.name]'s hand slides down her body and under her [JubesX.Panties]."
                        else:
                            "[JubesX.name]'s hand slides down her body and begins to caress her pussy."
                        $ JubesX.SeenPanties = 1
                        call Jubes_First_Bottomless(1)
                        "She starts to slowly rub herself."
                        menu:
                            "What do you do?"
                            "Nothing.":
                                    $ JubesX.change_stat("inhibition", 80, 3)
                                    $ JubesX.change_stat("inhibition", 60, 2)
                                    "[JubesX.name] begins to masturbate."
                            "Go for it.":
                                    $ JubesX.change_face("sexy, 1")
                                    $ JubesX.change_stat("inhibition", 80, 3)
                                    ch_p "That is so sexy, [JubesX.Pet]."
                                    $ JubesX.nameCheck() #checks reaction to petname
                                    "You lean back and enjoy the show."
                                    $ JubesX.change_stat("love", 80, 1)
                                    $ JubesX.change_stat("obedience", 90, 1)
                                    $ JubesX.change_stat("obedience", 50, 2)
                            "Ask her to stop.":
                                    $ JubesX.change_face("surprised")
                                    $ JubesX.change_stat("inhibition", 70, 1)
                                    ch_p "Let's not do that right now, [JubesX.Pet]."
                                    $ JubesX.nameCheck() #checks reaction to petname
                                    "[JubesX.name] pulls her hands away from herself."
                                    $ JubesX.OutfitChange()
                                    $ JubesX.change_stat("obedience", 90, 1)
                                    $ JubesX.change_stat("obedience", 50, 1)
                                    $ JubesX.change_stat("obedience", 30, 2)
                                    return
                        jump Jubes_M_Prep
                else:
                        $ temp_modifier = 0                               # fix, add jubes auto stuff here
                        $ offhand_action = 0
                return
    #End if Jubes intitiates this action

    #first time
    if not JubesX.Mast:
            $ JubesX.change_face("surprised", 1)
            $ JubesX.Mouth = "kiss"
            ch_v "So you like watching me masturbate?"
            if JubesX.Forced:
                $ JubesX.change_face("sad")
                ch_v "Nothing more than watching? . ."


    #First time dialog
    if not JubesX.Mast and Approval:
            if JubesX.Forced:
                $ JubesX.change_face("sad")
                $ JubesX.change_stat("love", 70, -3, 1)
                $ JubesX.change_stat("love", 20, -2, 1)
            elif JubesX.love >= JubesX.obedience and JubesX.love >= JubesX.inhibition:
                $ JubesX.change_face("sexy")
                $ JubesX.Brows = "sad"
                $ JubesX.Mouth = "smile"
                ch_v "I don't know, are you sure?"
            elif JubesX.obedience >= JubesX.inhibition:
                $ JubesX.change_face("normal")
                ch_v "If that's what you're into. . ."
            else: # Uninhibited
                $ JubesX.change_face("sad")
                $ JubesX.Mouth = "smile"
                ch_v "I could work off some stress. . ."


    #Second time+ initial dialog
    elif Approval:
            if JubesX.Forced:
                $ JubesX.change_face("sad")
                $ JubesX.change_stat("love", 70, -3, 1)
                $ JubesX.change_stat("love", 20, -2, 1)
                ch_v "Hmm, again?"
            elif Approval and "masturbation" in JubesX.recent_history:
                $ JubesX.change_face("sexy", 1)
                ch_v "I have built up some more stress. . ."
                jump Jubes_M_Prep
            elif Approval and "masturbation" in JubesX.daily_history:
                $ JubesX.change_face("sexy", 1)
                $ line = renpy.random.choice(["Did you enjoy that?",
                    "Didn't get enough earlier?",
                    "I enjoyed having an audience. . ."])
                ch_v "[line]"
            elif JubesX.Mast < 3:
                $ JubesX.change_face("sexy", 1)
                $ JubesX.Brows = "confused"
                ch_v "Was last time fun?"
            else:
                $ JubesX.change_face("sexy", 1)
                $ JubesX.ArmPose = 2
                $ line = renpy.random.choice(["You do enjoy watching.",
                    "Again?",
                    "You really enjoy watching me.",
                    "You want me to shlick again?"])
                ch_v "[line]"
                $ line = 0
    #End second time+ initial dialog

    #If she's into it. . .
    if Approval >= 2:
            if JubesX.Forced:
                $ JubesX.change_face("sad")
                $ JubesX.change_stat("obedience", 90, 1)
                $ JubesX.change_stat("inhibition", 60, 1)
                ch_v "Whatevs. . ."
            else:
                $ JubesX.change_face("sexy", 1)
                $ JubesX.change_stat("love", 90, 1)
                $ JubesX.change_stat("inhibition", 50, 3)
                $ line = renpy.random.choice(["Huh. Ok.",
                    "Couldn't hurt. . .",
                    "Allright.",
                    "Sure.",
                    "Heh, ok."])
                ch_v "[line]"
                $ line = 0
            $ JubesX.change_stat("obedience", 20, 1)
            $ JubesX.change_stat("obedience", 60, 1)
            $ JubesX.change_stat("inhibition", 70, 2)
            jump Jubes_M_Prep

    #If she's not into it, but maybe. . .
    else:
        menu:
            ch_v "I don't know, I'm not really into it right now."
            "Maybe later?":
                    $ JubesX.change_face("sexy", 1)
                    if JubesX.lust > 70:
                        ch_v "Maybe, just not with so many eyes on me. . ."
                    else:
                        ch_v "Hmm, maaaybe. . ."
                    $ JubesX.change_stat("love", 80, 2)
                    $ JubesX.change_stat("inhibition", 70, 2)
                    return
            "You look like you could use it. . .":
                    if Approval:
                        $ JubesX.change_face("sexy")
                        $ JubesX.change_stat("obedience", 90, 2)
                        $ JubesX.change_stat("obedience", 50, 2)
                        $ JubesX.change_stat("inhibition", 70, 3)
                        $ JubesX.change_stat("inhibition", 40, 2)
                        $ line = renpy.random.choice(["Huh. Ok.",
                                "Couldn't hurt. . .",
                                "Alright.",
                                "Sure.",
                                "Heh, ok."])
                        ch_v "[line]"
                        $ line = 0
                        jump Jubes_M_Prep

            "Just get at it already.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(JubesX, 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                    if Approval > 1 or (Approval and JubesX.Forced):
                        $ JubesX.change_face("sad")
                        $ JubesX.change_stat("love", 70, -5, 1)
                        $ JubesX.change_stat("love", 200, -5)
                        ch_v "Whatever."
                        $ JubesX.change_stat("obedience", 80, 4)
                        $ JubesX.change_stat("inhibition", 80, 1)
                        $ JubesX.change_stat("inhibition", 60, 3)
                        $ JubesX.Forced = 1
                        jump Jubes_M_Prep
                    else:
                        $ JubesX.change_stat("love", 200, -20)
                        $ JubesX.recent_history.append("angry")
                        $ JubesX.daily_history.append("angry")
    # end of asking her to do it

    #She refused all offers.
    $ JubesX.ArmPose = 1
    if JubesX.Forced:
            $ JubesX.change_face("angry", 1)
            ch_v "This isn't something I'm into."
            $ JubesX.change_stat("lust", 90, 5)
            if JubesX.love > 300:
                $ JubesX.change_stat("love", 70, -2)
            $ JubesX.change_stat("obedience", 50, -2)
            $ JubesX.recent_history.append("angry")
            $ JubesX.daily_history.append("angry")
            $ JubesX.recent_history.append("no masturbation")
            $ JubesX.daily_history.append("no masturbation")
            return
    elif Taboo:                             # she refuses and this is too public a place for her
            $ JubesX.change_face("angry", 1)
            $ JubesX.daily_history.append("tabno")
            ch_v "I don't want to do this in public!"
            $ JubesX.change_stat("lust", 90, 5)
            $ JubesX.change_stat("obedience", 50, -3)
            return
    elif JubesX.Mast:
            $ JubesX.change_face("sad")
            ch_v "I'm not into it right now."
    else:
            $ JubesX.change_face("normal", 1)
            ch_v "Um. . . no."
    $ JubesX.recent_history.append("no masturbation")
    $ JubesX.daily_history.append("no masturbation")
    $ temp_modifier = 0
    return

label Jubes_M_Prep:  #rkelj
    $ JubesX.Upskirt = 1
    $ JubesX.PantiesDown = 1
    call Jubes_First_Bottomless(1)
    call set_the_scene(Dress=0)

    #if she hasn't seen you yet. . .
    if "unseen" in JubesX.recent_history:
            $ JubesX.change_face("sexy")
            $ JubesX.Eyes = "closed"
            $ JubesX.ArmPose = 2
            "You see [JubesX.name] leaning back, masturbating. You don't think she's noticed you yet."
    else:
            $ JubesX.change_face("sexy")
            $ JubesX.ArmPose = 2
            "[JubesX.name] lays back and starts to toy with herself."
            if not JubesX.Mast:#First time
                    if JubesX.Forced:
                        $ JubesX.change_stat("love", 90, -20)
                        $ JubesX.change_stat("obedience", 70, 45)
                        $ JubesX.change_stat("inhibition", 80, 35)
                    else:
                        $ JubesX.change_stat("love", 90, 15)
                        $ JubesX.change_stat("obedience", 70, 35)
                        $ JubesX.change_stat("inhibition", 80, 40)


    $ primary_action = "masturbation"
    if not girl_offhand_action:
        $ girl_offhand_action = "fondle pussy"

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ line = 0
    if Taboo:
        $ JubesX.DrainWord("tabno")
    $ JubesX.DrainWord("no masturbation")
    $ JubesX.recent_history.append("masturbation")
    $ JubesX.daily_history.append("masturbation")

label Jubes_M_Cycle:
    if action_context == "join":
        $ renpy.pop_call()
        $ action_context = 0

    while Round > 0:
        call Jubes_Pos_Reset("masturbation")
        call Shift_Focus(JubesX)
        $ JubesX.lustFace()

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep Watching.":
                                pass

                        "[JubesX.name]. . .[[jump in]" if "unseen" not in JubesX.recent_history and "join" not in Player.recent_history and JubesX.Loc == bg_current:
                                "[JubesX.name] slows what she's doing with a sly grin."
                                ch_v "Oh, are you having fun?"
                                $ action_context = "join"
                                call Jubes_Masturbate
                        "\"Ahem. . .\"" if "unseen" in JubesX.recent_history and JubesX.Loc == bg_current:
                                jump Jubes_M_Interupted

                        "Start jack'in it." if offhand_action != "jackin":
                                call Jackin(JubesX)
                        "Stop jack'in it." if offhand_action == "jackin":
                                $ offhand_action = 0

                        "Slap her ass" if JubesX.Loc == bg_current:
                                if "unseen" in JubesX.recent_history:
                                        "You smack [JubesX.name] firmly on the ass!"
                                        jump Jubes_M_Interupted
                                else:
                                        call Slap_Ass(JubesX)
                                        $ counter += 1
                                        $ Round -= 1
                                        jump Jubes_M_Cycle
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
                                    "Offhand action" if JubesX.Loc == bg_current:
                                            if JubesX.Action and MultiAction:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ JubesX.Action -= 1
                                            else:
                                                ch_v "Maybe we could finish this up for now?"

                                    "Threesome actions (locked)" if not Partner or "unseen" in JubesX.recent_history or JubesX.Loc != bg_current:
                                        pass
                                    "Threesome actions" if Partner and "unseen" not in JubesX.recent_history and JubesX.Loc == bg_current:
                                        menu:
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(JubesX)
                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(JubesX)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jubes_M_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jubes_M_Cycle
                                            "Never mind":
                                                        jump Jubes_M_Cycle

                                    "Show her feet" if not ShowFeet and JubesX.Pose == "doggy":
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and JubesX.Pose == "doggy":
                                            $ ShowFeet = 0

                                    "Undress [JubesX.name]":
                                            if "unseen" in JubesX.recent_history:
                                                    ch_p "Oh, yeah, take it off. . ."
                                                    jump Jubes_M_Interupted
                                            else:
                                                    call Girl_Undress(JubesX)
                                    "Clean up [JubesX.name] (locked)" if not JubesX.Spunk:
                                            pass
                                    "Clean up [JubesX.name]" if JubesX.Spunk:
                                            if "unseen" in JubesX.recent_history:
                                                    ch_p "You've got a little something on you. . ."
                                                    jump Jubes_M_Interupted
                                            else:
                                                    call Girl_Cleanup(JubesX,"ask")
                                    "Never mind":
                                                    jump Jubes_M_Cycle

                        "Back to Sex Menu" if MultiAction and JubesX.Loc == bg_current:
                                    ch_p "Let's try something else."
                                    call Jubes_Pos_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Jubes_M_Interupted
                        "End Scene" if not MultiAction or JubesX.Loc != bg_current:
                                    ch_p "Let's stop for now."
                                    call Jubes_Pos_Reset
                                    $ line = 0
                                    jump Jubes_M_Interupted
        #End menu (if line)

        call Shift_Focus(JubesX)
        call Sex_Dialog(JubesX,Partner)

        #If either of you could cum

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up

        if Player.Focus >= 100 or JubesX.lust >= 100:
                    #If you can cum:
                    if Player.Focus >= 100:
                        if "unseen" not in JubesX.recent_history:
                            #if she knows you're there
                            call Player_Cumming(JubesX)
                            if "angry" in JubesX.recent_history:
                                call Jubes_Pos_Reset
                                return
                            $ JubesX.change_stat("lust", 200, 5)
                            if 100 > JubesX.lust >= 70 and JubesX.OCount < 2:
                                $ JubesX.recent_history.append("unsatisfied")
                                $ JubesX.daily_history.append("unsatisfied")
                            $ line = "came"
                        else: #If she wasn't aware you were there
                            "You grunt and try to hold it in."
                            $ Player.Focus = 95
                            if JubesX.Loc == bg_current:
                                    jump Jubes_M_Interupted

                    #If Jubes can cum
                    if JubesX.lust >= 100:
                        call Girl_Cumming(JubesX)
                        if JubesX.Loc == bg_current:
                                jump Jubes_M_Interupted

                    if line == "came":
                        $ line = 0
                        if not Player.Semen:
                            "You're emptied out, you should probably take a break."
                            $ offhand_action = 0 if offhand_action == "jackin" else offhand_action


                        if "unsatisfied" in JubesX.recent_history:#And Jubes is unsatisfied,
                            "[JubesX.name] still seems a bit unsatisfied with the experience."
                            menu:
                                "Let her keep going?"
                                "Yes, keep going for a bit.":
                                    $ line = "You let her get back into it"
                                    jump Jubes_M_Cycle
                                "No, I'm done.":
                                    "You ask her to stop."
                                    return
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        if "unseen" in JubesX.recent_history:
                if Round == 10:
                    "It's getting a bit late, [JubesX.name] will probably be wrapping up soon."
                elif Round == 5:
                    "She's definitely going to stop soon."
        else:
                if JubesX.Loc == bg_current:
                        call Escalation(JubesX) #sees if she wants to escalate things

                if Round == 10:
                        call Sex_Basic_Dialog(JubesX,10) #"I could use a break soon. . ."
                        $ JubesX.lust += 10
                elif Round == 5:
                        call Sex_Basic_Dialog(JubesX,5)   #". . . I could really use a break here. . ."
                        $ JubesX.lust += 25

    #Round = 0 loop breaks
    $ JubesX.change_face("bemused", 0)
    $ line = 0
    call Sex_Basic_Dialog(JubesX,"done") # ch_s "Ok, that's it, I need a break."

label Jubes_M_Interupted:

    # If she hasn't noticed you're there before cumming
    if "unseen" in JubesX.recent_history:
                $ JubesX.change_face("surprised", 2)
                "[JubesX.name] stops what she's doing with a start, eyes wide."
                call Jubes_First_Bottomless(1)
                $ JubesX.change_face("surprised", 2)

                #If you've been jacking it
                if offhand_action == "jackin":
                        ch_v "Oh!"
                        ch_v "How long were you standing there?"
                        $ JubesX.Eyes = "down"
                        menu:
                            ch_v "And um. . . you have your penis out. . . "
                            "A while, it was an excellent show.":
                                    $ JubesX.change_face("sexy",1)
                                    $ JubesX.change_stat("obedience", 50, 3)
                                    $ JubesX.change_stat("obedience", 70, 2)
                                    ch_v "Oh. . . um. . .thanks?"
                                    if JubesX.love >= 800 or JubesX.obedience >= 500 or JubesX.inhibition >= 500:
                                        $ temp_modifier += 10
                                        $ JubesX.change_stat("lust", 90, 5)
                                        ch_v "I, um. . . you're not so bad yourself. . ."

                            "I. . . just got here?":
                                    $ JubesX.change_face("angry",1)
                                    $ JubesX.change_stat("love", 70, 2)
                                    $ JubesX.change_stat("love", 90, 1)
                                    $ JubesX.change_stat("obedience", 50, 2)
                                    $ JubesX.change_stat("obedience", 70, 2)
                                    "She looks pointedly at your cock,"
                                    ch_v "Not by the looks of that thing."
                                    if JubesX.love >= 800 or JubesX.obedience >= 500 or JubesX.inhibition >= 500:
                                            $ temp_modifier += 10
                                            $ JubesX.change_stat("lust", 90, 5)
                                            $ JubesX.change_face("bemused", 1)
                                            ch_v "I guess I made an impression?"
                                    else:
                                            $ temp_modifier -= 10
                                            $ JubesX.change_stat("lust", 200, -5)
                        call Seen_First_Peen(JubesX,Partner)
                        ch_v "Hmm. . ."

                #you haven't been jacking it
                else:
                        ch_v "Oh!"
                        ch_v "How long were you standing there?"
                        menu:
                            extend ""
                            "A while.":
                                    $ JubesX.change_face("sexy", 1)
                                    $ JubesX.change_stat("obedience", 50, 3)
                                    $ JubesX.change_stat("obedience", 70, 2)
                                    ch_v "I guess it must have been interesting. . ."
                            "I just got here.":
                                    $ JubesX.change_face("bemused", 1)
                                    $ JubesX.change_stat("love", 70, 2)
                                    $ JubesX.change_stat("love", 90, 1)
                                    ch_v "Suuuure. . ."
                                    $ JubesX.change_stat("obedience", 50, 2)
                                    $ JubesX.change_stat("obedience", 70, 2)

                $ JubesX.DrainWord("unseen",1,0) #She sees you, so remove unseens
                $ JubesX.Mast += 1
                if Round <= 10:
                    ch_v "Well, I kinda needed a break anyway. . ."
                    return
                $ action_context = "join"
                call Jubes_Masturbate
                "error: report this if you see it."
                return #should be redundant
    #End Unseen

    #else, if She's seen you already
    $ JubesX.Action -= 1
    $ JubesX.Mast += 1
    call Checkout
    if action_context == "shift":
        $ action_context = 0
        return
    $ action_context = 0

    if Partner == EmmaX:
        call Partner_Like(JubesX,3)
    else:
        call Partner_Like(JubesX,2)

    if JubesX.Loc != bg_current:
        return

    if Round <= 10:
            ch_v "I need a break anyway. . ."
            return
    $ JubesX.change_face("sexy", 1)
    if JubesX.lust < 20:
        ch_v "Well. . . I certainly enjoyed that. . ."
    else:
        ch_v "So, what'd you wanna do next?"
    menu:
        extend ""
        "Well, I have something you could take care of. . ." if Player.Semen and JubesX.Action:
                $ action_context = "shift"
                return
        "You could just keep going. . ." if Player.Semen:
                $ JubesX.change_face("sly")
                if JubesX.Action and Round >= 10:
                    ch_v "Ok. . ."
                    jump Jubes_M_Cycle
                else:
                    ch_v "I need a minute here. . ."
        "I'm good here. [[Stop]":
                if JubesX.love < 800 and JubesX.inhibition < 500 and JubesX.obedience < 500:
                    $ JubesX.OutfitChange()
                $ JubesX.change_face("normal")
                $ JubesX.Brows = "confused"
                ch_v "Ok, cool. . ."
                $ JubesX.Brows = "normal"
        "You should probably stop for now." if JubesX.lust > 30:
                $ JubesX.change_face("angry")
                ch_v "Hrmm."
    return

## end JubesX.Masturbating ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



# Start Jubes Sex pose //////////////////////////////////////////////////////////////////////////////////
# JubesX.Sex_P //////////////////////////////////////////////////////////////////////

label Jubes_Sex_P:   #rkeljs
    #fix remove
    "This option is currently unavailable. It will be added in a later update."
    return
    #fix remove

    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JubesX)
    if JubesX.Sex >= 7: # She loves it
        $ temp_modifier += 15
    elif JubesX.Sex >= 3: #You've done it before several times
        $ temp_modifier += 12
    elif JubesX.Sex: #You've done it before
        $ temp_modifier += 10

    if JubesX.Addict >= 75 and (JubesX.CreamP + JubesX.CreamA) >=3: #She's really strung out and has creampied
        $ temp_modifier += 20
    elif JubesX.Addict >= 75:
        $ temp_modifier += 15

    if JubesX.lust > 85:
        $ temp_modifier += 10
    elif JubesX.lust > 75: #She's really horny
        $ temp_modifier += 5

    if action_context == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in JubesX.Traits:
        $ temp_modifier += (4*Taboo)
    if JubesX in Player.Harem or "sex friend" in JubesX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JubesX.Traits:
        $ temp_modifier -= 40
    if JubesX.ForcedCount and not JubesX.Forced:
        $ temp_modifier -= 5 * JubesX.ForcedCount



    if Taboo and "tabno" in JubesX.daily_history:
        $ temp_modifier -= 10

    if "no sex" in JubesX.daily_history:
        $ temp_modifier -= 15 if "no sex" in JubesX.recent_history else 5


    $ Approval = ApprovalCheck(JubesX, 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)

    if action_context == "auto":
                call Jubes_Sex_Launch("sex")
                if JubesX.wearing_skirt:
                    "You push [JubesX.name] onto her back, sliding her skirt up as you go."
                    $ JubesX.Upskirt = 1
                elif JubesX.PantsNum() >= 6:
                    "You push [JubesX.name] onto her back, sliding her pants down as you do."
                    $ JubesX.Upskirt = 1
                else:
                    "You push [JubesX.name] onto her back."
                $ JubesX.SeenPanties = 1
                "You rub the tip of your cock against her moist slit."
                $ JubesX.change_face("surprised", 1)

                if (JubesX.Sex and Approval) or (Approval > 1):
                    #this is not the first time you've had sex, or she's into it
                    "[JubesX.name] glances down and then breaks into a smile."
                    $ JubesX.change_face("sly")
                    $ JubesX.change_stat("obedience", 70, 3)
                    $ JubesX.change_stat("inhibition", 50, 3)
                    $ JubesX.change_stat("inhibition", 70, 1)
                    ch_v "Fine by me, [JubesX.Petname]."
                    jump Jubes_SexPrep
                else:
                    #she's questioning it
                    $ JubesX.Brows = "angry"
                    menu:
                        ch_v "Oh, taking it all the way, are we?"
                        "Sorry, sorry! Never mind.":
                            if Approval:
                                    $ JubesX.change_face("sexy", 1)
                                    $ JubesX.change_stat("obedience", 70, 3)
                                    $ JubesX.change_stat("inhibition", 50, 3)
                                    $ JubesX.change_stat("inhibition", 70, 1)
                                    ch_v "No no, not a problem. . ."
                                    jump Jubes_SexPrep
                            else:
                                    "You pull back before you really get it in."
                                    $ JubesX.change_face("bemused", 1)
                                    if JubesX.Sex:
                                        ch_v "Maybe ask first, [JubesX.Petname]?"
                                    else:
                                        ch_v "Maybe if you'd asked first. . ."
                        "Just fucking.":
                            $ JubesX.change_stat("love", 80, -10, 1)
                            $ JubesX.change_stat("love", 200, -10)
                            "You press inside some more."
                            $ JubesX.change_stat("obedience", 70, 3)
                            $ JubesX.change_stat("inhibition", 50, 3)
                            if not ApprovalCheck(JubesX, 700, "O", TabM=1):   #Checks if obedience is 700+
                                $ JubesX.change_face("angry")
                                "[JubesX.name] shoves you away and backhands you in the face."
                                ch_v "Dick."
                                ch_v "Don't push me."
                                $ JubesX.change_stat("love", 50, -10, 1)
                                $ JubesX.change_stat("obedience", 50, 3)
                                $ renpy.pop_call()
                                if action_context:
                                    $ renpy.pop_call()
                                call Jubes_Sex_Reset
                                $ JubesX.recent_history.append("angry")
                                $ JubesX.daily_history.append("angry")
                            else:
                                $ JubesX.change_face("sad")
                                "[JubesX.name] doesn't seem to be into this, you're lucky she's so obedient."
                                jump Jubes_SexPrep
                return
    #End Auto


    if not JubesX.Sex and "no sex" not in JubesX.recent_history:
            #first time
            $ JubesX.change_face("surprised", 1)
            $ JubesX.Mouth = "kiss"
            ch_v "Huh, you wanna fuck me? . . "
            if JubesX.Forced:
                $ JubesX.change_face("sad")
                ch_v "Pretty bold of you. . ."


    if not JubesX.Sex and Approval:
            #First time dialog
            if JubesX.Forced:
                $ JubesX.change_face("sad")
                $ JubesX.change_stat("love", 70, -30, 1)
                $ JubesX.change_stat("love", 20, -20, 1)
            elif JubesX.love >= (JubesX.obedience + JubesX.inhibition):
                $ JubesX.change_face("sexy")
                $ JubesX.Brows = "sad"
                $ JubesX.Mouth = "smile"
                ch_v "Well, you look so cute when you ask. . ."
            elif JubesX.obedience >= JubesX.inhibition:
                $ JubesX.change_face("normal")
                ch_v "Yes, [JubesX.Petname]. . ."
            elif JubesX.Addict >= 50:
                $ JubesX.change_face("manic", 1)
                ch_v "Sounds fun. . ."
            else: # Uninhibited
                $ JubesX.change_face("sad")
                $ JubesX.Mouth = "smile"
                ch_v "I was hoping you'd ask. . ."
            #End first time dialog

    elif Approval:
            #Second time+ dialog
            $ JubesX.change_face("sexy", 1)
            if JubesX.Forced:
                $ JubesX.change_face("sad")
                $ JubesX.change_stat("love", 70, -3, 1)
                $ JubesX.change_stat("love", 20, -2, 1)
                ch_v "I hope I don't wear you out."
            elif not Taboo and "tabno" in JubesX.daily_history:
                ch_v "Yeah, this is more covert."
            elif "sex" in JubesX.recent_history:
                ch_v "Again? Your funeral."
                jump Jubes_SexPrep
            elif "sex" in JubesX.daily_history:
                $ line = renpy.random.choice(["Back again?",
                    "You'd like another round?",
                    "I must be better than I thought.",
                    "Didn't get enough earlier?",
                    "Your funeral, " + JubesX.Petname + "."])
                ch_v "[line]"
            elif JubesX.Sex < 3:
                $ JubesX.Brows = "confused"
                $ JubesX.Mouth = "kiss"
                ch_v "Oh? Another round?"
            else:
                $ line = renpy.random.choice(["Oh, you want some of this?",
                    "You'd like another round?",
                    "I must be better than I thought.",
                    "I hope you don't plan on wearing me out.",
                    "You want to plow me?"])
                ch_v "[line]"
            $ line = 0
            #end Second time+ dialog

    if Approval >= 2:
            #She's into it. . .
            if JubesX.Forced:
                $ JubesX.change_face("sad")
                $ JubesX.change_stat("obedience", 90, 1)
                $ JubesX.change_stat("inhibition", 60, 1)
                ch_v "Ok, fine. Just make it good."
            elif "no sex" in JubesX.daily_history:
                ch_v "Ok, whatever. . ."
            else:
                $ JubesX.change_face("sexy", 1)
                $ JubesX.change_stat("love", 90, 1)
                $ JubesX.change_stat("inhibition", 50, 3)
                $ line = renpy.random.choice(["Well. . . fine, let's do it.",
                    "Sure.",
                    "We could, I guess.",
                    "Hmmm, sure.",
                    "Sounds fun."])
                ch_v "[line]"
                $ line = 0
            $ JubesX.change_stat("obedience", 20, 1)
            $ JubesX.change_stat("obedience", 60, 1)
            $ JubesX.change_stat("inhibition", 70, 2)
            jump Jubes_SexPrep

    else:
            #She's not into it, but maybe. . .
            $ JubesX.change_face("angry")
            if "no sex" in JubesX.recent_history:
                ch_v "Sorry, [JubesX.Petname] \"no.\""
            elif Taboo and "tabno" in JubesX.daily_history and "no sex" in JubesX.daily_history:
                ch_v "I told you. . . this place is too exposed."
            elif "no sex" in JubesX.daily_history:
                ch_v "I just told you \"no.\""
            elif Taboo and "tabno" in JubesX.daily_history:
                ch_v "I already told you this is too public!"
            elif not JubesX.Sex:
                $ JubesX.change_face("bemused")
                ch_v "Oh, you have no idea what you're in for. . ."
            else:
                $ JubesX.change_face("bemused")
                ch_v "Maybe later? . ."
            menu:
                extend ""
                "Sorry, never mind." if "no sex" in JubesX.daily_history:
                        $ JubesX.change_face("bemused")
                        ch_v "Well, you are persistant."
                        return
                "Maybe later?" if "no sex" not in JubesX.daily_history:
                        $ JubesX.change_face("sexy")
                        ch_v "Probably. . ."
                        $ JubesX.change_stat("love", 80, 2)
                        $ JubesX.change_stat("inhibition", 70, 2)
                        if Taboo:
                            $ JubesX.recent_history.append("tabno")
                            $ JubesX.daily_history.append("tabno")
                        $ JubesX.recent_history.append("no sex")
                        $ JubesX.daily_history.append("no sex")
                        return
                "I think you'd enjoy it as much as I would. . .":
                        if Approval:
                            $ JubesX.change_face("sexy")
                            $ JubesX.change_stat("obedience", 90, 2)
                            $ JubesX.change_stat("obedience", 50, 2)
                            $ JubesX.change_stat("inhibition", 70, 3)
                            $ JubesX.change_stat("inhibition", 40, 2)
                            $ line = renpy.random.choice(["Yeah, probably. . .",
                                "I guess. . .",
                                "Good point. . ."])
                            ch_v "[line]"
                            $ line = 0
                            jump Jubes_SexPrep
                "Just deal with it.":                                               # Pressured into it
                        $ Approval = ApprovalCheck(JubesX, 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
                        if Approval > 1 or (Approval and JubesX.Forced):
                            $ JubesX.change_face("sad")
                            $ JubesX.change_stat("love", 70, -5, 1)
                            $ JubesX.change_stat("love", 200, -5)
                            ch_v "Fine, if it'll shut you up."
                            $ JubesX.change_stat("obedience", 80, 4)
                            $ JubesX.change_stat("inhibition", 80, 1)
                            $ JubesX.change_stat("inhibition", 60, 3)
                            $ JubesX.Forced = 1
                            jump Jubes_SexPrep
                        else:
                            $ JubesX.change_stat("love", 200, -20)
                            $ JubesX.recent_history.append("angry")
                            $ JubesX.daily_history.append("angry")
                #end menu
    #end Approval check

    #She refused all offers.
    $ JubesX.ArmPose = 1
    if "no sex" in JubesX.daily_history:
        ch_v "Don't push me."
        $ JubesX.recent_history.append("angry")
        $ JubesX.daily_history.append("angry")
    elif JubesX.Forced:
        $ JubesX.change_face("angry", 1)
        ch_v "I'm over taking orders."
        $ JubesX.change_stat("lust", 200, 5)
        if JubesX.love > 300:
                $ JubesX.change_stat("love", 70, -2)
        $ JubesX.change_stat("obedience", 50, -2)
        $ JubesX.recent_history.append("angry")
        $ JubesX.daily_history.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ JubesX.change_face("angry", 1)
        $ JubesX.recent_history.append("tabno")
        $ JubesX.daily_history.append("tabno")
        ch_v "This place is way too exposed."
        $ JubesX.change_stat("lust", 200, 5)
        $ JubesX.change_stat("obedience", 50, -3)
    elif JubesX.Sex:
        $ JubesX.change_face("sad")
        ch_v "Just jack it or something."
    else:
        $ JubesX.change_face("normal", 1)
        ch_v "Yeah, no."
    $ JubesX.recent_history.append("no sex")
    $ JubesX.daily_history.append("no sex")
    $ temp_modifier = 0
    return

label Jubes_Sex_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(JubesX)
        call Jubes_Sex_Launch("sex")
        if action_speed >= 4:
            $ action_speed = 2
#            call action_speed_Shift(2)
        $ JubesX.lustFace()
        $ Player.Cock = "in"
        $ primary_action = "sex"
        $ JubesX.Upskirt = 1
        $ JubesX.PantiesDown = 1

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
                                    call Slap_Ass(JubesX)
                                    $ counter += 1
                                    $ Round -= 1
                                    jump Jubes_Sex_Cycle

                        "Turn her Around":
                                    $ JubesX.Pose = "doggy" if JubesX.Pose != "doggy" else 0
                                    "You turn her around. . ."
                                    jump Jubes_Sex_Cycle

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
                                            if JubesX.Action and MultiAction:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ JubesX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")

                                    "Shift primary action":
                                            if JubesX.Action and MultiAction:
                                                    menu:
                                                        "How about anal?":
                                                                $ action_context = "shift"
                                                                call Jubes_SexAfter
                                                                call Jubes_Sex_A
                                                        "Just stick it in her ass [[without asking].":
                                                                $ action_context = "auto"
                                                                call Jubes_SexAfter
                                                                call Jubes_Sex_A
                                                        "Pull back to hotdog her.":
                                                                $ action_context = "pullback"
                                                                call Jubes_SexAfter
                                                                call Jubes_Sex_H
                                                        "Never Mind":
                                                                jump Jubes_Sex_Cycle
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [JubesX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(JubesX)
                                            "Ask [JubesX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(JubesX)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(JubesX)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jubes_Sex_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jubes_Sex_Cycle
                                            "Never mind":
                                                        jump Jubes_Sex_Cycle
                                    "Just take a look at her.":
                                            $ Player.Cock = 0
                                            $ action_speed = 0
                                    "Undress [JubesX.name]":
                                            call Girl_Undress(JubesX)
                                    "Clean up [JubesX.name] (locked)" if not JubesX.Spunk:
                                            pass
                                    "Clean up [JubesX.name]" if JubesX.Spunk:
                                            call Girl_Cleanup(JubesX,"ask")
                                    "Never mind":
                                            jump Jubes_Sex_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Jubes_Sex_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Jubes_SexAfter
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Jubes_Sex_Reset
                                    $ line = 0
                                    jump Jubes_SexAfter
        #End menu (if line)

        call Shift_Focus(JubesX)
        call Sex_Dialog(JubesX,Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JubesX.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JubesX)
                            if "angry" in JubesX.recent_history:
                                call Jubes_Sex_Reset
                                return
                            $ JubesX.change_stat("lust", 200, 5)
                            if 100 > JubesX.lust >= 70 and JubesX.OCount < 2:
                                    $ JubesX.recent_history.append("unsatisfied")
                                    $ JubesX.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jubes_SexAfter
                            $ line = "came"

                    if JubesX.lust >= 100:
                            #If you're still going at it and Jubes can cum
                            call Girl_Cumming(JubesX)
                            if action_context == "shift" or "angry" in JubesX.recent_history:
                                jump Jubes_SexAfter

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Jubes_SexAfter
                            elif "unsatisfied" in JubesX.recent_history:
                                #And Jubes is unsatisfied,
                                $ line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ line = "You get back into it"
                                        jump Jubes_Sex_Cycle
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Jubes_SexAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Jubes_SexAfter
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if JubesX.SEXP >= 100 or ApprovalCheck(JubesX, 1200, "LO"):
            pass
        elif counter == (5 + JubesX.Sex):
                    $ JubesX.Brows = "confused"
                    ch_v "So are we getting close?"
        elif counter == (10 + JubesX.Sex):
                    $ JubesX.Brows = "angry"
                    menu:
                        ch_v "Hey. . . could we. . . try something. . . else?"
                        "How about a BJ?" if JubesX.Action and MultiAction:
                                $ action_context = "shift"
                                call Jubes_SexAfter
                                call Jubes_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ counter += 1
                                jump Jubes_Sex_Cycle
                        "Let's try something else." if MultiAction:
                                $ line = 0
                                call Jubes_Sex_Reset
                                $ action_context = "shift"
                                jump Jubes_SexAfter
                        "No, get back down there.":
                                if ApprovalCheck(JubesX, 1200) or ApprovalCheck(JubesX, 500, "O"):
                                    $ JubesX.change_stat("love", 200, -5)
                                    $ JubesX.change_stat("obedience", 50, 3)
                                    $ JubesX.change_stat("obedience", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    $ JubesX.change_face("angry", 1)
                                    call Jubes_Sex_Reset
                                    "She scowls at you and pulls out."
                                    ch_v "Not with that attitude."
                                    $ JubesX.change_stat("love", 50, -3, 1)
                                    $ JubesX.change_stat("love", 80, -4, 1)
                                    $ JubesX.change_stat("obedience", 30, -1, 1)
                                    $ JubesX.change_stat("obedience", 50, -1, 1)
                                    $ JubesX.recent_history.append("angry")
                                    $ JubesX.daily_history.append("angry")
                                    jump Jubes_SexAfter
        #End Count check

        call Escalation(JubesX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(JubesX,10) #"I could use a break soon. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(JubesX,5)   #". . . I could really use a break here. . ."

    #Round = 0 loop breaks
    $ JubesX.change_face("bemused", 0)
    $ line = 0
    call Sex_Basic_Dialog(JubesX,"done") # ch_s "Ok, that's it, I need a break."

# Jubes anal //////////////////////////////////////////////////////////////////////

label Jubes_Sex_A: #rkelj
    #fix remove
    "This option is currently unavailable. It will be added in a later update."
    return
    #fix remove

    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JubesX)
    if JubesX.Anal >= 7: # She loves it
        $ temp_modifier += 20
    elif JubesX.Anal >= 3: #You've done it before several times
        $ temp_modifier += 17
    elif JubesX.Anal: #You've done it before
        $ temp_modifier += 15

    if JubesX.Addict >= 75 and (JubesX.CreamP + JubesX.CreamA) >=3: #She's really strung out and has creampied
        $ temp_modifier += 25
    elif JubesX.Addict >= 75:
        $ temp_modifier += 15

    if JubesX.lust > 85:
        $ temp_modifier += 10
    elif JubesX.lust > 75: #She's really horny
        $ temp_modifier += 5

    $ temp_modifier += 10  # she starts out loose

    if action_context == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in JubesX.Traits:
        $ temp_modifier += (5*Taboo)

    if JubesX in Player.Harem or "sex friend" in JubesX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JubesX.Traits:
        $ temp_modifier -= 40
    if JubesX.ForcedCount and not JubesX.Forced:
        $ temp_modifier -= 5 * JubesX.ForcedCount

    if Taboo and "tabno" in JubesX.daily_history:
        $ temp_modifier -= 10
    if "no anal" in JubesX.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no anal" in JubesX.recent_history else 0

    $ Approval = ApprovalCheck(JubesX, 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)

    if action_context == "auto":
            call Jubes_Sex_Launch("anal")
            if JubesX.wearing_skirt:
                "You push [JubesX.name] onto her back, sliding her skirt up as you go."
                $ JubesX.Upskirt = 1
            elif JubesX.PantsNum() >= 6:
                "You push [JubesX.name] onto her back, sliding her pants down as you do."
                $ JubesX.Legs = 0
            else:
                "You push [JubesX.name] onto her back."
            $ JubesX.SeenPanties = 1
            "You press the tip of your cock against her tight rim."
            $ JubesX.change_face("surprised", 1)
            call Jubes_First_Bottomless(1)

            if (JubesX.Anal and Approval) or (Approval > 1):
                #this is not the first time you've had sex, or she's into it
                $ JubesX.change_stat("obedience", 70, 3)
                $ JubesX.change_stat("inhibition", 50, 3)
                $ JubesX.change_stat("inhibition", 70, 1)
                "[JubesX.name] glances down and then breaks into a smile."
                ch_v "Yeah, ok. . ."
                jump Jubes_AnalPrep
            else:
                #she's questioning it
                $ JubesX.Brows = "angry"
                menu:
                    ch_v "Oh? A backdoor intruder?"
                    "Sorry, sorry! Never mind.":
                        if Approval:
                            $ JubesX.change_face("sexy", 1)
                            $ JubesX.change_stat("obedience", 70, 3)
                            $ JubesX.change_stat("inhibition", 50, 3)
                            $ JubesX.change_stat("inhibition", 70, 1)
                            ch_v "Hey, whatever floats your boat. . ."
                            ch_v "Get in there."
                            jump Jubes_AnalPrep
                        "You pull back before you really get it in."
                        $ JubesX.change_face("bemused", 1)

                        if JubesX.Anal:
                            ch_v "You coulda warned me. . ."
                        else:
                            ch_v "Hey, all I expect is a little warning. . ."
                    "Just fucking.":
                        $ JubesX.change_stat("love", 80, -10, 1)
                        $ JubesX.change_stat("love", 200, -8)
                        "You press into her."
                        $ JubesX.change_stat("obedience", 70, 3)
                        $ JubesX.change_stat("inhibition", 50, 3)
                        if not ApprovalCheck(JubesX, 700, "O", TabM=1):
                            $ JubesX.change_face("angry")
                            "[JubesX.name] shoves you away and backhands you in the face."
                            ch_v "Yeah, not like that you won't."
                            $ JubesX.change_stat("love", 50, -10, 1)
                            $ JubesX.change_stat("obedience", 50, 3)
                            $ renpy.pop_call()
                            if action_context:
                                $ renpy.pop_call()
                            call Jubes_Sex_Reset
                            $ JubesX.recent_history.append("angry")
                            $ JubesX.daily_history.append("angry")
                        else:
                            $ JubesX.change_face("sad")
                            "[JubesX.name] doesn't seem to be into this, you're lucky she's so obedient."
                            jump Jubes_AnalPrep
            return
            #end "auto"


    if not JubesX.Anal and "no anal" not in JubesX.recent_history:
            #first time
            $ JubesX.change_face("surprised", 1)
            $ JubesX.Mouth = "kiss"
            ch_v "Huh, anal?"

            if JubesX.Forced:
                $ JubesX.change_face("sad")
                ch_v "Anal? That's what you're pushing for?"

    if "anal" in JubesX.recent_history:
            $ JubesX.change_face("sexy", 1)
            ch_v "Sure, get in there."
            jump Jubes_AnalPrep


    if not JubesX.Anal and Approval:
            #First time dialog
            if JubesX.Forced:
                $ JubesX.change_face("sad")
                $ JubesX.change_stat("love", 70, -3, 1)
                $ JubesX.change_stat("love", 20, -2, 1)
            elif JubesX.love >= (JubesX.obedience + JubesX.inhibition):
                $ JubesX.change_face("sexy")
                $ JubesX.Brows = "sad"
                $ JubesX.Mouth = "smile"
                ch_v "I was hoping you'd ask. . ."
            elif JubesX.obedience >= JubesX.inhibition:
                $ JubesX.change_face("normal")
                ch_v "I expected that. . ."
            elif JubesX.Addict >= 50:
                $ JubesX.change_face("manic", 1)
                ch_v "Hmm, sounds fun. . ."
            else: # Uninhibited
                $ JubesX.change_face("sad")
                $ JubesX.Mouth = "smile"
                ch_v "I was tired of waiting. . ."

    elif Approval:
            #Second time+ dialog
            if JubesX.Forced:
                $ JubesX.change_face("sad")
                $ JubesX.change_stat("love", 70, -3, 1)
                $ JubesX.change_stat("love", 20, -2, 1)
                ch_v "You don't hold back. . ."
            elif not Taboo and "tabno" in JubesX.daily_history:
                ch_v "I guess this is secluded enough. . ."
            elif "anal" in JubesX.daily_history and not JubesX.Loose:
                pass
            elif "anal" in JubesX.recent_history:
                ch_v "I am warmed up. . ."
                jump Jubes_AnalPrep
            elif "anal" in JubesX.daily_history:
                $ JubesX.change_face("sexy", 1)
                $ line = renpy.random.choice(["Back again so soon?",
                    "So you'd like another round?",
                    "Again? Sure.",
                    "Didn't get enough earlier?",
                    "Your funeral, " + JubesX.Petname + "."])
                ch_v "[line]"
            else:
                $ JubesX.change_face("sexy", 1)
                $ JubesX.ArmPose = 2
                $ line = renpy.random.choice(["Oooh, you want some of this?",
                    "So you'd like another round?",
                    "I knew you enjoyed it. . .",
                    "I hope you don't plan on wearing me out.",
                    "You want to plow me?"])
                ch_v "[line]"
            $ line = 0

    if Approval >= 2:
            #She's into it. . .
            if JubesX.Forced:
                $ JubesX.change_face("sad")
                $ JubesX.change_stat("obedience", 90, 1)
                $ JubesX.change_stat("inhibition", 60, 1)
                ch_v "Whatever."
            elif "no anal" in JubesX.daily_history:
                ch_v "Well, if you're going to keep asking. . ."
                ch_v "Might be fun. . ."
            else:
                $ JubesX.change_face("sexy", 1)
                $ JubesX.change_stat("love", 90, 1)
                $ JubesX.change_stat("inhibition", 50, 3)
                $ line = renpy.random.choice(["Well. . . ok.",
                    "Sure.",
                    "You could, I guess.",
                    "Um, yeah.",
                    "Heh, ok, ok."])
                ch_v "[line]"
                $ line = 0
            $ JubesX.change_stat("obedience", 20, 1)
            $ JubesX.change_stat("obedience", 60, 1)
            $ JubesX.change_stat("inhibition", 70, 2)
            jump Jubes_AnalPrep

    else:
            #She's not into it, but maybe. . .
            $ JubesX.change_face("angry")
            if "no anal" in JubesX.recent_history:
                ch_v "Sorry, [JubesX.Petname] \"no.\""
            elif Taboo and "tabno" in JubesX.daily_history and "no anal" in JubesX.daily_history:
                ch_v "I told you. . . this place is too exposed."
            elif "no anal" in JubesX.daily_history:
                ch_v "I just told you \"no.\""
            elif Taboo and "tabno" in JubesX.daily_history:
                ch_v "I already told you this is too public!"
            elif not JubesX.Anal:
                $ JubesX.change_face("bemused")
                ch_v "I don't know that you're ready for that yet."
            else:
                $ JubesX.change_face("bemused")
                ch_v "Maybe eventually. . ."
            menu:
                extend ""
                "Sorry, never mind." if "no anal" in JubesX.daily_history:
                    $ JubesX.change_face("bemused")
                    ch_v "Hey, I can't blame you."
                    return
                "Maybe later?" if "no anal" not in JubesX.daily_history:
                    $ JubesX.change_face("sexy")
                    ch_v "Oh, probably. . ."
                    ch_v ". . . often."
                    $ JubesX.change_stat("love", 80, 2)
                    $ JubesX.change_stat("inhibition", 70, 2)
                    if Taboo:
                        $ JubesX.recent_history.append("tabno")
                        $ JubesX.daily_history.append("tabno")
                    $ JubesX.recent_history.append("no anal")
                    $ JubesX.daily_history.append("no anal")
                    return
                "I bet it would feel really good. . .":
                    if Approval:
                        $ JubesX.change_face("sexy")
                        $ JubesX.change_stat("obedience", 90, 2)
                        $ JubesX.change_stat("obedience", 50, 2)
                        $ JubesX.change_stat("inhibition", 70, 3)
                        $ JubesX.change_stat("inhibition", 40, 2)
                        $ line = renpy.random.choice(["Yeah, probably. . .",
                                "I guess. . .",
                                "Good point. . ."])
                        ch_v "[line]"
                        $ line = 0
                        jump Jubes_AnalPrep
                    else:
                        pass

                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(JubesX, 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
                    if Approval > 1 or (Approval and JubesX.Forced):
                        $ JubesX.change_face("sad")
                        $ JubesX.change_stat("love", 70, -5, 1)
                        $ JubesX.change_stat("love", 200, -5)
                        ch_v "Oh fine, get it over with."
                        $ JubesX.change_stat("obedience", 80, 4)
                        $ JubesX.change_stat("inhibition", 80, 1)
                        $ JubesX.change_stat("inhibition", 60, 3)
                        $ JubesX.Forced = 1
                        jump Jubes_AnalPrep
                    else:
                        $ JubesX.change_stat("love", 200, -20)
                        $ JubesX.recent_history.append("angry")
                        $ JubesX.daily_history.append("angry")

    #She refused all offers.
    $ JubesX.ArmPose = 1
    if "no anal" in JubesX.daily_history:
        ch_v "Don't push it."
        $ JubesX.recent_history.append("angry")
        $ JubesX.daily_history.append("angry")
    elif JubesX.Forced:
        $ JubesX.change_face("angry", 1)
        ch_v "You're going too far."
        $ JubesX.change_stat("lust", 200, 5)
        if JubesX.love > 300:
                $ JubesX.change_stat("love", 70, -2)
        $ JubesX.change_stat("obedience", 50, -2)
        $ JubesX.recent_history.append("angry")
        $ JubesX.daily_history.append("angry")
    elif Taboo:
        # she refuses and this is too public a place for her
        $ JubesX.change_face("angry", 1)
        $ JubesX.recent_history.append("tabno")
        $ JubesX.daily_history.append("tabno")
        ch_v "This place is way too exposed."
        $ JubesX.change_stat("lust", 200, 5)
        $ JubesX.change_stat("obedience", 50, -3)
    elif "anal" in JubesX.daily_history:
        $ JubesX.change_face("bemused")
        ch_v "Not right now."
    elif JubesX.Anal:
        $ JubesX.change_face("sad")
        ch_v "You'll have to earn it."
    else:
        $ JubesX.change_face("normal", 1)
        ch_v "You haven't earned it yet."
    $ JubesX.recent_history.append("no anal")
    $ JubesX.daily_history.append("no anal")
    $ temp_modifier = 0
    return

label Jubes_AnalPrep:  #rkelj
    call Seen_First_Peen(JubesX,Partner,React=action_context)
    call Jubes_Sex_Launch("hotdog")

    if action_context == JubesX:
            #Jubes auto-starts
            $ action_context = 0
            if JubesX.wearing_skirt:
                "[JubesX.name] lays back, sliding her skirt up as she does so."
                $ JubesX.Upskirt = 1
            elif JubesX.PantsNum() >= 6:
                "[JubesX.name] lays back, sliding her [JubesX.Legs] down as she does so."
                $ JubesX.Upskirt = 1
            else:
                "[JubesX.name] rolls back and pulls you toward her."
            $ JubesX.SeenPanties = 1
            "She slides the tip along her asshole, and seems to want you to insert it."
            menu:
                "What do you do?"
                "Go with it.":
                    $ JubesX.change_stat("inhibition", 80, 3)
                    $ JubesX.change_stat("inhibition", 50, 2)
                    "[JubesX.name] slides it in."
                "Praise her.":
                    $ JubesX.change_face("sexy", 1)
                    $ JubesX.change_stat("inhibition", 80, 3)
                    ch_p "Oh yeah, [JubesX.Pet], let's do this."
                    $ JubesX.nameCheck() #checks reaction to petname
                    "[JubesX.name] slides it in."
                    $ JubesX.change_stat("love", 85, 1)
                    $ JubesX.change_stat("obedience", 90, 1)
                    $ JubesX.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ JubesX.change_face("surprised")
                    $ JubesX.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that right now, [JubesX.Pet]."
                    $ JubesX.nameCheck() #checks reaction to petname
                    "[JubesX.name] pulls back."
                    $ JubesX.change_stat("obedience", 90, 1)
                    $ JubesX.change_stat("obedience", 50, 1)
                    $ JubesX.change_stat("obedience", 30, 2)
                    $ Player.recent_history.append("nope")
                    $ JubesX.AddWord(1,"refused","refused")
                    return
            $ JubesX.PantiesDown = 1
            call Jubes_First_Bottomless(1)
    elif action_context != "auto":
        call AutoStrip(JubesX)

        if Taboo: # Jubes gets started. . .
            "[JubesX.name] glances around to see if anyone notices what she's doing."
            if "cockout" in Player.recent_history:
                "Then she lays back and slowly presses against your rigid member."
            else:
                "Then she pulls down your pants and lays back."
                "She slowly presses against your rigid member."
            $ JubesX.inhibition += int(Taboo/10)
            $ JubesX.lust += int(Taboo/5)
        else:
            if "cockout" in Player.recent_history:
                "[JubesX.name] lays back and slowly presses against your rigid member."
            else:
                "[JubesX.name] pulls down your pants and lays back."
                "She slowly presses against your rigid member."
        "She leans back a bit and your cock pops in."

    else: #if action_context == "auto"
        if (JubesX.PantsNum() >= 6 and not JubesX.Upskirt) and (JubesX.Panties and not JubesX.PantiesDown):
            "You quickly pull down her pants and her [JubesX.Panties] and press against her back door."
        elif (JubesX.Panties and not JubesX.PantiesDown):
            "You quickly pull down her [JubesX.Panties] and press against her back door."
        $ JubesX.Upskirt = 1
        $ JubesX.PantiesDown = 1
        $ JubesX.SeenPanties = 1
        call Jubes_First_Bottomless(1)

    if not JubesX.Anal:                                                      #First time stat buffs
        if JubesX.Forced:
            $ JubesX.change_stat("love", 90, -150)
            $ JubesX.change_stat("obedience", 70, 70)
            $ JubesX.change_stat("inhibition", 80, 40)
        else:
            $ JubesX.change_stat("love", 90, 10)
            $ JubesX.change_stat("obedience", 70, 30)
            $ JubesX.change_stat("inhibition", 80, 70)
    elif not JubesX.Loose:                                                   #first few times stat buffs
        if JubesX.Forced:
            $ JubesX.change_stat("love", 90, -20)
            $ JubesX.change_stat("obedience", 70, 10)
            $ JubesX.change_stat("inhibition", 80, 5)
        else:
            $ JubesX.change_stat("obedience", 70, 7)
            $ JubesX.change_stat("inhibition", 80, 5)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ line = 0
    $ counter = 0
    $ Player.Cock = "anal"
    $ primary_action = "anal"
    $ action_speed = 1
    if Taboo:
        $ JubesX.DrainWord("tabno")
    $ JubesX.DrainWord("no anal")
    $ JubesX.recent_history.append("anal")
    $ JubesX.daily_history.append("anal")

label Jubes_Anal_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(JubesX)
        call Jubes_Sex_Launch("anal")
        if action_speed >= 4:
            $ Shift = 2
#            call action_speed_Shift(2)
        $ JubesX.lustFace()
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
                                    call Slap_Ass(JubesX)
                                    $ counter += 1
                                    $ Round -= 1
                                    jump Jubes_Anal_Cycle

                        "Turn her Around":
                                    $ JubesX.Pose = "doggy" if JubesX.Pose != "doggy" else 0
                                    "You turn her around. . ."
                                    jump Jubes_Anal_Cycle

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
                                            if JubesX.Action and MultiAction:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ JubesX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")

                                    "Shift primary action":
                                            if JubesX.Action and MultiAction:
                                                    menu:
                                                        "How about sex?":
                                                                $ action_context = "shift"
                                                                call Jubes_AnalAfter
                                                                call Jubes_Sex_P
                                                        "Just stick it in her pussy [[without asking].":
                                                                $ action_context = "auto"
                                                                call Jubes_AnalAfter
                                                                call Jubes_Sex_P
                                                        "Pull back to hotdog her.":
                                                                $ action_context = "pullback"
                                                                call Jubes_AnalAfter
                                                                call Jubes_Sex_H
                                                        "Never Mind":
                                                                jump Jubes_Anal_Cycle
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [JubesX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(JubesX)
                                            "Ask [JubesX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(JubesX)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(JubesX)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jubes_Anal_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jubes_Anal_Cycle
                                            "Never mind":
                                                        jump Jubes_Anal_Cycle
                                    "Just take a look at her.":
                                            $ Player.Cock = 0
                                            $ action_speed = 0

                                    "Show her feet" if not ShowFeet and JubesX.Pose == "doggy":
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and JubesX.Pose == "doggy":
                                            $ ShowFeet = 0

                                    "Undress [JubesX.name]":
                                            call Girl_Undress(JubesX)
                                    "Clean up [JubesX.name] (locked)" if not JubesX.Spunk:
                                            pass
                                    "Clean up [JubesX.name]" if JubesX.Spunk:
                                            call Girl_Cleanup(JubesX,"ask")
                                    "Never mind":
                                            jump Jubes_Anal_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Jubes_Sex_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Jubes_AnalAfter
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Jubes_Sex_Reset
                                    $ line = 0
                                    jump Jubes_AnalAfter
        #End menu (if line)

        call Shift_Focus(JubesX)
        call Sex_Dialog(JubesX,Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JubesX.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JubesX)
                            if "angry" in JubesX.recent_history:
                                call Jubes_Sex_Reset
                                return
                            $ JubesX.change_stat("lust", 200, 5)
                            if 100 > JubesX.lust >= 70 and JubesX.OCount < 2:
                                    $ JubesX.recent_history.append("unsatisfied")
                                    $ JubesX.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jubes_AnalAfter
                            $ line = "came"

                    if JubesX.lust >= 100:
                            #If you're still going at it and Jubes can cum
                            call Girl_Cumming(JubesX)
                            if action_context == "shift" or "angry" in JubesX.recent_history:
                                jump Jubes_AnalAfter

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Jubes_AnalAfter
                            elif "unsatisfied" in JubesX.recent_history:
                                #And Jubes is unsatisfied,
                                $ line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ line = "You get back into it"
                                        jump Jubes_Anal_Cycle
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Jubes_AnalAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Jubes_AnalAfter
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if JubesX.SEXP >= 100 or ApprovalCheck(JubesX, 1200, "LO"):
            pass
        elif counter == (5 + JubesX.Anal):
                    $ JubesX.Brows = "confused"
                    ch_v "We getting close here?"
        elif counter == (10 + JubesX.Anal):
                    $ JubesX.Brows = "angry"
                    menu:
                        ch_v "Can we. . . do something. . . else?"
                        "How about a BJ?" if JubesX.Action and MultiAction:
                                $ action_context = "shift"
                                call Jubes_AnalAfter
                                call Jubes_Blowjob
                        "How about a Handy?" if JubesX.Action and MultiAction:
                                $ action_context = "shift"
                                call Jubes_AnalAfter
                                call Jubes_Handjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ counter += 1
                                jump Jubes_Anal_Cycle
                        "Let's try something else." if MultiAction:
                                $ line = 0
                                call Jubes_Sex_Reset
                                $ action_context = "shift"
                                jump Jubes_AnalAfter
                        "No, get back down there.":
                                if ApprovalCheck(JubesX, 1200) or ApprovalCheck(JubesX, 500, "O"):
                                    $ JubesX.change_stat("love", 200, -5)
                                    $ JubesX.change_stat("obedience", 50, 3)
                                    $ JubesX.change_stat("obedience", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    $ JubesX.change_face("angry", 1)
                                    call Jubes_Sex_Reset
                                    "She scowls at you and pulls out."
                                    ch_v "Not with that attitude."
                                    $ JubesX.change_stat("love", 50, -3, 1)
                                    $ JubesX.change_stat("love", 80, -4, 1)
                                    $ JubesX.change_stat("obedience", 30, -1, 1)
                                    $ JubesX.change_stat("obedience", 50, -1, 1)
                                    $ JubesX.recent_history.append("angry")
                                    $ JubesX.daily_history.append("angry")
                                    jump Jubes_AnalAfter
        #End Count check

        if Round == 10:
                call Sex_Basic_Dialog(JubesX,10) #"I could use a break soon. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(JubesX,5)   #". . . I could really use a break here. . ."

    #Round = 0 loop breaks
    $ JubesX.change_face("bemused", 0)
    $ line = 0
    call Sex_Basic_Dialog(JubesX,"done") # ch_s "Ok, that's it, I need a break."



# Jubes hotdog //////////////////////////////////////////////////////////////////////

label Jubes_Sex_H: #rkelj
    #fix remove
    "This option is currently unavailable. It will be added in a later update."
    return
    #fix remove

    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JubesX)
    if JubesX.Hotdog >= 3: #You've done it before several times
        $ temp_modifier += 10
    elif JubesX.Hotdog: #You've done it before
        $ temp_modifier += 5

    if JubesX.lust > 85:
        $ temp_modifier += 10
    elif JubesX.lust > 75: #She's really horny
        $ temp_modifier += 5
    if action_context == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in JubesX.Traits:
        $ temp_modifier += (3*Taboo)
    if JubesX in Player.Harem or "sex friend" in JubesX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JubesX.Traits:
        $ temp_modifier -= 40
    if JubesX.ForcedCount and not JubesX.Forced:
        $ temp_modifier -= 5 * JubesX.ForcedCount

    if Taboo and "tabno" in JubesX.daily_history:
        $ temp_modifier -= 10

    if "no hotdog" in JubesX.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no hotdog" in JubesX.recent_history else 0

    $ Approval = ApprovalCheck(JubesX, 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)

    if action_context == "auto":
            call Jubes_Sex_Launch("hotdog")
            "You push [JubesX.name] down, and press your cock against her."
            $ JubesX.change_face("surprised", 1)

            if (JubesX.Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
                "[JubesX.name] glances down and then breaks into a smile."
                $ JubesX.change_face("sly")
                $ JubesX.change_stat("obedience", 70, 3)
                $ JubesX.change_stat("inhibition", 50, 3)
                $ JubesX.change_stat("inhibition", 70, 1)
                ch_v "Oh, what did you have in mind with that? . ."
                jump Jubes_HotdogPrep
            else:                                                                                                            #she's questioning it
                $ JubesX.Brows = "angry"
                menu:
                    ch_v "You might want to take a step back, [JubesX.Petname]?"
                    "Sorry, sorry! Never mind.":
                        if Approval:
                            $ JubesX.change_face("sexy", 1)
                            $ JubesX.change_stat("obedience", 70, 3)
                            $ JubesX.change_stat("inhibition", 50, 3)
                            $ JubesX.change_stat("inhibition", 70, 1)
                            ch_v "Or not. . ."
                            jump Jubes_HotdogPrep
                        "You pull back from her."
                        $ JubesX.change_face("bemused", 1)
                        ch_v "Maybe ask first?"
                    "You'll see.":
                        $ JubesX.change_stat("love", 80, -10, 1)
                        $ JubesX.change_stat("love", 200, -8)
                        "You grind against her crotch."
                        $ JubesX.change_stat("obedience", 70, 3)
                        $ JubesX.change_stat("inhibition", 50, 3)
                        if not ApprovalCheck(JubesX, 500, "O", TabM=1): #Checks if obedience is 700+
                            $ JubesX.change_face("angry")
                            "[JubesX.name] shoves you away."
                            ch_v "Don't push it, [JubesX.Petname]."
                            $ JubesX.change_stat("love", 50, -10, 1)
                            $ JubesX.change_stat("obedience", 50, 3)
                            $ renpy.pop_call()
                            if action_context:
                                $ renpy.pop_call()
                            call Jubes_Sex_Reset
                            $ JubesX.recent_history.append("angry")
                            $ JubesX.daily_history.append("angry")
                        else:
                            $ JubesX.change_face("sad")
                            "[JubesX.name] doesn't seem to be into this, but she knows her place."
                            jump Jubes_HotdogPrep
            return
            #end auto


    if not JubesX.Hotdog and "no hotdog" not in JubesX.recent_history:
            #first time
            $ JubesX.change_face("surprised", 1)
            $ JubesX.Mouth = "kiss"
            ch_v "What, just grinding?"

            if JubesX.Forced:
                $ JubesX.change_face("sad")
                ch_v ". . . nothing more?"


    if not JubesX.Hotdog and Approval:
            #First time dialog
            if JubesX.Forced:
                $ JubesX.change_face("sad")
                $ JubesX.change_stat("love", 70, -3, 1)
                $ JubesX.change_stat("love", 20, -2, 1)
            elif JubesX.love >= (JubesX.obedience + JubesX.inhibition):
                $ JubesX.change_face("sexy")
                $ JubesX.Brows = "sad"
                $ JubesX.Mouth = "smile"
                ch_v "If that's what you're into. . ."
            elif JubesX.obedience >= JubesX.inhibition:
                $ JubesX.change_face("normal")
                ch_v "If that's what works for you. . ."
            elif JubesX.Addict >= 50:
                $ JubesX.change_face("manic", 1)
                ch_v "Hrmm. . ."
            else: # Uninhibited
                $ JubesX.change_face("sad")
                $ JubesX.Mouth = "smile"
                ch_v "Well if that's what gets you off. . ."

    elif Approval:
            #Second time+ dialog
            if JubesX.Forced:
                $ JubesX.change_face("sad")
                $ JubesX.change_stat("love", 70, -3, 1)
                $ JubesX.change_stat("love", 20, -2, 1)
                ch_v "That's pushing it. . ."
            elif not Taboo and "tabno" in JubesX.daily_history:
                ch_v "I guess this is a better location . ."
            elif "hotdog" in JubesX.recent_history:
                $ JubesX.change_face("sexy", 1)
                ch_v "Again? Fine, whatever."
                jump Jubes_HotdogPrep
            elif "hotdog" in JubesX.daily_history:
                $ JubesX.change_face("sexy", 1)
                $ line = renpy.random.choice(["Back again so soon?",
                    "So you'd like another round?",
                    "You're really into this. . .",
                    "Are you sure that's all you want?"])
                ch_v "[line]"
            else:
                $ JubesX.change_face("sexy", 1)
                $ JubesX.ArmPose = 2
                $ line = renpy.random.choice(["Oooh, you want some of this?",
                    "So you'd like another round?",
                    "You're really into this. . .",
                    "You want another rub?"])
                ch_v "[line]"
            $ line = 0

    if Approval >= 2:
            #She's into it. . .
            if JubesX.Forced:
                $ JubesX.change_face("sad")
                $ JubesX.change_stat("obedience", 80, 1)
                $ JubesX.change_stat("inhibition", 60, 1)
                ch_v "Ok, fine."
            elif "no hotdog" in JubesX.daily_history:
                ch_v "It was rather entertaining. . ."
            else:
                $ JubesX.change_face("sexy", 1)
                $ JubesX.change_stat("love", 80, 1)
                $ JubesX.change_stat("inhibition", 50, 2)
                $ line = renpy.random.choice(["Well, sure, let me give it a rub.",
                    "Very well.",
                    "Nice!",
                    "I guess we could do that.",
                    "Ok, let me. . .",
                    "Heh, ok, ok."])
                ch_v "[line]"
                $ line = 0
            $ JubesX.change_stat("obedience", 60, 1)
            $ JubesX.change_stat("inhibition", 70, 2)
            jump Jubes_HotdogPrep

    else:
            #She's not into it, but maybe. . .
            $ JubesX.change_face("angry")
            if "no hotdog" in JubesX.recent_history:
                ch_v "Sorry, [JubesX.Petname] \"no.\""
            elif Taboo and "tabno" in JubesX.daily_history and "no hotdog" in JubesX.daily_history:
                ch_v "I just told you. . .not in such an exposed location."
            elif "no hotdog" in JubesX.daily_history:
                ch_v "I'm believe I just told you \"no,\" [JubesX.Petname]."
            elif Taboo and "tabno" in JubesX.daily_history:
                ch_v "I told you. . . this place is too exposed."
            elif not JubesX.Hotdog:
                $ JubesX.change_face("bemused")
                ch_v "Hmm, that could be amusing, [JubesX.Petname]. . ."
            else:
                $ JubesX.change_face("bemused")
                ch_v "I don't think that would be appropriate. . ."
            menu:
                extend ""
                "Sorry, never mind." if "no hotdog" in JubesX.daily_history:
                    $ JubesX.change_face("bemused")
                    ch_v "So long as you don't push it."
                    return
                "Maybe later?" if "no hotdog" not in JubesX.daily_history:
                    $ JubesX.change_face("sexy")
                    ch_v "I gues eventually. . ."
                    $ JubesX.change_stat("love", 80, 1)
                    $ JubesX.change_stat("inhibition", 50, 1)
                    if Taboo:
                        $ JubesX.recent_history.append("tabno")
                        $ JubesX.daily_history.append("tabno")
                    $ JubesX.recent_history.append("no hotdog")
                    $ JubesX.daily_history.append("no hotdog")
                    return
                "You might like it. . .":
                    if Approval:
                        $ JubesX.change_face("sexy")
                        $ JubesX.change_stat("obedience", 60, 2)
                        $ JubesX.change_stat("inhibition", 50, 2)
                        $ line = renpy.random.choice(["Yeah, probably. . .",
                                "I guess. . .",
                                "Good point. . ."])
                        ch_v "[line]"
                        $ line = 0
                        jump Jubes_HotdogPrep
                    else:
                        pass

                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(JubesX, 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                    if Approval > 1 or (Approval and JubesX.Forced):
                        $ JubesX.change_face("sad")
                        $ JubesX.change_stat("love", 70, -2, 1)
                        $ JubesX.change_stat("love", 200, -2)
                        ch_v "Alright, fine."
                        $ JubesX.change_stat("obedience", 80, 4)
                        $ JubesX.change_stat("inhibition", 60, 2)
                        $ JubesX.Forced = 1
                        jump Jubes_HotdogPrep
                    else:
                        $ JubesX.change_stat("love", 200, -10)
                        $ JubesX.recent_history.append("angry")
                        $ JubesX.daily_history.append("angry")

    #She refused all offers.
    $ JubesX.ArmPose = 1

    if "no hotdog" in JubesX.daily_history:
        ch_v "What did I tell you?"
        $ JubesX.recent_history.append("angry")
        $ JubesX.daily_history.append("angry")
    if JubesX.Forced:
        $ JubesX.change_face("angry", 1)
        ch_v "There's no point trying."
        $ JubesX.change_stat("lust", 200, 5)
        if JubesX.love > 300:
                $ JubesX.change_stat("love", 70, -1)
        $ JubesX.change_stat("obedience", 50, -1)
        $ JubesX.recent_history.append("angry")
        $ JubesX.daily_history.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ JubesX.change_face("angry", 1)
        $ JubesX.recent_history.append("tabno")
        $ JubesX.daily_history.append("tabno")
        ch_v "This area is a bit too exposed for that sort of thing. . ."
        $ JubesX.change_stat("lust", 200, 5)
        $ JubesX.change_stat("obedience", 50, -3)
    elif JubesX.Hotdog:
        $ JubesX.change_face("sad")
        ch_v "Not anymore."
    else:
        $ JubesX.change_face("normal", 1)
        ch_v "No thanks."
    $ JubesX.recent_history.append("no hotdog")
    $ JubesX.daily_history.append("no hotdog")
    $ temp_modifier = 0
    return

label Jubes_Hotdog_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(JubesX)
        call Jubes_Sex_Launch("hotdog")
        if action_speed >= 4:
            $ action_speed = 2
#            call action_speed_Shift(2)
        $ JubesX.lustFace()
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
                                    call Slap_Ass(JubesX)
                                    $ counter += 1
                                    $ Round -= 1
                                    jump Jubes_Hotdog_Cycle

                        "Turn her Around":
                                    $ JubesX.Pose = "doggy" if JubesX.Pose != "doggy" else 0
                                    "You turn her around. . ."
                                    jump Jubes_Hotdog_Cycle

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
                                            if JubesX.Action and MultiAction:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ JubesX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")

                                    "Shift primary action":
                                            if JubesX.Action and MultiAction:
                                                    menu:
                                                        "How about sex?":
                                                            $ action_context = "shift"
                                                            call Jubes_HotdogAfter
                                                            call Jubes_Sex_P
                                                        "Just stick it in her pussy [[without asking].":
                                                            $ action_context = "auto"
                                                            call Jubes_HotdogAfter
                                                            call Jubes_Sex_P
                                                        "How about anal?":
                                                            $ action_context = "shift"
                                                            call Jubes_HotdogAfter
                                                            call Jubes_Sex_A
                                                        "Just stick it in her ass [[without asking].":
                                                            $ action_context = "auto"
                                                            call Jubes_HotdogAfter
                                                            call Jubes_Sex_A
                                                        "Never Mind":
                                                                jump Jubes_Hotdog_Cycle
                                            else:
                                                call Sex_Basic_Dialog(JubesX,"tired")
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [JubesX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(JubesX)
                                            "Ask [JubesX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(JubesX)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(JubesX)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jubes_Hotdog_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jubes_Hotdog_Cycle
                                            "Never mind":
                                                        jump Jubes_Hotdog_Cycle
                                    "Just take a look at her.":
                                            $ Player.Cock = 0
                                            $ action_speed = 0

                                    "Show her feet" if not ShowFeet and JubesX.Pose == "doggy":
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and JubesX.Pose == "doggy":
                                            $ ShowFeet = 0

                                    "Undress [JubesX.name]":
                                            call Girl_Undress(JubesX)
                                    "Clean up [JubesX.name] (locked)" if not JubesX.Spunk:
                                            pass
                                    "Clean up [JubesX.name]" if JubesX.Spunk:
                                            call Girl_Cleanup(JubesX,"ask")
                                    "Never mind":
                                            jump Jubes_Hotdog_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Jubes_Sex_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Jubes_HotdogAfter
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Jubes_Sex_Reset
                                    $ line = 0
                                    jump Jubes_HotdogAfter
        #End menu (if line)

        call Shift_Focus(JubesX)
        call Sex_Dialog(JubesX,Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JubesX.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JubesX)
                            if "angry" in JubesX.recent_history:
                                call Jubes_Sex_Reset
                                return
                            $ JubesX.change_stat("lust", 200, 5)
                            if 100 > JubesX.lust >= 70 and JubesX.OCount < 2:
                                    $ JubesX.recent_history.append("unsatisfied")
                                    $ JubesX.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jubes_HotdogAfter
                            $ line = "came"

                    if JubesX.lust >= 100:
                            #If you're still going at it and Jubes can cum
                            call Girl_Cumming(JubesX)
                            if action_context == "shift" or "angry" in JubesX.recent_history:
                                jump Jubes_HotdogAfter

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Jubes_HotdogAfter
                            elif "unsatisfied" in JubesX.recent_history:
                                #And Jubes is unsatisfied,
                                $ line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ line = "You get back into it"
                                        jump Jubes_Hotdog_Cycle
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Jubes_HotdogAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Jubes_HotdogAfter
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if JubesX.SEXP >= 100 or ApprovalCheck(JubesX, 1200, "LO"):
            pass
        elif counter == (5 + JubesX.Hotdog):
                    $ JubesX.Brows = "confused"
                    ch_v "Are we getting close here?"
        elif counter == (10 + JubesX.Hotdog):
                    $ JubesX.Brows = "angry"
                    menu:
                        ch_v "I'm kinda bored by this."
                        "How about a BJ?" if JubesX.Action and MultiAction:
                                $ action_context = "shift"
                                call Jubes_HotdogAfter
                                call Jubes_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ counter += 1
                                jump Jubes_Hotdog_Cycle
                        "Let's try something else." if MultiAction:
                                $ line = 0
                                call Jubes_Sex_Reset
                                $ action_context = "shift"
                                jump Jubes_HotdogAfter
                        "No, get back down there.":
                                if ApprovalCheck(JubesX, 1200) or ApprovalCheck(JubesX, 500, "O"):
                                    $ JubesX.change_stat("love", 200, -5)
                                    $ JubesX.change_stat("obedience", 50, 3)
                                    $ JubesX.change_stat("obedience", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    $ JubesX.change_face("angry", 1)
                                    call Jubes_Sex_Reset
                                    "She scowls at you and pulls away."
                                    ch_v "Not with that attitude."
                                    $ JubesX.change_stat("love", 50, -3, 1)
                                    $ JubesX.change_stat("love", 80, -4, 1)
                                    $ JubesX.change_stat("obedience", 30, -1, 1)
                                    $ JubesX.change_stat("obedience", 50, -1, 1)
                                    $ JubesX.recent_history.append("angry")
                                    $ JubesX.daily_history.append("angry")
                                    jump Jubes_HotdogAfter
        #End Count check

        call Escalation(JubesX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(JubesX,10) #"I could use a break soon. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(JubesX,5)   #". . . I could really use a break here. . ."

    #Round = 0 loop breaks
    $ JubesX.change_face("bemused", 0)
    $ line = 0
    call Sex_Basic_Dialog(JubesX,"done") # ch_s "Ok, that's it, I need a break."
