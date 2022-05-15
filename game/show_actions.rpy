label before_show:
    $ focused_Girl.Upskirt = 1
    $ focused_Girl.PantiesDown = 1

    call first_bottomless(focused_Girl, 1)
    call set_the_scene(check_if_dressed=0)

    if "unseen" in focused_Girl.recent_history:
        $ focused_Girl.change_face("sexy")
        $ focused_Girl.Eyes = "closed"
        $ focused_Girl.ArmPose = 2

        "You see [focused_Girl.name] leaning back, masturbating. You don't think she's noticed you yet."
    else:
        $ focused_Girl.change_face("sexy")
        $ focused_Girl.ArmPose = 2

        "[focused_Girl.name] lays back and starts to toy with herself."

        if not focused_Girl.Mast:#First time
            if focused_Girl.Forced:
                $ focused_Girl.change_stat("love", 90, -20)
                $ focused_Girl.change_stat("obedience", 70, 45)
                $ focused_Girl.change_stat("inhibition", 80, 35)
            else:
                $ focused_Girl.change_stat("love", 90, 15)
                $ focused_Girl.change_stat("obedience", 70, 35)
                $ focused_Girl.change_stat("inhibition", 80, 40)

    $ primary_action = "masturbation"

    if not girl_offhand_action:
        $ girl_offhand_action = "fondle_pussy"

    if action_context:
        $ renpy.pop_call()

        $ action_context = 0

    $ line = 0

    if Taboo:
        $ focused_Girl.DrainWord("tabno")

    $ focused_Girl.DrainWord("no_masturbation")
    $ focused_Girl.recent_history.append("masturbation")
    $ focused_Girl.daily_history.append("masturbation")

label show_cycle:
    if action_context == "join":
        $ renpy.pop_call()

        $ action_context = 0

    while Round > 0:
        call reset_position(focused_Girl, trigger = "masturbation")
        call shift_focus(focused_Girl)

        $ focused_Girl.lustFace

        if "unseen" in focused_Girl.recent_history:
            $ focused_Girl.Eyes = "closed"

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if Player.Focus < 100:
            menu:
                "Keep Watching.":
                    pass
                "[focused_Girl.name]. . .[[jump in]" if "unseen" not in focused_Girl.recent_history and "join" not in Player.recent_history and focused_Girl.location == bg_current:
                    "[focused_Girl.name] slows what she's doing with a sly grin."
                    ch_r "Yeah, did you want something, [focused_Girl.Petname]?"

                    $ action_context = "join"

                    call masturbate(focused_Girl)
                "\"Ahem. . .\"" if "unseen" in focused_Girl.recent_history:
                    jump after_show
                "Start jack'in it." if offhand_action != "jackin":
                    call Jackin(focused_Girl)
                "Stop jack'in it." if offhand_action == "jackin":
                    $ offhand_action = 0
                "Slap her ass" if focused_Girl.location == bg_current:
                    if "unseen" in focused_Girl.recent_history:
                        "You smack [focused_Girl.name] firmly on the ass!"

                        jump after_show
                    else:
                        call Slap_Ass(focused_Girl)

                        $ counter += 1
                        $ Round -= 1

                        jump show_cycle
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
                        "Offhand action" if focused_Girl.location == bg_current:
                            if focused_Girl.Action and multi_action:
                                call Offhand_Set

                                if offhand_action:
                                     $ focused_Girl.Action -= 1
                            else:
                                call tired_lines(focused_Girl)
                        "Threesome actions (locked)" if not Partner or "unseen" in focused_Girl.recent_history or focused_Girl.location == bg_current:
                            pass
                        "Threesome actions" if focused_Girl.location == bg_current and Partner and "unseen" not in focused_Girl.recent_history:
                            menu:
                                "Ask [Partner.name] to do something else":
                                    call Three_Change(focused_Girl)
                                "Swap to [Partner.name]":
                                    call primary_action_Swap(focused_Girl)
                                "Undress [Partner.name]":
                                    call Girl_Undress(Partner)

                                    jump show_cycle
                                "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                    pass
                                "Clean up [Partner.name]" if Partner.Spunk:
                                    call Girl_Cleanup(Partner,"ask")
                                    jump show_cycle
                                "Never mind":
                                    jump show_cycle
                        "Show her feet" if not ShowFeet and (focused_Girl.Pose == "doggy" or focused_Girl.Pose == "sex"):
                            $ ShowFeet = 1
                        "Hide her feet" if ShowFeet and (focused_Girl.Pose == "doggy" or focused_Girl.Pose == "sex"):
                            $ ShowFeet = 0
                        "Undress [focused_Girl.name]":
                            if "unseen" in focused_Girl.recent_history:
                                ch_p "Oh, yeah, take it off. . ."

                                jump after_show
                            else:
                                call Girl_Undress(focused_Girl)
                        "Clean up [focused_Girl.name] (locked)" if not focused_Girl.Spunk:
                                pass
                        "Clean up [focused_Girl.name]" if focused_Girl.Spunk:
                            if "unseen" in focused_Girl.recent_history:
                                ch_p "You've got a little something on you. . ."

                                jump after_show
                            else:
                                call Girl_Cleanup(focused_Girl,"ask")
                        "Never mind":
                            jump show_cycle
                "Back to Sex Menu" if multi_action and focused_Girl.location == bg_current:
                    ch_p "Let's try something else."

                    call reset_position(focused_Girl)

                    $ action_context = "shift"
                    $ line = 0

                    jump after_show
                "End Scene" if not multi_action or focused_Girl.location != bg_current:
                    ch_p "Let's stop for now."

                    call reset_position(focused_Girl)

                    $ line = 0

                    jump after_show

        call shift_focus(focused_Girl)
        call Sex_Dialog(focused_Girl,Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up

        if Player.Focus >= 100 or focused_Girl.lust >= 100:
            if Player.Focus >= 100:
                if "unseen" not in focused_Girl.recent_history:
                    call Player_Cumming(focused_Girl)

                    if "angry" in focused_Girl.recent_history:
                        call reset_position(focused_Girl)

                        return

                    $ focused_Girl.change_stat("lust", 200, 5)

                    if 100 > focused_Girl.lust >= 70 and focused_Girl.OCount < 2:
                        $ focused_Girl.recent_history.append("unsatisfied")
                        $ focused_Girl.daily_history.append("unsatisfied")

                    $ line = "came"
                else: #If she wasn't aware you were there
                    "You grunt and try to hold it in."

                    $ Player.Focus = 95

                    if focused_Girl.location == bg_current:
                        jump after_show

            #If Rogue can cum
            if focused_Girl.lust >= 100:
                call Girl_Cumming(focused_Girl)

                if focused_Girl.location == bg_current:
                    jump after_show

            if line == "came":
                $ line = 0

                if not Player.Semen:
                    "You're emptied out, you should probably take a break."

                    $ offhand_action = 0 if offhand_action == "jackin" else offhand_action

                if "unsatisfied" in focused_Girl.recent_history:#And Rogue is unsatisfied,
                    "[focused_Girl.name] still seems a bit unsatisfied with the experience."

                    menu:
                        "Let her keep going?"
                        "Yes, keep going for a bit.":
                            $ line = "You let her get back into it"

                            jump show_cycle
                        "No, I'm done.":
                            "You ask her to stop."

                            return

        if Partner and Partner.lust >= 100:
            call Girl_Cumming(Partner)

        if "unseen" in focused_Girl.recent_history:
            if Round == 10:
                "It's getting a bit late, [focused_Girl.name] will probably be wrapping up soon."
            elif Round == 5:
                "She's definitely going to stop soon."
        else:
            if focused_Girl.location == bg_current:
                call Escalation(focused_Girl) #sees if she wants to escalate things

            if Round == 10:
                ch_r "We might want to wrap this up, it's getting late."

                $ focused_Girl.lust += 10
            elif Round == 5:
                ch_r "Seriously, it'll be time to stop soon."

                $ focused_Girl.lust += 25

    $ focused_Girl.change_face("bemused", 0)

    $ line = 0

    if "unseen" not in focused_Girl.recent_history:
        ch_r "Ok, [focused_Girl.Petname], that's enough of that for now."

label after_show:
    if "unseen" in focused_Girl.recent_history:
        $ focused_Girl.change_face("surprised", 1)

        "[focused_Girl.name] stops what she's doing with a start, eyes wide."

        call first_bottomless(focused_Girl, 1)

        $ focused_Girl.change_face("surprised", 1)

        if offhand_action == "jackin":
            ch_r "H- how long you been stand'in there, [focused_Girl.Petname]?"

            $ focused_Girl.Eyes = "down"

            menu:
                ch_r "And why is your cock out like that?!"
                "Long enough, it was an excellent show.":
                    $ focused_Girl.change_face("sexy")
                    $ focused_Girl.change_stat("obedience", 50, 3)
                    $ focused_Girl.change_stat("obedience", 70, 2)

                    ch_r "Well, I imagine it was. . ."

                    if focused_Girl.love >= 800 or focused_Girl.obedience >= 500 or focused_Girl.inhibition >= 500:
                        $ temp_modifier += 10

                        $ focused_Girl.change_stat("lust", 90, 5)

                        ch_r "And the view from this angle ain't so bad either. . ."
                "I. . . just got here?":
                    $ focused_Girl.change_face("angry")
                    $ focused_Girl.change_stat("love", 70, 2)
                    $ focused_Girl.change_stat("love", 90, 1)
                    $ focused_Girl.change_stat("obedience", 50, 2)
                    $ focused_Girl.change_stat("obedience", 70, 2)

                    "She looks pointedly at your cock,"
                    ch_r "A likely story . . ."

                    if focused_Girl.love >= 800 or focused_Girl.obedience >= 500 or focused_Girl.inhibition >= 500:
                        $ temp_modifier += 10

                        $ focused_Girl.change_stat("lust", 90, 5)
                        $ focused_Girl.change_face("bemused", 1)

                        ch_r "Still, can't blame a fella for take'in inspirations."
                    else:
                        $ temp_modifier -= 10

                        $ focused_Girl.change_stat("lust", 200, -5)

            call Seen_First_Peen(focused_Girl,Partner)
            ch_r "Hmm. . ."
        else:
            ch_r "H- how long you been stand'in there, [focused_Girl.Petname]?"

            menu:
                extend ""
                "Long enough.":
                    $ focused_Girl.change_face("sexy", 1)
                    $ focused_Girl.change_stat("obedience", 50, 3)
                    $ focused_Girl.change_stat("obedience", 70, 2)

                    ch_r "Well I hope you got a good show out of it. . ."
                "I just got here.":
                    $ focused_Girl.change_face("bemused", 1)
                    $ focused_Girl.change_stat("love", 70, 2)
                    $ focused_Girl.change_stat("love", 90, 1)

                    ch_r "A likely story . . ."

                    $ focused_Girl.change_stat("obedience", 50, 2)
                    $ focused_Girl.change_stat("obedience", 70, 2)

        $ focused_Girl.DrainWord("unseen",1,0) #She sees you, so remove unseens
        $ focused_Girl.Mast += 1

        if Round <= 10:
            ch_r "It's getting too late to do much about it right now though."

            return

        $ action_context = "join"

        call masturbate(focused_Girl)

    $ focused_Girl.Action -= 1
    $ focused_Girl.Mast += 1

    if Partner == EmmaX:
        call Partner_Like(focused_Girl,4)
    else:
        call Partner_Like(focused_Girl,3)

    call checkout

    if action_context == "shift":
        $ action_context = 0

        return

    $ action_context = 0

    if focused_Girl.location != bg_current:
        return

    if Round <= 10:
        ch_r "I need to take a little break here, [focused_Girl.Petname]."

        return

    $ focused_Girl.change_face("sexy", 1)

    if focused_Girl.lust < 20:
        ch_r "That really worked for me, [focused_Girl.Petname]. How about you?"
    else:
        ch_r "Yeah, what did you want?"

    menu:
        extend ""
        "Well, I have something you could take care of. . ." if Player.Semen and focused_Girl.Action:
            $ action_context = "shift"

            return
        "You could just keep going. . ." if Player.Semen:
            $ focused_Girl.change_face("sly")

            if focused_Girl.Action and Round >= 10:
                ch_r "Well, alright. . ."

                jump show_cycle
            else:
                ch_r "I'm kinda worn out, maybe time for a break. . ."
        "I'm good here. [[Stop]":
            if focused_Girl.love < 800 and focused_Girl.inhibition < 500 and focused_Girl.obedience < 500:
                $ focused_Girl.OutfitChange(Changed=0)

            $ focused_Girl.change_face("normal")
            $ focused_Girl.Brows = "confused"

            ch_r "Well. . . ok then. . ."

            $ focused_Girl.Brows = "normal"
        "You should probably stop for now." if focused_Girl.lust > 30:
            $ focused_Girl.change_face("angry")

            ch_r "Well if you say so."

    return

label masturbate(Girl):
    $ Round -= 5 if Round > 5 else (Round-1)

    call shift_focus(Girl)

    if Girl.Mast:
        $ temp_modifier += 10
    if Girl.SEXP >= 50:
        $ temp_modifier += 25
    elif Girl.SEXP >= 30:
        $ temp_modifier += 15
    elif Girl.SEXP >= 15:
        $ temp_modifier += 5
    if Girl.lust >= 90:
        $ temp_modifier += 20
    elif Girl.lust >= 75:
        $ temp_modifier += 5
    if "exhibitionist" in Girl.Traits:
        $ temp_modifier += (3*Taboo)
    if Girl in Player.Harem or "sex friend" in Girl.Petnames:
        $ temp_modifier += 10
    elif "ex" in Girl.Traits:
        $ temp_modifier -= 40
    if Girl.ForcedCount and not Girl.Forced:
        $ temp_modifier -= 5 * Girl.ForcedCount

    $ Approval = Approvalcheck(Girl, 1200, TabM = 2) # 120, 135, 150, Taboo -80(200)

    $ Girl.DrainWord("unseen",1,0) #She sees you, so remove unseens

    if action_context == "join":       # This triggers if you ask to join in
        if Approval > 1 or (Approval and Girl.lust >= 50):
            $ Player.AddWord(1,"join")

            menu:
                extend ""
                "Would you like some help? I could lend some helping hands. . ."  if Player.Semen and Girl.Action:
                    $ Girl.change_stat("love", 90, 1)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_face("sexy")

                    ch_r "Well, [Girl.Petname], I suppose I could use some help with these. . ."

                    $ Girl.change_stat("obedience", 70, 2)
                    $ Girl.change_stat("inhibition", 70, 1)

                    $ offhand_action = "fondle_breasts"

                    $ Girl.Mast += 1

                    jump show_cycle
                "Would you like some help? I could. . . up to you, I guess." if Player.Semen and Girl.Action:
                    $ Girl.change_stat("love", 70, 2)
                    $ Girl.change_stat("love", 90, 1)
                    $ Girl.change_face("sexy")

                    ch_r "Well, [Girl.Petname], I suppose you could help me with these. . ."

                    $ Girl.change_stat("obedience", 70, 2)
                    $ Girl.change_stat("inhibition", 70, 1)

                    $ D20 = renpy.random.randint(1, 20)

                    if D20 > 10:
                        $ offhand_action = "fondle_breasts"
                    else:
                        $ offhand_action = "suck_breasts"

                    $ Girl.Mast += 1

                    jump show_cycle
                "Why don't we take care of each other?" if Player.Semen and Girl.Action:
                    $ Girl.change_face("sexy")

                    ch_r "Well what did you have in mind?"

                    $ renpy.pop_call()          #removes the call to this label

                    return                      #returns to sexmenu=
                "You look like you have things well in hand. . .":
                    if Girl.lust >= 50:
                        $ Girl.change_stat("love", 70, 2)
                        $ Girl.change_stat("love", 90, 1)
                        $ Girl.change_face("sexy")

                        ch_r "Well, [Girl.Petname], I suppose I do at that . ."

                        $ Girl.change_stat("obedience", 80, 3)
                        $ Girl.change_stat("inhibition", 80, 5)

                        jump show_cycle
                    elif Approvalcheck(Girl, 1000):
                        $ Girl.change_face("sly")

                        ch_r "Well I did, but I think I've got it taken care of for now. . ."
                    else:
                        $ Girl.change_face("angry")

                        ch_r "Well I did, but now you've blown the mood."

        $ Girl.ArmPose = 1
        $ Girl.OutfitChange(Changed=0)
        $ Girl.Action -= 1
        $ Player.change_stat("Focus", 50, 30)

        call checkout(1)

        $ line = 0
        $ action_context = 0

        $ renpy.pop_call()

        if Approval:
            $ Girl.change_face("bemused", 2)

            if bg_current == Girl.Home:
                ch_r "So what did you come over for anyway, [Girl.Petname]?"
            else:
                ch_r "So . . . fancy bumping into you here, [Girl.Petname]. . ."

            $ Girl.Blush = 1
        else:
            $ Girl.change_stat("love", 200, -5)
            $ Girl.change_face("angry")
            $ Girl.recent_history.append("angry")
            $ Girl.daily_history.append("angry")

            if bg_current == Girl.Home:
                ch_r "Well if you don't mind, I'd kind of appreciate you getting out of here. Maybe knock next time?"
                "[Girl.name] kicks you out of her room."

                $ renpy.pop_call()

                jump Campus_Map
            else:
                ch_r "Well if you don't mind, I'm getting out of here. Maybe knock next time?"

                call remove_girl(Girl)
        return

    if action_context == Girl:                                                                  #Rogue auto-starts
        if Approval > 2:                                                      # fix, add rogue auto stuff here
            if Girl.wearing_skirt:
                "[Girl.name]'s hand snakes down her body, and hikes up her skirt."

                $ Girl.Upskirt = 1
            elif Girl.PantsNum() > 6:
                "[Girl.name] slides her hand down her body and into her jeans."
            elif Girl.HoseNum() >= 5:
                "[Girl.name]'s hand slides down her body and under her [Girl.Hose]."
            elif Girl.Panties:
                "[Girl.name]'s hand slides down her body and under her [Girl.Panties]."
            else:
                "[Girl.name]'s hand slides down her body and begins to caress her pussy."

            $ Girl.SeenPanties = 1

            "She starts to slowly rub herself."

            call first_bottomless(Girl)

            menu:
                "What do you do?"
                "Nothing.":
                    $ Girl.change_stat("inhibition", 80, 3)
                    $ Girl.change_stat("inhibition", 60, 2)

                    "[Girl.name] begins to masturbate."
                "Go for it.":
                    $ Girl.change_face("sexy, 1")
                    $ Girl.change_stat("inhibition", 80, 3)

                    ch_p "That is so sexy, [Girl.Pet]."

                    $ Girl.namecheck() #checks reaction to petname

                    "You lean back and enjoy the show."

                    $ Girl.change_stat("love", 80, 1)
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ Girl.change_face("surprised")
                    $ Girl.change_stat("inhibition", 70, 1)

                    ch_p "Let's not do that right now, [Girl.Pet]."

                    $ Girl.namecheck() #checks reaction to petname

                    "[Girl.name] pulls her hands away from herself."

                    $ Girl.OutfitChange(Changed=0)
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Girl.change_stat("obedience", 30, 2)

                    return
            jump before_show
        else:
            $ temp_modifier = 0                               # fix, add rogue auto stuff here
            $ offhand_action = 0
        return

    if not Girl.Mast:
        $ Girl.change_face("surprised", 1)
        $ Girl.Mouth = "kiss"

        ch_r "You want me to get myself off, while you watch?"

        if Girl.Forced:
            $ Girl.change_face("sad")
            ch_r "So you just want to watch then?"

    if not Girl.Mast and Approval:
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
        elif Girl.love >= (Girl.obedience + Girl.inhibition):
            $ Girl.change_face("sexy")
            $ Girl.Brows = "sad"
            $ Girl.Mouth = "smile"

            ch_r "Since my love life's been a bit. . . limited, I've gotten pretty good at this."
        elif Girl.obedience >= Girl.inhibition:
            $ Girl.change_face("normal")

            ch_r "If that's what you want, [Girl.Petname]. . ."
        else: # Uninhibited
            $ Girl.change_face("sad")
            $ Girl.Mouth = "smile"

            ch_r "I guess it could be fun with you watching. . ."
    elif Approval:
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)

            ch_r "You want to watch me again?"
        elif Approval and "masturbation" in Girl.recent_history:
            $ Girl.change_face("sexy", 1)

            ch_r "I guess I have a bit more in me. . ."

            jump before_show
        elif Approval and "masturbation" in Girl.daily_history:
            $ Girl.change_face("sexy", 1)

            $ line = renpy.random.choice(["You enjoyed the show?",
                "Didn't get enough earlier?",
                "It is nice to have an audience. . ."])
            ch_r "[line]"
        elif Girl.Mast < 3:
            $ Girl.change_face("sexy", 1)
            $ Girl.Brows = "confused"

            ch_r "You like to watch, huh?"
        else:
            $ Girl.change_face("sexy", 1)
            $ Girl.ArmPose = 2

            $ line = renpy.random.choice(["You sure do like to watch.",
                "So you'd like me to go again?",
                "You want to watch some more?",
                "You want me ta diddle myself?"])
            ch_r "[line]"

            $ line = 0

    if Approval >= 2:
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 60, 1)

            ch_r "I suppose, let me get comfortable. . ."
        else:
            $ Girl.change_face("sexy", 1)
            $ Girl.change_stat("love", 90, 1)
            $ Girl.change_stat("inhibition", 50, 3)

            $ line = renpy.random.choice(["Well. . . ok.",
                "I suppose it would help to have something nice to look at. . .",
                "I've kind of needed this anyways. . .",
                "Sure!",
                "I guess I could. . . give it a go.",
                "Heh, ok, ok."])
            ch_r "[line]"

            $ line = 0

        $ Girl.change_stat("obedience", 20, 1)
        $ Girl.change_stat("obedience", 60, 1)
        $ Girl.change_stat("inhibition", 70, 2)

        jump before_show
    else:
        menu:
            ch_r "That's. . . a little intimate, [Girl.Petname]."

            "Maybe later?":
                $ Girl.change_face("sexy", 1)

                if Girl.lust > 50:
                    ch_r "Well, definitely later. . . but I'll have to think about inviting you."
                else:
                    ch_r "Hmm, maybe. . . I'll let you know."

                $ Girl.change_stat("love", 80, 2)
                $ Girl.change_stat("inhibition", 70, 2)

                return
            "You look like you could use it. . .":
                if Approval:
                    $ Girl.change_face("sexy")
                    $ Girl.change_stat("obedience", 90, 2)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("inhibition", 70, 3)
                    $ Girl.change_stat("inhibition", 40, 2)

                    $ line = renpy.random.choice(["Well. . . ok.",
                        "I suppose it would help to have something nice to look at. . .",
                        "I've kind of needed this anyways. . .",
                        "Sure!",
                        "I guess I could. . . give it a go.",
                        "Heh, ok, ok."])
                    ch_r "[line]"

                    $ line = 0

                    jump before_show
            "Just get at it already.":                                               # Pressured into it
                $ Approval = Approvalcheck(Girl, 450, "OI", TabM = 2) # 45, 60, 75, -80(125)

                if Approval > 1 or (Approval and Girl.Forced):
                    $ Girl.change_face("sad")
                    $ Girl.change_stat("love", 70, -5, 1)
                    $ Girl.change_stat("love", 200, -5)

                    ch_r "Ok, fine. I'll give it a try."

                    $ Girl.change_stat("obedience", 80, 4)
                    $ Girl.change_stat("inhibition", 80, 1)
                    $ Girl.change_stat("inhibition", 60, 3)
                    $ Girl.Forced = 1

                    jump before_show
                else:
                    $ Girl.change_stat("love", 200, -20)
                    $ Girl.recent_history.append("angry")
                    $ Girl.daily_history.append("angry")

    $ Girl.ArmPose = 1

    if Girl.Forced:
        $ Girl.change_face("angry", 1)

        ch_r "I'm not doing something so. . . intimate with you watching."

        $ Girl.change_stat("lust", 90, 5)
        if Girl.love > 300:
            $ Girl.change_stat("love", 70, -2)

        $ Girl.change_stat("obedience", 50, -2)
        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
        $ Girl.recent_history.append("no_masturbation")
        $ Girl.daily_history.append("no_masturbation")

        return
    elif Taboo:                             # she refuses and this is too public a place for her
        $ Girl.change_face("angry", 1)
        $ Girl.daily_history.append("tabno")

        ch_r "I can't do that here!"

        $ Girl.change_stat("lust", 90, 5)
        $ Girl.change_stat("obedience", 50, -3)

        return
    elif Girl.Mast:
        $ Girl.change_face("sad")

        ch_r "Nope, not anymore, you'll have to go back to Internet porn."
    else:
        $ Girl.change_face("normal", 1)

        ch_r "Heh, no, I'm not doing that."

    $ Girl.recent_history.append("no_masturbation")
    $ Girl.daily_history.append("no_masturbation")

    $ temp_modifier = 0

    return







label Group_Strip(Girl=0,temp_modifier = temp_modifier,temp_modifierP=[0,0],Girls=[]): #rkeljsv
        #Note, this event would break during a date, since it manipulates Adjacent. Perhaps use unique list?
        $ Present = []
        $ Girls = all_Girls[:]
        while Girls:
                if Girls[0].location == bg_current:
                        $ Present.append(Girls[0])
                $ Girls.remove(Girls[0])

        if not Present:
                "Nobody's here."
                "You dance alone."
                return

        while len(Present) > 2:
                #culls out extra members
                call remove_girl(Present[2])
    #            $ Present.remove(Present[2])

        if len(Present) == 2:
            $ renpy.random.shuffle(Present)
            if Girl and Present[0] != Girl:
                    $ Party.reverse()
            elif Approvalcheck(Present[0],check=1) <= Approvalcheck(Present[1],check=1):
                    # If second one likes you more, pick her
                    $ Present.reverse()

        call shift_focus(Present[0])

        $ Round -= 5 if Round > 5 else (Round-1)
        call set_the_scene(1,0,0,0)

        $ Present[0].change_face("sexy",1)
        if len(Present) >= 2:
                if Present[1] in all_Girls:
                        $ Present[1].change_face("sexy",1)
                else:
                        $ Present.remove(Present[1])

        $ counter = len(Present) #max 2
        while counter:
            $ counter -= 1 #max 1
            if Girl == EmmaX and "classcaught" in EmmaX.recent_history and Alonecheck(EmmaX):
                        #skip this step if during classcaught sequence
                        pass
            elif not Approvalcheck(Present[counter], 600, TabM = 1,Alt=[[EmmaX],(650+Taboo*10)]) or (Present[counter] == EmmaX and Taboo and "taboo" not in EmmaX.History):
                    if not Approvalcheck(Present[counter], 400):
                        if Present[counter] == RogueX:
                                ch_r "I'm just some sort'a gogo dancer now?"
                        elif Present[counter] == KittyX:
                                ch_k "Like I would just dance for you?"
                        elif Present[counter] == EmmaX:
                                ch_e "Oh, you think I'll dance to your tune?"
                        elif Present[counter] == LauraX:
                                ch_l "I don't dance."
                        elif Present[counter] == JeanX:
                                ch_j "I'm not in the mood."
                        elif Present[counter] == StormX:
                                ch_s "I do not dance."
                        elif Present[counter] == JubesX:
                                ch_v "I don't wanna dance, weirdo. . ."
                    elif Present[counter].Taboo:
                        if Present[counter] == RogueX:
                                ch_r "I don't think this is the best place for dance'n."
                        elif Present[counter] == KittyX:
                                ch_k "I don't know, this really isn't a good place for it?"
                        elif Present[counter] == EmmaX:
                                ch_e "You must be joking. Here?"
                        elif Present[counter] == LauraX:
                                if Approvalcheck(LauraX, 600, TabM = 0):    #should add a second Laura, then the first gets removed.
                                        $ Present.append(LauraX)            #This restores the "taboo is irrelevant to her" state
                                else:
                                        ch_l "I don't feel like it."
                        elif Present[counter] == JeanX:
                                ch_j "I don't want to just randomly dance in public."
                        elif Present[counter] == StormX:
                                ch_s "I would not want to make a scene."
                        elif Present[counter] == JubesX:
                                ch_v "This isn't really the place for it. . ."
                    else:
                        if Present[counter] == RogueX:
                                ch_r "I dont feel it right now."
                        elif Present[counter] == KittyX:
                                ch_k "I don't know, I don't really feel like dancing right now."
                        elif Present[counter] == EmmaX:
                                ch_e "I don't really feel like dancing at the moment."
                        elif Present[counter] == LauraX:
                                ch_l "I don't feel like it."
                        elif Present[counter] == JeanX:
                                ch_j "I'm not in the mood."
                        elif Present[counter] == StormX:
                                ch_s "I do not wish to dance right now."
                        elif Present[counter] == JubesX:
                                ch_v "Yeah, I don't feel like dancing right now. . ."
                    $ Present.remove(Present[counter])

        if not Present:
                return

        if EmmaX.location == bg_current and EmmaX not in Present:
                #If Emma is here, but does not agree to this,
                if "classcaught" not in EmmaX.History:
                        if EmmaX.location == EmmaX.Home:
                                #if it's her room. . .
                                ch_e "If the two of you would like to dance, please do it elsewhere."
                                $ Present = []
                                return
                        else:
                                ch_e "I should really be going."
                                call remove_girl(EmmaX)

        if "stripping" in Present[0].daily_history and Approvalcheck(Present[0], 500, TabM = 3):
                $ line = renpy.random.choice(["You liked the show earlier?",
                    "Didn't get enough earlier?",
                    "You're going to wear me out."])
        else:
                $ line = renpy.random.choice(["Ok, that sounds fun.",
                    "I could get into that.",
                    "Yeah, ok."])

        call Anyline(Present[0],line)
        $ line = 0

        call AllReset("all")


        $ counter = len(Present) #max 2
        while counter:
                $ counter -= 1 #max 1
                if Present[counter] == RogueX:
                            show Rogue_Sprite at Girl_Dance1(RogueX)
                elif Present[counter] == KittyX:
                            show Kitty_Sprite at Girl_Dance1(KittyX)
                elif Present[counter] == EmmaX:
                            show Emma_Sprite at Girl_Dance1(EmmaX)
                elif Present[counter] == LauraX:
                            show Laura_Sprite at Girl_Dance1(LauraX)
                elif Present[counter] == JeanX:
                            show Jean_Sprite at Girl_Dance1(JeanX)
                elif Present[counter] == StormX:
                            show Storm_Sprite at Girl_Dance1(StormX)
                elif Present[counter] == JubesX:
                            show Jubes_Sprite at Girl_Dance1(JubesX)
                $ Present[counter].recent_history.append("stripping")
                $ Present[counter].daily_history.append("stripping")
                $ Present[counter].Strip += 1
                $ Present[counter].Action -= 1
                $ temp_modifierP[counter] = temp_modifier
                if Present[counter].SeenChest or Present[counter].SeenPussy:
                        #You've seen her tits.
                        $ temp_modifierP[counter] += 20
                if Present[counter].SeenPanties:
                        #You've seen her panties.
                        $ temp_modifierP[counter] += 5
                if "exhibitionist" in Present[counter].Traits:
                        $ temp_modifierP[counter] += (4*Taboo)
                if ("sex friend" in Present[counter].Petnames or Present[counter] in Player.Harem) and not Taboo:
                        $ temp_modifierP[counter] += 15
                elif "ex" in Present[counter].Traits:
                        $ temp_modifierP[counter] -= 40
                elif Present[counter].ForcedCount and not Present[counter].Forced:
                        $ temp_modifierP[counter] -= 5 * Present[counter].ForcedCount

        if len(Present) >= 2:
                "They start to dance."
                $ Partner = Present[1]
                $ between_event_count = 1
        else:
                "She starts to dance."
                $ between_event_count = 0
                $ Partner = 0


        if Girl == EmmaX and "classcaught" in EmmaX.recent_history and Alonecheck(EmmaX):
                #skip this step if during classcaught sequence
                $ Count = 0
                jump Group_Stripping

        #this portion adds back in girls who dropped out, but sets their "stop" flag.
        $ Girls = all_Girls[:]
        while Girls:
                if Girls[0].location == bg_current and Girls[0] not in Present:
                        $ Present.append(Girls[0])
                        if "stopdancing" not in Girls[0].recent_history:
                                $ Girls[0].recent_history.append("stopdancing")
                $ Girls.remove(Girls[0])

        $ temp_modifier = temp_modifierP[0]
        $ primary_action = "strip"
        $ Count = 1

        while Count and Round >=10:
                #Loops endlessly until you do something.
                $ Round -= 2 if Round > 2 else Round
                if len(Present) >= 2:
                    $ Present[0].GLG(Present[1],600,1,1)
                    $ Present[1].GLG(Present[0],600,1,1)
                menu:
                    "Continue":
                            pass
                    "Would you kindly take off some clothes?":
                            #add checks here
                            call Anyline(Present[0],"Hmm?")
                            $ Count = 0
                    "Stop":
                            jump Group_Strip_End


        if EmmaX.location == bg_current and len(Present) >= 2:
                #If Emma is here, but does not agree to this,
                if "classcaught" not in EmmaX.History or "three" not in EmmaX.History or (Taboo and "taboo" not in EmmaX.History):
                    if EmmaX.location == "bg_emma":
                            #if it's her room. . .
                            ch_e "If the two of you would like to get indecent, please do it elsewhere."
                            $ Present = []
                            return
                    else:
                            ch_e "I should really be going."
                            call remove_girl(EmmaX)

label Group_Stripping:
        while Round >= 10 and Present:
            $ Round -= 2 if Round > 2 else Round

            if Present[Count] != focused_Girl:
                    call shift_focus(Present[Count])

            call Girl_Stripping(Present[Count])

            if len(Present) < 2 and Count != 0:
                    $ Count = 0
            if not Present or not Present[Count]: #threw "list index" errors?
                    jump Group_Strip_End
            if "stopdancing" in Present[Count].recent_history:
                    #if she's just standing around, cut back to the other girl
                    if len(Present) >= 2 and "stopdancing" in Present[0].recent_history and "stopdancing" in Present[1].recent_history:
                            jump Group_Strip_End

            $ primary_action = "strip"

            if not Present:
                    #If everyone leaves, quit out
                    jump Group_Strip_End

            if len(Present) >= 2 and Count != between_event_count:
                $ Present[Count].GLG(Present[between_event_count],800,2,1)
                $ Present[between_event_count].GLG(Present[Count],800,2,1)

            if len(Present) >= 2:
                    # Flips the numbers if in a group
                    # Count starts at 0
                    if Count == 0 and "stopdancing" not in Present[1].recent_history:
                            $ Count = 1
                            $ between_event_count = 0
                            $ temp_modifierP[1] = temp_modifier
                            $ temp_modifier = temp_modifierP[0]
                    elif Count == 1 and "stopdancing" not in Present[0].recent_history:
                            $ Count = 0
                            $ between_event_count = 1
                            $ temp_modifierP[0] = temp_modifier
                            $ temp_modifier = temp_modifierP[1]
                    call shift_focus(Present[Count])
    #                $ Partner = Present[between_event_count]

                    call Activity_check(focused_Girl,Partner)

            if len(Present) < 2 or "stopdancing" in Present[1].recent_history:
                    #Plays if only one girl is dancing
                    $ temp_modifier = temp_modifierP[Count]
                    $ Count = 0
                    $ between_event_count = 0
                    $ Partner = 0

                    call Activity_check(focused_Girl,Partner)

                    if not Present or "stopdancing" in Present[0].recent_history:
                            jump Group_Strip_End
            #ends loop
        if Present and Round <=15:
                call Anyline(Present[0],"It's getting late, we should probably take a break.")

label Group_Strip_End:
        #add like-ups here. . .
        if Present:
                $ Present[0].DrainWord("stopdancing",1,0,0)
                $ Present[0].DrainWord("keepdancing",1,0,0)
        if len(Present) >= 2:
                $ Present[1].DrainWord("stopdancing",1,0,0)
                $ Present[1].DrainWord("keepdancing",1,0,0)

        call set_the_scene(1,0,0,0)
        $ Count = 0
        $ between_event_count = 0
    #    $ renpy.pop_call()
        return

#end Dancing/Stripping / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Girl_Stripping(Girl=0,Nudist=0): #rkeljsv
        #This gets called by Group_Stripping, and returns there at the end.
        if "stopdancing" in Girl.recent_history:
                #if she's just standing around, cut back to the other girl
                return

        $ Girl.ArmPose = 2
        $ Girl.lustFace(1) #sets her lusty face

        if Girl == StormX and (StormX in Rules or Girl.Taboo <= 20):
                #if it's Storm and either you're in private or have broken Xavier, she doesn't fight you
                if Girl.Forced:
                        $ Nudist = -40
                else:
                        $ Nudist = Girl.Taboo
        if "keepdancing" not in Girl.recent_history:
                # if Count isn't 2, it loops.
                if Girl == JubesX and Girl.Acc and (Girl.Over or Girl.Chest) and (Girl.Panties or Girl.Legs or Girl.HoseNum() >= 10):
                    #will she lose the jacket when she's dressed under?
                    if Approvalcheck(Girl, 750, TabM = 3):
                            $ Girl.change_stat("obedience", 50, 1)
                            $ Girl.change_stat("inhibition", 25, 1)
                            $ Player.change_stat("Focus", 60, 3)
                            $ line = Girl.Acc
                            $ Girl.Acc = 0
                            "She shrugs off her [line] and throws it behind her."
                    else:
                            jump Strip_Ultimatum
                elif Girl == JubesX and Girl.Acc and Girl.Over and (Girl.Panties or Girl.Legs or Girl.HoseNum() >= 10):
                    #will she lose the jacket when she's dressed under?
                    if Approvalcheck(Girl, 750, TabM = 3):
                            $ Girl.change_stat("obedience", 50, 1)
                            $ Girl.change_stat("inhibition", 25, 1)
                            $ Player.change_stat("Focus", 60, 3)
                            $ line = Girl.Acc
                            $ Girl.Acc = 0
                            "She shrugs off her [line] and throws it behind her."
                    else:
                            jump Strip_Ultimatum
                elif Girl.Over and Girl.Chest and (Girl.Panties or Girl.Legs or Girl.HoseNum() >= 10):
                    #will she lose the overshirt when she's dressed under?
                    if Approvalcheck(Girl, 750, TabM = 3,Alt=[[StormX],(300-Nudist*3)]):
                            $ Girl.change_stat("obedience", 50, 1)
                            $ Girl.change_stat("inhibition", 25, 1)
                            $ Player.change_stat("Focus", 60, 3)
                            $ line = Girl.Over
                            $ Girl.Over = 0
                            if Girl == KittyX:
                                    "She drops her shoulders and her [line] falls to the floor."
                            else:
                                    "She pulls her [line] over her head and throws it behind her."
                    else:
                            jump Strip_Ultimatum

                elif Girl.Legs and (Girl.Panties or Girl.HoseNum() >= 10):
                    #will she lose the pants/skirt if she has panties on?
                    if Approvalcheck(Girl, 1200, TabM = 3,Alt=[[StormX],(600-Nudist*3)]) or (Girl.SeenPanties and Approvalcheck(Girl, 900, TabM = 3) and not Girl.Taboo):
                            $ Girl.change_stat("lust", 50, 5)
                            $ Girl.change_stat("obedience", 50, 1)
                            $ Girl.change_stat("inhibition", 30, 1)
                            $ Player.change_stat("Focus", 60, 5)
                            $ line = Girl.Legs
                            $ Girl.Legs = 0
                            if Girl == KittyX:
                                    "Her [line] slide through her legs until they're only on her toes, before she kicks them to the floor."
                            else:
                                    "She unzips and pulls down her [line], dropping them to the floor."
                            if not Girl.SeenPanties:
                                    $ Girl.change_stat("obedience", 50, 2)
                                    $ Girl.change_stat("obedience", 200, 3)
                                    $ Girl.change_stat("inhibition", 50, 3)
                                    $ Girl.change_stat("inhibition", 200, 2)
                                    $ Girl.SeenPanties = 1
                    else:
                            jump Strip_Ultimatum

                elif Girl.Hose:
                    # Will she lose the hose?
                    if Girl.HoseNum() >= 10:
                            if Approvalcheck(Girl, 1200, TabM = 3):
                                    $ Girl.change_stat("lust", 50, 6)
                                    $ Player.change_stat("Focus", 60, 6)
                            else:
                                    jump Strip_Ultimatum

                    elif Girl.HoseNum() >= 6 and Approvalcheck(Girl, 1200, TabM = 3):
                            if Approvalcheck(Girl, 1200, TabM = 3,Alt=[[StormX],(600-Nudist*3)]):
                                $ Girl.change_stat("lust", 50, 4)
                                $ Player.change_stat("Focus", 60, 4)
                            else:
                                jump Strip_Ultimatum
                    else:
                            $ Player.change_stat("Focus", 60, 3)
                    $ line = Girl.Hose
                    $ Girl.Hose = 0
                    if Girl == KittyX:
                            "Her [line] slide down off her legs, leaving them in a small pile."
                    else:
                            "She rolls the [line] down off her legs, leaving them in a small pile."
                    call expression Girl.Tag + "_First_Bottomless" pass (1)

                elif Girl == JubesX and Girl.Acc and (Girl.Panties or Girl.Legs or Girl.HoseNum() >= 10):
                    #will she lose the jacket when she's topless under?
                    if Approvalcheck(Girl, 1250, TabM = 3) or (Girl.SeenChest and Approvalcheck(Girl, 1000, TabM = 3) and not Girl.Taboo):
                            $ Girl.change_stat("lust", 60, 5)
                            $ Girl.change_stat("obedience", 50, 2)
                            $ Girl.change_stat("inhibition", 50, 10)
                            $ Player.change_stat("Focus", 80, 15)
                            $ line = Girl.Acc
                            $ Girl.Acc = 0
                            "She shrugs off her [line] and throws it behind her."
                            if not Girl.SeenChest:
                                    $ Girl.change_face("bemused", 1)
                                    $ Girl.change_stat("obedience", 50, 3)
                                    $ Girl.change_stat("obedience", 200, 4)
                                    $ Girl.change_stat("inhibition", 50, 3)
                                    $ Girl.change_stat("inhibition", 200, 3)
                                    "She hesitantly glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                                    call first_topless(Girl, silent = True)
                    else:
                            jump Strip_Ultimatum
                elif Girl.Over and not Girl.Chest and (Girl.Panties or Girl.HoseNum() >= 10):
                    #will she lose the top when she's topless with panties?
                    if Approvalcheck(Girl, 1250, TabM = 3,Alt=[[StormX],(650-Nudist*3)]) or (Girl.SeenChest and Approvalcheck(Girl, 1000, TabM = 3) and not Girl.Taboo):
                            $ Girl.change_stat("lust", 60, 5)
                            $ Girl.change_stat("obedience", 50, 2)
                            $ Girl.change_stat("inhibition", 50, 10)
                            $ Player.change_stat("Focus", 80, 15)
                            $ line = Girl.Over
                            $ Girl.Over = 0
                            if not Girl.SeenChest:
                                    $ Girl.change_face("bemused", 1)
                                    $ Girl.change_stat("obedience", 50, 3)
                                    $ Girl.change_stat("obedience", 200, 4)
                                    $ Girl.change_stat("inhibition", 50, 3)
                                    $ Girl.change_stat("inhibition", 200, 3)
                                    if Girl == KittyX:
                                            "She hesitantly glances your way, and then with tug her [line] passes through her, tossing it to the ground."
                                    elif Girl in (EmmaX,LauraX,StormX):
                                            "She glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                                    else:
                                            "She hesitantly glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                                    call first_topless(Girl, silent = True)
                            else:
                                if Girl == KittyX:
                                        "She drops her shoulders and her [line] falls to the floor."
                                else:
                                        "She pulls her [line] over her head, tossing it to the ground."
                    else:
                            jump Strip_Ultimatum

                elif Girl.Chest and not Girl.Over:
                    # Will she lose the bra?
                    if Approvalcheck(Girl, 1250, TabM = 3,Alt=[[StormX],(650-Nudist*3)]) or (Girl.SeenChest and Approvalcheck(Girl, 1000, TabM = 3) and not Girl.Taboo):
                            $ Girl.change_stat("lust", 60, 5)
                            $ Girl.change_stat("obedience", 50, 2)
                            $ Girl.change_stat("inhibition", 50, 1)
                            $ Player.change_stat("Focus", 80, 15)
                            $ line = Girl.Chest
                            $ Girl.Chest = 0
                            if not Girl.SeenChest:
                                    $ Girl.change_face("bemused", 1)
                                    if Girl == KittyX:
                                            "She hesitantly glances your way, and then with a shrug pulls her [line] through herself, tossing it to the ground."
                                    elif Girl in (EmmaX,LauraX,StormX):
                                            "She glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                                    else:
                                            "She hesitantly glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                                    $ Girl.change_stat("obedience", 50, 3)
                                    $ Girl.change_stat("obedience", 200, 4)
                                    $ Girl.change_stat("inhibition", 50, 3)
                                    $ Girl.change_stat("inhibition", 200, 3)
                                    call first_topless(Girl, silent = True)
                            else:
                                    $ Girl.change_face("sexy")
                                    if Girl == KittyX:
                                            "She pulls her [line] through herself, tossing it to the ground."
                                    else:
                                            "She pulls her [line] over her head, tossing it to the ground."
                    else:
                            jump Strip_Ultimatum

                elif Girl.Legs:
                    #will she lose the pants/skirt if she has no panties on?
                    if Approvalcheck(Girl, 1350, TabM = 3,Alt=[[StormX],(800-Nudist*3)]) or (Girl.SeenPussy and Approvalcheck(Girl, 1100, TabM = 3) and not Girl.Taboo):
                            $ Girl.change_stat("lust", 75, 10)
                            $ line = Girl.Legs
                            $ Girl.Legs = 0
                            if not Girl.SeenPussy:
                                    $ Girl.change_stat("obedience", 60, 3)
                                    $ Girl.change_stat("obedience", 200, 5)
                                    $ Girl.change_stat("inhibition", 50, 4)
                                    $ Girl.change_stat("inhibition", 200, 4)
                                    if Girl == KittyX:
                                            "She shyly looks up at you, and then slowly lets her [line] slide to the floor."
                                    elif Girl in (EmmaX,LauraX,JeanX):
                                            "She hesitantly looks up at you, and then slowly unzips and pulls down her [line], dropping them to the floor."
                                    else:
                                            "She shyly looks up at you, and then slowly unzips and pulls down her [line], dropping them to the floor."
                                    call expression Girl.Tag + "_First_Bottomless" pass (1)
                            else:
                                    $ Girl.change_stat("obedience", 50, 1)
                                    $ Girl.change_stat("obedience", 75, 1)
                                    if Girl == KittyX:
                                            "She lets her [line] pass through her legs, dropping them to the floor."
                                    else:
                                            "She unzips and pulls down her [line], dropping them to the floor."
                                    $ Girl.change_stat("inhibition", 70, 2)
                            $ Player.change_stat("Focus", 85, 15)
                    else:
                            jump Strip_Ultimatum

                elif Girl == JubesX and Girl.Acc:
                    #will she lose the jacket when she's naked under?
                    if Approvalcheck(Girl, 1350, TabM = 3) or (Girl.SeenPussy and Approvalcheck(Girl, 1100, TabM = 3) and not Girl.Taboo):
                            $ line = Girl.Acc
                            $ Girl.Acc = 0
                            if not Girl.SeenPussy:
                                    $ Girl.change_stat("obedience", 60, 3)
                                    $ Girl.change_stat("obedience", 200, 5)
                                    $ Girl.change_stat("inhibition", 50, 4)
                                    $ Girl.change_stat("inhibition", 200, 4)
                                    "She hesitantly glances your way, and then with a shrug pulls her [line] off, tossing it to the ground."
                                    call expression Girl.Tag + "_First_Bottomless" pass (1)
                            else:
                                    "She shrugs her [line] off, tossing it to the ground."

                            if not Girl.Chest or Girl.Uptop:
                                if not Girl.SeenChest:
                                        $ Girl.change_stat("obedience", 50, 3)
                                        $ Girl.change_stat("inhibition", 50, 3)
                                        call first_topless(Girl, silent = True)
                                else:
                                        $ Girl.change_stat("lust", 60, 15)
                                        $ Girl.change_stat("obedience", 50, 3)
                                        $ Girl.change_stat("obedience", 75, 1)
                                        $ Girl.change_stat("inhibition", 50, 3)
                            else:
                                    $ Girl.change_stat("lust", 75, 10)
                                    $ Girl.change_stat("obedience", 50, 1)
                                    $ Girl.change_stat("obedience", 75, 1)
                                    $ Girl.change_stat("inhibition", 70, 2)
                            $ Player.change_stat("Focus", 85, 15)
                    else:
                            jump Strip_Ultimatum
                elif Girl.Over and not Girl.Panties:
                    #will she lose the overshirt when she's bottomless under?
                    if Approvalcheck(Girl, 1350, TabM = 3,Alt=[[StormX],(800-Nudist*3)]) or (Girl.SeenPussy and Approvalcheck(Girl, 1100, TabM = 3) and not Girl.Taboo):
                            $ line = Girl.Over
                            $ Girl.Over = 0
                            if not Girl.SeenPussy:
                                    $ Girl.change_stat("obedience", 60, 3)
                                    $ Girl.change_stat("obedience", 200, 5)
                                    $ Girl.change_stat("inhibition", 50, 4)
                                    $ Girl.change_stat("inhibition", 200, 4)
                                    if Girl == KittyX:
                                            "She hesitantly glances your way, and then with a tug pulls her [line] through herself, tossing it to the ground."
                                    elif Girl in (EmmaX,LauraX,StormX):
                                            "She glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                                    else:
                                            "She hesitantly glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                                    call expression Girl.Tag + "_First_Bottomless" pass (1)
                            else:
                                if Girl == KittyX:
                                        "She drops her shoulders and her [line] falls to the floor."
                                else:
                                        "She pulls her [line] over her head, tossing it to the ground."

                            if not Girl.Chest or Girl.Uptop:
                                if not Girl.SeenChest:
                                        $ Girl.change_stat("obedience", 50, 3)
                                        $ Girl.change_stat("inhibition", 50, 3)
                                        call first_topless(Girl, silent = True)
                                else:
                                        $ Girl.change_stat("lust", 60, 15)
                                        $ Girl.change_stat("obedience", 50, 3)
                                        $ Girl.change_stat("obedience", 75, 1)
                                        $ Girl.change_stat("inhibition", 50, 3)
                            else:
                                    $ Girl.change_stat("lust", 75, 10)
                                    $ Girl.change_stat("obedience", 50, 1)
                                    $ Girl.change_stat("obedience", 75, 1)
                                    $ Girl.change_stat("inhibition", 70, 2)
                            $ Player.change_stat("Focus", 85, 15)
                    else:
                            jump Strip_Ultimatum

                elif Girl.Chest:
                    # Will she go topless?
                    if Approvalcheck(Girl, 1250, TabM = 3,Alt=[[StormX],(750-Nudist*3)]) or (Girl.SeenChest and Approvalcheck(Girl, 1100, TabM = 3) and not Girl.Taboo):
                            $ Girl.change_stat("lust", 60, 5)
                            $ line = Girl.Chest
                            $ Girl.Chest = 0
                            if not Girl.SeenChest:
                                    $ Girl.change_stat("obedience", 50, 3)
                                    $ Girl.change_stat("obedience", 200, 4)
                                    $ Girl.change_stat("inhibition", 50, 3)
                                    $ Girl.change_stat("inhibition", 200, 3)
                                    if Girl == KittyX:
                                            "She hesitantly glances your way, and then with a tug pulls her [line] through herself, tossing it to the ground."
                                    elif Girl in (EmmaX,LauraX,StormX):
                                            "She glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                                    else:
                                            "She hesitantly glances your way, and then with a shrug pulls her [line] over her head, tossing it to the ground."
                                    call first_topless(Girl, silent = True)
                            else:
                                    $ Girl.change_stat("obedience", 50, 2)
                                    if Girl == KittyX:
                                            "She drops her shoulders and her [line] falls to the floor."
                                    else:
                                            "She pulls her [line] over her head, tossing it to the ground."
                                    $ Girl.change_stat("inhibition", 50, 1)
                            $ Player.change_stat("Focus", 80, 15)
                    else:
                            jump Strip_Ultimatum

                elif Girl.Panties:
                    # Will she go bottomless?
                    if Approvalcheck(Girl, 1350, TabM = 3,Alt=[[StormX],(800-Nudist*3)]) or (Girl.SeenPussy and Approvalcheck(Girl, 1100, TabM = 3) and not Girl.Taboo):
                            $ Girl.change_stat("lust", 75, 10)
                            $ line = Girl.Panties
                            $ Girl.Panties = 0
                            if not Girl.SeenPussy:
                                    $ Girl.change_stat("obedience", 60, 3)
                                    $ Girl.change_stat("obedience", 200, 5)
                                    $ Girl.change_stat("inhibition", 50, 4)
                                    $ Girl.change_stat("inhibition", 200, 4)
                                    if Girl == KittyX:
                                            "She shyly looks up at you, and then slowly tugs her [line] off, flinging them to the side."
                                    elif Girl in (EmmaX,LauraX):
                                            "She looks up at you, and then slowly pulls her [line] down, kicking them off to the side."
                                    else:
                                            "She shyly looks up at you, and then slowly pulls her [line] down, kicking them off to the side."
                                    call expression Girl.Tag + "_First_Bottomless" pass (1)
                            else:
                                    $ Girl.change_stat("obedience", 50, 1)
                                    $ Girl.change_stat("obedience", 75, 1)
                                    if Girl == KittyX:
                                            "She  looks up at you, and then gently pulls her [line] off, flicking them to the side."
                                    else:
                                            "She  looks up at you, and then gently pulls her [line] down, kicking them off to the side."
                                    $ Girl.change_stat("inhibition", 70, 2)
                            $ Player.change_stat("Focus", 85, 15)
                    else:
                            jump Strip_Ultimatum

                else:
                    $ Girl.change_face("sexy")
                    if Girl == RogueX:
                            ch_r "I'm afraid that's all I have on, [Girl.Petname]. . ."
                    elif Girl == KittyX:
                            ch_k "It looks like I've run out of clothes. . ."
                    elif Girl == EmmaX:
                            ch_e "Well, it appears I've run out of clothes, [Girl.Petname]. . ."
                    elif Girl == LauraX:
                            ch_l "Well, that's all I've got, [Girl.Petname]. . ."
                    elif Girl == JeanX:
                            ch_j "I'm all out of clothes. . ."
                    elif Girl == StormX:
                            ch_s "I appear to have lost my clothing. . ."
                    elif Girl == JubesX:
                            ch_v "Well, it looks like I'm done here. . ."
                    menu:
                            extend ""
                            "Ok, you can stop":
                                    $ Girl.recent_history.append("stopdancing")
                                    call reset_position(Girl)

                                    return
                            "Keep on dancing":
                                    $ Girl.recent_history.append("keepdancing")
        # end "nude" not in Girl.recent_history loop

        $ Girl.change_stat("lust", 70, 2)               #lust/Focus
        if "exhibitionist" in Girl.Traits:
                $ Girl.change_stat("lust", 200, 2)
        $ Player.change_stat("Focus", 60, 3)
        if offhand_action == "jackin":
                $ Girl.change_stat("lust", 200, 2)
                $ Player.change_stat("Focus", 200, 5)

        if not Player.Semen and Player.Focus >= 50:
                $ Player.Focus = 50

        if Player.Focus >= 100 or Girl.lust >= 100:
                #If either of you could cum

                if Player.Focus >= 100:
                    #You cum
                    call Player_Cumming(Girl)
                    if "angry" in Girl.recent_history:
                            return
                    $ Girl.change_stat("lust", 200, 5)
                    if not Player.Semen and offhand_action == "jackin":
                            "You're spitting dust here, maybe just watch quietly for a while."
                            $ offhand_action = 0
                    if Player.Focus > 80:
                            jump Group_Strip_End

                if Girl.lust >= 100:
                    #and girl cums
                    call Girl_Cumming(Girl)
                    if action_context == "shift" or "angry" in Girl.recent_history:
                            $ Count = 0
                            jump Group_Strip_End

                call AllReset(Girl)

                if Girl == RogueX:
                            show Rogue_Sprite at Girl_Dance1(Girl)
                elif Girl == KittyX:
                            show Kitty_Sprite at Girl_Dance1(Girl)
                elif Girl == EmmaX:
                            show Emma_Sprite at Girl_Dance1(Girl)
                elif Girl == LauraX:
                            show Laura_Sprite at Girl_Dance1(Girl)
                elif Girl == JeanX:
                            show Jean_Sprite at Girl_Dance1(Girl)
                elif Girl == StormX:
                            show Storm_Sprite at Girl_Dance1(Girl)
                elif Girl == JubesX:
                            show Jubes_Sprite at Girl_Dance1(Girl)

                "[Girl.name] begins to dance again."

        if Partner and Partner.lust >= 100:
                #checks if partner could orgasm
                call Girl_Cumming(Partner)

        menu:
            "[Girl.name] should. . ."
            "Keep Going. . ." if "keepdancing" not in Girl.recent_history:
                    $ Girl.Eyes = "sexy"
                    if Girl.love >= 700 or Girl.obedience >= 500:
                        if not temp_modifier:
                            $ temp_modifier = 10
                        elif temp_modifier <= 20:
                            $ temp_modifier += 1
                    if Taboo and Girl.Strip <= 10:
                        $ Girl.change_stat("obedience", 50, 7)
                    elif Taboo or Girl.Strip <= 10:
                        $ Girl.change_stat("obedience", 50, 5)
                    elif Girl.Strip <= 50:
                        $ Girl.change_stat("obedience", 50, 3)
            "Keep Dancing. . ." if "keepdancing" in Girl.recent_history:
                    $ Girl.Eyes = "sexy"

            "Stop stripping, keep dancing" if "keepdancing" not in Girl.recent_history:
                    if Girl == RogueX:
                            ch_r "Ok. . ."
                    elif Girl == KittyX:
                            ch_k "K. . ."
                    elif Girl == EmmaX:
                            ch_e "Oh? Very well."
                    elif Girl == LauraX:
                            ch_l "Huh? I guess. . ."
                    elif Girl == JeanX:
                            ch_j "Ok, sure."
                    elif Girl == StormX:
                            ch_s "Fine. . ."
                    elif Girl == JubesX:
                            ch_v "Oh, well ok. . ."
                    $ Girl.recent_history.append("keepdancing")

            "Start stripping again" if "keepdancing" in Girl.recent_history:
                    $ Girl.recent_history.remove("keepdancing")
                    if "stripforced" in Girl.recent_history:
                            call Anyline(Girl,". . .")
                    else:
                            if Girl == RogueX:
                                    ch_r "Hmm. . ."
                            elif Girl == KittyX:
                                    ch_k "Huh?"
                            else:
                                    call Anyline(Girl,"Hmm. . .")

            "Just watch silently":
                if "watching" not in Girl.recent_history:
                    if "keepdancing" not in Girl.recent_history:
                        if Taboo and Girl.Strip <= 10:
                            $ Girl.change_stat("inhibition", 50, 3)
                        elif Taboo or Girl.Strip <= 10:
                            $ Girl.change_stat("inhibition", 50, 1)
                    elif Girl.Strip <= 50:
                            $ Girl.change_stat("inhibition", 50, 2)
                            $ Girl.change_stat("lust", 70, 2)
                    $ Girl.recent_history.append("watching")

            "Start jack'in it." if offhand_action != "jackin":
                    call Jackin(Girl)
            "Stop jack'in it." if offhand_action == "jackin":
                    $ offhand_action = 0

            "Lose the [Girl.Arms]. . ." if Girl.Arms:
                    $ Girl.change_face("surprised")
                    $ Girl.Mouth = "kiss"
                    call Anyline(Girl,"All right, "+Girl.Petname+".")
                    $ Girl.change_face("sexy")
                    $ Girl.Arms = 0

            "Ok, that's enough.":
                    if Girl == RogueX:
                            ch_r "Ok, [Girl.Petname]. . . "
                    elif Girl == KittyX:
                            ch_k "Ok. . ."
                    else:
                            call Anyline(Girl,"Alright, "+Girl.Petname+".")
                    $ renpy.pop_call()
                    jump Group_Strip_End

        return


label Strip_Ultimatum: #rkeljsv
        if "keepdancing" in Girl.recent_history:
            return

        call reset_position(Girl)

        $ Girl.change_face("bemused", 1)
        if "stripforced" in Girl.recent_history:
                    $ Girl.change_face("sad", 1)
                    if Girl == RogueX:
                            ch_r "That's as far as I care to go, [Girl.Petname]."
                    elif Girl == KittyX:
                            ch_k "That's all you get."
                    elif Girl == EmmaX:
                            ch_e "I think that's plenty, [Girl.Petname]."
                    elif Girl == LauraX:
                            ch_l "Last call, [Girl.Petname]."
                    elif Girl == JeanX:
                            ch_j "Ok, that's my limit."
                    elif Girl == StormX:
                            ch_s "I will go no further. . ."
                    elif Girl == JubesX:
                            ch_v "Ok, that's all you get. . ."
        else:
                    if Girl == RogueX:
                            ch_r "I'm sorry, [Girl.Petname], I'm not ready to show you more. . . Yet."
                    elif Girl == KittyX:
                            ch_k "I don't know, [Girl.Petname], that's as far as I'll go for now."
                    elif Girl == EmmaX:
                            ch_e "I'm afraid that's as far as I'm ready to go, [Girl.Petname]. . . for now."
                    elif Girl == LauraX:
                            ch_l "Ok, that's enough, [Girl.Petname]. . . for now."
                    elif Girl == JeanX:
                            ch_j "Ok, I think you've seen enough. . ."
                    elif Girl == StormX:
                            ch_s "That's enough for now. . ."
                    elif Girl == JubesX:
                            ch_v "I'm kinda done here. . ."
        menu:
            extend ""
            "That's ok, you can stop.":
                    if "ultimatum" not in Girl.daily_history:
                            $ Girl.change_stat("love", 50, 2)
                            $ Girl.change_stat("love", 90, 2)
                            $ Girl.change_stat("inhibition", 50, 2)
                            $ Girl.daily_history.append("ultimatum")
                    $ Girl.recent_history.append("stopdancing")
                    return
            "That's ok, but keep dancing for a bit. . .":
                    if "ultimatum" not in Girl.daily_history:
                            $ Girl.change_stat("love", 50, 2)
                            $ Girl.change_stat("obedience", 50, 2)
                            $ Girl.change_stat("inhibition", 50, 2)
                            $ Girl.daily_history.append("ultimatum")
                    $ Girl.recent_history.append("keepdancing")
                    if "stripforced" in Girl.recent_history:
                            call Anyline(Girl,". . .")
                    else:
                            if Girl == RogueX:
                                    ch_r "Heh, ok [Girl.Petname]."
                            elif Girl == KittyX:
                                    ch_k "Heh, alright."
                            elif Girl == EmmaX:
                                    ch_e "Oh, if I must, [Girl.Petname]."
                            elif Girl == LauraX:
                                    ch_l "Eh? Fine."
                            elif Girl == JeanX:
                                    ch_j "Ok, sure."
                            elif Girl == StormX:
                                    ch_s "Very well. . ."
                            elif Girl == JubesX:
                                    ch_v "Ok, sure. . ."
            "You'd better." if Girl.Forced:
                    if not Approvalcheck(Girl, 500, "O", TabM=5) and not Approvalcheck(Girl, 800, "L", TabM=5):
                            $ Girl.change_face("angry")
                            if Girl == RogueX:
                                    ch_r "I don't know who you think I am, but I ain't gonna just jump when you say \"toad\"."
                                    ch_r "I think we're done here for now."
                            elif Girl == KittyX:
                                    ch_k "I'm not just going to do \"whatever\"!"
                                    ch_k "I'm done with this."
                            elif Girl == EmmaX:
                                    ch_e "I think you're overstepping your bounds here, [Girl.Petname]."
                                    ch_e "Remember your place."
                            elif Girl == LauraX:
                                    ch_l "I don't like that tone, [Girl.Petname]."
                            elif Girl == JeanX:
                                    ch_j "Don't talk to me like that. -I- talk to -you- like that."
                            elif Girl == StormX:
                                    ch_s "I do not appreciate that tone."
                            elif Girl == JubesX:
                                    ch_v "I'd better not break your face either. . ."
                            $ Girl.recent_history.append("angry")
                            $ Girl.daily_history.append("angry")
                            call remove_girl(Girl)
                            return
                    $ temp_modifier += 20
                    $ Girl.Forced += 1
                    $ Girl.change_face("sad")
                    if "stripforced" in Girl.recent_history:
                            $ Girl.change_face("angry")
                            call Anyline(Girl,". . .")
                    else:
                            if Girl == RogueX:
                                    ch_r "I. . . guess I could. . ."
                            elif Girl == KittyX:
                                    ch_k "I. . . could show a bit more. . ."
                            elif Girl == EmmaX:
                                    ch_e "Hmm, forceful. . ."
                            elif Girl == LauraX:
                                    ch_l "Grrrr. . ."
                            elif Girl == JeanX:
                                    ch_j ". . . fine."
                            elif Girl == StormX:
                                    ch_s ". . ."
                            elif Girl == JubesX:
                                    ch_v "Well. . . ok. . ."
                            $ Girl.recent_history.append("stripforced")
                    $ Girl.change_stat("love", 200, -40)
            "You can do better than that. Keep going." if not Girl.Forced:
                    if not Approvalcheck(Girl, 300, "O", TabM=5) and not Approvalcheck(Girl, 700, "L", TabM=5):
                            $ Girl.change_face("angry")
                            if Girl == RogueX:
                                    ch_r "I don't know who you think I am, but I ain't gonna just jump when you say \"toad\"."
                                    ch_r "I think we're done here for now."
                            elif Girl == KittyX:
                                    ch_k "I'm not just going to do \"whatever\"!"
                                    ch_k "I'm done with this."
                            elif Girl == EmmaX:
                                    ch_e "I think you're overstepping your bounds here, [Girl.Petname]."
                                    ch_e "Remember your place."
                            elif Girl == LauraX:
                                    ch_l "I don't like that tone, [Girl.Petname]."
                            elif Girl == JeanX:
                                    ch_j "Don't talk to me like that. -I- talk to -you- like that."
                            elif Girl == StormX:
                                    ch_s "No, I do not think so."
                            elif Girl == JubesX:
                                    ch_v "Oh, I can, but you're not goinna see it. . ."
                            $ Girl.recent_history.append("angry")
                            $ Girl.daily_history.append("angry")
                            call remove_girl(Girl)
                            return
                    $ Girl.change_stat("love", 200, -10)
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_stat("obedience", 75, 5)
                    $ temp_modifier += 20
                    $ Girl.Forced += 1
                    $ Girl.change_face("sad")
                    if Girl == RogueX:
                            ch_r "Well, if you insist. . ."
                    elif Girl == KittyX:
                            ch_k "I mean, maybe. . ."
                    elif Girl == EmmaX:
                            ch_e "I can't imagine doing better than \"perfection\". . ."
                    elif Girl == LauraX:
                            ch_l ". . . Right. . ."
                    elif Girl == JeanX:
                            ch_j "I don't see how anyone could. . ."
                    elif Girl == StormX:
                            ch_s "We shall see. . ."
                    elif Girl == JubesX:
                            ch_v "Ok, how about this. . ."
        if "ultimatum" not in Girl.daily_history:
                    $ Girl.daily_history.append("ultimatum")

        if Girl == RogueX:
                    show Rogue_Sprite at Girl_Dance1(Girl)
        elif Girl == KittyX:
                    show Kitty_Sprite at Girl_Dance1(Girl)
        elif Girl == EmmaX:
                    show Emma_Sprite at Girl_Dance1(Girl)
        elif Girl == LauraX:
                    show Laura_Sprite at Girl_Dance1(Girl)
        elif Girl == JeanX:
                    show Jean_Sprite at Girl_Dance1(Girl)
        elif Girl == StormX:
                    show Storm_Sprite at Girl_Dance1(Girl)
        elif Girl == JubesX:
                    show Jubes_Sprite at Girl_Dance1(Girl)
        "[Girl.name] begins to dance again."
        return
