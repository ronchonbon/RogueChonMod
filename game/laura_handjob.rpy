## Girl.Handjob //////////////////////////////////////////////////////////////////////
label Laura_Handjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus(Girl)
    if Girl.Hand >= 7: # She loves it
        $ temp_modifier += 10
    elif Girl.Hand >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif Girl.Hand: #You've done it before
        $ temp_modifier += 3

    if Girl.Addict >= 75 and Girl.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 15
    if Girl.Addict >= 75:
        $ temp_modifier += 5

    if action_context == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in Girl.Traits:
        $ temp_modifier += (3*Taboo)
    if Girl in Player.Harem or "sex friend" in Girl.Petnames:
        $ temp_modifier += 10
    elif "ex" in Girl.Traits:
        $ temp_modifier -= 40
    if Girl.ForcedCount and not Girl.Forced:
        $ temp_modifier -= 5 * Girl.ForcedCount

    if Taboo and "tabno" in Girl.daily_history:
        $ temp_modifier -= 10

    if "no_hand" in Girl.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no_hand" in Girl.recent_history else 0

    $ Approval = ApprovalCheck(Girl, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if not Girl.Hand and "no_hand" not in Girl.recent_history:
        $ Girl.change_face("confused", 2)
        ch_l "Handjob, huh. . ."
        $ Girl.Blush = 1

    if not Girl.Hand and Approval:                                                 #First time dialog
        if Girl.Forced:
            $ Girl.change_face("sad",1)
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
        elif Girl.love >= (Girl.obedience + Girl.inhibition):
            $ Girl.change_face("sexy",1)
            $ Girl.Brows = "sad"
            $ Girl.Mouth = "smile"
            ch_l "You'd like that. . ."
        elif Girl.obedience >= Girl.inhibition:
            $ Girl.change_face("normal",1)
            ch_l "If you want, [Girl.Petname]. . ."
        else: # Uninhibited
            $ Girl.change_face("lipbite",1)
            ch_l "Hmm. . ."

    elif Approval:                                                                       #Second time+ dialog
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
            ch_l "Nothing more than that?"
        elif not Taboo and "tabno" in Girl.daily_history:
            ch_l "Well,this is a bit more secure. . ."
        elif "handjob" in Girl.recent_history:
            $ Girl.change_face("sexy", 1)
            ch_l "Hmm, another handy then. . ."
            jump Laura_HJ_Prep
        elif "handjob" in Girl.daily_history:
            $ Girl.change_face("sexy", 1)
            $ line = renpy.random.choice(["Another one?",
                "I'm glad I don't grow calluses.",
                "Didn't get enough earlier?",
                "Again the with handjobs, huh?",
                "I guess you want more."])
            ch_l "[line]"
        elif Girl.Hand < 3:
            $ Girl.change_face("sexy", 1)
            $ Girl.Brows = "confused"
            $ Girl.Mouth = "kiss"
            ch_l "You seem to like this one. . ."
        else:
            $ Girl.change_face("sexy", 1)
            $ Girl.ArmPose = 2
            $ line = renpy.random.choice(["You want some more?",
                "So you'd like another handy?",
                "You want a. . . [fist pumping hand gestures]?",
                "Another handjob?"])
            ch_l "[line]"
        $ line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 60, 1)
            ch_l "Ok, fine."
        elif "no_hand" in Girl.daily_history:
            ch_l "If it'll get you off my back. . ."
        else:
            $ Girl.change_face("sexy", 1)
            $ Girl.change_stat("love", 90, 1)
            $ Girl.change_stat("inhibition", 50, 3)
            $ line = renpy.random.choice(["Sure, I guess.",
                "O-kay.",
                "Fine.",
                "I suppose I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Ok, ok."])
            ch_l "[line]"
            $ line = 0
        $ Girl.change_stat("obedience", 20, 1)
        $ Girl.change_stat("obedience", 60, 1)
        $ Girl.change_stat("inhibition", 70, 2)
        jump Laura_HJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ Girl.change_face("angry")
        if "no_hand" in Girl.recent_history:
            ch_l "I just told you no, [Girl.Petname]."
        elif Taboo and "tabno" in Girl.daily_history and "no_hand" in Girl.daily_history:
            ch_l "I said not in public."
        elif "no_hand" in Girl.daily_history:
            ch_l "I told you \"no,\" [Girl.Petname]."
        elif Taboo and "tabno" in Girl.daily_history:
            ch_l "I said not in public."
        elif not Girl.Hand:
            $ Girl.change_face("bemused")
            ch_l "Seriously, [Girl.Petname]. . ."
        else:
            $ Girl.change_face("bemused")
            ch_l "Nah."
        menu:
            extend ""
            "Sorry, never mind." if "no_hand" in Girl.daily_history:
                $ Girl.change_face("bemused")
                ch_l "It's fine."
                return
            "Maybe later?" if "no_hand" not in Girl.daily_history:
                $ Girl.change_face("bemused")
                ch_l "Maybe."
                $ Girl.change_stat("love", 80, 2)
                $ Girl.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ Girl.recent_history.append("tabno")
                    $ Girl.daily_history.append("tabno")
                $ Girl.recent_history.append("no_hand")
                $ Girl.daily_history.append("no_hand")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ Girl.change_face("sexy")
                    $ Girl.change_stat("obedience", 90, 2)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("inhibition", 70, 3)
                    $ Girl.change_stat("inhibition", 40, 2)
                    $ line = renpy.random.choice(["Sure, I guess.",
                        "O-kay.",
                        "Fine.",
                        "I suppose I could. . .",
                        "Ok. . . [She gestures for you to come over].",
                        "Ok, ok."])
                    ch_l "[line]"
                    $ line = 0
                    jump Laura_HJ_Prep
                else:
                    pass

            "Come on, get to work.":                                               # Pressured into it
                call forced_action(Girl, "handjob")

    #She refused all offers.
    $ Girl.ArmPose = 1
    if "no_hand" in Girl.daily_history:
        $ Girl.change_face("angry", 1)

        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
    elif Girl.Forced:
        $ Girl.change_face("angry", 1)
        ch_l "No."
        $ Girl.change_stat("lust", 200, 5)
        if Girl.love > 300:
                $ Girl.change_stat("love", 70, -2)
        $ Girl.change_stat("obedience", 50, -2)
        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ Girl.change_face("angry", 1)
        $ Girl.daily_history.append("tabno")
        ch_l "This area's too exposed."
        $ Girl.change_stat("lust", 200, 5)
        $ Girl.change_stat("obedience", 50, -3)
    elif Girl.Hand:
        $ Girl.change_face("sad")
        ch_l "I'm not into it today. . ."
    else:
        $ Girl.change_face("normal", 1)
        ch_l "I don't know where that's been lately."
    $ Girl.recent_history.append("no_hand")
    $ Girl.daily_history.append("no_hand")
    $ temp_modifier = 0
    return


label Laura_HJ_Prep:
    if offhand_action == "handjob":
        return

    if Taboo:
        $ Girl.inhibition += int(Taboo/10)
        $ Girl.lust += int(Taboo/5)

    $ Girl.change_face("sexy")
    if Girl.Forced:
        $ Girl.change_face("sad")
    elif not Girl.Hand:
        $ Girl.Brows = "confused"
        $ Girl.Eyes = "sexy"
        $ Girl.Mouth = "smile"

    call Seen_First_Peen(Girl,Partner,React=action_context)
    call Laura_HJ_Launch("L")

    if action_context == Girl:
            #Laura auto-starts
            $ action_context = 0
            if offhand_action == "jackin":
                "[Girl.Name] brushes your hand aside and starts stroking your cock."
            else:
                "[Girl.Name] gives you a mischevious smile, and starts to fondle your cock."
            menu:
                "What do you do?"
                "Nothing.":
                    $ Girl.change_stat("inhibition", 70, 3)
                    $ Girl.change_stat("inhibition", 30, 2)
                    "[Girl.Name] continues her actions."
                "Praise her.":
                    $ Girl.change_face("sexy", 1)
                    $ Girl.change_stat("inhibition", 70, 3)
                    ch_p "Oooh, that's good, [Girl.Pet]."
                    $ Girl.NameCheck() #checks reaction to petname
                    "[Girl.Name] continues her actions."
                    $ Girl.change_stat("love", 80, 1)
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ Girl.change_face("surprised")
                    $ Girl.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that for now, [Girl.Pet]."
                    $ Girl.NameCheck() #checks reaction to petname
                    "[Girl.Name] puts it down."
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Girl.change_stat("obedience", 30, 2)
                    $ Player.recent_history.append("nope")
                    $ Girl.AddWord(1,"refused","refused")
                    return

    if not Girl.Hand:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -20)
            $ Girl.change_stat("obedience", 70, 25)
            $ Girl.change_stat("inhibition", 80, 30)
        else:
            $ Girl.change_stat("love", 90, 5)
            $ Girl.change_stat("obedience", 70, 20)
            $ Girl.change_stat("inhibition", 80, 20)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ line = 0
    $ counter = 0
    if Taboo:
        $ Girl.DrainWord("tabno")
    $ Girl.DrainWord("no_hand")
    $ Girl.recent_history.append("handjob")
    $ Girl.daily_history.append("handjob")

label Laura_HJ_Cycle:
    while Round > 0:
        call shift_focus(Girl)
        call Laura_HJ_Launch
        $ Girl.lustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if action_speed:
                                    pass

                        "Start moving? . ." if not action_speed:
                                    $ action_speed = 1

                        "action_speed up. . ." if action_speed < 2:
                                    $ action_speed = 2
                                    "You ask her to up the pace a bit."
                        "action_speed up. . . (locked)" if action_speed >= 2:
                                    pass

                        "Slow Down. . ." if action_speed:
                                    $ action_speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not action_speed:
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
                                    "I also want to fondle her breasts." if offhand_action != "fondle_breasts":
                                            if Girl.Action and multi_action:
                                                $ offhand_action = "fondle_breasts"
                                                "You start to fondle her breasts."
                                                $ Girl.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Shift primary action":
                                            if Girl.Action and multi_action:
                                                    menu:
                                                        "How about a blowjob?":
                                                                    if Girl.Action and multi_action:
                                                                        $ action_context = "shift"
                                                                        call Laura_HJ_After
                                                                        call Laura_Blowjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(Girl,"tired")

                                                        "How about a titjob?":
                                                                    if Girl.Action and multi_action:
                                                                        $ action_context = "shift"
                                                                        call Laura_HJ_After
                                                                        call Laura_Titjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(Girl,"tired")
                                                        "Never Mind":
                                                                jump Laura_HJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [Girl.Name] to do something else with [Partner.Name]" if primary_action == "lesbian":
                                                        call Les_Change(Girl)
                                            "Ask [Girl.Name] to do something else with [Partner.Name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(Girl)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.Name]":
                                                        call primary_action_Swap(Girl)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Laura_HJ_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Laura_HJ_Cycle
                                            "Never mind":
                                                        jump Laura_HJ_Cycle
                                    "undress [Girl.Name]":
                                            call Girl_Undress(Girl)
                                    "Clean up [Girl.Name] (locked)" if not Girl.Spunk:
                                            pass
                                    "Clean up [Girl.Name]" if Girl.Spunk:
                                            call Girl_Cleanup(Girl,"ask")
                                    "Never mind":
                                            jump Laura_HJ_Cycle

                        "Back to Sex Menu" if multi_action:
                                    ch_p "Let's try something else."
                                    call Laura_HJ_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Laura_HJ_After
                        "End Scene" if not multi_action:
                                    ch_p "Let's stop for now."
                                    call Laura_HJ_Reset
                                    $ line = 0
                                    jump Laura_HJ_After
        #End menu (if line)

        call shift_focus(Girl)
        call Sex_Dialog(Girl,Partner)

        #If either of you could cum

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or Girl.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(Girl)
                            if "angry" in Girl.recent_history:
                                call Laura_HJ_Reset
                                return
                            $ Girl.change_stat("lust", 200, 5)
                            if 100 > Girl.lust >= 70 and Girl.OCount < 2 and Girl.SEXP >= 20:
                                $ Girl.recent_history.append("unsatisfied")
                                $ Girl.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Laura_HJ_After
                            $ line = "came"

                    if Girl.lust >= 100:
                            #If Laura can cum
                            call Girl_Cumming(Girl)
                            if action_context == "shift" or "angry" in Girl.recent_history:
                                jump Laura_HJ_After

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in Girl.recent_history:#And Laura is unsatisfied,
                                "[Girl.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Laura_HJ_After
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if counter == 20:
                    $ Girl.Brows = "angry"
                    menu:
                        ch_l "Hmm, this is boring, can we take a break?"
                        "How about a BJ?" if Girl.Action and multi_action:
                                $ action_context = "shift"
                                call Laura_HJ_After
                                call Laura_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                jump Laura_HJ_Cycle
                        "Let's try something else." if multi_action:
                                $ line = 0
                                call Laura_HJ_Reset
                                $ action_context = "shift"
                                jump Laura_HJ_After
                        "No, get back down there.":
                                if ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "O"):
                                    $ Girl.change_stat("love", 200, -5)
                                    $ Girl.change_stat("obedience", 50, 3)
                                    $ Girl.change_stat("obedience", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    $ Girl.change_face("angry", 1)
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_l "I have better things to do with my time."
                                    $ Girl.change_stat("love", 50, -3, 1)
                                    $ Girl.change_stat("love", 80, -4, 1)
                                    $ Girl.change_stat("obedience", 30, -1, 1)
                                    $ Girl.change_stat("obedience", 50, -1, 1)
                                    $ Girl.recent_history.append("angry")
                                    $ Girl.daily_history.append("angry")
                                    jump Laura_HJ_After
        elif counter == 10 and Girl.SEXP <= 100 and not ApprovalCheck(Girl, 1200, "LO"):
                    $ Girl.Brows = "confused"
                    ch_l "This working for you?"
        #End Count check

        call Escalation(Girl) #sees if she wants to escalate things

        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [Girl.Petname]."

    #Round = 0 loop breaks
    $ Girl.change_face("bemused", 0)
    $ line = 0
    ch_l "Ok, [Girl.Petname], breaktime."

label Laura_HJ_After:
    $ Girl.change_face("sexy")

    $ Girl.Hand += 1
    $ Girl.Action -=1
    $ Girl.Addictionrate += 1
    if Player.addictive:
        $ Girl.Addictionrate += 1
    $ Girl.change_stat("lust", 90, 5)

    call Partner_Like(Girl,1)

    if "Laura Handi-Queen" in Achievements:
            pass
    elif Girl.Hand >= 10:
            $ Girl.change_face("smile", 1)
            ch_l "Looks like you filled out the punch card, [Girl.Petname]."
            $ Achievements.append("Laura Handi-Queen")
            $Girl.SEXP += 5
    elif Girl.Hand == 1:
            $Girl.SEXP += 10
            if Girl.love >= 500:
                $ Girl.Mouth = "smile"
                ch_l "That was kind of. . . pleasant. . ."
            elif Player.Focus <= 20:
                $ Girl.Mouth = "sad"
                ch_l "Did that do it for you?"
    elif Girl.Hand == 5:
                ch_l "I think I've got this down, maybe I should get a punch card."

    $ temp_modifier = 0
    if action_context == "shift":
        ch_l "Ok, so what did you have in mind?"
    else:
        call Laura_HJ_Reset
    call Checkout
    return

## end Girl.Handjob //////////////////////////////////////////////////////////////////////


## Girl.Titjob //////////////////////////////////////////////////////////////////////              Not finished
label Laura_Titjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus(Girl)
    if Girl.Tit >= 7: # She loves it
        $ temp_modifier += 10
    elif Girl.Tit >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif Girl.Tit: #You've done it before
        $ temp_modifier += 5

    if Girl.Addict >= 75 and Girl.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 15
    elif Girl.Addict >= 75:
        $ temp_modifier += 5

    if Girl.SeenChest and ApprovalCheck(Girl, 500): # You've seen her tits.
        $ temp_modifier += 10
    if not Girl.Chest and not Girl.Over: #She's already topless
        $ temp_modifier += 10
    if Girl.lust > 75: #She's really horny
        $ temp_modifier += 10
    if action_context == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in Girl.Traits:
        $ temp_modifier += (5*Taboo)
    if Girl in Player.Harem or "sex friend" in Girl.Petnames:
        $ temp_modifier += 10
    elif "ex" in Girl.Traits:
        $ temp_modifier -= 30
    if Girl.ForcedCount and not Girl.Forced:
        $ temp_modifier -= 5 * Girl.ForcedCount

    if Taboo and "tabno" in Girl.daily_history:
        $ temp_modifier -= 10

    if "no_titjob" in Girl.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no_titjob" in Girl.recent_history else 0

    $ Approval = ApprovalCheck(Girl, 1200, TabM = 4) # 120, 135, 150, Taboo -200(320)

    if not Girl.Tit and "no_titjob" not in Girl.recent_history:
        $ Girl.change_face("surprised", 1)
        $ Girl.Mouth = "kiss"
        ch_l "You want a titjob, huh?"

    if not Girl.Tit and Approval:                                                 #First time dialog
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
        elif Girl.love >= (Girl.obedience + Girl.inhibition):
            $ Girl.change_face("sexy")
            $ Girl.Brows = "sad"
            $ Girl.Mouth = "smile"
            ch_l "Well, maybe you deserve it."
        elif Girl.obedience >= Girl.inhibition:
            $ Girl.change_face("normal")
            ch_l "If you'd like that. . ."
        elif Girl.Addict >= 50:
            $ Girl.change_face("manic", 1)
            ch_l "Hmmmm. . . ."
        else: # Uninhibited
            $ Girl.change_face("sad")
            $ Girl.Mouth = "smile"
            ch_l "Sounds fun. . ."
    elif Approval:                                                                       #Second time+ dialog
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
            ch_l "You're kinda pushing it."
        elif not Taboo and "tabno" in Girl.daily_history:
            ch_l "Ok, I guess this is secluded enough. . ."
        elif "titjob" in Girl.recent_history:
            $ Girl.change_face("sexy", 1)
            ch_l "Huh, again?"
            jump Laura_TJ_Prep
        elif "titjob" in Girl.daily_history:
            $ Girl.change_face("sexy", 1)
            $ line = renpy.random.choice(["Back for more?",
                "You're really working these puppies.",
                "Didn't get enough earlier?",
                "You're really working these puppies."])
            ch_l "[line]"
        elif Girl.Tit < 3:
            $ Girl.change_face("sexy", 1)
            $ Girl.Brows = "confused"
            $ Girl.Mouth = "kiss"
            ch_l "Another titjob??"
        else:
            $ Girl.change_face("sexy", 1)
            $ Girl.ArmPose = 2
            $ line = renpy.random.choice(["You want some of this action [rubs her chest]?",
                "So you'd like another titjob?",
                "So you'd like another titjob?",
                "So you'd like another titjob?",
                "Another titjob?",
                "A little [points at her chest]?"])
            ch_l "[line]"
        $ line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 60, 1)
            ch_l "Well, could be worse. . ."
        elif "no_titjob" in Girl.daily_history:
            ch_l "Hmm, I guess. . ."
        else:
            $ Girl.change_face("sexy", 1)
            $ Girl.change_stat("love", 90, 1)
            $ Girl.change_stat("inhibition", 50, 3)
            $ line = renpy.random.choice(["Well, sure, put it here.",
                "Well. . . ok.",
                "Yum.",
                "Sure, whip it out.",
                "Fine. . . [She drools a bit into her cleavage].",
                "Heh, ok."])
            ch_l "[line]"
            $ line = 0
        $ Girl.change_stat("obedience", 20, 1)
        $ Girl.change_stat("obedience", 70, 1)
        $ Girl.change_stat("inhibition", 80, 2)
        jump Laura_TJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ Girl.change_face("angry")
        if "no_titjob" in Girl.recent_history:
            ch_l "I {i}just{/i} told you \"no,\" [Girl.Petname]."
        elif Taboo and "tabno" in Girl.daily_history and "no_titjob" in Girl.daily_history:
            ch_l "This is just way too exposed!"
        elif "no_titjob" in Girl.daily_history:
            ch_l "I already told you \"no,\" [Girl.Petname]."
        elif Taboo and "tabno" in Girl.daily_history:
            ch_l "This is just way too exposed!"
        elif not Girl.Tit:
            $ Girl.change_face("bemused")
            ch_l "I'm not really into that, [Girl.Petname]. . ."
        else:
            $ Girl.change_face("bemused")
            ch_l "Not right now [Girl.Petname]. . ."

        menu:
            extend ""
            "Sorry, never mind." if "no_titjob" in Girl.daily_history:
                $ Girl.change_face("bemused")
                ch_l "Yeah, ok, [Girl.Petname]."
                return
            "Maybe later?" if "no_titjob" not in Girl.daily_history:
                $ Girl.change_face("sexy")
                ch_l "Maybe."
                $ Girl.change_stat("love", 80, 2)
                $ Girl.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ Girl.recent_history.append("tabno")
                    $ Girl.daily_history.append("tabno")
                $ Girl.recent_history.append("no_titjob")
                $ Girl.daily_history.append("no_titjob")
                return
            "I think this could be fun for both of us. . .":
                if Approval:
                    $ Girl.change_face("sexy")
                    $ Girl.change_stat("obedience", 80, 2)
                    $ Girl.change_stat("obedience", 40, 2)
                    $ Girl.change_stat("inhibition", 70, 3)
                    $ Girl.change_stat("inhibition", 40, 2)
                    $ line = renpy.random.choice(["Well, ok, put it here.",
                        "Well. . . ok.",
                        "I guess.",
                        "I guess, whip it out.",
                        "Fine. . . [She drools a bit into her cleavage].",
                        "Heh, ok."])
                    ch_l "[line]"
                    $ line = 0
                    jump Laura_TJ_Prep
                else:
                    $ Approval = ApprovalCheck(Girl, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)             Handy instead?
                    if Approval >= 2 and Girl.Blow:
                        $ Girl.change_stat("inhibition", 80, 1)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.change_face("confused", 1)
                        ch_l "I could maybe blow you?"
                        menu:
                            ch_l "How about that [[blowjob]?"
                            "Ok, get down there.":
                                $ Girl.change_stat("love", 80, 2)
                                $ Girl.change_stat("inhibition", 60, 1)
                                $ Girl.change_stat("obedience", 50, 1)
                                jump Laura_BJ_Prep
                            "Nah, it's all about dem titties.":
                                $ line = "no_BJ"
                    if Approval and Girl.Hand:
                        $ Girl.change_stat("inhibition", 80, 1)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.change_face("confused", 1)
                        ch_l "I could give you a handy?"
                        menu:
                            ch_l "What do you say?"
                            "Sure, that's fine.":
                                $ Girl.change_stat("love", 80, 2)
                                $ Girl.change_stat("inhibition", 60, 1)
                                $ Girl.change_stat("obedience", 50, 1)
                                jump Laura_HJ_Prep
                            "Seriously, titties." if line == "no_BJ":
                                $ line = 0
                            "Nah, it's all about dem titties." if line != "no_BJ":
                                pass
                    $ Girl.change_stat("love", 200, -2)
                    ch_l "Nah."
                    $ Girl.change_stat("obedience", 70, 2)


            "Come on, let me fuck those titties, [Girl.Pet]":                                               # Pressured into it
                $ Girl.NameCheck() #checks reaction to petname
                $ Approval = ApprovalCheck(Girl, 700, "OI", TabM = 4) # 70, 85, 100, -160(230)
                if Approval > 1 or (Approval and Girl.Forced):
                    $ Girl.change_face("sad")
                    $ Girl.change_stat("love", 70, -5, 1)
                    $ Girl.change_stat("love", 200, -2)

                    $ Girl.change_stat("obedience", 50, 4)
                    $ Girl.change_stat("inhibition", 80, 1)
                    $ Girl.change_stat("inhibition", 60, 3)
                    $ Girl.Forced = 1
                    jump Laura_TJ_Prep
                else:
                    $ Girl.change_stat("love", 200, -15)
                    $ Girl.recent_history.append("angry")
                    $ Girl.daily_history.append("angry")

    #She refused all offers.
    if "no_titjob" in Girl.daily_history:
        $ Girl.change_face("angry", 1)

        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
    elif Girl.Forced:
        $ Girl.change_face("angry", 1)
        ch_l "No, try something else."
        $ Girl.change_stat("lust", 200, 5)
        if Girl.love > 300:
                $ Girl.change_stat("love", 70, -2)
        $ Girl.change_stat("obedience", 50, -2)
        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ Girl.change_face("angry", 1)
        $ Girl.daily_history.append("tabno")
        ch_l "You really expect me to do that here? This isn't exactly \"covert.\""
        $ Girl.change_stat("lust", 200, 5)
        $ Girl.change_stat("obedience", 50, -3)
    elif Girl.Tit:
        $ Girl.change_face("sad")
        ch_l "You'll know when it's time for that."
    else:
        $ Girl.change_face("normal", 1)
        ch_l "Nah."
    $ Girl.recent_history.append("no_titjob")
    $ Girl.daily_history.append("no_titjob")
    $ temp_modifier = 0
    return

label Laura_TJ_Prep:

    if Taboo:
        $ Girl.inhibition += int(Taboo/10)
        $ Girl.lust += int(Taboo/5)


    $ Girl.change_face("sexy")
    if Girl.Forced:
        $ Girl.change_face("sad")
    elif not Girl.Tit:
        $ Girl.Brows = "confused"
        $ Girl.Eyes = "sexy"
        $ Girl.Mouth = "smile"

    call Seen_First_Peen(Girl,Partner,React=action_context)
    call Laura_TJ_Launch("L")

    if action_context == Girl:
            #Laura auto-starts
            $ action_context = 0
            "[Girl.Name] slides down and sandwiches your dick between her tits."
            menu:
                "What do you do?"
                "Nothing.":
                    $ Girl.change_stat("inhibition", 80, 3)
                    $ Girl.change_stat("inhibition", 40, 2)
                    "[Girl.Name] starts to slide them up and down."
                "Praise her.":
                    $ Girl.change_face("sexy", 1)
                    $ Girl.change_stat("inhibition", 80, 3)
                    ch_p "Oh, that sounds like a good idea, [Girl.Pet]."
                    $ Girl.NameCheck() #checks reaction to petname
                    "[Girl.Name] continues her actions."
                    $ Girl.change_stat("love", 85, 1)
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ Girl.change_face("confused")
                    $ Girl.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that for now, [Girl.Pet]."
                    $ Girl.NameCheck() #checks reaction to petname
                    "[Girl.Name] lets it drop out from between her breasts."
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Player.recent_history.append("nope")
                    $ Girl.AddWord(1,"refused","refused")
                    return

    if not Girl.Tit:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -25)
            $ Girl.change_stat("obedience", 70, 30)
            $ Girl.change_stat("inhibition", 80, 35)
        else:
            $ Girl.change_stat("love", 90, 5)
            $ Girl.change_stat("obedience", 70, 25)
            $ Girl.change_stat("inhibition", 80, 30)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ line = 0
    $ counter = 0
    if Taboo:
        $ Girl.DrainWord("tabno")
    $ Girl.DrainWord("no_titjob")
    $ Girl.recent_history.append("titjob")
    $ Girl.daily_history.append("titjob")

label Laura_TJ_Cycle: #Repeating strokes
    while Round > 0:
        call shift_focus(Girl)
        call Laura_TJ_Launch
        $ Girl.lustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if action_speed:
                                    pass

                        "Start moving? . ." if action_speed == 0:
                                    call action_speed_Shift(1)

                        "action_speed up. . ." if  action_speed == 1:
                                    call action_speed_Shift(2)
                                    "You ask her to up the pace a bit."
                        "action_speed up. . . (locked)" if action_speed >= 2:
                                    pass

                        "Stop moving" if action_speed != 0:
                                    call action_speed_Shift(0)
                        "Slow Down. . ." if action_speed == 2:
                                    call action_speed_Shift(1)
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not action_speed:
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
                                    "I also want to fondle her breasts." if offhand_action != "fondle_breasts":
                                            if Girl.Action and multi_action:
                                                $ offhand_action = "fondle_breasts"
                                                "You start to fondle her breasts."
                                                $ Girl.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Shift primary action":
                                            if Girl.Action and multi_action:
                                                    menu:
                                                        "How about a blowjob?":
                                                                if Girl.Action and multi_action:
                                                                    $ action_context = "shift"
                                                                    call Laura_TJ_After
                                                                    call Laura_Blowjob
                                                                else:
                                                                    call Sex_Basic_Dialog(Girl,"tired")

                                                        "How about a handy?":
                                                                if Girl.Action and multi_action:
                                                                    $ action_context = "shift"
                                                                    call Laura_BJ_After
                                                                    call Laura_Handjob
                                                                else:
                                                                    call Sex_Basic_Dialog(Girl,"tired")
                                                        "Never Mind":
                                                                jump Laura_TJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [Girl.Name] to do something else with [Partner.Name]" if primary_action == "lesbian":
                                                        call Les_Change(Girl)
                                            "Ask [Girl.Name] to do something else with [Partner.Name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(Girl)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.Name]":
                                                        call primary_action_Swap(Girl)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Laura_TJ_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Laura_TJ_Cycle
                                            "Never mind":
                                                        jump Laura_TJ_Cycle
                                    "undress [Girl.Name]":
                                            call Girl_Undress(Girl)
                                    "Clean up [Girl.Name] (locked)" if not Girl.Spunk:
                                            pass
                                    "Clean up [Girl.Name]" if Girl.Spunk:
                                            call Girl_Cleanup(Girl,"ask")
                                    "Never mind":
                                            jump Laura_TJ_Cycle

                        "Back to Sex Menu" if multi_action:
                                    ch_p "Let's try something else."
                                    call Laura_TJ_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Laura_TJ_After
                        "End Scene" if not multi_action:
                                    ch_p "Let's stop for now."
                                    call Laura_TJ_Reset
                                    $ line = 0
                                    jump Laura_TJ_After
        #End menu (if line)

        call shift_focus(Girl)
        call Sex_Dialog(Girl,Partner)

        #If either of you could cum

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or Girl.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(Girl)
                            if "angry" in Girl.recent_history:
                                call Laura_TJ_Reset
                                return
                            $ Girl.change_stat("lust", 200, 5)
                            if 100 > Girl.lust >= 70 and Girl.OCount < 2 and Girl.SEXP >= 20:
                                $ Girl.recent_history.append("unsatisfied")
                                $ Girl.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Laura_TJ_After
                            $ line = "came"

                    if Girl.lust >= 100:
                            #If Laura can cum
                            call Girl_Cumming(Girl)
                            if action_context == "shift" or "angry" in Girl.recent_history:
                                jump Laura_TJ_After

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in Girl.recent_history:#And Laura is unsatisfied,
                                "[Girl.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Laura_TJ_After
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        if action_speed >= 4:
                call action_speed_Shift(0) #resets speed after orgasm
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Girl.SEXP >= 100 or ApprovalCheck(Girl, 1200, "LO"):
                pass
        elif counter == (5 + Girl.Tit):
                $ Girl.Brows = "confused"
                ch_l "Are you getting close here? I'm getting bored."
        if counter == (10 + Girl.Tit):
                $ Girl.Brows = "angry"
                menu:
                    ch_l "Seriously, can we do something else?"
                    "How about a BJ?" if Girl.Action and multi_action:
                        $ action_context = "shift"
                        call Laura_TJ_After
                        call Laura_Blowjob
                        return
                    "Finish up." if Player.FocusX:
                        "You release your concentration. . ."
                        $ Player.FocusX = 0
                        $ Player.Focus += 15
                        jump Laura_TJ_Cycle
                    "Let's try something else." if multi_action:
                        $ line = 0
                        call Laura_TJ_Reset
                        $ action_context = "shift"
                        jump Laura_TJ_After
                    "No, get back down there.":
                        if ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "O"):
                            $ Girl.change_stat("love", 200, -5)
                            $ Girl.change_stat("obedience", 50, 3)
                            $ Girl.change_stat("obedience", 80, 2)
                            "She grumbles but gets back to work."
                        else:
                            $ Girl.change_face("angry", 1)
                            "She scowls at you, drops you cock and pulls back."
                            ch_l "Well fuck you then."
                            $ Girl.change_stat("love", 50, -3, 1)
                            $ Girl.change_stat("love", 80, -4, 1)
                            $ Girl.change_stat("obedience", 30, -1, 1)
                            $ Girl.change_stat("obedience", 50, -1, 1)
                            $ Girl.recent_history.append("angry")
                            $ Girl.daily_history.append("angry")
                            jump Laura_TJ_After
            #End Count check

        call Escalation(Girl) #sees if she wants to escalate things

        if Round == 10:
            ch_l "It's kinda time to get moving."
        elif Round == 5:
            ch_l "Tic tock, [Girl.Petname]."

    #Round = 0 loop breaks
    $ Girl.change_face("bemused", 0)
    $ line = 0
    ch_l "Ok, [Girl.Petname], breaktime."

label Laura_TJ_After:
    $ Girl.change_face("sexy")

    $ Girl.Tit += 1
    $ Girl.Action -=1
    $ Girl.Addictionrate += 1
    if Player.addictive:
        $ Girl.Addictionrate += 1

    call Partner_Like(Girl,4)

    if Girl.Tit > 5:
        pass
    elif Girl.Tit == 1:
        $ Girl.SEXP += 12
        if Girl.love >= 500:
            $ Girl.Mouth = "smile"
            ch_l "That was fun."
        elif Player.Focus <= 20:
            $ Girl.Mouth = "sad"
            ch_l "Well I hope you got something out of that."
    elif Girl.Tit == 5:
            ch_l "You seem to enjoy that."

    $ temp_modifier = 0

    if action_context == "shift":
            ch_l "Mmm, so what else did you have in mind?"
    else:
            call Laura_TJ_Reset
    call Checkout
    return

## end Girl.Titjob //////////////////////////////////////////////////////////////////////



# Girl.Blowjob //////////////////////////////////////////////////////////////////////

label Laura_Blowjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus(Girl)
    if Girl.Blow >= 7: # She loves it
        $ temp_modifier += 15
    elif Girl.Blow >= 3: #You've done it before several times
        $ temp_modifier += 10
    elif Girl.Blow: #You've done it before
        $ temp_modifier += 7

    if Girl.Addict >= 75 and Girl.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 25
    elif Girl.Addict >= 75: #She's really strung out
        $ temp_modifier += 15

    if action_context == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in Girl.Traits:
        $ temp_modifier += (4*Taboo)
    if Girl in Player.Harem or "sex friend" in Girl.Petnames:
        $ temp_modifier += 10
    elif "ex" in Girl.Traits:
        $ temp_modifier -= 40
    if Girl.ForcedCount and not Girl.Forced:
        $ temp_modifier -= 5 * Girl.ForcedCount

    if Taboo and "tabno" in Girl.daily_history:
        $ temp_modifier -= 10

    if "no_blow" in Girl.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no_blow" in Girl.recent_history else 0

    $ Approval = ApprovalCheck(Girl, 1300, TabM = 4) # 130, 145, 160, Taboo -160(290)

    if not Girl.Blow and "no_blow" not in Girl.recent_history:
        $ Girl.change_face("surprised", 2)
        $ Girl.Mouth = "kiss"
        ch_l "You want me to suck your cock?"
        if Girl.Hand:
            $ Girl.Mouth = "smile"
            ch_l "Handjobs not enough now?"
        $ Girl.Blush = 1

    if not Girl.Blow and Approval:                                                 #First time dialog
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
        elif Girl.love >= (Girl.obedience + Girl.inhibition):
            $ Girl.change_face("sexy")
            $ Girl.Brows = "sad"
            $ Girl.Mouth = "smile"
            ch_l "I have wondered how you taste."
        elif Girl.obedience >= Girl.inhibition:
            $ Girl.change_face("normal")
            ch_l "If that's what you want. . ."
        elif Girl.Addict >= 50:
            $ Girl.change_face("manic", 1)
            ch_l "[[wipes away a little drool]"
        else: # Uninhibited
            $ Girl.change_face("sad")
            $ Girl.Mouth = "smile"
            ch_l "Huh. . ."
    elif Approval:                                                                       #Second time+ dialog
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
            ch_l "Again?"
        elif not Taboo and "tabno" in Girl.daily_history:
            ch_l "Hmm, this is private enough. . ."
        elif "blowjob" in Girl.recent_history:
            $ Girl.change_face("sexy", 1)
            ch_l "Mmm, again? [[yawns]"
            jump Laura_BJ_Prep
        elif "blowjob" in Girl.daily_history:
            $ Girl.change_face("sexy", 1)
            $ line = renpy.random.choice(["Back again so soon?",
                "Wear'in me out here.",
                "I must be too good at this.",
                "Let me get some saliva going.",
                "Didn't get enough earlier?"])
            ch_l "[line]"
        elif Girl.Blow < 3:
            $ Girl.change_face("sexy", 1)
            $ Girl.Brows = "confused"
            $ Girl.Mouth = "kiss"
            ch_l "You'd like another blowjob?"
        else:
            $ Girl.change_face("sexy", 1)
            $ Girl.ArmPose = 2
            $ line = renpy.random.choice(["You want me to [mimes blowing]?",
                "So you want another blowjob?",
                "You want me to lick you?",
                "You want me to suck you off?",
                "A little bj?"])
            ch_l "[line]"
        $ line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 60, 1)
            ch_l "Whatever."
        elif "no_blow" in Girl.daily_history:
            ch_l "Fine. . ."
        else:
            $ Girl.change_face("sexy", 1)
            $ Girl.change_stat("love", 90, 1)
            $ Girl.change_stat("inhibition", 50, 3)
            $ line = renpy.random.choice(["Sure. Ahhhhhh.",
                "Well. . . alright.",
                "Yum.",
                "Sure, whip it out.",
                "Ok. . . [She licks her lips].",
                "Alright, let's see it."])
            ch_l "[line]"
            $ line = 0
        $ Girl.change_stat("obedience", 20, 1)
        $ Girl.change_stat("obedience", 70, 1)
        $ Girl.change_stat("inhibition", 80, 2)
        jump Laura_BJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ Girl.change_face("angry")
        if "no_blow" in Girl.recent_history:
            ch_l "Just told you I wouldn't, [Girl.Petname]."
        elif Taboo and "tabno" in Girl.daily_history and "no_blow" in Girl.daily_history:
            ch_l "Like I told you, not in public."
        elif "no_blow" in Girl.daily_history:
            ch_l "Told you \"no,\" [Girl.Petname]."
        elif Taboo and "tabno" in Girl.daily_history:
            ch_l "Like I told you, too public!"
        elif not Girl.Blow:
            $ Girl.change_face("bemused")
            ch_l "I don't know if your taste will match your scent, [Girl.Petname]. . ."
        else:
            $ Girl.change_face("bemused")
            ch_l "I don't know, [Girl.Petname]!"
        menu:
            extend ""
            "Sorry, never mind." if "no_blow" in Girl.daily_history:
                $ Girl.change_face("bemused")
                ch_l "Cool."
                return
            "Maybe later?" if "no_blow" not in Girl.daily_history:
                $ Girl.change_face("sexy")
                ch_l "Yeah, maybe, [Girl.Petname]."
                $ Girl.change_stat("love", 80, 2)
                $ Girl.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ Girl.recent_history.append("tabno")
                    $ Girl.daily_history.append("tabno")
                $ Girl.recent_history.append("no_blow")
                $ Girl.daily_history.append("no_blow")
                return
            "Come on, please?":
                if Approval:
                    $ Girl.change_face("sexy")
                    $ Girl.change_stat("obedience", 90, 2)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("inhibition", 70, 3)
                    $ Girl.change_stat("inhibition", 40, 2)
                    $ line = renpy.random.choice(["Sure. Ahhhhhh.",
                        "Well. . . alright.",
                        "Yum.",
                        "Sure, whip it out.",
                        "Ok. . . [She licks her lips].",
                        "Alright, let's see it."])
                    ch_l "[line]"
                    $ line = 0
                    jump Laura_BJ_Prep
                else:
                    if ApprovalCheck(Girl, 1100, TabM = 3): # 110, 125, 140, Taboo -120(230)             Handy instead?
                        $ Girl.change_stat("inhibition", 80, 1)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.change_face("confused", 1)
                        $ Girl.ArmPose = 2
                        if Girl.Hand:
                            ch_l "Couldn't I just use my hand again?"
                            ch_l "You seemed to like that."
                        else:
                            ch_l "I could maybe use my hand instead, how's that sound?"
                        menu:
                            extend ""
                            "Sure, that's fine.":
                                $ Girl.change_stat("love", 80, 2)
                                $ Girl.change_stat("inhibition", 60, 1)
                                $ Girl.change_stat("obedience", 50, 1)
                                jump Laura_HJ_Prep
                            "Nah, if it's not a BJ, forget it.":
                                $ Girl.change_stat("love", 200, -2)
                                $ Girl.ArmPose = 1
                                ch_l "Fine, be that way."
                                $ Girl.change_stat("obedience", 70, 2)


            "Suck it, [Girl.Pet]":                                               # Pressured into it
                $ Girl.NameCheck() #checks reaction to petname
                $ Approval = ApprovalCheck(Girl, 750, "OI", TabM = 3) # 75, 90, 105, -120(195)
                if Approval > 1 or (Approval and Girl.Forced):
                    $ Girl.change_face("sad")
                    $ Girl.change_stat("love", 70, -5, 1)
                    $ Girl.change_stat("love", 200, -2)
                    ch_l
                    $ Girl.change_stat("obedience", 50, 4)
                    $ Girl.change_stat("inhibition", 80, 1)
                    $ Girl.change_stat("inhibition", 60, 3)
                    $ Girl.Forced = 1
                    jump Laura_BJ_Prep
                else:
                    $ Girl.change_stat("love", 200, -15)
                    $ Girl.recent_history.append("angry")
                    $ Girl.daily_history.append("angry")

    #She refused all offers.
    if "no_blow" in Girl.daily_history:
        $ Girl.change_face("angry", 1)
        $ Girl.ArmPose = 2
        $ Girl.Claws = 1

        $ Girl.ArmPose = 1
        $ Girl.Claws = 0
        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
    elif Girl.Forced:
        $ Girl.change_face("angry", 1)
        ch_l "That's just pushing it."
        $ Girl.change_stat("lust", 200, 5)
        if Girl.love > 300:
                $ Girl.change_stat("love", 70, -2)
        $ Girl.change_stat("obedience", 50, -2)
        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
        $ Girl.recent_history.append("no_blow")
        $ Girl.daily_history.append("no_blow")
        return
    elif Taboo:                             # she refuses and this is too public a place for her
        $ Girl.change_face("angry", 1)
        $ Girl.daily_history.append("tabno")
        ch_l "This area's too exposed."
        $ Girl.change_stat("lust", 200, 5)
        $ Girl.change_stat("obedience", 50, -3)
        return
    elif Girl.Blow:
        $ Girl.change_face("sad")
        ch_l "Nah, not this time."
    else:
        $ Girl.change_face("normal", 1)
        ch_l "Nope."
    $ Girl.recent_history.append("no_blow")
    $ Girl.daily_history.append("no_blow")
    $ temp_modifier = 0
    return


label Laura_BJ_Prep:
    if renpy.showing("Laura_HJ_Animation"):
        hide Laura_HJ_Animation with easeoutbottom
    if Taboo:
        $ Girl.inhibition += int(Taboo/10)
        $ Girl.lust += int(Taboo/5)

    $ Girl.change_face("sexy")
    if Girl.Forced:
        $ Girl.change_face("sad")
    elif not Girl.Blow:
        $ Girl.Brows = "confused"
        $ Girl.Eyes = "sexy"
        $ Girl.Mouth = "smile"

    call Seen_First_Peen(Girl,Partner,React=action_context)
    call Laura_BJ_Launch("L")
    if action_context == Girl:
            #Laura auto-starts
            $ action_context = 0
            "[Girl.Name] slides down and gives your cock a little lick."
            menu:
                "What do you do?"
                "Nothing.":
                    $ Girl.change_stat("inhibition", 80, 3)
                    $ Girl.change_stat("inhibition", 40, 2)
                    "[Girl.Name] continues licking at it."
                "Praise her.":
                    $ Girl.change_face("sexy", 1)
                    $ Girl.change_stat("inhibition", 80, 3)
                    ch_p "Hmmm, keep doing that, [Girl.Pet]."
                    $ Girl.NameCheck() #checks reaction to petname
                    "[Girl.Name] continues her actions."
                    $ Girl.change_stat("love", 85, 1)
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ Girl.change_face("surprised")
                    $ Girl.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that for now, [Girl.Pet]."
                    $ Girl.NameCheck() #checks reaction to petname
                    "[Girl.Name] puts it down."
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Player.recent_history.append("nope")
                    $ Girl.AddWord(1,"refused","refused")
                    return
    if not Girl.Blow:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -70)
            $ Girl.change_stat("obedience", 70, 45)
            $ Girl.change_stat("inhibition", 80, 60)
        else:
            $ Girl.change_stat("love", 90, 5)
            $ Girl.change_stat("obedience", 70, 35)
            $ Girl.change_stat("inhibition", 80, 40)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ line = 0
    $ counter = 0
    if Taboo:
        $ Girl.DrainWord("tabno")
    $ Girl.DrainWord("no_blow")
    $ Girl.recent_history.append("blowjob")
    $ Girl.daily_history.append("blowjob")

label Laura_BJ_Cycle: #Repeating strokes
    while Round > 0:
        call shift_focus(Girl)
        call Laura_BJ_Launch
        $ Girl.lustFace()

        if Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if action_speed:
                                    pass

                        "Lick it. . ." if action_speed != 1:
                                call action_speed_Shift(1)
                        "Lick it. . . (locked)" if action_speed == 1:
                                pass

                        "Just the head. . ." if action_speed != 2:
                                call action_speed_Shift(2)
                        "Just the head. . . (locked)" if action_speed == 2:
                                pass

                        "Suck on it." if action_speed != 3:
                                call action_speed_Shift(3)
                                if offhand_action == "jackin":
                                    "She dips her head a bit lower, and you move your hand out of the way."

                                if "Gwentro" not in Girl.History: #calls the special Gwentro event
                                            call Gwentro

                        "Suck on it. (locked)" if action_speed == 3:
                                pass

                        "Take it deeper." if action_speed != 4:
                                    if offhand_action == "jackin" and action_speed != 3:
                                        "She takes it to the root, and you move your hand out of the way."
                                    call action_speed_Shift(4)
                        "Take it deeper. (locked)" if action_speed == 4:
                                pass

                        "Set your own pace. . .":
                                "[Girl.Name] hums contentedly."
                                if "setpace" not in Girl.recent_history:
                                    $ Girl.change_stat("love", 80, 2)
                                $ D20 = renpy.random.randint(1, 20)
                                if Girl.Blow < 5:
                                    $ D20 -= 10
                                elif Girl.Blow < 10:
                                    $ D20 -= 5

                                if D20 > 15:
                                    call action_speed_Shift(4)
                                    if "setpace" not in Girl.recent_history:
                                        $ Girl.change_stat("inhibition", 80, 3)
                                elif D20 > 10:
                                    call action_speed_Shift(3)
                                elif D20 > 5:
                                    call action_speed_Shift(2)
                                else:
                                    call action_speed_Shift(1)
                                $ Girl.recent_history.append("setpace")

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
                                    "I also want to fondle her breasts." if offhand_action != "fondle_breasts":
                                            if Girl.Action and multi_action:
                                                $ offhand_action = "fondle_breasts"
                                                "You start to fondle her breasts."
                                                $ Girl.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Shift primary action":
                                            if Girl.Action and multi_action:
                                                    menu:
                                                        "How about a handy?":
                                                                if Girl.Action and multi_action:
                                                                    $ action_context = "shift"
                                                                    call Laura_BJ_After
                                                                    call Laura_Handjob
                                                                else:
                                                                    ch_l "I need a break, can we wrap on this?"
                                                        "How about a titjob?":
                                                                if Girl.Action and multi_action:
                                                                    $ action_context = "shift"
                                                                    call Laura_BJ_After
                                                                    call Laura_Titjob
                                                                else:
                                                                    ch_l "I need a break, can we wrap on this?"
                                                        "Never Mind":
                                                                jump Laura_BJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [Girl.Name] to do something else with [Partner.Name]" if primary_action == "lesbian":
                                                        call Les_Change(Girl)
                                            "Ask [Girl.Name] to do something else with [Partner.Name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(Girl)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.Name]":
                                                        call primary_action_Swap(Girl)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Laura_BJ_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Laura_BJ_Cycle
                                            "Never mind":
                                                        jump Laura_BJ_Cycle
                                    "undress [Girl.Name]":
                                            call Girl_Undress(Girl)
                                    "Clean up [Girl.Name] (locked)" if not Girl.Spunk:
                                            pass
                                    "Clean up [Girl.Name]" if Girl.Spunk:
                                            call Girl_Cleanup(Girl,"ask")
                                    "Never mind":
                                            jump Laura_BJ_Cycle

                        "Back to Sex Menu" if multi_action:
                                    ch_p "Let's try something else."
                                    call Laura_BJ_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Laura_BJ_After
                        "End Scene" if not multi_action:
                                    ch_p "Let's stop for now."
                                    call Laura_BJ_Reset
                                    $ line = 0
                                    jump Laura_BJ_After
        #End menu (if line)

        call shift_focus(Girl)
        call Sex_Dialog(Girl,Partner)

        #If either of you could cum

        $ counter += 1
        $ Round -= 1
        if action_speed:
            $ Player.Wet = 1 #wets penis
            $ Player.Spunk = 0 if Player.Spunk else Player.Spunk #cleans you off after one cycle

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or Girl.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(Girl)
                            if "angry" in Girl.recent_history:
                                call Laura_BJ_Reset
                                return
                            $ Girl.change_stat("lust", 200, 5)
                            if 100 > Girl.lust >= 70 and Girl.OCount < 2 and Girl.SEXP >= 20:
                                $ Girl.recent_history.append("unsatisfied")
                                $ Girl.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Laura_BJ_After
                            $ line = "came"

                    if Girl.lust >= 100:
                            #If Laura can cum
                            call Girl_Cumming(Girl)
                            if action_context == "shift" or "angry" in Girl.recent_history:
                                jump Laura_BJ_After

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."

                            if "unsatisfied" in Girl.recent_history:#And Laura is unsatisfied,
                                "[Girl.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Laura_BJ_After
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if Girl.SEXP >= 100 or ApprovalCheck(Girl, 1200, "LO"):
            pass
        elif counter == (10 + Girl.Blow):
                $ Girl.Brows = "angry"
                menu:
                    ch_l "I'm getting kinda bored. Can we do something else?"
                    "How about a Handy?" if Girl.Action and multi_action:
                            $ action_context = "shift"
                            call Laura_BJ_After
                            call Laura_Handjob
                            return
                    "Finish up." if Player.FocusX:
                            "You release your concentration. . ."
                            $ Player.FocusX = 0
                            $ Player.Focus += 15
                            jump Laura_BJ_Cycle
                    "Let's try something else." if multi_action:
                            $ line = 0
                            call Laura_BJ_Reset
                            $ action_context = "shift"
                            jump Laura_BJ_After
                    "No, get back down there.":
                            if ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "O"):
                                $ Girl.change_stat("love", 200, -5)
                                $ Girl.change_stat("obedience", 50, 3)
                                $ Girl.change_stat("obedience", 80, 2)
                                "She grumbles but gets back to work."
                            else:
                                $ Girl.change_face("angry", 1)
                                "She scowls at you, drops you cock and pulls back."
                                ch_l "Well fuck you then."
                                $ Girl.change_stat("love", 50, -3, 1)
                                $ Girl.change_stat("love", 80, -4, 1)
                                $ Girl.change_stat("obedience", 30, -1, 1)
                                $ Girl.change_stat("obedience", 50, -1, 1)
                                $ Girl.recent_history.append("angry")
                                $ Girl.daily_history.append("angry")
                                jump Laura_BJ_After
        elif counter == (5 + Girl.Blow) and Girl.SEXP <= 100 and not ApprovalCheck(Girl, 1200, "LO"):
                    $ Girl.Brows = "confused"
                    ch_l "Are you getting close here? I'm bored."
        #End Count check

        call Escalation(Girl) #sees if she wants to escalate things

        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [Girl.Petname]."

    #Round = 0 loop breaks
    $ Girl.change_face("bemused", 0)
    $ line = 0
    ch_l "Ok, I'm taking a quick break. . ."

label Laura_BJ_After:
    $ Girl.change_face("sexy")

    $ Girl.Blow += 1
    $ Girl.Action -=1
    $ Girl.Addictionrate += 1
    if Player.addictive:
        $ Girl.Addictionrate += 1

    call Partner_Like(Girl,2)

    if "Laura Jobber" in Achievements:
        pass
    elif Girl.Blow >= 10:
        $ Girl.change_face("smile", 1)
        ch_l "Your flavor is intoxicating."
        $ Achievements.append("Laura Jobber")
        $Girl.SEXP += 5
    elif action_context == "shift":
        pass
    elif Girl.Blow == 1:
            $Girl.SEXP += 15
            if Girl.love >= 500:
                $ Girl.Mouth = "smile"
                ch_l "Hey, whaddaya know, that wasn't bad."
            elif Player.Focus <= 20:
                $ Girl.Mouth = "sad"
                ch_l "I hope you enjoyed that."
    elif Girl.Blow == 5:
        ch_l "I'm really getting the hang of this. . . right?"
        menu:
            "[[nod]":
                $ Girl.change_face("smile", 1)
                $ Girl.change_stat("love", 90, 15)
                $ Girl.change_stat("obedience", 80, 5)
                $ Girl.change_stat("inhibition", 90, 10)
            "[[shake head \"no\"]":
                if ApprovalCheck(Girl, 500, "O"):
                    $ Girl.change_face("sad", 2)
                    $ Girl.change_stat("love", 200, -5)
                else:
                    $ Girl.change_face("angry", 2)
                    $ Girl.change_stat("love", 200, -25)
                $ Girl.change_stat("obedience", 80, 10)
                ch_l ". . ."
                $ Girl.change_face("sad", 1)

    $ temp_modifier = 0
    if action_context != "shift":
        call Laura_BJ_Reset
    call Checkout
    return



# end Girl.Blowjob                                 //////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy
label Laura_Dildo_Check:
    if "dildo" in Player.Inventory:
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in Girl.Inventory:
        "You ask [Girl.Name] to get out her favorite Dildo."
    else:
        "You don't have one of those on you."
        return 0
    return 1

label Laura_Dildo_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus(Girl)
    call Laura_Dildo_Check
    if not _return:
        return

    if Girl.DildoP: #You've done it before
        $ temp_modifier += 15
    if Girl.Legs == "pants:": # she's got pants on.
        $ temp_modifier -= 20

    if Girl.lust > 95:
        $ temp_modifier += 20
    elif Girl.lust > 85: #She's really horny
        $ temp_modifier += 15

    if action_context == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in Girl.Traits:
        $ temp_modifier += (5*Taboo)
    if Girl in Player.Harem or "sex friend" in Girl.Petnames:
        $ temp_modifier += 10
    elif "ex" in Girl.Traits:
        $ temp_modifier -= 40
    if Girl.ForcedCount and not Girl.Forced:
        $ temp_modifier -= 5 * Girl.ForcedCount

    if Taboo and "tabno" in Girl.daily_history:
        $ temp_modifier -= 10

    if "no_dildo" in Girl.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no_dildo" in Girl.recent_history else 0

    $ Approval = ApprovalCheck(Girl, 1250, TabM = 4) # 125, 140, 155, Taboo -160(335)

    if action_context == Girl:                                                                  #Laura auto-starts
                if Approval > 2:                                                      # fix, add laura auto stuff here
                    if Girl.wearing_skirt:
                        "[Girl.Name] grabs her dildo, hiking up her skirt as she does."
                        $ Girl.Upskirt = 1
                    elif Girl.PantsNum() >= 6:
                        "[Girl.Name] grabs her dildo, pulling down her pants as she does."
                        $ Girl.Legs = 0
                    else:
                        "[Girl.Name] grabs her dildo, rubbing is suggestively against her crotch."
                    $ Girl.SeenPanties = 1
                    call Laura_First_Bottomless(1)
                    "She slides the tip along her pussy and seems to want you to insert it."
                    menu:
                        "What do you do?"
                        "Nothing.":
                            $ Girl.change_stat("inhibition", 80, 3)
                            $ Girl.change_stat("inhibition", 50, 2)
                            "[Girl.Name] slides it in."
                        "Go for it.":
                            $ Girl.change_face("sexy", 1)
                            $ Girl.change_stat("inhibition", 80, 3)
                            ch_p "Oh yeah, [Girl.Pet], let's do this."
                            $ Girl.NameCheck() #checks reaction to petname
                            "You grab the dildo and slide it in."
                            $ Girl.change_stat("love", 85, 1)
                            $ Girl.change_stat("obedience", 90, 1)
                            $ Girl.change_stat("obedience", 50, 2)
                        "Ask her to stop.":
                            $ Girl.change_face("surprised")
                            $ Girl.change_stat("inhibition", 70, 1)
                            ch_p "Let's not do that right now, [Girl.Pet]."
                            $ Girl.NameCheck() #checks reaction to petname
                            "[Girl.Name] sets the dildo down."
                            $ Girl.OutfitChange()
                            $ Girl.change_stat("obedience", 90, 1)
                            $ Girl.change_stat("obedience", 50, 1)
                            $ Girl.change_stat("obedience", 30, 2)
                            return
                    jump Laura_DP_Prep
                else:
                    $ temp_modifier = 0                               # fix, add laura auto stuff here
                    $ offhand_action = 0
                return

    if action_context == "auto":
                "You rub the dildo across her body, and along her moist slit."
                $ Girl.change_face("surprised", 1)

                if (Girl.DildoP and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
                    "[Girl.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                    $ Girl.change_face("sexy")
                    $ Girl.change_stat("obedience", 70, 3)
                    $ Girl.change_stat("inhibition", 50, 3)
                    $ Girl.change_stat("inhibition", 70, 1)
                    ch_l "Ooo, [Girl.Petname], toys!"
                    jump Laura_DP_Prep
                else:                                                                                                            #she's questioning it
                    $ Girl.Brows = "angry"
                    menu:
                        ch_l "Hey, what are you planning to do with that?!"
                        "Sorry, sorry! Never mind.":
                            if Approval:
                                $ Girl.change_face("sexy", 1)
                                $ Girl.change_stat("obedience", 70, 3)
                                $ Girl.change_stat("inhibition", 50, 3)
                                $ Girl.change_stat("inhibition", 70, 1)
                                ch_l "Well, now that you mention it. . ."
                                jump Laura_DP_Prep
                            "You pull back before you really get it in."
                            $ Girl.change_face("bemused", 1)
                            if Girl.DildoP:
                                ch_l "Well ok, [Girl.Petname], maybe warn me next time?"
                            else:
                                ch_l "Well ok, [Girl.Petname], that's a little much. . . for now . . ."
                        "Just playing with my favorite toys.":
                            $ Girl.change_stat("love", 80, -10, 1)
                            $ Girl.change_stat("love", 200, -10)
                            "You press it inside some more."
                            $ Girl.change_stat("obedience", 70, 3)
                            $ Girl.change_stat("inhibition", 50, 3)
                            if not ApprovalCheck(Girl, 700, "O", TabM=1): #Checks if obedience is 700+
                                $ Girl.change_face("angry")
                                "[Girl.Name] shoves you away and slaps you in the face."
                                ch_l "Jerk!"
                                ch_l "Ask nice if you want to stick something in my pussy!"
                                $ Girl.change_stat("love", 50, -10, 1)
                                $ Girl.change_stat("obedience", 50, 3)
                                $ renpy.pop_call()
                                if action_context:
                                    $ renpy.pop_call()
                                if renpy.showing("Laura_SexSprite"):
                                    call Laura_Sex_Reset
                                $ Girl.recent_history.append("angry")
                                $ Girl.daily_history.append("angry")
                            else:
                                $ Girl.change_face("sad")
                                "[Girl.Name] doesn't seem to be into this, you're lucky she's so obedient."
                                jump Laura_DP_Prep
                return
    #end Auto

    if not Girl.DildoP:
            #first time
            $ Girl.change_face("surprised", 1)
            $ Girl.Mouth = "kiss"
            ch_l "Hmmm, so you'd like to try out some toys?"
            if Girl.Forced:
                $ Girl.change_face("sad")
                ch_l "I suppose there are worst things you could ask for."

    if not Girl.DildoP and Approval:
            #First time dialog
            if Girl.Forced:
                $ Girl.change_face("sad")
                $ Girl.change_stat("love", 70, -3, 1)
                $ Girl.change_stat("love", 20, -2, 1)
            elif Girl.love >= (Girl.obedience + Girl.inhibition):
                $ Girl.change_face("sexy")
                $ Girl.Brows = "sad"
                $ Girl.Mouth = "smile"
                ch_l "I've had a reasonable amount of experience with these, you know. . ."
            elif Girl.obedience >= Girl.inhibition:
                $ Girl.change_face("normal")
                ch_l "If that's what you want, [Girl.Petname]. . ."
            else: # Uninhibited
                $ Girl.change_face("sad")
                $ Girl.Mouth = "smile"
                ch_l "I guess it could be fun with a partner. . ."

    elif Approval:
            #Second time+ dialog
            if Girl.Forced:
                $ Girl.change_face("sad")
                $ Girl.change_stat("love", 70, -3, 1)
                $ Girl.change_stat("love", 20, -2, 1)
                ch_l "The toys again?"
            elif not Taboo and "tabno" in Girl.daily_history:
                ch_l "Well, at least you got us some privacy this time. . ."
            elif "dildo_pussy" in Girl.recent_history:
                $ Girl.change_face("sexy", 1)
                ch_l "Mmm, again? Ok, let's get to it."
                jump Laura_DP_Prep
            elif "dildo_pussy" in Girl.daily_history:
                $ Girl.change_face("sexy", 1)
                $ line = renpy.random.choice(["Breaking out the toys again?",
                    "Didn't get enough earlier?",
                    "You're going to wear me out."])
                ch_l "[line]"
            elif Girl.DildoP < 3:
                $ Girl.change_face("sexy", 1)
                $ Girl.Brows = "confused"
                $ Girl.Mouth = "kiss"
                ch_l "You want to stick it in my pussy again?"
            else:
                $ Girl.change_face("sexy", 1)
                $ Girl.ArmPose = 2
                $ line = renpy.random.choice(["You want some of this action?",
                    "So you'd like another go?",
                    "You want to stick it in my pussy again?",
                    "You want me ta lube up your toy?"])
                ch_l "[line]"
                $ line = 0

    if Approval >= 2:
            #She's into it. . .
            if Girl.Forced:
                $ Girl.change_face("sad")
                $ Girl.change_stat("obedience", 90, 1)
                $ Girl.change_stat("inhibition", 60, 1)
                ch_l "Ok, fine."
            else:
                $ Girl.change_face("sexy", 1)
                $ Girl.change_stat("love", 90, 1)
                $ Girl.change_stat("inhibition", 50, 3)
                $ line = renpy.random.choice(["Well, sure, stick it in.",
                    "Well. . . ok.",
                    "Sure!",
                    "I guess I could. . . stick it in.",
                    "Hells yeah.",
                    "Heh, ok, ok."])
                ch_l "[line]"
                $ line = 0
            $ Girl.change_stat("obedience", 20, 1)
            $ Girl.change_stat("obedience", 60, 1)
            $ Girl.change_stat("inhibition", 70, 2)
            jump Laura_DP_Prep

    else:
            #She's not into it, but maybe. . .
            $ Girl.change_face("angry")
            if "no_dildo" in Girl.recent_history:
                ch_l "What part of \"no,\" did you not get, [Girl.Petname]?"
            elif Taboo and "tabno" in Girl.daily_history and "no_dildo" in Girl.daily_history:
                ch_l "Stop swinging that thing around in public!"
            elif "no_dildo" in Girl.daily_history:
                ch_l "I already told you \"no,\" [Girl.Petname]."
            elif Taboo and "tabno" in Girl.daily_history:
                ch_l "Stop swinging that thing around in public!"
            elif not Girl.DildoP:
                $ Girl.change_face("bemused")
                ch_l "I'm just not into toys, [Girl.Petname]. . ."
            else:
                $ Girl.change_face("bemused")
                ch_l "I don't think we need any toys, [Girl.Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no_dildo" in Girl.daily_history:
                    $ Girl.change_face("bemused")
                    ch_l "Yeah, ok, [Girl.Petname]."
                    return
                "Maybe later?" if "no_dildo" not in Girl.daily_history:
                    $ Girl.change_face("sexy")
                    ch_l "Maybe I'll practice on my own time, [Girl.Petname]."
                    $ Girl.change_stat("love", 80, 2)
                    $ Girl.change_stat("inhibition", 70, 2)
                    if Taboo:
                        $ Girl.recent_history.append("tabno")
                        $ Girl.daily_history.append("tabno")
                    $ Girl.recent_history.append("no_dildo")
                    $ Girl.daily_history.append("no_dildo")
                    return
                "I think you'd like it. . .":
                    if Approval:
                        $ Girl.change_face("sexy")
                        $ Girl.change_stat("obedience", 90, 2)
                        $ Girl.change_stat("obedience", 50, 2)
                        $ Girl.change_stat("inhibition", 70, 3)
                        $ Girl.change_stat("inhibition", 40, 2)
                        $ line = renpy.random.choice(["Well, sure, stick it in.",
                            "I suppose. . .",
                            "You've got me there."])
                        ch_l "[line]"
                        $ line = 0
                        jump Laura_DP_Prep
                    else:
                        pass

                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck(Girl, 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                    if Approval > 1 or (Approval and Girl.Forced):
                        $ Girl.change_face("sad")
                        $ Girl.change_stat("love", 70, -5, 1)
                        $ Girl.change_stat("love", 200, -5)
                        ch_l
                        $ Girl.change_stat("obedience", 80, 4)
                        $ Girl.change_stat("inhibition", 80, 1)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.Forced = 1
                        jump Laura_DP_Prep
                    else:
                        $ Girl.change_stat("love", 200, -20)
                        $ Girl.recent_history.append("angry")
                        $ Girl.daily_history.append("angry")

    #She refused all offers.
    $ Girl.ArmPose = 1
    if "no_dildo" in Girl.daily_history:

            $ Girl.recent_history.append("angry")
            $ Girl.daily_history.append("angry")
    elif Girl.Forced:
            $ Girl.change_face("angry", 1)
            ch_l "I'm not going to let you use that on me."
            $ Girl.change_stat("lust", 200, 5)
            if Girl.love > 300:
                    $ Girl.change_stat("love", 70, -2)
            $ Girl.change_stat("obedience", 50, -2)
            $ Girl.recent_history.append("angry")
            $ Girl.daily_history.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
            $ Girl.change_face("angry", 1)
            $ Girl.recent_history.append("tabno")
            $ Girl.daily_history.append("tabno")
            ch_l "Not here!"
            $ Girl.change_stat("lust", 200, 5)
            $ Girl.change_stat("obedience", 50, -3)
    elif Girl.DildoP:
            $ Girl.change_face("sad")
            ch_l "Sorry, you can keep your toys to yourself."
    else:
            $ Girl.change_face("normal", 1)
            ch_l "No way."
    $ Girl.recent_history.append("no_dildo")
    $ Girl.daily_history.append("no_dildo")
    $ temp_modifier = 0
    return

label Laura_DP_Prep: #Animation set-up
    if offhand_action == "dildo_pussy":
        return

    if not Girl.Forced and action_context != "auto":
        $ temp_modifier = 15 if Girl.PantsNum() >= 6 else 0
        call Bottoms_Off(Girl)
        if "angry" in Girl.recent_history:
            return

    $ temp_modifier = 0
    call Laura_Pussy_Launch("dildo_pussy")
    if not Girl.DildoP:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -75)
            $ Girl.change_stat("obedience", 70, 60)
            $ Girl.change_stat("inhibition", 80, 35)
        else:
            $ Girl.change_stat("love", 90, 10)
            $ Girl.change_stat("obedience", 70, 20)
            $ Girl.change_stat("inhibition", 80, 45)
    if Taboo:
        $ Girl.inhibition += int(Taboo/10)
        $ Girl.lust += int(Taboo/5)


    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ line = 0
    $ counter = 0
    if Taboo:
        $ Girl.DrainWord("tabno")
    $ Girl.DrainWord("no_dildo")
    $ Girl.recent_history.append("dildo_pussy")
    $ Girl.daily_history.append("dildo_pussy")

label Laura_DP_Cycle: #Repeating strokes
    while Round > 0:
        call shift_focus(Girl)
        call Laura_Pussy_Launch("dildo_pussy")
        $ Girl.lustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                call Slap_Ass(Girl)
                                jump Laura_DP_Cycle

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
                                            if Girl.Action and multi_action:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ Girl.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Shift primary action":
                                            if Girl.Action and multi_action:
                                                    menu:
                                                        "I want to stick a finger in her ass.":
                                                                $ action_context = "shift"
                                                                call Laura_DP_After
                                                                call Laura_Insert_Ass
                                                        "Just stick a finger in her ass without asking.":
                                                                $ action_context = "auto"
                                                                call Laura_DP_After
                                                                call Laura_Insert_Ass
                                                        "I want to shift the dildo to her ass.":
                                                                $ action_context = "shift"
                                                                call Laura_DP_After
                                                                call Laura_Dildo_Ass
                                                        "Never Mind":
                                                                jump Laura_DP_Cycle
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Shift your focus" if offhand_action:
                                                $ action_context = "shift focus"
                                                call Laura_DP_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not offhand_action:
                                                pass
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [Girl.Name] to do something else with [Partner.Name]" if primary_action == "lesbian":
                                                        call Les_Change(Girl)
                                            "Ask [Girl.Name] to do something else with [Partner.Name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(Girl)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.Name]":
                                                        call primary_action_Swap(Girl)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Laura_DP_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Laura_DP_Cycle
                                            "Never mind":
                                                        jump Laura_DP_Cycle
                                    "undress [Girl.Name]":
                                            call Girl_Undress(Girl)
                                    "Clean up [Girl.Name] (locked)" if not Girl.Spunk:
                                            pass
                                    "Clean up [Girl.Name]" if Girl.Spunk:
                                            call Girl_Cleanup(Girl,"ask")
                                    "Never mind":
                                            jump Laura_DP_Cycle

                        "Back to Sex Menu" if multi_action:
                                    ch_p "Let's try something else."
                                    call Laura_Pos_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Laura_DP_After
                        "End Scene" if not multi_action:
                                    ch_p "Let's stop for now."
                                    call Laura_Pos_Reset
                                    $ line = 0
                                    jump Laura_DP_After
        #End menu (if line)

        if Girl.Panties or Girl.PantsNum() >= 6 or Girl.HoseNum() >= 5: #This checks if Laura wants to strip down.
                call Girl_Undress(Girl,"auto")

        call shift_focus(Girl)
        call Sex_Dialog(Girl,Partner)

        #If either of you could cum

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or Girl.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(Girl)
                            if "angry" in Girl.recent_history:
                                call Laura_Pos_Reset
                                return
                            $ Girl.change_stat("lust", 200, 5)
                            if 100 > Girl.lust >= 70 and Girl.OCount < 2:
                                $ Girl.recent_history.append("unsatisfied")
                                $ Girl.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Laura_DP_After
                            $ line = "came"

                    if Girl.lust >= 100:
                            #If Laura can cum
                            call Girl_Cumming(Girl)
                            if action_context == "shift" or "angry" in Girl.recent_history:
                                jump Laura_DP_After

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in Girl.recent_history:#And Laura is unsatisfied,
                                "[Girl.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Laura_DP_After
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if Girl.SEXP >= 100 or ApprovalCheck(Girl, 1200, "LO"):
            pass
        elif counter == (5 + Girl.DildoP):
                    $ Girl.Brows = "confused"
                    ch_l "What are you even doing down there?"
        elif Girl.lust >= 80:
                    pass
        elif counter == (15 + Girl.DildoP) and Girl.SEXP >= 15 and not ApprovalCheck(Girl, 1500):
                    $ Girl.Brows = "confused"
                    menu:
                        ch_l "[Girl.Petname], this is getting uncomfortable, maybe we could try something else."
                        "Finish up.":
                                "You let go. . ."
                                jump Laura_DP_After
                        "Let's try something else." if multi_action:
                                $ line = 0
                                $ action_context = "shift"
                                jump Laura_DP_After
                        "No, this is fun.":
                                if ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "O"):
                                    $ Girl.change_stat("love", 200, -5)
                                    $ Girl.change_stat("obedience", 50, 3)
                                    $ Girl.change_stat("obedience", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ Girl.change_face("angry", 1)
                                    call Laura_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_l "Well if that's your attitude, I don't need your \"help\"."
                                    $ Girl.change_stat("love", 50, -3, 1)
                                    $ Girl.change_stat("love", 80, -4, 1)
                                    $ Girl.change_stat("obedience", 30, -1, 1)
                                    $ Girl.change_stat("obedience", 50, -1, 1)
                                    $ Girl.recent_history.append("angry")
                                    $ Girl.daily_history.append("angry")
                                    jump Laura_DP_After
        #End Count check

        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [Girl.Petname]."

    #Round = 0 loop breaks
    $ Girl.change_face("bemused", 0)
    $ line = 0
    ch_l "Ok, [Girl.Petname], breaktime."


label Laura_DP_After:
    if not action_context: #fix  action_context != "shift" and action_context != "auto" and action_context != "pullback":
        call Laura_Pos_Reset

    $ Girl.change_face("sexy")

    $ Girl.DildoP += 1
    $ Girl.Action -=1

    call Partner_Like(Girl,1)

    if Girl.DildoP == 1:
            $ Girl.SEXP += 10
            if not action_context:
                if Girl.love >= 500 and "unsatisfied" not in Girl.recent_history:
                    ch_l "Thanks for the extra hand. . ."
                elif Girl.obedience <= 500 and Player.Focus <= 20:
                    $ Girl.change_face("perplexed", 1)
                    ch_l "Did you like that?"

    $ temp_modifier = 0
#    if action_context == "shift":
#        ch_l "Mmm, so what else did you have in mind?"
    call Checkout
    return

# end Girl.Dildo Pussy /////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////Start Insert Ass

label Laura_Dildo_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus(Girl)
    call Laura_Dildo_Check
    if not _return:
        return

    if Girl.Loose:
        $ temp_modifier += 30
    elif "anal" in Girl.recent_history or "dildo_anal" in Girl.recent_history:
        $ temp_modifier -= 20
    elif "anal" in Girl.daily_history or "dildo_anal" in Girl.daily_history:
        $ temp_modifier -= 10
    elif (Girl.Anal + Girl.DildoA + Girl.Plug) > 0: #You've done it before
        $ temp_modifier += 20

    if Girl.Legs == "pants:": # she's got pants on.
        $ temp_modifier -= 20

    if Girl.lust > 95:
        $ temp_modifier += 20
    elif Girl.lust > 85: #She's really horny
        $ temp_modifier += 15

    if action_context == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in Girl.Traits:
        $ temp_modifier += (5*Taboo)
    if Girl in Player.Harem or "sex friend" in Girl.Petnames:
        $ temp_modifier += 10
    elif "ex" in Girl.Traits:
        $ temp_modifier -= 40
    if Girl.ForcedCount and not Girl.Forced:
        $ temp_modifier -= 5 * Girl.ForcedCount

    if Taboo and "tabno" in Girl.daily_history:
        $ temp_modifier -= 10

    if "no_dildo" in Girl.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no_dildo" in Girl.recent_history else 0

    $ Approval = ApprovalCheck(Girl, 1450, TabM = 4) # 145, 160, 175, Taboo -160(355)

    if action_context == Girl:
            #Laura auto-starts
            if Approval > 2:                                                      # fix, add laura auto stuff here
                if Girl.wearing_skirt:
                    "[Girl.Name] grabs her dildo, hiking up her skirt as she does."
                    $ Girl.Upskirt = 1
                elif Girl.PantsNum() >= 6:
                    "[Girl.Name] grabs her dildo, pulling down her pants as she does."
                    $ Girl.Legs = 0
                else:
                    "[Girl.Name] grabs her dildo, rubbing is suggestively against her ass."
                $ Girl.SeenPanties = 1
                call Laura_First_Bottomless(1)
                "She slides the tip against her asshole, and seems to want you to insert it."
                menu:
                    "What do you do?"
                    "Nothing.":
                        $ Girl.change_stat("inhibition", 80, 3)
                        $ Girl.change_stat("inhibition", 50, 2)
                        "[Girl.Name] slides it in."
                    "Go for it.":
                        $ Girl.change_face("sexy", 1)
                        $ Girl.change_stat("inhibition", 80, 3)
                        ch_p "Oh yeah, [Girl.Pet], let's do this."
                        $ Girl.NameCheck() #checks reaction to petname
                        "You grab the dildo and slide it in."
                        $ Girl.change_stat("love", 85, 1)
                        $ Girl.change_stat("obedience", 90, 1)
                        $ Girl.change_stat("obedience", 50, 2)
                    "Ask her to stop.":
                        $ Girl.change_face("surprised")
                        $ Girl.change_stat("inhibition", 70, 1)
                        ch_p "Let's not do that right now, [Girl.Pet]."
                        $ Girl.NameCheck() #checks reaction to petname
                        "[Girl.Name] sets the dildo down."
                        $ Girl.OutfitChange()
                        $ Girl.change_stat("obedience", 90, 1)
                        $ Girl.change_stat("obedience", 50, 1)
                        $ Girl.change_stat("obedience", 30, 2)
                        return
                jump Laura_DA_Prep
            else:
                $ temp_modifier = 0                               # fix, add laura auto stuff here
                $ offhand_action = 0
            return

    if action_context == "auto":
            "You rub the dildo across her body, and against her tight anus."
            $ Girl.change_face("surprised", 1)

            if (Girl.DildoA and Approval) or (Approval > 1):
                #this is not the first time you've had sex, or she's into it
                "[Girl.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                $ Girl.change_face("sexy")
                $ Girl.change_stat("obedience", 70, 3)
                $ Girl.change_stat("inhibition", 50, 3)
                $ Girl.change_stat("inhibition", 70, 1)
                ch_l "Ooo, [Girl.Petname], toys!"
                jump Laura_DA_Prep
            else:
                #she's questioning it
                $ Girl.Brows = "angry"
                menu:
                    ch_l "Hey, what are you planning to do with that?!"
                    "Sorry, sorry! Never mind.":
                        if Approval:
                            $ Girl.change_face("sexy", 1)
                            $ Girl.change_stat("obedience", 70, 3)
                            $ Girl.change_stat("inhibition", 50, 3)
                            $ Girl.change_stat("inhibition", 70, 1)
                            ch_l "Well, now that you mention it. . ."
                            jump Laura_DA_Prep
                        "You pull back before you really get it in."
                        $ Girl.change_face("bemused", 1)
                        if Girl.DildoA:
                            ch_l "Well ok, [Girl.Petname], maybe warn me next time?"
                        else:
                            ch_l "Well ok, [Girl.Petname], that's a little much. . . for now . . ."
                    "Just playing with my favorite toys.":
                        $ Girl.change_stat("love", 80, -10, 1)
                        $ Girl.change_stat("love", 200, -10)
                        "You press it inside some more."
                        $ Girl.change_stat("obedience", 70, 3)
                        $ Girl.change_stat("inhibition", 50, 3)
                        if not ApprovalCheck(Girl, 700, "O", TabM=1): #Checks if obedience is 700+
                            $ Girl.change_face("angry")
                            "[Girl.Name] shoves you away and slaps you in the face."
                            ch_l "Jerk!"
                            ch_l "Ask nice if you want to stick something in my ass!"
                            $ Girl.change_stat("love", 50, -10, 1)
                            $ Girl.change_stat("obedience", 50, 3)
                            $ renpy.pop_call()
                            if action_context:
                                $ renpy.pop_call()
                            if renpy.showing("Laura_SexSprite"):
                                call Laura_Sex_Reset
                            $ Girl.recent_history.append("angry")
                            $ Girl.daily_history.append("angry")
                        else:
                            $ Girl.change_face("sad")
                            "[Girl.Name] doesn't seem to be into this, you're lucky she's so obedient."
                            jump Laura_DA_Prep
            return
    #end auto

    if not Girl.DildoA:
            #first time
            $ Girl.change_face("surprised", 1)
            $ Girl.Mouth = "kiss"
            ch_l "You want to try and fit that. . .?"
            if Girl.Forced:
                $ Girl.change_face("sad")
                ch_l "Always about the butt, huh?"

    if not Girl.Loose and ("dildo_anal" in Girl.recent_history or "anal" in Girl.recent_history or "dildo_anal" in Girl.daily_history or "anal" in Girl.daily_history):
            $ Girl.change_face("bemused", 1)
            ch_l "I'm still sore from earlier. . ."

    if not Girl.DildoA and Approval:
            #First time dialog
            if Girl.Forced:
                $ Girl.change_face("sad")
                $ Girl.change_stat("love", 70, -3, 1)
                $ Girl.change_stat("love", 20, -2, 1)
            elif Girl.love >= (Girl.obedience + Girl.inhibition):
                $ Girl.change_face("sexy")
                $ Girl.Brows = "sad"
                $ Girl.Mouth = "smile"
                ch_l "I haven't actually used one of these, back there before. . ."
            elif Girl.obedience >= Girl.inhibition:
                $ Girl.change_face("normal")
                ch_l "If that's what you want, [Girl.Petname]. . ."
            else: # Uninhibited
                $ Girl.change_face("sad")
                $ Girl.Mouth = "smile"
                ch_l "I guess it could be fun two-player. . ."

    elif Approval:
            #Second time+ dialog
            if Girl.Forced:
                $ Girl.change_face("sad")
                $ Girl.change_stat("love", 70, -3, 1)
                $ Girl.change_stat("love", 20, -2, 1)
                ch_l "The toys again?"
            elif not Taboo and "tabno" in Girl.daily_history:
                ch_l "Well, at least you got us some privacy this time. . ."
            elif "dildo_anal" in Girl.daily_history and not Girl.Loose:
                pass
            elif "dildo_anal" in Girl.daily_history:
                $ Girl.change_face("sexy", 1)
                $ line = renpy.random.choice(["Breaking out the toys again?",
                    "Didn't get enough earlier?",
                    "I'm still a bit sore from earlier.",
                    "You're going to wear me out."])
                ch_l "[line]"
            elif Girl.DildoA < 3:
                $ Girl.change_face("sexy", 1)
                $ Girl.Brows = "confused"
                $ Girl.Mouth = "kiss"
                ch_l "You want to stick it in my ass again?"
            else:
                $ Girl.change_face("sexy", 1)
                $ Girl.ArmPose = 2
                $ line = renpy.random.choice(["You want some of this action?",
                    "So you'd like another go?",
                    "You want to stick it in my ass again?",
                    "You want me ta lube up your toy?"])
                ch_l "[line]"
                $ line = 0

    if Approval >= 2:
            #She's into it. . .
            if Girl.Forced:
                $ Girl.change_face("sad")
                $ Girl.change_stat("obedience", 90, 1)
                $ Girl.change_stat("inhibition", 60, 1)
                ch_l "Ok, fine."
            else:
                $ Girl.change_face("sexy", 1)
                $ Girl.change_stat("love", 90, 1)
                $ Girl.change_stat("inhibition", 50, 3)
                $ line = renpy.random.choice(["Well, sure, stick it in.",
                    "Well. . . ok.",
                    "Sure!",
                    "I guess I could. . . stick it in.",
                    "Hells yeah.",
                    "Heh, ok, ok."])
                ch_l "[line]"
                $ line = 0
            $ Girl.change_stat("obedience", 20, 1)
            $ Girl.change_stat("obedience", 60, 1)
            $ Girl.change_stat("inhibition", 70, 2)
            jump Laura_DA_Prep

    else:
            #She's not into it, but maybe. . .
            $ Girl.change_face("angry")
            if "no_dildo" in Girl.recent_history:
                ch_l "What part of \"no,\" did you not get, [Girl.Petname]?"
            elif Taboo and "tabno" in Girl.daily_history and "no_dildo" in Girl.daily_history:
                ch_l "Stop swinging that thing around in public!"
            elif "no_dildo" in Girl.daily_history:
                ch_l "I already told you \"no,\" [Girl.Petname]."
            elif Taboo and "tabno" in Girl.daily_history:
                ch_l "I already told you that I wouldn't do that out here!"
            elif not Girl.DildoA:
                $ Girl.change_face("bemused")
                ch_l "I'm just not into toys, [Girl.Petname]. . ."
            elif not Girl.Loose and "dildo_anal" not in Girl.daily_history:
                $ Girl.change_face("perplexed")
                ch_l "You could have been a bit more gentle last time, [Girl.Petname]. . ."
            else:
                $ Girl.change_face("bemused")
                ch_l "I don't think we need any toys, [Girl.Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no_dildo" in Girl.daily_history:
                    $ Girl.change_face("bemused")
                    ch_l "Yeah, ok, [Girl.Petname]."
                    return
                "Maybe later?" if "no_dildo" not in Girl.daily_history:
                    $ Girl.change_face("sexy")
                    ch_l "Maybe I'll practice on my own time, [Girl.Petname]."
                    $ Girl.change_stat("love", 80, 2)
                    $ Girl.change_stat("inhibition", 70, 2)
                    if Taboo:
                        $ Girl.recent_history.append("tabno")
                        $ Girl.daily_history.append("tabno")
                    $ Girl.recent_history.append("no_dildo")
                    $ Girl.daily_history.append("no_dildo")
                    return
                "I think you'd like it. . .":
                    if Approval:
                        $ Girl.change_face("sexy")
                        $ Girl.change_stat("obedience", 90, 2)
                        $ Girl.change_stat("obedience", 50, 2)
                        $ Girl.change_stat("inhibition", 70, 3)
                        $ Girl.change_stat("inhibition", 40, 2)
                        $ line = renpy.random.choice(["Well, sure, stick it in.",
                            "I suppose. . .",
                            "You've got me there."])
                        ch_l "[line]"
                        $ line = 0
                        jump Laura_DA_Prep
                    else:
                        pass

                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck(Girl, 1050, "OI", TabM = 3) # 105, 120, 135, -120(225)
                    if Approval > 1 or (Approval and Girl.Forced):
                        $ Girl.change_face("sad")
                        $ Girl.change_stat("love", 70, -5, 1)
                        $ Girl.change_stat("love", 200, -5)

                        $ Girl.change_stat("obedience", 80, 4)
                        $ Girl.change_stat("inhibition", 80, 1)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.Forced = 1
                        jump Laura_DA_Prep
                    else:
                        $ Girl.change_stat("love", 200, -20)
                        $ Girl.recent_history.append("angry")
                        $ Girl.daily_history.append("angry")

    #She refused all offers.
    $ Girl.ArmPose = 1
    if "no_dildo" in Girl.daily_history:

            $ Girl.recent_history.append("angry")
            $ Girl.daily_history.append("angry")
    elif Girl.Forced:
            $ Girl.change_face("angry", 1)
            ch_l "I'm not going to let you use that on me."
            $ Girl.change_stat("lust", 200, 5)
            if Girl.love > 300:
                    $ Girl.change_stat("love", 70, -2)
            $ Girl.change_stat("obedience", 50, -2)
            $ Girl.recent_history.append("angry")
            $ Girl.daily_history.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
            $ Girl.change_face("angry", 1)
            $ Girl.recent_history.append("tabno")
            $ Girl.daily_history.append("tabno")
            ch_l "Not here!"
            $ Girl.change_stat("lust", 200, 5)
            $ Girl.change_stat("obedience", 50, -3)
    elif not Girl.Loose and "dildo_anal" in Girl.daily_history:
            $ Girl.change_face("bemused")
            ch_l "Sorry, I just need a little break back there, [Girl.Petname]."
    elif Girl.DildoA:
            $ Girl.change_face("sad")
            ch_l "Sorry, you can keep your toys out of there."
    else:
            $ Girl.change_face("normal", 1)
            ch_l "No way."
    $ Girl.recent_history.append("no_dildo")
    $ Girl.daily_history.append("no_dildo")
    $ temp_modifier = 0
    return

label Laura_DA_Prep: #Animation set-up
    if offhand_action == "dildo_anal":
        return

    if not Girl.Forced and action_context != "auto":
        $ temp_modifier = 20 if Girl.PantsNum() >= 6 else 0
        call Bottoms_Off(Girl)
        if "angry" in Girl.recent_history:
            return

    $ temp_modifier = 0
    call Laura_Pussy_Launch("dildo_anal")
    if not Girl.DildoA:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -75)
            $ Girl.change_stat("obedience", 70, 60)
            $ Girl.change_stat("inhibition", 80, 35)
        else:
            $ Girl.change_stat("love", 90, 10)
            $ Girl.change_stat("obedience", 70, 20)
            $ Girl.change_stat("inhibition", 80, 45)
    if Taboo:
        $ Girl.inhibition += int(Taboo/10)
        $ Girl.lust += int(Taboo/5)


    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ line = 0
    $ counter = 0
    if Taboo:
        $ Girl.DrainWord("tabno")
    $ Girl.DrainWord("no_dildo")
    $ Girl.recent_history.append("dildo_anal")
    $ Girl.daily_history.append("dildo_anal")

label Laura_DA_Cycle: #Repeating strokes
    while Round > 0:
        call shift_focus(Girl)
        call Laura_Pussy_Launch("dildo_anal")
        $ Girl.lustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                call Slap_Ass(Girl)
                                jump Laura_DA_Cycle

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
                                            if Girl.Action and multi_action:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ Girl.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Shift primary action":
                                            if Girl.Action and multi_action:
                                                    menu:
                                                        "I want to stick a finger in her pussy.":
                                                                $ action_context = "shift"
                                                                call Laura_DA_After
                                                                call Laura_Fondle_Pussy
                                                        "Just stick a finger in her pussy without asking.":
                                                                $ action_context = "auto"
                                                                call Laura_DA_After
                                                                call Laura_Fondle_Pussy
                                                        "I want to shift the dildo to her pussy.":
                                                                $ action_context = "shift"
                                                                call Laura_DA_After
                                                                call Laura_Dildo_Pussy
                                                        "Never Mind":
                                                                jump Laura_DA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Shift your focus" if offhand_action:
                                                $ action_context = "shift focus"
                                                call Laura_DA_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not offhand_action:
                                                pass
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [Girl.Name] to do something else with [Partner.Name]" if primary_action == "lesbian":
                                                        call Les_Change(Girl)
                                            "Ask [Girl.Name] to do something else with [Partner.Name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(Girl)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.Name]":
                                                        call primary_action_Swap(Girl)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Laura_DA_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Laura_DA_Cycle
                                    "Never mind":
                                            jump Laura_DA_Cycle

                        "Back to Sex Menu" if multi_action:
                                    ch_p "Let's try something else."
                                    call Laura_Pos_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Laura_DA_After
                        "End Scene" if not multi_action:
                                    ch_p "Let's stop for now."
                                    call Laura_Pos_Reset
                                    $ line = 0
                                    jump Laura_DA_After
        #End menu (if line)

        if Girl.Panties or Girl.PantsNum() >= 6 or Girl.HoseNum() >= 5: #This checks if Laura wants to strip down.
                call Girl_Undress(Girl,"auto")

        call shift_focus(Girl)
        call Sex_Dialog(Girl,Partner)

        #If either of you could cum

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or Girl.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(Girl)
                            if "angry" in Girl.recent_history:
                                call Laura_Pos_Reset
                                return
                            $ Girl.change_stat("lust", 200, 5)
                            if 100 > Girl.lust >= 70 and Girl.OCount < 2:
                                $ Girl.recent_history.append("unsatisfied")
                                $ Girl.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Laura_DA_After
                            $ line = "came"

                    if Girl.lust >= 100:
                            #If Laura can cum
                            call Girl_Cumming(Girl)
                            if action_context == "shift" or "angry" in Girl.recent_history:
                                jump Laura_DA_After

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in Girl.recent_history:#And Laura is unsatisfied,
                                "[Girl.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Laura_DA_After
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if Girl.SEXP >= 100 or ApprovalCheck(Girl, 1200, "LO"):
            pass
        elif counter == (5 + Girl.DildoA):
                    $ Girl.Brows = "confused"
                    ch_l "What are you even doing down there?"
        elif Girl.lust >= 80:
                    pass
        elif counter == (15 + Girl.DildoA) and Girl.SEXP >= 15 and not ApprovalCheck(Girl, 1500):
                    $ Girl.Brows = "confused"
                    menu:
                        ch_l "[Girl.Petname], this is getting uncomfortable, maybe we could try something else."
                        "Finish up.":
                                "You let go. . ."
                                jump Laura_DA_After
                        "Let's try something else." if multi_action:
                                $ line = 0
                                $ action_context = "shift"
                                jump Laura_DA_After
                        "No, this is fun.":
                                if ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "O"):
                                    $ Girl.change_stat("love", 200, -5)
                                    $ Girl.change_stat("obedience", 50, 3)
                                    $ Girl.change_stat("obedience", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ Girl.change_face("angry", 1)
                                    call Laura_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_l "Well if that's your attitude, I don't need your \"help\"."
                                    $ Girl.change_stat("love", 50, -3, 1)
                                    $ Girl.change_stat("love", 80, -4, 1)
                                    $ Girl.change_stat("obedience", 30, -1, 1)
                                    $ Girl.change_stat("obedience", 50, -1, 1)
                                    $ Girl.recent_history.append("angry")
                                    $ Girl.daily_history.append("angry")
                                    jump Laura_DA_After
        #End Count check

        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [Girl.Petname]."

    #Round = 0 loop breaks
    $ Girl.change_face("bemused", 0)
    $ line = 0
    ch_l "Ok, [Girl.Petname], breaktime."

label Laura_DA_After:
    if not action_context: #fix  action_context != "shift" and action_context != "auto" and action_context != "pullback":
        call Laura_Pos_Reset

    $ Girl.change_face("sexy")

    $ Girl.DildoA += 1
    $ Girl.Action -=1

    call Partner_Like(Girl,1)

    if Girl.DildoA == 1:
            $ Girl.SEXP += 10
            if not action_context:
                if Girl.love >= 500 and "unsatisfied" not in Girl.recent_history:
                    if Girl.Loose:
                        ch_l "That was. . . interesting. . ."
                    else:
                        ch_l "Ouch. . ."
                elif Girl.obedience <= 500 and Player.Focus <= 20:
                    $ Girl.change_face("perplexed", 1)
                    ch_l "Did you like that?"

    $ temp_modifier = 0
#    if action_context == "shift":
#        ch_l "Mmm, so what else did you have in mind?"
    call Checkout
    return

# end Girl.Dildo Ass /////////////////////////////////////////////////////////////////////////////

label Laura_Vibrator_Check:                                                                                 #fix this whole section is copy/paste unfinished
    if "vibrator" in Player.Inventory:
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in Girl.Inventory:
        "You ask [Girl.Name] to get out her vibrator."
    else:
        "You don't have one of those on you."
        return 0
    return 1

## Girl.Footjob //////////////////////////////////////////////////////////////////////
label Laura_Footjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call shift_focus(Girl)
    if Girl.Foot >= 7: # She loves it
        $ temp_modifier += 10
    elif Girl.Foot >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif Girl.Foot: #You've done it before
        $ temp_modifier += 3

    if Girl.Addict >= 75 and Girl.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 10
    if Girl.Addict >= 75:
        $ temp_modifier += 5

    if action_context == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in Girl.Traits:
        $ temp_modifier += (3*Taboo)
    if Girl in Player.Harem or "sex friend" in Girl.Petnames:
        $ temp_modifier += 10
    elif "ex" in Girl.Traits:
        $ temp_modifier -= 40
    if Girl.ForcedCount and not Girl.Forced:
        $ temp_modifier -= 5 * Girl.ForcedCount

    if Taboo and "tabno" in Girl.daily_history:
        $ temp_modifier -= 10

    if "no_foot" in Girl.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no_foot" in Girl.recent_history else 0

    $ Approval = ApprovalCheck(Girl, 1250, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if action_context == Girl:                                                                  #Laura auto-starts
        if Approval > 2:                                                      # fix, add laura auto stuff here
            "[Girl.Name] leans back  and starts rubbing your cock with her foot."
            menu:
                "What do you do?"
                "Nothing.":
                    $ Girl.change_stat("inhibition", 70, 3)
                    $ Girl.change_stat("inhibition", 30, 2)
                    "[Girl.Name] continues her actions."
                "Praise her.":
                    $ Girl.change_face("sexy", 1)
                    $ Girl.change_stat("inhibition", 70, 3)
                    ch_p "Oooh, that's good, [Girl.Pet]."
                    $ Girl.NameCheck() #checks reaction to petname
                    "[Girl.Name] continues her actions."
                    $ Girl.change_stat("love", 80, 1)
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ Girl.change_face("surprised")
                    $ Girl.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that for now, [Girl.Pet]."
                    $ Girl.NameCheck() #checks reaction to petname
                    "[Girl.Name] puts it down."
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Girl.change_stat("obedience", 30, 2)
                    return
            if primary_action:
                $ girl_offhand_action = "footjob"
                return
            jump Laura_FJ_Prep
        else:
            $ temp_modifier = 0                               # fix, add laura auto stuff here
            $ offhand_action = 0
            return

    if not Girl.Foot and "no_foot" not in Girl.recent_history:
        $ Girl.change_face("confused", 2)
        ch_l "Standard footjob?"
        $ Girl.Blush = 1

    if not Girl.Foot and Approval:                                                 #First time dialog
        if Girl.Forced:
            $ Girl.change_face("sad",1)
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
        elif Girl.love >= (Girl.obedience + Girl.inhibition):
            $ Girl.change_face("sexy",1)
            $ Girl.Brows = "sad"
            $ Girl.Mouth = "smile"
            ch_l "I guess it couldn't hurt. . ."
        elif Girl.obedience >= Girl.inhibition:
            $ Girl.change_face("normal",1)
            ch_l "If you want, [Girl.Petname]. . ."
        elif Girl.Addict >= 50:
            $ Girl.change_face("manic", 1)
            ch_l "Okay. . ."
        else: # Uninhibited
            $ Girl.change_face("lipbite",1)
            ch_l "Sure. . ."

    elif Approval:                                                                       #Second time+ dialog
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
            ch_l "That's it?"
        elif not Taboo and "tabno" in Girl.daily_history:
            ch_l "Um, I guess this is secure enough. . ."
        elif "footjob" in Girl.daily_history:
            $ Girl.change_face("sexy", 1)
            ch_l "More of that, huh. . ."
            jump Laura_FJ_Prep
#        elif "footjob" in Girl.daily_history:
#            $ Girl.change_face("sexy", 1)
#            $ line = renpy.random.choice(["Another one?",
#                "Didn't get enough earlier?",
#                "My feet are kinda sore from earlier.",
#                "My feet are kinda sore from earlier."])
#            ch_l "[line]"
        elif Girl.Foot < 3:
            $ Girl.change_face("sexy", 1)
            $ Girl.Brows = "confused"
            $ Girl.Mouth = "kiss"
            ch_l "Hmm, magic toes. . ."
        else:
            $ Girl.change_face("sexy", 1)
            $ Girl.ArmPose = 2
            $ line = renpy.random.choice(["You want me to use my feet?",
                "So you'd like another footjob?",
                "A little. . . [she rubs her foot along your leg]?",
                "A little TLC?"])
            ch_l "[line]"
        $ line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 60, 1)
            ch_l "Ok, sure."
        elif "no_foot" in Girl.daily_history:
            ch_l "Fine."
        else:
            $ Girl.change_face("sexy", 1)
            $ Girl.change_stat("love", 90, 1)
            $ Girl.change_stat("inhibition", 50, 3)
            $ line = renpy.random.choice(["Sure, I guess.",
                "OK.",
                "Fine, lemme see it.",
                "I guess I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Heh, ok, ok."])
            ch_l "[line]"
            $ line = 0
        $ Girl.change_stat("obedience", 20, 1)
        $ Girl.change_stat("obedience", 60, 1)
        $ Girl.change_stat("inhibition", 70, 2)
        jump Laura_FJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ Girl.change_face("angry")
        if "no_foot" in Girl.recent_history:
            ch_l "You should listen better, [Girl.Petname]."
        elif Taboo and "tabno" in Girl.daily_history and "no_foot" in Girl.daily_history:
            ch_l "I said not in public."
        elif "no_foot" in Girl.daily_history:
            ch_l "I told you \"no,\" [Girl.Petname]."
        elif Taboo and "tabno" in Girl.daily_history:
            ch_l "I said not in public!"
        elif not Girl.Foot:
            $ Girl.change_face("bemused")
            ch_l "Eh, [Girl.Petname]. . ."
        else:
            $ Girl.change_face("bemused")
            ch_l "Not now, ok?"
        menu:
            extend ""
            "Sorry, never mind." if "no_foot" in Girl.daily_history:
                $ Girl.change_face("bemused")
                ch_l "Sure, no problem."
                return
            "Maybe later?" if "no_foot" not in Girl.daily_history:
                $ Girl.change_face("sexy")
                ch_l ". . ."
                ch_l "Maybe."
                $ Girl.change_stat("love", 80, 2)
                $ Girl.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ Girl.recent_history.append("tabno")
                    $ Girl.daily_history.append("tabno")
                $ Girl.recent_history.append("no_foot")
                $ Girl.daily_history.append("no_foot")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ Girl.change_face("sexy")
                    $ Girl.change_stat("obedience", 90, 2)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("inhibition", 70, 3)
                    $ Girl.change_stat("inhibition", 40, 2)
                    $ line = renpy.random.choice(["Sure, I guess.",
                        "OK.",
                        "Fine, lemme see it.",
                        "I guess I could. . .",
                        "Ok. . . [She gestures for you to come over].",
                        "Heh, ok, ok."])
                    ch_l "[line]"
                    $ line = 0
                    jump Laura_FJ_Prep
                else:
                    pass

            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck(Girl, 400, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and Girl.Forced):
                    $ Girl.change_face("sad")
                    $ Girl.change_stat("love", 70, -5, 1)
                    $ Girl.change_stat("love", 200, -2)

                    $ Girl.change_stat("obedience", 50, 4)
                    $ Girl.change_stat("inhibition", 80, 1)
                    $ Girl.change_stat("inhibition", 60, 3)
                    $ Girl.Forced = 1
                    jump Laura_FJ_Prep
                else:
                    $ Girl.change_stat("love", 200, -15)
                    $ Girl.recent_history.append("angry")
                    $ Girl.daily_history.append("angry")

    #She refused all offers.
    $ Girl.ArmPose = 1
    if "no_foot" in Girl.daily_history:
        $ Girl.change_face("angry", 1)

        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
    elif Girl.Forced:
        $ Girl.change_face("angry", 1)
        ch_l "You understand that I have claws down there too. . ."
        $ Girl.change_stat("lust", 200, 5)
        if Girl.love > 300:
                $ Girl.change_stat("love", 70, -2)
        $ Girl.change_stat("obedience", 50, -2)
        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ Girl.change_face("angry", 1)
        $ Girl.daily_history.append("tabno")
        ch_l "This is too exposed."
        $ Girl.change_stat("lust", 200, 5)
        $ Girl.change_stat("obedience", 50, -3)
    elif Girl.Foot:
        $ Girl.change_face("sad")
        ch_l "Not right now."
    else:
        $ Girl.change_face("normal", 1)
        ch_l "I'd rather not."
    $ Girl.recent_history.append("no_foot")
    $ Girl.daily_history.append("no_foot")
    $ temp_modifier = 0
    return


label Laura_FJ_Prep:
    if offhand_action == "footjob":
        return

    if Taboo:
        $ Girl.inhibition += int(Taboo/10)
        $ Girl.lust += int(Taboo/5)

    $ Girl.change_face("sexy")
    if Girl.Forced:
        $ Girl.change_face("sad")
    elif not Girl.Foot:
        $ Girl.Brows = "confused"
        $ Girl.Eyes = "sexy"
        $ Girl.Mouth = "smile"

    call Seen_First_Peen(Girl,Partner)

    if not Girl.Foot:
        if Girl.Forced:
            $ Girl.change_stat("love", 90, -20)
            $ Girl.change_stat("obedience", 70, 25)
            $ Girl.change_stat("inhibition", 80, 30)
        else:
            $ Girl.change_stat("love", 90, 5)
            $ Girl.change_stat("obedience", 70, 20)
            $ Girl.change_stat("inhibition", 80, 20)

    if action_context:
        $ renpy.pop_call()
        $ action_context = 0
    $ line = 0
    $ counter = 0
    if Taboo:
        $ Girl.DrainWord("tabno")
    $ Girl.DrainWord("no_foot")
    $ Girl.recent_history.append("footjob")
    $ Girl.daily_history.append("footjob")

label Laura_FJ_Cycle:
    while Round > 0:
        call shift_focus(Girl)
        call Laura_Sex_Launch("footjob")
        $ Girl.lustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if action_speed:
                                    pass

                        "Start moving? . ." if not action_speed:
                                    $ action_speed = 1

                        "action_speed up. . ." if action_speed < 2:
                                    $ action_speed += 1
                                    "You ask her to up the pace a bit."
                        "action_speed up. . . (locked)" if action_speed >= 2:
                                    pass

                        "Slow Down. . ." if action_speed:
                                    $ action_speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not action_speed:
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
                                    $ Girl.Pose = "doggy" if Girl.Pose != "doggy" else "sex"
                                    "You turn her around. . ."
                                    jump Laura_FJ_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if Girl.Action and multi_action:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ Girl.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Shift primary action":
                                            if Girl.Action and multi_action:
                                                    menu:
                                                        "How about a blowjob?":
                                                                    if Girl.Action and multi_action:
                                                                        $ action_context = "shift"
                                                                        call Laura_FJ_After
                                                                        call Laura_Blowjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(Girl,"tired")
                                                        "How about a handjob?":
                                                                    if Girl.Action and multi_action:
                                                                        $ action_context = "shift"
                                                                        call Laura_FJ_After
                                                                        call Laura_Handjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(Girl,"tired")

                                                        "How about a titjob?":
                                                                    if Girl.Action and multi_action:
                                                                        $ action_context = "shift"
                                                                        call Laura_FJ_After
                                                                        call Laura_Titjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(Girl,"tired")



                                                        "Never Mind":
                                                                jump Laura_FJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [Girl.Name] to do something else with [Partner.Name]" if primary_action == "lesbian":
                                                        call Les_Change(Girl)
                                            "Ask [Girl.Name] to do something else with [Partner.Name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(Girl)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.Name]":
                                                        call primary_action_Swap(Girl)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        jump Laura_FJ_Cycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Laura_FJ_Cycle
                                            "Never mind":
                                                        jump Laura_FJ_Cycle
                                    "undress [Girl.Name]":
                                            call Girl_Undress(Girl)
                                    "Clean up [Girl.Name] (locked)" if not Girl.Spunk:
                                            pass
                                    "Clean up [Girl.Name]" if Girl.Spunk:
                                            call Girl_Cleanup(Girl,"ask")
                                    "Never mind":
                                            jump Laura_FJ_Cycle

                        "Back to Sex Menu" if multi_action:
                                    ch_p "Let's try something else."
                                    call Laura_Sex_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Laura_FJ_After
                        "End Scene" if not multi_action:
                                    ch_p "Let's stop for now."
                                    call Laura_Sex_Reset
                                    $ line = 0
                                    jump Laura_FJ_After
        #End menu (if line)

        call shift_focus(Girl)
        call Sex_Dialog(Girl,Partner)

        #If either of you could cum

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or Girl.lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(Girl)
                            if "angry" in Girl.recent_history:
                                call Laura_Sex_Reset
                                return
                            $ Girl.change_stat("lust", 200, 5)
                            if 100 > Girl.lust >= 70 and Girl.OCount < 2:
                                $ Girl.recent_history.append("unsatisfied")
                                $ Girl.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Laura_FJ_After
                            $ line = "came"

                    if Girl.lust >= 100:
                            #If Laura can cum
                            call Girl_Cumming(Girl)
                            if action_context == "shift" or "angry" in Girl.recent_history:
                                jump Laura_FJ_After

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in Girl.recent_history:#And Laura is unsatisfied,
                                "[Girl.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Laura_FJ_After
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if counter == 20:
                    $ Girl.Brows = "angry"
                    menu:
                        ch_l "Hmm, this is getting a bit boring."
                        "How about a BJ?" if Girl.Action and multi_action:
                                $ action_context = "shift"
                                call Laura_FJ_After
                                call Laura_Blowjob
                        "How about a Handy?" if Girl.Action and multi_action:
                                $ action_context = "shift"
                                call Laura_FJ_After
                                call Laura_Handjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ counter += 1
                                "[line]"
                                jump Laura_FJ_Cycle
                        "Let's try something else." if multi_action:
                                $ line = 0
                                call Laura_Sex_Reset
                                $ action_context = "shift"
                                jump Laura_FJ_After
                        "No, get back down there.":
                                if ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "O"):
                                    $ Girl.change_stat("love", 200, -5)
                                    $ Girl.change_stat("obedience", 50, 3)
                                    $ Girl.change_stat("obedience", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    $ Girl.change_face("angry", 1)
                                    "She scowls at you and pulls back."
                                    ch_l "Not interested."
                                    $ Girl.change_stat("love", 50, -3, 1)
                                    $ Girl.change_stat("love", 80, -4, 1)
                                    $ Girl.change_stat("obedience", 30, -1, 1)
                                    $ Girl.change_stat("obedience", 50, -1, 1)
                                    $ Girl.recent_history.append("angry")
                                    $ Girl.daily_history.append("angry")
                                    jump Laura_FJ_After
        elif counter == 10 and Girl.SEXP <= 100 and not ApprovalCheck(Girl, 1200, "LO"):
                    $ Girl.Brows = "confused"
                    ch_l "Ok, seriously, let's try something different."
        #End Count check

        call Escalation(Girl) #sees if she wants to escalate things

        if Round == 10:
            ch_l "It's getting late, we should wrap this up."
        elif Round == 5:
            ch_l "Tic tock, [Girl.Petname]."

    #Round = 0 loop breaks
    $ Girl.change_face("bemused", 0)
    $ line = 0
    ch_l "Ok, [Girl.Petname], breaktime."

label Laura_FJ_After:
    $ Girl.change_face("sexy")

    $ Girl.Foot += 1
    $ Girl.Action -=1
    $ Girl.Addictionrate += 1
    if Player.addictive:
        $ Girl.Addictionrate += 1
    $ Girl.change_stat("lust", 90, 5)

    call Partner_Like(Girl,1)

    if "Laurapedi" in Achievements:
            pass
    elif Girl.Foot >= 10:
            $ Girl.change_face("smile", 1)
            ch_l "I think I'm finally back into practice on this."
            $ Achievements.append("Laurapedi")
            $ Girl.SEXP += 5
    elif Girl.Foot == 1:
            $ Girl.SEXP += 10
            if Girl.love >= 500:
                $ Girl.Mouth = "smile"
                ch_l "Did you like that? . ."
            elif Player.Focus <= 20:
                $ Girl.Mouth = "sad"
                ch_l "Did that do it for you?"
    elif Girl.Foot == 5:
                ch_l "I'm getting used to this. . ."

    $ temp_modifier = 0
    if action_context == "shift":
        ch_l "Ok, so what did you have in mind?"
    else:
        call Laura_Sex_Reset
    call Checkout
    return

## end Girl.Footjob //////////////////////////////////////////////////////////////////////
