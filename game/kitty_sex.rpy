﻿# Kitty_SexMenu //////////////////////////////////////////////////////////////////////
label Kitty_SexAct(Act = 0):
        call Shift_Focus(KittyX)
        if AloneCheck(KittyX) and KittyX.Taboo == 20:
                $ KittyX.Taboo = 0
                $ Taboo = 0
        if Act == "SkipTo":
            $ renpy.pop_call() #causes it to skip past the primary_action Swap
            $ renpy.pop_call() #causes it to skip past the cycle you were in before
            #$ renpy.pop_call() #causes it to skip past the sex menu you were in before that
            call SkipTo(KittyX)
        elif Act == "switch":
            $ renpy.pop_call() #causes it to skip past call here from Sex_Menu_Threesome
            #$ renpy.pop_call() #causes it to skip past call to Sex_Menu_Threesome
            # drops through to sex menu
        elif Act == "masturbate":
            call Kitty_M_Prep
            if not action_context:
                return
        elif Act == "lesbian":
            call Les_Prep(KittyX)
            if not action_context:
                return
        elif Act == "kissing":
            call KissPrep(KittyX)
            if not action_context:
                return
        elif Act == "breasts":
            call Kitty_Fondle_Breasts
            if not action_context:
                return
        elif Act == "blow":
            call Kitty_BJ_Prep
            if not action_context:
                return
        elif Act == "hand":
            call Kitty_HJ_Prep
            if not action_context:
                return
        elif Act == "sex":
            call Kitty_SexPrep
            if not action_context:
                return

##  KittyX.Masturbating //////////////////////////////////////////////////////////////////////
# counter 1 means she's seen you, counter 0 means she hasn't.
label Kitty_Masturbate: #(action_context = action_context):
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(KittyX)
    if KittyX.Mast:
        $ temp_modifier += 10
    if KittyX.SEXP >= 50:
        $ temp_modifier += 25
    elif KittyX.SEXP >= 30:
        $ temp_modifier += 15
    elif KittyX.SEXP >= 15:
        $ temp_modifier += 5
    if KittyX.lust >= 90:
        $ temp_modifier += 20
    elif KittyX.lust >= 75:
        $ temp_modifier += 5
    if "exhibitionist" in KittyX.Traits:
        $ temp_modifier += (3*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.Petnames:
        $ temp_modifier += 10
    elif "ex" in KittyX.Traits:
        $ temp_modifier -= 40
    if KittyX.ForcedCount and not KittyX.Forced:
        $ temp_modifier -= 5 * KittyX.ForcedCount

    $ Approval = ApprovalCheck(KittyX, 1300, TabM = 2) # 120, 135, 150, Taboo -80(200)

    $ KittyX.DrainWord("unseen",1,0) #She sees you, so remove unseens

    if action_context == "join":       # This triggers if you ask to join in
                if Approval > 1 or (Approval and KittyX.lust >= 50):
                    $ Player.AddWord(1,"join")
                    menu:
                        extend ""
                        "Would you like some help? I could lend some helping hands. . ."  if Player.Semen and KittyX.Action:
                                $ KittyX.change_stat("love", 90, 1)
                                $ KittyX.change_stat("obedience", 50, 2)
                                $ KittyX.change_face("sexy")
                                ch_k "Um, you know, maybe start up top?"
                                $ KittyX.change_stat("obedience", 70, 2)
                                $ KittyX.change_stat("inhibition", 70, 1)
                                $ offhand_action = "fondle breasts"
                                $ KittyX.Mast += 1
                                jump Kitty_M_Cycle
                        "Would you like some help? I could. . . up to you, I guess." if Player.Semen and KittyX.Action:
                                $ KittyX.change_stat("love", 70, 2)
                                $ KittyX.change_stat("love", 90, 1)
                                $ KittyX.change_face("sexy")
                                ch_k "I'd[KittyX.like]love it if you could give me a hand. . ."
                                $ KittyX.change_stat("obedience", 70, 2)
                                $ KittyX.change_stat("inhibition", 70, 1)
                                $ D20 = renpy.random.randint(1, 20)
                                if D20 > 10:
                                    $ offhand_action = "fondle breasts"
                                else:
                                    $ offhand_action = "suck breasts"
                                $ KittyX.Mast += 1
                                jump Kitty_M_Cycle
                        "Why don't we take care of each other?" if Player.Semen and KittyX.Action:
                                $ KittyX.change_face("sexy")
                                ch_k "I think I could help with that. . ."
                                $ renpy.pop_call()          #removes the call to this label
                                return                      #returns to sexmenu=
                        "You look like you have things well in hand. . .":
                                if KittyX.lust >= 50:
                                    $ KittyX.change_stat("love", 70, 2)
                                    $ KittyX.change_stat("love", 90, 1)
                                    $ KittyX.change_face("sexy")
                                    ch_k "Well {i}I{/i} think so. . ."
                                    $ KittyX.change_stat("obedience", 80, 3)
                                    $ KittyX.change_stat("inhibition", 80, 5)
                                    jump Kitty_M_Cycle
                                elif ApprovalCheck(KittyX, 1200):
                                    $ KittyX.change_face("sly")
                                    ch_k "Yeah. . . but I think I'm kinda done. . ."
                                else:
                                    $ KittyX.change_face("angry")
                                    ch_k "Hrmph, yeah, I kinda {i}did.{/i}"

                #else: You've failed all checks so she kicks you out.
                $ KittyX.ArmPose = 1
                $ KittyX.OutfitChange()
                $ KittyX.Action -= 1
                $ Player.change_stat("Focus", 50, 30)
                call Checkout(1)
                $ line = 0
                $ action_context = 0
                $ renpy.pop_call()          #removes the call to this label
                if Approval:
                        $ KittyX.change_face("bemused", 2)
                        if bg_current == "bg_kitty":
                            ch_k "So what are you[KittyX.like]even doing here?"
                        else:
                            ch_k "I[KittyX.like]didn't expect to see you here. . ."
                        $ KittyX.Blush = 1
                else:
                        $ KittyX.change_stat("love", 200, -5)
                        $ KittyX.change_face("angry")
                        $ KittyX.recent_history.append("angry")
                        $ KittyX.daily_history.append("angry")
                        if bg_current == "bg_kitty":
                            ch_k "So in case you couldn't tell, I was a little {i}busy?{/i} Maybe knock sometime?"
                            "[KittyX.name] kicks you out of her room."
                            $ renpy.pop_call()
                            jump Campus_Map
                        else:
                            ch_k "So. . . I'm getting out of here? Maybe knock sometime?"
                            hide Kitty_Sprite with easeoutbottom
                            call Remove_Girl(KittyX)
                return                      #returns to sexmenu, which returns to original
    #End of "Join" option



    if action_context == KittyX:                                                                  #Kitty auto-starts
                if Approval > 2:                                                      # fix, add kitty auto stuff here
                        if KittyX.wearing_skirt:
                            "[KittyX.name]'s hand snakes down her body, and hikes up her skirt."
                            $ KittyX.Upskirt = 1
                        elif KittyX.PantsNum() > 6:
                            "[KittyX.name] slides her hand down her body and into her jeans."
                        elif KittyX.HoseNum() >= 5:
                            "[KittyX.name]'s hand slides down her body and under her [KittyX.Hose]."
                        elif KittyX.Panties:
                            "[KittyX.name]'s hand slides down her body and under her [KittyX.Panties]."
                        else:
                            "[KittyX.name]'s hand slides down her body and begins to caress her pussy."
                        $ KittyX.SeenPanties = 1
                        "She starts to slowly rub herself."
                        call Kitty_First_Bottomless
                        menu:
                            "What do you do?"
                            "Nothing.":
                                    $ KittyX.change_stat("inhibition", 80, 3)
                                    $ KittyX.change_stat("inhibition", 60, 2)
                                    "[KittyX.name] begins to masturbate."
                            "Go for it.":
                                    $ KittyX.change_face("sexy, 1")
                                    $ KittyX.change_stat("inhibition", 80, 3)
                                    ch_p "That is so sexy, [KittyX.Pet]."
                                    $ KittyX.nameCheck() #checks reaction to petname
                                    "You lean back and enjoy the show."
                                    $ KittyX.change_stat("love", 80, 1)
                                    $ KittyX.change_stat("obedience", 90, 1)
                                    $ KittyX.change_stat("obedience", 50, 2)
                            "Ask her to stop.":
                                    $ KittyX.change_face("surprised")
                                    $ KittyX.change_stat("inhibition", 70, 1)
                                    ch_p "Let's not do that right now, [KittyX.Pet]."
                                    $ KittyX.nameCheck() #checks reaction to petname
                                    "[KittyX.name] pulls her hands away from herself."
                                    $ KittyX.OutfitChange()
                                    $ KittyX.change_stat("obedience", 90, 1)
                                    $ KittyX.change_stat("obedience", 50, 1)
                                    $ KittyX.change_stat("obedience", 30, 2)
                                    return
                        jump Kitty_M_Prep
                else:
                        $ temp_modifier = 0                               # fix, add kitty auto stuff here
                        $ offhand_action = 0
                return
    #End if Kitty intitiates this action

    #first time
    if not KittyX.Mast:
            $ KittyX.change_face("surprised", 1)
            $ KittyX.Mouth = "kiss"
            ch_k "You want me to. . . touch myself?"
            ch_k "And you're going to . . .watch?"
            if KittyX.Forced:
                $ KittyX.change_face("sad")
                ch_k "So you {i}just{/i} want to watch. . ."


    #First time dialog
    if not KittyX.Mast and Approval:
            if KittyX.Forced:
                $ KittyX.change_face("sad")
                $ KittyX.change_stat("love", 70, -3, 1)
                $ KittyX.change_stat("love", 20, -2, 1)
            elif KittyX.love >= KittyX.obedience and KittyX.love >= KittyX.inhibition:
                $ KittyX.change_face("sexy")
                $ KittyX.Brows = "sad"
                $ KittyX.Mouth = "smile"
                ch_k "This is kind of {i}intimate{/i} . . ."
            elif KittyX.obedience >= KittyX.inhibition:
                $ KittyX.change_face("normal")
                ch_k "Ok by me, [KittyX.Petname]. . ."
            else: # Uninhibited
                $ KittyX.change_face("sad")
                $ KittyX.Mouth = "smile"
                ch_k "This could be kinda fun . . ."


    #Second time+ initial dialog
    elif Approval:
            if KittyX.Forced:
                $ KittyX.change_face("sad")
                $ KittyX.change_stat("love", 70, -3, 1)
                $ KittyX.change_stat("love", 20, -2, 1)
                ch_k "Again? Just looking?"
            elif Approval and "masturbation" in KittyX.recent_history:
                $ KittyX.change_face("sexy", 1)
                ch_k "I guess I could give it another go. . ."
                jump Kitty_M_Prep
            elif Approval and "masturbation" in KittyX.daily_history:
                $ KittyX.change_face("sexy", 1)
                $ line = renpy.random.choice(["Was it that good?",
                    "Didn't get enough earlier?",
                    "I kinda liked the audience. . ."])
                ch_k "[line]"
            elif KittyX.Mast < 3:
                $ KittyX.change_face("sexy", 1)
                $ KittyX.Brows = "confused"
                ch_k "Did you. . . like it last time?"
            else:
                $ KittyX.change_face("sexy", 1)
                $ KittyX.ArmPose = 2
                $ line = renpy.random.choice(["You really like to watch.",
                    "Again?",
                    "You like to watch me.",
                    "You want me to get myself off?"])
                ch_k "[line]"
                $ line = 0
    #End second time+ initial dialog

    #If she's into it. . .
    if Approval >= 2:
            if KittyX.Forced:
                $ KittyX.change_face("sad")
                $ KittyX.change_stat("obedience", 90, 1)
                $ KittyX.change_stat("inhibition", 60, 1)
                ch_k "Fine. . ."
            else:
                $ KittyX.change_face("sexy", 1)
                $ KittyX.change_stat("love", 90, 1)
                $ KittyX.change_stat("inhibition", 50, 3)
                $ line = renpy.random.choice(["Huh. Ok.",
                    "Couldn't hurt having you around. . .",
                    "Two birds with one stone. . .",
                    "K.",
                    "Sure, why not?",
                    "Lol, ok."])
                ch_k "[line]"
                $ line = 0
            $ KittyX.change_stat("obedience", 20, 1)
            $ KittyX.change_stat("obedience", 60, 1)
            $ KittyX.change_stat("inhibition", 70, 2)
            jump Kitty_M_Prep

    #If she's not into it, but maybe. . .
    else:
        menu:
            ch_k "That's. . . private? You know?"
            "Maybe later?":
                        $ KittyX.change_face("sexy", 1)
                        if KittyX.lust > 70:
                            ch_k "Well, I know what {i}I'll{/i} be doing later. Not sure if you can come."
                            ch_k "I mean-  you know, be there."
                            ch_k "I'm not sure you'll {i}be{/i} there."
                            ch_k ". . .coming."
                        else:
                            ch_k "Hmm, maybe. . . I'll text you?"
                        $ KittyX.change_stat("love", 80, 2)
                        $ KittyX.change_stat("inhibition", 70, 2)
                        return
            "You look like you could use it. . .":
                    if Approval:
                        $ KittyX.change_face("sexy")
                        $ KittyX.change_stat("obedience", 90, 2)
                        $ KittyX.change_stat("obedience", 50, 2)
                        $ KittyX.change_stat("inhibition", 70, 3)
                        $ KittyX.change_stat("inhibition", 40, 2)
                        $ line = renpy.random.choice(["Huh. Ok.",
                                "Couldn't hurt having you around. . .",
                                "Two birds with one stone. . .",
                                "K.",
                                "Sure, why not?",
                                "Lol, ok."])
                        ch_k "[line]"
                        $ line = 0
                        jump Kitty_M_Prep

            "Just get at it already.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(KittyX, 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                    if Approval > 1 or (Approval and KittyX.Forced):
                        $ KittyX.change_face("sad")
                        $ KittyX.change_stat("love", 70, -5, 1)
                        $ KittyX.change_stat("love", 200, -5)
                        ch_k "Fiiine, geeze."
                        $ KittyX.change_stat("obedience", 80, 4)
                        $ KittyX.change_stat("inhibition", 80, 1)
                        $ KittyX.change_stat("inhibition", 60, 3)
                        $ KittyX.Forced = 1
                        jump Kitty_M_Prep
                    else:
                        $ KittyX.change_stat("love", 200, -20)
                        $ KittyX.recent_history.append("angry")
                        $ KittyX.daily_history.append("angry")
    # end of asking her to do it

    #She refused all offers.
    $ KittyX.ArmPose = 1
    if KittyX.Forced:
            $ KittyX.change_face("angry", 1)
            ch_k "I. . . can't, not with you watching."
            $ KittyX.change_stat("lust", 90, 5)
            if KittyX.love > 300:
                $ KittyX.change_stat("love", 70, -2)
            $ KittyX.change_stat("obedience", 50, -2)
            $ KittyX.recent_history.append("angry")
            $ KittyX.daily_history.append("angry")
            $ KittyX.recent_history.append("no masturbation")
            $ KittyX.daily_history.append("no masturbation")
            return
    elif Taboo:                             # she refuses and this is too public a place for her
            $ KittyX.change_face("angry", 1)
            $ KittyX.daily_history.append("tabno")
            ch_k "Certainly not here!"
            $ KittyX.change_stat("lust", 90, 5)
            $ KittyX.change_stat("obedience", 50, -3)
            return
    elif KittyX.Mast:
            $ KittyX.change_face("sad")
            ch_k "Sorry, maybe try a porn game or something."
    else:
            $ KittyX.change_face("normal", 1)
            ch_k "Um, no."
    $ KittyX.recent_history.append("no masturbation")
    $ KittyX.daily_history.append("no masturbation")
    $ temp_modifier = 0
    return

label Kitty_M_Prep:
    $ KittyX.Upskirt = 1
    $ KittyX.PantiesDown = 1
    call Kitty_First_Bottomless(1)
    call set_the_scene(Dress=0)

    #if she hasn't seen you yet. . .
    if "unseen" in KittyX.recent_history:
            $ KittyX.change_face("sexy")
            $ KittyX.Eyes = "closed"
            $ KittyX.ArmPose = 2
            "You see [KittyX.name] leaning back, masturbating. You don't think she's noticed you yet."
    else:
            $ KittyX.change_face("sexy")
            $ KittyX.ArmPose = 2
            "[KittyX.name] lays back and starts to toy with herself."
            if not KittyX.Mast:#First time
                    if KittyX.Forced:
                        $ KittyX.change_stat("love", 90, -20)
                        $ KittyX.change_stat("obedience", 70, 45)
                        $ KittyX.change_stat("inhibition", 80, 35)
                    else:
                        $ KittyX.change_stat("love", 90, 15)
                        $ KittyX.change_stat("obedience", 70, 35)
                        $ KittyX.change_stat("inhibition", 80, 40)


    $ primary_action = "masturbation"
    if not girl_offhand_action:
        $ girl_offhand_action = "fondle pussy"
    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ line = 0
    if Taboo:
        $ KittyX.DrainWord("tabno")
    $ KittyX.DrainWord("no masturbation")
    $ KittyX.recent_history.append("masturbation")
    $ KittyX.daily_history.append("masturbation")

label Kitty_M_Cycle:
    if action_context == "join":
        $ renpy.pop_call()
        $ action_context = 0

    while Round > 0:
        call Kitty_Pos_Reset("masturbation")
        call Shift_Focus(KittyX)
        $ KittyX.lustFace()
        if "unseen" in KittyX.recent_history:
                $ KittyX.Eyes = "closed"

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep Watching.":
                                pass

                        "[KittyX.name]. . .[[jump in]" if "unseen" not in KittyX.recent_history and "join" not in Player.recent_history and KittyX.Loc == bg_current:
                                "[KittyX.name] slows what she's doing with a sly grin."
                                ch_k "Like what you see?"
                                $ action_context = "join"
                                call Kitty_Masturbate
                        "\"Ahem. . .\"" if "unseen" in KittyX.recent_history and KittyX.Loc == bg_current:
                                jump Kitty_M_Interupted

                        "Start jack'in it." if offhand_action != "jackin":
                                call Jackin(KittyX)
                        "Stop jack'in it." if offhand_action == "jackin":
                                $ offhand_action = 0

                        "Slap her ass" if KittyX.Loc == bg_current:
                                if "unseen" in KittyX.recent_history:
                                        "You smack [KittyX.name] firmly on the ass!"
                                        jump Kitty_M_Interupted
                                else:
                                        call Slap_Ass(KittyX)
                                        $ counter += 1
                                        $ Round -= 1
                                        jump Kitty_M_Cycle

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
                                    "Offhand action" if KittyX.Loc == bg_current:
                                            if KittyX.Action and MultiAction:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ KittyX.Action -= 1
                                            else:
                                                ch_k "I'm actually getting a little tired, so maybe we could wrap this up?"

                                    "Threesome actions (locked)" if not Partner or "unseen" in KittyX.recent_history or KittyX.Loc != bg_current:
                                        pass
                                    "Threesome actions" if Partner and "unseen" not in KittyX.recent_history and KittyX.Loc == bg_current:
                                        menu:
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(KittyX)
                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(KittyX)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Kitty_M_Cycle
                                            "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Kitty_M_Cycle
                                            "Never mind":
                                                        jump Kitty_M_Cycle

                                    "Show her feet" if not ShowFeet and (KittyX.Pose == "doggy" or KittyX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (KittyX.Pose == "doggy" or KittyX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [KittyX.name]":
                                            if "unseen" in KittyX.recent_history:
                                                    ch_p "Oh, yeah, take it off. . ."
                                                    jump Kitty_M_Interupted
                                            else:
                                                    call Girl_Undress(KittyX)
                                    "Clean up [KittyX.name] (locked)" if not KittyX.Spunk:
                                            pass
                                    "Clean up [KittyX.name]" if KittyX.Spunk:
                                            if "unseen" in KittyX.recent_history:
                                                    ch_p "You've got a little something on you. . ."
                                                    jump Kitty_M_Interupted
                                            else:
                                                    call Girl_Cleanup(KittyX,"ask")
                                    "Never mind":
                                            jump Kitty_M_Cycle

                        "Back to Sex Menu" if MultiAction and KittyX.Loc == bg_current:
                                    ch_p "Let's try something else."
                                    call Kitty_Pos_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Kitty_M_Interupted
                        "End Scene" if not MultiAction or KittyX.Loc != bg_current:
                                    ch_p "Let's stop for now."
                                    call Kitty_Pos_Reset
                                    $ line = 0
                                    jump Kitty_M_Interupted
        #End menu (if line)

        call Shift_Focus(KittyX)
        call Sex_Dialog(KittyX,Partner)

        #If either of you could cum

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up

        if Player.Focus >= 100 or KittyX.lust >= 100:
                    #If you can cum:
                    if Player.Focus >= 100:
                        if "unseen" not in KittyX.recent_history:
                            #if she knows you're there
                            call Player_Cumming(KittyX)
                            if "angry" in KittyX.recent_history:
                                call Kitty_Pos_Reset
                                return
                            $ KittyX.change_stat("lust", 200, 5)
                            if 100 > KittyX.lust >= 70 and KittyX.OCount < 2:
                                $ KittyX.recent_history.append("unsatisfied")
                                $ KittyX.daily_history.append("unsatisfied")
                            $ line = "came"
                        else: #If she wasn't aware you were there
                            "You grunt and try to hold it in."
                            $ Player.Focus = 95
                            if KittyX.Loc == bg_current:
                                    jump Kitty_M_Interupted

                    #If Kitty can cum
                    if KittyX.lust >= 100:
                        call Girl_Cumming(KittyX)
                        if KittyX.Loc == bg_current:
                                jump Kitty_M_Interupted

                    if line == "came":
                        $ line = 0
                        if not Player.Semen:
                            "You're emptied out, you should probably take a break."
                            $ offhand_action = 0 if offhand_action == "jackin" else offhand_action


                        if "unsatisfied" in KittyX.recent_history:#And Kitty is unsatisfied,
                            "[KittyX.name] still seems a bit unsatisfied with the experience."
                            menu:
                                "Let her keep going?"
                                "Yes, keep going for a bit.":
                                    $ line = "You let her get back into it"
                                    jump Kitty_M_Cycle
                                "No, I'm done.":
                                    "You ask her to stop."
                                    return
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        if "unseen" in KittyX.recent_history:
                if Round == 10:
                    "It's getting a bit late, [KittyX.name] will probably be wrapping up soon."
                elif Round == 5:
                    "She's definitely going to stop soon."
        else:
                if KittyX.Loc == bg_current:
                        call Escalation(KittyX) #sees if she wants to escalate things

                if Round == 10:
                    ch_k "We might want to wrap this up, it's getting late."
                    $ KittyX.lust += 10
                elif Round == 5:
                    ch_k "Seriously, it'll be time to stop soon."
                    $ KittyX.lust += 25

    #Round = 0 loop breaks
    $ KittyX.change_face("bemused", 0)
    $ line = 0
    if "unseen" not in KittyX.recent_history:
        ch_k "Ok, I'm kinda done for now, I need a break."

label Kitty_M_Interupted:

    # If she hasn't noticed you're there before cumming
    if "unseen" in KittyX.recent_history:
                $ KittyX.change_face("surprised", 2)
                "[KittyX.name] stops what she's doing with a start, eyes wide."
                call Kitty_First_Bottomless(1)
                $ KittyX.change_face("surprised", 2)

                #If you've been jacking it
                if offhand_action == "jackin":
                        ch_k "Eeep!"
                        ch_k "When did you get here?!"
                        $ KittyX.Eyes = "down"
                        menu:
                            ch_k "And um. . . your cock is out. . . "
                            "A while back, it was an excellent show.":
                                    $ KittyX.change_face("sexy",1)
                                    $ KittyX.change_stat("obedience", 50, 3)
                                    $ KittyX.change_stat("obedience", 70, 2)
                                    ch_k "Um, I mean. . . yeah. . ."
                                    if KittyX.love >= 800 or KittyX.obedience >= 500 or KittyX.inhibition >= 500:
                                        $ temp_modifier += 10
                                        $ KittyX.change_stat("lust", 90, 5)
                                        ch_k "I um. . . like what I'm seeing too. . ."

                            "I. . . just got here?":
                                    $ KittyX.change_face("angry",1)
                                    $ KittyX.change_stat("love", 70, 2)
                                    $ KittyX.change_stat("love", 90, 1)
                                    $ KittyX.change_stat("obedience", 50, 2)
                                    $ KittyX.change_stat("obedience", 70, 2)
                                    "She looks pointedly at your cock,"
                                    ch_k "Long enough to whip that out?"
                                    if KittyX.love >= 800 or KittyX.obedience >= 500 or KittyX.inhibition >= 500:
                                            $ temp_modifier += 10
                                            $ KittyX.change_stat("lust", 90, 5)
                                            $ KittyX.change_face("bemused", 1)
                                            ch_k "I, um, guess I should be flattered?"
                                    else:
                                            $ temp_modifier -= 10
                                            $ KittyX.change_stat("lust", 200, -5)
                        call Seen_First_Peen(KittyX,Partner)
                        ch_k "Hmm. . ."

                #you haven't been jacking it
                else:
                        ch_k "Eeep!"
                        ch_k "When did you get here?!"
                        menu:
                            extend ""
                            "A while back.":
                                    $ KittyX.change_face("sexy", 1)
                                    $ KittyX.change_stat("obedience", 50, 3)
                                    $ KittyX.change_stat("obedience", 70, 2)
                                    ch_k "I hope I kept you entertained. . ."
                            "I just got here.":
                                    $ KittyX.change_face("bemused", 1)
                                    $ KittyX.change_stat("love", 70, 2)
                                    $ KittyX.change_stat("love", 90, 1)
                                    ch_k "Yeah, I just bet. . ."
                                    $ KittyX.change_stat("obedience", 50, 2)
                                    $ KittyX.change_stat("obedience", 70, 2)

                $ KittyX.DrainWord("unseen",1,0) #She sees you, so remove unseens
                $ KittyX.Mast += 1
                if Round <= 10:
                    ch_k "It's getting kinda late to do anything about it. . ."
                    return
                $ action_context = "join"
                call Kitty_Masturbate
                "error: report this if you see it."
                return #should be redundant
    #End Unseen

    #else, if She's seen you already
    $ KittyX.Action -= 1
    $ KittyX.Mast += 1
    call Checkout
    if action_context == "shift":
        $ action_context = 0
        return
    $ action_context = 0

    call Partner_Like(KittyX,3)

    if KittyX.Loc != bg_current:
        return

    if Round <= 10:
            ch_k "Gimme a minute, I need to collect myself here. . ."
            return
    $ KittyX.change_face("sexy", 1)
    if KittyX.lust < 20:
        ch_k "Well that worked for me, how 'bout you?"
    else:
        ch_k "Um, yeah?"
    menu:
        extend ""
        "Well, I have something you could take care of. . ." if Player.Semen and KittyX.Action:
                $ action_context = "shift"
                return
        "You could just keep going. . ." if Player.Semen:
                $ KittyX.change_face("sly")
                if KittyX.Action and Round >= 10:
                    ch_k "Sure. . ."
                    jump Kitty_M_Cycle
                else:
                    ch_k "Gimme a minute, I need to collect myself here. . ."
        "I'm good here. [[Stop]":
                if KittyX.love < 800 and KittyX.inhibition < 500 and KittyX.obedience < 500:
                    $ KittyX.OutfitChange()
                $ KittyX.change_face("normal")
                $ KittyX.Brows = "confused"
                ch_k "Well. . . ok. . ."
                $ KittyX.Brows = "normal"
        "You should probably stop for now." if KittyX.lust > 30:
                $ KittyX.change_face("angry")
                ch_k "I guess? . ."
    return

## end KittyX.Masturbating ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Start Kitty Sex pose //////////////////////////////////////////////////////////////////////////////////
# KittyX.Sex_P //////////////////////////////////////////////////////////////////////

label Kitty_Sex_P:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(KittyX)
    if KittyX.Sex >= 7: # She loves it
        $ temp_modifier += 15
    elif KittyX.Sex >= 3: #You've done it before several times
        $ temp_modifier += 12
    elif KittyX.Sex: #You've done it before
        $ temp_modifier += 10

    if KittyX.Addict >= 75 and (KittyX.CreamP + KittyX.CreamA) >=3: #She's really strung out and has creampied
        $ temp_modifier += 20
    elif KittyX.Addict >= 75:
        $ temp_modifier += 15

    if KittyX.lust > 85:
        $ temp_modifier += 10
    elif KittyX.lust > 75: #She's really horny
        $ temp_modifier += 5

    if action_context == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in KittyX.Traits:
        $ temp_modifier += (4*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.Petnames:
        $ temp_modifier += 10
    elif "ex" in KittyX.Traits:
        $ temp_modifier -= 40
    if KittyX.ForcedCount and not KittyX.Forced:
        $ temp_modifier -= 5 * KittyX.ForcedCount



    if Taboo and "tabno" in KittyX.daily_history:
        $ temp_modifier -= 10

    if "no sex" in KittyX.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no sex" in KittyX.recent_history else 0


    $ Approval = ApprovalCheck(KittyX, 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)

    if action_context == "auto":
                call Kitty_Sex_Launch("sex")
                if KittyX.wearing_skirt:
                    "You press [KittyX.name] down onto her back, sliding her skirt up as you go."
                    $ KittyX.Upskirt = 1
                elif KittyX.PantsNum() > 6:
                    "You press [KittyX.name] down onto her back, sliding her pants down as you do."
                    $ KittyX.Upskirt = 1
                elif KittyX.PantsNum() == 6:
                    "You press [KittyX.name] down onto her back, sliding her shorts down as you do."
                    $ KittyX.Upskirt = 1
                else:
                    "You press [KittyX.name] down onto her back."
                $ KittyX.SeenPanties = 1
                "You rub the tip of your cock against her moist slit."
                $ KittyX.change_face("surprised", 1)

                if (KittyX.Sex and Approval) or (Approval > 1):
                    #this is not the first time you've had sex, or she's into it
                    "[KittyX.name] is briefly startled, but melts into a sly smile."
                    $ KittyX.change_face("sexy")
                    $ KittyX.change_stat("obedience", 70, 3)
                    $ KittyX.change_stat("inhibition", 50, 3)
                    $ KittyX.change_stat("inhibition", 70, 1)
                    ch_k "Oh. . . game on, [KittyX.Petname]."
                    jump Kitty_SexPrep
                else:
                    #she's questioning it
                    $ KittyX.Brows = "angry"
                    menu:
                        ch_k "Um, what do you think you're doing?"
                        "Sorry, sorry! Never mind.":
                            if Approval:
                                    $ KittyX.change_face("sexy", 1)
                                    $ KittyX.change_stat("obedience", 70, 3)
                                    $ KittyX.change_stat("inhibition", 50, 3)
                                    $ KittyX.change_stat("inhibition", 70, 1)
                                    ch_k "{i}Well. . .{/i} I didn't say I didn't want to. . ."
                                    jump Kitty_SexPrep
                            else:
                                    "You pull back before you really get it in."
                                    $ KittyX.change_face("bemused", 1)
                                    if KittyX.Sex:
                                        ch_k "Maybe you could[KittyX.like]warn me?"
                                    else:
                                        ch_k "Maybe you could[KittyX.like]warn me? I don't know that I'm[KittyX.like]ready for that sort of thing. . ."
                        "Just fucking.":
                            $ KittyX.change_stat("love", 80, -10, 1)
                            $ KittyX.change_stat("love", 200, -10)
                            "You press inside some more."
                            $ KittyX.change_stat("obedience", 70, 3)
                            $ KittyX.change_stat("inhibition", 50, 3)
                            if not ApprovalCheck(KittyX, 700, "O", TabM=1):   #Checks if obedience is 700+
                                $ KittyX.change_face("angry")
                                "[KittyX.name] shoves you away and slaps you in the face."
                                ch_k "Jerk!"
                                ch_k "I am not putting up with that shit!"
                                $ KittyX.change_stat("love", 50, -10, 1)
                                $ KittyX.change_stat("obedience", 50, 3)
                                $ renpy.pop_call()
                                if action_context:
                                    $ renpy.pop_call()
                                call Kitty_Sex_Reset
                                $ KittyX.recent_history.append("angry")
                                $ KittyX.daily_history.append("angry")
                            else:
                                $ KittyX.change_face("sad")
                                "[KittyX.name] doesn't seem to be into this, you're lucky she's so obedient."
                                jump Kitty_SexPrep
                return
    #End Auto


    if not KittyX.Sex and "no sex" not in KittyX.recent_history:
            #first time
            $ KittyX.change_face("surprised", 1)
            $ KittyX.Mouth = "kiss"
            ch_k "I haven't really had much experience with this. . . "
            if KittyX.Forced:
                $ KittyX.change_face("sad")
                ch_k "You'd really do this when you have me over a barrel?"


    if not KittyX.Sex and Approval:
            #First time dialog
            if KittyX.Forced:
                $ KittyX.change_face("sad")
                $ KittyX.change_stat("love", 70, -30, 1)
                $ KittyX.change_stat("love", 20, -20, 1)
            elif KittyX.love >= (KittyX.obedience + KittyX.inhibition):
                $ KittyX.change_face("sexy")
                $ KittyX.Brows = "sad"
                $ KittyX.Mouth = "smile"
                ch_k "I don't want you to think I'm some kind of slut. . ."
            elif KittyX.obedience >= KittyX.inhibition:
                $ KittyX.change_face("normal")
                ch_k "I suppose if it's you, [KittyX.Petname]. . ."
            elif KittyX.Addict >= 50:
                $ KittyX.change_face("manic", 1)
                ch_k "I have kind of been hoping you might. . ."
            else: # Uninhibited
                $ KittyX.change_face("sad")
                $ KittyX.Mouth = "smile"
                ch_k "I can't say it hasn't crossed my mind. . ."
            #End first time dialog

    elif Approval:
            #Second time+ dialog
            $ KittyX.change_face("sexy", 1)
            if KittyX.Forced:
                $ KittyX.change_face("sad")
                $ KittyX.change_stat("love", 70, -3, 1)
                $ KittyX.change_stat("love", 20, -2, 1)
                ch_k "Again? Why do you do this to me?"
            elif not Taboo and "tabno" in KittyX.daily_history:
                ch_k "I guess this is more secluded. . ."
            elif "sex" in KittyX.recent_history:
                ch_k "Another round? {i}Fine.{/i}"
                jump Kitty_SexPrep
            elif "sex" in KittyX.daily_history:
                $ line = renpy.random.choice(["Back again so soon?",
                    "So you'd like another round?",
                    "You can't stay away from this. . .",
                    "Didn't get enough earlier?",
                    "You're wearing me out here!"])
                ch_k "[line]"
            elif KittyX.Sex < 3:
                $ KittyX.Brows = "confused"
                $ KittyX.Mouth = "kiss"
                ch_k "So you'd like another round?"
            else:
                $ line = renpy.random.choice(["Oooh, you want some of this?",
                    "So you'd like another round?",
                    "You can't stay away from this. . .",
                    "You gonna make me purr?",
                    "You wanna slide into me?"])
                ch_k "[line]"
            $ line = 0
            #end Second time+ dialog

    if Approval >= 2:
            #She's into it. . .
            if KittyX.Forced:
                $ KittyX.change_face("sad")
                $ KittyX.change_stat("obedience", 90, 1)
                $ KittyX.change_stat("inhibition", 60, 1)
                ch_k "Ok, fiiiiine."
            elif "no sex" in KittyX.daily_history:
                ch_k "You've made your case. . ."
            else:
                $ KittyX.change_face("sexy", 1)
                $ KittyX.change_stat("love", 90, 1)
                $ KittyX.change_stat("inhibition", 50, 3)
                $ line = renpy.random.choice(["Well. . . ok.",
                    "Sure!",
                    "You could, I guess.",
                    "Um, yeah.",
                    "Heh, ok, ok."])
                ch_k "[line]"
                $ line = 0
            $ KittyX.change_stat("obedience", 20, 1)
            $ KittyX.change_stat("obedience", 60, 1)
            $ KittyX.change_stat("inhibition", 70, 2)
            jump Kitty_SexPrep

    else:
            #She's not into it, but maybe. . .
            $ KittyX.change_face("angry")
            if "no sex" in KittyX.recent_history:
                ch_k "I{i}just{/i}[KittyX.like]told you \"no!\""
            elif Taboo and "tabno" in KittyX.daily_history and "no sex" in KittyX.daily_history:
                ch_k "I already told you. . .not in public!"
            elif "no sex" in KittyX.daily_history:
                ch_k "I already[KittyX.like]told you \"no.\""
            elif Taboo and "tabno" in KittyX.daily_history:
                ch_k "I already told you this is too public!"
            elif not KittyX.Sex:
                $ KittyX.change_face("bemused")
                ch_k "I don't know that I'm. . .[KittyX.like]ready? . ."
            else:
                $ KittyX.change_face("bemused")
                ch_k "Maybe[KittyX.like]not right now? . ."
            menu:
                extend ""
                "Sorry, never mind." if "no sex" in KittyX.daily_history:
                        $ KittyX.change_face("bemused")
                        ch_k "It's cool."
                        return
                "Maybe later?" if "no sex" not in KittyX.daily_history:
                        $ KittyX.change_face("sexy")
                        ch_k "Maybe, you never know."
                        $ KittyX.change_stat("love", 80, 2)
                        $ KittyX.change_stat("inhibition", 70, 2)
                        if Taboo:
                            $ KittyX.recent_history.append("tabno")
                            $ KittyX.daily_history.append("tabno")
                        $ KittyX.recent_history.append("no sex")
                        $ KittyX.daily_history.append("no sex")
                        return
                "I think you'd enjoy it as much as I would. . .":
                        if Approval:
                            $ KittyX.change_face("sexy")
                            $ KittyX.change_stat("obedience", 90, 2)
                            $ KittyX.change_stat("obedience", 50, 2)
                            $ KittyX.change_stat("inhibition", 70, 3)
                            $ KittyX.change_stat("inhibition", 40, 2)
                            $ line = renpy.random.choice(["That's. . . true. . .",
                                "I suppose. . .",
                                "That's. . . that's a good point. . ."])
                            ch_k "[line]"
                            $ line = 0
                            jump Kitty_SexPrep
                "Just deal with it.":                                               # Pressured into it
                        $ Approval = ApprovalCheck(KittyX, 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
                        if Approval > 1 or (Approval and KittyX.Forced):
                            $ KittyX.change_face("sad")
                            $ KittyX.change_stat("love", 70, -5, 1)
                            $ KittyX.change_stat("love", 200, -5)
                            ch_k "Well! . .  ok, fine, stick it in."
                            $ KittyX.change_stat("obedience", 80, 4)
                            $ KittyX.change_stat("inhibition", 80, 1)
                            $ KittyX.change_stat("inhibition", 60, 3)
                            $ KittyX.Forced = 1
                            jump Kitty_SexPrep
                        else:
                            $ KittyX.change_stat("love", 200, -20)
                            $ KittyX.recent_history.append("angry")
                            $ KittyX.daily_history.append("angry")
                #end menu
    #end Approval check

    #She refused all offers.
    $ KittyX.ArmPose = 1
    if "no sex" in KittyX.daily_history:
        ch_k "Maybe[KittyX.like]take \"no\" for an answer?"
        $ KittyX.recent_history.append("angry")
        $ KittyX.daily_history.append("angry")
    elif KittyX.Forced:
        $ KittyX.change_face("angry", 1)
        ch_k "Not even."
        $ KittyX.change_stat("lust", 200, 5)
        if KittyX.love > 300:
                $ KittyX.change_stat("love", 70, -2)
        $ KittyX.change_stat("obedience", 50, -2)
        $ KittyX.recent_history.append("angry")
        $ KittyX.daily_history.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ KittyX.change_face("angry", 1)
        $ KittyX.recent_history.append("tabno")
        $ KittyX.daily_history.append("tabno")
        ch_k "I can't believe you'd even consider it around here!"
        $ KittyX.change_stat("lust", 200, 5)
        $ KittyX.change_stat("obedience", 50, -3)
    elif KittyX.Sex:
        $ KittyX.change_face("sad")
        ch_k "Maybe just[KittyX.like]fuck yourself, huh?"
    else:
        $ KittyX.change_face("normal", 1)
        ch_k "Nuhuh."
    $ KittyX.recent_history.append("no sex")
    $ KittyX.daily_history.append("no sex")
    $ temp_modifier = 0
    return

label Kitty_Sex_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(KittyX)
        call Kitty_Sex_Launch("sex")
        $ KittyX.lustFace()
        $ Player.Cock = "in"
        $ primary_action = "sex"
        $ KittyX.Upskirt = 1
        $ KittyX.PantiesDown = 1

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
                                    call Slap_Ass(KittyX)
                                    $ counter += 1
                                    $ Round -= 1
                                    jump Kitty_Sex_Cycle

                        "Turn her Around":
                                    $ KittyX.Pose = "doggy" if KittyX.Pose != "doggy" else "sex"
                                    "You turn her around. . ."
                                    jump Kitty_Sex_Cycle

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
                                            if KittyX.Action and MultiAction:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ KittyX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")

                                    "Shift primary action":
                                            if KittyX.Action and MultiAction:
                                                    menu:
                                                        "How about anal?":
                                                                $ action_context = "shift"
                                                                call Kitty_SexAfter
                                                                call Kitty_Sex_A
                                                        "Just stick it in her ass [[without asking].":
                                                                $ action_context = "auto"
                                                                call Kitty_SexAfter
                                                                call Kitty_Sex_A
                                                        "Pull back to hotdog her.":
                                                                $ action_context = "pullback"
                                                                call Kitty_SexAfter
                                                                call Kitty_Sex_H
                                                        "Never Mind":
                                                                jump Kitty_Sex_Cycle
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [KittyX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(KittyX)
                                            "Ask [KittyX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(KittyX)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(KittyX)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Kitty_Sex_Cycle
                                            "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Kitty_Sex_Cycle
                                            "Never mind":
                                                        jump Kitty_Sex_Cycle
                                    "Just take a look at her.":
                                            $ Player.Cock = 0
                                            $ action_speed = 0

                                    "Show her feet" if not ShowFeet and (KittyX.Pose == "doggy" or KittyX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (KittyX.Pose == "doggy" or KittyX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [KittyX.name]":
                                            call Girl_Undress(KittyX)
                                    "Clean up [KittyX.name] (locked)" if not KittyX.Spunk:
                                            pass
                                    "Clean up [KittyX.name]" if KittyX.Spunk:
                                            call Girl_Cleanup(KittyX,"ask")
                                    "Never mind":
                                            jump Kitty_Sex_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Kitty_Sex_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Kitty_SexAfter
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Kitty_Sex_Reset
                                    $ line = 0
                                    jump Kitty_SexAfter
        #End menu (if line)

        call Shift_Focus(KittyX)
        call Sex_Dialog(KittyX,Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or KittyX.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(KittyX)
                            if "angry" in KittyX.recent_history:
                                call Kitty_Sex_Reset
                                return
                            $ KittyX.change_stat("lust", 200, 5)
                            if 100 > KittyX.lust >= 70 and KittyX.OCount < 2:
                                    $ KittyX.recent_history.append("unsatisfied")
                                    $ KittyX.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Kitty_SexAfter
                            $ line = "came"

                    if KittyX.lust >= 100:
                            #If you're still going at it and Kitty can cum
                            call Girl_Cumming(KittyX)
                            if action_context == "shift" or "angry" in KittyX.recent_history:
                                jump Kitty_SexAfter

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Kitty_SexAfter
                            elif "unsatisfied" in KittyX.recent_history:
                                #And [KittyX.name] is unsatisfied,
                                $ line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ line = "You get back into it"
                                        jump Kitty_Sex_Cycle
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Kitty_SexAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Kitty_SexAfter
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if KittyX.SEXP >= 100 or ApprovalCheck(KittyX, 1200, "LO"):
            pass
        elif counter == (5 + KittyX.Sex):
                    $ KittyX.Brows = "confused"
                    ch_k "So are we[KittyX.like]getting close here?"
        elif counter == (10 + KittyX.Sex):
                    $ KittyX.Brows = "angry"
                    ch_k "I'm . . .getting . . kinda tired. . . here. . ."
                    menu:
                        ch_k "Can we. . . do something. . . else?"
                        "How about a BJ?" if KittyX.Action and MultiAction:
                                $ action_context = "shift"
                                call Kitty_SexAfter
                                call Kitty_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ counter += 1
                                jump Kitty_Sex_Cycle
                        "Let's try something else." if MultiAction:
                                $ line = 0
                                call Kitty_Sex_Reset
                                $ action_context = "shift"
                                jump Kitty_SexAfter
                        "No, get back down there.":
                                if ApprovalCheck(KittyX, 1200) or ApprovalCheck(KittyX, 500, "O"):
                                    $ KittyX.change_stat("love", 200, -5)
                                    $ KittyX.change_stat("obedience", 50, 3)
                                    $ KittyX.change_stat("obedience", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    $ KittyX.change_face("angry", 1)
                                    call Kitty_Sex_Reset
                                    "She scowls at you and pulls out."
                                    ch_k "Not with that attitude, mister!"
                                    $ KittyX.change_stat("love", 50, -3, 1)
                                    $ KittyX.change_stat("love", 80, -4, 1)
                                    $ KittyX.change_stat("obedience", 30, -1, 1)
                                    $ KittyX.change_stat("obedience", 50, -1, 1)
                                    $ KittyX.recent_history.append("angry")
                                    $ KittyX.daily_history.append("angry")
                                    jump Kitty_SexAfter
        #End Count check

        call Escalation(KittyX) #sees if she wants to escalate things

        if Round == 10:
            ch_k "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_k "Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ KittyX.change_face("bemused", 0)
    $ line = 0
    ch_k "Ok, [KittyX.Petname], that's enough of that for now."


# Kitty anal //////////////////////////////////////////////////////////////////////

label Kitty_Sex_A:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(KittyX)
    if KittyX.Anal >= 7: # She loves it
        $ temp_modifier += 20
    elif KittyX.Anal >= 3: #You've done it before several times
        $ temp_modifier += 17
    elif KittyX.Anal: #You've done it before
        $ temp_modifier += 15

    if KittyX.Addict >= 75 and (KittyX.CreamP + KittyX.CreamA) >=3: #She's really strung out and has creampied
        $ temp_modifier += 25
    elif KittyX.Addict >= 75:
        $ temp_modifier += 15

    if KittyX.lust > 85:
        $ temp_modifier += 10
    elif KittyX.lust > 75: #She's really horny
        $ temp_modifier += 5

    if KittyX.Loose:
        $ temp_modifier += 10
    elif "anal" in KittyX.recent_history:
        $ temp_modifier -= 20
    elif "anal" in KittyX.daily_history:
        $ temp_modifier -= 10

    if action_context == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in KittyX.Traits:
        $ temp_modifier += (5*Taboo)

    if KittyX in Player.Harem or "sex friend" in KittyX.Petnames:
        $ temp_modifier += 10
    elif "ex" in KittyX.Traits:
        $ temp_modifier -= 40
    if KittyX.ForcedCount and not KittyX.Forced:
        $ temp_modifier -= 5 * KittyX.ForcedCount

    if Taboo and "tabno" in KittyX.daily_history:
        $ temp_modifier -= 10
    if "no anal" in KittyX.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no anal" in KittyX.recent_history else 0

    $ Approval = ApprovalCheck(KittyX, 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)

    if action_context == "auto":
            call Kitty_Sex_Launch("anal")
            if KittyX.wearing_skirt:
                "You press [KittyX.name] down onto her back, sliding her skirt up as you go."
                $ KittyX.Upskirt = 1
            elif KittyX.PantsNum() > 6:
                "You press [KittyX.name] down onto her back, sliding her pants down as you do."
                $ KittyX.Upskirt = 1
            elif KittyX.PantsNum() == 6:
                "You press [KittyX.name] down onto her back, sliding her shorts down as you do."
                $ KittyX.Upskirt = 1
            else:
                "You press [KittyX.name] down onto her back."
            $ KittyX.SeenPanties = 1
            "You press the tip of your cock against her tight rim."
            $ KittyX.change_face("surprised", 1)

            if (KittyX.Anal and Approval) or (Approval > 1):
                #this is not the first time you've had sex, or she's into it
                $ KittyX.change_stat("obedience", 70, 3)
                $ KittyX.change_stat("inhibition", 50, 3)
                $ KittyX.change_stat("inhibition", 70, 1)
                if KittyX.Loose:
                    "[KittyX.name] is briefly startled, but melts into a sly smile."
                    ch_k "Hmm, stick it in. . ."
                else:
                    "[KittyX.name] is briefly startled, but shrugs."
                    ch_k "Oookay. . ."
                jump Kitty_AnalPrep
            else:
                #she's questioning it
                $ KittyX.Brows = "angry"
                menu:
                    ch_k "Um[KittyX.like]what are you doing back there?!"
                    "Sorry, sorry! Never mind.":
                        if Approval:
                            $ KittyX.change_face("sexy", 1)
                            $ KittyX.change_stat("obedience", 70, 3)
                            $ KittyX.change_stat("inhibition", 50, 3)
                            $ KittyX.change_stat("inhibition", 70, 1)
                            ch_k "Well[KittyX.like]just take it easy, ok? . ."
                            jump Kitty_AnalPrep
                        "You pull back before you really get it in."
                        $ KittyX.change_face("bemused", 1)

                        if KittyX.Anal:
                            ch_k "Maybe you could[KittyX.like]warn me?"
                        else:
                            ch_k "Maybe you could[KittyX.like]warn me? I don't know that I'm[KittyX.like]ready for that sort of thing. . ."
                    "Just fucking.":
                        $ KittyX.change_stat("love", 80, -10, 1)
                        $ KittyX.change_stat("love", 200, -8)
                        "You press into her."
                        $ KittyX.change_stat("obedience", 70, 3)
                        $ KittyX.change_stat("inhibition", 50, 3)
                        if not ApprovalCheck(KittyX, 700, "O", TabM=1):
                            $ KittyX.change_face("angry")
                            "[KittyX.name] shoves you away and slaps you in the face."
                            ch_k "Asshole!"
                            ch_k "You need to ask nicer than that!"
                            $ KittyX.change_stat("love", 50, -10, 1)
                            $ KittyX.change_stat("obedience", 50, 3)
                            $ renpy.pop_call()
                            if action_context:
                                $ renpy.pop_call()
                            call Kitty_Sex_Reset
                            $ KittyX.recent_history.append("angry")
                            $ KittyX.daily_history.append("angry")
                        else:
                            $ KittyX.change_face("sad")
                            "[KittyX.name] doesn't seem to be into this, you're lucky she's so obedient."
                            jump Kitty_AnalPrep
            return
            #end "auto"


    if not KittyX.Anal and "no anal" not in KittyX.recent_history:
            #first time
            $ KittyX.change_face("surprised", 1)
            $ KittyX.Mouth = "kiss"
            ch_k "You want to go in the \"out\" door?!"

            if KittyX.Forced:
                $ KittyX.change_face("sad")
                ch_k "Anal? Really?"

    if not KittyX.Loose and ("dildo anal" in KittyX.daily_history or "anal" in KittyX.daily_history):
            #if she's done anal stuff today
            $ KittyX.change_face("bemused", 1)
            ch_k "I'm not really over the last time, but. . ."
    elif "anal" in KittyX.recent_history:
            $ KittyX.change_face("sexy", 1)
            ch_k "Again? K."
            jump Kitty_AnalPrep


    if not KittyX.Anal and Approval:
            #First time dialog
            if KittyX.Forced:
                $ KittyX.change_face("sad")
                $ KittyX.change_stat("love", 70, -3, 1)
                $ KittyX.change_stat("love", 20, -2, 1)
            elif KittyX.love >= (KittyX.obedience + KittyX.inhibition):
                $ KittyX.change_face("sexy")
                $ KittyX.Brows = "sad"
                $ KittyX.Mouth = "smile"
                ch_k "I guess? . ."
            elif KittyX.obedience >= KittyX.inhibition:
                $ KittyX.change_face("normal")
                ch_k "Well. . ."
            elif KittyX.Addict >= 50:
                $ KittyX.change_face("manic", 1)
                ch_k "I. . . if that's how you want to do it. . . maybe?"
            else: # Uninhibited
                $ KittyX.change_face("sad")
                $ KittyX.Mouth = "smile"
                ch_k "Anything's worth a shot. . ."

    elif Approval:
            #Second time+ dialog
            if KittyX.Forced:
                $ KittyX.change_face("sad")
                $ KittyX.change_stat("love", 70, -3, 1)
                $ KittyX.change_stat("love", 20, -2, 1)
                ch_k "You really ask a lot here. . ."
            elif not Taboo and "tabno" in KittyX.daily_history:
                ch_k "I guess this is out of the way. . ."
            elif "anal" in KittyX.daily_history and not KittyX.Loose:
                pass
            elif "anal" in KittyX.recent_history:
                ch_k "I guess I'm warmed up. . ."
                jump Kitty_AnalPrep
            elif "anal" in KittyX.daily_history:
                $ KittyX.change_face("sexy", 1)
                $ line = renpy.random.choice(["Back again so soon?",
                    "So you'd like another round?",
                    "I'm still a little sore from earlier.",
                    "Didn't get enough earlier?",
                    "You're wearing me out here!"])
                ch_k "[line]"
            else:
                $ KittyX.change_face("sexy", 1)
                $ KittyX.ArmPose = 2
                $ line = renpy.random.choice(["Oooh, you want some of this?",
                    "So you'd like another round?",
                    "I do have booty for days. . .",
                    "You gonna make me purr?",
                    "You wanna slide into me?"])
                ch_k "[line]"
            $ line = 0

    if Approval >= 2:
            #She's into it. . .
            if KittyX.Forced:
                $ KittyX.change_face("sad")
                $ KittyX.change_stat("obedience", 90, 1)
                $ KittyX.change_stat("inhibition", 60, 1)
                ch_k "Ok, fine."
            elif "no anal" in KittyX.daily_history:
                ch_k "Well, ok, I've given it some thought, fine. . ."
            else:
                $ KittyX.change_face("sexy", 1)
                $ KittyX.change_stat("love", 90, 1)
                $ KittyX.change_stat("inhibition", 50, 3)
                $ line = renpy.random.choice(["Well. . . ok.",
                    "Sure!",
                    "You could, I guess.",
                    "Um, yeah.",
                    "Heh, ok, ok."])
                ch_k "[line]"
                $ line = 0
            $ KittyX.change_stat("obedience", 20, 1)
            $ KittyX.change_stat("obedience", 60, 1)
            $ KittyX.change_stat("inhibition", 70, 2)
            jump Kitty_AnalPrep

    else:
            #She's not into it, but maybe. . .
            $ KittyX.change_face("angry")
            if "no anal" in KittyX.recent_history:
                ch_k "I{i}just{/i}[KittyX.like]told you \"no!\""
            elif Taboo and "tabno" in KittyX.daily_history and "no anal" in KittyX.daily_history:
                ch_k "I already told you. . .not in public!"
            elif "no anal" in KittyX.daily_history:
                ch_k "I already[KittyX.like]told you \"no.\""
            elif Taboo and "tabno" in KittyX.daily_history:
                ch_k "I already told you this is too public!"
            elif not KittyX.Anal:
                $ KittyX.change_face("bemused")
                ch_k "I don't know that I'm. . .[KittyX.like]that kind of girl?"
            elif not KittyX.Loose and "anal" not in KittyX.daily_history:
                $ KittyX.change_face("perplexed")
                ch_k "That was kind of. . . rough last time?"
            else:
                $ KittyX.change_face("bemused")
                ch_k "Maybe[KittyX.like]not right now? . ."
            menu:
                extend ""
                "Sorry, never mind." if "no anal" in KittyX.daily_history:
                    $ KittyX.change_face("bemused")
                    ch_k "It's cool."
                    return
                "Maybe later?" if "no anal" not in KittyX.daily_history:
                    $ KittyX.change_face("sexy")
                    ch_k "Maybe, you never know."
                    $ KittyX.change_stat("love", 80, 2)
                    $ KittyX.change_stat("inhibition", 70, 2)
                    if Taboo:
                        $ KittyX.recent_history.append("tabno")
                        $ KittyX.daily_history.append("tabno")
                    $ KittyX.recent_history.append("no anal")
                    $ KittyX.daily_history.append("no anal")
                    return
                "I bet it would feel really good. . .":
                    if Approval:
                        $ KittyX.change_face("sexy")
                        $ KittyX.change_stat("obedience", 90, 2)
                        $ KittyX.change_stat("obedience", 50, 2)
                        $ KittyX.change_stat("inhibition", 70, 3)
                        $ KittyX.change_stat("inhibition", 40, 2)
                        $ line = renpy.random.choice(["That's. . . true. . .",
                            "I suppose. . .",
                            "That's. . . that's a good point. . ."])
                        ch_k "[line]"
                        $ line = 0
                        jump Kitty_AnalPrep
                    else:
                        pass

                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(KittyX, 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
                    if Approval > 1 or (Approval and KittyX.Forced):
                        $ KittyX.change_face("sad")
                        $ KittyX.change_stat("love", 70, -5, 1)
                        $ KittyX.change_stat("love", 200, -5)
                        ch_k "Well! . .  ok, fine, stick it in."
                        $ KittyX.change_stat("obedience", 80, 4)
                        $ KittyX.change_stat("inhibition", 80, 1)
                        $ KittyX.change_stat("inhibition", 60, 3)
                        $ KittyX.Forced = 1
                        jump Kitty_AnalPrep
                    else:
                        $ KittyX.change_stat("love", 200, -20)
                        $ KittyX.recent_history.append("angry")
                        $ KittyX.daily_history.append("angry")

    #She refused all offers.
    $ KittyX.ArmPose = 1
    if "no anal" in KittyX.daily_history:
        ch_k "Maybe[KittyX.like]take \"no\" for an answer?"
        $ KittyX.recent_history.append("angry")
        $ KittyX.daily_history.append("angry")
    elif KittyX.Forced:
        $ KittyX.change_face("angry", 1)
        ch_k "That's a bit much, even for you."
        $ KittyX.change_stat("lust", 200, 5)
        if KittyX.love > 300:
                $ KittyX.change_stat("love", 70, -2)
        $ KittyX.change_stat("obedience", 50, -2)
        $ KittyX.recent_history.append("angry")
        $ KittyX.daily_history.append("angry")
    elif Taboo:
        # she refuses and this is too public a place for her
        $ KittyX.change_face("angry", 1)
        $ KittyX.recent_history.append("tabno")
        $ KittyX.daily_history.append("tabno")
        ch_k "You're being ridiculous. That? Here?!"
        $ KittyX.change_stat("lust", 200, 5)
        $ KittyX.change_stat("obedience", 50, -3)
    elif not KittyX.Loose and "anal" in KittyX.daily_history:
        $ KittyX.change_face("bemused")
        ch_k "I'm[KittyX.like]a little sore here?"
    elif KittyX.Anal:
        $ KittyX.change_face("sad")
        ch_k "That's[KittyX.like]totally off the table."
    else:
        $ KittyX.change_face("normal", 1)
        ch_k "Noooope."
    $ KittyX.recent_history.append("no anal")
    $ KittyX.daily_history.append("no anal")
    $ temp_modifier = 0
    return

label Kitty_Anal_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(KittyX)
        call Kitty_Sex_Launch("anal")
        $ KittyX.lustFace()
        $ Player.Cock = "anal"
        $ primary_action = "anal"

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
                                    call Slap_Ass(KittyX)
                                    $ counter += 1
                                    $ Round -= 1
                                    jump Kitty_Anal_Cycle
                        "Turn her Around":
                                    $ KittyX.Pose = "doggy" if KittyX.Pose != "doggy" else "sex"
                                    "You turn her around. . ."
                                    jump Kitty_Anal_Cycle

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
                                            if KittyX.Action and MultiAction:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ KittyX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")

                                    "Shift primary action":
                                            if KittyX.Action and MultiAction:
                                                    menu:
                                                        "How about sex?":
                                                                $ action_context = "shift"
                                                                call Kitty_AnalAfter
                                                                call Kitty_Sex_P
                                                        "Just stick it in her pussy [[without asking].":
                                                                $ action_context = "auto"
                                                                call Kitty_AnalAfter
                                                                call Kitty_Sex_P
                                                        "Pull back to hotdog her.":
                                                                $ action_context = "pullback"
                                                                call Kitty_AnalAfter
                                                                call Kitty_Sex_H
                                                        "Never Mind":
                                                                jump Kitty_Anal_Cycle
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [KittyX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(KittyX)
                                            "Ask [KittyX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(KittyX)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(KittyX)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Kitty_Anal_Cycle
                                            "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Kitty_Anal_Cycle
                                            "Never mind":
                                                        jump Kitty_Anal_Cycle
                                    "Just take a look at her.":
                                            $ Player.Cock = 0
                                            $ action_speed = 0

                                    "Show her feet" if not ShowFeet and (KittyX.Pose == "doggy" or KittyX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (KittyX.Pose == "doggy" or KittyX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [KittyX.name]":
                                            call Girl_Undress(KittyX)
                                    "Clean up [KittyX.name] (locked)" if not KittyX.Spunk:
                                            pass
                                    "Clean up [KittyX.name]" if KittyX.Spunk:
                                            call Girl_Cleanup(KittyX,"ask")
                                    "Never mind":
                                            jump Kitty_Anal_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Kitty_Sex_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Kitty_AnalAfter
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Kitty_Sex_Reset
                                    $ line = 0
                                    jump Kitty_AnalAfter
        #End menu (if line)

        call Shift_Focus(KittyX)
        call Sex_Dialog(KittyX,Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or KittyX.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(KittyX)
                            if "angry" in KittyX.recent_history:
                                call Kitty_Sex_Reset
                                return
                            $ KittyX.change_stat("lust", 200, 5)
                            if 100 > KittyX.lust >= 70 and KittyX.OCount < 2:
                                    $ KittyX.recent_history.append("unsatisfied")
                                    $ KittyX.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Kitty_AnalAfter
                            $ line = "came"

                    if KittyX.lust >= 100:
                            #If you're still going at it and Kitty can cum
                            call Girl_Cumming(KittyX)
                            if action_context == "shift" or "angry" in KittyX.recent_history:
                                jump Kitty_AnalAfter

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Kitty_AnalAfter
                            elif "unsatisfied" in KittyX.recent_history:
                                #And [KittyX.name] is unsatisfied,
                                $ line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ line = "You get back into it"
                                        jump Kitty_Anal_Cycle
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Kitty_AnalAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Kitty_AnalAfter
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if KittyX.SEXP >= 100 or ApprovalCheck(KittyX, 1200, "LO"):
            pass
        elif counter == (5 + KittyX.Anal):
                    $ KittyX.Brows = "confused"
                    if KittyX.Loose:
                        ch_k "So are we[KittyX.like]getting close here?"
                    else:
                        ch_k "So are we[KittyX.like]getting close here? This is not super pleasant. . ."
        elif counter == (10 + KittyX.Anal):
                    $ KittyX.Brows = "angry"
                    ch_k "I'm . . .getting . . kinda tired. . . of this. . ."
                    menu:
                        ch_k "Can we. . . do something. . . else?"
                        "How about a BJ?" if KittyX.Action and MultiAction:
                                if KittyX.Anal >= 5 and KittyX.Blow >= 10 and KittyX.SEXP >= 50:
                                    $ action_context = "shift"
                                    call Kitty_AnalAfter
                                    call Kitty_Blowjob
                                else:
                                    ch_k "No thanks, [KittyX.Petname]. Maybe a Handy instead?"
                                    $ action_context = "shift"
                                    call Kitty_AnalAfter
                                    call Kitty_HJ_Prep
                        "How about a Handy?" if KittyX.Action and MultiAction:
                                $ action_context = "shift"
                                call Kitty_AnalAfter
                                call Kitty_Handjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ counter += 1
                                jump Kitty_Anal_Cycle
                        "Let's try something else." if MultiAction:
                                $ line = 0
                                call Kitty_Sex_Reset
                                $ action_context = "shift"
                                jump Kitty_AnalAfter
                        "No, get back down there.":
                                if ApprovalCheck(KittyX, 1200) or ApprovalCheck(KittyX, 500, "O"):
                                    $ KittyX.change_stat("love", 200, -5)
                                    $ KittyX.change_stat("obedience", 50, 3)
                                    $ KittyX.change_stat("obedience", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    $ KittyX.change_face("angry", 1)
                                    call Kitty_Sex_Reset
                                    "She scowls at you and pulls out."
                                    ch_k "Not with that attitude, mister!"
                                    $ KittyX.change_stat("love", 50, -3, 1)
                                    $ KittyX.change_stat("love", 80, -4, 1)
                                    $ KittyX.change_stat("obedience", 30, -1, 1)
                                    $ KittyX.change_stat("obedience", 50, -1, 1)
                                    $ KittyX.recent_history.append("angry")
                                    $ KittyX.daily_history.append("angry")
                                    jump Kitty_AnalAfter
        #End Count check

        if Round == 10:
            ch_k "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_k "Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ KittyX.change_face("bemused", 0)
    $ line = 0
    ch_k "Ok, [KittyX.Petname], that's enough of that for now."


# End Kitty Anal //////////////////////////////////////////////////////////////////////////////////



# Kitty hotdog //////////////////////////////////////////////////////////////////////

label Kitty_Sex_H:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(KittyX)
    if KittyX.Hotdog >= 3: #You've done it before several times
        $ temp_modifier += 10
    elif KittyX.Hotdog: #You've done it before
        $ temp_modifier += 5

    if KittyX.lust > 85:
        $ temp_modifier += 10
    elif KittyX.lust > 75: #She's really horny
        $ temp_modifier += 5
    if action_context == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in KittyX.Traits:
        $ temp_modifier += (3*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.Petnames:
        $ temp_modifier += 10
    elif "ex" in KittyX.Traits:
        $ temp_modifier -= 40
    if KittyX.ForcedCount and not KittyX.Forced:
        $ temp_modifier -= 5 * KittyX.ForcedCount

    if Taboo and "tabno" in KittyX.daily_history:
        $ temp_modifier -= 10

    if "no hotdog" in KittyX.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no hotdog" in KittyX.recent_history else 0

    $ Approval = ApprovalCheck(KittyX, 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)

    if action_context == "auto":
            call Kitty_Sex_Launch("hotdog")
            "You press [KittyX.name] down onto her back and press your cock against her."
            $ KittyX.change_face("surprised", 1)

            if (KittyX.Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
                "[KittyX.name] is briefly startled, but melts into a sly smile."
                $ KittyX.change_face("sexy")
                $ KittyX.change_stat("obedience", 70, 3)
                $ KittyX.change_stat("inhibition", 50, 3)
                $ KittyX.change_stat("inhibition", 70, 1)
                ch_k "Hmm, I've apparently got someone's attention. . ."
                jump Kitty_HotdogPrep
            else:                                                                                                            #she's questioning it
                $ KittyX.Brows = "angry"
                menu:
                    ch_k "Hmm, kinda rude, [KittyX.Petname]."
                    "Sorry, sorry! Never mind.":
                        if Approval:
                            $ KittyX.change_face("sexy", 1)
                            $ KittyX.change_stat("obedience", 70, 3)
                            $ KittyX.change_stat("inhibition", 50, 3)
                            $ KittyX.change_stat("inhibition", 70, 1)
                            ch_k "I guess it doesn't feel so bad. . ."
                            jump Kitty_HotdogPrep
                        "You pull back from her."
                        $ KittyX.change_face("bemused", 1)
                        ch_k "Thanks, not that it's {i}so{/i} bad, just maybe ask first?"
                    "You'll see.":
                        $ KittyX.change_stat("love", 80, -10, 1)
                        $ KittyX.change_stat("love", 200, -8)
                        "You grind against her crotch."
                        $ KittyX.change_stat("obedience", 70, 3)
                        $ KittyX.change_stat("inhibition", 50, 3)
                        if not ApprovalCheck(KittyX, 500, "O", TabM=1): #Checks if obedience is 700+
                            $ KittyX.change_face("angry")
                            "[KittyX.name] shoves you away."
                            ch_k "Jerk!"
                            ch_k "I'm not into that!"
                            $ KittyX.change_stat("love", 50, -10, 1)
                            $ KittyX.change_stat("obedience", 50, 3)
                            $ renpy.pop_call()
                            if action_context:
                                $ renpy.pop_call()
                            call Kitty_Sex_Reset
                            $ KittyX.recent_history.append("angry")
                            $ KittyX.daily_history.append("angry")
                        else:
                            $ KittyX.change_face("sad")
                            "[KittyX.name] doesn't seem to be into this, but she knows her place."
                            jump Kitty_HotdogPrep
            return
            #end auto


    if not KittyX.Hotdog and "no hotdog" not in KittyX.recent_history:
            #first time
            $ KittyX.change_face("surprised", 1)
            $ KittyX.Mouth = "kiss"
            ch_k "So, just grinding against me?"

            if KittyX.Forced:
                $ KittyX.change_face("sad")
                ch_k ". . . That's it?"


    if not KittyX.Hotdog and Approval:
            #First time dialog
            if KittyX.Forced:
                $ KittyX.change_face("sad")
                $ KittyX.change_stat("love", 70, -3, 1)
                $ KittyX.change_stat("love", 20, -2, 1)
            elif KittyX.love >= (KittyX.obedience + KittyX.inhibition):
                $ KittyX.change_face("sexy")
                $ KittyX.Brows = "sad"
                $ KittyX.Mouth = "smile"
                ch_k "It does look a bit swolen. . ."
            elif KittyX.obedience >= KittyX.inhibition:
                $ KittyX.change_face("normal")
                ch_k "If you want. . ."
            elif KittyX.Addict >= 50:
                $ KittyX.change_face("manic", 1)
                ch_k "Hmmm. . ."
            else: # Uninhibited
                $ KittyX.change_face("sad")
                $ KittyX.Mouth = "smile"
                ch_k "Hmm, you look ready to go. . ."

    elif Approval:
            #Second time+ dialog
            if KittyX.Forced:
                $ KittyX.change_face("sad")
                $ KittyX.change_stat("love", 70, -3, 1)
                $ KittyX.change_stat("love", 20, -2, 1)
                ch_k "That's {i}all{/i} you want?"
            elif not Taboo and "tabno" in KittyX.daily_history:
                ch_k "I guess this is a better location . ."
            elif "hotdog" in KittyX.recent_history:
                $ KittyX.change_face("sexy", 1)
                ch_k "Again? Ok."
                jump Kitty_HotdogPrep
            elif "hotdog" in KittyX.daily_history:
                $ KittyX.change_face("sexy", 1)
                $ line = renpy.random.choice(["Back again so soon?",
                    "So you'd like another round?",
                    "You're really digging this. . .",
                    "Are you sure that's all you want?"])
                ch_k "[line]"
            else:
                $ KittyX.change_face("sexy", 1)
                $ KittyX.ArmPose = 2
                $ line = renpy.random.choice(["Oooh, you want some of this?",
                    "So you'd like another round?",
                    "You're really digging this. . .",
                    "You want another rub?"])
                ch_k "[line]"
            $ line = 0

    if Approval >= 2:
            #She's into it. . .
            if KittyX.Forced:
                $ KittyX.change_face("sad")
                $ KittyX.change_stat("obedience", 80, 1)
                $ KittyX.change_stat("inhibition", 60, 1)
                ch_k "Ok, fine."
            elif "no hotdog" in KittyX.daily_history:
                ch_k "Well, I guess it's not so bad. . ."
            else:
                $ KittyX.change_face("sexy", 1)
                $ KittyX.change_stat("love", 80, 1)
                $ KittyX.change_stat("inhibition", 50, 2)
                $ line = renpy.random.choice(["Well, sure, give it a rub.",
                    "Well. . . ok.",
                    "Sure!",
                    "I guess we could do that.",
                    "Um, yeah.",
                    "Heh, ok, ok."])
                ch_k "[line]"
                $ line = 0
            $ KittyX.change_stat("obedience", 60, 1)
            $ KittyX.change_stat("inhibition", 70, 2)
            jump Kitty_HotdogPrep

    else:
            #She's not into it, but maybe. . .
            $ KittyX.change_face("angry")
            if "no hotdog" in KittyX.recent_history:
                ch_k "I{i}just{/i}[KittyX.like]told you \"no!\""
            elif Taboo and "tabno" in KittyX.daily_history and "no hotdog" in KittyX.daily_history:
                ch_k "I{i}just{/i}[KittyX.like]told, not in public!"
            elif "no hotdog" in KittyX.daily_history:
                ch_k "I{i}just{/i}[KittyX.like]told you \"no\" earlier!"
            elif Taboo and "tabno" in KittyX.daily_history:
                ch_k "I{i}just{/i}[KittyX.like]told you, not in public!"
            elif not KittyX.Hotdog:
                $ KittyX.change_face("bemused")
                ch_k "That's kinda hot, [KittyX.Petname]. . ."
            else:
                $ KittyX.change_face("bemused")
                ch_k "Not. . . now. . ."
            menu:
                extend ""
                "Sorry, never mind." if "no hotdog" in KittyX.daily_history:
                    $ KittyX.change_face("bemused")
                    ch_k "No problem."
                    return
                "Maybe later?" if "no hotdog" not in KittyX.daily_history:
                    $ KittyX.change_face("sexy")
                    ch_k "Yeah, maybe, [KittyX.Petname]."
                    $ KittyX.change_stat("love", 80, 1)
                    $ KittyX.change_stat("inhibition", 50, 1)
                    if Taboo:
                        $ KittyX.recent_history.append("tabno")
                        $ KittyX.daily_history.append("tabno")
                    $ KittyX.recent_history.append("no hotdog")
                    $ KittyX.daily_history.append("no hotdog")
                    return
                "You might like it. . .":
                    if Approval:
                        $ KittyX.change_face("sexy")
                        $ KittyX.change_stat("obedience", 60, 2)
                        $ KittyX.change_stat("inhibition", 50, 2)
                        $ line = renpy.random.choice(["Well, sure, ok.",
                            "I suppose. . .",
                            "That's. . . that's a good point. . ."])
                        ch_k "[line]"
                        $ line = 0
                        jump Kitty_HotdogPrep
                    else:
                        pass

                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(KittyX, 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                    if Approval > 1 or (Approval and KittyX.Forced):
                        $ KittyX.change_face("sad")
                        $ KittyX.change_stat("love", 70, -2, 1)
                        $ KittyX.change_stat("love", 200, -2)
                        ch_k "Ok, fine. Whatever."
                        $ KittyX.change_stat("obedience", 80, 4)
                        $ KittyX.change_stat("inhibition", 60, 2)
                        $ KittyX.Forced = 1
                        jump Kitty_HotdogPrep
                    else:
                        $ KittyX.change_stat("love", 200, -10)
                        $ KittyX.recent_history.append("angry")
                        $ KittyX.daily_history.append("angry")

    #She refused all offers.
    $ KittyX.ArmPose = 1

    if "no hotdog" in KittyX.daily_history:
        ch_k "I'm just not into that."
        $ KittyX.recent_history.append("angry")
        $ KittyX.daily_history.append("angry")
    if KittyX.Forced:
        $ KittyX.change_face("angry", 1)
        ch_k "Yeah, not happening."
        $ KittyX.change_stat("lust", 200, 5)
        if KittyX.love > 300:
                $ KittyX.change_stat("love", 70, -1)
        $ KittyX.change_stat("obedience", 50, -1)
        $ KittyX.recent_history.append("angry")
        $ KittyX.daily_history.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ KittyX.change_face("angry", 1)
        $ KittyX.recent_history.append("tabno")
        $ KittyX.daily_history.append("tabno")
        ch_k "[KittyX.Like]not here though?"
        $ KittyX.change_stat("lust", 200, 5)
        $ KittyX.change_stat("obedience", 50, -3)
    elif KittyX.Hotdog:
        $ KittyX.change_face("sad")
        ch_k "Yeah, not again."
    else:
        $ KittyX.change_face("normal", 1)
        ch_k "Noooop."
    $ KittyX.recent_history.append("no hotdog")
    $ KittyX.daily_history.append("no hotdog")
    $ temp_modifier = 0
    return

label Kitty_Hotdog_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(KittyX)
        call Kitty_Sex_Launch("hotdog")
        $ KittyX.lustFace()
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
                                    call Slap_Ass(KittyX)
                                    $ counter += 1
                                    $ Round -= 1
                                    jump Kitty_Hotdog_Cycle
                        "Turn her Around":
                                    $ KittyX.Pose = "doggy" if KittyX.Pose != "doggy" else "sex"
                                    "You turn her around. . ."
                                    jump Kitty_Hotdog_Cycle

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
                                            if KittyX.Action and MultiAction:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ KittyX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")

                                    "Shift primary action":
                                            if KittyX.Action and MultiAction:
                                                    menu:
                                                        "How about sex?":
                                                            $ action_context = "shift"
                                                            call Kitty_HotdogAfter
                                                            call Kitty_Sex_P
                                                        "Just stick it in her pussy [[without asking].":
                                                            $ action_context = "auto"
                                                            call Kitty_HotdogAfter
                                                            call Kitty_Sex_P
                                                        "How about anal?":
                                                            $ action_context = "shift"
                                                            call Kitty_HotdogAfter
                                                            call Kitty_Sex_A
                                                        "Just stick it in her ass [[without asking].":
                                                            $ action_context = "auto"
                                                            call Kitty_HotdogAfter
                                                            call Kitty_Sex_A
                                                        "Never Mind":
                                                                jump Kitty_Hotdog_Cycle
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [KittyX.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(KittyX)
                                            "Ask [KittyX.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(KittyX)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(KittyX)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Kitty_Hotdog_Cycle
                                            "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Kitty_Hotdog_Cycle
                                            "Never mind":
                                                        jump Kitty_Hotdog_Cycle
                                    "Just take a look at her.":
                                            $ Player.Cock = 0
                                            $ action_speed = 0

                                    "Show her feet" if not ShowFeet and (KittyX.Pose == "doggy" or KittyX.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Hide her feet" if ShowFeet and (KittyX.Pose == "doggy" or KittyX.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Undress [KittyX.name]":
                                            call Girl_Undress(KittyX)
                                    "Clean up [KittyX.name] (locked)" if not KittyX.Spunk:
                                            pass
                                    "Clean up [KittyX.name]" if KittyX.Spunk:
                                            call Girl_Cleanup(KittyX,"ask")
                                    "Never mind":
                                            jump Kitty_Hotdog_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Kitty_Sex_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Kitty_HotdogAfter
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Kitty_Sex_Reset
                                    $ line = 0
                                    jump Kitty_HotdogAfter
        #End menu (if line)

        call Shift_Focus(KittyX)
        call Sex_Dialog(KittyX,Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or KittyX.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(KittyX)
                            if "angry" in KittyX.recent_history:
                                call Kitty_Sex_Reset
                                return
                            $ KittyX.change_stat("lust", 200, 5)
                            if 100 > KittyX.lust >= 70 and KittyX.OCount < 2:
                                    $ KittyX.recent_history.append("unsatisfied")
                                    $ KittyX.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Kitty_HotdogAfter
                            $ line = "came"

                    if KittyX.lust >= 100:
                            #If you're still going at it and Kitty can cum
                            call Girl_Cumming(KittyX)
                            if action_context == "shift" or "angry" in KittyX.recent_history:
                                jump Kitty_HotdogAfter

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump Kitty_HotdogAfter
                            elif "unsatisfied" in KittyX.recent_history:
                                #And [KittyX.name] is unsatisfied,
                                $ line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if Player.Semen:
                                        $ line = "You get back into it"
                                        jump Kitty_Hotdog_Cycle
                                    "No, I'm done." if Player.Semen:
                                        "You pull back."
                                        jump Kitty_HotdogAfter
                                    "No, I'm spent." if not Player.Semen:
                                        "You pull back."
                                        jump Kitty_HotdogAfter
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if KittyX.SEXP >= 100 or ApprovalCheck(KittyX, 1200, "LO"):
            pass
        elif counter == (5 + KittyX.Hotdog):
                    $ KittyX.Brows = "confused"
                    ch_k "Are you getting close here?"
        elif counter == (10 + KittyX.Hotdog):
                    $ KittyX.Brows = "angry"
                    menu:
                        ch_k "This is getting a bit dull."
                        "How about a BJ?" if KittyX.Action and MultiAction:
                                $ action_context = "shift"
                                call Kitty_HotdogAfter
                                call Kitty_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ counter += 1
                                jump Kitty_Hotdog_Cycle
                        "Let's try something else." if MultiAction:
                                $ line = 0
                                call Kitty_Sex_Reset
                                $ action_context = "shift"
                                jump Kitty_HotdogAfter
                        "No, get back down there.":
                                if ApprovalCheck(KittyX, 1200) or ApprovalCheck(KittyX, 500, "O"):
                                    $ KittyX.change_stat("love", 200, -5)
                                    $ KittyX.change_stat("obedience", 50, 3)
                                    $ KittyX.change_stat("obedience", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    $ KittyX.change_face("angry", 1)
                                    call Kitty_Sex_Reset
                                    "She scowls at you and pulls away."
                                    ch_k "Not with that attitude, mister!"
                                    $ KittyX.change_stat("love", 50, -3, 1)
                                    $ KittyX.change_stat("love", 80, -4, 1)
                                    $ KittyX.change_stat("obedience", 30, -1, 1)
                                    $ KittyX.change_stat("obedience", 50, -1, 1)
                                    $ KittyX.recent_history.append("angry")
                                    $ KittyX.daily_history.append("angry")
                                    jump Kitty_HotdogAfter
        #End Count check

        call Escalation(KittyX) #sees if she wants to escalate things

        if Round == 10:
            ch_k "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_k "Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ KittyX.change_face("bemused", 0)
    $ line = 0
    ch_k "Ok, [KittyX.Petname], that's enough of that for now."
