# Jean_SexMenu //////////////////////////////////////////////////////////////////////
label Jean_SexAct(Act = 0):
        if AloneCheck(JeanX) and JeanX.Taboo == 20:
                $ JeanX.Taboo = 0
                $ Taboo = 0
        call Shift_Focus(JeanX)
        if Act == "SkipTo":
            $ renpy.pop_call() #causes it to skip past the Trigger Swap
            $ renpy.pop_call() #causes it to skip past the cycle you were in before
            #$ renpy.pop_call() #causes it to skip past the sex menu you were in before that
            call SkipTo(JeanX)
        elif Act == "switch":
            $ renpy.pop_call() #causes it to skip past call here from Sex_Menu_Threesome
            #$ renpy.pop_call() #causes it to skip past call to Sex_Menu_Threesome
            # drops through to sex menu
        elif Act == "masturbate":
            call Jean_M_Prep
            if not Situation:
                return
        elif Act == "lesbian":
            call Les_Prep(JeanX) #nee call Jean_Les_Prep
            if not Situation:
                return
        elif Act == "kissing":
            call KissPrep(JeanX)
            if not Situation:
                return
        elif Act == "breasts":
            call Jean_Fondle_Breasts
            if not Situation:
                return
        elif Act == "blow":
            call Jean_BJ_Prep
            if not Situation:
                return
        elif Act == "hand":
            call Jean_HJ_Prep
            if not Situation:
                return
        elif Act == "sex":
            call Jean_SexPrep
            if not Situation:
                return

##  JeanX.Masturbating //////////////////////////////////////////////////////////////////////
# Cnt 1 means she's seen you, Cnt 0 means she hasn't.
label Jean_Masturbate: #(Situation = Situation):
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
    if JeanX.Lust >= 90:
        $ temp_modifier += 20
    elif JeanX.Lust >= 75:
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

    if Situation == "join":       # This triggers if you ask to join in
                if Approval > 1 or (Approval and JeanX.Lust >= 50):
                    $ Player.AddWord(1,"join")
                    menu:
                        extend ""
                        "Would you like some help? I could lend some helping hands. . ."  if Player.Semen and JeanX.Action:
                                $ JeanX.Statup("Love", 90, 1)
                                $ JeanX.Statup("Obed", 50, 2)
                                $ JeanX.FaceChange("sexy")
                                ch_j "Hmm, ok, give these a squeeze. . ."
                                $ JeanX.Statup("Obed", 70, 2)
                                $ JeanX.Statup("Inbt", 70, 1)
                                $ Trigger2 = "fondle breasts"
                                $ JeanX.Mast += 1
                                jump Jean_M_Cycle
                        "Would you like some help? I could. . . up to you, I guess." if Player.Semen and JeanX.Action:
                                $ JeanX.Statup("Love", 70, 2)
                                $ JeanX.Statup("Love", 90, 1)
                                $ JeanX.FaceChange("sexy")
                                ch_j "Ok, sure. . ."
                                $ JeanX.Statup("Obed", 70, 2)
                                $ JeanX.Statup("Inbt", 70, 1)
                                $ D20 = renpy.random.randint(1, 20)
                                if D20 > 10:
                                    $ Trigger2 = "fondle breasts"
                                else:
                                    $ Trigger2 = "suck breasts"
                                $ JeanX.Mast += 1
                                jump Jean_M_Cycle
                        "Why don't we take care of each other?" if Player.Semen and JeanX.Action:
                                $ JeanX.FaceChange("sexy")
                                ch_j "Like what?"
                                $ renpy.pop_call()          #removes the call to this label
                                return                      #returns to sexmenu=
                        "You look like you have things well in hand. . .":
                                if JeanX.Lust >= 50:
                                    $ JeanX.Statup("Love", 70, 2)
                                    $ JeanX.Statup("Love", 90, 1)
                                    $ JeanX.FaceChange("sexy")
                                    ch_j "I'm getting there. . ."
                                    $ JeanX.Statup("Obed", 80, 3)
                                    $ JeanX.Statup("Inbt", 80, 5)
                                    jump Jean_M_Cycle
                                elif ApprovalCheck(JeanX, 1200):
                                    $ JeanX.FaceChange("sly")
                                    ch_j "Yeah. . . but I can take a break. . ."
                                else:
                                    $ JeanX.FaceChange("angry")
                                    ch_j "-well I -was.-"

                #else: You've failed all checks so she kicks you out.
                $ JeanX.ArmPose = 1
                $ JeanX.OutfitChange()
                $ JeanX.Action -= 1
                $ Player.Statup("Focus", 50, 30)
                call Checkout(1)
                $ Line = 0
                $ Situation = 0
                $ renpy.pop_call()          #removes the call to this label
                if Approval:
                        $ JeanX.FaceChange("bemused", 2)
                        if bg_current == JeanX.Home:
                            ch_j "Why are you in my room?"
                        else:
                            ch_j "I didn't call for anyone. . ."
                        $ JeanX.Blush = 1
                else:
                        $ JeanX.Statup("Love", 200, -5)
                        $ JeanX.FaceChange("angry")
                        $ JeanX.RecentActions.append("angry")
                        $ JeanX.DailyActions.append("angry")
                        if bg_current == JeanX.Home:
                            ch_j "I was busy, so get out."
                            "[JeanX.Name] kicks you out of her room."
                            $ renpy.pop_call()
                            jump Campus_Map
                        else:
                            ch_j "I'm leaving, but maybe knock next time?"
                            call Remove_Girl(JeanX)
                return                      #returns to sexmenu, which returns to original
    #End of "Join" option



    if Situation == JeanX:                                                                  #Jean auto-starts
                if Approval > 2:
                        if JeanX.PantsNum() == 5:
                            "[JeanX.Name]'s hand snakes down her body, and hikes up her skirt."
                            $ JeanX.Upskirt = 1
                        elif JeanX.PantsNum() >= 6:
                            "[JeanX.Name] slides her hand down her body and into her pants."
                        elif JeanX.HoseNum() >= 5:
                            "[JeanX.Name]'s hand slides down her body and under her [JeanX.Hose]."
                        elif JeanX.Panties:
                            "[JeanX.Name]'s hand slides down her body and under her [JeanX.Panties]."
                        else:
                            "[JeanX.Name]'s hand slides down her body and begins to caress her pussy."
                        $ JeanX.SeenPanties = 1
                        call Jean_First_Bottomless(1)
                        "She starts to slowly rub herself."
                        menu:
                            "What do you do?"
                            "Nothing.":
                                    $ JeanX.Statup("Inbt", 80, 3)
                                    $ JeanX.Statup("Inbt", 60, 2)
                                    "[JeanX.Name] begins to masturbate."
                            "Go for it.":
                                    $ JeanX.FaceChange("sexy, 1")
                                    $ JeanX.Statup("Inbt", 80, 3)
                                    ch_p "That is so sexy, [JeanX.Pet]."
                                    $ JeanX.NameCheck() #checks reaction to petname
                                    "You lean back and enjoy the show."
                                    $ JeanX.Statup("Love", 80, 1)
                                    $ JeanX.Statup("Obed", 90, 1)
                                    $ JeanX.Statup("Obed", 50, 2)
                            "Ask her to stop.":
                                    $ JeanX.FaceChange("surprised")
                                    $ JeanX.Statup("Inbt", 70, 1)
                                    ch_p "Let's not do that right now, [JeanX.Pet]."
                                    $ JeanX.NameCheck() #checks reaction to petname
                                    "[JeanX.Name] pulls her hands away from herself."
                                    $ JeanX.OutfitChange()
                                    $ JeanX.Statup("Obed", 90, 1)
                                    $ JeanX.Statup("Obed", 50, 1)
                                    $ JeanX.Statup("Obed", 30, 2)
                                    return
                        jump Jean_M_Prep
                else:
                        $ temp_modifier = 0
                        $ Trigger2 = 0
                return
    #End if Jean intitiates this action

    #first time
    if not JeanX.Mast:
            $ JeanX.FaceChange("surprised", 1)
            $ JeanX.Mouth = "kiss"
            ch_j "Oh, so you want to watch while I get off?"
            if JeanX.Forced:
                $ JeanX.FaceChange("sad")
                ch_j "But -just- watch, right? . ."


    #First time dialog
    if not JeanX.Mast and Approval:
            if JeanX.Forced:
                $ JeanX.FaceChange("sad")
                $ JeanX.Statup("Love", 70, -3, 1)
                $ JeanX.Statup("Love", 20, -2, 1)
            elif JeanX.Love >= JeanX.Obed and JeanX.Love >= (JeanX.Inbt - JeanX.IX):
                $ JeanX.FaceChange("sexy")
                $ JeanX.Brows = "sad"
                $ JeanX.Mouth = "smile"
                ch_j "Well. . ."
            elif JeanX.Obed >= (JeanX.Inbt - JeanX.IX):
                $ JeanX.FaceChange("normal")
                ch_j "If that's what you're into. . ."
            else: # Uninhibited
                $ JeanX.FaceChange("sad")
                $ JeanX.Mouth = "smile"
                ch_j "I do have some time. . ."


    #Second time+ initial dialog
    elif Approval:
            if JeanX.Forced:
                $ JeanX.FaceChange("sad")
                $ JeanX.Statup("Love", 70, -3, 1)
                $ JeanX.Statup("Love", 20, -2, 1)
                ch_j "Hmm, again?"
            elif Approval and "masturbation" in JeanX.RecentActions:
                $ JeanX.FaceChange("sexy", 1)
                ch_j "Mmmm . . ."
                jump Jean_M_Prep
            elif Approval and "masturbation" in JeanX.DailyActions:
                $ JeanX.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Did you enjoy that?",
                    "Didn't get enough earlier?",
                    "I do like having an audience. . ."])
                ch_j "[Line]"
            elif JeanX.Mast < 3:
                $ JeanX.FaceChange("sexy", 1)
                $ JeanX.Brows = "confused"
                ch_j "You enjoyed that, huh."
            else:
                $ JeanX.FaceChange("sexy", 1)
                $ JeanX.ArmPose = 2
                $ Line = renpy.random.choice(["You do like to watch.",
                    "Again?",
                    "You like to watch me.",
                    "You'd like me to masturbate again?"])
                ch_j "[Line]"
                $ Line = 0
    #End second time+ initial dialog

    #If she's into it. . .
    if Approval >= 2:
            if JeanX.Forced:
                $ JeanX.FaceChange("sad")
                $ JeanX.Statup("Obed", 90, 1)
                $ JeanX.Statup("Inbt", 60, 1)
                ch_j "Oh. . . fine. . ."
            else:
                $ JeanX.FaceChange("sexy", 1)
                $ JeanX.Statup("Love", 90, 1)
                $ JeanX.Statup("Inbt", 50, 3)
                $ Line = renpy.random.choice(["Sure. Ok.",
                    "Couldn't hurt. . .",
                    "All right.",
                    "Sure.",
                    "Sure, why not. . ."])
                ch_j "[Line]"
                $ Line = 0
            $ JeanX.Statup("Obed", 20, 1)
            $ JeanX.Statup("Obed", 60, 1)
            $ JeanX.Statup("Inbt", 70, 2)
            jump Jean_M_Prep

    #If she's not into it, but maybe. . .
    else:
        menu:
            ch_j "I don't know, it's kind of a bad time. . ."
            "Maybe later?":
                    $ JeanX.FaceChange("sexy", 1)
                    if JeanX.Lust > 70:
                        ch_j "Well -I- will, but after you leave."
                    else:
                        ch_j "Wel. . . maybe. . ."
                    $ JeanX.Statup("Love", 80, 2)
                    $ JeanX.Statup("Inbt", 70, 2)
                    return
            "You look like you could use it. . .":
                    if Approval:
                        $ JeanX.FaceChange("sexy")
                        $ JeanX.Statup("Obed", 90, 2)
                        $ JeanX.Statup("Obed", 50, 2)
                        $ JeanX.Statup("Inbt", 70, 3)
                        $ JeanX.Statup("Inbt", 40, 2)
                        $ Line = renpy.random.choice(["Sure. Ok.",
                                "Couldn't hurt. . .",
                                "All right.",
                                "Sure.",
                                "Sure, why not. . ."])
                        ch_j "[Line]"
                        $ Line = 0
                        jump Jean_M_Prep

            "Just get at it already.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(JeanX, 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                    if Approval > 1 or (Approval and JeanX.Forced):
                        $ JeanX.FaceChange("sad")
                        $ JeanX.Statup("Love", 70, -5, 1)
                        $ JeanX.Statup("Love", 200, -5)
                        ch_j "Oh. . . fine. . ."
                        $ JeanX.Statup("Obed", 80, 4)
                        $ JeanX.Statup("Inbt", 80, 1)
                        $ JeanX.Statup("Inbt", 60, 3)
                        $ JeanX.Forced = 1
                        jump Jean_M_Prep
                    else:
                        $ JeanX.Statup("Love", 200, -20)
                        $ JeanX.RecentActions.append("angry")
                        $ JeanX.DailyActions.append("angry")
    # end of asking her to do it

    #She refused all offers.
    $ JeanX.ArmPose = 1
    if JeanX.Forced:
            $ JeanX.FaceChange("angry", 1)
            ch_j "Nope, too kinky."
            $ JeanX.Statup("Lust", 90, 5)
            if JeanX.Love > 300:
                $ JeanX.Statup("Love", 70, -2)
            $ JeanX.Statup("Obed", 50, -2)
            $ JeanX.RecentActions.append("angry")
            $ JeanX.DailyActions.append("angry")
            $ JeanX.RecentActions.append("no masturbation")
            $ JeanX.DailyActions.append("no masturbation")
            return
    elif JeanX.Taboo:                             # she refuses and this is too public a place for her
            $ JeanX.FaceChange("angry", 1)
            $ JeanX.DailyActions.append("tabno")
            ch_j "I. . . couldn't do that in public. . ."
            $ JeanX.Statup("Lust", 90, 5)
            $ JeanX.Statup("Obed", 50, -3)
            return
    elif JeanX.Mast:
            $ JeanX.FaceChange("sad")
            ch_j "Eh, I think I'm ok for now. . ."
    else:
            $ JeanX.FaceChange("normal", 1)
            ch_j "Um, no."
    $ JeanX.RecentActions.append("no masturbation")
    $ JeanX.DailyActions.append("no masturbation")
    $ temp_modifier = 0
    return

label Jean_M_Prep:
    $ JeanX.Upskirt = 1
    $ JeanX.PantiesDown = 1
    call Jean_First_Bottomless(1)
    call Set_The_Scene(Dress=0)

    #if she hasn't seen you yet. . .
    if "unseen" in JeanX.RecentActions:
            $ JeanX.FaceChange("sexy")
            $ JeanX.Eyes = "closed"
            $ JeanX.ArmPose = 2
            "You see [JeanX.Name] leaning back, masturbating. You don't think she's noticed you yet."
    else:
            $ JeanX.FaceChange("sexy")
            $ JeanX.ArmPose = 2
            "[JeanX.Name] lays back and starts to toy with herself."
            if not JeanX.Mast:#First time
                    if JeanX.Forced:
                        $ JeanX.Statup("Love", 90, -20)
                        $ JeanX.Statup("Obed", 70, 45)
                        $ JeanX.Statup("Inbt", 80, 35)
                    else:
                        $ JeanX.Statup("Love", 90, 15)
                        $ JeanX.Statup("Obed", 70, 35)
                        $ JeanX.Statup("Inbt", 80, 40)


    $ Trigger = "masturbation"
    if not Trigger3:
        $ Trigger3 = "fondle pussy"

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    if JeanX.Taboo:
        $ JeanX.DrainWord("tabno")
    $ JeanX.DrainWord("no masturbation")
    $ JeanX.RecentActions.append("masturbation")
    $ JeanX.DailyActions.append("masturbation")

label Jean_M_Cycle:
    if Situation == "join":
        $ renpy.pop_call()
        $ Situation = 0

    while Round > 0:
        call Jean_Pos_Reset("masturbation")
        call Shift_Focus(JeanX)
        $ JeanX.LustFace()

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep Watching.":
                                pass

                        "[JeanX.Name]. . .[[jump in]" if "unseen" not in JeanX.RecentActions and "join" not in Player.RecentActions and JeanX.Loc == bg_current:
                                "[JeanX.Name] slows what she's doing with a sly grin."
                                ch_j "Like what you see?"
                                $ Situation = "join"
                                call Jean_Masturbate
                        "\"Ahem. . .\"" if "unseen" in JeanX.RecentActions and JeanX.Loc == bg_current:
                                jump Jean_M_Interupted

                        "Start jack'in it." if Trigger2 != "jackin":
                                call Jackin(JeanX)
                        "Stop jack'in it." if Trigger2 == "jackin":
                                $ Trigger2 = 0

                        "Slap her ass" if JeanX.Loc == bg_current:
                                if "unseen" in JeanX.RecentActions:
                                        "You smack [JeanX.Name] firmly on the ass!"
                                        jump Jean_M_Interupted
                                else:
                                        call Slap_Ass(JeanX)
                                        $ Cnt += 1
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
                                            if JeanX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ JeanX.Action -= 1
                                            else:
                                                ch_j "I'd like to stick with this."

                                    "Threesome actions (locked)" if not Partner or "unseen" in JeanX.RecentActions or JeanX.Loc != bg_current:
                                        pass
                                    "Threesome actions" if Partner and "unseen" not in JeanX.RecentActions and JeanX.Loc == bg_current:
                                        menu:
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(JeanX)
                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(JeanX)
                                            "Undress [Partner.Name]":
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

                                    "Undress [JeanX.Name]":
                                            if "unseen" in JeanX.RecentActions:
                                                    ch_p "Oh, yeah, take it off. . ."
                                                    jump Jean_M_Interupted
                                            else:
                                                    call Girl_Undress(JeanX)
                                    "Clean up [JeanX.Name] (locked)" if not JeanX.Spunk:
                                            pass
                                    "Clean up [JeanX.Name]" if JeanX.Spunk:
                                            if "unseen" in JeanX.RecentActions:
                                                    ch_p "You've got a little something on you. . ."
                                                    jump Jean_M_Interupted
                                            else:
                                                    call Girl_Cleanup(JeanX,"ask")
                                    "Never mind":
                                                    jump Jean_M_Cycle

                        "Back to Sex Menu" if MultiAction and JeanX.Loc == bg_current:
                                    ch_p "Let's try something else."
                                    call Jean_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Jean_M_Interupted
                        "End Scene" if not MultiAction or JeanX.Loc != bg_current:
                                    ch_p "Let's stop for now."
                                    call Jean_Pos_Reset
                                    $ Line = 0
                                    jump Jean_M_Interupted
        #End menu (if Line)

        call Shift_Focus(JeanX)
        call Sex_Dialog(JeanX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up

        if Player.Focus >= 100 or JeanX.Lust >= 100:
                    #If you can cum:
                    if Player.Focus >= 100:
                        if "unseen" not in JeanX.RecentActions:
                            #if she knows you're there
                            call Player_Cumming(JeanX)
                            if "angry" in JeanX.RecentActions:
                                call Jean_Pos_Reset
                                return
                            $ JeanX.Statup("Lust", 200, 5)
                            if 100 > JeanX.Lust >= 70 and JeanX.OCount < 2:
                                $ JeanX.RecentActions.append("unsatisfied")
                                $ JeanX.DailyActions.append("unsatisfied")
                            $ Line = "came"
                        else: #If she wasn't aware you were there
                            "You grunt and try to hold it in."
                            $ Player.Focus = 95
                            if JeanX.Loc == bg_current:
                                    jump Jean_M_Interupted

                    #If Jean can cum
                    if JeanX.Lust >= 100:
                        call Girl_Cumming(JeanX)
                        if JeanX.Loc == bg_current:
                                jump Jean_M_Interupted

                    if Line == "came":
                        $ Line = 0
                        if not Player.Semen:
                            "You're emptied out, you should probably take a break."
                            $ Trigger2 = 0 if Trigger2 == "jackin" else Trigger2


                        if "unsatisfied" in JeanX.RecentActions:#And Jean is unsatisfied,
                            "[JeanX.Name] still seems a bit unsatisfied with the experience."
                            menu:
                                "Let her keep going?"
                                "Yes, keep going for a bit.":
                                    $ Line = "You let her get back into it"
                                    jump Jean_M_Cycle
                                "No, I'm done.":
                                    "You ask her to stop."
                                    return
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        if "unseen" in JeanX.RecentActions:
                if Round == 10:
                    "It's getting a bit late, [JeanX.Name] will probably be wrapping up soon."
                elif Round == 5:
                    "She's definitely going to stop soon."
        else:
                if JeanX.Loc == bg_current:
                        call Escalation(JeanX) #sees if she wants to escalate things

                if Round == 10:
                    ch_j "Wow, look at the time. . ."
                    $ JeanX.Lust += 10
                elif Round == 5:
                    ch_j "Ok, can we take a break?"
                    $ JeanX.Lust += 25

    #Round = 0 loop breaks
    $ JeanX.FaceChange("bemused", 0)
    $ Line = 0
    if "unseen" not in JeanX.RecentActions:
        ch_j "Ok, that's it, break time."

label Jean_M_Interupted:

    # If she hasn't noticed you're there before cumming
    if "unseen" in JeanX.RecentActions:
                $ JeanX.FaceChange("surprised", 2)
                "[JeanX.Name] stops what she's doing with a start, eyes wide."
                call Jean_First_Bottomless(1)
                $ JeanX.FaceChange("surprised", 2)

                #If you've been jacking it
                if Trigger2 == "jackin":
                        ch_j "Oh, hey. . .[JeanX.Petname]."
                        ch_j "When did you get here?"
                        $ JeanX.Eyes = "down"
                        menu:
                            ch_j "I see you've been making yourself at home. . . "
                            "A while back, it was an excellent show.":
                                    $ JeanX.FaceChange("sexy",1)
                                    $ JeanX.Statup("Obed", 50, 3)
                                    $ JeanX.Statup("Obed", 70, 2)
                                    ch_j "True. . ."
                                    if JeanX.Love >= 800 or JeanX.Obed >= 500 or (JeanX.Inbt - JeanX.IX) >= 500:
                                        $ temp_modifier += 10
                                        $ JeanX.Statup("Lust", 90, 5)
                                        ch_j "And you can put on quite a show yourself. . ."

                            "I. . . just got here?":
                                    $ JeanX.FaceChange("angry",1)
                                    $ JeanX.Statup("Love", 70, 2)
                                    $ JeanX.Statup("Love", 90, 1)
                                    $ JeanX.Statup("Obed", 50, 2)
                                    $ JeanX.Statup("Obed", 70, 2)
                                    "She looks pointedly at your cock,"
                                    ch_j "A likely story. . ."
                                    if JeanX.Love >= 800 or JeanX.Obed >= 500 or (JeanX.Inbt - JeanX.IX) >= 500:
                                            $ temp_modifier += 10
                                            $ JeanX.Statup("Lust", 90, 5)
                                            $ JeanX.FaceChange("bemused", 1)
                                            ch_j "I guess I can't blame you. . ."
                                    else:
                                            $ temp_modifier -= 10
                                            $ JeanX.Statup("Lust", 200, -5)
                        call Seen_First_Peen(JeanX,Partner)
                        ch_j "Hmm. . ."

                #you haven't been jacking it
                else:
                        ch_j "Oh, hey. . .[JeanX.Petname]."
                        ch_j "When did you get here?"
                        menu:
                            extend ""
                            "A while back.":
                                    $ JeanX.FaceChange("sexy", 1)
                                    $ JeanX.Statup("Obed", 50, 3)
                                    $ JeanX.Statup("Obed", 70, 2)
                                    ch_j "Nice of you to let me know. . ."
                            "I just got here.":
                                    $ JeanX.FaceChange("bemused", 1)
                                    $ JeanX.Statup("Love", 70, 2)
                                    $ JeanX.Statup("Love", 90, 1)
                                    ch_j "Uh-huh. . ."
                                    $ JeanX.Statup("Obed", 50, 2)
                                    $ JeanX.Statup("Obed", 70, 2)

                $ JeanX.DrainWord("unseen",1,0) #She sees you, so remove unseens
                $ JeanX.Mast += 1
                if Round <= 10:
                    ch_j "I could use a break anyway. . ."
                    return
                $ Situation = "join"
                call Jean_Masturbate
                "error: report this if you see it."
                return #should be redundant
    #End Unseen

    #else, if She's seen you already
    $ JeanX.Action -= 1
    $ JeanX.Mast += 1
    call Checkout
    if Situation == "shift":
        $ Situation = 0
        return
    $ Situation = 0

    if Partner == EmmaX:
        call Partner_Like(JeanX,3)
    else:
        call Partner_Like(JeanX,2)

    if JeanX.Loc != bg_current:
        return

    if Round <= 10:
            ch_j "I need a minute here. . ."
            return
    $ JeanX.FaceChange("sexy", 1)
    if JeanX.Lust < 20:
        ch_j "I got off, how about you?"
    else:
        ch_j "So, what next?"
    menu:
        extend ""
        "Well, I have something you could take care of. . ." if Player.Semen and JeanX.Action:
                $ Situation = "shift"
                return
        "You could just keep going. . ." if Player.Semen:
                $ JeanX.FaceChange("sly")
                if JeanX.Action and Round >= 10:
                    ch_j "Ok. . ."
                    jump Jean_M_Cycle
                else:
                    ch_j "I need a minute here. . ."
        "I'm good here. [[Stop]":
                if JeanX.Love < 800 and JeanX.Inbt < 500 and JeanX.Obed < 500:
                    $ JeanX.OutfitChange()
                $ JeanX.FaceChange("normal")
                $ JeanX.Brows = "confused"
                ch_j "Ok."
                $ JeanX.Brows = "normal"
        "You should probably stop for now." if JeanX.Lust > 30:
                $ JeanX.FaceChange("angry")
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

    if JeanX.Lust > 85:
        $ temp_modifier += 10
    elif JeanX.Lust > 75: #She's really horny
        $ temp_modifier += 5

    if Situation == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in JeanX.Traits:
        $ temp_modifier += (4*Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JeanX.Traits:
        $ temp_modifier -= 40
    if JeanX.ForcedCount and not JeanX.Forced:
        $ temp_modifier -= 5 * JeanX.ForcedCount



    if JeanX.Taboo and "tabno" in JeanX.DailyActions:
        $ temp_modifier -= 10

    if "no sex" in JeanX.DailyActions:
        $ temp_modifier -= 15 if "no sex" in JeanX.RecentActions else 5


    $ Approval = ApprovalCheck(JeanX, 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)

    if Situation == "auto":
                call Jean_Sex_Launch("sex")
                if JeanX.PantsNum() == 5:
                    "You flip [JeanX.Name] around, sliding her skirt up as you go."
                    $ JeanX.Upskirt = 1
                elif JeanX.PantsNum() >= 6:
                    "You flip [JeanX.Name] around, sliding her pants down as you do."
                    $ JeanX.Upskirt = 1
                else:
                    "You flip [JeanX.Name] around."
                $ JeanX.SeenPanties = 1
                "You rub the tip of your cock against her moist slit."
                $ JeanX.FaceChange("surprised", 1)

                if (JeanX.Sex and Approval) or (Approval > 1):
                    #this is not the first time you've had sex, or she's into it
                    "[JeanX.Name] glances back and then breaks into a smile."
                    $ JeanX.FaceChange("sly")
                    $ JeanX.Statup("Obed", 70, 3)
                    $ JeanX.Statup("Inbt", 50, 3)
                    $ JeanX.Statup("Inbt", 70, 1)
                    ch_j "Oh, if you must, [JeanX.Petname]."
                    jump Jean_SexPrep
                else:
                    #she's questioning it
                    $ JeanX.Brows = "angry"
                    menu:
                        ch_j "Just sticking it in?"
                        "Sorry, sorry! Never mind.":
                            if Approval:
                                    $ JeanX.FaceChange("sexy", 1)
                                    $ JeanX.Statup("Obed", 70, 3)
                                    $ JeanX.Statup("Inbt", 50, 3)
                                    $ JeanX.Statup("Inbt", 70, 1)
                                    ch_j "Oh, no, it's fine."
                                    jump Jean_SexPrep
                            else:
                                    "You pull back before you really get it in."
                                    $ JeanX.FaceChange("bemused", 1)
                                    #if JeanX.Sex:
                                    ch_j "You should ask first, [JeanX.Petname]."
                                    #else:
                                        #ch_j "Maybe if you'd asked first. . ."
                        "Just fucking.":
                            $ JeanX.Statup("Love", 80, -10, 1)
                            $ JeanX.Statup("Love", 200, -10)
                            "You press inside some more."
                            $ JeanX.Statup("Obed", 70, 3)
                            $ JeanX.Statup("Inbt", 50, 3)
                            if not ApprovalCheck(JeanX, 700, "O", TabM=1):   #Checks if Obed is 700+
                                $ JeanX.FaceChange("angry")
                                "[JeanX.Name] shoves you away and backhands you in the face."
                                ch_j "Hey, I don't need my powers to hurt you."
                                $ JeanX.Statup("Love", 50, -10, 1)
                                $ JeanX.Statup("Obed", 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                call Jean_Sex_Reset
                                $ JeanX.RecentActions.append("angry")
                                $ JeanX.DailyActions.append("angry")
                            else:
                                $ JeanX.FaceChange("sad")
                                "[JeanX.Name] doesn't seem to be into this, you're lucky she's willing to give it a try."
                                jump Jean_SexPrep
                return
    #End Auto


    if not JeanX.Sex and "no sex" not in JeanX.RecentActions:
            #first time
            $ JeanX.FaceChange("surprised", 1)
            $ JeanX.Mouth = "kiss"
            ch_j "Oh, you wanna fuck . . "
            if JeanX.Forced:
                $ JeanX.FaceChange("sad")
                ch_j "Pretty bold of you. . ."


    if not JeanX.Sex and Approval:
            #First time dialog
            if JeanX.Forced:
                $ JeanX.FaceChange("sad")
                $ JeanX.Statup("Love", 70, -30, 1)
                $ JeanX.Statup("Love", 20, -20, 1)
            elif JeanX.Love >= (JeanX.Obed + JeanX.Inbt - JeanX.IX):
                $ JeanX.FaceChange("sexy")
                $ JeanX.Brows = "sad"
                $ JeanX.Mouth = "smile"
                ch_j "I was wondering when this would come up. . ."
            elif JeanX.Obed >= (JeanX.Inbt - JeanX.IX):
                $ JeanX.FaceChange("normal")
                ch_j "Ok, [JeanX.Petname]. . ."
            elif JeanX.Addict >= 50:
                $ JeanX.FaceChange("manic", 1)
                ch_j "That does sound fun. . ."
            else: # Uninhibited
                $ JeanX.FaceChange("sad")
                $ JeanX.Mouth = "smile"
                ch_j "I was wondering when this would come up. . ."
            #End first time dialog

    elif Approval:
            #Second time+ dialog
            $ JeanX.FaceChange("sexy", 1)
            if JeanX.Forced:
                $ JeanX.FaceChange("sad")
                $ JeanX.Statup("Love", 70, -3, 1)
                $ JeanX.Statup("Love", 20, -2, 1)
                ch_j "You'll pay for this eventually. . ."
            elif not JeanX.Taboo and "tabno" in JeanX.DailyActions:
                ch_j "Ok, yeah, this is better."
            elif "sex" in JeanX.RecentActions:
                ch_j "Again? Your funeral."
                jump Jean_SexPrep
            elif "sex" in JeanX.DailyActions:
                $ Line = renpy.random.choice(["Back again?",
                    "You'd like another round?",
                    "I must be better than I thought.",
                    "Didn't get enough earlier?",
                    "Your funeral, " + JeanX.Petname + "."])
                ch_j "[Line]"
            elif JeanX.Sex < 3:
                $ JeanX.Brows = "confused"
                $ JeanX.Mouth = "kiss"
                ch_j "Oh? Another round?"
            else:
                $ Line = renpy.random.choice(["Oh, you want some of this?",
                    "You'd like another round?",
                    "I must be better than I thought.",
                    "I hope you don't plan on wearing me out.",
                    "You want to fuck me?"])
                ch_j "[Line]"
            $ Line = 0
            #end Second time+ dialog

    if Approval >= 2:
            #She's into it. . .
            if JeanX.Forced:
                $ JeanX.FaceChange("sad")
                $ JeanX.Statup("Obed", 90, 1)
                $ JeanX.Statup("Inbt", 60, 1)
                ch_j "Ok, fine. Just make it good."
            elif "no sex" in JeanX.DailyActions:
                ch_j "Ok, whatever. . ."
            else:
                $ JeanX.FaceChange("sexy", 1)
                $ JeanX.Statup("Love", 90, 1)
                $ JeanX.Statup("Inbt", 50, 3)
                $ Line = renpy.random.choice(["Well. . . fine, let's do it.",
                    "Sure.",
                    "We could, I guess.",
                    "Hmmm, sure.",
                    "Sounds fun."])
                ch_j "[Line]"
                $ Line = 0
            $ JeanX.Statup("Obed", 20, 1)
            $ JeanX.Statup("Obed", 60, 1)
            $ JeanX.Statup("Inbt", 70, 2)
            jump Jean_SexPrep

    else:
            #She's not into it, but maybe. . .
            $ JeanX.FaceChange("angry")
            if "no sex" in JeanX.RecentActions:
                ch_j "I don't repeat myself."
            elif JeanX.Taboo and "tabno" in JeanX.DailyActions and "no sex" in JeanX.DailyActions:
                ch_j "I'm not comfortable with that. . ."
            elif "no sex" in JeanX.DailyActions:
                ch_j "Not today."
            elif JeanX.Taboo and "tabno" in JeanX.DailyActions:
                ch_j "I told you, I'm not comfortable with that. . ."
            elif not JeanX.Sex:
                $ JeanX.FaceChange("bemused")
                ch_j "Oh, this would be interesting. . ."
            else:
                $ JeanX.FaceChange("bemused")
                ch_j "I'm not in the mood right now . ."
            menu:
                extend ""
                "Sorry, never mind." if "no sex" in JeanX.DailyActions:
                        $ JeanX.FaceChange("bemused")
                        ch_j "Keep trying. . ."
                        return
                "Maybe later?" if "no sex" not in JeanX.DailyActions:
                        $ JeanX.FaceChange("sexy")
                        ch_j "Sure, whatever. . ."
                        $ JeanX.Statup("Love", 80, 2)
                        $ JeanX.Statup("Inbt", 70, 2)
                        if JeanX.Taboo:
                            $ JeanX.RecentActions.append("tabno")
                            $ JeanX.DailyActions.append("tabno")
                        $ JeanX.RecentActions.append("no sex")
                        $ JeanX.DailyActions.append("no sex")
                        return
                "I think you'd enjoy it as much as I would. . .":
                        if Approval:
                            $ JeanX.FaceChange("sexy")
                            $ JeanX.Statup("Obed", 90, 2)
                            $ JeanX.Statup("Obed", 50, 2)
                            $ JeanX.Statup("Inbt", 70, 3)
                            $ JeanX.Statup("Inbt", 40, 2)
                            $ Line = renpy.random.choice(["Yeah, probably. . .",
                                "I guess. . .",
                                "Good point. . ."])
                            ch_j "[Line]"
                            $ Line = 0
                            jump Jean_SexPrep
                "Just deal with it.":                                               # Pressured into it
                        $ Approval = ApprovalCheck(JeanX, 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
                        if Approval > 1 or (Approval and JeanX.Forced):
                            $ JeanX.FaceChange("confused",Eyes="side")
                            $ JeanX.Statup("Love", 70, -5, 1)
                            $ JeanX.Statup("Love", 200, -5)
                            ch_j ". . ."
                            ch_j ". . . Ok. . ."
                            $ JeanX.Statup("Obed", 80, 4)
                            $ JeanX.Statup("Inbt", 80, 1)
                            $ JeanX.Statup("Inbt", 60, 3)
                            $ JeanX.Forced = 1
                            jump Jean_SexPrep
                        else:
                            $ JeanX.Statup("Love", 200, -20)
                            $ JeanX.RecentActions.append("angry")
                            $ JeanX.DailyActions.append("angry")
                #end menu
    #end Approval check

    #She refused all offers.
    $ JeanX.ArmPose = 1
    if "no sex" in JeanX.DailyActions:
        ch_j "Don't push your luck, [JeanX.Petname]."
        $ JeanX.RecentActions.append("angry")
        $ JeanX.DailyActions.append("angry")
    elif JeanX.Forced:
        $ JeanX.FaceChange("angry", 1)
        ch_j "I'm the queen here!"
        $ JeanX.Statup("Lust", 200, 5)
        if JeanX.Love > 300:
                $ JeanX.Statup("Love", 70, -2)
        $ JeanX.Statup("Obed", 50, -2)
        ch_j "I do not take orders."
        $ JeanX.RecentActions.append("angry")
        $ JeanX.DailyActions.append("angry")
    elif JeanX.Taboo:                             # she refuses and this is too public a place for her
        $ JeanX.FaceChange("angry", 1)
        $ JeanX.RecentActions.append("tabno")
        $ JeanX.DailyActions.append("tabno")
        ch_j "I'm just not comfortable with that right now. . ."
        $ JeanX.Statup("Lust", 200, 5)
        $ JeanX.Statup("Obed", 50, -3)
    elif JeanX.Sex:
        $ JeanX.FaceChange("sad")
        ch_j "Maybe just fuck one of the others."
    else:
        $ JeanX.FaceChange("normal", 1)
        ch_j "Not interested."
    $ JeanX.RecentActions.append("no sex")
    $ JeanX.DailyActions.append("no sex")
    $ temp_modifier = 0
    return

label Jean_Sex_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(JeanX)
        call Jean_Sex_Launch("sex")
        if Speed >= 4:
            $ Speed = 2
#            call Speed_Shift(2)
        $ JeanX.LustFace()
        $ Player.Sprite = 1
        $ Player.Cock = "in"
        $ Trigger = "sex"
        $ JeanX.Upskirt = 1
        $ JeanX.PantiesDown = 1

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass
                        "Keep going. . . (locked)" if not Speed:
                                    pass

                        "Start moving? . ." if not Speed:
                                    $ Speed = 1
#                                    call Speed_Shift(1)
                        "Speed up. . ." if 0 < Speed < 3:
                                    $ Speed += 1
#                                    call Speed_Shift(Speed+1)
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 3:
                                    pass

                        "Slow Down. . ." if Speed:
                                    $ Speed -= 1
#                                    call Speed_Shift(Speed-1)
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(JeanX)
                                    $ Cnt += 1
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
                                            if JeanX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ JeanX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Shift primary action":
                                            if JeanX.Action and MultiAction:
                                                    menu:
                                                        "How about anal?":
                                                                $ Situation = "shift"
                                                                call Jean_SexAfter
                                                                call Jean_Sex_A
                                                        "Just stick it in her ass [[without asking].":
                                                                $ Situation = "auto"
                                                                call Jean_SexAfter
                                                                call Jean_Sex_A
                                                        "Pull back to hotdog her.":
                                                                $ Situation = "pullback"
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
                                            "Ask [JeanX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(JeanX)
                                            "Ask [JeanX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(JeanX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(JeanX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jean_Sex_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jean_Sex_Cycle
                                            "Never mind":
                                                        jump Jean_Sex_Cycle
                                    "Just take a look at her.":
                                            $ Player.Cock = 0
                                            $ Speed = 0

                                    "Show her feet" if not ShowFeet and JeanX.Pose == "doggy":
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and JeanX.Pose == "doggy":
                                            $ ShowFeet = 0

                                    "Undress [JeanX.Name]":
                                            call Girl_Undress(JeanX)
                                    "Clean up [JeanX.Name] (locked)" if not JeanX.Spunk:
                                            pass
                                    "Clean up [JeanX.Name]" if JeanX.Spunk:
                                            call Girl_Cleanup(JeanX,"ask")
                                    "Never mind":
                                            jump Jean_Sex_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Jean_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Jean_SexAfter
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Jean_Sex_Reset
                                    $ Line = 0
                                    jump Jean_SexAfter
        #End menu (if Line)

        call Shift_Focus(JeanX)
        call Sex_Dialog(JeanX,Partner)

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JeanX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JeanX)
                            if "angry" in JeanX.RecentActions:
                                call Jean_Sex_Reset
                                return
                            $ JeanX.Statup("Lust", 200, 5)
                            if 100 > JeanX.Lust >= 70 and JeanX.OCount < 2:
                                    $ JeanX.RecentActions.append("unsatisfied")
                                    $ JeanX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jean_SexAfter
                            $ Line = "came"

                    if JeanX.Lust >= 100:
                            #If you're still going at it and Jean can cum
                            call Girl_Cumming(JeanX)
                            if Situation == "shift" or "angry" in JeanX.RecentActions:
                                jump Jean_SexAfter

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Jean_SexAfter
                            elif "unsatisfied" in JeanX.RecentActions:
                                #And Jean is unsatisfied,
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ Line = "You get back into it"
                                        jump Jean_Sex_Cycle
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Jean_SexAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Jean_SexAfter
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if JeanX.SEXP >= 100 or ApprovalCheck(JeanX, 1200, "LO"):
            pass
        elif Cnt == (5 + JeanX.Sex):
                    $ JeanX.Brows = "confused"
                    ch_j "Ok, had enough yet?"
        elif Cnt == (10 + JeanX.Sex):
                    $ JeanX.Brows = "angry"
                    menu:
                        ch_j "Hey. . . you. . . about done. . . there?"
                        "How about a BJ?" if JeanX.Action and MultiAction:
                                $ Situation = "shift"
                                call Jean_SexAfter
                                call Jean_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ Cnt += 1
                                jump Jean_Sex_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Jean_Sex_Reset
                                $ Situation = "shift"
                                jump Jean_SexAfter
                        "No, get back down there.":
                                if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                                    $ JeanX.Statup("Love", 200, -5)
                                    $ JeanX.Statup("Obed", 50, 3)
                                    $ JeanX.Statup("Obed", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    $ JeanX.FaceChange("angry", 1)
                                    call Jean_Sex_Reset
                                    "She scowls at you and pulls out."
                                    ch_j "Don't overestimate yourself."
                                    $ JeanX.Statup("Love", 50, -3, 1)
                                    $ JeanX.Statup("Love", 80, -4, 1)
                                    $ JeanX.Statup("Obed", 30, -1, 1)
                                    $ JeanX.Statup("Obed", 50, -1, 1)
                                    $ JeanX.RecentActions.append("angry")
                                    $ JeanX.DailyActions.append("angry")
                                    jump Jean_SexAfter
        #End Count check

        call Escalation(JeanX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(JeanX,10) #"You might want to wrap this up, it's getting late."
        elif Round == 5:
                call Sex_Basic_Dialog(JeanX,5)   #"Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ JeanX.FaceChange("bemused", 0)
    $ Line = 0
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

    if JeanX.Lust > 85:
        $ temp_modifier += 10
    elif JeanX.Lust > 75: #She's really horny
        $ temp_modifier += 5

    $ temp_modifier += 10  # she starts out loose

    if Situation == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in JeanX.Traits:
        $ temp_modifier += (5*Taboo)

    if JeanX in Player.Harem or "sex friend" in JeanX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JeanX.Traits:
        $ temp_modifier -= 40
    if JeanX.ForcedCount and not JeanX.Forced:
        $ temp_modifier -= 5 * JeanX.ForcedCount

    if JeanX.Taboo and "tabno" in JeanX.DailyActions:
        $ temp_modifier -= 10
    if "no anal" in JeanX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no anal" in JeanX.RecentActions else 0

    $ Approval = ApprovalCheck(JeanX, 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)

    if Situation == "auto":
            call Jean_Sex_Launch("anal")
            if JeanX.PantsNum() == 5:
                "You flip [JeanX.Name] around, sliding her skirt up as you go."
                $ JeanX.Upskirt = 1
            elif JeanX.PantsNum() >= 6:
                "You flip [JeanX.Name] around, sliding her pants down as you do."
                $ JeanX.Legs = 0
            else:
                "You flip [JeanX.Name] around."
            $ JeanX.SeenPanties = 1
            "You press the tip of your cock against her tight rim."
            $ JeanX.FaceChange("surprised", 1)
            call Jean_First_Bottomless(1)

            if (JeanX.Anal and Approval) or (Approval > 1):
                #this is not the first time you've had sex, or she's into it
                $ JeanX.Statup("Obed", 70, 3)
                $ JeanX.Statup("Inbt", 50, 3)
                $ JeanX.Statup("Inbt", 70, 1)
                "[JeanX.Name] glances back and then breaks into a smile."
                ch_j "Oh! Sure. . ."
                jump Jean_AnalPrep
            else:
                #she's questioning it
                $ JeanX.Brows = "angry"
                menu:
                    ch_j "Sticking in the back?"
                    "Sorry, sorry! Never mind.":
                        if Approval:
                            $ JeanX.FaceChange("sexy", 1)
                            $ JeanX.Statup("Obed", 70, 3)
                            $ JeanX.Statup("Inbt", 50, 3)
                            $ JeanX.Statup("Inbt", 70, 1)
                            ch_j "Sure, works for me. . ."
                            ch_j "Get in there."
                            jump Jean_AnalPrep
                        "You pull back before you really get it in."
                        $ JeanX.FaceChange("bemused", 1)

                        #if JeanX.Anal:
                            #ch_j "You coulda warned me. . ."
                        #else:
                        ch_j "Hey, just ask first. . ."
                    "Just fucking.":
                        $ JeanX.Statup("Love", 80, -10, 1)
                        $ JeanX.Statup("Love", 200, -8)
                        "You press into her."
                        $ JeanX.Statup("Obed", 70, 3)
                        $ JeanX.Statup("Inbt", 50, 3)
                        if not ApprovalCheck(JeanX, 700, "O", TabM=1):
                            $ JeanX.FaceChange("angry")
                            "[JeanX.Name] shoves you away and backhands you in the face."
                            ch_j "Tsk tsk."
                            $ JeanX.Statup("Love", 50, -10, 1)
                            $ JeanX.Statup("Obed", 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            call Jean_Sex_Reset
                            $ JeanX.RecentActions.append("angry")
                            $ JeanX.DailyActions.append("angry")
                        else:
                            $ JeanX.FaceChange("sad")
                            "[JeanX.Name] doesn't seem to be into this, you're lucky she's willing to give it a try."
                            jump Jean_AnalPrep
            return
            #end "auto"


    if not JeanX.Anal and "no anal" not in JeanX.RecentActions:
            #first time
            $ JeanX.FaceChange("surprised", 1)
            $ JeanX.Mouth = "kiss"
            ch_j "Oh, you're into anal?"

            if JeanX.Forced:
                $ JeanX.FaceChange("sad")
                ch_j "That's the card you're going to play?"

    if "anal" in JeanX.RecentActions:
            $ JeanX.FaceChange("sexy", 1)
            ch_j "Ok, sure."
            jump Jean_AnalPrep


    if not JeanX.Anal and Approval:
            #First time dialog
            if JeanX.Forced:
                $ JeanX.FaceChange("sad")
                $ JeanX.Statup("Love", 70, -3, 1)
                $ JeanX.Statup("Love", 20, -2, 1)
            elif JeanX.Love >= (JeanX.Obed + JeanX.Inbt - JeanX.IX):
                $ JeanX.FaceChange("sexy")
                $ JeanX.Brows = "sad"
                $ JeanX.Mouth = "smile"
                ch_j "I was expecting this. . ."
            elif JeanX.Obed >= (JeanX.Inbt - JeanX.IX):
                $ JeanX.FaceChange("normal")
                ch_j "I expected that. . ."
            elif JeanX.Addict >= 50:
                $ JeanX.FaceChange("manic", 1)
                ch_j "Hmm, sounds fun. . ."
            else: # Uninhibited
                $ JeanX.FaceChange("sad")
                $ JeanX.Mouth = "smile"
                ch_j "I was tired of waiting. . ."

    elif Approval:
            #Second time+ dialog
            if JeanX.Forced:
                $ JeanX.FaceChange("sad")
                $ JeanX.Statup("Love", 70, -3, 1)
                $ JeanX.Statup("Love", 20, -2, 1)
                ch_j "Well you're optimistic. . ."
            elif not JeanX.Taboo and "tabno" in JeanX.DailyActions:
                ch_j "I guess here is fine. . ."
            elif "anal" in JeanX.DailyActions and not JeanX.Loose:
                pass
            elif "anal" in JeanX.RecentActions:
                ch_j "I am warmed up. . ."
                jump Jean_AnalPrep
            elif "anal" in JeanX.DailyActions:
                $ JeanX.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Back again so soon?",
                    "So you'd like another round?",
                    "Again? Sure.",
                    "Didn't get enough earlier?",
                    "Your funeral, " + JeanX.Petname + "."])
                ch_j "[Line]"
            else:
                $ JeanX.FaceChange("sexy", 1)
                $ JeanX.ArmPose = 2
                $ Line = renpy.random.choice(["Oooh, you want some of this?",
                    "So you'd like another round?",
                    "I knew you enjoyed it. . .",
                    "I hope you don't plan on wearing me out.",
                    "You want to plow me?"])
                ch_j "[Line]"
            $ Line = 0

    if Approval >= 2:
            #She's into it. . .
            if JeanX.Forced:
                $ JeanX.FaceChange("sad")
                $ JeanX.Statup("Obed", 90, 1)
                $ JeanX.Statup("Inbt", 60, 1)
                ch_j "Whatever."
            elif "no anal" in JeanX.DailyActions:
                ch_j "Well, if you're going to keep asking. . ."
                ch_j "Might be fun. . ."
            else:
                $ JeanX.FaceChange("sexy", 1)
                $ JeanX.Statup("Love", 90, 1)
                $ JeanX.Statup("Inbt", 50, 3)
                $ Line = renpy.random.choice(["Well. . . ok.",
                    "Sure.",
                    "You could, I guess.",
                    "Um, yeah.",
                    "Heh, ok, ok."])
                ch_j "[Line]"
                $ Line = 0
            $ JeanX.Statup("Obed", 20, 1)
            $ JeanX.Statup("Obed", 60, 1)
            $ JeanX.Statup("Inbt", 70, 2)
            jump Jean_AnalPrep

    else:
            #She's not into it, but maybe. . .
            $ JeanX.FaceChange("angry")
            if "no anal" in JeanX.RecentActions:
                ch_j "I don't repeat myself."
            elif JeanX.Taboo and "tabno" in JeanX.DailyActions and "no anal" in JeanX.DailyActions:
                ch_j "I'm not comfortable with that. . ."
            elif "no anal" in JeanX.DailyActions:
                ch_j "Not today."
            elif JeanX.Taboo and "tabno" in JeanX.DailyActions:
                ch_j "I told you, I'm not comfortable with that. . ."
            elif not JeanX.Anal:
                $ JeanX.FaceChange("bemused")
                ch_j "I don't know that you're ready for that yet."
            else:
                $ JeanX.FaceChange("bemused")
                ch_j "Maybe eventually. . ."
            menu:
                extend ""
                "Sorry, never mind." if "no anal" in JeanX.DailyActions:
                    $ JeanX.FaceChange("bemused")
                    ch_j "I get it."
                    return
                "Maybe later?" if "no anal" not in JeanX.DailyActions:
                    $ JeanX.FaceChange("sexy")
                    ch_j "Oh, probably. . ."
                    $ JeanX.Statup("Love", 80, 2)
                    $ JeanX.Statup("Inbt", 70, 2)
                    if JeanX.Taboo:
                        $ JeanX.RecentActions.append("tabno")
                        $ JeanX.DailyActions.append("tabno")
                    $ JeanX.RecentActions.append("no anal")
                    $ JeanX.DailyActions.append("no anal")
                    return
                "I bet it would feel really good. . .":
                    if Approval:
                        $ JeanX.FaceChange("sexy")
                        $ JeanX.Statup("Obed", 90, 2)
                        $ JeanX.Statup("Obed", 50, 2)
                        $ JeanX.Statup("Inbt", 70, 3)
                        $ JeanX.Statup("Inbt", 40, 2)
                        $ Line = renpy.random.choice(["Yeah, sure. . .",
                                "I guess. . .",
                                "Good point. . ."])
                        ch_j "[Line]"
                        $ Line = 0
                        jump Jean_AnalPrep
                    else:
                        pass

                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(JeanX, 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
                    if Approval > 1 or (Approval and JeanX.Forced):
                        $ JeanX.FaceChange("confused")
                        $ JeanX.Statup("Love", 70, -5, 1)
                        $ JeanX.Statup("Love", 200, -5)
                        $ JeanX.FaceChange("angry",Eyes="side")
                        ch_j "Oh fine, get it over with."
                        $ JeanX.Statup("Obed", 80, 4)
                        $ JeanX.Statup("Inbt", 80, 1)
                        $ JeanX.Statup("Inbt", 60, 3)
                        $ JeanX.Forced = 1
                        jump Jean_AnalPrep
                    else:
                        $ JeanX.Statup("Love", 200, -20)
                        $ JeanX.RecentActions.append("angry")
                        $ JeanX.DailyActions.append("angry")

    #She refused all offers.
    $ JeanX.ArmPose = 1
    if "no anal" in JeanX.DailyActions:
        ch_j "Know when to stop."
        $ JeanX.RecentActions.append("angry")
        $ JeanX.DailyActions.append("angry")
    elif JeanX.Forced:
        $ JeanX.FaceChange("angry", 1)
        ch_j "You're overestimating your power here."
        $ JeanX.Statup("Lust", 200, 5)
        if JeanX.Love > 300:
                $ JeanX.Statup("Love", 70, -2)
        $ JeanX.Statup("Obed", 50, -2)
        $ JeanX.RecentActions.append("angry")
        $ JeanX.DailyActions.append("angry")
    elif JeanX.Taboo:
        # she refuses and this is too public a place for her
        $ JeanX.FaceChange("angry", 1)
        $ JeanX.RecentActions.append("tabno")
        $ JeanX.DailyActions.append("tabno")
        ch_j "I'm just not comfortable with that right now. . ."
        $ JeanX.Statup("Lust", 200, 5)
        $ JeanX.Statup("Obed", 50, -3)
    elif "anal" in JeanX.DailyActions:
        $ JeanX.FaceChange("bemused")
        ch_j "Not right now."
    elif JeanX.Anal:
        $ JeanX.FaceChange("sad")
        ch_j "You'll have to earn that one. . ."
    else:
        $ JeanX.FaceChange("normal", 1)
        ch_j "You haven't earned it yet."
    $ JeanX.RecentActions.append("no anal")
    $ JeanX.DailyActions.append("no anal")
    $ temp_modifier = 0
    return

label Jean_Anal_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(JeanX)
        call Jean_Sex_Launch("anal")
        if Speed >= 4:
            $ Shift = 2
#            call Speed_Shift(2)
        $ JeanX.LustFace()
        $ Player.Sprite = 1
        $ Player.Cock = "anal"
        $ Trigger = "anal"

        if Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass
                        "Keep going. . . (locked)" if not Speed:
                                    pass

                        "Start moving? . ." if not Speed:
                                    $ Speed = 1
#                                    call Speed_Shift(1)
                        "Speed up. . ." if 0 < Speed < 3:
                                    $ Speed += 1
#                                    call Speed_Shift(Speed+1)
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 3:
                                    pass

                        "Slow Down. . ." if Speed:
                                    $ Speed -= 1
#                                    call Speed_Shift(Speed-1)
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(JeanX)
                                    $ Cnt += 1
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
                                            if JeanX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ JeanX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Shift primary action":
                                            if JeanX.Action and MultiAction:
                                                    menu:
                                                        "How about sex?":
                                                                $ Situation = "shift"
                                                                call Jean_AnalAfter
                                                                call Jean_Sex_P
                                                        "Just stick it in her pussy [[without asking].":
                                                                $ Situation = "auto"
                                                                call Jean_AnalAfter
                                                                call Jean_Sex_P
                                                        "Pull back to hotdog her.":
                                                                $ Situation = "pullback"
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
                                            "Ask [JeanX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(JeanX)
                                            "Ask [JeanX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(JeanX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(JeanX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jean_Anal_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jean_Anal_Cycle
                                            "Never mind":
                                                        jump Jean_Anal_Cycle
                                    "Just take a look at her.":
                                            $ Player.Cock = 0
                                            $ Speed = 0

                                    "Show her feet" if not ShowFeet and JeanX.Pose == "doggy":
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and JeanX.Pose == "doggy":
                                            $ ShowFeet = 0

                                    "Undress [JeanX.Name]":
                                            call Girl_Undress(JeanX)
                                    "Clean up [JeanX.Name] (locked)" if not JeanX.Spunk:
                                            pass
                                    "Clean up [JeanX.Name]" if JeanX.Spunk:
                                            call Girl_Cleanup(JeanX,"ask")
                                    "Never mind":
                                            jump Jean_Anal_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Jean_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Jean_AnalAfter
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Jean_Sex_Reset
                                    $ Line = 0
                                    jump Jean_AnalAfter
        #End menu (if Line)

        call Shift_Focus(JeanX)
        call Sex_Dialog(JeanX,Partner)

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JeanX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JeanX)
                            if "angry" in JeanX.RecentActions:
                                call Jean_Sex_Reset
                                return
                            $ JeanX.Statup("Lust", 200, 5)
                            if 100 > JeanX.Lust >= 70 and JeanX.OCount < 2:
                                    $ JeanX.RecentActions.append("unsatisfied")
                                    $ JeanX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jean_AnalAfter
                            $ Line = "came"

                    if JeanX.Lust >= 100:
                            #If you're still going at it and Jean can cum
                            call Girl_Cumming(JeanX)
                            if Situation == "shift" or "angry" in JeanX.RecentActions:
                                jump Jean_AnalAfter

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Jean_AnalAfter
                            elif "unsatisfied" in JeanX.RecentActions:
                                #And Jean is unsatisfied,
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ Line = "You get back into it"
                                        jump Jean_Anal_Cycle
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Jean_AnalAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Jean_AnalAfter
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if JeanX.SEXP >= 100 or ApprovalCheck(JeanX, 1200, "LO"):
            pass
        elif Cnt == (5 + JeanX.Anal):
                    $ JeanX.Brows = "confused"
                    ch_j "Ok, that good enough?"
        elif Cnt == (10 + JeanX.Anal):
                    $ JeanX.Brows = "angry"
                    menu:
                        ch_j "Can we. . . do something. . . else?"
                        "How about a BJ?" if JeanX.Action and MultiAction:
                                $ Situation = "shift"
                                call Jean_AnalAfter
                                call Jean_Blowjob
                        "How about a Handy?" if JeanX.Action and MultiAction:
                                $ Situation = "shift"
                                call Jean_AnalAfter
                                call Jean_Handjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ Cnt += 1
                                jump Jean_Anal_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Jean_Sex_Reset
                                $ Situation = "shift"
                                jump Jean_AnalAfter
                        "No, get back down there.":
                                if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                                    $ JeanX.Statup("Love", 200, -5)
                                    $ JeanX.Statup("Obed", 50, 3)
                                    $ JeanX.Statup("Obed", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    $ JeanX.FaceChange("angry", 1)
                                    call Jean_Sex_Reset
                                    "She scowls at you and pulls out."
                                    ch_j "Don't overestimate yourself."
                                    $ JeanX.Statup("Love", 50, -3, 1)
                                    $ JeanX.Statup("Love", 80, -4, 1)
                                    $ JeanX.Statup("Obed", 30, -1, 1)
                                    $ JeanX.Statup("Obed", 50, -1, 1)
                                    $ JeanX.RecentActions.append("angry")
                                    $ JeanX.DailyActions.append("angry")
                                    jump Jean_AnalAfter
        #End Count check

        if Round == 10:
                call Sex_Basic_Dialog(JeanX,10) #"You might want to wrap this up, it's getting late."
        elif Round == 5:
                call Sex_Basic_Dialog(JeanX,5)   #"Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ JeanX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(JeanX,"done")   #"Ok, [Girl.Petname], that's enough of that for now."



# Jean hotdog //////////////////////////////////////////////////////////////////////

label Jean_Sex_H:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(JeanX)
    if JeanX.Hotdog >= 3: #You've done it before several times
        $ temp_modifier += 10
    elif JeanX.Hotdog: #You've done it before
        $ temp_modifier += 5

    if JeanX.Lust > 85:
        $ temp_modifier += 10
    elif JeanX.Lust > 75: #She's really horny
        $ temp_modifier += 5
    if Situation == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in JeanX.Traits:
        $ temp_modifier += (3*Taboo)
    if JeanX in Player.Harem or "sex friend" in JeanX.Petnames:
        $ temp_modifier += 10
    elif "ex" in JeanX.Traits:
        $ temp_modifier -= 40
    if JeanX.ForcedCount and not JeanX.Forced:
        $ temp_modifier -= 5 * JeanX.ForcedCount

    if JeanX.Taboo and "tabno" in JeanX.DailyActions:
        $ temp_modifier -= 10

    if "no hotdog" in JeanX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no hotdog" in JeanX.RecentActions else 0

    $ Approval = ApprovalCheck(JeanX, 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)

    if Situation == "auto":
            call Jean_Sex_Launch("hotdog")
            "You push [JeanX.Name] down, and press your cock against her."
            $ JeanX.FaceChange("surprised", 1)

            if (JeanX.Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
                "[JeanX.Name] glances back and then breaks into a smile."
                $ JeanX.FaceChange("sly")
                $ JeanX.Statup("Obed", 70, 3)
                $ JeanX.Statup("Inbt", 50, 3)
                $ JeanX.Statup("Inbt", 70, 1)
                ch_j "Oh, what did you have in mind with that? . ."
                jump Jean_HotdogPrep
            else:                                                                                                            #she's questioning it
                $ JeanX.Brows = "angry"
                menu:
                    ch_j "Little close there, [JeanX.Petname]?"
                    "Sorry, sorry! Never mind.":
                        if Approval:
                            $ JeanX.FaceChange("sexy", 1)
                            $ JeanX.Statup("Obed", 70, 3)
                            $ JeanX.Statup("Inbt", 50, 3)
                            $ JeanX.Statup("Inbt", 70, 1)
                            ch_j "I didn't say I minded. . ."
                            jump Jean_HotdogPrep
                        "You pull back from her."
                        $ JeanX.FaceChange("bemused", 1)
                        ch_j "Just ask first."
                    "You'll see.":
                        $ JeanX.Statup("Love", 80, -10, 1)
                        $ JeanX.Statup("Love", 200, -8)
                        "You grind against her crotch."
                        $ JeanX.Statup("Obed", 70, 3)
                        $ JeanX.Statup("Inbt", 50, 3)
                        if not ApprovalCheck(JeanX, 500, "O", TabM=1): #Checks if Obed is 700+
                            $ JeanX.FaceChange("angry")
                            "[JeanX.Name] shoves you away."
                            ch_j "Don't push it, [JeanX.Petname]."
                            $ JeanX.Statup("Love", 50, -10, 1)
                            $ JeanX.Statup("Obed", 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            call Jean_Sex_Reset
                            $ JeanX.RecentActions.append("angry")
                            $ JeanX.DailyActions.append("angry")
                        else:
                            $ JeanX.FaceChange("sad")
                            "[JeanX.Name] doesn't seem to be into this, but she knows her place."
                            jump Jean_HotdogPrep
            return
            #end auto


    if not JeanX.Hotdog and "no hotdog" not in JeanX.RecentActions:
            #first time
            $ JeanX.FaceChange("surprised", 1)
            $ JeanX.Mouth = "kiss"
            ch_j "What, just grinding?"

            if JeanX.Forced:
                $ JeanX.FaceChange("sad")
                ch_j ". . . nothing more?"
                if Approval:
                    ch_j "Which of us has a pussy here?"


    if not JeanX.Hotdog and Approval:
            #First time dialog
            if JeanX.Forced:
                $ JeanX.FaceChange("sad")
                $ JeanX.Statup("Love", 70, -3, 1)
                $ JeanX.Statup("Love", 20, -2, 1)
            elif JeanX.Love >= (JeanX.Obed + JeanX.Inbt - JeanX.IX):
                $ JeanX.FaceChange("sexy")
                $ JeanX.Brows = "sad"
                $ JeanX.Mouth = "smile"
                ch_j "Ok, we can start with that. . ."
            elif JeanX.Obed >= (JeanX.Inbt - JeanX.IX):
                $ JeanX.FaceChange("normal")
                ch_j "Ok, we can start with that. . ."
            elif JeanX.Addict >= 50:
                $ JeanX.FaceChange("manic", 1)
                ch_j "Hrmm. . ."
            else: # Uninhibited
                $ JeanX.FaceChange("sad")
                $ JeanX.Mouth = "smile"
                ch_j "Ok, we can start with that. . ."

    elif Approval:
            #Second time+ dialog
            if JeanX.Forced:
                $ JeanX.FaceChange("sad")
                $ JeanX.Statup("Love", 70, -3, 1)
                $ JeanX.Statup("Love", 20, -2, 1)
                ch_j "Odd. . ."
            elif not JeanX.Taboo and "tabno" in JeanX.DailyActions:
                ch_j "I guess this is a better location . ."
            elif "hotdog" in JeanX.RecentActions:
                $ JeanX.FaceChange("sexy", 1)
                ch_j "Again? Fine, whatever."
                jump Jean_HotdogPrep
            elif "hotdog" in JeanX.DailyActions:
                $ JeanX.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Back again so soon?",
                    "So you'd like another round?",
                    "You're really into this. . .",
                    "Are you sure that's all you want?"])
                ch_j "[Line]"
            else:
                $ JeanX.FaceChange("sexy", 1)
                $ JeanX.ArmPose = 2
                $ Line = renpy.random.choice(["Oooh, you want some of this?",
                    "So you'd like another round?",
                    "You're really into this. . .",
                    "You want another rub?"])
                ch_j "[Line]"
            $ Line = 0

    if Approval >= 2:
            #She's into it. . .
            if JeanX.Forced:
                $ JeanX.FaceChange("sad")
                $ JeanX.Statup("Obed", 80, 1)
                $ JeanX.Statup("Inbt", 60, 1)
                ch_j "Ok, fine."
            elif "no hotdog" in JeanX.DailyActions:
                ch_j "It was fun enough. . ."
            else:
                $ JeanX.FaceChange("sexy", 1)
                $ JeanX.Statup("Love", 80, 1)
                $ JeanX.Statup("Inbt", 50, 2)
                $ Line = renpy.random.choice(["Well, sure, let me give it a rub.",
                    "Very well.",
                    "Nice!",
                    "I guess we could do that.",
                    "Ok, let me. . .",
                    "Heh, ok, ok."])
                ch_j "[Line]"
                $ Line = 0
            $ JeanX.Statup("Obed", 60, 1)
            $ JeanX.Statup("Inbt", 70, 2)
            jump Jean_HotdogPrep

    else:
            #She's not into it, but maybe. . .
            $ JeanX.FaceChange("angry")
            if "no hotdog" in JeanX.RecentActions:
                ch_j "I don't repeat myself."
            elif JeanX.Taboo and "tabno" in JeanX.DailyActions and "no hotdog" in JeanX.DailyActions:
                ch_j "I just told you. . .not in such an exposed location."
            elif "no hotdog" in JeanX.DailyActions:
                ch_j "I'm believe I just told you \"no,\" [JeanX.Petname]."
            elif JeanX.Taboo and "tabno" in JeanX.DailyActions:
                ch_j "I'm not comfortable with that. . ."
            elif not JeanX.Hotdog:
                $ JeanX.FaceChange("bemused")
                ch_j "Hmm, that could be amusing, [JeanX.Petname]. . ."
            else:
                $ JeanX.FaceChange("bemused")
                ch_j "I don't think that would be appropriate. . ."
            menu:
                extend ""
                "Sorry, never mind." if "no hotdog" in JeanX.DailyActions:
                    $ JeanX.FaceChange("bemused")
                    ch_j "So long as you don't push it."
                    return
                "Maybe later?" if "no hotdog" not in JeanX.DailyActions:
                    $ JeanX.FaceChange("sexy")
                    ch_j "I guess eventually. . ."
                    $ JeanX.Statup("Love", 80, 1)
                    $ JeanX.Statup("Inbt", 50, 1)
                    if JeanX.Taboo:
                        $ JeanX.RecentActions.append("tabno")
                        $ JeanX.DailyActions.append("tabno")
                    $ JeanX.RecentActions.append("no hotdog")
                    $ JeanX.DailyActions.append("no hotdog")
                    return
                "You might like it. . .":
                    if Approval:
                        $ JeanX.FaceChange("sexy")
                        $ JeanX.Statup("Obed", 60, 2)
                        $ JeanX.Statup("Inbt", 50, 2)
                        $ Line = renpy.random.choice(["Yeah, probably. . .",
                                "I guess. . .",
                                "Good point. . ."])
                        ch_j "[Line]"
                        $ Line = 0
                        jump Jean_HotdogPrep
                    else:
                        pass

                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(JeanX, 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                    if Approval > 1 or (Approval and JeanX.Forced):
                        $ JeanX.FaceChange("confused")
                        $ JeanX.Statup("Love", 70, -2, 1)
                        $ JeanX.Statup("Love", 200, -2)
                        ch_j ". . ."
                        ch_j ". . . fine."
                        $ JeanX.Statup("Obed", 80, 4)
                        $ JeanX.Statup("Inbt", 60, 2)
                        $ JeanX.Forced = 1
                        jump Jean_HotdogPrep
                    else:
                        $ JeanX.Statup("Love", 200, -10)
                        $ JeanX.RecentActions.append("angry")
                        $ JeanX.DailyActions.append("angry")

    #She refused all offers.
    $ JeanX.ArmPose = 1

    if "no hotdog" in JeanX.DailyActions:
        ch_j "What did I tell you?"
        $ JeanX.RecentActions.append("angry")
        $ JeanX.DailyActions.append("angry")
    if JeanX.Forced:
        $ JeanX.FaceChange("angry", 1)
        ch_j "There's no point trying."
        $ JeanX.Statup("Lust", 200, 5)
        if JeanX.Love > 300:
                $ JeanX.Statup("Love", 70, -1)
        $ JeanX.Statup("Obed", 50, -1)
        $ JeanX.RecentActions.append("angry")
        $ JeanX.DailyActions.append("angry")
    elif JeanX.Taboo:                             # she refuses and this is too public a place for her
        $ JeanX.FaceChange("angry", 1)
        $ JeanX.RecentActions.append("tabno")
        $ JeanX.DailyActions.append("tabno")
        ch_j "This area is a bit too exposed for that sort of thing. . ."
        $ JeanX.Statup("Lust", 200, 5)
        $ JeanX.Statup("Obed", 50, -3)
    elif JeanX.Hotdog:
        $ JeanX.FaceChange("sad")
        ch_j "Not anymore."
    else:
        $ JeanX.FaceChange("normal", 1)
        ch_j "No thanks."
    $ JeanX.RecentActions.append("no hotdog")
    $ JeanX.DailyActions.append("no hotdog")
    $ temp_modifier = 0
    return

label Jean_Hotdog_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(JeanX)
        call Jean_Sex_Launch("hotdog")
        if Speed >= 4:
            $ Speed = 2
#            call Speed_Shift(2)
        $ JeanX.LustFace()
        $ Player.Cock = "out"
        $ Player.Sprite = 1
        $ Trigger = "hotdog"

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass
                        "Keep going. . . (locked)" if not Speed:
                                    pass

                        "Start moving? . ." if not Speed:
                                    $ Speed = 1
#                                    call Speed_Shift(1)
                        "Speed up. . ." if 0 < Speed < 3:
                                    $ Speed += 1
#                                    call Speed_Shift(Speed+1)
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 3:
                                    pass

                        "Slow Down. . ." if Speed:
                                    $ Speed -= 1
#                                    call Speed_Shift(Speed-1)
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(JeanX)
                                    $ Cnt += 1
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
                                            if JeanX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ JeanX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Shift primary action":
                                            if JeanX.Action and MultiAction:
                                                    menu:
                                                        "How about sex?":
                                                            $ Situation = "shift"
                                                            call Jean_HotdogAfter
                                                            call Jean_Sex_P
                                                        "Just stick it in her pussy [[without asking].":
                                                            $ Situation = "auto"
                                                            call Jean_HotdogAfter
                                                            call Jean_Sex_P
                                                        "How about anal?":
                                                            $ Situation = "shift"
                                                            call Jean_HotdogAfter
                                                            call Jean_Sex_A
                                                        "Just stick it in her ass [[without asking].":
                                                            $ Situation = "auto"
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
                                            "Ask [JeanX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(JeanX)
                                            "Ask [JeanX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(JeanX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(JeanX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Jean_Hotdog_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jean_Hotdog_Cycle
                                            "Never mind":
                                                        jump Jean_Hotdog_Cycle
                                    "Just take a look at her.":
                                            $ Player.Cock = 0
                                            $ Speed = 0

                                    "Show her feet" if not ShowFeet and JeanX.Pose == "doggy":
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and JeanX.Pose == "doggy":
                                            $ ShowFeet = 0

                                    "Undress [JeanX.Name]":
                                            call Girl_Undress(JeanX)
                                    "Clean up [JeanX.Name] (locked)" if not JeanX.Spunk:
                                            pass
                                    "Clean up [JeanX.Name]" if JeanX.Spunk:
                                            call Girl_Cleanup(JeanX,"ask")
                                    "Never mind":
                                            jump Jean_Hotdog_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Jean_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Jean_HotdogAfter
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Jean_Sex_Reset
                                    $ Line = 0
                                    jump Jean_HotdogAfter
        #End menu (if Line)

        call Shift_Focus(JeanX)
        call Sex_Dialog(JeanX,Partner)

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JeanX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JeanX)
                            if "angry" in JeanX.RecentActions:
                                call Jean_Sex_Reset
                                return
                            $ JeanX.Statup("Lust", 200, 5)
                            if 100 > JeanX.Lust >= 70 and JeanX.OCount < 2:
                                    $ JeanX.RecentActions.append("unsatisfied")
                                    $ JeanX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jean_HotdogAfter
                            $ Line = "came"

                    if JeanX.Lust >= 100:
                            #If you're still going at it and Jean can cum
                            call Girl_Cumming(JeanX)
                            if Situation == "shift" or "angry" in JeanX.RecentActions:
                                jump Jean_HotdogAfter

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Jean_HotdogAfter
                            elif "unsatisfied" in JeanX.RecentActions:
                                #And Jean is unsatisfied,
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ Line = "You get back into it"
                                        jump Jean_Hotdog_Cycle
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Jean_HotdogAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Jean_HotdogAfter
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if JeanX.SEXP >= 100 or ApprovalCheck(JeanX, 1200, "LO"):
            pass
        elif Cnt == (5 + JeanX.Hotdog):
                    $ JeanX.Brows = "confused"
                    ch_j "'bout done there?"
        elif Cnt == (10 + JeanX.Hotdog):
                    $ JeanX.Brows = "angry"
                    menu:
                        ch_j "Well this is not fun."
                        "How about a BJ?" if JeanX.Action and MultiAction:
                                $ Situation = "shift"
                                call Jean_HotdogAfter
                                call Jean_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ Cnt += 1
                                jump Jean_Hotdog_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Jean_Sex_Reset
                                $ Situation = "shift"
                                jump Jean_HotdogAfter
                        "No, get back down there.":
                                if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                                    $ JeanX.Statup("Love", 200, -5)
                                    $ JeanX.Statup("Obed", 50, 3)
                                    $ JeanX.Statup("Obed", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    $ JeanX.FaceChange("angry", 1)
                                    call Jean_Sex_Reset
                                    "She scowls at you and pulls away."
                                    ch_j "Don't overestimate yourself."
                                    $ JeanX.Statup("Love", 50, -3, 1)
                                    $ JeanX.Statup("Love", 80, -4, 1)
                                    $ JeanX.Statup("Obed", 30, -1, 1)
                                    $ JeanX.Statup("Obed", 50, -1, 1)
                                    $ JeanX.RecentActions.append("angry")
                                    $ JeanX.DailyActions.append("angry")
                                    jump Jean_HotdogAfter
        #End Count check

        call Escalation(JeanX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(JeanX,10) #"You might want to wrap this up, it's getting late."
        elif Round == 5:
                call Sex_Basic_Dialog(JeanX,5)   #"Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ JeanX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(JeanX,"done")   #"Ok, [Girl.Petname], that's enough of that for now."
