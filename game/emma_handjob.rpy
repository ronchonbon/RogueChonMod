## Girl.Handjob //////////////////////////////////////////////////////////////////////
label Emma_Handjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(Girl)
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

    if "no hand" in Girl.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no hand" in Girl.recent_history else 0

    $ Approval = ApprovalCheck(Girl, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if not Girl.Hand and "no hand" not in Girl.recent_history:
        $ Girl.change_face("sly", 2)
        ch_e "You'd like me to take care of that for you?"

    if not Girl.Hand and Approval:                                                 #First time dialog
        if Girl.Forced:
            $ Girl.change_face("sad",1)
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
        elif Girl.love >= (Girl.obedience + Girl.inhibition):
            $ Girl.change_face("sexy",1)
            $ Girl.Brows = "sad"
            $ Girl.Mouth = "smile"
            ch_e "I suppose you've earned something. . ."
        elif Girl.obedience >= Girl.inhibition:
            $ Girl.change_face("normal",1)
            ch_e "If that's what you'd like, [Girl.Petname]. . ."
        elif Girl.Addict >= 50:
            $ Girl.change_face("manic", 1)
            ch_e "Mmmmmmmm. . ."
        else: # Uninhibited
            $ Girl.change_face("lipbite",1,Eyes="side")
            ch_e "I suppose. . ."

    elif Approval:                                                                       #Second time+ dialog
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
            ch_e "No more than that?"
        elif not Taboo and "tabno" in Girl.daily_history:
            ch_e "Here, hmm?. . ."
        elif "hand" in Girl.recent_history:
            $ Girl.change_face("sexy", 1)
            ch_e "I will need to grade papers later, you know. . ."
            jump Emma_HJ_Prep
        elif "hand" in Girl.daily_history:
            $ Girl.change_face("sexy", 1)
            $ line = renpy.random.choice(["Another?",
                "You're going to wear out my arm.",
                "Didn't get enough earlier?",
                "My hand's a bit sore from earlier.",
                "My hand's rather sore from before."])
            ch_e "[line]"
        elif Girl.Hand < 3:
            $ Girl.change_face("sly", 1)
            ch_e "Enjoyed last time?. . ."
        else:
            $ Girl.change_face("sexy", 1)
            $ Girl.ArmPose = 2
            $ line = renpy.random.choice(["You want more?",
                "So you'd like another?",
                "More of this? [fist pumping hand gestures]",
                "Oh, did you want some attention?"])
            ch_e "[line]"
        $ line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 60, 1)
            ch_e "Very well."
        elif "no hand" in Girl.daily_history:
            ch_e "Oh, fine!"
        else:
            $ Girl.change_face("sexy", 1)
            $ Girl.change_stat("love", 90, 1)
            $ Girl.change_stat("inhibition", 50, 3)
            $ line = renpy.random.choice(["Oh, I suppose.",
                "I'll do it.",
                "Well, give it here.",
                "I suppose I could. . .",
                "Fine. . . [She gestures for you to come over].",
                "Ok, ok."])
            ch_e "[line]"
            $ line = 0
        $ Girl.change_stat("obedience", 20, 1)
        $ Girl.change_stat("obedience", 60, 1)
        $ Girl.change_stat("inhibition", 70, 2)
        jump Emma_HJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ Girl.change_face("angry")
        if "no hand" in Girl.recent_history:
            ch_e "You need to learn to take\"no\" for an answer, [Girl.Petname]."
        elif "no hand" in Girl.daily_history:
            ch_e "I told you \"no,\" [Girl.Petname]."
        elif Taboo and "tabno" in Girl.daily_history:
            ch_e "I told you, this is too public!"
        elif not Girl.Hand:
            $ Girl.change_face("bemused")
            ch_e "Are you sure though, [Girl.Petname]?. . ."
        else:
            $ Girl.change_face("bemused")
            ch_e "I'd rather not right now though."
        menu:
            extend ""
            "Sorry, never mind." if "no hand" in Girl.daily_history:
                $ Girl.change_face("bemused")
                ch_e "Quite alright."
                return
            "Maybe later?" if "no hand" not in Girl.daily_history:
                $ Girl.change_face("sexy")
                ch_e ". . ."
                ch_e "I couldn't rule it out. . ."
                $ Girl.change_stat("love", 80, 2)
                $ Girl.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ Girl.recent_history.append("tabno")
                    $ Girl.daily_history.append("tabno")
                $ Girl.recent_history.append("no hand")
                $ Girl.daily_history.append("no hand")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ Girl.change_face("sexy")
                    $ Girl.change_stat("obedience", 90, 2)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("inhibition", 70, 3)
                    $ Girl.change_stat("inhibition", 40, 2)
                    $ line = renpy.random.choice(["Oh, I suppose.",
                        "I'll do it.",
                        "Well, give it here.",
                        "I suppose I could. . .",
                        "Fine. . . [She gestures for you to come over].",
                        "Ok, ok."])
                    ch_e "[line]"
                    $ line = 0
                    jump Emma_HJ_Prep

            "Come on, get to work.":                                               # Pressured into it
                call forced_action(Girl, "handjob")

    #She refused all offers.
    $ Girl.ArmPose = 1
    if "no hand" in Girl.daily_history:
        $ Girl.change_face("angry", 1)
        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
    elif Girl.Forced:
        $ Girl.change_face("angry", 1)
        ch_e "Even that is asking too much."
        $ Girl.change_stat("lust", 200, 5)
        if Girl.love > 300:
                $ Girl.change_stat("love", 70, -2)
        $ Girl.change_stat("obedience", 50, -2)
        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ Girl.change_face("angry", 1)
        $ Girl.daily_history.append("tabno")
        ch_e "I couldn't possibly do that. . . here!"
        $ Girl.change_stat("lust", 200, 5)
        $ Girl.change_stat("obedience", 50, -3)
    elif Girl.Hand:
        $ Girl.change_face("sad")
        ch_e "I'd really rather not. . ."
    else:
        $ Girl.change_face("normal", 1)
        ch_e "No, I don't think so, [Girl.Petname]."
    $ Girl.recent_history.append("no hand")
    $ Girl.daily_history.append("no hand")
    $ temp_modifier = 0
    return


label Emma_HJ_Prep:
    if offhand_action == "hand":
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
    call Emma_HJ_Launch("L")

    if action_context == Girl:
            #Emma auto-starts
            $ action_context = 0
            if offhand_action == "jackin":
                "[Girl.name] brushes your hand aside and starts stroking your cock."
            else:
                "[Girl.name] draws her fingers across your cock, and begins to stroke it."
            menu:
                "What do you do?"
                "Nothing.":
                    $ Girl.change_stat("inhibition", 70, 3)
                    $ Girl.change_stat("inhibition", 30, 2)
                    "[Girl.name] continues her actions."
                "Praise her.":
                    $ Girl.change_face("sexy", 1)
                    $ Girl.change_stat("inhibition", 70, 3)
                    ch_p "Oooh, that's good, [Girl.Pet]."
                    $ Girl.nameCheck() #checks reaction to petname
                    "[Girl.name] continues her actions."
                    $ Girl.change_stat("love", 80, 1)
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ Girl.change_face("surprised")
                    $ Girl.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that for now, [Girl.Pet]."
                    $ Girl.nameCheck() #checks reaction to petname
                    "[Girl.name] puts it down."
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
    $ Girl.DrainWord("no hand")
    $ Girl.recent_history.append("hand")
    $ Girl.daily_history.append("hand")

label Emma_HJ_Cycle:
    while Round > 0:
        call Shift_Focus(Girl)
        call Emma_HJ_Launch
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
                                    "I also want to fondle her breasts." if offhand_action != "fondle breasts":
                                            if Girl.Action and MultiAction:
                                                $ offhand_action = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ Girl.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Shift primary action":
                                            if Girl.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                    if Girl.Action and MultiAction:
                                                                        $ action_context = "shift"
                                                                        call Emma_HJ_After
                                                                        call Emma_Blowjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(Girl,"tired")

                                                        "How about a titjob?":
                                                                    if Girl.Action and MultiAction:
                                                                        $ action_context = "shift"
                                                                        call Emma_HJ_After
                                                                        call Emma_Titjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(Girl,"tired")
                                                        "Never Mind":
                                                                jump Emma_HJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [Girl.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(Girl)
                                            "Asks [Girl.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                call Three_Change(Girl)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(Girl)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Emma_HJ_Cycle
                                            "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_HJ_Cycle
                                            "Never mind":
                                                        jump Emma_HJ_Cycle
                                    "Undress [Girl.name]":
                                            call Girl_Undress(Girl)
                                    "Clean up [Girl.name] (locked)" if not Girl.Spunk:
                                            pass
                                    "Clean up [Girl.name]" if Girl.Spunk:
                                            call Girl_Cleanup(Girl,"ask")
                                    "Never mind":
                                            jump Emma_HJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Emma_HJ_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Emma_HJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Emma_HJ_Reset
                                    $ line = 0
                                    jump Emma_HJ_After
        #End menu (if line)

        call Shift_Focus(Girl)
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
                                call Emma_HJ_Reset
                                return
                            $ Girl.change_stat("lust", 200, 5)
                            if 100 > Girl.lust >= 70 and Girl.OCount < 2 and Girl.SEXP >= 20:
                                $ Girl.recent_history.append("unsatisfied")
                                $ Girl.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Emma_HJ_After
                            $ line = "came"

                    if Girl.lust >= 100:
                            #If [Girl.name] can cum
                            call Girl_Cumming(Girl)
                            if action_context == "shift" or "angry" in Girl.recent_history:
                                jump Emma_HJ_After

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in Girl.recent_history:#And [Girl.name] is unsatisfied,
                                    "[Girl.name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Emma_HJ_After
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if counter == 20:
                    $ Girl.Brows = "angry"
                    ch_e "Hmm, I'm getting a bit of a cramp here."
                    menu:
                        ch_e "Mind if we take a break?"
                        "How about a BJ?" if Girl.Action and MultiAction:
                                $ action_context = "shift"
                                call Emma_HJ_After
                                call Emma_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ counter += 1
                                "[line]"
                                jump Emma_HJ_Cycle
                        "Let's try something else." if MultiAction:
                                $ line = 0
                                call Emma_HJ_Reset
                                $ action_context = "shift"
                                jump Emma_HJ_After
                        "No, get back down there.":
                                if ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "O"):
                                    $ Girl.change_stat("love", 200, -5)
                                    $ Girl.change_stat("obedience", 50, 3)
                                    $ Girl.change_stat("obedience", 80, 2)
                                    "She scowls but gets back to work."
                                else:
                                    $ Girl.change_face("angry", 1)
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_e "You know, I do have better things to do with my time than this."
                                    $ Girl.change_stat("love", 50, -3, 1)
                                    $ Girl.change_stat("love", 80, -4, 1)
                                    $ Girl.change_stat("obedience", 30, -1, 1)
                                    $ Girl.change_stat("obedience", 50, -1, 1)
                                    $ Girl.recent_history.append("angry")
                                    $ Girl.daily_history.append("angry")
                                    jump Emma_HJ_After
        elif counter == 10 and Girl.SEXP <= 100 and not ApprovalCheck(Girl, 1200, "LO"):
                    $ Girl.Brows = "confused"
                    ch_e "Are you certain you didn't have anything else in mind?"
        #End Count check

        call Escalation(Girl) #sees if she wants to escalate things

        if Round == 10:
            ch_e "It's about time for a break."
        elif Round == 5:
            ch_e "Ok, that's enough, for now. . ."

    #Round = 0 loop breaks
    $ Girl.change_face("bemused", 0)
    $ line = 0
    ch_e "Ok, seriously, I'm putting it down for a minute."

label Emma_HJ_After:
    $ Girl.change_face("sexy")

    $ Girl.Hand += 1
    $ Girl.Action -=1
    $ Girl.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ Girl.Addictionrate += 1
    $ Girl.change_stat("lust", 90, 5)

    call Partner_Like(Girl,1)

    if "Emma Handi-Queen" in Achievements:
            pass
    elif Girl.Hand >= 10:
            $ Girl.change_face("smile", 1)
            ch_e "I've apparently become the \"queen\" of handjobs as well."
            $ Achievements.append("Emma Handi-Queen")
            $Girl.SEXP += 5
    elif Girl.Hand == 1:
            $Girl.SEXP += 10
            if not Girl.Forced:
                $ Girl.Mouth = "smile"
                ch_e "What a lovely experience. . ."
            elif Player.Focus <= 20:
                $ Girl.Mouth = "sad"
                ch_e "Was that sufficient?"
    elif Girl.Hand == 5:
                ch_e "Please do call again. . ."

    $ temp_modifier = 0
    if action_context == "shift":
        ch_e "Very well, what did you want to do?"
    else:
        call Emma_HJ_Reset
    call Checkout
    return

## end Girl.Handjob //////////////////////////////////////////////////////////////////////




## Girl.Titjob //////////////////////////////////////////////////////////////////////
label Emma_Titjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(Girl)
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

    if "no titjob" in Girl.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no titjob" in Girl.recent_history else 0

    $ Approval = ApprovalCheck(Girl, 1200, TabM = 5) # 120, 135, 150, Taboo -200(320)

    if not Girl.Tit and "no titjob" not in Girl.recent_history:
        $ Girl.change_face("surprised", 1)
        $ Girl.Mouth = "kiss"
        ch_e "Hmm, are you sure you can handle that, [Girl.Petname]?"

    if not Girl.Tit and Approval:
        #First time dialog
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
        elif Girl.love >= (Girl.obedience + Girl.inhibition):
            $ Girl.change_face("sexy")
            $ Girl.Brows = "sad"
            $ Girl.Mouth = "smile"
            ch_e "I suppose you've earned something special. . ."
        elif Girl.obedience >= Girl.inhibition:
            $ Girl.change_face("normal")
            ch_e "If that's what you want. . ."
        elif Girl.Addict >= 50:
            $ Girl.change_face("manic", 1)
            ch_e "Hmmmm. . . ."
        else: # Uninhibited
            $ Girl.change_face("sad")
            $ Girl.Mouth = "smile"
            ch_e "Hmm, I was wondering when you'd ask. . ."

    elif Approval:
        #Second time+ dialog
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
            ch_e "You aren't getting used to this service, are you?"
        elif not Taboo and "tabno" in Girl.daily_history:
            ch_e "I suppose this is secluded enough. . ."
        elif "titjob" in Girl.recent_history:
            $ Girl.change_face("sexy", 1)
            ch_e "Oh! Back for more?"
            jump Emma_TJ_Prep
        elif "titjob" in Girl.daily_history:
            $ Girl.change_face("sexy", 1)
            $ line = renpy.random.choice(["Back again so soon?",
                "You're going to wear them out.",
                "Didn't get enough earlier?",
                "I'm still a bit sore from earlier."])
            ch_e "[line]"
        elif Girl.Tit < 3:
            $ Girl.change_face("sly", 1)
            ch_e "Hmm, another titjob?"
        else:
            $ Girl.change_face("sexy", 1)
            $ Girl.ArmPose = 2
            $ line = renpy.random.choice(["You want some of these? [jiggles her tits]",
                "So you'd like another titjob?",
                "A little. . . [bounces tits]?",
                "A little warm embrace?"])
            ch_e "[line]"
        $ line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 60, 1)
            ch_e "I suppose there are worst ways to get you off. . ."
        elif "no titjob" in Girl.daily_history:
            ch_e "Oh, very well then. . ."
        else:
            $ Girl.change_face("sexy", 1)
            $ Girl.change_stat("love", 90, 1)
            $ Girl.change_stat("inhibition", 50, 3)
            $ line = renpy.random.choice(["Well, sure, come over here.",
                "Oh, very well.",
                "Mmmmm.",
                "Fine, whip it out.",
                "Fine. . . [She drools a bit into her cleavage].",
                "Oh, all right."])
            ch_e "[line]"
            $ line = 0
        $ Girl.change_stat("obedience", 20, 1)
        $ Girl.change_stat("obedience", 70, 1)
        $ Girl.change_stat("inhibition", 80, 2)
        jump Emma_TJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ Girl.change_face("angry")
        if "no titjob" in Girl.recent_history:
            ch_e "I {i}just{/i} refused, [Girl.Petname]."
        elif Taboo and "tabno" in Girl.daily_history and "no titjob" in Girl.daily_history:
            ch_e "This is not an appropriate location for that. !"
        elif "no titjob" in Girl.daily_history:
            ch_e "I already refused, [Girl.Petname]."
        elif Taboo and "tabno" in Girl.daily_history:
            ch_e "This is not an appropriate place for that."
        else:
            $ Girl.change_face("bemused")
            ch_e "Perhaps later, [Girl.Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no titjob" in Girl.daily_history:
                $ Girl.change_face("bemused")
                ch_e "That's all right, [Girl.Petname]."
                return
            "Maybe later?" if "no titjob" not in Girl.daily_history:
                $ Girl.change_face("sexy")
                ch_e "Perhaps."
                $ Girl.change_stat("love", 80, 2)
                $ Girl.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ Girl.recent_history.append("tabno")
                    $ Girl.daily_history.append("tabno")
                $ Girl.recent_history.append("no titjob")
                $ Girl.daily_history.append("no titjob")
                return
            "I think this could be fun for both of us. . .":
                if Approval:
                    $ Girl.change_face("sexy")
                    $ Girl.change_stat("obedience", 80, 2)
                    $ Girl.change_stat("obedience", 40, 2)
                    $ Girl.change_stat("inhibition", 70, 3)
                    $ Girl.change_stat("inhibition", 40, 2)
                    $ line = renpy.random.choice(["Well, sure, come over here.",
                            "Oh, very well.",
                            "Mmmmm.",
                            "Fine, whip it out.",
                            "Fine. . . [She drools a bit into her cleavage].",
                            "Oh, all right."])
                    ch_e "[line]"
                    $ line = 0
                    jump Emma_TJ_Prep
                else:
                    $ Approval = ApprovalCheck(Girl, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)             Handy instead?
                    if Approval >= 2:
                        $ Girl.change_stat("inhibition", 80, 1)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.change_face("confused", 1)
                        if Girl.Blow:
                            ch_e "You seemed to enjoy blowjobs, would that work instead?"
                        else:
                            ch_e "Would you perhaps prefer a blowjob?"
                        menu:
                            extend ""
                            "Ok, get down there.":
                                $ Girl.change_stat("love", 80, 2)
                                $ Girl.change_stat("inhibition", 60, 1)
                                $ Girl.change_stat("obedience", 50, 1)
                                jump Emma_BJ_Prep
                            "Nah, it's all about dem titties.":
                                $ line = "no BJ"
                    if Approval:
                        $ Girl.change_stat("inhibition", 80, 1)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.change_face("confused", 1)
                        ch_e "Perhaps a handjob?"
                        menu:
                            ch_e "Perhaps a handjob?"
                            "Sure, that's fine.":
                                $ Girl.change_stat("love", 80, 2)
                                $ Girl.change_stat("inhibition", 60, 1)
                                $ Girl.change_stat("obedience", 50, 1)
                                jump Emma_HJ_Prep
                            "Seriously, titties." if line == "no BJ":
                                $ line = 0
                            "Nah, it's all about dem titties." if line != "no BJ":
                                pass
                    $ Girl.change_stat("love", 200, -2)
                    ch_e "Well, that's too bad."
                    $ Girl.change_stat("obedience", 70, 2)


            "Come on, let me fuck those titties, [Girl.Pet]":                                               # Pressured into it
                $ Girl.nameCheck() #checks reaction to petname
                $ Approval = ApprovalCheck(Girl, 700, "OI", TabM = 4) # 70, 85, 100, -160(230)
                if Approval > 1 or (Approval and Girl.Forced):
                    $ Girl.change_face("sad")
                    $ Girl.change_stat("love", 70, -5, 1)
                    $ Girl.change_stat("love", 200, -2)
                    ch_e
                    $ Girl.change_stat("obedience", 50, 4)
                    $ Girl.change_stat("inhibition", 80, 1)
                    $ Girl.change_stat("inhibition", 60, 3)
                    $ Girl.Forced = 1
                    jump Emma_TJ_Prep
                else:
                    $ Girl.change_stat("love", 200, -15)
                    $ Girl.recent_history.append("angry")
                    $ Girl.daily_history.append("angry")

    #She refused all offers.
    if "no titjob" in Girl.daily_history:
        $ Girl.change_face("angry", 1)
        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
    elif Girl.Forced:
        $ Girl.change_face("angry", 1)
        ch_e "I couldn't put you through that."
        $ Girl.change_stat("lust", 200, 5)
        if Girl.love > 300:
                $ Girl.change_stat("love", 70, -2)
        $ Girl.change_stat("obedience", 50, -2)
        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ Girl.change_face("angry", 1)
        $ Girl.daily_history.append("tabno")
        ch_e "Can you imagine the scandal? Here?"
        $ Girl.change_stat("lust", 200, 5)
        $ Girl.change_stat("obedience", 50, -3)
    elif Girl.Tit:
        $ Girl.change_face("sad")
        ch_e "I'm afraid you'll just have to remember the last time."
    else:
        $ Girl.change_face("normal", 1)
        ch_e "How about let's not, [Girl.Petname]."
    $ Girl.recent_history.append("no titjob")
    $ Girl.daily_history.append("no titjob")
    $ temp_modifier = 0
    return

label Emma_TJ_Prep:

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
    call Emma_TJ_Launch("L")

    if action_context == Girl:
            #Emma auto-starts
            $ action_context = 0
            call Emma_TJ_Launch("L")
            "[Girl.name] slides down and wraps her tits around your dick."
            menu:
                "What do you do?"
                "Nothing.":
                    $ Girl.change_stat("inhibition", 80, 3)
                    $ Girl.change_stat("inhibition", 40, 2)
                    "[Girl.name] starts to slide them up and down."
                "Praise her.":
                    $ Girl.change_face("sexy", 1)
                    $ Girl.change_stat("inhibition", 80, 3)
                    ch_p "Oh, that sounds like a good idea, [Girl.Pet]."
                    $ Girl.nameCheck() #checks reaction to petname
                    "[Girl.name] continues her actions."
                    $ Girl.change_stat("love", 85, 1)
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ Girl.change_face("confused")
                    $ Girl.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that for now, [Girl.Pet]."
                    $ Girl.nameCheck() #checks reaction to petname
                    "[Girl.name] lets it drop out from between her breasts."
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
    $ Girl.DrainWord("no titjob")
    $ Girl.recent_history.append("titjob")
    $ Girl.daily_history.append("titjob")


label Emma_TJ_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(Girl)
        call Emma_TJ_Launch
        $ Girl.lustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if action_speed:
                                    pass

                        "Start moving? . ." if action_speed == 0:
                                    $ action_speed = 1

                        "action_speed up. . ." if  action_speed == 1:
                                    $ action_speed = 2
                                    "You ask her to up the pace a bit."
                        "action_speed up. . . (locked)" if action_speed >= 2:
                                    pass

                        "Stop moving" if action_speed == 1 or action_speed == 3:
                                    $ action_speed = 0
                        "Slow Down. . ." if action_speed == 2:
                                    $ action_speed = 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not action_speed:
                                    pass

                        "Lick it" if action_speed != 3:
                                    $ action_speed = 3
                        "Lick it (locked)" if action_speed == 3:
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
                                    "I also want to fondle her breasts." if offhand_action != "fondle breasts":
                                            if Girl.Action and MultiAction:
                                                $ offhand_action = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ Girl.Action -= 1
                                            else:
                                                ch_e "Actually, could we wrap this up soon?"

                                    "Shift primary action":
                                            if Girl.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                if Girl.Action and MultiAction:
                                                                    $ action_context = "shift"
                                                                    call Emma_TJ_After
                                                                    call Emma_Blowjob
                                                                else:
                                                                    ch_e "Actually, could we wrap this up soon?"

                                                        "How about a handy?":
                                                                if Girl.Action and MultiAction:
                                                                    $ action_context = "shift"
                                                                    call Emma_BJ_After
                                                                    call Emma_Handjob
                                                                else:
                                                                    ch_e "Actually, could we wrap this up soon?"
                                                        "Never Mind":
                                                                jump Emma_TJ_Cycle
                                            else:
                                                ch_e "Actually, could we wrap this up soon?"

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [Girl.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(Girl)
                                            "Asks [Girl.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(Girl)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(Girl)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Emma_TJ_Cycle
                                            "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_TJ_Cycle
                                            "Never mind":
                                                        jump Emma_TJ_Cycle
                                    "Undress [Girl.name]":
                                            call Girl_Undress(Girl)
                                    "Clean up [Girl.name] (locked)" if not Girl.Spunk:
                                            pass
                                    "Clean up [Girl.name]" if Girl.Spunk:
                                            call Girl_Cleanup(Girl,"ask")
                                    "Never mind":
                                            jump Emma_TJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Emma_TJ_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Emma_TJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Emma_TJ_Reset
                                    $ line = 0
                                    jump Emma_TJ_After
        #End menu (if line)

        call Shift_Focus(Girl)
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
                                call Emma_TJ_Reset
                                return
                            $ Girl.change_stat("lust", 200, 5)
                            if 100 > Girl.lust >= 70 and Girl.OCount < 2 and Girl.SEXP >= 20:
                                $ Girl.recent_history.append("unsatisfied")
                                $ Girl.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Emma_TJ_After
                            $ line = "came"

                    if Girl.lust >= 100:
                            #If [Girl.name] can cum
                            call Girl_Cumming(Girl)
                            if action_context == "shift" or "angry" in Girl.recent_history:
                                jump Emma_TJ_After

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in Girl.recent_history:#And [Girl.name] is unsatisfied,
                                "[Girl.name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Emma_TJ_After
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Girl.SEXP >= 100 or ApprovalCheck(Girl, 1200, "LO"):
            pass
        elif counter == (5 + Girl.Tit):
                    $ Girl.Brows = "confused"
                    ch_e "Are you getting close here? I'm getting a bit sore."
        elif counter == (10 + Girl.Tit):
                    $ Girl.Brows = "angry"
                    menu:
                        ch_e "I'm getting a bit worn out, could we settle this some other way?"
                        "How about a BJ?" if Girl.Action and MultiAction:
                                $ action_context = "shift"
                                call Emma_TJ_After
                                call Emma_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                jump Emma_TJ_Cycle
                        "Let's try something else." if MultiAction:
                                $ line = 0
                                call Emma_TJ_Reset
                                $ action_context = "shift"
                                jump Emma_TJ_After
                        "No, get back down there.":
                                if ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "O"):
                                    $ Girl.change_stat("love", 200, -5)
                                    $ Girl.change_stat("obedience", 50, 3)
                                    $ Girl.change_stat("obedience", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    $ Girl.change_face("angry", 1)
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_e "Then I suppose you can handle this yourself."
                                    $ Girl.change_stat("love", 50, -3, 1)
                                    $ Girl.change_stat("love", 80, -4, 1)
                                    $ Girl.change_stat("obedience", 30, -1, 1)
                                    $ Girl.change_stat("obedience", 50, -1, 1)
                                    $ Girl.recent_history.append("angry")
                                    $ Girl.daily_history.append("angry")
                                    jump Emma_TJ_After
        #End Count check

        call Escalation(Girl) #sees if she wants to escalate things

        if Round == 10:
            ch_e "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ Girl.change_face("bemused", 0)
    $ line = 0
    ch_e "All right, [Girl.Petname], that's plenty for now."

label Emma_TJ_After:
    $ Girl.change_face("sexy")

    $ Girl.Tit += 1
    $ Girl.Action -=1
    $ Girl.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ Girl.Addictionrate += 1

    if Partner == "Kitty":
        call Partner_Like(Girl,4,2)
    else:
        call Partner_Like(Girl,3)

    if Girl.Tit > 5:
            pass
    elif Girl.Tit == 1:
        $Girl.SEXP += 12
        if Girl.love >= 500:
            $ Girl.Mouth = "smile"
            ch_e "Mmm, was that as good for you as it was for me?"
        elif Player.Focus <= 20:
            $ Girl.Mouth = "sad"
            ch_e "I hope that lived up to expectations."
    elif Girl.Tit == 5:
            ch_e "You certainly get a lot of milage out of these."


    $ temp_modifier = 0
    if action_context == "shift":
            ch_e "Mmm, so what else did you have in mind?"
    else:
            call Emma_TJ_Reset
    call Checkout
    return

## end Girl.Titjob //////////////////////////////////////////////////////////////////////


# Girl.Blowjob //////////////////////////////////////////////////////////////////////

label Emma_Blowjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(Girl)
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

    if "no blow" in Girl.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no blow" in Girl.recent_history else 0

    $ Approval = ApprovalCheck(Girl, 1300, TabM = 4) # 130, 145, 160, Taboo -160(290)

    if not Girl.Blow and "no blow" not in Girl.recent_history:
        $ Girl.change_face("sly")
        ch_e "So you'd like me to suck you off?"

    if not Girl.Blow and Approval:                                                 #First time dialog
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
        elif Girl.love >= (Girl.obedience + Girl.inhibition):
            $ Girl.change_face("sexy")
            $ Girl.Brows = "sad"
            $ Girl.Mouth = "smile"
            ch_e "I am curious if it tastes as good as it looks. . ."
        elif Girl.obedience >= Girl.inhibition:
            $ Girl.change_face("normal")
            ch_e "If that's what you want. . ."
        elif Girl.Addict >= 50:
            $ Girl.change_face("manic", 1)
            ch_e "I don't know if I could wait. . ."
        else: # Uninhibited
            $ Girl.change_face("sad")
            $ Girl.Mouth = "smile"
            ch_e "I suppose. . ."
    elif Approval:                                                                       #Second time+ dialog
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
            ch_e "Ugh, that again?"
        elif not Taboo and "tabno" in Girl.daily_history:
            ch_e "Ok, I suppose this is secluded enough. . ."
        elif "blow" in Girl.recent_history:
            $ Girl.change_face("sexy", 1)
            ch_e "Mmm, again? [[yawns]"
            jump Emma_BJ_Prep
        elif "blow" in Girl.daily_history:
            $ Girl.change_face("sexy", 1)
            $ line = renpy.random.choice(["Back so soon?",
                "Let me get some saliva going.",
                "Didn't get enough earlier?",
                "My jaw's still sore from our prior engagement.",
                "My jaw's still a bit sore from earlier."])
            ch_e "[line]"
        elif Girl.Blow < 3:
            $ Girl.change_face("sexy", 1)
            $ Girl.Brows = "confused"
            $ Girl.Mouth = "kiss"
            ch_e "Another blowjob?"
        else:
            $ Girl.change_face("sexy", 1)
            $ Girl.ArmPose = 2
            $ line = renpy.random.choice(["You want me to [mimes blowing]?",
                "So you want another blowjob?",
                "You want me to suck you off?",
                "Are you asking if I'm hungry?"])
            ch_e "[line]"
        $ line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 60, 1)
            ch_e "Fine."
        elif "no blow" in Girl.daily_history:
            ch_e "Fine, I suppose you've earned it. . ."
        else:
            $ Girl.change_face("sexy", 1)
            $ Girl.change_stat("love", 90, 1)
            $ Girl.change_stat("inhibition", 50, 3)
            $ line = renpy.random.choice(["Well, ok.",
                "Well. . . ok.",
                "Mmmm.",
                "Sure, let me have it.",
                "Mmmm. . . [She licks her lips].",
                "Ok, fine."])
            ch_e "[line]"
            $ line = 0
        $ Girl.change_stat("obedience", 20, 1)
        $ Girl.change_stat("obedience", 70, 1)
        $ Girl.change_stat("inhibition", 80, 2)
        jump Emma_BJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ Girl.change_face("angry")
        if "no blow" in Girl.recent_history:
            ch_e "I believe I just told you, \"no.\""
        elif Taboo and "tabno" in Girl.daily_history and "no blow" in Girl.daily_history:
            ch_e "I told you, this is too public!"
        elif "no blow" in Girl.daily_history:
            ch_e "I told you \"no,\" [Girl.Petname]."
        elif Taboo and "tabno" in Girl.daily_history:
            ch_e "I told you this is too public!"
        elif not Girl.Blow:
            $ Girl.change_face("bemused")
            ch_e "I'm not sure you're up to my usual tastes, [Girl.Petname]. . ."
        else:
            $ Girl.change_face("bemused")
            ch_e "Perhaps later, [Girl.Petname]."
        menu:
            extend ""
            "Sorry, never mind." if "no blow" in Girl.daily_history:
                $ Girl.change_face("bemused")
                ch_e "No harm done, [Girl.Petname]."
                return
            "Maybe later?" if "no blow" not in Girl.daily_history:
                $ Girl.change_face("sexy")
                ch_e "I wouldn't rule it out, [Girl.Petname]."
                $ Girl.change_stat("love", 80, 2)
                $ Girl.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ Girl.recent_history.append("tabno")
                    $ Girl.daily_history.append("tabno")
                $ Girl.recent_history.append("no blow")
                $ Girl.daily_history.append("no blow")
                return
            "Come on, please?":
                if Approval:
                    $ Girl.change_face("sexy")
                    $ Girl.change_stat("obedience", 90, 2)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("inhibition", 70, 3)
                    $ Girl.change_stat("inhibition", 40, 2)
                    $ line = renpy.random.choice(["Well, I suppose.",
                        "Well. . . ok.",
                        "I could perhaps give it a try.",
                        "I suppose I could. . .",
                        "Fine. . . [She licks her lips].",
                        "Hmph, ok, fine."])
                    ch_e "[line]"
                    $ line = 0
                    jump Emma_BJ_Prep
                else:
                    if ApprovalCheck(Girl, 1100, TabM = 3): # 110, 125, 140, Taboo -120(230)             Handy instead?
                        $ Girl.change_stat("inhibition", 80, 1)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.change_face("confused", 1)
                        $ Girl.ArmPose = 2
                        if Girl.Hand:
                            ch_e "I could just stroke you off, perhaps?"
                        else:
                            ch_e "Would my hand be an adequate substitute?"
                        menu:
                            extend ""
                            "Sure, that's fine.":
                                $ Girl.change_stat("love", 80, 2)
                                $ Girl.change_stat("inhibition", 60, 1)
                                $ Girl.change_stat("obedience", 50, 1)
                                jump Emma_HJ_Prep
                            "Nah, if it's not your mouth, forget it.":
                                $ Girl.change_stat("love", 200, -2)
                                $ Girl.ArmPose = 1
                                ch_e "Pitty."
                                $ Girl.change_stat("obedience", 70, 2)


            "Suck it, [Girl.Pet]":                                               # Pressured into it
                $ Girl.nameCheck() #checks reaction to petname
                $ Approval = ApprovalCheck(Girl, 750, "OI", TabM = 3) # 75, 90, 105, -120(195)
                if Approval > 1 or (Approval and Girl.Forced):
                    $ Girl.change_face("sad")
                    $ Girl.change_stat("love", 70, -5, 1)
                    $ Girl.change_stat("love", 200, -2)
                    ch_e
                    $ Girl.change_stat("obedience", 50, 4)
                    $ Girl.change_stat("inhibition", 80, 1)
                    $ Girl.change_stat("inhibition", 60, 3)
                    $ Girl.Forced = 1
                    jump Emma_BJ_Prep
                else:
                    $ Girl.change_stat("love", 200, -15)
                    $ Girl.recent_history.append("angry")
                    $ Girl.daily_history.append("angry")

    #She refused all offers.
    if "no blow" in Girl.daily_history:
        $ Girl.change_face("angry", 1)
        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
    elif Girl.Forced:
        $ Girl.change_face("angry", 1)
        ch_e "You go too far!"
        $ Girl.change_stat("lust", 200, 5)
        if Girl.love > 300:
                $ Girl.change_stat("love", 70, -2)
        $ Girl.change_stat("obedience", 50, -2)
        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
        $ Girl.recent_history.append("no blow")
        $ Girl.daily_history.append("no blow")
        return
    elif Taboo:                             # she refuses and this is too public a place for her
        $ Girl.change_face("angry", 1)
        $ Girl.daily_history.append("tabno")
        ch_e "This is way too exposed!"
        $ Girl.change_stat("lust", 200, 5)
        $ Girl.change_stat("obedience", 50, -3)
        return
    elif Girl.Blow:
        $ Girl.change_face("sad")
        ch_e "I'm just not in the mood, [Girl.Petname]."
    else:
        $ Girl.change_face("normal", 1)
        ch_e "I don't think I will."
    $ Girl.recent_history.append("no blow")
    $ Girl.daily_history.append("no blow")
    $ temp_modifier = 0
    return


label Emma_BJ_Prep:
    if renpy.showing("Emma_HJ_Animation"):
        hide Emma_HJ_Animation with easeoutbottom
    if Taboo:
        $ Girl.inhibition += int(Taboo/10)
        $ Girl.lust += int(Taboo/5)

    $ Girl.change_face("sexy")
    if Girl.Forced:
        $ Girl.change_face("sad")

    call Seen_First_Peen(Girl,Partner,React=action_context)
    call Emma_BJ_Launch("L")

    if action_context == Girl:
            #Emma auto-starts
            $ action_context = 0
            "[Girl.name] slides down and places your cock against her lips."
            menu:
                "What do you do?"
                "Nothing.":
                    $ Girl.change_stat("inhibition", 80, 3)
                    $ Girl.change_stat("inhibition", 40, 2)
                    "[Girl.name] continues licking at it."
                "Praise her.":
                    $ Girl.change_face("sexy", 1)
                    $ Girl.change_stat("inhibition", 80, 3)
                    ch_p "Hmmm, keep doing that, [Girl.Pet]."
                    $ Girl.nameCheck() #checks reaction to petname
                    "[Girl.name] continues her actions."
                    $ Girl.change_stat("love", 85, 1)
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ Girl.change_face("surprised")
                    $ Girl.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that for now, [Girl.Pet]."
                    $ Girl.nameCheck() #checks reaction to petname
                    "[Girl.name] puts it down."
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
    $ Girl.DrainWord("no blow")
    $ Girl.recent_history.append("blow")
    $ Girl.daily_history.append("blow")

label Emma_BJ_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(Girl)
        call Emma_BJ_Launch
        $ Girl.lustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if action_speed:
                                    pass

                        "Lick it. . ." if action_speed != 1:
                                $ action_speed = 1
                        "Lick it. . . (locked)" if action_speed == 1:
                                pass

                        "Just the head. . ." if action_speed != 2:
                            $ action_speed = 2
                        "Just the head. . . (locked)" if action_speed == 2:
                                pass

                        "Suck on it." if action_speed != 3:
                                $ action_speed = 3
                                if offhand_action == "jackin":
                                    "She dips her head a bit lower, and you move your hand out of the way."

                        "Suck on it. (locked)" if action_speed == 3:
                                pass

                        "Take it deeper." if action_speed != 4:
                                if "pushed" not in Girl.recent_history and Girl.Blow < 5:
                                    $ Girl.change_stat("love", 80, -(20-(2*Girl.Blow)))
                                    $ Girl.change_stat("obedience", 80, (30-(3*Girl.Blow)))
                                    $ Girl.recent_history.append("pushed")
                                if offhand_action == "jackin" and action_speed != 3:
                                    "She takes it to the root, and you move your hand out of the way."
                                $ action_speed = 4
                        "Take it deeper. (locked)" if action_speed == 4:
                                pass

                        "Set your own pace. . .":
                                "[Girl.name] hums contentedly."
                                if "setpace" not in Girl.recent_history:
                                    $ Girl.change_stat("love", 80, 2)
                                $ D20 = renpy.random.randint(1, 20)
                                if Girl.Blow < 5:
                                    $ D20 -= 10
                                elif Girl.Blow < 10:
                                    $ D20 -= 5

                                if D20 > 15:
                                    $ action_speed = 4
                                    if "setpace" not in Girl.recent_history:
                                        $ Girl.change_stat("inhibition", 80, 3)
                                elif D20 > 10:
                                    $ action_speed = 3
                                elif D20 > 5:
                                    $ action_speed = 2
                                else:
                                    $ action_speed = 1
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
                                    "I also want to fondle her breasts." if offhand_action != "fondle breasts":
                                            if Girl.Action and MultiAction:
                                                $ offhand_action = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ Girl.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Shift primary action":
                                            if Girl.Action and MultiAction:
                                                    menu:
                                                        "How about a handy?":
                                                                if Girl.Action and MultiAction:
                                                                    $ action_context = "shift"
                                                                    call Emma_BJ_After
                                                                    call Emma_Handjob
                                                                else:
                                                                    ch_e "I'm kinda tired, could we just wrap this up. . ."
                                                        "How about a titjob?":
                                                                if Girl.Action and MultiAction:
                                                                    $ action_context = "shift"
                                                                    call Emma_BJ_After
                                                                    call Emma_Titjob
                                                                else:
                                                                    ch_e "I'm kinda tired, could we just wrap this up. . ."
                                                        "Never Mind":
                                                                jump Emma_BJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [Girl.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(Girl)
                                            "Asks [Girl.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(Girl)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(Girl)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Emma_BJ_Cycle
                                            "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_BJ_Cycle
                                            "Never mind":
                                                        jump Emma_BJ_Cycle
                                    "Undress [Girl.name]":
                                            call Girl_Undress(Girl)
                                    "Clean up [Girl.name] (locked)" if not Girl.Spunk:
                                            pass
                                    "Clean up [Girl.name]" if Girl.Spunk:
                                            call Girl_Cleanup(Girl,"ask")
                                    "Never mind":
                                            jump Emma_BJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Emma_BJ_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Emma_BJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Emma_BJ_Reset
                                    $ line = 0
                                    jump Emma_BJ_After
        #End menu (if line)

        call Shift_Focus(Girl)
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
                                call Emma_BJ_Reset
                                return
                            $ Girl.change_stat("lust", 200, 5)
                            if 100 > Girl.lust >= 70 and Girl.OCount < 2 and Girl.SEXP >= 20:
                                $ Girl.recent_history.append("unsatisfied")
                                $ Girl.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Emma_BJ_After
                            $ line = "came"

                    if Girl.lust >= 100:
                            #If [Girl.name] can cum
                            call Girl_Cumming(Girl)
                            if action_context == "shift" or "angry" in Girl.recent_history:
                                jump Emma_BJ_After

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in Girl.recent_history:#And [Girl.name] is unsatisfied,
                                    "[Girl.name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Emma_BJ_After
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if Girl.SEXP >= 100 or ApprovalCheck(Girl, 1200, "LO"):
            pass
        elif counter == (15 + Girl.Blow):
                $ Girl.Brows = "angry"
                menu:
                    ch_e "I'm getting a bit worn out here, could we do something else?"
                    "How about a Handy?" if Girl.Action and MultiAction:
                            $ action_context = "shift"
                            call Emma_BJ_After
                            call Emma_Handjob
                            return
                    "Finish up." if Player.FocusX:
                            "You release your concentration. . ."
                            $ Player.FocusX = 0
                            $ Player.Focus += 15
                            $ counter += 1
                            "[line]."
                            jump Emma_BJ_Cycle
                    "Let's try something else." if MultiAction:
                            $ line = 0
                            call Emma_BJ_Reset
                            $ action_context = "shift"
                            jump Emma_BJ_After
                    "No, get back down there.":
                            if ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "O"):
                                $ Girl.change_stat("love", 200, -5)
                                $ Girl.change_stat("obedience", 50, 3)
                                $ Girl.change_stat("obedience", 80, 2)
                                "She scowls but gets back to work."
                            else:
                                $ Girl.change_face("angry", 1)
                                "She scowls at you, drops you cock and pulls back."
                                ch_e "Well then."
                                $ Girl.change_stat("love", 50, -3, 1)
                                $ Girl.change_stat("love", 80, -4, 1)
                                $ Girl.change_stat("obedience", 30, -1, 1)
                                $ Girl.change_stat("obedience", 50, -1, 1)
                                $ Girl.recent_history.append("angry")
                                $ Girl.daily_history.append("angry")
                                jump Emma_BJ_After
        elif counter == (10 + Girl.Blow) and Girl.SEXP <= 100 and not ApprovalCheck(Girl, 1200, "LO"):
                    $ Girl.Brows = "confused"
                    ch_e "Are you about done? I'm a little tired of this."
        #End Count check

        call Escalation(Girl) #sees if she wants to escalate things

        if Round == 10:
            ch_e "It's getting a bit late. . ."
        elif Round == 5:
            ch_e "Do you mind if we take a break?"

    #Round = 0 loop breaks
    $ Girl.change_face("bemused", 0)
    $ line = 0
    ch_e "Ok, I need to rest my jaw for a minute. . ."

label Emma_BJ_After:
    $ Girl.change_face("sexy")

    $ Girl.Blow += 1
    $ Girl.Action -=1
    $ Girl.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ Girl.Addictionrate += 1

    call Partner_Like(Girl,2)

    if "Emma Jobber" in Achievements:
        pass
    elif Girl.Blow >= 10:
        $ Girl.change_face("smile", 1)
        ch_e "You taste positively intoxicating, [Girl.Petname]."
        $ Achievements.append("Emma Jobber")
        $Girl.SEXP += 5
    elif action_context == "shift":
        pass
    elif Girl.Blow == 1:
            $Girl.SEXP += 15
            if Girl.love >= 500:
                $ Girl.Mouth = "smile"
                ch_e "Hmm, better than I'd imagined. . ."
            elif Player.Focus <= 20:
                $ Girl.Mouth = "sad"
                ch_e "Was it all you dreamed of?"
    elif Girl.Blow == 5:
        ch_e "Best you've had, I'm sure."
        menu:
            "[[nod]":
                $ Girl.change_face("smile", 1)
                $ Girl.change_stat("love", 90, 10)
                $ Girl.change_stat("obedience", 80, 5)
                $ Girl.change_stat("inhibition", 90, 10)
            "[[shake head \"no\"]":
                if ApprovalCheck(Girl, 500, "O"):
                    $ Girl.change_face("sad", 2)
                    $ Girl.change_stat("love", 200, -5)
                else:
                    $ Girl.change_face("angry", 2)
                    $ Girl.change_stat("love", 200, -30)
                $ Girl.change_stat("obedience", 80, 20)
                ch_e ". . ."
                $ Girl.change_face("sad", 1)

    $ temp_modifier = 0
    if action_context != "shift":
        call Emma_BJ_Reset
    call Checkout
    return



# end Girl.Blowjob                                 //////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy
label Emma_Dildo_Check:
    if "dildo" in Player.Inventory:
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in Girl.Inventory:
        "You ask [Girl.name] to get out her favorite Dildo."
    else:
        "You don't have one of those on you."
        return 0
    return 1

label Emma_Dildo_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(Girl)
    call Emma_Dildo_Check
    if not _return:
        return

    if Girl.DildoP: #You've done it before
        $ temp_modifier += 15
    if Girl.PantsNum() >= 6: # she's got pants on.
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

    if "no dildo" in Girl.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no dildo" in Girl.recent_history else 0

    $ Approval = ApprovalCheck(Girl, 1250, TabM = 4) # 125, 140, 155, Taboo -160(335)

    if action_context == Girl:                                                                  #Emma auto-starts
                if Approval > 2:                                                      # fix, add emma auto stuff here
                    if Girl.wearing_skirt:
                        "[Girl.name] grabs her dildo, hiking up her skirt as she does."
                        $ Girl.Upskirt = 1
                    elif Girl.PantsNum() > 6:
                        "[Girl.name] grabs her dildo, pulling down her pants as she does."
                        $ Girl.Legs = 0
                    else:
                        "[Girl.name] grabs her dildo, rubbing is suggestively against her crotch."
                    $ Girl.SeenPanties = 1
                    "She slides the tip along her pussy and seems to want you to insert it."
                    menu:
                        "What do you do?"
                        "Nothing.":
                            $ Girl.change_stat("inhibition", 80, 3)
                            $ Girl.change_stat("inhibition", 50, 2)
                            "[Girl.name] slides it in."
                        "Go for it.":
                            $ Girl.change_face("sexy", 1)
                            $ Girl.change_stat("inhibition", 80, 3)
                            ch_p "Oh yeah, [Girl.Pet], let's do this."
                            $ Girl.nameCheck() #checks reaction to petname
                            "You grab the dildo and slide it in."
                            $ Girl.change_stat("love", 85, 1)
                            $ Girl.change_stat("obedience", 90, 1)
                            $ Girl.change_stat("obedience", 50, 2)
                        "Ask her to stop.":
                            $ Girl.change_face("surprised")
                            $ Girl.change_stat("inhibition", 70, 1)
                            ch_p "Let's not do that right now, [Girl.Pet]."
                            $ Girl.nameCheck() #checks reaction to petname
                            "[Girl.name] sets the dildo down."
                            $ Girl.OutfitChange()
                            $ Girl.change_stat("obedience", 90, 1)
                            $ Girl.change_stat("obedience", 50, 1)
                            $ Girl.change_stat("obedience", 30, 2)
                            return
                    jump Emma_DP_Prep
                else:
                    $ temp_modifier = 0                               # fix, add emma auto stuff here
                    $ offhand_action = 0
                return

    if action_context == "auto":
                "You rub the dildo across her body, and along her moist slit."
                $ Girl.change_face("surprised", 1)

                if (Girl.DildoP and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
                    "[Girl.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                    $ Girl.change_face("sexy")
                    $ Girl.change_stat("obedience", 70, 3)
                    $ Girl.change_stat("inhibition", 50, 3)
                    $ Girl.change_stat("inhibition", 70, 1)
                    ch_e "Hmm, [Girl.Petname], toys!"
                    jump Emma_DP_Prep
                else:                                                                                                            #she's questioning it
                    $ Girl.Brows = "angry"
                    menu:
                        ch_e "Excuse yourself, what are you planning to do with that?!"
                        "Sorry, sorry! Never mind.":
                            if Approval:
                                $ Girl.change_face("sexy", 1)
                                $ Girl.change_stat("obedience", 70, 3)
                                $ Girl.change_stat("inhibition", 50, 3)
                                $ Girl.change_stat("inhibition", 70, 1)
                                ch_e "Well, now that you mention it. . ."
                                jump Emma_DP_Prep
                            "You pull back before you really get it in."
                            $ Girl.change_face("bemused", 1)
                            if Girl.DildoP:
                                ch_e "Well, [Girl.Petname], maybe warn me next time?"
                            else:
                                ch_e "Well, [Girl.Petname], that's a little much. . . for now . . ."
                        "Just playing with my favorite toys.":
                            $ Girl.change_stat("love", 80, -10, 1)
                            $ Girl.change_stat("love", 200, -10)
                            "You press it inside some more."
                            $ Girl.change_stat("obedience", 70, 3)
                            $ Girl.change_stat("inhibition", 50, 3)
                            if not ApprovalCheck(Girl, 700, "O", TabM=1): #Checks if obedience is 700+
                                $ Girl.change_face("angry")
                                "[Girl.name] shoves you away and slaps you in the face."
                                ch_e "Ask nicely before trying anything like that!"
                                $ Girl.change_stat("love", 50, -10, 1)
                                $ Girl.change_stat("obedience", 50, 3)
                                $ renpy.pop_call()
                                if action_context:
                                    $ renpy.pop_call()
                                if renpy.showing("Emma_SexSprite"):
                                    call Emma_Sex_Reset
                                $ Girl.recent_history.append("angry")
                                $ Girl.daily_history.append("angry")
                            else:
                                $ Girl.change_face("sad")
                                "[Girl.name] doesn't seem to be into this, you're lucky she's so obedient."
                                jump Emma_DP_Prep
                return
    #end Auto

    if not Girl.DildoP:
            #first time
            $ Girl.change_face("surprised", 1)
            $ Girl.Mouth = "kiss"
            ch_e "Hmmm, so you'd like to try out some toys?"
            if Girl.Forced:
                $ Girl.change_face("sad")
                ch_e "I suppose there are worst things you could ask for."

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
                ch_e "I've had a reasonable amount of experience with these, you know. . ."
            elif Girl.obedience >= Girl.inhibition:
                $ Girl.change_face("normal")
                ch_e "If that's what you want, [Girl.Petname]. . ."
            else: # Uninhibited
                $ Girl.change_face("sad")
                $ Girl.Mouth = "smile"
                ch_e "I guess it could be fun with a partner. . ."

    elif Approval:
            #Second time+ dialog
            if Girl.Forced:
                $ Girl.change_face("sad")
                $ Girl.change_stat("love", 70, -3, 1)
                $ Girl.change_stat("love", 20, -2, 1)
                ch_e "The toys again?"
            elif not Taboo and "tabno" in Girl.daily_history:
                ch_e "Well, at least you got us some privacy this time. . ."
            elif "dildo pussy" in Girl.recent_history:
                $ Girl.change_face("sexy", 1)
                ch_e "Mmm, again? Ok, let's get to it."
                jump Emma_DP_Prep
            elif "dildo pussy" in Girl.daily_history:
                $ Girl.change_face("sexy", 1)
                $ line = renpy.random.choice(["Breaking out the toys again?",
                    "Didn't get enough earlier?",
                    "You're going to wear me out."])
                ch_e "[line]"
            elif Girl.DildoP < 3:
                $ Girl.change_face("sexy", 1)
                $ Girl.Brows = "confused"
                $ Girl.Mouth = "kiss"
                ch_e "You want to stick it in my pussy again?"
            else:
                $ Girl.change_face("sexy", 1)
                $ Girl.ArmPose = 2
                $ line = renpy.random.choice(["You want some of this action?",
                    "So you'd like another go?",
                    "You want to stick it in my pussy again?",
                    "You want me ta lube up your toy?"])
                ch_e "[line]"
                $ line = 0

    if Approval >= 2:
            #She's into it. . .
            if Girl.Forced:
                $ Girl.change_face("sad")
                $ Girl.change_stat("obedience", 90, 1)
                $ Girl.change_stat("inhibition", 60, 1)
                ch_e "Ok, fine."
            else:
                $ Girl.change_face("sexy", 1)
                $ Girl.change_stat("love", 90, 1)
                $ Girl.change_stat("inhibition", 50, 3)
                $ line = renpy.random.choice(["Well, sure, stick it in.",
                    "Well. . . ok.",
                    "Sure!",
                    "I guess I could. . . stick it in.",
                    "Delightful.",
                    "Hmm, ok, ok."])
                ch_e "[line]"
                $ line = 0
            $ Girl.change_stat("obedience", 20, 1)
            $ Girl.change_stat("obedience", 60, 1)
            $ Girl.change_stat("inhibition", 70, 2)
            jump Emma_DP_Prep

    else:
            #She's not into it, but maybe. . .
            $ Girl.change_face("angry")
            if "no dildo" in Girl.recent_history:
                ch_e "What part of \"no,\" did you not get, [Girl.Petname]?"
            elif Taboo and "tabno" in Girl.daily_history and "no dildo" in Girl.daily_history:
                ch_e "Stop showing that thing around in public!"
            elif "no dildo" in Girl.daily_history:
                ch_e "I already told you \"no,\" [Girl.Petname]."
            elif Taboo and "tabno" in Girl.daily_history:
                ch_e "Stop showing that thing around in public!"
            elif not Girl.DildoP:
                $ Girl.change_face("bemused")
                ch_e "I'm a bit past toys, [Girl.Petname]. . ."
            else:
                $ Girl.change_face("bemused")
                ch_e "We don't need any toys, do we, [Girl.Petname]?"
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in Girl.daily_history:
                    $ Girl.change_face("bemused")
                    ch_e "I thought as much, [Girl.Petname]."
                    return
                "Maybe later?" if "no dildo" not in Girl.daily_history:
                    $ Girl.change_face("sexy")
                    ch_e "Maybe I'll practice on my own time, [Girl.Petname]."
                    $ Girl.change_stat("love", 80, 2)
                    $ Girl.change_stat("inhibition", 70, 2)
                    if Taboo:
                        $ Girl.recent_history.append("tabno")
                        $ Girl.daily_history.append("tabno")
                    $ Girl.recent_history.append("no dildo")
                    $ Girl.daily_history.append("no dildo")
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
                            "You make a compelling argument."])
                        ch_e "[line]"
                        $ line = 0
                        jump Emma_DP_Prep
                    else:
                        pass

                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck(Girl, 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                    if Approval > 1 or (Approval and Girl.Forced):
                        $ Girl.change_face("sad")
                        $ Girl.change_stat("love", 70, -5, 1)
                        $ Girl.change_stat("love", 200, -5)
                        ch_e
                        $ Girl.change_stat("obedience", 80, 4)
                        $ Girl.change_stat("inhibition", 80, 1)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.Forced = 1
                        jump Emma_DP_Prep
                    else:
                        $ Girl.change_stat("love", 200, -20)
                        $ Girl.recent_history.append("angry")
                        $ Girl.daily_history.append("angry")

    #She refused all offers.
    $ Girl.ArmPose = 1
    if "no dildo" in Girl.daily_history:
            $ Girl.recent_history.append("angry")
            $ Girl.daily_history.append("angry")
    elif Girl.Forced:
            $ Girl.change_face("angry", 1)
            ch_e "I'm not going to let you use that on me."
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
            ch_e "Not here!"
            $ Girl.change_stat("lust", 200, 5)
            $ Girl.change_stat("obedience", 50, -3)
    elif Girl.DildoP:
            $ Girl.change_face("sad")
            ch_e "Sorry, you can keep your toys to yourself."
    else:
            $ Girl.change_face("normal", 1)
            ch_e "No way."
    $ Girl.recent_history.append("no dildo")
    $ Girl.daily_history.append("no dildo")
    $ temp_modifier = 0
    return

label Emma_DP_Prep: #Animation set-up
    if offhand_action == "dildo pussy":
        return

    if not Girl.Forced and action_context != "auto":
        $ temp_modifier = 15 if Girl.PantsNum() > 6 else 0
        call Bottoms_Off(Girl)
        if "angry" in Girl.recent_history:
            return

    $ temp_modifier = 0
    call Emma_Pussy_Launch("dildo pussy")
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
    $ Girl.DrainWord("no dildo")
    $ Girl.recent_history.append("dildo pussy")
    $ Girl.daily_history.append("dildo pussy")

label Emma_DP_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(Girl)
        call Emma_Pussy_Launch("dildo pussy")
        $ Girl.lustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                call Slap_Ass(Girl)
                                jump Emma_DP_Cycle

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
                                            if Girl.Action and MultiAction:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ Girl.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Shift primary action":
                                            if Girl.Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in her ass.":
                                                                $ action_context = "shift"
                                                                call Emma_DP_After
                                                                call Emma_Insert_Ass
                                                        "Just stick a finger in her ass without asking.":
                                                                $ action_context = "auto"
                                                                call Emma_DP_After
                                                                call Emma_Insert_Ass
                                                        "I want to shift the dildo to her ass.":
                                                                $ action_context = "shift"
                                                                call Emma_DP_After
                                                                call Emma_Dildo_Ass
                                                        "Never Mind":
                                                                jump Emma_DP_Cycle
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Shift your focus" if offhand_action:
                                                $ action_context = "shift focus"
                                                call Emma_DP_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not offhand_action:
                                                pass
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [Girl.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(Girl)
                                            "Asks [Girl.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(Girl)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(Girl)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Emma_DP_Cycle
                                            "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_DP_Cycle
                                            "Never mind":
                                                        jump Emma_DP_Cycle
                                    "Undress [Girl.name]":
                                            call Girl_Undress(Girl)
                                    "Clean up [Girl.name] (locked)" if not Girl.Spunk:
                                            pass
                                    "Clean up [Girl.name]" if Girl.Spunk:
                                            call Girl_Cleanup(Girl,"ask")
                                    "Never mind":
                                            jump Emma_DP_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Emma_Pos_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Emma_DP_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Emma_Pos_Reset
                                    $ line = 0
                                    jump Emma_DP_After
        #End menu (if line)

        if Girl.Panties or Girl.PantsNum() > 6 or Girl.HoseNum() >= 5: #This checks if [Girl.name] wants to strip down.
                call Girl_Undress(Girl,"auto")

        call Shift_Focus(Girl)
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
                                call Emma_Pos_Reset
                                return
                            $ Girl.change_stat("lust", 200, 5)
                            if 100 > Girl.lust >= 70 and Girl.OCount < 2:
                                $ Girl.recent_history.append("unsatisfied")
                                $ Girl.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Emma_DP_After
                            $ line = "came"
                    if Girl.lust >= 100:
                            #If [Girl.name] can cum
                            call Girl_Cumming(Girl)
                            if action_context == "shift" or "angry" in Girl.recent_history:
                                jump Emma_DP_After
                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."
                            if "unsatisfied" in Girl.recent_history:#And [Girl.name] is unsatisfied,
                                    "[Girl.name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Emma_DP_After
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if Girl.SEXP >= 100 or ApprovalCheck(Girl, 1200, "LO"):
            pass
        elif counter == (5 + Girl.DildoP):
                    $ Girl.Brows = "confused"
                    ch_e "What are you even doing down there?"
        elif Girl.lust >= 80:
                    pass
        elif counter == (15 + Girl.DildoP) and Girl.SEXP >= 15 and not ApprovalCheck(Girl, 1500):
                    $ Girl.Brows = "confused"
                    menu:
                        ch_e "[Girl.Petname], this is getting uncomfortable, maybe we could try something else."
                        "Finish up.":
                                "You let go. . ."
                                jump Emma_DP_After
                        "Let's try something else." if MultiAction:
                                $ line = 0
                                $ action_context = "shift"
                                jump Emma_DP_After
                        "No, this is fun.":
                                if ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "O"):
                                    $ Girl.change_stat("love", 200, -5)
                                    $ Girl.change_stat("obedience", 50, 3)
                                    $ Girl.change_stat("obedience", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ Girl.change_face("angry", 1)
                                    call Emma_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_e "Well if that's your attitude, I don't need your \"help\"."
                                    $ Girl.change_stat("love", 50, -3, 1)
                                    $ Girl.change_stat("love", 80, -4, 1)
                                    $ Girl.change_stat("obedience", 30, -1, 1)
                                    $ Girl.change_stat("obedience", 50, -1, 1)
                                    $ Girl.recent_history.append("angry")
                                    $ Girl.daily_history.append("angry")
                                    jump Emma_DP_After
        #End Count check

        if Round == 10:
            ch_e "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ Girl.change_face("bemused", 0)
    $ line = 0
    ch_e "Ok, [Girl.Petname], that's enough of that for now."


label Emma_DP_After:
    if not action_context: #fix  action_context != "shift" and action_context != "auto" and action_context != "pullback":
        call Emma_Pos_Reset

    $ Girl.change_face("sexy")

    $ Girl.DildoP += 1
    $ Girl.Action -=1

    call Partner_Like(Girl,1)

    if Girl.DildoP == 1:
            $ Girl.SEXP += 10
            if not action_context:
                if Girl.love >= 500 and "unsatisfied" not in Girl.recent_history:
                    ch_e "I appreciate the work you put in. . ."
                elif Girl.obedience <= 500 and Player.Focus <= 20:
                    $ Girl.change_face("perplexed", 1)
                    ch_e "Did you enjoy that?"

    $ temp_modifier = 0
#    if action_context == "shift":
#        ch_e "Mmm, so what else did you have in mind?"
    call Checkout
    return

# end Girl.Dildo Pussy /////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////Start Insert Ass

label Emma_Dildo_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(Girl)
    call Emma_Dildo_Check
    if not _return:
        return

    if Girl.Loose:
        $ temp_modifier += 30
    elif "anal" in Girl.recent_history or "dildo anal" in Girl.recent_history:
        $ temp_modifier -= 20
    elif "anal" in Girl.daily_history or "dildo anal" in Girl.daily_history:
        $ temp_modifier -= 10
    elif (Girl.Anal + Girl.DildoA + Girl.Plug) > 0: #You've done it before
        $ temp_modifier += 20

    if Girl.PantsNum() >= 6: # she's got pants on.
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

    if "no dildo" in Girl.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no dildo" in Girl.recent_history else 0

    $ Approval = ApprovalCheck(Girl, 1450, TabM = 4) # 145, 160, 175, Taboo -160(355)

    if action_context == Girl:
            #Emma auto-starts
            if Approval > 2:                                                      # fix, add emma auto stuff here
                if Girl.wearing_skirt:
                    "[Girl.name] grabs her dildo, hiking up her skirt as she does."
                    $ Girl.Upskirt = 1
                elif Girl.PantsNum() > 6:
                    "[Girl.name] grabs her dildo, pulling down her pants as she does."
                    $ Girl.Legs = 0
                else:
                    "[Girl.name] grabs her dildo, rubbing is suggestively against her ass."
                $ Girl.SeenPanties = 1
                "She slides the tip against her asshole, and seems to want you to insert it."
                menu:
                    "What do you do?"
                    "Nothing.":
                        $ Girl.change_stat("inhibition", 80, 3)
                        $ Girl.change_stat("inhibition", 50, 2)
                        "[Girl.name] slides it in."
                    "Go for it.":
                        $ Girl.change_face("sexy", 1)
                        $ Girl.change_stat("inhibition", 80, 3)
                        ch_p "Oh yeah, [Girl.Pet], let's do this."
                        $ Girl.nameCheck() #checks reaction to petname
                        "You grab the dildo and slide it in."
                        $ Girl.change_stat("love", 85, 1)
                        $ Girl.change_stat("obedience", 90, 1)
                        $ Girl.change_stat("obedience", 50, 2)
                    "Ask her to stop.":
                        $ Girl.change_face("surprised")
                        $ Girl.change_stat("inhibition", 70, 1)
                        ch_p "Let's not do that right now, [Girl.Pet]."
                        $ Girl.nameCheck() #checks reaction to petname
                        "[Girl.name] sets the dildo down."
                        $ Girl.OutfitChange()
                        $ Girl.change_stat("obedience", 90, 1)
                        $ Girl.change_stat("obedience", 50, 1)
                        $ Girl.change_stat("obedience", 30, 2)
                        return
                jump Emma_DA_Prep
            else:
                $ temp_modifier = 0                               # fix, add emma auto stuff here
                $ offhand_action = 0
            return

    if action_context == "auto":
            "You rub the dildo across her body, and against her tight anus."
            $ Girl.change_face("surprised", 1)

            if (Girl.DildoA and Approval) or (Approval > 1):
                #this is not the first time you've had sex, or she's into it
                "[Girl.name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                $ Girl.change_face("sexy")
                $ Girl.change_stat("obedience", 70, 3)
                $ Girl.change_stat("inhibition", 50, 3)
                $ Girl.change_stat("inhibition", 70, 1)
                ch_e "Mmmm, [Girl.Petname], toys. . ."
                jump Emma_DA_Prep
            else:
                #she's questioning it
                $ Girl.Brows = "angry"
                menu:
                    ch_e "Excuse yourself, what are you planning to do with that?!"
                    "Sorry, sorry! Never mind.":
                        if Approval:
                            $ Girl.change_face("sexy", 1)
                            $ Girl.change_stat("obedience", 70, 3)
                            $ Girl.change_stat("inhibition", 50, 3)
                            $ Girl.change_stat("inhibition", 70, 1)
                            ch_e "Well, now that you mention it. . ."
                            jump Emma_DA_Prep
                        "You pull back before you really get it in."
                        $ Girl.change_face("bemused", 1)
                        if Girl.DildoA:
                            ch_e "Well, [Girl.Petname], maybe warn me next time?"
                        else:
                            ch_e "Well, [Girl.Petname], that's a little much. . . for now . . ."
                    "Just playing with my favorite toys.":
                        $ Girl.change_stat("love", 80, -10, 1)
                        $ Girl.change_stat("love", 200, -10)
                        "You press it inside some more."
                        $ Girl.change_stat("obedience", 70, 3)
                        $ Girl.change_stat("inhibition", 50, 3)
                        if not ApprovalCheck(Girl, 700, "O", TabM=1): #Checks if obedience is 700+
                            $ Girl.change_face("angry")
                            "[Girl.name] shoves you away and slaps you in the face."
                            ch_e "Ask nicely if you want to stick something in my ass!"
                            $ Girl.change_stat("love", 50, -10, 1)
                            $ Girl.change_stat("obedience", 50, 3)
                            $ renpy.pop_call()
                            if action_context:
                                $ renpy.pop_call()
                            if renpy.showing("Emma_SexSprite"):
                                call Emma_Sex_Reset
                            $ Girl.recent_history.append("angry")
                            $ Girl.daily_history.append("angry")
                        else:
                            $ Girl.change_face("sad")
                            "[Girl.name] doesn't seem to be into this, you're lucky she's so obedient."
                            jump Emma_DA_Prep
            return
    #end auto

    if not Girl.DildoA:
            #first time
            $ Girl.change_face("surprised", 1)
            $ Girl.Mouth = "kiss"
            ch_e "Hmm, you don't take half measures. . ."
            if Girl.Forced:
                $ Girl.change_face("sad")
                ch_e "They always go for the butt. . ."

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
                ch_e "I suppose you might enjoy that. . ."
            elif Girl.obedience >= Girl.inhibition:
                $ Girl.change_face("normal")
                ch_e "If that's what you want, [Girl.Petname]. . ."
            else: # Uninhibited
                $ Girl.change_face("sad")
                $ Girl.Mouth = "smile"
                ch_e "I suppose I could enjoy that. . ."

    elif Approval:
            #Second time+ dialog
            if Girl.Forced:
                $ Girl.change_face("sad")
                $ Girl.change_stat("love", 70, -3, 1)
                $ Girl.change_stat("love", 20, -2, 1)
                ch_e "The toys again?"
            elif not Taboo and "tabno" in Girl.daily_history:
                ch_e "Well, at least you got us some privacy this time. . ."
            elif "dildo anal" in Girl.daily_history and not Girl.Loose:
                pass
            elif Girl.DildoA < 3:
                $ Girl.change_face("sexy", 1)
                $ Girl.Brows = "confused"
                $ Girl.Mouth = "kiss"
                ch_e "You want to stick it in my ass again?"
            else:
                $ Girl.change_face("sexy", 1)
                $ Girl.ArmPose = 2
                $ line = renpy.random.choice(["You want some of this action?",
                    "So you'd like another go?",
                    "You'd like to stick it in my ass again?",
                    "You'd like me to lube up your toy?"])
                ch_e "[line]"
                $ line = 0

    if Approval >= 2:
            #She's into it. . .
            if Girl.Forced:
                $ Girl.change_face("sad")
                $ Girl.change_stat("obedience", 90, 1)
                $ Girl.change_stat("inhibition", 60, 1)
                ch_e "Oh, fine."
            else:
                $ Girl.change_face("sexy", 1)
                $ Girl.change_stat("love", 90, 1)
                $ Girl.change_stat("inhibition", 50, 3)
                $ line = renpy.random.choice(["Well, sure, stick it in.",
                    "Hmm. . . ok.",
                    "Sure!",
                    "I guess I could. . . stick it in.",
                    "Delightful.",
                    "Hmm, ok, ok."])
                ch_e "[line]"
                $ line = 0
            $ Girl.change_stat("obedience", 20, 1)
            $ Girl.change_stat("obedience", 60, 1)
            $ Girl.change_stat("inhibition", 70, 2)
            jump Emma_DA_Prep

    else:
            #She's not into it, but maybe. . .
            $ Girl.change_face("angry")
            if "no dildo" in Girl.recent_history:
                ch_e "What part of \"no,\" did you not get, [Girl.Petname]?"
            elif Taboo and "tabno" in Girl.daily_history and "no dildo" in Girl.daily_history:
                ch_e "Stop swinging that thing around in public!"
            elif "no dildo" in Girl.daily_history:
                ch_e "I already told you \"no,\" [Girl.Petname]."
            elif Taboo and "tabno" in Girl.daily_history:
                ch_e "I already told you that I wouldn't do that out here!"
            elif not Girl.DildoA:
                $ Girl.change_face("bemused")
                ch_e "I'm just not into toys, [Girl.Petname]. . ."
            else:
                $ Girl.change_face("bemused")
                ch_e "I don't think we need any toys, [Girl.Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in Girl.daily_history:
                    $ Girl.change_face("bemused")
                    ch_e "I'm sure, [Girl.Petname]."
                    return
                "Maybe later?" if "no dildo" not in Girl.daily_history:
                    $ Girl.change_face("sexy")
                    ch_e "Perhaps I'll practice on my own time, [Girl.Petname]."
                    $ Girl.change_stat("love", 80, 2)
                    $ Girl.change_stat("inhibition", 70, 2)
                    if Taboo:
                        $ Girl.recent_history.append("tabno")
                        $ Girl.daily_history.append("tabno")
                    $ Girl.recent_history.append("no dildo")
                    $ Girl.daily_history.append("no dildo")
                    return
                "I think you'd like it. . .":
                    if Approval:
                        $ Girl.change_face("sexy")
                        $ Girl.change_stat("obedience", 90, 2)
                        $ Girl.change_stat("obedience", 50, 2)
                        $ Girl.change_stat("inhibition", 70, 3)
                        $ Girl.change_stat("inhibition", 40, 2)
                        $ line = renpy.random.choice(["Very well, stick it in.",
                            "I suppose. . .",
                            "You make a compelling argument."])
                        ch_e "[line]"
                        $ line = 0
                        jump Emma_DA_Prep
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
                        jump Emma_DA_Prep
                    else:
                        $ Girl.change_stat("love", 200, -20)
                        $ Girl.recent_history.append("angry")
                        $ Girl.daily_history.append("angry")

    #She refused all offers.
    $ Girl.ArmPose = 1
    if "no dildo" in Girl.daily_history:

            $ Girl.recent_history.append("angry")
            $ Girl.daily_history.append("angry")
    elif Girl.Forced:
            $ Girl.change_face("angry", 1)
            ch_e "I'm not going to let you use that on me."
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
            ch_e "Not here!"
            $ Girl.change_stat("lust", 200, 5)
            $ Girl.change_stat("obedience", 50, -3)
    elif Girl.DildoA:
            $ Girl.change_face("sad")
            ch_e "Sorry, you can keep your toys out of there."
    else:
            $ Girl.change_face("normal", 1)
            ch_e "No, thank you."
    $ Girl.recent_history.append("no dildo")
    $ Girl.daily_history.append("no dildo")
    $ temp_modifier = 0
    return

label Emma_DA_Prep: #Animation set-up
    if offhand_action == "dildo anal":
        return

    if not Girl.Forced and action_context != "auto":
        $ temp_modifier = 20 if Girl.PantsNum() > 6 else 0
        call Bottoms_Off(Girl)
        if "angry" in Girl.recent_history:
            return

    $ temp_modifier = 0
    call Emma_Pussy_Launch("dildo anal")
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
    $ Girl.DrainWord("no dildo")
    $ Girl.recent_history.append("dildo anal")
    $ Girl.daily_history.append("dildo anal")

label Emma_DA_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(Girl)
        call Emma_Pussy_Launch("dildo anal")
        $ Girl.lustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                call Slap_Ass(Girl)
                                jump Emma_DA_Cycle

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
                                            if Girl.Action and MultiAction:
                                                call Offhand_Set
                                                if offhand_action:
                                                     $ Girl.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Shift primary action":
                                            if Girl.Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in her pussy.":
                                                                $ action_context = "shift"
                                                                call Emma_DA_After
                                                                call Emma_Fondle_Pussy
                                                        "Just stick a finger in her pussy without asking.":
                                                                $ action_context = "auto"
                                                                call Emma_DA_After
                                                                call Emma_Fondle_Pussy
                                                        "I want to shift the dildo to her pussy.":
                                                                $ action_context = "shift"
                                                                call Emma_DA_After
                                                                call Emma_Dildo_Pussy
                                                        "Never Mind":
                                                                jump Emma_DA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Shift your focus" if offhand_action:
                                                $ action_context = "shift focus"
                                                call Emma_DA_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not offhand_action:
                                                pass
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [Girl.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(Girl)
                                            "Asks [Girl.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(Girl)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(Girl)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Emma_DA_Cycle
                                            "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_DA_Cycle
                                            "Never mind":
                                                        jump Emma_DA_Cycle
                                    "Undress [Girl.name]":
                                            call Girl_Undress(Girl)
                                    "Clean up [Girl.name] (locked)" if not Girl.Spunk:
                                            pass
                                    "Clean up [Girl.name]" if Girl.Spunk:
                                            call Girl_Cleanup(Girl,"ask")
                                    "Never mind":
                                            jump Emma_DA_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Emma_Pos_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Emma_DA_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Emma_Pos_Reset
                                    $ line = 0
                                    jump Emma_DA_After
        #End menu (if line)

        if Girl.Panties or Girl.PantsNum() > 6 or Girl.HoseNum() >= 5: #This checks if [Girl.name] wants to strip down.
                call Girl_Undress(Girl,"auto")

        call Shift_Focus(Girl)
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
                                call Emma_Pos_Reset
                                return
                            $ Girl.change_stat("lust", 200, 5)
                            if 100 > Girl.lust >= 70 and Girl.OCount < 2:
                                $ Girl.recent_history.append("unsatisfied")
                                $ Girl.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Emma_DA_After
                            $ line = "came"

                    if Girl.lust >= 100:
                            #If [Girl.name] can cum
                            call Girl_Cumming(Girl)
                            if action_context == "shift" or "angry" in Girl.recent_history:
                                jump Emma_DA_After

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in Girl.recent_history:#And [Girl.name] is unsatisfied,
                                    "[Girl.name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Emma_DA_After
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if Girl.SEXP >= 100 or ApprovalCheck(Girl, 1200, "LO"):
            pass
        elif counter == (5 + Girl.DildoA):
                    $ Girl.Brows = "confused"
                    ch_e "What are you even doing down there?"
        elif Girl.lust >= 80:
                    pass
        elif counter == (15 + Girl.DildoA) and Girl.SEXP >= 15 and not ApprovalCheck(Girl, 1500):
                    $ Girl.Brows = "confused"
                    menu:
                        ch_e "[Girl.Petname], this is getting uncomfortable, maybe we could try something else."
                        "Finish up.":
                                "You let go. . ."
                                jump Emma_DA_After
                        "Let's try something else." if MultiAction:
                                $ line = 0
                                $ action_context = "shift"
                                jump Emma_DA_After
                        "No, this is fun.":
                                if ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "O"):
                                    $ Girl.change_stat("love", 200, -5)
                                    $ Girl.change_stat("obedience", 50, 3)
                                    $ Girl.change_stat("obedience", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ Girl.change_face("angry", 1)
                                    call Emma_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_e "Well if that's your attitude, I don't need your \"help\"."
                                    $ Girl.change_stat("love", 50, -3, 1)
                                    $ Girl.change_stat("love", 80, -4, 1)
                                    $ Girl.change_stat("obedience", 30, -1, 1)
                                    $ Girl.change_stat("obedience", 50, -1, 1)
                                    $ Girl.recent_history.append("angry")
                                    $ Girl.daily_history.append("angry")
                                    jump Emma_DA_After
        #End Count check

        if Round == 10:
            ch_e "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ Girl.change_face("bemused", 0)
    $ line = 0
    ch_e "Ok, [Girl.Petname], that's enough of that for now."


label Emma_DA_After:
    if not action_context: #fix  action_context != "shift" and action_context != "auto" and action_context != "pullback":
        call Emma_Pos_Reset

    $ Girl.change_face("sexy")

    $ Girl.DildoA += 1
    $ Girl.Action -=1

    call Partner_Like(Girl,1)

    if Girl.DildoA == 1:
            $ Girl.SEXP += 10
            if not action_context:
                if Girl.love >= 500 and "unsatisfied" not in Girl.recent_history:
                    ch_e "That was. . . engaging. . ."
                elif Girl.obedience <= 500 and Player.Focus <= 20:
                    $ Girl.change_face("perplexed", 1)
                    ch_e "Did you enjoy that?"

    $ temp_modifier = 0
#    if action_context == "shift":
#        ch_e "Mmm, so what else did you have in mind?"
    call Checkout
    return

# end Girl.Dildo Ass /////////////////////////////////////////////////////////////////////////////

label Emma_Vibrator_Check:                                                                                 #fix this whole section is copy/paste unfinished
    if "vibrator" in Player.Inventory:
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in Girl.Inventory:
        "You ask [Girl.name] to get out her vibrator."
    else:
        "You don't have one of those on you."
        return 0
    return 1

## Girl.Footjob //////////////////////////////////////////////////////////////////////
label Emma_Footjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(Girl)
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

    if "no foot" in Girl.daily_history:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no foot" in Girl.recent_history else 0

    $ Approval = ApprovalCheck(Girl, 1250, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if action_context == Girl:                                                                  #Emma auto-starts
        if Approval > 2:                                                      # fix, add emma auto stuff here
            if offhand_action == "jackin":
                "[Girl.name] sits back and starts rubbing her foot along your cock."
            else:
                "[Girl.name] gives you a mischevious smile, and starts to rub her foot along your cock."
            menu:
                "What do you do?"
                "Nothing.":
                    $ Girl.change_stat("inhibition", 70, 3)
                    $ Girl.change_stat("inhibition", 30, 2)
                    "[Girl.name] continues her actions."
                "Praise her.":
                    $ Girl.change_face("sexy", 1)
                    $ Girl.change_stat("inhibition", 70, 3)
                    ch_p "Oooh, that's good, [Girl.Pet]."
                    $ Girl.nameCheck() #checks reaction to petname
                    "[Girl.name] continues her actions."
                    $ Girl.change_stat("love", 80, 1)
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 2)
                "Ask her to stop.":
                    $ Girl.change_face("surprised")
                    $ Girl.change_stat("inhibition", 70, 1)
                    ch_p "Let's not do that for now, [Girl.Pet]."
                    $ Girl.nameCheck() #checks reaction to petname
                    "[Girl.name] puts it down."
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Girl.change_stat("obedience", 30, 2)
                    return
            if primary_action:
                $ girl_offhand_action = "foot"
                return
            jump Emma_FJ_Prep
        else:
            $ temp_modifier = 0                               # fix, add emma auto stuff here
            $ offhand_action = 0
            return

    if not Girl.Foot and "no foot" not in Girl.recent_history:
        $ Girl.change_face("confused", 2)
        ch_e "Mmm, so you're into feet then, [Girl.Petname]?"
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
            ch_e "I suppose it couldn't hurt. . ."
        elif Girl.obedience >= Girl.inhibition:
            $ Girl.change_face("normal",1)
            ch_e "If you enjoy that, [Girl.Petname]. . ."
        elif Girl.Addict >= 50:
            $ Girl.change_face("manic", 1)
            ch_e "Very well. . ."
        else: # Uninhibited
            $ Girl.change_face("lipbite",1)
            ch_e "Very well. . ."

    elif Approval:                                                                       #Second time+ dialog
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
            ch_e "That's it?"
        elif not Taboo and "tabno" in Girl.daily_history:
            ch_e "Um, I suppose this is secluded enough. . ."
        elif "foot" in Girl.recent_history:
            $ Girl.change_face("sexy", 1)
            ch_e "You know, heels are nightmare on the arches. . ."
            jump Emma_FJ_Prep
        elif "foot" in Girl.daily_history:
            $ Girl.change_face("sexy", 1)
            $ line = renpy.random.choice(["Another?",
                "I'd rather not get calluses.",
                "Didn't get enough earlier?",
                "My feet are rather sore from earlier.",
                "My feet are rather sore from earlier."])
            ch_e "[line]"
        elif Girl.Foot < 3:
            $ Girl.change_face("sexy", 1)
            $ Girl.Brows = "confused"
            $ Girl.Mouth = "kiss"
            ch_e "Oh, very well. . ."
        else:
            $ Girl.change_face("sexy", 1)
            $ Girl.ArmPose = 2
            $ line = renpy.random.choice(["You'd like me to use my feet again?",
                "So you'd like another footjob?",
                "Mmmm, some. . . [she rubs her foot along your leg]?",
                "A little foot rub?"])
            ch_e "[line]"
        $ line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if Girl.Forced:
            $ Girl.change_face("sad")
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 60, 1)
            ch_e "Oh, fine."
        elif "no foot" in Girl.daily_history:
            ch_e "Oh, very well."
        else:
            $ Girl.change_face("sexy", 1)
            $ Girl.change_stat("love", 90, 1)
            $ Girl.change_stat("inhibition", 50, 3)
            $ line = renpy.random.choice(["Sure, I suppose.",
                "Fine.",
                "Very well, bring it out.",
                "I suppose I could. . .",
                "Fine. . . [She gestures for you to come over].",
                "Hmm, ok."])
            ch_e "[line]"
            $ line = 0
        $ Girl.change_stat("obedience", 20, 1)
        $ Girl.change_stat("obedience", 60, 1)
        $ Girl.change_stat("inhibition", 70, 2)
        jump Emma_FJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ Girl.change_face("angry")
        if "no foot" in Girl.recent_history:
            ch_e "Pay attention, [Girl.Petname]."
        elif Taboo and "tabno" in Girl.daily_history and "no foot" in Girl.daily_history:
            ch_e "I refuse to do this in public."
        elif "no foot" in Girl.daily_history:
            ch_e "I said \"no,\" [Girl.Petname]."
        elif Taboo and "tabno" in Girl.daily_history:
            ch_e "I told you, not in public!"
        elif not Girl.Foot:
            $ Girl.change_face("bemused")
            ch_e "I'm unsure, [Girl.Petname]. . ."
        else:
            $ Girl.change_face("bemused")
            ch_e "Not now, [Girl.Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no foot" in Girl.daily_history:
                $ Girl.change_face("bemused")
                ch_e "Thank you."
                return
            "Maybe later?" if "no foot" not in Girl.daily_history:
                $ Girl.change_face("sexy")
                ch_e ". . ."
                ch_e "Perhaps."
                $ Girl.change_stat("love", 80, 2)
                $ Girl.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ Girl.recent_history.append("tabno")
                    $ Girl.daily_history.append("tabno")
                $ Girl.recent_history.append("no foot")
                $ Girl.daily_history.append("no foot")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ Girl.change_face("sexy")
                    $ Girl.change_stat("obedience", 90, 2)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("inhibition", 70, 3)
                    $ Girl.change_stat("inhibition", 40, 2)
                    $ line = renpy.random.choice(["Sure, I suppose.",
                            "Fine.",
                            "Very well, bring it out.",
                            "I suppose I could. . .",
                            "Fine. . . [She gestures for you to come over].",
                            "Hmm, ok."])
                    ch_e "[line]"
                    $ line = 0
                    jump Emma_FJ_Prep
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
                    jump Emma_FJ_Prep
                else:
                    $ Girl.change_stat("love", 200, -15)
                    $ Girl.recent_history.append("angry")
                    $ Girl.daily_history.append("angry")

    #She refused all offers.
    $ Girl.ArmPose = 1
    if "no foot" in Girl.daily_history:
        $ Girl.change_face("angry", 1)
        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
    elif Girl.Forced:
        $ Girl.change_face("angry", 1)
        ch_e "You really don't want my heels near your manhood."
        $ Girl.change_stat("lust", 200, 5)
        if Girl.love > 300:
                $ Girl.change_stat("love", 70, -2)
        $ Girl.change_stat("obedience", 50, -2)
        $ Girl.recent_history.append("angry")
        $ Girl.daily_history.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ Girl.change_face("angry", 1)
        $ Girl.daily_history.append("tabno")
        ch_e "This truly isn't an appropriate place for that."
        $ Girl.change_stat("lust", 200, 5)
        $ Girl.change_stat("obedience", 50, -3)
    elif Girl.Foot:
        $ Girl.change_face("sad")
        ch_e "I'm not in the mood, [Girl.Petname]. . ."
    else:
        $ Girl.change_face("normal", 1)
        ch_e "I'm not in the mood for footplay today. . ."
    $ Girl.recent_history.append("no foot")
    $ Girl.daily_history.append("no foot")
    $ temp_modifier = 0
    return


label Emma_FJ_Prep:
    if offhand_action == "foot":
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

    call Seen_First_Peen(Girl,Partner,React=action_context)
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
    $ Girl.DrainWord("no foot")
    $ Girl.recent_history.append("foot")
    $ Girl.daily_history.append("foot")
    ch_e "Did you want me facing you, or from behind?"
    menu:
        extend ""
        "Facing me":
                $ Girl.Pose = "foot"
        "From behind.":
                $ Girl.Pose = "doggy"

label Emma_FJ_Cycle:
    while Round > 0:
        call Shift_Focus(Girl)
        call Emma_FJ_Launch
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

                        "Turn her Around":
                                    $ Girl.Pose = "doggy" if Girl.Pose != "doggy" else "foot"
                                    "You turn her around. . ."
                                    jump Emma_FJ_Cycle


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
                                    "I also want to fondle her thighs." if offhand_action != "fondle thighs":
                                            if MultiAction:
                                                $ offhand_action = "fondle thighs"
                                                "You start to fondle her thighs."
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Shift primary action":
                                            if Girl.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                    if Girl.Action and MultiAction:
                                                                        $ action_context = "shift"
                                                                        call Emma_FJ_After
                                                                        call Emma_Blowjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(Girl,"tired")
                                                        "How about a handjob?":
                                                                    if Girl.Action and MultiAction:
                                                                        $ action_context = "shift"
                                                                        call Emma_FJ_After
                                                                        call Emma_Handjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(Girl,"tired")

                                                        "How about a titjob?":
                                                                    if Girl.Action and MultiAction:
                                                                        $ action_context = "shift"
                                                                        call Emma_FJ_After
                                                                        call Emma_Titjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(Girl,"tired")

                                                        "Never Mind":
                                                                jump Emma_FJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(Girl,"tired")

                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Asks [Girl.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                                        call Les_Change(Girl)
                                            "Asks [Girl.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                                        pass
                                            "Ask [Partner.name] to do something else":
                                                        call Three_Change(Girl)

                                            "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                        $ position_change_timer = 0
                                            "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        $ position_change_timer = 0

                                            "Swap to [Partner.name]":
                                                        call primary_action_Swap(Girl)
                                            "Undress [Partner.name]":
                                                        call Girl_Undress(Partner)
                                                        jump Emma_FJ_Cycle
                                            "Clean up [Partner.name] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Clean up [Partner.name]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Emma_FJ_Cycle
                                            "Never mind":
                                                        jump Emma_FJ_Cycle
                                    "Undress [Girl.name]":
                                            call Girl_Undress(Girl)
                                    "Clean up [Girl.name] (locked)" if not Girl.Spunk:
                                            pass
                                    "Clean up [Girl.name]" if Girl.Spunk:
                                            call Girl_Cleanup(Girl,"ask")
                                    "Never mind":
                                            jump Emma_FJ_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Emma_FJ_Reset
                                    $ action_context = "shift"
                                    $ line = 0
                                    jump Emma_FJ_After
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Emma_FJ_Reset
                                    $ line = 0
                                    jump Emma_FJ_After
        #End menu (if line)

        call Shift_Focus(Girl)
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
                                call Emma_FJ_Reset
                                return
                            $ Girl.change_stat("lust", 200, 5)
                            if 100 > Girl.lust >= 70 and Girl.OCount < 2:
                                $ Girl.recent_history.append("unsatisfied")
                                $ Girl.daily_history.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Emma_FJ_After
                            $ line = "came"

                    if Girl.lust >= 100:
                            #If [Girl.name] can cum
                            call Girl_Cumming(Girl)
                            if action_context == "shift" or "angry" in Girl.recent_history:
                                jump Emma_FJ_After

                    if line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in Girl.recent_history:#And [Girl.name] is unsatisfied,
                                    "[Girl.name] still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ line = "You get back into it"
                                        "No, I'm done.":
                                            "You pull back."
                                            jump Emma_FJ_After
        if Partner and Partner.lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if counter == 20:
                    $ Girl.Brows = "angry"
                    menu:
                        ch_e "Hmm, foot cramp, could we take a short break?"
                        "How about a BJ?" if Girl.Action and MultiAction:
                                $ action_context = "shift"
                                call Emma_FJ_After
                                call Emma_Blowjob
                        "How about a Handy?" if Girl.Action and MultiAction:
                                $ action_context = "shift"
                                call Emma_FJ_After
                                call Emma_Handjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ counter += 1
                                "[line]"
                                jump Emma_FJ_Cycle
                        "Let's try something else." if MultiAction:
                                $ line = 0
                                call Emma_Sex_Reset
                                $ action_context = "shift"
                                jump Emma_FJ_After
                        "No, keep going.":
                                if ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "O"):
                                    $ Girl.change_stat("love", 200, -5)
                                    $ Girl.change_stat("obedience", 50, 3)
                                    $ Girl.change_stat("obedience", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    $ Girl.change_face("angry", 1)
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_e "I do have better things I could be doing."
                                    $ Girl.change_stat("love", 50, -3, 1)
                                    $ Girl.change_stat("love", 80, -4, 1)
                                    $ Girl.change_stat("obedience", 30, -1, 1)
                                    $ Girl.change_stat("obedience", 50, -1, 1)
                                    $ Girl.recent_history.append("angry")
                                    $ Girl.daily_history.append("angry")
                                    jump Emma_FJ_After
        elif counter == 10 and Girl.SEXP <= 100 and not ApprovalCheck(Girl, 1200, "LO"):
                    $ Girl.Brows = "confused"
                    ch_e "Could we be done here, my feet are getting sore."
        #End Count check

        call Escalation(Girl) #sees if she wants to escalate things

        if Round == 10:
            ch_e "Ok, it's getting a bit late here."
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ Girl.change_face("bemused", 0)
    $ line = 0
    ch_e "Ok, [Girl.Petname], that's enough of that for now."

label Emma_FJ_After:
    $ Girl.change_face("sexy")

    $ Girl.Foot += 1
    $ Girl.Action -=1
    $ Girl.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ Girl.Addictionrate += 1
    $ Girl.change_stat("lust", 90, 5)

    call Partner_Like(Girl,1)

    if "Emmapedi" in Achievements:
            pass
    elif Girl.Foot >= 10:
            $ Girl.change_face("smile", 1)
            ch_e "I'm glad that you enjoy my feet."
            ch_e "They've been trained well over the years."
            $ Achievements.append("Emmapedi")
            $ Girl.SEXP += 5
    elif Girl.Foot == 1:
            $ Girl.SEXP += 10
            if Girl.love >= 500:
                $ Girl.Mouth = "smile"
                ch_e "Your cock was so warm . ."
            elif Player.Focus <= 20:
                $ Girl.Mouth = "sad"
                ch_e "Did you enjoy that?"
    elif Girl.Foot == 5:
                ch_e "I'm enjoying this experience."

    $ temp_modifier = 0
    if action_context == "shift":
        ch_e "Ok then, what were you thinking?"
    else:
        call Emma_Sex_Reset
    call Checkout
    return

## end Girl.Footjob //////////////////////////////////////////////////////////////////////
