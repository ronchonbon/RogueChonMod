label Rogue_SexAct(Act = 0):
        if AloneCheck(character) and character.Taboo == 20:
                $ character.Taboo = 0
                $ Taboo = 0
        call Shift_Focus(character)
        if Act == "SkipTo":
                $ renpy.pop_call() #causes it to skip past the Trigger Swap
                $ renpy.pop_call() #causes it to skip past the cycle you were in before
                #$ renpy.pop_call() #causes it to skip past the sex menu you were in before that
                call SkipTo(character)
        elif Act == "switch":
                $ renpy.pop_call() #causes it to skip past call here from Sex_Menu_Threesome
                #$ renpy.pop_call() #causes it to skip past call to Sex_Menu_Threesome
                # drops through to sex menu
        elif Act == "masturbate":
                call Rogue_M_Prep
                if not Situation:
                        return
        elif Act == "lesbian":
                call Les_Prep(character)
                if not Situation:
                        return
        elif Act == "kissing":
                call KissPrep(character)
                if not Situation:
                        return
        elif Act == "breasts":
                call Rogue_Fondle_Breasts
                if not Situation:
                        return
        elif Act == "blow":
                call Rogue_BJ_Prep
                if not Situation:
                        return
        elif Act == "hand":
                call Rogue_HJ_Prep
                if not Situation:
                        return
        elif Act == "sex":
                call sex_prep(character)
                if not Situation:
                        return

        return

label Rogue_Masturbate: #(Situation = Situation):
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(character)
    if character.Mast:
        $ temp_modifier += 10
    if character.SEXP >= 50:
        $ temp_modifier += 25
    elif character.SEXP >= 30:
        $ temp_modifier += 15
    elif character.SEXP >= 15:
        $ temp_modifier += 5
    if character.Lust >= 90:
        $ temp_modifier += 20
    elif character.Lust >= 75:
        $ temp_modifier += 5
    if "exhibitionist" in character.Traits:
        $ temp_modifier += (3*Taboo)
    if character in Player.Harem or "sex friend" in character.Petnames:
        $ temp_modifier += 10
    elif "ex" in character.Traits:
        $ temp_modifier -= 40
    if character.ForcedCount and not character.Forced:
        $ temp_modifier -= 5 * character.ForcedCount

    $ Approval = ApprovalCheck(character, 1200, TabM = 2) # 120, 135, 150, Taboo -80(200)

    $ character.DrainWord("unseen",1,0) #She sees you, so remove unseens

    if Situation == "join":       # This triggers if you ask to join in
                if Approval > 1 or (Approval and character.Lust >= 50):
                    $ Player.AddWord(1,"join")
                    menu:
                        extend ""
                        "Would you like some help? I could lend some helping hands. . ."  if Player.Semen and character.Action:
                                $ character.Statup("Love", 90, 1)
                                $ character.Statup("Obed", 50, 2)
                                $ character.FaceChange("sexy")
                                ch_r "Well, [character.Petname], I suppose I could use some help with these. . ."
                                $ character.Statup("Obed", 70, 2)
                                $ character.Statup("Inbt", 70, 1)
                                $ Trigger2 = "fondle breasts"
                                $ character.Mast += 1
                                jump Rogue_M_Cycle
                        "Would you like some help? I could. . . up to you, I guess." if Player.Semen and character.Action:
                                $ character.Statup("Love", 70, 2)
                                $ character.Statup("Love", 90, 1)
                                $ character.FaceChange("sexy")
                                ch_r "Well, [character.Petname], I suppose you could help me with these. . ."
                                $ character.Statup("Obed", 70, 2)
                                $ character.Statup("Inbt", 70, 1)
                                $ D20 = renpy.random.randint(1, 20)
                                if D20 > 10:
                                    $ Trigger2 = "fondle breasts"
                                else:
                                    $ Trigger2 = "suck breasts"
                                $ character.Mast += 1
                                jump Rogue_M_Cycle
                        "Why don't we take care of each other?" if Player.Semen and character.Action:
                                $ character.FaceChange("sexy")
                                ch_r "Well what did you have in mind?"
                                $ renpy.pop_call()          #removes the call to this label
                                return                      #returns to sexmenu=
                        "You look like you have things well in hand. . .":
                                if character.Lust >= 50:
                                    $ character.Statup("Love", 70, 2)
                                    $ character.Statup("Love", 90, 1)
                                    $ character.FaceChange("sexy")
                                    ch_r "Well, [character.Petname], I suppose I do at that . ."
                                    $ character.Statup("Obed", 80, 3)
                                    $ character.Statup("Inbt", 80, 5)
                                    jump Rogue_M_Cycle
                                elif ApprovalCheck(character, 1000):
                                    $ character.FaceChange("sly")
                                    ch_r "Well I did, but I think I've got it taken care of for now. . ."
                                else:
                                    $ character.FaceChange("angry")
                                    ch_r "Well I did, but now you've blown the mood."

                #else: You've failed all checks so she kicks you out.
                $ character.ArmPose = 1
                $ character.OutfitChange(Changed=0)
                $ character.Action -= 1
                $ Player.Statup("Focus", 50, 30)
                call Checkout(1)
                $ Line = 0
                $ Situation = 0
                $ renpy.pop_call()          #removes the call to this label
                if Approval:
                        $ character.FaceChange("bemused", 2)
                        if bg_current == "bg rogue":
                            ch_r "So what did you come over for anyway, [character.Petname]?"
                        else:
                            ch_r "So . . . fancy bumping into you here, [character.Petname]. . ."
                        $ character.Blush = 1
                else:
                        $ character.Statup("Love", 200, -5)
                        $ character.FaceChange("angry")
                        $ character.RecentActions.append("angry")
                        $ character.DailyActions.append("angry")
                        if bg_current == "bg rogue":
                            ch_r "Well if you don't mind, I'd kind of appreciate you getting out of here. Maybe knock next time?"
                            "[character.Name] kicks you out of her room."
                            $ renpy.pop_call()
                            jump Campus_Map
                        else:
                            ch_r "Well if you don't mind, I'm getting out of here. Maybe knock next time?"
                            call Remove_Girl(character)
                return                      #returns to sexmenu, which returns to original
    #End of "Join" option



    if Situation == character:                                                                  #Rogue auto-starts
                if Approval > 2:                                                      # fix, add rogue auto stuff here
                        if character.PantsNum() == 5:
                            "[character.Name]'s hand snakes down her body, and hikes up her skirt."
                            $ character.Upskirt = 1
                        elif character.PantsNum() > 6:
                            "[character.Name] slides her hand down her body and into her jeans."
                        elif character.HoseNum() >= 5:
                            "[character.Name]'s hand slides down her body and under her [character.Hose]."
                        elif character.Panties:
                            "[character.Name]'s hand slides down her body and under her [character.Panties]."
                        else:
                            "[character.Name]'s hand slides down her body and begins to caress her pussy."
                        $ character.SeenPanties = 1
                        "She starts to slowly rub herself."
                        call Rogue_First_Bottomless
                        menu:
                            "What do you do?"
                            "Nothing.":
                                    $ character.Statup("Inbt", 80, 3)
                                    $ character.Statup("Inbt", 60, 2)
                                    "[character.Name] begins to masturbate."
                            "Go for it.":
                                    $ character.FaceChange("sexy, 1")
                                    $ character.Statup("Inbt", 80, 3)
                                    ch_p "That is so sexy, [character.Pet]."
                                    $ character.NameCheck() #checks reaction to petname
                                    "You lean back and enjoy the show."
                                    $ character.Statup("Love", 80, 1)
                                    $ character.Statup("Obed", 90, 1)
                                    $ character.Statup("Obed", 50, 2)
                            "Ask her to stop.":
                                    $ character.FaceChange("surprised")
                                    $ character.Statup("Inbt", 70, 1)
                                    ch_p "Let's not do that right now, [character.Pet]."
                                    $ character.NameCheck() #checks reaction to petname
                                    "[character.Name] pulls her hands away from herself."
                                    $ character.OutfitChange(Changed=0)
                                    $ character.Statup("Obed", 90, 1)
                                    $ character.Statup("Obed", 50, 1)
                                    $ character.Statup("Obed", 30, 2)
                                    return
                        jump Rogue_M_Prep
                else:
                        $ temp_modifier = 0                               # fix, add rogue auto stuff here
                        $ Trigger2 = 0
                return
    #End if Rogue intitiates this action

    #first time
    if not character.Mast:
            $ character.FaceChange("surprised", 1)
            $ character.Mouth = "kiss"
            ch_r "You want me to get myself off, while you watch?"
            if character.Forced:
                $ character.FaceChange("sad")
                ch_r "So you just want to watch then?"


    #First time dialog
    if not character.Mast and Approval:
            if character.Forced:
                $ character.FaceChange("sad")
                $ character.Statup("Love", 70, -3, 1)
                $ character.Statup("Love", 20, -2, 1)
            elif character.Love >= (character.Obed + character.Inbt):
                $ character.FaceChange("sexy")
                $ character.Brows = "sad"
                $ character.Mouth = "smile"
                ch_r "Since my love life's been a bit. . . limited, I've gotten pretty good at this."
            elif character.Obed >= character.Inbt:
                $ character.FaceChange("normal")
                ch_r "If that's what you want, [character.Petname]. . ."
            else: # Uninhibited
                $ character.FaceChange("sad")
                $ character.Mouth = "smile"
                ch_r "I guess it could be fun with you watching. . ."


    #Second time+ initial dialog
    elif Approval:
            if character.Forced:
                $ character.FaceChange("sad")
                $ character.Statup("Love", 70, -3, 1)
                $ character.Statup("Love", 20, -2, 1)
                ch_r "You want to watch me again?"
            elif Approval and "masturbation" in character.RecentActions:
                $ character.FaceChange("sexy", 1)
                ch_r "I guess I have a bit more in me. . ."
                jump Rogue_M_Prep
            elif Approval and "masturbation" in character.DailyActions:
                $ character.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["You enjoyed the show?",
                    "Didn't get enough earlier?",
                    "It is nice to have an audience. . ."])
                ch_r "[Line]"
            elif character.Mast < 3:
                $ character.FaceChange("sexy", 1)
                $ character.Brows = "confused"
                ch_r "You like to watch, huh?"
            else:
                $ character.FaceChange("sexy", 1)
                $ character.ArmPose = 2
                $ Line = renpy.random.choice(["You sure do like to watch.",
                    "So you'd like me to go again?",
                    "You want to watch some more?",
                    "You want me ta diddle myself?"])
                ch_r "[Line]"
                $ Line = 0
    #End second time+ initial dialog

    #If she's into it. . .
    if Approval >= 2:
            if character.Forced:
                $ character.FaceChange("sad")
                $ character.Statup("Obed", 90, 1)
                $ character.Statup("Inbt", 60, 1)
                ch_r "I suppose, let me get comfortable. . ."
            else:
                $ character.FaceChange("sexy", 1)
                $ character.Statup("Love", 90, 1)
                $ character.Statup("Inbt", 50, 3)
                $ Line = renpy.random.choice(["Well. . . ok.",
                    "I suppose it would help to have something nice to look at. . .",
                    "I've kind of needed this anyways. . .",
                    "Sure!",
                    "I guess I could. . . give it a go.",
                    "Heh, ok, ok."])
                ch_r "[Line]"
                $ Line = 0
            $ character.Statup("Obed", 20, 1)
            $ character.Statup("Obed", 60, 1)
            $ character.Statup("Inbt", 70, 2)
            jump Rogue_M_Prep

    #If she's not into it, but maybe. . .
    else:
        menu:
            ch_r "That's. . . a little intimate, [character.Petname]."
            "Maybe later?":
                    $ character.FaceChange("sexy", 1)
                    if character.Lust > 50:
                        ch_r "Well, definitely later. . . but I'll have to think about inviting you."
                    else:
                        ch_r "Hmm, maybe. . . I'll let you know."
                    $ character.Statup("Love", 80, 2)
                    $ character.Statup("Inbt", 70, 2)
                    return
            "You look like you could use it. . .":
                    if Approval:
                        $ character.FaceChange("sexy")
                        $ character.Statup("Obed", 90, 2)
                        $ character.Statup("Obed", 50, 2)
                        $ character.Statup("Inbt", 70, 3)
                        $ character.Statup("Inbt", 40, 2)
                        $ Line = renpy.random.choice(["Well. . . ok.",
                            "I suppose it would help to have something nice to look at. . .",
                            "I've kind of needed this anyways. . .",
                            "Sure!",
                            "I guess I could. . . give it a go.",
                            "Heh, ok, ok."])
                        ch_r "[Line]"
                        $ Line = 0
                        jump Rogue_M_Prep

            "Just get at it already.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(character, 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                    if Approval > 1 or (Approval and character.Forced):
                        $ character.FaceChange("sad")
                        $ character.Statup("Love", 70, -5, 1)
                        $ character.Statup("Love", 200, -5)
                        ch_r "Ok, fine. I'll give it a try."
                        $ character.Statup("Obed", 80, 4)
                        $ character.Statup("Inbt", 80, 1)
                        $ character.Statup("Inbt", 60, 3)
                        $ character.Forced = 1
                        jump Rogue_M_Prep
                    else:
                        $ character.Statup("Love", 200, -20)
                        $ character.RecentActions.append("angry")
                        $ character.DailyActions.append("angry")
    # end of asking her to do it

    #She refused all offers.
    $ character.ArmPose = 1
    if character.Forced:
            $ character.FaceChange("angry", 1)
            ch_r "I'm not doing something so. . . intimate with you watching."
            $ character.Statup("Lust", 90, 5)
            if character.Love > 300:
                $ character.Statup("Love", 70, -2)
            $ character.Statup("Obed", 50, -2)
            $ character.RecentActions.append("angry")
            $ character.DailyActions.append("angry")
            $ character.RecentActions.append("no masturbation")
            $ character.DailyActions.append("no masturbation")
            return
    elif Taboo:                             # she refuses and this is too public a place for her
            $ character.FaceChange("angry", 1)
            $ character.DailyActions.append("tabno")
            ch_r "I can't do that here!"
            $ character.Statup("Lust", 90, 5)
            $ character.Statup("Obed", 50, -3)
            return
    elif character.Mast:
            $ character.FaceChange("sad")
            ch_r "Nope, not anymore, you'll have to go back to Internet porn."
    else:
            $ character.FaceChange("normal", 1)
            ch_r "Heh, no, I'm not doing that."
    $ character.RecentActions.append("no masturbation")
    $ character.DailyActions.append("no masturbation")
    $ temp_modifier = 0
    return

label Rogue_M_Prep:
    $ character.Upskirt = 1
    $ character.PantiesDown = 1
    call Rogue_First_Bottomless(1)
    call Set_The_Scene(Dress=0)

    #if she hasn't seen you yet. . .
    if "unseen" in character.RecentActions:
            $ character.FaceChange("sexy")
            $ character.Eyes = "closed"
            $ character.ArmPose = 2
            "You see [character.Name] leaning back, masturbating. You don't think she's noticed you yet."
    else:
            $ character.FaceChange("sexy")
            $ character.ArmPose = 2
            "[character.Name] lays back and starts to toy with herself."
            if not character.Mast:#First time
                    if character.Forced:
                        $ character.Statup("Love", 90, -20)
                        $ character.Statup("Obed", 70, 45)
                        $ character.Statup("Inbt", 80, 35)
                    else:
                        $ character.Statup("Love", 90, 15)
                        $ character.Statup("Obed", 70, 35)
                        $ character.Statup("Inbt", 80, 40)


    $ Trigger = "masturbation"
    if not Trigger3:
        $ Trigger3 = "fondle pussy"

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    if Taboo:
        $ character.DrainWord("tabno")
    $ character.DrainWord("no masturbation")
    $ character.RecentActions.append("masturbation")
    $ character.DailyActions.append("masturbation")

label Rogue_M_Cycle:
    if Situation == "join":
        # resets the call made to this option
        $ renpy.pop_call()
        $ Situation = 0

    while Round > 0:
        call reset_position(character, trigger = "masturbation")
        call Shift_Focus(character)
        $ character.LustFace
        if "unseen" in character.RecentActions:
                $ character.Eyes = "closed"

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep Watching.":
                                pass

                        "[character.Name]. . .[[jump in]" if "unseen" not in character.RecentActions and "join" not in Player.RecentActions and character.Loc == bg_current:
                                "[character.Name] slows what she's doing with a sly grin."
                                ch_r "Yeah, did you want something, [character.Petname]?"
                                $ Situation = "join"
                                call Rogue_Masturbate
                        "\"Ahem. . .\"" if "unseen" in character.RecentActions:
                                jump Rogue_M_Interupted

                        "Start jack'in it." if Trigger2 != "jackin":
                                call Jackin(character)
                        "Stop jack'in it." if Trigger2 == "jackin":
                                $ Trigger2 = 0

                        "Slap her ass" if character.Loc == bg_current:
                                if "unseen" in character.RecentActions:
                                        "You smack [character.Name] firmly on the ass!"
                                        jump Rogue_M_Interupted
                                else:
                                        call Slap_Ass(character)
                                        $ Cnt += 1
                                        $ Round -= 1
                                        jump Rogue_M_Cycle

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
                                    "Offhand action" if character.Loc == bg_current:
                                            if character.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ character.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(character,"tired")

                                    "Threesome actions (locked)" if not Partner or "unseen" in character.RecentActions or character.Loc == bg_current:
                                        pass
                                    "Threesome actions" if character.Loc == bg_current and Partner and "unseen" not in character.RecentActions:
                                        menu:
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(character)
                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(character)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Rogue_M_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Rogue_M_Cycle
                                            "Never mind":
                                                        jump Rogue_M_Cycle

                                    "Show her feet" if not ShowFeet and (character.Pose == "doggy" or character.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (character.Pose == "doggy" or character.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [character.Name]":
                                            if "unseen" in character.RecentActions:
                                                    ch_p "Oh, yeah, take it off. . ."
                                                    jump Rogue_M_Interupted
                                            else:
                                                    call Girl_Undress(character)
                                    "Clean up [character.Name] (locked)" if not character.Spunk:
                                            pass
                                    "Clean up [character.Name]" if character.Spunk:
                                            if "unseen" in character.RecentActions:
                                                    ch_p "You've got a little something on you. . ."
                                                    jump Rogue_M_Interupted
                                            else:
                                                    call Girl_Cleanup(character,"ask")
                                    "Never mind":
                                            jump Rogue_M_Cycle

                        "Back to Sex Menu" if MultiAction and character.Loc == bg_current:
                                    ch_p "Let's try something else."
                                    call reset_position(character)
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Rogue_M_Interupted
                        "End Scene" if not MultiAction or character.Loc != bg_current:
                                    ch_p "Let's stop for now."
                                    call reset_position(character)
                                    $ Line = 0
                                    jump Rogue_M_Interupted
        #End menu (if Line)

        call Shift_Focus(character)
        call Sex_Dialog(character,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up

        if Player.Focus >= 100 or character.Lust >= 100:
                    #If you can cum:
                    if Player.Focus >= 100:
                        if "unseen" not in character.RecentActions:
                            #if she knows you're there
                            call Player_Cumming(character)
                            if "angry" in character.RecentActions:
                                call reset_position(character)
                                return
                            $ character.Statup("Lust", 200, 5)
                            if 100 > character.Lust >= 70 and character.OCount < 2:
                                $ character.RecentActions.append("unsatisfied")
                                $ character.DailyActions.append("unsatisfied")
                            $ Line = "came"
                        else: #If she wasn't aware you were there
                            "You grunt and try to hold it in."
                            $ Player.Focus = 95
                            if character.Loc == bg_current:
                                    jump Rogue_M_Interupted

                    #If Rogue can cum
                    if character.Lust >= 100:
                        call Girl_Cumming(character)
                        if character.Loc == bg_current:
                                jump Rogue_M_Interupted

                    if Line == "came":
                        $ Line = 0
                        if not Player.Semen:
                            "You're emptied out, you should probably take a break."
                            $ Trigger2 = 0 if Trigger2 == "jackin" else Trigger2


                        if "unsatisfied" in character.RecentActions:#And Rogue is unsatisfied,
                            "[character.Name] still seems a bit unsatisfied with the experience."
                            menu:
                                "Let her keep going?"
                                "Yes, keep going for a bit.":
                                    $ Line = "You let her get back into it"
                                    jump Rogue_M_Cycle
                                "No, I'm done.":
                                    "You ask her to stop."
                                    return
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        if "unseen" in character.RecentActions:
                if Round == 10:
                    "It's getting a bit late, [character.Name] will probably be wrapping up soon."
                elif Round == 5:
                    "She's definitely going to stop soon."
        else:
                if character.Loc == bg_current:
                        call Escalation(character) #sees if she wants to escalate things

                if Round == 10:
                    ch_r "We might want to wrap this up, it's getting late."
                    $ character.Lust += 10
                elif Round == 5:
                    ch_r "Seriously, it'll be time to stop soon."
                    $ character.Lust += 25

    #Round = 0 loop breaks
    $ character.FaceChange("bemused", 0)
    $ Line = 0
    if "unseen" not in character.RecentActions:
        ch_r "Ok, [character.Petname], that's enough of that for now."

label Rogue_M_Interupted:

    # If she hasn't noticed you're there before cumming
    if "unseen" in character.RecentActions:
                $ character.FaceChange("surprised", 1)
                "[character.Name] stops what she's doing with a start, eyes wide."
                call Rogue_First_Bottomless(1)
                $ character.FaceChange("surprised", 1)

                #If you've been jacking it
                if Trigger2 == "jackin":
                        ch_r "H- how long you been stand'in there, [character.Petname]?"
                        $ character.Eyes = "down"
                        menu:
                            ch_r "And why is your cock out like that?!"
                            "Long enough, it was an excellent show.":
                                    $ character.FaceChange("sexy")
                                    $ character.Statup("Obed", 50, 3)
                                    $ character.Statup("Obed", 70, 2)
                                    ch_r "Well, I imagine it was. . ."
                                    if character.Love >= 800 or character.Obed >= 500 or character.Inbt >= 500:
                                        $ temp_modifier += 10
                                        $ character.Statup("Lust", 90, 5)
                                        ch_r "And the view from this angle ain't so bad either. . ."

                            "I. . . just got here?":
                                    $ character.FaceChange("angry")
                                    $ character.Statup("Love", 70, 2)
                                    $ character.Statup("Love", 90, 1)
                                    $ character.Statup("Obed", 50, 2)
                                    $ character.Statup("Obed", 70, 2)
                                    "She looks pointedly at your cock,"
                                    ch_r "A likely story . . ."
                                    if character.Love >= 800 or character.Obed >= 500 or character.Inbt >= 500:
                                            $ temp_modifier += 10
                                            $ character.Statup("Lust", 90, 5)
                                            $ character.FaceChange("bemused", 1)
                                            ch_r "Still, can't blame a fella for take'in inspirations."
                                    else:
                                            $ temp_modifier -= 10
                                            $ character.Statup("Lust", 200, -5)
                        call Seen_First_Peen(character,Partner)
                        ch_r "Hmm. . ."

                #you haven't been jacking it
                else:
                        ch_r "H- how long you been stand'in there, [character.Petname]?"
                        menu:
                            extend ""
                            "Long enough.":
                                    $ character.FaceChange("sexy", 1)
                                    $ character.Statup("Obed", 50, 3)
                                    $ character.Statup("Obed", 70, 2)
                                    ch_r "Well I hope you got a good show out of it. . ."
                            "I just got here.":
                                    $ character.FaceChange("bemused", 1)
                                    $ character.Statup("Love", 70, 2)
                                    $ character.Statup("Love", 90, 1)
                                    ch_r "A likely story . . ."
                                    $ character.Statup("Obed", 50, 2)
                                    $ character.Statup("Obed", 70, 2)

                $ character.DrainWord("unseen",1,0) #She sees you, so remove unseens
                $ character.Mast += 1
                if Round <= 10:
                    ch_r "It's getting too late to do much about it right now though."
                    return
                $ Situation = "join"
                call Rogue_Masturbate
                "error: report this if you see it."
                return #should be redundant
    #End Unseen

    #else, if She's seen you already
    $ character.Action -= 1
    $ character.Mast += 1

    if Partner == EmmaX:
        call Partner_Like(character,4)
    else:
        call Partner_Like(character,3)
    call Checkout
    if Situation == "shift":
        $ Situation = 0
        return
    $ Situation = 0

    if character.Loc != bg_current:
        return

    if Round <= 10:
            ch_r "I need to take a little break here, [character.Petname]."
            return
    $ character.FaceChange("sexy", 1)
    if character.Lust < 20:
        ch_r "That really worked for me, [character.Petname]. How about you?"
    else:
        ch_r "Yeah, what did you want?"
    menu:
        extend ""
        "Well, I have something you could take care of. . ." if Player.Semen and character.Action:
                $ Situation = "shift"
                return
        "You could just keep going. . ." if Player.Semen:
                $ character.FaceChange("sly")
                if character.Action and Round >= 10:
                    ch_r "Well, alright. . ."
                    jump Rogue_M_Cycle
                else:
                    ch_r "I'm kinda worn out, maybe time for a break. . ."
        "I'm good here. [[Stop]":
                if character.Love < 800 and character.Inbt < 500 and character.Obed < 500:
                    $ character.OutfitChange(Changed=0)
                $ character.FaceChange("normal")
                $ character.Brows = "confused"
                ch_r "Well. . . ok then. . ."
                $ character.Brows = "normal"
        "You should probably stop for now." if character.Lust > 30:
                $ character.FaceChange("angry")
                ch_r "Well if you say so."
    return

label Rogue_Sex_P:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(character)
    call sex_set_modifier(character, action)


    $ Approval = ApprovalCheck(character, 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)

    if Situation == "auto":
        $ character.Pose = "doggy"
        call Rogue_Sex_Launch("sex")
        if character.PantsNum() == 5:
            "You press up against [character.Name]'s backside, sliding her skirt up as you go."
            $ character.Upskirt = 1
        elif character.PantsNum() > 6:
            "You press up against [character.Name]'s backside, sliding her pants down as you do."
            $ character.Legs = 0
        else:
            "You press up against [character.Name]'s backside."
        $ character.SeenPanties = 1
        "You rub the tip of your cock against her moist slit."
        $ character.FaceChange("surprised", 1)

        if (character.Sex and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
            "[character.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            $ character.FaceChange("sexy")
            $ character.Statup("Obed", 70, 3)
            $ character.Statup("Inbt", 50, 3)
            $ character.Statup("Inbt", 70, 1)
            ch_r "Ok, [character.Petname], let's do this."
            call sex_prep(character)
        else:                                                                                                            #she's questioning it
            $ character.Brows = "angry"
            menu:
                ch_r "Hey, what do you think you're doing back there?!"
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ character.FaceChange("sexy", 1)
                        $ character.Statup("Obed", 70, 3)
                        $ character.Statup("Inbt", 50, 3)
                        $ character.Statup("Inbt", 70, 1)
                        ch_r "Well, since you're be'in so nice about it, I guess we can give it a go. . ."
                        call sex_prep(character)
                    "You pull back before you really get it in."
                    $ character.FaceChange("bemused", 1)
                    if character.Sex:
                        ch_r "Well ok, [character.Petname], no harm done. Just give me a little warning next time."
                    else:
                        ch_r "Well ok, [character.Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."
                "Just fucking.":
                    $ character.Statup("Love", 80, -10, 1)
                    $ character.Statup("Love", 200, -10)
                    "You press inside some more."
                    $ character.Statup("Obed", 70, 3)
                    $ character.Statup("Inbt", 50, 3)
                    if not ApprovalCheck(character, 700, "O", TabM=1):   #Checks if Obed is 700+
                        $ character.FaceChange("angry")
                        "[character.Name] shoves you away and slaps you in the face."
                        ch_r "Jackass!"
                        ch_r "If that's how you want to treat me, we're done here!"
                        $ character.Statup("Love", 50, -10, 1)
                        $ character.Statup("Obed", 50, 3)
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Rogue_Sex_Reset
                        $ character.RecentActions.append("angry")
                        $ character.DailyActions.append("angry")
                    else:
                        $ character.FaceChange("sad")
                        "[character.Name] doesn't seem to be into this, you're lucky she's so obedient."
                        call sex_prep(character)
        return


    if not character.Sex and "no sex" not in character.RecentActions:                           #first time
        $ character.FaceChange("surprised", 1)
        $ character.Mouth = "kiss"
        ch_r "So, you'd like to take this to the next level? Actual sex? . . ."
        if character.Forced:
            $ character.FaceChange("sad")
            ch_r "You'd really take it that far?"


    if not character.Sex and Approval:                                                  #First time dialog
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Love", 70, -30, 1)
            $ character.Statup("Love", 20, -20, 1)
        elif character.Love >= (character.Obed + character.Inbt):
            $ character.FaceChange("sexy")
            $ character.Brows = "sad"
            $ character.Mouth = "smile"
            ch_r "Well, I've never been able to do this before now, so this might be fun."
        elif character.Obed >= character.Inbt:
            $ character.FaceChange("normal")
            ch_r "If that's what you want, [character.Petname]. . ."
        elif character.Addict >= 50:
            $ character.FaceChange("manic", 1)
            ch_r "Well. . . I bet it would feel really good down there."
        else: # Uninhibited
            $ character.FaceChange("sad")
            $ character.Mouth = "smile"
            ch_r "Hmm, I've always wanted to try it. . ."

    elif Approval:                                                                       #Second time+ dialog
        $ character.FaceChange("sexy", 1)
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Love", 20, -2, 1)
            ch_r "That's really what you want?"
        elif not Taboo and "tabno" in character.DailyActions:
            ch_r "Well, at least you got us some privacy this time. . ."
        elif "sex" in character.RecentActions:
            ch_r "You want to go again? Ok."
            call sex_prep(character)
        elif "sex" in character.DailyActions:
            $ Line = renpy.random.choice(["Back again so soon?",
                "So you'd like another go?",
                "You can't stay away from this. . .",
                "Didn't get enough earlier?",
                "You're going to wear me out."])
            ch_r "[Line]"
        elif character.Sex < 3:
            $ character.Brows = "confused"
            $ character.Mouth = "kiss"
            ch_r "So you'd like another go?"
        else:
            $ Line = renpy.random.choice(["You want some of this action?",
                "So you'd like another go?",
                "You can't stay away from this. . .",
                "You want me to ride your pole?",
                "You wanna dip your wick?"])
            ch_r "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Obed", 90, 1)
            $ character.Statup("Inbt", 60, 1)
            ch_r "Ok, fine."
        elif "no sex" in character.DailyActions:
            ch_r "Ok, you've won me over on this one. . ."
        else:
            $ character.FaceChange("sexy", 1)
            $ character.Statup("Love", 90, 1)
            $ character.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, stick it in.",
                "Well. . . ok.",
                "Sure!",
                "I guess I could. . . stick it in.",
                "Hells yeah.",
                "Heh, ok, ok."])
            ch_r "[Line]"
            $ Line = 0
        $ character.Statup("Obed", 20, 1)
        $ character.Statup("Obed", 60, 1)
        $ character.Statup("Inbt", 70, 2)
        call sex_prep(character)

    else:                                                                               #She's not into it, but maybe. . .
        $ character.FaceChange("angry")
        if "no sex" in character.RecentActions:
            ch_r "I {i}just{/i} told you \"no,\" [character.Petname]."
        elif Taboo and "tabno" in character.DailyActions and "no sex" in character.DailyActions:
            ch_r "I already told you that I wouldn't bang you in public!"
        elif "no sex" in character.DailyActions:
            ch_r "I already told you \"no,\" [character.Petname]."
        elif Taboo and "tabno" in character.DailyActions:
            ch_r "I already told you this is too public!"
        elif not character.Sex:
            $ character.FaceChange("bemused")
            ch_r "I just don't think I'm ready yet, [character.Petname]. . ."
        else:
            $ character.FaceChange("bemused")
            ch_r "Not, right now [character.Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no sex" in character.DailyActions:
                $ character.FaceChange("bemused")
                ch_r "Yeah, ok, [character.Petname]."
                return
            "Maybe later?" if "no sex" not in character.DailyActions:
                $ character.FaceChange("sexy")
                ch_r "I'll give it some thought, [character.Petname]."
                $ character.Statup("Love", 80, 2)
                $ character.Statup("Inbt", 70, 2)
                if Taboo:
                    $ character.RecentActions.append("tabno")
                    $ character.DailyActions.append("tabno")
                $ character.RecentActions.append("no sex")
                $ character.DailyActions.append("no sex")
                return
            "I think you'd enjoy it as much as I would. . .":
                if Approval:
                    $ character.FaceChange("sexy")
                    $ character.Statup("Obed", 90, 2)
                    $ character.Statup("Obed", 50, 2)
                    $ character.Statup("Inbt", 70, 3)
                    $ character.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",
                        "I suppose. . .",
                        "You've got me there."])
                    ch_r "[Line]"
                    $ Line = 0
                    call sex_prep(character)
            "Bend over.":                                               # Pressured into it
                $ Approval = ApprovalCheck(character, 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
                if Approval > 1 or (Approval and character.Forced):
                    $ character.FaceChange("sad")
                    $ character.Statup("Love", 70, -5, 1)
                    $ character.Statup("Love", 200, -5)
                    ch_r "Ok, fine. If we're going to do this, stick it in already."
                    $ character.Statup("Obed", 80, 4)
                    $ character.Statup("Inbt", 80, 1)
                    $ character.Statup("Inbt", 60, 3)
                    $ character.Forced = 1
                    call sex_prep(character)
                else:
                    $ character.Statup("Love", 200, -20)
                    $ character.RecentActions.append("angry")
                    $ character.DailyActions.append("angry")

    #She refused all offers.
    $ character.ArmPose = 1
    if "no sex" in character.DailyActions:
        ch_r "Learn to take \"no\" for an answer, [character.Petname]."
        $ character.RecentActions.append("angry")
        $ character.DailyActions.append("angry")
    elif character.Forced:
        $ character.FaceChange("angry", 1)
        ch_r "I'm not doing that just because you have me over a barrel."
        $ character.Statup("Lust", 200, 5)
        if character.Love > 300:
                $ character.Statup("Love", 70, -2)
        $ character.Statup("Obed", 50, -2)
        $ character.RecentActions.append("angry")
        $ character.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ character.FaceChange("angry", 1)
        $ character.RecentActions.append("tabno")
        $ character.DailyActions.append("tabno")
        ch_r "Even if I wanted to, it certainly wouldn't be here!"
        $ character.Statup("Lust", 200, 5)
        $ character.Statup("Obed", 50, -3)
    elif character.Sex:
        $ character.FaceChange("sad")
        ch_r "Maybe you could go fuck yourself instead."
    else:
        $ character.FaceChange("normal", 1)
        ch_r "No way."
    $ character.RecentActions.append("no sex")
    $ character.DailyActions.append("no sex")
    $ temp_modifier = 0
    return


label Rogue_Sex_A:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(character)
    call sex_set_modifier(character, action)

    $ Approval = ApprovalCheck(character, 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)

    if Situation == "auto":
        $ character.Pose = "doggy"
        call Rogue_Sex_Launch("anal")
        if character.PantsNum() == 5:
            "You press up against [character.Name]'s backside, sliding her skirt up as you go."
            $ character.Upskirt = 1
        elif character.PantsNum() > 6:
            "You press up against [character.Name]'s backside, sliding her pants down as you do."
            $ character.Legs = 0
        else:
            "You press up against [character.Name]'s backside."
        $ character.SeenPanties = 1
        "You press the tip of your cock against her tight rim."
        $ character.FaceChange("surprised", 1)

        if (character.Anal and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
            "[character.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            $ character.FaceChange("sexy")
            $ character.Statup("Obed", 70, 3)
            $ character.Statup("Inbt", 50, 3)
            $ character.Statup("Inbt", 70, 1)
            ch_r "Hmm, stick it in. . ."
            call anal_prep(character)
        else:                                                                                                            #she's questioning it
            $ character.Brows = "angry"
            menu:
                ch_r "Hey, what do you think you're doing back there?!"
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ character.FaceChange("sexy", 1)
                        $ character.Statup("Obed", 70, 3)
                        $ character.Statup("Inbt", 50, 3)
                        $ character.Statup("Inbt", 70, 1)
                        ch_r "I guess if you really want to try it. . ."
                        call anal_prep(character)
                    "You pull back before you really get it in."
                    $ character.FaceChange("bemused", 1)
                    if character.Anal:
                        ch_r "Well ok, [character.Petname], no harm done. Just give me a little warning next time."
                    else:
                        ch_r "Well ok, [character.Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."
                "Just fucking.":
                    $ character.Statup("Love", 80, -10, 1)
                    $ character.Statup("Love", 200, -8)
                    "You press into her."
                    $ character.Statup("Obed", 70, 3)
                    $ character.Statup("Inbt", 50, 3)
                    if not ApprovalCheck(character, 700, "O", TabM=1):
                        $ character.FaceChange("angry")
                        "[character.Name] shoves you away and slaps you in the face."
                        ch_r "Jackass!"
                        ch_r "If that's how you want to treat me, we're done here!"
                        $ character.Statup("Love", 50, -10, 1)
                        $ character.Statup("Obed", 50, 3)
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Rogue_Sex_Reset
                        $ character.RecentActions.append("angry")
                        $ character.DailyActions.append("angry")
                    else:
                        $ character.FaceChange("sad")
                        "[character.Name] doesn't seem to be into this, you're lucky she's so obedient."
                        call anal_prep(character)
        return


    if not character.Anal and "no anal" not in character.RecentActions:                                                               #first time
        $ character.FaceChange("surprised", 1)
        $ character.Mouth = "kiss"
        ch_r "Wait, so you want to stick it in my butt?!"

        if character.Forced:
            $ character.FaceChange("sad")
            ch_r "Seriously?"

    if not character.Loose and ("dildo anal" in character.DailyActions or "anal" in character.DailyActions):
        $ character.FaceChange("bemused", 1)
        ch_r "I'm still a little sore from earlier."

    elif "anal" in character.RecentActions:
        $ character.FaceChange("sexy", 1)
        ch_r "You want to go again? Ok."
        call anal_prep(character)


    if not character.Anal and Approval:                                                 #First time dialog
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Love", 20, -2, 1)
        elif character.Love >= (character.Obed + character.Inbt):
            $ character.FaceChange("sexy")
            $ character.Brows = "sad"
            $ character.Mouth = "smile"
            ch_r "I guess if you really want to try it. . ."
        elif character.Obed >= character.Inbt:
            $ character.FaceChange("normal")
            ch_r "Ok, [character.Petname], I'm ready."
        elif character.Addict >= 50:
            $ character.FaceChange("manic", 1)
            ch_r "Well. . . I bet it would feel really good down there."
        else: # Uninhibited
            $ character.FaceChange("sad")
            $ character.Mouth = "smile"
            ch_r "Hmm, it has been on my list. . ."

    elif Approval:                                                                       #Second time+ dialog
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Love", 20, -2, 1)
            ch_r "That's really what you want?"
        elif not Taboo and "tabno" in character.DailyActions:
            ch_r "Well, at least you got us some privacy this time. . ."
        elif "anal" in character.DailyActions and not character.Loose:
            pass
        elif "anal" in character.RecentActions:
            ch_r "I think I'm warmed up. . ."
            call anal_prep(character)
        elif "anal" in character.DailyActions:
            $ character.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",
                "So you'd like another go?",
                "I'm still a little sore from earlier.",
                "Didn't get enough earlier?",
                "You're going to wear me out."])
            ch_r "[Line]"
        elif character.Anal < 3:
            $ character.FaceChange("sexy", 1)
            $ character.Brows = "confused"
            $ character.Mouth = "kiss"
            ch_r "So you'd like another go?"
        else:
            $ character.FaceChange("sexy", 1)
            $ character.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action?",
                "So you'd like another go?",
                "You can't stay away from this booty.",
                "You want me to ride your pole?",
                "You wanna dip your wick?"])
            ch_r "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Obed", 90, 1)
            $ character.Statup("Inbt", 60, 1)
            ch_r "Ok, fine."
        elif "no anal" in character.DailyActions:
            ch_r "Ok, ok, I have been itching for this. . ."
        else:
            $ character.FaceChange("sexy", 1)
            $ character.Statup("Love", 90, 1)
            $ character.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, stick it in.",
                "Well. . . ok.",
                "Sure!",
                "I guess I could. . . stick it in.",
                "Hells yeah.",
                "Heh, ok, ok."])
            ch_r "[Line]"
            $ Line = 0
        $ character.Statup("Obed", 20, 1)
        $ character.Statup("Obed", 60, 1)
        $ character.Statup("Inbt", 70, 2)
        call anal_prep(character)

    else:                                                                               #She's not into it, but maybe. . .
        $ character.FaceChange("angry")
        if "no anal" in character.RecentActions:
            ch_r "What part of \"no,\" did you not get, [character.Petname]?"
        elif Taboo and "tabno" in character.DailyActions and "no anal" in character.DailyActions:
            ch_r "I already told you that I wouldn't do that out here!"
        elif "no anal" in character.DailyActions:
            ch_r "I already told you \"no,\" [character.Petname]."
        elif Taboo and "tabno" in character.DailyActions:
            ch_r "I already told you that I wouldn't do that out here!"
        elif not character.Anal:
            $ character.FaceChange("bemused")
            ch_r "I'm just not into that, [character.Petname]. . ."
        elif not character.Loose and "anal" not in character.DailyActions:
            $ character.FaceChange("perplexed")
            ch_r "You could have been a bit more gentle last time, [character.Petname]. . ."
        else:
            $ character.FaceChange("bemused")
            ch_r "Not, right now [character.Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no anal" in character.DailyActions:
                $ character.FaceChange("bemused")
                ch_r "Yeah, ok, [character.Petname]."
                return
            "Maybe later?" if "no anal" not in character.DailyActions:
                $ character.FaceChange("sexy")
                ch_r "I'll give it some thought, [character.Petname]."
                $ character.Statup("Love", 80, 2)
                $ character.Statup("Inbt", 70, 2)
                if Taboo:
                    $ character.RecentActions.append("tabno")
                    $ character.DailyActions.append("tabno")
                $ character.RecentActions.append("no anal")
                $ character.DailyActions.append("no anal")
                return
            "I bet it would feel really good. . .":
                if Approval:
                    $ character.FaceChange("sexy")
                    $ character.Statup("Obed", 90, 2)
                    $ character.Statup("Obed", 50, 2)
                    $ character.Statup("Inbt", 70, 3)
                    $ character.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",
                        "I suppose. . .",
                        "You've got me there."])
                    ch_r "[Line]"
                    $ Line = 0
                    call anal_prep(character)
                else:
                    pass

            "Bend over.":                                               # Pressured into it
                $ Approval = ApprovalCheck(character, 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
                if Approval > 1 or (Approval and character.Forced):
                    $ character.FaceChange("sad")
                    $ character.Statup("Love", 70, -5, 1)
                    $ character.Statup("Love", 200, -5)
                    ch_r "Ok, fine. If we're going to do this, stick it in already."
                    $ character.Statup("Obed", 80, 4)
                    $ character.Statup("Inbt", 80, 1)
                    $ character.Statup("Inbt", 60, 3)
                    $ character.Forced = 1
                    call anal_prep(character)
                else:
                    $ character.Statup("Love", 200, -20)
                    $ character.RecentActions.append("angry")
                    $ character.DailyActions.append("angry")

    #She refused all offers.
    $ character.ArmPose = 1
    if "no anal" in character.DailyActions:
        ch_r "Learn to take \"no\" for an answer, [character.Petname]."
        $ character.RecentActions.append("angry")
        $ character.DailyActions.append("angry")
    elif character.Forced:
        $ character.FaceChange("angry", 1)
        ch_r "That's a bit much, even for you."
        $ character.Statup("Lust", 200, 5)
        if character.Love > 300:
                $ character.Statup("Love", 70, -2)
        $ character.Statup("Obed", 50, -2)
        $ character.RecentActions.append("angry")
        $ character.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ character.FaceChange("angry", 1)
        $ character.RecentActions.append("tabno")
        $ character.DailyActions.append("tabno")
        ch_r "That you would even suggest such a thing in a place like this. . ."
        $ character.Statup("Lust", 200, 5)
        $ character.Statup("Obed", 50, -3)
    elif not character.Loose and "anal" in character.DailyActions:
        $ character.FaceChange("bemused")
        ch_r "Sorry, I just need a little break back there, [character.Petname]."
    elif character.Anal:
        $ character.FaceChange("sad")
        ch_r "The only thing you can do with my ass is kiss it, [character.Petname]."
        ch_r ". . .Don't get any ideas."
    else:
        $ character.FaceChange("normal", 1)
        ch_r "Not happening."
    $ character.RecentActions.append("no anal")
    $ character.DailyActions.append("no anal")
    $ temp_modifier = 0
    return


label Rogue_Sex_H:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(character)
    call sex_set_modifier(character, action)

    $ Approval = ApprovalCheck(character, 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)

    if Situation == "auto":
        $ character.Pose = "doggy"
        call Rogue_Sex_Launch("hotdog")
        "You press up against [character.Name]'s backside."
        $ character.FaceChange("surprised", 1)

        if (character.Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
            "[character.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            $ character.FaceChange("sexy")
            $ character.Statup("Obed", 70, 3)
            $ character.Statup("Inbt", 50, 3)
            $ character.Statup("Inbt", 70, 1)
            ch_r "Hmm, I've apparently got someone's attention. . ."
            call hotdog_prep(character)
        else:                                                                                                            #she's questioning it
            $ character.Brows = "angry"
            menu:
                ch_r "Hmm, kinda rude, [character.Petname]."
                "Sorry, sorry! Never mind.":
                    if Approval:
                        $ character.FaceChange("sexy", 1)
                        $ character.Statup("Obed", 70, 3)
                        $ character.Statup("Inbt", 50, 3)
                        $ character.Statup("Inbt", 70, 1)
                        ch_r "I guess it doesn't feel so bad. . ."
                        call hotdog_prep(character)
                    "You pull back before you really get it in."
                    $ character.FaceChange("bemused", 1)
                    if character.Hotdog:
                        ch_r "Well ok, [character.Petname], it has been kinda fun."
                    else:
                        ch_r "Well ok, [character.Petname], that's a bit dirty, maybe ask a girl?"
                "You'll see.":
                    $ character.Statup("Love", 80, -10, 1)
                    $ character.Statup("Love", 200, -8)
                    "You grind against her asscrack."
                    $ character.Statup("Obed", 70, 3)
                    $ character.Statup("Inbt", 50, 3)
                    if not ApprovalCheck(character, 500, "O", TabM=1): #Checks if Obed is 700+
                        $ character.FaceChange("angry")
                        "[character.Name] shoves you away."
                        ch_r "Dick!"
                        ch_r "If that's how you want want to act, I'm out of here!"
                        $ character.Statup("Love", 50, -10, 1)
                        $ character.Statup("Obed", 50, 3)
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Rogue_Sex_Reset
                        $ character.RecentActions.append("angry")
                        $ character.DailyActions.append("angry")
                    else:
                        $ character.FaceChange("sad")
                        "[character.Name] doesn't seem to be into this, but she knows her place."
                        call hotdog_prep(character)
        return


    if not character.Hotdog and "no hotdog" not in character.RecentActions:                                                               #first time
        $ character.FaceChange("surprised", 1)
        $ character.Mouth = "kiss"
        ch_r "Wait, so you want to grind against my butt?!"

        if character.Forced:
            $ character.FaceChange("sad")
            ch_r ". . . That's all?"


    if not character.Hotdog and Approval:                                                 #First time dialog
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Love", 20, -2, 1)
        elif character.Love >= (character.Obed + character.Inbt):
            $ character.FaceChange("sexy")
            $ character.Brows = "sad"
            $ character.Mouth = "smile"
            ch_r "It looks like you need some relief. . ."
        elif character.Obed >= character.Inbt:
            $ character.FaceChange("normal")
            ch_r "If that's what you need, [character.Petname]."
        elif character.Addict >= 50:
            $ character.FaceChange("manic", 1)
            ch_r "Hmmm. . ."
        else: # Uninhibited
            $ character.FaceChange("sad")
            $ character.Mouth = "smile"
            ch_r "Hmm, you look ready for it, at least. . ."

    elif Approval:                                                                       #Second time+ dialog
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Love", 20, -2, 1)
            ch_r "That's all you want?"
        elif not Taboo and "tabno" in character.DailyActions:
            ch_r "Well, at least you got us some privacy this time. . ."
        elif "hotdog" in character.RecentActions:
            $ character.FaceChange("sexy", 1)
            ch_r "You want to go again? Ok."
            call hotdog_prep(character)
        elif "hotdog" in character.DailyActions:
            $ character.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",
                "So you'd like another go?",
                "You can't stay away from this booty. . .",
                "Are you sure that's all you want?"])
            ch_r "[Line]"
        elif character.Hotdog < 3:
            $ character.FaceChange("sexy", 1)
            $ character.Brows = "confused"
            $ character.Mouth = "kiss"
            ch_r "So you'd like another go?"
        else:
            $ character.FaceChange("sexy", 1)
            $ character.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action?",
                "So you'd like another go?",
                "You can't stay away from this booty.",
                "You want me to slick your pole?"])
            ch_r "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Obed", 80, 1)
            $ character.Statup("Inbt", 60, 1)
            ch_r "Ok, fine."
        elif "no hotdog" in character.DailyActions:
            ch_r "Well, I guess it's not so bad. . ."
        else:
            $ character.FaceChange("sexy", 1)
            $ character.Statup("Love", 80, 1)
            $ character.Statup("Inbt", 50, 2)
            $ Line = renpy.random.choice(["Well, sure, give it a rub.",
                "Well. . . ok.",
                "Sure!",
                "I guess we could do that.",
                "Hells yeah.",
                "Heh, ok, ok."])
            ch_r "[Line]"
            $ Line = 0
        $ character.Statup("Obed", 60, 1)
        $ character.Statup("Inbt", 70, 2)
        call hotdog_prep(character)

    else:                                                                               #She's not into it, but maybe. . .
        $ character.FaceChange("angry")
        if "no hotdog" in character.RecentActions:
            ch_r "I {i}just{/i} told you \"no,\" [character.Petname]."
        elif Taboo and "tabno" in character.DailyActions and "no hotdog" in character.DailyActions:
            ch_r "I told you that I didn't want you rubb'in up on me in public!"
        elif "no hotdog" in character.DailyActions:
            ch_r "I told you \"no\" earlier, [character.Petname]."
        elif Taboo and "tabno" in character.DailyActions:
            ch_r "I told you that I didn't want you rubb'in up on me in public!"
        elif not character.Hotdog:
            $ character.FaceChange("bemused")
            ch_r "That's kinda naughty, [character.Petname]. . ."
        else:
            $ character.FaceChange("bemused")
            ch_r "Not, right now [character.Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no hotdog" in character.DailyActions:
                $ character.FaceChange("bemused")
                ch_r "Yeah, ok, [character.Petname]."
                return
            "Maybe later?" if "no hotdog" not in character.DailyActions:
                $ character.FaceChange("sexy")
                ch_r "Yeah, maybe, [character.Petname]."
                $ character.Statup("Love", 80, 1)
                $ character.Statup("Inbt", 50, 1)
                if Taboo:
                    $ character.RecentActions.append("tabno")
                    $ character.DailyActions.append("tabno")
                $ character.RecentActions.append("no hotdog")
                $ character.DailyActions.append("no hotdog")
                return
            "You might like it. . .":
                if Approval:
                    $ character.FaceChange("sexy")
                    $ character.Statup("Obed", 60, 2)
                    $ character.Statup("Inbt", 50, 2)
                    $ Line = renpy.random.choice(["Well, sure, give it a rub.",
                        "I suppose. . .",
                        "You've got me there."])
                    ch_r "[Line]"
                    $ Line = 0
                    call hotdog_prep(character)
                else:
                    pass

            "Bend over.":                                               # Pressured into it
                $ Approval = ApprovalCheck(character, 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and character.Forced):
                    $ character.FaceChange("sad")
                    $ character.Statup("Love", 70, -2, 1)
                    $ character.Statup("Love", 200, -2)
                    ch_r "Ok, fine. Whatever."
                    $ character.Statup("Obed", 80, 4)
                    $ character.Statup("Inbt", 60, 2)
                    $ character.Forced = 1
                    call hotdog_prep(character)
                else:
                    $ character.Statup("Love", 200, -10)
                    $ character.RecentActions.append("angry")
                    $ character.DailyActions.append("angry")

    #She refused all offers.
    $ character.ArmPose = 1

    if "no hotdog" in character.DailyActions:
        ch_r "I just don't want to, [character.Petname]."
        $ character.RecentActions.append("angry")
        $ character.DailyActions.append("angry")
    if character.Forced:
        $ character.FaceChange("angry", 1)
        ch_r "Even that's not worth it."
        $ character.Statup("Lust", 200, 5)
        if character.Love > 300:
                $ character.Statup("Love", 70, -1)
        $ character.Statup("Obed", 50, -1)
        $ character.RecentActions.append("angry")
        $ character.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ character.FaceChange("angry", 1)
        $ character.RecentActions.append("tabno")
        $ character.DailyActions.append("tabno")
        ch_r "I'd be a bit embarassed doing that here."
        $ character.Statup("Lust", 200, 5)
        $ character.Statup("Obed", 50, -3)
    elif character.Hotdog:
        $ character.FaceChange("sad")
        ch_r "Eh-eh, not anymore, [character.Petname]."
    else:
        $ character.FaceChange("normal", 1)
        ch_r "Not interested."
    $ character.RecentActions.append("no hotdog")
    $ character.DailyActions.append("no hotdog")
    $ temp_modifier = 0
    return


image AssBase:                  #This is the base image, used in masks
    "images/RogueDoggy/Rogue_Doggy_Ass.png"

image Dildo_Animation:
    contains:
        "UI_Dildo"
        block:
            ease 1 pos (100,300) #pos (0,50)
            ease 1 pos (100,400) #pos (0,0)
            repeat

image AssTest:
#    "Dildo_Animation"
    AlphaMask("Dildo_Animation", "AssBase")
