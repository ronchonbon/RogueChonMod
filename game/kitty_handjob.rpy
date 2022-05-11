## KittyX.Handjob //////////////////////////////////////////////////////////////////////
label Kitty_Handjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(KittyX)
    if KittyX.Hand >= 7: # She loves it
        $ temp_modifier += 10
    elif KittyX.Hand >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif KittyX.Hand: #You've done it before
        $ temp_modifier += 3

    if KittyX.Addict >= 75 and KittyX.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 15
    if KittyX.Addict >= 75:
        $ temp_modifier += 5

    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in KittyX.Traits:
        $ temp_modifier += (3*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.Petnames:
        $ temp_modifier += 10
    elif "ex" in KittyX.Traits:
        $ temp_modifier -= 40
    if KittyX.ForcedCount and not KittyX.Forced:
        $ temp_modifier -= 5 * KittyX.ForcedCount

    if Taboo and "tabno" in KittyX.DailyActions:
        $ temp_modifier -= 10

    if "no hand" in KittyX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no hand" in KittyX.RecentActions else 0

    $ Approval = ApprovalCheck(KittyX, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if not KittyX.Hand and "no hand" not in KittyX.RecentActions:
        $ KittyX.FaceChange("confused", 2)
        ch_k "So you want a handy then?"
        $ KittyX.Blush = 1

    if not KittyX.Hand and Approval:                                                 #First time dialog
        if KittyX.Forced:
            $ KittyX.FaceChange("sad",1)
            $ KittyX.Statup("Love", 70, -3, 1)
            $ KittyX.Statup("Love", 20, -2, 1)
        elif KittyX.Love >= (KittyX.Obed + KittyX.Inbt):
            $ KittyX.FaceChange("sexy",1)
            $ KittyX.Brows = "sad"
            $ KittyX.Mouth = "smile"
            ch_k "I guess it could be interesting. . ."
        elif KittyX.Obed >= KittyX.Inbt:
            $ KittyX.FaceChange("normal",1)
            ch_k "If you want, [KittyX.Petname]. . ."
        elif KittyX.Addict >= 50:
            $ KittyX.FaceChange("manic", 1)
            ch_k "I kind of {i}need{/i} to. . ."
        else: # Uninhibited
            $ KittyX.FaceChange("lipbite",1)
            ch_k "I guess. . ."

    elif Approval:                                                                       #Second time+ dialog
        if KittyX.Forced:
            $ KittyX.FaceChange("sad")
            $ KittyX.Statup("Love", 70, -3, 1)
            $ KittyX.Statup("Love", 20, -2, 1)
            ch_k "That's it, right?"
        elif not Taboo and "tabno" in KittyX.DailyActions:
            ch_k "Well, I guess if it's here. . ."
        elif "hand" in KittyX.RecentActions:
            $ KittyX.FaceChange("sexy", 1)
            ch_k "You're giving me carpal tunnel. . ."
            jump Kitty_HJ_Prep
        elif "hand" in KittyX.DailyActions:
            $ KittyX.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Another one?",
                "You're going to give me calluses.",
                "Didn't get enough earlier?",
                "My hand's kinda sore from earlier.",
                "My hand's kinda sore from earlier."])
            ch_k "[Line]"
        elif KittyX.Hand < 3:
            $ KittyX.FaceChange("sexy", 1)
            $ KittyX.Brows = "confused"
            $ KittyX.Mouth = "kiss"
            ch_k "Hmm, magic fingers. . ."
        else:
            $ KittyX.FaceChange("sexy", 1)
            $ KittyX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this?",
                "So you'd like another handy?",
                "A little. . . [fist pumping hand gestures]?",
                "A little TLC?"])
            ch_k "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if KittyX.Forced:
            $ KittyX.FaceChange("sad")
            $ KittyX.Statup("Obed", 90, 1)
            $ KittyX.Statup("Inbt", 60, 1)
            ch_k "Ok, fine."
        elif "no hand" in KittyX.DailyActions:
            ch_k "OK, geeze!"
        else:
            $ KittyX.FaceChange("sexy", 1)
            $ KittyX.Statup("Love", 90, 1)
            $ KittyX.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Sure, I guess.",
                "Ooooookay.",
                "Cool, lemme see it.",
                "I guess I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Heh, ok, ok."])
            ch_k "[Line]"
            $ Line = 0
        $ KittyX.Statup("Obed", 20, 1)
        $ KittyX.Statup("Obed", 60, 1)
        $ KittyX.Statup("Inbt", 70, 2)
        jump Kitty_HJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ KittyX.FaceChange("angry")
        if "no hand" in KittyX.RecentActions:
            ch_k "You don't[KittyX.like]listen do you, [KittyX.Petname]."
        elif Taboo and "tabno" in KittyX.DailyActions and "no hand" in KittyX.DailyActions:
            ch_k "I said not in public!"
        elif "no hand" in KittyX.DailyActions:
            ch_k "I told you \"no,\" [KittyX.Petname]."
        elif Taboo and "tabno" in KittyX.DailyActions:
            ch_k "I said not in public!"
        elif not KittyX.Hand:
            $ KittyX.FaceChange("bemused")
            ch_k "I don't know, [KittyX.Petname]. . ."
        else:
            $ KittyX.FaceChange("bemused")
            ch_k "Not now, ok?"
        menu:
            extend ""
            "Sorry, never mind." if "no hand" in KittyX.DailyActions:
                $ KittyX.FaceChange("bemused")
                ch_k "Yeah."
                return
            "Maybe later?" if "no hand" not in KittyX.DailyActions:
                $ KittyX.FaceChange("sexy")
                ch_k ". . ."
                ch_k "Maybe."
                $ KittyX.Statup("Love", 80, 2)
                $ KittyX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ KittyX.RecentActions.append("tabno")
                    $ KittyX.DailyActions.append("tabno")
                $ KittyX.RecentActions.append("no hand")
                $ KittyX.DailyActions.append("no hand")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ KittyX.FaceChange("sexy")
                    $ KittyX.Statup("Obed", 90, 2)
                    $ KittyX.Statup("Obed", 50, 2)
                    $ KittyX.Statup("Inbt", 70, 3)
                    $ KittyX.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Sure, I guess.",
                            "Ooooookay.",
                            "Cool, lemme see it.",
                            "I guess I could. . .",
                            "Ok. . . [She gestures for you to come over].",
                            "Heh, ok, ok."])
                    ch_k "[Line]"
                    $ Line = 0
                    jump Kitty_HJ_Prep
                else:
                    pass

            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck(KittyX, 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and KittyX.Forced):
                    $ KittyX.FaceChange("sad")
                    $ KittyX.Statup("Love", 70, -5, 1)
                    $ KittyX.Statup("Love", 200, -2)
                    ch_k "Ok, fine."
                    $ KittyX.Statup("Obed", 50, 4)
                    $ KittyX.Statup("Inbt", 80, 1)
                    $ KittyX.Statup("Inbt", 60, 3)
                    $ KittyX.Forced = 1
                    jump Kitty_HJ_Prep
                else:
                    $ KittyX.Statup("Love", 200, -15)
                    $ KittyX.RecentActions.append("angry")
                    $ KittyX.DailyActions.append("angry")

    #She refused all offers.
    $ KittyX.ArmPose = 1
    if "no hand" in KittyX.DailyActions:
        $ KittyX.FaceChange("angry", 1)
        ch_k "I'm not telling you again."
        $ KittyX.RecentActions.append("angry")
        $ KittyX.DailyActions.append("angry")
    elif KittyX.Forced:
        $ KittyX.FaceChange("angry", 1)
        ch_k "Not even if you had a ten foot pole."
        $ KittyX.FaceChange("surprised", 2)
        ch_k "I mean. . ."
        $ KittyX.FaceChange("angry", 1)
        ch_k "You know what I mean!"
        $ KittyX.Statup("Lust", 200, 5)
        if KittyX.Love > 300:
                $ KittyX.Statup("Love", 70, -2)
        $ KittyX.Statup("Obed", 50, -2)
        $ KittyX.RecentActions.append("angry")
        $ KittyX.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ KittyX.FaceChange("angry", 1)
        $ KittyX.DailyActions.append("tabno")
        ch_k "Not here, not anywhere near here."
        $ KittyX.Statup("Lust", 200, 5)
        $ KittyX.Statup("Obed", 50, -3)
    elif KittyX.Hand:
        $ KittyX.FaceChange("sad")
        ch_k "I'm not feeling it today. . ."
    else:
        $ KittyX.FaceChange("normal", 1)
        ch_k "I don't wanna touch that."
    $ KittyX.RecentActions.append("no hand")
    $ KittyX.DailyActions.append("no hand")
    $ temp_modifier = 0
    return


label Kitty_HJ_Prep:
    if Trigger2 == "hand":
        return

    if Taboo:
        $ KittyX.Inbt += int(Taboo/10)
        $ KittyX.Lust += int(Taboo/5)

    $ KittyX.FaceChange("sexy")
    if KittyX.Forced:
        $ KittyX.FaceChange("sad")
    elif not KittyX.Hand:
        $ KittyX.Brows = "confused"
        $ KittyX.Eyes = "sexy"
        $ KittyX.Mouth = "smile"

    call Seen_First_Peen(KittyX,Partner,React=Situation)
    call Kitty_HJ_Launch("L")

    if Situation == KittyX:
            #Kitty auto-starts
            $ Situation = 0
            if Trigger2 == "jackin":
                "[KittyX.Name] brushes your hand aside and starts stroking your cock."
            else:
                "[KittyX.Name] gives you a mischevious smile, and starts to fondle your cock."
            menu:
                "What do you do?"
                "Nothing.":
                    $ KittyX.Statup("Inbt", 70, 3)
                    $ KittyX.Statup("Inbt", 30, 2)
                    "[KittyX.Name] continues her actions."
                "Praise her.":
                    $ KittyX.FaceChange("sexy", 1)
                    $ KittyX.Statup("Inbt", 70, 3)
                    ch_p "Oooh, that's good, [KittyX.Pet]."
                    $ KittyX.NameCheck() #checks reaction to petname
                    "[KittyX.Name] continues her actions."
                    $ KittyX.Statup("Love", 80, 1)
                    $ KittyX.Statup("Obed", 90, 1)
                    $ KittyX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ KittyX.FaceChange("surprised")
                    $ KittyX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [KittyX.Pet]."
                    $ KittyX.NameCheck() #checks reaction to petname
                    "[KittyX.Name] puts it down."
                    $ KittyX.Statup("Obed", 90, 1)
                    $ KittyX.Statup("Obed", 50, 1)
                    $ KittyX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ KittyX.AddWord(1,"refused","refused")
                    return

    if not KittyX.Hand:
        if KittyX.Forced:
            $ KittyX.Statup("Love", 90, -20)
            $ KittyX.Statup("Obed", 70, 25)
            $ KittyX.Statup("Inbt", 80, 30)
        else:
            $ KittyX.Statup("Love", 90, 5)
            $ KittyX.Statup("Obed", 70, 20)
            $ KittyX.Statup("Inbt", 80, 20)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ KittyX.DrainWord("tabno")
    $ KittyX.DrainWord("no hand")
    $ KittyX.RecentActions.append("hand")
    $ KittyX.DailyActions.append("hand")

label Kitty_HJ_Cycle:
    while Round > 0:
        call Shift_Focus(KittyX)
        call Kitty_HJ_Launch
        $ KittyX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass

                        "Start moving? . ." if not Speed:
                                    $ Speed = 1

                        "Speed up. . ." if Speed < 2:
                                    $ Speed = 2
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 2:
                                    pass

                        "Slow Down. . ." if Speed:
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:
                                    pass
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
                                    "I also want to fondle her breasts." if Trigger2 != "fondle breasts":
                                            if KittyX.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ KittyX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")

                                    "Shift primary action":
                                            if KittyX.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                    if KittyX.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Kitty_HJ_After
                                                                        call Kitty_Blowjob
                                                                    else:
                                                                        ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."

#                                                        "How about a titjob?":
#                                                                    if KittyX.Action and MultiAction:
#                                                                        $ Situation = "shift"
#                                                                        call Kitty_HJ_After
#                                                                        call Kitty_Titjob
#                                                                    else:
#                                                                        ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."
                                                        "Never Mind":
                                                                jump Kitty_HJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [KittyX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(KittyX)
                                            "Ask [KittyX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(KittyX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(KittyX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Kitty_HJ_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Kitty_HJ_Cycle
                                            "Never mind":
                                                        jump Kitty_HJ_Cycle
                                    "Undress [KittyX.Name]":
                                            call Girl_Undress(KittyX)
                                    "Clean up [KittyX.Name] (locked)" if not KittyX.Spunk:
                                            pass
                                    "Clean up [KittyX.Name]" if KittyX.Spunk:
                                            call Girl_Cleanup(KittyX,"ask")
                                    "Never mind":
                                            jump Kitty_HJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Kitty_HJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Kitty_HJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Kitty_HJ_Reset
                                    $ Line = 0
                                    jump Kitty_HJ_After
        #End menu (if Line)

        call Shift_Focus(KittyX)
        call Sex_Dialog(KittyX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or KittyX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(KittyX)
                            if "angry" in KittyX.RecentActions:
                                call Kitty_HJ_Reset
                                return
                            $ KittyX.Statup("Lust", 200, 5)
                            if 100 > KittyX.Lust >= 70 and KittyX.OCount < 2 and KittyX.SEXP >= 20:
                                $ KittyX.RecentActions.append("unsatisfied")
                                $ KittyX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Kitty_HJ_After
                            $ Line = "came"

                    if KittyX.Lust >= 100:
                            #If Kitty can cum
                            call Girl_Cumming(KittyX)
                            if Situation == "shift" or "angry" in KittyX.RecentActions:
                                jump Kitty_HJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in KittyX.RecentActions:#And Kitty is unsatisfied,
                                "[KittyX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Kitty_HJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Cnt == 20:
                    $ KittyX.Brows = "angry"
                    menu:
                        ch_k "Ouch, hand cramp, can we[KittyX.like]take a break?"
                        "How about a BJ?" if KittyX.Action and MultiAction:
                                $ Situation = "shift"
                                call Kitty_HJ_After
                                call Kitty_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                jump Kitty_HJ_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Kitty_HJ_Reset
                                $ Situation = "shift"
                                jump Kitty_HJ_After
                        "No, get back down there.":
                                if ApprovalCheck(KittyX, 1200) or ApprovalCheck(KittyX, 500, "O"):
                                    $ KittyX.Statup("Love", 200, -5)
                                    $ KittyX.Statup("Obed", 50, 3)
                                    $ KittyX.Statup("Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    $ KittyX.FaceChange("angry", 1)
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_k "Hey, I've got better things to do if you're[KittyX.like]going to be a dick about it."
                                    $ KittyX.Statup("Love", 50, -3, 1)
                                    $ KittyX.Statup("Love", 80, -4, 1)
                                    $ KittyX.Statup("Obed", 30, -1, 1)
                                    $ KittyX.Statup("Obed", 50, -1, 1)
                                    $ KittyX.RecentActions.append("angry")
                                    $ KittyX.DailyActions.append("angry")
                                    jump Kitty_HJ_After
        elif Cnt == 10 and KittyX.SEXP <= 100 and not ApprovalCheck(KittyX, 1200, "LO"):
                    $ KittyX.Brows = "confused"
                    ch_k "Can we[KittyX.Like]be done with this now? I'm getting sore."
        #End Count check

        call Escalation(KittyX) #sees if she wants to escalate things

        if Round == 10:
            ch_k "It's kind of time to get moving."
        elif Round == 5:
            ch_k "For real[KittyX.like]time's up."

    #Round = 0 loop breaks
    $ KittyX.FaceChange("bemused", 0)
    $ Line = 0
    ch_k "Ok, we need to take a break."

label Kitty_HJ_After:
    $ KittyX.FaceChange("sexy")

    $ KittyX.Hand += 1
    $ KittyX.Action -=1
    $ KittyX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ KittyX.Addictionrate += 1
    $ KittyX.Statup("Lust", 90, 5)

    call Partner_Like(KittyX,1)

    if "Kitty Handi-Queen" in Achievements:
            pass
    elif KittyX.Hand >= 10:
            $ KittyX.FaceChange("smile", 1)
            ch_k "I've kinda become[KittyX.like]a \"Handi-Queen\" or something."
            $ Achievements.append("Kitty Handi-Queen")
            $KittyX.SEXP += 5
    elif KittyX.Hand == 1:
            $KittyX.SEXP += 10
            if KittyX.Love >= 500:
                $ KittyX.Mouth = "smile"
                ch_k "It was so warm to the touch. . ."
            elif Player.Focus <= 20:
                $ KittyX.Mouth = "sad"
                ch_k "Did that work out for you?"
    elif KittyX.Hand == 5:
                ch_k "Let me know any time you need me to give you a hand."

    $ temp_modifier = 0
    if Situation == "shift":
        ch_k "Ok, so what were you thinking?"
    else:
        call Kitty_HJ_Reset
    call Checkout
    return

## end KittyX.Handjob //////////////////////////////////////////////////////////////////////


## KittyX.Titjob //////////////////////////////////////////////////////////////////////              Not finished
label Kitty_Titjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(KittyX)
    if KittyX.Tit >= 7: # She loves it
        $ temp_modifier += 10
    elif KittyX.Tit >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif KittyX.Tit: #You've done it before
        $ temp_modifier += 5

    if KittyX.Addict >= 75 and KittyX.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 15
    elif KittyX.Addict >= 75:
        $ temp_modifier += 5

    if KittyX.SeenChest and ApprovalCheck(KittyX, 500): # You've seen her tits.
        $ temp_modifier += 10
    if not KittyX.Chest and not KittyX.Over: #She's already topless
        $ temp_modifier += 10
    if KittyX.Lust > 75: #She's really horny
        $ temp_modifier += 10
    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in KittyX.Traits:
        $ temp_modifier += (5*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.Petnames:
        $ temp_modifier += 10
    elif "ex" in KittyX.Traits:
        $ temp_modifier -= 30
    if KittyX.ForcedCount and not KittyX.Forced:
        $ temp_modifier -= 5 * KittyX.ForcedCount

    if Taboo and "tabno" in KittyX.DailyActions:
        $ temp_modifier -= 10

    if "no titjob" in KittyX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no titjob" in KittyX.RecentActions else 0

    $ Approval = ApprovalCheck(KittyX, 1200, TabM = 5) # 120, 135, 150, Taboo -200(320)

    if not KittyX.Tit and "no titjob" not in KittyX.RecentActions:
        $ KittyX.FaceChange("surprised", 1)
        $ KittyX.Mouth = "kiss"
        ch_k "You want to rub your cock against my. . . breasts?"

    if not KittyX.Tit and Approval:                                                 #First time dialog
        if KittyX.Forced:
            $ KittyX.FaceChange("sad")
            $ KittyX.Statup("Love", 70, -3, 1)
            $ KittyX.Statup("Love", 20, -2, 1)
        elif KittyX.Love >= (KittyX.Obed + KittyX.Inbt):
            $ KittyX.FaceChange("sexy")
            $ KittyX.Brows = "sad"
            $ KittyX.Mouth = "smile"
            ch_k "It's nice that you even thought about it."
        elif KittyX.Obed >= KittyX.Inbt:
            $ KittyX.FaceChange("normal")
            ch_k "I mean. . ."
        elif KittyX.Addict >= 50:
            $ KittyX.FaceChange("manic", 1)
            ch_k "Hmmmm. . . ."
        else: # Uninhibited
            $ KittyX.FaceChange("sad")
            $ KittyX.Mouth = "smile"
            ch_k "Hadn't really considered that."
    elif Approval:                                                                       #Second time+ dialog
        if KittyX.Forced:
            $ KittyX.FaceChange("sad")
            $ KittyX.Statup("Love", 70, -3, 1)
            $ KittyX.Statup("Love", 20, -2, 1)
            ch_k "This isn't going to become a habit, will it?"
        elif not Taboo and "tabno" in KittyX.DailyActions:
            ch_k "Ok, I guess this is private enough. . ."
        elif "titjob" in KittyX.RecentActions:
            $ KittyX.FaceChange("sexy", 1)
            ch_k "Mmm, again?"
            jump Kitty_TJ_Prep
        elif "titjob" in KittyX.DailyActions:
            $ KittyX.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",
                "You're going to make me sore.",
                "Didn't get enough earlier?",
                "My tits are still kinda sore from earlier."])
            ch_k "[Line]"
        elif KittyX.Tit < 3:
            $ KittyX.FaceChange("sexy", 1)
            $ KittyX.Brows = "confused"
            $ KittyX.Mouth = "kiss"
            ch_k "So you'd like another titjob?"
        else:
            $ KittyX.FaceChange("sexy", 1)
            $ KittyX.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action [rubs her chest]?",
                "So you'd like another titjob?",
                "So you'd like another titjob?",
                "So you'd like another titjob?",
                "A little. . . puffpuff?",
                "A little soft embrace?"])
            ch_k "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if KittyX.Forced:
            $ KittyX.FaceChange("sad")
            $ KittyX.Statup("Obed", 90, 1)
            $ KittyX.Statup("Inbt", 60, 1)
            ch_k "Well, could be worse. . ."
        elif "no titjob" in KittyX.DailyActions:
            ch_k "Hmm, I guess. . ."
        else:
            $ KittyX.FaceChange("sexy", 1)
            $ KittyX.Statup("Love", 90, 1)
            $ KittyX.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, put it here.",
                "Well. . . ok.",
                "Yum.",
                "Sure, whip it out.",
                "Fine. . . [She drools a bit into her cleavage].",
                "Heh, ok."])
            ch_k "[Line]"
            $ Line = 0
        $ KittyX.Statup("Obed", 20, 1)
        $ KittyX.Statup("Obed", 70, 1)
        $ KittyX.Statup("Inbt", 80, 2)
        jump Kitty_TJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ KittyX.FaceChange("angry")
        if "no titjob" in KittyX.RecentActions:
            ch_k "I {i}just{/i} told you \"no,\" [KittyX.Petname]."
        elif Taboo and "tabno" in KittyX.DailyActions and "no titjob" in KittyX.DailyActions:
            ch_k "This is just way too exposed!"
        elif "no titjob" in KittyX.DailyActions:
            ch_k "I already told you \"no,\" [KittyX.Petname]."
        elif Taboo and "tabno" in KittyX.DailyActions:
            ch_k "This is just way too exposed!"
        elif not KittyX.Tit:
            $ KittyX.FaceChange("bemused")
            ch_k "I'm not really up for that, [KittyX.Petname]. . ."
        else:
            $ KittyX.FaceChange("bemused")
            ch_k "Not, right now [KittyX.Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no titjob" in KittyX.DailyActions:
                $ KittyX.FaceChange("bemused")
                ch_k "Yeah, ok, [KittyX.Petname]."
                return
            "Maybe later?" if "no titjob" not in KittyX.DailyActions:
                $ KittyX.FaceChange("sexy")
                ch_k "Maybe."
                $ KittyX.Statup("Love", 80, 2)
                $ KittyX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ KittyX.RecentActions.append("tabno")
                    $ KittyX.DailyActions.append("tabno")
                $ KittyX.RecentActions.append("no titjob")
                $ KittyX.DailyActions.append("no titjob")
                return
            "I think this could be fun for both of us. . .":
                if Approval:
                    $ KittyX.FaceChange("sexy")
                    $ KittyX.Statup("Obed", 80, 2)
                    $ KittyX.Statup("Obed", 40, 2)
                    $ KittyX.Statup("Inbt", 70, 3)
                    $ KittyX.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Well, ok, put it here.",
                        "Well. . . ok.",
                        "I guess.",
                        "I guess, whip it out.",
                        "Fine. . . [She drools a bit into her cleavage].",
                        "Heh, ok."])
                    ch_k "[Line]"
                    $ Line = 0
                    jump Kitty_TJ_Prep
                else:
                    $ Approval = ApprovalCheck(KittyX, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)             Handy instead?
                    if Approval >= 2 and KittyX.Blow:
                        $ KittyX.Statup("Inbt", 80, 1)
                        $ KittyX.Statup("Inbt", 60, 3)
                        $ KittyX.FaceChange("confused", 1)
                        ch_k "Could I[KittyX.like]. . . blow you instead?"
                        menu:
                            ch_k "What do you say [[blowjob]?"
                            "Ok, get down there.":
                                $ KittyX.Statup("Love", 80, 2)
                                $ KittyX.Statup("Inbt", 60, 1)
                                $ KittyX.Statup("Obed", 50, 1)
                                jump Kitty_BJ_Prep
                            "Nah, it's all about dem titties.":
                                $ Line = "no BJ"
                    if Approval and KittyX.Hand:
                        $ KittyX.Statup("Inbt", 80, 1)
                        $ KittyX.Statup("Inbt", 60, 3)
                        $ KittyX.FaceChange("confused", 1)
                        ch_k "Maybe you'd[KittyX.like]settle for a handy?"
                        menu:
                            ch_k "What do you say?"
                            "Sure, that's fine.":
                                $ KittyX.Statup("Love", 80, 2)
                                $ KittyX.Statup("Inbt", 60, 1)
                                $ KittyX.Statup("Obed", 50, 1)
                                jump Kitty_HJ_Prep
                            "Seriously, titties." if Line == "no BJ":
                                $ Line = 0
                            "Nah, it's all about dem titties." if Line != "no BJ":
                                pass
                    $ KittyX.Statup("Love", 200, -2)
                    ch_k "Nah."
                    $ KittyX.Statup("Obed", 70, 2)


            "Come on, let me fuck those titties, [KittyX.Pet]":                                               # Pressured into it
                $ KittyX.NameCheck() #checks reaction to petname
                $ Approval = ApprovalCheck(KittyX, 700, "OI", TabM = 4) # 70, 85, 100, -160(230)
                if Approval > 1 or (Approval and KittyX.Forced):
                    $ KittyX.FaceChange("sad")
                    $ KittyX.Statup("Love", 70, -5, 1)
                    $ KittyX.Statup("Love", 200, -2)
                    ch_k "Ok, fine, whip it out."
                    $ KittyX.Statup("Obed", 50, 4)
                    $ KittyX.Statup("Inbt", 80, 1)
                    $ KittyX.Statup("Inbt", 60, 3)
                    $ KittyX.Forced = 1
                    jump Kitty_TJ_Prep
                else:
                    $ KittyX.Statup("Love", 200, -15)
                    $ KittyX.RecentActions.append("angry")
                    $ KittyX.DailyActions.append("angry")

    #She refused all offers.
    if "no titjob" in KittyX.DailyActions:
        $ KittyX.FaceChange("angry", 1)
        ch_k "Look, I already told you no thanks, [KittyX.Petname]."
        $ KittyX.RecentActions.append("angry")
        $ KittyX.DailyActions.append("angry")
    elif KittyX.Forced:
        $ KittyX.FaceChange("angry", 1)
        ch_k "No, that's just weird."
        $ KittyX.Statup("Lust", 200, 5)
        if KittyX.Love > 300:
                $ KittyX.Statup("Love", 70, -2)
        $ KittyX.Statup("Obed", 50, -2)
        $ KittyX.RecentActions.append("angry")
        $ KittyX.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ KittyX.FaceChange("angry", 1)
        $ KittyX.DailyActions.append("tabno")
        ch_k "You really expect me to do that here? You realize how. . . exposed that would be?"
        $ KittyX.Statup("Lust", 200, 5)
        $ KittyX.Statup("Obed", 50, -3)
    elif KittyX.Tit:
        $ KittyX.FaceChange("sad")
        ch_k "I think I'll let you know when I want you touching these again."
    else:
        $ KittyX.FaceChange("normal", 1)
        ch_k "How about let's not, [KittyX.Petname]."
    $ KittyX.RecentActions.append("no titjob")
    $ KittyX.DailyActions.append("no titjob")
    $ temp_modifier = 0
    return

label Kitty_TJ_Prep:

    if Taboo:
        $ KittyX.Inbt += int(Taboo/10)
        $ KittyX.Lust += int(Taboo/5)


    $ KittyX.FaceChange("sexy")
    if KittyX.Forced:
        $ KittyX.FaceChange("sad")
    elif not KittyX.Tit:
        $ KittyX.Brows = "confused"
        $ KittyX.Eyes = "sexy"
        $ KittyX.Mouth = "smile"

    call Seen_First_Peen(KittyX,Partner,React=Situation)
    call Kitty_TJ_Launch("L")

    if Situation == KittyX:
            #Kitty auto-starts
            $ Situation = 0
            call Kitty_TJ_Launch("L")
            "[KittyX.Name] slides down and presses your dick between her tits."
            menu:
                "What do you do?"
                "Nothing.":
                    $ KittyX.Statup("Inbt", 80, 3)
                    $ KittyX.Statup("Inbt", 40, 2)
                    "[KittyX.Name] starts to slide up and down."
                "Praise her.":
                    $ KittyX.FaceChange("sexy", 1)
                    $ KittyX.Statup("Inbt", 80, 3)
                    ch_p "Oh, that sounds like a good idea, [KittyX.Pet]."
                    $ KittyX.NameCheck() #checks reaction to petname
                    "[KittyX.Name] continues her actions."
                    $ KittyX.Statup("Love", 85, 1)
                    $ KittyX.Statup("Obed", 90, 1)
                    $ KittyX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ KittyX.FaceChange("confused")
                    $ KittyX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [KittyX.Pet]."
                    $ KittyX.NameCheck() #checks reaction to petname
                    "[KittyX.Name] lets it drop out from between her breasts."
                    $ KittyX.Statup("Obed", 90, 1)
                    $ KittyX.Statup("Obed", 50, 3)
                    $ Player.RecentActions.append("nope")
                    $ KittyX.AddWord(1,"refused","refused")
                    return
    if not KittyX.Tit:
        if KittyX.Forced:
            $ KittyX.Statup("Love", 90, -25)
            $ KittyX.Statup("Obed", 70, 30)
            $ KittyX.Statup("Inbt", 80, 35)
        else:
            $ KittyX.Statup("Love", 90, 5)
            $ KittyX.Statup("Obed", 70, 25)
            $ KittyX.Statup("Inbt", 80, 30)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ KittyX.DrainWord("tabno")
    $ KittyX.DrainWord("no titjob")
    $ KittyX.RecentActions.append("titjob")
    $ KittyX.DailyActions.append("titjob")

label Kitty_TJ_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(KittyX)
        call Kitty_TJ_Launch
        $ KittyX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass

                        "Start moving? . ." if Speed == 0:
                                    $ Speed = 1

                        "Speed up. . ." if  Speed == 1:
                                    $ Speed = 2
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 2:
                                    pass

                        "Stop moving" if Speed == 1 or Speed == 3:
                                    $ Speed = 0
                        "Slow Down. . ." if Speed == 2:
                                    $ Speed = 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:
                                    pass

                        "Lick it" if Speed != 3:
                                    $ Speed = 3
                        "Lick it (locked)" if Speed == 3:
                                    pass

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
                                    "I also want to fondle her breasts." if Trigger2 != "fondle breasts":
                                            if KittyX.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ KittyX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")

                                    "Shift primary action":
                                            if KittyX.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                if KittyX.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Kitty_TJ_After
                                                                    call Kitty_Blowjob
                                                                else:
                                                                    ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."

                                                        "How about a handy?":
                                                                if KittyX.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Kitty_BJ_After
                                                                    call Kitty_Handjob
                                                                else:
                                                                    ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."
                                                        "Never Mind":
                                                                jump Kitty_TJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [KittyX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(KittyX)
                                            "Ask [KittyX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(KittyX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(KittyX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Kitty_TJ_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Kitty_TJ_Cycle
                                            "Never mind":
                                                        jump Kitty_TJ_Cycle
                                    "Undress [KittyX.Name]":
                                            call Girl_Undress(KittyX)
                                    "Clean up [KittyX.Name] (locked)" if not KittyX.Spunk:
                                            pass
                                    "Clean up [KittyX.Name]" if KittyX.Spunk:
                                            call Girl_Cleanup(KittyX,"ask")
                                    "Never mind":
                                            jump Kitty_TJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Kitty_TJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Kitty_TJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Kitty_TJ_Reset
                                    $ Line = 0
                                    jump Kitty_TJ_After
        #End menu (if Line)

        call Shift_Focus(KittyX)
        call Sex_Dialog(KittyX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or KittyX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(KittyX)
                            if "angry" in KittyX.RecentActions:
                                call Kitty_TJ_Reset
                                return
                            $ KittyX.Statup("Lust", 200, 5)
                            if 100 > KittyX.Lust >= 70 and KittyX.OCount < 2 and KittyX.SEXP >= 20:
                                $ KittyX.RecentActions.append("unsatisfied")
                                $ KittyX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Kitty_TJ_After
                            $ Line = "came"

                    if KittyX.Lust >= 100:
                            #If Kitty can cum
                            call Girl_Cumming(KittyX)
                            if Situation == "shift" or "angry" in KittyX.RecentActions:
                                jump Kitty_TJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in KittyX.RecentActions:#And Kitty is unsatisfied,
                                "[KittyX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Kitty_TJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if KittyX.SEXP >= 100 or ApprovalCheck(KittyX, 1200, "LO"):
                pass
        elif Cnt == (5 + KittyX.Tit):
                $ KittyX.Brows = "confused"
                ch_k "Are you getting close here? I'm getting as little sore."
        if Cnt == (10 + KittyX.Tit):
                $ KittyX.Brows = "angry"
                menu:
                    ch_k "I'm getting rug-burn here [KittyX.Petname]. Can we do something else?"
                    "How about a BJ?" if KittyX.Action and MultiAction:
                        $ Situation = "shift"
                        call Kitty_TJ_After
                        call Kitty_Blowjob
                        return
                    "Finish up." if Player.FocusX:
                        "You release your concentration. . ."
                        $ Player.FocusX = 0
                        $ Player.Focus += 15
                        jump Kitty_TJ_Cycle
                    "Let's try something else." if MultiAction:
                        $ Line = 0
                        call Kitty_TJ_Reset
                        $ Situation = "shift"
                        jump Kitty_TJ_After
                    "No, get back down there.":
                        if ApprovalCheck(KittyX, 1200) or ApprovalCheck(KittyX, 500, "O"):
                            $ KittyX.Statup("Love", 200, -5)
                            $ KittyX.Statup("Obed", 50, 3)
                            $ KittyX.Statup("Obed", 80, 2)
                            "She grumbles but gets back to work."
                        else:
                            $ KittyX.FaceChange("angry", 1)
                            "She scowls at you, drops you cock and pulls back."
                            ch_k "Well fuck you then."
                            $ KittyX.Statup("Love", 50, -3, 1)
                            $ KittyX.Statup("Love", 80, -4, 1)
                            $ KittyX.Statup("Obed", 30, -1, 1)
                            $ KittyX.Statup("Obed", 50, -1, 1)
                            $ KittyX.RecentActions.append("angry")
                            $ KittyX.DailyActions.append("angry")
                            jump Kitty_TJ_After
            #End Count check

        call Escalation(KittyX) #sees if she wants to escalate things

        if Round == 10:
            ch_k "It's kinda time to get moving."
        elif Round == 5:
            ch_k "For real[KittyX.like]time's up."

    #Round = 0 loop breaks
    $ KittyX.FaceChange("bemused", 0)
    $ Line = 0
    ch_k "Ok, we need to take a break."

label Kitty_TJ_After:
    $ KittyX.FaceChange("sexy")

    $ KittyX.Tit += 1
    $ KittyX.Action -=1
    $ KittyX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ KittyX.Addictionrate += 1

    call Partner_Like(KittyX,4)

    if KittyX.Tit > 5:
        pass
    elif KittyX.Tit == 1:
        $ KittyX.SEXP += 12
        if KittyX.Love >= 500:
            $ KittyX.Mouth = "smile"
            ch_k "That was kinda fun."
        elif Player.Focus <= 20:
            $ KittyX.Mouth = "sad"
            ch_k "Well I hope you got something out of that."
    elif KittyX.Tit == 5:
            ch_k "Huh, I guess these are good for something."

    $ temp_modifier = 0

    if Situation == "shift":
            ch_k "Mmm, so what else did you have in mind?"
    else:
            call Kitty_TJ_Reset
    call Checkout
    return

## end KittyX.Titjob //////////////////////////////////////////////////////////////////////

# KittyX.Blowjob //////////////////////////////////////////////////////////////////////

label Kitty_Blowjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(KittyX)
    if KittyX.Blow >= 7: # She loves it
        $ temp_modifier += 15
    elif KittyX.Blow >= 3: #You've done it before several times
        $ temp_modifier += 10
    elif KittyX.Blow: #You've done it before
        $ temp_modifier += 7

    if KittyX.Addict >= 75 and KittyX.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 25
    elif KittyX.Addict >= 75: #She's really strung out
        $ temp_modifier += 15

    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in KittyX.Traits:
        $ temp_modifier += (4*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.Petnames:
        $ temp_modifier += 10
    elif "ex" in KittyX.Traits:
        $ temp_modifier -= 40
    if KittyX.ForcedCount and not KittyX.Forced:
        $ temp_modifier -= 5 * KittyX.ForcedCount

    if Taboo and "tabno" in KittyX.DailyActions:
        $ temp_modifier -= 10

    if "no blow" in KittyX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no blow" in KittyX.RecentActions else 0

    $ Approval = ApprovalCheck(KittyX, 1300, TabM = 4) # 130, 145, 160, Taboo -160(290)

    if not KittyX.Blow and "no blow" not in KittyX.RecentActions:
        $ KittyX.FaceChange("surprised", 2)
        $ KittyX.Mouth = "kiss"
        ch_k "You want me to suck your dick?"
        if KittyX.Hand:
            $ KittyX.Mouth = "smile"
            ch_k "Not satisfied with handies?"
        $ KittyX.Blush = 1

    if not KittyX.Blow and Approval:                                                 #First time dialog
        if KittyX.Forced:
            $ KittyX.FaceChange("sad")
            $ KittyX.Statup("Love", 70, -3, 1)
            $ KittyX.Statup("Love", 20, -2, 1)
        elif KittyX.Love >= (KittyX.Obed + KittyX.Inbt):
            $ KittyX.FaceChange("sexy")
            $ KittyX.Brows = "sad"
            $ KittyX.Mouth = "smile"
            ch_k "I have wondered what you. . . taste like."
        elif KittyX.Obed >= KittyX.Inbt:
            $ KittyX.FaceChange("normal")
            ch_k "If you want me to. . ."
        elif KittyX.Addict >= 50:
            $ KittyX.FaceChange("manic", 1)
            ch_k "My mouth is watering. . ."
        else: # Uninhibited
            $ KittyX.FaceChange("sad")
            $ KittyX.Mouth = "smile"
            ch_k "[KittyX.Like]sure. . ."
    elif Approval:                                                                       #Second time+ dialog
        if KittyX.Forced:
            $ KittyX.FaceChange("sad")
            $ KittyX.Statup("Love", 70, -3, 1)
            $ KittyX.Statup("Love", 20, -2, 1)
            ch_k "You want me to do that again?"
        elif not Taboo and "tabno" in KittyX.DailyActions:
            ch_k "Ok, I guess this is private enough. . ."
        elif "blow" in KittyX.RecentActions:
            $ KittyX.FaceChange("sexy", 1)
            ch_k "Mmm, again? [[stretches her jaw]"
            jump Kitty_BJ_Prep
        elif "blow" in KittyX.DailyActions:
            $ KittyX.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",
                "You're going to give me lockhee- . . . jaw.",
                "Let me get some saliva going.",
                "Didn't get enough earlier?",
                "My jaw's still a bit sore from earlier.",
                "My jaw's still a bit sore from earlier."])
            ch_k "[Line]"
        elif KittyX.Blow < 3:
            $ KittyX.FaceChange("sexy", 1)
            $ KittyX.Brows = "confused"
            $ KittyX.Mouth = "kiss"
            ch_k "So you'd like another blowjob?"
        else:
            $ KittyX.FaceChange("sexy", 1)
            $ KittyX.ArmPose = 2
            $ Line = renpy.random.choice(["You want me to [mimes blowing]?",
                "So you wanna 'nother blowjob?",
                "A little. . . lick?",
                "You want me to suck you off?",
                "A little tlc?"])
            ch_k "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if KittyX.Forced:
            $ KittyX.FaceChange("sad")
            $ KittyX.Statup("Obed", 90, 1)
            $ KittyX.Statup("Inbt", 60, 1)
            ch_k "Whatever."
        elif "no blow" in KittyX.DailyActions:
            ch_k "Ok, fine, I suppose it isn't {i}sooo{/i} bad. . ."
        else:
            $ KittyX.FaceChange("sexy", 1)
            $ KittyX.Statup("Love", 90, 1)
            $ KittyX.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, ahhhhhh.",
                "Well. . . ok.",
                "Yum.",
                "Sure, whip it out.",
                "Ok. . . [She licks her lips].",
                "Lol, ok, alright."])
            ch_k "[Line]"
            $ Line = 0
        $ KittyX.Statup("Obed", 20, 1)
        $ KittyX.Statup("Obed", 70, 1)
        $ KittyX.Statup("Inbt", 80, 2)
        jump Kitty_BJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ KittyX.FaceChange("angry")
        if "no blow" in KittyX.RecentActions:
            ch_k "What did I[KittyX.like]{i}just{/i} tell you [KittyX.Petname]."
        elif Taboo and "tabno" in KittyX.DailyActions and "no blow" in KittyX.DailyActions:
            ch_k "I told you, not in public!"
        elif "no blow" in KittyX.DailyActions:
            ch_k "I told you \"no,\" [KittyX.Petname]."
        elif Taboo and "tabno" in KittyX.DailyActions:
            ch_k "I told you this is too public!"
        elif not KittyX.Blow:
            $ KittyX.FaceChange("bemused")
            ch_k "I don't know about the taste, [KittyX.Petname]. . ."
        else:
            $ KittyX.FaceChange("bemused")
            ch_k "Later, [KittyX.Petname]!"
        menu:
            extend ""
            "Sorry, never mind." if "no blow" in KittyX.DailyActions:
                $ KittyX.FaceChange("bemused")
                ch_k "Aw, it's ok, [KittyX.Petname]."
                return
            "Maybe later?" if "no blow" not in KittyX.DailyActions:
                $ KittyX.FaceChange("sexy")
                ch_k "You[KittyX.like]never know, [KittyX.Petname]."
                $ KittyX.Statup("Love", 80, 2)
                $ KittyX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ KittyX.RecentActions.append("tabno")
                    $ KittyX.DailyActions.append("tabno")
                $ KittyX.RecentActions.append("no blow")
                $ KittyX.DailyActions.append("no blow")
                return
            "Come on, please?":
                if Approval:
                    $ KittyX.FaceChange("sexy")
                    $ KittyX.Statup("Obed", 90, 2)
                    $ KittyX.Statup("Obed", 50, 2)
                    $ KittyX.Statup("Inbt", 70, 3)
                    $ KittyX.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Well, sure, I guess.",
                        "Well. . . ok.",
                        "I could maybe give it a try.",
                        "I guess I could. . .",
                        "Fiiine. . . [She licks her lips].",
                        "Heh, ok, fine."])
                    ch_k "[Line]"
                    $ Line = 0
                    jump Kitty_BJ_Prep
                else:
                    if ApprovalCheck(KittyX, 1100, TabM = 3): # 110, 125, 140, Taboo -120(230)             Handy instead?
                        $ KittyX.Statup("Inbt", 80, 1)
                        $ KittyX.Statup("Inbt", 60, 3)
                        $ KittyX.FaceChange("confused", 1)
                        $ KittyX.ArmPose = 1
                        if KittyX.Hand:
                            ch_k "Maybe I could just use my hand?"
                        else:
                            ch_k "I could maybe. . . [[she makes a jerking motion with her hand]?"
                        menu:
                            ch_k "Would that work?"
                            "Sure, that's fine.":
                                $ KittyX.Statup("Love", 80, 2)
                                $ KittyX.Statup("Inbt", 60, 1)
                                $ KittyX.Statup("Obed", 50, 1)
                                jump Kitty_HJ_Prep
                            "Nah, if it's not a BJ, forget it.":
                                $ KittyX.Statup("Love", 200, -2)
                                $ KittyX.ArmPose = 0
                                ch_k "Ok, your loss."
                                $ KittyX.Statup("Obed", 70, 2)


            "Suck it, [KittyX.Pet]":                                               # Pressured into it
                $ KittyX.NameCheck() #checks reaction to petname
                $ Approval = ApprovalCheck(KittyX, 750, "OI", TabM = 3) # 75, 90, 105, -120(195)
                if Approval > 1 or (Approval and KittyX.Forced):
                    $ KittyX.FaceChange("sad")
                    $ KittyX.Statup("Love", 70, -5, 1)
                    $ KittyX.Statup("Love", 200, -2)
                    ch_k "Ok, fine. . ."
                    $ KittyX.Statup("Obed", 50, 4)
                    $ KittyX.Statup("Inbt", 80, 1)
                    $ KittyX.Statup("Inbt", 60, 3)
                    $ KittyX.Forced = 1
                    jump Kitty_BJ_Prep
                else:
                    $ KittyX.Statup("Love", 200, -15)
                    $ KittyX.RecentActions.append("angry")
                    $ KittyX.DailyActions.append("angry")

    #She refused all offers.
    if "no blow" in KittyX.DailyActions:
        $ KittyX.FaceChange("angry", 1)
        ch_k "You can eat a dick, 'cos I'm not."
        $ KittyX.RecentActions.append("angry")
        $ KittyX.DailyActions.append("angry")
    elif KittyX.Forced:
        $ KittyX.FaceChange("angry", 1)
        ch_k "I just can't do that!"
        $ KittyX.Statup("Lust", 200, 5)
        if KittyX.Love > 300:
                $ KittyX.Statup("Love", 70, -2)
        $ KittyX.Statup("Obed", 50, -2)
        $ KittyX.RecentActions.append("angry")
        $ KittyX.DailyActions.append("angry")
        $ KittyX.RecentActions.append("no blow")
        $ KittyX.DailyActions.append("no blow")
        return
    elif Taboo:                             # she refuses and this is too public a place for her
        $ KittyX.FaceChange("angry", 1)
        $ KittyX.DailyActions.append("tabno")
        ch_k "This is way too exposed!"
        $ KittyX.Statup("Lust", 200, 5)
        $ KittyX.Statup("Obed", 50, -3)
        return
    elif KittyX.Blow:
        $ KittyX.FaceChange("sad")
        ch_k "No, not this time."
    else:
        $ KittyX.FaceChange("normal", 1)
        ch_k "Nope."
    $ KittyX.RecentActions.append("no blow")
    $ KittyX.DailyActions.append("no blow")
    $ temp_modifier = 0
    return


label Kitty_BJ_Prep:
    if renpy.showing("Kitty_HJ_Animation"):
        hide Kitty_HJ_Animation with easeoutbottom
    if Taboo:
        $ KittyX.Inbt += int(Taboo/10)
        $ KittyX.Lust += int(Taboo/5)

    $ KittyX.FaceChange("sexy")
    if KittyX.Forced:
        $ KittyX.FaceChange("sad")
    elif not KittyX.Blow:
        $ KittyX.Brows = "confused"
        $ KittyX.Eyes = "sexy"
        $ KittyX.Mouth = "smile"

    call Seen_First_Peen(KittyX,Partner,React=Situation)
    call Kitty_BJ_Launch("L")

    if Situation == KittyX:
            #Kitty auto-starts
            $ Situation = 0
            "[KittyX.Name] slides down and gives your cock a little lick."
            menu:
                "What do you do?"
                "Nothing.":
                    $ KittyX.Statup("Inbt", 80, 3)
                    $ KittyX.Statup("Inbt", 40, 2)
                    "[KittyX.Name] continues licking at it."
                "Praise her.":
                    $ KittyX.FaceChange("sexy", 1)
                    $ KittyX.Statup("Inbt", 80, 3)
                    ch_p "Hmmm, keep doing that, [KittyX.Pet]."
                    $ KittyX.NameCheck() #checks reaction to petname
                    "[KittyX.Name] continues her actions."
                    $ KittyX.Statup("Love", 85, 1)
                    $ KittyX.Statup("Obed", 90, 1)
                    $ KittyX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ KittyX.FaceChange("surprised")
                    $ KittyX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [KittyX.Pet]."
                    $ KittyX.NameCheck() #checks reaction to petname
                    "[KittyX.Name] puts it down."
                    $ KittyX.Statup("Obed", 90, 1)
                    $ KittyX.Statup("Obed", 50, 3)
                    $ Player.RecentActions.append("nope")
                    $ KittyX.AddWord(1,"refused","refused")
                    return
    if not KittyX.Blow:
        if KittyX.Forced:
            $ KittyX.Statup("Love", 90, -70)
            $ KittyX.Statup("Obed", 70, 45)
            $ KittyX.Statup("Inbt", 80, 60)
        else:
            $ KittyX.Statup("Love", 90, 5)
            $ KittyX.Statup("Obed", 70, 35)
            $ KittyX.Statup("Inbt", 80, 40)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ KittyX.DrainWord("tabno")
    $ KittyX.DrainWord("no blow")
    $ KittyX.RecentActions.append("blow")
    $ KittyX.DailyActions.append("blow")

label Kitty_BJ_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(KittyX)
        call Kitty_BJ_Launch
        $ KittyX.LustFace()

        if Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass

                        "Lick it. . ." if Speed != 1:
                                $ Speed = 1
                        "Lick it. . . (locked)" if Speed == 1:
                                pass

                        "Just the head. . ." if Speed != 2:
                            $ Speed = 2
                        "Just the head. . . (locked)" if Speed == 2:
                                pass

                        "Suck on it." if Speed != 3:
                                $ Speed = 3
                                if Trigger2 == "jackin":
                                    "She dips her head a bit lower, and you move your hand out of the way."

                        "Suck on it. (locked)" if Speed == 3:
                                pass

                        "Take it deeper." if Speed != 4:
                                if "pushed" in KittyX.RecentActions:
                                    ch_k "Sorry, I just can't handle all of you yet."
                                elif KittyX.Blow < 5:
                                    $ KittyX.Statup("Love", 80, -(20-(2*KittyX.Blow)))
                                    $ KittyX.Statup("Obed", 80, (30-(3*KittyX.Blow)))
                                    "She gags on it slightly and moves back to a more comfortable pace."
                                    $ KittyX.RecentActions.append("pushed")
                                else:
                                    if Trigger2 == "jackin" and Speed != 3:
                                        "She takes it to the root, and you move your hand out of the way."
                                    $ Speed = 4
                        "Take it deeper. (locked)" if Speed == 4:
                                pass

                        "Set your own pace. . .":
                                "[KittyX.Name] hums contentedly."
                                if "setpace" not in KittyX.RecentActions:
                                    $ KittyX.Statup("Love", 80, 2)
                                $ D20 = renpy.random.randint(1, 20)
                                if KittyX.Blow < 5:
                                    $ D20 -= 10
                                elif KittyX.Blow < 10:
                                    $ D20 -= 5

                                if D20 > 15:
                                    $ Speed = 4
                                    if "setpace" not in KittyX.RecentActions:
                                        $ KittyX.Statup("Inbt", 80, 3)
                                elif D20 > 10:
                                    $ Speed = 3
                                elif D20 > 5:
                                    $ Speed = 2
                                else:
                                    $ Speed = 1
                                $ KittyX.RecentActions.append("setpace")

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
                                    "I also want to fondle her breasts." if Trigger2 != "fondle breasts":
                                            if KittyX.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ KittyX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")

                                    "Shift primary action":
                                            if KittyX.Action and MultiAction:
                                                    menu:
                                                        "How about a handy?":
                                                                if KittyX.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Kitty_BJ_After
                                                                    call Kitty_Handjob
                                                                else:
                                                                    ch_k "I'm kinda tired, could we just wrap this up. . ."
                                                        "How about a titjob?":
                                                                if KittyX.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Kitty_BJ_After
                                                                    call Kitty_Titjob
                                                                else:
                                                                    ch_k "I'm kinda tired, could we just wrap this up. . ."
                                                        "Never Mind":
                                                                jump Kitty_BJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [KittyX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(KittyX)
                                            "Ask [KittyX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(KittyX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(KittyX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Kitty_BJ_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Kitty_BJ_Cycle
                                            "Never mind":
                                                        jump Kitty_BJ_Cycle
                                    "Undress [KittyX.Name]":
                                            call Girl_Undress(KittyX)
                                    "Clean up [KittyX.Name] (locked)" if not KittyX.Spunk:
                                            pass
                                    "Clean up [KittyX.Name]" if KittyX.Spunk:
                                            call Girl_Cleanup(KittyX,"ask")
                                    "Never mind":
                                            jump Kitty_BJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Kitty_BJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Kitty_BJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Kitty_BJ_Reset
                                    $ Line = 0
                                    jump Kitty_BJ_After
        #End menu (if Line)

        call Shift_Focus(KittyX)
        call Sex_Dialog(KittyX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1
        if Speed:
            $ Player.Wet = 1 #wets penis
            $ Player.Spunk = 0 if Player.Spunk else Player.Spunk #cleans you off after one cycle

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or KittyX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(KittyX)
                            if "angry" in KittyX.RecentActions:
                                call Kitty_BJ_Reset
                                return
                            $ KittyX.Statup("Lust", 200, 5)
                            if 100 > KittyX.Lust >= 70 and KittyX.OCount < 2 and KittyX.SEXP >= 20:
                                $ KittyX.RecentActions.append("unsatisfied")
                                $ KittyX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Kitty_BJ_After
                            $ Line = "came"

                    if KittyX.Lust >= 100:
                            #If Kitty can cum
                            call Girl_Cumming(KittyX)
                            if Situation == "shift" or "angry" in KittyX.RecentActions:
                                jump Kitty_BJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."

                            if "unsatisfied" in KittyX.RecentActions:#And Kitty is unsatisfied,
                                "[KittyX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Kitty_BJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if KittyX.SEXP >= 100 or ApprovalCheck(KittyX, 1200, "LO"):
            pass
        elif Cnt == (10 + KittyX.Blow):
                $ KittyX.Brows = "angry"
                menu:
                    ch_k "I'm[KittyX.like]totally worn out here. Can we do something else?"
                    "How about a Handy?" if KittyX.Action and MultiAction:
                            $ Situation = "shift"
                            call Kitty_BJ_After
                            call Kitty_Handjob
                            return
                    "Finish up." if Player.FocusX:
                            "You release your concentration. . ."
                            $ Player.FocusX = 0
                            $ Player.Focus += 15
                            jump Kitty_BJ_Cycle
                    "Let's try something else." if MultiAction:
                            $ Line = 0
                            call Kitty_BJ_Reset
                            $ Situation = "shift"
                            jump Kitty_BJ_After
                    "No, get back down there.":
                            if ApprovalCheck(KittyX, 1200) or ApprovalCheck(KittyX, 500, "O"):
                                $ KittyX.Statup("Love", 200, -5)
                                $ KittyX.Statup("Obed", 50, 3)
                                $ KittyX.Statup("Obed", 80, 2)
                                "She grumbles but gets back to work."
                            else:
                                $ KittyX.FaceChange("angry", 1)
                                "She scowls at you, drops you cock and pulls back."
                                ch_k "Well fuck you then."
                                $ KittyX.Statup("Love", 50, -3, 1)
                                $ KittyX.Statup("Love", 80, -4, 1)
                                $ KittyX.Statup("Obed", 30, -1, 1)
                                $ KittyX.Statup("Obed", 50, -1, 1)
                                $ KittyX.RecentActions.append("angry")
                                $ KittyX.DailyActions.append("angry")
                                jump Kitty_BJ_After
        elif Cnt == (5 + KittyX.Blow) and KittyX.SEXP <= 100 and not ApprovalCheck(KittyX, 1200, "LO"):
                    $ KittyX.Brows = "confused"
                    ch_k "Are you getting close here? I'm cramping up."
        #End Count check

        call Escalation(KittyX) #sees if she wants to escalate things

        if Round == 10:
            ch_k "It's kind of time to get moving."
        elif Round == 5:
            ch_k "For real[KittyX.like]time's up."

    #Round = 0 loop breaks
    $ KittyX.FaceChange("bemused", 0)
    $ Line = 0
    ch_k "Ok, I gotta rest my jaw for a minute. . ."

label Kitty_BJ_After:
    $ KittyX.FaceChange("sexy")

    $ KittyX.Blow += 1
    $ KittyX.Action -=1
    $ KittyX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ KittyX.Addictionrate += 1

    call Partner_Like(KittyX,2)

    if "Kitty Jobber" in Achievements:
        pass
    elif KittyX.Blow >= 10:
        $ KittyX.FaceChange("smile", 1)
        ch_k "I can't[KittyX.like]get your taste out of my mind."
        $ Achievements.append("Kitty Jobber")
        $KittyX.SEXP += 5
    elif Situation == "shift":
        pass
    elif KittyX.Blow == 1:
            $KittyX.SEXP += 15
            if KittyX.Love >= 500:
                $ KittyX.Mouth = "smile"
                ch_k "Huh, that wasn't bad."
            elif Player.Focus <= 20:
                $ KittyX.Mouth = "sad"
                ch_k "I hope you enjoyed that."
    elif KittyX.Blow == 5:
        ch_k "I'm getting better at this. . . right?"
        menu:
            "[[nod]":
                $ KittyX.FaceChange("smile", 1)
                $ KittyX.Statup("Love", 90, 15)
                $ KittyX.Statup("Obed", 80, 5)
                $ KittyX.Statup("Inbt", 90, 10)
            "[[shake head \"no\"]":
                if ApprovalCheck(KittyX, 500, "O"):
                    $ KittyX.FaceChange("sad", 2)
                    $ KittyX.Statup("Love", 200, -5)
                else:
                    $ KittyX.FaceChange("angry", 2)
                    $ KittyX.Statup("Love", 200, -25)
                $ KittyX.Statup("Obed", 80, 10)
                ch_k ". . ."
                $ KittyX.FaceChange("sad", 1)

    $ temp_modifier = 0
    if Situation != "shift":
        call Kitty_BJ_Reset
    call Checkout
    return



# end KittyX.Blowjob                                 //////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy
label Kitty_Dildo_Check:
    if "dildo" in Player.Inventory:
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in KittyX.Inventory:
        "You ask [KittyX.Name] to get out her favorite Dildo."
    else:
        "You don't have one of those on you."
        return 0
    return 1

label Kitty_Dildo_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(KittyX)
    call Kitty_Dildo_Check
    if not _return:
        return

    if KittyX.DildoP: #You've done it before
        $ temp_modifier += 15
    if KittyX.PantsNum() > 6: # she's got pants on.
        $ temp_modifier -= 20

    if KittyX.Lust > 95:
        $ temp_modifier += 20
    elif KittyX.Lust > 85: #She's really horny
        $ temp_modifier += 15

    if Situation == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in KittyX.Traits:
        $ temp_modifier += (5*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.Petnames:
        $ temp_modifier += 10
    elif "ex" in KittyX.Traits:
        $ temp_modifier -= 40
    if KittyX.ForcedCount and not KittyX.Forced:
        $ temp_modifier -= 5 * KittyX.ForcedCount

    if Taboo and "tabno" in KittyX.DailyActions:
        $ temp_modifier -= 10

    if "no dildo" in KittyX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no dildo" in KittyX.RecentActions else 0

    $ Approval = ApprovalCheck(KittyX, 1250, TabM = 4) # 125, 140, 155, Taboo -160(335)

    if Situation == KittyX:                                                                  #Kitty auto-starts
                if Approval > 2:                                                      # fix, add kitty auto stuff here
                    if KittyX.PantsNum() == 5:
                        "[KittyX.Name] grabs her dildo, hiking up her skirt as she does."
                        $ KittyX.Upskirt = 1
                    elif KittyX.PantsNum() > 6:
                        "[KittyX.Name] grabs her dildo, pulling down her pants as she does."
                        $ KittyX.Legs = 0
                    else:
                        "[KittyX.Name] grabs her dildo, rubbing is suggestively against her crotch."
                    $ KittyX.SeenPanties = 1
                    "She slides the tip along her pussy and seems to want you to insert it."
                    menu:
                        "What do you do?"
                        "Nothing.":
                            $ KittyX.Statup("Inbt", 80, 3)
                            $ KittyX.Statup("Inbt", 50, 2)
                            "[KittyX.Name] slides it in."
                        "Go for it.":
                            $ KittyX.FaceChange("sexy", 1)
                            $ KittyX.Statup("Inbt", 80, 3)
                            ch_p "Oh yeah, [KittyX.Pet], let's do this."
                            $ KittyX.NameCheck() #checks reaction to petname
                            "You grab the dildo and slide it in."
                            $ KittyX.Statup("Love", 85, 1)
                            $ KittyX.Statup("Obed", 90, 1)
                            $ KittyX.Statup("Obed", 50, 2)
                        "Ask her to stop.":
                            $ KittyX.FaceChange("surprised")
                            $ KittyX.Statup("Inbt", 70, 1)
                            ch_p "Let's not do that right now, [KittyX.Pet]."
                            $ KittyX.NameCheck() #checks reaction to petname
                            "[KittyX.Name] sets the dildo down."
                            $ KittyX.OutfitChange()
                            $ KittyX.Statup("Obed", 90, 1)
                            $ KittyX.Statup("Obed", 50, 1)
                            $ KittyX.Statup("Obed", 30, 2)
                            return
                    jump Kitty_DP_Prep
                else:
                    $ temp_modifier = 0                               # fix, add kitty auto stuff here
                    $ Trigger2 = 0
                return

    if Situation == "auto":
                "You rub the dildo across her body, and along her moist slit."
                $ KittyX.FaceChange("surprised", 1)

                if (KittyX.DildoP and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
                    "[KittyX.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                    $ KittyX.FaceChange("sexy")
                    $ KittyX.Statup("Obed", 70, 3)
                    $ KittyX.Statup("Inbt", 50, 3)
                    $ KittyX.Statup("Inbt", 70, 1)
                    ch_k "Ooo, [KittyX.Petname], toys!"
                    jump Kitty_DP_Prep
                else:                                                                                                            #she's questioning it
                    $ KittyX.Brows = "angry"
                    menu:
                        ch_k "Hey, what are you planning to do with that?!"
                        "Sorry, sorry! Never mind.":
                            if Approval:
                                $ KittyX.FaceChange("sexy", 1)
                                $ KittyX.Statup("Obed", 70, 3)
                                $ KittyX.Statup("Inbt", 50, 3)
                                $ KittyX.Statup("Inbt", 70, 1)
                                ch_k "Well, now that you mention it. . ."
                                jump Kitty_DP_Prep
                            "You pull back before you really get it in."
                            $ KittyX.FaceChange("bemused", 1)
                            if KittyX.DildoP:
                                ch_k "Well ok, [KittyX.Petname], maybe warn me next time?"
                            else:
                                ch_k "Well ok, [KittyX.Petname], that's a little much. . . for now . . ."
                        "Just playing with my favorite toys.":
                            $ KittyX.Statup("Love", 80, -10, 1)
                            $ KittyX.Statup("Love", 200, -10)
                            "You press it inside some more."
                            $ KittyX.Statup("Obed", 70, 3)
                            $ KittyX.Statup("Inbt", 50, 3)
                            if not ApprovalCheck(KittyX, 700, "O", TabM=1): #Checks if Obed is 700+
                                $ KittyX.FaceChange("angry")
                                "[KittyX.Name] shoves you away and slaps you in the face."
                                ch_k "Jerk!"
                                ch_k "Ask nice if you want to stick something in my pussy!"
                                $ KittyX.Statup("Love", 50, -10, 1)
                                $ KittyX.Statup("Obed", 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                if renpy.showing("Kitty_SexSprite"):
                                    call Kitty_Sex_Reset
                                $ KittyX.RecentActions.append("angry")
                                $ KittyX.DailyActions.append("angry")
                            else:
                                $ KittyX.FaceChange("sad")
                                "[KittyX.Name] doesn't seem to be into this, you're lucky she's so obedient."
                                jump Kitty_DP_Prep
                return
    #end Auto

    if not KittyX.DildoP:
            #first time
            $ KittyX.FaceChange("surprised", 1)
            $ KittyX.Mouth = "kiss"
            ch_k "Hmmm, so you'd like to try out some toys?"
            if KittyX.Forced:
                $ KittyX.FaceChange("sad")
                ch_k "I suppose there are worst things you could ask for."

    if not KittyX.DildoP and Approval:
            #First time dialog
            if KittyX.Forced:
                $ KittyX.FaceChange("sad")
                $ KittyX.Statup("Love", 70, -3, 1)
                $ KittyX.Statup("Love", 20, -2, 1)
            elif KittyX.Love >= (KittyX.Obed + KittyX.Inbt):
                $ KittyX.FaceChange("sexy")
                $ KittyX.Brows = "sad"
                $ KittyX.Mouth = "smile"
                ch_k "I've had a reasonable amount of experience with these, you know. . ."
            elif KittyX.Obed >= KittyX.Inbt:
                $ KittyX.FaceChange("normal")
                ch_k "If that's what you want, [KittyX.Petname]. . ."
            else: # Uninhibited
                $ KittyX.FaceChange("sad")
                $ KittyX.Mouth = "smile"
                ch_k "I guess it could be fun with a partner. . ."

    elif Approval:
            #Second time+ dialog
            if KittyX.Forced:
                $ KittyX.FaceChange("sad")
                $ KittyX.Statup("Love", 70, -3, 1)
                $ KittyX.Statup("Love", 20, -2, 1)
                ch_k "The toys again?"
            elif not Taboo and "tabno" in KittyX.DailyActions:
                ch_k "Well, at least you got us some privacy this time. . ."
            elif "dildo pussy" in KittyX.RecentActions:
                $ KittyX.FaceChange("sexy", 1)
                ch_k "Mmm, again? Ok, let's get to it."
                jump Kitty_DP_Prep
            elif "dildo pussy" in KittyX.DailyActions:
                $ KittyX.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Breaking out the toys again?",
                    "Didn't get enough earlier?",
                    "You're going to wear me out."])
                ch_k "[Line]"
            elif KittyX.DildoP < 3:
                $ KittyX.FaceChange("sexy", 1)
                $ KittyX.Brows = "confused"
                $ KittyX.Mouth = "kiss"
                ch_k "You want to stick it in my pussy again?"
            else:
                $ KittyX.FaceChange("sexy", 1)
                $ KittyX.ArmPose = 2
                $ Line = renpy.random.choice(["You want some of this action?",
                    "So you'd like another go?",
                    "You want to stick it in my pussy again?",
                    "You want me ta lube up your toy?"])
                ch_k "[Line]"
                $ Line = 0

    if Approval >= 2:
            #She's into it. . .
            if KittyX.Forced:
                $ KittyX.FaceChange("sad")
                $ KittyX.Statup("Obed", 90, 1)
                $ KittyX.Statup("Inbt", 60, 1)
                ch_k "Ok, fine."
            else:
                $ KittyX.FaceChange("sexy", 1)
                $ KittyX.Statup("Love", 90, 1)
                $ KittyX.Statup("Inbt", 50, 3)
                $ Line = renpy.random.choice(["Well, sure, stick it in.",
                    "Well. . . ok.",
                    "Sure!",
                    "I guess I could. . . stick it in.",
                    "Hells yeah.",
                    "Heh, ok, ok."])
                ch_k "[Line]"
                $ Line = 0
            $ KittyX.Statup("Obed", 20, 1)
            $ KittyX.Statup("Obed", 60, 1)
            $ KittyX.Statup("Inbt", 70, 2)
            jump Kitty_DP_Prep

    else:
            #She's not into it, but maybe. . .
            $ KittyX.FaceChange("angry")
            if "no dildo" in KittyX.RecentActions:
                ch_k "What part of \"no,\" did you not get, [KittyX.Petname]?"
            elif Taboo and "tabno" in KittyX.DailyActions and "no dildo" in KittyX.DailyActions:
                ch_k "Stop swinging that thing around in public!"
            elif "no dildo" in KittyX.DailyActions:
                ch_k "I already told you \"no,\" [KittyX.Petname]."
            elif Taboo and "tabno" in KittyX.DailyActions:
                ch_k "Stop swinging that thing around in public!"
            elif not KittyX.DildoP:
                $ KittyX.FaceChange("bemused")
                ch_k "I'm just not into toys, [KittyX.Petname]. . ."
            else:
                $ KittyX.FaceChange("bemused")
                ch_k "I don't think we need any toys, [KittyX.Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in KittyX.DailyActions:
                    $ KittyX.FaceChange("bemused")
                    ch_k "Yeah, ok, [KittyX.Petname]."
                    return
                "Maybe later?" if "no dildo" not in KittyX.DailyActions:
                    $ KittyX.FaceChange("sexy")
                    ch_k "Maybe I'll practice on my own time, [KittyX.Petname]."
                    $ KittyX.Statup("Love", 80, 2)
                    $ KittyX.Statup("Inbt", 70, 2)
                    if Taboo:
                        $ KittyX.RecentActions.append("tabno")
                        $ KittyX.DailyActions.append("tabno")
                    $ KittyX.RecentActions.append("no dildo")
                    $ KittyX.DailyActions.append("no dildo")
                    return
                "I think you'd like it. . .":
                    if Approval:
                        $ KittyX.FaceChange("sexy")
                        $ KittyX.Statup("Obed", 90, 2)
                        $ KittyX.Statup("Obed", 50, 2)
                        $ KittyX.Statup("Inbt", 70, 3)
                        $ KittyX.Statup("Inbt", 40, 2)
                        $ Line = renpy.random.choice(["Well, sure, stick it in.",
                            "I suppose. . .",
                            "You've got me there."])
                        ch_k "[Line]"
                        $ Line = 0
                        jump Kitty_DP_Prep
                    else:
                        pass

                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck(KittyX, 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                    if Approval > 1 or (Approval and KittyX.Forced):
                        $ KittyX.FaceChange("sad")
                        $ KittyX.Statup("Love", 70, -5, 1)
                        $ KittyX.Statup("Love", 200, -5)
                        ch_k "Ok, fine. If we're going to do this, stick it in already."
                        $ KittyX.Statup("Obed", 80, 4)
                        $ KittyX.Statup("Inbt", 80, 1)
                        $ KittyX.Statup("Inbt", 60, 3)
                        $ KittyX.Forced = 1
                        jump Kitty_DP_Prep
                    else:
                        $ KittyX.Statup("Love", 200, -20)
                        $ KittyX.RecentActions.append("angry")
                        $ KittyX.DailyActions.append("angry")

    #She refused all offers.
    $ KittyX.ArmPose = 1
    if "no dildo" in KittyX.DailyActions:
            ch_k "Learn to take \"no\" for an answer, [KittyX.Petname]."
            $ KittyX.RecentActions.append("angry")
            $ KittyX.DailyActions.append("angry")
    elif KittyX.Forced:
            $ KittyX.FaceChange("angry", 1)
            ch_k "I'm not going to let you use that on me."
            $ KittyX.Statup("Lust", 200, 5)
            if KittyX.Love > 300:
                    $ KittyX.Statup("Love", 70, -2)
            $ KittyX.Statup("Obed", 50, -2)
            $ KittyX.RecentActions.append("angry")
            $ KittyX.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
            $ KittyX.FaceChange("angry", 1)
            $ KittyX.RecentActions.append("tabno")
            $ KittyX.DailyActions.append("tabno")
            ch_k "Not here!"
            $ KittyX.Statup("Lust", 200, 5)
            $ KittyX.Statup("Obed", 50, -3)
    elif KittyX.DildoP:
            $ KittyX.FaceChange("sad")
            ch_k "Sorry, you can keep your toys to yourself."
    else:
            $ KittyX.FaceChange("normal", 1)
            ch_k "No way."
    $ KittyX.RecentActions.append("no dildo")
    $ KittyX.DailyActions.append("no dildo")
    $ temp_modifier = 0
    return

label Kitty_DP_Prep: #Animation set-up
    if Trigger2 == "dildo pussy":
        return

    if not KittyX.Forced and Situation != "auto":
        $ temp_modifier = 15 if KittyX.PantsNum() > 6 else 0
        call Bottoms_Off(KittyX)
        if "angry" in KittyX.RecentActions:
            return

    $ temp_modifier = 0
    call Kitty_Pussy_Launch("dildo pussy")
    if not KittyX.DildoP:
        if KittyX.Forced:
            $ KittyX.Statup("Love", 90, -75)
            $ KittyX.Statup("Obed", 70, 60)
            $ KittyX.Statup("Inbt", 80, 35)
        else:
            $ KittyX.Statup("Love", 90, 10)
            $ KittyX.Statup("Obed", 70, 20)
            $ KittyX.Statup("Inbt", 80, 45)
    if Taboo:
        $ KittyX.Inbt += int(Taboo/10)
        $ KittyX.Lust += int(Taboo/5)


    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ KittyX.DrainWord("tabno")
    $ KittyX.DrainWord("no dildo")
    $ KittyX.RecentActions.append("dildo pussy")
    $ KittyX.DailyActions.append("dildo pussy")

label Kitty_DP_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(KittyX)
        call Kitty_Pussy_Launch("dildo pussy")
        $ KittyX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                call Slap_Ass(KittyX)
                                jump Kitty_DP_Cycle

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
                                                if Trigger2:
                                                     $ KittyX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")

                                    "Shift primary action":
                                            if KittyX.Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in her ass.":
                                                                $ Situation = "shift"
                                                                call Kitty_DP_After
                                                                call Kitty_Insert_Ass
                                                        "Just stick a finger in her ass without asking.":
                                                                $ Situation = "auto"
                                                                call Kitty_DP_After
                                                                call Kitty_Insert_Ass
                                                        "I want to shift the dildo to her ass.":
                                                                $ Situation = "shift"
                                                                call Kitty_DP_After
                                                                call Kitty_Dildo_Ass
                                                        "Never Mind":
                                                                jump Kitty_DP_Cycle
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Kitty_DP_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [KittyX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(KittyX)
                                            "Ask [KittyX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(KittyX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(KittyX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Kitty_DP_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Kitty_DP_Cycle
                                            "Never mind":
                                                        jump Kitty_DP_Cycle
                                    "Undress [KittyX.Name]":
                                            call Girl_Undress(KittyX)
                                    "Clean up [KittyX.Name] (locked)" if not KittyX.Spunk:
                                            pass
                                    "Clean up [KittyX.Name]" if KittyX.Spunk:
                                            call Girl_Cleanup(KittyX,"ask")
                                    "Never mind":
                                            jump Kitty_DP_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Kitty_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Kitty_DP_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Kitty_Pos_Reset
                                    $ Line = 0
                                    jump Kitty_DP_After
        #End menu (if Line)

        if KittyX.Panties or KittyX.PantsNum() > 6 or KittyX.HoseNum() >= 5: #This checks if Kitty wants to strip down.
                call Girl_Undress(KittyX,"auto")

        call Shift_Focus(KittyX)
        call Sex_Dialog(KittyX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or KittyX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(KittyX)
                            if "angry" in KittyX.RecentActions:
                                call Kitty_Pos_Reset
                                return
                            $ KittyX.Statup("Lust", 200, 5)
                            if 100 > KittyX.Lust >= 70 and KittyX.OCount < 2:
                                $ KittyX.RecentActions.append("unsatisfied")
                                $ KittyX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Kitty_DP_After
                            $ Line = "came"

                    if KittyX.Lust >= 100:
                            #If Kitty can cum
                            call Girl_Cumming(KittyX)
                            if Situation == "shift" or "angry" in KittyX.RecentActions:
                                jump Kitty_DP_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in KittyX.RecentActions:#And Kitty is unsatisfied,
                                "[KittyX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Kitty_DP_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if KittyX.SEXP >= 100 or ApprovalCheck(KittyX, 1200, "LO"):
            pass
        elif Cnt == (5 + KittyX.DildoP):
                    $ KittyX.Brows = "confused"
                    ch_k "What are you even doing down there?"
        elif KittyX.Lust >= 80:
                    pass
        elif Cnt == (15 + KittyX.DildoP) and KittyX.SEXP >= 15 and not ApprovalCheck(KittyX, 1500):
                    $ KittyX.Brows = "confused"
                    menu:
                        ch_k "[KittyX.Petname], this is getting uncomfortable, maybe we could try something else."
                        "Finish up.":
                                "You let go. . ."
                                jump Kitty_DP_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Kitty_DP_After
                        "No, this is fun.":
                                if ApprovalCheck(KittyX, 1200) or ApprovalCheck(KittyX, 500, "O"):
                                    $ KittyX.Statup("Love", 200, -5)
                                    $ KittyX.Statup("Obed", 50, 3)
                                    $ KittyX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ KittyX.FaceChange("angry", 1)
                                    call Kitty_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_k "Well if that's your attitude, I don't need your \"help\"."
                                    $ KittyX.Statup("Love", 50, -3, 1)
                                    $ KittyX.Statup("Love", 80, -4, 1)
                                    $ KittyX.Statup("Obed", 30, -1, 1)
                                    $ KittyX.Statup("Obed", 50, -1, 1)
                                    $ KittyX.RecentActions.append("angry")
                                    $ KittyX.DailyActions.append("angry")
                                    jump Kitty_DP_After
        #End Count check

        if Round == 10:
            ch_k "It's kind of time to get moving."
        elif Round == 5:
            ch_k "For real[KittyX.like]time's up."

    #Round = 0 loop breaks
    $ KittyX.FaceChange("bemused", 0)
    $ Line = 0
    ch_k "Ok, we need to take a break."


label Kitty_DP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Kitty_Pos_Reset

    $ KittyX.FaceChange("sexy")

    $ KittyX.DildoP += 1
    $ KittyX.Action -=1

    call Partner_Like(KittyX,1)

    if KittyX.DildoP == 1:
            $ KittyX.SEXP += 10
            if not Situation:
                if KittyX.Love >= 500 and "unsatisfied" not in KittyX.RecentActions:
                    ch_k "Thanks for the extra hand. . ."
                elif KittyX.Obed <= 500 and Player.Focus <= 20:
                    $ KittyX.FaceChange("perplexed", 1)
                    ch_k "Did you like that?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_k "Mmm, so what else did you have in mind?"
    call Checkout
    return

# end KittyX.Dildo Pussy /////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////Start Insert Ass

label Kitty_Dildo_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(KittyX)
    call Kitty_Dildo_Check
    if not _return:
        return

    if KittyX.Loose:
        $ temp_modifier += 30
    elif "anal" in KittyX.RecentActions or "dildo anal" in KittyX.RecentActions:
        $ temp_modifier -= 20
    elif "anal" in KittyX.DailyActions or "dildo anal" in KittyX.DailyActions:
        $ temp_modifier -= 10
    elif (KittyX.Anal + KittyX.DildoA + KittyX.Plug) > 0: #You've done it before
        $ temp_modifier += 20

    if KittyX.PantsNum() > 6: # she's got pants on.
        $ temp_modifier -= 20

    if KittyX.Lust > 95:
        $ temp_modifier += 20
    elif KittyX.Lust > 85: #She's really horny
        $ temp_modifier += 15

    if Situation == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in KittyX.Traits:
        $ temp_modifier += (5*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.Petnames:
        $ temp_modifier += 10
    elif "ex" in KittyX.Traits:
        $ temp_modifier -= 40
    if KittyX.ForcedCount and not KittyX.Forced:
        $ temp_modifier -= 5 * KittyX.ForcedCount

    if Taboo and "tabno" in KittyX.DailyActions:
        $ temp_modifier -= 10

    if "no dildo" in KittyX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no dildo" in KittyX.RecentActions else 0

    $ Approval = ApprovalCheck(KittyX, 1450, TabM = 4) # 145, 160, 175, Taboo -160(355)

    if Situation == KittyX:
            #Kitty auto-starts
            if Approval > 2:                                                      # fix, add kitty auto stuff here
                if KittyX.PantsNum() == 5:
                    "[KittyX.Name] grabs her dildo, hiking up her skirt as she does."
                    $ KittyX.Upskirt = 1
                elif KittyX.PantsNum() > 6:
                    "[KittyX.Name] grabs her dildo, pulling down her pants as she does."
                    $ KittyX.Legs = 0
                else:
                    "[KittyX.Name] grabs her dildo, rubbing is suggestively against her ass."
                $ KittyX.SeenPanties = 1
                "She slides the tip against her asshole, and seems to want you to insert it."
                menu:
                    "What do you do?"
                    "Nothing.":
                        $ KittyX.Statup("Inbt", 80, 3)
                        $ KittyX.Statup("Inbt", 50, 2)
                        "[KittyX.Name] slides it in."
                    "Go for it.":
                        $ KittyX.FaceChange("sexy", 1)
                        $ KittyX.Statup("Inbt", 80, 3)
                        ch_p "Oh yeah, [KittyX.Pet], let's do this."
                        $ KittyX.NameCheck() #checks reaction to petname
                        "You grab the dildo and slide it in."
                        $ KittyX.Statup("Love", 85, 1)
                        $ KittyX.Statup("Obed", 90, 1)
                        $ KittyX.Statup("Obed", 50, 2)
                    "Ask her to stop.":
                        $ KittyX.FaceChange("surprised")
                        $ KittyX.Statup("Inbt", 70, 1)
                        ch_p "Let's not do that right now, [KittyX.Pet]."
                        $ KittyX.NameCheck() #checks reaction to petname
                        "[KittyX.Name] sets the dildo down."
                        $ KittyX.OutfitChange()
                        $ KittyX.Statup("Obed", 90, 1)
                        $ KittyX.Statup("Obed", 50, 1)
                        $ KittyX.Statup("Obed", 30, 2)
                        return
                jump Kitty_DA_Prep
            else:
                $ temp_modifier = 0                               # fix, add kitty auto stuff here
                $ Trigger2 = 0
            return

    if Situation == "auto":
            "You rub the dildo across her body, and against her tight anus."
            $ KittyX.FaceChange("surprised", 1)

            if (KittyX.DildoA and Approval) or (Approval > 1):
                #this is not the first time you've had sex, or she's into it
                "[KittyX.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                $ KittyX.FaceChange("sexy")
                $ KittyX.Statup("Obed", 70, 3)
                $ KittyX.Statup("Inbt", 50, 3)
                $ KittyX.Statup("Inbt", 70, 1)
                ch_k "Ooo, [KittyX.Petname], toys!"
                jump Kitty_DA_Prep
            else:
                #she's questioning it
                $ KittyX.Brows = "angry"
                menu:
                    ch_k "Hey, what are you planning to do with that?!"
                    "Sorry, sorry! Never mind.":
                        if Approval:
                            $ KittyX.FaceChange("sexy", 1)
                            $ KittyX.Statup("Obed", 70, 3)
                            $ KittyX.Statup("Inbt", 50, 3)
                            $ KittyX.Statup("Inbt", 70, 1)
                            ch_k "Well, now that you mention it. . ."
                            jump Kitty_DA_Prep
                        "You pull back before you really get it in."
                        $ KittyX.FaceChange("bemused", 1)
                        if KittyX.DildoA:
                            ch_k "Well ok, [KittyX.Petname], maybe warn me next time?"
                        else:
                            ch_k "Well ok, [KittyX.Petname], that's a little much. . . for now . . ."
                    "Just playing with my favorite toys.":
                        $ KittyX.Statup("Love", 80, -10, 1)
                        $ KittyX.Statup("Love", 200, -10)
                        "You press it inside some more."
                        $ KittyX.Statup("Obed", 70, 3)
                        $ KittyX.Statup("Inbt", 50, 3)
                        if not ApprovalCheck(KittyX, 700, "O", TabM=1): #Checks if Obed is 700+
                            $ KittyX.FaceChange("angry")
                            "[KittyX.Name] shoves you away and slaps you in the face."
                            ch_k "Jerk!"
                            ch_k "Ask nice if you want to stick something in my ass!"
                            $ KittyX.Statup("Love", 50, -10, 1)
                            $ KittyX.Statup("Obed", 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            if renpy.showing("Kitty_SexSprite"):
                                call Kitty_Sex_Reset
                            $ KittyX.RecentActions.append("angry")
                            $ KittyX.DailyActions.append("angry")
                        else:
                            $ KittyX.FaceChange("sad")
                            "[KittyX.Name] doesn't seem to be into this, you're lucky she's so obedient."
                            jump Kitty_DA_Prep
            return
    #end auto

    if not KittyX.DildoA:
            #first time
            $ KittyX.FaceChange("surprised", 1)
            $ KittyX.Mouth = "kiss"
            ch_k "You want to try and fit that. . .?"
            if KittyX.Forced:
                $ KittyX.FaceChange("sad")
                ch_k "Always about the butt, huh?"

    if not KittyX.Loose and ("dildo anal" in KittyX.RecentActions or "anal" in KittyX.RecentActions or "dildo anal" in KittyX.DailyActions or "anal" in KittyX.DailyActions):
            $ KittyX.FaceChange("bemused", 1)
            ch_k "I'm still[KittyX.like]sore from earlier. . ."

    if not KittyX.DildoA and Approval:
            #First time dialog
            if KittyX.Forced:
                $ KittyX.FaceChange("sad")
                $ KittyX.Statup("Love", 70, -3, 1)
                $ KittyX.Statup("Love", 20, -2, 1)
            elif KittyX.Love >= (KittyX.Obed + KittyX.Inbt):
                $ KittyX.FaceChange("sexy")
                $ KittyX.Brows = "sad"
                $ KittyX.Mouth = "smile"
                ch_k "I[KittyX.like]haven't actually used one of these, back there before. . ."
            elif KittyX.Obed >= KittyX.Inbt:
                $ KittyX.FaceChange("normal")
                ch_k "If that's what you want, [KittyX.Petname]. . ."
            else: # Uninhibited
                $ KittyX.FaceChange("sad")
                $ KittyX.Mouth = "smile"
                ch_k "I guess it could be fun two-player. . ."

    elif Approval:
            #Second time+ dialog
            if KittyX.Forced:
                $ KittyX.FaceChange("sad")
                $ KittyX.Statup("Love", 70, -3, 1)
                $ KittyX.Statup("Love", 20, -2, 1)
                ch_k "The toys again?"
            elif not Taboo and "tabno" in KittyX.DailyActions:
                ch_k "Well, at least you got us some privacy this time. . ."
            elif "dildo anal" in KittyX.DailyActions and not KittyX.Loose:
                pass
            elif "dildo anal" in KittyX.DailyActions:
                $ KittyX.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Breaking out the toys again?",
                    "Didn't get enough earlier?",
                    "I'm still a bit sore from earlier.",
                    "You're going to wear me out."])
                ch_k "[Line]"
            elif KittyX.DildoA < 3:
                $ KittyX.FaceChange("sexy", 1)
                $ KittyX.Brows = "confused"
                $ KittyX.Mouth = "kiss"
                ch_k "You want to stick it in my ass again?"
            else:
                $ KittyX.FaceChange("sexy", 1)
                $ KittyX.ArmPose = 2
                $ Line = renpy.random.choice(["You want some of this action?",
                    "So you'd like another go?",
                    "You want to stick it in my ass again?",
                    "You want me ta lube up your toy?"])
                ch_k "[Line]"
                $ Line = 0

    if Approval >= 2:
            #She's into it. . .
            if KittyX.Forced:
                $ KittyX.FaceChange("sad")
                $ KittyX.Statup("Obed", 90, 1)
                $ KittyX.Statup("Inbt", 60, 1)
                ch_k "Ok, fine."
            else:
                $ KittyX.FaceChange("sexy", 1)
                $ KittyX.Statup("Love", 90, 1)
                $ KittyX.Statup("Inbt", 50, 3)
                $ Line = renpy.random.choice(["Well, sure, stick it in.",
                    "Well. . . ok.",
                    "Sure!",
                    "I guess I could. . . stick it in.",
                    "Hells yeah.",
                    "Heh, ok, ok."])
                ch_k "[Line]"
                $ Line = 0
            $ KittyX.Statup("Obed", 20, 1)
            $ KittyX.Statup("Obed", 60, 1)
            $ KittyX.Statup("Inbt", 70, 2)
            jump Kitty_DA_Prep

    else:
            #She's not into it, but maybe. . .
            $ KittyX.FaceChange("angry")
            if "no dildo" in KittyX.RecentActions:
                ch_k "What part of \"no,\" did you not get, [KittyX.Petname]?"
            elif Taboo and "tabno" in KittyX.DailyActions and "no dildo" in KittyX.DailyActions:
                ch_k "Stop swinging that thing around in public!"
            elif "no dildo" in KittyX.DailyActions:
                ch_k "I already told you \"no,\" [KittyX.Petname]."
            elif Taboo and "tabno" in KittyX.DailyActions:
                ch_k "I already told you that I wouldn't do that out here!"
            elif not KittyX.DildoA:
                $ KittyX.FaceChange("bemused")
                ch_k "I'm just not into toys, [KittyX.Petname]. . ."
            elif not KittyX.Loose and "dildo anal" not in KittyX.DailyActions:
                $ KittyX.FaceChange("perplexed")
                ch_k "You could have been a bit more gentle last time, [KittyX.Petname]. . ."
            else:
                $ KittyX.FaceChange("bemused")
                ch_k "I don't think we need any toys, [KittyX.Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in KittyX.DailyActions:
                    $ KittyX.FaceChange("bemused")
                    ch_k "Yeah, ok, [KittyX.Petname]."
                    return
                "Maybe later?" if "no dildo" not in KittyX.DailyActions:
                    $ KittyX.FaceChange("sexy")
                    ch_k "Maybe I'll practice on my own time, [KittyX.Petname]."
                    $ KittyX.Statup("Love", 80, 2)
                    $ KittyX.Statup("Inbt", 70, 2)
                    if Taboo:
                        $ KittyX.RecentActions.append("tabno")
                        $ KittyX.DailyActions.append("tabno")
                    $ KittyX.RecentActions.append("no dildo")
                    $ KittyX.DailyActions.append("no dildo")
                    return
                "I think you'd like it. . .":
                    if Approval:
                        $ KittyX.FaceChange("sexy")
                        $ KittyX.Statup("Obed", 90, 2)
                        $ KittyX.Statup("Obed", 50, 2)
                        $ KittyX.Statup("Inbt", 70, 3)
                        $ KittyX.Statup("Inbt", 40, 2)
                        $ Line = renpy.random.choice(["Well, sure, stick it in.",
                            "I suppose. . .",
                            "You've got me there."])
                        ch_k "[Line]"
                        $ Line = 0
                        jump Kitty_DA_Prep
                    else:
                        pass

                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck(KittyX, 1050, "OI", TabM = 3) # 105, 120, 135, -120(225)
                    if Approval > 1 or (Approval and KittyX.Forced):
                        $ KittyX.FaceChange("sad")
                        $ KittyX.Statup("Love", 70, -5, 1)
                        $ KittyX.Statup("Love", 200, -5)
                        ch_k "Ok, fine. If we're going to do this, stick it in already."
                        $ KittyX.Statup("Obed", 80, 4)
                        $ KittyX.Statup("Inbt", 80, 1)
                        $ KittyX.Statup("Inbt", 60, 3)
                        $ KittyX.Forced = 1
                        jump Kitty_DA_Prep
                    else:
                        $ KittyX.Statup("Love", 200, -20)
                        $ KittyX.RecentActions.append("angry")
                        $ KittyX.DailyActions.append("angry")

    #She refused all offers.
    $ KittyX.ArmPose = 1
    if "no dildo" in KittyX.DailyActions:
            ch_k "Learn to take \"no\" for an answer, [KittyX.Petname]."
            $ KittyX.RecentActions.append("angry")
            $ KittyX.DailyActions.append("angry")
    elif KittyX.Forced:
            $ KittyX.FaceChange("angry", 1)
            ch_k "I'm not going to let you use that on me."
            $ KittyX.Statup("Lust", 200, 5)
            if KittyX.Love > 300:
                    $ KittyX.Statup("Love", 70, -2)
            $ KittyX.Statup("Obed", 50, -2)
            $ KittyX.RecentActions.append("angry")
            $ KittyX.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
            $ KittyX.FaceChange("angry", 1)
            $ KittyX.RecentActions.append("tabno")
            $ KittyX.DailyActions.append("tabno")
            ch_k "Not here!"
            $ KittyX.Statup("Lust", 200, 5)
            $ KittyX.Statup("Obed", 50, -3)
    elif not KittyX.Loose and "dildo anal" in KittyX.DailyActions:
            $ KittyX.FaceChange("bemused")
            ch_k "Sorry, I just need a little break back there, [KittyX.Petname]."
    elif KittyX.DildoA:
            $ KittyX.FaceChange("sad")
            ch_k "Sorry, you can keep your toys out of there."
    else:
            $ KittyX.FaceChange("normal", 1)
            ch_k "No way."
    $ KittyX.RecentActions.append("no dildo")
    $ KittyX.DailyActions.append("no dildo")
    $ temp_modifier = 0
    return

label Kitty_DA_Prep: #Animation set-up
    if Trigger2 == "dildo anal":
        return

    if not KittyX.Forced and Situation != "auto":
        $ temp_modifier = 20 if KittyX.PantsNum() > 6 else 0
        call Bottoms_Off(KittyX)
        if "angry" in KittyX.RecentActions:
            return

    $ temp_modifier = 0
    call Kitty_Pussy_Launch("dildo anal")
    if not KittyX.DildoA:
        if KittyX.Forced:
            $ KittyX.Statup("Love", 90, -75)
            $ KittyX.Statup("Obed", 70, 60)
            $ KittyX.Statup("Inbt", 80, 35)
        else:
            $ KittyX.Statup("Love", 90, 10)
            $ KittyX.Statup("Obed", 70, 20)
            $ KittyX.Statup("Inbt", 80, 45)
    if Taboo:
        $ KittyX.Inbt += int(Taboo/10)
        $ KittyX.Lust += int(Taboo/5)


    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ KittyX.DrainWord("tabno")
    $ KittyX.DrainWord("no dildo")
    $ KittyX.RecentActions.append("dildo anal")
    $ KittyX.DailyActions.append("dildo anal")

label Kitty_DA_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(KittyX)
        call Kitty_Pussy_Launch("dildo anal")
        $ KittyX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                call Slap_Ass(KittyX)
                                jump Kitty_DA_Cycle

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
                                                if Trigger2:
                                                     $ KittyX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")

                                    "Shift primary action":
                                            if KittyX.Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in her pussy.":
                                                                $ Situation = "shift"
                                                                call Kitty_DA_After
                                                                call Kitty_Fondle_Pussy
                                                        "Just stick a finger in her pussy without asking.":
                                                                $ Situation = "auto"
                                                                call Kitty_DA_After
                                                                call Kitty_Fondle_Pussy
                                                        "I want to shift the dildo to her pussy.":
                                                                $ Situation = "shift"
                                                                call Kitty_DA_After
                                                                call Kitty_Dildo_Pussy
                                                        "Never Mind":
                                                                jump Kitty_DA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Kitty_DA_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [KittyX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(KittyX)
                                            "Ask [KittyX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(KittyX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(KittyX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Kitty_DA_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Kitty_DA_Cycle
                                    "Never mind":
                                            jump Kitty_DA_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Kitty_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Kitty_DA_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Kitty_Pos_Reset
                                    $ Line = 0
                                    jump Kitty_DA_After
        #End menu (if Line)

        if KittyX.Panties or KittyX.PantsNum() > 6 or KittyX.HoseNum() >= 5: #This checks if Kitty wants to strip down.
                call Girl_Undress(KittyX,"auto")

        call Shift_Focus(KittyX)
        call Sex_Dialog(KittyX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or KittyX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(KittyX)
                            if "angry" in KittyX.RecentActions:
                                call Kitty_Pos_Reset
                                return
                            $ KittyX.Statup("Lust", 200, 5)
                            if 100 > KittyX.Lust >= 70 and KittyX.OCount < 2:
                                $ KittyX.RecentActions.append("unsatisfied")
                                $ KittyX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Kitty_DA_After
                            $ Line = "came"

                    if KittyX.Lust >= 100:
                            #If Kitty can cum
                            call Girl_Cumming(KittyX)
                            if Situation == "shift" or "angry" in KittyX.RecentActions:
                                jump Kitty_DA_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in KittyX.RecentActions:#And Kitty is unsatisfied,
                                "[KittyX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Kitty_DA_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if KittyX.SEXP >= 100 or ApprovalCheck(KittyX, 1200, "LO"):
            pass
        elif Cnt == (5 + KittyX.DildoA):
                    $ KittyX.Brows = "confused"
                    ch_k "What are you even doing down there?"
        elif KittyX.Lust >= 80:
                    pass
        elif Cnt == (15 + KittyX.DildoA) and KittyX.SEXP >= 15 and not ApprovalCheck(KittyX, 1500):
                    $ KittyX.Brows = "confused"
                    menu:
                        ch_k "[KittyX.Petname], this is getting uncomfortable, maybe we could try something else."
                        "Finish up.":
                                "You let go. . ."
                                jump Kitty_DA_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Kitty_DA_After
                        "No, this is fun.":
                                if ApprovalCheck(KittyX, 1200) or ApprovalCheck(KittyX, 500, "O"):
                                    $ KittyX.Statup("Love", 200, -5)
                                    $ KittyX.Statup("Obed", 50, 3)
                                    $ KittyX.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ KittyX.FaceChange("angry", 1)
                                    call Kitty_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_k "Well if that's your attitude, I don't need your \"help\"."
                                    $ KittyX.Statup("Love", 50, -3, 1)
                                    $ KittyX.Statup("Love", 80, -4, 1)
                                    $ KittyX.Statup("Obed", 30, -1, 1)
                                    $ KittyX.Statup("Obed", 50, -1, 1)
                                    $ KittyX.RecentActions.append("angry")
                                    $ KittyX.DailyActions.append("angry")
                                    jump Kitty_DA_After
        #End Count check

        if Round == 10:
            ch_k "It's kind of time to get moving."
        elif Round == 5:
            ch_k "For real[KittyX.like]time's up."

    #Round = 0 loop breaks
    $ KittyX.FaceChange("bemused", 0)
    $ Line = 0
    ch_k "Ok, we need to take a break."

label Kitty_DA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Kitty_Pos_Reset

    $ KittyX.FaceChange("sexy")

    $ KittyX.DildoA += 1
    $ KittyX.Action -=1

    call Partner_Like(KittyX,1)

    if KittyX.DildoA == 1:
            $ KittyX.SEXP += 10
            if not Situation:
                if KittyX.Love >= 500 and "unsatisfied" not in KittyX.RecentActions:
                    if KittyX.Loose:
                        ch_k "That was. . . interesting. . ."
                    else:
                        ch_k "Ouch. . ."
                elif KittyX.Obed <= 500 and Player.Focus <= 20:
                    $ KittyX.FaceChange("perplexed", 1)
                    ch_k "Did you like that?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_k "Mmm, so what else did you have in mind?"
    call Checkout
    return

# end KittyX.Dildo Ass /////////////////////////////////////////////////////////////////////////////

label Kitty_Vibrator_Check:                                                                                 #fix this whole section is copy/paste unfinished
    if "vibrator" in Player.Inventory:
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in KittyX.Inventory:
        "You ask [KittyX.Name] to get out her vibrator."
    else:
        "You don't have one of those on you."
        return 0
    return 1

## KittyX.Footjob //////////////////////////////////////////////////////////////////////
label Kitty_Footjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(KittyX)
    if KittyX.Foot >= 7: # She loves it
        $ temp_modifier += 10
    elif KittyX.Foot >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif KittyX.Foot: #You've done it before
        $ temp_modifier += 3

    if KittyX.Addict >= 75 and KittyX.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 10
    if KittyX.Addict >= 75:
        $ temp_modifier += 5

    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in KittyX.Traits:
        $ temp_modifier += (3*Taboo)
    if KittyX in Player.Harem or "sex friend" in KittyX.Petnames:
        $ temp_modifier += 10
    elif "ex" in KittyX.Traits:
        $ temp_modifier -= 40
    if KittyX.ForcedCount and not KittyX.Forced:
        $ temp_modifier -= 5 * KittyX.ForcedCount

    if Taboo and "tabno" in KittyX.DailyActions:
        $ temp_modifier -= 10

    if "no foot" in KittyX.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no foot" in KittyX.RecentActions else 0

    $ Approval = ApprovalCheck(KittyX, 1250, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if Situation == KittyX:                                                                  #Kitty auto-starts
        if Approval > 2:                                                      # fix, add kitty auto stuff here
            "[KittyX.Name] leans back  and starts rubbing your cock between her feet."
            menu:
                "What do you do?"
                "Nothing.":
                    $ KittyX.Statup("Inbt", 70, 3)
                    $ KittyX.Statup("Inbt", 30, 2)
                    "[KittyX.Name] continues her actions."
                "Praise her.":
                    $ KittyX.FaceChange("sexy", 1)
                    $ KittyX.Statup("Inbt", 70, 3)
                    ch_p "Oooh, that's good, [KittyX.Pet]."
                    $ KittyX.NameCheck() #checks reaction to petname
                    "[KittyX.Name] continues her actions."
                    $ KittyX.Statup("Love", 80, 1)
                    $ KittyX.Statup("Obed", 90, 1)
                    $ KittyX.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ KittyX.FaceChange("surprised")
                    $ KittyX.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [KittyX.Pet]."
                    $ KittyX.NameCheck() #checks reaction to petname
                    "[KittyX.Name] puts it down."
                    $ KittyX.Statup("Obed", 90, 1)
                    $ KittyX.Statup("Obed", 50, 1)
                    $ KittyX.Statup("Obed", 30, 2)
                    return
            if Trigger:
                $ Trigger3 = "foot"
                return
            jump Kitty_FJ_Prep
        else:
            $ temp_modifier = 0                               # fix, add kitty auto stuff here
            $ Trigger2 = 0
            return

    if not KittyX.Foot and "no foot" not in KittyX.RecentActions:
        $ KittyX.FaceChange("confused", 2)
        ch_k "Huh, so you'd like me to touch your cock with my feet?"
        $ KittyX.Blush = 1

    if not KittyX.Foot and Approval:                                                 #First time dialog
        if KittyX.Forced:
            $ KittyX.FaceChange("sad",1)
            $ KittyX.Statup("Love", 70, -3, 1)
            $ KittyX.Statup("Love", 20, -2, 1)
        elif KittyX.Love >= (KittyX.Obed + KittyX.Inbt):
            $ KittyX.FaceChange("sexy",1)
            $ KittyX.Brows = "sad"
            $ KittyX.Mouth = "smile"
            ch_k "I guess it couldn't hurt. . ."
        elif KittyX.Obed >= KittyX.Inbt:
            $ KittyX.FaceChange("normal",1)
            ch_k "If you want, [KittyX.Petname]. . ."
        elif KittyX.Addict >= 50:
            $ KittyX.FaceChange("manic", 1)
            ch_k "Okay. . ."
        else: # Uninhibited
            $ KittyX.FaceChange("lipbite",1)
            ch_k "Sure. . ."

    elif Approval:                                                                       #Second time+ dialog
        if KittyX.Forced:
            $ KittyX.FaceChange("sad")
            $ KittyX.Statup("Love", 70, -3, 1)
            $ KittyX.Statup("Love", 20, -2, 1)
            ch_k "That's all?"
        elif not Taboo and "tabno" in KittyX.DailyActions:
            ch_k "Um, I guess this is secluded enough. . ."
        elif "foot" in KittyX.RecentActions:
            $ KittyX.FaceChange("sexy", 1)
            ch_k "I'm getting foot cramps. . ."
            jump Kitty_FJ_Prep
        elif "foot" in KittyX.DailyActions:
            $ KittyX.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Another one?",
                "You're going to give me calluses.",
                "Didn't get enough earlier?",
                "My feet are kinda sore from earlier.",
                "My feet are kinda sore from earlier."])
            ch_k "[Line]"
        elif KittyX.Foot < 3:
            $ KittyX.FaceChange("sexy", 1)
            $ KittyX.Brows = "confused"
            $ KittyX.Mouth = "kiss"
            ch_k "Hmm, magic toes. . ."
        else:
            $ KittyX.FaceChange("sexy", 1)
            $ KittyX.ArmPose = 2
            $ Line = renpy.random.choice(["You want me to use my feet?",
                "So you'd like another foot sesh?",
                "A little. . . [she rubs her foot along your leg]?",
                "A little TLC?"])
            ch_k "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if KittyX.Forced:
            $ KittyX.FaceChange("sad")
            $ KittyX.Statup("Obed", 90, 1)
            $ KittyX.Statup("Inbt", 60, 1)
            ch_k "Ok, fine."
        elif "no foot" in KittyX.DailyActions:
            ch_k "OK, geeze!"
        else:
            $ KittyX.FaceChange("sexy", 1)
            $ KittyX.Statup("Love", 90, 1)
            $ KittyX.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Sure, I guess.",
                "Ooooookay.",
                "Cool, lemme see it.",
                "I guess I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Heh, ok, ok."])
            ch_k "[Line]"
            $ Line = 0
        $ KittyX.Statup("Obed", 20, 1)
        $ KittyX.Statup("Obed", 60, 1)
        $ KittyX.Statup("Inbt", 70, 2)
        jump Kitty_FJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ KittyX.FaceChange("angry")
        if "no foot" in KittyX.RecentActions:
            ch_k "You don't[KittyX.like]listen do you, [KittyX.Petname]."
        elif Taboo and "tabno" in KittyX.DailyActions and "no foot" in KittyX.DailyActions:
            ch_k "I said not in public!"
        elif "no foot" in KittyX.DailyActions:
            ch_k "I told you \"no,\" [KittyX.Petname]."
        elif Taboo and "tabno" in KittyX.DailyActions:
            ch_k "I said not in public!"
        elif not KittyX.Foot:
            $ KittyX.FaceChange("bemused")
            ch_k "I don't know, [KittyX.Petname]. . ."
        else:
            $ KittyX.FaceChange("bemused")
            ch_k "Not now, ok?"
        menu:
            extend ""
            "Sorry, never mind." if "no foot" in KittyX.DailyActions:
                $ KittyX.FaceChange("bemused")
                ch_k "Yeah."
                return
            "Maybe later?" if "no foot" not in KittyX.DailyActions:
                $ KittyX.FaceChange("sexy")
                ch_k ". . ."
                ch_k "Maybe."
                $ KittyX.Statup("Love", 80, 2)
                $ KittyX.Statup("Inbt", 70, 2)
                if Taboo:
                    $ KittyX.RecentActions.append("tabno")
                    $ KittyX.DailyActions.append("tabno")
                $ KittyX.RecentActions.append("no foot")
                $ KittyX.DailyActions.append("no foot")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ KittyX.FaceChange("sexy")
                    $ KittyX.Statup("Obed", 90, 2)
                    $ KittyX.Statup("Obed", 50, 2)
                    $ KittyX.Statup("Inbt", 70, 3)
                    $ KittyX.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Sure, I guess.",
                            "Ooooookay.",
                            "Cool, lemme see it.",
                            "I guess I could. . .",
                            "Ok. . . [She gestures for you to come over].",
                            "Heh, ok, ok."])
                    ch_k "[Line]"
                    $ Line = 0
                    jump Kitty_FJ_Prep
                else:
                    pass

            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck(KittyX, 400, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and KittyX.Forced):
                    $ KittyX.FaceChange("sad")
                    $ KittyX.Statup("Love", 70, -5, 1)
                    $ KittyX.Statup("Love", 200, -2)
                    ch_k "Ok, fine."
                    $ KittyX.Statup("Obed", 50, 4)
                    $ KittyX.Statup("Inbt", 80, 1)
                    $ KittyX.Statup("Inbt", 60, 3)
                    $ KittyX.Forced = 1
                    jump Kitty_FJ_Prep
                else:
                    $ KittyX.Statup("Love", 200, -15)
                    $ KittyX.RecentActions.append("angry")
                    $ KittyX.DailyActions.append("angry")

    #She refused all offers.
    $ KittyX.ArmPose = 1
    if "no foot" in KittyX.DailyActions:
        $ KittyX.FaceChange("angry", 1)
        ch_k "I'm not telling you again."
        $ KittyX.RecentActions.append("angry")
        $ KittyX.DailyActions.append("angry")
    elif KittyX.Forced:
        $ KittyX.FaceChange("angry", 1)
        ch_k "I don't even want to step on it."
        $ KittyX.Statup("Lust", 200, 5)
        if KittyX.Love > 300:
                $ KittyX.Statup("Love", 70, -2)
        $ KittyX.Statup("Obed", 50, -2)
        $ KittyX.RecentActions.append("angry")
        $ KittyX.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ KittyX.FaceChange("angry", 1)
        $ KittyX.DailyActions.append("tabno")
        ch_k "Not here, not anywhere near here."
        $ KittyX.Statup("Lust", 200, 5)
        $ KittyX.Statup("Obed", 50, -3)
    elif KittyX.Foot:
        $ KittyX.FaceChange("sad")
        ch_k "I'm not feeling it today. . ."
    else:
        $ KittyX.FaceChange("normal", 1)
        ch_k "I don't know about using my feet for. . . that."
    $ KittyX.RecentActions.append("no foot")
    $ KittyX.DailyActions.append("no foot")
    $ temp_modifier = 0
    return


label Kitty_FJ_Prep:
    if Trigger2 == "foot":
        return

    if Taboo:
        $ KittyX.Inbt += int(Taboo/10)
        $ KittyX.Lust += int(Taboo/5)

    $ KittyX.FaceChange("sexy")
    if KittyX.Forced:
        $ KittyX.FaceChange("sad")
    elif not KittyX.Foot:
        $ KittyX.Brows = "confused"
        $ KittyX.Eyes = "sexy"
        $ KittyX.Mouth = "smile"

    call Seen_First_Peen(KittyX,Partner,React=Situation)

    if not KittyX.Foot:
        if KittyX.Forced:
            $ KittyX.Statup("Love", 90, -20)
            $ KittyX.Statup("Obed", 70, 25)
            $ KittyX.Statup("Inbt", 80, 30)
        else:
            $ KittyX.Statup("Love", 90, 5)
            $ KittyX.Statup("Obed", 70, 20)
            $ KittyX.Statup("Inbt", 80, 20)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ KittyX.DrainWord("tabno")
    $ KittyX.DrainWord("no foot")
    $ KittyX.RecentActions.append("foot")
    $ KittyX.DailyActions.append("foot")

label Kitty_FJ_Cycle:
    while Round > 0:
        call Shift_Focus(KittyX)
        call Kitty_Sex_Launch("foot")
        $ KittyX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass

                        "Start moving? . ." if not Speed:
                                    $ Speed = 1

                        "Speed up. . ." if Speed < 2:
                                    $ Speed = 2
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 2:
                                    pass

                        "Slow Down. . ." if Speed:
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:
                                    pass
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0

                        "Turn her Around":
                                    $ KittyX.Pose = "doggy" if KittyX.Pose != "doggy" else "sex"
                                    "You turn her around. . ."
                                    jump Kitty_FJ_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if KittyX.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ KittyX.Action -= 1
                                            else:
                                                ch_k "I kinda need a break, so if we could wrap this up?"

                                    "Shift primary action":
                                            if KittyX.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                    if KittyX.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Kitty_FJ_After
                                                                        call Kitty_Blowjob
                                                                    else:
                                                                        ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."
                                                        "How about a handjob?":
                                                                    if KittyX.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Kitty_FJ_After
                                                                        call Kitty_Handjob
                                                                    else:
                                                                        ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."

#                                                        "How about a titjob?":
#                                                                    if KittyX.Action and MultiAction:
#                                                                        $ Situation = "shift"
#                                                                        call Kitty_FJ_After
#                                                                        call Kitty_Titjob
#                                                                    else:
#                                                                        ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."



                                                        "Never Mind":
                                                                jump Kitty_FJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(KittyX,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [KittyX.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(KittyX)
                                            "Ask [KittyX.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(KittyX)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(KittyX)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Kitty_FJ_Cycle
                                            "Clean up [Partner.Name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.Name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Kitty_FJ_Cycle
                                            "Never mind":
                                                        jump Kitty_FJ_Cycle
                                    "Undress [KittyX.Name]":
                                            call Girl_Undress(KittyX)
                                    "Clean up [KittyX.Name] (locked)" if not KittyX.Spunk:
                                            pass
                                    "Clean up [KittyX.Name]" if KittyX.Spunk:
                                            call Girl_Cleanup(KittyX,"ask")
                                    "Never mind":
                                            jump Kitty_FJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Kitty_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Kitty_FJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Kitty_Sex_Reset
                                    $ Line = 0
                                    jump Kitty_FJ_After
        #End menu (if Line)

        call Shift_Focus(KittyX)
        call Sex_Dialog(KittyX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or KittyX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(KittyX)
                            if "angry" in KittyX.RecentActions:
                                call Kitty_Sex_Reset
                                return
                            $ KittyX.Statup("Lust", 200, 5)
                            if 100 > KittyX.Lust >= 70 and KittyX.OCount < 2:
                                $ KittyX.RecentActions.append("unsatisfied")
                                $ KittyX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Kitty_FJ_After
                            $ Line = "came"

                    if KittyX.Lust >= 100:
                            #If Kitty can cum
                            call Girl_Cumming(KittyX)
                            if Situation == "shift" or "angry" in KittyX.RecentActions:
                                jump Kitty_FJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in KittyX.RecentActions:#And Kitty is unsatisfied,
                                "[KittyX.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Kitty_FJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Cnt == 20:
                    $ KittyX.Brows = "angry"
                    menu:
                        ch_k "Ouch, foot cramp, can we[KittyX.like]take a break?"
                        "How about a BJ?" if KittyX.Action and MultiAction:
                                $ Situation = "shift"
                                call Kitty_FJ_After
                                call Kitty_Blowjob
                        "How about a Handy?" if KittyX.Action and MultiAction:
                                $ Situation = "shift"
                                call Kitty_FJ_After
                                call Kitty_Handjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump Kitty_FJ_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Kitty_Sex_Reset
                                $ Situation = "shift"
                                jump Kitty_FJ_After
                        "No, get back down there.":
                                if ApprovalCheck(KittyX, 1200) or ApprovalCheck(KittyX, 500, "O"):
                                    $ KittyX.Statup("Love", 200, -5)
                                    $ KittyX.Statup("Obed", 50, 3)
                                    $ KittyX.Statup("Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    $ KittyX.FaceChange("angry", 1)
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_k "Hey, I've got better things to do if you're[KittyX.like]going to be a dick about it."
                                    $ KittyX.Statup("Love", 50, -3, 1)
                                    $ KittyX.Statup("Love", 80, -4, 1)
                                    $ KittyX.Statup("Obed", 30, -1, 1)
                                    $ KittyX.Statup("Obed", 50, -1, 1)
                                    $ KittyX.RecentActions.append("angry")
                                    $ KittyX.DailyActions.append("angry")
                                    jump Kitty_FJ_After
        elif Cnt == 10 and KittyX.SEXP <= 100 and not ApprovalCheck(KittyX, 1200, "LO"):
                    $ KittyX.Brows = "confused"
                    ch_k "Can we[KittyX.Like]be done with this now? I'm getting sore."
        #End Count check

        call Escalation(KittyX) #sees if she wants to escalate things

        if Round == 10:
            ch_k "It's kind of time to get moving."
        elif Round == 5:
            ch_k "For real[KittyX.like]time's up."

    #Round = 0 loop breaks
    $ KittyX.FaceChange("bemused", 0)
    $ Line = 0
    ch_k "Ok, we need to take a break."

label Kitty_FJ_After:
    $ KittyX.FaceChange("sexy")

    $ KittyX.Foot += 1
    $ KittyX.Action -=1
    $ KittyX.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ KittyX.Addictionrate += 1
    $ KittyX.Statup("Lust", 90, 5)

    call Partner_Like(KittyX,1)

    if "Kittypedi" in Achievements:
            pass
    elif KittyX.Foot >= 10:
            $ KittyX.FaceChange("smile", 1)
            ch_k "I guess I've gotten pretty smooth at the \"Kittypedi.\""
            $ Achievements.append("Kittypedi")
            $ KittyX.SEXP += 5
    elif KittyX.Foot == 1:
            $ KittyX.SEXP += 10
            if KittyX.Love >= 500:
                $ KittyX.Mouth = "smile"
                ch_k "I could feel you down there. . ."
            elif Player.Focus <= 20:
                $ KittyX.Mouth = "sad"
                ch_k "Did that work out for you?"
    elif KittyX.Foot == 5:
                ch_k "Let me know any time you need me to \"foot you up.\""

    $ temp_modifier = 0
    if Situation == "shift":
        ch_k "Ok, so what were you thinking?"
    else:
        call Kitty_Sex_Reset
    call Checkout
    return

## end KittyX.Footjob //////////////////////////////////////////////////////////////////////
